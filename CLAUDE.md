# CLAUDE.md — GTM_Agent

Day-to-day operating guide for this directory. `docs/plan.md` is the source of
truth for architecture, scope, and phase history — read it before editing any
agent file, ref file, or YAML.

## Model Delegation Policy (heavy/long-running tasks)

For heavy, long-running implementation tasks in this project, delegate to a more powerful model: **Opus 5 or Fable 5**. Fable 5 has a token cap of **200k tokens** for any single such task — if that cap is reached and the implementation is not yet finished, stop and switch to **Opus 5** to complete the remaining work.

## Start Here (new session)

1. **Read `docs/plan.md` in full** before writing any agent file, ref file, or YAML — it owns architecture, naming, scope, and the full phase record.
2. **Docs convention:** every authored doc for this project lives in `docs/`. Only `README.md` and `CLAUDE.md` stay at the repo root. (Generated guides for *target* projects still write to the target's own root, unchanged.)
3. **Status: fully implemented, all six phases done** — four build phases, a Phase 5 post-review hardening pass, and Phase 6's two new specialists (both 2026-08-29). Orchestrator (`gtm-agent.md`) + **5 specialists** + **8 ref files** (`positioning-methodology.md` and `pricing-and-licensing.md` are the new ones) + 12 `platforms/*.yaml` + `lib/validate_platforms.py` + `README.md` + `docs/HowTo.md` all exist. Combined mode is the default and now runs in **two waves** — Positioning alone first, then Shipping/Distribution/Marketing/Pricing in parallel — stitching one `GTM_GUIDE.md` with five sections; single-guide mode runs one specialist on request; either can run as a refresh of an existing guide. **Three specialists now require live `WebSearch`** (Positioning, Marketing, Pricing), up from one. Phase-by-phase detail and the dogfood results are in `docs/plan.md` §8/§9. **Validated end to end on 2026-08-31** — a combined, two-wave, self-dogfood run against this project succeeded on the first pass with zero fallbacks; see Recent Work (2026-08-31) below.
4. **The six agent files are meant to be symlinked into `/home/vscode/.claude/agents/`** (`Dev_Agents/CLAUDE.md` rule 9). **On this machine that directory does not currently exist — the symlinks are missing** (surfaced by the 2026-08-31 dogfood run; the earlier "all six symlinked, verified with `readlink -f`" claim here and in `docs/plan.md` was wrong). The named subagent types still resolve via project-level discovery while a session's cwd is inside this repo, so combined mode runs; the symlinks only matter for invoking `@gtm-agent` from *other* projects on this machine. Re-create them, then verify with `readlink -f`:
   ```bash
   mkdir -p /home/vscode/.claude/agents
   ln -sf /workspaces/Prj_utils/Dev_Agents/GTM_Agent/.claude/agents/<name>.md /home/vscode/.claude/agents/<name>.md
   ```
5. **Harness quirk:** a registered subagent type does not hot-reload its `.md` after an in-session edit (it once served a stale pre-Phase-4 copy and wrongly refused combined mode). To test a just-edited agent file in the same session, use a fresh general-purpose agent told to re-read it from disk — not the named subagent type.

## Recent Work (2026-08-31)

- **First real end-to-end run — SUCCESS.** `@gtm-agent` was run in combined mode
  (fresh, two waves) as a self-dogfood against this project, writing
  `docs/GTM_GUIDE.md` (470 lines, overwriting the prior dogfood output). **All
  five specialists returned on the first invocation — zero retries, zero Critical
  Rule 8 fallbacks, no "Generation notes" footer.** The two things `docs/plan.md`
  flagged three times as unvalidated — **two-wave execution** and the
  **Wave 1 → Wave 2 positioning-context handoff** — both worked. Classification
  came out `AI agent` / `Claude Code agent` / `functional, untested-in-production`.
  The Step 6 self-check against `refs/guide-quality-checklist.md` passed on every
  applicable list. Also run earlier the same day against `control-center` (an
  external project) via a manual application of the methodology, not the
  orchestrator — the orchestrator run recorded here is the real test.
- **Still untested: the failure path.** Nothing failed, so Critical Rule 8's
  retry → ref-file fallback → footer-disclosure chain remains unexercised by a
  real run. `docs/HowTo.md` Part 6 still has the steps to force it deliberately;
  do that next if the failure contract needs real coverage.
- **The dogfood run surfaced three genuine issues in this project** (the same
  "docs claim more than git ships" pattern the Phase 4 portfolio pass found —
  `Dev_Agents/CLAUDE.md` "GTM_Agent — Complete"):
  1. **Name collision — the headline finding.** "GTM agent" is an established
     2026 category label for sales/outbound-automation tooling (Gartner tracks an
     "AI GTM Platforms" market), and `gtmagents/gtm-agents` — a same-named Claude
     Code agent collection (~96★) — is already on the plugin marketplace this
     project's own `platforms/claude-code-plugin-marketplace.yaml` recommends
     launching on. The name points straight at the one audience this agent has a
     hard rule against serving. `docs/plan.md` §0 only ever justified the name
     against *other agents inside this repo*. Decide the name now, while the repo
     is unpushed and a rename is one find-and-replace. Positioning presented it as
     three options with tradeoffs, not a rename order.
  2. **Symlinks missing** — see the correction in Start Here item 4 above.
  3. **Working tree not shippable** — `git ls-tree -r HEAD` shows HEAD carries
     only 4 of 6 agent files and 5 of 8 ref files; `docs/` and `lib/` are
     untracked entirely; no `LICENSE`, no GitHub remote. A fresh clone cannot run
     combined mode. Four of the guide's five sections independently hit this same
     blocker, which is why `docs/GTM_GUIDE.md` reads more repetitively than a
     normal target's would.
- **`docs/GTM_GUIDE.md` is now the 2026-08-31 orchestrator output**, replacing the
  older hand-verified self-review. It is untracked in git (all of `docs/` is).

## Recent Work (2026-08-29)

- **Phase 6 — the last two review issues closed (3 and 6), taking the agent from
  3 specialists to 5.** New `positioning-specialist.md` (+
  `refs/positioning-methodology.md`) runs **first** in a combined run and
  produces the namespace/collision check, refined one-liner, competitor table
  with a defensible-vs-merely-true call on each differentiator, and the "who this
  is NOT for" boundary. New `pricing-specialist.md` (+
  `refs/pricing-and-licensing.md`) produces the license recommendation,
  free-vs-paid boundary, live-searched comparables, and a concrete
  `PaymentAgent`/`donation-specialist` handoff block. `gtm-agent.md` was reworked
  for **two-wave** combined execution (Wave 1: Positioning alone; Wave 2: the
  other four in one parallel batch, each carrying Positioning's compact context
  block), with Critical Rule 8 extended to cover both new sections and Rule 8.4
  governing what Wave 2 is told when Wave 1 falls back.
  `refs/guide-quality-checklist.md` gained Positioning and Pricing section lists.
  Full record: `docs/plan.md` §8 "Phase 6". **Not yet run end to end** — see the
  harness quirk in Start Here item 5 and `docs/HowTo.md` Part 6.
- **`docs/HowTo.md` rewritten** — stale "three specialists" references fixed
  throughout, Positioning and Pricing subsections added to Part 4, and a new
  **Part 6 — Manual Testing** giving runnable verification steps for every
  capability (there is still no automated end-to-end test).
- **Post-review hardening pass — 6 of the 8 open issues closed** (1, 2, 4, 5, 7,
  8; see "Issues Found" below and `docs/plan.md` §8 "Phase 5"). In short:
  `gtm-agent.md` gained a failure-recovery contract (Critical Rule 8), parallel
  specialist execution, pass-contents-not-paths (Critical Rule 9), a model-tiering
  section, and a refresh mode (Critical Rule 10 + Step 3b); `refs/guide-quality-checklist.md`
  and `lib/validate_platforms.py` are new; `refs/deployment-patterns.md §8` was
  expanded to parity with §9; `refs/pitch-and-outreach.md` gained a search
  budget. Issues 3 (positioning) and 6 (pricing) were deliberately left open.
- **First tooling in this project** — `lib/validate_platforms.py` runs on the
  shared `Dev_Agents/.venv/`; all 12 existing `platforms/*.yaml` passed with no
  file fixes needed. See Environment/Quick Commands below.

## Recent Work (2026-08-27)

- **`docs/` migration** — `plan.md`, `HowTo.md`, `GTM_GUIDE.md` moved to `docs/`; all cross-references in `README.md`, this file, `Dev_Agents/CLAUDE.md`, the agent files, and the ref files updated. Not yet committed.
- **Git initialized** — `git init` (branch `main`) + `.gitignore` that deliberately keeps the shipped `.claude/agents/*.md` tracked (excluding them was `LegalAgent`'s mistake) + initial commit `f3f89c5`. Repo is local-only; no GitHub remote pushed yet.
- **`README.md` refreshed** — status line, Setup/Usage, Project Structure, and Roadmap moved from "planning stage" to Phase 1–4-complete.
- **First external dogfood run** — combined-mode `GTM_GUIDE.md` produced for `A_OpenClaw` (a project *outside* the `Dev_Agents` portfolio). Output was complete and accurate; verified independently (all 8 platform composite scores recomputed, sub-scores checked against YAML, category exclusions confirmed).
- **Design review written** — `docs/design-review-2026-08.md`: gaps, efficiency ideas, and a recommendation on whether 3 guides is the right set.

## Issues Found (see `docs/design-review-2026-08.md` for full detail)

Original numbering from the 2026-08-27 review is kept throughout, so a reference
to "issue 4" means the same thing here, in `docs/plan.md` §8 Phase 5, and in the
review itself.

### Open

All 8 of the 2026-08-27 review's numbered issues are closed — 1, 2, 4, 5, 7 and 8
in Phase 5, and 3 and 6 in Phase 6, both on 2026-08-29. The Phase 5/6
end-to-end-validation caveat is now **partly closed**: the 2026-08-31 dogfood run
(see Recent Work above) exercised two-wave execution and the positioning handoff
for real and both worked. What remains open:

- **Failure-recovery path unexercised.** Critical Rule 8 (retry → ref-file
  fallback → footer disclosure) has still never fired in a real run. Force it via
  `docs/HowTo.md` Part 6 if it needs coverage.
- **No automated test.** `refs/guide-quality-checklist.md` + the manual Part 6
  steps are the only verification; the fixture-based `test/` harness from review
  §2.1 does not exist.
- **This project's own shipping blockers** (from the dogfood run, not agent
  defects): undecided name collision, missing user-level symlinks, and an
  uncommitted / unpushed / unlicensed working tree where HEAD can't run combined
  mode. Detailed in Recent Work (2026-08-31).

The deferred items listed at the end of this section remain deferred; they are
standing scope decisions, not open defects.

### Resolved (2026-08-29)

1. **Combined mode failure-recovery contract** — `gtm-agent.md` Critical Rule 8: retry a failed specialist once → produce that section from its own ref files → disclose it in the `GTM_GUIDE.md` "Generation notes" footer. Wired into Workflow Steps 4 and 5 and the Deliverables template. A fallback Marketing section is explicitly un-searched (Critical Rule 6 still holds).
2. **Guide-quality self-check** — new `refs/guide-quality-checklist.md`, checked by `gtm-agent.md` Step 6 (whole guide) and by each specialist's Report step (its own section only). The minimum-viable form of the harness `docs/plan.md` §7 planned; a fixture-based `test/` directory is still the "better" option named in review §2.1.
3. **Positioning pass** (Phase 6) — new `positioning-specialist.md` + `refs/positioning-methodology.md`, run **first** in a combined run and feeding a compact positioning context block into the other four. Produces the namespace/collision check (live-searched, colliding project named), the refined one-liner shown against the README's current one, a competitor table whose dimensions come from `target_user`, an explicit defensible-vs-merely-true call on every differentiator, and the "who this is NOT for" boundary. A name collision is always a finding with three options, never a rename instruction.
4. **Efficiency pass** — the three specialists now run **in parallel** (one batch of tool calls, `gtm-agent.md` Step 4; safe only because of issue 1); the orchestrator passes input-file **contents** rather than paths (Critical Rule 9, plus each specialist's Inputs table and Step 1); and the run is **model-tiered** via a new "Model tiering" section plus `model:` frontmatter on the three specialists (Sonnet / Sonnet / Opus). Review §3.4's search cap landed too — `refs/pitch-and-outreach.md`'s "Search budget" section, 2 baseline + up to 2 optional.
5. **Platform schema validator** — new `lib/validate_platforms.py`; all 12 existing files pass unmodified. Pointer added to `refs/platform-scoring-methodology.md`'s schema section.
6. **Commercial-model coverage** (Phase 6) — new `pricing-specialist.md` + `refs/pricing-and-licensing.md`, the fifth specialist and the last section of a combined guide. Produces a license recommendation reasoned against the project's own stated goal (with the one tradeoff it accepts, never a mandate), the free-vs-paid/open-core boundary and packaging model, a live-searched comparables table with non-transferable pricing flagged, and a **concrete handoff block** — a filled-in `python PaymentAgent/scaffold.py …` command, or `@payment-setup-agent` when the provider is genuinely undecided, or `@donation-specialist` for a stay-free project. Guide-only: it writes the command, never runs it. Legal/financial matters carry a "confirm with counsel" note attached to the specific recommendation.
7. **`deployment-patterns.md §8` expanded** to parity with §9 — when it applies vs. §9, container image → registry → persistent host (reusing §2's backend row, not re-deriving it), per-environment secrets, health checks/uptime monitoring, and the `CI_CD_agent` pipeline handoff, with `A_OpenClaw` and `CI_CD_agent`'s Flask service as archetypes.
8. **Refresh mode** — `gtm-agent.md` Critical Rule 10 + Workflow Step 3b + a "What changed since `<date>`" Deliverables block; each specialist gained a "Refresh mode" workflow step returning updated content plus its own change list. Marketing always re-runs its live search on a refresh.

Not carried over from the review: §3.5 (`platforms/index.yaml` digest) — marginal at 12 files, and the validator now gives the registry the regression guard that mattered more.

Deferred (revisit only on demonstrated need, per `docs/plan.md §8`): `platforms/*.yaml` category expansion beyond AI-agent/dev-tool once a real SaaS/game/mobile/API fixture appears; the `ContentPost_agent`/`mediaContentAgent` launch-asset handoffs; naming `platforms/claude-code-plugin-marketplace.yaml`'s channel specifically ("Build with Claude", launched 2026-08-23).

## What This Project Is

**GTM Agent (Go-To-Market Agent)** — a document-generation agent that turns a finished or near-finished project into a concrete, prioritized plan for shipping and getting it in front of real users. Given a target project's `README.md`/`plan.md`/`CLAUDE.md` (or any other file the user points it at), combined mode produces one `GTM_GUIDE.md` with five sections:

1. **Positioning** — namespace/collision check, refined one-liner, competitor table with a defensible-vs-merely-true call, "who this is NOT for" boundary.
2. **Shipping Guide** — deployment options + a presentation checklist (README quality, demo video, repo hygiene).
3. **Distribution Guide** — a rated, prioritized, step-by-step list of platforms to launch on.
4. **Marketing Plan** — an ongoing strategy grounded in a live web search for the project's field, plus a pitch/meeting script.
5. **Pricing & Packaging** — license recommendation, free-vs-paid boundary, live-searched comparables, and a concrete `PaymentAgent`/`donation-specialist` handoff.

Any one section can be requested on its own instead. It never deploys, posts, or publishes anything itself — every specialist's output is a Markdown guide for the user to execute. See `docs/plan.md` §1–§4 for the full identity, scope, and non-goals.

## Architecture Summary

Orchestrator (`gtm-agent.md`) + **5 specialists** (`positioning-specialist.md`, `shipping-specialist.md`, `distribution-specialist.md`, `marketing-specialist.md`, `pricing-specialist.md`), matching the `PaymentAgent`/`ContentPost_agent` orchestrator+specialist pattern used elsewhere in this repo.

The architectural departure is live search: **three** of the five specialists need `WebSearch` — Marketing (channel effectiveness and field practice change faster than deployment or platform-submission mechanics), Positioning (namespace status and who actually competes are facts about right now), and Pricing (comparable prices go stale in weeks). Their knowledge is intentionally not baked into static ref files; the ref files own the *method*, the search owns the *substance* (`docs/plan.md` §5, which also covers why `platforms/` here does not duplicate `ContentPost_agent/platforms/`). Shipping and Distribution remain fully static-ref-file-driven.

`gtm-agent.md` defaults to combined mode and runs it in **two waves**: Wave 1 is `positioning-specialist` alone, because positioning is message–market fit and a genuine input to everything after it; Wave 2 is the other four in a single parallel batch, each handed the classification block, the input-file contents, and Positioning's compact **positioning context block** (one-liner, defensible differentiators, "not for" boundary, name-collision finding). The five sections stitch into one `GTM_GUIDE.md` in the order **Positioning → Shipping → Distribution → Marketing → Pricing & Packaging**. A single guide can still be requested, running only that specialist, which writes its own file directly.

## Directory Structure

```
GTM_Agent/
├── CLAUDE.md                   ← this file
├── README.md                   ← user-facing docs
├── docs/                       ← all authored docs (README.md + CLAUDE.md stay at root)
│   ├── plan.md                  ← implementation plan + phase record (read first)
│   ├── HowTo.md                 ← step-by-step usage guide
│   ├── GTM_GUIDE.md             ← GTM_Agent's own dogfood output (2026-08-31 orchestrator run)
│   └── design-review-2026-08.md ← gaps / efficiency / "are 3 guides enough" critique
├── .claude/agents/             ← 6 files
│   ├── gtm-agent.md                 ← orchestrator; two-wave combined mode by default, no forced model
│   ├── positioning-specialist.md    ← Wave 1, runs alone and first; WebSearch; model: opus
│   ├── shipping-specialist.md       ← Wave 2; model: sonnet
│   ├── distribution-specialist.md   ← Wave 2; model: sonnet
│   ├── marketing-specialist.md      ← Wave 2; WebSearch; model: opus
│   └── pricing-specialist.md        ← Wave 2; WebSearch; model: opus
├── lib/
│   └── validate_platforms.py   ← platforms/*.yaml schema validator (shared Dev_Agents/.venv)
├── refs/                       ← 8 files: project-classification, presentation-standards,
│                                  deployment-patterns, platform-scoring-methodology,
│                                  pitch-and-outreach, guide-quality-checklist,
│                                  positioning-methodology, pricing-and-licensing
└── platforms/                  ← 12 files: product-hunt, hacker-news, github-topics,
                                   package-registries, niche-communities, itch-io, steam,
                                   indie-hackers, claude-code-plugin-marketplace,
                                   awesome-lists, app-stores-mobile, devto
```

## Development Rules (specific to this directory)

- **Guides only, never actions.** No specialist may post, deploy, or otherwise act on the user's behalf — output is always a Markdown document. A harder boundary than the usual "review only" agents here, because a launch/marketing agent is unusually tempting to wire up to real posting — don't, without an explicit separate decision.
- **Classify before routing.** Every run starts with project classification (`refs/project-classification.md`) — no specialist generates output before category/stack/maturity is known.
- **Platform rules belong in YAML** (`platforms/*.yaml`), never in prompt strings (`Dev_Agents/CLAUDE.md` rules 5/7).
- **Do not duplicate `ContentPost_agent`'s platform-formatting rules.** `GTM_Agent/platforms/*.yaml` entries carry only launch-strategy fields (category fit, effort/reach rating, prerequisites, submission workflow) — never character limits, hashtag rules, or tone. See `docs/plan.md` §5.
- **Every rated recommendation must show its scoring rationale** (from `refs/platform-scoring-methodology.md`) — a ranked list with no "why" is not acceptable output from `distribution-specialist`.
- **`marketing-specialist` must ground claims in its own live search results**, not generic training-data advice, and must flag field-specific vs. generic tactics.

## Environment

No runtime dependencies **at agent-run time** — every specialist and ref file is Markdown/YAML/live `WebSearch` consumed directly by Claude Code, and a guide can be produced with no Python involved at all.

The one exception is the maintenance tool: `lib/validate_platforms.py` (added 2026-08-29) is the platform-registry validator this section previously anticipated. It runs on the shared **`Dev_Agents/.venv/`** as planned — stdlib plus PyYAML 6.0.3, nothing else — and is a pre-edit/pre-commit guard for `platforms/*.yaml`, not part of any agent's runtime path. Keep it that way: if a future tool needs a dependency the shared venv doesn't have, that's a signal to reconsider the tool, not to give this project its own environment.

## Quick Commands

Guides are produced via Claude Code's agent mechanism, pointing at a target project directory:

```
@gtm-agent produce a full GTM guide for LegalAgent          # default: combined, all 5 sections
@gtm-agent produce a positioning guide for LegalAgent        # single-guide mode
@gtm-agent produce just a shipping guide for LegalAgent
@gtm-agent produce a distribution guide for code-mapper
@gtm-agent produce a marketing plan for PaymentAgent
@gtm-agent produce a pricing guide for mediaContentAgent
@gtm-agent refresh LegalAgent's GTM_GUIDE.md                 # refresh mode — reports what changed
```

The one shell command in this project — run it after editing or adding any `platforms/*.yaml`:

```bash
# Validate the platform registry against refs/platform-scoring-methodology.md's schema
/workspaces/Prj_utils/Dev_Agents/.venv/bin/python lib/validate_platforms.py
/workspaces/Prj_utils/Dev_Agents/.venv/bin/python lib/validate_platforms.py platforms/product-hunt.yaml  # one file
```

Or invoke a specialist directly (always standalone — writes its own file; skips the orchestrator's classification step only if you hand it a classification block):

```
@positioning-specialist ...   @shipping-specialist ...   @distribution-specialist ...
@marketing-specialist ...     @pricing-specialist ...
```

Verifying a change by hand? `docs/HowTo.md` **Part 6 — Manual Testing** has the
runnable steps (what to run → what correct output looks like → what a failure
looks like) for every capability, including how to exercise the failure-recovery
contract deliberately. There is still no automated end-to-end test.

If invoking a named agent right after editing its `.md` file in the same session, re-read Start Here item 5 — a registered subagent type can serve a stale cached copy of its own instructions mid-session.
