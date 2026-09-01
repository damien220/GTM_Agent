# Positioning Methodology

Defines the durable, structural half of `POSITIONING_GUIDE.md` — how to run a
namespace check, how to construct a one-liner, how to choose comparison
dimensions, and how to tell a defensible differentiator from a merely true one.
The other half, "which names are actually taken and who actually competes right
now," is `positioning-specialist`'s live `WebSearch` job, not this file's — the
same division of labor `pitch-and-outreach.md` draws for `marketing-specialist`,
and for the same reason: a registry's contents and a competitive field change
weekly, a method for reading them does not.

Load this file when: writing any section of `POSITIONING_GUIDE.md`, or the
Positioning section of a combined `GTM_GUIDE.md`, after the project has been
classified (`project-classification.md`).

## Division of labor: this file vs. live search

This file holds the **procedure and the judgment calls**. The search holds the
**facts**. `positioning-specialist` must never present this file's reasoning as
if it were a search finding, and must never state a namespace status or name a
competitor that no search result actually supports. Where a check could not be
completed, the honest output is **"not verified"** — never an inference from
absence of evidence, which in a namespace check reads identically to "clear"
and is wrong in exactly the expensive direction.

## 1. The namespace / collision check

The point is not to find a *unique* name. The point is to make sure the user
knows what their name currently means to the audience that will encounter it —
before that audience tells them.

### Which namespaces to check, by stack

| Stack (from classification) | Check |
|---|---|
| Any | **GitHub** — both `github.com/<name>` (org) and repo-name search. This is where a developer audience will collide first. |
| Python | **PyPI** (`pypi.org/project/<name>`) |
| Node / TypeScript | **npm** (`npmjs.com/package/<name>`), including the scoped form the project would actually publish under |
| Rust | **crates.io** |
| Ruby / Go / other | RubyGems / the module path / the ecosystem's equivalent |
| Claude Code agent (`.md` definitions, no hosted runtime) | Usually **no registry namespace at all** — say so; the collision surface is GitHub, the plugin-marketplace listing, and the spoken name, not a package index. |
| Any, always | **A plain-name domain check** — `<name>.com` plus the one obvious alternative for the field (`.dev`, `.sh`, `.io`) |

For a **dual-artifact project** (a standalone script *and* an agent definition —
`deployment-patterns.md`'s dual-artifact case), check the namespace for each
artifact's actual published name; they are frequently different strings.

### Check the right string

The directory name, the README's title, and the manifest's `name` field are
often three different strings. Check what the project will actually be
*published and spoken* as. A namespace check run against the directory name
when the package publishes under something else is a confidently wrong finding —
worse than no check, because it will be trusted.

### Taken vs. crowded vs. clear

- **Taken** — the exact name is already in use in a namespace this project
  would need. Consequence: a concrete blocker (you cannot publish under it) or a
  concrete confusion cost (searching the name returns them, not you).
- **Crowded** — the exact name is technically free, but the name-space around it
  is dense: several similarly-named projects, or one dominant project whose name
  is a near-miss. Consequence: no blocker, but every discovery channel is
  fighting an existing association. Crowded is the more common and more
  under-diagnosed case; it doesn't stop a launch, it just quietly halves the
  return on every launch channel.
- **Clear** — free and not adjacent to anything dominant in the same field.
- **Not verified** — the check couldn't be completed. Say this; do not round it
  to "clear."

Scale matters more than count. One 350k-star project in the exact same niche is
a far bigger collision than twenty abandoned repos sharing a common word — say
which kind you found, with the specific project named.

### Why a plain-domain check matters even for a CLI

A CLI that will never have a website still gets typed into a search bar by
someone who heard the name in a podcast, a conference hallway, or a Hacker News
thread. The domain is a proxy for **what the name already means**: if
`<name>.com` is a live product in an adjacent field, every spoken mention of the
project routes attention there. The finding is not "buy the domain" — it is
"this name already has an owner in the audience's head." That is a positioning
fact whether or not the project ever wants a site.

### The collision is a finding, not a rename order

Three options, always presented with tradeoffs, never collapsed into one
recommendation:

1. **Position against it** — make the collision the hook ("the small, local
   alternative to X"). Costs: you permanently define yourself relative to
   someone else, and you inherit their framing of the problem. Works best when
   the colliding project is well-known *and* genuinely different in approach.
   This was the `A_OpenClaw` answer.
2. **Differentiate the name** — rename, or qualify it (a prefix, a suffix, a
   scope). Costs: the real one is not the rename, it is every link, doc, and
   mention already pointing at the old name; cheap pre-launch, expensive after.
3. **Accept the overlap** — ship anyway and absorb the confusion. Costs: SEO and
   word-of-mouth discovery both leak to the other project indefinitely.
   Legitimate when the fields are genuinely disjoint or the other project is
   dormant.

Renaming is the user's call. The failure mode this section prevents is not "the
user chose wrong" — it is "the user found out from a commenter after launch."

## 2. One-liner construction

### The skeleton

**What it is · for whom · unlike what.** All three parts, one sentence. The
third part is the one people skip and the one that does the positioning work —
without it, a one-liner is a description, not a position.

### The user's-language test

Write the sentence, then ask: **would the target user say it this way?** Not
"would they understand it" — understanding is a low bar and jargon usually
clears it. Would this phrasing appear in the sentence they'd type into a search
bar, or say to a colleague when explaining why they went looking? If the answer
uses the maker's internal vocabulary (the module names, the architecture, the
phase numbers), it fails, however accurate it is.

The classification's `target_user` is the input to this test. This is the
concrete reason `positioning-specialist` cannot skip classification: "developers
who need X" and "solo founders who need X" produce different correct sentences
for the same project.

### The common failure: leading with the mechanism

The most frequent bad one-liner leads with **how it works** rather than **what
changes for the user**:

- Mechanism-first: "An orchestrator plus five specialist subagents with a YAML
  platform registry and live web search."
- Outcome-first: "Turns a finished side project into a concrete plan for
  shipping it and getting it in front of real users."

Both describe the same thing. Only the second one survives contact with a reader
who does not already know what the project is. Mechanism-first phrasing is
especially seductive for technical projects because the mechanism is the part
the maker is proud of and the part they've been thinking about all week — which
is precisely why it needs a deliberate check rather than a general intention to
"write clearly."

### Always show the original

Quote the project's current one-liner verbatim next to the refined one, plus one
or two lines saying what changed and why. A refinement shown alone is
unverifiable and reads as a style preference; shown against the original, the
argument is visible and the user can disagree with it specifically.

If the README has no one-liner at all — it opens with an install command, or a
badge row, or a phase table — that is itself the finding, and a more serious one
than an imperfect existing line.

## 3. The competitor comparison table

### Pick the rows from `target_user`, not from your feature list

This is the whole method, and the most common way the section goes wrong. If the
comparison dimensions are drawn from what this project happens to do, the table
is won by construction and tells the reader nothing — every project wins a
comparison scored on its own feature list.

Instead: ask what a person matching the classified `target_user` is actually
deciding between, and what they would weigh. A solo developer evaluating a dev
tool weighs setup time, whether it works offline, and whether it will still
exist in a year. An enterprise buyer evaluating the same tool weighs support,
compliance, and procurement friction. Same project, disjoint tables. Three to
five rows is usually right; past that the table stops being readable and starts
being a spec sheet.

### Choosing the competitors

Three to five, real and named, confirmed by live search rather than recalled.
"Real" means a target user would plausibly evaluate it — not merely that it
exists in the same technical space.

**When there is no direct competitor**, do not pad the table with weak matches.
Compare against the **status quo alternative**: the manual process, the
general-purpose incumbent people currently bend to the task, or "they don't do
this at all today." What they do instead is always a legitimate column, and for
a genuinely new category it is the only honest one.

## 4. The defensible-vs-true test

Every differentiator gets one of two labels. This is the section's reason to
exist — a comparison table without it is a feature checklist, which the project's
own README already is.

**Defensible** — the advantage follows from a **structural choice a competitor
cannot cheaply reverse**: architecture, licensing, the data you have and they
don't, a distribution position, or a business-model constraint that makes
copying it actively costly for them.

**Merely true** — the advantage is real today and is a **feature-parity gap**.
It closes whenever the competitor decides it matters. Still worth stating; just
not worth building a position on, and never worth building a *price* on
(`pricing-and-licensing.md`'s packaging section leans on this call directly).

The test question: **if a well-resourced competitor decided tomorrow that this
mattered, what stops them?** If the answer is "nothing but priorities," it's
merely true.

### Worked examples

1. **"We're faster — 78% fewer tokens than reading source files raw."**
   *Merely true.* Speed and efficiency numbers are the most copyable
   differentiator that exists; the competitor reads your README, implements the
   same compaction, and the gap is gone in a release. It becomes defensible only
   if the efficiency comes from something structural — a format the ecosystem
   has standardized on because of you, say — and not from an optimization.

2. **"We're MIT-licensed and self-hosted; the incumbent is a hosted SaaS with
   per-seat pricing."**
   *Defensible.* Not because the license is hard to change, but because the
   competitor's entire revenue model depends on the opposite choice. Matching
   you means cannibalizing their own business — the constraint is structural,
   not technical. This is the strongest common form of defensibility available
   to a small project.

3. **"We support 13 platforms; they support 6."**
   *Merely true*, and a trap: it invites a race the better-resourced party wins.
   It converts to defensible only if the coverage rests on something structural —
   a contributor community adding platforms faster than a closed team can, or a
   registry format others build against. Coverage counts by themselves are a
   snapshot, not a moat.

An honest output frequently ends up with **one** defensible differentiator and
several merely-true ones. That is a normal and useful result. A table where
every row reads "defensible" means the test wasn't actually applied.

## 5. Who it's not for

A positioning with no excluded audience is too vague to act on. If the answer to
"who is this for" is "anyone who needs it," the project has no position — it has
a description.

The section should name **2-3 real, plausible audiences** that would genuinely
land on this project and should be sent elsewhere, with where they should go
instead. Two tests for whether a boundary is real:

- Would someone in that group **actually show up**? "Not for people who don't
  write software" is not a boundary for a dev tool — nobody in that group was
  ever going to arrive. "Not for teams who need SSO and an audit log — use X"
  is, because those people arrive constantly.
- Could the user **decline a feature request with it**? That is the boundary's
  practical function: it is the sentence that makes "we're not building that"
  a principled answer rather than a capacity excuse.

Excluding an audience makes the remaining audience recognize themselves. This is
the section that converts a description into a position, and it is the one most
often dropped for fear of turning users away — which is the point of it.

## 6. Disclaimer posture (adapted from `pitch-and-outreach.md`)

Positioning guidance here is **tactical, not marketing, legal, or trademark
counsel** (`docs/plan.md` §4's non-goal), the same posture `LegalAgent` takes
toward legal conclusions, adapted to this domain's actual risk:

- **A namespace check is not a trademark search.** A name being free on GitHub,
  PyPI, and as a domain says nothing about whether it infringes a registered
  mark, and this guide must never imply otherwise. Where a name is close to a
  known commercial product's, say plainly that a trademark question is a lawyer's
  question and out of this agent's scope — do not reason about likelihood of
  confusion, classes, or registrability.
- **Never present a positioning as guaranteed.** "This frames the project
  against X, which matters because Y" — never "this positioning will win the
  category." The market decides; this file supplies a method, not an outcome.
- **Never state a competitor or namespace fact that no search result supports.**
  Attribute inline (`(source: ...)`), and mark anything unconfirmed **"not
  verified"** rather than asserting it. An unattributed competitive claim is a
  fabricated-authority problem — and unlike a soft marketing claim, a wrong
  namespace finding can send someone to rename a project that never needed it.
- **A name collision is never rendered as an instruction to rename.** Options
  with tradeoffs; the decision is the user's (§1 above).

## 7. Output format

`positioning-specialist` renders the four sections in this order — **Namespace
Check → One-Liner → Competitor Comparison → Who This Is NOT For** — because each
informs the next: the collision constrains the one-liner, the one-liner sets the
comparison's frame, and the comparison's defensible differentiator is what the
"not for" boundary carves around.

Mark each live-searched claim's source inline (`(source: ...)`), exactly as
`pitch-and-outreach.md`'s Output format requires of Marketing. Mark every
differentiator **defensible** or **merely true**. This is what makes "the
namespace check and competitor table are real" verifiable rather than an
assertion.
