# POS3 account01/B11 — finite fork funnel to a strict predecessor-nested endpoint

**Run:** `20260922T031426Z-b11-pos3-r11`  
**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent POS3:** OPEN / NOT PROVED  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact inherited state consumed

The target remains the arbitrary-size width-at-most-three scope of the 1/3–2/3 conjecture under the uniform law on all linear extensions.

This run uses the newest complete campaign-lead candidate

- **account04/B10**, `proofnet24/collective-POS3/account04/B10/20260922T024220Z-B10-POS3-r39/REPORT.md`, blob `c1b4721b079ea67e9176948c7f5ea4cc179c79f3`.

Its proved equal-predecessor channel theorem says that in a hypothetical no-balanced width-three poset, if `a||b`, `Pred(a)=Pred(b)`, and `a prec_* b` in the transitive strong-majority order, then either

1. **span descent:** there is a Hasse blocker `z` with `a prec_* z prec_* b` and `z||b`, or
2. **fork escalation:** there are exactly two Hasse successor blockers `z_1,z_2` of `a`, both strictly after `b` in the strong-majority order, with `{b,z_1,z_2}` a three-antichain and total positive channel mass `>E/3`.

The lead left open whether repeated span-descent/fork-escalation can propagate indefinitely without yielding a contradiction.

The required named OTHER-account result consumed and applied is

- **account02/B19 r13**, `proofnet24/collective-POS3/account02/B19/20260922T022215Z-account02-B19-pos3-r13/REPORT.md`, blob `4eeff46882d7fc03828b4c9a01b9296a78294b08`.

It constructs an exact width-three autonomous-chain family `P_m` for which a quotient balanced pair migrates a linear fraction of the expanded chain: the first balanced replacement depth satisfies

`min_balanced_depth(P_m)/m -> 1-sqrt(2/3)`.

Thus a valid global argument cannot assume that width three forces balance after `O(1)` or `o(m)` local migration. I use this below to delimit what the new funnel theorem legitimately proves: finite reduction to a new structural endpoint, not constant-depth closure.

I also use the previous account01/B11 exact endpoint exchange, report blob `5fdf6f70d35fee1011b67c217b9e177fb197e81a`. For an incomparable pair `x,y` with `Pred(y) subseteq Pred(x)`, if `E=e(P)`, `Q` is the common minimal-successor-blocker event, and `R` is the reverse nonneutral-blocker remainder, then

`p_xy = 1-(Q+R)/(2E)`.                                      (1.1)

## 2. Compact conditional end-to-end route

Assume for contradiction that `P` is a finite width-at-most-three poset with no balanced incomparable pair. The inherited minimal-counterexample state supplies a transitive strong-majority total order `prec_*`. At the first boundary, the lead reduces the clean sibling branch to an equal-predecessor extreme pair.

The missing structural question is whether the lead's fork escalation merely creates an uncontrolled new fork forever. The theorem below answers **no**: every run of clean equal-predecessor fork escalations is finite, and its first exit is an extreme incomparable pair whose predecessor sets are **strictly nested**. That pair lies exactly in the scope of the previous endpoint exchange identity (1.1).

So the surviving proof route becomes

`first boundary -> clean equal-Pred pair -> finite fork funnel -> strict Pred nesting -> exact endpoint exchange -> global mass inequality`.

The first unpaid implication is no longer termination of the fork process. It is a quantitative inequality for the strict predecessor-nested endpoint, stated in Section 6.

## 3. Width-three predecessor nesting at a two-cover fork

### Lemma 3.1 — fork siblings have nested predecessor sets

Let `P` have width at most three. Suppose

- `a||b` and `Pred(a)=Pred(b)`,
- `a lessdot u` and `a lessdot v`,
- `u||v`, `u||b`, and `v||b`.

Then `Pred(u)` and `Pred(v)` are nested: either

`Pred(u) subseteq Pred(v)`

or

`Pred(v) subseteq Pred(u)`.

#### Proof

Assume not. Choose

`d in Pred(u)\Pred(v)`, `e in Pred(v)\Pred(u)`.

First, `d||a`. Indeed, `d<a` would imply `d<a<v`, contradicting `d notin Pred(v)`, while `a<d<u` contradicts the cover `a lessdot u`. Similarly `e||a`.

Next, `d||b`. If `d<b`, then `d in Pred(b)=Pred(a)`, contradicting `d||a`. If `b<d<u`, then `b<u`, contradicting `b||u`. Thus `d||b`; similarly `e||b`.

Also `d||v`: `d<v` is excluded by the choice of `d`, while `v<d<u` would imply `v<u`, contradicting `u||v`. Likewise `e||u`.

Finally `d||e`. If `d<e<v`, then `d<v`, contradiction; if `e<d<u`, then `e<u`, contradiction.

Therefore `{a,b,d,e}` is a four-element antichain, impossible when `width(P)<=3`. Hence the predecessor sets are nested. `square`

This is exactly the width-three constraint that was missing from the fork iteration: two incomparable successor channels cannot independently acquire lower witnesses on opposite sides.

## 4. A strict nested exit carries at most two lower Hasse blockers

### Lemma 4.1 — maximal predecessor difference is a two-channel Hasse interface

Let `x||y` and

`Pred(y) proper_subset Pred(x)`.

Put

`D=Max(Pred(x)\Pred(y))`.

Then every `d in D` satisfies `d lessdot x` and `d||y`; `D` is an antichain; and if `width(P)<=3`, then `1<=|D|<=2`.

#### Proof

For `d in D`, `d<y` is impossible because then `d in Pred(y)`. Also `y<d<x` would imply `y<x`, contradicting `x||y`. Thus `d||y`.

If `d<w<x`, then `w<y` would imply `d<y`, impossible; `y<w<x` would imply `y<x`, impossible; and `w||y` would place `w` in `Pred(x)\Pred(y)` strictly above `d`, contradicting maximality. Hence no such `w` exists and `d lessdot x`.

Maximal elements of the difference form an antichain. Since each is incomparable with `y`, three distinct members together with `y` would form a four-antichain. Thus width at most three gives `|D|<=2`. Strict inclusion gives `D` nonempty. `square`

So the first non-clean exit has a genuine one- or two-channel lower Hasse interface, dual to the one- or two-channel minimal-successor interface already used by the endpoint exchange.

## 5. Finite clean-fork funnel theorem

Call an ordered incomparable pair `(a,b)` **clean extreme** when `Pred(a)=Pred(b)` and `a prec_* b`. In a no-balanced candidate this means `Pr(a<b)>2/3`.

### Theorem 5.1 — clean fork escalation cannot persist indefinitely

Let `P` be finite of width at most three with no balanced incomparable pair. Starting from any clean extreme pair `(a_0,b_0)`, repeatedly apply the lead's span-descent/fork-escalation theorem. Whenever fork escalation occurs and its two successor blockers have equal predecessor sets, order those blockers by `prec_*` and continue with them as `(a_{i+1},b_{i+1})`.

Then after finitely many steps the process produces an extreme incomparable pair `(x,y)` with **strictly nested predecessor sets**.

More precisely, at each continued clean fork step

`a_i prec_* b_i prec_* a_{i+1} prec_* b_{i+1}`,               (5.1)

so if `rho(v)` denotes the position of `v` in the strong-majority total order,

`rho(a_{i+1}) >= rho(a_i)+2`.                                 (5.2)

Hence at most `floor((|P|-rho(a_0))/2)` clean fork continuations are possible.

#### Proof

Apply the lead theorem at `(a_i,b_i)`.

**Span-descent case.** There is a blocker `z` with `a_i<z`, `z||b_i`, and `a_i prec_* z prec_* b_i`. Since `Pred(a_i)=Pred(b_i)`, every predecessor of `b_i` is below `a_i`, hence below `z`. Moreover `a_i in Pred(z)` but `a_i notin Pred(b_i)`. Therefore

`Pred(b_i) proper_subset Pred(z)`.

Thus `(z,b_i)` is already the desired strict predecessor-nested incomparable pair.

**Fork-escalation case.** There are exactly two Hasse blockers `u,v`, both strictly after `b_i` in `prec_*`. By Lemma 3.1 their predecessor sets are nested. If the nesting is strict, `(u,v)` is the desired exit. If the predecessor sets are equal, orient them by `prec_*` as `(a_{i+1},b_{i+1})`. Because both lie strictly after `b_i`, (5.1) holds, hence (5.2).

A finite total order cannot contain infinitely many strict position increases. Therefore a clean fork continuation must terminate, and the only terminating alternatives above are strict predecessor-nested incomparable pairs. `square`

### Corollary 5.2 — the lower-distinguisher branch is canonical

If the terminal pair comes from a fork and `Pred(y) proper_subset Pred(x)`, then every maximal lower distinguisher belongs to the set `D` of Lemma 4.1. Thus the vague statement “the siblings eventually acquire a lower distinguisher” sharpens to a one- or two-element set of Hasse predecessors of `x`, all incomparable with `y`.

This converts the lead's two branches into one endpoint geometry: either span descent or unequal fork siblings, but in both cases one reaches a strict predecessor-nested endpoint with at most two lower Hasse channels.

## 6. Exact endpoint consequence and the new first missing implication

Take the terminal pair and label it `(x,y)` so that

`Pred(y) proper_subset Pred(x)`.

The previous account01/B11 endpoint theorem applies exactly. Let `M=Min{z:x<z and z||y}`, let `Q` count extensions in which `y` precedes every member of `M`, and let `R` count reverse extensions `y<x` whose open interval contains an endpoint-nonneutral element. Then

`Pr(x<y)=1-(Q+R)/(2E)`.                                      (6.1)

Because there is no balanced pair, exactly one of the two strict regimes holds:

`Pr(x<y)>2/3  =>  Q+R<2E/3`,                                 (6.2)

`Pr(x<y)<1/3  =>  Q+R>4E/3`.                                 (6.3)

The lower predecessor-difference interface `D` from Lemma 4.1 has size one or two, and the usual width-three argument gives `|M|<=2` as well. Thus the unresolved endpoint has a bounded **two-sided Hasse interface**, even though the distance needed to locate a balanced pair need not be bounded.

The first essential missing implication is now:

> **Nested-endpoint mass lemma.** In the source-exact minimal-counterexample setting, use the global three-chain heavy-slice / rank-atom constraints and the delayed-distinguisher structure to rule out both extreme alternatives (6.2) and (6.3) for the strict predecessor-nested endpoint produced by Theorem 5.1; equivalently force
>
> `2E/3 <= Q+R <= 4E/3`.

By (6.1), that immediately yields a balanced pair and closes this branch.

This is materially narrower than the previous obligation “show fork escalation terminates”: termination is now proved. What remains is an exact global mass inequality on a pair with at most two lower and at most two upper Hasse channels.

## 7. Application of account02/B19 r13

The partner family `P_m` proves that no legitimate next step should replace the nested-endpoint mass lemma by a bounded-radius local search. In that family

`Pr(x<c_j)=j/(m+1)`

and the first balanced descendant lies at asymptotic depth

`(1-sqrt(2/3))m`.

Therefore width three by itself does not imply that a balance witness appears within `O(1)` or `o(m)` local moves from a selected endpoint/module boundary. The finite funnel theorem above avoids that false strengthening: it guarantees only that repeated **clean equal-predecessor fork escalations** cannot continue forever and must exit to strict predecessor nesting. It makes no constant-depth claim about where the eventual balanced pair lies.

This is the substantive use of the assigned partner result: it rules out a tempting overinterpretation of Theorem 5.1 and points the next proof toward a global mass conservation/three-chain argument rather than a bounded-neighborhood selector.

## 8. Status

- Width-three fork-sibling predecessor nesting: **PROVED**.
- Strict nested predecessor pair has one/two maximal lower Hasse blockers: **PROVED**.
- Finite clean-fork funnel to a strict predecessor-nested endpoint: **PROVED**, conditional on the lead's already proved equal-predecessor span-descent/fork-escalation theorem and the inherited no-balanced strong-majority setting.
- Exact endpoint formula at the terminal pair: **PROVED previously and applied exactly**.
- Nested-endpoint mass lemma: **OPEN / FIRST ESSENTIAL MISSING IMPLICATION**.
- Parent POS3: **OPEN / NOT PROVED**.
- Inherited finite frontier `n_bal=14`: unchanged.

No finite computation was used in this run's proof. No novelty/priority claim is made. No benchmark gold or keys, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email, Drive, paid model/API/Codex execution, remote workflow, public posting, permission change, or production-brain mutation was used.
