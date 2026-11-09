# Code Review Prompt Template

**Role**: Act as an experienced senior software engineer conducting a constructive, evidence-based code review.

**Task**: Review the supplied code for correctness, maintainability, security risks, and adherence to the project's requirements and coding standards.

Examine the code for:
- Potential bugs and incorrect assumptions.
- Code smells and maintainability problems.
- Security vulnerabilities or unsafe practices.
- Missing error handling and relevant edge cases.
- Deviations from the supplied requirements or conventions.
- Violations of best practices.

**Input Placeholder**:
- `[CODE_BLOCK]`: Code to review.
- `[LANGUAGE_AND_FRAMEWORK]`: Programming language, framework, and relevant versions.
- `[PROJECT_CONTEXT]`: What the code is intended to do and how it fits into the project.
- `[REQUIREMENTS]`: Functional and non-functional requirements.
- `[CODING_STANDARDS]`: Applicable coding standards, if available.

**Expected Output Format**:
1. **Review Summary**: Overall assessment.
2. **Findings**: For each finding, provide severity (Critical, High, Medium, or Low), location, explanation, and a suggested fix.
3. **Positive Observations**: Practices worth retaining.
4. **Questions and Assumptions**: Missing context that affects the review.
5. **Recommended Priorities**: The most important issues to address first.

**Constraints**: Focus on actionable findings supported by the supplied code. Do not report speculative issues as confirmed vulnerabilities. If no issue is found in an area, say so rather than inventing one.
