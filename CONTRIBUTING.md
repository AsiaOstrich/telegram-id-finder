# Contributing to Telegram ID Finder
# 貢獻指南

Thank you for your interest in contributing to this project!
感謝您有興趣為此專案做出貢獻！

---

## Documentation Standards | 文件標準

This project follows the [Universal Documentation Standards](https://github.com/AsiaOstrich/universal-doc-standards).

本專案遵循 [Universal Documentation Standards](https://github.com/AsiaOstrich/universal-doc-standards)。

### Essential Standards | 必要規範

Please review these before contributing | 貢獻前請先閱讀：

1. **Anti-Hallucination Guidelines | AI 防幻覺指引** - [.standards/anti-hallucination.md](.standards/anti-hallucination.md)
2. **Check-in Standards | 簽入標準** - [.standards/checkin-standards.md](.standards/checkin-standards.md)
3. **Commit Message Guide | Commit 訊息指南** - [.standards/commit-message-guide.md](.standards/commit-message-guide.md)
4. **Git Workflow | Git 工作流程** - [.standards/git-workflow.md](.standards/git-workflow.md)

---

## Git Workflow | Git 工作流程

This project uses **GitHub Flow**.

本專案使用 **GitHub Flow**。

### Branch Structure | 分支結構

```
main      ────●─────────●──────●── (Always deployable | 永遠可部署)
               ╲         ╱      ╱
feature/*       ●───●───●      ╱  (Feature + PR | 功能 + PR)
                              ╱
bugfix/*                 ────●  (Bug fixes | Bug 修復)
```

### Key Principles | 關鍵原則

1. **`main` is always deployable** | `main` 永遠可部署
2. **Branch from `main`** | 從 `main` 分支
3. **Merge to `main` via PR** | 透過 PR 合併到 `main`
4. **Deploy immediately after merge** | 合併後立即部署

### Branch Naming | 分支命名

| Type | Format | Example |
|------|--------|---------|
| 類型 | 格式 | 範例 |
| Feature / 新功能 | `feature/[description]` | `feature/group-lookup` |
| Bug fix / Bug 修復 | `fix/[description]` | `fix/api-timeout` |
| Hotfix / 緊急修復 | `hotfix/[description]` | `hotfix/security-patch` |
| Documentation / 文件 | `docs/[description]` | `docs/api-reference` |
| Refactoring / 重構 | `refactor/[description]` | `refactor/extract-service` |

### Pull Request Process | Pull Request 流程

1. **Fork the repository** | Fork 此儲存庫
2. **Create feature branch from `main`** | 從 `main` 建立功能分支
   ```bash
   git checkout main
   git pull origin main
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes** | 提交變更
   ```bash
   git add .
   git commit -m "feat(scope): add amazing feature"
   ```
4. **Push to branch** | 推送到分支
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open Pull Request** | 開啟 Pull Request
6. **Wait for review and CI** | 等待審查與 CI
7. **Merge after approval** | 核准後合併

---

## Commit Message Format | Commit 訊息格式

This project uses **English** commit types following [Conventional Commits](https://www.conventionalcommits.org/).

本專案使用**英文** commit 類型，遵循 [Conventional Commits](https://www.conventionalcommits.org/)。

### Format | 格式

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Allowed Types | 允許的類型

| Type | Description | 描述 |
|------|-------------|------|
| `feat` | New feature | 新功能 |
| `fix` | Bug fix | Bug 修復 |
| `refactor` | Code refactoring | 重構 |
| `docs` | Documentation | 文件 |
| `style` | Formatting | 格式化 |
| `test` | Tests | 測試 |
| `perf` | Performance | 效能 |
| `build` | Build system | 建置 |
| `ci` | CI/CD | 持續整合 |
| `chore` | Maintenance | 維護 |

### Allowed Scopes | 允許的範圍

| Scope | Usage | 用途 |
|-------|-------|------|
| `ui` | User interface components | 使用者介面元件 |
| `api` | Telegram API interactions | Telegram API 互動 |
| `config` | Configuration | 設定 |
| `docs` | Documentation | 文件 |
| `tests` | Test files | 測試檔案 |

### Examples | 範例

```bash
feat(ui): Add group ID lookup form
# 新增群組 ID 查詢表單

fix(api): Handle rate limiting from Telegram API
# 處理 Telegram API 速率限制

docs(readme): Add installation instructions
# 新增安裝說明

refactor(config): Extract API settings to environment variables
# 將 API 設定提取到環境變數
```

---

## Check-in Checklist | 簽入檢查清單

Before submitting a PR, ensure | 提交 PR 前請確認：

- [ ] Code compiles/runs successfully | 程式碼成功編譯/執行
- [ ] All tests pass | 所有測試通過
- [ ] Documentation is updated (if needed) | 文件已更新（如需要）
- [ ] Commit messages follow the format | Commit 訊息遵循格式
- [ ] No hardcoded secrets or credentials | 無硬編碼的密鑰或憑證
- [ ] Branch is synchronized with main | 分支已與 main 同步

---

## Code Style | 程式碼風格

- Follow existing patterns in the codebase | 遵循程式碼庫中的現有模式
- Use meaningful variable and function names | 使用有意義的變數與函式名稱
- Add comments for complex logic | 為複雜邏輯添加註解
- Keep functions focused and small | 保持函式專注且精簡

---

## Pull Request Template | Pull Request 範本

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

## Questions? | 有問題？

If you have questions about contributing, feel free to:
如果您對貢獻有任何問題，歡迎：

- Open an issue for discussion | 開啟 issue 討論
- Review existing issues and PRs for context | 查看現有 issues 與 PRs 了解脈絡

---

## License | 授權

By contributing, you agree that your contributions will be licensed under the same license as the project.

貢獻即表示您同意您的貢獻將以與專案相同的授權條款進行授權。
