# ADR-005: Command Parsing Approach

## Status
Accepted

## Date
2026-01-01

## Context
The application needs to interpret user commands entered at the interactive prompt. We need to decide how to parse these commands while maintaining simplicity and adhering to the "no manual coding" constraint that requires Claude Code to generate all logic.

## Decision
Simple space-split parsing with basic command recognition and quoted string support where needed. Commands will be parsed by splitting on spaces with special handling for quoted strings that contain spaces.

## Alternatives Considered
- Full argument parser library (argparse) (would add dependency and complexity)
- Third-party CLI frameworks (would violate no-external-dependencies constraint)
- Regular expression-based parsing (potentially overkill for simple commands)
- State machine parser (unnecessary complexity for this scope)

## Consequences
### Positive
- Keeps dependencies minimal (none beyond standard library)
- Aligns with "no manual coding" constraint by allowing Claude Code to generate lightweight logic
- Simple to implement and understand
- Sufficient for Phase I scope
- Easy to extend in future phases if needed
- Clear separation between command and arguments

### Negative
- Limited to basic command formats
- May struggle with complex nested arguments
- Manual parsing requires careful handling of edge cases
- Less robust than established parsing libraries
- Potential issues with special characters in task titles/descriptions

## References
- plan.md: Technical Context section
- research.md: Command syntax research
- contracts/commands.md: Command interface specification