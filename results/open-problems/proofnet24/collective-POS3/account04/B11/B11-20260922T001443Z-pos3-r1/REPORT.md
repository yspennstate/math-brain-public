# POS3 account04/B11 — explicit bounded-variance anchor and no-finite-kernel warning

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has a `1/3–2/3` balanced incomparable pair under the uniform law on linear extensions.  
**Parent status after this report:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run follows the later collective-open-problems owner directive, which supersedes the older benchmark assignment for this slot.  The assigned POS3 subproblem is to attack the exceptional bounded-variance / high-comparability regime left after using the actual bounded-width variance theorem, without inventing a finite-kernel reduction.

## 1. Source-bound state consumed

The current source target is width at most three, not order dimension.  Three compatible results were consumed before deriving the new statements below.

1. **Assigned partner `account01/B19`.**  `proofnet24/collective-POS3/account01/B19/B19-20260921T235148Z-pos3-r01/REPORT.md` proves the exact chain insertion/deletion fiber formula.  In particular, for one deleted element `x`, every extension `tau` of `P-x` has an exact number `W_x(tau)` of legal insertion gaps, and
   `e(P)=sum_tau W_x(tau)`.  The induced law after deletion is therefore weighted, not generally uniform.
2. **Other-account result `account02/B11`.**  `proofnet24/collective-POS3/account02/B11/20260921T235736Z-b11-44e20585/REPORT.md` proves exact ordinal factorization by incomparability components.  Hence a cardinality-minimal POS3 counterexample may be assumed to have connected incomparability graph.  With inherited state, its unresolved core has width exactly three, at least 15 elements, and at least five maximal contiguous chain blocks in the strong-majority order.
3. **Other-account result `account01/B10`.**  `proofnet24/collective-POS3/account01/B10/20260921T235306Z-account01-B10/REPORT.md` gives the exact three-chain ideal-state/path encoding and its heavy-slice normal form.  It retains the third-chain multiplicity rather than replacing it by a uniform two-chain projection.

The designated team-lead root `proofnet24/collective-POS3/account04/B10/` was absent at the final pre-write repository check, so there was no complete team-lead version to consume.  The required state was therefore reconstructed from the source-bound target and the completed compatible reports above rather than waiting or inventing a lead result.

The external theorem used is Max Aires and Jeff Kahn, *Variance vs. range for linear extensions, and balancing extensions in posets of bounded width*, arXiv:2510.26134v1 (30 Oct 2025), especially Theorems 1.5, 1.6, the Shepp XYZ inequality recalled as Theorem 2.1, Corollary 2.4, and Theorem 2.6.  Their Theorem 1.6 is qualitative: for fixed width, sufficiently large incomparability range forces balance tending to `1/2`; it does **not** provide a finite-size kernel for the present problem.

## 2. A product-form strengthening of the boundary theorem

The following observation is implicit in the two XYZ applications in the proof of Aires--Kahn Theorem 2.6, but keeping the actual boundary sizes and actual two-sided probabilities gives a sharper form useful at width three.

### Lemma 2.1 — boundary product lemma

Let `P` be the disjoint union of `{x}`, an ideal `D`, and a filter `U`.  Put

`A=max(D)` and `B=min(U)`.

Assume the events below have positive probability.  Then

`Pr(A precedes x precedes B) >= product_{a in A, b in B} Pr(a precedes x precedes b)`.

**Proof.**  Write `r_ab=Pr(a precedes x precedes b)`.  Fix `a in A`.  Conditioning on `a precedes x` gives a uniform linear-extension law of the poset obtained by adjoining that relation.  The XYZ inequality gives

`Pr(x precedes B | a precedes x)`
` >= product_{b in B} Pr(x precedes b | a precedes x)`
` = product_b r_ab / Pr(a precedes x)^{|B|}`.

After multiplying by `Pr(a precedes x)` and using `Pr(a precedes x)<=1`,

`Pr(a precedes x precedes B) >= product_b r_ab`.

Now condition on `x precedes B`.  A second XYZ application, this time to all `a in A`, gives

`Pr(A precedes x | x precedes B)`
` >= product_a Pr(a precedes x | x precedes B)`.

Using the previous inequality in each factor and multiplying back by `Pr(x precedes B)<=1` yields

`Pr(A precedes x precedes B) >= product_{a,b} r_ab`.

This is exactly the source proof with the coarse replacements `|A|,|B|<=w` postponed rather than made at the start.  `□`

## 3. Width-three majority-rank anchor

For an element `x`, write

`delta_x=max_{y!=x} min(Pr(x precedes y),Pr(y precedes x))`.

Assume `P` has width at most three and `delta_x<1/3`.  Define

`D_x={y!=x : Pr(y precedes x)>2/3}`,

`U_x={y!=x : Pr(x precedes y)>2/3}`.

Because no pair involving `x` is balanced, `D_x` and `U_x` partition `P-{x}`.  Also `D_x` is an ideal: if `z<y` and `y in D_x`, the event `y precedes x` implies `z precedes x`.  Symmetrically `U_x` is a filter.

Put `A=max(D_x)` and `B=min(U_x)`.  Both are antichains, so `|A|,|B|<=3`.

### Theorem 3.1 — explicit canonical rank atom

Let `f(x)` be the rank of `x` in a uniformly random linear extension and put

`k_x=|D_x|+1`.

Then

`Pr(f(x)=k_x) > 16/6561`.

If `D_x` or `U_x` is empty, the stronger bound

`Pr(f(x)=k_x) > 8/27`

holds.

**Proof: two-sided case.**  Assume both `D_x,U_x` are nonempty.  For `a in A,b in B`, there are three possibilities relevant to a lower bound.

- If both `a` and `b` are incomparable with `x`, then `Pr(a precedes x)>2/3` and `Pr(x precedes b)>2/3`, so the union bound gives `Pr(a precedes x precedes b)>1/3`.
- If exactly one of `a,b` is incomparable with `x`, the other comparison with `x` is forced by the poset, so `Pr(a precedes x precedes b)>2/3`.
- If both are comparable with `x`, then necessarily `a<x<b` in the poset and the probability is `1`.

Let `a=|A|`, `b=|B|`, and let `m` and `n` be the numbers of members of `A` and `B`, respectively, incomparable with `x`.  Since `A` is an antichain and `P` has width at most three, `m<=2` whenever `a=3`; otherwise `m<=a`.  Thus `m<=min(a,2)`, and similarly `n<=min(b,2)`.

By Lemma 2.1,

`Pr(A precedes x precedes B)`
` > (1/3)^(mn) (2/3)^(m(b-n)+(a-m)n)`.

Minimizing this elementary expression over

`1<=a,b<=3`, `0<=m<=min(a,2)`, `0<=n<=min(b,2)`

gives `16/6561`, with the formal worst pattern `a=b=3,m=n=2`.

Finally, if every maximal member of the ideal `D_x` precedes `x`, then every element of `D_x` precedes `x`; if `x` precedes every minimal member of the filter `U_x`, then `x` precedes every element of `U_x`.  Hence the event `A precedes x precedes B` forces exactly the `|D_x|` elements of `D_x` to lie before `x`, so it is contained in `{f(x)=k_x}`.  This proves the displayed bound.

**Proof: one-sided case.**  If `D_x` is empty, let `B=min(U_x)`.  Then `|B|<=3`, and XYZ gives

`Pr(x precedes B) >= product_{b in B} Pr(x precedes b) > (2/3)^|B| >= 8/27`.

The event `x precedes B` forces `x` before all of the filter `U_x`, hence `f(x)=1`.  The case `U_x` empty is symmetric.  `□`

### Corollary 3.2 — explicit bounded-variance normal form

If `P` is a POS3 counterexample, then `delta_x<1/3` for **every** `x`.  Therefore

`q(x):=max_k Pr(f(x)=k) > 16/6561`

for every element.  By Aires--Kahn Corollary 2.4 (`sigma(x)=Theta(1/q(x))`), all element-rank standard deviations are bounded by an absolute constant in a hypothetical width-three counterexample.

This makes the “bounded-variance exceptional regime” explicit rather than merely invoking Theorem 1.5 qualitatively.  No claim is made that the hidden constant in the source's `Theta` notation has been made explicit here.

In the inherited global counterexample state, the strong-majority orientation is a transitive total order `L_*`; then `D_x` is exactly the set of elements before `x` in `L_*`, so `k_x` is the `L_*` rank of `x`.  Thus every element has a non-negligible atom at its canonical strong-majority rank.

## 4. New splice to the partner's deletion recurrence

Apply the account01/B19 one-element deletion formula with `Q=P-x`.  For `tau in L(Q)`, `W_x(tau)` is the number of legal gaps in which `x` can be inserted, and

`e(P)=sum_{tau in L(Q)} W_x(tau)`.

For a fixed rank `k`, each `tau` contributes at most one full extension in which `x` has rank `k`.  Hence

`#{L in L(P): f(x)=k} <= e(P-x)`.

Combining this with Theorem 3.1 at `k=k_x` gives the exact counterexample-specific deletion-ratio bound

`e(P)/e(P-x) < 6561/16 = 410.0625`

for every `x`.

For a strong-majority endpoint (equivalently one of `D_x,U_x` is empty),

`e(P)/e(P-x) < 27/8 = 3.375`.

Equivalently, under the **uniform** law on `L(P-x)`,

`E[W_x] = e(P)/e(P-x) < 6561/16`.

This does not contradict B19's width-two family with unbounded `max W/min W`: that family concerns a universal pointwise density ratio, whereas the present statement is a **counterexample-specific mean insertion-multiplicity bound** forced by the absence of a balanced partner.  It is therefore a usable replacement for the false bounded-density shortcut.

A simple Markov consequence is that for any `T>0`, at most `(6561/16)/T` of the extensions of `P-x` can have `W_x(tau)>=T`.  This is not yet a balance transfer theorem, but it sharply limits how much of a hypothetical counterexample's deletion law can sit in very high-multiplicity fibers.

## 5. New splice to the exact three-chain path encoding

Fix the account01/B10 chain partition `C_1 sqcup C_2 sqcup C_3=P`, and suppose `x=c_{a,r}`.  Let `g_b(x)` and `g_c(x)` be the numbers of elements of the other two chains preceding `x` in the strong-majority order `L_*`.

Immediately before the canonical `x` step, define the unique ideal-state

`u_x^*=(...,r-1,...,g_b(x),...,g_c(x),...)`.

On the event `A precedes x precedes B` from Theorem 3.1, all members of `D_x` are before `x` and all members of `U_x` after it.  Therefore the corresponding full path uses this single canonical edge

`u_x^* -> u_x^*+e_a`.

With the forward/backward counts `A_path,B_path` of account01/B10 and `E=e(P)`, we obtain

`A_path(u_x^*) B_path(u_x^*+e_a) > (16/6561) E`.

At a strong-majority endpoint the lower bound improves to `(8/27)E`.

Thus the prior one-dimensional heavy-slice normal form can be supplemented with a **joint canonical-cell anchor**: every element in a hypothetical counterexample has one exact three-chain edge carrying a fixed positive fraction of all full extensions.  This is stronger information than a marginal insertion slice alone and is expressed entirely in the true uniform law on `L(P)`.

## 6. What the actual bounded-width theorem does and does not buy

Aires--Kahn Theorem 1.6 implies qualitatively that there exists some finite constant `K_3` such that any width-at-most-three POS3 counterexample must satisfy

`pi(P):=max_x |{y:y || x}| <= K_3`.

The paper does not supply here a numerical `K_3` suitable for a finite census, and even a proved numerical bound on `pi(P)` would **not** by itself reduce the problem to finitely many orders.

### Proposition 6.1 — bounded incomparability range is not a finite kernel

For every `n>=3`, define a poset `Q_n` on `{1,...,n}` by

`i <_{Q_n} j` iff `j-i>=3`.

Then:

1. `Q_n` has width exactly three: every consecutive triple is an antichain, while four pairwise incomparable indices cannot fit inside distance two of each other.
2. Its incomparability graph is the square `P_n^2` of the `n`-vertex path, hence is connected.
3. Every element is incomparable with at most four others, so `pi(Q_n)<=4`.
4. The order `n` is arbitrary.

Therefore width three + connected incomparability graph + bounded incomparability range does not imply bounded `|P|`.  In particular, the qualitative `K_3` supplied by Theorem 1.6 cannot be turned into an exhaustive finite-kernel argument without a genuinely new reduction.  This directly rules out the shortcut forbidden in the assignment.

`Q_n` is only a structural non-compactness witness; it is **not** claimed to be a counterexample to POS3.

## 7. Deterministic finite regression

The companion standard-library script

`code/verify_majority_rank_anchor.py`

exhausts every distinct transitively closed strict relation compatible with the natural order for `n<=6`, restricts to width at most three, enumerates all linear extensions exactly, and checks every local pair `(P,x)` for which `x` has no `1/3–2/3` balanced partner.

Archived output:

`POS3_MAJORITY_RANK_ANCHOR_CHECK_PASS`

with

- `3702` width-at-most-three posets in the deduplicated natural-order-compatible enumeration;
- `3275` qualifying `(P,x)` cases;
- `886` two-sided and `2389` one-sided cases;
- no violation of the `16/6561` anchor;
- no violation of the stronger `8/27` one-sided anchor;
- no violation of the exact boundary-product inequality.

The smallest observed canonical rank atom in this range was `1/5`.  This finite regression is evidence against implementation/algebra mistakes only; the proof is Sections 2--3.

A useful false start was preserved in the run history: the first version tried to apply the two-sided boundary theorem to an `L_*` endpoint, where one of `D_x,U_x` is empty.  The finite checker exposed that missing hypothesis.  Replacing that step by the one-sided XYZ argument produced the stronger endpoint bound `8/27`; no theorem threshold was weakened to make the test pass.

## 8. Net progress and remaining obstruction

The parent POS3 target remains open.  The progress is a quantitative characterization of the regime that survives the actual bounded-width variance theorem:

- every element of a counterexample has a canonical rank atom `>16/6561`;
- the two strong-majority endpoints have canonical rank atoms `>8/27`;
- every one-element deletion has mean insertion multiplicity `<6561/16`, with endpoint mean `<27/8`;
- in the exact three-chain path model every element has a single canonical edge carrying `>16/6561` of all paths;
- bounded incomparability range cannot be misreported as a finite-size kernel.

The highest-value next splice is to combine the counterexample-specific **mean** insertion-multiplicity bound with account04/B20's proved adjacent-swap `1`-Lipschitz law for one-element insertion weights.  B19 shows that a universal pointwise density bound is false; the present theorem supplies a bounded mean, while B20 supplies local Lipschitz control.  A successful reflection/pairing argument only needs to control the aggregate path cost on most fibers, not `max W/min W` globally.  In parallel, the joint canonical-edge anchors should be tested against B10's simultaneous `>E/3` heavy-slice constraints to seek an overlap contradiction.

No full solution, novelty/priority claim, benchmark result, held-out data, production key, private transcript, email/Drive action, paid compute, workflow dispatch, or permission change is claimed.
