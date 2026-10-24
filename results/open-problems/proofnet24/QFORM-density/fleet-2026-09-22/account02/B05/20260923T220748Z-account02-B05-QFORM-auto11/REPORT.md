SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B05, 2026-09-23T22:07:48.647517Z.
attacking: QFORM-HUB-WEDGE-INVARIANCE-v1 — convert the b-independent physical hub-triple determinant into a determinant-only rough density receiver, then spend the account03/B05 Pluecker compiler on its finite literal bi-star endpoint without selecting a dimension-dependent minor.

# account02/B05 — determinant-only null-pivot receiver and bi-star closure

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control revision: `2026-09-22.15`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **PROVED SUPPORTING THEOREM / LITERAL BI-STAR ENDPOINT CLOSED / FULL QFORM OPEN**  
Continuity: not claimed by the new theorem; the conclusion is an essential density bound from a uniform interval estimate.

## 1. First unpaid implication

The preceding B05 run reduced the rough small-coupling core to the critical punctured problem

\[
Q=2aHL+\gamma V^2+2bLP+\alpha L^2+\text{affine terms},
\tag{1.1}
\]

where `H` is one literal original cap-one coordinate, `L,V,P` are linear forms on the disjoint residual original coordinates, and in the live normalized core `a=1`, `|gamma|>=1`, while `L,V,P` are orthonormal coefficient vectors. The exact `b=0` endpoint is paid; every fixed `b!=0` is paid; the remaining issue is uniformity as `b->0` in the critical two-sheet/convex window.

This run proves that the **finite literal bi-star endpoint is not part of that obstruction**. A zero physical pivot plus any nonsingular physical `3 x 3` principal determinant already gives a determinant-only density bound, with no singular-value penalty. Combined with the fresh account03/B05 Pluecker compiler, this pays its Case C uniformly.

The first unpaid implication after this run is therefore

`QFORM-HUB-TWOBANK-AGGREGATE-WEDGE-v1`:

> in the small-`b` critical hub core, pay the compiler's genuinely aggregate Case A/B endpoints — especially the two independent near-complementary product banks — **before** selecting or inverting an individual Pluecker edge. The literal finite bi-star endpoint is now closed.

## 2. Determinant-only null-pivot theorem

### Theorem 2.1 — `QFORM-NULL-PIVOT-DET-ONLY-v1`

Let `X_0,X_1,X_2` be independent real random variables with probability densities bounded by one. Let

\[
q(x)=x^TMx+r^Tx+c,
\qquad M=M^T\in\mathbb R^{3\times3},
\]

and suppose

\[
M_{00}=0,\qquad \det M\ne0.
\tag{2.1}
\]

Then the law of `q(X_0,X_1,X_2)` has an essentially bounded density and

\[
\boxed{
\|p_q\|_{\infty,\mathrm{ess}}
\le C_0 |\det M|^{-1/3},
\qquad C_0=7.761982175235\ldots<7.762.
}
\tag{2.2}
\]

The same bound applies to an ambient quadratic form after conditioning every other original coordinate: arbitrary outside coefficients and cross-couplings become affine terms in the retained triple and do not alter `M`.

### Proof

Write

\[
u=(M_{01},M_{02}),\qquad s=\|u\|_2.
\]

Since `M_00=0` and `det M!=0`, necessarily `s>0`. Choose an orthogonal `2 x 2` matrix `R` that sends `u` to `(s,0)`, and put

\[
(Y_1,Y_2)^T=R^T(X_1,X_2)^T.
\]

No independence is asserted between `Y_1,Y_2`. What is preserved is exactly what is needed: because the original pair has joint density `f_1(x_1)f_2(x_2)<=1` and `|det R|=1`, the transformed pair has joint density at most one. It remains independent of `X_0`.

In these coordinates the quadratic block is

\[
\widetilde M=
\begin{pmatrix}
0&s&0\\
s&\beta&\delta\\
0&\delta&\eta
\end{pmatrix}.
\tag{2.3}
\]

If the affine term has coefficient `r_0` on `X_0`, translate `Y_1` by `r_0/(2s)`. Translation preserves the joint density cap and absorbs that term into `2sX_0Y_1`; it changes only the remaining affine/constant coefficients. Now scale only the genuine independent hub,

\[
H=sX_0.
\]

Its density cap is at most `1/s`. The pair `(Y_1,Y_2)` has joint density cap at most one. Therefore the already proved B05 theorem `QFORM-NULL-HUB-TRANSVERSE-SQUARE-v1` applies to

\[
2HY_1+\beta Y_1^2+2\delta Y_1Y_2+\eta Y_2^2+\text{affine},
\]

and gives

\[
\|p_q\|_{\infty,\mathrm{ess}}
\le C_0 s^{-2/3}|\eta|^{-1/3}.
\tag{2.4}
\]

But expansion of (2.3) along the first row gives

\[
\det \widetilde M=-s^2\eta.
\tag{2.5}
\]

Orthogonal change of the last two coordinates preserves determinant, so `|det M|=s^2|eta|`. Substituting into (2.4) proves (2.2). QED.

### Why this theorem is special

A determinant alone does **not** generally control a three-variable quadratic density. The cancellation here uses the literal zero diagonal: the bad conditioning of the hub slope and the transverse square coefficient cancel exactly through

\[
|\det M|=s^2|\eta|.
\]

Thus no smallest-singular-value or bounded-entry hypothesis is being smuggled in.

## 3. The punctured coupling does not enter any physical hub-triple determinant

Return to (1.1). For residual original coordinates `j,k`, let

\[
\Delta_{jk}=l_jv_k-l_kv_j.
\tag{3.1}
\]

The quadratic block on the physical triple `{H,j,k}` has hub row `a(l_j,l_k)` and residual block

\[
B_{jk}
=
\gamma vv^T
+b(lp^T+pl^T)
+\alpha ll^T
\quad\text{restricted to }\{j,k\}.
\]

A direct bordered-determinant expansion gives the exact identity

\[
\boxed{
\det A[\{H,j,k\}]
=-a^2\gamma\,(l_jv_k-l_kv_j)^2
=-a^2\gamma\,\Delta_{jk}^2.
}
\tag{3.2}
\]

Every term carrying an `l` factor in the residual block vanishes against the bordered wedge. In particular, **the determinant is exactly independent of `b`, `p`, and `alpha`**. The same remains true for the translated square `gamma(V+sL)^2`, since its additional `LV` and `L^2` pieces also carry an `l` factor.

Combining (3.2) with Theorem 2.1 yields the ambient conditional estimate

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
\le C_0\bigl(|a|^2|\gamma|\,\Delta_{jk}^2\bigr)^{-1/3}
}
\tag{3.3}
\]

for every physical residual pair with `Delta_jk!=0`, uniformly in the punctured coupling `b` and in all outside coefficients. This is the promised `QFORM-HUB-WEDGE-INVARIANCE-v1` receiver.

## 4. Fresh account03/B05 r33 applied: the literal bi-star endpoint is paid

The newest compatible partner report is

`yspennstate/math-open-problems@4f1f31064431e8bb0d0be813ed5540d0b12ab590:`
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260923T214237Z-account03-B05-QFORM-r33/REPORT.md`.

Its deterministic core applies to **any** Parseval two-frame. Apply it here to

\[
g_j=(l_j,v_j),\qquad \sum_j g_jg_j^T=I_2.
\tag{4.1}
\]

For a current subset `K`, write

\[
G_K=\sum_{j\in K}g_jg_j^T,
\qquad D_K=\det G_K.
\]

If a row `h` has current whitened leverage

\[
q_h^{(K)}=g_h^TG_K^{-1}g_h\ge\frac12,
\]

r33 proves the exact peel identity

\[
\boxed{
D_{K\setminus\{h\}}=D_K(1-q_h^{(K)}),
}
\tag{4.2}
\]

so each heavy peel halves the remaining internal Pluecker determinant. With r33's threshold

\[
\eta=\frac1{64},
\]

a first threshold crossing occurs after at most six heavy peels. Its Case C gives a literal row `h_k` such that

\[
\sum_{r<k}\Delta_{h_kh_r}^2>\frac1{128},
\qquad
\sum_{i\in K_k}\Delta_{h_ki}^2>\frac1{128}.
\tag{4.3}
\]

There are at most five previously peeled rows. Hence the **finite side** of (4.3) contains an actual edge with

\[
\boxed{
\Delta_{h_kh_r}^2>\frac1{640}
}
\tag{4.4}
\]

for some `r<k`. This is exactly where a single-edge extraction becomes safe: the cardinality is universally bounded by five, so no dimension-dependent reciprocal-minor loss occurs.

Apply (3.3) to the physical triple `{H,h_k,h_r}`. We obtain

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
< C_0\,640^{1/3}
|a|^{-2/3}|\gamma|^{-1/3}
<66.891\,|a|^{-2/3}|\gamma|^{-1/3}.
}
\tag{4.5}
\]

In the live normalized core `a=1`, `|gamma|>=1`, therefore

\[
\boxed{\|p_Q\|_{\infty,\mathrm{ess}}<66.891.}
\tag{4.6}
\]

This closes the r33-style **literal bi-star Case C** for the rough hub/two-sheet core. The second star in (4.3) is not even needed once the zero-pivot determinant receiver is available.

The threshold is tunable. Re-running the same exact r33 determinant identities with any `eta<1/4` gives a three-way tradeoff. For example `eta=1/5` forces a threshold crossing by the third heavy peel; in its Case C there are at most two earlier rows and one gets `Delta^2>1/20`, hence the sharper isolated Case-C constant

\[
C_0 20^{1/3}<21.070.
\]

I keep the partner's `eta=1/64` as the live compiler because its unresolved Case B is much closer to two complementary rank-one banks (`1/32` operator tails), which is more useful for the next step.

## 5. Required pinned `e5f71d79...` source applied to the actual obstruction

The required source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:`
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`

was read through `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

Two completed results are used to remove branches before the new compiler is needed.

1. **Fresnel-Brascamp-Lieb diffuse gate.** Theorem F gives
   \[
   \|p_Q\|_\infty\le12
   \tag{5.1}
   \]
   for an exact-rank-three active frame when every original-coordinate leverage is at most `1/2`. Thus an unpaid exact-rank-three instance reaching the present hub compiler is necessarily on a high-leverage side; the heavy-row mechanism is not an artificial case split.

2. **Ruled one-sheet gate.** For exact-rank-three signature `(2,1)`, Theorem C gives
   \[
   p_Q(s)\le\pi\sqrt2,\qquad s\ge0,
   \tag{5.2}
   \]
   on the ruled one-sheet side. Consequently the geometric endpoint still requiring new work is the complementary convex/two-sheet side (and the definite signature), precisely the side on which the small-`b` critical hub core arose.

The pinned counterexample search reports no target-valid counterexample. Equation (4.6) additionally shows that a high-leverage literal bi-star cannot furnish one: its full output law is uniformly bounded before any `b->0` limit is taken.

## 6. What remains after the new closure

The partner compiler's geometric endpoints now separate cleanly for this hub frame.

- **Literal bi-star (Case C): PAID** by (4.6).
- **Two-sided aggregate Pluecker mass (Case A):** still requires spending an aggregate bank crossing without selecting a potentially tiny individual edge when the third `P` direction overlaps the same product banks.
- **Near-complementary two-bank endpoint (Case B):** `det G_K,det G_H<=1/64`, each bank is within `1/32` in operator norm of a complementary rank-one coefficient-plane projection, and cross Pluecker mass is at least `31/32`. The small coefficient tails cannot be deleted as random errors; they must remain inside the product integral.

Thus the next theorem should be an **aggregate null-hub/two-bank receiver** whose cost depends on a bank determinant or total Pluecker mass, not on `max_{jk}|Delta_jk|^{-1}`. The exact physical determinant invariance (3.2) strongly suggests that `b` should disappear from the final currency if the aggregation is done before reciprocal inversion.

## 7. Integrity and scope

- Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**.
- No moments, bounded support, log-concavity, identical laws, Gaussianity, or connected support are assumed.
- No post-rotation independence is used: the rotated physical pair in Theorem 2.1 is treated only through its joint density cap.
- No arbitrary-joint 3D coarea theorem is used.
- No conditional density-cap moment is used.
- No unrestricted curved-fiber supremum is taken.
- No small coefficient is discarded as a small random variable.
- Essential boundedness is proved in the stated branches; continuity is separate.
- The determinant identity (3.2) and constants were checked independently by symbolic/algebraic computation; the computation is saved with this run.

Independent review of the new theorem is **PENDING**.
