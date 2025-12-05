# Git Workflow Standards - GitHub Flow
# Git 工作流程標準 - GitHub Flow

**Version | 版本**: 1.0.0
**Last Updated | 最後更新**: 2025-12-05
**Applicability | 適用範圍**: telegram-id-finder project | telegram-id-finder 專案

---

## Purpose | 目的

This project uses **GitHub Flow** for its simplicity and continuous deployment compatibility.

本專案使用 **GitHub Flow**，因其簡單且適合持續部署。

---

## Why GitHub Flow | 為何選擇 GitHub Flow

**Best For | 最適合**:
- ✅ Continuous deployment | 持續部署
- ✅ Web applications | Web 應用程式
- ✅ Small to medium teams | 中小型團隊
- ✅ Fast iteration cycles | 快速迭代週期

**Not Ideal For | 不適合**:
- ❌ Scheduled releases (monthly, quarterly) | 定期發布（每月、每季）
- ❌ Multiple production versions maintained simultaneously | 同時維護多個正式版本
- ❌ Large teams with formal release processes | 大型團隊與正式發布流程

---

## Branch Structure | 分支結構

```
main      ────●─────────●──────●── (Always deployable | 永遠可部署)
               ╲         ╱      ╱
feature/*       ●───●───●      ╱  (Feature + PR | 功能 + PR)
                              ╱
bugfix/*                 ────●  (Bug fixes | Bug 修復)
                        ╱
hotfix/*           ────●  (Urgent fixes | 緊急修復)
```

---

## Branch Types | 分支類型

| Branch Type | Purpose | Base Branch | Merge Target | Lifetime |
|-------------|---------|-------------|--------------|----------|
| 分支類型 | 用途 | 基礎分支 | 合併目標 | 生命週期 |
| `main` | Production code | - | - | Permanent |
| `main` | 正式程式碼 | - | - | 永久 |
| `feature/*` | New features | `main` | `main` | Temporary |
| `feature/*` | 新功能 | `main` | `main` | 暫時 |
| `bugfix/*` | Bug fixes | `main` | `main` | Temporary |
| `bugfix/*` | Bug 修復 | `main` | `main` | 暫時 |
| `hotfix/*` | Urgent fixes | `main` | `main` | Temporary |
| `hotfix/*` | 緊急修復 | `main` | `main` | 暫時 |

---

## Key Principles | 關鍵原則

1. **`main` is always deployable** | `main` 永遠可部署
   - Never commit broken code to main
   - 永不提交壞掉的程式碼到 main

2. **Branch from `main`** | 從 `main` 分支
   - All work starts from main branch
   - 所有工作從 main 分支開始

3. **Merge to `main` via PR** | 透過 PR 合併到 `main`
   - All changes require pull request review
   - 所有變更需要 pull request 審查

4. **Deploy immediately after merge** | 合併後立即部署
   - Merged code goes to production quickly
   - 合併的程式碼快速進入正式環境

---

## Workflow Steps | 工作流程步驟

### Step 1: Create Feature Branch | 建立功能分支

```bash
# Ensure you're on main and up-to-date
# 確保在 main 分支且是最新
git checkout main
git pull origin main

# Create feature branch
# 建立功能分支
git checkout -b feature/group-id-lookup
```

### Step 2: Work and Commit | 開發並提交

```bash
# Make changes and commit frequently
# 進行變更並頻繁提交
git add .
git commit -m "feat(ui): Add group ID input form"

# Push to remote
# 推送到遠端
git push -u origin feature/group-id-lookup
```

### Step 3: Open Pull Request | 開啟 Pull Request

1. Go to GitHub repository | 前往 GitHub 儲存庫
2. Click "New Pull Request" | 點擊 "New Pull Request"
3. Select your branch | 選擇你的分支
4. Write clear description | 撰寫清晰描述
5. Request reviewers | 請求審查者

### Step 4: Review and Merge | 審查並合併

1. Wait for CI to pass | 等待 CI 通過
2. Address review comments | 處理審查意見
3. Get approval | 取得核准
4. Merge via GitHub UI | 透過 GitHub 介面合併

### Step 5: Delete Feature Branch | 刪除功能分支

```bash
# GitHub auto-deletes after merge (if configured)
# GitHub 合併後自動刪除（如已設定）

# Or manually delete
# 或手動刪除
git branch -d feature/group-id-lookup
git push origin --delete feature/group-id-lookup
```

---

## Branch Naming Conventions | 分支命名慣例

### Format | 格式

```
<type>/<short-description>
```

### Types | 類型

| Type | Usage | Example |
|------|-------|---------|
| 類型 | 用途 | 範例 |
| `feature/` | New functionality | `feature/channel-lookup` |
| `feature/` | 新功能 | `feature/channel-lookup` |
| `fix/` or `bugfix/` | Bug fixes | `fix/api-timeout` |
| `fix/` 或 `bugfix/` | Bug 修復 | `fix/api-timeout` |
| `hotfix/` | Urgent production fixes | `hotfix/security-patch` |
| `hotfix/` | 緊急正式修復 | `hotfix/security-patch` |
| `refactor/` | Code refactoring | `refactor/extract-utils` |
| `refactor/` | 程式碼重構 | `refactor/extract-utils` |
| `docs/` | Documentation only | `docs/api-reference` |
| `docs/` | 僅文件 | `docs/api-reference` |
| `test/` | Test additions | `test/api-integration` |
| `test/` | 新增測試 | `test/api-integration` |

### Naming Rules | 命名規則

1. **Use lowercase** | 使用小寫
2. **Use hyphens for spaces** | 使用連字號分隔
3. **Be descriptive but concise** | 具描述性但簡潔
4. **Avoid issue numbers only** | 避免僅用 issue 編號

**Good Examples | 良好範例**:
```
feature/group-id-lookup
fix/telegram-api-timeout
hotfix/security-vulnerability
refactor/extract-validation-utils
docs/update-installation-guide
```

**Bad Examples | 不良範例**:
```
feature/123                    # ❌ Not descriptive | 無描述性
Fix-Bug                        # ❌ Not lowercase | 非小寫
feature/add_new_feature        # ❌ Underscores, too vague | 底線，太模糊
myFeature                      # ❌ camelCase, no type prefix | 駝峰式，無類型前綴
```

---

## Merge Strategy | 合併策略

This project uses **Squash Merge** for clean history.
本專案使用 **Squash Merge** 以保持乾淨歷史。

### Why Squash Merge | 為何使用 Squash Merge

**Pros | 優點**:
- ✅ Clean, linear history | 乾淨的線性歷史
- ✅ One commit per feature | 每功能一個提交
- ✅ Easy to read git log | 易讀的 git log
- ✅ Easy to revert entire feature | 易於回退整個功能

**Cons | 缺點**:
- ❌ Loses detailed commit history | 失去詳細提交歷史
- ❌ Can't cherry-pick individual commits | 無法挑選個別提交

### Configure in GitHub | 在 GitHub 設定

```
Repository Settings → Pull Requests
☑ Allow squash merging
☐ Allow merge commits (optional)
☐ Allow rebase merging (optional)
```

---

## Pull Request Guidelines | Pull Request 指引

### PR Checklist | PR 檢查清單

- [ ] **Title follows commit convention** | 標題遵循 commit 慣例
- [ ] **Description explains why** | 描述解釋原因
- [ ] **Linked to issue** (if applicable) | 連結 issue（如適用）
- [ ] **Tests included** | 包含測試
- [ ] **Documentation updated** | 文件已更新
- [ ] **CI passes** | CI 通過

### PR Description Template | PR 描述範本

```markdown
## What | 做了什麼

[Brief description of changes | 變更簡述]

## Why | 為什麼

[Explanation of why this change is needed | 說明為何需要此變更]

## Changes | 變更清單

- [Change 1 | 變更 1]
- [Change 2 | 變更 2]

## Testing | 測試

- [ ] Unit tests added/updated | 已新增/更新單元測試
- [ ] Manual testing performed | 已執行手動測試

## Screenshots (if applicable) | 截圖（如適用）

[Add screenshots for UI changes | 為 UI 變更新增截圖]

## Related Issues | 相關 Issues

Closes #123
```

---

## Conflict Resolution | 衝突解決

### Prevention | 預防

1. **Sync frequently** | 頻繁同步
   ```bash
   git checkout main
   git pull origin main
   git checkout feature/my-feature
   git merge main
   ```

2. **Keep branches small** | 保持分支小型化
   - Avoid long-lived feature branches | 避免長時間的功能分支
   - Break large features into smaller PRs | 將大功能拆分為小 PR

3. **Communicate** | 溝通
   - Announce major changes | 宣布重大變更
   - Coordinate on shared files | 協調共享檔案

### Resolution Steps | 解決步驟

```bash
# 1. Update main
# 1. 更新 main
git checkout main
git pull origin main

# 2. Merge main into feature branch
# 2. 將 main 合併到功能分支
git checkout feature/my-feature
git merge main

# 3. Resolve conflicts in files
# 3. 解決檔案中的衝突
# Edit files marked with conflict markers
# 編輯標記有衝突標記的檔案

# 4. Stage resolved files
# 4. 暫存已解決的檔案
git add resolved-file.js

# 5. Complete the merge
# 5. 完成合併
git commit -m "chore: resolve merge conflicts with main"

# 6. Push
# 6. 推送
git push origin feature/my-feature
```

---

## Common Git Commands | 常用 Git 指令

### Daily Operations | 日常操作

```bash
# Check status | 檢查狀態
git status

# View changes | 檢視變更
git diff

# Stage changes | 暫存變更
git add .
git add <file>

# Commit | 提交
git commit -m "type(scope): description"

# Push | 推送
git push origin <branch>

# Pull latest | 拉取最新
git pull origin main
```

### Branch Operations | 分支操作

```bash
# List branches | 列出分支
git branch -a

# Create branch | 建立分支
git checkout -b feature/new-feature

# Switch branch | 切換分支
git checkout main

# Delete local branch | 刪除本地分支
git branch -d feature/old-feature

# Delete remote branch | 刪除遠端分支
git push origin --delete feature/old-feature
```

### Stash Operations | 暫存操作

```bash
# Stash changes | 暫存變更
git stash save "WIP: description"

# List stashes | 列出暫存
git stash list

# Apply stash | 應用暫存
git stash pop
```

---

## Troubleshooting | 疑難排解

### Accidentally Committed to Wrong Branch | 意外提交到錯誤分支

```bash
# Undo last commit but keep changes
# 撤銷最後提交但保留變更
git reset --soft HEAD~1

# Switch to correct branch
# 切換到正確分支
git checkout correct-branch

# Commit changes
# 提交變更
git add .
git commit -m "feat: add feature"
```

### Need to Update Branch from Main | 需要從 main 更新分支

```bash
# Option 1: Merge (preserves history)
# 選項 1：合併（保留歷史）
git checkout feature/my-feature
git merge main

# Option 2: Rebase (cleaner history)
# 選項 2：變基（更乾淨歷史）
git checkout feature/my-feature
git rebase main
```

---

## Version History | 版本歷史

| Version | Date | Changes |
|---------|------|---------|
| 版本 | 日期 | 變更 |
| 1.0.0 | 2025-12-05 | Initial GitHub Flow standard | 初版 GitHub Flow 標準 |

---

## References | 參考資料

- [GitHub Flow Guide](https://docs.github.com/en/get-started/using-github/github-flow)
- [Universal Documentation Standards](https://github.com/AsiaOstrich/universal-doc-standards)

---

## License | 授權

This standard is released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Adapted from [Universal Documentation Standards](https://github.com/AsiaOstrich/universal-doc-standards).

本標準以 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 授權發布。
改編自 [Universal Documentation Standards](https://github.com/AsiaOstrich/universal-doc-standards)。
