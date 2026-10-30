SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B02, 2026-09-23T05:03:29Z.
attacking: repair the compound-hub edge-times-E2 branch by comparing the cross-only anchored Schur packet with the TRUE full physical-pair Schur packet, then apply fractional-volume smoothing only at its stated marginal gates.

# fleet03/B02 QFORM r21 — true-pair Schur rank-one repair and fractional-volume receiver

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Integrated Fourier estimate  
**Owner control at start:** revision `2026-09-22.15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full target:** `OPEN / NOT PROVED / NOT DISPROVED`  
**Full target-wide unweighted Fourier L1 criterion:** `OPEN / NOT PROVED / NOT DISPROVED`  
**Continuity:** proved only on the fractional three-volume exit and on the designated-partner residual theorem itself; the new pair receivers below assert essential boundedness only.

## 1. Exact target and the first unpaid implication attacked

The target remains unrestricted: for every finite `n`, independent real ORIGINAL coordinates `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^T A X` has a density with one universal finite `L^infinity` bound, or give a valid target counterexample. No Gaussian, moment, compact-support, connected-support, iid, log-concavity, sign, spectral-coordinate-independence, or hidden regularity assumption is introduced.

The immediate B02 predecessor is

`yspennstate/math-open-problems@648ea277fc2cfcc8ce11a7093c61951a9e15baa8`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260923T043653Z-fleet03-B02-qform-r20/ADDENDUM_COMPOUND_HUB_COMPILER.md`.

It converted a concentrated third-compound hub into either an edge times aggregate second-volume resource or a two-star transverse packet, but it explicitly left the analytic payment of the edge/`E2` resource open.

The key live correction is fleet03/B06's target-valid witness showing that the tempting identification

`cross-only anchored Schur E2 = true full physical-pair Schur E2`

is false when same-side anchor couplings are present. Canonical source:

`yspennstate/math-open-problems@15b6186ccb23f17a42749b71bfa05f3b80622f05`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260923T022131Z-fleet03-B06-qform-auto11/REPORT.md`.

This run resolves the algebraic gap exactly: the difference between those two Schur cross blocks is always rank one, and loss of the cross-only `E2` therefore forces an explicit correction packet rather than allowing the resource to disappear.

## 2. Fresh fractional-volume input actually applied

The newest required volume-stability theorem is

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,

`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

For an ORIGINAL-coordinate cross block `B`, put

`Z=E3(B)=e_3(B^T B)>0`,

and let `alpha_i` be the row inclusion marginals of the normalized squared `3x3`-minor law. If

`1<=q<3/2`, `alpha_i<=q/2` for every row,                           (2.1)

then the full ambient quadratic-plus-affine form has a continuous density and

`||p_Q||_infinity <= C3(q) Z^(-1/6)`,
`C3(q)=3e/((3-2q)sqrt(q)).`                                        (2.2)

The theorem applies after transposing `B`, so the same conclusion holds when the column marginals satisfy the gate. All same-bank quadratic terms and outside couplings remain present.

At the concrete value

`q=4/3`,                                                         (2.3)

(2.2) gives

`C3(4/3)=(9sqrt(3)e)/2=21.186910062820...`.                      (2.4)

The gate `alpha_i<=2/3` is retained exactly below; it is never silently dropped.

## 3. Exact rank-one repair of the cross-only / true-pair Schur mismatch

### Theorem 3.1 — `QFORM-CROSS-SCHUR-TO-TRUE-PAIR-RANKONE-v1`

Let `x,y` be two distinct ORIGINAL coordinates. Put

`d=A_xx`, `e=A_yy`, `a=A_xy`,
`P=[[d,a],[a,e]]`, `delta=det P=de-a^2`.                         (3.1)

Assume `a!=0` and `delta!=0`. Let `U,V` be disjoint residual physical banks, disjoint from `{x,y}`, and define

`u=A[U,x]`, `c=A[U,y]`,
`r=A[x,V]`, `v=A[y,V]`,
`N=A[U,V]`.                                                       (3.2)

The cross-only anchored Schur block associated with the physical cross edge `a` is

`S=N-c r^T/a`.                                                    (3.3)

The TRUE cross block in the Schur complement obtained by completing the full principal pair `P`, including every same-side anchor coupling, is

`T=N-[u,c] P^(-1) [r;v]`.                                        (3.4)

Define

`xi=a u-d c`, `eta=a v-e r`.                                     (3.5)

Then the exact identity

`boxed: T=S+xi eta^T/(a delta)`                                  (3.6)

holds.

#### Proof

Since

`P^(-1)=delta^(-1)[[e,-a],[-a,d]]`,

(3.4) expands to

`T=N-(e/delta)u r^T+(a/delta)u v^T
      +(a/delta)c r^T-(d/delta)c v^T`.                           (3.7)

Subtract (3.3). Because

`a/delta+1/a=de/(a delta)`,                                      (3.8)

the difference is

`T-S=(1/delta)[a u v^T-e u r^T-d c v^T+(de/a)c r^T]
    =(a u-d c)(a v-e r)^T/(a delta)`,                            (3.9)

which is (3.6). QED.

The B06 counterexample therefore identifies a real obstruction, but the obstruction is a single rank-one correction, not an uncontrolled destruction of the second-compound bank.

## 4. Exterior-square identity and the correction-safe E2 dichotomy

For a linear map `S` and vectors `p,q`, let `C2(S)=wedge^2 S`. For decomposable `z1 wedge z2`, direct expansion gives

`C2(S+p q^T)=C2(S)+L_p S iota_q`,                                (4.1)

where `L_p` is exterior multiplication by `p` and `iota_q` is contraction by `q`.

Choose orthonormal coordinates with `p=||p||e_1` and `q=||q||f_1`. The only domain wedge basis vectors surviving the second term in (4.1) are `f_1 wedge f_j`, `j>=2`. Therefore

`||L_p S iota_q||_HS
 =||p|| ||q|| ||P_(p^perp) S P_(q^perp)||_F`.                   (4.2)

Also the transverse block in (4.2) is unchanged under the rank-one update:

`P_(p^perp)(S+p q^T)P_(q^perp)=P_(p^perp)SP_(q^perp)`.          (4.3)

Apply (4.1)-(4.3) to (3.6). With the convention that the correction term is zero when `xi=0` or `eta=0`, set

`F=||P_(xi^perp) S P_(eta^perp)||_F
 =||P_(xi^perp) T P_(eta^perp)||_F`.                            (4.4)

Since `E2(M)=||C2(M)||_HS^2`, the triangle inequality gives

`sqrt(E2(S))
 <=sqrt(E2(T))+ ||xi|| ||eta|| F/(|a delta|).`                  (4.5)

Hence

`boxed:
 max{ a^2 E2(T),
      (||xi||^2 ||eta||^2/delta^2) F^2 }
 >= a^2 E2(S)/4.
`                                                                    (4.6)

This is `QFORM-CROSS-E2-TO-TRUE-SCHUR-OR-CORRECTION-v1`.

The first alternative is now the exact TRUE pair-Schur `E2` currency required by the live correction. The second alternative is an explicit same-side correction packet. Nothing is discarded and no individual `2x2` minor is selected.

## 5. Apply the newest E3 gate and compile its failure into the repaired packet

Let `B=A[I,J]` be any actual physical cross block with `Z=E3(B)>0`. Give each row/column triple pair probability proportional to its squared determinant, and denote the row and column inclusion marginals by `alpha_i,beta_j`.

Fix `1<q<3/2`.

If every row marginal is at most `q/2`, (2.2) pays the full ambient law. If every column marginal is at most `q/2`, apply (2.2) to `B^T`.

Otherwise choose physical anchors `x in I`, `y in J` with

`alpha_x>q/2`, `beta_y>q/2`.                                      (5.1)

Under the same squared-minor probability law,

`P(x in row triple and y in column triple)
 >=alpha_x+beta_y-1>q-1`.                                        (5.2)

Thus the joint incident third-volume mass `J_xy` satisfies

`J_xy>(q-1)Z`.                                                    (5.3)

This gate-failure-to-joint-anchor step is already present in fleet03/B08; it is included here only so the new repaired implication is end-to-end.

Write the cross block around the anchors as

`B=[[a,r^T],[c,N]]`.                                              (5.4)

If `a=0`, the exact joint-star exterior identity reduces to

`sqrt(J_xy)
 =||c|| ||r|| ||P_(c^perp)N P_(r^perp)||_F`,                     (5.5)

so the gate failure directly forces a two-star transverse resource greater than `sqrt((q-1)Z)`.

Now suppose `a!=0`. The exact incident-minor Schur identity from the preceding B02 run gives

`J_xy=a^2 E2(S)`, `S=N-c r^T/a`.                                (5.6)

If the principal pair determinant `delta=de-a^2` is zero, the anchor is a genuine singular-pair residue and is recorded separately; no inverse pair is invented.

If `delta!=0`, combine (5.3), (5.6), and (4.6):

`boxed:
 max{ a^2 E2(T),
      (||a u-d c||^2 ||a v-e r||^2/delta^2) F^2 }
 > (q-1) Z/4.
`                                                                    (5.7)

This is the main new compiler of the run.

At `q=4/3`, one has the concrete exhaustive alternative:

* either the fractional-three-volume gate pays a continuous density with
  `||p_Q||infinity <=21.186911 Z^(-1/6)`;
* or `a=0` and the two-star packet in (5.5) is `>sqrt(Z/3)`;
* or `a!=0, delta=0` and the anchor is a singular physical pair;
* or `a!=0, delta!=0` and

`max{a^2 E2(T), correction-resource}>Z/12`.                      (5.8)

The old cross-only `E2` branch has therefore been replaced by a correction-safe TRUE-Schur-or-same-side-payment branch.

## 6. New analytic payment on the TRUE-Schur branch with the wider 2-volume marginal gate

The completed fractional rank-two volume theorem is fleet03/B01,

`yspennstate/math-open-problems@e83f41d90267abdb753682dbe60bceecd8e6558a`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B01/fleet03-B01-20260922T223030Z-auto12/REPORT.md`.

For a quadratic remainder `R` with physical cross block `T`, write `Delta=E2(T)>0` and let its normalized squared `2x2`-minor row marginals be `gamma_i`. At interpolation parameter `theta=3/4`, the exact gate is

`gamma_i<=2/3` for every row,                                      (6.1)

or the analogous column gate after transposition. Under this gate,

`||p_R||_3 <= C_E2 Delta^(-1/6)`,                                (6.2)

where

`C_E2
 =[e*(9)*K_(3/4)^(-1/3)]^(2/3)
 =7.437387807756...`,
`K_(3/4)=(3/4)^(-3/4)(1/4)^(-1/4).`                              (6.3)

Now assume the anchor principal pair `P` is indefinite, so `delta<0`, and set

`D=|delta|`, `kappa=sigma_min(P)`.                                (6.4)

The completed B06 pair-log `L^3` receiver, applied to the TRUE full-pair Schur remainder, says

`||p_Q||infinity
 <=7(pi/12)^(1/7)
   ||p_R||_3^(3/7) D^(-3/14) kappa^(-2/7).`                      (6.5)

Insert (6.2):

`boxed:
 ||p_Q||infinity
 <=13.658928
   D^(-3/14) kappa^(-2/7) Delta^(-1/14).
`                                                                    (6.6)

This is `QFORM-PAIR-TRUE-SCHUR-E2-MARGINAL23-v1`.

It strictly enlarges the available analytic gate compared with the earlier range-leverage-`1/2` receiver: here the actual determinant-weighted `E2` marginal may be as large as `2/3`. The gate is retained, not suppressed.

On the concrete `q=4/3` third-volume failure branch, if the first term of (5.8) fires, then

`Delta>Z/(12a^2)`.                                                 (6.7)

Combining (6.6)-(6.7) yields the actual target-level inequality

`boxed:
 ||p_Q||infinity
 <16.311766
   |a|^(1/7) D^(-3/14) kappa^(-2/7) Z^(-1/14),
`                                                                    (6.8)

provided the TRUE pair-Schur `E2` bank satisfies the stated `2/3` row or column marginal gate.

No continuity claim is made for (6.6)-(6.8); the pair-log receiver proves essential boundedness.

## 7. Designated partner fleet04/B02 applied to a new inequality

The designated partner completed

`QFORM-ZERO-DIAGONAL-TRIPLE-CONTINUITY-v1`,

canonical source

`yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B02/20260922T193108Z-fleet04-B02-QFORM-r2/REPORT.md`.

It proves that if a quadratic form in independent cap-one ORIGINAL coordinates has a nonsingular physical principal `3x3` block `H` with a zero diagonal entry, then its density is continuous and

`||p||infinity <= M_H:=3*2^(2/3)|det H|^(-1/3)`.                  (7.1)

Apply this theorem not to the full form directly, but to the TRUE Schur remainder `R` after completing an invertible indefinite pair `P`. The remaining variables are still literal original independent coordinates, so the partner theorem is applicable whenever the Schur matrix of `R` contains such an `H`.

The pair-log envelope gives for every cutoff `rho>0`

`p_Q(t)
 <=2sqrt(2)/rho
   +D^(-1/2) E log_+(2rho^2/(kappa|t-R|)).`                      (7.2)

If `p_R<=M_H`, then for `A0>0`

`E log_+(A0/|t-R|)
 <=M_H int_R log_+(A0/|x|) dx
 =2A0 M_H`.                                                       (7.3)

With `A0=2rho^2/kappa`, equations (7.2)-(7.3) give the ACTUAL inequality

`p_Q(t)
 <=2sqrt(2)/rho
   +4 M_H D^(-1/2) kappa^(-1) rho^2`.                            (7.4)

Optimizing the right side over `rho>0` yields exactly

`||p_Q||infinity
 <=6 M_H^(1/3) D^(-1/6) kappa^(-1/3)`.                           (7.5)

Substitute (7.1):

`boxed:
 ||p_Q||infinity
 <=6*3^(1/3)*2^(2/9)
   D^(-1/6) kappa^(-1/3)|det H|^(-1/9)
 <10.094557
   D^(-1/6) kappa^(-1/3)|det H|^(-1/9).
`                                                                    (7.6)

This is `QFORM-PAIR-PLUS-ZERODIAG-TRIPLE-NESTED-v1`. It is a genuine new use of the designated partner result inside the pair-log receiver, rather than a restatement of the partner theorem. The residual density in (7.1) is continuous; (7.6) itself is recorded only as an essential-density bound.

## 8. The B06 counterexample is exactly repaired by the new correction term

Use the target-valid B06 witness ordered as `(x,y,u1,u2,v1,v2)`:

`A=
 [[0,1,0,1,0,0],
  [1,0,0,0,0,1],
  [0,0,0,0,1,0],
  [1,0,0,0,0,1],
  [0,0,1,0,0,0],
  [0,1,0,1,0,0]].`                                               (8.1)

For the left bank `(x,u1,u2)` and right bank `(y,v1,v2)`, the cross block is `I_3`. With anchors `x,y`,

`d=e=0`, `a=1`, `delta=-1`,
`S=I_2`,
`T=diag(1,0)`.                                                     (8.2)

Thus

`E2(S)=1`, `E2(T)=0`.                                               (8.3)

But

`xi=eta=(0,1)`, `F=1`,                                            (8.4)

so the same-side correction resource in (4.6) is exactly one. In fact (4.5) is equality in this witness:

`1=0+1`.                                                            (8.5)

Therefore the new theorem does not contradict the live B06 correction; it identifies exactly where the lost second-compound mass went.

## 9. Deterministic checks

`CHECKS.py` and `CHECK_RESULTS.txt` are stored beside this report. One hundred seeded random instances checked the exact rank-one identity (3.6) and the compound triangle inequality (4.5). The maximum scaled identity error was

`7.947e-16`,

and the maximum positive compound-inequality violation was zero at floating-point precision. The B06 witness check returned

`E2(S)=1`, `E2(T)=0`, `correction-resource=1`.

The same checker evaluates

`C3(4/3)=21.186910062820`,
`C_E2=7.437387807757`,
`C_pair-E2=13.658927456391`,
`C_gate-after-J>Z/3=16.311765644144`,
`C_partner-nested=10.094556036479`.

These computations are regression checks only; the matrix and exterior identities are proved symbolically above.

## 10. Fourier status and exact next obligations

This run still does **not** produce a valid exact-target counterexample to a universal unweighted

`integral_R |E exp(it X^T A X)| dt`

bound, and it does not prove that stronger criterion at full scope. The fractional-three-volume exit has an integrable characteristic function and therefore a continuous density. The repaired pair branches (6.6) and (7.6) use finite-`p`/physical pair smoothing and do not establish target-wide Fourier `L1`.

The first unpaid implications are now narrower:

1. **Same-side correction packet:** spend
   `(||a u-d c||^2 ||a v-e r||^2/delta^2)F^2`
   by a product-preserving mixed-Fresnel/fractional-volume estimate, without treating `xi,eta` as independent rotated coordinates.
2. **Concentrated TRUE-Schur E2:** if the first term in (5.7) fires but the true `E2` row and column minor marginals both exceed the `2/3` gate, compile that concentration into a new physical anchor before any reciprocal minor is paid.
3. **Singular principal pair:** treat `a!=0, delta=0` by a grouped-square/ridge mechanism rather than an illegal inverse pair.

The important advance is that the cross-only/true-Schur discrepancy is no longer an unstructured failure mode: it is exactly rank one and obeys the quantitative conservation law (4.6).

Full QFORM remains OPEN. Full continuity remains OPEN.
