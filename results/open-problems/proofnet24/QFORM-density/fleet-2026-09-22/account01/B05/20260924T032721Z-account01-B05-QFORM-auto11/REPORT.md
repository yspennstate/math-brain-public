SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B05, 2026-09-24T03:27:21Z.
attacking: the near-coloop Witt product-projection Borel tube; use original-coordinate two-variable coarea before any projection/fiber supremum, then quantify exactly the aggregate Pluecker factor still missing.

# account01/B05 — pairwise Pluecker tube theorem and exact aggregate-coarea debt

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** quadratic coarea / equivalent interval bound preserving arbitrary product densities.  
**Control:** OWNER CONTROL revision `2026-09-22.15`; QFORM-only.  
**Status:** `NEW_PRODUCT_PRESERVING_PAIRWISE_TUBE_THEOREM / PARTNER_MAXCUT_APPLIED / TARGET_VALID_DIMENSION_LOSS_EXHIBITED / FULL_QFORM_OPEN`.  
**Regularity:** the new paid branches prove an essentially bounded density; continuity for the full target is not proved here.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact unpaid state inherited from the previous B05 run

The preceding immutable B05 report is

`yspennstate/math-open-problems@28238ad9b68d613f205feab35e3048a51fd48179:`  
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B05/20260924T024114Z-account01-B05-QFORM-auto11/REPORT.md`.

It reduces the high-leverage, exact-rank-three, zero-pivot survivor to the physical Witt form

\[
Q=2aV(H+\kappa U)+\alpha V^2+2\gamma VW+\delta W^2,                 \tag{1.1}
\]

where

* `H` is a literal original coordinate and is genuinely independent of the residual product bank;
* `U,V,W` are three orthonormal coefficient projections of that residual product bank, but are not probabilistically independent;
* `a\ne0`, `\delta\ne0`;
* in the near-coloop chamber, `0\le\kappa<1/\sqrt7`;
* the exact determinant-star currency through the heavy physical coordinate is

\[
\boxed{S_i=a^2|\delta|=c\Delta_3.}                                  \tag{1.2}
\]

At target normalization in this branch, `S_i>=1/2`.

Completing the transverse square without rotating the random coordinates,

\[
Z=W+\frac{\gamma}{\delta}V,\qquad
A=\alpha-\frac{\gamma^2}{\delta},                                  \tag{1.3}
\]

gives

\[
Q=2aVH+2a\kappa UV+A V^2+\delta Z^2.                                \tag{1.4}
\]

For output centre `t` and `V\ne0`, put

\[
\Psi_t
=\kappa U+\frac{A}{2a}V+\frac{\delta Z^2-t}{2aV}.                \tag{1.5}
\]

Then exactly

\[
Q-t=2aV(H+\Psi_t).                                                   \tag{1.6}
\]

For `r>0`, let `\nu_{r,t}` be the shell submeasure of `\Psi_t` on `r\le|V|\le2r`. The preceding B05 compiler proves that if

\[
\nu_{r,t}(E)
\le K_T\sqrt{\frac{|a|}{|\delta|}}r^{3/2}|E|^{1/2}                 \tag{1.7}
\]

for every Borel `E`, then, for density cap `m_H` of `H`,

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
\le C_0(K_T/K_0)^{2/3}m_H^{2/3}S_i^{-1/3},
}                                                                    \tag{1.8}
\]

where

\[
K_0=\frac83(4-\sqrt2)=6.895430500338\ldots,                         \tag{1.9}
\]

and

\[
C_0
=3\,2^{-5/3}[K_0(1+\sqrt2)]^{2/3}
=6.160689335164\ldots.                                               \tag{1.10}
\]

The old run established (1.7) at `\kappa=0` from account02/B05's affine-shear Borel theorem, but the `\kappa>0` product-projection case remained unpaid. It also proved that (1.7) is false for arbitrary joint density-one triples, so the product provenance cannot be discarded.

This run proves a new product-preserving local theorem for every physical coordinate pair, uniform in `\kappa`, and then identifies exactly why selecting one pair is insufficient.

## 2. New theorem: a physical-pair Borel tube bound uniform in the shared shear

Write the residual product vector as `X=(X_1,...,X_m)` with independent densities `f_j<=1`, and write the coefficient vectors of `U,V,W` as `u,v,w`, so

\[
\langle u,v\rangle=\langle u,w\rangle=\langle v,w\rangle=0,
\qquad \|u\|=\|v\|=\|w\|=1.                                      \tag{2.1}
\]

For a physical pair `j<k`, define its square-carrier Pluecker coefficient

\[
b_{jk}:=v_jw_k-v_kw_j.                                              \tag{2.2}
\]

Notice that replacing `W` by `Z=W+(\gamma/\delta)V` does not change this coefficient:

\[
v_j z_k-v_k z_j=b_{jk}.                                             \tag{2.3}
\]

### Theorem 2.1 — `QFORM-WITT-PAIRWISE-PLUECKER-TUBE-v1`

For every pair `j<k` with `b_{jk}\ne0`, every `r>0`, every `t\in\mathbb R`, and every Borel set `E\subset\mathbb R` of finite Lebesgue measure,

\[
\boxed{
\nu_{r,t}(E)
\le
\frac{K_0}{|b_{jk}|}
\sqrt{\frac{|a|}{|\delta|}}
r^{3/2}|E|^{1/2}.
}                                                                    \tag{2.4}
\]

The estimate is uniform in `\kappa`, `A`, `\gamma/\delta`, `t`, all conditioned original coordinates, and all admissible one-dimensional input laws. No rotated-coordinate independence, moment, support, log-concavity, or continuity assumption is used.

#### Proof

Condition on every original coordinate except `X_j,X_k`. Their conditional joint density remains the honest product `f_j(x_j)f_k(x_k)<=1`.

Set

\[
p=(v_j,v_k),\qquad P=\|p\|_2.                                      \tag{2.5}
\]

Since `b_{jk}\ne0`, necessarily `P>0`. Make only the following determinant-one orthogonal change **inside this physical coordinate pair**:

\[
y=\frac{v_jx_j+v_kx_k}{P},
\qquad
s=\frac{-v_kx_j+v_jx_k}{P}.                                        \tag{2.6}
\]

All other coordinates are frozen. Thus

\[
V=v_*+Py,\qquad dx_jdx_k=dyds=\frac{dV\,ds}{P}.                    \tag{2.7}
\]

On a fixed level `V=v`, both `U` and `Z` are affine functions of `s`. The `s`-slope of `Z` is

\[
\frac{v_jz_k-v_kz_j}{P}=\frac{b_{jk}}{P}.                           \tag{2.8}
\]

Consequently, on that fixed `V=v`, the function `s\mapsto\Psi_t` is an arbitrary affine function plus a quadratic whose quadratic coefficient is exactly

\[
q(v)=\frac{\delta}{2av}\frac{b_{jk}^2}{P^2}.                       \tag{2.9}
\]

This is the key point: the shared term `\kappa U` contributes only an affine function of `s`; it cannot reduce or cancel the quadratic coefficient (2.9).

For any real quadratic `q(s-s_0)^2+c` with `q\ne0`, the pushforward of one-dimensional Lebesgue measure has density

\[
\frac{1}{\sqrt{|q|\,|y-c|}}
\]

on the appropriate half-line. Therefore decreasing rearrangement gives, for every Borel set `E` of length `m`,

\[
\operatorname{Leb}\{s:q(s-s_0)^2+c\in E\}
\le2\sqrt{\frac{m}{|q|}}.                                          \tag{2.10}
\]

Applying (2.10) to (2.9), then using (2.7), the conditional physical-pair measure of the section at a fixed `v` is at most

\[
\frac{2\sqrt2}{|b_{jk}|}
\sqrt{\frac{|a|}{|\delta|}}
\sqrt{|v|}\,|E|^{1/2}\,dv.                                        \tag{2.11}
\]

The product density is at most one, so no additional factor appears. Integrating over both sign components of `r\le|v|\le2r`,

\[
\int_{r\le|v|\le2r}\sqrt{|v|}\,dv
=\frac43(2^{3/2}-1)r^{3/2}.                                        \tag{2.12}
\]

The constant in (2.11)--(2.12) is

\[
\frac{8\sqrt2}{3}(2^{3/2}-1)
=\frac83(4-\sqrt2)
=K_0.                                                               \tag{2.13}
\]

The bound is independent of all frozen coordinates, so averaging them proves (2.4). QED.

### Corollary 2.2 — pairwise full density estimate

Insert (2.4) into the already-proved Borel-profile compiler (1.8). Since `m_H<=1`, every nonzero physical pair satisfies

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
\le
C_0 |b_{jk}|^{-2/3} S_i^{-1/3},
\qquad
C_0=6.160689335164\ldots.
}                                                                    \tag{2.14}
\]

In the target-normalized high-leverage branch `S_i>=1/2`,

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
<7.762\,|b_{jk}|^{-2/3}.
}                                                                    \tag{2.15}
\]

This closes every Witt instance possessing one square-carrier physical pair with `|b_{jk}|` bounded below by an absolute constant. It is not the full branch because the Pluecker mass can be distributed over arbitrarily many tiny pairs.

## 3. Exact Jacobian/curvature conservation

There is a complementary structural identity showing that no curvature is actually lost when all individual `b_{jk}` are small.

Let

\[
a_{jk}:=v_ju_k-v_ku_j.                                              \tag{3.1}
\]

For the map `F=(V,\Psi_t)`, direct differentiation gives

\[
\boxed{
J_{jk}:=
\det\begin{pmatrix}
\partial_jV&\partial_kV\\
\partial_j\Psi_t&\partial_k\Psi_t
\end{pmatrix}
=
\kappa a_{jk}
+\frac{\delta}{a}\frac{Z}{V}b_{jk}.
}                                                                    \tag{3.2}
\]

Because `u,v,w` are orthonormal, the two exterior products `v\wedge u` and `v\wedge w` are orthonormal in `\Lambda^2\mathbb R^m`. Hence

\[
\sum_{j<k}a_{jk}^2=1,
\qquad
\sum_{j<k}b_{jk}^2=1,
\qquad
\sum_{j<k}a_{jk}b_{jk}=0.                                          \tag{3.3}
\]

Therefore

\[
\boxed{
\sum_{j<k}J_{jk}^2
=
\kappa^2+rac{\delta^2}{a^2}\frac{Z^2}{V^2}.
}                                                                    \tag{3.4}
\]

Equation (3.4) is a full two-Jacobian conservation law. Equation (2.9) is even more useful for the present Borel trace because it avoids pointwise cancellation between the two terms in (3.2): after fixing `V`, `\kappa U` is affine and the second derivative is governed solely by `b_{jk}^2`.

Also, by Cauchy--Binet,

\[
\boxed{\sum_{j<k}b_{jk}^2=1.}                                      \tag{3.5}
\]

Thus the obstruction is not absence of curvature. It is the order of operations: conditioning on a **single** physical pair converts the conserved mass (3.5) into one reciprocal `|b_{jk}|^{-1}` before the remaining pairs can be aggregated.

## 4. Designated partner account02/B05 applied to an actual inequality

The completed partner report

`yspennstate/math-open-problems@4ad9d206dba1b22fd917280717c24f4e1dd6ea09:`  
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260924T022915Z-account02-B05-QFORM-auto11/REPORT.md`

proves the source-disjoint max-cut theorem for exactly this determinant-star plane. In the present notation there is a partition of the residual **original coordinates** into disjoint banks `J,K` such that

\[
\boxed{
M_{J,K}:=
\sum_{j\in J,k\in K}b_{jk}^2\ge\frac12.
}                                                                    \tag{4.1}
\]

Equivalently, since the heavy-coordinate principal determinants satisfy

\[
|\det A_{\{i,j,k\}}|=S_i b_{jk}^2,                                 \tag{4.2}
\]

the cross-bank determinant star satisfies

\[
\sum_{j\in J,k\in K}|\det A_{\{i,j,k\}}|
\ge\frac{S_i}{2}.                                                    \tag{4.3}
\]

This partner result gives an immediate, honest inequality from Theorem 2.1. Since there are at most `|J||K|` cross pairs, (4.1) implies

\[
\max_{j\in J,k\in K}|b_{jk}|
\ge(2|J||K|)^{-1/2}.                                                 \tag{4.4}
\]

Selecting that pair in (2.14) yields

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
\le
7.761982175236\,(|J||K|)^{1/3}S_i^{-1/3}.
}                                                                    \tag{4.5}
\]

At target normalization `S_i>=1/2`,

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
<9.780\,(|J||K|)^{1/3}.
}                                                                    \tag{4.6}
\]

So the partner's aggregate star has been applied to the new coarea theorem at an actual density inequality. The result pinpoints, quantitatively, the exact defect of pair selection: a factor `( |J||K| )^{1/3}` is introduced **after** a dimension-free cross-star mass `>=1/2` was already available.

## 5. Target-valid stress family: the pair-selection loss is genuinely unbounded

The factor in (4.6) is not an artefact of the max-cut proof. It can occur inside the exact three-large-eigenvalue target while the total Pluecker currency stays equal to one.

Let `N` be divisible by four. In the residual `N`-dimensional physical-coordinate bank define three orthonormal coefficient vectors

\[
v=N^{-1/2}(1,\ldots,1),                                             \tag{5.1}
\]

\[
w=N^{-1/2}(\underbrace{1,\ldots,1}_{N/2},
             \underbrace{-1,\ldots,-1}_{N/2}),                      \tag{5.2}
\]

and let `u` be the quarter-alternating Walsh vector

\[
u=N^{-1/2}(+^{N/4},-^{N/4},+^{N/4},-^{N/4}).                      \tag{5.3}
\]

Take

\[
c=\frac{15}{16},\qquad \kappa=\sqrt{\frac{1-c}{c}}=\frac1{\sqrt{15}},\tag{5.4}
\]

and form the physical spectral frame whose first spectral column is `\sqrt c` on the heavy coordinate plus `\sqrt{1-c}\,u` on the residual bank, whose second and third columns are `v,w`. These three columns are orthonormal.

Use the spectral coefficient matrix

\[
M_0=
\begin{pmatrix}
0&1&0\\
1&0&0\\
0&0&1
\end{pmatrix}.                                                       \tag{5.5}
\]

Its spectrum is exactly `{1,-1,1}`. Hence the resulting physical matrix is an exact-rank-three **valid instance of the full target**. Its Witt form is

\[
Q=2\sqrt c\,HV+2\sqrt{1-c}\,UV+W^2,                               \tag{5.6}
\]

so `a=\sqrt c`, `\delta=1`, and

\[
S_i=a^2|\delta|=c=15/16.                                             \tag{5.7}
\]

But its physical-pair square-carrier minors are

\[
b_{jk}=0\quad\text{within either half},
\qquad
|b_{jk}|=\frac2N\quad\text{across the two halves}.                  \tag{5.8}
\]

There are `N^2/4` cross pairs, and therefore

\[
\sum_{j<k}b_{jk}^2
=\frac{N^2}{4}\frac4{N^2}=1,                                        \tag{5.9}
\]

while

\[
\max_{j<k}|b_{jk}|=\frac2N\longrightarrow0.                         \tag{5.10}
\]

The pairwise theorem therefore gives only

\[
\|p_Q\|_{\infty,\mathrm{ess}}
\le C_0 (N/2)^{2/3}(15/16)^{-1/3},                                  \tag{5.11}
\]

which diverges as `N^{2/3}` even though the exact target curvature (5.9) is constant. For the natural partition into the two halves, the partner cross-star mass is actually `M_{J,K}=1`, stronger than the generic `1/2` guarantee.

This is **not** a counterexample to QFORM. It is a target-valid counterexample to any proof that first chooses one physical square-carrier pair and only then pays reciprocal curvature.

## 6. The precise remaining implication

The calculations above isolate one exact missing theorem.

### `QFORM-WITT-CROSSSTAR-AGGREGATE-COAREA-v1`

For a source-disjoint partition `J,K`, with

\[
M_{J,K}=\sum_{j\in J,k\in K}b_{jk}^2,                               \tag{6.1}
\]

prove directly from the original product law, **before selecting any pair**, that

\[
\boxed{
\nu_{r,t}(E)
\le
C_{\rm ag}\,M_{J,K}^{-1/2}
\sqrt{\frac{|a|}{|\delta|}}
 r^{3/2}|E|^{1/2}
}                                                                    \tag{6.2}
\]

for one universal `C_ag` and all Borel `E`.

Any finite universal `C_ag` closes the near-coloop Witt endpoint, because account02/B05 supplies `M_{J,K}>=1/2` and the previous B05 compiler then gives a universal density constant. If the sharp pair constant `C_ag=K_0` were retained, (6.2), (4.1), and (1.8) would give

\[
\|p_Q\|_{\infty,\mathrm{ess}}
\le7.761982175236\,S_i^{-1/3}
<9.779484731488                                                   \tag{6.3}
\]

at `S_i>=1/2`.

The important point is not the numerical value in (6.3). The missing factor is now exact:

\[
\boxed{
\text{replace }|b_{jk}|^{-1}
\text{ from one physical-pair slice by }
\left(\sum_{j\in J,k\in K}b_{jk}^2\right)^{-1/2}
\text{ before inversion.}
}                                                                    \tag{6.4}
\]

Naively averaging the already-inverted pairwise bounds cannot do this: weighting (2.4) by `b_{jk}^2` and summing produces

\[
\frac{\sum_{j\in J,k\in K}|b_{jk}|}
     {\sum_{j\in J,k\in K}b_{jk}^2},                                \tag{6.5}
\]

which is `N/2` in the target-valid Walsh family (5.1)--(5.10). Thus the aggregation must occur at the coarea/Brascamp--Lieb level, before reciprocal minors appear.

## 7. Relation to live corrections and scope

This run respects all currently binding corrections.

1. **No independence after rotation.** The only rotation in Theorem 2.1 is inside two literal physical coordinates after conditioning the rest; it is only a determinant-one change of integration variables. No probabilistic independence of `U,V,W` is asserted.
2. **No arbitrary-joint coarea.** The proof uses `f_jf_k<=1` in original coordinates. The previous B05 generic-joint curved-slab counterexample remains valid and is not bypassed.
3. **No fiber supremum.** The Borel inverse-image length is integrated against the actual physical-pair product density before averaging the remaining coordinates.
4. **No pointwise oscillatory decay.** No Fourier decay is used.
5. **No small-tail deletion.** The shared variable `\kappa U` is retained exactly; Theorem 2.1 is uniform in `\kappa`, including the full interval `0\le\kappa<1/\sqrt7`.
6. **No single-minor claim.** Section 5 gives a target-valid family proving that one-pair selection is quantitatively insufficient.

A brief literature search did not locate a published theorem with the exact rough-product, curved Borel profile (6.2); this is only a search result, not a novelty claim.

## 8. Status and next action

**Full QFORM:** OPEN / not proved / not disproved.  
**Full continuity conclusion:** OPEN.  
**New proved claim:** `QFORM-WITT-PAIRWISE-PLUECKER-TUBE-v1`, equations (2.4), (2.14).  
**New exact identity:** `QFORM-WITT-PLUECKER-JACOBIAN-CONSERVATION-v1`, equations (3.2)--(3.4).  
**New target-valid method obstruction:** the Walsh family (5.1)--(5.11) forces `max|b_jk|=2/N` while total and cross Pluecker mass remain one.  
**Partner result actually applied:** account02/B05 max-cut gives (4.1), which combined with the new theorem yields the actual density inequality (4.5)--(4.6).  
**First unpaid implication:** `QFORM-WITT-CROSSSTAR-AGGREGATE-COAREA-v1`, equation (6.2).

The next B05 run should attack (6.2) as a two-bank nonlinear Brascamp--Lieb/coarea inequality. It should work with the independent source banks `J,K` supplied by the partner max-cut and retain the within-bank tails, rather than select a single cross edge or replace the projected triple by a generic bounded joint density.
