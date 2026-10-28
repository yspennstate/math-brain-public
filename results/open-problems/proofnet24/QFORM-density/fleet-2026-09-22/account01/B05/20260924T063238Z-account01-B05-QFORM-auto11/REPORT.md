SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B05, 2026-09-24T06:32:38Z.
attacking: aggregate cross-star coarea in the near-coloop Witt survivor; pay the longitudinal-spike/rank-two-tail endpoint without reciprocal physical-pair selection.

# account01/B05 auto11 — sharp independent-hub / joint-planar coarea and the longitudinal-spike rank-two-tail closure

**Programme:** `QFORM-DENSITY-3EIG-20260922`.
**Assignment:** quadratic coarea / equivalent interval bound preserving arbitrary original-coordinate product densities.
**Status:** `NEW SUPPORTING ANALYTIC THEOREM + LONGITUDINAL-SPIKE EXACT-RANK-TWO-TAIL BRANCH PAID + PARTNER MAX-CUT APPLIED`; the full unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**.
**Regularity:** the new receivers prove absolute continuity and an essential `L^infinity` bound. They do **not** by themselves prove a continuous representative. Full-target continuity remains OPEN.
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The live corrections are retained throughout: no post-rotation independence, no arbitrary-joint rank-three coarea theorem, no conditional projection-density cap inferred from a marginal cap, no pointwise law-uniform van der Corput estimate, no moment/support/log-concavity hypothesis, and no deletion of a small random term.

## 1. Live Witt packet and newest compatible sources

The current exact-rank-three high-leverage zero-pivot survivor from account01/B05 is

\[
Q=2aV(H+\kappa U)+\alpha V^2+2\gamma VW+\delta W^2,                 \tag{1.1}
\]

where `H` is one literal original coordinate, independent of the residual original-coordinate product bank, and

\[
U=u\cdot X,\qquad V=v\cdot X,\qquad W=w\cdot X                     \tag{1.2}
\]

with `u,v,w` an orthonormal three-frame on that residual bank. The determinant-star currency is

\[
\boxed{S_i=a^2|\delta|.}                                              \tag{1.3}
\]

In the target-normalized high-leverage branch, `S_i>=1/2`.

The structural addendum `yspennstate/math-open-problems@b8c42cc3e7d06ba1362b8138887c79de8940348b` proved that if a normalized residual row is heavy, then either its transverse energy

\[
q_j=v_j^2+w_j^2                                                     \tag{1.4}
\]

is at least `1/4`, in which case the pair-anchored determinant star satisfies `T_ij>=S_i/4`, or else

\[
u_j^2>1/4,\qquad q_j<1/4.                                          \tag{1.5}
\]

There are at most three rows of the latter type. Account03/B05 r39 then paid every transverse-heavy row by the pair-anchored determinant-star coarea theorem, so the finite longitudinal-spike alternative is a genuine remaining endpoint.

The newest designated partner account02/B05 report is

`yspennstate/math-open-problems@3ca6f8113ff32fc642cc3582b4a338082e8d6d25`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260924T052537Z-account02-B05-qform-auto11/REPORT.md`.

It proves, among other things, the exact bank-gap implication

\[
\|p_J\|^2+\|p_K\|^2\ge G,
\qquad
G=s(1-s)(\alpha_J-\alpha_K)^2,                                      \tag{1.6}
\]

and records the completed source-disjoint Pluecker max-cut theorem used below. It also correctly rules out replacing the live linear product-projection triple by a generic bounded joint law.

The newest account03/B05 r41 report,

`yspennstate/math-open-problems@fe9f82e0c3206c1056b60963a75989baff4aa0ef`,

identifies the exact three-frame bank volume as the extra factor required by a rank-three physical crossing. In the notation below it is a determinant `D_B`, i.e. residual **area**, not merely residual length.

Finally, the already source-valid planar product-projection input used elsewhere in the programme is: if `B` is an original-coordinate coefficient matrix with two columns and positive Gram `G=B^T B`, then the two-dimensional projection of independent cap-one coordinates has joint density bounded by

\[
\boxed{\|p_{B^TX}\|_\infty\le 2/\sqrt{\det G}.}                     \tag{1.7}
\]

One explicit source using this exact normalized cap `2` is `proofnet24/QFORM-density/interactive/20260923T203000Z-two-bank-outer-density/REPORT.md`.

## 2. New analytic theorem: sharp-scaling one-hub / arbitrary-joint-planar receiver

The previous source theorem `proofnet24/QFORM-density/interactive/20260923T203100Z-beta-uniform-one-hub-square/REPORT.md` proves a uniform one-hub estimate with linear dependence on the planar density cap. The following interpolation uses both the planar cap and its total probability mass and gives the determinant scaling needed by the live Witt packet.

### Theorem 2.1 — `QFORM-INDEPENDENT-HUB-JOINT-PAIR-INTERPOLATED-COAREA-v1`

Let `H` be independent of a pair `(V,W)`. Assume

\[
0\le f_H\le m,\qquad \int f_H=1,
\qquad
0\le \rho_{V,W}\le K,\qquad \iint\rho_{V,W}=1.                    \tag{2.1}
\]

Let `a,d` be nonzero real numbers. Let `R(v,w)` be any real function which, for each fixed `v`, is a quadratic polynomial in `w` with **constant nonzero quadratic coefficient** `d`:

\[
R(v,w)=d w^2+\ell(v)w+r(v),                                         \tag{2.2}
\]

where `ell,r` may be arbitrary measurable functions for which the displayed random variable is finite. Then

\[
Q=2aVH+R(V,W)                                                        \tag{2.3}
\]

has an absolutely continuous law and

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
\le 3\,2^{2/3}\,K^{2/3}m^{2/3}
       (a^2|d|)^{-1/3}.
}                                                                    \tag{2.4}
\]

In particular the estimate is uniform in arbitrary `V^2`, `VW`, `V`, `W`, and constant terms. An arbitrary deterministic affine term in `(H,V,W)` is also allowed: because the active quadratic matrix has determinant `-a^2d`, a fixed translation removes the affine term without changing independence or density caps.

#### Proof

For `v!=0`, conditioning on `(V,W)=(v,w)` and changing variables in `H` gives the density formula

\[
p_Q(t)
=\iint \frac{\rho(v,w)}{2|av|}
 f_H\!\left(\frac{t-R(v,w)}{2av}\right)\,dw\,dv.                    \tag{2.5}
\]

The set `v=0` has zero `(V,W)`-probability because the pair has a joint density.

Fix `v!=0`. Complete the square in `w`:

\[
\frac{t-R(v,w)}{2av}=A_v-B_v(w-w_v)^2,
\qquad
|B_v|=\frac{|d|}{2|av|}.                                            \tag{2.6}
\]

We use the elementary one-sided half-Riesz bathtub inequality

\[
\int_{\mathbb R} f(A-Bx^2)\,dx
\le 2\sqrt m\,|B|^{-1/2}                                            \tag{2.7}
\]

for every probability density `0<=f<=m`. Indeed, with `y=|B|x^2`, the left side is

\[
|B|^{-1/2}\int_0^\infty
f(A-\operatorname{sgn}(B)y)y^{-1/2}\,dy,
\]

and among densities bounded by `m` with mass one the decreasing kernel is maximized by height `m` on `[0,1/m]`, whose integral is `2sqrt(m)`.

Using `rho<=K`, equations (2.5)--(2.7) give a pointwise-in-`v` contribution bounded by

\[
A_0|v|^{-1/2},
\qquad
A_0:=K\sqrt{2m}\,|ad|^{-1/2}.                                      \tag{2.8}
\]

There is a second bound which uses probability mass rather than the planar cap. Since `f_H<=m`, if

\[
p_V(v)=\int\rho(v,w)\,dw,
\]

then the same `v`-contribution is at most

\[
B_0\,p_V(v)|v|^{-1},
\qquad
B_0:=\frac{m}{2|a|}.                                                 \tag{2.9}
\]

Hence, for every `R_0>0`,

\[
\begin{aligned}
p_Q(t)
&\le \int_{|v|\le R_0}A_0|v|^{-1/2}\,dv
  +\int_{|v|>R_0}B_0p_V(v)|v|^{-1}\,dv\\
&\le 4A_0\sqrt{R_0}+\frac{B_0}{R_0}.                                \tag{2.10}
\end{aligned}
\]

The exact optimizer is

\[
R_0=\left(\frac{B_0}{2A_0}\right)^{2/3}.                            \tag{2.11}
\]

Substitution gives

\[
4A_0\sqrt{R_0}+B_0/R_0
=3\,2^{2/3}A_0^{2/3}B_0^{1/3}.                                     \tag{2.12}
\]

The powers of two inside `A_0,B_0` cancel, and

\[
A_0^{2/3}B_0^{1/3}
=K^{2/3}m^{2/3}(a^2|d|)^{-1/3}.                                    \tag{2.13}
\]

This proves (2.4), uniformly in `t`. The formula also gives interval domination, hence absolute continuity. QED.

### Why this theorem does not contradict the live arbitrary-joint counterexamples

The theorem needs a **genuinely independent hub `H`** and only a two-dimensional joint light pair. Account02/B05's live cancellation obstruction uses a third residual variable `U` sharing source with `(V,W)` and arranges `U` nonlinearly so that `W^2` cancels inside `H+kappa U`. That construction cannot be inserted into Theorem 2.1 without destroying hub independence. Thus Theorem 2.1 is a dependence-safe receiver for exactly the rank-two light endpoint, not a resurrected arbitrary-joint rank-three coarea lemma.

## 3. New structural theorem: longitudinal spikes cannot steal the transverse plane

Return to the orthonormal residual three-frame `(u,v,w)`. Let `L` be any set of longitudinal spikes satisfying

\[
|L|\le3,
\qquad
q_j=v_j^2+w_j^2<\frac14\quad(j\in L),                               \tag{3.1}
\]

and let `T=L^c` inside the residual bank. Define the tail transverse Gram matrix

\[
G_T=
\begin{pmatrix}
\|v_T\|^2&\langle v_T,w_T\rangle\\
\langle v_T,w_T\rangle&\|w_T\|^2
\end{pmatrix}.                                                       \tag{3.2}
\]

### Theorem 3.1 — `QFORM-LONGSPIKE-TRANSVERSE-GRAM-FLOOR-v1`

One has

\[
\boxed{G_T\succeq \frac14 I_2,\qquad \det G_T\ge\frac1{16}.}       \tag{3.3}
\]

Consequently the complete Pluecker square mass contained **entirely inside the tail** satisfies

\[
\boxed{
\sum_{j<k,\ j,k\in T}(v_jw_k-v_kw_j)^2
=\det G_T\ge\frac1{16}.
}                                                                    \tag{3.4}
\]

#### Proof

Because `(v,w)` are orthonormal on the full residual bank,

\[
G_T=I_2-G_L,
\qquad
G_L:=\sum_{j\in L}\binom{v_j}{w_j}(v_j,w_j).                        \tag{3.5}
\]

The matrix `G_L` is positive semidefinite and

\[
\operatorname{tr}G_L=\sum_{j\in L}q_j<\frac34.                     \tag{3.6}
\]

Therefore

\[
\lambda_{\max}(G_L)\le\operatorname{tr}G_L<\frac34,
\]

which proves `G_T>(1/4)I_2`; the weak inequalities in (3.3) follow. Equation (3.4) is the two-dimensional Cauchy--Binet identity. QED.

This is stronger than a statement that only finitely many rows are problematic: after all such rows are removed, a quantitatively nondegenerate transverse plane remains.

## 4. Designated partner result applied to an actual new inequality

Whiten the tail plane by

\[
\widetilde B_T=[v_T\ w_T]G_T^{-1/2}.                                \tag{4.1}
\]

Its two columns are orthonormal, so the total squared Pluecker mass of the whitened tail frame is one. Apply the completed account02/B05 source-disjoint Pluecker max-cut result to these actual nonnegative edge weights. There is a partition

\[
T=J\sqcup K                                                        \tag{4.2}
\]

for which

\[
\sum_{j\in J,k\in K}\widetilde b_{jk}^2\ge\frac12.                \tag{4.3}
\]

A two-by-two minor transforms by the determinant of `G_T^{1/2}`:

\[
b_{jk}=v_jw_k-v_kw_j
=\sqrt{\det G_T}\,\widetilde b_{jk}.                               \tag{4.4}
\]

Therefore the partner result gives the **actual original-coordinate tail inequality**

\[
\boxed{
M_{J,K}^{(T)}
:=\sum_{j\in J,k\in K}b_{jk}^2
\ge\frac12\det G_T
\ge\frac1{32}.
}                                                                    \tag{4.5}
\]

This is the required equation-level partner application. It is source-disjoint because `J,K` are disjoint sets of original independent coordinates. No individual edge is selected or inverted.

The newest account02/B05 bank-gap theorem also remains active on any such bank decomposition: whenever the regression-gap currency is `G`, its exact inequality (1.6) forces at least `G` shared-shear residual energy. The result below deliberately bypasses that residual-length/angle issue at the exact rank-two tail endpoint instead of assuming it away.

## 5. New paid branch: exact rank-two longitudinal tail has density at most 24

Define the three-frame tail volume

\[
D_T:=\det\operatorname{Gram}(u_T,v_T,w_T).                           \tag{5.1}
\]

Because `G_T` is positive definite, Schur complementation gives the exact identity

\[
\boxed{
D_T=\det G_T\,
\|u_T-\Pi_{\operatorname{span}\{v_T,w_T\}}u_T\|_2^2.
}                                                                    \tag{5.2}
\]

Thus `D_T=0` if and only if there are real `b,c` such that

\[
u_T=bv_T+cw_T.                                                     \tag{5.3}
\]

### Theorem 5.1 — `QFORM-LONGSPIKE-RANKTWO-TAIL-CLOSURE-v1`

In the live Witt packet (1.1), suppose `L` is the longitudinal-spike set from the residual-heavy dichotomy and the complementary tail satisfies `D_T=0`. Then

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
\le 3\,2^{2/3}\,8^{2/3}S_i^{-1/3}.
}                                                                    \tag{5.4}
\]

Under the target normalization `S_i>=1/2`, this becomes the clean universal bound

\[
\boxed{\|p_Q\|_{\infty,\mathrm{ess}}\le24.}                         \tag{5.5}
\]

#### Proof

Condition only on the literal original spike coordinates `X_L=x_L`. The tail original coordinates remain independent with their original cap-one densities, and the physical hub `H` remains independent of the entire tail.

Put

\[
V=V_T+v_0,\qquad W=W_T+w_0,\qquad U=U_T+u_0,                        \tag{5.6}
\]

where `u_0,v_0,w_0` are deterministic under the conditioning. By (5.3),

\[
U_T=bV_T+cW_T.                                                       \tag{5.7}
\]

Hence, after deterministic translations of `H,V,W`, all dependence on `U_T` is absorbed into the `V^2` and `VW` coefficients. The conditional form has exactly the shape

\[
Q=2a\bar V\,\bar H
  +A\bar V^2+2C\bar V\bar W+\delta\bar W^2+\text{constant},          \tag{5.8}
\]

where `bar H` is still independent of `(bar V,bar W)` and has density cap one.

By the planar product-projection theorem (1.7), the tail pair has conditional joint density cap

\[
K_T\le\frac2{\sqrt{\det G_T}}\le8.                                 \tag{5.9}
\]

Apply Theorem 2.1 with `m=1`, `K=K_T`, and `d=delta`. Uniformly in the conditioned spike values,

\[
\|p_{Q\mid X_L=x_L}\|_{\infty,\mathrm{ess}}
\le3\,2^{2/3}8^{2/3}(a^2|\delta|)^{-1/3}.                           \tag{5.10}
\]

Averaging over the spike coordinates proves (5.4). Finally use `a^2|delta|=S_i>=1/2`:

\[
3\,2^{2/3}\cdot8^{2/3}\cdot2^{1/3}
=3\cdot2^{2/3+2+1/3}=24,                                            \tag{5.11}
\]

which proves (5.5). QED.

### What was actually paid

This is not an easy diagonal subclass. It is the exact shared-source longitudinal-spike endpoint left by the preceding B05 structural dichotomy, under the natural rank-two-tail condition `D_T=0`. The residual variables `(V_T,W_T)` may be arbitrarily dependent; only their genuine original-product planar projection density is used. The shared multiplier `U_T` is allowed to overlap completely with them, provided its coefficient vector lies in their tail plane, which is exactly the rank-two condition.

## 6. Relation to the newest r41 exact-cross theorem and the precise remaining factor

Account03/B05 r41 pays a physical rank-three crossing through quantities such as

\[
D_B=\det\operatorname{Gram}(u_B,v_B,w_B).                            \tag{6.1}
\]

Its bound necessarily deteriorates when such a three-frame volume tends to zero. Theorem 5.1 proves that **the exact zero-volume endpoint itself is benign**: after the finite longitudinal spikes are retained and the transverse tail plane is aggregated, the density is uniformly bounded by `24`.

Therefore a future proof should not invert a three-frame determinant before gluing to the rank-two endpoint. The natural scalar measuring the remaining tail departure from rank two is

\[
\boxed{
\sigma_T^2
:=\|u_T-\Pi_{\operatorname{span}\{v_T,w_T\}}u_T\|^2
=\frac{D_T}{\det G_T}.
}                                                                    \tag{6.2}
\]

Because `det G_T>=1/16`, the only new degeneracy is this **orthogonal shared-shear residual**, not loss of the transverse plane.

The first unpaid implication is now

`QFORM-WITT-RANKTWO-TAIL-GLUE-v1`:

> prove a product-preserving coarea/interval estimate which is uniform as `sigma_T downarrow 0`, interpolating between Theorem 5.1 at `sigma_T=0` and the existing exact-rank-three crossing/diffuse exits when a quantitative three-frame volume is present. The proof must retain the original tail product source and the aggregate tail cross-star `M_{J,K}^{(T)}>=1/32`; it may not condition on the projected residual coordinate, invert one tiny physical Pluecker edge, or replace the tail triple by a generic joint density.

This sharpens the previous missing factor. The longitudinal spikes themselves do not destroy transverse curvature; after they are removed the tail has a planar Gram floor `1/4` and an original-coordinate cross-star at least `1/32`. The remaining difficulty is solely how to spend a nonzero but possibly tiny orthogonal shared-shear residual without losing continuity at the exactly rank-two endpoint.

## 7. Partner control and comparator

The latest designated partner account02/B05 source-disjoint theorem also gives, for genuinely independent cap-one scalars `H,U,V,W`,

\[
Q_\kappa=2V(H+\kappa U)+W^2,
\qquad
\|p_{Q_\kappa}\|_\infty\le4\sqrt2.                                \tag{7.1}
\]

The coefficient matrix has nonzero spectrum

\[
\{1,+\sqrt{1+\kappa^2},-\sqrt{1+\kappa^2}\},                       \tag{7.2}
\]

so this is an actual owner-target family. Theorem 2.1, after replacing `H+kappa U` by the independent scalar convolution `S` with density cap at most one, independently gives the slightly sharper comparator

\[
\|p_{Q_\kappa}\|_\infty
\le3\,2^{2/3}<4.763.                                                  \tag{7.3}
\]

Equation (7.1) is the completed partner result applied to the same target-valid polynomial; (7.3) is a consistency/improvement check for the new receiver, not a claim that the live shared-source problem has become source-disjoint.

## 8. Scope audit

**Proved in this run:** the interpolated independent-hub/joint-planar receiver (2.4); the longitudinal-spike transverse Gram floor (3.3); the tail Pluecker conservation (3.4); partner max-cut application giving an original-coordinate tail cross-star at least `1/32` (4.5); the exact tail-volume identity (5.2); and the target-normalized `<=24` density bound for the exact rank-two longitudinal tail (5.5).

**Not proved:** the `sigma_T>0` glue uniformly as `sigma_T->0`; the whole exact-rank-three survivor; arbitrary higher-rank matrices with additional spectrum; the full owner conjecture; or full-target continuity.

The new theorem proves an essentially bounded density, not continuity. No Monte Carlo evidence is used as proof.