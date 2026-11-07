# superagent-demo

A tiny demo project for the video **"DeepSeek Super Agent, explained and set up free and local"** by Mervin Praison.

It has one real bug on purpose, so an AI coding agent has something to fix:

- `invoice.py` should return the total **plus** 10% tax, but it returns only the tax.
- `test_invoice.py` catches it: the test fails until the bug is fixed.

```sh
pip install pytest
pytest -q
```

Expected before the fix: `1 failed` (`assert 2.5 == 27.5`).

This repository is used to point DeepSeek's Super Agent prototype
(https://github.com/deepseek-ai/dsh-superagent-prototype) at a real GitHub project.
It is a demo only: please don't open pull requests against it.
