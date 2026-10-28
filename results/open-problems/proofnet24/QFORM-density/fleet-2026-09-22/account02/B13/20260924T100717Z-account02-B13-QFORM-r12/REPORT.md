SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B13, 2026-09-24T10:07:17.305283Z.
attacking: replace convex-hull/interval width by a fragmentation-preserving affine-defect functional in the rank-one-plus-four-diagonal survivor, and close the remaining spectral qualifier with partner r45's explicit pre-bootstrap tail bound.

# account02/B13 r12 — fragmentation-preserving affine defect and explicit spectral gate

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T100717Z-account02-B13-QFORM-r12`  
Role: extremal product laws / complementary constructions and source-valid counterexamples  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING OBSTRUCTION / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**.

No moment, compact-support, log-concavity, connected-support, diagonal-basis, post-rotation-independence, common-diameter, fixed-fragment-count, or attained-bathtub-optimizer assumption is used.

## 1. First unpaid implication

`QFORM-AFFINE-DEFECT-BANK-TO-ROUGH-RECEIVER-v1`:

> In the designated partner's rank-one-plus-four-diagonal endpoint, convert the forced slab-mass-trimmed **quadratic affine defect** on actual fragmented physical product sets into a density payment while retaining both the `O(rho^-1)` separable diagonal tail and the secondary rank-one carrier in the actual phase. Equivalently, rule out or construct a genuine cap-one/finite-union counterexample in which the defect lower bound in (5.7) is paid by remote fragmented supports.

This is narrower and more source-valid than the previous interval-width obligation: convex-hull gaps no longer count as oscillation unless the quadratic phase is genuinely non-affine on the retained support.

## 2. Fresh compatible inputs


The latest completed designated partner is account03/B13 r45, canonical math `a1ccc98be0cd4752de1b2b29e4c46f8193854757`. In the surviving diffuse exact-rank-two chamber it gives

\[
A=D_C+\lambda_1vv^T+E_{\rm sep}+\lambda_2ww^T,
\qquad |C|\le4,
\tag{2.1}
\]
with

\[
E_{\rm sep}=D_{C^c},\qquad
\|E_{\rm sep}\|_{op}\le {C_D\over\rho},
\qquad C_D=2\sqrt{30\pi}=19.41625912555699\ldots,
\tag{2.2}
\]

\[
\|w\|_2=1,
\qquad
|\lambda_2|\le {\sqrt H\over\rho},
\qquad
H=\sqrt{1536e^2},
\qquad
\sqrt H=10.321552950446426\ldots .
\tag{2.3}
\]
The later self-improvement `|lambda_2|=O(rho^-7/6)` is stronger asymptotically but is not needed below.

The previous account02/B13 grouping theorem applies to

\[
M:=D_C+\lambda_1vv^T
\tag{2.4}
\]
whenever `s_3(M)>=1/2`: every affine `M`-form under arbitrary independent cap-one laws has density bounded by

\[
C_M:=500e\,5(8+\log5)
=65302.90114768759\ldots .
\tag{2.5}
\]

## 3. Explicitly close the spectral qualifier

Put

\[
F:=E_{\rm sep}+\lambda_2ww^T,
\qquad A=M+F.
\tag{3.1}
\]
The target assumption is `s_3(A)>=1`. From (2.2)--(2.3),

\[
\|F\|_{op}
\le {C_D+\sqrt H\over\rho}
={29.7378120760034\ldots\over\rho}.
\tag{3.2}
\]
Weyl therefore gives

\[
\boxed{
 s_3(M)\ge1-{C_D+\sqrt H\over\rho}.
}
\tag{3.3}
\]
Consequently

\[
\boxed{
\rho\ge R_{\rm spec}:=2(C_D+\sqrt H)
=59.47562415200683\ldots
\Longrightarrow s_3(M)\ge\frac12.
}
\tag{3.4}
\]
The rough-law theorem below is invoked only for `rho>=4C_M=261211.60459075036...`, so its affine-core hypothesis is automatic. There is no separate high-density `s_3(M)<1/2` side branch in the r45 normal form.

## 4. New general theorem: slab-mass-trimmed affine defect

### Theorem 4.1 — `QFORM-SLAB-MASS-TRIMMED-AFFINE-DEFECT-v1`

Let `X=(X_1,...,X_n)` have independent cap-one probability densities and let `A=M+F` be symmetric. Assume every random variable

\[
X^TMX+b^TX+c
\tag{4.1}
\]
has density at most `C_M`, uniformly in deterministic `b,c`.

Let `J` be an interval of length `ell`, and put

\[
p:=\Pr\{X^TAX\in J\}=\rho\ell.
\tag{4.2}
\]
Choose arbitrary measurable physical-coordinate sets `G_i` satisfying

\[
\eta:=\sum_i\Pr\{X_i\notin G_i\}\le {p\over2},
\qquad G:=\prod_iG_i.
\tag{4.3}
\]
No connectedness, boundedness, or finite-fragment hypothesis is imposed. Define the quadratic affine defect

\[
\Delta_{\rm aff}(F;G)
:=
\inf_{a\in\mathbb R^n,\ c\in\mathbb R}
\operatorname*{ess\,sup}_{x\in G}
\left|x^TFx-a^Tx-c\right|,
\tag{4.4}
\]
where the essential supremum is with respect to the original product law restricted to `G`.

Then

\[
\boxed{
\rho\ell-\eta
\le C_M\bigl(\ell+2\Delta_{\rm aff}(F;G)\bigr).
}
\tag{4.5}
\]
In particular, if `rho>=4C_M`, every family satisfying (4.3) obeys

\[
\boxed{
\Delta_{\rm aff}(F;G)
\ge {\rho\ell\over8C_M}
={p\over8C_M}.
}
\tag{4.6}
\]

### Proof

Fix `a,c` within an arbitrary epsilon of the infimum in (4.4) and write

\[
X^TAX
=
\underbrace{X^TMX+a^TX+c}_{Q_0(X)}
+
\underbrace{(X^TFX-a^TX-c)}_{R(X)}.
\tag{4.7}
\]
The first term is an allowed affine `M`-form. On `G`, `|R|<=Delta_aff+epsilon` almost surely. Hence

\[
\{X^TAX\in J\}\cap G
\subseteq
\{Q_0(X)\in J+[-\Delta_{\rm aff}-\epsilon,\Delta_{\rm aff}+\epsilon]\}.
\tag{4.8}
\]
The union bound gives `P(G^c)<=eta`, so the affine-core density cap yields (4.5) after `epsilon downarrow0`. If `eta<=p/2` and `rho>=4C_M`, then

\[
2C_M\Delta_{\rm aff}
\ge (\rho/2-C_M)\ell
\ge {\rho\ell\over4},
\]
which is (4.6). QED.

The key gain over interval radius is that an arbitrary constant and arbitrary physical linear form are quotiented out before measuring the rough quadratic tail. Remote gaps therefore do not pay merely because their convex hull is large.

## 5. Fragmentation-preserving r45 consequence

For a measurable one-dimensional set `S` define its quadratic Chebyshev defect

\[
\kappa(S)
:=
\inf_{\alpha,\beta\in\mathbb R}
\operatorname*{ess\,sup}_{x\in S}
|x^2-\alpha x-\beta|.
\tag{5.1}
\]
For a product set `G=prod G_i` define similarly

\[
\kappa_w(G)
:=
\inf_{\alpha,\beta\in\mathbb R}
\operatorname*{ess\,sup}_{x\in G}
\left|(w^Tx)^2-\alpha w^Tx-\beta\right|.
\tag{5.2}
\]
Because a sum of coordinatewise affine approximants and an affine function of `w^Tx` is still an affine function of the original physical coordinates,

\[
\Delta_{\rm aff}(F;G)
\le
\sum_{i\notin C}|d_i|\,\kappa(G_i)
+|\lambda_2|\,\kappa_w(G).
\tag{5.3}
\]
Using `|d_i|<=C_D/rho`, (4.6) gives, for every product family with total omitted marginal probability at most `p/2`,

\[
\boxed{
C_D\sum_{i\notin C}\kappa(G_i)
+\rho|\lambda_2|\,\kappa_w(G)
\ge {\rho p\over8C_M}
={\rho^2\ell\over8C_M}.
}
\tag{5.4}
\]
The explicit pre-bootstrap estimate `rho|lambda_2|<=sqrt(H)` makes this completely quantitative:

\[
\boxed{
C_D\sum_{i\notin C}\kappa(G_i)
+\sqrt H\,\kappa_w(G)
\ge {\rho p\over8C_M}.
}
\tag{5.5}
\]
Since `sqrt(H)<C_D`,

\[
\boxed{
\sum_{i\notin C}\kappa(G_i)+\kappa_w(G)
\ge
{\rho p\over 8C_MC_D}
=
{\rho^2\ell\over 10143504.402673082\ldots}.
}
\tag{5.6}
\]
This is the main new obstruction. It is formulated on the **actual retained fragmented sets**, not on their convex hulls.

Define the slab-mass-trimmed defect functional

\[
\mathfrak D_p(F;X)
:=
\inf_{(G_i):\ \sum_iP(X_i\notin G_i)\le p/2}
\Delta_{\rm aff}(F;\prod_iG_i).
\tag{5.7}
\]
Then `rho>=4C_M` implies

\[
\boxed{
\mathfrak D_p(F;X)\ge {p\over8C_M}.
}
\tag{5.8}
\]
No optimizer or attainment is asserted.

### Exact shell check: why this is materially sharper

For

\[
S_R=[R-a,R+a]\cup[-R-a,-R+a],\qquad R>a>0,
\tag{5.9}
\]
symmetry shows the optimal affine slope for approximating `x^2` is zero, and the range of `x^2` is `[(R-a)^2,(R+a)^2]`. Therefore

\[
\boxed{
\kappa(S_R)=\frac{(R+a)^2-(R-a)^2}{2}=2Ra.
}
\tag{5.10}
\]
By contrast, the convex-hull half-width is `R+a`, whose square is order `R^2`. Thus two remote thin fragments pay only their genuine quadratic non-affineness `O(Ra)`, not the empty gap between them. For a single interval `[m-h,m+h]`, one similarly has `kappa=h^2/2` after subtracting the best tangent/constant. This is exactly the geometry required by the role constraint that fragmented supports remain admissible.

## 6. Required pinned Fourier result: real obstruction and endpoint blindness

The owner-pinned source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` was freshly read in `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. Its completed unconditional D5 theorem gives for every disjoint **original-coordinate** physical cross block `B=A[I,J]`

\[
\|p_Q\|_\infty
\le5\sqrt{2e}\,e_5(B^TB)^{-1/10}.
\tag{6.1}
\]
Hence every ratio-`rho` slab witness satisfies the genuine global obstruction

\[
\boxed{
e_5(B^TB)
\le\left({5\sqrt{2e}\over\rho}\right)^{10},
\qquad
s_5(B)\le {5\sqrt{2e}\over\rho}
={11.6582199079856\ldots\over\rho}.
}
\tag{6.2}
\]
This uses no support or moment assumptions and no rotated product law.

In the exact-rank-two r45 endpoint, however, every off-diagonal physical cross block is the sum of the two rank-one carriers `lambda_1 v_Iv_J^T+lambda_2 w_Iw_J^T`; diagonal pieces contribute nothing across a cut. Thus `rank B<=2` and `e_5(B^TB)=0` identically. The D5 theorem is therefore **structurally blind at precisely this endpoint**. Equation (6.2) is a real obstruction for the general survivor before exact-rank-two collapse, while (5.4)--(5.8) target the complementary chamber D5 cannot see.

The numerical counterexample search in the pinned source reports no growing tested family, but no numerical result is used as proof here.

## 7. Extremal-product interface

Theorem 4.1 already holds for arbitrary cap-one product laws, including unbounded and infinitely fragmented marginals. For complementary construction work, the completed optimizer-free purification may still transfer a strict violation with arbitrarily small loss to finite convex mixtures of indicators of bounded finite unions of total measure one. No centered interval, bounded diameter, common support window, fixed fragment count, or attained global bathtub optimizer is inferred.

The new defect formulation is deliberately compatible with that reduction: the retained sets `G_i` may themselves be fragmented, and empty gaps are quotiented out to the extent that the rough quadratic is affine across the retained product support.

## 8. What remains

The spectral qualifier in the r45 core receiver is now explicitly closed by (3.4), and interval/convex-hull width has been replaced by the stronger fragmentation-preserving affine defect (4.4). The surviving obstacle is therefore sharply stated: a putative divergent-density sequence must force large non-affineness of the small separable/secondary quadratic tail on every product set retaining all but half of the actual bad-slab marginal tail budget. Paying that defect by a product-preserving oscillatory receiver, or realizing it in a genuine counterexample sequence, is the next mathematical target.
