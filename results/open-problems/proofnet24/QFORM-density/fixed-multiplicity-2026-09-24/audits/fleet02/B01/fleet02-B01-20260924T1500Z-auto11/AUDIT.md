# Fleet02/B01 independent full audit — nine-eigenvalue constant-400 candidate

Run: `fleet02-B01-20260924T1500Z-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Lens: theorem quantifiers, scaling, dependency closure; fleet02 counterexample emphasis.

## Exact sources

Latest candidate audited line-by-line:
- source commit: `eeb752c8943536541b34b42b8bf48e924f4d3d2f`
- source path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex`
- source blob: `19fb119877426b640b2c0dae19ec2f78a399fe11`
- recorded SHA-256: `bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3`
- source length: 955 lines.

I also read the candidate README, NINE_400_AND_OVERLAP.md, AUDIT_NEW.md, MANIFEST.json, proof_map.csv, verify_new.py and checks_new.json, and independently read the complete preserved 790-line seventeen-eigenvalue baseline:
- baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`
- baseline blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`
- baseline SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

Prior PASS reports were not used as substitutes for the reconstruction below.

## Verdict

**PASS** for the mathematical claim in the exact nine-eigenvalue source:
[
s_9(A)ge s>0,quad 0le f_ile K
quadLongrightarrowquad
|p_{X^TAX+b^TX+c}|_inftyle 400K^2/s.
]

All input quantifiers are preserved: arbitrary dimension, arbitrary independent real rough coordinate laws under the density cap, arbitrary real symmetric A, arbitrary signature and remaining spectrum, and arbitrary affine b,c. No moments, iid assumption, compact support, log-concavity, exact rank, diagonal basis, or post-rotation independence is introduced.

This review does **not** claim the unrestricted three-eigenvalue conjecture. The eight-eigenvalue theorem is also still open. The overlap theorem is supporting algebra only.

## Complete line coverage

The companion `LINE_AUDIT.csv` covers every source line 1–955 by contiguous ranges. The companion `LABEL_AUDIT.csv` separately checks every label/equation entry in the supplied proof map. No source interval is left UNCHECKED for mathematical validity. Novelty/priority is outside this review and remains UNCHECKED.

## Quantifiers and scaling — PASS

Lines 46–84 and 833–860 preserve the theorem's exact hypotheses. The normalization is exact: for (Y=KX), every coordinate density of Y is at most one and
[
widetilde Q
=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c
=(K^2/s)Q.
]
Thus (Q=(s/K^2)widetilde Q), so a normalized constant C becomes (CK^2/s). Affine terms scale consistently.

## Independent dependency reconstruction

1. **Fourier foundations, lines 85–164 — PASS.** Plancherel has the correct (2pi) normalization. Gaussian inversion and the Riesz representation are justified by Tonelli/dominated convergence. The envelope integrals give exactly the displayed powers.
2. **Spectral algebra, 165–215 — PASS.** Singular-value perturbation is used correctly for nonsymmetric auxiliaries. The Schur count loses at most the pivot dimension, including the singular-A limiting case. Strict diagonal dominance is applied only after locating the forced diagonal entries in the complement L.
3. **Geometric BL, projections, scalar Fourier powers, 216–297 — PASS.** The heat-flow sign is correct; the large-time limit uses the frame trace. Product projections are deterministic integrals, not rotated-independence assertions. The scalar Fourier-power proof works for every real p>=2 by lowering to an even exponent.
4. **Decoupling / determinant, 298–396 — PASS.** Difference coordinates remain independent and cap-one. The graph frame has the stated weights; (alpha=(2pi e)^2) cancels the entropy factors, and the fourth root gives determinant exponent (-1/8). Order five is used for density, order three only for a half potential.
5. **Grouped mollified-L2 receiver / promotion, 397–527 — PASS.** Jensen is applied first to (mu_t*ho_delta). The pure J phase is removed only after integrating the original independent I variables. Weighted Hölder is valid for the finite kernel measure because the weights sum to one; probability normalization is unnecessary. The projected map has Gram determinant (S^2det(C_TC_T^T)). The entropy identity has the correct sign. Approximate-identity passage is legitimate because (mu_tin L^2). Row promotion retains literal original hubs and all their remaining couplings. The final scales are (Z_3^{-1/6}) for density and (Z_2^{-1/8}) for a full half potential.
6. **Pivot analytic inputs, 528–662 — PASS.** Scalar completion is a conditional domination identity, not an independence statement. Definite-pair rotation occurs only inside a two-dimensional integral. The hyperbolic Jacobian is (1/(2sqrt D)); the tail rearrangement uses only density cap and mass. The quarter-power concentration proof uses joint crossing decay, not the false law-uniform scalar Fresnel estimate.
7. **Disjoint-minor interpolation, 663–766 — PASS.** Singular deleted seeds are excluded where invertibility is required. The volume count is an inequality in the correct direction. The interpolation P may be nonsymmetric; its correction has global rank <=3r and complement rank <=r. D vanishes on the seed; E has zero diagonal. With d=3/40, p=1/400, h=2/25, the exact dominance margins are 1131/2200 and 51/2200 for r=1,2. The random cut loses exactly (4^{-k}).
8. **Full pair half potential / five-direction compiler, 767–832 — PASS.** Output scaling is (D^{-1/4}), not (D^{-1/2}). In the indefinite case the near/far split at 1/64 gives (12+5log2<16). The scalar-pivot branch explicitly restores the outer tail of the full half potential.
9. **Main theorem, 833–860 — PASS.** The no-pivot, scalar-pivot, definite-pair and indefinite-pair cases exhaust all matrices. The Schur spectral counts are stronger than the residual hypotheses consumed.
10. **Overlap theorem, 861–925 — PASS as stated.** D diagonal and E zero-diagonal are Frobenius-orthogonal. Best rank-3r approximation supplies the spectral tail. Same-index bordered determinants give the W term exactly and distinct-index borders are controlled by ((r+1)^2V_{r+1}). Therefore the s8 overlap inequality is valid, but it is not a density theorem.

## Constants independently recomputed

From the displayed formulas:
- (C_3=14.818337662843);
- (C_2=12.095072570796486);
- no-pivot density (=370.458441571075<375);
- scalar / no-pivot residual (<255.604<280);
- scalar / pair residual (<261.279<320);
- scalar / scalar residual (=360.8472793874<383);
- definite pair (<62.832<80);
- indefinite pair (=384.5746868807<392.5<400).

Thus 400 has strict slack in every normalized branch.

## Counterexample stress and the eight-direction boundary

The false shortcut “overlap-one bordered third volume can be fed directly into the disjoint (Z_3) theorem” is explicitly refuted in the companion improvement note.

A five-coordinate symmetric block
[
B=egin{pmatrix}
0&0&1&0&1\
0&0&0&1&0\
1&0&0&0&1\
0&1&0&0&0\
1&0&1&0&0
end{pmatrix}
]
has spectrum ({2,1,-1,-1,-1}). For S={1,2}, T={3,4}, h=5, the 2x2 seed is the identity and the overlap-one bordered determinant is -1. Yet in five active coordinates every disjoint physical crossing block has rank at most two. Direct-summing B with three scalar [1] blocks produces an eight-dimensional symmetric A with (s_8(A)=1), nonzero overlap-one 3-minor, and (Z_3(A_{I,J})=0) for every literal disjoint cut I|J. This does not disprove an eight-eigenvalue density theorem; it disproves a naive replacement of overlap mass by disjoint third crossing volume.

## Remaining proof obligation below nine — GAP

The paper correctly stops at the algebraic overlap estimate. In the no-pivot s8 chamber the same physical coordinate h appears as both added row and added column. Duplicating h invents independence; conditioning h deletes the third bilinear direction; treating h as one hub leaves a rank-two seed and requires a new analytic resource.

The exact missing receiver should control an overlap packet through
[
det A_{Scup{h},Tcup{h}}
=det(A_{S,T})left(A_{hh}-A_{h,T}A_{S,T}^{-1}A_{S,h}ight)
]
while using the random coordinate h only once and retaining arbitrary same-bank quadratic terms. Until such a product-preserving shared-coordinate estimate is proved, threshold eight is not closed.

## Historical seventeen-eigenvalue baseline

The preserved seventeen-eigenvalue manuscript was independently read in full. Its theorem/scaling, Fourier determinant route, nonsymmetric interpolation, spectral-to-volume conversion, pivot half-potential compiler and final constant are internally consistent on this pass. It is now a corollary-level historical baseline rather than the current threshold.

## Review gate

This artifact is one complete independent review of blob `19fb119877426b640b2c0dae19ec2f78a399fe11`. During this run a distinct fleet01/B20 full review of the same blob was also fetched and found to report PASS with no conflicting mathematical finding. The two artifacts are separate reviews; this B01 report does not alter protected release metadata or claim journal/formal verification.
