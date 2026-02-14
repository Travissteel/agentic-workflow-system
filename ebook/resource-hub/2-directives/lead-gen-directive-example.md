# Lead Qualification Workflow Directive

**Created**: February 2026
**Owner**: Sales Operations
**Frequency**: Continuous (triggered on form submission)

---

## Objective

**What needs to happen:**
Automatically qualify inbound leads from website contact forms by enriching company data, scoring leads based on predefined criteria, and routing high-priority leads directly to sales reps while filtering out unqualified prospects.

**Why this matters:**
Manually qualifying 50-100 weekly form submissions takes 5-8 hours of sales team time. By automating lead enrichment and scoring, we reduce response time from 24 hours to under 5 minutes for hot leads while eliminating 40% of unqualified prospects before they reach the sales team. This allows reps to focus on closing deals instead of researching companies.

---

## Inputs

**Required Data:**
- [ ] Form submission data: Name, Email, Company Name, Job Title, Message
- [ ] CRM access: HubSpot API with read/write permissions
- [ ] Lead enrichment API: Apollo.io or Clearbit for company data

**Required Access:**
- [ ] Website form webhook (Webflow, WordPress, or custom)
- [ ] HubSpot API key with contacts and companies scope
- [ ] Apollo API key with enrichment credits
- [ ] Email service: SendGrid or Resend for notifications
- [ ] Slack webhook for hot lead alerts (optional)

**Trigger Conditions:**
- **When**: Contact form is submitted on website
- **If**: Submission contains valid email address and company name

---

## Process

**Step-by-step workflow (in plain English):**

1. **Receive Form Submission**
   - Success looks like: Webhook payload contains name, email, company, title, and message
   - If error: If any required field is missing, send to "incomplete submissions" queue and notify admin via email

2. **Validate Email Address**
   - Check if email format is valid (contains @ and valid domain)
   - Check if domain is not a free provider (gmail.com, yahoo.com, outlook.com)
   - Success looks like: Email is valid and from business domain
   - If error: If free email address, mark lead as "Low Priority - Personal Email" and skip enrichment

3. **Check for Duplicate in CRM**
   - Search HubSpot contacts by email address
   - Success looks like: Found existing contact OR confirmed new contact
   - If error: If HubSpot API fails, retry once after 5 seconds; if still failing, create local record and flag for manual sync

4. **Enrich Company Data**
   - Send company name to Apollo API for enrichment
   - Extract: Employee count, industry, revenue range, technologies used
   - Success looks like: Apollo returns company data with at least 3 of 4 fields populated
   - If error: If Apollo returns no match, use company domain from email to retry lookup; if still no match, proceed with basic data only

5. **Calculate Lead Score (0-100)**
   - **Employee Count** (0-40 points):
     * 1-10 employees: 0 points
     * 11-50 employees: 10 points
     * 51-200 employees: 25 points
     * 201-1000 employees: 35 points
     * 1000+ employees: 40 points
   - **Industry Match** (0-20 points):
     * Target industries (SaaS, E-commerce, Professional Services): 20 points
     * Adjacent industries (Tech, Marketing): 10 points
     * Other industries: 0 points
   - **Job Title** (0-30 points):
     * C-level (CEO, CTO, CFO): 30 points
     * VP/Director: 20 points
     * Manager: 10 points
     * Individual contributor: 0 points
   - **Technologies Used** (0-10 points):
     * Uses competing tools: 10 points
     * Uses complementary tools: 5 points
     * No relevant tech detected: 0 points
   - Success looks like: Lead score between 0-100 calculated
   - If error: If any scoring data is missing, assign 0 for that category and continue

6. **Categorize Lead by Score**
   - **Hot Lead** (70-100 points):
     * Assign to sales rep immediately
     * Send Slack alert to #sales-hot-leads channel
     * Send personalized email to lead within 5 minutes
   - **Warm Lead** (40-69 points):
     * Add to "Warm Prospects" workflow in HubSpot
     * Schedule follow-up task for sales rep (next business day)
     * Send automated "Thanks for your interest" email
   - **Cold Lead** (0-39 points):
     * Add to nurture campaign
     * No immediate sales contact
     * Send generic "Thanks for contacting us" email
   - Success looks like: Lead assigned to correct category and workflow
   - If error: If categorization logic fails, default to Warm Lead and notify admin

7. **Create or Update HubSpot Contact**
   - If new contact: Create with all enriched data
   - If existing contact: Update with new form submission data and recalculated score
   - Add form message as note
   - Tag with "Auto-Qualified" and current date
   - Success looks like: Contact appears in HubSpot with correct data and tags
   - If error: If HubSpot API fails, save data locally and retry up to 3 times; if still failing, escalate to stuck agent

8. **Assign to Sales Rep (Hot and Warm Leads)**
   - Round-robin assignment based on rep availability
   - Create task in HubSpot: "Follow up with [Company Name] - [Score] points"
   - Include enriched data in task notes
   - Success looks like: Task assigned and visible in rep's queue
   - If error: If no reps available, assign to sales manager

9. **Send Notifications**
   - **For Hot Leads**: Slack alert + SMS to assigned rep
   - **For Warm Leads**: Email to assigned rep
   - **For All Leads**: Log entry to leads_processed.csv
   - Success looks like: All notifications sent successfully
   - If error: If Slack fails, fall back to email only

10. **Log Completion**
    - Record: Lead name, company, score, category, assigned rep, timestamp
    - Update dashboard: Total leads processed today, average score, hot/warm/cold breakdown
    - Success looks like: Log entry created and dashboard updated
    - If error: If logging fails, continue (logging is non-critical)

**Edge Cases & Exceptions:**

- **If company name is vague or generic** (e.g., "ABC Corp"): Use email domain to look up company instead
- **If multiple contacts from same company**: Link to existing company record in HubSpot instead of creating duplicate
- **If form submission is spam** (contains spam keywords like "SEO services", "viagra"): Mark as spam and delete without processing
- **If lead score ties exactly at boundary** (e.g., exactly 70 points): Round up to higher category
- **If all sales reps are at capacity**: Create unassigned task and alert sales manager

---

## Definition of Done

**This workflow is complete when:**
- [ ] Form submission is validated and processed
- [ ] Company data is enriched with at least 3 data points
- [ ] Lead score is calculated (0-100)
- [ ] Lead is categorized (Hot/Warm/Cold)
- [ ] HubSpot contact is created or updated
- [ ] Hot and Warm leads are assigned to sales reps
- [ ] All notifications are sent
- [ ] Completion is logged

**Quality Standards:**
- Lead scoring is consistent (same inputs = same score)
- Hot leads are alerted within 5 minutes of form submission
- Enriched data is accurate (no mismatched companies)
- No duplicate contacts created in HubSpot
- Email notifications are personalized (use actual names, not "Hi there")
- Spam leads are filtered out (0 spam in sales queue)

**Notification:**
- **Who to notify**: Sales Operations Manager
- **How**: Daily summary email at 5 PM
- **What to include**: Total leads processed, hot/warm/cold breakdown, average score, any errors

---

## Notes & Learnings

**Known Issues:**
- Apollo sometimes can't match companies with unusual names (use domain lookup as backup)
- HubSpot API occasionally times out during high traffic (retry logic handles this)
- Free email addresses (Gmail, Yahoo) don't enrich well (we filter these early now)

**Optimization Ideas:**
- Add LinkedIn profile enrichment to improve job title accuracy
- Consider adjusting employee count thresholds based on actual conversion data
- Experiment with bonus points for "urgent" keywords in form message

**Self-Annealing Updates:**
- Feb 2026: Added spam keyword filter after 12 spam submissions in one day
- Feb 2026: Increased timeout for Apollo API from 5s to 10s after seeing occasional slowness
- Feb 2026: Added email domain fallback for company lookup when name doesn't match
