# AI Collaboration Anti-Hallucination Standards
# AI 協作防幻覺標準

**Version | 版本**: 1.0.0
**Last Updated | 最後更新**: 2025-12-05
**Applicability | 適用範圍**: telegram-id-finder project | telegram-id-finder 專案

---

## Purpose | 目的

This standard defines strict guidelines for AI assistants to prevent hallucination (generating false or unverified information) when analyzing code, making recommendations, or documenting systems.

本標準定義 AI 助理的嚴格準則，以防止在分析程式碼、提出建議或撰寫系統文件時產生幻覺（生成錯誤或未經驗證的資訊）。

---

## Core Principles | 核心原則

### 1. Evidence-Based Analysis Only | 僅基於證據的分析

**Rule | 規則**: Only analyze and reference content that has been explicitly provided or read.
僅分析和引用已明確提供或讀取的內容。

**Guidelines | 指引**:
- ✅ Analyze code files that have been read using file reading tools
  分析已使用檔案讀取工具讀取的程式碼檔案
- ✅ Reference documentation that has been fetched
  引用已擷取的文件
- ✅ Cite configuration files that have been inspected
  引用已檢視的設定檔
- ❌ Do NOT speculate about APIs, functions, or configurations not seen
  不要猜測未看過的 API、函式或設定
- ❌ Do NOT assume framework behavior without verification
  不要在未驗證的情況下假設框架行為
- ❌ Do NOT fabricate requirement details
  不要捏造需求細節

**Examples | 範例**:

✅ **Correct | 正確**:
```
[Evidence | 證據] In src/api/telegram.js:45, the API call uses the 'node-telegram-bot-api' library
[Evidence | 證據] 在 src/api/telegram.js:45，API 呼叫使用 'node-telegram-bot-api' 套件
```

❌ **Incorrect | 錯誤**:
```
This system uses Redis for caching (code not reviewed)
此系統使用 Redis 做快取（程式碼未審查）
```

---

### 2. Explicit Source Attribution | 明確來源標註

**Rule | 規則**: All code references must include file path and line number.
所有程式碼引用必須包含檔案路徑與行號。

**Format | 格式**:
```
[file_path:line_number] - Description | 描述
```

**Examples | 範例**:

✅ **Correct | 正確**:
```
src/utils/telegram.js:142 - Group ID extraction logic
src/utils/telegram.js:142 - 群組 ID 提取邏輯
```

❌ **Incorrect | 錯誤**:
```
The telegram service handles group lookups (no file/line reference)
telegram 服務處理群組查詢（無檔案/行號引用）
```

---

### 3. Classify Certainty Levels | 分類確定性等級

**Rule | 規則**: Clearly distinguish between confirmed facts, inferences, and unknowns.
明確區分已確認事實、推測與未知事項。

**Classification Tags | 分類標籤**:

| Tag | English | 繁體中文 | Use When | 使用時機 |
|-----|---------|---------|----------|---------|
| `[Confirmed]` | Confirmed | 已確認 | Direct evidence from code/docs | 直接來自程式碼/文件的證據 |
| `[Inferred]` | Inferred | 推測 | Logical deduction from available evidence | 基於現有證據的邏輯推論 |
| `[Assumption]` | Assumption | 假設 | Based on common patterns (needs verification) | 基於常見模式（需驗證）|
| `[Unknown]` | Unknown | 未知 | Information not available | 資訊不可得 |
| `[Need Confirmation]` | Need Confirmation | 需確認 | Requires user clarification | 需要使用者澄清 |

**Examples | 範例**:

✅ **Correct | 正確**:
```
[Confirmed | 已確認] src/api/telegram.js:12 - Using 'node-telegram-bot-api' package
[Inferred | 推測] Based on the file structure, likely using Express.js
[Need Confirmation | 需確認] Should the tool support private channels?
```

---

### 4. Prohibited Behaviors | 禁止行為

**AI assistants MUST NOT | AI 助理禁止**:

1. **Fabricate APIs or Function Signatures | 捏造 API 或函式簽章**
   - ❌ Do NOT invent method names, parameters, or return types
     不要捏造方法名稱、參數或回傳類型
   - ✅ DO read the actual source code or ask the user
     請讀取實際原始碼或詢問使用者

2. **Assume Requirements | 假設需求**
   - ❌ Do NOT guess user needs or business rules
     不要猜測使用者需求或業務規則
   - ✅ DO ask clarifying questions when requirements are ambiguous
     當需求模糊時請提出澄清問題

3. **Speculate About Unread Code | 猜測未讀程式碼**
   - ❌ Do NOT describe functionality of files not reviewed
     不要描述未審查檔案的功能
   - ✅ DO explicitly state "Need to read [file] to confirm"
     請明確表示「需要讀取 [file] 以確認」

4. **Invent Configuration | 捏造設定**
   - ❌ Do NOT assume environment variables, config keys, or database schemas
     不要假設環境變數、設定鍵或資料庫結構
   - ✅ DO review actual configuration files
     請審查實際設定檔

5. **Hallucinate Errors or Bugs | 幻覺錯誤或 Bug**
   - ❌ Do NOT claim code has issues without evidence
     不要在無證據的情況下聲稱程式碼有問題
   - ✅ DO analyze actual code and cite specific lines
     請分析實際程式碼並引用具體行號

---

## Implementation Checklist | 實施檢查清單

Before making any statement about code, requirements, or architecture, verify:
在對程式碼、需求或架構做出任何陳述前，請驗證:

- [ ] **Source Verified | 來源已驗證**
  Have I read the actual file/document? | 我是否已讀取實際的檔案/文件？

- [ ] **Reference Cited | 引用已標註**
  Did I include file path and line number? | 我是否已包含檔案路徑與行號？

- [ ] **Certainty Classified | 確定性已分類**
  Did I tag as [Confirmed], [Inferred], [Assumption], [Unknown], or [Need Confirmation]?
  我是否已標註為 [已確認]、[推測]、[假設]、[未知] 或 [需確認]？

- [ ] **No Fabrication | 無捏造**
  Did I avoid inventing APIs, configs, or requirements?
  我是否避免了捏造 API、設定或需求？

- [ ] **User Clarification | 使用者澄清**
  Did I ask for clarification on ambiguous points?
  我是否對模糊點請求澄清？

---

## AI Assistant Workflow | AI 助理工作流程

```
┌─────────────────────────────────┐
│  User Request Received          │
│  收到使用者請求                  │
└─────────────┬───────────────────┘
              │
              ▼
┌─────────────────────────────────┐
│  Identify Information Needed    │
│  識別所需資訊                    │
└─────────────┬───────────────────┘
              │
              ▼
         ┌────┴────┐
         │ Available? │
         │ 可用？     │
         └────┬────┘
              │
      ┌───────┴───────┐
      │               │
     YES / 是        NO / 否
      │               │
      ▼               ▼
┌──────────┐   ┌─────────────┐
│  Read/   │   │  Ask User   │
│  Analyze │   │  for Info   │
│  讀取/   │   │  詢問使用者  │
│  分析    │   │  資訊       │
└────┬─────┘   └──────┬──────┘
     │                │
     ▼                ▼
┌─────────────────────────────────┐
│  Tag Response with:             │
│  標註回應：                      │
│  - [Confirmed] for facts        │
│  - [Inferred] for deductions    │
│  - [Need Confirmation] for gaps │
└─────────────┬───────────────────┘
              │
              ▼
┌─────────────────────────────────┐
│  Cite Sources (file:line)       │
│  引用來源（檔案:行號）           │
└─────────────┬───────────────────┘
              │
              ▼
┌─────────────────────────────────┐
│  Deliver Response               │
│  提交回應                        │
└─────────────────────────────────┘
```

---

## Version History | 版本歷史

| Version | Date | Changes |
|---------|------|---------|
| 版本 | 日期 | 變更 |
| 1.0.0 | 2025-12-05 | Initial standard published | 初版發布 |

---

## License | 授權

This standard is released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Adapted from [Universal Documentation Standards](https://github.com/AsiaOstrich/universal-doc-standards).

本標準以 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 授權發布。
改編自 [Universal Documentation Standards](https://github.com/AsiaOstrich/universal-doc-standards)。
