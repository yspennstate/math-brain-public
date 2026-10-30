# POS3 fleet04/B20 r11 — ray-switch trichotomy and heavy-cover backtrack

**Outcome:** `ESSENTIAL_STEP_APPLIED`.

**Parent target:** POS3 remains **OPEN / NOT PROVED**. This report does not claim a full proof candidate.

**Execution status:** `WITHOUT_VERIFIED_BRAIN`.

## Scope

Target: every finite nonchain poset of width at most three should contain incomparable `x,y` with

`1/3 <= Pr(x<y) <= 2/3`

under the uniform law on all linear extensions.

This run attacks the current global recycler obstruction after the fixed-ray and local transposition mechanisms have already been controlled.

## Fresh source state consumed

1. **Team lead fleet04/B10 r17**: `proofnet24/collective-POS3/fleet04/B10/20260922T071036Z-B10-POS3-r17/REPORT.md`, source commit `732a848a9fa315f3907c654f0c54591dfe04535d`; shared handoff blob `f5a263be6f1255619bc09574c10833602f1b8b85`.
   - In the coherent heavy-cover gate, the surviving right branch gives a 3-antichain `{y,r_L,r_R}` with forced strong-majority order `y prec_* r_L prec_* r_R`.
   - The first unpaid universal step is global outward recycling / ray-switch accounting.

2. **Designated OTHER-account partner fleet01/B19 r13**: shared handoff `POS3-HANDOFF-fleet01-B19-20260922T054717Z.md`, blob `15bb349464fc92c3381abfef24c78f377ca18268`.
   - Exact-two four-pair windows have the conserved quantity `K` and a `3E/11` minority selector.
   - The first non-exact boundary defect remains a live obstruction.
   - Its inherited heavy-cover theorem says that a cover `u lessdot v` with an incomparable `z` satisfying `Pr(u<z<v)>1/3` cannot be a closed neutral object in a minimal no-balanced core; it must export at least two external relation channels or hit an accepted terminal exit.

3. **OTHER-account fleet02/B10 r11**: shared handoff blob `6971479872d6c25633d3e4beee71d9c3a7b925cd`.
   - For any strong incomparable pair, outgoing illegal transpositions have at most four Hasse-witness channels and one channel carries `>E/12` marks.
   - Its remaining named obstruction is `POS3-RAY-SWITCH-CHARGE-ACCOUNTING-v1`.

4. **OTHER-account fleet01/B10 r11**: shared handoff blob `b972080fb69669dcd68a40f1bab756e87b8a7ef6`.
   - On a fixed right ray, `Psi_R(p,q)=n*rho(q)+(rho(q)-rho(p))` strictly increases across all already-proved right-facing outward mechanisms unless an accepted target exit occurs.
   - Dually, `Psi_L(p,q)=n*(n-1-rho(p))+(rho(q)-rho(p))` controls a fixed left ray.
   - Hence the only remaining way to evade fixed-ray acyclicity is to switch rays or enter a mechanism outside that class.

Here `prec_*` is the strict `>2/3` majority order in a hypothetical no-balanced counterexample, and `rho` is its rank. Existing campaign work establishes that `prec_*` is a total order in that hypothetical state.

## Compact conditional end-to-end argument

Assume a cardinality-minimal POS3 counterexample with no balanced incomparable pair. Existing campaign results reduce every nonterminal heavy-cover episode to outward marked incomparable pairs. Fixed-ray chains are finite by `Psi_R/Psi_L`. Thus an infinite or cyclic recycler would need either infinitely many left/right ray switches among the four-channel transposition states, or infinitely many exits through the still-unpaid exact-two / non-crossed / multi-distinguisher mechanisms.

The theorem below eliminates the first alternative as a self-contained recycler: every genuine ray switch either gives strict span descent, expands the cumulative majority-order hull, or creates a heavy cover-gap of mass `>1/3`, which is already known to export. Therefore a surviving global recycler must repeatedly use one of the remaining non-transposition mechanisms. This reduces the open accounting problem to splicing those mechanisms to the exact-two conserved `K` / first-boundary-defect analysis.

## New theorem: ray-switch trichotomy

Let `(p,q)` be an outward transposition state with `p || q` and `p prec_* q`.

A **right outward transition** is `(p,q) -> (q,r)` coming from an outgoing Hasse witness with `p lessdot r`, `r || q`, and `q prec_* r`.

A **left outward transition** from `(q,r)` is `(q,r) -> (s,q)` with `s lessdot r`, `s || q`, and `s prec_* q`.

Consider two consecutive outward transitions that switch sides:

`(p,q) -> (q,r) -> (s,q)`.

Then exactly one of the following occurs.

### (A) Strict span descent

If `p prec_* s prec_* q`, then `(s,q)` is a strict `prec_*` subinterval of `(p,q)`, so `span_*(s,q) < span_*(p,q)`. This is an already-accepted strict majority-span-descent exit.

### (B) Cumulative hull expansion

If `s prec_* p`, then the cumulative strong-order hull of the endpoints seen by the recycler expands strictly to the left.

### (C) Exact two-step backtrack creates a heavy cover-gap

If `s=p`, then `p lessdot r`, `q || p,r`, and `p prec_* q prec_* r`.

Partition all `E=e(P)` linear extensions by the relative location of `q` with respect to the comparable cover `p<r`:

- `A = #{L : p<q<r}`,
- `B = #{L : p<r<q}`,
- `C = #{L : q<p<r}`.

These classes are disjoint and exhaustive, so `E=A+B+C`.

Because `p prec_* q`, the minority orientation is `q<p`, hence `C < E/3`. Because `q prec_* r`, the minority orientation is `r<q`, and under `p<r` this is exactly the class `p<r<q`, hence `B < E/3`. Therefore

`A = E-B-C > E/3`.

Thus `Pr(p<q<r) > 1/3`.

So the exact backtrack itself creates a heavy cover-gap on the cover `p lessdot r` with `q` incomparable to both endpoints. By the inherited heavy-cover theorem already used by the designated partner, this configuration cannot be a closed neutral recycler in the minimal no-balanced core: it exports at least two external relation channels or reaches an accepted terminal exit.

The left-then-right case is the order-dual statement.

## Corollary: outward transposition recycling is globally acyclic up to heavy-cover export

Track the cumulative hull `H_t=[min rho(v), max rho(v)]` over all endpoints encountered by an outward-transposition recycler.

At every genuine side switch, unless strict span descent or heavy-cover export occurs, the ray-switch trichotomy forces `H_t` to expand strictly by at least one rank.

Since the strong order has `n` vertices, the cumulative hull can expand at most `n-2` times from a nontrivial initial incomparable interval. Between side switches, fleet01/B10's fixed-ray potentials `Psi_R` and `Psi_L` strictly increase, hence fixed-ray motion is finite.

Therefore a recycler composed solely of the already-classified outward four-channel transposition moves plus the fixed-ray mechanisms **cannot cycle indefinitely** without producing one of:

- a balanced pair,
- strict strong-order span descent,
- a heavy cover-gap export,
- a proper autonomous/ordinal reduction or other previously accepted terminal exit.

Equivalently, any surviving nonterminal recycler must use a transition outside this transposition/fixed-ray graph, namely one of the still-live non-crossed staircase or exact-two / multi-distinguisher boundary mechanisms.

## Why this is a genuine new step

Earlier fleet04/B20 work proved only that incoming reverse-transposition cancellation cannot cycle on the same or a smaller majority interval. Fleet01/B10 then made fixed-ray outward chains acyclic. Neither statement controlled alternating left/right rays. The theorem here closes that gap for the entire four-channel transposition graph by showing that a side switch has only three outcomes: descent, hull expansion, or a new heavy cover-gap packet `>E/3`.

The exact-backtrack branch is the critical point: the apparent return does not actually return neutrally; it creates a target-scale middle-gap event.

## First unpaid implication after this run

The remaining obstruction is now the splice between this acyclic transposition graph and the partner's **first non-exact boundary defect / exact-two recurrence**.

A sufficient next lemma would be:

> Whenever a charged path exits the transposition graph through a non-crossed staircase or an exact-two/multi-distinguisher boundary mechanism and later re-enters the transposition graph, either (i) an accepted terminal exit occurs, (ii) the cumulative strong-order hull is strictly larger than at the preceding entry, or (iii) a target-scale exact charge is conserved in a bounded state variable compatible with the partner's `K` recurrence.

Proving that statement would combine the finite hull budget above with fixed-ray acyclicity and would leave no room for an unbounded mixed-mechanism recycler.

## Verification / computation

No finite enumeration or numerical search is used for the theorem in this report. The argument is analytic and consists only of the Hasse-witness transition definitions, the total strong-majority order, and the three-class partition `E=A+B+C` in the exact-backtrack case.

## Status and limitations

- Outcome: `ESSENTIAL_STEP_APPLIED`.
- POS3: **OPEN / NOT PROVED**.
- No claim that every mixed-mechanism recycler has yet been eliminated.
- No claim that the heavy-cover export by itself finishes the conjecture.
- No weakening of the `[1/3,2/3]` target.
- No benchmark/gold material, credentials, email/Drive data, paid/remote compute, workflow dispatch, or unrelated private data was used.
- Execution remained `WITHOUT_VERIFIED_BRAIN`.
