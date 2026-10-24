Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime model/effort telemetry or binding selector is exposed.

# P0029 — exact root-pinned independent-set formula for the two-peak pair law

## 1. Source and purpose

Target: Krzysztof Burdzy, *My favorite open problems*, Problem 9, “Do peaks of random labelings repell each other?”  For a uniformly random labeling of the `n x n` discrete square conditioned on exactly two peaks, with `rho_n` their graph distance, the source asks whether `rho_n/n -> 0` in distribution.

This artifact gives a new exact reduction for the **actual** two-peak pair law on an arbitrary finite connected graph.  It removes the polynomial rank-2 promotion loss from the preceding R7-04 report and replaces the problem by the spatial asymptotics of a positive two-point quantity obtained from an alternating independent-set expansion.

The mechanism is a root-pinned specialization of the inclusion-exclusion method in:

Prarthana Agrawal, Abdurrahman Hadi Erturk, Ard Louis, *Successive vertex orderings of connected graphs*, arXiv:2604.07408 (2026).

That paper gives an exact independent-set formula for successive vertex orderings and a generating polynomial whose derivatives count failures of the successive condition.  The root-pinned exactly-one-additional-peak formula below is derived explicitly here because it is the object needed for Burdzy's conditioned two-peak law.  No novelty claim is made without a complete citation search.

## 2. Descending orders and bad events

Let `G=(V,E)` be a finite connected graph with `|V|=N`.  A labeling is equivalently a descending-label order

`pi=(v_1,...,v_N)`.

A vertex is a peak exactly when it has no neighbour before it in this descending order.  Hence peaks are precisely the vertices violating the successive-ordering condition.

For `x in V`, let `N(x)` be its open neighbourhood and `N[x]={x} union N(x)` its closed neighbourhood.  For a set `I`, write `N[I]=union_{x in I} N[x]`.

For every independent set `I`, define

`b(empty)=1`,

and, for `I != empty`,

`b(I) = (1/|N[I]|) sum_{x in I} b(I\{x}).`                 (2.1)

This is the same recursive weight appearing in Agrawal--Erturk--Louis.

### Lemma 2.1 — relative-order interpretation of b(I)

Let `I` be independent.  In a uniformly random permutation of a vertex set containing `N[I]` (with any number of extra vertices outside `N[I]`), let `E_I` be the event that every `x in I` occurs before every neighbour of `x`.  Then

`P(E_I)=b(I).`                                             (2.2)

**Proof.**  The earliest vertex of `N[I]` is uniform on `N[I]`.  On `E_I` it must belong to `I`, since if a neighbour of some `x in I` were earliest then that `x` would fail.  Condition on the earliest vertex being `x in I`.  Because `I` is independent, deleting `x` leaves exactly the same precedence constraints for `I\{x}`; moreover the remaining relative order is uniform.  Therefore

`P(E_I)=sum_{x in I} (1/|N[I]|) P(E_{I\{x}})`,

which is (2.1), with the empty-set base case.  Extra vertices outside `N[I]` do not affect the relative order inside any closed neighbourhood.  QED.

## 3. Root-pinned exactly-one-defect theorem

Fix a vertex `r` and condition that `r` is first in the descending order, i.e. `r` is the highest peak.  The remaining `N-1` vertices are uniformly permuted.

A vertex `x != r` can be another peak only if `x` is **not adjacent** to `r`.  Define the candidate set

`U_r := V \ N[r]`.

For `x in U_r`, let `B_x` be the event that `x` precedes all its neighbours in the relative order of `V\{r}`.  Then `B_x` is exactly the event that `x` is an additional peak.

For an independent set `I subset U_r`, the root `r` lies outside `N[I]`, so Lemma 2.1 gives

`P(intersection_{x in I} B_x | r first)=b(I).`             (3.1)

If `I` is not independent the intersection is empty, because two adjacent vertices cannot each precede the other.

For nonadjacent `r,v`, let `W(r,v)` be the number of full descending orders having exactly two peaks, with highest peak `r` and the other peak `v`.

### Theorem 3.1 — exact ordered two-peak pair weight

For every nonadjacent ordered pair `(r,v)`,

`W(r,v) = (N-1)! C(r,v)`,                                  (3.2)

where

`C(r,v) := sum_{I independent, I subset U_r, v in I}
              (-1)^(|I|-1) b(I).`                          (3.3)

In particular `C(r,v)>=0`, because it is a probability.

**Proof.**  Condition on `r` being first.  Exactly one additional peak, namely `v`, means

`B_v intersect intersection_{x in U_r\{v}} complement(B_x)`.

Apply inclusion-exclusion to the complement events.  A term indexed by `J subset U_r\{v}` is

`(-1)^|J| P(B_v intersect intersection_{x in J} B_x)`.

It vanishes unless `I=J union {v}` is independent.  In the independent case, (3.1) gives probability `b(I)`.  Reindexing by `I` yields (3.3).  There are `(N-1)!` equally likely relative orders after fixing `r` first, proving (3.2).  QED.

### Corollary 3.2 — exact conditioned pair law

Every exactly-two-peak labeling has a unique highest peak `r` and a unique second peak `v`.  Therefore

`P((r,v) is the ordered peak pair | exactly two peaks)
   = C(r,v) / sum_{a,b: a not~ b, a!=b} C(a,b).`            (3.4)

For any symmetric observable `phi(r,v)`, in particular graph distance,

`E[phi(r,v) | exactly two peaks]
 = [sum_{r,v} phi(r,v) C(r,v)]/[sum_{r,v} C(r,v)].`         (3.5)

Thus for the `n x n` square,

`E[rho_n/n | exactly two peaks]
 = [sum_{r,v} d(r,v) C_n(r,v)]
   / [n sum_{r,v} C_n(r,v)].`                               (3.6)

This is an exact formula for the frozen R7-04 metric sequence, not a rank-2 approximation.

## 4. Pinned polynomial and two-point correlation language

Define the multivariate root-pinned polynomial

`Z_r(z) := sum_{I independent, I subset U_r}
              (-1)^|I| b(I) prod_{x in I} z_x.`             (4.1)

Then Theorem 3.1 is equivalently

`C(r,v) = - partial_{z_v} Z_r(z)|_{z=1}.`                   (4.2)

The total probability of exactly one extra peak after pinning `r` is

`sum_{v in U_r} C(r,v).`                                   (4.3)

Hence P0029 becomes a spatial two-point problem for the positive kernel `C_n(r,v)`, despite its sign-alternating representation.  The exact source question is now whether the normalized mass of this kernel concentrates on `d(r,v)=o(n)`.

This is a materially sharper object than the preceding report's rank-2 law `Q_n`, because no `n^2` promotion distortion remains.

## 5. Exact rank-2 formula as a companion identity

The previous report used `F({r,v})`, the number of completions when nonadjacent `r,v` occupy the first two descending positions and every later vertex has an earlier neighbour.

Condition on those first two positions.  An additional peak can only lie outside `N[r] union N[v]`.  Applying the same inclusion-exclusion argument gives

`F({r,v})/(N-2)!
 = sum_{I independent, I cap (N[r] union N[v]) = empty}
      (-1)^|I| b(I).`                                      (5.1)

Thus both the actual pair weight `W` and the rank-2 weight `F` use the same graph-local coefficients `b(I)`.  Their difference is no longer mysterious: they are two different evaluations/derivatives of the same independent-set expansion.

## 6. B3 outcome — stronger exact statement

The attempted stronger theorem was not an asymptotic bound but an exact formula for the **true** pair law.  Theorem 3.1 succeeds and strictly improves the previous polynomial-comparison reduction:

- before: true pair weights controlled only up to a factor `N-1` by `F({r,v})`;
- now: true ordered pair weights are exactly `(N-1)! C(r,v)`.

What remains is asymptotic control of the spatial profile of `C_n(r,v)`, not the second-birth rank.

## 7. B7 outcome — take the limit after exposing the right finite-volume object

The natural finite-volume object for any limiting argument is now the pinned correlation kernel `C_n(r,v)` from (3.3)/(4.2), rather than `log F({r,v})` alone.  A possible bulk scaling question is whether, after placing `r` a macroscopic distance from the boundary, the normalized measure

`mu_{n,r}(v) := C_n(r,v) / sum_w C_n(r,w)`

has a nontrivial scaling limit under `v -> v/n`.

The obstruction is explicit: (3.3) is an alternating independent-set series with substantial cancellation.  Crude termwise bounds on `b(I)` destroy the positivity that is present only after summation.  A successful limit theorem therefore needs a correlation/cluster representation, a cancellation-preserving comparison, or another positive probabilistic representation of `C`.

No such asymptotic theorem is claimed here.

## 8. B24 outcome — exact finite extremal/certificate data through 5x5

The new formula enables exact computation by enumerating independent sets rather than all vertex subsets.  On the `n x n` square the numbers of independent sets are

- `n=2`: 7,
- `n=3`: 63,
- `n=4`: 1234,
- `n=5`: 55447.

The exact checker computes all `b(I)` with rational arithmetic, all ordered `W(r,v)`, and all rank-2 `F({r,v})`.  For `n<=4`, an independent implementation of the older prefix/completion subset DP is run and asserted pair-by-pair equal to the new formula.

All crosschecks pass.

### Exact exactly-two-peak totals

- `2x2`: `8`
- `3x3`: `143808`
- `4x4`: `779299174080`
- `5x5`: `7063261481362958280000`

### Exact conditional normalized mean distances

- `2x2`: `1`
- `3x3`: `666/749 ~= 0.889185580774366`
- `4x4`: `377754599/463868556 ~= 0.814356985645735`
- `5x5`: `5689414559220285956/7357564043086414875 ~= 0.773274214930740`

The `5x5` value is new finite evidence only.  The monotone decrease from `n=2` to `5` does not decide the limit.

### Exact 5x5 distance distribution

For exactly two peaks:

- `d=2`: `759127145926367076000`
- `d=3`: `2034099833145681772800`
- `d=4`: `2315729092924013995200`
- `d=5`: `1393059798442968360000`
- `d=6`: `473582366731277968800`
- `d=7`: `82379424872165332800`
- `d=8`: `5283819320483774400`

So, for example,

`P(d>=3 | two peaks) = 525344527953049267/588605123446913190 ~= 0.89252456`,

`P(d>=4 | two peaks) = 1779181042621212263/2943025617234565950 ~= 0.60454147`,

`P(d>=5 | two peaks) = 54286261371302651/196201707815637730 ~= 0.27668598`.

Again these are finite certificates, not an asymptotic refutation.

### Promotion tilt is not radial

For the unordered actual weight `H({r,v})=W(r,v)+W(v,r)`, the ratio `H/(2F)` on `5x5` ranges exactly from

`10015190708869/6016139663276 ~= 1.664720446901224`

to

`55946653552157/13713733608932 ~= 4.079607723728711`.

Pair extrema are affected strongly by boundary geometry; actual weights are not simply monotone in graph distance.  Any asymptotic proof should therefore separate a bulk region from boundary corrections before attempting a radial comparison.

## 9. Exact checker

Executed exact-arithmetic artifacts:

- `research7_2026-09-17/R7-04/artifacts/2026-09-18/2026-09-18T200317Z__P0029_pinned_independent_set_check.py`
- `research7_2026-09-17/R7-04/artifacts/2026-09-18/2026-09-18T200317Z__P0029_pinned_independent_set_check.out`

The output terminates with `ALL_EXACT_CHECKS_PASS`.

The checker uses only Python arbitrary-precision integers and `fractions.Fraction`; no randomness or floating-point arithmetic enters any asserted identity.  Decimal displays are derived only after the exact fractions are established.

## 10. What this does and does not settle

This run proves an exact arbitrary-graph formula for the actual conditioned pair law and extends exact square certificates through `5x5`.  It does **not** prove whether `rho_n/n -> 0` on the square.  The admission-fixed source metric

`D_* = limsup_n E[rho_n/n | exactly two peaks]`

therefore remains `UNKNOWN/UNMEASURED`.

The exact remaining mathematical obstacle can now be stated without the previous rank-2 surrogate:

> Control the spatial scale of the positive kernel `C_n(r,v)` in (3.3), despite its cancellation-heavy independent-set expansion, strongly enough to decide whether its mass is asymptotically concentrated in `d(r,v)=o(n)`.

That is the object the mandatory next-run stuck diagnosis should analyze.
