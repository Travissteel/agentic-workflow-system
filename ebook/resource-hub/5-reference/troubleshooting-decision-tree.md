# Troubleshooting Decision Tree

Use this flowchart to quickly identify which agent to invoke when problems occur.

---

## Problem Classification

```
PROBLEM DETECTED
    |
    What type of problem?
    |
    ├─ CODE NOT WORKING ──> Is it a build/compile error?
    │                        ├─ YES ──> Invoke CODER agent
    │                        └─ NO ──> Is it a visual/rendering issue?
    │                                   ├─ YES ──> Invoke TESTER agent
    │                                   └─ NO ──> Continue below
    │
    ├─ DEPLOYMENT FAILING ──> Is it Modal-related?
    │                        ├─ YES ──> Invoke DEPLOYER agent
    │                        └─ NO ──> Invoke STUCK agent
    │
    ├─ PRODUCTION ERROR ──> Is it a Shadow Orchestrator deployment?
    │                        ├─ YES ──> Invoke SUPPORT agent
    │                        └─ NO ──> Invoke STUCK agent
    │
    └─ UNCLEAR / STUCK ──> ALWAYS invoke STUCK agent
```

---

## Agent Selection Guide

### Invoke CODER when:
- ✅ Code won't compile or run
- ✅ Function returns unexpected results
- ✅ Need to implement a new feature
- ✅ Logic needs refactoring
- ✅ Dependencies are missing
- ✅ Errors during local testing

**What CODER will do**: Fix code, implement features, resolve build errors

---

### Invoke TESTER when:
- ✅ Code runs but visual output is wrong
- ✅ UI elements are misaligned or missing
- ✅ Need to verify end-to-end workflow
- ✅ Screenshots show incorrect rendering
- ✅ Interactive elements don't work (clicks, forms)
- ✅ Responsive design is broken

**What TESTER will do**: Use Playwright MCP to visually verify correctness, take screenshots, test interactions

---

### Invoke DEPLOYER when:
- ✅ Need to deploy workflow to Modal
- ✅ Modal deployment is failing
- ✅ Authentication setup is needed
- ✅ Creating n8n wrapper workflow
- ✅ Generating handover package for client
- ✅ Bearer token issues

**What DEPLOYER will do**: Build Modal endpoint, configure authentication, create n8n workflow, deliver handover package

---

### Invoke SUPPORT when:
- ✅ Production error in Shadow Orchestrator deployment
- ✅ Need to diagnose unknown production issue
- ✅ Determining if error can be auto-fixed
- ✅ Updating directives with production learnings
- ⚠️ **ONLY for Shadow Orchestrator deployments**

**What SUPPORT will do**: Diagnose root cause, classify error tier (1/2/3), auto-fix safe errors, escalate critical errors

---

### Invoke STUCK when:
- ✅ ANY other agent hits an error
- ✅ You're uncertain which agent to use
- ✅ Multiple approaches are possible
- ✅ Need human decision on implementation
- ✅ Tests fail and fix is unclear
- ✅ Business logic question arises
- ⚠️ **STUCK is the ONLY agent with AskUserQuestion**

**What STUCK will do**: Ask human for guidance, present clear options, relay decision back to system

---

## Common Scenarios

### Scenario 1: "Build fails with import error"
**Answer**: Invoke **CODER** (code/dependency issue)

### Scenario 2: "Page renders but header is misaligned"
**Answer**: Invoke **TESTER** (visual verification needed)

### Scenario 3: "Modal deploy returns 401 error"
**Answer**: Invoke **DEPLOYER** (authentication setup issue)

### Scenario 4: "Production workflow failed with unknown API error"
**Answer**:
- If Shadow Orchestrator: Invoke **SUPPORT**
- If Standard deployment: Invoke **STUCK**

### Scenario 5: "Not sure if we should use REST or GraphQL"
**Answer**: Invoke **STUCK** (needs human decision)

### Scenario 6: "Tests pass locally but fail in production"
**Answer**: Invoke **STUCK** (unclear root cause, needs diagnosis)

---

## The Golden Rule

**When in doubt, invoke STUCK agent.**

Better to ask for human guidance than proceed blindly with assumptions.

---

## Agent Invocation Protocol

### For Orchestrator:
1. Identify problem type
2. Use decision tree to select agent
3. Invoke with clear, specific task
4. Wait for completion
5. If agent hits error → They will invoke STUCK automatically

### For Subagents:
1. If you encounter ANY problem
2. **IMMEDIATELY** invoke STUCK agent
3. DO NOT use fallbacks or workarounds
4. DO NOT make assumptions
5. DO NOT skip errors

---

## Error Escalation Flowchart

```
AGENT ENCOUNTERS ERROR
    |
    Is this agent the STUCK agent?
    ├─ YES ──> Use AskUserQuestion to get human input
    └─ NO ──> Invoke STUCK agent with error details
              |
              STUCK asks human for guidance
              |
              Human provides decision
              |
              STUCK relays decision back to original agent
              |
              Original agent proceeds with human-approved action
```

---

## Self-Annealing Trigger Points

After STUCK agent resolves an issue, update the directive:

1. **CODER fixes code error** → Update execution comments and directive edge cases
2. **TESTER finds visual issue** → Update Definition of Done to catch similar issues
3. **DEPLOYER encounters deployment issue** → Update deployment checklist
4. **SUPPORT auto-fixes production error** → Automatically updates directive (built-in)

---

**Related Resources:**
- `coder-agent.md` - Implementation specialist
- `tester-agent.md` - Visual QA specialist
- `deployer-agent.md` - Cloudification specialist
- `support-agent.md` - Production self-annealing (Shadow only)
- `stuck-agent.md` - Human-in-the-loop escalation
