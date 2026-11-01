# POS3 fleet02/B10 — one-distinguisher balance theorem and doubled delayed-witness obligation

**Run:** `B10-20260922T024630Z-pos3-r13`  
**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

No benchmark or installation work is performed here. All probabilities below are under the actual uniform law on the full linear-extension set of the stated poset.

## 1. Fresh source-bound state consumed

The run began from fresh owner control revision `2026-09-22.2` at main commit `09514511ab60a8956ed4abdba5f30a453a3dadeb`. The active owner programme assigns fleet02/B10 to POS3 coupling/adjacent-swap research and stops the old benchmark/installation duties.

The essential mathematical inputs are:

1. **Campaign lead fleet04/B10**, run `20260922T011127Z-fleet04-B10-POS3-r11`, report blob `1e5a9682e4f90f38484a86e7199428de0b0160f8`. In a hypothetical width-at-most-three counterexample, every element has its strong-majority rank with probability `>1/81`; equivalently each corresponding three-chain central flux cell satisfies `81 W>E`.
2. **Named partner fleet03/B11**, run `B11-20260922T021330Z-pos3`, report blob `84167cd7b3a69dc8e4c699fc5ca0e5c9ba5e4a8d`. It proves the exact two-gap deletion-fiber formula for an incomparable pair and that global probability `>2/3` forces an exact fiber with `A_tau>2B_tau`. Its eight-element width-three witness has `121` extensions, sibling probability `Pr(3<6)=82/121`, and exactly two distinguisher vertices `{4,5}`.
3. **Partner predecessor fleet03/B11**, run `20260922T011439Z-fleet03-B11-pos3-r12`, report blob `3443c6ccc4436b9eaf060884c4eec6fc85dc1792`. At the first strong-majority chain-block boundary `x prec_* y`, the canonical successor blockers are exactly two Hasse covers `x lessdot s_1,s_2`; the pair `{s_1,s_2}` is nonautonomous, and every vertex distinguishing the two blockers occurs strictly after the whole second majority block `B_2`.
4. **Immediate fleet02/B10 predecessor**, report blob `acdb868b3e35a9248d494126311bfff3bfee150b`. It proves the exact endpoint blocker-product bound and, at the first boundary of a hypothetical counterexample, activates **both** Hasse-blocker deletion-flow channels.

The new theorem below directly strengthens item 3 and uses the same exact-multiplicity philosophy as item 2. It does not assume that a deletion skeleton is uniformly distributed.

## 2. Compact conditional end-to-end route

Assume, for contradiction, a cardinality-minimal width-at-most-three POS3 counterexample. Use the inherited transitive strong-majority order and its first chain-block boundary `x prec_* y`.

The partner gives two successor Hasse blockers `s_1,s_2`. Because they are incomparable, their pair itself must be extreme in a counterexample. The partner already proves that every vertex distinguishing `s_1` from `s_2` occurs only after `B_2`, but previously nonautonomy guaranteed only **one** such delayed witness.

The first missing implication attacked in this run is:

> Can a single delayed distinguisher support an extreme blocker-sibling probability, once every exact insertion multiplicity is retained?

The answer is **no**. In fact, in every finite poset, an incomparable pair with exactly one distinguisher is automatically balanced. Hence a hypothetical counterexample must give the endpoint blocker siblings at least **two distinct delayed distinguishers after `B_2`**.

Combined with the previous fleet02/B10 result, the first endpoint now has two simultaneous multiplicity constraints:

- both Hasse blocker **flow channels** are active; and
- the blocker-sibling pair has at least two distinct later **structural distinguisher channels**.

This does not close POS3. The next unpaid step is to couple these two-by-two structures through the next strong-majority boundary.

## 3. Distinguisher definition

For incomparable `a,b`, call `z notin {a,b}` a **distinguisher** if its poset relation to `a` differs from its relation to `b`. Thus the three-valued relation

`rel(z,a) in {z<a, z||a, a<z}`

differs from `rel(z,b)`.

If there are no distinguishers, `{a,b}` is an autonomous two-point antichain and the label-swap involution gives `Pr(a<b)=1/2`.

The new case is exactly one distinguisher.

## 4. One-distinguisher balance theorem

### Theorem 4.1

Let `P` be any finite poset and let `a,b` be incomparable. Suppose exactly one vertex `z` distinguishes `a` from `b`. Then

`1/3 <= Pr(a<b) <= 2/3`.

More precisely, after possibly swapping `a,b` and/or taking the order dual, one may assume

`a<z`, `b||z`,

and then

`1/2 <= Pr(a<b) <= 2/3`.

### Proof

By the stated symmetries it is enough to treat `a<z` and `b||z`. Put

`Q=P\{a,b,z}`

and fix an arbitrary skeleton `tau in L(Q)`. Number its external insertion gaps `0,1,...,|Q|`.

Because `z` is the **only** distinguisher, every element of `Q` has exactly the same relation to `a` as to `b`. Hence the admissible gap intervals of `a` and `b` relative to `tau` coincide. Write

`I_a(tau)=I_b(tau)=I=[ell,u]`.

Write the admissible interval for `z` as

`J=[r,s]`.

The relation `a<z` forces a useful nesting of the endpoints. Every predecessor of `a` is also a predecessor of `z`, so

`r>=ell`.

Every successor of `z` in `Q` is a successor of `a`; since no element of `Q` distinguishes `a,b`, it is also a successor of `b`. Thus

`Succ_Q(z) subseteq Succ_Q(a)=Succ_Q(b)`,

so the earliest successor bounding `z` cannot occur before the earliest common successor bounding `a,b`, and therefore

`s>=u`.

Shift the gap indices by `ell`. Put

`I={0,1,...,m-1}`,
`J={d,d+1,...,m-1+e}`

for integers `m>=1`, `d,e>=0` (with `J` nonempty).

A lift of `tau` must respect `a<z`. Hence exactly three relative orders of the inserted triple are possible:

`b<a<z`, `a<b<z`, `a<z<b`.

Let their exact lift counts be `B_tau,C_tau,D_tau`, respectively. Choosing the three external gaps gives

`C_tau = #{(i,j,k): i,j in I, k in J, i<=j<=k}`,

`B_tau = #{(i,j,k): i,j in I, k in J, j<=i<=k}`,

`D_tau = #{(i,j,k): i,j in I, k in J, i<=k<=j}`.

Equal-gap cases are counted exactly once in each displayed relative order: the order inside a shared external gap is fixed by the displayed triple order. Swapping the dummy variables `i,j` gives the exact symmetry

`B_tau=C_tau`.                                                (4.1)

It remains to compare `D_tau` with `C_tau`. If `d>=m`, then no `k in J` lies in `I`, so `D_tau=0`. Otherwise,

`D_tau = sum_{k=d}^{m-1} (k+1)(m-k)`.                         (4.2)

On the other hand, fixing the gap `j` of `b` in the pattern `a<b<z`,

`C_tau = sum_{j=0}^{m-1} (j+1) * #{k in J:k>=j}`.             (4.3)

For every `j>=d`,

`#{k in J:k>=j}=m+e-j >= m-j`.

The terms with `j<d` are nonnegative. Therefore (4.3) dominates (4.2) term by term on `j=d,...,m-1`, and

`D_tau<=C_tau`.                                                (4.4)

Now sum over **all** skeletons `tau`; no distribution on skeletons is introduced. Let

`B=sum B_tau`, `C=sum C_tau`, `D=sum D_tau`.

Then (4.1)-(4.4) give `B=C` and `0<=D<=C`. The full extension counts are

`N(b<a)=B=C`,
`N(a<b)=C+D`.

Thus `N(a<b)>=N(b<a)` and `N(a<b)<=2N(b<a)`. Equivalently,

`1/2 <= Pr(a<b) <= 2/3`.

The swap/order-dual reductions cover every possible single-distinguisher type. This proves the theorem. `square`

### Corollary 4.2 — two distinguishers are necessary for every extreme pair

If a finite poset has no balanced incomparable pair, then **every incomparable pair has at least two distinguishers**.

Indeed zero distinguishers gives probability `1/2`, while exactly one is covered by Theorem 4.1.

This corollary needs no width hypothesis.

## 5. Applied to the partner's endpoint fork

At the first strong-majority block boundary in the inherited hypothetical width-three counterexample, the named partner proves that the blocker siblings `s_1,s_2` are incomparable and that **every** distinguisher of them lies strictly after the entire second block `B_2`.

Corollary 4.2 now upgrades that statement:

> There exist at least two **distinct** vertices after `B_2` that distinguish `s_1` from `s_2`.

The order-dual statement gives at least two distinct delayed distinguishers before the penultimate block for the last-boundary predecessor siblings.

This is a real strengthening of the current arbitrary-size structural state. It is also compatible with the fleet02/B10 two-channel mass transport: the first endpoint simultaneously has two active Hasse flow channels and at least two delayed nonautonomy witnesses.

## 6. Sharpness and source-valid failure of the stronger count claim

The numerical constants in Theorem 4.1 are sharp already on three vertices. For the poset with only `a<z` and `b` incomparable to both, there are exactly three extensions and

`Pr(a<b)=2/3`.

Therefore the closed interval `[1/3,2/3]` cannot be improved by the one-distinguisher hypothesis.

More importantly, the named partner's exact eight-element witness shows that the new structural count `>=2` cannot be upgraded to `>=3` from distinguisher count alone. Its relation generators are

`0<2, 0<5, 1<2, 1<3, 1<6, 2<4, 3<4, 3<5, 5<7, 6<7`.

It has exactly `121` linear extensions. The sibling pair `(3,6)` has exactly the two distinguishers `{4,5}` and

`Pr(3<6)=82/121>2/3`.

The poset itself is not a POS3 counterexample; as the partner report records, it has a balanced escape pair. Thus this refutes only the stronger local statement “an extreme pair must have at least three distinguishers,” not the parent target.

## 7. Exact regression computation

The companion standard-library verifier does three things:

1. exhaustively checks the fiber inequality `B_tau=C_tau` and `D_tau<=C_tau` for `798` interval-parameter triples in a broad finite regression range;
2. checks the three-element equality example `Pr(a<b)=2/3` exactly;
3. reconstructs the partner's 121-extension witness, verifies `Pr(3<6)=82/121`, and verifies that its distinguisher set is exactly `[4,5]`.

Recorded output:

```
gap_parameter_cases 798
one_distinguisher_tight 3 2 2/3
partner_witness 121 82 82/121 distinguishers [4, 5]
POS3_ONE_DISTINGUISHER_BALANCE_REGRESSION_PASS
```

The arbitrary-size theorem is proved symbolically in Section 4; this computation is regression/tightness evidence only.

## 8. New exact residual

The parent problem remains open. The first missing implication is now more constrained than in the preceding B10 run:

> **Two-flow / two-distinguisher span implication.** At the first strong-majority boundary of a cardinality-minimal width-three counterexample, combine the two active Hasse-cover deletion-flow channels with the at least two distinct delayed blocker-sibling distinguishers after `B_2`. Show that propagation to the next adjacent strong-majority boundary forces at least one of: a balanced incomparable pair; four mutually incomparable vertices; or a proper autonomous nonchain.

Any proof of this implication must retain the exact extension multiplicities. A statement confined to one fork, one distinguisher, or one deletion fiber is already ruled out by the team's exact adversaries.

A natural next attack is to classify the two delayed distinguishers by their four possible one-sided relation types to `s_1,s_2`, then couple those types to the two positive endpoint defect channels. Theorem 4.1 removes the entire one-distinguisher branch before that case analysis starts.

## 9. Provenance and limits

Outcome is `ESSENTIAL_STEP_APPLIED`, not `FULL_PROOF_CANDIDATE`. No claim of novelty or priority is made. No finite census is promoted to arbitrary-size closure. No induced deletion law is treated as uniform.

A scoped privacy/provenance review found only mathematical definitions, source-bound peer identifiers, and exact finite relation data already present in the cited peer report. No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email, Drive data, paid model/API/Codex call, remote workflow, public posting, or permission change is included.
