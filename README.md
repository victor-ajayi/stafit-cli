# stafit-cli

CLI for processing CSV files with macroeconomic data and generating reports.

## Usage

```bash
python main.py --files data/economic1.csv data/economic2.csv --report average-gdp
```

Multiple CSV files can be passed. The report is built from all files combined.

## Adding New Reports

To add a new report type:

1. Create a handler in `handlers/` following the existing example (`handlers/average_gdp.py`)
2. Register it in `handlers/__init__.py` in the `REPORTS` dict

The handler must return headers and rows. Rows are automatically numbered and printed as a table.

## Installation

Install dependencies with your package manager.

Astral UV:
```bash
uv sync
```

Poetry:
```bash
poetry install
```

## Testing

Run tests with:

```bash
pytest .
```
