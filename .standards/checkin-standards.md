# Code Check-in Standards
# 程式碼簽入檢查點標準

**Version | 版本**: 1.0.0
**Last Updated | 最後更新**: 2025-12-05
**Applicability | 適用範圍**: telegram-id-finder project | telegram-id-finder 專案

---

## Purpose | 目的

This standard defines quality gates that MUST be passed before committing code to version control. It ensures every commit maintains codebase stability and quality.

本標準定義提交程式碼到版本控制前必須通過的品質關卡。確保每次提交都維持程式碼庫的穩定性與品質。

---

## Core Philosophy | 核心哲學

**Every commit should | 每次提交應該**:
- ✅ Be a complete logical unit of work | 是完整的邏輯工作單元
- ✅ Leave the codebase in a working state | 讓程式碼庫處於可運作狀態
- ✅ Be reversible without breaking functionality | 可回退而不破壞功能
- ✅ Contain its own tests (for new features) | 包含自己的測試（新功能）
- ✅ Be understandable to future developers | 讓未來開發者能理解

---

## Mandatory Checklist | 必檢清單

### 1. Build Verification | 建置驗證

- [ ] **Code compiles/runs successfully | 程式碼成功編譯/執行**
  - Zero build errors | 零建置錯誤
  - Zero build warnings (or documented exceptions) | 零建置警告（或已記錄的例外）

- [ ] **Dependencies are satisfied | 依賴已滿足**
  - All package dependencies installed | 所有套件依賴已安裝
  - Dependency versions locked/documented | 依賴版本已鎖定/記錄

**Project Build Commands | 專案建置指令**:
```bash
# Node.js project | Node.js 專案
npm install && npm run build

# Python project | Python 專案
pip install -r requirements.txt

# Static HTML/JS (no build required)
# 靜態 HTML/JS（無需建置）
```

---

### 2. Test Verification | 測試驗證

- [ ] **All existing tests pass | 所有現有測試通過**
  - Unit tests: 100% pass rate | 單元測試：100% 通過率
  - Integration tests: 100% pass rate | 整合測試：100% 通過率

- [ ] **New code is tested | 新程式碼已測試**
  - New features have corresponding tests | 新功能有對應測試
  - Bug fixes include regression tests | Bug 修復包含回歸測試

**Project Test Commands | 專案測試指令**:
```bash
# Node.js with Jest | Node.js 使用 Jest
npm test

# Python with pytest | Python 使用 pytest
pytest
```

---

### 3. Code Quality | 程式碼品質

- [ ] **Follows coding standards | 遵循編碼標準**
  - Naming conventions adhered to | 遵守命名慣例
  - Code formatting consistent | 程式碼格式一致
  - Comments/documentation present | 有註解/文件

- [ ] **No code smells | 無程式碼異味**
  - Methods not too long | 方法不過長
  - No duplicated code blocks | 無重複程式碼區塊
  - Reasonable complexity | 合理的複雜度

- [ ] **Security checked | 安全性已檢查**
  - No hardcoded secrets (passwords, API keys) | 無硬編碼密鑰（密碼、API 金鑰）
  - No SQL injection vulnerabilities | 無 SQL 注入漏洞
  - No XSS vulnerabilities | 無 XSS 漏洞

---

### 4. Documentation | 文件

- [ ] **API documentation updated | API 文件已更新**
  - Public APIs have doc comments | 公開 API 有文件註解
  - Parameter descriptions complete | 參數描述完整

- [ ] **README updated (if needed) | README 已更新（如需要）**
  - New features documented | 新功能已記錄
  - Breaking changes noted | 破壞性變更已註記

---

### 5. Workflow Compliance | 工作流程合規

- [ ] **Branch naming correct | 分支命名正確**
  - Follows GitHub Flow convention | 遵循 GitHub Flow 慣例
  - Format: `feature/`, `fix/`, `hotfix/`, `docs/`, `refactor/`

- [ ] **Commit message formatted | Commit 訊息已格式化**
  - Follows conventional commits | 遵循 conventional commits
  - Clear and descriptive | 清晰且具描述性

- [ ] **Synchronized with main branch | 已與 main 分支同步**
  - Merged latest changes from main | 已合併 main 的最新變更
  - No merge conflicts | 無合併衝突

---

## Check-in Timing Guidelines | 簽入時機指引

### ✅ Appropriate Times to Commit | 適合提交的時機

| Scenario | 情境 | Description | 描述 |
|----------|------|-------------|------|
| **Completed Functional Unit** | 完成功能單元 | Feature fully implemented, tests written | 功能完整實作、測試已撰寫 |
| **Specific Bug Fixed** | 修復特定 Bug | Bug reproduced, fixed, regression test added | Bug 已重現、修復、回歸測試已新增 |
| **Independent Refactor** | 獨立重構 | Refactoring complete, no functional changes | 重構完成、無功能變更 |
| **Runnable State** | 可執行狀態 | Code compiles, application can run | 程式碼可編譯、應用程式可執行 |

**Good Examples | 良好範例**:
```
✅ feat(ui): Add group ID lookup form
   群組 ID 查詢表單完整實作，包含驗證與錯誤處理

✅ fix(api): Resolve timeout in Telegram API calls
   修復 API 逾時問題，新增重試機制與錯誤處理

✅ refactor(utils): Extract ID validation to helper
   提取 ID 驗證邏輯為獨立 helper，所有測試通過
```

---

### ❌ Inappropriate Times to Commit | 不適合提交的時機

| Scenario | 情境 | Problem | 問題 |
|----------|------|---------|------|
| **Build Failures** | 建置失敗 | Compilation errors, unresolved dependencies | 編譯錯誤、未解決的依賴 |
| **Test Failures** | 測試失敗 | One or more tests failing | 一個或多個測試失敗 |
| **Incomplete Features** | 未完成功能 | Would break existing functionality | 會破壞現有功能 |
| **Experimental Code** | 實驗性程式碼 | TODO comments, debugging code left in | 殘留 TODO 註解、除錯程式碼 |

**Bad Examples | 不良範例**:
```
❌ "WIP: trying to fix login"
   建置有錯誤、測試失敗、不清楚嘗試了什麼

❌ "feat(api): new endpoint (incomplete)"
   端點回傳硬編碼資料、無驗證、測試寫著 "TODO"

❌ "refactor: experimenting with new structure"
   一半檔案已移動、舊程式碼被註解而非刪除
```

---

## Commit Granularity Guidelines | Commit 粒度指引

### Ideal Commit Size | 理想的 Commit 大小

| Metric | Recommended | Description |
|--------|-------------|-------------|
| 指標 | 建議值 | 說明 |
| File Count | 1-10 files | Consider splitting if >10 files |
| 檔案數量 | 1-10 個 | 超過 10 個檔案應考慮拆分 |
| Lines Changed | 50-300 lines | Too large is hard to review |
| 變更行數 | 50-300 行 | 過大難以審查 |
| Scope | Single concern | One commit does one thing |
| 功能範圍 | 單一關注點 | 一個 commit 只做一件事 |

### Splitting Principles | 拆分原則

**Should be combined | 應該合併**:
- Feature implementation + corresponding tests | 功能實作 + 對應測試
- Tightly related multi-file changes | 緊密相關的多檔案變更

**Should be separate | 應該分開**:
- Feature A + Feature B | 功能 A + 功能 B
- Refactoring + new feature | 重構 + 新功能
- Bug fix + incidental refactoring | Bug 修復 + 順帶重構

---

## AI Assistant Integration | AI 助理整合

When AI assistants complete code changes, they MUST follow this workflow:
當 AI 助理完成程式碼變更時，必須遵循此工作流程：

### Step 1: Evaluate Check-in Timing | 評估簽入時機

**AI must assess | AI 必須評估**:
- Is this a complete logical unit? | 這是完整的邏輯單元嗎？
- Is the codebase in a working state? | 程式碼庫處於可運作狀態嗎？
- Are there incomplete TODOs? | 有未完成的 TODO 嗎？

### Step 2: Run Checklist | 執行檢查清單

**AI must verify | AI 必須驗證**:
- [ ] Build command succeeds | 建置指令成功
- [ ] Tests pass | 測試通過
- [ ] Code follows project standards | 程式碼遵循專案標準
- [ ] Documentation updated | 文件已更新
- [ ] Commit message prepared | Commit 訊息已準備

### Step 3: Prompt User for Confirmation | 提示使用者確認

**AI MUST use this prompt format | AI 必須使用此提示格式**:

```
## 請確認是否簽入 | Please Confirm Check-in

已完成 | Completed: [Brief description | 簡述]

### 檢查結果 | Checklist Results
✅ Item 1
✅ Item 2
⚠️ Item 3 (needs verification | 需驗證)

建議 commit message | Suggested commit message:
<type>(<scope>): <description>

是否立即建立 commit? | Proceed with commit now?
```

### Step 4: Wait for Confirmation | 等待確認

**AI must NOT | AI 禁止**:
- ❌ Automatically execute `git add`
- ❌ Automatically execute `git commit`
- ❌ Automatically execute `git push`

**AI must | AI 必須**:
- ✅ Wait for explicit user approval | 等待使用者明確核准
- ✅ Provide clear checklist summary | 提供清晰的檢查清單摘要
- ✅ Allow user to decline or request changes | 允許使用者拒絕或請求變更

---

## Version History | 版本歷史

| Version | Date | Changes |
|---------|------|---------|
| 版本 | 日期 | 變更 |
| 1.0.0 | 2025-12-05 | Initial standard published | 初版發布 |

---

## References | 參考資料

- [Conventional Commits](https://www.conventionalcommits.org/)
- [Universal Documentation Standards](https://github.com/AsiaOstrich/universal-doc-standards)

---

## License | 授權

This standard is released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Adapted from [Universal Documentation Standards](https://github.com/AsiaOstrich/universal-doc-standards).

本標準以 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 授權發布。
改編自 [Universal Documentation Standards](https://github.com/AsiaOstrich/universal-doc-standards)。
