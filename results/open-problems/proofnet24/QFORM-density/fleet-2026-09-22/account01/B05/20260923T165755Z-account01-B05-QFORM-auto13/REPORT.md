SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B05, 2026-09-23T16:57:55Z.
attacking: the punctured heavy near-null bridge after arbitrary-pivot mixed-support absorption; replace the vanishing moving-slope triple by a complementary uniformly transverse triple and locate the exact fiber-mass loss.

# account01/B05 auto13 — complementary moving-slope coordinates, uniform fiber determinant, and the source-adapted mass-refund obstruction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Quadratic coarea / equivalent interval bound preserving arbitrary product densities  
**Run:** `20260923T165755Z-account01-B05-QFORM-auto13`  
**Status:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_STRUCTURAL_THEOREM_PROVED / DESIGNATED_PARTNER_APPLIED / PRECISE_MISSING_FACTOR_IDENTIFIED / FULL_QFORM_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** no new unrestricted continuity claim is made here; the full-target continuity question remains open.

The full conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. This report is an exact-rank-three heavy-row reduction. It does not silently extend to arbitrary higher-rank Schur remainders. No moment, compact-support, connected-support, log-concavity, iid, diagonal-basis, post-rotation-independence, conditional-density-cap, or law-uniform pointwise van-der-Corput hypothesis is introduced.

Fresh control at the start remained OWNER CONTROL revision `2026-09-22.15`, QFORM-only. The live correction that arbitrary-joint three-dimensional coarea and positive conditional projection-height moments are false is retained throughout.

## 1. Source state and immediate predecessor

The preceding account01/B05 theorem is

`QFORM-ARBITRARY-PIVOT-MIXED-SUPPORT-ABSORPTION-v1`,

canonical mathematics

`yspennstate/math-open-problems@118a74200ff58a869f7e4f81d93d5da45ecd7d8d`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B05/20260923T160511Z-account01-B05-QFORM-auto12/REPORT.md`.

It shows that every residual longitudinal coefficient carried on an original coordinate with zero transverse coefficient can be absorbed exactly into a synthetic cap-one hub. Thus the only genuinely unpaid leakage is same-coordinate mixed leakage. In its notation the exact endpoint `rho_M=0` is already paid, and the punctured branch can be pruned to a graph-small mixed-support state without losing active spectral scale.

The freshest completed designated-partner account02/B05 report used here is

`yspennstate/math-open-problems@040cd52d6a6e19c4e00080876babd39aaf07413c`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260923T160925Z-account02-B05-QFORM-d5159a85/REPORT.md`.

It identifies the heavy near-null normal form, the moving slope, the exact determinant cancellation, and the obstruction to repairing the full three-square absolute-Fourier argument by any law-uniform `L^p` Fourier estimate with `p<2`.

For the quantitative fiber estimate below I apply account02/B05's completed theorem

`QFORM-NEARNULL-SCALAR-DEPENDENT-PAIR-v1`,

canonical source

`yspennstate/math-open-problems@c661893c05a7fd40d7f1e9b0a0a81a6f08f242a6`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260923T035943Z-account02-B05-QFORM-r21/REPORT.md`.

That theorem states: if a cap-one scalar `X` is independent of a two-dimensional pair `(C,D)` having joint density cap `M`, and

`q=aX^2+2 beta XC+alpha C^2+2 delta CD+gamma D^2`

has `beta!=0`, `gamma!=0` and invertible coefficient matrix `B`, then

`||p_q||_infinity <=31 M^(2/3)|beta^2 gamma det B|^(-1/6)`.

No independence inside `(C,D)` is required.

The standard product-projection input used below is the source-pinned Livshyts--Paouris--Pivovarov bound already in the QFORM record: an `r`-dimensional orthogonal projection of an original-coordinate product density with factors at most one has density at most `2^(r/2)`.

## 2. Partner near-null normal form

Work in the exact-rank-three branch

`A=R M R^T`, `R^T R=I_3`, `s_min(M)>=1`,

with an original physical hub `0` of leverage

`c=||r_0||^2>1/2`, `rho=1-c`.

Rotate only the deterministic active coefficient basis so that `r_0=sqrt(c)e_1`, and align the coupling arm in `e_1^perp`. Then

\[
M=
\begin{pmatrix}
\eta&b&0\\
b&\alpha&\delta\\
0&\delta&\gamma
\end{pmatrix}.
\tag{2.1}
\]

For the residual original-coordinate product bank write

`u=sqrt(rho) xi`,

where `xi,v,w` are orthonormal coefficient vectors, and put

\[
T=\xi\cdot X,\qquad V=v\cdot X,\qquad W=w\cdot X,
\qquad S=\sqrt c X_0+\sqrt\rho T.
\tag{2.2}
\]

Then

\[
Q=\eta S^2+2bSV+\alpha V^2+2\delta VW+\gamma W^2.
\tag{2.3}
\]

The only immediate independence is `X_0` from the whole residual original-coordinate bank. In particular, `T,V,W` are generally dependent.

The genuine near-null collar will mean

\[
0<|\eta|\le {1\over2}.
\tag{2.4}
\]

Since `s_min(M)>=1`,

\[
\eta^2+b^2=\|Me_1\|^2\ge1,
\]

so

\[
\boxed{|b|\ge\sqrt3/2.}
\tag{2.5}
\]

## 3. First exact cancellation: the root discriminant forgets the longitudinal innovation

Define the partner moving slope

\[
L=\eta\sqrt\rho\,T+bV.
\tag{3.1}
\]

Expanding (2.3) in the physical hub gives

\[
Q=c\eta X_0^2+2\sqrt c\,L X_0+H(T,V,W),
\tag{3.2}
\]

where

\[
H=\eta\rho T^2+2b\sqrt\rho TV+\alpha V^2+2\delta VW+\gamma W^2.
\tag{3.3}
\]

Fix an output level `s`. For a conditional root in `X_0`, the squared half-derivative is

\[
(c\eta X_0+\sqrt c L)^2
=c\,\Delta_s(T,V,W),
\tag{3.4}
\]

where

\[
\Delta_s=L^2+\eta(s-H).
\tag{3.5}
\]

The `T^2` and `TV` terms cancel **exactly**:

\[
\boxed{
\Delta_s(V,W)
=\eta s+(b^2-\eta\alpha)V^2
-2\eta\delta VW-\eta\gamma W^2.
}
\tag{3.6}
\]

Thus the reciprocal-gradient singularity is purely transverse. The same-source longitudinal variable survives only inside the location at which the physical hub density is sampled.

Writing

\[
N_\eta=
\begin{pmatrix}
b^2-\eta\alpha&-\eta\delta\\
-\eta\delta&-\eta\gamma
\end{pmatrix},
\tag{3.7}
\]

one has the exact determinant identity

\[
\boxed{\det N_\eta=\eta\det M.}
\tag{3.8}
\]

For `Delta_s>0`, the two conditional roots are

\[
\boxed{
X_{0,\pm}
=-\sqrt{\rho/c}\,T
+{-bV\pm\sqrt{\Delta_s(V,W)}\over\sqrt c\,\eta}.
}
\tag{3.9}
\]

Consequently the exact density formula, whenever written through conditional roots, has the structure

\[
p_Q(s)
={1\over2\sqrt c}
\sum_{\pm}
\mathbb E\left[
 {f_0\!\left(-\sqrt{\rho/c}\,T+\Psi_{\pm,s}(V,W)\right)
  \mathbf 1_{\{\Delta_s>0\}}
 \over\sqrt{\Delta_s(V,W)}}
\right],
\tag{3.10}
\]

with

\[
\Psi_{\pm,s}(v,w)
={-bv\pm\sqrt{\Delta_s(v,w)}\over\sqrt c\,\eta}.
\tag{3.11}
\]

Formula (3.10) is the exact source-adapted object which must be controlled. Replacing `f_0` by its cap `1` loses the only information involving `T` and leaves the rank-two half-Riesz scale `|eta det M|^(-1/4)`, which diverges at the null limit. This is a proof-interface loss, not a counterexample.

## 4. New complementary moving-slope coordinates

The partner report emphasizes that the triple `(L,V,W)` has volume

\[
|\eta|\sqrt\rho,
\]

which vanishes at the near-null endpoint. There is, however, an exact complementary triple with no such degeneration.

Use `(T,L,W)` instead. Relative to the orthonormal residual frame `(T,V,W)`,

\[
\begin{pmatrix}T\\L\\W\end{pmatrix}
=
\begin{pmatrix}
1&0&0\\
\eta\sqrt\rho&b&0\\
0&0&1
\end{pmatrix}
\begin{pmatrix}T\\V\\W\end{pmatrix},
\tag{4.1}
\]

hence

\[
\boxed{|\det \partial(T,L,W)/\partial(T,V,W)|=|b|\ge\sqrt3/2.}
\tag{4.2}
\]

Thus the vanishing `|eta|sqrt(rho)` projection volume is not an unavoidable three-dimensional projection loss; it depends on which third linear coordinate is retained.

Solving

\[
V={L-\eta\sqrt\rho T\over b}
\tag{4.3}
\]

and defining

\[
\theta={b^2-\eta\alpha\over b^2},
\tag{4.4}
\]

one obtains the exact identity

\[
\boxed{
\begin{aligned}
Q={}&c\eta X_0^2+2\sqrt c\,LX_0
+{\alpha\over b^2}L^2
+2\sqrt\rho\,\theta LT
-\eta\rho\theta T^2\\
&+{2\delta\over b}LW
-{2\delta\eta\sqrt\rho\over b}TW
+\gamma W^2.
\end{aligned}}
\tag{4.5}
\]

No random variable has been rotated into an independent coordinate. Equation (4.5) is only an invertible deterministic rewrite of three simultaneous linear forms of the residual product bank.

## 5. Main new theorem: every fixed-`T` homogeneous three-variable core is uniformly nondegenerate

For fixed `T=t`, all `t`-dependence in (4.5) outside the constant is affine in `(L,W)`. The homogeneous quadratic matrix in `(X_0,L,W)` is

\[
B_{\rm fib}=
\begin{pmatrix}
c\eta&\sqrt c&0\\
\sqrt c&\alpha/b^2&\delta/b\\
0&\delta/b&\gamma
\end{pmatrix}.
\tag{5.1}
\]

A direct determinant computation gives

\[
\boxed{
\det B_{\rm fib}={c\over b^2}\det M.
}
\tag{5.2}
\]

This is independent of both `eta` and `rho` except through the original matrix determinant. In particular the fixed-`T` quadratic core does **not** become singular when the physical pivot tends to zero.

There is an analogous exact determinant for the residual `(T,W)` slice after fixing `L`:

\[
K_{T,W}=
\begin{pmatrix}
-\eta\rho\theta&-\delta\eta\sqrt\rho/b\\
-\delta\eta\sqrt\rho/b&\gamma
\end{pmatrix},
\tag{5.3}
\]

and

\[
\boxed{
\det K_{T,W}={\eta\rho\over b^2}\det M.
}
\tag{5.4}
\]

Thus the two coordinate systems expose complementary resources:

- `(L,V,W)` keeps the transverse Schur curvature explicit but has vanishing projection volume `|eta|sqrt(rho)`;
- `(T,L,W)` has uniform three-dimensional projection volume `|b|`, while the small `eta rho` factor is confined to a two-dimensional slice determinant;
- fixed `T` eliminates that small determinant entirely: the full `(X_0,L,W)` determinant is `c det M/b^2`.

### 5.1 Uniform coefficient product for the designated partner theorem

The account02/B05 scalar/dependent-pair theorem depends on

`|beta^2 gamma det B_fib|`.

Here

\[
\beta=\sqrt c,
\]

so

\[
|\beta^2\gamma\det B_{\rm fib}|
={c^2|\gamma\det M|\over b^2}.
\tag{5.5}
\]

This quantity has a universal positive lower bound in the near-null collar.

First, because `||M^{-1}||op<=1`, the `(1,1)` cofactor gives

\[
|\alpha\gamma-\delta^2|
\le |\det M|.
\tag{5.6}
\]

The determinant identity

\[
\det M=\eta(\alpha\gamma-\delta^2)-b^2\gamma
\tag{5.7}
\]

therefore implies

\[
b^2|\gamma|
\le(1+|\eta|)|\det M|
\le {3\over2}|\det M|.
\tag{5.8}
\]

Second, apply `||Mz||>=||z||` to

`z=(delta,0,-b)`.

Since

`Mz=(eta delta,0,-gamma b)`,

\[
(\gamma^2-1)b^2\ge(1-\eta^2)\delta^2\ge0.
\]

Because `b!=0`,

\[
\boxed{|\gamma|\ge1.}
\tag{5.9}
\]

Combining (5.8)-(5.9),

\[
\boxed{
{|\gamma\det M|\over b^2}
\ge {\gamma^2\over1+|\eta|}
\ge {2\over3}.
}
\tag{5.10}
\]

Therefore

\[
\boxed{
|\beta^2\gamma\det B_{\rm fib}|
\ge {2\over3}c^2.
}
\tag{5.11}
\]

This is the first essential implication of the run: **after retaining `T` rather than `V` as the third residual coordinate, every normalized fixed-`T` scalar/dependent-pair problem has a determinant resource bounded away from zero uniformly through `eta ->0`.**

## 6. Actual application of account02/B05 r21 and the exact remaining factor

Let `h(t,l,w)` be the joint density of `(T,L,W)`. Since `(T,V,W)` is an orthonormal three-dimensional projection of the original residual product source, its density is at most `2^(3/2)`. By (4.2),

\[
\boxed{
\|h\|_\infty
\le M_3:={2^{3/2}\over|b|}
\le {2^{5/2}\over\sqrt3}.
}
\tag{6.1}
\]

Let

\[
m(t)=\iint h(t,l,w)\,dl\,dw=p_T(t).
\tag{6.2}
\]

For almost every `t` with `m(t)>0`, the normalized conditional pair `(L,W)|T=t` has joint density cap at most

\[
{M_3\over m(t)}.
\tag{6.3}
\]

The physical hub `X_0` remains independent of this conditional pair. The `t`-dependent terms in (4.5) are only affine translations and a constant, which are allowed by account02/B05 r21. Applying that theorem with (5.11) gives

\[
\boxed{
\|p_{Q\mid T=t}\|_\infty
\le31\left({M_3\over m(t)}\right)^{2/3}
     \left({2c^2\over3}\right)^{-1/6}.
}
\tag{6.4}
\]

This is an equation-level application of the designated partner result to the actual near-null fiber.

Multiplying by the fiber mass `m(t)` shows that the subprobability output measure carried by a `dt` slice obeys

\[
\|dq_t/ds\|_\infty
\le31M_3^{2/3}\left({2c^2\over3}\right)^{-1/6}
   m(t)^{1/3}dt.
\tag{6.5}
\]

Using `c>1/2` and (6.1), all constants simplify to

\[
\boxed{
31M_3^{2/3}\left({2c^2\over3}\right)^{-1/6}
\le {124\over6^{1/6}}<92.
}
\tag{6.6}
\]

Hence, for every measurable set `E` of `T`-values, the part of the output law generated by `T in E` has a density satisfying

\[
\boxed{
\|p_{Q;\,T\in E}\|_\infty
\le {124\over6^{1/6}}
\int_E p_T(t)^{1/3}\,dt.
}
\tag{6.7}
\]

For finite-measure `E`, Holder gives the localized form

\[
\boxed{
\|p_{Q;\,T\in E}\|_\infty
<92\,|E|^{2/3}\,\mathbb P(T\in E)^{1/3}.
}
\tag{6.8}
\]

Equations (6.7)-(6.8) are a valid coarea-equivalent interval estimate for the punctured near-null branch, but they are not yet uniform on the whole line. They identify exactly what direct normalized-fiber integration loses.

## 7. The remaining `int p_T^(1/3)` factor is genuinely nonuniform even in a diffuse mixed-support frame

It is important not to hide the factor in (6.7) behind a false conditional-density-moment assertion. It can diverge inside a completely legal original-coordinate product projection with all longitudinal support genuinely mixed.

Take eight residual coordinates and choose three columns of a normalized `8 x 8` Hadamard matrix:

\[
\xi_j,v_j,w_j\in\{\pm1/\sqrt8\},
\qquad \xi\perp v\perp w\perp\xi.
\tag{7.1}
\]

Then every physical residual row has transverse leverage

\[
v_j^2+w_j^2={1\over4}< {1\over2},
\tag{7.2}
\]

and every coordinate carrying longitudinal coefficient `xi_j` also carries nonzero transverse coefficients. Thus this is not the pure-longitudinal bank already removed by the absorption theorem.

Choose the first Hadamard column to be all positive, so

\[
T={1\over\sqrt8}\sum_{j=1}^8 X_j.
\tag{7.3}
\]

Let

\[
X_1\sim {\rm Unif}[0,R],\qquad
X_2,\ldots,X_8\sim {\rm Unif}[0,1],
\tag{7.4}
\]

independently, with `R>=8`. Every density is at most one. Write

`Z=(X_2+...+X_8)/sqrt(8)`.

Since `Z` is supported on `[0,7/sqrt(8)]` and `X_1/sqrt(8)` is uniform on `[0,R/sqrt(8)]` with density `sqrt(8)/R`, convolution gives the exact plateau

\[
p_T(t)={\sqrt8\over R}
\quad\text{for}\quad
{7\over\sqrt8}\le t\le {R\over\sqrt8}.
\tag{7.5}
\]

Therefore

\[
\boxed{
\int_{\mathbb R}p_T(t)^{1/3}dt
\ge {R-7\over2R^{1/3}}
\longrightarrow\infty.
}
\tag{7.6}
\]

This example also remains compatible with the small-`rho` mixed graph condition from the preceding B05 pruning: with `u_j=sqrt(rho)xi_j`, each longitudinal coefficient is `sqrt(rho/8)` while each transverse row norm is `1/2`, so the cube-root graph inequality holds throughout the sufficiently small punctured collar (indeed for the owner-scale small `rho`).

Equation (7.6) is **not a counterexample to QFORM** and says nothing bad about the true output density. It proves only that the direct route “normalize every `T` fiber, apply a positive power of its conditional density cap, then integrate the fiber suprema” cannot yield a law-uniform constant. The missing factor cannot be paid by a one-dimensional marginal bound on `T`.

More generally, any fiberwise estimate whose normalized conditional-cap dependence is a positive power `M^a`, `a>0`, produces after disintegration a factor of the type

\[
\int p_T(t)^{1-a}dt,
\]

which is not uniformly controlled under the allowed cap-one source laws. Thus the problem is structural, not a bad exponent specific to `2/3`.

## 8. Precise first unpaid implication

The first B05 debt is sharpened to

`QFORM-NEARNULL-SOURCE-ADAPTED-SELECTOR-REFUND-v1`:

> In the near-null exact-rank-three heavy-row normal form (2.1)-(2.3), prove a universal bound on the exact root-selector integral (3.10) while retaining the original-coordinate product source. Equivalently, refund the `int p_T^(1/3)` loss in (6.7) by using the fact that `T` enters only as the translation `-sqrt(rho/c) T` of the **same physical hub density** `f_0`, before normalizing or taking a fiber supremum.

This is more specific than an arbitrary-joint coarea problem. The reciprocal Jacobian `Delta_s^{-1/2}` is independent of `T`; the entire longitudinal innovation appears only in the source-adapted hub selector. The newest source continuation's adapted-hub functional `(SP)` and account02/B16's source-adapted-hub barrier point in the same direction, but neither currently proves the arbitrary-law estimate needed here.

A correct next mechanism should therefore keep

\[
f_0\!\left(-\sqrt{\rho/c}\,T+\Psi_{\pm,s}(V,W)\right)
\tag{8.1}
\]

inside the original product integral until the transverse reciprocal kernel has been paid. Replacing it by `1`, replacing `(T,V,W)` by an arbitrary bounded joint density, or normalizing `T` fibers first all lose a quantitatively necessary source factor.

## 9. Scope / status

- Full QFORM: `OPEN / NOT PROVED / NOT DISPROVED`.
- New proved structural facts: (3.6)-(3.10), the complementary volume identity (4.2), the fiber determinant identities (5.2)/(5.4), the uniform coefficient product (5.11), and the localized partner-driven bound (6.7)-(6.8).
- New proof-interface obstruction: the exact diffuse mixed Hadamard family (7.1)-(7.6) makes the direct fiber quasi-norm diverge.
- No new full-target continuity claim.
- Execution remains `WITHOUT_VERIFIED_BRAIN`: authenticated repository use occurred, but no native learned-memory receiver retrieval/use was verified.
- No scheduler state, email or notification setting, public-release state, paid model/API/Codex call, cross-account authentication, or permission state was changed.
