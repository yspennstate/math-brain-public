# POS3 fleet01/B10 — TP2 amplification of canonical reverse channels

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run continues `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. It does no superseded installation or benchmark work. All probabilities below are under the **uniform law on the full set of linear extensions of the original poset**.

## 1. Exact collective state consumed

The latest complete campaign-lead result read this run is

- **fleet04/B10**, `proofnet24/collective-POS3/fleet04/B10/20260922T041420Z-B10-POS3-r13/REPORT.md`, blob `6acb56ae36d1cf3c59af1b9d22cc1b0cb2f70f44`.

It proves that, in the inherited first-fork strict delayed-predecessor corridor, once strong-majority span descent is exhausted, one obtains a canonical incomparable pair with minority probability in `(1/6,1/3)`. In the majority-late subbranch with endpoint minority at most `1/6`, it forces exactly two Hasse-successor blockers and a width-three bridge. Its first global unpaid implication is to amplify the local `1/6` mass toward `1/3` using exact three-chain flux rather than another local counting surrogate.

The required named **OTHER-account partner** result consumed and applied is

- **fleet02/B11**, `proofnet24/collective-POS3/fleet02/B11/20260922T035147Z-b11-pos3-r14-931012ae/REPORT.md`, blob `0d3bc896c83f0f37c8cc46bb46e61799ebfdd49a`.

For every width-three nested endpoint `a||b` with `Pred(b) subseteq Pred(a)`, it defines

`D=Pred(a)\Pred(b)`, `T=Max(D)`,
`S={z:b<z and z||a}`, `U=Min(S)`,

and proves the exact reverse-remainder decomposition

`R/E = Pr( union_{t in T}{b<t} union union_{u in U}{u<a} )`,      (1.1)

with `|T|<=2`, `|U|<=2`. Every `t in T` is a Hasse predecessor of `a`, every `u in U` a Hasse successor of `b`. For the endpoint identity, writing `p=Pr(a<b)` and `q=Q/E` for the normalized forward common-blocker count,

`p = 1-(q+r)/2`, where `r=R/E`.                                  (1.2)

Hence, since `q<=1`,

`r >= 1-2p`.                                                       (1.3)

In a hypothetical no-balanced counterexample in the majority-late/no-channel-span-descent orientation `b prec_* a`, every canonical channel in (1.1) has probability `<1/3`.

The same-slot exact flux input is

- **fleet01/B10**, `proofnet24/collective-POS3/fleet01/B10/20260922T024151Z-b10-pos3-r11b/REPORT.md`, blob `19b166fc7ab374365c098e88da1148a79da78de4`.

For any fixed three-chain cover and fixed element `x`, its exact two-coordinate full-extension flux matrix `W_x(s,t)` is TP2. Consequently the two other-chain prefix counts are positively quadrant dependent under the actual uniform full-extension law. In particular, for upper-tail coordinate events `A,B`,

`Pr(A intersect B) >= Pr(A)Pr(B)`.                                (1.4)

The present run applies (1.4) to the partner's canonical Hasse channels and gets a quantitative amplification that neither input alone gives.

## 2. Compact conditional end-to-end route

Assume POS3 is false and work in the inherited cardinality-minimal width-three counterexample with its transitive strong-majority order.

The current lead funnel reaches a strict nested endpoint or descends to a shorter extreme pair. The partner theorem then compresses every later nested endpoint, even after the predecessor discrepancy stops being a chain and successor nesting fails, to at most four canonical reverse channels. The previous B10 flux theorem supplies positive association **within each two-channel side** of this decomposition.

Thus the first missing implication attacked here is:

> Convert the partner's qualitative bounded-channel compression into a universal quantitative lower bound, strictly larger than `1/6`, on some canonical incomparable-pair minority probability.

The theorem below does this. It also gives substantially stronger constants in the first-fork chain-difference branch and in the partner's double-predecessor-fan obstruction.

## 3. Two-channel TP2 union inequality

### Lemma 3.1 — same-anchor canonical channels are positively associated

Let `x,y,z` be three pairwise incomparable elements of a width-at-most-three poset. Then

`Pr(y<x and z<x) >= Pr(y<x)Pr(z<x)`,                             (3.1)

and dually

`Pr(x<y and x<z) >= Pr(x<y)Pr(x<z)`.                             (3.2)

Consequently, if both event probabilities are at most `c`, then

`Pr({y<x} union {z<x}) <= 2c-c^2`,                              (3.3)

and likewise for the two events in (3.2).

#### Proof

Because `{x,y,z}` is a three-element antichain, in any partition of the poset into three chains these elements lie on three distinct chains. Fix `x` as the distinguished element in the exact B10 three-chain flux. The event `y<x` is an upper-tail event in the prefix coordinate of the chain containing `y`, and `z<x` is the corresponding upper-tail event in the other coordinate. The TP2/positive-quadrant inequality (1.4) gives (3.1). Equation (3.2) follows by using the two lower-tail coordinate events instead. Finally

`Pr(A union B)=Pr(A)+Pr(B)-Pr(A intersect B)`
`             <= Pr(A)+Pr(B)-Pr(A)Pr(B)`.

On `[0,c]^2` this expression is increasing in each argument, giving (3.3). `square`

Define for `j=0,1,2`

`F_0(c)=0`, `F_1(c)=c`, `F_2(c)=2c-c^2`.                        (3.4)

## 4. General four-channel amplification

At a partner nested endpoint let

`m=|T|`, `n=|U|`, so `0<=m,n<=2`.                               (4.1)

Suppose we are in the no-balanced majority-late/no-channel-span-descent branch. Thus

`p=Pr(a<b)<1/3`,                                                 (4.2)

and every atomic reverse-channel probability

`alpha_t=Pr(b<t)`, `t in T`,
`beta_u=Pr(u<a)`, `u in U`,                                     (4.3)

lies strictly below `1/3`.

### Theorem 4.1 — channel-count amplification

Let `c in (0,1/3)` satisfy

`1-2c = F_m(c)+F_n(c)`.                                         (4.4)

If the smaller root exists in `(0,1/3)`, then at least one of the endpoint or its canonical channel pairs has minority probability **strictly greater than `c`** and strictly less than `1/3`.

#### Proof

Assume contrariwise that

`p<=c`, `alpha_t<=c` for all `t in T`, `beta_u<=c` for all `u in U`.   (4.5)

The set `T` is an antichain and every `t in T` is incomparable with `b`. If `m=2`, Lemma 3.1 with anchor `b` gives

`Pr(union_{t in T}{b<t}) <= F_2(c)`;                            (4.6)

for `m=0,1` the same statement with `F_m` is immediate. Similarly, `U` is an antichain and every `u in U` is incomparable with `a`, so

`Pr(union_{u in U}{u<a}) <= F_n(c)`.                            (4.7)

Using only a union bound **between** the predecessor and successor channel groups,

`r <= F_m(c)+F_n(c) = 1-2c`.                                   (4.8)

But from the exact endpoint identity, (1.3),

`r >= 1-2p`.                                                     (4.9)

Every linear-extension probability is rational, whereas all three constants used below are irrational. Thus `p` cannot equal the chosen root `c`; under (4.5), actually `p<c`. Therefore

`r > 1-2c`,                                                      (4.10)

contradicting (4.8). Hence (4.5) is false. Since the poset is assumed to have no balanced pair, whichever endpoint/channel probability exceeds `c` is still `<1/3`. `square`

### Corollary 4.2 — universal general-nested constant

For the worst possible channel count `(m,n)=(2,2)`, solve

`1-2c = 4c-2c^2`.

The smaller root is

`c_22 = (3-sqrt(7))/2 = 0.1771243444677046...`.                  (4.11)

Because `F_m(c)+F_n(c)` is no larger for any `m,n<=2`, every majority-late/no-channel-span-descent nested endpoint in a hypothetical POS3 counterexample has a canonical incomparable pair with

`(3-sqrt(7))/2 < minority_probability < 1/3`.                    (4.12)

This improves the lead's `1/6` terminal scale **without assuming that the predecessor discrepancy remains a chain**.

## 5. Sharper constants for the actual surviving local shapes

The channel-count formula is more informative than the worst-case bound.

### Corollary 5.1 — first-fork chain-difference branch

In the lead's strict delayed-predecessor first-fork branch, `D` is a nonempty chain. Hence the partner set `T=Max(D)` has exactly one element, while `|U|<=2`. The worst channel count is therefore `(m,n)=(1,2)`.

Solving

`1-2c = c+(2c-c^2)=3c-c^2`

gives

`c_12 = (5-sqrt(21))/2 = 0.2087121525220801...`.                 (5.1)

Therefore the lead's unified majority-late strict-chain selector can be sharpened in this branch from

`1/6 < minority_probability < 1/3`

to

`(5-sqrt(21))/2 < minority_probability < 1/3`.                  (5.2)

This is an arbitrary-size statement under the original uniform extension law.

### Corollary 5.2 — double-predecessor fan

In the partner's successor-free hard state, `U=empty` and `|T|=2`. Thus

`1-2c = 2c-c^2`,

whose smaller root is

`c_20 = 2-sqrt(3) = 0.2679491924311227...`.                     (5.3)

Hence the partner's double-predecessor Hasse fan in a hypothetical no-balanced counterexample already contains a canonical incomparable pair with

`2-sqrt(3) < minority_probability < 1/3`.                       (5.4)

The same bound applies dually to a pure two-successor-channel state.

This is much closer to `1/3` than the generic `1/6` selector. It shows that the apparently difficult successor-free fan is quantitatively rigid rather than diffuse.

## 6. Why the TP2 step is source-valid

No deletion or quotient law appears in the proof. For the two predecessor channels `t_1,t_2`, the set `{b,t_1,t_2}` is a three-antichain; therefore they occupy three distinct chains in every three-chain cover, and the events `{b<t_i}` are literal coordinate upper tails of the exact full-extension flux `W_b`. For the successor channels `u_1,u_2`, `{a,u_1,u_2}` is a three-antichain, and `{u_i<a}` are coordinate upper tails of `W_a`.

Thus the only correlation inequality used is the previously proved TP2/PQD inequality for the **actual uniform full-extension measure**. No independence, no FKG property for unrelated events, and no cross-group positive association are assumed. The predecessor-group and successor-group bounds are combined only by the ordinary union bound.

## 7. Application to the partner's 33-extension local witness

The fleet02/B11 report gives the six-element width-three local witness

`0<1`, `0<5`, `1<3`, `1<4`, `2<3`,

with endpoint `(a,b)=(3,5)`. It has

`E=33`, `T={1,2}`, `U=empty`,
`Pr(a<b)=10/33`,
`Pr(b<1)=Pr(b<2)=9/33`,
`Pr(b<1 and b<2)=5/33`,
`R/E=13/33`.                                                     (7.1)

The TP2 prediction is exact here:

`5/33 > (9/33)^2`.                                               (7.2)

The pure-fan lower threshold `2-sqrt(3)` is approximately `0.267949`, while each channel has probability `9/33=3/11 approximately 0.272727`, so the witness lies just above the theorem's guaranteed channel scale. The poset itself is not a POS3 counterexample because `(1,2)` is balanced; this calculation is only a sharp local calibration of the new inequality.

## 8. What is now unpaid

Combining the lead and partner states with this run gives the following conditional architecture.

1. Span descent shortens the inherited strong-majority corridor whenever available.
2. Otherwise, every nested endpoint has at most four canonical reverse channels.
3. Exact TP2 prevents either same-anchor two-channel group from behaving as two disjoint rare events.
4. Consequently the generic terminal minority scale is not merely `1/6` but at least `c_22=(3-sqrt(7))/2`; in the first-fork chain branch it is at least `c_12=(5-sqrt(21))/2`; in the pure double-fan obstruction it is at least `c_20=2-sqrt(3)`.

The **first essential remaining implication** is now more specific:

> **Cross-group / consecutive-boundary amplification.** Use the exact three-chain path geometry to control overlap or transport between the predecessor-channel group and successor-channel group at consecutive nested boundaries. Either force enough additional overlap to raise the selector from the constants above to `1/3`, or prove that the worst `(2,2)` state cannot persist without a strict strong-majority span descent, ordinal/autonomous reduction, or balanced pair.

The current proof deliberately stops here. TP2 for one fixed anchor does not by itself control a predecessor event `{b<t}` against a successor event `{u<a}` with different anchors, so replacing the union bound between those groups by a positive-correlation claim would be unsupported.

## 9. Status and integrity

- fleet02/B11 general nested reverse-channel compression: **CONSUMED/APPLIED**.
- fleet04/B10 current `1/6` strict-corridor selector: **CONSUMED/APPLIED**.
- fleet01/B10 exact full-extension TP2/PQD flux: **CONSUMED/APPLIED**.
- same-anchor two-channel union inequality: **PROVED**.
- general nested-endpoint selector above `(3-sqrt(7))/2`: **PROVED** under the inherited majority-late/no-channel-span-descent counterexample hypotheses.
- first-fork chain-difference selector above `(5-sqrt(21))/2`: **PROVED**.
- pure double-fan selector above `2-sqrt(3)`: **PROVED**.
- parent POS3 theorem: **OPEN / NOT PROVED**.
- outcome: `ESSENTIAL_STEP_APPLIED`.

Scoped privacy/provenance review: this report contains only mathematical statements and source-bound private-repository references. It contains no benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email/Drive content, paid model/API/Codex calls, remote workflows, public posting, permission changes, or production-brain mutation. No verified-brain claim is made.
