"""
Telegram ID Finder - FastAPI Application
Telegram ID 查詢器 - FastAPI 應用程式

A web tool to find Telegram group/channel/user IDs for configuration.
網頁工具：取得 Telegram 群組、頻道、用戶 ID 用於設定。
"""

import os
from contextlib import asynccontextmanager
from typing import Optional
from dataclasses import asdict

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import yaml

from dotenv import load_dotenv

from .telegram_service import (
    TelegramService,
    get_telegram_service,
    set_telegram_service,
    DialogInfo,
    SenderInfo,
)

# Load environment variables | 載入環境變數
load_dotenv()


# ============================================================================
# Pydantic Models | Pydantic 模型
# ============================================================================

class SendCodeRequest(BaseModel):
    """Request model for sending verification code | 發送驗證碼的請求模型"""
    phone: str
    api_id: Optional[int] = None
    api_hash: Optional[str] = None


class VerifyCodeRequest(BaseModel):
    """Request model for verifying code | 驗證碼的請求模型"""
    code: str
    password: Optional[str] = None


class GenerateConfigRequest(BaseModel):
    """Request model for generating config | 產生設定的請求模型"""
    chats: list[dict]  # List of {id, name} | {id, name} 列表
    senders: list[dict]  # List of {id, name, chat_id} | {id, name, chat_id} 列表


# ============================================================================
# Application Lifecycle | 應用程式生命週期
# ============================================================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan handler.
    應用程式生命週期處理器。
    """
    # Startup | 啟動
    api_id = os.getenv("TELEGRAM_API_ID")
    api_hash = os.getenv("TELEGRAM_API_HASH")
    session_name = os.getenv("TELEGRAM_SESSION_NAME", "telegram_id_finder")

    if api_id and api_hash:
        service = TelegramService(
            api_id=int(api_id),
            api_hash=api_hash,
            session_name=session_name
        )
        set_telegram_service(service)
        await service.start()

    yield

    # Shutdown | 關閉
    service = get_telegram_service()
    if service:
        await service.stop()


# ============================================================================
# FastAPI Application | FastAPI 應用程式
# ============================================================================

app = FastAPI(
    title="Telegram ID Finder",
    description="Web tool to find Telegram group/channel/user IDs | 網頁工具：取得 Telegram ID",
    version="1.0.0",
    lifespan=lifespan
)

# Templates configuration | 模板設定
templates = Jinja2Templates(
    directory=os.path.join(os.path.dirname(__file__), "templates")
)


# ============================================================================
# Helper Functions | 輔助函式
# ============================================================================

def get_service_or_error() -> TelegramService:
    """
    Get the Telegram service or raise an error.
    取得 Telegram 服務或拋出錯誤。
    """
    service = get_telegram_service()
    if not service:
        raise HTTPException(
            status_code=503,
            detail="Telegram service not initialized. Please set API credentials. | "
                   "Telegram 服務未初始化，請設定 API 憑證。"
        )
    return service


# ============================================================================
# Frontend Routes | 前端路由
# ============================================================================

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """
    Render the main page.
    渲染主頁面。
    """
    return templates.TemplateResponse("index.html", {"request": request})


# ============================================================================
# Authentication API | 認證 API
# ============================================================================

@app.post("/api/auth/send-code")
async def send_code(request: SendCodeRequest):
    """
    Send verification code to phone number.
    發送驗證碼到手機號碼。

    If api_id and api_hash are provided, initialize a new service.
    如果提供了 api_id 和 api_hash，則初始化新服務。
    """
    # If credentials provided, create new service | 如果提供憑證，建立新服務
    if request.api_id and request.api_hash:
        session_name = os.getenv("TELEGRAM_SESSION_NAME", "telegram_id_finder")
        service = TelegramService(
            api_id=request.api_id,
            api_hash=request.api_hash,
            session_name=session_name
        )
        set_telegram_service(service)
        await service.start()
    else:
        service = get_service_or_error()

    result = await service.send_code(request.phone)
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])

    return result


@app.post("/api/auth/verify")
async def verify_code(request: VerifyCodeRequest):
    """
    Verify the login code.
    驗證登入碼。
    """
    service = get_service_or_error()
    result = await service.verify_code(request.code, request.password)

    if not result["success"] and not result.get("needs_2fa"):
        raise HTTPException(status_code=400, detail=result["message"])

    return result


@app.get("/api/auth/status")
async def auth_status():
    """
    Get current authentication status.
    取得當前認證狀態。
    """
    service = get_telegram_service()
    if not service:
        return {
            "is_logged_in": False,
            "message": "Service not initialized. Please provide API credentials. | "
                       "服務未初始化，請提供 API 憑證。"
        }

    return await service.get_status()


@app.post("/api/auth/logout")
async def logout():
    """
    Log out from Telegram.
    從 Telegram 登出。
    """
    service = get_service_or_error()
    result = await service.logout()

    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])

    return result


# ============================================================================
# Dialogs API | 對話 API
# ============================================================================

@app.get("/api/dialogs")
async def get_dialogs():
    """
    Get all groups and channels.
    取得所有群組和頻道。
    """
    service = get_service_or_error()
    status = await service.get_status()

    if not status.get("is_logged_in"):
        raise HTTPException(
            status_code=401,
            detail="Not logged in | 未登入"
        )

    dialogs = await service.get_dialogs()
    return {
        "dialogs": [asdict(d) for d in dialogs]
    }


@app.get("/api/dialogs/{chat_id}/messages")
async def get_dialog_messages(chat_id: int, limit: int = 100):
    """
    Get recent message senders from a chat.
    從聊天中取得最近的訊息發送者。

    Args:
        chat_id: The chat/group/channel ID
        limit: Maximum messages to fetch (default 100) | 最大訊息數（預設 100）
    """
    service = get_service_or_error()
    status = await service.get_status()

    if not status.get("is_logged_in"):
        raise HTTPException(
            status_code=401,
            detail="Not logged in | 未登入"
        )

    # Limit the maximum to prevent abuse | 限制最大值以防止濫用
    limit = min(limit, 500)

    senders = await service.get_messages_senders(chat_id, limit)
    return {
        "chat_id": chat_id,
        "senders": [asdict(s) for s in senders]
    }


# ============================================================================
# Config Generation API | 設定產生 API
# ============================================================================

@app.post("/api/generate-config")
async def generate_config(request: GenerateConfigRequest):
    """
    Generate settings.yaml content for telegram-signal-parser.
    為 telegram-signal-parser 產生 settings.yaml 內容。
    """
    # Build the config structure | 建立設定結構
    config = {
        "telegram": {
            "chats": []
        }
    }

    # Group senders by chat | 按聊天分組發送者
    senders_by_chat = {}
    for sender in request.senders:
        chat_id = sender.get("chat_id")
        if chat_id not in senders_by_chat:
            senders_by_chat[chat_id] = []
        senders_by_chat[chat_id].append({
            "id": sender["id"],
            "name": sender.get("name", "")
        })

    # Build chat configurations | 建立聊天設定
    for chat in request.chats:
        chat_config = {
            "id": chat["id"],
            "name": chat.get("name", ""),
        }

        # Add senders if any selected for this chat
        # 如果此聊天有選擇的發送者則加入
        if chat["id"] in senders_by_chat:
            chat_config["senders"] = senders_by_chat[chat["id"]]

        config["telegram"]["chats"].append(chat_config)

    # Convert to YAML | 轉換為 YAML
    yaml_content = yaml.dump(
        config,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False
    )

    return {
        "yaml": yaml_content,
        "config": config
    }


# ============================================================================
# Entry Point | 程式進入點
# ============================================================================

if __name__ == "__main__":
    import uvicorn

    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", "8000"))

    uvicorn.run(
        "app.main:app",
        host=host,
        port=port,
        reload=True
    )
