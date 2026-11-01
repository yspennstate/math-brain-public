# F0081 second attempt: insertion and variance (2026-10-11)

## Current result and scope
The argument below establishes the unconditional upper bound
    P*(X>r) <= (2 |B(0,r/2)|)^(-1/2) = C_d r^(-d/2)
for the critical two-colour stable Poisson matching in every dimension d>=1, by the finite-to-infinite argument written below. It gives all positive moments alpha<d/2. In dimension d=2, source Theorem 2 supplies E*X=infinity, so the full positive-moment criterion follows in that dimension. In d>=3 the critical lower moment remains unresolved. This is a PARTIAL answer to F0081, not a solution of its all-dimensions statement. No novelty claim is made.

The two alternative approaches and brain queries are recorded in ATTEMPT.md section 8. The selected approach replaces the earlier boundary-flux estimate with conservative insertion and variance tensorization. Every probabilistic transition is proved here; the original source is used for existence/perfection and the known dimension-two lower bound.

## A. Finite stable matching and comparative statics
Take finite red and blue sets in a metric space, with distinct distances from each vertex to its opposite-colour candidates. Length of an unmatched vertex is infinity. Process all red-blue edges in increasing length, accepting an edge precisely when neither endpoint was matched earlier. Ties between disjoint edges may be processed in either order. This is the unique stable partial matching.

Proof of stability: for any omitted edge, when it was processed at least one endpoint was matched by an edge of smaller length; that endpoint cannot strictly prefer the omitted edge. Accepted edges never change. Thus no blocking pair exists. Proof of uniqueness: the shortest available edge has mutually closest endpoints and must occur in any stable matching; otherwise both endpoints prefer one another over their proposed partners or being unmatched. Delete that pair and repeat finitely many times. Removing a matched pair from a stable matching leaves a stable matching on the remaining sets, since a blocking pair on the smaller sets would already block on the larger sets.

Lemma A1. Adding one blue vertex weakly decreases every old red matching length.
Proof. Let m and m' be the old and new stable matchings. Suppose an old red u has new length strictly larger than its old length. Let v=m(u). The new matching omits (u,v), and u prefers v, so stability of m' forces v to have a new red partner u1 strictly closer than u. This u1 is an old red (no red was added). The old matching omits (u1,v), and v prefers u1 over u. Therefore stability of m forces u1 to have an old partner v1 strictly closer than v. The vertex v1 is an old blue. In the new matching u1 is matched to v, and hence prefers v1; stability of m' forces v1 to have a new red partner u2 strictly closer than u1. Iteration produces a strictly decreasing sequence of edge lengths, alternating edges of m and m'. A finite configuration has only finitely many edge lengths, contradiction. All partners asserted to exist follow from the relevant endpoint strictly preferring an omitted finite edge over its current partner (which might have infinite length). The new blue never appears as an old partner v_i, so it cannot terminate this contradiction. This proves A1.

Lemma A2. Adding one red vertex a weakly improves all old blue lengths and weakly worsens all old red lengths.
Proof. The blue conclusion is A1 with colours interchanged. If a is unmatched in the new matching, its restriction to old vertices is stable, hence equals the old matching by uniqueness, and all old lengths stay equal. Otherwise let b be a's new partner. Delete the new pair (a,b). The restricted matching is stable on the old red set and the old blue set minus b. Reinsert b into this smaller problem. A1 says that every red length can only decrease on this reinsertion, and the resulting stable matching is precisely the original matching on the old vertex sets. Thus every old red length in the original configuration is at most its length in the configuration with a. This proves A2. The same proof with colours reversed applies to blue insertion.

## B. Conservative one-atom insertion lemma
Fix a threshold r and define the signed residual measure
    xi_r = sum_{red x: length(x)>r} delta_x
           - sum_{blue y: length(y)>r} delta_y.
For any finite configuration, adding one red vertex changes xi_r by exactly one positive Dirac mass, at some vertex location (not necessarily the inserted location). Adding one blue changes it by exactly one negative Dirac mass.

Proof. Under red insertion, A2 says that all previously residual reds remain residual, some old reds may become residual, and some previously residual blues may cease to be residual. The inserted red may or may not be residual. Consequently the signed-measure difference is a nonnegative integer-valued counting measure. Regardless of the matching, its total residual signed charge equals N_red-N_blue: every edge of length <=r removes one red and one blue from the initial signed count. Red insertion increases N_red-N_blue by exactly 1. The nonnegative integer measure difference therefore has total mass 1 and consists of exactly one atom. A2 with exchanged colours proves the blue case. This is valid for unbalanced inputs and unmatched vertices, whose lengths are infinity. It does not require conditioning the two point counts to be equal.

In particular, for any measurable Q,
    red insertion: D_r(Q) changes by 0 or +1;
    blue insertion: D_r(Q) changes by 0 or -1.       (B1)
The new atom's location is equivariant under simultaneous translations of the original configuration and insertion point, provided the metric and matching are equivariant.

## C. Finite-volume variance bound, with a self-contained product proof
Let T be a flat torus of volume t, with its periodic Euclidean distance. Let Q be any Borel subset of T. For two independent intensity-one Poisson processes on T, define the finite stable partial matching and D_r^T(Q) as above. Then
    E D_r^T(Q)=0,   E [D_r^T(Q)^2] <= 2 |Q|.       (C1)

First prove this for two independent binomial point processes built from m slots per colour, each occupied with probability q=t/m (m>=t), an occupied location uniform on T. Coincidences and endpoint-distance ties have probability zero. The base process obtained by deleting any one slot is stationary on T, even though its two colours have slightly different count laws. Insert an independent uniform point of that slot's colour. By B, the absolute signed-measure change is one Dirac atom. Its unconditional location is uniform on T: the joint law of the base process and inserted location is translation invariant, and the rule for the atom commutes with translations. A probability distribution invariant under all torus translations is normalized Haar measure. Hence
    P(the insertion atom belongs to Q)=|Q|/t.       (C2)
This assertion averages over the random base process; it is not claimed for each deterministic base process.

Condition on all slots other than a given red slot. If the slot is empty, D_r^T(Q) is a base value f0. If it is occupied at uniform location U, B1 makes D_r^T(Q)=f0+I, where I is a 0-1 variable determined by U and the base configuration. Thus, conditionally on all other slots, the variance is b(1-b)<=b, with b=q*P(I=1 | base). Taking expectations and using C2 bounds this expected conditional variance by q |Q|/t. For a blue slot the values are f0 and f0-I, and the same variance bound holds.

For independent slots X_1,...,X_{2m}, variance tensorization gives
    Var(F) <= sum_i E Var(F | all slots except i).
For completeness: write F-EF as its Doob martingale sum with respect to the successively revealed slots. Martingale differences are orthogonal, so variance is the sum of their squared L2 norms. For the ith difference, average over later slots and compare two independent copies of Xi while keeping all other slots fixed. Conditional Jensen bounds its squared norm by (1/2) E[(F(X)-F(X with Xi replaced))^2]. Conditional on all other slots, this last quantity is exactly Var(F | all other slots). Summing proves tensorization. All variables here have finite moments since |F| is bounded by the total number of occupied slots.

Applying this inequality to F=D_r^T(Q) yields
    Var(D_r^T(Q)) <= 2m q |Q|/t = 2|Q|.
Colour-exchange symmetry gives mean zero in this binomial model.

Now let m tend to infinity with t fixed. Each colour's point count Bin(m,t/m) converges in total variation to Poisson(t); conditioned on the count, the locations are independent uniform points in both models. Hence their entire finite point configurations converge in total variation. Moreover their count moment generating functions satisfy
    E exp(s N_colour) = (1+(t/m)(exp(s)-1))^m
                       <= exp(t(exp(s)-1)), s>=0.
The total point counts have uniformly bounded exponential moments, so D_r^T(Q)^2, bounded by total_count^2, is uniformly integrable. Total variation plus this uniform integrability transfers first and second moments to the Poisson model. Therefore (C1) holds. This argument proves the required special case of the Poisson Poincare inequality rather than merely assuming a Gaussian Poincare theorem applies.

## D. Passing from tori to the Euclidean Poisson matching
Fix r>0 and a bounded deterministic Q in R^d. Couple the two infinite Poisson processes with processes on successively larger centred flat tori by restricting each infinite process to its centred fundamental cube and using periodic distance. These restricted processes have exactly the independent Poisson laws required in C. They are not conditioned on balanced counts.

We need threshold status to be local. Here are the details. For a matching m and a finite threshold a, let S(x,a) indicate that x has a partner at distance strictly less than a. Stability implies the recursion
    S(x,a)=1 iff there exists a compatible y with |x-y|<a
                         and S(y,|x-y|)=0.         (D1)
If the left side holds, choose x's partner y; y has that same matching length and no shorter partner, proving the right side. Conversely if such a y exists, then if x's partner were farther than |x-y| (or absent), x,y would block unless matched together. Either x is matched to y or it already has a partner no farther than |x-y|. In both cases x is matched at distance <a. No equal candidate distances arise almost surely.

Recursion D1 examines a finitely branching tree of paths with strictly decreasing edge lengths, all smaller than the starting threshold. Each vertex has finitely many candidates in any finite radius by local finiteness. Almost surely there is no infinite strictly descending path in the union of the two Poisson processes. One proof follows. The union is a Poisson process of intensity 2. For a bounded starting region A and initial bound R, the expected number of n-edge self-avoiding paths starting in A, with decreasing lengths <=R, is at most
    2 |A| (2 kappa_d R^d)^n / n!,                 (D2)
by the factorial moment formula: integrate the start, then successive displacement vectors in a radius-R ball; the ordered radial lengths occupy 1/n! of the product volume. Discarding the distinctness constraint only enlarges the integral. The bound tends to zero as n tends to infinity. Thus an infinite self-avoiding descending path has probability zero. Any infinite descending path can be loop-erased to an infinite self-avoiding descending path: each vertex is visited finitely often, because all incident edges below R form a finite set and no edge can recur under strict length decrease. Erasing loops retains a subsequence of the original edges and therefore retains strict decrease. Consequently no infinite descending path exists. A countable cover by bounded rational cubes and integer R proves this simultaneously for all starting vertices and finite thresholds.

A finitely branching tree with arbitrarily large depth has an infinite branch: repeatedly choose a child whose descendants have unbounded depth; finite branching guarantees such a child at each step. Therefore the recursion tree in D1 is finite. Its decisions can be evaluated from the leaves upward and require only finitely many vertices and their candidate edges. This also reproves the fixed-threshold localization stated in Holroyd-Martin-Peres Proposition 2.2, PDF p.8.

There are finitely many input points in Q. The union of their finite decision trees is finite. For sufficiently large torus side length, this finite set and all candidate balls at its nodes lie strictly inside the fundamental cube. No periodic wraparound edge of length less than a node's threshold can reach any of these nodes, since every node is farther than r from the cube boundary. The torus and Euclidean decision trees therefore coincide. All threshold statuses for points in Q agree eventually, almost surely. No raw opposite-colour pair has distance exactly the fixed r, so using >r rather than >=r or a strict recursion threshold does not alter these statuses.

Thus D_r^T(Q) converges almost surely to D_r(Q). For all sufficiently large tori,
    |D_r^T(Q)| <= R(Q)+B(Q),
where this is the same fixed finite Poisson count under the coupling. Its squared value is integrable. Dominated convergence transfers the C1 second-moment bound, giving
    E D_r(Q)=0,  E D_r(Q)^2 <= 2 |Q|              (D3)
for every bounded Q and fixed r. The original source supplies that the infinite stable matching exists uniquely and is perfect for these inputs; no new assertion about unbalanced infinite matchings is required.

## E. Tail bound and dimension-two resolution
If Q has diameter at most r, the already proved monochromatic-residual identity gives
    2|Q| p(r)=E|D_r(Q)| <= sqrt(E D_r(Q)^2)
                           <= sqrt(2|Q|).
Choose the ball Q=B(0,r/2), of volume kappa_d (r/2)^d. Division gives
    p(r) <= C_d r^(-d/2),
    C_d=2^((d-1)/2)/sqrt(kappa_d).                 (E1)
Here kappa_d is the volume of the Euclidean unit ball. This holds for all r>0; it may exceed the trivial bound 1 at small r.

For every alpha>0, Tonelli gives
    E*X^alpha = alpha integral_0^infinity
                         r^(alpha-1) p(r) dr.
The part below 1 is finite. Using E1, the part above 1 is bounded by C_d alpha times integral_1^infinity r^(alpha-1-d/2) dr, finite for alpha<d/2. Hence all positive subcritical moments are finite in every d.

For d=2, source Theorem 2 (PDF p.4) states that any translation-invariant two-colour matching of independent intensity-one Poisson processes has E*X^(d/2)=infinity. The stable matching meets its hypotheses. Thus E*X=infinity. For alpha>=1, X^alpha>=X on {X>=1}, and E*[X;X<1]<=1, so E*X^alpha=infinity. Combined with E1, this proves the target criterion for d=2. The lower half here is a direct application of the printed theorem, not a newly proved lower estimate.

## F. Hostile-referee audit and unresolved lower half
1. Same-side insertion monotonicity is not assumed: it is derived in A2 by removing the new matched pair and reinserting its blue endpoint. This uses only uniqueness and A1.
2. Total residual charge conservation holds for partial finite matchings, including unmatched vertices. Conditioning equal counts would destroy the product-slot argument; it is explicitly avoided.
3. A one-atom change refers to the signed residual measure. In the red-insertion case, newly residual reds and removed residual blues both contribute positive atoms, so cancellation cannot conceal multiple changes.
4. Uniformity of the insertion atom is unconditional over a stationary base and uniform insertion location. It is never claimed for a fixed base, nor for a nonuniform insertion.
5. The finite torus has distinct endpoint distances almost surely, notwithstanding periodic metric cut loci. All relevant distance equality sets have Lebesgue measure zero. No preference tie rule carrying a spatial bias is used.
6. Binomial approximation takes m to infinity at fixed torus volume, before enlarging the torus. Uniform integrability is supplied by a count bound, not by an asserted continuity of stable matching in particle positions.
7. Threshold localization is proved through the finite recursion tree and factorial path bound. The torus limit is taken at fixed r,Q; no unjustified uniform-in-r convergence is needed.
8. Dominated convergence uses the local input count R(Q)+B(Q), not the full torus count (which would diverge).
9. The new upper bound does not prove a matching lower bound on residual-charge variance or first absolute moment. The earlier proposed fourth-moment criterion is no longer needed for the upper half.
10. For d>=3 source E*X^d=infinity does not imply E*X^(d/2)=infinity. That lower moment is still the exact remaining gap. E1 allows critical convergence if the actual tail has an additional sufficiently decaying logarithmic factor, so the endpoint cannot be decided from this upper bound.

The finite insertion lemma, variance argument, and localization were audited as above. The finite numerical and algebra checks below passed. Full F0081 remains PARTIAL: these checks do not supply its missing lower half in d>=3.

## G. Independent checks completed

1. `probe_monotonicity.py`: 4500 planar finite comparisons of red insertion passed both colourwise length inequalities.
2. `second_experiment.py`: 4500 new configurations in dimensions 1,2,3, with possibly unequal red/blue counts, checked all inter-edge thresholds. Every full signed residual-measure change was nonnegative with total mass exactly 1. No failure was found.
3. `exhaustive_insertion.py`: enumerated all 720 strict edge orders for insertion into a 2-red/2-blue instance, and all 40320 strict edge orders for insertion into a 3-red/2-blue instance. Every order and every integer threshold passed both comparative statics and the one-atom statement. These weights need not be Euclidean; the proof applies to symmetric bipartite preference weights without a triangle inequality. This is an exhaustive finite check, not a proof for arbitrary sizes.
4. Independent Poisson counts on flat tori (rather than balanced binomial counts) were sampled 350 times each in d=2 and d=3. Cubes of side 2 at threshold 2*sqrt(d) passed monochromatic residual checks. Descriptive second moments are below the theoretical bound; no inference rests on Monte Carlo confidence.

| d | cube volume | measured mean charge | measured second moment | proved second-moment upper bound |
|---|---|---|---|---|
| 2 | 4 | 0.03142857 | 2.46000000 | 8 |
| 3 | 8 | 0.04571429 | 1.81142857 | 16 |

Random check runtime: 23.53 seconds. Exhaustive check runtime: 3.02 seconds. Jobs were small (at most a few hundred points per colour, finite matrices well below 1 GB). Saved raw files: second_experiments.json, exhaustive_insertion.json.

`InsertionChecks.lean` compiled with exit code 0; second_lean_check.log records the invocation. Three arithmetic lemmas formalize the unique-unit-change step, restriction to a zero-or-one window increment, and equality of its square to itself. Imports are only Mathlib.Data.Int.Basic and Lean.Elab.Tactic.Omega. No sorry or native_decide. These lemmas are checked by the Lean kernel; the entire stochastic argument is not formalized.

The missing d>=3 endpoint lower bound has not been tested by pretending that finite-volume residual variance has a scale-uniform positive lower bound. Even a volume upper bound plus a local Poisson input does not force such a lower bound, because conservative redistribution can move covariance to spatial scales larger than r. Neither the earlier fourth-moment criterion nor association supplies the needed lower first absolute moment here.
