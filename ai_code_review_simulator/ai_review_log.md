# AI Review Log – Task Priority Filtering

## Review Context
**Feature:** Task Priority Filtering  
**AI Review Perspectives:** Security, Performance, and Maintainability

## Inline Comments

### 1. Input Validation
**Location:** `tasks.py`, line 10  
**Persona:** Security

Validate the priority value and reject unsupported values with a clear error message.

### 2. Case Sensitivity
**Location:** `tasks.py`, line 12  
**Persona:** Maintainability

Normalize priority values using `.lower()` to handle inputs such as `"HIGH"` and `"High"` consistently.

### 3. Missing Priority Values
**Location:** `tasks.py`, line 15  
**Persona:** Security

Use `.get()` or validate task data to prevent errors when a task has no priority field.

### 4. Function Documentation
**Location:** `tasks.py`, line 5  
**Persona:** Maintainability

Add a short docstring explaining the function's purpose, parameters, and return value.

## Global Feedback

### 5. Test Coverage
**Persona:** Maintainability

Add tests for all priority levels, invalid inputs, and empty task lists.

### 6. Performance
**Persona:** Performance

The filtering approach has O(n) time complexity, which is appropriate for a simple task list.

### 7. Error Handling
**Persona:** Security

Handle invalid inputs gracefully and provide clear error messages instead of unexpected exceptions.

### 8. Code Organization
**Persona:** Maintainability

Keep filtering logic separate from API or user interface code to improve reusability and testability.

## Review Summary

The feature has a straightforward implementation. The main improvement areas are input validation, error handling, test coverage, and code readability. All suggestions should be verified against the actual implementation before being accepted.