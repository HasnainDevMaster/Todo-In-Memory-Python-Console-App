<!--
SYNC IMPACT REPORT:
Version change: N/A (initial version) → 1.0.0
Modified principles: N/A
Added sections: All principles and sections (initial creation)
Removed sections: None
Templates requiring updates: ⚠ pending - .specify/templates/plan-template.md, .specify/templates/spec-template.md, .specify/templates/tasks-template.md
Follow-up TODOs: None
-->
# Todo In-Memory Python Console App Constitution

## Core Principles

### Spec-Driven Development
All implementation must derive from detailed specifications using Spec-Kit Plus and Claude Code.

### No Manual Coding
Code generation exclusively through Claude Code; refine specs iteratively until correct output is achieved.

### Simplicity and Modularity
Focus on in-memory storage and basic functionality to build a clean, maintainable foundation.

### Clean Code Practices
Adhere to Pythonic idioms, readability, and proper structure for console applications.

### Technology Stack Requirements
Use UV for dependency management with Python 3.13+ for core implementation, following project structure with /src for source code, specs history folder for specification files, README.md for setup, and CLAUDE.md for instructions.

## Feature Implementation Standards
Cover all five basic features (Add Task, Delete Task, Update Task, View Task List, Mark as Complete) with title and description support. Maintain code quality with meaningful variable names and include status indicators in the application.

## Project Structure Requirements
Include /src for source code, specs history folder for specification files, README.md for setup, and CLAUDE.md for instructions. Use meaningful variable names and include status indicators in the application.

## Governance
This constitution governs all development practices for the Todo In-Memory Python Console App. All implementation must comply with the stated principles. Changes to this constitution require explicit approval and documentation of the rationale for the changes.

**Version**: 1.0.0 | **Ratified**: 2026-01-01 | **Last Amended**: 2026-01-01