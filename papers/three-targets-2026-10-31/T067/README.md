# A three-state posterior cone and reconstruction on finite-mean Galton-Watson trees

Yitzchak Shmalo, 31 October 2026

The complete manuscript is [T067_Finite_Mean_Reconstruction.pdf](T067_Finite_Mean_Reconstruction.pdf); editable LaTeX source is in [paper/](paper/). The main contribution is the three-state posterior cone and its threshold theorem for arbitrary finite-mean offspring, including critical equality. The paper states the implication for Formentin-Kulske Conjecture 2.13 explicitly. The four-state result is attributed as a consequence of the earlier four-state cone.

## Contents

- `paper/`: complete LaTeX source for the manuscript.
- `analytic/q3_exact_pair_simple.cpp`: the original three-state exact certificate encoder.
- `computation/q3_independent_coefficients.cpp`: the second original exact coefficient implementation.
- `computation/verify_q3_python.py`: a separate dependency-free Python implementation of both displayed certificate polynomials.
- `computation/q3_python_result.json`: fresh exact verification result for the Python implementation.
- `computation/q3_independent_coefficients_A.tsv` and `_B.tsv`: all 80,532 coefficient positions, freshly regenerated with the separate Python implementation. Their byte hashes match the original C++ tables.
- `computation/published_q4/`: the prior four-state verifier, its license, and retained complete-traversal records.
- `SUPPLEMENT.md`: compilation and reproduction instructions.
- `THIRD_PARTY_NOTICES.md`: attribution and licensing for prior verification code.
- `../MANIFEST.json`: current byte lengths and SHA-256 checksums.

All polynomial sign decisions use exact integers or rational numbers. The verification is computational and internal mathematical checking, not a proof-assistant formalization or external peer review. This package is an updated version of the October 2026 T067 work, not a separate additional problem count.

This consolidation clarifies iid child ordering in the pruning proof. Use the top-level MANIFEST.json for the delivered file hashes; the contribution history is in [PROVENANCE.md](../PROVENANCE.md).
