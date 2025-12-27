# Agentic Workflow System - Quick Summary

**Version:** 2.2 | **Updated:** December 2024

## What It Does

A multi-agent orchestration system for AI-assisted software development. One orchestrator manages the project while specialized subagents handle implementation, testing, and human escalation.

## The Agents

| Agent | Role | Model |
|-------|------|-------|
| **Orchestrator** | Manages todos, delegates tasks, tracks progress | Claude (200K) / Gemini 2.5 Pro (1M+) |
| **Coder** | Implements one task at a time | Claude Sonnet / Gemini 2.5 Pro |
| **Tester** | Visual verification with Playwright | Claude Haiku / Gemini 2.5 Flash |
| **Stuck** | Human escalation (no fallbacks) | Claude Haiku / Gemini 2.5 Flash |

## Core Workflow

```
User Request → Create Todos → Delegate to Coder → Test → Mark Complete → Repeat
```

## Key Rules

1. **One task at a time** - Never delegate multiple tasks simultaneously
2. **Always test** - Every implementation verified by tester with screenshots
3. **No fallbacks** - Problems escalate to humans via stuck agent
4. **Split large tasks** - Keep coder tasks under ~30K tokens
5. **No 404s** - Create pages before adding navigation links

## File Structure

```
.claude/           # Claude Code config
  CLAUDE.md        # Orchestrator instructions
  agents/          # Subagent definitions (coder, tester, stuck)

.gemini/           # Gemini/Antigravity config
  GEMINI.md        # Orchestrator instructions
  agents/          # Subagent definitions

.mcp.json          # Playwright MCP for visual testing
```

## Quick Start

```bash
cd your-project
# Copy this system's .claude/ or .gemini/ folder
claude  # or use Antigravity IDE

# Then describe your project:
"Build a [project] with [features] using [tech stack]"
```

## What Makes It Different

- **Human-in-the-loop**: No silent failures or blind workarounds
- **Visual testing**: Screenshots prove features work
- **Context isolation**: Each subagent gets a fresh, focused context
- **Multi-provider**: Same workflow works with Claude and Gemini

## Proven Results

Successfully built the **Antigravity Directory** (Next.js 14, TypeScript, Tailwind, Shadcn UI) with:
- 40 pages generated
- Zero 404 errors
- Safety scoring system
- Full visual test coverage

---

**The orchestrator remembers everything. The subagents focus on one task. Humans decide when things go wrong.**
