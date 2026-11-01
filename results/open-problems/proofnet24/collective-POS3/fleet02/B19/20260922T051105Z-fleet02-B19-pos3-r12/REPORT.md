# POS3 fleet02/B19 — prime full-arity-three terminal adversary

**Run:** `20260922T051105Z-fleet02-B19-pos3-r12`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact source state consumed

The run used the active collective-open-problems reallocation and did no installation or benchmark work.

The latest complete campaign-lead report consumed was:

- fleet04/B10, `proofnet24/collective-POS3/fleet04/B10/20260922T041420Z-B10-POS3-r13/REPORT.md`;
- source commit `fdfdc6be6943abfdef73c950a71c528bf582c6e8`;
- report blob `6acb56ae36d1cf3c59af1b9d22cc1b0cb2f70f44`.

Its strict delayed-predecessor analysis closes the local majority-early/majority-late fork to a canonical incomparable pair with minority probability in `(1/6,1/3)` and leaves the global three-chain mass-amplification step open.

The named OTHER-account partner result actually applied was the newest complete fleet03/B10 report visible at the science base used by this run:

- fleet03/B10, `proofnet24/collective-POS3/fleet03/B10/B10-20260922T041731Z-pos3-r11/REPORT.md`;
- report blob `c2ccba77c8790e42710cfb9cb6ca609cab2c4989`.

It proves the exact first-element projection formula and the bounded-multiplicity core: under the actual projected law more than `80/81` of the mass has insertion multiplicity `W<=47`, while the genuine uniform source law has an even smaller tail. Its remaining `BW47-WICSL` problem is structural covariance transfer for an adaptively selected pair, not a replacement of the projected law by a uniform law.

I also used two compatible current selector/flux dependencies:

- fleet02/B10, `proofnet24/collective-POS3/fleet02/B10/20260922T044758Z-b10-r12-9941265a/REPORT.md`, blob `2dd9b8b5a1ff8dada78596279ed93fc2cea0b2c1`. Its defect/arity lemma improves the majority-late canonical terminal minority to at least `1/5`, because the exact negative blocker union has at most three canonical channels.
- fleet01/B19, `proofnet24/collective-POS3/fleet01/B19/20260922T044807Z-pos3-r11-b19/REPORT.md`, report blob `003d2bf0593cb55f11738f50d68509413bb8d234`. It gives the exact three-chain `F*G` flux recurrence and shows that a strong cover flip in a no-balanced poset needs at least two external distinguishers.

These inputs make the immediate adversarial question precise: can the majority-late `m=3` branch be removed locally, for example by connectedness, autonomous-primality, local no-balancedness, or support redundancy, so that the `1/5` arity bound can be replaced by the two-channel `1/4` bound before any genuinely global argument? The answer is no.

## 2. Compact conditional end-to-end route

Assume for contradiction that POS3 fails and take a cardinality-minimal counterexample `P`. The current route has two compatible interfaces.

1. The lead plus fleet02/B10 local selector produces a strict delayed-predecessor terminal pair. In the difficult majority-late polarity its minority `epsilon` is at least `1/5`, and the exact negative blocker mass is routed through one lower event and at most two upper events.
2. Independently, the named partner's first-element deletion analysis reduces the nonuniform induction problem to a `47`-bounded exact tilt on a `>80/81` projected-mass core. Closing that route requires a structural covariance/selection statement, not merely a bounded density ratio.
3. Fleet01/B19 expresses pair probabilities and probability drops as literal forward/backward edge flux in a three-chain ideal lattice.

A sufficient global completion would therefore show that a full three-channel majority-late terminal state cannot persist in a minimal no-balanced width-three poset: its blocker mass must force either a balanced pair, strict majority-span descent, a width-four antichain, a proper autonomous nonchain, or an adaptively selected pair entering the partner's central core band.

The first issue is whether the third local channel is only an artifact of a loose union bound. The construction below proves it is not. A width-three connected autonomous-prime poset can realize all three canonical channels with positive **unique** mass, while every incomparable pair in the five-vertex selector block is itself unbalanced.

## 3. Exact width-three adversary

Let `P*` have vertices

`{r,s,d,a,b,t,u,v,w,z}`

and transitive-reduction covers

`r<a, r<b,`

`s<t, s<w,`

`d<a, d<u, d<v,`

`a<w, a<z,`

`b<u, b<v, b<w,`

`t<u, t<z,`

`v<z`.

A three-chain cover is

`d<a<w`,
`s<t<u`,
`r<b<v<z`.

The set `{r,s,d}` is an antichain, so the width is exactly three. The incomparability graph is connected. Exhaustive checking of all nonempty proper subsets finds **zero** nontrivial autonomous subsets, so the core is autonomous-prime.

The exact uniform extension count is

`e(P*) = 1919`.

All claims in this report are checked by the saved exact enumerator; no random vectors, induced-law substitution, or sampling is used in the certificate.

## 4. It realizes the full majority-late arity-three state

Take the endpoint pair `a||b`. Its predecessor/successor differences are exactly

`Pred(b) = {r}`,
`Pred(a) = {r,d}`,
`D := Pred(a)\Pred(b) = {d}`,

and

`Succ(a) = {w,z}`,
`Succ(b) = {u,v,w,z}`,
`U := Succ(b)\Succ(a) = {u,v}`,
`M := Min(U) = {u,v}`.

Thus the current majority-late selector has its maximum local defect arity: one lower channel and **two** minimal upper channels.

Under the actual uniform law on all 1919 linear extensions,

`Pr(a<b) = 506/1919`,
`Pr(b<d) = 471/1919`,
`Pr(u<a) = 240/1919`,
`Pr(v<a) = 564/1919`.

All four are strictly below `1/3`. Hence this is already in the no-internal-span-descent numerical regime used by the current selector.

More strongly, every incomparable pair inside the five-vertex selector block `{d,b,a,u,v}` is unbalanced:

`Pr(d<b) = 1448/1919 > 2/3`,
`Pr(b<a) = 1413/1919 > 2/3`,
`Pr(a<u) = 1679/1919 > 2/3`,
`Pr(a<v) = 1355/1919 > 2/3`,
`Pr(u<v) = 25/101 < 1/3`.

So the local strong-majority orientation is coherent (in particular `d prec_* b prec_* a`, and `a` is strongly before both upper blockers), yet **there is no balanced escape pair anywhere inside the canonical five-vertex block**.

This is the key strengthening over a symmetric three-channel toy example: one cannot dismiss the third channel by saying that the two upper blockers themselves must already be balanced.

## 5. All three blocker channels carry indispensable exact mass

Define the three canonical negative blocker events

`E_d = {b<d}`,
`E_u = {u<a}`,
`E_v = {v<a}`.

Here the opposite-sign predecessor and successor differences are empty, so the negative blocker identity is especially clean. Exact enumeration gives

`Pr(E_d union E_u union E_v) = 907/1919`

and

`907/1919 = 1 - 2*(506/1919) = 1 - 2 Pr(a<b)`.

The event-pattern counts, with bits ordered as `(a<b,E_d,E_u,E_v)`, are

`0000: 506`,
`0001: 276`,
`0010: 60`,
`0011: 100`,
`0100: 253`,
`0101: 138`,
`0110: 30`,
`0111: 50`,
`1000: 506`.

In particular each blocker has positive mass **not covered by either of the other two**:

`E_d only: 253/1919`,
`E_u only: 60/1919`,
`E_v only: 276/1919`.

Therefore no two of the three canonical channels capture the exact blocker union. This is not a bookkeeping artifact caused by overlapping labels: the third channel is support-essential in the actual uniform extension law.

Consequently the current `m=3` branch cannot be replaced by `m<=2` using only any combination of:

- width at most three;
- connectedness of the incomparability graph;
- absence of nontrivial autonomous subsets;
- the strict predecessor-nested majority-late geometry;
- absence of a balanced pair inside the five-vertex selector block; or
- deletion of a channel that is supposedly redundant in the blocker union.

A proof that upgrades the local `1/5` threshold must use genuinely nonlocal information.

## 6. This is not a POS3 counterexample

The verifier checks **all 21 incomparable-pair probabilities**. Exactly seven are balanced:

`Pr(r<s)=1173/1919`,
`Pr(r<d)=1195/1919`,
`Pr(s<d)=953/1919`,
`Pr(a<t)=905/1919`,
`Pr(u<w)=51/101`,
`Pr(u<z)=1242/1919`,
`Pr(w<z)=65/101`.

Thus `P*` supports POS3 rather than refuting it. The point is sharper and local: the balanced escape is forced to occur **outside** the canonical five-vertex terminal block in this example.

This matters for the current proof architecture. A local selector that sees only `{d,b,a,u,v}` cannot close the branch, even after prime reduction and exact support accounting. The external vertices `r,s,t,w,z` carry the escape geometry that any successful global argument must exploit.

## 7. Arbitrary-size ordinal padding

For any `L,R>=0`, form

`C_L oplussum P* oplussum C_R`,

where the added prefix/suffix chains are totally below/above `P*`. The width remains three, every incomparable pair lies inside the `P*` block, and every internal linear-extension probability is unchanged because every full extension is the forced concatenation of the prefix, one extension of `P*`, and the suffix.

Hence the full-arity-three obstruction persists at arbitrarily large finite sizes. It is not a finite-census boundary effect. (The padded posets are intentionally not claimed autonomous-prime; the unpadded ten-vertex core is.)

## 8. Application of the named partner result

The named partner's `BW47-WICSL` reduction says that the exact first-element projected law has a `>80/81` core on which the insertion weight is an integer in `1..47`; a bounded density ratio alone is explicitly insufficient, so one must control structural covariance for an adaptively selected pair.

The new adversary identifies the complementary obstruction on the lead/selector side. Even after the strongest local simplifications available here, three canonical defect events can all be necessary and their entire five-vertex block can remain unbalanced. Therefore a combined proof cannot close by either

- bounded-weight numerics alone, or
- local arity compression alone.

It must connect **external three-chain flux** to the partner's **bounded-weight covariance** or to another genuinely global monotone quantity.

A source-valid next lemma can be stated as follows.

> **Full-arity-three global escape.** In a cardinality-minimal no-balanced width-three candidate, take a majority-late terminal state with `D={d}` and two minimal upper blockers `M={u,v}` after span descent is exhausted. If all three exact blocker channels have positive unique mass, prove that the three-chain `F*G` flow outside `{d,b,a,u,v}` forces either (i) a balanced external pair, (ii) a strict strong-majority span descent, (iii) a width-four antichain, (iv) a proper autonomous nonchain, or (v) an adaptively selected deletion-core pair in the partner's central band `[28/81,53/81]`.

The present witness proves that the words **outside `{d,b,a,u,v}`** are essential: removing them makes the proposed statement false as a local claim.

That is the first essential missing implication after this run.

## 9. Exact executable certificate

Authoritative verifier:

`verify_prime_full_arity3_adversary.py`

Git blob: `5f3c3f08f62e4477395e7acd1fe792d984fd37ef`  
SHA-256: `92a7879fd51398b5db12bae91cb083337fd9ee9ac5e345a6882f92a8bde96c97`

Authoritative output:

`verify_prime_full_arity3_adversary.out`

Git blob: `02f66c49a6351851af6c31f7fd8ff77a6cce93b1`  
SHA-256: `1a545f0383463a00ac03f39e5da98b443b29cd89fa243507faf3cd3cbd7fd1f7`

Terminal marker:

`POS3_PRIME_FULL_ARITY3_ADVERSARY_PASS`

The script independently constructs the transitive closure from the displayed Hasse covers, enumerates all 1919 uniform linear extensions, certifies the width-three cover and antichain, checks connectedness and every proper subset for autonomy, verifies the exact selector sets and blocker event-pattern counts, and prints every incomparable-pair probability.

The exploratory search that located the core is not used as proof and is not assigned closure credit; every reported mathematical assertion is rechecked from the explicit finite poset by the saved exact verifier.

## 10. Status

- POS3: **OPEN / NOT PROVED**.
- Full majority-late arity `m=3` realizable in width three: **VERIFIED**.
- Same with connected incomparability graph: **VERIFIED**.
- Same with no proper nontrivial autonomous subset: **VERIFIED**.
- Same with every incomparable pair in the canonical five-vertex selector block unbalanced: **VERIFIED**.
- Every one of the three canonical blocker channels has positive unique actual-law mass: **VERIFIED**.
- Local `m=3 -> m<=2` support compression under those hypotheses: **REFUTED**.
- Parent theorem or global full-arity-three escape lemma: **NOT PROVED**.

No finite census is claimed as a proof of the arbitrary-size target. No induced distribution is relabelled uniform. No benchmark gold, credentials, scheduler identifiers, machine paths, raw private transcripts, email, Drive data, public posting, paid model/API/Codex, remote workflow, permission change, or production-brain mutation was used.
