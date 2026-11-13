# Fix Validation

## bug1_fixed.py – Duplicate Removal

- **Original Issue:** The function removed an existing item when it encountered a duplicate, causing values appearing multiple times to disappear.
- **Fix Applied:** Removed the `else` branch. An item is now appended only if it is not already in the result.
- **Test Cases:**
  - Input: `[1, 2, 2, 3, 3, 3, 4, 4]` → Expected: `[1, 2, 3, 4]`
  - Input: `[]` → Expected: `[]`
  - Input: `[5, 5, 5]` → Expected: `[5]`
- **Test Results:** All 3 test cases should return the expected output.

## bug2_fixed.js – Shopping Cart Total

- **Original Issue:** The function added each item's price once instead of accounting for its quantity.
- **Fix Applied:** Multiplied `item.price` by `item.quantity` when calculating the total.
- **Test Cases:**
  - Book (15 × 2), Pen (3 × 5), Bag (30 × 1) → Expected: `75`
  - Empty cart → Expected: `0`
  - Item with quantity `0` → Expected: `0`
- **Test Results:** Expected totals: `75`, `0`, and `0`.

## bug3_fixed.java – Bank Account Withdrawal

- **Original Issue:** Negative withdrawal amounts were accepted and increased the account balance.
- **Fix Applied:** Added validation requiring the withdrawal amount to be greater than zero and not exceed the available balance.
- **Test Cases:**
  - Initial balance `500`, withdraw `-100` → Expected: `false`, balance `500`
  - Initial balance `500`, withdraw `100` → Expected: `true`, balance `400`
  - Initial balance `500`, withdraw `600` → Expected: `false`, balance `500`
  - Initial balance `500`, withdraw `0` → Expected: `false`, balance `500`
- **Test Results:** The negative and valid withdrawal cases are included in the Java main method. Additional cases should be executed separately.

## bug4_fixed.py – Word Occurrence Counting

- **Original Issue:** Words followed by punctuation were not counted because punctuation remained attached during comparison.
- **Fix Applied:** Imported `string` and used `strip(string.punctuation)` to remove surrounding punctuation before comparing words.
- **Test Cases:**
  - Text: `Python, is useful. I like PYTHON!` → Expected: `2`
  - Text: `PYTHON; python.` → Expected: `2`
  - Text: `Java is useful.` → Expected: `0`
- **Test Results:** The updated logic handles common punctuation. Execute the cases using a sample text file to verify.