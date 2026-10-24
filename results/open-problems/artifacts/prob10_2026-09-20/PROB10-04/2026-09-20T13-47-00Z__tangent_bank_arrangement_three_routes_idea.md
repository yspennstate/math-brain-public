# PROB10-04 idea before code — replace geometric triangulation by a finite entropy-tangent arrangement

Runtime model: **GPT-5.6 Sol; reasoning level UNVERIFIED**. This is an idea-first artifact, not a threshold claim.

## Frozen source/model/ownership state

Exact source model remains classical proper iid random 3-SAT: `n` Boolean variables, `m=floor(alpha n)` independent clauses, each clause choosing three distinct variables uniformly and independent fair signs. The externally auditable explicit bracket remains `[3.52,4.4898]`, width `0.9698`; no project-internal candidate is promoted here without the repository's independent-validation standard.

Scoped ownership remains `operations/claims/PROB10-04.md`: cluster-aware weighted counting / overlap-variational work, complementary to NM13-06's constructive lower-bound route and NM13-13's interpolation/survey upper-bound candidate. The pre-refocus HARD7-06 F0095/binary-cascade state remains immutably preserved at `runs/hard7_2026-09-18/HARD7-06/2026-09-19T23-49-30Z__handoff_to_prob10-04.md` and is not relabeled as 3-SAT work.

The preceding PROB10-04 run proved the one-tangent simplicial entropy-dual certificate

`Phi(y)=K(y)+E(y)+const`, `E=V+C=inf_eta L_eta(y)`,

with convex explicit copy term `K` and affine entropy-dual majorants `L_eta`. It also proved an interior finite-cover theorem but left boundary pieces and the large number of geometric simplices as the next obstruction.

## Route A — mixture-of-tangents minmax relaxation

For a finite tangent bank `L_1,...,L_J`, set `E_J(y)=min_j L_j(y)`. Since for every probability vector `p in Delta_J`,

`E_J(y) <= sum_j p_j L_j(y)`,

one gets on any polytope `R`

`sup_R [K+E] <= inf_{p in Delta_J} max_{v in Vert(R)} [K(v)+sum_j p_j L_j(v)]`.

The right side is a finite LP/convex minimax problem over tangent weights and region vertices. This would be extremely attractive if it were tight enough because no geometric subdivision is needed.

**Missing lemma A:** determine whether a finite bank generated from the known Gibbs centers can make this global mixture bound strictly below the saddle value outside the local saddle neighborhood. Falsification criterion: on the already-studied difficult ray `y0+t d`, show a positive upper gap even after adding endpoint/midpoint tangents; if so, identify the loss as the minimax/Jensen relaxation rather than an entropy-dual failure.

## Route B — exact lower-envelope arrangement, keeping `K` exact

Do not replace `min_j L_j` by one convex combination. Partition `R` into cells

`C_j = {y in R : L_j(y) <= L_k(y) for all k}`.

On `C_j`, the finite-bank surrogate is exactly

`K(y)+E_J(y)=K(y)+L_j(y)`,

which is convex. Hence its maximum over the polytope `C_j` occurs at an extreme point of `C_j`. Therefore the continuum supremum of the surrogate over `R` should reduce to finitely many arrangement vertices formed from original region facets and tangent-equality hyperplanes `L_j=L_k`.

**Missing lemma B:** prove the exact arrangement-vertex reduction, including lower-dimensional cells/faces and the continuous extension `0 log 0=0` for the copy term on copy-simplex boundaries. Then test whether a small tangent bank certifies the entire previously difficult ray in one shot, without six hand-cut segments, and whether it strengthens the indefinite-tetrahedron certificate.

## Route C — information-geometric tangent cover, including entropy boundaries

For an attained Gibbs mean `y` with natural parameter `theta_y`, the entropy tangent from a center `c` with parameter `theta_c` has exact overpayment

`L_{theta_c}(y)-E(y) = D_A(theta_c,theta_y)`,

where `A` is the finite-support log partition and `D_A` is its Bregman divergence; blockwise this is a weighted KL divergence between Gibbs laws. For `E=V+C`, the overpayment is the sum of the variable- and clause-side KL divergences.

This suggests replacing Euclidean Hessian balls by a KL Voronoi cover of the entropy mean polytope. More importantly, at a boundary mean the dual infimum need not be attained by a finite parameter, but the representation `E(y)=inf_eta L_eta(y)` still supplies arbitrarily accurate finite tangents pointwise.

**Missing lemma C:** prove a boundary-uniform finite-bank theorem: on every compact feasible region where `E` is continuous, for every `eps>0` there exists a finite set of finite dual parameters such that

`0 <= min_j L_j(y)-E(y) <= eps`

uniformly, including boundary points. The proof should use only the infimum representation, continuity, and compactness, not uniform Hessian bounds. Combine this with Route B to obtain a finite exact certificate architecture whose only remaining 3-SAT-specific work is an outward-certified tangent bank plus exact support/arrangement enumeration.

## Planned order and success criteria

1. Prove or kill Route A first because it is algebraically cheapest. A quantitative failure is useful if it isolates the relaxation loss.
2. Prove Route B completely, then test it on the inherited Díaz finite-support surrogate. The diagnostic must compare against the preceding one-tangent segment/tetrahedron bounds and remain labeled non-interval evidence.
3. Prove Route C and its exact KL/Bregman identity. This is the intended method change after the previous run's boundary/Hessian obstruction.

A successful run may leave the external source width unchanged, but it must produce a complete theorem and a precise new remaining lemma toward an actual endpoint. No finite SAT instance, simulation, or physics decimal counts as source progress.