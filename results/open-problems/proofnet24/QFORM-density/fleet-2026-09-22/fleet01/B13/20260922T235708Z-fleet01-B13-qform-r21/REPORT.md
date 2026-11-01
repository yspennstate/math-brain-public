SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 01, slot B13, 2026-09-22T23:57:08Z.
attacking: the exact-rank-three common-graph/tiny-leakage collar by combining the designated-partner combined-Gram paving result with the disjoint exterior-mass theorem before any reciprocal minor selection.

# fleet01/B13 r21 — every non-tiny combined light residual is paid

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Extremal product laws  
**Run:** `20260922T235708Z-fleet01-B13-qform-r21`  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING TARGET-LEVEL THEOREM / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

The full owner conjecture remains **OPEN / NOT PROVED**. This report proves a new exact-rank-three closure theorem inside the final one-heavy/two-transverse-bank geometry. It removes the designated partner's high-combined-leverage alternative whenever the **global** light-bank longitudinal Schur variance is bounded below. Consequently every still-unpaid instance in that geometry has one quantitative common graph plane with total squared longitudinal regression residual below `7/25600`.

No arbitrary-joint coarea inequality, conditional projection-density moment, pointwise law-uniform quadratic oscillatory decay, post-rotation independence, single-good-minor selection, bounded support, bounded diameter, single-interval extremality, or bounded fragment count is used.

## 1. Source-pinned state actually used

Fresh protected control was read from `yspennstate/math-research-brain` main; the owner control remains revision `2026-09-22.15`, QFORM only. The live correction inbox was reread before this write.

The designated partner `fleet02/B13` is used in two places.

1. **Exact bang-bang product reduction**

   `yspennstate/math-open-problems@604a08009638981da254a72f09a24dd50e3a3c94`

   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260922T115714Z-fleet02-B13-qform-480ba28b/REPORT.md`.

   For each fixed bounded slab kernel, the supremum over all independent one-dimensional densities `0<=f_j<=1`, `int f_j=1`, equals the supremum over arbitrary product indicators `1_{E_j}`, `|E_j|=1`, with zero loss. No interval or centered-set extremality is asserted.

2. **Combined-bank paving theorem**

   `yspennstate/math-open-problems@d61a6ae3f85a8910112b551d56d6636c71b0ea45`

   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260922T225728Z-fleet02-B13-extremal-r19/REPORT.md`.

   In the final exact-rank-three two-bank geometry it forms the full light Gram `S`, and if every physical light row has leverage at most `1/12` relative to `S`, its elementary Rademacher paving produces two disjoint full-rank original-coordinate banks. The proof actually yields

   `||p_Q||_infinity <= 4 C_1 (det S)^(-1/3)`,                    (1.1)

   where

   `C_1=(e sqrt(pi)/(2 sqrt(2))) Gamma(1/4)/Gamma(3/4)
        =5.039897503914386...`.

   The partner report inserted a lower bound on `det S` through its quantity `V`; below I instead insert the exact global regression determinant.

The exact two-bank geometry itself comes from fleet01/B13 r17,

`yspennstate/math-open-problems@01c524aa389abf1b9b58c852bfa11fc747ec5b59`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B13/20260922T190849Z-fleet01-B13-qform-r17/REPORT.md`.

After already-paid branches, one has exact rank three

`A=R Lambda R^T`, `R^T R=I_3`, `min |eig(Lambda)|>=1`,

one heavy original coordinate `i` with

`r_i=sqrt(c)u`, `c>3/10`,

and a light set `L=L_1 disjoint_union L_2`. Write

`r_j=t_j u+p_j`, `p_j in u^perp`,

and

`G=sum_(j in L) p_j p_j^T`,
`G_a=sum_(j in L_a) p_j p_j^T`.

The source gives

`G_a >= kappa I_2`, `kappa=7/800`,                            (1.2)

hence

`G=G_1+G_2 >=2 kappa I_2`, `det G>=4 kappa^2`.                (1.3)

The high-transverse-leverage branch is already paid, so throughout the surviving branch

`a_j:=p_j^T G^(-1)p_j <1/32` for every `j in L`.              (1.4)

The exterior-mass payment used below is fleet01/B13 r13,

`yspennstate/math-open-problems@0b5cf04790e5927df0efed8811a2a1295006e141`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B13/20260922T135910Z-fleet01-B13-qform-r13/REPORT.md`.

For any two disjoint full-rank original-coordinate banks with row Grams `S_G,S_H`, it gives the translation-uniform bound

`||p_Q||_infinity <=6 |det Lambda|^(-1/3)(det S_G det S_H)^(-1/6)`.
                                                                    (1.5)

Equivalently, if

`D_0=sum_(I cap J=empty, |I|=|J|=3) det(R_I)^2 det(R_J)^2`,

then the same random-coloring proof, which is local and does not require the selected rows to exhaust the frame, gives

`||p_Q||_infinity <=12 |det Lambda|^(-1/3) D_0^(-1/6)`.       (1.6)

All unused original coordinates may be conditioned; they produce only the fixed spectral translation already allowed in (1.5).

## 2. Exact global common-graph regression

For the full light cloud define

`h=sum_(j in L) t_j p_j`,
`w=G^(-1)h`,
`e_j=t_j-w^T p_j`,
`rho=sum_(j in L)e_j^2`.

Then

`sum_j e_j p_j=0`,                                                (2.1)

and the light spectral Gram

`S=sum_(j in L) r_j r_j^T`

has, after the determinant-one shear `(t,p) -> (t-w^T p,p)`, the exact block form

`S ~ diag(rho,G)`.                                                 (2.2)

Therefore

`boxed(det S=(det G) rho)`.                                      (2.3)

If `rho>0`, block inversion in the same sheared coordinates gives the exact leverage identity

`boxed(ell_j:=r_j^T S^(-1)r_j
       =a_j+e_j^2/rho)`.                                         (2.4)

Thus `rho` is the **single global common-graph defect**: `rho=0` iff all light rows lie in one graph plane over `u^perp`.

The designated partner's bankwise identity is compatible with (2.3): if `w_a=G_a^(-1)h_a` and `rho_a` are its two bank regressions, then

`rho=rho_1+rho_2+(w_1-w_2)^T(G_1^(-1)+G_2^(-1))^(-1)(w_1-w_2)`.
                                                                    (2.5)

The present proof pays `rho` directly rather than only its lower surrogate `V`.

## 3. Diffuse full-light leverage: the partner paving already pays every `rho>=kappa/32`

Assume first

`max_(j in L) ell_j <=1/12`.                                     (3.1)

The designated partner's rank-three Rademacher paving proof applies to `S` itself. By (1.1)--(1.3), whenever

`rho>=kappa/32`,                                                  (3.2)

we have

`det S=(det G)rho
       >=4 kappa^2 (kappa/32)
       =kappa^3/8`.                                               (3.3)

Hence

`||p_Q||_infinity
 <=4 C_1 (kappa^3/8)^(-1/3)
 =8 C_1/kappa
 <4607.907`.                                                      (3.4)

This is already stronger than the partner report's stated `V`-threshold formulation: no separate bankwise residual or slope-misalignment lower bound is needed once the **actual combined** `rho` is known.

## 4. High full-light leverage: a disjoint Pluecker channel is forced

It remains to treat

`rho>=kappa/32`                                                    (4.1)

when some light row `j` satisfies

`ell_j>1/12`.                                                      (4.2)

This is exactly the alternative left open in the designated partner report. The point is that the same high leverage that obstructs its paving forces a quantitative disjoint exterior-mass channel once combined with the heavy row and the already-proved transverse diffuseness (1.4).

Put

`G_0=G-p_j p_j^T`.                                                (4.3)

By the matrix determinant lemma and (1.4),

`det G_0=(1-a_j)det G >(31/32)det G`.                            (4.4)

### 4.1 Heavy-triple Pluecker mass avoiding `j`

For light `k,l !=j`,

`det(r_i,r_k,r_l)^2=c det_2(p_k,p_l)^2`.

Therefore two-dimensional Cauchy--Binet gives

`A_*:=sum_(k<l; k,l!=j) det(r_i,r_k,r_l)^2
     =c det G_0`.                                                (4.5)

Using `c>3/10`, (1.3), and (4.4),

`boxed(A_* > (93/80) kappa^2)`.                                 (4.6)

For a fixed `s!=j`, let `A_s` be the part of `A_*` with the heavy triple also containing `s`. Again by the 2D adjugate identity,

`A_s/A_*=p_s^T G_0^(-1)p_s`.                                   (4.7)

Sherman--Morrison and Cauchy--Schwarz in the `G^(-1)` metric give

`p_s^T G_0^(-1)p_s
 =a_s+(p_s^T G^(-1)p_j)^2/(1-a_j)
 <=a_s/(1-a_j)
 <1/31`.                                                        (4.8)

Hence

`boxed(A_s < A_*/31 for every s!=j)`.                           (4.9)

This is the needed anti-concentration of the heavy-triple mass over physical indices.

### 4.2 Light triples containing the high-leverage row

Let

`B_*:=sum_(m<n; m,n!=j) det(r_j,r_m,r_n)^2`.                    (4.10)

Cauchy--Binet plus the determinant lemma gives the exact identity

`B_*=det S-det(S-r_jr_j^T)
    =(det S) ell_j`.                                             (4.11)

Indeed the difference of the two Cauchy--Binet sums is exactly the sum of squared light `3x3` minors containing `j`.

By (4.1)--(4.2), (1.3), and (2.3),

`B_* >(det G)rho/12
     >=(4 kappa^2)(kappa/32)/12
     =kappa^3/96`.                                               (4.12)

For `s!=j`, let `B_s` be the portion of `B_*` whose light triple additionally contains `s`. Every pair `{m,n}` is counted twice, so

`sum_(s!=j) B_s=2B_*`.                                          (4.13)

### 4.3 The disjoint mass cannot disappear into overlaps

Pair a heavy triple `{i,k,l}` from (4.5) with a light triple `{j,m,n}` from (4.10). The pair fails to be disjoint only if the transverse pairs `{k,l}` and `{m,n}` share at least one light index `s`.

Therefore, by the union bound over the shared index and (4.9), the total overlapping product mass is at most

`sum_(s!=j) A_s B_s
 <(A_*/31) sum_s B_s
 =(2/31)A_*B_*`.                                                 (4.14)

Consequently the genuinely disjoint Pluecker mass satisfies

`D_0 >=(1-2/31)A_*B_*
      =(29/31)A_*B_*`.                                          (4.15)

Substituting (4.6) and (4.12),

`boxed(
 D_0 > (29/31)(93/80)(1/96) kappa^5
     = (899/79360) kappa^5.
 )`                                                              (4.16)

This is an aggregate-before-inversion statement. No individual `3x3` determinant is required to be large.

Apply the completed disjoint exterior-mass theorem (1.6), and use `|det Lambda|>=1`:

`boxed(
 ||p_Q||_infinity
 <12 [(899/79360) kappa^5]^(-1/6)
 <1313.656.
 )`                                                              (4.17)

Thus the high-combined-leverage branch is not an obstruction at all once the combined longitudinal volume `rho` is at least `kappa/32`.

## 5. Main new theorem

### `QFORM-RANK3-GLOBAL-LIGHT-RESIDUAL-CLOSURE-v1`

In the final exact-rank-three one-heavy/two-transverse-bank branch (1.2)--(1.4), if the combined light regression residual

`rho=min_(w in u^perp) sum_(j in L)(t_j-w^T p_j)^2`

satisfies

`boxed(rho>=kappa/32=7/25600)`,                                    (5.1)

then the full quadratic output has an essentially bounded density, uniformly over dimension, arbitrary cap-one product input laws, arbitrary support fragmentation, and all outside conditioned affine terms, with the explicit bound

`boxed(||p_Q||_infinity<4607.907)`.                               (5.2)

If all full-light leverages are at most `1/12`, (5.2) is (3.4). If one exceeds `1/12`, the stronger bound (4.17) applies.

The proof remains in original physical coordinate banks. The determinant-one regression shear is only spectral bookkeeping; it is never interpreted as an independence-preserving change of the random inputs.

## 6. Actual extremal-product inequality via the designated partner

Now apply `fleet02/B13`'s exact bang-bang theorem to the slab kernel. For every interval `J` and every family of arbitrary measurable sets `E_k` of Lebesgue measure one, throughout the branch (5.1),

`boxed(
 |{x in product_k E_k : x^T A x in J}|
 <=4607.907 |J|.
 )`                                                              (6.1)

Conversely the same constant controls every independent product law with densities in `[0,1]` and mass one. This is the requested B13 geometric form. No interval, centered-uniform, bounded-diameter, or bounded-fragment extremality is inserted.

## 7. Exact remaining rank-three collar

Combining (5.1) with the previous paid branches yields a sharper necessary condition for every still-unpaid sequence in the final mixed exact-rank-three geometry:

`boxed(
 rho<7/25600=0.0002734375.
 )`                                                              (7.1)

Equivalently, there is one vector `w in u^perp` such that

`sum_(j in L)(t_j-w^T p_j)^2<7/25600`.                           (7.2)

So **all** light spectral rows, across both independent banks simultaneously, lie within one common graph plane in total squared residual. This is stronger and cleaner than tracking two separate small residuals plus a slope-alignment surrogate.

Using the designated partner identity (2.5), (7.1) immediately implies

`rho_1+rho_2<7/25600`,                                            (7.3)

and, because `(G_1^(-1)+G_2^(-1))^(-1)>= (kappa/2)I`,

`||w_1-w_2||<1/4`.                                                (7.4)

The older common-graph/tiny-leakage collar is therefore recovered as a consequence of the single intrinsic condition (7.1), not as two independent assumptions.

The already-proved exact-graph/null-heavy-pivot endpoint from fleet01/B13 auto11 remains compatible: if `rho=0`, then each bank has zero residual and the same graph slope; when the heavy spectral pivot is exactly zero, that endpoint has the universal bound `<335.063`. The present theorem does **not** claim continuity from `rho=0` to small positive `rho`.

## 8. First unpaid implication

The next exact-rank-three implication is now

`QFORM-RANK3-NEAR-COMMON-GRAPH-CLOSURE-v1`:

> In the final one-heavy/two-transverse-bank geometry, close the state with the single global common-graph defect `rho<7/25600`, retaining the original product-bank provenance. The exact `rho=0` / zero-heavy-pivot endpoint is already paid, while a non-small heavy pivot is already paid by the completed Schur/fractional theorem. What remains is a stability mechanism for simultaneous small positive graph defect and near-null heavy pivot that does not invoke a false conditional projection cap or support-diameter continuity.

This is strictly narrower than `QFORM-NEARNULL-COMMON-GRAPH-OR-HIGHCOMBINEDLEVERAGE-v1`: the **high-combined-leverage branch is now paid whenever it can carry a non-tiny third-direction volume**.

After exact rank three is fully closed, the arbitrary-additional-spectrum bridge remains a separate full-target debt. Nothing in this report claims the unrestricted owner conjecture.

## 9. Corrections respected

The argument never uses:

- the refuted arbitrary-joint coarea inequality;
- positive moments of worst conditional projection densities;
- post-rotation independence;
- law-uniform pointwise quadratic van der Corput;
- one fixed good physical minor;
- bounded support, bounded diameter, a fixed fragment count, or centered intervals;
- a claim that a bounded 2D projection density by itself pays an indefinite quadratic pushforward.

The only conditioning is on original independent physical coordinates, and the only spectral shear is determinant-one algebra for Gram identities. The new exterior-mass payment aggregates disjoint original-coordinate triples before any inverse determinant is taken.
