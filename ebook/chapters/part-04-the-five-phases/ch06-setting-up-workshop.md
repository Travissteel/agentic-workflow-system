# Chapter 6: The AI War Room: Phase 1 Setup

## The Industrialization of Intelligence

Most people approach AI as a toy—a clever chatbot to draft an email or summarize a meeting. If that’s your goal, close this book and go back to ChatGPT.

But if you’re here to build a **Workforce of One**, you need to stop treating AI as a conversation and start treating it as an engine. 

The primary reason 99% of businesses fail to automate is that they lack a "War Room." They try to build complex systems using nothing but a browser tab. It’s like trying to build a high-performance race car with a hammer and a prayer. It doesn't work, it’s prone to error, and it’s impossible to scale.

To build autonomous workflows, you need a controlled environment where AI agents have:
1. **The Blueprint**: Instructions they can read and update.
2. **The Tools**: Permission to write code, access data, and run scripts.
3. **The Sandbox**: A safe space to fail, self-heal, and improve without breaking your mission-critical systems.

In this chapter, we are going to build your Infrastructure Stack. We’re moving from the "copy-paste hamster wheel" to a production-grade AI workshop. This isn't just software installation. This is the industrialization of your business logic.

By the end of this session, you will have a functioning AI War Room ready to deploy autonomous agents at scale.

---

## The Infrastructure Stack: Why This Works

We don’t use chatbots for automation. We use the **Antigravity IDE**. Here is the tactical advantage of this environment:

**1. The Command Center (Gemini 2.0 Flash)**
This is your Project Manager. It doesn’t just "talk"—it orchestrates. It reads your business playbooks, delegates the dirty work to subagents, and maintains the mission state across 1M+ tokens of context.

**2. The Execution Layer (VS Code Core)**
We build on the industry standard. Your agents live inside the same environment professional software engineers use. They create, edit, and organize your business assets with precision.

**3. Strategic Permissions**
We give the AI "hands." Permission to run terminal commands, install dependencies, and launch browser automation. It’s the difference between a consultant who gives advice and a specialist who does the work.

**4. The Self-Healing Loop**
This is the "Secret Sauce" of the DOE Framework. When a workflow hits a wall, the system doesn't just crash. It diagnoses the failure, fixes the execution code, and updates the master directive to prevent the error from ever happening again. This is **Battle-Hardening** in real-time.

**The Cost:** Zero. By using Gemini 2.0 Flash, you get 1,500 requests per day for free. That is enough to run a small army of agents without spending a cent on operational overhead.

---

## How It Works

Google Antigravity IDE combines several powerful tools into a single, cohesive environment:

**1. The Orchestrator (Gemini 2.0 Flash)**
- The "project manager" AI that maintains the big picture
- Reads your directives (business playbooks in plain English)
- Breaks work into tasks and delegates to specialist agents
- Tracks progress across your entire project
- Uses Google's free, powerful Gemini 2.0 Flash model

**2. The Workspace (VS Code Foundation)**
- Built on Visual Studio Code (the most popular code editor in the world)
- File explorer, terminal, and editor all in one interface
- Agents can create, edit, and organize files automatically
- You can manually review or edit anything agents create

**3. Agentic Permissions**
- AI can read and write files in your project folder (not your entire computer)
- AI can run terminal commands (install dependencies, run scripts)
- AI can launch browser automation (test websites, take screenshots)
- All sandboxed for security—agents only access what you explicitly allow

**4. Built-in MCPs (Model Context Protocol)**
- MCPs are "hands" for AI—they let agents interact with real systems
- Playwright MCP: browser automation for testing and scraping
- File system MCP: read CSVs, process PDFs, save outputs
- More MCPs installable as needed (databases, email, CRM, etc.)

**5. The Self-Annealing Loop**
- When agents hit errors, they diagnose the problem
- They fix the code AND update their directives with learnings
- Your system gets smarter every time it runs
- Battle-hardening without your intervention

**The cost?** Free. Google provides Gemini 2.0 Flash with a generous free tier (1,500 requests per day for personal use). For most business automation, you'll never hit the limit.

---

## Real Example

Let me show you the difference between "ChatGPT copy-pasting" and "Antigravity workshop automation" with a real scenario.

**The task:** Process 50 invoices (mix of PDFs and images) to extract customer name, invoice amount, due date, and save everything to a spreadsheet.

**The ChatGPT approach:**
1. Open first invoice PDF
2. Copy the text into ChatGPT
3. Ask ChatGPT to extract the data
4. Copy ChatGPT's response into Excel
5. Repeat 49 more times
6. Manually fix formatting inconsistencies (ChatGPT gave you dates in three different formats)
7. Total time: 2-3 hours
8. Mental state: Drained, questioning your life choices

**The Antigravity approach:**
1. Write a directive (one time, 5 minutes): "Process all invoices in the /invoices folder. Extract customer name, invoice amount, and due date. Save results to invoices.csv with consistent formatting."
2. Run the directive
3. The orchestrator reads the instruction
4. It delegates to the coder agent: "Build a script that processes PDFs and images, extracts structured data, and saves to CSV"
5. Coder writes a Python script using OCR libraries
6. Tester agent verifies the output with sample invoices
7. The script processes all 50 invoices in 2 minutes
8. You review invoices.csv (perfect formatting, ready to import)
9. Total time: 5 minutes setup + 2 minutes processing + 3 minutes review = 10 minutes
10. Mental state: Impressed, wondering what else you can automate

**The real win:** Next month, you run the same directive on 200 invoices. Still takes 10 minutes. The time savings compound forever.

This is why you need a workshop, not just a chatbot.

---

---

## Deployment: The AI War Room Setup

Follow these directives precisely. You are building the foundation of your automated workforce. Do not cut corners.

### Mission Step 1: Install the Environment

**Target:** [antigravity.dev/download](https://antigravity.dev/download)

1. **Download the Package:** Get the installer for your OS. It’s free and open-source.
2. **Install with Default Defaults:** Don't get creative with custom paths yet. Stick to the standard installation.
3. **Verify Connection:** 
   - Click "Configure AI."
   - Generate your free Gemini API key from [ai.google.dev](https://ai.google.dev).
   - Paste the key.
   - Click "Verify Connection."
   - **Crucial:** You must see: "Connected to Gemini 2.0 Flash ✓" before proceeding.

### Mission Step 2: Establish the Physical Workspace

Create a dedicated folder for your AI operations. Do not store these in cloud-synced folders (Dropbox, OneDrive). The constant background syncing will create "Race Conditions" that confuse the agents and break your logic.

- **Windows Strategic Location:** `C:\AI-Projects\`
- **Mac/Linux Strategic Location:** `~/AI-Projects/`

### Mission Step 3: Initialize the Project Blueprint

In your new project folder, we need to create the standardized DOE structure. Antigravity agents are trained to recognize this specific layout.

**The War Room Structure:**
- `.antigravity/` → The brain (Master Instructions + Agents).
- `directives/` → Your business logic (Plain English).
- `executions/` → The deterministic code (Scripts).
- `.env` → The secure vault (API keys).

**Strategic Shortcut:** 
Open the Antigravity IDE, go to the chat panel, and type:
*"Initialize standard DOE project structure with all agent definitions (coder, tester, stuck)."*

Watch the system build its own skeleton in seconds.

---

### Step 3: Initialize the Antigravity Structure (5 minutes)

This is the critical step. We're creating a specific folder structure that Antigravity agents expect—like building the shelves, drawers, and tool racks in a carpenter's workshop.

**The structure you're building:**

```text
invoice-processor/
├── .antigravity/                    # Orchestrator configuration
│   ├── GEMINI.md               # Master instructions for orchestrator
│   └── agents/                 # Specialist agent definitions
│       ├── coder.md            # The implementation specialist
│       ├── tester.md           # The quality assurance specialist
│       └── stuck.md            # The human escalation specialist
├── .gemini/                    # Gemini-specific config (optional)
│   └── GEMINI.md               # Gemini model preferences
├── directives/                 # Your business playbooks (plain English)
│   └── (your directive files go here)
├── executions/                 # Code that agents write
│   └── (Python scripts, JS files automatically created)
├── .env                        # API keys and secrets
├── .gitignore                  # Prevents committing secrets
└── README.md                   # Project overview
```

**Why each folder matters:**

- **`.antigravity/GEMINI.md`**: The "brain" of your orchestrator. Read every session. Contains the high-level strategy: how to delegate tasks, when to test, when to escalate to humans.

- **`.antigravity/agents/`**: Job descriptions for each specialist agent. The coder knows how to implement. The tester knows how to verify. The stuck agent knows when to ask you for help.

- **`.gemini/GEMINI.md`**: Optional Gemini-specific settings (model preferences, temperature, token limits). Most projects don't need this.

- **`directives/`**: Your business logic in plain English markdown files. "When an invoice arrives, extract customer name, amount, due date, and save to Airtable." The orchestrator reads these and translates them into executable tasks.

- **`executions/`**: The deterministic code (Python scripts, JavaScript) that agents write to implement your directives. You rarely touch these—agents manage them automatically.

- **`.env`**: Your secrets (API keys, passwords, database credentials). Never hardcoded in scripts, always stored separately for security.

- **`.gitignore`**: Tells Git to ignore `.env` and other sensitive files. Prevents accidentally publishing API keys to GitHub.

**How to create it (easiest method):**

In the Gemini chat panel (right side of Antigravity), paste this:

```
Please set up the Antigravity project structure. I need:
- .antigravity/ folder with GEMINI.md and agents/ subfolder
- agent definitions for coder.md, tester.md, stuck.md
- .gemini/ folder with GEMINI.md
- directives/ folder (empty)
- executions/ folder (empty)
- .env file with placeholders
- .gitignore that excludes .env
- README.md with basic project info

Use the standard Antigravity templates for all agent definitions.
```

Press Enter. The orchestrator will create everything in 10-15 seconds. You'll see files appear in the left sidebar as they're created.

**Alternative: Download the Starter Kit**

Visit the resources page and download the pre-configured template:

```
┌─────────────────────────────────────────────────────┐
│  DOWNLOAD THE ANTIGRAVITY STARTER KIT               │
│                                                      │
│  Pre-configured folder structure + agent            │
│  definitions + sample directives + .env template:   │
│                                                      │
│  travissteel.net/the-last-employee/                      │
│      resources#starter-kit         │
│                                                      │
│  Extract the ZIP into your project folder and       │
│  you're ready to go in 30 seconds.                  │
└─────────────────────────────────────────────────────┘
```

---

### Step 4: Configure Agent Permissions (3 minutes)

By default, AI assistants can only chat. We're about to give them hands—the ability to create files, run commands, and test websites.

This is what transforms Antigravity from a chatbot into an autonomous workshop.

**Enable agentic mode:**

1. Click the **Settings** icon (⚙️) in the bottom-left corner
2. Or use keyboard shortcut: `Ctrl+,` (Windows/Linux) or `Cmd+,` (Mac)
3. Search for: **"Agent Mode"** or **"Autonomous Mode"**
4. Toggle the setting to **ON**
5. You'll see a confirmation: "AI agents can now read/write files and execute terminal commands in this workspace"

**What this enables:**

- **File operations:** Agents can create, edit, and delete files inside your project folder (NOT your entire system—only the workspace)
- **Terminal commands:** Agents can run `pip install`, `npm run`, `python script.py`, etc.
- **Browser control:** Agents can launch Playwright, navigate websites, click buttons, take screenshots, verify visual output

**Security boundaries:**

- Agents can ONLY access files inside your project folder
- They cannot read your personal documents, browse your entire hard drive, or access other applications
- They cannot install system-level software or modify OS settings
- This is a sandboxed environment by design

**Save and restart:**

1. Close the settings panel
2. Restart Antigravity IDE (File → Restart or Ctrl+Q)
3. Reopen your project folder (it should auto-reopen)

**If you're nervous about permissions:** Completely understandable. Start with a test project (like we're doing now) before connecting agents to real business data. Build trust gradually by seeing what they do.

---

### Step 5: Set Up Your .env File (5 minutes)

This file stores your secrets—the API keys, passwords, and tokens that authenticate your agents with external services.

Think of it as a locked drawer in your workshop where you keep the valuable tools.

**Create the .env file:**

1. In the file explorer sidebar, right-click your project root folder
2. Select **New File**
3. Name it exactly: `.env` (note the period at the start)
4. Click the file to open it in the editor

**Add your credentials:**

Copy this template and paste it into `.env`:

```text
# Antigravity AI Workshop - Environment Variables
# NEVER commit this file to version control!

# AI Provider API Keys (you need at least one)
GOOGLE_API_KEY=your_gemini_api_key_here
ANTHROPIC_API_KEY=your_anthropic_key_here
OPENAI_API_KEY=your_openai_key_here

# Optional: Services you might integrate later
AIRTABLE_API_KEY=your_airtable_key
HUBSPOT_API_KEY=your_hubspot_key
STRIPE_API_KEY=your_stripe_key
MODAL_TOKEN_ID=your_modal_token_id
MODAL_TOKEN_SECRET=your_modal_token_secret

# Database credentials (if needed)
DATABASE_URL=postgresql://user:password@host:port/database
```

**Fill in your actual keys:**

Replace `your_gemini_api_key_here` with your real API key from [ai.google.dev](https://ai.google.dev).

Leave blank any services you're not using yet. You can add them later as needed.

**Secure the file:**

1. Open `.gitignore` (should already exist from Step 3)
2. Verify it contains this line: `.env`
3. If not, add it
4. Save `.gitignore`

This prevents Git from tracking your secrets. Critical for security.

**Where to get API keys:**

- **Google Gemini:** [ai.google.dev](https://ai.google.dev) → Get API Key (free tier: 1,500 requests/day)
- **Anthropic Claude:** [console.anthropic.com](https://console.anthropic.com) → API Keys ($5 free credit)
- **OpenAI:** [platform.openai.com](https://platform.openai.com) → API Keys ($5 free credit)

**Cost awareness:**

Start with Google Gemini's free tier (more than enough for most projects). If you need more capacity or want to use Claude/GPT-4:

- Typical automation project: $5-10/month
- High-volume production workflow: $50-100/month (but saving you 40+ hours of manual work)
- Set billing alerts in your provider dashboard to avoid surprises

---

### Step 6: Your First "Hello World" Test (5 minutes)

Time to verify everything works. This is like a carpenter testing their saw before starting the real project.

**Create a test directive:**

1. In the `directives/` folder, create a new file: **`test.md`**
2. Paste this content:

```markdown
# Test Directive

**Objective:** Verify the AI Workshop is functioning correctly

**Inputs:** None (this is a self-contained test)

**Process:**
1. Create a file named `hello.txt` in the project root folder
2. Write the following text into the file: "The workshop is live! Today is [current date]."
3. Verify the file was created successfully
4. Report back with confirmation

**Definition of Done:**
- File `hello.txt` exists in project root
- File contains correct text with today's date
- No errors occurred during creation
```

3. Save the file (Ctrl+S or Cmd+S)

**Run the test:**

1. In the Gemini chat panel (right sidebar), type:

```
Please execute the directive in directives/test.md
```

2. Press Enter

**What should happen:**

You'll see the orchestrator spring into action:

1. It reads `directives/test.md`
2. It understands the objective (create a test file)
3. It delegates to the coder agent: "Create hello.txt with the specified content"
4. Coder creates the file
5. Tester verifies it exists and contains correct content
6. Orchestrator reports back: "Task complete. File created successfully."
7. You see `hello.txt` appear in your file explorer sidebar

**Verify the output:**

1. Click `hello.txt` in the sidebar
2. It should open in the editor
3. You should see: "The workshop is live! Today is February 13, 2026." (or whatever today's date is)

**If it works:**

Congratulations! Your AI Workshop is operational. You just witnessed:
- Orchestrator reading a directive
- Delegation to specialist agents
- Code execution
- Verification
- Completion report

Everything is configured correctly.

**If it doesn't work, common issues:**

| Error | Likely Cause | Fix |
|-------|--------------|-----|
| "Permission denied" | Agentic mode not enabled | Go back to Step 4, enable agent permissions, restart |
| "Cannot find directive" | File in wrong location | Ensure `test.md` is in `directives/` folder, not project root |
| "API key error" | Invalid or missing key | Check `.env` has correct Gemini API key with no typos |
| "Agent not responding" | Application needs restart | Restart Antigravity IDE (File → Restart) |

**Debugging tip:** If you get an error, copy the error message and ask Gemini: "I got this error: [paste error]. What's the likely cause and how do I fix it?" The orchestrator is excellent at diagnosing setup problems.

---

## Common Setup Mistakes to Avoid

Learn from others' pain. These are the top five mistakes that trip up first-time builders:

**1. Skipping the Hello World Test**

*The mistake:* "I'll test it when I build something real."

*Why it hurts:* You won't know if your workshop is properly configured until you're deep into a complex project, hitting cryptic errors, unsure if the problem is your directive, the agent's code, or a broken environment.

*The fix:* Always run the hello world test. It takes 5 minutes and saves hours of frustration later.

**2. Using Cloud-Synced Project Folders**

*The mistake:* "I'll put my AI Workshop in Dropbox so I can access it from multiple devices."

*Why it hurts:* Sync conflicts destroy agent workflows. File locking, delayed writes, version mismatches. Agents write code, the cloud sync "helpfully" reverts it to an older version, and chaos ensues.

*The fix:* Use a local folder (not synced). If you need multi-device access, use Git for version control (sync code intentionally, not continuously).

**3. Ignoring Folder Structure Conventions**

*The mistake:* "I'll just put everything in one folder. Why does structure matter?"

*Why it hurts:* Agents rely on convention. The orchestrator expects directives in `directives/`, code in `executions/`, agent definitions in `.antigravity/agents/`. Random organization confuses the system. You'll waste hours debugging path errors.

*The fix:* Follow the Antigravity structure exactly. Once you understand why it's designed this way, you can customize. But start with the blueprint.

**4. Not Verifying API Key Quotas**

*The mistake:* Assuming the free tier is unlimited.

*Why it hurts:* Gemini's free tier is generous (1,500 requests/day) but not infinite. Complex workflows can use 50-100 requests. If you hit your limit mid-task, workflows fail cryptically.

*The fix:* Monitor your quota in the Google AI Studio dashboard. Upgrade to pay-as-you-go if you're doing high-volume work (still very cheap).

**5. Committing .env to GitHub**

*The mistake:* Accidentally pushing your `.env` file to a public repository.

*Why it hurts:* Your API keys are now public. Malicious actors will find them, steal them, and rack up charges on your account within hours.

*The fix:* Always verify `.env` is in `.gitignore` before your first commit. If you accidentally push it, regenerate all API keys immediately (within 5 minutes).

---

## Key Takeaway

**Your workshop is the foundation. Spend 30 minutes setting it up correctly, and you'll save 30 hours of troubleshooting later.**

Think of it like this: A carpenter can technically build furniture with dull tools, bad lighting, and no workbench. But they'll work five times slower, make more mistakes, and hate every minute of it.

The workshop isn't optional. It's what separates frustration from flow state.

You've now built:
- A properly configured orchestrator environment (Google Antigravity IDE)
- A standardized folder structure where agents know where to find everything
- Secure credential storage (`.env` file)
- Agentic permissions that let AI act, not just advise
- Proof that it works (hello world test passing)

This workshop will serve you for every automation project you build. You set it up once. You use it forever.

In the next chapter, we'll fill this workshop with your first real directive—a business playbook that turns your manual process into an autonomous workflow. We'll take a messy, ad-hoc task (something you currently do manually every week) and translate it into a clear, AI-executable directive.

---

┌─────────────────────────────────────────────────────┐
│  RESOURCES FOR THIS CHAPTER                         │
│                                                      │
│  **Watch the Setup Video:**                         │
│  See me set up a fresh workshop from scratch in     │
│  under 10 minutes (with troubleshooting tips):      │
│  travissteel.net/the-last-employee/                      │
│      resources#setup-video         │
│                                                      │
│  **Download the Antigravity Starter Kit:**          │
│  Pre-configured folder structure + agent            │
│  definitions + sample directives + .env template:   │
│  travissteel.net/the-last-employee/                      │
│      resources#starter-kit         │
│                                                      │
│  **Troubleshooting Guide:**                         │
│  Common setup errors and fixes with screenshots:    │
│  travissteel.net/the-last-employee/                      │
│      resources#troubleshooting     │
│                                                      │
│  **Join the Community:**                            │
│  Get help, share your setup, see what others        │
│  are building:                                       │
│  travissteel.net/the-last-employee/community             │
└─────────────────────────────────────────────────────┘

---

> [!IMPORTANT]
> **Security Reminder:** Never commit your `.env` file to version control. This file contains your "digital cash"—the API keys that power your business automation. Add `.env` to `.gitignore` immediately after creating it. If you ever accidentally push it to GitHub, regenerate all keys within 5 minutes. Set up billing alerts on all API providers to catch unauthorized usage quickly.

---

## What's Next

Now that your workshop is ready, it's time to write your first business playbook.

In **Chapter 7: Phase 2 - Writing Your Business Playbook**, you'll learn how to translate your messy, ad-hoc processes into clear, AI-executable directives. We'll take a real business workflow—something you currently do manually every week—and turn it into a directive that agents can follow autonomously.

You'll learn:
- The four essential components of every directive (Objective, Inputs, Process, Definition of Done)
- How to write instructions that are clear to AI but flexible enough for edge cases
- The difference between "probabilistic" business logic (directives) and "deterministic" implementation (executions)
- How to test your directive before building the automation
- The common pitfalls that make directives fail (and how to avoid them)

We'll use concrete examples: invoice processing, lead scraping, client reporting. By the end of Chapter 7, you'll have written your first directive and be ready to hand it to your AI team for implementation.

**Turn to Chapter 7 →**
