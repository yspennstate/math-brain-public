"""Summarize saved referee computations and independently check quoted evidence counts."""
import csv
import json
from pathlib import Path
from decimal import Decimal, getcontext

getcontext().prec = 50
root = Path(__file__).resolve().parent


def read(sizes, tag=""):
    rows = []
    for n in sizes:
        with (root/f"referee_spectra{tag}_n{n}.csv").open() as handle:
            for row in csv.DictReader(handle):
                rows.append({key: int(value) if key in ("n", "k") else Decimal(value)
                             for key, value in row.items()})
    return rows


def case(row):
    return {key: str(value) for key, value in row.items()}


def aggregate(rows):
    nonanti = [r for r in rows if 2*r["k"] != r["n"]]
    anti = [r for r in rows if 2*r["k"] == r["n"]]
    return dict(cases=len(rows), antipodal_cases=len(anti), nonantipodal_cases=len(nonanti),
                max_antipodal_error=str(max((r["antipodal_residual"] for r in anti), default=Decimal(0))),
                max_rw_formula_error=str(max(r["rw_formula_residual"] for r in rows)),
                max_mh_formula_error=str(max(r["mh_formula_residual"] for r in rows)),
                min_nonantipodal_cycle_margin=case(min(nonanti, key=lambda r:r["a"]-r["gamma"])),
                min_mh_cycle_margin=case(min(rows, key=lambda r:r["a"]-r["mh_gap"])),
                worst_rw_relative_slack=case(max(rows, key=lambda r:r["rw_relative_slack"])),
                worst_mh_relative_slack=case(max(rows, key=lambda r:r["mh_relative_slack"])),
                min_nonantipodal_rw_slack=str(min(r["rw_slack"] for r in nonanti)),
                rw_bound_violations=sum(r["rw_slack"] < Decimal("-1e-45") for r in rows),
                mh_bound_violations=sum(r["mh_slack"] < Decimal("-1e-45") for r in rows),
                nonantipodal_strict_failures=sum(r["gamma"] >= r["a"] for r in nonanti),
                mh_strict_failures=sum(r["mh_gap"] >= r["a"] for r in rows),
                per_n=[dict(n=n, cases=sum(r["n"]==n for r in rows),
                            max_rw_relative_slack=str(max(r["rw_relative_slack"] for r in rows if r["n"]==n)),
                            max_mh_relative_slack=str(max(r["mh_relative_slack"] for r in rows if r["n"]==n)))
                       for n in sorted({r["n"] for r in rows})])


even = read((4, 6, 8, 10, 12, 20, 30))
odd = read((5, 7, 9, 11, 13, 21, 31))
extreme = read((4, 6, 8, 10, 12, 20, 30), "_extreme")
data = dict(even=aggregate(even), odd=aggregate(odd), extreme=aggregate(extreme))
data["illustrations"] = [case(r) for r in even if
    (r["n"], r["k"], r["w"]) in {
        (4, 2, Decimal("1")), (6, 2, Decimal("1")), (6, 3, Decimal("1")),
        (8, 2, Decimal("100")), (8, 4, Decimal("100")),
        (10, 4, Decimal("100")), (30, 2, Decimal("100")),
        (30, 14, Decimal("100")), (30, 15, Decimal("100"))}]
data["author_evidence"] = {}
for name in ("exact_matrix", "exact_paths", "exploration", "metropolis", "controls"):
    content = json.loads((root/"evidence"/f"{name}.json").read_text())
    data["author_evidence"][name] = {k:v for k,v in content.items() if k != "records"}
    records = content.get("records", [])
    if records:
        data["author_evidence"][name]["counted_records"] = len(records)
        data["author_evidence"][name]["counted_antipodal"] = sum(r["n"] == 2*r["k"] for r in records)
        data["author_evidence"][name]["counted_nonantipodal"] = sum(r["n"] != 2*r["k"] for r in records)
out = root/"referee_summary.json"
out.write_text(json.dumps(data, indent=2)+"\n")
print(json.dumps(data, indent=2))
