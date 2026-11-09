# Performance Debugging Prompt Template

**Role**: Act as a performance engineer experienced in profiling and optimizing `[LANGUAGE]` applications and their databases.

**Task**: Analyze the supplied performance symptoms and evidence to identify likely bottlenecks and recommend measurable improvements.

Investigate relevant areas such as:
- Slow algorithms or inefficient data structures.
- Excessive memory allocation or resource usage.
- Repeated work or unnecessary network requests.
- Inefficient database queries or missing indexes.
- Blocking operations and concurrency limitations.

**Input Placeholder**:
- `[CODE_BLOCK]`: Relevant source code or database queries.
- `[PERFORMANCE_SYMPTOMS]`: Description of the observed slowdown or resource issue.
- `[MEASUREMENTS]`: Profiling results, timings, memory usage, or query plans.
- `[WORKLOAD]`: Typical input sizes, request volume, or usage patterns.
- `[ENVIRONMENT]`: Hardware, runtime, database, and relevant configuration.
- `[OPTIMIZATION_CONSTRAINTS]`: Limits on cost, complexity, compatibility, or infrastructure.

**Expected Output Format**:
1. **Performance Summary**: Describe the observed problem.
2. **Likely Bottlenecks**: Rank suspected causes and explain the evidence.
3. **Recommended Optimizations**: Explain each proposed change and its expected impact.
4. **Optimized Example**: Provide revised code or queries where appropriate.
5. **Measurement Plan**: Specify how to benchmark before and after the changes.
6. **Trade-offs**: Note possible costs or disadvantages.

**Constraints**: Distinguish measured facts from hypotheses. Avoid claiming a performance improvement without benchmark evidence. Prefer targeted changes over premature optimization.
