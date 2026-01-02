# ADR-002: Task ID Generation

## Status
Accepted

## Date
2026-01-01

## Context
The application needs to uniquely identify tasks so users can reference them for operations like update, delete, and toggle completion. We need to decide on an ID generation strategy that is both user-friendly and technically sound for the in-memory storage approach.

## Decision
Use sequential integers starting from 1, auto-incremented on each new task. Each task will receive the next available integer ID, and IDs will not be reused after deletion.

## Alternatives Considered
- Start from 0 (confusing for user-facing references)
- Timestamp-based IDs (harder for users to remember and type)
- UUIDs (too long and complex for console application)
- String-based identifiers (unnecessary complexity)

## Consequences
### Positive
- Human-readable and intuitive for users (e.g., "update 3")
- Matches common todo app conventions
- Simple to implement in-memory
- Predictable and stable within a session
- Clear referencing in console output
- Easy for users to remember and type

### Negative
- IDs are not reused after deletion (potential for ID values to grow large over long sessions)
- Sequential nature means IDs can be predicted
- No inherent collision prevention if multiple instances run simultaneously

## References
- plan.md: Technical Context section
- research.md: Decision about ID generation approach
- data-model.md: Task entity definition
- spec.md: Task identification requirements