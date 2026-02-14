# Ebook Resource Hub Plan

## URL Structure
**Base URL:** `https://travissteel.net/the-last-employee/resources`

### Page Layout
A single resource hub page with anchored sections, or a landing page linking to individual resource pages. Recommend **single page with sections** for simplicity on Zyro.

---

## Resource Categories & Downloads

### 1. Framework Templates
**Section anchor:** `/resources#templates`

| Resource | Format | Referenced In | Description |
|----------|--------|---------------|-------------|
| GEMINI.md Orchestrator Template | `.md` (copy-paste + download) | Ch 6, Appendix A | Complete orchestrator prompt - the brain of the system |
| Coder Agent Definition | `.md` | Ch 14, Appendix B | Implementation specialist prompt |
| Tester Agent Definition | `.md` | Ch 14, Appendix B | Visual verification specialist prompt |
| Stuck Agent Definition | `.md` | Ch 14, Appendix B | Human escalation agent prompt |
| Deployer Agent Definition | `.md` | Ch 14, Appendix B | Cloud deployment specialist prompt |
| Support Agent Definition | `.md` | Ch 14, Appendix B | Production self-annealing agent prompt |
| Folder Structure Starter | `.zip` | Ch 6 | Pre-configured project skeleton with all folders |

### 2. Directive Templates
**Section anchor:** `/resources#directives`

| Resource | Format | Referenced In | Description |
|----------|--------|---------------|-------------|
| Blank Directive Template | `.md` | Ch 7, Ch 27, Appendix C | Fill-in-the-blank directive with instructions |
| Lead Gen Directive Example | `.md` | Ch 22, Appendix C | Complete directive for lead qualification pipeline |
| Content Pipeline Directive Example | `.md` | Ch 23, Appendix C | Complete directive for content production |
| Invoice Processing Directive Example | `.md` | Ch 24, Appendix C | Complete directive for invoice automation |
| Hybrid Wrapper Deployment Directive | `.md` | Ch 10, Ch 18, Appendix D | Step-by-step cloud deployment workflow |
| Shadow Orchestrator Directive | `.md` | Ch 12, Appendix D | Production self-annealing pattern |
| Modal Endpoint Guide | `.md` | Ch 10, Appendix D | Reference for building Modal endpoints |

### 3. Code Templates
**Section anchor:** `/resources#code`

| Resource | Format | Referenced In | Description |
|----------|--------|---------------|-------------|
| Modal App Template | `.py` | Ch 10, Ch 18 | Basic Modal endpoint with auth + Gemini AI |
| Shadow Orchestrator Template | `.py` | Ch 12 | Advanced Modal endpoint with self-annealing |
| .env Example | `.env` | Ch 6 | Environment variable template |
| .mcp.json Config | `.json` | Ch 17 | Playwright MCP configuration |
| package.json | `.json` | Ch 6 | Node dependencies for MCP tools |

### 4. Client Handoff Templates
**Section anchor:** `/resources#client-handoff`

| Resource | Format | Referenced In | Description |
|----------|--------|---------------|-------------|
| Client Intake Form | `.md` / `.pdf` | Ch 20, Appendix G | Pre-call questionnaire |
| Managed Service Proposal | `.md` / `.pdf` | Ch 20, Appendix G | Retainer model proposal template |
| Full Handover Proposal | `.md` / `.pdf` | Ch 20, Appendix G | One-time delivery proposal template |
| Handoff Decision Guide | `.md` / `.pdf` | Ch 20, Appendix G | 3-question decision tree for picking delivery model |
| n8n Workflow Template | `.json` | Ch 18 | Example n8n workflow for Hybrid Wrapper |

### 5. Quick Reference Cards
**Section anchor:** `/resources#reference`

| Resource | Format | Referenced In | Description |
|----------|--------|---------------|-------------|
| Skills Quick-Reference Card | `.pdf` | Ch 16, Appendix F | One-page summary of all skills |
| MCP Configuration Reference | `.pdf` | Ch 17, Appendix E | Setup guide for key MCPs |
| Modal Deployment Checklist | `.pdf` | Ch 10, Appendix D | Pre-flight checklist for going live |
| DOE Terminology Glossary | `.pdf` | Throughout | Key terms and definitions |
| Troubleshooting Decision Tree | `.pdf` | Appendix H | When to use which agent / what to do when stuck |

### 6. The Complete Starter Kit (All-in-One Download)
**Section anchor:** `/resources#starter-kit`

A single `.zip` download containing everything above, organized in the correct folder structure:

```
agentic-workflows-starter-kit/
├── .antigravity/
│   ├── GEMINI.md
│   └── agents/
│       ├── coder.md
│       ├── tester.md
│       ├── stuck.md
│       ├── deployer.md
│       └── support.md
├── directives/
│   ├── TEMPLATE.md
│   ├── hybrid-wrapper-deployment.md
│   ├── shadow-orchestrator.md
│   ├── modal-endpoint-guide.md
│   └── client-handoff/
│       ├── handoff-decision-guide.md
│       ├── managed-service-proposal.md
│       ├── full-handover-proposal.md
│       └── client-intake-form.md
├── templates/
│   ├── modal_app_template.py
│   └── shadow_orchestrator_template.py
├── examples/
│   ├── lead-gen-directive.md
│   ├── content-pipeline-directive.md
│   └── invoice-processing-directive.md
├── .env.example
├── .mcp.json
├── package.json
└── README.md
```

---

## Implementation on Zyro

### Option A: Single Resource Page (Recommended)
- Create one new page: `/resources`
- Use sections with anchors for each category
- Each resource gets a "Copy" button (code block) + download link
- Host files on GitHub repo (public) and link from the page
- Add email gate for the Starter Kit zip (lead capture)

### Option B: Resource Hub with Sub-Pages
- Landing page: `/resources`
- Sub-pages for each category
- More SEO surface area but more pages to maintain on Zyro

### Recommendation
**Option A** with a **public GitHub repo** for the actual files. The Zyro page acts as the pretty front door with descriptions and context, GitHub hosts the raw files. This way:
- Files are version-controlled and always up to date
- No file hosting limits on Zyro
- Readers can also star/fork the repo
- You can track downloads via GitHub insights

### GitHub Repository
- **Repo:** `https://github.com/Travissteel/Agentic-Workflows-for-Automating-Any-Business-book`
- **Visibility:** Public (confirmed, pushed)
- **Organization:** Under Travissteel account
- **Link from:** Every chapter that references a template, the resource page, and the book's introduction
- **Note:** Downloadable resource files will live in a `resources/` folder in this repo alongside the book content

---

## Lead Capture Strategy

### Free Resources (No Gate)
- Individual templates (copy-paste from page)
- Code snippets
- Quick reference cards
- All files on GitHub

### Gated Resources (Email Required)
- Complete Starter Kit `.zip` (all-in-one download)
- Bonus: video walkthrough of setup (if you create one later)
- Bonus: private community/Discord access

This gives readers immediate value (free templates) while building your email list with the premium bundle.

### Newsletter Signup Integration

**Primary placement - persistent on page:**
- Sticky newsletter signup form embedded on the resource page
- Position: between the free resources and the Starter Kit section (natural conversion point)
- Also include in footer of the page

**Newsletter value proposition (not just "subscribe"):**

```
┌─────────────────────────────────────────────────────────┐
│  THE AGENTIC WORKFLOWS NEWSLETTER                       │
│                                                          │
│  Weekly tips on building AI systems that run             │
│  your business - new templates, use cases, and           │
│  framework updates delivered every Tuesday.              │
│                                                          │
│  [Your email]  [Subscribe]                               │
│                                                          │
│  + New directive templates monthly                       │
│  + Real-world automation case studies                    │
│  + Early access to framework updates                    │
│  + Unsubscribe anytime                                  │
└─────────────────────────────────────────────────────────┘
```

**Secondary placements:**
1. **Top of page:** Subtle banner - "Get updates when new resources are added"
2. **After Starter Kit download:** Post-download thank you page with newsletter opt-in
3. **Exit intent popup:** "Before you go - want weekly automation tips?"

**Newsletter content ideas (to plan ahead):**
- Weekly template drops (one new directive per week)
- "Workflow of the week" - real use case breakdown
- Framework updates (new skills, MCPs, agent improvements)
- Reader Q&A / troubleshooting tips
- Client success stories
- Industry-specific automation ideas

**Email platform options:**
| Platform | Free Tier | Best For |
|----------|-----------|----------|
| ConvertKit | 1,000 contacts | Creators, courses, sequences |
| Beehiiv | 2,500 contacts | Newsletter-first, referral program built in |
| Mailchimp | 500 contacts | General email marketing |
| Buttondown | 100 contacts | Simple, developer-friendly |

**Recommended:** ConvertKit or Beehiiv. Both designed for content creators building an audience around a methodology.

**Eat your own dogfood opportunity:**
Build the newsletter signup -> welcome sequence -> weekly send pipeline USING the DOE framework itself. This becomes:
1. A real working example for the book (Chapter 23: Content & Marketing)
2. Your own lead nurture system
3. Proof that the framework works for marketing automation

---

## In-Book References

Every chapter that references a downloadable resource should include a callout box:

```
┌─────────────────────────────────────────────────────┐
│  DOWNLOAD THIS TEMPLATE                             │
│                                                      │
│  Get the [Orchestrator Template] ready to use:       │
│  travissteel.net/the-last-employee/              │
│      resources#templates           │
│                                                      │
│  Or grab the complete Starter Kit with everything:   │
│  travissteel.net/the-last-employee/              │
│      resources#starter-kit         │
└─────────────────────────────────────────────────────┘
```

---

## Resource Page Copy (Draft)

### Hero Section
**Headline:** Agentic Workflows Resource Hub
**Subheadline:** Everything you need to build AI systems that run your business - templates, code, and ready-to-use starter kits from the book.

### Intro Paragraph
Welcome to the companion resource hub for *The Last Employee: Why the Future of Business is One Person and a Self-Healing AI System*. Below you'll find every template, agent definition, directive, and code sample referenced in the book. Copy-paste what you need, or download the complete Starter Kit to get running in minutes.

### CTA
**Get the Complete Starter Kit** - All templates, agents, directives, and code in one download. Enter your email and we'll send it right over.
