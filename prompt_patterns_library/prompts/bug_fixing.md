# Bug Fixing Prompt Template

**Role**: Act as a senior `[LANGUAGE]` developer responsible for diagnosing and fixing bugs in an existing codebase.

**Task**: Fix the reported bug while preserving intended existing functionality and minimizing unrelated changes.

Consider these scenarios:
- **Normal case**: The feature works as expected with valid input.
- **Edge case**: Boundary values, empty input, or unusual but valid input.
- **Failure case**: Invalid input, unavailable dependencies, or an operation that fails.

For the proposed fix, consider whether these scenarios are handled correctly.

**Input Placeholder**:
- `[BUG_DESCRIPTION]`: Clear description of the bug.
- `[CODE_BLOCK]`: Relevant source code.
- `[EXPECTED_BEHAVIOR]`: Correct behavior.
- `[ACTUAL_BEHAVIOR]`: Observed incorrect behavior.
- `[REPRODUCTION_STEPS]`: Steps or input needed to reproduce the bug.
- `[PROJECT_CONSTRAINTS]`: Relevant dependencies, interfaces, and compatibility requirements.

**Expected Output Format**:
1. **Root Cause**: Explain why the bug occurs.
2. **Proposed Fix**: Provide the corrected code or a focused patch.
3. **Explanation**: Describe what changed and why.
4. **Scenario Checks**: Explain how the fix handles normal, edge, and failure cases.
5. **Regression Tests**: Suggest tests that help ensure existing behavior remains intact.
6. **Potential Side Effects**: Identify any possible side effects or risks introduced by the fix, including changes to existing behavior or compatibility.

**Constraints**: Keep the change focused. Do not silently change public interfaces or unrelated behavior. Do not claim the fix is verified unless it has actually been tested.
