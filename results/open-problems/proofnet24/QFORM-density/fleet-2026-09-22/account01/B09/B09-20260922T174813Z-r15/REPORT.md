# B09 QFORM r15 — exact Schur singular-value inheritance and pivot routing

Programme: `QFORM-DENSITY-3EIG-20260922`  
Logical worker: `account01/B09`  
Run: `B09-20260922T174813Z-r15`  
Outcome: **ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN**  
Execution context: **WITHOUT_VERIFIED_BRAIN**

## 1. Full target and current conditional proof

The full target remains: for independent real coordinates with densities bounded by one and every real symmetric `A` having at least three eigenvalues of modulus at least one, prove a universal `L^infinity` density bound for `Q=X^T A X`, with continuity tracked separately.

This run attacks the first structural implication in the heavy-physical-pivot branch. The key point is that scalar Schur completion loses **no singular-value scale at all** in the sense relevant to the third spectral direction. This removes a condition-number loss used in earlier heavy-pivot routing.

Dependencies actually used:

1. account02/B09 `QFORM-PIVOT-OFFDIAG-STABLERANK-v1`, canonical source `yspennstate/math-open-problems@77d71ed8bbd7f8a3fd40958e54b5bf658163c27a`, which states for a physical pivot `a!=0`, Schur complement `S`, `s=||S||_op`, and `S^o=S-diag(S)`, if
   
   `||S^o||_F^2 >= 24 s^2`,
   
   then
   
   `||p_Q||_infinity <= 11.876 / sqrt(|a| s)`.

2. account02/B09 `QFORM-ZERODIAG-TRIANGLE-LOGSMOOTH-v1`, canonical source `yspennstate/math-open-problems@1abb65eef22eb44be26d8b21dd5c7174fba4aa1`, which states that if a zero-diagonal physical triple in a quadratic form has edge product `tau=|abc|>0`, then the residual quadratic form has density at most
   
   `(3+log 8) tau^(-1/3)`.

3. account03/B20 `QFORM-NESTED-CUT-THREE-RESOURCE-v1`, canonical source `yspennstate/math-open-problems@06ef7346c08f41c3fac240e1acdeb1b42dc2995d`, whose current heavy-pivot branch supplies a physical pivot of size at least `157/320` in one unresolved case.

No pointwise quadratic-phase decay, post-rotation independence, conditional projection-density cap, or fixed-small-minor dichotomy is used.

## 2. Exact theorem: Schur singular-value inheritance

### Theorem `QFORM-SCHUR-SINGULAR-INHERITANCE-v1`

Let

`A = [[a,b^T],[b,C]]`

be real symmetric with `a!=0`, and let

`S = C - b b^T/a`

be the physical scalar Schur complement. Write singular values in decreasing order. Then for every `1<=j<=n-1`,

` s_{j+1}(A) <= s_j(S). `

In particular, if `s_3(A)>=1`, then

` s_2(S)>=1 `

for **every** nonzero physical pivot, with no hypothesis whatsoever on `||b||/|a|`.

### Proof

Set `v=(a,b)^T`. Then the scalar completion identity is

` A = (1/a) v v^T + (0 direct_sum S). `

The first summand has rank one. For singular values, the Weyl/Ky-Fan inequality

` s_{p+q-1}(X+Y) <= s_p(X)+s_q(Y) `

with `X=0 direct_sum S`, `Y=(1/a)vv^T`, `p=j`, `q=2` gives

` s_{j+1}(A) <= s_j(0 direct_sum S)+s_2((1/a)vv^T) = s_j(S). `

This proves the claim.

### Iterated form

If `m` successive scalar Gaussian-elimination pivots are nonzero and `S_m` is the resulting nested Schur complement, then induction gives

` s_{j+m}(A) <= s_j(S_m). `

Thus every completed physical square can spend at most one singular direction. No congruence-condition-number estimate is needed for this counting statement.

## 3. Direct application of the assigned partner theorem

Assume the target hypothesis `s_3(A)>=1`, choose any physical pivot `a!=0`, and form `S`. By the theorem above,

`||S||_op >= s_2(S)>=1`.

If the account02/B09 stable-rank hypothesis

`||S-diag(S)||_F^2 >=24 ||S||_op^2`

holds, then its proved theorem gives

`||p_Q||_infinity <= 11.876 / sqrt(|a| ||S||_op)`

and hence the strictly stronger target-level consequence

`boxed: ||p_Q||_infinity <= 11.876 |a|^(-1/2).`

This removes the earlier auxiliary requirement `|a|>=||b||_2` and removes the earlier Schur spectral loss `2/(3+sqrt(5))`.

On the current account03/B20 heavy-pivot threshold

`|a|>=157/320`,

the whole high-Schur-stable-rank subbranch is therefore paid by

`boxed: ||p_Q||_infinity < 11.876 sqrt(320/157) <16.955.`

For the older `|a|>=1/312` threshold the same argument gives `<209.772` without any condition on the pivot row norm.

This is an `O(|I|)` interval bound immediately:

`P(Q in I) <= 16.955 |I|`

on the `157/320` branch. The cited stable-rank theorem supplies the bounded density; continuity is not added here.

## 4. A new exact local routing consequence

Let `D=diag(S)`, `H=S-D`, and

`d=||D||_op=max_i |S_ii|`.

Since `s_2(S)>=1`, singular-value perturbation gives

` s_2(H) >= 1-d. `

Therefore either

1. `d>=1/2`, so there is a second genuine physical scalar pivot in the Schur complement of size at least `1/2`; or
2. `d<1/2`, in which case `s_2(H)>1/2`.

For case 2, take a random Rademacher diagonal matrix `R` and define

`K=(H-RHR)/2`.

Because `H` has zero diagonal, `E K=H/2`. After permuting coordinates according to the random sign cut,

`K=[[0,C],[C^T,0]]`.

The Ky-Fan four-norm is convex, hence

`E ||K||_(4) >= ||E K||_(4)= (1/2)||H||_(4) >= s_2(H)`.

But

`||K||_(4)=2(s_1(C)+s_2(C))`.

Consequently some physical cut obeys

`boxed: s_1(C)+s_2(C) >= s_2(H)/2 >= (1-d)/2.`

In particular, when `d<1/2`, some cut has

` s_1(C)+s_2(C)>1/4. `

Thus either

` s_2(C) >= (1-d)/8 `

or

` s_1(C) > 3(1-d)/8. `

This gives an exact pivot-or-two-cross-or-one-strong-cross routing statement **inside every nonzero-pivot target Schur complement**. It is a structural implication only; the one-strong-cross branch still needs a genuinely independent third smoother, and arbitrary extra same-bank curvature cannot be discarded.

## 5. Application of the latest account02/B09 zero-diagonal triangle theorem

The preceding outer scalar pivot also gives a clean way to consume the partner's newest triangle theorem.

Suppose the Schur residual `S` has a physical zero-diagonal triple with edge product

`tau=|S_ij S_ik S_jk|>0`.

Let `Z=Y^T S Y`. By account02/B09,

`||p_Z||_infinity <= M := (3+log 8) tau^(-1/3).`

After completing the outer scalar pivot,

`Q=a(X+m(Y))^2+Z`,

where `m(Y)` may depend arbitrarily on all residual coordinates. Conditional on `Y`, the square pushforward obeys

`p_{Q|Y}(t) <= |a|^(-1/2) |t-Z|^(-1/2)`.

For every one-dimensional probability density `p<=M`, rearrangement around the singularity gives

`sup_t int |t-z|^(-1/2) p(z) dz <= 2 sqrt(2M)`.

Therefore

`boxed: ||p_Q||_infinity <= 2 sqrt(2(3+log 8)) |a|^(-1/2) tau^(-1/6).`

Numerically the prefactor is `<6.375`. This remains valid with a fully correlated completed-square center `m(Y)`; no independence between `m(Y)` and `Z` is used.

This pays a concrete zero-diagonal-triangle subbranch of the new Schur routing while preserving all original-coordinate product structure.

## 6. Compact conditional end-to-end route after this run

For any target matrix with a physical pivot `|a|>=157/320`:

1. Schur completion leaves a residual `S` with `s_2(S)>=1` exactly.
2. If `||S^o||_F^2>=24||S||_op^2`, the account02/B09 theorem plus Step 1 gives `||p_Q||_infinity<16.955`.
3. Otherwise, if `max_i|S_ii|>=1/2`, take a second scalar pivot; the iterated inheritance theorem guarantees the next Schur remainder still has operator norm at least one.
4. If all `|S_ii|<1/2`, a physical cut has `s_1+s_2>1/4`; hence either a two-cross-direction resource or one strong cross direction is present.
5. In the zero-diagonal triangle subcase, the newest account02/B09 logarithmic smoother plus the outer square gives the explicit `<6.375 |a|^(-1/2) tau^(-1/6)` endpoint above.

The first unpaid implication is therefore narrower than before:

`QFORM-SCHUR-HALFRIESZ-TWO-LARGE-v1` — prove a universal translation-uniform half-Riesz estimate for an arbitrary residual quadratic form `Y^T S Y` under only `s_2(S)>=1`, or finish the exact routing of the low-stable-rank alternatives (second scalar pivot / two-cross cut / one-strong-cross plus nested resource) into already-proved product-preserving smoothers.

If `QFORM-SCHUR-HALFRIESZ-TWO-LARGE-v1` were proved with constant `C_{1/2}`, then every target matrix with physical pivot `|a|>=alpha` would immediately satisfy

`||p_Q||_infinity <= C_{1/2}/sqrt(alpha)`

by scalar completion. The remaining global issue would then be the zero/near-zero physical-pivot branch.

## 7. Integrity and status

The full QFORM conjecture is **not proved** here. The new singular-value inheritance theorem is exact and dimension-free; the density conclusions are only those obtained after applying already-proved partner hypotheses or the stated triangle subcase. No claim is made that every low-stable-rank Schur complement automatically falls into one of the paid endpoints.

Essential boundedness is proved on the paid subbranches above. Continuity is not newly proved by this report.
