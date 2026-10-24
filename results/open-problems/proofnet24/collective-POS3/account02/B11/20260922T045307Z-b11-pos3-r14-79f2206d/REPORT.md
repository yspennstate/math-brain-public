# POS3 account02/B11 — double-fan reroute into the strict chain corridor

**Run:** `20260922T045307Z-b11-pos3-r14-79f2206d`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Inherited finite frontier:** `n_bal=14` (unchanged).  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

No installation or benchmark work was performed. All probabilities below are under the original uniform law on the full set of linear extensions of the stated poset. Finite enumeration is used only as regression/adversarial evidence for analytic statements, never as arbitrary-size closure.

## 1. Exact source-bound state consumed

The latest complete campaign-lead report consumed is

- account04/B10, `proofnet24/collective-POS3/account04/B10/20260922T041420Z-B10-POS3-r13/REPORT.md`, blob `6acb56ae36d1cf3c59af1b9d22cc1b0cb2f70f44`.

Its Theorem 4.1 proves the **direct 1/6 selector** in a strict predecessor-chain corridor: once internal strong-majority span descent is exhausted, either the endpoint itself or a canonical blocker pair has minority probability strictly in `(1/6,1/3)`. Its explicit remaining obligation is a global amplification/charge theorem; it also records non-chain strict predecessor-difference exits as a separate unpaid branch.

The named partner result actually consumed is

- account03/B19, `proofnet24/collective-POS3/account03/B19/20260922T040111Z-b19-pos3-r11/REPORT.md`, blob `eb9cf8999ab3d4e9327a141abb1e5dd0e618244f`.

For consecutive exact-two crossed lower-fringe states it proves, without uniformizing a deletion skeleton, the transfer invariant `K=A+Z` and recurrence

`A_(i-1) + 3 A_i + A_(i+1) = E + K`.                         (1.1)

The other-account structural dependency used essentially is

- account01/B11, `proofnet24/collective-POS3/account01/B11/20260922T031426Z-b11-pos3-r11/ADDENDUM_STRONGER_NESTING.md`, blob `4813f489bd0c54deda662f70b2027bf4ac866472`.

It proves that if `a||b`, `Pred(b) subseteq Pred(a)`, `a lessdot u`, `a lessdot v`, and the fork siblings `u,v` are pairwise incomparable and each incomparable with `b`, then `Pred(u)` and `Pred(v)` are nested. Its main report, blob `3481fa66f303337da62a0a1c8ca0f0a7b5dd610b`, gives a finite clean-fork funnel: an equal-predecessor extreme pair either descends in strong-majority span or, after finitely many clean fork escalations, exits to strict predecessor nesting.

The immediately previous account02/B11 result compressed an arbitrary width-three nested endpoint to at most four reverse Hasse channels and exposed one successor-free obstruction: a **double-predecessor fan** consisting of two incomparable Hasse predecessors of the larger-predecessor endpoint, both incomparable with the other endpoint. The present run attacks that obstruction.

## 2. Compact conditional end-to-end route

Assume POS3 false and work inside the inherited cardinality-minimal no-balanced width-three candidate with transitive strong-majority order.

Earlier reductions make both the comparability and incomparability graphs connected and remove the ordinal/parallel decomposable cases. The account01/B11 funnel reaches strict nesting; the lead turns a strict **chain-difference** corridor into a canonical `(1/6,1/3)` minority charge. The previous B11 reverse-channel theorem showed that when later predecessor nesting is not a chain, the only successor-free no-descent obstruction is a double-predecessor fan.

The missing structural question was therefore:

> can the double-predecessor fan terminate the transport in a genuinely new local geometry, or must it re-enter a chain-difference corridor (possibly after strict span descent)?

Sections 3-5 show that it cannot be terminal. The key strengthening is that strict fork-sibling nesting automatically has a **chain** difference, not merely a nested difference. By order duality this reroutes every successor-free double-predecessor fan into either strict span descent or a strict successor-chain corridor. The lead's selector then applies in the dual order, while exact-two continuations inherit the partner's recurrence (1.1).

The global 1/6-to-1/3 amplification remains open.

## 3. New fork-sibling chain-difference lemma

### Theorem 3.1 — strict fork siblings have chain difference

Let `P` have width at most three. Suppose

- `a||b`,
- `Pred(b) subseteq Pred(a)`,
- `a lessdot u` and `a lessdot v`,
- `u||v`, `u||b`, and `v||b`.

Then `Pred(u)` and `Pred(v)` are nested, and, **if the nesting is strict, the proper difference is a chain**.

More explicitly, after possibly exchanging `u,v`, if

`Pred(v) proper_subset Pred(u)`,                               (3.1)

then

`Pred(u) \ Pred(v)`                                           (3.2)

is a nonempty chain.

#### Proof

Nesting itself is the account01/B11 stronger fork-sibling lemma. Assume (3.1) and put `D=Pred(u)\Pred(v)`.

Take arbitrary `d in D`.

First `d||a`. If `d<a`, then `d<a<v`, so `d in Pred(v)`, contradiction. If `a<d<u`, this contradicts the cover `a lessdot u`. Thus `d||a`.

Next `d||b`. If `d<b`, then `d in Pred(b) subseteq Pred(a)`, contradicting `d||a`. If `b<d<u`, then `b<u`, contradicting `b||u`.

Finally `d||v`: the relation `d<v` contradicts `d notin Pred(v)`, while `v<d<u` contradicts `v||u`.

Hence **every** member of `D` is incomparable with both `b` and `v`. If two members `d,e in D` were incomparable, then

`{b,v,d,e}`

would be a four-element antichain, impossible at width at most three. Therefore all members of `D` are pairwise comparable, so `D` is a chain. `QED`

### Dual form

Under order duality:

- if `a||b`, `Succ(b) subseteq Succ(a)`,
- `u lessdot a` and `v lessdot a`,
- `u||v`, `u||b`, `v||b`,

then `Succ(u),Succ(v)` are nested, and any strict successor-set difference is a chain.

This is stronger than the nesting statement alone and is exactly the geometry required by the lead's strict-chain selector after dualization.

## 4. Successor-free double-predecessor fans are not terminal

Let `a||b` satisfy

`Pred(b) proper_subset Pred(a)`.                              (4.1)

Put

`D=Pred(a)\Pred(b)`, `T=Max(D)`.                             (4.2)

Assume the previous B11 successor-free obstruction:

`T={t_1,t_2}`,                                               (4.3)

and

`S={z:b<z and z||a}=empty`.                                 (4.4)

The previous reverse-channel theorem already gives

`t_1 lessdot a`, `t_2 lessdot a`, `t_1||t_2`, and `t_i||b`.   (4.5)

### Lemma 4.1 — the companion successor inclusion

Condition (4.4) implies

`Succ(b) subseteq Succ(a)`.                                   (4.6)

Indeed, if `b<z`, then (4.4) says `z` is comparable with `a`. The relation `z<a` would force `b<a`, impossible, so `a<z`.

### Theorem 4.2 — double-fan dual-chain reroute

Under (4.1)-(4.4), the successor sets of `t_1,t_2` are nested. If they are unequal, their proper difference is a nonempty chain.

#### Proof

Apply the dual form of Theorem 3.1 using (4.5) and the inclusion (4.6). This gives nested successor sets and the chain conclusion for a strict difference. `QED`

There is also a direct width-three proof of the chain part that is useful for intuition. Suppose

`Succ(t_2) proper_subset Succ(t_1)`

and let `V=Succ(t_1)\Succ(t_2)`. For `z in V`, one has `z||t_2`: `t_2<z` is excluded by definition and `z<t_2` together with `t_1<z` would force `t_1<t_2`. Also `z||b`: if `z<b`, then `t_1<z<b` contradicts `t_1||b`; if `b<z`, then (4.6) gives `a<z`, whence `t_2<a<z`, contradicting `z notin Succ(t_2)`. Thus any two incomparable members of `V`, together with `b,t_2`, would form a four-antichain. Hence `V` is a chain.

### Corollary 4.3 — finite reroute in a no-balanced candidate

In the inherited no-balanced strong-majority setting, a successor-free double-predecessor fan yields one of the following after finitely many source-valid structural steps:

1. a strict strong-majority span descent; or
2. a strict **successor-nested pair whose proper successor difference is a chain**.

Proof: if `Succ(t_1) != Succ(t_2)`, Theorem 4.2 gives outcome 2 immediately. If the successor sets are equal, pass to the order-dual poset. The pair `t_1,t_2` is then a clean equal-predecessor extreme pair after orienting it by the dual strong-majority order. Apply account01/B11 Theorem 5.1. Its finite clean-fork funnel either takes a strict span descent or exits through strict fork-sibling predecessor nesting. In the latter case Theorem 3.1 upgrades that exit to a **chain** predecessor difference in the dual, hence a chain successor difference in `P`. `QED`

Thus the double-predecessor fan is no longer an independent terminal obstruction.

## 5. Applying the latest lead and the named partner

### 5.1 Lead r13 applies after dual rerouting

Take outcome 2 of Corollary 4.3 and pass to the order dual. It is precisely a strict predecessor-nested endpoint with nonempty **chain** predecessor difference. The no-balanced property and the uniform extension law are invariant under reversal of every linear extension; strong-majority span is merely reversed.

Therefore account04/B10 r13 Theorem 4.1 applies verbatim in the dual order:

- if there is an internal strong-majority span descent, that is structural progress;
- otherwise a canonical incomparable pair has minority probability strictly in `(1/6,1/3)`.

In its small-minority subbranch the dual statement produces exactly two Hasse **predecessor** blockers.

So the old double-fan obstruction feeds the same quantitative `>1/6` charge regime as the primal strict predecessor corridor.

### 5.2 Partner r11 exact-two recurrence also dualizes

Now suppose a rerouted strict successor-chain corridor enters the partner's consecutive **exact-two crossed** subclass. Reverse every full linear extension. This is a bijection from `L(P)` to `L(P^op)` and preserves the total count `E`; it transforms upper-fringe exact-two continuation in `P` into the lower-fringe exact-two continuation of account03/B19.

Consequently the partner's skeleton-by-skeleton transfer identity applies without any induced-law substitution. After the natural dual relabeling, the same integer `K` is conserved and the endpoint minority counts satisfy

`A_(i-1) + 3 A_i + A_(i+1) = E + K`.                         (5.1)

Thus the double-fan branch, once it enters exact-two continuation, is governed by the same rigid second-order transport already proved by the named partner; it does not create a new uncontrolled probability law.

This is a direct application of account03/B19 r11, not merely a citation.

## 6. Source-valid adversary to a stronger local shortcut

The new reroute must not be overstated as “the double fan itself contains a balanced pair.” That stronger claim is false even under both complementary-graph connectivity conditions.

Take the nine-element poset on `0,...,8` with transitive-reduction covers

`(0,4),(1,2),(2,3),(3,4),(3,7),(4,8),(4,5),(6,8)`.           (6.1)

It has width exactly three, connected comparability graph, connected incomparability graph, and exactly

`E=243`

linear extensions.

For

`a=8`, `b=7`, `T={4,6}`,                                   (6.2)

one has

`Pred(b)={1,2,3}`,  
`Pred(a)={0,1,2,3,4,6}`,  
`Succ(a)=Succ(b)=empty`,                                      (6.3)

so this is exactly a successor-free double-predecessor fan. Exact uniform counts are

`Pr(a<b)=76/243 < 1/3`,                                      (6.4)

`Pr(b<4)=75/243 = 25/81 < 1/3`,                              (6.5)

`Pr(b<6)=43/243 < 1/3`,                                      (6.6)

`Pr(4<6)=63/243 = 7/27 < 1/3`.                               (6.7)

Thus the endpoint and all three pairs inside the fan are unbalanced. The reverse-channel union has

`Pr((b<4) OR (b<6))=91/243`,                                 (6.8)

and checks the exact endpoint defect

`91 = E - 2*76`.                                               (6.9)

Nevertheless

`Succ(6)={8} proper_subset Succ(4)={5,8}`,                (6.10)

with chain difference `{5}`, exactly as Theorem 4.2 predicts. The rerouted pair `(4,6)` already has minority `7/27`, which lies in the lead's `(1/6,1/3)` selector window.

The poset is not a POS3 counterexample: for example

`Pr(0<2)=114/243=38/81`

is balanced. The example therefore refutes only the tempting **local fan-balance** shortcut, while supporting the necessity of rerouting to global charge.

## 7. Exact regression

`verify_double_fan_dual_corridor_v1.py` exhaustively checks every distinct naturally labelled transitively closed poset through order six and every width-at-most-three instance of the hypotheses above.

The run checked:

- `5230` naturally labelled transitive posets for `2<=n<=6`;
- `3701` with width at most three;
- `2011` fork-sibling configurations satisfying Theorem 3.1's hypotheses;
- `825` strict fork-sibling nestings, all `825` with chain proper difference;
- `1581` successor-free double-predecessor fan states;
- `892` with equal successor sets;
- `689` with strict successor nesting, all `689` with chain proper difference.

It then exactly enumerates the 243 extensions of (6.1) and verifies (6.2)-(6.10), both graph connectivities, and a balanced global escape.

Verifier SHA-256: `77c21353109f98a4b2ec83adb8965f3327a1009238310832deac97cb2445ca5a`  
Captured stdout SHA-256: `27792046b7aa86d436f822198bfd12c3795a90958660f54f1f0e9fe56b66fd20`  
Terminator: `POS3_DOUBLE_FAN_DUAL_CORRIDOR_V1_PASS`.

These counts are regression evidence only. Theorems 3.1 and 4.2 are analytic and arbitrary-size.

## 8. What is now genuinely unresolved

This run removes the **successor-free double-predecessor fan as an independent terminal geometry**.

After the inherited ordinal/parallel reductions and the current local reroute, the surviving transport can be organized as:

1. strict strong-majority span descent; or
2. a primal strict predecessor-chain corridor; or
3. a dual strict successor-chain corridor.

After span descent is exhausted, the latest lead theorem supplies a canonical minority charge in `(1/6,1/3)` in either orientation. On exact-two consecutive subruns, the named partner recurrence (5.1) controls the charge propagation exactly.

The first essential unpaid implication is therefore a genuinely **global amplification/conservation statement**:

> show that primal/dual `(1/6,1/3)` corridor charges, together with their exact-two recurrence where applicable, cannot propagate through all remaining multi-distinguisher exits without either overlapping enough to force minority at least `1/3`, producing another strict span descent, or triggering an already excluded ordinal/parallel reduction.

The 243-extension adversary above shows that a fan-local balance theorem is false; the partner's 833-extension four-corridor witness shows that a fixed short termination bound is false. The missing step must use global three-chain/cumulative-band flux rather than another local cutoff.

## 9. Status and integrity

- Fork-sibling strict difference is a chain: **PROVED**.
- Dual fork-sibling strict difference is a chain: **PROVED**.
- Successor-free double-predecessor fan reroutes to span descent or a dual strict-chain corridor: **PROVED** using the account01/B11 finite clean-fork funnel.
- Latest lead r13 `(1/6,1/3)` selector applied to the rerouted branch: **APPLIED BY ORDER DUALITY**.
- Named partner account03/B19 exact-two invariant/recurrence applied to dual exact-two continuations: **APPLIED BY ORDER DUALITY**.
- Stronger “the fan itself must contain a balanced pair” shortcut: **REFUTED** by the exact 9-point witness.
- POS3: **OPEN / NOT PROVED**.
- Run classification: `ESSENTIAL_STEP_APPLIED`.

Scoped privacy/provenance review: the scientific artifacts contain only mathematical statements, source-bound repository references, deterministic verifier code/output, nonsecret run labels, and aggregate operational provenance. No credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, benchmark material, email/Drive content, paid model/API/Codex calls, remote workflows, public posting, permission changes, or brain mutation were used.
