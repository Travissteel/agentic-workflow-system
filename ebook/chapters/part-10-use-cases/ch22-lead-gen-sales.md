# Chapter 22: Lead Generation & Sales

<!-- STATUS: Complete Draft -->
<!-- WORD COUNT: 4,400+ words -->
<!-- WORD TARGET: 3,500-4,500 words -->

## Chapter Summary
Concrete lead gen and sales automation use cases with complete directives and real production examples from an actual agency pipeline.

---

Lead generation and sales are the lifeblood of any business, but they are also the most prone to "manual fatigue." Research shows that most sales teams spend 60% of their time on administrative tasks—researching prospects, cleaning CRM data, drafting follow-up emails, and updating pipeline stages. That leaves only 40% for actual selling: conversations, demos, and closing deals.

By applying agentic workflows, we can flip that ratio completely. We don't just automate the *sending* of messages; we automate the *thinking* behind who to message, what to say, and when to follow up. The result is a sales team that feels like it has 3x more people, without hiring anyone new.

This chapter covers four concrete use cases you can build and deploy this week—or package and sell to clients who need their sales engine overhauled. These aren't theoretical examples. I'll walk you through a real production system we built for our own agency, complete with costs, tool recommendations, and copy-paste-ready directives.

---

## Use Case 1: The Scrape & Qualify Pipeline

**The Problem:** Finding quality prospects is manual, slow, and inconsistent. A typical sales development rep spends hours each day searching LinkedIn, copying names into spreadsheets, hunting for email addresses, and trying to "guess" if each person is a good fit based on job title or company size. By the time they've researched 20 prospects, the day is over—and they haven't sent a single email.

Worse, the quality is inconsistent. One rep might be thorough and take 15 minutes per prospect. Another might rush and add anyone with a pulse. The pipeline fills up with low-quality leads that waste the closer's time.

Agentic workflows solve both problems: speed and consistency.

### The Real Architecture (From Our Agency Pipeline)

In our own agency, we built exactly this system using a combination of tools that costs about $0.30 per prospect and processes 100+ people per day on autopilot. Here's how it works:

**1. Trigger Layer: Google Sheets**
We start with a simple Google Sheets document where the team adds target prospects—just a company name and website URL. New rows in this sheet trigger the workflow. No fancy form, no CRM input screen. Just paste a name and hit Enter.

**2. Orchestration: n8n**
An n8n workflow monitors the Google Sheet every 5 minutes. When it detects a new row, it kicks off the research process. n8n acts as the central brain, managing the flow from research to enrichment to CRM delivery.

**3. AI Research: GPT-4**
GPT-4 does the heavy lifting. We send it the company website URL and ask it to:
- Scrape the homepage and About page
- Extract key information: what they do, who they serve, and what problems they solve
- Identify signals that match our Ideal Customer Profile (ICP): company size, tech stack, recent funding, job openings
- Generate a 150-250 word research summary that a human could use to personalize an outreach email

This takes about 15-20 seconds per prospect and costs roughly $0.15 in API calls.

**4. Lead Scoring & ICP Matching**
The orchestrator then scores the lead on a 1-100 scale based on:
- Industry fit (worth 30 points)
- Company size (worth 25 points)
- Technology signals (worth 20 points)
- Recent growth indicators—hiring, funding, expansion (worth 25 points)

Leads scoring 80+ are "hot." Leads scoring 60-79 go into a "nurture" list. Anything below 60 is archived.

**5. Email Personalization: 3 Variants**
For hot leads, GPT-4 generates three different email variants:
- **Variant A:** Direct value proposition ("We help [industry] companies reduce [pain point] by 40%")
- **Variant B:** Case study angle ("We just helped [similar company] achieve [result]")
- **Variant C:** Curiosity hook ("Most [job title] don't realize [insight]—here's why it matters")

The salesperson can pick whichever angle feels right for that prospect, or let Smartlead A/B test them automatically.

**6. CRM Delivery: HubSpot**
The final step pushes everything to HubSpot:
- Creates a new contact record
- Adds the research summary to the Notes field
- Tags the lead with the ICP score
- Enrolls them in the appropriate email sequence based on score

The entire process—from Google Sheet entry to CRM-ready lead with personalized emails—takes about 45 seconds and costs $0.30.

### The Complete Outreach Stack

To make this work end-to-end, we use a tightly integrated stack of tools:

**Smartlead** ([https://smartlead.ai?via=travis](https://smartlead.ai?via=travis))
This is our primary cold email engine. Smartlead lets you connect unlimited email accounts (we run 15 different sending domains), automatically warms them up with AI-generated engagement, and rotates inboxes to maximize deliverability. It also handles bounce management, reply detection, and unsubscribe processing. We send 500-1,000 cold emails per day through Smartlead without landing in spam.

**Instantly** (email warming companion)
While Smartlead has its own warmup, we also use Instantly for an extra layer of deliverability insurance. Instantly focuses specifically on inbox reputation: it sends and receives emails between a pool of real accounts to build sender history. We run our domains through Instantly for 2 weeks before sending any cold emails.

**GoHighLevel** ([https://www.gohighlevel.com/?fp_ref=rxwfh](https://www.gohighlevel.com/?fp_ref=rxwfh))
GHL acts as our client-facing dashboard and pipeline manager. While HubSpot is the backend CRM, GHL gives us visual pipeline boards, task automation, and integrated SMS follow-ups. When a lead replies to a cold email, GHL moves them to the "Replied" stage and triggers a Slack notification to the sales team.

**HubSpot** (the CRM backbone)
HubSpot stores everything: contacts, companies, deals, notes, and email history. The free tier is enough for most small teams. We use it because it integrates with everything and has rock-solid APIs. If you're already invested in Salesforce or Pipedrive, those work fine too—but HubSpot's free tier makes it the default choice for startups.

**Apollo.io** (optional: lead enrichment)
If you're starting with just a company name (no website URL), Apollo can enrich the record with contact info, employee count, tech stack, and recent news. We use Apollo for about 20% of our prospects where we need extra data. It costs about $0.10 per enrichment.

**n8n** (workflow orchestration)
n8n ties everything together. It's visual, self-hostable, and has pre-built nodes for all the tools above. We run n8n on a $12/month DigitalOcean droplet. If you prefer cloud-hosted, n8n Cloud starts at $20/month.

**The flow looks like this:**
```
Google Sheets → n8n detects new row → GPT-4 research → Lead scoring →
Email generation → Smartlead campaign → HubSpot contact created →
GHL pipeline stage set → Slack notification sent
```

### Rate Limiting & Cost Control

One critical detail: we implemented rate limiting to avoid hitting API quotas. GPT-4 allows 10,000 requests per minute, but HubSpot's free tier only allows 100 API calls per 10 seconds. We throttle n8n to process 10 prospects per minute, which keeps us safely under all limits.

We also track costs in a separate Google Sheet. Each workflow run logs:
- Prospect name
- GPT-4 API cost
- Apollo enrichment cost (if used)
- Total cost per lead

Over 6 months, our average cost per qualified lead landed at $0.28. Compare that to hiring an SDR at $50,000/year who can research maybe 30 leads per day. The ROI is absurd.

### The Complete Directive: Prospect Qualifier

Here's the actual directive we use, ready to copy and paste:

```markdown
# DIRECTIVE: Prospect Qualifier

## Objective
Identify and score 20 high-fit prospects in the [Target Industry] industry who match our Ideal Customer Profile (ICP).

## Inputs
- Google Sheet: "Prospect Pipeline" with columns [Company Name, Website URL]
- ICP Scoring Rubric (stored in n8n environment variables)
- HubSpot API credentials

## Process
1. **Monitor Trigger**
   - Check Google Sheet every 5 minutes for new rows
   - Extract Company Name and Website URL from each new entry

2. **Company Research**
   - Visit the company website homepage
   - Scrape the About page, Careers page, and latest blog posts
   - Extract: company size, industry, target customers, recent news
   - Generate a 150-250 word research summary highlighting:
     * What they do
     * Who they serve
     * Current challenges (inferred from job postings or blog topics)
     * Technology stack (visible from website footer or job descriptions)

3. **Lead Scoring**
   - Score the lead on a 1-100 scale using the ICP Rubric:
     * Industry match (30 points)
     * Company size 50-500 employees (25 points)
     * Uses [Target Tech Stack] (20 points)
     * Recent growth signals—hiring, funding, expansion (25 points)
   - Assign tier: Hot (80+), Warm (60-79), Cold (<60)

4. **Email Personalization**
   - For Hot and Warm leads only, generate 3 email variants:
     * Variant A: Direct value proposition
     * Variant B: Case study angle
     * Variant C: Curiosity/insight hook
   - Each email must be 4-6 sentences, reference specific company context, and end with a single clear CTA

5. **CRM Delivery**
   - Create contact in HubSpot with all extracted data
   - Add research summary to Notes field
   - Tag with ICP score and tier
   - Enroll Hot leads in "Cold Outreach Sequence A"
   - Enroll Warm leads in "Nurture Sequence B"

6. **Logging**
   - Write results to "Qualified Leads" tab in Google Sheet
   - Log API costs (GPT-4 + HubSpot + Apollo if used)

## Definition of Done
- 20 leads processed with ICP scores >60
- All Hot leads (80+) added to HubSpot with personalized emails
- Research summaries included in CRM notes
- Slack notification sent: "20 new leads qualified—12 Hot, 8 Warm"

## Error Handling
- If website is unreachable, mark lead as "Research Failed" and skip
- If HubSpot API fails, retry 3 times with 30-second delay
- If cost per lead exceeds $0.50, trigger alert to Slack

## Rate Limiting
- Process maximum 10 leads per minute to stay under API limits
```

### Expected Results

When this workflow is running, you get:
- **100+ prospects researched per day** with zero human effort
- **3x improvement in lead quality** because the AI evaluates every prospect against the same ICP rubric
- **$0.30 per prospect** vs. $15-25 per prospect for manual research (based on SDR hourly wage)
- **Pipeline always full** without manual prospecting work

The sales team's job shifts from "finding people to email" to "having conversations with qualified leads who already replied."

---

## Use Case 2: Follow-Up Automation

**The Problem:** Everyone in sales knows "the fortune is in the follow-up," but follow-ups are where deals go to die. Standard email sequences send generic "just checking in" messages that get ignored. Salespeople forget to follow up after a call. Prospects who showed interest 3 weeks ago go cold because no one circled back.

The issue isn't that follow-ups don't happen—it's that they're generic, delayed, or both. A "just checking in" email has a 1% response rate because it adds zero value to the prospect. By the time a salesperson gets around to drafting a personalized follow-up, the prospect has moved on.

### The Architecture

Here's how we automate follow-ups while keeping them genuinely personalized:

**1. Trigger: CRM Status Change**
A lead changes status in the CRM—"Replied but not booked," "Demo completed—decision pending," or "Went cold after proposal." This status change triggers the workflow.

**2. Context Gathering**
The orchestrator pulls:
- Previous email thread (last 3 messages)
- Notes from the last call (if available)
- Prospect's LinkedIn activity from the past 2 weeks (recent posts, job changes, company news)

**3. AI Follow-Up Drafting**
The AI (we prefer advanced reasoning models like Gemini 2.5 Pro or Claude Opus for writing tasks) drafts a follow-up that:
- References a specific challenge or goal mentioned in the previous conversation
- Ties in something recent—a LinkedIn post the prospect made, a company announcement, or an industry trend
- Offers one piece of actionable advice or a relevant resource (blog post, case study, calculator)
- Ends with a low-pressure CTA: "If this is still a priority, let me know—happy to chat this week."

The email is 3-4 sentences, max. Short, relevant, valuable.

**4. Quality Check (Tester Agent)**
Before the email goes anywhere, a tester agent reviews it against these criteria:
- Does it sound like a template? (Fail if yes)
- Does it reference specific context from the previous interaction? (Fail if no)
- Are there any broken links or placeholder text? (Fail if yes)

If it passes, the email is saved to the salesperson's Gmail Drafts folder. If it fails, the workflow alerts the stuck agent for human review.

**5. Human Review**
The salesperson gets a Slack notification: "Draft follow-up for [Prospect Name] is ready in your Gmail Drafts." They open it, read it in 10 seconds, maybe tweak one sentence, and hit Send.

The AI did 95% of the work. The human retains the final 5%—the "kill switch" to ensure the tone is perfect.

### Tool Integration

**Smartlead for Sequence Management**
If the follow-up is part of a multi-touch sequence (e.g., "3 touches over 2 weeks"), Smartlead handles the scheduling and delivery. We still let the AI write each individual message, but Smartlead manages the timing.

**GoHighLevel for Trigger Management**
GHL watches for pipeline stage changes and triggers the follow-up workflow. It also tracks engagement: if the prospect opens the follow-up email 3+ times but doesn't reply, GHL escalates them to "High Intent—Call Immediately."

**AI for Personalization**
We use advanced LLMs (via API) for follow-up drafting because they are better at maintaining conversational tone and avoiding "AI slop" phrases. Gemini 2.x and Claude 3.x tend to sound more human than traditional models.

### The Complete Directive: Value-Add Follower

```markdown
# DIRECTIVE: Value-Add Follower

## Objective
Draft a personalized follow-up email for [Lead Name] that adds value and reignites the conversation.

## Inputs
- CRM record for [Lead Name]
- Email thread (last 3 messages)
- LinkedIn profile URL
- Notes from last call (if available)

## Process
1. **Summarize Previous Interaction**
   - What was the main pain point or goal discussed?
   - What was the prospect's timeline or next step?
   - Why did the conversation stall? (e.g., "needed to check with team," "decision delayed," "went dark")

2. **Gather New Context**
   - Visit LinkedIn profile
   - Check for recent posts, job changes, or company announcements in the past 14 days
   - Identify one "new" piece of context that's relevant to the original conversation

3. **Draft Follow-Up**
   - Opening: Reference the last conversation ("When we spoke about [pain point]...")
   - Bridge: Tie in the new context ("I saw your post about [topic]—that's exactly the challenge we help with")
   - Value: Offer one piece of actionable advice or a resource (blog post, case study, ROI calculator)
   - CTA: Low-pressure close ("If this is still a priority, let me know—happy to chat this week")
   - Keep it 3-4 sentences total

4. **Quality Check**
   - Does it sound like a template? (Fail if yes)
   - Does it reference specific context? (Fail if generic)
   - Are there any broken links or placeholder text? (Fail if yes)
   - Pass/Fail decision

5. **Delivery**
   - If Pass: Save to salesperson's Gmail Drafts folder
   - If Fail: Alert stuck agent for human review
   - Send Slack notification: "Draft follow-up for [Lead Name] ready"

## Definition of Done
- A high-quality, personalized follow-up draft waiting in Gmail Drafts
- Tester agent verified it doesn't sound templated
- Salesperson can send with <10 seconds of review

## Expected Response Rate
- 15-25% reply rate (vs. 1-3% for generic "checking in" emails)
```

### Expected Results

When this workflow is live:
- **3x higher response rates** compared to standard sequences (15-25% vs. 1-3%)
- **90% of drafting work automated**—the salesperson only reviews and clicks Send
- **Follow-ups happen within hours, not days**—no more "I'll get to it later" delays
- **Prospects feel like you remembered them**—the personalization is genuine, not templated

---

## Use Case 3: Proposal Generation

**The Problem:** Drafting a custom proposal after a discovery call takes 1-2 hours of deep work. You have to review the call notes, decide which service package fits, calculate ROI projections, and write persuasive copy explaining why your solution solves their specific problem.

Most salespeople delay this. They say, "I'll send it next week," and by the time they finally deliver the proposal, the prospect has gone cold or chosen a competitor. Speed matters. Proposals sent within 24 hours of the discovery call have a 40% higher close rate than proposals sent after 3+ days.

Agentic workflows eliminate the delay. Proposals get generated in 15 minutes, while the prospect is still hot.

### The Architecture

**1. Trigger: Discovery Call Transcript or Intake Form**
After a discovery call, the salesperson uploads the transcript (Zoom, Gong, or Fireflies auto-generates this) to a shared folder. Or, if you use intake forms, a completed form submission triggers the workflow.

**2. Data Extraction**
The orchestrator extracts:
- **Pain Points:** What problems is the prospect trying to solve?
- **Goals:** What does success look like for them?
- **Timeline:** When do they need this implemented?
- **Budget Signals:** Did they mention a budget range or ask about pricing tiers?
- **Decision Makers:** Who else is involved in the decision?

**3. Solution Mapping**
Based on the extracted data, the AI selects the appropriate service package:
- **Tier 1 (Starter):** Basic implementation, 2-week delivery
- **Tier 2 (Professional):** Full implementation + training, 4-week delivery
- **Tier 3 (Enterprise):** Custom build + ongoing support, 8-week delivery

If the pain points and budget signals suggest Tier 2, that package becomes the default recommendation. The AI can also flag "good upsell opportunity to Tier 3" if the prospect mentioned complex requirements.

**4. ROI Calculation**
The AI calculates estimated ROI using formulas you've pre-defined:
- If they're spending 20 hours/week on manual data entry, and your automation saves 15 hours, that's $780/week saved (at $50/hour fully loaded cost)
- Over 12 months: $40,560 saved
- Your fee: $8,000
- ROI: 5x return

These calculations populate dynamically in the proposal.

**5. Proposal Drafting**
The AI takes your proposal template (a Google Doc or Word doc with placeholders like `[CLIENT_NAME]`, `[PAIN_POINT_1]`, `[ROI_CALCULATION]`) and fills in all the blanks with the specific data from this prospect.

It also writes a custom Executive Summary section (2-3 paragraphs) explaining:
- Why this prospect is a great fit for this solution
- How the solution directly addresses their top 3 pain points
- What success looks like 90 days after implementation

**6. Final Delivery**
The workflow generates a PDF, saves it to a shared folder, and sends a Slack message: "Proposal for [Client Name] is ready for review." The salesperson gives it a 2-minute glance, makes any final tweaks, and sends it while the prospect is still in the discovery call debrief mindset.

### The Complete Directive: Proposal Builder

```markdown
# DIRECTIVE: Proposal Builder

## Objective
Create a custom, professional proposal for [Client Name] within 15 minutes of discovery call completion.

## Inputs
- Discovery call transcript (Zoom, Gong, or Fireflies)
- Proposal template (Google Doc with placeholders)
- Service package pricing matrix
- ROI calculation formulas

## Process
1. **Extract Key Data**
   - Pain Points: What problems are they trying to solve? (list top 3)
   - Goals: What does success look like? (specific outcomes)
   - Timeline: When do they need this delivered?
   - Budget Signals: Did they mention a budget or ask about pricing?
   - Decision Makers: Who else is involved?

2. **Select Solution Package**
   - Based on pain points and budget signals, recommend:
     * Tier 1 (Starter): $3,000–$5,000, basic implementation
     * Tier 2 (Professional): $8,000–$12,000, full implementation + training
     * Tier 3 (Enterprise): $20,000+, custom build + ongoing support
   - Flag upsell opportunities if requirements suggest higher tier

3. **Calculate ROI**
   - Identify time/cost savings from automation
   - Use formula: (Hours Saved per Week × Fully Loaded Hourly Cost × 52 weeks) ÷ Project Fee
   - Example: 15 hours saved/week × $50/hour × 52 = $39,000 saved ÷ $8,000 fee = 4.9x ROI

4. **Populate Proposal Template**
   - Replace all placeholders: [CLIENT_NAME], [PAIN_POINT_1], [GOAL_1], [ROI_CALCULATION], etc.
   - Write custom Executive Summary (2-3 paragraphs):
     * Why this client is a great fit
     * How solution addresses their top 3 pain points
     * What success looks like 90 days post-implementation

5. **Generate PDF**
   - Convert Google Doc to PDF
   - Save to shared folder: `/proposals/[CLIENT_NAME]_[DATE].pdf`

6. **Notify Salesperson**
   - Send Slack message: "Proposal for [Client Name] ready for review"
   - Include link to PDF

## Definition of Done
- A polished, personalized 3-5 page proposal document
- All placeholders replaced with client-specific data
- ROI calculation included and accurate
- Salesperson notified within 15 minutes of call completion

## Quality Checks
- No placeholder text remaining (e.g., no `[CLIENT_NAME]` visible)
- ROI calculation uses correct hourly cost assumptions
- Recommended package matches pain points and budget signals
- Executive Summary references specific challenges from call
```

### Expected Results

- **Proposals delivered within 15 minutes** of discovery call
- **40% higher close rate** vs. proposals sent after 3+ days
- **Consistent professional quality**—no more rushed, typo-filled proposals
- **No delays**—the prospect gets the proposal while still excited about the solution

---

## Use Case 4: CRM Data Hygiene (New)

**The Problem:** CRM data degrades over time. Duplicates pile up. Contact info becomes outdated. Required fields stay blank. Leads marked "Hot" 6 months ago are still sitting there, untouched.

Dirty CRM data costs sales teams 550 hours per year (according to HubSpot's research). Reps waste time calling dead leads, sending emails to invalid addresses, and manually merging duplicate records.

### The Architecture

**1. Scheduled Weekly Scan**
Every Monday at 6 AM, a workflow scans the entire CRM for common issues:
- Duplicate contacts (same email or same name + company)
- Missing required fields (phone, job title, company size)
- Stale leads (no activity in 90+ days)
- Invalid email addresses (bounced in last 3 sends)

**2. Automated Fixes**
For duplicates, the AI intelligently merges records:
- Keeps the record with the most complete data
- Merges notes and activity history
- Archives the duplicate

For missing fields, the AI enriches data using Apollo or Clearbit:
- Pulls LinkedIn profile to fill job title
- Uses domain lookup to add company size and industry

For stale leads, the AI flags them for re-engagement or archival:
- If they were once "Hot" but went cold, move to "Re-Engage" campaign
- If they never responded to 3+ touches, archive

**3. Weekly Report**
The workflow generates a "CRM Health Report" and sends it to the sales manager:
- 47 duplicates merged
- 132 missing fields enriched
- 89 stale leads archived
- 23 leads flagged for re-engagement
- Current CRM health score: 87/100

### Expected Results

- **550 hours per year saved** on manual data cleanup
- **15% increase in email deliverability** (fewer bounces from invalid addresses)
- **Sales team confidence**—they trust the data in the CRM

---

## The Complete Lead Gen Stack

Here's how all the tools fit together in a production-ready lead gen engine:

### Recommended Tools & Integrations

**Smartlead** ([https://smartlead.ai?via=travis](https://smartlead.ai?via=travis))
**Purpose:** Cold email at scale with unlimited sending accounts and AI warmup
**Cost:** $39/month (basic) to $149/month (agency)
**Why we use it:** Best-in-class deliverability, automated inbox rotation, and built-in reply detection. We send 500-1,000 cold emails per day without hitting spam folders.

**Instantly** (Email warming and deliverability)
**Purpose:** Email warmup service that builds sender reputation
**Cost:** $30/month per inbox
**Why we use it:** Pairs perfectly with Smartlead to ensure new domains don't land in spam. Run new sending domains through Instantly for 2 weeks before sending cold emails.

**GoHighLevel** ([https://www.gohighlevel.com/?fp_ref=rxwfh](https://www.gohighlevel.com/?fp_ref=rxwfh))
**Purpose:** All-in-one CRM, pipeline management, and client dashboard
**Cost:** $97/month (starter) to $297/month (unlimited)
**Why we use it:** Visual pipeline boards, automated SMS follow-ups, and a white-label client portal. Perfect for agencies who want to offer "CRM as a service" to clients.

**HubSpot** (Free tier available)
**Purpose:** Enterprise-grade CRM backbone with rock-solid APIs
**Cost:** Free (up to 1,000 contacts) to $800+/month (enterprise)
**Why we use it:** The free tier is incredibly powerful, and it integrates with every tool in the stack. If you're already on Salesforce or Pipedrive, stick with those—but HubSpot's free tier makes it the default for startups.

**Apollo.io**
**Purpose:** Lead enrichment and prospecting database with 275M+ contacts
**Cost:** $49/month (basic) to $149/month (organization)
**Why we use it:** When we only have a company name, Apollo enriches the record with contact info, tech stack, employee count, and recent news. $0.10 per enrichment.

**Advanced LLM Pricing (Gemini/Claude/GPT-4o)**
**Cost:** Gemini: $0.075 per million input tokens; Claude: $3 per million input tokens; GPT-4o: $5 per million input tokens
**Why we use it:** Advanced reasoning models for writing tasks (follow-ups, proposals), GPT-4o for research and data extraction. Both are excellent; pick based on tone preference.

**n8n** (Self-hosted or cloud)
**Purpose:** Visual workflow orchestration that ties everything together
**Cost:** Free (self-hosted) or $20/month (cloud starter)
**Why we use it:** Pre-built nodes for all the tools above, visual debugging, and self-hostable (we run ours on a $12/month DigitalOcean droplet).

### The Complete Flow

Here's how it all connects:

```
┌─────────────────────────────────────────────────────────────┐
│                     Google Sheets (Trigger)                 │
│                  New row = New prospect                     │
└────────────────────────┬────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────────┐
│                 n8n Workflow (Orchestrator)                 │
│  • Detects new row every 5 minutes                          │
│  • Extracts company name + website URL                      │
└────────────────────────┬────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────────┐
│              GPT-4 Research (AI Specialist)                 │
│  • Scrapes website (homepage, About, Careers)               │
│  • Generates 150-250 word company summary                   │
│  • Scores lead against ICP (1-100 scale)                    │
│  • Creates 3 personalized email variants                    │
└────────────────────────┬────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────────┐
│           Smartlead Campaign (Outreach Engine)              │
│  • Adds high-scoring leads to cold email sequence           │
│  • Sends from rotated inbox pool                            │
│  • Tracks opens, clicks, replies                            │
└────────────────────────┬────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────────┐
│             HubSpot CRM (Data Repository)                   │
│  • Creates contact record with research notes               │
│  • Tags with ICP score                                      │
│  • Enrolls in sequence based on tier                        │
└────────────────────────┬────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────────┐
│          GoHighLevel (Pipeline Management)                  │
│  • Moves contact to "Cold Outreach" stage                   │
│  • Triggers Slack notification to sales team                │
│  • Watches for replies → moves to "Replied" stage           │
└─────────────────────────────────────────────────────────────┘
```

Every piece talks to every other piece. The data flows automatically from trigger to delivery, with zero manual handoffs.

---

## Try It Yourself: Build a Mini Version

Don't try to build the entire stack on Day 1. Start small and prove the concept.

**Week 1: Build the Core Research Loop**
1. Create a Google Sheet with 10 target prospects (just company name + website URL)
2. Use n8n (free trial) to detect new rows
3. Call GPT-4 API to research each company and generate a summary
4. Email yourself the results

**Cost:** $1.50 for 10 prospects (GPT-4 API)
**Time:** 2-3 hours to set up

**Week 2: Add Lead Scoring**
1. Define your ICP rubric (industry, company size, tech stack, growth signals)
2. Have GPT-4 score each lead on a 1-100 scale
3. Filter out leads scoring <60

**Week 3: Generate Personalized Emails**
1. For leads scoring 80+, have GPT-4 generate 3 email variants
2. Save them to a Google Sheet
3. Manually review and send 5 of them

**Week 4: Connect the CRM**
1. Sign up for HubSpot free tier
2. Use n8n's HubSpot node to create contacts automatically
3. Add research summaries to the Notes field

**Week 5: Add Smartlead**
1. Connect Smartlead to your workflow
2. Set up a simple 3-email sequence
3. Let it send 20 cold emails

By Week 5, you've built a working lead gen engine that processes prospects automatically. Now you scale: add more prospects, tweak the ICP scoring, and refine the email copy based on reply rates.

---

## Key Takeaways

Agentic workflows in sales move the team from "data entry" to "deal closing" by handling the research, scoring, drafting, and follow-ups automatically.

The patterns in this chapter are:
1. **Trigger:** New prospect, status change, or scheduled scan
2. **Research:** AI gathers context from websites, LinkedIn, CRM
3. **Score/Decide:** AI evaluates fit and selects the next action
4. **Draft:** AI writes personalized outreach, follow-ups, or proposals
5. **Human Review:** Salesperson gets a 10-second review step before final send

You're not replacing salespeople. You're giving them superpowers. They spend their time on high-value activities—calls, demos, negotiations—while the AI handles the grunt work.

The best part? These workflows are sellable. If you're an agency or consultant, you can package any of these systems and deploy them for clients at $5,000–$15,000 per implementation. You build it once, deploy it for 10 clients, and collect recurring revenue for maintenance and optimization.

---

┌─────────────────────────────────────────────────────┐
│  DOWNLOAD THE LEAD GEN DIRECTIVE BUNDLE             │
│                                                      │
│  Get all 4 complete directives from this chapter:   │
│  • Prospect Qualifier                               │
│  • Value-Add Follower                               │
│  • Proposal Builder                                 │
│  • CRM Health Monitor                               │
│                                                      │
│  Ready to copy, paste, and deploy.                  │
│                                                      │
│  travissteel.net/the-last-employee/resources#lead-gen            │
└─────────────────────────────────────────────────────┘

---

**Next Chapter:** We'll look at content creation and marketing workflows—how to generate SEO-optimized blog posts, social media content, and email campaigns using the same agentic principles.
