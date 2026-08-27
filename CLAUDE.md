# CLAUDE.md — GTM_Agent

This file provides guidance to Claude Code when working in this directory.

## Model Delegation Policy (heavy/long-running tasks)

For heavy, long-running implementation tasks in this project, delegate to a more powerful model: **Opus 5 or Fable 5**. Fable 5 has a token cap of **200k tokens** for any single such task — if that cap is reached and the implementation is not yet finished, stop and switch to **Opus 5** to complete the remaining work.

## Start Here (new session)

1. **Read `plan.md` in full before writing any agent file, ref file, or YAML.** It is the source of truth for architecture, naming, scope, and phase order — this file is only the day-to-day operating guide.
2. **Status: fully implemented — all four phases done.**
   - **Phase 1** — `gtm-agent.md` orchestrator (classification + routing) + `shipping-specialist.md` + the three core ref files (`project-classification.md`, `presentation-standards.md`, `deployment-patterns.md`). Produces `SHIPPING_GUIDE.md`.
   - **Phase 2** — `distribution-specialist.md` + `refs/platform-scoring-methodology.md` + a 12-file `platforms/*.yaml` registry spanning all 8 project categories. Produces `DISTRIBUTION_GUIDE.md`.
   - **Phase 3** — `marketing-specialist.md` (the only specialist with live `WebSearch` access) + `refs/pitch-and-outreach.md`. Produces `MARKETING_PLAN.md`, grounded in real search results, never generic advice.
   - **Phase 4** — `gtm-agent.md` gained full combined-mode orchestration (default run stitches all three into one `GTM_GUIDE.md`; single-guide mode still available on request), plus a real, file-writing dogfood pass across 5 portfolio projects (see item 3).
   Every ref file, all 12 `platforms/*.yaml` files, all four agent files, `README.md`, and `HowTo.md` exist.
3. **Every phase was tested against real `Dev_Agents` subdirectories before being called done**, not just written and assumed correct. Phases 1–3: dry run (no files written) against `LegalAgent`, `PaymentAgent`, `code-mapper` — found and fixed 9 real gaps across the three passes (classification-input handling, presentation/git-tracking checks, dual-artifact deployment guidance, secondary-category tagging, prerequisite clarity, "why now" search guidance, claim-scope matching). Phase 4: a real, file-writing run against `LegalAgent`, `CI_CD_agent`, `PaymentAgent`, `mediaContentAgent`, and `GTM_Agent` itself — **zero design gaps found in `gtm-agent.md` or the specialists**; every finding was a genuine issue in the target project (see `plan.md` §8's "Dogfood Pass Results" for the full list, and `Dev_Agents/CLAUDE.md`'s git-hygiene finding for the cross-cutting pattern it surfaced). Full record, including one honestly-flagged unmet acceptance bullet ("4 distinct categories" — this portfolio only has 2), is in `plan.md` §8/§9.
4. **All four agent files are symlinked into `/home/vscode/.claude/agents/`** — verified with `readlink -f`. Repeat the same symlink step for any future new agent file, per `Dev_Agents/CLAUDE.md` rule 9:
   ```bash
   ln -sf /workspaces/Prj_utils/Dev_Agents/GTM_Agent/.claude/agents/<name>.md /home/vscode/.claude/agents/<name>.md
   ```
   Verify with `readlink -f /home/vscode/.claude/agents/<name>.md` — do not assume the symlink command succeeded silently.
5. **Known harness quirk, worth remembering:** a registered subagent type (e.g. invoking `GTM Agent` via the Agent tool by name) does not hot-reload its instructions if the underlying `.md` file is edited later in the same session — it served a stale, pre-Phase-4 cached copy once during this build and incorrectly refused combined mode per rules that no longer existed on disk. If you edit an agent `.md` file and need to immediately test the new behavior in the same session, use a fresh general-purpose agent explicitly told to re-read the file from disk rather than invoking the named subagent type directly.

## Next Steps (nothing blocking — the agent is fully functional)

- ~~**GTM_Agent's own dogfood run found two real gaps in this project itself**: no git repository, and a stale `README.md` status line.~~ **Both fixed 2026-08-27:** `git init` (branch `main`) + `.gitignore` (deliberately does *not* exclude the shipped `.claude/agents/*.md` — that was `LegalAgent`'s mistake) + initial commit; `README.md` status line, Setup/Usage section, Project Structure block, and Roadmap all updated to reflect Phase 1–4-complete status. The repo is local-only — no GitHub remote has been created/pushed yet (do that when the project is ready to be public).
- **Optional accuracy improvement, not currently blocking anything:** `platforms/claude-code-plugin-marketplace.yaml` still describes the channel generically. A real community marketplace ("Build with Claude") launched August 23, 2026 and could be named specifically. Low priority since `marketing-specialist` re-verifies current facts via live search every run regardless of what's cached in the YAML.
- **Deferred by explicit Phase 4 decision — revisit only if real usage demonstrates a need, not speculatively** (`plan.md` §8): expanding `platforms/*.yaml` coverage once a genuinely new project category (SaaS/game/mobile/API) appears in the portfolio as a real fixture; reconsidering the `ContentPost_agent` JSON-handoff for `marketing-specialist` if a user is ever observed manually retyping `MARKETING_PLAN.md` content into `content-router` prompts.

## What This Project Is

**GTM Agent (Go-To-Market Agent)** — a document-generation agent that turns a finished or near-finished project into a concrete, prioritized plan for shipping and getting it in front of real users. Given a target project's `README.md`/`plan.md`/`CLAUDE.md` (or any other file the user points it at), it produces up to three guides:

1. **Shipping Guide** — deployment options + a presentation checklist (README quality, demo video, repo hygiene).
2. **Distribution Guide** — a rated, prioritized, step-by-step list of platforms to launch on.
3. **Marketing Plan** — an ongoing strategy grounded in a live web search for the project's field, plus a pitch/meeting script.

It never deploys, posts, or publishes anything itself — every specialist's output is a Markdown guide for the user to execute. See `plan.md` §1–§4 for the full identity, scope, and non-goals.

## Architecture Summary

Orchestrator (`gtm-agent.md`) + 3 specialists (`shipping-specialist.md`, `distribution-specialist.md`, `marketing-specialist.md`), matching the `PaymentAgent`/`ContentPost_agent` orchestrator+specialist pattern already used in this repo. The one architectural departure from the rest of `Dev_Agents`: `marketing-specialist.md` is the only specialist that needs live `WebSearch` tool access — its knowledge is intentionally not fully baked into static ref files, because marketing-channel effectiveness changes faster than deployment or platform-submission mechanics do. See `plan.md` §5 for the full reasoning, including why `platforms/` here does not duplicate `ContentPost_agent/platforms/`. `gtm-agent.md` defaults to combined mode (runs all three specialists, stitches one `GTM_GUIDE.md`); a single guide can still be requested, in which case only that one specialist runs and writes its own file directly, unchanged from Phases 1–3.

## Directory Structure (see `plan.md` §5 for the full target tree)

```
GTM_Agent/
├── CLAUDE.md                   ← this file
├── plan.md                     ← implementation plan (read first)
├── README.md                   ← user-facing docs (status line is stale — see Next Steps)
├── HowTo.md                    ← step-by-step usage guide, done
├── GTM_GUIDE.md                 ← GTM_Agent's own real dogfood output (Phase 4) — a genuine self-review, not a demo file
├── .claude/agents/
│   ├── gtm-agent.md                 ← orchestrator, done — defaults to combined mode, all 3 specialists below
│   ├── shipping-specialist.md       ← done
│   ├── distribution-specialist.md   ← done
│   └── marketing-specialist.md      ← done (the only specialist with WebSearch access)
├── refs/
│   ├── project-classification.md       ← done
│   ├── presentation-standards.md       ← done
│   ├── deployment-patterns.md          ← done
│   ├── platform-scoring-methodology.md ← done
│   └── pitch-and-outreach.md           ← done
└── platforms/                   ← 12 files, done: product-hunt, hacker-news,
                                     github-topics, package-registries, niche-communities,
                                     itch-io, steam, indie-hackers,
                                     claude-code-plugin-marketplace, awesome-lists,
                                     app-stores-mobile, devto
```

## Development Rules (specific to this directory)

- **Guides only, never actions.** No specialist may post, deploy, or otherwise act on the user's behalf — output is always a Markdown document. This is a harder boundary here than the usual "review only" agents in this repo, because a launch/marketing agent is unusually tempting to wire up to real posting — do not do it without an explicit, separate decision.
- **Classify before routing.** Every run starts with project classification (`refs/project-classification.md`) — no specialist should generate output before the target project's category/stack/maturity is known.
- **Platform rules belong in YAML** (`platforms/*.yaml`), never in prompt strings — same rule as `ContentPost_agent`/`PaymentAgent` (`Dev_Agents/CLAUDE.md` rules 5/7).
- **Do not duplicate `ContentPost_agent`'s platform-formatting rules.** `GTM_Agent/platforms/*.yaml` entries carry only launch-strategy fields (category fit, effort/reach rating, prerequisites, submission workflow) — never character limits, hashtag rules, or tone. See `plan.md` §5 for the full boundary and the deferred Phase 4 handoff to `ContentPost_agent`.
- **Every rated recommendation must show its scoring rationale** (from `refs/platform-scoring-methodology.md`) — a ranked list with no "why" is not an acceptable output from `distribution-specialist`.
- **`marketing-specialist` must ground claims in its own live search results**, not generic training-data marketing advice, and should flag when a tactic is field-specific versus generic.

## Environment

- No runtime dependencies. Every specialist and ref file is Markdown/YAML/live `WebSearch` consumed directly by Claude Code — no Python/venv needed. Revisit only if a future platform-registry tool needs one; default to the shared `Dev_Agents/.venv/` if so.

## Quick Commands

No standalone CLI — invoke via Claude Code's agent mechanism, pointing at a target project directory:

```
@gtm-agent produce a full GTM guide for LegalAgent          # default: combined GTM_GUIDE.md
@gtm-agent produce just a shipping guide for LegalAgent      # single-guide mode
@gtm-agent produce a distribution guide for code-mapper
@gtm-agent produce a marketing plan for PaymentAgent
```

Or invoke a specialist directly (skips the orchestrator's classification step
only if you already have a classification block to hand it — this always runs
in standalone mode, writing that specialist's own file):

```
@shipping-specialist ...
@distribution-specialist ...
@marketing-specialist ...
```

If invoking a named agent right after editing its `.md` file in the same
session, re-read Start Here item 5 first — a registered subagent type can
serve a stale cached copy of its own instructions mid-session.
