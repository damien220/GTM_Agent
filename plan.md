# Plan — GTM Agent (Go-To-Market Agent)

## Status

**All four phases complete** (§8 below). All ref files, all 12
`platforms/*.yaml` files, and all four agent files exist; all four are
symlinked into `/home/vscode/.claude/agents/` per `Dev_Agents/CLAUDE.md` rule
9. `gtm-agent.md` now defaults to combined mode (one stitched `GTM_GUIDE.md`
per run) with single-guide mode still available on request. The real (non-dry-
run) dogfood pass is done: `GTM_GUIDE.md` now exists in `LegalAgent/`,
`CI_CD_agent/`, `PaymentAgent/`, `mediaContentAgent/`, and `GTM_Agent/` itself
— see the Dogfood Pass Results entry under §8 for what each run found.

## 0. Naming

Directory/agent name: **GTM_Agent** (Go-To-Market Agent). Chosen over the original working name `Delivery_Agent` because "delivery" already means something specific in this repo — `CI_CD_agent` owns continuous *delivery* (build → test → deploy pipelines). "GTM" (go-to-market) is the actual industry term for "how do I ship, list, and sell/announce a finished project," and does not collide with any existing agent's naming.

## 1. What This Agent Is

A **document-generation agent** that turns a finished (or near-finished) project into a concrete, prioritized plan for getting it in front of the people who'd use, test, fund, or buy it. It does not write code, deploy anything, or post anything itself — it writes **guides**, the same way LegalAgent writes a risk report and CI_CD_agent writes release notes.

Input: `README.md`, `plan.md`, `CLAUDE.md` of a target project by default, or any other file(s) the user points it at (a pitch deck, an existing landing page draft, a spec). From these it infers what the project *is* (stack, maturity, category/field, target user) and produces three guides:

1. **Shipping Guide** — deployment options for the detected stack, a presentation checklist (README quality bar, demo video, screenshots/GIFs, optional landing page), and repo hygiene (VCS setup, license, topics/tags).
2. **Distribution Guide** — a step-by-step, **rated and prioritized** list of where to list/launch the project (dev communities, marketplaces, aggregators, forums specific to its field) so it reaches real users/testers/communities.
3. **Marketing Plan** — an ongoing strategy (social cadence, trust-building, outreach) informed by a **live web search** for current best practices in the project's specific field, plus a written pitch/meeting script aimed at convincing a buyer, backer, or early adopter.

## 2. Why This Matters / Who Uses It

Every project in `Dev_Agents` (and every project this portfolio's future buyers build) eventually needs to ship and be seen — that need is universal in a way no single vertical agent's market is. It also has direct internal value: this agent can be dogfooded on `Dev_Agents`' own agents (CI_CD_agent, LegalAgent, PaymentAgent, mediaContentAgent) to produce their actual launch guides, per `Dev_Agents/plan.md` §5 ("Write a real README" / "The README is the product page").

Users: solo developers and small teams who built something and don't know how to get it noticed; this repo's own maintainer, as a capstone step after each agent reaches a shippable phase.

## 3. Scope — Phase 1

Phase 1 ships the orchestrator, project classification, and the **Shipping Guide** specialist only, against static ref-file knowledge (no live web search yet). See §8.

## 4. Non-Goals (all phases unless stated otherwise)

- **Does not generate images, video, or website code.** It writes briefs/scripts for a demo video or landing page — production is left to the user or to `mediaContentAgent`/a design tool.
- **Does not post or publish anything.** Output is a Markdown guide, not an automated posting action. (Future integration point, not Phase 1–4 scope: handing a drafted post off to `ContentPost_agent`'s social-media-specialist, contract-only, no shared code — mirrors the existing `mediaContentAgent → ProdReel` pattern.)
- **Not a hosting provider or deploy tool.** It recommends deployment targets/steps; it does not run `terraform apply` or push to a host.
- **Not legal, financial, or PR counsel.** Trust-building and pitch-script guidance is tactical, not a substitute for legal/financial review — same disclaimer posture as `LegalAgent`'s UPL policy, adapted.

## 5. Architecture

### Why orchestrator + specialists, not one agent

The three guides need genuinely different knowledge (deployment mechanics vs. a rated platform registry vs. live-researched marketing tactics) and, critically, different **tool access** — the marketing specialist needs live `WebSearch`, the other two do not. Splitting them mirrors `PaymentAgent` (orchestrator + per-provider specialists) and `ContentPost_agent` (content-router + specialists), both established patterns in this repo.

```
GTM_Agent/
├── README.md                        ← user-facing docs (usage, setup, examples)
├── plan.md                          ← this file
├── CLAUDE.md                        ← guidance for Claude Code working in this directory
├── HowTo.md                         ← step-by-step usage guide (matches LegalAgent/PaymentAgent convention)
├── .claude/agents/
│   ├── gtm-agent.md                 ← orchestrator: classifies the project, delegates to specialists, stitches output
│   ├── shipping-specialist.md       ← Phase 1
│   ├── distribution-specialist.md   ← Phase 2
│   └── marketing-specialist.md      ← Phase 3 (only specialist with WebSearch tool access)
├── refs/
│   ├── project-classification.md    ← how to infer category/field/stack/maturity from input files
│   ├── presentation-standards.md    ← README/demo-video/landing-page quality bar
│   ├── deployment-patterns.md       ← common deploy paths by stack/project type
│   ├── platform-scoring-methodology.md  ← rubric: reach, effort, audience fit, prerequisites/sequencing
│   └── pitch-and-outreach.md        ← trust-building tactics, meeting/pitch script structure
└── platforms/                       ← YAML registry, one file per distribution platform (ContentPost_agent pattern)
    ├── product-hunt.yaml
    ├── hacker-news.yaml
    ├── github-topics.yaml
    ├── package-registries.yaml      ← npm / PyPI / crates.io, etc. (field-conditional)
    ├── niche-communities.yaml       ← Reddit/Discord/forums, tagged by category
    └── ...                         ← additive; new platform = new YAML file, no code change
```

### Orchestrator workflow (`gtm-agent.md`)

1. Read the input file(s) (default: target project's `README.md`, `plan.md`, `CLAUDE.md`; or user-specified paths).
2. Classify the project using `refs/project-classification.md`: category (dev tool/library, SaaS/web app, CLI, game, mobile app, API, content/creative tool, AI agent), stack, maturity stage, target user.
3. Route to the requested specialist(s) — default is all three, producing a combined `GTM_GUIDE.md` with three sections; a user can ask for just one (e.g. "just the distribution guide").
4. Each specialist returns its guide section; the orchestrator stitches and writes the final Markdown output.

### `platforms/` scope vs. `ContentPost_agent/platforms/` — no overlap in what's stored

Both directories are YAML-per-platform registries, and a few platform names appear in both (Twitter/X, LinkedIn, Reddit, Hacker News) — worth stating explicitly why this is not duplication:

- **`ContentPost_agent/platforms/*.yaml` answers "how do I format a valid post for this platform?"** — character limits, hashtag rules, tone, media specs. It has no concept of a project, a launch sequence, or whether a platform is worth using at all.
- **`GTM_Agent/platforms/*.yaml` answers "should I use this platform for *this* project, and when in my launch sequence?"** — category fit, effort/reach ratings, prerequisites (e.g. "get 3 testimonials before submitting to Product Hunt"), account-setup/submission workflow. It carries zero post-formatting rules.
- Most of `GTM_Agent`'s platform set (Product Hunt, npm/PyPI, itch.io, GitHub Topics, niche communities) doesn't exist in `ContentPost_agent` at all — those are discovery/launch platforms, not social-content platforms — so calling `content-router` for a GTM task would return nothing for most of what the Distribution Guide needs to cover.
- For the few platforms that genuinely are both (X, LinkedIn, Reddit, HN): `GTM_Agent`'s entry for that platform stores only the launch-strategy fields above, never formatting rules. When the Distribution or Marketing guide reaches the point of "now draft the actual post," it hands that off to `ContentPost_agent`'s specialists (contract-only, JSON, no shared code — the same pattern as `mediaContentAgent → ProdReel`) rather than re-deriving formatting rules — this is the Phase 4 integration point noted in §4/§8. Until that handoff exists, `GTM_Agent`'s guides describe *what to post and when*, not the exact formatted text.

### The rating/prioritization requirement (distribution-specialist)

The user's brief explicitly asks for each distribution step to be **rated** and the overall list **prioritized**, not just enumerated. This needs a real rubric, not a vibe — `refs/platform-scoring-methodology.md` will define scoring dimensions (reach potential, effort/cost, audience fit to the classified project category, time-to-value, and prerequisite dependencies — e.g. "get 3 testimonials before a Product Hunt launch") and every `platforms/*.yaml` entry carries the fields that rubric scores against. This is the same shape as `LegalAgent/refs/risk-scoring-methodology.md` scoring clause risk, applied to launch channels instead.

### Live web search (marketing-specialist only)

This is an architectural departure from the rest of `Dev_Agents`: every other agent's knowledge is static (ref files, YAML registries) because the domain knowledge is stable enough to bake in. Marketing tactics and which channels currently work are not — the user explicitly asked for the marketing plan to be grounded in a live search for current best practices in the project's specific field. `marketing-specialist.md` is the only file in this repo's agent roster (besides general-purpose research use) that requires `WebSearch` as a first-class tool, and its Critical Rules should say so explicitly, matching this repo's "separate identity from knowledge" convention while acknowledging the exception.

## 6. Critical Rules (for the eventual agent definition files)

- **Classify before routing.** Every run starts with project classification (`refs/project-classification.md`) — platform and marketing recommendations are meaningless without knowing the project's field.
- **Guides only, never actions.** No specialist posts, deploys, or files anything on the user's behalf; output is always a Markdown document for the user to execute.
- **Platform rules live in YAML**, not prompt strings — same rule as `ContentPost_agent`/`PaymentAgent` (`Dev_Agents/CLAUDE.md` rules 5/7). Adding a distribution platform is one new YAML file.
- **Every rated recommendation must cite its scoring dimensions** (from `platform-scoring-methodology.md`), not present a bare ranked list with no rationale — this is what makes the guide actionable instead of generic.
- **marketing-specialist must ground claims in its live search results**, not general training-data assumptions about "what works in marketing," and should note when a tactic is field-specific vs. generic.

## 7. Research Summary (what still needs validating during Phase 1 build)

- Draft the initial `platforms/*.yaml` set against a representative spread of project categories (dev tool, SaaS, game, content tool) — this repo's own agents are convenient test subjects.
- Confirm which fields belong on a platform YAML entry (name, url, category tags, effort rating, reach rating, prerequisites, submission format) by drafting 3–4 real entries first (Product Hunt, Hacker News "Show HN", npm, a game-specific store like itch.io) before generalizing the schema.
- Validate `project-classification.md`'s inference rules against this repo's existing `README.md`/`plan.md`/`CLAUDE.md` files as real fixtures (mirrors `LegalAgent`'s hand-labeled-fixture testing approach, adapted since there's no single "correct" JSON schema output here — output is prose, so validation is closer to `docs-builder`'s quality-review model than to `validate_report.py`'s schema check).

## 8. Implementation Phases

### Phase 1 — Core: orchestrator + classifier + Shipping Guide — **COMPLETE**
- `gtm-agent.md` (orchestrator, single-specialist routing only), `shipping-specialist.md`, `refs/project-classification.md`, `refs/presentation-standards.md`, `refs/deployment-patterns.md` — all built, and `gtm-agent.md`/`shipping-specialist.md` symlinked into `/home/vscode/.claude/agents/` (verified with `readlink -f`).
- Deliverable: given a project's README/plan/CLAUDE.md, produce a `SHIPPING_GUIDE.md` covering deployment options for the detected stack + a presentation checklist.
- Acceptance: dry-run tested (no files written to the targets) against `LegalAgent`, `PaymentAgent`, and `code-mapper` — chosen to cover both the "Claude Code agent" stack special case and a traditional dev-tool/library stack. Classification came out correct and specific for all three (including correctly detecting the Claude Code agent stack instead of forcing a hosting recommendation onto it). The first test pass surfaced 4 real gaps, since fixed in the ref files before calling this done:
  1. `project-classification.md`'s "Inputs to read" was too rigid on exact filenames — `PaymentAgent` has no `README.md`/`CLAUDE.md`, only `payment_guide.md` + `HowTo.md`. Added a fallback for substitute filenames.
  2. `presentation-standards.md` §1 had no check for "no `README.md` at all, even though substitute docs exist" — added, marked blocking.
  3. `presentation-standards.md` §3 had no check for README-embedded assets being untracked in git (live-verified against `code-mapper`: `Image.png` is referenced in its README but untracked) or for `.gitignore` excluding a project's own core files (live-verified against `LegalAgent`: its `.gitignore` excludes `CLAUDE.md`/`plan.md`/`HowTo.md`/`.claude/`, meaning the agent definition itself isn't committed) — both added as blocking checks.
  4. `deployment-patterns.md` had no guidance for a dual-artifact project (e.g. `code-mapper` is both a standalone script needing §1's package-registry path *and* ships `agent.md` needing §9's registration path) — added so both deployment actions get surfaced instead of one being silently dropped.
- Note on `§9`'s "4 distinct categories" criterion: this repo's actual subdirectories skew heavily toward **AI agent** (Claude Code agent-definition projects) and **dev tool/library**, with no real SaaS/game/mobile/API fixture currently in the portfolio to test against — see the honest caveat under §9 rather than a fabricated pass on that specific bullet.

### Phase 2 — Distribution Guide + platform registry — **COMPLETE**
- `distribution-specialist.md`, `refs/platform-scoring-methodology.md`, and 12 `platforms/*.yaml` files (product-hunt, hacker-news, github-topics, package-registries, niche-communities, itch-io, steam, indie-hackers, claude-code-plugin-marketplace, awesome-lists, app-stores-mobile, devto) spanning all 8 categories from `project-classification.md` — built, and `distribution-specialist.md` symlinked into `/home/vscode/.claude/agents/` (verified with `readlink -f`). `gtm-agent.md` extended to route to it as a second guide type (still single-specialist-per-run).
- Deliverable: `DISTRIBUTION_GUIDE.md` — rated, prioritized, step-by-step platform list for the classified project.
- Acceptance: dry-run tested (no files written to the targets) against `LegalAgent`, `code-mapper`, and `PaymentAgent`. All 3 passed: category-fit exclusion worked correctly (itch-io/steam/app-stores-mobile never surfaced for non-matching categories), composite scores computed correctly per the formula, and Product Hunt was correctly placed in **Blocked** in all three despite having the highest raw composite score each time — the prerequisite-override rule fired as designed rather than being defeated by a high score. `niche-communities.yaml` was correctly instantiated with real, field-specific subreddits per project rather than left generic, and `claude-code-plugin-marketplace.yaml` matched correctly for the AI-agent-stack targets. The test pass surfaced 3 minor gaps, since fixed:
  1. `project-classification.md`'s Dimension 1 worked examples didn't note that `code-mapper` also deserves an **AI agent** secondary tag (its README documents an optional `agent.md` companion) — missing this would have silently dropped `claude-code-plugin-marketplace.yaml` from its guide, since `distribution-specialist` matches on primary *or* secondary category. Added `code-mapper` as a second worked example alongside `CI_CD_agent`.
  2. `platform-scoring-methodology.md` didn't distinguish a **project-state** prerequisite (verifiable from the project's files, e.g. "actually published") from an **operator-preparation** prerequisite (about the human, e.g. "enough standing in the community") — the latter is permanently Blocked on every run by design, but read like a project defect without the distinction. Added a clarifying note.
  3. `platforms/package-registries.yaml`'s prerequisite wording was ambiguous between "could be packaged" and "has actually been published" — tightened.

### Phase 3 — Marketing Plan + live search — **COMPLETE**
- `marketing-specialist.md` with `WebSearch` tool access, `refs/pitch-and-outreach.md` — built, and `marketing-specialist.md` symlinked into `/home/vscode/.claude/agents/` (verified with `readlink -f`). `gtm-agent.md` extended to route to it as a third guide type (still single-specialist-per-run; combined output stays Phase 4).
- Deliverable: `MARKETING_PLAN.md` — social/content strategy, trust-building tactics, and a written pitch/meeting script, grounded in a live search for the project's field's current marketing practices.
- Acceptance: dry-run tested (no files written to the targets), with real live `WebSearch` calls, against `LegalAgent` (legal-tech field) and `code-mapper` (dev-tooling field) — deliberately different fields to stress genuine grounding rather than one lucky search. Both passed: every field-specific claim carried a `(source: ...)` tag with real, current-feeling findings (e.g. a 2026 survey on in-house legal teams' AI adoption for LegalAgent; a real open-source dev-tool's zero-ad-spend growth story for code-mapper), general-practice items were correctly marked `(general practice)`, both pitch scripts were fully written with zero placeholders, and — critically — the maturity-matching guidance held under real pressure: neither guide fabricated social proof for these "functional/untested, no real users yet" projects (LegalAgent's Proof honestly stated its tests pass but it hasn't been used on a real client matter; code-mapper's Proof cited only its own reproducible README benchmark, never invented adoption numbers). The test pass surfaced 2 real gaps, since fixed:
  1. `pitch-and-outreach.md`'s "Why now" script step (and `marketing-specialist.md` Step 2) didn't note that a single broad field-survey search rarely produces a strong, citable "why now" hook — a second, more targeted follow-up search (e.g. a pricing-gap or cost-shift angle) was needed in both test runs. Added guidance to run that follow-up search explicitly.
  2. `pitch-and-outreach.md`'s attribution rule checked that a claim traced to *a* search result, but not that the claim's measured population actually matched the classified `target_user` — real risk surfaced live: a stat about in-house enterprise legal teams' AI adoption could be miscited as evidence of solo-practitioner demand (LegalAgent's actual audience) despite being topically "legal AI." Added an explicit scope-matching check to both the ref file and `marketing-specialist.md`'s Step 2.

### Phase 4 — Combined mode + polish
- `gtm-agent.md` gains full multi-specialist orchestration: default run produces one stitched `GTM_GUIDE.md` covering all three guides in sequence. **Done** — combined mode is now the default; a user can still request a single guide, which runs only that specialist exactly as in Phases 1–3. Each specialist's final "assemble and write" step now branches: standalone/single-guide invocation writes its own file directly (unchanged from Phases 1–3); combined-mode invocation returns its content to the orchestrator instead, which assembles the one `GTM_GUIDE.md`.
- Expand `platforms/*.yaml` coverage per additional verticals as real projects are run through it. Deferred — no new category has appeared in the portfolio since Phase 2's 12-platform set was drafted (see `§9`'s "4 distinct categories" caveat); revisit when a genuinely new category (SaaS/game/mobile/API) shows up as a real fixture, not speculatively now.
- Dogfood pass: run GTM_Agent against `Dev_Agents`' own shippable agents (`CI_CD_agent`, `LegalAgent`, `PaymentAgent`, `mediaContentAgent`) and use the output as their actual launch guides — doubles as end-to-end validation and real deliverables. **Done** — see the Dogfood Pass Results entry below.
- Revisit the `ContentPost_agent` handoff non-goal (§4) — decide whether marketing-specialist should optionally emit ready-to-route JSON briefs for `content-router`, once both agents are stable. **Decision: defer, don't build.** Both agents are individually stable, but nothing in three phases of dry-run and real-run testing has shown an actual need for this handoff — no user has asked `marketing-specialist` to hand off a drafted post, and `MARKETING_PLAN.md`'s Ongoing Strategy already tells the user *what* to post and *when* in prose, which is enough for a human to act on directly. Building a speculative JSON-brief contract now would be scope creep against a demonstrated need (`Dev_Agents/CLAUDE.md`'s "don't design for hypothetical future requirements"). Revisit only if real usage surfaces an actual friction point — e.g. a user manually retyping `MARKETING_PLAN.md` content into `content-router` prompts often enough that the handoff would save real, observed effort.

### Dogfood Pass Results (Phase 4)

Ran the real (file-writing, not dry-run) combined-mode `gtm-agent.md` against `LegalAgent` first to validate the design end-to-end, then against `CI_CD_agent`, `PaymentAgent`, `mediaContentAgent`, and `GTM_Agent` itself. Every target now has a real `GTM_GUIDE.md` in its own root. Combined-mode structure held up correctly across all five (one shared classification header, three full sections, nothing compressed or dropped) — no design fixes were needed to `gtm-agent.md` or the specialists themselves during this pass, only real findings surfaced by running it for real:

- **LegalAgent** — correctly classified as AI agent / Claude Code agent stack. Found a real blocking bug via direct inspection: `.gitignore` excludes `.claude/`, `CLAUDE.md`, `plan.md`, and `HowTo.md`, so the actual GitHub remote doesn't contain the agent file this project ships. Marketing Plan correctly rejected a well-known but wrong-population stat (lawyer/law-firm AI adoption) in favor of a small-business-owner-specific finding matching LegalAgent's real target user, per the Phase 3 scope-matching fix.
- **CI_CD_agent** — classified AI agent (secondary: dev tool), Python/Flask service calling the Anthropic API directly (not the Claude Code `.md`-agent stack case — correctly distinguished from the other four targets). Found that `CLAUDE.md` and `README.md` directly contradict each other on Tier 3's status, and that `tier3/` plus several core docs are entirely `.gitignore`-excluded and untracked — a fresh clone would be missing Tier 3 despite the README's "Complete" claim.
- **PaymentAgent** — classified AI agent (secondary: **CLI**, reversed from code-mapper's dev-tool-secondary pattern, reasoned independently rather than pattern-matched) given `scaffold.py`'s genuinely standalone, Claude-Code-independent usage. Found no git repository exists at all. Marketing Plan surfaced a real correction to `payment_guide.md`'s own claim that no AI payment tooling exists — Paddle and Stripe both shipped MCP servers/agent-skill plugins in 2026.
- **mediaContentAgent** — classified dev tool/library (secondary: AI agent) for its Python library/CLI plus thin agent-wrapper dual-artifact shape, matching maturity to its own `CLAUDE.md` (functional/untested — ComfyUI backend only smoke-tested against a fake server) rather than the optimistic parent-table summary. Found no git repository, no `README.md`, and no `LICENSE`.
- **GTM_Agent itself** — classified AI agent / Claude Code agent stack, `functional/untested-in-production` (dogfooded against this portfolio, never run against a project outside it). Honestly flagged its own gaps rather than writing a flattering self-review: no git repository anywhere up the tree, a stale `README.md` that still says "planning stage" despite this `plan.md`'s own Phase 1–4-complete status, and no `HowTo.md` yet despite `CLAUDE.md`'s own stated plan to write one. Marketing Plan found a genuinely timely hook via live search: a community Claude Code plugin marketplace launched publicly 3 days before this run.

**Cross-cutting finding worth acting on separately from any single guide:** three of five targets (`PaymentAgent`, `mediaContentAgent`, `GTM_Agent`) have no git repository at all, and a fourth (`LegalAgent`) has one whose `.gitignore` excludes the actual shipped artifact — `CI_CD_agent`'s docs additionally contradict each other about what's actually tracked. This is a portfolio-wide pattern, not a coincidence across independently-run guides, and is worth `Dev_Agents/CLAUDE.md`-level attention beyond what any single project's own `GTM_GUIDE.md` can fix on its own.

**One design point noted, not a defect:** the registered "GTM Agent" subagent type served a stale cached copy of its pre-Phase-4 instructions when first invoked for this pass (it correctly refused combined mode per rules that no longer exist in the file on disk) — subagent-type registrations don't hot-reload from disk mid-session. Worked around by using a fresh general-purpose agent explicitly told to re-read `gtm-agent.md` and the specialist files from disk for each dogfood run; worth remembering for any future same-session edit-then-immediately-invoke-by-name workflow in this repo.

## 9. Acceptance Criteria for "Phase 1 Complete"

- `gtm-agent.md` correctly classifies at least 4 distinct project categories from real `Dev_Agents` subdirectories. **Not literally met as written, by portfolio composition rather than a classifier defect**: real `Dev_Agents` subdirectories currently span only **AI agent** (Claude Code agent-definition projects — `LegalAgent`, `PaymentAgent`, `CI_CD_agent`, most of the portfolio) and **dev tool/library** (`code-mapper`; `mediaContentAgent` is dev tool/library with a content/creative-tool secondary tag) — 2 distinct primary categories were actually testable, not 4. Both classified correctly, including the Claude Code agent stack special case. Revisit this bullet once a real SaaS/game/mobile/API project exists in the portfolio to test against, rather than reinterpreting classification confidence as satisfying a category count the fixtures can't exercise.
- `shipping-specialist.md` produces a `SHIPPING_GUIDE.md` with no factual errors about the target project's actual stack (verified by re-reading the target's own docs). **Met** — dry-run tested against `LegalAgent`, `PaymentAgent`, `code-mapper`; see §8 Phase 1 for the 4 gaps found and fixed during this pass.
- Directory structure, `README.md`, and `CLAUDE.md` for `GTM_Agent/` exist and follow the `Dev_Agents/plan.md` §6 "Structure every agent consistently" convention. **Met.**
- This `plan.md` updated to mark Phase 1 items complete before Phase 2 work starts (per `Dev_Agents/CLAUDE.md` rule 2). **Met — this update.**
