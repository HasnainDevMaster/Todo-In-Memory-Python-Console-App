---
description: "Task list template for feature implementation"
---

# Tasks: Todo Menu-Driven Python Console App with File Persistence

**Input**: Design documents from `/specs/1-todo-console-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Manual validation based on updated success criteria including persistence and full description display.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, root-level `tasks.json` for persistence
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and updated structure

- [X] T001 Update project structure per new implementation plan (add src/ui/ directory)
- [X] T002 Ensure Python 3.13+ project with only standard library dependencies
- [X] T003 [P] Create/confirm directory structure: src/, src/models/, src/services/, src/ui/

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure including persistence that MUST be complete before user stories

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Confirm Task model in src/models/task.py with id, title, description, completed
- [X] T005 [P] Enhance TodoService in src/services/todo_service.py with in-memory storage
- [X] T006 Implement load_tasks() method to read tasks from tasks.json on startup (handle missing/corrupt file gracefully)
- [X] T007 Implement save_tasks() method to write current tasks to tasks.json (pretty-printed JSON)
- [X] T008 Implement automatic save after every mutating operation (add, update, delete, complete)
- [X] T009 Add serialization support: to_dict() and from_dict() in Task model
- [X] T010 Create menu display and handling in src/ui/menu.py
- [X] T011 Update main.py entry point with menu-driven loop (display menu, get choice, dispatch, repeat until exit)
- [X] T012 Implement sequential ID generation (load max ID from file on startup, continue from there)

**Checkpoint**: Foundation ready with persistence and menu framework — user story implementation can now begin

---

## Phase 3: User Story 1 - Add and View Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to add tasks with title and description, then view all tasks with full title/description and completion status via menu

**Independent Test**: Can be fully tested by adding multiple tasks with titles and descriptions using the menu interface, then viewing the list to verify all tasks appear with proper status indicators and full details displayed, delivering a complete basic todo workflow with data persistence.

### Implementation for User Story 1

- [X] T013 [P] [US1] Implement add_task flow in menu: prompt for title (required) and description (optional), add via TodoService, auto-save
- [X] T014 [P] [US1] Implement view_tasks menu option: display all tasks with "[ ]"/"[x]" indicator, full title, and full description
- [X] T015 [US1] Update list display format: "[ ] ID: Title - Description" (show actual description, "No description" if empty)
- [X] T016 [US1] Handle empty task list with friendly message: "No tasks yet. Add one!"
- [X] T017 [US1] Validate title not empty/whitespace during add, with clear error message and return to menu

**Checkpoint**: User Story 1 fully functional and testable independently (including persistence)

---

## Phase 4: User Story 2 - Update and Complete Tasks (Priority: P2)

**Goal**: Enable updating task details and toggling completion status via menu options

**Independent Test**: Can be fully tested by adding a task, updating its details through the menu interface, marking it complete, then viewing to verify changes are reflected and saved to the file, delivering complete task lifecycle management with data persistence.

### Implementation for User Story 2

- [X] T018 [P] [US2] Implement update_task menu flow: prompt for ID, display current task, prompt for new title/description (optional), update and auto-save
- [X] T019 [P] [US2] Implement toggle_complete in TodoService (single method that flips status)
- [X] T020 [US2] Add "Mark as Complete" menu option: prompt for ID, toggle status, auto-save
- [X] T021 [US2] Ensure view reflects updated details and completion status immediately
- [X] T022 [US2] Add error handling: invalid ID → "Task not found", stay in menu

**Checkpoint**: User Stories 1 and 2 functional and persisted across sessions

---

## Phase 5: User Story 3 - Delete Tasks (Priority: P3)

**Goal**: Enable removal of tasks via dedicated menu option

**Independent Test**: Can be fully tested by adding tasks, deleting specific ones by ID through the menu interface, then viewing the list to verify only remaining tasks appear and the deletion is saved to the file, delivering complete task lifecycle control with data persistence.

### Implementation for User Story 3

- [X] T023 [P] [US3] Implement delete_task menu flow: prompt for ID, confirm deletion, remove and auto-save
- [X] T024 [US3] Add success message after deletion
- [X] T025 [US3] Add error handling for invalid ID during deletion

**Checkpoint**: All user stories functional with full CRUD + persistence

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Usability, robustness, and documentation improvements

- [X] T026 Add main menu with numbered options: 1. Add Task, 2. View Tasks, 3. Update Task, 4. Mark Task as Complete, 5. Delete Task, 6. Exit
- [X] T027 Ensure menu redisplays after every operation (except exit)
- [X] T028 Add clear welcome/header message on startup
- [X] T029 Graceful handling of file I/O errors (e.g., permission issues)
- [X] T030 Comprehensive input validation and user-friendly error messages throughout
- [X] T031 Update README.md with new menu-driven usage instructions and note about tasks.json persistence
- [X] T032 Final validation: full workflow with app restart to confirm persistence

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: Start immediately
- **Foundational (Phase 2)**: Depends on Setup — BLOCKS all user stories (persistence and menu core required)
- **User Stories (Phase 3+)**: All depend on Foundational completion
  - Can proceed sequentially (P1 → P2 → P3) or in parallel if capacity allows
- **Polish (Final Phase)**: After all desired user stories complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Models before services
- Services before UI components
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tasks for User Story 1 together:
Task: "Implement add_task flow in menu: prompt for title (required) and description (optional), add via TodoService, auto-save"
Task: "Implement view_tasks menu option: display all tasks with "[ ]"/"[x]" indicator, full title, and full description"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence