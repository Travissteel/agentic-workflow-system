# Shadow Orchestrator Directive

**Created**: February 2026
**Owner**: DOE Framework
**Frequency**: Production (continuous monitoring)

---

## Objective

**What needs to happen:**
Monitor production workflows in real-time, automatically diagnose and fix non-critical errors using a three-tier classification system, and continuously update directives with production learnings through self-annealing.

**Why this matters:**
Production workflows encounter unpredictable issues (website redesigns, API changes, data format variations) that traditional automation can't handle. The Shadow Orchestrator prevents 2 AM support calls by auto-fixing routine issues while escalating critical problems to human oversight, ensuring 99%+ uptime without manual intervention.

---

## Inputs

**Required Data:**
- [ ] Production error reports from primary workflow endpoint
- [ ] Historical error patterns and fixes from directive logs
- [ ] Current directive file for the monitored workflow
- [ ] Workflow execution logs and API responses

**Required Access:**
- [ ] Read/Write access to directive repository (GitHub)
- [ ] Modal endpoint logs and monitoring
- [ ] Claude Opus API access for complex error diagnosis
- [ ] Stuck agent invocation capability for escalations

**Trigger Conditions:**
- **When**: Primary workflow reports an error or unexpected output
- **If**: Error is detected during execution (not a successful completion)

---

## Process

**Step-by-step workflow (in plain English):**

1. **Detect Error from Primary Workflow**
   - Success looks like: Error report received with error type, message, context, and severity
   - If error: If error report is malformed, log and escalate to stuck agent

2. **Classify Error Using 3-Tier Model**
   - **Tier 1 Check**: Is this a known error pattern documented in directive?
     * Success looks like: Pattern matched to documented fix in directive's "Edge Cases Learned" section
     * If match found: Apply documented fix → Log event → Continue (auto-fix complete)
   - **Tier 3 Check**: Does this involve money, security, or data deletion?
     * Success looks like: Pattern analysis determines risk level
     * If high-risk detected: STOP immediately → Preserve state → Escalate to stuck agent
   - **Tier 2 Path**: Unknown error that requires diagnosis
     * Success looks like: Error queued for intelligent analysis
     * If error: Proceed to Step 3

3. **Diagnose Root Cause (Tier 2 Errors)**
   - Use Claude Opus to analyze error with full context
   - Success looks like: Root cause identified with confidence level (high/medium/low)
   - If error: If diagnosis fails or is inconclusive, escalate to stuck agent

4. **Determine Fix Strategy**
   - **Decision Tree**:
     * Is root cause 100% clear? (NO → Escalate)
     * Can fix be tested safely? (NO → Escalate)
     * Is fix isolated with no side effects? (NO → Escalate)
     * Has similar fix worked before? (YES → Higher confidence)
   - Success looks like: Fix strategy with confidence rating (high/medium/low)
   - If error: If confidence is not HIGH, escalate to stuck agent

5. **Test the Fix in Sandbox**
   - Create temporary version with proposed fix
   - Run on sample data that triggered the error
   - Success looks like: Fix resolves error and produces expected output
   - If error: If test fails, escalate to stuck agent with test results

6. **Apply Fix to Production**
   - Update production workflow code
   - Restart from point of failure
   - Success looks like: Workflow resumes and completes successfully
   - If error: Rollback fix and escalate to stuck agent

7. **Update Directive with Learning**
   - Add entry to "Edge Cases Learned" section with:
     * Date and error message
     * Root cause analysis
     * Fix applied (before/after code)
     * Prevention strategy
   - Commit to GitHub repository
   - Success looks like: Directive updated and committed successfully
   - If error: Log warning but don't block (fix is already applied)

8. **Log and Notify**
   - Create detailed log entry with timestamp, error, fix, and confidence
   - Send summary notification (not urgent alert)
   - Success looks like: Log entry created and notification sent
   - If error: Continue (logging failure is not critical)

**Edge Cases & Exceptions:**

- **If error classification is ambiguous**: Err on the side of caution and escalate to Tier 3
- **If multiple errors occur simultaneously**: Queue them and process one at a time, prioritizing by severity
- **If same error recurs after auto-fix**: Escalate to stuck agent (fix didn't work as expected)
- **If directive update fails**: Continue operation but flag for manual review (directive is out of sync)

---

## Definition of Done

**This workflow is complete when:**
- [ ] Error is classified correctly (Tier 1, 2, or 3)
- [ ] Tier 1 errors are auto-fixed using documented solutions
- [ ] Tier 2 errors are diagnosed, tested, and fixed OR escalated if unsafe
- [ ] Tier 3 errors are immediately escalated to stuck agent
- [ ] All auto-fixes are logged with before/after code
- [ ] Directive is updated with new learnings
- [ ] Primary workflow resumes and completes successfully

**Quality Standards:**
- Auto-fix success rate >95% for Tier 1 errors
- Escalation rate <5% for false Tier 3 classifications
- Zero production data loss or corruption from auto-fixes
- All directive updates include clear prevention strategies
- Mean time to diagnosis <1 minute
- Mean time to fix <5 minutes

**Notification:**
- **Who to notify**: System administrator or workflow owner
- **How**: Email or Slack with summary (not urgent unless Tier 3)
- **What to include**: Error type, fix applied, directive update link, before/after comparison

---

## Notes & Learnings

**Known Issues:**
- First-time errors (never seen before) always require Tier 2 analysis, which adds 30-60 seconds
- GitHub commit failures can occur during directive updates (retry logic needed)

**Optimization Ideas:**
- Maintain local cache of common error patterns to speed up Tier 1 matching
- Batch multiple directive updates if several errors are fixed in one session
- Add metrics dashboard to track auto-fix success rate over time

**Self-Annealing Updates:**
- [Date]: [What was changed and why - this directive itself evolves through use]

---

## The 3-Tier Error Classification Model

### Tier 1: Known Friction (Auto-Fix Without Notification)

**Auto-fix when:**
- Rate limiting (429 errors) → Add retry with exponential backoff
- Temporary timeouts (503 errors) → Wait and retry
- Missing optional fields → Use default values
- File format mismatches → Auto-convert when possible
- Authentication token refresh → Use refresh token to get new access token

**Requirements:**
- Pattern is documented in directive
- Fix has worked successfully before
- No risk of data corruption
- No security implications

### Tier 2: Unknown Obstacles (Safe Annealing with Notification)

**Diagnose and fix when:**
- Website CSS selector changes → Analyze new structure, update selectors
- API response format changes → Map new fields to expected structure
- New data format variations → Recognize patterns and adapt extraction logic
- Unexpected but non-critical errors → Analyze root cause and propose fix

**Requirements:**
- Can analyze problem with AI diagnosis
- Can test fix safely before applying
- Fix doesn't affect financial data, security, or irreversible actions
- Business outcome remains the same (how changes, but what doesn't)

### Tier 3: Critical Logic Failures (Mandatory Human Escalation)

**Escalate immediately when:**
- Financial data discrepancies or unexpected amounts
- Data deletion or overwriting about to occur
- Security credentials appear unexpectedly
- Authentication or authorization failures
- Business logic needs to change (not just implementation)
- Root cause is unclear or confidence is low
- Any ambiguity about correct behavior

**Action:**
- STOP execution immediately
- Preserve complete state and context
- Invoke stuck agent with error details, diagnosis, and suggested actions
- Wait for human decision before resuming

---

## Decision Engine Flowchart

```
Error Detected
    ↓
Question 1: Is this a known error pattern?
    (Match in directive's Edge Cases Learned section?)
    ├── YES → Apply documented fix → Log → Continue (Tier 1)
    └── NO → Question 2
              ↓
Question 2: Money/Security/Data Deletion?
    (Financial, auth, or irreversible actions?)
    ├── YES → STOP → Preserve state → Escalate (Tier 3)
    └── NO → Question 3
              ↓
Question 3: Can I safely test a fix?
    (Clear root cause + sandbox testing possible?)
    ├── YES → Diagnose → Test → Apply → Update Directive (Tier 2)
    └── NO → STOP → Preserve state → Escalate (Tier 3)
```

**Core Principle:** When in doubt, escalate. Better to wake a human unnecessarily than silently make a wrong decision.

---

## Production Metrics to Track

**Auto-Fix Performance:**
- Total errors detected
- Tier 1 auto-fixes (should be 60-80% of total)
- Tier 2 safe annealing (should be 15-30% of total)
- Tier 3 escalations (should be <5% of total)
- False positive escalations (escalated but could have been auto-fixed)

**Speed Metrics:**
- Mean time to detection (should be <10 seconds)
- Mean time to diagnosis (should be <1 minute)
- Mean time to fix (should be <5 minutes for Tier 1, <90 seconds for Tier 2)

**Quality Metrics:**
- Auto-fix success rate (target >95%)
- Recurrence rate (same error after fix, target <1%)
- Directive update accuracy (fixes documented correctly)

---

## When to Use Shadow Orchestrator

**Use Shadow Orchestrator when:**
- ✅ High-volume production workflows (hundreds/thousands of executions daily)
- ✅ Mission-critical applications (client business depends on uptime)
- ✅ Long-running deployments (will be in production for months/years)
- ✅ Workflows with evolving requirements (APIs and websites change)

**Don't use Shadow Orchestrator when:**
- ❌ First Modal deployment (learn Standard Hybrid Wrapper first)
- ❌ Low-volume workflows (<50 executions/day)
- ❌ Static requirements (workflow logic won't change)
- ❌ Budget-conscious projects (Opus calls add cost)

---

## Implementation Notes

**For deployer agent:**
This directive requires TWO Modal endpoints:
1. **Primary Endpoint**: Your workflow with error classification
2. **Agentic Support Endpoint**: Error diagnosis and auto-fixing engine

Plus GitHub integration for automatic directive updates.

See `deployer-agent.md` and `support-agent.md` for implementation details.

---

**Related Resources:**
- Chapter 12: The Shadow Orchestrator Pattern (full context)
- `support-agent.md`: Production error diagnosis specialist
- `deployer-agent.md`: Modal deployment with Shadow setup
- `hybrid-wrapper-deployment.md`: Standard deployment (without Shadow)
