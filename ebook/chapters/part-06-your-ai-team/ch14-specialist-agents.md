# Chapter 14: The Specialist Agents - Your AI Dream Team

<!-- STATUS: Complete Draft -->
<!-- WORD TARGET: 4,500-5,500 words -->
<!-- ACTUAL WORD COUNT: ~5,200 words -->

## Chapter Summary
Meet the five specialist agents that work under your Orchestrator: the Coder who builds, the Tester who verifies, the Stuck Agent who escalates, the Deployer who launches, and the Support Agent who maintains production systems.

---

Imagine you're hiring for a major project. You need someone to build a client onboarding system—forms, email automation, database integration, payment processing, the works.

You have two options:

**Option A**: Hire one person who will do everything. They'll design the interface, write all the code, test every feature, deploy to production, and handle ongoing maintenance. One person, one massive job description.

**Option B**: Hire a team of specialists. A developer who writes code, a QA tester who verifies everything works, a project manager who escalates problems, a DevOps engineer who handles deployment, and a support engineer who maintains the live system.

Which team ships faster? Which produces better results? Which one doesn't collapse under the complexity?

Option B wins every time. Not because the individuals are more talented, but because **specialization beats generalization** when the stakes are high.

This is exactly why the DOE framework uses specialist agents instead of one "do-everything" AI. The Orchestrator you met in Chapter 13 doesn't implement code, doesn't run tests, doesn't deploy to production. It manages specialists who do those jobs better because they have one clear focus and a fresh start for every task.

In this chapter, you'll meet your AI dream team: the five specialist agents that turn your directives into production-ready systems.

---

## The Problem with One-AI-Does-Everything

Before we dive into the specialists, let's understand why the traditional "single AI conversation" model breaks down.

When you open ChatGPT and start building something complex, here's what happens:

**Message 1-10**: The AI is sharp. It understands your requirements clearly and implements exactly what you asked for.

**Message 11-25**: The AI starts juggling multiple threads. It's trying to remember the database structure from message 5, the brand colors from message 8, and the API endpoints from message 12. You start noticing small inconsistencies.

**Message 26-50**: The AI is overloaded. It's repeating things it already said. It's forgetting details you specified earlier. It starts contradicting itself. You're spending more time correcting mistakes than making progress.

**Message 51+**: You're frustrated. You're re-explaining basic requirements. You're copying and pasting your own earlier messages to remind the AI what it's supposed to be doing. The conversation has become a second job.

This isn't the AI's fault. It's a context management problem.

Think of it like asking a single employee to simultaneously write code, test the code, design the interface, handle customer support, and deploy to production—all while remembering every detail from a three-week-long conversation. That employee's brain would melt.

Human brains have a limit. So do AI context windows. Even with 200,000 tokens, a single AI conversation degrades when it's trying to hold too many responsibilities at once.

**The DOE solution:** Give each job to a specialist with a clean slate.

The Coder gets a fresh context window with one task: "Build the user registration form." It's not distracted by deployment details or test scenarios. It focuses on writing clean, functional code.

The Tester gets a fresh context window with one task: "Verify the registration form works correctly." It's not thinking about database schemas or API integrations. It's purely focused on quality assurance.

Each specialist starts fresh, stays focused, and does one job exceptionally well.

The Orchestrator coordinates them all, maintaining the big picture while the specialists handle the details.

This is how real teams work. This is how AI teams should work too.

---

## The Five Specialists

Let's meet the team.

### 1. The Coder: Your Implementation Expert

**Role**: Turns directives into working code.

The Coder is your hands-on builder. When the Orchestrator delegates a task like "Create a contact form with email validation," the Coder writes the HTML, CSS, JavaScript, and server-side logic to make that happen.

**What the Coder does:**

- Writes clean, functional code based on the task directive
- Follows best practices for the language and framework
- Implements error handling and validation
- Creates necessary files and folder structures
- Documents what it built and why
- Tests basic functionality with Bash commands when applicable

**What the Coder does NOT do:**

- Make assumptions when requirements are unclear
- Use workarounds when something fails
- Skip error handling to "finish faster"
- Proceed blindly past obstacles

**The Coder's superpower: Focus without distraction.**

Because the Coder works in its own context window, it's not juggling the entire project history. It gets one task, implements it completely, and reports back. This means:

- **Cleaner code**: Without distractions, the Coder writes code that's maintainable and well-structured.
- **Faster completion**: The Coder isn't context-switching between design decisions and deployment concerns.
- **Fewer bugs**: The Coder follows the exact specifications in the directive without "creative interpretation."

**The Coder's critical rule: When stuck, escalate immediately.**

Here's what separates the DOE Coder from a traditional AI assistant: it knows when to stop.

If the Coder hits an error—a package won't install, a file path doesn't exist, an API returns an unexpected response—it doesn't guess. It doesn't try five different workarounds. It immediately invokes the Stuck Agent and asks a human for guidance.

This might sound inefficient ("Why not let the AI figure it out?"), but it's actually a massive time-saver. Here's why:

**Without the Stuck Agent:**
- Coder hits an error
- Coder tries a workaround (guesses)
- Workaround creates a new problem
- Coder tries another workaround
- Three workarounds later, the code is a mess
- You spend hours debugging the "solutions" the AI invented

**With the Stuck Agent:**
- Coder hits an error
- Coder invokes Stuck Agent: "Package installation failed. Should we use a different package or fix the dependency issue?"
- Human responds: "Use this alternative package instead."
- Coder implements the correct solution immediately
- Project continues on solid foundation

The Stuck Agent pattern prevents "spaghetti code" where the AI has layered workaround upon workaround to avoid asking for help.

**Real example:**

The Orchestrator delegates: "Create an email notification system using the Resend API."

The Coder starts implementing. It realizes the Resend API key isn't configured in the environment variables.

A traditional AI would:
1. Assume a placeholder key
2. Or skip the integration and leave a "TODO" comment
3. Or use a different email service without asking

The DOE Coder:
1. Stops immediately
2. Invokes the Stuck Agent: "Resend API key not found in .env file. Should I configure it now or use a placeholder for testing?"
3. Human responds: "Here's the API key: rsk_abc123. Add it to the .env file."
4. Coder implements correctly with the real key

The project continues on a solid foundation instead of building on assumptions.

**Self-Annealing: The Coder learns from errors.**

When the Coder encounters and resolves an issue (with human help via the Stuck Agent), it documents what went wrong and what solution worked. This information flows back to the Orchestrator, which can update the directive for future runs.

For example, if the Coder discovers that Package X doesn't work on Windows but Package Y does, that learning gets documented. The next time a similar task runs, the directive includes: "On Windows systems, use Package Y instead of Package X."

This is self-annealing in action: the system battle-hardens itself with every problem it solves.

---

### 2. The Tester: Your Quality Assurance Inspector

**Role**: Visually verifies that implementations actually work.

The Tester is your quality gatekeeper. It doesn't just look at code and assume it works. It actually renders the output, takes screenshots, and verifies that what was built matches what was requested.

**What the Tester does:**

- Uses Playwright MCP to navigate to web pages and applications
- Takes screenshots of actual rendered output
- Verifies visual layout, positioning, and styling
- Tests interactive elements (buttons, forms, navigation)
- Checks responsive design at different screen sizes
- Confirms all links work and lead to the correct destinations
- Validates against the "Definition of Done" from the directive

**What the Tester does NOT do:**

- Assume something works because the code looks correct
- Mark tests as passing without visual proof
- Skip verification steps to save time
- Try to fix broken implementations (that's the Coder's job)

**The Tester's superpower: Seeing is believing.**

Here's why visual testing matters so much:

Code can look perfect and still be completely broken in practice. A CSS file might have correct syntax but position elements 100 pixels off-screen. A form might have proper validation logic but display error messages in white text on a white background. A navigation menu might have all the right links but be invisible on mobile devices.

The Tester catches these issues because it actually renders the output and looks at it.

**Real example:**

The Orchestrator delegates to the Tester: "Verify that the contact form displays correctly and accepts user input."

Here's what the Tester does:

1. Uses Playwright MCP to navigate to `http://localhost:3000/contact`
2. Takes a screenshot of the initial page load
3. Verifies all form fields are visible (name, email, message)
4. Checks that field labels are readable
5. Fills in the form fields using Playwright
6. Takes a screenshot of the filled form
7. Submits the form
8. Takes a screenshot of the confirmation message
9. Verifies the form submission succeeded

If any step fails—if a field is missing, if the submit button doesn't work, if the confirmation message doesn't appear—the Tester captures a screenshot showing exactly what's wrong and invokes the Stuck Agent with visual proof.

**The Tester prevents "works on my machine" problems.**

One of the most common issues in software development: the developer tests on their own computer and everything works fine. Then it ships to production and breaks for users.

Why? Because the developer's environment is different. They have specific browser extensions. They're testing on a large monitor. They have cached data that masks a bug.

The Tester simulates a real user environment. It tests at multiple screen sizes (mobile, tablet, desktop). It clears cache between tests. It verifies functionality from a clean slate.

This catches environment-specific bugs before they reach production.

**The Tester's critical rule: No visual issue is too small.**

If the Tester sees something wrong in a screenshot—a button is misaligned by 5 pixels, a color is slightly off, a font size is inconsistent—it reports it. It doesn't assume "close enough is good enough."

Why? Because small visual issues compound. A button that's 5 pixels too far right might be invisible on some screen sizes. A font that's 1pt too small might be unreadable for users with visual impairments. A color that's "close" to the brand guide might damage client trust.

The Tester's job is to ensure what was built matches exactly what was specified. Period.

**Self-Annealing: The Tester improves test coverage.**

When the Tester discovers an edge case—like "the form breaks when a user enters an email with a plus sign"—it documents that finding. Future test directives include that scenario.

Over time, the test suite becomes more comprehensive. The system learns what to check based on what's broken before.

> [!IMPORTANT]
> The Tester uses a separate context window from the Coder. This means it approaches every task with fresh eyes, no assumptions, and no bias toward "hoping" the code works. It's the independent inspector you need to maintain quality.

---

### 3. The Stuck Agent: Your Human Liaison

**Role**: Escalates problems to you when any agent hits an obstacle.

The Stuck Agent is the most important agent in the entire system. Why? Because it's the only agent allowed to ask you questions, and it ensures the system never proceeds blindly past errors.

**What the Stuck Agent does:**

- Receives escalations from other agents when they encounter problems
- Gathers context about the issue (error messages, screenshots, logs)
- Presents the problem to you clearly and concisely
- Offers 2-4 specific options for how to proceed
- Waits for your decision
- Relays your decision back to the agent that escalated

**What the Stuck Agent does NOT do:**

- Make decisions on behalf of the human
- Suggest workarounds or fallbacks
- Allow other agents to proceed without human input
- Skip escalation to "save time"

**The Stuck Agent's superpower: Guaranteed human control.**

Here's the fundamental safety principle of the DOE framework: **The system never guesses on important decisions.**

In traditional AI workflows, when the AI encounters an error, it either:
1. Makes an assumption and continues (risky)
2. Throws a generic error and stops (unhelpful)
3. Tries multiple workarounds until something sticks (creates technical debt)

All three options are problematic. Option 1 can lead to incorrect implementations. Option 2 wastes your time debugging. Option 3 creates a mess of band-aid solutions.

The Stuck Agent solves this by enforcing a hard rule: **When any agent hits a problem, stop and ask a human.**

**Real example:**

The Coder is implementing a payment integration and discovers two possible APIs: Stripe and PayPal. The directive doesn't specify which one to use.

A traditional AI might:
- Pick whichever is more popular (Stripe)
- Implement both and let you choose later (wasted effort)
- Skip the payment integration entirely (incomplete work)

The DOE Coder invokes the Stuck Agent:

**Stuck Agent presents to you:**

```
PROBLEM: Payment Integration Choice
The directive specifies "payment processing" but doesn't indicate which provider.

OPTIONS:
1. Use Stripe (most common, 2.9% + $0.30 per transaction)
2. Use PayPal (familiar to users, 3.49% + $0.49 per transaction)
3. Implement both (more flexibility, more complexity)
4. Pause and clarify requirements first

Which should we proceed with?
```

You respond: "Use Stripe. Our accounting system already integrates with it."

The Stuck Agent relays this to the Coder: "Use Stripe for payment processing. Reasoning: existing accounting integration."

The Coder implements Stripe. The project continues on solid ground.

**Total time cost to you: 30 seconds to make a decision.**

Compare that to the alternative: discovering two weeks later that the AI picked PayPal and now you have to refactor the entire payment system because your accounting doesn't support it.

**The Stuck Agent makes AI safe for business-critical work.**

The reason most businesses don't trust AI with important tasks: they're worried the AI will make a mistake they don't catch until it's too late.

The Stuck Agent eliminates that fear. It ensures that humans review all critical decision points, while still allowing the AI to handle the routine implementation work.

You're not micromanaging every line of code. You're making high-level decisions when they matter.

This is the difference between "AI as an assistant" (you control everything) and "AI as a team" (you manage strategically, AI executes tactically).

**Self-Annealing: The Stuck Agent captures lessons learned.**

Every time the Stuck Agent escalates a problem and receives your decision, it documents the context and the reasoning. This becomes part of the self-annealing process.

For example, if you consistently choose Stripe over PayPal for payment integrations, that pattern gets documented. Future directives can include: "For payment processing, default to Stripe unless client specifically requires PayPal."

The system learns your preferences and decision patterns, reducing the number of escalations over time while maintaining safety.

> [!IMPORTANT]
> The Stuck Agent is your guarantee that AI stays under your control. It's the difference between an AI assistant and an AI that makes decisions on your behalf. You never want the latter.

---

### 4. The Deployer: Your DevOps Engineer

**Role**: Takes battle-tested local workflows and deploys them to production in the cloud.

The Deployer is your deployment specialist. Once you've built and tested a workflow locally (Phase 3-4 of the DOE framework), the Deployer handles everything needed to make it live and accessible to clients.

**What the Deployer does:**

- Converts local workflows into production-ready cloud endpoints
- Sets up authentication and security (Bearer tokens, API keys)
- Deploys to Modal (serverless Python platform)
- Returns a complete handover package:
  - Production endpoint URL
  - Authentication credentials
  - cURL command for testing
  - n8n HTTP Request node configuration
  - Input/output specifications
  - Client documentation

**What the Deployer does NOT do:**

- Deploy untested code (always requires Phase 3-4 completion first)
- Skip security configuration
- Make assumptions about infrastructure requirements
- Proceed without verifying successful deployment

**The Deployer's superpower: Client-ready handoffs in minutes.**

Here's the traditional deployment pain: you've built a workflow that works perfectly on your local machine. Now you need to get it live so a client can use it. You spend hours configuring servers, setting up authentication, writing deployment scripts, creating documentation, and testing in production.

The Deployer does all of this automatically.

**Real example:**

You've built a lead enrichment workflow that takes a company name, researches it online, and returns structured data (industry, size, funding, key contacts). It works great locally. Now you need to deploy it so your sales team can trigger it from their CRM via a webhook.

The Orchestrator delegates to the Deployer: "Deploy the lead enrichment workflow to Modal with webhook authentication."

The Deployer:

1. Reviews the local workflow code
2. Wraps it in a Modal-compatible function
3. Adds Bearer token authentication
4. Tests the endpoint locally
5. Deploys to Modal's cloud infrastructure
6. Captures the production URL: `https://unified--lead-enrichment.modal.run`
7. Generates a secure Bearer token and stores it as a Modal secret
8. Tests the live endpoint with a cURL command
9. Creates an n8n HTTP Request node configuration
10. Writes client documentation explaining how to trigger the workflow

The Deployer returns this complete package to you in about 2-3 minutes.

You now have:
- A live endpoint your CRM can call
- Authentication set up securely
- A working cURL command to test with
- An n8n workflow template ready to import
- Documentation you can send to your client

**The Hybrid Wrapper Strategy: Making agentic workflows client-friendly.**

One of the Deployer's key responsibilities is implementing the Hybrid Wrapper pattern. This combines the power of your agentic Python workflow with the accessibility of visual no-code tools like n8n.

Here's what that looks like:

**Layer 1 (Client-Facing)**: n8n workflow with visual nodes
- Trigger: Form submission, email arrival, webhook, schedule
- HTTP Request: Calls your Modal endpoint
- Final Action: Send email, update CRM, post to Slack

**Layer 2 (Your Agentic Logic)**: Modal endpoint with Python code
- Receives the request from n8n
- Runs your complex agentic workflow
- Returns structured results

**Layer 3 (Security)**: Bearer token authentication
- n8n includes the token in the request header
- Modal validates the token before processing
- Unauthorized requests are rejected

The client gets a visual workflow they can understand and modify. You keep your complex logic in version-controlled Python that's battle-tested and reliable.

**The Deployer's critical rule: Never deploy untested code.**

The Deployer only runs after Phase 3 (Building) and Phase 4 (Testing) are complete. It refuses to deploy workflows that haven't been battle-tested locally.

Why? Because production errors are expensive. If something breaks locally, you fix it and try again. If something breaks in production, your client sees the error, loses trust, and might stop using the system.

The Deployer ensures that what reaches production is already proven to work.

> [!TIP]
> The Deployer only gets invoked AFTER Phases 3-4 are complete (build and test locally). Never deploy code that hasn't been battle-tested. Fix all the bugs in the safety of your local environment before shipping to the cloud.

---

### 5. The Support Agent: Your On-Call Engineer (Advanced)

**Role**: Monitors production systems and auto-fixes non-critical errors.

The Support Agent is the most advanced specialist, used only in Shadow Orchestrator deployments (Strategy 2). Most businesses won't need this agent initially, but it's worth understanding for when your systems scale.

**What the Support Agent does:**

- Monitors production endpoints for errors
- Diagnoses issues when workflows fail
- Auto-fixes known, non-critical errors
- Escalates critical errors to the Stuck Agent (and to you)
- Updates directives with fixes so errors don't recur
- Redeploys corrected workflows automatically

**What the Support Agent does NOT do:**

- Auto-fix critical errors (data corruption, security issues, business logic failures)
- Modify production without logging changes
- Skip human approval for significant changes
- Ignore patterns that suggest larger problems

**The Support Agent's superpower: Self-healing production systems.**

Here's the problem with traditional production systems: when something breaks, it stays broken until a human notices and fixes it. If that breakage happens at 2 AM on a Sunday, your system is down for hours.

The Support Agent provides graduated error response:

**Tier 1: Known Errors (Auto-Fix)**
- Input validation failures
- Rate limiting issues
- Timeout errors
- Temporary API unavailability

The Support Agent fixes these automatically, logs the fix, and continues. No human needed.

**Tier 2: Unknown Errors (Diagnose & Decide)**
- New error patterns
- Unexpected API responses
- Edge cases not previously encountered

The Support Agent analyzes the error, determines if it's safe to auto-fix, and either fixes it or escalates to a human.

**Tier 3: Critical Errors (Always Escalate)**
- Data corruption
- Security vulnerabilities
- Business logic failures
- Financial transaction errors

The Support Agent immediately invokes the Stuck Agent, which alerts you with full context.

**Real example:**

You have a production workflow that scrapes company data from LinkedIn. It's been running successfully for weeks. Then LinkedIn changes their page layout.

**Traditional system:**
- Scraper breaks
- Workflow fails silently
- You discover the issue 3 days later when a client asks why they haven't received updates
- You spend an hour debugging
- You fix the scraper manually
- Lost time: 3 days of missing data + 1 hour debugging

**With Support Agent:**
- Scraper hits an error (can't find the expected HTML element)
- Support Agent diagnoses: "LinkedIn page structure changed"
- Support Agent analyzes the new page structure
- Support Agent updates the scraper to use the new HTML selectors
- Support Agent tests the fix
- Support Agent redeploys the corrected workflow
- Support Agent logs the change: "Updated LinkedIn scraper for new page layout"
- Total downtime: 2-3 minutes (automated)

You wake up the next morning to a notification: "Production issue auto-fixed: LinkedIn layout change. Scraper updated and redeployed. No data loss."

**When you need the Support Agent:**

Most businesses start with the standard deployment strategy (Strategy 1), which doesn't include production self-annealing. You only add the Support Agent when:

- You have high-volume production workflows (hundreds of runs per day)
- Downtime has significant business impact
- You want continuous improvement from production learnings
- You're comfortable with AI making non-critical operational decisions

For most client handoffs, the standard Hybrid Wrapper (Deployer only) is sufficient.

> [!IMPORTANT]
> The Support Agent is an advanced feature. If you're just getting started with agentic workflows, use Strategy 1 (standard Hybrid Wrapper) and skip the Support Agent. Add it later when your workflows are mature and you want production self-annealing.

---

## How the Specialists Work Together

Let's watch the full team collaborate on a real project: building an automated invoice processing system.

**You say:** "Build a system that extracts data from invoice PDFs, validates the amounts, and posts to QuickBooks."

### Phase 1: Planning

**Orchestrator** creates an 8-task breakdown:
1. Set up workspace and dependencies
2. Create data types for invoice fields
3. Build PDF extraction module (OCR)
4. Build validation rules
5. Create QuickBooks API integration
6. Build error handling and logging
7. Test with sample invoices
8. Deploy to production

### Phase 2: Implementation (Tasks 1-6)

**Task 1: Workspace setup**
- Orchestrator → Coder: "Set up Python project with necessary dependencies"
- Coder: Creates folder structure, requirements.txt, .env template
- Orchestrator → Tester: "Verify project initializes without errors"
- Tester: Runs `python main.py`, confirms no errors, takes screenshot
- Result: Task 1 complete ✓

**Task 2: Data types**
- Orchestrator → Coder: "Create data models for invoice fields (vendor, date, amount, line items)"
- Coder: Implements Pydantic models with validation
- Orchestrator → Tester: "Verify data models handle valid and invalid inputs correctly"
- Tester: Tests with sample data, confirms validation works
- Result: Task 2 complete ✓

**Task 3: PDF extraction**
- Orchestrator → Coder: "Build OCR module to extract structured data from invoice PDFs"
- Coder: Starts implementing with PyPDF2, hits error (doesn't handle scanned PDFs)
- Coder → Stuck Agent: "PyPDF2 can't extract text from scanned PDFs. Should we use OCR library or restrict to digital PDFs only?"
- Stuck Agent → You: Presents the choice
- You: "Use Tesseract OCR to handle both digital and scanned PDFs"
- Stuck Agent → Coder: "Implement Tesseract OCR for both PDF types"
- Coder: Implements with pytesseract
- Orchestrator → Tester: "Test extraction with both digital and scanned invoice samples"
- Tester: Confirms both types work, captures screenshots
- Result: Task 3 complete ✓

**Task 4: Validation rules**
- Orchestrator → Coder: "Implement validation: check for duplicates, flag amounts over $10k, verify totals match line items"
- Coder: Implements validation logic
- Orchestrator → Tester: "Test validation with edge cases (duplicate invoices, high amounts, mismatched totals)"
- Tester: Confirms all validation rules trigger correctly
- Result: Task 4 complete ✓

**Task 5: QuickBooks integration**
- Orchestrator → Coder: "Create QuickBooks API integration to post validated invoices"
- Coder: Implements OAuth flow and API calls
- Orchestrator → Tester: "Test API connection and invoice posting with test QuickBooks account"
- Tester: Verifies invoices appear in QuickBooks, captures screenshots
- Result: Task 5 complete ✓

**Task 6: Error handling**
- Orchestrator → Coder: "Add comprehensive error handling and logging for all modules"
- Coder: Implements try-catch blocks, logging to file and console
- Orchestrator → Tester: "Trigger intentional errors and verify they're caught and logged properly"
- Tester: Confirms error handling works
- Result: Task 6 complete ✓

### Phase 3: End-to-End Testing

**Task 7: Integration testing**
- Orchestrator → Tester: "Run complete workflow with 10 different invoice formats"
- Tester: Processes sample invoices, verifies:
  - PDFs extracted correctly
  - Data validated properly
  - Invoices posted to QuickBooks
  - Errors logged when expected
  - Screenshots captured for each step
- Result: Task 7 complete ✓

### Phase 4: Deployment

**Task 8: Go live**
- Orchestrator → Deployer: "Deploy invoice processing system to Modal with webhook trigger"
- Deployer:
  - Converts to Modal-compatible endpoint
  - Adds Bearer token authentication
  - Tests locally
  - Deploys to production
  - Returns endpoint URL: `https://unified--invoice-processor.modal.run`
  - Provides cURL command for testing
  - Creates n8n workflow configuration
  - Writes client documentation
- Result: Task 8 complete ✓

### Phase 5: Production Monitoring (Optional - Shadow Orchestrator Only)

**Ongoing: Support Agent monitors**
- Support Agent: Watches for errors in production
- Week 2: Detects that invoices with European date format (DD/MM/YYYY) fail validation
- Support Agent: Auto-fixes by adding date format detection
- Support Agent: Logs change and updates directive
- You receive notification: "Auto-fixed: Added European date format support"

---

## Agent Roles at a Glance

| Agent | Role | When to Invoke | Returns | On Error |
|-------|------|----------------|---------|----------|
| **Coder** | Implements code from directives | Every coding task | Working implementation | Invokes Stuck Agent |
| **Tester** | Visually verifies functionality | After every Coder task | Pass/fail + screenshots | Invokes Stuck Agent |
| **Stuck** | Human escalation point | When any agent hits a problem | Human decision + guidance | N/A (IS the escalation) |
| **Deployer** | Cloud deployment & handoffs | When ready to go live | Endpoint + auth + docs | Invokes Stuck Agent |
| **Support** | Production error diagnosis | Only in Shadow Orchestrator | Auto-fix or escalation | Invokes Stuck Agent for critical errors |

---

## The Agent Interaction Flow

```
┌─────────────────────────────────────────────────────────────┐
│                  SPECIALIST AGENT WORKFLOW                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ORCHESTRATOR: "Build invoice processing system"           │
│         │                                                    │
│         ▼                                                    │
│  ORCHESTRATOR: Creates 8-task breakdown                     │
│         │                                                    │
│         ▼                                                    │
│  ┌──────────────────────────────────────────┐              │
│  │  TASK 1: Set up workspace                │              │
│  │                                           │              │
│  │  ORCHESTRATOR → CODER                     │              │
│  │    (fresh context, focused task)         │              │
│  │         │                                 │              │
│  │         ▼                                 │              │
│  │  CODER: Implements solution               │              │
│  │         │                                 │              │
│  │         ▼                                 │              │
│  │  ORCHESTRATOR → TESTER                    │              │
│  │    (fresh context, verify only)          │              │
│  │         │                                 │              │
│  │         ▼                                 │              │
│  │  TESTER: Takes screenshots, verifies      │              │
│  │         │                                 │              │
│  │         ▼                                 │              │
│  │  Result: ✓ PASS                          │              │
│  └──────────────────────────────────────────┘              │
│         │                                                    │
│         ▼                                                    │
│  ┌──────────────────────────────────────────┐              │
│  │  TASK 3: PDF extraction                  │              │
│  │                                           │              │
│  │  ORCHESTRATOR → CODER                     │              │
│  │         │                                 │              │
│  │         ▼                                 │              │
│  │  CODER: Hits error (scanned PDFs fail)   │              │
│  │         │                                 │              │
│  │         ▼                                 │              │
│  │  CODER → STUCK AGENT                      │              │
│  │    "PyPDF2 can't handle scanned PDFs.    │              │
│  │     Use OCR or restrict to digital only?" │              │
│  │         │                                 │              │
│  │         ▼                                 │              │
│  │  STUCK AGENT → HUMAN                      │              │
│  │    Presents choice with context           │              │
│  │         │                                 │              │
│  │         ▼                                 │              │
│  │  HUMAN: "Use Tesseract OCR"              │              │
│  │         │                                 │              │
│  │         ▼                                 │              │
│  │  STUCK AGENT → CODER                      │              │
│  │    Relays decision                        │              │
│  │         │                                 │              │
│  │         ▼                                 │              │
│  │  CODER: Implements Tesseract              │              │
│  │         │                                 │              │
│  │         ▼                                 │              │
│  │  ORCHESTRATOR → TESTER                    │              │
│  │         │                                 │              │
│  │         ▼                                 │              │
│  │  TESTER: Verifies both PDF types work    │              │
│  │         │                                 │              │
│  │         ▼                                 │              │
│  │  Result: ✓ PASS                          │              │
│  └──────────────────────────────────────────┘              │
│         │                                                    │
│         ▼                                                    │
│  ... Tasks 4-7 complete ...                                │
│         │                                                    │
│         ▼                                                    │
│  ┌──────────────────────────────────────────┐              │
│  │  TASK 8: Deploy to production            │              │
│  │                                           │              │
│  │  ORCHESTRATOR → DEPLOYER                  │              │
│  │    (fresh context, deployment only)      │              │
│  │         │                                 │              │
│  │         ▼                                 │              │
│  │  DEPLOYER: Deploys to Modal               │              │
│  │         │                                 │              │
│  │         ▼                                 │              │
│  │  Returns: Endpoint + auth + docs         │              │
│  │         │                                 │              │
│  │         ▼                                 │              │
│  │  Result: ✓ LIVE                          │              │
│  └──────────────────────────────────────────┘              │
│         │                                                    │
│         ▼                                                    │
│  ORCHESTRATOR: "All tasks complete. System deployed."       │
│         │                                                    │
│         ▼                                                    │
│  [OPTIONAL: Shadow Orchestrator only]                       │
│         │                                                    │
│  SUPPORT AGENT: Monitors production                         │
│    Auto-fixes non-critical errors                           │
│    Escalates critical errors to Stuck Agent                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Try It Yourself: Observe Agent Collaboration

Here's an exercise to understand how the specialists work together:

**Step 1: Pick a simple project**

Choose something small enough to complete in 30-60 minutes:
- A contact form that emails you submissions
- A simple web scraper that collects data from a public website
- An automated email responder that replies to form submissions

**Step 2: Write the high-level goal**

Write one sentence describing what you want built:

*"Create a contact form that collects name, email, and message, then sends the submission to my email address."*

**Step 3: Watch the specialists in action**

If you have access to the DOE framework, delegate this to your Orchestrator and observe:

- How the Orchestrator breaks down your one sentence into 5-8 specific tasks
- How the Coder gets a fresh start for each task
- How the Tester takes actual screenshots to verify functionality
- If an error occurs, how the Stuck Agent presents the problem to you
- How quickly the Deployer can make it production-ready

**Step 4: Compare to a single-AI approach**

Now try building the same thing in a ChatGPT conversation (don't use the DOE framework). Notice:

- How many times you have to re-explain requirements
- How long it takes to debug issues
- How much context-switching happens
- How tired you are at the end versus how fresh you were with the DOE approach

The difference is the specialist advantage. Each agent has one job and does it exceptionally well, while the Orchestrator maintains the big picture.

---

## Key Takeaway

**One AI trying to do everything creates mediocre results. A team of specialists, each with one focused job, creates production-ready systems.**

The Coder writes clean code. The Tester proves it works. The Stuck Agent keeps you in control. The Deployer makes it live. The Support Agent keeps it running.

Each specialist starts fresh, stays focused, and escalates when stuck. The Orchestrator coordinates them all, maintaining perfect memory of the big picture while specialists handle the details.

This is how real development teams work. This is how AI teams should work too.

In the next chapter, we'll explore why this isolation—giving each specialist a fresh context—is the secret that makes the entire system work. You'll see why "context isolation" is the breakthrough that transformed AI from a chatbot into a reliable team.

---

> [!TIP]
> **Start with the Core Three**: Most projects only need Coder, Tester, and Stuck Agent. Add Deployer when you're ready to go live. Add Support Agent only for high-volume production systems. Don't overcomplicate—start simple and expand as needed.

┌─────────────────────────────────────────────────────┐
│  DOWNLOAD THE AGENT DEFINITIONS                     │
│                                                      │
│  Get the complete agent configuration files:        │
│  • coder.md                                          │
│  • tester.md                                         │
│  • stuck.md                                          │
│  • deployer.md                                       │
│  • support.md                                        │
│                                                      │
│  travissteel.net/the-last-employee/resources#specialist-agents   │
└─────────────────────────────────────────────────────┘
