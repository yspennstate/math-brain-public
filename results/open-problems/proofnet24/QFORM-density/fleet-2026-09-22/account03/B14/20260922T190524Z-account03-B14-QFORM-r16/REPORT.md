# account03/B14 — determinant-only physical-triple localization theorem

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T190524Z-account03-B14-QFORM-r16`  
**Assignment:** translations and localization  
**Startup control:** `yspennstate/math-research-brain@7ed828180d96d58c9d4048b479c2ec534303470b`  
**Pre-publication control refresh:** `yspennstate/math-research-brain@ee9d00b72aec45d9b3df87b6018ab907463093af`  
**Owner control at refresh:** `2026-09-22.12`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** proved supporting target-level theorem; full QFORM remains OPEN. Continuity is not proved.

## 1. Main result

This run proves a product-structure-valid replacement for the localized three-coordinate regime without using the refuted arbitrary-joint coarea lemma.

### Theorem A — `QFORM-PRINCIPAL-TRIPLE-DETERMINANT-LOCALIZATION-v1`

Let `A` be any real symmetric `n x n` matrix. Let `X_1,...,X_n` be independent real random variables with probability densities bounded by one. Suppose there is an ORIGINAL-coordinate triple `I={i,j,k}` whose principal block

\[
B=A_{I,I}
\]

is nonsingular, and put

\[
\delta=|\det B|>0.
\]

Then the law of `Q=X^TAX` has an essentially bounded density and

\[
\boxed{\|p_Q\|_\infty\le 32\sqrt{10}\,\delta^{-1/3}.}
\]

The same bound holds for `X^TAX+b^TX+c` with an arbitrary deterministic affine perturbation.

No hypothesis on any other eigenvalue of `A` is required. In particular all additional eigenvalues, signs, outside quadratic coefficients and cross-couplings are arbitrary. No moment, compact-support, connected-support, log-concavity, smoothness, fragment-count, support-diameter or support-location hypothesis is used.

### Corollary B — rigorous localized regime

If an ORIGINAL-coordinate `3 x 3` principal block has all three eigenvalue magnitudes at least `c>0`, then

\[
|\det B|\ge c^3,
\]

and therefore

\[
\boxed{\|p_Q\|_\infty\le 32\sqrt{10}/c.}
\]

Thus the localized regime suggested in the latest owner message is valid, but its proof must retain the original-coordinate product structure. The refuted arbitrary-joint rank-three coarea assertion is not used. The determinant condition in Theorem A is strictly weaker than requiring each of the three block eigenvalues to be at least `c`.

For the full target, if some principal triple has `|det B|>=1`, this branch closes with the universal numerical constant

\[
32\sqrt{10}=101.192885125388\ldots.
\]

The remaining full-target obstruction is structural: the bare hypothesis that `A` has three eigenvalues of absolute value at least one does not force a dimension-independent lower bound on one physical principal-triple determinant. Diffuse/bank families can spread the determinant mass among many coordinates.

## 2. Localization and translations cost zero

Condition on all coordinates outside `I`. Since the inputs are independent ORIGINAL coordinates, the three active variables remain independent with their original cap-one marginal densities. The conditional polynomial is

\[
q_z(x)=x^TBx+\ell(z)^Tx+c(z).
\]

Because `B` is invertible, every affine vector `ell(z)` belongs to `Ran(B)=R^3`. The completed partner theorem account04/B14, `QFORM-CENTERED-AFFINE-LOCALIZATION-EQUIVALENCE-v1`, gives exact constant-preserving reduction of this cap-one affine problem to centered compact finite-fragment product inputs, with no support-diameter, fragment-count, separation or tail tax. Its canonical source is

`yspennstate/math-open-problems@1250c776b3840b8494ace461b27541f8e156e9bf:proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260922T182134Z-account04-B14-centered-affine-r3/REPORT.md`.

Consequently it is enough to establish a bound uniform in the affine vector and the localized supports. The proof below in fact works directly for arbitrary cap-one laws, so this partner theorem is applied as an exact no-loss localization/translation transfer rather than as an extra hypothesis.

## 3. Two completed analytic inputs

The proof uses two current completed supporting estimates.

### Input 1: orientation-free rank-two half-Riesz estimate

For independent cap-one coordinates `Y=(Y_1,Y_2)`, every invertible symmetric `2 x 2` matrix `N`, every affine vector `u`, and every `w`,

\[
\mathbb E\,|Y^TNY+u^TY-w|^{-1/2}
\le 16\sqrt{30}\,|\det N|^{-1/4}.
\]

The sharper constant applies because in two physical dimensions `N` is invertible, hence every affine vector lies in `Ran(N)`. This is the range-compatible case of `QFORM-RANK2-AFFINE-HALF-RIESZ-v1`, canonical source

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a:proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

### Input 2: indefinite physical-pair logarithmic smoothing

For an invertible indefinite physical pair `C`, set `D=|det C|` and `kappa=sigma_min(C)`. If after completing this pair the remaining random scalar `R` satisfies

\[
\sup_t\Pr\{|R-t|<\rho\}\le H\sqrt\rho,
\]

then

\[
\|p_Q\|_\infty\le4\sqrt{2H}\,(D\kappa)^{-1/4}.
\]

This is equation (1.3) of `QFORM-PAIR-LOG-SMALLBALL-SMOOTHING-v1`, canonical source

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f:proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

For a one-dimensional remainder `R=rZ^2+sZ+d` with `Z` cap one, the rank-one affine small-ball lemma in the rank-two-fusion report gives

\[
\sup_t\Pr\{|R-t|<\rho\}\le10\sqrt{\rho/|r|},
\]

so `H=10/sqrt(|r|)`.

Both inputs retain arbitrary affine perturbations and use original-coordinate independence only.

## 4. A determinant-normalized matrix dichotomy

Write the physical block as

\[
B=\begin{pmatrix}
d_1&a&b\\
a&d_2&c\\
b&c&d_3
\end{pmatrix},
\qquad \delta=|\det B|.
\]

Set

\[
\tau=\frac9{16}.
\]

We split according to the largest physical diagonal.

### Branch S: a scalar pivot is large

Assume

\[
\max_i|d_i|\ge\tau\delta^{1/3}.
\]

Choose such an index and reorder it first. Write

\[
B=\begin{pmatrix}d&v^T\\v&C\end{pmatrix},
\qquad d\ne0,
\]

and let

\[
N=C-vv^T/d
\]

be the `2 x 2` Schur complement. Since `B` is invertible,

\[
\det N=\frac{\det B}{d}\ne0.
\]

Conditioning outside the triple only adds affine terms. Conditional on the two remaining active coordinates, the first active coordinate appears as a translated scalar square with coefficient `d`, and its cap-one density implies the standard square kernel bound

\[
p_{q_z}(t)\le |d|^{-1/2}
\mathbb E|t-(Y^TNY+u^TY+s)|^{-1/2}.
\]

Input 1 therefore yields

\[
\|p_{q_z}\|_\infty
\le16\sqrt{30}\,|d|^{-1/2}|\det N|^{-1/4}
=16\sqrt{30}\,|d|^{-1/4}\delta^{-1/4}.
\]

Using `|d|>=tau delta^(1/3)` gives

\[
\|p_{q_z}\|_\infty
\le16\sqrt{30}\,\tau^{-1/4}\delta^{-1/3}.
\]

Because

\[
\tau^{-1/4}=(16/9)^{1/4}=2/\sqrt3,
\]

we obtain exactly

\[
\boxed{\|p_{q_z}\|_\infty\le32\sqrt{10}\,\delta^{-1/3}.}
\]

The bound is uniform in the outside realization `z`.

### Branch P: all scalar pivots are small, hence an indefinite pair is quantitative

Assume now

\[
|d_i|<\tau\delta^{1/3}\qquad(i=1,2,3).
\]

Let

\[
m=\max\{|a|,|b|,|c|\}.
\]

By AM-GM on the three singular values of `B`,

\[
\|B\|_F^2\ge3\delta^{2/3}.
\]

On the other hand,

\[
\|B\|_F^2=d_1^2+d_2^2+d_3^2+2(a^2+b^2+c^2)
<3\tau^2\delta^{2/3}+6m^2.
\]

Hence

\[
m^2>\frac{1-\tau^2}{2}\delta^{2/3}
=\frac{175}{512}\delta^{2/3},
\]

so

\[
m>\frac{5\sqrt{14}}{32}\delta^{1/3}.
\]

Choose the physical pair containing the off-diagonal coefficient of magnitude `m`; call its principal matrix `C_2`. Its diagonal entries both have magnitude less than `tau delta^(1/3)`. Therefore

\[
m^2>|d_id_j|,
\]

because `175/512>81/256=162/512`. Thus

\[
\det C_2=d_id_j-m^2<0,
\]

so `C_2` is invertible and indefinite.

Compare `C_2` to the zero-diagonal matrix with off-diagonal entries `m`. Weyl's singular-value inequality gives

\[
\kappa:=\sigma_{\min}(C_2)
\ge m-\max(|d_i|,|d_j|)
>\kappa_0\delta^{1/3},
\]

where

\[
\kappa_0=\frac{5\sqrt{14}-18}{32}>0.
\]

Now condition on every coordinate outside the selected physical triple. Complete the pair `C_2` inside the resulting three-variable quadratic. The remaining scalar quadratic coefficient is the scalar Schur complement

\[
r=d_k-e^TC_2^{-1}e.
\]

The determinant identity is exact:

\[
\det B=(\det C_2)r.
\]

Writing `D=|det C_2|`, this gives

\[
D|r|=\delta.
\]

The third active coordinate is independent of the selected pair and retains a cap-one density. Therefore the one-dimensional rank-one affine small-ball bound gives `H=10/sqrt(|r|)`. Input 2 now yields

\[
\begin{aligned}
\|p_{q_z}\|_\infty
&\le4\sqrt{2H}(D\kappa)^{-1/4}\\
&=8\sqrt5\,(D\kappa|r|)^{-1/4}\\
&=8\sqrt5\,(\delta\kappa)^{-1/4}\\
&<8\sqrt5\,\kappa_0^{-1/4}\delta^{-1/3}.
\end{aligned}
\]

Numerically,

\[
8\sqrt5\,\kappa_0^{-1/4}=46.3778035026\ldots,
\]

well below `32 sqrt(10)`. A purely exact comparison is also immediate: `kappa_0>1/1024`, so

\[
8\sqrt5\,\kappa_0^{-1/4}<8\sqrt5\,(1024)^{1/4}=32\sqrt{10}.
\]

Thus Branch P satisfies the same displayed theorem constant.

## 5. Completion of Theorem A

For almost every outside realization `z`, Branch S or Branch P gives

\[
\Pr\{q_z(X_I)\in J\}\le32\sqrt{10}\,\delta^{-1/3}|J|
\]

for every interval `J`. The constant is independent of `z`, every induced affine coefficient, support location, support diameter, fragment number and fragment separation. Averaging over the outside coordinates proves the same small-ball inequality for the full form. Hence the output law is absolutely continuous with

\[
\|p_Q\|_\infty\le32\sqrt{10}\,\delta^{-1/3}.
\]

The same conditioning argument proves the claim with an arbitrary deterministic affine perturbation.

This proof is product-safe: no spectral rotation of the input variables is made. Orthogonal diagonalization appears only inside already-proved analytic inputs where it acts on Lebesgue geometry/Fourier variables rather than declaring transformed random coordinates independent.

## 6. Why this matters for the live full proof

The newest owner-message source describes a localized regime through a three-dimensional coarea assertion. CURRENT_RESEARCH simultaneously records a source-valid correction showing that the proposed arbitrary-joint coarea inequality is false. Theorem A provides a corrected product-preserving route to the localized conclusion:

> a quantitatively nonsingular physical principal triple is enough, and in fact a determinant lower bound alone is enough.

No conditional joint-density cap is invoked.

The full theorem is still not closed because the global three-large-eigenvalue hypothesis can be highly delocalized in the physical coordinates. The next structural target can now be stated more sharply:

> either produce one physical triple with `|det A_{I,I}|>=c_0` for a universal `c_0>0`, in which case Theorem A closes the form immediately, or use a genuinely mass-linear/grouped mechanism that aggregates many small principal-triple determinants before paying inverse determinant cost.

The known singleton-plus-bank and diffuse examples show why a naive maximum-single-minor reduction is not enough. This report does not claim the first alternative always occurs.

## 7. Partner result actually applied

The requested partner was account04/B14. Its completed `QFORM-CENTERED-AFFINE-LOCALIZATION-EQUIVALENCE-v1` was read from the canonical report at commit `1250c776b3840b8494ace461b27541f8e156e9bf` and applied here as follows.

For every outside realization, `B` is invertible, so the induced affine vector is range-compatible. The partner theorem identifies the optimal cap-one small-ball constant for the arbitrary unbounded translated three-coordinate problem with the corresponding centered compact finite-fragment affine problem. The bound proved in Sections 4--5 is independent of every fragment parameter, so the exact same constant transfers back to arbitrary shifts, distant fragments and unbounded supports. This is an equality-of-constants application, not merely a citation.

## 8. Corrections respected

This report does not use:

- the refuted arbitrary-joint `||rho||_infinity^(2/3)` coarea inequality;
- the refuted positive conditional-projection-density moment;
- pointwise van-der-Corput decay for arbitrary cap-one densities;
- independence after spectral rotation;
- a bounded support diameter or fixed fragment count;
- Gaussian, log-concave, moment, centered-law or connected-support assumptions;
- Monte Carlo histograms as proof.

The full conjecture remains OPEN.

## 9. Continuity

The theorem proves existence of an essentially bounded density. It does not prove a continuous representative for arbitrary measurable cap-one input densities. Continuity remains a separate open conclusion.

## 10. Diagnostic computation

`CHECK.py` verifies the exact threshold identities, evaluates the constants, and checks the `det B = det(C_2) * r` Schur identity on 10,000 deterministic pseudorandom nonsingular indefinite-pair examples. Its output is recorded in `CHECK_OUTPUT.txt`. These computations are diagnostics only; the universal proof is the algebra above.
