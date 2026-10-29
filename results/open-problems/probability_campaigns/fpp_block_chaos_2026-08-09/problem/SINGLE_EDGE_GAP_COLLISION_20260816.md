# A single-edge gap collision is controlled by the squared geodesic influences

Date: 2026-08-16  
Status: exact edge-level estimate proved under a uniformly positive density;
its insertion into the block-scale variance engine remains open

Companion: `GAP_WEIGHTED_TARGET_COLLISION_20260816.md`, SHA-256
`f0f378ad896fa63f9c47858aa1a9c777bb7ba6358f9f681cb212c4b26abfd217`.

Let iid edge weights on `Z^d`, `d>=2`, have an absolutely continuous law `G`
supported on `[a,b] subset (0,infinity)`, with density

`rho(x)>=alpha>0` for almost every `x in [a,b].`              (1)

For the unique geodesic from `0` to `v`, write

`p_e=P(e belongs to gamma(0,v)).`                             (2)

The exact threshold structure of one edge turns its gap-weighted target
collision into an `l^2` influence quantity.  Combining this with Corollary 1.3
of Dembin--Elboim--Peled, [On the influence of edges in first-passage
percolation on Z^d](https://arxiv.org/abs/2307.01162v2), gives

`Gamma_edge<=C ||v||^(2/(d+1)) (log ||v||)^d.`                (3)

This is an edge-coordinate result.  It does not control the outside-interaction
term in the distinguished-coordinate spectral lemma, nor does it automatically

## 1. The through/avoiding split is a one-dimensional threshold

Fix an undirected edge `e`.  Among paths from `0` to `v` that use `e`, define

`B_e=min (path cost with the one copy of w_e removed),`

and let

`C_e=min cost among paths avoiding e.`

Positive weights allow minimizers to be taken simple, so a through path uses
`e` only once.  Both `B_e` and `C_e` are measurable with respect to the weights
outside `e`.  Put

`T_e=C_e-B_e.`                                                (4)

Conditionally on the outside environment, the passage time is

`X=min{w_e+B_e,C_e}.`                                         (5)

The weight law is atomless and independent of `T_e`, so ties have probability
zero and

`{e in gamma(0,v)}={w_e<T_e}` almost surely.                  (6)

If `g_e` is the gap from the selected through-edge route to the best route
avoiding `e`, set to zero when the geodesic avoids `e`, then

`g_e=(T_e-w_e)^+` almost surely.                              (7)

This is the single-edge specialization of the companion's gap cap; here the
cap itself has an exact scalar-threshold form.

## 2. A deterministic local detour bounds the threshold

Choose one unit plaquette containing `e`.  Replace `e` in a minimizing through
path by the other three edges of that plaquette.  The result is a walk avoiding
`e`; erasing any loops cannot increase its cost.  Since every edge weight is at
most `b`,

`C_e<=B_e+3b,       hence T_e<=3b.`                           (8)

This argument also applies to edges incident to an endpoint.  It uses only
`d>=2`, positivity, and the upper support bound.

For `x in [a,b]`, define the target-conditioned mean gap

`h_e(x)=E[g_e|w_e=x]=E[(T_e-x)^+].`                           (9)

Let `q_e(t)=P(T_e>t)`.  Layer-cake integration and (8) give

`h_e(x)=integral_x^(3b) q_e(t) dt.`                          (10)

On the support interval, Fubini and (6) yield

`integral_a^b q_e(t) rho(t) dt
 =P(w_e<T_e)=p_e.`                                           (11)

Using the density lower bound in (1),

`integral_a^b q_e(t) dt<=alpha^(-1) p_e.`                    (12)

For `t>b`, the event `{T_e>t}` is contained in `{T_e>b}`.  On
`{T_e>b}`, every possible value of `w_e` lies below `T_e`, so

`P(T_e>b)<=p_e.`                                             (13)

Equations (10)--(13) prove the uniform estimate

`0<=h_e(x)<=(alpha^(-1)+2b)p_e,       x in [a,b].`            (14)

No independence between different edge-use events is asserted or needed.

## 3. The gap collision and the published influence bound

Define the single-edge gap-weighted target collision

`Gamma_edge=sum_e E[h_e(w_e)^2].`                            (15)

Only finitely many summands can be nonzero at fixed endpoints: the straight
coordinate path has cost at most `b||v||_1`, while every geodesic edge costs at
least `a`, so a geodesic has deterministically bounded length and range.

Squaring (14), averaging in `w_e`, and summing gives

`Gamma_edge
 <=(alpha^(-1)+2b)^2 sum_e p_e^2.`                          (16)

Dembin--Elboim--Peled assume exactly (1).  Their Corollary 1.3, specialized to
the squared influences, states that for `||v||>=2`,

`sum_e p_e^2
 <=C_(d,G) ||v||^(2/(d+1)) (log ||v||)^d.`                  (17)

Combining (16) and (17) proves (3).  In the planar case this is

`Gamma_edge<=C ||v||^(2/3) (log ||v||)^2.`                  (18)

The cited paper proves (17) through a quantitative bound on the number of
edges with influence above a threshold; the only new calculation here is the
elementary threshold-gap conversion (4)--(16).  No novelty claim is made
without a dedicated literature comparison.

## 4. Consequence for the distinguished edge mass

Let `w_e'` be an independent replacement, let `X^e` be the passage time after
replacing only `e`, and put

`z_e=(X^e-X)^+.`                                             (19)

Use the pair `Y_e=(w_e,w_e')` as the distinguished coordinate.  Define

`C_edge=sum_e(E z_e)^2,`

`P_edge=sum_e Var(E[z_e|Y_e]).`

The target-sharing identity and the pointwise gap cap from the companion give

`C_edge+P_edge<=Gamma_edge.`                                 (20)

Therefore (3) also bounds the pure distinguished-edge contribution to the
spectral ledger.  This removes one possible edge-level obstruction: the target
coordinate's unsmoothed ANOVA mass is sublinear in the endpoint distance under
(1).

It does not close the FPP variance problem.  If the engine is run with
single-edge coordinates, the remaining outside variance `V_z` and its
variance-weighted algorithmic revealment are still uncontrolled.  If the
engine is run with its original `n` by `W_n` blocks, (16) does not directly
bound the corresponding block gap: avoiding a whole block is a different and
potentially much more expensive constraint than avoiding one edge.  Finally,
in `d=2` the rate in (18) still carries logarithms and is only comparable to
the conjectural `n^(2/3)` passage-time variance scale.

## 5. Break-it checks

* The threshold `T_e` is outside-measurable because every through path has the
  same coefficient one on `w_e`; this fails for a multi-edge block and is why
  the result is not silently promoted to blocks.
* The local detour produces a walk, possibly with repeated vertices.  Loop
  erasure uses positive weights and yields an avoiding path of no larger cost,
  so (8) is unaffected.
* The tail interval in (10) is essential.  Replacing it by an integral only to
  `b` would miss environments in which the edge wins for every possible value
  of its own weight.  Equation (13) pays for that robust-use event.
* The density lower bound, not merely absolute continuity, is what converts
  Lebesgue length in (12) to the influence `p_e`.  The argument does not cover
  arbitrary atomless or atomic laws.
* Equation (17) is an external theorem under the same distributional
  assumptions.  The present note does not reprove it.

An independent proof and source audit is required before (3) or (20) is used
as a campaign dependency.
