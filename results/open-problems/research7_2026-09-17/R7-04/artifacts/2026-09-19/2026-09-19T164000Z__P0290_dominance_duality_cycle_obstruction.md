# P0290: dominance coordinates, randomized observable reduction, and an exact reverse-monotonicity obstruction

Target: Lasse Leskelä, *Ross's second conjecture and supermodular stochastic ordering*, Queueing Systems 100 (2022), 213--215, DOI `10.1007/s11134-022-09824-0`, Problem 2 on journal p. 214.

Status of this artifact: **PARTIAL / OPEN**. It does not prove or refute Problem 2. It rewrites the complete second-order light-traffic mechanism in finite dominance coordinates and proves that the most direct high-quality-factor directed-cycle lift is impossible for every strictly positive stationary law.

Source rechecked 2026-09-19 in the accepted manuscript:
`https://acris.aalto.fi/ws/portalfiles/portal/89616571/Ross_s_second_conjecture_and_supermodular_stochastic_ordering.pdf`.
Problem 2 asks whether Ross workload monotonicity remains valid when `lambda(t)=f(X(t))`, with `f` Boolean or more generally deterministic and `X` a doubly stochastically monotone CTMC. A bounded fresh title/problem search did not locate a later explicit solution. This is negative evidence only, not a proof of current openness or novelty.

A directly relevant prior-art bridge is Brando Vagenende, Brecht Verbeken, Marie-Anne Guerry, *Eigenvalue regions and realising monotone stochastic matrices*, Electronic Journal of Linear Algebra 42 (2026), 387--398, DOI `10.13001/ela.2026.10159`. Their dominance matrix is nonnegative for a monotone stochastic matrix and preserves the nontrivial spectrum. The continuous-time stationary-adjoint identities below are derived here for the P0290 mechanism; no novelty claim is made for the underlying dominance-coordinate idea.

---

## 1. Setup

Let `X` be an irreducible finite-state CTMC on the ordered state space

\[
E=\{0,1,\ldots,m\},\qquad m\ge 1,
\]

with generator `Q` and strictly positive stationary law

\[
\pi=(\pi_0,\ldots,\pi_m),\qquad \pi Q=0.
\]

For `k=1,...,m`, define the upper-threshold vector

\[
h_k(i)=\mathbf 1_{\{i\ge k\}}.
\]

Let `H` be the `(m+1) x m` matrix with columns `h_k`. Every real observable `f:E->R` has the unique representation

\[
f=f(0)\mathbf 1+Hd,
\qquad d_k=f(k)-f(k-1).
\tag{1.1}
\]

Write

\[
p_k=\Pr_\pi\{X\ge k\}=\sum_{i=k}^m\pi_i,
\qquad p=(p_1,\ldots,p_m)^T,
\]

and center the threshold matrix by

\[
\bar H=H-\mathbf 1p^T.
\tag{1.2}
\]

Then `pi \bar H=0`.

Let `D` denote the first-difference operator on vectors indexed by `E`, so that

\[
(Dv)_k=v(k)-v(k-1),\qquad k=1,\ldots,m.
\]

Define the continuous-time dominance block

\[
\boxed{A=DQH.}
\tag{1.3}
\]

Because a vector is determined by its value at `0` and its first differences, there is a row vector `r^T` with

\[
QH=\mathbf 1r^T+HA.
\]

Multiplying by `pi` and using `pi Q=0` gives `r^T=-p^TA`. Hence

\[
\boxed{Q\bar H=\bar H A.}
\tag{1.4}
\]

Consequently

\[
\boxed{e^{tQ}\bar H=\bar H e^{tA}\qquad(t\ge0).}
\tag{1.5}
\]

This is the exact finite-dimensional reduction of every centered deterministic observable.

---

## 2. B17 -- the dominance-matrix language from monotone stochastic matrices

The 2026 Vagenende--Verbeken--Guerry paper makes the one-order-lower dominance matrix central for discrete-time monotone stochastic matrices. In the present threshold convention, (1.5) gives the continuous-time analogue directly.

For a stochastic matrix `P` on the ordered finite state space, stochastic monotonicity is equivalent to requiring every tail probability `P h_k` to be nondecreasing in the starting state. Equivalently,

\[
DPH\ge0\quad\text{entrywise}.
\]

Applying this to `P_t=e^{tQ}` and (1.5),

\[
DP_tH=e^{tA}.
\]

Therefore

\[
\boxed{
Q\text{ is stochastically monotone}
\iff e^{tA}\ge0\text{ for every }t\ge0
\iff A\text{ is Metzler}.
}
\tag{2.1}
\]

Thus forward stochastic monotonicity becomes ordinary positivity of a lower-dimensional semigroup.

---

## 3. Threshold covariance metric and its exact inverse

Let `Pi=diag(pi_0,...,pi_m)` and define

\[
G=\bar H^T\Pi\bar H.
\tag{3.1}
\]

Because the threshold differences span the centered functions, `G` is positive definite. Directly,

\[
\boxed{
G_{k\ell}=p_{\max(k,\ell)}-p_kp_\ell.
}
\tag{3.2}
\]

There is a useful exact inverse. For `1<=k<=m`,

\[
\boxed{
(G^{-1})_{kk}=\frac1{\pi_{k-1}}+\frac1{\pi_k},
}
\tag{3.3}
\]

and for `1<=k<m`,

\[
\boxed{
(G^{-1})_{k,k+1}=(G^{-1})_{k+1,k}=-\frac1{\pi_k},
}
\tag{3.4}
\]

with all other off-diagonal entries zero.

### Proof of (3.3)--(3.4)

Let `B` denote the tridiagonal matrix specified by (3.3)--(3.4). For fixed `ell`, the function `k -> G_{k ell}` is affine in the cumulative tail on each side of `ell`; applying the weighted second-difference row of `B` cancels on `k<ell` and `k>ell`. At `k=ell`, the jump of the first difference equals `1`. Equivalently, direct substitution using

\[
p_k-p_{k+1}=\pi_k
\]

shows `(BG)_{k ell}=delta_{k ell}`. Hence `B=G^{-1}`. This is the discrete Brownian-bridge precision matrix associated with the stationary masses.

---

## 4. B25 -- count the adjoint action two ways

Let `Q*` be the stationary time reversal,

\[
Q^*_{ij}=\frac{\pi_j}{\pi_i}Q_{ji}.
\]

Let `A*` be its dominance block, so

\[
Q^*\bar H=\bar H A^*.
\]

For arbitrary difference vectors `d,e`, count the same stationary inner product in two ways:

\[
\begin{aligned}
d^TGA^*e
&=\langle \bar Hd,Q^*\bar He\rangle_\pi\\
&=\langle Q\bar Hd,\bar He\rangle_\pi\\
&=d^TA^TGe.
\end{aligned}
\]

Therefore

\[
\boxed{A^*=G^{-1}A^TG.}
\tag{4.1}
\]

Combining (2.1) for `Q` and `Q*` yields the exact source-order constraint

\[
\boxed{
X\text{ is doubly stochastically monotone}
\iff
A\text{ and }G^{-1}A^TG\text{ are both Metzler}.
}
\tag{4.2}
\]

This is the finite-dimensional core that the earlier raw-generator searches were missing: source admissibility is not merely a spectral sector condition; it is simultaneous cone positivity for `A` and its `G`-adjoint.

---

## 5. Exact covariance and the light-traffic derivative in dominance coordinates

For `f` with difference vector `d`, constants do not affect covariance. From (1.5),

\[
\boxed{
C_f(t)=\operatorname{Cov}_\pi(f(X_0),f(X_t))
=d^TG e^{tA}d.
}
\tag{5.1}
\]

The recovered P0290 light-traffic coefficient is

\[
J_f(c)=\int_0^1(1-u)C_f(cu)\,du.
\]

Put

\[
\Psi(z)=\int_0^1u(1-u)e^{uz}\,du
=\frac{(z-2)e^z+z+2}{z^3},
\qquad \Psi(0)=\frac16.
\]

Differentiating under the finite-dimensional integral gives

\[
\boxed{
J_f'(c)=d^TGA\Psi(cA)d.
}
\tag{5.2}
\]

Hence a second-order source counterexample is equivalent to a positive direction of

\[
\operatorname{Sym}[GA\Psi(cA)]
\]

inside the bi-Metzler admissible cone (4.2), together with the elementary lift constraints ensuring that the dominance block comes from a genuine Markov generator.

---

## 6. B9 -- randomize the observable, not the chain

The deterministic function `f` is arbitrary in Problem 2. This permits a useful probabilistic existence test.

Choose a Gaussian difference vector

\[
D\sim N(0,G^{-1}).
\]

Taking expectation in (5.2),

\[
\begin{aligned}
\mathbb E[J_D'(c)]
&=\operatorname{tr}\bigl(GA\Psi(cA)G^{-1}\bigr)\\
&=\boxed{\operatorname{tr}(A\Psi(cA))}.
\end{aligned}
\tag{6.1}
\]

Therefore

\[
\boxed{
\operatorname{tr}(A\Psi(cA))>0
\Longrightarrow
\exists\text{ deterministic real }f\text{ with }J_f'(c)>0.
}
\tag{6.2}
\]

Since adding a constant to `f` changes only the `c`-independent mean term, the same derivative is obtained after shifting `f` to be nonnegative. Thus (6.2) is a valid source-facing sufficient condition for activating the already-recovered light-traffic counterexample route.

This reduces one observable search to a purely spectral scalar test. It is only sufficient: the trace can be nonpositive while the symmetric quadratic form still has a positive direction.

---

## 7. Exact obstruction to the directed-cycle lift

The previous R7-04 run proved that high-quality-factor directed cycles can make the scalar triangular filter rise, but those cycles were outside the source class. The most natural attempted lift is to place the same directed cycle in the dominance block itself.

Let `m>=3` and let `C` be the `m x m` cyclic shift

\[
C_{k,k+1}=1\quad(1\le k<m),
\qquad C_{m,1}=1,
\]

with all other entries zero. Consider

\[
A=\alpha C-\beta I,
\qquad \alpha>0,
\tag{7.1}
\]

where `beta` is arbitrary. This `A` is Metzler, so it satisfies forward dominance positivity. The reverse constraint fails for every positive stationary law.

**Theorem 7.1 (pure cycle dominance obstruction).** For every strictly positive probability vector `pi` on `0,...,m`,

\[
\boxed{
\left(G^{-1}A^TG\right)_{2m}
=-\alpha\pi_m\left[
\frac{\pi_1+\cdots+\pi_{m-1}}{\pi_1}
+\frac{\pi_1}{\pi_2}
\right]<0.
}
\tag{7.2}
\]

Consequently `G^{-1}A^TG` is not Metzler. No irreducible doubly stochastically monotone CTMC can have a dominance generator equal to a shifted/scaled directed cycle.

### Proof

The diagonal term `-beta I` does not affect the off-diagonal entry `(2,m)`, so it suffices to compute `G^{-1}C^TG`.

By (3.3)--(3.4), row `2` of `G^{-1}` has exactly three nonzero entries:

\[
(G^{-1})_{2,1}=-\pi_1^{-1},
\quad
(G^{-1})_{2,2}=\pi_1^{-1}+\pi_2^{-1},
\quad
(G^{-1})_{2,3}=-\pi_2^{-1}.
\]

Because `C` is the forward cyclic shift, rows `1,2,3` of `C^TG` are respectively rows `m,1,2` of `G`. Also, from (3.2),

\[
G_{r,m}=\pi_m(\pi_0+\cdots+\pi_{r-1})
\quad(1\le r\le m),
\]

where the `r=m` case reads `G_{m,m}=\pi_m(1-\pi_m)`. Therefore

\[
\begin{aligned}
(G^{-1}C^TG)_{2m}
={}&-\frac{G_{m,m}}{\pi_1}
+\left(\frac1{\pi_1}+\frac1{\pi_2}\right)G_{1,m}
-\frac{G_{2,m}}{\pi_2}\\
={}&-\pi_m\frac{\pi_0+\cdots+\pi_{m-1}}{\pi_1}
+\pi_m\pi_0\left(\frac1{\pi_1}+\frac1{\pi_2}\right)
-\pi_m\frac{\pi_0+\pi_1}{\pi_2}\\
={}&-\pi_m\left[
\frac{\pi_1+\cdots+\pi_{m-1}}{\pi_1}
+\frac{\pi_1}{\pi_2}
\right].
\end{aligned}
\]

Multiplication by `alpha>0` proves (7.2). Every mass is strictly positive, so the bracket is strictly positive. QED.

---

## 8. Quantitative compensation inequality

The obstruction has a useful robust form. Define the reverse-monotonicity functional

\[
\mathcal L_\pi(B)=\left(G^{-1}B^TG\right)_{2m}.
\]

Double monotonicity requires `L_pi(A)>=0`. If

\[
A=\alpha C-\beta I+E,
\]

then Theorem 7.1 forces

\[
\boxed{
\mathcal L_\pi(E)
\ge
\alpha\pi_m\left[
\frac{\pi_1+\cdots+\pi_{m-1}}{\pi_1}
+\frac{\pi_1}{\pi_2}
\right].
}
\tag{8.1}
\]

Thus any source-admissible attempt to preserve the high-Q directed-cycle mechanism must add enough chord/extra-rate structure to compensate a strictly positive dual deficit. The required correction is not infinitesimal for a fixed stationary law.

This explains structurally why the prior directed-cycle counterexample to generic time-average monotonicity did not lift automatically into Leskelä's Problem 2.

---

## 9. What this run settles and what it does not

Settled in this artifact:

1. The complete finite second-order P0290 mechanism has the exact dominance-coordinate form (5.2).
2. Double stochastic monotonicity is simultaneous Metzler positivity of `A` and its explicit stationary metric adjoint `G^{-1}A^TG`.
3. Randomizing the deterministic observable gives the spectral sufficient test (6.2).
4. The pure directed-cycle dominance mechanism is impossible for every positive stationary distribution, with the exact deficit (7.2) and compensation bound (8.1).

Not settled:

1. The bi-Metzler cone may still contain more complicated nonnormal oscillatory blocks for which `J_f'(c)>0`.
2. Excluding all second-order reversals would still not prove the full queueing statement at moderate or heavy load.
3. No source-valid positive `Delta_Ross` has been certified.
4. No universal proof of Problem 2 has been obtained.

Therefore the source status remains **OPEN / PARTIAL** and the frozen source metric does not move.
