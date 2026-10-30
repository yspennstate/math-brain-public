# POS3 fleet04/B10 — crossed-neighborhood union identity and width-three fringe selector

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status after this report:** **OPEN / NOT PROVED**.  
**Inherited finite frontier:** `n_bal=14` (unchanged).  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run continues `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. It performs no installation or benchmark work and does not claim novelty or priority.

## 1. Exact state consumed

The latest complete campaign-lead report consumed is

- fleet04/B10, `proofnet24/collective-POS3/fleet04/B10/20260922T031005Z-B10-POS3-r11/REPORT.md`, blob `b077c3fedba7e6e8ab72b683b5eafd8203005467`.

That report pays the first-fork lower-distinguisher nesting step. In the live strict branch the sibling predecessor sets are nested, their proper difference is a chain, and the branch either gives strict strong-majority span descent or continues through a canonical successor blocker.

The named OTHER-account partner result used as a proof dependency is

- fleet01/B11, `proofnet24/collective-POS3/fleet01/B11/20260922T021210Z-b11-pos3-exchange-r11/REPORT.md`, blob `5fdf6f70d35fee1011b67c217b9e177fb197e81a`.

Its Theorem 3.1 states that for incomparable `(a,b)` with `Pred(b) subseteq Pred(a)`, if `E=e(P)`, `Q` is the forward common-blocker count and `R` is the reverse nonneutral-blocker remainder, then

`p_ab = 1 - (Q+R)/(2E)`.

The second named OTHER-account result applied here is

- fleet02/B19, `proofnet24/collective-POS3/fleet02/B19/20260922T031214Z-fleet02-B19-pos3-r11/REPORT.md`, blob `53669a7baac8d3a37b45229448c1288bf7c0cf60`.

It gives the 15-point width-three module-prime adversary with `E=1810` and the sharp crossed pair `(3,13)` satisfying

`Pred(13)=Pred(3) union {12}`,

`Succ(3)=Succ(13) union {9}`,

`12<9`, and

`Pr(3<13)=1207/1810=2/3+1/5430`.

That report refutes any fixed positive margin above `2/3` based only on two-distinguisher local geometry. The derivation below identifies the exact count polynomial responsible for that one-count endpoint slack and then extracts the width-three pair-selection consequence that survives it.

## 2. Compact conditional end-to-end route

Assume POS3 false and take the inherited cardinality-minimal no-balanced width-three candidate with transitive strong-majority order `L_*`. The current first-fork funnel reaches an extreme incomparable pair with a strict chain of lower predecessor distinguishers. The next terminal exception is the **crossed-neighborhood branch**: after orienting the natural early endpoint as `x` and the late endpoint as `y`,

`Pred(x) subseteq Pred(y)` and `Succ(y) subseteq Succ(x)`.       (2.1)

The previous endpoint formula is one-sided and does not by itself expose the interaction between these lower and upper discrepancies. The first missing implication for this fixed branch is therefore:

> express the full majority defect of `(x,y)` only in terms of the actual lower/upper fringe crossings, then show width three either gives strict internal span descent or selects a new extreme fringe pair with a quantitative nonvanishing minority mass.

Sections 3–5 prove exactly that. The full target remains open because an outward fringe selector still has to be globally charged, and the successor sets need not always satisfy the crossed nesting (2.1).

## 3. Exact crossed-neighborhood union identity

Let `P` be any finite poset, not necessarily width three. Let `x||y` and assume (2.1). Put

`D = Pred(y) \ Pred(x)`,

`U = Succ(x) \ Succ(y)`.

Every `d in D` satisfies `d<y` and `d||x`; every `u in U` satisfies `x<u` and `u||y`.

Define full-extension events

`A_D = {there exists d in D with x preceding d}`,

`B_U = {there exists u in U with u preceding y}`.

All probabilities below are under the original uniform law on **all** linear extensions of `P`.

### Theorem 3.1 — crossed-neighborhood union identity

Under (2.1),

`2 Pr(x<y) - 1 = Pr(A_D union B_U)`.                            (3.1)

Equivalently, in exact counts with `E=e(P)` and `N_xy=#{L:x<y}`,

`2 N_xy - E = #{L:A_D union B_U}`.                             (3.2)

In particular `Pr(x<y)>=1/2`, with equality exactly when the fringe union is empty.

### Proof

Apply fleet01/B11 Theorem 3.1 with its endpoint labels `(a,b)=(y,x)`. Its predecessor hypothesis holds because `Pred(x) subseteq Pred(y)`.

For those labels the forward successor-blocker set is

`S_y(x)={z:y<z and z||x}`.

But `Succ(y) subseteq Succ(x)`, so `S_y(x)` is empty. Hence its minimal-blocker set is empty and its count `Q` is the vacuous count `E`. The partner identity becomes

`Pr(y<x) = 1 - (E+R)/(2E) = (E-R)/(2E)`,

so

`2 Pr(x<y)-1 = R/E`.                                          (3.3)

It remains only to identify `R`. In the partner theorem, `R` counts reverse-orientation extensions `x ... y` whose open endpoint interval is nonneutral. Under (2.1), an element can be nonneutral in that interval only in one of two ways:

1. it is a predecessor of `y` incomparable with `x`, hence belongs to `D`; or
2. it is a successor of `x` incomparable with `y`, hence belongs to `U`.

Conversely, in an extension with `x<y`, a fixed `d in D` lies in the open interval exactly when `x<d`, because `d<y` is forced; a fixed `u in U` lies in the interval exactly when `u<y`, because `x<u` is forced. Therefore the event counted by `R` is exactly `A_D union B_U`. Substitution into (3.3) proves (3.1) and (3.2). `□`

### Boundary cases

- If `D=U=empty`, then `Pr(x<y)=1/2`, so `(x,y)` is balanced immediately.
- If only one side is nonempty, the entire majority defect is exactly that one fringe union.
- No width, connectedness, minimality, or induced-uniformity assumption entered Theorem 3.1.

## 4. Width-three canonical fringe compression

Now assume `width(P)<=3`. Let `D_max` be the maximal elements of `D`, and `U_min` the minimal elements of `U`.

### Lemma 4.1 — only maximal lower and minimal upper distinguishers matter

`A_D = union_{d in D_max}{x<d}`,                               (4.1)

`B_U = union_{u in U_min}{u<y}`.                               (4.2)

Moreover

`|D_max|<=2` and `|U_min|<=2`.                                 (4.3)

### Proof

If `x<d` for some `d in D`, choose a maximal `d' in D` with `d<=d'`; then `x<d'`. This proves (4.1). Dually, if `u<y` for some `u in U`, choose a minimal `u' in U` with `u'<=u`; then `u'<y`, proving (4.2).

The elements of `D_max` are pairwise incomparable and each is incomparable with `x`, so `D_max union {x}` is an antichain. Width at most three gives `|D_max|<=2`. Likewise `U_min union {y}` is an antichain, proving the second bound. `□`

The inherited delayed-predecessor first-fork branch is stronger: its proper predecessor difference `D` is a nonempty chain. Hence there is a unique `d=max D`, and Theorem 3.1 compresses to at most three canonical fringe events,

`2 Pr(x<y)-1 = Pr( {x<d} union union_{u in U_min}{u<y} )`,      (4.4)

with `|U_min|<=2`.

This compression is independent of `|P|`; arbitrarily many noncanonical distinguishers do not create arbitrarily many endpoint charges.

## 5. First missing pair-selection implication: quantitative outward fringe

Assume now that `P` is a hypothetical no-balanced width-three candidate, `x prec_* y` in its transitive strong-majority order, the lower discrepancy `D` is the inherited nonempty chain, and (2.1) holds.

Suppose further that the current pair has reached the **no-internal-descent** branch: there is no incomparable strong-majority pair strictly inside the `L_*` interval from `x` to `y` produced by a canonical distinguisher.

Let `d=max D` and `M=U_min`.

Because `d<y` in the poset, `d prec_* y`. If `x prec_* d`, then `x prec_* d prec_* y` and `x||d`, giving the forbidden shorter extreme span. Therefore

`d prec_* x`, hence `Pr(x<d)<1/3`.                              (5.1)

For every `u in M`, `x<u` in the poset, so `x prec_* u`. If `u prec_* y`, then `x prec_* u prec_* y` and `u||y`, again giving a shorter extreme span. Therefore

`y prec_* u`, hence `Pr(u<y)<1/3`.                              (5.2)

By Theorem 3.1, `Pr(x<y)>=1/2`; since the candidate has no balanced pair, in fact `Pr(x<y)>2/3`. Consequently (4.4) gives

`Pr( {x<d} union union_{u in M}{u<y} ) > 1/3`.                 (5.3)

There are at most three events in this union. Hence:

### Theorem 5.1 — width-three fringe selector

In the inherited strict-chain / crossed-successor / no-internal-descent branch,

1. `M` is nonempty; and
2. at least one canonical fringe event has probability `>1/9`.

Therefore there is an incomparable fringe pair, either `(d,x)` or `(y,u)` for some `u in M`, whose minority orientation probability lies in

`(1/9,1/3)`,

and whose strong-majority orientation probability lies in

`(2/3,8/9)`.                                                   (5.4)

If `|M|=1`, the stronger pigeonhole bound holds: one of the two fringe events has probability `>1/6`, so one selected strong fringe pair has probability strictly below `5/6`.

### Proof

If `M` were empty, (5.3) would reduce to `Pr(x<d)>1/3`, contradicting (5.1); hence `M` is nonempty. There are one lower event and at most two upper events, so (5.3) forces one event above `1/9`. Equations (5.1)–(5.2) keep that event below `1/3`. Taking the complementary majority orientation gives (5.4). If `|M|=1`, there are only two events, giving `>1/6`. `□`

This is the direct arbitrary-size pair-selection implication requested by the live branch: the crossed terminal exception cannot merely sit at the original endpoint. It must export more than `1/9` of the entire extension mass through one canonical outward fringe pair, and in the singleton-upper case more than `1/6`.

## 6. Exact singleton two-gap polynomial and the sharp adversary

When `D={d}` and `U={u}`, put

`alpha = Pr(x<d)`,

`beta  = Pr(u<y)`,

`eta   = Pr(x<d and u<y)`.

Theorem 3.1 and inclusion-exclusion give the exact two-gap polynomial

`2 Pr(x<y)-1 = alpha + beta - eta`.                             (6.1)

If additionally `d<u`, then the intersection event is exactly

`{x<d<u<y}`.                                                   (6.2)

In a no-internal-descent no-balanced branch, `alpha,beta<1/3`; nevertheless a strong endpoint requires

`alpha+beta-eta > 1/3`.                                        (6.3)

Thus the exact remaining local threshold is the overlap inequality

`eta >= alpha+beta-1/3`.                                       (6.4)

A proof of (6.4) from only the local crossed geometry is impossible. The fleet02/B19 15-point adversary misses it by the arithmetically minimum amount.

For its exact pair `(x,y,d,u)=(3,13,12,9)`, independent enumeration in this run gives

`E=1810`,

`N_xy=1207`,

`A=#{3<12}=336`,

`B=#{9<13}=352`,

`H=#{3<12 and 9<13}=84`,

so

`R=A+B-H=604=2N_xy-E`.                                        (6.5)

The endpoint excess can be written in either equivalent integer form

`3N_xy-2E = 1`,                                                (6.6)

`3R-E = 2`.                                                    (6.7)

Hence

`Pr(3<13)-2/3 = (3R-E)/(6E) = 1/(3E) = 1/5430`.               (6.8)

The parity forced by `N_xy=(E+R)/2` makes `3R-E` even, so `2` is the smallest positive possible numerator in (6.7). The B19 adversary therefore saturates the exact two-gap threshold at the first possible integer step; this explains, rather than merely observes, why a fixed local margin cannot work.

It also verifies the selector bound sharply enough to be informative:

`alpha=336/1810`, `beta=352/1810`,

and both are strictly between `1/6` and `1/3`. The same poset contains a balanced pair `(8,13)` with exact count `1081/1810`, confirming that the local violation must be charged to global structure rather than accepted as a counterexample.

### Exact checker

`verify_crossed_two_gap.py` re-enumerates all 1810 uniform linear extensions from the displayed B19 transitive reduction and checks the neighborhood discrepancies and identities (6.5)–(6.7).

- verifier SHA-256: `eb1449305b88fa9ea085e9d0fa8b05a842c3de63a44d79c9eadc7ea33287c163`
- captured-output SHA-256: `d3d540c257652795abb11471ba7929c7dc13b6c614064f0e880a970cbf5aff07`
- terminator: `POS3_CROSSED_TWO_GAP_REGRESSION_PASS`

Captured output:

```text
extensions 1810
crossed_pair 3 13 Nxy 1207 fraction 1207/1810
lower_only_event_A 336 fraction 336/1810
upper_only_event_B 352 fraction 352/1810
intersection_H 84 fraction 84/1810
union_R 604 fraction 604/1810
identity_2Nxy_minus_E 604 equals_R 604
threshold_count_3Nxy_minus_2E 1
union_threshold_3R_minus_E 2
balanced_escape_pair_8_13 1081 fraction 1081/1810
POS3_CROSSED_TWO_GAP_REGRESSION_PASS
```

The computation is regression evidence for the published adversary. Theorems 3.1, 4.1 and 5.1 are analytic and do not depend on finite enumeration.

## 7. Exact remaining obligation

The crossed-neighborhood exception is now reduced to a source-valid global charge rather than a vague local transport statement.

For the singleton two-gap case, a hypothetical counterexample must satisfy simultaneously

`alpha<1/3`, `beta<1/3`, and `alpha+beta-eta>1/3`.              (7.1)

For the inherited width-three chain-difference case, it must export more than `1/9` mass through a canonical outward fringe pair by Theorem 5.1.

The next lead step is therefore:

> use the full three-chain cumulative-band constraints / block corridor charges to show that repeated canonical fringe export either encounters a balanced pair, creates an internal strong-majority span descent, or forces the two-gap overlap bound `eta>=alpha+beta-1/3` at one crossed terminal endpoint.

The fleet02/B19 adversary proves this cannot be obtained from the local two-distinguisher counts alone: it violates (6.4) by exactly the minimum integer amount while possessing balanced pairs elsewhere. Thus the next proof must genuinely import global path/flux information; another local constant or distinguisher census is insufficient.

The non-crossed successor branch (`Succ(y) not subseteq Succ(x)`) also remains unpaid and must not be silently folded into this theorem.

## 8. Status

- Crossed-neighborhood union identity (3.1): **PROVED** for every finite poset.
- Width-three canonical fringe compression (4.1)–(4.3): **PROVED**.
- Inherited strict-chain crossed branch fringe selector (5.4): **PROVED**.
- Exact singleton two-gap polynomial and arithmetic threshold: **PROVED**.
- Fleet02/B19 sharp adversary: independently reproduced for the quantities used here.
- POS3: **OPEN / NOT PROVED**.
- I0122 finite frontier: `n_bal=14`, unchanged.
- Run classification: `ESSENTIAL_STEP_APPLIED`.

Scoped privacy/provenance review: the committed scientific files contain only mathematical statements, source-bound repository references, deterministic verifier code/output and nonsecret run labels. No credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, benchmark material, email/Drive content, paid model/API calls, remote workflows, public posting or permission changes were used.
