"""Average GDP by country report."""

import csv
from collections import defaultdict
from pathlib import Path


def generate(files: list[Path]) -> tuple[list[str], list[list]]:
    """Average GDP by country across all given files."""
    gdp_by_country: dict[str, list[float]] = defaultdict(list)

    for file in files:
        with open(file) as f:
            reader = csv.DictReader(f)
            for row in reader:
                country = row["country"]
                gdp = float(row["gdp"])
                gdp_by_country[country].append(gdp)

    rows = []

    for country, gdps in gdp_by_country.items():
        average_gdp = sum(gdps) / len(gdps)
        rows.append([country, f"{average_gdp:.2f}"])

    rows.sort(key=lambda row: float(row[1]), reverse=True)

    headers = ["Country", "Average GDP"]
    return headers, rows
