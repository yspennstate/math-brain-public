# fleet01/B04 — product rearrangement for a two-zero-diagonal rotated triple

Run: `20260922T124333Z-fleet01-B04-QFORM-r11`  
Programme: `QFORM-DENSITY-3EIG-20260922`, owner control revision `2026-09-22.5`  
Assignment: Product Fourier rearrangement  
Outcome: `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and corrections respected

The full target remains open: for every dimension, every independent real inputs whose one-dimensional densities are bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal essential-supremum bound for the density of `X^T A X`, or construct a valid counterexample. Continuity is a separate stronger requested conclusion.

This report does not use law-uniform pointwise quadratic-phase decay, independence after spectral rotation, a cross minor by itself, unrestricted fiber suprema, or a universal constant `pi`. The current correction inbox was refreshed immediately before publication. In particular, the pointwise Fourier-decay route is known false for arbitrary bounded fragmented densities.

## 2. Compact conditional end-to-end route

The currently proved local mechanisms include:

1. a diffuse rank-three branch using geometric Brascamp--Lieb / Hausdorff--Young when row leverage is controlled;
2. nonzero scalar-pivot Schur mechanisms, including both definite and indefinite binary Schur complements;
3. the all-zero-diagonal pure-cross triple theorem of fleet02/B04.

The first global missing implication is still a product-preserving aggregation theorem converting the sole spectral assumption (three eigenvalues of modulus at least one) into one of these controlled local/aggregate configurations without selecting a dimension-losing tiny principal minor.

The present run closes a useful interpolation gap between items 2 and 3. The nonzero-pivot estimate deteriorates as the pivot tends to zero, while the pure-cross theorem covers exactly zero diagonal. I prove a determinant-scale bound uniform across that transition for every invertible physical `3x3` block with two zero diagonal entries.

## 3. Named OTHER-account result actually applied

I use the completed fleet02/B04 result

`yspennstate/math-open-problems@b7168a1b0b52fbf69705170ff9795435efeb849f`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/fleet02-B04-20260922T122057Z-01c809a1/REPORT.md`.

The precise ingredient applied below is its proved product-density rearrangement bound: if `U,V` are independent with densities at most one, then for `s != 0`,

`p_{UV}(s) <= 4 log(1+1/(2 sqrt(|s|)))`.

Equivalently, for nonzero `c`,

`p_{2cUV}(w) <= (2/|c|) log(1+sqrt(|c|/2)/sqrt(|w|)).`   (3.1)

No pointwise Fourier-decay statement is imported.

## 4. Main theorem

### Theorem — `QFORM-TWO-ZERO-DIAGONAL-DETERMINANT-v1`

Let `X,Y,Z` be independent real random variables with probability densities bounded by one. Let

`B = [[d,a,b],[a,0,c],[b,c,0]]`

be real symmetric and invertible. Put

`Q = d X^2 + 2aXY + 2bXZ + 2cYZ`.

Then `Q` has an essentially bounded density and

`||p_Q||_infinity <= 12 exp(-2/3) |det B|^(-1/3) < 6.162 |det B|^(-1/3).`   (4.1)

More sharply,

`||p_Q||_infinity <= (2/|c|) J(2 |c|^(3/2)/sqrt(|det B|)),`   (4.2)

where

`J(R)=log(1+R)+R log(1+1/R)`.

The same estimates hold after adding arbitrary affine terms in `(X,Y,Z)`. Consequently they also hold conditionally, with the same constant, for an ambient quadratic form after conditioning on every coordinate outside such a physical principal triple.

Only an essentially bounded density is established here. Continuity is not claimed.

### Proof

Since `B` is invertible and the last two diagonal entries vanish, necessarily `c != 0`. The determinant identity is

`det B = c(2ab-dc).`   (4.3)

Condition on `X=x`. Completing the cross product in the original product coordinates gives the exact identity

`Q = 2c (Y+(b/c)x)(Z+(a/c)x) - kappa x^2,`   (4.4)

where

`kappa = 2ab/c-d = det(B)/c^2 != 0.`   (4.5)

For fixed `x`, the translated variables

`Y_x=Y+(b/c)x`, `Z_x=Z+(a/c)x`

remain independent and each retains density cap one. Therefore the fleet02/B04 bound (3.1), applied to the actual conditional density, yields for every real `t`

`p_Q(t)
 <= (2/|c|) integral f_X(x)
      log(1 + A/sqrt(|t+kappa x^2|)) dx,`   (4.6)

with

`A=sqrt(|c|/2)`.

This is the point at which the named partner result enters an actual inequality.

We now integrate the logarithmic singularity by layer cake rather than trying to dominate it pointwise in frequency. For `s>0`,

`log(1+A/sqrt(r)) > s`

is equivalent to

`r < delta_s := A^2/(e^s-1)^2.`   (4.7)

The elementary one-dimensional quadratic sublevel estimate

`|{x : |t+kappa x^2| < delta}|
 <= 2 sqrt(2 delta/|kappa|)`   (4.8)

holds uniformly in `t`. To verify (4.8), scale to `|x^2-u|<epsilon`. If `u>=epsilon`, the total length is

`2(sqrt(u+epsilon)-sqrt(u-epsilon))`,

which decreases in `u` and equals `2 sqrt(2epsilon)` at `u=epsilon`. If `-epsilon<u<epsilon`, the set is centered and has length at most the same quantity. The remaining values of `u` give the empty set.

Since `0<=f_X<=1` and `int f_X=1`, (4.7)--(4.8) imply

`integral f_X(x) log(1+A/sqrt(|t+kappa x^2|)) dx
 <= integral_0^infinity min(1, R/(e^s-1)) ds,`   (4.9)

where

`R = 2 sqrt(2) A/sqrt(|kappa|)
   = 2 |c|^(3/2)/sqrt(|det B|).`   (4.10)

The last integral is exact. Splitting at `s_0=log(1+R)` gives

`integral_0^infinity min(1,R/(e^s-1)) ds
 = log(1+R)+R log(1+1/R)
 = J(R).`   (4.11)

Substitution into (4.6) proves the sharp form (4.2).

It remains to remove the residual dependence on `c`. Put

`P=|det B|`, `u=|c|/P^(1/3)`, `r=2u^(3/2)`.

Then (4.2) becomes

`||p_Q||_infinity
 <= 2^(5/3) P^(-1/3) J(r) r^(-2/3).`   (4.12)

Let `A_0=1+log 2`. For `0<r<=1`,

`J(r)
 = log(1+r)+r log(1+1/r)
 <= r [A_0+log(1/r)].`   (4.13)

Writing `s=r^(1/3)`, the right side of `J(r)r^(-2/3)` is

`s(A_0-3 log s)`.

Its maximum on `(0,1]` is attained at

`s=exp((A_0-3)/3)`

and equals

`3 exp((log 2-2)/3).`   (4.14)

For `r>=1`, use the exact symmetry

`J(r)=r J(1/r)`.

With `s=1/r<=1`, (4.13) gives

`J(r)r^(-2/3)
 <= s^(2/3)[A_0+log(1/s)]
 <= A_0,`   (4.15)

because the displayed function is increasing on `(0,1]`. Since `A_0` is smaller than the value in (4.14), (4.12) gives

`||p_Q||_infinity
 <= 2^(5/3) * 3 exp((log 2-2)/3) P^(-1/3)
 = 12 exp(-2/3) P^(-1/3).`

This is (4.1).

If an affine term `ell^T(x,y,z)+const` is present, invertibility of `B` permits the coordinate translation

`h=(1/2) B^(-1) ell`,

which removes the linear term. Translating the three original coordinates separately preserves their independence and density caps. Conditioning an ambient quadratic form on all outside coordinates creates only such affine and constant terms in this selected triple, so the conditional estimate survives averaging. QED.

## 5. Explicit genuinely rotated indefinite target instance

Take

`B_0=[[-1,1,1],[1,0,1],[1,1,0]].`

Its eigenvalues are exactly

`-sqrt(3), -1, sqrt(3)`,

so all three have modulus at least one and the form is indefinite and genuinely non-diagonal in the independent input coordinates. Here

`Q_0=-X^2+2XY+2XZ+2YZ`, `det B_0=3`.

The sharper bound (4.2), with `c=1`, gives

`||p_{Q_0}||_infinity
 <= 2 J(2/sqrt(3))
 = 2.975932645... .`   (5.1)

The coarser determinant-only theorem gives

`||p_{Q_0}||_infinity <= 12e^(-2/3) 3^(-1/3)=4.271802575...`.

Thus the run supplies the requested explicit estimate for a genuinely rotated indefinite form under completely arbitrary independent input densities bounded by one.

## 6. Integrated Fourier corollary

The result also yields a correction-compatible integrated Fourier estimate. If `M=12e^(-2/3)|det B|^(-1/3)`, then

`||p_Q||_2^2 <= ||p_Q||_1 ||p_Q||_infinity <= M`.

With the convention `phi_Q(t)=int e^(ity)p_Q(y)dy`, Plancherel gives

`int_R |phi_Q(t)|^2 dt = 2pi int_R |p_Q(y)|^2dy`.

Hence

`||phi_Q||_2
 <= sqrt(24pi) e^(-1/3) |det B|^(-1/6)
 < 6.222 |det B|^(-1/6).`   (6.1)

This is an averaged `L^2` Fourier estimate. It is not an `L^1` estimate and does not imply or assert any law-uniform pointwise decay.

## 7. What this pays and what remains

This theorem gives a determinant-scale local bound that is uniform as the lone diagonal entry `d` crosses zero. It therefore bridges the nonzero scalar-pivot and pure-cross regimes on this codimension-two family without paying a factor that blows up like a negative power of `|d|`.

It does not solve the full arbitrary-matrix conjecture. Three large eigenvalues do not presently force one physical triple of this shape with determinant bounded below, nor does a fixed principal-minor selection avoid dimension loss.

The first essential unpaid implication is now:

**`QFORM-NEAR-PURE-CROSS-AGGREGATION-v1`.** Convert the global three-large-eigenvalue condition into a dimension-free aggregate of the already controlled branches (diffuse leverage, scalar-pivot Schur, pure-cross, and the present two-zero-diagonal bridge), or extend the rearrangement argument to quantitatively small/nonzero second and third diagonal entries without introducing a small-pivot loss.

A useful rank-three identity available for such an aggregation remains

`sum_{j<k; j,k!=i} det[u_i,u_j,u_k]^2 = ||u_i||_2^2`

for the rows of an orthonormal `n x 3` frame. The remaining task is to turn this wedge budget into an averaged conditional-density estimate rather than select one potentially tiny minor.

## 8. Status / provenance

- Full target: **OPEN**.
- Result here: **proved supporting theorem**, not independently reviewed yet.
- Continuous density: **not proved here**; only existence of an essentially bounded density.
- Partner result actually consumed: fleet02/B04, full commit `b7168a1b0b52fbf69705170ff9795435efeb849f`, exact report path given above.
- Current control and correction set were refreshed before this publication.
- Changed-file privacy review: this report contains only mathematical statements, public-style theorem metadata, repository commit identifiers, and no credentials, scheduler IDs, machine paths, unrelated private data, or private source excerpts. No external secret-scanner runtime was invoked; the fallback was an explicit manual review of this single-file allowlist.
- No email, Drive action, public release, paid model/API/Codex call, remote workflow, scheduler mutation, notification change, or permission expansion was performed.
