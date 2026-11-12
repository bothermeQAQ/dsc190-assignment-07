import csv
from calendar import Day
from datetime import date
from pathlib import Path


def main() -> None:
    source_path = Path("data/transformed/events.csv")
    output_path = Path("data/features/events.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with (
        source_path.open(encoding="utf-8", newline="") as source,
        output_path.open("w", encoding="utf-8", newline="") as output,
    ):
        reader = csv.DictReader(source)
        columns = [*reader.fieldnames, "duration_minutes", "weekday"]
        writer = csv.DictWriter(output, columns, lineterminator="\n")
        writer.writeheader()
        for row in reader:
            row["duration_minutes"] = str(int(row["duration_seconds"]) / 60)
            row["weekday"] = Day(date.fromisoformat(row["date"]).weekday()).name.title()
            writer.writerow(row)


if __name__ == "__main__":
    main()
