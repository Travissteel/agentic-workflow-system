# DOE Framework Terminology Glossary

## Quick Reference

This glossary defines key terms used throughout the Directive Orchestration Execution (DOE) framework.

---

## Core Concepts

**Directive**
Natural language SOP stored in `.md` file - the instruction manual for agents. Describes WHAT needs to happen, not HOW to implement it. Example: "Extract lead information from the contact form and save to CRM."

**Execution**
Deterministic code (Python, TypeScript, JavaScript) that performs specific tasks. The actual implementation that follows the directive. Example: The Python script that scrapes the form and calls the CRM API.

**Orchestrator**
The master agent that maintains state and delegates tasks. Operates within Antigravity IDE (or preferred LLM) with a large context window. Breaks down projects into todos, assigns them to specialist agents, and tracks overall progress.

**Self-Annealing**
Process where agents fix mistakes and update directives with learnings. When an error occurs, the system diagnoses it, fixes the code, and updates the directive with the edge case so it won't happen again.

**Cloudifying**
Moving battle-tested local workflows to cloud platforms (Modal, webhooks, cron jobs) for autonomous operation. Phase 5 of the DOE workflow.

**Definition of Done**
Success criteria that allows agents to self-evaluate completion. Specific, measurable outcomes that determine when a task is truly complete. Example: "CSV file contains 200-500 leads with name, email, and phone for each entry."

**Metadirective**
Umbrella directive that groups multiple workflows for end-to-end functions. Coordinates several sub-directives to accomplish a complex business process.

---

## Agent Types

**Coder Agent**
Implementation specialist that writes code to fulfill specific todo items. Takes directives and produces working executions. Part of the DOE Execution layer.

**Tester Agent**
Visual QA specialist that uses Playwright MCP to verify implementations work correctly by seeing the rendered output. Part of the DOE Validation layer.

**Stuck Agent**
Human escalation point for ANY problem. The only agent authorized to ask humans for input. Ensures no blind fallbacks or silent failures. Part of the DOE Human-in-the-Loop layer.

**Deployer Agent**
Cloud deployment specialist for Modal. Takes battle-tested workflows and deploys them to production with proper authentication and monitoring. Part of the DOE Cloudification layer.

**Support Agent**
Production error diagnosis and auto-fixing for Shadow Orchestrator deployments. Analyzes production errors and applies safe fixes autonomously. Only used in Strategy 2 (Shadow) deployments.

---

## Deployment Strategies

**Standard Hybrid Wrapper (Strategy 1)**
Recommended for 90% of deployments. Workflow is battle-tested locally, then deployed as a static Modal endpoint wrapped in n8n for client accessibility. Self-annealing happens only during local development.

**Shadow Orchestrator (Strategy 2)**
Advanced self-healing deployment for mission-critical workflows. Production errors are automatically classified (Tier 1/2/3), and safe fixes are applied autonomously. System learns and improves continuously in production.

**Hybrid Wrapper Strategy**
Three-layer architecture combining n8n (visual trigger/action layer), Modal (agentic logic layer), and HTTP (connection layer). Makes powerful AI systems accessible to non-technical clients.

---

## Architecture Components

**Outer Shell (n8n)**
Visual no-code layer that clients see and interact with. Handles triggers (webhooks, schedules, email watchers) and final actions (send email, update CRM, post to Slack).

**Inner Core (Modal + Python)**
Where actual agentic logic lives. Handles complex data transformations, LLM reasoning, API integrations, and business logic too complex for visual tools.

**Connection Layer (HTTP)**
Simple HTTP POST requests between n8n and Modal. Bearer token authentication for security. Clean JSON input/output contract.

---

## Error Handling

**Tier 1: Known Friction (Auto-Fix)**
Predictable, routine technical issues like rate limiting, timeouts, missing optional fields. Shadow Orchestrator handles automatically without human involvement.

**Tier 2: Unknown Obstacles (Safe Annealing)**
New patterns not anticipated in the original directive. Shadow analyzes, proposes fix, tests in sandbox, applies if safe, updates directive.

**Tier 3: Critical Logic Failures (Mandatory Escalation)**
Issues involving money, security, irreversible actions, or fundamental business logic changes. Always escalated to human via stuck agent.

**Safety Mechanisms**
Guardrails that prevent runaway autonomous behavior: rate limiting on auto-fixes (max 3/hour), rollback capability, monitor-only mode, audit trails, and scope limits.

---

## Development Phases

**Phase 1: Environment Preparation**
IDE setup (Antigravity IDE or preferred workspace), agent permissions, workspace initialization, folder structure creation.

**Phase 2: Framework Configuration**
System prompts (.antigravity/GEMINI.md + agent definitions), credential management (.env files), modular directives.

**Phase 3: Building & Personalizing Logic**
Analyze project scope, create detailed todo lists, delegate to coder agent, test with tester agent, iterate until complete.

**Phase 4: Testing & Self-Annealing**
Monitor reasoning loops, fix errors and update directives, battle-harden the system through real-world testing.

**Phase 5: Cloudifying**
Deploy to Modal, wrap with n8n (Hybrid Wrapper), configure authentication, set up monitoring, enable production operations.

---

## Tools & Technologies

**MCP (Model Context Protocol)**
Standardized protocol that gives AI agents hands and eyes. Enables file operations, web browsing, database queries, API calls, and more.

**Playwright MCP**
Browser automation tool that enables visual testing. Agents can navigate websites, take screenshots, fill forms, and verify rendered output.

**Modal**
Serverless Python platform for deploying agentic workflows to the cloud. Zero-scaling, pay-per-use, no DevOps required.

**n8n**
Open-source visual workflow automation tool. Used as the "Outer Shell" in Hybrid Wrapper deployments to make agentic logic client-accessible.

---

## Business Models

**Managed Service**
You host and maintain the workflow. Client pays monthly retainer. Best for non-technical clients who want results without responsibility.

**Full Handover**
Client owns and maintains the workflow after delivery. One-time project fee. Best for technical clients who want full control.

**GitHub Codespace**
Pre-configured development environment for technical clients. One-click setup, full access to code and directives.

**Manual Folder**
Deliver directives + executions as a folder. Client sets up their own environment. Best for internal teams or budget-conscious technical clients.

---

## Quality & Verification

**Battle-Testing**
Running a workflow through 10-20 local execution cycles to discover and fix edge cases before deploying to production.

**Visual Confidence**
Using n8n's execution logs and screenshots to build client trust. Clients can see exactly what happened at each step.

**Audit Trail**
Comprehensive logging of every action the Shadow Orchestrator takes: timestamp, error message, decision path, proposed fix, test results, human decisions.

**Rollback Capability**
Automatic backup before every Shadow fix. If new code causes regression, system rolls back to previous version automatically.

---

## Common Acronyms

**DOE** - Directive Orchestration Execution (the framework)
**MCP** - Model Context Protocol (agent capabilities)
**SOP** - Standard Operating Procedure (traditional process docs)
**SLA** - Service Level Agreement (uptime guarantees)
**API** - Application Programming Interface
**CRM** - Customer Relationship Management
**JSON** - JavaScript Object Notation (data format)
**HTTP** - Hypertext Transfer Protocol
**OAuth** - Open Authorization (authentication standard)
**QA** - Quality Assurance

---

## Attribution

The DOE Framework was created by **Nick Saraev** and provides a systematic approach to building reliable, self-improving AI automation systems by separating probabilistic directives from deterministic executions.

---

## Quick Lookup

Need a quick definition? Use Ctrl+F (Cmd+F on Mac) to search this document.

For more detailed explanations, see:
- **Appendices in "The Last Employee" book**
- **GEMINI.md orchestrator template**
- **Individual agent definitions in .antigravity/agents/**
