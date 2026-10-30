# POS3 fleet04/B11 — the bounded-range exception is infinite even at pi=7

**Outcome:** `CANDIDATE_REFUTED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose uniform-linear-extension ordering probability lies in `[1/3,2/3]`.  
**Parent status after this report:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

The candidate refuted here is **not POS3**.  It is the tempting finite-kernel implication from the bounded-range/high-comparability regime after the actual bounded-width theorem and the collective minimal-counterexample reductions.  The new family below shows that even the first unresolved range value `pi(P)=7`, connected incomparability, module-primality, width exactly three, uniformly bounded rank variance, and uniformly bounded one-element insertion fibers allow arbitrarily large order.  Therefore the exceptional regime cannot be discharged by a finite census unless one proves an additional genuinely no-balanced-specific reduction.

## 1. Exact state and named peer applied

The current owner-selected scope is width at most three under the **uniform** law on all linear extensions.  I used the following exact completed collective inputs.

1. **Assigned partner, fleet01/B19:** `proofnet24/collective-POS3/fleet01/B19/20260922T004631Z-b19-pos3-r11/REPORT.md`.  It gives the exact arbitrary-chain insertion weight `W_C(tau)`, the dual interval recurrence, the exact short-gap defect for endpoint-ordered adjacent swaps, and proves that only nested chain profiles can have context-dependent swap sign.  It also refutes a universal arbitrary-chain `|Delta W|<=1` bound.
2. **fleet03/B11:** `proofnet24/collective-POS3/fleet03/B11/20260922T003936Z-fleet03-B11-pos3-r11/REPORT.md`.  In a hypothetical counterexample every adjacent incomparable boundary in the transitive strong-majority order has a double-blocker certificate; a purely local mixed-blocker closure is false.
3. **This slot's preceding report:** `proofnet24/collective-POS3/fleet04/B11/B11-20260922T001443Z-pos3-r1/REPORT.md`.  It proves the explicit canonical-rank atom `>16/6561`, the endpoint atom `>8/27`, the one-element mean-insertion bound, and already warns that bounded incomparability range alone is not a finite kernel.
4. **fleet03/B10:** `proofnet24/collective-POS3/fleet03/B10/fleet03-B10-20260922T001407Z-pos3-r11/REPORT.md`.  It pins the bounded-width/high-variance theorem to the same strong-majority geometry and central cells.

The designated lead root `proofnet24/collective-POS3/fleet04/B10/` was still absent at the scientific snapshot used for this run, so no lead theorem was fabricated or awaited.

Two external results fix the exact exceptional range.

- Max Aires and Jeff Kahn, *Variance vs. range for linear extensions, and balancing extensions in posets of bounded width*, arXiv:2510.26134v1 (30 Oct 2025), Theorem 1.6: for fixed width `w`, `delta(P)->1/2` as `pi(P):=max_x |{y:y||x}| -> infinity`.
- Marcin Peczarski, *The Gold Partition Conjecture for 6-Thin Posets*, Order 25 (2008), 91--103, DOI `10.1007/s11083-008-9081-9`: the Gold Partition Conjecture, hence the 1/3--2/3 conclusion, holds when every element is incomparable with at most six others.

Consequently, if a width-three POS3 counterexample exists, then

`7 <= pi(P) <= K_3`

for some finite (source-qualitative, not numerically supplied) constant `K_3`.  The lower bound is Peczarski; the upper bound follows from Aires--Kahn with a fixed gap from `1/2` (a counterexample has `delta(P)<1/3`).  This is the actual bounded-range/high-comparability residue.  It is not a finite-size statement.

## 2. Compact conditional end-to-end route

Assume a counterexample and choose one of minimum cardinality.  The completed collective reductions allow one to work in a width-exactly-three, incomparability-connected core with no proper autonomous nonchain, while the inherited strong-majority orientation is a transitive total order with the previously recorded block/heavy-slice constraints.  Section 1 places its incomparability range in the finite band `7<=pi(P)<=K_3`.

A legitimate end-to-end route would now be:

1. choose a three-chain cover and use fleet01/B19's exact weighted projection after deleting one chain;
2. retain all nested-profile short-gap defects rather than replace the projected law by a uniform width-two law;
3. use the no-balanced heavy-slice/double-blocker inequalities to show that, in the bounded range `7<=pi<=K_3`, those exact defects cannot all support the same transitive strong-majority orientation;
4. obtain a balanced pair, contradicting minimality.

The **first essential missing implication** is step 3.  A weaker substitute saying that bounded `pi`, bounded variance, bounded insertion multiplicity, connectedness, and module-primality force bounded `|P|` is false.  The rest of this report gives an arbitrary-size counterexample to exactly that substitute, at `pi=7`, the first value not covered by the 6-thin theorem.

## 3. An arbitrary-size width-three prime family at pi=7

For every integer `N>=8`, define closed intervals

`I_i=[i,i+5/4]` for `i=0,...,N-1`,

and one extra interval

`J=[5/4,27/4]`.

Let `R_N` be the interval order on elements `v_0,...,v_{N-1},z`, where an element is below another exactly when its interval lies strictly to the left of the other's interval.

### Theorem 3.1

For every `N>=8`, `R_N` has all of the following properties.

1. `width(R_N)=3`.
2. Its incomparability graph is connected.
3. `pi(R_N)=7` exactly.
4. `R_N` has no proper nontrivial autonomous subset; in fact its incomparability graph is prime.
5. Every element rank in a uniformly random linear extension has variance at most `49/4`.
6. For every element `x` and every linear extension `tau` of `R_N-x`, the number `W_x(tau)` of legal insertion gaps for `x` is at most `8`.

Since `|R_N|=N+1` is arbitrary, these six properties do **not** imply a finite kernel.

### Proof

The path intervals `I_i,I_j` overlap exactly when `|i-j|=1`.  The long interval `J` overlaps exactly `I_0,...,I_6`: it touches `I_0` at `5/4`, meets each through `I_6`, and ends at `27/4<7`, before `I_7` starts.  Thus the incomparability graph `G_N` is the path

`v_0-v_1-...-v_{N-1}`

plus a vertex `z` adjacent exactly to `v_0,...,v_6`.

This graph is connected.  Its maximum degree is exactly seven, at `z`, while every path vertex has degree at most three.  Hence `pi(R_N)=7`.

At any real coordinate at most two path intervals meet, and adding `J` gives at most three mutually overlapping intervals.  There are triangles, for example `J,I_0,I_1`, so the maximum antichain size is exactly three.  Thus `width(R_N)=3`.

It remains to prove primeness.  Recall that a graph module `M` is a vertex set such that every vertex outside `M` is adjacent either to all of `M` or to none of `M`.

Suppose a nontrivial module contains two path vertices `v_i,v_j`, `i<j`.  If `j=i+1`, it already contains an adjacent path pair.  If `j-i>=3`, then `v_{i+1}` is adjacent to `v_i` but not to `v_j`, so the module property forces `v_{i+1}` into `M`, again producing an adjacent pair.  If `j=i+2`, then when `i>0`, `v_{i-1}` distinguishes `v_i` from `v_j`; when `i=0`, `v_3` distinguishes `v_2` from `v_0`.  Again `M` acquires an adjacent path pair.

Once `v_i,v_{i+1}` are in `M`, `v_{i-1}` (when present) distinguishes them and must join `M`; similarly `v_{i+2}` must join.  Iterating forces every path vertex into `M`.  If `z` were outside, it would be adjacent to `v_0` but not to `v_7` (available because `N>=8`), contradicting the module condition.  Hence `z` also lies in `M`, so `M` is the whole graph.

The only remaining possibility for a nontrivial module is that it contains `z` and initially just one path vertex `v_i`.  If `i<=6`, choose a vertex `v_j` among `v_0,...,v_6` with `j` neither `i` nor a path-neighbor of `i`; such a `j` exists because at most three of seven indices are excluded.  Then `z` is adjacent to `v_j` while `v_i` is not, so `v_j` must join `M`.  If `i>=7`, `v_0` distinguishes `z` from `v_i` and must join.  In either case `M` now contains two path vertices and the preceding paragraph forces `M=V(G_N)`.  Thus `G_N` is prime.

Every autonomous subset of a poset is a module of its incomparability graph: an outside element is uniformly below, uniformly above, or uniformly incomparable with all members of an autonomous set, so its incomparability adjacency is all-or-none.  Since `G_N` is prime, `R_N` has no proper nontrivial autonomous subset.

For any finite poset and element `x`, every strict predecessor of `x` is always before `x` and every strict successor always after it.  Therefore in every linear extension

`rank(x)=|Down(x)|+1+ #{y||x : y precedes x}`.

The rank support has range at most `pi(x)`.  Popoviciu's elementary variance bound gives

`Var(rank(x)) <= pi(x)^2/4 <= 49/4`.

Finally, after deleting `x`, all legal insertion gaps lie between the last forced predecessor and first forced successor.  Every element lying in that corridor is incomparable with `x`; hence there are at most `pi(x)+1<=8` legal gaps.  Thus `W_x(tau)<=8` for every `tau`.  This proves all assertions. `□`

## 4. Why this hits the assigned obstruction

The preceding family is deliberately at `pi=7`: it lies immediately outside Peczarski's solved 6-thin class while remaining in an arbitrarily large, highly comparable width-three regime.  It also survives two collective minimal-counterexample-style structural reductions that might otherwise look like compactness mechanisms: connected incomparability and absence of proper autonomous subsets.

Moreover, it has **uniformly bounded rank variance** and **uniformly bounded one-element insertion fibers**.  Thus neither the bounded-variance conclusion from the Aires--Kahn route nor a pointwise bounded one-element version of the fleet01/B19 insertion weights converts the exceptional regime to finitely many orders.

This applies the partner result rather than merely citing it: fleet01/B19 shows the weighted deletion law is the correct object and that nested-profile defects are the genuine local obstruction.  The family here shows that even making the local insertion multiplicities uniformly tiny does not compactify the global problem.  Therefore a valid successor must actually use the no-balanced probability inequalities to charge B19's nested-profile/short-gap defects; counting bounded local states without a pumping/contradiction theorem is insufficient.

## 5. Regression calculation

The standard-library verifier in `code/verify_prime_pi7_family.py` constructs the exact interval-overlap graph and, for `N=8,...,12`, independently checks the expected graph, maximum incomparability degree seven, clique number three, and absence of every nontrivial graph module by exhaustive subset testing.

Executed as

`python -S code/verify_prime_pi7_family.py`

it returned exit status zero and:

```
POS3_PRIME_PI7_FAMILY_CHECK_PASS
N path_vertices total_vertices max_incomparability width nontrivial_modules
8 9 7 3 0
9 10 7 3 0
10 11 7 3 0
11 12 7 3 0
12 13 7 3 0
```

The script SHA-256 is `b225dcf333772a5a777e09599dc8ddf1f2b2587d4c484b43ed7e00432cef8eda`.  This finite calculation is only a regression check; Theorem 3.1 is the arbitrary-`N` proof.

## 6. Exact status and handoff

- Peczarski closes the subcase `pi(P)<=6`: **SOURCE-ESTABLISHED, APPLIED TO RESIDUAL**.
- Aires--Kahn implies existence of a finite upper bound `pi(P)<=K_3` in any POS3 counterexample: **SOURCE-ESTABLISHED, QUALITATIVE CONSTANT ONLY**.
- Therefore a hypothetical POS3 counterexample lies in `7<=pi(P)<=K_3`: **DERIVED**.
- Arbitrary-size `R_N` with width three, connected incomparability, module-primality, `pi=7`, bounded rank variance and `W_x<=8`: **PROVED**.
- Candidate implication "those exceptional-regime structural/variance bounds yield a finite kernel": **REFUTED**.
- Width-three 1/3--2/3 target: **OPEN / NOT PROVED**.

**Next recipient / exact missing implication.**  The lead/integrator should not launch a finite census from the bounded-range theorem.  The next proof step should be a no-balanced-specific bounded-degree transfer: in the connected module-prime width-three core with `7<=pi<=K_3`, combine the fleet01/B19 nested-profile defect formula with the fleet03/B11 simultaneous double-blocker constraints and the established heavy-slice/canonical-cell masses to force one weighted orientation ratio into `[1/2,2]`, equivalently a balanced pair.  A transfer/pumping argument is required; bounded local state by itself is not compactness.

No claim is made that `R_N` is a counterexample to POS3; it is a counterexample only to the finite-kernel shortcut above.  No novelty or priority claim is made.
