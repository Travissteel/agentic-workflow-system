# Appendix E: MCP Configuration Reference

## Introduction

Model Context Protocol (MCP) servers are the bridge between your AI agents and the real world. While a language model on its own can only process text and generate responses, MCPs give your agents the ability to actually *do* things—read files, search the web, take screenshots, update spreadsheets, send notifications, and more.

Think of MCPs as giving your AI agents "hands and eyes." Without them, your agents can think and plan, but they can't interact with external systems. With them, they become powerful automation engines capable of executing complex business workflows autonomously.

Throughout this book, we've referenced various MCPs—the Playwright MCP for visual testing in the tester agent (Chapter 14), the Filesystem MCP for reading and writing directives, and the Brave Search MCP for web research. This appendix provides a comprehensive reference for configuring and using the most valuable MCPs for business automation.

The beauty of MCPs is their standardized architecture. Once you understand how to configure one, you can configure any of them. They all follow the same pattern: install the server, add configuration to your `.mcp.json` file, provide any necessary credentials, and start using them in your agent workflows.

In this appendix, you'll find step-by-step setup instructions for five essential MCPs, configuration templates you can copy directly into your projects, security best practices to protect your credentials, and troubleshooting guidance for common issues. Whether you're setting up your first MCP or building a complex multi-MCP workflow, this reference will guide you through the process.

┌─────────────────────────────────────────────────────┐
│  DOWNLOAD READY-TO-USE CONFIGURATIONS              │
│                                                      │
│  Get pre-configured .mcp.json files for all the     │
│  MCPs covered in this appendix:                     │
│                                                      │
│  travissteel.net/the-last-employee/resources#reference          │
│                                                      │
│  Includes: Playwright, Filesystem, Brave Search,    │
│  Google Drive, Slack, and more.                     │
└─────────────────────────────────────────────────────┘

## Core MCP Concepts

### How MCPs Work

MCPs operate on a server-client architecture. The MCP server is a standalone process that provides specific capabilities—web scraping, file operations, database queries, API integrations, etc. Your AI agent (running in Antigravity IDE, for example) acts as the client, sending requests to the MCP server and receiving responses.

When you invoke a tool in Antigravity IDE (like "take a screenshot of this webpage"), Antigravity IDE sends a standardized request to the appropriate MCP server. The server executes the action, and sends back the result. This happens seamlessly in the background, making it appear as if the agent has native capabilities.

The standardization is the key. All MCP servers expose their capabilities through a consistent protocol, which means:
- **Uniform Configuration**: Every MCP is configured the same way in `.mcp.json`
- **Consistent Error Handling**: Errors are reported in a standard format
- **Easy Discovery**: Agents can query what tools an MCP provides
- **Simplified Integration**: Adding a new capability is just adding a new server

### Configuration in .mcp.json

All MCP servers are configured in a single file: `.mcp.json` in your project root. This file tells Antigravity IDE (or other MCP clients) which servers to start, how to start them, and what credentials they need.

The basic structure looks like this:

```json
{
  "mcpServers": {
    "server-name": {
      "command": "command-to-start-server",
      "args": ["--arg1", "--arg2"],
      "env": {
        "API_KEY": "your-api-key-here"
      }
    }
  }
}
```

Each server gets a unique name (like "playwright" or "filesystem"), a command to launch it, optional arguments, and optional environment variables for credentials.

**Pro Tip**: Never hardcode sensitive credentials directly in `.mcp.json`. Instead, reference environment variables from a `.env` file that's excluded from version control (covered in the Security section below).

### Authentication and Security Considerations

MCPs often require credentials to access external services—API keys for Brave Search, OAuth tokens for Google Drive, webhook URLs for Slack. These credentials must be protected carefully, especially if your `.mcp.json` file is committed to a Git repository.

**Best Practice: The .env Pattern**

1. Create a `.env` file in your project root
2. Add it to `.gitignore` (never commit it)
3. Store all credentials in the `.env` file:
   ```
   BRAVE_API_KEY=your_brave_api_key_here
   GOOGLE_CLIENT_ID=your_google_client_id
   GOOGLE_CLIENT_SECRET=your_google_client_secret
   SLACK_WEBHOOK_URL=https://hooks.slack.com/services/YOUR/WEBHOOK/URL
   ```
4. Reference these environment variables in `.mcp.json`:
   ```json
   {
     "env": {
       "BRAVE_API_KEY": "${BRAVE_API_KEY}"
     }
   }
   ```

This pattern ensures that:
- Credentials are never committed to version control
- `.mcp.json` can be safely shared and versioned
- Team members can use their own credentials
- Production deployments can inject environment variables securely

**Additional Security Considerations:**

- **Principle of Least Privilege**: Only grant MCPs the minimum permissions they need. For example, the Filesystem MCP should only have access to specific directories, not your entire system.
- **Credential Rotation**: Regularly rotate API keys and OAuth tokens, especially for production deployments.
- **Audit Logs**: For sensitive operations (database writes, financial transactions), ensure your MCP server logs all actions for audit purposes.
- **Network Security**: Some MCPs expose HTTP endpoints. Use authentication tokens and restrict access to trusted networks.

### Testing MCP Connections

Before relying on an MCP in production workflows, test that it's configured correctly. Here's a systematic approach:

**1. Verify Installation**

After installing an MCP server, check that the command exists:

```bash
# For Node-based MCPs
npx @modelcontextprotocol/server-playwright --version

# For Python-based MCPs
python -m mcp_server_filesystem --version
```

**2. Check .mcp.json Configuration**

Ensure your `.mcp.json` file is valid JSON. Use a JSON validator or try loading it in Antigravity IDE. Common mistakes:
- Missing commas between properties
- Trailing commas (not allowed in strict JSON)
- Incorrect path to server command
- Typos in environment variable names

**3. Test Basic Operations**

Once configured, test the MCP with a simple operation:

- **Playwright**: "Navigate to google.com and take a screenshot"
- **Filesystem**: "List all files in the current directory"
- **Brave Search**: "Search for 'MCP protocol documentation'"
- **Google Drive**: "List all files in my Google Drive"
- **Slack**: "Send a test message to the #test channel"

**4. Verify Authentication**

If the MCP requires credentials, test that they're correctly loaded:
- Check that environment variables are set (`echo $BRAVE_API_KEY`)
- Verify API keys are active (not expired or revoked)
- Test OAuth flows complete successfully

**5. Monitor Error Messages**

If an MCP fails, read the error messages carefully. They usually indicate exactly what's wrong:
- "Command not found" → MCP server not installed
- "API key invalid" → Credential issue
- "Permission denied" → Filesystem permissions
- "Connection refused" → Server not running

## Essential MCPs for Business Automation

### Playwright MCP (for Visual Testing)

The Playwright MCP is arguably the most powerful MCP for business automation. It gives your agents full browser control—navigating websites, filling forms, clicking buttons, taking screenshots, and scraping data. In the DOE framework, this is what powers the tester agent (Chapter 14).

**What It's Used For:**
- Visual testing of web applications
- Automated data entry into web forms
- Scraping data from websites
- Generating screenshots for reports
- Testing responsive design across devices
- Monitoring website changes

**Installation Steps:**

```bash
# Install the Playwright MCP server
npm install -g @modelcontextprotocol/server-playwright

# Install browser binaries
npx playwright install chromium
```

**Configuration in .mcp.json:**

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@modelcontextprotocol/server-playwright"
      ]
    }
  }
}
```

**Common Usage Patterns:**

**Pattern 1: Visual Testing**
```
Agent: "Navigate to https://myapp.com/login and take a screenshot"
Agent: "Enter 'test@example.com' into the email field"
Agent: "Click the 'Sign In' button"
Agent: "Verify that the dashboard loaded successfully"
```

**Pattern 2: Data Scraping**
```
Agent: "Navigate to https://competitors-website.com/pricing"
Agent: "Extract all pricing tiers and their features"
Agent: "Save the data to pricing-comparison.json"
```

**Pattern 3: Form Automation**
```
Agent: "Navigate to the CRM lead entry form"
Agent: "Fill in the form with data from new-leads.csv"
Agent: "Submit the form and capture the confirmation number"
```

**Troubleshooting Tips:**

**Issue: "Browser binary not found"**
- **Solution**: Run `npx playwright install chromium` to download browser binaries
- **Why**: Playwright requires actual browser executables, not just the Node package

**Issue: "Navigation timeout"**
- **Solution**: Increase timeout or check network connectivity
- **Why**: Slow websites or network issues can exceed default timeout (30s)

**Issue: "Element not found"**
- **Solution**: Add wait conditions or use more specific selectors
- **Why**: Pages may load dynamically; wait for elements to appear

**Issue: "Screenshot is blank"**
- **Solution**: Add a delay after navigation before capturing
- **Why**: Page may not be fully rendered when screenshot is taken

**Security Considerations:**

The Playwright MCP has full browser access, which means it can access any website you can. This is powerful but requires caution:
- Don't run untrusted scripts with Playwright access
- Be careful when automating actions on production websites
- Consider rate limiting to avoid overwhelming target sites
- Use headless mode (`headless: true`) for production to reduce resource usage

### Filesystem MCP (for File Operations)

The Filesystem MCP enables your agents to read, write, create, and delete files on your local system or server. It's essential for managing directives, execution scripts, and data files in the DOE framework.

**What It's Used For:**
- Reading directive files (`.md`)
- Writing execution scripts (`.py`, `.js`)
- Managing data files (`.csv`, `.json`)
- Creating and organizing project folders
- Self-annealing (updating directives after errors)

**Installation Steps:**

```bash
# Install the Filesystem MCP server
npm install -g @modelcontextprotocol/server-filesystem
```

**Configuration in .mcp.json:**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "@modelcontextprotocol/server-filesystem",
        "/path/to/allowed/directory"
      ]
    }
  }
}
```

**Security Considerations:**

The Filesystem MCP is incredibly powerful and potentially dangerous. By default, it can access any file on your system. **Always restrict it to specific directories:**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "@modelcontextprotocol/server-filesystem",
        "/Users/yourname/projects/your-project",
        "--allowed-paths",
        "/Users/yourname/projects/your-project/directives",
        "/Users/yourname/projects/your-project/executions"
      ]
    }
  }
}
```

This configuration:
- Restricts access to your project directory
- Only allows reading/writing in `directives/` and `executions/`
- Prevents accidental deletion of system files
- Blocks access to sensitive directories like `/etc`, `~/.ssh`, etc.

**Common Usage Patterns:**

**Pattern 1: Reading Directives**
```
Agent: "Read the file at directives/scrape-leads.md"
Agent: "Parse the 'Definition of Done' section"
```

**Pattern 2: Creating Execution Scripts**
```
Agent: "Create a new file at executions/lead-scraper.py"
Agent: "Write the following Python code to the file..."
```

**Pattern 3: Self-Annealing (Updating Directives)**
```
Agent: "Read directives/email-automation.md"
Agent: "Add a new edge case to the error handling section"
Agent: "Write the updated content back to the file"
```

**Pattern 4: Data Management**
```
Agent: "Read the CSV file at data/leads.csv"
Agent: "Filter for leads with 'status: new'"
Agent: "Write filtered results to data/leads-new.csv"
```

**Troubleshooting Tips:**

**Issue: "Permission denied"**
- **Solution**: Check file permissions with `ls -la` (Unix) or use file properties (Windows)
- **Why**: The MCP server runs under your user account; ensure it has read/write access

**Issue: "Path not allowed"**
- **Solution**: Add the path to `--allowed-paths` in `.mcp.json`
- **Why**: Security restriction preventing access outside configured directories

**Issue: "File not found"**
- **Solution**: Use absolute paths, not relative paths
- **Why**: The MCP server's working directory may differ from expectations

**Issue: "Cannot write to file"**
- **Solution**: Ensure the parent directory exists first
- **Why**: Some filesystem operations don't auto-create parent directories

**Best Practices:**

1. **Use Absolute Paths**: Always use full paths like `/Users/name/project/file.md` rather than relative paths like `../file.md`
2. **Version Control**: Keep directive and execution files in Git so you can track changes from self-annealing
3. **Backup Before Overwriting**: When updating files, read the current content first and keep a backup
4. **Validate File Content**: After writing, read the file back to verify it was written correctly
5. **Organize by Type**: Keep directives, executions, and data in separate folders for clarity

### Brave Search MCP (for Web Research)

The Brave Search MCP gives your agents the ability to search the web and retrieve up-to-date information. Unlike a language model's training data (which has a cutoff date), Brave Search provides real-time access to current information.

**What It's Used For:**
- Market research and competitive analysis
- Finding current contact information
- Validating business details (addresses, phone numbers)
- Discovering industry trends
- Lead generation and enrichment

**Installation Steps:**

1. **Get a Brave Search API Key**:
   - Go to https://brave.com/search/api/
   - Sign up for a free account (1,000 searches/month)
   - Copy your API key

2. **Install the Brave Search MCP Server**:
   ```bash
   npm install -g @modelcontextprotocol/server-brave-search
   ```

3. **Add API Key to .env**:
   ```
   BRAVE_API_KEY=your_brave_api_key_here
   ```

**Configuration in .mcp.json:**

```json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": [
        "@modelcontextprotocol/server-brave-search"
      ],
      "env": {
        "BRAVE_API_KEY": "${BRAVE_API_KEY}"
      }
    }
  }
}
```

**Common Usage Patterns:**

**Pattern 1: Lead Research**
```
Agent: "Search for 'Melbourne accounting firms with 10-50 employees'"
Agent: "Extract business names and websites from results"
Agent: "For each result, search for 'company_name contact email'"
```

**Pattern 2: Market Research**
```
Agent: "Search for 'SaaS pricing trends 2026'"
Agent: "Summarize the top 5 results"
Agent: "Search for 'freemium model conversion rates'"
```

**Pattern 3: Contact Information Validation**
```
Agent: "Search for 'Acme Corp Melbourne official website'"
Agent: "Navigate to the website and find contact information"
Agent: "Verify the phone number matches our database"
```

**Pattern 4: Competitive Intelligence**
```
Agent: "Search for 'competitor_name new features 2026'"
Agent: "Search for 'competitor_name pricing changes'"
Agent: "Compile a summary of recent competitive moves"
```

**Troubleshooting Tips:**

**Issue: "API key invalid"**
- **Solution**: Verify the API key is correct in `.env` and has been loaded
- **Why**: Typos, expired keys, or environment variable not loaded

**Issue: "Rate limit exceeded"**
- **Solution**: Reduce search frequency or upgrade to paid plan
- **Why**: Free tier is limited to 1,000 searches/month

**Issue: "No results found"**
- **Solution**: Refine search query or try synonyms
- **Why**: Query may be too specific or use unusual terminology

**Issue: "Results not relevant"**
- **Solution**: Add more specific keywords or use advanced search operators
- **Why**: Broad queries return broad results

**Best Practices:**

1. **Specific Queries**: Use detailed search terms ("Melbourne SaaS startups" vs. "startups")
2. **Combine with Web Scraping**: Search finds the page, Playwright extracts the data
3. **Rate Limiting**: Track search usage to avoid exceeding free tier limits
4. **Result Validation**: Cross-reference search results; don't trust a single source
5. **Cache Results**: Save search results to avoid repeating identical queries

**Free vs. Paid Plans:**

| Feature | Free | Paid |
|---------|------|------|
| Searches/month | 1,000 | 100,000+ |
| Rate limiting | Strict | Higher limits |
| Support | Community | Priority |
| Cost | $0 | From $5/month |

For most business automation workflows, the free tier is sufficient. Upgrade when you're consistently hitting the 1,000 search limit.

### Google Drive MCP (for Document Access)

The Google Drive MCP enables your agents to read and write files in Google Drive, making it invaluable for businesses that store documents, spreadsheets, and data in Google Workspace.

**What It's Used For:**
- Reading data from Google Sheets (customer lists, inventory, etc.)
- Writing results to Google Sheets (reports, dashboards)
- Accessing Google Docs for directive storage
- Managing shared team files
- Automating document workflows

**Installation Steps:**

1. **Set Up Google Cloud Project**:
   - Go to https://console.cloud.google.com/
   - Create a new project (or use existing)
   - Enable the Google Drive API
   - Create OAuth 2.0 credentials (Desktop app type)
   - Download the credentials JSON file

2. **Install the Google Drive MCP Server**:
   ```bash
   npm install -g @modelcontextprotocol/server-google-drive
   ```

3. **Add Credentials to .env**:
   ```
   GOOGLE_CLIENT_ID=your_client_id.apps.googleusercontent.com
   GOOGLE_CLIENT_SECRET=your_client_secret
   ```

**Configuration in .mcp.json:**

```json
{
  "mcpServers": {
    "google-drive": {
      "command": "npx",
      "args": [
        "@modelcontextprotocol/server-google-drive"
      ],
      "env": {
        "GOOGLE_CLIENT_ID": "${GOOGLE_CLIENT_ID}",
        "GOOGLE_CLIENT_SECRET": "${GOOGLE_CLIENT_SECRET}"
      }
    }
  }
}
```

**OAuth Flow:**

The first time you use the Google Drive MCP, it will:
1. Open a browser window for Google authentication
2. Ask you to grant permissions to the app
3. Store an access token locally for future use
4. Automatically refresh the token when it expires

**Common Usage Patterns:**

**Pattern 1: Reading Google Sheets Data**
```
Agent: "List all files in my Google Drive"
Agent: "Open the spreadsheet named 'Customer Database'"
Agent: "Read all rows from the 'Leads' sheet"
Agent: "Filter for leads with status 'New'"
```

**Pattern 2: Writing Results to Sheets**
```
Agent: "Open the spreadsheet 'Weekly Report'"
Agent: "Create a new sheet named '2026-02-14'"
Agent: "Write the following data as a table: [data]"
Agent: "Apply formatting: bold headers, freeze top row"
```

**Pattern 3: Document Management**
```
Agent: "Search for documents containing 'sales proposal'"
Agent: "Download the most recent one to local directory"
Agent: "Update the pricing section based on new-pricing.json"
Agent: "Upload the updated document back to Google Drive"
```

**Pattern 4: Shared Team Workflows**
```
Agent: "List all files in the 'Marketing' shared folder"
Agent: "For each PDF, extract text and summarize"
Agent: "Write summaries to 'Marketing Content Summary.docx'"
```

**Troubleshooting Tips:**

**Issue: "OAuth consent screen not configured"**
- **Solution**: In Google Cloud Console, configure the OAuth consent screen
- **Why**: Google requires consent screen setup before OAuth flows work

**Issue: "Access token expired"**
- **Solution**: The MCP should auto-refresh; if not, delete cached token and re-authenticate
- **Why**: Tokens expire after 1 hour; refresh tokens extend access

**Issue: "Insufficient permissions"**
- **Solution**: Check OAuth scopes include Drive access
- **Why**: Overly restrictive scopes prevent file operations

**Issue: "File not found"**
- **Solution**: Verify file name exactly (case-sensitive) or use file ID
- **Why**: Google Drive allows duplicate file names; IDs are unique

**Best Practices:**

1. **Use File IDs**: For production workflows, use file IDs (immutable) rather than names (can change)
2. **Shared Folders**: Store team documents in shared folders for easier access
3. **Version History**: Google Drive tracks versions; use this for safety
4. **Permissions**: Be mindful of what your agent can access; limit to necessary folders
5. **Batch Operations**: When reading/writing multiple files, batch requests to reduce API calls

**Security Considerations:**

The Google Drive MCP has access to *all* files your Google account can access. This includes:
- Personal documents
- Shared team files
- Client data
- Financial records

**Mitigations:**
- Create a dedicated Google account for automation (don't use your personal account)
- Use granular OAuth scopes (e.g., read-only access if writes aren't needed)
- Regularly audit which files the MCP has accessed
- Revoke access immediately if credentials are compromised

### Slack MCP (for Notifications)

The Slack MCP enables your agents to send messages to Slack channels, providing real-time notifications for workflow events, errors, and completion statuses.

**What It's Used For:**
- Notifying teams when workflows complete
- Alerting on errors or stuck agent escalations
- Sending daily/weekly reports
- Posting lead notifications to sales channels
- Logging important events for audit trails

**Installation Steps:**

1. **Create a Slack Incoming Webhook**:
   - Go to https://api.slack.com/apps
   - Create a new app or select existing
   - Enable "Incoming Webhooks"
   - Add a webhook to a specific channel
   - Copy the webhook URL

2. **Install the Slack MCP Server**:
   ```bash
   npm install -g @modelcontextprotocol/server-slack
   ```

3. **Add Webhook URL to .env**:
   ```
   SLACK_WEBHOOK_URL=https://hooks.slack.com/services/YOUR/WEBHOOK/URL
   ```

**Configuration in .mcp.json:**

```json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": [
        "@modelcontextprotocol/server-slack"
      ],
      "env": {
        "SLACK_WEBHOOK_URL": "${SLACK_WEBHOOK_URL}"
      }
    }
  }
}
```

**Common Usage Patterns:**

**Pattern 1: Workflow Completion Notifications**
```
Agent: "All leads have been processed successfully"
Agent: "Send to Slack: '✅ Lead Processing Complete: 47 new leads added to CRM'"
```

**Pattern 2: Error Alerts**
```
Agent: "An error occurred during data scraping"
Agent: "Send to Slack: '🚨 ERROR: Lead scraper failed at step 3. Check logs.'"
```

**Pattern 3: Daily Reports**
```
Agent: "Generate summary of today's activity"
Agent: "Send to Slack: 'Daily Report for 2026-02-14: 23 leads, 15 emails sent, 8 follow-ups scheduled'"
```

**Pattern 4: Human Escalation Notifications**
```
Agent: "Stuck agent invoked - need human decision"
Agent: "Send to Slack: '@channel Workflow paused: Need approval for pricing tier change'"
```

**Advanced Formatting:**

Slack supports rich message formatting with Markdown-like syntax:

```json
{
  "text": "*Workflow Complete*\n\n• Leads processed: 47\n• Success rate: 94%\n• Errors: 3\n\n<https://dashboard.example.com|View Dashboard>"
}
```

**Troubleshooting Tips:**

**Issue: "Webhook URL invalid"**
- **Solution**: Verify the URL is complete and hasn't been regenerated
- **Why**: Webhooks can be revoked/regenerated, invalidating old URLs

**Issue: "Message not appearing in channel"**
- **Solution**: Check the webhook is configured for the correct channel
- **Why**: Webhooks are channel-specific; changing channels requires new webhook

**Issue: "Rate limiting errors"**
- **Solution**: Reduce message frequency or batch updates
- **Why**: Slack limits webhook requests (1 message per second)

**Issue: "Formatting not displaying correctly"**
- **Solution**: Use Slack's message formatting tester
- **Why**: Slack uses mrkdwn, which differs slightly from standard Markdown

**Best Practices:**

1. **Channel Organization**: Create dedicated channels for different automation types (#automation-leads, #automation-errors)
2. **Clear Messaging**: Include context, not just "Success" or "Error"
3. **Actionable Alerts**: Include links to dashboards, logs, or next steps
4. **Avoid Spam**: Don't send a message for every minor event; batch updates
5. **Emoji for Quick Scanning**: Use emojis (✅, 🚨, ℹ️) to make alerts scannable

**Alternative: Slack Bot API**

For more advanced Slack integration (two-way communication, reading messages, etc.), consider the full Slack Bot API instead of incoming webhooks. This requires:
- OAuth setup (similar to Google Drive)
- Bot token with appropriate scopes
- More complex configuration

Use webhooks for simple outbound notifications; use the Bot API when you need agents to read Slack messages or interact with users.

## Advanced MCP Patterns

### Chaining Multiple MCPs

The real power of MCPs emerges when you chain them together in multi-step workflows. Each MCP provides a specific capability; combining them creates sophisticated automation.

**Example 1: Web Research → Spreadsheet**

```
1. Brave Search MCP: Search for "Melbourne SaaS companies"
2. Playwright MCP: Visit each result and scrape contact info
3. Google Drive MCP: Write results to "Lead Database" spreadsheet
4. Slack MCP: Notify sales team "15 new leads added"
```

**Example 2: Scheduled Report Generation**

```
1. Filesystem MCP: Read sales data from data/sales.csv
2. (Agent processes data and generates insights)
3. Google Drive MCP: Write report to "Weekly Sales Report" doc
4. Slack MCP: Post summary to #sales channel
```

**Example 3: Self-Annealing After Error**

```
1. Playwright MCP: Attempts website interaction, fails
2. Filesystem MCP: Read directive file to understand expected behavior
3. (Agent diagnoses issue)
4. Filesystem MCP: Update directive with edge case handling
5. Slack MCP: Notify team "Directive updated after error"
```

**Best Practices for Chaining:**

- **Sequential Dependencies**: Ensure each step completes before the next begins
- **Error Propagation**: If step 2 fails, don't proceed to step 3
- **Intermediate Validation**: Verify data quality between MCP operations
- **Rollback Capability**: Have a plan to undo changes if later steps fail

### Error Handling Across MCPs

When chaining MCPs, errors can occur at any step. Robust workflows need comprehensive error handling.

**Error Handling Strategy:**

```
1. Try MCP Operation
2. Check for errors
3. If error:
   a. Log error details (what failed, why, context)
   b. Determine if retryable or fatal
   c. If retryable: retry with exponential backoff
   d. If fatal: invoke stuck agent for human escalation
4. If success: proceed to next step
```

**Common Error Types:**

| Error Type | Retryable? | Handling Strategy |
|------------|-----------|-------------------|
| Network timeout | Yes | Retry with backoff |
| Rate limit exceeded | Yes | Wait and retry |
| Authentication failure | No | Check credentials, escalate |
| Invalid input | No | Validate input, escalate |
| File not found | No | Verify path, escalate |
| Permission denied | No | Check permissions, escalate |

**Example Error Handling in Directive:**

```markdown
## Error Handling Protocol

### Playwright Navigation Timeout
- Retry 3 times with 10s delay
- If still failing, invoke stuck agent with URL and error details

### Brave Search Rate Limit
- Wait 60 seconds
- Retry the search
- If repeated failures, defer to next hour

### Google Drive File Not Found
- Do NOT retry (file won't appear)
- Escalate immediately with file name and expected location
```

### Performance Considerations

MCPs involve external operations (network calls, file I/O, browser automation) which are slower than in-memory operations. Optimize for performance:

**1. Batch Operations**

Instead of:
```
For each of 100 leads:
  - Search for lead name (Brave Search)
  - Open company website (Playwright)
  - Extract email (Playwright)
  - Write to spreadsheet (Google Drive)
```

Do:
```
For each of 100 leads:
  - Search for lead name (Brave Search)
  - Open company website (Playwright)
  - Extract email (Playwright)
  - Store in memory

Write all 100 leads to spreadsheet at once (Google Drive)
```

This reduces Google Drive API calls from 100 to 1.

**2. Parallel Operations**

When operations are independent, run them in parallel:

```
Parallel:
  - Brave Search for "competitor pricing"
  - Playwright screenshot of own pricing page
  - Google Drive fetch last quarter's pricing data

Then:
  - Analyze all three inputs together
```

**3. Caching**

For data that doesn't change frequently, cache it:

```
If file data/company-info.json exists and is less than 24 hours old:
  - Read from local file (Filesystem MCP)
Else:
  - Fetch from Google Drive
  - Write to local cache
  - Use cached version
```

**4. Lazy Loading**

Don't load data until you need it:

```
Read directive (Filesystem)
Parse which data sources are required
Only fetch those specific sources (Google Drive, Brave Search)
```

### Security Best Practices

Running multiple MCPs increases the attack surface. Follow these security principles:

**1. Principle of Least Privilege**

Each MCP should have the minimum permissions necessary:
- Filesystem: Only specific directories, not entire system
- Google Drive: Only necessary folders, not all files
- Slack: Only specific channels

**2. Credential Isolation**

Never reuse credentials across different environments:
- Development: Use separate API keys
- Staging: Different Google account
- Production: Dedicated service accounts

**3. Audit Logging**

Log all MCP operations for security auditing:
```
[2026-02-14 10:23:15] Filesystem: Read directives/sales-automation.md
[2026-02-14 10:23:47] Brave Search: Query "competitor pricing"
[2026-02-14 10:24:02] Google Drive: Write to file ID abc123
[2026-02-14 10:24:10] Slack: Message sent to #sales
```

**4. Rate Limiting**

Implement rate limits even if the MCP doesn't enforce them:
- Prevent accidental DoS of external services
- Avoid triggering security alerts
- Stay within free tier limits

**5. Secrets Management**

For production deployments:
- Use environment variable injection (not `.env` files)
- Consider dedicated secrets management (AWS Secrets Manager, HashiCorp Vault)
- Rotate credentials regularly
- Never log or expose credentials in error messages

## Quick Reference Tables

### MCP Comparison Table

| MCP | Use Case | Setup Difficulty | Typical Cost | Best For |
|-----|----------|-----------------|--------------|----------|
| **Playwright** | Browser automation, testing, scraping | Medium | Free | Web interaction, visual testing |
| **Filesystem** | File operations, directive management | Easy | Free | Local file management, self-annealing |
| **Brave Search** | Web research, lead discovery | Easy | Free tier available | Market research, contact finding |
| **Google Drive** | Document access, spreadsheets | Hard (OAuth) | Free tier available | Team collaboration, data storage |
| **Slack** | Notifications, alerts | Easy | Free tier available | Team communication, monitoring |
| **GitHub** | Code management, version control | Medium | Free tier available | Directive versioning, CI/CD |
| **Database** | Structured data storage | Medium | Varies | CRM data, transaction logs |
| **Email** | Sending emails | Easy | Varies | Notifications, reports |

### Common Configuration Snippets

**Basic .mcp.json with Multiple Servers:**

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-playwright"]
    },
    "filesystem": {
      "command": "npx",
      "args": [
        "@modelcontextprotocol/server-filesystem",
        "/Users/yourname/projects/automation",
        "--allowed-paths",
        "/Users/yourname/projects/automation/directives",
        "/Users/yourname/projects/automation/executions",
        "/Users/yourname/projects/automation/data"
      ]
    },
    "brave-search": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "${BRAVE_API_KEY}"
      }
    },
    "google-drive": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-google-drive"],
      "env": {
        "GOOGLE_CLIENT_ID": "${GOOGLE_CLIENT_ID}",
        "GOOGLE_CLIENT_SECRET": "${GOOGLE_CLIENT_SECRET}"
      }
    },
    "slack": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-slack"],
      "env": {
        "SLACK_WEBHOOK_URL": "${SLACK_WEBHOOK_URL}"
      }
    }
  }
}
```

**Corresponding .env File:**

```
# Brave Search API Key
BRAVE_API_KEY=BSAyour_api_key_here

# Google Drive OAuth Credentials
GOOGLE_CLIENT_ID=123456789.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=your_client_secret_here

# Slack Webhook
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/YOUR/WEBHOOK/URL
```

### Troubleshooting Decision Tree

```
MCP not working?
│
├─ Is MCP installed?
│  ├─ No → Run installation command
│  └─ Yes → Continue
│
├─ Is .mcp.json valid JSON?
│  ├─ No → Fix syntax errors
│  └─ Yes → Continue
│
├─ Are credentials configured?
│  ├─ No → Add to .env file
│  └─ Yes → Continue
│
├─ Are environment variables loaded?
│  ├─ No → Restart Antigravity IDE / reload environment
│  └─ Yes → Continue
│
├─ Does MCP server start successfully?
│  ├─ No → Check error logs
│  └─ Yes → Continue
│
├─ Are permissions correct?
│  ├─ No → Fix file/API permissions
│  └─ Yes → Continue
│
└─ Still not working?
   └─ Check Appendix H: Troubleshooting Guide
```

## Summary and Next Steps

This appendix has provided comprehensive configuration instructions for the five essential MCPs for business automation:

1. **Playwright MCP**: Browser control for testing and scraping
2. **Filesystem MCP**: File operations for directives and data
3. **Brave Search MCP**: Web research for lead generation
4. **Google Drive MCP**: Document and spreadsheet access
5. **Slack MCP**: Notifications and team communication

You've also learned:
- Core MCP concepts (server-client architecture, configuration patterns)
- Security best practices (credential management, least privilege)
- Advanced patterns (chaining, error handling, performance optimization)
- Troubleshooting strategies for common issues

**Recommended Next Steps:**

1. **Start Small**: Configure just one MCP (Filesystem is easiest) and verify it works
2. **Add Gradually**: Once comfortable, add additional MCPs one at a time
3. **Build a Test Workflow**: Create a simple multi-MCP workflow to understand chaining
4. **Review Security**: Audit your `.env` file and ensure it's in `.gitignore`
5. **Document Your Setup**: Keep notes on which MCPs you use and why

**Cross-References:**

- **Chapter 17**: Deep dive into MCP concepts and philosophy
- **Chapter 14**: See the tester agent using Playwright MCP in practice
- **Appendix H**: Troubleshooting guide for when MCPs misbehave

┌─────────────────────────────────────────────────────┐
│  DOWNLOAD READY-TO-USE CONFIGURATIONS              │
│                                                      │
│  Get pre-configured .mcp.json files for all the     │
│  MCPs covered in this appendix:                     │
│                                                      │
│  travissteel.net/the-last-employee/resources#reference          │
│                                                      │
│  Includes: Playwright, Filesystem, Brave Search,    │
│  Google Drive, Slack, and more.                     │
└─────────────────────────────────────────────────────┘

**Remember**: MCPs are tools, not magic. They give your agents capabilities, but the real power comes from well-designed directives that use those capabilities effectively. Start with clear objectives, define your "Definition of Done," and let the MCPs execute the work.

Now you're ready to give your agents the hands and eyes they need to automate any business workflow!
