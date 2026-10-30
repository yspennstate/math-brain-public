# fleet03/B02 — square-pivot integrated determinant threshold theorem

Run: `20260922T142939Z-fleet03-B02-QFORM-r11b`  
Programme: `QFORM-DENSITY-3EIG-20260922`, owner control revision `2026-09-22.5`  
Assignment: Integrated Fourier estimate  
Status: `ESSENTIAL_STEP_APPLIED / SUPPORTING_TARGET_BRANCHES_PROVED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Exact target and scope

The full target is the universal statement for every dimension, every independent real input with coordinate densities bounded by one, and every real symmetric matrix having at least three eigenvalues of absolute value at least one. That full statement remains OPEN here. No moment, compact-support, log-concavity, continuity-of-input-density, or post-rotation independence assumption is used.

The owner-requested continuity conclusion is tracked separately. The new branches below prove an essentially bounded output density; continuity is **not** claimed by the square-pivot argument.

## 2. Dependencies actually used

The only non-elementary analytic input is the already archived regularized-determinant characteristic-function estimate from

- `yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`, interactive report `proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`.

Its Sections 3--6 received a completed independent PASS from fleet02/B02 at

- `yspennstate/math-open-problems@e3fe4ce35f6aa4a90cca913051886c96c7febfc3`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/20260922T140817Z-fleet02-B02-qform-r11/REPORT.md`.

For disjoint physical coordinate sets `I,J`, `B=A[I,J]`, it gives the endpoint

`|phi(t)| <= det(I + 4 t^2 B B^T/(pi^2 e^2))^(-1/8)`

without a leverage hypothesis, and for `1 <= q < 2`, when the maximum coordinate leverage of `range(B)` on the `I` side is at most `q/2`,

`|phi(t)| <= det(I + 2 q t^2 B B^T/(pi^2 e^2))^(-1/(4q))`.

I use the notation `q=2` for the unconditional endpoint. No pointwise scalar van-der-Corput estimate is used.

The designated partner `fleet04/B02` had no completed current-QFORM handoff in the shared directory at the pre-publication observation point, so no result was attributed to that partner. The completed compatible fleet02/B02 review/result above is actually applied.

## 3. Main theorem: a scalar physical square halves the determinant-order threshold

Let `X=(Z,W)` be independent original coordinates with all coordinate densities at most one, and write the symmetric matrix in the physical coordinate `Z` as

`A = [[d, a^T],[a,C]]`, with `d != 0`.

Complete the physical square:

`Q = d (Z + a^T W/d)^2 + R(W)`,

where

`R(W)=W^T S W`, `S=C-aa^T/d`.

Choose disjoint original-coordinate sets `I,J` among the coordinates of `W`, put `B=S[I,J]`, and for an integer `k>=1` define

`E_k(B)=e_k(s_1(B)^2,s_2(B)^2,...) = sum_{|R|=|T|=k} det(B[R,T])^2`.

Fix either

1. `q=2`, with no leverage hypothesis; or
2. `1 <= q < 2`, with maximum physical-coordinate leverage of the projection onto `range(B) subset R^I` at most `q/2`.

Assume `k>q` and `E_k(B)>0`. Choose any Fourier exponent `r` satisfying

`max(1,2q/k) < r < 2`.

Then `Q` has an essentially bounded density and

`||p_Q||_infinity <= C(q,k,r) |d|^(-1/2) E_k(B)^(-1/(4k))`,

where

`C(q,k,r) = P(r) sqrt(e) 2^(-3/4) q^(-1/4) * sqrt( (1/k) BETA(1/(2k), r/(4q)-1/(2k)) )`,

and

`P(r)=4 (2-r)^((r-3)/2) r^(-r/2)`.

This is `QFORM-SQUARE-PIVOT-EK-INTEGRATED-v1`.

### Why this is a genuine threshold improvement

Without the scalar physical square, direct Fourier inversion of the regularized determinant estimate requires determinant order `k>2q`. The theorem above needs only `k>q`. The square-pivot potential estimate therefore halves the aggregate cross-determinant order needed for integrability.

In particular:

- unconditional endpoint `q=2`: a rank-three aggregate (`E_3>0`) is enough after a scalar pivot, whereas direct inversion needs `k>=5`;
- leverage-assisted endpoint `q=1`: a rank-two aggregate (`E_2>0`) is enough after a scalar pivot, whereas direct inversion needs `k>=3`.

This directly advances the fleet02/B02 aggregate-determinant result rather than selecting one tiny physical minor.

## 4. Proof

### Step 1: integrated Fourier credit for the Schur remainder

Set

`alpha_q = 2q/(pi^2 e^2)`.

For `q<2` the reviewed fractional determinant theorem gives

`|phi_R(t)| <= det(I+alpha_q t^2 B B^T)^(-1/(4q))`.

For `q=2`, this is exactly the unconditional determinant theorem because `alpha_2=4/(pi^2 e^2)` and exponent `-1/8`.

The elementary-symmetric expansion of the determinant gives

`det(I+alpha_q t^2 B B^T) >= 1 + alpha_q^k E_k(B) t^(2k)`.

Therefore, for `kr>2q`,

`int_R |phi_R(t)|^r dt`
` <= int_R (1+alpha_q^k E_k(B) t^(2k))^(-r/(4q)) dt`
` = (1/k) BETA(1/(2k), r/(4q)-1/(2k)) alpha_q^(-1/2) E_k(B)^(-1/(2k))`.

This is the promised integrated estimate. It remains valid for arbitrary self-blocks and arbitrary outside couplings already absorbed into the Schur remainder.

### Step 2: Hausdorff--Young creates an `L^p` density for `R`

Let `p=r/(r-1)>2`. With Fourier convention

`phi_R(t)=int e^(itr) p_R(r) dr`,

inverse Hausdorff--Young by interpolation between `L^1 -> L^infinity` and Plancherel gives

`||p_R||_p <= (2pi)^(-1/r) ||phi_R||_r`.

Consequently, if

`K(q,k,r)=(1/k) BETA(1/(2k), r/(4q)-1/(2k))`,

then

`M:=||p_R||_p`
` <= (2pi)^(-1/r) K(q,k,r)^(1/r) alpha_q^(-1/(2r)) E_k(B)^(-1/(2kr))`.

Thus the Schur remainder has an actual `L^p`, `p>2`, density. This conclusion is distributional and does not require prior absolute continuity of `R`.

### Step 3: uniform conditional square kernel

Condition on `W=w`. The translated input `Z+a^T w/d` still has a density bounded by one. Hence the conditional density of

`d (Z+a^T w/d)^2`

is pointwise bounded by

`|d|^(-1/2) |u|^(-1/2)`

on its appropriate sign half-line. Dropping the sign restriction can only enlarge the upper bound. Therefore

`p_Q(t) <= |d|^(-1/2) int_R p_R(s) |t-s|^(-1/2) ds`.

No conditional-independence replacement is made: this follows directly from the original physical coordinate `Z`, which is independent of `W` before conditioning.

### Step 4: one-dimensional potential estimate

For every probability density `p0` with `||p0||_p=M`, `p>2`, let `r=p/(p-1)` as above. Split at a radius `R0>0`. Holder on the near part and probability mass on the far part give

`int p0(s)|t-s|^(-1/2) ds`
` <= A_r M R0^(1/r-1/2) + R0^(-1/2)`,

where

`A_r=[4/(2-r)]^(1/r)`.

Optimizing `R0` yields

`sup_t int p0(s)|t-s|^(-1/2) ds <= P(r) M^(r/2)`,

with

`P(r)=4 (2-r)^((r-3)/2) r^(-r/2)`.

Substituting the bound for `M`, using

`(2pi)^(-1/2) alpha_q^(-1/4)=sqrt(e) 2^(-3/4) q^(-1/4)`,

proves the theorem exactly.

## 5. Explicit useful instances

### 5.1 Leverage-compatible rank-two Schur cross block

Take `q=1`, `k=2`, `r=3/2`. If the range leverage of `B` is at most `1/2`, then

`||p_Q||_infinity <= C_2 |d|^(-1/2) E_2(B)^(-1/8)`,

where

`C_2 = 2^(11/4) sqrt(e) 3^(-3/4) sqrt(BETA(1/4,1/8)/2)`
` = 11.67915220701016...`.

If `s_1(B),s_2(B)>=sigma`, then `E_2(B)>=sigma^4`, hence

`||p_Q||_infinity <= 11.680 |d|^(-1/2) sigma^(-1/2)`.

### 5.2 Unconditional rank-three Schur cross block

Take `q=2`, `k=3`, `r=3/2`. No leverage assumption is required, and

`||p_Q||_infinity <= C_3 |d|^(-1/2) E_3(B)^(-1/12)`,

with

`C_3 = 17.315056317897863... < 17.316`.

If `s_1(B),s_2(B),s_3(B)>=sigma`, then `E_3(B)>=sigma^6`, so

`||p_Q||_infinity <17.316 |d|^(-1/2) sigma^(-1/2)`.

Thus a scalar square plus only three aggregate cross directions already closes a branch that direct `L^1` Fourier inversion cannot close from the unconditional exponent.

## 6. Aggregate-minor example showing why this is stronger than paying one minor

For `m` divisible by four, let `U` be the `m x 2` orthonormal frame whose first column is the normalized all-ones vector and whose second column is `+1/sqrt(m)` on the first half and `-1/sqrt(m)` on the second half. Let `V=U` and `B=UV^T`.

Then

- singular values of `B` are exactly `1,1`;
- maximum row leverage of `range(B)` is `2/m <=1/2` for `m>=4`;
- by Cauchy--Binet, `E_2(B)=1`;
- every individual `2x2` physical minor has absolute determinant at most `4/m^2`.

Therefore the new rank-two theorem gives the dimension-free bound

`||p_Q||_infinity <=11.680 |d|^(-1/2)`,

while any route that pays the reciprocal of one selected `2x2` determinant can lose polynomially in `m`.

The exact target-class matrix `diag(d, [[0,B],[B^T,0]])` with `d=1` has nonzero eigenvalues `1,+1,+1,-1,-1`, so this aggregate advantage occurs inside, not outside, the owner's spectral regime.

## 7. Structural application to an original rank-three cross block

Suppose before Schur complementation the physical cross block is `C0=A[I,J]` and `s_3(C0)>=sigma`. For an outside physical pivot `k`, the Schur cross block is a rank-one perturbation

`B=C0-u v^T/d`.

Rank-one singular-value interlacing gives

`s_2(B)>=s_3(C0)>=sigma`.

Hence `E_2(B)>=sigma^4`. Whenever this residual two-dimensional range also has leverage at most one half, the preceding theorem yields

`||p_Q||_infinity <=11.680 |d|^(-1/2) sigma^(-1/2)`.

So the rank-three-cross branch is reduced, after a genuine physical pivot, to the explicitly identified leverage-heavy residual case rather than a tiny-minor problem.

## 8. Exact-rank-three Schur determinant identity

There is a useful exact algebraic identity behind the same mechanism. Let

`A=U Lambda U^T`

have exact rank three with `U^T U=I_3`, choose physical coordinate `k` with `d=A_kk !=0`, and let `ell_k=||U_{k,*}||_2^2`. The Schur complement `S` on the other coordinates has rank at most two. If it has rank two and is written `S=V M V^T`, `V^T V=I_2`, then

`|det M| = |det Lambda| ell_k/|d|`.

Proof: for every pair `i<j`, the principal-minor Schur identity gives

`det A[{k,i,j}] = d det S[{i,j}]`.

Cauchy--Binet gives

`sum_{i<j} |det A[{k,i,j}]| = |det Lambda| ell_k`,

because all rank-three principal minors have sign `sign(det Lambda)` and the squared Plucker coordinates containing row `k` sum to `ell_k`. Likewise all rank-two principal minors of `S` have sign `sign(det M)` and

`sum_{i<j}|det S[{i,j}]|=|det M|`.

Combining the two sums proves the identity.

Thus determinant mass cannot disappear after a nonzero physical pivot; what can still fail is a product-preserving, leverage-compatible coordinate split of that rank-two Schur remainder.

## 9. What remains unpaid

This report does **not** derive a universal scalar pivot plus leverage-compatible Schur cross block from the bare three-large-eigenvalue hypothesis. That extraction is false in simpler forms: the live correction `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE` exhibits exact target matrices whose nonzero pivots leave only rank-one star residuals. The live `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE` also rules out a fixed good principal-minor/rank-three-cross dichotomy.

The first remaining implication for this route is therefore:

`QFORM-PIVOT-AGGREGATE-OR-LOWRANK-BANK-v1` — in the residual low-stable-rank regime, either produce a nonzero physical pivot whose Schur remainder has an `E_k` packet covered above (rank two with leverage margin, or unconditional rank three), or route the matrix into one of the already-proved product-bank/star/hyperbolic-square mechanisms without paying a tiny physical minor.

The full QFORM conjecture remains OPEN. No universal continuity claim is made by the new theorem.

## 10. Numerical/symbolic regression performed

A direct computation checked the explicit constants and the flat-frame example for `m=4,8,16,32`. It returned `E_2(B)=1` to floating precision, maximum `2x2` minor exactly `4/m^2` to floating precision, leverage `2/m`, and constants

- `C_2 = 11.67915220701016...`,
- `C_3 = 17.315056317897863...`.

These checks are regression evidence only; the proof above is analytic.
