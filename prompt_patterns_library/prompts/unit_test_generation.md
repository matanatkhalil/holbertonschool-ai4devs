# Unit Test Generation Prompt Template

**Role**: Act as an experienced `[LANGUAGE]` test engineer familiar with `[TEST_FRAMEWORK]` and unit-testing best practices.

**Task**: Create focused unit tests for the supplied function, class, or component. Verify its behavior in isolation, including normal inputs, boundary conditions, and expected failures.

Consider:
- Typical valid inputs and expected results.
- Boundary values and edge cases.
- Invalid inputs and error handling.
- Dependencies that should be mocked or stubbed to isolate the unit.

**Input Placeholder**:
- `[CODE_BLOCK]`: Function, class, or component to test.
- `[EXPECTED_BEHAVIOR]`: Requirements or expected behavior.
- `[TEST_FRAMEWORK]`: Testing framework and relevant version.
- `[DEPENDENCIES]`: External dependencies and which should be mocked.
- `[EXISTING_TEST_CONVENTIONS]`: Project test structure and naming conventions.

**Expected Output Format**:
1. **Test Approach**: Briefly describe the behaviors to cover.
2. **Test Code**: Provide executable test cases in the requested framework.
3. **Coverage Summary**: Map test cases to normal, edge, and failure scenarios.
4. **Assumptions**: List any behavior or setup details that need confirmation.

**Constraints**: Test one unit at a time where practical. Avoid testing implementation details unnecessarily. Do not invent APIs or claim tests pass without execution.
