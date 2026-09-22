# Contributing

**English** · [简体中文](CONTRIBUTING.zh-CN.md)

Thank you for helping improve the JEV ecosystem map.

## Submit a project

Open an issue and include as much of the following as possible:

1. GitHub repository URL;
2. a factual one-line description;
3. where JEV participates in the decision;
4. preferably, an immutable commit link to that source;
5. the project license.

A project mentioned only by topic, repository name, or README stays in the unverified discovery layer until its integration can be located in public source.

## Correct a category or description

Explain what is inaccurate and attach public evidence. Keep descriptions neutral; avoid “fastest,” “best,” or “fully compatible” unless independently reproduced.

## Refresh locally

```bash
python scripts/sync.py
```

After the run, confirm that both README files, both catalogs, `data/`, and `docs/data.js` changed together.
