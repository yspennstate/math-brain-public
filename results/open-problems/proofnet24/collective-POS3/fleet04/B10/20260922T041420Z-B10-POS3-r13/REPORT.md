# POS3 fleet04/B10 — direct 1/6 selector in the strict predecessor corridor

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status after this report:** **OPEN / NOT PROVED**.  
**Inherited finite frontier:** `n_bal=14` (unchanged).  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run continues `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. It performs no installation or benchmark work and makes no novelty or priority claim.

## 1. Exact state consumed

The latest complete campaign-lead report consumed is

- fleet04/B10, `proofnet24/collective-POS3/fleet04/B10/20260922T034709Z-B10-POS3-r12/REPORT.md`, blob `4759a4ecb5f2963a3d190f66fc6728459bb1a46e`.

It proves the crossed-neighborhood union identity and, in the inherited strict-chain crossed branch, a canonical outward fringe selector. It leaves the non-crossed successor branch and the global upgrade to a balanced pair unpaid.

The required named **OTHER-account partner** input is

- fleet01/B11, `proofnet24/collective-POS3/fleet01/B11/20260922T031426Z-b11-pos3-r11/ADDENDUM_STRONGER_NESTING.md`, commit `d88f0dc5d26786eee8ec892426b1e385bb3529fb`, blob `4813f489bd0c54deda662f70b2027bf4ac866472`.

It strengthens the first-fork nesting statement: the sibling predecessor sets are nested already from `Pred(y) subseteq Pred(x)`, without requiring equality, and the finite clean-fork funnel exits to a strict predecessor-nested endpoint.

A second **OTHER-account** result used directly is

- fleet03/B10, `proofnet24/collective-POS3/fleet03/B10/20260922T031643Z-a03-b10-pos3-r11/REPORT.md`, blob `e39ea9f7c820637f16470822d2979f2bbe494e0c`.

That report handles the strict delayed-predecessor corridor when the endpoint with the larger predecessor set is majority-early. By conditioning on the top delayed predecessor it reaches an equal-predecessor child, proves one-blocker impossibility without span descent, and shows the only no-descent residue has two positive blockers. It leaves the **majority-late** polarity as the next source-valid missing branch.

The exact same-account transport identity used below is

- fleet04/B20, `proofnet24/collective-POS3/fleet04/B20/20260922T034210Z-b20-auto11/REPORT.md`, blob `336cfa5de180db89c2528696d5d4845e6e0a7849`.

For every incomparable `a,b`, with

`D_a=Pred(a)\Pred(b)`, `D_b=Pred(b)\Pred(a)`,
`U_a=Succ(a)\Succ(b)`, `U_b=Succ(b)\Succ(a)`,

it defines

`B_-={b precedes some d in D_a OR some u in U_b precedes a}`,
`B_+={a precedes some d in D_b OR some u in U_a precedes b}`

and proves the exact original-law identity

`2 Pr(a<b)-1 = Pr(B_+) - Pr(B_-)`.                              (1.1)

No induced law is renamed uniform in this report.

## 2. Compact conditional end-to-end route

Assume for contradiction-search purposes that `P` is a finite width-at-most-three poset with no balanced incomparable pair, and let `prec_*` be the inherited transitive strong-majority order.

The fleet01/B11 funnel reduces the first Hasse-fork geometry to a strict predecessor-nested endpoint. The still-unpaid first-fork branch singled out by fleet03/B10 is the delayed-chain corridor

`a||b`,
`Pred(b) proper_subset Pred(a)`,
`D:=Pred(a)\Pred(b)` nonempty and a chain,                       (2.1)

when the larger-predecessor endpoint is majority-late,

`b prec_* a`, equivalently `p:=Pr(a<b)<1/3`.                   (2.2)

Fix this arbitrary-size branch. The first missing implication is to show that it cannot remain a featureless endpoint after internal span descent has been exhausted.

The result below proves a quantitative selector directly in the **original uniform law**:

> if there is no strict strong-majority span descent inside `(b,a)`, then either the endpoint `(a,b)` itself already has minority probability in `(1/6,1/3)`, or the smaller-predecessor endpoint `b` has exactly two canonical Hasse-successor blockers and one of the resulting flanking incomparable pairs has minority probability in `(1/6,1/3)`.

In the latter branch the first-fork width-three witness also forces a new bridge relation into one blocker.

Thus the majority-late polarity is no longer an untreated exception. The remaining problem is to upgrade this uniform `1/6` selector / fork bridge to the target threshold `1/3` by global three-chain mass conservation.

## 3. Canonical compression of the lower and upper blocker events

Let

`d=max D`,                                                       (3.1)

which exists because the inherited predecessor difference `D` is a finite nonempty chain.

Let

`U:=Succ(b)\Succ(a)`,
`M:=Min(U)`.                                                     (3.2)

### Lemma 3.1 — the lower blocker event is one event

The first part of `B_-` is exactly

`{b precedes some element of D} = {b<d}`.                       (3.3)

#### Proof

If `b<d`, the left event holds. Conversely, if `b<d'` for some `d' in D`, then `d'<=d` because `D` is a chain with top `d`, so every linear extension has `b<d'<=d`, hence `b<d`. `square`

### Lemma 3.2 — only minimal upper distinguishers matter

`{some u in U precedes a} = union_{u in M}{u<a}`.               (3.4)

Moreover

`|M|<=2`,                                                        (3.5)

and every `u in M` is a Hasse successor of `b` and is incomparable with `a`.

#### Proof

The event equality follows by choosing a minimal member of `U` below any witnessing member.

The set `M` is an antichain and every member is incomparable with `a`; otherwise it would not belong to `Succ(b)\Succ(a)`. Thus `M union {a}` is an antichain, so width at most three gives `|M|<=2`.

For the cover statement, suppose `b<w<u` with `u in M`. If `w<a`, then `b<w<a`, contradicting `a||b`. If `a<w`, then `a<u`, contradicting `u notin Succ(a)`. If `w||a`, then `w in U` lies strictly below the minimal element `u`, contradiction. Hence no such `w` exists and `b lessdot u`. `square`

## 4. Majority-late strict corridor: direct 1/6 selector

Assume (2.1)-(2.2) and suppose there is **no strict internal strong-majority span descent** between `b` and `a`.

Because `d<a` in the poset, `d prec_* a`. Since `d||b`, if `b prec_* d prec_* a`, the incomparable pair `(b,d)` is a strict internal span descent. Therefore no descent forces

`d prec_* b prec_* a`.                                         (4.1)

The no-balanced hypothesis then gives

`Pr(b<d)<1/3`.                                                   (4.2)

Likewise, for every `u in M`, the relation `b<u` gives `b prec_* u`. If `u prec_* a`, then `(u,a)` is a strict internal span descent. Thus no descent forces

`b prec_* a prec_* u`,                                         (4.3)

and hence

`Pr(u<a)<1/3` for every `u in M`.                               (4.4)

Because `Pred(b) subset Pred(a)`, the set `D_b` in (1.1) is empty. Therefore

`B_- = {b<d} union union_{u in M}{u<a}`,                        (4.5)

while `B_+` is some nonnegative-probability successor-blocker event on the opposite side. Since `p<1/3`, (1.1) gives

`Pr(B_-)-Pr(B_+) = 1-2p > 1/3`.                                (4.6)

In particular

`Pr(B_-) >= 1-2p`.                                              (4.7)

### Theorem 4.1 — majority-late 5/6 selector

Under (2.1)-(2.2) and no internal span descent, there exists an incomparable pair `(r,s)` such that

`1/6 < min(Pr(r<s),Pr(s<r)) < 1/3`.                            (4.8)

More precisely:

1. if `p>1/6`, take `(r,s)=(a,b)`;
2. if `p<=1/6`, then `|M|=2`, and for at least one `u in M`,

   `1/6 < Pr(u<a) < 1/3`.                                      (4.9)

Thus in the second branch `b` has exactly two canonical Hasse-successor blockers relative to `a`.

#### Proof

If `p>1/6`, then `p<1/3` from (2.2), so the endpoint itself has the required minority probability.

Now assume `p<=1/6`. From (4.7),

`Pr(B_-) >= 1-2p >= 2/3`.                                      (4.10)

Using (4.2) and the union bound with (4.5),

`Pr(union_{u in M}{u<a})`
` >= Pr(B_-) - Pr(b<d)`
` > 2/3 - 1/3 = 1/3`.                                         (4.11)

Hence `M` is nonempty. By (3.5), it has at most two elements. Each individual event in (4.11) has probability `<1/3` by (4.4), so one event cannot realize a union of probability `>1/3`. Therefore `|M|=2`. Finally the union probability is at most the sum of the two event probabilities, so at least one satisfies

`Pr(u<a)>1/6`.                                                   (4.12)

Combine with (4.4) to get (4.9). `square`

This proves the first previously missing pair-selection implication in the majority-late delayed-chain branch. It is arbitrary-size, uses the actual uniform extension law, and does not assume a bounded search radius.

## 5. First-fork bridge in the small-endpoint subbranch

Return to the inherited first Hasse-fork geometry. In the strict sibling branch, let `c` denote the previous clean-fork right endpoint: `c` is incomparable with both strict siblings and lies before both in `prec_*`. In the majority-late labeling above,

`c prec_* b prec_* a`,
`c||b`, `c||a`.                                                 (5.1)

Assume the second branch of Theorem 4.1, so `p<=1/6` and `M={u_1,u_2}`. By Lemma 3.2,

`a||u_1`, `a||u_2`, `u_1||u_2`,                                (5.2)

so `{a,u_1,u_2}` is a three-antichain.

### Corollary 5.1 — width-saturating bridge

At least one `u_i` satisfies

`c<u_i`.                                                         (5.3)

#### Proof

If `c` were incomparable with both `u_1,u_2`, then `{c,a,u_1,u_2}` would be a four-antichain, impossible at width at most three. Thus `c` is comparable with some `u_i`. Equation (4.3) and (5.1) place `c` before `u_i` in `prec_*`; since `prec_*` extends the poset, the comparability must be `c<u_i`. `square`

Hence the small-minority majority-late branch does not merely output a numerical pair. It creates the same kind of nonlocal second-fork bridge that fleet03/B10 obtained in the majority-early polarity.

## 6. Synthesis with the OTHER-account majority-early result

The fleet03/B10 report treated the opposite strict-chain polarity

`a prec_* b`, `p:=Pr(a<b)>2/3`.                                (6.1)

Its conditioning proof shows the no-descent residue has exactly two positive blockers. The blocker-swap identity (1.1) gives a shorter direct quantitative consequence that is useful for the common lead state.

Because `Pred(b) subset Pred(a)`, `B_+` is exactly the upper successor-difference union

`B_+={some u in Succ(a)\Succ(b) precedes b}`.                  (6.2)

From (1.1) and `p>2/3`,

`Pr(B_+)-Pr(B_-)=2p-1>1/3`,

so

`Pr(B_+)>1/3`.                                                   (6.3)

Compress `B_+` to the at most two minimal successor distinguishers. Under no internal span descent, each such blocker lies after `b` in `prec_*`, so each individual crossing probability is `<1/3`. Therefore there are exactly two, and at least one has crossing probability `>1/6`.

Thus the majority-early branch from fleet03/B10 and the new majority-late theorem share one common output:

> **Unified strict-chain terminal selector.** In the inherited first-fork strict delayed-predecessor corridor, after internal strong-majority span descent is exhausted, there is always a canonical incomparable pair with minority probability strictly in `(1/6,1/3)`. In the majority-early polarity a two-successor-blocker fork is forced; in the majority-late polarity either the endpoint itself is already in that window or, when its minority is at most `1/6`, a two-successor-blocker fork and bridge are forced.

This uses the named fleet03/B10 result as the already-proved opposite-polarity state and pays the polarity that report explicitly left open.

## 7. Exact sharp-adversary calibration

The fleet02/B19 15-point width-three adversary carried through the previous lead report has

`E=1810`,
`Pr(13<3)=603/1810`,
`Pred(3) proper_subset Pred(13)`,
`D={12}`,
`Pr(3<12)=336/1810`,
`Succ(3)\Succ(13)={9}`,
`Pr(9<13)=352/1810`,
`Pr(3<12 and 9<13)=84/1810`.

Take `(a,b,d,u)=(13,3,12,9)`. Then

`p=603/1810 = 1/3-1/5430`,                                    (7.1)

so this witness lies in the **first** branch of Theorem 4.1: `p>1/6`, and the endpoint itself is the selected `(1/6,1/3)` pair.

The direct blocker identity calibrates exactly:

`B_-={3<12 OR 9<13}`,
`|B_-|=336+352-84=604`,
`B_+=empty`,                                                     (7.2)

and

`1-2p = 604/1810`.                                              (7.3)

Thus the new theorem does not falsely eliminate the published one-count adversary. It explains where that adversary sits: the majority-late endpoint is already arbitrarily close to the target boundary from below, while the stronger two-blocker/bridge conclusion is reserved for the genuinely small-minority subbranch `p<=1/6`.

No new finite census or code is used as proof in this run. The arithmetic above is an exact recombination of the published integer counts already independently checked in the predecessor reports.

## 8. Exact remaining obligation

The first-fork strict delayed-predecessor corridor is now quantitatively normalized in both polarities:

- internal span descent reduces the strong-majority span;
- otherwise a canonical pair has minority probability in `(1/6,1/3)`;
- majority-early always creates a two-successor-blocker fork;
- majority-late with endpoint minority `<=1/6` also creates exactly two Hasse blockers and a width-forced bridge from the previous fork endpoint.

What remains unpaid is a **global amplification/charge theorem** that upgrades this `1/6` mass to `1/3`, or shows that repeated bridged two-cover forks cannot propagate through the three-chain lattice-path corridor without producing a balanced pair. The fleet02/B19 linear-depth family and the sharp 15-point adversary forbid replacing this by a bounded-radius selector or by a local fixed positive margin.

The next lead step should therefore use the exact three-chain cumulative-band / blocker-corridor flux, not another local distinguisher count: charge the `>1/6` crossing mass from consecutive canonical blockers and prove that either two such charges overlap enough to yield a balanced pair or the width-three path geometry forces a strict span descent / ordinal reduction.

The non-chain strict predecessor-difference exits produced later in the clean-fork funnel remain separate; this report deliberately pays the source-exact **chain-difference first-fork branch** inherited from the lead and fleet03/B10, rather than silently generalizing beyond its hypotheses.

## 9. Status and integrity

- fleet01/B11 strengthened first-fork predecessor nesting: **CONSUMED/APPLIED**.
- fleet03/B10 majority-early strict corridor: **CONSUMED/APPLIED**.
- Majority-late delayed-chain first missing implication: **PROVED** as Theorem 4.1.
- Majority-late small-endpoint two-blocker bridge: **PROVED** as Corollary 5.1.
- Unified strict-chain no-descent `(1/6,1/3)` selector: **PROVED**.
- POS3: **OPEN / NOT PROVED**.
- I0122 finite frontier: `n_bal=14`, unchanged.
- Run classification: `ESSENTIAL_STEP_APPLIED`.

Scoped privacy/provenance review: this report contains only mathematical statements, source-bound private-repository references, exact nonsecret integer counts already present in the POS3 research archive, and nonsecret run labels. No credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, benchmark gold, email/Drive content, paid model/API/Codex calls, remote workflows, public posting, permission changes, or production-brain mutation were used.
