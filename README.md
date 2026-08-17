# deos-review-agent-eval

Eval companion for the `deos-review-agent` PR review bot.

This repository contains intentionally seeded defects in pull requests so the
review agent can be exercised against real GitHub diffs and its findings
verified manually. The `main` branch should remain clean; defects live only in
eval PRs.

## Eval set

- `eval_set/pagination.py` — pagination helpers.
- `eval_set/webhook.py` — webhook signature helpers.

See open eval PRs for the current defects under review.
