# BT4 fleet03/B04 — seven-budget extremal normalization and strengthened two-cycle obstruction

Run: `20260922T001544Z-fleet03-B04-r11`
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`
Campaign: `BT4`
Outcome: `ESSENTIAL_STEP_APPLIED`
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and source status

Target: prove that every finite loopless digraph with at most one arc per ordered pair, minimum outdegree at least seven, and opposite arcs allowed contains four vertex-disjoint genuinely directed cycles.

Current source check: Bessy, Muis, Sereni, Steiner and Wiederrecht, *A relaxation of the Bermond-Thomassen conjecture*, arXiv:2608.12948 (13 Aug 2026), states that the exact conjecture remains unresolved for every k>=4 and proves only the near-directed relaxation at threshold 2k-1. Thus BT4 remains open as of the source check for this run.

Inputs used:
- Lichiardopol, Por and Sereni, *A Step toward the Bermond-Thomassen Conjecture about Disjoint Cycles in Digraphs*, SIAM J. Discrete Math. 23 (2009), 979-992, DOI 10.1137/080715792. Besides k=3 (minimum outdegree 5 gives three disjoint directed cycles), its abstract records the stronger k=2 input used below: every digraph in which all vertices have outdegree at least 3 except at most two vertices of outdegree 2 contains two disjoint cycles.
- Bang-Jensen, Bessy and Thomasse, *Disjoint 3-Cycles in Tournaments: A Proof of the Bermond-Thomassen Conjecture for Tournaments*, J. Graph Theory 75 (2014), 284-302, DOI 10.1002/jgt.21740: every tournament with minimum outdegree at least 2k-1 contains k disjoint directed 3-cycles.

## Exact other-account artifact consumed

Consumed before deriving the new step:

`proofnet24/collective-BT4/fleet01/B04/20260921T234516Z-b04-8fd1d4/report.md`

Git blob: `05c8cc232a9706214937f6eff31b85464a498859`.

That report established a useful minimum-three-cycle-packing exchange lemma and the path-fan inequality, and explicitly identified the two-cycle deletion obstruction as a pressure point. This run strengthens that pressure point using the exceptional-vertex form of the 2009 k=2 theorem, and develops a deliberately different arc-minimal / shortest-cycle normalization.

Important compatibility warning: fleet01/B04 chose a vertex-minimal and then ARC-MAXIMAL counterexample to obtain its missing-arc packing consequence and |R|>=3. Here I choose a vertex-minimal and then ARC-MINIMAL counterexample to force exact outdegree seven. Those two secondary extremal choices must not be silently combined. The minimum-total packing exchange lemma itself can still be reused when its stated hypotheses hold.

## 1. Arc-minimal seven-budget normalization

Assume BT4 has a counterexample. Choose D with minimum |V(D)|, and subject to that with minimum |A(D)| among counterexamples satisfying delta^+(D)>=7.

### Lemma 1.1 — exact 7-outregularity

Every vertex of D has outdegree exactly 7.

Proof. If some v had d^+(v)>=8, delete any one outgoing arc from v. Every vertex would still have outdegree at least 7, and deleting an arc cannot create four disjoint directed cycles. This would be a counterexample on the same vertex set with fewer arcs, contradicting arc-minimality. QED.

### Lemma 1.2 — no digons

D is oriented.

Proof. If x<->y is a digon, then deleting x,y reduces every surviving outdegree by at most two, so delta^+(D-{x,y})>=5. The known k=3 theorem yields three vertex-disjoint directed cycles in D-{x,y}; with the digon this gives four in D. QED.

### Lemma 1.3 — strong connectivity

D is strongly connected.

Proof. Otherwise a sink strongly connected component S has no outgoing arc to V(D)\S. Hence every vertex of S still has all seven outneighbors in S. Since S is proper, vertex-minimality says D[S] cannot be a counterexample, so D[S] contains four disjoint directed cycles. QED.

### Corollary 1.4 — order floor

|V(D)|>=16.

Indeed D is oriented and 7-outregular, so 7n=|A(D)|<=n(n-1)/2, hence n>=15. Equality n=15 forces an orientation on every unordered pair, i.e. D is a tournament; the tournament theorem at k=4 then supplies four disjoint directed 3-cycles. Therefore n>=16.

This normalization is useful because every later residual-degree inequality becomes an exact seven-unit budget rather than a one-sided lower bound.

## 2. Shortest-cycle heavy/light structure

Let C be a globally shortest directed cycle of D, with g=|C|, and put H=D-C. Define

    a_C(v)=|N_D^+(v) intersect V(C)|

for v outside C. Call v C-heavy if a_C(v)>=3 and C-light if a_C(v)<=2.

### Lemma 2.1 — C is induced as a directed cycle and sends exactly six arcs per vertex outside

Every c in C has precisely its successor as an outneighbor on C. Hence, by 7-outregularity,

    d_H^+(c)=6.

Proof. Any additional arc c_i->c_j between nonconsecutive vertices of C closes with the appropriate directed section of C to form a strictly shorter directed cycle (the predecessor case would be a digon, already excluded). QED.

### Lemma 2.2 — a heavy vertex cannot receive an arc from C

If v outside C and a_C(v)>=3, then there is no arc from C to v.

Proof. Suppose b->v with b in C. For every a in N^+(v) intersect C, the walk b->v->a followed by the directed C-segment a->...->b is a directed cycle. Shortestness of C forces that segment to have at least g-2 edges. Therefore every such a must be among the first two successors of b on C, giving a_C(v)<=2, contradiction. QED.

### Lemma 2.3 — heavy vertices exist

There is at least one C-heavy vertex.

Proof. If every v outside C were light, then deleting C would reduce every surviving outdegree by at most two. Hence delta^+(H)>=5, so the k=3 theorem would give three disjoint cycles in H; together with C they form four. QED.

Consequently every one of the six outside outneighbors of each c in C is C-light.

### Lemma 2.4 — the remainder is 4-outdegenerate in the directed minimum-degree sense

Every nonempty induced subdigraph J of H has a vertex of outdegree at most 4 inside J. Equivalently, H has an ordering v_1,...,v_h such that

    d^+_{D[{v_i,...,v_h}]}(v_i) <= 4

for every i.

Proof. If some induced J subset H had minimum outdegree at least 5, the k=3 theorem would give three disjoint directed cycles in J, disjoint from C, producing four in D. Repeatedly remove a vertex of current outdegree at most four. QED.

Using exact d_D^+=7, this ordering satisfies the explicit budget

    d_C^+(v_i) + d^+_{ {v_1,...,v_{i-1}} }(v_i) >= 3.       (2.1)

In particular d_C^+(v_1)>=3, d_C^+(v_2)>=2 and d_C^+(v_3)>=1.

### Lemma 2.5 — light-corridor existence and terminal fan bound

Let X be the C-heavy vertices and Y=V(H)\X. There is a directed C-to-X path whose internal vertices lie in Y. If

    P: c_0 -> p_1 -> ... -> p_{L-1} -> x

is a shortest such path, where x in X and L is its number of edges, then

    a_C(x) <= min(g,L+1).

In particular L>=a_C(x)-1>=2.

Proof. Every y in Y has at most two outneighbors on C, hence at least five outneighbors in H. Let R be the set of light vertices reachable from C by a path that stays in Y after leaving C. It is nonempty by Lemmas 2.1 and 2.2. If no vertex of R sent an arc to X, then every H-outneighbor of every y in R would again be a reachable light vertex, so D[R] would have minimum outdegree at least five. The k=3 theorem would give three disjoint cycles in R, plus C, contradiction. Hence such a path to X exists.

For the bound, fix a in N^+(x) intersect C. Appending x->a and the directed C-segment a->...->c_0 to P gives a directed cycle. Shortestness of C forces its length to be at least g. If L+1<g, this places every possible a among the first L+1 successors of c_0, so there are at most L+1 choices; if L+1>=g the trivial bound a_C(x)<=g suffices. QED.

This is a shortest-cycle version of the path-fan obstruction which does not use the arc-maximal normalization from fleet01/B04.

## 3. New strengthened two-cycle deletion obstruction

This is the main new reusable step of the run.

Let A and B be ANY two vertex-disjoint directed cycles in a BT4 counterexample D, and put

    T = D - (V(A) union V(B)).

T cannot contain two vertex-disjoint directed cycles, since together with A and B they would give four in D.

The 2009 Lichiardopol-Por-Sereni theorem says that a digraph has two disjoint cycles if every vertex has outdegree at least 3 except possibly two vertices of outdegree 2. Taking the contrapositive gives the following exact dichotomy.

### Lemma 3.1 — 6-fan / three-5-fan dichotomy

For every pair A,B of disjoint directed cycles in D, at least one of the following holds:

1. there exists v in T with d_T^+(v)<=1, hence

       |N_D^+(v) intersect (V(A) union V(B))| >= 6;

2. there exist at least three DISTINCT vertices v_1,v_2,v_3 in T with d_T^+(v_s)<=2, hence for each s

       |N_D^+(v_s) intersect (V(A) union V(B))| >= 5.

Proof. If neither held, every vertex of T would have outdegree at least 2, at most two vertices would have outdegree exactly 2, and every other vertex would have outdegree at least 3. The cited theorem would give two disjoint cycles in T, impossible. Since D is 7-outregular, deleting A union B removes exactly 7-d_T^+(v) outgoing neighbors from v, yielding the displayed 6/5 bounds. QED.

Remark: even without arc-minimality, minimum outdegree at least seven would still give the same lower bounds. Exact 7-regularity matters later when several witness inequalities are combined.

This strictly strengthens the basic pair-deletion statement “some residual vertex sends at least five arcs into A union B”: either one witness sends at least six, or there are three distinct five-fan witnesses.

## 4. Three-cycle certificate system and witness reuse

Take any three vertex-disjoint directed cycles C_1,C_2,C_3 (existence follows already from the k=3 theorem), and define

    a_i(v)=|N_D^+(v) intersect V(C_i)|.

Apply Lemma 3.1 separately to the three pairs {C_1,C_2}, {C_1,C_3}, {C_2,C_3}. Each pair therefore carries either one 6-fan certificate or three distinct 5-fan certificates in the complement of that pair.

A vertex lying on C_k can only witness the pair excluding C_k. Hence a witness reused for two different pair certificates necessarily lies outside all three cycles.

### Lemma 4.1 — overlap amplification

Suppose v is outside C_1 union C_2 union C_3 and, for distinct i,j,k,

    a_i(v)+a_j(v) >= p,
    a_i(v)+a_k(v) >= q,

where p,q are each 5 or 6. Then

    a_i(v) >= p+q-7.

Thus the possible threshold combinations force

    (p,q)=(5,5)  => a_i(v)>=3,
    (6,5)        => a_i(v)>=4,
    (6,6)        => a_i(v)>=5.

Proof. Since d_D^+(v)=7,

    a_i(v)+a_j(v)+a_k(v) <= 7.

Adding the two pair inequalities gives

    2a_i(v)+a_j(v)+a_k(v) >= p+q,

so a_i(v)>=p+q-(a_i+a_j+a_k)>=p+q-7. QED.

If C_1,C_2,C_3 are chosen as a minimum-total three-cycle packing and v lies in its acyclic remainder, then fleet01/B04's packing-exchange lemma applies: the first line above already makes v heavy on the common cycle C_i, so no vertex of C_i can send an arc directly to v; the 6+5 and 6+6 overlaps strengthen the corresponding path-fan lower bound to at least 3 and 4 edges respectively before v can be reached from C_i through the remainder.

This turns reuse of the new pair-deletion certificates into an explicit blocked-return condition instead of another unquantified “high degree into the packing” statement.

## 5. Exact first unpaid implication

The next step is NOT to reprove the basic deletion witness. It is to resolve the following certificate-system alternative for a minimum-total three-cycle packing:

> For the three pair-deletion certificates supplied by Lemma 3.1, either force a reused remainder witness and exploit Lemma 4.1 plus the directed path-fan exchange, or prove that a configuration in which the certificates stay separated on the complementary packed cycles has enough cross-cycle saturation to admit a simultaneous disjointness-preserving rerouting/shortening.

The first branch now has quantitative thresholds 3/4/5 on the common cycle. The second branch is the precise object to hand to the packing-exchange workers: a five-fan certificate carried by a vertex of the third packed cycle means that vertex sends at least five arcs into the other two cycles; a six-fan certificate means at least six. These are much stronger than an average-degree statement and retain the original seven-outdegree budget.

I have NOT proved that one of these branches already closes BT4. In particular, the pair certificates are existential and may choose different witnesses, and a saturated vertex lying on the third packed cycle cannot be fed directly into the one-vertex replacement lemma without repairing disjointness. That is the remaining exchange problem.

## Outcome

`ESSENTIAL_STEP_APPLIED`.

New rigorous content in this run:

1. an alternative arc-minimal normalization giving exact 7-outregularity, orientation, strong connectivity and n>=16;
2. a shortest-cycle heavy/light decomposition with an exact six-outgoing budget, 4-outdegenerate remainder, light-corridor existence and terminal fan bound;
3. most importantly, a source-backed strengthening of the two-cycle deletion obstruction from one 5-fan witness to the **6-fan / three-distinct-5-fan dichotomy**;
4. the exact overlap-amplification formula `a_i >= p+q-7`, converting reuse of pair certificates into a 3/4/5-heavy common-cycle obstruction.

No full BT4 proof is claimed. No novelty claim is made. The next recipient should attack the separated-certificate cross-cycle exchange rather than repeat the elementary minimum-degree reductions.
