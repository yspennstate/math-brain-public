# Supplement — newest fleet02/B16 bank-aggregate gate-failure result

Programme: `QFORM-DENSITY-3EIG-20260922`.  
Run: `20260923T113953Z-fleet01-B16-QFORM-r12`.  
Status: `DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`.

This supplement is append-only relative to the run report. It records the newer designated-partner result that landed after the report calculation was begun.

## 1. Source pin

Newest compatible designated partner:

`yspennstate/math-open-problems@7dc1a1fb738f263d7fe021dcf3ce5c37223ced4e`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B16/20260923T112849Z-fleet02-B16-QFORM-6a31b2a7/REPORT.md`

blob `8c7a389e625a6c9dd019652585e2befe0803f854`.

It proves `QFORM-GATEFAIL-NEARCOLOOP-BANK-AGGREGATE-v1`. For every `0<a<1/64`, `m>=64`, and arbitrary cap-one independent original-coordinate laws, its exact-rank-three target family has spectrum `{1,-1,1}` and satisfies

`||p_(Q_gate)||_infinity <211`.                                  (1.1)

The proof aggregates two diffuse source banks before paying the reciprocal determinant. In the same family, a one-physical-coordinate-per-bank determinant certificate degrades like `m^(2/3)`, so the aggregation is mathematically essential rather than cosmetic.

## 2. Apply the completed partner inequality to an actual higher-rank target

Let `Z=(Z_1,...,Z_q)` be any further collection of independent real variables, disjoint from every source used in `Q_gate`, each with density at most one. Let `C=C^T` be an arbitrary real `q x q` matrix and define

`W=Z^T C Z`,

`Q_ext=Q_gate+W`.                                                (2.1)

The two summands are independent. Hence, writing `mu_W` for the law of `W`,

`p_(Q_ext)=p_(Q_gate)*mu_W`

in the sense of densities, and Young's probability-convolution inequality gives

`boxed: ||p_(Q_ext)||_infinity <= ||p_(Q_gate)||_infinity <211`. (2.2)

This is an actual arbitrary-dimensional target extension. Its coefficient matrix is the block direct sum

`A_ext=A_gate direct_sum C`.

Since `A_gate` already has the three eigenvalues `{1,-1,1}`, `A_ext` has at least three eigenvalues of modulus at least one for every choice of `q` and `C`. Thus (2.2) is a uniform density inequality inside the owner's full target class, not merely a lower-rank surrogate.

For a concrete nontrivial example, with three new cap-one independent coordinates,

`W=Z_1^2+2Z_2Z_3`,                                               (2.3)

we obtain

`boxed: ||p_(Q_gate+Z_1^2+2Z_2Z_3)||_infinity<211`.             (2.4)

No moment, support, centering, or sign hypothesis is introduced.

## 3. Relation to this run's new full-ambient fresh-bank theorem

The main report proves `QFORM-FRESH-BANK-FULL-AMBIENT-CROSS-LIFT-v1`: once one scalar bank is genuinely disjoint from the dependent two-dimensional receiver bank, arbitrary outside quadratic structure and arbitrary outside cross-coupling into the receiver bank can be conditioned away at no extra density cost beyond the rank-two affine half-Riesz constant.

The newest fleet02 family deliberately sits on the other side of that interface. Its variables

`S=sqrt(c)X0+t1X1+t2Y2+qY3-qY4`,
`T=sqrt(h)X1+sqrt(1-h)Y2`,
`V=(Y3+Y4)/sqrt(2)`

reuse the `Y3,Y4` source banks between the hyperbolic factor and the square factor. Hence `V` is **not** a fresh bank relative to `(S,T)`, and the theorem in the main report cannot simply be invoked by relabeling projected coordinates. Fleet02's source-bank aggregation theorem supplies a uniform bound precisely in this genuinely shared-bank chamber.

This is useful structural information: the remaining B16 compiler must distinguish

1. a genuine disjoint fresh scalar bank, paid by `QFORM-FRESH-BANK-FULL-AMBIENT-CROSS-LIFT-v1`; from
2. a shared-bank near-coloop geometry, where aggregate-before-determinant arguments such as `QFORM-GATEFAIL-NEARCOLOOP-BANK-AGGREGATE-v1` are required.

The first still-unpaid implication is therefore

`QFORM-TRUE-NEAR-COLOOP-BANK-COMPILER-v1`:

force one of those paid source-level geometries uniformly from an arbitrary surviving near-coloop frame, or produce a new source-first Fresnel/volume receiver for the residual shared-bank case.

Full QFORM remains open. Global continuity is not established by (2.2); the supplement claims only absolute continuity and the displayed essential bounds.
