# Platform Scoring Methodology

Defines the platform YAML schema and the rubric `distribution-specialist` uses to
turn `platforms/*.yaml` entries into the **rated, prioritized** list required by
`DISTRIBUTION_GUIDE.md` (`plan.md` §1, §5, §6). This is the same shape as
`LegalAgent/refs/risk-scoring-methodology.md` scoring clause risk, applied to
launch channels instead: a fixed set of dimensions, a formula that combines
them, and an explicit rule for the one case where the formula alone gives the
wrong answer (there: a critical finding overriding the numeric score; here: an
unmet prerequisite overriding the numeric ranking).

Load this file when: computing which platforms apply to a classified project,
scoring them, or determining launch sequence.

## Platform YAML schema

Every file in `platforms/` is one platform, with these fields:

```yaml
id: product-hunt                  # kebab-case, matches filename
display_name: "Product Hunt"
url: "https://www.producthunt.com"
category_fit:                     # categories from project-classification.md this platform suits at all
  - "dev tool / library"
  - "SaaS / web app"
stack_fit_notes: >                # optional — stack-conditional caveats (e.g. needs a visitable URL)
  Needs something a visitor can actually try — a bare source repo undersells here.
audience: >
  One or two sentences on who's actually there and what they expect.
reach_rating: 5                   # 1–5: potential visibility/audience size if it goes well
effort_rating: 3                  # 1–5: setup/submission cost, independent of prerequisites
time_to_value: fast               # fast | medium | slow — how soon results become visible
prerequisites:                    # each a plain-language condition; empty list if none
  - "A live, visitable product or demo, not just a repo."
  - "3+ early testimonials or usage signals before launch day."
submission_workflow:              # ordered, concrete steps
  - "Create/find a hunter account."
  - "Prepare a tagline, image gallery, and maker's first comment."
notes: >                          # optional — anything the rubric can't capture as a field
  Free text for caveats that don't fit a structured field.
```

`category_fit` uses the exact category strings from
`project-classification.md`'s Dimension 1 list, so a classification block can be
matched against it with no translation step. A platform with an empty
`category_fit` for the classified project's category is **not scored at all** —
see "Excluding non-fits" below.

## Scoring dimensions

Scored **per classified project**, not as a fixed platform leaderboard — the
same platform can score very differently depending on what's being launched.

1. **Reach** (1–5) — `reach_rating` from the YAML, used as-is once category fit
   is confirmed. This is a static estimate of the platform's own audience size,
   not a promise of what this specific project will get.
2. **Effort** (1–5, lower is better) — `effort_rating` from the YAML,
   independent of whether prerequisites are currently met (that's handled
   separately — see Prerequisite Sequencing below, not folded into this number).
3. **Audience fit** (1–5) — compare the YAML's `audience` description against
   the classified project's `target_user` (from `project-classification.md`
   Dimension 4). A platform whose stated audience doesn't match the project's
   actual target user scores low here even if `category_fit` technically
   matches (e.g. a project for solo developers scores low audience fit on a
   platform whose audience is enterprise buyers).
4. **Time to value** — `time_to_value` from the YAML, kept qualitative
   (fast/medium/slow) rather than forced into the numeric composite: it answers
   a different question ("when do I see results") than the composite answers
   ("is this worth doing"), and collapsing it into one number would hide that
   distinction from the user.

## Composite score

```
composite = (reach * 0.4) + (audience_fit * 0.4) + ((6 - effort) * 0.2)
```

Reach and audience fit are weighted equally and highest, since a platform that
scores high on both is the actual point of distribution; effort is weighted
lowest and inverted (a 1-effort platform contributes more than a 5-effort one)
because effort is a real but secondary cost, not the goal. `time_to_value`
intentionally has no weight in the formula — carry it alongside the composite
score in the output instead (see Output Format), since "fast" vs. "slow" is
information the user needs, not a reason to rank one platform above another.

## Excluding non-fits

If the classified project's category isn't in a platform's `category_fit` list
at all, exclude that platform from the guide entirely — do not compute a low
score and show it anyway. A game classified project has no business being told
"npm scored low for you"; it should simply never appear.

## Prerequisite sequencing (the override rule)

**A platform's position in the composite-score ranking is not its position in
the launch sequence — prerequisites can force a reorder.** This mirrors
`risk-scoring-methodology.md`'s override rule (a critical finding always forces
at least a `high` label, regardless of the numeric score): here, an unmet
prerequisite always pushes a platform later in sequence, regardless of how high
it scored.

1. Compute the composite score for every category-fit-matched platform.
2. Split into two tiers:
   - **Ready now** — every item in `prerequisites` is already satisfied by what
     classification/the project's actual state shows (e.g. a live URL exists,
     testimonials exist).
   - **Blocked** — at least one prerequisite is unmet.

   Note the two different *kinds* of prerequisite this covers, since they read
   differently in the output: a **project-state** prerequisite is something
   verifiable from the project's own files/history (e.g.
   `package-registries.yaml`'s "actually published to the registry") — Blocked
   here signals a real gap in the project itself. An **operator-preparation**
   prerequisite is about the human running the launch, not the codebase (e.g.
   `niche-communities.yaml`'s "enough standing in the community," or
   `claude-code-plugin-marketplace.yaml`'s "already dogfooded") — this can
   never be confirmed "met" from project files alone, so it will land Blocked
   on effectively every run. That's correct behavior, not a bug, but phrase the
   guide's language accordingly: "you'll need to do X first" rather than
   something that reads as a defect in the project.
3. Sequence: all "ready now" platforms first, ordered by composite score
   descending, then "blocked" platforms, also ordered by composite score
   descending among themselves, each annotated with exactly which prerequisite
   is unmet and — where a "ready now" platform's own workflow would naturally
   satisfy it (e.g. testimonials gathered from an itch.io or Hacker News launch
   feeding into a later Product Hunt prerequisite) — note that dependency
   explicitly instead of treating the two platforms as unrelated.
4. Never present a "blocked" platform as launch-ready. State plainly what needs
   to happen first.

## Rating rationale requirement

Every platform in the output must show the dimension values it was scored on,
not a bare rank — per `plan.md` §6 Critical Rules ("every rated recommendation
must cite its scoring dimensions"). A ranked list with no "why" is not an
acceptable `distribution-specialist` output.

## Output format

For each recommended platform, in sequence order:

```
N. <display_name> — composite <score>/5 (reach <r>, audience fit <a>, effort <e>) · time to value: <fast/medium/slow>
   Why: <one line tying reach/audience fit back to this project's classification>
   Prerequisites: <met, or exactly what's missing and how to get there>
   First step: <first item from submission_workflow>
```

Followed by a **Blocked** section (if any) in the same format, clearly
separated so the user doesn't mistake a blocked platform for something to do
today.

## What this score is and isn't

This rubric ranks **static, YAML-encoded estimates** against a project's
classification — it is a starting sequencing aid, not live traffic data or a
guarantee of results. A platform's real-world effectiveness drifts over time
in ways this file can't track; grounding recommendations in *current* field-
specific practice is `marketing-specialist`'s job (Phase 3, via live
`WebSearch`), not this rubric's. Don't present a composite score with false
precision — it's a sequencing tool, not a prediction.

## Worked example

Project: a CLI dev tool, classified `category: CLI (secondary: dev tool /
library)`, `target_user: individual developers`, no testimonials yet, has a
GitHub repo but no separate landing page.

- **Hacker News (Show HN)** — reach 4, audience fit 5 (HN's audience is
  exactly "developers evaluating dev tools"), effort 2 → composite
  `(4*.4)+(5*.4)+((6-2)*.2) = 1.6+2.0+0.8 = 4.4`. No prerequisites. **Ready now.**
- **Package registry (npm/PyPI)** — reach 3, audience fit 4, effort 2 →
  composite `1.2+1.6+0.8 = 3.6`. No prerequisites beyond the package itself
  existing. **Ready now.**
- **Product Hunt** — reach 5, audience fit 3 (PH skews toward SaaS/consumer
  products more than raw CLIs), effort 3 → composite `2.0+1.2+0.6 = 3.8`, but
  prerequisites (live/visitable demo, testimonials) are unmet. **Blocked** —
  sequence after Hacker News, noting that HN's own comment thread can supply
  the testimonial signal PH wants.

Sequence: **1. Hacker News (4.4, ready) → 2. Package registry (3.6, ready) →
Blocked: Product Hunt (3.8, needs testimonials — satisfy via steps 1–2 first).**
Note Product Hunt's raw composite score (3.8) would rank it above the package
registry (3.6) on numbers alone — the prerequisite override is what correctly
pushes it later.
