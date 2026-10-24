# account04/B18 — sharp capped-basis payment for the equal-split Schur core

Run: `20260923T032213Z-account04-B18-QFORM-r2`

Status: `ESSENTIAL_STEP_APPLIED / SUPPORTING TARGET BRANCH PROVED / FULL QFORM OPEN`.

## 1. Exact target and sources

The owner target remains the unrestricted statement for independent real original-coordinate variables with density caps at most one and arbitrary symmetric matrices with at least three eigenvalues of modulus at least one. Continuity is separate.

This note applies account01/B18's completed `QFORM-FRESNEL-CAPPED-BASIS-WEIGHTS-v1` at scientific commits `4c81bbf59005c3f527e9139f55c078f6817b3dad` and `1f269a8ae64baa9401910aec1f14251128537afd`. Its analytic inputs are Beckner's sharp Hausdorff--Young theorem and the Gaussian-exhaustion form of Brascamp--Lieb due to Lieb and Bennett--Carbery--Christ--Tao. Their actual gates are exactly those used here: an original-coordinate product density, an admissible random law on full bases, and basis marginals at most one half. No independence is asserted after projection.

The source packet begins at `e5f71d79eff325201dd0274053d20268ce65b837`; later Claude-review corrections are retained. The earlier account04/B18 balanced-bank theorem is at `46b0ba122327714fe17f3d14bfd615fd029b1034`.

## 2. Live equal-split Schur-isotropic packet

Consider the exact-rank-three core

\[
Q=(Y+uX_0)^T D(Y+uX_0),\qquad Y=V^T X_{\rm res},
\]

where `X_0` and all residual coordinates are independent and cap one, `V^TV=I_3`, `D` is invertible symmetric, and `u^TDu=0`. Put `r=||u||`,

\[
L=[u,V^T],\qquad G=LL^T=I+uu^T.
\]

Assume the residual physical rows split into two disjoint original-coordinate banks with Grams

\[
\sum_{i\in I_0}v_iv_i^T=\frac12I_3,
\qquad
\sum_{j\in J}v_jv_j^T=\frac12I_3.
\tag{2.1}
\]

The previous full-bank theorem paid this packet, but with a larger determinant-bank constant. The capped-basis theorem pays the entire full-volume law directly when `0<r<=1`.

## 3. Full-volume basis law and exact gates

Let `Omega` be the determinant-squared volume-sampling law on all three-element physical bases of `L`. Cauchy--Binet gives its score

\[
Z_\Omega=\sum_{|S|=3}\det(L_S)^2=\det G=1+r^2.
\tag{3.1}
\]

Its coordinate marginals are the leverage scores

\[
p_k=\ell_k^TG^{-1}\ell_k,
\qquad \sum_kp_k=3.
\tag{3.2}
\]

For the special column `u`, Sherman--Morrison gives

\[
p_0=u^T(I+uu^T)^{-1}u=\frac{r^2}{1+r^2}=:\beta.
\tag{3.3}
\]

Hence `p_0<=1/2` exactly when `r<=1`.

For every residual row, `G^{-1}<=I`, while (2.1) implies `v_kv_k^T<=(1/2)I` and therefore `||v_k||^2<=1/2`. Consequently

\[
p_k=v_k^TG^{-1}v_k\le ||v_k||^2\le\frac12.
\tag{3.4}
\]

Thus every marginal gate in account01/B18 is verified for `0<r<=1`, using only original-coordinate provenance.

## 4. Exact capped-basis factor

Account01/B18 gives

\[
||p_Q||_\infty
\le3B_p^{2/3}(|\det D|Z_\Omega)^{-1/3},
\qquad
B_p=\prod_k(1-p_k)^{-(1-p_k)/2},
\tag{4.1}
\]

and a continuous density.

Because `A=L^TDL` has exactly three nonzero eigenvalues,

\[
|\operatorname{pdet}A|=|\det D|\det G=|\det D|(1+r^2)\ge1,
\tag{4.2}
\]

so the last factor in (4.1) is at most one.

Put `f(x)=-(1-x)log(1-x)/2`. The elementary inequality

\[
-(1-x)\log(1-x)\le x\qquad(0\le x<1)
\tag{4.3}
\]

gives `f(x)<=x/2`. Keeping the special leverage exactly and using `sum_{k ne0}p_k=3-beta`,

\[
\log B_p
=f(\beta)+\sum_{k\ne0}f(p_k)
\le -\frac{1-\beta}{2}\log(1-\beta)+\frac{3-\beta}{2}.
\tag{4.4}
\]

Substitution into (4.1) proves the new target-level theorem

### `QFORM-EQUAL-SPLIT-FULL-BASIS-CAP-v1`

For every packet above with `0<r<=1`, `Q` has a continuous density and

\[
\boxed{
||p_Q||_\infty
\le 3\exp\!\left(\frac{3-\beta}{3}\right)
(1-\beta)^{-(1-\beta)/3},
\qquad \beta=\frac{r^2}{1+r^2}.
}
\tag{4.5}
\]

The logarithmic derivative of the factor after `3` is `log(1-beta)/3<=0`. Therefore

\[
\boxed{||p_Q||_\infty\le3e=8.154845485\ldots}
\tag{4.6}
\]

uniformly for `0<r<=1`. At the endpoint `r=1` (`beta=1/2`),

\[
\boxed{||p_Q||_\infty
\le3e^{5/6}2^{1/6}=7.748274335\ldots .}
\tag{4.7}
\]

This is an actual application of the completed account01/B18 theorem to a previously live Schur-isotropic matrix class. It improves the earlier full-bank estimate on this equal-split subfamily and supplies continuity from the Fourier route itself.

## 5. Precise boundary

The new full-volume law ceases to be admissible at `r>1` because the special-coordinate marginal `beta` exceeds one half. A mixed basis law can restore the marginal gate, but its score loses the cancellation in (4.2) and again grows with shear. The current result therefore does not close extreme shear, arbitrary mixed frames without (2.1), or additional spectrum.

The first remaining structural implication is unchanged in kind but narrower in this packet: when `r>1`, construct a product-valid basis mixture whose entropy factor and score jointly remain universal, or route the special-coordinate concentration to an already-paid null-pivot/ridge/hub branch. The full conjecture remains open.

## 6. Primary-source gate ledger

- Beckner, *Inequalities in Fourier analysis*, Annals of Mathematics 102 (1975), 159--182: sharp Hausdorff--Young constants used in the capped-basis Fourier estimate.
- Lieb, *Gaussian kernels have only Gaussian maximizers*, Inventiones Mathematicae 102 (1990), 179--208: Gaussian extremization for the Brascamp--Lieb integral.
- Bennett--Carbery--Christ--Tao, *The Brascamp--Lieb inequalities: finiteness, structure and extremals*, GAFA 17 (2008), 1343--1415: finiteness/critical-subspace framework used for Gaussian exhaustion.
- Livshyts--Paouris--Pivovarov, arXiv:1507.07949 / Israel J. Math. 216 (2016), 877--889: sharp product marginal theorem used elsewhere in the same transfer programme; it is not silently upgraded here to independence of projected coordinates.

No search miss is used as a novelty claim. Repository transport is not verified native ingestion; model and hidden reasoning metadata remain unknown.
