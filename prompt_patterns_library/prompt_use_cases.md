# Prompt Use Cases

## Code Quality

- **Refactoring**
  - **Goal**: Improve code readability, maintainability, and performance without changing its existing functionality.
  - **Input**: Source code in [LANGUAGE] and relevant requirements.
  - **Output**: Refactored code with an explanation of the improvements.

- **Style Enforcement**
  - **Goal**: Ensure consistent naming conventions, formatting, and coding standards throughout the codebase.
  - **Input**: Source code in [LANGUAGE] and a set of coding standards or style guidelines.
  - **Output**: Revised code that follows the specified conventions, along with a summary of the changes.

- **Code Review**
  - **Goal**: Identify potential bugs, code smells, security concerns, and violations of best practices.
  - **Input**: Source code, relevant project context, and applicable coding standards.
  - **Output**: A structured review listing identified issues, their severity, and suggested improvements.

## Debugging

- **Error Diagnosis**
  - **Goal**: Identify the root cause of an error or unexpected application behavior.
  - **Input**: Error message, relevant source code, and steps to reproduce the issue.
  - **Output**: Explanation of the root cause and a suggested solution.

- **Bug Fixing**
  - **Goal**: Resolve a specific bug while preserving existing functionality and avoiding unintended side effects.
  - **Input**: Bug description, affected source code, and expected versus actual behavior.
  - **Output**: Corrected code with an explanation of the fix and any potential side effects.

- **Performance Debugging**
  - **Goal**: Identify and resolve performance bottlenecks such as slow execution, excessive memory usage, or inefficient database queries.
  - **Input**: Relevant source code, performance measurements, and execution context.
  - **Output**: Identified bottlenecks, recommended optimizations, and improved code where appropriate.

## Documentation

- **Function and Method Documentation**
  - **Goal**: Generate clear documentation explaining the purpose, parameters, return values, and possible exceptions of functions or methods.
  - **Input**: Source code containing functions or methods in [LANGUAGE].
  - **Output**: Documentation comments following the specified documentation convention.

- **API Documentation**
  - **Goal**: Create clear and consistent documentation for API endpoints to help developers understand and integrate with the API.
  - **Input**: API routes, HTTP methods, request parameters, response formats, and authentication requirements.
  - **Output**: Structured API documentation covering endpoint descriptions, parameters, example requests, and responses.

## Testing

- **Unit Test Generation**
  - **Goal**: Generate unit tests to verify that individual functions or components behave as expected.
  - **Input**: Source code, expected behavior, and the testing framework in [FRAMEWORK].
  - **Output**: Unit tests covering normal cases, edge cases, and expected failure scenarios.

- **Integration Test Generation**
  - **Goal**: Generate tests that verify whether multiple components, modules, or services work together correctly.
  - **Input**: Source code of the components being integrated, their interfaces, dependencies, and the testing framework in [FRAMEWORK].
  - **Output**: Integration tests covering interactions between components, data flow, and expected behavior, including potential failure scenarios.

- **Test Case Generation**
  - **Goal**: Identify different scenarios that should be tested to verify that a feature meets its requirements.
  - **Input**: Feature description, functional requirements, and expected behavior.
  - **Output**: A structured list of test cases containing test scenarios, input data, expected results, and relevant edge cases.
