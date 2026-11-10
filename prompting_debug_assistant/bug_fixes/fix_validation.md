# Fix Validation Report

## Bug 1 – bug1_fixed.py
- **Command**: `python bug1_fixed.py` and `python test_bugs.py`
- **Input**: prices=[12.50, 8.00, 4.25], tax_rate=0.10
- **Expected Output**: Total: 27.225
- **Actual Output**:
  ```
  Total: 27.225
  ```
- **Test**: `assert abs(calculate_total(...) - 27.225) < 1e-9` passed
- **Fix confirmed**: ✔ Yes. The missing `:` operator was restored and the script now runs.

## Bug 2 – bug2_fixed.js
- **Command**: `node bug2_fixed.js` and `node test_bugs.js`
- **Input**: cart = Notebook (12 × 2) + Pen set (9 × 1), isMember=false
- **Expected Output**: 41
- **Actual Output**:
  ```
  41
  ```
- **Additional assertions**: getShippingCost(0)=8, (33)=8, (50)=0, (60)=0, all passed
- **Fix confirmed**: ✔ Yes. Shipping is free at or above 50, otherwise 8. Membership does not affect shipping.

## Bug 3 – bug3_fixed.py
- **Command**: `python bug3_fixed.py` and `python test_bugs.py`
- **Input**: Aylin [85,90,78], Murad [92,88,95], Leyla []
- **Expected Output**: Averages 84.33 and 91.67, and "N/A (no recorded scores)" for Leyla
- **Actual Output**:
  ```
  Student: Aylin
  Scores: [85, 90, 78]
  Average: 84.33
  Student: Murad
  Scores: [92, 88, 95]
  Average: 91.67
  Student: Leyla
  Scores: []
  Average: N/A (no recorded scores)
  ```
- **Fix confirmed**: ✔ Yes. The empty list no longer raises ZeroDivisionError.

## Bug 4 – bug4_fixed.c
- **Command**: `gcc -Wall -Wextra bug4_fixed.c -o bug4 && ./bug4`
- **Input**: temperatures = {18, 21, 19, 23, 20}
- **Expected Output**: Total: 101, Average: 20.20
- **Actual Output**:
  ```
  Recorded temperatures:
  18 21 19 23 20 
  Total: 101
  Average: 20.20
  ```
- **Fix confirmed**: ✔ Yes. The loop uses `i < count`, so there is no out-of-bounds read. It compiles with no warnings.

## Bug 5 – bug5_fixed.js
- **Command**: `node bug5_fixed.js` and `node test_bugs.js`
- **Input**: scores = [9, 80, 100, 25]
- **Expected Output**: 9, 25, 80, 100 (one per line)
- **Actual Output**:
  ```
  Leaderboard scores:
  9
  25
  80
  100
  ```
- **Fix confirmed**: ✔ Yes. The comparator `(a, b) => a - b` sorts numerically instead of as strings.

## Manual Tweaks
- Added `module.exports` guards to bug2/bug5 so the test file can import them. No logic changes.
- No other manual changes beyond the AI-suggested fixes.

## Test Script Results
```
> python test_bugs.py
Student: Aylin
Scores: [85, 90, 78]
Average: 84.33
Student: Murad
Scores: [92, 88, 95]
Average: 91.67
Student: Leyla
Scores: []
Average: N/A (no recorded scores)
All Python assertions passed
> node test_bugs.js
41
Leaderboard scores:
9
25
80
100
All JS assertions passed
```
