# Config Loading Convention
# ─────────────────────────────────────────────────────────────
# This block is embedded in every skill. It defines how skills
# discover and apply the shared project config.
# ─────────────────────────────────────────────────────────────

## Loading the Config

At the very start of any skill, before doing anything else:

1. Look for `.bmo/config.yaml`.
2. **If the file is missing: stop immediately and warn the user.**
   > "⚠️ Config file not found at `.bmo/config.yaml`. Please create it before running this skill. You can use the config template as a starting point."
3. If found, read and resolve these values:

| Config Key                  | Used for                                              |
|-----------------------------|-------------------------------------------------------|
| `project_name`              | Personalizing output filenames and document titles    |
| `output_folder`             | Where to save all output files                        |
| `communication_language`    | The language Claude speaks to the user in             |
| `document_output_language`  | The language used inside generated documents          |

## Output File Naming

Use this pattern for all skill output files:

```
{output_folder}/{skill-name}/{topic-slug}-{YYYY-MM-DD}.md
```

Example: `.bmo/_output/research/ev-europe-2025-03-14.md`

## Project Context

After loading the config, read `{output_folder}/project-context.md` to understand the project's background, goals, and any relevant details that should inform the skill's output.

- **If the file is missing**: warn the user and continue.
  > "⚠️ Project context file not found at `{output_folder}/project-context.md`. Continuing without it — consider creating it for better results."
- **If found**: read it fully before proceeding. Use it to personalize and ground all outputs.

## Language Behavior

- Speak to the user in `communication_language` throughout.
- Write all document content (headings, body, summaries) in `document_output_language`.
- If both are the same (the common case), no special handling needed.