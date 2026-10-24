# account01/B19 guarded improvements — constant sharpening, leverage deletion, and lower-threshold audit

Run: `20260924T124715Z-account01-B19-fixedmult-audit-r11`  
Pinned baseline: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Status: proved improvements/structural reductions only. **No unconditional multiplicity reduction below 17 is claimed.**

## 1. Same-proof constant sharpening at multiplicity 17

The baseline defines

\[
L_0=4+4\log 16.
\]

Its scalar-pivot proof of the nine-direction truncated half-potential actually gives

\[
H(Q)\le 10(20+12\log16)=200+120\log16,
\]

which is larger than the no-pivot `<200`, definite-pair `<40\pi`, and indefinite-pair bounds. Therefore

\[
\sup_a\mathbb E|Q-a|^{-1/2}
\le 201+120\log16.
\]

At the main scalar pivot `|A_{ii}|>=1/100`,

\[
\|p_Q\|_\infty
\le10(201+120\log16)
=2010+1200\log16
=5337.1064666877\ldots .
\]

All other main branches are smaller. Hence, with **every baseline hypothesis unchanged**,

\[
\boxed{\|p_Q\|_\infty\le(2010+1200\log16)K^2/s<5610K^2/s.}
\]

This is a complete numerical strengthening of the written `10000 K^2/s` theorem, not a change of multiplicity.

## 2. Independent check and application of the fractional leverage determinant

After completing the baseline audit, I checked the current fractional graph-determinant calculation independently. For

\[
Z=F(X_I)+2X_I^TMX_J+G(X_J),
\]

let `m_i^T` be row `i` of `M` and

\[
\ell_i=m_i^T(M^TM)^+m_i.
\]

For `q\in[1,2]`, if `max_i ell_i<=q/2`, the unsquared decoupling inequality, Jensen to power `q`, the same graph Brascamp--Lieb frame, and scalar Fourier exponent `q/d_i>=2` give

\[
\boxed{
|\phi_Z(t)|\le
\det\!\left(I+\frac{q t^2}{2\pi^2e^2}M^TM\right)^{-1/(4q)}.
}
\]

The cancellation uses the regularizer

\[
\alpha=\frac{8\pi^2e^2}{q}.
\]

If `Z_k(M)>0`, retaining order `k` gives power `p=k/(2q)`. When `k>2q`, Fourier inversion yields

\[
\boxed{
\|p_Z\|_\infty
\le e\sqrt{\frac2q}\frac{k}{k-2q}
Z_k(M)^{-1/(2k)}.
}
\]

At order four with `q=3/2` and maximum row leverage `<=3/4`,

\[
\|p_Z\|_\infty\le\frac{8e}{\sqrt3}Z_4(M)^{-1/8}.
\]

The baseline spectral-to-volume proposition is valid at `k=4`; thus no pivot plus `s_13(A)>=1` gives a physical cut with

\[
Z_4(M)\ge4^{-4}\kappa^4,
\qquad Z_4(M)^{-1/8}\le160.
\]

If that volume-good cut has a row or, after swapping banks, column leverage maximum `<=3/4`, then

\[
\boxed{
\|p_Q\|_\infty\le\frac{1280e}{\sqrt3}<2009.
}
\]

The pivot branches already close under `s_13` because a scalar pivot leaves at least twelve large Schur directions, while a pair branch needs less. Thus this is a rigorous **conditional 13-eigenvalue theorem** with the explicit diffuse-leverage gate. It is not the unconditional fixed-13 theorem.

## 3. New exact row-deletion inequality for crossing volume

This run adds a deterministic bridge between ordinary row leverage and the order-`k` crossing volume.

Let `M` be an `m x n` real matrix, let `M_{-i}` denote deletion of physical row `i`, and define

\[
Z_k(M)=\sum_{|S|=|T|=k}\det(M_{S,T})^2
=e_k(s_1(M)^2,\ldots,s_r(M)^2).
\]

For a nonzero row-space direction define

\[
\ell_i=m_i^T(M^TM)^+m_i,
\]

and put `ell_i=0` for a zero row.

### Lemma

For every `k>=1`,

\[
\boxed{Z_k(M_{-i})\ge(1-\ell_i)Z_k(M).}
\]

Equivalently, if `C_i^{(k)}` is the total squared `k x k` minor mass using row `i`, then

\[
\boxed{
\frac{C_i^{(k)}}{Z_k(M)}\le\ell_i
}
\]

whenever `Z_k(M)>0`.

### Proof

Write an SVD

\[
M=U\Sigma V^T,
\qquad \lambda_j=\sigma_j^2>0,
\qquad j=1,\ldots,r.
\]

By Cauchy--Binet,

\[
Z_k(M)=e_k(\lambda_1,\ldots,\lambda_r).
\]

The normalized squared-minor weights on `k`-row subsets are the fixed-size determinantal weights associated with `L=MM^T`. Expanding once more by Cauchy--Binet in the eigenbasis gives the exact inclusion fraction of physical row `i` as

\[
\tau_i^{(k)}
:=\frac{C_i^{(k)}}{Z_k(M)}
=\sum_{j=1}^r U_{ij}^2 p_j,
\]

where

\[
p_j=
\frac{\lambda_j e_{k-1}(\lambda_1,\ldots,\widehat{\lambda_j},\ldots,\lambda_r)}
{e_k(\lambda_1,\ldots,\lambda_r)}.
\]

Each `p_j` is an inclusion probability in the elementary-symmetric `k`-subset distribution, hence `0<=p_j<=1`. Therefore

\[
\tau_i^{(k)}
\le\sum_{j=1}^rU_{ij}^2
=(M(M^TM)^+M^T)_{ii}
=\ell_i.
\]

Since `Z_k(M)=Z_k(M_{-i})+C_i^{(k)}`, the displayed deletion inequality follows.

### Consequence for the attempted 13-direction route

A row of leverage at most `3/4` can be deleted while retaining at least one quarter of every order-four volume:

\[
Z_4(M_{-i})\ge\frac14 Z_4(M).
\]

Thus low-leverage rows are quantitatively harmless for the crossing-volume currency. The only obstruction to iterating toward the fractional determinant receiver is genuinely near-coloop geometry, where one or more physical rows have leverage tending to one. This does **not** itself close that branch: high ordinary leverage does not force the row to carry a fixed fraction of `Z_4`, because `tau_i^{(4)}<=ell_i` is one-sided.

## 4. Why the current proof does not give multiplicity 16

The baseline no-pivot contradiction at order five uses a sampled ratio at `r<=4`. At the terminal `r=4` under the attempted hypothesis `s_16(A)>=1`, the full completion rank bound `rank R<=12` gives only

\[
16-12=4
\]

large diagonal entries of `D`. The restricted correction has `rank R[L,L]<=4`, so four large diagonals no longer contradict it.

A current account02/B19 exact construction shows the `(3r,r)` rank pair can already saturate at `r=1`; I independently recomputed its matrices and ranks. Hence this is not an artifact that can be removed by simply tightening the manuscript's rank bookkeeping.

Current terminal refinements are useful but not closing:

- repivoting the four large diagonal indices yields an exact **8-versus-8** Schur saturation rather than a contradiction;
- a completed neighboring-minor calculation forces two adjacent disjoint four-minors to be larger than the sampled seed by the factor
  \[
  (109/100)^4>1,
  \]
  but the larger neighbors are not known to satisfy the same small residual ratio required to repeat the good-seed argument.

Therefore

\[
\boxed{\text{unconditional multiplicity 16 remains GAP / OPEN in this architecture}.}
\]

Any claimed `17 -> 16` replacement must solve the terminal good-seed transfer (or use a genuinely different analytic/structural receiver). The conditional order-four leverage theorem gives a separate path toward 13, whose unpaid endpoint is the two-sided heavy-leverage/near-coloop case.

## Current rigorous threshold accounting

- Unconditional fixed multiplicity: **17**, with improved constant `<5610 K^2/s` from the same proof.
- Conditional diffuse-leverage multiplicity: **13**, with explicit order-four leverage gate and normalized no-pivot bound `<2009`.
- Unconditional 16: **not proved**.
- Unconditional 13: **not proved**.
- Full 3-eigenvalue conjecture: **open**.
