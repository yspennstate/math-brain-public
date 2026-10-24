# account01/B03 r15 — current fixed-multiplicity audit

Objective: QFORM-FIXED-MULTIPLICITY-AUDIT-20260924.
Run: 20260924T154801Z-account01-B03-fixedmult-audit-r15.

Fresh AGENTS.md and CURRENT_OBJECTIVE.md were read before work.

Current standalone source pin:
- repo yspennstate/math-open-problems
- commit eeb752c8943536541b34b42b8bf48e924f4d3d2f
- paper proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex
- blob 19fb119877426b640b2c0dae19ec2f78a399fe11
- SHA256 bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3
- 955 lines.

## Nine/400 source verdict

PASS for the mathematical theorem s_9(A)>=s => density <=400 K^2/s under arbitrary independent coordinate densities <=K, arbitrary real symmetric A, and arbitrary affine terms.

Source ledger:
1-164 PASS: quantifiers, scaling, Fourier inversion/regularization, negative-half-moment identity.
165-297 PASS: singular values, Schur count, diagonal dominance, geometric BL, product projections, scalar Fourier powers.
298-396 PASS: literal-bank independent-copy decoupling, second/fourth powers, regularized determinant exponent -1/8.
397-477 PASS: grouped mollified-L2 proof. The phase-weighted image is L2 before the limiting step; Jensen is applied to mollified norms; only the literal J bank is copied; the pure J phase is removed after integrating original independent I-coordinates; weighted Holder is valid for the finite kernel measure; the joint row-Gram determinant is S^2 det(C_T C_T^T); all scalar powers are >=2.
478-527 PASS: physical-row promotion and terminal hub cases; C3<15 and C2<14.
528-662 PASS: scalar profile, definite/hyperbolic pairs, quarter-power concentration.
663-766 PASS: volume sampling, nonsymmetric completion, global rank <=3r versus restricted rank <=r, no-pivot entry bounds and r=1,2 margins.
767-860 PASS: full pair half-potential with D^(-1/4) scaling, s5 half-potential, main theorem and K^2/s scaling.
861-955 PASS: spectral-tail/overlap inequality.

Package README, NINE_400_AND_OVERLAP, AUDIT_NEW, MANIFEST, proof_map, verify_new and checks_new were read on current master. Textual scope PASS. Fresh execution of verify_new and PDF rebuild/render are UNCHECKED in this run. Bibliographic priority claims are UNCHECKED and nonessential because specialized inputs are reproved. FALSE: none found.

## Lower multiplicity

I independently reconstructed QFORM-FIXED-MULTIPLICITY-8-v1 from the B04 terminal dichotomy, B17 robust-anchor extraction, B20 one-high closure, B19 incident-volume receiver, and B01 two-high exclusion.

Normalized branch bounds:
- scalar pivot <1150;
- definite pair <40;
- indefinite pair <199;
- no-pivot large V3 <2400, with C0 density;
- no-pivot robust terminal state <23.48, with C0 density.

In the terminal state a literal pair H has g=det(CC^T)>8/25. For Q_C=C^T(CC^T)^(-1)C, let J={i:q_i>2/3}; rank Q_C=2 gives |J|<=2. If |J|<=1 and W_dis<=g/48, the anchored-minor correction has Frobenius error <=1/4, residual global rank <=5 and low-coordinate rank <=2. Perturbing s_8>=1 forces three low diagonal coefficients of modulus >=3/4. The associated 3x3 residual block is strictly diagonally dominant, contradicting rank <=2. Therefore W_dis>g/48 and the product-safe q=3 receiver closes the branch.

If J={i,j}, determinantal weights give det(C_ij)^2>g/3>8/75. The no-pivot physical entry cap gives det(C_ij)^2<10201/25000000, contradiction. Hence the two-high endpoint is empty.

Verdict: PASS for the candidate s_8(A)>=s => ||p_Q||_infinity<2400 K^2/s.

A separate complete PASS review exists at audits/account03/B08/20260924T151825Z-account03-B08-s8-full-review-r59/AUDIT.md. This B03 file is a second independent complete reconstruction; it does not assign any owner/release/formal-verification flag.

Global continuity is not proved by the pivot branches. The unrestricted three-eigenvalue problem remains OPEN. No closed s7 theorem was found in the current repository; s7 currently has structural overlap reductions only.
