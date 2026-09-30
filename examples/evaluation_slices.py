"""Invented evaluation fixture, newly authored for this portfolio.

No company data, original implementation, fitted model, or third-party packages.
"""

from math import isclose, sqrt
from statistics import mean


def metrics(rows):
    """Return sample count, MAE, RMSE, and signed prediction bias."""
    if not rows:
        raise ValueError("At least one (reference, prediction) pair is required")
    errors = [prediction - reference for reference, prediction in rows]
    return len(rows), mean(abs(e) for e in errors), sqrt(mean(e * e for e in errors)), mean(errors)


def main():
    # Deliberately imbalanced, wholly invented retrospective observations.
    early = [(10.0 + i / 10.0, 10.5 + i / 10.0) for i in range(90)]
    near_end = [(i / 3.0, 9.5) for i in range(10)]
    rows = early + near_end
    slices = {
        "overall": rows,
        "reference > 3": [row for row in rows if row[0] > 3.0],
        "reference <= 3": [row for row in rows if row[0] <= 3.0],
    }
    values = {name: metrics(sample) for name, sample in slices.items()}
    weighted_mae = sum(values[name][0] * values[name][1] for name in ("reference > 3", "reference <= 3")) / len(rows)
    assert isclose(values["overall"][1], weighted_mae)
    assert values["reference <= 3"][1] > values["overall"][1]
    assert values["reference <= 3"][3] > 0

    print("SYNTHETIC ONLY: invented values; no company data or model results.")
    print("slice             n   MAE    RMSE   bias")
    for name, (n, mae, rmse, bias) in values.items():
        print(f"{name:15s} {n:3d}  {mae:5.2f}  {rmse:5.2f}  {bias:5.2f}")
    print("Weighted-MAE decomposition: verified.")


if __name__ == "__main__":
    main()
