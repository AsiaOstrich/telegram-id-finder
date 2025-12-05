# Telegram ID 查詢器

網頁工具：取得 Telegram 群組、頻道、用戶 ID 用於設定。

---

## 功能特色

- **Telegram 登入**：使用 API 憑證登入你的 Telegram 帳號
- **列出群組/頻道**：查看所有已加入的群組和頻道及其 ID
- **查看發言者**：查看任何群組中的最近發言者及其用戶 ID
- **產生設定檔**：將選擇的聊天和發言者匯出為 `settings.yaml`，供 [telegram-signal-parser](https://github.com/AsiaOstrich/telegram-signal-parser) 使用
- **一鍵複製**：快速複製任何 ID 到剪貼簿

---

## 螢幕截圖

*即將推出*

---

## 開始使用

### 前置需求

- Python 3.11 或更高版本
- 從 [my.telegram.org/apps](https://my.telegram.org/apps) 取得的 Telegram API 憑證

### 安裝

```bash
# 複製儲存庫
git clone https://github.com/AsiaOstrich/telegram-id-finder.git
cd telegram-id-finder

# 建立虛擬環境（建議）
python -m venv venv
source venv/bin/activate  # Windows 系統：venv\Scripts\activate

# 安裝相依套件
pip install -r requirements.txt
```

### 設定

1. 複製範例環境變數檔案：
   ```bash
   cp .env.example .env
   ```

2. （選擇性）編輯 `.env` 加入你的 Telegram API 憑證：
   ```env
   TELEGRAM_API_ID=your_api_id
   TELEGRAM_API_HASH=your_api_hash
   ```

   > **注意**：你也可以直接在網頁介面中輸入憑證。

### 執行應用程式

```bash
# 使用 uvicorn 執行
uvicorn app.main:app --reload

# 或直接執行
python -m app.main
```

應用程式將在 [http://127.0.0.1:8000](http://127.0.0.1:8000) 啟動

---

## 使用方式

### 步驟 1：登入 Telegram

1. 輸入你從 [my.telegram.org/apps](https://my.telegram.org/apps) 取得的 **API ID** 和 **API Hash**
2. 輸入手機號碼（含國碼，例如 `+886912345678`）
3. 點擊「發送驗證碼」並輸入從 Telegram 收到的驗證碼
4. 如果啟用了 2FA，請輸入密碼

### 步驟 2：選擇群組/頻道

- 瀏覽所有已加入的群組和頻道
- 點擊「複製」來複製任何聊天 ID
- 勾選要加入設定檔的聊天

### 步驟 3：查看發言者（選擇性）

- 點擊任何群組的「查看發言者」來查看最近的發言者
- 複製用戶 ID 或選擇要加入設定檔的發言者

### 步驟 4：產生設定檔

- 檢視已選擇的聊天和發言者
- 點擊「產生 settings.yaml」來建立設定
- 複製 YAML 內容到你的專案中使用

---

## API 端點

| 方法 | 端點 | 說明 |
|------|------|------|
| POST | `/api/auth/send-code` | 發送驗證碼 |
| POST | `/api/auth/verify` | 驗證登入碼 |
| GET | `/api/auth/status` | 檢查登入狀態 |
| POST | `/api/auth/logout` | 登出 |
| GET | `/api/dialogs` | 取得所有群組/頻道 |
| GET | `/api/dialogs/{chat_id}/messages` | 取得訊息發送者 |
| POST | `/api/generate-config` | 產生 settings.yaml |

---

## 專案結構

```
telegram-id-finder/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI 應用程式
│   ├── telegram_service.py  # Telethon 服務封裝
│   └── templates/
│       └── index.html       # 網頁介面
├── .standards/              # 文件標準
├── .env.example             # 環境變數範本
├── requirements.txt         # Python 相依套件
├── README.md                # 英文文件
├── README.zh-TW.md          # 本檔案（中文）
├── CLAUDE.md                # AI 助理指引
└── CONTRIBUTING.md          # 貢獻指南
```

---

## 安全注意事項

- **API 憑證**是敏感資訊。絕對不要提交 `.env` 或分享你的 API Hash。
- **Session 檔案**（`*.session`）包含認證資料。預設已加入 gitignore。
- 應用程式在本機執行，不會將資料發送到外部伺服器（除了 Telegram 的 API）。

---

## 技術堆疊

- **後端**：FastAPI
- **前端**：HTML + Tailwind CSS + 原生 JavaScript
- **Telegram 客戶端**：Telethon（MTProto）
- **Python**：3.11+

---

## 文件標準

本專案遵循 [Universal Documentation Standards](https://github.com/AsiaOstrich/universal-doc-standards)。

- 參閱 [CLAUDE.md](CLAUDE.md) 了解 AI 助理指引
- 參閱 [CONTRIBUTING.md](CONTRIBUTING.md) 了解貢獻指南
- 參閱 [.standards/](.standards/) 了解詳細標準

---

## 貢獻

請閱讀 [CONTRIBUTING.md](CONTRIBUTING.md) 了解行為準則和提交 Pull Request 的流程。

---

## 授權

MIT 授權 - 詳見 [LICENSE](LICENSE)。

---

## 相關專案

- [telegram-signal-parser](https://github.com/AsiaOstrich/telegram-signal-parser) - 從 Telegram 解析交易訊號
- [Universal Documentation Standards](https://github.com/AsiaOstrich/universal-doc-standards) - 文件框架
