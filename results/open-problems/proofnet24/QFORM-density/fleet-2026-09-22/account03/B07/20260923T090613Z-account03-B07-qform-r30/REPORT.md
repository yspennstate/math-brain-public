SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B07, 2026-09-23T09:06:13Z.
attacking: the r29 double-anchored third-volume survivor — compress an anchored 3x3-minor bank into either edge-times-E2 currency or a nested two-star/core packet, without selecting a single minor.

# account03/B07 QFORM r30 — double-anchored third volume compresses to lower-order physical banks

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: coordinate minor selection / GEOMETRY  
Run: `20260923T090613Z-account03-B07-qform-r30`  
Start control: `yspennstate/math-research-brain@06365a6016e640cdd2b9ceb4b41fd379197a2b13`  
Pre-publication control refresh: `yspennstate/math-research-brain@a38200956554f4eb2481aec8bb1dec82ae52c07e`  
OWNER CONTROL revision: `2026-09-22.15`  
Execution: `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`  
Status: **NEW SUPPORTING AGGREGATE-MINOR COMPRESSION / ONE NESTED SUBBRANCH CONTINUOUSLY PAID / FULL QFORM OPEN**.

## 1. Scope and live correction boundary

The target remains the unrestricted statement: for every dimension, independent real ORIGINAL coordinates with probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove a universal essential-supremum bound for the density of `Q=X^TAX`, or give a valid counterexample. Continuity is tracked separately.

No Gaussianity, moment, compact-support, log-concavity, connected-support, iid, diagonal-basis, or post-rotation independence assumption is used. This report does not use law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea, positive moments of worst conditional projection-density caps, naive fiber-supremum integration, deletion of a small nonzero quadratic term, or existence of one uniformly good physical minor.

Fresh controls and the live correction inbox were reread immediately before publication. The designated `account04/B07` QFORM archive and handoff directories were checked again and remained absent, so no partner result is fabricated. Section 7 applies instead the compatible completed `account04/B18` rearrangement theorem at a genuinely new four-disjoint-bank inequality.

## 2. Incoming r29 H3 packet

Use this slot's completed r29 report

`yspennstate/math-open-problems@0e842117ca7ec8472538faa120677507f16b5c17`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260923T084007Z-account03-B07-qform-r29/REPORT.md`.

Its theorem `QFORM-FOURHUB-M4-ANCHOR-TRANSDUCER-v1` reduces the previously raw hub-times-far-core motif to four alternatives. The only one attacked here is the double-anchored third-volume survivor: for one actual physical row `i` and one actual physical column `a` of an ORIGINAL-coordinate cross block `N`,

`G := G3^(i,a)(N)
   = sum_(|R|=|T|=3, i in R, a in T) det N[R,T]^2
   > gamma F^6`.                                                (2.1)

At r29's standard collar `theta=1/16`, `delta=1/4`, `tau=1/16`,

`gamma = 1/12824703626379264
       = 1/113246208^2`.                                        (2.2)

The inherited `F` is the parent cross-block Frobenius scale; all subblocks below have Frobenius norm at most `F`.

After physical row/column permutations only, write

`N = [[b, r^T],
      [c,  D ]]`,                                                (2.3)

where `b=N_ia`, `r` is the rest of the anchor row, `c` the rest of the anchor column, and `D` the far physical core. All displayed groups remain ORIGINAL-coordinate groups.

## 3. Exact anchored determinant decomposition

For a far row pair `R={u,v}` and far column pair `T={s,t}`, Laplace expansion along the anchor gives

`det N[{i,u,v},{a,s,t}]
 = b det D[R,T] - Psi_(R,T)`,                                   (3.1)

where

`Psi_(R,T)
 = r_s(c_u D_(v,t)-c_v D_(u,t))
   -r_t(c_u D_(v,s)-c_v D_(u,s)).`                              (3.2)

Put

`V2 := sum_(R,T) Psi_(R,T)^2`.                                  (3.3)

For each row pair `R={u,v}`, define the far-column vector

`w_R := c_u D_(v,*) - c_v D_(u,*)`.                             (3.4)

Then `Psi_(R,{s,t})` is exactly the `(s,t)` coordinate of the exterior product `r wedge w_R`. Therefore

`sum_T Psi_(R,T)^2
 = ||r wedge w_R||_2^2
 = ||r||_2^2||w_R||_2^2 - <r,w_R>^2`.                          (3.5)

A second exterior-product identity, now in the row index, gives

`sum_R ||w_R||_2^2
 = ||c||_2^2||D||_F^2 - ||D^T c||_2^2`.                         (3.6)

Similarly

`sum_R <r,w_R>^2
 = ||c||_2^2||Dr||_2^2 - (c^TDr)^2`.                            (3.7)

Combining (3.5)--(3.7) yields the exact identity

`boxed:
 V2 = ||r||^2||c||^2||D||_F^2
      -||r||^2||D^T c||^2
      -||c||^2||D r||^2
      +(c^T D r)^2.`                                            (3.8)

When `r,c` are nonzero this is equivalently

`V2 = ||r||^2||c||^2
      ||P_(c^perp) D P_(r^perp)||_F^2`;                         (3.9)

(3.8) is the definition-safe form when either vector vanishes. In particular,

`V2 <= ||r||^2||c||^2||D||_F^2`.                               (3.10)

This identity is the main new cancellation ledger: all non-`b det D` cancellation in the double-anchored third compound is itself an exact transverse star-star-core quantity.

## 4. Main theorem: anchored H3 becomes edge-E2 or four disjoint banks

### Theorem 4.1 — `QFORM-ANCHORED-H3-TO-EDGE-E2-OR-FOURBANK-v1`

For every real matrix `N` written as in (2.3), with `G=G3^(i,a)(N)>0`, at least one of the following holds.

**(E2-edge)**

`|b| sqrt(E2(D)) >= sqrt(G)/2`,                                (4.1)

where

`E2(D)=sum_(|R|=|T|=2) det D[R,T]^2`.

Moreover there is a physical two-coloring of the far row and column coordinates and a matching `sigma in S_2` such that, with four disjoint ORIGINAL-coordinate banks,

`boxed:
 |b| ||D[L1,R_sigma(1)]||_F
     ||D[L2,R_sigma(2)]||_F
 >= sqrt(G)/8.`                                                 (4.2)

**(star-star-core)** There are four disjoint ORIGINAL-coordinate banks `L0,L1,R0,R1` such that

`boxed:
 ||c_(L0)||_2 ||r_(R0)||_2 ||D[L1,R1]||_F
 >= sqrt(G)/16.`                                                (4.3)

#### Proof

Regard the arrays

`U_(R,T)=b det D[R,T]`, `W_(R,T)=Psi_(R,T)`

as Euclidean vectors. By (3.1),

`sqrt(G)=||U-W||_2 <= ||U||_2+||W||_2
        = |b|sqrt(E2(D))+sqrt(V2)`.                             (4.4)

If the first term is at least `sqrt(G)/2`, (4.1) holds. The physical two-color argument already proved in this slot's r26 report gives two row colors and two column colors for which one matching product of squared Frobenius block norms is at least `E2(D)/16`. Taking square roots and using (4.1) proves (4.2).

It remains that `sqrt(V2)>=sqrt(G)/2`, hence

`V2>=G/4`.                                                       (4.5)

Expand (3.2) into its four monomials and define the positive ordered-monomial ledger

`Smon := sum_(u!=v, s!=t) c_u^2 r_s^2 D_(v,t)^2`.              (4.6)

For each unordered row pair and unordered column pair, `(x1+x2+x3+x4)^2<=4 sum x_j^2`; summing gives

`V2 <=4 Smon`, so `Smon>=G/16`.                                (4.7)

Now color each far row independently into `L0/L1` and each far column independently into `R0/R1`. Set

`Tcolor := ||c_(L0)||_2^2 ||r_(R0)||_2^2
           ||D[L1,R1]||_F^2`.                                  (4.8)

Every ordered quadruple `(u,v,s,t)` with `u!=v,s!=t` contributes to (4.8) exactly when `u in L0`, `v in L1`, `s in R0`, `t in R1`, an event of probability `1/16`. Therefore

`E[Tcolor]=Smon/16 >=G/256`.                                   (4.9)

Some coloring attains at least its expectation. Taking square roots proves (4.3). QED.

The proof never selects, divides by, or lower-bounds one individual determinant. It first aggregates the entire double-anchored third-compound mass and only then selects positive physical bank norms.

## 5. Quantitative standard-collar consequences

Using `sqrt(gamma)=1/113246208`, (2.1) gives `sqrt(G)>F^3/113246208`.

In the E2-edge branch,

`boxed:
 |b| ||D[L1,R_sigma(1)]||_F
     ||D[L2,R_sigma(2)]||_F
 > F^3/905969664.`                                              (5.1)

In the star-star-core branch, writing

`x=||c_(L0)||_2`, `y=||r_(R0)||_2`, `H=D[L1,R1]`, `h=||H||_F`,

one has

`boxed: x y h > kappa F^3`,                                    (5.2)

with

`kappa := 1/1811939328`.                                       (5.3)

Since `x,y,h<=F`, (5.2) separately implies

`x>kappa F`, `y>kappa F`, `h>kappa F`, `xy>kappa F^2`.         (5.4)

Thus the H3 survivor has been reduced to lower-order physical resources at a dimension-free quantitative scale.

## 6. Apply the completed core quadrichotomy and newest volume theorem

Apply this slot's completed theorem

`QFORM-NESTED-CORE-R1-E2-VOLUME-OR-BICORE-v1`,

source

`yspennstate/math-open-problems@86ff1278a9b52d8a2736c340b7f54893c6b8c267`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260923T060629Z-account03-B07-qform-r26/REPORT.md`,

to the actual ORIGINAL-coordinate cross block `H` in (5.2). It gives four exhaustive subcases.

### 6.1 R1: explicit rank-one tube

`dist_F(H,{rank<=1})<h/2`, while (5.2)--(5.4) retain the two disjoint star banks and the quantitative lower scale `h>kappa F`. No tail is deleted; this remains an unpaid but now sharply localized tube.

### 6.2 E2: nested four-bank matching

The r26 coloring theorem supplies four further disjoint physical subbanks inside the `L1 x R1` coordinates with matched block norms `B1,B2` satisfying

`B1 B2 >= (sqrt(3)/16)h^2`.                                    (6.1)

Together with (5.2) and `h>kappa F`,

`boxed:
 x y B1 B2
 > (sqrt(3)/16) kappa^2 F^4.`                                  (6.2)

All six displayed banks are inherited from disjoint ORIGINAL-coordinate groups: the two outer star banks lie in `L0,R0`, while the matched blocks lie in the disjoint colors inside `L1,R1`.

### 6.3 VOL: a genuinely paid full-ambient branch

The deterministic r26 hypotheses in this branch imply

`E3(H)>h^6/27`                                                  (6.3)

and every third-volume inclusion marginal on the better-oriented physical side is at most `2/3`.

Now apply directly the current required volume theorem

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,

`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

At `q=4/3` it gives a continuous full-ambient density

`||p_Q||_infinity
 <=(9sqrt(3)e/2) E3(H)^(-1/6)
 <(27e/2) h^(-1)
 <(27e/(2 kappa)) F^(-1).`                                     (6.4)

For the standard collar,

`boxed:
 ||p_Q||_infinity < 66492383619.232 F^(-1).`                   (6.5)

The constant is intentionally not optimized; the structural point is that arbitrary same-bank curvature, affine terms, outside couplings and additional spectrum survive, and this branch is paid before any reciprocal individual minor.

### 6.4 BICORE: two additional physical stars

There are an actual row of `H` and column of `H`, with coefficient-vector norms `u,v`, such that

`u>sqrt(2/27)h`, `v>sqrt(2/27)h`.                              (6.6)

These vectors live on the `R1` and `L1` original-coordinate banks respectively, disjoint from the outer stars on `L0,R0`. Therefore

`boxed:
 x y u v
 > (2/27) x y h^2
 > (2/27) kappa^2 F^4.`                                        (6.7)

This is a four-independent-bank physical certificate, not a generic projected-density statement.

## 7. Compatible account04 result applied to a new inequality

The designated `account04/B07` current-QFORM directory and handoff remain absent at the fresh check. The compatible completed account04 theorem used here is

`account04/B18`, `QFORM` r2,

`yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T182500Z-account04-B18-QFORM-r2/REPORT.md`.

Its Juškevičius--Lee rearrangement transfer, together with the sharp one-dimensional cube-slicing bound, gives for any original-coordinate coefficient bank `z`

`||p_(z^T X)||_infinity <= sqrt(2)/||z||_2`.                   (7.1)

Because the four BICORE banks in (6.7) are mutually disjoint ORIGINAL-coordinate groups, their linear forms are genuinely independent. Applying (7.1) to each one gives the actual four-dimensional product-density inequality

`||p_(star_L0,star_R0,row_H,col_H)||_infinity
 <=4/(x y u v)
 <54 kappa^(-2) F^(-4).`                                      (7.2)

At the standard collar,

`boxed:
 ||p_(four linear banks)||_infinity
 <177288702931066945536 F^(-4).`                               (7.3)

Already before the BICORE split, the two outer star projections obey

`||p_(star_L0,star_R0)||_infinity
 <=2/(xy)
 <3623878656 F^(-2).`                                         (7.4)

Equations (7.2)--(7.4) are retained only as genuine product-provenance currency. The live correction ledger forbids treating a bounded projected joint density by itself as control of an arbitrary curved indefinite quadratic pushforward.

## 8. Regression checks

`CHECKS.py` and captured `CHECKS.txt` are beside this report. They check the exact exterior-product identity (3.8), the positive-monomial bound `V2<=4Smon`, the triangle decomposition, the exhaustive two-color lower bound `max Tcolor>=Smon/16`, and the E2 matching lower bound `max P>=E2/16` on 900 deterministic-seed integer matrices of rectangular sizes from `2x2` through `4x3`.

Captured output:

`cases 900`
`min_trans_ratio 3.3145780051150897`
`min_e2_ratio 3.84`
`gamma_sqrt_den 113246208`
`edge_three_link_den 905969664`
`trans_three_link_den 1811939328`
`STATUS=PASS`

These computations are algebraic regression only; the proof is Sections 3--7.

## 9. Remaining implication and status

This run removes the raw r29 double-anchored `H3` bank as a terminal structural obstruction. It is now replaced by:

1. an edge-times-two-E2-bank packet (5.1); or
2. a four-disjoint-bank star-star-core packet (5.2), which itself is split into a rank-one tube, a nested E2 matching, a continuously paid diffuse-volume branch, or a four-physical-star BICORE packet.

The first unpaid B07 implication is now

`QFORM-ANCHOR-H3-LOWERORDER-CURVATURE-RECEIVER-v1`:

consume the edge-times-E2 packet, the retained rank-one core tube, the six-bank nested E2 packet, or the four-star BICORE product packet through a nonlinear receiver that preserves arbitrary within-bank curvature and the true ambient Schur remainder. The r29 rank-two-tube sibling and r28 `M1,M2,M3,M5` siblings remain separate obligations.

**Full QFORM remains OPEN / not proved / not disproved.** The present VOL subbranch proves a continuous density; the full-target continuity conclusion remains OPEN. No external novelty claim is made, and no independent end-to-end review of this r30 theorem has yet been completed.
