# GTM Agent (Go-To-Market Agent)

Point it at a finished or near-finished project and it writes back a concrete, prioritized plan for shipping that project and getting it in front of real users. Not code, not a deployment, not a social post — a Markdown guide you follow.

![GTM_thumb.png]

You give it your project's `README.md`, `plan.md`, and `CLAUDE.md` (or any other files you name). It classifies the project — category, tech stack, maturity, target user — and produces a single `GTM_GUIDE.md` with five sections.

## What it produces

| Section                 | Answers                                                                                                                                                                                |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Positioning**         | What exactly is this, to whom, and unlike what? Is the name already taken by something bigger in the same niche? Which differentiators would survive a competitor's next release?      |
| **Shipping Guide**      | What are the deployment options for this stack? Is the presentation — README, demo video, repo hygiene — actually good enough to ship?                                                 |
| **Distribution Guide**  | Which platforms should this launch on, in what order, and what effort/payoff should each be expected to return?                                                                        |
| **Marketing Plan**      | What is the current best-practice marketing strategy for a project like this, and what should be said in a meeting to convince someone to use, back, or buy it?                        |
| **Pricing & Packaging** | Which license fits the goal for this project? Free, paid, or donation — and where is the line? What do comparable tools charge, and what is the exact next command to set payments up? |

Any one section can be requested on its own. An existing guide can also be **refreshed** — re-run against the project's current state, with a "what changed" summary at the top.

Three of the five sections are grounded in **live web search** rather than baked-in advice: Positioning (namespace and competitor checks), Marketing (current field practice), and Pricing (comparable prices go stale in weeks). The ref files own the _method_; the search owns the _substance_.

## What it does not do

- Does not deploy, post, publish, or register anything on your behalf. Every output is a Markdown document for you to act on.
- Does not generate images, video, or website code — it writes the brief or script for a demo video or landing page, not the assets.
- Is not legal, financial, or PR counsel. Pitch and trust-building guidance is tactical, not professional advice.

## How it works

An orchestrator (`gtm-agent.md`) plus five specialists, following the orchestrator + specialist pattern.

1. The orchestrator reads the input files once and classifies the project.
2. It runs the specialists in two waves. **Positioning runs first, alone** — a namespace collision or a fuzzy one-liner changes what the other four sections are even worth doing. Its findings (refined one-liner, defensible differentiators, "who this is not for" boundary, name-collision check) are then handed to **Shipping, Distribution, Marketing, and Pricing**, which run in parallel.
3. If a specialist fails, the orchestrator retries once, then produces that section itself from the same ref files and notes it in the guide's footer. A run never stalls on a dead specialist.
4. Distribution recommendations are rated and prioritized against a documented rubric — reach potential, effort/cost, audience fit, prerequisite sequencing — never a bare unranked list.
5. Platform knowledge lives in YAML, one file per platform. Adding a launch platform is a new YAML file, no code change.

## Setup and usage

No install and no runtime dependencies to produce a guide — every specialist and ref file is Markdown, YAML, and live `WebSearch` consumed directly by Claude Code.

Invoke via the agent mechanism, pointing at a target project directory:

```
@gtm-agent produce a full GTM guide for ./my-project      # default: combined, all 5 sections
@gtm-agent produce a positioning guide for ./my-project    # single section
@gtm-agent produce a distribution guide for ./my-project
@gtm-agent produce a marketing plan for ./my-project
@gtm-agent produce a pricing guide for ./my-project
@gtm-agent refresh ./my-project's GTM_GUIDE.md             # re-run, report what changed
```

Or invoke a specialist directly — it writes its own file:

```
@positioning-specialist ...   @shipping-specialist ...   @distribution-specialist ...
@marketing-specialist ...     @pricing-specialist ...
```

The one shell command in the project is a maintenance tool, not part of any run — a schema check for the platform registry after editing a `platforms/*.yaml` file:

```bash
python lib/validate_platforms.py
```

See [`docs/HowTo.md`](./docs/HowTo.md) for the step-by-step guide and [`docs/GTM_GUIDE.md`](./docs/GTM_GUIDE.md) for a full example of the combined output.

## Project structure

```
GTM_Agent/
├── README.md
├── CLAUDE.md                         guidance for Claude Code in this directory
├── docs/
│   ├── plan.md                       architecture and design record
│   ├── HowTo.md                      step-by-step usage guide
│   └── GTM_GUIDE.md                  example combined output
├── .claude/agents/
│   ├── gtm-agent.md                  orchestrator (two-wave combined mode by default)
│   ├── positioning-specialist.md     runs first, feeds the other four (WebSearch)
│   ├── shipping-specialist.md
│   ├── distribution-specialist.md
│   ├── marketing-specialist.md       (WebSearch)
│   └── pricing-specialist.md         (WebSearch)
├── lib/
│   └── validate_platforms.py         schema validator for the platform registry
├── refs/                             8 method files: project-classification, presentation-standards,
│                                       deployment-patterns, platform-scoring-methodology,
│                                       pitch-and-outreach, guide-quality-checklist,
│                                       positioning-methodology, pricing-and-licensing
└── platforms/                        12 launch-platform YAML files: product-hunt, hacker-news,
                                        github-topics, package-registries, niche-communities,
                                        itch-io, steam, indie-hackers,
                                        claude-code-plugin-marketplace, awesome-lists,
                                        app-stores-mobile, devto
```

Each `platforms/*.yaml` entry carries only launch-strategy metadata — category fit, effort/reach rating, prerequisites, submission workflow — never post-formatting rules like character limits or hashtags.
