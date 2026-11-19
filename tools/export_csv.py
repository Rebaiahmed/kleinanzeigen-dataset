#!/usr/bin/env python3
"""Export the checked-in hierarchy as UTF-8 CSV; no network requests."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
source = json.loads((ROOT / "data/categories.json").read_text(encoding="utf-8"))

with (ROOT / "data/categories.csv").open("w", encoding="utf-8", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=["level", "id_or_slug", "label", "parent_id", "top_level_id"], lineterminator="\n")
    writer.writeheader()
    for top in source.values():
        writer.writerow({"level": 1, "id_or_slug": top["id"], "label": top["label"], "parent_id": "", "top_level_id": top["id"]})
        for child in top.get("subcategories", {}).values():
            writer.writerow({"level": 2, "id_or_slug": child["id"], "label": child["label"], "parent_id": top["id"], "top_level_id": top["id"]})
            for leaf in child.get("subcategories", {}).values():
                writer.writerow({"level": 3, "id_or_slug": leaf["id"], "label": leaf["label"], "parent_id": child["id"], "top_level_id": top["id"]})
