# Appendix F: Skills Quick-Reference Card

## Introduction: Your Automation Power-Ups

Skills are pre-packaged capabilities that extend what AI agents can do in your automation workflows. Think of them as specialized power-ups that you invoke when you need specific expertise or workflows that go beyond basic code generation.

### What Are Skills?

Skills are reusable, expert-level capabilities built into Antigravity IDE and similar AI platforms. Unlike Model Context Protocol (MCP) servers that provide external data access, skills are behavioral patterns—they tell the AI agent HOW to approach a specific task using proven methodologies.

**Key Differences:**
- **MCPs** = External data/tool access (databases, APIs, filesystems)
- **Skills** = Expert workflows and methodologies (debugging patterns, testing strategies)
- **Custom Code** = One-off solutions for unique problems

### How to Invoke Skills

Skills can be invoked in two ways:

**1. Using the Skill Tool** (recommended for automation):
```typescript
// In your directive or orchestrator
invoke_skill({
  name: "systematic-debugging",
  context: "User reports 500 error on checkout endpoint",
  parameters: {
    focus_area: "payment_processing"
  }
});
```

**2. Using Slash Commands** (for interactive sessions):
```
/systematic-debugging "Investigate checkout 500 errors"
```

### When to Use Skills vs. Custom Code

**Use Skills When:**
- The task fits a proven pattern (debugging, testing, planning)
- You need expert-level methodology applied consistently
- You want reusable workflows across projects
- You're orchestrating complex multi-step processes

**Write Custom Code When:**
- The task is business-specific and unique
- No existing skill matches your needs
- You need fine-grained control over every step
- The task is simple and one-off

### Skills in the DOE Framework

In the Directive Orchestration Execution (DOE) framework, skills bridge the gap between directives (natural language instructions) and executions (deterministic code):

- **Directives** tell the agent WHAT to achieve
- **Skills** provide expert HOW methodologies
- **Executions** are the actual code produced

Skills are especially powerful when invoked BY your orchestrator as part of delegating to subagents. For example, your orchestrator might invoke the `systematic-debugging` skill when delegating a bug investigation to the coder agent.

┌─────────────────────────────────────────────────────┐
│  DOWNLOADABLE SKILLS CHEAT SHEET                    │
│                                                      │
│  Get a one-page PDF reference card with all         │
│  skills, usage patterns, and decision trees:        │
│                                                      │
│  travissteel.net/the-last-employee/resources#reference          │
│                                                      │
│  Perfect for printing and keeping by your desk!     │
└─────────────────────────────────────────────────────┘

---

## Essential Skills Reference

### Development & Code Quality

#### systematic-debugging
**What it does:** Applies a methodical 5-step debugging process: reproduce, isolate, analyze, hypothesize, verify.

**When to use:**
- Production bugs that are difficult to reproduce
- Complex issues spanning multiple systems
- When previous debugging attempts failed
- Before resorting to "random fixes"

**Key benefits:** Finds root causes faster, prevents regression, documents findings for future reference.

**Invocation:**
```
/systematic-debugging "Users report intermittent checkout failures"
```

---

#### test-driven-development
**What it does:** Implements the TDD cycle: write failing test, write minimal code to pass, refactor.

**When to use:**
- Building new features from scratch
- When requirements are well-defined
- Refactoring existing code safely
- When code quality and maintainability are priorities

**Key benefits:** Higher test coverage, better design, living documentation, fewer bugs in production.

**Invocation:**
```
/test-driven-development "Build user authentication system"
```

---

#### verification-before-completion
**What it does:** Runs comprehensive pre-commit checks: tests pass, linting clean, builds succeed, no obvious issues.

**When to use:**
- Before EVERY commit (make this a habit)
- Before marking tasks complete
- Before handoff to testing/staging
- As final step in automated workflows

**Key benefits:** Catches issues before they enter version control, reduces CI/CD failures, maintains code quality.

**Invocation:**
```
/verification-before-completion
```

---

#### receiving-code-review
**What it does:** Guides you through responding to code review feedback constructively and efficiently.

**When to use:**
- After receiving PR review comments
- When feedback feels overwhelming
- When prioritizing which changes to make first

**Key benefits:** Faster PR approval cycles, better collaboration with team, improved code quality.

**Invocation:**
```
/receiving-code-review "PR #234 has 15 comments"
```

---

#### requesting-code-review
**What it does:** Helps prepare comprehensive PR descriptions and context for reviewers.

**When to use:**
- Before submitting any pull request
- When changes are complex and need explanation
- When multiple reviewers are involved

**Key benefits:** Faster review cycles, fewer clarification requests, better team communication.

**Invocation:**
```
/requesting-code-review "Refactored payment processing pipeline"
```

---

### Planning & Execution

#### brainstorming
**What it does:** Facilitates structured ideation sessions using divergent then convergent thinking patterns.

**When to use:**
- Before starting major features or refactors
- When stuck on a design decision
- During architecture planning
- When exploring multiple solution approaches

**Key benefits:** Better solutions through exploration, avoids premature optimization, documents decision rationale.

**Invocation:**
```
/brainstorming "How should we structure our microservices architecture?"
```

---

#### writing-plans
**What it does:** Creates detailed, actionable implementation plans with dependencies, milestones, and success criteria.

**When to use:**
- Before complex features or multi-week projects
- When coordinating work across multiple developers
- When breaking down vague requirements
- As input to subagent-driven-development

**Key benefits:** Clear roadmap, parallelizable tasks, prevents scope creep, enables progress tracking.

**Invocation:**
```
/writing-plans "Migrate from MongoDB to PostgreSQL"
```

---

#### executing-plans
**What it does:** Systematically executes implementation plans with checkpoint validation and rollback capability.

**When to use:**
- After creating a plan with writing-plans
- For multi-step migrations or refactors
- When order of operations matters
- When rollback capability is critical

**Key benefits:** Consistent execution, early failure detection, safe rollback points, progress visibility.

**Invocation:**
```
/executing-plans plan_file="migration-plan.md"
```

---

#### subagent-driven-development
**What it does:** Parallelizes development by spawning multiple subagents for independent tasks.

**When to use:**
- When tasks can be done independently
- For batch operations (creating 10 API endpoints)
- When time is critical
- For embarrassingly parallel work

**Key benefits:** Massive speedups (5-10x on parallel tasks), efficient context usage, scales with complexity.

**Invocation:**
```
/subagent-driven-development tasks="[task1.md, task2.md, task3.md]"
```

---

### Testing & Quality

#### condition-based-waiting
**What it does:** Implements smart waiting strategies that check for actual conditions instead of arbitrary sleep() calls.

**When to use:**
- Writing E2E or integration tests
- Automating UI interactions
- Waiting for async operations
- Replacing flaky sleep-based waits

**Key benefits:** Eliminates 90% of test flakiness, tests run faster, more reliable CI/CD.

**Invocation:**
```
/condition-based-waiting "Wait for payment confirmation before asserting"
```

---

#### testing-anti-patterns
**What it does:** Reviews test code and identifies common anti-patterns: brittle selectors, hidden dependencies, unclear assertions.

**When to use:**
- When tests are flaky
- During test suite refactoring
- Before adding new test patterns
- When test maintenance is painful

**Key benefits:** More maintainable tests, faster feedback loops, reduced false failures.

**Invocation:**
```
/testing-anti-patterns file="checkout.test.ts"
```

---

#### testing-skills-with-subagents
**What it does:** Validates that custom skills work correctly across different contexts and subagent invocations.

**When to use:**
- After writing a new custom skill
- Before sharing skills with team
- When debugging skill invocation issues
- During skill refactoring

**Key benefits:** Ensures skills are reusable, catches edge cases, validates documentation.

**Invocation:**
```
/testing-skills-with-subagents skill="custom-deployment-validator"
```

---

### Git & Workflow

#### using-git-worktrees
**What it does:** Sets up isolated Git worktrees for parallel feature development without branch switching.

**When to use:**
- Working on multiple features simultaneously
- Reviewing PRs while keeping work in progress
- Running long test suites while continuing development
- Comparing feature branches side-by-side

**Key benefits:** No context switching, parallel work streams, no stashing required, faster reviews.

**Invocation:**
```
/using-git-worktrees feature_branch="feature/new-auth"
```

---

#### finishing-a-development-branch
**What it does:** Guides you through proper branch completion: rebase vs merge decision, conflict resolution, cleanup.

**When to use:**
- Before merging feature branches
- When deciding merge strategy
- Cleaning up after PR approval
- Managing feature flags during merge

**Key benefits:** Clean Git history, proper conflict resolution, no orphaned branches.

**Invocation:**
```
/finishing-a-development-branch branch="feature/payment-v2"
```

---

#### sharing-skills
**What it does:** Packages custom skills for sharing with team or contributing to upstream repositories.

**When to use:**
- After creating valuable custom skills
- Contributing to open source
- Standardizing workflows across team
- Building internal skill libraries

**Key benefits:** Reusable across projects, team consistency, community contribution.

**Invocation:**
```
/sharing-skills skill="custom-api-testing-workflow"
```

---

### Debugging & Analysis

#### root-cause-tracing
**What it does:** Traces errors back to their origin through logs, stack traces, and code history.

**When to use:**
- When error messages are vague or misleading
- Debugging cascading failures
- Finding when a bug was introduced
- Understanding complex error chains

**Key benefits:** Fixes the real problem, not symptoms, prevents recurrence, faster resolution.

**Invocation:**
```
/root-cause-tracing error="Database connection pool exhausted"
```

---

#### dispatching-parallel-agents
**What it does:** Spawns multiple investigation agents to explore different hypotheses simultaneously.

**When to use:**
- Complex bugs with multiple possible causes
- Performance investigation across systems
- When single-threaded debugging is too slow
- Exploring multiple solution approaches

**Key benefits:** Faster investigation, explores dead-ends in parallel, comprehensive analysis.

**Invocation:**
```
/dispatching-parallel-agents hypotheses="[db_locks, memory_leak, network_timeout]"
```

---

#### defense-in-depth
**What it does:** Implements multiple validation layers: input validation, business logic checks, output sanitization.

**When to use:**
- Building security-critical features
- Handling untrusted input
- Financial transaction processing
- Preventing data corruption

**Key benefits:** Robust error handling, security hardening, fail-safe behavior.

**Invocation:**
```
/defense-in-depth component="payment-processing"
```

---

### Platform-Specific Skills

#### n8n-workflow-creation
**What it does:** Guides creation of n8n workflows with best practices: error handling, webhooks, scheduling.

**When to use:**
- Building automations in n8n
- Integrating n8n with Modal endpoints
- Setting up webhook receivers
- Creating scheduled workflows

**Key benefits:** Production-ready workflows, proper error handling, maintainable automation.

**Invocation:**
```
/n8n-workflow-creation integration="CRM to Modal AI endpoint"
```

---

#### n8n-error-handling
**What it does:** Implements robust error handling in n8n: retry logic, fallbacks, alerting.

**When to use:**
- When n8n workflows fail silently
- Building mission-critical automations
- Handling unreliable third-party APIs
- Before client handoff

**Key benefits:** Reliable workflows, better debugging, production readiness.

**Invocation:**
```
/n8n-error-handling workflow="lead-processing"
```

---

#### remotion-best-practices
**What it does:** Applies Remotion video generation best practices: performance optimization, composition structure, rendering.

**When to use:**
- Building video generation workflows
- Optimizing render times
- Creating reusable video templates
- Debugging Remotion rendering issues

**Key benefits:** Faster renders, maintainable compositions, production-quality output.

**Invocation:**
```
/remotion-best-practices project="social-media-videos"
```

---

#### image-generation
**What it does:** Orchestrates AI image generation with proper prompting, resolution selection, and post-processing.

**When to use:**
- Creating marketing visuals
- Generating product mockups
- Building image-heavy automations
- A/B testing visual content

**Key benefits:** Consistent quality, optimized prompts, proper error handling.

**Invocation:**
```
/image-generation prompt="Modern SaaS dashboard hero image"
```

---

#### video-generation
**What it does:** Coordinates video generation workflows: script to speech, scene composition, rendering pipeline.

**When to use:**
- Automating video content creation
- Building social media video pipelines
- Generating personalized video messages
- Batch video production

**Key benefits:** End-to-end automation, consistent branding, scalable production.

**Invocation:**
```
/video-generation script="explainer-video-script.md"
```

---

## Quick Decision Guide

### Which Skill Should I Use?

Use this decision tree to quickly identify the right skill for your situation:

**Starting a new feature?**
→ brainstorming → writing-plans → test-driven-development

**Debugging an issue?**
→ Is it complex? YES: systematic-debugging → root-cause-tracing
→ Is it complex? NO: Just fix it directly

**Before committing code?**
→ ALWAYS: verification-before-completion

**Working on multiple features?**
→ using-git-worktrees

**Need to parallelize work?**
→ Many similar tasks? subagent-driven-development
→ Investigating bug? dispatching-parallel-agents

**Tests are flaky?**
→ testing-anti-patterns → condition-based-waiting

**Preparing a PR?**
→ requesting-code-review

**Merging a feature branch?**
→ finishing-a-development-branch

**Building automation workflows?**
→ For n8n? n8n-workflow-creation + n8n-error-handling
→ For video? remotion-best-practices OR video-generation
→ For images? image-generation

**Creating reusable workflows?**
→ Build custom skill → testing-skills-with-subagents → sharing-skills

### Skills That Should ALWAYS Be Used

These skills should become automatic habits:

| Skill | When | Why |
|-------|------|-----|
| **verification-before-completion** | Before every commit | Catches issues before they enter version control |
| **requesting-code-review** | Before every PR | Speeds up review cycles dramatically |
| **condition-based-waiting** | In ALL tests with async operations | Eliminates 90% of test flakiness |
| **defense-in-depth** | For ANY security-critical code | Multiple validation layers prevent exploits |
| **n8n-error-handling** | In ALL n8n workflows | Production workflows must handle failures gracefully |

### Common Scenarios Mapped to Skills

| Scenario | Primary Skill | Supporting Skills |
|----------|---------------|-------------------|
| Building new feature | test-driven-development | brainstorming, writing-plans |
| Production bug | systematic-debugging | root-cause-tracing |
| Code review | requesting-code-review | verification-before-completion |
| Refactoring | writing-plans | test-driven-development |
| Flaky tests | condition-based-waiting | testing-anti-patterns |
| Complex investigation | dispatching-parallel-agents | systematic-debugging |
| Client handoff | n8n-workflow-creation | n8n-error-handling |
| Video automation | remotion-best-practices | video-generation |
| Parallel development | subagent-driven-development | writing-plans |

---

## Skill Invocation Examples

### Using the Skill Tool in Directives

When writing directives or orchestrator logic, invoke skills programmatically:

```typescript
// In your orchestrator directive
async function investigateBug(bugReport: string) {
  // First, apply systematic debugging
  const debugResult = await invoke_skill({
    name: "systematic-debugging",
    context: bugReport,
    parameters: {
      reproduction_steps: "From user report #1234",
      expected_behavior: "Checkout completes successfully",
      actual_behavior: "500 error on payment submission"
    }
  });

  // If multiple hypotheses emerge, dispatch parallel agents
  if (debugResult.hypotheses.length > 3) {
    await invoke_skill({
      name: "dispatching-parallel-agents",
      context: debugResult.summary,
      parameters: {
        hypotheses: debugResult.hypotheses,
        time_limit: "30 minutes"
      }
    });
  }

  // Always verify before committing fix
  await invoke_skill({
    name: "verification-before-completion"
  });
}
```

### Chaining Skills for Complex Workflows

Skills can be chained together for sophisticated automation:

```typescript
// Build feature with full workflow
async function buildFeatureWithQuality(featureName: string) {
  // 1. Brainstorm approach
  const ideas = await invoke_skill({
    name: "brainstorming",
    context: `New feature: ${featureName}`
  });

  // 2. Create implementation plan
  const plan = await invoke_skill({
    name: "writing-plans",
    context: ideas.selected_approach
  });

  // 3. Execute using TDD
  await invoke_skill({
    name: "test-driven-development",
    parameters: {
      plan: plan.tasks,
      coverage_target: 80
    }
  });

  // 4. Pre-commit verification
  await invoke_skill({
    name: "verification-before-completion"
  });

  // 5. Prepare for review
  await invoke_skill({
    name: "requesting-code-review",
    context: `Feature: ${featureName}\nPlan: ${plan.summary}`
  });
}
```

### Interactive Slash Command Usage

During interactive development sessions:

```bash
# Start with brainstorming
/brainstorming "How should we cache API responses?"

# Once approach is clear, create a plan
/writing-plans "Implement Redis caching layer"

# Use TDD to build it
/test-driven-development "Build cache abstraction with TTL support"

# Before committing
/verification-before-completion

# When ready for PR
/requesting-code-review "Added Redis caching for API responses"
```

### Passing Complex Parameters

Some skills accept structured parameters:

```typescript
// Testing custom skills with specific scenarios
await invoke_skill({
  name: "testing-skills-with-subagents",
  parameters: {
    skill_name: "custom-deployment-validator",
    test_scenarios: [
      {
        name: "Happy path deployment",
        context: "All services healthy",
        expected: "Deployment approved"
      },
      {
        name: "Database migration pending",
        context: "Migration not yet run",
        expected: "Deployment blocked with clear error"
      }
    ],
    subagent_count: 3
  }
});
```

---

## Custom Skills: When and How

### When to Create Custom Skills

Build custom skills when:

**You find yourself repeating the same workflow**
- If you've manually done the same multi-step process 3+ times, make it a skill

**Your team needs consistency**
- Standardizing code review checklists, deployment procedures, etc.

**The workflow is complex but reusable**
- Not every business, but many businesses (e.g., "compliance-audit-preparation")

**You want to contribute to the community**
- Skills can be shared across companies and industries

### Don't Create Custom Skills When:

**The workflow is business-specific**
- "Process returns for Acme Corp's policy" → This is a directive, not a skill

**It's a one-off task**
- No reuse value = custom code is fine

**Existing skills can be combined**
- Chain existing skills rather than reinventing

### How to Create Custom Skills

Use the `writing-skills` skill to guide creation:

```bash
/writing-skills "Create skill for validating API documentation completeness"
```

The skill will walk you through:
1. Defining the skill's purpose and scope
2. Identifying required inputs and parameters
3. Designing the step-by-step workflow
4. Adding validation and error handling
5. Writing documentation and examples

### Testing and Sharing

Always test custom skills before deploying:

```bash
# Test your new skill
/testing-skills-with-subagents skill="api-docs-validator"

# If it works well, share it
/sharing-skills skill="api-docs-validator"
```

For detailed guidance on writing skills, see Chapter 16 (Essential Skills for Business Automation) in the main book.

---

## Skills vs. MCPs vs. Custom Code: A Comparison

| Feature | Skills | MCPs | Custom Code |
|---------|--------|------|-------------|
| **Purpose** | Expert workflows | External data/tools | Unique business logic |
| **Reusability** | High (across projects) | High (across agents) | Low (project-specific) |
| **When to use** | Proven patterns | Need external access | One-off tasks |
| **Examples** | TDD, debugging, planning | Database, filesystem, APIs | Your pricing calculator |
| **Complexity** | Medium | Low (plug-and-play) | Varies |
| **Learning curve** | Learn once, reuse often | Minimal | Every time |

**Best Practice:** Combine all three!
- Use **skills** for proven workflows (debugging, testing)
- Use **MCPs** for data access (database, Google Sheets)
- Write **custom code** for business-specific logic (pricing rules)

---

## Troubleshooting Skill Invocation

**Skill not found?**
- Check spelling: skill names are case-sensitive
- Verify skill is available in your environment
- Some skills require specific MCPs to be installed

**Skill fails with unclear error?**
- Check parameters: some skills require specific inputs
- Review skill documentation: `/help skill-name`
- Try with minimal parameters first, then add complexity

**Skill seems to hang?**
- Some skills (like dispatching-parallel-agents) take time
- Check for circular dependencies in skill chains
- Set timeout parameters if available

**Skill output doesn't match expectation?**
- Review context you provided: skills need good input
- Check if skill is appropriate for your use case
- Consider using a different skill or custom code

For comprehensive troubleshooting guidance, see Appendix H (Troubleshooting Guide).

---

## Quick Tips for Skill Mastery

1. **Start with the "always use" skills**: verification-before-completion, requesting-code-review, condition-based-waiting

2. **Chain skills for complex workflows**: brainstorming → writing-plans → executing-plans

3. **Use skills in directives**: Make skills part of your standard operating procedures

4. **Test skills before relying on them**: Understand what they do before putting them in automation

5. **Combine with MCPs**: Skills + data access = powerful automation

6. **Don't over-skill**: If custom code is simpler, use custom code

7. **Document which skills you use**: Makes workflows reproducible and trainable

8. **Contribute back**: If you create valuable skills, share them with the community

---

┌─────────────────────────────────────────────────────┐
│  DOWNLOADABLE SKILLS CHEAT SHEET                    │
│                                                      │
│  Get a one-page PDF reference card with all         │
│  skills, usage patterns, and decision trees:        │
│                                                      │
│  travissteel.net/the-last-employee/resources#reference          │
│                                                      │
│  Perfect for printing and keeping by your desk!     │
└─────────────────────────────────────────────────────┘

---

**Next Steps:**
- Review Chapter 16 for in-depth skill usage examples
- Download the PDF cheat sheet for quick reference
- Start using verification-before-completion on your next commit
- Experiment with brainstorming and writing-plans on your next feature

**Remember:** Skills are power-ups, not replacements for thinking. Use them to augment your workflow, not to avoid understanding what you're building.
