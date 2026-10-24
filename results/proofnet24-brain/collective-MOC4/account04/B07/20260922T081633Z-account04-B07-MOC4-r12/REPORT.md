# account04/B07 MOC4 report — Spin(6) cofactor-deficit constraint

Run: `20260922T081633Z-account04-B07-MOC4-r12`  
Status: `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / not proved / not disproved**.  
Execution status: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## Exact target and assignment

Target: for all complex normal `4 x 4` pairs `A,B` with spectra `a_i,b_i`, prove

`det(A+B) in conv{prod_i (a_i+b_{sigma(i)}): sigma in S_4}`,

including singular and repeated-spectrum cases. This report works only on the `n=4` problem.

Assignment: attack the shared mixed-minor constraint by representation theory / exterior algebra, without assuming an unproved positive common lift.

## Fresh source state consumed

The latest complete team-lead report visible during this run is:

- account03/B07, run `20260922T060726Z-account03-B07-MOC4-r11`;
- path `proofnet24/collective-MOC4/account03/B07/20260922T060726Z-account03-B07-MOC4-r11/REPORT.md`;
- source read at main commit `86ebffd8566c6594c03aeb66f5a209e076098aee`;
- source blob `3c11567e275d39376f217a9b9e3c10693efa3127`;
- named result consumed: `MOC4-SPIN4-SATURATION-TO-ZERO-FACE-v1`.

That result proves that saturation of a genuine mixed Spin(4) Hessian gate at a global support maximizer produces an exactly support-flat genuine coordinate `SU(2)` orbit and hence an equal-support representative with a zero entry. It does **not** by itself prove the zero-entry face safe; its report explicitly leaves the zero-face support inequality and the strictly curved interior branch unpaid. I therefore use it only for the legitimate dichotomy: a positive-gap maximizer is either reducible to the zero face through such a saturation, or it lies on the strict-curvature branch.

This satisfies the required named OTHER-account consumption. The newest visible account01/B08 roots inspected during the run did not yet expose a newer complete proof report, so no unsupported partner theorem is attributed here and the run did not wait.

## Exterior-square setup

Use the exceptional isomorphism underlying the campaign. For the real exterior-square action

`O = Lambda^2 U in SO(6)`

choose an orthogonal complex structure `R^6 ~= C^3` and write the real orthogonal map as

`T(z) = M z + N conjugate(z)`, with `M,N in M_3(C)`.

Real orthogonality is equivalent to

`M M* + N N* = I`,  
`M N^T + N M^T = 0`.

The anti-linear block `N` is the orientation-mixing part. The quantities

`q^-_{alpha beta} = |n_{alpha beta}|^2`

are precisely the anti-conformal block masses in this gauge.

## New exact theorem

### `MOC4-SPIN6-COFACTOR-DEFICIT-v1`

For every `O in SO(6)` written as above, there is a scalar `lambda in [0,1]` such that the singular values of `N` are

`(sqrt(lambda), sqrt(lambda), 0)`.

Equivalently, there are unit vectors `v,w in C^3` with

`N N* = lambda (I - v v*)`,  
`N* N = lambda (I - w w*)`.

Define

`r_alpha = sum_beta |n_{alpha beta}|^2`,  
`c_beta  = sum_alpha |n_{alpha beta}|^2`.

Then

`sum_{alpha,beta} |n_{alpha beta}|^2 = 2 lambda`

and, for every row `alpha` and column `beta`,

`|cof_{alpha beta}(N)|^2 = (lambda-r_alpha)(lambda-c_beta)`.        (CF)

In expanded complementary-minor form, if `{gamma,eta}` are the other two rows and `{delta,zeta}` the other two columns,

`| n_{gamma delta} n_{eta zeta} - n_{gamma zeta} n_{eta delta} |^2`
`= (lambda-r_alpha)(lambda-c_beta)`.

Consequently, the phase-free masses satisfy all nine exact interval constraints

`(sqrt(q^-_{gamma delta} q^-_{eta zeta}) - sqrt(q^-_{gamma zeta} q^-_{eta delta}))^2`
`<= (lambda-r_alpha)(lambda-c_beta)`
`<= (sqrt(q^-_{gamma delta} q^-_{eta zeta}) + sqrt(q^-_{gamma zeta} q^-_{eta delta}))^2`.     (PF)

These are genuine same-Spin(6)-point constraints. They are not positivity of an auxiliary lift.

### Proof

First work on the open chart `det M != 0` and put `Z=M^{-1}N`. The second orthogonality relation gives

`0 = M N^T + N M^T = M (Z^T+Z) M^T`,

hence `Z^T=-Z`.

Every complex `3 x 3` skew-symmetric matrix has singular values `(t,t,0)` for some `t>=0` (unitary congruence puts it into one `2 x 2` skew block plus zero). The first orthogonality relation becomes

`M (I+Z Z*) M* = I`.

Thus `M=V(I+ZZ*)^{-1/2}` for a unitary `V`, and

`N = V(I+ZZ*)^{-1/2} Z`.

Using the push-through identity, the eigenvalues of `N*N` are

`t^2/(1+t^2), t^2/(1+t^2), 0`.

Set `lambda=t^2/(1+t^2)`. Therefore the singular values of `N` are `(sqrt(lambda),sqrt(lambda),0)`.

The chart `det M != 0` is dense in `SO(6)`: `det M` is a real-analytic function on connected `SO(6)` and is nonzero at the identity, so its zero set has empty interior. Singular values depend continuously on the matrix entries. Hence the same singular-value conclusion extends to all `O in SO(6)`, including the singular chart.

Choose unit left/right kernel vectors `v,w`. The spectral form gives

`NN*=lambda(I-vv*)`, `N*N=lambda(I-ww*)`.

Hence

`lambda-r_alpha = lambda |v_alpha|^2`,  
`lambda-c_beta  = lambda |w_beta|^2`.

For rank two, `adj(N)` has rank one and its sole nonzero singular value equals the product of the two nonzero singular values of `N`, namely `lambda`. Since its columns lie in the right kernel and its rows in the left kernel,

`adj(N) = lambda e^{i theta} w v*`

for some phase. Because `adj(N)_{beta alpha}=cof_{alpha beta}(N)`,

`|cof_{alpha beta}(N)|^2`
`= lambda^2 |v_alpha|^2 |w_beta|^2`
`= (lambda-r_alpha)(lambda-c_beta)`.

If `rank N<2`, then `lambda=0` and both sides vanish, so (CF) holds there too. The interval (PF) is the triangle/reverse-triangle inequality applied to the two products in the complementary `2 x 2` determinant.

This proves the theorem.

## Immediate quantitative collar

A useful equivalent one-sided consequence is

`|sqrt(q^-_{gamma delta}q^-_{eta zeta}) - sqrt(q^-_{gamma zeta}q^-_{eta delta})|`
`<= sqrt((lambda-r_alpha)(lambda-c_beta))`.

Thus whenever a row or column approaches the maximal anti-linear mass `lambda`, the opposite `2 x 2` block is forced toward determinant cancellation. In particular, if either `r_alpha=lambda` or `c_beta=lambda`, the complementary `2 x 2` minor of `N` vanishes exactly.

This is the first concrete exterior-algebra "payment" extracted from the rank-two parity mask: concentration of anti-linear mass is not free; it forces complementary-minor degeneracy.

## Decisive strict-cut witness against the old mass/two-rook relaxation

Consider the nonnegative mass matrix

`S = diag(1, 1/2, 1/2)`.

It has total mass `2`, every row/column sum is at most `1`, and it is explicitly in the two-rook convex hull:

`S = (1/2) diag(1,1,0) + (1/2) diag(1,0,1)`.

Thus the usual mass-only/two-rook constraints accept it.

If it were `q^-=|N|^2` for a genuine Spin(6) point, total mass `2` would force `lambda=1`. For `alpha=beta=1`, the row and column sums equal `1`, so the right side of (CF) is zero. But the complementary `2 x 2` block has diagonal magnitudes `1/sqrt(2),1/sqrt(2)` and zero cross entries; therefore its determinant has squared modulus exactly `1/4` for every choice of phases. Contradiction.

So the cofactor-deficit identities strictly cut the natural two-rook/mass relaxation. This is a counterexample to that **relaxation mechanism only**, not a counterexample to MOC4.

## Exact computation

`verify_cofactor_deficit.py` uses exact SymPy rational arithmetic. It constructs a generic rational `O in SO(6)` as a product of eight rational Givens rotations, converts its `2 x 2` real blocks into the `(M,N)` decomposition, and verifies:

- `O^T O=I`, `det O=1`;
- both real-orthogonality identities for `M,N`;
- `rank N=2`, `det N=0`;
- `charpoly(NN*) = t*(4167516340*t-3653361019)^2/17368192444166995600`;
- `lambda=3653361019/4167516340`;
- all nine cofactor-deficit identities exactly;
- the two-rook decomposition of `S`;
- its cofactor lower bound `1/4` versus deficit product `0`.

The exact stdout is preserved in `verify_cofactor_deficit.out`.

## Compact conditional end-to-end argument

Fix a support direction. A MOC4 violation would have a positive-gap genuine global maximizer `U_*`.

1. By the team lead's `MOC4-SPIN4-SATURATION-TO-ZERO-FACE-v1`, if a genuine mixed Spin(4) gate saturates, there is an equal-gap zero-entry representative. This reduces that branch to the still-unpaid zero-face inequality; it does not silently declare it solved.
2. Otherwise the maximizer lies on the strict mixed-Spin(4)-curvature branch.
3. In every exterior-square complex gauge used for the mixed-minor analysis, the same genuine point has an anti-linear block `N` obeying the exact nine equations (CF), and hence the phase-free collars (PF).
4. Therefore any relaxation used to prove the zero-face or strict-curvature branch must preserve these cofactor deficits; the explicit matrix `S` proves that row/column mass, total mass and two-rook membership alone are insufficient.

The first essential missing implication is now the source-valid statement

`MOC4-STRICT-CURVATURE-COFACTOR-PAYMENT-v1`:

> At a positive-gap global support maximizer on the strict Spin(4)-curvature branch, combine the six genuine Spin(4) curvature reserves with the gauge-conjugate cofactor-deficit identities (CF) and the same-unitary exterior-minor relations to pay every possible support excess over the 24 endpoint support values.

This implication is **not proved here**. The present run supplies a new exact nonlinear constraint and a strict counterexample to the weaker mass/two-rook substitute, so it materially narrows what a valid proof of that implication may use.

For the saturated branch, the corresponding boundary task remains the lead's zero-face support problem; the cofactor collar is available there as an additional exact constraint but is not claimed to close it.

## Failure / non-claims

- No full proof of MOC4 is claimed.
- No MOC4 counterexample is claimed.
- No universal positive `S_4` lift is assumed or recovered.
- The explicit `S` witness is not asserted to arise from a unitary; the point is exactly that the new theorem excludes it.
- The lead's zero-entry reduction is not misreported as a proof of the zero-face inequality.
- No claim depends on a literature search miss.
- Singular and repeated spectra are not removed from the target; no division by spectral gaps occurs in the new Spin(6) theorem.

## Verdict

`ESSENTIAL_STEP_APPLIED`.

The new result upgrades the anti-linear rank-two condition to an exact nine-equation cofactor-deficit system and proves that a natural two-rook relaxation used in earlier exterior-algebra approaches is strictly too large. The remaining target-level obstruction is the quantitative combination of these exact same-unitary constraints with the campaign's strict Spin(4) Hessian reserves (and, on the saturated branch, the zero-face support inequality).
