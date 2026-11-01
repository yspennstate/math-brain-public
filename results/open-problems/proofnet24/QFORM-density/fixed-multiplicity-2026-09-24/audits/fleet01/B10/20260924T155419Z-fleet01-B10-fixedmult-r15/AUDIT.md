# B10 r15 full-source audit

Objective QFORM-FIXED-MULTIPLICITY-AUDIT-20260924.

Current source: eeb752c8943536541b34b42b8bf48e924f4d3d2f, paper.tex blob 19fb119877426b640b2c0dae19ec2f78a399fe11, 955 lines. Preserved baseline: 7c0d6e60946b19423e6400a12d34b473cf0591e2, manuscript blob 183ccd294763214e6a707e8d4749ff9a8cf7006d, 790 lines. All requested package support files were read.

Verdict: PASS AFTER ONE LOCAL REPAIR; no fatal theorem defect found.

Current lines 598-600 have a local proof gap. The positive hyperbolic tail selects i from u, then the negative tail switches to w but still cites that i. Equal norms of u,w do not make the same coordinate large. Repair: choose a separate i_minus on the negative tail with abs(w_i_minus)>=abs(w)/sqrt(2), and use its coordinate density. Its cutoff has exactly the same bound, so every displayed constant is unchanged. Baseline lines 472-474 have the same inherited issue and repair.

All other current ranges PASS: 1-213 analytic/spectral preliminaries; 214-396 Brascamp-Lieb, projections, scalar Fourier powers, decoupling and determinant; 397-527 grouped mollified-L2 and row promotion; 528-597 scalar/definite profiles and positive hyperbolic tail; 601-776 concentration, sampling/completion, rank and no-pivot volume; 777-905 full half-potentials, pivot assembly and scaling; 906-955 overlap-tail theorem. No other mathematical source range remains UNCHECKED in this review.

Exact current constants rechecked: p+d^2=13/1600<1/121; interpolation dominance margins 1131/2200 and 51/2200; C3<15; no-pivot density<375; all printed theorem branches<400.

Checker coverage: verify_new.py/checks_new.json are finite diagnostics only. They do not computationally certify Fourier/Riesz, heat-flow limits, grouped mollified-L2, entropy, hyperbolic coarea, pair half-potential or conditional Tonelli. Those are proof-only, not mathematical gaps.

Adversarial exact diagnostics retained: an r=2 no-pivot completion attains rank R=6 and restricted rank 2 simultaneously; a singular r=2 seed can have a nonsingular one-step extension. These rule out two tempting checker/rank shortcuts but are not theorem proofs.

Global continuity is not claimed. Full three-eigenvalue QFORM remains open.
