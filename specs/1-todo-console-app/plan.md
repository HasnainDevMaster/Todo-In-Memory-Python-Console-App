# Implementation Plan: Todo In-Memory Python Console App

**Branch**: `1-todo-console-app` | **Date**: 2026-01-02 | **Spec**: [link]
**Input**: Feature specification from `/specs/1-todo-console-app/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implement a simple command-line todo application with file-based persistence that allows users to add, view, update, delete, and mark tasks as complete. The application will feature a menu-driven interface that displays numbered options and loops until the user chooses to exit. Tasks (including titles and descriptions) will be saved to and loaded from a JSON file, with both title and description fully displayed when viewing the task list.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: Built-in Python libraries only (json, os, pathlib – no external dependencies)
**Storage**: In-memory list of Task objects during runtime, with automatic load/save to tasks.json in the project root
**Testing**: Manual validation based on updated success criteria
**Target Platform**: Cross-platform console application
**Project Type**: Single console application
**Performance Goals**: <1 second response time for all operations, <1 second load/save for reasonable task counts
**Constraints**: <100MB memory usage, single-user, file-based persistence using standard library
**Scale/Scope**: Single user, up to 1000 tasks

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- ✅ Spec-Driven Development: Implementation follows updated specification
- ✅ No Manual Coding: Code generated exclusively through Claude Code
- ✅ Simplicity and Modularity: Enhancements maintain simplicity using only stdlib for JSON persistence
- ✅ Clean Code Practices: Following Pythonic idioms and proper structure
- ✅ Technology Stack Requirements: Using Python 3.13+, standard library only (json module for persistence)
- ✅ Feature Implementation Standards: Covers all 5 basic features with full title/description display and cross-session persistence
- ✅ Project Structure Requirements: Code in /src directory, persistence file (tasks.json) in root

## Project Structure

### Documentation (this feature)

```text
specs/1-todo-console-app/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
tasks.json                   # Auto-generated persistence file (JSON array of tasks)
src/
├── main.py                  # Main application entry point with menu-driven loop
├── models/
│   └── task.py              # Task model/class definition (with to_dict/from_dict for serialization)
├── services/
│   └── todo_service.py      # Business logic + persistence operations (load/save)
└── ui/
    └── menu.py              # Menu display, input handling, and user prompts

tests/
└── manual/
    └── validation.md        # Updated manual test cases including persistence
```

**Structure Decision**: Adjusted separation of concerns – added ui/menu.py for clean menu handling, enhanced todo_service.py with load/save functions, and added serialization support in the Task model. Persistence file placed in root for simplicity and discoverability.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Menu-driven interface instead of command prompt | Significantly improves usability and discoverability for console users; reduces errors from mistyped commands | Keeping command-based would leave the UI feeling "bland" as reported by user feedback |
| File-based persistence (tasks.json) | Allows tasks to survive across sessions, making the app practically useful | Pure in-memory limits utility to single session only, reducing real-world value |
| Full description display in list view | Current implementation shows placeholder ("-") instead of actual description | Breaks user expectation that added description will be visible when viewing tasks |
