SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B06, 2026-09-23T19:19:38Z.
attacking: the reciprocal rank-one two-hub survivor by integrating the complete two-slope hyperbolic kernel against its original-product joint slope law; no conditional fiber supremum.

# account03/B06 r42 — joint-slope curved integration for the exact-zero two-hub core

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** `2026-09-22.15`; programme revision `2026-09-22.5`  
**Owner continuation:** `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`  
**Assignment:** Curved fiber integration  
**Status:** `NEW PRODUCT-WEIGHTED CURVED RECEIVER / ZERO-CORE R41 BRANCH PAID OR FOUR-STAR / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains OPEN. No Gaussian, log-concave, moment, compact-support, connected-support, iid, finite-rank, sign, or post-rotation-independence assumption is introduced. The new argument keeps the entire environment polynomial and averages its two moving slopes jointly before any singular reciprocal is paid.

## 1. Fresh source-valid inputs

This run continues the literal original-coordinate packet from account03/B06 r41,

`yspennstate/math-open-problems@a867a320432a932e279f704d60b0c833ff4acbd5`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260923T181904Z-account03-B06-qform-r41/REPORT.md`.

Its unpaid small mutual-edge state has a cross block

`N=A[J,K]=[[b,r^T],[c,D]]`,                                      (1.1)

with physical anchors `i in J`, `a in K`, and

`|b|=|A_ia|<1/32`.                                               (1.2)

From the determinant-pair heavy-anchor calculation in r40/r41,

`||N[i,K]||_2^2, ||N[J,a]||_2^2 > M0^2`,                         (1.3)

where

`M0^2 = 226233/33554432`.                                        (1.4)

Consequently

`||r||_2^2, ||c||_2^2 > R2 := M0^2-1/1024
                         =193465/33554432`,                      (1.5)

and therefore

`||r||_2 ||c||_2 > R2 =0.005765706300735474...`.                 (1.6)

The full r41 packet also retains arbitrary same-bank curvature and its nonzero ultra-thin tail. Nothing below deletes them.

A completed designated-partner result is now genuinely available. Account04/B06 r1,

`yspennstate/math-open-problems@f24c8db8946d54f4da2d11898697913af766ad32`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B06/20260923T184145Z-account04-B06-QFORM-r1/REPORT.md`,

proves `QFORM-BANKWISE-TRIPLE-CURVATURE-v1`. Its actual application is recorded in Section 5 below. This replaces the previous B06 runs' honest statement that the designated partner had not yet published a canonical current-QFORM theorem.

The two-dimensional product-projection density cap used below is the standard source-valid projection theorem already used in the current projected-crossing package: if `P` is an orthonormal two-dimensional projection of an original-coordinate product law with one-dimensional density caps one, then

`||p_(PZ)||_infinity <=2`.                                       (1.7)

The current correction ledger was reread: no arbitrary-joint coarea cap, conditional projection-density supremum, pointwise van-der-Corput decay, rotated independence, unrestricted fiber maximum, or one-good-minor principle is used here.

## 2. A weighted two-slope theorem

The first missing implication is analytic rather than matrix-theoretic. A zero physical two-hub core leaves two random affine slopes, and paying either slope by itself creates an unnecessary `1/|slope|` singularity. Joint integration changes that singularity into an integrable two-dimensional kernel.

### Theorem 2.1 — `QFORM-TWO-SLOPE-JOINTCAP-v1`

Let `X,Y` be independent real random variables with probability density caps

`||p_X||_infinity<=L_X`, `||p_Y||_infinity<=L_Y`,                (2.1)

and suppose `(X,Y)` is independent of an arbitrary environment `E`. Let `A(E),B(E),R(E)` be measurable. Assume `(A,B)` has a joint density `h` satisfying

`||h||_infinity<=M`.                                              (2.2)

Then

`Q=R(E)+2A(E)X+2B(E)Y`                                           (2.3)

has a bounded continuous density and

`boxed: ||p_Q||_infinity <=2 sqrt(M L_X L_Y).`                   (2.4)

No assumption whatsoever is made on the law or regularity of `R(E)` or on dependence between `R,A,B`.

#### Proof

Fix an environment value with `A=a`, `B=b`. Except on a null set, `ab!=0` because `(A,B)` has an absolutely continuous law. The two summands `2aX` and `2bY` remain independent, with density caps

`L_X/(2|a|)`, `L_Y/(2|b|)`.                                      (2.5)

Convolution with a probability density cannot increase the `L^infinity` norm, hence the conditional density `q_E` of (2.3) obeys

`||q_E||_infinity
 <= min{L_X/(2|A|), L_Y/(2|B|)}.                                 (2.6)

Put

`U=A/L_X`, `V=B/L_Y`, `H=M L_X L_Y`.                             (2.7)

The joint density of `(U,V)` is bounded by `H`. Since

`min{L_X/|A|,L_Y/|B|}=1/max{|U|,|V|}`,                           (2.8)

we must estimate

`E K(U,V)`, `K(u,v)=1/max{|u|,|v|}`.                             (2.9)

For `t>0`,

`{K>t}={|u|<1/t, |v|<1/t}`                                      (2.10)

has Lebesgue area `4/t^2`. Probability normalization and the density cap therefore give

`P(K>t)<=min{1,4H/t^2}`.                                         (2.11)

Layer cake, with the split point `2sqrt(H)`, yields exactly

`E K
 <= integral_0^infinity min{1,4H/t^2}dt
 =4sqrt(H).`                                                      (2.12)

Averaging (2.6) now proves

`||p_Q||_infinity <=(1/2) E K <=2sqrt(H)`,                       (2.13)

which is (2.4).

For continuity, for almost every environment value the convolution of the two scaled `L^1` densities is a continuous `C_0` function of the output coordinate, translated by `R(E)`. The right side of (2.6) is integrable by (2.12). Dominated convergence therefore passes continuity through the environment average. QED.

This is the desired weighted curved-fiber replacement in its simplest form: the two reciprocal slopes are integrated as one two-dimensional hyperbolic kernel. Taking the larger of two fiber suprema first would lose exactly this compensation.

## 3. Original-product affine slopes

### Corollary 3.1 — `QFORM-ZEROCORE-PRODUCT-SLOPE-WEDGE-v1`

Let `Z` have independent original coordinates with one-dimensional density caps one and be independent of `X,Y`. Let

`A=alpha dot Z+a0`, `B=beta dot Z+b0`,                            (3.1)

where `alpha,beta` are linearly independent. Set

`Delta=||alpha||^2||beta||^2-<alpha,beta>^2
     =||alpha wedge beta||^2`.                                    (3.2)

For arbitrary measurable `R(Z)`,

`Q=R(Z)+2X(alpha dot Z+a0)+2Y(beta dot Z+b0)`                     (3.3)

has a bounded continuous density satisfying

`boxed: ||p_Q||_infinity <=2sqrt(2) Delta^(-1/4).`               (3.4)

#### Proof

Let `G` be the `2x2` Gram matrix of `(alpha,beta)`. The linear map

`Z -> (alpha dot Z,beta dot Z)`                                   (3.5)

is an orthonormal two-dimensional projection followed by an invertible linear map of determinant `sqrt(det G)=sqrt(Delta)`. By (1.7), its joint density is bounded by

`M<=2/sqrt(Delta)`.                                                (3.6)

Translations `a0,b0` do not alter the cap. Apply Theorem 2.1 with `L_X=L_Y=1`. QED.

Notice that `R(Z)` may contain the complete quadratic form on the environment, including arbitrary same-bank terms and every small nonzero spectral tail. It never enters a denominator.

## 4. Apply to the r41 exact-zero hub core

Study first the exact-zero physical two-hub endpoint

`A_ii=A_aa=A_ia=0`.                                               (4.1)

This is a genuine endpoint of the r41 small-edge chamber, not an approximation to the nonzero-core case. With

`J'=J\{i}`, `K'=K\{a}`,                                          (4.2)

write the two complete hub-to-environment coefficient vectors as

`alpha=(s,r) in R^(J') direct_sum R^(K')`,
`beta =(c,t) in R^(J') direct_sum R^(K')`.                        (4.3)

Define

`W:=||alpha wedge beta||=sqrt(Delta)`.                            (4.4)

The mixed `J' x K'` component of the exterior product is exactly

`s tensor t-c tensor r`.                                         (4.5)

Since an orthogonal component cannot exceed the full exterior norm and reverse triangle holds in Hilbert--Schmidt norm,

`W >= ||s tensor t-c tensor r||_F
   >= | ||s|| ||t||-||c|| ||r|| |.`                              (4.6)

Put

`C_R:=||c|| ||r||`.                                               (4.7)

By (1.6), `C_R>R2`. There are now only two branches.

### Branch A: the full slope wedge pays

If

`W >= C_R/2`,                                                     (4.8)

Corollary 3.1 gives

`||p_Q||_infinity
 <=2sqrt(2) W^(-1/2)
 <=4 C_R^(-1/2)
 <4 R2^(-1/2)`                                                    (4.9)

and therefore

`boxed: ||p_Q||_infinity <52.679.`                               (4.10)

The density is continuous. This is a full-ambient bound on the exact-zero-core branch: the environmental quadratic polynomial, same-bank curvature and ultra-thin tail are all retained inside `R(Z)`.

### Branch B: failure forces a four-star packet

If instead

`W<C_R/2`,                                                        (4.11)

then (4.6) gives

`||s|| ||t|| > C_R-W > C_R/2 >R2/2`.                             (4.12)

Thus

`boxed: ||s|| ||t|| >193465/67108864
                      =0.002882853150367737... .`                (4.13)

At the same time the opposite-bank product remains

`||c|| ||r|| >193465/33554432`.                                  (4.14)

Hence failure of the paid joint-slope wedge does not leave a generic rank-one obstruction: **both opposite-bank and same-side star products are quantitatively nonzero.** No individual edge is selected and no star maximum is substituted for the aggregate products.

### Theorem 4.1 — `QFORM-R41-ZEROCORE-WEDGE-OR-FOURSTAR-v1`

Under the r41 simultaneous low-disjointness packet and the exact-zero physical hub core, either

`||p_Q||_infinity<52.679` with a continuous density,              (4.15)

or the complete four-star packet (4.13)--(4.14) holds. Every environmental quadratic term and every nonzero tail direction remains present.

The theorem does **not** replace the live small but nonzero physical hub core by zero. Doing that would be an invalid small-random-error step for unbounded input laws. The nonzero-core continuation is explicitly left to Section 7.

## 5. Designated partner result applied at an actual inequality

Account04/B06 r1 proves the following live bankwise receiver. In its exact-rank-three physical-pair chamber, for an original-coordinate bank `J_b`, let

`G_b=sum_(k in J_b) r_k r_k^T`,                                  (5.1)

where `r_k=(g_1k,g_2k,h_k)`. If `G_b` is invertible, all normalized physical leverages are at most `1/2`, and `D=|det B|`, then

`||p_Q||_infinity <=12[D|lambda| det G_b]^(-1/3)`.              (5.2)

Its actual live packet supplies

`D|lambda|>=1/4`,                                                 (5.3)

`W_b:=sum_(k in J_b)h_k^2>61/1728`.                              (5.4)

On the partner's aggregate-transversality branch

`det G_b>=W_b/64`,                                                (5.5)

insert (5.3)--(5.5) directly into (5.2):

`D|lambda| det G_b
 >61/(4*1728*64)`.                                                 (5.6)

Therefore

`boxed: ||p_Q||_infinity
 <12[61/(4*1728*64)]^(-1/3)
 =232.2732529465... <232.274.`                                    (5.7)

This is the required application of the **designated** account04/B06 result to a concrete inequality. Its branch gives a continuous density. It is a compatible exact-rank-three exit, not a claim that every r41 ultra-thin state satisfies the partner's bankwise Gram gate.

The conceptual match is useful: the partner theorem spends three curvatures by integrating an entire original-coordinate bank through translation-uniform product Fourier volume; Theorem 2.1 spends the two zero-core slopes by integrating their complete original-product joint law. Both mechanisms avoid a curved-fiber maximum.

## 6. Checks

The exact arithmetic checker records

`M0^2=226233/33554432`,
`R2=193465/33554432`,
`R2/2=193465/67108864`,                                          (6.1)

and evaluates

`4/sqrt(R2)=52.67854041413689...`,                               (6.2)

while the designated-partner insertion gives

`232.27325294645095...`.                                         (6.3)

It also verifies the layer-cake identity (2.12) at several exact rational values of `H`. The calculations are sanity checks; Sections 2--5 are symbolic proofs.

## 7. Precise remaining implication

The first B06 debt is now

`QFORM-NEARZERO-TWOHUB-JOINTSLOPE-DYADIC-v1`.

Starting from the same two physical hubs, retain a genuinely nonzero small `2x2` hub core, both robust opposite stars, the four-star alternative (4.13)--(4.14), arbitrary same-bank curvature and the full ultra-thin tail. The goal is to replace the exact-zero conditional convolution in Theorem 2.1 by a curved ellipse/hyperbola estimate integrated jointly over the two original-product slopes, with a bound uniform as the hub core tends to zero. A valid alternative is to route the four-star packet into the completed grouped-crossing or account04/B06 triple-curvature receiver with all leverage/volume gates checked quantitatively.

This is a real additional analytic step: a small quadratic hub core cannot be discarded, and a frozen two-dimensional indefinite kernel has a logarithmic singularity. The new joint-slope averaging suggests a dyadic payment of that logarithm rather than a pointwise core bound.

**Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED. Global continuity remains OPEN.** Continuity is proved in this run only on the exact-zero wedge-paid branch and on the separately scoped account04/B06 partner branch. This run remains `WITHOUT_VERIFIED_BRAIN`: authenticated repository retrieval and writeback occurred, but no authenticated native mathematical-memory receiver use was established.
