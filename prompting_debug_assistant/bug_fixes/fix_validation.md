# Fix Validation Report

## Bug 1 – `bug1_fixed.py`

**Test Case**: Calculate the total for prices `[12.50, 8.00, 4.25]` with a 10% tax rate.

**Expected Output**: `27.225`

**Actual Output**: `27.225`

**Result**: PASS – The function correctly calculates the subtotal, applies the tax rate, and returns the total.

## Bug 2 – `bug2_fixed.js`

**Test Cases**:

| Input (Order Subtotal) | Expected Output | Actual Output |
|---|---:|---:|
| 33 | 41 | 41 |
| 0 | 8 | 8 |
| 50 | 50 | 50 |
| 60 | 60 | 60 |

**Result**: PASS – All four test cases passed. Orders below $50 include standard shipping ($8), while orders of $50 or more qualify for free shipping. Membership status does not affect shipping costs.

## Bug 3 – `bug3_fixed.py`

**Test Cases**:

| Input (Scores) | Expected Output | Actual Output |
|---|---|---|
| `[85, 90, 78]` | Average: 84.33 | Average: 84.33 |
| `[92, 88, 95]` | Average: 91.67 | Average: 91.67 |
| `[]` | N/A (no recorded scores) | N/A (no recorded scores) |

**Result**: PASS – All three cases handled correctly, including the empty-list edge case without raising a division-by-zero exception.

## Bug 4 – `bug4_fixed.c`

**Test Case**: Process the array `[18, 21, 19, 23, 20]`.

**Expected Output**: Total = 101, Average = 20.20.

**Actual Output**: Total = 101, Average = 20.20.

**Result**: PASS – All five array elements are processed exactly once, without accessing an index outside the array bounds.

## Bug 5 – `bug5_fixed.js`

**Test Case**: Sort the scores `[9, 80, 100, 25]` in ascending numerical order.

**Expected Output**: `[9, 25, 80, 100]`.

**Actual Output**: `[9, 25, 80, 100]`.

**Result**: PASS – Scores are sorted in ascending numerical order rather than lexicographical order.
