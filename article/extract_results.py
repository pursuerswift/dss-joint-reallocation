"""Regenerate article-level source values from the three deposited study archives."""
import csv
import io
from collections import Counter
from pathlib import Path
from zipfile import ZipFile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULTS = "experiments/upgrade_v3/results/"
ARCHIVES = (
    "DSS_v3_reproduction.zip",
    "DSS_v3_update_20261119.zip",
    "DSS_v3_frontiers_20261119.zip",
)

def read_rows(path):
    member = RESULTS + path
    for name in reversed(ARCHIVES):
        with ZipFile(ROOT / name) as archive:
            if member in archive.namelist():
                with archive.open(member) as source:
                    return list(csv.DictReader(io.TextIOWrapper(source, encoding="utf-8-sig")))
    raise FileNotFoundError(member)

def write_rows(name, rows):
    with (HERE / name).open("w", newline="", encoding="utf-8") as output:
        writer = csv.DictWriter(output, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

def figure_values():
    summary = read_rows("major_revision_20261118/revision/summary.csv")
    records = [row for row in summary if row["block"] == "headline"
               and row["family"] == "compatibility" and float(row["cap_share"]) == 1]
    methods = ("score_original", "score_stopping", "greedy_rematch", "type_flow")
    values = []
    for position, method in enumerate(methods, 1):
        row, = [r for r in records if r["method"] == method]
        values.append({"position": position, "method": method,
                       **{k: row[k] for k in ("gross", "cost", "net")}})
    return values

def historical_values():
    folder = "expanded_v3/empirical/"
    def candidates(filename):
        return {(r["dataset"], r["seed"]): r for r in read_rows(folder + filename)
                if r["scenario"] == "pair_low" and r["key"] == "cost_flow:cap1"}
    test = candidates("test_candidates.csv")
    adoption = candidates("gate_candidates.csv")
    if set(test) != set(adoption) or len(test) != 9:
        raise ValueError("Expected nine aligned test and adoption partitions.")
    rows = []
    for cohort, seed in sorted(test):
        t = test[cohort, seed]
        rows.append({"cohort": cohort, "split_seed": seed, "test_exchanges": t["exchanges"],
                     "test_net_per_1000": 1000 * float(t["net"]),
                     "test_lower_per_1000": 1000 * float(t["lower"]),
                     "test_upper_per_1000": 1000 * float(t["upper"]),
                     "adoption_lcb_per_1000": 1000 * float(adoption[cohort, seed]["lcb_max_t"])})
    frozen = read_rows(folder + "frozen_decision_test.csv")
    counts = Counter((r["rule"], r["key"]) for r in frozen)
    if counts != {(rule, "retain"): 324 for rule in ("max_t", "bonferroni", "hoeffding")}:
        raise ValueError("Unexpected frozen-decision totals.")
    return rows

if __name__ == "__main__":
    write_rows("figure_3.csv", figure_values())
    write_rows("historical_candidates.csv", historical_values())
    print("Wrote the four plotted method means and nine historical candidates. Verified 972 retention decisions.")

