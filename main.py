"""
CLI for processing macroeconomic CSV data and generating reports.
"""

from argparse import ArgumentParser, Namespace
from pathlib import Path

from tabulate import tabulate

from handlers import REPORTS


def parse_args() -> Namespace:
    parser = ArgumentParser(
        description="Process macroeconomic CSV files and generate reports.",
    )
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        type=Path,
        help="Paths to CSV files with economic data.",
    )
    parser.add_argument(
        "--report",
        required=True,
        choices=list(REPORTS),
        help="Report type to generate (e.g. average-gdp).",
    )
    return parser.parse_args()


def main():
    args: Namespace = parse_args()

    func = REPORTS[args.report]
    headers, rows = func(args.files)
    numbered_rows = [[i + 1] + row for i, row in enumerate(rows)]

    colalign = ("right", "left", "right")

    print(
        tabulate(
            numbered_rows,
            headers=["#"] + headers,
            tablefmt="pretty",
            stralign="left",
            numalign="right",
            colalign=colalign,
        )
    )


if __name__ == "__main__":
    main()
