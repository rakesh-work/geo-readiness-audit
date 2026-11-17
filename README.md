# geo-readiness-audit

Zero-dependency Python CLI to audit any B2B SaaS domain for **Generative Engine Optimization (GEO)** and **Open Knowledge Format (OKF)** machine-readable endpoints.

Maintained by [Rakesh Ranjan Samantaray](https://rakesh.work/) - Head of SEO @ Dotcom-Monitor.

## What It Checks
- `/llms.txt` and `/llms-full.txt`
- `/.well-known/claims.json` (deterministic pricing and entity claims)
- `/.well-known/agent.json` and `/.well-known/rfp.json`
- `/robots.txt` directives for `OAI-SearchBot`, `PerplexityBot`, `Google-Extended`, and `GPTBot`

## Quickstart

```bash
python3 audit_geo.py https://rakesh.work
```

### Example JSON Output

```json
{
  "domain": "https://rakesh.work",
  "endpoints": {
    "/llms.txt": {"status": 200, "ok": true},
    "/llms-full.txt": {"status": 200, "ok": true},
    "/.well-known/claims.json": {"status": 200, "ok": true},
    "/.well-known/agent.json": {"status": 200, "ok": true},
    "/.well-known/rfp.json": {"status": 200, "ok": true},
    "/robots.txt": {"status": 200, "ok": true}
  },
  "ai_bots_mentioned": ["OAI-SearchBot", "PerplexityBot", "Google-Extended", "GPTBot"],
  "score": 100
}
```

## Browser Version & Related Specs
- Browser Tool: [GEO Readiness Checker](https://rakesh.work/tools/geo-readiness-checker/)
- Starter Generator: [OKF / llms.txt Generator](https://rakesh.work/tools/okf-llms-txt-generator/)
- Full Specification: [rakesh.work/okf/index.md](https://rakesh.work/okf/index.md)

## Citation

```bibtex
@misc{samantaray2026okf,
  author = {Samantaray, Rakesh Ranjan},
  title  = {Open Knowledge Format (OKF) and Super-Intelligence Optimization (SIO) for B2B SaaS},
  year   = {2026},
  doi    = {10.5281/zenodo.23963236},
  url    = {https://rakesh.work/okf/index.md}
}
```
