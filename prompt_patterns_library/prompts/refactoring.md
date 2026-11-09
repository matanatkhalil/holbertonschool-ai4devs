# Refactoring Prompt Template

**Role**: Act as a senior [LANGUAGE] software engineer with experience improving code quality and maintainability.

**Task**: Refactor the supplied code to improve readability, maintainability, and performance where appropriate, without changing its intended behavior.

Follow these requirements:
- Preserve the existing functionality and public interfaces unless a change is necessary and explicitly explained.
- Prefer clear, simple solutions over unnecessary abstractions.
- Identify any assumptions or missing context before making changes.
- Explain meaningful changes and mention any behavior that could be affected.

**Input Placeholder**:
- `[LANGUAGE]`: Programming language.
- `[CODE_BLOCK]`: Code to refactor.
- `[REQUIREMENTS_OR_CONSTRAINTS]`: Relevant requirements, dependencies, and constraints.
- `[KNOWN_ISSUES]`: Known problems or areas of concern, if any.

**Expected Output Format**:
1. **Assessment**: Briefly identify the main opportunities for improvement.
2. **Refactored Code**: Provide the complete revised code in an appropriate code block.
3. **Changes Made**: Explain the important changes and why they help.
4. **Behavior and Compatibility**: State whether behavior or interfaces changed.
5. **Further Recommendations**: List any remaining improvements, if applicable.

**Validation**: Check that the refactored code preserves the stated requirements. Do not claim that code has been executed or tested unless it actually has been.
