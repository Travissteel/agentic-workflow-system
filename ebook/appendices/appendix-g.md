# Appendix G: Client Handoff Templates

The hardest part of selling agentic workflow services isn't building the automation. It's knowing how to position it, price it, and hand it off in a way that makes the client feel confident and empowered.

This appendix provides ready-to-use templates that have been battle-tested in real consulting engagements. Whether you're proposing a managed service retainer or delivering a full handoff with training, these templates will save you hours of proposal writing and eliminate the guesswork from client conversations.

## Why Client Handoff Matters in the DOE Framework

In traditional software development, "deployment" means pushing code to production. In the Directive Orchestration Execution (DOE) framework, deployment is only half the story. The real measure of success is whether your client can understand, maintain, and eventually evolve the workflow you've built for them.

This is where the separation of Directives (natural language instructions) and Executions (deterministic code) becomes invaluable. When you hand off a workflow, you're not just delivering code. You're delivering:

- **Directives**: The markdown files that explain what the workflow does and why
- **Executions**: The Python scripts or Modal endpoints that do the actual work
- **Context**: The decision-making framework that allows the client to modify it later
- **Confidence**: The assurance that they're not locked into endless dependence on you

The four handoff models we covered in Chapter 19 represent different points on the spectrum between "you run everything" and "they run everything." Choosing the right model determines whether your client relationship is a one-time transaction or a long-term partnership.

## The Four Handoff Models (Quick Recap)

Before we dive into the templates, let's briefly review the four handoff models:

1. **Hybrid Wrapper (n8n + Modal)**: The recommended approach for most clients. You deploy the complex logic to Modal, wrap it in an n8n visual workflow, and hand the client a no-code interface they can understand and maintain.

2. **Managed Service**: You host and maintain everything. The client pays a monthly retainer and submits change requests. Best for non-technical clients who want results without responsibility.

3. **GitHub Codespace**: You deliver a one-click development environment pre-configured with all directives, executions, and dependencies. Best for technical clients who want full control and can handle code.

4. **Manual Folder**: You deliver a folder with directives and executions, and the client sets up their own environment. Best for technical clients on a tight budget or internal teams.

Choosing the right model isn't about what's easiest for you. It's about what sets the client up for success. A non-technical client forced to manage a GitHub Codespace will feel abandoned. A technical client locked into a managed service will feel infantilized and overcharged.

The templates in this appendix will help you navigate these conversations with confidence.

```
┌─────────────────────────────────────────────────────┐
│  DOWNLOAD EDITABLE TEMPLATES                        │
│                                                      │
│  Get Word docs and PDFs of all these templates      │
│  ready to customize for your business:              │
│                                                      │
│  travissteel.net/the-last-employee/resources#client-handoff     │
│                                                      │
│  Includes: Intake form, proposals, email scripts,   │
│  and the 3-question decision guide.                 │
└─────────────────────────────────────────────────────┘
```

---

## The 3-Question Handoff Decision Guide

Use this decision tree during your discovery call or immediately after your intake form. Three simple questions will tell you which handoff model to propose.

### Question 1: Is the client technical?

**How to assess:**
- Do they have developers or IT staff in-house?
- Have they built internal tools or integrations before?
- Are they comfortable reading code, even if they don't write it?

**If YES**: They're a candidate for GitHub Codespace or Manual Folder.
**If NO**: They need Hybrid Wrapper or Managed Service.

### Question 2: Do they want ongoing support?

**How to assess:**
- Ask directly: "After we build this, do you want us to maintain it, or would you prefer to own it completely?"
- Listen for signals: "We want to be able to change it ourselves" vs "We just want it to work"
- Consider their team capacity: Do they have bandwidth to manage another system?

**If YES (ongoing support)**: Managed Service is the best fit.
**If NO (one-time delivery)**: Hybrid Wrapper, GitHub Codespace, or Manual Folder.

### Question 3: What's their budget?

**How to assess:**
- Are they a small business ($2K-$10K project budgets)?
- Mid-market company ($10K-$50K project budgets)?
- Enterprise ($50K+ project budgets)?

**Budget implications:**
- **Low ($2K-$10K)**: Manual Folder or simplified Hybrid Wrapper
- **Medium ($10K-$30K)**: Hybrid Wrapper or GitHub Codespace
- **High ($30K+)**: Managed Service or premium Hybrid Wrapper with extensive training

### Decision Matrix

| Question 1: Technical? | Question 2: Support? | Question 3: Budget? | Recommended Model |
|------------------------|----------------------|---------------------|-------------------|
| No | Yes | Any | Managed Service |
| No | No | Medium-High | Hybrid Wrapper (n8n + Modal) |
| No | No | Low | Hybrid Wrapper (simplified) |
| Yes | Yes | High | Managed Service (premium tier) |
| Yes | No | Medium-High | GitHub Codespace |
| Yes | No | Low | Manual Folder |

### Visual Decision Tree

```
START: New Client
    |
    Is client technical?
    ├─ NO ──> Do they want ongoing support?
    │         ├─ YES ──> Managed Service
    │         └─ NO ──> Hybrid Wrapper (n8n + Modal)
    │
    └─ YES ──> Do they want ongoing support?
              ├─ YES ──> Budget?
              │          ├─ High ──> Managed Service (premium)
              │          └─ Low-Med ──> Hybrid Wrapper
              └─ NO ──> Budget?
                         ├─ Medium-High ──> GitHub Codespace
                         └─ Low ──> Manual Folder
```

### Common Edge Cases

**"We're semi-technical but don't have time"**
→ Hybrid Wrapper. They'll appreciate the visual interface and won't feel condescended to.

**"We want to learn how to build this ourselves eventually"**
→ GitHub Codespace with training sessions. Position it as education, not just delivery.

**"We want you to build it, but we need to white-label it for our clients"**
→ Manual Folder or GitHub Codespace with licensing agreement. They need full ownership.

**"We're not sure what we need yet"**
→ Start with Managed Service on a 3-month pilot. Lock in recurring revenue while they figure out their strategy.

---

## Template 1: Client Intake Form

Use this questionnaire before your discovery call to save time and qualify leads. Send it as a Google Form, Typeform, or simple email.

---

### Agentic Workflow Automation - Client Intake Form

**Thank you for your interest in automating your business processes with AI-powered workflows. This brief questionnaire helps us understand your needs and prepare for our discovery call.**

---

#### 1. Business Background

**Company Name:**
_________________________________

**Industry:**
_________________________________

**Company Size:**
☐ Solo/Freelancer
☐ 2-10 employees
☐ 11-50 employees
☐ 51-200 employees
☐ 200+ employees

**Primary Contact Name:**
_________________________________

**Role/Title:**
_________________________________

**Email:**
_________________________________

**Phone (optional):**
_________________________________

---

#### 2. Current Processes and Pain Points

**What business process are you looking to automate?**
(e.g., lead qualification, data entry, report generation, customer onboarding)

_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

**How is this process currently handled?**
(e.g., manually in spreadsheets, partially automated, outsourced)

_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

**What's the biggest pain point with the current process?**
(e.g., too slow, error-prone, can't scale, costs too much)

_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

**Approximately how much time does this process consume per week?**
☐ 1-5 hours
☐ 6-15 hours
☐ 16-30 hours
☐ 30+ hours

**What would success look like for this project?**
(e.g., "Reduce time spent from 10 hours/week to 1 hour/week")

_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

---

#### 3. Technical Capabilities

**Does your team have any of the following?** (Check all that apply)
☐ In-house developers or IT staff
☐ Experience with no-code tools (Zapier, Make, n8n)
☐ Experience with APIs or webhooks
☐ Cloud hosting accounts (AWS, Google Cloud, etc.)
☐ GitHub or version control experience
☐ None of the above

**Who will be responsible for maintaining the workflow after delivery?**
☐ Our internal team
☐ We want you to maintain it
☐ We're not sure yet

**Are you comfortable reading code, even if you don't write it?**
☐ Yes
☐ No
☐ Some team members are

---

#### 4. Budget and Timeline

**What's your budget range for this project?**
☐ Under $5,000
☐ $5,000 - $15,000
☐ $15,000 - $30,000
☐ $30,000 - $50,000
☐ $50,000+
☐ Flexible, pending proposal

**Are you open to a monthly retainer model instead of a one-time project?**
☐ Yes, preferred
☐ Maybe, depending on the details
☐ No, we want full ownership

**What's your ideal timeline for this project?**
☐ Urgent (within 2 weeks)
☐ Soon (within 1 month)
☐ Standard (1-3 months)
☐ Flexible (3+ months)

---

#### 5. Success Criteria

**How will you measure the success of this automation?**
(Check all that apply)
☐ Time saved
☐ Cost reduction
☐ Error reduction
☐ Increased capacity
☐ Faster turnaround time
☐ Better customer experience
☐ Other: _________________________________

**What would make this project a "home run" for you?**

_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

---

#### 6. Additional Context

**Is there anything else we should know about your business, process, or goals?**

_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

**How did you hear about us?**
☐ Referral (please specify): _________________________________
☐ Google search
☐ LinkedIn
☐ Conference/event
☐ Other: _________________________________

---

**Next Steps:**
After submitting this form, we'll review your responses and reach out within 1-2 business days to schedule a discovery call. During that call, we'll walk through your process in detail and propose the best solution for your needs.

---

### How to Use This Intake Form

**Before the call:**
Review their answers and identify which handoff model makes sense using the 3-Question Decision Guide above.

**During the call:**
Don't re-ask questions they already answered. Use the call to dig deeper into specifics, clarify ambiguities, and build rapport.

**After the call:**
Reference their intake answers in your proposal to show you listened and understood their unique situation.

---

## Template 2: Managed Service Proposal

Use this template when the client wants ongoing support and maintenance. This is your recurring revenue model.

---

### Proposal: Managed Agentic Workflow Service

**Prepared for:** [CLIENT NAME]
**Prepared by:** [YOUR COMPANY NAME]
**Date:** [DATE]
**Proposal Valid Until:** [DATE + 30 DAYS]

---

#### Executive Summary

Based on our discovery call on [DATE], we understand that [CLIENT NAME] is currently spending approximately [X HOURS] per week on [PROCESS NAME], which is [PAIN POINT: too slow / error-prone / difficult to scale]. This manual process is preventing your team from focusing on higher-value activities like [CLIENT'S CORE BUSINESS ACTIVITY].

We propose building and managing a fully automated AI-powered workflow that will reduce the time spent on [PROCESS NAME] from [X HOURS] to [Y HOURS] per week, delivering immediate ROI through [TIME SAVINGS / COST REDUCTION / INCREASED CAPACITY].

This is a **Managed Service engagement**, meaning we build, host, maintain, and continuously optimize your workflow. You submit requests, we handle everything behind the scenes, and you enjoy the results without the technical burden.

---

#### What You Get

**1. Custom-Built Agentic Workflow**
We will design and develop a workflow that:
- [Specific deliverable 1, e.g., "Automatically scrapes and qualifies inbound leads from your contact form"]
- [Specific deliverable 2, e.g., "Enriches each lead with company data from Apollo and LinkedIn"]
- [Specific deliverable 3, e.g., "Sends qualified leads directly to your CRM with a lead score"]

**2. Fully Managed Hosting**
We handle all infrastructure:
- Cloud hosting on secure, scalable servers (Modal.com)
- Authentication and security configuration
- Monitoring and uptime guarantees (99.5% SLA)
- Monthly usage reports and optimization recommendations

**3. Ongoing Maintenance and Support**
Included in your monthly retainer:
- Unlimited bug fixes and error resolution
- Monthly optimization reviews
- Priority support (response within 24 business hours)
- Access to our team via email, Slack, or scheduled calls

**4. Change Requests**
Each month, you receive [X] hours of included development time for:
- Adding new features
- Modifying existing logic
- Integrating additional tools or data sources

Additional hours available at [$ PER HOUR] if needed.

---

#### Pricing

**Monthly Retainer:** $[X,XXX] per month
**Minimum Commitment:** [3 or 6] months
**Setup Fee (First Month):** $[X,XXX] (covers initial build and deployment)

**What's Included in the Monthly Retainer:**
- Unlimited bug fixes and error handling
- Hosting and infrastructure (up to [X] executions per month)
- [X] hours of change requests or new feature development
- Monthly performance and optimization reports
- Priority support (24-hour response time)

**What's NOT Included:**
- Third-party API costs (e.g., OpenAI, Apollo, Gemini) — billed at cost
- Major scope expansions beyond [X] hours/month (billed separately at $[XXX]/hour)
- Integration with new platforms requiring significant custom development (quoted separately)

**Volume-Based Pricing:**
If your usage exceeds [X] executions per month, we'll work with you to adjust pricing to reflect the increased infrastructure costs. Our goal is to keep this fair and scalable as you grow.

---

#### Service Level Agreement (SLA)

**Uptime Guarantee:** 99.5% monthly uptime
**Support Response Time:** Within 24 business hours for all inquiries
**Critical Bug Resolution:** Within 48 business hours
**Change Request Turnaround:** Most requests completed within 5-7 business days

**What happens if we miss our SLA?**
You'll receive a prorated credit on the following month's invoice equal to [X]% of the monthly retainer for each percentage point below 99.5% uptime.

---

#### Deliverables and Timeline

**Month 1 (Setup Phase):**
- Week 1-2: Workflow design and development
- Week 3: Deployment to production
- Week 4: Testing, training, and handoff call

**Ongoing (Months 2+):**
- Continuous monitoring and optimization
- Monthly check-in calls (optional)
- Change requests processed as submitted

---

#### Ownership and Exit Terms

**Intellectual Property:**
You own all the data and outputs produced by the workflow. We retain ownership of the underlying code and infrastructure, but you have the right to request a full export of all directives (instruction files) and executions (code) at any time.

**Cancellation Policy:**
After the initial [3 or 6]-month commitment, either party may cancel with [30 or 60] days' written notice. Upon cancellation, we will provide:
- A full export of all workflow code and documentation
- A 30-day transition period to help you migrate to self-hosting or another provider
- A final usage report and recommendations for future maintenance

**What happens to my workflow if I cancel?**
You can take the code and host it yourself, hire another developer to maintain it, or simply pause the workflow. We'll provide clear documentation to make this transition as smooth as possible.

---

#### Why Managed Service Makes Sense for You

Based on our conversation, a Managed Service model is the best fit for [CLIENT NAME] because:

1. **Your team is focused on [CORE BUSINESS], not technical maintenance.** You need automation that "just works" without becoming another IT burden.

2. **You want continuous optimization.** As your business evolves, your workflows should too. Our monthly retainer ensures you're always running the most efficient version.

3. **You value peace of mind.** With our SLA and dedicated support, you never have to worry about downtime, bugs, or "who's going to fix this?"

This isn't outsourcing. It's a partnership. We succeed when you save time, reduce costs, and scale faster.

---

#### Next Steps

1. **Review this proposal** and let us know if you have any questions.
2. **Schedule a brief call** (if needed) to clarify details or adjust scope.
3. **Sign the agreement** and we'll begin work immediately.

**Target Start Date:** [DATE]
**Expected Go-Live Date:** [DATE + 4 WEEKS]

We're excited to help [CLIENT NAME] automate [PROCESS NAME] and free up your team to focus on what matters most.

**[YOUR NAME]**
[YOUR TITLE]
[YOUR COMPANY NAME]
[EMAIL]
[PHONE]

---

### Pricing Guidance for Managed Services

**Small Business (2-10 employees):**
$1,500 - $3,000/month for single workflow with light maintenance

**Mid-Market (11-200 employees):**
$3,000 - $8,000/month for multiple workflows or complex integrations

**Enterprise (200+ employees):**
$8,000 - $20,000+/month for mission-critical workflows with SLA guarantees

**Setup Fees:**
Typically 2-3x the monthly retainer for the first month to cover build time.

---

## Template 3: Full Handover Proposal

Use this template when the client wants to own and maintain the workflow themselves after delivery.

---

### Proposal: Custom Agentic Workflow (Full Handover)

**Prepared for:** [CLIENT NAME]
**Prepared by:** [YOUR COMPANY NAME]
**Date:** [DATE]
**Proposal Valid Until:** [DATE + 30 DAYS]

---

#### Executive Summary

Based on our discovery call on [DATE], we understand that [CLIENT NAME] wants to automate [PROCESS NAME] while maintaining full ownership and control of the workflow after delivery. You have [technical capabilities: in-house developers / experience with no-code tools / a technical team member] and prefer a one-time build-and-handoff engagement rather than ongoing management.

We propose designing, building, testing, and delivering a fully functional AI-powered workflow using the **Hybrid Wrapper Strategy** (see Chapter 18). This approach combines the power of agentic Python logic deployed to Modal with the accessibility of n8n's visual workflow interface. Your team will receive a working system they can understand, modify, and maintain without deep coding expertise.

**Outcome:** By [PROJECT COMPLETION DATE], you'll have a production-ready workflow that reduces [PROCESS NAME] from [X HOURS] to [Y HOURS] per week, complete with documentation, training, and 30 days of warranty support.

---

#### What You Get

**1. Fully Functional Agentic Workflow**
We will design, build, test, and deploy:
- [Specific deliverable 1, e.g., "Modal endpoint that scrapes lead data and enriches with AI analysis"]
- [Specific deliverable 2, e.g., "n8n visual workflow with trigger, authentication, and final actions"]
- [Specific deliverable 3, e.g., "Integration with your existing CRM/database"]

**2. Complete Documentation Package**
You'll receive:
- **Directives folder**: Natural language instruction files explaining what each part does and why
- **Executions folder**: All Python code, fully commented
- **Setup guide**: Step-by-step instructions for modifying or extending the workflow
- **Troubleshooting guide**: Common issues and how to resolve them
- **Architecture diagram**: Visual map of how all the pieces connect

**3. Live Training Session**
We'll conduct a [60 or 90]-minute screen-share training covering:
- How the workflow operates end-to-end
- How to modify triggers, inputs, and outputs in n8n
- How to read and understand the Modal endpoint code
- How to monitor usage and troubleshoot errors
- Best practices for future enhancements

**4. 30-Day Warranty Support**
After handoff, we provide:
- Bug fixes for any issues discovered in the delivered workflow
- Email support for technical questions (response within 48 business hours)
- One follow-up call if needed to clarify functionality

After 30 days, you own and maintain the workflow completely. Additional support available on an hourly basis if needed.

---

#### Pricing

**Total Project Cost:** $[X,XXX] (fixed price)

**Payment Schedule:**
- **50% deposit** ($[X,XXX]) upon contract signing
- **50% final payment** ($[X,XXX]) upon successful handoff and training

**What's Included in This Price:**
- Complete workflow design and development
- Deployment to Modal (your account or ours, your choice)
- n8n workflow configuration and testing
- All documentation and training materials
- Live training session (up to 90 minutes)
- 30 days of warranty support

**What's NOT Included:**
- Third-party API costs (OpenAI, Gemini, Apollo, etc.) — you'll need your own accounts
- n8n hosting fees (approximately $20-$50/month depending on plan)
- Modal hosting fees (typically $10-$100/month depending on usage)
- Future enhancements or modifications after the 30-day warranty period
- Ongoing maintenance or monitoring

**Optional Add-Ons:**
- **Extended warranty** (90 days total): +$[XXX]
- **Additional training session** (for team onboarding): $[XXX] per hour
- **Pre-paid support hours** (10-hour block for future changes): $[XXX] per hour

---

#### Deliverables Checklist

At the end of this engagement, you will receive:

**Technical Deliverables:**
- ✅ Modal endpoint URL and authentication token
- ✅ n8n workflow (exported JSON file you can import)
- ✅ Complete Python codebase with comments
- ✅ Environment variable configuration file (.env template)
- ✅ All directives (markdown instruction files)

**Documentation:**
- ✅ Setup and installation guide
- ✅ User manual (how to operate the workflow)
- ✅ Developer guide (how to modify the code)
- ✅ Troubleshooting guide
- ✅ Architecture diagram

**Training:**
- ✅ Live 90-minute training session (recorded for your reference)
- ✅ Q&A support during training
- ✅ Follow-up resources and links

**Support:**
- ✅ 30 days of warranty support via email
- ✅ One follow-up call if needed (within 30 days)

---

#### Timeline and Milestones

**Week 1-2: Design and Development**
- Workflow logic design and approval
- Python endpoint development
- Initial testing in local environment

**Week 3: Deployment and Integration**
- Deploy to Modal production
- Configure n8n workflow
- End-to-end testing with real data

**Week 4: Documentation and Handoff**
- Finalize all documentation
- Conduct live training session
- Transfer all credentials and access
- Final walkthrough and Q&A

**Total Timeline:** 4 weeks from contract signing to handoff

**Milestone Payments:**
- Deposit (50%) due upon signing
- Final payment (50%) due after successful training and handoff

---

#### Ownership and Intellectual Property

**You own everything.**

Upon final payment, you receive:
- Full source code with unlimited modification rights
- All documentation and training materials
- Complete ownership of the deployed workflow
- No licensing fees, royalties, or ongoing obligations

**What we retain:**
We reserve the right to reuse general patterns, frameworks, and techniques from this project in future client work (but never your proprietary business logic or data).

---

#### Success Criteria (Definition of Done)

This project is considered complete when:

1. The workflow runs successfully from trigger to final action
2. All edge cases identified during testing are handled
3. Documentation is clear and complete
4. Training session is conducted and recorded
5. You confirm the workflow meets the success criteria defined in the intake form
6. All deliverables are transferred to your systems

**What "successful handoff" means:**
You should be able to operate, monitor, and make minor modifications to the workflow without contacting us. If you encounter a bug or error within 30 days that was present in the original delivery, we'll fix it at no charge.

---

#### Why Full Handover Makes Sense for You

Based on our conversation, a full handover model is the best fit for [CLIENT NAME] because:

1. **You have technical capabilities.** Your team [has developers / understands no-code tools / is comfortable learning new systems] and wants full control.

2. **You prefer to own your infrastructure.** Rather than paying ongoing fees, you want to invest upfront and maintain internally.

3. **You value independence.** You don't want to rely on external vendors for day-to-day operations or minor changes.

This model gives you complete ownership, full transparency, and the freedom to evolve the workflow as your business grows.

---

#### What Happens After Handoff?

**Option 1: Full Independence**
You maintain and evolve the workflow on your own. We're here if you need ad-hoc support at our hourly rate ($[XXX]/hour).

**Option 2: Pre-Paid Support Blocks**
Purchase 10-hour blocks of support at a discounted rate ($[XXX]/hour instead of $[XXX]/hour) for future enhancements or troubleshooting.

**Option 3: Convert to Managed Service**
If you later decide you'd prefer us to manage it, we can transition to a monthly retainer (pricing based on complexity).

---

#### Next Steps

1. **Review this proposal** and confirm the scope matches your expectations.
2. **Schedule a brief call** (optional) if you have questions or want to adjust deliverables.
3. **Sign the agreement** and submit the 50% deposit to begin work.

**Target Start Date:** [DATE]
**Expected Handoff Date:** [DATE + 4 WEEKS]

We're excited to build a workflow that gives [CLIENT NAME] complete ownership and control over [PROCESS NAME].

**[YOUR NAME]**
[YOUR TITLE]
[YOUR COMPANY NAME]
[EMAIL]
[PHONE]

---

### Pricing Guidance for Full Handover

**Simple Workflow (single trigger, single action, minimal logic):**
$3,000 - $8,000

**Standard Workflow (multiple steps, API integrations, basic AI logic):**
$8,000 - $20,000

**Complex Workflow (multi-stage process, custom AI models, database integration):**
$20,000 - $50,000+

**Training and Documentation:**
Typically included, but can add $1,500 - $3,000 if extensive onboarding is needed.

---

## Email Templates

Use these ready-to-send email templates to move prospects through your pipeline.

---

### Email 1: Initial Outreach / Discovery Call Invitation

**Subject:** Quick question about automating [PROCESS NAME]

Hi [FIRST NAME],

I came across [COMPANY NAME] and noticed you're [relevant observation: "hiring for data entry roles" / "manually processing a high volume of leads" / "posting about scaling challenges on LinkedIn"].

I specialize in building AI-powered workflow automation for [INDUSTRY] companies like yours. Most of my clients are spending 10-20 hours per week on tasks that could be automated down to 1-2 hours with the right system.

Would you be open to a quick 20-minute call to explore whether automation could help you scale [PROCESS NAME] without hiring more staff?

If so, you can grab a time here: [CALENDLY LINK]

Or just reply with your availability and I'll send over some options.

Either way, happy to share a few quick wins you could implement even if we don't end up working together.

Best,
[YOUR NAME]

---

### Email 2: Proposal Follow-Up

**Subject:** Proposal for [PROJECT NAME] - Ready to Review

Hi [FIRST NAME],

Thanks again for the great conversation on [DATE]. I've put together a detailed proposal based on what we discussed.

**Quick Summary:**
- **What we're automating:** [PROCESS NAME]
- **Expected time savings:** [X HOURS] per week
- **Pricing:** $[X,XXX] [per month / one-time]
- **Timeline:** [X WEEKS] from kickoff to handoff

You can review the full proposal here: [LINK TO PROPOSAL PDF]

I've also included a few pricing options so you can choose the model that makes the most sense for your team (managed service vs full handoff).

**Next Steps:**
If this looks good, we can start as early as [DATE]. If you'd like to hop on a quick call to clarify anything, just let me know.

Looking forward to helping you automate [PROCESS NAME]!

Best,
[YOUR NAME]

**P.S.** If you have colleagues who'd benefit from seeing this, feel free to forward it along. I'm happy to answer any questions.

---

### Email 3: Handoff Completion and Training Invitation

**Subject:** [PROJECT NAME] is Live - Training Scheduled for [DATE]

Hi [FIRST NAME],

Great news! Your automated workflow for [PROCESS NAME] is officially live and running in production.

I've scheduled our training session for:
**Date:** [DATE]
**Time:** [TIME]
**Zoom Link:** [LINK]

During this session, we'll cover:
- How to monitor the workflow and check for errors
- How to modify triggers, inputs, or outputs
- How to troubleshoot common issues
- Best practices for making future changes

I'll also share my screen and walk through the entire system so you feel 100% confident operating it.

**Before the Call:**
Take a look at the documentation I sent over (especially the "Quick Start Guide"). Don't worry if it feels overwhelming—we'll go through everything step-by-step during training.

If you have specific questions or scenarios you'd like to cover during the session, just reply to this email and I'll make sure we address them.

See you on [DATE]!

Best,
[YOUR NAME]

---

### Email 4: 30-Day Check-In After Handoff

**Subject:** How's the [PROCESS NAME] workflow performing?

Hi [FIRST NAME],

It's been about a month since we handed off the [PROCESS NAME] automation, and I wanted to check in.

**How's it going?**
- Is the workflow running smoothly?
- Have you encountered any issues or edge cases we didn't anticipate?
- Are you seeing the time savings we projected?

If everything's working perfectly, great! You're all set. If there's anything that's unclear or not working as expected, let me know and I'll help you troubleshoot (still covered under the warranty period).

Also, if you're interested in expanding the workflow—adding new features, integrating additional tools, or automating other processes—I'd be happy to put together a quick proposal.

Either way, thanks for trusting me with this project. It's been great working with [COMPANY NAME].

Best,
[YOUR NAME]

**P.S.** If you know anyone else who could benefit from workflow automation, I'd appreciate the referral. Happy to offer a discount to any colleagues you send my way.

---

```
┌─────────────────────────────────────────────────────┐
│  DOWNLOAD EDITABLE TEMPLATES                        │
│                                                      │
│  Get Word docs and PDFs of all these templates      │
│  ready to customize for your business:              │
│                                                      │
│  travissteel.net/the-last-employee/resources#client-handoff     │
│                                                      │
│  Includes: Intake form, proposals, email scripts,   │
│  and the 3-question decision guide.                 │
└─────────────────────────────────────────────────────┘
```

---

## How to Use These Templates in Practice

### Step 1: Qualify with the Intake Form

Send the intake form before scheduling a discovery call. This eliminates unqualified leads and ensures you're spending time only with prospects who have real budgets and clear pain points.

### Step 2: Use the 3-Question Decision Guide

During or immediately after the discovery call, run through the three questions:
1. Are they technical?
2. Do they want ongoing support?
3. What's their budget?

Your answers will tell you which proposal template to use.

### Step 3: Customize the Proposal

Don't just find-and-replace [CLIENT NAME]. Take the time to:
- Reference specific pain points from the intake form
- Use their language (if they say "lead gen," don't call it "customer acquisition")
- Include their success metrics in the executive summary
- Adjust pricing based on complexity and value delivered

### Step 4: Follow Up Strategically

Don't send a proposal and go silent. Follow up 2-3 days later with Email Template 2. If no response, follow up again after 5-7 days with a simple: "Just circling back—did you get a chance to review the proposal? Happy to answer any questions."

### Step 5: Deliver with Excellence

Once they sign, over-communicate. Send weekly updates during the build. Deliver on time. Make the training session valuable. Check in after 30 days.

Your goal isn't just to complete the project. It's to create a client who refers you to three more clients.

---

## Common Objections and How to Address Them

**"This seems expensive."**
→ "I hear you. Let me break down the ROI: You're currently spending [X HOURS] per week on [PROCESS]. That's [Y HOURS] per year. If we conservatively value your team's time at $[Z]/hour, you're spending $[TOTAL] per year on this process. Our solution pays for itself in [TIMEFRAME] and continues saving you money every month after that."

**"Can't we just use Zapier?"**
→ "Great question. Zapier works well for simple trigger-action workflows. But what you're describing requires [multi-step logic / AI decision-making / custom data transformations] that Zapier can't handle. That said, we actually use Zapier-like tools (like n8n) as part of the solution—we just wrap them around more powerful custom logic."

**"What if we want to change something after you're done?"**
→ "That's exactly why we document everything in natural language (directives) alongside the code. You'll be able to understand what each part does and make changes. For small tweaks, you can do it yourself. For bigger changes, we're available on an hourly basis. Or you can hire any developer—the code is yours."

**"How do we know this will actually work?"**
→ "We build in phases. You'll see the workflow working in a test environment before we deploy to production. And we include a 30-day warranty, so if anything breaks or doesn't work as expected, we fix it at no cost. Our goal is to deliver something you trust and can rely on."

---

## Final Thoughts

These templates are starting points, not scripts. The best proposals are customized to the client's unique situation, written in their language, and focused on their specific outcomes.

But having a foundation to work from saves hours of staring at a blank page. Use these templates, adapt them to your voice, and refine them based on what works in your market.

The clients who get the most value from agentic workflows aren't the ones who want the fanciest AI. They're the ones who have a clear problem, a realistic budget, and a willingness to trust the process.

Your job is to help them see that automation isn't just about saving time. It's about reclaiming focus, scaling without overwhelm, and building a business that doesn't depend on you doing everything manually.

Now go close some deals.

---

**Cross-References:**
- Chapter 18: The Hybrid Wrapper Strategy (n8n + Modal)
- Chapter 19: The Four Handoff Models
- Chapter 20: How to Sell Agentic Workflow Services
- Appendix F: Business Ideas and Use Cases