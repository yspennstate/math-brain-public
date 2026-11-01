SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B10, 2026-09-23T02:39:46Z.
attacking: the active near-null nonzero-coloop interpolation first; after finding that exact scope already proved in fresh current work, splice it into B10's exact-rank-three proof graph and quantify the first genuinely unpaid small-Pluecker-mass hub/star collar.

# fleet03/B10 r23b — exact-coloop interpolation consumed; small-disjoint-mass forces a physical near-null hub/star

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** rank-three coupled case  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Classification:** `SOURCE-MATCHED SUBPROBLEM CLOSED + NEW SUPPORTING STRUCTURAL REDUCTION / FULL TARGET OPEN`.

## 1. Exact target and current correction boundary

The target remains unrestricted: for every finite `n`, arbitrary independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal finite bound on the essential supremum of the density of `X^T A X`, or give a valid counterexample. No Gaussianity, log-concavity, moment, compact-support, connected-support, or diagonal-basis hypothesis is introduced. General spectral rotations are not treated as preserving independence. Continuity is tracked separately.

Fresh current owner continuation assigns B10 specifically to the **near-null nonzero coloop interpolation**, distinct from the already-paid exact-null endpoint. The live corrections still forbid law-uniform pointwise quadratic-phase decay, arbitrary-joint rank-three coarea, worst conditional projection-height bounds, independence after rotation, and extraction of one uniformly well-conditioned physical minor from the spectral hypothesis alone.

The mathematical source tree changed materially since B10 r22: a source-matching theorem now closes the exact coloop interpolation. Under the owner's rule, I do not duplicate that proof. I apply it below and move the B10 proof graph to the first genuinely unpaid collar.

## 2. Source-matching result: every exact spectral coloop is paid uniformly

The completed theorem is

`QFORM-CROSS-TRANSVERSE-PROJECTION-PRODUCT-v1`,

source:

`yspennstate/math-open-problems@80f95e245b7f3418e8da36173ac4eb9d81fb58a7`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B16/20260923T003846Z/REPORT.md`.

Let an exact-rank-three target have a leverage-one ORIGINAL physical coordinate. In an orthonormal spectral basis write the resulting coefficient matrix as

`B=[[a,b^T],[b,C]]`, `D=|det B|=|det Lambda|>=1`.

The original coloop scalar is genuinely independent of the two-dimensional projection of the remaining product source, and the latter has joint density cap at most `2`.

When `|a|<=1/2`, rotate only inside the two-dimensional receiver plane so that `b=(beta,0)` and write

`C=[[c,d],[d,e]]`, `P=beta^2|e|`.

The inverse-cofactor identity is

`|(B^{-1})_00|=|det C|/D<=1`,

because every eigenvalue of `B` has modulus at least one. Therefore

`P=|a det C-det B| >= D-|a||det C| >=D/2`.                 (2.1)

The completed cross-transverse theorem gives, with receiver density cap `M<=2`,

`||p_Q||_infinity
 <=103680^(1/3) M^(2/3)(DP)^(-1/6)`

`<=103680^(1/3) 2^(5/6) D^(-1/3)`

`<83.707`.                                                  (2.2)

This is uniform through every nonzero near-null value and through `a=0`.

When `|a|>1/2`, the completed orientation-free scalar-pivot / rank-two affine half-Riesz theorem gives

`||p_Q||_infinity <=128(|a|D)^(-1/4)<152.219`.              (2.3)

Hence the exact-coloop interpolation requested by the current B10 assignment is now completely paid:

`boxed: exact spectral coloop => ||p_Q||_infinity<153.`      (2.4)

The source theorem proves essential boundedness. It does not promote the full exact-coloop conclusion to a new continuity theorem, so I do not do so here.

## 3. Compatible fleet04 result applied at an actual inequality

The exact designated partner `fleet04/B10` still has no completed current-QFORM mathematical artifact in the fresh canonical handoff/archive lookup. I do not fabricate one. I instead apply the completed compatible fleet04/B16 theorem

`QFORM-RULED-PLUECKER-ENDPOINT-v1`,

source:

`yspennstate/math-open-problems@b111363ff02b67015d14db35482e0150591744cd`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B16/20260922T231542Z-fleet04-B16-QFORM-r1/REPORT.md`.

For exact rank three write

`A=R Lambda R^T`, `R^T R=I_3`,

and put

`w_S=det(R_S)^2`, `|S|=3`.

Cauchy--Binet gives `sum_S w_S=1`, so `w` is a probability law on physical bases. For independent `S,T~w` define the disjoint-Pluecker mass

`d=P(S cap T=emptyset)`.                                     (3.1)

The fleet04 theorem yields the actual two-sided inequality

`||p_Q||_infinity <=12 |det Lambda|^(-1/3)d^(-1/6)`          (3.2)

whenever `d>0`. In particular,

`boxed: d>=1/64 => ||p_Q||_infinity<=24.`                    (3.3)

This branch has a continuous density by the product-preserving cross-cut Fourier proof. For indefinite signature, the same fleet04 theorem independently gives the one-sheet / majority-sign bound

`ess sup p_Q <=pi sqrt(2)`                                    (3.4)

on the appropriate sign side, without requiring `d>0`.

## 4. New identity for the small-disjoint-mass collar

The following exact identity converts small `d` into an ORIGINAL-coordinate hub certificate without selecting a reciprocal minor.

### Lemma 4.1 — `QFORM-PLUECKER-DISJOINT-GRAM-IDENTITY-v1`

For a physical triple `S`, put

`G_S=R_S^T R_S`.

Then

`boxed: d=sum_S w_S det(I_3-G_S).`                           (4.1)

#### Proof

Fix `S`. By Cauchy--Binet on the complementary row frame,

`sum_(T subset S^c, |T|=3) w_T
 =det(R_(S^c)^T R_(S^c))`

`=det(I_3-R_S^T R_S)`

`=det(I_3-G_S)`.                                             (4.2)

Multiply (4.2) by `w_S` and sum over `S`. The left side is exactly the probability that two independent `w`-distributed triples are disjoint. QED.

### Corollary 4.2 — a three-coordinate approximate-coloop packet

If `0<d<delta`, there is a physical basis `S` with `w_S>0` and

`det(I-G_S)<=d<delta`.                                       (4.3)

Let the eigenvalues of `G_S` be `mu_1>=mu_2>=mu_3`. Since `0<=G_S<=I`,

`prod_k(1-mu_k)<=d`,

so

`mu_1>=1-d^(1/3)`.                                           (4.4)

Writing physical leverages `c_i=||r_i||^2`,

`sum_(i in S)c_i=tr G_S>=mu_1`,

and therefore some `i in S` obeys

`boxed: c_i>= [1-d^(1/3)]/3.`                               (4.5)

For the concrete collar left by (3.3),

`0<d<1/64 => c_i>1/4`.                                      (4.6)

Thus the small-disjoint-mass branch cannot remain a completely diffuse rank-three frame: three ORIGINAL coordinates already capture more than `3/4` of one spectral direction, and one actual original coordinate has leverage exceeding `1/4`.

## 5. New near-null hub/star dichotomy in the unpaid collar

Take the coordinate `i` from (4.6). The exact-rank-three scalar-pivot theorem states

`||p_Q||_infinity
 <=128 [c_i |A_ii| |det Lambda|]^(-1/4)`                    (5.1)

whenever `A_ii!=0`.

Hence if

`|A_ii|>=1/64`,

then `c_i>1/4`, `|det Lambda|>=1`, and

`boxed: ||p_Q||_infinity<512.`                               (5.2)

The only still-unpaid small-`d` subbranch may therefore be assumed to satisfy

`c_i>1/4`, `|A_ii|<1/64`.                                   (5.3)

Normalize the spectral row by

`u_i=r_i/sqrt(c_i)`.

Then

`|u_i^T Lambda u_i|
 =|A_ii|/c_i
 <1/16`.                                                     (5.4)

So the surviving physical hub is quantitatively **near null** in spectral Rayleigh quotient.

There is also a dimension-free aggregate star resource. Because `R^TR=I_3`,

`sum_(j!=i) A_ij^2
 =(A^2)_ii-A_ii^2`

`=r_i^T Lambda^2 r_i-A_ii^2`

`=c_i u_i^T Lambda^2 u_i-A_ii^2`.                           (5.5)

Every spectral eigenvalue has modulus at least one, hence `u_i^T Lambda^2 u_i>=1`. Using (5.3),

`sum_(j!=i) A_ij^2
 >1/4-1/4096`

`=1023/4096`.                                                (5.6)

Therefore

`boxed: ||A_(i,[n]\{i})||_2 > sqrt(1023)/64 >0.499.`         (5.7)

This is aggregate-before-inversion: no individual star coefficient is required to be large.

Equivalently, in spectral coordinates relative to the normalized hub direction,

`||(I-u_i u_i^T)Lambda u_i||^2
 =u_i^T Lambda^2u_i-(u_i^T Lambda u_i)^2`

`>255/256`.                                                  (5.8)

The branch is necessarily indefinite: in a definite signature with all spectral eigenvalue moduli at least one, every unit Rayleigh quotient has modulus at least one, contradicting (5.4). Consequently the fleet04 ruled theorem also pays the entire majority-sign output side by (3.4).

Call (4.1)--(5.8) the supporting reduction

`QFORM-SMALL-DISJOINT-MASS-NEARNULL-HUB-STAR-v1`.

It converts the quantitative collar `0<d<1/64` into a real physical near-null hub with a fixed `l2` star resource, unless a scalar pivot already pays the full density.

## 6. The opposite endpoint `d=0` is now completely paid

The completed fleet02/B16 base-packing classification for `d=0` has only three structural cases:

1. at most five nonzero physical rows;
2. one spectral line plus at most three exceptional nonzero rows;
3. an exact spectral coloop.

The first is paid by a physical-triple theorem with bound `<224.529`. The second is paid by finite line-bank compression with bound `<330.869`. The third is now paid by (2.4) with bound `<153`.

Therefore

`boxed: d=0 => ||p_Q||_infinity<331.`                        (6.1)

No continuity conclusion is asserted uniformly across all three `d=0` cases.

## 7. Current exact-rank-three proof map after this run

The Pluecker-disjointness parameter now has both endpoints under quantitative control:

- `d>=1/64`: full density `<=24`, continuous, by fleet04/B16;
- `d=0`: full density `<331`, by base packing plus the newly consumed exact-coloop interpolation;
- `0<d<1/64`: either a physical scalar pivot pays with `<512`, or there is an ORIGINAL physical hub satisfying

  `c_i>1/4`,
  `|u_i^T Lambda u_i|<1/16`,
  `||A_(i,-i)||_2>sqrt(1023)/64`,

  and only the minority-sign/two-sheet side remains unaccounted for by the ruled theorem.

This is strictly narrower than the earlier B10 `single-null-hub mixed-row` description: exact coloop interpolation is no longer a gap, and the nonzero collar now carries a fixed aggregate physical star norm forced directly by the spectral hypothesis and small Pluecker-disjointness.

A compatible newer fleet03/B16 finite-heavy-core compiler independently reduces the same exact-rank-three debt to at most 192 near-null heavy coordinates in a near-line/near-plane Gram geometry. The present reduction supplies a stronger single-row certificate (`c_i>1/4` plus (5.7)) specifically in the small-`d` collar.

## 8. First unpaid implication and proposed successor

The exact current B10 near-null **exact coloop** assignment is source-matched and complete, so duplicating it would violate the owner request. The proposed successor for owner approval is

`QFORM-SMALL-PLUECKER-MASS-NEARNULL-HUB-STAR-PAYMENT-v1`:

> In exact rank three, assume `0<d<1/64`, an original physical row has leverage `c>1/4`, normalized Rayleigh quotient `<1/16`, and aggregate off-diagonal star norm `>sqrt(1023)/64`. Prove a universal minority-sign density bound while retaining arbitrary within-leaf quadratic curvature and the original-coordinate product law.

The next mechanism should aggregate the star before reciprocal local-minor payment and combine it with the remaining transverse quadratic curvature. A receiver-only conditional density cap is not sufficient, and the small physical diagonal is not a perturbative random-error license. The current B09 aggregate-star/cross-bank results and the newest volume/tail-hub alternatives are natural scoped inputs, but no unproved transfer from those results is asserted here.

The full exact-rank-three theorem remains OPEN. Arbitrary additional spectral directions remain a separate debt for the full owner target.

## 9. Continuity status

Continuity is proved on the `d>=1/64` cross-cut Fourier branch. The source-matched exact-coloop cross-transverse theorem supplies essential boundedness but does not claim continuity in its general form. The new small-`d` hub/star reduction is structural and proves no new continuity statement. Therefore unrestricted continuity remains OPEN separately from essential boundedness.

## 10. Deterministic regression check

A finite numerical checker accompanies this report. It verifies on random Parseval frames that

`d=sum_S w_S det(I-G_S)`

to machine precision and checks the leverage consequence whenever the sampled frame happens to lie in the small-`d` collar. This is only a regression check; the proof is the exact Cauchy--Binet derivation above.

## 11. Honest status

**Full QFORM is OPEN / NOT PROVED / NOT DISPROVED.**  
**Exact near-null nonzero coloop interpolation is paid by a source-matching completed theorem and is not duplicated.**  
**New in this run:** the exact disjoint-mass/Gram identity and the quantitative small-`d` near-null hub/star reduction (4.1)--(5.8), plus its splice with the fleet04 full-density and one-sheet estimates.  
**Native brain ingestion:** not verified; execution remains `WITHOUT_VERIFIED_BRAIN`.
