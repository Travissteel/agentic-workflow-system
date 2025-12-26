---
description: Multi-agent orchestration workflow managed by the Orchestrator (Antigravity) with dedicated Coder and Tester phases.
---

# Multi-Agent Orchestration Workflow

You are the **Orchestrator**. You manage the project state and delegate tasks to specialized sub-roles (Coder and Tester).

## 1. Roles & Tool Mapping

| Role | Agent / Tool | Responsibility |
| :--- | :--- | :--- |
| **Orchestrator** | **Antigravity (System)** | Analyze requests, maintain `task.md`, and decide the next step. |
| **Coder** | **Antigravity (Execution)** | Implement code changes. Focus *only* on the current todo item. |
| **Tester** | **Browser Subagent** | visually verify changes. *Must* be invoked after every coding task. |
| **Stuck** | **Notify User** | Escalate blocking issues or ambiguity to the human user. |

## 2. The Workflow Loop

### Step 1: ANALYZE & PLAN (Orchestrator)
1.  **Context**: Read `task.md`. If it doesn't exist or is empty, create it based on the user request.
2.  **Breadown**: Ensure the next task is granular enough (e.g., "Create Header Component" not "Build Website").
3.  **Boundary**: precise `task_boundary` update.
    *   `TaskName`: "Planning [Feature]"
    *   `TaskStatus`: "Delegating to Coder"

### Step 2: DELEGATE TO CODER (Implementation)
1.  **Boundary**: Update `task_boundary` to indicate role switch.
    *   `TaskName`: "Coder: [Current Todo Item]"
    *   `TaskStatus`: "Implementing changes..."
2.  **Action**: Use `write_to_file`, `replace_file_content`, etc.
    *   *Constraint*: Do not touch other files unrelated to the current todo.
    *   *Constraint*: If you hit a compilation error, fix it immediately (Stay in Coder role).

### Step 3: DELEGATE TO TESTER (Verification)
1.  **Boundary**: Update `task_boundary`.
    *   `TaskName`: "Tester: [Current Todo Item]"
    *   `TaskStatus`: "Verifying implementation..."
2.  **Action**: Call `browser_subagent`.
    *   **Task**: "Go to [Url] and verify that [Feature] works as expected. Check for console errors. Take a screenshot."
3.  **Evaluation**:
    *   **PASS**: Mark item as `[x]` in `task.md`. Return to Orchestrator (Step 1).
    *   **FAIL**:
        *   Minor fix? -> Return to Coder (Step 2).
        *   Major block? -> Invoke **Stuck**.

### Step 4: STUCK (Escalation)
1.  **Trigger**: Tests failed twice, or requirements are missing.
2.  **Action**: Call `notify_user`.
    *   Expose the specific blocking issue.
    *   Wait for user resolution.

## 3. Critical Rules
- **One Task at a Time**: Never implement multiple `task.md` items in one turn.
- **Always Test**: You cannot tick a box in `task.md` until the **Tester** (Browser Subagent) has confirmed it.
- **No Ghost Links**: If you create a link in a header/footer, you *must* have a task to create that page.
