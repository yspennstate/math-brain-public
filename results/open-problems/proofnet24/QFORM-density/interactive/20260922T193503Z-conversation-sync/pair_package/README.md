# QFORM: arbitrary-rank pair proof and corrected proof routes

The unrestricted three-large-eigenvalue conjecture remains unproved by this work.

Start with FULL_MATRIX_PAIR_EXTENSION.md. It supplies a complete supporting argument for arbitrary rank under a quantitative indefinite ORIGINAL-coordinate pair condition. All remaining eigenvalues and affine terms are unrestricted. Independent end-to-end review is pending. PAIR_LOG_THEOREM.md gives the underlying logarithmic envelope and a sharper exact-rank-three branch.

CORRECTIONS.md gives two exact counterexamples to proposed intermediate claims. Neither is a counterexample to the original independent-input conjecture: the first uses dependent joint inputs, and the second refutes a conditional-density moment used in a proof route rather than the quadratic output-density conclusion.

## Canonical archive
Repository: yspennstate/math-open-problems
Directory: proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/
Full-matrix proof commit: 742ac943440e41925fe09db9a8c02a96cbd83dbc
Pair-envelope proof commit: f7f0fedb2d93b46824f96cac1164af6f8a55626f
Corrections commit: f305dcc8ae0f602f2b21ab32cf4d8ddcdcb56b92
Final bundle commit: 91463281b113b3dbb9aa66dcbaa14d2d1645e5ff
Shared proof-first worker request update: math-research-brain commit 944d5664bcfe9e8fe7e49ec647c578a519f55eee

All three mathematical report Git blob hashes were read back and match these local report bytes. The committed result JSON files contain the same executed data with different whitespace formatting.

## Reproduce finite checks
Requires Python 3.10+, numpy, scipy, sympy. From this directory run:

    python checks.py
    python full_matrix_checks.py

These verify scalar algebra, the exact conditional-cube formula against quadrature, and finite matrix examples. The proofs are the analytic arguments in the Markdown files, not numerical experiments. The checks do not certify the unrestricted conjecture, establish literature-wide novelty, or constitute independent review.

All research remains on the original arbitrary-dimension, arbitrary-sign, arbitrary-cap-one-product-law problem. No simulation-based completion claim, independent-review approval, or native learned-memory-ingestion claim is made.
