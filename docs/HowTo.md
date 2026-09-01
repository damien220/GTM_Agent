# GTM Agent — How To Use

A step-by-step guide for using GTM_Agent to turn a finished (or near-finished) project
into a concrete plan for positioning it, shipping it, listing it, getting it in front of
real users, and deciding what to charge for it.

---

## Before You Start — Read This

This agent is a **document-generation tool, not an automation tool.** It reads your
project's docs, classifies what kind of project it is, and writes Markdown guides — it
never deploys anything, never submits to a platform, never posts content, never
registers a name or domain, never sets up payments, and never contacts anyone on your
behalf. Every guide it produces is something *you* execute.

It does **not**:
- Run `terraform apply`, push to a host, or otherwise deploy your project.
- Create accounts, submit listings, or post to Product Hunt/Hacker News/anywhere else.
- Send outreach messages, DMs, or emails.
- Register a package name, buy a domain, file a trademark, or rename anything.
- Run `PaymentAgent/scaffold.py`, configure a payment provider, or write a `LICENSE`
  file into your project. The Pricing guide **writes the command; you run it.**
- Generate the actual demo video, screenshots, or landing page — it writes a brief for
  what to capture, production is on you (or a tool like `mediaContentAgent`).

Marketing, positioning, licensing and pricing guidance is tactical advice — **not legal,
financial, tax, trademark, or PR counsel.** Anything touching dual licensing, trademarks,
contributor licensing, or tax gets an explicit "confirm with counsel/an accountant" note
in the guide itself. See `refs/pitch-and-outreach.md`, `refs/positioning-methodology.md`
§6 and `refs/pricing-and-licensing.md` §5 if you want the full reasoning.

---

## What This Agent Produces

Point it at a project and, by default, it produces one combined guide:

| File | Contents |
|---|---|
| `GTM_GUIDE.md` (default) | All five guides below, stitched into one file under a single shared classification header |
| `POSITIONING_GUIDE.md` (on request) | A namespace/collision check (GitHub, package registry, domain), a refined one-liner shown against your current one, a competitor table with a **defensible vs. merely true** call on each differentiator, and a "who this is NOT for" boundary |
| `SHIPPING_GUIDE.md` (on request) | Deployment options for the detected stack + a presentation-readiness checklist (README quality, demo/screenshot brief, repo hygiene) |
| `DISTRIBUTION_GUIDE.md` (on request) | A rated, prioritized, step-by-step list of platforms to launch on, split into "Ready Now" and "Blocked" |
| `MARKETING_PLAN.md` (on request) | An ongoing content/trust-building strategy grounded in a live web search for your project's field, plus a fully-written pitch/meeting script |
| `PRICING_GUIDE.md` (on request) | A license recommendation with its tradeoff, the free-vs-paid boundary, a live-searched table of what comparable tools charge, and a concrete `PaymentAgent` (or donation) handoff command |

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
the five specialists are invocable from any directory on this machine.

To use it against a project **outside** this repo (or on a different machine), copy the
whole directory and register it:

```bash
mkdir -p /path/to/your/other/machine/.claude/agents
cp -r GTM_Agent/.claude/agents/*.md   /path/to/your/other/machine/.claude/agents/
cp -r GTM_Agent/refs                   /path/to/target/GTM_Agent/refs
cp -r GTM_Agent/platforms              /path/to/target/GTM_Agent/platforms
```

The six agent `.md` files reference `refs/*.md` and `platforms/*.yaml` by relative
path from `GTM_Agent/`, so keep that directory structure intact wherever you copy it.

Three of the five specialists (Positioning, Marketing, Pricing) need live `WebSearch`.
If your environment has no web access they will say so rather than inventing findings —
but you'll get noticeably thinner guides for those three sections, so it's worth knowing
up front.

---

## Part 2 — Running It

### Combined mode (default) — the full GTM guide

```
@gtm-agent produce a go-to-market guide for ../LegalAgent
```

This classifies the target, runs all five specialists, and writes one `GTM_GUIDE.md`
into the target project's root: **Positioning, then Shipping Guide, then Distribution
Guide, then Marketing Plan, then Pricing & Packaging**, each showing its full content
under the shared classification header.

It runs in **two waves**, and you'll see that in the agent's own progress messages:

1. **Wave 1** — the Positioning Specialist runs alone. It does the namespace and
   competitor searches and produces the position: your refined one-liner, which of your
   differentiators are actually defensible, who this isn't for, and any name collision.
2. **Wave 2** — Shipping, Distribution, Marketing and Pricing run **in parallel**, all
   four dispatched at once, each handed Positioning's findings.

Positioning gets its own wave because it's the only section the others genuinely depend
on — Shipping uses the one-liner to say how your README should lead, Distribution uses
the position to judge which communities actually fit, Marketing takes its hook from it,
and Pricing needs the *defensible* differentiators specifically (a differentiator a
competitor closes next release can't support a price). The other four don't depend on
each other at all, so running them one after another would only cost you wall-clock
time.

### Single-guide mode — just one guide

```
@gtm-agent produce a positioning guide for ../A_OpenClaw
@gtm-agent produce just a shipping guide for ../code-mapper
@gtm-agent produce a distribution guide for ../PaymentAgent
@gtm-agent produce a marketing plan for ../mediaContentAgent
@gtm-agent produce a pricing guide for ../LegalAgent
```

Runs only the named specialist, which writes its own file directly
(`POSITIONING_GUIDE.md`, `SHIPPING_GUIDE.md`, `DISTRIBUTION_GUIDE.md`,
`MARKETING_PLAN.md`, or `PRICING_GUIDE.md`).

### Invoking a specialist directly

If you already have a classification in hand (e.g. from a prior run) and just want one
guide regenerated, you can skip the orchestrator:

```
@positioning-specialist ...
@shipping-specialist ...
@distribution-specialist ...
@marketing-specialist ...
@pricing-specialist ...
```

A directly-invoked specialist always runs standalone — it classifies the project itself
if you don't hand it a classification block, and always writes its own file. Note that a
directly-invoked Pricing Specialist won't have Positioning's context block (nothing
passed it one), so its reasoning about what your differentiation can support will be
thinner than in a combined run.

### Refresh mode — updating a guide you already have

A guide ages. Deployment options and platform prerequisites drift slowly; namespace
status, competitor moves, marketing findings, and comparable prices go stale in weeks.
Rather than regenerating from scratch and leaving you to spot the differences yourself,
ask for a refresh:

```
@gtm-agent refresh the GTM_GUIDE.md in ../LegalAgent
@gtm-agent update ../PaymentAgent's MARKETING_PLAN.md
@gtm-agent refresh ../code-mapper/DISTRIBUTION_GUIDE.md
@gtm-agent refresh ../A_OpenClaw/POSITIONING_GUIDE.md
```

Any of these triggers refresh mode — asking to "refresh"/"update" an existing
guide, or simply pointing the agent at an existing `GTM_GUIDE.md`,
`POSITIONING_GUIDE.md`, `SHIPPING_GUIDE.md`, `DISTRIBUTION_GUIDE.md`,
`MARKETING_PLAN.md`, or `PRICING_GUIDE.md`. What happens then:

1. It reads the **existing guide** and notes its date.
2. It **re-classifies the project against its current state** — a changed
   category, stack, maturity, or target user is the most consequential possible
   change, since it invalidates platform matches, the positioning frame, and
   marketing targeting downstream, so it gets reported first.
3. It **re-runs the relevant specialists**. Positioning, Marketing and Pricing always run
   *fresh* live searches — reusing the old namespace check, field findings, or comparable
   prices would defeat the point.
4. It writes the updated guide (in place, at the prior guide's own path) with a
   **"What changed since &lt;date&gt;"** block at the top.

That block carries concrete deltas only — "Product Hunt moved from Blocked to
Ready Now: the live demo its prerequisite wanted now exists," or "the npm name
was clear in June and is now taken by *X*," not "distribution outlook improved."
A prerequisite that is still unmet is not a change; a comparable that re-searched
to the same price is not a change. **If nothing material changed, it says exactly
that** rather than padding the list with rewordings; a refresh that reports "no
material change since 2026-06-14, project state and three fresh searches all
re-checked" is a useful answer, not a failed run.

The rest of the file below that block is a complete guide, not a diff — it still
stands alone for someone who never saw the earlier version.

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
everything downstream (the positioning frame, deployment recommendations, platform
matches, marketing targeting, which comparables get chosen) depends on it being right. A
wrong category will produce guide content that doesn't fit your project, and a wrong
`target_user` will quietly produce a competitor table and a pricing comparison aimed at
someone who isn't your buyer.

---

## Part 4 — Understanding Each Section

### Positioning

Comes first, and it's the section most likely to change what you do with the rest.

**Namespace / Collision Check** covers GitHub, the package registry that matches your
stack (PyPI, npm, crates.io — a Claude Code agent project usually has no registry
namespace at all, which the guide says outright), and a plain-name domain check. Each
comes back **clear / taken / crowded / not verified**, and anything taken or crowded
**names the specific colliding project**. "Crowded" is the under-diagnosed case: the name
is technically free but there's something dominant nearby, so every discovery channel is
fighting an existing association. A real collision is reported as a **finding with three
options** — position against it, differentiate the name, or accept the overlap, each with
its cost. It will never tell you to rename; that call is yours, and the point is that you
make it now rather than hearing about it from a commenter after launch.

**One-Liner** quotes your README's current version verbatim next to a refined one, plus
a line on what changed. The most common fix is moving from mechanism-first ("an
orchestrator plus five specialist subagents with a YAML registry") to outcome-first
("turns a finished side project into a concrete plan for shipping it"). If your README
has no one-liner at all, that's itself the finding.

**Competitor Comparison** picks 3-5 real, live-searched alternatives and — importantly —
picks the comparison *rows* from your classified target user, not from your own feature
list. A table scored on your own features is one you win by construction. Then every
differentiator gets called **defensible** (it follows from a structural choice a
competitor can't cheaply reverse — architecture, licensing, data, distribution position)
or **merely true** (a feature-parity gap that closes on their next release). Expect one
defensible and several merely-true; a table where everything reads "defensible" means the
test wasn't really applied.

**Who This Is NOT For** names 2-3 audiences that would genuinely land on your project and
should be sent elsewhere. It should be sharp enough that you can use it to decline a
feature request.

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

### Pricing & Packaging

Comes last, because it depends on everything above it — most directly on Positioning's
defensible differentiators, since those are what a price can actually be built on.

**License** gives you one recommendation, 2-3 reasons it fits *this* project's stated
goal (and it will tell you where it found that goal — a README status line, a parent
`CLAUDE.md`, the repo's own "sold, licensed, or donated" thesis), and **the one main
thing that choice gives up**. It's a recommendation with a tradeoff, never a mandate, and
never a lecture surveying every license. If the recommendation touches dual licensing,
trademark, or contributor licensing, you'll get a "confirm with counsel" note attached to
that specific item.

**Free vs. Paid** draws the open-core line if anything is paid — what's free forever and
genuinely useful on its own (not a functioning demo with a misleading name), versus what's
fair to gate — and picks one-time vs. subscription vs. usage-based based on how your tool
actually delivers value over time. A one-shot generator getting a subscription is the
mismatch this catches. **"Stay free" is a legitimate answer here**, and for a portfolio
piece or a tool whose whole advantage is being frictionless it's often the right one.

**What Comparable Tools Charge** is live-searched, 3-5 real named tools with their actual
current prices, each attributed `(source: ...)`. Comparables are chosen by **same buyer,
not same technology** — the thing your target user already pays for instead, even if it
shares no stack. Anything whose model doesn't transfer gets flagged: VC-subsidized
pricing an indie can't match, enterprise pricing that only exists behind a sales call, a
loss-leader attached to a bigger product. Prices are always given as a **range with
reasoning**, never a single confident number.

**Next Step** is a concrete handoff, not a suggestion — either a filled-in
`python PaymentAgent/scaffold.py --provider … --stack … --db …` command with every flag
already chosen from your classified stack, or `@payment-setup-agent` when the provider
genuinely turns on facts the agent doesn't have (tax exposure, geography, volume), or
`@donation-specialist` if the recommendation was stay-free. **The guide writes the
command; you run it.**

---

## Part 5 — Troubleshooting

### It refuses to produce a combined guide, or only mentions three specialists

If you're using an already-registered subagent (invoked by name rather than through a
fresh session) right after this agent's files were edited, it may be serving a stale
cached copy of its own instructions — subagent registrations don't hot-reload mid-
session. Start a fresh Claude Code session, or ask it to re-read `gtm-agent.md` from
disk before proceeding. This is the single most common confusing failure with this agent;
Part 6 opens with it for that reason.

### The classification looks wrong or too generic

Check `confidence_notes` in the classification block — it will say plainly if the input
files were too thin to be confident about a dimension. Point it at more specific input
files, or correct it directly and ask it to proceed with your correction.

### Marketing Plan has no live-search citations, or they look generic

Ask it to run a second, more targeted search specifically for your project's "why now"
angle (a pricing gap, a named competitor, a recent shift) — a single broad field survey
often isn't enough on its own, and the agent is instructed to run a follow-up search
rather than settle for generic results.

### The Positioning namespace check says "not verified" for something

That's the honest answer, not a bug — the agent is explicitly forbidden from rounding an
unverified check up to "clear," because a false "clear" is wrong in the expensive
direction. Check that registry yourself, or re-run with web access if the search was
unavailable.

### Positioning says my only differentiator is "merely true"

That's a real finding, not a harsh one. It means the thing you're leading with is a
feature-parity gap a competitor closes when they decide it matters. The useful follow-up
is in `refs/positioning-methodology.md` §4: what would it take to make it structural?
Sometimes the answer is a licensing or distribution choice you can actually make.

### The Pricing guide won't give me a specific price

By design — it gives a range with the reasoning that produced it, because a single number
reads as more authoritative than the evidence supports. If you want to narrow it, the
useful thing to feed back is a constraint the agent didn't have: your actual costs, a
specific competitor you're positioning against, or a target buyer's budget.

### The guide ends with a "Generation notes" footer saying a section was produced by fallback

That footer means a specialist failed twice (crashed, returned nothing, or returned
truncated output), so the orchestrator produced that section itself from the same ref
files rather than stalling the run. The section is real content, but it is second-best,
and the footer names the exact re-run command to get a proper one. This matters most for
the three live-search sections, since the orchestrator deliberately does **not** run
searches on their behalf: a fallback **Marketing** section is un-searched
general-practice framework, a fallback **Positioning** section has **no namespace status
and no named competitors** (it tells you what to check instead), and a fallback
**Pricing** section has **no comparables table** (the license and packaging reasoning
still works un-searched, so you get that). If Positioning fell back, the footer will also
say the other four sections ran without positioning context. Re-run the named specialist
when you want the full version.

### A platform I expected to see isn't in the Distribution Guide

Check your project's classification — a platform only appears if your category (primary
or secondary) is in that platform's `category_fit` list. If your project genuinely spans
two categories (e.g. it's both a standalone script and a Claude Code agent, like
`code-mapper`), make sure the secondary tag was actually assigned — ask it to reclassify
explicitly considering a secondary tag if it seems to have missed one.

---

## Part 6 — Manual Testing

There is still **no automated end-to-end test** for this agent (`docs/plan.md` §8, Phase
5 and Phase 6 acceptance both say so plainly). The two repeatable checks that do exist
are the platform-registry validator and the guide-quality checklist; everything else is
verified by running it and reading the output. This part is that procedure — each item as
**what to run → what correct output looks like → what a failure looks like**.

Work through it in order. Test 0 blocks everything after it.

### 0. The harness quirk — do this first

**What to run.** Nothing yet. Read this first, because it will otherwise make every
other test below produce misleading results.

A registered subagent type **does not hot-reload its `.md` file after an in-session
edit.** If you edit `gtm-agent.md` and then invoke `@gtm-agent` in the same session, you
may get the *previous* version of its instructions. This has already caused a real
false failure: the agent once correctly refused combined mode according to rules that no
longer existed on disk (`docs/plan.md` §8, Phase 4 dogfood notes). A newly *added* agent
file has the same problem in reverse — the session may not know it exists at all.

**How to test current-disk behavior instead**, either:

- **Start a fresh Claude Code session.** Simplest and most reliable.
- **Or use a fresh general-purpose agent** and tell it explicitly to re-read the agent
  files from disk and follow them — not the named subagent type. This is the workaround
  that was used for the entire Phase 4 dogfood pass.

**What correct looks like:** the agent's behavior matches what you just read in the file
— e.g. it mentions five specialists and two waves.

**What failure looks like:** it talks about three specialists, refuses combined mode, or
doesn't recognize `positioning-specialist`/`pricing-specialist` at all. That's a stale
registration, not a bug in the files. Restart the session.

> **This is why the Phase 5 and Phase 6 work has not been run end to end yet.** Both
> passes were implemented in-session, which means the very session that wrote them can't
> reliably test them by name.

### 1. Platform registry validator

**What to run**, from `GTM_Agent/`:

```bash
../.venv/bin/python lib/validate_platforms.py
echo "exit: $?"
```

**What correct looks like:** 12 `PASS` lines (one per file in `platforms/`), a closing
"All 12 platform file(s) conform to the schema…" line, and **exit 0**.

**Now break it deliberately** to confirm the validator actually validates — edit any
platform file and give it a bad `time_to_value`:

```bash
sed -i 's/^time_to_value: .*/time_to_value: instant/' platforms/devto.yaml
../.venv/bin/python lib/validate_platforms.py
echo "exit: $?"
```

**What correct looks like:** `FAIL  devto.yaml` with a specific message naming the field
and the allowed values (`time_to_value` must be one of ['fast','medium','slow'] (got
'instant')), a "1 of 12 platform file(s) failed schema validation" line, and **exit 1**.

**Then restore it** — `git checkout platforms/devto.yaml` — and re-run to confirm you're
back to 12/12 PASS. Don't skip the restore.

**What failure looks like:** the broken file still passes (the validator isn't checking
what it claims), or the run errors out before reaching the file (a venv/PyYAML problem,
not a schema problem).

### 2. Classification

**What to run** — against two or three real portfolio projects with genuinely different
shapes:

```
@gtm-agent produce a go-to-market guide for ../LegalAgent
@gtm-agent produce a go-to-market guide for ../code-mapper
@gtm-agent produce a go-to-market guide for ../CI_CD_agent
```

(If you don't want the files written, say "dry run, don't write any files" — the
classification block is still stated.)

**What correct looks like:**

- The classification block is **stated before any guide content** — category, stack,
  maturity, target_user, source_files, confidence_notes.
- `LegalAgent` → **AI agent**, stack "Claude Code agent (.md definitions … no hosted
  runtime)", maturity *functional/untested* (not "shipped" — its own docs say tests pass
  but it hasn't been used on a real matter).
- `code-mapper` → **dev tool / library** with an **AI agent secondary tag**. This one is
  the real test: the secondary tag exists because its README documents an optional
  `agent.md` companion, and missing it silently drops
  `claude-code-plugin-marketplace.yaml` from the Distribution section. If the secondary
  tag is absent, that's a classifier regression.
- `CI_CD_agent` → **AI agent** with a **dev tool secondary tag**, and a Python/Flask
  stack — *not* the Claude Code `.md`-agent stack case. Getting this one wrong in either
  direction is a meaningful failure, since it changes the whole deployment story.

**What failure looks like:** guide content appearing before the classification block;
maturity rounded up to "shipped" on a project whose docs say otherwise; `code-mapper`
classified dev-tool-only; `CI_CD_agent` classified as the no-hosted-runtime agent case.

### 3. Combined mode — five sections, two waves

**What to run:**

```
@gtm-agent produce a go-to-market guide for ../LegalAgent
```

**What correct looks like:**

- **One** `GTM_GUIDE.md` written to the *target's* root — not five separate files, not a
  file inside `GTM_Agent/`.
- **Five sections in this order:** Positioning → Shipping Guide → Distribution Guide →
  Marketing Plan → Pricing & Packaging.
- **One shared classification header** at the top, and no per-section classification
  lines that could drift from it.
- **Positioning ran first**, alone — visible in the agent's progress output as a wave
  boundary before the other four dispatch.
- **Nothing compressed.** Each section carries the specialist's full content: scoring
  rationale on every platform, `(source: ...)` on every field-specific marketing claim,
  the full pitch script with no placeholder brackets, the full comparables table, the
  filled-in handoff command.
- No "Generation notes" footer at all, if nothing failed (it should be **absent**, not
  rendered empty or with "none").

**What failure looks like:** four sections; Pricing appearing before Marketing;
per-section classification headers; a section summarized down to a few bullets; a
"Generation notes" footer rendered with nothing in it.

### 4. Parallel execution (Wave 2)

**What to run:** the same combined run as test 3, watching the tool calls.

**What correct looks like:** after Positioning returns, the four Wave 2 specialists are
dispatched **in a single batch** — four sub-agent invocations issued together, not one
starting after the previous returns. In a transcript this looks like four tool calls in
one block.

**What failure looks like:** Shipping runs, returns, then Distribution starts, and so on
— that's Phase 5's parallel execution having regressed. Also a failure: all *five*
dispatched in one batch, which means the two-wave dependency was collapsed and the other
four never got Positioning's context block.

### 5. Failure-recovery contract

This is the hardest thing here to exercise, and the most important — it exists because a
real run deadlocked twice (`docs/design-review-2026-08.md` §1). Two ways to trigger it
deliberately:

**Option A — break a ref file path.** Temporarily rename a ref file a specialist depends
on, e.g. `mv refs/platform-scoring-methodology.md refs/_tmp.md`, then run a combined
guide. The Distribution Specialist should fail to load its knowledge.

**Option B — interrupt a specialist mid-run.** Less deterministic but closer to the real
failure: cancel a running specialist sub-agent while a combined run is in flight.

**What correct looks like** (either way):

1. The orchestrator **says out loud** that the specialist failed and that it's retrying
   once — "Distribution Specialist returned nothing, retrying once."
2. On the second failure, it produces that section **itself** from the remaining ref
   files, rather than waiting.
3. The finished `GTM_GUIDE.md` has **all five sections present** and ends with a
   **"Generation notes"** footer naming the fallen-back section, what failed, which ref
   files it was built from, and the re-run invocation.
4. For a fallback in one of the three live-search sections, the footer additionally says
   the section is un-searched: no namespace status or named competitors for Positioning,
   no comparables table for Pricing, no `(source: ...)` claims for Marketing. **A
   fallback section that quotes a source is a fabrication** — that's the specific thing
   to look for.
5. If **Positioning** was the one that failed, the footer also states that the other four
   sections ran without positioning context, and Wave 2 still ran.

**What failure looks like:** the run hangs waiting for a return signal (the original
defect); the guide is written with only four sections and no explanation; a fallback
section appears with no footer disclosure; or a fallback Positioning/Pricing section
confidently asserts a namespace status or a competitor's price it never searched for.

**Restore the ref file afterwards** — `git status` should be clean of that rename before
you move on.

### 6. Refresh mode

**What to run** — three steps, in order:

1. Produce a fresh combined guide for a target that's missing something observable:
   ```
   @gtm-agent produce a go-to-market guide for ../mediaContentAgent
   ```
   (`mediaContentAgent` is a good fixture: at last check it had no `README.md`, no
   `LICENSE`, and no git repo — three things the Shipping section will flag.)
2. **Change one observable thing** in the target — add a `LICENSE` file, or run
   `git init`, or add the missing `README.md`.
3. Refresh:
   ```
   @gtm-agent refresh ../mediaContentAgent/GTM_GUIDE.md
   ```

**What correct looks like:**

- A **"What changed since &lt;date&gt;"** block at the top, below the classification line,
  and the date is the **prior guide's** date, not today's.
- It names **that specific delta** — "`LICENSE` now exists (MIT), so the Shipping
  section's blocking item is cleared" — and nothing invented around it.
- The body below the block is a **full guide**, not a diff — it still stands alone.
- Positioning, Marketing and Pricing all **re-searched fresh** (visible in their
  reasoning), even if their findings came back the same.

**Then run it again with nothing changed.** Correct output: the block contains exactly
one line saying nothing material changed, naming what was re-checked (project state, plus
the three fresh searches). That is the *preferred* answer, not a failed run.

**What failure looks like:** a "what changed" list padded with rewordings of unchanged
content; a delta the project state doesn't actually support; today's date in the header
instead of the prior guide's; a refresh that reuses the prior guide's search findings
instead of re-searching; or a file that's been reduced to just a changelog.

### 7. Positioning Specialist

**What to run:**

```
@gtm-agent produce a positioning guide for ../code-mapper
```

**What correct looks like:**

- `POSITIONING_GUIDE.md` in the target's root, with the classification header.
- The namespace check **names real colliding projects** — a specific GitHub repo or a
  specific PyPI package, with `(source: ...)`. This is the tell that the live search
  actually ran; a namespace section with statuses and no named projects means it didn't.
- Anything unconfirmed says **"not verified"** rather than "clear."
- The one-liner section **quotes the README's current line verbatim** next to the refined
  one.
- The competitor table has 3-5 **real, named, searched** alternatives, and rows drawn
  from the target user rather than from `code-mapper`'s own feature list.
- **Every differentiator carries a defensible-or-merely-true call** with a structural
  reason. (`code-mapper`'s headline "78% token reduction" should come out *merely true* —
  it's an efficiency number a competitor can match. If everything reads "defensible,"
  the test wasn't applied.)
- A **"Who This Is NOT For"** section naming real, plausible audiences with somewhere
  else to send them.
- If a collision was found, it's stated as a **finding with three options**, never as
  "you should rename this."

**What failure looks like:** namespace statuses with no named projects or no sources; a
refined one-liner shown without the original; a comparison table scored on the project's
own features; missing or blanket defensible calls; no "not for" section; a rename
instruction.

### 8. Pricing Specialist

**What to run:**

```
@gtm-agent produce a pricing guide for ../LegalAgent
```

**What correct looks like:**

- `PRICING_GUIDE.md` in the target's root, with the classification header.
- A **license recommendation with its tradeoff stated** and the project's own stated goal
  named (with where it was found) — not a survey of every license, not "you must use X."
- If it touches dual licensing, trademark, or CLA/DCO: a **"confirm with counsel"** note
  attached to that specific recommendation, not a blanket preamble.
- Comparables that are **real, named, current, and attributed** `(source: ...)`, chosen
  by same-buyer rather than same-technology, with any non-transferable pricing
  (VC-subsidized, enterprise-behind-a-sales-call, loss-leader) explicitly flagged.
- Every price given as a **range with reasoning**, never a single number stated as fact.
- A **concrete handoff block**: a filled-in `python PaymentAgent/scaffold.py --provider
  … --stack … --db …` with no placeholders and only valid flag values, *or*
  `@payment-setup-agent` with a stated reason the provider is genuinely undecided, *or*
  `@donation-specialist` if the recommendation was stay-free.
- Nothing executed — no scaffold run, no `LICENSE` written into the target.

**What failure looks like:** a license lecture instead of a recommendation; a
recommendation with no tradeoff; unattributed or stale prices; a hard number ("charge
$19/month"); a handoff with `<placeholder>` flags or an invalid provider/stack/db value;
a guaranteed-revenue claim; or the agent actually running the scaffold command.

### 9. Guide-only boundary

**What to check**, after every test above — this is the one thing worth verifying on
every single run, because it's the boundary the whole agent is built around.

**What correct looks like:**

- No account was created anywhere.
- Nothing was deployed, submitted, posted, or published.
- No name, domain, or trademark was registered.
- No payment provider was configured and no `scaffold.py` was executed.
- **Files written only to the target project's own root** (or the explicit output path
  you gave) — check with `git status` in both `GTM_Agent/` and the target. Nothing should
  have been written into `GTM_Agent/` by a run against another project, and nothing
  outside the target's root by a run against it.

**What failure looks like:** any of the above happening, or stray files appearing outside
the target — both are hard failures, not stylistic problems.

### 10. Quality self-check

**What to check:** the orchestrator's final report.

**What correct looks like:** it states that it checked the assembled guide against
`refs/guide-quality-checklist.md`, and in combined mode that means "All guides" plus all
five section lists plus "Combined mode" (plus "Refresh mode" on a refresh). Standalone
specialists report checking their own section's list only.

**What failure looks like:** no mention of the checklist; or — worse — the checklist
mentioned *and* a known-failing item reported as a caveat rather than fixed. The
instruction is explicit that a failing item gets fixed and re-checked, never disclosed
and shipped. The one legitimate exception is a disclosed fallback section, which the
checklist itself carves out.

---

## Quick Reference

```
# Combined guide (default) — five sections, two waves
@gtm-agent produce a go-to-market guide for <path-to-project>

# One guide only
@gtm-agent produce a positioning guide for <path-to-project>
@gtm-agent produce just a shipping guide for <path-to-project>
@gtm-agent produce a distribution guide for <path-to-project>
@gtm-agent produce a marketing plan for <path-to-project>
@gtm-agent produce a pricing guide for <path-to-project>

# Non-default input files
@gtm-agent produce a shipping guide for <path>, using <file1> and <file2> instead

# Refresh an existing guide — reports what changed since it was written
@gtm-agent refresh <path-to-project>/GTM_GUIDE.md

# Maintenance: validate the platform registry after editing platforms/*.yaml
../.venv/bin/python lib/validate_platforms.py

# Verifying a change by hand? Part 6 above is the manual-test procedure — start with
# test 0 (the subagent-cache quirk), which otherwise makes every other test misleading.
```

Output files land in the **target project's own root**, not inside `GTM_Agent/` —
except when you run GTM_Agent against itself, in which case both are the same
directory (see `docs/GTM_GUIDE.md` for a real worked example of the agent's own
output, produced during its Phase 4 dogfood pass).
