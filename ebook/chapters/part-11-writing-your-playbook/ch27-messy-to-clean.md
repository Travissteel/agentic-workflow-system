# Chapter 27: From Messy Process to Clean Directive

<!-- STATUS: Complete Draft -->
<!-- WORD TARGET: 4,000-5,000 words -->
<!-- ACTUAL WORD COUNT: ~5,973 words -->

## Chapter Summary
Most business processes exist as "tribal knowledge" or messy Google Docs that no one reads. This chapter teaches you how to audit your business, extract those processes with clinical precision, and translate them into machine-executable directives that actually get the work done.

---

## The Invisible Weight of the "Unsaid"

Every business has a "Directive Layer," whether you realize it or not. It’s the collection of rules, preferences, and "how-we-do-things-here" knowledge that keeps the lights on. 

But in most businesses, this layer is invisible. It’s "tribal knowledge" trapped in the heads of key employees. It’s a 40-page SOP written in 2019 that sits unread in a forgotten Google Drive folder. It’s the "shadow work" that disappears the moment your best admin takes a vacation.

This invisibility is the ceiling on your scale. You can't automate what you haven't defined, and you can't delegate what is invisible. 

To build an agentic business, we have to move that knowledge from the messy human brain into the **Clean Directive Layer**. This chapter is your guide to doing exactly that.

---

## The Messy Reality: What Business Processes Actually Look Like

Before we talk about clean directives, let's be honest about what most business processes look like in the wild. They're not neat flowcharts. They're chaos.

### The Anatomy of Business Mess

Here's what a typical "client onboarding" process looks like in a small agency:

**Email 1 (from Sales):** "Hey team, new client signed! Details attached. Can someone set them up?"

**Email 2 (from Sarah in Ops):** "Got it. What's their HubSpot tier again? The pricing doc is outdated."

**Email 3 (from Sarah, 2 hours later):** "Never mind, I'll just use last quarter's setup. Also, do they need Slack access or just email?"

**Email 4 (from Sales):** "Oh yeah, they want Slack. And can you copy their branding from the proposal? It's in the shared drive somewhere."

**Sarah's actual process (unwritten, in her head):**
1. Check the contract PDF (buried in email attachments)
2. Manually create a new folder in Google Drive (using last client's structure as template)
3. Copy-paste their logo from the proposal into 4 different places
4. Create HubSpot account with a password she'll send via Slack
5. Invite them to Slack (but remember to use their work email, not the personal one from the form)
6. Update the master tracking sheet (which has 3 tabs because the old one got too messy)
7. Send welcome email using template from 2023 (the 2024 one has a broken link)
8. Hope she didn't forget anything

This process lives entirely in Sarah's brain. There's no documentation. When Sarah takes vacation, onboarding stops. When Sarah makes a mistake, no one knows what the "correct" version should have been.

**This is the invisible weight of the "unsaid."**

### Common Patterns of Business Chaos

Every business has variations of these messy patterns:

**The Email Chain Hell:** A "process" that requires forwarding 6 different emails to get context, with critical information buried in "RE: RE: FWD: Quick question."

**The "Check With Sarah" Dependencies:** Any task that officially takes 10 minutes but actually takes 3 days because you're waiting for one person to answer a question only they know.

**The Frankenstein Spreadsheet:** A Google Sheet with 47 tabs, color-coding that made sense in 2019, and formulas that break if you look at them wrong. No one dares to clean it up because "it works."

**The Tool Graveyard:** You use Asana for projects, Trello for tasks, Monday.com for tracking (but only Karen uses it), Slack for everything urgent, and email for everything else. Information lives in all five places and nowhere.

**The "We'll Just Remember" Rituals:** Weekly team meetings where the same 3 questions get asked because no one wrote down the answers from last time.

### Why This Mess Matters

This chaos isn't just annoying. It's expensive:

- **Personnel Risk:** When Sarah quits, 6 months of institutional knowledge walks out the door
- **Quality Inconsistency:** Every client gets a slightly different experience depending on who does the onboarding
- **Scale Ceiling:** You can't hire fast enough because training new people takes 3 months of "shadow Sarah and take notes"
- **Opportunity Cost:** Sarah could be doing strategic work, but instead she's manually copying logos into folders

The good news? All of this mess can be translated into clean directives. But first, we need a systematic way to extract the truth from the chaos.

---

## Phase 1: The Tedium Map (Auditing for Automation)

Before you write your first directive, you need to find the right candidate. Most business owners make the mistake of trying to "automate the whole company" on day one. They start with the most complex, most strategic task they have. 

**This is a mistake.** Complexity is the enemy of automation. 

Instead, we use a tool called the **Tedium Map** to identify the "low-hanging fruit" that will provide the fastest ROI.

### How to Create Your Tedium Map

Take 30 minutes and list every task you and your team performed in the last seven days. Don't worry about being "professional"—write down everything from "answering refund emails" to "re-formatting the sales spreadsheet for the third time."

Now, plot each task on two axes:

1.  **Repetitiveness:** How often do you do this? (Daily, Weekly, Monthly)
2.  **Information Density:** Does this require "deep human empathy and creative strategy," or just "shuffling data between systems"?

### Identifying the Winners

**The "Agentic Sweet Spot":** Any task that is high-repetition and high-information-density. 
- **Examples:** Scoring 500 leads from a webinar, processing 100 invoices, cross-referencing competitor prices, drafting routine weekly reports, or triaging support tickets.

These tasks are the perfect candidates for directives. They follow predictable logic, they happen often enough to be a burden, and they involve enough data to make a human's eyes glaze over.

---

## The 5 Questions Method: Extracting Structure from Chaos

Before you can write a directive, you need to extract the real process from the mess. The 5 Questions Method forces you to confront what's actually happening, not what you think is happening.

Grab a notebook and a process you want to automate. Answer these five questions with brutal honesty.

### Question 1: "What's the ACTUAL trigger?"

Most people say: "We onboard clients when they sign up."

The truth is usually: "Sarah checks her email every morning, looks for contracts in the Sales inbox, and sometimes Sales Slack-messages her if it's urgent."

**Why this matters:** Your AI can't "just know" when to start. You need to define the trigger precisely.

**Good triggers:**
- "When a new row appears in the 'Signed Contracts' sheet"
- "Every Monday at 9am"
- "When a webhook is received from Stripe"

**Bad triggers:**
- "When someone tells me to start"
- "When I remember"
- "Whenever"

### Question 2: "What inputs do I ACTUALLY use?" (Not what I should use)

Don't list the official company wiki. List what you actually click on when you do this task.

**Example:**
- "The contract PDF in my email" (not the CRM, even though it should be there)
- "Last quarter's client folder as a template" (not the official template from 2019)
- "The pricing Google Doc that only me and Sarah can edit" (not the outdated public version)

**Pro tip:** Screen record yourself doing the task once. Note every tab you open, every file you reference, every time you copy-paste from somewhere. Those are your real inputs.

### Question 3: "What does SUCCESS actually look like?"

This is your Definition of Done, but stated from the perspective of the person who benefits.

**Bad success criteria:**
- "The client is set up"
- "Everything is done"
- "It works"

**Good success criteria:**
- "The client can log into HubSpot with their credentials, their brand colors are applied to all templates, their Slack workspace invite is sent, and their kickoff meeting is scheduled for next Tuesday"

**The test:** Could you hand this success criteria to a stranger and have them verify completion without asking you questions?

### Question 4: "What are the forks in the road?"

This is where most processes fail. Every real-world process has exceptions, edge cases, and "it depends" moments.

**The magic question:** "When I'm doing this task, what makes me stop and think?"

**Example forks:**
- "If the client is Enterprise tier, they get a dedicated Slack channel. If they're Starter, they just get added to the general client channel."
- "If their logo is a PNG with transparency, use it directly. If it's a JPG with a white background, ask the design team to clean it up first."
- "If the website field is blank, Google their company name + 'official site' and use the first result. If nothing relevant appears, mark for human review."

Write down every "if-then" decision you make, even the ones that seem obvious to you. They're not obvious to an AI.

### Question 5: "What's the human safety net?"

Even the best directive will encounter weird edge cases. Define when the AI should stop and ask for help.

**Examples:**
- "If the contract value is over $50,000, flag for manual review before proceeding"
- "If the email domain is from a government or military address (.gov, .mil), escalate to legal team"
- "If the automated logo extraction fails 3 times, create a ticket for design team and notify client success manager"

**The rule:** Your AI should never guess on high-stakes decisions. When in doubt, it should always escalate to a human.

---

## Phase 2: The 4-Step Extraction

Once you’ve picked a process—let's say "Qualifying New Leads"—don't try to sit down and write "The Perfect Directive" from scratch. You’ll get writer's block. Instead, follow this clinical extraction sequence to get the truth out of your head and onto the page.

### 1. The Brain Dump (The "Loom" Method)
Record your screen or yourself doing the task for 15 minutes. As you work, explain *why* you are making certain decisions. 
- *"I'm skipping this lead because their company size says 1-10 and we only want 50+."*
- *"I'm tagging this one as 'High Priority' because they mentioned 'Budget' in the comments."*
This narration captures the "hidden logic" that you do automatically without thinking.

### 2. The Document Audit
Gather all the "messy" inputs. The old spreadsheets, the email templates, the login URLs, the brand voice guides. Look at the *real* data you use, not the idealized version in an SOP. If you use a specific Google Sheet to check pricing, that Sheet URL must be part of your audit.

### 3. The Objective Statement (The "Win")
Define exactly what "Success" looks like in a single sentence. 
- *Bad:* "Help me with the leads."
- *Good:* "Categorize every lead in the 'New' tab of the CRM as 'Qualified' or 'Unqualified' based on company size and industry, and move them to the appropriate folder."

### 4. The 'If-This-Then-That' Audit
Identify the forks in the road. This is where most people fail at process. They forget to tell the AI what to do when things *don't* follow the script.
- *"If the website is down, search for them on LinkedIn."*
- *"If the email is personal (Gmail/Hotmail), mark as 'Low Priority' unless the company name is recognizable."*

---

## Phase 3: Drafting the Clean Directive

A "Clean Directive" is the bridge between human intent and agentic execution. It is the training manual your AI employees will read every time they start a task. 

Every directive in the DOE (Directive Orchestration Execution) framework MUST follow this four-part structure.

### 1. Objective Statement
A one-sentence summary of what "Success" looks like. It should be imperative (starting with a verb) and measurable.
- **Example:** "Extract all line items from the provided PDF invoices and enter them into the 'Monthly Expenses' spreadsheet, ensuring the totals match the invoice amounts."

### 2. Input Specifications
What does the agent need to start? Be pedantic. If the agent needs a specific login, tell it exactly where to find it (usually in a `.env` file).
- URLs for the tools it needs.
- Reference documents (e.g., "Use `PRICING_GUIDE.pdf` for discount rules").
- Sample outputs (e.g., "Format the final CSV exactly like `sample_output.csv`").

### 3. Step-by-Step Process
The core of the directive. Use clear, imperative language. Start every step with a verb: "Search," "Extract," "Compare," "Draft," "Verify."
- **Good:** "Step 1: Open the 'Invoices' folder. Step 2: For each file, identify the 'Total Amount Due'."
- **Bad:** "You should probably look at the invoices and find the totals."

### 4. Definition of Done (DoD)
This is the checklist the **Tester Agent** uses to verify the work. If the work doesn't meet this checklist, the task is not complete.
- [ ] Every line item is extracted.
- [ ] Totals in the spreadsheet match the PDF.
- [ ] Any invoice with a 'Discrepancy' is flagged for human review.

---

## Modular Design: Why Smaller is Smarter

One of the biggest mistakes newcomers make is trying to write a "Master Directive" that runs their entire company. They build a 50-step monster that tries to do lead gen, sales outreach, and reporting all in one file.

**Don't do it.** 

Modular directives are the key to a scalable AI system. Think of your business processes like LEGO bricks. Each brick should do one thing perfectly. 

### The Rule of Three
If your process has more than 10 steps, or if it involves more than three distinct "systems" (e.g., CRM, Browser, and Spreadsheet), break it into smaller directives.

**Instead of `Manage_Sales.md`, build:**
1.  `Lead_Discovery.md`: Finds the leads.
2.  `Lead_Enrichment.md`: Finds their email and LinkedIn.
3.  `Outreach_Drafting.md`: Writes the personalized email.

### The Benefits of Modularity:
- **Easier Debugging:** If the emails look weird, you know the bug is in `Outreach_Drafting.md`. You don't have to search through a giant file.
- **Reuse:** You can use `Lead_Discovery.md` for a different project without changing a single line of code.
- **Swapping Specialists:** You can have a "Creative Specialist" run the outreach and a "Data Specialist" run the enrichment.

---

## Real-World Walkthrough: Client Onboarding (The Full Journey)

Let's take the messy client onboarding process from earlier and walk through the complete transformation from chaos to clean directive.

### The "Before" State (Painful Detail)

Sarah's current process involves **15 different tools** and **23 manual steps**:

**Tools involved:**
1. Gmail (to find the contract)
2. Google Drive (create folder structure)
3. HubSpot (create account)
4. Slack (send invites)
5. Calendly (schedule kickoff)
6. Canva (download logo from proposal)
7. Google Sheets (update tracking spreadsheet)
8. Notion (create project workspace)
9. Figma (set up brand kit)
10. Loom (record welcome video)
11. DocuSign (verify signature)
12. Stripe (verify payment)
13. Intercom (enable support chat)
14. LastPass (generate secure password)
15. Gmail again (send welcome email)

**Actual time:** 90 minutes per client
**Stated time in SOP:** "About 30 minutes"
**Error rate:** 1 in 4 clients has something wrong (usually Slack invite to wrong email or missing folder permissions)

### Step 1: Apply the 5 Questions

**Q1: What's the trigger?**
- Currently: "Sales Slack-messages Sarah when contract is signed"
- Better trigger: "When a new row appears in 'Signed Contracts' sheet with Status='Awaiting Onboarding'"

**Q2: What are the real inputs?**
- Contract PDF (in Google Drive folder: `/Sales/2024/Contracts/`)
- Client details sheet (specific Google Sheet URL)
- Logo file (extracted from proposal PDF or website)
- Pricing tier (from contract)
- Preferred contact email (from HubSpot form submission)
- Onboarding checklist template (Google Doc)

**Q3: What does success look like?**
- Client has HubSpot login credentials (emailed)
- Slack workspace invite sent to work email
- Google Drive folder created with correct permissions
- Brand colors extracted and saved to Figma file
- Kickoff meeting scheduled for next available Tuesday 10am
- Tracking sheet row updated with "Onboarding Complete" + date
- Welcome email sent with Loom video embedded

**Q4: What are the forks?**
- If pricing tier = Enterprise → create dedicated Slack channel
- If pricing tier = Starter → add to #general-clients channel
- If logo is unavailable → use placeholder and flag for design team
- If preferred email is personal (Gmail/Yahoo) → use company domain from contract instead
- If contract value > $20k → assign dedicated success manager
- If contract value < $5k → assign to shared success queue

**Q5: What's the safety net?**
- If contract signature is missing → stop and alert Sales
- If payment verification fails → stop and alert Finance
- If any step fails 3 times → create Asana task for Sarah with error details
- If client responds negatively to welcome email → immediately notify success manager

### Step 2: Map the Clean Process

Now we organize the chaos into a logical flow:

**Phase A: Verification (Stop if anything fails)**
1. Verify contract signature exists in DocuSign
2. Verify payment received in Stripe
3. Extract client details from contract PDF

**Phase B: Setup (Core onboarding)**
4. Create Google Drive folder using template structure
5. Generate secure password in LastPass
6. Create HubSpot account with credentials
7. Extract brand colors from logo/website
8. Create Figma brand kit with colors + logo
9. Determine Slack strategy (dedicated channel vs general)
10. Send Slack invite to work email

**Phase C: Scheduling & Communication**
11. Find next available Tuesday 10am slot in Calendly
12. Send calendar invite with Zoom link
13. Record personalized Loom welcome (using script template)
14. Send welcome email with: credentials + Loom + calendar invite

**Phase D: Finalization**
15. Update tracking sheet with all details
16. Create Notion project workspace
17. Assign success manager based on contract value
18. Set 48-hour follow-up reminder

### Step 3: Write the Clean Directive

```markdown
# Directive: Client Onboarding Automation

## Objective
Onboard new signed clients by provisioning all required tools, sending credentials and welcome materials, and scheduling their kickoff meeting—all within 2 hours of contract signature.

## Inputs
- **Signed Contracts Sheet:** [Google Sheet URL]
  - Required columns: Client Name, Contact Email, Company Domain, Pricing Tier, Contract Value, Contract PDF URL
- **Folder Template:** `/Templates/Client_Onboarding_Structure/`
- **Welcome Email Template:** `assets/welcome-email-template.html`
- **Loom Script Template:** `assets/loom-script.md`
- **Credentials:**
  - `HUBSPOT_API_KEY` (for account creation)
  - `SLACK_WORKSPACE_TOKEN` (for invitations)
  - `CALENDLY_API_KEY` (for scheduling)
  - `LASTPASS_CLI_TOKEN` (for password generation)

## Process

### Phase A: Verification
1. **Check for new clients:** Query 'Signed Contracts' sheet for rows where `Status = "Awaiting Onboarding"`
2. **Verify signature:** Use DocuSign API to confirm signature status = "Completed"
   - If missing: Update Status to "Signature Required" and alert Sales team via Slack
   - If present: Continue
3. **Verify payment:** Use Stripe API to confirm payment status = "Paid"
   - If unpaid: Update Status to "Payment Required" and alert Finance team
   - If paid: Continue
4. **Extract client data:** Parse contract PDF to extract:
   - Client legal name
   - Primary contact name
   - Work email (use company domain, not personal)
   - Phone number
   - Pricing tier (Starter/Growth/Enterprise)

### Phase B: Provisioning
5. **Create folder structure:**
   - Duplicate `/Templates/Client_Onboarding_Structure/` to `/Clients/2024/[Client Name]/`
   - Set permissions: Client contact = Editor, Internal team = Owner
6. **Generate credentials:**
   - Use LastPass CLI to generate 16-character password
   - Format: `[ClientName]_Hub_2024_[Random]`
7. **Create HubSpot account:**
   - POST to HubSpot API with client details
   - Assign tier-appropriate permissions
   - Save login credentials to LastPass vault
8. **Extract branding:**
   - Use Playwright to visit client website
   - Extract primary brand color (most common color in header/logo)
   - Download logo in highest resolution available
   - If website unavailable: Use placeholder and flag for design team
9. **Create Figma brand kit:**
   - Duplicate Figma template file
   - Upload client logo
   - Set brand color variables
   - Generate shareable link

### Phase C: Slack Strategy
10. **Determine channel setup:**
    - If `Pricing Tier = "Enterprise"`: Create dedicated channel `#client-[company-name]`
    - If `Pricing Tier = "Starter" OR "Growth"`: Add to `#general-clients`
11. **Send Slack invite:**
    - Use Slack API to send workspace invite
    - Recipient: Work email (never personal email)
    - Include welcome message with Figma brand kit link

### Phase D: Scheduling
12. **Find available slot:**
    - Query Calendly for next available Tuesday at 10:00 AM AEST
    - If no Tuesday slots in next 14 days: Use next available Wednesday
13. **Send calendar invite:**
    - Create Zoom meeting link
    - Send invite to: Client contact + assigned success manager
    - Include: Agenda, Zoom link, "What to prepare" doc

### Phase E: Communication
14. **Record Loom video:**
    - Use `assets/loom-script.md` as script template
    - Personalize with client name and specific use case from contract
    - Upload to Loom and set permissions to "Anyone with link"
15. **Send welcome email:**
    - Use `assets/welcome-email-template.html`
    - Replace variables: `{CLIENT_NAME}`, `{HUBSPOT_LOGIN}`, `{TEMP_PASSWORD}`, `{LOOM_URL}`, `{KICKOFF_DATE}`
    - Attach: Brand kit PDF export from Figma
    - CC: Assigned success manager

### Phase F: Finalization
16. **Update tracking sheet:**
    - Set `Status = "Onboarding Complete"`
    - Fill columns: Onboarding Date, Success Manager, HubSpot ID, Slack Channel
17. **Create Notion workspace:**
    - Duplicate project template
    - Link to Google Drive folder and Figma file
18. **Assign success manager:**
    - If `Contract Value > $20,000`: Assign dedicated manager (round-robin from Enterprise team)
    - If `Contract Value <= $20,000`: Assign to shared queue
19. **Set follow-up reminder:**
    - Create Asana task for success manager: "Check in with [Client Name]"
    - Due date: 48 hours from onboarding completion

## Definition of Done
- [ ] Client has received HubSpot credentials via email
- [ ] Client has received Slack workspace invite to work email
- [ ] Client has confirmed calendar invite for kickoff meeting
- [ ] Google Drive folder exists with correct permissions
- [ ] Figma brand kit is created and linked in Notion
- [ ] Tracking sheet row shows "Onboarding Complete" status
- [ ] Success manager has been assigned and notified
- [ ] Welcome email sent with all attachments and links functional
- [ ] Loom video is accessible and embedded in welcome email

## Error Handling
- **If signature verification fails:** Stop process, update Status to "Signature Required", alert Sales via `#sales-alerts` Slack channel
- **If payment verification fails:** Stop process, update Status to "Payment Required", alert Finance via `#finance-alerts`
- **If logo extraction fails:** Continue with placeholder logo, create Asana task for design team with client website URL
- **If any step fails 3 consecutive times:** Stop process, create high-priority Asana task for Sarah with full error log, send Slack notification to `#onboarding-errors`
```

### Step 4: The Transformation Results

**Before automation:**
- Time per client: 90 minutes
- Error rate: 25%
- Sarah's capacity: ~5 clients per day
- Training time for new team member: 3 months
- Client feedback: "Onboarding was slow and confusing"

**After automation:**
- Time per client: 8 minutes (mostly waiting for API calls)
- Error rate: < 2% (only when external APIs fail)
- System capacity: 50+ clients per day
- Training time: 1 hour to understand directive + error handling
- Client feedback: "Onboarding was seamless and professional"

**Sarah's new role:** Instead of manually processing clients, Sarah now manages exception handling (the 2% edge cases) and focuses on process improvements.

This is the power of clean directives.

---

## Example: From Tribal Knowledge to Clean Directive

Let's look at a real transformation. 

### Before (The Tribal Knowledge)
*"Hey, when new people sign up for the newsletter, just look them up and see if they look like a good fit for our agency. If they do, send them that one email we wrote about the case study. Make sure you check if they are in Australia though, we can't help people outside Australia yet."*

### After (The Clean Directive)

```markdown
# Directive: New Newsletter Lead Qualification

## Objective
Qualify new newsletter subscribers and send relevant case studies to high-fit prospects.

## Inputs
- Newsletter Subscriber List (Google Sheet URL)
- Agency Case Study PDF (file:///assets/case-study.pdf)
- Outreach Template (file:///assets/outreach-email.txt)

## Process
1.  **Identify New Leads:** Check the 'Newsletter' sheet for rows marked 'Status: New'.
2.  **Verify Location:** Use the 'Playwright' tool to search for the subscriber's company on LinkedIn/Google.
    - If the company is NOT based in Australia, mark as 'Status: Discarded' and STOP.
3.  **Analyze Fit:** Check if company size is > 10 employees.
4.  **Draft Outreach:** If 'Australia' AND '> 10 employees', draft a personalized email using the Outreach Template.
    - Mention one specific detail from their website to prove it's not a template.
    - Attach the Agency Case Study PDF.
5.  **Finalize:** Set row 'Status' to 'Qualified - Drafted'.

## Definition of Done
- [ ] Every 'New' subscriber row is updated to 'Discarded' or 'Qualified - Drafted'.
- [ ] Location is verified for every qualified lead.
- [ ] Drafted emails include a specific website detail.
```

---

> [!TIP]
> **The 'Rubber Duck' Test**
> If you are struggling to write a process, explain it to a non-technical friend or your AI Orchestrator. If they can understand the steps without seeing your screen, you finally have a clean process. 

---

---

## Common Pitfalls (And How to Avoid Them)

Even with the 5 Questions Method and a step-by-step extraction process, most people make the same mistakes when writing their first directives. Here are the most common traps—and how to sidestep them.

### Pitfall 1: Over-Simplifying (The "It's Easy" Trap)

**What it looks like:**
```markdown
## Process
1. Get the client details
2. Set them up in all systems
3. Send welcome email
```

**Why it's a problem:** This isn't a directive, it's a to-do list. There's no detail on *how* to do any of these steps. An AI (or a new employee) would have no idea where to start.

**The fix:** If you can't hand your directive to a smart stranger and have them execute it without asking questions, it's too vague. Add the "how" to every step.

**Better version:**
```markdown
1. Extract client details from row in 'Signed Contracts' sheet (columns: Name, Email, Tier)
2. Create HubSpot account via API POST to /accounts/create endpoint
3. Send welcome email using template at assets/welcome.html
```

**The test:** "Could I hand this to a capable intern on their first day?"

### Pitfall 2: Over-Complicating (The "Future-Proofing" Trap)

**What it looks like:**
A 50-step directive that handles every possible edge case you can imagine, including:
- What to do if the client is based on Mars
- How to handle a client whose legal name has emoji characters
- Backup procedures if the internet goes down globally

**Why it's a problem:** You're trying to solve problems that haven't happened yet. The directive becomes so complex that it's unmaintainable, and the AI gets confused by the sheer volume of branching logic.

**The fix:** Start simple. Handle the 95% case first. Add edge cases only *after* you encounter them in real usage.

**The rule:** If an edge case hasn't happened in the last 6 months of manual operation, don't build logic for it yet. Wait until it happens, then add it to the directive.

### Pitfall 3: Confusing "Current Tool" with "Actual Goal"

**What it looks like:**
```markdown
## Objective
Log into the Acme CRM, click the "New Lead" button, fill in the form fields, and click Submit.
```

**Why it's a problem:** This directive is married to one specific tool (Acme CRM). If you switch CRMs next month, the entire directive becomes useless. You've documented *how you currently do it*, not *what you're trying to achieve*.

**The fix:** State objectives in tool-agnostic language. Describe the outcome, not the clicks.

**Better version:**
```markdown
## Objective
Create a new lead record in the CRM with fields: Name, Email, Company, Lead Source, and Status.

## Inputs
- CRM_TYPE: Currently "Acme CRM" (if changed, update credentials in .env)
- CRM_API_ENDPOINT: [API URL]
```

Now if you switch from Acme to HubSpot, you only update the inputs and API calls, not the entire directive logic.

**The test:** "If we switched tools tomorrow, would the objective statement still be true?"

### Pitfall 4: Vague Success Criteria (The "I'll Know It When I See It" Trap)

**What it looks like:**
```markdown
## Definition of Done
- [ ] Everything looks good
- [ ] Client is happy
- [ ] No obvious errors
```

**Why it's a problem:** These are subjective. Your tester agent (or a new team member) can't verify "looks good." Different people will have different standards.

**The fix:** Make success criteria binary (yes/no) and verifiable without human judgment.

**Better version:**
```markdown
## Definition of Done
- [ ] Client record exists in CRM with non-null values in all required fields
- [ ] Welcome email sent to client's work email address (verified in sent folder)
- [ ] Calendar invite accepted or pending (not declined)
- [ ] Tracking sheet row updated with Status = "Onboarding Complete" and today's date
```

**The test:** "Could a robot verify this without asking for clarification?"

### Pitfall 5: Ignoring the Unhappy Path

**What it looks like:**
A directive that assumes everything will work perfectly:
- APIs never timeout
- Files are always where they should be
- Users always fill out forms correctly

**Why it's a problem:** In the real world, things break. If your directive doesn't handle errors, your AI will either guess (bad) or crash (worse).

**The fix:** For every critical step, add an "If this fails" clause.

**Pattern:**
```markdown
3. **Download contract PDF:**
   - Fetch from URL in 'Contract_PDF_URL' column
   - Save to /temp/contracts/[client-id].pdf
   - **If download fails:** Retry up to 3 times with 5-second delay
   - **If still failing:** Send Slack alert to #finance-team with client name and PDF URL, mark Status as "Contract Unavailable", STOP process
```

**The rule:** Every step that touches an external system (API, file download, web scraping) needs a failure handler.

---

┌─────────────────────────────────────────────────────┐
│  DOWNLOAD THIS TEMPLATE                             │
│                                                      │
│  Get the Blank Directive Template:                   │
│  travissteel.net/the-last-employee/resources#directive-template  │
│                                                      │
│  Includes the "Objective, Inputs, Process, DoD"      │
│  structure ready to fill in for your next workflow.  │
└─────────────────────────────────────────────────────┘

---

## Try It Yourself: Your First Extraction (Guided Exercise)

It's time to transform one of your own messy processes into a clean directive. Follow this step-by-step exercise to create your first extraction.

### Step 1: Pick Your Process (5 minutes)

Choose a task that meets these criteria:
- You do it at least once per week
- It takes 30-60 minutes each time
- It's mostly "data shuffling" or "routine checking" (not deep creative work)
- You find yourself thinking "I wish I didn't have to do this again"

**Good examples:**
- Processing customer support tickets from shared inbox
- Creating weekly reports from multiple data sources
- Qualifying leads from webinar signups
- Invoicing clients from completed project spreadsheet
- Updating CRM after sales calls

**Bad examples (too creative/strategic for first directive):**
- Writing marketing copy
- Designing new product features
- Making hiring decisions

Write down your chosen process here: ___________________________

### Step 2: The Loom Brain Dump (15 minutes)

Do the task one more time, but this time:

1. **Record your screen** using Loom, QuickTime, or even your phone pointing at your monitor
2. **Narrate as you work:** Explain your thinking out loud
   - "I'm opening this spreadsheet because..."
   - "I'm skipping this row because..."
   - "I'm copying this into Slack because..."
3. **Don't edit yourself:** Capture the messy reality, not the idealized version

**What to capture:**
- Every tab/tool you switch to
- Every decision point ("I check if X, then I do Y")
- Every time you reference something in your memory ("We always use the blue logo for enterprise clients")
- Every time you copy-paste from somewhere

When done, watch the video back and take notes on:
- All the tools you touched
- All the "rules" you mentioned
- All the places you got information from

### Step 3: Answer the 5 Questions (20 minutes)

Use your video + notes to answer these with brutal specificity:

**1. What's the ACTUAL trigger that starts this task?**

Not "when I need to" but "what specific event/time/signal."

Your answer: ___________________________

**2. What inputs do you ACTUALLY use?** (List the real URLs, file paths, logins)

- Input 1: ___________________________
- Input 2: ___________________________
- Input 3: ___________________________
- Input 4: ___________________________
- Input 5: ___________________________

**3. What does SUCCESS look like?** (Be so specific a stranger could verify it)

Your Definition of Done:
- [ ] ___________________________
- [ ] ___________________________
- [ ] ___________________________
- [ ] ___________________________

**4. What are your "if-then" forks?**

List every decision point:
- If ___________________________, then ___________________________
- If ___________________________, then ___________________________
- If ___________________________, then ___________________________

**5. When should the AI stop and ask for help?**

Escalation triggers:
- If ___________________________, alert ___________________________
- If ___________________________, alert ___________________________

### Step 4: Write Your First Directive (30 minutes)

Using the template below, fill in your answers from Step 3:

```markdown
# Directive: [Your Process Name]

## Objective
[One sentence describing success - start with a verb]

## Inputs
- **[Input 1 Name]:** [URL or file path]
- **[Input 2 Name]:** [URL or file path]
- **[Input 3 Name]:** [URL or file path]

## Process
1. **[Step 1 name]:** [Detailed action with specific tool/location]
   - If [condition]: [what to do]
   - If [condition]: [what to do]
2. **[Step 2 name]:** [Detailed action]
3. **[Step 3 name]:** [Detailed action]
[Continue for all major steps]

## Definition of Done
- [ ] [Specific, verifiable outcome 1]
- [ ] [Specific, verifiable outcome 2]
- [ ] [Specific, verifiable outcome 3]

## Error Handling
- **If [critical step] fails:** [Escalation action]
- **If [timeout/API error]:** [Retry logic or escalation]
```

### Step 5: The Quality Checklist (10 minutes)

Before you consider your directive "done," run it through this checklist:

**Clarity Check:**
- [ ] Could a smart stranger execute this without asking questions?
- [ ] Are all URLs/file paths specific (not "the spreadsheet" but actual URLs)?
- [ ] Does every step start with a clear action verb?

**Completeness Check:**
- [ ] Did I document the "obvious" steps that I do automatically?
- [ ] Did I include at least one "if-then" decision fork?
- [ ] Did I specify what to do when things fail?

**Verification Check:**
- [ ] Is my Definition of Done measurable (yes/no, not subjective)?
- [ ] Could my tester agent verify completion without human judgment?
- [ ] Did I specify exact outputs (file formats, field names, locations)?

**Simplicity Check:**
- [ ] Is this focused on ONE specific outcome (not a mega-process)?
- [ ] Did I avoid over-engineering for edge cases that haven't happened?
- [ ] Could this directive be executed in under 2 hours?

### Step 6: Test with a Human First (Optional but Recommended)

Before handing this to an AI:

1. Give your directive to a colleague or team member
2. Ask them to execute it without asking you any questions
3. Watch where they get confused or stuck
4. Update the directive to clarify those areas

This human test will reveal gaps in your documentation faster than any AI test.

---

**Congratulations!** You've just created your first clean directive. You've taken messy tribal knowledge and transformed it into something that can be executed consistently, delegated reliably, and automated eventually.

In the next chapter, we'll look at how to take these clean directives and add advanced patterns like branching logic, self-healing, and modular composition.

**Key Takeaway:** Directives are the "DNA" of your AI employees. By translating messy human processes into structured, modular directives, you make your business immune to personnel turnover and scalable by default. You are no longer managing people; you are managing the *systems* that run the work.
