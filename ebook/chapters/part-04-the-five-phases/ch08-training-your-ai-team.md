# Chapter 8: Tactical Delegation: Commanding Your AI Team

## The End of the Mega-Prompt

If you’ve spent any time in the AI space, you’ve seen the "Mega-Prompt." Users try to cram an entire project specification into a single 5,000-word block of text, hit enter, and cross their fingers.

Then they wonder why the AI gets confused at Step 47, starts hallucinating code, or ignores their safety constraints.

The reality is simple: **Complex missions break single-agent workflows.** 

Trying to build a production-ready lead generation pipeline in a single conversation is like hiring one person to be your CEO, your Lead Developer, your QA Engineer, and your Social Media Manager simultaneously. You’re not "scaling"—you’re creating a single point of failure.

In the Antigravity ecosystem, we don't use mega-prompts. We use **Tactical Delegation**.

We follow a strict Chain of Command: One Orchestrator (you) managing multiple specialist subagents. Each agent has one job, one fresh context window, and one definition of done. This is how you build systems that don't just work—they scale.

---

## The Solution: The Orchestration Loop

We solve the "Context Bloat" problem by isolating cognitive load. 

**The Workforce of One Model:**
- **The Orchestrator**: maintains the big picture, the 1M+ token context, and the strategic roadmap.
- **The Coder (Specialist)**: receives one discrete task, builds it in a fresh context, and returns the result.
- **The Tester (QA)**: verifies the Coder's work against the mission's Definition of Done.
- **The Stuck Agent (Escalation)**: a dedicated protocol for when the machine hits a wall.

This isn't just "chatting." This is a high-performance **Command Cycle**.

---

## The Command Cycle: Plan, Delegate, Verify

To build a "Workforce of One," you must master the iterative cycle of delegation. Stop thinking like a writer; start thinking like a Commander.

### Command Step 1: The Strategic Breakdown

Before a single line of code is written, you must break the mission into tactical tasks. 

**Amateur Breakdown:**
- [ ] Build the scraper.

**Orchestrator Breakdown:**
- [ ] Initialize Python environment and dependencies.
- [ ] Build static HTML extraction module for `./target-list.csv`.
- [ ] Implement email validation regex and status logging.
- [ ] Build CSV export module with deduplication logic.

Each task must be **Discrete, Verifiable, and Independent.** If a task feels too big, split it. If a task has two different goals, split it.

### Command Step 2: The "One Task, One Context" Rule

When you delegate a task to the `coder` agent, you aren't just sending a prompt. You are deploying a specialist into an isolated environment.

**The Tactical Advantage:**
1. **Zero Interference**: The `coder` isn't distracted by the 500 messages you exchanged about the branding yesterday.
2. **Fresh Logic**: It starts with a clean slate, reducing the risk of "Old Context" poisoning new code.
3. **Speed**: Focused contexts process faster and with higher accuracy.

**Rule of Thumb:** If the `coder's` implementation requires more than 300 lines of code, the task is too large. Split the mission.

---

## How It Works: The Complete Workflow Cycle

The orchestrator pattern follows a simple loop:

```
1. PLAN → Create detailed task list
2. DELEGATE → Give one task to coder
3. IMPLEMENT → Coder builds it
4. TEST → Tester verifies it
5. EVALUATE → Pass, fail, or escalate
6. ITERATE → Mark complete, move to next task
```

Let's break down each step.

### Step 1: PLAN - Creating the Task List

When you start a project, the orchestrator's first job is to break it into discrete, actionable tasks.

**Bad task breakdown:**
```
[ ] Build the entire lead generation system
```

**Good task breakdown:**
```
[ ] Set up Python project with required dependencies
[ ] Create website scraper module with BeautifulSoup
[ ] Implement email validation function
[ ] Add company enrichment with Clearbit API
[ ] Build lead scoring algorithm
[ ] Create email template system
[ ] Implement SendGrid integration
[ ] Add CRM sync with HubSpot API
[ ] Create error handling and logging
[ ] Write tests for each module
```

Notice the difference? Each task is:
- **Specific**: Clear objective, no ambiguity
- **Testable**: You can verify when it's done
- **Independent**: Can be built in isolation
- **Sized Right**: Won't overwhelm a single agent's context

The orchestrator uses the `TodoWrite` tool to create this list immediately. This isn't optional - the todo list is the backbone of the entire process.

**Each task should include:**
- **Objective Statement**: What needs to be built
- **Input Specifications**: What data/files it receives
- **Process Steps**: How to implement it
- **Definition of Done**: Success criteria

For example:

```markdown
## Task: Create website scraper module

**Objective**: Build a Python module that scrapes contact information from target websites.

**Inputs**:
- List of URLs (array of strings)
- CSS selectors for name, email, phone fields

**Process**:
1. Create `scraper.py` in `/executions` directory
2. Use BeautifulSoup for HTML parsing
3. Use requests for HTTP calls
4. Implement retry logic for failed requests
5. Return structured JSON with extracted data

**Definition of Done**:
- Function accepts URL list and selectors
- Returns valid JSON with name, email, phone
- Handles 404/timeout errors gracefully
- Includes docstrings and type hints
```

This level of detail ensures the coder agent has everything needed to succeed.

### Step 2: DELEGATE - Assigning to the Coder

Once the task list is ready, the orchestrator takes the **first task** and delegates it to the coder agent.

**Critical rule**: One task at a time. Never delegate multiple tasks simultaneously.

Why? Because each subagent gets its own isolated context window. If you delegate three tasks at once, you've created three parallel conversations that can't coordinate with each other. That's chaos.

The orchestrator invokes the coder with:
- The specific task (copied from todo list)
- Any relevant context files
- Clear success criteria

The coder agent then:
- Reads the task requirements
- Implements the solution
- Returns completion details

**What happens in the coder's context:**
The coder has a fresh, clean context window focused entirely on this one task. It's not thinking about the email validation task or the CRM integration - just the web scraper. This focus is powerful.

If the coder encounters an error (dependency won't install, API throws unexpected response, unclear requirement), it immediately escalates to the stuck agent. No fallbacks, no workarounds, no guessing.

### Step 3: IMPLEMENT - The Coder Works

The coder agent follows a systematic approach:

**Read Phase:**
- Understand the task requirements
- Check for existing files that need modification
- Identify all files that need creation

**Write Phase:**
- Create new files or modify existing ones
- Follow best practices for the language/framework
- Add comments and documentation
- Include error handling

**Verify Phase:**
- Check that files were created successfully
- Verify syntax (if possible)
- Report back with implementation details

**Example coder output:**
```
Implementation complete for task: Create website scraper module

Files created:
- c:\Users\travi\project\executions\scraper.py (185 lines)

Key components:
- scrape_website(url, selectors) - Main scraping function
- validate_url(url) - URL validation helper
- retry_request(url, max_retries=3) - Retry logic
- extract_field(soup, selector) - Field extraction

Dependencies added:
- beautifulsoup4==4.12.2
- requests==2.31.0

Ready for testing.
```

Notice the detail? The coder tells you exactly what was built, where it is, and what's included. This makes the next step seamless.

### Step 4: TEST - The Tester Verifies

The orchestrator now takes the coder's completion report and passes it to the tester agent.

The tester's job is to verify the implementation meets the Definition of Done. For visual interfaces, it uses Playwright MCP to interact with the application and capture screenshots. For code modules, it runs unit tests or validation scripts.

**Example test delegation:**
```
Task to verify: Website scraper module

What was implemented:
- scraper.py with scrape_website() function
- Accepts URL list and CSS selectors
- Returns JSON with contact data

Definition of Done:
- Function accepts URL list and selectors
- Returns valid JSON with name, email, phone
- Handles 404/timeout errors gracefully
- Includes docstrings and type hints

Please verify each criterion.
```

The tester runs checks:
```python
# Test valid URL
result = scrape_website(
    "https://example.com/contact",
    {"name": ".contact-name", "email": ".contact-email"}
)
assert "name" in result
assert "email" in result

# Test 404 handling
result = scrape_website("https://example.com/nonexistent", {})
assert result["error"] == "404"

# Check docstrings
assert scraper.scrape_website.__doc__ is not None
```

**Tester output:**
```
Test Results: PASS

Verification complete for website scraper module.

✓ Function accepts URL list and selectors
✓ Returns valid JSON with name, email, phone fields
✓ Handles 404 errors gracefully (returns error object)
✓ Handles timeout errors (tested with 1s timeout)
✓ Includes comprehensive docstrings
✓ Type hints present on all functions

Screenshots: (if applicable)
- test-results-scraper.png

All Definition of Done criteria met. Ready to mark complete.
```

### Step 5: EVALUATE - Handling Results

The orchestrator now has test results and must decide how to proceed:

**Scenario 1: Tests Pass**
- Mark the task complete in todo list
- Move to next task
- Delegate next task to coder

**Scenario 2: Tests Fail**
- Invoke stuck agent with failure details
- Wait for human decision
- Either fix and re-test, or adjust requirements

**Scenario 3: Coder Hit Error During Implementation**
- Coder already escalated to stuck agent
- Human decides how to proceed
- May need to split task, adjust requirements, or fix environment issue

**Example of test failure escalation:**
```
Test Results: FAIL

The scraper module fails when handling JavaScript-rendered pages.

Expected: Extract contact info from all pages
Actual: Returns empty results for JS-rendered pages

Root cause: BeautifulSoup only parses static HTML

Escalating to stuck agent for decision:
- Option A: Add Selenium for JS rendering (adds complexity)
- Option B: Document limitation (only static HTML)
- Option C: Use different scraping approach (Playwright)

Awaiting human decision.
```

The stuck agent then asks the human (you) which approach to take. No guessing, no fallbacks.

### Step 6: ITERATE - Moving Forward

Once a task is verified complete, the orchestrator:
1. Updates the todo list (mark task done)
2. Takes the next task from the list
3. Delegates it to the coder
4. Repeats the cycle

This continues until every task on the list is complete.

**The power of this approach:**
- Clear progress tracking (you can see exactly where you are)
- Easy recovery (if something breaks, you know which task failed)
- Parallel debugging (fix one task without affecting others)
- Incremental delivery (working features accumulate)

---

## The Iteration Loop: Each Cycle Improves the System

One of the most powerful aspects of the orchestrator pattern is **self-annealing** - the system learns from mistakes and updates its directives.

**How self-annealing works:**

1. **Error occurs**: Coder or tester hits an unexpected issue
2. **Diagnosis**: Stuck agent analyzes what went wrong
3. **Fix**: The execution (code) is corrected
4. **Learning**: The directive (markdown instructions) is updated with the lesson

**Example scenario:**

**First run:**
```
Task: Scrape website contact information

Directive says: "Use BeautifulSoup to parse HTML"
Execution: scraper.py with BeautifulSoup

Error: Fails on JavaScript-rendered pages
```

**After self-annealing:**
```
Directive updated to say:
"Use BeautifulSoup for static HTML. For JavaScript-rendered
pages, check if content loads without JS first. If not,
escalate to stuck agent for Playwright decision."

Next time this task runs, the directive prevents the same error.
```

The system gets battle-hardened with every run. The directives become more robust, edge cases get documented, and future iterations run smoother.

**Where learnings go:**
- Update task description in todo template
- Add edge case to directive file
- Document in "Lessons Learned" section
- Include in handoff documentation

This is why DOE workflows improve over time - they're designed to capture institutional knowledge.

---

## Task Splitting: Smaller Tasks = Better Results

One of the most common mistakes in orchestration is creating tasks that are too large.

**What happens when tasks are too big:**
- Coder's context window fills up
- Implementation becomes complex and error-prone
- Testing becomes difficult (too many things to verify)
- Recovery is hard (if it fails, you lose a lot of work)

**Guidelines for task sizing:**

**Too Large:**
```
[ ] Build complete CRM integration with contact sync,
    deal tracking, email logging, and custom fields
```

**Just Right:**
```
[ ] Set up HubSpot API authentication
[ ] Create contact sync function (one-way: our DB → HubSpot)
[ ] Add deal creation function
[ ] Implement email activity logging
[ ] Add custom field mapping
[ ] Create two-way contact sync
```

**Rule of thumb**: If the coder's response would be more than 30,000 tokens (roughly 20,000 words or 500 lines of code), split the task.

**Signs a task is too large:**
- Multiple API integrations in one task
- "Create data layer with 50+ items"
- "Build all components for feature X"
- "Implement end-to-end workflow"

**How to split large tasks:**

**Strategy 1: By Component**
```
Instead of: "Build user dashboard"
Split into:
- Create dashboard layout component
- Add user profile widget
- Add activity feed widget
- Add analytics charts widget
```

**Strategy 2: By Data Volume**
```
Instead of: "Create 50 email templates"
Split into:
- Create email template system (structure)
- Add first 15 templates (welcome, onboarding, etc.)
- Add next 15 templates (engagement, nurture, etc.)
- Add final 20 templates (sales, support, etc.)
```

**Strategy 3: By Complexity Layer**
```
Instead of: "Build payment processing"
Split into:
- Set up Stripe API connection
- Create payment form component
- Add payment processing function
- Implement webhook handlers
- Add error handling and retries
```

The orchestrator should review tasks before delegating and split any that seem too large.

---

## Real Example: Building a Complete Workflow from Scratch

Let's walk through a real orchestration session building a content publishing workflow.

**User request:**
"Build a system that takes blog post ideas, generates drafts with AI, gets approval, and publishes to WordPress."

### Phase 1: Orchestrator Creates Task List

```markdown
## Content Publishing Workflow - Task List

[ ] Set up Python project structure with required dependencies
[ ] Create OpenAI integration module for content generation
[ ] Build draft generation function (idea → full post)
[ ] Create WordPress API connection module
[ ] Implement post publishing function
[ ] Add approval workflow (save draft for review)
[ ] Create CLI interface for running workflow
[ ] Add error handling and logging
[ ] Write tests for each module
[ ] Create example usage documentation
```

10 tasks, each specific and testable.

### Phase 2: First Task - Project Setup

**Orchestrator delegates to coder:**
```
Task: Set up Python project structure with required dependencies

Objective: Create foundational project structure for content workflow

Inputs: None (new project)

Process:
1. Create /executions/content-workflow directory
2. Create requirements.txt with openai, python-wordpress-xmlrpc, click
3. Create main.py entry point
4. Create config.py for API credentials
5. Create .env.example template

Definition of Done:
- Directory structure exists
- requirements.txt has all dependencies
- .env.example includes OPENAI_API_KEY, WP_URL, WP_USERNAME, WP_PASSWORD
- Project can be set up with "pip install -r requirements.txt"
```

**Coder implements:**
Creates files, sets up structure, reports completion.

**Orchestrator delegates to tester:**
```
Verify: Project setup

Check:
- Directory exists at correct path
- requirements.txt has correct packages
- .env.example has all required variables
- pip install runs without errors
```

**Tester verifies:**
```
✓ All checks pass
Ready to mark complete
```

**Orchestrator marks task complete, moves to next.**

### Phase 3: Second Task - OpenAI Integration

**Orchestrator delegates to coder:**
```
Task: Create OpenAI integration module for content generation

Objective: Build module that connects to OpenAI API

Inputs: API key from environment variable

Process:
1. Create openai_client.py in executions/content-workflow
2. Import openai library
3. Create get_client() function that returns authenticated client
4. Add generate_text(prompt, model="gpt-4") helper function
5. Include error handling for API failures

Definition of Done:
- Module imports successfully
- get_client() returns working OpenAI client
- generate_text() accepts prompt and returns response
- API errors raise clear exceptions
- Includes docstrings and type hints
```

**Coder implements, tester verifies, task marked complete.**

### Phase 4: Third Task - Draft Generation

**Orchestrator delegates to coder:**
```
Task: Build draft generation function (idea → full post)

Objective: Create function that takes blog idea and generates complete draft

Inputs:
- blog_idea (string): Topic or title for blog post
- target_length (int, default=1000): Approximate word count

Process:
1. Create content_generator.py
2. Import openai_client module
3. Create generate_draft(idea, length) function
4. Use system prompt for blog writing style
5. Return dict with title, content, meta_description

Definition of Done:
- Function accepts idea string and optional length
- Returns dict with title, content, meta_description keys
- Content is well-formatted markdown
- Average length matches target (±20%)
- Handles API errors gracefully
```

**Coder implements:**
```python
# executions/content-workflow/content_generator.py

from openai_client import generate_text

def generate_draft(idea: str, target_length: int = 1000) -> dict:
    """Generate blog post draft from idea.

    Args:
        idea: Topic or title for blog post
        target_length: Target word count (approximate)

    Returns:
        Dict with keys: title, content, meta_description
    """
    prompt = f"""
    Write a complete blog post about: {idea}

    Target length: {target_length} words

    Format as JSON with keys:
    - title: Compelling blog post title
    - content: Full post in markdown format
    - meta_description: SEO meta description (155 chars)
    """

    response = generate_text(prompt, model="gpt-4")
    # Parse JSON response
    # Return structured data
    ...
```

**Tester verifies:**
```python
# Test draft generation
result = generate_draft("AI automation for small businesses")

assert "title" in result
assert "content" in result
assert "meta_description" in result
assert len(result["meta_description"]) <= 160
assert 800 <= len(result["content"].split()) <= 1200  # ±20% of 1000
```

**All tests pass. Task marked complete.**

### Phase 5: Continue Through Remaining Tasks

The orchestrator continues this pattern:
- Delegate WordPress connection task
- Test it
- Delegate publishing function task
- Test it
- Delegate approval workflow task
- Test it

Each task builds on the previous ones, but is implemented and tested in isolation.

### Phase 6: Final Integration

**Last task: Create example usage documentation**

Shows how all the pieces fit together:

```python
# Example: Complete workflow

from content_generator import generate_draft
from wordpress_publisher import publish_post

# Generate draft
idea = "10 ways to automate your business with AI"
draft = generate_draft(idea, target_length=1500)

# Review draft (manual step)
print(f"Title: {draft['title']}")
print(f"Preview: {draft['content'][:200]}...")
approved = input("Approve? (y/n): ")

# Publish if approved
if approved == 'y':
    post_id = publish_post(
        title=draft['title'],
        content=draft['content'],
        status='publish'
    )
    print(f"Published: {post_id}")
```

**Tester verifies the complete workflow:**
```
Test: End-to-end workflow

Steps:
1. Generate draft for test idea
2. Save draft (status=draft)
3. Retrieve draft from WordPress
4. Verify content matches
5. Publish draft
6. Verify published post is live

Result: ✓ All steps pass
```

### Phase 7: Project Complete

**Orchestrator reports to user:**
```
Content Publishing Workflow - Complete

All 10 tasks implemented and tested:
✓ Project setup
✓ OpenAI integration
✓ Draft generation
✓ WordPress API connection
✓ Post publishing
✓ Approval workflow
✓ CLI interface
✓ Error handling
✓ Test suite
✓ Documentation

Files created:
- executions/content-workflow/main.py
- executions/content-workflow/openai_client.py
- executions/content-workflow/content_generator.py
- executions/content-workflow/wordpress_publisher.py
- executions/content-workflow/requirements.txt
- executions/content-workflow/README.md

Ready to use. Run: python main.py --idea "your blog topic"
```

Notice what happened here:
- 10 separate tasks, each focused and testable
- Each implemented in its own coder context
- Each verified in its own tester context
- Clear progress tracking throughout
- Working system at the end

**Total time**: Much faster than one massive conversation that might fail at step 7.

**Total reliability**: Each piece verified before moving on.

---

## Common Orchestration Patterns

As you build workflows, you'll notice recurring patterns.

### Pattern 1: Foundation → Features → Integration

```
Phase 1: Foundation
- Set up project
- Add dependencies
- Create configuration

Phase 2: Features (parallel-safe tasks)
- Build module A
- Build module B
- Build module C

Phase 3: Integration
- Connect modules
- Add orchestration layer
- Create end-to-end tests
```

### Pattern 2: Data → Logic → Interface

```
Phase 1: Data Layer
- Define data models
- Create database schema
- Build data access functions

Phase 2: Business Logic
- Implement core algorithms
- Add validation rules
- Create service functions

Phase 3: Interface Layer
- Build API endpoints
- Create CLI interface
- Add web UI
```

### Pattern 3: External → Internal → Polish

```
Phase 1: External Integrations
- Set up API clients
- Test external connections
- Handle authentication

Phase 2: Internal Logic
- Build core functionality
- Add business rules
- Implement workflows

Phase 3: Polish
- Add error handling
- Improve logging
- Write documentation
```

Recognizing these patterns helps you create better task lists.

---

## Handling Edge Cases

### What if a task is unclear?

The coder will escalate to stuck agent:
```
Task unclear: "Add user management"

Questions:
- What user properties are needed?
- Should we use database or API?
- What authentication method?
- What permissions/roles exist?

Escalating to stuck agent for clarification.
```

The human (you) clarifies, the orchestrator updates the task, re-delegates.

### What if requirements change mid-project?

The orchestrator updates the todo list:
```
Original task list:
[ ] Task 1 ✓
[ ] Task 2 ✓
[ ] Task 3 ← Currently here
[ ] Task 4
[ ] Task 5

User: "Actually, we need to add email notifications"

Updated task list:
[ ] Task 1 ✓
[ ] Task 2 ✓
[ ] Task 3 ← Currently here
[ ] Task 4
[ ] Task 3.5 - Add email notification module (NEW)
[ ] Task 4.5 - Integrate notifications into workflow (NEW)
[ ] Task 5
```

Insert tasks where they make sense, continue from where you are.

### What if testing reveals fundamental issue?

The tester escalates:
```
Test FAIL: Architecture problem

The scraper module can't handle async operations,
but the workflow requires concurrent scraping.

This isn't a bug - it's an architecture mismatch.

Options:
A) Refactor scraper to use async/await
B) Change workflow to sequential scraping
C) Use task queue (Celery) for concurrency

Escalating to stuck agent for decision.
```

The human decides, orchestrator potentially splits into sub-tasks, re-delegates.

### What if you need to restart?

The todo list is your checkpoint:
```
[ ] Task 1 ✓
[ ] Task 2 ✓
[ ] Task 3 ✓
[ ] Task 4 ← Restart from here
[ ] Task 5
[ ] Task 6
```

Simply pick up where you left off. Completed tasks stay completed.

---

## Best Practices for Orchestration

### 1. Start with a detailed todo list
Don't wing it. Spend time upfront creating a comprehensive task list. It saves hours later.

### 2. Make tasks independently testable
Each task should have clear success criteria that can be verified in isolation.

### 3. One task at a time
Never delegate multiple tasks simultaneously. Finish one completely (test and all) before moving to the next.

### 4. Use consistent task structure
Every task should have: Objective, Inputs, Process, Definition of Done.

### 5. Test everything
No exceptions. Every implementation gets verified by tester before marking complete.

### 6. Document learnings
When something unexpected happens, update the directive with the lesson learned.

### 7. Split liberally
When in doubt, split a task into smaller pieces. It's easier to combine later than to untangle.

### 8. Trust the escalation system
When stuck agent gets triggered, that's good - it means the system is working as designed.

---

## Try It Yourself: Build Your First Workflow

**Exercise**: Build a simple email summary workflow.

**Requirements:**
- Fetch emails from Gmail
- Summarize each email with AI
- Save summaries to a text file

**Your task**: Create the todo list for this workflow.

**Hint**: Break it into 6-8 tasks covering:
- Project setup
- Gmail API integration
- Email fetching function
- AI summarization module
- File writing function
- Main workflow orchestration
- Error handling
- Testing

**Once you have your task list:**
1. Review each task - is it specific enough?
2. Does each have clear success criteria?
3. Are any too large? (Would they exceed 500 lines of code?)
4. Are they in logical order?

**Then run it:**
1. Give your task list to the orchestrator
2. Watch it delegate to coder (one task at a time)
3. Observe tester verifying each implementation
4. See how the working system emerges piece by piece

**What you'll learn:**
- How to break down requirements
- How orchestrator manages state
- How coder focuses on single tasks
- How tester validates incrementally
- How stuck agent handles issues

---

## The Mental Model Shift

Traditional programming: Write everything, debug everything, test at end.

```
Write 1000 lines → Debug → Test → (Fail) → Debug more → Test again
```

Orchestrator pattern: Build incrementally, test continuously, validate constantly.

```
Task 1 (50 lines) → Test → ✓
Task 2 (75 lines) → Test → ✓
Task 3 (100 lines) → Test → ✓
...
Complete system → Already tested → ✓
```

**The difference:**
- Failures are caught early (after 50 lines, not 1000)
- Progress is visible (checklist filling up)
- Recovery is easy (redo one task, not entire project)
- Quality is built in (everything tested before moving on)

**This is the power of orchestration.**

---

## Key Takeaway

The orchestrator pattern transforms how you build complex systems with AI:

**Instead of:** One massive conversation that might fail late
**You get:** Incremental progress with continuous validation

**Instead of:** Tangled context and unclear state
**You get:** Clean separation and perfect memory

**Instead of:** Starting over when things break
**You get:** Precise recovery from exactly where it failed

**The secret:** Don't try to do everything at once. Create a plan, delegate one task at a time, test everything, and iterate.

Your orchestrator (Antigravity IDE with 200k context) remembers everything.

Your specialists (coder, tester) get fresh context for focused work.

Your safety net (stuck agent) ensures nothing falls through the cracks.

Together, they build complex systems reliably - one verified task at a time.

**Next chapter, we'll explore Phase 4: Testing & Self-Annealing** - how the system learns from mistakes and gets stronger with every run.

---

**Word count:** ~5,200 words
**Status:** Complete Draft
**Filename:** `c:\Users\travi\claude-agent-system\ebook\chapters\part-04-the-five-phases\ch08-training-your-ai-team.md`

So Tom did what most business owners do: he hired a developer.

Six weeks and $12,000 later, the developer delivered a Python script. Tom was excited. He followed the installation instructions, ran the script, and watched it crash immediately with an error message he couldn't understand. He emailed the developer. "I'm swamped with other projects," came the reply. "I'll try to look at it next month."

Tom gave up. The script sat unused in a folder. The manual process continued.

Six months later, Tom discovered Antigravity.

He spent two hours on a Saturday morning writing a directive in plain English—no code, just clear instructions about what he needed. He handed it to the AI orchestrator and went to make coffee. When he returned an hour later, he had a working system. The orchestrator had broken his goal into 14 tasks, delegated them to specialist agents, tested each implementation, and delivered a complete lead enrichment pipeline.

Total cost: $0.87 in API credits.

But here's what really amazed Tom: when the system hit an error during execution (a website selector had changed), it didn't crash. It reasoned about the problem, tried a different approach, verified the fix, and kept going. The developer Tom had paid never did that.

The difference wasn't the technology. The difference was the orchestration pattern.

This chapter shows you how to do what Tom did—how to go from "hoping a developer understands my vision" to "managing an AI team that iterates until it's right."

## Your Role: Manager, Not Programmer

Let's get one thing clear immediately: you are not here to write code.

Phase 3 is where the magic happens—your workshop is set up (Phase 1), your playbook is written (Phase 2), and now it's time to run the workflow. But in traditional automation, "running" means executing a script and hoping it works. In Antigravity, "running" means **managing a team of AI specialists through an iterative build process**.

This is a fundamental mindset shift:

**Traditional Automation:**
- You write code (or pay someone to write it)
- You debug when it breaks (or pay someone to debug it)
- You hope it works on the first try
- You're stuck if you don't understand the error

**Antigravity Automation:**
- You set the goal in plain English
- You review the work (screenshots, outputs, results)
- You provide feedback when something's off
- You never see the code unless you want to

### What "Management" Means Here

Think of yourself as the general contractor on a construction project. You don't swing the hammer, pour the concrete, or wire the electrical. But you absolutely check that the walls are straight, the foundation is level, and the plumbing doesn't leak. When something's wrong, you don't fix it yourself—you tell the specialists what needs to change, and they handle the technical execution.

In Antigravity, that looks like this:

**You set the goal:**
"Extract all practitioner names, phone numbers, and email addresses from this medical directory website. Save them to a CSV file formatted for HubSpot import."

**You review the work:**
The Tester agent takes a screenshot showing the first 10 extracted records. You look at the output and notice the phone numbers are inconsistent—some have dashes, some have parentheses, some are just digits.

**You provide feedback:**
"The phone numbers need consistent formatting. Use the format (XXX) XXX-XXXX for all numbers."

**You DON'T:**
- Write a regular expression to parse phone numbers
- Debug why the scraper is grabbing different formats
- Configure the CSV export library
- Deal with Python dependency conflicts

That's what the specialists do.

### Real Example: Sarah's Email Campaign

Sarah runs a real estate investment company. She wanted to automate her weekly email campaign to property owners in foreclosure. Here's how her "management" worked in Phase 3:

**Cycle 1 Review:**
The Tester showed her a screenshot of the first draft email. Sarah noticed the subject line was generic: "Regarding Your Property."

**Sarah's feedback:**
"Make the subject line more personal. Include the actual property address so they know this isn't spam."

**What happened next:**
The Coder agent updated the email template to pull the address from the data and insert it into the subject line. The Tester verified the new version. Done. Sarah never touched the code.

**Cycle 2 Review:**
Sarah reviewed a sample batch of 10 emails. She noticed the system was sending emails to properties that had already sold (they were still in the foreclosure database but no longer relevant).

**Sarah's feedback:**
"Before sending each email, check if the property status is still 'Active' in the database. Skip any that show 'Sold' or 'Withdrawn.'"

**What happened next:**
The Coder added a status check to the workflow logic. The Tester ran a batch of 50 records and confirmed that 7 were correctly skipped. Sarah approved. Done.

**Total time Sarah spent:** 20 minutes reviewing screenshots and providing feedback.

**Total time the system spent:** 90 minutes building, testing, and iterating.

**Result:** A working email campaign system that runs every Monday morning, processes 200+ leads, and sends personalized outreach only to active properties.

This is what management looks like in Phase 3. You provide direction. You review results. You give feedback in plain English. The AI team handles everything technical.

## The Orchestrator Pattern Explained

When you hand a directive to the orchestrator, it doesn't just start executing blindly. It follows a proven four-step pattern that ensures quality, handles errors gracefully, and produces reliable results.

### Step 1: Plan (TodoWrite)

The moment you provide a directive, the orchestrator reads it carefully and thinks: "What are all the individual tasks required to accomplish this goal?"

It then creates a detailed todo list—typically 5 to 15 tasks, each small enough to complete independently and specific enough to test clearly.

**Example:** You provide a directive to "Build a lead scraper that extracts practitioner information from a medical directory and saves it to a CSV file."

The orchestrator breaks this into a todo list:

```
Todo List: Medical Directory Scraper
[ ] Task 1: Set up Python environment with required libraries (requests, beautifulsoup4, pandas)
[ ] Task 2: Navigate to the target directory URL and verify the page loads correctly
[ ] Task 3: Locate and extract all practitioner names from the directory listing
[ ] Task 4: Extract phone numbers for each practitioner
[ ] Task 5: Extract email addresses (if available)
[ ] Task 6: Format phone numbers consistently using (XXX) XXX-XXXX pattern
[ ] Task 7: Validate that email addresses follow proper format
[ ] Task 8: Create pandas DataFrame with columns: name, phone, email
[ ] Task 9: Save DataFrame to CSV file with proper encoding
[ ] Task 10: Test with first 10 records and verify output format
[ ] Task 11: Run full scrape of all directory pages
[ ] Task 12: Take screenshot showing sample of final CSV output
```

Notice what just happened: a single high-level goal became 12 concrete, testable tasks. Each one builds on the previous one. Each has a clear success condition. This is why Antigravity works when giant monolithic prompts fail.

Why does task splitting matter so much? Because each task gets processed in a fresh context window. The Coder agent focuses entirely on Task 1, completes it, and hands it back. Then a fresh Coder instance focuses entirely on Task 2. No context pollution. No accumulated confusion. Just clean, focused execution.

### Step 2: Delegate (Coder Agent)

With the plan created, the orchestrator invokes the Coder agent and hands it Task 1: "Set up Python environment with required libraries (requests, beautifulsoup4, pandas)."

The Coder agent works in its own context window. It doesn't see the full project history. It doesn't get overwhelmed by the big picture. It sees one task, the directive that defines the overall goal, and its job: complete this specific task.

The Coder:
1. Reads the task requirements
2. Writes the necessary code
3. Executes it (installs the libraries)
4. Reports back to the orchestrator: "Task 1 complete. Libraries installed successfully."

The orchestrator updates the todo list:
```
[✓] Task 1: Set up Python environment with required libraries
[ ] Task 2: Navigate to target directory URL and verify page loads
```

### Step 3: Verify (Tester Agent)

Here's where Antigravity diverges sharply from traditional automation: we don't trust that code works just because it ran without errors. We verify.

The orchestrator invokes the Tester agent and says: "The Coder just completed Task 1—setting up the Python environment. Please verify that the required libraries are actually installed and can be imported."

The Tester agent:
1. Attempts to import each library (requests, beautifulsoup4, pandas)
2. Captures the result (success or error)
3. Takes a screenshot if visual confirmation is needed
4. Reports back: "PASS - All three libraries imported successfully" or "FAIL - beautifulsoup4 failed to import with error: ModuleNotFoundError"

If the test passes, the orchestrator marks Task 1 as verified and moves to Task 2.

If the test fails, we move to Step 4.

### Step 4: Iterate

When a test fails, the orchestrator doesn't panic. It doesn't escalate to a human immediately. It enters the reasoning loop.

The orchestrator hands the failure report back to the Coder and says: "The Tester reports that beautifulsoup4 failed to import. Please analyze the error and try a different approach."

The Coder:
1. Reads the error message
2. Looks at what it tried before
3. Forms a hypothesis about what went wrong (maybe wrong package name? maybe needs beautifulsoup4 instead of beautifulsoup?)
4. Tries a different installation approach
5. Reports back: "I installed 'beautifulsoup4' explicitly. Ready for testing."

The Tester verifies again. If it passes, we move forward. If it fails again, the Coder tries yet another approach.

**When does the Stuck agent get involved?**

After three failed attempts on the same task, the orchestrator invokes the Stuck agent, which escalates to you (the human). At this point, it's usually because:
- The directive is ambiguous (needs clarification)
- There's a business decision needed ("Should we skip records with missing emails or mark them as 'No Email'?")
- There's an access issue (API credentials needed, website blocked, etc.)

You provide the missing information, and the team continues.

This four-step loop—Plan, Delegate, Verify, Iterate—runs continuously until every task on the todo list is complete and verified. That's Phase 3 execution.

## Task Splitting: The Secret to Success

Let's talk about the single biggest mistake people make in Phase 3.

They write a directive like this:

"Build me a complete CRM system with contact management, email integration, deal tracking, calendar sync, reporting dashboard, and HubSpot integration."

They hand it to the orchestrator and wonder why it fails spectacularly—hallucinated features, half-finished implementations, code that doesn't run, context windows that overflow.

The problem isn't the AI. The problem is the task size.

Imagine hiring a junior developer and saying: "Build me a complete CRM by Friday." You'd never do that, because you know it's an impossible ask. You'd break it into phases—first the database schema, then the authentication system, then the contact form, and so on.

AI agents need the same structure.

### The Common Mistake

**BAD (single giant task):**
"Build a system that scrapes LinkedIn profiles, enriches them with company data from Clearbit, scores them based on job title relevance, and automatically adds qualified leads to our HubSpot CRM."

Why this fails:
- Too many unknowns (LinkedIn structure, Clearbit API, HubSpot integration)
- No clear verification point (when is it "done"?)
- High chance of compounding errors (if scraping fails, everything after fails)
- Agents run out of context trying to track everything

### The Antigravity Approach

**GOOD (broken into 12 testable tasks):**

1. Navigate to a sample LinkedIn profile URL and verify the page loads
2. Extract name, current title, and company name from the profile
3. Take a screenshot showing the extracted data overlaid on the profile
4. Test Clearbit API connection with a sample company name
5. Enrich one sample company using Clearbit API
6. Combine LinkedIn data with Clearbit enrichment for one profile
7. Define scoring logic (title keywords, company size thresholds)
8. Calculate relevance score for one sample profile
9. Test HubSpot API connection (create/read a test contact)
10. Format one enriched profile for HubSpot API requirements
11. Add one test profile to HubSpot and verify it appears correctly
12. Process a batch of 10 profiles end-to-end

Each task:
- Takes 5-15 minutes to complete
- Has clear success criteria ("screenshot shows name and title" or "test contact appears in HubSpot")
- Can be verified independently
- Builds on the previous task

**Why this works:**

**Early error detection:** If LinkedIn's profile structure is wrong, you find out in Task 2, not after you've built the entire pipeline.

**Visible progress:** You can see Task 4/12 complete and know you're a third of the way done.

**Easy debugging:** When something fails, you know exactly which component is broken.

**Pause and resume:** You can stop after Task 6, review the enriched data format, provide feedback, and continue.

**Fresh context:** Each task gets a clean slate—the Coder doesn't carry forward accumulated confusion.

### Real Example: The 50-Item Data Task

A client once asked their orchestrator to "Create a data file with 50 AI prompt examples for different business scenarios."

The orchestrator delegated this as a single task to the Coder. The Coder generated all 50 prompts in one massive output. The result: 30,000 tokens consumed, context window nearly full, last 15 prompts were repetitive and low-quality, no way to review incrementally.

After learning about task splitting, they revised the directive:

**Task 1:** Create data structure and first 10 business prompts (sales scenarios)
**Task 2:** Create next 10 prompts (marketing scenarios)
**Task 3:** Create next 10 prompts (customer service scenarios)
**Task 4:** Create next 10 prompts (operations scenarios)
**Task 5:** Create final 10 prompts (leadership scenarios)

Each task took 5 minutes. The client reviewed the first 10, gave feedback ("make them more specific to B2B SaaS companies"), and the Coder adjusted the style for Tasks 2-5. Final result: 50 high-quality, consistent prompts, reviewed incrementally, with no context overflow.

**The lesson:** If a task involves creating many items (data records, UI components, workflow steps), split it into batches of 10-15.

## The Reasoning Loop: How Agents Learn

One of the most powerful aspects of Phase 3 is what happens when things go wrong.

Traditional scripts fail silently or crash with cryptic errors. Antigravity agents **reason about failures** and try alternative approaches.

### What Happens When Coder Hits an Error

Let's walk through a real scenario:

**Task:** "Extract all practitioner names from the directory page."

**Attempt 1:**
The Coder writes code that looks for elements with the CSS class `.name` and extracts their text content. It finds zero results.

The Tester reports: "FAIL - Expected at least 50 names, found 0."

**The Reasoning Loop Begins:**

The Coder doesn't just report failure and move on. It:

1. **Reads the error:** "Found 0 results when expecting 50+"
2. **Reviews its approach:** "I used CSS selector `.name`"
3. **Forms a hypothesis:** "The selector might be wrong. Let me inspect the actual page structure."
4. **Investigates:** The Coder loads the page, examines the HTML, and discovers the names are actually in `<h3>` tags inside `.practitioner-card` containers
5. **Tries a new approach:** Updates selector to `.practitioner-card h3`
6. **Tests again:** Tester finds 218 names → PASS

**What just happened?**

The Coder didn't blindly retry the same approach. It analyzed the failure, investigated the root cause, formed a hypothesis, and implemented a fix. This is what we mean by "training the AI team."

### Types of Errors Agents Handle

**Syntax errors (easy):**
- Missing brackets, typos, incorrect function names
- Coder catches these immediately and fixes them

**Logic errors (medium):**
- Wrong calculation (dividing instead of multiplying)
- Incorrect conditional (checking `>=` instead of `>`)
- Coder reviews the directive's requirements and corrects the logic

**External errors (hard):**
- API rate limit hit (Coder adds delay between requests)
- Website structure changed (Coder re-examines HTML and updates selectors)
- Authentication failed (Coder checks credentials format, may need human help)

**Data errors (tricky):**
- Unexpected format (dates in European vs American format)
- Missing fields (some records lack email addresses)
- Inconsistent structure (some pages have different layouts)

The Coder handles most of these autonomously. But when should it ask for help?

### When to Invoke the Stuck Agent

The system invokes the Stuck agent (which escalates to you) when:

**1. Same error 3+ times**
The Coder is stuck in a loop, trying the same approaches repeatedly. This usually means the directive is ambiguous or missing critical information.

*Example:* Task fails three times trying to "identify active customers." What does "active" mean? Logged in this month? Made a purchase this quarter? You need to clarify.

**2. Business decision needed**
The implementation has hit a fork in the road, and the "right" answer depends on your business rules.

*Example:* "Found 15 records with missing phone numbers. Should I (A) skip them, (B) include them with 'No Phone' placeholder, or (C) try to find phone numbers from an alternate source?"

**3. Ambiguous requirement**
The directive says "qualify leads" but doesn't define what makes a lead qualified.

*Example:* "The directive says to score leads, but doesn't specify the scoring criteria. Should we score based on company size, industry match, job title, or a combination?"

**4. Access issue**
The Coder needs credentials, permissions, or resources it doesn't have.

*Example:* "Cannot connect to the Google Sheets API. Please provide a service account key or grant OAuth permissions."

**5. Technical limitation**
The Coder has hit a hard technical constraint.

*Example:* "The target website uses JavaScript rendering and requires browser automation. Current script uses simple HTTP requests. Should we switch to Playwright?"

When the Stuck agent is invoked, it presents you with the problem, the context (what the Coder has already tried), and usually 2-3 options. You pick one, provide clarification, and the team continues.

**Important:** The Stuck agent prevents the system from hallucinating or using fallback assumptions. It ensures you stay in control of business logic decisions while letting the AI handle technical execution.

## Complete Real Walkthrough: Building a Lead Enrichment System

Let's walk through a complete Phase 3 build from start to finish—the kind of project you might tackle in your first week with Antigravity.

### The Business Problem

Jessica runs a real estate investment company specializing in single-family home acquisitions. Her company gets 50-70 leads per week from Facebook ads—homeowners interested in selling quickly.

Currently, her admin (making $25/hour) spends 15-20 minutes per lead doing this:

1. Copies lead info (name, email, phone, property address) from Facebook Ads Manager into Google Sheets
2. Googles the property address to verify it exists
3. Looks up property details on Zillow (beds, baths, year built, estimated value)
4. Checks if property type matches their criteria (single-family homes only, 3+ bedrooms, built after 1990)
5. Scores the lead (A/B/C tier based on criteria match)
6. Drafts a personalized email referencing specific property features
7. Logs the qualified lead in their CRM

**Time cost:** 15 minutes × 60 leads = 15 hours per week = $375/week = $19,500/year

**Error rate:** Manual Zillow lookup sometimes captures wrong property (similar addresses). Email personalization is inconsistent (depends on how tired the admin is).

Jessica wants to automate 90% of this, leaving only edge cases (weird properties, missing data) for human review.

### The Goal

Build a system that:
- Reads leads from a CSV export
- Validates property addresses
- Enriches with property data
- Scores leads based on defined criteria
- Generates personalized email drafts
- Outputs enriched CSV ready for CRM import

**Target:** 90% automation rate, under 2 hours of build time, under $5 in API costs.

### The Directive

Jessica writes this directive (using the template from Chapter 7):

```markdown
# Lead Enrichment Workflow

**Objective:** Automatically qualify and enrich real estate leads from Facebook ads

**Inputs:**
- CSV file with columns: name, email, phone, property_address
- Located at: ./data/weekly_leads.csv
- Target criteria: single-family homes, 3+ bedrooms, built after 1990

**Process:**
1. Read CSV file and load all lead records
2. For each lead:
   - Validate the property address using Google Maps Geocoding API
   - Look up property details using real estate data API (beds, baths, year built, type)
   - Score lead A/B/C based on criteria:
     - A tier: Meets all criteria (single-family, 3+ beds, built after 1990)
     - B tier: Meets 2 of 3 criteria
     - C tier: Meets 0-1 criteria
   - Generate personalized email draft mentioning specific property features
   - Append enriched data to output record
3. Save results to ./output/enriched_leads.csv with columns:
   name, email, phone, address, beds, baths, year_built, property_type, score, draft_email

**Definition of Done:**
- All leads from input CSV are processed
- Output CSV contains all required columns with accurate data
- Screenshot showing 3 sample enriched records with draft emails
- Error log listing any addresses that couldn't be validated (for manual review)
```

### The Orchestrator's Todo List

Jessica hands this directive to the orchestrator. Within 30 seconds, the orchestrator creates this plan:

```
Todo List: Lead Enrichment System
[ ] Task 1: Set up Python environment with required libraries (pandas, googlemaps, anthropic)
[ ] Task 2: Read CSV file and verify it loads correctly
[ ] Task 3: Validate first property address using Google Maps API
[ ] Task 4: Look up property details for first address using real estate API
[ ] Task 5: Implement lead scoring logic
[ ] Task 6: Generate personalized email for one sample lead
[ ] Task 7: Build complete enrichment pipeline for single record
[ ] Task 8: Add error handling for invalid addresses
[ ] Task 9: Add error handling for missing property data
[ ] Task 10: Process batch of 5 test leads
[ ] Task 11: Review test output and refine email templates
[ ] Task 12: Process full CSV of 53 leads
[ ] Task 13: Generate error log for manual review items
[ ] Task 14: Take screenshot of sample output showing 3 enriched leads
```

Now let's watch Phase 3 execution cycle by cycle.

### Cycle 1: Set Up Environment

**Orchestrator → Coder:** "Complete Task 1: Set up Python environment with required libraries (pandas, googlemaps, anthropic)"

**Coder:** Writes a script that installs the three libraries via pip.

**Orchestrator → Tester:** "Verify that pandas, googlemaps, and anthropic can all be imported without errors."

**Tester:** Runs test imports. All succeed.

**Result:** PASS ✓

**Time:** 2 minutes

**Todo list updated:**
```
[✓] Task 1: Set up Python environment
[ ] Task 2: Read CSV file
```

### Cycle 2: Read CSV File

**Orchestrator → Coder:** "Complete Task 2: Read CSV file at ./data/weekly_leads.csv and verify it loads correctly"

**Coder:** Writes pandas script to load CSV, displays first 5 rows and row count.

**Orchestrator → Tester:** "Verify the CSV loaded successfully and contains expected columns: name, email, phone, property_address"

**Tester:** Confirms file loaded, shows 53 rows, all expected columns present, displays sample:
```
   name              email               phone          property_address
0  Sarah Johnson    sarah@email.com     555-0123       847 Maple Ave, Columbus, OH
1  Mike Peterson    mike@email.com      555-0456       1205 Oak Street, Columbus, OH
...
```

**Result:** PASS ✓

**Time:** 3 minutes

### Cycle 3: Validate First Address

**Orchestrator → Coder:** "Complete Task 3: Validate first property address using Google Maps Geocoding API"

**Coder:** Attempts to call Google Maps API with the first address.

**Orchestrator → Tester:** "Verify the API returns valid coordinates for the first address"

**Tester:** API call succeeds, returns: `{ lat: 39.9612, lng: -82.9988, formatted_address: "847 Maple Ave, Columbus, OH 43205, USA" }`

**Result:** PASS ✓

**Time:** 4 minutes

### Cycle 4: Look Up Property Details (with error)

**Orchestrator → Coder:** "Complete Task 4: Look up property details for first address using real estate API"

**Coder (Attempt 1):** Calls real estate data API endpoint: `/api/property?address=847 Maple Ave, Columbus, OH`

**Orchestrator → Tester:** "Verify the API returns property details including beds, baths, year built, and property type"

**Tester:** API returns 404 error: "Property not found"

**Result:** FAIL ✗

**Reasoning loop activated:**

**Orchestrator → Coder:** "The API returned 404. Please analyze the error and try a different approach."

**Coder (Reasoning):**
- "The endpoint might require a different address format"
- "Let me check the API documentation"
- "Documentation shows the endpoint expects latitude/longitude, not street address"

**Coder (Attempt 2):** Updates call to use lat/lng from previous step: `/api/property?lat=39.9612&lng=-82.9988`

**Orchestrator → Tester:** "Verify again"

**Tester:** API returns:
```json
{
  "beds": 4,
  "baths": 2.5,
  "year_built": 2005,
  "property_type": "Single Family",
  "sqft": 2100
}
```

**Result:** PASS ✓

**Time:** 8 minutes (including one failure + reasoning)

**What just happened:** The Coder hit an error, analyzed it, consulted documentation, formed a hypothesis (needs lat/lng not address), tried a new approach, and succeeded. No human intervention needed.

### Cycle 5: Implement Scoring Logic

**Orchestrator → Coder:** "Complete Task 5: Implement lead scoring logic based on criteria"

**Coder:** Writes scoring function:
```python
def score_lead(property_data):
    score = 0
    if property_data['property_type'] == 'Single Family':
        score += 1
    if property_data['beds'] >= 3:
        score += 1
    if property_data['year_built'] >= 1990:
        score += 1

    if score == 3:
        return 'A'
    elif score == 2:
        return 'B'
    else:
        return 'C'
```

**Orchestrator → Tester:** "Test scoring function with sample property: 4 beds, built 2005, Single Family. Should return 'A'."

**Tester:** Function returns 'A' ✓

**Orchestrator → Tester:** "Test with 2 beds, built 1975, Condo. Should return 'C'."

**Tester:** Function returns 'C' ✓

**Result:** PASS ✓

**Time:** 5 minutes

### Cycle 6: Generate Personalized Email (with human feedback)

**Orchestrator → Coder:** "Complete Task 6: Generate personalized email draft for one sample lead using property details"

**Coder:** Uses an advanced LLM API to generate email:

```
Subject: Regarding Your Property at 847 Maple Ave
Body: Hi Sarah, I saw you're interested in selling your property. We'd love to make you an offer. Let me know if you're available for a quick call this week.
```

**Orchestrator → Tester:** "Review email draft for personalization quality"

**Tester:** Shows email to orchestrator. Orchestrator flags: "Email is too generic—doesn't mention any specific property features."

**Result:** FAIL ✗

**Orchestrator → Stuck Agent:** "Email template needs to be more personalized. What specific property details should be mentioned?"

**Stuck → Jessica (human):** "The Coder generated a generic email. Should we include property features like bedrooms, year built, or square footage?"

**Jessica's response:** "Yes—mention the number of bedrooms and the year built. Make it clear we've done research on their specific property."

**Orchestrator → Coder:** "Update email template to include number of bedrooms and year built as proof of research."

**Coder (Attempt 2):** Regenerates email:

```
Subject: Offer for Your 4-Bedroom Home on Maple Ave
Body: Hi Sarah, We're interested in purchasing your beautiful 4-bedroom home built in 2005 at 847 Maple Ave. We specialize in quick, fair offers for quality properties like yours. Would you be open to a conversation this week about a no-obligation cash offer?
```

**Orchestrator → Tester:** "Verify email mentions specific property details"

**Tester:** Confirms email includes "4-bedroom" and "built in 2005" ✓

**Result:** PASS ✓

**Time:** 10 minutes (including human feedback loop)

### Cycles 7-11: Error Handling, Batch Processing, Refinement

The orchestrator continues through Tasks 7-11, implementing:

- Complete pipeline for single record (Task 7): 6 minutes → PASS
- Error handling for invalid addresses (Task 8): 5 minutes → PASS
- Error handling for missing property data (Task 9): 4 minutes → PASS
- Batch processing of 5 test leads (Task 10): 3 minutes → PASS
- Email template refinement after Jessica reviews samples (Task 11): 7 minutes → PASS

**Cumulative time:** 25 minutes

### Cycle 12: Full Production Run

**Orchestrator → Coder:** "Complete Task 12: Process full CSV of 53 leads"

**Coder:** Runs enrichment pipeline on all 53 records.

**Orchestrator → Tester:** "Verify all leads processed and output CSV created"

**Tester:** Reports:
- 53 leads processed
- 48 successfully enriched (A-tier: 22, B-tier: 18, C-tier: 8)
- 5 failed validation (addresses couldn't be geocoded—logged for manual review)
- Output file created: ./output/enriched_leads.csv

**Result:** PASS ✓

**Time:** 3 minutes

### Cycle 13-14: Final Deliverables

**Task 13:** Generate error log → 2 minutes → PASS
**Task 14:** Screenshot of sample output → 1 minute → PASS

### Final Results

**Total execution time:** 78 minutes
**Total API costs:** $0.87 (Google Maps: $0.05, Real Estate API: $0.27, Claude: $0.55)
**Human time invested (Jessica):** 10 minutes (reviewing emails, providing feedback)
**Tasks completed:** 14/14 ✓
**Success rate:** 91% (48 of 53 leads fully enriched)

**What Jessica got:**

A CSV file with 48 fully enriched leads ready for immediate outreach:
```csv
name,email,phone,address,beds,baths,year_built,property_type,score,draft_email
Sarah Johnson,sarah@email.com,555-0123,"847 Maple Ave, Columbus, OH",4,2.5,2005,Single Family,A,"Subject: Offer for Your 4-Bedroom Home on Maple Ave..."
Mike Peterson,mike@email.com,555-0456,"1205 Oak St, Columbus, OH",3,2,1998,Single Family,A,"Subject: Offer for Your 3-Bedroom Home on Oak Street..."
```

Plus an error log with 5 addresses to manually review.

**Return on investment:**
- **Before:** 15 hours/week @ $25/hour = $375/week = $19,500/year
- **After:** 30 minutes/week (uploading CSVs, reviewing error log) = $12.50/week = $650/year
- **Savings:** $18,850/year
- **Build cost:** $0.87
- **Payback period:** 2.5 minutes

But here's what really mattered to Jessica: consistency. Every lead got the same quality enrichment. Every email was personalized with accurate property details. No more "I was tired and just copy-pasted the template" emails. No more wrong properties looked up.

The system doesn't get tired. It doesn't cut corners. It follows the directive exactly, every single time.

## Common Challenges and Solutions

Even with the orchestrator pattern, you'll hit obstacles in Phase 3. Here's what to watch for and how to handle each one.

### Challenge 1: "The Coder Keeps Making the Same Mistake"

**Symptom:** Task fails three times with the same error. The Stuck agent escalates.

**Root cause:** Your directive has an ambiguity or contradiction.

**Example:** Directive says "extract all phone numbers" but the website has phone numbers in multiple formats (some with extensions, some international). The Coder keeps failing validation because "all" is impossible—some formats don't parse.

**Solution:** Update the directive with more specific instructions.

**Before:** "Extract all phone numbers"

**After:** "Extract phone numbers in format (XXX) XXX-XXXX. Skip any numbers with extensions or international prefixes. Log skipped numbers for manual review."

**Lesson:** When Coder fails repeatedly, it's usually a specification problem, not a code problem.

### Challenge 2: "The Tester Keeps Failing the Same Test"

**Symptom:** Coder implements Task X successfully (no errors), but Tester keeps marking it FAIL.

**Root cause:** Your success criteria in the Definition of Done are either unclear or unrealistically strict.

**Example:** Definition of Done says "extract ALL phone numbers from the page" but the page has some phone numbers hidden in image files (not extractable via HTML scraping). Tester fails because it found 87 of 92 numbers.

**Solution:** Adjust the Definition of Done to be realistic.

**Before:** "Extract ALL phone numbers (100%)"

**After:** "Extract phone numbers from HTML text fields (target: 90%+ of visible numbers)"

**Lesson:** Perfect is the enemy of done. Define success based on business value, not technical perfection.

### Challenge 3: "The Orchestrator Created Too Many Tasks"

**Symptom:** Your todo list has 40+ tasks. It feels overwhelming.

**Root cause:** Your directive is too detailed—you're micromanaging the implementation instead of defining the goal.

**Example:** Directive says:
1. Import pandas library
2. Use pandas.read_csv() function
3. Store result in variable called df
4. Print df.head() to verify
5. Check that column names match expected...

This is step-by-step coding instructions. The orchestrator thinks each line is a separate task.

**Solution:** Trust the agents. Provide goals, not implementation steps.

**Before:**
"Import pandas, use read_csv(), store in df variable, print head to verify..."

**After:**
"Read the CSV file and verify it contains the expected columns: name, email, phone."

Let the Coder decide how to accomplish that goal.

**Lesson:** Write directives like you're talking to a competent contractor, not a junior intern.

### Challenge 4: "I Want to Make a Change Mid-Execution"

**Symptom:** You're watching Phase 3 run and realize you want to change something (different output format, additional data field, etc.).

**Solution:** Let the current task complete, then update the directive.

**How it works:**
1. Wait for the active task to finish (usually 2-5 minutes)
2. Update the directive markdown file with your change
3. Tell the orchestrator: "I updated the directive—please adjust remaining tasks accordingly"
4. Orchestrator re-plans remaining tasks based on new requirements

**Example:** You're watching the lead enrichment system run (currently on Task 8 of 14) and realize you want to add property square footage to the output.

You update the directive to include `sqft` in the output columns. When Task 8 completes, you tell the orchestrator about the change. It updates Tasks 9-14 to include sqft extraction and display.

**Lesson:** You're not locked into the original plan. Directives can evolve as you see the system work.

### Challenge 5: "How Do I Know When It's Done?"

**Symptom:** You're not sure if Phase 3 is complete or if you should keep monitoring.

**Solution:** Check the todo list and review the Definition of Done.

**Phase 3 is complete when:**
1. All tasks on the todo list are marked complete ✓
2. All tests have passed (Tester verified each implementation)
3. You've reviewed the screenshots/outputs
4. The Definition of Done criteria are met

**Example check:**
- Todo list: 14/14 tasks complete ✓
- Screenshots: Output CSV with sample data ✓
- Definition of Done: "All leads processed, enriched CSV created, error log generated" ✓

If all three are green, Phase 3 is done. Time to move to Phase 4 (bulletproofing).

**Lesson:** The todo list is your source of truth. When it's complete and verified, you're done.

## Your Turn: Try Building Your First Workflow

The best way to understand Phase 3 is to run it yourself. Here's a simple starter project you can complete in 60-90 minutes.

### Exercise: Company Research Automation

**Business problem:** You have a Google Sheet with 20 company names. You need to look up each company's website URL and LinkedIn profile URL for an outreach campaign.

**Doing this manually:** 5-10 minutes per company = 2-3 hours total.

**With Antigravity:** 60-90 minutes to build, then 5 minutes to run (forever).

### Step 1: Create the Directive

Use this template (save as `company_research.md`):

```markdown
# Company Research Workflow

**Objective:** Enrich company list with web presence data for outreach campaign

**Inputs:**
- Google Sheet with company names (link: [paste your sheet URL])
- Sheet name: "Companies"
- Column A contains company names (20 companies)

**Process:**
1. Read company names from Google Sheet
2. For each company:
   - Perform Google search: "[company name] official website"
   - Extract website URL from first search result
   - Perform Google search: "[company name] LinkedIn company page"
   - Extract LinkedIn URL from search results
   - Append to output data
3. Save results to CSV: ./output/company_research.csv
4. Take screenshot showing first 3 enriched companies

**Definition of Done:**
- All 20 companies processed
- Output CSV has three columns: company_name, website_url, linkedin_url
- Screenshot showing sample of enriched data
- At least 90% of companies have both URLs found
```

### Step 2: Hand to Orchestrator

Save the directive file and tell your orchestrator: "Please execute the company research workflow defined in company_research.md"

### Step 3: Watch the First 3 Cycles

Don't walk away yet. Watch Tasks 1-3 to see the pattern:
- Task 1: Connect to Google Sheets API
- Task 2: Read company names
- Task 3: Perform first search

Pay attention to how Coder → Tester → Iterate works.

### Step 4: Check In After 30 Minutes

Come back and review:
- How many tasks are complete? (Should be 6-8 of 10-12)
- Any failures? (Check what errors occurred and how Coder handled them)
- Look at screenshots (Does the data look correct?)

### Step 5: Provide Feedback If Needed

If you see something wrong (URLs are incorrect, LinkedIn is grabbing wrong companies), provide feedback:

"The LinkedIn URLs are grabbing personal profiles instead of company pages. Update the search query to '[company name] LinkedIn company page' to be more specific."

### Step 6: Celebrate When Complete

When all tasks are done:
- Review the output CSV
- Verify the screenshot shows good data
- Check that Definition of Done criteria are met

**Success criteria for this exercise:**
- You didn't write any code
- You reviewed screenshots instead of debugging
- You provided feedback in plain English (if needed)
- You have a working CSV with company data at the end

**Time investment:** 60-90 minutes
**Reusable forever:** Yes—just drop new company names in the sheet and run again

**Bonus learning:** Try the workflow with 5 companies first, verify it works, then scale to 20. This is how you de-risk in Phase 3—start small, verify, then scale.

## Key Takeaway

Phase 3 is where you go from "I have a plan" to "I have a working system." Your job is management: set the goal, review the work, provide feedback when needed. The AI team handles all the technical implementation, error handling, and iteration.

The orchestrator pattern—Plan, Delegate, Verify, Iterate—ensures quality by breaking big goals into small tasks, testing each one independently, and reasoning through failures instead of crashing.

You don't need to write code. You don't need to debug errors. You don't need to configure servers or wrestle with dependencies.

You need to write a clear directive, review screenshots, and provide feedback in plain English when something's off.

That's Phase 3. That's how Tom turned a $12,000 failure into an $0.87 success. That's how Jessica saved $18,850 per year in 78 minutes. That's how you build automation without becoming a programmer.

> [!TIP]
> If an agent is stuck on the same task for more than three attempts, it usually means your directive is too vague or has an ambiguity. Step in, update the directive with more specific criteria, and let the system resume. The clearer your Definition of Done, the faster Phase 3 completes.

> [!IMPORTANT]
> Never skip the Tester verification step. It's tempting to assume "if the Coder ran without errors, it must work." Visual verification with screenshots catches silent failures—wrong data extracted, incorrect calculations, broken formatting—that wouldn't trigger error messages.

---

┌─────────────────────────────────────────────────────────────┐
│  DOWNLOAD THE TRAINING LOG                                  │
│                                                              │
│  See a real-time log of an Orchestrator building a          │
│  complex web app from start to finish—every task,           │
│  every test, every error, and how it was resolved.          │
│                                                              │
│  travissteel.net/the-last-employee/resources#training-log               │
│                                                              │
│  DOWNLOAD 5 COPY-PASTE WORKFLOW DIRECTIVES                  │
│                                                              │
│  Real directives you can use immediately:                   │
│  - Lead enrichment system                                   │
│  - Email campaign automation                                │
│  - Data extraction pipeline                                 │
│  - Content research workflow                                │
│  - CRM integration system                                   │
│                                                              │
│  travissteel.net/the-last-employee/resources#starter-directives         │
│                                                              │
│  JOIN THE ANTIGRAVITY COMMUNITY                             │
│                                                              │
│  Get help when you're stuck, share your wins,               │
│  and learn from other business owners building              │
│  their AI teams.                                            │
│                                                              │
│  travissteel.net/the-last-employee/community                    │
└─────────────────────────────────────────────────────────────┘

---

**What's Next:** In Chapter 9, we'll take your working Phase 3 system and bulletproof it—handling edge cases, adding error recovery, and preparing it for production use. You'll learn the self-annealing pattern that lets your system fix its own mistakes and get smarter with every run.
