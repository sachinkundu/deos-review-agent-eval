# deos-review-agent-eval

Eval companion for the `deos-review-agent` PR review bot.

This repository contains intentionally seeded defects in pull requests so the
review agent can be exercised against real GitHub diffs and its findings
verified manually. The default branch should remain clean; defects live only in
eval PRs.

## Active eval PRs

- [#1 — Eval: seeded defects for review-bot Phase 1](https://github.com/sachinkundu/deos-review-agent-eval/pull/1)
  - Pagination off-by-one on an added line
  - Hallucinated GitHub webhook signature header (`X-GitHub-Signature-Sha256`
    instead of `X-Hub-Signature-256`)
  - PR-body claim mismatch (claims 1-indexed pagination fix, code is still
    0-indexed)

## CI

`.github/workflows/review-bot.yml` runs the agent on every eval PR. It checks
out the review-bot source from the `review-bot-phase-1/impl` branch of
`sachinkundu/deos-review`, installs it with `uv`, and posts a review as the
GitHub App.

Required repository secrets:

- `REVIEW_BOT_APP_ID`
- `REVIEW_BOT_INSTALLATION_ID`
- `REVIEW_BOT_PRIVATE_KEY` (full PEM content)
- `REVIEW_BOT_BOT_USERNAME` (e.g. `deos-review-agent[bot]`)

## Adding new eval defects

1. Open a branch from `master`.
2. Add or modify files under `eval_set/`.
3. Reference an issue or project key in the PR body so the agent can test linked
   issue extraction.
4. Make at least one claim in the PR body that the diff does not actually
   implement.
5. Open the PR; CI will run the agent and post its review.
