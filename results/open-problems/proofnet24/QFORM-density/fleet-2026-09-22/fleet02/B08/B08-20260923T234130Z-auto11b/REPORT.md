SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B08, 2026-09-23T23:41:30Z.
attacking: the exact aligned two-bank carrier-plus-diagonal endpoint; upgrade the critical diffuse rank-two Fresnel bound by one ORIGINAL-coordinate diagonal twist before any local Schur inversion.

# fleet02/B08 r30 — diffuse rank-two carrier + diagonal twist via Fresnel/Strichartz

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: diffuse eigenvector case / complementary constructions and source-valid counterexamples  
Status: **NEW SUPPORTING THEOREM + QUANTIFIED HYBRID ROUTER + TARGET-VALID LOCAL-PIVOT OBSTRUCTION / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`

The unrestricted conjecture remains OPEN. The first unpaid implication after this report is

`QFORM-NEARRANK1-ALIGNED-TWIST-LOCALIZED-COMPILER-v1`:

> in the exact aligned state, consume the chamber where the two-dimensional common-plane carrier has very small second spectral volume and the large physical diagonal twist lies on an arm-heavy coordinate or survives the rank-one limit without the near-cancellation hypothesis of fleet03/B08 r47. The proof must retain arbitrary product sources, arbitrary hub curvature and affine terms, and may not treat a small matrix remainder as a small random quadratic perturbation.

The point of the present run is that a **genuinely rank-two diffuse carrier no longer needs a well-conditioned physical scalar/pair pivot at all** once one nonzero physical diagonal twist is available on a diffuse carrier row.

## 1. Exact scope and fixed-source input

Condition on any coordinates outside the light bank `I` and on any hub coordinates. This preserves the product law of the remaining ORIGINAL coordinates and produces only arbitrary affine terms. The light quadratic block has the exact form

\[
A_I=D+U\Lambda U^T,
\qquad U^TU=I_2,
\qquad \Lambda=\operatorname{diag}(\lambda_1,\lambda_2),
\tag{1.1}
\]

with `D=diag(d_i)` physical diagonal. Put

\[
c_i=\|U_{i,:}\|_2^2,\qquad P=|\lambda_1\lambda_2|.
\tag{1.2}
\]

The completed Fresnel--Brascamp--Lieb proof in

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`
(and its rank-r formulation in `FOURIER_ROUTE_REPORT.md`) gives, after Fresnel linearisation of the two rank-two squares, a geometric Brascamp--Lieb integral in which each ORIGINAL coordinate enters through

\[
G_i(s,\tau)=\int_{\mathbb R}e^{i(sx^2+\tau x)}f_i(x)\,dx.
\tag{1.3}
\]

For every fixed `s`, the fixed-source twisted Fourier lemma gives

\[
\int_{\mathbb R}|G_i(s,\tau)|^p\,d\tau\le {4\pi\over\sqrt p},
\qquad p\ge2.
\tag{1.4}
\]

In particular, if every `c_i<=1/2`, the source theorem gives the critical rank-two bound

\[
|\phi_Q(t)|\le 4\pi P^{-1/2}|t|^{-1}.
\tag{1.5}
\]

This is a real obstruction: `|t|^{-1}` is not integrable, so the fixed-source absolute-value argument alone does not prove a bounded density in rank two. The new step is to **not spend** (1.4) on one twisted coordinate.

## 2. Main theorem: one diagonal twist upgrades critical rank two

### Theorem `QFORM-RANK2-CARRIER-DIAGONAL-STRICHARTZ-v1`

Assume (1.1), all `c_i<=1/2`, and choose an ORIGINAL coordinate `j` with

\[
0<c_j<1/2,\qquad d_j\ne0.
\tag{2.1}
\]

Set

\[
p_j={1\over c_j},\qquad q_j={4\over1-2c_j},
\tag{2.2}
\]

so `2/q_j+1/p_j=1/2`. Let `S(c_j)` be the finite one-dimensional homogeneous Schrödinger/Strichartz constant in

\[
\left\|\,\|G_j(s,\cdot)\|_{L^{p_j}_\tau}\right\|_{L^{q_j}_s}
\le S(c_j)\|f_j\|_2.
\tag{2.3}
\]

Since `f_j<=1` and `\int f_j=1`, `\|f_j\|_2<=1`. Then the full ambient quadratic form, including all conditioned outside coefficients and arbitrary affine terms, has a continuous `C_0` density and

\[
\boxed{
\|p_Q\|_\infty
\le C_{FS}(c_j)\,
P^{-2/(5-2c_j)}
|d_j|^{-(1-2c_j)/(5-2c_j)},
}
\tag{2.4}
\]

where, writing `q=q_j`,

\[
C_{FS}(c)
={q+1\over\pi}
\left[
{2\pi\over q}
\,{[2(q-1)]^{(q-1)/q}\,S(c)\over(4\pi\sqrt c)^c}
\right]^{q/(q+1)}.
\tag{2.5}
\]

The coefficient powers in (2.4) add to `-1` under the scaling `A -> L A`.

Moreover, for `0<c<=1/4`, the admissible Strichartz pairs lie between `(q,p)=(8,4)` and `(4,infinity)`. Interpolating the two standard one-dimensional endpoint estimates gives a finite absolute constant `S_*` with `S(c)<=S_*` throughout this range. A crude uniform consequence is

\[
\boxed{
P\ge p_0L^2,\quad |d_j|\ge d_0L,\quad c_j\le1/4
\Longrightarrow
\|p_Q\|_\infty
\le 12S_*^{8/9}p_0^{-4/9}d_0^{-1/5}L^{-1}.
}
\tag{2.6}
\]

For the explicit gates `P>=L^2/4096` and `|d_j|>=L/128`, (2.6) is `<1277 S_*^{8/9}/L`.

### Proof

The fixed-source Fresnel representation for the rank-two part has prefactor

\[
(4\pi)^{-1}P^{-1/2}|t|^{-1}
\tag{2.7}
\]

and leaves a two-dimensional integral of `\prod_i|G_i(td_i,tb_i+\langle U_{i,:},u\rangle)|`. Geometric Brascamp--Lieb with exponents `c_i` gives

\[
|\phi_Q(t)|
\le 4\pi P^{-1/2}|t|^{-1}h_j(t),
\tag{2.8}
\]

where

\[
h_j(t)
={\|G_j(td_j,\cdot)\|_{p_j}\over(4\pi\sqrt{c_j})^{c_j}}.
\tag{2.9}
\]

Indeed, for every `i!=j`, (1.4) contributes exactly `(4\pi)^{c_i}` after the tight-frame scaling, while the `j`-factor is left unspent. The same fixed-source lemma also shows `0<=h_j(t)<=1`.

By (2.3) and the change of variables `s=td_j`,

\[
\|h_j\|_{L^{q_j}_t}
\le |d_j|^{-1/q_j}
{S(c_j)\over(4\pi\sqrt{c_j})^{c_j}}.
\tag{2.10}
\]

For any `T>0`, use `|\phi|<=1` on `|t|<=T` and Hölder on the tail. Since the conjugate exponent is `q/(q-1)`,

\[
\int_{|t|>T}|t|^{-1}h_j(t)\,dt
\le
[2(q-1)]^{(q-1)/q}T^{-1/q}\|h_j\|_q.
\tag{2.11}
\]

Thus

\[
\int_{\mathbb R}|\phi_Q(t)|dt
\le2T+D T^{-1/q},
\tag{2.12}
\]

with

\[
D=4\pi P^{-1/2}[2(q-1)]^{(q-1)/q}
|d_j|^{-1/q}{S(c_j)\over(4\pi\sqrt{c_j})^{c_j}}.
\tag{2.13}
\]

The minimiser is `T=(D/(2q))^{q/(q+1)}`. Fourier inversion gives `(2\pi)^{-1}\int|\phi|`, and substitution yields exactly (2.4)-(2.5). The integrable characteristic-function majorant also gives a continuous `C_0` density. No stochastic rotation was used. QED.

## 3. Exact aligned-state router

Return to the B08 aligned normal form

\[
A=\begin{pmatrix}B&M\\M^T&M^TRM+D\end{pmatrix},
\qquad D=\operatorname{diag}(d_1,\dots,d_m),
\tag{3.1}
\]

where `B,R` are arbitrary symmetric `2x2` matrices and `M` has row rank two. If `R` is invertible, the nonzero rank-two carrier `M^TRM` has column space `row(M)`. Hence its physical spectral leverage is exactly

\[
\ell_j=m_j^T(MM^T)^{-1}m_j,
\tag{3.2}
\]

and the product of its two nonzero eigenvalues in modulus is

\[
\boxed{P=|\det R|\det(MM^T).}
\tag{3.3}
\]

Therefore, at target scale `L`, the actual gate

\[
\max_j\ell_j\le1/4,\qquad
|\det R|\det(MM^T)\ge L^2/4096,\qquad
\|D\|_{op}\ge L/128
\tag{3.4}
\]

implies the universal `O(L^{-1})` estimate (2.6), with **no condition at all on the physical scalar pivot** `a_j=d_j+m_j^TRm_j`. In particular exact or near cancellation of that pivot is harmless in the genuinely rank-two carrier chamber.

Combine this with the newest fleet03/B08 small-twist result `QFORM-EXACTMATCH-SMALLTWIST-RIDGE-LOCALIZED-v1`: if instead `\|D\|_{op}<=L/128`, then either

\[
\boxed{\|p_Q\|_\infty<64/L}
\tag{3.5}
\]

with continuous density, or the actual spectral-window projection `1_{|A|>=L/64}` has a physical diagonal entry `>1/32`, hence an actual localized coordinate star at scale `L/(256\sqrt2)`.

Consequently, in the exact aligned state with diffuse arm leverage `<=1/4`, the remaining large-twist chamber is forced into the **near-rank-one carrier gate**

\[
\boxed{|\det R|\det(MM^T)<L^2/4096}
\tag{3.6}
\]

unless it is already paid by (2.6). If the arm itself violates the `1/4` leverage gate, an actual original coordinate already carries `>1/4` of the two-dimensional arm projection mass. This is the promised explicit localized/diffuse split.

## 4. Newest partner result applied at the singular endpoint

The latest compatible fleet03/B08 result is

`yspennstate/math-open-problems@41a02a4ecaa02ccfa4029ca3fd323afe5e886144`,
Theorem `QFORM-RANK1-ALIGNED-CANCELLED-TWIST-SHEAR-v1`.

In the exact rank-one carrier state `R=lambda rr^T`, if `max ell_j<=1/3`, a physical twist `d_j` is near-cancelled in the actual diagonal

\[
a_j=d_j+\lambda w_j^2,\qquad |a_j|\le\theta|d_j|<|d_j|,
\tag{4.1}
\]

then a product-safe triangular shear creates two genuine hubs and gives

\[
\boxed{
\|p_Q\|_\infty
\le4(1-\theta)^{-1/4}(|d_j|s_2(M))^{-1/2},
\qquad p_Q\in C_0.
}
\tag{4.2}
\]

Apply it to the target-valid partner stress family with `s_2(M)=L`, every arm leverage `1/3`, `d_1=-L/3`, and exact cancellation `a_1=0`. Then

\[
\boxed{\|p_Q\|_\infty\le4\sqrt3/L<6.929/L.}
\tag{4.3}
\]

Thus the new rank-two Strichartz compiler and the partner rank-one shear compiler meet on opposite sides of the carrier-rank transition: the remaining debt is not generic diagonal twisting, but the quantitatively near-rank-one / localized transition described after (3.6).

## 5. Target-valid diffuse stress family: every physical pair is weak

Let `m=2048` and let `U` be the first two normalized Sylvester-Hadamard columns in `R^m`. Then `U^TU=I_2` and every row leverage is

\[
c_i=2/m.
\tag{5.1}
\]

Set

\[
A_m=4L(UU^T+e_1e_1^T).
\tag{5.2}
\]

The nonzero eigenvalues are exactly

\[
4L(1-\sqrt{2/m}),\qquad4L,\qquad4L(1+\sqrt{2/m}),
\tag{5.3}
\]

so this is a genuine target matrix (indeed all three exceed `L`). Yet every physical `2x2` principal block is below the preceding `L/64` conditioning gate. If neither index is `1`, its operator norm is at most

\[
16L/m=L/128.
\tag{5.4}
\]

For a pair `{1,j}`, testing the second basis vector gives

\[
\sigma_{min}\le\sqrt{A_{1j}^2+A_{jj}^2}
\le8\sqrt2L/m
=0.0055243\ldots L<L/64.
\tag{5.5}
\]

So no proof can force the new physical-pair `L/64` gate on this diffuse target family.

For the same family, however, the rank-two carrier has `P=16L^2`, the physical twist has `d_1=4L`, and `c_1=2/m`. The theorem above gives

\[
\boxed{
\|p_{X^TA_mX}\|_\infty
<1.680\,S(2/m)^{0.800313}/L,
\qquad p_Q\in C_0.
}
\tag{5.6}
\]

The deterministic checker reproduces the eigenvalues, pair-gate failures, exponents and the coefficient `1.679157777...` and terminates `QFORM_B08_R30_CHECK_PASS`.

This is also the required fixed-source application to a real obstruction: on (5.2), the completed rank-two Fresnel--Brascamp--Lieb calculation gives exactly the critical envelope

\[
\boxed{|\phi_Q(t)|\le\min(1,\pi/(L|t|)).}
\tag{5.7}
\]

The logarithmic divergence of the absolute integral is genuine at the level of that source theorem. Retaining the one ORIGINAL diagonal twist instead of spending its twisted Fourier norm upgrades (5.7) to the integrable estimate (5.6).

## 6. Remaining hybrid, quantified

After the r29 exact-alignment router, the r45 small-twist ridge router, the theorem of this report, and the newest r47 rank-one shear receiver, an unpaid aligned diffuse state must exhibit at least one of the following concrete defects:

1. **arm localization:** `max_j ell_j>1/4`;
2. **spectral-window localization:** the `|A|>=L/64` projection has a diagonal entry `>1/32` on the small-twist branch;
3. **near-rank-one carrier:** `|det R| det(MM^T)<L^2/4096` on the large-twist branch;
4. in the exact rank-one limit with a near-cancelled large twist, the partner payment can fail only through its stated anisotropy/scale gates, notably small `s_2(M)` or loss of the large-twist threshold.

No moment, bounded-support, log-concavity, iid, diagonal-basis, or post-rotation independence assumption has entered. Small operator errors have not been discarded as random errors. Continuity is asserted only on the explicit Fourier/partner paid branches above.
