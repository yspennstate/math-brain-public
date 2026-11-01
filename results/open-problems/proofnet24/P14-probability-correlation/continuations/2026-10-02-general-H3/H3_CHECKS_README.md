# Reproducing the H3 and response-space checks

The complete analytic result is `GENERAL_H3_SOS_PROOF.md`. The draft and
intermediate outputs preserve their status at the time of calculation;
labels such as "unproved candidate" in early JSON files are historical,
not a replacement for the final proof and independent analytic audits.

The scripts use exact Fraction arithmetic, integer forest sums, or a
connectivity frontier dynamic program. Run from this continuation directory
in a checkout of the repository. The two preceding continuation directories
supply already archived electrical and forest-enumeration helper modules:

```bash
export PYTHONPATH=../2026-10-02-general-H2:../2026-10-02-forest-families
python H3_response_wedge_heat.py
python H3_positive_offdiag_audit_heat.py
g++ -std=c++17 -O2 forest_subset_integer_audit.cpp -o forest_subset_integer_audit
python H3_non_M_matrix_audit.py
python response_positive_offdiagonal_root_audit.py
python response_space_lemma_counterexample_audit.py
python local_score_grassmann_heat.py
```

The C++ executable is generated locally and is not an artifact to commit.
The calling Python script checks its conservative signed-128-bit bound
before execution; subsequent polynomial products use Python integers.

The separate three-port response counterexample was independently audited
by root using a freshly assembled Dirichlet matrix and rational linear
solver. It rules out nonnegative ordinary-edge decompositions of the
response Gram, not its positive semidefiniteness. The exact symbolic
two-port score checker rules out the proposed all-orders confinement to
linear contrast modes. Both failed routes are important limits on extending
the proved H3 theorem.

The companion H2 proof is in
[`../2026-10-02-general-H2/GENERAL_H2_SOS_PROOF.md`](../2026-10-02-general-H2/GENERAL_H2_SOS_PROOF.md).
The new H3 equality geometry does not provide an H4 recursion. Arbitrarily
long vanishing-coefficient chains remain a required scope check.
