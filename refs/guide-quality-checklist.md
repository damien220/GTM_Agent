# Guide Quality Checklist

The self-check every GTM_Agent output passes before it is reported as done. This
is the minimum-viable form of the validation harness `docs/plan.md §7` planned
and never built (`docs/design-review-2026-08.md §2.1`): GTM_Agent's output is
prose, so there is no `validate_report.py`-style schema check to run against it —
what there *can* be is a fixed list of failure modes already observed in real
runs, checked deliberately rather than hoped for.

Load this file when: you are about to report a finished guide — `gtm-agent.md`
Step 6 (against every section it assembled), or a specialist's own Report step
(against its own section's items only). Not before drafting; this is a gate, not
a template.

## How to use this file

Walk the applicable sections below and check each item against the text you are
about to hand over. **If an item fails, fix the guide and re-check — do not
report the guide as done with a known failing item, and do not report the
failure as a caveat instead of fixing it.** The one exception is a fallback-
produced section (see "Combined mode" below), where the degradation is disclosed
in the footer by design rather than repaired in place.

Check only the sections that apply to what you actually produced: a standalone
`DISTRIBUTION_GUIDE.md` run checks "All guides" + "Distribution"; a combined
`GTM_GUIDE.md` run checks "All guides" + **all five** section lists
(Positioning, Shipping, Distribution, Marketing, Pricing) + "Combined mode"; any
refresh-mode run adds "Refresh mode" on top of whichever of the above applies.

## All guides

- [ ] **Classification header present**, and it matches the run's actual
      classification block verbatim (category, secondary tag if any, stack,
      maturity, target_user) — not a re-worded or rounded-up restatement.
- [ ] **No contradictory classification anywhere in the body.** No section's
      prose implies a different category, stack, or maturity than the header
      states (e.g. a Shipping section describing a hosted runtime under a
      "Claude Code agent, no hosted runtime" header). In combined mode this is a
      correctness bug per `gtm-agent.md` Critical Rule 3, not a style nit.
- [ ] **Maturity not rounded up.** Recommendations are framed at the classified
      maturity stage, not the one the target's own README aspires to
      (`project-classification.md` Dimension 3's "do not round up").
- [ ] **Guide-only.** Nothing in the text reads as an action already taken on
      the user's behalf ("submitted to", "deployed to", "posted"). Every step is
      phrased as something the user executes.
- [ ] **No unresolved placeholder text** anywhere — no `<...>`, `[TODO]`,
      `[your project]`, or template scaffolding left from the Deliverables
      shapes.

## Positioning section

- [ ] **Classification header present**, and the comparison table's dimensions
      were drawn from the classified `target_user` rather than from this
      project's own feature list (`positioning-methodology.md` §3). A table
      scored on your own features is won by construction and says nothing.
- [ ] **Every namespace status and every named competitor is attributed
      inline** with `(source: ...)` from an actual live search
      (`positioning-specialist.md` Critical Rule 3). Anything that couldn't be
      confirmed says **"not verified"** — never rounded to "clear," which is
      wrong in exactly the expensive direction.
- [ ] **Every taken/crowded namespace names the specific colliding project.**
      "Taken" with no name is one search short of being actionable.
- [ ] **A defensible-vs-merely-true call is present for every differentiator**,
      each with the structural reason behind it
      (`positioning-methodology.md` §4). Missing calls, or a table where every
      row reads "defensible," means the test wasn't actually applied.
- [ ] **A "who this is NOT for" boundary is present and excludes a real,
      plausible audience** — someone who would genuinely land on this project —
      with where they should go instead. "Not for people who don't need it" is
      not a boundary.
- [ ] **A name collision is stated as a finding with options** (position
      against / differentiate the name / accept the overlap), each with its
      tradeoff — never as an instruction to rename
      (`positioning-specialist.md` Critical Rule 5).
- [ ] **The refined one-liner is shown alongside the project's current one**,
      quoted verbatim (or "the README states none"), with one or two lines
      saying what changed. A refinement shown alone is unverifiable.
- [ ] **No trademark reasoning anywhere.** A namespace check is not a trademark
      search; where the question arises it is named and handed to counsel
      (`positioning-methodology.md` §6).

## Shipping section

- [ ] **Exactly one primary deployment path**, plus at most one alternative with
      a one-line tradeoff (`deployment-patterns.md`'s Output format,
      `shipping-specialist.md` Critical Rule 7) — not a survey of every host the
      ref file mentions.
- [ ] **A Claude Code agent-stack target received no hosting-provider
      recommendation** (`deployment-patterns.md §9`,
      `shipping-specialist.md` Critical Rule 6). This is the single most
      identifiable failure this specialist can produce against this repo's own
      fixtures.
- [ ] **Every dual-artifact project got a deployment step per artifact** — if
      the project ships both a standalone script/CLI and an agent definition,
      neither was silently dropped (`deployment-patterns.md`'s dual-artifact
      note).
- [ ] **Only genuinely-missing presentation items are marked `[missing]`** — no
      item the target actually has is flagged, and satisfied items are marked
      `[present]` without elaboration (`presentation-standards.md`'s "How to use
      this file").
- [ ] **Every stack claim traces to something actually observed** in the
      target's files — no invented manifest, framework, or directory.

## Distribution section

- [ ] **Every recommended platform shows its scoring dimensions** — reach,
      audience fit, effort, and time-to-value, per
      `platform-scoring-methodology.md`'s Output format. A bare ranked list with
      no "why" is a failed output, not a terse one.
- [ ] **No platform outside the classified `category_fit`** appears at all —
      excluded, not shown with a low score
      (`platform-scoring-methodology.md`'s "Excluding non-fits"). Check against
      both the primary and secondary category tags.
- [ ] **No platform with an unmet prerequisite appears in "Ready Now."** The
      prerequisite override beats the composite score every time
      (`platform-scoring-methodology.md`'s override rule) — Product Hunt ranking
      highest on numbers is not a reason to promote it out of Blocked.
- [ ] **Every Blocked entry names the specific unmet prerequisite** and how to
      satisfy it, and cross-platform dependencies are stated where a Ready Now
      platform's own output would satisfy a Blocked one's prerequisite.
- [ ] **Operator-preparation prerequisites are phrased as "you'll need to do X
      first,"** not as a defect in the project
      (`platform-scoring-methodology.md`'s two-kinds-of-prerequisite note).
- [ ] **`niche-communities.yaml` was instantiated, not restated** — 2-3 real,
      field-specific communities named for this project, never the generic
      pattern text.
- [ ] **Every platform named exists in `platforms/*.yaml`** — no invented
      channel, and no composite score computed from remembered rather than
      actual YAML values.

## Marketing section

- [ ] **Every field-specific claim carries `(source: ...)` or
      `(general practice)`** inline (`pitch-and-outreach.md`'s Output format).
      An unattributed specific claim is a fabricated-authority problem, not a
      formatting lapse.
- [ ] **Every cited stat's measured population matches the classified
      `target_user`** — a stat about enterprise buyers does not support a claim
      about solo developers even when the topic matches
      (`pitch-and-outreach.md`'s scope-matching rule). If it doesn't match, it
      is qualified explicitly or dropped.
- [ ] **The pitch script is fully written with no placeholder brackets** and is
      specific to this project — all five parts (hook, why now, what it is,
      proof, the ask) filled in, per `pitch-and-outreach.md`'s script structure.
- [ ] **"Why now" cites an actual search finding**, not the durable framework
      wearing a citation's clothes.
- [ ] **Proof matches actual maturity** — no fabricated traction, users, or
      adoption numbers for a project that has none.
- [ ] **No guaranteed-outcome language** anywhere ("this will get you X users")
      — every recommendation is framed as "worth trying because X"
      (`marketing-specialist.md` Critical Rule 5).
- [ ] **The field-specific-vs-generic summary paragraph is present** and
      actually distinguishes the two rather than restating the plan.

## Pricing section

- [ ] **The license recommendation names one license, gives 2-3 reasons tied to
      the project's own stated goal, and states the main tradeoff it accepts** —
      a recommendation, never a mandate, and never a survey of every license
      (`pricing-specialist.md` Critical Rule 6, `pricing-and-licensing.md` §1).
- [ ] **The stated goal the license was reasoned against is named, with where
      it was found** — a recommendation whose premise is invisible can't be
      argued with.
- [ ] **Every comparable's pricing figure is attributed inline
      `(source: ...)` and current**, with "not confirmed" used honestly where it
      couldn't be verified (`pricing-specialist.md` Critical Rule 4). A
      remembered price presented as current is a fabricated-authority problem
      with a number attached.
- [ ] **Non-transferable comparables are flagged** — VC-subsidized pricing an
      indie can't match, enterprise pricing behind a sales call, a loss-leader
      attached to a larger product (`pricing-and-licensing.md` §3).
- [ ] **Every price is a range with its reasoning, never a hard number stated
      as fact** (`pricing-specialist.md` Critical Rule 5).
- [ ] **Legal- and finance-adjacent matters carry a "confirm with counsel / an
      accountant" note attached to the specific recommendation that raises
      them** — dual licensing, trademark, CLA/DCO, tax treatment — not as a
      blanket preamble (`pricing-specialist.md` Critical Rule 3).
- [ ] **The handoff block is present and concrete** — a filled-in
      `python PaymentAgent/scaffold.py …` command with no placeholders and only
      valid flag values, or `@payment-setup-agent` with a stated reason the
      provider is genuinely undecided, or `@donation-specialist` for a
      stay-free/donation-only recommendation. "Set up payments" left unassigned
      is a failed handoff (`pricing-and-licensing.md` §4).
- [ ] **Nothing was executed** — no scaffold run, no license file written, no
      provider configured. The guide names the command; the user runs it.
- [ ] **No guaranteed revenue or conversion language** anywhere, and the
      recommendation matches the classified maturity rather than assuming a
      pre-shipped project should take payments this week.

## Combined mode

- [ ] **All five sections are present, in the Positioning → Shipping →
      Distribution → Marketing → Pricing order, and carry each specialist's full
      content** — nothing compressed, summarized, or dropped in the stitch
      (`gtm-agent.md` Critical Rule 7).
- [ ] **One shared classification header, no per-section duplicates** that could
      drift from it.
- [ ] **Fallback footer present and accurate.** If any section was produced by
      orchestrator fallback (`gtm-agent.md` Critical Rule 8), the footer names
      that section, says why, states which ref files it was built from, and — for
      the three live-search sections (Positioning, Marketing, Pricing) — states
      plainly that the section is un-searched framework only: for Positioning
      that its namespace and competitor checks were **not performed**, for
      Pricing that it carries **no comparable prices**. If Positioning fell back,
      the footer also says the other four sections ran **without positioning
      context** (`gtm-agent.md` Critical Rule 8.4). If no fallback occurred, the
      footer is absent entirely, not rendered empty or with a "none"
      placeholder.
- [ ] **A fallback-produced section is not silently held to the full bar.** It
      still meets its own section's checklist items *except* the ones that
      structurally require the missing capability (the `(source: ...)`
      attributions in Positioning, Marketing and Pricing above all) — those are
      disclosed in the footer, not faked. A fallback Positioning section
      asserting a namespace status, or a fallback Pricing section quoting a
      comparable's price, is a fabrication, not a degraded section.

## Refresh mode

- [ ] **The "What changed since `<date>`" block is present** at the top of the
      refreshed guide, and the date is the prior guide's actual date, not
      today's.
- [ ] **Every listed change traces to a real delta** — an observed change in the
      target project's current state (a prerequisite now met, a file that now
      exists, a maturity change) or a genuinely different live-search result.
      No change invented to make the refresh look productive
      (`gtm-agent.md` Critical Rule 10).
- [ ] **"Nothing material changed" is stated plainly when true**, rather than
      padded with cosmetic rewording presented as movement.
- [ ] **Changes are concrete, not directional** — "Product Hunt moved from
      Blocked to Ready Now: the demo URL its prerequisite wanted now exists",
      not "distribution outlook improved."
- [ ] **The refreshed body is a full guide, not a diff.** The "What changed"
      block is a header on top of complete content, so the file still stands
      alone for a reader who never saw the prior version.
