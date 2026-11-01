# E0101: research record

Date: 2026-10-12.

## Source and exact question
Candellero and Hutchcroft, *On the boundary at infinity for branching random walk*, arXiv:2205.15287v1 (30 May 2022), Problem 4.2, PDF p. 9:
> Give conditions under which the support of W coincides almost surely with the set of accumulation points of B.

Theorem 1.1, PDF p. 2 assumes a transient, irreducible countable-state Markov chain, spatially constant independent offspring law with finite mean m>1 and E[N log N]<infinity. The measures m^{-n} B_n converge weakly almost surely on the compact metrizable Martin compactification K to W; E_x W(A)=P_x(X_infinity in A). W is a finite positive measure supported on the harmonic Martin boundary. The question concerns accumulation in the full Martin boundary, not merely its harmonic part. The source itself gives a lamplighter counterexample on p. 9. Thus universal equality is already false.

Define L={xi in K\S: there exist particles u_j at generations n_j -> infinity with positions X(u_j)->xi}. Since generations are finite and S is discrete in K, this also equals the boundary accumulation set of the complete particle trace. On extinction both L and supp W are empty.

## A sufficient condition: boundary regularity
For a relatively open boundary set V let h_V(x)=P_x(X_infinity in V).
Assume there is a countable basis V_i of the boundary topology such that, for every i and every xi in V_i,

(R) liminf_{S contains x -> xi} h_{V_i}(x) > 0.

The liminf is topological: some K-neighborhood O of xi and some c>0 satisfy h_{V_i}(x)>=c for x in O intersect S. The stronger usual Dirichlet regularity condition h_V(x)->1 for xi in V implies (R). No uniformity over xi or i, and no second moment of offspring, are required.

**Theorem.** Under the source hypotheses and (R), supp W=L almost surely.

### Proof
1. The inclusion supp W subset L requires no regularity. Work on the weak-convergence event. If xi is in supp W, every K-open neighborhood U of xi has W(U)>0. Portmanteau gives liminf_n m^{-n}B_n(U)>=W(U)>0. Consequently every such U contains particle positions at all sufficiently large times. Choose shrinking metric neighborhoods and increasing generations to obtain a sequence tending to xi. The source theorem implies supp W is a subset of the boundary (S is open and discrete and W(S)=0).

2. Let Z denote the total Galton-Watson martingale limit from one particle. Its law does not depend on the starting location, E Z=1 by the source L log L hypothesis, and W_x(V)<=Z in the same process. For c>0 choose a finite K_c with E[Z 1_{Z>K_c}]<c/2. If h_V(x)>=c, the expectation identity gives
c <= E_x W_x(V) <= K_c P_x(W_x(V)>0) + E[Z 1_{Z>K_c}].
Thus P_x(W_x(V)>0)>=c/(2K_c)=:p_c>0. This uses integrability of Z, not a second moment.

3. Use the full genealogical filtration F_n, including positions and offspring revealed through generation n, with particles labelled by finite sequences of natural numbers. For each generation-n particle u let W^u be the weak limit of its descendant process rescaled from u's birth. Simultaneously these limits exist for all actual particles: there are countably many possible labels and the theorem applies conditionally to each birth position. At each fixed n there are finitely many particles. The identity of generation measures and weak convergence then imply, as an equality of finite measures,
W = m^{-n} sum_{|u|=n} W^u.
Conditionally on F_n the descendant processes are independent and each has the one-particle law at X(u). Hence, for A={W(V)=0},
P(A|F_n) = product_{|u|=n} P_{X(u)}(W_{X(u)}(V)=0).
The empty product is 1. In particular if any generation-n particle has h_V(X(u))>=c, then P(A|F_n)<=1-p_c.

4. Since A belongs to F_infinity=sigma(union_n F_n), the bounded conditional-expectation martingale P(A|F_n) tends almost surely to 1_A. On A, therefore, there can be only finitely many generations containing a particle with h_V>=c. Apply this statement simultaneously to every basis V_i and c=1/j (j a positive integer). There are countably many such pairs, so the resulting event has probability one.

5. On that event suppose xi in L but xi not in supp W. There is a K-open neighborhood U of xi with W(U)=0 and a basis V_i with xi in V_i subset U intersect boundary; thus W(V_i)=0. By (R) there exist a neighborhood O of xi and c>=1/j>0 with h_{V_i}>=1/j on O intersect S. A particle sequence tending to xi enters O at infinitely many generations, contradicting step 4. Therefore L subset supp W. Together with step 1 this proves equality. All sets V_i are Borel subsets of K, as the boundary is closed.

## Referee checks already passed
- A null mass in a direction need not mean zero mass in every neighborhood: the proof only uses open neighborhoods and support.
- Selecting an accumulation point after observing the BRW does not cause an uncountable exceptional-event problem: all probability-one assertions are indexed by a countable basis and positive rational thresholds.
- A particle can have an extinct subtree. Step 2 retains a fixed positive unconditional success probability and step 4 handles arbitrary dependence across visits.
- Visits at random times need no stopping-line independence: deterministic-time conditional probabilities converge on the zero-mass event.
- A single fast genealogical ray can have zero genealogical mass. The proof never assigns positive mass to a single ray.
- The proof does not assert a converse to (R). It does not treat irregular Martin boundary points.
- Earlier intake E0101-A001 asserted a directional-uniform-integrability equivalence without proof. It is not used here. Integrability of the spatially invariant total mass is sufficient for step 2; the missing issue is boundary accessibility, not automatically directional UI.

## Interim tasks (completed below)
Literature checks, concrete regular-tree and hyperbolic-group applications, and the tree proof are completed below. No complete classification of irregular chains is proved.

## Concrete corollary: simple random walk on a regular tree
Let T have degree q+1 with integer q>=2. For every supercritical offspring law satisfying E[N log N]<infinity, the limiting Martin-boundary measure has support equal to the BRW accumulation set, with no restriction on the relation between m and the local-survival threshold.

Here is a self-contained verification of the needed boundary facts. For a fixed target a, until hitting a the distance R from a decreases with probability 1/(q+1) and increases with probability q/(q+1). For 0<r<L, the probability of hitting 0 before L is
f_L(r)=(q^{-r}-q^{-L})/(1-q^{-L}).
The endpoints are f_L(0)=1 and f_L(L)=0, and direct substitution gives f_L(r)=[f_L(r-1)+q f_L(r+1)]/(q+1). The finite chain exits [1,L-1] almost surely: in every L steps it has probability at least (q+1)^{-L} of exiting by consecutive downward moves. Uniqueness follows by applying the finite maximum principle to the difference of two solutions: a strictly positive interior maximum propagates to an endpoint, a contradiction; the same argument handles a negative minimum. Thus f_L is the hitting probability. As L increases, the event of hitting 0 before L increases to the event of ever hitting 0: every path that hits 0 does so at a finite time and has a finite maximum distance before then. Consequently P_x(hit a)=q^{-d(x,a)}.

Starting from a and after the first step, the chance of returning to a is 1/q. The strong Markov property at return times makes the number of visits a geometric variable with mean G(a,a)=q/(q-1). In particular visits to every vertex are finite almost surely. Applying this simultaneously to countably many vertices shows every finite ball is eventually left permanently. On a tree this implies end convergence: for every finite ball, after the last visit the path remains in a single component of its complement; the resulting nested components determine a unique end.

By the strong Markov property at the first visit to y,
G(x,y)=q^{-d(x,y)} q/(q-1).
The Martin kernel based at o is therefore
K(x,y)=q^{d(o,y)-d(x,y)}=q^{2(x|y)_o-|x|}.
If y tends to an end xi, its common-prefix length with each fixed x stabilizes and the kernel tends to q^{2(x|xi)_o-|x|}. Different ends are separated by these values: choose x beyond their splitting vertex on one end. Conversely, every sequence escaping finite balls has an end-convergent subsequence by compactness of the end compactification (finite branching and a diagonal extraction); the displayed formula identifies its Martin limit with that end. A sequence with a unique Martin limit cannot have two different end-subsequence limits, so it converges to the corresponding end. These facts identify the compactifications and their topologies, including all boundary points.

For a vertex v at depth k>=1 let C_v consist of ends whose ray from o passes through v. The C_v form a countable clopen basis. If x is in the forward subtree of v, failure to end in C_v requires hitting the parent of v. Hence
h_{C_v}(x)>=1-q^{-[d(x,v)+1]}.
When x tends to xi in C_v, x is eventually in that forward subtree and d(x,v) tends to infinity. Thus h_{C_v}(x)->1. Condition (R) holds, proving the corollary. Extinction and both weak and strong local-survival regimes are covered by the same proof.

Exact finite verification: tree_exact_check.txt records 3045 rational-arithmetic tests of the displayed recurrence and endpoint formula, for q=2,...,8 and L=2,...,30. These corroborate the algebra only; the limiting argument is proved above.

## Hyperbolic-group corollary, using established boundary theory
A second concrete class is random walk on a non-elementary word-hyperbolic group with a symmetric, finitely supported step law whose support generates the group, and spectral radius r(P)<1. More generally the argument applies whenever the Martin and geometric compactifications coincide and the latter is Dirichlet regular. Any spatially constant supercritical L log L offspring law is allowed, including at and on either side of the BRW local-survival threshold.

The boundary-theory inputs are explicitly separated from the new probability argument. Kaimanovich and Woess, arXiv:2205.13615v2, Proposition 3.38, PDF p. 24, supplies Dirichlet regularity for an end, hyperbolic or Floyd compactification with infinite boundary when Aut(X,P) acts quasi-transitively and fixes no boundary point. Their discussion of the Martin compactification on PDF p. 25, item (ii), identifies it with the hyperbolic compactification for bounded-range hyperbolic walks with r(P)<1; here the walk is uniformly irreducible as well. The same identification is recalled by the source in its introduction with Ancona references. We invoke these existing boundary-theory facts, rather than claiming new proofs of them.

Apply them to the Cayley graph using the symmetric support as generating set. The graph is locally finite and hyperbolic; left translations preserve P and act transitively. Non-elementary hyperbolicity gives an infinite boundary with no global fixed point for this action. The walk is bounded range and uniformly irreducible (the minimum positive generator probability is positive). The assumed r(P)<1 gives transience by summability of diagonal transition probabilities, and generating support gives irreducibility. Consequently the Martin compactification is Dirichlet regular.

To check precisely that this implies (R), fix boundary-open V and xi in V. Compact metrizability gives a continuous function phi on the boundary with 0<=phi<=1, phi(xi)=1, and phi=0 outside V. The unique continuous harmonic extension f of phi equals E_x phi(X_infinity): the bounded martingale f(X_n) tends to phi(X_infinity) by boundary convergence and continuity, and bounded convergence gives the equality of expectations. Therefore h_V(x)>=f(x)->1 as x->xi; since h_V<=1, it tends to 1. The regularity theorem now proves the support equality. This corollary depends only on the cited standard boundary inputs; its use of them and all ensuing steps are explicit.

## A literature discrepancy that does not invalidate the proof
Woess, arXiv:2405.07301, downloaded version, PDF p. 26, note added in proof asserts that Geldbach proved dim(supp mu_infinity)=min{2 lambda,1}, and infers strict support inclusion for lambda<1/2. Geldbach, arXiv:2509.06730v3, Theorem 1.1 and Corollary 3.2 instead concern the dimension of the measure, defined via full-measure sets; Corollary 3.2 uses a countable union of typical-ray sets. Such a union need not be closed. It therefore does not give an upper bound on the dimension of the topological support. Measures of small dimension can have full support. We do not take Woess's attribution as a proved counterexample, or use either Brownian-motion paper as a solution of the discrete source question. The discrepancy should be resolved independently before using that note in further research.

## Scope and conclusion
The source asks for conditions, not an if-and-only-if classification. Condition (R), its Dirichlet-regularity consequence, and the explicit regular-tree and standard hyperbolic-group applications provide such conditions, with a complete proof of the support equality. This is an original argument in this record, NOT a SOLVED_IN_LITERATURE finding. A necessary-and-sufficient classification for irregular Martin boundaries remains unproved and is not claimed. The source's lamplighter example already shows equality is not universal. No novelty claim beyond the bounded search is made.

## Additional boundary-case audit
The L log L assumption cannot simply be dropped, even on a regular tree. Let a_k=1/[k^2 (log k)^2] for k>=3, let A=sum_{k>=3}a_k (positive and finite), and set P(N=2)=1/2 and P(N=k)=a_k/(2A) for k>=3. These probabilities sum to one. The mean is finite because sum 1/[k(log k)^2] converges, and exceeds 2 since all N>=2 with positive probability of N>2. But E[N log N]=infinity because sum 1/[k log k] diverges. The Galton-Watson tree survives surely. Kesten-Stigum, as stated in the source, makes the normalized total mass tend to zero, so any normalized weak limit on the compactification is zero (for any bounded continuous f, its integral is bounded in absolute value by ||f|| times total mass). Meanwhile the genealogical ray obtained by always choosing the first child has the underlying simple-random-walk law and converges to a tree end almost surely by the tree proof above. Thus L is nonempty and supp W is empty. This is a counterexample ONLY to deleting the source's moment assumption, not a counterexample under that assumption.

## Final verification
MassPositivity.lean was checked with `lake env lean ~/brain_workers/TRIO_1011/op/E0101/MassPositivity.lean` from ~/lean_verify, one job at a time and with subprocess timeout 3600 seconds. Final exit code 0 is saved in lean_check.txt. It imports only three targeted Mathlib modules and contains no sorry, axiom, or native_decide. The Lean result verifies the real-algebra positivity/lower-bound step only; the measure, martingale, and boundary arguments are mathematical proofs in this document. An initial shell encoding failure changed Unicode symbols to question marks; the file was corrected and the complete corrected file passed. A harmless unused-hypothesis linter warning remains.

The finite radial recurrence was verified by exact Fraction arithmetic, not floating-point simulation. No computational claim substitutes for the infinite-time proofs. Refereeing did not reveal a gap in the sufficient-condition theorem or tree corollary. The hyperbolic corollary expressly invokes existing boundary-theory results. Necessary conditions and arbitrary irregular-boundary behavior remain outside the proved scope.
