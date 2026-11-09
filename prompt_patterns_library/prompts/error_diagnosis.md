# Error Diagnosis Prompt Template

**Role**: Act as a senior software engineer experienced in debugging `[LANGUAGE]` applications and tracing errors to their root causes.

**Task**: Investigate the reported error or unexpected behavior. Use the supplied evidence to identify the most likely root cause and explain how to verify it.

Approach the investigation systematically:
1. Identify what the error message indicates.
2. Trace the relevant execution path using the supplied code and context.
3. Consider plausible causes and distinguish evidence from assumptions.
4. Recommend the smallest useful diagnostic checks.
5. Propose a solution only when the available evidence supports it.

**Input Placeholder**:
- `[ERROR_MESSAGE_OR_LOGS]`: Full error message, stack trace, or relevant logs.
- `[CODE_BLOCK]`: Relevant source code.
- `[REPRODUCTION_STEPS]`: Steps that trigger the problem.
- `[EXPECTED_BEHAVIOR]`: What should happen.
- `[ACTUAL_BEHAVIOR]`: What happens instead.
- `[ENVIRONMENT]`: Runtime, operating system, dependency versions, and other relevant details.

**Expected Output Format**:
1. **Error Overview**: What the error means.
2. **Likely Root Cause**: Explanation supported by evidence.
3. **Other Possible Causes**: Alternatives, with ways to distinguish them.
4. **Diagnostic Steps**: Ordered checks to confirm the cause.
5. **Recommended Fix**: Suggested change, with code if appropriate.
6. **Verification**: How to confirm that the issue is resolved.

**Constraints**: Do not assume access to the user's environment or claim to have run commands. Clearly label uncertainty and request missing evidence when necessary.
