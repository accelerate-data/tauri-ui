# Tauri UI Plugin

Shared plugin repository for project-agnostic Tauri app building and debugging guidance used by Claude Code and Codex.

**Maintenance rule:** This file contains durable repository guidance, not volatile inventory.

## Instruction Hierarchy

1. `AGENTS.md` - canonical, cross-agent source of truth
2. Skill-local references under `skills/<skill>/references/`
3. `CLAUDE.md` - Claude-specific adapter and routing

## Repository Purpose

Single plugin-source repo for Tauri app skills.

- Root manifests: `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json`
- Canonical skill content: `skills/`
- Rules: `rules/`

## Skills

- `skills/tauri/SKILL.md` - Tauri desktop app framework, frontend IPC, capabilities, plugins, sidecars, and distribution

## Rules

Always-on coding standards in `rules/` covering naming conventions, logging policy, execution policy, and schema changes.

## Conventions

- Keep all skill directories under `skills/`.
- Keep all rule files under `rules/`.
- Keep `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json` on the same plugin name and version.
- When plugin content or metadata changes, bump both manifest versions together and run `python3 scripts/validate_plugin_manifests.py`.
