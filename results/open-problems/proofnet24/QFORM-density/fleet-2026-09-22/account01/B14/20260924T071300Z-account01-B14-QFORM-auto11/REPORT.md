SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B14, 2026-09-24T07:13:00Z.
attacking: determinant/cap-normalized whole-bank localization — keep three disjoint original-coordinate banks aggregated before any active fragment normalization, then spend their final one-dimensional density caps against the completed account02/B14 hyperbolic determinant compiler.

# account01/B14 — cap-normalized whole-bank localization and a diffuse three-bank target chamber

Programme: `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`.  
Owner control: `2026-09-22.15`.  
Assignment: translations and localization.  
Status: supporting theorem proved; full unrestricted QFORM remains OPEN; full continuity remains OPEN.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and dependencies

The target remains: independent original-coordinate variables with probability densities bounded by one, and an arbitrary real symmetric matrix having at least three eigenvalues of modulus at least one. No moments, bounded support, connected support, finite fragment count, centering, log-concavity or independence after rotation is assumed.

The live corrections remain in force: law-uniform pointwise quadratic Fourier decay is false; bounded-diameter/fixed-fragment localization is false; arbitrary-joint coarea and positive conditional projection moments are false proof interfaces; a spectral rotation does not preserve independence.

The newest completed designated-partner result consumed is account02/B14, run `20260924T065901Z-account02-B14-QFORM-auto11`, canonical mathematics

`yspennstate/math-open-problems@a785db1a405eec1874fc553b28b8178f32d416d0`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260924T065901Z-account02-B14-QFORM-auto11/REPORT.md`.

Its cap-weighted active-mixture theorem implies, in particular, that for three independent scalar variables with density caps `k_1,k_2,k_3`, an invertible symmetric `3 x 3` quadratic block `B`, and arbitrary deterministic or independently conditioned affine terms,

`||p_Q||_infinity <= 6 sqrt(pi) / sigma_min(K^{-1} B K^{-1})`,

where `K=diag(k_1,k_2,k_3)`.

The sharper sign-specific input used below is the immediately preceding completed account02/B14 overlap theorem

`yspennstate/math-open-problems@0b9ffba8bc766e021ec0f0b6729b43ad9a7ad51d`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260924T055741Z-account02-B14-QFORM-auto11/REPORT.md`.

For independent cap-one scalar laws and

`Q=2aUV+2bUY+2cVY+lambda Y^2+affine`,

with `delta=lambda-2bc/a`, it proves

`||p_Q||_infinity <= (2/|a|) Phi(2 sqrt(|a|/|delta|))`,

where

`Phi(theta)=2 sqrt(theta)` for `theta<=1`,
`Phi(theta)=2+log(theta)` for `theta>=1`.

It also proves the determinant whole-law exit `4+2 log 2` when `|a|>=1` and the physical determinant has modulus at least one, and proves that fragmenting the third active curvature before paying the logarithmic singularity can incur an unavoidable `m log(1/m)` loss. Thus the active banks below are deliberately kept whole.

The one-dimensional product projection estimate used below is the standard Ball--Rogozin consequence: if `c` is a nonzero coefficient vector on independent cap-one coordinates, then

`||p_{c^T X}||_infinity <= sqrt(2)/||c||_2`.

A source-pinned occurrence already used by this slot is `math-open-problems@eeb8a099ee584596693a0aee03e270bf7279e909`, account01/B14 run `20260924T044943Z-account01-B14-auto11`, Section 6.

## 2. Cap-aware form of the partner hyperbolic theorem

Let `U,V,Y` be independent probability variables having finite positive density caps

`k_U=||p_U||_infinity`, `k_V=||p_V||_infinity`, `k_Y=||p_Y||_infinity`.

Consider

`Q=2aUV+2bUY+2cVY+lambda Y^2+alpha U+beta V+gamma Y+eta`,

with `a!=0` and

`delta=lambda-2bc/a !=0`.

Define

`U'=k_U U`, `V'=k_V V`, `Y'=k_Y Y`.

The primed variables are still independent and have density caps at most one. Rewriting the same random variable in the primed coordinates gives

`a'=a/(k_U k_V)`,
`b'=b/(k_U k_Y)`,
`c'=c/(k_V k_Y)`,
`lambda'=lambda/k_Y^2`,

and the Schur residual transforms exactly as

`delta'=lambda'-2b'c'/a' = delta/k_Y^2`.

Applying the completed account02/B14 overlap theorem to the primed variables therefore gives the exact cap-aware inequality

`boxed:
||p_Q||_infinity
 <= (2 k_U k_V/|a|)
    Phi( 2 k_Y sqrt( |a|/(k_U k_V |delta|) ) ).
`                                                               (2.1)

No support location, support diameter, moment or fragment count enters. Arbitrary affine terms are retained exactly.

This is only an analytic rescaling of the three final scalar bank variables; the original target matrix is not replaced by a probabilistic spectral rotation.

## 3. Three disjoint original-coordinate banks

Let `I_1,I_2,I_3` be pairwise disjoint sets of original coordinates. Let `e_r` be a unit vector supported on `I_r`, and put

`Z_r=e_r^T X`, `r=1,2,3`.

Because the supports are disjoint and the original coordinates are independent, `Z_1,Z_2,Z_3` are independent. Ball--Rogozin gives

`k_r:=||p_{Z_r}||_infinity <= sqrt(2)`                         (3.1)

for every `r`, uniformly over arbitrary translations, disconnected/distant support pieces, unbounded support and absence of moments in the original marginals.

Let `E=[e_1 e_2 e_3]`; then `E^T E=I_3`. Let

`C=[[0,a,b],[a,0,c],[b,c,lambda]]`                            (3.2)

be symmetric and assume all three eigenvalues of `C` have modulus at least one. The original-coordinate rank-three matrix

`A_0=E C E^T`                                                  (3.3)

has exactly the three nonzero eigenvalues of `C`, so it lies in the exact owner target.

More generally, let `W` denote any collection of outside original coordinates, independent of the active banks, and consider the pure quadratic ambient matrix

`A=[[E C E^T, E G],[G^T E^T,D]]`,                              (3.4)

where `G,D` are arbitrary compatible real matrices with `D` symmetric. Then

`X^T A X = Z^T C Z + 2 Z^T G W + W^T D W`.                    (3.5)

Conditioning on `W=w` produces only an arbitrary affine term in the three independent scalar bank variables `Z`. Hence every affine-uniform scalar theorem applies with the identical constant. The active original-coordinate principal block `E C E^T` has the three protected eigenvalues of `C` plus zeros; Cauchy interlacing therefore keeps the ambient matrix inside the exact three-large-eigenvalue target.

Thus arbitrary outside self-curvature and arbitrary outside-to-active couplings are allowed, provided those couplings land in the three bank directions, i.e. have the product-preserving form `E G`.

## 4. First actual application of the newest account02/B14 theorem

Let `K=diag(k_1,k_2,k_3)`. From (3.1), every diagonal entry of

`S=sqrt(2) K^{-1}`

is at least one. Therefore

`K^{-1} C K^{-1} = (1/2) S C S`.                              (4.1)

The signed-threshold congruence lemma used in the newest account02/B14 report says that congruence by `S>=I` cannot decrease the number of eigenvalues at least `1` or at most `-1`. Since all three eigenvalues of `C` have modulus at least one, every eigenvalue of `S C S` has modulus at least one. Hence

`sigma_min(K^{-1} C K^{-1}) >= 1/2`.                           (4.2)

Applying the newest completed account02/B14 cap-weighted theorem pointwise after conditioning on `W` gives the real target inequality

`boxed:
||p_{X^T A X}||_infinity <= 12 sqrt(pi)
=21.26944621086619... .
`                                                               (4.3)

This already proves a universal bound for every arbitrary-sign disjoint-three-bank chamber (3.4), uniformly in bank sizes and source geometry.

## 5. Hyperbolic refinement: `8+4 log 2`

The zero diagonal physical pair in (3.2) lets the sharper completed account02/B14 overlap theorem replace (4.3).

Write

`D_0=|det C|=|a|^2 |delta|`.

Because all three eigenvalues of `C` have modulus at least one,

`D_0>=1`.                                                       (5.1)

Also the `2 x 2` principal block `[[0,a],[a,0]]` has eigenvalues `+-|a|`. Cauchy interlacing with the three protected eigenvalues of `C` gives

`|a|>=1`.                                                       (5.2)

Set

`x=k_1 k_2 <=2`, `z=k_3<=sqrt(2)`, `A=|a|>=1`.

Formula (2.1) becomes

`||p_Q||_infinity
 <= (2x/A) Phi( 2 z A^(3/2)/sqrt(x D_0) ).`                    (5.3)

The function `Phi` is increasing. Using `z<=sqrt(2)` and `D_0>=1`,

`||p_Q||_infinity
 <= (2x/A) Phi( 2 sqrt(2) A^(3/2)/sqrt(x) ).`                  (5.4)

Since `x<=2` and `A>=1`, the argument of `Phi` on the right is at least `2`, so the logarithmic branch applies:

`||p_Q||_infinity
 <= (2x/A)[2+log(2 sqrt(2) A^(3/2)/sqrt(x))].`                 (5.5)

For fixed `A`, the right side is increasing in `x` on `(0,2]`. Indeed, apart from the positive factor `2/A`, its derivative is

`2+log(2 sqrt(2))+(3/2)log A-(1/2)log x-1/2`,

whose minimum on `A>=1`, `x<=2` is

`3/2+log 2 >0`.

Thus `x=2` is worst, giving

`||p_Q||_infinity
 <= (4/A)[2+log 2+(3/2)log A].`                               (5.6)

The last expression is strictly decreasing for `A>=1`, because its derivative has the sign of

`3/2-[2+log2+(3/2)log A]
 =-1/2-log2-(3/2)log A <0`.

Therefore its maximum occurs at `A=1`, and

`boxed:
||p_{X^T A X}||_infinity
 <= 4(2+log2)
 =8+4log2
 =10.77258872223978... .
`                                                               (5.7)

This is uniform in the dimensions/cardinalities of all three banks, every original marginal law, and the arbitrary outside matrices `G,D` in (3.4).

The proof never selects an individual coordinate or a small physical minor. It first aggregates each disjoint original-coordinate bank to one scalar variable, pays only the final projection density caps, and only then spends the partner determinant/hyperbolic curvature. Hence arbitrarily distant fragments and unbounded supports are zero-tax in this chamber.

## 6. Diffuse exact-target stress family

Take three disjoint banks `I,J,K` of arbitrary positive sizes `m,n,r` and define

`U=m^(-1/2) sum_{i in I} X_i`,
`V=n^(-1/2) sum_{j in J} X_j`,
`Y=r^(-1/2) sum_{k in K} X_k`.

Consider

`Q=2UV+Y^2`.                                                    (6.1)

The scalar bank matrix is

`C_0=[[0,1,0],[1,0,0],[0,0,1]]`,

with spectrum `{1,-1,1}`. Therefore the original-coordinate matrix has exactly three nonzero eigenvalues `{1,-1,1}` no matter how large the banks are. Its individual matrix coefficients are only `1/sqrt(mn)` on the `I x J` cross block and `1/r` on the `K x K` block, and hence can all tend to zero.

Nevertheless (5.7) gives

`boxed:
||p_{2UV+Y^2}||_infinity <= 8+4log2 <10.773
`                                                               (6.2)

for every choice of independent original-coordinate probability densities bounded by one, including arbitrarily translated, disconnected and unbounded laws with no moments.

For comparison, applying the newest account02/B14 general cap-weighted three-dimensional theorem to exactly the same family gives the valid coarser bound `12sqrt(pi)=21.2694...`; the hyperbolic determinant compiler improves that by almost a factor two.

The same `8+4log2` bound survives the ambient extension (3.4) with `C=C_0`, arbitrary `G,D`, because outside conditioning produces only affine terms in `(U,V,Y)` and the partner theorem is uniform in those affine coefficients.

## 7. Localization interpretation and remaining gap

This run sharpens the proof-order lesson from account02/B14. Spatially fragmenting an active curvature carrier before the logarithmic/Beta singularity is paid can incur an unavoidable entropy or sublinear-mass loss. By contrast, **grouping a disjoint original-coordinate bank first is safe**: the whole bank is summarized by a one-dimensional density cap bounded solely by its coefficient `l2` norm, independent of where its source mass lives.

Thus in the disjoint-bank hyperbolic chamber, translations, distant pieces, unbounded support and lack of moments are not separate debts. The bank aggregation is performed before any reciprocal curvature scale, and the exact three-eigenvalue target supplies `|a|>=1` and determinant modulus at least one only after that aggregation.

The full unrestricted QFORM theorem remains OPEN. A general symmetric target matrix need not admit three disjoint-support bank directions, and even when a useful bank decomposition exists its active/outside coupling need not land in the three-dimensional bank span as in (3.4). The next structural implication is therefore:

`QFORM-PRODUCT-PRESERVING-THREE-BANK-OR-OTHER-WHOLE-ACTIVE-EXIT-v1`:

from bare `s_3(A)>=1`, force either a quantitatively usable disjoint/grouped bank chamber before active fragmentation, or one of the already completed ridge/hub/receiver/physical-pair/Schur exits. No claim of that final implication is made here.
