# Cross-Language Specification – Log Analyzer

## 1. Algorithm Description

Develop a Log Analyzer that processes server logs and generates basic statistics.

The algorithm should:
- Count total valid requests.
- Group requests by HTTP method and status code.
- Calculate the error rate (4xx and 5xx responses).
- Identify the most frequently requested endpoint.
- Calculate the average response time.
- Count malformed log entries.

## 2. Input Format

An array of log entries in the following format:

```text
TIMESTAMP METHOD ENDPOINT STATUS_CODE RESPONSE_TIME
```

Example:

```text
2026-11-13T10:30:00Z GET /api/users 200 120
2026-11-13T10:31:00Z POST /api/users 201 150
2026-11-13T10:32:00Z GET /api/products 404 80
```

## 3. Output Format

A JSON object containing:

```json
{
  "totalRequests": 3,
  "requestsByMethod": {
    "GET": 2,
    "POST": 1
  },
  "requestsByStatus": {
    "200": 1,
    "201": 1,
    "404": 1
  },
  "errorRate": 33.33,
  "mostRequestedEndpoint": "/api/users",
  "averageResponseTime": 116.67,
  "malformedEntries": 0
}
```

## 4. Edge Cases

- Empty input.
- Malformed log entries.
- Invalid HTTP status codes (outside 100–599).
- Negative or non-numeric response times.
- Multiple endpoints with equal request counts (choose alphabetically).
- All requests returning error status codes.
- Mixture of valid and invalid entries.

## 5. Test Cases

| Test | Input | Expected Result |
|---|---|---|
| 1. Normal logs | 3 valid entries: 200, 201, 404 | 3 requests, 33.33% error rate |
| 2. Empty input | Empty array | 0 requests, 0% error rate |
| 3. Malformed entries | 1 valid, 2 invalid entries | 1 request, 2 malformed |
| 4. All errors | 3 valid entries: 404, 500, 503 | 3 requests, 100% error rate |
| 5. Invalid values | 1 valid, 2 invalid entries | 1 request, 2 malformed |

## 6. Cross-Language Requirements

Implement the same algorithm in:
- JavaScript
- Python
- TypeScript

All implementations must:
- Follow the same input and output formats.
- Apply identical validation rules.
- Handle the defined edge cases.
- Produce equivalent results for all test cases.

## 7. Evaluation Criteria

- Correctness of calculations.
- Input validation.
- Edge case handling.
- Consistency across languages.
- Code readability and test results.
