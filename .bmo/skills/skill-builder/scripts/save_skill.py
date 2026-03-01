#!/usr/bin/env python3
"""
save_skill.py — BMO Skill Saver

Saves a skill to the correct folder inside the bmo project, following
project conventions defined in .bmo/config.yaml.

Skills are always saved to:
    .bmo/skills/<skill_name>/SKILL.md

Usage:
    python -m scripts.save_skill <skill_name>

Examples:
    python -m scripts.save_skill market-research
    python -m scripts.save_skill summarizer

The script will:
  1. Read .bmo/config.yaml (project_name, communication_language, etc.)
  2. Resolve the skill path as .bmo/skills/<skill_name>/SKILL.md
  3. Validate the SKILL.md (frontmatter + config-loading block)
  4. Print a summary of what was saved
"""

import sys
from pathlib import Path

# ── Optional YAML parser (falls back to manual parsing if PyYAML not installed) ──
try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


# ────────────────────────────────────────────────────────────────────────────────
# Config
# ────────────────────────────────────────────────────────────────────────────────

CONFIG_PATH = Path(".bmo/config.yaml")
SKILLS_ROOT = Path(".bmo/skills")            # all skills live here
CONFIG_LOADING_MARKER = "Load Config"        # string that must appear in SKILL.md


# ────────────────────────────────────────────────────────────────────────────────
# Helpers
# ────────────────────────────────────────────────────────────────────────────────

def load_config() -> dict:
    """Read and parse .bmo/config.yaml. Exits on failure."""
    if not CONFIG_PATH.exists():
        print(
            "⚠️  Config file not found at `.bmo/config.yaml`.\n"
            "   Please create it before running this script.\n"
            "   You can use the config template as a starting point."
        )
        sys.exit(1)

    content = CONFIG_PATH.read_text(encoding="utf-8")

    if HAS_YAML:
        config = yaml.safe_load(content) or {}
    else:
        # Minimal manual YAML parser — handles simple key: value lines only.
        config = {}
        for line in content.splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if ":" in line:
                key, _, value = line.partition(":")
                config[key.strip()] = value.strip().strip('"').strip("'")

    return config


def parse_frontmatter(text: str) -> dict:
    """
    Extract YAML frontmatter from a Markdown file.
    Returns a dict of frontmatter keys, or {} if none found.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}

    fm_lines = []
    for line in lines[1:]:
        if line.strip() == "---":
            break
        fm_lines.append(line)

    fm_text = "\n".join(fm_lines)

    if HAS_YAML:
        try:
            return yaml.safe_load(fm_text) or {}
        except yaml.YAMLError:
            return {}
    else:
        result = {}
        for line in fm_lines:
            if ":" in line:
                key, _, value = line.partition(":")
                result[key.strip()] = value.strip().strip('"').strip("'")
        return result


def validate_skill(skill_md_path: Path) -> list[str]:
    """
    Validate a SKILL.md file. Returns a list of error strings (empty = valid).
    Checks:
      - File exists and is readable
      - YAML frontmatter is present with 'name' and 'description'
      - Config-loading block is present
    """
    errors = []

    if not skill_md_path.exists():
        errors.append(f"File not found: {skill_md_path}")
        return errors  # Nothing else to check

    text = skill_md_path.read_text(encoding="utf-8")

    # ── Frontmatter ──────────────────────────────────────────────────────────
    fm = parse_frontmatter(text)

    if not fm:
        errors.append("Missing YAML frontmatter (file must start with ---)")
    else:
        if not fm.get("name", "").strip():
            errors.append("Frontmatter is missing 'name' field")
        if not fm.get("description", "").strip():
            errors.append("Frontmatter is missing 'description' field")

    # ── Config-loading block ─────────────────────────────────────────────────
    if CONFIG_LOADING_MARKER not in text:
        errors.append(
            f"Missing config-loading block — SKILL.md must contain "
            f"a section with '{CONFIG_LOADING_MARKER}' "
            f"(see references/config-convention.md)"
        )

    return errors


# ────────────────────────────────────────────────────────────────────────────────
# Main
# ────────────────────────────────────────────────────────────────────────────────

def main():
    # ── Args ─────────────────────────────────────────────────────────────────
    if len(sys.argv) != 2:
        print("Usage: python -m scripts.save_skill <skill_name>")
        print()
        print("Examples:")
        print("  python -m scripts.save_skill market-research")
        print("  python -m scripts.save_skill summarizer")
        sys.exit(1)

    skill_name = sys.argv[1].strip().lower()
    source_skill_md = SKILLS_ROOT / skill_name / "SKILL.md"

    print(f"\n📦 BMO Skill Saver")
    print(f"   Skill name : {skill_name}")
    print(f"   Path       : {source_skill_md}")
    print()

    # ── Load config ───────────────────────────────────────────────────────────
    config = load_config()
    print(f"✅ Config loaded from {CONFIG_PATH}")
    print(f"   Skills root       : {SKILLS_ROOT}")
    print(f"   Project           : {config.get('project_name', '(not set)')}")
    print(f"   Comm. language    : {config.get('communication_language', '(not set)')}")
    print(f"   Doc language      : {config.get('document_output_language', '(not set)')}")
    print()

    # ── Validate ──────────────────────────────────────────────────────────────
    print("🔍 Validating SKILL.md...")
    errors = validate_skill(source_skill_md)
    if errors:
        print("❌ Validation failed:")
        for err in errors:
            print(f"   • {err}")
        print()
        print("   Fix the issues above and try again.")
        sys.exit(1)
    print("✅ Validation passed\n")

    # ── Summary ───────────────────────────────────────────────────────────────
    dest_dir = SKILLS_ROOT / skill_name
    saved_files = [source_skill_md]

    references_dir = dest_dir / "references"
    if references_dir.exists() and references_dir.is_dir():
        for f in references_dir.rglob("*"):
            if f.is_file():
                saved_files.append(f)

    print(f"✅ Skill '{skill_name}' is ready!")
    print(f"   Location: {dest_dir}")
    print()
    print("   Files:")
    for f in saved_files:
        rel = f.relative_to(Path.cwd()) if f.is_relative_to(Path.cwd()) else f
        print(f"   • {rel}")
    print()
    print(f"🎉 Done! Your skill is ready at: {dest_dir / 'SKILL.md'}")
    print()


if __name__ == "__main__":
    main()