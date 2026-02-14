# Chapter 28: Advanced Directive Patterns

<!-- STATUS: Complete Draft -->
<!-- WORD TARGET: 3,500-4,500 words -->
<!-- ACTUAL WORD COUNT: ~4,280 words -->

---

## The Problem

You've written your first directive. It's clean. It has an objective, inputs, a step-by-step process, and a definition of done. You run it, and it works beautifully for a week.

Then the real world shows up.

A client asks, "Can we customize the report based on their industry?" You add a note to the directive. Another client needs the process to run twice for separate divisions. You add another note. A third client has a special data source that requires completely different logic. You start duplicating the entire directive and maintaining two versions.

Fast forward three months. You have seven variations of the same directive, each slightly different. When you discover a bug, you have to fix it seven times. When you improve the process, you have to update seven files. Your "clean" directive system has become a maintenance nightmare.

The problem isn't the directive framework. It's that **simple directives hit limits when facing complex reality**. Business processes aren't always linear. They branch based on conditions. They repeat until success. They coordinate multiple tasks happening simultaneously. They involve judgment calls, not just mechanical steps.

To handle real-world complexity, you need **Advanced Directive Patterns**—battle-tested structures that let your AI navigate the messy, non-linear nature of actual business operations.

This chapter is your field guide to those patterns.

---

## The Solution

Think of basic directives like recipes: "Step 1, Step 2, Step 3, done." They're perfect for making scrambled eggs. But what happens when you're running a restaurant kitchen during dinner rush?

You don't just follow one recipe. You're coordinating multiple stations, adapting to ingredient availability, making judgment calls about substitutions, and adjusting timing based on how busy the dining room is. You're using **kitchen systems**—patterns that chefs have developed over centuries to handle complexity.

Advanced directive patterns are the same concept, applied to AI workflows. They're design patterns that solve recurring problems:

- **How do I coordinate multiple workflows that always run together?** → Metadirectives
- **How do I make decisions mid-workflow based on data?** → Conditional logic
- **How do I handle tasks that need to run simultaneously?** → Fan-out patterns
- **How do I dig deeper until I find the answer?** → Recursive loops
- **How do I make my directives improve themselves?** → Self-annealing integration

These aren't theoretical concepts. They're practical tools you'll use constantly once your agentic system moves beyond simple tasks.

Let's break them down.

---

## How It Works: Five Essential Patterns

### Pattern 1: The Metadirective (The Umbrella)

As your directive library grows, you'll notice that certain workflows always happen together. Instead of creating one massive 50-step directive, you build a **Metadirective**—a high-level coordinator that calls smaller, specialized directives in sequence.

**The Problem It Solves:**

Your new client onboarding process involves five distinct operations:
1. Pull their data from the CRM
2. Create a dedicated Slack channel
3. Draft a welcome email with personalized details
4. Set up their billing profile in Stripe
5. Schedule the kickoff meeting

Each operation is complex enough to deserve its own directive. But you don't want to manually trigger five separate workflows every time you onboard a client. You want one button to press.

**The Structure:**

A metadirective is essentially a **playbook that references other playbooks**. Here's what it looks like:

```markdown
# Metadirective: New Client Onboarding

## Objective
Complete all technical and communication setup for a new client within 24 hours of contract signing.

## Inputs
- Client name
- CRM record ID
- Contract value
- Primary contact email

## Process

### Step 1: Data Integration
Call `Directive: Ingest CRM Data`
- Pass: CRM record ID
- Output: Structured client data file (client_data.json)

### Step 2: Communication Setup
Call `Directive: Create Slack Channel`
- Pass: Client name, Primary contact email
- Output: Slack channel URL

### Step 3: Welcome Communication
Call `Directive: Draft Welcome Email`
- Pass: Client data file, Slack channel URL
- Output: Draft email in Gmail

### Step 4: Billing Configuration
Call `Directive: Set Up Stripe Profile`
- Pass: Client name, Contract value, Primary contact email
- Output: Stripe customer ID

### Step 5: Meeting Scheduling
Call `Directive: Schedule Kickoff Meeting`
- Pass: Primary contact email, Slack channel URL
- Output: Calendar invite sent

## Definition of Done
- [ ] All five sub-directives completed successfully
- [ ] Client record updated with Slack URL and Stripe ID
- [ ] Welcome email sent
- [ ] Kickoff meeting on calendar within 5 business days
```

**Why This Works:**

Each sub-directive is modular and reusable. You can update the "Welcome Email" logic without touching the "Stripe Profile" logic. If you hire a client from a different source (referral instead of CRM), you can skip Step 1 and start at Step 2. The metadirective provides structure without rigidity.

**The Management Analogy:**

A CEO doesn't personally handle HR, finance, operations, and sales. They delegate to department heads who each run their own teams. The CEO's job is coordination, not execution. A metadirective is the CEO of your workflow—it makes sure everything happens in the right order, but the actual work is done by specialists.

---

### Pattern 2: Conditional Logic (The If-Else Decision Tree)

Not every client needs the same treatment. Not every lead gets the same follow-up. Your directives need the ability to **make strategic choices mid-workflow** based on data.

**The Problem It Solves:**

You're building a competitive research directive. But the analysis you need depends entirely on the prospect's business model:
- E-commerce companies need SEO audits for product pages
- Service agencies need lead magnet analysis
- SaaS companies need pricing page teardowns

One-size-fits-all doesn't work. You need branching logic.

**The Structure:**

Conditional directives use natural language decision trees:

```markdown
# Directive: Competitive Website Audit

## Objective
Generate a 3-page competitive analysis report customized to the prospect's business model.

## Inputs
- Prospect website URL
- Industry (if known)

## Process

### Step 1: Business Model Classification
Analyze the prospect's website and classify their business model:
- Look for shopping cart, product catalogs → E-commerce
- Look for service descriptions, case studies, contact forms → Service Agency
- Look for pricing tiers, free trial CTAs, demo requests → SaaS
- If unclear, default to "General"

Document the classification in the output notes.

### Step 2: Conditional Audit Path

**Branch A: If E-commerce**
- Call `Directive: Audit Shopify SEO`
- Focus on product page optimization, site speed, checkout flow
- Include competitor price comparison

**Branch B: If Service Agency**
- Call `Directive: Audit Lead Magnet Strategy`
- Focus on content offers, email capture, nurture sequences
- Include competitor content gap analysis

**Branch C: If SaaS**
- Call `Directive: Audit Pricing Page Strategy`
- Focus on pricing transparency, feature comparison, trial friction
- Include competitor pricing matrix

**Branch D: If General (Fallback)**
- Call `Directive: Generic Site Audit`
- Focus on basic SEO, page speed, mobile responsiveness
- Include high-level competitive positioning notes

### Step 3: Report Compilation
Compile the audit results into a standardized 3-page PDF report.

## Definition of Done
- [ ] Business model correctly classified
- [ ] Appropriate audit directive executed
- [ ] PDF report generated
- [ ] Competitor comparison included
```

**Why This Works:**

The agent isn't following a rigid script. It's making an informed decision based on data, then executing the appropriate specialized workflow. Each branch can be as complex as needed without cluttering the others.

**The Specialist Analogy:**

When you go to the doctor with chest pain, they don't immediately perform heart surgery. They diagnose first. If it's heartburn, you get antacids. If it's a muscle strain, you get physical therapy. If it's a heart attack, you get emergency care. The treatment depends on the diagnosis. Conditional directives work the same way: assess, then act accordingly.

---

### Pattern 3: The Fan-Out Pattern (Parallel Processing)

Some tasks are inherently sequential—you can't write the report before gathering the data. But other tasks are **embarrassingly parallel**—they don't depend on each other and can happen simultaneously.

**The Problem It Solves:**

You need to analyze 20 competitors for a client. If you process them one at a time, each taking 5 minutes, that's 100 minutes of sequential execution. But there's no reason Competitor #2 has to wait for Competitor #1 to finish. They're independent tasks.

**The Structure:**

Fan-out directives explicitly tell the orchestrator to spawn multiple specialist agents simultaneously:

```markdown
# Directive: Multi-Competitor Analysis

## Objective
Generate a comprehensive competitive landscape report covering all major competitors in the prospect's market.

## Inputs
- List of competitor domains (up to 20)
- Analysis depth (Quick / Standard / Deep)

## Process

### Step 1: Competitor List Validation
- Remove duplicates
- Verify domains are reachable
- Categorize by company size (if detectable)

### Step 2: Fan-Out Parallel Research
**Orchestrator Action:** For each validated competitor domain, spawn a separate Researcher Agent instance.

Each Researcher Agent executes:
- Call `Directive: Single Competitor Audit`
- Pass: Competitor domain, Analysis depth
- Output: Competitor profile JSON file

**Critical:** All researcher agents run simultaneously. Do not wait for Agent 1 to finish before starting Agent 2.

Set timeout: 10 minutes per agent. If any agent exceeds timeout, log the failure and continue with remaining agents.

### Step 3: Aggregation (Wait for All)
Once all researcher agents complete (or timeout):
- Collect all competitor profile JSON files
- Call `Directive: Synthesize Competitive Landscape`
- Pass: Array of all competitor profiles
- Output: Comparative analysis report with market positioning matrix

## Definition of Done
- [ ] At least 80% of competitor domains successfully analyzed
- [ ] Landscape synthesis report generated
- [ ] Market positioning matrix included
- [ ] Failed competitors logged with reasons
```

**Why This Works:**

Instead of 100 minutes of sequential processing, you get 5-10 minutes of parallel processing (limited only by API rate limits and computing resources). The orchestrator doesn't babysit each task—it launches them all, then waits for the results.

**The Project Manager Analogy:**

If you need 10 blog posts written, you don't hire one writer and wait for them to finish all 10 sequentially. You hire 10 writers, give them each one assignment, and collect the drafts when they're all done. Fan-out directives do the same thing with AI agents.

---

### Pattern 4: Recursive Research Loops (Seek and Refine)

Most AI research is shallow. You ask a question, get a surface-level answer, and move on. But what if you need **depth**? What if you need the AI to keep digging until it finds the real answer, not just the first answer?

**The Problem It Solves:**

You're researching a complex topic—let's say "How do enterprise SaaS companies structure their sales compensation plans?" A single search gives you generic advice. But you need specific data points: base salary ranges, commission structures, quota attainment bonuses, accelerators.

**The Structure:**

Recursive directives contain a loop with a stopping condition:

```markdown
# Directive: Deep Research on Complex Topic

## Objective
Produce a comprehensive research report with authoritative data, not surface-level summaries.

## Inputs
- Research question
- Depth level (1-3, where 3 is deepest)
- Maximum iterations (default: 3)

## Process

### Step 1: Initial Search
Perform a broad search for the research question.
Extract key findings and document all claims that lack supporting data.

Tag each finding:
- ✅ PROVEN: Has citation, data, or authoritative source
- ❓ CLAIM: Stated but no evidence provided
- 🔍 GAP: Contradictory information or missing context

### Step 2: Recursive Deep Dive (Loop)

**For each ❓ CLAIM or 🔍 GAP:**
1. Formulate a targeted sub-question to validate or disprove the claim
2. Perform a focused search for that specific sub-question
3. Extract supporting data or contradicting evidence
4. Update the finding status (❓ → ✅ or ❓ → ❌ DISPROVEN)

**Repeat until:**
- All ❓ CLAIMS are resolved to ✅ PROVEN or ❌ DISPROVEN, OR
- Maximum iterations reached, OR
- No new information found in the last iteration

### Step 3: Synthesis
Compile all ✅ PROVEN findings into a structured research report.
Flag any remaining ❓ CLAIMS as "Unverified" in a separate section.

## Definition of Done
- [ ] At least 80% of claims validated or disproven
- [ ] Research report cites authoritative sources
- [ ] Unverified claims clearly flagged
- [ ] Iteration count logged
```

**Why This Works:**

Traditional research stops at the first answer. Recursive research treats the first answer as a **starting point** and keeps digging. Each iteration reveals deeper layers, filling gaps and validating claims.

**The Investigative Journalist Analogy:**

A lazy reporter reads a press release and publishes it as fact. An investigative journalist reads the press release, identifies the unsupported claims, interviews sources, digs through public records, cross-references data, and publishes only what they can verify. Recursive directives turn your AI into an investigative journalist.

---

### Pattern 5: Self-Annealing Integration (The Learning Loop)

This is the pattern that separates static automation from living systems. It instructs the agent to not just execute the directive, but to **improve it** when something goes wrong.

**The Problem It Solves:**

Your directive works perfectly for 95% of cases. Then a client sends data in an unexpected format, and the workflow breaks. You fix it manually. Two weeks later, the same issue happens with a different client. You fix it again.

Without self-annealing, you're stuck in an endless break-fix cycle.

**The Structure:**

Self-annealing directives include explicit instructions for handling and learning from errors:

```markdown
# Directive: Process Client Invoice Data

## Objective
Extract invoice data from uploaded files and update billing records.

## Inputs
- Invoice file (PDF or CSV)
- Client ID

## Process

### Step 1: File Format Detection
Identify whether the invoice is PDF or CSV.
Extract relevant fields: Invoice number, Date, Amount due, Line items.

### Step 2: Data Validation
Verify that all required fields are present and properly formatted.
Check for anomalies: negative amounts, future dates, missing line items.

### Step 3: Update Billing Records
Write validated data to the billing database.
Mark invoice as "Processed" in the tracking system.

## Error Handling & Self-Annealing

**If you encounter an error not covered in this directive:**

1. **Stop execution immediately.** Do not guess or use fallback logic.

2. **Diagnose the root cause:**
   - Is this a new file format variation?
   - Is this a data quality issue (missing fields, wrong data type)?
   - Is this an external system error (database unavailable, API timeout)?

3. **Categorize the error:**
   - **Tier 1 (Routine):** Missing field, format variation, known edge case → Auto-fixable
   - **Tier 2 (Novel):** New file structure, unexpected data type → Requires analysis
   - **Tier 3 (Critical):** Data corruption risk, financial discrepancy, security concern → Escalate to human

4. **For Tier 1 & 2 errors:**
   - Document the specific error condition
   - Draft a fix for the execution code
   - Update THIS DIRECTIVE with a new step or conditional branch to handle this case
   - Submit a "Learnings Update" to the orchestrator

5. **For Tier 3 errors:**
   - Invoke the Stuck Agent immediately
   - Provide full error context and diagnostic findings
   - Wait for human decision before proceeding

**Learnings Log:**
This section is automatically updated by the self-annealing process. Do not manually edit.

- 2026-01-15: Added handling for CSV files with semicolon delimiters (European format)
- 2026-01-22: Added validation for invoices with multiple currency symbols
- 2026-02-03: Added fallback for PDFs with scanned (non-searchable) text
```

**Why This Works:**

The directive isn't static. It's a **living document** that grows smarter with every error it encounters. The same mistake never happens twice because the fix becomes part of the permanent playbook.

**The Expert Employee Analogy:**

Imagine you hire two assistants. Assistant A follows the manual exactly and stops whenever something unexpected happens. Assistant B follows the manual, but when they encounter a new situation, they solve it, document the solution, and update the manual for next time.

After six months, Assistant A is still stopping at the same issues. Assistant B has encountered 30 edge cases and now handles all of them automatically. That's the difference self-annealing makes.

---

## Real Example: The Complete Advanced Directive

Let's see how these patterns work together in a real-world scenario. Here's a directive that uses **all five advanced patterns** to handle a complex business process: quarterly client reporting.

```markdown
# Metadirective: Quarterly Client Reporting (Q1 2026)

## Objective
Generate customized quarterly performance reports for all active clients, delivered within 48 hours of quarter close.

## Inputs
- List of active client IDs (from CRM)
- Reporting quarter (e.g., Q1 2026)
- Report template preference per client (stored in client profile)

## Process

### Step 1: Client List Validation
Call `Directive: Fetch Active Clients`
Output: Array of client objects with IDs, names, industry, contract tier

### Step 2: Conditional Template Selection (Per Client)
For each client, determine the appropriate report template:

**Branch A: If contract tier = Enterprise**
- Use template: `Enterprise_Quarterly_Report_v2.3`
- Include: Executive summary, ROI calculator, strategic recommendations

**Branch B: If contract tier = Professional**
- Use template: `Professional_Quarterly_Report_v2.1`
- Include: Performance metrics, trend analysis, next quarter forecast

**Branch C: If contract tier = Starter**
- Use template: `Starter_Quarterly_Report_v1.5`
- Include: Basic metrics summary, key wins, support ticket stats

### Step 3: Fan-Out Parallel Report Generation
**Orchestrator Action:** For each client, spawn a separate Report Generator Agent.

Each agent executes:
- Call `Directive: Generate Single Client Report`
- Pass: Client ID, Quarter, Template type
- Output: PDF report file

All agents run simultaneously. Timeout: 15 minutes per agent.

### Step 4: Recursive Quality Check (Loop)
For each generated report:

1. Call `Directive: Validate Report Completeness`
2. Check for: Missing data fields, broken charts, incorrect calculations
3. Tag each report:
   - ✅ COMPLETE: All sections populated, data validated
   - ⚠️ INCOMPLETE: Missing data in non-critical sections
   - ❌ FAILED: Critical data missing or calculations incorrect

**For each ⚠️ INCOMPLETE or ❌ FAILED report:**
- Attempt to regenerate with enhanced data fetching
- If regeneration fails, escalate to Stuck Agent

**Repeat until:** All reports are ✅ COMPLETE or escalated, OR maximum 2 iterations reached.

### Step 5: Delivery & Self-Annealing

Call `Directive: Deliver Client Reports`
- Send via client's preferred channel (email, Slack, portal upload)
- Log delivery confirmation

**Self-Annealing Check:**
If ANY report generation failed or required manual intervention:
1. Document the specific failure mode
2. Update the relevant sub-directive with handling logic
3. Log the learning in the Quarterly Reporting Learnings repository

## Definition of Done
- [ ] Reports generated for 100% of active clients
- [ ] All reports pass completeness validation
- [ ] All reports delivered via preferred channel
- [ ] Any failures documented and directive updated
- [ ] Process completion time logged (target: < 48 hours)

## Learnings Log
- Q4 2025: Added handling for clients with paused campaigns (show historical data with "Paused" flag)
- Q1 2026: Added retry logic for clients with API rate limiting on data sources
```

This metadirective orchestrates multiple sub-directives, uses conditional logic to customize per client, fans out for parallel processing, employs recursive loops for quality assurance, and includes self-annealing to improve with each quarterly run.

---

## Try It Yourself: Add Advanced Patterns to Your Directive

Take one of your existing directives—ideally one that's starting to feel clunky or limited—and identify where an advanced pattern could help:

**Exercise 1: Identify Repetition**
Do you have multiple versions of similar directives? Create a metadirective that coordinates them instead of duplicating logic.

**Exercise 2: Identify Decision Points**
Does your directive have notes like "sometimes do X, sometimes do Y"? Add explicit conditional logic to formalize those decisions.

**Exercise 3: Identify Bottlenecks**
Does your directive process a list of items sequentially? Consider if fan-out parallel processing would speed it up.

**Exercise 4: Identify Shallow Results**
Does your directive stop at the first answer? Add a recursive loop to dig deeper until the real insight emerges.

**Exercise 5: Identify Recurring Fixes**
Do you keep manually fixing the same issues? Add self-annealing instructions so the directive learns from those fixes.

Pick one pattern and implement it this week. You'll immediately see the difference between a basic directive and an advanced one.

---

┌─────────────────────────────────────────────────────┐
│  DOWNLOAD THIS TEMPLATE                             │
│                                                      │
│  Get the Advanced Directive Pattern Library:        │
│  travissteel.net/the-last-employee/resources#advanced            │
│                                                      │
│  Includes ready-to-use templates for:                │
│  - Metadirectives with sub-directive coordination    │
│  - Conditional logic decision trees                  │
│  - Fan-out parallel processing patterns              │
│  - Recursive research loops with stopping conditions │
│  - Self-annealing error handling frameworks          │
└─────────────────────────────────────────────────────┘

---

## Key Takeaway

Basic directives are linear: Step 1, Step 2, Step 3, done. Advanced directives are **adaptive**: they coordinate multiple workflows, make strategic decisions, process tasks in parallel, dig deeper when needed, and improve themselves over time.

The difference between a directive that works in a demo and one that works in production is whether it can handle real-world complexity. These five patterns—metadirectives, conditional logic, fan-out processing, recursive loops, and self-annealing—are how you build directives that don't just execute tasks, but solve problems.

Your AI isn't just following instructions. It's thinking, adapting, and learning. That's the power of advanced directive patterns.
