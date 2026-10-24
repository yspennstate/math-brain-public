# POS3 account03/B19 — exact reverse-blocker branching at a strict nested endpoint

**Run:** `20260922T0332Z-b19-pos3-r11`  
**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent POS3:** **OPEN / NOT PROVED**  
**Inherited finite frontier:** `n_bal=14` unchanged  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact state consumed

The source target is the width-at-most-three scope of the 1/3–2/3 conjecture under the uniform law on **all** linear extensions. No projected/deleted law is silently replaced by a uniform law.

The assigned named partner is **account04/B10**. I consumed its completed run `20260922T031005Z-B10-POS3-r11`, report blob `b077c3fedba7e6e8ab72b683b5eafd8203005467` at source commit `e24ee7f00535e0428bfa2a677ea02c508f9413c9`. Its strict nested-corridor theorem gives the following state in a cardinality-minimal hypothetical counterexample at the first-boundary sibling pair, after relabeling:

- `a || b` and `Pred(b) subsetneq Pred(a)`;
- `D=Pred(a)\Pred(b)` is a chain, and its top `d=max D` satisfies `d lessdot a`;
- the account01/B11 exact endpoint identity applies:

  `p_ab = 1-(Q+R)/(2E)`,

  where `E=e(P)`, `Q` is the common forward minimal-blocker event and `R` is the reverse nonneutral-blocker remainder;
- in the majority-late branch `b prec_* a`, either `(b,d)` is a shorter extreme pair or there exists a minimal Hasse successor blocker of `b` relative to `a`; in the no-span-descent subbranch every such blocker lies after `a` in the strong-majority order.

I also use the exact endpoint theorem proved by account01/B11 and my immediately preceding cut-charge addendum, which converts deletion of the delayed predecessor-difference chain into original-uniform pair probabilities rather than a fictitiously uniform quotient law.

The partner's first unpaid implication was global: iterate the incoming bow-tie and outgoing blocker corridor until a balanced pair, a four-antichain, an autonomous nonchain, span descent, or a flux contradiction occurs. This run attacks that implication by resolving the **local channel structure of every strict majority-late continuation** exactly.

## 2. Compact conditional route

Assume for contradiction that `P` is a cardinality-minimal POS3 counterexample. Take a strict nested endpoint `a||b` with

`Pred(b) subsetneq Pred(a)`.

Let

`D=Pred(a)\Pred(b)={d_1<...<d_k}`, `d=d_k`,

and define the two minimal successor-blocker sets

`M = Min{z : a<z and z||b}`,
`U = Min{z : b<z and z||a}`.

The partner already proves that in the majority-early branch `a prec_* b`, absence of span descent forces `|M|=2`.

The missing majority-late branch is more delicate because the reverse remainder `R` could in principle look like a single opaque error term. The theorem below shows that it is not opaque: it is the union of at most three explicit pair events, and in a no-balanced no-descent counterexample no single one can carry the required mass. Hence strict continuation is necessarily **branching**, not a one-dimensional corridor.

## 3. Exact reverse-blocker union identity

### Theorem 3.1

Let `P` be any finite poset, let `a||b`, assume

`Pred(b) subsetneq Pred(a)`,

and assume `D=Pred(a)\Pred(b)` is a finite chain with top `d`. Put

`U=Min{z:b<z and z||a}`.

Let `R` be the account01/B11 reverse nonneutral-blocker remainder: the number of linear extensions in which `b` precedes `a` and the open interval between them contains an element comparable in the poset with at least one endpoint.

Then, as an exact set identity on the original uniform extension space,

`R = | {L:b<_{L}d} union (union_{u in U}{L:u<_{L}a}) |`.        `(RB)`

No deletion, quotient, or induced-law uniformity is used.

### Proof

Fix a reverse extension `L` with `b<_{L}a`. The structural part of the endpoint exchange theorem says that every nonneutral element between `b` and `a` is of one of two kinds:

1. a predecessor of `a` incomparable with `b`, or
2. a successor of `b` incomparable with `a`.

The first class is exactly `D`. Since `D` is a chain with top `d` and every element of `D` is below `a` in the poset, some member of `D` lies between `b` and `a` in `L` iff `b<_{L}d`.

For the second class, suppose `z` lies between `b` and `a`, with `b<z` in the poset and `z||a`. Choose a minimal element `u` of `{w:b<w, w||a}` below `z`; then `u in U`. Because `u<=z` in the poset and `z<_{L}a`, we have `u<_{L}a`. Conversely, if `u in U` and `u<_{L}a`, then the poset relation `b<u` places `u` strictly between `b` and `a`, so the interval is nonneutral.

Thus the reverse extension is counted by `R` iff at least one event displayed in `(RB)` occurs. `square`

## 4. Width-three channel budget

### Lemma 4.1

The set `M union U` is an antichain. Consequently, when `width(P)<=3`,

`|M|+|U| <= 3`.                                               `(WB)`

### Proof

Each of `M` and `U` is an antichain by minimality. Take `m in M` and `u in U`. If `m<u`, then `a<m<u`, contradicting `u||a`. If `u<m`, then `b<u<m`, contradicting `m||b`. Hence `m||u`. `square`

This couples the forward and reverse endpoint channels for the first time: the width-three hypothesis budgets them **jointly**, not separately.

In particular:

- the partner's majority-early/no-descent state `|M|=2` forces `|U|<=1`;
- if the majority-late branch ever has `|U|=2`, then `|M|<=1`.

## 5. Branching theorem for the majority-late strict corridor

### Theorem 5.1

Assume now that `P` is a hypothetical POS3 counterexample, that the strict endpoint satisfies

`b prec_* a`,

and that the partner's shorter-span escape through `(b,d)` does not occur. Then:

1. `U` is nonempty and every `u in U` lies after `a` in the strong-majority order;
2. every atomic reverse event in `(RB)` has probability strictly below `1/3`:

   `Pr(b<d)<1/3`,
   `Pr(u<a)<1/3` for every `u in U`;
3. nevertheless their union has probability strictly above `1/3`:

   `R/E > 1/3`;
4. therefore no single reverse blocker can account for the continuation. At least two atomic channel events are necessary to form `R`.

If `|U|=1`, writing `U={u}`, the two events

`A={L:b<_{L}d}`, `B={L:u<_{L}a}`

satisfy

`|A|<E/3`, `|B|<E/3`, but `|A union B|=R>E/3`.

Hence neither contains the other, and both exclusive crossing classes are nonempty:

`A\B != empty`, `B\A != empty`.                              `(X2)`

### Proof

Part 1 is the named partner's strict nested-corridor continuation theorem. Since `(b,d)` is not a shorter extreme pair, the partner derives `d prec_* b`; because `b||d` and there is no balanced pair, this gives `Pr(b<d)<1/3`.

For every `u in U`, no span descent forces `a prec_* u`; since `a||u` and no pair is balanced, `Pr(u<a)<1/3`. This proves part 2.

The endpoint identity gives, in the branch `p_ab<1/3`,

`Q+R>4E/3`.

Since always `Q<=E`, we obtain `R>E/3`. By Theorem 3.1 this is exactly the union of the atomic events in part 2. A union of just one such event would have mass `<E/3`, contradiction, so at least two channels are genuinely needed.

When `|U|=1`, `(RB)` has exactly the two events `A,B`. If `A subseteq B`, then their union has size `|B|<E/3`, contradiction; similarly for `B subseteq A`. This gives `(X2)`. `square`

### Interpretation

The named partner's continuation cannot be a single blocker path. In the majority-early branch it already produces **two forward Hasse blockers**. In the majority-late branch, Theorem 5.1 shows that the supercritical reverse remainder is necessarily assembled from at least two subcritical atomic crossing channels. Together with `(WB)`, every strict no-descent endpoint has a sharply bounded but genuinely branching local channel structure.

This is the new applied essential step. The remaining global problem is no longer merely “follow the next blocker.” It is to prove that repeated branching/merging inside a width-three strong-majority order cannot continue indefinitely without one of the known escape outcomes.

## 6. Exact six-element sharpness witness

The local theorem is sharp enough that a stronger endpoint-only closure is false. Consider the six-element poset with Hasse covers

`0<3`, `1<2`, `1<3`, `2<4`, `2<5`, `3<5`.

It has width **two** (hence is a valid width-at-most-three test object) and exactly `E=14` linear extensions. Take

`a=3`, `b=2`, `d=0`, `u=4`.

Then

`Pred(b)={1}`, `Pred(a)={0,1}`, `D={0}`, `U={4}`, `M=empty`.

Exact ideal-state counting gives

`Pr(a<b)=4/14=2/7<1/3`,
`Pr(b<d)=4/14=2/7<1/3`,
`Pr(u<a)=4/14=2/7<1/3`.

Here `Q=E=14`, while the exact reverse remainder is `R=6`. Thus

`Q+R=20`, and
`p_ab=1-(Q+R)/(2E)=1-20/28=4/14`.

Let

`A={L:b<_{L}d}`, `B={L:u<_{L}a}`.

The exact counts are

`|A|=4`, `|B|=4`, `|A cap B|=2`, `|A union B|=6`,
`|A\B|=|B\A|=2`.

So each atomic channel is strictly subcritical, yet their union is supercritical:

`4/14<1/3`, but `6/14=3/7>1/3`.

The only balanced incomparable pairs are `(0,1)` with counts `5/9` in the two orientations and `(4,5)` with counts `9/5`; neither endpoint `a=3` nor `b=2` participates in a balanced pair.

Therefore the tempting stronger statement

> a strict majority-late endpoint with `R>E/3` must have one balanced reverse-blocker channel, or a balanced pair touching the endpoint itself

is false even in width two. This is **not** a counterexample to POS3; the witness contains balanced pairs, as it must in the known width-two case. It is a targeted counterexample to a stronger local closure mechanism.

## 7. Exact executable certificate

`verify_pos3_reverse_branching.py` independently enumerates all 14 linear extensions of the witness from its transitive closure and checks:

- width exactly two;
- the strict predecessor nesting and blocker sets;
- all three `4/14` endpoint/channel probabilities;
- the endpoint identity with `Q=14`, `R=6`;
- the two atomic channel sizes, their intersection, union and exclusive masses;
- the full list of balanced incomparable pairs;
- absence of a balanced pair touching `a` or `b`.

Verifier SHA-256: `423d5c9643db20e6ffb931d62df22dff6df0624291c9fb0b3e758a762e416b4a`.  
Captured output SHA-256: `8ceeabe0c82d61cd11b6bed4dd0b339d49d4ca0903e2e4549600267c8b5d68c1`.  
Terminal marker: `POS3_B19_REVERSE_BRANCHING_CERTIFICATE_PASS`.

The finite witness validates/refutes only the local mechanism. Theorem 3.1, Lemma 4.1 and Theorem 5.1 are proved symbolically for arbitrary finite posets satisfying their hypotheses.

## 8. First remaining global implication

The first missing implication is now the following narrower statement.

**GLOBAL_BRANCH_MERGER.** In a cardinality-minimal width-at-most-three counterexample, start from the inherited first-boundary strict nested endpoint and repeatedly apply the partner's Hasse-corridor continuation. Using simultaneously

- the joint channel budget `|M|+|U|<=3`,
- the majority-early two-forward-blocker branch,
- the majority-late reverse-union branching theorem above,
- the delayed-distinguisher/nested-predecessor structure,
- the exact original-uniform cut-charge/crossing identities,
- and the inherited pinned-rank/heavy-slice constraints,

prove that the finite branching structure must terminate in a balanced pair, a four-antichain, a proper autonomous nonchain, strict span descent, or a signed flux contradiction.

The six-element witness shows that no proof can replace this with a one-boundary pigeonhole on `R`; two subcritical reverse channels may genuinely aggregate above `1/3` while balance occurs only after moving to adjacent structure.

This is a strict narrowing of the partner's prior “iterate the corridor” residual: the local degree, event identity, and cross-channel incomparability are now exact. What remains is a **global branch-merger/conservation argument**.

## 9. Claims not made

This report does not claim POS3 solved, does not move the `n_bal=14` frontier, does not treat any biased induced law as uniform, does not claim novelty or priority, and does not claim verified brain use. It preserves the parent target as OPEN / NOT PROVED.
