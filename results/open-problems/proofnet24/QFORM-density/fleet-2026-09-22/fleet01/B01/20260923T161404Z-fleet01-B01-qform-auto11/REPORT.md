SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B01, 2026-09-23T16:14:04Z.
attacking: the critical two-physical-hub packet, upgrading its nonintegrable t^{-1} Plancherel envelope to an L1 characteristic function by coupling it to one source-disjoint scalar L2 residual, while retaining arbitrary curvature on the hub-slope bank.

# fleet01/B01 — two-hub weighted-frequency gluing with an independent L2 residual

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T161404Z-fleet01-B01-qform-auto11`  
Assignment: Oscillatory replacement  
Classification: **ESSENTIAL_STEP_APPLIED / SUPPORTING THEOREM PROVED / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Continuity: **proved for the scoped theorem below; full-target continuity remains OPEN.**

## 1. Target, correction boundary, and source state

The owner target remains the unrestricted statement: for every dimension, every product law of independent real coordinates with probability densities bounded by one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal bound on the density of `Q=X^T A X`, or give a valid counterexample. No moment, Gaussian, log-concavity, compact-support, connected-support, identical-law, or diagonal-basis assumption is introduced here.

The phase-aligned fragmented-support counterexample to scalar pointwise quadratic decay is preserved. For any prescribed `s>0` and small `delta>0`, choose a finite union of intervals of total length one inside

`{x: dist(s x^2,2 pi Z)<=delta}`.

Its indicator is an admissible probability density and satisfies

`Re E exp(i s X^2)>=cos(delta)`.

Thus no law-uniform pointwise estimate `|E exp(i s X^2)| <= C |s|^{-1/2}` is available. The argument below instead uses a **weighted L2 frequency budget** after a two-dimensional original-coordinate Plancherel step.

Fresh owner control was reread before publication: revision `2026-09-22.15`, QFORM-only, no B01 stop. The live correction inbox was also reread. In particular, this report does not use post-rotation independence, an arbitrary-joint coarea estimate, a worst conditional projection-density cap, a one-good-minor assertion, or small-operator-norm perturbation in law.

## 2. Source-valid inputs actually used

### 2.1 Previous B01 two-hub projected-slope theorem

The previous B01 report

`yspennstate/math-open-problems@acabb94da43b40201ac8633cebad6b817ce679e3`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B01/20260923T040513Z-fleet01-B01-qform-auto11/REPORT.md`

proved the following source-valid linear-image and Plancherel facts. If `B` is a real `2 x m` rank-two matrix and `Y` has independent cap-one coordinates, then for `S=BY+d`,

`||p_S||_infinity <= 2 det(BB^T)^(-1/2)`.                       (2.1)

Consequently

`||p_S||_2 <= sqrt(2) det(BB^T)^(-1/4)`.                         (2.2)

Moreover, even if the same `Y` bank carries an arbitrary measurable phase `R(Y)`, two physical cap-one hub coordinates give the critical pointwise envelope

`|phi(t)| <= pi |t|^(-1) ||p_S||_2`.                              (2.3)

The exponent `-1` is exactly nonintegrable; by itself it yields fractional smoothing, not a bounded density.

### 2.2 Newest designated partner fleet02/B01 r46

The newest completed designated partner at publication refresh is

`yspennstate/math-open-problems@a9cb334579e92753035a96d258fa94cac01cdbfc`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B01/20260923T160109Z-fleet02-B01-qform-r46/REPORT.md`.

For an invertible indefinite ORIGINAL-coordinate physical pair `P`, put

`D_P=|det A[P,P]|`, `kappa_P=sigma_min(A[P,P])`,

and let `W2(P)` be its overlap-two exterior currency. The partner proves the exact identity

`W2(P)=D_P^2 F(A/P)`, `F(S)=sum_(i!=j) S_ij^2`,                  (2.4)

and, at `beta=1/4`, the density estimate

`||p_Q||_infinity <=22.385 D_P^(-1/6) kappa_P^(-1/6) W2(P)^(-1/12)`.  (2.5)

I apply (2.4)-(2.5) to an explicit strict-N3 family in Section 7.

### 2.3 Required newest Claude theorem actually applied

The required Fresnel--Brascamp--Lieb package

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`

contains Theorem H. For two physical hubs and a diagonal leaf block (`r=0` in that theorem), if the augmented hub-slope Gram is `G` with leaf leverage at most `1/2`, it gives

`|phi(t)| <= (2|t|)^(-2)(4pi)^2 det(G)^(-1/2)`.                  (2.6)

In Section 7, on the zero-curvature member of the stress family, `G=k^2 I_2` and every leaf leverage is `1/m`; hence (2.6) gives

`|phi(t)| <= min(1,4 pi^2 k^(-2)|t|^(-2))`,
`||p_Q||_infinity <=4/k`.                                        (2.7)

This source application is important because it prevents misclassifying the diagonal-leaf baseline as new. The theorem proved below instead retains an **arbitrary same-bank phase `R(Y)`**, including dense full-rank quadratic curvature for which paying every leaf-curvature direction through Theorem H has no dimension-free certificate supplied by (2.6).

## 3. A sharp elementary L2 product-density lemma

### Lemma 3.1 (`QFORM-PRODUCT-DENSITY-L2-v1`)

Let `U,V` be independent real variables with probability densities `f,g` satisfying

`||f||_infinity<=M`, `||g||_infinity<=N`.

Then the density `q` of `UV` satisfies

`boxed: ||q||_2^2 <=4 M N.`                                      (3.1)

#### Proof

For almost every `z`,

`q(z)=int f(x) g(z/x) dx/|x|`.

Expanding `||q||_2^2`, integrating first in `z`, and then substituting `x=r x'` gives the exact correlation identity

`||q||_2^2 = int_R K_f(r) K_g(r) dr`,                             (3.2)

where

`K_f(r)=int f(x)f(rx)dx`, `K_g(r)=int g(y)g(ry)dy`.               (3.3)

Since `f,g` have mass one,

`K_f(r)<=M min(1,|r|^(-1))`,
`K_g(r)<=N min(1,|r|^(-1))`.                                     (3.4)

Therefore

`||q||_2^2 <=MN int_R min(1,|r|^(-1))^2 dr =4MN`.                (3.5)

No support or regularity assumption is used. QED.

### Corollary 3.2 — affine hyperbolic edge

For independent cap-one `U,V`, `c!=0`, and arbitrary real `alpha,beta,gamma`, put

`Z=2cUV+alpha U+beta V+gamma`.

Complete the product:

`Z=2c(U+beta/(2c))(V+alpha/(2c)) + gamma-alpha beta/(2c)`.         (3.6)

Translations preserve the density caps and independence. Scaling (3.1) yields

`boxed: ||p_Z||_2 <= sqrt(2)|c|^(-1/2).`                         (3.7)

This is an integrated/collision estimate, not pointwise oscillatory decay.

## 4. Main theorem: a critical two-hub packet plus one independent L2 residual

### Theorem 4.1 (`QFORM-TWO-HUB-INDEPENDENT-L2-RESIDUAL-v1`)

Let the ORIGINAL independent coordinates be split into

- two physical hubs `H=(H_1,H_2)`;
- a disjoint product bank `Y`;
- a disjoint scalar random variable `Z`, independent of `(H,Y)`.

Assume the two hub densities and every coordinate density in `Y` are bounded by one, while `Z` has a density in `L2`. Let

`Q = H^T C H + 2 H^T(BY+d) + R(Y) + Z`,                          (4.1)

where

- `C` is arbitrary symmetric `2 x 2`;
- `B` is an arbitrary real rank-two `2 x m` matrix;
- `d` is arbitrary;
- `R(Y)` is **arbitrary measurable real-valued**, hence may contain arbitrary quadratic, affine, and constant terms on the entire `Y` bank.

Put

`D=det(BB^T)>0`, `P=||p_(BY+d)||_2`, `R_2=||p_Z||_2`.            (4.2)

Then `phi_Q in L1(R)`, so `Q` has a continuous density vanishing at infinity, and

`boxed: ||p_Q||_infinity <=3*2^(-2/3) (P R_2)^(2/3).`            (4.3)

Using (2.2),

`boxed: ||p_Q||_infinity <=3*2^(-1/3) D^(-1/6) R_2^(2/3).`       (4.4)

#### Proof

For each frequency `t`, push the complex measure

`exp(i t R(y)) dP_Y(y)`

through `s=By+d`. Its Radon--Nikodym density `a_t(s)` exists and satisfies

`|a_t(s)|<=p_(BY+d)(s)`, hence `||a_t||_2<=P`.                   (4.5)

For a fixed hub value `h`, the leaf expectation is

`F_t(h)=int exp(2it h^T s) a_t(s) ds = hat a_t(2t h)`             (4.6)

up to the irrelevant Fourier-sign convention. The hub self-phase has modulus one. Since every hub density is bounded by one and has mass one,

`||f_(H_1) f_(H_2)||_2<=1`.                                      (4.7)

Cauchy--Schwarz in the two ORIGINAL hub coordinates, scaling, and two-dimensional Plancherel give

`|phi_(Q-Z)(t)|
 <= [int_R2 |hat a_t(2t h)|^2 dh]^(1/2)
 = pi |t|^(-1)||a_t||_2
 <= pi P |t|^(-1).`                                               (4.8)

Because `Z` is source-disjoint and independent,

`|phi_Q(t)| <= pi P |t|^(-1)|phi_Z(t)|`.                         (4.9)

Combine (4.9) with `|phi_Q(t)|<=1`. For every `T>0`,

`int_R |phi_Q(t)|dt
 <=2T + pi P int_(|t|>T) |phi_Z(t)|/|t| dt`                      (4.10)

and Cauchy--Schwarz in **frequency** gives

`int_(|t|>T) |phi_Z(t)|/|t| dt
 <=(2/T)^(1/2)||phi_Z||_2
 =2 sqrt(pi/T) R_2`,                                              (4.11)

where the last equality is one-dimensional Plancherel. Hence

`int |phi_Q|
 <=2T+2 pi sqrt(pi) P R_2 T^(-1/2).`                             (4.12)

The optimum is

`T=(pi^(3/2) P R_2/2)^(2/3)`.                                   (4.13)

At the optimum the right side of (4.12) is `6T`, so Fourier inversion gives

`||p_Q||_infinity
 <=(2pi)^(-1) 6T
 =3*2^(-2/3)(P R_2)^(2/3)`.                                     (4.14)

Since the proof establishes `phi_Q in L1`, the inverse Fourier transform is a continuous `C_0` density. QED.

### Why this is not the earlier generic L2 packet-gluing lemma

Fleet01/B03 previously proved a useful theorem gluing **two independent packets each already possessing a complete L2 characteristic-function budget**. The present theorem changes the scaling at the critical endpoint: the two-hub packet itself is only known through the weighted `t^{-1}` estimate (4.8), and the independent scalar residual is used only in the high-frequency tail. Consequently `R_2` enters with exponent `2/3`, not linearly. This is quantitatively decisive in the strict-N3 stress family below.

## 5. Hyperbolic-edge corollary with arbitrary same-bank curvature

Take `Z` in Theorem 4.1 to be the source-disjoint affine hyperbolic edge from Corollary 3.2. Then (2.2), (3.7), and (4.3) give

`P R_2 <=2 D^(-1/4)|c|^(-1/2)`.                                 (5.1)

Therefore:

### Corollary 5.1 (`QFORM-TWO-HUB-HYPERBOLIC-EDGE-L1-v1`)

Under the exact original-coordinate decomposition

`Q = H^T C H +2H^T(BY+d)+R(Y)
     +2cUV+alpha U+beta V+gamma`,                                 (5.2)

where the groups `H`, `Y`, `U`, `V` are source-disjoint original product coordinates, `rank(B)=2`, and `c!=0`, one has

`boxed: ||p_Q||_infinity <=3 D^(-1/6)|c|^(-1/3).`                (5.3)

The density is continuous and vanishes at infinity.

The scaling is exact: under `A -> sA`, `D -> s^4D` and `c->sc`, so the right side scales as `s^(-1)`.

This theorem permits completely arbitrary hub curvature `C`, completely arbitrary same-bank leaf curvature hidden in `R(Y)`, arbitrary translations, and arbitrary affine terms generated by conditioning outside original coordinates. What it does **not** permit is hidden coupling between the source-disjoint hyperbolic edge `(U,V)` and the active `(H,Y)` packet; such coupling would destroy the factorization in (4.9).

## 6. Strict-N3 family paid uniformly despite a vanishing hyperbolic edge

Let `k>=2`, let `m` be large, and let the leaf bank be the disjoint union of two `m`-coordinate banks. Let `e_1,e_2` be the normalized all-ones vectors on the two banks and define

`B_(k,m) = [ k e_1^T ; k e_2^T ]`.                               (6.1)

Thus

`B_(k,m) B_(k,m)^T = k^2 I_2`, `D=k^4`.                          (6.2)

Add source-disjoint cap-one physical coordinates `U,V` with hyperbolic coefficient

`c=k^(-2)`.                                                       (6.3)

Allow **any** leaf phase `R(Y)` in the theorem. A concrete dense stress choice is

`R(Y)=Y^T C_m Y`,                                                  (6.4)

where `N=2m` admits a symmetric orthogonal Hadamard matrix `S_N`, and

`C_m=N^(-1/2) S_N`.                                               (6.5)

Then `||C_m||op=N^(-1/2)`, every physical entry is of order `N^(-1)`, and `||C_m||_F=1`; it is nevertheless full rank, and no step discards it as a small random perturbation.

The quadratic matrix without `C_m` has nonzero spectrum

`{+k,+k,-k,-k,+k^(-2),-k^(-2)}`.                                (6.6)

Adding `C_m` only on the leaf block perturbs eigenvalues by at most `N^(-1/2)`, so for `k>=2` and large `m` at least four eigenvalues still have modulus greater than one.

Every diagonal tends to zero. The largest hub-leaf physical pair determinant is `k^2/m`, the `U,V` determinant is `k^(-4)`, and the leaf-leaf principal pair determinants are `O(N^(-2))`. Therefore, for every fixed no-pivot threshold `tau>0`, first choose `k` with `k^(-4)<tau`, then choose `m >> k^2/tau`. The family lies in the strict-N3 regime while retaining four target-scale spectral directions.

Corollary 5.1 gives, for **every** admissible product input law,

`||p_Q||_infinity
 <=3 (k^4)^(-1/6)(k^(-2))^(-1/3)
 =3.`                                                             (6.7)

The bound is independent of `k,m` and of the entire dense leaf phase `C_m`. The density is continuous.

This is precisely the weighted-frequency phenomenon: the two-hub packet alone is critical (`t^-1`), and the independent hyperbolic edge becomes physically tiny (`c=k^-2`), but its L2 collision budget supplies exactly the missing half power after frequency averaging.

## 7. Actual partner r46 application to the same strict-N3 family

Use the physical pair `P={U,V}`. Its matrix is

`[[0,k^(-2)],[k^(-2),0]]`,

so

`D_P=k^(-4)`, `kappa_P=k^(-2)`.                                  (7.1)

Because this pair is source-disjoint from the remaining packet, its exact Schur complement is simply the `H-Y` block with leaf curvature `C_m`. Its off-diagonal energy is

`F(A/P)=4k^2 + F(C_m)`.                                           (7.2)

For the normalized-Hadamard choice (6.5),

`||C_m||_F^2=1`, `sum_i (C_m)_(ii)^2=1/N`,

hence

`F(C_m)=1-1/N`.                                                    (7.3)

The partner's exact identity (2.4) therefore gives

`boxed: W2(P)=k^(-8)(4k^2+1-1/N).`                               (7.4)

Applying the completed partner inequality (2.5) at this actual pair yields

`||p_Q||_infinity
 <=22.385 k^(5/3)(4k^2+1-1/N)^(-1/12).`                          (7.5)

In particular this certificate has asymptotic scale

`22.385*4^(-1/12) k^(3/2)
 =19.943... k^(3/2)`.                                             (7.6)

Thus the partner theorem is valid on this exact family but deteriorates as the physical hyperbolic pair becomes tiny. The new weighted-frequency compiler gives the complementary uniform estimate `3` and continuity. This is an equation-level application of the designated partner, not a bibliography-only citation.

## 8. Required Claude Theorem H comparison and the exact new scope

Set `C_m=0` in the same family. Then the newest Claude Theorem H applies with two hubs, `r=0`, Gram `G=k^2 I_2`, and every leaf leverage `1/m`. Its exact bound is

`|phi(t)|<=min(1,4pi^2 k^(-2)|t|^(-2))`,
`||p_Q||_infinity<=4/k`.                                         (8.1)

So the zero-curvature baseline was already paid and is not claimed as new progress.

What changes in this run is that (5.3) remains **unchanged when an arbitrary nonseparable quadratic form is inserted on the same `Y` bank**. The full-rank `C_m` in (6.5) is a concrete stress test. Treating it through a rank decomposition in Theorem H introduces all of its tiny curvature directions; treating it as a small random quadratic perturbation is forbidden for unbounded product inputs. The complex-pushforward step (4.5) absorbs `R(Y)` exactly at modulus one instead.

The older fleet01/B03 generic L2-packet glue also does not have the same scaling. Applied to a hyperbolic edge of size `k^-2` and a rank-two cross block with singular product `k^2`, its product of L2 budgets grows like `k^(1/2)`. The weighted `t^-1`/tail interpolation in Theorem 4.1 changes this to the constant `3` in (6.7).

## 9. What is now paid and what remains

**Paid in this run.** A critical two-physical-hub projected-slope packet with completely arbitrary same-bank curvature acquires an integrable characteristic function whenever one source-disjoint scalar residual has an L2 density. For a source-disjoint physical hyperbolic edge this gives the explicit continuous-density bound

`3 det(BB^T)^(-1/6)|c|^(-1/3)`.

The theorem pays strict-N3 families in which the two hub singular directions grow while the independent hyperbolic edge shrinks at the reciprocal product scale.

**Not paid.** The bare three-large-eigenvalue hypothesis does not force a source-disjoint hyperbolic edge after extracting a two-hub packet. In the genuine `<=2 by <=2` heavy-volume survivor, arbitrary cross-couplings may entangle the would-be residual edge with the hub/leaf bank, so the exact factorization (4.9) can fail.

The first unpaid implication is therefore

`QFORM-N3-CRITICAL-TWOHUB-L2-RESIDUAL-ROUTING-v1`:

> From the remaining no-pivot / at-most-two-heavy-per-side structural class, either produce a two-hub rank-two slope packet together with a source-disjoint scalar residual whose density has a quantitative L2 budget satisfying the scale balance in (4.3), or route the entangled residual to an already-paid pair-Schur, mixed-hub, volume, grouped-square, ridge, or null-coloop receiver **before** taking a reciprocal tiny physical minor.

A natural next analytic extension is to replace source-disjoint independence in (4.9) by a conditional `L2(dt)` estimate for an **entangled** scalar residual while preserving original-coordinate product provenance. The correction `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` rules out replacing this with a generic conditional-density cap.

The unrestricted QFORM conjecture therefore remains OPEN, and no full-target continuity claim or end-to-end review is made.

## 10. Integrity / scope checklist

- No law-uniform scalar quadratic pointwise decay is used.
- No spectral rotation is declared independent.
- No moments, compact support, connected support, log-concavity, Gaussianity, or identical laws are assumed.
- The dense leaf curvature is retained exactly inside the complex pushforward; it is not treated perturbatively.
- The source-disjoint residual requirement is explicit and is the remaining structural restriction.
- The partner fleet02/B01 r46 is applied at an actual physical pair and actual `W2` identity.
- The required newest Claude Theorem H is applied to the zero-curvature baseline and used to isolate the genuinely new arbitrary-curvature scope.
- The phase-aligned fragmented-support counterexample remains valid and is not weakened.
- Full conjecture: **OPEN**.
