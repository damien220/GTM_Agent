# GTM Agent (Go-To-Market Agent)

> **Status: complete — all six phases implemented.** The orchestrator, all five specialists, every ref file, and the 12-file platform registry exist; Phases 1–4 were dry-run and real-run tested against this repo's own projects plus one project outside it. Phase 5 (2026-08-29) hardened what that external run exposed: a failure-recovery contract, parallel specialists, a refresh mode, a quality self-check, and a registry validator. Phase 6 (2026-08-29) added the Positioning and Pricing specialists. Phase 5 and 6 are not yet validated by a real end-to-end run — [`docs/HowTo.md`](./docs/HowTo.md) Part 6 is the manual-test procedure. See [`docs/plan.md`](./docs/plan.md) §8/§9 for the full phase-by-phase record and dogfood results.

Give it your project's `README.md`, `plan.md`, and `CLAUDE.md` (or any other file you point it at) and it writes back a concrete plan for shipping and getting the project in front of real users — not code, not a deployment, not a social post: a guide you follow.

## What it produces

| Guide | Answers | Specialist |
|---|---|---|
| **Positioning** | What exactly is this, to whom, and unlike what? Is my name already taken by something bigger in my own niche? Which of my differentiators would survive a competitor's next release? | `positioning-specialist` (live web search — namespace and competitor checks) |
| **Shipping Guide** | What are my deployment options for this stack, and is my presentation (README, demo video, repo hygiene) actually good enough to ship? | `shipping-specialist` |
| **Distribution Guide** | Which platforms should I launch this on, in what order, and how much effort/payoff should I expect from each? | `distribution-specialist` |
| **Marketing Plan** | What's the current best-practice marketing strategy for a project like this, and what do I say in a meeting to convince someone to use/back/buy it? | `marketing-specialist` (live web search — current field practice) |
| **Pricing & Packaging** | Which license fits what I actually want from this? Free, paid, or donation — and where's the line? What do comparable tools charge, and what's the exact next command to set payments up? | `pricing-specialist` (live web search — comparable pricing) |

By default it produces all five as one stitched `GTM_GUIDE.md`, **Positioning first** — a namespace collision or a fuzzy one-liner changes what the other four sections are even worth doing, so Positioning runs alone up front and its findings (the refined one-liner, the differentiators that are actually defensible, the "not for" boundary) are handed to the other four, which then run in parallel. You can also ask for just one guide, or ask it to **refresh** a guide it wrote earlier and tell you what changed.

## What it does not do

- Does not deploy anything, post anything, or publish anything on your behalf — every output is a Markdown document for you to act on.
- Does not generate images, video, or website code — it writes briefs/scripts for a demo video or landing page, not the assets themselves.
- Is not legal, financial, or PR counsel — trust-building and pitch guidance is tactical, not professional advice.

See `docs/plan.md` §4 for the full non-goals list and the reasoning behind each.

## How it's built

Orchestrator (`gtm-agent.md`) + 5 specialists, the same pattern used by `PaymentAgent` (orchestrator + per-provider specialists) and `ContentPost_agent` (content-router + specialists) elsewhere in this repo:

1. The orchestrator reads your input files and classifies the project (category, stack, maturity, target user).
2. It routes to the specialist(s) you asked for. The default runs all five in **two waves**: Positioning alone first, then Shipping, Distribution, Marketing and Pricing together in parallel, each carrying Positioning's findings. Positioning gets its own wave because it's the only one the others genuinely depend on; the other four have no cross-dependencies, so running them sequentially would buy nothing but time. Each specialist gets the file contents the orchestrator already read rather than re-reading your project four more times. If a specialist fails, the orchestrator retries once, then produces that section itself from the same ref files and says so in the guide's footer — a run never stalls waiting on a dead specialist.
3. Distribution recommendations are rated and prioritized against a documented rubric (`refs/platform-scoring-methodology.md`), not a bare unranked list — reach potential, effort/cost, audience fit, and prerequisite sequencing all factor in.
4. Platform knowledge lives in YAML (`platforms/*.yaml`), one file per platform — adding a new launch platform is a new YAML file, no code change.

`GTM_Agent/platforms/*.yaml` is a different registry from `ContentPost_agent/platforms/*.yaml` even where a platform name overlaps (X, LinkedIn, Reddit, Hacker News): this repo's version stores only launch-strategy metadata (should I use this platform, when, and why), never post-formatting rules (character limits, hashtags, tone) — see `docs/plan.md` §5 for the full boundary.

## Setup / Usage

No install, no runtime dependencies to produce a guide — every specialist and ref file is Markdown/YAML/live `WebSearch` consumed directly by Claude Code. (The one Python file, `lib/validate_platforms.py`, is a maintenance tool for the platform registry, not part of any run — see the end of this section.) Invoke via the agent mechanism, pointing at a target project directory:

```
@gtm-agent produce a full GTM guide for LegalAgent          # default: combined, all 5 sections
@gtm-agent produce a positioning guide for LegalAgent        # single-guide mode
@gtm-agent produce just a shipping guide for LegalAgent
@gtm-agent produce a distribution guide for code-mapper
@gtm-agent produce a marketing plan for PaymentAgent
@gtm-agent produce a pricing guide for mediaContentAgent
```

Already have a guide and want it brought up to date? Ask for a **refresh** instead of a fresh run:

```
@gtm-agent refresh the GTM_GUIDE.md in ../LegalAgent
@gtm-agent update PaymentAgent's MARKETING_PLAN.md
```

A refresh re-classifies the project against its *current* state, re-runs the relevant specialists (Positioning re-checks the namespace and competitors, Marketing re-searches its field, Pricing re-checks comparable prices — all three fresh), and puts a **"What changed since &lt;date&gt;"** summary at the top of the updated guide — concrete deltas only. If nothing material changed, it says so rather than inventing churn.

Or invoke a specialist directly (standalone mode — writes that specialist's own file):

```
@positioning-specialist ...
@shipping-specialist ...
@distribution-specialist ...
@marketing-specialist ...
@pricing-specialist ...
```

Maintaining the platform registry? Adding or editing a `platforms/*.yaml` file has one check to run:

```bash
../.venv/bin/python lib/validate_platforms.py
```

See [`docs/HowTo.md`](./docs/HowTo.md) for the step-by-step guide and [`docs/GTM_GUIDE.md`](./docs/GTM_GUIDE.md) for a real example of the combined output (GTM_Agent's own dogfood run against itself).

## Project Structure

```
GTM_Agent/
├── README.md                        ← this file
├── CLAUDE.md                        ← guidance for Claude Code working in this directory
├── docs/
│   ├── plan.md                       ← implementation plan — read first
│   ├── HowTo.md                      ← step-by-step usage guide
│   └── GTM_GUIDE.md                  ← real dogfood output (GTM_Agent on itself)
├── .claude/agents/
│   ├── gtm-agent.md                 ← orchestrator (defaults to two-wave combined mode)
│   ├── positioning-specialist.md    ← Positioning — runs first, feeds the other four (WebSearch)
│   ├── shipping-specialist.md       ← Shipping Guide
│   ├── distribution-specialist.md   ← Distribution Guide
│   ├── marketing-specialist.md      ← Marketing Plan (WebSearch)
│   └── pricing-specialist.md        ← Pricing & Packaging (WebSearch)
├── lib/
│   └── validate_platforms.py        ← schema validator for the platform registry
├── refs/                            ← project-classification, presentation-standards, deployment-patterns,
│                                        platform-scoring-methodology, pitch-and-outreach,
│                                        guide-quality-checklist, positioning-methodology,
│                                        pricing-and-licensing
└── platforms/                       ← 12 YAML files: product-hunt, hacker-news, github-topics,
                                          package-registries, niche-communities, itch-io, steam,
                                          indie-hackers, claude-code-plugin-marketplace, awesome-lists,
                                          app-stores-mobile, devto
```

## Roadmap

All six phases are complete:

- **Phase 1 ✓** — orchestrator + project classifier + Shipping Guide (static ref-file knowledge only).
- **Phase 2 ✓** — Distribution Guide + rated/prioritized 12-file platform registry.
- **Phase 3 ✓** — Marketing Plan, grounded in live web search, plus a pitch/meeting script.
- **Phase 4 ✓** — combined `GTM_GUIDE.md` output + a real, file-writing dogfood pass across `LegalAgent`, `CI_CD_agent`, `PaymentAgent`, `mediaContentAgent`, and this project itself.
- **Phase 5 ✓** (2026-08-29) — post-review hardening after the first dogfood run on a project outside this repo: a failure-recovery contract so a crashed specialist can't stall a run, parallel specialist execution, a refresh mode, a guide-quality self-check, a platform-registry schema validator, and model tiering.
- **Phase 6 ✓** (2026-08-29) — the two new specialists the same review recommended: **Positioning** (namespace/collision check, refined one-liner, competitor table with a defensible-vs-merely-true call, "who this is NOT for") and **Pricing & Packaging** (license recommendation, free-vs-paid boundary, live-searched comparables, and a concrete `PaymentAgent`/donation handoff). The orchestrator moved to two-wave combined execution to carry Positioning's findings into the other four sections. Every numbered issue in the design review is now closed.

Still open, deliberately:

- **No automated end-to-end test.** The guide-quality checklist and the platform-registry validator are the only repeatable checks; the `test/` fixture directory with property assertions that [`docs/design-review-2026-08.md`](./docs/design-review-2026-08.md) §2.1 called the "better" option is still unbuilt, and neither Phase 5 nor Phase 6 has been exercised by a real run. [`docs/HowTo.md`](./docs/HowTo.md) Part 6 is the manual procedure in the meantime.
- **`platforms/` category expansion.** The registry covers all 8 project categories on paper, but this portfolio has only ever supplied AI-agent and dev-tool fixtures to test against — a real SaaS, game, mobile, or API project has to show up before expanding it means anything.

Full detail, acceptance criteria per phase, and dogfood results: [`docs/plan.md`](./docs/plan.md) §8/§9.
