SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B05, 2026-09-23T13:04:27.012267Z.
attacking: close the Pluecker-diffuse heavy-null two-sheet branch by a slice-Fourier/Fresnel--Brascamp--Lieb estimate on the full residual product bank, without selecting physical Pluecker coordinates or taking curved-fiber suprema.

# fleet02/B05 — slice-Fresnel closure of the Pluecker-diffuse heavy-null branch

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Quadratic coarea bound / complementary constructions and source-valid counterexamples  
**Run:** `20260923T130427Z-fleet02-B05-QFORM-auto11`  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / HEAVY_NULL_EXACT_RANK3_BRANCH_CLOSED / FULL_QFORM_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** only essential boundedness is asserted by the new theorem; full-target continuity remains separate.

The full conjecture remains OPEN. No moment, support, log-concavity, iid, diagonal-basis, post-rotation-independence, or conditional-density hypothesis is introduced.

## 1. First unpaid implication and result of this run

The immediately preceding B05 run reduced the exact-rank-three heavy physical null-pivot survivor to a residual-diffuse product bank. In that survivor a heavy original coordinate has leverage `c>1/2`, while every residual original coordinate has transverse leverage at most `1/2`. The preceding finite-Pluecker theorem paid the punctured innovation range whenever a bounded physical Pluecker frame captures the two-dimensional curved normal pencil, and a Walsh--Hadamard exact-target family showed that no bounded-cardinality physical Pluecker frame can be forced.

The first unpaid implication was therefore

`QFORM-HEAVY-NULL-PLUECKER-DIFFUSE-BRIDGE-v1`.

This report closes that implication without selecting any physical Pluecker coordinate. The key is to slice first in the transverse linear coordinate, leaving one genuine square on the slice. Fresnel linearisation of that square converts the entire curved slice into a translated **two-dimensional Fourier integral**. The translation contains the same-bank longitudinal variable but costs nothing because the geometric Brascamp--Lieb inequality is translation invariant. The completed newest-Claude one-dimensional `L^p` Fourier lemma then pays the two-dimensional integral directly from the residual transverse leverage bound.

The resulting slice theorem is uniform in the longitudinal innovation, including the Pluecker-diffuse regime:

\[
\boxed{
 \mu_l(I)
 \le C_* |\gamma|^{-1/2}|I|^{1/2},
 \qquad
 C_*=4e^{1/8}2^{-1/4}\Gamma(1/4)
 <13.819.
}
\]

Feeding this into the completed fleet03/B05 single-hub receiver gives, throughout the residual-diffuse heavy-null target branch,

\[
\boxed{\|p_Q\|_{\infty,\mathrm{ess}}<55.776.}
\]

Combining with the already-completed nested-heavy exit closes the **entire exact-rank-three heavy physical null-pivot branch**. Thus the first unpaid exact-rank-three heavy-row implication after this run is the genuinely near-null but nonzero physical pivot bridge:

`QFORM-HEAVY-NEARNULL-NONZERO-PIVOT-BRIDGE-v1`.

That next step must remain uniform as `A_ii -> 0` without treating the small matrix coefficient as a uniformly small random quadratic perturbation.

## 2. Source inputs actually applied

### 2.1 Fresh controls and predecessor


The immediate predecessor is

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B05/20260923T123346Z-fleet02-B05-QFORM-5e5df016/REPORT.md`.

It gives the heavy-null normal form, proves the finite-Pluecker punctured bridge, and exhibits the exact-target Walsh--Hadamard family in which every bounded physical Pluecker frame degenerates.

### 2.2 Required newest-Claude package: a real inequality application

I read all three owner-pinned files at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`:

- `RESULTS.md`,
- `FOURIER_ROUTE_REPORT.md`,
- `COUNTEREXAMPLE_SEARCH.md`.

The completed one-dimensional Fourier lemma from `RESULTS.md`/`FOURIER_ROUTE_REPORT.md` is applied below at equation (5.4): if `f<=1` is a probability density, then for every `p>=2`,

\[
\int_{\mathbb R}|\widehat f(s)|^p\,ds\le {4\pi\over\sqrt p}.
\tag{2.1}
\]

Together with the exact translation-invariant geometric Brascamp--Lieb step used in Theorem F, it yields the concrete two-dimensional bound `(4 pi)^2` in (5.5). This is the decisive dimension-free estimate of the present proof, not a citation-only mention.

The source's `COUNTEREXAMPLE_SEARCH.md` still records the ruled one-sheet estimate `p(s)<=pi sqrt(2)` and identifies the convex/two-sheet side as the remaining rank-three geometry. The theorem below pays a substantial high-leverage two-sheet branch using product provenance rather than arbitrary-joint X-rays.

### 2.3 Designated partner fleet03/B05

The freshest designated-partner report found before publication is fleet03/B05 r25,

`yspennstate/math-open-problems@02e8b920f91cd9489773d6d895d2117920b2b75a`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B05/20260923T123731Z-fleet03-B05-QFORM-r25/REPORT.md`.

It proves that a bounded ambient reciprocal-gradient budget, even together with caps on every one-dimensional projection of an arbitrary joint law, cannot control the level trace; the missing ingredient must use actual original-coordinate product-projection provenance. The present proof does exactly that in (5.3)-(5.5): it never replaces the residual law by an arbitrary joint density.

For the final hub step I apply the completed positive receiver from fleet03/B05 r24,

`yspennstate/math-open-problems@b0e14a08fe8abb97f7aeb518cfa8cf4cef568d36`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B05/20260923T094405Z-fleet03-B05-QFORM-r24/REPORT.md`.

Its single-hub theorem states that for the normalized form `2XL+Y`, if the unnormalised `L=l` slice measure satisfies

\[
\mu_l(E)\le K|E|^{1/2}
\tag{2.2}
\]

uniformly in `l`, then an independent cap-one hub gives

\[
\|p\|_{\infty,\mathrm{ess}}\le {1\over2}+2\sqrt2 K.
\tag{2.3}
\]

It is applied quantitatively in Section 7.

### 2.4 Nested-heavy exit

Fleet02/B10's completed theorem

`QFORM-NULL-ROW-NESTED-HEAVY-CLOSURE-v1`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B10/20260922T193653Z-fleet02-B10-QFORM-r15/REPORT.md`,

shows that in the exact-rank-three heavy-null state, if any residual row has transverse leverage `>1/2`, a uniformly nonzero physical pivot or a uniformly indefinite physical pair is already available and the corresponding density branch is paid. Hence only the residual-diffuse case treated below is needed for heavy-null closure.

## 3. Exact heavy-null residual-diffuse normal form

Let

\[
A=RMR^T,\qquad R^TR=I_3,
\]

be exact rank three with

\[
\sigma_{\min}(M)\ge1.
\]

Assume an original coordinate `0` has leverage

\[
c=\|r_0\|^2>{1\over2}
\]

and exact physical null pivot

\[
A_{00}=0.
\]

Rotate only the deterministic three-dimensional coefficient basis so that

\[
r_0=\sqrt c\,e_1.
\]

No random variable is rotated. As in the predecessor, after an additional deterministic rotation in `e_1^perp`,

\[
M=
\begin{pmatrix}
0&b&0\\
b&\alpha&\delta\\
0&\delta&\gamma
\end{pmatrix}.
\tag{3.1}
\]

Since `||M^{-1}||op<=1`,

\[
|b|\ge1,\qquad |\gamma|\ge1.
\tag{3.2}
\]

Write every residual spectral row as

\[
r_j=(u_j,v_j,w_j),\qquad j\ne0.
\]

Parseval gives

\[
\sum u_j^2=\rho:=1-c,
\quad \sum v_j^2=\sum w_j^2=1,
\quad \sum u_jv_j=\sum u_jw_j=\sum v_jw_j=0.
\tag{3.3}
\]

The nested-heavy exit permits restriction to

\[
\boxed{v_j^2+w_j^2\le{1\over2}\quad\text{for every }j\ne0.}
\tag{3.4}
\]

If `rho>0`, put

\[
\xi={u\over\sqrt\rho},
\qquad
T=\xi\cdot X_{-0},
\qquad
V=v\cdot X_{-0},
\qquad
W=w\cdot X_{-0}.
\]

Then `xi,v,w` are orthonormal coefficient vectors on the residual original coordinates. If `rho=0`, all terms containing `T` vanish and `xi` can simply be omitted.

The quadratic form is

\[
Q=2b(\sqrt c X_0+\sqrt\rho T)V
  +\alpha V^2+2\delta VW+\gamma W^2.
\tag{3.5}
\]

The only probabilistic independence asserted here is that the physical hub `X_0` is independent of the residual original-coordinate product bank.

## 4. Shear away the transverse cross term without rotating randomness

Set

\[
r={\delta\over\gamma},
\qquad
z=w+r v,
\qquad
Z=z\cdot X_{-0}=W+rV,
\qquad
\kappa=\alpha-{\delta^2\over\gamma}.
\tag{4.1}
\]

This is only algebra inside the phase. We do **not** assert that `V` and `Z` are independent. Equation (3.5) becomes

\[
Q=2hX_0V+Y,
\qquad
h=b\sqrt c,
\tag{4.2}
\]

with

\[
Y=\gamma Z^2+2aVT+\kappa V^2,
\qquad a=b\sqrt\rho.
\tag{4.3}
\]

Let `R_2` be the residual coefficient matrix with columns `(v,z)`. Because

\[
[v\ z]=[v\ w]
\begin{pmatrix}1&r\\0&1\end{pmatrix},
\]

its Gram matrix is

\[
G=R_2^TR_2=
\begin{pmatrix}1&r\\r&1+r^2\end{pmatrix},
\qquad \det G=1.
\tag{4.4}
\]

For the `j`th original-coordinate row `q_j=(v_j,z_j)`, the normalized leverage is invariant under this invertible shear:

\[
q_jG^{-1}q_j^T=v_j^2+w_j^2\le{1\over2}.
\tag{4.5}
\]

This identity is the geometric reason the potentially large deterministic ratio `delta/gamma` costs nothing.

## 5. Main slice-Fresnel theorem

For almost every `l`, let `mu_l` denote the unnormalised slice measure in the `Y` variable obtained by disintegrating the residual product measure along `V=l`:

\[
\mu_l(B)
=\int_{\{v\cdot x=l\}}
 \mathbf 1_{\{\gamma(z\cdot x)^2+2al(\xi\cdot x)+\kappa l^2\in B\}}
 \prod_{j\ne0}f_j(x_j)\,d\mathcal H^{m-1}(x),
\tag{5.1}
\]

where `||v||=1`, so no additional coarea factor appears.

### Theorem 5.1 — `QFORM-SLICE-FRESNEL-BL-v1`

Under (3.4), for every `t!=0` and almost every `l`, the Fourier transform of the slice measure has the representative

\[
\boxed{
|\widehat\mu_l(t)|
\le4\sqrt\pi\,|\gamma t|^{-1/2}.
}
\tag{5.2}
\]

The estimate is independent of `a=b sqrt(rho)`, hence independent of the longitudinal innovation and uniform as `rho ->0`.

#### Proof

The term `exp(i t kappa l^2)` has modulus one and can be discarded. On the hyperplane `V=l`, the mixed term is exactly the linear phase

\[
2atVT=2atlT.
\]

This is the critical order of operations: slice first, then linearize. We never condition on `T` given `(V,W)`.

Apply the one-square Fresnel formula from the pinned newest-Claude source to `exp(i t gamma Z^2)`. After removing the standard Gaussian damping by dominated convergence, it gives

\[
|\widehat\mu_l(t)|
\le(4\pi|\gamma t|)^{-1/2}
\int_{\mathbb R}|I_l(q)|\,dq,
\tag{5.3}
\]

where

\[
I_l(q)=
\int_{\{v\cdot x=l\}}
 e^{i(qz+2atl\xi)\cdot x}
 \prod f_j(x_j)\,d\mathcal H^{m-1}(x).
\]

For the hyperplane transform, Fourier inversion in its normal coordinate gives

\[
|I_l(q)|
\le {1\over2\pi}
\int_{\mathbb R}
 \prod_j
 \left|\widehat f_j(sv_j+qz_j+2atl\xi_j)\right|\,ds.
\tag{5.4}
\]

The double integral in `(s,q)` is now an **original-coordinate product Fourier integral**. Put

\[
c_j=q_jG^{-1}q_j^T.
\]

By (4.5), `0<=c_j<=1/2` and `sum c_j=2`. The geometric Brascamp--Lieb inequality is invariant under the coordinatewise translations `2atl xi_j`, and the exact same normalization used in newest-Claude Theorem F gives

\[
\begin{aligned}
&\int_{\mathbb R^2}
 \prod_j|\widehat f_j(sv_j+qz_j+2atl\xi_j)|\,ds\,dq\\
&\quad\le(\det G)^{-1/2}
 \prod_{c_j>0}
 \left(c_j^{-1/2}\int|\widehat f_j(\omega)|^{1/c_j}d\omega\right)^{c_j}.
\end{aligned}
\tag{5.5}
\]

Now apply the pinned completed Fourier lemma (2.1) with `p=1/c_j>=2`:

\[
\int|\widehat f_j|^{1/c_j}\le4\pi\sqrt{c_j}.
\tag{5.6}
\]

Every bracket in (5.5) is therefore at most `4 pi`; since `sum c_j=2` and `det G=1`,

\[
\boxed{
\int_{\mathbb R^2}
 \prod_j|\widehat f_j(sv_j+qz_j+2atl\xi_j)|\,ds\,dq
\le(4\pi)^2.
}
\tag{5.7}
\]

Combining (5.3), (5.4), and (5.7) gives

\[
(4\pi|\gamma t|)^{-1/2}{(4\pi)^2\over2\pi}
=4\sqrt\pi|\gamma t|^{-1/2},
\]

which is (5.2).

For arbitrary rough input densities, first convolve each `f_j` with a smooth approximate identity. This preserves probability mass and the cap `<=1`, so all bounds above are unchanged. The absolute integrability in `(s,q)` supplied by (5.7) gives the hyperplane Fourier representative. Passing to the original laws in `L^1` and then by Fatou at the interval-measure level proves the same inequality for the original product law. No continuity of the final output density is assumed. QED.

## 6. Rough-input interval estimate on every slice

Let `I=[y_0-epsilon/2,y_0+epsilon/2]`. The elementary Gaussian majorant

\[
\mathbf1_I(y)
\le e^{1/8}
 \exp\left(-{(y-y_0)^2\over2\epsilon^2}\right)
\tag{6.1}
\]

and Fourier inversion give

\[
\mu_l(I)
\le {e^{1/8}\epsilon\over\sqrt{2\pi}}
\int_{\mathbb R}
 e^{-\epsilon^2t^2/2}|\widehat\mu_l(t)|\,dt.
\tag{6.2}
\]

Insert (5.2) and use

\[
\int_{\mathbb R}e^{-\epsilon^2t^2/2}|t|^{-1/2}dt
=2^{1/4}\Gamma(1/4)\epsilon^{-1/2}.
\tag{6.3}
\]

Hence

\[
\boxed{
\mu_l(I)
\le C_*|\gamma|^{-1/2}\epsilon^{1/2},
\qquad
C_*=4e^{1/8}2^{-1/4}\Gamma(1/4)
=13.8188014756908\ldots .
}
\tag{6.4}
\]

This is the requested rough-input interval theorem. It uses the entire diffuse product bank before any physical-coordinate selection; the Pluecker packet may be arbitrarily diffuse.

## 7. Feed the slice bound into the independent physical hub

Return to

\[
Q=2hX_0V+Y,
\qquad h=b\sqrt c.
\]

Set `L'=hV`. Under this scalar change of the slicing variable, the unnormalised slice constant in (6.4) becomes

\[
K'={C_*\over |h|\sqrt{|\gamma|}}.
\tag{7.1}
\]

Apply the completed fleet03/B05 r24 single-hub receiver (2.3):

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
\le {1\over2}
+{2\sqrt2\,C_*
 \over |b|\sqrt c\sqrt{|\gamma|}}.
}
\tag{7.2}
\]

In the target heavy-null normalization (3.2), `c>1/2`, so

\[
|b|\sqrt c\sqrt{|\gamma|}>{1\over\sqrt2}.
\]

Therefore

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
< {1\over2}+4C_*
=55.7752059027634\ldots <55.776.
}
\tag{7.3}
\]

This proves absolute continuity with an essentially bounded density in the branch. No continuous representative is claimed here.

## 8. Closure of the exact-rank-three heavy-null branch

There are two cases after a heavy physical null row is exposed.

1. Some residual physical row has transverse leverage `>1/2`. Then `QFORM-NULL-ROW-NESTED-HEAVY-CLOSURE-v1` supplies either a uniformly nonzero physical pivot or a uniformly conditioned indefinite physical pair, and its completed receiver closes the branch.

2. Every residual row has transverse leverage `<=1/2`. Then Theorem 5.1 and (7.3) apply.

Thus:

### Corollary 8.1 — `QFORM-HEAVY-NULL-EXACT-RANK3-CLOSURE-v1`

For every exact-rank-three target form with `sigma_min(M)>=1`, if there is a physical row of leverage `>1/2` and its physical diagonal coefficient is exactly zero, the quadratic form in arbitrary independent cap-one inputs has an essentially bounded density with a universal constant. In the residual-diffuse branch the explicit constant is `<55.776`; the nested-heavy branch uses the previously published constants of its pivot/pair receivers.

If no physical row has leverage `>1/2`, newest-Claude Theorem F already gives the rank-three density bound `<=12`. Therefore an exact-rank-three obstruction cannot remain at an exact zero physical pivot.

## 9. Exact Pluecker-diffuse stress family is now paid on both sides

The predecessor's Walsh--Hadamard family has

\[
M=\begin{pmatrix}0&1&0\\1&0&0\\0&0&1\end{pmatrix},
\qquad
\operatorname{spec}(A)=\{-1,1,1\},
\]

one heavy hub of leverage `c>1/2`, and residual Walsh vectors `xi,v,w`. For `N>=4`,

\[
v_j^2+w_j^2={2\over N}\le{1\over2}.
\]

Its normal pencil is maximally Pluecker-diffuse: every bounded set of physical pair coordinates has vanishing lower frame constant as `N->infinity`. The predecessor could pay only the one-sheet side uniformly via newest-Claude Theorem C plus a finite-frame conditional branch.

Equation (7.3) now pays the **entire output law** of this exact-target Pluecker-diffuse family by `<55.776`, uniformly in `N` and uniformly as the longitudinal coefficient `sqrt(1-c)` tends to zero. This confirms that the finite-frame obstruction was a proof-interface obstruction, not evidence for a QFORM counterexample.

## 10. Why the fleet03/B05 r25 shell obstruction does not apply

Partner r25 constructs arbitrary joint parabolic/spherical shells with excellent ambient gradient and one-dimensional projection bounds but unbounded quadratic level density. The present proof uses strictly more structure: at (5.4) the slice is represented by a product of the **individual original-coordinate Fourier transforms**, and (5.5) spends the exact two-dimensional coefficient geometry before any level supremum. That factorization is unavailable for r25's engineered joint shells.

Thus r25 is used as a real obstruction criterion: any proof replacing (5.4) by only a joint-density or projection-cap summary would be invalid, whereas the present argument remains inside the product class at every step.

## 11. Remaining implication

The finite-Pluecker and Pluecker-diffuse heavy-null branches are no longer unpaid. The next high-leverage exact-rank-three obstruction is

**`QFORM-HEAVY-NEARNULL-NONZERO-PIVOT-BRIDGE-v1`.**

For a heavy physical row with small but nonzero diagonal coefficient `d=A_ii`, obtain a density estimate uniform as `d->0`, preserving arbitrary unbounded product laws. The existing nonzero-pivot half-Riesz theorem deteriorates as a negative power of `|d|`; the exact `d=0` endpoint is now uniformly paid by Corollary 8.1. Small `d` cannot be discarded as a small random quadratic perturbation. A plausible next route is to retain the same `V=l` slice but jointly spend the additional `T^2` curvature generated by the nonzero longitudinal square, rather than bounding it absolutely.

## 12. Scope and review status

Proved this run:

- `QFORM-SLICE-FRESNEL-BL-v1`, the dimension-free slice Fourier decay (5.2);
- the rough-input interval theorem (6.4), uniform in the longitudinal innovation and with no finite Pluecker-frame certificate;
- the residual-diffuse heavy-null density bound (7.3);
- with the completed nested-heavy theorem, closure of the entire exact-rank-three heavy physical null-pivot branch.

Not proved:

- a uniform bridge for a nonzero pivot tending to zero;
- the unrestricted exact-rank-three convex/two-sheet theorem;
- the arbitrary-rank full QFORM conjecture;
- global continuity.

Independent review of the new theorem is **PENDING**.
