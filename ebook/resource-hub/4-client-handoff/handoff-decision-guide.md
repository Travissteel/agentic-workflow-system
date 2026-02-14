# The 3-Question Handoff Decision Guide

Use this decision tree during your discovery call or immediately after your intake form. Three simple questions will tell you which handoff model to propose.

---

## Question 1: Is the client technical?

**How to assess:**
- Do they have developers or IT staff in-house?
- Have they built internal tools or integrations before?
- Are they comfortable reading code, even if they don't write it?

**If YES**: They're a candidate for GitHub Codespace or Manual Folder.
**If NO**: They need Hybrid Wrapper or Managed Service.

---

## Question 2: Do they want ongoing support?

**How to assess:**
- Ask directly: "After we build this, do you want us to maintain it, or would you prefer to own it completely?"
- Listen for signals: "We want to be able to change it ourselves" vs "We just want it to work"
- Consider their team capacity: Do they have bandwidth to manage another system?

**If YES (ongoing support)**: Managed Service is the best fit.
**If NO (one-time delivery)**: Hybrid Wrapper, GitHub Codespace, or Manual Folder.

---

## Question 3: What's their budget?

**How to assess:**
- Are they a small business ($2K-$10K project budgets)?
- Mid-market company ($10K-$50K project budgets)?
- Enterprise ($50K+ project budgets)?

**Budget implications:**
- **Low ($2K-$10K)**: Manual Folder or simplified Hybrid Wrapper
- **Medium ($10K-$30K)**: Hybrid Wrapper or GitHub Codespace
- **High ($30K+)**: Managed Service or premium Hybrid Wrapper with extensive training

---

## Decision Matrix

| Question 1: Technical? | Question 2: Support? | Question 3: Budget? | Recommended Model |
|------------------------|----------------------|---------------------|-------------------|
| No | Yes | Any | Managed Service |
| No | No | Medium-High | Hybrid Wrapper (n8n + Modal) |
| No | No | Low | Hybrid Wrapper (simplified) |
| Yes | Yes | High | Managed Service (premium tier) |
| Yes | No | Medium-High | GitHub Codespace |
| Yes | No | Low | Manual Folder |

---

## Visual Decision Tree

```
START: New Client
    |
    Is client technical?
    ├─ NO ──> Do they want ongoing support?
    │         ├─ YES ──> Managed Service
    │         └─ NO ──> Hybrid Wrapper (n8n + Modal)
    │
    └─ YES ──> Do they want ongoing support?
              ├─ YES ──> Budget?
              │          ├─ High ──> Managed Service (premium)
              │          └─ Low-Med ──> Hybrid Wrapper
              └─ NO ──> Budget?
                         ├─ Medium-High ──> GitHub Codespace
                         └─ Low ──> Manual Folder
```

---

## Common Edge Cases

**"We're semi-technical but don't have time"**
→ Hybrid Wrapper. They'll appreciate the visual interface and won't feel condescended to.

**"We want to learn how to build this ourselves eventually"**
→ GitHub Codespace with training sessions. Position it as education, not just delivery.

**"We want you to build it, but we need to white-label it for our clients"**
→ Manual Folder or GitHub Codespace with licensing agreement. They need full ownership.

**"We're not sure what we need yet"**
→ Start with Managed Service on a 3-month pilot. Lock in recurring revenue while they figure out their strategy.

---

## The Four Handoff Models (Quick Recap)

### 1. Hybrid Wrapper (n8n + Modal) - RECOMMENDED FOR MOST

**What it is**: Complex Python logic deployed to Modal, wrapped in an n8n visual workflow

**Best for:**
- Non-technical clients who want control
- Medium budget ($10K-$30K)
- One-time delivery but with maintainability

**Pros:**
- Client can modify triggers and actions without code
- Visual, understandable interface
- Proven, stable, easy to support

**Cons:**
- Client needs n8n account ($20-50/month)
- Some technical learning curve

---

### 2. Managed Service

**What it is**: You host, maintain, and continuously optimize everything

**Best for:**
- Clients who want results, not responsibility
- Any technical level
- Recurring revenue model

**Pros:**
- Easiest for client (zero maintenance)
- Recurring monthly revenue for you
- Continuous optimization

**Cons:**
- Client is dependent on you
- Ongoing support overhead

---

### 3. GitHub Codespace

**What it is**: One-click development environment with all code and docs

**Best for:**
- Technical clients who want full control
- Medium-high budget ($10K-$50K)
- Clients who may extend the workflow themselves

**Pros:**
- Full transparency and control
- Easy for technical teams to modify
- Professional delivery method

**Cons:**
- Requires technical expertise
- Client must manage their own hosting

---

### 4. Manual Folder

**What it is**: Folder with directives and executions, client sets up environment

**Best for:**
- Technical clients on tight budget
- Internal teams
- Quick handoffs

**Pros:**
- Simplest for you
- Full ownership for client
- Low cost

**Cons:**
- Most setup work for client
- Minimal hand-holding
- Higher risk of setup issues

---

## How to Use This Guide

1. **During Discovery Call**: Ask the three questions naturally in conversation
2. **Immediately After**: Use the decision matrix to determine recommended model
3. **In Proposal**: Explain why this model fits their situation
4. **Offer Alternative**: Present one backup option in case they prefer different approach

---

## Example Decision Flow

**Client: Mid-size marketing agency**
- Question 1 (Technical?): No in-house developers, but comfortable with tools like Zapier
- Question 2 (Support?): Want to own it, don't want ongoing costs
- Question 3 (Budget?): $15K project budget

**Decision**: Hybrid Wrapper (n8n + Modal)

**Why**: They're semi-technical (comfortable with visual tools), want one-time delivery, and have medium budget. Hybrid Wrapper gives them visual control without requiring code expertise.

---

**Related Resources:**
- `client-intake-form.md` - Gather data to answer these questions
- `managed-service-proposal.md` - Template for ongoing support model
- `full-handover-proposal.md` - Template for one-time delivery model
