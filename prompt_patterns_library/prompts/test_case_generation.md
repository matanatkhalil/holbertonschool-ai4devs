# Test Case Generation Prompt Template

**Role**: Act as a QA engineer and test analyst experienced in translating software requirements into clear, verifiable test cases.

**Task**: Analyze the supplied feature requirements and identify test scenarios that can verify whether the feature behaves as expected.

Use a scenario-based approach and include:
- Normal cases for expected usage.
- Boundary and unusual but valid cases.
- Invalid-input and failure cases.
- Relevant permission, state, or dependency conditions.

**Input Placeholder**:
- `[FEATURE_DESCRIPTION]`: Feature or functionality to test.
- `[FUNCTIONAL_REQUIREMENTS]`: Detailed requirements and acceptance criteria.
- `[USER_ROLES_AND_PERMISSIONS]`: Relevant user types and access rules.
- `[INPUT_CONSTRAINTS]`: Valid formats, ranges, and validation rules.
- `[EXPECTED_BEHAVIOR]`: Description of how the feature should behave under the specified conditions.
- `[KNOWN_EDGE_CASES]`: Known risks or special scenarios.
- `[TESTING_SCOPE]`: Features or behaviors included and excluded from testing.

**Expected Output Format**:
Provide a table with these columns:
| ID | Case Type | Scenario | Preconditions | Test Steps | Test Data | Expected Result | Priority |
|---|---|---|---|---|---|---|---|

After the table, include:
1. **Coverage Summary**: Group scenarios into normal, edge, and failure cases.
2. **Requirement Gaps**: Highlight ambiguous or missing acceptance criteria.
3. **Additional Recommendations**: Suggest areas needing further testing, if applicable.

**Constraints**: Make each test case specific, independently understandable, and verifiable. Avoid duplicate scenarios and do not invent requirements. Mark assumptions explicitly.
