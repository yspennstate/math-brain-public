SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-24T00:48:17Z.
attacking: local-row spectral reserve: allow arbitrary huge added signed modes in q physical row directions while paying only the first unreserved local square-energy singular value; compose with account04/B12 multihub shear.

# account03/B12 — local spectral-leakage reserve for arbitrary additional eigenvalues

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T004817Z-qform-eigenvalue-r45`  
Status: **PROVED SUPPORTING STABILITY THEOREM / FULL QFORM OPEN**  
Continuity: **not claimed for the combined density theorem; the six-mode compiler used below gives essential boundedness.**

## 1. Scope

The target remains: independent real coordinates with arbitrary probability densities bounded by one, and an arbitrary real symmetric coefficient matrix with at least three eigenvalues of absolute value at least one. No Gaussian, log-concave, moment, compact-support, connected-support, post-rotation independence, or diagonal-basis hypothesis is introduced.

This run addresses only coefficient stability under added eigenvalues. Every statement below is deterministic at the matrix level until the already-proved physical six-square-mode density compiler is invoked. In particular, no term `X^T T X` is treated as independent noise or as a convolution factor.

The designated partner actually applied is account04/B12, run `20260924T002154Z-account04-B12-multihub-shear-r8`, canonical report `yspennstate/math-open-problems@bcb9fd2641440a89d6e4967781d755618e163001:proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260924T002154Z-account04-B12-multihub-shear-r8/REPORT.md`. Its theorem gives a lower singular-value gate for a physical row block after arbitrary signed spectral packets aligned with a bounded-dimensional physical hub plane.

The density receiver is the completed account02/B12 theorem `QFORM-SIX-SQUARE-MODE-PAIR-COMPILER-v2` at commit `c635fcdce6aa206c68f1f14e061cf617d72376fb`, with

`C_m = max{8 binom(m,2) sqrt(6 pi m), 4 pi binom(m,2), 3*400^(1/3)*(4 binom(m,2))^(5/6), 10 sqrt(2e/3)}`.

## 2. Local-row reserve theorem

Let `H` be a set of `m` ORIGINAL coordinates and let `P_H` denote the `m x n` row-selection matrix. Let

`A = A_* + T_1 + ... + T_s`

with all matrices symmetric. For packet `T_j`, choose an integer `q_j>=0` and define

`tau_j = s_(q_j+1)(P_H T_j)`,  `Q = sum_j q_j`.

### Theorem 2.1 — `QFORM-LOCAL-ROW-MULTIPACKET-RESERVE-v1`

For every `k>=1` with `k+Q<=m`,

`boxed( s_k(P_H A) >= s_(k+Q)(P_H A_*) - sum_j tau_j ).`

Equivalently,

`boxed( sqrt(lambda_k((A^2)[H,H])) >= sqrt(lambda_(k+Q)((A_*^2)[H,H])) - sum_j tau_j ).`

#### Proof

For each `Y_j=P_H T_j`, take a best rank-`q_j` approximation `K_j` in operator norm. By Eckart-Young,

`rank(K_j)<=q_j`,  `||Y_j-K_j||_op=tau_j`.

Set `K=sum_j K_j` and `E=sum_j(Y_j-K_j)`. Then

`rank(K)<=Q`,  `||E||_op<=sum_j tau_j`,

and

`P_H A = P_H A_* + K + E`.

Rank-`Q` singular-value interlacing gives

`s_k(P_H A_*+K) >= s_(k+Q)(P_H A_*)`.

Indeed, applying the standard singular-value inequality to

`P_H A_* = (P_H A_*+K)-K`

gives

`s_(k+Q)(P_H A_*) <= s_k(P_H A_*+K)+s_(Q+1)(K)=s_k(P_H A_*+K)`.

Finally operator-norm Weyl gives

`s_k(P_H A) >= s_k(P_H A_*+K)-||E||_op`.

Combining the last two displays proves the claim. Since

`(P_H A)(P_H A)^T = P_H A^2 P_H^T = (A^2)[H,H]`,

the square-Gram formulation is identical. QED.

This is strictly more local than a global packet bound using `s_(q+1)(T_j)`: always

`s_(q+1)(P_H T_j) <= s_(q+1)(T_j)`,

and the inequality may be arbitrarily stronger when huge spectral modes have little or low-dimensional footprint on `H`.

## 3. Exact spectral-leakage formula

For one symmetric packet

`T = sum_a theta_a v_a v_a^T`,

where the `v_a` are orthonormal eigenvectors, put `u_a=P_H v_a`. Then

`(P_H T)(P_H T)^T = P_H T^2 P_H^T = sum_a theta_a^2 u_a u_a^T`.

Therefore, for every `q>=0`,

`boxed( tau_q(H,T)^2 := s_(q+1)(P_H T)^2 = lambda_(q+1)( sum_a theta_a^2 u_a u_a^T ) ).`

By Courant-Fischer this has the exact variational form

`tau_q(H,T)^2 = min_(dim L=q) max_(x perp L, ||x||=1) sum_a theta_a^2 <x,u_a>^2`.

Thus signs disappear only inside the deterministic square-energy accounting; no probabilistic independence is asserted or needed.

### Corollary 3.1 — arbitrary large modes plus arbitrary small spectrum

Fix `h>=0` and let

`L_h = span{ P_H v_a : |theta_a|>h }`,  `q_h=dim L_h`.

Then

`boxed( s_(q_h+1)(P_H T) <= h ).`

#### Proof

Split

`G=P_H T^2 P_H^T=G_big+G_small`,

where `G_big` sums `|theta_a|>h` and `G_small` sums the remaining eigenmodes. By construction `rank(G_big)<=q_h`. Moreover

`G_small <= h^2 sum_(small a) u_a u_a^T <= h^2 I_H`,

because a subfamily of an orthonormal eigenbasis has projection Gram bounded by the identity. Rank-`q_h` interlacing then gives

`lambda_(q_h+1)(G) <= ||G_small||_op <= h^2`.

Taking square roots proves the claim. QED.

This is the key additional-eigenvalue control: arbitrarily many eigenvalues of arbitrary magnitude and either sign are completely free if their physical `H`-projections span only `q_h` directions; all remaining eigenvalues, however numerous and however oriented, cost only the common threshold `h` when their magnitudes are at most `h`.

A useful profile is

`d_H(T;h)=dim span{P_H v_a: |theta_a|>h}`.

The final carrier can trade physical reserve directions against spectral threshold by choosing `h` so that `d_H(T;h)` fits the available reserve.

## 4. Composition with the completed account04/B12 partner theorem

Use the partner notation on the same ORIGINAL-coordinate bank `H`:

`C_* = U Lambda U^T`,  `B_* = U W^T + R`,  `U^T R=0`,

where `U` has `p` orthonormal columns. Put

`g0 = gamma(||Lambda^(-1) W^T||_op) min{s_p(Lambda),s_ell(R)}`,

`gamma(t)=(sqrt(t^2+4)-t)/2`.

Partner account04/B12 proves

`s_(p+ell)(P_H A_*) >= g0`.

Now add arbitrary symmetric packets `T_1,...,T_s`. Choose local reserve integers `q_j` and set

`Q=sum q_j`,  `tau_j=s_(q_j+1)(P_H T_j)`.

### Theorem 4.1 — `QFORM-MULTIHUB-LOCAL-SPECTRAL-LEAKAGE-COMPILER-v1`

If

`p+ell-Q >= 6`

and

`g = g0 - sum_j tau_j > 0`,

then the actual final matrix `A=A_*+sum_j T_j` satisfies

`boxed( sqrt(lambda_6((A^2)[H,H])) >= g )`

and every independent cap-one product input obeys

`boxed( ||p_(X^T A X)||_(infinity,ess) <= C_m/g ).`

#### Proof

Apply Theorem 2.1 with `k=p+ell-Q`. Then

`s_(p+ell-Q)(P_H A) >= s_(p+ell)(P_H A_*) - sum_j tau_j >= g`.

Since `p+ell-Q>=6`, monotonicity of singular values gives `s_6(P_H A)>=g`. The identity

`s_6(P_H A)=sqrt(lambda_6((A^2)[H,H]))`

supplies the final square-energy gate. The completed physical six-square-mode compiler applies directly to this final matrix and gives `C_m/g`. No added quadratic term is removed from the random variable. QED.

### Corollary 4.2 — threshold form

For each packet `T_j`, choose a threshold `h_j>=0` and let

`q_j = dim span{P_H v : v is an eigenvector of T_j with |theta|>h_j}`.

If

`p+ell-sum_j q_j >=6`

and

`g0-sum_j h_j>0`,

then

`||p_(X^T A X)||_(infinity,ess) <= C_m/(g0-sum_j h_j)`.

Thus each packet may contain arbitrarily many unbounded positive and negative eigenvalues. Their number is irrelevant; only the dimension of their physical footprint on the chosen bank is charged. Every remaining full-rank small spectrum costs only its magnitude threshold.

## 5. Actual partner application

Take `m=8`, `p=2`, `ell=6`. Let

`U=(e_1,e_2)`

and choose a transverse carrier `R` with `U^T R=0` and

`s_6(R)=2`.

Allow an arbitrary signed aligned packet already absorbed into the partner aggregate `Lambda,W`, subject only to

`s_2(Lambda)>=4`,

`||Lambda^(-1) W^T||_op<=1`.

The completed account04/B12 inequality gives the actual equation

`s_8(P_H A_*) >= gamma(1) min{4,2} = 2 gamma(1) = sqrt(5)-1 = 1.2360679774997898...`.

Now add one further completely arbitrary symmetric spectral packet `T`. Assume only that for threshold

`h=1/100`

the `H`-projections of every eigenvector of `T` whose eigenvalue satisfies `|theta|>1/100` span at most two dimensions. The number, signs, and magnitudes of those large eigenvalues are unrestricted. All other eigenvalues may have arbitrary orientation and rank, subject only to `|theta|<=1/100`.

Corollary 3.1 gives

`s_3(P_H T)<=1/100`.

Theorem 2.1, now at the actual partner equation with `k=6,q=2`, yields

`boxed( s_6(P_H(A_*+T)) >= sqrt(5)-1-1/100 = 1.2260679774997898... ).`

Equivalently,

`boxed( sqrt(lambda_6((A^2)[H,H])) >= 1.2260679774997898... ).`

This is strictly broader than the partner's earlier example `||P_H T||_op<=1/100`: here the first two local singular values of `P_H T` may be arbitrarily large.

For `m=8`, `N_2=28` and

`C_8 = 8*28*sqrt(48 pi) = 2750.7021909601613...`,

which dominates the other three compiler constants. Therefore

`boxed( ||p_(X^T A X)||_(infinity,ess) <= 2243.515238502045... ).`

Also `s_6(P_H A)<=s_6(A)`, so this family satisfies `s_6(A)>1` and hence lies genuinely inside the original target class.

This application uses the designated account04/B12 result at a concrete inequality and then strengthens its tail stability from a full local operator-norm restriction to an unbounded two-direction local spectral packet plus arbitrary full-rank small spectrum.

## 6. Why this is not a convolution argument

The final random variable is always the exact

`Q=X^T A X`,  `A=A_*+sum_j T_j`.

The proof never conditions in a rotated eigenbasis and never asserts that `X^T T_j X` is independent of the baseline quadratic form. The packets enter only through deterministic singular-value inequalities for the final physical row block `P_H A`. The only probabilistic theorem invoked is the existing six-square-mode compiler, which works in original coordinates.

## 7. Finite deterministic checks

The accompanying seeded checker performed two tests.

1. 5,000 spectral-threshold instances with `m=8,n=14,q=2,h=0.01`. Arbitrarily large signed eigenvalues, with magnitudes up to `10^5`, were placed in an eight-dimensional global subspace whose `H`-projections lie in a two-plane; the remaining six eigenvalues were arbitrary in `[-h,h]`. There were zero violations of `s_3(P_H T)<=h`. Maximum observed `s_3(P_H T)` was `0.00999989064994689`.

2. 5,000 two-packet random symmetric instances of Theorem 2.1. There were zero violations of the local multipacket reserve inequality. The minimum numerical margin was `6.957753258643377`; the maximum error in the exact identity `s_(q+1)(P_H T)^2=lambda_(q+1)((T^2)[H,H])` was `6.217248937900877e-15`.

These computations are consistency checks only; the theorem is proved analytically above.

## 8. Sharpness and limits

The reserve-direction loss cannot be removed in general. A rank-`q` packet can cancel exactly `q` singular directions of a baseline row block, so a theorem retaining the same singular index after allowing `q` completely unbounded local directions is false without additional geometry. Likewise the coefficient one in the residual operator loss is the standard sharp Weyl coefficient.

What remains unpaid is structural. The bare target hypothesis `s_3(A)>=1` does not yet force a bounded ORIGINAL-coordinate bank carrying eight baseline square-energy modes with only two local high-spectrum directions, nor any equivalent bounded-reserve profile. Failure must still be routed into one of the proved projected-crossing, grouped-bank, ridge, hub/common-plane, physical-core, Schur, or Pluecker-volume exits.

Therefore the full QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**.
