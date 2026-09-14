# Saudi Market Pulse | نبض السوق السعودي

واجهة تحليلية تفاعلية تجمع مؤشرات الاقتصاد السعودي، نشاط المدفوعات، وتحديثات السوق المالية في تجربة واحدة واضحة.

## Preview

افتح `index.html` مباشرة، أو شغّل خادمًا محليًا:

```bash
python3 -m http.server 4173
```

ثم افتح `http://localhost:4173`.

## Features

- Arabic-first dashboard with newspaper-style Arabic typography.
- Full Arabic/English language toggle.
- Responsive layout for desktop and mobile.
- Interactive particle/network background with pointer response.
- Economic health, liquidity, POS momentum, sector performance, and market-signal cards.
- Official-source catalogue linking to SAMA and CMA pages.
- Demo-mode disclosure so illustrative values are not mistaken for live market data.
- No framework or build step required for the current static MVP.

## Data status

The visual layer is complete, but the displayed KPIs are demo values. The official source catalogue and production ingestion plan are documented in [`data/README.md`](data/README.md).

The production data layer should preserve the source URL, publication date, observation period, retrieval timestamp, and validation status for every observation.

## Roadmap

- [ ] Download and parse the latest SAMA POS PDF/XLSX report.
- [ ] Download and parse weekly money-supply reports.
- [ ] Connect CMA open-data files and classify announcements.
- [ ] Add a normalized historical dataset and automated calculations.
- [ ] Add tooltips, date/sector filters, and a weekly narrative summary.
- [ ] Add automated source-health checks and scheduled refresh.

The repository includes `scripts/ingest_sources.py` to discover the latest official report files and write a source manifest. Because official reports may change layout, table extraction remains a controlled validation step rather than silently publishing unverified numbers.

## Disclaimer

This project is an information and visualization tool. It is not investment advice or a recommendation to buy or sell any security. Always verify figures against the original official source before making a decision.

## License

MIT. See [`LICENSE`](LICENSE).
