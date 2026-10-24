SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B02, 2026-09-23T09:17:56Z.
attacking: integrated Fourier estimate — recurse the newest account02/B02 incident-(3+2) determinant compiler through its common-anchor E2 failure packet, using a second product-preserving cross-disjointness test before any local inverse is paid.

# account01/B02 — nested incident-3 / anchored-2 cross-disjoint Fourier compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T091756Z-account01-B02-qform-auto11-r27`  
**Status:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_ANALYTIC_THEOREM / FULL_QFORM_OPEN`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** proved on the new unweighted-`L1_t` branch; unrestricted continuity remains open.  
**Global universal `L1_t` criterion:** `OPEN_NOT_REFUTED`.

The target remains exactly the owner's unrestricted problem: independent ORIGINAL real coordinates with one-dimensional probability densities bounded by one, and an arbitrary real symmetric coefficient matrix with at least three eigenvalues of modulus at least one. No moment, support, log-concavity, identical-law, Gaussian, or post-rotation-independence assumption is used.

The new point is that the latest designated partner `account02/B02` result already forces a fixed residual physical row/column anchor carrying a constant fraction of `E2`. This run does not try to invert that anchor or identify its cross-only Schur packet with a true symmetric-pair Schur complement. Instead it mixes the original incident third-minor law with the **anchored** residual second-minor law. If the two laws have any quantitative cross-disjointness, sharp Hausdorff--Young gives a genuine unweighted Fourier integral. If they do not, a second exact failure certificate forces either a three-anchor residual `E2` concentration or a doubly anchored physical `E3` packet carrying a fixed fraction of the live third-volume currency.

## 1. Designated partner result actually applied

Fresh completed source:

`yspennstate/math-open-problems@94189deb89884b0dd57057041ec04f98a85e6764`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260923T091200Z-account02-B02-QFORM-auto11/REPORT.md`.

Its theorem `QFORM-INCIDENT32-CROSSDISJOINT-SHARP-HY-L1-v1` starts from a physical cross block

`B=A[I,J]`

between disjoint banks of original coordinates, fixes a physical row anchor `x in I` and column anchor `y in J`, and defines

`J3 = sum_(|R|=|T|=2) det B[{x} union R,{y} union T]^2`,          (1.1)

`N=B[I\{x},J\{y}]`,

`E2=e2(N^T N)`.                                                   (1.2)

The partner proves a direct `L1_t` estimate unless the normalized incident-third-minor law and the residual `E2` law have small row and column cross-disjointness. More importantly for the present run, if both of those first-level disjointness probabilities are `<eta`, it proves that some fixed physical residual row/column anchor `(i,j)` satisfies

`K := H2^(i,j)(N)
   = sum_(u!=i,v!=j) det N[{i,u},{j,v}]^2
   > (1-2eta) E2/4`.                                               (1.3)

At the partner's canonical scale `eta=1/16`,

`boxed: K>7E2/32.`                                                 (1.4)

The same report also records the exact algebraic identity, supplied by its account03/B02 partner,

`K=||aM-cr^T||_F^2`                                                (1.5)

when the residual block is written at `(i,j)` as `N=[[a,r^T],[c,M]]`. I use only the determinant definition (1.3), not a true-pair interpretation of (1.5).

In the live two-sided failure of the third-volume marginal gate at `q=4/3`, the partner further has

`boxed: J3>Z3/3,   Z3=E3(B).`                                      (1.6)

Equations (1.4) and (1.6) are applied to the new Fourier inequality in Section 5.

## 2. The anchored residual `E2` law

Assume `J3>0` and `K>0`. Let `mu3` be the normalized incident-third-minor law on residual pairs `(R,T)`, `|R|=|T|=2`:

`mu3(R,T)
 = det B[{x} union R,{y} union T]^2 / J3`.                         (2.1)

Let `kappa` be the normalized anchored residual-two law. It is naturally a law on one additional residual row `u!=i` and one additional residual column `v!=j`:

`kappa(u,v)
 = det N[{i,u},{j,v}]^2/K`.                                       (2.2)

Equivalently the sampled residual row pair is `{i,u}` and the sampled residual column pair is `{j,v}`.

Draw `(R,T)~mu3` and `(u,v)~kappa` independently. Define the second-level cross-disjointness probabilities

`delta_r^* = P( R cap {i,u} = empty )`,                            (2.3)

`delta_c^* = P( T cap {j,v} = empty )`.                            (2.4)

These are deterministic functions of the actual physical coefficient matrix. No random input coordinate is rotated or transformed.

## 3. Main theorem — `QFORM-INCIDENT3-ANCHORED2-CROSSDISJOINT-L1-v1`

### Theorem 3.1

In the setup above, if `delta_r^*>0`, then the full ambient quadratic-plus-affine form has a continuous density vanishing at infinity and

`boxed:
 integral_R |phi_Q(t)| dt
 <= 10*pi*e*2^(-1/5)
    (delta_r^* J3 K)^(-1/10).
}`                                                                  (3.1)

Consequently

`boxed:
 ||p_Q||_infinity
 <= 5*e*2^(-1/5)
    (delta_r^* J3 K)^(-1/10).
}`                                                                  (3.2)

The same conclusions hold with `delta_c^*` in place of `delta_r^*`, by transposing the physical cross block.

No outer cross edge is required to be nonzero. All same-bank quadratic curvature, all outside couplings, and all conditioning-generated affine terms are retained.

### Proof

Condition any original coordinates outside `I union J`. One-sided Weyl differencing in the original `J` bank gives exactly the source-valid inequality used by the designated partner,

`|phi_Q(t)|^2
 <= integral_(R^J)
      prod_(r in I) h_r((Bw)_r)
      prod_(s in J) g_s(w_s) dw`,                                 (3.3)

where

`h_r(z)=|psi_r(2tz)|`,

`g_s=f_s*tilde(f_s)`, `0<=g_s<=1`, `integral g_s=1`.              (3.4)

Thus arbitrary same-bank phases disappear only through legitimate differencing; no conditional-density cap or post-rotation independence is used.

Condition the product determinant law `mu3 tensor kappa` on the row-disjoint event

`E_r={R cap {i,u}=empty}`.                                        (3.5)

Let `mu3'`, `kappa'` be its two conditioned marginals and put

`D3=D(mu3'||mu3)`, `D2=D(kappa'||kappa)`.

Since the conditioned joint law has relative entropy exactly `log(1/delta_r^*)` from the independent product law, and relative entropy decomposes into the two marginal divergences plus mutual information,

`D3+D2 <= log(1/delta_r^*)`.                                      (3.6)

Write the residual-row inclusion marginals under `mu3'` and `kappa'` as `alpha_r^(3)`, `alpha_r^(2)`, and their residual-column inclusion marginals as `beta_s^(3)`, `beta_s^(2)`. Define

`alpha_x=1/2`,
`alpha_r=(alpha_r^(3)+alpha_r^(2))/2` for r!=x,                    (3.7)

`beta_y=1/2`,
`beta_s=(beta_s^(3)+beta_s^(2))/2` for s!=y.                      (3.8)

Both sampled residual row sets have size two and are disjoint pointwise under (3.5), so

`0<=alpha_r<=1/2`, `sum_(r in I) alpha_r=5/2`.                    (3.9)

On the column side no disjointness is needed:

`0<=beta_s<=1`, `sum_(s in J) beta_s=5/2`.                        (3.10)

Now put positive Gaussian parameters `d_r` on the row maps `w -> (Bw)_r` and `e_s` on the coordinate maps `w -> w_s`. In the exact diagonal-plus-PSD determinant expansion retain two nonnegative basis families.

**Incident-three family.** Choose the row map `x`, the two residual row maps `R`, and coordinate vectors outside `{y} union T`. The basis determinant is

`det B[{x} union R,{y} union T]`.

Weighted AM--GM with `mu3'` gives

`A3 >= J3 exp(-D3) d_x
       prod_(r!=x)d_r^(alpha_r^(3))
       prod_(s!=y)e_s^(1-beta_s^(3)).`                            (3.11)

**Anchored-two family.** Choose the coordinate vector `e_y`, the two residual row maps `{i,u}`, and coordinate vectors outside `{y,j,v}`. Expanding along `e_y`, its basis determinant is exactly

`det N[{i,u},{j,v}]`.                                              (3.12)

Therefore weighted AM--GM with `kappa'` gives

`A2 >= K exp(-D2) e_y
       prod_(r!=x)d_r^(alpha_r^(2))
       prod_(s!=y)e_s^(1-beta_s^(2)).`                            (3.13)

The full Gaussian determinant contains both positive sums. Hence

`det(D_J+B^T D_I B)
 >= A3+A2
 >=2 sqrt(A3 A2)`                                                  (3.14)

and therefore

`det(D_J+B^T D_I B)
 >=2 (J3K)^(1/2) exp[-(D3+D2)/2]
   prod_r d_r^alpha_r prod_s e_s^(1-beta_s).`                     (3.15)

Lieb's Gaussian characterization gives

`BL <=2^(-1/2) exp[(D3+D2)/4](J3K)^(-1/4)
       prod_r alpha_r^(-alpha_r/2)
       prod_s(1-beta_s)^(-(1-beta_s)/2).`                          (3.16)

Zero exponents are omitted by continuity, exactly as in the partner's endpoint-safe determinant argument.

For every `0<c<=1/2`, sharp Hausdorff--Young in the same Fourier normalization gives

`integral_R |psi_r(2tz)|^(1/c) dz
 <=(pi/|t|) sqrt(c)
   (1-c)^(-(1-c)/(2c)).`                                          (3.17)

Apply Brascamp--Lieb to (3.3). The powers `alpha_r^(alpha_r/2)` from (3.17) cancel the inverse-alpha factors in (3.16). Since

`-(1-u)log(1-u)<=u`, `0<=u<=1`,

and both sums in (3.9)-(3.10) equal `5/2`, the remaining row and column entropy factors are each at most `e^(5/4)`. Using (3.6),

`|phi_Q(t)|^2
 <=2^(-1/2)e^(5/2)pi^(5/2)
   (delta_r^* J3K)^(-1/4)|t|^(-5/2).`                             (3.18)

Thus

`|phi_Q(t)|
 <=min{1,
   2^(-1/4)e^(5/4)pi^(5/4)
   (delta_r^*J3K)^(-1/8)|t|^(-5/4)}.`                            (3.19)

Finally

`integral_R min(1,A|t|^(-5/4))dt=10 A^(4/5)`.                    (3.20)

Equations (3.19)-(3.20) prove (3.1). Fourier inversion gives (3.2), continuity, and vanishing at infinity. QED.

The proof is literally on the unreduced physical cross block. In particular neither the algebraic packet `aM-cr^T` nor a small coefficient remainder is substituted for a random quadratic form.

## 4. Exact second-level failure certificate

The new theorem also has an explicit complement.

Define the `kappa` other-row and other-column marginals

`w_u = sum_(v!=j) kappa(u,v)`, `u!=i`,                            (4.1)

`z_v = sum_(u!=i) kappa(u,v)`, `v!=j`.                            (4.2)

They are probability vectors. Let

`alpha_i=P_mu3(i in R)`, `beta_j=P_mu3(j in T)`.                 (4.3)

From the definition of `delta_r^*`, conditioning first on `(R,T)~mu3` gives the exact identity

`boxed:
 delta_r^*
 = E_mu3[ 1_{i notin R} (1-sum_(u in R) w_u) ].
}`                                                                  (4.4)

Indeed if `i in R` disjointness is impossible; otherwise the anchored pair `{i,U}` misses `R` exactly when `U notin R`. Similarly

`boxed:
 delta_c^*
 = E_mu3[ 1_{j notin T} (1-sum_(v in T) z_v) ].
}`                                                                  (4.5)

Consequently, for every `0<theta<1/2`, if

`max_u w_u <=theta`,                                               (4.6)

then

`delta_r^* >=(1-alpha_i)(1-2theta)`.                              (4.7)

Thus `delta_r^*<eta` implies

`alpha_i >1-eta/(1-2theta)`.                                      (4.8)

The column statement is identical.

Take the concrete values

`theta=1/4`, `eta=1/16`.                                          (4.9)

If both `delta_r^*,delta_c^*<1/16`, then at least one of the following holds:

1. **three-anchor residual-E2 row localization:** some `u!=i` has `w_u>1/4`, hence

   `sum_(v!=j) det N[{i,u},{j,v}]^2 > K/4`;                       (4.10)

2. **three-anchor residual-E2 column localization:** some `v!=j` has `z_v>1/4`, hence

   `sum_(u!=i) det N[{i,u},{j,v}]^2 > K/4`;                       (4.11)

3. **doubly anchored incident-third-volume:** if neither localization occurs, then by (4.8)

   `alpha_i>7/8`, `beta_j>7/8`.

   Hence under the single law `mu3`,

   `P(i in R and j in T)>3/4`,                                   (4.12)

   and therefore

   `boxed:
   M_(x,i;y,j)
   :=sum_(u notin {x,i},v notin {y,j})
       det B[{x,i,u},{y,j,v}]^2
   >3J3/4.
   }`                                                             (4.13)

No probabilistic independence between row and column minor selections is used in (4.12); it is only the union bound `P(A cap B)>=P(A)+P(B)-1` under `mu3`.

At the exact endpoint, (4.4)-(4.5) identify why disjointness can vanish: either the incident-third law is a true row/column coloop at the common anchor, or the anchored residual `E2` packet itself is localized onto one additional physical row/column.

## 5. Actual application to the newest account02/B02 failure branch

Now impose the live two-sided D' failure and then the latest partner's first-level cross-disjointness failure at `eta=1/16`. The partner supplies simultaneously

`J3>Z3/3`,                                                        (5.1)

`K>7E2/32`.                                                       (5.2)

### 5.1 New `L1_t` exit

If

`max(delta_r^*,delta_c^*)>=1/16`,                                (5.3)

Theorem 3.1 applies. From (5.1)-(5.3),

`delta^* J3 K
 > (1/16)(Z3/3)(7E2/32)
 = 7 Z3E2/1536`.                                                  (5.4)

Thus the full characteristic function obeys the genuine unweighted bound

`boxed:
 integral_R |phi_Q(t)|dt
 < 10*pi*e*2^(-1/5)(1536/7)^(1/10)
   (Z3E2)^(-1/10)
 <127.459 (Z3E2)^(-1/10).
}`                                                                  (5.5)

Fourier inversion yields the continuous-density estimate

`boxed:
 ||p_Q||infinity
 <5e*2^(-1/5)(1536/7)^(1/10)
  (Z3E2)^(-1/10)
 <20.286 (Z3E2)^(-1/10).
}`                                                                  (5.6)

This is an actual equation-level application of the newest designated partner result. It improves the partner report's `60.276774 (Z3E2)^(-1/10)` mixed-gate bound on this nested-disjoint subbranch and, unlike the previous B02 edge/E2 recursion, requires no nonzero outer cross edge.

### 5.2 New exact survivor when the nested Fourier exit also fails

Suppose both nested disjointness probabilities are `<1/16`. From Section 4 and (5.2), either

`boxed:
 some fixed (i,u;j) carries >K/4>7E2/128
}`                                                                  (5.7)

in the row-localized sense (4.10), or the transposed three-anchor statement holds, **or**

`boxed:
 M_(x,i;y,j)>3J3/4>Z3/4.
}`                                                                  (5.8)

Thus the newest partner's common-anchor `E2` survivor has been sharpened one full level: unless the characteristic function is already integrable, the obstruction is now either a fixed three-physical-anchor second-volume packet or a fixed two-row/two-column anchored third-volume packet carrying more than one quarter of the entire third exterior mass.

Neither (5.7) nor (5.8) is yet promoted to a universal density theorem. Doing so without a source-valid receiver is the next structural obligation.

## 6. Why the live corrections are respected

1. **No pointwise scalar van der Corput.** The only time decay comes after one-sided Weyl differencing, determinant Brascamp--Lieb, and sharp Hausdorff--Young. Fragmented phase-aligned scalar supports remain admissible.
2. **No post-rotation independence.** All active banks and anchors are literal original-coordinate sets. The determinant laws live only on coefficient minors.
3. **No arbitrary-joint coarea or conditional cap.** The proof uses only original-product differencing and one-dimensional sharp Hausdorff--Young.
4. **No cross-Schur/true-pair substitution.** Although `K=||aM-cr^T||_F^2`, the proof uses `K` only as the sum of actual physical squared `2x2` minors in (1.3).
5. **No law-uniform matrix perturbation.** Nothing is discarded because a coefficient is small.
6. **No reciprocal selected local minor.** Every quantitative currency is an aggregate squared-minor sum before any inverse is paid.

## 7. First unpaid implication

The new first unpaid interface is

`QFORM-DOUBLEANCHOR-Z3-OR-TRIPLEANCHOR-E2-RECEIVER-v1`:

> Starting from (5.7) or (5.8), retain arbitrary same-bank curvature and extra spectrum and produce either a direct `L1_t`/linear-small-ball receiver or a product-preserving reduction to an already-paid two-hub, rank-two-cross-plus-square, pair-log, grouped-bank, ridge, or exact-rank-three mechanism. The reduction must aggregate before reciprocal local conditioning. In particular, (5.8) should be treated as a fixed two-row/two-column **exterior-volume** resource, not as permission to invert its physical `2x2` corner.

The target-wide universal statement

`integral_R |E exp(i t X^T A X)| dt <= C`

remains `OPEN_NOT_REFUTED`: this run proves it on the displayed branch and produces no valid counterexample to it. Full bounded density and full continuity also remain open.

## 8. Finite algebra checks

As sanity checks only (not proofs), random rectangular matrices were used to verify to floating precision:

- the outer identity `J3=a^2 E2(S)` when a nonzero outer edge is available;
- the incident identity `K=||bD-qp^T||_F^2` for a selected residual anchor;
- formula (4.4) by direct enumeration of both determinant laws.

The symbolic determinant/entropy argument above is the proof. No Monte Carlo output is used to infer a universal density bound.
