# fleet04/B20 — cross-dominated second-Schur-row closure

**Run:** `20260922T172057Z-fleet04-B20-QFORM-r3`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner control revision `2026-09-22.8`  
**Classification:** `ESSENTIAL_STEP_APPLIED / TARGET_LEVEL_BRANCH_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and status

The sole target is the unrestricted quadratic-form conjecture: for every dimension, every independent real input vector whose coordinate densities are bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove that the quadratic form has a universally bounded density, or give a valid counterexample.

This report closes the cross-dominated second-Schur-row branch left by the assigned partner fleet01/B20. It retains arbitrary outside spectrum, arbitrary affine terms created by conditioning, every sign, and arbitrary cap-one coordinate laws. It proves essential boundedness in this branch. It does not prove continuity here, and the full conjecture remains open.

## 2. Source-pinned dependencies

1. **Assigned partner fleet01/B20 r13.** `yspennstate/math-open-problems@f45187170f0d940c8bdc61d095564f92fb749092`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B20/20260922T164728Z-fleet01-B20-QFORM-r13/REPORT.md`. It proves the shared-anchor exterior-square reserve and physical diagonal/cross-cut dichotomy, closes the diagonal-dominated second-row branch, and leaves exactly the cross-dominated alternative.

2. **Cross-bank quarter moment.** fleet01/B19, `yspennstate/math-open-problems@2e5d5cdc3bb7121673bc920497fb11cac9eceb46`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B19/20260922T155027Z-fleet01-B19-QFORM-r11/REPORT.md`. For disjoint original-coordinate banks and cross block of top singular value `sigma`, with arbitrary same-bank quadratic and affine terms,

   `sup_t E|W-t|^(-1/4) <= B sigma^(-1/4)`,

   where `B=(2+sqrt(pi))(4e)^(1/4)`.

3. **Physical three-pivot endpoint.** fleet02/B20, `yspennstate/math-open-problems@2979c262e6ba9c4cef66314aabd714431f5e9c95`. For successive scalar Schur pivots `p1,p2,p3`,

   `||p_Q||_infinity <= C3 (|p1|^4 |p2|^3 |p3|)^(-1/8)`, `C3<94.356`.

4. **Translated quadratic kernel.** The source kernel recorded in `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`, path `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`, states for

   `Psi(u)=1+log(1/|u|)` when `0<|u|<=1` and `Psi(u)=|u|^(-1/4)` when `|u|>=1`,

   that every cap-one density obeys

   `int f(x)|u-x^2|^(-1/2) dx <=8 Psi(u)`.

5. The scalar projection theorem gives density at most `sqrt(2)/||c||` for `c^T Y` when the coordinates of `Y` are independent with density caps one.

No pointwise scalar Fresnel decay, rotated-coordinate independence, moment hypothesis, compact support, or fiber supremum is used.

## 3. Partner setup and the exact unpaid branch

In the partner's minimum-counterexample reduction, after a first physical scalar pivot one has

`|a|>=tau>=1/4`,

and the first Schur complement `S` has two high spectral directions. A physical row `j` selected from that rank-two high window gives

`S=[[d,c^T],[c,C]]`.

All alternatives except the cross-dominated one have already been paid. Thus the only unpaid state is

`||c||_2>|d|`,  `||c||_2>tau/9`.                                      (3.1)

The complete quadratic form, after conditioning on outside original coordinates and completing only physical scalar squares, is allowed to carry arbitrary affine terms. They are retained below.

## 4. Zero second pivot: direct two-kernel closure

### Lemma 4.1

If `X` has density at most one and `m!=0`, then uniformly in `s`,

`E|s-mX|^(-1/2) <=2sqrt(2)|m|^(-1/2)`.                              (4.1)

If `Z` has density at most `H`, then uniformly in `ell`,

`E|2Z+ell|^(-1/2) <=2sqrt(H)`.                                      (4.2)

### Proof

For a cap-`K` probability density, the integral of `|x|^(-1/2)` is maximized by filling the interval of length `1/K` adjacent to the singularity. Its value is `2sqrt(2K)`. Scaling gives (4.1). The variable `2Z+ell` has density cap `H/2`, giving (4.2). QED.

Assume now `d=0`. Write the residual form as

`R=2X_j c^T Y + ell X_j + W(Y)`,

where `W` is an arbitrary quadratic-affine function of the remaining original coordinates. Put `Z=c^T Y`. The scalar projection theorem gives `H<=sqrt(2)/||c||`. Conditioning on `Y`, using (4.1), and then using (4.2),

`sup_t E|t-R|^(-1/2)
 <=2sqrt(2) E|2Z+ell|^(-1/2)
 <=4sqrt(2H)
 <=4*2^(3/4)||c||^(-1/2).`                                         (4.3)

The first scalar pivot supplies

`||p_Q||_infinity
 <=|a|^(-1/2) sup_t E|t-R|^(-1/2)
 <4*2^(3/4)(tau*tau/9)^(-1/2)
 <=48*2^(3/4)<80.727.`                                             (4.4)

The arbitrary contaminant `W(Y)` causes no loss because (4.1) is uniform in its translated target.

## 5. A log-to-quarter transfer

### Lemma 5.1 — `QFORM-LOG-TO-QUARTER-TRANSFER-v1`

Let `W` be any real random variable satisfying

`sup_s E|W-s|^(-1/4) <=L`.                                         (5.1)

Then for every `delta>0`,

`sup_s E Psi((W-s)/delta) <=6 delta^(1/4)L`.                        (5.2)

### Proof

Fix `s` and put `q=W-s`. On `|q|>=delta`,

`Psi(q/delta)=delta^(1/4)|q|^(-1/4)`,

whose expectation is at most `delta^(1/4)L`.

On `|q|<delta`, use

`1+log(delta/|q|)=1+int_0^infinity 1_{|q|<delta exp(-u)} du`.

Markov's inequality applied to (5.1) gives

`P(|q|<r)<=L r^(1/4)`.

Therefore the inside contribution is at most

`delta^(1/4)L + int_0^infinity L delta^(1/4)exp(-u/4)du
 =5 delta^(1/4)L`.

Adding the outside contribution proves (5.2). QED.

This is the missing complete-argument integration step: the cross-bank quarter moment pays both the large residual tail and the logarithmic double-root singularity of the scalar square kernel.

## 6. Nonzero second pivot

Assume `d!=0` and define the second Schur complement

`T=C-cc^T/d`.

The proof of the partner's shared-anchor reserve uses only the rank-two high window, its leakage bound, `P_jj>1/32`, and `d!=0`; it does not use diagonal dominance or a sign condition. Hence it applies unchanged in (3.1):

`|d| s_1(T)>tau^2/64`.                                             (6.1)

The partner's physical diagonal/cut dichotomy therefore gives one of:

`|T_kk|>tau^2/(128|d|)`,                                          (6.2)

or an original-coordinate cut `L union R` with

`sigma=s_1(T[L,R])>tau^2/(256|d|)`.                               (6.3)

### 6.1 Physical diagonal

In (6.2), the successive physical pivots are `a,d,T_kk`. The three-pivot theorem gives exactly the partner estimate

`||p_Q||_infinity<1198.924`.                                      (6.4)

No sign assumption is involved.

### 6.2 Product-preserving cross cut

In (6.3), after completing the `X_j` square, write the remaining quadratic-affine form as `W`. Its cross block between the disjoint original-coordinate banks is `T[L,R]`; arbitrary self blocks and affine terms are allowed. Hence the fleet01/B19 theorem gives

`sup_s E|W-s|^(-1/4) <=B sigma^(-1/4)`,

`B=(2+sqrt(pi))(4e)^(1/4)`.                                      (6.5)

For fixed remaining variables, apply the translated quadratic kernel to `X_j`:

`sup_t E|t-R|^(-1/2)
 <=8|d|^(-1/2) sup_t E Psi((W-t)/|d|)`.                            (6.6)

Lemma 5.1 and (6.5) yield

`sup_t E|t-R|^(-1/2)
 <=48B (|d|sigma)^(-1/4)`.                                        (6.7)

Using the first scalar pivot and (6.3),

`||p_Q||_infinity
 <=48B |a|^(-1/2)(|d|sigma)^(-1/4)
 <192B tau^(-1)
 <=768B
 =5261.066291...`.                                                (6.8)

This is below the partner chain's candidate cap

`C_*=32768sqrt(2)=46340.950012...`.

## 7. Closed branch and remaining target

Equations (4.4), (6.4), and (6.8) exhaust `d=0`, `d!=0` with a physical third pivot, and `d!=0` with a product-preserving cross cut. Thus:

### Theorem 7.1 — `QFORM-CROSS-DOMINATED-SECOND-SCHUR-CLOSURE-v1`

In the fleet01/fleet02 B20 diagonal-dominated first-pivot reduction, every cross-dominated second Schur row satisfying (3.1) has an essentially bounded density, with the uniform branch bound

`||p_Q||_infinity<5262`.

Combined with fleet01/B20 r13, this closes the entire localized second-row alternative of that first-pivot branch.

The unrestricted conjecture is still open. The remaining full-target obligations lie before this branch: the cross-dominated/near-zero outer physical-pivot geometry and the structural passage from the full three-large-eigenvalue hypothesis into one of the now-paid diagonal-first-pivot, ridge-window, grouped-square, or aggregate determinant packets. In the fleet02/B20 full-matrix chain, the explicit O0 singleton-plus-five-bank determinant packet remains unpaid.

Continuity is not proved in this new branch; only absolute continuity and an essential density bound are established.

## 8. Operational note

The current-account native inventory contained the same twenty B01--B20 tasks. Under the create-only 17Z account lease, titles and prompts were reapplied from `prompts/fleet04.json`; readback found 20/20 exact title/prompt matches, enabled, and hourly-valid. Schedules and enablement were not changed. Notification fields were not exposed by the inventory, so no stronger notification claim is made. Native prompt readback is not evidence of later worker adoption.

