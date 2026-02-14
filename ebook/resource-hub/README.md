# The Last Employee - Resource Hub

Welcome to the complete resource library for readers of **The Last Employee: Building AI Automation Services Without Employees**.

## What's Inside

This resource hub contains everything you need to build production-ready agentic workflows using the Directive Orchestration Execution (DOE) framework.

### 📁 Directory Structure

```
resource-hub/
├── 1-templates/          → Agent definitions & orchestrator prompts
├── 2-directives/         → Workflow instruction templates
├── 3-code/              → Python templates & configuration files
├── 4-client-handoff/    → Proposals, intake forms, and delivery docs
├── 5-reference/         → Quick reference guides & checklists
└── README.md            → You are here
```

## Quick Start

### If you're brand new to the DOE framework:
1. Start with `1-templates/GEMINI-md-orchestrator.md` to understand the system
 
## Quick Start
 
1. Create a `.antigravity/` folder in your project root.
2. Copy the content of `GEMINI-md-orchestrator.md` into `.antigravity/GEMINI.md`.
3. Your preferred LLM (Gemini, Claude, GPT-4) now has its operating instructions.
2. Review `2-directives/blank-directive-template.md` to learn directive structure
3. Copy `3-code/modal-app-template.py` for your first deployment
4. Use `5-reference/skills-quick-reference.md` as your cheat sheet

### If you're ready to build your first workflow:
1. Copy `2-directives/blank-directive-template.md` and fill it in
2. Use `1-templates/coder-agent.md` to set up your implementation agent
3. Reference `2-directives/hybrid-wrapper-deployment.md` for cloud deployment
4. Follow `5-reference/modal-deployment-checklist.md` before going live

### If you're delivering to clients:
1. Start with `4-client-handoff/client-intake-form.md` to qualify leads
2. Use `4-client-handoff/handoff-decision-guide.md` to choose delivery model
3. Customize `4-client-handoff/managed-service-proposal.md` or `full-handover-proposal.md`
4. Reference `4-client-handoff/n8n-workflow-template.json` for Hybrid Wrapper setup

## What Each Folder Contains

### 1-templates/
Copy-paste ready agent definitions for your `.antigravity/agents/` folder:
- **GEMINI-md-orchestrator.md** - Master orchestrator prompt (the brain)
- **coder-agent.md** - Implementation specialist
- **tester-agent.md** - Visual QA with Playwright
- **stuck-agent.md** - Human-in-the-loop escalation
- **deployer-agent.md** - Cloud deployment specialist
- **support-agent.md** - Production error diagnosis (Shadow Orchestrator only)

### 2-directives/
Templates for creating workflow instructions:
- **blank-directive-template.md** - Start here for any new workflow
- **lead-gen-directive-example.md** - Complete lead generation workflow
- **content-pipeline-directive-example.md** - Content creation automation
- **invoice-processing-directive-example.md** - Accounts payable automation
- **hybrid-wrapper-deployment.md** - Step-by-step cloud deployment guide
- **shadow-orchestrator.md** - Advanced self-healing production pattern
- **modal-endpoint-guide.md** - Building Modal API endpoints

### 3-code/
Production-ready code templates:
- **modal-app-template.py** - Basic Modal endpoint with authentication
- **shadow-orchestrator-template.py** - Advanced self-annealing deployment
- **env-example.env** - All required environment variables
- **mcp-config.json** - Playwright MCP configuration
- **package.json** - Node dependencies for MCP tools

### 4-client-handoff/
Sales and delivery templates:
- **client-intake-form.md** - Pre-discovery questionnaire
- **managed-service-proposal.md** - Monthly retainer template
- **full-handover-proposal.md** - One-time delivery template
- **handoff-decision-guide.md** - Choose the right delivery model
- **n8n-workflow-template.json** - Hybrid Wrapper visual workflow

### 5-reference/
Quick reference guides and checklists:
- **skills-quick-reference.md** - DOE framework cheat sheet
- **mcp-configuration-reference.md** - Setting up Model Context Protocol tools
- **modal-deployment-checklist.md** - Pre-deployment safety checklist
- **doe-terminology-glossary.md** - Framework vocabulary
- **troubleshooting-decision-tree.md** - Debug common issues

## How to Use These Resources

### Method 1: Copy Individual Files
Browse the folders above and copy the specific templates you need for your current project.

### Method 2: Clone the Entire Hub
If you want the complete set, download this entire `resource-hub/` folder to your project.

### Method 3: Customize and Expand
These templates are starting points. Adapt them to your specific business needs, industry, and client requirements.

## Important Notes

### Credentials and Security
- Never hardcode API keys or credentials
- Use `.env` files for local development (add to `.gitignore`)
- Use Modal Secrets for production deployments
- Rotate credentials regularly

### Version Control
- Commit directives and agent definitions to Git
- Track changes to directives as they self-anneal
- Don't commit `.env` files, credentials, or client data
- Use branches for testing major directive changes

### Getting Help
- **Book Website**: travissteel.net/the-last-employee
- **Resource Updates**: travissteel.net/the-last-employee/resources
- **Community**: travissteel.net/the-last-employee/community
- **Author**: Contact information in the book

## License

These templates are provided for use by readers of "The Last Employee" book. You may:
- Use them in your commercial projects
- Modify them for your needs
- Share them with team members and clients

Attribution to the DOE framework and Nick Saraev's work is appreciated but not required.

## Updates and Community Contributions

These templates improve over time based on real-world usage. Check the book website periodically for updates:
- New directive examples
- Additional code templates
- Community-contributed improvements
- Framework updates and enhancements

## What's Next?

1. **Read the book** if you haven't already - these resources make more sense in context
2. **Pick one workflow** to automate first (start small)
3. **Copy the templates** that match your use case
4. **Build, test, deploy** following the 5-phase DOE workflow
5. **Let the system self-anneal** and improve over time

Remember: Version 1 doesn't need to be perfect. The self-annealing process will refine it through real-world execution. Your job right now is to get it good enough to test.

Happy building!

---

**Attribution**: This resource hub operationalizes the Directive Orchestration Execution (DOE) Framework created by Nick Saraev. The framework provides a systematic approach to building reliable, self-improving AI automation systems.
