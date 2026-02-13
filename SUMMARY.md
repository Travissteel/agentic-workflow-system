# Agentic Workflow System - Quick Summary

**Version:** 3.0 | **Updated:** January 2026
**Framework:** Nick Saraev's Directive Orchestration Execution (DOE)

---

## What It Does

A multi-agent orchestration system for AI-assisted software development based on the DOE framework. One orchestrator manages the project while specialized subagents handle implementation, testing, and human escalation.

### The DOE Principle

Separates logic into two layers:
- **Directives** (`.md` files): Natural language instructions (probabilistic layer)
- **Executions** (code): Deterministic implementation (deterministic layer)

---

## The 5 Phases

| Phase | Name | Description |
|-------|------|-------------|
| 1 | **Environment Preparation** | IDE setup, folder structure, agent permissions |
| 2 | **Framework Configuration** | System prompts, credentials, modular directives |
| 3 | **Building & Logic** | Analyze, plan, delegate, test, iterate |
| 4 | **Testing & Self-Annealing** | Battle-harden through error learning |
| 5 | **Cloud Deployment** | Cloudify to Modal, webhooks, cron jobs |

---

## The Agents

| Agent | Role | Model |
|-------|------|-------|
| **Orchestrator** | Manages todos, delegates tasks, tracks progress | Claude (200K) / Gemini 2.5 Pro (1M+) |
| **Coder** | Implements one task at a time (Execution layer) | Claude Sonnet / Gemini 2.5 Pro |
| **Tester** | Visual verification with Playwright (Validation layer) | Claude Haiku / Gemini 2.5 Flash |
| **Stuck** | Human escalation - no fallbacks (Human-in-the-Loop) | Claude Haiku / Gemini 2.5 Flash |

---

## Core Workflow

```
User Request → Create Todos → Delegate to Coder → Test → Mark Complete → Repeat
                                     ↓
                              On Error: Self-Anneal or Escalate to Stuck
```

---

## Key Rules

1. **One task at a time** - Never delegate multiple tasks simultaneously
2. **Always test** - Every implementation verified by tester with screenshots
3. **No fallbacks** - Problems escalate to humans via stuck agent
4. **Split large tasks** - Keep coder tasks under ~30K tokens
5. **No 404s** - Create pages before adding navigation links
6. **Definition of Done** - Every task needs clear success criteria

---

## DOE Terminology

| Term | Definition |
|------|------------|
| **Directive** | Natural language SOP in `.md` file |
| **Execution** | Deterministic code (Python/TypeScript) |
| **Self-Annealing** | Agents fix mistakes and update directives with learnings |
| **Cloudifying** | Moving local workflows to cloud (Modal, webhooks) |
| **Metadirective** | Umbrella directive for complex end-to-end functions |
| **Shadow Orchestrator** | Hybrid: cloud execution + local agent fallback |

---

## SOP/Directive Requirements

Every task/directive should have:
- Clear **objective statement**
- **Input specifications**
- Step-by-step **process**
- **Definition of done** (success criteria)

---

## File Structure

```
project/
├── .claude/           # Claude Code config
│   ├── CLAUDE.md      # Orchestrator instructions
│   └── agents/        # Subagent definitions (coder, tester, stuck)
│
├── .gemini/           # Gemini/Antigravity config
│   ├── GEMINI.md      # Orchestrator instructions
│   └── agents/        # Subagent definitions
│
├── directives/        # Natural language SOPs (optional)
├── executions/        # Deterministic scripts (optional)
├── .env               # Credentials (never commit)
└── .mcp.json          # Playwright MCP for visual testing
```

---

## Workflow Handoff Methods

| Method | Client Effort | Resilience |
|--------|---------------|------------|
| **GitHub Codespaces** | Medium | High - One-click pre-configured IDE |
| **Manual Folder Duplication** | Low | Medium - Copy directives/executions |
| **Google Docs/Notion** | Zero | Medium - Non-technical users edit in natural language |
| **Managed Service** | Zero | High - You host cloud; they pay retainer |

---

## Quick Start

```bash
cd your-project
# Copy this system's .claude/ or .gemini/ folder
claude  # or use Antigravity IDE

# Then describe your project:
"Build a [project] with [features] using [tech stack]"
```

---

## What Makes It Different

- **Human-in-the-loop**: No silent failures or blind workarounds
- **Visual testing**: Screenshots prove features work
- **Context isolation**: Each subagent gets a fresh, focused context
- **Multi-provider**: Same workflow works with Claude and Gemini
- **Self-annealing**: System learns from errors and improves directives

---

## Current Project: Agentic Workflows Book

**Status:** In Progress (15/29 chapters completed)
**Project:** "Agentic Workflows for Automating Any Business" - Comprehensive guide to the DOE framework
**Repository:** https://github.com/Travissteel/Agentic-Workflows-for-Automating-Any-Business-book

### Progress Summary

| Category | Status |
|----------|--------|
| **Chapters** | 15 of 29 complete (52%) |
| **Appendices** | 0 of 8 complete |
| **Word Count** | ~60,000 words (estimated) |
| **Target** | ~120,000 words total |

**Completed Chapters:**
- Part 1: Chapters 1-2 ✓
- Part 2: Chapter 3 ✓
- Part 3: Chapter 5 ✓
- Part 4: Chapters 6-7, 9 ✓
- Part 5: Chapters 11-12 ✓
- Part 6: Chapter 14 ✓
- Part 10: Chapters 22-24, 26 ✓
- Part 11: Chapter 28 ✓

**Remaining Work:**
- 14 chapters (Chapters 4, 8, 10, 13, 15-21, 25, 27, 29)
- 8 appendices (A-H)
- Resource files for companion website
- Front matter and introduction
- Final review and polish

---

## Proven Results: Antigravity Directory

Successfully built with this system (Next.js 14, TypeScript, Tailwind, Shadcn UI, Appwrite, Cloudflare):

| Metric | Result |
|--------|--------|
| Total Resources | 88 (35 prompts, 21 rules, 17 workflows, 15 MCPs) |
| Pages Generated | 100+ static pages |
| 404 Errors | Zero |
| Branding | Official Google 2025 "Brighter" Palette |
| Features | Advanced search, Blog, Breadcrumbs, Auth Foundation |
| Deployment | Ready for Cloudflare Pages |

**Repository:** https://github.com/Travissteel/antigravitydirectory

---

## Attribution

This system is based on **Nick Saraev's Directive Orchestration Execution (DOE) Framework**.

---

**The orchestrator remembers everything. The subagents focus on one task. Humans decide when things go wrong. The system learns and improves.**
