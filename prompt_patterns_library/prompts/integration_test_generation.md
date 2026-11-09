# Integration Test Generation Prompt Template

**Role**: Act as a senior test engineer experienced in integration testing for `[LANGUAGE]` applications and `[TEST_FRAMEWORK]`.

**Task**: Design integration tests that verify whether the supplied components, modules, or services work correctly together across their real interfaces.

Consider:
- Data passed between components.
- Interaction with databases, APIs, queues, or other dependencies.
- Correct handling of successful interactions.
- Failure responses, timeouts, and dependency errors.
- Setup, isolation, and cleanup of test resources.

**Input Placeholder**:
- `[COMPONENTS_TO_INTEGRATE]`: Components or services under test.
- `[SOURCE_CODE_OR_INTERFACES]`: Relevant implementations, contracts, or API definitions.
- `[DEPENDENCIES_AND_TEST_ENVIRONMENT]`: Database, external services, test containers, or mocks.
- `[EXPECTED_INTERACTIONS]`: Expected data flow and behavior.
- `[TEST_FRAMEWORK]`: Testing framework and relevant version.
- `[PROJECT_TEST_CONVENTIONS]`: Existing setup, fixtures, and naming conventions.

**Expected Output Format**:
1. **Integration Scope**: Identify the components and boundaries being tested.
2. **Test Scenarios**: List successful, edge, and failure interactions.
3. **Test Code**: Provide integration tests in the requested framework.
4. **Test Setup and Cleanup**: Explain required fixtures, test data, and resource cleanup.
5. **Coverage Summary**: Map the tests to the component interactions, data flows, expected behaviors, and failure scenarios they verify.
6. **Assumptions and Gaps**: Identify missing environment or interface details.

**Constraints**: Focus on interactions between components rather than isolated unit behavior. Make clear which dependencies are real and which are mocked. Do not claim tests pass without execution.
