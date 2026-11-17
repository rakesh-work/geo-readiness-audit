#!/usr/bin/env python3
"""Zero-dependency CLI to audit a B2B SaaS domain for AI search & OKF readiness."""

import json
import sys
import urllib.error
import urllib.request

ENDPOINTS = [
    "/llms.txt",
    "/llms-full.txt",
    "/.well-known/claims.json",
    "/.well-known/agent.json",
    "/.well-known/rfp.json",
    "/robots.txt",
]

AI_BOTS = ["OAI-SearchBot", "PerplexityBot", "Google-Extended", "GPTBot"]


def fetch_url(url: str, timeout: int = 8) -> tuple[int, str]:
    req = urllib.request.Request(
        url, headers={"User-Agent": "geo-readiness-audit/1.0"}
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read().decode("utf-8", errors="ignore")
    except urllib.error.HTTPError as err:
        return err.code, ""
    except Exception:
        return 0, ""


def audit_domain(domain: str) -> dict:
    base = domain.rstrip("/")
    if not base.startswith("http"):
        base = "https://" + base

    results = {
        "domain": base,
        "endpoints": {},
        "ai_bots_mentioned": [],
        "score": 0,
    }
    passed = 0

    for path in ENDPOINTS:
        status, body = fetch_url(base + path)
        ok = status == 200 and len(body.strip()) > 0
        results["endpoints"][path] = {"status": status, "ok": ok}
        if ok:
            passed += 1
        if path == "/robots.txt" and ok:
            for bot in AI_BOTS:
                if bot.lower() in body.lower():
                    results["ai_bots_mentioned"].append(bot)

    results["score"] = round((passed / len(ENDPOINTS)) * 100)
    return results


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 audit_geo.py https://example.com")
        sys.exit(1)
    print(json.dumps(audit_domain(sys.argv[1]), indent=2))
