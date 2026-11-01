Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: `N_sep > 11 -> N_sep > 11`; methods #5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #14 FIND THE GROUP ACTING, #26 HUNT THE SPORADIC CASE.**

# R20 — KNSV Conjecture 8.2: exact no-go for the full one-cross-edge simpleification family at n=12

## 0. Continuity, ownership, source, and current status

R20 does **not** reopen retired Paley one-localization I0100. Its frozen historical exact-certificate frontier remains `p_max=1213`. The current exclusive R20 target remains the create-only reservation

`operations/claims/KNSV-2026-LOOPY-U.md`,

for Anatol Kirillov, Gleb Nenashev, Boris Shapiro, Arkady Vaintrob, *The Loopy Polynomial: from Tutte's Universal V-Function to Bizonotopal Geometry*, arXiv:2609.07728v1, Conjecture 8.2.

The source conjectures that, on **simple graphs**, the ordinary loopy polynomial `L` and ordinary `U`-polynomial have the same distinguishing power. The source reports exhaustive verification through 11 vertices and gives a loopless-multigraph counterexample outside the simple-graph scope. Therefore the frozen source metric is

`N_sep = minimum order of a rigorously certified simple U/L separator`,

with source baseline `N_sep>11`.

Fresh current-source check on 18 September 2026: the accessible arXiv record is still v1, submitted 7 September 2026, and still states the simple-graph conjecture and verification through 11 vertices. Bounded queries using the exact title, arXiv id, author names, `Conjecture 8.2`, `proof`, `counterexample`, and `simple graph` found no later source-matching proof or simple-graph counterexample. This is bounded negative evidence only.

Before new work I recovered the current campaign INDEX/RANKING, root POSTED/RESULTS/QUEUE, the current implementation manifest, the KNSV claim, the newest R20 report, and the newer R20 idea/checker artifacts already present on master. Root `RESULTS.md` still has the stale historical R20/I0100 row; R20 does not edit shared roots.

## 1. Starting point and why this run is genuinely new

The preceding theorem eliminated every `n=12` simpleification of the KNSV five-vertex multigraph separator in which the four excess parallel copies are replaced by **independent** connected simple two-terminal networks whose seven total internal vertices are pairwise disjoint.

The smallest missing deformation is one edge between internal vertices belonging to two different replacement slots. The idea-before-code artifact fixed exactly this family before the new validation:

- four connected simple two-terminal replacement networks, no terminal edge;
- positive internal sizes `r_1+...+r_4=7`;
- exactly one additional edge joining an internal vertex of one slot to an internal vertex of a distinct slot;
- total order exactly `n=12`.

This is move #5: cross-coupling number `c` is the deformation parameter away from the completely independent family, and this run attacks the first value `c=1` only.

The first labelled checker showed that this family is large: 1,839,792 labelled cross-edge instances on each multigraph side. It left 47 common 12-trace vectors, 916 and 1,200 labelled instances on those vectors, and 832 side-2 instances matching a side-1 low-degree ordinary-`U` truncation. That was only a filter, not a theorem.

## 2. Exact group quotient: the labelled search collapses to 157,212 representatives per side

For a replacement network with `r` internal vertices, let terminal-fixed isomorphism mean graph isomorphism fixing both boundary terminals. For the two slots incident to the unique cross edge, additionally mark the internal endpoint used by the cross edge and require the isomorphism to fix that mark.

Because `r_1+...+r_4=7` with all `r_i>=1`, every slot has `1<=r<=4`. The new checker enumerates **every** connected simple two-terminal network on those sizes and canonically quotients by all internal permutations fixing the terminals, and in the pointed case by all internal permutations fixing terminals and the mark.

The exact rooted-isomorphism type counts are

| internal vertices `r` | unpointed terminal-fixed types | pointed terminal+mark-fixed types |
|---:|---:|---:|
| 1 | 1 | 1 |
| 2 | 8 | 14 |
| 3 | 67 | 171 |
| 4 | 701 | 2394 |

The checker independently recovers the complete labelled connected-network counts `1,14,314,12424`, agreeing with the previous transfer enumeration.

For every positive composition of seven into four parts and every one of the six unordered choices of coupled slots, the two coupled slots use pointed types and the other two use unpointed types. Thus the exact quotient size on each KNSV multigraph side is

\[
\boxed{
\sum_{r_1+\cdots+r_4=7\atop r_i\ge1}
\sum_{1\le s<t\le4}
P_{r_s}P_{r_t}\prod_{j\ne s,t}U_{r_j}
=157{,}212.
}
\]

### Coverage lemma

Every labelled graph in the stated one-cross-edge family is isomorphic to one of these 157,212 representatives.

**Proof.** Fix the four internal sizes and the pair of slots hit by the cross edge. In each uncoupled slot choose a terminal-fixed isomorphism to its canonical unpointed representative. In each coupled slot choose a terminal-and-mark-fixed isomorphism sending its cross-edge endpoint to the canonical marked internal vertex. The four maps agree on every shared support vertex because all terminal maps are fixed. Since internal vertex sets are disjoint, they glue to a bijection of the entire 12-vertex graph. It preserves every replacement-network edge, all six fixed support edges, and the unique cross edge because the two marked endpoints are preserved. Hence it is a graph isomorphism. `square`

This is the actual group action from move #14; unlike the earlier transfer quotient, it preserves **all** graph invariants, including both `U` and `L`, by literal rooted graph isomorphism.

## 3. Exact necessary filter from the forest shadow of U

As in the preceding run, ordinary `U_G` determines the rooted spanning-forest polynomial

\[
\det(zI+L_G)
=
\sum_{F\text{ spanning forest}}z^{k(F)}\prod_{C\in F}|C|.
\]

Therefore

\[
U_G=U_H \Longrightarrow
\operatorname{tr}(L_G^j)=\operatorname{tr}(L_H^j)
\quad(j\ge1).
\]

The checker computes the first twelve power traces exactly over the integers for every quotient representative. Across the two 157,212-element sides it finds

- `common_trace12 = 47`;
- `trace_survivor_instances = 117,122`;
- exactly `322` cross pairs sharing the complete 12-trace vector.

Thus any possible `U_G=U_H` pair in the attacked family lies among those 322 exact candidates.

## 4. Exact ordinary-U specialization kills 108 pairs

For the 239 trace-survivor instances, the checker evaluates the **full** ordinary `U` polynomial at the exact finite-field point

\[
q=7,
\qquad
x_s=s^2+22s+68,
\qquad
\bmod 1{,}000{,}000{,}007.
\]

The evaluator is not a truncation: it processes every edge by partition dynamic programming and exactly computes

\[
\sum_{A\subseteq E}
q^{|A|-|V|+k(A)}\prod_{C\in\pi(A)}x_{|C|}
\pmod{1{,}000{,}000{,}007}.
\]

If two integer `U` polynomials are equal, their values at this specialization must be equal. Therefore unequal residues are a rigorous certificate of `U`-inequality; equality of residues is **not** promoted to polynomial equality.

Of the 322 trace-matched cross pairs,

\[
\boxed{108}
\]

have unequal exact residues and therefore cannot be `U`-collisions.

As an implementation self-check, on a 19-edge survivor the dynamic-programming evaluation was recomputed by direct enumeration of all `2^19` spanning edge subsets. Both routes give

`357009066 mod 1000000007`.

## 5. The remaining 214 pairs are all exactly graph-isomorphic

For the 214 pairs that survive both the 12-trace filter and the full-`U` specialization, the checker performs an exact graph-isomorphism test by exhaustive backtracking on a bijection of the twelve vertices, pruned only by exact degree and neighbor-degree signatures. Every adjacency/nonadjacency relation to already mapped vertices is enforced at every recursion step. No hash or probabilistic isomorphism test is used.

The result is

- `specialization_equal_pairs = 214`;
- `specialization_equal_isomorphic_pairs = 214`;
- `specialization_equal_nonisomorphic_pairs = 0`.

This yields the route theorem:

\[
\boxed{\text{Within the full stated n=12 one-cross-edge family, there is no nonisomorphic cross-side pair with equal ordinary U.}}
\]

Consequently this entire one-cross-edge architecture contains **no counterexample in the attacked direction**

\[
U_G=U_H,
\qquad
L_G\ne L_H.
\]

This does **not** rule out the opposite source-separating direction `L_G=L_H` but `U_G!=U_H`, and it does not address arbitrary 12-vertex simple graphs. Hence it is PARTIAL and does not move `N_sep`.

## 6. Section-B moves and what happened

### #5 ADD A PARAMETER AND DIFFERENTIATE IN IT

Parameterize departure from the exhausted independent-network family by the number `c` of cross-coupling edges. The first new value `c=1` was attacked completely at `n=12`. Outcome: `c=1` still cannot port the KNSV multigraph `U`-collision in the direction sought.

### #14 FIND THE GROUP ACTING

Use terminal-fixed rooted isomorphism on uncoupled replacement networks and terminal+mark-fixed rooted isomorphism on the two coupled networks. Outcome: the labelled family collapses from 1,839,792 instances per side to 157,212 exact graph-isomorphism representatives per side, with a written coverage proof.

### #26 HUNT THE SPORADIC CASE

After exact spectral filtering, only 322 cross pairs remain. A full-`U` specialization eliminates 108; exact isomorphism identifies every one of the remaining 214 as the same graph on the two sides up to relabeling. Outcome: there is no sporadic nonisomorphic `U`-collision hidden in the one-cross-edge family.

## 7. What remains, and rotation state

The source obligation is unchanged: either exhibit an actual simple pair separating the collision relations of `U` and `L`, or prove their source-level equivalence. This report only kills the most economical cross-coupled port of the source's multigraph counterexample.

The next genuinely different architectures would be: two or more cross edges; shared internal vertices rather than a cross edge; changing the six-edge simple support; or abandoning the multigraph-port mechanism and searching primitive 12-vertex `U` collision fibers directly. Those are not claimed solved here.

This is the **sixth consecutive immutable KNSV research report visible from the first KNSV report at 12:59 UTC through this report with no movement of the frozen source metric**. Historical ledger fields recorded the stagnation counter itself as `UNKNOWN`, so this report does not retroactively rewrite that field. Nevertheless, the operational rule says a CLOSABLE target rotates after six unchanged runs. Therefore R20 records **ROTATION_DUE / HANDOFF_AFTER_THIS_RUN** and should not spend the next invocation on another KNSV gadget family unless the source is explicitly reassigned with a fresh route. The exclusive historical claim is not overwritten here; shared/operations files are left untouched.

If KNSV is later reassigned, the next unused methods recorded for that target are #6 DEFORM TO A POINT YOU CAN SOLVE, #13 FIND WHAT ONLY INCREASES, and #22 READ THE FAILURES, NOT THE SUCCESSES. The next ordinary R20 invocation should instead perform successor admission from the current queue under the source/current-status/ownership gates.

## 8. Exact artifacts

Idea-before-code already on master:

- `artifacts/R20/2026-09-18T17-50-00Z_knsv_cross_coupling_idea.md`.

Earlier labelled exploratory checker/output:

- `artifacts/R20/knsv_one_cross_edge_n12_exact.cpp`, creation commit `f8a1bf5ba3b3a91176fe3954cf2899a49c6543d0`;
- `artifacts/R20/knsv_one_cross_edge_n12_exact.out`, creation commit `6c81bd4002c0228727c3be704b1a572784c8dd17`.

Rooted-isomorphism completeness audit already on master:

- `artifacts/R20/knsv_transfer_signature_iso_n12_check.py`, commit `4558afc78047eff758711fc78b6ab16cdbcd2e92`;
- output commit `e4379ea18115bbe0b87e5a459ab59432b278267a`.

Final exact checker for this report:

- `artifacts/R20/knsv_one_cross_edge_quotient_exact.cpp`, commit `b919d582792bf4729dd4023143fd28784fadf28c`;
- exact executed output `artifacts/R20/knsv_one_cross_edge_quotient_exact.out`, commit `93108629831f8a34be3d51fe8c7dc2ad8bdc03aa`;
- script SHA-256 `6f105e75be1e6e80a89a11ffb16b86bcfa74204a2c75032dcad0cf5a03bd555f`.

All finite statements in Sections 2–5 are **SELF-CHECK ONLY** pending independent other-track audit. No P26 or second independent audit is claimed.

## 9. Scheduler/model control status

The current documented task-control surface still exposes prompt/title/schedule/timing/enabled controls but no binding model-family selector, no reasoning-effort selector, no authenticated applied-model receipt, and no guaranteed one-hour execution control. Thus `GPT-6 / maximum` remains a request in prompt text rather than an enforceable setting from this worker surface. The recorded P26 update attempt returned `You cannot modify this task`; the lawful workaround is an owner/admin-authorized product/backend context or platform support, not a permission bypass or duplicate task. No scheduler or permission change was attempted in this run.

## 10. Structured ledger delta

```yaml
ledger_delta:
  worker: R20
  source: "Kirillov-Nenashev-Shapiro-Vaintrob, arXiv:2609.07728v1, Conjecture 8.2"
  ownership: "operations/claims/KNSV-2026-LOOPY-U.md; exclusive R20 historical claim"
  metric: "N_sep = minimum order of a rigorously certified simple U/L separator in either direction"
  before: ">11"
  after: ">11"
  movement: "NO MOVEMENT"
  status: "PARTIAL / SELF_CHECK_ONLY / ROTATION_DUE"
  unchanged_count_field_before: "UNKNOWN"
  unchanged_count_field_after: "UNKNOWN"
  observed_consecutive_no_metric_movement_KNSV_reports_including_this_one: 6
  tried_moves: [5, 14, 26]
  new_finite_result: "No nonisomorphic U-equal cross-side pair exists in the complete rooted-isomorphism quotient of the n=12 one-cross-edge port family."
  exact_counts:
    quotient_instances_per_side: 157212
    common_trace12: 47
    trace_cross_pairs: 322
    U_specialization_unequal_pairs: 108
    U_specialization_equal_pairs: 214
    exact_isomorphic_pairs: 214
    exact_nonisomorphic_survivors: 0
  remaining_obligation: "Settle KNSV Conjecture 8.2 on all simple graphs: actual U/L separator in either direction, or source-level equivalence proof."
  next_state: "HANDOFF_AFTER_THIS_RUN; next R20 invocation should perform successor admission unless explicitly reassigned"
  evidence:
    - "b919d582792bf4729dd4023143fd28784fadf28c: final exact checker"
    - "93108629831f8a34be3d51fe8c7dc2ad8bdc03aa: executed checker output"
    - "e4379ea18115bbe0b87e5a459ab59432b278267a: rooted/pointed isomorphism completeness output"
  audits: []
```

**NO I0100 REOPENING. NO KNSV CLOSURE OR REFUTATION CLAIM. `N_sep` REMAINS `>11`. KNSV IS HANDED OFF AFTER THIS SIXTH UNCHANGED REPORT UNDER THE CLOSABLE-ROTATION RULE.**
