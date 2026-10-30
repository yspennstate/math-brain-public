# POS3 fleet02/B10 — second canonical blockers force superheavy sandwich mass

**Run:** `20260922T0548Z-b10-pos3-auto11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has incomparable `x,y` with `1/3 <= Pr(x<y) <= 2/3` under the uniform law on all full linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run implements `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z` and the fleet02/B10 coupling/adjacent-swap assignment. It performs no brain-installation or benchmark work. Every probability below is under the original uniform measure on **all** linear extensions of the actual poset; no deletion projection is replaced by a uniform surrogate.

## 1. Exact completed inputs actually consumed

The newest complete campaign-lead report read before the derivation is

- **fleet04/B10**, `proofnet24/collective-POS3/fleet04/B10/20260922T051259Z-B10-POS3-r14/REPORT.md`.

Its bridge theorem shows that, in the live majority-late bridged-blocker branch of a hypothetical no-balanced width-three poset, a saturated bridge contains a unique cover `x lessdot y` with

`Pr(x<a)>2/3`, `Pr(y<a)<1/3`,

and hence

`Pr(x<a<y)>1/3`.

Using the exact fleet01/B19 cover-two-witness theorem, that lead report further forces at least two external relation-witness channels for this heavy cover. Thus the current global debt is no longer creation of target-scale mass; it is converting or recycling that mass into a balanced pair, strict majority-span descent, a forbidden width-four antichain, or an autonomous/ordinal reduction.

The required named **OTHER-account partner** input used directly is

- **fleet03/B11**, `proofnet24/collective-POS3/fleet03/B11/20260922T044349Z-fleet03-B11-pos3-r11/REPORT.md`, Git blob `337b660656cf3df6fc194a4be79b4801bfc99b97`.

In the amplified outer-fringe branch it starts with an incomparable pair `d,u` satisfying

`Pr(d<u)>5/6`,
`Pred(d) subseteq Pred(u)`,
`Succ(u) subseteq Succ(d)`,

and inherited canonical fringe points `x in Pred(u)\Pred(d)` and `y in Succ(d)\Succ(u)`. It proves that the mandatory additional outer distinguisher gives one of:

1. strict strong-majority span descent;
2. a **second canonical lower or upper blocker**; or
3. a shadow Hasse cover carrying a three-point sandwich event of probability `>1/3`.

The second canonical blocker alternative was structural but had no target-scale mass estimate. This run pays exactly that missing quantitative implication.

A compatible amplification input, used only to identify the source of the partner configuration, is

- **fleet04/B19**, `proofnet24/collective-POS3/fleet04/B19/B19-20260922T041629Z-auto11/REPORT.md`.

It proves the outer crossed nesting and the strict amplification `Pr(d<u)>5/6` from the earlier crossed-singleton inner pair, and excludes the reciprocal-singleton autonomous `2+2` closure.

The immediately preceding fleet02/B10 result used for continuity is

- `proofnet24/collective-POS3/fleet02/B10/20260922T044758Z-b10-r12-9941265a/REPORT.md`, blob `2dd9b8b5a1ff8dada78596279ed93fc2cea0b2c1`.

It gave the defect/arity selector, improving the local terminal minority floor to `1/5` in the unified branch and `1/4` in the exact-two branch. The present run changes scale: it tracks the partner's exported blocker event itself rather than improving that endpoint constant again.

## 2. Compact conditional end-to-end route

Assume for contradiction that `P` is a cardinality-minimal width-at-most-three counterexample, hence has no balanced incomparable pair, and work in the inherited transitive strong-majority order `prec_*`.

The current route is:

1. the lead's bridged branch produces an actual cover-gap event of mass `>1/3` and at least two witness channels;
2. in the crossed-singleton export, fleet04/B19 amplifies to an outer incomparable pair `(d,u)` with `Pr(d<u)>5/6`;
3. the named partner fleet03/B11 localizes every mandatory third outer distinguisher to span descent, a second canonical blocker, or a shadow-cover sandwich of mass `>1/3`;
4. **new step in this run:** after span descent is excluded, every second canonical blocker actually carries a sandwich event of mass **strictly greater than `1/2`**;
5. therefore the surviving global charge problem has only two quantitative local outputs: a shadow-cover charge `>1/3`, or a second-blocker charge `>1/2`. What remains is to prove that these charges cannot be recycled indefinitely through the width-three corridor without producing the target balanced pair or one of the already-valid structural exits.

Step 4 is proved next without changing measure or conditioning law.

## 3. Lower second-blocker theorem

Keep the partner's amplified outer pair `d||u`, and define

`D = Pred(u) \ Pred(d)`.

The inherited point `x` is a maximal element of `D`. Suppose the partner's second-blocker alternative occurs on the lower side, so there is

`ell in Max(D)`, `ell != x`.

Width at most three implies `Max(D)={x,ell}`: the set `Max(D) union {d}` is an antichain, so there cannot be a third maximal discrepancy point.

### Lemma 3.1 — the second lower blocker is a cover and is incomparable with `d`

One has

`ell lessdot u`, `ell || d`.

#### Proof

By definition `ell<u` and `ell not<d`. If `d<ell`, then `d<ell<u`, contradicting `d||u`. Thus `ell||d`.

If `ell<z<u`, then `z` cannot lie below `d`, since that would imply `ell<d`; and `d<z` would imply `d<u`. Hence `z||d`, so `z in D`, contradicting maximality of `ell`. Therefore no point lies strictly between `ell` and `u`, proving `ell lessdot u`. `square`

The forced relation `ell<u` implies `ell prec_* u`. Also the amplified pair has `d prec_* u` because `Pr(d<u)>5/6`.

### Theorem 3.2 — no-descent lower second blocker carries more than half the extension mass

If there is no strict strong-majority span descent inside the outer interval `(d,u)`, then

`ell prec_* d prec_* u`,

and

`Pr(ell<d<u) > 1/2`.                                           (3.1)

More exactly,

`Pr(ell<d<u) = Pr(ell<d) + Pr(d<u) - 1`.                       (3.2)

#### Proof

If instead `d prec_* ell`, then

`d prec_* ell prec_* u`

and `d||ell`, so `(d,ell)` is a strict strong-majority incomparable span properly inside `(d,u)`, which is exactly the already-authorized span-descent exit. Excluding that exit forces `ell prec_* d`, and no balance gives

`Pr(ell<d)>2/3`.                                                (3.3)

Because `ell<u` is forced in the poset while `d` is incomparable with both `ell` and `u`, every linear extension has exactly one of the relative orders

`d<ell<u`, `ell<d<u`, `ell<u<d`.

Writing their probabilities as `A,B,C`, respectively,

`Pr(ell<d)=B+C`,
`Pr(d<u)=A+B`,
`A+B+C=1`.

Therefore

`B=Pr(ell<d)+Pr(d<u)-1`,

which is (3.2). The partner/amplification theorem gives `Pr(d<u)>5/6`; combining with (3.3) yields

`Pr(ell<d<u) > 2/3 + 5/6 - 1 = 1/2`.

No conditional law has entered. `square`

Thus the second lower blocker alternative is not merely a new distinguisher. It creates a **superheavy exact cover sandwich** supported on the Hasse edge `ell lessdot u`.

## 4. Upper dual

Let

`U = Succ(d) \ Succ(u)`.

The inherited point `y` is a minimal member of `U`. If the partner's second-blocker alternative occurs on the upper side, let

`r in Min(U)`, `r != y`.

Then width three gives `Min(U)={y,r}`, and the dual of Lemma 3.1 gives

`d lessdot r`, `r || u`.

Since `d<r`, we have `d prec_* r`, while amplification gives `d prec_* u`. If `r prec_* u`, then

`d prec_* r prec_* u`

with `r||u`, a strict span descent. Excluding that exit forces

`u prec_* r`, hence `Pr(u<r)>2/3`.

Exactly the same three-order partition, now using the forced relation `d<r`, gives

`Pr(d<u<r) = Pr(d<u) + Pr(u<r) - 1 > 1/2`.                    (4.1)

So **either** canonical second-blocker side, after span descent is removed, carries a strict `>1/2` three-point event under the original full-extension law.

## 5. Quantitative refinement of the partner trichotomy

The named partner's Theorem 5.1 can therefore be sharpened, in the exact inherited amplified outer branch, to the following source-compatible trichotomy:

1. strict strong-majority span descent; or
2. a unique second canonical lower/upper Hasse blocker whose associated sandwich event has probability `>1/2`; or
3. a shadow Hasse cover whose associated sandwich event has probability `>1/3`.

This is a strict gain on alternative 2. The `>1/2` event is already larger than the balanced-pair threshold scale; the missing difficulty is **conversion**, not mass creation.

It also interacts cleanly with the lead's r14 bridge state. Both the lead bridge and the partner shadow branch output genuine cover-linked three-point mass `>1/3`; the second-blocker branch now outputs a strictly stronger `>1/2` charge. A future global potential can therefore charge the second-blocker branch more aggressively than the shadow branch instead of treating every witness channel uniformly.

## 6. Exact local calibration and a failed stronger shortcut

To test whether the new `>1/2` sandwich itself forces one endpoint pair to be balanced, I constructed and exactly enumerated the width-three poset on vertices `0,...,8` with transitive reduction

`0<6, 0<7, 1<4, 2<3, 2<7, 3<6, 4<5, 5<7, 6<8`.

It has exactly `353` linear extensions and width exactly three; `{0,3,5}` is an antichain of size three.

For

`d=3`, `u=7`, inherited-style lower blocker `x=5`, second lower blocker `ell=0`, and upper blocker `y=6`,

one gets

`D=Pred(7)\Pred(3)={0,1,4,5}`, `Max(D)={0,5}`,

`U=Succ(3)\Succ(7)={6,8}`, `Min(U)={6}`,

with Hasse edges

`0 lessdot 7`, `5 lessdot 7`, `3 lessdot 6`.

The exact full-extension probabilities are

`Pr(3<7)=333/353 > 5/6`,
`Pr(3<5)=261/353 > 2/3`,
`Pr(0<3)=242/353 > 2/3`,
`Pr(6<7)=273/353 > 2/3`,

and

`Pr(0<3<7)=222/353 > 1/2`.

The exact identity from Theorem 3.2 is visible numerically:

`222/353 = 242/353 + 333/353 - 1`.

This calibration is intentionally **local**: it exercises the outer second-blocker hypotheses and the new identity, but it is not claimed to realize every earlier crossed-singleton hypothesis in the inherited minimal-counterexample chain. Indeed the poset has balanced escape pairs; for example

`Pr(5<6)=200/353`.

It decisively rejects the stronger shortcut

> a `>1/2` second-blocker sandwich by itself must balance one of its two adjacent incomparable endpoint pairs.

Here both `(0,3)` and `(3,7)` are still strongly oriented while the sandwich has mass `222/353>1/2`. Thus the next step must use the **other width-three channels/global structure**, not merely the size of this one three-point event.

The deterministic standard-library verifier saved with this run recomputes the transitive closure, width, all 353 extensions, the discrepancy maxima/minima, Hasse-cover assertions, every displayed rational probability, and the exact identity. It terminates with

`POS3_SECOND_BLOCKER_SUPERHEAVY_CHECK_PASS`.

Artifact SHA-256 values from the executed in-run bytes:

- `verify_second_blocker_superheavy.py`: `334f3a2e6736727c721e32b3fb7c28627c5d7edcfeda1c35ee260286af899759`;
- `verify_second_blocker_superheavy.out`: `ad449387f22aeb8b897802dc8cdf8b1a96eb2ebfe9f3e8131134f87695ec7b1b`.

The finite computation is regression/adversarial evidence only. Theorem 3.2 and its dual are symbolic arbitrary-size statements.

## 7. First unpaid implication after this run

The local quantitative hierarchy is now:

- lead bridge cover: sandwich mass `>1/3` plus at least two witness channels;
- partner shadow cover: sandwich mass `>1/3`;
- partner second canonical blocker, after span descent is excluded: sandwich mass `>1/2`.

The first essential remaining statement is therefore the following source-matching global transport problem.

### `POS3-SUPERHEAVY-RECYCLING-v1`

In a cardinality-minimal width-at-most-three no-balanced poset, prove that a canonical second-blocker sandwich of mass `>1/2`, or a shadow/bridge cover sandwich of mass `>1/3`, cannot be transported through the next canonical blocker/witness layer while keeping every incomparable pair outside `[1/3,2/3]`, unless one obtains a strict strong-majority span descent, a four-element antichain, or a proper autonomous/ordinal reduction.

A sufficient next lemma must couple **at least two witness channels simultaneously**. One-channel monotonicity is already refuted by the calibration above and by earlier team adversaries. The full extension weights must stay attached to the transported event; no projected word/skeleton law may be silently made uniform.

## 8. Status and integrity

- lead r14 target-scale bridge flux: **CONSUMED**;
- named partner fleet03/B11 r11 third-distinguisher trichotomy: **CONSUMED AND QUANTITATIVELY STRENGTHENED ON ITS SECOND-BLOCKER BRANCH**;
- lower second blocker `ell lessdot u`, no-descent orientation, exact `>1/2` sandwich: **PROVED**;
- upper second blocker dual exact `>1/2` sandwich: **PROVED**;
- stronger claim that the superheavy event alone forces local endpoint balance: **REFUTED BY SOURCE-VALID WIDTH-THREE LOCAL CALIBRATION**;
- full POS3 target: **OPEN / NOT PROVED**;
- run classification: **`ESSENTIAL_STEP_APPLIED`**.

Scoped privacy/provenance review: this run contains mathematical statements, repository-relative source references, nonsecret Git object identifiers, deterministic verifier code/output, and a nonsecret run label only. It contains no benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email/Drive material, paid model/API/Codex use, remote workflow execution, permission bypass, or public-posting action.
