# Structured Bug Reports

## Bug Report 1 – bug1.py

- **File Name:** `bug1.py`
- **Bug Summary:** Syntax error in the function definition prevented the Python script from executing.
- **Root Cause:** A missing colon (`:`) at the end of the `calculate_total()` function definition.
- **Resolution:**
  - **AI-Generated:** Identified the missing colon and suggested adding it to the function definition.
  - **Manual Edits:** Applied the correction and executed the script to verify that it ran successfully.
- **Lessons Learned:** Small syntax errors can prevent an entire program from running. Always check function definitions and other Python syntax requirements when debugging.

## Bug Report 2 – bug2.js

- **File Name:** `bug2.js`
- **Bug Summary:** Incorrect discount eligibility condition caused the program to apply the discount based on membership status rather than the required order total.
- **Root Cause:** The conditional statement incorrectly included the `isMember` condition, even though discount eligibility depended only on whether the order total was at least 50.
- **Resolution:**
  - **AI-Generated:** Identified the incorrect conditional logic and suggested checking only whether `orderTotal >= 50`.
  - **Manual Edits:** Updated the condition, removed the unnecessary membership requirement, and tested different order totals to verify the discount behavior.
- **Lessons Learned:** Debugging requires checking whether conditional statements accurately represent the intended business rules. Testing values below, at, and above a threshold helps identify logical errors.

## Bug Report 3 – bug3.py

- **File Name:** `bug3.py`
- **Bug Summary:** The program encountered a runtime error when processing a student with an empty scores list.
- **Root Cause:** The average calculation did not properly handle empty lists, resulting in an invalid division by zero.
- **Resolution:**
  - **AI-Generated:** Identified the missing empty-list check and suggested handling students without recorded scores separately.
  - **Manual Edits:** Added a condition to check whether the scores list contains values before calculating the average. Updated the output to display an appropriate message when no scores are available.
- **Lessons Learned:** Always account for empty collections and other edge cases before performing calculations. Validating input data helps prevent runtime errors.

## Bug Report 4 – bug4.c

- **File Name:** `bug4.c`
- **Bug Summary:** The program incorrectly processed array elements when calculating the total and average of five temperatures.
- **Root Cause:** An incorrect loop boundary caused an off-by-one error, resulting in an attempt to access an element outside the valid array indices.
- **Resolution:**
  - **AI-Generated:** Identified the incorrect loop boundary and suggested correcting the iteration range to process exactly five elements.
  - **Manual Edits:** Applied the loop correction and compiled and executed the program to verify that all five temperatures were processed exactly once.
- **Lessons Learned:** Array indexing and loop boundaries must be handled carefully. Remember that array indices start at zero, and always test loops to ensure they do not access elements outside the array.

## Bug Report 5 – bug5.js

- **File Name:** `bug5.js`
- **Bug Summary:** The program did not sort numeric values in the correct ascending order.
- **Root Cause:** The JavaScript `sort()` method was used without a comparison function. By default, it sorts elements as strings rather than comparing them numerically.
- **Resolution:**
  - **AI-Generated:** Identified the default lexicographical sorting behavior and suggested providing a numeric comparison function.
  - **Manual Edits:** Updated the sorting implementation to compare numbers numerically and verified the result using an array containing values of different digit lengths.
- **Lessons Learned:** Understand the default behavior of built-in methods rather than assuming they work as expected for every data type. For numeric sorting in JavaScript, explicitly provide a comparison function.

---

## Summary

Five bugs were identified, corrected, and tested across Python, JavaScript, and C.

The debugging process demonstrated the importance of:
- Identifying root causes rather than simply addressing symptoms.
- Critically evaluating AI-generated suggestions before applying them.
- Making manual adjustments when necessary.
- Testing corrected code with normal inputs and edge cases.
- Verifying that the actual output matches the expected behavior.
