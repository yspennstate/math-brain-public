SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B07, 2026-09-23T10:03:06Z.
attacking: coordinate-minor selection via a determinant-weighted E3-to-E2 compilation for the double-anchor diffuse survivor, aiming to feed the mixed 3/2-volume receiver without selecting a tiny minor.

# fleet01/B07 r22 — exact fractional E2 shadow of an anchored E3 law

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: coordinate minor selection / GEOMETRY  
Status: `ESSENTIAL_STEP_APPLIED / NEW EXACT E3->E2 SHADOW COMPILER + 3/5 HUB-DIFFUSE REDUCTION / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`.

## 1. Scope and source boundary

The target remains the full unrestricted statement: for every dimension, independent real ORIGINAL-coordinate inputs with densities at most one, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^TAX` has a density with one universal essential-supremum bound, or give a target-valid counterexample. No Gaussian, moment, compact-support, connected-support, log-concavity, iid, or post-rotation independence hypothesis is added. Continuity is tracked separately.

Fresh owner control before the mathematical write remained revision `2026-09-22.15`, QFORM-only, with no B07 pause. The live correction ledger was read. This report does not use law-uniform pointwise Fresnel decay, arbitrary-joint rank-three coarea, positive conditional projection-height moments, naive fiber-sup integration, deletion of a nonzero small tail, or one reciprocal coordinate minor.

Completed sources actually used:

1. This slot's immediately preceding mixed-order theorem, `QFORM-MIXED-32-FRACTIONAL-COMPOUND-BL-v1`, at
   `yspennstate/math-open-problems@7bf5a0bd8a8d2fa12a5c2370811ecfe5d2cf7444`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B07/fleet01-B07-20260923T090322Z-r20/REPORT.md`.
   The present report first extends its packet definition from 0/1 packet selection to fractional packet coefficients in `[0,1]`, with the same proof.
2. Designated partner fleet02/B07, `QFORM-CROSS-FIBER-PLANCHEREL-v1`, at
   `yspennstate/math-open-problems@5266d24ea98d9bb5902c51a92eca0e3e38112e39`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B07/20260922T193347Z-b07-639234ec/REPORT.md`.
   Its one-sided physical-row-triple estimate is applied below at an actual determinant inequality.
3. The fresh fleet03/B07 r29 double-anchor branch at
   `yspennstate/math-open-problems@0e842117ca7ec8472538faa120677507f16b5c17`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260923T084007Z-fleet03-B07-qform-r29/REPORT.md`.
   On its standard collar it supplies
   `G > F^6/12824703626379264`.

Full QFORM and global continuity remain OPEN.

## 2. Fractional-packet extension of the mixed E3/E2 receiver

The r20 theorem was stated for subcollections of physical minors. Its proof in fact allows arbitrary fractional coefficients.

### Lemma 2.1 — `QFORM-FRACTIONAL-PACKET-MIXED-32-BL-v1`

Let `M` be an ORIGINAL-coordinate physical cross block. For `k=2,3`, let `theta_k(S,T)` be arbitrary coefficients in `[0,1]` on physical `k x k` minors, not all zero, and define

`Z_k = sum theta_k(S,T) det M[S,T]^2`.

Normalize the weights `theta_k det^2/Z_k` and let their row inclusion marginals be `alpha_i^(k)`. For `0<w<1`, put

`r=2+w`,
`p_i=w alpha_i^(3)+(1-w)alpha_i^(2)`,
`K_w=w^(-w)(1-w)^(-(1-w)) Z_3^w Z_2^(1-w)`.

If `1<=q<r/2` and `max_i p_i<=q/2`, then the full ambient quadratic form has a continuous density and

`||p_Q||_infinity <= [e r/((r-2q)sqrt(q))] K_w^(-1/(2r)).`      (2.1)

The symmetric column-side statement also holds.

#### Proof

In the diagonal-plus-Gram determinant expansion

`det(D_J+M^T D_I M)
 =sum_(k>=0) sum_(|S|=|T|=k)
 det M[S,T]^2 prod_(i in S)d_i prod_(j notin T)e_j`,

all terms are nonnegative. Therefore for each order `k=2,3` one may retain the fractional sub-sum

`S_k^theta=sum theta_k(S,T) det M[S,T]^2 monomial_(S,T)`

because `0<=theta_k<=1`. Weighted AM--GM with weights `theta_k det^2/Z_k` gives exactly the same monomial lower bound as in r20, with inclusion marginals computed from the fractional weights. The weighted geometric mean of the order-three and order-two bounds is unchanged. Every subsequent step in the r20 proof — Lieb--Brascamp--Lieb, sharp Hausdorff--Young, Jensen, entropy cancellation, envelope integration and Fourier inversion — depends only on `Z_3,Z_2` and these inclusion marginals. Hence (2.1) follows verbatim. QED.

This extension is useful because a determinant bank can now be thinned continuously while preserving exact determinant weights. No artificial weight larger than an actual determinant-square coefficient is introduced.

## 3. Exact anchored E3 -> complementary physical E2 shadow

Let `M` be a real physical cross block. Fix a physical row `i` and physical column `a`. Define the double-anchored third-volume bank

`G = sum_(|R|=|C|=3, i in R, a in C) det M[R,C]^2 >0`.          (3.1)

For every residual row pair `K` with `|K|=2`, `i notin K`, put

`g_K = sum_(|C|=3, a in C) det M[{i} union K,C]^2`,             (3.2)

so `G=sum_K g_K`. Normalize `mu_K=g_K/G`; its residual row inclusion marginals are

`rho_k=sum_(K contains k) mu_K`,                                (3.3)

and `sum rho_k=2`.

Let

`R_i=||M[i,:]||_2`,
`W_K=sum_(|T|=2) det M[K,T]^2
    =det(M[K,:]M[K,:]^T)`.                                     (3.4)

### Theorem 3.1 — `QFORM-ANCHORED-E3-EXACT-E2-SHADOW-v1`

For every residual row pair `K`,

`boxed: g_K <= R_i^2 W_K.`                                     (3.5)

Consequently there is a fractional physical `2 x 2` determinant packet avoiding row `i`, with total second-volume mass

`boxed: Z_2=G/R_i^2,`                                          (3.6)

whose normalized row-pair law is **exactly** `mu_K`. In particular its row inclusion marginals are

`alpha_i^(2)=0`,
`alpha_k^(2)=rho_k` for `k!=i`.                                (3.7)

#### Proof

By Cauchy--Binet,

`g_K <= sum_(|C|=3) det M[{i} union K,C]^2
      = det(M[{i} union K,:] M[{i} union K,:]^T).`              (3.8)

Write the `3 x 3` row Gram matrix in block form with the anchor row first:

`[[R_i^2, u^T],[u,G_K]]`,

where `G_K=M[K,:]M[K,:]^T` is PSD. If `G_K` is invertible, the Schur determinant identity gives

`det = det(G_K)(R_i^2-u^T G_K^(-1)u)
     <=R_i^2 det(G_K)=R_i^2 W_K.`                              (3.9)

The singular case follows by continuity (and if `W_K=0`, then the three-row Gram determinant is zero). This proves (3.5).

Because `G>0`, `R_i>0`. For every `K` with `W_K>0`, set

`eta_K=g_K/(R_i^2 W_K) in [0,1]`,                              (3.10)

and set `eta_K=0` when `W_K=0`. Assign the same fractional coefficient `eta_K` to **every** physical `2 x 2` minor with row pair `K`. Then the retained second-volume mass on row pair `K` is

`eta_K W_K=g_K/R_i^2`.                                        (3.11)

Summing gives (3.6), and after normalization the pair weight is

`(g_K/R_i^2)/(G/R_i^2)=g_K/G=mu_K`,                            (3.12)

which proves (3.7). QED.

This is an exact determinant-weighted shadow, not an existential one-minor extraction. Arbitrarily small individual `2 x 2` minors are harmless because only the complete pair-bank `W_K` is thinned.

## 4. A fixed 3/5 mixed-order payment

Let

`m_R=max_(k!=i) rho_k`.                                        (4.1)

### Theorem 4.1 — `QFORM-DOUBLE-ANCHOR-ROW-FLAT-PAYMENT-v1`

If

`m_R<=3/5`,                                                     (4.2)

then the full ambient quadratic form has a continuous density satisfying

`boxed:
 ||p_Q||_infinity
 <= C_shadow G^(-5/26) R_i^(2/13),
`                                                                  (4.3)

where

`C_shadow
 =13 e sqrt(5/6)
   (5/3)^(-3/26)(5/2)^(-1/13)
 =28.3425230588... .`                                          (4.4)

The same statement holds with rows and columns interchanged.

#### Proof

Use the anchored third-volume bank (3.1) as the order-three packet and the exact fractional order-two shadow from Theorem 3.1. Choose

`w=3/5`, `q=6/5`, `r=2+w=13/5`.                               (4.5)

On the anchor row,

`p_i=w*1+(1-w)*0=3/5=q/2`.                                    (4.6)

On a residual row `k`, Theorem 3.1 gives identical order-three and order-two marginals, so

`p_k=w rho_k+(1-w)rho_k=rho_k<=3/5=q/2`.                       (4.7)

Moreover

`q=6/5 < 13/10=r/2`.                                           (4.8)

Thus Lemma 2.1 applies. Here

`K_w=(5/3)^(3/5)(5/2)^(2/5)
     G^(3/5)(G/R_i^2)^(2/5)
    =(5/3)^(3/5)(5/2)^(2/5) G R_i^(-4/5).`                    (4.9)

Substitution into (2.1) gives (4.3)-(4.4). The Fourier proof supplies a continuous density vanishing at infinity. QED.

### Scale cancellation

If a branch supplies

`G>=c F^6`, `R_i<=F`,                                          (4.10)

then (4.3) becomes

`boxed:
 ||p_Q||_infinity
 <= C_shadow c^(-5/26) F^(-1).
`                                                                  (4.11)

The exponent cancellation is exact:

`G^(-5/26)R_i^(2/13)
 <=c^(-5/26)F^(-30/26+4/26)
 =c^(-5/26)F^(-1).`                                           (4.12)

This is why the shadow compiler is correctly scaled for the live `G~F^6` double-anchor branch.

## 5. Complementary concentrated-row branch: apply fleet02/B07 at an actual inequality

Define the `3/5`-heavy residual rows

`H={k!=i: rho_k>3/5}`                                          (5.1)

and the light marginal tail

`delta_R=sum_(k notin H) rho_k`.                               (5.2)

Because `sum rho_k=2`, `|H|<=3`.

### Theorem 5.1 — `QFORM-DOUBLE-ANCHOR-3OVER5-CORE-OR-SHADOW-v1`

For the double-anchored bank `G`, at least one of the following holds on the row side:

1. **shadow payment:** `max rho_k<=3/5`, and Theorem 4.1 pays the full form by (4.3);
2. **physical row-triple payment:** `delta_R<=1/2`, and the full form has a continuous density with

`boxed:
 ||p_Q||_infinity
 <=3 sqrt(e) (6/G)^(1/6);
`                                                                  (5.3)
3. **genuine hub-plus-diffuse survivor:** there is a residual row `h` with `rho_h>3/5` and simultaneously `delta_R>1/2`.

The same trichotomy holds on the column side.

#### Proof of branch 2 and designated-partner application

Suppose `delta_R<=1/2`. Under the residual pair law `mu`, the event that at least one selected residual row is light is bounded by the number of selected light rows. Therefore

`P(residual pair not subset H)
 <=E[# selected light rows]
 =delta_R<=1/2`.                                                (5.4)

Hence

`P(residual pair subset H)>=1/2`.                              (5.5)

There are at most `binom(3,2)=3` heavy residual pairs, so one physical pair `K_* subset H` has

`mu_(K_*)>=1/6`,
`g_(K_*)>=G/6`.                                                 (5.6)

Let `I_*={i} union K_*`, a fixed physical row triple. Summing over **all** column triples only enlarges the anchored sum, hence Cauchy--Binet gives

`det(M[I_*,:]M[I_*,:]^T)
 =sum_(|C|=3) det M[I_*,C]^2
 >=g_(K_*)
 >=G/6.`                                                        (5.7)

Now apply the completed designated-partner fleet02/B07 theorem `QFORM-CROSS-FIBER-PLANCHEREL-v1`, its one-sided full-row-rank `r=3` estimate,

`||p_Q||_infinity
 <=3 sqrt(e) det(M[I_*,:]M[I_*,:]^T)^(-1/6)`.                 (5.8)

Using (5.7) gives (5.3). The partner theorem retains arbitrary self blocks, outside couplings, affine terms, signs and extra ambient spectrum, and proves continuity. QED.

No single column triple is selected at any stage.

## 6. The only surviving double-anchor geometry: two residual hubs plus diffuse tails

Apply Theorem 5.1 on both physical sides. If neither side pays, then there are a residual row `h` and residual column `b` with

`rho_h>3/5`, `sigma_b>3/5`,                                   (6.1)

while the total residual marginal on coordinates of marginal at most `3/5` exceeds `1/2` on **each** side.

Because the row and column inclusion events in the same anchored third-minor law have probabilities `rho_h` and `sigma_b`, the union bound gives

`P(h in R and b in C)
 >=rho_h+sigma_b-1
 >1/5.`                                                         (6.2)

Therefore the fixed two-row/two-column anchored third-volume bank

`G_(i,h;a,b)
 :=sum_(k notin {i,h}, l notin {a,b})
    det M[{i,h,k},{a,b,l}]^2`                                  (6.3)

satisfies the dimension-free lower bound

`boxed: G_(i,h;a,b) > G/5.`                                   (6.4)

This is the new precise residual object. It is substantially narrower than the former generic double-anchor state: two physical rows and two physical columns are now fixed, yet the remaining row/column directions may stay fully diffuse. Selecting one extension `(k,l)` is still forbidden; the entire determinant-weighted bank (6.3) must be retained.

If the physical `2 x 2` pivot `B=M[{i,h},{a,b}]` is invertible, then the exact Schur identity gives the further structural equality

`G_(i,h;a,b)=det(B)^2 ||S||_F^2`,                              (6.5)

where `S` is the full rectangular Schur complement of `B` in `M`. Equation (6.5) is an identity, not a payment: the next receiver must average the product `det(B)^2 ||S||_F^2` before any reciprocal pivot loss. The singular-pivot case remains included in (6.3) and is not discarded.

## 7. Application to the live fleet03/B07 r29 H3 branch

The standard r29 H3 branch supplies

`G > F^6/D`,
`D=12824703626379264`.                                        (7.1)

### 7.1 Flat-residual side

If on either side every residual anchored marginal is at most `3/5`, Theorem 4.1 and `R_i<=F` (or the column analogue) yield

`||p_Q||_infinity
 < C_shadow D^(5/26) F^(-1)
 =35492.7720373... F^(-1).`                                   (7.2)

The density is continuous.

### 7.2 Small light-tail side

If on either side the corresponding `3/5` light-tail mass is at most `1/2`, Theorem 5.1 and the designated partner give

`||p_Q||_infinity
 <3 sqrt(e)(6D)^(1/6) F^(-1)
 =3225.78135224... F^(-1).`                                   (7.3)

Again the density is continuous.

### 7.3 Genuine survivor

Thus an unpaid r29 H3 state must have, on both sides, a residual hub of marginal `>3/5` and a light marginal tail `>1/2`; moreover (6.4) gives the fixed two-row/two-column bank

`boxed:
 G_(i,h;a,b)
 > F^6/64123518131896320.
`                                                                  (7.4)

This replaces the previous generic double-anchor debt by a much more rigid **double-pair anchored** determinant bank.

No universal lower bound on `F` is asserted here unless supplied by the surrounding branch. Equations (7.2)-(7.3) are therefore correctly scale-sensitive and are not promoted to a full universal theorem by themselves.

## 8. Why this advances the coordinate-minor problem

The key point is not the numerical constants. The exact identity (3.6) compiles every anchored `E3` determinant law into a **complementary physical E2 determinant packet of the right total scale**, while keeping the same residual row-pair distribution and avoiding the anchor row completely. This is exactly the geometry required by the mixed `E3/E2` Fourier receiver.

The obstruction is now explicit rather than hidden: the mixed receiver fails only when a residual coordinate carries too much of the determinant law. The `3/5` trichotomy either pays that geometry by the partner's one-sided row-triple theorem or forces a fixed second row/column hub plus a genuinely diffuse tail. In the latter case a fixed `2 x 2` physical pivot is present in more than one fifth of the entire double-anchor third-volume bank, but one still must not invert that pivot before averaging.

## 9. First unpaid implication

The first B07 debt is now

`QFORM-DOUBLEPAIR-ANCHOR-BANK-RECEIVER-v1`:

> Starting from a physical cross block with a fixed two-row/two-column third-volume bank `G_(i,h;a,b)` as in (6.3)-(6.4), and with genuine residual determinant-marginal tails on both sides, obtain a full-form density bound by averaging before reciprocal inversion. In the invertible-pivot subcase the exact currency is `det(B)^2 ||S||_F^2`; the receiver must retain arbitrary same-bank curvature, outside couplings, signs, and the true nonzero remainder. The singular-pivot face must be handled separately rather than excluded.

A natural next split is on the physical pivot `det(B)` versus the Schur Frobenius energy in (6.5), but any valid payment must be product-preserving and must survive the known diffuse-pair counterexamples where every individual extension minor is tiny.

Full QFORM and global continuity remain OPEN / NOT PROVED / NOT DISPROVED.
