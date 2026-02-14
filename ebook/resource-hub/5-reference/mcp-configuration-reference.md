# MCP Configuration Quick Reference

Model Context Protocol (MCP) tools provide agents with capabilities for browser automation, web search, file operations, and more.

---

## Essential MCP Servers for DOE Framework

### Playwright (Visual Testing)
**Purpose**: Browser automation for tester agent
**Installation**: `npx -y @modelcontextprotocol/server-playwright`
**Use Cases**: Visual verification, web scraping, screenshot capture

### Brave Search (Research)
**Purpose**: Web search for data gathering
**Installation**: `npx -y @modelcontextprotocol/server-brave-search`
**Requires**: `BRAVE_API_KEY` environment variable
**Use Cases**: Research, competitive intelligence, lead enrichment

### Filesystem (File Operations)
**Purpose**: Read/write project files
**Installation**: `npx -y @modelcontextprotocol/server-filesystem <path>`
**Use Cases**: Reading directives, writing executions, managing project files

### GitHub (Version Control)
**Purpose**: Repository operations
**Installation**: `npx -y @modelcontextprotocol/server-github`
**Requires**: `GITHUB_PERSONAL_ACCESS_TOKEN` environment variable
**Use Cases**: Directive updates, code commits, self-annealing

### Memory (Context Persistence)
**Purpose**: Maintain context across sessions
**Installation**: `npx -y @modelcontextprotocol/server-memory`
**Use Cases**: Self-annealing tracking, learning accumulation

---

## Optional MCP Servers

### Google Drive
**Installation**: `npx -y @modelcontextprotocol/server-gdrive`
**Requires**: `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`
**Use Cases**: Client document access, shared files

### Slack
**Installation**: `npx -y @modelcontextprotocol/server-slack`
**Requires**: `SLACK_BOT_TOKEN`, `SLACK_TEAM_ID`
**Use Cases**: Notifications, team communication

### PostgreSQL
**Installation**: `npx -y @modelcontextprotocol/server-postgres <connection-string>`
**Use Cases**: Database-backed workflows, data storage

---

## Configuration File Structure

Create `.mcp.json` in your project root:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-playwright"]
    },
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "${BRAVE_API_KEY}"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/project"]
    }
  }
}
```

---

## Environment Variables

Store in `.env` file (never commit to GitHub):

```bash
# Required
BRAVE_API_KEY=your_brave_api_key_here
GITHUB_PERSONAL_ACCESS_TOKEN=ghp_your_token_here

# Optional
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
SLACK_BOT_TOKEN=xoxb-your-slack-token
SLACK_TEAM_ID=T0123456789
```

---

## Quick Setup

1. Install MCP servers globally:
```bash
npm install -g @modelcontextprotocol/server-playwright \
  @modelcontextprotocol/server-brave-search \
  @modelcontextprotocol/server-filesystem \
  @modelcontextprotocol/server-github \
  @modelcontextprotocol/server-memory
```

2. Create `.mcp.json` configuration file (see `mcp-config.json` template)

3. Create `.env` file with required API keys

4. Test Playwright installation:
```bash
npx @modelcontextprotocol/server-playwright --help
```

5. List installed servers:
```bash
npm list -g --depth=0 | grep @modelcontextprotocol
```

---

## Agent-Specific MCP Usage

**Orchestrator**: Filesystem, Memory, GitHub
**Coder**: Filesystem, GitHub
**Tester**: Playwright, Filesystem
**Deployer**: Filesystem, GitHub
**Stuck**: Filesystem (read-only for context)

---

## Troubleshooting

**Problem**: MCP server not found
**Solution**: Install globally with `npm install -g @modelcontextprotocol/server-*`

**Problem**: Environment variable not loading
**Solution**: Ensure `.env` file is in project root and variables are exported

**Problem**: Playwright fails to launch browser
**Solution**: Install system dependencies (Chromium, etc.) with `npx playwright install`

---

**Related Resources:**
- `mcp-config.json` - Complete configuration template
- `package.json` - NPM dependencies for MCP tools
- `.env-example.env` - Environment variable template
