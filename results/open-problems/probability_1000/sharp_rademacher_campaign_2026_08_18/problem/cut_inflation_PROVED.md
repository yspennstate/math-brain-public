# The cut-inflation inequality, proved

Author: session 6c4d55a4, 2026-08-20. Supersedes the conjectural status in
`the_cut_inflation_conjecture.md`, which should be read for motivation and for the failed routes.
Every step below is machine-checked; the failure counts are stated with the successes.

**This does not prove the sharp Rademacher singularity conjecture.** It proves a Layer-II statement.
See the scope section.

## Theorem

For a graph `G` (loops dropped, parallel edges allowed) with `V` vertices, `E` edges and `b`
bipartite connected components,

    F(G) := SUM_{x in {+-1}^V} 2^{cut(x)}   <=   B(G) := 2^{E - V + 2b} 3^{V - b},

equivalently `Z(G) := F/(2^V (3/2)^E) <= (4/3)^{E-V+b}`. Equality holds exactly on forests.

## Proof

Induction on `E`.

**S1 Multiplicativity.** Cuts in different components are independent, so `F` multiplies over
components; `B` multiplies too, since `E`, `V` and `b` are all additive. So it suffices to treat one
component at a time, and disconnected intermediate graphs are fine.

**S0 Base.** `E = 0`: every vertex is its own bipartite component, `F = 2^V` and
`B = 2^{0-V+2V} 3^{V-V} = 2^V`. Equality.

**S2 Bridges.** Let `e` be a bridge joining `A` and `B`. For fixed configurations on `A` and `B`,
flipping all of `B` preserves both internal cut counts and toggles whether `e` is cut, so the pair
contributes `2^{cutA}2^{cutB}(2 + 1)`. Hence `F(G) = (3/2) F(A) F(B)`. And `B(G) = (3/2)B(A)B(B)`,
since `E` gains 1, `V` and the component structure combine, and `b(G) = 1` iff both are bipartite.
The same constant on both sides, so the bridge case follows from the two smaller graphs.
*Checked: 15,242 bridged graphs, `2F(G) = 3F(G-e)` exactly, 0 failures.*

**The recursion.** Splitting the sum on whether `e`'s endpoints agree,

    F(G) = 2 F(G-e) - F(G/e).

*Checked: 27,474 connected graphs, 0 mismatches.*

**The point.** `F(G/e)` enters with a MINUS sign, so no lower bound on it is needed beyond
`F >= 0`, which is immediate. What is needed is `2 B(G-e) <= B(G)`, and since deleting an edge drops
`E` by one, that holds **exactly when `b(G-e) = b(G)`** — i.e. when deleting `e` does not turn a
non-bipartite component bipartite. Call such an `e` *non-critical*.

**S5 `G` bipartite, bridgeless.** Delete any `e`. `G-e` is connected and still bipartite, so
`b` is unchanged and `B(G-e) = B(G)/2`. Then
`F(G) = 2F(G-e) - F(G/e) <= 2B(G-e) - 0 = B(G)`.

**S3 A non-critical edge exists.** Let `G` be connected, bridgeless, non-bipartite and not itself an
odd cycle. Bridgelessness makes `G-f` connected for every `f`, so only non-bipartiteness is at
issue. Take any odd cycle `C`. If `E > |C|`, pick `f` outside `C`: then `C` survives in `G-f`, which
is therefore non-bipartite. If `E = |C|`, then `C` already uses `|C|` edges and `|C|` vertices; any
vertex outside `C` would need further edges, so `V = |C| = E` and the connected graph `G` is exactly
`C` — excluded by hypothesis. QED.
*Checked: 11,851 such graphs, a non-critical edge found in every one, 0 failures.*

**S4 `G` non-bipartite, bridgeless, not an odd cycle.** Take the non-critical `f` from S3. Then
`b(G-f) = b(G)`, `B(G-f) = B(G)/2`, and the same two lines as S5 give `F(G) <= B(G)`.
*Checked, S4 and S5 together: 12,219 graphs, `2B(G-e) <= B(G)` for the chosen edge, 0 failures.*

**S6 `G` an odd cycle `C_m`.** Going around a cycle the number of sign changes is even, so
`F(C_m) = 2 SUM_{j even} C(m,j) 2^j = 3^m + (-1)^m`, which for odd `m` is `3^m - 1`. And
`B(C_m) = 2^{m-m+0} 3^{m-0} = 3^m`. So `F = B - 1 < B`. QED.
*Checked at m = 3,5,7,9,11.*

Every case is covered: bridges by S2, bipartite by S5, non-bipartite non-cycles by S3+S4, odd cycles
by S6, and the empty graph by S0. The induction is on `E` and every branch recurses to strictly
fewer edges. **QED.**

## Why the obvious version fails, and why that is the content

Handling an ARBITRARY edge does not work. If `e` is critical — `G` non-bipartite but `G-e`
bipartite — then `B(G-e) = (2/3)B(G)` and the step needs `F(G/e) >= B(G)/3`, which is false in
general: **470,797 of 634,291 critical instances fail it**, the worst at margin 0.318 on a
`V=7, E=13` graph whose contraction is `K_{3,3}`-like. The proof works only because the induction
gets to CHOOSE the edge, and S3 says a good one always exists.

This is worth recording because I spent real effort on the wrong version first, including testing
`2B(G-e) - B(G/e) <= B(G)`, which is a consistency property of `B` and not the induction step at all.

## Independent check of the theorem itself

Beyond the per-step checks: **every connected graph on up to 7 vertices — 1,893,730 of them —
verified in exact rational arithmetic, zero violations**, worst ratio exactly `1.000000000` attained
at a tree. Plus targeted families: odd cycles `C3..C13` (0.962963 rising to 0.999999, approaching 1
strictly from below), `K3..K8`, `K_{a,b}`, wheels, and dense random graphs at `V = 8..10` down to
ratio 0.000151.

## Consequence: Conjecture RC

With `c = log2 Z(G)` (proved in `the_fibre_is_an_ising_partition_function.md`) and the pair-sum
residual family giving `d_cb <= |V| - b`, RC — `c <= beta(k - d_cb)` — follows for every linear NAE
triangle system.

**The caveat, stated plainly.** The inequality above is proved unconditionally. The step from it to
RC uses a `d_cb` bound from an explicit residual construction, which has now been measured against
the campaign's own `valid_R` — see the next section for what that showed, including a correction to
my own construction. Summary: the graph inequality is a theorem; the `d_cb` bound is verified on 189
systems with no surviving counterexample, but is not proved in general.

## The d_cb side, measured against the campaign's own valid_R

The step from the inequality to RC needs `d_cb <= dim span{one pair-sum per triangle}`, and that is
only a bound if the space is ADMISSIBLE under the campaign's `valid_R`. I had called this blocked
because `fast_dcb` enumerates `C(|cand|, d)` subspaces and never terminates. That framing was wrong:
checking one candidate space is a single `valid_R` call, not a search.

Measured:

- **Structured systems (9): valid_R True on every one** - cycles m = 3..6, paths of 2..4 triangles,
  and the K_{n,n} sharing graphs including K_{3,3} at r = 15, |A| = 2754. `dim R` equals `|V| - b`
  exactly on the cycles and on K_{n,n}.
- **Random systems (240, two seeds): 239 admissible, ONE failure.** The failure was in my SELECTION
  RULE, not the family. `pairsum_space` always takes each triangle's SHARED pair; on
  `((0,1,6),(0,2,4),(0,3,7),(1,2,7),(5,6,7),(1,3,4))` that specific choice is one of only 4
  inadmissible choices out of 729, and the minimum admissible dimension is 5 - the same dimension.
  RC holds there with room (5 against an allowance of 7.45). That system also has `|D| = 30` rather
  than `r + k = 14`, so it sits outside the campaign's P6.
- **With the pair CHOSEN rather than fixed (180 systems, three seeds): 0 systems with no admissible
  choice, 0 where the shared-pair rule failed, 0 where RC is at risk.** Tightest slack exactly
  0.0000 - minimum admissible dim 3 against an allowance of exactly 3.0000, on disjoint-triple
  systems, which is the campaign's own P2/P3 equality family.

**So the corrected statement is: the residual pair must be CHOSEN, not fixed to the shared pair.**
With that, no counterexample survives in 189 systems.

**NOW PROVED, on the |D| = r+k regime.** Let `R` be the span of one chosen pair-sum per triangle.

  M1. `f_t = e_a + e_b + e_c` and `v_t = e_a + e_b` lies in `R`, so `f_t == e_c mod R`: every
      leftover form lands in the class of a COORDINATE form.
  M2. Coordinate forms merge along the chosen-pair graph `H` (`e_a == -e_b` per chosen pair); a
      bipartite component of `H` gives one class, a non-bipartite one forces `e == -e`, i.e. `e` in
      `R`, so those coordinates fall into the zero class. Either way every class contains at least
      one coordinate form.
  M3. Hence `#classes <= r`, and picking one COORDINATE form per class gives distinct coordinate
      forms, which are automatically linearly independent. `valid_R`'s transversal exists. QED

The argument needs `D = {coordinate forms} u {f_t}`, i.e. `|D| = r + k`; otherwise a class can
consist only of extra dual forms with no coordinate to pick.

**Measured, and the mechanism confirmed rather than just the conclusion.** Over 300 systems:

    |D| = r+k   valid_R TRUE   243        |D| > r+k   valid_R TRUE   56
    |D| = r+k   valid_R FALSE    0        |D| > r+k   valid_R FALSE   1

**The cell that would refute the argument - `|D| = r+k` with `valid_R` false - is empty.** And on a
further 240 systems, tracking M2 and M3 directly:

    |D| = r+k :  M2 True, M3 True, valid_R True   196 of 196, no other combination
    |D| > r+k :  M2 False in 20 cases              - exactly the predicted failure mode

**A scope note on P6, not a correction to it.** The campaign's `WHAT_STANDS` table lists P6 as
`|D| = r+k`. Its source (`why_ceil_k_over_two.md` §9) derives `|D| = 3k+1` with `r = 2k+1`, i.e. for
TRIANGLE-TREES, where `3k+1 = r+k` holds. So P6 is right in its stated setting; the table's
compression reads more generally than the derivation supports. Measured on general linear systems,
`|D| = r+k` fails about 19% of the time (29/150 and 28/150 on two seeds). Worth fixing in the table.

**Consequence.** RC is proved for every linear NAE triangle system with `|D| = r + k` - which
includes every triangle-tree by P6's own derivation. Outside that regime the d_cb bound held on
every system tested but is not proved.

**The other regime needs no new machinery, and may need nothing at all.** RC is
`c <= beta(k - d_cb)`, and the campaign has PROVED `d_cb <= k`, so ANY system with `c <= 0`
satisfies RC outright - no step-3 argument required. And there is a structural reason to expect
`c <= 0` exactly where `|D| > r+k`: `|D|` counts linear forms that are +-1-valued on the fibre, so
extra forms appear when `A` is SMALL, while `c > 0` requires `|A| > 2^r (3/4)^k`, a LARGE fibre. The
two pull in opposite directions.

Measured over 596 random linear systems, three seeds:

    |D| = r+k  (proved regime) : 416 systems, 28 with c > 0   <- RC has content, the chain applies
    |D| > r+k  (outside)       : 149 systems,  0 with c > 0   <- RC follows from d_cb <= k

**No system outside the regime had `c > 0`**, largest observed there `c/beta = -0.409`. So RC held
on every one of the 596, by one route or the other.

**What is still not proved:** that `|D| > r + k` forces `c <= 0` (149/149, unproven), and,
independently, that some pair-choice is always admissible when `|D| > r + k`. Either one closes the
last regime; neither is needed inside it. The structure is favourable -
with `R` spanned by the chosen pair-sums, each `f_t` reduces to `+-e` of its third coordinate, so
every leftover form joins an existing coordinate class and the class count is automatically at most
`r`; what needs an argument is the independent transversal. That is a statement about `valid_R` and
is the one remaining link in the chain.

## Scope

Nothing here touches `ell = 1`, where `STATE_OF_THE_PROOF.md` §1 locates the sharp Rademacher
conjecture's actual difficulty. RC is a Layer-II statement about selector distances on triangle
systems. The conjecture remains OPEN.

## Verification record

<box> `/tmp`, read-only, nice -n 15: `proof_steps_check.py` (S0/S2/S3/S4/S5/S6),
`rc_graph_inequality.py` (exhaustive V<=7), `one_case_left.py` (the 470,797 critical-edge failures),
`deletion_contraction.py` (the recursion), `targeted_ineq.py` (extremal families),
`two_sided.py` (the failed lower-bound routes).
