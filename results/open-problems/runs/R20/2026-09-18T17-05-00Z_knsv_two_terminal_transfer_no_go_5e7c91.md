Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: `N_sep > 11 -> N_sep > 11`; methods #10 DERANDOMIZE, #12 FIND WHAT IS CONSERVED, #21 ASK WHO ELSE HAS THIS SHAPE.**

# R20 — KNSV Conjecture 8.2: exact two-terminal-transfer no-go at the first open order

## 0. Continuity, ownership, source status, and method-history correction

R20 does **not** reopen the retired Paley one-localization predecessor I0100.  Its frozen historical metric remains `p_max=1213`.  The current exclusive R20 target is the create-only reservation

`operations/claims/KNSV-2026-LOOPY-U.md`,

owned by R20 and marked `CLAIMED / READY / CLOSABLE OUTSIDE`.

Current source:

- Anatol Kirillov, Gleb Nenashev, Boris Shapiro, Arkady Vaintrob, *The Loopy Polynomial: from Tutte's Universal V-Function to Bizonotopal Geometry*, arXiv:2609.07728v1, Conjecture 8.2.
- Exact source scope: for **simple graphs** the ordinary loopy polynomial `L` and ordinary `U` have the same distinguishing power (equivalently with the other invariants listed in the source).
- Fixed R20 metric: `N_sep`, the least order of a rigorously certified simple pair separating ordinary `U` and `L` in either direction.
- Source baseline: the paper reports exhaustive verification through 11 vertices, hence `N_sep>11`.

Fresh status check, 18 September 2026: bounded current-web queries used the exact title, exact arXiv id `2609.07728`, author names, `Conjecture 8.2`, `proof`, `counterexample`, and `simple graph`.  The current accessible arXiv record is still the September 2026 paper and the current Boris Shapiro paper list still lists the paper as submitted.  I found no later source-matching proof or simple-graph counterexample in the accessible search.  This is bounded negative evidence only, not a claim about inaccessible literature.

Repository continuity was read before research: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the KNSV ownership claim, the newest R20 report, and the KNSV-specific R20 search history.  Repository search for exact arXiv id `2609.07728` recovered the KNSV claim and R20 reports, with no peer-track ownership collision.

The idea-before-code artifact initially listed planned moves #10/#18/#25.  The required history check showed #18 and #25 had already been used on this KNSV target two runs earlier, so they are **not counted** as this run's three new moves.  The substantive run replaced them by unused moves #12 and #21.  The counted new triple is therefore exactly **#10, #12, #21**.

## 1. Starting point from the required stuck recovery

The preceding thinking-only report selected exactly one recovery action: port the technique from the source's nearest solved problem, Theorem 8.10 / Example 8.11.  KNSV give a five-vertex **loopless multigraph** pair with equal ordinary `U` but distinct `L`.  In R20's zero-based labeling both multigraphs have common six-edge simple support

\[
E_0=\{02,24,41,13,30,04\},
\]

with edge multiplicities

\[
M_1=(1,2,2,3,1,1),\qquad
M_2=(1,2,1,2,3,1).
\]

Thus each side has four excess parallel-edge copies.  The earlier path-only simpleification kept one direct edge on every support edge and replaced each excess copy by a path.  At the first possible simple order `n=12`, all 400 such positive path-length allocations failed even to preserve `U`.

This run ports the multigraph mechanism much more generally: **a path is replaced by an arbitrary connected simple two-terminal network**.

## 2. The exact family attacked

Keep one direct edge on every edge of `E_0`.  For each of the four excess parallel copies, insert a connected simple two-terminal network `N` satisfying:

1. its two boundary terminals are the endpoints of that support edge;
2. it has no terminal-terminal edge, because that direct edge is already present in the simple support;
3. its internal vertices are disjoint from all other replacement networks;
4. the four networks have positive internal-vertex counts `r_1,...,r_4` with
   \[
   r_1+r_2+r_3+r_4=7,
   \]
   so the glued graph has exactly twelve vertices.

For `M_1` the four excess-copy slots lie on support-edge indices `(1,2,3,3)`; for `M_2` they lie on `(1,3,4,4)`.  Since all four `r_i` are positive and sum to seven, only `r=1,2,3,4` can occur in an individual network.

This family strictly contains the previous path-only family: it permits arbitrary branching and local cycles inside each replacement network.  It does **not** permit different excess-copy networks to share an internal vertex or an edge between their internal vertex sets.  That distinction becomes the next obstruction after the theorem below.

## 3. Exact two-terminal transfer signature

For a two-terminal network `N` with terminals `s,t`, and for every selected-edge subset `A subseteq E(N)`, record:

- whether `s,t` lie in the same component;
- if they are connected: the number of internal vertices in their common boundary component;
- if they are separated: the numbers of internal vertices in the `s`- and `t`-components, in terminal order;
- the multiset of sizes of all components disjoint from both terminals;
- `|A|`.

The **transfer signature** `Sigma(N)` is the integer multiplicity table of those states over all `A subseteq E(N)`.

### Lemma 3.1 — transfer sufficiency

If two networks `N,N'` with the same number of internal vertices have

\[
\Sigma(N)=\Sigma(N'),
\]

then replacing `N` by `N'` inside any host graph that meets the network only in the two terminals leaves the ordinary `U`-polynomial unchanged.

### Proof

Fix a selected host-edge subset `B`.  Every selected edge set in the glued graph decomposes uniquely as `B union A`, with `A subseteq E(N)`.  The transfer state tells exactly how the network components attach to the two host terminal components: either the two host components are merged, or they stay separate; it tells how many network vertices are added to each resulting boundary component; and it supplies the sizes of every network component closed away from the host.  Together with `|A|`, this determines both the final component-size partition and

\[
|A|+|B|-|V|+k(A\cup B),
\]

the total cyclomatic exponent in the ordinary `U` term.  Therefore each transfer state contributes the same ordinary-`U` monomial with the same multiplicity for `N` and `N'`.  Summing first over `A` and then over `B` proves the claim.  `square`

This is the conserved object sought under move #12.  It allows us to keep only one representative of each exact transfer type without losing any possible `U`-collision in the attacked family.

## 4. Exhaustive transfer quotient

The checker enumerates every labelled simple graph on terminals `0,1` plus `r` internal vertices, forbids edge `01`, retains exactly the connected networks, and forms `Sigma(N)` over the integers.

The exact counts are:

| internal vertices `r` | connected labelled networks | distinct exact transfer types |
|---:|---:|---:|
| 1 | 1 | 1 |
| 2 | 14 | 8 |
| 3 | 314 | 67 |
| 4 | 12,424 | 701 |

There are exactly 20 positive compositions of seven into four parts.  Consequently the complete transfer-quotient search has

\[
\sum_{r_1+\cdots+r_4=7\atop r_i\ge1}
T_{r_1}T_{r_2}T_{r_3}T_{r_4}
=11{,}284
\]

assignments on **each** multigraph side, where

\[
(T_1,T_2,T_3,T_4)=(1,8,67,701).
\]

Thus 11,284 representatives per side cover all labelled-network choices in the stated family up to the exact ordinary-`U` transfer relation.

## 5. A different language: the matrix-forest shadow of `U`

The decisive speedup does not compute the full `U` polynomial 22,568 times.  It moves to the Laplacian.

Let `L_G` be the graph Laplacian.  The cyclomatic-zero part of ordinary `U_G` counts spanning forests by component-size partition.  By the rooted matrix-forest theorem,

\[
\boxed{
\det(zI+L_G)
=
\sum_{F\text{ spanning forest}}
 z^{k(F)}\prod_{C\in F}|C|.
}
\tag{5.1}
\]

Indeed, for each unrooted spanning forest, choosing one root in each component gives exactly `prod_C |C|` rooted forests.  Therefore the right-hand side of (5.1) is obtained directly from the `q^0` / cyclomatic-zero coefficients of ordinary `U_G` by multiplying a component-size monomial `x_lambda` by `z^{ell(lambda)} prod_i lambda_i`.

Hence

\[
U_G=U_H
\quad\Longrightarrow\quad
\det(zI+L_G)=\det(zI+L_H)
\quad\Longrightarrow\quad
\operatorname{tr}(L_G^j)=\operatorname{tr}(L_H^j)
\quad(j\ge1).
\tag{5.2}
\]

This is move #21: an invariant from the matrix-forest/Laplacian language gives an exact necessary condition for a `U`-collision.

The checker uses the first nine integer power traces only.  No floating point is involved.  Its signed-64-bit matrix products are provably safe: for a simple 12-vertex graph `Delta<=11`, and the explicit conservative dot-product bound through the ninth power is

\[
12\cdot 11\cdot 22^8
=7{,}243{,}615{,}306{,}752
<2^{63}-1.
\]

## 6. Exact result: the entire independent-network port fails at n=12

For all 11,284 quotient representatives on each side, the exact common-moment-pair counts after imposing successively

\[
(\operatorname{tr}L,\ldots,\operatorname{tr}L^k)
\]

are:

| `k` | common moment vectors | cross pairs remaining |
|---:|---:|---:|
| 1 | 10 | 25,170,416 |
| 2 | 143 | 2,118,156 |
| 3 | 633 | 423,874 |
| 4 | 1,456 | 34,824 |
| 5 | 369 | 2,715 |
| 6 | 22 | 185 |
| 7 | 3 | 19 |
| 8 | 1 | 2 |
| **9** | **0** | **0** |

Therefore equation (5.2) gives the exact finite theorem

\[
\boxed{
\text{No pair in the full independent connected two-terminal replacement family at }n=12
\text{ has equal ordinary }U.
}
\tag{6.1}
\]

In particular, this family cannot port KNSV's loopless-multigraph `U/L` separator into a simple 12-vertex separator.

This is a route-level no-go only.  It **does not** imply `N_sep>12`, because arbitrary simple 12-vertex graphs and simpleifications with cross-coupled/shared internal vertices are outside the searched family.

## 7. The last near-collision and an independent exact readback

Only one moment vector survives through power eight:

\[
(36,172,972,5968,38456,255826,1741160,12055528).
\]

It corresponds to two quotient representatives on side 1 and one on side 2.  At the ninth trace they split:

\[
84{,}587{,}130\quad\text{versus}\quad84{,}587{,}076,
\]

a gap of 54.

One representative pair has graph6 codes

`KUwgQSASA_A?`

and

`KUwgWPO?K_Q?`.

As a move-#10 derandomization consistency check, the script then ignores the Laplacian filter and recomputes ordinary `U` on this final near pair **twice**:

1. directly, by exact spanning-edge-subset partition DP on the glued 12-vertex graph;
2. from the two-terminal transfer tables plus exact host gluing.

The two routes agree on each graph.  The two graphs are not `U`-equal.  Their first displayed coefficient discrepancy is

\[
[x_{4}x_1^8 q^0]U:\qquad149\quad\text{versus}\quad147.
\]

The exact polynomial digests archived by the checker are

- side 1: `16f9ff67abb0ac19019e9c8761a8151e039e4e105c1d7e7c074545fe27f682f8`;
- side 2: `f2bf23684917cecf61f25a025fef39d58f51213f950cfba3628090cce967e63e`.

This direct recomputation is validation of the finite route theorem; it is not promoted to a global conjecture claim.

## 8. Section-B moves and what happened

### #10 DERANDOMIZE

Instead of trying random gadgets, quotient every possible connected simple replacement network of the required sizes by an exact ordinary-`U` boundary transfer state.  Outcome: the intended port becomes a finite exhaustive search of 11,284 transfer assignments per side, and the complete family is eliminated at `n=12`.

### #12 FIND WHAT IS CONSERVED

The transfer signature `Sigma(N)` is the exact conserved object under arbitrary two-terminal substitution into a host.  Outcome: labelled graph multiplicity collapses from 1/14/314/12,424 networks to 1/8/67/701 exact transfer types for `r=1,2,3,4`.

### #21 ASK WHO ELSE HAS THIS SHAPE

The forest layer of ordinary `U` is exactly the data needed for the rooted matrix-forest determinant.  Outcome: Laplacian power traces become a cheap, exact, rigorously necessary collision filter.  Nine traces eliminate every cross-side transfer assignment; the final near pair is then checked directly in `U`.

The previously planned #18/#25 are not counted because KNSV history showed they had already been used.

## 9. What this teaches the next route

The multigraph mechanism cannot survive at minimal order by replacing the four excess edge copies with **independent** connected two-terminal networks.  Therefore a fixed-support minimal-order port must use something absent from this whole family.  The most economical missing mechanism is **cross-coupling**: internal vertices or internal edges must interact across two excess copies, especially inside the multiplicity-three bundle, or the support itself must change.

The next run should not add a larger independent gadget.  It should first allow one controlled interaction between the two replacement pieces on the multiplicity-three support edge and quotient by the automorphism of the five-cycle-with-chord support.  That is the smallest architecture not killed by (6.1).

Next unused Section-B moves for this KNSV target:

- **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT:** use the number/type of cross-coupling edges as a deformation parameter away from the now-exhausted independent family;
- **#14 FIND THE GROUP ACTING:** quotient support-edge and terminal-network relabelings before any search;
- **#26 HUNT THE SPORADIC CASE:** attack the first one-cross-edge coupled family at exactly `n=12` before considering larger orders.

The remaining source obligation is unchanged: produce an actual simple pair separating `U` and `L`, or prove source-level equivalence.  Restricted no-go families remain PARTIAL.

## 10. Exact artifacts and execution

Idea before code:

- `artifacts/R20/2026-09-18T16-55-00Z_knsv_two_terminal_transfer_idea.md`
- creation commit `bfd734d58c75fd8a14328c38f0102d2a33c15d78`.

Exact checker:

- `artifacts/R20/knsv_two_terminal_transfer_n12_check.py`
- creation commit `8cce83c29c8f46930281cff10ac1059f00abdf1f`.

Executed output:

- `artifacts/R20/knsv_two_terminal_transfer_n12_check.out`
- creation commit `50443493ef48e364d758b0e3b2a42f60edbf5f78`.

The output ends

`VERDICT=PASS: no ordinary-U collision exists in the full independent connected two-terminal replacement family at n=12.`

and immediately records the strict PARTIAL scope.  This is a self-check, not an independent fleet audit.

## 11. Model / scheduler limitation

The implementation record remains unchanged.  The exposed automation-control schema offers prompt/title/schedule/timing/enabled controls, but no binding model-family selector, no reasoning-effort selector, no authenticated completed-run model receipt, and no guaranteed one-hour execution field.  Therefore `GPT-6 / maximum` remains prompt text rather than an enforceable scheduler setting on this worker surface; the present report honestly identifies the actual model as GPT-5.6 Sol with reasoning level UNVERIFIED.

The historical P26 `You cannot modify this task` failure was authorization-context-specific; the repository records that a later authorized context succeeded.  The lawful workaround remains an owner/admin-authorized product or backend surface that exposes the control, or platform support.  No permission bypass, duplicate scheduler, or scheduler edit was attempted in this run.

## 12. Structured ledger delta

```yaml
ledger_delta:
  worker: R20
  source: "KNSV arXiv:2609.07728v1, Conjecture 8.2"
  ownership: "operations/claims/KNSV-2026-LOOPY-U.md; exclusive R20"
  predecessor: "I0100 retired; historical p_max=1213; not reopened"
  metric: "N_sep = minimum simple-graph U/L separator order"
  before: ">11"
  after: ">11"
  metric_movement: "none"
  status: "PARTIAL / CLAIMED / OPEN-looking / EXACT ROUTE NO-GO"
  unchanged_count_before: UNKNOWN
  unchanged_count_after: UNKNOWN
  tried_moves: [10, 12, 21]
  finite_result:
    family: "four independent connected simple two-terminal replacements of the four excess copies in KNSV Example 8.11; seven internal vertices total; n=12"
    transfer_types_r1_r4: [1, 8, 67, 701]
    transfer_assignments_per_side: 11284
    necessary_invariant: "tr(L^k), k=1,...,9, derived from the U forest layer via det(zI+L)"
    common_trace9_vectors: 0
    verdict: "no U-collision in this family"
  remaining_obligation: "source-valid simple U/L separator or full equivalence proof; next minimal missing architecture is cross-coupled/shared-internal-vertex replacement at n=12"
  evidence:
    - "artifacts/R20/2026-09-18T16-55-00Z_knsv_two_terminal_transfer_idea.md @ bfd734d58c75fd8a14328c38f0102d2a33c15d78"
    - "artifacts/R20/knsv_two_terminal_transfer_n12_check.py @ 8cce83c29c8f46930281cff10ac1059f00abdf1f"
    - "artifacts/R20/knsv_two_terminal_transfer_n12_check.out @ 50443493ef48e364d758b0e3b2a42f60edbf5f78"
  audit_ids: []
  audit_status: "SELF_CHECK_ONLY"
  next_moves: [5, 14, 26]
```

**NO I0100 REOPENING. NO KNSV CLOSURE OR REFUTATION CLAIM. CURRENT R20 STATUS: PARTIAL / CLAIMED / OPEN-looking.**
