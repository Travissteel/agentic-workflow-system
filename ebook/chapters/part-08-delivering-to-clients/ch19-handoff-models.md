# Chapter 19: The Four Handoff Models

**Status:** Complete Draft

---

## The Wrong Way to Deliver

You've built the perfect workflow. It scrapes leads, qualifies them with AI, and sends personalized outreach emails. Your client loves the demo. Then they ask the question:

"So... how do I get this?"

And you freeze.

Do you send them a zip file of Python scripts? Host it on your server and charge monthly? Build them a custom dashboard? Give them access to your Modal account?

Most consultants default to whatever they've done before. The technical consultant always sends GitHub repos. The agency always hosts it themselves. The solopreneur always builds a custom UI.

They're all leaving money on the table.

**The insight:** Different clients need different delivery models. The entrepreneur who wants to "own" the automation needs something different than the enterprise CMO who wants you to "just make it work." The technical founder needs different access than the operations manager who's never seen code.

One-size-fits-all delivery doesn't work. You either over-deliver (spending weeks building features they don't need) or under-deliver (handing them something they can't use).

This chapter solves that problem. I'll show you four delivery models that cover 99% of client situations, a decision tree to pick the right one, and pricing strategies for each.

By the end, you'll know exactly how to deliver any automation to any client in a way that maximizes both their success and your revenue.

---

## The Solution: Four Delivery Models

There are exactly four ways to hand off agentic workflows to clients. Each has different setup effort, maintenance requirements, and revenue potential:

### Model Comparison

| Model | Client Effort | Best For | Your Revenue | Client Access |
|-------|--------------|----------|--------------|---------------|
| **Hybrid Wrapper** | Minimal | 90% of clients | Setup fee + optional retainer | Full (visual n8n workflow) |
| **Managed Service** | Zero | Enterprise, non-technical | Monthly retainer (highest) | None (you run it) |
| **GitHub Codespace** | Medium | Technical users, developers | One-time setup fee | Full (code level) |
| **Manual Handover** | High | Internal teams, partners | Training fee (lowest) | Full (local files) |

Let's break down each model in detail.

---

## Model 1: Hybrid Wrapper (The Default Choice)

**What it is:** Your battle-tested Python workflow runs on Modal as an HTTP endpoint. The client triggers it from n8n (or Make/Zapier) with a visual workflow they can understand and modify.

**The three-layer architecture:**

1. **Outer Shell (n8n):** Visual workflow the client sees
   - Trigger: webhook, form submission, schedule, email
   - HTTP Request: calls your Modal endpoint
   - Final Action: send email, update CRM, post to Slack

2. **Inner Core (Modal):** Your Python logic they don't see
   - AI decision-making
   - Data transformations
   - Complex business logic
   - Database operations

3. **Connection:** HTTP Request node with Bearer token authentication

**Why it works:**

- Clients get a visual workflow they can understand
- You maintain control of complex logic in version-controlled Python
- No deployment headaches (n8n handles hosting)
- Easy to debug (n8n shows execution logs)
- Client can modify triggers and actions without touching code

**When to use this:**

- 90% of client situations
- Client wants to "see" how it works
- Workflow needs visual transparency
- Client may want to modify triggers/outputs
- You want to maintain the core logic

**What you deliver:**

1. Modal endpoint URL (e.g., `https://profile--app-name.modal.run`)
2. Bearer token for authentication
3. Pre-built n8n workflow (importable JSON)
4. Documentation: what the workflow does, how to modify triggers/actions
5. Test data to verify it works

**Pricing strategy:**

- **Setup fee:** $2,000-$10,000 (depending on complexity)
- **Optional retainer:** $500-$2,000/month for updates and monitoring
- **Per-execution fees:** If using expensive AI models, pass through costs

**Example client conversation:**

> **Client:** "Can I modify the email template?"
>
> **You:** "Absolutely. You'll have access to the n8n workflow where the email is sent. You can change the subject line, body, and even add attachments without touching any code. The AI logic that qualifies leads stays protected on my server."
>
> **Client:** "What if it breaks?"
>
> **You:** "The n8n interface shows you exactly where errors happen with color-coded logs. Most issues are simple (wrong API key, missing field) and you can fix them yourself. For anything complex, I'm available on the monthly retainer."

**Pros:**
- Visual interface clients love
- You retain IP control
- Easy to support remotely
- Client can make safe modifications
- Works from anywhere (cloud-based)

**Cons:**
- Requires n8n subscription ($20-$50/month)
- Client needs basic n8n familiarity
- Two-part system (n8n + Modal)

---

## Model 2: Managed Service (Maximum Revenue)

**What it is:** You run everything. The client gives you inputs (a spreadsheet, a form submission, an email) and gets outputs (a report, updated records, notifications). They never see the workflow.

**How it works:**

- You host the automation on your infrastructure (Modal, AWS, your server)
- Client accesses it through a simple interface you control:
  - Email: "Send your list to leads@yourcompany.com"
  - Form: Simple web form with file upload
  - Shared folder: Client drops files in Google Drive/Dropbox
  - API: Client's system hits your webhook
- You handle all errors, updates, and maintenance
- Client pays monthly retainer

**When to use this:**

- Enterprise clients with budget
- Non-technical clients who just want results
- Workflows requiring ongoing optimization
- When you want recurring revenue
- Client values reliability over control

**What you deliver:**

1. Simple input method (email, form, shared folder)
2. Documentation on how to submit requests
3. SLA (service level agreement): response times, uptime guarantees
4. Monthly reports showing usage and results
5. Point of contact for issues

**Pricing strategy:**

- **Setup fee:** $5,000-$20,000 (you're building long-term infrastructure)
- **Monthly retainer:** $1,000-$10,000+ (based on usage, complexity, value delivered)
- **Tiered pricing:** Different retainers for different usage levels
  - Bronze: Up to 100 executions/month - $1,000
  - Silver: Up to 500 executions/month - $3,000
  - Gold: Unlimited + priority support - $7,000

**Example client conversation:**

> **Client:** "What if it breaks?"
>
> **You:** "That's exactly why you're paying me. I monitor the system 24/7, handle all errors, and guarantee 99% uptime. You'll never have to troubleshoot anything. If something goes wrong, I fix it before you even notice."
>
> **Client:** "Can I modify it?"
>
> **You:** "You don't need to. Just tell me what you want changed and I'll update it within 24 hours. You're paying for results, not maintenance headaches."

**Pros:**
- Highest recurring revenue
- Complete control over IP
- Client never sees complexity
- Easiest for client (zero effort)
- You can optimize behind the scenes

**Cons:**
- You're on the hook for uptime
- Requires monitoring and support
- Client dependency on you (lock-in concern)
- More infrastructure management

**Advanced variation: White-label managed service**

You run the automation, but the client presents it as their own product to their customers. Higher retainer ($5,000-$20,000/month) but massive scale potential.

---

## Model 3: GitHub Codespace (Technical Clients)

**What it is:** You package the entire workflow (directives + executions + environment) into a GitHub repository with a one-click Codespace setup. The client clicks a button, gets a fully configured IDE in their browser, and runs the automation locally.

**How it works:**

1. You create a GitHub repo with:
   - All Python scripts
   - `.antigravity/` folder with agent directives
   - `.devcontainer/` for Codespace configuration
   - `.env.example` for credentials
   - `README.md` with setup instructions

2. Client clicks "Open in Codespace"

3. Codespace launches with:
   - Python environment pre-configured
   - Dependencies installed
   - Antigravity IDE extension ready
   - Instructions displayed

4. Client adds their API keys to `.env` and runs the workflow

**When to use this:**

- Technical clients (developers, data scientists)
- Clients who want full code access
- Workflows requiring heavy customization
- When you're handing off to an internal team
- Client wants to learn how it works

**What you deliver:**

1. GitHub repository (private or public)
2. Codespace configuration files
3. Comprehensive README with setup steps
4. Video walkthrough (Loom recording)
5. Example `.env` with placeholder credentials
6. Test data to verify it works

**Pricing strategy:**

- **One-time setup fee:** $3,000-$8,000
- **Optional training session:** $500-$1,500 (1-2 hour call)
- **Support retainer (optional):** $500-$1,000/month for ongoing questions
- **Update packages:** $1,000-$2,000 per major update

**Example client conversation:**

> **Client:** "Can I modify it?"
>
> **You:** "Absolutely. You'll have full access to the Python code and agent directives. The Codespace gives you a pre-configured development environment, so you can modify anything. I recommend starting with the directives (natural language instructions) before touching the code."
>
> **Client:** "What if I break something?"
>
> **You:** "That's what Git is for. You can always revert to the original version. Plus, the Codespace is isolated—if you break it, just delete and create a new one. Your changes are saved in your fork of the repo."

**Pros:**
- Client gets full code ownership
- One-click setup (no local environment issues)
- Works from anywhere (browser-based)
- Git version control built-in
- Good for technical clients who want to learn

**Cons:**
- Client needs coding knowledge
- You give away all IP
- Lower recurring revenue potential
- Support questions can be time-consuming

---

## Model 4: Manual Handover (Internal Teams)

**What it is:** You zip up the `directives/` and `executions/` folders, send it to the client, and they run it locally on their machine or server. The most basic handoff.

**How it works:**

1. You package:
   - `directives/` folder (markdown SOPs)
   - `executions/` folder (Python scripts)
   - `requirements.txt` for dependencies
   - `.env.example` for credentials
   - `README.md` with setup instructions

2. Client downloads, installs dependencies, adds credentials, runs locally

**When to use this:**

- Internal team members or partners
- Proof-of-concept handoffs
- Training scenarios
- When budget is limited
- Quick knowledge transfer

**What you deliver:**

1. ZIP file or Google Drive folder with all files
2. Setup documentation (markdown or PDF)
3. Video walkthrough (optional but recommended)
4. 1-hour training call (optional)

**Pricing strategy:**

- **Training fee:** $500-$2,000 (one-time)
- **Documentation package:** $1,000-$3,000 (if creating comprehensive docs)
- **Hourly support:** $150-$300/hour for follow-up questions

**Example client conversation:**

> **Client:** "What if it breaks?"
>
> **You:** "You'll have all the files and documentation. Most issues come from missing dependencies or incorrect API keys. I'll do a training session to walk you through troubleshooting. After that, I'm available at my hourly rate for support."
>
> **Client:** "Can I modify it?"
>
> **You:** "Yes, you'll have full access to everything. The directives (markdown files) are natural language instructions, so you can update those without coding. The Python scripts require programming knowledge to modify."

**Pros:**
- Fastest delivery method
- Client has full control
- No ongoing hosting costs
- Simple setup for technical teams

**Cons:**
- Lowest revenue potential
- Client needs local setup knowledge
- No version control (unless they set it up)
- Environment issues ("works on my machine")
- No recurring revenue

---

## The Decision Tree: Three Questions

How do you pick the right model? Ask these three questions:

### Question 1: Does the client want to own it or have you manage it?

**Own it:**
- They want control
- They have technical resources
- They may want to modify it
- They're cost-conscious
→ **Go to Question 2**

**Manage it:**
- They want results, not maintenance
- They have budget for ongoing service
- They value reliability over control
- They're non-technical
→ **Use Managed Service (Model 2)**

### Question 2: Do they need access from multiple locations?

**Yes (cloud-based):**
- Team in different offices
- Remote workers
- Want to access from phone/tablet
- Need collaboration
→ **Go to Question 3**

**No (local is fine):**
- Single user or co-located team
- Running on dedicated server
- Internal team with shared machine
→ **Use Manual Handover (Model 4)**

### Question 3: How technical are they? (1-5 scale)

**1-2 (Non-technical):**
- Never written code
- Uncomfortable with command line
- Uses no-code tools (Zapier, Airtable)
→ **Use Hybrid Wrapper (Model 1)**

**3-4 (Technical):**
- Can read/modify code
- Comfortable with GitHub
- Developers or data scientists
→ **Use GitHub Codespace (Model 3)**

**5 (Expert):**
- Senior engineers
- Want to deeply customize
- Already using advanced tools
→ **Use GitHub Codespace (Model 3) or Manual Handover (Model 4)**

### Decision Tree Flowchart

```
START: New client wants automation
        |
        V
┌─────────────────────────────────────┐
│ Do they want to OWN or MANAGE?      │
└─────────────────────────────────────┘
        |                    |
    [OWN IT]            [MANAGE IT]
        |                    |
        V                    V
┌──────────────────┐   ┌──────────────────┐
│ Cloud or Local?  │   │ MANAGED SERVICE  │
└──────────────────┘   │   (Model 2)      │
        |              └──────────────────┘
    [CLOUD]  [LOCAL]
        |        |
        V        V
┌───────────┐  ┌──────────────────┐
│ Technical │  │ MANUAL HANDOVER  │
│  Level?   │  │   (Model 4)      │
└───────────┘  └──────────────────┘
    |      |
 [1-2]  [3-5]
    |      |
    V      V
┌────────┐ ┌──────────────────┐
│ HYBRID │ │ GITHUB CODESPACE │
│WRAPPER │ │   (Model 3)      │
│(Model 1)│ └──────────────────┘
└────────┘
```

---

## Real Example: Picking the Right Model

Let me walk you through a real client decision.

**The client:** Marketing agency with 5-person team. They want an automation that:
- Scrapes competitor websites weekly
- Analyzes pricing changes with AI
- Sends alerts to Slack when prices drop

**Working through the decision tree:**

**Question 1: Own or manage?**

I ask: "Do you want to run this yourself, or have me handle it for you?"

Client: "We want to see how it works and maybe modify the Slack alerts, but we don't want to maintain servers or debug code."

→ **They want to OWN it, but with low maintenance**

**Question 2: Cloud or local?**

I ask: "Do team members need to access this from different locations?"

Client: "Yes, we're fully remote. Plus, we want it to run automatically even when our computers are off."

→ **They need CLOUD-based**

**Question 3: Technical level?**

I ask: "On a scale of 1-5, how technical is your team? 1 is 'never written code,' 5 is 'senior engineers.'"

Client: "Probably a 2. We use Zapier and Airtable, but none of us code."

→ **Non-technical (level 1-2)**

**Decision: Hybrid Wrapper (Model 1)**

**The pitch:**

"Perfect. I'll build you a Hybrid Wrapper. Here's how it works:

- The scraping and AI analysis runs on my Modal server as a secure endpoint
- You'll get an n8n workflow (like Zapier but more powerful) that triggers it weekly
- The n8n workflow shows you visually what's happening: scrape → analyze → send to Slack
- You can modify the Slack message, change the schedule, or add email alerts without touching code
- The complex AI logic stays on my server, version-controlled and secure
- Setup fee is $4,000, and I'll include 3 months of support for $500/month

If you ever want to hand it off to a developer to customize the scraping logic, I can give you the Python code later. But 90% of changes you'll want to make, you can do yourself in n8n."

**Client response:** "That's perfect. We want to see what's happening but don't want to manage infrastructure. When can you start?"

**Why this worked:**
- Matched their technical level (visual interface)
- Met their need for cloud-based access
- Gave them ownership without maintenance burden
- Protected your IP (they can't see the Python logic)
- Created recurring revenue opportunity (support retainer)

---

## Handling Objections

Every delivery model has concerns. Here's how to address them:

### Objection 1: "What if it breaks?"

**Hybrid Wrapper response:**
"The n8n interface shows you exactly where errors happen with color-coded logs and error messages. Most issues are simple—wrong API key, missing field—and you can fix them yourself with the documentation I provide. For anything complex, I'm available on the support retainer to jump in within 24 hours."

**Managed Service response:**
"That's exactly why you're paying me. I monitor the system 24/7, handle all errors, and guarantee 99% uptime in the SLA. You'll never have to troubleshoot anything. If something goes wrong, I fix it before you even notice."

**GitHub Codespace response:**
"That's what Git is for. You can always revert to the original version with one command. Plus, the Codespace is isolated—if you break the environment, just delete it and spin up a new one in 60 seconds. Your changes are saved in your fork."

**Manual Handover response:**
"You'll have all the files and documentation, including a troubleshooting guide for common issues. I'll also do a 1-hour training session to walk you through debugging. After that, I'm available at my hourly rate for support calls."

### Objection 2: "Can I modify it?"

**Hybrid Wrapper response:**
"Absolutely. You can modify triggers (when it runs), actions (what it does with results), and outputs (emails, Slack messages, etc.) directly in the visual n8n workflow. The core AI logic stays protected on my server. If you want to modify that later, we can discuss opening up the Python code."

**Managed Service response:**
"You don't need to. Just tell me what you want changed and I'll update it within 24 hours. That's included in your retainer. You're paying for results, not the burden of making changes yourself."

**GitHub Codespace response:**
"Yes, you have full access to all the code and directives. I recommend starting with the directives (markdown files with natural language instructions) since those are easier to modify. The Python code is also fully accessible if you have development resources."

**Manual Handover response:**
"Yes, you'll have complete access to everything. The directives are natural language, so you can update those without coding knowledge. The Python scripts require programming experience to modify safely."

### Objection 3: "What about security?"

**All models:**
"Great question. Here's how credentials are handled:

- API keys and passwords never appear in the code—they're stored as environment variables
- [Hybrid/Managed] Your credentials are encrypted in Modal Secrets, which are isolated per project
- [Codespace/Manual] You add credentials to a local `.env` file that's never committed to Git
- The authentication uses Bearer tokens (like API keys) that you can rotate anytime
- All communication happens over HTTPS encrypted connections

If you have specific compliance requirements (HIPAA, SOC 2, etc.), we can discuss additional security measures."

### Objection 4: "How do I know it will keep working?"

**Hybrid Wrapper response:**
"The workflow runs on Modal's infrastructure, which has 99.9% uptime. n8n is enterprise-grade automation software used by thousands of companies. The only dependencies are the external APIs you're using (e.g., OpenAI, your CRM). If those go down, nothing will work—but that's true regardless of who builds the integration."

**Managed Service response:**
"That's covered in the SLA. I guarantee 99% uptime and commit to fixing any issues within [X hours]. I also monitor the system proactively, so I often catch and fix issues before they affect you. Plus, I maintain the workflow as APIs change—if OpenAI updates their API, I update your integration at no extra cost."

**GitHub Codespace response:**
"The Codespace environment is frozen in the configuration, so it will always work the same way. Dependencies are pinned to specific versions. That said, external APIs do change over time, so you may need to update the code eventually. I can provide update packages for a fee, or you can modify it yourself."

**Manual Handover response:**
"As long as you don't change the environment (Python version, dependencies), it will work the same way. External APIs may change over time, requiring updates. I've included documentation on how to update dependencies, and I'm available for hourly support if needed."

---

## The Handover Package: What to Deliver

Regardless of which model you choose, professionalism matters. Here's what to include:

### Core Deliverables (All Models)

1. **Documentation**
   - What the automation does (plain English summary)
   - How to use it (step-by-step instructions)
   - How to troubleshoot common issues
   - Where to get help

2. **Test Data**
   - Sample inputs to verify it works
   - Expected outputs to compare against
   - Instructions for running a test

3. **Credentials Template**
   - `.env.example` or credential checklist
   - Where to obtain each API key
   - How to add credentials securely

4. **Video Walkthrough**
   - 5-10 minute Loom recording
   - Shows how to use it
   - Demonstrates one full execution
   - Points out common pitfalls

### Model-Specific Additions

**Hybrid Wrapper:**
- n8n workflow JSON (importable)
- Modal endpoint URL and Bearer token
- cURL command to test the endpoint
- n8n setup guide (if they don't have n8n yet)

**Managed Service:**
- SLA document (uptime guarantees, response times)
- Input method instructions (how to submit requests)
- Monthly reporting template
- Escalation contact info

**GitHub Codespace:**
- Repository URL with "Open in Codespace" button
- `CONTRIBUTING.md` for how to modify safely
- Codespace configuration (`.devcontainer/`)
- Example `.env` file

**Manual Handover:**
- ZIP file or shared folder link
- `requirements.txt` for dependencies
- Setup guide (markdown or PDF)
- Training session recording (if conducted)

### Presentation Tips

**Don't just email a link.** Schedule a 30-minute handover call where you:

1. **Demo it live:** Show the automation running end-to-end
2. **Walk through the package:** Open each file and explain what it does
3. **Answer questions:** Address concerns in real-time
4. **Set expectations:** Clarify what support is included vs. paid
5. **Get sign-off:** Confirm they can successfully run a test

This call dramatically reduces support requests later and ensures client satisfaction.

---

## Pricing Strategies by Model

Here's how to think about pricing for each model:

### Hybrid Wrapper Pricing

**Setup fee:** $2,000-$10,000
- Based on workflow complexity
- Include: Modal deployment + n8n workflow + documentation + handover call
- Add 20% for each additional integration (CRM, database, etc.)

**Optional retainer:** $500-$2,000/month
- Include: Bug fixes, minor updates, monitoring, priority support
- Tier by response time (24hr, 4hr, 1hr SLA)

**Per-execution fees (if applicable):**
- Pass through AI costs if using expensive models
- E.g., "First 100 executions/month included, $0.50 per execution after that"

### Managed Service Pricing

**Setup fee:** $5,000-$20,000
- Higher because you're building long-term infrastructure
- Include: Workflow build + hosting + monitoring + SLA

**Monthly retainer:** $1,000-$10,000+
- Price based on value delivered, not cost
- E.g., lead generation that produces 50 qualified leads/month? Charge based on lead value
- Tiered by usage (executions per month)

**Annual contracts:**
- Offer 10-15% discount for annual prepayment
- Locks in recurring revenue

### GitHub Codespace Pricing

**One-time setup:** $3,000-$8,000
- Include: Repo setup + Codespace config + documentation + video walkthrough

**Training session (optional):** $500-$1,500
- 1-2 hour live call
- Screen sharing, Q&A, troubleshooting practice

**Support retainer (optional):** $500-$1,000/month
- For ongoing questions
- Most clients won't need this after the first month

### Manual Handover Pricing

**Training fee:** $500-$2,000
- Include: Documentation + 1-hour training call

**Hourly support:** $150-$300/hour
- For follow-up questions
- Most clients use 2-5 hours total


---

## Try It Yourself: Classify Your Clients

Take your current client list (or prospects) and classify them using the decision tree.

**Exercise:** For each client, answer:

1. Do they want to own it or have you manage it?
2. Do they need cloud-based access or is local fine?
3. What's their technical level (1-5)?

Then map them to a delivery model:

| Client Name | Own/Manage | Cloud/Local | Tech Level | Model | Price |
|-------------|------------|-------------|------------|-------|-------|
| Acme Corp | Manage | Cloud | 2 | Managed Service | $3K/mo |
| StartupXYZ | Own | Cloud | 4 | GitHub Codespace | $5K setup |
| Local Biz | Own | Local | 1 | Manual Handover | $1K training |

**Reflection questions:**

- Are you using the same model for all clients? (If yes, you're leaving money on the table)
- Which clients would pay more for a managed service?
- Which clients are technical enough for Codespace but you're over-delivering with managed?
- Are any clients frustrated because the model doesn't match their needs?

**Action item:** For your next 3 client deliveries, deliberately choose different models based on the decision tree. See how it affects client satisfaction and your revenue.

---

## Resource: Proposal Templates

Need help pitching these models? I've created proposal templates for each:

**Hybrid Wrapper Proposal:**
- Explains the three-layer architecture in client-friendly language
- Includes pricing breakdown
- Addresses common objections
- [Download template]

**Managed Service Proposal:**
- SLA terms and uptime guarantees
- Tiered pricing options
- Monthly reporting format
- [Download template]

**GitHub Codespace Proposal:**
- One-click setup explanation
- Training session outline
- Ongoing support options
- [Download template]

**Manual Handover Proposal:**
- Documentation package contents
- Training session agenda
- Hourly support terms
- [Download template]

*Templates available in the resources folder: `/ebook/resources/proposal-templates/`*

---

## Key Takeaway

**Stop using one-size-fits-all delivery.** Match the delivery model to the client's needs, technical level, and budget.

**The decision tree:**
1. Own or manage?
2. Cloud or local?
3. Technical level?

**The four models:**
- **Hybrid Wrapper:** Visual interface + your protected logic (90% of clients)
- **Managed Service:** You run everything (highest recurring revenue)
- **GitHub Codespace:** One-click code access (technical clients)
- **Manual Handover:** ZIP file delivery (internal teams)

**The business impact:**
- Right-sized delivery = higher client satisfaction
- Managed services = recurring revenue
- Clear pricing = fewer objections
- Professional handover = fewer support requests

**In the next chapter**, we'll cover how to build productized offers around these delivery models—turning one-off projects into repeatable, scalable revenue streams.

**But first**, classify your current clients. You might discover you're over-delivering to some (leaving money on the table with manual work) and under-delivering to others (frustrated clients who can't use what you built).

The right delivery model turns one-time clients into long-term relationships.

---

**Word Count:** 4,487 words
