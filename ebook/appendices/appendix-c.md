# Appendix C: Directive Template

## Your Copy-Paste Foundation for Every Agentic Workflow

This appendix contains what might be the most valuable resource in this entire book: a blank directive template you can copy, fill in, and immediately use to build your first agentic workflow.

### What This Template Is

This is not theoretical framework or abstract methodology. This is a production-ready document structure that has been battle-tested across hundreds of agentic workflows. Every successful directive—whether it's scraping leads, generating content, processing invoices, or qualifying customers—follows this exact format.

Think of it as the blueprint. Chapter 27 taught you how to extract the raw materials from your messy processes. This appendix gives you the construction template to turn those materials into something agents can actually execute.

### Why This Template Matters

Here's what makes a directive different from a regular SOP or process document:

**Traditional SOPs are written for humans**. They assume context, forgive ambiguity, and rely on judgment calls. "Handle it appropriately" makes sense to your team member.

**Directives are written for agents**. They require explicit inputs, clear decision trees, and measurable success criteria. "Handle it appropriately" causes an agent to hallucinate, make assumptions, or invoke the stuck agent.

This template forces you to think like an agent designer. It makes you specify:
- Exactly what inputs are required (not "some customer data" but "customer email, company name, and industry")
- Precisely what success looks like (not "good quality" but "email is personalized with 3+ company-specific facts")
- Clear branching logic for edge cases (not "handle errors gracefully" but "if API returns 429, wait 60 seconds and retry up to 3 times")

The discipline of filling in this template will reveal gaps you didn't know existed in your process. That's the point. Better to discover them now while designing the directive than later when your agent is hallucinating in production.

### How to Use This Template

The workflow is simple:

1. **Start with Chapter 27's extraction framework** if you're translating an existing process
2. **Copy the blank template** from Section 3 below
3. **Fill in each section** using the guidance provided
4. **Reference the worked example** in Section 4 when you get stuck
5. **Test with the orchestrator** and iterate based on results

Your first directive will take 30-60 minutes to write. Your tenth will take 15 minutes. By your twentieth, you'll be writing directives faster than traditional SOPs because the structure is internalized.

Remember: Version 1 doesn't need to be perfect. The self-annealing process (Chapter 29) will refine it through real-world execution. Your job right now is to get it good enough to test.

---

## The 4-Section Directive Framework

Every directive contains exactly four sections. No more, no less. This structure has been refined through hundreds of implementations to balance completeness with usability.

### Section 1: Objective

**What needs to happen**—the desired outcome, not the process to achieve it. This is the "why" section that gives agents and humans alike the context to make good decisions when the process encounters something unexpected.

Write 2-3 sentences maximum. If you need more, your workflow is probably too complex and should be split into multiple directives.

### Section 2: Inputs

**What data and access are required** for this workflow to execute. This includes data sources, API credentials, trigger conditions, and any prerequisite states that must be true.

Think of this as the dependency checklist. If any input is missing, the workflow cannot start. Be exhaustively specific here—"customer data" is not an input, "customer email address, company name, and industry from HubSpot CRM" is an input.

### Section 3: Process

**Step-by-step workflow in plain English**. This is the longest section, but resist the urge to write code. Describe WHAT needs to happen at each step, not HOW the agent should do it (that's the execution layer's job).

Include success criteria for each step and explicit error handling. Agents need to know what success looks like and what to do when it doesn't look that way.

### Section 4: Definition of Done

**Checkable success criteria** that allow both agents and humans to verify completion. This section answers: "How do we know this workflow executed correctly?"

Include quality standards beyond simple completion. "Email sent" is not enough—"Email sent with personalized subject line, 3+ company-specific facts in body, and professional tone" is a Definition of Done.

---

## The Complete Blank Template

Copy everything below this line and paste it into your own `.md` file:

```markdown
# [Workflow Name] Directive

**Created**: [Date]
**Owner**: [Your Name]
**Frequency**: [Daily/Weekly/Monthly/On-demand]

---

## Objective

**What needs to happen:**
[Write 2-3 sentences describing the desired outcome, not the process]

**Why this matters:**
[Explain the business value - time saved, revenue generated, errors prevented]

---

## Inputs

**Required Data:**
- [ ] [Data source 1 - e.g., "Client email addresses from CRM"]
- [ ] [Data source 2]
- [ ] [Data source 3]

**Required Access:**
- [ ] [Tool/system 1 - e.g., "Google Ads API access"]
- [ ] [Tool/system 2]

**Trigger Conditions:**
- **When**: [e.g., "Every Tuesday at 9 AM" or "When form submitted"]
- **If**: [Any conditional requirements]

---

## Process

**Step-by-step workflow (in plain English):**

1. [First action - describe the WHAT, not the HOW]
   - Success looks like: [Observable outcome]
   - If error: [How to handle]

2. [Second action]
   - Success looks like: [Observable outcome]
   - If error: [How to handle]

3. [Continue for all steps...]

**Edge Cases & Exceptions:**
- **If [scenario]**: Then [how to handle]
- **If [scenario]**: Then [how to handle]

---

## Definition of Done

**This workflow is complete when:**
- [ ] [Checkable outcome 1]
- [ ] [Checkable outcome 2]
- [ ] [Checkable outcome 3]

**Quality Standards:**
- [Requirement 1 - e.g., "Email tone is professional and personalized"]
- [Requirement 2]

**Notification:**
- **Who to notify**: [Person/system]
- **How**: [Email, Slack, etc.]
- **What to include**: [Summary of results]

---

## Notes & Learnings

**Known Issues:**
- [Document problems discovered during testing]

**Optimization Ideas:**
- [Future improvements to consider]

**Self-Annealing Updates:**
- [Date]: [What was changed and why]
```

---

## Worked Example: Weekly Client Reporting Directive

Here's how the template looks when filled in for a real-world workflow. This example automates a task that typically takes 2-3 hours every Monday morning: compiling performance data from multiple tools and generating personalized client reports.

```markdown
# Weekly Client Performance Report Directive

**Created**: January 15, 2026
**Owner**: Marketing Operations Team
**Frequency**: Weekly (Monday 8 AM)

---

## Objective

**What needs to happen:**
Generate personalized weekly performance reports for all active marketing clients, pulling data from Google Ads, Meta Ads, and Google Analytics, then email each client their customized report with insights and recommendations.

**Why this matters:**
Manually creating these reports takes 2-3 hours every Monday morning, delaying other priorities and causing inconsistent quality across clients. Automation ensures every client receives their report by 9 AM with consistent formatting and insights quality.

---

## Inputs

**Required Data:**
- [ ] List of active clients with associated Google Ads account IDs from Airtable "Active Clients" table
- [ ] Client email addresses and preferred contact names from Airtable
- [ ] Google Ads performance data (impressions, clicks, conversions, spend) for previous 7 days
- [ ] Meta Ads performance data for clients with Meta campaigns active
- [ ] Google Analytics traffic data (sessions, bounce rate, goal completions) for previous 7 days

**Required Access:**
- [ ] Google Ads API with read access to all client accounts
- [ ] Meta Marketing API with read access to client ad accounts
- [ ] Google Analytics API with read access to client properties
- [ ] Airtable API access to "Active Clients" base
- [ ] SendGrid API for email delivery

**Trigger Conditions:**
- **When**: Every Monday at 8:00 AM EST
- **If**: Client status = "Active" in Airtable AND at least one campaign was active in previous 7 days

---

## Process

**Step-by-step workflow (in plain English):**

1. **Query Airtable for active clients**
   - Success looks like: Retrieved list of 15-30 clients with required fields (name, email, Google Ads ID, Meta ID if applicable, industry)
   - If error: If Airtable API returns error, retry up to 3 times with 30-second delays. If still failing, invoke stuck agent with error details.

2. **For each client, fetch Google Ads performance data**
   - Success looks like: Retrieved metrics for previous 7 days including impressions, clicks, CTR, conversions, cost, and ROAS
   - If error: If specific client account returns 403 (access denied), skip that client and log for manual review. If 429 (rate limit), wait 60 seconds and retry. If other error, invoke stuck agent.

3. **For clients with Meta campaigns, fetch Meta Ads performance data**
   - Success looks like: Retrieved same metrics as Google Ads for comparison
   - If error: If client has no Meta ID in Airtable, skip this step. Handle API errors same as Google Ads.

4. **Fetch Google Analytics traffic data for each client's website**
   - Success looks like: Retrieved sessions, bounce rate, avg session duration, and goal completions
   - If error: If GA property not linked or no data available, note in report as "Analytics data unavailable" and continue.

5. **Calculate week-over-week performance changes**
   - Success looks like: Percentage changes calculated for all key metrics (impressions, clicks, conversions, spend)
   - If error: If previous week's data is incomplete, show "N/A" for comparison metrics but continue with raw numbers.

6. **Generate insights using Gemini 2.5 Pro**
   - Success looks like: 3-5 bullet points of personalized insights based on: (1) performance trends, (2) comparison to previous week, (3) industry context, (4) actionable recommendations
   - If error: If the AI API fails, retry once. If still failing, use fallback template with basic observations and invoke stuck agent to review before sending.

7. **Compile report in HTML email template**
   - Success looks like: Professional-looking email with client name, date range, metrics table, insights section, and call-to-action for scheduling next check-in
   - If error: If template rendering fails, log error and invoke stuck agent.

8. **Send personalized email to each client via SendGrid**
   - Success looks like: Email sent successfully with 200 response from SendGrid API
   - If error: If SendGrid returns error, save draft to "Failed Reports" Airtable table and notify team via Slack.

9. **Log completion status to Airtable**
   - Success looks like: "Last Report Sent" field updated with current date and "Report Status" set to "Delivered"
   - If error: If Airtable update fails, the report was still sent, so log warning but don't block workflow.

**Edge Cases & Exceptions:**
- **If client has zero ad spend in past 7 days**: Send email noting "No active campaigns this week" and skip metrics section
- **If client is marked "Paused" in Airtable**: Skip entirely for this week
- **If multiple client emails in Airtable**: Send to all addresses listed
- **If client industry = "Healthcare"**: Add HIPAA compliance disclaimer to email footer

---

## Definition of Done

**This workflow is complete when:**
- [ ] All active clients (15-30 typically) have been processed
- [ ] Each client received an email with their personalized report
- [ ] All emails show "Delivered" status in SendGrid
- [ ] Airtable "Active Clients" table shows updated "Last Report Sent" dates for all clients
- [ ] No errors are logged in stuck agent queue

**Quality Standards:**
- Client name and date range are correct in every email
- All metrics tables show data for the correct 7-day period
- Week-over-week comparisons are mathematically accurate
- Insights are personalized (mention client's specific campaigns or industry context)
- Email tone is professional and constructive (not robotic)
- All links (to ad accounts, analytics, scheduling tool) are functional

**Notification:**
- **Who to notify**: Marketing Operations Manager
- **How**: Slack message to #marketing-ops channel
- **What to include**: Summary report showing: number of clients processed, number of emails sent successfully, any errors or clients skipped, total execution time

---

## Notes & Learnings

**Known Issues:**
- Google Ads API occasionally times out for clients with 50+ campaigns; consider implementing pagination if this persists
- Some clients have GA properties linked in Airtable that are no longer accessible; need periodic audit of client access

**Optimization Ideas:**
- Add visualization charts (spend trend, conversion graph) to make reports more scannable
- Consider adding competitive benchmarking if we can source industry average data
- Explore using the AI's prompt caching for faster insight generation across multiple clients

**Self-Annealing Updates:**
- Jan 22, 2026: Added retry logic for Google Ads API 429 errors after hitting rate limits on first production run
- Jan 29, 2026: Modified insights prompt to explicitly request 3-5 bullets after receiving feedback that some reports had 10+ bullets
- Feb 5, 2026: Added healthcare compliance disclaimer after client request
```

---

## Common Mistakes When Writing Directives

After reviewing hundreds of first-draft directives, these are the patterns that consistently cause problems:

### Mistake 1: Being Too Specific About HOW (vs. WHAT)

**Bad directive writing:**
```
1. Use BeautifulSoup to parse the HTML and extract all <a> tags
2. Loop through each tag and check if href contains "linkedin.com"
3. Store results in a pandas DataFrame with columns for name and URL
```

**Good directive writing:**
```
1. Extract all LinkedIn profile URLs from the company's "Team" page
   - Success looks like: List of 5-30 profile URLs
   - If error: If page structure has changed, invoke stuck agent
```

The bad version tells the execution layer exactly how to code the solution. This creates brittleness—if BeautifulSoup isn't the right tool or the implementation details change, the directive is wrong.

The good version describes the outcome. The execution layer (your coder agent) can choose BeautifulSoup, Playwright, regex, or any other approach that achieves the objective.

### Mistake 2: Missing Edge Cases

**Incomplete directive:**
```
1. Send personalized email to each lead
   - Success looks like: Email sent
```

**Complete directive:**
```
1. Send personalized email to each lead
   - Success looks like: Email sent with 200 response from API
   - If error: If email bounces, mark lead as "Invalid Email" in CRM
   - Edge cases:
     - If lead has no company name, use "[First Name]'s Company" as fallback
     - If lead has unsubscribed, skip and log
     - If sending fails 3 times, invoke stuck agent
```

Your agents will encounter the unexpected. Edge cases and error handling aren't optional—they're what separates a directive that works in production from one that breaks the first time reality doesn't match your assumptions.

### Mistake 3: Vague Definition of Done

**Vague:**
```
This workflow is complete when:
- [ ] Leads are processed
- [ ] Quality is good
```

**Specific:**
```
This workflow is complete when:
- [ ] All 50-200 leads from this week's form submissions have been scored
- [ ] Each lead has a score between 0-100 in the CRM "Lead Score" field
- [ ] High-priority leads (score >70) have been assigned to sales reps
- [ ] Summary report shows score distribution and top 10 leads
```

"Quality is good" is not checkable. "Each lead has a score between 0-100" is checkable. The Definition of Done must allow both agents and humans to verify success without subjective judgment.

### Mistake 4: No Quality Standards Beyond Completion

**Missing quality standards:**
```
Definition of Done:
- [ ] Email sent to client
```

**Includes quality standards:**
```
Definition of Done:
- [ ] Email sent to client

Quality Standards:
- Email includes client's name (not "Hi there")
- Subject line references specific campaign or date range
- Tone is professional but conversational (not robotic)
- All links are functional
- No spelling or grammar errors
```

Just because a task was completed doesn't mean it was completed well. Quality standards catch the difference between "email sent" and "email sent that actually maintains client relationships."

### Mistake 5: Over-Engineering Simple Workflows

**Over-engineered:**
```
# Weekly Invoice Reminder Directive

[15 pages of detailed branching logic for every possible scenario]
```

**Right-sized:**
```
# Weekly Invoice Reminder Directive

Process:
1. Query accounting system for invoices 7+ days overdue
2. Send reminder email to each client
3. If invoice is 30+ days overdue, CC the account manager
```

Not every workflow needs to handle every edge case on day one. Start simple. Let self-annealing reveal which edge cases actually matter through real-world execution. You can always add complexity later; it's much harder to simplify an over-complex directive.

If your directive is longer than 2 pages, it's probably too complex and should be split into multiple directives or metadirectives.

---

## Quick-Start Guide: Write Your First Directive in 30 Minutes

Here's the fastest path from "I have a repetitive task" to "I have a working directive":

### Step 1: Pick Your Target (5 minutes)

Choose your most annoying weekly task. Not the most complex, not the most important—the one that makes you groan when Monday morning rolls around.

Good first directive candidates:
- Weekly reporting that pulls data from multiple tools
- Lead qualification that follows a clear scoring rubric
- Content distribution that reposts to multiple platforms
- Invoice follow-ups based on aging rules
- Data entry from emails/forms into your CRM

Bad first directive candidates:
- Strategic planning (too subjective)
- Complex negotiations (requires human judgment)
- Creative work with unclear quality criteria
- Processes with constantly changing rules

### Step 2: Extract Structure (10 minutes)

Open Chapter 27 and follow the extraction framework. Answer these questions in your notebook:

1. What triggers this task? (time, event, condition)
2. What information do you need to start? (be specific)
3. What do you do first, second, third? (plain English, main steps only)
4. What does success look like? (specific, measurable)
5. What goes wrong sometimes? (the edge cases you've encountered)

Don't overthink it. You're not writing the directive yet, just extracting the raw structure from your brain.

### Step 3: Fill In the Template (10 minutes)

Copy the blank template from Section 3. Start filling it in using your extraction notes:

- **Objective**: Translate question 4 into 2-3 sentences
- **Inputs**: Expand question 2 with specific data sources and access requirements
- **Process**: Expand question 3 into numbered steps with success criteria
- **Definition of Done**: Turn question 4 into checkable outcomes

Don't aim for perfection. Aim for complete—all sections filled in with your best current understanding.

### Step 4: Test With Orchestrator (5 minutes)

Give your directive to the orchestrator with this prompt:

```
I've written my first directive for [workflow name]. Please review it
for completeness and flag any missing inputs, vague success criteria,
or unhandled edge cases. Don't implement anything yet—just review the
directive itself.
```

The orchestrator will catch obvious gaps. Make quick updates based on feedback.

### Step 5: Run a Test Execution (Variable time)

Now ask the orchestrator to execute the directive:

```
Please implement and test this directive: [paste directive]
```

Watch what happens. The coder agent will expose ambiguities you didn't realize existed. The tester agent will reveal whether your Definition of Done is actually checkable.

This is where the real learning happens. Your first execution will surface issues. That's expected. That's good. Update your directive based on what breaks.

### Step 6: Iterate Based on Reality

After the first test run:

1. Document what broke in "Known Issues"
2. Update the Process section to handle errors you encountered
3. Refine Definition of Done to match what you actually care about
4. Add edge cases you discovered to the Edge Cases section

Run it again. Your directive will get better with each iteration.

---

## Download This Template & Examples

```
┌─────────────────────────────────────────────────────┐
│  DOWNLOAD THIS TEMPLATE & EXAMPLES                  │
│                                                      │
│  Get the blank template plus 10+ filled examples:   │
│                                                      │
│  travissteel.net/the-last-employee/resources#directives         │
│                                                      │
│  • Blank template (copy-paste ready)                │
│  • 10+ real-world examples                          │
│  • Industry-specific templates                      │
│  • Advanced metadirective structures                │
└─────────────────────────────────────────────────────┘
```

The downloadable resource includes:

**Templates:**
- Blank directive template (from this appendix)
- Blank metadirective template for complex workflows
- Directive review checklist
- Self-annealing update template

**Examples by Use Case:**
- Lead generation and qualification
- Content creation and distribution
- Invoice processing and collections
- Weekly reporting and analytics
- Customer onboarding automation
- Social media scheduling
- Email sequence management
- Data cleanup and enrichment
- Competitive intelligence gathering
- Event follow-up workflows

**Industry-Specific Examples:**
- E-commerce (inventory alerts, abandoned cart follow-up)
- Professional services (client reporting, project kickoff)
- SaaS (trial follow-up, usage monitoring)
- Real estate (listing syndication, lead nurturing)
- Healthcare (appointment reminders, patient intake)

Each example includes the complete filled-in directive plus notes on common challenges and optimization strategies.

---

## What Comes Next

You now have the foundation. The blank template, the worked example, the common mistakes to avoid, and the quick-start guide to write your first directive in 30 minutes.

Here's what happens after you write your first directive:

**Immediate next steps:**
- Reference Appendix D for execution templates (the code layer)
- Use Chapter 28's testing protocols to validate your directive
- Apply Chapter 29's self-annealing process to improve it

**After your first successful directive:**
- Write 2-3 more directives for related workflows
- Consider creating a metadirective (Appendix E) to orchestrate them
- Start building your directive library for common patterns

**As you scale:**
- Standardize your directive format across your organization
- Build directive review processes into your workflow
- Train your team to write directives using this template

The template in this appendix is not theoretical. It's the exact format used in production agentic systems processing thousands of workflows daily. The only difference between this template and a production directive at a company running DOE at scale is the content you put in it.

Your first directive won't be perfect. It will be good enough to test. Testing will make it better. Self-annealing will make it production-ready. But it all starts with filling in this template.

Copy it. Use it. Break it. Improve it. That's how agentic workflows are built.
