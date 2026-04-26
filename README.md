# Tauri UI Skill

Shared Claude/Codex plugin source for building Tauri apps. The current plugin
ships one project-agnostic Tauri skill plus always-on coding rules.

## What The Tauri Skill Covers

The `tauri` skill is for agents building or debugging apps that use
`src-tauri`, `tauri.conf.*`, Rust commands, `invoke`, events,
`@tauri-apps/api`, capabilities, permissions, plugins, sidecars, WebView2,
signing, updater, mobile, build, bundle, or desktop distribution.

It is intentionally project-agnostic. Agents are told to inspect the target
app's existing package manager, frontend framework, scripts, versions,
capabilities, command modules, IPC wrappers, state, and tests before editing.

Skill contents:

- [skills/tauri/SKILL.md](skills/tauri/SKILL.md) - main routing guide with the
  first-inspect checklist, official documentation map, command quick reference,
  and app-building practices.
- [skills/tauri/references/app-building-links.md](skills/tauri/references/app-building-links.md) -
  categorized official Tauri links for setup, frontend APIs, IPC, security,
  plugins, sidecars, distribution, signing, updater, and migration.
- [skills/tauri/references/commands.md](skills/tauri/references/commands.md) -
  Tauri CLI command variants for npm, pnpm, yarn, bun, deno, and cargo, plus
  Rust-side verification commands.
- [skills/tauri/references/security.md](skills/tauri/references/security.md) -
  concise guidance for capabilities, permissions, scopes, CSP, filesystem,
  shell/process access, updater behavior, remote URLs, and sidecars.

The old copied documentation extracts were removed. The skill now links to
official Tauri docs instead of carrying stale or malformed local copies.

## Rules

Always-on coding standards in `rules/` covering naming conventions, logging policy, execution policy, and schema changes.

## Evals

Baseline Promptfoo/OpenCode evals live under `tests/evals/`.

They currently cover:

- Rust command and frontend `invoke` routing.
- Filesystem access with least-privilege capabilities, permissions, and scopes.
- Windows signing and release build guidance.
- Node sidecars without requiring a user-installed runtime.
- Remote asset and IPC security hardening.

Useful eval commands:

```bash
npm --prefix tests/evals run eval:tauri
npm --prefix tests/evals run eval:coverage
npm --prefix tests/evals run eval:codex-compatibility
npm --prefix tests/evals run test:opencode-cli-provider
```

## Install

```bash
claude marketplace add accelerate-data/plugin-marketplace
claude plugin install tauri-ui@plugin-marketplace
```

Codex installs plugins through registered marketplaces:

```bash
codex plugin marketplace add accelerate-data/plugin-marketplace
```

Do not register this plugin source repo directly as a marketplace root.

## Local development

```bash
claude --plugin-dir .      # Load without installing
claude plugin validate .   # Validate structure
python3 scripts/validate_plugin_manifests.py
python3 scripts/check_plugin_version_bump.py --base-ref origin/main
npm --prefix tests/evals run eval:coverage
npm --prefix tests/evals run eval:codex-compatibility
npm --prefix tests/evals run eval:tauri  # Requires OpenCode auth
npm --prefix tests/evals run test:opencode-cli-provider
codex plugin marketplace --help  # Confirm the local Codex CLI marketplace workflow
```

## Updating the plugin

1. Make your changes to skills, commands, or rules
2. Bump `version` in both `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json` to the same value
3. Validate: `python3 scripts/validate_plugin_manifests.py`
4. Check the shared version bump: `python3 scripts/check_plugin_version_bump.py --base-ref origin/main`
5. Run deterministic eval checks: `npm --prefix tests/evals run eval:coverage` and `npm --prefix tests/evals run eval:codex-compatibility`
6. Run the Tauri skill eval when OpenCode auth is available: `npm --prefix tests/evals run eval:tauri`
7. Run the OpenCode provider unit test: `npm --prefix tests/evals run test:opencode-cli-provider`
8. Validate in Claude: `claude plugin validate .`
9. Test locally in Claude: `claude --plugin-dir .`
10. Confirm the local Codex CLI marketplace workflow: `codex plugin marketplace --help`
11. Commit and push — the marketplaces pick up the latest default branch automatically
12. After merge, verify from the marketplace repo that references this plugin source
