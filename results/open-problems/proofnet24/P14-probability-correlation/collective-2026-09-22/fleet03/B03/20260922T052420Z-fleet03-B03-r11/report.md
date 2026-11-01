# FOREST / fleet03 B03 — exact expansion criterion exposes the remaining Cocks-scope dependency

**Run:** `20260922T052420Z-fleet03-B03-r11`  
**Candidate version:** `FOREST-EXPANSION-SCOPE-v4`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`  
**Target status:** OPEN externally; the team lead's internal full-proof candidate is not promoted here.

## 1. Exact assignment and other-account result consumed

The source target is the Grimmett--Winkler pairwise negative-correlation inequality for the uniform law on **all** unrooted forests of every finite simple graph, including disconnected forests, the empty forest and all forest sizes.

This run's assignment is to compute exact forest-pair counts for structured adversaries to the shared candidate and use any failure to isolate the missing structural constraint rather than return a census.

The named assigned other-account result consumed and applied is:

- `fleet04/B01`, run `fleet04-b01-20260922T043827Z-forest-r13`, report `proofnet24/P14-probability-correlation/collective-2026-09-22/fleet04/B01/fleet04-b01-20260922T043827Z-forest-r13/report.md`, blob `759684087c34ffa3a92a7f26d2d4e9584b8c5c30`, candidate `FOREST-UNIT-MINIMAL-3CONN-v2`.

That report proves exact two-cut gluing identities. For two marked edges in one bridge it reduces the outside of the bridge to a positive virtual edge activity

`lambda_i = sum_{j != i} C_j/D_j`

and then invokes the fixed-graph Cocks implication to replace unit negative correlation of the smaller augmented bridge by weighted independence correlation at activity `lambda_i`. This is the precise non-elementary step attacked here.

The current lead candidate is `FOREST-KN-COCKS-RECONCILED-v3`, fleet01/B01 run `20260922T030948Z-b01-forest-auto11`, report blob `58b8b1d8ac522a4eda7479400820e590c12f22aa`. Its all-graphs transfer likewise uses the fixed-graph statement

`unit pNC on K_n  =>  M(K_n) independence correlated`

before deleting nonedges.

## 2. New exact structural result

Let `M=M(G)` be a graphic matroid, fix distinct marked edges `e,f`, and let `g` be another edge. For integers `a>=2`, `k>=1`, define `Q_{k,a}` to be the graph consisting of the distinguished edge `g=uv` plus `k` internally vertex-disjoint `u-v` paths of length `a`. Two-sum `M` with `M(Q_{k,a})` along `g`. Graphically, after the common edge is deleted this replaces `g` by `k` internally-disjoint paths of length `a`; because `a>=2`, a simple host stays simple.

Put

`q(k,a)=k/(2^a-1)`

and

`D(k,a)=(2^a-1)^k`.

The exact two-sum calculation gives

`I(M[Q_{k,a}]) = D(k,a) I(M; y_g=q(k,a))`

when every edge of the expanded graph is assigned unit weight and all unchanged host weights are one. Replacing any collection `X` of unmarked host edges independently gives

`I(M[Q^X]) = (prod_{g in X} D_g) I(M; y_g=q_g, g in X)`.

Since the multiplicative prefactor is independent of the marked variables `e,f`, the exact Rayleigh differences satisfy

`Delta_{M[Q^X]}(1;e,f) = (prod_{g in X} D_g)^2 Delta_M(q;e,f)`.

This identity is for the ordinary independent-set polynomial of the graphic matroid, hence exactly the unrooted all-forest law required by the source problem. It does not condition on connectedness, component count or forest size.

### Density

The set

`{ k/(2^a-1) : a>=2, k>=1 integers }`

is dense in `(0,infinity)`: for any `x>0`, take `a` large and choose `k` nearest to `x(2^a-1)`. The error is at most `1/(2(2^a-1))`.

Consequently, by continuity of the Rayleigh polynomial, for a fixed host `G` and marked pair `e,f`:

> **Expanded-family criterion.** If every simple graph obtained from `G` by independently replacing each unmarked edge by one of the above `Q_{k,a}` two-terminal expansions satisfies the unit forest inequality for the inherited marked pair, then `M(G)` is I-Rayleigh for that pair at every positive real edge weighting.

Conversely, if `M(G)` has a negative weighted Rayleigh difference at some positive weighting, an arbitrarily close rational/dense gadget weighting produces a **simple unit-weight expanded graph** with a negative exact Rayleigh difference. Thus a weighted failure compiles into a source-valid unit counterexample, but generally on a larger graph.

This is the exact mechanism visible in Alejandro Erickson's 2008 Waterloo thesis, Proposition 5.2.2 and Corollary 5.2.3. The thesis explicitly describes its result as: if **all graphs** are I-negatively correlated then they are all I-Rayleigh, and says this was published independently by Cocks. The construction uses precisely the same `k/(2^a-1)` gadget family. The proof therefore requires unit negative correlation on the expanded graphs `M[Q^{E-{e,f}}]`, not merely on the original fixed host.

## 3. Exact structured count: K4 at q=2/3

This run independently checked the identity by exhaustive enumeration of **all** acyclic edge subsets.

Take host `K4` on vertices `0,1,2,3`, marked edges

`e=01`, `f=02`,

and give `g=23` activity `q=2/3`, with every other edge activity one. Exact weighted counts are

- `Z = 100/3`,
- `Z_e = 37/3`,
- `Z_f = 38/3`,
- `Z_ef = 11/3`,
- `Delta = Z_e Z_f - Z Z_ef = 34`.

Now replace `23` by two internally-disjoint length-two paths `2-4-3` and `2-5-3`. The resulting graph is simple, has six vertices and nine edges, and all of its edges have unit weight. Exact counts over all its forests are

- `Z = 300`,
- `Z_e = 111`,
- `Z_f = 114`,
- `Z_ef = 33`,
- `Delta = 2754`.

Here `D=(2^2-1)^2=9`, so every count is exactly `9` times its weighted-host counterpart and

`2754 = 9^2 * 34`.

The checker is `check_expansion_identity.py`; its committed output is `check_expansion_identity.out`. No floating-point arithmetic is used.

## 4. Why this changes the all-graphs proof obligation

The new point is not that the expansion construction exists; variants were already present in the team's theta-gadget work. The decisive point is its **scope** in the current proof chain.

### 4.1 Lead complete-graph route

The internal lead proves the unit inequality for every complete graph `K_n`. The expanded-family criterion does **not** upgrade that fact alone to weighted `K_n`, because the graphs

`K_n[Q^{E(K_n)-{e,f}}]`

are generally not complete graphs. Therefore the independently reproducible expansion proof cannot justify

`unit K_n => weighted K_n`.

To retain the lead's short complete-graph-to-all-graphs route, one genuinely needs the stronger fixed-host theorem attributed to Cocks, or an independent proof of it.

### 4.2 Partner's minimal-counterexample route

The same issue occurs more sharply in the consumed fleet04/B01 argument. Edge-minimality makes a smaller augmented bridge `H_i` unit-pNC. The partner then needs weighted pNC of that **same** `H_i` at an arbitrary virtual activity `lambda_i`.

The expansion criterion would instead require unit pNC for a family of graphs `H_i[Q^X]`. Those expansions can have arbitrarily many more edges than the original purported minimal counterexample. Hence edge-minimality supplies no such hypothesis. Replacing the fixed-graph theorem by the expansion theorem leaves a real gap.

Thus the exact remaining structural constraint is:

> either prove/verify the genuinely **fixed-graph** implication `unit pNC on G => I-Rayleigh for M(G)`, or prove unit pNC for the dense two-terminal expansion family needed to simulate every positive weighting.

The latter is a strictly larger family than the complete graphs and is not supplied by the current Hermite calculation.

## 5. Source reconciliation: what is proved and what is still source-dependent

There is a genuine wording tension in the available 2008 sources, so this run does not overclaim either direction.

1. The final published Semple--Welsh paper, Section 5 Note, explicitly says that Cocks showed: if Conjecture 1.1 holds for a graph `G`, then `M(G)` is independence correlated. Taken literally, this is the fixed-graph theorem needed by the lead and partner.

2. Cocks's published abstract says the Grimmett--Winkler conjecture is equivalent to statements about correlated graphic matroids, but the accessible abstract does not expose the theorem/proof body or enough quantifiers to distinguish fixed-host from class-global equivalence.

3. Erickson's 2008 thesis gives an explicit proof, says it was published independently by Cocks, and states only the class-global conclusion: **graphs are all I-negatively correlated iff they are all I-Rayleigh**. Its Proposition 5.2.2 requires unit pNC of the expanded graphs `M[Q^{E-{e,f}}]`. This proof therefore does not establish fixed-host closure.

Accordingly, this run does **not** mark the lead candidate false: the final Semple--Welsh Note is positive evidence for the stronger Cocks theorem. But neither the team's theta construction nor the independently inspectable Erickson/Cocks-style network construction can substitute for the missing primary theorem body. The lead remains source-conditional on that exact fixed-host result.

## 6. Computation beyond the exact certificate

As an adversarial check, a bounded exact search sampled 250 labelled simple graphs on eight vertices with 10--14 edges, 15 independent positive integer weightings per graph, and all marked edge pairs. No negative weighted Rayleigh value was found. This is only a stress test and is **not** evidence that the fixed-host theorem follows from unit pNC; no finite random search can establish the universal implication. The exact K4 expansion certificate above is the only computation counted as a mathematical identity in this report.

A floating-point exploratory search initially produced a tiny negative value on a bridge-separated pair; high-precision recomputation showed the true difference was zero, so it was rejected and is not reported as a counterexample.

## 7. Compact end-to-end state after this run

The team's current proof architecture can be separated cleanly:

1. **Complete graphs:** the Hermite argument is an internal full all-`n` candidate and is not challenged here.
2. **Complete graph weighted upgrade:** still depends on the exact fixed-graph Cocks theorem as stated by the Semple--Welsh Note; the explicit network proof available here gives only the expanded-family/global-class theorem.
3. **Minor/deletion transfer:** weighted independence correlation is minor-closed once Step 2 is genuinely available.
4. **Arbitrary simple graphs:** then follow as deletion minors of complete graphs.

So the first essential unpaid item for a source-self-contained proof is Step 2. A mathematically equivalent alternative is to prove unit pNC on the dense gadget-expansion family described above.

## 8. Status and handoff

**Outcome: `ESSENTIAL_STEP_APPLIED`.**

New reusable result: `FOREST-EXPANSION-SCOPE-v4`.

What is new and durable:

- exact all-parameter simple expansion identity and density statement;
- exact K4 `q=2/3` forest-count certificate;
- proof that the independently inspectable network mechanism is class-global/expanded-family, not by itself fixed-host;
- precise explanation of why the partner's edge-minimality argument cannot replace fixed-host Cocks by the expansion mechanism;
- exact next target for the lead: obtain the Cocks primary fixed-host theorem/proof or independently prove the fixed-host implication; failing that, attack unit pNC on the `K_n[Q^X]` expansion family.

No source-valid counterexample to the original FOREST conjecture was found. The original target remains externally open, and this report makes no novelty, priority or public solved-problem claim.

## 9. Sources

- Grimmett and Winkler, *Negative association in uniform forests and connected graphs*, Random Structures & Algorithms 24 (2004), arXiv:math/0302185.
- Charles Semple and Dominic Welsh, *Negative Correlation in Graphs and Matroids*, Combinatorics, Probability and Computing 17 (2008), 423--435, DOI 10.1017/S0963548307008978; final author PDF `https://www.math.canterbury.ac.nz/~c.semple/papers/SW07.pdf`, especially Proposition 3.5 and the Section 5 Note.
- Clifford C. Cocks, *Correlated Matroids*, Combinatorics, Probability and Computing 17(4) (2008), 511--518, DOI 10.1017/S0963548308009152.
- Alejandro Erickson, *Negative Correlation Properties for Matroids*, M.Math. thesis, University of Waterloo (2008), Chapter 5, Proposition 5.2.2 and Corollary 5.2.3.
