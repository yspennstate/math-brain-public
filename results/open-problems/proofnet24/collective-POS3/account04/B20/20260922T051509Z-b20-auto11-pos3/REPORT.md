# POS3 account04/B20 — static cross-group correlation shortcut is false

**Run:** `20260922T051509Z-b20-auto11-pos3`  
**Outcome:** `CANDIDATE_REFUTED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair with ordering probability in `[1/3,2/3]` under the uniform law on all linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

No superseded brain-installation or benchmark work was performed. All probabilities below are under the uniform law on the full set of linear extensions of the displayed poset.

## 1. Exact collective state consumed

The current campaign-lead report consumed is account04/B10

`proofnet24/collective-POS3/account04/B10/20260922T041420Z-B10-POS3-r13/REPORT.md`, blob `6acb56ae36d1cf3c59af1b9d22cc1b0cb2f70f44`.

It proves the direct strict-chain terminal selector: after strong-majority span descent is exhausted, a canonical endpoint or blocker pair has minority probability in `(1/6,1/3)`. Its remaining task is global amplification/charging, not another local selector.

The required named OTHER-account result consumed and applied is account01/B19

`proofnet24/collective-POS3/account01/B19/20260922T044807Z-pos3-r11-b19/REPORT.md`, blob `003d2bf0593cb55f11738f50d68509413bb8d234`.

It gives the exact three-chain `F*G` cover-flux recurrence and proves that a strong cover flip must have at least two external relation witnesses. Its first unpaid implication is a two-witness flux charging theorem; mere witness counting is explicitly insufficient.

A directly relevant newer OTHER-account input is account01/B10

`proofnet24/collective-POS3/account01/B10/20260922T045216Z-account01-B10-pos3-r11/REPORT.md`, blob `7ab3502e574d795c8300fd0ec70dc33f12b87f0a`.

It uses the previously proved TP2 of the exact full-extension three-chain flux to obtain positive association **within** a two-channel predecessor group or **within** a two-channel successor group. It deliberately leaves predecessor-versus-successor cross-group overlap unpaid and warns that positive correlation across different anchors has not been proved.

The present run attacks the strongest natural static completion of that missing step and refutes it exactly.

## 2. The candidate being tested

At a strict nested endpoint let

- `a || b`,
- `Pred(b) proper_subset Pred(a)`,
- `D = Pred(a) \ Pred(b)` be a chain with top `d`,
- `Succ(a) subset Succ(b)`, and
- `U = Min(Succ(b) \ Succ(a))` be the canonical upper blockers.

The tempting cross-group completion is:

> for every `u in U`, the reverse-channel events
> `L={b<d}` and `R_u={u<a}` are non-negatively correlated under the full uniform extension law,
> i.e.
> `Pr(L intersect R_u) >= Pr(L)Pr(R_u)`.

If true, this would let one combine the account01/B10 same-anchor TP2 bounds with a direct cross-group overlap lower bound. The claim is false, even in a structurally clean width-three state with all local canonical pairs still unbalanced in the expected direction.

## 3. Exact nine-element counterexample

Let `P` have vertices `0,...,8` and transitive-reduction covers

`0<1, 0<5, 1<2, 2<6, 3<4, 3<5, 4<6, 4<7, 4<8, 5<8`.

It has exactly

`E=e(P)=482`

linear extensions. Its width is exactly three: `{1,4,5}` is an antichain, while

`[0<1<2<6]`, `[3<4<7]`, `[5<8]`

is a three-chain cover. Both the comparability and incomparability graphs are connected. The only proper nontrivial autonomous set is the chain `{1,2}`; in particular there is no proper autonomous nonchain.

Take

`a=5, b=4, d=0, u_1=6, u_2=7`.

Then

`Pred(b)={3}`,
`Pred(a)={0,3}`,
so `D={0}` is a singleton chain and `d=0` is a Hasse predecessor of `a`.

Also

`Succ(a)={8}`,
`Succ(b)={6,7,8}`,
so the canonical minimal upper blockers are exactly `U={6,7}`; both `4<6` and `4<7` are covers.

The endpoint and every canonical reverse channel are on the strict minority side:

`N(a<b)=154`,
`N(b<d)=70`,
`N(u_1<a)=50`,
`N(u_2<a)=116`.

Since `E/3=160+2/3`, all four probabilities are strictly below `1/3`. Thus this is not a failure caused by one of the local canonical pairs already being balanced.

## 4. Cross-group positive association fails

For the lower channel `L={4<0}` and the first upper channel `R_6={6<5}`, exact enumeration gives

`N(L)=70`,
`N(R_6)=50`,
`N(L intersect R_6)=7`.

Hence

`N(L intersect R_6) E - N(L)N(R_6)`
`= 7*482 - 70*50`
`= -126 < 0`.

Equivalently,

`Pr(4<0 and 6<5) < Pr(4<0) Pr(6<5)`.

So the two canonical groups can be **negatively** correlated even though the poset has width three, the predecessor discrepancy is a singleton chain, the endpoint and all canonical channels are unbalanced in the hard-branch direction, both graph-connectivity reductions hold, and there is no proper autonomous nonchain.

This is therefore a direct source-valid counterexample to replacing the missing consecutive-boundary transport theorem by a one-boundary cross-group FKG/TP2 assertion.

## 5. The existing blocker identity remains exact

The counterexample does not break the exact local blocker decomposition. The remaining intersections are

`N(L intersect R_7)=30`,
`N(R_6 intersect R_7)=30`,
`N(L intersect R_6 intersect R_7)=5`.

Thus

`N(L union R_6 union R_7)`
`=70+50+116-7-30-30+5`
`=174`.

And indeed

`174 = E - 2 N(a<b) = 482 - 2*154`.

So the failure is precisely in trying to force **additional cross-group overlap** beyond the exact union identity. The account01/B10 use of a plain union bound between predecessor and successor groups was therefore not merely cautious; without further global information it is necessary.

## 6. This is not a POS3 counterexample

The poset has several balanced escape pairs. Exact counts include

- `N(0<3)=248`,
- `N(1<4)=252`,
- `N(2<5)=174`,
- `N(2<7)=312`,
- `N(6<8)=210`,
- `N(7<8)=299`,

all out of `482`, hence all in `[1/3,2/3]` after choosing the displayed orientation.

Therefore nothing here refutes POS3. What it refutes is the local cross-group correlation shortcut inside the current proof architecture.

## 7. Consequence for the next proof step

The first unpaid implication is now sharper.

A successful amplification cannot be a static theorem saying that a predecessor reverse channel and a successor reverse channel are always positively associated, even after imposing the current width-three, strict-chain, graph-connected, no-proper-autonomous-nonchain, locally-unbalanced geometry.

The next viable route has to use information that this nine-element state does **not** encode locally: specifically the account01/B19 exact `F*G` transport across consecutive cover boundaries, the account03/B19 conserved-`K` recurrence when exact-two witnesses persist, or the global minimal-counterexample/strong-majority corridor constraints that force a balanced escape elsewhere. In particular, the object to control is not static cross-group covariance at one endpoint but **how blocker mass is transported from one canonical boundary to the next**.

That is a genuine narrowing of the two-witness charging problem and prevents the team from spending further runs trying to extend same-anchor TP2 to different anchors without extra hypotheses.

## 8. Deterministic certificate and integrity

`verify_cross_group_adversary.py` reconstructs the transitive closure and counts all constrained linear extensions by exact ideal-state dynamic programming. It verifies width three, the explicit chain cover, both graph connectivities, all proper autonomous sets, the exact corridor discrepancy sets, all probability counts, the negative covariance numerator `-126`, the blocker-union identity, and the full balanced-escape list.

Recorded terminator:

`POS3_CROSS_GROUP_STATIC_CORRELATION_REFUTED_PASS`.

The finite computation is the proof of the explicit counterexample. No arbitrary-size theorem, finite-frontier advance, target-level closure, novelty/priority claim, or verified-brain use is asserted.

No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email/Drive content, paid model/API/Codex use, remote workflow, permission change, or public posting is included.
