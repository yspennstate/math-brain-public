Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.** Source metric `d_sym: 3 -> 3` at run start. Planned methods: **B1 / B20 / B26**.

# Idea before code — the V=12 equality boundary as a five-edge affine section problem

Current canonical target remains `operations/claims/MAHLER-SYMMETRIC-VOLUME-PRODUCT.md`: for every origin-symmetric convex body `K=-K subset R^n`, prove `|K||K^circ| >= 4^n/n!`. The verified source metric is `d_sym=3`; nothing in this checkpoint moves it.

I resume the exact `n=4,V=12,E=5` equality boundary isolated in `2026-09-20T04-58-00Z__mahler_exact_quotient_and_V12_boundary.md`. There are six antipodal vertex-pair indices. Equality forces five nonsimplicial facet pairs, each omitting a distinct index; after relabeling they omit `1,...,5`, so index `6` belongs to all five.

Let `K=ker A` be the 2-dimensional antipodal dependency space and choose a `2 x 6` matrix `B` whose row space is `K`. Then the polar section is

`Q = K^perp cap [-1,1]^6 = ker(B) cap [-1,1]^6`.

A nonsimplicial facet omitting index `j` corresponds to a section vertex `q^(j)` in the relative interior of a cube edge parallel to coordinate `j`:

`q^(j)_i in {+1,-1}` for `i != j`, and `|q^(j)_j|<1`, with `B q^(j)=0`.

Because index 6 is saturated at every one of the five vertices, replace `q^(j)` by its antipode when necessary and orient all five so that `q^(j)_6=1`. Then all five points lie in

`H := K^perp cap {x_6=1}`,

which is a 3-dimensional affine subspace of the 5-dimensional cube facet `[-1,1]^5 x {1}`. Therefore the equality-realizability problem has an exact lower-dimensional form:

> Does there exist a 3-dimensional affine subspace `H subset R^5` meeting the relative interiors of five cube edges, one in each coordinate direction `j=1,...,5`, at points `p^(j)`, such that every four of the five lifted points are affinely independent (equivalently every four corresponding facet normals are linearly independent)?

This is B1: change category from 4D centrally symmetric polytopes to codimension-two affine sections of the 5-cube facet.

There is a useful algebraic encoding for B20. Orient as above and write the five lifted edge points as the rows of a `5 x 6` matrix `Q5=[M | 1]`, where

- `M_jj=t_j` with `|t_j|<1`;
- `M_ji in {+1,-1}` for `i != j`.

The five points lie in a 3-flat iff `rank(Q5)<=4`; the desired full-spark normal condition is exactly `rank(Q5)=4` and every four rows independent. Hence there is a unique affine dependence `lambda != 0` satisfying

`lambda^T M=0`, `sum_j lambda_j=0`,

with every `lambda_j != 0`.

After using the last coordinate to normalize, each column equation can be rewritten as follows. For column `j`, let `S_j={i != j : M_ij=-1}`. Since `sum lambda_i=0`,

`sum_{i in S_j} lambda_i = -c_j lambda_j`, where `c_j=(1-t_j)/2 in (0,1)`.

Thus a realizable equality pattern requires five strict signed-subset contraction identities with a common nonzero zero-sum vector `lambda`. This is a much sharper object than the previous rank/debt count.

B20 will ask whether those five contraction identities are impossible once every `lambda_j` is nonzero, or whether they force a very small sign/Radon pattern. B26 will hunt the sporadic case: either construct one exact rational section satisfying all five edge conditions and full-sparkness, or prove that no sign pattern admits `c_j in (0,1)`.

Before any code, two cautions are fixed:

1. A finite sign search is only a certificate for this `V=12,E=5` equality boundary, not the full Mahler conjecture and not movement of `d_sym`.
2. If an exact section exists, the result is a **route obstruction/construction**, not a counterexample to Mahler; it only proves that incidence plus cube-section realizability do not by themselves eliminate the equality boundary.
