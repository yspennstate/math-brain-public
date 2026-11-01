# C0017 referee packet (w419)

2026-10-10 preliminary source-scope verdicts:

- **KEEP, w417-target-000, metadata scope only.** Reproduction: ranking CSV line 538 is exactly `5,C0017,Conformal invariance of critical bond percolation on the square lattice,attempted_un,conformal invariance on Z^2`. Its claim makes no current-open or proof assertion. Remaining gap: primary formulation and later proof claims.
- **KEEP, w418-C0017-S1.1, abstract-scope only.** Reproduction: arXiv:0909.4499 is cited by w418 as triangular-site. The local C0017 intake line 17 specifies independent square-bond p=1/2. Model hypotheses differ, so a theorem restricted to triangular-site cannot be directly instantiated at C0017. Remaining gap: full theorem review and a transfer theorem; no transfer is proved here.

These KEEP verdicts do not solve C0017. Recheck any subsequent proof claims from w417/w418 step by step.

## Mathematical verdicts, 2026-10-10

- **KEEP w417-L1, finite product-law weighted comparison.** Independent telescoping derivation is in ATTEMPT.md. Reproduction: `mu_i=Bernoulli(1/4)`, `nu_i=Bernoulli(1/2)`, three-cell AND gives actual difference = weighted bound = 0.109375; unweighted bound 0.75. W418 independently found the same lemma sound. Remaining gap: no faithful common skeleton or vanishing total error for C0017.
- **KEEP w417-L2, exact finite gadget obstruction.** Reproduced by the minimal-tree leaf/path argument in ATTEMPT.md. Its 2^(-m) lower bound is for m fair independent edges when all terminals lie in one deterministic graph component. Remaining gap: growing approximate gadgets and dependent substitutions are not excluded.
- **KEEP w417-L3 and C1, scoped counterexamples.** Reproduced star probability 0.6464466094 versus 0.5, and dependent two-bit event difference 0.5 despite zero marginal TV. These refute pair-matching and marginal-only inference, respectively; they do not refute C0017.
- **KEEP w418 weak-CR obstruction, abstract scope.** `python -X utf8 verify_weak_cr.py` reported residual 0 and average error 0 for n=1,2,4,8, with contour integral i. Source alignment checked against Duminil-Copin, arXiv:1208.3787, Definition 3 and Proposition 4. W418's corrected conditional Morera step uses **i delta** times the WCR sum. Remaining gap: actual q=1 observable may possess extra coherence not modeled by this example.
- **KEEP w418 endpoint-only trap.** Independent majority-event arithmetic at epsilon=0.01 gives false endpoint bound 0.058212 and actual difference 0.999404; true middle hybrid sensitivity is (1-epsilon)^2+epsilon^2. Remaining gap: bound all actual hybrid sensitivities for a percolation comparison.
- **KEEP w417 source correction of C0017-A001 spin, subject to source convention.** Smirnov primary source and Duminil-Copin Definition 3 give sigma(1)=1/3. Reproduced algebra in CLAIMS.jsonl row C0017-source-002. The historical attempt's 2/3 is q=3 under this convention. The draft correction is in w417/CORRECTED_ATTEMPT_DRAFT.json; no live correction applied here.

The single hardest unresolved claim is the vanishing model-comparison error G1 under hybrid laws, or an independent q=1 observable coherence theorem. None of the KEEP verdicts proves the parent problem. No formal proof receipt is asserted; no served-model identity was available to verify.
