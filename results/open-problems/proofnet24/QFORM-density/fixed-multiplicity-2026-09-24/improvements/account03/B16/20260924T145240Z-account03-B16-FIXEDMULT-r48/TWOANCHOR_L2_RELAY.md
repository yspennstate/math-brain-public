# account03/B16 — two-anchor joint-L2 relay and the multiplicity-eight endpoint

Run: `20260924T145240Z-account03-B16-FIXEDMULT-r48`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Execution/memory status: **WITHOUT_VERIFIED_BRAIN**.  
Pinned baseline manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

Status: **new proved supporting theorem and a sharper reduction of the open multiplicity-eight endpoint; no multiplicity-eight theorem is claimed.** The unrestricted three-eigenvalue conjecture remains open.

## 1. Main theorem: `QFORM-TWOANCHOR-JOINT-L2-RELAY-v1`

Let `X=(X_1,X_2)` be independent of a random pair `(L,R) in R^2 x R`. Assume `X_1,X_2` have probability densities `f_1,f_2`, and put

\[
\kappa_X:=\bigl(\|f_1\|_2^2\|f_2\|_2^2\bigr)^{1/2}.
\]

Let `B=B^T` be an arbitrary real `2 x 2` matrix and define

\[
Q=X^T B X+2X\cdot L+R.
\tag{1.1}
\]

Assume the joint law of `(L,R)` has a density `h(l,r)` in `L^2(R^3)`, with

\[
H:=\|h\|_2<\infty.
\]

Then `Q` has a continuous `C_0` density and

\[
\boxed{
\|p_Q\|_\infty
\le 3\,2^{-2/3}(\kappa_X H)^{2/3}.
}
\tag{1.2}
\]

In particular, if `0<=f_i<=1`, then `\kappa_X<=1` and

\[
\boxed{
\|p_Q\|_\infty
\le 3\,2^{-2/3}\,\|h\|_2^{2/3}.
}
\tag{1.3}
\]

The estimate is completely uniform in the two-anchor self matrix `B`; no factor involving `det B`, `||B||`, its sign, or its rank occurs.

### Proof

For `t != 0`, define the two-anchor oscillatory transform

\[
A_t(l)=\int_{\mathbb R^2}
 f_1(x_1)f_2(x_2)
 e^{it(x^T Bx+2l\cdot x)}\,dx.
\tag{1.4}
\]

Write

\[
g_t(l)=\int_{\mathbb R}e^{itr}h(l,r)\,dr.
\tag{1.5}
\]

Independence of `X` from `(L,R)` gives

\[
\phi_Q(t)=\int_{\mathbb R^2}A_t(l)g_t(l)\,dl.
\tag{1.6}
\]

The crucial point is that the quadratic phase `x^T Bx` has modulus one and therefore disappears from the exact Plancherel norm in the **linear-frequency variable** `l`. With the Fourier convention `\widehat u(\xi)=\int e^{i\xi\cdot x}u(x)dx`, put

\[
u_t(x)=f_1(x_1)f_2(x_2)e^{itx^TBx}.
\]

Then `A_t(l)=\widehat u_t(2tl)`, so two-dimensional Plancherel and the change of variables `xi=2tl` give

\[
\begin{aligned}
\|A_t\|_2^2
&={1\over 4t^2}\int_{\mathbb R^2}|\widehat u_t(\xi)|^2d\xi\\
&={\pi^2\over t^2}\int_{\mathbb R^2}f_1(x_1)^2f_2(x_2)^2dx\\
&={\pi^2\kappa_X^2\over t^2}.
\end{aligned}
\tag{1.7}
\]

Hence Cauchy--Schwarz gives

\[
|\phi_Q(t)|\le {\pi\kappa_X\over |t|}\,\|g_t\|_2.
\tag{1.8}
\]

A second, one-dimensional Plancherel identity, now in the output variable `r`, yields

\[
\int_{\mathbb R}\|g_t\|_2^2dt
=2\pi\|h\|_2^2
=2\pi H^2.
\tag{1.9}
\]

For any `tau>0`, use `|phi_Q|<=1` on `|t|<=tau` and (1.8)--(1.9) outside:

\[
\begin{aligned}
\|\phi_Q\|_1
&\le 2\tau
+\pi\kappa_X
 \left(\int_{|t|>\tau}t^{-2}dt\right)^{1/2}
 \left(\int_{\mathbb R}\|g_t\|_2^2dt\right)^{1/2}\\
&\le 2\tau+2\pi\sqrt\pi\,\kappa_XH\,\tau^{-1/2}.
\end{aligned}
\tag{1.10}
\]

The right side is minimized at

\[
\tau=\left({\pi\sqrt\pi\,\kappa_XH\over2}\right)^{2/3},
\]

and the minimum is

\[
\|\phi_Q\|_1
\le 3\,2^{1/3}\pi(\kappa_XH)^{2/3}.
\tag{1.11}
\]

Fourier inversion therefore gives a continuous density vanishing at infinity and

\[
\|p_Q\|_\infty
\le {1\over2\pi}\|\phi_Q\|_1
\le3\,2^{-2/3}(\kappa_XH)^{2/3}.
\]

This proves (1.2). If `f_i<=1`, then `\int f_i^2<=\int f_i=1`, so `\kappa_X<=1`, proving (1.3). QED.

### Why this is correction-safe

This is an integrated Fourier estimate, not a pointwise van-der-Corput assertion for a rough quadratic phase. It never rotates `X` and never assumes independence of spectral coordinates. The only independence used is the literal original two-coordinate bank `X` versus the outside variables producing `(L,R)`. The nonlinear self-curvature `B` is kept exactly throughout.

The theorem is also deliberately weaker than an arbitrary-joint coarea statement: it asks for one concrete `L^2` joint-density norm of `(L,R)`. That norm is the remaining object to control in the terminal application below.

## 2. Exact structural reduction in the current multiplicity-eight collar

Use the completed account03/B15 terminal collapse. In the unresolved normalized no-pivot `s_8(A)>=1` branch there is a literal physical two-set `H` such that, writing the matrix in the original-coordinate block form

\[
A=
\begin{pmatrix}
B&C\\ C^T&D
\end{pmatrix},
\qquad |H|=2,
\tag{2.1}
\]

one has

\[
\det(CC^T)\ge {\delta_*^2\over2}
=0.36494426588270207\ldots,
\tag{2.2}
\]

and

\[
\|B\|_{op}<0.110499,
\qquad
\delta_*=0.854335140191133771\ldots.
\tag{2.3}
\]

The exact-zero subchamber `B=0` was already paid there. The following additional fact is immediate but important for the nonzero weak-self endpoint.

### Lemma `QFORM-S8-STRONGPAIR-OUTSIDE-S4-v1`

For every block decomposition (2.1), regardless of the size or sign of `B` and regardless of (2.2),

\[
\boxed{s_8(A)\ge1\quad\Longrightarrow\quad s_4(D)\ge1.}
\tag{2.4}
\]

#### Proof

Set

\[
K=
\begin{pmatrix}
B&C\\ C^T&0
\end{pmatrix},
\qquad
A_0=
\begin{pmatrix}
0&0\\0&D
\end{pmatrix}.
\]

The range of `K` is contained in `R^2 direct_sum ran(C^T)`, so

\[
\operatorname{rank}K\le 2+\operatorname{rank}C\le4.
\]

Since `A=A_0+K`, the rank-shift singular-value inequality gives

\[
s_8(A)\le s_4(A_0)=s_4(D).
\]

Thus (2.4) follows. QED.

This shows that the weak self block cannot be blamed for consuming all residual curvature: after removing the entire two-anchor star, four unit-scale singular directions remain in the literal outside quadratic matrix.

## 3. A clean sufficient condition that would close multiplicity eight

Write the full affine quadratic polynomial relative to the pair `H` as

\[
Q=X_H^TBX_H+2X_H\cdot(CY+b_H/2)
 +\bigl(Y^TDY+b_{H^c}^TY+c\bigr).
\tag{3.1}
\]

Define the three-dimensional outside statistic

\[
\mathcal Z=
\left(
CY+b_H/2,
\;Y^TDY+b_{H^c}^TY+c
\right)\in\mathbb R^3.
\tag{3.2}
\]

If its density `h_H` obeys a universal terminal bound

\[
\boxed{\|h_H\|_2\le H_0,}
\tag{3.3}
\]

then Theorem (1.3) immediately gives

\[
\boxed{
\|p_Q\|_\infty\le3\,2^{-2/3}H_0^{2/3},
\qquad p_Q\in C_0(\mathbb R),
}
\tag{3.4}
\]

with **no dependence at all on `det B`**. Thus the current multiplicity-eight endpoint can be reformulated as the following concrete joint-smoothing problem:

### `QFORM-S8-STRONGCROSS-S4-JOINTL2-v1` — OPEN

For arbitrary independent cap-one coordinates `Y`, prove a dimension-free `L^2(R^3)` density bound for

\[
(CY+u,\;Y^TDY+v^TY+w)
\tag{3.5}
\]

under the terminal quantitative conditions

\[
\det(CC^T)\ge0.3649442658\ldots,
\qquad
s_4(D)\ge1,
\tag{3.6}
\]

with the additional no-pivot structure inherited from the terminal branch available if needed.

A proof of this `L^2` statement would close the remaining no-pivot `s_8` branch and, together with the already-paid pivot branches, yield the eight-eigenvalue theorem. This report does **not** claim (3.5)--(3.6) has been proved.

The reformulation is materially different from the previously blocked approaches:

- it does not ask for an `L^infinity` conditional density on the fibers `CY=l`;
- it does not take a fiber supremum;
- it does not require a pointwise quadratic-phase decay estimate;
- and it does not divide by `sqrt(|det B|)`.

The endpoint is now an integrated three-dimensional `L^2` projection/quadratic pushforward estimate.

## 4. A transverse-fiber rank fact when the weak self block is invertible

There is an additional exact identity useful for attacking (3.5). Suppose `B` is invertible and let

\[
S=D-C^TB^{-1}C
\]

be its Schur complement. The manuscript's Schur count gives `s_6(S)>=1` from `s_8(A)>=1`. Let `P` be the orthogonal projection in the outside coordinate space onto `row(C)`; (2.2) makes `rank P=2`. Then

\[
(I-P)S(I-P)=(I-P)D(I-P),
\tag{4.1}
\]

because `C(I-P)=0`. Moreover

\[
S-(I-P)S(I-P)=PS+(I-P)SP
\]

has rank at most four. A second rank shift therefore gives

\[
\boxed{
 s_2\bigl((I-P)D(I-P)\bigr)
 =s_2\bigl((I-P)S(I-P)\bigr)
 \ge1.
}
\tag{4.2}
\]

Thus in the invertible weak-self chamber the affine fibers of the strong two-dimensional projection `CY` retain two unit-scale quadratic Hessian directions. This does not by itself prove a conditional density cap, because conditioning a rough product law on a rotated projection can concentrate. It does, however, identify the exact geometric resource that an `L^2` proof of (3.5) should consume.

Notice that (4.2) is uniform as `det B -> 0`: the potentially huge rank-two Schur term is annihilated on `ker C`. This is why an `L^2` joint-pushforward route is better adapted to the weak-self limit than the old `1/sqrt(|det B|)` pair profile.

## 5. Strict target family paid uniformly through arbitrary weak self-curvature

The relay gives a concrete target-level theorem which is not available from a `det B` denominator.

Let

- `X=(X_1,X_2)`, `Y=(Y_1,Y_2)`, and `Z_1,...,Z_4` be mutually independent cap-one original coordinates;
- `B=B^T` be arbitrary with `||B||_op<=1/2`;
- and

\[
Q_B=X^TBX+4X\cdot Y+\sum_{j=1}^4 Z_j^2.
\tag{5.1}
\]

Here `L=2Y`. Its density satisfies

\[
\|p_L\|_2\le\frac12.
\tag{5.2}
\]

Indeed `p_L(l)=\frac14f_{Y_1}(l_1/2)f_{Y_2}(l_2/2)` and `\int f_{Y_i}^2<=1`.

For

\[
R=\sum_{j=1}^4Z_j^2,
\]

the first two squares already have density cap at most `pi`: each square density is bounded by `u^{-1/2}1_{u>0}`, whose self-convolution is exactly `pi`; convolution with the remaining two square laws cannot increase the `L^infinity` norm. Hence

\[
\|p_R\|_2\le\sqrt\pi.
\tag{5.3}
\]

Since `L` and `R` are independent, their joint density has

\[
H=\|p_Lp_R\|_2\le{\sqrt\pi\over2}.
\tag{5.4}
\]

The relay therefore yields

\[
\boxed{
\|p_{Q_B}\|_\infty
\le {3\pi^{1/3}\over2^{4/3}}
=1.743671027264439\ldots,
\qquad p_{Q_B}\in C_0(\mathbb R).
}
\tag{5.5}
\]

This estimate is uniform over all symmetric `B` with `||B||<=1/2`, including definite, indefinite, singular and arbitrarily small-determinant matrices.

It is a strict eight-direction target family. The `X,Y` carrier matrix is

\[
M_B=
\begin{pmatrix}
B&2I_2\\2I_2&0
\end{pmatrix}.
\tag{5.6}
\]

At `B=0` its eigenvalues are `2,2,-2,-2`. Weyl perturbation by `diag(B,0)` of norm at most `1/2` leaves two eigenvalues at least `3/2` and two at most `-3/2`. The four independent `Z_j^2` directions add four eigenvalues exactly `1`. Hence the full coefficient matrix of (5.1) has at least eight eigenvalues of modulus at least one.

## 6. Designated account04/B16 result applied to the same actual inequality

The completed account04/B16 theorem `QFORM-PROJECTIONPRODUCT-DEFINITE-OR-PHASEALIGNED-EXIT-v1` proves that a definite two-dimensional projected quadratic plane with matrix `H` gives

\[
\|p_Q\|_\infty\le {2\pi\over\sqrt{|\det H|}}
\tag{6.1}
\]

after conditioning on all disjoint original-coordinate banks.

Apply it to (5.1), conditioning on every variable except `(Z_1,Z_2)`. Their quadratic matrix is `I_2`, so the partner result gives the actual strict-target inequality

\[
\boxed{\|p_{Q_B}\|_\infty\le2\pi.}
\tag{6.2}
\]

The new relay (5.5) is stronger on this family and, unlike a definite-plane argument, directly demonstrates the intended two-anchor projection-product mechanism. The partner application is retained as an independent valid bound rather than used as a premise for (1.2).

Partner source: `proofnet24/QFORM-density/fleet-2026-09-22/account04/B16/20260924T041516Z-account04-B16-QFORM-r4/REPORT.md`, blob `6373fddaeb3206e86af61fc7b48eeb6f39e34666`.

## 7. What changed mathematically

The preceding multiplicity-eight endpoint was described as a **strong-cross / weak-self two-anchor receiver** problem. The relay above removes the weak self matrix itself from the analytic denominator: once the three-dimensional outside statistic has a uniform `L^2` density, the whole pair is paid with a constant independent of `B` and automatically gains `C_0` regularity.

Combined with the new rank fact (2.4), the first missing implication is now:

> **strong two-dimensional physical cross map + four unit outside singular directions -> uniform `L^2` density of one linear-linear-quadratic outside statistic.**

The invertible subchamber has the sharper transverse-fiber certificate (4.2): two unit Hessian directions survive on `ker C` itself. A successful proof should exploit this in an integrated `L^2`/Plancherel manner, not by a conditional fiber supremum.

## 8. Exact scope

- Pinned seventeen-eigenvalue manuscript: separately audited in the sibling audit report for this run; source unchanged.
- Nine-eigenvalue candidate: already reconstructed by this B16 lineage; independent release/validation remains a separate owner gate.
- `QFORM-TWOANCHOR-JOINT-L2-RELAY-v1`: **PROVED**.
- `QFORM-S8-STRONGPAIR-OUTSIDE-S4-v1`: **PROVED**.
- Invertible-pair transverse fiber estimate (4.2): **PROVED**.
- Strict `s_8` family (5.1): **PROVED**, with continuous density height `<1.744`.
- General multiplicity-eight theorem: **OPEN**; it is reduced here to the joint-`L^2` implication (3.5)--(3.6) in the remaining terminal collar.
- Full three-eigenvalue conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.
- No Gaussian, log-concavity, moment, compact-support, connected-support, diagonal-basis, post-rotation independence, arbitrary-joint coarea, or pointwise rough quadratic-phase decay assumption is introduced.
