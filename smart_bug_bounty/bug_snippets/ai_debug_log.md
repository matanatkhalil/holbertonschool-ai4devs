# AI Debugging Log

## bug1.py – Incorrect Duplicate Removal

**AI Explanation:** The function removes an element from the result list whenever it encounters a duplicate. This causes previously added unique values to disappear when an element occurs multiple times.

**Suggested Fix:** Remove the `else` block and only append an item if it is not already in the result list.

**Confidence:** High

## bug2.js – Incorrect Shopping Cart Total

**AI Explanation:** The function adds the price of each item only once, regardless of its quantity. This results in an incorrect shopping cart total.

**Suggested Fix:** Multiply `item.price` by `item.quantity` when calculating the total:

```javascript
total += item.price * item.quantity;
```

**Confidence:** High

## bug3.java – Incorrect Bank Account Withdrawal

**AI Explanation:** The withdrawal method checks whether the requested amount is less than or equal to the current balance but does not check whether the amount is positive. A negative withdrawal therefore increases the account balance.

**Suggested Fix:** Update the condition to check both requirements:

```java
if (amount > 0 && amount <= balance) {
```

**Confidence:** High

## bug4.py – Incorrect File Processing

**AI Explanation:** The function compares words without removing surrounding punctuation. For example, `Python,` and `Python.` are treated as different words from `Python`, causing some occurrences to be missed.

**Suggested Fix:** Use Python's `string.punctuation` and `strip()` to remove punctuation before comparing words:

```python
import string

for word in words:
    cleaned_word = word.strip(string.punctuation)
    if cleaned_word.lower() == target_word.lower():
        word_count += 1
```

**Confidence:** High