# account01/B18 r27 — Tropp-Chernoff transfer sharpens and enlarges the diffuse Schur-isotropic branch

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** literature-to-proof transfer; designated partner `account02/B18`  
**Status:** PROVED SUPPORTING TARGET-LEVEL SHARPENING / PARTNER RESULT APPLIED. Full QFORM remains OPEN.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact setting consumed from account02/B18 r26

The completed partner theorem works in the exact-rank-three Schur-isotropic representation

\[
Q=(Y+r nX_0)^T D(Y+r nX_0),\qquad Y=V^T X_R,
\]

where `V^T V=I_3`, `||n||=1`, `n^T Dn=0`, the residual rows are `v_j\in R^3`, and

\[
\delta:=\max_j\|v_j\|_2^2.
\]

For a residual partition `S\sqcup T`, write

\[
G_S=\sum_{j\in S}v_jv_j^T,\qquad G_T=\sum_{j\in T}v_jv_j^T=I-G_S.
\]

The partner's source-pinned Theorem D gives, whenever the row-side volume-sampling marginals satisfy `alpha_j<=1/2`,

\[
\|p_Q\|_\infty\le 6\sqrt e\, Z^{-1/6}.
\]

If `G_S,G_T\succeq cI`, then

\[
\alpha_j=v_j^TG_S^{-1}v_j\le \delta/c,
\]

and the exact determinant ledger in the partner report gives

\[
Z\ge |\det D|^2 c^6(1+r^2).
\]

Hence, provided `delta/c<=1/2`,

\[
\|p_Q\|_\infty
\le \frac{6\sqrt e}{c}|\det D|^{-1/3}(1+r^2)^{-1/6}.
\tag{1.1}
\]

Under the target spectral normalization `|lambda_i|>=s` for the three nonzero eigenvalues, the partner ledger gives

\[
|\det D|\ge \frac{s^3}{1+r^2},
\]

so (1.1) becomes

\[
\boxed{\|p_Q\|_\infty\le \frac{6\sqrt e}{sc}(1+r^2)^{1/6}.}
\tag{1.2}
\]

The only input to improve is therefore the deterministic existence of a residual partition with a better lower spectral floor `c`.

## 2. Primary literature transfer: Tropp matrix Chernoff

Tropp, *User-Friendly Tail Bounds for Sums of Random Matrices*, Found. Comput. Math. 12 (2012), Theorem 1.1, states the following. If independent PSD self-adjoint matrices `X_k` satisfy `lambda_max(X_k)<=R` almost surely, and

\[
\mu_{\min}=\lambda_{\min}\!\left(\sum_k\mathbb EX_k\right),\qquad
\mu_{\max}=\lambda_{\max}\!\left(\sum_k\mathbb EX_k\right),
\]

then for `0<=eps<=1`,

\[
\Pr\!\left\{\lambda_{\min}\!\left(\sum_kX_k\right)\le(1-\varepsilon)\mu_{\min}\right\}
\le d\left[\frac{e^{-\varepsilon}}{(1-\varepsilon)^{1-\varepsilon}}\right]^{\mu_{\min}/R},
\tag{2.1}
\]

and for `eps>=0`,

\[
\Pr\!\left\{\lambda_{\max}\!\left(\sum_kX_k\right)\ge(1+\varepsilon)\mu_{\max}\right\}
\le d\left[\frac{e^{\varepsilon}}{(1+\varepsilon)^{1+\varepsilon}}\right]^{\mu_{\max}/R}.
\tag{2.2}
\]

All hypotheses match here with no probabilistic assumptions on the QFORM source laws: choose independent Bernoulli `xi_j~Bernoulli(1/2)` only as an auxiliary partition device and set

\[
X_j=\xi_j v_jv_j^T.
\]

Then `d=3`, `R=delta`, and, because `sum_j v_jv_j^T=I_3`,

\[
\sum_j\mathbb EX_j=\frac12I_3,
\qquad \mu_{\min}=\mu_{\max}=\frac12.
\]

Let `G=\sum_jX_j=G_S`. Since `G_T=I-G`, the event `G_T\not\succeq cI` is the event `lambda_max(G)>(1-c)`. Taking

\[
c=\frac{1-\varepsilon}{2}
\]

and applying (2.1)-(2.2) plus the union bound gives

\[
\Pr\{G_S\not\succeq cI\text{ or }G_T\not\succeq cI\}
\le F(\varepsilon,\delta),
\tag{2.3}
\]
where
\[
F(\varepsilon,\delta):=
3\left[\frac{e^{-\varepsilon}}{(1-\varepsilon)^{1-\varepsilon}}\right]^{1/(2\delta)}
+3\left[\frac{e^{\varepsilon}}{(1+\varepsilon)^{1+\varepsilon}}\right]^{1/(2\delta)}.
\tag{2.4}
\]
Therefore **whenever `F(eps,delta)<1` there exists a deterministic partition** with both Gram matrices at least `cI`.

This is a direct existence transfer from the primary theorem; no QFORM random variable has been randomized or altered.

## 3. New clean threshold: delta <= 1/14

Take

\[
\varepsilon=\frac57,\qquad c=\frac17.
\]

If `delta<=1/14`, then `1/(2delta)>=7`; both bases in (2.4) are in `(0,1)`, hence the worst case is `delta=1/14`. At that endpoint,

\[
F\!\left(\frac57,\frac1{14}\right)
=3\left[\frac{49}{4e^5}+e^5\left(\frac7{12}\right)^{12}\right]
=0.9388059643036212\ldots <1.
\tag{3.1}
\]

Thus there exists a partition with

\[
\boxed{G_S,G_T\succeq \frac17I_3.}
\tag{3.2}
\]

The row marginal gate is exactly respected:

\[
\alpha_j\le\frac{\delta}{c}
\le \frac{1/14}{1/7}=\frac12.
\tag{3.3}
\]

Substitution into the partner inequality (1.2) proves the new target-level branch

\[
\boxed{
\delta\le\frac1{14}
\quad\Longrightarrow\quad
\|p_Q\|_\infty
\le42\sqrt e\,s^{-1}(1+r^2)^{1/6}.
}
\tag{3.4}
\]

Numerically `42 sqrt(e)=69.2462933694...`.

This **strictly enlarges** the partner's previous clean leverage range `delta<=1/18` to `delta<=1/14`.

## 4. Sharper constant on the old delta <= 1/18 range

At the old endpoint `delta<=1/18`, take instead

\[
\varepsilon=\frac58,\qquad c=\frac3{16}.
\]

Again the worst case in (2.4) is `delta=1/18`, where

\[
F\!\left(\frac58,\frac1{18}\right)
=0.9823446394902505\ldots <1.
\tag{4.1}
\]

Thus

\[
G_S,G_T\succeq \frac3{16}I_3,
\qquad
\alpha_j\le \frac{1/18}{3/16}=\frac8{27}<\frac12.
\tag{4.2}
\]

Equation (1.2) now gives

\[
\boxed{
\delta\le\frac1{18}
\quad\Longrightarrow\quad
\|p_Q\|_\infty
\le32\sqrt e\,s^{-1}(1+r^2)^{1/6}.
}
\tag{4.3}
\]

Numerically `32 sqrt(e)=52.7590806624...`. The completed account02/B18 r26 bound on the same branch was `54 sqrt(e) s^{-1}(1+r^2)^{1/6}`. Thus the coefficient is multiplied by

\[
\frac{32}{54}=\frac{16}{27}=0.592592\ldots,
\]

a **40.74% reduction**.

## 5. Actual partner stress-family inequalities

For the partner circular Parseval frame,

\[
v_j=
\left(m^{-1/2},\sqrt{2/m}\cos(2\pi j/m),\sqrt{2/m}\sin(2\pi j/m)\right),
\]

one has `delta=3/m`, and in the normalized stress family the three nonzero physical eigenvalues are exactly `{-1,1,1}`, so `s=1`.

Therefore:

* `m>=42` implies `delta<=1/14`, and the new transfer gives
  \[
  \boxed{\|p_Q\|_\infty\le42\sqrt e\,(1+r^2)^{1/6}.}
  \tag{5.1}
  \]
  The partner r26 theorem required `m>=54`.

* `m>=54` implies `delta<=1/18`, and the sharpened transfer gives
  \[
  \boxed{\|p_Q\|_\infty\le32\sqrt e\,(1+r^2)^{1/6}.}
  \tag{5.2}
  \]
  replacing the partner's `54 sqrt(e)` coefficient.

These are whole-line essential-density estimates for **every independent cap-one source law** in the partner family. No moment, iid, bounded-support, log-concavity, or smoothness hypothesis is added.

## 6. Anti-concentration source audit

I also re-read Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, Theorem 1.1. For a product density `f=prod_i f_i` with `||f_i||_1=1`, it proves the precise orthogonal-marginal bound

\[
\|\pi_E f\|_\infty
\le \min\!\left\{\left(\frac n{n-k}\right)^{(n-k)/2},2^{k/2}\right\}
\prod_i\|f_i\|_\infty^{\gamma_i},
\]

for suitable `gamma_i\in[0,1]`, `sum gamma_i=k`; in particular cap-one products give `||pi_E f||_infty<=2^{k/2}`. This exactly matches the unrestricted cap-one product hypothesis used elsewhere in the QFORM proofnet. It does **not** itself remove the nonplanar shear obstruction here, because the unpaid interface is not merely a marginal-density estimate.

No exact prior theorem found in this targeted search simultaneously has the owner's unrestricted non-iid cap-one source hypothesis and yields the desired universal density bound for arbitrary symmetric quadratic forms from only three spectral eigenvalues. Search absence is **not** being treated as novelty evidence.

## 7. Corrections preserved

This proof does not use any refuted interface. In particular:

- no independence after rotation;
- no arbitrary-joint three-dimensional coarea bound;
- no bounded-conditional-density-as-independence substitution;
- no positive moment of a worst conditional projection cap;
- no law-uniform pointwise Fresnel decay;
- no perturbative deletion of small coefficients;
- no fixed-good-minor, single-row, or exact-two-plane extraction.

The Bernoulli variables in Section 2 exist only to prove a deterministic partition by positive probability. The actual QFORM source remains untouched.

## 8. What remains unpaid

The large-shear exponent remains:

\[
(1+r^2)^{1/6}.
\]

Thus this run enlarges and sharpens the completed partner branch but does **not** solve full QFORM. The next structural debt remains

`QFORM-NONPLANAR-ONEPLUS2-AGGREGATE-v1`:

construct a product-preserving asymmetric `1+2` payment whose determinant sees the full `r^2|det D|` scale, or route the near-coloop survivor into another already-paid branch.

## 9. Continuity ledger

The partner r26 theorem explicitly supplies a whole-line essential `L^infty` density estimate but does **not** assert continuity. The Tropp transfer changes only the partition constants. Therefore this report **does not claim continuity** for (3.4)-(5.2); continuity remains tracked separately.

## 10. Primary sources

1. Joel A. Tropp, *User-Friendly Tail Bounds for Sums of Random Matrices*, Foundations of Computational Mathematics **12** (2012), 389–434, Theorem 1.1 (Matrix Chernoff), DOI `10.1007/s10208-011-9099-z`.
2. Galyna Livshyts, Grigoris Paouris, Peter Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. **216** (2016), 877–889; arXiv:`1507.07949`, Theorem 1.1.
3. Designated partner source: `account02/B18/20260923T081256Z-account02-B18-QFORM-r26/REPORT.md`, commit `b0fe7c60d4fb400917fb53d2435d5262fdcfea97`.

The numerical checks in (3.1), (4.1), and the constants are reproduced in `verify.py` in this immutable run directory.
