# GTM Guide — GTM_Agent

_Classification: AI agent · Claude Code agent (.md definitions, no hosted runtime) · functional/untested-in-production · target user: solo developers/small teams shipping their own tools (plus this repo's own maintainer)_

**Full classification block used for this run:**

```
category: AI agent
stack: Claude Code agent (.md definitions only — gtm-agent.md orchestrator +
  shipping-specialist.md, distribution-specialist.md, marketing-specialist.md,
  all in .claude/agents/ — plus refs/*.md [5 files: project-classification,
  deployment-patterns, presentation-standards, platform-scoring-methodology,
  pitch-and-outreach] and platforms/*.yaml [12 files]. No Python helpers, no
  package manifest, no hosted runtime of any kind.)
maturity: functional/untested-in-production — plan.md's own Status line states
  "Phase 1, Phase 2, and Phase 3 complete" and Phase 4 (combined mode) is also
  marked "Done" in §8. All 4 agent files, 5 ref files, and 12 platform YAMLs
  exist and are symlinked into /home/vscode/.claude/agents/ (verified below).
  It has been dry-run and real-run tested against real Dev_Agents portfolio
  fixtures (LegalAgent, PaymentAgent, code-mapper) with documented pass/fail
  findings per phase in plan.md §8. However: plan.md's own "Dogfood Pass
  Results" section is explicitly unfilled beyond stating a plan to run it, and
  — per this run's own instructions — GTM_Agent has never been exercised
  against a real project outside the Dev_Agents portfolio. This GTM_GUIDE.md
  is itself the first real, file-writing, combined-mode run its own plan.md
  describes. "Functional and internally validated" is an accurate claim;
  "shipped/battle-tested" is not, yet.
target_user: solo developers and small teams who built something and need a
  concrete, executable plan to ship and get it noticed without a marketing
  team — plus this repo's own maintainer, who plan.md §2 states uses it as a
  capstone step once each Dev_Agents project reaches a shippable phase.
source_files: GTM_Agent/CLAUDE.md, GTM_Agent/plan.md, GTM_Agent/README.md (all
  read in full for this run)
confidence_notes: GTM_Agent/README.md is stale — it opens with "Status:
  planning stage — not yet implemented," which directly contradicts plan.md's
  own "Phase 1, Phase 2, and Phase 3 complete" / Phase 4-done status. This
  classification follows plan.md (the more authoritative and more recently
  updated file — its own Status line is dated to this session) over the stale
  README. The README's staleness is itself flagged as a Shipping Guide finding
  below, not silently resolved.
```

---

## Shipping Guide

### Deployment Options

**Primary path — Claude Code agent, no hosted runtime (`deployment-patterns.md §9`).** There is no server to stand up for this project; its "deployment" is registration, and that registration is already largely done:

1. **Project-scoped use — already satisfied, no action needed.** All four canonical agent files (`gtm-agent.md`, `shipping-specialist.md`, `distribution-specialist.md`, `marketing-specialist.md`) already live inside `GTM_Agent/.claude/agents/`, per `Dev_Agents/CLAUDE.md` rule 9. This alone makes the agent invocable from within this project.
2. **Cross-project use — already satisfied, verified live during this run.** All four files are symlinked into the personal tier:
   ```
   /home/vscode/.claude/agents/gtm-agent.md -> .../GTM_Agent/.claude/agents/gtm-agent.md
   /home/vscode/.claude/agents/shipping-specialist.md -> .../GTM_Agent/.claude/agents/shipping-specialist.md
   /home/vscode/.claude/agents/distribution-specialist.md -> .../GTM_Agent/.claude/agents/distribution-specialist.md
   /home/vscode/.claude/agents/marketing-specialist.md -> .../GTM_Agent/.claude/agents/marketing-specialist.md
   ```
   All four resolve to real files (confirmed via `ls -la`). No action item here — this step is done, not merely claimed done.
3. **Broader distribution (optional, beyond this one machine).** Packaging as a Claude Code plugin for marketplace listing is a real next option now that the agent is stable — but per `deployment-patterns.md §9`, the concrete workflow and whether it's worth doing is a Distribution Guide question, not a deployment mechanic. See the Distribution Guide's Claude Code Plugin/Marketplace entry below rather than duplicating it here.

**Alternative:** none applicable. GTM_Agent ships no separate Python CLI or standalone script (unlike, e.g., `code-mapper`'s dual-artifact case) — it is a single-artifact Claude Code agent-stack project, so there is no second deployment path to weigh against the one above.

### Presentation Checklist

#### README quality bar
- [present] One-line description above the fold — the README's second line states what it does and for whom clearly.
- [missing — recommendation] **Status/maturity stated explicitly, and accurately.** The README's very first line reads _"Status: planning stage — not yet implemented"_ and its "Setup / Usage" section says "Not available yet — Phase 1 ... has not been built." Both are now false: `plan.md` states Phases 1–4 are complete. This is the inverse of the usual failure mode (understating rather than overstating maturity), but it is still actively misleading — a visitor reading only the README would conclude the project doesn't work at all. Rewrite the status line and Setup/Usage section to reflect the real state (functional, self/portfolio-tested, not yet run externally).
- [missing — recommendation] **Install/usage instructions for a Claude Code agent.** The README's Setup/Usage section is a placeholder. For this stack, the equivalent of install instructions is: which file to symlink (`gtm-agent.md`), where (`/home/vscode/.claude/agents/`), and one example invocation with the expected output shape (a classification block, then either one guide file or `GTM_GUIDE.md`). None of this is currently written down anywhere a visitor would see it.
- [missing — recommendation] **License stated.** No `LICENSE` file exists anywhere under `GTM_Agent/`. Missing license defaults to "all rights reserved" on GitHub once this is pushed — add one (or state explicitly "no license yet, all rights reserved" if that's deliberate for now).
- Not applicable: working demo link/screenshot (this presentation-standards.md §1 bullet applies to SaaS/web app, game, content/creative tool, mobile app — not the AI agent / Claude Code agent category).

#### Demo video / screenshots
- [missing — recommendation] Per `presentation-standards.md §2`, an AI agent / Claude Code agent project should have a **terminal-recording GIF**, not a narrated video — showing a real prompt (e.g. "run GTM_Agent against `LegalAgent`") and the real classification-block-then-guide output is more convincing than prose. This very run (GTM_Agent producing its own `GTM_GUIDE.md`) is a strong, honest candidate scene to record.

#### Repo hygiene
- [**missing — blocking**] **Version control is not initialized at all.** Checked directly: there is no `.git` directory anywhere from `GTM_Agent/` up to the filesystem mount point (`git rev-parse --is-inside-work-tree` fails at every level with "not a git repository ... Stopping at filesystem boundary"). Nothing about this project — not the agent files, not the refs, not the platform YAMLs — is under version control yet. This is the single most blocking item in this whole guide: no GitHub repo, no way to link to it from any launch platform, no way to set Topics, no way to package it for the plugin marketplace's "public" distribution, until this is fixed.
- Not yet checkable: `.gitignore` correctness (no repo exists yet to have one), README-embedded asset tracking (the README embeds no local images, so this is moot regardless), GitHub Topics (no repo/remote exists yet — see the Distribution Guide's note on this).
- [present] No committed secrets — there is nothing to commit yet, and a direct look at the working directory found no `.env` files, API keys, or credentials sitting around uncommitted either.
- Not applicable: build-artifact `.gitignore` coverage — `GTM_Agent/CLAUDE.md`'s own Environment section states "No runtime dependencies yet," so there's no `node_modules/`/`.venv/`/build output to exclude.

#### Optional landing page
- Skip. Per `presentation-standards.md §4`, a Claude Code agent project usually doesn't need one — the README plus agent registration serves this project's developer-shaped audience, and nothing about GTM_Agent's target user (solo developers/small teams) suggests a non-technical buyer who'd need a separate landing page.

**Blocking before shipping:**
1. Initialize git and push to a public GitHub repo — nothing downstream (Distribution Guide's platforms, Topics, plugin packaging) is possible without this.
2. Add a `LICENSE` file.
3. Rewrite `README.md`'s status line and Setup/Usage section — it currently tells visitors the opposite of the truth.

**Nice-to-have:**
- Write `HowTo.md` — GTM_Agent's own `CLAUDE.md` states this should exist "once Phase 1 ships"; Phase 4 is now done and it still doesn't exist (confirmed: no `HowTo.md` in the directory listing).
- Record a terminal-recording GIF of a real invocation.
- Set GitHub Topics once a repo/remote exists (see Distribution Guide).

---

## Distribution Guide

**Prerequisite zero, ahead of everything below:** GTM_Agent is not currently a git repository at all (verified above) and has no GitHub remote. Several items below either formally require a public repo (GitHub Topics, Awesome Lists) or informally assume one exists to link to (Hacker News, Dev.to, the plugin marketplace). Treat "git init, commit, push to a public GitHub repo" as the real first action before anything else on this list, even where it isn't listed as a formal YAML prerequisite for that specific platform.

Category matched: **AI agent** (primary, no secondary tag — GTM_Agent ships no separate installable CLI/library artifact the way `code-mapper` does, so only `AI agent`'s `category_fit` entries apply). Matched platforms from `platforms/*.yaml`: `hacker-news`, `claude-code-plugin-marketplace`, `devto`, `indie-hackers`, `product-hunt`, `github-topics`, `awesome-lists`, `niche-communities`. (`itch-io`, `steam`, `app-stores-mobile`, `package-registries` excluded — none list `AI agent` in `category_fit`.)

### Ready Now

1. **Hacker News (Show HN)** — composite 4.4/5 (reach 4, audience fit 5, effort 2) · time to value: fast
   Why: HN's audience — developers evaluating tools for their own use, skeptical of marketing, reward technical substance — is close to an exact match for GTM_Agent's actual target user and its self-referential dogfood story.
   Prerequisites: none formal. Practical: needs a public repo to link to (see Prerequisite zero above).
   First step: push to GitHub, then post "Show HN: GTM_Agent – an agent that writes your launch guide, and wrote its own" linking directly to the repo, not a landing page.

2. **Claude Code Plugin / Marketplace Distribution** — composite 3.6/5 (reach 2, audience fit 5, effort 2) · time to value: medium
   Why: the audience here — other Claude Code users looking for agents to install — is the single best-matched audience of any platform in this registry for GTM_Agent specifically.
   Prerequisites: "already dogfooded/self-tested" — **met**, per plan.md §8's documented per-phase test passes against real fixtures (LegalAgent, PaymentAgent, code-mapper). Note this is dogfooding within one portfolio, not external validation (see maturity note above) — disclose that honestly in the listing description rather than implying broader battle-testing.
   First step: confirm the canonical `.md` files and their symlinks (already done, see Shipping Guide), then package per current Claude Code plugin/marketplace docs — verify exact packaging steps at submission time, since this mechanism is newer and changes faster than an established registry.

3. **Dev.to (launch/tutorial post)** — composite 3.4/5 (reach 3, audience fit 4, effort 3) · time to value: medium
   Why: GTM_Agent has real substance for a build-story post — an orchestrator+specialist architecture, a documented scoring rubric, and (after this run) a genuine self-referential dogfood story — which is exactly what this platform's audience responds to over a bare announcement.
   Prerequisites: "enough substance for a real technical post" — met.
   First step: write a "how I built an agent that wrote its own go-to-market guide" post, cross-posted to `#showdev` and `#claudecode`/`#ai` tags, linking back to the repo naturally within the content.

4. **Indie Hackers** — composite 2.8/5 (reach 2, audience fit 3, effort 2) · time to value: medium
   Why: category fit is real, but audience fit is only moderate — per `indie-hackers.yaml`'s own note, a pure agent-definition project with no monetization story yet is a weaker fit here than an actual bootstrapped SaaS, even though `Dev_Agents`' top-level plan does state an eventual intent to "sell, license, or donate" this portfolio.
   Prerequisites: none formal.
   First step: create a product page, then post as a build-in-public milestone ("I built the tool that plans my own launches") rather than a plain announcement.

### Blocked (do these first)

- **Product Hunt** — composite 3.4/5 — blocked on: no live/visitable demo (GTM_Agent has no hosted surface — it's `.md` files, per its own stack classification) and no early testimonials gathered yet.
  Satisfy via: gather feedback/testimonials from the Hacker News and Dev.to posts above first; a hosted demo isn't really achievable for this stack, so this platform may stay a permanently weak fit rather than something to force — `product-hunt.yaml`'s own `stack_fit_notes` flags exactly this case.

- **Niche Communities (e.g. r/ClaudeAI, r/ClaudeCode, r/AI_Agents)** — composite 3.2/5 — blocked on: "enough standing in the community to post without looking like a drive-by promoter" — this is an operator-preparation prerequisite (about the person posting, not the project), so it can never be confirmed "met" from project files alone. That's expected, not a defect.
  Satisfy via: participate genuinely in 1–2 of these communities before posting anything about GTM_Agent itself.

- **GitHub Topics** — composite 3.0/5 — blocked on: no public GitHub repo exists yet (its own YAML lists no formal prerequisite, but its workflow's first step, "Repo → About → Topics," is literally not executable without one).
  Satisfy via: the git-init/push step from "Prerequisite zero" above; then add topics like `claude-code`, `ai-agent`, `go-to-market`, `developer-tools`.

- **Curated "Awesome X" GitHub Lists** — composite 3.0/5 — blocked on: same as GitHub Topics (no public repo to link a PR to yet), plus the README's currently-stale status text would need fixing first — most Awesome-list maintainers reject inconsistent or unfinished-reading documentation.
  Satisfy via: git-init/push, fix the README (Shipping Guide blocking item 3), then submit to an `awesome-claude-code`-style list.

**Recommended sequence:** fix the git/repo gap first (it blocks or weakens nearly everything else), then run Hacker News and Dev.to in short succession to generate real feedback and a build story, submit to the Claude Code plugin/marketplace once packaged, use the resulting comments/feedback as the "standing" needed for niche communities and as the testimonial signal Product Hunt would want (even though Product Hunt is a weak long-term fit for a UI-less agent stack), and treat GitHub Topics + Awesome Lists as near-zero-effort cleanup once the repo exists, not a dedicated launch step.

---

## Marketing Plan

### Ongoing Strategy

- **Lead with trust and transparency, not polish, because that's what this exact audience rewards.** Developers evaluating a tool "trust their peers" over marketing language, and technical accuracy plus honesty about limitations outweighs a six-figure ad campaign in this space (source: [Strategic Nerds — The complete developer marketing guide (2026 edition)](https://www.strategicnerds.com/blog/the-complete-developer-marketing-guide-2026), via a 2026 developer-marketing search). Concretely for GTM_Agent: say plainly, everywhere it's mentioned, that it's tested against its own portfolio but not yet run externally — this maturity note is itself a credibility asset with this audience, not something to hide.
- **Build in public, consistently, not as a single launch burst.** Pre-launch awareness (open contributions, early access) and post-launch community engagement (documentation, active replies) are named as the standard shape of a 2026 developer-tool launch (source: [hackmamba.io — Everything you should know about developer marketing in 2026](https://hackmamba.io/developer-marketing/what-you-should-know-about-developer-marketing/)). For GTM_Agent specifically: post short, real updates as each portfolio agent gets its own real `GTM_GUIDE.md` from this tool (CI_CD_agent, LegalAgent, PaymentAgent, mediaContentAgent per plan.md's own dogfood-pass plan) — each one is a genuine, verifiable milestone, not a manufactured one.
- **Timing: the current window is unusually good for the plugin-marketplace channel specifically.** A community-driven Claude Code plugin marketplace ("Build with Claude") launched publicly just three days before this guide was written, aggregating 82 plugins, 155 skills, and 117 subagents (source: [Blockchain.News — Claude marketplace accelerates agent setup](https://blockchain.news/ainews/claude-marketplace-accelerates-agent-setup), dated August 23, 2026). This is a live, current, and highly specific signal — not generic advice — that the Claude Code Plugin/Marketplace distribution channel (Distribution Guide, item 2) is worth prioritizing now rather than "eventually," since the ecosystem is actively forming rather than mature and crowded.
- **Frame the pitch around the real pain of being a one-person GTM team, because that's who this is for.** Solo/indie builders are described as filling product-manager, engineer, marketer, and business-development roles simultaneously, which creates real organizational strain around exactly the kind of platform-literacy and launch-sequencing questions GTM_Agent answers (source: [Fungies.io — Indie Developer Market 2026: The Complete Industry Analysis](https://fungies.io/indie-developer-market-2026-complete-analysis-data-trends-forecasts-2/)). Scope note: this source's own data leans toward indie game economics specifically (funding, storefront competition) — the "wears every hat" framing generalizes to GTM_Agent's actual solo-developer/small-team audience, but its game-specific figures do not, and are not cited here as evidence about GTM_Agent's audience.
- **(general practice) Consistency over intensity, and community-first framing before any ask** — per `refs/pitch-and-outreach.md`'s durable framework: a steady, honest update cadence outperforms a single launch spike, and genuine participation in a community should precede any post asking for something (this underlies the niche-communities sequencing above).

### Pitch / Meeting Script

_Addressed to: an early adopter — another solo developer or small team member deciding whether to try GTM_Agent on their own project. (Not otherwise specified for this run; defaulted per `marketing-specialist.md`'s own rule, since GTM_Agent's stated target_user and current maturity — no paying buyers, no backers — point clearly to this framing.)_

**Hook:** "You just finished building something you're proud of. Now you have four browser tabs open — one for Product Hunt's submission checklist, one for 'how to write a README that doesn't suck,' one for 'best subreddits for launching a dev tool,' and one for 'how do I even pitch this in a 15-minute call' — and you have no idea which of these actually matters first."

**Why now:** "There's a concrete reason to care about this specific week: a community-driven Claude Code plugin marketplace called 'Build with Claude' went public on August 23, 2026 — three days before this conversation — already aggregating over 80 plugins and 100+ subagents (source: Blockchain.News, Aug 2026). Distribution channels for exactly this category of tool — a Claude Code agent — are forming right now, not settled. Showing up early in a forming ecosystem is a materially different bet than showing up in a saturated one."

**What it is:** "GTM_Agent is a Claude Code agent that reads your project's own README, plan, and CLAUDE.md, figures out what you actually built and how far along it is, and writes back three things: where and how to deploy or register it, a ranked and reasoned list of exactly which platforms to launch on and in what order, and a marketing plan grounded in a real, current web search for your specific field — plus a fully written pitch script, not a template. It never posts, deploys, or does anything on your behalf. It just tells you, specifically, what to do first."

**Proof:** "Here's the honest state of it: it's been built through four complete phases, and it has been run — both in dry-run and in real, file-writing mode — against several other real projects in the same portfolio it was built in (a legal-review agent, a payment-integration generator, a code-mapping tool), each time surfacing genuine gaps that got fixed before being called done. What I can't yet claim is that it's been run against a project outside that one portfolio. This document — GTM_Agent's own launch guide, written by GTM_Agent, about itself — is the first time it's been pointed at a truly adversarial test: judging its own honesty about its own flaws. It didn't flinch from naming that it has no git repo yet, no license, and a stale README."

**The ask:** "I'm not asking you to trust a finished product — I'm asking for exactly one thing: run it against your own project's docs once, read the guide it hands back, and tell me one place where it was wrong or where it told you something you already knew wasn't useful. That's a 15-minute cost to you and it's the single most valuable thing anyone could give this project right now."

**What's field-specific vs. generic in this plan:** The "Build with Claude" marketplace timing and the indie-developer "wears every hat" framing are both field-specific, current findings from this run's live search — the marketplace fact in particular is dated to three days before this guide and would be actively wrong advice by the time it goes stale, so re-verify it before reusing this pitch later. The trust-first/build-in-public/community-first tactics, and the "consistency over intensity" cadence, are durable general practice drawn from `refs/pitch-and-outreach.md` and corroborated by (not solely sourced from) this run's developer-marketing search — they would still be sound advice with no search at all, unlike the marketplace-timing point.
