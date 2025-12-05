"""
Telegram Service | Telegram 服務
Encapsulates all Telethon operations for Telegram API interactions.
封裝所有 Telethon 操作以進行 Telegram API 互動。
"""

import os
import asyncio
from typing import Optional
from dataclasses import dataclass
from enum import Enum

from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.types import (
    User,
    Chat,
    Channel,
    Message,
    PeerUser,
    PeerChat,
    PeerChannel,
)
from telethon.errors import (
    SessionPasswordNeededError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    FloodWaitError,
    AuthKeyUnregisteredError,
)


class DialogType(str, Enum):
    """Dialog type enumeration | 對話類型枚舉"""
    GROUP = "group"
    CHANNEL = "channel"
    USER = "user"
    BOT = "bot"
    UNKNOWN = "unknown"


@dataclass
class DialogInfo:
    """Dialog information structure | 對話資訊結構"""
    id: int
    name: str
    dialog_type: DialogType
    username: Optional[str] = None
    members_count: Optional[int] = None


@dataclass
class SenderInfo:
    """Message sender information | 訊息發送者資訊"""
    id: int
    name: str
    username: Optional[str] = None
    is_bot: bool = False


@dataclass
class AuthState:
    """Authentication state | 認證狀態"""
    is_logged_in: bool = False
    phone_code_hash: Optional[str] = None
    phone_number: Optional[str] = None
    needs_2fa: bool = False
    user_id: Optional[int] = None
    user_name: Optional[str] = None


class TelegramService:
    """
    Telegram service class for handling all Telegram operations.
    Telegram 服務類別，處理所有 Telegram 操作。
    """

    def __init__(self, api_id: int, api_hash: str, session_name: str = "session"):
        """
        Initialize the Telegram service.
        初始化 Telegram 服務。

        Args:
            api_id: Telegram API ID
            api_hash: Telegram API Hash
            session_name: Name for the session file | Session 檔案名稱
        """
        self.api_id = api_id
        self.api_hash = api_hash
        self.session_name = session_name
        self._client: Optional[TelegramClient] = None
        self._auth_state = AuthState()

    @property
    def client(self) -> Optional[TelegramClient]:
        """Get the Telegram client | 取得 Telegram 客戶端"""
        return self._client

    @property
    def auth_state(self) -> AuthState:
        """Get current authentication state | 取得當前認證狀態"""
        return self._auth_state

    async def start(self) -> None:
        """
        Start the Telegram client connection.
        啟動 Telegram 客戶端連線。
        """
        if self._client is None:
            self._client = TelegramClient(
                self.session_name,
                self.api_id,
                self.api_hash
            )

        await self._client.connect()

        # Check if already authorized | 檢查是否已授權
        if await self._client.is_user_authorized():
            me = await self._client.get_me()
            self._auth_state = AuthState(
                is_logged_in=True,
                user_id=me.id,
                user_name=self._get_display_name(me)
            )

    async def stop(self) -> None:
        """
        Stop the Telegram client connection.
        停止 Telegram 客戶端連線。
        """
        if self._client:
            await self._client.disconnect()

    async def send_code(self, phone: str) -> dict:
        """
        Send verification code to phone number.
        發送驗證碼到手機號碼。

        Args:
            phone: Phone number with country code | 帶國碼的手機號碼

        Returns:
            dict with status and message | 包含狀態和訊息的字典
        """
        if not self._client:
            await self.start()

        try:
            result = await self._client.send_code_request(phone)
            self._auth_state.phone_code_hash = result.phone_code_hash
            self._auth_state.phone_number = phone
            return {
                "success": True,
                "message": "Verification code sent | 驗證碼已發送"
            }
        except FloodWaitError as e:
            return {
                "success": False,
                "message": f"Too many requests. Wait {e.seconds} seconds | 請求過多，請等待 {e.seconds} 秒"
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"Failed to send code: {str(e)} | 發送驗證碼失敗：{str(e)}"
            }

    async def verify_code(self, code: str, password: Optional[str] = None) -> dict:
        """
        Verify the login code (and 2FA password if needed).
        驗證登入碼（如有需要則驗證 2FA 密碼）。

        Args:
            code: Verification code | 驗證碼
            password: 2FA password if required | 如需要則提供 2FA 密碼

        Returns:
            dict with status and message | 包含狀態和訊息的字典
        """
        if not self._client or not self._auth_state.phone_number:
            return {
                "success": False,
                "message": "No pending verification | 無待驗證的請求"
            }

        try:
            await self._client.sign_in(
                phone=self._auth_state.phone_number,
                code=code,
                phone_code_hash=self._auth_state.phone_code_hash
            )

            me = await self._client.get_me()
            self._auth_state = AuthState(
                is_logged_in=True,
                user_id=me.id,
                user_name=self._get_display_name(me)
            )

            return {
                "success": True,
                "message": "Login successful | 登入成功",
                "user": {
                    "id": me.id,
                    "name": self._get_display_name(me)
                }
            }

        except SessionPasswordNeededError:
            # 2FA is enabled | 已啟用 2FA
            if password:
                try:
                    await self._client.sign_in(password=password)
                    me = await self._client.get_me()
                    self._auth_state = AuthState(
                        is_logged_in=True,
                        user_id=me.id,
                        user_name=self._get_display_name(me)
                    )
                    return {
                        "success": True,
                        "message": "Login successful | 登入成功",
                        "user": {
                            "id": me.id,
                            "name": self._get_display_name(me)
                        }
                    }
                except Exception as e:
                    return {
                        "success": False,
                        "message": f"Invalid 2FA password: {str(e)} | 無效的 2FA 密碼：{str(e)}"
                    }
            else:
                self._auth_state.needs_2fa = True
                return {
                    "success": False,
                    "needs_2fa": True,
                    "message": "2FA password required | 需要 2FA 密碼"
                }

        except PhoneCodeInvalidError:
            return {
                "success": False,
                "message": "Invalid verification code | 無效的驗證碼"
            }
        except PhoneCodeExpiredError:
            return {
                "success": False,
                "message": "Verification code expired | 驗證碼已過期"
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"Login failed: {str(e)} | 登入失敗：{str(e)}"
            }

    async def logout(self) -> dict:
        """
        Log out from Telegram.
        從 Telegram 登出。

        Returns:
            dict with status and message | 包含狀態和訊息的字典
        """
        if not self._client:
            return {
                "success": False,
                "message": "Not connected | 未連線"
            }

        try:
            await self._client.log_out()
            self._auth_state = AuthState()

            # Remove session file | 移除 session 檔案
            session_file = f"{self.session_name}.session"
            if os.path.exists(session_file):
                os.remove(session_file)

            return {
                "success": True,
                "message": "Logged out successfully | 登出成功"
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"Logout failed: {str(e)} | 登出失敗：{str(e)}"
            }

    async def get_status(self) -> dict:
        """
        Get current authentication status.
        取得當前認證狀態。

        Returns:
            dict with authentication status | 包含認證狀態的字典
        """
        if not self._client:
            return {
                "is_logged_in": False,
                "message": "Client not initialized | 客戶端未初始化"
            }

        try:
            is_authorized = await self._client.is_user_authorized()
            if is_authorized:
                me = await self._client.get_me()
                return {
                    "is_logged_in": True,
                    "user": {
                        "id": me.id,
                        "name": self._get_display_name(me),
                        "username": me.username
                    }
                }
            else:
                return {
                    "is_logged_in": False,
                    "message": "Not logged in | 未登入"
                }
        except AuthKeyUnregisteredError:
            self._auth_state = AuthState()
            return {
                "is_logged_in": False,
                "message": "Session expired | Session 已過期"
            }
        except Exception as e:
            return {
                "is_logged_in": False,
                "message": f"Error checking status: {str(e)} | 檢查狀態錯誤：{str(e)}"
            }

    async def get_dialogs(self) -> list[DialogInfo]:
        """
        Get all dialogs (chats, groups, channels).
        取得所有對話（聊天、群組、頻道）。

        Returns:
            List of DialogInfo objects | DialogInfo 物件列表
        """
        if not self._client or not await self._client.is_user_authorized():
            return []

        dialogs = []
        async for dialog in self._client.iter_dialogs():
            entity = dialog.entity
            dialog_type = self._get_dialog_type(entity)

            # Skip private chats (users) for this tool's purpose
            # 跳過私人聊天（用戶），因為此工具主要用於群組/頻道
            if dialog_type == DialogType.USER:
                continue

            members_count = None
            if hasattr(entity, 'participants_count'):
                members_count = entity.participants_count

            dialogs.append(DialogInfo(
                id=dialog.id,
                name=dialog.name or "Unknown",
                dialog_type=dialog_type,
                username=getattr(entity, 'username', None),
                members_count=members_count
            ))

        return dialogs

    async def get_messages_senders(
        self,
        chat_id: int,
        limit: int = 100
    ) -> list[SenderInfo]:
        """
        Get unique senders from recent messages in a chat.
        從聊天的最近訊息中取得唯一的發送者。

        Args:
            chat_id: Chat/Group/Channel ID
            limit: Maximum number of messages to fetch | 要取得的最大訊息數

        Returns:
            List of unique SenderInfo objects | 唯一的 SenderInfo 物件列表
        """
        if not self._client or not await self._client.is_user_authorized():
            return []

        seen_ids = set()
        senders = []

        try:
            async for message in self._client.iter_messages(chat_id, limit=limit):
                if message.sender_id and message.sender_id not in seen_ids:
                    seen_ids.add(message.sender_id)

                    sender = message.sender
                    if sender:
                        is_bot = getattr(sender, 'bot', False)
                        senders.append(SenderInfo(
                            id=sender.id,
                            name=self._get_display_name(sender),
                            username=getattr(sender, 'username', None),
                            is_bot=is_bot
                        ))
        except Exception as e:
            # Log error but return what we have
            # 記錄錯誤但返回已有的資料
            print(f"Error fetching messages: {e}")

        return senders

    def _get_dialog_type(self, entity) -> DialogType:
        """
        Determine the dialog type from entity.
        從實體判斷對話類型。
        """
        if isinstance(entity, User):
            if entity.bot:
                return DialogType.BOT
            return DialogType.USER
        elif isinstance(entity, Chat):
            return DialogType.GROUP
        elif isinstance(entity, Channel):
            if entity.broadcast:
                return DialogType.CHANNEL
            return DialogType.GROUP
        return DialogType.UNKNOWN

    def _get_display_name(self, entity) -> str:
        """
        Get display name from entity.
        從實體取得顯示名稱。
        """
        if hasattr(entity, 'title'):
            return entity.title

        parts = []
        if hasattr(entity, 'first_name') and entity.first_name:
            parts.append(entity.first_name)
        if hasattr(entity, 'last_name') and entity.last_name:
            parts.append(entity.last_name)

        if parts:
            return " ".join(parts)

        if hasattr(entity, 'username') and entity.username:
            return f"@{entity.username}"

        return "Unknown"


# Singleton instance management | 單例實例管理
_service_instance: Optional[TelegramService] = None


def get_telegram_service() -> Optional[TelegramService]:
    """Get the global Telegram service instance | 取得全域 Telegram 服務實例"""
    return _service_instance


def set_telegram_service(service: TelegramService) -> None:
    """Set the global Telegram service instance | 設定全域 Telegram 服務實例"""
    global _service_instance
    _service_instance = service
