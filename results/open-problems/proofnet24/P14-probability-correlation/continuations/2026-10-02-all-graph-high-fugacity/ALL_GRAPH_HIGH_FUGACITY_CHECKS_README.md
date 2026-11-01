# Reproducing the all-orders induction checks

The analytic proof is `ALL_GRAPH_HIGH_FUGACITY_PROOF.md`. The draft and
earlier closure checkpoint remain preserved; their historical candidate/gap
labels are superseded only by the explicit final proof and transfer audits.

Run from this continuation directory in a repository checkout:

```bash
export PYTHONPATH=../2026-10-02-general-H2:../2026-10-02-general-H3:../2026-10-02-forest-families
python response_induction_local_audit.py
python response_iteration_research_heat.py
```

The first checker implements Fraction exterior algebra, determinant Gaussian
moments, and marked rank-one covariance derivatives. It computes the local
scores directly, without using the conjectured response formula. Five
nested two-port examples have first nonconstant orders 1,2,2,3,3, with exact
eigenvalues 1/8,1/128,1/512,1/2048,1/51200. Each next quartic agrees with
the independent Ward particular solution.

The second checker independently computes the complete forest Rayleigh
polynomial using the archived frontier-connectivity dynamic program, then
compares it with the iterated electrical trace/wedge predictions. It checks
K4 chains through first positive H4,H5,H6 and a 14-vertex asymmetric
three-port H4 case with positive off-diagonal entries in a response matrix.
Both scripts were rerun successfully by root. Their outputs are exact
rationals/integers, although some early status strings record the exploratory
state in which the scripts were first written.

The full analytic induction is required for graphs and delayed orders beyond
these examples. No finite suite is substituted for the transfer lemma,
contrast-range closure, valid grounding, or finite-growth proof.

The preceding complete proofs are available at
[general H2](../2026-10-02-general-H2/GENERAL_H2_SOS_PROOF.md) and
[general H3](../2026-10-02-general-H3/GENERAL_H3_SOS_PROOF.md).
