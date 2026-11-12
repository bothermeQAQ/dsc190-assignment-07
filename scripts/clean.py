import csv
from datetime import datetime
from pathlib import Path

COLUMNS = ("user_id", "timestamp", "event_type", "duration_seconds")
EVENT_TYPES = {"click", "login", "purchase", "scroll", "view"}


def normalize_timestamp(value: str) -> str:
    if "/" in value:
        timestamp = datetime.strptime(value, "%m/%d/%Y %H:%M:%S")
    else:
        timestamp = datetime.fromisoformat(value)
    return timestamp.replace(tzinfo=None).isoformat(timespec="seconds")


def main() -> None:
    source_path = Path("data/raw/events.csv")
    output_path = Path("data/clean/events.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with (
        source_path.open(encoding="utf-8", newline="") as source,
        output_path.open("w", encoding="utf-8", newline="") as output,
    ):
        writer = csv.writer(output, lineterminator="\n")
        writer.writerow(COLUMNS)
        for row in csv.DictReader(source):
            user_id, timestamp, event_type, seconds = (
                (row[column] or "").strip() for column in COLUMNS
            )
            if not all((user_id, timestamp, event_type, seconds)):
                continue
            if event_type not in EVENT_TYPES:
                continue

            duration = int(seconds)
            if duration <= 0:
                continue

            writer.writerow((user_id, normalize_timestamp(timestamp), event_type, duration))


if __name__ == "__main__":
    main()
