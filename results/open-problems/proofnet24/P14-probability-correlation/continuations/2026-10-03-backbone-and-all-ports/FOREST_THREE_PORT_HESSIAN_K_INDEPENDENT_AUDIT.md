# Independent audit of the hypothetical-triangle backbone lemma

2 October 2026. **PASS.** The parent proposed the hypothetical-triangle
reduction; I independently reconstructed the polynomial, checked the precise
primary matroid theorem, derived the Hessian and homogeneous strictness
bound, and wrote separate literal-graph checks. No mathematical gap was
found in the lemma proved in
[`forest_three_port_hessian_lemma_k_proof.md`](forest_three_port_hessian_lemma_k_proof.md).
Historical novelty and the full matching proof are separate matters.

The crucial points are:

1. Adding one hypothetical edge \(ij\) has coefficient \(A_{ij}\). Adding
   any two triangle edges is accepted precisely on the all-separated
   backbone partition, giving coefficient \(r\). The cubic is forbidden
   by the new triangle itself. This holds for parallel edges and after
   conditioning ports to coincide. It is an ordinary unrooted-forest
   calculation, with no component-size root factors.
2. Theorem 4.1 of Anari–Liu–Oveis Gharan–Vinzant,
   [arXiv:1811.01600v1](https://arxiv.org/pdf/1811.01600), uses the
   coefficient-one homogeneous independent-set polynomial. Its affine
   restriction lemma permits dummy coordinate one and fixed backbone
   activities. Thus log-concavity applies to the actual triangle polynomial,
   including boundary activities by continuity. No factorial-normalized
   polynomial or off-diagonal Hessian-sign assertion is substituted.
3. At zero, negative logarithmic Hessian is exactly
   \((\mathbf A\mathbf A^T-rF(\mathbf1\mathbf1^T-I))/F^2\). Its full PSD
   inequality, evaluated on \((b_1b_2,b_1b_3,b_2b_3)\), gives
   \(M^2\geq2BJF\). A one-apex scalar derivative only gives factor \(3/2\)
   and is insufficient. That earlier gap is now closed.
4. Homogeneous Euler identity and PSD Cauchy–Schwarz give the additional
   bound \(M^2-2BJF\geq M^2/N\), so strictness follows whenever \(M>0\).
   The proof does not silently assume strict log-concavity. All formulas
   include \(M=0\), \(J=0\), zero columns and port identifications.
5. Conditioning required-present backbone edges is graphic-matroid
   contraction; conditioning absent edges is deletion. The fixed required
   activity product is a common positive factor. This preserves the proof
   while permitting loops/parallel edges and \(r=0\). Arbitrary positive
   fields are already allowed activities.

The independent checker directly evaluated every unweighted labeled
backbone on at most six vertices (33864 graphs) and 106 weighted/conditioned
literal examples. It checked every principal minor of the ordinary and
degree-sharpened three-by-three matrices, the scalar cone, and the full
eight-coefficient augmented triangle expansion. All computations were exact.
Source and record:

- [`forest_three_port_hessian_lemma_k_exact.py`](forest_three_port_hessian_lemma_k_exact.py)
- [`forest_three_port_hessian_lemma_k_exact_results.json`](forest_three_port_hessian_lemma_k_exact_results.json)

The checks supplement the analytic proof; the finite sweep is not used to
extrapolate to all graphs. They preserve the false arbitrary-row proposal
\((1,0,0,0,1)\), whose cone gap is \(-3\), and distinguish the valid full PSD
inequality from the unproved stronger off-diagonal Rayleigh inequalities.

The lemma is ready for use in the separately owned arbitrary-backbone
matching marginal proof. This audit does not certify that marginal's full
OR-law, its increasing-event reduction, or historical priority, and does
not assert a theorem for all forest edge indicators.
