# Appendix H: Troubleshooting Guide

## Introduction: How to Use This Guide

When building agentic workflows, problems are inevitable. They're not failures—they're opportunities to strengthen your system through self-annealing. This guide helps you diagnose issues quickly and choose the right path to resolution.

**How This Guide Works:**

Think of troubleshooting like medical diagnosis: symptoms → diagnosis → treatment. Each section follows this pattern to get you from "something's broken" to "everything works" as efficiently as possible.

The most common mistake newcomers make is trying to fix everything themselves. They create workarounds, skip validation steps, or implement fallbacks that hide the real problem. This creates technical debt that compounds over time.

**The Stuck Agent Philosophy:**

The DOE framework includes a "stuck agent" specifically to handle problems. Using it isn't admitting defeat—it's following best practices. When you encounter ANY error, uncertainty, or unexpected behavior, invoke the stuck agent immediately. It escalates to human decision-making, ensuring you never proceed blindly past issues.

Think of it this way: the stuck agent is your safety net. Expert developers use it constantly. Junior developers resist it and create messy workarounds. Which do you want to be?

**This Guide Covers Five Categories:**

1. **Agent Selection**: Which agent handles which problem
2. **Phase-Specific Issues**: Common problems in each DOE phase
3. **Error Patterns**: Recognizing and fixing recurring issues
4. **Quick Reference**: Fast lookup tables for common symptoms
5. **Getting Unstuck**: The systematic process when you're completely lost

Use the table of contents to jump to relevant sections. If you're unsure where to start, begin with the Agent Selection Decision Tree below.

```
┌─────────────────────────────────────────────────────┐
│  DOWNLOAD THE TROUBLESHOOTING FLOWCHART             │
│                                                      │
│  Get a printable PDF decision tree for diagnosing   │
│  issues and choosing the right agent:               │
│                                                      │
│  travissteel.net/the-last-employee/resources#reference          │
│                                                      │
│  Includes: Agent selection flowchart, error code    │
│  lookup table, and phase-by-phase checklists.       │
└─────────────────────────────────────────────────────┘
```

---

## Agent Selection Decision Tree

Choosing the right agent for your problem is critical. Each agent has a specific role in the DOE framework. Here's your decision guide:

### When to Use the Coder Agent

**Purpose:** Implement ONE specific task from your todo list.

**Use the coder agent when:**
- You have a clear, specific implementation task
- The task has defined inputs, process, and Definition of Done
- You need code written (components, functions, API integrations)
- The task is small enough to fit in one context window (~30K tokens)
- You've already broken down the work into actionable items

**Example scenarios:**
- "Create a TodoList component with add/remove functionality"
- "Build an API endpoint that scrapes website data"
- "Implement authentication middleware with JWT tokens"

**Don't use the coder agent when:**
- You have multiple unrelated tasks (delegate one at a time)
- The task is vague or lacks clear requirements
- You're unsure what needs to be built (clarify with orchestrator first)
- You encounter ANY error during implementation (coder invokes stuck agent)

### When to Use the Tester Agent

**Purpose:** Verify implementations with visual validation using Playwright.

**Use the tester agent when:**
- Coder just completed an implementation
- You need to verify UI renders correctly
- You want screenshots as proof of functionality
- You need to test user flows (click paths, form submissions)
- You're checking that all navigation links work (no 404s)

**Example scenarios:**
- "Verify the login form appears and accepts credentials"
- "Check that all header links navigate to actual pages"
- "Screenshot the dashboard showing the new widget"
- "Test the multi-step wizard from start to finish"

**Don't use the tester agent when:**
- Nothing has been implemented yet (test after coding)
- You need unit tests (those are part of coder's implementation)
- The error is in the code logic (that's a coder/stuck agent issue)
- Tests fail repeatedly (invoke stuck agent after second failure)

### When to Use the Stuck Agent

**Purpose:** Escalate ANY problem to human decision-making.

**Use the stuck agent when:**
- ✅ ANY error occurs (package won't install, command fails, etc.)
- ✅ Something doesn't work on the first try
- ✅ Tests fail (after tester reports failure)
- ✅ You're unsure how to proceed
- ✅ You need to make assumptions about requirements
- ✅ An API key doesn't work
- ✅ A file path doesn't exist as expected
- ✅ Dependencies conflict
- ✅ You're tempted to use a workaround
- ✅ The user's instructions are ambiguous
- ✅ You need clarification on business logic
- ✅ A deployment fails
- ✅ Authentication rejects your credentials
- ✅ You encounter rate limiting
- ✅ An external service is down

**Example scenarios:**
- "npm install fails with dependency conflict"
- "Playwright can't find the submit button element"
- "Modal deployment returns 401 Unauthorized"
- "Should this button be blue or green? Design spec unclear"

**Critical rule:** The stuck agent is the ONLY agent that can use `AskUserQuestion` to get human input. Never guess, never use fallbacks, never skip validation. When in doubt, invoke stuck agent.

### When to Use the Deployer Agent

**Purpose:** Deploy battle-tested workflows to Modal for client handoff.

**Use the deployer agent when:**
- ✅ Phase 3 (Building) is complete
- ✅ Phase 4 (Testing) is complete and all tests pass
- ✅ You're ready to cloudify the workflow
- ✅ You have Modal credentials ready
- ✅ You know the input/output specifications
- ✅ You want to create a Hybrid Wrapper for n8n

**Example scenarios:**
- "Deploy the lead scraper workflow to Modal with n8n integration"
- "Cloudify the email parser with webhook trigger"
- "Create Modal endpoint for the CRM sync workflow"

**Don't use the deployer agent when:**
- ❌ Tests are still failing
- ❌ Core logic isn't working locally
- ❌ You haven't defined inputs/outputs
- ❌ Modal credentials aren't ready
- ❌ The workflow is still being developed

### When to Use the Support Agent

**Purpose:** Diagnose and auto-fix production errors (Shadow Orchestrator ONLY).

**Use the support agent when:**
- You deployed using Shadow Orchestrator strategy (Strategy 2)
- A production error occurred in a live Modal endpoint
- You need diagnosis of an unknown error pattern
- You want automated fixing for non-critical errors

**Don't use the support agent when:**
- You're using standard Hybrid Wrapper deployment (Strategy 1)
- You're still in local development (Phases 1-4)
- The error is critical (data corruption, security, business logic)
- You haven't deployed to production yet

**Note:** Most users will use the standard deployment strategy and will NEVER need the support agent. It's an advanced pattern for high-volume production workflows.

### Quick Decision Table

| Situation | Agent to Use |
|-----------|--------------|
| Need to implement a specific task | **Coder** |
| Need to verify implementation works | **Tester** |
| ANY error or uncertainty | **Stuck** |
| Ready to deploy to cloud (after all tests pass) | **Deployer** |
| Production error in Shadow Orchestrator | **Support** |
| Multiple tasks to coordinate | **Orchestrator** (you!) |

**Golden Rule:** When in doubt, use the stuck agent. It's always better to ask than to guess.

---

## Common Problems by Phase

### Phase 1: Environment Preparation

#### Problem 1: MCP Server Won't Connect

**Symptoms:**
- Error message: "Failed to connect to MCP server"
- Playwright commands timeout or fail
- MCP appears in settings but doesn't respond

**Diagnosis:**
This usually happens when the MCP server isn't running, the configuration is incorrect, or there's a port conflict.

**Solution:**
1. Check `.mcp.json` configuration file exists in project root
2. Verify the server command path is correct (absolute path required)
3. Restart Antigravity IDE extension/editor
4. Check if another process is using the same port
5. Review MCP logs in `.antigravity/mcp.log` if available

**Prevention:**
- Use absolute paths in MCP configuration
- Test MCP connection immediately after setup
- Keep MCP server dependencies updated
- Document working configuration in project README

#### Problem 2: Agent Permissions Blocked

**Symptoms:**
- Agent can't create files
- Bash commands fail with "Permission denied"
- Can't install packages or run scripts

**Diagnosis:**
The agent mode isn't set to allow autonomous operations, or the system requires elevated permissions.

**Solution:**
1. Check Antigravity IDE settings → Agent mode
2. Set to "Allow autonomous operations" or equivalent
3. If on Windows, check User Account Control settings
4. Verify file/folder permissions on the project directory
5. Try running VS Code/editor as administrator (Windows) or with sudo (Mac/Linux)

**Prevention:**
- Configure agent permissions during initial setup
- Document required permissions in project README
- Use consistent agent mode across team members

#### Problem 3: .env File Not Loading

**Symptoms:**
- API keys show as undefined
- Environment variables return null
- "Missing API key" errors despite .env file existing

**Diagnosis:**
The .env file isn't in the correct location, has syntax errors, or isn't being loaded by the application.

**Solution:**
1. Verify `.env` is in project root (not in subdirectory)
2. Check syntax: `KEY=value` with no spaces around `=`
3. Ensure no quotes around values unless required
4. Verify you're using the correct env loader (dotenv, etc.)
5. Restart the application after .env changes
6. Check `.env` isn't in `.gitignore` preventing access

**Example correct .env format:**
```
OPENAI_API_KEY=sk-1234567890abcdef
MODAL_TOKEN_ID=ak-1234567890
MODAL_TOKEN_SECRET=as-abcdefghijklmnop
```

**Prevention:**
- Use `.env.example` with placeholder values
- Document required environment variables
- Add validation that checks for required keys at startup

#### Problem 4: Git Hooks Failing

**Symptoms:**
- `git commit` fails with hook error
- Pre-commit checks fail unexpectedly
- Husky/lint-staged errors

**Diagnosis:**
Git hooks are failing due to linting errors, formatting issues, or missing dependencies.

**Solution:**
1. Read the error message carefully (shows which hook failed)
2. Run the hook command manually to see detailed output
3. Fix linting/formatting issues: `npm run lint --fix`
4. Ensure all hook dependencies are installed
5. If urgent, use `git commit --no-verify` (NOT recommended for regular use)
6. Update hooks if using outdated configuration

**Prevention:**
- Run linters before committing (`npm run lint`)
- Use editor plugins that auto-format on save
- Keep hook dependencies updated
- Test hooks in a clean repository clone

---

### Phase 2: Framework Configuration

#### Problem 5: Orchestrator Not Delegating Properly

**Symptoms:**
- Orchestrator tries to implement code itself
- No subagent invocations happening
- Tasks not being split up correctly

**Diagnosis:**
The orchestrator's instructions (GEMINI.md) aren't clear enough, or the agent is confused about its role.

**Solution:**
1. Review `.antigravity/GEMINI.md` - ensure it clearly states "you are the orchestrator"
2. Check that delegation examples are included
3. Explicitly remind: "Invoke the coder agent with this specific task"
4. Verify subagent definitions exist in `.antigravity/agents/`
5. If still failing, invoke stuck agent to clarify the issue

**Prevention:**
- Use the template GEMINI.md from this book
- Add explicit examples of delegation
- Start each project with: "Create todo list and delegate first task"

#### Problem 6: Subagent Not Receiving Task Correctly

**Symptoms:**
- Subagent says "I don't have enough information"
- Task seems incomplete or garbled
- Context not passed properly

**Diagnosis:**
The task delegation is missing key components (objective, inputs, process, Definition of Done) or is too vague.

**Solution:**
1. Ensure every delegated task includes:
   - **Objective**: What needs to be built
   - **Inputs**: What data/files are available
   - **Process**: Step-by-step instructions
   - **Definition of Done**: Success criteria
2. Be specific: "Create a React component called TodoList that displays an array of todos passed as props, with delete buttons for each item"
3. Avoid vague tasks: "Make the todo app better"

**Prevention:**
- Use the SOP template from Chapter 8 for every task
- Review delegated task before sending
- Include file paths, component names, expected behavior

#### Problem 7: Context Window Exceeded

**Symptoms:**
- Agent stops mid-response
- Error: "Maximum context length exceeded"
- Incomplete implementations

**Diagnosis:**
The task is too large for a single subagent context window (~30K tokens).

**Solution:**
1. Split the task into smaller subtasks
2. Instead of "Create 50 data entries," split into:
   - "Create data types and helper functions"
   - "Create first 15 entries"
   - "Create next 15 entries"
   - "Create final 20 entries"
3. Have orchestrator track overall progress across multiple subtasks

**Prevention:**
- Review task size before delegating
- When dealing with large datasets, split proactively
- Set a rule: no more than ~20 items per delegation
- See "Task Splitting Guidelines" in GEMINI.md

#### Problem 8: Agent Using Fallbacks Instead of Stuck Agent

**Symptoms:**
- Agent says "I'll try a workaround"
- Agent implements alternative approach without asking
- Errors are hidden or ignored

**Diagnosis:**
Agent isn't following the "no fallbacks" rule and needs reinforcement.

**Solution:**
1. Update agent instructions to emphasize: "On ANY error, invoke stuck agent immediately"
2. Add examples of what counts as an error (package install fails, API returns 404, etc.)
3. Remove any language suggesting "try alternatives"
4. Explicitly state: "NEVER use workarounds without human approval"

**Example addition to agent instructions:**
```
CRITICAL: If ANY command fails, do NOT try alternatives.
Invoke the stuck agent with the error message and context.
Examples of errors requiring stuck agent:
- npm install fails
- API returns non-200 status
- File path doesn't exist
- Dependency conflict
- Authentication failure
```

**Prevention:**
- Reinforce stuck agent usage during onboarding
- Celebrate stuck agent usage (it's good practice!)
- Review agent responses and correct fallback attempts immediately

---

### Phase 3: Building & Personalizing Logic

#### Problem 9: Coder Creates 404 Errors (Links Without Pages)

**Symptoms:**
- Navigation links return 404 errors
- Header/footer links go nowhere
- Routing errors in console

**Diagnosis:**
Coder created links in header/footer/navigation without creating the corresponding pages. This is extremely common and should be caught during testing.

**Solution:**
1. Review all header/footer links
2. Create actual pages for each link:
   ```
   /about → Create about.jsx
   /contact → Create contact.jsx
   /pricing → Create pricing.jsx
   ```
3. Update routing configuration to include new pages
4. Test every link with tester agent

**Prevention:**
- Add to GEMINI.md: "ALWAYS create pages for EVERY link in headers/footers - NO 404s allowed"
- Add to coder's Definition of Done: "All navigation links must have corresponding pages"
- Tester agent should specifically check: "Verify all header/footer links navigate successfully"

**Real example:**
```
BAD: Created <Link to="/about">About</Link> without about.jsx
GOOD: Created Link AND created pages/about.jsx with content
```

#### Problem 10: Todo List Not Updating

**Symptoms:**
- Completed tasks still show as incomplete
- Orchestrator re-delegates already finished tasks
- Progress seems stuck

**Diagnosis:**
The orchestrator isn't updating the todo list after each completion, or TodoWrite isn't being used correctly.

**Solution:**
1. After EACH task completion, explicitly update todos:
   ```
   TodoWrite: Mark task #1 complete
   Move to task #2
   ```
2. Review current todo state regularly
3. Use clear numbering for tasks
4. Confirm completion before moving on

**Prevention:**
- Make todo updates part of the orchestrator's workflow
- Use numbered lists for easy tracking
- Review progress after every 3-5 tasks

#### Problem 11: Tests Pass Locally but Fail in Tester Agent

**Symptoms:**
- `npm test` passes on your machine
- Tester agent reports failures
- Screenshots show unexpected state

**Diagnosis:**
Environment differences between local and tester agent context, timing issues, or missing setup steps.

**Solution:**
1. Check if tester agent has same dependencies installed
2. Add explicit wait times for async operations
3. Ensure test setup is included in delegated task
4. Verify environment variables are available to tester
5. Screenshot comparison: local vs. tester output

**Example fix:**
```javascript
// BAD: Tests immediately, might not be ready
await page.goto('http://localhost:3000');
await page.click('#submit');

// GOOD: Waits for element to be ready
await page.goto('http://localhost:3000');
await page.waitForSelector('#submit');
await page.click('#submit');
```

**Prevention:**
- Include setup steps in test instructions
- Use explicit waits instead of assuming readiness
- Provide tester agent with complete environment setup

#### Problem 12: Agent Skips Definition of Done Checks

**Symptoms:**
- Agent reports completion but requirements aren't met
- Implementation is incomplete
- Edge cases not handled

**Diagnosis:**
The Definition of Done wasn't clear enough, or agent didn't validate against it.

**Solution:**
1. Make Definition of Done explicit and measurable:
   ```
   BAD: "Create a login form"
   GOOD: "Create a login form that:
   - Has email and password fields
   - Validates email format
   - Shows error messages for invalid input
   - Submits to /api/login endpoint
   - Redirects to /dashboard on success"
   ```
2. Add checklist format for complex tasks
3. Require agent to confirm each item before reporting completion

**Prevention:**
- Always include Definition of Done in task delegation
- Make criteria specific and testable
- Use checklists for multi-requirement tasks

---

### Phase 4: Testing & Self-Annealing

#### Problem 13: Playwright Can't Find Elements

**Symptoms:**
- Error: "Timeout waiting for selector"
- Element exists visually but test can't find it
- Selector works in browser devtools but fails in test

**Diagnosis:**
Selector is incorrect, element loads slowly, or there are multiple matching elements.

**Solution:**
1. Verify selector in browser devtools first
2. Use more specific selectors:
   ```
   BAD: page.click('button')
   GOOD: page.click('button[data-testid="submit-button"]')
   ```
3. Add wait conditions:
   ```javascript
   await page.waitForSelector('button[data-testid="submit"]');
   await page.click('button[data-testid="submit"]');
   ```
4. Check if element is in iframe (requires switching context)
5. Screenshot before click to verify element is visible

**Prevention:**
- Use data-testid attributes during implementation
- Add explicit waits for dynamic content
- Test selectors in isolated environment first

#### Problem 14: Screenshots Show Wrong Page

**Symptoms:**
- Tester screenshots don't match expected output
- Shows loading screen instead of content
- Captures before navigation completes

**Diagnosis:**
Timing issue: screenshot taken before page fully loads.

**Solution:**
1. Wait for navigation to complete:
   ```javascript
   await page.goto('http://localhost:3000/dashboard', {
     waitUntil: 'networkidle'
   });
   ```
2. Wait for specific content:
   ```javascript
   await page.waitForSelector('.dashboard-content');
   await page.screenshot({ path: 'dashboard.png' });
   ```
3. Add delay if necessary (last resort):
   ```javascript
   await page.waitForTimeout(2000); // 2 seconds
   ```

**Prevention:**
- Use `waitUntil: 'networkidle'` for SPAs
- Wait for key elements before screenshots
- Include wait instructions in tester delegation

#### Problem 15: Flaky Tests (Pass Sometimes, Fail Others)

**Symptoms:**
- Tests intermittently fail
- Works on retry
- No consistent error pattern

**Diagnosis:**
Race conditions, timing dependencies, or external service variability.

**Solution:**
1. Identify the flaky step (add logging)
2. Add retry logic for network requests:
   ```javascript
   await page.waitForResponse(
     response => response.url().includes('/api/data') && response.status() === 200
   );
   ```
3. Increase timeout for slow operations
4. Mock external dependencies when possible
5. Use deterministic test data

**Prevention:**
- Avoid time-dependent tests (comparing current date, etc.)
- Mock external APIs during testing
- Use stable test data
- Add sufficient wait conditions

#### Problem 16: Agent Reports Completion but Implementation Incomplete

**Symptoms:**
- Agent says "done" but features missing
- Partial implementation
- Edge cases not handled

**Diagnosis:**
Definition of Done was unclear, or agent misunderstood requirements.

**Solution:**
1. Review what was actually implemented vs. what was requested
2. Create new task for missing pieces
3. Improve Definition of Done for future tasks:
   ```
   Add checklist:
   - [ ] Happy path works
   - [ ] Error handling for invalid input
   - [ ] Loading states shown
   - [ ] Success confirmation displayed
   - [ ] Edge case: empty data handled
   ```
4. Invoke stuck agent if requirements were misunderstood

**Prevention:**
- Use detailed checklists for Definition of Done
- Include "edge cases" section in task specs
- Review implementation before marking complete

---

### Phase 5: Cloud Deployment (Cloudifying)

#### Problem 17: Modal Authentication Fails

**Symptoms:**
- Error: "Invalid token"
- 401 Unauthorized response
- Deployment rejected

**Diagnosis:**
Modal credentials are incorrect, expired, or not configured properly.

**Solution:**
1. Verify Modal credentials:
   ```bash
   modal token set --token-id ak-xxx --token-secret as-xxx
   ```
2. Check credentials are stored as Modal secrets (not in code)
3. Regenerate token if expired
4. Ensure token has correct permissions
5. Test authentication with simple Modal app first

**Prevention:**
- Store credentials in `.env` locally
- Use Modal secrets for production
- Document credential setup process
- Test authentication before full deployment

#### Problem 18: Endpoint Works Locally, Fails in Cloud

**Symptoms:**
- Local testing passes
- Deployed endpoint returns errors
- Different behavior in production

**Diagnosis:**
Environment differences: file paths, dependencies, environment variables.

**Solution:**
1. Check all file paths are relative (not absolute):
   ```python
   BAD: '/Users/name/project/data.json'
   GOOD: './data.json' or use Path(__file__).parent
   ```
2. Verify all dependencies in `requirements.txt`
3. Check environment variables are set in Modal
4. Review Modal logs for specific error messages
5. Test with Modal's local development mode first

**Prevention:**
- Use relative paths always
- Test in Modal dev mode before deploying
- Include all dependencies explicitly
- Document environment variables required

#### Problem 19: n8n Can't Reach Modal Endpoint

**Symptoms:**
- n8n HTTP Request node times out
- Connection refused errors
- No response from endpoint

**Diagnosis:**
URL incorrect, authentication missing, or endpoint not publicly accessible.

**Solution:**
1. Verify endpoint URL is correct (from Modal dashboard)
2. Check endpoint is deployed and running
3. Add Bearer token to n8n HTTP Request headers:
   ```
   Authorization: Bearer <your-token>
   ```
4. Test with cURL first:
   ```bash
   curl -X POST https://your-app.modal.run \
     -H "Authorization: Bearer your-token" \
     -H "Content-Type: application/json" \
     -d '{"test": "data"}'
   ```
5. Check Modal logs for incoming requests

**Prevention:**
- Test with cURL before n8n integration
- Document exact n8n configuration
- Include authentication in initial setup
- Verify URL and token together

#### Problem 20: Bearer Token Rejected

**Symptoms:**
- 401 Unauthorized despite correct token
- "Invalid token" error
- Authentication fails consistently

**Diagnosis:**
Token format incorrect, token not validated properly in endpoint, or token mismatch.

**Solution:**
1. Verify token format in request:
   ```
   Authorization: Bearer your-token-here
   ```
   (Note: "Bearer" with capital B, space before token)
2. Check endpoint validation logic:
   ```python
   auth_header = request.headers.get("Authorization")
   if not auth_header or not auth_header.startswith("Bearer "):
       return {"error": "Unauthorized"}, 401
   token = auth_header.split(" ")[1]
   if token != os.environ["EXPECTED_TOKEN"]:
       return {"error": "Invalid token"}, 401
   ```
3. Ensure token stored in Modal secrets matches
4. Test token independently

**Prevention:**
- Use exact token format from deployer agent
- Store token consistently across systems
- Add clear error messages for auth failures
- Test authentication before business logic

#### Problem 21: Production Errors in Shadow Orchestrator

**Symptoms:**
- Live endpoint returning errors
- Unknown error patterns
- Production behaving differently than expected

**Diagnosis:**
This is specifically for Shadow Orchestrator deployments (Strategy 2). Production errors need diagnosis.

**Solution:**
1. Check error classification (Tier 1, 2, or 3)
2. For Tier 1 (known errors): Support agent should auto-fix
3. For Tier 2 (unknown errors): Support agent diagnoses, decides fix or escalate
4. For Tier 3 (critical errors): Automatically escalates to stuck agent
5. Review production logs in Modal dashboard
6. Check if directive needs updating after resolution

**Prevention:**
- Only use Shadow Orchestrator for high-volume workflows
- Ensure error classification is robust
- Monitor production logs regularly
- Have rollback plan ready

**Note:** Most users use standard Hybrid Wrapper (Strategy 1) and won't encounter this. Shadow Orchestrator is advanced pattern for production self-annealing.

---

## When to Use the Stuck Agent: Detailed Criteria

The stuck agent is your safety net. Using it is a sign of professional development practice, not weakness. Here's exactly when to invoke it:

### Always Use Stuck Agent If:

1. **Installation Failures**
   - npm/pip/yarn install fails
   - Dependency conflicts
   - Version incompatibilities

2. **Authentication Issues**
   - API key rejected
   - OAuth flow fails
   - Token authentication doesn't work

3. **File System Problems**
   - Expected file doesn't exist
   - Permission denied errors
   - Path resolution failures

4. **Network/API Errors**
   - API returns non-200 status
   - Timeout errors
   - Rate limiting encountered

5. **Deployment Failures**
   - Modal deployment errors
   - Build failures
   - Configuration errors

6. **Test Failures**
   - Tests fail after second attempt
   - Unexpected behavior in testing
   - Screenshot shows wrong output

7. **Requirement Ambiguity**
   - Unclear business logic
   - Design decisions needed
   - Multiple valid interpretations

8. **Environment Issues**
   - Environment variable not loading
   - Service not starting
   - Port conflicts

9. **Data Problems**
   - Expected data format doesn't match
   - Database connection fails
   - Data validation errors

10. **Integration Failures**
    - Third-party service down
    - Webhook not receiving data
    - MCP connection issues

11. **Performance Issues**
    - Unexpectedly slow operations
    - Memory errors
    - Timeout on operations that should be fast

12. **Security Concerns**
    - Exposing sensitive data
    - Uncertain about credential storage
    - Authorization logic unclear

13. **Version Control Problems**
    - Git merge conflicts
    - Branch sync issues
    - Commit hook failures

14. **Build Errors**
    - Compilation failures
    - Bundle size issues
    - Asset loading problems

15. **Logic Uncertainty**
    - Multiple ways to solve problem
    - Unsure which approach is best
    - Need architectural decision

### Don't Try to Fix Yourself If:

- You're tempted to use a workaround
- The error message is unclear
- You've tried the same fix twice without success
- You need to make assumptions about requirements
- The solution requires guessing
- You're about to skip a validation step
- You want to "just get it working" without understanding why
- You're considering a quick hack instead of proper implementation

### Real Example Walkthrough

**Scenario:** Deploying to Modal, getting 401 Unauthorized error.

**Wrong approach:**
```
❌ "Let me try a different authentication method"
❌ "Maybe I can skip authentication for now"
❌ "I'll use a public endpoint instead"
```

**Correct approach:**
```
✅ Invoke stuck agent immediately:

"I'm attempting to deploy the lead scraper workflow to Modal.
The endpoint is deployed but returning 401 Unauthorized when
tested with the Bearer token.

Error message:
{
  "error": "Unauthorized",
  "detail": "Invalid authentication credentials"
}

What I tried:
1. Verified token format: Authorization: Bearer <token>
2. Checked token is stored in Modal secrets
3. Tested with cURL - same error

What I need:
Guidance on diagnosing the authentication issue. Should I
regenerate the token, check the endpoint code, or is there
a configuration issue?"
```

**Human decision:**
"Check the endpoint code - make sure it's reading from the correct environment variable name. Modal secrets must match exactly."

**Resolution:**
Found mismatch: code checked for `AUTH_TOKEN` but secret was stored as `BEARER_TOKEN`. Renamed secret, re-deployed, works perfectly.

**Learning documented:**
Updated deployment directive with: "Verify environment variable names match exactly between code and Modal secrets before deployment."

**Result:** Self-annealing occurred. Next time, this error won't happen.

---

## Quick Reference Tables

### Error Message Lookup

| Error Message | Likely Cause | Agent to Use | Quick Fix |
|---------------|--------------|--------------|-----------|
| "Module not found" | Missing dependency | Stuck | Check package.json, npm install |
| "401 Unauthorized" | Authentication failure | Stuck | Verify API key/token |
| "404 Not Found" | Missing page/endpoint | Coder | Create the page/route |
| "Timeout waiting for selector" | Element not ready/wrong selector | Tester | Add wait or fix selector |
| "Maximum context exceeded" | Task too large | Orchestrator | Split into smaller tasks |
| "Permission denied" | File/folder permissions | Stuck | Check agent mode settings |
| "Cannot resolve module" | Import path wrong | Coder | Fix import statement |
| "CORS error" | Cross-origin restriction | Stuck | Configure CORS headers |
| "Network request failed" | API/service down | Stuck | Check service status |
| "Invalid token" | Token format/value wrong | Stuck | Verify token and format |

### Common Symptoms by Phase

| Symptom | Phase | Likely Problem | Solution |
|---------|-------|----------------|----------|
| Agent won't start task | 2 | Missing task specs | Add objective, inputs, process, DOD |
| Links return 404 | 3 | Pages not created | Create page files for all links |
| Tests pass then fail | 4 | Timing/race condition | Add explicit waits |
| Local works, cloud fails | 5 | Environment difference | Check paths, dependencies, env vars |
| Agent implements code | 2 | Orchestrator confused | Reinforce delegation pattern |
| Tasks not updating | 3 | Todo list not maintained | Explicitly update after each task |
| Screenshot wrong page | 4 | Page not loaded | Wait for navigation complete |
| Endpoint times out | 5 | URL/auth issue | Test with cURL first |

### Agent Comparison Chart

| Task Type | Use This Agent | Don't Use |
|-----------|----------------|-----------|
| Implement feature | Coder | Orchestrator |
| Verify UI | Tester | Coder |
| Handle error | Stuck | Any other agent |
| Deploy to cloud | Deployer | Coder |
| Diagnose prod error | Support* | Stuck |
| Coordinate tasks | Orchestrator | Subagents |
| Split large task | Orchestrator | Coder |
| Ask human | Stuck (only!) | Any other |

*Only for Shadow Orchestrator deployments

---

## Getting Unstuck: The Systematic Workflow

When you're completely stuck and don't know what to do:

### Step 1: Don't Panic or Guess

Take a breath. Guessing or trying random solutions wastes time and creates more problems. The stuck agent exists specifically for this situation.

### Step 2: Gather Context

Collect this information before invoking stuck agent:

- **What you were trying to do** (the specific task)
- **What you expected to happen** (desired outcome)
- **What actually happened** (error message, unexpected behavior)
- **What you already tried** (list previous attempts)
- **Relevant code/config** (files, commands, settings)

### Step 3: Invoke Stuck Agent with Full Context

Format your request clearly:

```
Stuck Agent Request Template:

Task: [What you were implementing]

Expected: [What should happen]

Actual: [What actually happened]

Error message:
[Paste full error message]

What I tried:
1. [First attempt]
2. [Second attempt]
3. [Third attempt]

Relevant code:
[Paste relevant sections]

Question: [Specific question or request for guidance]
```

### Step 4: Wait for Human Decision

The stuck agent will escalate to a human who will:
- Review the context
- Diagnose the issue
- Provide specific guidance
- Make any necessary decisions

Do NOT proceed until you receive the response.

### Step 5: Implement the Decided Solution

Follow the guidance exactly:
- Don't improvise or add "improvements"
- Ask clarifying questions if anything is unclear
- Report back when implemented

### Step 6: Document the Learning

Update the relevant directive with:
- What went wrong
- Why it went wrong
- How it was fixed
- How to prevent it next time

This is self-annealing in action—the system learns and improves.

### Step 7: Continue Forward

With the issue resolved and documented:
- Mark the task complete
- Move to the next task
- Apply the learning to future work

### Example Walkthrough

**Situation:** npm install fails with dependency conflict.

**Step 1:** Recognize this is an error → invoke stuck agent (don't try to fix)

**Step 2:** Gather context:
```
- Task: Setting up React project
- Expected: Dependencies install successfully
- Actual: Error about React version conflict
- Tried: npm install, npm install --force, clearing node_modules
```

**Step 3:** Invoke stuck agent:
```
"I'm setting up a React project and npm install is failing with
a dependency conflict. Error message:

npm ERR! ERESOLVE unable to resolve dependency tree
npm ERR! While resolving: project@0.1.0
npm ERR! Found: react@18.2.0
npm ERR! Could not resolve dependency:
npm ERR! peer react@"^17.0.0" from react-router-dom@5.3.0

I tried:
1. npm install (failed)
2. npm install --force (installed but app won't run)
3. rm -rf node_modules && npm install (same error)

What should I do? Update react-router-dom or downgrade React?"
```

**Step 4:** Human responds:
```
"Update react-router-dom to version 6 which supports React 18:
npm install react-router-dom@6

Note: This changes the API slightly - you'll need to update any
<Switch> components to <Routes> and <Route> syntax is different."
```

**Step 5:** Implement:
```bash
npm install react-router-dom@6
# Update routing code as instructed
# Test that app runs
```

**Step 6:** Document learning:
```
Add to project setup directive:
"When using React 18, ensure react-router-dom is version 6+.
Version 5 has peer dependency on React 17 and will cause conflicts."
```

**Step 7:** Continue with next task (setup complete, move to building components)

---

```
┌─────────────────────────────────────────────────────┐
│  DOWNLOAD THE TROUBLESHOOTING FLOWCHART             │
│                                                      │
│  Get a printable PDF decision tree for diagnosing   │
│  issues and choosing the right agent:               │
│                                                      │
│  travissteel.net/the-last-employee/resources#reference          │
│                                                      │
│  Includes: Agent selection flowchart, error code    │
│  lookup table, and phase-by-phase checklists.       │
└─────────────────────────────────────────────────────┘
```

---

## Cross-References

For deeper understanding of concepts in this appendix:

- **Chapter 8: Phase 3 - Training Your AI Team** - Learn how to write clear directives and Definition of Done criteria
- **Chapter 9: Phase 4 - Bulletproofing with Testing & Self-Annealing** - Understand the testing philosophy and self-annealing process
- **Chapter 14: The Specialist Agents** - Detailed documentation of each agent's role and capabilities
- **Appendix E: MCP Configuration Guide** - Step-by-step MCP setup to avoid connection issues
- **Appendix F: Modal Deployment Guide** - Complete cloudifying instructions for Phase 5

---

## Final Thoughts: Troubleshooting is Learning

Every error you encounter is an opportunity to make your system stronger through self-annealing. When you:

1. Hit an error
2. Invoke the stuck agent
3. Receive guidance
4. Fix the issue
5. Document the learning

You're not just solving one problem—you're preventing it from happening again. The directives get updated, the system gets battle-hardened, and future implementations become smoother.

The best developers aren't the ones who never encounter errors. They're the ones who have systematic approaches to handling them. The stuck agent gives you that system.

**Remember:**
- Errors are normal and expected
- Asking for help is professional practice
- Self-annealing makes the system smarter
- Documentation prevents repeat issues

**When in doubt, invoke the stuck agent. It's not a last resort—it's best practice.**
