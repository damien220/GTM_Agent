# GTM_Agent — Design Review (2026-08)

Written 2026-08-27, after the first real external dogfood run (`A_OpenClaw`, a
project outside the `Dev_Agents` portfolio). GTM_Agent is "Phase 1–4 complete";
this review asks what's still missing, what could be faster, and whether the
three guides (Shipping / Distribution / Marketing) are the right set.

Companion to `plan.md` — that file is the build record; this one is the
forward-looking critique. Nothing here is committed roadmap yet.

---

## 1. Context: what the A_OpenClaw run exposed

The run succeeded (a complete, accurate `GTM_GUIDE.md` was produced) but two
things went wrong along the way, and one output pattern stood out:

- **The orchestrator deadlocked twice.** The Distribution Specialist sub-agent
  crashed mid-output; the orchestrator then parked between turns waiting for a
  return signal that never came. A human had to notice, kill a stale watcher,
  and hand-drive the recovery (re-run the specialist, then stitch).
- **The single highest-value finding was a positioning call**, not a
  shipping/distribution/marketing one: "your name collides with a 350k-star
  project in your exact niche — position *against* it, here is the one-sentence
  position." That only surfaced because the Marketing Specialist's live search
  happened to hit it. Nothing in the agent's design guarantees a positioning
  pass.
- Every guide the agent has ever produced ends, in effect, with "now go write
  all the actual launch assets yourself."

---

## 2. What's missing from the implementation

### 2.1 No repeatable test / validation harness — biggest gap

`plan.md §7` planned validation "closer to `docs-builder`'s quality-review
model than `validate_report.py`'s schema check." It was never built. Every
sibling agent in the repo has a real one (`LegalAgent`: 44 tests + 12
hand-labeled fixtures; `CI_CD_agent`: 46 tests). GTM_Agent's entire validation
history is manual dry-runs performed during the build — none of it is
repeatable, so there is no regression guard against a ref-file or YAML edit
silently degrading output.

- **Minimum viable:** `refs/guide-quality-checklist.md` that the orchestrator
  (and each standalone specialist) self-checks against in its report step —
  classification header present, every distribution recommendation carries a
  score, no platform outside the classified `category_fit`, every
  field-specific marketing claim attributed, no placeholder brackets in the
  pitch script.
- **Better:** a `test/` directory with 3–4 hand-labeled fixture classifications
  (drawn from real projects) plus property assertions on the produced guides,
  matching `LegalAgent`'s fixture approach adapted for prose output.

### 2.2 No `platforms/*.yaml` schema validator

The schema is documented (`platform-scoring-methodology.md` → "Platform YAML
schema") but nothing enforces it. A missing `reach_rating`, a malformed
`category_fit` list, or a typo'd `time_to_value` value silently breaks scoring
on the next run. A ~30-line `lib/validate_platforms.py` (or a documented
one-liner) closes this, and becomes the natural regression guard as the
registry grows past 12 files.

### 2.3 Combined mode has no failure-recovery contract

Observed twice in one run (§1). `gtm-agent.md` Steps 4–5 assume every specialist
returns usable content. When one doesn't, the orchestrator has no defined
behavior and stalls.

Required contract:

1. If a specialist doesn't return usable content, **retry once**.
2. If it fails again, **produce that section directly** from the specialist's
   own ref files (`deployment-patterns.md` / `platform-scoring-methodology.md` +
   `platforms/*.yaml` / `pitch-and-outreach.md`).
3. **Always note the fallback** in the `GTM_GUIDE.md` footer, naming which
   section was produced by fallback and why.

This must land **before** any move to run specialists in parallel (§3.1) —
parallelism widens this failure window.

### 2.4 No "refresh / diff an existing guide" mode

Every run regenerates from scratch. Marketing content in particular goes stale
in weeks — the A_OpenClaw guide's own text flags a marketplace fact that "would
be actively wrong by the time it goes stale." A mode that takes an existing
`GTM_GUIDE.md` / `MARKETING_PLAN.md`, re-runs against current project state and
a fresh search, and reports **what changed** would make the agent useful
repeatedly on one project instead of once.

### 2.5 `deployment-patterns.md §8` (hosted AI-agent service) is thin

~6 lines, versus ~34 for §9's Claude Code agent case. The portfolio now has
real-runtime agents (`A_OpenClaw`; `CI_CD_agent`'s Flask service). The
hosted-agent path — container registry, persistent host, secrets management,
health checks, the handoff to `CI_CD_agent` for the pipeline — deserves parity
with the Claude Code section.

### 2.6 No commercial-model coverage

The repo's stated purpose (`Dev_Agents/plan.md`) is that these projects get
"sold, licensed, or donated." The Shipping Guide *notices* a missing `LICENSE`
but offers no help choosing one; the Marketing pitch script assumes the ask is
already decided. See §4.B.

### 2.7 `platforms/` untested outside two categories

SaaS / game / mobile / API YAML entries exist but the portfolio has no fixture
to exercise them. Honestly flagged in `plan.md §8/§9`; restated here as a
standing limitation, not a fabricated pass.

### 2.8 Marketing's live-search volume is unbounded

The A_OpenClaw run made seven searches for one section. Not wrong, but there is
no guidance on when enough is enough, and a pathological case would be much
worse. See §3.4.

---

## 3. Efficiency

### 3.1 Run the three specialists in parallel, not sequentially

They are fully independent: same classification block in, no cross-dependencies,
each returns one section. `gtm-agent.md` currently runs them "in sequence."
Parallel execution is roughly a 3× wall-clock improvement, with Marketing's
live-search latency as the natural long pole.

**Blocked on §2.3** — the deadlock in §1 happened *because* a parallel child
crashed. Recovery handling first, then parallelism.

### 3.2 Pass file contents, not paths, to the specialists

`gtm-agent.md` Step 4 hands each specialist "the same input files." Each then
re-reads the target's `README.md` / `plan.md` / `CLAUDE.md` — which the
orchestrator already read during classification and still has in context.
Passing the contents eliminates 3× redundant reads per run.

### 3.3 Model tiering

Already a documented repo convention (`Dev_Agents/CLAUDE.md`, CI_CD_agent
section). Nothing in GTM_Agent specifies it; the whole run executes at one
tier.

| Stage | Suggested tier | Why |
|---|---|---|
| Classification | Haiku | Bounded extraction from a few docs against a fixed rubric |
| Shipping, Distribution | Sonnet | Ref-file-bounded reasoning, no open-ended synthesis |
| Marketing | Top model | Live-search synthesis + a written, non-template pitch script |

### 3.4 Cap and shape Marketing's searches

In `pitch-and-outreach.md`: 2 baseline searches (field survey + a targeted
"why now" angle), plus up to 2 optional (a named-competitor pattern, current
channel effectiveness) — rather than open-ended.

### 3.5 Generate a `platforms/index.yaml`

A digest (`id`, `display_name`, `category_fit`, `reach_rating`,
`effort_rating`) lets the Distribution Specialist filter by category first and
deep-read only the 4–8 matching files instead of all 12. Marginal today;
compounds as the registry grows.

---

## 4. Are the three guides enough?

**Shipping → Distribution → Marketing** is a coherent arc (ship it → list it →
sustain attention) and a defensible MVP. But there are two real gaps *inside*
the "get a finished project in front of users" scope, both with evidence from
the A_OpenClaw run. Both fit the existing orchestrator + specialist pattern
with **no architectural change** — each is one new specialist plus one ref
file.

### 4.A Positioning / Messaging guide — recommend building, highest leverage

The most valuable output of the A_OpenClaw run was a positioning call (§1), and
it surfaced only by luck. Positioning is neither shipping, nor distribution, nor
ongoing-marketing-cadence — it is message–market fit, and it logically comes
**first**, feeding the other three.

A `positioning-specialist`, run before the others, would produce:

- a namespace / collision check (GitHub, PyPI, npm, domain) — the A_OpenClaw
  case is the archetype
- the refined one-liner / elevator pitch
- a competitor comparison table, and an explicit call on which differentiators
  are **defensible** versus merely true
- the "who is this *not* for" boundary

It needs live `WebSearch` (like Marketing) for the competitor and namespace
checks. In combined mode its output becomes a short "Positioning" section at the
top of `GTM_GUIDE.md` and is passed as context into the other three
specialists.

### 4.B Pricing & Packaging guide — recommend building, PaymentAgent bridge

Serves the repo's "sold, licensed, or donated" thesis directly, and is the
natural handoff to the sibling `PaymentAgent` (mirroring Shipping → CI_CD_agent).

A `pricing-specialist` would produce:

- license selection (MIT vs Apache-2 vs AGPL vs dual / commercial), reasoned
  against the project's goal
- free vs paid tiers, the open-core boundary, one-time vs subscription
- "what comparable tools charge" — live-search-grounded, exactly like Marketing
- an explicit handoff block: which `PaymentAgent` invocation to run next

Also needs live `WebSearch`.

### 4.C Not a separate guide: launch-asset generation

The gap is real — every guide ends with "now write all the assets yourself"
(demo-video script, Show HN title + first comment, Product Hunt tagline, launch
tweet). But the knowledge already lives in `ContentPost_agent` (post formatting)
and `mediaContentAgent` (media). The right fix is to **build the handoffs
`plan.md §4` keeps deferring** — contract-only, JSON, no shared code, the same
shape as `mediaContentAgent → ProdReel` — not a fourth standalone specialist.

### 4.D Explicitly out of scope

- Community / support infrastructure setup (Discord, issue templates,
  `CONTRIBUTING.md`) → fold into `presentation-standards.md`, don't make it a
  guide.
- Analytics / metrics instrumentation → post-launch, adjacent to but outside
  "get it in front of users."
- Full investor / fundraising deck → the pitch script covers the "backer" case
  at the depth this agent should go.

---

## 5. Suggested priority order

> **Status as of 2026-08-29 — all 6 items implemented.** The priority order
> below was written before implementation and is left as-written for the record;
> what actually happened is in §6. In short, the order was not followed: the
> efficiency pass (item 4) and the §2.2/§2.4/§2.5 tail (item 6) landed *before*
> the positioning guide (item 3) and the pricing guide (item 5), because
> everything in items 1, 2, 4 and 6 was a fix to existing files while §4.A/§4.B
> were new specialists — so the work split into a hardening pass and then an
> expansion pass rather than descending this list. Full build record: `plan.md`
> §8 "Phase 5 — Post-review hardening (2026-08-29)" and "Phase 6 — Positioning &
> Pricing specialists (2026-08-29)".

1. **§2.3 failure-recovery contract** — it is a live defect, not a nice-to-have.
2. **§2.1 quality checklist** (the minimum-viable form) — cheapest durable
   quality guard.
3. **§4.A Positioning guide** — proven need, feeds the other three.
4. **§3.1–3.3 efficiency pass** (parallel + pass-contents + model tiering),
   done together, after §2.3.
5. **§4.B Pricing guide** — serves the commercial goal, clean PaymentAgent
   handoff.
6. **§2.2 YAML validator**, **§2.5 §8 expansion**, **§2.4 refresh mode** — as
   capacity allows.

Items in §4.C / §4.D and the `platforms/` category expansion (§2.7) stay
deferred until a real project demonstrates the need — consistent with
`plan.md §8`'s "don't design for hypothetical future requirements."

---

## 6. Status (2026-08-29)

Implemented across two passes on the same day: the post-review **hardening pass**
(Phase 5) and the **two-specialist expansion** (Phase 6). Per-item detail — what
was built, where, and why — is in `plan.md` §8 "Phase 5" and "Phase 6"; this
table is the index. **All nine numbered items in §2/§3 and both recommended
specialists in §4 are now built.**

| Item | Status | Landed as |
|---|---|---|
| §2.1 quality checklist | **Done** (minimum-viable form) | `refs/guide-quality-checklist.md`; self-checked by `gtm-agent.md` Step 6 and each specialist's Report step. Phase 6 added its Positioning and Pricing section lists (five section lists total) |
| §2.2 YAML schema validator | **Done** | `lib/validate_platforms.py` — all 12 platform files pass unmodified |
| §2.3 failure-recovery contract | **Done** | `gtm-agent.md` Critical Rule 8 + Steps 4/5 + the "Generation notes" fallback footer |
| §2.4 refresh / diff mode | **Done** | `gtm-agent.md` Critical Rule 10 + Step 3b + "What changed since `<date>`" block; a "Refresh mode" step in each specialist |
| §2.5 `deployment-patterns.md §8` expansion | **Done** | §8 rewritten to parity with §9 — container path, secrets, health checks, `CI_CD_agent` handoff |
| §3.1 parallel specialists | **Done** | `gtm-agent.md` Step 4, one batch of tool calls — gated on §2.3, as this review required |
| §3.2 pass contents not paths | **Done** | `gtm-agent.md` Critical Rule 9 + each specialist's Inputs table and Step 1 |
| §3.3 model tiering | **Done** | `gtm-agent.md` "Model tiering" section + `model:` frontmatter (`sonnet`/`sonnet`/`opus`); orchestrator left unpinned on purpose |
| §3.4 cap Marketing's searches | **Done** | `refs/pitch-and-outreach.md` "Search budget" (2 baseline + up to 2 optional), referenced from `marketing-specialist.md` Step 2 |
| §4.A positioning specialist | **Done** (Phase 6) | `.claude/agents/positioning-specialist.md` + `refs/positioning-methodology.md`; runs as Wave 1 of `gtm-agent.md` Step 4, alone and first, returning both its section and a compact positioning context block passed into the other four specialists. Produces the namespace/collision check, the refined one-liner, the competitor table with a mandatory defensible-vs-merely-true call, and the "who this is NOT for" boundary |
| §4.B pricing & packaging specialist | **Done** (Phase 6) | `.claude/agents/pricing-specialist.md` + `refs/pricing-and-licensing.md`; Wave 2, last section of the combined guide. License recommendation with its tradeoff, free-vs-paid/open-core boundary, live-searched comparables with non-transferable pricing flagged, and a concrete `PaymentAgent` `scaffold.py` / `@payment-setup-agent` / `@donation-specialist` handoff block — named, never run |
| §2.6 commercial-model coverage | **Done** (Phase 6) | Same item as §4.B above |

**Still open, deliberately:**

- **§2.1's "better" option** — a `test/` fixture directory with property
  assertions. The checklist is the floor, not the ceiling.
- **§3.5 `platforms/index.yaml`** — not built. Marginal at 12 files by this
  review's own assessment, and §2.2's validator delivered the more valuable half
  of the same concern (a real regression guard on the registry). Revisit if the
  registry grows well past 12.
- **§2.7 `platforms/` untested outside two categories** — unchanged and not
  fixable from inside this repo; needs a real SaaS/game/mobile/API fixture.
- **§2.8** — closed by §3.4 above.
- **§2.6** — closed by §4.B in Phase 6; see the table.
- **§4.C / §4.D** — unchanged, still deferred on the same reasoning. §4.C's
  argument is if anything stronger now: Phase 6's Pricing Specialist ends its
  guide with a *named, runnable* handoff to a sibling tool, which is exactly the
  shape §4.C proposes for the launch-asset gap — the `ContentPost_agent` /
  `mediaContentAgent` handoffs, not a sixth standalone specialist. Still gated
  on a demonstrated need per `plan.md` §8's Phase 4 decision.

**Not yet validated by a real run.** Everything above is implemented and
internally consistent, but the next combined-mode run against a live target is
the actual test of two-wave execution, the positioning context handoff, and the
fallback path — treat it as one. `docs/HowTo.md` **Part 6 — Manual Testing** is
the concrete procedure for doing so.
