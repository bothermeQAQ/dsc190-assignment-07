# DSC 190 Assignment 07 — Reproducible Data Pipelines

Run these commands from the repository root:

```sh
uv sync
uv run dvc repro
uv run marimo edit notebooks/report.py
```

DVC runs `clean`, `transform`, and `features` in dependency order. The notebook
reads `data/features/events.csv` and plots the distribution of event durations
in minutes.

The source CSV comes from the [course assignment](https://github.com/dsc-courses/dsc190-tools-2026-fa/tree/main/assignments/07-reproducibility).
The cleaning stage accepts the five event types in the dataset: `click`,
`login`, `purchase`, `scroll`, and `view`. It preserves the wall-clock time
of each timestamp at second precision.
