# Fix Validation

## bug1_fixed.py – Duplicate Removal

- **Original Issue:** The function removed previously added elements when duplicates were encountered multiple times.
- **Fix Applied:** Removed the incorrect `else` branch. Elements are now added only if they are not already present.
- **Test Cases:**
  - Input: `[1, 2, 2, 3, 3, 3, 4, 4]` → Expected: `[1, 2, 3, 4]`
  - Input: `[]` → Expected: `[]`
  - Input: `[5, 5, 5]` → Expected: `[5]`
  - Input: `[1, 2, 1, 3]` → Expected: `[1, 2, 3]`
- **Test Results:** PASS – All 4 test cases passed.

## bug2_fixed.js – Shopping Cart Total

- **Original Issue:** The function added each item's price only once instead of multiplying it by its quantity.
- **Fix Applied:** Multiplied `item.price` by `item.quantity` when calculating the total.
- **Test Cases:**
  - Book (15 × 2), Pen (3 × 5), Bag (30 × 1) → Expected: `75`
  - Empty cart → Expected: `0`
  - Item with quantity `0` → Expected: `0`
  - Item with price `4` and quantity `3` → Expected: `12`
- **Test Results:** PASS – All 4 test cases passed.

## bug3_fixed.java – Bank Account Withdrawal

- **Original Issue:** Negative withdrawal amounts were accepted, incorrectly increasing the account balance.
- **Fix Applied:** Added validation requiring the withdrawal amount to be greater than zero and not exceed the available balance.
- **Test Cases:**
  - Initial balance `500`, withdraw `-100` → Expected: `false`, balance `500`
  - Initial balance `500`, withdraw `100` → Expected: `true`, balance `400`
  - Initial balance `400`, withdraw `600` → Expected: `false`, balance `400`
  - Initial balance `400`, withdraw `0` → Expected: `false`, balance `400`
- **Test Results:** PASS – All 4 test cases passed. Java compilation and execution were successful.

## bug4_fixed.py – Word Occurrence Counting

- **Original Issue:** Words followed by punctuation were not counted because punctuation remained attached during comparison.
- **Fix Applied:** Imported Python's `string` module and used `strip(string.punctuation)` to remove surrounding punctuation before comparing words.
- **Test Cases:**
  - Text: `Python, is useful. I like PYTHON!` → Expected: `2`
  - Text: `PYTHON; python.` → Expected: `2`
  - Text: `Java is useful.` → Expected: `0`
- **Test Results:** PASS – All 3 test cases passed. File reading, case-insensitive comparison, and punctuation handling worked as expected.

## Overall Validation Summary

- **Total Test Cases:** 15
- **Passed:** 15
- **Failed:** 0
- **Overall Result:** PASS

All four corrected files were tested using multiple test cases. The observed outputs matched the expected results.