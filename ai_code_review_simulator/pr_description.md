# Pull Request: Add Task Priority Filtering

## Summary

This pull request introduces task priority filtering, allowing users to view tasks based on their priority level. Users can filter tasks by High, Medium, or Low priority, making task management more organized and efficient.

## Changes

- Added a `filter_tasks_by_priority()` function to filter tasks by priority.
- Added support for High, Medium, and Low priority levels.
- Added input validation to handle invalid priority values.
- Added unit tests covering valid filters, empty task lists, and invalid priority values.

## Context

As the number of tasks increases, finding important tasks becomes more difficult. This feature helps users focus on tasks based on their urgency and importance.

The implementation is intended to be approximately 100–200 lines of code, including tests and supporting logic.

**Related Issue:** Add task filtering functionality.

## Testing

- Verify that filtering by High, Medium, and Low returns the correct tasks.
- Verify that an empty task list returns an empty result.
- Verify that invalid priority values are handled appropriately.
- Run the existing test suite to ensure no regressions.

## Expected Outcome

Users can filter their tasks by priority, and the existing application functionality remains unaffected.