#!/usr/bin/env python3
"""Discover the latest official source files and write a source manifest.

This deliberately stores source metadata first. PDF/XLSX table parsing should be
validated per report format before it is allowed to overwrite dashboard values.
"""
import json, re, sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin

try:
    import requests
except ImportError:
    print("Install dependencies with: pip install requests", file=sys.stderr)
    raise SystemExit(1)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "sources.json"
SOURCES = {
    "sama_pos": "https://sama.gov.sa/en-US/Statistics/Indices/pages/pos.aspx",
    "sama_money_supply": "https://sama.gov.sa/ar-sa/Statistics/Indices/pages/weeklymoneysupply.aspx",
    "cma_open_data": "https://cma.gov.sa/AboutCMA/ResearchAndReports/opendata/Pages/default.aspx",
}

def discover(url):
    try:
        r = requests.get(url, timeout=30, headers={"User-Agent": "SaudiMarketPulse/0.1"})
        r.raise_for_status()
        links = []
        for raw in re.findall(r'href=["\']([^"\']+)["\']', r.text, re.I):
            if any(ext in raw.lower() for ext in (".pdf", ".xlsx", ".xls", ".csv")):
                links.append(urljoin(url, raw))
        return {"status": "reachable", "url": url, "files": list(dict.fromkeys(links))[:10]}
    except Exception as exc:
        return {"status": "unavailable", "url": url, "files": [], "error": str(exc)}

manifest = {"retrieved_at": datetime.now(timezone.utc).isoformat(), "sources": {k: discover(v) for k, v in SOURCES.items()}}
OUT.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
print(f"Wrote {OUT}")
for name, item in manifest["sources"].items():
    print(f"{name}: {item['status']} ({len(item['files'])} files discovered)")
