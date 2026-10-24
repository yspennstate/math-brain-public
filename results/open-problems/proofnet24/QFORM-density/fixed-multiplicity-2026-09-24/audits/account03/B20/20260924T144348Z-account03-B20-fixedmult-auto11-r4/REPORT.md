SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B20, 2026-09-24T14:43:48Z.

# account03/B20 r4 — release-gate correction, nine-direction certification, and the one-symmetrization L2 barrier at multiplicity eight

Run: `20260924T144348Z-account03-B20-fixedmult-auto11-r4`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned baseline: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.  
Execution status: `WITHOUT_VERIFIED_BRAIN`.

## 1. Release-gate correction: the pinned singular-Schur paragraph is sound

A previous B20 audit (`r2`) classified the singular-`A` passage of `lem:schur` as a repairable moving-threshold gap. That classification was too pessimistic and is retracted here.

Let `B` be the already invertible `k x k` principal pivot block and let

`S = C - F B^{-1} E`

be the Schur complement. For the regularized matrix `A_eps=A+eps I`, the corresponding principal pivot `B_eps=B+eps I_k` remains invertible for all sufficiently small `eps`, and `S_eps -> S` in operator norm as `eps->0`.

Fix `t>0`, and put `m=N_A(t)-k`. If `m<=0` there is nothing to prove. For every sufficiently small `eps` with `|eps|<t`, Weyl's inequality gives

`N_{A_eps}(t-|eps|) >= N_A(t)`.

The already-proved invertible case of the Schur count, applied to `A_eps` at threshold `t-|eps|`, therefore gives

`N_{S_eps}(t-|eps|) >= m`.

Equivalently,

`s_m(S_eps) >= t-|eps|`.

Singular values are continuous in operator norm, so along any `eps_j->0`,

`s_m(S)=lim_j s_m(S_{eps_j}) >= lim_j(t-|eps_j|)=t`.

Hence

`N_S(t)>=N_A(t)-k`.

No illegitimate passage from a lower moving threshold to a fixed threshold occurs: the inequality is on the `m`-th singular value itself and the lower bound converges to `t`. This matches the independent account01/B05 and account02/B16 full-source audits, both of which explicitly mark the singular-Schur approximation PASS.

**Corrected source status:** the pinned seventeen-direction mathematical proof is PASS in this B20 release-gate review. The minor product-projection wording issue concerning zero Brascamp--Lieb weights is editorial only (`sum_{b_i>0}(1-b_i)<=d` after omission, rather than an equality on the restricted index set) and does not change the theorem or constants.

The theorem actually certified by the pinned source is an essential-density statement. It does not establish global continuity.

## 2. Lowest release-grade bounded-density multiplicity in the current source tree: nine

Two separate complete reconstructions now support the same rough-law-safe nine-direction replacement:

1. account01/B05, commit `c98bc2c787b36dc6d315bd3e335913b682fd8fd8`, independently audits all 790 source lines and reconstructs the nine-direction replacement;
2. account02/B16, commit `d3299af8809b11f51e3d6dd1273c54913c197989`, independently audits the pinned baseline and reconstructs the nine-direction replacement.

Both retain independent coordinate densities bounded by `K`, arbitrary real symmetric `A`, arbitrary signs, arbitrary affine `b,c`, arbitrary dimension and remaining spectrum, and no moment/support/log-concavity assumptions. A common safe constant from the independently reconstructed chain is

`||p_Q||_infinity < 5338 K^2/s`

under `s_9(A)>=s>0`.

Therefore B20's release-grade multiplicity threshold for **essential boundedness** is now

`m_release = 9`.

Several newer workers report smaller constants, but B20 does not promote a smaller numerical constant here unless the same exact constant has two complete independent reviews. The threshold improvement `9 -> 8` remains unproved.

Continuity is tracked separately. The pinned seventeen-direction source does not claim it globally. Fresh fleet work contains separate continuity compilers at multiplicity nine, but this run does not count those as part of the two-review `L^infinity` release certificate unless their complete end-to-end continuity chains are separately reviewed.

## 3. Current multiplicity-eight endpoint

The terminal no-pivot `s_8(A)>=1` collar now has a literal original-coordinate pair `H_*` with outside cross map

`C=A[H_*,H_*^c]`

satisfying

`det(CC^T)>=D_0=0.3649442658827020...`.

The exact-zero self-block subcase is already continuously paid. Uniformly in the self-block, the determinant-free two-anchor theorem gives the critical characteristic-function envelope

`|phi_Q(t)| <= min(1,6.664084228844337/|t|)`

and hence a density in every finite `L^p`, with near-Lipschitz `h log(1/h)` small-ball control. This is a genuine endpoint result but not `L^infinity`.

The local pair data alone cannot suffice: current explicit rank-two product examples have the same strong cross-Gram lower bound, arbitrarily weak nonzero self-curvature, and an unbounded logarithmic output density. The missing information must use the extra spectral provenance forced by `s_8(A)>=1` (for an invertible pair pivot, six unit-scale Schur directions) or the overlap-one/overlap-two determinant currency.

The robust-anchor reduction also gives, for every good seed `B=A[S,T]` assigned to `H_*`, the overlap-two four-by-four determinant

`|det A[S union H_*, T union H_*]| >= gamma_* |det B|`,

where

`gamma_*=1-3 sqrt(2)/40 = 0.8939339828220179...`.

This is precisely the curvature that disappears under naive disjointification.

## 4. New theorem: a one-symmetrization L2 compiler is exponent-critical

### Theorem `QFORM-OVERLAP4-ONE-SYMMETRIZATION-L2-BARRIER-v1`

Let `M` be an invertible real `d x d` matrix and let `F,G in L^2(R^d)`. For `t!=0` define

`B_t(F,G)=int int exp(i t u^T M v) F(u)G(v) du dv`.

With the manuscript Fourier convention

`hat G(xi)=int exp(i xi dot v)G(v)dv`,

one has the exact Hilbert-space operator bound

`|B_t(F,G)| <= (2 pi)^(d/2) |t|^(-d/2) |det M|^(-1/2) ||F||_2 ||G||_2`.    (4.1)

Moreover the power `|t|^(-d/2)` is optimal for an argument using only the two `L^2` norms: the map

`T_t G(u)=hat G(t M^T u)`

has **exact** `L^2 -> L^2` norm

`(2 pi)^(d/2)|t|^(-d/2)|det M|^(-1/2)`.

#### Proof

Write

`B_t(F,G)=int F(u) hat G(t M^T u) du`.

Cauchy--Schwarz gives

`|B_t(F,G)| <= ||F||_2 ||hat G(t M^T dot)||_2`.

The change of variables `xi=t M^T u` and Plancherel give

`||hat G(t M^T dot)||_2^2
 = |t|^(-d)|det M|^(-1)||hat G||_2^2
 = (2 pi)^d |t|^(-d)|det M|^(-1)||G||_2^2`,

which proves (4.1). The displayed identity is itself the exact norm formula for `T_t`; for any nonzero `G`, equality in Cauchy--Schwarz is attained by taking `F` proportional to the complex conjugate of `T_tG`. Thus no better power of `t` follows uniformly from `L^2` information alone. QED.

### Consequence at the actual overlap-two `s_8` geometry

After one independent-copy symmetrization, the tempting use of the full overlap-two `4 x 4` block is a `d=4` bilinear problem. Even granting a perfect reduction to separated `L^2` amplitudes, (4.1) yields at best

`|phi_Q(t)|^2 <= (2 pi)^2 |t|^-2 |det M|^-1/2 * (L2 amplitude factors)`,

hence

`|phi_Q(t)| <= 2 pi |t|^-1 |det M|^-1/4 * (L2 amplitude factors)^(1/2)`.    (4.2)

For a good seed, `|det M|>=gamma_*|det B|`, so determinant aggregation can improve the **coefficient** in (4.2) but not its time exponent. The exponent remains exactly the nonintegrable `1/|t|` endpoint.

Therefore the following strategy is now ruled out as a complete multiplicity-eight proof:

> one symmetrization + retain the overlap-two `4 x 4` determinant + reduce all selected paired sources only to `L^2` norms + Plancherel.

This cannot create the positive Fourier-integrability margin required by absolute inversion. It does **not** prove that multiplicity eight is false and does not rule out nonabsolute Fourier inversion. It says the next successful endpoint must use information strictly beyond that Hilbert-space route: for example paired-source structure beyond `L^2`, a genuinely unsquared cancellation estimate, a second mechanism coupled to the six Schur directions, or a direct small-ball/coarea argument that keeps the shared anchors.

This sharpens the current frontier because the paired-source work already showed that naive splitting loses the shared anchor; the theorem above shows that even a hypothetical perfect `L^2` separation of the full order-four overlap block would still be only critical.

## 5. Threshold accounting and next exact target

The current rigorous hierarchy used by B20 is:

- pinned source: multiplicity 17, essential boundedness, PASS;
- independently reconstructed replacement: multiplicity 9, essential boundedness, release-grade bound `<5338 K^2/s`;
- multiplicity 8: density exists in every finite `L^p` with explicit dimension-free bounds, but universal `L^infinity` remains OPEN;
- unrestricted multiplicity 3 conjecture: OPEN / not proved / not disproved.

The next exact target is

`QFORM-S8-SHARED-ANCHOR-SIX-SCHUR-ENDPOINT-v1`:

construct a product-law-safe endpoint receiver that simultaneously spends (i) the shared-anchor overlap determinant currency and/or (ii) the six unit-scale Schur directions, without reducing the argument to the critical one-symmetrization `L^2` estimate above.

No Gaussianity, log-concavity, moment, compact-support, connected-support, diagonal-basis, post-rotation independence, arbitrary-joint coarea, or law-uniform pointwise quadratic-phase decay assumption is introduced in this report.
