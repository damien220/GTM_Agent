# Pitch and Outreach

Defines the durable, structural half of `MARKETING_PLAN.md`'s trust-building and
pitch-script sections — the parts of "how to run outreach" that don't change
month to month. The other half, "what's currently working in this specific
field," is `marketing-specialist`'s live `WebSearch` job, not this file's — see
"Division of labor" below for the hard line between the two.

Load this file when: writing the trust-building/outreach-cadence section or the
pitch/meeting script section of `MARKETING_PLAN.md`.

## Division of labor: this file vs. live search

This file holds the **structural skeleton** — what makes any pitch, outreach
message, or trust-building cadence effective in general (clarity, social proof,
a specific ask). The live search's job is **current, field-specific
substance** — which channels/tactics are actually working right now for this
project's classified category and field. `marketing-specialist` must never
present this file's general framework as if it were a live-search finding, and
must never present a live-search finding as more universal than it is. State
plainly in the guide which parts come from this file (durable structure) versus
the search (current, field-specific) — per `docs/plan.md` §6's Critical Rule that
the guide "should note when a tactic is field-specific vs. generic."

## Search budget: 2 baseline + up to 2 optional

The live search is `marketing-specialist`'s job, but *how much* of it is enough
is a durable question, so it belongs here rather than being re-decided each run.
Cap a normal run at four searches:

**Baseline (always run both):**
1. **Field survey** — current marketing/outreach practice for the classified
   category and field ("developer tool launch marketing 2026," "indie game
   marketing tactics 2026").
2. **The targeted "why now" angle** — the follow-up the script structure below
   requires, aimed at this project's own hook (a pricing gap, a cost shift, a
   named competitor pattern). The broad survey rarely produces one on its own.

**Optional (run only if a baseline left a specific gap):**
3. **A named-competitor pattern** — what a direct comparable actually did, when
   the pitch needs a concrete contrast rather than a trend.
4. **Current channel effectiveness** — which channels are working now for this
   field, when the Ongoing Strategy's cadence would otherwise be generic.

Stop at four. A real run made seven searches for one section
(`docs/design-review-2026-08.md` §2.8) — not wrong, but past the fourth the
marginal finding stops changing the plan, and an unbounded search loop is the
pathological case this cap exists to prevent. If four searches genuinely
produced no citable "why now," say so and fall back to this file's durable
framework labeled as general practice — never keep searching until something
usable turns up, and never pad the gap with invented specifics (see the
Disclaimer posture below).

## Trust-building tactics (durable framework)

- **Social proof ladder, matched to actual maturity** (from
  `project-classification.md`'s maturity dimension — never overstate this):
  - No users yet → lean on the maker's own credibility and the clarity of the
    problem being solved, not fabricated social proof.
  - Early users → direct, attributed quotes and real (if small) usage numbers
    beat a vague "trusted by many."
  - Established → concrete before/after case studies with real metrics.
- **Transparency as a trust lever.** Being explicit about current limitations
  and maturity stage builds more credibility with a technical audience than
  overclaiming — especially relevant for a dev tool / CLI / API / AI agent
  audience, which tends to actively distrust polish that outruns substance.
- **Consistency over intensity.** A steady, honest update cadence outperforms
  one big launch burst followed by silence — this is the backbone of the
  "ongoing strategy" `docs/plan.md` §1 asks the Marketing Plan to describe, not a
  one-time push.
- **Community-first framing.** Genuine participation in a relevant community
  before making any ask — mirrors `niche-communities.yaml`'s own prerequisite
  ("enough standing to post without looking like a drive-by promoter").

## Outreach message structure (cold outreach template shape)

1. **Specific, personalized opening** — something real and specific about the
   recipient, never generic boilerplate ("I saw you're interested in X").
2. **One-sentence problem framing**, in the recipient's own likely language,
   not the maker's internal jargon.
3. **A concrete proof point** — a demo link, an early metric, a relevant
   credential. This is where a live-search-informed detail (a stat, a named
   trend) can strengthen the pitch, if genuinely found and cited.
4. **A specific, low-friction ask** — never "let me know what you think"; a
   scoped yes/no question ("worth a 15-minute call next week?").
5. **A clear identity/credibility signature** — who you are and why you're
   building this, briefly.

## Pitch / meeting script structure

A five-part skeleton `marketing-specialist` fills in **specifically** for the
classified project — never left as a fill-in-the-blank template in the final
output (Phase 3's acceptance bar explicitly requires this: "the pitch script is
specific to the classified project, not a template with blanks").

1. **Hook** — the problem, stated the way the target audience itself would
   state it, not the way the builder would.
2. **Why now** — a reason this matters currently, grounded in an actual
   live-search finding (a market shift, a named competitor gap, a stat) — this
   step fails outright if it isn't backed by a real citation from the search.
   A single broad field-survey search (e.g. "developer tool launch marketing
   2026") usually won't itself surface a strong, citable "why now" — run a
   second, more targeted follow-up search aimed specifically at this project's
   angle (a pricing gap, a cost/context-window shift, a named competitor
   pattern) rather than settling for whatever the general search happened to
   return.
3. **What it is** — one or two sentences, no feature list; tie directly to the
   classified `category` and `target_user`.
4. **Proof** — whatever credible signal exists at the project's *actual*
   maturity stage (never fabricate traction that doesn't exist).
5. **The ask** — scoped to who's being pitched: a buyer wants pricing/timeline,
   a backer wants milestones/market size, an early adopter wants access and a
   clear way to give feedback.

## Disclaimer posture (adapted from `LegalAgent/refs/upl-and-disclaimer-policy.md`)

Marketing and pitch guidance here is **tactical, not legal, financial, or PR
counsel** (`docs/plan.md` §4's non-goal) — the same posture `LegalAgent` takes
toward legal conclusions, adapted to this domain's actual risk:

- Never present a tactic as guaranteed to produce results — frame
  recommendations as "worth trying because X" not "this will get you Y users."
- Never state a market-size, competitor, or trend claim as fact unless it
  traces to an actual live-search result — attribute it explicitly ("per a
  2026 search on [topic], [finding]"), the same way `LegalAgent` requires a
  verbatim quote rather than a paraphrase for every finding. An unattributed
  claim in this domain is a fabricated-authority problem, not just weak
  writing.
- **An attribution must match the source's actual measured population, not
  just its topic.** Citing a real, correctly-quoted stat is not enough if its
  scope gets quietly broadened to fit the classified project's target
  audience — e.g. a stat about in-house enterprise legal teams' AI adoption
  does not support a claim about solo-practitioner demand, even when both are
  "legal AI" on the surface. Check the source's actual population/segment
  against `target_user` before using it as "why now" or market evidence, and
  if it doesn't match, either qualify it explicitly (state whose behavior it
  actually reflects) or don't use it.
- If the live search turns up nothing useful for a given angle, say so and
  fall back to this file's durable framework explicitly labeled as generic —
  never silently pad with invented specifics to make the section look
  complete.

## Output format

When `marketing-specialist` writes the relevant `MARKETING_PLAN.md` sections,
mark each claim's source inline where it isn't obvious from context — e.g.
`(source: [search result title/date])` for a live-search-grounded claim, or
"(general practice)" for something drawn from this file's durable framework.
This is what makes "cites what it found, not generic boilerplate" (Phase 3
acceptance) verifiable rather than an assertion.
