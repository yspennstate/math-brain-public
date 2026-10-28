SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B13, 2026-09-24T00:28:58Z.
attacking: convert the aggregate Pluecker packet core into quantitative projective collapse, using account02/B13 r37 and the sharp leave-one-out DPP normalization.

# account01/B13 — absolute packet mass forces projective collapse at scale rho^{-1/10}

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: extremal product laws / analytic derivation and exact structural identities  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **new supporting target-level structural theorem proved; full unrestricted QFORM remains OPEN / NOT PROVED / NOT DISPROVED; unrestricted continuity remains separately OPEN.**

No moments, compact support, connected support, log-concavity, Gaussianity, post-rotation independence, centered intervals, bounded support diameter, fixed fragment count, or deletion of a coefficient-small quadratic tail is used. Latent two-dimensional rotations below are deterministic coefficient-basis changes only; the independent random coordinates are never rotated.

## 1. Fresh source-pinned premises


The completed designated partner result actually applied is account02/B13 r37:

`yspennstate/math-open-problems@4a8e12f1956a541cbd8a03961c29de79d1b12592`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260923T225517Z-account02-B13-qform-r37/REPORT.md`.

Its exact chamber is

`A=D+U Lambda U^T`, `U^T U=I_2`, `max_i c_i<=1/3`, `c_i=||u_i||^2`, `s_3(A)>=1`,       (1.1)

with a selected physical coordinate `k` satisfying `|d_k|>=1`. For leaves `i,j != k`, write

`q_ij=det(u_i,u_j)^2`.                                                  (1.2)

For a leaf pair `E`, let `Delta_E` be the complementary leave-one-out determinant weight, set

`W=sum_E q_E Delta_E`, `mu(E)=q_E Delta_E/W`,                           (1.3)

and for a four-set `R={a,b,c,d}` define the three perfect-matching weights

`w_1=q_ab q_cd`, `w_2=q_ac q_bd`, `w_3=q_ad q_bc`, `S_R=w_1+w_2+w_3`.   (1.4)

The partner proves the exact identities

`W=2 sum_R S_R`,                                                        (1.5)

`max_m w_m <= (2/3) S_R`,                                              (1.6)

and the four-set probability law

`nu(R)=S_R/(sum_T S_T)`.                                                (1.7)

If `M=E_mu |tau_E|`, an edge is called good when `|tau_E|<=M/eta`. Let `C_3` be the four-sets for which all three matchings are clean, and `C_2` those with exactly two clean matchings. If `kappa_R` is the dirty matching fraction in `C_2`, then for every `0<eta<1/6`, `0<gamma<1`,

`nu(C_3 union {R in C_2:kappa_R<=gamma}) >=1-6 eta-2 eta/gamma`.       (1.8)

The present run also consumes my previous sharp leave-one-out DPP theorem:

`yspennstate/math-open-problems@090f67b2941f8781c0da2cb3be2f5698b5742418`.

In the chamber (1.1) it improves the normalization to

`W>=1/12`, hence `sum_R S_R>=1/24`,                                  (1.9)

and, in the partner non-rank-one branch,

`M=E_mu |tau_E| <= M_0/rho`,                                          (1.10)

where

`M_0=3037500/(1536 e^2)=267.630809134903...`,                         (1.11)

and `rho=P{X^T A X in J}/|J|` is the actual slab ratio.

The purpose of this run is to turn (1.8)-(1.10) into a coefficient-space collapse with a positive **unnormalized** amount of four-point Pluecker currency, without dividing by any individual minor.

## 2. Extremal-product reduction retained at exact scope

For completeness, the product-law reduction used throughout B13 is the following optimizer-free statement.

### Proposition 2.1 — zero-loss coordinatewise purification

Let `K>=0` be bounded and measurable on `R^n`. For arbitrary probability densities `0<=f_i<=1`, there exist measurable sets `E_i` with `|E_i|=1` such that

`int K(x) prod_i 1_{E_i}(x_i) dx >= int K(x) prod_i f_i(x_i) dx`.      (2.1)

#### Proof

Fix all coordinates except `i` and define the fiber score

`G_i(t)=int K(x_1,...,t,...,x_n) prod_{j!=i} f_j(x_j) dx_{-i}`.       (2.2)

Then `0<=G_i<=||K||_infinity`. On the nonatomic line, the bathtub principle gives a measurable unit-measure set `E_i` satisfying

`int_{E_i} G_i >= int f_i G_i`,                                     (2.3)

because `0<=f_i<=1` and `int f_i=1`. Replace `f_i` by `1_{E_i}`. The objective does not decrease. Repeating for `i=1,...,n` proves (2.1). No global optimizer is asserted.

For the QFORM slab kernel `K=1_{x^T A x in J}` this is exact and has no integrability issue. By Lebesgue regularity, each unit set may, for a strict witness, be approximated in symmetric difference by a bounded finite union of intervals of measure exactly one. The product error is at most the sum of the one-coordinate symmetric-difference errors. This approximation has no uniform diameter or fragment-count bound. QED.

Thus every actual slab witness can be studied geometrically on arbitrary unit-measure product sets, for the same `A` and the same interval `J`, without assuming a single interval or centered uniform law.

## 3. New deterministic lemma: a light Pluecker matching contains a near-parallel physical pair

For a nonzero physical row `u_i`, put `ell_i=||u_i||^2`, and for `i!=j` define its projective sine

`sigma_ij^(1/2) = |det(u_i,u_j)|/(||u_i|| ||u_j||) in [0,1]`.         (3.1)

Thus

`q_ij=ell_i ell_j sigma_ij`.                                         (3.2)

### Lemma 3.1 — `QFORM-LIGHT-MATCHING-PROJECTIVE-PAIR-v1`

For a four-set `R={a,b,c,d}`, suppose one perfect matching, say `{ab,cd}`, has

`w_0/S_R<=gamma`.                                                    (3.3)

Then one of its two physical pairs obeys

`boxed: sin angle(u_a,u_b) <=(3 gamma)^(1/4)`                       (3.4)

or

`boxed: sin angle(u_c,u_d) <=(3 gamma)^(1/4)`.                      (3.5)

#### Proof

All three perfect matching weights have the same row-norm factor

`P=ell_a ell_b ell_c ell_d`,                                       (3.6)

and every sine-square factor is at most one. Therefore `S_R<=3P`. Since

`w_0=P sigma_ab sigma_cd`,                                         (3.7)

(3.3) gives `sigma_ab sigma_cd<=3 gamma`. Taking square roots and then the smaller of the two sine factors proves (3.4)-(3.5). QED.

This is exact and requires no lower bound on any `ell_i`.

## 4. New deterministic lemma: six good edges force a hub leaf or a three-row projective cluster

Rotate only the latent coefficient basis so

`u_k=(sqrt(c),0)`, `c=c_k>0`.                                     (4.1)

For a leaf with nonzero transverse coordinate write

`u_i=(x_i,y_i)`, `s_i=y_i^2`, `r_i=x_i/y_i`.                      (4.2)

Then

`q_ki=c s_i`,
`q_ij=s_i s_j (r_i-r_j)^2`.                                      (4.3)

Recall

`tau_ij=d_k q_ij+d_i q_kj+d_j q_ki`.                              (4.4)

Put

`a_i=c d_i/s_i`,
`e_ij=tau_ij/(s_i s_j)`.                                          (4.5)

Then the exact identity is

`e_ij=a_i+a_j+d_k(r_i-r_j)^2`.                                    (4.6)

Equivalently, with `b_i=a_i+d_k r_i^2`,

`e_ij=b_i+b_j-2d_k r_i r_j`.                                      (4.7)

### Lemma 4.1 — `QFORM-SIXEDGE-SLOPE-RIGIDITY-v1`

Let `R` be a four-set whose six edges satisfy `|tau_ij|<=T`. Fix `theta>0`. Then either

`min_{i in R} s_i < theta`,                                       (4.8)

or there is a three-set `C subset R` such that every `i,j in C` satisfies

`boxed: sin angle(u_i,u_j) <= sqrt(2T/(|d_k| theta^2))`,           (4.9)

and every `i in C` satisfies

`boxed: |c d_i/s_i| <= (7/2) T/theta^2`.                          (4.10)

#### Proof

If (4.8) fails, all `s_i>=theta`, so from (4.5)

`|e_ij|<=epsilon:=T/theta^2`.                                     (4.11)

For four distinct labels `1,2,3,4`, (4.7) gives the exact mixed-difference identity

`e_13-e_14-e_23+e_24
 =-2d_k(r_1-r_2)(r_3-r_4)`.                                       (4.12)

Hence every perfect matching of slope differences obeys

`|(r_1-r_2)(r_3-r_4)| <= delta:=2 epsilon/|d_k|`.                 (4.13)

Order the four slopes as `z_1<=z_2<=z_3<=z_4`. Applying (4.13) to the matching `{1,3},{2,4}` gives

`(z_3-z_1)(z_4-z_2)<=delta`.                                      (4.14)

Thus either the first three or the last three slopes lie in an interval of length `sqrt(delta)`. Let `C` be that triple. For any two leaves,

`sin angle(u_i,u_j)
 = |r_i-r_j|/[sqrt(1+r_i^2)sqrt(1+r_j^2)]
 <=|r_i-r_j|`,                                                    (4.15)

which proves (4.9).

For distinct `i,j,l in C`, (4.6) gives another exact identity,

`a_i
 =-d_k(r_i-r_j)(r_i-r_l)
   +(e_ij+e_il-e_jl)/2`.                                          (4.16)

The first term is at most `|d_k| delta=2epsilon`, and the second at most `3epsilon/2`. This proves (4.10). QED.

If (4.8) holds, the corresponding physical coefficient row is close to the hub line in the exact sense

`dist(u_i,span(u_k))=|y_i|<sqrt(theta)`.                           (4.17)

Again, this is coefficient geometry only; no random variable has been rotated.

## 5. Main theorem: positive absolute packet mass collapses at the optimized rho^{-1/10} scale

### Theorem 5.1 — `QFORM-ABSOLUTE-PACKET-PROJECTIVE-110-v1`

Assume the exact diffuse rank-two chamber (1.1), the non-rank-one branch giving (1.10), and `rho>1`. Define

`gamma=rho^(-2/5)`,
`eta=gamma/16`,
`theta=rho^(-1/5)`.                                                (5.1)

Let

`C_rho=C_3 union {R in C_2:kappa_R<=gamma}`.                       (5.2)

Then

`boxed:
 nu(C_rho) >= 7/8-(3/8)rho^(-2/5)`,                              (5.3)

and, using (1.9),

`boxed:
 sum_{R in C_rho} S_R
 >= (7-3rho^(-2/5))/192.}`                                        (5.4)

Moreover every `R in C_rho` satisfies a concrete projective degeneration. Namely, at least one of the following occurs:

1. a leaf is close to the hub coefficient line,

`boxed: dist(u_i,span(u_k))<rho^(-1/10);}`                         (5.5)

2. two physical leaf rows are nearly projectively parallel,

`boxed: sin angle(u_i,u_j)
 <=B_0 rho^(-1/10),}`                                             (5.6)

where

`B_0=sqrt(2T_0)=92.54288677319774...`,                             (5.7)

and

`T_0=16M_0=4282.092946158448...`.                                 (5.8)

In the `C_3` branch, if (5.5) does not occur, one can choose a three-leaf cluster `C` for which **all three** pairwise projective sines satisfy (5.6), and simultaneously

`boxed:
 |c d_i/s_i|
 <=A_0 rho^(-1/5), i in C,}`                                     (5.9)

with

`A_0=(7/2)T_0=14987.325311554569...`.                             (5.10)

In the `C_2` branch the sharper pair bound holds:

`boxed:
 sin angle(u_i,u_j)
 <=3^(1/4) rho^(-1/10)
 =1.3160740129524924... rho^(-1/10).}`                            (5.11)

#### Proof

Apply the completed partner theorem (1.8) with (5.1). Since `eta=gamma/16`,

`1-6eta-2eta/gamma
 =1-(3/8)gamma-1/8
 =7/8-(3/8)rho^(-2/5)`,                                          (5.12)

which proves (5.3). Multiplying by `sum_R S_R>=1/24` gives (5.4).

By (1.10), every good edge in the partner theorem obeys

`|tau_E|<=M/eta
 <=16M_0 rho^(-1)/gamma
 =T_0 rho^(-3/5).`                                                (5.13)

If `R in C_2` with `kappa_R<=gamma`, Lemma 3.1 gives (5.11).

If `R in C_3`, all six edges are good. Apply Lemma 4.1 with

`T=T_0 rho^(-3/5)`, `theta=rho^(-1/5)`.                           (5.14)

If some `s_i<theta`, (4.17) gives (5.5). Otherwise

`epsilon=T/theta^2=T_0 rho^(-1/5)`,                               (5.15)

and `|d_k|>=1` implies

`sqrt(2epsilon/|d_k|)
 <=sqrt(2T_0)rho^(-1/10)=B_0rho^(-1/10)`,                         (5.16)

while (4.10) gives (5.9). This proves the theorem. QED.

### Why the exponent 1/10 is the natural balance of this packet mechanism

More generally, put `gamma=rho^{-a}` and `theta=rho^{-b}`. The `C_2` projective angle has exponent `a/4`; the small-transverse-coordinate alternative has exponent `b/2`; and the `C_3` slope-cluster angle has exponent `(1-a)/2-b`. Equalizing the three gives

`a=2/5`, `b=1/5`,                                                 (5.17)

and the common exponent is exactly `1/10`. This optimization uses only the partner packet theorem and the exact slope identities above.

## 6. Geometric product-set consequence

By Proposition 2.1, Theorem 5.1 applies without loss to every unit-product-set slab witness. Thus, in the exact chamber (1.1), if measurable sets `|E_i|=1` obey

`|{x in prod_i E_i : x^T A x in J}| = rho |J|`,                   (6.1)

then the coefficient system must have the positive raw packet mass (5.4) on four-sets satisfying (5.5) or (5.6). In particular, define the packet degeneracy

`zeta_R=min( min_{i in R} dist(u_i,span(u_k)),
             min_{i<j in R} sin angle(u_i,u_j) )`.                 (6.2)

Then

`boxed:
 sum_{R: zeta_R<=B_0 rho^(-1/10)} S_R
 >=(7-3rho^(-2/5))/192.}`                                        (6.3)

This is an actual geometric sublevel-set obstruction. A hypothetical diverging-density sequence in the exact diffuse rank-two non-rank-one chamber must place a fixed positive amount of its **unnormalized** four-point Pluecker matching currency on packets becoming asymptotically one-dimensional in physical coefficient geometry.

Equivalently, if every positive-volume packet has `zeta_R>=zeta>0`, then

`boxed: rho <= max(1,(B_0/zeta)^10).}`                             (6.4)

The constant is intentionally not optimized. The point is that no individual determinant is inverted.

## 7. Exact zero-cancellation endpoint classification

The limiting algebra behind Theorem 5.1 can be classified exactly.

### Theorem 7.1 — `QFORM-TAU-COMPLETEGRAPH-EXACT-CLASSIFICATION-v1`

Keep (4.1). Let `L` be a set of at least four leaves with `s_i>0` for every `i in L`. If

`tau_ij=0 for every distinct i,j in L`,                            (7.1)

then all but at most one of the slopes `r_i=x_i/y_i` are equal. If `r_0` is the common slope, then every leaf in the common-slope class satisfies

`boxed: d_i=0`,                                                    (7.2)

while a possible exceptional leaf `h` satisfies

`boxed:
 c d_h/s_h = -d_k(r_h-r_0)^2.}`                                  (7.3)

#### Proof

Under (7.1), (4.7) becomes

`b_i+b_j=2d_k r_i r_j`.                                           (7.4)

For four distinct labels `i,m,j,l`, the mixed difference gives

`(r_i-r_m)(r_j-r_l)=0`,                                           (7.5)

because `d_k!=0`. Choose `i,m` with distinct slopes if such a pair exists. Then all labels outside `{i,m}` have one common slope `r_0`. Applying (7.5) to the alternate pairing `{i,j},{m,l}` with two outside labels shows

`(r_i-r_0)(r_m-r_0)=0`.                                           (7.6)

Hence at most one leaf is exceptional.

The common class has at least three members. For two common-slope leaves, (4.6) and (7.1) give `a_i+a_j=0`; using three leaves forces each `a_i=0`, hence `d_i=0`. For an exceptional `h`, (4.6) against a common leaf gives

`a_h+d_k(r_h-r_0)^2=0`,                                          (7.7)

which is (7.3). QED.

So complete pairwise transverse cancellation does not leave an arbitrary four-dimensional packet: it is a one-projective-line configuration plus at most one exceptional leaf, with the physical diagonal forced to vanish on the common line.

## 8. What is paid and what remains

This run materially sharpens the previous unpaid implication `QFORM-ABSOLUTE-PLUCKER-PACKET-TO-BANK-RECEIVER-v1`:

- the partner's normalized `C_2/C_3` packet core is converted to an **absolute raw mass** lower bound (5.4);
- the `C_2` escape necessarily carries a physical near-parallel pair, with no row-norm floor;
- the `C_3` escape is either a physical leaf approaching the hub line or a three-row projective cluster, and the normalized diagonal curvature on that cluster is simultaneously `O(rho^-1/5)`;
- at exact zero cancellation the leaf system is classified by Theorem 7.1.

The first unpaid implication is now

`QFORM-PROJECTIVE-COLLAPSE-TO-PRODUCT-BANK-RECEIVER-v1`:

> Consume the fixed positive packet mass from (6.3) with a product-preserving receiver. In the near-hub branch, aggregate the leaves approaching `span(u_k)` into a physical bank before paying any reciprocal coefficient. In the near-parallel-pair / three-row-cluster branch, quotient the common projective direction while retaining the `O(rho^-1/5)` transverse diagonal-curvature currency and all outside quadratic coefficients. For a general, not exactly `D+U Lambda U^T`, high-ratio survivor, retain account02/B13's proved every-cut `s_5=O(rho^-1)` cross-tail obstruction instead of deleting the tail as a small random perturbation.

This remaining receiver is not proved here. The full QFORM conjecture therefore remains **OPEN**. No unrestricted continuity conclusion is claimed.

## 9. Arithmetic / algebra checks

A local finite check verified the mixed-difference identity (4.12) and the recovery identity (4.16) on 1000 random coefficient configurations to maximum absolute floating error below `5e-13`. The constants used above are

`M_0=267.630809134903...`,
`T_0=4282.092946158448...`,
`B_0=92.54288677319774...`,
`3^(1/4)=1.3160740129524924...`,
`A_0=14987.325311554569...`.

The finite checks are diagnostics only; Sections 3-7 are analytic proofs.
