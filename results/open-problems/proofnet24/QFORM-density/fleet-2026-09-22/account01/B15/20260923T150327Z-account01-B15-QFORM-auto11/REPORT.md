SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B15, 2026-09-23T15:03:27Z.
attacking: soft weighted majority residual compiler and fixed-scale physical-sheet stability under matrix perturbations.

# Status

Classification: `ESSENTIAL_STEP_APPLIED / SOFT-MAJORITY-RESIDUAL-COMPILER / SHEET-TENT-STABILITY`.

Full QFORM remains OPEN. Raw continuity remains a separate stronger issue and is not used below. The live corrections remain in force: no law-uniform pointwise quadratic Fourier decay, no rotated-independence assumption, and no projection/X-ray-only shortcut.


## 1. Partner input

For an invertible indefinite ORIGINAL-coordinate physical triple `S`, let `B=A_{S,S}` and let `G_S` be the conditional majority/one-sheet event after conditioning on the outside original coordinates. The completed account02/B15 theorem gives the output submeasure

\[
\mu_S^+(E):=\Pr\{Q\in E,\,G_S\}\le C_S|E|,
\qquad
C_S\le \frac{\pi\sqrt2}{\kappa_S},
\quad \kappa_S=\sigma_{\min}(B).
\]

This allows arbitrary outside quadratic terms and cross-couplings and uses no post-rotation independence.

## 2. Soft fractional-majority residual compiler

Take a finite bank `T` of such triples and arbitrary weights `a_S>=0`. Put

\[
R(X):=\sum_{S\in\mathcal T}a_S\mathbf 1_{G_S}(X),
\qquad
\beta_\delta(E):=\Pr\{Q\in E,\ R(X)<\delta\}.
\]

The pointwise inequality

\[
1\le \mathbf1_{\{R<\delta\}}+\frac{R}{\delta}
\]

gives, for every Borel `E`,

\[
\mu_Q(E)
\le \beta_\delta(E)+\frac1\delta\sum_Sa_S\mu_S^+(E)
\le \beta_\delta(E)+\frac1\delta\Big(\sum_Sa_SC_S\Big)|E|.
\]

Therefore, as an extended-real inequality,

\[
\boxed{
D_\infty(\mu_Q)
\le D_\infty(\beta_\delta)
+\frac1\delta\sum_Sa_SC_S.
}
\]

More generally, for every nonnegative probability kernel `K`,

\[
\boxed{
(K*\mu_Q)(y)
\le (K*\beta_\delta)(y)
+\frac1\delta\sum_Sa_SC_S.
}
\]

In particular, for the exact fixed-unit tent normal form `K_1(x)=(1-|x|)_+`,

\[
\boxed{
s_3(A)\|K_1*\mu_Q\|_\infty
\le
s_3(A)\|K_1*\beta_\delta\|_\infty
+\frac{s_3(A)}{\delta}\sum_Sa_SC_S.
}
\]

This is useful because deterministic full cone coverage is not needed: one pays all majority sheets in aggregate and isolates a residual carried by points where the cost-efficient physical triples are predominantly on their minority/two-sheet sides.

### Harmonic/coarse corollary

Choose

\[
a_S=\frac{\kappa_S}{\sum_T\kappa_T}.
\]

Using the partner estimate,

\[
\sum_Sa_SC_S
\le
\frac{\pi\sqrt2\,N}{\sum_S\kappa_S}.
\]

Hence if

\[
\frac1N\sum_S\kappa_S\ge c\,s_3(A),
\]

then

\[
\boxed{
s_3(A)\|K_1*\mu_Q\|_\infty
\le
s_3(A)\|K_1*\beta_\delta\|_\infty
+\frac{\pi\sqrt2}{c\delta}.
}
\]

This is an explicit aggregate-before-inversion certificate. The remaining work in this branch is now exactly to control the low-weighted-majority residual by an original-product minority/ridge/volume/grouped-coordinate argument.

## 3. Algebraic form of the physical majority sheet

For the same triple write

\[
A=\begin{pmatrix}B&E\\E^\top&F\end{pmatrix},\qquad x=(u,w),\qquad g_A(x)=2Ax.
\]

The conditional critical value after completing the square is

\[
c_S(w)=w^\top(F-E^\top B^{-1}E)w.
\]

Then

\[
Q-c_S(w)=\frac14 g_{A,S}^\top B^{-1}g_{A,S}
=\frac{1}{4\det B}g_{A,S}^\top\operatorname{adj}(B)g_{A,S}.
\]

For BOTH indefinite signatures `(2,1)` and `(1,2)`, the majority/one-sheet condition is therefore exactly

\[
\boxed{
G_{A,S}
=
\left\{
F_{A,S}(x):=
 g_{A,S}(x)^\top\operatorname{adj}(B)g_{A,S}(x)
\le0
\right\}.
}
\]

The sign check is important: when `det B<0` the majority side is `Q-c>=0`; when `det B>0` the majority side is `Q-c<=0`; both reduce to `F_{A,S}<=0`.

## 4. Boundary of a physical sheet is source-null

Assume the full input law is absolutely continuous. Then

\[
\Pr\{F_{A,S}(X)=0\}=0.
\]

Proof: fix the outside coordinate `w`. The map

\[
u\mapsto v=Bu+Ew
\]

is an invertible affine map because `B` is invertible. In the `v` variable,

\[
F_{A,S}=4v^\top\operatorname{adj}(B)v.
\]

Since `adj(B)` is invertible, this is a nonzero quadratic polynomial on `R^3`; its zero set has three-dimensional Lebesgue measure zero. Fubini in `w` proves the claim.

This null-boundary fact is the key regularity input below and uses only original coordinates.

## 5. Moment-free fixed-tent stability under matrix perturbation

Let `A_m -> A` coefficientwise. Fix an original-coordinate triple `S` for which `B=A_{S,S}` is invertible indefinite. Then for all sufficiently large `m`, `B_m=(A_m)_{S,S}` has the same inertia and is invertible. Define `Q_m`, `F_m=F_{A_m,S}`, and `G_m={F_m<=0}`.

For every fixed `x`,

\[
Q_m(x)\to Q(x),\qquad F_m(x)\to F(x).
\]

Since `P(F(X)=0)=0`,

\[
\mathbf1_{G_m}(X)\to\mathbf1_G(X)\qquad a.s.
\]

Let `tau(t)=(1-|t|)_+` and

\[
T_{m,S}(y)=E[\tau(Q_m-y)\mathbf1_{G_m}],
\qquad
T_S(y)=E[\tau(Q-y)\mathbf1_G].
\]

Using `0<=tau<=1` and `Lip(tau)=1`, uniformly in `y`,

\[
\begin{aligned}
|T_{m,S}(y)-T_S(y)|
&\le E|\tau(Q_m-y)-\tau(Q-y)|+P(G_m\triangle G)\\
&\le E\min\{1,|Q_m-Q|\}+P(G_m\triangle G).
\end{aligned}
\]

Both terms tend to zero by bounded convergence. Hence

\[
\boxed{
\sup_y|T_{m,S}(y)-T_S(y)|\to0.
}
\]

No moment of `X` is required. This is deliberately a FIXED-SCALE statement; it does not contradict the completed shrinking-scale obstruction.

## 6. Finite-bank residual stability

For a fixed finite bank and weights `a_S`, define

\[
R_m=\sum_Sa_S\mathbf1_{G_{m,S}},\qquad R=\sum_Sa_S\mathbf1_{G_S}.
\]

Then `R_m -> R` a.s. If `delta` is chosen outside the finite set of subset sums of the weights `{a_S}`, then `R(X) != delta` for every `X`, and therefore

\[
\mathbf1_{\{R_m<\delta\}}\to \mathbf1_{\{R<\delta\}}
\quad a.s.
\]

For the residual fixed-tent profile

\[
H_{m,\delta}(y)
=E[\tau(Q_m-y)\mathbf1_{\{R_m<\delta\}}],
\]

the same bounded/Lipschitz argument yields

\[
\boxed{
\sup_y|H_{m,\delta}(y)-H_\delta(y)|\to0.
}
\]

Thus the exact residual compiler is stable under coefficientwise matrix approximation without moments, provided the selected limiting physical blocks stay invertible indefinite. This gives a safe generic-approximation interface for a FIXED bank. It does not solve a sequence in which the relevant minors themselves become singular.

## 7. Regularity ledger

Qualitative absolute continuity remains much easier than the owner target: any nonzero symmetric `A` and any absolutely continuous full joint input law give an absolutely continuous law of `X^TAX` by coarea away from `ker A`.

Universal bounded density is the genuinely quantitative statement and is exactly equivalent, by the already established spectral-homogeneity argument, to a uniform fixed-unit tent bound.

Raw continuity is stronger and separate. The fixed-tent stability above is not a continuity theorem for the raw density and is not a desmoothing estimate.

## 8. What is still unpaid

The new compiler reduces one branch to a sharp dichotomy. If a bank has nondegenerate mean physical conditioning, the majority contribution costs a universal constant after harmonic weighting. A counterexample sequence must then have a large fixed-tent trace in the residual where weighted majority coverage is small, i.e. where most cost-efficient original-coordinate triples are simultaneously on their minority/two-sheet sides. The next target is to show that this residual necessarily satisfies one of the existing product-preserving ridge/volume/grouped-coordinate certificates, or to bound its tent trace directly.

Near-singular banks remain the structural obstruction; this report does not claim QFORM solved.

Execution context: `WITHOUT_VERIFIED_BRAIN`.
