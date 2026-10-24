Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: `N_sep > 11 -> N_sep > 11`; methods #11 DUALIZE, #19 MAKE IT AN ALGORITHM, #24 FIND THE EXTREMAL OBJECT.**

# R20 — KNSV Conjecture 8.2: an exact dual obstruction to local-linear recovery and a refined join no-go

## 0. Continuity, ownership, and source status

R20 does **not** reopen the retired Paley one-localization predecessor I0100 in this run.  Its frozen historical metric remains `p_max=1213` after retirement.  The current exclusive R20 target is the create-only claim

`operations/claims/KNSV-2026-LOOPY-U.md`,

owned by R20 and marked `CLAIMED / READY / CLOSABLE OUTSIDE`.

Current source:

- Anatol Kirillov, Gleb Nenashev, Boris Shapiro, Arkady Vaintrob,
  *The Loopy Polynomial: from Tutte's Universal V-Function to Bizonotopal Geometry*, arXiv:2609.07728v1, Conjecture 8.2.
- Source target: for **simple** graphs, ordinary loopy `L`, ordinary `U`, the polychromate, and the Tutte symmetric function have the same distinguishing power.
- Fixed R20 metric:
  `N_sep = minimum vertex count of a rigorously certified simple U/L separator in either direction`.
- Source baseline: Proposition 8.6 verifies the equivalence through 11 vertices, so `N_sep>11`.

A fresh 18 September 2026 source/current-literature check used the exact arXiv id `2609.07728`, exact title, `Conjecture 8.2`, the authors' current paper list, and searches for later proof/counterexample/simple-graph resolution.  The accessible current record remains arXiv v1, submitted 7 September 2026, and the authors' page still lists the paper as submitted.  I found no later source-matching proof or simple-graph counterexample.  This is bounded negative search evidence, not a claim that an inaccessible paper cannot exist.

The author-hosted current PDF was checked directly.  It states Conjecture 8.2 on page 39, verifies all simple graphs through eleven vertices in Proposition 8.6, gives the block-transform formulation in Section 9.2, and records the authors' exhaustive code/data DOI `10.5281/zenodo.21929427` in Appendix A.  Direct Zenodo access is unavailable through the web surface exposed in this run, so I did not claim to inspect those files.

Repository continuity checked in this run includes `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, the operative implementation record, the KNSV ownership file, the newest R20 report, and existing R20 KNSV artifacts.  The newest predecessor report is

`runs/R20/2026-09-18T14-13-09Z_knsv_graphical_block_rigidity_two_terminal_0c51e7.md`.

That report left the metric at `N_sep>11` and isolated the first nonautomatic block profile `(4,3)` with hidden vector `(h1,h2,h3)`.  I continue from that state rather than restarting.

## 1. Starting point: the first hidden `(4,3)` statistic

For a four-vertex set `B`, write

\[
\mathcal C_G(B;q)=q^3\sum_{j=0}^3 a_j(B)(1+q)^j,
\]

with all `a_j(B)=0` when `G[B]` is disconnected.  For a three-vertex set `C`, write

\[
\mathcal C_G(C;q)=q^2(\alpha_C+\beta_C(1+q)).
\]

For a simple graph, `beta_C=1` exactly when `G[C]=K_3`, and `beta_C=0` otherwise.  For the block profile `(4,3,1^{n-7})`, the previous report showed that after fixing the ordinary-U layer the transformed loopy layer can lose only the correlations

\[
h_r(G):=
\sum_{\substack{|B|=4,\ |C|=3\\B\cap C=\varnothing}}
      a_{r-1}(B)\,\beta_C,
\qquad r=1,2,3.
\]

A discrepancy in this vector inside an actual ordinary-U collision would therefore be an exact source-valid `U_G=U_H` but `L_G\ne L_H` witness.

The question for this run was whether ordinary U forces these numbers by a simple local identity, and whether known lower-order collision classes can be lifted by joins to create a first counterexample at 12 vertices.

## 2. Method #11 — DUALIZE: no universal linear local formula for `h1`

### 2.1 The proposed proof architecture

At seven vertices the profile is exactly `(4,3)`, with no outside singletons.  A natural proof route is to seek constants `c_{lambda,r}` such that for every seven-vertex simple graph

\[
h_1(G)=\sum_{\lambda,r}c_{\lambda,r}\,[z_\lambda y^r]U_G.
\tag{2.1}
\]

Such an identity would lift to arbitrary `n`: summing (2.1) over seven-subsets would express the global `(4,3,1^{n-7})` hidden statistic by ordinary-U block-profile coefficients with singleton blocks.  The same idea could then be attempted for `h2,h3`.

I attacked (2.1) on the dual side.  It is enough to find a signed linear combination of seven-vertex simple graph types whose total ordinary-U coefficient vector vanishes but whose total `h1` does not.

### 2.2 Exact sparse dual certificate

The following exact integer relation was found and then verified from scratch by the checker in Section 5.  Graphs are given by graph6 strings; integer coefficients mean formal multiplicities.

\[
\begin{aligned}
&U_{\texttt{F~\{OO}}
 +3U_{\texttt{FG?`G}}
 +2U_{\texttt{FC_`G}}
 +U_{\texttt{F`?GW}}
 +3U_{\texttt{F`G`G}}
 +U_{\texttt{FetA?}}
 +U_{\texttt{F`_pg}}\\
&\qquad=
3U_{\texttt{FOg?G}}
+3U_{\texttt{F@G`G}}
+3U_{\texttt{FK_`G}}
+2U_{\texttt{Fms?G}}
+U_{\texttt{F~|A?}}.
\tag{2.2}
\end{aligned}
\]

Both sides contain twelve graph copies counting multiplicity.  Ordinary U is checked coefficient-by-coefficient over `Z` in the basis

\[
(\text{component-size partition},\ \text{total cyclomatic number}).
\]

But the same two formal multisets have

\[
\sum_{\rm left} h_1=1,
\qquad
\sum_{\rm right} h_1=4.
\tag{2.3}
\]

Therefore (2.1) is impossible.

### 2.3 What this proves and what it does not

**Proved, exact finite statement.** `h1` is not a universal rational linear combination of the ordinary-U coefficient functions on seven-vertex simple graphs.  Consequently, the first hidden `(4,3)` statistic cannot be recovered by the most direct local-linear identity and then lifted by summing over seven-subsets.

**Not proved.** This is not a pair of graphs with equal U.  It is a relation between two weighted multisets of graph types.  There are no ordinary-U collisions below eight vertices in the source census.  Hence (2.2)--(2.3) is a dual obstruction to a proof architecture, **not** a refutation of Conjecture 8.2 and not movement of `N_sep`.

The same exploratory finite linear algebra also showed rank jumps for `h2` and `h3`, but I do not promote those modular calculations to theorem claims here because the exact archived certificate in this run is only (2.2)--(2.3).  One exact obstruction is already enough to kill universal linear recovery of the full hidden vector.

## 3. Method #19 — MAKE IT AN ALGORITHM: hidden-vector-first collision search

The block reduction gives a cheaper exact separator test than computing full `L`.

Suppose a candidate pair of simple graphs has already passed an **exact** ordinary-U equality test.  Then the ordinary `(4,3,1^{n-7})` layer is the same on both sides.  The transformed loopy layer depends injectively on `(h1,h2,h3)` once that ordinary layer is fixed.  Therefore

\[
(h_1,h_2,h_3)(G)\ne(h_1,h_2,h_3)(H)
\quad\Longrightarrow\quad
L_G(1,x)\ne L_H(1,x).
\tag{3.1}
\]

This suggests the next exact search order:

1. produce or inherit a guaranteed ordinary-U collision;
2. compute `(h1,h2,h3)` exactly;
3. only if the hidden vector agrees, pay for fuller transformed-block or `L(1,x)` computation.

This is especially useful at `n=12`, where source-scale exhaustive U computation is expensive but `(h1,h2,h3)` is only a finite sum over disjoint 4- and 3-subsets with small connected-subgraph polynomials.

The source Appendix A already provides the right outer architecture: its connected-block recursion computes all `C_G(B;q)` in `O(3^n)` ring operations and then obtains U/L-type fingerprints by partition dynamic programming.  The new observation is that the first nonautomatic loopy discrepancy can be tested **before** the full loopy fingerprint by the three exact integers above.

No new source-scale enumeration is claimed in this run because the authors' Zenodo files were not accessible through the present web surface.  The exact local certificate checker below is independent of those files.

## 4. Method #24 — FIND THE EXTREMAL OBJECT: all join-generated lifts of known collisions are a dead end

The obvious way to manufacture guaranteed ordinary-U collisions at the first open order is to take a known collision `G,H` on at most eleven vertices and join the same graph `J` to both sides.  Source Corollary 9.2 proves that ordinary-U / XB collision classes are preserved by joins.

For the actual source census, however, this entire strategy is stronger than necessary and cannot produce a loopy separator.

### Proposition 4.1 (refined collision closure under joins; SELF-CHECK ONLY)

If simple graphs `G,H` satisfy

\[
U_G^{\rm ext}=U_H^{\rm ext},
\]

then for every fixed simple graph `J`,

\[
U_{G\vee J}^{\rm ext}=U_{H\vee J}^{\rm ext}
\quad\text{and hence}\quad
L_{G\vee J}=L_{H\vee J}.
\tag{4.1}
\]

#### Proof

Use the extended polychromate, which the source identifies equivalently with the extended U-polynomial.  A block of a set partition records the pair

\[
(s,e_G(B)).
\]

Under complementation that pair becomes

\[
\left(s,{s\choose2}-e_G(B)\right),
\]

an invertible blockwise substitution.  Hence equality of the extended invariant is preserved by complement.

From the defining spanning-subgraph expansion, extended U is multiplicative under disjoint union: components of an edge subset never mix the two disjoint factors, and the component variables multiply.  Therefore

\[
U^{\rm ext}_{\bar G}=U^{\rm ext}_{\bar H}
\Longrightarrow
U^{\rm ext}_{\bar G\sqcup\bar J}
 =U^{\rm ext}_{\bar H\sqcup\bar J}.
\]

Complement once more and use

\[
\overline{G\vee J}=\bar G\sqcup\bar J.
\]

This gives the first assertion of (4.1).  The source identifies the refined loopy invariant with extended U and ordinary `L` is a specialization of that refined invariant, so equality of extended U implies equality of ordinary `L`.  QED.

### Corollary 4.2 (join-generated n=12 no-go from the complete <=11 census)

Source Proposition 8.6 states that through eleven vertices the ordinary-U, extended-U, and loopy collision partitions coincide.  Hence every known ordinary-U collision seed in that complete range is already an extended-U collision.  Proposition 4.1 therefore implies:

\[
\boxed{\text{No simple n=12 separator can be obtained by joining a fixed graph to any <=11 U-collision seed.}}
\tag{4.2}
\]

More generally, repeatedly applying complement, disjoint union with a fixed graph, and join with a fixed graph to any source-certified extended-U collision cannot turn it into an ordinary-U / loopy separator.

This removes a large and very natural family of guaranteed n=12 U-collisions **symbolically**, not by another finite gadget search.  It also explains why coning/joining the source's ten-vertex collision pair was not a promising continuation of the previous two-terminal experiment.

I have not found this refined join-closure corollary stated explicitly in the source.  The proof is short and uses the source equivalences, so I label it **SELF-CHECK ONLY** pending an independent audit rather than presenting it as literature novelty.

## 5. Exact finite checker

Idea note, written before the checker artifact:

- `artifacts/R20/2026-09-18T14-50-00Z_knsv_dual_join_ideas_7d4c2a.md`
- commit `8fe652b6d8406125d25c62fa6f4455c786d0a3cc`.

Exact checker:

- `artifacts/R20/knsv_seven_vertex_dual_check.py`
- commit `1b442d0ffe5dbbbbff776b17d3a72ef049939dbf`.

Archived executed output:

- `artifacts/R20/knsv_seven_vertex_dual_check.out`
- commit `16e8b8e94fb8797d4ad20b3d89fec084fff1e152`.

The checker is self-contained: it decodes the twelve graph6 strings, enumerates all spanning edge subsets to form ordinary U exactly over `Z`, computes `h1` exactly from connected spanning subgraphs on four-sets with triangular complements, and verifies (2.2)--(2.3).  Its terminal lines are

`ordinary_U_weighted_sums_equal= True`

`h1_weighted_sum_left= 1`

`h1_weighted_sum_right= 4`

`VERDICT=PASS`

with scope explicitly `PARTIAL_ONLY`.

This is a **SELF-CHECK / EXACT-FINITE** certificate, not an independent audit.

## 6. What moved and what did not

The source metric does **not** move:

\[
N_{\rm sep}>11\quad\longrightarrow\quad N_{\rm sep}>11.
\]

But two proof/search architectures moved substantially:

1. **local-linear recovery is dead.**  There is an exact 12-type dual certificate showing that even `h1` cannot be a universal linear combination of seven-vertex ordinary-U coefficient functions;
2. **join-generated first-order counterexamples are dead.**  Any collision seed from the complete <=11 source census is extended-U-equal, and refined equality survives every fixed join, so such a lift cannot separate ordinary `L` at n=12 or later.

The remaining useful search space is therefore more primitive: an actual separator must be a U-collision in which refined/extended information has already split, and at the first hidden block profile that split can be detected by `(h1,h2,h3)`.  In particular, a minimal n=12 counterexample cannot be merely a join-lift of a previously known collision class.

The exact remaining obligation is still one of:

- produce a simple pair with exact `U_G=U_H` and exact `L_G\ne L_H` (a discrepancy in the hidden vector would suffice in the attacked direction); or
- prove that ordinary U forces every transformed block layer for all simple graphs.

No closure, refutation, or `N_sep>12` claim is made.

## 7. Next genuinely different methods

Do not repeat #11/#19/#24 next run.  The next three moves are:

- **#4 PROVE SOMETHING WEAKER, COMPLETELY:** characterize the full `(4,3,1^{n-7})` implication on a nontrivial graph class larger than triangle-free graphs, with an exact formula rather than another search;
- **#20 FIND WHY THE ALGORITHM FAILS:** determine the weakest nonlinear/additive statistic of the seven-vertex ordinary-U vector that could recover `h1` despite the exact linear dual obstruction, and prove a no-go or a lifting theorem;
- **#27 SWAP THE QUANTIFIERS:** instead of searching all n=12 graphs, classify U-collision classes that are *refined-primitive* (not generated from smaller extended collisions by complement/union/join), then search only those for hidden-vector discrepancy.

If the metric/remaining obligation is unchanged for three consecutive runs under a known count, the next run must invoke the Section-I stuck protocol.  The inherited unchanged count is still `UNKNOWN`, and this run preserves it as `UNKNOWN` rather than inventing a streak.

## 8. Model/scheduler control

The requested GPT-6 / maximum setting is still not enforceable from the scheduler surface documented in the operative repository implementation record.  The actual runtime model here is GPT-5.6 Sol and the reasoning level is UNVERIFIED.  The exposed control surface records prompt/title/schedule/timing/enabled state but has **no binding model-family selector, no reasoning-effort selector, no authenticated completed-run model receipt, and no guaranteed hour-long execution control**.

The historical P26 response `You cannot modify this task` was authorization-context-specific; repository history records later success from a different authorized context.  The lawful route is the owning/admin-authorized product or backend surface, or platform support.  There is no legitimate permission-bypass workaround.  No scheduler change was attempted in this run.

## 9. Structured ledger delta

```yaml
ledger_delta:
  worker: R20
  source: "Kirillov--Nenashev--Shapiro--Vaintrob, arXiv:2609.07728v1, Conjecture 8.2"
  source_scope: "simple graphs; equivalence of ordinary loopy L and ordinary U distinguishing power"
  metric: N_sep
  metric_definition: "minimum vertex count of a rigorously certified simple U/L separator in either direction"
  before: ">11"
  after: ">11"
  status: "PARTIAL / CLAIMED / OPEN-looking"
  unchanged_count_before: UNKNOWN
  unchanged_count_after: UNKNOWN
  tried_moves: [11, 19, 24]
  evidence:
    - "operations/claims/KNSV-2026-LOOPY-U.md"
    - "runs/R20/2026-09-18T14-13-09Z_knsv_graphical_block_rigidity_two_terminal_0c51e7.md"
    - "artifacts/R20/2026-09-18T14-50-00Z_knsv_dual_join_ideas_7d4c2a.md"
    - "artifacts/R20/knsv_seven_vertex_dual_check.py"
    - "artifacts/R20/knsv_seven_vertex_dual_check.out"
  audit_ids: []
  new_exact_finite_result: "Exact weighted relation between twelve seven-vertex graph types: ordinary-U sums agree coefficientwise over Z, while h1 weighted sums are 1 versus 4. Therefore h1 is not a universal linear combination of seven-vertex ordinary-U coefficient functions."
  new_symbolic_reduction: "If U_ext(G)=U_ext(H), then U_ext(G vee J)=U_ext(H vee J) for every fixed simple J; hence L also agrees. Since every <=11 source U-collision is also an extended-U collision, no join-generated lift of the complete known census can be an n=12 loopy separator. SELF_CHECK_ONLY pending audit."
  remaining_obligation: "Find a source-valid simple separator or prove full equivalence. Search refined-primitive U-collisions; use (h1,h2,h3) as the first exact separator filter; linear local recovery of h1 is now ruled out."
  next_moves: [4, 20, 27]
  retired_predecessor: "I0100 Paley one-localization remains frozen at p_max=1213; not reopened"
```

**NO I0100 REOPENING. NO CONJECTURE-8.2 CLOSURE OR REFUTATION CLAIM. CURRENT R20 STATUS: PARTIAL / CLAIMED / OPEN-looking.**
