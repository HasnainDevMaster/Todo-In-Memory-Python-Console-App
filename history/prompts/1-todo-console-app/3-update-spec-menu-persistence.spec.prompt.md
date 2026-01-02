---
id: 3
title: Update spec for menu and persistence
stage: spec
date: 2026-01-02
surface: agent
model: claude-sonnet-4-5-20250929
feature: 1-todo-console-app
branch: 1-todo-console-app
user: Claude
command: /sp.phr
labels: ["spec", "todo-app", "menu", "persistence", "requirements"]
links:
  spec: specs/1-todo-console-app/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/1-todo-console-app/spec.md
tests:
  - none
---

## Prompt

Update the following current specification for the Todo Python Console App to incorporate these new requirements:

Change the user interaction model from a command-based prompt (e.g., typing 'add "title"', 'list', etc.) to a menu-driven interface. The app should display a numbered menu with options such as: 1. Add Task, 2. View Tasks, 3. Update Task, 4. Delete Task, 5. Mark Task as Complete, 6. Exit. The app should loop, redisplaying the menu after each operation until the user selects Exit.
Add persistence using a simple file to save and load tasks (e.g., a JSON file named 'tasks.json' in the project root). On app startup, load existing tasks from the file if it exists. After any change (add, update, delete, mark complete), automatically save the updated task list to the file. This allows tasks to persist across sessions.
Ensure that when viewing the task list, both the title and description are fully displayed for each task (e.g., fix any issues where description shows as '-' or is missing).

Make the following adjustments to align with these changes:

Update the project title if needed to reflect persistence (no longer strictly in-memory).
Revise clarifications to specify the new menu-driven interaction model instead of the previous command-loop decision.
Update user stories, acceptance scenarios, and edge cases to reflect the menu interface and persistence (e.g., scenarios for loading/saving, handling file errors).
Revise functional requirements to include file-based persistence (e.g., add FR for loading/saving tasks), and ensure FR-002 explicitly requires displaying title and description.
Update key entities if needed (e.g., note file storage).
Revise success criteria to include persistence (e.g., tasks persist after exit and reload on restart) and full display of task details.
Remove or adjust any conflicting elements, such as strict in-memory constraints or command-based examples.
Maintain clean code principles; use Python's standard library for file I/O (e.g., json module), no external dependencies.

Here is the current specification to update:
text# Feature Specification: Todo In-Memory Python Console App

**Feature Branch**: `1-todo-console-app`
**Created**: 2026-01-01
**Status**: Draft
**Input**: User description: "Todo In-Memory Python Console App
Target audience: Hackathon participants acting as Product Architects, using AI for spec-driven development
Focus: Build a simple command-line todo application with in-memory storage, simulating real-world software evolution starting from a basic script
Success criteria:

Implements all 5 basic features: Add Task (with title and description), Delete Task (by ID), Update Task (details), View Task List (with status indicators), Mark as Complete (toggle completion)
All code generated via Claude Code without manual coding, following spec-driven workflow
GitHub repository includes Constitution file, specs history folder with all specification files, /src folder with Python source code, README.md with setup instructions, and CLAUDE.md with Claude Code instructions
Working console application demonstrates adding tasks, listing tasks with status, updating details, deleting by ID, and marking complete/incomplete
Adheres to clean code principles and proper Python project structure"

## Clarifications

### Session 2026-01-01

- Q: How should users interact with the application - through an interactive loop that keeps running, or single command executions that exit after each operation? → A: Interactive prompt loop
- Q: Should the task IDs be sequential numbers starting from 1, or should they be based on other methods like timestamps or UUIDs? → A: Sequential integers starting from 1
- Q: What specific characters or symbols should be used to indicate task completion status in the display? → A: Brackets with space/x ([ ] for incomplete, [x] for complete)
- Q: How should the application handle the case when a user requests to view tasks but there are no tasks in the list? → A: Display "No tasks found" or similar message
- Q: What specific error message should be displayed when a user tries to update, delete, or mark complete a task that doesn't exist? → A: "Task with ID [X] not found"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Add and View Tasks (Priority: P1)

A user wants to add tasks to their todo list with a title and description, then view all tasks with their completion status. This is the core functionality that enables the basic todo experience.

**Why this priority**: This is the fundamental feature that establishes the core value proposition of the todo application - allowing users to capture and view their tasks.

**Independent Test**: Can be fully tested by adding multiple tasks with titles and descriptions, then viewing the list to verify all tasks appear with proper status indicators, delivering a complete basic todo workflow.

**Acceptance Scenarios**:
1. **Given** user has opened the console app, **When** user adds a task with title "Buy groceries" and description "Milk, bread, eggs", **Then** task appears in the task list with title, description, and "Incomplete" status
2. **Given** user has added multiple tasks, **When** user views the task list, **Then** all tasks appear with their titles, descriptions, and completion status indicators

---

### User Story 2 - Update and Complete Tasks (Priority: P2)

A user wants to update task details after creation and mark tasks as complete when finished. This adds the ability to manage the lifecycle of tasks.

**Why this priority**: This provides essential task management capabilities that make the todo app useful for ongoing task tracking.

**Independent Test**: Can be fully tested by adding a task, updating its details, marking it complete, then viewing to verify changes are reflected, delivering complete task lifecycle management.

**Acceptance Scenarios**:
1. **Given** user has an existing task, **When** user updates the task description, **Then** the task shows the updated description when viewed
2. **Given** user has an incomplete task, **When** user marks the task as complete, **Then** the task shows "Complete" status with appropriate visual indicator

---

### User Story 3 - Delete Tasks (Priority: P3)

A user wants to remove tasks they no longer need from their todo list. This provides cleanup capabilities for the task management system.

**Why this priority**: This completes the basic CRUD operations for task management, allowing users to maintain a clean and relevant task list.

**Independent Test**: Can be fully tested by adding tasks, deleting specific ones by ID, then viewing the list to verify only remaining tasks appear, delivering complete task lifecycle control.

**Acceptance Scenarios**:
1. **Given** user has multiple tasks in the list, **When** user deletes a task by its ID, **Then** that task no longer appears in the task list

---

## Edge Cases

- What happens when user tries to delete a task that doesn't exist?
- How does system handle invalid task IDs during update or deletion?
- What happens when user tries to mark complete a task that doesn't exist?
- How does the system handle empty title or description during task creation?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow users to add tasks with a required title and optional description
- **FR-002**: System MUST display all tasks with their title, description, and completion status
- **FR-003**: Users MUST be able to update task details (title and/or description) by task ID
- **FR-004**: System MUST allow users to mark tasks as complete/incomplete by task ID
- **FR-005**: System MUST allow users to delete tasks by their unique ID
- **FR-006**: System MUST assign unique sequential IDs to each task for referencing
- **FR-007**: System MUST maintain task data in memory during the application session
- **FR-008**: System MUST display clear status indicators for task completion (e.g., [ ] for incomplete, [x] for complete)
- **FR-009**: System MUST provide clear error messages when invalid operations are attempted

### Key Entities

- **Task**: Represents a single todo item with attributes: ID

## Response snapshot

Successfully updated the specification file to incorporate menu-driven interface and file persistence requirements. Updated the project title, clarifications, user stories, acceptance scenarios, edge cases, functional requirements, key entities, and success criteria to reflect the new requirements. The specification now accurately reflects the new requirements for a menu-driven interface with numbered options (1. Add Task, 2. View Tasks, 3. Update Task, 4. Delete Task, 5. Mark Task as Complete, 6. Exit) and file persistence using 'tasks.json' that loads on startup and saves after each change.

## Outcome

- ✅ Impact: Specification updated to include menu-driven interface and file persistence requirements
- 🧪 Tests: none
- 📁 Files: specs/1-todo-console-app/spec.md
- 🔁 Next prompts: none
- 🧠 Reflection: Specification now properly reflects new requirements for menu interface and persistence

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Validate with implementation