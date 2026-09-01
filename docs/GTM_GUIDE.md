# GTM Guide — GTM_Agent (Go-To-Market Agent)

_Generated 2026-08-31 by a combined-mode, two-wave run of GTM_Agent against its own
project. Fresh run, not a refresh._

```
category: AI agent
stack: Claude Code agent (.md subagent definitions + refs/*.md knowledge files +
  platforms/*.yaml registry + one Python maintenance helper, lib/validate_platforms.py,
  on the shared Dev_Agents/.venv — no hosted runtime, no runtime dependencies at guide-
  generation time)
maturity: functional / untested-in-production — all six phases implemented (orchestrator
  + 5 specialists + 8 ref files + 12 platform YAMLs + validator); dogfooded across 5
  in-portfolio targets and 1 external project (A_OpenClaw); Phases 5 and 6 explicitly
  NOT yet validated by any real end-to-end run; no automated test suite exists
target_user: solo developers and small teams who have finished (or nearly finished) a
  project and don't know how to get it in front of real users — plus this repo's own
  maintainer, as a capstone step after each agent reaches a shippable phase
source_files: GTM_Agent/README.md, GTM_Agent/docs/plan.md, GTM_Agent/CLAUDE.md
  (secondary signals inspected directly: git log/remote/status/ls-tree, .gitignore,
  absence of LICENSE, .claude/agents/ contents, /home/vscode/.claude/agents/)
confidence_notes: (1) The plan file is at docs/plan.md, not the root — this project
  moved all authored docs under docs/ by its own convention. (2) NO secondary category
  tag: lib/validate_platforms.py is a maintenance-only registry validator explicitly
  outside every agent runtime path, so the dual-artifact "dev tool" secondary that
  applies to code-mapper and PaymentAgent does NOT apply here. This is a pure Claude
  Code agent-definition project. (3) Maturity is deliberately not rounded up to
  "shipped": README, CLAUDE.md and plan.md all three state that Phase 5 + Phase 6 work
  is unvalidated by a real run, so testing — not deployment — is the actual next step.
```

---

## Positioning

### Namespace / Collision Check

**Strings checked:** `GTM Agent` (README H1 / the spoken name), `gtm-agent` (the actual invocation string — `@gtm-agent` — and the agent filename), `GTM_Agent` (directory). There is no manifest and no published package name; `lib/validate_platforms.py` is maintenance-only and publishes nothing, so there is no registry string to check.

| Namespace | Status | Finding |
|---|---|---|
| GitHub — repo name `gtm-agent` / `gtm-agents` | **Crowded, heavily** | Not one collision but a dense field of active, same-named projects: [`gtmagents/gtm-agents`](https://github.com/gtmagents/gtm-agents) (~96 stars, 92 agents + 52 skills + 67 plugins, "for claude code"), [`getaero-io/deepline-gtm-agent`](https://github.com/getaero-io/deepline-gtm-agent), [`oneshot-agent/oneshot-gtm`](https://github.com/oneshot-agent/oneshot-gtm), [`gtm-skills/gtm`](https://github.com/gtm-skills/gtm), [`attentiontech/gtm-superintelligence`](https://github.com/attentiontech/gtm-superintelligence), [`chapter-gtm/chapter`](https://github.com/chapter-gtm/chapter) (source: GitHub search results, 2026-08-31) |
| GitHub — org handle `gtmagents` | **Taken** | [github.com/gtmagents](https://github.com/gtmagents) is a live org (source: GitHub search results, 2026-08-31) |
| GitHub — org handle `gtm-agent` (exact) | **Not verified** | Did not resolve this specific handle in search; do not read this row as "clear" |
| Package registry | **N/A — no registry namespace** | Correct for the stack: `.md` subagent definitions have no package index. Per `positioning-methodology.md` §1, the real collision surface is GitHub + the plugin-marketplace listing + the spoken name |
| **Claude Code plugin marketplace** (the registry-equivalent for this stack) | **Taken, by a same-named competitor** | `gtmagents/gtm-agents` is already listed as a Claude Code plugin marketplace under the name "GTM Agents" ([claudemarketplaces.com/plugins/gtmagents-gtm-agents](https://claudemarketplaces.com/plugins/gtmagents-gtm-agents)); it has third-party writeups as "GTM Agents: a Claude Code plugin marketplace for revenue teams" (source: [codeline.co](https://www.codeline.co/thoughts/repo-review/2026/gtm-agents-claude-code-plugin-marketplace-for-revenue-teams), [syncgtm.com](https://syncgtm.com/blog/claude-code-gtm-skills-2026), 2026-08-31). If this project ever lists on the marketplace this repo's own `platforms/claude-code-plugin-marketplace.yaml` recommends, it lands next to an entry with its name |
| Domain — `gtmagent.com`, `gtmagents.com`, `gtmagent.io` | **Resolving (in use)** | All three resolve to live DNS (source: direct DNS lookup from this environment, 2026-08-31) |
| Domain — `gtm-agent.com`, `.dev`, `.ai` | **Not verified** | No DNS resolution, which is *not* evidence of availability — a registered domain can park without an A record. Registration status unchecked |
| The term itself | **Category-owned** | "GTM agent" is not a free descriptor in 2026; it is an established industry category meaning *AI that runs sales motions* — prospecting, enrichment, outreach, CRM updates. Gartner maintains a peer-insights market called [AI GTM Platforms](https://www.gartner.com/reviews/market/ai-gtm-platforms); vendor and analyst content defines a GTM agent as a system that executes "account research, lead enrichment, outreach generation, signal monitoring, campaign creation, CRM updates" (source: [dhisana.ai](https://www.dhisana.ai/top10-gtm-ai-agent-platforms.html), [smartlead.ai](https://www.smartlead.ai/blog/gtm-agents-accelerating-go-to-market-strategy), [zoominfo](https://pipeline.zoominfo.com/sales/gtm-ai), 2026-08-31) |

**Assessment**

**This is a real collision, and it is worse than a name clash — the name places the project in the wrong category.** `docs/plan.md` §0 records that "GTM" was chosen because it does not collide with any existing agent's naming *inside this repo*, and explicitly notes no external check was ever run. That check now has an answer. Externally, "GTM agent" is a saturated 2026 category term that means autonomous sales/outbound automation. This project does the opposite of that category on its single loudest axis: the category's defining behavior is *acting on your behalf* (emailing, enriching, updating CRM), and this project's hardest development rule is *never acting on the user's behalf*. Anyone who arrives via the name arrives expecting the thing the project has explicitly ruled out.

Two aggravating specifics. First, the closest neighbor is not in an adjacent field — `gtmagents/gtm-agents` is a Claude Code agent collection, on the same runtime, distributed through the same plugin marketplace, under effectively the same name. Second, the name fails a discovery test in *both* directions: it returns sales tooling to anyone searching it, and the classified `target_user` — a solo developer who just finished something — does not use the phrase "GTM" at all. They search "how do I launch my side project." The name therefore costs discovery without buying any.

The mitigating specific, and it matters: **the rename cost here is near zero and will never be this low again.** Observed repo state is one commit, no remote, nothing ever pushed, no LICENSE, no external links, no users, and all Phase 5 + 6 work still uncommitted. `positioning-methodology.md` §1 notes the real cost of a rename is the accumulated links, docs and mentions — this project has none. That is a genuinely unusual position and it is the reason this finding is cheap today.

The three options, with tradeoffs — **this is a finding, not a rename instruction; the call is the maintainer's:**

1. **Position against it** — lead with "not that kind of GTM agent." Cost: you spend the one-liner on a disclaimer, and unlike the `A_OpenClaw` case (one large project to define against), here you would be positioning against an entire analyst-recognized category with many well-funded members. You cannot out-shout a category term. Weakest of the three here, and it is weak specifically *because* the collision is categorical rather than singular.
2. **Differentiate the name** — rename, or qualify it into a phrase the target user actually says (something in the "launch"/"ship it"/"first users" register rather than the "GTM"/"revenue"/"pipeline" register). Cost: the internal churn of updating six agent files, eight ref files, two `CLAUDE.md`s and the parent portfolio table — real work, but it is a one-afternoon find-and-replace against an unpushed repo, and it is the only option that also fixes the *target-user-language* problem rather than just the collision. Note this reopens §0's original question, which was a real one: whatever the new name is, it must still not collide with `CI_CD_agent`'s ownership of "delivery" inside this repo.
3. **Accept the overlap** — ship as `GTM_Agent`. Cost: permanent search leakage to sales tooling; a plugin-marketplace listing that sits beside a same-named competitor; and an inbound audience systematically mismatched to what the project does (see "Who This Is NOT For," first bullet). Legitimate only if the project stays an internal portfolio tool and never courts external discovery — which contradicts `README.md`'s framing and the parent repo's stated "sold, licensed, or donated" purpose.

**Out of scope:** none of the above is a trademark search. Whether "GTM Agent" or any replacement infringes a registered mark is a lawyer's question and this guide does not reason about it.

---

### One-Liner

**Currently (from `README.md`, the line under the status blockquote — verbatim):**

> "Give it your project's `README.md`, `plan.md`, and `CLAUDE.md` (or any other file you point it at) and it writes back a concrete plan for shipping and getting the project in front of real users — not code, not a deployment, not a social post: a guide you follow."

(The README's actual first line is a status blockquote — six phases, dry-run testing, `docs/plan.md` §8/§9 — so a reader meets a changelog before they meet a description. The line above is the closest thing to a one-liner and is what I am treating as the current one.)

**Refined:**

> "Reads the project you just finished and writes back the launch plan — how to position it, where to ship it, which platforms to launch on in what order, and what to charge — for solo developers whose problem is that nobody knows the thing exists yet, unlike the 'GTM agents' that automate outbound sales."

**What changed and why:**

- **It stops leading with the mechanism.** The current line opens on inputs ("give it your `README.md`, `plan.md`, and `CLAUDE.md`") — and two of those three are maker's vocabulary; `plan.md` and `CLAUDE.md` are *this repo's* conventions, not files most target users have. The refined line opens on the user's state ("the project you just finished") and the outcome.
- **It adds the missing "unlike what."** The current line defines by negation against things nobody confused it with ("not code, not a deployment, not a social post") while omitting the one contrast that actually matters given the namespace finding — the sales-automation tools that share its name. That clause does double duty: it positions, and it pre-empts the wrong-audience arrival.
- **It names the pain, not the artifact.** "Nobody knows the thing exists yet" is the sentence the target user would actually say; "a concrete plan for shipping and getting the project in front of real users" is the sentence the maker would say. Same fact, different register.

---

### Competitor Comparison

Alternatives a **solo developer or small team who just finished a project and doesn't know how to get users** would actually evaluate — live-searched, not recalled. Note that column 3 is included because it *shares this project's name*, not because the target user would choose it; that mismatch is itself the finding.

| | **GTM_Agent (this)** | **skills-gtm** | **gtm-agents** | **Launch-checklist sites** | **Just asking Claude directly** |
|---|---|---|---|---|---|
| **Does it look at my actual project, or hand me generic advice?** | Reads the repo, classifies it (category/stack/maturity/target user), everything downstream keys off that | Reads your inputs via a structured intake, then runs research agents | Reads your CRM/prospect data; the project itself is not the subject | Generic — the same checklist for every product | Reads whatever you paste; no enforced classification step |
| **Do I get a ranked "launch here first, then here" with the reasoning shown?** | Yes — scored against a documented rubric (`platform-scoring-methodology.md`), and a bare unranked list is a rule violation | GTM strategy through to meeting prep; ranking rubric not documented in the listing | No — not the problem it solves | Mostly single-platform (Product Hunt) plus alternative lists; sequencing advice is prose, not scored | Ad hoc, different answer each run, no rubric to check |
| **What do I need before it's useful?** | Claude Code + a repo with docs. No install, no API keys, no data | Claude Code | Claude Code + real GTM data sources (CRM, enrichment providers) | Nothing — a browser | A Claude subscription |
| **Does it cover the whole path or one slice?** | Whole path in one document, five sections that argue from one shared position | Broad: intake → strategy → meeting prep | Very broad but sales-shaped: 92 agents, 52 skills, 67 plugins | One slice — the launch-day event | Whatever you think to ask for; coverage is on you |
| **Can I actually get it, and will it still be here?** | **No.** No LICENSE, no remote, one commit, never pushed. Not obtainable today at any price, and legally unusable even if copied | Public GitHub repo | Public GitHub repo, ~96 stars, active maintenance, marketplace-listed | Live public sites, commercially operated | Always available |

_Competitors: [`elliottrjacobs/skills-gtm`](https://github.com/elliottrjacobs/skills-gtm) — "9 agent skills and 19 research agents for Claude Code that build a complete go-to-market strategy — from first intake to meeting prep" (source: GitHub search, 2026-08-31); [`gtmagents/gtm-agents`](https://github.com/gtmagents/gtm-agents) — 92 agents / 52 skills / 67 plugins for Claude Code, ~96 stars (source: GitHub + [claudemarketplaces.com](https://claudemarketplaces.com/plugins/gtmagents-gtm-agents), 2026-08-31); launch-checklist sites [LaunchList](https://getlaunchlist.com/checklists/producthunt), [Smol Launch](https://smollaunch.com/alternatives/product-hunt), [Donkey Directories](https://www.donkey.directory/blog/product-hunt-submission-checklist-2026) (source: web search, 2026-08-31). The final column is the status-quo alternative per `positioning-methodology.md` §3 — for this target user it is the honest default, not a padding column._

**Differentiators, called:**

- **One classification feeding five sections that argue from the same position (the positioning context block handed forward to Wave 2)** — **defensible, narrowly.** The structural argument is real but bounded: against the *marketplace-shaped* competitors (`gtm-agents`' 67 independently-invoked plugins), coherence-from-a-shared-classification is not a feature they can add — it is an architecture they'd have to rebuild, and their plugin-marketplace distribution model is precisely what makes 92 agents agree on one message expensive. It is **not** defensible against a from-scratch competitor, and `skills-gtm`'s intake→strategy pipeline is already partway to the same property. Call it a real but shallow moat, defensible against one class of competitor only.
- **Reads and classifies your actual repo before advising** — **merely true.** Against generic checklists, yes. Against `skills-gtm`, not even true today. Nothing structural stops any Claude Code agent from reading a repo; it is the cheapest capability in this comparison.
- **Documented scoring rubric with mandatory shown rationale** — **merely true.** The discipline is genuinely better than the field's norm, but `refs/platform-scoring-methodology.md` is a public markdown file in an open repo. A competitor reads it and ships their own rubric in a release. It converts to defensible only if the *registry format* gets adopted by others — i.e. if `platforms/*.yaml` becomes something people write files against. Nothing today points that way.
- **Live-search grounding on the three facts that go stale (namespace, field practice, prices), with "the ref file owns the method, the search owns the substance"** — **merely true.** A well-reasoned architectural commitment, and copyable in an afternoon by anyone who reads `docs/plan.md` §5. What stops a competitor is nothing but priorities — the methodology's own test question, answered.
- **12-platform launch registry, 8 ref files, 5 specialists** — **merely true**, and the trap `positioning-methodology.md` §4 example 3 names explicitly. `gtm-agents` already has 92 agents. Coverage counts invite a race the better-resourced party wins, and this project is losing that race on the numbers today.
- **Guides-only: never posts, deploys, or registers** — **not a differentiator at all, and I want to be direct about this.** It is a correct safety boundary and a good engineering decision, but "we do less on purpose" is not something the classified target user is choosing between vendors on. Solo developers do not select tools for restraint. State it as a scope boundary in the docs; do not build the position on it.
- **PaymentAgent / donation-specialist handoff with a filled-in command** — **defensible for exactly one user and worthless for the other.** For the repo maintainer (the second `target_user` in the classification) this is genuinely non-copyable: no competitor can hand off to *your* sibling agents. For an external solo developer it is negative value — a recommended next command pointing at a tool they do not have. This is a real fork in the positioning, and it is worth deciding deliberately which of the two target users the project is actually for.

**The honest summary:** one narrowly-defensible differentiator, one that is defensible only for the in-repo maintainer, and everything else merely true. That is a normal result per the methodology — but it lands harder here because of the last table row. **No differentiator is currently doing any work at all, because the project has no public existence:** no LICENSE (default all-rights-reserved — nobody may legally use it), no remote, one commit, and both new specialists uncommitted. A positioning argument is downstream of being obtainable. Fixing that is a Shipping and Pricing concern, but it caps the value of everything in this section until it is done.

---

### Who This Is NOT For

- **Revenue, sales and marketing teams looking for GTM automation** — they will arrive *constantly*, because the name and the entire 2026 meaning of "GTM agent" promise them prospecting, enrichment, outbound sequences and CRM updates (source: [Gartner AI GTM Platforms](https://www.gartner.com/reviews/market/ai-gtm-platforms), [dhisana.ai](https://www.dhisana.ai/top10-gtm-ai-agent-platforms.html), 2026-08-31). This project does none of it and has a hard rule against ever doing it. Send them to [`gtmagents/gtm-agents`](https://github.com/gtmagents/gtm-agents) or a commercial platform in that category. This is the boundary that makes "we're not adding outreach" a principled answer rather than a roadmap deferral — and it is the single strongest argument in favor of collision option 2.
- **Anyone who wants the launch actually executed** — people who want the Product Hunt submission filed, the posts scheduled, the emails sent. They arrive because "GTM agent" implies autonomy, and they will be disappointed by a Markdown file. Send them to `ContentPost_agent`'s `social-media-specialist` inside this repo, or a scheduling product outside it. This is the feature-request decline sentence the project needs most.
- **Founders who haven't built the thing yet and are looking for market validation** — they will read "go-to-market" and expect customer discovery, ICP definition, or demand testing. Every workflow here starts by reading a finished repo; with nothing built, the classification step has no input and the output degrades to generic advice. Send them to customer-discovery work first, then come back. This one is worth stating because it is the audience most likely to blame the tool for a vague answer.

_Positioning guidance above is tactical, not marketing, legal or trademark counsel. Nothing here guarantees an outcome — the namespace and competitor findings are facts as of 2026-08-31; the framing recommendations are arguments the maintainer can and should disagree with specifically._

**Sources:** [gtmagents/gtm-agents](https://github.com/gtmagents/gtm-agents) · [elliottrjacobs/skills-gtm](https://github.com/elliottrjacobs/skills-gtm) · [getaero-io/deepline-gtm-agent](https://github.com/getaero-io/deepline-gtm-agent) · [oneshot-agent/oneshot-gtm](https://github.com/oneshot-agent/oneshot-gtm) · [gtm-skills/gtm](https://github.com/gtm-skills/gtm) · [attentiontech/gtm-superintelligence](https://github.com/attentiontech/gtm-superintelligence) · [chapter-gtm/chapter](https://github.com/chapter-gtm/chapter) · [claudemarketplaces.com](https://claudemarketplaces.com/plugins/gtmagents-gtm-agents) · [codeline.co repo review](https://www.codeline.co/thoughts/repo-review/2026/gtm-agents-claude-code-plugin-marketplace-for-revenue-teams) · [syncgtm.com](https://syncgtm.com/blog/claude-code-gtm-skills-2026) · [Gartner AI GTM Platforms](https://www.gartner.com/reviews/market/ai-gtm-platforms) · [dhisana.ai](https://www.dhisana.ai/top10-gtm-ai-agent-platforms.html) · [smartlead.ai](https://www.smartlead.ai/blog/gtm-agents-accelerating-go-to-market-strategy) · [ZoomInfo](https://pipeline.zoominfo.com/sales/gtm-ai) · [LaunchList](https://getlaunchlist.com/checklists/producthunt) · [Smol Launch](https://smollaunch.com/alternatives/product-hunt) · [Donkey Directories](https://www.donkey.directory/blog/product-hunt-submission-checklist-2026)

---

## Shipping Guide

### Deployment Options

This is a Claude Code agent: its entire runtime is `.md` subagent definitions plus `refs/*.md` and `platforms/*.yaml`, read directly by Claude Code. There is no server, container, or hosted process — **do not deploy this to Vercel/Railway/Fly/AWS or any host** (`deployment-patterns.md §9`). The single Python file, `lib/validate_platforms.py`, is a maintenance helper explicitly outside every agent's runtime path (per the classification, this is *not* a dual-artifact project); it ships as a repo file, invoked only during registry maintenance, not as a separately-published tool. "Deployment" here means registration.

Because Phases 5 and 6 are unvalidated by a real end-to-end run (classified maturity: functional / untested-in-production), do the registration steps below now — they are what makes a validation run and further dogfooding possible — but hold the plugin/marketplace route until an end-to-end run passes.

**Primary path — make the agents invocable (`deployment-patterns.md §9`)**

1. **Commit the working tree first.** HEAD is not a runnable copy of this project: it is missing both `positioning-specialist.md` and `pricing-specialist.md` (which the orchestrator invokes in every combined run), three of the eight ref files, and the entire `docs/` and `lib/` directories; `plan.md` exists at HEAD only at its old pre-migration path. A fresh clone cannot run combined mode at all. Run `git add -A && git commit` so the repo matches the working copy.
2. **Project-scoped use** needs nothing further once step 1 is done — the canonical files already live in `GTM_Agent/.claude/agents/` (per `Dev_Agents/CLAUDE.md` rule 9), so `@gtm-agent` and the five specialists resolve from any session whose working directory is inside this repo.
3. **Cross-project use on this machine.** To invoke the agents from any directory regardless of git-repo boundaries, symlink each canonical file into the personal tier:
   ```bash
   mkdir -p /home/vscode/.claude/agents
   for a in gtm-agent positioning-specialist shipping-specialist \
            distribution-specialist marketing-specialist pricing-specialist; do
     ln -sf /workspaces/Prj_utils/Dev_Agents/GTM_Agent/.claude/agents/$a.md \
            /home/vscode/.claude/agents/$a.md
   done
   ```
   Then verify each resolves: `readlink -f /home/vscode/.claude/agents/gtm-agent.md` (and the other five). `CLAUDE.md` asserts this is already done; on the current machine `/home/vscode/.claude/agents/` does not exist, so it is not — treat this as outstanding, and re-create it on every machine the repo is cloned to (it is machine-local and never committed).
4. **Publish the repo** — see the "publish to GitHub" blocking item in Repo hygiene below. Nothing downstream (Distribution, Marketing) has anywhere to point people until the remote exists.

**Alternative — package as a Claude Code plugin**

Once a real end-to-end run has validated Phases 5–6, the six agents can be bundled as a Claude Code plugin for marketplace / team-wide distribution instead of per-machine symlinks. Tradeoff: wider reach and no manual symlink step, but it adds a submission workflow and a stability bar the project has not cleared. Whether it is worth doing, and the submission mechanics, are a `distribution-specialist` question (there is already a `platforms/claude-code-plugin-marketplace.yaml` for this) — not a step to perform here.

### Presentation Checklist

#### README quality bar
- `README.md` exists at the project root — **[present]**.
- One-line description above the fold — **[missing / weak]**. The README opens with a five-line bold status blockquote before any description, and the first actual description sentence does not say who it is for or distinguish the project from the established 2026 meaning of "GTM agent" (sales/outbound automation — see the Positioning section's severe name collision). Replace the lead with Positioning's refined one-liner: *"Reads the project you just finished and writes back the launch plan — how to position it, where to ship it, which platforms to launch on in what order, and what to charge — for solo developers whose problem is that nobody knows the thing exists yet, unlike the 'GTM agents' that automate outbound sales."*
- Install/usage instructions that run — **[missing / weak]**. The Setup/Usage section gives `@gtm-agent …` invocations (good) but omits the two things `presentation-standards.md §1` requires for a Claude Code agent: which file to symlink and where (the step 3 block above), and one example invocation *with its expected output shape* (e.g. "prints the classification block, then writes `GTM_GUIDE.md` into the target project's root with five sections in Positioning → Shipping → Distribution → Marketing → Pricing order").
- Status/maturity stated explicitly — **[missing / weak]**. The README leads with **"Status: complete — all six phases implemented"** and only walks it back mid-paragraph. Classified maturity is *functional / untested-in-production*. Change the headline to state that directly, e.g. "Status: functional; all six phases implemented, Phases 5–6 not yet validated by an end-to-end run" — do not let "complete" stand as the first word a stranger reads.
- License stated — **[missing]**. The README names no license and no `LICENSE` file exists (see Repo hygiene). Blocking; covered below.
- Working demo link/screenshot above the fold — not applicable to this category.

#### Demo video / screenshots
- **[missing — recommendation]** `presentation-standards.md §2` recommends a terminal-recording GIF for an AI-agent project, not a narrated video. Capture one 20–40s run of `@gtm-agent produce a full GTM guide for LegalAgent`: hook = the classification block printing in the first ~3s, core action = the two-wave run, end state = the written `GTM_GUIDE.md` open in the editor showing the five section headings. A real prompt and real output is more convincing here than prose.

#### Repo hygiene
- Version control initialized — **[present]** (git repo, branch `main`) — but see the two blocking items below; the current HEAD is not a shippable copy.
- `.gitignore` doesn't exclude core files — **[present]**. It explicitly keeps `.claude/agents/*.md` tracked ("`.claude/agents/*.md` ARE the product here — never ignore them") and covers `__pycache__/`, `*.pyc`, `.venv/` for the one Python helper.
- Every README-embedded asset tracked in git — **[present]** (the README embeds no local images or media).
- `LICENSE` file present — **[missing]**. Blocking; see below.
- Topics/tags set — **[missing — recommendation]**. Can't be done until a GitHub remote exists. Once it does, add topics matching the classification: `claude-code`, `ai-agent`, `subagent`, `go-to-market`, `developer-tools`, `launch`. Feeds `distribution-specialist`.
- No committed secrets — **[present]** (no `.env`, key, or credential files tracked; `.venv/` is the shared `Dev_Agents` venv and is gitignored).
- `.gitignore` covers build artifacts / dependencies — **[present]**.
- **Publish to GitHub — [missing]**. Blocking; see below.
- **Working tree matches HEAD — [missing]**. Blocking; see below.

#### Optional landing page
Skip — Claude Code agent with a developer audience; the README plus the eventual GitHub repo listing serve this role (`presentation-standards.md §4`).

**Blocking before shipping:**
- **Commit the working tree.** HEAD is missing 2 of 6 agent files, 3 of 8 ref files, and the whole `docs/` and `lib/` directories; `plan.md` is at HEAD only at its stale path. This is the `presentation-standards.md §3` "published repo doesn't match the working copy" failure shape — the product is non-functional from a clean clone. `git add -A && git commit`.
- **Add a `LICENSE` file.** Absent means default all-rights-reserved on GitHub — legally unusable by anyone, which nullifies every downstream Distribution and Marketing step and contradicts the parent portfolio's stated "sold, licensed, or donated as open-source" goal. Fast fix; take the license named in the Pricing & Packaging section and make sure the README's new status line matches it.
- **Create a GitHub remote and push.** There is no remote and history exists only on this machine. Create the repo on GitHub, run `git remote add origin` with its URL, then `git push -u origin main`. Nothing is obtainable, discoverable, or backed up until this is done.

**Nice-to-have:**
- Replace the README's "Status: complete" headline with the classified maturity.
- Lead the README with Positioning's refined one-liner.
- Add the symlink step and an expected-output-shape example to the README Setup/Usage section.
- Record a 20–40s terminal GIF of one combined run.
- Set GitHub Topics once the remote exists.
- Re-create the `/home/vscode/.claude/agents/` symlinks (also Deployment step 3) — `CLAUDE.md` claims they exist; they do not on this machine.

---

## Distribution Guide

### Overview

Eight platforms in `platforms/*.yaml` list `AI agent` in their `category_fit` and are scored below: Hacker News, Dev.to, Product Hunt, Claude Code Plugin/Marketplace, Niche Communities, GitHub Topics, Awesome Lists, Indie Hackers. Four are excluded outright (not shown with a low score, per the methodology): `itch-io` and `steam` (game only), `app-stores-mobile` (mobile app only), and `package-registries` (dev tool / CLI only — and its own `stack_fit_notes` rules out a pure Claude Code agent with no installable package artifact, which is exactly this project).

Composite scores use the rubric formula `(reach x 0.4) + (audience_fit x 0.4) + ((6 - effort) x 0.2)`, with `reach` and `effort` taken verbatim from each YAML and `audience_fit` judged against the classified `target_user` (solo developers / small teams who finished a project and can't get it seen, plus this repo's own maintainer).

### One shared precondition gates the entire list

Every platform below requires the same three things that do not yet exist, so **there is nothing in "Ready Now."** This is one blocker with eight downstream effects, not eight separate problems:

1. **No public repository.** The git repo has a single local commit and no remote — nothing has ever been pushed. Every channel here needs a URL to link to (a Show HN post, a Dev.to back-link, a marketplace listing, a topic tag). There is currently no such URL.
2. **No `LICENSE` file.** Default copyright is all-rights-reserved: anyone who finds the project cannot legally use it. Launching a tool whose entire pitch is "get your project adopted" into a state where adoption is legally blocked is self-defeating, and several channels (Awesome Lists especially) reject unlicensed projects on sight.
3. **Phase 5 + 6 work is uncommitted.** `positioning-specialist.md`, `pricing-specialist.md`, `docs/`, `lib/`, and three ref files are untracked; six files are modified-unstaged. A fresh clone of `HEAD` today is missing `plan.md` at either path and two of the five specialists — it does not run. This must be committed before the repo is pushed.

The Shipping Guide section above covers the mechanics of items 1–3. Distribution cannot begin until they are done. Everything below is sequenced so that the moment the precondition clears, the order of execution is already decided.

**What you can prepare while blocked (not a launch, just runway):** draft the Show HN title and first comment; draft the Dev.to build-story post; pick the GitHub topic tags; and start participating genuinely in the niche communities named below so a launch post there isn't a first post.

### Ready Now

**Empty.** No platform's prerequisites are met, because the shared precondition above (public licensed repo, fully committed) is unmet. Per the scoring methodology's override rule, a high composite score never promotes a platform out of Blocked — so Hacker News (4.0) and the rest all wait.

### Blocked (do these first — ordered by composite score, which is the order to launch once unblocked)

**1. Hacker News (Show HN) — composite 4.0/5 (reach 4, audience fit 4, effort 2) · time to value: fast**
   Why: HN's audience is "developers and technical founders evaluating tools for their own use" — a direct match for solo developers who just shipped something. The YAML's `stack_fit_notes` explicitly calls HN a good fit for a Claude Code agent with no hosted URL, because HN readers read READMEs and source directly rather than needing a polished demo. Highest composite in the set and fast time-to-value.
   Prerequisites: YAML lists none, but the shared precondition applies — the Show HN must link to a public repo, which does not exist yet (project-state). Satisfy via: push the committed, licensed repo to GitHub (Shipping Guide).
   Launch risk to plan for (name collision): "GTM agent" is an established 2026 term for sales/outbound automation, and HN will pattern-match a bare "Show HN: GTM Agent" as yet another sales tool and dismiss it. Use the refined positioning one-liner as the title tail and open the first comment by distinguishing it from sales-automation "GTM agents" and by stating honestly that Phases 5–6 are not yet validated end-to-end — HN rewards that and punishes evasiveness.
   First step: post with a title in the shape "Show HN: I built an agent that writes the launch plan for the project you just finished".

**2. Dev.to (launch/tutorial post) — composite 3.4/5 (reach 3, audience fit 4, effort 3) · time to value: medium**
   Why: Dev.to's audience is developers reading "how I built X" and build-in-public write-ups. This project has genuine technical substance to carry a real post — the two-wave orchestration, five specialists arguing from one shared classification, and the deliberate split between static ref files (method) and live search (substance). That is a stronger fit than a bare announcement channel. Audience fit 4 rather than 5 because Dev.to skews toward general web/app developers, only some of whom are the "I finished a project and can't get it seen" persona.
   Prerequisites: the YAML prerequisite ("enough substance for a real technical post") is genuinely met — the architecture story is real. The blocker is the shared precondition: a build-story post that can't link to a usable, licensed repo underperforms badly. Satisfy via: same repo push as step 1.
   First step: write a tutorial-style or build-story post that uses the project as the example, not a direct pitch.

**3. Product Hunt — composite 3.4/5 (reach 5, audience fit 2, effort 3) · time to value: fast**
   Why: highest raw reach in the registry (5), but audience fit is only 2 — PH's crowd rewards a strong visual first impression and a one-click try, and the YAML's `stack_fit_notes` calls a pure Claude Code agent with no hosted surface "a weak fit unless it has a companion CLI/demo to point at." This project is `.md` files; there is nothing to click. The prerequisite override, not the score, is what places it here — but even unblocked, this is a lower-value channel for this project type than its composite suggests, and may not be worth the effort at all.
   Prerequisites (all unmet, project-state and preparation): (a) "a live, visitable product, demo, or install path" — none exists; (b) "3+ early testimonials or usage signals before launch day" — the project has zero external users and no validated end-to-end run; (c) launch assets (tagline, 3–5 gallery images/GIFs, maker's first comment) — not prepared. Satisfy via: run steps 1 and 4 first — Hacker News and the niche communities are where the testimonials and usage signals PH's algorithm needs actually come from (this is the dependency the scoring methodology's own worked example describes); separately, build at least a recorded demo (an asciinema/GIF of a real `@gtm-agent` run producing a guide) so there is something visitable.
   First step: create a hunter account, or find an established hunter to submit on your behalf — but only after steps 1 and 4 have produced seed testimonials.

**4. Claude Code Plugin / Marketplace Distribution — composite 3.2/5 (reach 2, audience fit 4, effort 2) · time to value: medium**
   Why: this is the one channel in the registry specific to this repo's own output type (Claude Code agents), and its audience — Claude Code users browsing for agents to install — is a high-intent subset of the target user, with zero friction to try (a marketplace install vs. cloning and reading docs). That would normally be audience fit 5. It is scored 4 because of a channel-specific collision (below) that directly suppresses discoverability here.
   Name collision (critical for this entry): `gtmagents/gtm-agents` — a same-named Claude Code agent collection, ~96 stars — is **already listed on the Claude Code plugin marketplace**. Marketplace discovery is by browsing and searching a small catalog, so listing "GTM Agent" here means competing for the exact same search term against an established incumbent and looking like a fork of it. A listing under a colliding name is worse than no listing. Resolve the naming question from the Positioning section before publishing here.
   Prerequisites (unmet, mixed): the YAML asks the agent be "stable and already dogfooded/self-tested" — partially true (dogfooded across 6 targets) but **Phases 5 and 6, which added two of the five specialists and the two-wave execution model, have never been run end to end**, and there is no automated test suite. A marketplace listing invites cold install traffic that would hit exactly that unvalidated path. Plus the shared precondition (repo must be public; agent must be packaged as a plugin). Satisfy via: run a real end-to-end combined-mode test (the steps are in `docs/HowTo.md` Part 6) and stand up at least a minimal fixture test; settle the name; then package per the current plugin/marketplace docs (verify against Claude Code's own documentation at submission time — this mechanism changes faster than any other channel here).
   First step: confirm the canonical `.md` files live in `.claude/agents/` and are symlinked into the personal tier (the local-use baseline), then package the agent and its refs/YAML as a Claude Code plugin.

**5. Niche Communities (Reddit / Discord) — composite 3.2/5 (reach 2, audience fit 4, effort 2) · time to value: medium**
   Why: small total reach per post, but members are self-selected around the exact interest, so a well-placed post out-converts a broad platform per visitor. Audience fit 4 because the right communities for this project are populated by precisely the target user (Claude Code users and solo devs shipping side projects).
   Instantiated communities for this project (not the generic pattern):
   - **r/ClaudeAI** (and r/ClaudeCode if active) — Claude Code users are the zero-friction audience; frame as "I built an agent that writes a launch plan for a finished project," with an honest note on the unvalidated phases.
   - **The official Claude Developers Discord** — the "built with Claude" / showcase channels; this is the audience most able to install and run it immediately.
   - **r/SideProject and/or r/EntrepreneurRideAlong** — solo developers who have shipped something and are figuring out distribution: the target-user persona almost exactly. Build-in-public framing, not an announcement.
   - Optional: the discussion space around the `awesome-claude-code` list.
   Prerequisites: the YAML prerequisite — "enough standing in the community to post without looking like a drive-by promoter" — is an operator-preparation item, not a project defect: you'll need to have participated genuinely in two or three of these for a few weeks before you post a launch. Plus the shared precondition (a repo link to point at). In Claude Code communities specifically, expect the same "GTM agent" collision with the existing `gtm-agents` collection — lead with what's different.
   First step: identify the 2–3 communities above, read each one's self-promotion rules exactly, and start participating now (while the precondition is being cleared).

**6. GitHub Topics — composite 3.0/5 (reach 2, audience fit 3, effort 1) · time to value: slow**
   Why: passive, compounding discovery for developers who search GitHub by subject rather than arriving from a launch post. Lowest effort in the entire registry (1) — a two-minute task. Audience fit 3: it reaches developers generally, not specifically the "can't get my project seen" persona, and it is a slow trickle, not a spike.
   Prerequisites: the YAML lists none, but the workflow's first step ("Repo → About → Topics") is impossible until the repo exists on GitHub (project-state — the shared precondition). This is the single fastest prerequisite to clear and the first thing to do the moment the repo is pushed.
   First step: on the pushed repo, open About (gear icon) → Topics and add 5–10 specific tags — e.g. `claude-code`, `claude-code-agent`, `ai-agent`, `go-to-market`, `gtm`, `product-launch`, `developer-tools`, `markdown` — not generic terms like `tool`.

**7. Curated "Awesome X" GitHub Lists — composite 2.6/5 (reach 1, audience fit 3, effort 1) · time to value: slow**
   Why: lowest reach in the registry (1) but also lowest effort — high trust per click since inclusion implies vetting, tiny absolute traffic. Worth doing, never worth prioritizing over a launch-day channel. Target lists for this project: an `awesome-claude-code`-style list, `awesome-ai-agents`, and possibly a "build in public / indie" list.
   Prerequisites (project-state, unmet): the YAML asks for "a genuinely complete, documented project — most Awesome lists' contribution guidelines reject unfinished or undocumented entries," and many explicitly require an open-source license. With no `LICENSE`, no public repo, and two phases unvalidated, a strict list maintainer will treat this as unfinished. Satisfy via: the shared precondition plus at least one real external validation signal (e.g. the Hacker News thread from step 1), then open a one-line PR per list following its `CONTRIBUTING.md` exactly.
   First step: find 2–3 relevant Awesome lists and read each one's `CONTRIBUTING.md` before touching anything.

**8. Indie Hackers — composite 2.4/5 (reach 2, audience fit 2, effort 2) · time to value: medium**
   Why: lowest composite in the set. IH's audience is founders "building and monetizing their own products," receptive to build-in-public posts with a revenue or founder-journey angle. The YAML's own `notes` warn that "an agent-definition project with no monetization story is a weaker fit here even though `category_fit` technically matches" — which is this project today (an internal portfolio tool, no commercial model decided yet). Hence audience fit 2.
   Prerequisites: YAML lists none, but a meaningful IH product page and forum post need a story that doesn't exist yet — the commercial model is still being decided (see the Pricing & Packaging section below). Plus the shared precondition. Satisfy via: decide the free/paid/open-source model from the Pricing section, push the repo, and only then post — framed as a build-in-public milestone if and when there's a monetization or open-source-adoption angle to report.
   First step: after the commercial model is decided, create a product page under the Products directory.

### Recommended sequence

Nothing ships until the one precondition is cleared: **commit the Phase 5–6 work, add a `LICENSE`, and push the repo to a public GitHub remote** (the Shipping Guide covers this). The instant that is done, **set GitHub Topics** (step 6 — two minutes, do it immediately). Then run the real launch in this order: **Hacker News Show HN** first (step 1 — highest fit, fast, and the source of the credible testimonials later channels need), immediately followed by posting into the **niche communities** you've been participating in — r/ClaudeAI, the Claude Developers Discord, and r/SideProject (step 5). Once those two have produced usage signals and feedback, publish the **Dev.to build-story post** (step 2) and add the project to 2–3 **Awesome lists** (step 7). Only after all of that — and only after settling the name collision from the Positioning section and running a real end-to-end test of Phases 5–6 — pursue the **Claude Code plugin marketplace** listing (step 4), where a same-named incumbent is already on the shelf. Treat **Product Hunt** (step 3) as optional and low-priority for a no-hosted-surface agent, and only attempt it with a recorded demo and the testimonials from steps 1 and 5 in hand. **Indie Hackers** (step 8) waits until there is a commercial-model story to tell.

---

## Marketing Plan

### Ongoing Strategy

**Pitch target (assumed, not specified):** early adopter — per `pitch-and-outreach.md`'s script step 5, defaulted because the classified `target_user` is solo developers and the project has nothing to sell (no LICENSE, no price, no public repo). Everything below is written for "get five real people to run it and tell you what broke," not for a buyer or a backer.

#### 0. Before any of this: there is currently nothing to market

This is not a marketing tactic, it is the gate on all of them. The observed repo state is: one commit, no git remote, no `LICENSE`, and all Phase 5 + Phase 6 work uncommitted. **Nobody can obtain this project today**, and with no license the default is all-rights-reserved — so even a reader who found the repo could not legally use it. Additionally, per the Positioning section, the name currently routes the exact audience you want to a different market.

Do not run a single item in the cadence below until: (a) Phase 5+6 work is committed, (b) a `LICENSE` exists, (c) a public remote exists, (d) the name question from the Positioning section is resolved. Publishing content that points at a repo people can't get is the one move here that spends credibility for nothing (general practice — `pitch-and-outreach.md`'s transparency lever, inverted).

#### 1. What the live search actually says about this field's discovery structure

Three findings shape everything downstream. All three are specific to the Claude Code agent/extension field, not general marketing advice.

**Finding A — the marketplace is not a distribution channel.** Claude Code plugins use a decentralized model: "There's no single app store — plugins come from marketplaces you add yourself, and once a marketplace is registered, its plugins become installable" (source: [Install Claude Code Plugins + Add a Marketplace (2026), MCSA Guru](https://mcsaguru.com/install-claude-code-plugins-marketplace-guide); corroborated by [Create and distribute a plugin marketplace, Claude Code Docs](https://code.claude.com/docs/en/plugin-marketplaces)). The official `claude-plugins-official` marketplace is added automatically; the community one (`anthropics/claude-plugins-community`) must be added manually and only carries plugins that passed automated safety screening (same sources).

*Consequence for this project:* being listed is not being found. Any plan that treats "submit to the marketplace" as the distribution step is wrong for this field. Listing is a prerequisite for installability, not a source of traffic.

**Finding B — curated "awesome" lists are the de facto discovery layer.** "The awesome lists became the discovery layer that GitHub's own search doesn't provide" (source: [How a Curated Awesome List Hit 42K Stars in 11 Months, gitpicks.dev](https://gitpicks.dev/featured/claude-code-awesome-list-42k-stars)). Concrete scale: `awesome-claude-code` crossed 42,000 stars in 11 months (same source); `hesreallyhim/awesome-claude-code` is cited at 47.6k stars and `affaan-m/everything-claude-code` at 163k+ (source: [Awesome Claude Code: 11 Curated Lists Worth Bookmarking, claudefa.st](https://claudefa.st/blog/tools/resources/awesome-claude-code)).

*Consequence:* the highest-leverage single distribution action in this field is a PR to two or three of those lists — which the Distribution Guide ranks as step 7, and which is gated on the repo actually existing.

**Finding C — coverage counts are commoditized; verification is scarce.** A single competing toolkit advertises "135 agents, 35 curated skills, 42 commands, 176+ plugins, 20 hooks" (source: [rohitg00/awesome-claude-code-toolkit, GitHub](https://github.com/rohitg00/awesome-claude-code-toolkit)). Meanwhile reviewers testing the ecosystem report the opposite problem: "The biggest frustration was never whether plugins work — it's that it's almost impossible to tell what 'working' actually means until you've run one on something real" (source: [7 Claude Code Plugins From the Marketplace Worth Your Time, Security Boulevard, June 2026](https://securityboulevard.com/2026/06/7-claude-code-plugins-from-the-marketplace-worth-your-time/)), and the review format that has emerged is explicitly winnowing — "11 Tested, 4 Worth Keeping" (source: [Best Claude Code Plugins (2026), buildtolaunch](https://buildtolaunch.substack.com/p/best-claude-code-plugins-tested-review)).

*Consequence — this is the most important finding for this specific project:* your "12 platforms / 8 refs / 5 specialists" numbers compete directly against a repo claiming 135 agents and lose. Positioning already flagged those counts as merely true, and the search independently confirms why: counts are the saturated axis. **The scarce asset in this field is a record of the tool being run on something real** — and that is the one asset this project actually has (six dogfood targets with named, verifiable findings). Your content strategy should be built almost entirely on that asset and almost not at all on capability lists.

#### 2. What I searched for and deliberately did not use

Making this visible is part of the deliverable, per `pitch-and-outreach.md`'s scope-matching rule.

- **Discarded — AI coding market size.** The field survey returned Cursor at $2B ARR, Claude at $2.5B annualized, Google's $2.4B Windsurf acqui-hire (source: [The Complete Guide to Agentic Coding Tools in 2026, datalakehousehub](https://datalakehousehub.com/blog/agentic-coding-tools/)). Real numbers, wrong population: they measure enterprise/prosumer spend on *coding* agents, and say nothing about whether a solo developer will adopt a free launch-planning agent. Using them as "why now" would be exactly the fabricated-authority move the ref file names.
- **Discarded — viral consumer launch.** Outbid.lol drew 1M visitors and $120k in bids in 48 hours from an August 2026 launch (source: [The Globe and Mail, Newsfile](https://www.theglobeandmail.com/investing/markets/markets-news/Newsfile/3992894/120-000-and-one-million-visitors-in-48-hours-for-solo-founder-s-side-project-outbid-lol/)). A consumer auction novelty. No transfer to a developer tool; citing it would be survivorship theater.
- **Discarded — paid long-tail search.** A solo-founder playbook recommends €10–20/day on long-tail commercial Google keywords once a landing page converts (source: [Solo Founder Marketing 2026, lishchuk.com](https://lishchuk.com/blog/solo-founder-marketing-playbook-2026.html)). Not applicable here on three counts: no landing page, nothing to buy, and — decisively — the name collision means the keyword set you'd bid on returns sales-automation tooling (per the Positioning section). Revisit only if the name changes *and* a paid tier exists.
- **Used with an explicit scope caveat** — the solo-founder cadence numbers in §3 below. Flagged inline where they appear.

#### 3. The cadence

Structured in three stages against actual maturity (functional / untested-in-production, zero users). Per `pitch-and-outreach.md`'s social-proof ladder, the "no users yet" rung applies: lean on the maker's own credibility and the clarity of the problem, never on fabricated proof (general practice). No case studies with metrics, no "trusted by" language, no install counts — you have none.

**Stage 1 — Weeks 1–2: make the artifact findable and legible (not promotional)**

| Action | Why | Source |
|---|---|---|
| Commit Phase 5+6, add a LICENSE, push a public remote | Nothing below functions without it | observed repo state |
| Publish the six dogfood `GTM_GUIDE.md` outputs *in the repo*, unedited, including the ones that criticize this repo | The one thing reviewers say is missing from this ecosystem is evidence of a tool run on something real | (source: Security Boulevard, June 2026 — Finding C) |
| Rewrite the README's opening line to the plain-language problem, not the category name | The audience searches "how do I launch my side project," never "GTM" | Positioning section; supported by Finding A (no central search surface to rank in) |
| Keep the "Phase 5 and 6 are not yet validated by a real end-to-end run" line prominently in the README | Transparency about maturity earns more credibility with a technical audience than polish that outruns substance | (general practice — `pitch-and-outreach.md`, trust levers) |

**Stage 2 — Weeks 2–6: the discovery layer, in the order the search says matters**

1. **PR into 2–3 curated lists.** This is the top-ranked field-specific action (source: gitpicks.dev, Finding B). Target the general Claude Code lists and any subagent-specific list. Worth doing first because it is the only channel the search identifies as substituting for GitHub's own search — not because it guarantees traffic.
2. **Register the plugin marketplace entry** — but treat it as an installability prerequisite, not a launch (source: MCSA Guru / Claude Code Docs, Finding A). Note the community marketplace requires manual addition and safety screening, so budget review latency rather than assuming same-day availability.
3. **Write one post in the format the field already rewards: the winnowing review.** Not "introducing my agent." The proven-in-this-field artifact is the tested-and-discarded writeup (source: buildtolaunch, "11 Tested, 4 Worth Keeping"). Your version writes itself and is honest: *"I pointed a launch-planning agent at six of my own finished projects. Three had no git repository at all. One's `.gitignore` excluded the very file it shipped. One's docs claimed no competing tooling existed when two vendors had shipped it months earlier. Here's every finding."* This is the single highest-value content asset available to this project, it requires no new work, and it demonstrates the tool by consequence rather than by description.

**Stage 3 — Ongoing: consistency over intensity**

- A steady, honest update cadence outperforms one launch burst followed by silence (general practice — `pitch-and-outreach.md`). For this project the natural beat is *one finding per post*: each time you run it against a new target, publish what it caught.
- **Build-in-public, with a scope caveat.** One 2026 solo-founder playbook claims building in public 3–5×/week for 90 days drives "2–4× faster early acquisition," and frames Product Hunt as a milestone earned after 60–90 days of presence, with a Top-5 finish typically worth ~1,500 visits and ~120 signups (source: [Solo Founder Marketing 2026, lishchuk.com](https://lishchuk.com/blog/solo-founder-marketing-playbook-2026.html)). **Scope limits, stated plainly:** this is a single practitioner playbook, not an independent study; its measured population is solo *SaaS* founders with a landing page and a signup funnel, not maintainers of a free Claude Code agent. The *directional* claim (sustained presence beats a cold launch) is consistent with the durable framework and worth acting on; the *numbers* do not transfer — you have no signup to convert, and "1,500 visits" against a repo means stars and issues, which is a different and much noisier signal. Do not plan against those figures.
- **Community-first.** The same playbook observes that solo founders who succeed "built for communities they're already part of" (same source, advisory rather than measured — treat as directional). This one happens to be structurally true here: the maintainer builds Claude Code agents and the audience is people who build Claude Code agents. That is a genuine asset, and it means participating in those communities on their terms first, before any ask (general practice — mirrors `niche-communities.yaml`'s standing prerequisite).

#### 4. Trust-building specific to this project

- **Lead with the failure, not the feature.** Your `docs/plan.md` records that the first run against an outside project deadlocked twice and needed a human to hand-drive recovery. Publishing that — and what you changed because of it — is more persuasive to this audience than any capability list, and it is the concrete form of the transparency lever (general practice) reinforced by Finding C's "can't tell what working means" complaint.
- **Never claim validation you don't have.** The README already says Phases 5 and 6 are unvalidated by a real end-to-end run. Keep that. The moment marketing copy rounds "implemented" up to "tested," the dogfood record — your only real asset — loses the property that makes it worth anything.
- **Do not market the `PaymentAgent` / `donation-specialist` handoff externally.** Per the Positioning section it is non-copyable but only valuable to the in-repo maintainer, and negative value to an external solo developer, for whom it reads as a dependency on a repo they don't have.
- **Do not pitch "guides only, never actions" as a benefit.** Positioning explicitly calls it a scope boundary, not a differentiator. Stated as a feature it sounds like a limitation with good PR; stated where it belongs — in the README's scope section — it reads as honest.

### Pitch / Meeting Script

Written for an **early adopter**: another developer who builds or uses Claude Code agents, encountered in a community thread, a DM, or a short call. Spoken length ~90 seconds. All five parts per `pitch-and-outreach.md`'s structure.

> **[Hook]**
> "You know the part after the project is done? Where it works, it's on your disk, and that's it — nobody knows it exists, and you don't really know where you'd even start. Not 'I need users,' more like: there's a list of things you're supposed to do to launch something and you've never seen the list.
>
> **[Why now]**
> The thing that makes it worse right now is that for Claude Code agents specifically, there's no central place to be found. The plugin system is deliberately decentralized — there's no single app store, people add marketplaces themselves. So getting listed doesn't get you discovered. What actually functions as the discovery layer is a handful of community-curated 'awesome' lists — one of them went from nothing to 42,000 stars in eleven months, precisely because GitHub's own search doesn't do that job. And on the other side, the collections you're competing with advertise 135 agents, 176 plugins. So the counts are saturated, and the reviewers who test this stuff say the actual frustration isn't whether things work, it's that you can't tell what 'working' means until someone's run it on something real. Which means the scarce thing isn't features. It's evidence.
>
> **[What it is]**
> So: it's a Claude Code agent you point at a project you've already finished. It reads your README, your plan, your CLAUDE.md, works out what kind of thing you built and who it's for, and writes you back the launch plan — how to position it, what to fix before showing it, which platforms to go to in what order and why, and what to charge. It's a document you execute. It doesn't post anything or deploy anything.
>
> **[Proof]**
> I want to be straight about where this is: it has zero users. That's not modesty, that's the actual state. What it does have is a record of being run on real things. I pointed it at six finished projects — five of mine and one outside the repo. It found that three of them had no git repository at all, so they weren't obtainable by anyone. One had a `.gitignore` that excluded the very agent file it shipped, so the GitHub copy was broken. One's docs claimed no competing tooling existed in its category when two vendors had shipped exactly that months earlier. On the external project, the highest-value thing it found was a name collision with a 350,000-star project in the same niche. And when I pointed it at its own repo, it flagged its own README as stale rather than writing me a flattering review.
> It also broke. The first run against a project outside the repo deadlocked twice — a sub-agent crashed mid-output and the orchestrator sat there waiting for a signal that never came, and I had to hand-drive the recovery. That's what the last two phases of work were: a failure-recovery contract, a quality gate, a positioning pass so the collision finding isn't luck. Those two phases have not yet been validated by a real end-to-end run. I'd rather tell you that now than have you find it.
>
> **[The ask]**
> What I want is one run against a project of yours that I didn't build — that's the gap in everything above; every real run so far has been mine. Point it at something you finished and never launched, and tell me two things: which section was wrong about your project, and which section you'd actually act on. Fifteen minutes of your time, and I'd rather have the section that's wrong than a compliment. Worth a try this week?"

**Notes on the script.** The hook is deliberately in the user's language, not the project's — per the Positioning section, the target user searches "how do I launch my side project," never "GTM," so the word "go-to-market" appears nowhere. The "why now" rests on three live findings (decentralized marketplace, awesome-lists-as-discovery-layer, count saturation vs. verification scarcity), all cited in §1 above. The proof step claims nothing beyond the dogfood record — no users, no stars, no adoption — and leads with the deadlock, which is the strongest available trust move for a technical audience at this maturity (general practice).

#### Written variant (issue comment / DM / forum reply — the realistic channel here)

Follows `pitch-and-outreach.md`'s five-part outreach structure. Three fields are yours to fill per recipient and are marked in braces; everything else is final copy. Do not send it cold with a generic opener — the first line must reference something the recipient actually said.

> Saw your note about {the specific thing they said} — the "it's finished and now what" part is the bit I've been stuck on too.
>
> I built a Claude Code agent that reads a finished project and writes back the launch plan: positioning, what to fix first, which platforms in what order, what to charge. Guides you follow, not actions it takes.
>
> Honest state: zero users. What it has instead is a record — I ran it on six real projects and it found that three of them had no git repo at all, one shipped a `.gitignore` that excluded its own agent file, and one's docs claimed a category was empty when two vendors were already in it. Pointed at its own repo, it flagged its own README as stale. It also deadlocked twice on the first outside project and I had to recover it by hand; the fix for that is in, but unvalidated.
>
> Would you run it once on something of yours I've never seen and tell me which section is wrong? That's the specific gap — every real run so far has been my own code. Repo's here: {repo URL}. Yes or no is a fine answer.
>
> — {your name}, building Claude Code agents in the open; this one came out of needing it for my own shelf of finished-but-invisible projects.

### What's field-specific vs. generic in this plan

The field-specific material is everything traceable to the four live searches and only that: the decentralized-marketplace structure that makes "get listed" a prerequisite rather than a distribution channel (Claude Code Docs / MCSA Guru); curated awesome-lists functioning as the discovery layer GitHub search doesn't provide, with the 42k-in-11-months growth figure (gitpicks.dev, claudefa.st); the saturation of coverage counts against a competing 135-agent/176-plugin toolkit (rohitg00 repo); and the reviewer-side complaint that nobody can tell what "working" means without seeing a tool run on something real, plus the winnowing-review format that has emerged in response (Security Boulevard, buildtolaunch). Those four are what make Stage 2's ordering — lists before marketplace, evidence-post before announcement-post — a claim about *this* ecosystem rather than a hunch. Everything else is generic and labeled as such: the social-proof ladder matched to maturity, transparency-as-trust-lever, consistency over intensity, community participation before an ask, and the five-part script skeleton all come from `refs/pitch-and-outreach.md`'s durable framework and would apply to any project at this stage. The solo-founder cadence figures (build-in-public 3–5×/week, Product Hunt ~1,500 visits / ~120 signups) sit deliberately in between and are flagged where they appear: the direction is consistent with the durable framework, but the measured population is solo SaaS founders with a signup funnel, not maintainers of a free Claude Code agent, so the numbers are cited and then explicitly not planned against. Four searches also produced material I discarded outright rather than stretched — AI-coding-market revenue figures and a viral consumer launch — and §2 names them, because in this domain what was rejected for scope mismatch is part of the evidence that what remains was not.

*No recommendation here is a prediction. Every tactic is framed as worth trying because of a stated finding; none will reliably produce a given number of users, stars, or installs. This is tactical guidance, not PR, legal, or financial counsel.*

**Sources:** [MCSA Guru — Install Claude Code Plugins + Add a Marketplace (2026)](https://mcsaguru.com/install-claude-code-plugins-marketplace-guide) · [Claude Code Docs — Create and distribute a plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces) · [gitpicks.dev — How a Curated Awesome List Hit 42K Stars in 11 Months](https://gitpicks.dev/featured/claude-code-awesome-list-42k-stars) · [claudefa.st — Awesome Claude Code: 11 Curated Lists Worth Bookmarking](https://claudefa.st/blog/tools/resources/awesome-claude-code) · [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) · [Security Boulevard — 7 Claude Code Plugins From the Marketplace Worth Your Time (June 2026)](https://securityboulevard.com/2026/06/7-claude-code-plugins-from-the-marketplace-worth-your-time/) · [buildtolaunch — Best Claude Code Plugins (2026): 11 Tested, 4 Worth Keeping](https://buildtolaunch.substack.com/p/best-claude-code-plugins-tested-review) · [lishchuk.com — Solo Founder Marketing 2026](https://lishchuk.com/blog/solo-founder-marketing-playbook-2026.html) · [datalakehousehub — The Complete Guide to Agentic Coding Tools in 2026](https://datalakehousehub.com/blog/agentic-coding-tools/) *(cited only as discarded)* · [The Globe and Mail — Outbid.lol](https://www.theglobeandmail.com/investing/markets/markets-news/Newsfile/3992894/120-000-and-one-million-visitors-in-48-hours-for-solo-founder-s-side-project-outbid-lol/) *(cited only as discarded)*

---

## Pricing & Packaging

### License

**Recommended: MIT.**

The goal this is reasoned against is stated in the **parent `Dev_Agents/CLAUDE.md`, "What This Repository Is"**: *"a portfolio of high-value, production-ready agents that can be sold, licensed, or donated as open-source tools."* GTM_Agent's own `docs/plan.md` §8 quotes the same line as the reason the Pricing specialist exists at all. That goal is deliberately disjunctive — three futures, not one — so the license question is really "which choice keeps the most of them open while costing the least right now."

Three reasons MIT fits *this* project specifically:

1. **Of the three futures the goal names, MIT is the only one that forecloses nothing you can currently act on.** "Donated as open-source tools" is directly satisfied; "licensed" and "sold" remain available for *services, hosted variants, and the sibling agents* under their own licenses, since MIT on GTM_Agent binds only GTM_Agent. A copyleft or source-available choice would trade a revenue path this project has no evidence it can use for adoption it demonstrably needs.
2. **Every named competitor in this exact niche is already MIT and free.** `gtmagents/gtm-agents` (92 agents + 52 skills) is open-source ([source](https://github.com/gtmagents/gtm-agents)), and the `gtm-skills`/LeadMagic collection is "100% free and open source under the MIT license, no paywalls, no signup required" ([source](https://gtm-skills.com/), [source](https://leadmagic.io/gtm-skills)). Positioning found this project is *behind* on distribution against those. Adding license friction at the one place you are already losing is the wrong direction.
3. **The artifact is prompt text, and copyleft's protection model doesn't reach it.** Copyleft assumes a distribution boundary — you ship a binary, the obligation attaches. An agent `.md` is read, paraphrased, and re-typed; `refs/platform-scoring-methodology.md` is a public Markdown file that a competitor can absorb the *ideas* out of without ever copying a line. GPL/AGPL here would buy near-zero real protection and pay full adoption cost for it. (Positioning already scored that rubric "merely true" for exactly this reason.)

**What it gives up:** MIT is irrevocable for anything released under it. A better-resourced competitor — `gtm-agents` is the obvious one — can take the two-wave orchestration design, the scoring rubric, and the ref-file method wholesale, ship them under their own name inside a collection that already has marketplace distribution, and give nothing back. You are trading leverage for reach on purpose, and you cannot undo that trade for code already published.

*If corporate/enterprise adoption later becomes a real goal, Apache-2.0 is the same permissive shape with explicit patent language; it is a swap, not a different strategy.*

**Two things to settle before publishing, and one to take to counsel:**

- **Scope the LICENSE deliberately.** This repo is a portfolio of self-contained agents with different commercial futures (`Dev_Agents/CLAUDE.md` Development Rule 1). A single MIT file at the `Dev_Agents/` root would silently MIT-license `LegalAgent` and `PaymentAgent` too. Put the file at `GTM_Agent/LICENSE`, per-project.
- **Contributor licensing (CLA vs. DCO) is cheapest to decide now,** while the outside-contributor count is zero. Retrofitting one after a public repo takes contributions means getting agreement from everyone who already contributed. **Whether you need one, and which, is a question for counsel — this guide names it and stops there.**
- **Trademark is a separate question from the license, and Positioning made it live.** "GTM agent" is an established 2026 industry term and `gtmagents/gtm-agents` occupies the near-identical name. MIT governs the code; it says nothing about whether this project may use that name. **Confirm the naming question with counsel before any public launch.** No trademark reasoning is offered here, and Positioning's namespace check is not a trademark search.

### Free vs. Paid

**Recommendation: free — MIT plus a donation link. No commercial machinery, now or at the next milestone.**

This is the recommendation, not a hedge on the way to a paid tier. Four things force it:

- **Nothing here can currently carry a price premium.** Positioning's own summary is blunt: one narrowly-defensible differentiator (a single classification feeding five sections that argue from one shared position), one that is defensible *only for the in-repo maintainer* (the `PaymentAgent`/`donation-specialist` handoff — which is **negative** value to an external solo developer who doesn't own those siblings), and everything else merely true. A price has to be defended against a $0 MIT incumbent that is further along on distribution. There is no argument to make yet.
- **Frictionlessness is the entire distribution advantage.** The install route is the Claude Code plugin marketplace, where free directories (skills.sh, claudeskills.info, Anthropic's own in-product directory) are the default discovery path ([source](https://kissmyskills.com/blogs/news/best-claude-skills-marketplaces-2026)). A price is a decision, imposed at precisely the moment the project needs there to be nothing to decide.
- **The classified maturity does not support a support obligation.** Functional / untested-in-production: Phases 5 and 6 are implemented and *never validated by a real end-to-end run*, there is no automated test suite, and `docs/plan.md` §8 states that caveat three separate times. Taking money creates an expectation against software that has not yet been run start-to-finish by anyone.
- **The prior question isn't price, it's existence.** No `LICENSE` (default all-rights-reserved — nobody may legally use or modify it today even if they somehow obtained it), no git remote, nothing ever pushed, all Phase 5+6 work uncommitted, zero users. Pricing answers "how much"; this project has not yet answered "can anyone get it."

**What free actually buys here:** the honest return on GTM_Agent is credibility for the portfolio — a working, publicly inspectable capstone that makes the *sellable* agents in `Dev_Agents/` (`LegalAgent`, `PaymentAgent`) more credible. That is a legitimate return, and it is maximized by being free and visible, not by being priced and unused.

**The deferred paid decision — for when the maturity actually changes, not this week.** Revisit only when three conditions hold simultaneously: the repo is public with a real remote, at least one *external* end-to-end run has happened, and someone who is not the maintainer has asked for a change. If that day comes, the boundary that would survive scrutiny is narrow:

- **Free forever:** all five specialists, all eight ref files, combined mode, the classification pass. This is the point of the tool; gating it would fail the "is the paid thing fair to gate" test outright.
- **The only thing fair to gate:** the *maintained* `platforms/*.yaml` registry — submission workflows, marketplace channels, and effort/reach ratings are the one component that genuinely decays (the Claude Code plugin marketplace's own channel already shifted in 2026, per this repo's own deferred-items note). That is the honest subscription pitch — "you are paying me to keep this current" — and it maps to your recurring cost, not to withholding a capability.
- **Model, if so:** subscription for the registry; **not** one-time. One-time is the right model for a bounded event, and a stale registry is exactly the thing a one-time fee stops paying for.
- **Range, with its reasoning — and note it is speculative until demand exists:** the two brackets the search supports are that individual paid Claude skills sell one-time at **$3.99–$14.99** ([source](https://kissmyskills.com/blogs/news/best-claude-skills-marketplaces-2026)) and that a solo founder's *entire* fixed tool budget runs about **$19–50/month** ([source](https://saasranger.com/blog/indie-hacker-tool-stack-what-successful-solo-founders-actually-use/)). A registry subscription competing against $0 MIT alternatives has to sit at the very bottom of that budget to be a non-decision — roughly **$3–8/month, or a $20–35 one-time for a pinned snapshot**. That range comes from those two brackets plus the fact that the free alternatives are the buyer's realistic default, not from any observed willingness to pay for this specific thing.
- **Tax and revenue-recognition treatment of any recurring charge — including how a merchant-of-record arrangement changes what you owe and where — is an accountant's question.** It is named here because a subscription raises it; it is not answered here.

### What Comparable Tools Charge

Chosen by **same buyer** (a solo developer who has finished something and needs it seen), not by same technology. Prices checked 2026-08-31; marketplace operators change pricing without notice.

| Tool | Model | Current price | Notes |
|---|---|---|---|
| **gtmagents/gtm-agents** — Claude Code GTM agent collection, 92 agents + 52 skills | Open source | **$0** ([source](https://github.com/gtmagents/gtm-agents)) | The nearest namesake and Positioning's severe collision. Serves a *different* buyer (revenue/sales teams), but competes for the same name and the same marketplace shelf. Its price is the one this project's would be read against. |
| **gtm-skills / LeadMagic GTM Skills** | Open source, MIT | **$0** — "no paywalls, no signup required, no usage limits" ([source](https://gtm-skills.com/), [source](https://leadmagic.io/gtm-skills)) | **Flag — free artifact attached to a larger business.** LeadMagic is a commercial GTM vendor publishing these skills alongside its own product; what it actually monetizes was not confirmed in this search. Either way an unfunded solo project cannot match "free forever, professionally maintained" structurally. This is the free incumbent, and free incumbents are the hardest price point to beat. |
| **Paid Claude Code skills marketplaces** (KissMySkills, Claude Protocol, Agensi's security-scanned listings) | One-time, **per skill** | **$3.99–$14.99 per skill** ([source](https://kissmyskills.com/blogs/news/best-claude-skills-marketplaces-2026)) | Normalization: *per skill, one-time* — a five-specialist bundle is not 5× this, and these sit inside marketplaces that monetize listing/curation, so the number reflects a shelf price, not a standalone product's economics. Figures come from marketplace operators' own comparison content, not audited listings; treat as an indicative band. This is the only evidence found that anyone pays for a Claude Code artifact at all. |
| **Directory-submission / launch services** (LaunchDirectories, LaunchIgniter, StartupSubmit) | One-time | **$99–$199** for 100–220+ manual submissions; **$0.50–$5.99 per directory** ([source](https://launchdirectories.com/best-directory-submission-service), [source](https://launchigniter.com/submit-directories), [source](https://startupsubmit.app/), [source](https://smollaunch.com/best-of/directory-submission-services-compared-2026)) | **Flag — model does not transfer.** These sell *execution*: a human submits your product and sends back live links. GTM_Agent explicitly never executes (`docs/plan.md` §4, guides-only). This is the price of doing the work; the price of the advice about the work is a different and much smaller number. Anchoring on $99–199 would be the single most misleading thing this table could do. |
| **Status quo: a free blog checklist and doing it yourself** | Free | **$0** | The real default for this buyer, and the one most of them will keep choosing. Context: the whole solo-founder fixed stack is **$19–50/month** ([source](https://saasranger.com/blog/indie-hacker-tool-stack-what-successful-solo-founders-actually-use/)), so any new line item competes inside that ceiling, not against enterprise budgets. |

Not confirmed by this search: any paid product that sells a *generated launch plan* for indie developers — the closest paid category found sells submissions instead. Absence of a comparable is itself a finding, and it cuts both ways: possibly an unserved gap, more likely a signal that this buyer does not pay for plans.

### Next Step — `donation-specialist` Handoff

`PaymentAgent/scaffold.py` **does not apply here, and should not be bent to fit.** Its `--stack` tokens are `nextjs`, `fastapi`, `express`, `django`, `sveltekit` and its `--db` values are `prisma`, `sqlalchemy`, `django-orm` (confirmed against `PaymentAgent/scaffold.py`'s own `SUPPORTED_*` constants and `--list` output). GTM_Agent has no hosted runtime, no web framework, and no database — there is no application for a webhook handler or checkout route to live in. `@payment-setup-agent` is equally wrong: the provider is not *undecided*, there is simply nothing to charge for at this maturity.

The correct handoff, matching the stay-free recommendation:

```
@donation-specialist GTM_Agent is a free, MIT-licensed Claude Code agent that reads a finished
project and writes back its launch plan (positioning, shipping, distribution, marketing, pricing).
Zero users, first public release pending. Set up a donation path — Buy Me a Coffee and/or Patreon —
and write the funding blurb for the README and the repo's FUNDING.yml.
```

**Why this invocation:** `donation-specialist` (in `ContentPost_agent`) is the agent that covers Buy Me a Coffee and Patreon and writes the actual posts, so the donation path becomes a named executable step rather than an unassigned "add a donate link"; there is no provider, stack, db, or payment-model choice to make because the recommendation is free, which is also why no `scaffold.py` flags appear above.

**Two things gate even that**, and both are yours to run — nothing here has been executed:

1. Add `GTM_Agent/LICENSE` containing the MIT text with your copyright line. Until it exists the project is all-rights-reserved and the free recommendation is not actually in effect.
2. Commit the Phase 5 + 6 work and push to a remote. The pricing question is downstream of the distribution question, and right now nobody can obtain this at any price.
