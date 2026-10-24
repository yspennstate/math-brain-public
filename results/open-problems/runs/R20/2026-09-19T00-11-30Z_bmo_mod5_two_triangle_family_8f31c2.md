Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT: `n_all: 8 -> 8`; status `PARTIAL / CLAIMED / READY / CLOSABLE OUTSIDE / SELF_CHECK_ONLY`; methods #3 PROVE SOMETHING STRONGER, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #22 READ THE FAILURES NOT THE SUCCESSES.**

# R20 — a mod-5 construction for the first unresolved three-cycle cactus family

## 0. Continuity, ownership, source status, and metric

This run does **not** reopen the stale scheduler-title target Bandeira / Randomstrasse 2025 Conjecture 26 / intake I0100. Repository continuity is decisive: R20 already rotated away from I0100 after its historical localized-Paley exact-certificate program, whose frozen frontier remains `p_max=1213`; finite prime certificates never proved the source asymptotic. R20 later rotated away from the KNSV target as well.

The current exclusive R20 claim is

`operations/claims/BMO-2025-PUSHING-DELTA.md`,

owned by R20 and marked `CLAIMED / READY / CLOSABLE OUTSIDE`. Its source is Julien Bensmail, Clara Marcille and Mano Orenga, *Pushing Vertices to Make Graphs Irregular*, DMTCS 27:3 (2025), article 7, DOI `10.46298/dmtcs.14963`, Conjecture 2.6. For every nice finite simple graph `G` the source conjectures

\[
P^\ell(G)\le \Delta(G),
\]

where a pushing scheme `rho:V(G)->N_0` gives

\[
\sigma_\rho(u)=(1+\rho(u))d_G(u)+\sum_{v\sim u}\rho(v),
\]

and is proper when adjacent vertices receive unequal integer sums.

Fresh source/literature check on 19 September 2026: the DMTCS source page remains the current 2025 article; the June 17, 2026 paper of Rautenbach--Schwartze--Werner, *Coloring by Pushing Vertices*, still describes the general `Delta` bound as conjectural and proves it for cubic graphs and regular bipartite graphs. Bounded fresh searches for the exact title/DOI, Conjecture 2.6, cactus pushing schemes and later-author work found these sources but no later source-matching general proof or published readable proof of the optimal cactus bound. This is bounded negative evidence, not a novelty certificate.

The fixed metric remains

\[
n_{\rm all}=\max\{n:\text{every nice simple graph of order at most }n\text{ has an exact witness with }\max\rho\le\Delta\},
\]

with supported value `n_all=8`. The theorem below is infinite-family structural progress, so it does **not** move this metric.

The preceding stuck review singled out as the simplest still-unproved structural family a central cycle `C_m`, `m>=4`, with one leaf triangle attached at each of two distinct central vertices. It also diagnosed the failure of the previous mod-3 state algebra: equal residues can still correspond to unequal integer sums separated by `3,6,...`. This run attacks exactly that family by changing the modulus rather than enlarging the mod-3 state.

The new idea was written **before** the checker in

`artifacts/R20/2026-09-18T23-50-00Z_bmo_mod5_two_triangles_idea_before_code.md`

at commit `a9ee91f81c42cfb03a79f39ceb960003fad34db2`.

## 1. The category change hidden inside #3/#17: modulus five

Let

\[
Q=D+A
\]

be the signless Laplacian of `G`. Then

\[
\sigma_\rho=d+Q\rho.
\]

Suppose we seek only pushes `rho(v) in {0,1,2}` and define

\[
y(v)=2-\rho(v)\in\{0,1,2\}.
\]

Since `Q 1=2d`, we obtain the exact identity

\[
\sigma_\rho
 =d+Q(2\mathbf 1-y)
 =d+4d-Qy
 =5d-Qy.
\]

Hence

\[
\boxed{\sigma_\rho\equiv -Qy\pmod5.}
\]

Therefore it is enough to construct `y:V(G)->{0,1,2}` for which `Qy` is a proper vertex coloring modulo `5`. Distinct residues imply distinct integer sums, and then `rho=2-y` is a proper pushing scheme with maximum push at most `2`.

This reformulation is closely shaped like the neighbour-sum-distinguishing edge-weighting / 1-2-3 problem: on an edge `uv`, the contribution to the two endpoint `Qy` sums is

\[
w_{uv}=y(u)+y(v)\pmod5.
\]

The crucial restriction is that these edge weights are not independent; they must be endpoint sums. The source itself makes the connection to the 1-2-3 line. The modern 1-2-3 theorem therefore does not settle the pushing problem, but it suggests looking for a small-modulus sum-coloring language. Modulus `5` fits the three allowed vertex labels `{0,1,2}` much better than the previous modulus `3`: the two residues `3,4` become genuine slack states lying outside the label set.

## 2. Flexible-triangle lemma

Consider a leaf triangle whose articulation/root is `r`. Let

\[
a=y(r)\in\{0,1,2\},
\]

and let `e` denote the contribution to `(Qy)(r)` from edges outside the triangle. Give the two private triangle vertices labels

\[
b,c\in\{0,1,2\}.
\]

The three `Qy` colors are, modulo `5`,

\[
\begin{aligned}
C_r&=e+2a+b+c,\\
C_b&=2b+a+c,\\
C_c&=2c+a+b.
\end{aligned}
\]

Subtracting gives

\[
C_b-C_c=b-c,
\]

and

\[
C_r-C_b=e+a-b,
\qquad
C_r-C_c=e+a-c.
\]

Thus the triangle is proper modulo `5` exactly when

\[
b\ne c,\qquad b\ne e+a,\qquad c\ne e+a\pmod5.
\]

In particular, if

\[
\boxed{e+a\in\{3,4\},}
\]

then the last two restrictions disappear because `b,c` lie in `{0,1,2}`. Every distinct pair works. The three unordered distinct-pair sums are

\[
0+1=1,\qquad0+2=2,\qquad1+2=3.
\]

Consequently the attainable final root colors

\[
C_r=e+2a+(b+c)
\]

form a three-element subset of `F_5`.

### Lemma 2.1 (flexible leaf triangle)

If the central part of the graph is already labeled and, at a triangle root `r`, its central contribution `e` satisfies `e+y(r) in {3,4}` modulo `5`, then the leaf triangle can be completed in three different ways producing three distinct possible final colors at `r`, while all three triangle edges remain proper modulo `5`.

This three-value list is the main piece of slack used below.

## 3. A period-four library for a central path with zero-labeled ends

Let an arc have vertices `v_0,...,v_d`, with both endpoint labels zero. For an internal degree-two central-cycle vertex the `Qy` color is

\[
\kappa_i=2y_i+y_{i-1}+y_{i+1}\pmod5.
\]

We now define an explicit word `W_d` of length `d+1` over `{0,1,2}` with zero endpoints.

For the four short lengths,

\[
\begin{array}{c|c}
d&W_d\\ \hline
2&(0,2,0)\\
3&(0,1,2,0)\\
4&(0,2,1,2,0)\\
5&(0,2,0,1,2,0).
\end{array}
\]

For `d>=6`, write

\[
d=6+4q+r,\qquad r\in\{0,1,2,3\},
\]

and define

\[
W_d=(0,2,0,0,0)\,(1,0,0,0)^q\,T_r\,(0),
\]

where

\[
T_0=(2),\quad
T_1=(1,2),\quad
T_2=(1,0,2),\quad
T_3=(1,0,0,2).
\]

The labels immediately next to the two zero endpoints are `(2,2)` for every `d` except `d=3`, where they are `(1,2)` in the displayed orientation.

For `d=2,3,4,5`, the internal color words `kappa_1,...,kappa_{d-1}` are respectively

\[
(4),\quad(4,0),\quad(0,1,0),\quad(4,3,4,0),
\]

so consecutive colors are distinct.

For `d>=6`, direct substitution into the period-four interior gives

\[
(\kappa_1,\ldots,\kappa_{d-1})
=(4,2,0)\,(1,2,1,0)^q\,V_r,
\]

with

\[
\begin{aligned}
V_0&=(2,4),\\
V_1&=(1,4,0),\\
V_2&=(1,2,3,4),\\
V_3&=(1,2,1,2,4).
\end{aligned}
\]

Every adjacent pair in each displayed word is unequal, including the concatenation boundaries. Also, the endpoint label `0` is distinct from the first/last internal colors where those endpoint colors are already fixed later by the triangle choices. What matters before attaching the triangles is that **every internal edge of the arc is already proper modulo five**.

### Lemma 3.1 (zero-end path library)

For every `d>=2`, `W_d` labels a path with zero-labeled endpoints so that every edge whose endpoints are internal to the path is proper under the `Qy` colors. The labels adjacent to an endpoint are both `2`, except that a length-three arc has endpoint-adjacent pair `(1,2)` up to reversal.

The proof is the explicit calculation above; no recurrence or computer search is needed.

## 4. Nonadjacent triangle roots

Let the two triangle roots on the central cycle be `r_0,r_1`, and first suppose they are nonadjacent. The two arcs between them have lengths

\[
d_1,d_2\ge2,\qquad d_1+d_2=m.
\]

Set

\[
y(r_0)=y(r_1)=0.
\]

Label each arc by the corresponding word `W_{d_j}`, reversing one if convenient. By Lemma 3.1 all central-cycle edges not incident with a root are already proper modulo `5`.

At a root, its central contribution `e` is simply the sum of the two neighboring central labels. If neither arc has length `3`, both incident labels supplied by each arc are `2`, hence

\[
e=2+2=4.
\]

If exactly one arc has length `3`, one of the two incident labels is `1` at one end of that arc while the other is `2`; hence the two roots see contributions in `{3,4}`. If both arcs have length `3` (the opposite roots of `C_6`), orient the two copies so that each root sees `1+2=3`. Therefore at each root

\[
e+y(r_i)=e\in\{3,4\}.
\]

Lemma 2.1 now applies to both leaf triangles. At each root the triangle gives **three possible final root colors**. The two roots are nonadjacent, so each root merely has to avoid the colors of its two already fixed central neighbors. A three-element list cannot be contained in a forbidden set of size at most two. Choose any surviving color independently at each root and then choose the corresponding distinct pair `(b,c)` in the leaf triangle.

This makes every central-cycle edge incident with a root proper, as well as every leaf-triangle edge. Hence the entire graph is proper modulo `5`.

## 5. Adjacent triangle roots

It remains to handle the case where the two triangle roots are adjacent. Name them `v_0,v_1` around `C_m`. We deliberately break the root-label symmetry and set

\[
y_0=0,\qquad y_1=1.
\]

For the two smallest cycles use

\[
C_4:\quad (0,1,0,2),
\]

and

\[
C_5:\quad (0,1,0,0,2).
\]

For `m>=6`, write `m=6+4q+r`, `r in {0,1,2,3}`, and use the cyclic label word

\[
Y_m=(0,1,0,0,0)(1,0,0,0)^qT_r,
\]

with the same tails `T_r` as above.

For `m=4`, the two nonroot central colors are `(3,4)`; for `m=5` they are `(1,2,4)`. For `m>=6`, the nonroot central colors, in order from `v_2` through `v_{m-1}`, are

\[
(1,0)(1,2,1,0)^qV_r,
\]

with the same `V_r` as in Section 3. Again consecutive entries are unequal, so every central edge whose endpoints are both nonroots is already proper.

Now inspect the two roots before attaching their triangles. At `v_0`, the root label is `0`, and its two central neighbors have labels `1` and `2`, so

\[
e_0+y_0=3.
\]

At `v_1`, the root label is `1`, while both central neighbors have label `0`. The central contribution to `(Qy)(v_1)` is

\[
e_1=2y_1+y_0+y_2=2,
\]

in the notation of Lemma 2.1 where `e_1` includes the already fixed central part but not the leaf triangle. Hence

\[
e_1+y_1=3.
\]

Both leaf triangles are therefore flexible. Each root has a three-element list of possible final colors.

For `v_0`, one central neighbor is the other root `v_1`; the other central neighbor has an already fixed color. Delete from the three-element list only the latter fixed color. At least two choices remain. Do the same for `v_1`. Thus both roots retain lists of size at least two. From two subsets of a five-element set, each of size at least two, one can choose `c_0` from the first and `c_1` from the second with `c_0 != c_1`; otherwise both sets would have to be the same singleton. Choose such a pair. Then the edge `v_0v_1` is proper, and each root also differs from its other central neighbor. Finally realize each selected root color by the corresponding distinct private-triangle labels from Lemma 2.1.

Hence the whole graph is proper modulo `5` also in the adjacent-root case.

## 6. The structural theorem

Combining Sections 4 and 5 gives the following.

### Theorem 6.1 — SELF_CHECK_ONLY

Let `G` be obtained from a cycle `C_m`, `m>=4`, by attaching a leaf triangle at each of two distinct vertices of `C_m` (the two triangles otherwise vertex-disjoint). Then there exists

\[
y:V(G)\to\{0,1,2\}
\]

such that `Qy` is a proper vertex coloring modulo `5`. Consequently

\[
\rho=2-y:V(G)\to\{0,1,2\}
\]

is a proper pushing scheme, and therefore

\[
\boxed{P^\ell(G)\le2.}
\]

#### Proof

Use the nonadjacent-root construction of Section 4 or the adjacent-root construction of Section 5. In either case every edge has distinct endpoint `Qy` colors modulo `5`. Set `rho=2-y`. The exact identity

\[
\sigma_\rho=5d-Qy
\]

implies

\[
\sigma_\rho(u)-\sigma_\rho(v)
\equiv -(Qy(u)-Qy(v))\not\equiv0\pmod5
\]

on every edge `uv`. Thus the integer sums are unequal on every edge. Since every `rho(v)` lies in `{0,1,2}`, the claimed bound follows. QED.

This theorem exactly closes the simplest structural family isolated by the preceding stuck review. It does **not** prove the full cactus statement and does not prove or refute Conjecture 2.6. It is labeled `SELF_CHECK_ONLY` until independently audited.

## 7. Exact validation, written only after the route existed

After the proof route was written, I implemented the exact construction in

`artifacts/R20/bmo_mod5_two_triangles_exact.py`

creation commit `f4b1ee8a7f90484e1182ba34930728cd116e0486`.

The checker contains the explicit period-four formulas above, constructs both adjacent and nonadjacent cases, chooses the triangle completion from the exact three-value lists, converts `y` to `rho=2-y`, and verifies both modular and integer edge inequalities.

The executed output is archived in

`artifacts/R20/bmo_mod5_two_triangles_exact.out`

at commit `b4a3183c2dee548782dfaa75a4644f541484762f`. It records:

```text
R20 BMO mod-5 exact construction check
word_lengths_checked_through=500
central_cycle_lengths_checked=4..300
ordered_attachment_distances_checked=44847
all_constructed_pushes_in={0,1,2}
all_edges_distinct_mod_5=True
all_edges_distinct_over_Z=True
VERDICT=PASS
```

The computation is a validation of the explicit formulas, not the reason the theorem holds. The proof on the page covers all `m>=4`.

## 8. Outcomes of the three Section-B moves

### #3 PROVE SOMETHING STRONGER

The useful stronger statement was not the previously failed demand of properness modulo `3`. The correct strengthening is:

> construct a two-push witness whose endpoint sums are already different modulo `5` on **every** edge.

That stronger modular conclusion is exactly what Theorem 6.1 proves for the first unresolved three-cycle family, and the identity `sigma=5d-Qy` makes it feed directly into the integer pushing problem.

### #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE

The source is explicitly connected to the 1-2-3 neighbour-sum-distinguishing edge-weighting problem. That literature suggests replacing direct manipulation of `sigma` by incident-sum colors. The modern 1-2-3 theorem cannot be imported literally because pushing imposes the endpoint-sum restriction on edge weights, but the analogy exposed the right object:

\[
w_{uv}=y(u)+y(v)\pmod5.
\]

The new modulus `5` is not borrowed as a published pushing theorem; it is the natural modulus produced by the exact substitution `rho=2-y`, because `1+rho(u)+rho(v)=5-y(u)-y(v)` on every edge.

### #22 READ THE FAILURES, NOT THE SUCCESSES

The source authors say their cactus modulo approach became too dependent on exhaustive computer checks to yield the readable proof they wanted. The previous R20 mod-3 state algebra reproduced precisely that failure mode: it became a finite transition system and then lost essential integer-height information at four triangles. The lesson was to **change the modulus before enlarging the state**. Modulo `5`, the unused residues `3,4` provide slack, and the central-cycle part collapses to a closed period-four word. For this family the resulting proof is formulaic rather than a state census.

## 9. What this suggests next

The strongest next route is no longer the exact-height interface from the preceding stuck report. The mod-5 construction suggests a potentially much cleaner full-cactus induction.

Computational exploration in this run suggests that rooted cactus pieces have far richer mod-5 boundary lists than their mod-3 analogues, and that bridges quickly create flexibility. I do **not** promote those observations to a theorem here. The next mathematical target should instead be a written rooted extension lemma of the following shape:

> for a rooted cactus block tree, prescribe the root label `y(r) in {0,1,2}` and an outside contribution modulo `5`; unless the rooted piece is the trivial `K_2` obstruction excluded by niceness, the piece admits enough root-color choices to glue upward.

If that lemma can be proved by block induction, it would give the source authors' requested readable cactus theorem `P^l<=2` in one stroke. A second, algebraically different route is the polynomial

\[
F_G(\rho)=\prod_{uv\in E(G)}(\sigma_\rho(u)-\sigma_\rho(v)),
\]

and a Combinatorial-Nullstellensatz / permanent certificate with exponents at most two for cactus block trees. This connects directly to weight-choosability methods from the 1-2-3 literature and is worth pursuing only if the rooted mod-5 induction stalls.

The next nonrepeating Section-B moves are **#11 DUALIZE, #18 SAY IT IN ANOTHER LANGUAGE, #25 COUNT THE SAME THING TWICE**. Concretely: derive the rooted mod-5 interface as a dual list-avoidance condition, translate it into constrained edge-sum weighting / polynomial language, and search for a cancellation-free orientation count that proves the required coefficient nonzero.

Because the fixed metric `n_all` has now remained at `8` for **five consecutive BMO runs after admission**, the next run is the last permitted unchanged closable run before the six-unchanged rotation rule triggers. It should therefore aim at either (i) a theorem broad enough to move the fixed all-graphs metric, (ii) the full cactus theorem plus a justified metric consequence if one exists, or (iii) a source-level proof/counterexample. If the frozen metric is unchanged again, preserve the handoff and rotate rather than manufacturing a seventh unchanged report.

## 10. Model/scheduler-control status

The operative scheduler implementation record still exposes prompt/title/schedule/timing/enabled controls but no binding model-family selector, no reasoning-effort selector, no authenticated completed-run model receipt, and no guaranteed hour-long execution control. Therefore the prompt's request for GPT-6/maximum cannot be represented as an enforced runtime setting from this worker surface; this report truthfully states GPT-5.6 Sol and reasoning `UNVERIFIED`.

The same implementation record preserves the historical P26 response `You cannot modify this task`. That is an authorization boundary. The legitimate workaround is an owner/admin-authorized product/backend context that exposes the task; enforcing a model/reasoning choice would additionally require that surface to expose those controls. No scheduler modification, permission bypass, email, Drive action or public posting was attempted.

## 11. Structured ledger delta

```yaml
ledger_delta:
  track: R20
  active_source: "Julien Bensmail, Clara Marcille, Mano Orenga, Pushing Vertices to Make Graphs Irregular, DMTCS 27:3 (2025), Conjecture 2.6"
  canonical_claim: "operations/claims/BMO-2025-PUSHING-DELTA.md"
  source_scope: "every nice finite simple graph; P^l(G) <= Delta(G)"
  predecessor_I0100: "retired/rotated historical R20 target; exact-prime frontier p_max=1213 preserved; not reopened"
  fixed_metric: "n_all = largest n such that every nice simple graph of order <= n has an exact witness with max rho <= Delta"
  metric_before: 8
  metric_after: 8
  movement: false
  unchanged_count_after: 5
  status: "PARTIAL / CLAIMED / READY / CLOSABLE OUTSIDE / SELF_CHECK_ONLY"
  tried_moves: [3, 17, 22]
  move_outcomes:
    3: "proved the stronger all-edges-proper-mod-5 statement for the central-cycle plus two leaf-triangles family"
    17: "ported neighbour-sum edge-weighting language; endpoint-sum restriction yields w_uv=y_u+y_v mod 5"
    22: "used the source's failed computer-heavy cactus-modulus route and R20's own mod-3 obstruction to change modulus rather than enlarge the state table"
  new_theorem: "If G is C_m (m>=4) with two leaf triangles attached at distinct central vertices, then P^l(G)<=2; explicit construction makes all edge sums distinct mod 5"
  theorem_scope: "SELF_CHECK_ONLY; structural family only; not the full cactus theorem or source conjecture"
  evidence:
    idea_before_code:
      path: "artifacts/R20/2026-09-18T23-50-00Z_bmo_mod5_two_triangles_idea_before_code.md"
      commit: "a9ee91f81c42cfb03a79f39ceb960003fad34db2"
    checker:
      path: "artifacts/R20/bmo_mod5_two_triangles_exact.py"
      commit: "f4b1ee8a7f90484e1182ba34930728cd116e0486"
    checker_output:
      path: "artifacts/R20/bmo_mod5_two_triangles_exact.out"
      commit: "b4a3183c2dee548782dfaa75a4644f541484762f"
      verdict: "PASS"
      cycle_lengths: "4..300"
      ordered_attachment_distances: 44847
  audits: []
  remaining_obligation: "prove or refute BMO Conjecture 2.6; immediate structural opportunity is a readable rooted mod-5 induction for all nice cacti"
  next_moves: [11, 18, 25]
  rotation_if_next_metric_unchanged: true
```

No closure, refutation, independent audit, or publication claim is made.