# deos-review-agent-eval

Target "defect garden" for the `deos-review-agent` PR review bot.

This repository contains intentionally seeded defects in pull requests. The
review agent (in `sachinkundu/deos-review`) runs against these PRs as part of
its eval regression suite. The default branch should remain clean; defects live
only in eval PRs.

## Active eval PRs

- [#1 — Eval: seeded defects for review-bot Phase 1](https://github.com/sachinkundu/deos-review-agent-eval/pull/1)
  - Pagination off-by-one on an added line
  - Hallucinated GitHub webhook signature header (`X-GitHub-Signature-Sha256`
    instead of `X-Hub-Signature-256`)
  - PR-body claim mismatch (claims 1-indexed pagination fix, code is still
    0-indexed)

## Adding new eval defects

1. Open a branch from `master`.
2. Add or modify files under `eval_set/`.
3. Reference an issue or project key in the PR body so the agent can test linked
   issue extraction.
4. Make at least one claim in the PR body that the diff does not actually
   implement.
5. Open the PR. The regression harness in `sachinkundu/deos-review` will run
   the agent against it on every agent-code change.
