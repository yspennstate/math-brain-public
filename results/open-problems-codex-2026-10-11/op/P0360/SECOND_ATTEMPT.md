# P0360 — second serious attempt, 2026-10-11

## Starting gap and two new approaches

The first attempt established a necessary alternating disagreement cascade for geometric freezing sets, but could not exclude it. Ordinary legal rays with activation times tending to zero actually exist, so excluding those weaker rays cannot settle the question.

Two approaches not pursued in the first attempt:

1. **Intrinsic feasible-state sets and tree automata.** For each innovation subtree, collect the actual burning times realizable by all genuine frozen solutions on that subtree. Unlike a chosen anticipative solution, this entire feasible set depends only on its own subtree. Disjoint child feasible sets should therefore restore independence. Prove a gluing rule, derive a set-valued recursive equation, and ask whether canonical endogeny forces singleton feasible sets. A crucial check is that local burning-recursion solutions are not automatically genuine frozen solutions.
2. **Small-time truncation and uniform propagation bounds.** Compare arbitrary solutions with the unique solution for a freezing set truncated below θ^N. For every solution, early burning at time t requires ordinary T_t percolation, giving the universal bound P(Y_i≤t)≤t. Try to propagate this O(θ^N) input error upward through a disagreement/influence exploration. A crucial check is that arbitrary solutions can correlate descendant discrepancies with ancestral innovations, so the usual iid-boundary endogeny theorem cannot simply be invoked.

Approach 1 is selected first. Its prospective benefit is to replace arbitrary dependencies of a selected solution by independence of intrinsic child-subtree objects. No assertion of singleton collapse is made at this stage.

## Brain query

Ran the read-only math-store queries:

- “endogeny arbitrary boundary conditions frozen percolation disagreement cascade Rath Swart”;
- “tree automata pivot tree interpretations endogeny rogue fixed point”.

The first returned the frozen-percolation definitions and neighbouring open problems, but no theorem closing the gap. The second returned cards about randomized tree automata, interpretability and pivot trees. In particular the randomized-automaton attempt warns that the relevant measurable information is the marked innovation tree, not the unmarked tree. These are leads only. The present argument uses the full innovation subtree.

## Work in progress

We restrict this approach initially to Ξ_θ={θ^n:n≥0}, 0<θ<1, on the common probability-one event that no activation equals a freezing time and every subtree has a strictly positive ordinary percolation threshold. Statements about feasible states must use the full equation (1.3), not merely the local recursion χ.

## Proposition D: intrinsic genuine feasible sets restore subtree independence

For an innovation realization ω on a rooted subtree, let S(ω) be the set of root burning times of all sets F satisfying the full frozen equation on that subtree. Times are in Ξ_θ∪{∞}. For the subtree at i write S_i=S(Ω_i). Then, almost surely:

1. S_i is nonempty and finite at every vertex.
2. The pair (S_i1,S_i2) is iid and independent of ω_i; its common distribution is that of S_i. This concerns the intrinsic feasible sets, not an arbitrarily selected solution.
3. The exact set-valued recursion is

       S_i = {χ[ω_i](x,y): x∈S_i1, y∈S_i2}.

4. Let a_n=P(θ^n∈S_root) and b_n=P(S_root contains a state ≥θ^n), where ∞ counts as larger than all finite states. Then

       a_n = θ^n + 2b_n − 2,
       (1−θ)θ^n/(1+θ) ≤ a_n ≤ θ^n,
       P(max S_root < θ^n) = (θ^n−a_n)/2.

In particular E|S_root|≤1+1/(1−θ), independently of any endogeny assumption.

Proof of measurability. Code innovations in the countable product of [0,1]×{1,2}, and subsets F in {0,1}^T. For a fixed allowed time t, percolation from i is equivalent to existence of an open legal path of each finite length. For each length only finitely many vertices are tested. Thus the percolation predicate is Borel in (ω,F). The solution relation is Borel: the defining equation uses countable unions over allowed times and countable intersections over vertices. The event t∈S(ω) is the projection of the Borel relation obtained by additionally requiring the root burning time to equal t. Equality to a finite t is expressible using percolation at t and absence of percolation at smaller allowed times; equality to ∞ means absence at every allowed time. These projections are analytic, hence universally measurable. Consequently S_i is measurable in the completion of its subtree innovation sigma-field. Independence remains valid for the completed independent sigma-fields. This handles the possible lack of a measurable selector; no selector is presumed.

Proof of nonemptiness and finiteness. The source's canonical solution exists on an extension of the iid innovation probability space. Therefore almost every innovation realization admits at least one genuine solution. The same holds simultaneously for all countably many subtrees. For any genuine solution and any t∈Ξ, Y_i≤t implies ordinary percolation through T_t with F removed from the restriction, hence P_empty(i,t). Ordinary percolation at t has probability t, as proved in Proposition C. Its events decrease as t=θ^n decreases. The probability of percolation at all θ^n is therefore zero. Almost surely each subtree fails to percolate at some θ^N and hence at all smaller freezing times. S_i is consequently contained in the finitely many larger freezing times, together with ∞. It is nonempty and finite.

Proof of the gluing recursion. Restriction of any genuine solution to each child subtree is a genuine solution there. Its root burning time obeys the local recursion χ, giving one inclusion. Conversely choose any genuine solutions on the two child subtrees with root burning times x and y. Use their frozen sets on the descendants, and put the parent in F exactly when κ=1 and x≤τ. This makes the full frozen equation hold at the parent, since the child's percolation is unchanged. All descendant equations still hold, since they only inspect descendants. If κ=2 the parent percolates at an allowed time iff at least one child does, so its burning time is min(x,y). If κ=1 and x≤τ, the parent is frozen and never percolates. If κ=1 and x>τ is finite, the parent is open by time x and percolates at x, with no earlier allowed percolation. If x=∞, the child never percolates at any allowed time and neither does the parent. This proves the other inclusion and the formula χ. The unused child at an internal vertex still carries its own valid subtree solution, as required by equations at all vertices of T.

Proof of independence and the identities. Each child feasible set is a universally measurable function of its own innovation subtree, so disjoint subtrees and the parent's innovation are independent. They have the same law by iid innovations and the identical definition of feasibility at each root. At an internal vertex θ^n is attainable exactly when the first child set contains θ^n and τ<θ^n, giving probability θ^n a_n. At a branching vertex θ^n is attainable exactly when one child set contains θ^n and the other contains a value at least θ^n. The union of those two events has probability 2a_n b_n−a_n²: their intersection is the event that both sets contain θ^n. Hence

       a_n = (θ^n a_n + 2a_n b_n − a_n²)/2.

The canonical burning-time law has positive mass p_n=(1−θ)θ^n/(1+θ) at θ^n; canonical realizations are genuine solutions and thus p_n≤a_n. This gives a_n>0, so division proves the identity. The upper bound a_n≤θ^n follows from ordinary percolation. Since S is nonempty and finite, 1−b_n=P(max S<θ^n), proving the final identity. Finally |S|=1_{∞∈S}+Σ_n 1_{θ^n∈S}; Tonelli's theorem gives E|S|≤1+Σ_n θ^n. QED.

The use of analytic-set measurability is standard for Polish spaces and is explicitly a set-existence assertion, not an algorithm for computing S. No Borel selector or stationarity of a selected frozen solution is inferred.

## Proposition E: exact characterization of the relaxed local-recursion states

Let R_i be the set of root states attained by ANY assignment (X_j) on the subtree satisfying the local recursion X_j=χ[ω_j](X_j1,X_j2), with states in Ξ_θ∪{∞}; do not impose that X_j is the actual burning time of the recovered frozen set. On the no-tie event,

       R_i = {∞} ∪ {t∈Ξ_θ : P_empty(i,t)}.

Consequently R_i is a finite, subtree-measurable, stationary set-valued solution of the same recursion as S_i. It contains every genuine feasible state and, in an endogenous regime, contains the canonical innovation-measurable burning time. It nevertheless fails to be singleton with positive probability (indeed P(1∈R_i)=1, so R_i contains at least 1 and ∞ almost surely). It has E|R_i|=1+1/(1−θ), and its parameters a_n=θ^n, b_n=1 satisfy every identity and bound of Proposition D.

Proof. All-∞ is a local-recursion assignment. If X_i=t is finite, at a branching vertex with state t choose a child with state t, which exists because min of the child states is t. At an internal vertex with finite state t, the legal child's state is t and τ<t. Repeating yields an infinite legal T_t path, proving necessity.

Conversely, given an infinite legal T_t path from i, assign state t to its vertices and ∞ to every other vertex of the subtree. On the no-tie event an internal vertex of the path has τ<t and a legal child on the path. Its recursion outputs t. A branching vertex of the path has one child assigned t and its other child assigned ∞, so its output is t. Off-path vertices have no on-path descendants (the path starts at the subtree root), and both relevant child states are ∞; their recursions output ∞. Thus this is a local-recursion assignment with root t. This proves the characterization. Ordinary percolation is subtree-measurable and has probability t; finiteness and the expected cardinality follow as in Proposition D.

One can also check the set recursion directly. At an internal vertex, finite attainable states are exactly the child's ordinary-percolating times strictly larger than τ; ∞ is always attainable. At a branching vertex, the presence of ∞ in both child sets makes the finite attainable set the union of their finite parts; that union is exactly the parent's ordinary-percolating times. QED.

## Referee consequence and precise new obstruction

It is false that an independent, finite-mean, intrinsic set-valued solution containing an endogenous canonical state must be singleton. R supplies a counterexample to THAT proposed auxiliary assertion, within the same innovations and local recursion. This is not a counterexample to P0360: R contains labels from assignments that are not genuine frozen solutions.

For the ray assignment in Proposition E, every vertex of the recovered frozen set is unfrozen: on the ray the legal child has value t>τ, and off the ray the child has value ∞. Hence F=empty. The resulting ordinary burning times generally differ from the labels; more decisively, F=empty fails the full equation almost surely. To see this explicitly, fix an allowed time s=θ^n<1. At a fresh vertex the event κ=1, τ≥s and P_empty(i1,s) has probability (1−s)s/2>0, by independence. At vertices in an infinite deterministic antichain the corresponding innovation subtrees are disjoint, so these events are independent. Almost surely at least one (in fact infinitely many) occurs. The full equation requires those vertices to freeze, contradicting F=empty.

Thus the remaining task for Approach 1 is not independence or finiteness, both of which are proved. It is to distinguish S from R using the global requirement that each label equal the actual percolation time of the recovered frozen set. The set-valued recursion and its first-moment identities alone cannot make that distinction.

An even sharper obstruction is **top-state inflation**. Given the canonical burning assignment Y*, define B_i={Y_i*} unless Y_i*=1, in which case put B_i={1,∞}. On the no-tie event τ_i<1 at all vertices, B satisfies exactly the same set-valued recursion. At an internal vertex a child state 1 passes through as 1; inflating it yields both 1 and ∞ and inflates the output in the same way. Every other child state is uninflated. At a branching vertex, if the canonical minimum is below 1, adding ∞ beside a child state 1 cannot change that minimum. If the minimum is 1, both child states are in {1,∞}, at least one is 1, and the inflated image is exactly {1,∞}. If both states are ∞ the image stays {∞}. These cases exhaust the recursion and prove the claim.

When the canonical RTP is endogenous, B is an intrinsic innovation-measurable set-valued solution, iid across child subtrees, with E|B|=1+p_0 and P(|B|=2)=p_0>0. Nevertheless B has the SAME finite-state presence probabilities as the canonical singleton field, and min B_i=Y_i*. Thus it even satisfies a_n=p_n and H(t)=t/(1+θ), as well as the moment identity below, without collapsing. Its extra ∞ labels cannot be actual burning times of genuine solutions, by Propositions G/H. This illustrates why those propositions require genuine feasibility, even after every displayed scalar equality has been verified for an abstract set field.

This is a counterexample to a strengthened auxiliary claim about set recursions, not a counterexample to P0360. It preserves the local algebra while violating actual burning-time interpretation.

## Approach 2 pursued after the set-valued obstruction

The relaxed counterexample blocks the initial route to singleton collapse, so we also examine the truncation approach. It gives a rigorous convergence theorem in the endogenous regime, but still leaves a selection issue for arbitrary solutions.

## Proposition F: finite-truncation solutions converge to the endogenous canonical solution

Fix 0<θ<1 and Ξ_N={θ^k:0≤k≤N}. Let F^(N) be the unique genuine solution for this finite freezing set on the same iid innovations, with burning times Y_i^(N). Let (F*,Y*) be the canonical solution for full Ξ_θ. If its RTP is endogenous, then for every vertex i,

       P(Y_i^(N)≠Y_i*) → 0,
       P(1_{i∈F^(N)}≠1_{i∈F*}) → 0.

There is an explicit comparison for a finite innovation prefix U of depth d (vertices of length <d). Write ρ_N for the marginal law of Y_root^(N), ρ for that of Y_root*, and

       δ_N = θ^(N+1)/(1+θ).

Then

       TV(ρ_N,ρ) ≤ (N+2)δ_N,
       TV(Law(Ω_U,Y_root^(N)),Law(Ω_U,Y_root*))
           ≤ 2^d (N+2)δ_N.

If h_d(Ω_U) is a predictor for the endogenous Y_root* with error e_d=P(h_d≠Y_root*)→0, the common-innovations coupling satisfies

       P(Y_root^(N)≠Y_root*) ≤ 2e_d + 2^d(N+2)δ_N.

Proof of the marginal bound. For the finite freezing set, write C_N(t)=ρ_N([0,t]). Starting at the smallest freezing time θ^N, the source's finite-set recursion (Lemma 20, equation (2.11), PDF p.14) gives C_N(θ^N)=θ^N and, ascending through times,

       C_N(t)=f_t(C_N(previous time)),
       f_t(x)=max(x,t−x)=t/2+|x−t/2|.

This recurrence follows also by successively imposing the RDE identity and C_N(t)≥t/2 at the finite freezing times; the source proves that it is the law of the genuine canonical solution. Finite-set pathwise uniqueness makes the same law apply to F^(N). The full geometric law has C(θ^k)=θ^k/(1+θ). At the smallest time the difference is θ^N−θ^N/(1+θ)=δ_N. The map f_t is 1-Lipschitz, since ||x−t/2|−|y−t/2||≤|x−y|. Also C(θ^k)=f_(θ^k)(C(θ^(k+1))), since θ/(1+θ)<1/2. Induction gives |C_N(θ^k)−C(θ^k)|≤δ_N for every k≤N.

For k<N the point-mass error is at most 2δ_N by subtracting successive CDFs. For k=N the finite law's mass is θ^N, whereas the full law's mass is (1−θ)θ^N/(1+θ), with exact difference 2δ_N. The full mass on the omitted smaller freezing times is C(θ^(N+1))=δ_N, and the mass error at ∞ is at most δ_N. Summing absolute errors over this countable state space and dividing by two proves TV≤(N+2)δ_N. No assumption θ<1/2 is used; the max recurrence handles times with zero finite-truncation mass.

Proof of the finite-prefix bound. Finite-set uniqueness implies that F^(N) is an innovation-measurable subtree-equivariant solution: its canonical stationary/adapted/tree-respecting realization exists, and every genuine solution on the same innovations agrees with it. Consequently (ω,Y^(N)) has the RTP law with marginal ρ_N. At the boundary of the fixed depth-d prefix, the 2^d burning variables are iid with law ρ_N and independent of Ω_U. The canonical full process has the same property with marginal ρ. Couple these boundary variables coordinatewise by maximal couplings, using the same Ω_U. The probability that at least one boundary value differs is at most 2^d TV(ρ_N,ρ). If all agree, the root values obtained by the same finite recursion agree. This gives the stated total-variation bound on the joint root/prefix laws. The coupling here compares laws only; it does not presume boundary independence in the user's original common-innovations coupling of the two full solutions.

Proof of predictors and common-innovations convergence. Endogeny makes Y_root* a measurable function of all innovations and its state space is countable. For any ε>0, choose a finite set of states carrying probability at least 1−ε. The indicator of each chosen state is approximable in L1 by its conditional expectation given an increasing finite innovation prefix, by martingale convergence. A maximum-conditional-probability predictor among those finitely many states therefore has error tending to at most ε. A diagonal choice gives predictors h_d with e_d→0. Equivalently a Bayes predictor on all countably many states gives the same conclusion.

The event {y≠h_d(ω_U)} is measurable in the pair (ω_U,y), so the finite-prefix TV bound gives

       P(Y_root^(N)≠h_d(Ω_U)) ≤ e_d + 2^d(N+2)δ_N.

A union bound with the event {Y_root*≠h_d(Ω_U)} proves the explicit common-coupling estimate. First send N→∞ at fixed d, then d→∞. This yields equality in probability of the burning times, not merely convergence in their ordinary Euclidean distance. Subtree stationarity gives the same at every vertex. Finally F^(N) and F* are recovered by the same rule κ_i=1 and Y_i1≤τ_i, so the probability of differing membership at i is at most P(Y_i1^(N)≠Y_i1*), proving the second assertion. QED.

This applies to the entire source endogenous geometric regime 0<θ≤θ_*, including θ≥1/2. It is a statement about the unique finite-cutoff approximations, not unrestricted uniqueness of the full-time equation.

For 0<θ≤1/2 the marginal TV bound is sharp:

       TV(ρ_N,ρ) = (N+2)θ^(N+1)/(1+θ).

Indeed the preceding finite CDF is at most θ^(k+1)≤θ^k/2, so every finite recurrence uses the branch t−x. Starting with CDF error δ_N at θ^N, the errors at successive larger times alternate signs with the same magnitude. Every included atom then has absolute mass error 2δ_N, the omitted tail has mass δ_N, and the ∞ atom has absolute error δ_N. Dividing their sum by two gives equality, including the boundary θ=1/2 where a finite atom can vanish.

There is also a deterministic increasing cutoff subsequence N_j along which all vertices' burning labels and frozen memberships converge almost surely, eventually agreeing at each fixed vertex. To prove this, enumerate the vertices. By convergence in probability, choose N_j>N_(j−1) so that the probability of any burning-label discrepancy at the first j vertices is at most 2^(−j). Borel–Cantelli makes these discrepancy events occur only finitely often. Each fixed vertex therefore agrees for all sufficiently large j. Frozen membership follows by including its legal child in the enumeration. This is again a property of the cutoff approximation, not a capture theorem for arbitrary solutions.

## What truncation convergence does and does not establish

Every solution that is a vertexwise limit in probability of these uniquely determined finite-cutoff solutions equals the canonical solution almost surely. The proof is immediate from Proposition F: limits in probability are unique, and T is countable. More generally any such subsequential limit is canonical.

What is missing is a proof that every arbitrary genuine full-time solution is stable under removing the times below θ^N, or is otherwise captured by the finite-cutoff approximation. Proposition B shows exactly how a discrepancy could descend through every cutoff. The early-burning bound P(Y_i≤θ^N)≤θ^N is uniform for each fixed vertex but does not by itself control all descendants reached by that cascade. Endogeny supplies convergence of the canonical finite-cutoff laws; it has not supplied uniform stability across all full-time solutions.

## Proposition G: a scalar attainability criterion suffices for full uniqueness

Return to the intrinsic genuine feasible sets of Proposition D, and put p_n=(1−θ)θ^n/(1+θ). If a_n=p_n for every n≥0, unrestricted full-time solutions are almost surely unique. Conversely unrestricted uniqueness implies these equalities. In an endogenous regime, P0360 for Ξ_θ is therefore equivalent to proving that genuine feasibility cannot increase any finite-time attainability probability beyond its canonical mass.

Proof of sufficiency. Couple a canonical genuine solution with the innovations, on an extension if necessary. For every vertex i and every n, the event {Y_i*=θ^n} is contained in {θ^n∈S_i}; both have the same probability by the proposed equality. Their indicators consequently agree almost surely. There are only countably many (i,n), so this holds simultaneously for all of them on one probability-one event. On that event any other genuine solution has burning labels Z_i satisfying:

- if Y_i*=∞ then S_i has no finite state and Z_i=∞;
- if Y_i*=t<∞ then S_i has no finite state except t, and Z_i is either t or ∞.

Suppose 0<t<1 and Z_i=∞ while Y_i*=t. If κ_i=1, the canonical recursion forces Y_i1*=t and τ_i<t. The alternative recursion and the absence of any alternative finite label except t at child i1 force Z_i1=∞. If κ_i=2, at least one child has canonical state t. The alternative state ∞ forces both alternative children to have state ∞, so choose a child with canonical state t. Continue. This constructs an infinite legal path whose canonical label is t and whose alternative label is ∞ at every vertex; every internal vertex on it has τ<t. The alternative frozen set does not freeze these path vertices, since each legal child has alternative label ∞. Thus the path is open in the alternative solution at time t. Its root actually percolates at t, contradicting the supposed actual burning time Z_i=∞. This path argument also works at t=1 on the no-tie event, since τ<1 at every internal vertex. Hence Z_i=Y_i* at all vertices, and the recovered frozen sets agree. No measurable choice of the competing solution was required for this direction; the argument is pathwise on the common probability-one event.

Proof of necessity, including the measurability issue. Unrestricted almost sure uniqueness makes the canonical solution endogenous by the source's Lemma 7. Take Borel versions of its innovation-measurable frozen set and burning labels, which exist on the standard Borel innovation space. If a_n>p_n for some n, the analytic event

       {θ^n∈S_root and Y_root*≠θ^n}

has positive probability a_n−p_n. The Borel relation defining genuine solutions with root label θ^n admits a universally measurable selector on its analytic projection by the Jankov–von Neumann selection theorem. Select such a solution on that event and use the canonical solution outside it. This is a random genuine solution on the completed innovation probability space. It differs in actual root burning time with positive probability, so cannot have the same frozen set. This contradicts unrestricted uniqueness. Thus a_n=p_n for every n. QED.

Referee note: The sufficiency proof specifically invokes actual percolation for the alternative labels. The ray with all alternative labels ∞ shows exactly why it fails for the relaxed set R, even if an artificial family of local states had the same finite-time presence probabilities as the canonical process. The projection/selection theorem is used only in the converse, and no stationarity, adaptation or child independence of the selected solution is claimed.

The remaining scalar gap is explicit: prove a_n≤p_n for genuine feasible sets in the endogenous regime, or exhibit an n with a_n>p_n and genuine witnessing solutions. Presently only p_n≤a_n≤θ^n is proved. Proposition D rewrites this as identifying the distribution of max S, but gives no further inequality. The relaxed recursion reaches the upper endpoint a_n=θ^n, so its equations alone cannot prove the needed estimate.

## Proposition H: minimal feasible burning-time criterion and an exact moment equation

There is an equivalent scalar criterion using the minimum feasible time. Let L_i=min S_i and, for an allowed time t, define

       H(t)=P(L_root≤t),
       R_t(S)=max(S∩(0,t]) if this set is nonempty, and 0 otherwise.

Then

       H(t)^2 = E[R_t(S_root)],
       t/(1+θ) ≤ H(t) ≤ t       (t∈Ξ_θ).

If H(t)=t/(1+θ) at every allowed time, unrestricted uniqueness holds. Conversely unrestricted uniqueness implies those equalities. Thus proving this upper bound with constant 1/(1+θ), rather than the present constant 1, is another precise form of the remaining gap.

Proof of the moment equation. At a branching vertex the minimum feasible time is min(L_1,L_2), so the probability it is ≤t is 2H(t)−H(t)^2. At an internal vertex some feasible output is finite and ≤t exactly when the child feasible set contains an x with τ<x≤t. Conditional on the child set, this event has probability R_t(S_child), because τ is independent uniform on [0,1]. Average the two types and cancel H(t) from

       H(t) = E[R_t]/2 + (2H(t)−H(t)^2)/2.

The upper bound follows either from ordinary percolation or from R_t≤t·1_{L≤t} and H(t)^2≤tH(t). The canonical solution supplies H(t)≥P(Y_root*≤t)=t/(1+θ). QED for the identities.

Proof of sufficiency. On a canonical coupling the event {Y_i*≤t} is contained in {L_i≤t}; equality of their probabilities makes the events equal almost surely, simultaneously for all vertices and allowed times. Therefore any genuine alternative burning assignment Z satisfies Z_i≥Y_i* at every vertex: a strict inequality in the other direction would be separated by the allowed time t=Z_i. The recovered frozen set G then satisfies G⊂F*, since Z_i1≤τ_i implies Y_i1*≤τ_i.

Let A_ω(F) be the set defined by the right side of the full frozen equation. Removing more vertices cannot create an infinite open legal path, so A_ω is order reversing. Since G and F* are fixed points, G⊂F* implies G=A_ω(G)⊃A_ω(F*)=F*. Hence G=F*. This proves uniqueness without assuming that the alternative is stationary or adapted. It also emphasizes that two comparable frozen-set fixed points cannot be distinct.

Proof of necessity. Under unrestricted uniqueness the canonical solution is endogenous. If H(t)>P(Y_root*≤t) for an allowed t, with positive probability a genuine feasible root label is ≤t while the canonical label is >t. Choose one witnessing finite label on a positive-probability part of that event (there are finitely/countably many choices), and use the same analytic-relation uniformization argument as Proposition G to construct a measurable alternative solution. Its actual burning time differs, contradicting uniqueness. The opposite inequality H(t)≥t/(1+θ) is already proved, so equality follows. QED.

The relaxed set R from Proposition E has H(t)=t and R_t=t·1_{P_empty(root,t)}, hence E[R_t]=t². It satisfies the moment equation and the loose bound exactly. Therefore even this additional exact identity does not distinguish genuine feasibility from the spurious relaxed states. A proof using the actual-percolation requirement is still needed to improve the constant from 1 to 1/(1+θ).

## Hostile referee checks and bounded computations

1. **Solution class:** S uses the full equation and actual burning times. R uses only the local recursion. Both are finite and independent across disjoint subtrees, but only S has physical meaning. The explicit ray construction and the empty-frozen-set failure prevent conflating them.
2. **Measurability:** Existence projections defining S are analytic, not asserted to be Borel. Universal measurability suffices on the completed iid law. The converse of Proposition G invokes Jankov–von Neumann uniformization explicitly; it does not assume that a canonical-law sampler has support equal to S. Standard references are A. S. Kechris, *Classical Descriptive Set Theory*, Springer (1995), for analytic-set measurability and uniformization, and ordinary martingale convergence for the predictors in Proposition F.
3. **Finiteness and simultaneous events:** Ordinary percolation probabilities θ^n→0 rule out root labels accumulating at zero for every possible solution, on a countable intersection over all vertices. This bound is intrinsic and is not merely an almost-sure property of a selected solution. Minima of finite feasible sets therefore exist.
4. **Gluing:** Choosing child solutions separately preserves every descendant equation and all percolation witnesses there. The parent is one newly assigned vertex, whose equation and actual burning time are checked in all cases. No consistency of independently selected entire subtrees at deeper levels is assumed.
5. **Branching overlap:** The intersection in 2a_n b_n−a_n² is exactly the event that both child sets contain the target time, even if they also contain other states. This identity is kernel-checked by `FeasibleSetIdentity.lean` for any linearly ordered state space.
6. **Finite models as a hostile test:** `feasible_set_checks.py` exhaustively checks 2,025 branching membership cases on four-state alphabets and 288 exact top-state inflation intertwining cases. For θ=1/4,1/2,3/4 and Ξ={θ²,θ,1}, exact rational transformation verifies two different fixed laws of the set recursion: the singleton finite-model canonical law and the nonsingleton ordinary-percolation law. It also verifies the inflated fixed law and equality of its finite-state presence probabilities with the canonical law. These finite models have uniquely determined genuine solutions. Thus the proposed set-recursion-only uniqueness argument fails in a setting whose physical answer is already known. Results are saved in `feasible_set_checks.json`.
7. **Cutoff masses:** `truncation_checks.py` checks all marginal and total-variation inequalities with exact rational arithmetic for θ=1/4,1/2,3/5,3/4,9/10 and N=0,1,2,5,10,25,50 (35 cases). It includes θ≥1/2 where some truncated point masses vanish, and N=0. The estimates do not rely on falsely assuming every truncated time has positive mass. Results are saved in `truncation_checks.json`.
8. **Coupling quantifiers:** The maximal boundary coupling in Proposition F establishes a finite-prefix distance between laws. Equality in probability on the original same-innovation space is then proved separately with the predictor h_d. A law-coupling argument alone would not prove it.
9. **No unproved boundary independence:** No boundary independence is asserted for arbitrary full solutions. It is used only for the canonical RTPs of the finite and full models, where it is part of their established law.
10. **Scalar criterion:** The path in Proposition G carries the same finite canonical label at every step; canonical recursion provides the legal continuation. Each alternative label is ∞, so none of its internal vertices freezes, and τ<t makes them active at the target time. The contradiction uses actual percolation, exactly the extra hypothesis absent from the relaxed model.
11. **Minimum criterion:** Proposition H compares genuine frozen sets only after proving a pointwise order of their actual burning labels. The direction is G⊂F* for later alternative burning. Applying the order-reversing full equation reverses that inclusion and forces equality. No comparison of arbitrary local-recursion labels is sufficient.

Lean check: `lake env lean ~/brain_workers/TRIO_1011/op/P0360/FeasibleSetIdentity.lean`, run from `~/lean_verify`, checks the branching membership identity and the order argument excluding comparable distinct antitone fixed points. Imports are `Mathlib.Data.Set.Basic`, `Mathlib.Order.MinMax`, and `Mathlib.Order.Monotone.Basic`. Final exit code is 0, recorded in `feasible_lean_check.txt`. No `sorry` or `native_decide` is used. The measure-theoretic and global percolation arguments are written proofs, not claimed to be Lean formalizations.

## Final outcome of the additional attempt

PARTIAL. New proved results are the intrinsic feasible-set reduction and scalar identities (Proposition D), a precise counterexample to a relaxed auxiliary uniqueness assertion (Proposition E), endogenous convergence of the unique finite-time approximations with explicit marginal/prefix bounds (Proposition F), and scalar criteria for full uniqueness (Propositions G and H).

None is a proof or counterexample for P0360. The unresolved inequalities are a_n≤(1−θ)θ^n/(1+θ), or equivalently H(θ^n)≤θ^n/(1+θ), for genuine feasible sets in the endogenous regime. Equivalently, one must exclude genuine solutions inaccessible to the finite-cutoff limit. The θ<1/2 conjecture remains unresolved here, as does the larger endogenous regime.
