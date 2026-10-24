SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B08, 2026-09-23T06:42:47.604019Z.
attacking: the actual-spectral-gate hybrid after the newest account03/B08 2/3 barrier — strengthen the fixed double-nested packet, feed it into the physical-core compilers, and isolate a source-valid rank-one-chain obstruction without deleting tails.

# account02/B08 r23 — near-2/3 anchored router, core receiver, and double-anchor Schur obstruction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Diffuse eigenvector case / complementary constructions and source-valid counterexamples  
**Run:** `20260923T064247Z-account02-B08-qform-diffuse-r23`  
**Classification:** `NEW SUPPORTING ROUTER + EXACT STRUCTURAL IDENTITY + TARGET-VALID MECHANISM OBSTRUCTION / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (`full_brain_connected=false`).

## 1. Target, corrections, and first unpaid implication

The unrestricted target remains OPEN: for arbitrary finite dimension, independent real ORIGINAL coordinates with probability densities bounded by one, and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one, prove one universal finite essential-density bound for `Q=X^TAX`, or give a genuine counterexample. Continuity is separate.

This run uses no moments, support diameter, connectedness, log-concavity, iid assumption, independence after spectral rotation, law-uniform pointwise stationary phase, arbitrary-joint coarea estimate, positive moment of a worst conditional projection height, one-good-minor extraction, or deletion of a small matrix tail. In particular the fresh correction `QFORM-UNIFORM-MATRIX-PERTURBATION-CONTINUITY-FALSE-v1` is respected: a small matrix perturbation is never treated as a uniformly small random quadratic perturbation for arbitrary unbounded cap-one sources.

The first unpaid implication at entry was the previous B08 state

`QFORM-DIFFUSE-DOUBLE-NESTED-OR-STAR-PAYMENT-v1`:

> after the actual spectral gate, consume either a physical cross-star or a fixed two-row/two-column aggregate third-determinant packet, while keeping arbitrary same-bank curvature, all complementary spectrum, and original-coordinate product provenance.

This run strengthens that packet using the newest designated partner `account03/B08` result, then converts it to an explicit receiver tree. One subbranch is continuously paid. The remaining obstruction is no longer an undifferentiated determinant packet.

## 2. Sources actually applied

1. **Immediate B08 router.** `yspennstate/math-open-problems@2e8dce7760ed0b7dc1ab1be7b9d82ecc3c7b7df1`, account02/B08 r21, proves: if an ORIGINAL-coordinate cross block `B` has `Z_3=e_3(B^TB)>=zeta^6`, then either the full ambient form is continuously paid by `<18.218/zeta`, or there is a row/column anchor `(i,a)` whose incident third-volume `W_ia` satisfies

   `W_ia > (38/125) Z_3`,

   with the remaining failure encoded in physical anchor-star / conditional anchored-volume structure.

2. **Newest designated partner.** `yspennstate/math-open-problems@c58aa132fd02c6e739650559cf25a6754fad5435`, account03/B08 r29, theorem `QFORM-ANCHORED-VARIABLE-MIXTURE-v1`. For anchored third-volume `W`, anchor-row norm `R`, residual occupancy `h_0`, mixture parameter `theta`, and `q`, if

   `max(theta,h_0)<=q/2`, `q>=1`, `2+theta>2q`,

   then the FULL ambient form has a continuous `C_0` density bounded by

   `e q^(-1/2) (2+theta)/(2+theta-2q)
      W^(-1/(2(2+theta))) R^((1-theta)/(2+theta))
      [theta^theta(1-theta)^(1-theta)]^(1/(2(2+theta))).`      (2.1)

   The same holds after transposing the physical cross block. The partner also proves that `2/3` is the exact occupancy barrier of this particular order-3/order-2 self-matched Jensen mechanism.

3. **Physical packet compilers used through the partner proof tree.** Account03/B07 r25, `yspennstate/math-open-problems@5e2f0ed9c6f5b7621d6344af21b13a05234fdd47`, converts a fixed one-sided nested third-volume packet `P_1` into either

   `||c|| ||w_1|| ||w_2|| >= sqrt(P_1)/6`                      (2.2)

   on three disjoint ORIGINAL-coordinate banks, or an edge-star-core packet

   `|e| ||s|| ||N||_F >= sqrt(P_1)/(6sqrt(2)).`                (2.3)

   Account03/B07 r26, `yspennstate/math-open-problems@67a8e05e237bc914ad0563e361f6eb035b76e7fe`, sends `G=||N||_F` into the exhaustive R1/E2/VOL/BICORE quadrichotomy. In the VOL case it proves the full-ambient continuous bound

   `||p_Q||_infinity < (27e/2) G^(-1).`                         (2.4)

4. **Required Claude/e5f source applied to an actual target family.** `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `FOURIER_ROUTE_REPORT.md`, Proposition H: three independent physical blocks can be combined by Holder in frequency; in particular `2(X_1X_2+X_3X_4+X_5X_6)` has density at most `3`. Section 7 below applies this to the rank-one-chain stress family after product-projection normalization, giving `<3*2^(1/3)<3.78`.

5. **Product projection currency.** The compatible completed account04/B18 consequence at `yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061` gives, on an ORIGINAL-coordinate cap-one product bank,

   `||p_(u^T X)||_infinity <= sqrt(2)/||u||_2`.                (2.5)

It is used only as linear product currency, never as an arbitrary curved pushforward theorem.

## 3. New near-2/3 anchored router

Fix

`h = theta = 83/125`,  `q=166/125`.                            (3.1)

Then

`2+theta =333/125`,
`2+theta-2q =1/125>0`,
`q/2=h`,                                                        (3.2)

so the newest partner theorem applies whenever the largest residual anchored row marginal is at most `h`. Let `B` satisfy

`Z_3=e_3(B^TB)>=zeta^6`.                                       (3.3)

Suppose the r21 fractional-volume payment has not already occurred. Then there is a physical row/column anchor `(i,a)` with

`W:=W_ia > (38/125)Z_3 >= (38/125)zeta^6`.                    (3.4)

Assume also that no physical row or column cross-star has norm `>zeta`; in particular the anchor-row and anchor-column norms are at most `zeta`.

### Theorem 3.1 — `QFORM-DIFFUSE-83/125-DOUBLE-NESTED-ROUTER-v1`

Under (3.3)-(3.4), one of the following holds:

1. the full ambient quadratic form has a continuous `C_0` density with

   `||p_Q||_infinity < 872/zeta`;                               (3.5)

2. some physical row or column cross-star has norm `>zeta`; or

3. there are fixed distinct physical rows `i,k` and fixed distinct physical columns `a,b` with

   `P_{ik;ab}:=sum_(ell,c)
      det B[{i,k,ell},{a,b,c}]^2
      > (1558/15625) Z_3
      >= (1558/15625) zeta^6.`                                 (3.6)

Here `ell,c` range over residual rows/columns, and no individual minor is selected.

#### Proof

Assume alternative 2 fails. Consider the normalized anchored order-three determinant-square law on the packet `W` in (3.4). If every residual row marginal is at most `h`, apply the partner theorem (2.1) with (3.1), `R_i<=zeta`, and (3.4). The scale exponent is exactly `-1` because

`-6/[2(2+h)] + (1-h)/(2+h) = -1`.                              (3.7)

Thus

`||p_Q||_infinity <= C_h/zeta`,                                 (3.8)

where

`C_h = e (166/125)^(-1/2) 333
       (38/125)^(-125/666)
       [(83/125)^(83/125)(42/125)^(42/125)]^(125/666)`         (3.9)

and the checker gives

`C_h=871.294970001098...<872`.                                  (3.10)

The same argument applies after transposition if every residual column marginal is at most `h`.

If neither orientation is paid, choose a residual row `k` and residual column `b` whose conditional inclusion probabilities are both `>83/125` under the SAME anchored order-three law. Their simultaneous conditional inclusion probability is greater than

`2(83/125)-1 = 41/125`.                                        (3.11)

Therefore the fixed double-nested packet carries more than `(41/125)W`; by (3.4),

`P_{ik;ab} > (41/125)(38/125) Z_3
            = (1558/15625) Z_3`.                               (3.12)

This proves the theorem. The value `83/125` is chosen close to, but strictly below, the partner's exact `2/3` barrier; it strengthens the packet without making the paid constant exceed the downstream core payment below. QED.

The new packet fraction is `1558/15625=0.099712`, versus `19/500=0.038` in B08 r22.

## 4. New no-star receiver for the strengthened packet

Assume alternative 3 of Theorem 3.1 and still no star `>zeta`. Let `P_1` be the complete one-sided nested packet fixing rows `i,k` and column `a`. Since the double-nested packet (3.6) is a subpacket,

`P_1 >= P_{ik;ab} > c_* zeta^6`,
`c_*:=1558/15625`.                                              (4.1)

Apply account03/B07 r25 to `P_1`.

### S branch — three genuinely independent scalar banks

Equation (2.2) gives

`||c|| ||w_1|| ||w_2||
 > sqrt(c_*) zeta^3 /6
 =0.0526286782826... zeta^3.`                                  (4.2)

The three supports are disjoint ORIGINAL-coordinate banks. Applying (2.5) on each bank and multiplying genuine independent densities yields the actual joint linear-density cap

`||p_(c^T X,w_1^T X,w_2^T X)||_infinity
 < 2sqrt(2) / (||c||||w_1||||w_2||)
 < [1500sqrt(2)/sqrt(1558)] zeta^(-3)`                         (4.3)

and hence

`boxed: joint cap <53.744 zeta^(-3).`                           (4.4)

This is product-linear currency only; the live arbitrary-joint coarea correction forbids promoting (4.4) by itself to the desired curved density bound.

### E branch — edge-star-core

Equation (2.3) gives

`|e| ||s|| G > sqrt(c_*) zeta^3/(6sqrt(2)),
 G:=||N||_F.`                                                   (4.5)

The edge and star in the r25 construction are literal subobjects of the two fixed anchor rows. Since the global star exit has failed,

`|e|<=zeta`, `||s||<=zeta`.                                    (4.6)

Therefore

`boxed:
 G > g_* zeta,
 g_*:=sqrt(c_*)/(6sqrt(2))
     =0.0372140952985... .`                                    (4.7)

Now apply account03/B07 r26 to the ACTUAL residual core `N`.

**VOL.** The full ambient form is continuously paid by

`||p_Q||_infinity
 <(27e/2)G^(-1)
 <[10125 e sqrt(2)/sqrt(1558)] zeta^(-1)
 =986.099605265... zeta^(-1)
 < boxed(987/zeta).`                                            (4.8)

**R1.** The core is an honest relative rank-one tube,

`dist_F(N,{rank<=1})<G/2`,                                     (4.9)

while both (4.5) and the size floor (4.7) remain present. No tail is dropped.

**E2.** The core has

`E_2(N)>=3G^4/16
 >3.5960948148e-7 zeta^4`,                                     (4.10)

and four disjoint physical subbanks with the matched Frobenius-product reserve

`P_match>=3G^4/256
 >2.2475592592e-8 zeta^4`.                                     (4.11)

**BICORE.** There are an actual physical row and column of `N` with star norms each exceeding

`sqrt(2/27)G
 >0.0101283938578... zeta`.                                    (4.12)

### Theorem 4.1 — `QFORM-DIFFUSE-POST-2/3-CORE-ROUTER-v1`

Combining Sections 3-4: for every ORIGINAL-coordinate cross block with `Z_3>=zeta^6`, the full ambient form is either continuously paid by `<987/zeta`, or a physical star exceeds `zeta`, or one of four explicit product-preserving survivors remains:

- an S-branch of three disjoint linear banks satisfying (4.2)-(4.4);
- an edge-star plus relative-rank-one core satisfying (4.5), (4.7), (4.9);
- an edge-star plus aggregate E2/four-bank core satisfying (4.5), (4.7), (4.10)-(4.11);
- an edge-star plus two-sided heavy core satisfying (4.5), (4.7), (4.12).

The former fixed double-nested packet is therefore no longer itself an unpaid terminal state.

## 5. Feed the router back into the actual spectral gate

Use the B08 actual spectral gate at `yspennstate/math-open-problems@9fb59f9549a85af6173ade505fd53bc035c611ba`, with selected three-eigenvector leverage at most `1/48` and

`beta=(3/16)sqrt(3/5)L=0.145236875482778...L`.                  (5.1)

Retain all previously paid low-rank-tube and fifth-volume exits. The relevant volume scales from r21-r22 are

`zeta_0=beta`,
`zeta_1=beta/14400^(1/6)=0.0294453337964...L`,
`zeta_2=(beta/120)/225^(1/6)=0.000490755563273...L`.            (5.2)

On the new packet/core tree, the partner payment (3.5) and the new VOL payment (4.8) become:

| actual child count | partner payment | core-VOL payment | core floor `G/L` | BICORE star floor / `L` |
|---|---:|---:|---:|---:|
| `k=0` | `<6000/L` | `<6790/L` | `>0.00540485` | `>0.00147101` |
| `k=1` | `<29591/L` | `<33490/L` | `>0.00109578` | `>0.00029823` |
| `k=2` | `<1.776e6/L` | `<2.010e6/L` | `>1.8263e-5` | `>4.9705e-6` |

These constants are intentionally not optimized. The important point is structural: after the explicit ACTUAL principal-spectrum gate, the double-nested survivor is replaced by a finite physical receiver tree with quantified dimension-free scales, while all complementary spectrum and same-side curvature remain untouched.

The genuine rank-one/rank-two cross tubes already present in the `k=1,2` spectral branches remain parallel open states; nothing here silently promotes them to exact low rank.

## 6. Exact double-anchor Schur identity

The downstream tree above does not require an invertible local anchor. The reason is visible in a useful exact identity.

Fix the same two physical rows and columns and write, after physical permutations only,

`B = [[ C, U ],
      [ V, N ]]`,                                               (6.1)

where `C` is `2x2`, `U` is `2 x q`, `V` is `p x 2`, and `N` is `p x q`. Put `d=det C`. For every residual row `ell` and residual column `c`, the bordered determinant identity gives

`det [[C,u_c],[v_ell^T,n_ellc]]
 = d n_ellc - v_ell^T adj(C) u_c.`                              (6.2)

Summing squares yields the exact packet identity

`boxed:
 P_{ik;ab}
 = || d N - V adj(C) U ||_F^2.`                                (6.3)

Call (6.3) `QFORM-DOUBLE-ANCHOR-SCHUR-PACKET-v1`.

If `C` is invertible, this is the usual Schur residual identity

`P_{ik;ab}=|det C|^2 ||N-VC^{-1}U||_F^2`.                      (6.4)

But (6.3) remains valid at a singular anchor. If `rank C=1`, then `adj(C)` also has rank one; a large packet can be carried entirely by the chain `V adj(C) U` even when `det C=0` and `N=0`. Therefore:

> a large fixed double-nested packet does **not** force either a uniformly invertible `2x2` anchor or a nonzero residual block after deleting both anchor row/column pairs.

This is an exact structural obstruction, not a probabilistic heuristic.

## 7. Target-valid rank-one-chain stress family and actual e5f payment

For `m>=2`, define the `(m+2)x(m+2)` physical cross block `M_m` by

- `M_m(1,1)=1`;
- row `2` has value `m^(-1/2)` on columns `3,...,m+2` and zero elsewhere;
- column `2` has value `m^(-1/2)` on rows `3,...,m+2` and zero elsewhere;
- every other entry is zero.

Equivalently it is the direct sum of three rank-one blocks: one scalar edge and two mutually disjoint unit-norm stars. Hence its nonzero singular values are exactly

`s_1(M_m)=s_2(M_m)=s_3(M_m)=1`.                                (7.1)

Set

`A_m=[[0,M_m],[M_m^T,0]].`                                     (7.2)

Then `A_m` has nonzero spectrum `+1,+1,+1,-1,-1,-1`, so it lies in the exact QFORM target for every `m`.

Choose anchor rows `1,2` and columns `1,2`. Then

`C=diag(1,0)`, `det C=0`, `N=0`,                               (7.3)

while (6.3) gives

`P_{12;12}=1`.                                                  (7.4)

Indeed all `m^2` contributing `3x3` minors have magnitude exactly `1/m`. Thus the aggregate packet stays fixed while every individual contributing local minor tends to zero, the anchor determinant is zero, and the double-deleted residual block is zero. This simultaneously rules out three tempting replacements for the packet: one good minor, an invertible anchor pair, or a forced nonzero double-deleted core.

This family is **not** a QFORM counterexample. Its quadratic form is the sum of three bilinear terms supported on three mutually disjoint ORIGINAL-coordinate blocks. Applying the required e5f Proposition H together with the sharp product-projection normalization for the two normalized star projections gives the actual target inequality

`boxed:
 ||p_{X^T A_m X}||_infinity
 <= 3*2^(1/3)
 =3.77976314968... <3.78,
}`                                                               (7.5)

uniformly in `m` and in all admissible cap-one product source laws.

The stress family lands in the exact-rank-one core endpoint of the E/R1 branch. Thus the endpoint itself is paid; what remains difficult is **stability in the full ambient form with arbitrary extra couplings and a nonzero rank-one-tube tail**. The fresh matrix-perturbation correction precludes solving that stability problem by simply deleting a small operator-norm or Frobenius tail for arbitrary unbounded sources.

## 8. What changed and next implication

The newest account03/B08 variable-mixture theorem was used at a genuine equation, not merely cited. Moving the residual occupancy threshold from `9/16` to `83/125` raises the forced fixed double-nested share from `19/500` to `1558/15625`, while the corresponding anchored branch still has a finite `<872/zeta` full-form bound.

The strengthened packet was then consumed by the completed physical-link/core compilers. One residual-core subbranch is now fully paid by `<987/zeta`; the others carry explicit original-coordinate product resources and no reciprocal individual minor.

The first unpaid B08 implication is now

`QFORM-DIFFUSE-POST-83/125-RECEIVER-v1`:

> in the FULL ambient form, consume either (S) the three-disjoint-linear-bank currency, (R1) the edge-star plus genuine nonzero rank-one-tube core, (E2) the aggregate second-compound/four-bank reserve, or (BICORE) the two-sided physical core stars, while retaining arbitrary unused anchor couplings and same-bank curvature. In the actual `k=1,2` spectral branches, the independent genuine rank-one/rank-two cross tubes remain parallel debts.

The exact tripod family (7.2) shows that an exact singular-anchor rank-one chain is benign, but it also shows why any successful next theorem has to be a **full-ambient receiver**, not a local-minor extraction. Full QFORM and global continuity remain OPEN. The new router/identity are source-pinned and finite-checked; independent proof review is pending.