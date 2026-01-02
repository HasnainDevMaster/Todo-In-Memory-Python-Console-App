# ADR-003: Status Indicator Format

## Status
Accepted

## Date
2026-01-01

## Context
The application needs to visually distinguish between completed and incomplete tasks in the console output. We need to choose a format that is easily recognizable and readable in plain text console environments.

## Decision
Use "[ ]" for incomplete and "[x]" for complete in task listings. This format will appear as "[ ] 1: Task Title - Description" for incomplete tasks and "[x] 1: Task Title - Description" for completed tasks.

## Alternatives Considered
- Checkmark symbols (✓/✗) (might not display properly in all console environments)
- Text labels (INCOMPLETE/COMPLETE) (too verbose for compact listings)
- Other symbols (>, -, +) (less intuitive than brackets)
- Colors only (not accessible to all users, might not work in all terminals)

## Consequences
### Positive
- Widely recognized from Markdown and GitHub task lists
- Excellent readability in plain console text
- Minimal characters while remaining visually distinct
- Consistent visual feedback across listings
- Easy to parse visually by users
- Works in all terminal environments

### Negative
- Limited visual differentiation (only two characters)
- Might be confused with other bracket-based syntax in some contexts
- Less visually appealing than color-based indicators

## References
- plan.md: Technical Context section
- research.md: Decision about display format
- spec.md: Status indicator requirements