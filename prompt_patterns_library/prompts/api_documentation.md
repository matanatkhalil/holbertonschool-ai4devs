# API Documentation Prompt Template

**Role**: Act as a senior API designer and technical writer experienced in documenting RESTful services and developer-facing interfaces.

**Task**: Produce clear, accurate API documentation for the supplied endpoints so that developers can understand and use them.

Document each endpoint's purpose, HTTP method, path, authentication requirements, parameters, request body, responses, and relevant errors. Include examples where the supplied information supports them.

**Input Placeholder**:
- `[API_ROUTES_OR_SPECIFICATION]`: Endpoint definitions or API specification.
- `[HTTP_METHODS_AND_PATHS]`: Methods and endpoint paths, if not included above.
- `[REQUEST_SCHEMAS]`: Parameters, headers, and request body schemas.
- `[RESPONSE_SCHEMAS]`: Response bodies and status codes.
- `[AUTHENTICATION_AND_AUTHORIZATION]`: Security requirements.
- `[EXAMPLE_REQUESTS_AND_RESPONSES]`: Available examples.
- `[DOCUMENTATION_FORMAT]`: Markdown, OpenAPI, or another required format.

**Expected Output Format**:
For each endpoint, provide:
1. **Endpoint**: HTTP method and path.
2. **Description**: Purpose and behavior.
3. **Authentication**: Required credentials or permissions.
4. **Parameters**: Name, type, location, required status, and description.
5. **Request Body**: Schema and example, if applicable.
6. **Responses**: Document status codes, descriptions, and example response bodies.
7. **Errors and Edge Cases**: Describe relevant failure responses and their examples.
8. **Usage Example**: Provide example HTTP requests, including headers and request bodies where applicable.

**Constraints**: Do not invent endpoint behavior, schemas, status codes, or authentication rules. Clearly identify missing information and keep the output consistent with `[DOCUMENTATION_FORMAT]`.
