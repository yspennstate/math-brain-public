from difflib import unified_diff
from pathlib import Path


ROOT = Path("~")
OUT = ROOT / "brain_workers/w398/patches"
OUT.mkdir(exist_ok=True)


def emit(relative: str, output: str, old_namespace: str, extra=None) -> None:
    source = ROOT / relative
    before = source.read_text(encoding="utf-8")
    needle = f'"namespace": "{old_namespace}"'
    assert before.count(needle) > 0, (relative, "namespace absent")
    after = before.replace(needle, '"namespace": "probability.core"')
    if extra:
        for old, new in extra:
            assert after.count(old) == 1, (relative, old, after.count(old))
            after = after.replace(old, new)
    diff = "".join(unified_diff(
        before.splitlines(keepends=True),
        after.splitlines(keepends=True),
        fromfile=f"a/~/{relative}",
        tofile=f"b/~/{relative}",
    ))
    assert diff
    target = OUT / output
    target.write_text(diff, encoding="utf-8")
    print(target, "namespace_replacements", before.count(needle))


emit(
    "math-brain-inbox/w396/bundle_001.json",
    "01_w396_bundle_review_fixes.diff",
    "probability.selfavoiding",
    [
        ("E D_tau=D_0=r(A)-r(B)", "E D_tau=E D_0=r(A)-r(B)"),
        ("lambda times that probability is at most D_0", "lambda times that probability is at most E D_0"),
    ],
)
emit(
    "math-brain-inbox/w397/bundle_001.json",
    "02_w397_bundle_001_review_fixes.diff",
    "probability.saw",
    [
        ('"kind": "refutes",', '"kind": "proves",'),
        (
            "contradicting the target entry's identity-alone uniqueness/compactness implication.",
            "proving the target entry's statement that identity-alone uniqueness/compactness is a false inference.",
        ),
        (
            "The finite collar reduction belongs to the positive chordal route, whose ensemble distinction and unproved bridge are recorded in the target scope entry.",
            "The finite collar reduction applies to both ensembles; the target scope entry records that it does not transfer convergence between them.",
        ),
    ],
)
emit(
    "math-brain-inbox/w397/bundle_002.json",
    "03_w397_bundle_002_namespace.diff",
    "probability.saw",
)
