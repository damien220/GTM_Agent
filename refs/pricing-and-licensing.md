# Pricing and Licensing

Defines the durable, structural half of `PRICING_GUIDE.md` — the license
decision path, packaging-model heuristics, how to choose and normalize
comparables, and the exact handoff contract to `PaymentAgent` or
`ContentPost_agent`'s `donation-specialist`. The other half, "what comparable
tools actually charge right now," is `pricing-specialist`'s live `WebSearch`
job, not this file's — prices move weekly, a method for reading them does not.
Same division of labor `pitch-and-outreach.md` draws for `marketing-specialist`
and `positioning-methodology.md` draws for `positioning-specialist`.

Load this file when: writing any section of `PRICING_GUIDE.md`, or the Pricing &
Packaging section of a combined `GTM_GUIDE.md`, after the project has been
classified (`project-classification.md`).

## Division of labor: this file vs. live search

This file holds the **decision paths and the heuristics**. The search holds the
**numbers and the names**. `pricing-specialist` must never present this file's
reasoning as a search finding, and must never state a competitor's price that no
search result supports. Where a figure couldn't be confirmed, the honest output
is **"not confirmed"** — a remembered price presented as current is worse than a
missing one, because the user will build their own number on top of it.

## 1. License decision path

Keyed on **the project's own stated goal**, not on a survey of licenses. Find
the goal first (a README status line, a parent `CLAUDE.md`, an existing
`LICENSE`, or — for a project inside this portfolio — `Dev_Agents/plan.md`'s
"sold, licensed, or donated" thesis). If no goal is stated anywhere, ask; this
decision is not derivable without one.

| Goal | Recommend | The one tradeoff it accepts |
|---|---|---|
| **Maximize adoption**; get it used and forked with the least friction | **MIT** | Anyone can take it closed-source, ship it commercially, and give nothing back — including a competitor. You are trading leverage for reach, deliberately. |
| Maximize adoption **and patent exposure matters** — corporate users, or a domain where patents are live | **Apache-2.0** | Slightly heavier: a `NOTICE` file and change-notification obligations. Corporate legal teams read it faster than MIT precisely because it's explicit; individuals find it wordier. |
| **Protect against closed-source forks** — anyone who improves it must share back | **GPL-3.0** | Real adoption cost. Many companies have a blanket policy against GPL dependencies, so this closes a door you cannot selectively reopen later. |
| Protect specifically against **SaaS capture** — someone hosting your code as a service without contributing | **AGPL-3.0** | The same adoption cost as GPL, plus more: AGPL is on more corporate denylists than any other common OSI license. Choose it when the hosted-fork scenario is a live threat, not as generic insurance. |
| Want a **revenue path while staying source-available** | **Dual licensing** (AGPL + a commercial license) or **open-core** (permissive core, proprietary add-ons) | Dual licensing requires you to own or have been assigned all the copyright — which means a CLA on every outside contribution, forever, and that is a real ongoing cost in both process and goodwill. Open-core avoids that but forces you to keep drawing a boundary that will annoy someone every time you move it. |
| **Pure gift** — a portfolio piece, a tool you want used and don't want to run a business around | **MIT + a donation link**, and no commercial machinery at all | You are foreclosing a revenue path that is expensive to add later, since a permissive license can't be retracted from code already released under it. This is a legitimate and frequently correct choice — see §2's note on when "free" is the answer. |

**Never present this table as guide content.** It is reference material for the
specialist. The guide gets one recommendation, 2-3 reasons it fits *this*
project, and the one tradeoff it accepts (`pricing-specialist.md` Critical
Rule 6). A user who wanted a license survey would have read one.

### Three things that need a lawyer, not this file

Per the disclaimer posture in §5 — attach the note to the specific
recommendation that raises it, not as a blanket preamble:

- **Dual licensing.** The mechanism is simple to describe and full of traps to
  execute: copyright assignment, CLA enforceability across jurisdictions,
  what happens to contributions made before the CLA existed. Recommend the
  *shape*; send the execution to counsel.
- **Trademark.** A license governs the code, not the name. A project can be
  MIT-licensed and still have a name it cannot legally use. `positioning-
  methodology.md` §1's namespace check is not a trademark search, and neither is
  anything here.
- **Contributor licensing (CLA/DCO)** on a project already taking outside
  contributions. Retrofitting one means getting agreement from everyone who has
  already contributed, which gets harder every month.

Tax treatment and revenue recognition are an accountant's questions, not this
file's, and get the same treatment: name the question, hand it off.

## 2. Packaging models

### The open-core boundary

Two tests, both required:

- **Is the free tier genuinely useful on its own?** Not "useful enough to
  evaluate" — useful enough that someone who never pays still gets real value
  and would recommend it. A free tier that is a functioning demo is a trial with
  a misleading name, and a technical audience reads it that way immediately.
- **Is the paid thing fair to gate?** The boundary that works is one where the
  paid side maps to *someone else's* cost or scale — team features, hosted
  infrastructure, compliance and audit, priority support, volume. The boundary
  that generates resentment is one that gates a core capability the tool
  obviously has, purely to force an upgrade.

The practical version: gate what costs you money to provide, or what only
matters at a scale where the user is clearly making money too. Don't gate what
is simply the point of the tool.

### One-time vs. subscription vs. usage-based

Keyed on **how the tool delivers value over time**, not on which model is
fashionable:

- **One-time** — the tool delivers its value in a bounded event and then keeps
  working. Generators, scaffolders, converters, one-shot analyzers. A
  subscription here is asking to be paid repeatedly for a thing that happened
  once, and users notice. Pairs with `PaymentAgent`'s `--payment-model one-time`.
- **Subscription** — the value is continuous: the tool runs against changing
  input, or you maintain it against a moving external dependency (an API, a
  registry, a platform's rules), or it holds state the user relies on. This is
  the honest case for recurring revenue, and the one to say out loud in the
  guide: "you are paying me to keep this current."
- **Usage-based** — your own costs scale with usage (LLM tokens, GPU time,
  storage, egress). Then usage-based is not a pricing tactic, it's cost
  pass-through, and framing it that way is both more honest and easier to
  defend. Its cost is that the buyer can't forecast the bill, so pair it with a
  cap or a floor unless the buyer is sophisticated.

### "Free during beta, price later"

This is a **specific promise, not a hedge.** Said casually it reads to users as
"free," and the later price change lands as a betrayal even when it was always
the plan. If it's the recommendation, the guide must say what makes it concrete:
what "beta" ends at (a version, a date, a capability), what early users get when
it does (grandfathering, a discount, nothing — but stated), and that this is
published, not implied. A vague "we'll figure out pricing later" costs more
goodwill than a price would have.

### When "free" is the answer

Frequently. `pricing-specialist.md` Critical Rule 9 makes this explicit because
the pull toward manufacturing a paid tier is strong and produces bad guides. It
is the right answer when: the project is a portfolio piece whose return is
credibility rather than revenue; when its entire distribution advantage is being
frictionless (a tool people try because there is nothing to decide); when the
maintainer does not actually want the support obligation that a price creates;
or when the addressable audience is too small for the machinery to pay for
itself. In those cases the recommendation is MIT + a donation link, and the
handoff goes to `donation-specialist` (§4).

## 3. The comparables method

### Choose by same buyer, not same technology

The comparable is whatever the classified `target_user` is **already paying for
instead** — not whatever shares a stack. A project with an identical
architecture aimed at enterprise buyers tells you nothing about what a solo
developer will pay. A completely different tool that solves the same problem for
the same person tells you everything.

Include the **status quo** as a comparable where it applies: the manual process,
the general-purpose incumbent bent to the task, or "they do nothing today." A
free incumbent is a price point — usually the hardest one to beat.

Three to five comparables. Real, named, confirmed by live search rather than
recalled.

### Normalize before comparing

Prices as published are rarely comparable as published. Before putting two
numbers in the same table, normalize:

- **Per unit of what** — per seat, per project, per run, per month, per
  organization. A $10/seat tool and a $50/org tool are not $10 and $50.
- **Billing period** — annual-billed prices are usually shown discounted;
  compare like with like and say which you used.
- **What the tier actually includes** — the headline price is often a tier that
  excludes the capability being compared.
- **Free tier presence** — a comparable with a generous free tier is competing
  at $0 for most of the target user's decision, whatever its paid price says.

State the normalization in the table's Notes column. An un-normalized comparison
table looks rigorous and misleads.

### The VC-subsidy caveat

Some comparables are priced below their own cost to buy market share, funded by
investors who expect that to change. **An indie project cannot match that price
and should not try.** Flag it explicitly in the guide when it applies — an
unflagged subsidized comparable is the single most misleading thing the section
can contain, because it anchors the user to a number that was never available to
them and often isn't sustainable for the company charging it either.

Related non-transferable cases to flag the same way: enterprise pricing that
exists only behind a sales call (the published number is a starting position,
not a price), and a loss-leader attached to a larger product (priced to sell
something else, not itself).

## 4. The handoff: `PaymentAgent` or `donation-specialist`

### The contract

**GTM_Agent writes the command. The user runs it.** This mirrors the Shipping
Guide's handoff to `CI_CD_agent` (`deployment-patterns.md` §1/§8 — "a forward
pointer, not a step to execute here") and is the same guide-only boundary
`docs/plan.md` §4 draws for the whole agent. `pricing-specialist` never invokes
`scaffold.py`, `@payment-setup-agent`, or `@donation-specialist` — a handoff
block is a recommendation, not a delegation.

### `scaffold.py` directly vs. `@payment-setup-agent`

Use a **concrete `scaffold.py` command** when the provider recommendation is
well-founded from what you know — the project's geography, its stated tax
posture, its scale, its stack. Fill every flag; a handoff with a placeholder in
it has failed at the one thing it's for.

```bash
python PaymentAgent/scaffold.py --provider <paddle|stripe> --stack <stack> --db <db> [--payment-model one-time] [--tiers "..."]
```

Valid values, from `PaymentAgent`'s own interface — keep these in sync with
`PaymentAgent/scaffold.py --list` rather than inventing flags:

- **providers:** `paddle`, `stripe`
- **stacks:** `nextjs`, `fastapi`, `express`, `django`, `sveltekit` — combine two
  with `+` (e.g. `nextjs+fastapi` for a Next.js frontend with a FastAPI backend)
- **dbs:** `prisma`, `sqlalchemy`, `django-orm`
- **payment models:** `subscription` (default) and `one-time`
  (`--payment-model one-time`)
- **`--tiers "starter,pro"`** where a tier structure was recommended

The rough provider split, per `PaymentAgent`'s own
`refs/provider-comparison.md`: **Paddle** is a merchant of record and handles
tax/VAT/GST — the usual fit for a global, solo/small-team product that doesn't
want tax overhead. **Stripe** gives more granular billing control — the usual
fit for US-focused or higher-volume products. That is a starting heuristic, not
a decision procedure.

Use **`@payment-setup-agent`** when the provider is *genuinely* undecided —
the merchant-of-record question turns on facts you don't have (real tax
exposure, geography, expected volume). Routing there is better than picking on a
coin flip: that agent exists for exactly this question and will ask it.

Use it also when the classified stack **isn't one `scaffold.py` supports**. Say
that plainly rather than bending the stack to fit a flag — a scaffold generated
against the wrong framework is worse than no scaffold.

### The donation-only branch

When the recommendation is stay-free (§2's "when free is the answer"), the
handoff is **`@donation-specialist`** in `ContentPost_agent` — it covers Patreon
and Buy Me a Coffee and writes the actual posts. Name it explicitly. "Add a
donate link" left as an unassigned instruction is exactly the "now go do all of
this yourself" ending `docs/design-review-2026-08.md` §1 flags across every guide
this agent has ever produced; the whole point of a handoff block is that it
names the next executable thing.

## 5. Disclaimer posture (adapted from `pitch-and-outreach.md`)

Pricing and licensing guidance here is **tactical, not legal, financial, or tax
counsel** (`docs/plan.md` §4's non-goal) — the same posture `LegalAgent`'s
`refs/upl-and-disclaimer-policy.md` takes toward legal conclusions, adapted to
this domain's actual risk:

- **Never guarantee revenue or conversion.** No projected MRR, no conversion
  rate, no "developers will happily pay for this." Frame every recommendation as
  "worth trying because X" — the same rule `marketing-specialist` works under.
- **Never state a comparable's price as fact unless it traces to an actual
  live-search result**, attributed inline (`(source: ...)`). Mark anything
  unconfirmed **"not confirmed"** rather than filling it from memory. A stale
  price presented as current is a fabricated-authority problem with a number
  attached, which makes it more persuasive and more damaging than a vague claim.
- **Always a range with reasoning, never a hard number.** False precision reads
  as analysis and isn't. The reasoning is the deliverable; the range summarizes
  it.
- **A license recommendation is a recommendation with its tradeoff stated**,
  never "you must use X." The project's owner is choosing, and needs to see what
  they're giving up.
- **Dual licensing, trademark, contributor licensing (CLA/DCO), tax treatment,
  and revenue recognition get an explicit "confirm with counsel / an accountant"
  note**, attached to the specific recommendation that raises it. Never reason
  about likelihood of infringement, registrability, or tax liability — name the
  question and hand it off. A disclaimer attached everywhere is a disclaimer
  attached nowhere.

## 6. Output format

`pricing-specialist` renders four sections in this order — **License → Free vs.
Paid → What Comparable Tools Charge → Next Step (handoff)** — because each
constrains the next: the license bounds which commercial models are even
available, the free/paid boundary determines what there is to price, the
comparables set the range, and the handoff names the command that implements it.

Attribute every live-searched figure inline (`(source: ...)`), exactly as
`pitch-and-outreach.md`'s Output format requires of Marketing. State every price
as a range with its reasoning. Attach counsel notes to the specific items that
raise them. The handoff block ends the guide, filled in and runnable — never run.
