SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B08, 2026-09-23T06:48:30Z.
attacking: the post-2/3 nested packet by a sequential second-side mixed-minor payment, then an exact double-nested degree-drop router on the actual physical cross block.

# account03/B08 r30 — sequential second-side self-match and double-nested degree drop

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** revision `2026-09-22.15`  
**Assignment:** diffuse eigenvector case / quantitative inequalities  
**Run:** `20260923T064830Z-account03-B08-qform-diffuse-r30`  
**Classification:** `NEW SUPPORTING STRUCTURAL COMPILER + NEW CONTINUOUS SUBBRANCH / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (`full_brain_connected=false`).

## 1. Scope, corrections, and source pins

The full target remains OPEN: for arbitrary dimension, independent real ORIGINAL coordinates with one-dimensional probability densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal essential-density bound for `Q=X^TAX`, or give a valid counterexample. Continuity is tracked separately.

No moment, Gaussian, iid, compact-support, connected-support, log-concavity, post-rotation independence, pointwise law-uniform Fresnel decay, arbitrary-joint coarea, positive conditional projection-height moment, naive fiber supremum, or single-good-minor principle is used.

Fresh owner control was read from `yspennstate/math-research-brain` main; OWNER CONTROL remains revision `2026-09-22.15`, QFORM only. The current-hour canonical login was already occupied by the preceding B08 invocation and was preserved rather than overwritten, exactly as the protocol requires.

The immediate predecessor is

`yspennstate/math-open-problems`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260923T062121Z-account03-B08-qform-diffuse-r29/REPORT.md`.

The analytic compiler reused below is B08 r28 `QFORM-MIXED-ORDER-JENSEN-COMPILER-v1` at

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260923T052144Z-account03-B08-qform-diffuse-r28/REPORT.md`.

The physical-core compiler used below is account03/B07 r26 `QFORM-NESTED-CORE-R1-E2-VOLUME-OR-BICORE-v1`, reported at scientific commit

`67a8e05e237bc914ad0563e361f6eb035b76e7fe`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260923T060629Z-account03-B07-qform-r26/REPORT.md`.

The live hidden-shear correction from account01/B05 r27 is also respected: a bounded residual joint density is not substituted for the original product-linear provenance. In particular, the degree-drop matrix below is used only as a deterministic exterior identity for the ACTUAL physical cross block; it is not called a true quadratic Schur complement and no same-side curvature is deleted.

A fresh search still found no completed current-QFORM artifact for the designated `account04/B08` partner slot. No result is fabricated for it. Section 7 applies a compatible completed account04/B18 product-projection theorem at an actual inequality.

## 2. Incoming one-sided nested packet

Use the r29 survivor after its `<374/L` continuous branch and large-row-star alternative have both failed. Thus there is an ACTUAL original-coordinate cross block `B=A[I,J]`, distinct fixed physical rows `i,k in I`, and a fixed physical column `a in J` such that

`R_i=||B[i,:]||_2<=L`, `R_k=||B[k,:]||_2<=L`,                  (2.1)

and the complete one-sided nested third-volume packet

`P=sum_(r in I\{i,k}) sum_(b<c in J\{a})
   det B[{i,k,r},{a,b,c}]^2`

satisfies

`boxed: P>L^6/10800.`                                           (2.2)

No individual `3x3` minor is selected from this packet.

## 3. Sequential second-side self-match

Write `c_a=B[:,a]` for the full physical anchor column and

`C_a=||c_a||_2`.                                                  (3.1)

Normalize the packet (2.2) to a probability law `w3^P` on the anchored order-three minors. For each residual physical column pair `C={b,c} subset J\{a}`, put

`W_C=sum_(r in I\{i,k}) det B[{i,k,r},{a} union C]^2`,
`eta_C=W_C/P`.                                                     (3.2)

Let `beta_j` be the residual column inclusion marginals under `eta`; then

`sum_(j!=a) beta_j=2`.                                            (3.3)

For the same pair `C={b,c}`, define the complete physical order-two column-pair volume

`D_C=sum_(|U|=2) det B[U,C]^2
    =||c_b wedge c_c||_2^2`.                                     (3.4)

Cauchy--Binet and exterior monotonicity give

`W_C
 <=sum_(|S|=3) det B[S,{a,b,c}]^2
 =||c_a wedge c_b wedge c_c||_2^2
 <=C_a^2 D_C`.                                                    (3.5)

Hence, whenever `eta_C>0`,

`D_C>=eta_C P/C_a^2`.                                             (3.6)

Construct an order-two physical-minor law `nu2*` by first drawing `C` with law `eta`, then drawing a physical row pair `U` conditionally with probability

`det B[U,C]^2/D_C`.                                               (3.7)

Its ORIGINAL-column marginals are exactly the same `beta_j` as the order-three law. The entropy-determinant calculation is identical to the row-side self-match but now on the second physical side:

`log K(nu2*)
 =H(eta)+sum_C eta_C log D_C
 >=H(eta)+sum_C eta_C log(eta_C P/C_a^2)
 =log(P/C_a^2)`.                                                   (3.8)

Therefore

`boxed: K(nu2*)>=P/C_a^2.`                                       (3.9)

For `0<theta<1`, mix before any reciprocal-minor selection:

`Omega_theta=theta w3^P+(1-theta)nu2*`.                          (3.10)

Viewed as a physical-minor law for `B^T`, it has mean order `2+theta`, anchor-row marginal `theta`, residual row marginals `beta_j`, and

`boxed:
 K(Omega_theta)
 >=P C_a^(-2(1-theta))
   theta^(-theta)(1-theta)^(-(1-theta)).
`                                                                    (3.11)

Thus B08 r28, applied to `B^T`, proves:

### Theorem 3.1 — `QFORM-NESTED-SECOND-SIDE-SELF-MATCH-v1`

If `q>=1`,

`max(theta,max_j beta_j)<=q/2`,                                  (3.12)

and

`2+theta>2q`,                                                     (3.13)

then the FULL ambient quadratic form, with arbitrary same-bank curvature, outside couplings and induced affine terms retained, has a continuous `C_0` density satisfying

`boxed:
 ||p_Q||_infinity
 <=e q^(-1/2)(2+theta)/(2+theta-2q)
   P^(-1/(2(2+theta)))
   C_a^((1-theta)/(2+theta))
   [theta^theta(1-theta)^(1-theta)]^(1/(2(2+theta))).
`                                                                    (3.14)

Exactly as in r29, every fixed residual column occupancy below `2/3` is payable by this family; `2/3` is the strict integrability barrier for this two-order self-match. The new point is that the one-sided nested packet itself can be self-matched on the OTHER physical side before any local determinant is chosen.

## 4. Fixed universal second-side payment and stronger double nest

Choose

`theta=16/25`, `q=32/25`.                                       (4.1)

Then `2+theta=66/25`, the integrability gap is `2/25`, and the ratio in (3.14) is `33`.

If

`C_a<=L`, `max_j beta_j<=16/25`,                                (4.2)

then (2.2) and (3.14) give

`boxed: ||p_Q||_infinity<407/L`,                                (4.3)

more precisely the checker gives `406.784140524029.../L`. The density is continuous and vanishes at infinity.

If `C_a>L`, retain instead the large physical column-star resource. If `C_a<=L` but (4.2) fails, choose a residual physical column `b` with `beta_b>16/25`. The complete fixed two-row/two-column nested packet

`D=sum_(r in I\{i,k}) sum_(c in J\{a,b})
   det B[{i,k,r},{a,b,c}]^2`                                    (4.4)

obeys

`D=beta_b P>(16/25)(L^6/10800)`, hence

`boxed: D>L^6/16875.`                                           (4.5)

This is stronger than the earlier simultaneous-union-bound double nest and is obtained sequentially without selecting one physical `3x3` minor.

If the newly exposed second anchor column has norm `C_b=||B[:,b]||_2>L`, retain that large-star resource. The rest of the report assumes

`R_i,R_k,C_a,C_b<=L`.                                           (4.6)

## 5. Exact double-nested degree drop

Permute only physical coordinates and write the actual cross block around the four fixed anchors as

`B = [ C  R ]`
`    [ S  N ]`,                                                  (5.1)

where `C=B[{i,k},{a,b}]` is `2x2`, `R` has the two fixed rows and residual columns, `S` has residual rows and the two fixed columns, and `N` is the residual physical cross block.

For each residual row `r` and residual column `c`, block expansion gives the exact identity

`det [[C,R[:,c]],[S[r,:],N_rc]]
 =det(C) N_rc-S[r,:] adj(C) R[:,c]`.                            (5.2)

Therefore the entire double-nested third-volume packet is exactly

### Theorem 5.1 — `QFORM-DOUBLE-NESTED-DEGREE-DROP-v1`

`boxed:
 D=|| det(C)N-S adj(C)R ||_F^2.
`                                                                    (5.3)

Consequently

`sqrt(D)<=|det C| ||N||_F+||S adj(C)R||_F`.                     (5.4)

At least one of the following two branches holds:

**A — determinant-times-residual-core**

`|det C| ||N||_F>sqrt(D)/2`;                                    (5.5)

**B — aligned two-sided link**

`||S adj(C)R||_F>sqrt(D)/2`.                                    (5.6)

This is an exterior degree-drop identity only. It does NOT assert that `det(C)N-S adj(C)R` is the true Schur cross block of the ambient quadratic form; the hidden-shear correction forbids that shortcut in general. Every later probability-facing receiver below is applied to the actual residual physical block `N` or to actual original-coordinate linear banks.

## 6. Branch A: a much larger actual residual core, then B07 r26

Under (4.6),

`|det C|<=||C||_F^2/2<=L^2`.                                   (6.1)

Combining (4.5), (5.5), and (6.1) yields

`G:=||N||_F
 >L/(2sqrt(16875))
 =boxed(L/(150sqrt(3))).`                                       (6.2)

Apply account03/B07 r26 to this ACTUAL physical cross block `N`.

**VOL.** If its diffuse-volume case holds, the full ambient quadratic form has a continuous `C_0` density and

`||p_Q||_infinity<(27e/2)G^(-1)
 <2025 e sqrt(3)/L
 =9534.109528269.../L
 <boxed(9535/L).`                                                (6.3)

**R1.** Otherwise one allowed structural survivor is the genuine relative rank-one tube

`dist_F(N,{rank<=1})<G/2`, with the quantitative floor (6.2).    (6.4)

**E2.** In the aggregate second-compound case,

`E_2(N)>=3G^4/16
 >boxed(L^4/(48*150^4))`,                                       (6.5)

and the B07 physical coloring yields four disjoint subbanks with matching Frobenius-product reserve

`P_match>=3G^4/256
 >boxed(L^4/(768*150^4)).`                                      (6.6)

**BICORE.** In the two-sided heavy physical-core case there are an actual residual row and residual column with star norms each exceeding

`sqrt(2/27)G
 >boxed(L/(675sqrt(2))).`                                       (6.7)

Thus one half of the double-nested branch is converted either into a continuous full-ambient payment or into substantially stronger rigid resources than the previous one-sided nested router.

## 7. Branch B: an aligned three-link packet, with account04 mathematics applied

Take a singular-value decomposition

`adj(C)=sum_(j=1)^r sigma_j u_j v_j^T`, `r<=2`.                  (7.1)

Then

`S adj(C)R=sum_j sigma_j (S u_j)(R^T v_j)^T`,                  (7.2)

so (5.6) and the triangle inequality force some `j` with

`boxed:
 sigma ||S u||_2 ||R^T v||_2>sqrt(D)/4
 >L^3/(300sqrt(3)).
`                                                                    (7.3)

Under (4.6),

`sigma<=||C||_op<=sqrt(2)L`,
`||S u||_2<=sqrt(2)L`,
`||R^T v||_2<=sqrt(2)L`.                                       (7.4)

Hence each of the three factors is itself bounded below:

`boxed:
 sigma, ||S u||_2, ||R^T v||_2>L/(600sqrt(3)).
`                                                                    (7.5)

The two coefficient vectors `S u` and `R^T v` live on disjoint ORIGINAL residual-coordinate banks. Define

`Y=(S u)^T X_(I\{i,k})`,
`Z=(R^T v)^T X_(J\{a,b})`.                                     (7.6)

A fresh check found no designated `account04/B08` theorem. Apply instead the completed compatible account04/B18 sharp product-projection consequence from scientific commit

`ce50e74f705c49f66524aa6565d4aa4a9be88061`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T182500Z-account04-B18-QFORM-r2/REPORT.md`:

`||p_(u^T X)||_infinity<=sqrt(2)/||u||_2`                       (7.7)

for a coefficient vector on an original-coordinate cap-one product bank.

Because the two banks in (7.6) are disjoint, `Y,Z` are genuinely independent. From (7.3) and `sigma<=sqrt(2)L`,

`||S u||_2 ||R^T v||_2>L^2/(300sqrt(6))`.                       (7.8)

Therefore the partner theorem gives the actual quantitative inequality

`boxed:
 ||p_(Y,Z)||_infinity
 <=2/(||S u||_2||R^T v||_2)
 <600sqrt(6)/L^2
 =1469.69384567.../L^2.
`                                                                    (7.9)

Equation (7.9) is retained as product-linear provenance currency. In view of the hidden-shear and bounded-projection corrections, it is NOT promoted to a generic indefinite quadratic-pushforward bound. Branch B remains analytically unpaid; its new content is the aligned anchor-singular direction (7.5) coupled to two disjoint, quantitatively nontrivial original-coordinate projections.

## 8. What changed and first unpaid implication

The r29 one-sided packet `P>L^6/10800` no longer ends at an undifferentiated second-side heavy state. This run gives the following exhaustive continuation after large-star exits:

1. a new continuous branch `||p_Q||_infinity<407/L`;
2. a stronger fixed double nest `D>L^6/16875`;
3. from that nest, either a residual actual cross core with `||N||_F>L/(150sqrt(3))`, leading to the paid `<9535/L` VOL branch or the rigid R1/E2/BICORE alternatives (6.4)-(6.7);
4. or an aligned three-link packet (7.3)-(7.5) whose two residual product projections have joint density `<600sqrt(6)/L^2`.

The first unpaid B08 implication is now `QFORM-ALIGNED-DOUBLE-NEST-CURVED-RECEIVER-v1`: consume branch B while retaining the four anchor coordinates, arbitrary same-bank curvature and all unused couplings, using the simultaneous original-coordinate product-linear provenance rather than a generic bounded joint density. In parallel, the R1/E2/BICORE survivors in branch A remain available to the universal proof assembly.

The unrestricted conjecture remains **OPEN / not proved / not disproved**. Global continuity remains OPEN. Continuity is proved only on the new second-side `<407/L` branch and the B07 VOL `<9535/L` branch.

## 9. Finite checks

`CHECKS.py` and `CHECKS.txt` beside this report verify the exact `1/16875` double-nested coefficient, the `<407/L`, `<9535/L`, and partner `<1470/L^2` constants, and a seeded 1000-sample algebra regression for (5.2). The largest determinant-identity error was `5.329e-15`; the checker terminates `QFORM_B08_R30_CHECK_PASS`.

These finite checks are regression evidence only; the symbolic inequalities above are the substantive proof.
