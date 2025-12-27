# Claude Agentic Workflow System

**A reusable, powerful orchestration framework for building ANY software project with AI coding assistants**

Version: 2.2
License: MIT
Compatible with: Claude Code CLI, Gemini 2.5 (Antigravity IDE)
Last Updated: December 2024

---

## 🎯 What Is This?

This is a **generic, reusable multi-agent system** that transforms how you build software projects with AI coding assistants. It uses specialized subagents to manage complex projects from start to finish, with mandatory human oversight and visual testing.

**Works with both Claude Code and Gemini** - use whichever AI assistant you prefer!

**Use this system for ANY project:** web apps, APIs, mobile apps, scripts, automation tools, or any software development task.

---

## ⚡ Key Features

- **🧠 Orchestrator** - Large context window managing the big picture and todos (Claude 200K / Gemini 1M+)
- **✍️ Coder Subagent** - Implements one task at a time in isolated context
- **👁️ Tester Subagent** - Visual verification using Playwright MCP browser automation
- **🆘 Stuck Subagent** - Human escalation point (no automatic fallbacks)
- **📋 Todo Tracking** - Always see exactly where your project stands
- **🔄 Iterative Workflow** - Create todos → delegate to coder → test → repeat
- **🔀 Multi-Provider** - Works with Claude Code CLI and Gemini 2.5 (Antigravity IDE)
- **📏 Smart Task Splitting** - Automatically handles large tasks by splitting them into manageable pieces

---

## 🚀 Quick Start (Any Project)

### Prerequisites

1. **Claude Code CLI** installed ([docs](https://docs.claude.com/en/docs/claude-code))
2. **Node.js** (for Playwright MCP visual testing)
3. **Git** (optional, for version control)

### Step 1: Copy This System to Your Project

```bash
# Option A: Copy the entire system
cp -r /c/Users/travi/claude-agent-system /path/to/your-project/.

# Option B: Clone and copy
git clone <this-repo> /path/to/your-project/claude-agent-system
```

### Step 2: Navigate and Start Claude Code

```bash
cd /path/to/your-project/claude-agent-system
claude
```

The agents load automatically from the `.claude/` directory.

### Step 3: Tell Claude What to Build

Just describe your project naturally:

```
"Build a React todo app with TypeScript and Tailwind CSS"
```

OR

```
"Create a REST API with Express, PostgreSQL, and JWT authentication"
```

OR

```
"Build a Python script that scrapes website data and exports to CSV"
```

Claude will:
1. Create a detailed TodoWrite list
2. Delegate tasks to the coder subagent
3. Test implementations with the tester subagent
4. Ask you questions via stuck agent when needed
5. Complete the project iteratively

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────┐
│  YOU (User)                                     │
│  - Provides project requirements                │
│  - Makes decisions when agents ask              │
└────────────┬────────────────────────────────────┘
             │
             ↓
┌─────────────────────────────────────────────────┐
│  ORCHESTRATOR (Main Claude - 200K context)      │
│  - Creates comprehensive TodoWrite lists        │
│  - Maintains big picture and project state      │
│  - Delegates one task at a time to subagents    │
│  - Tracks overall progress                      │
└──┬────────┬────────┬─────────────────────────────┘
   │        │        │
   ↓        ↓        ↓
┌──────┐ ┌──────┐ ┌──────┐
│CODER │ │TESTER│ │STUCK │
│      │ │      │ │      │
│Fresh │ │Fresh │ │Asks  │
│context│ │context│ │you   │
│      │ │      │ │      │
│Builds│ │Visual│ │Human │
│code  │ │tests │ │input │
└──────┘ └──────┘ └──────┘
```

---

## 📋 The Workflow

```
USER: "Build X"
    ↓
ORCHESTRATOR: Creates detailed TodoWrite list
    ↓
ORCHESTRATOR: Invokes coder(todo #1)
    ↓
CODER (fresh context): Implements feature
    ↓
    ├─→ Problem? → Invokes STUCK → You decide → Continue
    ↓
CODER: Reports completion
    ↓
ORCHESTRATOR: Invokes tester(verify todo #1)
    ↓
TESTER (fresh context): Playwright screenshots & verification
    ↓
    ├─→ Test fails? → Invokes STUCK → You decide → Continue
    ↓
TESTER: Reports success
    ↓
ORCHESTRATOR: Marks todo #1 complete ✓
    ↓
ORCHESTRATOR: Invokes coder(todo #2)
    ↓
... Repeat until all todos done ...
    ↓
ORCHESTRATOR: Reports final results to YOU
```

---

## 🤖 The Agents

### Orchestrator (Main Claude)
**Location:** `.claude/CLAUDE.md`
**Context:** 200K tokens (maintains entire project)

**Responsibilities:**
- Creates and maintains comprehensive todo lists using TodoWrite
- Maintains the big picture and project vision
- Delegates individual tasks to specialized subagents
- Tracks overall progress across all tasks
- Reports to user at key milestones

**What it does NOT do:**
- Implement code directly (delegates to coder)
- Test implementations (delegates to tester)
- Make assumptions (uses stuck agent for clarification)

### Coder Subagent
**Location:** `.claude/agents/coder.md`
**Context:** Fresh context per task

**Responsibilities:**
- Receives ONE specific todo item
- Implements clean, functional code
- Follows best practices for the language/framework
- NEVER uses fallbacks or workarounds
- Invokes stuck agent immediately when problems occur

**Tools Available:**
- Read, Write, Edit (file operations)
- Glob, Grep (search)
- Bash (terminal commands)
- Task (spawn other agents)

### Tester Subagent
**Location:** `.claude/agents/tester.md`
**Context:** Fresh context per test

**Responsibilities:**
- Verifies implementations by ACTUALLY RENDERING AND VIEWING them
- Uses Playwright MCP for visual testing
- Takes screenshots as proof
- Tests interactions (clicks, forms, navigation)
- NEVER marks failing tests as passing
- Invokes stuck agent when visual issues found

**Tools Available:**
- Task (for Playwright MCP)
- Read (to understand what was built)
- Bash (to run tests)

### Stuck Subagent
**Location:** `.claude/agents/stuck.md`
**Context:** Fresh context per problem

**Responsibilities:**
- Human escalation point for ANY problem
- Presents clear options for you to choose
- Blocks progress until you respond
- Returns your decision to the calling agent
- Ensures no blind fallbacks or workarounds

**This is the key differentiator:** No silent failures!

---

## 🎯 The "No Fallbacks" Rule

**Traditional AI:** Hits error → tries workaround → might fail silently

**This System:** Hits error → asks you → you decide → proceeds correctly

Every agent is hardwired to invoke the stuck agent rather than guess or use fallbacks. **You stay in control.**

---

## 💡 Example Sessions

### Example 1: React Todo App

```
YOU: "Build a React todo app with TypeScript and Tailwind CSS"

ORCHESTRATOR creates todos:
  [ ] Initialize Next.js with TypeScript
  [ ] Set up Tailwind CSS
  [ ] Create TodoList component
  [ ] Create TodoItem component
  [ ] Add state management (useState)
  [ ] Style with Tailwind
  [ ] Test all functionality

ORCHESTRATOR invokes coder(todo #1)
CODER: Creates Next.js project with TypeScript
CODER: Reports completion

ORCHESTRATOR invokes tester("Verify Next.js app runs")
TESTER: Uses Playwright, takes screenshot
TESTER: Reports success

ORCHESTRATOR: Marks todo #1 complete ✓
ORCHESTRATOR invokes coder(todo #2)
... continues until all todos done
```

### Example 2: Python Data Scraper

```
YOU: "Build a Python script that scrapes product data from a website and exports to CSV"

ORCHESTRATOR creates todos:
  [ ] Set up Python project with dependencies (requests, beautifulsoup4, pandas)
  [ ] Create scraper function to fetch HTML
  [ ] Parse HTML to extract product data
  [ ] Store data in pandas DataFrame
  [ ] Export to CSV with proper formatting
  [ ] Add error handling
  [ ] Test with sample URL

ORCHESTRATOR invokes coder(todo #1)
CODER: Creates requirements.txt, installs packages
CODER: Reports completion

ORCHESTRATOR invokes coder(todo #2)
CODER: Implements scraper function
CODER: ERROR - Website requires authentication
CODER: Invokes STUCK agent

STUCK: Asks YOU:
  "Target website requires authentication. How to proceed?"
  Options:
  - Add authentication (provide credentials)
  - Use a different test website
  - Skip authentication for MVP

YOU choose: "Use a different test website (https://example.com)"

STUCK: Returns your decision to coder
CODER: Proceeds with example.com
... continues until done
```

### Example 3: Express REST API

```
YOU: "Create a REST API with Express, PostgreSQL, and JWT authentication"

ORCHESTRATOR creates todos:
  [ ] Initialize Node.js project with TypeScript
  [ ] Set up Express server
  [ ] Configure PostgreSQL connection
  [ ] Create database schema (users table)
  [ ] Implement user registration endpoint
  [ ] Implement login endpoint with JWT
  [ ] Add protected route with JWT middleware
  [ ] Add error handling middleware
  [ ] Test all endpoints

ORCHESTRATOR invokes coder(todo #1)
... delegates systematically ...
CODER builds each feature
TESTER verifies endpoints with test requests
... completes entire API
```

---

## 📂 Directory Structure

```
claude-agent-system/
├── .claude/                   # Claude Code configuration
│   ├── CLAUDE.md              # Orchestrator instructions
│   ├── settings.local.json    # Claude settings
│   └── agents/
│       ├── coder.md          # Coder subagent definition
│       ├── tester.md         # Tester subagent definition
│       └── stuck.md          # Stuck subagent definition
├── .gemini/                   # Gemini configuration
│   ├── GEMINI.md              # Orchestrator instructions
│   ├── settings.json          # Gemini settings
│   └── agents/
│       ├── coder.md          # Coder subagent definition
│       ├── tester.md         # Tester subagent definition
│       └── stuck.md          # Stuck subagent definition
├── .mcp.json                  # Playwright MCP configuration
├── .gitignore
├── README.md                  # This file
└── HOW-TO-USE.md             # Detailed usage guide

# Your project files will be created here:
├── (generated project structure)
│   ├── src/
│   ├── package.json
│   └── ...
```

---

## 🎓 How to Use for Different Project Types

### Web Applications (Next.js, React, Vue)

```
"Build a [app type] with [features] using [tech stack]"

Example:
"Build a blog with user authentication using Next.js 14, TypeScript, and Supabase"
```

### APIs (Express, FastAPI, Django)

```
"Create a REST API with [endpoints] using [framework] and [database]"

Example:
"Create a REST API with CRUD operations for a task manager using Express and MongoDB"
```

### Scripts & Automation

```
"Build a Python/Node script that [does something]"

Example:
"Build a Node.js script that monitors a folder and automatically backs up new files to S3"
```

### Mobile Apps (React Native)

```
"Build a [mobile app type] with [features] using React Native"

Example:
"Build a weather app with location-based forecasts using React Native and OpenWeather API"
```

### Desktop Apps (Electron)

```
"Create an Electron app that [functionality]"

Example:
"Create an Electron app that manages local markdown notes with search and tags"
```

---

## ⚙️ Customization

### Adding Custom Agents

Create a new agent file in `.claude/agents/your-agent.md`:

```markdown
---
name: your-agent
description: What this agent does
tools: Read, Write, Bash, etc.
model: sonnet
---

# Your Custom Agent

You are [agent role and purpose]

## Your Mission
[Describe what this agent should do]

## Workflow
1. [Step 1]
2. [Step 2]
...

## When to Invoke Stuck Agent
[Conditions that require human input]
```

Then invoke from orchestrator:
```
Invoke the your-agent subagent for [specific task]
```

### Modifying Agent Behavior

Edit the agent files in `.claude/agents/` to customize:
- Available tools
- Workflow steps
- Escalation triggers
- Success criteria

### Changing MCP Configuration

Edit `.mcp.json` to add more MCP servers:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"],
      "env": {}
    },
    "your-mcp-server": {
      "command": "your-command",
      "args": ["args"],
      "env": {}
    }
  }
}
```

---

## 🚨 Critical Rules for Success

### For You (The User):
1. ✅ Provide clear project requirements
2. ✅ Respond promptly when stuck agent asks questions
3. ✅ Trust the process - let agents complete tasks
4. ✅ Review screenshots from tester agent
5. ✅ Check TodoWrite list to track progress

### For the Orchestrator:
1. ✅ Create detailed TodoWrite lists immediately
2. ✅ Delegate ONE task at a time
3. ✅ Test EVERY implementation with tester
4. ✅ Update todos after each completion
5. ✅ NEVER create header/footer links without creating pages (prevents 404s)

### For All Agents:
1. ✅ INVOKE STUCK AGENT for any problem, uncertainty, or error
2. ✅ NEVER use fallbacks or workarounds
3. ✅ NEVER skip testing
4. ✅ NEVER make assumptions about requirements

---

## 📊 Success Metrics

A project is COMPLETE when:
- ✅ All todos marked complete in TodoWrite
- ✅ All tests passing (tester verified with screenshots)
- ✅ Code runs without errors
- ✅ Requirements met (functionality matches user request)
- ✅ Zero 404 errors or broken links
- ✅ User satisfied with result

---

## 🐛 Troubleshooting

### "Agents not loading"
- Verify `.claude/` directory exists in current directory
- Check agent files exist: `.claude/agents/*.md`
- Restart Claude Code in the correct directory

### "Coder keeps failing"
- It should automatically invoke stuck agent
- Check if stuck agent is asking you a question
- Review error messages for clarity

### "Tester not providing screenshots"
- Ensure Node.js is installed (required for Playwright)
- Check `.mcp.json` configuration
- Verify Playwright MCP can run: `npx @playwright/mcp@latest`

### "Progress seems slow"
- Normal! Complex tasks take time
- Check TodoWrite list for progress
- Ask orchestrator: "What's the current status?"

### "Too many questions from stuck agent"
- Good! That means no silent failures
- Agents are being thorough
- Your decisions guide the project correctly

---

## 💡 Pro Tips

1. **Start Small** - Test the system with a simple project first
2. **Be Specific** - The more detailed your requirements, the better the result
3. **Trust Screenshots** - Tester provides visual proof of every feature
4. **Quick Decisions** - When stuck agent asks, respond promptly
5. **Check Todos** - Progress is always visible in TodoWrite
6. **Iterate** - You can always ask for changes after completion

---

## 🎓 Best Practices

### Write Clear Requirements

**❌ Bad:**
```
"Build a website"
```

**✅ Good:**
```
"Build a portfolio website with:
- Homepage with hero section and project grid
- About page with bio and skills
- Contact form that sends emails
- Responsive design for mobile
- Dark mode toggle
Technology: Next.js 14, TypeScript, Tailwind CSS"
```

### Provide Context

**❌ Bad:**
```
"Add authentication"
```

**✅ Good:**
```
"Add user authentication with:
- Email/password registration
- JWT tokens for session management
- Protected routes requiring login
- Password reset functionality
Use: Supabase Auth for backend"
```

### Make Decisions Quickly

When stuck agent asks:
- ✅ Read options carefully
- ✅ Choose the best approach for your needs
- ✅ Don't overthink - you can always change later
- ✅ Provide clear direction

---

## 📚 Additional Resources

- **Claude Code Docs:** https://docs.claude.com/en/docs/claude-code
- **Subagents Guide:** https://docs.claude.com/en/docs/claude-code/sub-agents
- **Playwright MCP:** https://github.com/microsoft/playwright-mcp
- **Original Repo:** https://github.com/IncomeStreamSurfer/claude-code-agents-wizard-v2

---

## 🤝 Contributing

This system is open and extensible! Feel free to:
- Add new specialized agents
- Improve existing agent prompts
- Share your custom configurations
- Submit PRs with enhancements

---

## 📝 License

MIT License - Use it, modify it, share it!

---

## 🎯 Quick Reference Card

```
┌─────────────────────────────────────────────────┐
│  QUICK REFERENCE                                │
├─────────────────────────────────────────────────┤
│  Start:                                         │
│  $ cd your-project/claude-agent-system          │
│  $ claude                                       │
│                                                 │
│  Tell Claude:                                   │
│  "Build [project] with [features] using [tech]" │
│                                                 │
│  Agents:                                        │
│  • ORCHESTRATOR - Creates todos, delegates      │
│  • CODER - Implements one task at a time        │
│  • TESTER - Visual verification with Playwright │
│  • STUCK - Asks you when problems occur         │
│                                                 │
│  Key Principle:                                 │
│  NO FALLBACKS - You decide, not the AI          │
│                                                 │
│  Check Progress:                                │
│  TodoWrite list always shows current status     │
└─────────────────────────────────────────────────┘
```

---

**Ready to build amazing things with AI-assisted development? Start a Claude Code session in this directory and describe your project! 🚀**
