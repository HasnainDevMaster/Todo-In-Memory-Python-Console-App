# ADR-001: Interaction Model

## Status
Accepted

## Date
2026-01-01

## Context
The application needs to provide an intuitive user interface for managing todo tasks. We need to decide how users will interact with the application - whether through an interactive loop, single commands, or a menu-driven interface. This decision affects the entire user experience and application architecture.

## Decision
Adopt interactive prompt loop with text commands (add, list, update <id>, delete <id>, complete <id>, exit). Users will run the application once and then enter commands at a prompt until they explicitly exit.

## Alternatives Considered
- Single-command execution via arguments (e.g., `python todo.py add "task"`, `python todo.py list`)
- Menu-driven numbered selection (show numbered menu, user selects option number)
- GUI-based interface

## Consequences
### Positive
- Enables multiple operations in one session without restarting the application
- Provides immediate feedback to users after each command
- Aligns with typical console todo app user experience
- Keeps implementation simple while remaining extensible
- Application maintains state in a continuous loop
- Users stay in the app until explicit exit
- Easier testing via manual interaction

### Negative
- Requires maintaining application state in memory throughout the session
- More complex error handling since the application doesn't reset between operations
- Users must remember available commands (vs menu-driven approach)

## References
- plan.md: Technical Context section
- research.md: Command syntax research
- spec.md: User interaction requirements