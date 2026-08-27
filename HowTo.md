# GTM Agent — How To Use

A step-by-step guide for using GTM_Agent to turn a finished (or near-finished) project
into a concrete plan for shipping it, listing it, and getting it in front of real users.

---

## Before You Start — Read This

This agent is a **document-generation tool, not an automation tool.** It reads your
project's docs, classifies what kind of project it is, and writes Markdown guides — it
never deploys anything, never submits to a platform, never posts content, and never
contacts anyone on your behalf. Every guide it produces is something *you* execute.

It does **not**:
- Run `terraform apply`, push to a host, or otherwise deploy your project.
- Create accounts, submit listings, or post to Product Hunt/Hacker News/anywhere else.
- Send outreach messages, DMs, or emails.
- Generate the actual demo video, screenshots, or landing page — it writes a brief for
  what to capture, production is on you (or a tool like `mediaContentAgent`).

Marketing/pitch guidance is tactical advice, not legal, financial, or PR counsel — see
`refs/pitch-and-outreach.md`'s disclaimer posture if you want the full reasoning.

---

## What This Agent Produces

Point it at a project and, by default, it produces one combined guide:

| File | Contents |
|---|---|
| `GTM_GUIDE.md` (default) | All three guides below, stitched into one file under a single shared classification header |
| `SHIPPING_GUIDE.md` (on request) | Deployment options for the detected stack + a presentation-readiness checklist (README quality, demo/screenshot brief, repo hygiene) |
| `DISTRIBUTION_GUIDE.md` (on request) | A rated, prioritized, step-by-step list of platforms to launch on, split into "Ready Now" and "Blocked" |
| `MARKETING_PLAN.md` (on request) | An ongoing content/trust-building strategy grounded in a live web search for your project's field, plus a fully-written pitch/meeting script |

Every run starts by **classifying** the target project — category (dev tool/library,
SaaS/web app, CLI, game, mobile app, API, content/creative tool, or AI agent), stack,
maturity stage, and target user (`refs/project-classification.md`). This classification
is shown to you before any guide content is written, so a wrong read is visible and
correctable, not silently baked into the output.

---

## Part 1 — Setup

No installation needed if you're already working inside the `Dev_Agents` repo — the
agent files are registered project-locally (`GTM_Agent/.claude/agents/`) and also
symlinked into the personal tier (`/home/vscode/.claude/agents/`), so `@gtm-agent` and
the three specialists are invocable from any directory on this machine.

To use it against a project **outside** this repo (or on a different machine), copy the
whole directory and register it:

```bash
mkdir -p /path/to/your/other/machine/.claude/agents
cp -r GTM_Agent/.claude/agents/*.md   /path/to/your/other/machine/.claude/agents/
cp -r GTM_Agent/refs                   /path/to/target/GTM_Agent/refs
cp -r GTM_Agent/platforms              /path/to/target/GTM_Agent/platforms
```

The four agent `.md` files reference `refs/*.md` and `platforms/*.yaml` by relative
path from `GTM_Agent/`, so keep that directory structure intact wherever you copy it.

---

## Part 2 — Running It

### Combined mode (default) — the full GTM guide

```
@gtm-agent produce a go-to-market guide for ../LegalAgent
```

This classifies the target, runs all three specialists, and writes one
`GTM_GUIDE.md` into the target project's root — Shipping Guide, then Distribution
Guide, then Marketing Plan, each showing its full content under the shared
classification header.

### Single-guide mode — just one guide

```
@gtm-agent produce just a shipping guide for ../code-mapper
@gtm-agent produce a distribution guide for ../PaymentAgent
@gtm-agent produce a marketing plan for ../mediaContentAgent
```

Runs only the named specialist, which writes its own file directly
(`SHIPPING_GUIDE.md`, `DISTRIBUTION_GUIDE.md`, or `MARKETING_PLAN.md`).

### Invoking a specialist directly

If you already have a classification in hand (e.g. from a prior run) and just want one
guide regenerated, you can skip the orchestrator:

```
@shipping-specialist ...
@distribution-specialist ...
@marketing-specialist ...
```

A directly-invoked specialist always runs standalone — it classifies the project itself
if you don't hand it a classification block, and always writes its own file.

### Pointing it at non-default input files

By default it reads the target's `README.md`, `plan.md`, and `CLAUDE.md` (or whatever
subset exists — see the next section for what happens when those don't exist). To point
it at something else:

```
@gtm-agent produce a shipping guide for ../SomeProject, using its docs/overview.md
and docs/setup.md instead of the usual files
```

---

## Part 3 — Reading the Classification

Every guide opens with a classification line:

```
_Classification: AI agent · Claude Code agent (.md definitions, no hosted runtime) ·
functional/untested-in-production · target user: solo founders and small teams..._
```

**If your project has no `README.md`/`plan.md`/`CLAUDE.md`** (e.g. it uses different
filenames for its overview/usage docs), the agent looks for whichever files are actually
serving those roles instead of stopping at "not enough input" — check the
`source_files` note in the classification for which files it actually used.

**If the classification looks wrong**, say so before reading further into the guide —
everything downstream (deployment recommendations, platform matches, marketing
targeting) depends on it being right. A wrong category will produce guide content that
doesn't fit your project.

---

## Part 4 — Understanding Each Section

### Shipping Guide

**Deployment Options** names one primary path plus at most one alternative — it will
never recommend a hosting provider (Vercel, Railway, etc.) for a project whose stack is
"Claude Code agent (no hosted runtime)"; instead it describes the actual deployment
story for that case: registering the agent file locally and, for cross-machine use,
symlinking it into the personal tier.

**Presentation Checklist** marks each item `[present]` or `[missing — recommendation]`
across README quality, demo/screenshot brief, repo hygiene, and whether a landing page
is even worth it for your category. It also checks things a docs-only read can't catch
by inspecting the actual repo state — e.g. whether `.gitignore` accidentally excludes
files your README claims to ship, or whether an image your README embeds is actually
tracked in git. Ends with a **Blocking vs. Nice-to-have** split so you know what to fix
before shipping versus what can wait.

### Distribution Guide

Every platform is scored on reach, audience fit, and effort (`refs/platform-scoring-
methodology.md`'s composite formula) and split into:
- **Ready Now** — sequenced by score, nothing blocking it.
- **Blocked** — has an unmet prerequisite (e.g. Product Hunt needs a live demo and
  testimonials before it's worth attempting), with a note on how to satisfy it — often
  by pointing at another Ready Now item's own output (a Hacker News thread's comments
  can be the testimonial source Product Hunt wants).

A platform never appears if your project's category doesn't fit it at all — you won't
see itch.io/Steam recommendations for a CLI tool, for instance.

### Marketing Plan

Grounded in a real, live web search for your project's specific field — not generic
"best practices" advice. Every claim in the Ongoing Strategy is marked
`(source: ...)` (a real search finding) or `(general practice)` (a durable tactic from
`refs/pitch-and-outreach.md`), and a claim is only used if its measured population
actually matches your project's target user — a stat about enterprise adoption won't get
used as evidence for a solo-developer product just because both are "AI." The
Pitch/Meeting Script is fully written and specific to your project (a real hook, a
sourced "why now," proof matched to your project's *actual* maturity — it won't
fabricate traction you don't have) — never a fill-in-the-blank template.

---

## Part 5 — Troubleshooting

### It refuses to produce a combined guide and says only one specialist is available

If you're using an already-registered subagent (invoked by name rather than through a
fresh session) right after this agent's files were edited, it may be serving a stale
cached copy of its own instructions — subagent registrations don't hot-reload mid-
session. Start a fresh Claude Code session, or ask it to re-read `gtm-agent.md` from
disk before proceeding.

### The classification looks wrong or too generic

Check `confidence_notes` in the classification block — it will say plainly if the input
files were too thin to be confident about a dimension. Point it at more specific input
files, or correct it directly and ask it to proceed with your correction.

### Marketing Plan has no live-search citations, or they look generic

Ask it to run a second, more targeted search specifically for your project's "why now"
angle (a pricing gap, a named competitor, a recent shift) — a single broad field survey
often isn't enough on its own, and the agent is instructed to run a follow-up search
rather than settle for generic results.

### A platform I expected to see isn't in the Distribution Guide

Check your project's classification — a platform only appears if your category (primary
or secondary) is in that platform's `category_fit` list. If your project genuinely spans
two categories (e.g. it's both a standalone script and a Claude Code agent, like
`code-mapper`), make sure the secondary tag was actually assigned — ask it to reclassify
explicitly considering a secondary tag if it seems to have missed one.

---

## Quick Reference

```
# Combined guide (default)
@gtm-agent produce a go-to-market guide for <path-to-project>

# One guide only
@gtm-agent produce just a shipping guide for <path-to-project>
@gtm-agent produce a distribution guide for <path-to-project>
@gtm-agent produce a marketing plan for <path-to-project>

# Non-default input files
@gtm-agent produce a shipping guide for <path>, using <file1> and <file2> instead
```

Output files land in the **target project's own root**, not inside `GTM_Agent/` —
except when you run GTM_Agent against itself, in which case both are the same
directory (see `GTM_Agent/GTM_GUIDE.md` for a real worked example of the agent's own
output, produced during its Phase 4 dogfood pass).
