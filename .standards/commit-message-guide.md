# Commit Message Guide
# Commit 訊息規範指南

**Version | 版本**: 1.1.0
**Last Updated | 最後更新**: 2025-12-05
**Applicability | 適用範圍**: telegram-id-finder project | telegram-id-finder 專案

---

## Purpose | 目的

Standardized commit messages improve code review efficiency, facilitate automated changelog generation, and make project history searchable and understandable.

標準化的 commit 訊息提升程式碼審查效率、促進自動化變更日誌生成，並使專案歷史可搜尋、可理解。

---

## Basic Format | 基本格式

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Components | 組成元素

| Component | Required | Description |
|-----------|----------|-------------|
| 組成 | 必要 | 描述 |
| `type` | ✅ Yes | Type of change | 變更類型 |
| `scope` | Optional | Module/component affected | 受影響的模組/元件 |
| `subject` | ✅ Yes | Brief description (≤72 chars) | 簡述（≤72 字元）|
| `body` | Recommended | Detailed explanation | 詳細說明 |
| `footer` | Optional | Issue references, breaking changes | Issue 引用、破壞性變更 |

---

## Type Classification | 類型分類

### This Project Uses: Bilingual Mode (Option C)
### 本專案使用：雙語對照模式（選項 C）

Use English `type` and `scope` for tool compatibility, with bilingual subject/body/footer.

使用英文 `type` 和 `scope` 以確保工具相容性，subject/body/footer 採用雙語對照。

### Available Types | 可用類型

| Type | When to Use | 使用時機 |
|------|-------------|---------|
| `feat` | New feature | 新功能 |
| `fix` | Bug fix | Bug 修復 |
| `refactor` | Code refactoring (no functional change) | 重構（無功能變更）|
| `docs` | Documentation only | 僅文件更新 |
| `style` | Formatting, whitespace (no code logic change) | 格式化、空白（無邏輯變更）|
| `test` | Adding or updating tests | 新增或更新測試 |
| `perf` | Performance improvement | 效能改進 |
| `build` | Build system or dependencies | 建置系統或依賴 |
| `ci` | CI/CD pipeline changes | CI/CD 管道變更 |
| `chore` | Maintenance tasks | 維護任務 |
| `revert` | Revert previous commit | 回退先前提交 |

---

## Bilingual Mode Format | 雙語對照模式格式

**Format | 格式**:
```
<type>(<scope>): <English subject>. <中文主旨>。

<English body>

<中文主體>

<footer>
```

**Simple Example | 簡單範例**:
```
fix(api): Correct timeout handling. 修正逾時處理。

Fix API call timeout not being handled correctly.

修正 API 呼叫逾時未正確處理的問題。

Fixes #445
```

---

## Scope Guidelines | 範圍指引

Scope indicates which part of the codebase is affected.
範圍指出程式碼庫的哪個部分受影響。

### Project-Specific Scopes | 專案特定範圍

| Scope | Description | 描述 |
|-------|-------------|------|
| `ui` | User interface components | 使用者介面元件 |
| `api` | Telegram API interactions | Telegram API 互動 |
| `config` | Configuration files | 設定檔 |
| `docs` | Documentation files | 文件檔案 |
| `tests` | Test files | 測試檔案 |
| `utils` | Utility functions | 工具函式 |

**Special Scopes | 特殊範圍**:
- `*`: Multiple scopes affected | 影響多個範圍
- (no scope): Global changes | 全域變更

---

## Subject Line Rules | 主旨行規則

1. **Length | 長度**: ≤72 characters (50 ideal) | ≤72 字元（50 為理想）
2. **Tense | 時態**: Use imperative mood ("Add feature" not "Added feature") | 使用祈使語氣
3. **Capitalization | 大寫**: First letter capitalized | 首字母大寫
4. **No period at end | 結尾無句點**: But use period between English and Chinese | 但英中之間用句點分隔
5. **Bilingual | 雙語**: English first, Chinese follows | 英文在前，中文在後

### Good Examples | 良好範例

```
feat(ui): Add group ID lookup form. 新增群組 ID 查詢表單。
fix(api): Resolve timeout in API calls. 解決 API 呼叫逾時問題。
refactor(utils): Extract ID validation to helper. 提取 ID 驗證至 helper。
docs(readme): Update installation instructions. 更新安裝說明。
test(api): Add unit tests for channel lookup. 新增頻道查詢單元測試。
```

### Bad Examples | 不良範例

```
❌ "fixed bug" - Too vague, no scope, not bilingual | 太模糊，無範圍，非雙語
❌ "feat(ui): added form" - Past tense | 過去式
❌ "Update stuff." - Too vague | 太模糊
❌ "WIP" - Not descriptive | 無描述性
```

---

## Body | 主體內容

Use the body to explain **WHY** the change was made, not **WHAT** was changed.
使用主體解釋**為何**做此變更，而非**變更了什麼**。

### Bilingual Body Structure | 雙語主體結構

```
<Subject line | 主旨行>

<Blank line | 空行>

<English explanation>

<中文說明>

<footer>
```

### Example: Feature | 範例：新功能

```
feat(auth): Add OAuth2 Google login support. 新增 OAuth2 Google 登入支援。

Implement Google OAuth2 authentication flow for user login.

- Add Google OAuth2 SDK integration
- Create callback endpoint for OAuth flow
- Store refresh tokens securely

實作 Google OAuth2 認證流程供使用者登入。

- 整合 Google OAuth2 SDK
- 建立 OAuth 流程回呼端點
- 安全儲存更新權杖

Closes #123
```

### Example: Bug Fix | 範例：Bug 修復

```
fix(api): Resolve race condition in concurrent requests. 解決並發請求的競爭條件。

Fix concurrent API requests overwriting each other due to missing lock mechanism.

- Add request queuing mechanism
- Implement mutex lock for shared resources
- Add proper error handling for queue overflow

修復並發 API 請求因缺少鎖定機制而互相覆蓋的問題。

- 新增請求佇列機制
- 實作共享資源的互斥鎖
- 新增佇列溢出的錯誤處理

Fixes #789
```

---

## Footer | 頁尾

### Issue References | Issue 引用

```
Closes #123      # Automatically closes issue | 自動關閉 issue
Fixes #456       # Automatically closes issue | 自動關閉 issue
Resolves #789    # Automatically closes issue | 自動關閉 issue
Refs #101, #102  # Links without closing | 連結但不關閉
```

### Breaking Changes | 破壞性變更

**CRITICAL | 重要**: Always document breaking changes in footer.
永遠在頁尾記錄破壞性變更。

**Format | 格式**:
```
BREAKING CHANGE: <English description>
破壞性變更: <中文描述>

Migration guide | 遷移指南:
- Step 1 | 步驟 1
- Step 2 | 步驟 2
```

**Example | 範例**:
```
feat(api): Change response format for ID lookup. 變更 ID 查詢的回應格式。

BREAKING CHANGE: API response format changed
破壞性變更: API 回應格式已變更

Old format | 舊格式:
{ "id": "123456789" }

New format | 新格式:
{ "data": { "id": "123456789", "type": "group" } }

Migration guide | 遷移指南:
- Update API consumers to use response.data.id
- 更新 API 消費者使用 response.data.id

Closes #234
```

---

## Complete Examples | 完整範例

### Example 1: Simple Fix | 簡單修復

```
fix(api): Correct timeout handling in API calls. 修正 API 呼叫的逾時處理。

The API call timeout was not handled correctly, causing the app to hang.
Now properly catches timeout errors and displays user-friendly message.

API 呼叫逾時未正確處理，導致應用程式掛起。
現在正確捕獲逾時錯誤並顯示使用者友善訊息。

Fixes #445
```

### Example 2: Feature with Details | 含詳細說明的功能

```
feat(api): Add support for private channel lookup. 新增私人頻道查詢支援。

Add ability to look up private Telegram channels using bot authentication.

- Add authentication token handling for private channels
- Update API client to support both channel types
- Add error handling for unauthorized access
- Use Telegram Bot API v6.0 features

新增使用機器人認證查詢私人 Telegram 頻道的功能。

- 新增私人頻道的認證 token 處理
- 更新 API 客戶端以支援兩種頻道類型
- 新增未授權存取的錯誤處理
- 使用 Telegram Bot API v6.0 功能

Closes #123
```

### Example 3: Documentation Update | 文件更新

```
docs: Initialize project documentation standards. 初始化專案文件規範。

Add comprehensive bilingual documentation following Universal Documentation Standards.

- Add .standards/ with core documentation standards
- Add CLAUDE.md for AI assistant guidelines
- Add CONTRIBUTING.md with GitHub Flow workflow
- Update README.md with project documentation

新增遵循 Universal Documentation Standards 的完整雙語文件。

- 新增 .standards/ 核心文件規範
- 新增 CLAUDE.md AI 助理指引
- 新增 CONTRIBUTING.md 含 GitHub Flow 工作流程
- 更新 README.md 專案文件

Based on: https://github.com/AsiaOstrich/universal-doc-standards
```

---

## Anti-Patterns | 反模式

### ❌ Anti-Pattern 1: Vague Messages | 模糊訊息

```
fix: bug fix
update: changes
```

**Problem | 問題**: No context, not bilingual.
無背景，非雙語。

**✅ Fix | 修正**:
```
fix(api): Prevent duplicate API calls on rapid clicks. 防止快速點擊時重複 API 呼叫。
```

---

### ❌ Anti-Pattern 2: Mixing Multiple Concerns | 混合多個關注點

```
feat: add form, fix bugs, update docs
```

**Problem | 問題**: Should be separate commits.
應分開 commit。

**✅ Fix | 修正**: Split into separate commits | 拆分為獨立 commit

---

### ❌ Anti-Pattern 3: English Only or Chinese Only | 僅英文或僅中文

```
feat(ui): Add group lookup form
```

**Problem | 問題**: Missing Chinese translation in bilingual mode.
雙語模式缺少中文翻譯。

**✅ Fix | 修正**:
```
feat(ui): Add group lookup form. 新增群組查詢表單。
```

---

## Version History | 版本歷史

| Version | Date | Changes |
|---------|------|---------|
| 版本 | 日期 | 變更 |
| 1.1.0 | 2025-12-05 | Adopt Bilingual Mode (Option C) | 採用雙語對照模式（選項 C）|
| 1.0.0 | 2025-12-05 | Initial guide | 初版指南 |

---

## References | 參考資料

- [Conventional Commits](https://www.conventionalcommits.org/)
- [Universal Documentation Standards](https://github.com/AsiaOstrich/universal-doc-standards)

---

## License | 授權

This guide is released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Adapted from [Universal Documentation Standards](https://github.com/AsiaOstrich/universal-doc-standards).

本指南以 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 授權發布。
改編自 [Universal Documentation Standards](https://github.com/AsiaOstrich/universal-doc-standards)。
