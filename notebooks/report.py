import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import csv

    import marimo as mo
    from matplotlib.figure import Figure

    return Figure, csv, mo


@app.cell
def _(csv, mo):
    _path = mo.notebook_dir().parent / "data" / "features" / "events.csv"
    with _path.open(encoding="utf-8", newline="") as _source:
        durations = [float(row["duration_minutes"]) for row in csv.DictReader(_source)]
    return (durations,)


@app.cell
def _(Figure, durations):
    _figure = Figure(figsize=(7, 4), layout="constrained")
    _axes = _figure.subplots()
    _axes.hist(durations, bins=30, color="#267985", edgecolor="white")
    _axes.set(
        title="Distribution of event durations",
        xlabel="Duration (minutes)",
        ylabel="Number of events",
    )
    _figure
    return


if __name__ == "__main__":
    app.run()
