# Fix Validation Report

## Bug 1 – bug1_fixed.py
- **Input**: prices=[12.50, 8.00, 4.25], tax_rate=0.10
- **Expected Output**: Total: 27.225
- **Actual Output**: Total: 27.225 ✅

## Bug 2 – bug2_fixed.js
- **Input**: items subtotal 33 (cart: Notebook 12×2 + Pen set 9×1), isMember=false
- **Expected Output**: 41
- **Actual Output**: 41 ✅

- **Input**: items subtotal 0 (empty cart)
- **Expected Output**: 8
- **Actual Output**: 8 ✅

- **Input**: items subtotal 50
- **Expected Output**: 50
- **Actual Output**: 50 ✅

- **Input**: items subtotal 60
- **Expected Output**: 60
- **Actual Output**: 60 ✅

## Bug 3 – bug3_fixed.py
- **Input**: scores=[85, 90, 78]
- **Expected Output**: Average: 84.33
- **Actual Output**: Average: 84.33 ✅

- **Input**: scores=[92, 88, 95]
- **Expected Output**: Average: 91.67
- **Actual Output**: Average: 91.67 ✅

- **Input**: scores=[]
- **Expected Output**: Average: N/A (no recorded scores)
- **Actual Output**: Average: N/A (no recorded scores) ✅

## Bug 4 – bug4_fixed.c
- **Input**: temperatures=[18, 21, 19, 23, 20]
- **Expected Output**: Total: 101, Average: 20.20
- **Actual Output**: Total: 101, Average: 20.20 ✅

## Bug 5 – bug5_fixed.js
- **Input**: scores=[9, 80, 100, 25]
- **Expected Output**: [9, 25, 80, 100]
- **Actual Output**: [9, 25, 80, 100] ✅

## Manual Tweaks
- No manual changes were needed beyond the AI-suggested fixes.