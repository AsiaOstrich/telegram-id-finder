# Testing Standards
# 測試標準

**Version | 版本**: 1.0.0
**Last Updated | 最後更新**: 2025-12-05
**Applicability | 適用範圍**: telegram-id-finder project | telegram-id-finder 專案

---

## Purpose | 目的

This standard defines testing conventions and best practices to ensure software quality through systematic testing at multiple levels.

本標準定義測試慣例與最佳實踐，透過多層級的系統化測試確保軟體品質。

---

## Testing Pyramid | 測試金字塔

```
                    ┌─────────┐
                    │   E2E   │  ← Fewer, slower, expensive
                    │  端對端  │    較少、較慢、成本高
                   ─┴─────────┴─
                  ┌─────────────┐
                  │     ST      │  ← System Testing
                  │   系統測試   │    整體系統驗證
                 ─┴─────────────┴─
                ┌─────────────────┐
                │       IT        │  ← Integration Testing
                │     整合測試     │    模組間互動
               ─┴─────────────────┴─
              ┌─────────────────────┐
              │         UT          │  ← Unit Testing (Foundation)
              │       單元測試       │    最多、最快、成本低
              └─────────────────────┘
```

### Recommended Ratio | 建議比例

| Level | Percentage | Execution Time |
|-------|------------|----------------|
| 層級 | 百分比 | 執行時間 |
| UT (單元測試) | 70% | < 10 min |
| IT (整合測試) | 20% | < 30 min |
| ST (系統測試) | 7% | < 2 hours |
| E2E (端對端) | 3% | < 4 hours |

---

## Unit Testing (UT) | 單元測試

### Definition | 定義

Tests individual functions, methods, or classes in isolation from external dependencies.

測試個別函式、方法或類別，與外部相依性隔離。

### Characteristics | 特性

- **Isolated | 獨立**: No database, network, or file system access | 不存取資料庫、網路或檔案系統
- **Fast | 快速**: Each test < 100ms | 每個測試 < 100ms
- **Deterministic | 確定性**: Same input always produces same output | 相同輸入永遠產生相同輸出

### Scope | 範圍

| ✅ Include | ❌ Exclude |
|-----------|-----------|
| Single function/method | Database queries |
| Single class | External API calls |
| Pure business logic | File I/O operations |
| Data transformations | Multi-class interactions |
| Validation rules | |

### Naming Convention | 命名慣例

**File Naming | 檔案命名**:
```
[ClassName].test.[ext]
[ClassName].spec.[ext]

Examples:
  IdValidator.test.ts
  TelegramApi.test.js
```

**Method Naming | 方法命名**:
```
[MethodName]_[Scenario]_[ExpectedResult]
should_[ExpectedBehavior]_when_[Condition]

Examples:
  validateGroupId_withValidId_returnsTrue()
  should_return_null_when_channel_not_found()
```

### Coverage Guidelines | 覆蓋率指引

| Metric | Minimum | Recommended |
|--------|---------|-------------|
| 指標 | 最低 | 建議 |
| Line Coverage | 70% | 85% |
| Branch Coverage | 60% | 80% |
| Function Coverage | 80% | 90% |

---

## Integration Testing (IT) | 整合測試

### Definition | 定義

Tests interactions between multiple components, modules, or external systems.

測試多個元件、模組或外部系統之間的互動。

### Characteristics | 特性

- **Component Integration | 元件整合**: Tests module boundaries | 測試模組邊界
- **Real Dependencies | 真實相依性**: Uses actual APIs (often mocked) | 使用實際 API（通常模擬）
- **Slower | 較慢**: Each test typically 1-10 seconds | 每個測試通常 1-10 秒

### Scope for This Project | 本專案範圍

| ✅ Include | ❌ Exclude |
|-----------|-----------|
| Telegram API interactions | Full user workflows |
| ID validation + API lookup | UI interactions |
| Error handling flows | |

### Naming Convention | 命名慣例

**File Naming | 檔案命名**:
```
[ComponentName].integration.test.[ext]
[ComponentName].itest.[ext]

Examples:
  TelegramService.integration.test.ts
  api-client.itest.js
```

---

## End-to-End Testing (E2E) | 端對端測試

### Definition | 定義

Tests complete user workflows from the user interface through all system layers.

從使用者介面測試完整的使用者工作流程，貫穿所有系統層。

### Characteristics | 特性

- **User Perspective | 使用者視角**: Simulates real user interactions | 模擬真實使用者互動
- **Full Stack | 全棧**: UI → API → External Services | UI → API → 外部服務
- **Slowest | 最慢**: Each test typically 30 seconds to several minutes | 每個測試通常 30 秒到數分鐘

### Scope for This Project | 本專案範圍

| ✅ Include | ❌ Exclude |
|-----------|-----------|
| Critical user journeys | Every possible user path |
| ID lookup workflows | Edge cases (use UT/IT) |
| Error message display | Performance benchmarking |

### Naming Convention | 命名慣例

**File Naming | 檔案命名**:
```
[UserJourney].e2e.[ext]
[Feature].e2e.spec.[ext]

Examples:
  group-id-lookup.e2e.ts
  channel-search.e2e.spec.ts
```

---

## Test Doubles | 測試替身

### Types | 類型

| Type | Chinese | Purpose | Example Use |
|------|---------|---------|-------------|
| **Stub** | 樁 | Returns predefined values | Fixed API responses |
| **Mock** | 模擬物件 | Verifies interactions | Verify method called |
| **Fake** | 假物件 | Simplified implementation | In-memory storage |
| **Spy** | 間諜 | Records calls, delegates to real | Partial mocking |

### Usage by Test Level | 依測試層級使用

| Level | Recommendation |
|-------|----------------|
| UT | Use Mocks/Stubs for all external dependencies |
| IT | Use Stubs for Telegram API, minimize mocking |
| E2E | Use real components, stub only external APIs |

---

## Test Data Management | 測試資料管理

### Principles | 原則

1. **Isolation | 隔離**: Each test manages its own data | 每個測試管理自己的資料
2. **Cleanup | 清理**: Tests clean up after themselves | 測試結束後自行清理
3. **Determinism | 確定性**: Tests don't depend on shared state | 測試不依賴共享狀態
4. **Readability | 可讀性**: Test data clearly shows intent | 測試資料清楚顯示意圖

---

## Best Practices | 最佳實踐

### AAA Pattern | AAA 模式

```javascript
test('validateGroupId returns true for valid ID', () => {
    // Arrange - 準備測試資料與環境
    const validId = '-1001234567890';

    // Act - 執行被測試的行為
    const result = validateGroupId(validId);

    // Assert - 驗證結果
    expect(result).toBe(true);
});
```

### FIRST Principles | FIRST 原則

| Principle | Chinese | Description |
|-----------|---------|-------------|
| **F**ast | 快速 | Tests run quickly |
| **I**ndependent | 獨立 | Tests don't affect each other |
| **R**epeatable | 可重複 | Same result every time |
| **S**elf-validating | 自我驗證 | Clear pass/fail |
| **T**imely | 及時 | Written with production code |

### Anti-Patterns to Avoid | 應避免的反模式

| ❌ Anti-Pattern | Description |
|----------------|-------------|
| Test Interdependence | Tests that must run in specific order |
| 測試相依 | 必須依特定順序執行的測試 |
| Flaky Tests | Tests that sometimes pass, sometimes fail |
| 不穩定測試 | 有時通過、有時失敗的測試 |
| Over-Mocking | Mocking so much that nothing real is tested |
| 過度模擬 | 模擬太多導致沒有測試到真實行為 |
| Missing Assertions | Tests that verify nothing meaningful |
| 缺少斷言 | 沒有驗證有意義內容的測試 |

---

## Quick Reference Card | 快速參考卡

```
┌─────────────────────────────────────────────────────────────┐
│                    Testing Levels Summary                    │
├──────────┬──────────────────────────────────────────────────┤
│   UT     │ Single unit, isolated, mocked deps, < 100ms     │
│  單元測試 │ 單一單元、隔離、模擬相依、< 100ms               │
├──────────┼──────────────────────────────────────────────────┤
│   IT     │ Component integration, API stubs, 1-10 sec      │
│  整合測試 │ 元件整合、API 樁、1-10 秒                       │
├──────────┼──────────────────────────────────────────────────┤
│  E2E     │ User journeys, UI to API, critical paths only   │
│ 端對端   │ 使用者流程、UI 到 API、僅關鍵路徑               │
├──────────┴──────────────────────────────────────────────────┤
│                    Naming Conventions                        │
├─────────────────────────────────────────────────────────────┤
│  UT:  [Name].test.ts, [Name].spec.ts                        │
│  IT:  [Name].integration.test.ts, [Name].itest.ts           │
│  E2E: [Name].e2e.ts, [Name].e2e.spec.ts                     │
├─────────────────────────────────────────────────────────────┤
│                    Coverage Targets                          │
├─────────────────────────────────────────────────────────────┤
│  Line: 70% min / 85% recommended                            │
│  Branch: 60% min / 80% recommended                          │
│  Function: 80% min / 90% recommended                        │
└─────────────────────────────────────────────────────────────┘
```

---

## Related Standards | 相關標準

- [Anti-Hallucination Standard](anti-hallucination.md) - AI 協作防幻覺標準
- [Code Check-in Standards](checkin-standards.md) - 程式碼簽入檢查點標準
- [Commit Message Guide](commit-message-guide.md) - Commit 訊息規範

---

## Version History | 版本歷史

| Version | Date | Changes |
|---------|------|---------|
| 版本 | 日期 | 變更 |
| 1.0.0 | 2025-12-05 | Initial testing standards adapted from universal-doc-standards 初版測試標準，改編自 universal-doc-standards |

---

## References | 參考資料

- [Universal Documentation Standards - Testing Standards](https://github.com/AsiaOstrich/universal-doc-standards/blob/main/core/testing-standards.md)

---

## License | 授權

This standard is released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Adapted from [Universal Documentation Standards](https://github.com/AsiaOstrich/universal-doc-standards).

本標準以 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 授權發布。
改編自 [Universal Documentation Standards](https://github.com/AsiaOstrich/universal-doc-standards)。
