SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B07, 2026-09-23T13:07:49Z.
attacking: the stable rank-four two-sided >3/4 fourth-volume survivor — double-anchor its entire fourth-compound mass, then force residual E3, a paid physical pair, or six disjoint original-coordinate banks without selecting one minor.

# fleet03/B07 — fourth-volume double-anchor compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: coordinate minor selection / GEOMETRY  
Run: `20260923T130749Z-fleet03-B07-qform-r30`  
Initial control commit: `yspennstate/math-research-brain@59383df8077cb277b6ba91f56b93a642872bdb3e`  
Pre-publication main observed: `yspennstate/math-research-brain@9c69e96e9ef6095c411efe2801498cabdbd7bb16`  
Execution: `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`  
Status: **NEW SUPPORTING AGGREGATE-MINOR COMPILER / DESIGNATED PARTNER APPLIED / ONE SUBBRANCH ESSENTIALLY BOUNDED / FULL QFORM OPEN / FULL CONTINUITY OPEN**.

The unrestricted conjecture remains open. No Gaussian, moment, compact-support, connected-support, log-concavity, diagonal-basis, or post-rotation independence assumption is used. Every independence statement below concerns disjoint subsets of the original independent coordinates. No law-uniform pointwise quadratic-phase estimate, arbitrary-joint coarea estimate, positive conditional-density moment, or single selected reciprocal minor is used.

## 1. Source-valid incoming state

### 1.1 Designated partner fleet04/B07

The completed designated-partner result actually used is

`yspennstate/math-open-problems@842652e93680813d356fde0f15f12ab70b59c3c3`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B07/20260923T091740Z-fleet04-B07-actual-core-diffuse-banks-r1/REPORT.md`.

It supplies, in the current N3 survivor, the fixed physical coefficient scale

`h=(2sqrt(2)-1)/1572864`

and, after the completed same-slot disjoint-innovation step, two disjoint original-coordinate star banks with

`P:=||r0||_2 ||c0||_2 > beta h^2`,  `beta=sqrt(63)/16`.             (1.1)

The same N3 state has the global physical-coordinate caps

`|A_ij|<=h/8` for `i!=j`,   `|A_ii|<tau0:=h^2/128`.                (1.2)

Numerically the partner lower floor is

`P>6.7038341000970468e-13`.                                       (1.3)

This partner result is used quantitatively in Sections 5 and 6; it is not merely cited.

### 1.2 Current B07 rank-four survivor

The immediately preceding B07 natural-scale compiler is

`yspennstate/math-open-problems@d54c89467491a2dc95da16b392ed1d95b5554e8a`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260923T124137Z-fleet03-B07-qform-r31/REPORT.md`,

with the later fourth-volume addendum

`yspennstate/math-open-problems@bfa9412bfb743bd30fc104e779f280dce0a0db14`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260923T124137Z-fleet03-B07-qform-r31/FRESH_SOURCE_ADDENDUM.md`.

All other branches in that report are already paid or routed separately. The rank-four state left by the addendum has an actual ORIGINAL-coordinate cross block `M`, a scale

`a=s3(M)>16 sqrt(P/4617)`,                                        (1.4)

small fifth tail, and fourth-compound row and column inclusion maxima both strictly between `3/4` and `1`. Also

`E4(M)>=a^8/256`.                                                  (1.5)

The addendum records the actual fourth-volume marginal inequality

`W4 <= (E3/E4) M M^T`,                                           (1.6)

and, using `T3 E3<=4E4` and `T3>=s4(M)^2>=a^2/256`, concludes that any physical row whose fourth-volume inclusion marginal exceeds `3/4` has literal row norm squared greater than

`3a^2/4096`.                                                      (1.7)

The transposed statement holds for columns.

### 1.3 Analytic pair receiver

For the physical-pair exit I use the completed arbitrary-rank theorem

`yspennstate/math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc`,

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`.

If an ORIGINAL-coordinate principal pair `B` is invertible indefinite, `D=|det B|`, `kappa=sigma_min(B)`, and the full target has `s3(A)>=1`, then

`||p_Q||_infinity <=3*400^(1/3) (D^2 kappa)^(-1/6)`.              (1.8)

This proves essential boundedness, not continuity.

## 2. Double-anchor more than half of the entire fourth compound

Choose a physical row `u` whose fourth-volume row inclusion marginal `rho_u` is maximal, and a physical column `v` whose fourth-volume column inclusion marginal `sigma_v` is maximal. In the remaining state,

`rho_u>3/4`, `sigma_v>3/4`.                                      (2.1)

Let

`G4^(u,v)(M)
 := sum_{R,T: |R|=|T|=3} det M[{u} union R,{v} union T]^2`,       (2.2)

where `R` and `T` range over physical rows/columns different from the anchors. Normalize all squared `4x4` minors by `E4(M)`. If `I,J` denote the random row and column 4-subsets under that distribution, then

`P(u in I)=rho_u`, `P(v in J)=sigma_v`.

The union bound gives

`P(u in I and v in J)>=rho_u+sigma_v-1>1/2`.                     (2.3)

Therefore

`G4^(u,v)(M)>E4(M)/2>=a^8/512`.                                  (2.4)

This is the first key point: two actual physical coordinates carry more than half of the whole fourth-compound mass jointly, so no single `4x4` minor is selected.

By (1.7), with

`g:=sqrt(3)a/64`,                                                 (2.5)

the full literal row and column of the selected anchors obey

`||M[u,*]||_2>g`, `||M[*,v]||_2>g`.                              (2.6)

## 3. Bordered fourth-compound inequality

Write the actual physical cross block around `(u,v)` as

`M = [[b,r^T],[c,D]]`,                                           (3.1)

where `b=M_uv`, `r` is the remainder of row `u`, `c` is the remainder of column `v`, and `D` is the far physical core.

For every row triple `R` and column triple `T`, Laplace expansion gives

`det M[{u} union R,{v} union T]
 = b det D[R,T] - Psi_(R,T)`,                                   (3.2)

where

`Psi_(R,T)= r_T^T adj(D[R,T]) c_R`.                              (3.3)

The family `Psi_(R,T)` is naturally the matrix of the exterior-map composition

`K=(c wedge .) o (wedge^2 D) o i_r`                              (3.4)

from the third exterior power of the far column space to the third exterior power of the far row space, up to irrelevant orientation signs. Wedge multiplication by `c` has operator norm `||c||`, contraction by `r` has operator norm `||r||`, and

`||wedge^2 D||_HS^2=E2(D)`.                                     (3.5)

Hence

`sum_(R,T) Psi_(R,T)^2
 =||K||_HS^2
 <=||c||^2 ||r||^2 E2(D)`.                                    (3.6)

Taking the Euclidean norm in the full anchored-minor array and using (3.2),

`sqrt(G4^(u,v)(M))
 <= |b| sqrt(E3(D)) + ||c|| ||r|| sqrt(E2(D))`.                  (3.7)

Combining (2.4) and (3.7), at least one of

`|b| sqrt(E3(D)) > a^4/(32sqrt(2))`,                             (3.8)

`||c|| ||r|| sqrt(E2(D)) > a^4/(32sqrt(2))`                      (3.9)

must hold.

This is `QFORM-R4-DOUBLEANCHOR-COMPOUND-DOWNSHIFT-v1`. It converts a determinant-weighted fourth-volume concentration into lower compound currencies without inverting any individual determinant.

## 4. A star-star/E2 selector with collision accounting

I now prove a general selector used on (3.9).

### Lemma 4.1 — `QFORM-STARSTAR-E2-TO-PAIR-OR-SIXBANK-v1`

Let `c` and `r` be nonzero physical star vectors on the row and column sides of a matrix `D`, and put

`C=||c||`, `R=||r||`, `E=E2(D)>0`.                              (4.1)

Let `rho_i` be the row inclusion probabilities and `sigma_j` the column inclusion probabilities under the squared-`2x2`-minor distribution of `D`:

`rho_i=E^(-1) sum_(K contains i,T) det D[K,T]^2`,
`sum_i rho_i=2`,                                                  (4.2)

and similarly `sum_j sigma_j=2`. Define the star/minor collision parameters

`A_c=sum_i (c_i^2/C^2) rho_i`,
`A_r=sum_j (r_j^2/R^2) sigma_j`.                                 (4.3)

Then either

(a) there is a literal physical coefficient in one star with

`|c_i|>=C/sqrt(60)` or `|r_j|>=R/sqrt(60)`,                      (4.4)

or there are six mutually disjoint ORIGINAL-coordinate banks — three on each side — such that, for one of the two cross matchings,

`||c_L0|| ||r_R0|| B1 B2 > C R sqrt(E)/(27sqrt(3))`,             (4.5)

where `B1,B2` are the Frobenius norms of the two matched `D` subblocks.

#### Proof

If `A_c>=1/3`, let `H={i:rho_i>=1/6}`. Since `sum rho_i=2`, `|H|<=12`. Writing `p(H)=sum_(i in H)c_i^2/C^2`,

`A_c <= p(H)+(1-p(H))/6=1/6+5p(H)/6`.                            (4.6)

Thus `p(H)>=1/5`, and some `i in H` has `c_i^2/C^2>=1/60`, proving (4.4). The same argument applies if `A_r>=1/3`.

Assume now `A_c<1/3` and `A_r<1/3`. Choose independently a row index `i` with probability `c_i^2/C^2`, a column index `j` with probability `r_j^2/R^2`, and a squared-minor pair `(K,T)`. By the union bound,

`P(i notin K and j notin T)>1-A_c-A_r>1/3`.                      (4.7)

Equivalently, the disjoint monomial weight

`W:=sum_(i notin K,j notin T)c_i^2 r_j^2 det D[K,T]^2`

satisfies

`W>(1/3) C^2 R^2 E`.                                             (4.8)

Randomly color all far row coordinates by `0,1,2`, and independently all far column coordinates by `0,1,2`. Retain a monomial in (4.8) if `i` has row color zero, the two members of `K` have row colors one and two in either order, `j` has column color zero, and the two members of `T` have column colors one and two in either order. Because the indices are disjoint inside an accepted monomial, its retention probability is

`(1/3 * 2/9)^2=4/729`.                                          (4.9)

So some coloring satisfies

`||c_L0||^2 ||r_R0||^2 S > (4/2187) C^2 R^2 E`,                 (4.10)

where `S` is the total accepted squared `2x2`-minor mass. Every accepted determinant obeys

`det[[x,y],[z,w]]^2<=2(x^2w^2+y^2z^2)`.                         (4.11)

Summing (4.11) over accepted minors gives

`S<=2(B11^2 B22^2+B12^2 B21^2)`.                                (4.12)

Thus one of the two matchings satisfies

`||c_L0||^2 ||r_R0||^2 B1^2 B2^2
 > (1/2187) C^2 R^2 E`.                                         (4.13)

Taking square roots and using `sqrt(2187)=27sqrt(3)` proves (4.5). All six selected banks are pairwise disjoint because they are color classes on two initially disjoint original-coordinate sides. QED.

## 5. Apply the compiler to the remaining rank-four state

The edge-heavy case `|b|>=g/2` is already paid by the preceding r31 report. Work in the still-unpaid edge-light case

`|b|<g/2`.                                                       (5.1)

By (2.6),

`||r||,||c|| > sqrt(3)g/2 = 3a/128`.                            (5.2)

### 5.1 First lower-compound branch: residual third volume

If (3.8) holds, then (5.1) and (2.5) give

`sqrt(E3(D)) > a^4/(16sqrt(2)g)=4a^3/sqrt(6)`.                   (5.3)

Therefore

`boxed: E3(D)>(8/3)a^6`.                                        (5.4)

This is a genuinely residual physical third-volume packet on the far core. It retains determinant weight in aggregate; no `3x3` minor has been selected or reciprocated.

### 5.2 Second lower-compound branch: pair or six banks

Suppose (3.9) holds and apply Lemma 4.1.

If its collision alternative (4.4) occurs, (5.2) yields a literal off-diagonal physical coefficient

`t> (3a/128)/sqrt(60)=sqrt(3)a/(256sqrt(5)) = g/(4sqrt(5)).       (5.5)

The designated partner lower floor (1.1), together with (1.4), gives

`a>1.9279762269984055e-7`,
`t>5.8336092336317451e-10`.                                      (5.6)

Meanwhile `2tau0=2.1115092689870561e-14`, so in particular `t>2tau0`. The ORIGINAL-coordinate principal pair attached to that coefficient has diagonals of modulus below `tau0`; hence it is invertible indefinite, with

`D_pair>=3t^2/4`, `kappa_pair>t/2`.                              (5.7)

Applying (1.8),

`||p_Q||_infinity
 <3*400^(1/3)*(32/9)^(1/6)t^(-5/6)`.                            (5.8)

At the designated-partner floor this is

`boxed: ||p_Q||_infinity <1.354e9`.                              (5.9)

Thus this collision branch is fully paid at the target quantifiers. The theorem used here provides essential boundedness only, so continuity is not claimed on this branch.

If instead the diffuse collision alternative (4.5) occurs, combine it with (3.9):

`boxed:
 ||c_L0|| ||r_R0|| B1 B2
 > a^4/(864sqrt(6)).`                                            (5.10)

These are six mutually disjoint ORIGINAL-coordinate banks and therefore preserve genuine product provenance. Arbitrary within-bank curvature, unused couplings, and all additional spectrum remain untouched.

## 6. Main new routing theorem

### Theorem 6.1 — `QFORM-R4-34COLOOP-TO-E3-PAIR-OR-SIXBANK-v1`

In the current B07 rank-four survivor from the r31 fourth-volume addendum — namely, `s3(M)=a>16sqrt(P/4617)`, small fifth tail, both row and column fourth-volume maximal inclusion probabilities in `(3/4,1)`, the N3 coefficient caps (1.2), and the designated-partner scale (1.1) — one of the following holds:

1. the already-paid edge-heavy physical-pair branch;
2. the residual far core has `E3(D)>(8/3)a^6`;
3. the full ambient QFORM law has an essentially bounded density, quantitatively `<1.354e9`, via a newly forced ORIGINAL-coordinate indefinite pair;
4. six mutually disjoint original-coordinate banks satisfy the product certificate (5.10).

The new content is alternatives 2--4 in the edge-light state. It narrows `QFORM-STABLE-R4-TWOSIDED-34COLOOP-CONDITIONAL-H3-RECEIVER-v1` without selecting or paying the reciprocal of one tiny coordinate minor.

The designated fleet04/B07 result is applied twice: first through the positive lower floor `P>beta h^2` that feeds (1.4), and then to make the collision-pair bound (5.9) a dimension-free numerical constant under the exact target hypotheses.

## 7. Remaining debt and regularity status

The first unpaid implication after this run is

`QFORM-R4-RESIDUAL-E3-OR-SIXBANK-CURVATURE-RECEIVER-v1`:
consume either the far-core `E3(D)>(8/3)a^6` packet or the six-bank product packet (5.10) while retaining arbitrary same-bank quadratic curvature and the true ambient Schur remainder. A natural next split is to apply the existing three-volume marginal theorem to the residual `E3(D)` packet; only its physically concentrated marginal survivor should then remain. The separate stable-rank-three and relative-rank-one/rank-two siblings from prior B07 runs are not claimed closed here.

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains **OPEN**. The newly paid pair branch proves only essential boundedness. Previously paid D5, volume-stability, and fourth-volume diffuse/end-point branches retain their separate continuity conclusions from their source theorems.

## 8. Computation and provenance

`CHECKS.py` and `CHECKS.txt` in this directory check the bordered fourth-compound inequality on 250 deterministic random matrices and verify the propagated constants. Their output ends `STATUS=PASS`. These are algebraic/numerical regression checks only; the proof is Sections 2--6.

Repository access and native learned-memory ingestion are separate. No authenticated native receiver retrieval occurred, so this run remains `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`.
