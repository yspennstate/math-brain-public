Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED**. GPT-6 maximum was requested, but this run has no authenticated GPT-6/maximum telemetry and the scheduler exposes no writable model/effort selector, so this report does not claim otherwise. **Source status OPEN -> OPEN; complete-all-graphs order metric 9 -> 9; structural-family metric advances from complete tripartite graphs whose two smallest part sizes sum to at most five to those whose two smallest part sizes sum to at most six.**

# PROB10-07 — complete tripartite fixed-width-six transfer theorem

Repository/branch: private `yspennstate/math-open-problems` / `master`  
Parent: Grimmett–Winkler pairwise edge negative correlation for the uniform measure on **all forests**  
Status: **PARTIAL / universal conjecture OPEN**  
Artifact stem: `20260920T0540Z_tripartite-sum6-d2a7`

## 1. Continuity, exact ownership boundary, and consumed evidence

This run followed `operations/PROB10_2026-09-20.md`, current `POSTED.md`, and the complete newest parent-owner handoffs before fixing scope:

- P14 mandatory forest handoff: `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T05-19-47Z__mandatory-handoff-report.md`, blob `bed2241d948b8a20b854efc248ccf5b46b4325cd`;
- HARD10-01 forest handoff: `proofnet24/HARD10-01/runs/2026-09-16/2026-09-16T21-16-42Z__report.md`, blob `d95d0b06d9eedb6f9edd8557d7e292267074d492`;
- newest own predecessor: `runs/prob10_2026-09-20/PROB10-07/20260920T0436Z_tripartite-sum5-5c91.md`;
- newest same-parent neighboring structural result visible before this run: `proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T05-21-16Z__triangle-right-linear-forest-sign-theorem.md`.

P14/HARD10-01 retain the complete-order-nine census, minimal-counterexample, separator, and three-terminal obstruction history. NM13-04/NM13-08 own their triangle-join/right-layer response families. This run does **not** repeat graph-order enumeration and does not seize those claims. It continues the separate PROB10-07 complete-tripartite fixed-core transfer line.

The superseded Komlós assignment remains preserved at `runs/R13/20260919T2345Z_handoff-to-PROB10-07-forest.md` and is not reopened.

The mathematical idea was recorded before the production checker in

`artifacts/prob10_2026-09-20/PROB10-07/20260920T0540Z_tripartite-sum6-d2a7_idea.md`

at commit `2c8fe39d6dde26ed68b5084afcbc984ca7e2e901`.

A non-mutating parent handoff is saved at

`artifacts/prob10_2026-09-20/PROB10-07/20260920T0540Z_tripartite-sum6-d2a7_forest-owner-handoff.md`

at commit `25eaa13ea06205eb34abfcbb3a42f9154c7ce623`.

No shared root ledger, peer report, scheduler, cadence, enabled state, workflow, permission, email, Drive, or public-posting state was changed.

## 2. Source statement and before/after metrics

For a finite simple graph `G=(V,E)`, let `F(G)` be the set of all acyclic edge subsets, isolated vertices allowed and all component counts mixed. Put

\[
Z=|F(G)|,
\qquad
Z_e=|\{F\in F(G):e\in F\}|,
\qquad
Z_{ef}=|\{F\in F(G):e,f\in F\}|.
\]

For the uniform all-forests law,

\[
\Pr(e)\Pr(f)-\Pr(e,f)
=\frac{Z_eZ_f-ZZ_{ef}}{Z^2}.
\]

Thus the exact source inequality is

\[
\boxed{\Delta_G(e,f):=Z_eZ_f-ZZ_{ef}\ge0.}
\tag{2.1}
\]

This is **not** a uniform spanning-tree law, random minimum spanning tree, connected random-cluster endpoint, or fixed-component forest ensemble.

Parent metrics:

- arbitrary-graph source status: `OPEN -> OPEN`;
- largest completely certified all-simple-graph order in repository continuity: `9 -> 9`;
- exact counterexample: `none -> none`;
- structural complete-tripartite parameter range: `two smallest parts sum <=5 -> <=6`.

The finite-order metric is deliberately separate. A new infinite graph class does not prove the universal statement.

## 3. Current source/prior-art screen

Primary and known baselines were rechecked during the run:

1. Grimmett–Winkler, `https://arxiv.org/abs/math/0302185`, is the arbitrary finite-graph uniform-**all-forests** source; its published computation covers all graphs through eight vertices and the nine-vertex sector through eighteen edges.
2. Erickson, `https://arxiv.org/abs/1008.3660`, proves a stronger all-positive-weight Rayleigh statement for the known series-parallel class. That result is a baseline, not this run's theorem.
3. Tang–Zhang, `https://arxiv.org/abs/2603.10738`, treats specified uniform spanning-subgraph families of `K_n`, including fixed-component forests for fixed `k` and sufficiently large `n`; this is not the arbitrary-graph all-component measure here.
4. Tang–Zhang, `https://arxiv.org/abs/2609.11578` (10 September 2026), states that pairwise negative correlation below one remains open on general finite graphs and proves a high-degree regular random-cluster regime. Its `Q=0` endpoint is connected percolation, not the uniform-all-forest law.
5. Bado, DOI `10.1016/j.spl.2026.110960`, now online, proves strict p-NC for wheel graphs using a `2 x 2` transfer matrix. Wheels are a distinct 3-connected non-series-parallel family.

A bounded search for the exact complete-tripartite uniform-forest Rayleigh theorem did not surface it. Searches included phrases around `complete tripartite`, `uniform forests`, `negative correlation`, and `Rayleigh`. The search instead surfaced unrelated complete-tripartite spanning-tree literature. This is negative evidence only. **Novelty/priority of the theorem below remains UNVERIFIED.**

## 4. Three materially different attacks compared before production coding

### Route A — deletion/contraction to a complete-multipartite closed formula

For distinct tested edges `e,f`, graphic-matroid contraction gives the tempting identities `Z_e=Z(G/e)` and `Z_{ef}=Z(G/{e,f})`. Because a complete tripartite graph has only finitely many edge-pair orbits, one could hope to reduce every Rayleigh difference to explicit forest counts of contracted complete multipartite graphs.

The route stops at a real algebraic gap: contraction creates identified vertices and parallel edge classes, while the current source chain contains no derived closed formula for the **unrooted all-forest** partition function of all such contracted multigraphs. The matrix-forest determinant counts rooted forests and cannot be substituted silently for `Z`. This route was not promoted.

### Route B — quotient the Bell transfer by `S_a x S_b`

The repeated third-part vertices only see the connectivity partition of the fixed terminals. Since the fixed core is `K_{a,b}`, one can quotient terminal set partitions by permutations inside each fixed part, and additionally swap the parts when `a=b`. This is the natural scalable route beyond width six.

The unproved obligation is strong lumpability for **all marked-edge initial vectors**, not just the unmarked transfer. I did not assume it. At width six, the full Bell state space has only `B_6=203` states, so an exact non-quotiented proof is still practical.

### Route C — full exact Bell transfer at width six

This route succeeds. It is the theorem below.

## 5. New theorem

### Theorem `PROB10-07-TRIPARTITE-SUM6`

For every integer `n>=1`, every distinct edge pair is strictly negatively correlated under the uniform measure on all forests of each graph

\[
\boxed{K_{1,5,n},\qquad K_{2,4,n},\qquad K_{3,3,n}.}
\tag{5.1}
\]

Equivalently, for every such graph and every distinct present `e,f`,

\[
\boxed{\Delta_G(e,f)>0.}
\tag{5.2}
\]

Combining (5.1) with the preceding PROB10-07 width-five theorem, the preceding `K_{1,2,n}` theorem, and the known series-parallel baseline for the remaining `K_{1,1,n}` layer gives:

> **Corollary.** Every complete tripartite graph `K_{a,b,c}` whose two smallest part sizes sum to at most six has strict pairwise negative edge correlation for the uniform-all-forests measure.

The parent arbitrary-graph conjecture remains OPEN/PARTIAL.

## 6. Exact terminal-partition transfer

Fix `(a,b)` in `{(1,5),(2,4),(3,3)}` and put

\[
m=a+b=6.
\]

Call the first two parts the **fixed terminals** and process the `n` vertices of the third part one at a time. A partial forest induces a set partition `pi` of the six terminals, according to which terminals are connected in the partial forest.

When a new third-part vertex `r` is added, choose a spoke set `S` from `r` to the six terminals.

### Lemma 6.1 — exact acyclicity criterion

The extension is acyclic iff `S` meets each block of `pi` in at most one terminal. If legal, the blocks met by `S` merge into one block; if `|S|<=1`, the terminal partition is unchanged.

**Proof.** If two members of `S` already lie in the same block, the existing forest contains a path between them, and the two new spokes through `r` close a cycle. Conversely, if the chosen terminals lie in distinct components, the star centered at `r` joins distinct tree components. Adding edges from a new vertex to distinct components cannot create a cycle. The connectivity update is exactly the stated block merge. `QED`

Let `M_6` be the resulting transfer matrix indexed by the `B_6=203` set partitions.

The empty spoke set and each of the six singleton spoke sets preserve every partition. Hence every diagonal entry is exactly seven. Every other legal spoke set merges at least two existing blocks. Therefore

\[
M_6=7I+N_6,
\tag{6.1}
\]

where every nonzero transition of `N_6` strictly reduces the number of blocks. There are at most six blocks, so

\[
N_6^6=0.
\tag{6.2}
\]

The exact checker also verifies `N_6^5\ne0`; this is not needed for positivity but confirms the expected nilpotence depth.

For every integer `x>=0`, the binomial theorem truncates exactly:

\[
M_6^x
=7^x\sum_{j=0}^{5}\binom{x}{j}\left(\frac{N_6}{7}\right)^j.
\tag{6.3}
\]

## 7. Exhaustive marked-edge reduction

Fix a distinct edge pair `e,f`. Under permutations inside the two fixed parts, part swap when `a=b`, and permutations of repeated third-part vertices, the pair lies in one of finitely many orbits.

The pair touches at most two repeated vertices. Let `k in {0,1,2}` be the number of repeated vertices needed to expose the marked pair. Enumerate exactly all acyclic subsets of the fixed `K_{a,b}` core together with those `k` distinguished repeated stars. This produces four row vectors indexed by terminal partitions:

\[
v_0,\qquad v_e,\qquad v_f,\qquad v_{ef},
\]

according as no marked edge, only `e`, only `f`, or both are required.

If

\[
x=n-k\ge0
\]

unmarked repeated vertices remain, then, writing `1` for the all-ones column vector,

\[
Z=v_0M_6^x\mathbf1,
\quad
Z_e=v_eM_6^x\mathbf1,
\quad
Z_f=v_fM_6^x\mathbf1,
\quad
Z_{ef}=v_{ef}M_6^x\mathbf1.
\tag{7.1}
\]

By (6.3), for each `C in {0,e,f,ef}` there is an exact rational polynomial `P_C(x)` of degree at most five such that

\[
Z_C=7^xP_C(x).
\tag{7.2}
\]

Consequently

\[
\Delta_G(e,f)=7^{2x}R_{e,f}(x),
\tag{7.3}
\]

where

\[
R_{e,f}(x)=P_e(x)P_f(x)-P_0(x)P_{ef}(x)
\]

has degree at most ten.

The automorphism enumeration is exhaustive. The exact orbit counts are

\[
10\quad\text{for }K_{1,5,n},
\qquad
15\quad\text{for }K_{2,4,n},
\qquad
9\quad\text{for }K_{3,3,n},
\tag{7.4}
\]

for **34 total edge-pair orbits**.

## 8. Exact sign certificate

For each of the 34 orbits, the production checker constructs the four vectors from actual forest subsets, computes the polynomial (7.3) using exact `Fraction` arithmetic, clears denominators, divides by the common integer gcd, and writes the complete primitive coefficient list to the archived output.

For **every orbit**, every ordinary monomial coefficient of `R_{e,f}(x)` is nonnegative.

- If `k>=1`, the constant coefficient is strictly positive, so `R_{e,f}(x)>0` for every physical `x>=0`.
- If `k=0`, the physical domain is `x=n>=1`. Every such orbit has `R_{e,f}(1)>0`; the only zero constant term in the new width-six output is harmless because its linear coefficient is strictly positive.

Thus (7.3) proves strict positivity for every physical integer `n>=1`.

Representative certificates follow.

For the first fixed-core orbit of `K_{1,5,n}`,

\[
R(x)=\frac{1}{5764801}
\bigl(
39348960x+97679260x^2+106824832x^3+66698203x^4
+25624233x^5+6037524x^6+804816x^7+46656x^8
\bigr),
\tag{8.1}
\]

strictly positive for `x>=1`.

For one fixed-core orbit of `K_{2,4,n}`,

\[
R(x)=\frac{1}{1441200}
\bigl(
466948881+708260700x+444241884x^2+147704905x^3
+27596763x^4+2793339x^5+128952x^6+1296x^7
\bigr)>0.
\tag{8.2}
\]

For a fixed-core orbit of `K_{3,3,n}`,

\[
R(x)=\frac{1}{2882400}
\bigl(
2594160450+3315653404x+1753271545x^2+492374396x^3
+78012658x^4+6743862x^5+270000x^6+2592x^7
\bigr)>0.
\tag{8.3}
\]

The archived exact output contains all 34 primitive coefficient lists, so the finite sign core is explicit rather than hidden behind a floating-point search.

## 9. Falsification and independent direct regressions inside the checker

The production executable does more than test polynomial coefficients.

For each family it separately enumerates every forest of the actual graphs at `n=1` and `n=2`, then checks **every actual distinct edge pair** against the transfer counts and Rayleigh gap. The exact direct regressions are:

- `K_{1,5,1}`: 11 edges, 55 edge pairs, 891 forests;
- `K_{1,5,2}`: 17 edges, 136 edge pairs, 18,176 forests;
- `K_{2,4,1}`: 14 edges, 91 edge pairs, 3,648 forests;
- `K_{2,4,2}`: 20 edges, 190 edge pairs, 58,495 forests;
- `K_{3,3,1}`: 15 edges, 105 edge pairs, 5,701 forests;
- `K_{3,3,2}`: 21 edges, 210 edge pairs, 85,116 forests.

Every direct Rayleigh gap is strictly positive, every direct count agrees with the transfer polynomial, and the archived execution terminates

`PROB10_07_TRIPARTITE_SUM6_EXACT_PASS`.

This is a self-check, not an independent external audit.

## 10. Executed artifacts and readback

Production checker:

`artifacts/prob10_2026-09-20/PROB10-07/20260920T0540Z_tripartite-sum6-d2a7_checker.py`

- local executed SHA-256 before persistence: `d221508d1375a5c76ea7d52ea4b3bacfffef807b41ad69f302be43f957e6b3ee`;
- creation commit: `1354fdf03e3947af22b3d71cee02b804ab497db5`;
- exact-commit readback blob: `a6d2c39ae537add9616ed8d73401f467384c004b`.

Executed output:

`artifacts/prob10_2026-09-20/PROB10-07/20260920T0540Z_tripartite-sum6-d2a7.out`

- local SHA-256 before persistence: `7c34c06d5d307c1cb701648b2916dddeb356331186bba4a4f202d9a9fb81c71d`;
- creation commit: `47d456084a62341dbb85c8c4298f446d196bf5ce`;
- exact-commit readback blob: `b832123cf155b1fad2fdd9b0c87f4ce81fcb560e`.

Independent-audit count for the new theorem: **0/2**. No closure label is claimed.

## 11. What moved and what did not

### Source-level movement

None. The universal Grimmett–Winkler conjecture remains OPEN. Complete arbitrary-graph coverage remains through order nine only.

### Structural-family movement

The complete-tripartite theorem advances by a full fixed-width layer:

\[
\boxed{
\text{two smallest parts sum }\le5
\quad\Longrightarrow\quad
\text{two smallest parts sum }\le6.
}
\]

The new boundary cases are exactly

\[
K_{1,5,n},\quad K_{2,4,n},\quad K_{3,3,n}.
\]

This is an all-parameter result in `n`, not a finite list of tested graph sizes.

### Auxiliary mechanism gain

The full unquotiented Bell transfer remains practical at width six: `203` partition states and `34` marked pair orbits. The exact coefficient positivity persists one complete layer beyond the previous width-five computation.

## 12. Remaining full-scope gap and next obstruction

Nothing here controls an arbitrary 3-connected graph, so the P14/HARD10 three-terminal obstruction remains untouched in full generality.

Even within the complete-tripartite line, the next layer

\[
K_{1,6,n},\qquad K_{2,5,n},\qquad K_{3,4,n}
\]

has seven fixed terminals and `B_7=877` Bell states. More importantly, a naive initial marked-vector enumeration for the densest core `K_{3,4}` with two distinguished repeated vertices has `12+14=26` available edges, making raw `2^{26}` subset enumeration the wrong next algorithm.

Therefore the next substantive route should **not** merely increase the brute-force limit. It should prove and use one of:

1. a strong-lumpability theorem for the `S_a x S_b` orbit quotient, including every marked-edge initial condition; or
2. an edge-by-edge partition DP for the marked fixed core that constructs `v_0,v_e,v_f,v_{ef}` without enumerating all subsets.

Either mechanism would turn width seven into another exact symbolic theorem and, more importantly, indicate whether the coefficient-positivity phenomenon is structural enough for an arbitrary fixed width.

## 13. Honest status and ledger delta

```yaml
ledger_delta:
  track: PROB10-07
  parent_source: "Grimmett-Winkler uniform-all-forests pairwise edge negative correlation"
  parent_status_before: OPEN
  parent_status_after: OPEN
  complete_all_graphs_order_before: 9
  complete_all_graphs_order_after: 9
  exact_counterexample: NONE
  structural_metric: "complete tripartite K_{a,b,c}: maximum certified sum of two smallest part sizes"
  structural_before: 5
  structural_after: 6
  new_families:
    - "K_{1,5,n}, all n>=1"
    - "K_{2,4,n}, all n>=1"
    - "K_{3,3,n}, all n>=1"
  exact_pair_orbits_certified: 34
  checker_status: PASS
  direct_regression: "all actual edge pairs at n=1,2 in all three families PASS"
  independent_audits: "0/2"
  novelty: UNVERIFIED
  status: PARTIAL
```

No scheduler, cadence, enabled state, email, Drive, public posting, workflow execution, or permission setting was changed.