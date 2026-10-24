# account03/B08 r57 — independent reconstruction of the nine-eigenvalue candidate

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T124642Z-account03-B08-fixedmult-r57`  
Baseline manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Candidate reviewed: `yspennstate/math-open-problems@8ff490c177d0cd7d6f33130f1431785e312a9d10`, account03/B04 nine-eigenvalue candidate  
Status: **PASS in this independent worker review; second independent end-to-end review still required before promotion.**

## Result

For arbitrary independent real coordinates with densities bounded by `K`, arbitrary real symmetric `A`, and arbitrary affine `b,c`, the B04 threshold reduction is valid:

\[
 s_9(A)\ge s>0
 \quad\Longrightarrow\quad
 X^TAX+b^TX+c\text{ has an essentially bounded density.}
\]

The candidate's written constant `6010 K^2/s` is valid. In addition, combining the same threshold proof with the independently rechecked exact pivot constants below gives the sharper bound

\[
 \boxed{\ \|p_{X^TAX+b^TX+c}\|_\infty<3110\,K^2/s.\ }
\]

This review does **not** establish continuity in every branch. The no-pivot branch below is `C_0`; the full nine-eigenvalue theorem is recorded only as an essential-supremum statement.

## 1. Dependency audit

I did not treat the new B04 grouped compiler as a black box. I reconstructed the threshold argument using two earlier full-form original-coordinate receivers whose exact scopes match the required branches:

1. `QFORM-THIRDCOMPOUND-CROSS-PROMOTION-v1`, `yspennstate/math-open-problems@c2ce876df8b5483a00802170001d4144bb4cdbfa`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B04/20260923T194715Z-account01-B04-QFORM-auto11-r18/REPORT.md`:
   for a literal original-coordinate split with crossing block `B`, arbitrary same-bank quadratic/affine phases retained,
   \[
   E_3(B)=e_3(BB^T)>0
   \implies
   \|p_Q\|_\infty\le6^{4/3}E_3(B)^{-1/6},\qquad p_Q\in C_0.
   \]
   The finite promotion proof removes all physical row-marginal assumptions without rotating the random inputs.

2. `QFORM-ROW-MARGINAL-FREE-2VOLUME-COLLISION-v1`, `yspennstate/math-open-problems@588fa418bc29d4b889fcbbee2b61370234ceef37`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B03/20260923T175336Z-account01-B03-QFORM-r30/REPORT.md`:
   for a literal two-bank full quadratic with `Z_2=e_2(BB^T)>0`,
   \[
   \sup_a\mathbb E|Q-a|^{-1/2}
   \le8(2e)^{1/4}Z_2^{-1/8}.
   \]
   Again arbitrary same-bank quadratic/affine phases are retained and the row-marginal gate is removed by a finite physical-hub promotion tree.

Both are compatible with every live correction relevant here: no post-rotation independence, no conditional-cap shortcut, no arbitrary-joint coarea, and no law-uniform pointwise quadratic-phase decay is used.

## 2. No-pivot branch under only nine large eigenvalues

Normalize first to `K=s=1`, and keep the manuscript's
\[
 \eta=1/100,\qquad \kappa=1/80^2.
\]
If `A` has no `eta`-pivot and `s_9(A)>=1`, the audited manuscript spectral-to-volume proposition with `k=3` applies because `4k-3=9`:
\[
 V_3(A)\ge\kappa^3.
\]
The audited random physical half-cut gives an original-coordinate crossing block `M=A[I,J]` with
\[
 E_3(M)\ge4^{-3}\kappa^3.
\]
Therefore the completed third-compound receiver gives
\[
 \|p_Q\|_\infty
 \le6^{4/3}(4^{-3}\kappa^3)^{-1/6}
 =160\,6^{4/3}
 <1744.436.
\]
This branch has a continuous `C_0` density. All same-bank terms and all affine terms remain inside the full-form receiver.

## 3. Scalar pivot under only nine large eigenvalues

Suppose an original diagonal entry satisfies `|A_hh|>=eta`. Completing the square only in the original coordinate `X_h` gives the manuscript profile
\[
 p_Q(z)\le |A_{hh}|^{-1/2}\,\mathbb E|z-R|^{-1/2},
\]
where the quadratic matrix `S` of `R` is the scalar Schur complement. The audited Schur count gives
\[
 N_S(1)\ge N_A(1)-1\ge8.
\]

If `S` has an `eta`-pivot, the sharpened pivot estimate in Section 4 below gives
\[
 \sup_a\mathbb E|R-a|^{-1/2}<311.
\]
If `S` has no `eta`-pivot, then `s_5(S)>=1`; the audited spectral-to-volume proposition with `k=2` and the physical random cut give a crossing `M_S` with
\[
 Z_2=e_2(M_SM_S^T)\ge4^{-2}\kappa^2.
\]
The completed two-volume half-Riesz theorem yields
\[
 \sup_a\mathbb E|R-a|^{-1/2}
 \le8(2e)^{1/4}(4^{-2}\kappa^2)^{-1/8}
 =8(2e)^{1/4}\sqrt{160}
 <154.519<311.
\]
Thus in either scalar-pivot subcase
\[
 \|p_Q\|_\infty<10\cdot311=3110.
\]
No independence between the completed square and `R` is asserted; the manuscript profile is a conditional measure-domination inequality.

## 4. Independent check of the `<311` pivot half-potential constant

This is a same-proof constant refinement, not a new probabilistic premise.

For the manuscript kernel
\[
 J(d)=\int_{-1}^1|x|^{-1/2}|x-d|^{-1/2}\,dx,
\]
direct splitting and the substitutions `x=d sin^2 theta`, `x=d cosh^2 t`, and `x=-d sinh^2 t` give
\[
 J(d)=2\operatorname{asinh}(d^{-1/2})+\pi+2\operatorname{acosh}(d^{-1/2})\quad(0<d\le1),
\]
\[
 J(d)=2\operatorname{asinh}(d^{-1/2})+2\arcsin(d^{-1/2})\quad(d\ge1),
\]
and hence
\[
 J(d)<7+2\log_+(1/d).
\]

The exact Gaussian-smoothing coefficient in the manuscript quarter-power lemma is
\[
 2^{5/8}\pi^{-1/4}e^{3/8}\Gamma(3/8)=3.995259\ldots<9/2.
\]
Therefore, whenever the remainder has operator norm at least one,
\[
 \sup_a\mathbb E\log_+\frac1{|R-a|}
 \le L_1:=4+4\log(9/2).
\]
At `eta=1/100`, the three pivot branches consequently satisfy:

- scalar pivot: truncated half-potential
  \[
  \le10(7+2L_1)<278;
  \]
- definite pair: `<40 pi<160`;
- indefinite pair: retaining the exact hyperbolic middle-length constant `(15/2)log2` gives
  \[
  H(Q)\le D^{-1/2}\left(8+30\log2+4\log_+(16\sqrt D)\right),\qquad D\ge1/100.
  \]
  Writing `u=sqrt(D)>=1/10`, the right side is decreasing from `u=1/10` because its numerator already exceeds the derivative contribution `4`; hence
  \[
  H(Q)\le10\left(8+30\log2+4\log(8/5)\right)<310.
  \]

Outside `|Q-a|<=1`, the half-Riesz kernel is at most one, so any pivot matrix with at least two surviving unit-scale eigenvalues satisfies
\[
 \sup_a\mathbb E|Q-a|^{-1/2}<311.
\]
This independently confirms the constant sharpening reported by account03/B13 at `df58be3590f9919c65ebe3f3fe15f64272e2b5cf`.

## 5. Two-coordinate pivots

The main `s_9` problem's remaining pivot cases are cheaper.

- A definite physical `2x2` pivot of determinant modulus at least `eta` has conditional density at most
  \[
  \pi/\sqrt\eta=10\pi<32.
  \]
- For an indefinite physical pair, the Schur count leaves at least seven eigenvalues of modulus at least one, hence in particular a nonzero unit-scale spectral direction. The audited hyperbolic-pair/logarithmic-potential argument applies verbatim and gives the manuscript bound `<251` (the exact constants above can only improve it).

These alternatives, the scalar pivot, and the no-pivot branch exhaust the normalized problem.

## 6. Scaling and exact quantifiers

For general `K,s`, put `Y=KX` and
\[
 \widetilde Q=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c=(K^2/s)Q.
\]
The coordinates of `Y` have density cap one and `s_9(A/s)>=1`; therefore
\[
 \|p_Q\|_\infty=(K^2/s)\|p_{\widetilde Q}\|_\infty<3110K^2/s.
\]
No Gaussianity, moments, log-concavity, support condition, sign restriction, diagonal-basis assumption, or independence after rotation has entered.

## 7. Review verdict and remaining threshold

**Verdict: PASS** for the nine-eigenvalue theorem in this independent B08 reconstruction. The B04 candidate's `6010` bound is valid, and the same threshold proof plus independently checked constants yields `<3110`.

This is one independent worker review only. A second genuinely separate end-to-end review is still required before the nine-eigenvalue theorem should replace the pinned release candidate under the owner's validation rule.

The unrestricted three-eigenvalue conjecture remains OPEN. Global continuity remains OPEN. The next structural threshold is `8`, whose no-pivot terminal chamber is isolated in the sibling improvement report for this run.
