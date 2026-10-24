SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B04, 2026-09-23T21:51:55Z.
attacking: optimize the marginal-free E3 product-Fourier threshold and spend the completed account04/B04 nested-anchor packet through the sharper incident-volume receiver.

# account03/B04 r42 — optimal E3 threshold and sharp nested-anchor incident payment

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement  
Status: `NEW CONSTANT OPTIMIZATION / DESIGNATED-PARTNER RESULT APPLIED / EXPLICIT ROTATED-INDEFINITE ESTIMATE / FULL TARGET OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Continuity: proved on every branch below (`C_0`); full-target continuity remains OPEN.

The unrestricted conjecture is **not** proved here. All random variables stay in original product coordinates. No post-rotation independence, pointwise law-uniform quadratic-phase decay, moment assumption, compact-support assumption, arbitrary-joint coarea lemma, or naive fiber-supremum bound is used.

## 1. Fresh sources

Fresh owner control was read from `yspennstate/math-research-brain` main at `02e18dfc3abd04de1d6165de11d114d2ea48015b`; OWNER CONTROL remains revision `2026-09-22.15`. The live correction inbox blob is `47b2ff15d8ca6acfe35d9fd3de3b6281a86439f3`.

The two analytic inputs refined here are:

1. account03/B04 r39, `QFORM-CROSS-E3-SHARP-ENTROPY-MARGINALFREE-v1`, full report at
   `yspennstate/math-open-problems@04f0b30d5f729ed26d9f8c2cb1354973c587c3cc:proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/20260923T185112Z-account03-B04-auto11-r39/REPORT.md`;
2. the completed designated-partner result account04/B04 r1, `QFORM-NESTED-ANCHOR-D3-MARGINALFREE-PAYMENT-v1`, full report at
   `yspennstate/math-open-problems@3224f273e92d97a8bff7424e9b1191c1e49d0611:proofnet24/QFORM-density/fleet-2026-09-22/account04/B04/20260923T214340Z-account04-B04-QFORM-r1/REPORT.md`.

The checked grouped projected-crossing source underlying r39 is
`yspennstate/math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a:proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

## 2. Exact minimax optimization of the marginal-free E3 compiler

Let `M` be any literal original-coordinate cross block with

`Z=E_3(M)>0`.

The r39 proof has two exhaustive branches, parametrized by `h in [1/2,3/4)`.

* Diffuse third-volume marginals (`max_i gamma_i<=h`):

`||p_Q||_infinity <= D(h) Z^(-1/6)`,

where

`D(h)=3e/[sqrt(2h)(3-4h)]`.                                      (2.1)

* A heavy physical row (`gamma_i>h`): the incident-third-volume receiver gives

`||p_Q||_infinity < H(h) Z^(-1/6)`,

where

`H(h)=3*2^(4/3) h^(-1/6)`.                                      (2.2)

The previous run selected the convenient rational `h=131/256`, giving coefficient `8.45736769648...`. The best constant obtainable from these two already-proved branches is slightly smaller and can be written exactly.

### Theorem 2.1 — `QFORM-CROSS-E3-OPTIMAL-THRESHOLD-v1`

There is a unique `h_* in (1/2,3/4)` satisfying

`e = 2^(11/6) h_*^(1/3) (3-4h_*)`.                              (2.3)

Equivalently, with `u_*=h_*^(1/3)`,

`4u_*^4-3u_*+e/2^(11/6)=0`.                                     (2.4)

Define

`C_* = 3e/[sqrt(2h_*)(3-4h_*)]
      = 3*2^(4/3) h_*^(-1/6)`.                                  (2.5)

Then every such cross block satisfies

`boxed:
 ||p_Q||_infinity <= C_* E_3(M)^(-1/6),`                         (2.6)

and the characteristic function is in `L^1`, so the density is continuous and vanishes at infinity. Numerically,

`h_* = 0.511559008194236206492964132867...`,

`C_* = 8.45302122552817687470491804598...`.                      (2.7)

Moreover `C_*` is the exact minimum of `max(D(h),H(h))` over `h in [1/2,3/4)`.

#### Proof

On `[1/2,3/4)`, `H(h)` is strictly decreasing. The denominator of `D(h)` is

`g(h)=sqrt(2h)(3-4h)`.

Its logarithmic derivative is

`g'(h)/g(h)=1/(2h)-4/(3-4h)=(3-12h)/[2h(3-4h)]<0`,              (2.8)

so `D(h)` is strictly increasing on this interval. At `h=1/2`,

`D(1/2)=3e < 3*2^(3/2)=H(1/2)`,                                 (2.9)

whereas `D(h)->infinity` as `h->3/4`. Hence the maximum of the two monotone branch constants is minimized at their unique intersection. Equating (2.1) and (2.2) gives (2.3). Substituting the intersection into the exhaustive r39 dichotomy proves (2.6). The same `L^1` Fourier envelopes used in r39 are unchanged, hence continuity and `C_0` follow. QED.

This is an optimization of the existing proof architecture, not a claim that `C_*` is the sharp constant for all fixed-cross-block arguments.

## 3. Designated-partner application: the nested anchor pays at <602.012

The newly completed account04/B04 result supplies a literal physical cross block `M=A[I,J]`, a physical row `i`, a physical column `j`, and a separated anchored third-minor mass

`J_3^sep(i,j)
 = sum det M[{i,r_1,r_2},{j,c_1,c_2}]^2
 > delta`,                                                       (3.1)

with

`delta = 47045881/(12*10^18)
       = 3.920490083333333333...*10^(-12)`.                      (3.2)

Every summand in (3.1) is a physical `3x3` minor whose row set contains the same row `i`. Let

`J_i = sum_{R contains i, |R|=3, |T|=3} det M[R,T]^2`            (3.3)

be the full incident third-volume currency of row `i`. Positivity of squared minors gives the **actual inequality**

`boxed: J_i >= J_3^sep(i,j) > delta.`                            (3.4)

The incident receiver proved in r39 is

`||p_Q||_infinity <= 3*2^(4/3) J_i^(-1/6)`.                    (3.5)

It retains arbitrary same-bank quadratic terms, affine terms created by outside conditioning, and every extra crossing coefficient. Apply (3.4) directly in (3.5):

`boxed:
 ||p_Q||_infinity
 < 3*2^(4/3) delta^(-1/6)
 = 602.0111324191178360573... <602.012.`                         (3.6)

The characteristic function is `L^1`, so this branch has a continuous `C_0` density.

This is the requested equation-level use of the completed designated partner `account04/B04`. It improves that partner's own valid marginal-free third-compound payment

`868.250297051749...`                                           (3.7)

by about `30.66%`. Even the globally optimized Theorem 2.1 would give the intermediate bound

`C_* delta^(-1/6)=673.1655766271576597...`,                      (3.8)

but the fixed physical row in the partner packet allows the stronger incident receiver (3.6).

The same argument can be run after transposing the cross block because every separated minor also contains the fixed physical column `j`; no symmetry assumption on `M` is needed.

## 4. A fully dense genuinely rotated indefinite example

Let

`H = [[ 1, 1, 1, 1],
      [ 1,-1, 1,-1],
      [ 1, 1,-1,-1],
      [ 1,-1,-1, 1]]`,                                          (4.1)

so `H H^T = 4 I_4`. Let `J_4` be the all-ones `4x4` matrix and define the symmetric `8x8` matrix

`A_* = [[J_4/8, H],
        [H^T,   J_4/8]].`                                        (4.2)

Every entry of `A_*` is nonzero, and the cross block is dense. The unperturbed matrix

`A_0=[[0,H],[H^T,0]]`

has spectrum `{+2 (x4), -2 (x4)}` because all singular values of `H` are `2`. The same-bank perturbation `diag(J_4/8,J_4/8)` has operator norm `1/2`. Weyl's inequality therefore gives four eigenvalues of `A_*` at least `3/2` and four at most `-3/2`. Thus `A_*` satisfies the owner's spectral hypothesis very strongly while remaining non-diagonal in the independent coordinates.

Every `3x3` minor of `H` has determinant `+/-4`, hence squared determinant `16`. For a fixed physical row there are `C(3,2)*C(4,3)=12` such minors, so

`J_i=12*16=192`.                                                 (4.3)

The incident theorem therefore gives, for **every** independent cap-one input law,

`boxed:
 ||p_{X^T A_* X}||_infinity
 <= 3*2^(4/3) * 192^(-1/6)
 = 2^(1/3) 3^(5/6)
 = 3.1473451902649445566... .`                                  (4.4)

The density is continuous and vanishes at infinity. This estimate is product-coordinate native: the Hadamard structure is a coefficient matrix, not a rotation applied to the random variables.

For comparison, `E_3(H)=16*16=256`, so Theorem 2.1 alone would give `3.3545836964...`; the incident row structure improves it to (4.4).

## 5. What this does and does not close

The full conjecture remains OPEN. The new result pays the live account04/B04 nested-anchor branch more sharply, but the bare three-large-eigenvalue hypothesis still does not force a target-scale cross `E_3` or incident `J_i` on an arbitrary physical cut. Low-cross-rank, high-leverage and zero/near-zero-pivot geometries therefore remain genuine survivors.

The next B04 implication is:

`QFORM-HEAVY-CARRIER-INCIDENT-OR-ZEROPIVOT-v1` — on the remaining rank-five heavy-carrier branch from the current proof graph, prove either a target-scale incident third-volume packet `J_i>=c` (then (3.5) pays it) or a bounded physical zero/near-zero-pivot configuration that can be routed to the completed linear-square / pair-star receivers, without taking a reciprocal of a vanishing local minor.

No scheduler state, task identity, email, notification, public-release, paid-API or cross-account authentication state is changed by this report.
