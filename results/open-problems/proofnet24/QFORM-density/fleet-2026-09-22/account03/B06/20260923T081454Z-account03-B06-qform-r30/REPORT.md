SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B06, 2026-09-23T08:14:54Z.
attacking: the near-collinear shared-coefficient double-star survivor; convert small joint wedge either into a paid weighted coefficient-density bound or into a dimension-free same-side star reserve.

# account03/B06 r30 — wedge-or-same-side transfer for the shared double-star packet

**Run:** `20260923T081454Z-account03-B06-qform-r30`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** revision `2026-09-22.15`  
**Assignment:** Curved fiber integration  
**Classification:** `NEW SUPPORTING ANALYTIC/STRUCTURAL DICHOTOMY / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and predecessor

The full owner target remains open: for every dimension, independent ORIGINAL real coordinates with probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal essential bound for the density of `Q=X^TAX`, or give a valid counterexample. No Gaussian, log-concave, moment, compact-support, connected-support, iid, or diagonal-basis assumption is added. Continuity remains a separate desired conclusion.

The immediate predecessor is account03/B06 r29, canonical source

`yspennstate/math-open-problems@5368af077ca929e49b8dc8adeb3e0cefad85f827`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260923T071947Z-account03-B06-qform-r29/REPORT.md`.

In the zero-cross-anchor branch the two complete random linear coefficients are

`W=alpha.Omega+w0`, `Z=beta.Omega+z0`,

with the background coordinates split into two original-coordinate banks and

`alpha=(s,r)`, `beta=(c,t)`.

Here `r` and `c` are the opposite-bank star vectors from r28, while `s,t` are the same-side anchor-to-leaf coefficient vectors. The r28 determinant currency gives

`K:=||r|| ||c|| > sqrt(127/800) G^2`.                              (1.1)

The r29 weighted shared-background theorem proves, whenever `alpha,beta` are linearly independent and `sigma` is the sine of their angle,

`||p_T||_infinity
 <= [2 sqrt(3e)/sqrt(||alpha||||beta||)] sqrt(1+1/sigma)`           (1.2)

for

`T=2XW+2YZ+R(Omega)`,

with arbitrary dependence among `W,Z,R` through the background and arbitrary original cap-one laws. This theorem integrates the true two-dimensional coefficient density before inversion; it does not take a fiber supremum.

The previous run stopped after imposing an arbitrary collar `sigma>=1/4`. The point of the present run is to remove that artificial collar.

## 2. Exact exterior decomposition

Let

`A0=||alpha||`, `B0=||beta||`,
`S=||s||`, `Rr=||r||`, `C=||c||`, `Tt=||t||`.

Choose the sign of `beta` so that the angle `theta` between `alpha` and `beta` lies in `[0,pi/2]`; this does not change any of these norms. Put

`sigma=sin(theta)`.

Because the background coefficient space is the orthogonal direct sum `H_L direct_sum H_R`, the exterior square decomposes orthogonally as

`Lambda^2(H_L direct_sum H_R)
 =Lambda^2 H_L direct_sum (H_L tensor H_R) direct_sum Lambda^2 H_R`.

The mixed component of `alpha wedge beta` is exactly

`s tensor t - c tensor r`.                                        (2.1)

Therefore

`||s tensor t-c tensor r||_F
 <= ||alpha wedge beta||
 = A0 B0 sigma`.                                                   (2.2)

On the other hand, reverse triangle inequality for rank-one tensors gives

`| S Tt - C Rr |
 <= ||s tensor t-c tensor r||_F`.                                  (2.3)

Combining (2.2)-(2.3),

`boxed: |S Tt-K| <= A0 B0 sigma.`                                  (2.4)

This identity is the missing deterministic bridge: small coefficient angle cannot merely make the two random coefficients nearly dependent; unless the weighted theorem already pays, it transfers essentially the whole opposite-bank star currency into the same-side stars.

## 3. Wedge-or-same-side theorem

### Theorem `QFORM-DOUBLESTAR-WEDGE-OR-SAMESIDE-TRANSFER-v1`

Under the r29 hypotheses and notation, with `K=Rr C>0`, exactly one of the following useful alternatives holds.

**A. Wedge-paid branch.** If

`A0 B0 sigma >= K/2`,                                              (3.1)

then `T` has a continuous density and

`boxed: ||p_T||_infinity <= 4 sqrt(3e) / sqrt(K).`                  (3.2)

**B. Same-side-transfer branch.** If

`A0 B0 sigma < K/2`,                                               (3.3)

then

`boxed: S Tt > K/2.`                                               (3.4)

The statement includes the exactly collinear case `sigma=0`: then only branch B is possible, and in fact the stronger identity `S Tt=K` holds.

#### Proof

For branch A, rewrite the predecessor bound (1.2) as

`||p_T||_infinity
 <=2 sqrt(3e) sqrt((1+sigma)/(A0 B0 sigma)).`                        (3.5)

Since `0<sigma<=1`, `1+sigma<=2`; (3.1) yields

`||p_T||_infinity
 <=2 sqrt(3e) sqrt(2/(K/2))
 =4 sqrt(3e)/sqrt(K)`,

which proves (3.2).

For branch B, (2.4) gives

`S Tt >= K-A0B0sigma >K/2`,

proving (3.4). If `sigma=0`, then `alpha wedge beta=0`, hence the mixed component (2.1) is zero and the rank-one tensors satisfy `s tensor t=c tensor r`; taking Frobenius norms gives `S Tt=K`. QED.

The proof aggregates the complete coefficient vectors and their full wedge before paying any reciprocal local coefficient. No largest physical edge or fiber maximum is selected.

## 4. Live B06 constants

Insert the r28 currency (1.1):

`K > kappa G^2`, `kappa=sqrt(127/800)=0.3984344362627307...`.

In branch A,

`||p_T||_infinity
 < [4 sqrt(3e)/sqrt(kappa)] G^(-1)
 =18.0962849488... G^(-1).`                                        (4.1)

Thus the entire small-angle region for which the *unnormalized* wedge `||alpha wedge beta||=A0B0sigma` is at least half the determinant-star currency is paid, with no fixed angular collar.

In branch B,

`boxed: ||s|| ||t||
 > (1/2) sqrt(127/800) G^2
 =0.199217218131365... G^2.`                                        (4.2)

Consequently at least one same-side anchor star has norm

`max(||s||,||t||) > sqrt(0.199217218131365...) G
                  =0.446337... G`.                                 (4.3)

Because each same-side block is symmetric, its operator norm is at least the Euclidean norm of the corresponding anchor row restricted to its own bank. Hence the unpaid branch contains a genuine, dimension-free same-side principal-star spectral resource; it is not merely “near-collinear coefficients.”

The residual vectors are not deleted. Equation (4.2) is only a routing certificate for the next product-preserving hub/star receiver.

## 5. Actual account04 square splice

The exact designated partner `account04/B06` still has no completed current-QFORM canonical artifact visible in the fresh repository search, so no partner theorem is fabricated. The compatible completed account04 result actually available is account04/B18 `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, canonical

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T113729Z-account04-B18-qform-r1/REPORT.md`.

Whenever the paid branch A occurs as a residual `R0` and an untouched original-coordinate pivot gives

`Q_final=R0+a V_(R0)^2`, `a!=0`,

with the theorem's conditional cap-one property, the actual inequality is

`||p_Qfinal||_infinity <=2 sqrt(||p_R0||_infinity/|a|).`             (5.1)

Using (4.1),

`boxed: ||p_Qfinal||_infinity
 <8.507945686 / sqrt(|a| G).`                                       (5.2)

No independence between `R0` and the translated square variable is asserted.

## 6. Correction audit and next exact debt

Consumed live corrections: law-uniform pointwise quadratic-phase decay is false; arbitrary-joint rank-three coarea is false; positive moments of worst conditional projected-density caps are false; post-rotation independence is false; unrestricted fiber suprema lose dimension; one-good-minor and one-triple rank-two extraction can lose dimension; and small nonzero spectral tails may not be discarded.

The new theorem removes the arbitrary angle collar from r29. The zero-cross-anchor shared-background state is now reduced to:

1. a paid continuous-density branch with `||p||_infinity<18.097/G`; or
2. a same-side two-star reserve `||s||||t||>0.199217 G^2` while the entire opposite-star and residual curvature remain present.

The first unpaid implication is therefore

`QFORM-SAMESIDE-TWOSTAR-HUB-RECEIVER-v1`:

> Starting from two original-coordinate anchor stars on opposite physical banks with product `||s||||t||>0.199217 G^2`, while retaining the opposite-bank star vectors, arbitrary same-bank leaf curvature and every ambient coupling, either route quantitatively into the completed mixed-hub Pluecker theorem / physical-pair / ridge / third-volume nodes, or prove a weighted two-hub receiver directly. Do not condition to a worst fiber and do not select one local edge before aggregation.

This is a strictly narrower obstruction than the predecessor's near-collinear coefficient tube.

## 7. Status

`QFORM-DOUBLESTAR-WEDGE-OR-SAMESIDE-TRANSFER-v1`: **PROVED supporting theorem**.  
Full QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.  
Universal continuous-density conclusion: **OPEN**; continuity is proved only on branch A by the predecessor weighted theorem.
