# Agent Instructions

> This file is mirrored across CLAUDE.md and GEMINI.md to ensure the same instructions are loaded consistently across all environments.

You operate using a three-layer architecture that separates concerns to maximize reliability and maintainability.

LLMs are probabilistic by nature, whereas most business logic is deterministic and requires consistency, accuracy, and predictability. This architecture bridges that gap by separating probabilistic reasoning from deterministic business logic, ensuring reliable and consistent execution.

## The three layers

### Layer 1 — Directives (what to do)
- Plain-language SOPs in Markdown, stored in `directives/`.
- Each directive states the goal, inputs, which tools/scripts to run, expected outputs, and known edge cases.
- Directives are living documents: when you learn something new (an API limit, a better approach, a failure mode), update the directive.

### Layer 2 — Orchestration (decision making)
- This is you. Read the relevant directive, decide which tools to call and in what order, handle errors, ask for clarification when a decision is genuinely the user's, and update directives with what you learn.
- Do not do deterministic work "by hand" in your head when a script exists or should exist. Route it to Layer 3.

### Layer 3 — Execution (doing the work)
- Deterministic Python scripts in `tools/`. They are reliable, testable, and fast.
- Data and content live in code/data files (e.g. `tools/base_resume.py`, `tools/job_profiles.py`); logic that turns them into outputs lives in scripts (e.g. `tools/build_resumes.py`).
- Generated output goes to `applications/` (git-ignored).

## Operating principles

1. **Check for existing tools first.** Before writing a new script, look in `tools/` and `directives/`.
2. **Self-anneal when things break.** Read the error, fix the script, re-run and verify, then update the directive so the fix sticks.
3. **Keep facts deterministic.** Resume content must come from `tools/base_resume.py`. Job profiles may reword bullets to match a posting's language but must never invent experience; unmet requirements go in a profile's `gaps` list and stay off the resume.
4. **Verify before reporting.** Run the build and confirm its checks pass (e.g. every keyword probe is found) before saying work is done.
5. **Keep the mirror in sync.** Any change to this file must be copied to `GEMINI.md`.

## Repository layout

```
directives/            # Layer 1: SOPs in Markdown
tools/                 # Layer 3: deterministic Python scripts and data
  base_resume.py       #   source-of-truth resume facts (bullets keyed by ID)
  job_profiles.py      #   per-job tailoring: summary, competencies, keywords, rewrites, gaps
  build_resumes.py     #   builds .docx/.pdf per job + KEYWORD_MATCH_REPORT.md
applications/          # generated output (git-ignored)
```
