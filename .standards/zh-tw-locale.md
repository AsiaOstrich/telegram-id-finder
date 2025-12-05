# Traditional Chinese (Taiwan) Locale Standard
# 繁體中文（台灣）地區規範

**Version | 版本**: 1.0.0
**Last Updated | 最後更新**: 2025-12-05
**Applicability | 適用範圍**: telegram-id-finder project | telegram-id-finder 專案

---

## Purpose | 目的

This standard defines language usage guidelines for this bilingual project, ensuring consistency between Chinese content and English code.

本標準定義此雙語專案的語言使用準則，確保中文內容與英文程式碼之間的一致性。

---

## Core Principle | 核心原則

**Chinese for Communication, English for Code**
**中文用於溝通，英文用於程式碼**

- ✅ Documentation: Bilingual (English + Traditional Chinese)
- ✅ Code (variables, functions, classes): English
- ✅ Commit message types: English (feat, fix, etc.)
- ✅ Commit message body: Can be bilingual
- ✅ Comments: Traditional Chinese or bilingual

---

## Language Usage Matrix | 語言使用矩陣

| Content Type | Language | Example |
|--------------|----------|---------|
| 內容類型 | 語言 | 範例 |
| **Code** | | |
| Variable names | English | `groupId` ✅ / `群組ID` ❌ |
| Function names | English | `lookupGroupId()` ✅ |
| Class names | English | `TelegramService` ✅ |
| **Documentation** | | |
| README.md | Bilingual | English + 繁體中文 |
| CONTRIBUTING.md | Bilingual | English + 繁體中文 |
| API docs | Bilingual | English + 繁體中文 |
| **Code Comments** | | |
| Inline comments | 繁體中文 or Bilingual | `// 驗證群組 ID` ✅ |
| Doc comments | Bilingual | See examples below |
| **Commit Messages** | | |
| Type | English | `feat`, `fix`, `docs` ✅ |
| Scope | English | `(ui)`, `(api)` ✅ |
| Subject | English | `Add group lookup` ✅ |
| Body | Bilingual | English + 繁體中文 |
| **Configuration** | | |
| Config keys | English | `apiKey` ✅ |
| Config comments | 繁體中文 | `# API 金鑰` ✅ |

---

## Code Naming Conventions | 程式碼命名慣例

### ✅ Correct Examples | 正確範例

```javascript
// Class names: English, PascalCase
// 類別名稱：英文，PascalCase
class TelegramIdFinder {
    // Properties: English, camelCase
    // 屬性：英文，camelCase
    constructor(apiToken) {
        this.apiToken = apiToken;
    }

    // Methods: English, camelCase
    // 方法：英文，camelCase
    /**
     * Look up group ID by username
     * 透過使用者名稱查詢群組 ID
     *
     * @param {string} username - Group username | 群組使用者名稱
     * @returns {string} Group ID | 群組 ID
     */
    async lookupGroupId(username) {
        // 驗證輸入參數
        if (!username) {
            throw new Error('Username is required');
        }

        // 呼叫 Telegram API
        const result = await this.callApi(username);
        return result.id;
    }
}
```

### ❌ Incorrect Examples | 錯誤範例

```javascript
// ❌ WRONG: Using Chinese for code names
// ❌ 錯誤：使用中文作為程式碼名稱
class 電報ID查詢器 {  // ❌ Chinese class name
    constructor(apiToken) {
        this.api金鑰 = apiToken;  // ❌ Chinese property name
    }

    async 查詢群組ID(使用者名稱) {  // ❌ Chinese method/parameter names
        // ...
    }
}
```

---

## Documentation Language Guidelines | 文件語言準則

### Bilingual Format | 雙語格式

Use `English | 繁體中文` format for headings and key content:

```markdown
## Purpose | 目的

This tool helps find Telegram IDs.
本工具協助查詢 Telegram ID。

### Features | 功能

- Group ID lookup | 群組 ID 查詢
- Channel ID lookup | 頻道 ID 查詢
- User ID lookup | 用戶 ID 查詢
```

### Tables | 表格

```markdown
| Feature | Description | 功能 | 描述 |
|---------|-------------|------|------|
| Group lookup | Find group IDs | 群組查詢 | 查詢群組 ID |
```

---

## Commit Message Language | Commit 訊息語言

### Format | 格式

```
<type>(<scope>): <English subject>

<Bilingual body - English + 繁體中文>

<footer>
```

### Example | 範例

```
feat(ui): Add group ID lookup form

新增群組 ID 查詢表單功能。
Add a form for users to look up Telegram group IDs.

功能包含 | Features include:
- Input validation | 輸入驗證
- Error handling | 錯誤處理
- Loading indicator | 載入指示器

Closes #123
```

---

## Typography Standards | 排版標準

### Chinese-English Mixed Text | 中英混合文字

**Add spaces between Chinese and English | 中英文之間加空格**:

```markdown
✅ CORRECT | 正確:
本專案使用 GitHub Flow 工作流程，採用 Squash Merge 策略。

❌ WRONG | 錯誤:
本專案使用GitHub Flow工作流程，採用Squash Merge策略。
```

### Punctuation | 標點符號

**Use Chinese punctuation in Chinese text | 中文文字使用中文標點**:

```markdown
✅ CORRECT | 正確:
專案包含：群組查詢、頻道查詢、用戶查詢。

❌ WRONG | 錯誤:
專案包含:群組查詢,頻道查詢,用戶查詢.
```

**Use English punctuation in code and English text | 程式碼與英文使用英文標點**:

```javascript
// ✅ CORRECT: English punctuation in code comments
// This function validates the input, checks the API, and returns the result.

// ❌ WRONG: Chinese punctuation in English
// This function validates the input，checks the API，and returns the result。
```

### Numbers | 數字

**Use Arabic numerals | 使用阿拉伯數字**:

```markdown
✅ CORRECT | 正確:
專案包含 3 種查詢功能、支援 2 種語言。

❌ WRONG | 錯誤:
專案包含三種查詢功能、支援兩種語言。
```

---

## Terminology Glossary | 術語詞彙表

### Common Terms | 常見術語

| English | 繁體中文 | Notes | 備註 |
|---------|---------|-------|------|
| Group | 群組 | Telegram group | |
| Channel | 頻道 | Telegram channel | |
| User | 用戶 | Telegram user | |
| Bot | 機器人 | Telegram bot | |
| ID | ID | Keep English | 保留英文 |
| API | API | Keep English | 保留英文 |
| Token | Token | Keep English | 保留英文 |
| Commit | Commit | Keep English | 保留英文 |
| Pull Request | Pull Request | Keep English | 保留英文 |
| Branch | 分支 | | |
| Merge | 合併 | | |
| Repository | 儲存庫 | | |

### Project-Specific Terms | 專案特定術語

| English | 繁體中文 |
|---------|---------|
| ID Finder | ID 查詢器 |
| Group Lookup | 群組查詢 |
| Channel Lookup | 頻道查詢 |
| User Lookup | 用戶查詢 |

---

## Error Messages | 錯誤訊息

### User-Facing Errors | 使用者錯誤訊息

Use bilingual for user-facing error messages:
使用者錯誤訊息使用雙語：

```javascript
const errors = {
    INVALID_ID: {
        en: 'Invalid Telegram ID format',
        zh: '無效的 Telegram ID 格式'
    },
    NOT_FOUND: {
        en: 'Group or channel not found',
        zh: '找不到群組或頻道'
    },
    API_ERROR: {
        en: 'Failed to connect to Telegram API',
        zh: '無法連接 Telegram API'
    }
};
```

### System Errors | 系統錯誤

Use English for system/log errors:
系統/日誌錯誤使用英文：

```javascript
// ✅ English for logging
console.error('Failed to fetch group data:', error);
throw new Error('API request timeout');
```

---

## Version History | 版本歷史

| Version | Date | Changes |
|---------|------|---------|
| 版本 | 日期 | 變更 |
| 1.0.0 | 2025-12-05 | Initial locale standard | 初版地區標準 |

---

## References | 參考資料

- [Chinese Copywriting Guidelines](https://github.com/sparanoid/chinese-copywriting-guidelines)
- [Universal Documentation Standards](https://github.com/AsiaOstrich/universal-doc-standards)

---

## License | 授權

This standard is released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Adapted from [Universal Documentation Standards](https://github.com/AsiaOstrich/universal-doc-standards).

本標準以 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 授權發布。
改編自 [Universal Documentation Standards](https://github.com/AsiaOstrich/universal-doc-standards)。
