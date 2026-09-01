# Project Classification

Defines how `gtm-agent.md` infers a target project's **category, stack, maturity
stage, and target user** from its docs before routing to any specialist. This is
the first step of every run (`CLAUDE.md` rule "Classify before routing") — a
`shipping-specialist` cannot recommend a deploy path, and a `distribution-specialist`
cannot rate a platform, for a project it hasn't identified yet.

Load this file when: starting a new run, right after reading the target project's
input files and before calling any specialist.

## Inputs to read

Default input set (mirrors `docs/plan.md §1`):

- `README.md`, `plan.md`, `CLAUDE.md` at the target project's root.
- If the user points the agent at other files instead (a pitch deck, a spec, a
  landing-page draft), read those in place of — not in addition to — the defaults,
  but still apply the same four dimensions below.
- **If the named triad isn't fully present, don't stop at "input is thin"
  before checking for substitutes.** Several real `Dev_Agents` projects use
  different filenames for the same role — e.g. `PaymentAgent` has no
  `README.md`/`CLAUDE.md` at all, only `payment_guide.md` (overview/analysis)
  and `HowTo.md` (usage guide). Read whichever root-level `.md` files are
  functioning as the overview and usage-guide role before treating the project
  as low-confidence input — reserve that judgment for when no such files exist
  at all, not merely when they're not named `README.md`/`plan.md`/`CLAUDE.md`.
  Record which files actually served each role in `source_files`.

Secondary signals, read only if present, to corroborate or resolve ambiguity in the
above (do not require these — thin projects may have none):

- Manifest files: `package.json`, `pyproject.toml`, `requirements.txt`,
  `Cargo.toml`, `go.mod`, `Gemfile`.
- Deploy/infra hints: `Dockerfile`, `docker-compose.yml`, `vercel.json`,
  `netlify.toml`, `.github/workflows/*.yml`.
- `.claude/agents/*.md` or a `.claude/skills/` directory — strong signal the
  project itself *is* a Claude Code agent/skill, not software with a traditional
  runtime (see the "Claude Code agent project" note under Stack below).
- `tests/` or `test/` directory, and whether a test count/pass status is stated in
  the docs (e.g. "44 passing tests").
- `LICENSE` file.

If none of the default files exist or they are too thin to classify confidently
(see "Low-confidence input" under Edge Cases), say so and ask the user for more
input rather than guessing.

## Dimension 1: Category

Pick one **primary** category from the fixed list below (kept identical to
`docs/plan.md §5` so specialist prompts and `platforms/*.yaml` category-fit fields stay
in sync). A project may also carry one **secondary** tag when it genuinely spans
two — see Edge Cases.

- **dev tool / library** — used by other developers inside their own code or
  workflow (a CLI utility, a code generator, a linter, an SDK). Signal: README
  leads with an install command and API/usage examples aimed at developers.
- **SaaS / web app** — a hosted product end users log into. Signal: mentions of
  accounts, subscriptions, a frontend framework, a hosted URL, or billing.
- **CLI** — primary interface is a terminal command, not a library import or a
  web UI. Signal: README's main usage example is a shell invocation.
- **game** — signal: mentions of a game engine (Unity, Unreal, Godot), players,
  levels, or a storefront target (Steam, itch.io).
- **mobile app** — signal: mentions of iOS/Android, an app store listing, React
  Native/Flutter/Swift/Kotlin.
- **API** — a service consumed programmatically by other software, not a human
  UI. Signal: README documents endpoints/request-response shapes rather than
  screens or commands.
- **content / creative tool** — produces media (images, video, audio, text) as
  its output. Signal: mentions of generation, rendering, or export formats as the
  core value, not developer tooling.
- **AI agent** — an LLM-driven agent or agent definition, including a Claude Code
  subagent. Signal: `.claude/agents/*.md` present, or the README describes
  "an agent that…" rather than a library/app a human operates directly.

This repo's own agents are convenient concrete examples: `LegalAgent` and
`PaymentAgent` are **AI agent** (each ships as Claude Code subagent `.md` files +
YAML registries, not a running service); `code-mapper` is **dev tool / library**
(a standalone Python script other developers run against their own codebase)
with an **AI agent** secondary tag (its README documents an optional Claude
Code agent companion — `agent.md` — alongside the standalone script, so it's a
dual-artifact project the same way `deployment-patterns.md §9`'s dual-artifact
guidance describes: two independent things to ship, not two readings of one
category); `CI_CD_agent` is **AI agent** with a **dev tool** secondary tag (it's
a reasoning layer, but it also runs as a webhook server other tooling calls).

Getting a secondary tag right matters beyond classification itself: a
downstream specialist like `distribution-specialist` matches
`platforms/*.yaml` entries against primary *or* secondary category — missing a
real secondary tag (e.g. treating `code-mapper` as dev-tool-only) silently
drops a real channel (there, `claude-code-plugin-marketplace.yaml` would never
surface) rather than just under-describing the project.

## Dimension 2: Stack

Identify language(s), framework(s), and runtime from manifest files and docs.
Report what's actually there — do not infer a stack the project doesn't show
evidence of.

**Special case — Claude Code agent project.** Most of this repo's own agents (and
likely many targets this tool will be run against, since it's dogfooded on
`Dev_Agents` itself) have no traditional runtime at all: the "stack" is Claude
Code subagent `.md` definitions, optional `refs/*.md` knowledge files, optional
`platforms/*.yaml` or `providers/*.yaml` registries, and occasionally a thin
Python CLI (e.g. `scaffold.py`, `validate_report.py`) with no server component.
Classify this explicitly as **stack: Claude Code agent (.md definitions + refs +
YAML/Python helpers, no hosted runtime)** rather than forcing it into a
language/framework slot — this distinction matters directly to
`shipping-specialist`, whose deployment options differ completely for "runs as a
hosted service" versus "runs as a Claude Code subagent invoked locally or
symlinked into the personal tier."

## Dimension 3: Maturity Stage

Pick one stage. Prefer the project's own stated status over inference — most
`Dev_Agents` projects state this explicitly (a `## Status` line, a status column
in a parent `CLAUDE.md` table, or "Phase N complete" language in `plan.md`).

- **planning-only** — a `plan.md`/spec exists but no agent files, source, or
  templates have been written yet. Signal: "planning complete," "not started,"
  or a directory containing only docs.
- **in-development / partial** — some phases or components are built, others
  are explicitly marked pending. Signal: a phase table with mixed
  complete/pending rows, or "Tier 2 and 3 implemented but not yet tested."
- **functional / untested-in-production** — the full described scope is built
  and internally exercised (unit tests passing, smoke-tested) but not yet
  validated against real-world use or a real external dependency. Signal:
  "implemented + smoke-tested against a fake server, not yet tested against a
  real instance," or "awaiting testing."
- **shipped / production-ready** — complete, tested, and the docs describe it as
  ready to use or ship as-is, with no open phase blocking that claim.

Do not round up: a project whose docs say "awaiting testing" is
**functional / untested-in-production**, not shipped, even if every planned
feature is implemented — `shipping-specialist` needs to know testing is the
actual next step, not deployment.

## Dimension 4: Target User

Pull this from the project's own stated audience wherever possible — most
`plan.md`/README files in this repo have an explicit "Who uses this" or "Why
this matters" section. Where it's not explicit, infer narrowly from the category
and stack (e.g. a CLI dev tool with no billing or account system implies
"individual developers," not "enterprise buyers") rather than defaulting to a
generic "everyone" answer, which gives `distribution-specialist` nothing to
rate platform fit against.

## Output format

Emit a short classification block before calling any specialist, so every
specialist consumes the same facts instead of re-deriving them:

```
category: <primary> [(secondary: <secondary>)]
stack: <languages/frameworks/runtime, or the Claude Code agent special case>
maturity: <planning-only | in-development/partial | functional/untested | shipped>
target_user: <one line>
source_files: <which files were actually read>
confidence_notes: <any ambiguity, thin input, or assumption made — omit if none>
```

## Edge Cases

- **Multi-category projects.** Assign the category the project's *primary* value
  proposition matches (what a user would say it *is*), and add a secondary tag
  only when a specialist's recommendations would genuinely differ because of the
  second facet (e.g. `CI_CD_agent`'s "dev tool" secondary tag matters because it
  changes deployment options — a webhook server needs hosting, a pure agent
  definition doesn't). Don't add a secondary tag just because a project touches
  another domain in passing.
- **Claude Code agent projects specifically.** Since this repo's own agents are
  the primary test fixtures for Phase 1 acceptance (`docs/plan.md §9`), do not default
  their maturity or deployment framing to "it needs a hosting provider" — see the
  Stack special case above. Their "shipping" story is usually: register the
  agent file (symlink into `/home/vscode/.claude/agents/` per `Dev_Agents/CLAUDE.md`
  rule 9's convention), not deploy a server.
- **Low-confidence input.** If the default files are missing, contradictory, or
  too thin to fill in a dimension (e.g. no stated audience anywhere and the
  category doesn't imply one), state the gap in `confidence_notes` and ask the
  user for clarification rather than inventing specifics that later guides would
  present as fact.

## Worked example

`LegalAgent/CLAUDE.md` + `plan.md` read together:

```
category: AI agent
stack: Claude Code agent (.md definition + refs/*.md + clause-libraries/*.yaml +
  lib/*.py validation helpers, no hosted runtime)
maturity: functional/untested — Phase 1+2 complete, Phase 3 UK/EU primer complete,
  44 passing tests exist but no stated real-world/production use yet
target_user: individuals/teams needing a first-pass contract risk review
  (NDA/MSA/contractor/employment/ToS/privacy policy) without hiring counsel for
  routine review
source_files: LegalAgent/CLAUDE.md, LegalAgent/plan.md
confidence_notes: none
```
