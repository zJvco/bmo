---
name: research
description: Conduct comprehensive research — market, technical, or domain/industry — using current web data and verified sources. Use this skill whenever the user mentions "research", "analyze the market", "competitive analysis", "technical evaluation", "industry analysis", "domain research", "I want to build X, can you research it?", "should we enter this market?", "which technology should we use?", "understand the landscape", or wants to validate an idea, evaluate a technology, or understand an industry. Trigger even when research type is unclear — this skill will guide the user to the right workflow.
---

# Research Skill

Conduct structured, web-verified research across three types: **Market**, **Technical**, and **Domain**. Each type follows a step-by-step workflow with user confirmation at every stage.

## Prerequisites

**Web search is required.** If unavailable, stop and inform the user.

## Step 0 — Load Config (Always First)

Before anything else:

1. Read `.bmo/config.yaml`.
   - **If missing**: stop and say:
     > "⚠️ Config file not found at `.bmo/config.yaml`. Please create it before running this skill."
   - **If found**, extract: `project_name`, `output_folder`, `communication_language`, `document_output_language`.
     Speak to the user in `communication_language`. Write all document content in `document_output_language`.

2. Read `./_output/project-context.md`.
   - **If missing**: warn and continue:
     > "⚠️ Project context file not found at `./_output/project-context.md`. Continuing without it — consider creating it for better results."
   - **If found**: read it fully before proceeding. Use it to personalize and ground all outputs.

---

## Step 1 — Discover Topic and Choose Research Type

Greet the user and ask what they want to research. Keep it light and conversational.

**Say something like:**

> "Welcome! Let's get your research started. What do you want to research or learn more about?
>
> Once I know the topic, I'll help you pick the right research approach."

After the user describes their topic, **recommend a research type** based on what they said. Briefly explain what each type covers so they can confirm or redirect:

---

### Research Types

**🛒 Market Research**
Best for understanding *customers, competitors, and business opportunity*.
→ Use this if you want to know: Who are the customers? What do they need? Who else is in this space? Is there a market for this?
*Example: "I want to launch a fitness app — who are my customers and competitors?"*

**🔧 Technical Research**
Best for evaluating *technologies, architectures, and implementation approaches*.
→ Use this if you want to know: Which framework should I use? How do others solve this technical problem? What's the best architecture?
*Example: "Should we use GraphQL or REST for our new API?"*

**🏭 Domain Research**
Best for understanding *an industry or sector in depth* — its dynamics, regulations, and trends.
→ Use this if you want to know: How does this industry work? What regulations apply? Who are the main players and what trends are shaping it?
*Example: "I need to understand the European sustainable packaging market."*

---

**Ask the user to confirm:**

> "Based on what you shared, I'd suggest **[recommended type]** — does that sound right? Or would you like a different approach?"

> 💡 **Tip:** Each research type follows a structured step-by-step process. Following all steps leads to better, more complete results — I'll guide you through each one.

---

## Step 2 — Route to Workflow

Once the user confirms the research type, load the appropriate workflow file:

| Type | File to Load |
|---|---|
| Market Research | `./references/market-research.md` |
| Technical Research | `./references/technical-research.md` |
| Domain Research | `./references/domain-research.md` |

Pass the discovered topic and goals into the workflow so it doesn't ask again.

---

## Output Format

Save research to a single Markdown file using the path from config:
`{output_folder}/research/{type}-{topic-slug}-{YYYY-MM-DD}.md`

Example: `./_output/research/market-ev-europe-2026-02-27.md`

Use this document frontmatter:

```markdown
---
topic: [research topic]
date: [today's date]
goals: [research goals]
status: complete
---
```

---

## Research Standards (apply to all types)

- **Always cite URLs** for web search results. No unsourced claims.
- **Use current sources** — prefer content from the past 1–2 years where possible.
- **Flag uncertainty** — if data is scarce or conflicting, say so explicitly.
- **Multiple sources** for critical claims.
- **Write in prose** for synthesis sections; use structured lists for data sections.
- Run searches in parallel where possible to save time.