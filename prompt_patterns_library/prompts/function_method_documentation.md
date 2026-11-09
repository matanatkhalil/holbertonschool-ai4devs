# Function and Method Documentation Prompt Template

**Role**: Act as a technical writer and experienced `[LANGUAGE]` developer who produces accurate, developer-friendly code documentation.

**Task**: Document the supplied functions or methods so that another developer can understand their purpose, inputs, outputs, side effects, and failure conditions.

**Input Placeholder**:
- `[LANGUAGE]`: Programming language.
- `[CODE_BLOCK]`: Function or method implementation, including relevant types or interfaces.
- `[DOCUMENTATION_CONVENTION]`: Required format, such as JSDoc, Python docstrings, or another convention.
- `[PROJECT_CONTEXT]`: Relevant behavior or domain terminology.
- `[KNOWN_CONSTRAINTS]`: Any documentation rules or details that must be preserved.

**Expected Output Format**:
1. **Documented Code**: The original code with documentation added in the requested convention.
2. **Parameter Details**: Explain each parameter and its type, where applicable.
3. **Return Value**: Describe the return value and its type.
4. **Exceptions and Errors**: Document errors that the implementation can actually raise.
5. **Side Effects**: Describe relevant state changes, I/O, or external interactions.

**Constraints**: Base documentation on the implementation and supplied context. Do not invent behavior, parameter types, exceptions, or guarantees. Mark unclear details for confirmation.
