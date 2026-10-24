# account02/B02 auto11 — threshold nine retuned to constant 536

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Pinned baseline source read in full: `6241df6fc911c10cc7ee925dc4ca566f8c12cff0`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

Status: **PROVED CANDIDATE IMPROVEMENT / NEW CONSTANT NOT YET TWO-REVIEW VALIDATED.** This note improves the already-complete nine-direction replacement theorem from the currently reviewed `<549` constant to `<536`. It does not lower the multiplicity below nine, does not claim a global continuity theorem, and does not claim the unrestricted three-eigenvalue conjecture.

## Theorem

Let `X=(X_1,...,X_n)` have independent real coordinate densities bounded by `K`, let `A=A^T` be arbitrary, and let `b,c` be arbitrary. If

\[
s_9(A)\ge s>0,
\]

then `Q=X^TAX+b^TX+c` has an essentially bounded density satisfying

\[
\boxed{\ \|p_Q\|_\infty<536\,K^2/s.\ }
\]

No moment, support, log-concavity, sign, iid, exact-rank, diagonal-basis, leverage, smoothness, or post-rotation-independence assumption is added.

The proof uses the completed and re-read marginal-free physical-crossing receivers from the threshold-nine proof:

\[
\|p_Q\|_\infty\le C_3 E_3(M)^{-1/6},
\qquad
C_3=3\sqrt2\,e(9/2)^{1/6}
<\frac{232551}{15680},
\tag{R3}
\]

and

\[
\sup_a\mathbb E|Q-a|^{-1/2}
\le C_2E_2(M)^{-1/8},
\qquad C_2=8\sqrt e\,2^{-1/8}<13.
\tag{R2}
\]

These receivers retain arbitrary same-bank and affine phases and use only literal independent coordinate banks; deterministic projections occur only in Jacobian/density estimates. Their complete grouped weighted-subset/physical-row-promotion proof was re-read in this invocation.

## 1. New rational structural retuning

Normalize `K=s=1` and set

\[
\eta=\frac{2}{41},\qquad
\rho=\sqrt\kappa=\frac{18}{325},\qquad
\kappa=\rho^2.
\tag{1}
\]

A pivot means a scalar diagonal entry of modulus at least `eta`, or a principal `2x2` determinant of modulus at least `eta`.

With no pivot,

\[
|a_{ii}|<\eta,
\qquad
|a_{ij}|<q:=\sqrt{\eta^2+\eta}=\frac{\sqrt{86}}{41}.
\tag{2}
\]

### Retuned spectral-to-volume proposition, orders `k<=3`

If `1<=k<=3`, there is no pivot, and `s_{4k-3}(A)>=1`, then

\[
V_k(A)\ge\kappa^k.
\tag{3}
\]

**Proof.** If `V_k<kappa^k`, the standard telescoping argument selects `0<=r<=k-1<=2` with `V_r>0` and `V_{r+1}<kappa V_r` (or the last positive volume before the first zero). For `r=0`,

\[
\|A\|\le\|\operatorname{diag}A\|+\|\operatorname{off}A\|_F
<\eta+\rho<1,
\]

contradicting the spectral hypothesis.

For `r=1,2`, volume-sampled completion gives

\[
A=D+R+E,
\quad \operatorname{rank}R\le3r,
\quad \operatorname{rank}R_{L,L}\le r,
\quad \|E\|_F<(r+1)\rho,
\]

with zero-diagonal `E` and `D=0` on the seed. Put `m=4k-3`. Since `m>=4r+1`, singular-value perturbation and global rank subtraction force at least `r+1` diagonal entries of `D` on `L` to have modulus at least `1-(r+1)rho`. Choose those coordinates as `H`. On `H`,

\[
|R_{ii}|>1-(r+1)\rho-\eta,
\qquad
|R_{ij}|<q+(r+1)\rho.
\]

For `r=2`, strict diagonal dominance follows from

\[
1-\eta-2q>9\rho.
\tag{4}
\]

Indeed (4) is equivalent to

\[
6033>650\sqrt{86},
\]

and squaring gives

\[
6033^2=36,397,089>36,335,000=650^2\cdot86.
\]

For `r=1`, it suffices that `1-eta-q>4rho`; using `sqrt(86)<10`, the left side exceeds `29/41`, while `4rho=72/325`. Thus `R[H,H]` has rank `r+1`, contradicting `rank R[L,L]<=r`. This proves (3).

A fair physical coordinate cut therefore gives, at order three,

\[
E_3(M)\ge4^{-3}\rho^6,
\qquad
E_3(M)^{-1/6}\le\frac2\rho=\frac{325}{9}.
\tag{5}
\]

At order two it gives

\[
E_2(M)^{-1/8}\le\sqrt{\frac2\rho}=\frac{5\sqrt{13}}3.
\tag{6}
\]

## 2. Pivot half-potential at the new `eta`

The sharpened kernel and quarter-power estimates already proved in the reviewed nine-direction retuning are

\[
J(d)<6+2\log_+(1/|d|)
\tag{7}
\]

and, for any quadratic polynomial with quadratic operator norm at least one,

\[
\sup_a\mathbb E\log_+\frac1{|R-a|}<\frac{199}{20}.
\tag{8}
\]

For a scalar pivot under a two-large-direction hypothesis, the exact square-profile domination, Schur count, (7), and (8) therefore give

\[
H(Q)<\eta^{-1/2}\left(6+2\frac{199}{20}\right)
=\frac{259}{10}\eta^{-1/2}.
\tag{9}
\]

The definite-pair branch is smaller because `4*pi<259/10`.

For the indefinite-pair branch use the reviewed physical-coordinate hyperbolic tail split with `q=2/9`, which gives

\[
H_{\rm ind}(D)
\le D^{-1/2}\bigl(4C_0+8+4\log_+(B\sqrt D)\bigr),
\]

where `C_0<81/20` and `B=36sqrt(2)/49`. For `D>=eta`, this function is decreasing once the logarithm activates, while before activation it is a constant times `D^-1/2`; moreover

\[
B\sqrt\eta=\frac{72}{49\sqrt{41}}<1.
\]

Hence its maximum occurs at `D=eta` and

\[
H_{\rm ind}<\frac{121}{5}\eta^{-1/2}
<\frac{259}{10}\eta^{-1/2}.
\tag{10}
\]

Thus every pivot with at least two unit spectral directions has truncated half potential bounded by the right side of (9), and full half potential bounded by

\[
\frac{259}{10}\eta^{-1/2}+1.
\tag{11}
\]

## 3. The four nine-direction branches

Assume `s_9(A)>=1`.

**No pivot.** By (3), (5), and (R3),

\[
\|p_Q\|_\infty
<\frac{232551}{15680}\frac{325}{9}
=\frac{1679535}{3136}
<536,
\tag{12}
\]

because `536*3136-1679535=1361>0`. This branch has an integrable characteristic function and hence a continuous `C_0` density.

**Scalar pivot.** The exact Schur complement retains at least eight unit spectral directions. If it has a pivot, (11) applies. If it has no pivot, then `s_5>=1`; (3), the order-two cut, and (R2) give full half potential

\[
<13\frac{5\sqrt{13}}3<79,
\]

which is much smaller than (11). The outer square profile therefore yields

\[
\|p_Q\|_\infty
<\eta^{-1}\frac{259}{10}+\eta^{-1/2}
=\frac{10619}{20}+\sqrt{\frac{41}{2}}.
\]

Since `sqrt(41/2)<23/5` (equivalently `1025<1058`),

\[
\|p_Q\|_\infty<\frac{10711}{20}=535.55<536.
\tag{13}
\]

**Definite pair pivot.** Direct conditioning gives

\[
\|p_Q\|_\infty\le\pi\eta^{-1/2}
=\pi\sqrt{41/2}<15<536.
\tag{14}
\]

**Indefinite pair pivot.** The pair Schur complement retains at least seven unit spectral directions. Averaging the physical-coordinate hyperbolic envelope against its critical-value law and using (8) gives a bound below `100`, hence below 536. (For example `log16<14/5`, `sqrt(41/2)<23/5` already suffice.)

These alternatives exhaust the normalized problem, proving

\[
\|p_Q\|_\infty<536.
\]

For general `K,s`, set `Y=KX` and

\[
\widetilde Q=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c,
\qquad Q=(s/K^2)\widetilde Q.
\]

Then `Y` has coordinate density caps one and `s_9(A/s)>=1`; one-dimensional density scaling gives

\[
\boxed{\|p_Q\|_\infty<536K^2/s.}
\]

## 4. B02 endpoint obstruction below the current proof

The scalar Fourier-power exponent cannot itself be improved: for the admissible cap-one Gaussian `f(x)=e^{-pi x^2}`,

\[
\widehat f(t)=e^{-t^2/(4\pi)},
\qquad
\int|\widehat f(t)|^pdt=\frac{2\pi}{\sqrt p}.
\]

Moreover an order-two certificate alone cannot produce a universal density bound. If `U,V` are independent `Unif[-1/2,1/2]`, then `U^2` has density `s^{-1/2}` on `(0,1/4)`, so the density of `U^2-V^2` at zero is

\[
\int_0^{1/4}\frac{ds}{s}=\infty.
\]

Thus a threshold-eight proof must spend the additional overlap/collar structure found by the structural reductions; it cannot close merely by sharpening constants in the scalar Fourier-power lemma or by treating `E_2` as an `L^infinity` endpoint.

## Status

This run supplies one complete review of the new `<536` retuning. It does **not** satisfy the owner requirement of two genuinely separate complete reviews for that new constant, so it remains a candidate improvement rather than release-validated. Multiplicity eight remains `GAP`; unrestricted three-eigenvalue QFORM remains `OPEN`.
