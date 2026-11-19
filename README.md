# 🗂️ Kleinanzeigen Dataset

A community-maintained snapshot of marketplace category names and identifiers, available in **JSON and CSV**. Prepared by [AnzeigenBoost](https://anzeigenboost.de) for developers building search, analytics and listing tools.

> This is an **unofficial snapshot**, not a live API or an official Kleinanzeigen dataset. It is not affiliated with or endorsed by Kleinanzeigen. The source map was last changed on **17 October 2026** and was **not independently checked against the live site at publication**.

## 📦 What's inside

| Level | Records | Example |
| --- | ---: | --- |
| Top-level categories | 15 | Familie, Kind & Baby |
| Subcategories | 143 | Baby- & Kinderschuhe |
| Third-level labels | 476 | Sneaker & Sportschuhe |

These counts describe the checked-in snapshot only; they are not a claim about current marketplace coverage.

- 📄 [categories.json](data/categories.json) — nested category map.
- 📊 [categories.csv](data/categories.csv) — the same map flattened for spreadsheets and analysis.
- 🔎 [metadata.json](data/metadata.json) — origin, version and limitations.

The first two levels use IDs from the source category map. **Third-level values may be attribute slugs rather than numeric category IDs.** Preserve the parent ID when matching them; do not treat every slug as a globally unique category. No listing records, seller information, prices, brand lists or size lists are included.

## 🚀 Use the data

Download [categories.json](data/categories.json) or [categories.csv](data/categories.csv) from this repository. The JSON is a dictionary keyed by top-level ID, with `label`, `id` and nested `subcategories`. The CSV provides `level`, `id_or_slug`, `label`, `parent_id` and `top_level_id`.

To regenerate the CSV from the checked-in JSON using Python 3:

```bash
python tools/export_csv.py
```

No account, API key or network requests are required for the export.

## 🔍 Source and accuracy

This is an export of the category map already used in the AnzeigenBoost codebase. Its last recorded source-file change is identified in [metadata.json](data/metadata.json). Category names, identifiers and availability can change; please independently verify values before relying on them in production. This repository does not yet contain a verified update schedule.

Found an error? [Open an issue](../../issues) with the category and a public reference, or propose a correction in a pull request. Please do not include customer messages or personal information.

## 📄 License

The scripts in `tools/` are provided under the [MIT License](LICENSE). Category names and identifiers describe a third-party platform; the project does not claim ownership of that platform or grant rights to its trademarks or underlying data. Review applicable platform terms before reuse.
