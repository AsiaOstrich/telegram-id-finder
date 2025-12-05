# CLAUDE.md - AI Assistant Guidelines
# AI 助理指南

This file provides guidance for AI assistants working on this project.
本檔案為在此專案工作的 AI 助理提供指引。

---

## Project Overview | 專案概述

**Project Name | 專案名稱**: telegram-id-finder
**Description | 描述**: Web UI tool to find Telegram group/channel IDs and user IDs for configuration / 網頁工具：取得 Telegram 群組、頻道、用戶 ID

---

## Documentation Standards | 文件標準

This project follows the [Universal Documentation Standards](https://github.com/AsiaOstrich/universal-doc-standards).

本專案遵循 [Universal Documentation Standards](https://github.com/AsiaOstrich/universal-doc-standards)。

Core standards are located in `.standards/` | 核心規範位於 `.standards/`：
- `anti-hallucination.md` - AI collaboration guidelines | AI 協作指引
- `checkin-standards.md` - Code check-in quality gates | 簽入品質關卡
- `commit-message-guide.md` - Commit message conventions | Commit 訊息慣例
- `git-workflow.md` - GitHub Flow workflow | GitHub Flow 工作流程
- `testing-standards.md` - Testing conventions (UT/IT/E2E) | 測試慣例（UT/IT/E2E）

---

## Git Workflow | Git 工作流程

This project uses **GitHub Flow**.

本專案使用 **GitHub Flow**。

### Key Principles | 關鍵原則

1. **`main` is always deployable** | `main` 永遠可部署
2. **Branch from `main`** | 從 `main` 分支
3. **Merge to `main` via PR** | 透過 PR 合併到 `main`
4. **Deploy immediately after merge** | 合併後立即部署

### Branch Naming | 分支命名

```
feature/[description]   # New features | 新功能
fix/[description]       # Bug fixes | Bug 修復
hotfix/[description]    # Urgent fixes | 緊急修復
docs/[description]      # Documentation | 文件
refactor/[description]  # Refactoring | 重構
```

---

## Development Guidelines | 開發指引

### Language & Framework | 語言與框架

- **Primary Language | 主要語言**: [To be determined | 待定]

### Code Style | 程式碼風格

- Follow existing code patterns in the project | 遵循專案中的現有模式
- Use meaningful variable and function names | 使用有意義的變數與函式名稱
- Add comments for complex logic | 為複雜邏輯添加註解

### Commit Messages | Commit 訊息

Use **English** commit types following Conventional Commits:

使用**英文** commit 類型，遵循 Conventional Commits：

```
feat(scope): Add new feature
fix(scope): Fix bug
docs(scope): Update documentation
refactor(scope): Refactor code
test(scope): Add tests
```

**Allowed Scopes | 允許的範圍**:
| Scope | Usage | 用途 |
|-------|-------|------|
| `ui` | User interface | 使用者介面 |
| `api` | Telegram API interactions | Telegram API 互動 |
| `config` | Configuration | 設定 |
| `docs` | Documentation | 文件 |
| `tests` | Test files | 測試檔案 |

---

## AI Assistant Behavior | AI 助理行為

### Before Making Changes | 進行變更前

1. **Read existing code** before suggesting modifications | 在建議修改前先讀取現有程式碼
2. **Verify file paths** and line numbers before referencing | 在引用前驗證檔案路徑與行號
3. **Ask for clarification** if requirements are ambiguous | 若需求模糊請求澄清

### Anti-Hallucination Rules | 防幻覺規則

- ❌ Do NOT invent APIs or functions not in the codebase | 不要捏造程式碼庫中不存在的 API 或函式
- ❌ Do NOT assume configurations without reading them | 不要在未讀取的情況下假設設定
- ❌ Do NOT fabricate requirements | 不要捏造需求
- ✅ DO cite file paths and line numbers | 請引用檔案路徑與行號
- ✅ DO ask questions when uncertain | 不確定時請提問
- ✅ DO read files before making recommendations | 在提出建議前請讀取檔案

### Check-in Process | 簽入流程

Before committing | 提交前：
1. Ensure code compiles/runs successfully | 確保程式碼成功編譯/執行
2. Verify all tests pass | 驗證所有測試通過
3. Follow commit message format | 遵循 commit 訊息格式
4. Get user confirmation before executing git commands | 執行 git 指令前取得使用者確認

---

## Project Structure | 專案結構

```
telegram-id-finder/
├── .standards/              # Documentation standards | 文件規範
│   ├── anti-hallucination.md
│   ├── checkin-standards.md
│   ├── commit-message-guide.md
│   ├── git-workflow.md
│   └── testing-standards.md
├── .gitignore              # Git ignore rules | Git 忽略規則
├── CLAUDE.md               # This file - AI guidelines | 此檔案 - AI 指引
├── README.md               # Project documentation | 專案文件
├── CONTRIBUTING.md         # Contribution guidelines | 貢獻指南
└── [source files]          # Application source code | 應用程式原始碼
```

---

## Quick Reference | 快速參考

| Task | Command/Action |
|------|----------------|
| 任務 | 指令/動作 |
| Read standards | Check `.standards/` directory |
| 讀取規範 | 查看 `.standards/` 目錄 |
| Commit format | `type(scope): subject` |
| Commit 格式 | `type(scope): subject` |
| Before commit | Run tests, verify build |
| 提交前 | 執行測試、驗證建置 |
| Git workflow | GitHub Flow (branch from main, PR to main) |
| Git 工作流程 | GitHub Flow（從 main 分支，PR 到 main）|

---

## Contact | 聯繫

For questions about these guidelines, refer to the Universal Documentation Standards repository or ask the project maintainer.

如有關於這些指引的問題，請參考 Universal Documentation Standards 儲存庫或詢問專案維護者。
