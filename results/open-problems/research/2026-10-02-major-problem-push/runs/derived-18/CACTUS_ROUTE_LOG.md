# Route log: from one pendant vertex to cactus block trees

3 October 2026 UTC. This records the successful and failed extensions so a
later run does not recycle a narrow intermediate as a new result.

## Route A: monotone secular equation for one pendant vertex

The first extension used the cycle determinant `D_C(s)=det(K+sB)` only for
one fixed profile. If a leaf of profile `gamma` and edge weight `w` is
attached at `u`, then

    D_new(s)=(1+s gamma)D_C(s;beta)
                +wD_C(s;beta+gamma e_u).

With `s=-t`, `R=(K-tB)^(-1)` and `m=e_u*R e_u`, roots off the base poles
satisfy

    F(t)=1+w-gamma t[1+w m(t)]=0.

The identity

    m(t)+t m'(t)=e_u*R K R e_u>0

makes `F'(t)<0` on every pole interval; its one-sided limits give one root
per interval. Degeneracies follow by limits. This is a valid proof for one
leaf, but it did not by itself explain how to iterate, because bare
real-rootedness loses the profile-update response needed at the next leaf.

The exact one-leaf checker remains in the local development record. The
final immutable theorem uses the stronger profile-uniform lift instead and
does not count Route A as a separate headline result.

## Route B: profile-uniform rank-one determinant lift

Retaining the entire representation

    D_G(z)=c det(K+sum_x z_x q_xq_x*)

solves the iteration problem. The new leaf uses

    K'=diag(K,1+w),
    q'_v=(sqrt[w/(1+w)]q_u,1).

The determinant lemma reproduces the absent/present leaf recurrence exactly,
keeps `K'>0`, and preserves span. This attaches arbitrary trees and proves
the unicyclic/pseudoforest intermediate theorem.

## Route C: articulation gluing

The decisive further step observes `q_u*K^(-1)q_u=1`, normalizes the shared
vector to the first coordinate, and identifies that coordinate in two DR
pencils. The Schur complement matches the fixed-forest compatibility rule

    D(z_u^(1)+z_u^(2))
      =D_1(z_u^(1))E_2+E_1D_2(z_u^(2))-E_1E_2,

where `E_i=partial_(z_u^(i))D_i`. This closes DR under one-vertex sums and
therefore over every cactus block tree. It also exposes full multivariate
real stability, not merely same-ray real-rootedness.

## Boundary that remains open: adding an internal edge

Neither closure operation adds an edge between two existing vertices. That
operation is required to create a 2-connected theta block (three internally
disjoint paths between the same endpoints) and more general cyclomatic-two
blocks. A naive rank-one determinant update would have to encode the
deletion/contraction forest constraint and is not supplied by the current
DR data. Earlier exact/numerical searches found no apex-root counterexample
on small dense graphs, but absence of a counterexample is not a closure
theorem. No theta, series-parallel, arbitrary-graph, or full forest
conjecture claim is made.
