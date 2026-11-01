# POS3 fleet02/B19 — exact greedy-fringe 2-cycle and majority-late conditioning trap

**Outcome:** `CANDIDATE_REFUTED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run continues `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. It does no new brain-installation or benchmark work. The new mathematics attacks the current crossed-neighborhood selector by an exact selector-dynamics construction rather than another static threshold example.

## 1. Exact collective state consumed

The latest complete campaign-lead report consumed is fleet04/B10,

`proofnet24/collective-POS3/fleet04/B10/20260922T034709Z-B10-POS3-r12/REPORT.md`, blob `4759a4ecb5f2963a3d190f66fc6728459bb1a46e`, science commit `838f837e53739dab6bf7143a5a8f59d183618b32`.

Its crossed-neighborhood identity says that for an incomparable strong pair `x||y` with

`Pred(x) subseteq Pred(y)` and `Succ(y) subseteq Succ(x)`, 

putting `D=Pred(y)\Pred(x)` and `U=Succ(x)\Succ(y)`, one has under the actual uniform law

`2 Pr(x<y)-1 = Pr(A_D union B_U)`.

In the inherited strict-chain/no-internal-descent branch, `D` has a unique maximal element `d`, `U_min` has size at most two, every canonical fringe event has probability below `1/3`, and at least one has probability above `1/9`; when `|U_min|=1`, one is above `1/6`. The lead explicitly leaves the resulting outward fringe selector to be globally charged.

The named OTHER-account result consumed and applied is fleet03/B10,

`proofnet24/collective-POS3/fleet03/B10/20260922T031643Z-a03-b10-pos3-r11/REPORT.md`, blob `e39ea9f7c820637f16470822d2979f2bbe494e0c`, science commit `114518e3e96cdf1eb609ac8e5ade4a1b27094b08`.

It proves the exact two-child decomposition for a strict predecessor corridor: if `Pred(b) proper_subset Pred(a)`, `D=Pred(a)\Pred(b)` is a chain, and `d=max D`, then conditioning on `d<b` gives a genuine uniform child `P^+=P+(d<b)` with equal predecessor sets, while the opposite child forces `b<a`; hence for the event `a<b`,

`Pr_P(a<b)=gamma Pr_{P^+}(a<b)`, with `gamma=Pr_P(d<b)`.

Its proved progress theorem treats the branch where the larger-predecessor endpoint `a` is majority-early. It explicitly leaves the **larger-predecessor-majority-late** branch unpaid. The construction below lands exactly in that complementary branch twice.

## 2. Conditional route and the first missing implication

Assume for contradiction that POS3 has a cardinality-minimal no-balanced width-three counterexample. The current lead route reaches a crossed strong endpoint pair and exports probability mass through a bounded set of canonical fringe pairs. A natural local completion is to select a canonical fringe event of largest probability and iterate, hoping the chosen pair strictly progresses toward balance or a shorter/well-founded corridor.

The first essential missing implication is therefore not merely existence of a `>1/9` fringe pair; it is a **global anti-cycle / progress theorem** for the exported fringe pair. The local crossed-neighborhood identities alone do not provide such a theorem. The exact width-three poset below makes the largest-mass fringe selector cycle with period two.

This does **not** refute the lead theorem, the partner theorem, or POS3. It refutes only the stronger local shortcut that the lead's canonical fringe data themselves make the greedy selector well-founded. The example has balanced pairs and two nontrivial autonomous modules, so any successful target-level proof may still use the global minimal-counterexample/module-prime/no-balanced hypotheses to rule it out.

## 3. Exact width-three core

Let `P` be the 11-element poset with transitive reduction

`0<1, 0<5, 1<2, 1<6, 1<10, 2<3, 4<1, 4<5, 5<3, 5<6, 6<7, 8<9, 9<5, 9<10, 10<3, 10<7`.

It has the explicit three-chain cover

`C0=(0,1,2,3)`,

`C1=(4,5,6,7)`,

`C2=(8,9,10)`.

The antichain `{0,4,8}` proves width at least three, and the cover proves width at most three. Exact enumeration gives

`E=e(P)=932`

uniform linear extensions. The incomparability graph is connected. The verifier checks every one of the 18 incomparable-pair probabilities. It also records the limitation honestly: the only nontrivial proper autonomous subsets are `{0,4}` and `{8,9}`.

The core is therefore a source-valid adversary to a **local selector lemma**, not a target counterexample and not a module-prime minimal-counterexample model.

## 4. First selector step

Take

`(x,y)=(5,10)`.

The exact neighborhood discrepancies are singleton crossed fringes:

`Pred(10)\Pred(5)={1}`,

`Succ(5)\Succ(10)={6}`.

The endpoint is strong:

`Pr(5<10)=662/932=331/466>2/3`.

With the lead's singleton notation

`alpha=Pr(5<1)=192/932=48/233`,

`beta=Pr(6<10)=284/932=71/233`,

`eta=Pr(5<1 and 6<10)=84/932=21/233`.

Hence the lead identity is exact:

`2 Pr(5<10)-1 = alpha+beta-eta = 392/932 = 98/233 > 1/3`.

Both canonical fringe events lie strictly in `(1/6,1/3)`, so neither is balanced. The larger one is `beta=71/233`. Choosing the largest canonical fringe event therefore exports the majority-oriented pair

`(10,6)`

with

`Pr(10<6)=1-71/233=162/233>2/3`.

## 5. Second selector step and exact 2-cycle

For the exported pair

`(x',y')=(10,6)`, 

the crossed structure repeats with new singleton fringes:

`Pred(6)\Pred(10)={5}`,

`Succ(10)\Succ(6)={3}`,

and

`Pr(10<6)=648/932=162/233>2/3`.

Its exact two-gap data are

`alpha'=Pr(10<5)=270/932=135/466`,

`beta'=Pr(3<6)=164/932=41/233`,

`eta'=Pr(10<5 and 3<6)=70/932=35/466`.

Again both canonical fringe events are strictly in `(1/6,1/3)`, and

`2 Pr(10<6)-1 = alpha'+beta'-eta' = 364/932 = 91/233 > 1/3`.

Now `alpha'>beta'`, so the largest canonical fringe event is the lower one. Its complementary majority-oriented pair is

`(5,10)`

with probability `331/466`, exactly the original endpoint. Thus the deterministic largest-fringe rule has the exact cycle

`(5,10) -> (10,6) -> (5,10)`.

No rounding or sampling is involved. This is a literal equality of endpoint labels and exact rational probabilities.

### Refuted local candidate

The following strengthening is false:

> **LOCAL-GREEDY-PROGRESS.** For every width-at-most-three crossed strong endpoint satisfying the lead's singleton-fringe/no-internal-descent inequalities, replacing it by the majority orientation complementary to the largest canonical fringe event cannot return to a previously visited crossed endpoint without first producing a balanced canonical fringe pair.

The displayed `P` refutes it in two steps. Therefore a proof cannot close the lead's selector by “always take the largest exported channel” unless it additionally invokes a genuinely global invariant that excludes this cycle in a minimal no-balanced candidate.

## 6. Direct application of the fleet03/B10 conditioning theorem

The same two-cycle hits exactly the partner's still-unpaid majority-late corridor.

### First endpoint

For `(5,10)`, relabel in the partner's predecessor convention as

`(a,b,d)=(10,5,1)`,

so `Pred(5) proper_subset Pred(10)`. Here the larger-predecessor endpoint is majority-**late**:

`Pr_P(10<5)=270/932=135/466<1/3`.

The genuine conditioning weight is

`gamma_1=Pr_P(1<5)=740/932=185/233`.

In the exact child `P^+=P+(1<5)`, the predecessor sets of `10` and `5` are equal, and

`Pr_{P^+}(10<5)=270/740=27/74`,

which is balanced. Nevertheless the exact partner scaling gives

`Pr_P(10<5)=(185/233)(27/74)=135/466<1/3`.

Thus a balanced same pair in the equal-predecessor child does not lift to a balanced same pair in the original law.

### Second endpoint

For `(10,6)`, use

`(a,b,d)=(6,10,5)`.

Again the larger-predecessor endpoint is majority-late:

`Pr_P(6<10)=284/932=71/233<1/3`.

Now

`gamma_2=Pr_P(5<10)=662/932=331/466`,

and in `P^+=P+(5<10)` the predecessor sets of `6` and `10` are equal with

`Pr_{P^+}(6<10)=284/662=142/331`,

again balanced. Yet

`Pr_P(6<10)=(331/466)(142/331)=71/233<1/3`.

So the exact majority-late obstruction repeats on both vertices of the greedy cycle. This applies the named fleet03/B10 decomposition directly and identifies its next missing transfer: child balance must force a **possibly different original pair** or feed a global charge; scalar same-pair lifting cannot work.

## 7. Infinite asymmetric ordinal-sum family

For arbitrary integers `s,t>=0`, form

`P_{s,t}=C_s ordinal-sum P ordinal-sum C_t`.

Every new element is comparable with every point of the 11-element core. Hence:

- `width(P_{s,t})=3`;
- every linear extension is the forced prefix, followed by one of the same 932 extensions of `P`, followed by the forced suffix;
- the same 18 incomparable pairs and all their probabilities are unchanged;
- the same greedy 2-cycle and both conditioning traps persist exactly.

Assigning all prefix/suffix elements to the first chain gives a three-chain cover of lengths

`(4+s+t,4,3)`,

so the obstruction persists for arbitrarily large and arbitrarily asymmetric chain lengths. This is an infinite exact family, not a finite-census conclusion.

## 8. Exact verification

Authoritative verifier: `verify_greedy_fringe_2cycle.py`.

- execution/source SHA-256: `c61e836cf62b42b369a137c98f24ce6bd1c8949a07f2a1a8405b48ee3b0b11bf`
- captured-output SHA-256: `de017ae20bdf1d48b668bca647aee71b9b1d73f11c84d995aedb956aeffd2cb3`
- terminator: `POS3_GREEDY_FRINGE_2CYCLE_PASS`

The checker enumerates all 932 linear extensions with weight one, verifies the three-chain cover and width witness, checks connectedness and the exact autonomous modules, prints all 18 incomparable-pair probabilities, verifies both crossed-neighborhood identities and both greedy choices, proves the exact two-cycle, and checks the two fleet03/B10 conditioning children have equal predecessor sets with the stated balanced probabilities.

The discovery search was heuristic and is not used as evidence. Every promoted numerical claim is recomputed deterministically from the displayed transitive reduction.

## 9. Accepted step and remaining obligation

**Classification:** `CANDIDATE_REFUTED` for `LOCAL-GREEDY-PROGRESS`; POS3 remains **OPEN**.

The first essential missing implication is now:

> **GLOBAL-ANTI-CYCLE / MAJORITY-LATE TRANSPORT.** In a cardinality-minimal no-balanced width-three candidate, use the module-prime/strong-majority-block/rank-pinning structure to show that the lead's outward fringe transport cannot cycle, or replace the greedy selector by a quantitatively charged selector with a proved well-founded global potential. In the complementary larger-predecessor-majority-late conditioning branch, a balanced equal-predecessor child must force some possibly different original pair into the balance interval; same-pair scaling is insufficient.

The two nontrivial autonomous modules in this adversary show one plausible source of a global anti-cycle invariant, but no theorem that module-primality alone excludes all such cycles is claimed here. That is a valid next proof target rather than an inferred conclusion.

## 10. Integrity

No target closure, novelty, or priority is claimed. No biased induced law is substituted for the actual uniform law. No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email, Drive, public posting, paid model/API/Codex execution, remote workflow, permission change, or production-brain mutation was used.
