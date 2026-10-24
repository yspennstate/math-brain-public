Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.**

# Idea before code — dimension-four symmetric Mahler via shadow-flow incidence debt

Fresh target: symmetric Mahler volume-product conjecture, canonical claim `operations/claims/MAHLER-SYMMETRIC-VOLUME-PRODUCT.md`.

Frozen source metric: `d_sym=3` at admission. This checkpoint proposes an auxiliary structural theorem; it does not move `d_sym`.

Methods: **B2 / B5 / B11**.

## Core idea

Take a centrally symmetric 4-polytope `P=-P` with `V` vertices, `F` facets, vertex-facet incidence total

`I=sum_G m(G)`,

where `m(G)` is the number of vertices of facet `G`. For a direction `theta`, define symmetric speeds by `alpha(-x)=-alpha(x)`. On a facet not parallel to `theta`, preserving planarity costs at most `m(G)-4` linear constraints; an opposite facet gives the same constraints under oddness. A facet parallel to `theta` costs none. Hence

`dim A^s_theta(P) >= (V-I+4F)/2 + C_theta(P)`,

where

`C_theta(P)=1/2 sum_{G: theta in lin(G-G)} (m(G)-4)`.

The globally affine symmetric shear speeds `alpha(x)=w dot x` have dimension four. If a locally volume-product-minimizing polytope has any admissible speed outside that four-dimensional subspace, the associated short shadow flow has affine primal volume; Meyer--Reisner polar-volume convexity plus rigidity then contradicts local minimality. Therefore every local minimizer must satisfy, for every direction,

`(V-I+4F)/2 + C_theta(P) <= 4`.

For generic `theta`, this yields `I >= V+4F-8`; polarity yields simultaneously `I >= F+4V-8`. If `theta` is parallel to a facet with `q` vertices, the stronger inequality is

`I >= V+4F+2q-16`.

This immediately predicts an all-dimensional structural phenomenon: in the natural `n`-dimensional version, a centrally symmetric **simplicial** local minimizer has every facet size `n`, so every odd speed is admissible. Unless `V=2n`, there are more than `n` odd speed variables and hence a nontrivial shadow flow. Thus the only simplicial local minimizer can be the cross-polytope; by polarity the only simple one can be a parallelotope. This is a structural reduction, not the Mahler conjecture.

## Negation test chosen before computation

Test the exact 4-polytope

`P=conv(+-e_1,...,+-e_4,+-(1,1,1,1))`.

It has ten vertices. If it were a plausible isolated minimizer/counterexample candidate, the shadow-rigidity screen should fail to expose a nontrivial odd speed. The exact computation will enumerate all supporting facets with rational arithmetic, determine their sizes, and exhibit an explicit nontrivial odd speed if the polytope is simplicial.

No numerical volume-product value will be used as a source claim. The checker will test only finite combinatorics/algebra suggested by this idea.