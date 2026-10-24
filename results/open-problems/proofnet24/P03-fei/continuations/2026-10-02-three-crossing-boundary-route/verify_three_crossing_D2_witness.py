"""Independent stdlib-only exact reconstruction of the D3=2 witness."""
from fractions import Fraction
import json
from pathlib import Path

weights = (33, 34, 36, 40, 48)
crossings = (-34, 0, 34)
n, size = len(weights), 1 << len(weights)
scores = [sum(weight * (1 if vertex & (1 << j) else -1)
              for j, weight in enumerate(weights)) for vertex in range(size)]
assert len(set(scores)) == size
assert all(crossing not in scores for crossing in crossings)
regions = [sum(score > crossing for crossing in crossings) for score in scores]
sizes = [regions.count(region) for region in range(4)]
assert sizes == [12, 4, 4, 12]
labels = [1 if region % 2 == 0 else -1 for region in regions]


def influence(values):
    counts = [sum(values[v] != values[v ^ (1 << j)] for v in range(size))
              for j in range(n)]
    return Fraction(sum(counts), size), counts


main_i, main_counts = influence(labels)
component_i = []
component_counts = []
for region in range(4):
    value, counts = influence([1 if found == region else -1 for found in regions])
    component_i.append(value)
    component_counts.append(counts)
positive = component_i[0] + component_i[2]
negative = component_i[1] + component_i[3]
assert main_i == Fraction(11, 8)
assert positive == negative == Fraction(23, 8)
assert min(positive, negative) / main_i == Fraction(23, 11)
report = dict(status="PASS", weights=list(weights), crossings=list(crossings),
              score_region_sizes=sizes, physical_I=str(main_i),
              physical_component_I=list(map(str, component_i)),
              physical_B_positive=str(positive), physical_B_negative=str(negative),
              ratio=str(min(positive, negative) / main_i),
              main_directed_flip_counts=main_counts,
              component_directed_flip_counts=component_counts,
              scores=scores, region_indices=regions,
              scope="Exact finite counterexample to D3=2; not an unbounded-ratio family",
              dependencies="Python stdlib only; no helper imports")
Path(__file__).with_name("three_crossing_D2_counterexample.json").write_text(
    json.dumps(report, indent=2) + "\n")
print(json.dumps({key: value for key, value in report.items()
                  if key not in {"scores", "region_indices"}}, indent=2))
