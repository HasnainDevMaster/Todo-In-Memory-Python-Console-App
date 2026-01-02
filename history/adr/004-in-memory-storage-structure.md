# ADR-004: In-Memory Storage Structure

## Status
Accepted

## Date
2026-01-01

## Context
The application needs to store tasks in memory during the session. We need to decide on a data structure that balances simplicity, performance, and functionality for a basic todo application.

## Decision
Store tasks in a list of Task objects with a separate counter for next_id. The main tasks container will be a list preserving insertion order, and a separate integer counter will track the next available ID to ensure sequential IDs even after deletions.

## Alternatives Considered
- Dictionary with ID as key (would lose insertion order, require more complex ID management)
- List with manual ID management (would complicate ID assignment after deletions)
- Separate ID pool system (unnecessary complexity for this use case)
- Multiple parallel lists (inefficient and hard to maintain consistency)

## Consequences
### Positive
- List preserves insertion order (natural chronological view)
- Separate counter ensures reliable sequential IDs even after deletions
- Natural ordering for default listing
- Simple iteration for display
- Straightforward implementation with built-in Python data structures
- Predictable behavior for users

### Negative
- O(n) lookup by ID (acceptable for small in-memory scale but inefficient for large datasets)
- More complex ID management compared to dictionary-based approach
- Requires iteration to find specific tasks by ID
- Memory usage grows linearly with task count

## References
- plan.md: Technical Context section
- data-model.md: In-Memory Storage Structure
- spec.md: In-memory storage requirements