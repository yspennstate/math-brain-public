SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B15, 2026-09-24T06:36:01Z.
attacking: majority-sheet submass regularity and its limits: test whether square-root input-mass gains can aggregate without dimension loss, independently recheck the ruled rough-input bridge, and apply a completed e5f71d79 result to a genuine inequality or obstruction.

# account02/B15 — uniform multi-marginal stability on the ruled majority sheet and regular blow-up extraction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T063601Z-account02-B15-QFORM-auto11-r1`  
Status: `RULED_MULTI-MARGINAL_STABILITY_PROVED / MAJORITY_HALF-LINE_C0_PROVED / REGULAR_BLOWUP_EXTRACTION_PROVED / LOCAL-TRIPLE-DEGENERATION_FORCED / FULL_QFORM_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact status and first unpaid implication

The unrestricted owner theorem remains OPEN:

\[
C_*:=\sup_{\substack{n\ge3,\ s_3(A)\ge1\\
X_i\text{ independent},\ 0\le f_i\le1}}
\|p_{X^TAX}\|_\infty<\infty
\]

is not proved here and no QFORM counterexample is produced.

This run makes two target-relevant advances.

1. On the completed isotropic rank-three ruled majority sheet, the preceding one-coordinate square-root submass theorem telescopes with an **absolute** constant over simultaneous marginal changes. This gives a canonical `C_0([0,infinity))` majority-sheet density for arbitrary rough cap-one inputs and an explicit input-`L1` to output-`Linf` stability estimate. The essential height is paid separately by the owner-pinned `e5f71d79...` ruled theorem; continuity is downstream.

2. Combining the newest account03/B15 countable rational core, its fixed-matrix output-density stability, and its newest product-preserving localized-triple theorem yields a **regular counterexample extraction**: if `C_*=infinity`, there is a blow-up sequence with strictly positive real-analytic Schwartz marginals and rational algebraically generic matrices, while the best physical `3x3` principal block necessarily degenerates quantitatively like the reciprocal peak height.

Therefore the first unpaid implication is now even more sharply localized: obtain an aggregate-before-inversion estimate in the diffuse/no-good-physical-triple branch, in particular on the complementary convex/two-sheet contribution, while retaining original-coordinate product provenance. Rough-input limiting and output continuity are not that missing step.

## 2. Height language: essential boundedness comes first

For a finite positive measure `nu` on `R`, write

\[
H(\nu)=\sup_{I:\,|I|>0}\frac{\nu(I)}{|I|},
\]

with `I` ranging over bounded intervals. If `H(nu)<infinity`, then `nu<=H(nu) dx`, hence `nu` has an essentially bounded density. This conclusion uses no continuity.

All rough-input height passages below are made first at this interval-measure level. Continuous representatives are constructed only afterward.

## 3. Required source actually used: the completed ruled theorem

The required source was read at exactly

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`:

- `RESULTS.md`,
- `FOURIER_ROUTE_REPORT.md`,
- `COUNTEREXAMPLE_SEARCH.md`.

Its completed Theorem C states that for

\[
q_R(x)=\langle r_1,x\rangle^2+\langle r_2,x\rangle^2-\langle r_3,x\rangle^2,
\qquad r_1,r_2,r_3\text{ orthonormal},
\]

and arbitrary independent cap-one original-coordinate laws, the one-sheet side obeys

\[
\boxed{
\Pr\{q_R(X)\in I,\ q_R(X)\ge0\}\le\pi\sqrt2\,|I|.
}
\tag{3.1}
\]

This is the completed source result applied below to an actual output submeasure. It is not a continuity statement.

For smooth projected density `rho` on `R^3`, the source ruling is

\[
F(\theta,t)=\sqrt s\,e_\theta+t(e_\theta^\perp+e_3),
\qquad s\ge0,
\]

with exact coarea identity

\[
F_\theta\times F_t={1\over2}\nabla q_0(F),
\qquad
\delta(q_0-s)\,dy={1\over2}\,d\theta\,dt.
\tag{3.2}
\]

The ruling parameter is not arclength: `|e_theta^perp+e_3|=sqrt(2)`. Thus a line integral parameterized by `t` equals `1/sqrt(2)` times the corresponding two-dimensional orthogonal-projection density. The product-projection cap `2` then gives `sqrt(2)` per line, and the angular average in (3.2) yields exactly `pi sqrt(2)`.

## 4. Input from the preceding account02/B15 run: uniform one-coordinate submass gain

The preceding completed account02/B15 result is

`yspennstate/math-open-problems@45779cb1dca5f453ac620431b380ad015a052e70`.

It proves the following theorem for the same isotropic ruled form. Replace one ORIGINAL-coordinate probability density by an arbitrary cap-one subdensity `g` of mass `m<=1`, while keeping all other original-coordinate marginals arbitrary cap-one probabilities. Let `nu_g^+` be the positive-sheet output submeasure. Then

\[
\boxed{
H(\nu_g^+)\le20\sqrt2\,\sqrt m.
}
\tag{4.1}
\]

The proof keeps the exact ruled coarea factor, the non-arclength speed, and the product-projection provenance. Its rough-input conclusion is transported by total variation, not by continuity.

## 5. New theorem: simultaneous multi-marginal majority-sheet stability

### Theorem 5.1 — `QFORM-RULED-MULTIMARGINAL-HOLDER-v1`

Let `R in R^(n x 3)` have orthonormal columns. For two collections of independent cap-one probability densities

\[
f=(f_1,\dots,f_n),\qquad g=(g_1,\dots,g_n),
\]

let `nu_f^+` and `nu_g^+` be the positive-sheet output measures for `q_R`, and let `r_f^+,r_g^+` be any essentially bounded density representatives. Put

\[
\delta_j=\|f_j-g_j\|_1.
\]

Then

\[
\boxed{
\|r_f^+-r_g^+\|_{L^\infty([0,\infty))}
\le40\sum_{j=1}^n\sqrt{\delta_j}.
}
\tag{5.1}
\]

The constant `40` is independent of `n`, `R`, the laws, and the changed coordinates; dimension enters only through the explicit finite sum.

### Proof

Telescope the two product densities in original coordinates:

\[
\prod_i f_i-\prod_i g_i
=
\sum_{j=1}^n
(f_j-g_j)
\prod_{i<j}f_i
\prod_{i>j}g_i.
\tag{5.2}
\]

For each `j`, write

\[
f_j-g_j=h_j^+-h_j^-.
\]

Since `f_j,g_j` are probability densities,

\[
\int h_j^+=\int h_j^-={\delta_j\over2},
\tag{5.3}
\]

and because `0<=f_j,g_j<=1`, both `h_j^+` and `h_j^-` are cap-one subdensities.

Apply (4.1) separately to the two positive submeasures generated by `h_j^+` and `h_j^-`. Each has majority-sheet density height at most

\[
20\sqrt2\sqrt{\delta_j/2}=20\sqrt{\delta_j}.
\tag{5.4}
\]

The signed `j`-th telescoping contribution therefore has `L^infinity` norm at most `40 sqrt(delta_j)`. Summing the signed output measures proves (5.1).

No continuity is used in this proof; it is a consequence of interval domination for positive submeasures plus the signed measure identity.

### Scope warning

The right side contains `sum_j sqrt(delta_j)`. It is useful for fixed finite `n` and for constructing canonical representatives, but it is **not** a dimension-free replacement for the still-open QFORM height estimate. In particular, it must not be confused with an aggregate curvature theorem.

## 6. New downstream regularity: canonical majority density in `C_0([0,infinity))`

### Theorem 6.1 — `QFORM-RULED-MAJORITY-HALFLINE-C0-v1`

For every arbitrary rough cap-one product law in Theorem 5.1, the positive-sheet output measure has a canonical density

\[
r_f^+\in C_0([0,\infty))
\]

such that

\[
\boxed{0\le r_f^+(s)\le\pi\sqrt2\qquad(s\ge0).}
\tag{6.1}
\]

For any second product law `g`, the canonical representatives satisfy the pointwise version of (5.1).

### Proof: smooth approximation only after the height theorem

For every original marginal choose cap-preserving compactly supported smooth probability approximants

\[
f_{j,k}\in C_c^\infty(\mathbb R),
\qquad
0\le f_{j,k}\le1,
\qquad
\|f_{j,k}-f_j\|_1\to0.
\tag{6.2}
\]

Such approximants can be made by truncating, mollifying without increasing the cap, and restoring the missing mass in a disjoint far-away smooth bump of height at most one.

Let `F_k=prod_j f_{j,k}`. Because `R^T` is surjective, the projected density

\[
\rho_k(y)=\int_{\ker R^T}F_k(Ry+z)\,dz
\]

is `C_c^infinity(R^3)`. For `s>=0`, the exact source ruling gives the pointwise formula

\[
r_k^+(s)
={1\over2}\int_0^{2\pi}\int_{\mathbb R}
\rho_k\bigl(\sqrt s\,e_\theta+t(e_\theta^\perp+e_3)\bigr)
\,dt\,d\theta.
\tag{6.3}
\]

For `s` in a compact neighborhood of any `s_0>=0`, compact support of `rho_k` restricts the relevant `t` to a common bounded interval. The integrand is jointly continuous in `(s,theta,t)`; dominated convergence therefore proves that `r_k^+` is continuous all the way to the cone vertex `s=0`. Since `F_k` is compactly supported, `r_k^+` vanishes for all sufficiently large `s`, hence

\[
r_k^+\in C_0([0,\infty)).
\tag{6.4}
\]

Apply Theorem 5.1 to two approximants `F_k,F_l`:

\[
\|r_k^+-r_l^+\|_\infty
\le40\sum_j\sqrt{\|f_{j,k}-f_{j,l}\|_1}
\longrightarrow0.
\tag{6.5}
\]

Thus `r_k^+` converges uniformly on the whole half-line to a function `r_f^+ in C_0([0,infinity))`.

To identify the limit measure, product telescoping gives

\[
\|F_k-F\|_1\le\sum_j\|f_{j,k}-f_j\|_1\to0.
\tag{6.6}
\]

Restriction to `{q_R>=0}` and deterministic pushforward by `q_R` contract total variation. Hence for every bounded interval `I`,

\[
\nu_{f,k}^+(I)\to\nu_f^+(I).
\tag{6.7}
\]

Uniform convergence in (6.5) also gives

\[
\int_I r_k^+\to\int_I r_f^+.
\]

Therefore `nu_f^+(I)=int_I r_f^+` for every bounded interval, so `r_f^+` is the canonical density of the rough positive-sheet measure.

Finally, the completed `e5f71d79...` Theorem C gives for each smooth approximant

\[
0\le r_k^+(s)\le\pi\sqrt2.
\]

Passing to the uniform limit proves (6.1). **The height was paid by the ruled interval theorem before continuity was constructed.**

Because the canonical representatives are continuous, the essential estimate (5.1) upgrades automatically to the pointwise supremum estimate stated there.

## 7. Independent audit of the ruled rough-input bridge

The preceding proof gives one audit in the homogeneous isotropic setting. The same logic works for the affine conditional form assigned by the continuation.

Condition on all original coordinates outside an invertible active physical `3x3` block `B`. The conditional polynomial is

\[
Q_w(x)=x^TBx+2d(w)^Tx+c_0(w).
\]

Since `B` is invertible,

\[
Q_w(x)
=(x+B^{-1}d(w))^TB(x+B^{-1}d(w))+c(w).
\tag{7.1}
\]

Thus the later affine-range correction is automatically satisfied: the affine term lies in `Range(B)`. More importantly, square completion is only a deterministic **translation in the original three independent coordinates**. It does not claim independence after diagonalizing `B`.

For rough active marginals, mollify only those original coordinates. Cap one and independence are preserved, and

\[
\left\|\prod_{i=1}^3f_i^{(\eta)}-
\prod_{i=1}^3f_i\right\|_1
\le\sum_{i=1}^3\|f_i^{(\eta)}-f_i\|_1\to0.
\tag{7.2}
\]

The translation in (7.1) does not change the `L1` error. Restriction to the fixed conditional majority event and deterministic quadratic pushforward contract total variation. Hence any smooth ruled interval estimate passes to arbitrary rough cap-one active marginals with the **identical coefficient**.

The geometric factors also remain exactly those of the source: the coarea factor is `1/2`, and after anisotropic spectral scaling the ruling direction

\[
v_\theta=
\left(
-{\sin\theta\over\sqrt{\lambda_1}},
{\cos\theta\over\sqrt{\lambda_2}},
{1\over\sqrt\mu}
\right)
\]

is not arclength, so the line estimate contributes `1/|v_theta|`. With the two-dimensional product-projection cap `2`, this reproduces the completed source coefficient

\[
(\lambda_1\lambda_2\mu)^{-1/2}
\int_0^{2\pi}
{d\theta\over
\sqrt{\sin^2\theta/\lambda_1+
\cos^2\theta/\lambda_2+1/\mu}}.
\tag{7.3}
\]

No output continuity is used in this rough height passage.

## 8. Newest account03/B15 continuation consumed

The newest compatible account03/B15 report read during this run is

`yspennstate/math-open-problems@4bd938cedd73ec402daa15e56294b754c29ec814`,

with rigor addendum

`yspennstate/math-open-problems@40b108ab5984542e26b8c8ff2cd059e13446bea8`.

It proves a product-preserving localized physical-triple theorem. If some ORIGINAL-coordinate principal `3x3` block `B` has all three eigenvalue magnitudes at least `s>0`, then

\[
\boxed{
\|p_{X^TAX}\|_\infty
\le {C_{loc}\over s},
\qquad
C_{loc}=128\,2^{1/4}<153,
}
\tag{8.1}
\]

with arbitrary outside coefficients/cross-couplings and rough cap-one input laws. Continuity is added only afterward by the same-constant `C_0` compiler.

This repaired theorem uses original-coordinate scalar/pair pivots and does not use the refuted arbitrary-joint coarea height lemma.

## 9. Countable rational core from the preceding account03/B15 continuation

The immediately preceding account03/B15 theorem at

`yspennstate/math-open-problems@6ea11aaafcf72491b05cb7b51b93166a91e1ad2d`

with rigor check

`yspennstate/math-open-problems@8d15f0dd3348e545d9854ae08a914588da315505`

proved that the exact full universal interval constant equals its restriction to a **countable** rational skeleton:

- rational symmetric matrices with simple spectrum, every nonempty principal minor nonzero, and at least three eigenvalues of modulus strictly bigger than one;
- marginals `1_E`, where `E` is a finite union of rational-endpoint intervals of total length one;
- rational output intervals.

Using the completed fixed-instance `C_0` theorem, the same result is equivalently

\[
C_*
=
\sup_{\theta\in\mathscr S}
\sup_{y\in\mathbb Q}p_\theta(y),
\tag{9.1}
\]

where `S` is countable and every `p_theta` is an individually bounded continuous density. This is an exact reduction, not a proof that the supremum is finite.

## 10. Regular blow-up extraction with forced physical-triple degeneration

### Theorem 10.1 — `QFORM-REGULAR-BLOWUP-LOCALTRIPLE-DEGENERATION-v1`

Assume, conditionally, that the owner conjecture is false, i.e. `C_*=infinity`. Then for every integer `N>=1` there exist

- a dimension `n_N`;
- a **rational algebraically generic** symmetric matrix `A_N` having at least three eigenvalues of modulus `>1`;
- independent probability densities `f_{i,N}` that are **strictly positive, real analytic, Schwartz, and bounded by one**;
- a rational output point `y_N`;

such that the canonical output density `p_N in C_0(R)` satisfies

\[
\boxed{p_N(y_N)>N.}
\tag{10.1}
\]

Define the best physical-triple conditioning scale

\[
\kappa_3(A)
=
\max_{|S|=3}
\min_{\lambda\in\operatorname{spec}(A_{S,S})}|\lambda|.
\tag{10.2}
\]

Then the same witnesses may be chosen so that

\[
\boxed{
0<\kappa_3(A_N)
< {C_{loc}\over N}
< {153\over N}.
}
\tag{10.3}
\]

Thus any failure sequence can be made perfectly smooth at the input and algebraically generic at the matrix level, while **every** physical triple becomes quantitatively ill-conditioned. Exact singularities are unnecessary; reciprocal local conditioning is forced to diverge.

### Proof

By (9.1), for each `N` choose a rational-skeleton instance

\[
(A_N,1_{E_{1,N}},\dots,1_{E_{n_N,N}})
\]

and `y_N in Q` with canonical density `p_N^(0)` satisfying

\[
p_N^{(0)}(y_N)>2N.
\tag{10.4}
\]

Keep the matrix fixed and Gaussian-smooth every original marginal:

\[
f_{i,N,\sigma}=1_{E_{i,N}}*\gamma_\sigma.
\tag{10.5}
\]

For every `sigma>0`, this is a probability density with

\[
0<f_{i,N,\sigma}\le1,
\]

and it is real analytic and Schwartz. As `sigma downarrow0`, it converges to `1_E` in `L1`.

The completed account03/B15 fixed-matrix density-stability theorem at

`yspennstate/math-open-problems@696a0784ba7d270db657c1596d9c2ee940a1745d`

proves, for every fixed rank-at-least-three matrix, uniform output-density convergence under cap-preserving marginal `L1` approximation. Therefore, for the fixed `A_N`,

\[
\|p_{N,\sigma}-p_N^{(0)}\|_\infty\to0.
\tag{10.6}
\]

Choose a **rational** `sigma_N>0` sufficiently small that

\[
p_{N,\sigma_N}(y_N)>N.
\]

Set `p_N=p_{N,sigma_N}` and `f_{i,N}=f_{i,N,sigma_N}`. This proves (10.1) with strictly positive analytic Schwartz sources.

Because `A_N` is algebraically generic, every physical `3x3` principal block is invertible, so `kappa_3(A_N)>0`. Choose a triple attaining the maximum in (10.2). The newest account03/B15 localized theorem (8.1), applied with `s=kappa_3(A_N)`, gives

\[
\|p_N\|_\infty
\le {C_{loc}\over\kappa_3(A_N)}.
\tag{10.7}
\]

Together with `p_N(y_N)>N`, this forces

\[
\kappa_3(A_N)<{C_{loc}\over N},
\]

which is (10.3).

### Interpretation

This is a **conditional obstruction**, not a counterexample to QFORM. It says that if QFORM fails, the failure cannot fundamentally require rough marginal discontinuities, compact-support edges, exact repeated eigenvalues, or exact vanishing physical minors. It can be witnessed by regular analytic inputs and generic matrices, but only while the best physical triple degenerates quantitatively.

Therefore any proof that selects one physical triple and pays a reciprocal conditioning constant cannot be the final matrix-uniform argument. Aggregation must occur before that reciprocal loss.

## 11. A second direct application of the required e5f71d79 result

The completed `e5f71d79...` Theorem C gives not only the height (3.1) but, after Theorem 6.1, the concrete regularity package

\[
\boxed{
r_f^+\in C_0([0,\infty)),
\qquad
0\le r_f^+\le\pi\sqrt2,
}
\tag{11.1}
\]

and for two arbitrary rough product inputs

\[
\boxed{
\|r_f^+-r_g^+\|_\infty
\le40\sum_j\sqrt{\|f_j-g_j\|_1}.
}
\tag{11.2}
\]

At the triangular-kernel scale, (3.1) also yields the actual owner-style inequality

\[
\boxed{
\mathbb E\bigl[(\varepsilon-|q_R(X)-y|)_+
\mathbf 1_{\{q_R(X)\ge0\}}\bigr]
\le\pi\sqrt2\,\varepsilon^2.
}
\tag{11.3}
\]

Indeed integrate the tent against the positive-sheet density bounded by `pi sqrt(2)`. This is an essential-height consequence. The later continuity theorem is not used to establish it.

## 12. Absolute continuity remains strictly weaker

For completeness, if `A!=0` and the joint input law merely has an absolutely continuous density `F`, then `q(x)=x^TAx` has critical set `ker A`, a proper Lebesgue-null subspace. For a Lebesgue-null set `N`, local coarea on

\[
\{|x|\le k,\ |\nabla q(x)|\ge1/k\}
\]

shows that `q^{-1}(N)` outside `ker A` is null; hence the quadratic pushforward is absolutely continuous.

This proves existence of a density under much weaker hypotheses than the owner target, but gives **no** finite universal height and no continuity. The `L^infinity` estimates above are paid separately by interval domination; continuity is then proved separately by the uniform-density limit or by the fixed-instance `C_0` compiler.

## 13. What remains open

The full owner theorem is still OPEN. The new regular-blow-up extraction and the live diffuse-bank correction point in the same direction: a proof must pay collective original-coordinate geometry before choosing or inverting a nearly singular physical triple.

The ruled majority sheet is now unusually clean:

- rough interval height paid uniformly by `e5f71d79...`;
- exact coarea and reciprocal ruling speed audited;
- one-coordinate submass gain `O(sqrt(m))` uniform in dimension/orientation;
- simultaneous marginal stability (5.1);
- canonical half-line `C_0` density (6.1).

The complementary convex/two-sheet contribution and higher-rank diffuse/no-good-pivot structure remain the first unpaid analytic/structural obligations. The live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction still forbids discarding product provenance and replacing the missing step by a generic X-ray bound.

## 14. Source discipline

Fresh owner programme: `QFORM-DENSITY-3EIG-20260922`, OWNER CONTROL revision `2026-09-22.15`.

Required source actually read: `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, all three named files.

Newest designated partner consumed: account03/B15 `math-open-problems@4bd938cedd73ec402daa15e56294b754c29ec814`, rigor addendum `40b108ab5984542e26b8c8ff2cd059e13446bea8`.

Countable-core partner dependency: account03/B15 `6ea11aaafcf72491b05cb7b51b93166a91e1ad2d`, rigor addendum `8d15f0dd3348e545d9854ae08a914588da315505`.

Fixed-matrix density-stability dependency: account03/B15 `696a0784ba7d270db657c1596d9c2ee940a1745d`.

Fixed-instance regularity dependency: account02/B15 `9b8bb7e84811978a2c46c7bb5ec50f2570dbc056`.

Repository transport was authenticated, but authenticated native mathematical receiver ingestion/use was not verified. Execution therefore remains `WITHOUT_VERIFIED_BRAIN`.
