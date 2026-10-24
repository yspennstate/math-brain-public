# P0360 — unrestricted uniqueness of frozen percolation

Date: 2026-10-11. All assertions below are local results, not a solution of Question 1.

## Exact model and question

The source is B. Ráth, J. M. Swart and M. Szőke, *A phase transition between endogeny and nonendogeny*, arXiv:2103.14408v2; Electronic Journal of Probability 27 (2022), DOI 10.1214/22-ejp872. Page numbers below refer to the downloaded arXiv PDF.

Let T be the binary word tree. The innovations (τ_i,κ_i) are independent and uniform on [0,1]×{1,2}. At κ_i=1 only child i1 is legal; at κ_i=2 both children are legal. Let I={i:κ_i=1}, B={i:κ_i=2}, and T_t=B∪{i∈I:τ_i≤t}. Write P_A(i,t) for existence of an infinite legal path from i entirely in T_t\A, including i. Fix a relatively closed deterministic Ξ⊂(0,1]. A solution is a random subset F⊂T such that, simultaneously at all vertices,

    i∈F ⇔ κ_i=1 and ∃t∈Ξ, t≤τ_i, P_F(i1,t).

The canonical solution is stationary, adapted and respects the tree structure, with burning times Y_i=inf{t∈Ξ:P_F(i,t)}. Its RTP is endogenous if Y_root is measurable in the innovations. Question 1 (PDF p.8) asks whether this implies equality almost surely of ANY two solutions driven by the same innovations, with none of those three restrictions. The question is not limited to geometric Ξ. For Ξ_θ={θ^n:n≥0}, Theorem 9 (p.9) gives endogeny for 0<θ≤θ_*≈0.636; the source separately conjectures unrestricted uniqueness and alternating-envelope collapse for θ<1/2.

## Proposition A: uniqueness for well-ordered freezing sets

If Ξ is well ordered by the usual order on the real line, unrestricted solutions are almost surely unique. Relative closedness is retained for the source model, but the proof of uniqueness does not require it. This extends the source's elementary finite-set observation; it does not include Ξ_θ.

Proof. First Ξ is countable. For each nonmaximal t∈Ξ its strict upper subset has a least element s(t)>t. Choose a rational in (t,s(t)). These disjoint intervals assign distinct rationals to distinct nonmaximal elements. There is at most one maximal element. Thus countability follows. Because T and Ξ are countable and each τ_i is continuous, with probability one τ_i≠t for every i∈T and t∈Ξ. Fix such an innovation realization and any two sets F,G satisfying the equation. Both sets are subsets of I.

Let D={t∈Ξ:∃i∈T, P_F(i,t)≠P_G(i,t)}. If D is nonempty it has a least element t. For any i∈T_t, branching vertices belong to neither F nor G. If i is internal then τ_i≤t, and in fact τ_i<t. Every s∈Ξ with s≤τ_i is strictly below t. By minimality of t, P_F(i1,s)=P_G(i1,s) for each such s. The defining equation therefore gives i∈F iff i∈G. Consequently T_t\F=T_t\G. Their percolation predicates are identical, contradicting t∈D. Hence D is empty. Applying the equation again, at each vertex the existence predicates defining membership in F and G agree, so F=G. This argument applies to all solution pairs on the same probability-one set of innovations, even if the sets have additional randomness. QED.

Example: Ξ={1/2}∪{1−1/(n+2):n≥1}∪{1} is relatively closed and well ordered, with order type ω+1. Proposition A covers this infinite set and arbitrary jointly defined solutions.

## Proposition B: descending alternating disagreement paths

Assume Ξ is countable and τ_i∉Ξ at every vertex. If F,G are distinct solutions, then there is an infinite legal ray containing successive internal vertices v_n and a strictly decreasing sequence t_n∈Ξ such that

    t_(n+1) ≤ τ_(v_n) < t_n.

The ray alternates between segments open in F at t_n and segments open in G at t_(n+1). In particular for Ξ_θ, t_n→0. Every internal activation time along the tail of this ray tends to zero (in the precise sense: for each ε>0, all internal vertices sufficiently far along the ray have activation ≤ε).

Proof. Distinct solutions give a vertex whose membership differs. The freezing equation supplies a time t_0 and a child u_0 where percolation differs: one solution has a witness, whereas the nonfreezing solution has no witness at any allowed time ≤the activation of that vertex. Relabel F,G so that P_F(u_0,t_0) holds and P_G(u_0,t_0) fails. Select an infinite legal path from u_0 in T_(t_0)\F. At least one vertex on it belongs to G, for otherwise this very path would witness P_G(u_0,t_0). Choose the first such vertex v_0. It is internal, is not in F, and has τ_(v_0)≤t_0, hence τ_(v_0)<t_0. Since v_0∈G, its freezing equation supplies t_1∈Ξ with t_1≤τ_(v_0) and P_G(v_01,t_1). Since v_0∉F and is internal, P_F(v_01,t_1) fails. This repeats the original situation with the roles reversed, starting at the legal child of v_0, at the strictly earlier time t_1.

Iterate, each time selecting the first obstructing vertex on a witnessing infinite path and a witness time for its freezing. For countable Ξ a witness can be selected using any fixed enumeration of Ξ; no minimum witness is needed. Concatenate the finite initial path segment through v_n with the segment starting at its legal child. Each step advances at least one edge, so concatenation is an infinite legal ray. Every internal vertex of segment n is activated by t_n. This proves the assertions except the geometric limit. Write t_n=θ^(k_n). Strict decrease implies k_(n+1)>k_n, so k_n≥k_0+n and t_n≤θ^(k_0+n)→0. The activation-tail assertion follows from the segment bound. QED.

## Why Proposition B is not a proof for geometric sets

It would be invalid to say iid continuous activation times exclude rays whose activations tend to zero. Rays are selected using the entire innovation field; a fixed-ray probability-zero argument does not control all rays. Moreover even an ordinary open path at fixed time ε has positive survival probability for every ε>0: the offspring distribution of its open-vertex exploration has probabilities p_2=1/2, p_1=ε/2, p_0=(1−ε)/2, with mean 1+ε/2>1 and extinction probability 1−ε. Thus a uniform subcritical domination at small times is unavailable. Proposition B supplies only a necessary condition, not existence of a competing solution or an exclusion theorem.

## A recursive-equation shortcut that fails

The local burning recursion is χ[τ,1](x,y)=x if x>τ and ∞ otherwise, and χ[τ,2](x,y)=min(x,y). The assignment Y_i=∞ at every vertex satisfies this recursion for every innovation realization. It does NOT correspond to the actual burning times of a solution: the recovered frozen set would be empty. For empty F, at time 1 all legal vertices are open, and every legal tree has an infinite path (each vertex has at least child 1), so Y_i≤1 whenever 1∈Ξ. Also the freezing equation fails at every internal vertex with an allowed time below its activation. Thus unrestricted fixed points of the local recursion are a larger class than frozen-percolation solutions. A counterexample using only that recursion would not answer the question.

## Proposition C: the weaker ray obstruction actually occurs

Almost surely the innovation tree has, from every vertex, an infinite legal ray along which internal activation times tend to zero. This ray is not asserted to be a disagreement ray of two solutions. It shows that the activation-tail conclusion of Proposition B alone cannot rule out nonuniqueness, for any θ.

Proof. Explore ordinary percolation T_t breadth first, placing the root in an unexamined frontier. A processed branching vertex gives two unexamined legal children; an internal vertex with τ≤t gives one; an internal vertex with τ>t gives none. Thus frontier sizes Z_n form a Galton–Watson process with generating function f_t(z)=(1−t)/2+(t/2)z+z²/2. For t>0 its extinction probability is the smaller root of f_t(q)=q, namely q=1−t. To justify this characterization directly, the probability of extinction by generation n is f_t iterated n times at 0; its increasing limit is the least fixed point in [0,1]. Nonextinction is equivalent to an infinite open legal path by finite branching (König's lemma). Hence a fresh subtree percolates at time t with probability t.

On nonextinction the frontier is unbounded. Here is an elementary proof valid also at t=1. Fix an integer M≥1. If 1≤Z_n≤M, then the event that every processed vertex during the next M generations is branching has conditional probability at least c_M=2^(−M(2^M−1))>0. On that event Z_(n+M)=2^M Z_n>M. Therefore the conditional probability of staying in [1,M] for a whole further block of M generations is at most 1−c_M. Iterating the bound proves that the process cannot stay in [1,M] forever. Starting at Z_0=1, nonextinction therefore forces hitting arbitrarily large frontier sizes.

Fix 0<δ<t≤1 and a vertex u. On the event u percolates at t, its reachable open t-cluster contains a vertex that percolates at δ. Indeed, let N_M be the first exploration generation with Z_(N_M)≥M. Its frontier nodes are unexamined; conditional on the exploration up to that generation, their entire descendant innovation subtrees are independent copies of the original field. Each frontier node percolates at δ with probability δ. The conditional probability that none does is (1−δ)^(Z_(N_M))≤(1−δ)^M. Each frontier node is reachable from u by a legal path whose proper ancestors are open at t. A node that percolates at δ is itself open at t too. Thus, if the t-cluster contains no δ-percolating vertex, none of the frontier nodes can δ-percolate. Intersect with {N_M<∞} and average to bound this failure probability by (1−δ)^M. On t-percolation N_M<∞ for every M. Sending M→∞ proves the claim.

Choose any deterministic decreasing sequence t_0=1>t_1>t_2>...→0, for example t_n=θ^n. Apply the preceding probability-one implication simultaneously for all vertices and all pairs (t_n,t_(n+1)); this is a countable intersection. Every root percolates at t_0=1, since each vertex has a legal child and all vertices are open. Suppose u_n percolates at t_n. It has a legal child w_n that percolates at t_n, by taking the first edge of an infinite witnessing path. Apply the implication at w_n to find a vertex u_(n+1) reachable from w_n in T_(t_n), percolating at t_(n+1). Connect u_n to u_(n+1) by that finite open path. The endpoint is a strict descendant of u_n. Concatenating these paths gives an infinite legal ray; internal vertices in segment n have activation at most t_n. Consequently their activation times tend to zero. The same construction works simultaneously from every vertex. QED.

This does not construct F or G: Proposition B additionally imposes alternating openness, freezing witnesses and absence of percolation in the opposite solution. Proposition C verifies only that a proposed weaker exclusion argument fails.

The conclusion is nonvacuous: almost surely every legal ray contains infinitely many internal vertices. Indeed, the same exploration at t=0 has generating function (1+z²)/2, whose only fixed point in [0,1] is 1, so it becomes extinct almost surely. A countable intersection over all vertices rules out any infinite all-branching tail.

`percolation_checks.py` checks the offspring normalization and fixed-point polynomial exactly with rational arithmetic for t=0,1/100,1/4,1/2,3/4,1. It also computes 2,000 iterations of f_t at 60 decimal digits and exact finite-frontier failure bounds, saved in `percolation_checks.json`. For example δ=1/100 and frontier size 1,000 give failure bound (99/100)^1000≈4.3171×10^(-5). These are sanity checks of Proposition C's inputs, not experiments on the original uniqueness question.

## Referee checks

1. All fixed-set arguments use the full frozen equation, not just its local burning recursion. The all-infinite recursion assignment above diagnoses that distinction.
2. The no-tie event is invoked only for countable deterministic Ξ. Proposition A first proves countability. Proposition B assumes it; no claim for uncountable Ξ uses it.
3. The minimum in Proposition A is justified by well ordering. It is unavailable for geometric Ξ, which has strictly decreasing sequences.
4. The path switch in Proposition B is strictly downward in the tree: it restarts at the legal child of an internal obstruction. Every finite segment has positive progress; concatenation cannot cycle or terminate.
5. The frontier at the stopping generation in Proposition C is unexamined. No conditioning on survival of those frontier subtrees is used in the independence calculation. Survival is used only to ensure that N_M is finite; the upper bound is first taken on the larger event {N_M<∞}.
6. Proposition C controls ordinary percolation, not the open sets of a frozen solution. This distinction is exactly why it cannot establish nonuniqueness.
7. Lean formalizes only the abstract well-founded induction and the inequality at a switch. Verification of the abstraction's hypotheses for percolation is the written proof of Proposition A; no claim is made that the full probability argument is formalized.

Lean verification: `lake env lean ~/brain_workers/TRIO_1011/op/P0360/WellFoundedUniqueness.lean`, run from `~/lean_verify`, returned exit code 0. Output is saved in `lean_check.txt`. Only `Mathlib.Logic.Basic` and `Mathlib.Order.Basic` are imported. Neither theorem uses `sorry`, `native_decide`, or an unchecked computational axiom. The first run exposed a missing order import; adding the explicit order import fixed it before the successful check.

## Remaining gap

No proof or counterexample has been obtained for the unrestricted question. In particular none of the arguments excludes the alternating disagreement cascade of Proposition B for any geometric Ξ_θ, including θ<1/2. To prove the desired implication one must exclude valid competing global frozen sets under endogeny, rather than merely prove bivariate uniqueness within the canonical RTP law. Endogeny controls that law; no argument here puts arbitrary solutions in that law or gives uniform control over their boundary conditions.

## Additional serious attempt requested by the user

See `SECOND_ATTEMPT.md` for two new approaches and complete proofs of Propositions D–H. Intrinsic genuine feasible-state sets restore subtree independence and give the exact identity a_n=θ^n+2b_n−2, with canonical mass p_n≤a_n≤θ^n. A larger explicitly characterized relaxed set-valued solution demonstrates why these local equations cannot force physical uniqueness. The unique finite-cutoff genuine solutions converge in probability to the canonical solution under endogeny, with TV(ρ_N,ρ)≤(N+2)θ^(N+1)/(1+θ). Full unrestricted uniqueness is equivalent to a_n=p_n at every finite freezing time; sufficiency is proved using the actual-percolation requirement, and necessity uses measurable uniformization. An alternative criterion is H(θ^n)=θ^n/(1+θ), where H is the CDF of the minimum genuine feasible burning time. Its sufficiency uses order reversal to exclude comparable distinct frozen fixed points.

The sharpened remaining gap is to prove a_n≤p_n for genuine feasible sets in the endogenous regime, or construct a genuine solution increasing one of those probabilities. Finite-cutoff convergence does not establish that every arbitrary full-time solution lies in its limiting class. Overall verdict remains PARTIAL.
