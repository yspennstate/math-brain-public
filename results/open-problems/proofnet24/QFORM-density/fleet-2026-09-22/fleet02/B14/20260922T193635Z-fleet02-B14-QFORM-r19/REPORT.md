# fleet02/B14 — exterior-volume localization barrier and bank-preserving transfer

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T193635Z-fleet02-B14-QFORM-r19`  
**Assignment:** Translations and localization  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** proved supporting localization theorem + rigorous target-family obstruction to bounded-active-set localization. Full QFORM remains OPEN.

## 1. First unpaid implication

The determinant-only physical-triple theorem now gives a clean localized certificate, but the three-large-eigenvalue hypothesis does not force a physical principal triple with determinant bounded below. The first unpaid implication is therefore not another support truncation: it is to preserve and aggregate the *off-diagonal exterior-volume bank* before conditioning away the coordinates that carry it.

This report proves exactly where that bank lives and shows quantitatively that no bounded-size original-coordinate localization can retain a constant fraction of it, even on an exact rank-three target family.

## 2. Source-pinned partner theorem used

Completed assigned-partner result:

- fleet03/B14, run `20260922T190524Z-fleet03-B14-QFORM-r16`
- canonical commit `89e6481f4f7ed7d49a77cfcb989ee93572d5d5cd`
- path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B14/20260922T190524Z-fleet03-B14-QFORM-r16/REPORT.md`
- theorem `QFORM-PRINCIPAL-TRIPLE-DETERMINANT-LOCALIZATION-v1`:

For every original-coordinate triple `I` with nonsingular principal block `B=A_{I,I}`, every independent cap-one input law and every deterministic affine perturbation,

\[
\|p_Q\|_\infty\le 32\sqrt{10}\,|\det B|^{-1/3}.
\]

The theorem is uniform in arbitrary outside coefficients, outside couplings, translations, support geometry and moments. I use only this stated scope.

Relevant live corrections consumed include the facts that one uniformly good physical triple need not exist, local cross-rank-three dichotomies fail on bank families, and law localization must not normalize tiny fragments and then pay a blown-up density cap. None of the results below uses arbitrary-joint coarea or conditional positive moments.

## 3. Exact bank-preserving partial localization

### Theorem 1 — `QFORM-PARTIAL-LOCALIZATION-ZERO-TAX-v1`

Let `A` be real symmetric, let `S` be any set of original coordinates, and write `T=S^c`. Let the coordinates of `X` be independent with probability densities bounded by one. Suppose there is a constant `C_S(A)` such that for every deterministic `z` in the outside coordinates, every cap-one product law on the active coordinates, and every affine vector/constant, the quadratic polynomial

\[
q_z(x_S)=x_S^T A_{S,S}x_S+\ell(z)^Tx_S+c(z)
\]

has a density bounded by `C_S(A)`, uniformly in `z,\ell,c`. Then the full quadratic form `Q=X^TAX` has density bounded by the *same* constant:

\[
\boxed{\|p_Q\|_\infty\le C_S(A).}
\]

No support, moment, centering, compactness or fragment assumption is required.

### Proof

Condition on `X_T=z`. Independence of the original coordinates means that the conditional law of `X_S` is exactly the same product of the original cap-one marginals; only the affine term and additive constant of the active polynomial change. Hence, for every interval `J`,

\[
\Pr\{Q\in J\mid X_T=z\}\le C_S(A)|J|
\]

for almost every `z`. Integrating in `z` gives

\[
\Pr\{Q\in J\}\le C_S(A)|J|.
\]

Lebesgue differentiation yields the asserted essential density bound. The proof is mass-linear and therefore also survives arbitrary positive subprobability localization of the outside law without renormalizing any active marginal. ∎

This theorem records the precise zero-tax interface: conditioning outside `S` preserves the entire physical Hessian `A_{S,S}` and turns all outside effects into arbitrary affine shifts. Conversely, any mixed curvature using a row or column outside `S` is destroyed by this conditioning and becomes affine data.

## 4. Exterior-volume identity

For `|I|=|J|=3`, write

\[
d_{I,J}=\det A_{I,J}.
\]

The matrix of the exterior-power operator `\wedge^3 A` in the standard coordinate wedge basis has entries `d_{I,J}`. Therefore

\[
\boxed{
\sum_{|I|=|J|=3} d_{I,J}^2
=\|\wedge^3 A\|_{HS}^2
=e_3(s_1(A)^2,\ldots,s_n(A)^2),
}
\tag{4.1}
\]

where `s_i(A)` are the singular values. In particular, if at least three singular values are at least one,

\[
\sum_{I,J}d_{I,J}^2\ge1.
\tag{4.2}
\]

Thus the target spectral assumption always contains one unit of third exterior-volume mass, but it need not lie on principal triples `I=J`.

For an active coordinate set `S`, the amount retained after conditioning `S^c` is exactly

\[
\mathcal E_3(S):=
\sum_{\substack{I,J\subset S\\|I|=|J|=3}}d_{I,J}^2
=\|\wedge^3 A_{S,S}\|_{HS}^2.
\tag{4.3}
\]

Theorem 1 therefore preserves `\mathcal E_3(S)` at zero probabilistic cost, but cannot preserve exterior mass whose row or column support exits `S`.

## 5. Exact target-family obstruction to bounded active sets

### Theorem 2 — `QFORM-BOUNDED-ACTIVE-SET-EXTERIOR-MASS-FALSE-v1`

For every `m>=1`, let

\[
A_m=[1]\oplus \frac1mJ_m\oplus\left(-\frac1mJ_m\right),
\tag{5.1}
\]

where `J_m` is the all-ones matrix. Then `A_m` is symmetric and its nonzero spectrum is exactly

\[
\{1,1,-1\}.
\]

Hence it lies in the exact target class with three singular values equal to one.

Let `0` denote the singleton coordinate, `P` the positive bank and `N` the negative bank. For a coordinate subset `S`, let

\[
p=|S\cap P|,\qquad q=|S\cap N|.
\]

Then

\[
\boxed{
\mathcal E_3(S)=
\begin{cases}
\dfrac{p^2q^2}{m^4},&0\in S,\\[6pt]
0,&0\notin S.
\end{cases}}
\tag{5.2}
\]

Consequently, if `|S|<=k`,

\[
\boxed{
\mathcal E_3(S)
\le \frac{(k-1)^4}{16m^4}.
}
\tag{5.3}
\]

In particular, for every fixed `k`,

\[
\sup_{|S|\le k}\mathcal E_3(S)\longrightarrow0
\qquad(m\to\infty),
\]

even though the global mass is exactly

\[
\mathcal E_3(\{1,\ldots,2m+1\})=1.
\tag{5.4}
\]

More quantitatively, retaining a fixed fraction `c in (0,1]` of the global exterior mass forces

\[
\boxed{|S|\ge1+2c^{1/4}m.}
\tag{5.5}
\]

Thus any localization principle that first conditions down to `O(1)` original coordinates necessarily loses essentially all third exterior-volume mass on this valid target family.

### Proof

The two bank blocks `J_m/m` and `-J_m/m` have ranks one and eigenvalues `1` and `-1`; the singleton contributes the third eigenvalue `1`, proving the spectral statement.

A `3x3` mixed minor `A_{I,J}` is nonzero exactly when both `I` and `J` contain the singleton, one positive-bank coordinate and one negative-bank coordinate. In that case block diagonality and the constant bank entries give

\[
|\det A_{I,J}|=\frac1{m^2}.
\]

Inside an active set containing the singleton there are `pq` choices of `I` and independently `pq` choices of `J`; hence there are `p^2q^2` nonzero mixed minors, each with square `m^{-4}`. This proves (5.2). If the singleton is absent, the compression has rank at most two, so every third minor vanishes.

If `|S|<=k`, then `p+q<=k-1` and `pq<=((k-1)/2)^2`, giving (5.3). Globally `p=q=m`, giving (5.4). Finally `\mathcal E_3(S)>=c` implies `pq>= c^{1/2}m^2`, while `p+q>=2\sqrt{pq}`, giving (5.5). ∎

## 6. Principal triples see only a vanishing diagonal slice

For the same family, a principal `3x3` determinant is nonzero only for a triple consisting of the singleton, one positive-bank coordinate and one negative-bank coordinate. Every such determinant has magnitude `m^{-2}`. Therefore

\[
\boxed{
\max_{|I|=3}|\det A_{m;I,I}|=m^{-2},
}
\tag{6.1}
\]

and

\[
\boxed{
\sum_{|I|=3}|\det A_{m;I,I}|^2=m^{-2},
}
\tag{6.2}
\]

whereas the full mixed-minor mass is one. The ratio between full exterior mass and principal exterior mass is exactly `m^2`.

Applying the completed fleet03/B14 determinant theorem to the best physical triple therefore produces the certificate

\[
32\sqrt{10}\,(m^{-2})^{-1/3}
=32\sqrt{10}\,m^{2/3},
\tag{6.3}
\]

which diverges with `m`.

This remains true after *arbitrary law localization*. Indeed, suppose the input product law is decomposed into positive subprobability pieces of masses `w_alpha`, and on each piece one adaptively chooses any physical triple `I_alpha` before invoking the determinant theorem. Since the matrix is unchanged by law localization, every usable triple still has determinant at most `m^{-2}`. The mass-linear recombination cost furnished by this certificate is therefore at least

\[
\sum_\alpha w_\alpha\,32\sqrt{10}\,m^{2/3}
=32\sqrt{10}\,m^{2/3}.
\tag{6.4}
\]

This is a counterexample to the *proof mechanism* “localize the laws as finely as desired, then pick one determinant-certified physical triple on each piece.” It is not a counterexample to QFORM.

## 7. Interpretation: localization cannot repair matrix localization

The obstruction is exact:

1. unbounded supports, arbitrary translations and distant fragments can be removed from the outside coordinates at zero cost by Theorem 1;
2. however, conditioning coordinates also deletes mixed quadratic curvature crossing the conditioning boundary;
3. on `A_m`, all but `m^{-2}` of the unit exterior-volume bank is off the principal diagonal `I=J`;
4. no bounded active coordinate set captures a positive fraction of that bank;
5. therefore a full proof must aggregate the diffuse positive/negative banks *before* reciprocal determinant payment or before conditioning reduces them to affine shifts.

This sharply separates two notions of localization that were previously easy to conflate: **law localization is safe when mass-linear**, while **matrix localization to a bounded physical coordinate set is not target-preserving**.

## 8. First unpaid implication after this run

A viable full-target bridge must exploit the global identity

\[
\|\wedge^3 A\|_{HS}^2\ge1
\]

without first selecting one bounded-size physical block. Concretely, one needs either:

- a grouped-coordinate/product-preserving shell estimate whose constant depends on an aggregate exterior-volume quantity before inversion; or
- an aggregate coarea/Fourier inequality that sums the mixed minors at the `\ell_2` level and only then pays a reciprocal curvature factor.

Any argument that first reduces to a uniformly bounded number of original coordinates cannot derive its nondegeneracy solely from the three-large-eigenvalue hypothesis, by Theorem 2.

## 9. Sanity check

Direct finite-dimensional enumeration for `m=2,3,4` verifies

- spectrum `\{1,1,-1,0,\ldots,0\}`;
- global mixed third-minor square sum exactly `1` (up to floating roundoff);
- principal third-minor square sum exactly `m^{-2}`;
- the active-set formula (5.2) on sample subsets.

The proof itself is exact and does not depend on this computation.

## 10. Scope

This report does **not** prove the full conjecture and does not claim a universal bounded-density theorem from exterior volume alone. It proves a target-level localization interface and a rigorous obstruction showing why a bounded physical active set cannot preserve the spectral nondegeneracy in general. It uses only original-coordinate independence, exact matrix identities, and the stated completed partner theorem.
