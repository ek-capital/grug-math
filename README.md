# grug-math

One branch. One math problem. One agent.

## Use

1. Create a branch.
2. Put the exact problem in `problem.md`.
3. Point an agent at the branch and say: **work on it**.

The agent creates whatever code, searches, proofs, tests, and notes it needs.
Nothing else is imposed by the repo.

Check recent research with one uv-managed helper:

```bash
uv run papers.py 'all:"your topic" AND cat:math.CO'
```

The research method is adapted from
[Shouqiao Wang's workflow](https://x.com/Qiaoqiao2001/status/2080003441821163958)
and OpenAI's
[Cycle Double Cover prompt](https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_prompt.pdf).

MIT licensed.
