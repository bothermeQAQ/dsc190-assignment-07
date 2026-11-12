import csv
from pathlib import Path


def main() -> None:
    source_path = Path("data/clean/events.csv")
    output_path = Path("data/transformed/events.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with (
        source_path.open(encoding="utf-8", newline="") as source,
        output_path.open("w", encoding="utf-8", newline="") as output,
    ):
        reader = csv.DictReader(source)
        writer = csv.DictWriter(output, [*reader.fieldnames, "date"], lineterminator="\n")
        writer.writeheader()
        for row in reader:
            row["date"] = row["timestamp"].split("T", maxsplit=1)[0]
            writer.writerow(row)


if __name__ == "__main__":
    main()
