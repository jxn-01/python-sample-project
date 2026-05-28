import argparse
import csv
from pathlib import Path
from typing import Iterable

def load_numbers_from_csv(path: str) -> list[float]:
    """Load numeric values from the first column of a CSV file."""
    file_path = Path(path)
    with file_path.open(newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        numbers = []
        for row in reader:
            if not row:
                continue
            try:
                numbers.append(float(row[0]))
            except ValueError as exc:
                raise ValueError(f"Invalid numeric value in {file_path}: {row[0]!r}") from exc

    if not numbers:
        raise ValueError(f"No numeric values found in {file_path}")

    return numbers

def summarize_numbers(values: Iterable[float]) -> dict[str, float]:
    """Return a simple numeric summary for a list of values."""
    data = list(values)
    if not data:
        raise ValueError("No data to summarize")

    total = sum(data)
    count = len(data)
    return {
        "count": count,
        "sum": total,
        "min": min(data),
        "max": max(data),
        "average": total / count,
    }

def format_summary(summary: dict[str, float]) -> str:
    """Format the summary data as human-readable text."""
    return (
        "Summary\n"
        "-------\n"
        f"Count:   {summary['count']}\n"
        f"Sum:     {summary['sum']:.2f}\n"
        f"Minimum: {summary['min']:.2f}\n"
        f"Maximum: {summary['max']:.2f}\n"
        f"Average: {summary['average']:.2f}\n"
    )

def parse_args(args: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Load numeric data from a CSV file and print a simple summary."
    )
    parser.add_argument(
        "path",
        metavar="CSV_PATH",
        help="Path to a CSV file containing one numeric value per row.",
    )
    return parser.parse_args(args)

def main(args: list[str] | None = None) -> int:
    parsed = parse_args(args)
    numbers = load_numbers_from_csv(parsed.path)
    summary = summarize_numbers(numbers)
    print(format_summary(summary))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
