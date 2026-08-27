# GTM Agent (Go-To-Market Agent)

> **Status: complete — all four phases implemented and tested.** The orchestrator, all three specialists, every ref file, and the 12-file platform registry exist and have been dry-run and real-run tested against this repo's own projects. See [`plan.md`](./plan.md) §8/§9 for the full phase-by-phase record and dogfood results.

Give it your project's `README.md`, `plan.md`, and `CLAUDE.md` (or any other file you point it at) and it writes back a concrete plan for shipping and getting the project in front of real users — not code, not a deployment, not a social post: a guide you follow.

## What it produces

| Guide | Answers | Specialist |
|---|---|---|
| **Shipping Guide** | What are my deployment options for this stack, and is my presentation (README, demo video, repo hygiene) actually good enough to ship? | `shipping-specialist` |
| **Distribution Guide** | Which platforms should I launch this on, in what order, and how much effort/payoff should I expect from each? | `distribution-specialist` |
| **Marketing Plan** | What's the current best-practice marketing strategy for a project like this, and what do I say in a meeting to convince someone to use/back/buy it? | `marketing-specialist` (grounded in a live web search — the one specialist here with `WebSearch` access) |

By default it runs all three and stitches one `GTM_GUIDE.md`; you can also ask for just one guide.

## What it does not do

- Does not deploy anything, post anything, or publish anything on your behalf — every output is a Markdown document for you to act on.
- Does not generate images, video, or website code — it writes briefs/scripts for a demo video or landing page, not the assets themselves.
- Is not legal, financial, or PR counsel — trust-building and pitch guidance is tactical, not professional advice.

See `plan.md` §4 for the full non-goals list and the reasoning behind each.

## How it's built

Orchestrator (`gtm-agent.md`) + 3 specialists, the same pattern used by `PaymentAgent` (orchestrator + per-provider specialists) and `ContentPost_agent` (content-router + specialists) elsewhere in this repo:

1. The orchestrator reads your input files and classifies the project (category, stack, maturity, target user).
2. It routes to the specialist(s) you asked for (default: all three).
3. Distribution recommendations are rated and prioritized against a documented rubric (`refs/platform-scoring-methodology.md`), not a bare unranked list — reach potential, effort/cost, audience fit, and prerequisite sequencing all factor in.
4. Platform knowledge lives in YAML (`platforms/*.yaml`), one file per platform — adding a new launch platform is a new YAML file, no code change.

`GTM_Agent/platforms/*.yaml` is a different registry from `ContentPost_agent/platforms/*.yaml` even where a platform name overlaps (X, LinkedIn, Reddit, Hacker News): this repo's version stores only launch-strategy metadata (should I use this platform, when, and why), never post-formatting rules (character limits, hashtags, tone) — see `plan.md` §5 for the full boundary.

## Setup / Usage

No install, no runtime dependencies — every specialist and ref file is Markdown/YAML/live `WebSearch` consumed directly by Claude Code. Invoke via the agent mechanism, pointing at a target project directory:

```
@gtm-agent produce a full GTM guide for LegalAgent          # default: combined GTM_GUIDE.md
@gtm-agent produce just a shipping guide for LegalAgent      # single-guide mode
@gtm-agent produce a distribution guide for code-mapper
@gtm-agent produce a marketing plan for PaymentAgent
```

Or invoke a specialist directly (standalone mode — writes that specialist's own file):

```
@shipping-specialist ...
@distribution-specialist ...
@marketing-specialist ...
```

See [`HowTo.md`](./HowTo.md) for the step-by-step guide and [`GTM_GUIDE.md`](./GTM_GUIDE.md) for a real example of the combined output (GTM_Agent's own dogfood run against itself).

## Project Structure

```
GTM_Agent/
├── README.md                        ← this file
├── plan.md                          ← implementation plan — read first
├── CLAUDE.md                        ← guidance for Claude Code working in this directory
├── HowTo.md                         ← step-by-step usage guide
├── GTM_GUIDE.md                     ← real dogfood output (GTM_Agent on itself)
├── .claude/agents/
│   ├── gtm-agent.md                 ← orchestrator (defaults to combined mode)
│   ├── shipping-specialist.md       ← Shipping Guide
│   ├── distribution-specialist.md   ← Distribution Guide
│   └── marketing-specialist.md      ← Marketing Plan (the one specialist with WebSearch access)
├── refs/                            ← project-classification, presentation-standards, deployment-patterns,
│                                        platform-scoring-methodology, pitch-and-outreach
└── platforms/                       ← 12 YAML files: product-hunt, hacker-news, github-topics,
                                          package-registries, niche-communities, itch-io, steam,
                                          indie-hackers, claude-code-plugin-marketplace, awesome-lists,
                                          app-stores-mobile, devto
```

## Roadmap

All four phases are complete:

- **Phase 1 ✓** — orchestrator + project classifier + Shipping Guide (static ref-file knowledge only).
- **Phase 2 ✓** — Distribution Guide + rated/prioritized 12-file platform registry.
- **Phase 3 ✓** — Marketing Plan, grounded in live web search, plus a pitch/meeting script.
- **Phase 4 ✓** — combined `GTM_GUIDE.md` output + a real, file-writing dogfood pass across `LegalAgent`, `CI_CD_agent`, `PaymentAgent`, `mediaContentAgent`, and this project itself.

Full detail, acceptance criteria per phase, and dogfood results: [`plan.md`](./plan.md) §8/§9.
