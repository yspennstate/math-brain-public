SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B06, 2026-09-22T21:05:04Z.
attacking: the near-rank-two / grouped-coordinate branch after the curved-fiber aggregate split; replace reciprocal fiber suprema by an averaged two-dimensional product projection, and test whether small opposite-side curvature can be perturbative.

# fleet02/B06 — one-sided nonlinear hyperbolic smoother and a two-sided perturbation obstruction

**Run:** `b06-20260922T210504Z-abc2116c80c5`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Curved fiber integration / GEOMETRY  
**Classification:** `ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED`  
**Full target:** OPEN / NOT PROVED / NOT DISPROVED  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 0. Controls, exact scope, and source pins


Target quantifiers are unchanged: the original coordinates are independent, each one-dimensional density is at most one, and the symmetric matrix has at least three eigenvalues of absolute value at least one. No moment, support, identical-law, diagonal-basis, or post-rotation-independence assumption is added.

Source-valid inputs actually used:

1. **Weighted affine-fiber projection theorem** `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, fleet02/B06 canonical report `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`. If `R` has `k` orthonormal columns and `X` is a cap-one product vector, then `R^T X` has density at most `exp(k/2)`. In particular a unit scalar projection has density at most `sqrt(e)` and a two-dimensional orthogonal projection has density at most `e`.

2. **Named partner fleet03/B06 r18**, corrected bundle commit `fc92e85ebc8099f25a9770d81348d74d5d2aa4d5`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260922T201841Z-fleet03-B06-qform-r18/REPORT.md`. Its `QFORM-ONE-ROW-E2-HYBRID-L3-v1` and near-coloop application give: at `g=gamma/16`, with `Z=H(g^2I+H^TH)^(-1/2)`, `theta=||Z||_F^2>=256/129`; if `eta=E_2(Z_0)>=1/64`, the post-pivot law has density `<72/sqrt(|a| gamma)`. If `eta<1/64`, then `Z` lies within squared Frobenius distance `<129/4064` of rank at most two. The same source records the dependence-safe square-kernel inequality used below.

No source-reported theorem is promoted beyond its stated scope.

## 1. A two-dimensional reciprocal lemma with the probability weight kept inside

### Lemma 1 — reciprocal radius under a planar density cap

If `Y in R^2` has probability density `rho<=M`, then for every `y0`,

`E[1/||Y-y0||] <= 2 sqrt(pi M)`.                                      (1.1)

**Proof.** By layer cake,

`E[1/||Y-y0||] = integral_0^infinity P(||Y-y0||<1/t) dt`.

The probability in the integrand is at most `min(1, M pi/t^2)`. Splitting at `t=sqrt(pi M)` gives exactly `2 sqrt(pi M)`. QED.

This is the weighted replacement for the invalid operation `integral sup_fiber`: the singular reciprocal factor is integrated against the genuine two-dimensional projected probability law before any supremum is taken.

## 2. Main theorem: arbitrary nonlinear curvature on one product bank

### Theorem 2 — `QFORM-ONE-SIDED-RANK2-CROSS-SMOOTHER-v1`

Partition original coordinates into disjoint sets `I,J,K`. Let `X_I,X_J,X_K` be the corresponding independent product banks, all coordinate densities bounded by one. Let the conditional quadratic form after fixing `X_K=k` be

`R_k = F_k(X_I) + 2 X_I^T H X_J + b_k^T X_J + c_k`,                 (2.1)

where `F_k` is **arbitrary measurable** (in particular it may contain arbitrary quadratic and affine terms on the whole `I` bank), `H` is fixed, and the `J` bank has no quadratic self-term. If the second singular value of `H` is

`s_2(H)=sigma>0`,

then the unconditional law has an essentially bounded density and

`boxed( ||p_R||_infinity <= e sqrt(pi) / sigma ).`                    (2.2)

Equivalently, for a full ambient symmetric matrix, if some original-coordinate bank `J` has principal block `A_JJ=0` and the cross block `A_IJ` has second singular value at least `sigma`, then (2.2) holds after conditioning all remaining original coordinates. Arbitrary `A_II`, `A_IK`, `A_JK`, `A_KK` are allowed.

### Proof

Fix `k`; the bound below is uniform in `k`. Take an SVD

`H = U diag(s_1,s_2,...) V^T`, `s_1>=s_2=sigma>0`.

Let `U_2,V_2` denote the first two singular-vector columns and put

`Y=U_2^T X_I in R^2`.

By the weighted affine-fiber theorem, `Y` has density at most `e` even though its two coordinates need not be independent.

Condition now on the **entire original bank** `X_I=x`. The term `F_k(x)` is only a shift. The remaining random term in the genuine independent `J` bank is the scalar linear projection

`a(x)^T X_J`, `a(x)=2H^T x+b_k`.                                    (2.3)

For `a!=0`, the scalar `k=1` projection theorem gives conditional density at most

`sqrt(e)/||a(x)||`.                                                   (2.4)

Projecting the coefficient onto the first two right singular directions cannot increase its norm:

`||a(x)|| >= ||V_2^T a(x)||
            = ||2 diag(s_1,s_2) Y + beta||`,
 beta=V_2^T b_k.                                                       (2.5)

Set `y0=-(1/2)diag(s_1,s_2)^(-1) beta`. Then

`||a(x)|| >= 2 sigma ||Y-y0||`.                                      (2.6)

The exceptional set `a=0` has probability zero because (2.6) forces the absolutely continuous two-dimensional variable `Y` to equal one point. Averaging the conditional densities and applying Lemma 1 with `M=e`,

`p_R(t|k)
 <= sqrt(e)/(2sigma) E[1/||Y-y0||]
 <= sqrt(e)/(2sigma) * 2 sqrt(pi e)
 = e sqrt(pi)/sigma`.                                                 (2.7)

The bound is uniform in `k`, so averaging over the outside bank proves (2.2). QED.

### What is new in the scope

No physical pair is selected and no reciprocal minor is paid. Extra singular directions of `H` are harmless: after SVD their right singular directions are orthogonal to the two directions retained in (2.5), so they cannot cancel the controlling two-dimensional coefficient. More importantly, **all same-side nonlinear terms on the `I` bank survive unchanged**, because we condition on the entire original bank and average only the moving linear coefficient against the two-dimensional product-derived projection law.

## 3. Applying the named partner result: complete the eta split when the opposite self-block vanishes

Use the exact fleet03/B06 r18 near-coloop state. Its large-aggregate branch is already a real inequality:

`eta>=1/64  ==>  ||p_Q||_infinity <72/sqrt(|a| gamma).`              (3.1)

Now suppose `eta<1/64`. The partner gives a rank-at-most-two approximation to `Z` with squared Frobenius error

`tau < 129/4064`.                                                     (3.2)

By Eckart--Young,

`sum_(r>=3) s_r(Z)^2 <129/4064`.                                      (3.3)

Every singular value of

`Z=H(g^2I+H^TH)^(-1/2)`

is strictly below one. Since `||Z||_F^2>=256/129`,

`s_2(Z)^2
 = ||Z||_F^2-s_1(Z)^2-sum_(r>=3)s_r(Z)^2
 > 256/129 -1-129/4064
 = 499487/524256.`                                                     (3.4)

Set

`c0=sqrt(499487/524256)>0.976091183264`.                              (3.5)

Writing `B=(g^2I+H^TH)^(1/2)`, one has `H=ZB` and `B^2>=g^2 I`. Hence

`HH^T=ZB^2Z^T >= g^2 ZZ^T`,

so by eigenvalue monotonicity

`s_2(H)>=g s_2(Z)>c0 g`.                                               (3.6)

Therefore, **if the opposite (`J`) Schur self-block in this r18 residual is zero**, Theorem 2 applies to the residual law and gives, using `g=gamma/16`,

`||p_R||_infinity
 < e sqrt(pi)/(c0 g)
 = [16 e sqrt(pi)/c0]/gamma
 < 78.977/gamma.`                                                      (3.7)

The dependence-safe square kernel recorded in the partner proof says

`p_Q(t)<=|a|^(-1/2) integral_0^infinity p_R(t-sgn(a)u) u^(-1/2)du`.   (3.8)

For any probability density `h<=M`, splitting at `rho` gives

`integral_0^infinity h(t-u)u^(-1/2)du <=2M sqrt(rho)+rho^(-1/2)`.

At `rho=(2M)^(-1)` this is `2sqrt(2M)`. With (3.7),

`boxed( ||p_Q||_infinity <25.136/sqrt(|a| gamma) )`                    (3.9)

in the `eta<1/64` branch.

Combining (3.1) and (3.9) yields the conditional end-to-end closure

`boxed( ||p_Q||_infinity <72/sqrt(|a| gamma) )`                       (3.10)

for the entire partner near-coloop `eta` split **whenever the opposite residual physical bank has zero quadratic self-block**. This directly applies the named partner result rather than merely citing it.

## 4. Exact adversary: small opposite-side curvature is not perturbative

A tempting repair is to replace `A_JJ=0` in Theorem 2 by `||A_JJ||` small. That statement is false even with a perfectly conditioned cross block.

### Construction — `QFORM-TWO-SIDED-SMALL-CURVATURE-PERTURBATION-FALSE-v1`

Fix `0<epsilon<1`. Let `U_1,U_2,V_1,V_2` be independent `Uniform[-1/2,1/2]`. Define

`R_epsilon
 =2 epsilon^(-2) U_1U_2
  +2(U_1V_2+U_2V_1)
  +2 epsilon^2 V_1V_2`                                                (4.1)

so that

`R_epsilon=2(U_1/epsilon+epsilon V_1)(U_2/epsilon+epsilon V_2)`.       (4.2)

In the `I=(U_1,U_2)`, `J=(V_1,V_2)` block decomposition,

`H=[[0,1],[1,0]]`, so `s_2(H)=1`,                                  (4.3)

whereas

`A_JJ=epsilon^2 [[0,1],[1,0]]`, so `||A_JJ||_op=epsilon^2 ->0`.       (4.4)

Nevertheless `R_epsilon` has **unbounded density** at zero. Indeed put

`S_i=U_i/epsilon+epsilon V_i`.

The two `S_i` are independent. The density `h_epsilon` of `S_i` is the convolution of a uniform density `epsilon` on an interval of length `1/epsilon` and a uniform density `1/epsilon` on an interval of length `epsilon`. Hence on the nonempty central plateau

`|s| <= r_epsilon=(epsilon^(-1)-epsilon)/2`

one has exactly `h_epsilon(s)=epsilon`. For `0<|z|<r_epsilon^2`, the product-density formula gives

`p_(S_1S_2)(z)
 = integral h_epsilon(x)h_epsilon(z/x) dx/|x|
 >= epsilon^2 integral_(|z|/r_epsilon)^r_epsilon dx/x
 = epsilon^2 log(r_epsilon^2/|z|) ->infinity`.                        (4.5)

Since `R_epsilon=2S_1S_2`, its essential density supremum is infinite.

The coefficient matrix factors as `A=l_1 l_2^T+l_2 l_1^T` with

`l_1=(epsilon^(-1),0,epsilon,0)`,
`l_2=(0,epsilon^(-1),0,epsilon)`.

Thus its only nonzero eigenvalues are

`+/- (epsilon^(-2)+epsilon^2)`.

So this is **not** a counterexample to QFORM (it has only two nonzero eigenvalues). It is an exact source-valid falsifier of the perturbative intermediate claim. Arbitrarily small opposite-side self-curvature can cooperate with arbitrarily large same-side curvature to recreate the rank-two logarithmic singularity while the cross block stays uniformly conditioned.

## 5. Consequence for the full proof route

The first unpaid implication is now narrower:

`QFORM-TWO-SIDED-CURVATURE-ABSORPTION-v1` — in the small-`eta` near-rank-two survivor, structurally spend the nonzero opposite-side Schur curvature through a genuine original-coordinate square/pair/half-Riesz payment, or build a two-sided weighted product estimate that keeps both banks simultaneously. **Operator-norm smallness of that self-block is not a valid perturbative bridge**, by Section 4.

A compact conditional proof skeleton is therefore:

1. use existing pair/ridge/scalar-pivot reductions to reach the fleet03/B06 r18 near-coloop state;
2. if `eta>=1/64`, apply the partner bound (3.1);
3. if `eta<1/64`, the normalized cross matrix has `s_2(Z)>c0` by (3.4), not merely abstract closeness to rank two;
4. if one side is quadratically null, Theorem 2 plus the physical square kernel closes with (3.9);
5. otherwise the surviving debt is genuinely two-sided curvature, and Section 4 forbids simply discarding it as a small perturbation.

This is progress on the exact full-target reduction, not a full proof.

## 6. Exact check

A deterministic rational checker in this run verifies the exact constant in (3.4), the epsilon=1/8 adversary factorization/eigenvalues, the perfectly conditioned cross block, and the small opposite block. Its output records

- `c0^2 = 499487/524256`, `c0 = 0.976091183265`;
- residual coefficient `16 e sqrt(pi)/c0 = 78.976705083389`;
- square-smoothed coefficient `25.135903418559`;
- at `epsilon=1/8`, nonzero eigenvalues `+/-4097/64`, `s_2(H)=1`, and `||A_JJ||=1/64`.

The checker is confirmatory only; the proofs above are analytic.

## 7. Status and next action

**Status:** `ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED`. Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED. Continuity is not established here.

**Next action:** attack `QFORM-TWO-SIDED-CURVATURE-ABSORPTION-v1` using a product-preserving physical square or indefinite-pair extraction before any norm-small perturbation. The exact adversary shows why a generic stability-in-`A_JJ` argument cannot be the missing step.
