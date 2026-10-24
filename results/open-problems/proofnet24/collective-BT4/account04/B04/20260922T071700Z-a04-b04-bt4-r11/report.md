# account04/B04 BT4 proof attempt — 2026-09-22T071700Z

**Outcome:** `ESSENTIAL_STEP_APPLIED`

**New result:** `BT4-F3-R3-SLACKONE-LADDER-v1`

**Target.** The k=4 Bermond–Thomassen conjecture in the full finite digraph scope of the collective order: loopless, at most one arc per ordered vertex pair, digons allowed in the statement, and minimum outdegree at least seven.

**Execution context.** `WITHOUT_VERIFIED_BRAIN`. No brain-installation or benchmark work was performed. No mathematical computation was used in this run; the new step is combinatorial. No paid/remote model, API, workflow dispatch, email or Drive access was used.

## 1. Source boundary and exact dependencies

Fresh control was resolved on `yspennstate/math-research-brain` before work. Active control revision was `2026-09-22.2`, directive `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`; B04 remained assigned to BT4 structural case splitting and no B04 stop/pause was present.

The controlling complete team-lead source read in this run was:

- account02/B04, `BT4-CROSS-ROW-COMPRESSION-v1`, scientific report
  `proofnet24/collective-BT4/account02/B04/20260922T0619Z-b04-bt4-r11/report.md`, commit `14b8affcde6130bdbacbdfbd03888816b96d61ef`, plus the source-bound handoff `scheduled_tasks/work/shared/collective-open-problems-2026-09-22/BT4-HANDOFF-account02-B04-20260922T0619Z.md`.

The required named OTHER-account partner result actually applied is:

- account01/B05, `BT4-F3-RETURN-RESTART-v1`, source-bound handoff `scheduled_tasks/work/shared/collective-open-problems-2026-09-22/BT4-HANDOFF-account01-B05-20260922T0640Z.md`.

The handoff advertises a canonical account01/B05 scientific report/commit, but the authorized scientific repository lookup for that advertised ref/path returned not-found in this run. I therefore use the shared source-bound handoff as the admissible partner source and do not pretend that the advertised canonical report was independently read.

Secondary source applied below:

- account02/B20, `BT4-OPPOSITE-INTERSECTION-BYPASS-v1`, source-bound handoff `BT4-HANDOFF-account02-B20-20260922T065811Z-r16.md`.

The team-lead and partner results use the standard minimal-counterexample consequences already established in their source chain: an oriented 3-vertex-strong minimal counterexample, arc domination, the k=3 theorem at minimum outdegree five, and a globally minimum-total-order three-cycle packing. I do not re-prove those dependencies here.

## 2. Point of entry from account01/B05

Use the partner's `BT4-F3-RETURN-RESTART-v1` after its return-cycle construction in the triangular F3 both-repeat branch. The partner obtains three pairwise disjoint directed cycles

\[
 H,\quad C,\quad T_c
\]

whose complement is an acyclic three-vertex remainder

\[
 R'=\{a,b,t\},
\]

with `t` a sink of `D[R']`. The current three-cycle packing has total packed order `n-3`, while the canonical globally minimum three-packing in this exact-R4 frontier has total order `n-4`.

Unless the SIX branch already occurs, the sink fan of `t` into `(H,C,T_c)` is `(3,2,2)`. Denote the three-fan support by `J` (heavy) and the other two supports by `L,M` (light). The partner closes/restarts several short-heavy return cases but leaves the long-heavy R3 sink configuration as a live structural debt.

The goal here is to classify all possible packed returns to `t` in that debt.

## 3. Slack-one inport collar

### Lemma 3.1 (slack-one collar)

Let `T` be one of the three currently packed directed cycles in the `n-3` packing. Suppose

\[
 c\to t,\qquad t\to y,
\]

with `c,y in V(T)`. Write `d_T(c,y)` for the forward directed distance from `c` to `y` along `T`. Then

\[
 d_T(c,y)\le 3.
\]

Moreover, if `d_T(c,y)=3`, replacing `T` by

\[
 T' = c\to t\to y\to T[y,c]
\]

produces a three-cycle packing of total order exactly `n-4`. Its four-vertex complement either contains a directed cycle, immediately giving four disjoint cycles, or is acyclic and is an exact-R4 restart state.

### Proof

The replacement cycle has

\[
 |T'|=|T|-d_T(c,y)+2.
\]

Hence the new total packed order is

\[
 (n-3)-|T|+|T'|=n-1-d_T(c,y).
\]

By global minimum of the canonical three-packing, every three-cycle packing has total order at least `n-4`. Thus

\[
 n-1-d_T(c,y)\ge n-4,
\]

so `d_T(c,y)<=3`. Equality `d=3` gives packed order `n-4`, and the complement has four vertices. If that complement is cyclic its directed cycle is disjoint from the three packed cycles; otherwise the exchanged packing is another exact-R4 canonical state. QED.

### Corollary 3.2 (no-restart collar)

In a branch in which neither a four-pack nor an exact-R4 restart occurs, every target of `t` on a packed support `T` having an inport `c->t` lies among

\[
 \{c^+,c^{++}\}.
\]

The point `c` itself cannot be a target because the minimal counterexample is oriented.

## 4. Return-port classification

Assume from now on that neither a four-pack, SIX, nor an exact-R4 restart has occurred.

### Lemma 4.1 (heavy support cannot return)

There is no arc `J -> t`.

### Proof

If `c->t` with `c in J`, Corollary 3.2 says all three distinct `t`-targets on `J` lie in the two-vertex set `{c^+,c^{++}}`, impossible. QED.

### Lemma 4.2 (each light support has a unique possible return port)

If `c->t` for `c in L`, then

\[
 N^+(t)\cap L=\{c^+,c^{++}\}.
\]

Consequently `L` contains at most one vertex sending to `t`; the same holds for `M`.

### Proof

The light fan has exactly two distinct targets. Corollary 3.2 leaves exactly the two stated successors. That ordered consecutive pair determines its predecessor `c` uniquely on a directed cycle of length at least three. QED.

### Lemma 4.3 (at least one light return)

At least one of `L,M` sends an arc to `t`.

### Proof

Three-vertex-strongness gives `d^-(t)>=3`. At most two in-neighbors of `t` lie in `R'-{t}`; Lemma 4.1 forbids a heavy in-neighbor. Hence at least one packed in-neighbor lies on a light support. QED.

Thus the surviving R3 sink is already reduced to one or two uniquely located light return ports, with no heavy return.

## 5. Arc-domination ladder

Fix a light return port `c in L` with `c->t`. Repeatedly apply the inherited arc-domination property to the current arc into `t`.

Choose `z_1` dominating `c->t`, so

\[
 z_1\to c,t.
\]

If `z_1` is residual, choose `z_2` dominating `z_1->t`, and continue. There are only two residual vertices other than `t`. Because the digraph is oriented, a residual vertex cannot recur as the next dominator in a way that creates a reverse arc to the preceding step. Hence after at most two residual vertices the ladder reaches a packed in-neighbor `e->t`.

By Lemmas 4.1–4.2, `e` is either the unique return port `c` on `L`, or the unique return port on the other light support `M`.

### Lemma 5.1 (self-ladder forces a light triangle)

If the domination ladder starting from `c->t` first returns to the same packed support `L`, then its packed apex is `c` and both residual vertices occur. After relabeling them `z_1,z_2`,

\[
 c\to z_2\to z_1\to c
\]

is a directed triangle and

\[
 c,z_1,z_2\to t.
\]

The returning light support has `|L|=3` unless an exact-R4 restart/four-pack already occurs.

### Proof

Uniqueness of the L-return port forces the packed apex to be `c`. A one-residual closure would give both `c->z_1` and `z_1->c`, impossible in the oriented minimal counterexample, so both residual vertices occur and form the displayed triangle `Q`.

Replace `L` by `Q`. The total packed order becomes

\[
 (n-3)-|L|+3=n-|L|.
\]

Global minimality `n-|L| >= n-4` gives `|L|<=4`. If `|L|=4`, the replacement has exact minimum total `n-4`, hence gives a four-pack if its complement is cyclic and an exact-R4 restart otherwise. Excluding those outcomes leaves `|L|<=3`; oriented directed cycles have length at least three, so `|L|=3`. QED.

### Corollary 5.2 (self-ladder triple-hit witness)

In the self-ladder leaf, let

\[
 Q=c\to z_2\to z_1\to c.
\]

Some vertex outside `Q` sends arcs to all three vertices of `Q`.

### Proof

If every outside vertex sent at most two arcs into `Q`, then deleting `Q` would leave minimum outdegree at least `7-2=5`. The established k=3 Bermond–Thomassen theorem would give three disjoint directed cycles in `D-Q`, and together with `Q` this would be a four-pack. QED.

This witness cannot be `t` (the remainder sink has no arcs to `z_1,z_2`, and `c->t`). If it lies on the returning triangle `L`, it must be `c^-` and therefore gives a packed-to-two-residual fork; otherwise it lies on one of the other packed supports and gives an external three-hit interface to `Q`.

### Lemma 5.3 (two-light swap ladder)

Suppose the ladder from `c in L` reaches a return port `e in M`. It yields a directed `M->L` path from `e` to `c` whose internal vertices lie in `{a,b}`. Run the domination ladder again from `e->t`.

Either:

1. it self-closes at `e`, in which case Lemma 5.1 forces `M` to be a directed triangle (unless restart/four-pack); or
2. it reaches `c`, yielding an opposite directed `L->M` path, again with all internal vertices in `{a,b}`.

In case 2, if the two opposite paths meet internally, account02/B20's `BT4-OPPOSITE-INTERSECTION-BYPASS-v1` converts their first intersection into a same-support bypass. If they are internally disjoint, their union is a simple directed mixed cycle of order three or four (order two is excluded by orientedness).

### Proof

After `e` is known to be the M-return port, Lemmas 4.1–4.2 leave only `e` and `c` as possible packed terminals of the second ladder. Self-termination is Lemma 5.1. Otherwise the terminal is `c`. The path statements follow directly from the domination chain. The intersection/bypass conclusion is exactly the cited B20 trimming lemma; if internally disjoint, concatenating the opposite paths yields a simple directed cycle, and there are only two possible internal residual vertices. QED.

## 6. Same-support bypass tax in the slack-one state

If an opposite-path intersection produces a same-support bypass of arc length `ell` replacing a forward support interval of length `d`, then replacing that interval changes the current `n-3` total by `ell-d`. Global minimum therefore gives

\[
 n-3+\ell-d\ge n-4,
\]

or

\[
 \ell-d\ge -1.
\]

Equality is an exact `n-4` exchange and therefore a four-pack or exact-R4 restart. Consequently, in the surviving no-restart branch,

\[
 \ell\ge d.
\]

Thus every bypass generated by the ladder is neutral-or-long; this lands directly in the team lead's current CROSS/BYPASS splice wall rather than introducing a new unpriced shortcut.

## 7. Exact structural split obtained

The account01/B05 R3 sink debt now has the following exhaustive split after excluding SIX:

**R3-A — restart/four-pack.** Some packed inport `c->t` has a t-target at forward distance three. The slack-one exchange is exact `n-4`, yielding either an immediate fourth cycle or an exact-R4 restart. In particular, every heavy-support inport lands here.

**R3-B — single-light self ladder.** The heavy support has no return; exactly one light support returns. The domination ladder must self-close, the returning light support is a directed triangle, both residual vertices occur in the domination triangle, and that triangle has an external three-hit witness.

**R3-C — dual-light with a self ladder.** Both light supports have unique return ports, and one domination ladder self-closes. The corresponding light support is a directed triangle, with the same three-hit-witness conclusion.

**R3-D — dual-light swap.** Both light supports have unique return ports and neither ladder self-closes. There are opposite light-to-light directed paths with interiors in the two residual vertices. Internal intersection gives a same-support bypass subject to the neutral-or-long tax; internal disjointness gives a 3/4-vertex mixed directed cycle through the two return ports.

No heavy return survives outside R3-A.

## 8. Compact conditional end-to-end argument

The partner's F3 return theorem reduces its unresolved `|U|=3` state to the R3 sink described above. The slack-one collar either returns immediately to the canonical exact-R4 engine (R3-A) or reduces every packed return to the rank-one light-port geometry R3-B/C/D. In R3-D the B20 intersection theorem feeds any intersecting opposite pair into the lead's same-support bypass wall; otherwise the entire reciprocal interface is a single 3/4-cycle using only the two light ports and at most two residual vertices. In R3-B/C the only self-return support is a triangle and carries a forced external three-hit witness.

Therefore the first genuinely unpaid implication on this branch is now:

`BT4-F3-R3-LIGHT-RANKONE-SPLICE-v1` — In R3-B/C/D, combine the triangular three-hit interface or the reciprocal rank-one light interface with the team lead's fresh-reverse/third-support and 2x2 cyclic-order machinery to force one of: a legal two-cycle replacement, a strict packed-order decrease, an exact-R4 restart, SIX, or four disjoint directed cycles.

A natural next move in R3-D is to delete the two light return ports and invoke 3-vertex-strongness: the account03/B05 fresh-reverse theorem then forces either a connector with fresh endpoints or mediation through the third packed support. That connector can be paired with the existing opposite rank-one interface and tested against the lead/B20 2x2 cyclic matching wall. I do **not** claim this final splice here.

## 9. What this does and does not close

This result closes the *return-port classification* of the partner's F3 R3 sink debt. It does not prove BT4. Separate debts in the shared tree remain, including the final rank-one splice above and the team lead's other explicit branches (including SIX and other non-F3 leaves). No cross edge, neutral exchange, witness count, or restart label is promoted to a fourth cycle without the corresponding construction.

## 10. Failure / verification log

- The account01/B05 shared handoff was read and applied. Its advertised canonical scientific report/ref was not retrievable through the authorized scientific repository in this run; no unverified content beyond the handoff was used.
- No brute-force or symbolic code was used; therefore there is no computational output to promote.
- The current public literature status was checked against Bessy–Muis–Sereni–Steiner–Wiederrecht, arXiv:2608.12948 (submitted 2026-08-13), which states that the exact Bermond–Thomassen conjecture remains unresolved for all `k>=4` and proves a one-reversed-arc relaxation instead. This is status context only, not a novelty proof for the lemma above.
- No authenticated brain retrieval was used: `WITHOUT_VERIFIED_BRAIN`.

## 11. Model/provider accounting

- Model self-report: `GPT-5.6 Sol`.
- Requested reasoning effort: maximum actually supported in the active runtime.
- Configured reasoning effort: `UNKNOWN` (no genuine selector/value exposed to this worker).
- Provider reasoning-token counter: `NOT_EXPOSED`, not zero.
- Provider thinking-time counter: `NOT_EXPOSED`, not zero.
- Elapsed execution is recorded separately in the immutable run receipt/finish; it includes tool/network/serialization overhead and is not pure thinking time.

## 12. Privacy / provenance review

Only scoped mathematical source paths, public literature metadata, account/slot labels and repository commit identities needed for provenance are included. No credentials, machine paths, scheduler identifiers, benchmark gold, unrelated private material, email/Drive content, or private transcripts are present.
