# QFORM three-hub joint-Plancherel receiver

Programme: QFORM-DENSITY-3EIG-20260922

Worker: account02/B01, oscillatory replacement / complementary constructions

Run: 20260923T140911Z-account02-B01-qform-r43

Status: **NEW SUPPORTING ANALYTIC THEOREM + STRICT-N3 APPLICATION; FULL QFORM REMAINS OPEN.** Independent end-to-end review has not been supplied.

## 1. Sources and corrections actually used

Owner control was resolved from `yspennstate/math-research-brain` fresh main at the start of the run. The active target is the full bounded-density conjecture, not FEI. The pointwise scalar Fresnel claim is known false by phase-aligned fragmented densities and is not used here. No rotated-coordinate independence is used.

Required Claude source was read at the owner-pinned commit

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`

and at the latest compatible master state observed during the run. The completed ingredient used below is the product-projection density bound recorded in `FOURIER_ROUTE_REPORT.md`: a 3-dimensional linear image of independent cap-one coordinates has density at most `2^(3/2)` after whitening; equivalently, for a rank-three `3 x m` matrix `B`,

`||p_{BY}||_infinity <= 2^(3/2) det(B B^T)^(-1/2)`.

The same source's D/D'/D5/H gates are evaluated explicitly on the stress family in Section 4.

Newest designated-partner handoff actually consumed:

`account03/B01`, run `account03-B01-20260923T133048Z-auto11`, canonical mathematics
`yspennstate/math-open-problems@40c82306ce748ae60a09a941277931ae8ca3b05b`.

Its theorem for an invertible indefinite physical pair followed by an arbitrary-sign exact-rank-two Schur principal bank is applied in Section 5. The earlier account03/B01 continuity correction was also consumed; no full-scope continuity claim from that partner theorem is used.

## 2. New theorem: three original hubs with arbitrary curvature on both sides

### Theorem QFORM-THREE-HUB-JOINT-PLANCHEREL-v1

Let `H` consist of three ORIGINAL coordinates and write the remaining original coordinates as a vector `Y`. Allow arbitrary affine terms. Suppose the quadratic polynomial can be written

`Q = X_H^T C X_H + d^T X_H + 2 X_H^T (B Y + c) + R(Y)`,

where

* `C` is any real symmetric `3 x 3` matrix;
* `R(Y)` is an arbitrary real quadratic polynomial (the proof actually only uses that its phase has modulus one);
* `B` is a real `3 x m` matrix of rank three;
* all coordinates of `(X_H,Y)` are independent and have probability densities bounded by one.

Set

`Pi_3(B) = sqrt(det(B B^T)) = sigma_1(B) sigma_2(B) sigma_3(B)`.

Then

`|phi_Q(t)| <= min{1, 2^(3/4) pi^(3/2) Pi_3(B)^(-1/2) |t|^(-3/2)}`,

and therefore `Q` has a continuous `C_0` density satisfying

`||p_Q||_infinity <= 3 sqrt(2) Pi_3(B)^(-1/3)`.

The result is uniform in `C,d,c,R` and in all admissible input laws.

### Proof

Put `U=BY+c`. By the completed three-dimensional product-projection theorem used in the Claude Fourier report,

`||p_U||_infinity <= K := 2^(3/2) Pi_3(B)^(-1)`.

Since `p_U` is a probability density,

`||p_U||_2 <= K^(1/2) = 2^(3/4) Pi_3(B)^(-1/2)`.

For fixed real `t`, define the three-dimensional Fourier transform of the ORIGINAL hub product density with its full hub quadratic phase retained:

`F_t(xi) = E_H exp(i t (X_H^T C X_H + d^T X_H) + i xi^T X_H)`.

The phase has modulus one. Plancherel, together with `0<=f_h<=1`, gives

`||F_t||_2^2 = (2 pi)^3 int prod_{h in H} f_h(x_h)^2 dx_H <= (2 pi)^3`,

hence `||F_t||_2 <= (2 pi)^(3/2)`.

Now condition only algebraically on `Y`; do not rotate or condition the hub laws. The characteristic function is exactly

`phi_Q(t) = E_Y [ exp(i t R(Y)) F_t(2t U) ]`.

Discarding the arbitrary `Y`-phase only after this identity and then using the density of `U`,

`|phi_Q(t)| <= int p_U(u) |F_t(2tu)| du`.

Cauchy-Schwarz and the three-dimensional scaling `v=2tu` give

`|phi_Q(t)|
 <= ||p_U||_2 [ int |F_t(2tu)|^2 du ]^(1/2)
 =  ||p_U||_2 (2|t|)^(-3/2) ||F_t||_2
 <= 2^(3/4) pi^(3/2) Pi_3(B)^(-1/2) |t|^(-3/2)`.

Together with `|phi_Q|<=1`, put

`a = 2^(3/4) pi^(3/2) Pi_3(B)^(-1/2)`.

The elementary integral is

`int_R min(1,a|t|^(-3/2)) dt = 6 a^(2/3)`.

Fourier inversion therefore yields

`||p_Q||_infinity <= (1/(2pi)) 6 a^(2/3)
                   = 3 sqrt(2) Pi_3(B)^(-1/3)`.

The displayed characteristic-function majorant is integrable, so the inverse Fourier transform gives a continuous `C_0` representative in this theorem's scope. QED.

### What this does and does not say

This is a joint three-dimensional averaged-frequency estimate. It is not obtained by multiplying three law-uniform scalar Fresnel estimates, and it does not imply any such scalar estimate. The phase-aligned-density refutation is therefore preserved.

The key new point relative to the previous B01 two-hub/half-Riesz endpoint is that three physical hubs supply an `L^2` scaling exponent `3/2`, which is integrable. Arbitrary hub-hub quadratic curvature is kept inside `F_t`; arbitrary leaf-leaf curvature is kept inside the discarded unit-modulus phase. No diagonal or low-rank hypothesis is imposed on either self block.

## 3. General k-hub calculation (supporting observation)

The same proof works for `k>=3` original hub coordinates if one uses the standard `k`-dimensional product-projection cap `2^(k/2) det(BB^T)^(-1/2)`. Writing `Pi_k` for the product of the `k` nonzero singular values gives

`|phi(t)| <= min(1, 2^(k/4) pi^(k/2) Pi_k^(-1/2) |t|^(-k/2))`

and

`||p_Q||_infinity <= [k sqrt(2)/(k-2)] Pi_k^(-1/k)`.

Only the `k=3` case is needed for the target-level application below; no claim of optimality is made for general `k`.

## 4. Strict-N3 coloop family paid at constant 3 sqrt(2)

Fix an integer `k>=4` and let `m=k^4`. Use three original hub coordinates `h_1,h_2,h_3`, two disjoint leaf banks `J_1,J_2` of size `m`, and one additional leaf coordinate `z`.

Let `u_1,u_2` be the flat unit vectors on `J_1,J_2`. Define the hub-to-leaf block

`B_k = [ k u_1^T ; k u_2^T ; k^(-2) e_z^T ]`.

Thus every nonzero physical coefficient in the first two hub rows is `1/k`, while the `h_3-z` coefficient is `1/k^2`. The three singular values of `B_k` are exactly

`k, k, k^(-2)`,

so

`Pi_3(B_k)=1`.

First take both self blocks zero. The full symmetric bipartite matrix

`A_k^0 = [[0,B_k],[B_k^T,0]]`

has nonzero spectrum

`{k,k,k^(-2),-k,-k,-k^(-2)}`.

Hence it has at least four eigenvalues of absolute value at least one. Every physical diagonal is zero and every nonzero physical `2 x 2` principal determinant has magnitude at most `1/k^2`. Thus for every fixed no-pivot threshold `tau>0`, `A_k^0` lies in strict N3 for all sufficiently large `k`.

The theorem gives the parameter-free bound

`||p_{X^T A_k^0 X}||_infinity <= 3 sqrt(2) = 4.242640687...`.

The same bound is unchanged if an arbitrary symmetric leaf self block `E_k` is added. To make this tolerance concrete while staying in strict N3, order the `2m+1` leaves on an odd cycle and put

`E_k = k^(-1) Adj(C_{2m+1})`.

Then `E_k` is non-diagonal and full rank (odd cycle), `||E_k||_op<=2/k`, every off-diagonal entry has magnitude at most `1/k`, and every physical diagonal remains zero. Weyl leaves the four eigenvalues near `+/-k` larger than one in modulus for `k>=4`, while all physical pair determinants are still `<=1/k^2` in magnitude. The new theorem still gives exactly `3sqrt(2)` because it never pays for `E_k`.

## 4.1 Actual application of the newest Claude volume/hub report

On the natural hub-versus-leaf cross block, the completed Claude volume quantity is strong:

`Z_3 = e_3(B_k^T B_k) = Pi_3(B_k)^2 = 1`.

But the exact-rank-three volume marginals are concentrated. If the constrained side is the three hubs, all three row marginals equal one. If the constrained side is the leaves (`B_k^T`), every row in `J_1` or `J_2` has leverage `1/m`, whereas the singleton `z` row has leverage exactly one. Hence Theorem D's `1/2` gate and D' with any `h<3/4` fail on both natural orientations even though `Z_3=1`. D5 is unavailable because the cross block has rank three, so `Z_5=0`.

Likewise, in Theorem H with all three hubs and `r=0`, the augmented Gram is `B_k B_k^T`, and the normalized leverage of the singleton `z` leaf is exactly one. Thus the clean three-hub H gate fails on this natural packet. These are concrete source-valid obstructions, not a claim that every conceivable source decomposition fails.

At the inequality level, the source's checked three-dimensional product-projection theorem is exactly what starts the new proof:

`||p_{B_k Y}||_infinity <= 2^(3/2) / Pi_3(B_k) = 2^(3/2)`.

It is then converted by joint hub Plancherel into the target bound `3sqrt(2)` without a volume-marginal gate.

## 5. Newest designated-partner theorem applied to the same family

Use the zero-leaf-curvature member `A_k^0` for a clean comparison. Select the indefinite original physical pair

`P={h_1,y_{1,1}}`.

Its block is

`[[0,1/k],[1/k,0]]`,

so

`D=1/k^2`, `kappa=1/k`.

Because `y_{1,1}` couples only to `h_1`, while `h_1` couples only to the `J_1` bank, the exact Schur correction from this hyperbolic pair vanishes on all principal blocks disjoint from `J_1`. In particular the remaining pair

`V={h_2,y_{2,1}}`

is an exact-rank-two symmetric Schur principal block

`S_0=[[0,1/k],[1/k,0]]`

with

`Pi_2=|mu_1 mu_2|=1/k^2`.

The newest account03/B01 theorem therefore gives the valid full-form bound

`||p_Q||_infinity
 <= min{512 kappa^(-1/2) Pi_2^(-1/4),
        64(D kappa)^(-1/4) Pi_2^(-1/8)}
 = min{512 k,64 k}
 = 64 k`.

This is a real application, not a summary. It also exhibits the structural reason to aggregate before local pair inversion: along this strict-N3 family the local pair+Schur certificate diverges linearly in `k`, while the joint three-hub receiver remains `3sqrt(2)` because the global singular product `k*k*k^(-2)` is exactly one.

For the cycle-curved variant, choose `y_{1,1}` and `y_{2,1}` nonadjacent on the cycle. The Schur principal block on `V` remains the displayed hyperbolic block, so the same partner inequality remains available; the new theorem still ignores all cycle curvature.

## 6. Why this is full-target relevant

The family simultaneously has:

1. at least three actual eigenvalues of magnitude at least one (in fact four);
2. arbitrarily small physical diagonal and pair-pivot currency;
3. a rank-three cross packet with fixed volume `Z_3=1` but a volume coloop of marginal one;
4. optional genuinely non-diagonal, full-rank leaf curvature;
5. a local indefinite-pair+rank-two-Schur certificate whose bound diverges;
6. a global product-preserving three-hub singular-product certificate whose density bound is universal.

Thus one remaining no-pivot routing theorem should not automatically invert the first small physical pair or discard a rank-three packet merely because one volume marginal is a coloop. A three-row aggregate can be paid directly in joint `L^2` frequency.

## 7. First unpaid implication after this run

`QFORM-N3-THREE-HUB-OR-VOLUME-ROUTING-v1`:

From arbitrary strict N3 under the three-large-eigenvalue hypothesis, prove that one can either

* extract three ORIGINAL hub coordinates whose full complement slope matrix `B` has `Pi_3(B)` bounded below at target scale and then apply QFORM-THREE-HUB-JOINT-PLANCHEREL-v1; or
* route quantitatively to an already-paid D/D'/D5 volume, mixed-hub/Fresnel, definite/indefinite pair, rank-two Schur, ridge, grouped-square, exact-null/coloop, or other existing receiver,

before paying an uncontrolled reciprocal tiny physical determinant.

The theorem proved here pays the analytic three-hub receiver, including arbitrary self-curvature. It does **not** prove the required exhaustive matrix-structural extraction from the bare spectral hypothesis. Full QFORM therefore remains OPEN.
