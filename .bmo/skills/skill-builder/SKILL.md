---
name: skill-builder
description: A full-wizard skill for creating, modifying, and improving skills inside a bmo project. Use this skill whenever the user wants to create a new skill, build a skill, add a skill to the project, or automate a new workflow. Also trigger when the user wants to edit, update, fix, improve, or refine an existing skill. Guides the user step-by-step through intent capture, SKILL.md authoring, test case creation, and saving — all following bmo project conventions. Trigger even if the user just says "let's make a skill", "I want to automate X", "update my skill", or "this skill needs fixing".
---

# Skill Builder

A full-wizard skill that guides users through creating, modifying, and improving skills, following all bmo project conventions.

---

## Step 0 — Load Config (Always First)

Before anything else:

1. Read `.bmo/config.yaml`.
   - **If missing**: stop and say:
     > "⚠️ Config file not found at `.bmo/config.yaml`. Please create it before running this skill."
   - **If found**, extract and hold these values for the entire session:
     - `project_name`
     - `output_folder`
     - `communication_language` → speak to the user in this language from now on
     - `document_output_language` → write all skill file content in this language

2. Read `.bmo/_output/project-context.md`.
   - **If missing**: warn and continue:
     > "⚠️ Project context file not found at `.bmo/_output/project-context.md`. Continuing without it — consider creating it for better results."
   - **If found**: read it fully before proceeding.

---

## Step 1 — Detect Mode: Create or Edit?

Ask the user what they want to do if it isn't already clear from context:

- **Create**: Build a new skill from scratch → follow Steps 2–6
- **Edit**: Modify or improve an existing skill → follow the [Edit Flow](#edit-flow) below

---

## Create Flow

### Step 2 — Capture Intent

Ask the user (one conversational message, not a form):

1. **What should this skill do?** What problem does it solve?
2. **When should it trigger?** What phrases or situations should activate it?
3. **What's the expected output?** A file? A summary? An action?
4. **Does it need test cases?** Skills with verifiable outputs (files, structured data, code) benefit from tests. Skills with subjective outputs (style, tone) usually don't. Suggest the appropriate default and let the user confirm.

Wait for answers before proceeding. Summarize back what you understood and ask for confirmation.

---

### Step 3 — Interview & Research

Go deeper before writing anything. Ask about:

- **Edge cases**: What should happen with incomplete input, missing files, ambiguous requests?
- **Input format**: What does the user provide? A topic? A file? A URL?
- **Output format**: Markdown doc? Structured YAML? Plain text?
- **Dependencies**: Does this skill need web search, file creation, specific tools?
- **Examples**: Can the user show an example input and ideal output?

Also check if there are similar skills already in `.bmo/skills/` to avoid duplication or to use as a reference.

Once you feel confident, summarize the plan and ask for a green light before writing the skill.

---

### Step 4 — Write the SKILL.md

Create the skill at:
```
.bmo/skills/{skill-name}/SKILL.md
```

Every skill MUST include the following sections:

#### Required: YAML Frontmatter

```yaml
---
name: {skill-name}
description: [When to trigger + what it does. Be specific and slightly pushy — mention all phrases, contexts, and synonyms that should trigger it.]
---
```

#### Required: Config Loading Block

Every skill must start with this block verbatim (adapt paths if needed, but keep the logic):

```markdown
## Step 0 — Load Config (Always First)

Before anything else:

1. Read `.bmo/config.yaml`.
   - **If missing**: stop and say:
     > "⚠️ Config file not found at `.bmo/config.yaml`. Please create it before running this skill."
   - **If found**, extract: `project_name`, `output_folder`, `communication_language`, `document_output_language`.
     Speak to the user in `communication_language`. Write all document content in `document_output_language`.

2. Read `.bmo/_output/project-context.md`.
   - **If missing**: warn and continue:
     > "⚠️ Project context file not found at `.bmo/_output/project-context.md`. Continuing without it — consider creating it for better results."
   - **If found**: read it fully. Use it to ground and personalize all outputs.
```

#### Required: Output File Naming

All skill output files must follow:
```
{output_folder}/{skill-name}/{topic-slug}-{YYYY-MM-DD}.md
```

Example: `.bmo/_output/research/ev-europe-2025-03-14.md`

#### Skill Body

Write the rest of the skill's instructions clearly and concisely:
- Use numbered steps for sequential workflows
- Keep SKILL.md under 500 lines; move large reference content to `references/` subfolder
- If the skill supports multiple domains or variants, organize into `references/{variant}.md` and point to them from SKILL.md

Show the draft to the user and ask for feedback before moving on.

---

### Step 5 — Create Test Cases

If the user agreed to test cases (Step 2), create 3–5 test prompts that represent realistic usage:

- **Trigger tests**: Does the skill activate when it should?
- **Happy path**: Normal, well-formed input → expected output
- **Edge cases**: Missing input, unusual phrasing, ambiguous requests

For each test case, run through the skill yourself following its instructions, then show the user the output and ask: *"How does this look? Anything you'd change?"*

Collect feedback and refine the SKILL.md accordingly. Repeat until the user is satisfied.

---

### Step 6 — Save the Skill

Once the skill is approved, save it to the project:

```bash
python -m scripts.save_skill {skill-name}
```

This will validate the skill at `.bmo/skills/{skill-name}/SKILL.md` and confirm everything is in order.

Confirm to the user:
> "Your skill **{skill-name}** is ready! It's saved at `.bmo/skills/{skill-name}/SKILL.md` and follows all bmo project conventions."

---

## Edit Flow

Use this flow when the user wants to modify or improve an existing skill.

### Step E1 — Identify the Skill

Ask which skill they want to edit if not already clear. Read the current SKILL.md from:
```
.bmo/skills/{skill-name}/SKILL.md
```

Show a brief summary of what the skill currently does and ask: *"What would you like to change or improve?"*

### Step E2 — Understand the Change

Clarify the requested change before touching anything:

- Is this a **bug fix**? (skill behaves incorrectly or inconsistently)
- Is this a **refinement**? (improve wording, add an edge case, tighten a step)
- Is this an **extension**? (add new capability or output format)
- Is this a **description/trigger improvement**? (skill isn't activating when it should)

Summarize the planned change and ask for confirmation.

### Step E3 — Edit the SKILL.md

Apply the changes directly to `.bmo/skills/{skill-name}/SKILL.md`. Show a clear before/after diff of what changed and explain why each change was made.

Make sure the edit preserves all required conventions:
- [ ] YAML frontmatter with `name` and `description` intact
- [ ] Config loading block still present
- [ ] Output file naming pattern still present
- [ ] No steps removed accidentally

### Step E4 — Review & Iterate

Ask the user: *"How does this look? Anything else to adjust?"*

Repeat Steps E2–E3 until the user is satisfied.

### Step E5 — Save the Updated Skill

```bash
python -m scripts.save_skill {skill-name}
```

Confirm to the user:
> "Skill **{skill-name}** has been updated and saved at `.bmo/skills/{skill-name}/SKILL.md`."

---

## Conventions Reference

For full details on config loading and output naming, see:
`.bmo/references/config-convention.md`

---

## Quick Checklist

Before finishing, verify every skill (new or edited) has:

- [ ] YAML frontmatter with `name` and `description`
- [ ] Config loading block at the top (Step 0) — reads `.bmo/config.yaml`
- [ ] Project context loading — reads `.bmo/_output/project-context.md` (warn if missing)
- [ ] Output file naming pattern: `{output_folder}/{skill-name}/{topic-slug}-{YYYY-MM-DD}.md`
- [ ] Language behavior (communicate in `communication_language`, write docs in `document_output_language`)
- [ ] Clear, numbered workflow steps
- [ ] Saved to `.bmo/skills/{skill-name}/SKILL.md`