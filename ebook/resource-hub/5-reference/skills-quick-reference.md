# Skills Quick Reference

One-page reference for essential DOE framework skills.

---

## Phase 1: Environment Setup

| Skill | Tool | Command |
|-------|------|---------|
| Install Modal | pip | `pip install modal` |
| Authenticate Modal | modal | `modal token set` |
| Install MCP servers | npm | `npm install -g @modelcontextprotocol/server-*` |
| Create virtual env | Python | `python -m venv venv` |
| Activate venv | Shell | `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows) |

---

## Phase 2: Directive Writing

| Component | Purpose | Template Location |
|-----------|---------|-------------------|
| Objective | What and why | `blank-directive-template.md` |
| Inputs | Required data and access | `blank-directive-template.md` |
| Process | Step-by-step workflow | `blank-directive-template.md` |
| Definition of Done | Success criteria | `blank-directive-template.md` |

**Key Principle**: Describe WHAT, not HOW. Let agents determine implementation.

---

## Phase 3: Building Workflows

| Task | Agent | Tool |
|------|-------|------|
| Implement code | coder | Read, Write, Edit, Bash |
| Test visually | tester | Playwright MCP |
| Get human input | stuck | AskUserQuestion |
| Track progress | orchestrator | TodoWrite |

**Workflow**: Orchestrator → Coder → Tester → (Pass or invoke Stuck) → Repeat

---

## Phase 4: Testing

| Test Type | Tool | Purpose |
|-----------|------|---------|
| Local validation | Python/Node | Prove logic works |
| Visual verification | Playwright | See rendered output |
| Edge case testing | Manual scenarios | Handle unexpected inputs |
| Definition of Done check | Directive comparison | Confirm success criteria met |

---

## Phase 5: Deployment (Hybrid Wrapper)

| Step | Tool | Output |
|------|------|--------|
| Build Modal endpoint | Python + Modal | API function |
| Generate Bearer token | `openssl rand -hex 32` | 64-char token |
| Create Modal secret | `modal secret create` | Stored credential |
| Deploy to Modal | `modal deploy` | Endpoint URL |
| Build n8n wrapper | n8n | Visual workflow |
| Test end-to-end | cURL + n8n | Working automation |

---

## Essential Modal Commands

```bash
# Setup
modal token set

# Secrets
modal secret create api-auth-token API_AUTH_TOKEN=token
modal secret list

# Development
modal run app.py::function_name
modal deploy app.py

# Monitoring
modal app list
modal app logs app-name --follow
```

---

## Essential n8n Configuration

**HTTP Request Node (to Modal)**:
- Method: POST
- URL: Modal endpoint URL
- Auth: Header Auth
  - Name: `Authorization`
  - Value: `Bearer your_token`
- Body: JSON payload

**IF Node (error handling)**:
- Condition: `{{ $json.success }} === true`
- True: Continue to final action
- False: Send error notification

---

## File Structure

```
project/
├── .claude/
│   ├── CLAUDE.md          # Orchestrator instructions
│   └── agents/            # Subagent definitions
├── directives/            # Natural language SOPs
├── executions/            # Python/JavaScript code
├── .env                   # Secrets (never commit)
├── .mcp.json              # MCP configuration
└── package.json           # Node dependencies
```

---

## Agent Roles Summary

| Agent | Role | When to Use |
|-------|------|-------------|
| **orchestrator** | Master planner | Always (you are this) |
| **coder** | Build code | Every todo item |
| **tester** | Verify visually | After every coder task |
| **deployer** | Deploy to cloud | Phase 5 cloudifying |
| **support** | Fix production errors | Shadow Orchestrator only |
| **stuck** | Get human input | ANY problem |

---

## Common Error Solutions

| Error | Cause | Fix |
|-------|-------|-----|
| `ModuleNotFoundError` | Missing dependency | Add to `requirements.txt` |
| `401 Unauthorized` | Missing/wrong token | Check Bearer token in header |
| `Timeout` | Function takes too long | Increase `timeout=X` parameter |
| `Secret not found` | Modal secret missing | `modal secret create` |
| Visual misalignment | CSS/layout issue | Invoke tester agent |

---

## Decision Trees

### Which Handoff Model?
1. Technical? → Yes: Codespace/Folder, No: Wrapper/Managed
2. Want support? → Yes: Managed, No: One-time
3. Budget? → Low: Folder, Med: Wrapper, High: Managed

### Which Agent?
- Code broken? → coder
- Visuals wrong? → tester
- Deploy failing? → deployer
- Production error (Shadow)? → support
- Anything else? → stuck

---

## Quality Checklist

**Before deploying**:
- [ ] Directive has Definition of Done
- [ ] Code tested locally
- [ ] Tester verified visually
- [ ] Authentication implemented
- [ ] Secrets not hardcoded
- [ ] Error handling in place
- [ ] Documentation complete

---

## Quick Links

- Blank directive: `2-directives/blank-directive-template.md`
- Modal template: `3-code/modal-app-template.py`
- n8n template: `4-client-handoff/n8n-workflow-template.json`
- Deployment checklist: `5-reference/modal-deployment-checklist.md`

---

**Remember**: The DOE framework separates Directives (what to do) from Executions (how to do it). Agents translate natural language into deterministic code.
