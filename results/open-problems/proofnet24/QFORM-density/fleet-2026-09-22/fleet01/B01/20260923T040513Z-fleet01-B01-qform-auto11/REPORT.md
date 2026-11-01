# Three-hub projected-slope smoothing: an unconditional `t^{-3/2}` packet

Run: `20260923T040513Z-fleet01-B01-qform-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: `fleet01/B01` — oscillatory replacement  
Status: **ESSENTIAL_STEP_APPLIED / SUPPORTING THEOREM PROVED / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B01, 2026-09-23T04:05:13Z.  
attacking: spectral-to-pivot-E2 structural bridge via integrated determinant identities and a pivot-free oscillatory alternative.

## 1. Exact target and source corrections

The owner target remains: for every dimension, every collection of independent real random variables whose one-dimensional densities are bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal finite bound on the density of `Q=X^T A X`, or give a counterexample. Continuity is an additional requested conclusion and is recorded separately.

The full target is still **OPEN**. This report does not assume moments, centering, compact or connected support, log-concavity, Gaussianity, or independence after a spectral rotation.

The phase-aligned counterexample to scalar pointwise van der Corput decay is retained. For any prescribed frequency `s>0` and small `delta>0`, the set

`{x : dist(s x^2, 2 pi Z) <= delta}`

has infinite Lebesgue measure. Choose a finite union of intervals inside it with total length one and take its indicator as a probability density. Then

`Re E exp(i s X^2) >= cos(delta)`.

Hence no law-uniform bound `|E exp(i s X^2)| <= C |s|^{-1/2}` can hold over all cap-one densities. The result below instead creates decay from a *multidimensional random linear slope*, then integrates that decay in frequency.


## 2. Source theorem used: density of a full-rank linear image

I use the product-marginal theorem in exactly the source-valid scope recorded in

`yspennstate/math-open-problems@f643a9fa13dd0d3bc084de86e1791e11a6bf348b`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B18/20260922T115514Z-qform-B18-a01/REPORT.md`.

For a rank-`k` real matrix `T` and independent cap-one coordinates `Y_j`,

`||p_{TY}||_infinity <= 2^(k/2) / sqrt(det(T T^T)).`                (2.1)

The cited source is Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, Theorem 1.1, transferred there from orthogonal projections to arbitrary full-rank linear images. If the domain dimension equals `k`, the elementary change-of-variables bound is at least as strong, so (2.1) remains valid.

## 3. Main theorem: arbitrary self phases, `k` physical hubs

### Theorem 3.1 (projected-slope `L^2` compiler)

Let the ORIGINAL coordinates be split into a hub set `H` of size `k` and its complement `K`. Write `U=X_H in R^k`, `Y=X_K`, and suppose

`Q = U^T C U + 2 U^T(MY+c) + R(Y)`,                              (3.1)

where

- `C` is an arbitrary real symmetric `k x k` matrix;
- `M` is a real `k x |K|` matrix of rank `k`;
- `c in R^k` is arbitrary;
- `R` is any measurable real function of `Y` (in particular it may contain every quadratic, affine and constant term on the leaf coordinates);
- all physical coordinates of `(U,Y)` are mutually independent and have densities at most one.

Put

`D = det(M M^T) > 0.`                                               (3.2)

Then for every nonzero `t`,

`|phi_Q(t)| <= min{1, 2^(k/4) pi^(k/2) D^(-1/4) |t|^(-k/2)}.`      (3.3)

Consequently, for every `k>=3`, `phi_Q` is integrable and `Q` has a continuous density vanishing at infinity with

`boxed: ||p_Q||_infinity <= sqrt(2) * k/(k-2) * D^(-1/(2k)).`        (3.4)

In particular, for three physical hubs,

`boxed: ||p_Q||_infinity <= 3 sqrt(2) D^(-1/6).`                    (3.5)

No leverage condition is imposed on either side of `M`, and no quadratic block besides the rank condition on the actual hub-to-leaf slope matrix is restricted.

### Proof

Let `S=MY+c`. By (2.1), `S` has a density `p_S` satisfying

`||p_S||_infinity <= 2^(k/2) D^(-1/2).`                            (3.6)

For each fixed `t`, push the complex measure

`exp(i t R(y)) prod_(j in K) f_j(y_j) dy`

forward by `y -> My+c`. Since its total variation is dominated by the ordinary law of `S`, its Radon--Nikodym density `g_t` satisfies

`|g_t(s)| <= p_S(s)` almost everywhere.                             (3.7)

Therefore

`||g_t||_2^2 <= ||p_S||_infinity int p_S = ||p_S||_infinity`,

so

`||g_t||_2 <= 2^(k/4) D^(-1/4).`                                   (3.8)

Now define

`h_t(u)=exp(i t u^T C u) prod_(i in H) f_i(u_i)`

(the harmless fixed linear term coming from `c` can equivalently be left inside the transform). Because every `0<=f_i<=1` and has mass one,

`||h_t||_2^2 = prod_(i in H) int f_i(x)^2 dx <=1.`                  (3.9)

With Fourier convention `hat g(xi)=int exp(i <xi,s>)g(s) ds`, (3.1) gives

`phi_Q(t)=int_(R^k) h_t(u) hat g_t(2t u) du`                        (3.10)

up to an irrelevant unimodular fixed phase. Cauchy--Schwarz, scaling and Plancherel yield

`|phi_Q(t)|
 <= ||h_t||_2 [int |hat g_t(2t u)|^2 du]^(1/2)
 = (2|t|)^(-k/2) ||hat g_t||_2
 = (2|t|)^(-k/2) (2pi)^(k/2) ||g_t||_2
 <= 2^(k/4) pi^(k/2) D^(-1/4)|t|^(-k/2).`                         (3.11)

Together with `|phi_Q|<=1`, this proves (3.3).

Set

`B=2^(k/4) pi^(k/2)D^(-1/4)`, `a=k/2>1`.

The exact crossover is `T=B^(1/a)=B^(2/k)`, and

`int_R min(1,B|t|^(-a)) dt
 = 2 T a/(a-1)
 = 2 B^(2/k) k/(k-2).`                                             (3.12)

Fourier inversion then gives

`||p_Q||_infinity
 <= (1/(2pi)) int |phi_Q|
 <= [k/(pi(k-2))] B^(2/k)
 = sqrt(2) k/(k-2) D^(-1/(2k)).`                                   (3.13)

Since `phi_Q in L^1`, the inverse Fourier transform is a continuous density tending to zero at infinity. QED.

## 4. Exact match with the designated partner at the critical two-hub endpoint

The latest completed designated partner result is fleet02/B01 r35:

`yspennstate/math-open-problems@0bc769a70ba86df2c5bc5b73b5e5bbfe6021cfd8`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B01/20260923T030247Z-fleet02-B01-qform-r35/REPORT.md`.

For two physical hubs and an arbitrary leaf remainder it proves

`H_(1/2)(Q):=sup_s E|Q-s|^(-1/2) <= 2^(11/4) D^(-1/8),`           (4.1)

and its pointwise intermediate estimate is

`|phi_Q(t)| <= min{1, pi sqrt(2) D^(-1/4)|t|^(-1)}.`               (4.2)

Theorem 3.1 at `k=2` reproduces (4.2) **exactly**:

`2^(k/4)pi^(k/2)D^(-1/4)=sqrt(2)pi D^(-1/4).`

Thus the present result is not a new scalar Fresnel claim; it is the same partner-proved projected-slope/Plancherel mechanism one dimension higher. The critical distinction is that `k=2` gives the nonintegrable exponent `|t|^-1` and therefore only a fractional-potential conclusion, whereas `k=3` gives `|t|^-3/2`, which is integrable and directly produces a continuous bounded density.

### Actual partner inequality on a target-valid family

Let `m>=1`. Take three hub coordinates and split `3m` leaf coordinates into three disjoint `m`-element banks. Let `e_1,e_2,e_3` be the normalized all-ones vectors on the three banks and let `M_m` have rows `e_1^T,e_2^T,e_3^T`. Define

`A_m = [[0, M_m],[M_m^T,0]].`                                      (4.3)

Then

`M_m M_m^T=I_3`,                                                   (4.4)

and the nonzero spectrum of `A_m` is exactly

`{1,1,1,-1,-1,-1}.`                                                (4.5)

Every nonzero physical hub-leaf coefficient has magnitude `m^(-1/2)`, and every nonzero physical `3x3` cross minor has magnitude `m^(-3/2)`; no single such minor remains macroscopically large.

Apply the partner r35 theorem to hubs 1 and 2, treating hub 3 and every leaf as part of its arbitrary remainder. The corresponding two-row slope Gram is `I_2`, hence the partner gives the actual uniform inequality

`boxed: H_(1/2)(X^T A_m X) <= 2^(11/4)`                            (4.6)

for every admissible cap-one product law and every `m`.

Applying the new three-hub theorem to all three hub rows gives the stronger target-level conclusion

`boxed: ||p_(X^T A_m X)||_infinity <= 3 sqrt(2),`                   (4.7)

and the density is continuous. Thus the partner's two-hub fractional smoothing and the present three-hub `L^1` smoothing fit together without selecting any of the `m^-3/2` physical minors.

## 5. Exact aggregate-minor identity

For a fixed physical hub triple `H` and `K=H^c`, let

`M_H=A[H,K]`.

Cauchy--Binet gives the exact identity

`boxed:
 det(M_H M_H^T)
 = sum_(T subset K, |T|=3) det(A[H,T])^2.`                          (5.1)

Therefore (3.5) can be rewritten as

`||p_Q||_infinity
 <= 3 sqrt(2)
    [sum_(T subset H^c, |T|=3) det(A[H,T])^2]^(-1/6).`             (5.2)

This is the structural point of the run: the proof spends the **entire disjoint three-minor star of a physical triple before paying any reciprocal individual minor**.

For the family (4.3), exactly `m^3` cross minors are nonzero, each has squared determinant `m^-3`, and (5.1) sums them to one. Thus (5.2) stays dimension free while every one-minor certificate diverges.

Summing (5.1) over hub triples gives the global disjoint-three-minor energy

`sum_(|H|=3) det(A[H,H^c]A[H^c,H])
 = sum_(|H|=|T|=3, H cap T=empty) det(A[H,T])^2.`                   (5.3)

Separately, the full exterior-power identity is

`e_3(A^2)=sum_(|H|=|T|=3) det(A[H,T])^2.`                          (5.4)

The bare target hypothesis implies `e_3(A^2)>=1`, but (5.4) includes overlap classes `|H cap T|=0,1,2,3`; it does **not** force a single hub triple in (5.1) to have dimension-free mass. This is the remaining structural issue, not an analytic gap in Theorem 3.1.

## 6. Relation to the newest all-cross-minor compiler

During this run, fleet03/B02 supplied a stronger balanced cross-minor aggregation (`QFORM-BALANCED-CROSSMINOR-ENTROPY-L1-v1`) on `math-open-problems` commit `c24c63bd01e1f3c46fb85cd700c180b4e59ffe01`. It controls an arbitrary original-coordinate cross block when a probability law on its nonzero `3x3` minors has row marginals at most `1/2`, using the entire three-volume and an entropy penalty.

The present theorem is complementary: it has **no row-marginal/leverage gate at all**, but it requires the three hub variables to be an actual fixed physical triple. Thus it is a clean endpoint compiler for a concentrated three-row packet. It does not replace the balanced theorem in the diffuse multi-row regime, and the balanced theorem does not make (3.5) unnecessary in a fixed-hub analysis.

A useful immediate corollary is: if a cross block has total three-volume `W_3` and one physical row triple `H` carries a fraction `theta` of that volume, then

`det(A[H,J]A[J,H]) >= theta W_3`

for the corresponding leaf side, and therefore

`||p_Q||_infinity <= 3 sqrt(2) (theta W_3)^(-1/6)`                 (6.1)

whenever the coordinates outside `H` include that leaf side and all remaining terms are absorbed into `R`. This pays a genuine three-row atom before any tiny minor is selected.

## 7. What this does and does not solve

**Proved in this run.** A rank-three actual physical slope packet gives a uniform `t^-3/2` characteristic-function envelope, a universal continuous density bound `3 sqrt(2)D^-1/6`, and an aggregate Cauchy--Binet formulation that pays a whole three-minor star.

**Not proved.** The target's three-large-eigenvalue assumption does not by itself yield one physical hub triple with `det(A[H,H^c]A[H^c,H])` bounded below. Diagonal/block-bank examples can place the spectral resource in the overlap classes of (5.4), and previous fleet corrections forbid replacing this with a one-good-minor claim.

The first unpaid implication is therefore

`QFORM-EXTERIOR3-OVERLAP-ROUTING-v1`:

Starting from

`e_3(A^2)>=1`,

split the exact exterior-three energy by intersection size `r=|H cap T|`. Route the disjoint part (`r=0`) to either the balanced all-cross-minor compiler or the fixed-three-hub theorem above; route `r=1` through a physical scalar Schur pivot plus aggregate pair-volume; route `r=2` through a two-hub/pair packet; and route `r=3` through a physical principal-three/localized mechanism, **without selecting a vanishing individual minor and without taking a worst conditional rotated fiber**. The determinant identities for the overlap classes should be used before any reciprocal payment.

This is a sharper structural target than the previous generic `spectral-to-pivot-E2` label, but the full routing is not proved here. Hence the full QFORM conjecture remains **OPEN**, and no full-proof status is claimed.

## 8. Privacy / operational note

Only mathematical source files and the current authorized QFORM controls were read. No unrelated data, credentials, account secrets, public-release action, paid model/API call, remote workflow, email, notification mutation, schedule mutation or cross-account authentication was used. Repository use is file transport only and is not labelled as native brain ingestion.
