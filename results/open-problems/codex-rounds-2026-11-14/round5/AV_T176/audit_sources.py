"""Recheck the saved source graph, quotations and rational constants."""

from fractions import Fraction
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent
LEAN = ROOT / "sources" / "lean"
PREFIX = "OAI.Probability.ThorpShuffle."
sources = {PREFIX + p.stem: p.read_text() for p in sorted(LEAN.glob("*.lean"))}
imports = {
    name: re.findall(r"^import (\S+)", source, re.MULTILINE)
    for name, source in sources.items()
}

visited = set()
active = []
external = set()


def visit(name):
    if name in active:
        raise AssertionError(f"Import cycle: {active + [name]}")
    if name in visited:
        return
    assert name in sources, f"Missing source {name}"
    visited.add(name)
    active.append(name)
    for dependency in imports[name]:
        if dependency.startswith("OAI."):
            visit(dependency)
        else:
            external.add(dependency)
    active.pop()


visit(PREFIX + "Main")
assert len(visited) == 51
assert len(sources) == 55
assert external == {"Mathlib"}
assert {x.removeprefix(PREFIX) for x in sources.keys() - visited} == {
    "FirstMain", "FirstFourier", "FirstMoment", "ExceptionalShapes"
}
holes = [
    (name, line_no, line)
    for name, source in sources.items()
    for line_no, line in enumerate(source.splitlines(), 1)
    if re.search(r"\b(sorry|admit|axiom|unsafe)\b", line)
]
assert not holes, holes

pattern = re.compile(
    r"\\begin\{(?:theorem|corollary)\}[\s\S]*?"
    r"\\end\{(?:theorem|corollary)\}"
)
verify = (ROOT / "VERIFY.md").read_text()
quotes = []
for name, expected in [("optimal", 1), ("compatibility", 3), ("routing", 1)]:
    source = (ROOT / "sources" / f"{name}.tex").read_text()
    environments = pattern.findall(source)
    assert len(environments) == expected
    for environment in environments:
        assert verify.count(environment) == 1, name
    quotes.extend(environments)
for name in ["optimal", "compatibility-header", "routing-header"]:
    header = (ROOT / "sources" / f"{name}.tex").read_text()
    assert r"\author{OpenAI}" in header
    assert r"\date{September 26, 2026}" in header
for name in ["PROOF.md", "VERIFY.md", "REPORT.md", "LOG.md"]:
    source = (ROOT / name).read_text()
    assert not any(ord(c) < 32 and c not in "\n\t" for c in source), name

single = Fraction(5, 8) * (1 + Fraction(4, 5) ** 4)
double = Fraction(5, 4) ** 2 * Fraction(4, 5) ** 4
assert single == Fraction(881, 1000) <= Fraction(9, 10)
assert double == Fraction(16, 25) <= Fraction(9, 10) ** 2
assert 7**2 * 8 // 4 == 98
assert 98 * 32 == 3136
assert 8 * 4 * 3 == 96
assert 8 * 200 == 1600
assert 2 - 16 * Fraction(1, 4) == -2
assert 2 - 16 * Fraction(5, 16) == -3
assert (ROOT / "REPORT.md").read_text().startswith("VERDICT: PARTIAL ")

print(json.dumps({
    "solution_modules": len(sources),
    "main_closure": len(visited),
    "outside_imports": sorted(external),
    "literal_hole_tokens": len(holes),
    "exact_theorem_quotes": len(quotes),
    "single_pair_factor": str(single),
    "double_pair_factor": str(double),
    "marginal_squared_prefactor": 98,
    "marginal_rate_constant": 3136,
    "full_rate_base": 96,
    "physical_steps_per_dimension": 1600,
    "status": "passed; source audit only, no Lean build",
}, indent=2))
