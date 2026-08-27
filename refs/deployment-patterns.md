# Deployment Patterns

Defines the **deployment options** half of `SHIPPING_GUIDE.md` (the other half is
the presentation checklist — see `presentation-standards.md`). Organized by the
category/stack a project was assigned in `project-classification.md`, since "how
do I ship this" is a fundamentally different question for a hosted web app than
for a package or a Claude Code agent definition.

Load this file when: writing the deployment-options section of a Shipping Guide,
after the project has already been classified.

## How to use this file

Look up the section matching the project's **primary category** from
classification. If the category is ambiguous or spans two sections (e.g. a
content tool that's also a hosted SaaS), use the stack to disambiguate — stack
tells you whether there's a server to host at all. Recommend **one primary path**
plus at most one alternative with a one-line tradeoff — this is a decision the
user has to act on, not a survey of every host that exists. Never recommend
running `terraform apply` or performing the deploy on the user's behalf
(`plan.md §4` — this agent writes guides, it does not deploy).

**Dual-artifact projects are a different case from an ambiguous single category —
don't collapse them into "pick one section."** Some projects genuinely ship two
independent things that each need their own deployment action, not two readings
of the same category. Concretely: `code-mapper` is both a standalone script
(needs §1's package-registry path) *and* ships `agent.md` as a Claude Code
agent (needs §9's registration/symlink path) — these are two separate steps a
human must both do, not alternatives to choose between. When a project's files
show more than one independently-shippable artifact, give each its own short
subsection in Deployment Options rather than picking whichever category seems
"primary" and silently dropping the other artifact's deployment step.

## 1. dev tool / library

Distribution *is* the deployment for this category — there's no server to stand
up.

- **Primary path:** publish to the package registry matching the stack —
  npm (`npm publish`), PyPI (`twine upload` / `uv publish`), crates.io
  (`cargo publish`), RubyGems (`gem push`), or a Homebrew tap for anything CLI
  and cross-language. Recommend semantic versioning and a matching git tag per
  release.
- **Alternative:** GitHub Releases with the raw source/build artifact attached,
  for a tool not yet ready to commit to a registry's namespace/versioning
  guarantees, or aimed at users who'd rather `git clone` than add a registry
  dependency.
- Note CI hookup as a forward pointer, not a step to execute here: publishing on
  tag-push via GitHub Actions is what `CI_CD_agent` (this repo's own tool) is
  for — don't re-derive pipeline config in this guide.

## 2. SaaS / web app

- **Primary path, by piece:**
  - Frontend-only or full-stack framework with serverless API routes (Next.js,
    SvelteKit, Remix): **Vercel** or **Netlify** — connect the git repo, set env
    vars, deploy on push. Fastest path to a live URL.
  - Separate backend (FastAPI, Express, Django) needing a persistent process or
    background jobs: **Railway**, **Render**, or **Fly.io** — pick based on
    whether the project already has a `Dockerfile` (Fly.io and Railway both take
    one directly; Render can build from one or from buildpacks).
  - Anything requiring more control over infra (custom networking, compliance
    requirements, existing cloud spend): **AWS/GCP/Azure** directly — flag that
    this is meaningfully more setup than the above and only worth it if there's
    a specific reason for it.
- **Database:** if the project's stack includes Prisma/SQLAlchemy/Django ORM
  against Postgres, note managed options (Neon, Supabase, Railway Postgres,
  RDS) rather than self-hosting one, unless the project has already made a
  self-hosting choice.
- **Env vars / secrets:** point at the host's environment-variable UI; do not
  restate `PaymentAgent`'s webhook-secret sequencing guidance here — cross-
  reference `PaymentAgent/refs/deployment-and-delivery-guide.md`'s pattern
  (sandbox/production keys are entirely separate, first deploy can succeed
  before the webhook secret exists) as the model to follow if the target project
  has payment webhooks, rather than duplicating it.
- **Custom domain:** mention as a later step once the default host subdomain is
  live and confirmed working — sequencing matters more than the DNS mechanics.

## 3. CLI

Same registries as dev tool / library (§1) if the CLI is installed via a package
manager. Add, when relevant:

- **Standalone binary distribution:** GitHub Releases with prebuilt binaries per
  platform (via `pkg`, `pyinstaller`, `cargo build --release`, or Go's native
  cross-compilation) for a CLI aimed at non-developers who shouldn't need a
  language runtime installed.
- **Homebrew tap** as the primary path specifically for a macOS/Linux-targeted
  CLI with a technical but not necessarily language-specific audience.

## 4. Game

- **Primary path:** **itch.io** — lowest friction, works for a web (HTML5),
  Windows/Mac/Linux, or downloadable build, no upfront cost or review gate.
  Recommend this first for any game without an existing audience or budget for
  a Steam page's $100 setup fee.
- **Alternative:** **Steam (Steamworks)** — much larger discovery surface but
  requires the $100 direct-to-Steam fee, store page assets (trailer, capsule
  images — briefed via `presentation-standards.md §2`, not produced here), and
  a review/approval cycle. Recommend only once the project has validated
  interest elsewhere (itch.io, a demo, a community) — this is a
  `distribution-specialist` prioritization question as much as a deployment one;
  flag the connection rather than re-deriving platform-launch sequencing here.
- **Web export** (itch.io HTML5, or a static host for a WebGL/Godot HTML5
  build) as the zero-install option if the engine supports it — lowest barrier
  for a first playtest audience.

## 5. Mobile app

- **Primary path:** platform's own store — **Apple App Store** (requires an
  Apple Developer account, $99/year, and App Review, which can take days and
  reject on guideline grounds) or **Google Play** ($25 one-time fee, review is
  typically faster and less strict than Apple's).
- **Recommend internal/beta testing first:** **TestFlight** (iOS) or Google
  Play's **Internal/Closed testing tracks** — surfaces crashes and store-listing
  issues before a public review submission, and both are effectively required
  steps rather than optional polish.
- Flag account/verification lead time explicitly (Apple's business verification
  in particular is not instant) the same way `PaymentAgent`'s Paddle guidance
  flags Merchant-of-Record verification lead time — this is a "start it early"
  item, not a same-day step.

## 6. API

- **Primary path:** same host options as SaaS §2's backend row (Railway,
  Render, Fly.io) — an API needs the same "persistent process somewhere" as a
  SaaS backend, just without a frontend to also deploy.
- **Documentation hosting:** recommend publishing an OpenAPI/Swagger spec (many
  frameworks generate this automatically — FastAPI does by default) alongside
  the deploy, since an API with no interactive docs is much harder for a
  potential integrator to evaluate than one with a live `/docs` route.
- **API gateway / rate limiting:** mention as a maturity-dependent add-on
  (Cloudflare, an API gateway service) only if the project's stated target user
  implies public/third-party traffic — skip for an internal-only or single-
  consumer API, where it would be over-engineering advice.

## 7. Content / creative tool

This category splits by stack rather than having its own hosting story — use
whichever of the above actually matches:

- If it's a library/CLI a developer runs locally (e.g. a generation script): use
  §1 (dev tool / library).
  If it's a hosted app end users interact with through a browser: use §2
  (SaaS / web app).
- No separate deployment guidance is needed beyond picking the right section
  above — this entry exists so the category isn't accidentally left unhandled.

## 8. AI agent (general, hosted service)

For an AI agent that runs as a hosted service (a webhook server, an API a user
calls) rather than as a Claude Code subagent: treat as §6 (API) or §2 (SaaS)
depending on whether it has a UI — pick using the same stack signals.

## 9. AI agent — Claude Code agent (the stack special case)

This is the pattern most relevant to `Dev_Agents` itself, since most projects in
this repo classify this way (`project-classification.md`'s Stack special case).
**There is no hosting step** — do not recommend Vercel/Railway/etc. for a project
whose entire "runtime" is Claude Code subagent `.md` files.

- **Primary path — local/project-scoped use:** the agent's canonical `.md` file
  already lives in its own `.claude/agents/` directory (per
  `Dev_Agents/CLAUDE.md` rule 9) — this alone makes it usable within that
  project's own git repository. No further action needed for project-scoped use.
- **Primary path — cross-project use on the same machine:** symlink the
  canonical file into the personal/user-level tier so it's invocable via
  `@agent-name` from any directory, regardless of git-repo boundaries:
  ```bash
  ln -sf /path/to/project/.claude/agents/<agent-name>.md \
         /home/vscode/.claude/agents/<agent-name>.md
  ```
  Verify with `readlink -f /home/vscode/.claude/agents/<agent-name>.md` — per
  `Dev_Agents/CLAUDE.md`'s own note, don't assume the symlink succeeded silently.
  This is machine-local and must be re-created on any other machine the repo is
  cloned onto.
- **Broader distribution (optional, beyond a single machine):** packaging the
  agent as a **Claude Code plugin** for marketplace/team-wide distribution is a
  real option once the agent is stable, but the concrete submission workflow and
  whether it's worth doing for a given agent is a `distribution-specialist`
  question (Phase 2), not a deployment mechanic — flag it here as the forward
  pointer, don't attempt to write that guidance in the Shipping Guide.
- If the project also ships a thin Python CLI/helper alongside the agent
  definitions (e.g. `scaffold.py`, `validate_report.py`), that helper's
  "deployment" is §1 (dev tool / library) if it's meant to be reusable
  standalone — otherwise it stays local, invoked only by the agent's own
  workflow.

## Output format

State the recommended primary path first, in imperative steps (what to click/run,
in order), then at most one alternative with a one-sentence tradeoff. Do not list
every host this file mentions for the category — that's reference material for
this agent, not the guide's output.
