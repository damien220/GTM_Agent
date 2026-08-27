# Presentation Standards

Defines the quality bar `shipping-specialist` checks a target project against when
building the **presentation checklist** half of `SHIPPING_GUIDE.md` (the other half
is deployment options — see `deployment-patterns.md`). This file answers "is this
project ready to be looked at by a stranger?", independent of whether it's deployed
anywhere yet.

Load this file when: writing the presentation-checklist section of a Shipping
Guide, after the project has already been classified (`project-classification.md`).

## How to use this file

For each section below: check what the target project already has (from the input
files read during classification, plus a look at the repo root if the agent has
filesystem access to it), mark each item **present** or **missing**, and only write
guidance for missing or weak items. Do not restate items that are already
satisfied — a checklist that praises what's already done is noise; the user needs
to know what's left.

Every item below is tagged with which categories it applies to. An item with no
category tag applies to all projects.

## 1. README quality bar

A stranger should be able to read the README top-to-bottom and know what the
project does, whether it's for them, and how to try it — without opening any other
file.

- **A `README.md` actually exists at the project root.** Check this before
  anything else in this section, and flag it as a **blocking** item, not a
  nice-to-have, if it doesn't — GitHub, package registries, and most launch
  platforms only auto-render a file named exactly `README.md`. A project whose
  overview/usage info lives only under other filenames (e.g. a `payment_guide.md`
  + `HowTo.md` pair used for classification per `project-classification.md`'s
  input-substitution note) still needs an actual `README.md` before it's
  presentable to a stranger, even though those substitute files were good enough
  to classify the project from.
- **One-line description above the fold.** What it does and who it's for, in the
  first sentence or two — not a feature list, not the tech stack.
- **Install/usage instructions that actually run.** [dev tool / library, CLI, API]
  A copy-pasteable install command and a minimal working example. If the project
  is a **Claude Code agent** (per the stack special case in
  `project-classification.md`), the equivalent is: which agent file to symlink,
  where, and one example invocation with expected output shape — not `pip install`
  instructions that don't apply.
- **A working demo link or screenshot above the fold.** [SaaS / web app, game,
  content / creative tool, mobile app] Text alone under-sells anything visual;
  see §2 for what "working" means here.
- **Status/maturity stated explicitly.** Carry forward whatever
  `project-classification.md` determined (planning-only /
  in-development-partial / functional-untested / shipped) — don't let the README
  imply more maturity than the classification found, and flag it as a fix if it
  currently does.
- **License stated.** Missing license is treated as "all rights reserved" by
  default on GitHub — flag this explicitly if `LICENSE` is absent, since it's a
  common reason a project gets passed over even when the code is fine.

## 2. Demo video / screenshots / GIFs

This agent does not produce media — see `plan.md §4`. This section is a **brief**
for what the user (or `mediaContentAgent`) should capture, not a generated asset.

- **[SaaS / web app, game, mobile app, content / creative tool] required.** A
  15–60 second screen recording or GIF showing the core loop: the one action that
  demonstrates the value proposition, not a full feature tour. State this as a
  scene brief: what's on screen at second 0, what action happens, what result is
  visible at the end.
- **[dev tool / library, CLI, API] optional but recommended for anything with a
  visual or interactive output** (a CLI with rich terminal output, a codegen tool
  whose output is inspectable). Skip the recommendation entirely for a library
  whose entire interface is a function signature — a static code example in the
  README does more work than a video would.
- **[AI agent / Claude Code agent] recommended as a terminal-recording GIF**, not
  a narrated video — showing an actual prompt and the agent's real output is more
  convincing than a voiceover explaining what it does.
- Where a video is warranted, state the brief as: hook (first 3 seconds), core
  action shown, and the single result that should be visible when it ends. Don't
  specify shot-by-shot direction beyond that — that level of production detail is
  `mediaContentAgent`/the user's call, not this agent's.

## 3. Repo hygiene

- **Version control initialized.** If the target has no `.git` (check
  `is a git repository` state the way this repo's own top-level context reports
  it), this is a blocking item, not a nice-to-have — nothing else in this
  checklist matters if the code isn't in a repo a platform can point to.
- **`.gitignore` doesn't exclude the project's own core files.** Check what
  `.gitignore` actually excludes against what the project needs to function or
  be understood — a project can look complete locally while its repo silently
  ships broken. Treat this as **blocking**, more severe than a missing license:
  it means the published repo doesn't match the working copy at all. Two
  concrete failure shapes to check for specifically: an agent's own definition
  file(s) excluded (e.g. a `.gitignore` line for `CLAUDE.md`, `plan.md`,
  `HowTo.md`, or `.claude/` on an **AI agent**–category project — the thing
  being shipped would be entirely absent from a fresh clone), and dependency/
  build directories excluded appropriately for the detected stack (e.g.
  `node_modules/`, `__pycache__/`, `.venv/` present in `.gitignore`, flagged as
  missing only if absent and the stack implies it).
- **Every asset the README embeds is actually tracked in git**, not just
  present in the local working copy. Cross-check each local image/video
  reference in the README (e.g. `![...](Image.png)`) against `git status`/
  `git ls-files` — an untracked asset renders locally but breaks on a fresh
  clone or on the platform hosting the README (GitHub, npm, PyPI). Flag any
  README-referenced asset that isn't tracked as **blocking**, not cosmetic.
- **`LICENSE` file present** and matches what the README claims (or the README
  claims none, deliberately).
- **Topics/tags set** (GitHub "Topics" or equivalent) — matching the category and
  stack from classification, since this is what makes the project turn up in
  platform search/discovery (feeds directly into `distribution-specialist` in
  Phase 2 — flag it here, don't duplicate platform-specific submission steps).
- **No committed secrets.** A quick sanity check for `.env` files, API keys, or
  credentials committed to the repo — flag immediately and treat as high priority
  if found, since this is a security issue, not a polish issue.
- **`.gitignore` covers build artifacts / dependencies** appropriate to the
  detected stack (e.g. `node_modules/`, `__pycache__/`, `.venv/`) — flag if
  clearly missing and the stack implies it.

## 4. Optional landing page

Not required for every category — call this out explicitly rather than defaulting
to "you should build a landing page," which is generic advice that wastes a dev
tool's time.

- **[SaaS / web app, game, mobile app] worth considering** if there's no other
  place a non-technical visitor could land (i.e., the GitHub README is the only
  thing to point people at). Recommend only a brief (sections, one-line value
  prop, screenshot placement, CTA) — production is out of scope (`plan.md §4`).
- **[dev tool / library, CLI, API, Claude Code agent] usually skip.** The
  README/package registry listing already serves this role for a developer
  audience; recommending a separate landing page here is over-scoping unless the
  project specifically targets non-technical buyers (rare for this category).

## Output format

Render the checklist grouped by the four section headers above, each item marked
`[present]` or `[missing — recommendation]`. Keep recommendations to 1–2 sentences
each; this is a checklist a human executes, not an essay. End with a short
"blocking vs. nice-to-have" summary line so the user knows what to fix before
shipping versus what can wait.

## Worked example

`PaymentAgent` (classified as **AI agent**, Claude Code agent stack,
functional/untested maturity):

```
README quality bar:
- [present] one-line description, install-equivalent (symlink) instructions
- [missing — recommendation] no explicit maturity/status line in README itself
  (it's only in the parent Dev_Agents/CLAUDE.md table) — add one so the README
  stands on its own for someone who lands on it directly, e.g. via GitHub search.
- [present] license (check LICENSE exists in real run)

Demo / screenshots:
- [missing — recommendation] no terminal-recording GIF of `scaffold.py` in action
  — a 20-second recording of one `scaffold.py --provider paddle ...` invocation
  and the resulting file tree would do more than the current text-only usage
  section.

Repo hygiene:
- [present] git repository, no secrets detected
- [missing — recommendation] GitHub Topics not set — add `payments`, `stripe`,
  `paddle`, `claude-code`, `code-generator` once this repo has a remote.

Landing page: skip — dev-tool-shaped audience, README + registry listing suffice.

Blocking: none found. Nice-to-have: README status line, demo GIF, Topics.
```
