# Reproducing the strong LTF and composition checks

The complete analytic proof is `strong_ltf_and_balanced_composition_proof.md`.
The original longer complementary-KL candidate is retained as a separate
independently audited route. The final proof uses the shorter universal
unate near-dictator lemma.

Run from this continuation directory in a repository checkout:

```bash
export PYTHONPATH=../2026-10-02-hamming-band
python verify_strong_ltf_composition.py
python independent_strong_ltf_check.py
```

The first checker requires NumPy. It checks every monotone truth table
through dimension five (7,778 functions across the dimensions), 3,488
near-dictator splits, 401 LTF cases, and 150 composition nodes with 90
formula roots through 13 leaves. Threshold scores use integer-valued
weights. Floating-point entropy is used only for sanity checks; the
analytic proof is the theorem certificate.

The independent checker uses integer Walsh transforms and exact Fraction
influence/variance recursions. It imports the previously archived monotone
truth-table generator from the Hamming-band continuation. It checks 2,977
exact recursions, 281 near-dictator splits and five disjoint balanced
compositions through 12 leaves. Entropy comparisons use floating point.

Root read both scripts in full and reran both successfully. The supporting
all-LTF proof and four full audits are in
[the largest-weight continuation](../2026-10-02-largest-weight/).
