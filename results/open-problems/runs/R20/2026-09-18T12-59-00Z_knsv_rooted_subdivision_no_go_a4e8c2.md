Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: `N_sep > 11 -> N_sep > 11`; methods #9 RANDOMIZE, #23 DO WHAT THE PROPOSER DID NOT EXPECT, #30 ONE SCALE / ONE DIRECTION AT A TIME.**

# R20 — KNSV Conjecture 8.2: rooted-gadget module and minimal-order simpleification no-go

## 0. Controlling state recovered

I started from current `master`, not from the stale scheduler title. The retired Paley I0100 track remains frozen at exact-certified frontier `p_max=1213` after its six-unchanged-run handoff; I did not reopen it. The current exclusive R20 claim is instead `operations/claims/KNSV-2026-LOOPY-U.md`, created at commit `7b4c47c2c5d22c9d691b50156346871481e3894b` and classified **CLAIMED / READY / CLOSABLE OUTSIDE**.

The source is Anatol Kirillov, Gleb Nenashev, Boris Shapiro and Arkady Vaintrob, *The Loopy Polynomial: from Tutte's Universal V-Function to Bizonotopal Geometry*, arXiv:2609.07728v1 (7 September 2026), Conjecture 8.2. For **simple graphs** it asks whether

\[
L_G=L_H\iff U_G=U_H\iff \eta_G=\eta_H\iff X_{B,G}=X_{B,H}.
\]

The last three equivalences are classical in the source; the conjectural content is ordinary loopy `L` versus ordinary `U`. The source verifies the equivalence for all simple graphs on at most 11 vertices, so a source-valid separator must have at least 12 vertices. The source also gives a five-vertex **loopless multigraph** pair with `U_G=U_H` but `L_G\ne L_H`; the only issue for Conjecture 8.2 is simplicity.

Fresh source/status check, 18 September 2026: the current arXiv/source paper still states Conjecture 8.2, and bounded web queries for the exact title, exact arXiv id `2609.07728`, `Conjecture 8.2`, `proof`, and `counterexample` found the source/mirrors but no later source-matching proof or refutation. This is bounded negative evidence only. The author-hosted PDF was inspected directly at the pages containing Conjecture 8.2 and Theorem 8.10 / Example 8.11. The source is only eleven days old, so citing-paper evidence is necessarily sparse.

The predecessor R20 artifacts already tested every rooted two-new-vertex simple gadget attached through one old root of the source's ten-vertex collision pair `I?bB@_wYO`, `I?bB@_wk_`: among 3,600 cross extensions there were 208 `U` collisions, 8 nontrivial ones, and **zero** `U`-equal / `L(1,x)`-different separators. That predecessor finite miss was PARTIAL and did not move `N_sep`.

## 1. Idea before code

The new ideas were written first in

`artifacts/R20/2026-09-18T12-55-00Z_knsv_route_ideas.md`

at commit `466e8d63dddf9dae6c532404f93a6335d1bce06d`.

The run then pursued two genuinely different source-generated mechanisms rather than extending the old two-vertex checker mechanically.

## 2. #9 RANDOMIZE — replace raw graph search by the rooted-state module

Let `R_U(G,r)` retain, for every spanning edge set, the size of the component containing the root `r`, the multiset of sizes of all other components, and total cyclomatic number. Let `P_L(G,r)` retain, for every spanning forest, the loopy exponent of the root component separately from the multiset of exponents of all other components, at `t=1`.

For a one-vertex sum of rooted graphs `(G,r)` and `(K,\rho)`, these states glue bilinearly.

For `U`, an edge subset is uniquely a pair `(A_G,A_K)`. The two root components merge and have size

\[
s_G+s_K-1,
\]

all other components are unchanged, and cyclomatic numbers add. Therefore ordinary `U` of the glued graph is exactly the convolution

\[
(s_G,O_G,c_G),(s_K,O_K,c_K)
\mapsto
(\operatorname{sort}(s_G+s_K-1,O_G,O_K),c_G+c_K).
\]

For `L(1,x)`, choose an edge order with all edges of one summand in one block and all edges of the other summand in the other block. A cycle cannot cross the articulation vertex, so spanning forests split and external activities are computed independently inside the two summands. The two root-component exponents therefore add, while all other component exponents are retained. Since the loopy polynomial is order-independent, this gives the exact convolution

\[
(a_G,O_G),(a_K,O_K)
\mapsto
\operatorname{sort}(a_G+a_K,O_G,O_K).
\]

This is useful because an arbitrary small rooted gadget can now be explored through its finite rooted state, rather than by recomputing an entire 13-vertex graph invariant from scratch.

### Exact seed-state result

For the KNSV ten-vertex seed pair, exact arithmetic gives the complete cross-root collision relations

\[
R_U(G_1,i)=R_U(G_2,j)
\iff (i,j)\in\{(2,2),(9,9)\},
\]

and independently

\[
P_L(G_1,i)=P_L(G_2,j)
\iff (i,j)\in\{(2,2),(9,9)\}.
\]

Thus the rooted-`U` and pointed-loopy collision relations **coincide exactly** on this seed pair. Consequently, any one-root construction whose preservation of `U` is justified merely by equality of the rooted-`U` states is structurally dead here: the same root pair already has equal pointed loopy state, and every rooted one-sum gadget preserves the `L` collision as well.

This does not rule out an accidental noninjective `U` convolution from two unequal rooted states, so I tested that possibility next.

### All rooted simple gadgets on three new vertices

There are `2^6=64` labelled simple graphs on `{root,a,b,c}`. I computed the exact rooted `U` and pointed `L(1,x)` state of all 64, attached each gadget to each of the ten roots of each seed graph, and compared all

\[
(10\cdot64)^2=409600
\]

cross extensions. Results:

- extensions per seed: `640`;
- exact `U`-equal cross pairs: `2472`;
- exact `U`-equal but `L(1,x)`-different pairs: **`0`**.

Therefore **no simple one-root gadget on exactly three new vertices turns this KNSV seed collision into a Conjecture-8.2 separator**. Together with the predecessor two-new-vertex run, this exhausts this source seed under arbitrary one-root gadgets of orders 3 and 4 (root included), reaching total graph orders 12 and 13 in that architecture.

This is a finite architecture no-go only, not a statement about arbitrary simple graphs.

## 3. #23 DO WHAT THE PROPOSER DID NOT EXPECT — simple-ify their multigraph counterexample

The source's Theorem 8.10 / Example 8.11 already has exactly the separation we want, but on loopless multigraphs. Its common underlying simple support is the 5-cycle `1,3,5,2,4` plus chord `{1,5}`, with edge order

\[
\{1,3\},\{3,5\},\{5,2\},\{2,4\},\{4,1\},\{1,5\},
\]

and multiplicities

\[
G_1:(1,2,2,3,1,1),\qquad
G_2:(1,2,1,2,3,1).
\]

Both have ten edge copies. Keep one copy of each of the six support edges as a direct simple edge. There are then four extra parallel copies. Replace each extra copy by an internally vertex-disjoint path. If the four path-internal vertex counts are positive integers `a_1,...,a_4`, the resulting graph is simple. At the **minimum possible source order** `n=12`, we require

\[
a_1+a_2+a_3+a_4=7.
\]

There are exactly

\[
\binom{6}{3}=20
\]

positive compositions on each side. Every resulting graph has 12 vertices and

\[
6+(7+4)=17
\]

edges. Thus there are only `20 x 20 = 400` exact cross comparisons.

The result is sharper than merely finding no separator: **none of the 400 pairs even has equal ordinary `U`**. Therefore this entire minimal-order independent-subdivision simpleification of the source's multigraph counterexample cannot refute Conjecture 8.2.

## 4. #30 ONE SCALE / ONE DIRECTION AT A TIME — what the two failures say

The first possible counterexample order remains `n=12`. Two very natural ways of transporting the source's own non-simple/pointed obstructions into that order now fail for precise reasons:

1. the one-root route factors through rooted states, and on the ten-vertex collision seed the exact rooted-`U` collision relation is already identical to the pointed-loopy collision relation; all three-new-vertex accidental collapses were also checked and failed;
2. the explicit multigraph separator loses its ordinary-`U` equality under every minimal `n=12` independent path-simpleification in the 20-by-20 family.

So the next attack should not add another lemma to either architecture. The first qualitatively new place is a **two-root / two-terminal gadget**: a new vertex or small gadget must meet at least two old seed vertices so that pointed information from different components can mix rather than factor through one articulation. This also matches the source's block-transform formulation: the first possible obstruction occurs only once at least two nonsingleton blocks interact.

Recommended next Section-B triple, not repeating this run: **#15 BREAK THE SYMMETRY ON PURPOSE, #18 SAY IT IN ANOTHER LANGUAGE, #25 COUNT THE SAME THING TWICE.** Concretely: classify two-root attachment orbits under the seed automorphism groups; rewrite their `U` effect as a two-terminal partition-state transfer matrix; use the same transfer matrix to identify which exact coefficient of `L(1,x)` can escape the `U` constraints.

## 5. Exact checker and output

The finite claims above are checked over the integers, with no floating point arithmetic:

- checker: `artifacts/R20/knsv_next_routes_check.py`, commit `7b1ebce91ff8052364652f52b3e6a40af5cf2639`;
- executed output: `artifacts/R20/knsv_next_routes_check.out`, commit `ed4ec320e1ea655dd2bcbf2ad100d01333bac61f`.

The archived output records:

- `rooted_U_cross_matches=[(2,2),(9,9)]`;
- `pointed_L1_cross_matches=[(2,2),(9,9)]`;
- 409,600 rooted three-new-vertex cross extensions, 2,472 exact `U` collisions, 0 separators;
- 400 minimal-order subdivision simpleifications, 0 exact `U` collisions.

These are **SELF_CHECK / EXACT-FINITE** results. No independent audit is claimed.

## 6. Model / scheduler control

The model request in the task text remains unenforceable from the exposed scheduler surface. The actual model for this run is GPT-5.6 Sol and the reasoning level is UNVERIFIED. The current task-control schema exposes prompt/title, schedule or offset, timing mode and enabled state; it exposes **no binding model-family selector, no reasoning-effort selector, no authenticated applied-model receipt, and no guaranteed one-hour execution field**. Enforcing GPT-6 / maximum would require an authorized product/backend scheduler surface that exposes model and reasoning fields and attests what actually ran.

The historical P26 `You cannot modify this task` response remains an authorization-context boundary, not a mathematical blocker. Repository history records a later successful P26 edit from an authorized context. The lawful workaround is owner/admin-authorized access or platform support; no duplication or permission bypass is appropriate. No scheduler changes were attempted in this run.

## 7. Status and ledger delta

No source-level proof or refutation is claimed. Conjecture 8.2 remains current-open-looking after the bounded 18 September literature check. The exact metric does not move.

```yaml
ledger_delta:
  worker: R20
  source: "Kirillov--Nenashev--Shapiro--Vaintrob, arXiv:2609.07728v1, Conjecture 8.2"
  source_scope: "simple graphs; equivalence of ordinary L and ordinary U distinguishing power"
  metric: N_sep
  metric_definition: "minimum vertex count of a rigorously certified simple U/L separator"
  before: ">11"
  after: ">11"
  status: "PARTIAL / CLAIMED / OPEN-looking"
  unchanged_count_before: UNKNOWN
  unchanged_count_after: UNKNOWN
  tried_moves: [9, 23, 30]
  evidence:
    - "operations/claims/KNSV-2026-LOOPY-U.md"
    - "artifacts/R20/knsv_loopy_rooted_gadget_check.out"
    - "artifacts/R20/2026-09-18T12-55-00Z_knsv_route_ideas.md"
    - "artifacts/R20/knsv_next_routes_check.py"
    - "artifacts/R20/knsv_next_routes_check.out"
  audit_ids: []
  remaining_obligation: "Find a source-valid simple pair with U_G=U_H and L_G!=L_H or L_G=L_H and U_G!=U_H, or prove the full simple-graph equivalence. Next route must leave one-root and independent-subdivision architectures."
  retired_predecessor: "I0100 Paley one-localization remains frozen at p_max=1213; not reopened"
```

**NO I0100 REOPENING. NO CONJECTURE-8.2 CLOSURE CLAIM. CURRENT R20 TARGET = KNSV-2026-LOOPY-U, PARTIAL.**
