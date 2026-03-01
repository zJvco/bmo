---
name: project-context
description: Creates or updates a project-context.md file containing critical rules, patterns, and implementation guidelines that AI agents must follow when writing code for this project. Use this skill whenever the user says "create project context", "set up project context", "initialize project context", "update project context", or when starting a new project and other skills reference a missing project-context.md. Also trigger when the user says things like "agents keep making the same mistakes" or "I want to set up rules for AI agents" — this skill captures exactly that. Run this before using the research, prd, or any implementation skill for the first time on a project.
---

# Project Context Creator

Create or update a `project-context.md` file — the shared memory that tells every AI agent how to implement code consistently in this project. Focused on **unobvious rules** that agents would otherwise miss.

## Prerequisites

No web search required. This skill works entirely from local project files and user input.

## Step 0 — Load Config (Always First)

Before anything else, read `.bmo/config.yaml`.

- **If missing**: stop and say:
  > "⚠️ Config file not found at `.bmo/config.yaml`. Please create it before running this skill."
- **If found**, extract: `project_name`, `output_folder`, `communication_language`, `document_output_language`.
  Speak to the user in `communication_language`. Write all document content in `document_output_language`.

Resolve these paths:
- `output_file` = `{output_folder}/project-context.md`

---

## Step 1 — Discover & Initialize

🚫 Do not generate any content yet. This step is discovery only.

### 1.1 Check for Existing Context

Look for an existing file at `output_file`.

- **If found**: read it fully. Tell the user how many sections it has and ask:
  > "I found an existing project context with [N] sections. Would you like to update it or create a fresh one?"
- **If not found**: proceed to create a new one.

### 1.2 Scan Project Files

Read and analyze available project files to understand the technology stack and conventions. Look for:

**Architecture & planning:**
- `**/architecture.md` or `**/ARCHITECTURE.md`
- Any planning artifacts in the output folder

**Package & dependency files:**
- `package.json`, `requirements.txt`, `Cargo.toml`, `go.mod`, `Gemfile`, `pyproject.toml`
- Extract exact versions of all key dependencies

**Configuration files:**
- `tsconfig.json`, `jsconfig.json`
- `next.config.js`, `vite.config.ts`, `webpack.config.js`
- `.eslintrc*`, `.prettierrc*`
- `jest.config.*`, `vitest.config.*`
- `.env.example` (for required environment variables)

**Existing code patterns** (scan a sample of source files):
- File and folder naming conventions
- Import/export patterns
- Component or module structure
- Test file naming and organization

### 1.3 Present Discovery Summary

Report what was found and ask the user to confirm before proceeding:

> "Here's what I found for **[project_name]**:
>
> **Technology Stack:**
> [List technologies and versions found]
>
> **Patterns Detected:**
> [List conventions, config rules, and structures found]
>
> **Areas I'll document:**
> - Technology stack & exact versions
> - Language-specific rules
> - Framework-specific patterns
> - Testing rules
> - Code quality & style rules
> - Development workflow rules
> - Critical anti-patterns to avoid
>
> Ready to generate your project context rules?
> [C] Continue"

🚫 Do not proceed until user selects [C].

---

## Step 2 — Generate Rules Collaboratively

Work through each category below. For each one: generate the content based on discovery, present it to the user, and wait for confirmation before moving on.

After presenting each category's content, always ask:
> **[C] Continue** — save these rules and move to the next category

🚫 Do not move to the next category until the user selects [C].

---

### Category 1: Technology Stack & Versions

Document the exact stack found during discovery. Be precise — agents need exact versions, not ranges.

```markdown
## Technology Stack & Versions

- [Language] [exact version]
- [Framework] [exact version]
- [Key dependency] [exact version]
- [Runtime/platform] [exact version]
```

Ask the user: *"Are there version constraints or compatibility notes I should add?"*

---

### Category 2: Language-Specific Rules

Focus on unobvious rules the language config enforces — not general best practices.

Examples to look for and document:
- TypeScript strict mode requirements (noImplicitAny, strictNullChecks, etc.)
- Import/export conventions (named vs default, barrel files, path aliases)
- Async/await vs Promise patterns
- Error handling patterns specific to this codebase
- Any language-version-specific syntax in use or forbidden

```markdown
### Language-Specific Rules

- [Specific rule with example if helpful]
- [Specific rule]
```

Ask: *"Any language rules agents commonly get wrong in this project?"*

---

### Category 3: Framework-Specific Rules

Document conventions that are specific to how *this project* uses its framework — not generic framework docs.

Examples:
- React: hooks patterns, component structure, state management library conventions
- Next.js: app vs pages router, data fetching patterns, API route conventions
- Express/Fastify: middleware order, error handler placement
- Any other framework in use

```markdown
### Framework-Specific Rules

- [Rule specific to how this project uses the framework]
- [Rule]
```

Ask: *"Any framework patterns agents should always follow or avoid here?"*

---

### Category 4: Testing Rules

Document what consistent test quality looks like in this project.

- Test file naming and location conventions
- How mocks are set up and where they live
- Unit vs integration vs e2e test boundaries
- Coverage expectations (if enforced)
- Any forbidden testing patterns (e.g., "never mock the DB directly, use test containers")

```markdown
### Testing Rules

- [Rule]
- [Rule]
```

Ask: *"Any testing rules that agents tend to miss or get wrong?"*

---

### Category 5: Code Quality & Style Rules

Document the enforced style that linting/formatting config locks in — agents should know what they can't change.

- Specific ESLint rules that cause failures if violated
- Prettier config values that affect code shape
- File and folder naming conventions (PascalCase components, kebab-case routes, etc.)
- Comment and documentation requirements

```markdown
### Code Quality & Style Rules

- [Rule]
- [Rule]
```

Ask: *"Anything the linter enforces that agents might accidentally break?"*

---

### Category 6: Development Workflow Rules

Document patterns that affect how agents should structure their work.

- Branch naming conventions
- Commit message format (conventional commits, custom patterns, etc.)
- PR/review requirements
- Environment variable handling (never hardcode, always use `.env.example` pattern, etc.)
- Deployment or build considerations agents should be aware of

```markdown
### Development Workflow Rules

- [Rule]
- [Rule]
```

Ask: *"Any workflow rules that affect how agents should submit or organize their work?"*

---

### Category 7: Critical Anti-Patterns

The most important category — things agents must **never** do in this codebase.

- Common mistakes made previously (if user knows them)
- Security rules (never log tokens, never expose secrets, etc.)
- Performance gotchas specific to this stack
- Architectural boundaries that must not be crossed
- Any "we tried this and it broke everything" patterns

```markdown
### Critical Anti-Patterns (Never Do These)

- ❌ [Anti-pattern with brief reason]
- ❌ [Anti-pattern]
```

Ask: *"What mistakes do agents (or humans) most often make in this project?"*

---

## Step 3 — Finalize & Save

Once all categories are complete, assemble and save the final file.

### 3.1 Build the Complete File

```markdown
---
project_name: [project_name]
generated_by: project-context-creator
date: [YYYY-MM-DD]
status: complete
---

# Project Context for AI Agents

_Critical rules and patterns for [project_name]. Read this before writing any code. Focus on the unobvious details — these are the things agents most often get wrong._

---

## Technology Stack & Versions

[Category 1 content]

## Critical Implementation Rules

### Language-Specific Rules

[Category 2 content]

### Framework-Specific Rules

[Category 3 content]

### Testing Rules

[Category 4 content]

### Code Quality & Style Rules

[Category 5 content]

### Development Workflow Rules

[Category 6 content]

### Critical Anti-Patterns (Never Do These)

[Category 7 content]

---

## Usage Guidelines

**For AI agents:** Read this file before implementing any code. Follow all rules exactly. When in doubt, prefer the more restrictive option. Flag this file for update if you discover new patterns.

**For humans:** Keep this file lean. Update when the tech stack changes. Remove rules that become obvious over time. Review when agents start making repeated mistakes.

---

_Last updated: [date] — [project_name]_
```

### 3.2 Optimize Before Saving

Before writing the file, review the assembled content:
- Remove any redundant or obviously generic rules
- Ensure every rule is **specific and actionable**, not vague
- Keep bullet points concise — one clear idea per line
- The file should be scannable in under 2 minutes

### 3.3 Save and Present

Save the file to `output_file` and present it to the user.

Confirm completion:

> "✅ **Project context saved** to `[output_file]`
>
> **Summary:**
> - [N] critical rules across 7 categories
> - Tech stack documented with exact versions
> - Ready for agent consumption
>
> All skills in this project (research, prd, and implementation agents) will now read this file automatically before starting work. Update it whenever patterns evolve or agents start making repeated mistakes."