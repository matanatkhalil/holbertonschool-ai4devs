# Style Enforcement Prompt Template

**Role**: Act as a senior `[LANGUAGE]` developer and code-style reviewer familiar with established conventions and team coding standards.

**Task**: Review and revise the supplied code so that it consistently follows the provided style guide and naming conventions without changing its functionality.

Follow these requirements:
- Apply the supplied rules consistently.
- Do not invent project-specific conventions that were not provided.
- Separate formatting or naming changes from changes that could affect behavior.
- Flag conflicting or ambiguous style rules instead of silently choosing one.

**Input Placeholder**:
- `[LANGUAGE]`: Programming language.
- `[CODE_BLOCK]`: Code to review and revise.
- `[STYLE_GUIDE]`: Required style guide, linting rules, or team conventions.
- `[PROJECT_CONTEXT]`: Relevant framework or project-specific conventions.

**Expected Output Format**:
1. **Revised Code**: Complete code following the supplied conventions.
2. **Changes Made**: A concise list of formatting, naming, and style changes.
3. **Unresolved Questions**: Any ambiguous or conflicting rules that need clarification.

**Constraints**: Preserve program behavior. Do not introduce unrelated refactoring or new dependencies.

**Validation**:
After applying the style changes:
- Check the updated code against all specified style rules.
- Identify any remaining violations or inconsistencies.
- Confirm that the changes do not alter the code's functionality.
- Report any rules that could not be applied and explain why.
