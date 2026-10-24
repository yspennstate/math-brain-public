# BT4 account02/B20 — global missing-arc saturation and a count-only obstruction

Run: `20260922T000112Z-account02-B20-r11`
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`
Campaign: `BT4`
Outcome on main candidate: `ESSENTIAL_STEP_APPLIED`
Full-target movement: `NONE` — this is not a proof of BT4.
Mechanism result: `BT4-FAN-ONLY-v1` is refuted; the surviving candidate is `BT4-GLOBAL-SWITCH-v2`.
Brain status: `WITHOUT_VERIFIED_BRAIN`.

## Source-exact target and consumed peer

Target: every finite loopless digraph with at most one arc per ordered pair and minimum outdegree at least seven contains four vertex-disjoint genuinely directed cycles; opposite arcs and digons are allowed.

This run substantively consumes account01/B04's completed source-bound result `BT4-MCR-v1`, canonical report
`proofnet24/collective-BT4/account01/B04/20260921T234516Z-b04-8fd1d4/report.md`,
math-open-problems commit `8a71d11efa2a3110db78c39684ea4c9cce03a28b`.
That report establishes, for a vertex-minimal then arc-maximal counterexample D, that D is oriented and strongly connected; there is a minimum-total three-cycle packing C1,C2,C3 leaving a DAG R of at least three vertices; the packed cycles are chordless; the t=1,2,3 deletion hierarchy forces 3/5/7-fan witnesses; and for x in R, if m_i(x)=|N+(x)∩C_i|, then any C_i-to-x path with all internal vertices in R has length at least m_i(x)-1. In particular m_i(x)>=3 forbids every direct C_i->x arc.

The assigned partner account04/B06 had started its first BT4 run during this invocation, but no finalized mathematical result from it was available when this derivation was completed, so no start/check-in is treated as scientific uptake.

## 1. Complementary five-fan cascade

Fix the minimum-total packing C1,C2,C3 from `BT4-MCR-v1`. For {i,j,k}={1,2,3}, define the residual outdegree after deleting the other two packed cycles by

    q_i(v) = d^+_{D-(C_j union C_k)}(v),    v in C_i union R.

Because the k=2 Bermond-Thomassen case is known at minimum outdegree three, a BT4 counterexample cannot have q_i(v)>=3 for every remaining vertex: otherwise D-(C_j union C_k) contains two disjoint directed cycles, and C_j,C_k supply two more. Hence for every i there exists a witness w_i in C_i union R with

    q_i(w_i) <= 2.

Since d_D^+(w_i)>=7, w_i sends at least five arcs into C_j union C_k.

This splits exactly:

* If w_i is in C_i, chordlessness of C_i gives exactly one internal outneighbor, so
      d_R^+(w_i) <= 1
  and w_i has at least five outneighbors in C_j union C_k.

* If w_i is in R, writing m_h(w)=|N^+(w)∩C_h|,
      d_R^+(w_i)+m_i(w_i) <= 2,
      m_j(w_i)+m_k(w_i) >= 5.
  Therefore one of m_j(w_i),m_k(w_i) is at least three. By the one-vertex exchange lemma from the consumed B04 result, that heavy packed cycle has no direct arc into w_i.

Now let x be a sink of R and suppose C_i is heavy at x: m_i(x)>=3. Since d_R^+(x)=0, q_i(x)=m_i(x)>=3, so the complementary witness w_i is necessarily distinct from x. Thus every heavy sink forces either

(A) a packed-cycle switch vertex w_i in C_i with at most one R-outarc and at least five arcs into the other two packed cycles, or

(B) a distinct R-vertex w_i almost detached in the C_i direction but heavy (>=3) toward one of the other packed cycles, which in turn forbids direct return from that new heavy cycle.

This is a genuine consequence of the full counterexample hypothesis and sharpens the t=2 five-fan statement into a location-sensitive switching dichotomy.

## 2. Why five-fan counts alone cannot force the short return

The natural next hope in `BT4-MCR-v1` was that the three t=2 five-fan inequalities, plus the local path-fan exchange constraint, might numerically force the missing short return. They do not.

The attached exact construction `bt4_fan_only_countermodel.py` builds an 18-vertex oriented digraph with three designated chordless directed 5-cycles C1,C2,C3 and R={x1,x2,x3}. Its pure-stdlib checks verify:

* minimum outdegree is 7;
* the graph is strongly connected;
* R is an independent DAG, hence every x_s is a sink;
* the sink signatures are
      x1: (m1,m2,m3)=(2,3,2),
      x2: (2,2,3),
      x3: (3,2,2);
* the corresponding heavy cycles C2,C3,C1 have no arc into x1,x2,x3 respectively, exactly matching the local one-vertex exchange consequence;
* x1 is a valid t=2 witness for residual C1 (q1=2, five arcs into C2 union C3), x2 for residual C2, and x3 for residual C3.

Because R has no arcs and the heavy cycles have no direct arcs to their corresponding sinks, none of these heavy sink/cycle pairs has an R-internal return path at all. Thus the local fan-count + chordless + strong-connectivity + DAG + heavy-no-direct package does not imply the short-return obligation.

The construction deliberately is NOT a BT4 counterexample. The checker exhibits four vertex-disjoint directed cycles:

    (a0,b0,c0),
    (a1,a2,c4),
    (a4,b1,a3),
    (b2,c2,x1).

This is the decisive point: the missing ingredient is exactly the global no-four-cycle condition, not another optimization of the 3/5/7 fan counts. Therefore `BT4-FAN-ONLY-v1` is refuted as a proof mechanism without making any claim against BT4 itself.

Exact artifacts:
* `bt4_fan_only_countermodel.py` SHA-256 `6d57ce6dcb23b057a7599dadde79398be82bdc7786edf18784af5f09846bf5a7`
* `bt4_fan_only_countermodel_output.json` SHA-256 `670428a049f86fcd443f6b515d56b789346b996d323a30664a115afcad8e44a5`

## 3. Global missing-arc saturation lemma

The no-four-cycle hypothesis can be injected through arc maximality, and it gives a new exact return certificate.

**Lemma (saturation return certificate).**
Let x be a sink of R and let C_i be heavy at x with m=|N^+(x)∩C_i|>=3. Then no vertex of C_i sends an arc to x. Fix b in C_i with x->b absent. Add the missing arc x->b. Since D was chosen arc-maximal among vertex-minimal counterexamples, D+x->b contains four vertex-disjoint directed cycles. At least one of them uses the new arc, because D itself has no four-cycle packing. Call that cycle Q.

Deleting the new edge from Q leaves a directed path P from b to x entirely in D. Also |Q|>=3, because b->x is absent. The other three cycles of the four-packing lie in D and are disjoint from Q, so they form an admissible three-cycle packing leaving at least |Q|>=3 vertices. By minimum-total choice of C1,C2,C3,

    |C1|+|C2|+|C3| <= n-|Q|.

Since |R|=n-(|C1|+|C2|+|C3|),

    |Q| <= |R|,

and therefore the return path P has length

    |P| = |Q|-1 <= |R|-1.

This uses the global no-four-cycle assumption in an essential way.

If P, after its last vertex on C_i, avoids the other packed cycles and runs only through R to x, then the consumed B04 path-fan lemma applies to that suffix and gives

    m <= |P_suffix|+1 <= |R|.

Consequently, whenever m>|R| and x does not dominate all of C_i, every missing-arc saturation certificate x->b is forced to switch through at least one of the other packed cycles before reaching x. If x dominates all of C_i, strong connectivity plus the same path-fan bound shows that an R-only return is impossible whenever m>|R|+1, so that branch is also forced into a packed-cycle switch in the large-m regime.

This is the first applied global inference beyond `BT4-MCR-v1`: the obstruction is no longer merely “find a short return.” It is now a quantified dichotomy between an R-internal return bounded by |R| and a forced visit to another packed cycle.

## 4. Surviving candidate and next exact obligation

The surviving version is `BT4-GLOBAL-SWITCH-v2`:

1. keep the minimal/arc-maximal counterexample and minimum-total 3-packing from `BT4-MCR-v1`;
2. use the complementary five-fan cascade above to locate low-forward/high-cross witnesses;
3. use the saturation-return certificate for missing x->b arcs at a heavy sink;
4. analyze the first visit of a saturation path to a different packed cycle and prove a **two-cycle exchange** that either
   (a) produces an R-internal return shorter than m-1, contradicting the path-fan lemma, or
   (b) replaces two packed cycles by two disjoint directed cycles while freeing enough vertices to create a smaller admissible three-packing.

The count-only witness proves that step 4 must use the global no-four-cycle/packing-saturation geometry. Merely summing the t=2 five-fan inequalities cannot close it.

The next recipient should therefore work on the exact first-switch geometry: given a saturation path b in C_i -> ... -> C_j -> ... -> x and the three untouched cycles supplied by D+x->b, identify a disjoint splice/bypass that either removes the C_j switch or creates a strictly smaller three-cycle packing. This is the remaining essential step; BT4 remains open.
