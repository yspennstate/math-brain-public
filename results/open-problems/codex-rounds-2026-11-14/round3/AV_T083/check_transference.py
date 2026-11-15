"""Exact arithmetic checks for PROOF.md; no external packages or network."""

from fractions import Fraction as F
from pathlib import Path
import os
import resource
import time

started = time.monotonic()
assert os.environ.get("OMP_NUM_THREADS") == "1"
e = F(1, 100)

# Independent polygon formulas, without the square change of variables.
# Vertices run counterclockwise.
vertices = [(-e, F(0)), (e, -2 * e / 3), (e, F(0)), (-e, 2 * e / 3)]
area_twice = first_y_times_6 = second_y_times_12 = F(0)
for (x, y), (u, v) in zip(vertices, vertices[1:] + vertices[:1]):
    cross = x * v - u * y
    area_twice += cross
    first_y_times_6 += (y + v) * cross
    second_y_times_12 += (y * y + y * v + v * v) * cross
area_polygon = area_twice / 2
first_polygon = first_y_times_6 / 6
second_polygon = second_y_times_12 / 12

# Independent direct integral in eta: width is 2e-3|eta|.
h = 2 * e / 3
area_slices = 2 * (2 * e * h - 3 * h * h / 2)
second_slices = 2 * (2 * e * h**3 / 3 - 3 * h**4 / 4)
assert area_polygon == area_slices == 4 * e * e / 3
assert first_polygon == 0
assert second_polygon == second_slices == 8 * e**4 / 81
assert second_polygon / area_polygon == 2 * e * e / 27
print(f"area = {area_polygon}; integral eta = {first_polygon}")
print(f"integral eta^2 = {second_polygon}; mean eta^2 = {second_polygon / area_polygon}")

# For a quadratic test kernel K(t)=t^2, Taylor remainder is exact.
# The constant 1/2 times mean eta^2 is attained, since K''=2.
for n in range(-5, 6):
    error_mean = (2 * n * first_polygon + second_polygon) / area_polygon
    assert error_mean == F(1, 2) * 2 * (2 * e * e / 27)
print("quadratic Taylor coefficient: exact equality for 11 integer centers")

# Compute product_{j=0}^3(s-jz), represented by coefficients of s^(4-i)z^i.
coefficients = [F(1)]
for j in range(4):
    out = [F(0)] * (len(coefficients) + 1)
    for i, coefficient in enumerate(coefficients):
        out[i] += coefficient
        out[i + 1] -= j * coefficient
    coefficients = out
assert coefficients == [1, -6, 11, -6, 0]
print(f"directional derivative coefficients = {coefficients}")

# Enumerate prefix choices, including empty and full blocks, and complex phases.
checks = 0
for length in range(1, 8):
    for prefix in range(length + 1):
        for phase in (1, -1, 1j, -1j):
            values = [phase if k < prefix else 0 for k in range(length)]
            variation = max(abs(v) for v in values)
            variation += sum(abs(b - a) for a, b in zip(values, values[1:]))
            assert variation <= 2  # After dividing by 4sqrt(w): <=1/(2sqrt(w)).
            sample = [complex(k * k, 2 * k - 1) for k in range(length + 1)]
            telescoped = sum(values[k] * (sample[k + 1] - sample[k]) for k in range(length))
            assert telescoped == phase * (sample[prefix] - sample[0])
            checks += 1
print(f"prefix variation and telescoping checks = {checks}")

# Source continuity and exact quotation audit, if VERIFY.md is present.
here = Path(__file__).resolve().parent
old = Path("~/codex_op_1114/briefs/AV_T083/sources")
names = {
    "candidate1-introduction.tex": "candidate1-introduction.tex",
    "candidate2-introduction.tex": "candidate2-01-introduction.tex",
    "candidate3-introduction.tex": "candidate3-introduction.tex",
    "candidate3-transfer.tex": "candidate3-transfer.tex",
    "candidate1-inputs.tex": "candidate1-inputs.tex",
    "candidate3-ergodic.tex": "candidate3-ergodic.tex",
}
for name, earlier in names.items():
    current = (here / "sources" / name).read_text()
    assert current.rstrip() == (old / earlier).read_text().rstrip(), name
print(f"current versus earlier source comparisons = {len(names)} unchanged")

verification_path = here / "VERIFY.md"
if verification_path.exists():
    verification = verification_path.read_text()
    for name in list(names)[:3]:
        source = (here / "sources" / name).read_text()
        begin = source.index(r"\begin{theorem}\label{thm:main}")
        end = source.index(r"\end{theorem}", begin) + len(r"\end{theorem}")
        assert source[begin:end] in verification, name
    print("exact main-theorem quotation checks = 3 passed")

print(f"per-scale normalized Taylor factor = {e * e / 27}")
print(f"summed normalized Taylor factor = {4 * e * e / 81}")
print(f"nice = {os.getpriority(os.PRIO_PROCESS, 0)}")
print(f"peak RSS (macOS bytes) = {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}")
print(f"elapsed seconds = {time.monotonic() - started:.3f}")
