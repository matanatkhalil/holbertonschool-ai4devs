# Bug Descriptions

These snippets are intentionally flawed. Their purpose is to provide reproducible examples for the debugging exercises. The issue descriptions state the intended behavior without giving away the exact correction.

## Bug 1 – `bug1.py`

**Intended Behavior**: Calculate and return the total price of a list of items after applying a tax rate, then print the result.

**Issue Type**: Syntax error.

**Notes**: The program should run when supplied with a list of prices and a valid tax rate.

## Bug 2 – `bug2.js`

**Intended Behavior**: Calculate an order's subtotal and add standard shipping unless the order reaches the free-shipping threshold. Members should receive free shipping only if that is an explicitly defined business rule.

**Issue Type**: Logical error.

**Notes**: Compare the shipping decision with the intended policy for members and non-members, including orders below and at the free-shipping threshold.

## Bug 3 – `bug3.py`

**Intended Behavior**: Print a report for each student, including their name, scores, and average score. The program should handle a student who has no recorded scores without crashing.

**Issue Type**: Runtime exception.

**Notes**: One student has an empty score list. The report should handle this case clearly.

## Bug 4 – `bug4.c`

**Intended Behavior**: Print every recorded temperature exactly once, calculate their sum, and display the average.

**Issue Type**: Off-by-one / loop boundary error.

**Notes**: The array contains five values. The loop should process only valid array elements.

## Bug 5 – `bug5.js`

**Intended Behavior**: Return and print player scores in ascending numerical order.

**Issue Type**: Misuse of a library method / data type.

**Notes**: Scores are numbers, so the ordering must be numeric rather than based on their string representations.
