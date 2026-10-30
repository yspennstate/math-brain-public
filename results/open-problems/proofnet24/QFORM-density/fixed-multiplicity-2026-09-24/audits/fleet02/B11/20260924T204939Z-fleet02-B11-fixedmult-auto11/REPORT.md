# fleet02/B11 — fixed-multiplicity audit

Run: 20260924T204939Z-fleet02-B11-fixedmult-auto11
Objective: QFORM-FIXED-MULTIPLICITY-AUDIT-20260924

## Source pins

Preserved baseline: commit 7c0d6e60946b19423e6400a12d34b473cf0591e2, manuscript.tex blob 183ccd294763214e6a707e8d4749ff9a8cf7006d, package-recorded SHA-256 9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69, 790 lines.

Latest standalone nine-value source: commit eeb752c8943536541b34b42b8bf48e924f4d3d2f, paper.tex blob 19fb119877426b640b2c0dae19ec2f78a399fe11, package-recorded SHA-256 bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3, 955 lines.

Separately written nine-value source: paper.tex blob 823201f05363fcc60c38cce0feb5abb636f081d7, manifest SHA-256 ea56bc35cff9815db71a9f5a620e0160e3a39cf53ff60c789707294d53240eba.

## Baseline line ledger

- 1--436: PASS. Definitions, theorem quantifiers, normalization/scaling, Fourier inversion, Riesz representation, rank perturbation, Schur statement, diagonal dominance, Brascamp--Lieb, product projections, scalar Fourier powers, decoupling, determinant receiver, scalar and definite-pair profiles.
- 437--471: PASS. Hyperbolic parametrization, Jacobian, positive-tail estimate.
- 472--475: GAP_REPAIRABLE_LOCAL. The negative tail says to use the negative exponential vector but the displayed cutoff is still justified from the coordinate chosen for the positive exponential vector. The same coordinate need not be large for both.
- 476--790: PASS after the local repair. Quarter-power concentration, interpolation/completion, global and restricted ranks, spectral-to-volume conversion, random cuts, pivot half-potentials, final theorem assembly, K^2/s scaling and scope.
- FALSE: none found.
- UNCHECKED in this invocation: fresh execution of verify.py, raw-byte independent SHA-256 recomputation, PDF rebuild/render, exhaustive novelty search.

The baseline package support files were all read. verify.py source-binds its finite suite to the baseline SHA; checks.json records PASS with 534 exact interpolation seeds, 18 volume-sampling cases, 9 strict cases, exact diagonal-dominance slack 297/2800, plus 240 Schur and 30 graph-weight diagnostics.

## Latest nine/400 line ledger

- 1--562: PASS. Full quantifiers and scaling; Fourier/Riesz/rank/Schur foundations; BL/projections; determinant receiver; grouped mollified-L2 compiler; determinant-weighted Holder/entropy; literal-row promotion; E3 density and E2 half-potential receivers; scalar/definite pair.
- 563--597: PASS. Hyperbolic parametrization, Jacobian and positive tail.
- 598--600: GAP_REPAIRABLE_LOCAL. Same negative-tail coordinate-selection omission.
- 601--955: PASS after the repair. Concentration, retuned interpolation, full pair half-potential, five-direction half-potential, nine/400 case assembly, spectral-tail/overlap theorem and limitations.
- FALSE: none found.
- Packaging GAP: verify_new.py imports hashlib but does not hash/read paper.tex, so its finite PASS is not source-bound to the manifest source. This is not a mathematical proof defect.
- UNCHECKED here: fresh execution of verify_new.py, independent raw SHA, PDF rebuild.

The separately written nine-value paper has the same local omission in Lemma 5.3: after choosing i large for u, the negative-tail sentence switches to u' but retains the cutoff justification from |u_i|. Its finite Lean/numerical evidence does not formalize the two-dimensional change-of-variables proof, exactly as its AUDIT.md states.

## Exact hyperbolic repair

On a branch write
    w(t)=u e^t+v e^{-t},  |u|=|v|=rho0.
Choose i_+ with |u_{i_+}|>=rho0/sqrt(2) for t->+infinity and independently choose i_- with |v_{i_-}|>=rho0/sqrt(2) for t->-infinity. Apply the identical one-coordinate monotonicity/change-of-variable estimate on the two tails. Because |u|=|v|, both cutoff bounds and both 3 log 2 tail costs are unchanged. Therefore the envelope
    p_q(z) <= D^(-1/2) [ 6 + log_+(16 sqrt(D)/|z-v0|) ]
is unchanged, and all downstream constants in the 17 and nine/400 theorems remain unchanged.

## B11 Schur theorem and singular repair

For
    A = [[B,C],[C^T,D]],  B=B^T invertible,  S=D-C^T B^(-1) C,
let U be the block column (I ; C^T B^(-1)). Then exactly
    A = U B U^T + diag(0,S).
The first term has rank k=dim B. Rank perturbation gives
    s_{j+k}(A) <= s_j(S),
hence N_S(t)>=N_A(t)-k for every t>0, with no nonsingularity assumption on A or S.

If inertia(B)=(p,q), split UBU^T=R_+-R_- with R_+,R_- positive semidefinite of ranks p,q. Loewner monotonicity and finite-rank interlacing give the signed refinements
    N_S^+(t)>=N_A^+(t)-p,
    N_S^-(t)>=N_A^-(t)-q.

For singular B the naive Moore--Penrose Schur extension is false: with A=[[0,I_k],[I_k,0]] and B=0, the pseudoinverse Schur expression is zero although A has k positive and k negative unit eigenvalues. If range(C) is contained in range(B), however, X=B^dagger C gives the exact factorization
    A = (I ; X^T) B (I, X) + diag(0, D-C^T B^dagger C),
so the absolute loss is rank(B) and the signed losses are n_+(B), n_-(B).

## Policy-sharp counterexamples

Scalar threshold d in (0,1): choose N>d^(-1)-1, a^2=(d^(-1)-1)/N<1, u=(1,a,...,a), and A=d u u^T. The first coordinate is the unique scalar pivot at threshold d, all other diagonals are below d, every principal 2x2 determinant is zero, spectrum(A)={1,0,...}, and the selected scalar Schur complement is zero. At the nine-paper threshold d=3/40 one may take N=111, a=1/3.

Pair threshold p in (0,1): set eps=sqrt(p), choose m>eps^(-1)-1 and a^2=(eps^(-1)-1)/m<1. Let B=eps[[0,1],[1,0]], let U have first rows e1,e2 and then m copies of a e1 and m copies of a e2, and put A=U B U^T. Every diagonal is zero; the first pair is the unique pair pivot with determinant -p; every other principal pair determinant has smaller modulus; spectrum(A)={1,-1,0,...}; and the pair Schur complement is zero. At p=1/400 take eps=1/20, m=76, a=1/2. Thus an arbitrarily small indefinite pivot can consume exactly one positive and one negative threshold-large direction, even under the actual pivot-selection policy.

These examples rule out replacing the Schur charge by the number of threshold-large eigenvalues visible inside the pivot, by its norm, by a near-singularity parameter, or by alternate pivot selection.

## Threshold accounting after the audit

A complete source-present replacement at multiplicity eight is currently available in the repository at improvements/fleet01/B13/.../EIGHT_EIGENVALUE_REPLACEMENT.md (blob 8f792f8f80d70fd1eda26dfdabd855b9a6235e29), with a conservative bound 6010 K^2/s; the later corrected B17 reconstruction gives the same threshold with constant 400. The structural chain was rechecked here: V2 lower bound, good two-seed, two robust literal anchors, Gram lower bound, leverage split, rank-5/restricted-rank-2 contradiction, two-high-leverage exclusion, and product-safe disjoint incident third-volume receiver. The hyperbolic local repair above is required in its indefinite-pivot branch.

A five-singular-value theorem is described by two PASS audit documents under results/five-singular-values-2026-09-24/, but the advertised 1,093-line main.tex is absent from current master (direct fetch returns 404). Therefore multiplicity five is SOURCE-LEVEL UNCHECKED/PACKAGING-GAP in this run and is not promoted as the current source-audited replacement.

Accordingly the strongest complete replacement proof I can source-audit from present repository content is multiplicity eight. Multiplicity seven, four and the unrestricted three-eigenvalue density theorem remain open here.

## New compatible endpoint information

Fresh fleet03/B18 proves a fixed-hub Schur payment: if a=A_hh is nonzero and Omega_h is the ordered overlap-two bordered-minor energy through h, then
    ||p_Q||_infinity <= 8*2^(7/8) K^2 |a|^(-1/4) Omega_h^(-1/8).
The proof is source-valid: Omega_h=a^2 V2(S^(h)), a literal fair cut pays V2 by the grouped E2 half-potential receiver, then the original-coordinate scalar-square profile pays the hub. This narrows the lower-threshold obstruction but is not uniform when the shared hub diagonal tends to zero.

A fresh fleet01/B20 theorem pays a genuine two-hub zero-diagonal crossing block:
    Q=2 U^T C Y + q^T U + F(Y),  det(CC^T)=g>0
implies
    ||p_Q||_infinity <= e sqrt(pi) K^2 g^(-1/4).
The unresolved lower-threshold endpoint is therefore not Schur counting; it is a source-preserving receiver for shared-anchor packets when the available physical diagonal is zero or arbitrarily small and only one effective hub survives.

Unrestricted three-eigenvalue QFORM is OPEN / NOT PROVED / NOT DISPROVED.
