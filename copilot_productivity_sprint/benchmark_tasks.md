# Benchmark Tasks – Copilot Productivity Sprint

## Introduction

This document defines three JavaScript coding tasks for evaluating developer productivity with and without AI coding assistance.

Each task is designed to take approximately 15–30 minutes and focuses on a different programming skill.

The same requirements and acceptance criteria will be used in both development sessions to ensure a fair comparison.

---

## Task 1 – Shopping Cart Calculator

**Estimated Time:** 20 minutes

**Difficulty:** Beginner–Intermediate

### Requirements

Implement a function called `calculateCartTotal` that calculates the total price of items in a shopping cart.

The function should:

- Accept an array of shopping cart items.
- Calculate the total price using each item's price and quantity.
- Apply a discount percentage if provided.
- Return the final amount rounded to two decimal places.

### Inputs

An array of objects containing:

- `name`: Product name (string).
- `price`: Price per item (positive number).
- `quantity`: Number of items (positive integer).

An optional discount percentage (number between 0 and 100).

Example:

```javascript
const cart = [
  { name: "Laptop", price: 800, quantity: 1 },
  { name: "Mouse", price: 25, quantity: 2 },
  { name: "Keyboard", price: 50, quantity: 1 }
];

calculateCartTotal(cart, 10);
```

### Outputs

The function should return the final cart total after applying the discount.

Expected output:

```javascript
810
```

### Acceptance Criteria

- Correctly calculates the total using price and quantity.
- Applies the specified discount percentage.
- Returns the total rounded to two decimal places.
- Returns `0` for an empty cart.
- Rejects invalid prices, quantities, or discount percentages with an appropriate error.

---

## Task 2 – Student Grade Analyzer

**Estimated Time:** 25 minutes

**Difficulty:** Intermediate

### Requirements

Implement a function called `analyzeGrades` that processes a collection of student records and generates a summary of their academic performance.

The function should:

- Calculate each student's average score.
- Assign a letter grade based on the average.
- Calculate the overall class average.
- Identify the student with the highest average score.

Use the following grading scale:

| Average Score | Letter Grade |
|---|---|
| 90–100 | A |
| 80–89 | B |
| 70–79 | C |
| 60–69 | D |
| Below 60 | F |

### Inputs

An array of student objects containing:

- `name`: Student's name (string).
- `scores`: Array of numerical scores between 0 and 100.

Example:

```javascript
const students = [
  { name: "Aylin", scores: [85, 90, 95] },
  { name: "Murad", scores: [70, 80, 75] },
  { name: "Leyla", scores: [95, 100, 90] }
];

analyzeGrades(students);
```

### Outputs

An object containing:

- `students`: Each student's name, average score, and letter grade.
- `classAverage`: Average score across all students.
- `topStudent`: Name of the student with the highest average.

Expected output:

```javascript
{
  students: [
    { name: "Aylin", average: 90, grade: "A" },
    { name: "Murad", average: 75, grade: "C" },
    { name: "Leyla", average: 95, grade: "A" }
  ],
  classAverage: 86.67,
  topStudent: "Leyla"
}
```

### Acceptance Criteria

- Correctly calculates individual student averages.
- Assigns letter grades according to the specified grading scale.
- Calculates the overall class average correctly.
- Identifies the student with the highest average.
- Handles empty student lists and students with empty score arrays appropriately.
- Rejects invalid scores outside the range of 0–100.

---

## Task 3 – Input Data Validator

**Estimated Time:** 20 minutes

**Difficulty:** Intermediate

### Requirements

Implement a function called `validateUser` that validates user registration data.

The function should check:

- Whether the username contains at least 3 characters.
- Whether the email has a valid basic email format.
- Whether the password contains at least 8 characters.
- Whether the password contains at least one uppercase letter and one number.

The function should collect all validation errors rather than stopping after the first invalid field.

### Inputs

An object containing:

- `username`: User's username (string).
- `email`: User's email address (string).
- `password`: User's password (string).

Example:

```javascript
const user = {
  username: "john",
  email: "john@example.com",
  password: "Password123"
};

validateUser(user);
```

### Outputs

An object containing:

- `isValid`: Boolean indicating whether the input is valid.
- `errors`: Array of validation error messages.

Expected output for valid input:

```javascript
{
  isValid: true,
  errors: []
}
```

Example output for invalid input:

```javascript
{
  isValid: false,
  errors: [
    "Username must contain at least 3 characters.",
    "Email address is invalid.",
    "Password must contain at least 8 characters."
  ]
}
```

### Acceptance Criteria

- Validates username length.
- Checks email format.
- Checks password length, uppercase letters, and numbers.
- Returns all applicable validation errors.
- Returns `isValid: true` only when all validation checks pass.
- Handles missing or incorrectly typed input fields appropriately.

---

## 4. Benchmarking Guidelines

To ensure a fair comparison between manual development and AI-assisted development:

1. Complete all three tasks without AI assistance first.
2. Record the time spent on each task.
3. Complete the same three tasks again using GitHub Copilot.
4. Use identical requirements and acceptance criteria in both sessions.
5. Record the time spent on each AI-assisted task.
6. Test both implementations using the same test cases.
7. Record any bugs, corrections, or additional changes required.

### Metrics to Collect

| Metric | Description |
|---|---|
| Completion Time | Total time required to complete each task. |
| Lines of Code | Number of lines in the final implementation. |
| Code Quality | Readability, maintainability, and correctness. |
| Test Results | Number of passed and failed test cases. |
| AI Assistance | Number and type of AI suggestions used. |
| Manual Corrections | Changes required to fix or improve AI-generated code. |

## 5. Conclusion

These three benchmark tasks provide a small but varied set of programming challenges involving calculations, data processing, and input validation.

Using the same tasks in both manual and AI-assisted sessions will help evaluate how GitHub Copilot affects development speed, code quality, and the amount of manual effort required.
