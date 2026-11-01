# fleet01/B05 — a universal integrable pointwise radial envelope is impossible

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T205545Z-fleet01-B05-QFORM-r19`  
**Assignment:** quadratic coarea bound  
**Outcome:** `ESSENTIAL_STEP_APPLIED / REFUTED_INTERMEDIATE_MECHANISM / PRECISE_MISSING_FACTOR_IDENTIFIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and conditional end-to-end map

The full target remains open: for independent real coordinates with probability densities bounded by one and arbitrary real symmetric `A` with at least three eigenvalues of absolute value at least one, prove a universal essential density bound for `X^T A X`, or give a valid counterexample. Continuity is a separate desired conclusion and is not proved here.

The preceding B05 report `QFORM-HEAVY-ISOTROPIC-ZERO-LEVEL-CURVATURE-v1` reduced the exact-rank-three heavy-isotropic survivor to a radial coarea integral. It paid the entire curvature tail at output level `q=0` by an `O(rho^-2)` slice bound, and proposed as the next implication a translation-uniform hyperbolic trace estimate retaining `rho^-2` or at least some universal integrable pointwise radial gain for every `q`.

This run tests that first missing implication immediately. The answer is negative in the strongest natural pointwise sense: already for the exact three-dimensional target form `2XY+Z^2`, no universal integrable function of the radial parameter can dominate all coarea slices uniformly in the output level and admissible product law. Thus the next proof must integrate the moving stationary ridge in `rho` jointly before taking the output supremum; it cannot close by proving a better pointwise radial envelope.

## 2. Exact target-valid radial coarea formula

Take

```
A0 = [[0,1,0],
      [1,0,0],
      [0,0,1]].
```

Its eigenvalues are `{1,-1,1}`, so it satisfies the exact target hypothesis with three eigenvalues of modulus one. Let `X,Y,Z` be independent with arbitrary cap-one probability densities `f_X,f_Y,f_Z`. Then

`Q=2XY+Z^2`.

Solving for `x` and then setting `z=rho y` gives, for the standard coarea representative,

`p_Q(q) = (1/2) integral_R J_rho(q) d rho`,                       (2.1)

where

`J_rho(q)=integral_R f_X(q/(2y)-rho^2 y/2) f_Y(y) f_Z(rho y) dy`. (2.2)

The null set `y=0` is irrelevant. Formula (2.1) is exact: solving `q=2xy+z^2` contributes `1/(2|y|)`, while `z=rho y` contributes Jacobian `|y|`.

## 3. Main correction theorem

### `QFORM-NO-UNIVERSAL-INTEGRABLE-RADIAL-ENVELOPE-v1`

There is no nonnegative `w in L^1([2,infinity))` with the following property:

> for every independent cap-one probability densities `f_X,f_Y,f_Z` and every `q`, one has `J_rho(q)<=w(rho)` for almost every `rho>=2`.

Hence no bound of the form `J_rho(q)<=C rho^(-1-epsilon)` can hold uniformly over the target class for any `epsilon>0`; more generally, **no law-independent integrable pointwise radial majorant exists at all**.

### Proof

Fix a real `R>=2`. Define three admissible probability densities by

`f_Z = 1_[R,R+1]`,                                                (3.1)

`f_X = 1_[-R^2-1/2,-R^2+1/2]`,                                  (3.2)

and

`f_Y = 1_[1,1+1/R] + 1_[3,4-1/R]`.                              (3.3)

The two components in (3.3) have total length

`1/R + (1-1/R)=1`,

so all three functions are probability densities bounded by one. Put

`q_R=-R^2`.                                                       (3.4)

We prove a lower bound on a positive-measure radial interval, not merely at a single radius. Let

`rho = R + u/R`, `0<=u<=1/8`,                                    (3.5)

and

`y = 1 + s/R`, `0<=s<=1/2`.                                      (3.6)

Then `f_Y(y)=1`. Also

`z=rho y = R+s+u/R+us/R^2`.

For `R>=2`,

`0<=z-R<=1/2+1/16+1/64=37/64<1`,

so `f_Z(rho y)=1`.

It remains to inspect the `X` argument. Write

`P=R^2/(2y)+rho^2 y/2`.

Since `z=rho y`,

`P = rho (R^2+z^2)/(2z)
   = rho [R+(z-R)^2/(2z)]`.

Therefore

`P-R^2 = R(rho-R) + rho (z-R)^2/(2z)
       = u + (z-R)^2/(2y)`.

Using `u<=1/8`, `y>=1`, and `z-R<=37/64`,

`0<=P-R^2 <= 1/8 + (37/64)^2/2 < 1/2`.                           (3.7)

Thus

`q_R/(2y)-rho^2 y/2 = -P in [-R^2-1/2,-R^2]`,

so the `X` factor is also one. Consequently, throughout

`I_R := [R,R+1/(8R)]`,

one has

`J_rho(-R^2) >= integral_[1,1+1/(2R)] 1 dy = 1/(2R)`.             (3.8)

Now suppose a universal `w in L^1([2,infinity))` existed. Apply the asserted almost-everywhere bound to the construction above for every rational `R>=2`. Let `N_R` be the exceptional null set for that particular law and output level, and let `N` be their countable union; `N` is null.

For every `rho>=2` outside `N`, choose a rational `R<=rho` so close that

`rho-R < 1/(8R)`.

Then `rho in I_R`, and (3.8) yields

`w(rho) >= 1/(2R) >= 1/(2rho)`.

Thus `w(rho)>=1/(2rho)` for almost every sufficiently large `rho`, contradicting `w in L^1([2,infinity))`. QED.

## 4. Why the obstruction is a moving stationary ridge, not a QFORM counterexample

For `q=-R^2`, the phase entering the first density is

`psi_rho(y) = -R^2/(2y)-rho^2 y/2`.

Its derivative vanishes at

`y_*(rho)=R/rho`,                                                  (4.1)

and the stationary value is

`psi_rho(y_*)=-R rho`.                                             (4.2)

At `rho=R`, the stationary point is exactly `y=1` and the stationary value is exactly the center `-R^2` of the chosen `X` packet. Quadratic tangency in `y` lets a unit-width `X` packet capture a `Y` interval of size `asymp 1/R`; the stationary value then moves in `rho` with speed

`|d(-R rho)/d rho|=R`,                                             (4.3)

so the same packet can remain resonant only across radial width `asymp 1/R`. The construction above realizes these two reciprocal scales explicitly.

This is the exact reason the slice can be as large as `c/rho` while the *joint* radial contribution can still be harmless. Indeed the lower rectangle found above has area only

`|I_R| * 1/(2R) = 1/(16R^2)`.                                    (4.4)

Thus this correction does not disprove a uniform bound on the integrated radial trace `integral J_rho(q)d rho`; it disproves the stronger strategy of obtaining that bound from a universal integrable pointwise radial majorant.

## 5. Assigned partner result applied to an actual inequality

The assigned partner fleet02/B05 proved `QFORM-THREE-BANK-GENERAL-CORE-v1` in

`yspennstate/math-open-problems@a31006ef311ca9e937f37c62d602d21ada3b1139`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B05/20260922T202100Z-b05-qform-47d9c1a2/REPORT.md`.

Its exact statement says that if three independent cap-one scalar variables have a symmetric `3x3` quadratic core `M` with `sigma_min(M)>=s`, then the quadratic-plus-affine law has density `<36/s`.

For the stress form above,

`M=A0`, `sigma_min(A0)=1`.

Therefore the partner theorem applies to **every** choice of `f_X,f_Y,f_Z` above and gives the concrete target-valid bound

`boxed( ||p_(2XY+Z^2)||_infinity < 36 ).`                          (5.1)

So the same family that forces the coarea slices to have a nonintegrable universal pointwise envelope is nevertheless uniformly bounded at the level of the full quadratic pushforward. This cleanly separates a false intermediate mechanism from the conjecture itself.

## 6. Correct first unpaid implication

The prior first debt `QFORM-TRANSLATION-UNIFORM-HYPERBOLIC-CURVE-TRACE-v1`, when interpreted as demanding an integrable pointwise envelope in `rho`, is now refuted.

The corrected first unpaid implication is

### `QFORM-STATIONARY-RIDGE-JOINT-RADIAL-TRACE-v1`

In the preceding heavy-isotropic normal form

`Q=2B (sqrt(c) X_i+T') Y + tau Z^2`,

with radial slices `I_rho(q)` from the prior report, prove directly that

`sup_q integral_(curvature sector) I_rho(q) d rho <= C B sqrt(c)`   (6.1)

for a universal `C`, or an equivalent interval/small-ball estimate, **without first replacing `I_rho(q)` by a law-independent pointwise majorant in `rho`**.

The stationary equation for the translated scalar argument is

`-q/(2B y^2) - (tau/(2B)) rho^2 = 0`.                             (6.2)

When `q tau<0`, its moving solution has

`|y_*| = sqrt(|q/tau|)/|rho|`.                                    (6.3)

Thus the required gain should come from the transversality of the moving stationary value across the original-coordinate product law as `rho` varies, not from per-radius decay. The simplified stress test above shows the critical scaling exactly: slice height `1/rho`, resonant radial width `1/rho`.

A proof of (6.1), combined with the already-paid balanced sector, would close this exact-rank-three heavy-isotropic branch. The unrestricted full-matrix theorem would still require the separate additional-spectrum / aggregate-leakage passage now being pursued by the other slots.

## 7. Integrity and source ledger


Sources actually used:

- preceding B05 coarea report: `yspennstate/math-open-problems@d5aecac785f127174d8349c01db0f492035ad341:proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B05/20260922T195340Z-fleet01-B05-QFORM-r17/REPORT.md`;
- assigned partner theorem actually applied: `yspennstate/math-open-problems@a31006ef311ca9e937f37c62d602d21ada3b1139:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B05/20260922T202100Z-b05-qform-47d9c1a2/REPORT.md`;
- current programme controls/corrections from `yspennstate/math-research-brain`, revision `2026-09-22.15`.

Full QFORM: `OPEN_NOT_PROVED`. Continuity: `NOT_PROVED`. No scheduler, task, notification, email, Drive, public-release, paid-model/API, remote-workflow, permission, or installation mutation is made by this report.
