SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B06, 2026-09-23T04:19:15Z.
attacking: the product-projection weighted section functional left by r22; test it against an exact two-coordinate orthogonal projection of fragmented cap-one product laws before attempting any further one-sided Schur gluing.

# fleet01/B06 r23 — product-projection section functional is not uniformly bounded

**Run:** `20260923T041915Z-fleet01-B06-QFORM-r23`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Curved fiber integration  
**Classification:** `ESSENTIAL_STEP_APPLIED / R22_INTERFACE_REFUTED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Scope, controls, and predecessor

The target is unchanged: for every dimension, independent real original coordinates with probability densities at most one, and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove a universal essential bound for the density of `Q=X^T A X`, or give a valid target counterexample. The requested continuous-density conclusion is tracked separately and is not proved here.


The immediate predecessor is fleet01/B06 r22, visible on the pre-run math-open-problems master snapshot `dab12d4ed1332190aaf62f597482db7bc4c4c7e6` at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B06/20260923T035013Z-qform-r22-b06/REPORT.md`.

It proved `QFORM-CHAIN-WEIGHTED-SECTION-FUNCTIONAL-v1`. For a planar density `g(y,z)`, put

`m(y)=int g(y,z) dz`,
`H(y)=ess sup_z g(y,z)`,

and

`J_(y0)(g)=int sqrt(H(y)m(y)) |y-y0|^(-1/2) dy`.                    (0.1)

In the physical-chain square/hyperbola geometry, finiteness of this functional gives a density bound. r22 also proved that a global joint-density cap plus a middle-marginal cap does not control `J`, but its counterexample used an arbitrary dependent pair. The first unpaid implication was therefore:

`QFORM-PRODUCT-PROJECTION-WEIGHTED-SECTION-v1`:

> Does `J_(y0)` admit a dimension-free bound when `(Y,Z)` is specifically an orthogonal projection of an original-coordinate cap-one product law?

This run answers **no**, already for two original coordinates. This is a counterexample to the proposed proof interface, not to QFORM.

## 1. Designated partner result actually used

The assigned partner fleet02/B06 proved `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical source

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.

For an `n x k` matrix `R` with orthonormal columns and independent cap-one original coordinates `X`, the projected vector `R^T X` has density bounded by

`product_i (1-ell_i)^(-(1-ell_i)/2) <= exp(k/2)`,                    (1.1)

where `ell_i` are the row leverages and rows with `ell_i=1` contribute factor one.

Below I apply this to the exact `2 x 2` orthogonal rotation. Both row leverages equal one, so the theorem gives the actual inequality

`boxed: ||p_(Y,Z)||_infinity <= 1.`                                  (1.2)

Thus the counterexample lies inside the strongest possible product-projection density-cap regime supplied by the partner theorem.

## 2. Fragmented cap-one product source

Let

`S = sum_(k=3)^infinity 1/[k (log k)^2] < infinity`,
`delta_k = 1/[S k (log k)^2]`.                                      (2.1)

Then

`sum_(k=3)^infinity delta_k=1`.                                      (2.2)

Also, since `x -> 1/(x log^2 x)` is decreasing on `[3,infinity)`,

`S >= int_3^infinity dx/[x(log x)^2] = 1/log 3`.                    (2.3)

Hence

`delta_k <= log 3/[k(log k)^2] <= 1/(k log k)`,                      (2.4)

and in particular `delta_k<1/2` for every `k>=3`.

Set

`R_k=3k`,
`I_k=[R_k,R_k+delta_k]`,
`E=union_(k>=3) I_k`.                                                (2.5)

The intervals are disjoint and `|E|=1`. Let

`X_1 ~ density 1_E`,
`X_2 ~ density 1_[0,1]`,                                             (2.6)

independently. Both are admissible cap-one probability densities.

Define the exact orthogonal rotation

`Y=(X_1+X_2)/sqrt(2)`,
`Z=(X_1-X_2)/sqrt(2)`.                                               (2.7)

The Jacobian has absolute value one, so the joint density is

`g(y,z)
 =1_E((y+z)/sqrt(2)) 1_[0,1]((y-z)/sqrt(2))`.                       (2.8)

Thus `g` is itself an indicator and

`||g||_infinity=1`,                                                   (2.9)

in agreement with the partner inequality (1.2).

## 3. Exact middle marginal and divergence of the weighted section functional

Let

`T_0=X_1+X_2`.                                                        (3.1)

Its density is the convolution

`h(s)=int 1_E(x)1_[0,1](s-x) dx`.                                    (3.2)

For the `k`th fragment `I_k`, the corresponding convolution support is

`[R_k,R_k+delta_k+1]`.                                                (3.3)

These supports are mutually disjoint because `R_(k+1)-R_k=3` and `delta_k+1<3/2`.

For

`s in [R_k+delta_k,R_k+1]`,                                          (3.4)

the unit interval `[s-1,s]` contains all of `I_k`, so

`h(s)=delta_k`.                                                       (3.5)

Since `Y=T_0/sqrt(2)`, its marginal density is

`m(y)=sqrt(2) h(sqrt(2)y)`.                                          (3.6)

Define the plateau

`J_k=[(R_k+delta_k)/sqrt(2),(R_k+1)/sqrt(2)]`.                       (3.7)

For a.e. `y in J_k`, the `z`-section of the indicator density (2.8) has positive length. Therefore

`H(y)=1`,
`m(y)=sqrt(2) delta_k`                                                (3.8)

throughout the interior of `J_k`.

Take the critical section point `y_0=0`. The contribution of `J_k` to (0.1) is bounded below by

`int_(J_k) sqrt(H(y)m(y)) y^(-1/2) dy`

`>= 2^(1/4) sqrt(delta_k)
    *[(1-delta_k)/sqrt(2)]
    *[((R_k+1)/sqrt(2))^(-1/2)]`

`=(1-delta_k) sqrt(delta_k)/sqrt(R_k+1).`                             (3.9)

Using `delta_k<1/2`, `R_k=3k`, and `3k+1<=4k`,

`(3.9)
 >= (1/2) * [1/sqrt(S k (log k)^2)] * [1/(2sqrt(k))]`

`= 1/[4 sqrt(S) k log k].`                                           (3.10)

Therefore

`J_0(g)
 >= (1/[4sqrt(S)]) sum_(k=3)^infinity 1/(k log k)
 = infinity.`                                                        (3.11)

We have proved:

### Proposition 3.1 — `QFORM-PRODUCT-PROJECTION-WEIGHTED-SECTION-FALSE-v1`

There exist **two independent cap-one original coordinates** and a **two-dimensional orthogonal projection** `(Y,Z)` of them such that

`||p_(Y,Z)||_infinity=1`                                             (3.12)

but

`J_0(p_(Y,Z))=infinity`.                                              (3.13)

Consequently no universal estimate of the r22 weighted section functional can hold over all two-dimensional orthogonal projections of cap-one product laws.

This is stronger than the arbitrary-dependent-pair obstruction from r22: the bad pair has exact original product provenance, and even the designated partner's optimal full-dimensional projection cap is one.

## 4. Why this is not a counterexample to QFORM: the lifted quadratic form is actually easy

Introduce an independent third coordinate

`X_0 ~ Uniform[0,1]`.                                                  (4.1)

Consider the spectral-coordinate chain form

`Q = X_0^2 + 2YZ`.                                                     (4.2)

Because of the exact orthogonal identity

`2YZ
 = (X_1+X_2)(X_1-X_2)
 = X_1^2-X_2^2`,                                                      (4.3)

we have in the **original independent coordinates**

`boxed: Q=X_0^2+X_1^2-X_2^2.`                                       (4.4)

Its matrix is diagonal with eigenvalues `{1,1,-1}`, so it is an exact target instance.

For any cap-one scalar density, the density of `X^2` is bounded by `t^(-1/2)` on `t>0`. Hence the two independent positive squares `X_0^2` and `X_1^2` have convolution density bounded by the beta integral

`int_0^t [u(t-u)]^(-1/2) du = pi`.                                  (4.5)

Convolution with the independent random variable `-X_2^2` cannot increase the `L^infinity` norm. Thus

`boxed: ||p_Q||_infinity <= pi`,                                     (4.6)

even though the spectral-chain functional in (3.11) is infinite.

So the divergence is entirely a **proof-interface loss** caused by first compressing the original product source to the dependent pair `(Y,Z)` and then paying a one-coordinate section singularity. The full original-coordinate integral contains cancellation/aggregation that the section functional destroys.

## 5. Consequence for the B06 mechanism

The r22 unpaid implication `QFORM-PRODUCT-PROJECTION-WEIGHTED-SECTION-v1` is refuted. No further run should try to prove a uniform bound for `J_(y0)` from product-projection provenance alone.

This is the third closely related run in the zero-diagonal one-sided-overlap chain after r20/r21/r22, so this run changes mechanism on the same QFORM target as required. The correct next interface is:

`QFORM-PROJECTION-LIFTED-PREIMAGE-CURVATURE-v1`.

Instead of conditioning on a projected middle coordinate and estimating `J_(y0)`, lift the curved spectral packet back to the original independent coordinates **before** taking a section supremum. Seek a bankwise inequality that spends the entire two-row wedge/exterior mass inside the original product integral. The two-coordinate model shows exactly what the desired lift must recover:

`2YZ = X_1^2-X_2^2`,                                                  (5.1)

turning an infinite spectral section functional into the paid two-square beta integral. In the live one-sided Schur survivor the analogous task is to use the `>1/2` one-L/two-R Pluecker packet as an aggregate preimage curvature currency, rather than choosing one physical minor or conditioning on one spectral middle coordinate.

This successor is a precise mathematical task, not a proved claim.

## 6. Status

- Full arbitrary-dimensional QFORM conjecture: **OPEN**.
- Valid counterexample to the original conjecture: **none produced**.
- New result: **explicit product-projection counterexample to the r22 weighted-section proof interface**.
- Partner result applied: fleet02/B06 `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, giving the actual cap `||p_(Y,Z)||_infinity<=1` in (1.2).
- Separate continuous-density conclusion for the full target: **OPEN / not proved here**.
- Execution: `WITHOUT_VERIFIED_BRAIN`; repository retrieval is not claimed as native learned-memory ingestion.
