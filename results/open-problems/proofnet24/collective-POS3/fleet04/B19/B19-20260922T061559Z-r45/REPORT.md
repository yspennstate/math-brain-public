# POS3 fleet04/B19 — active blocker mass compresses to six canonical Hasse channels

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run continues `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. It performs no installation or benchmark work. Every probability below is under the uniform law on all full linear extensions of the original poset.

## 1. Exact collective state consumed

The latest complete team-lead report available at the start of the proof work is

- **fleet04/B10 r14**, `proofnet24/collective-POS3/fleet04/B10/20260922T051259Z-B10-POS3-r14/REPORT.md`, Git blob `50bac494667235f3630991a512438eac42c30521`.

Its bridge theorem produces, in the surviving bridged blocker branch of a hypothetical no-balanced width-three poset, a cover

`x lessdot y`, `a||x,y`,

with

`p:=Pr(x<a)>2/3`, `q:=Pr(y<a)<1/3`,

hence the literal middle event

`H={x<a<y}` has `Pr(H)=p-q>1/3`.

The required named **OTHER-account assigned partner** result consumed and applied is

- **fleet01/B10 r11**, `proofnet24/collective-POS3/fleet01/B10/20260922T045216Z-fleet01-B10-pos3-r11/REPORT.md`, Git blob `7ab3502e574d795c8300fd0ec70dc33f12b87f0a`.

It proves exact same-anchor TP2/PQD for three-chain full-extension flux. In particular, if `r,s` are both incomparable with an anchor `z`, then

`Pr(z<r and z<s) >= Pr(z<r)Pr(z<s)`,

and dually for the reverse tails. I use this only for same-anchor canonical channel pairs; no cross-anchor FKG claim is made.

The immediate same-account input is

- **fleet04/B20**, `proofnet24/collective-POS3/fleet04/B20/20260922T054301Z-b20-auto11-pos3/REPORT.md`.

It proves the two-sided active-blocker theorem. Writing `E=e(P)` and partitioning extensions into

`A={a<x<y}`, `H={x<a<y}`, `C={x<y<a}`,

it defines the middle extensions for which the position swap `x <-> a` is invalid (`B_L`) and those for which `a <-> y` is invalid (`B_R`), and proves

`|B_L| >= H-A`, `|B_R| >= H-C`,

or, after division by `E`,

`Pr(B_L) >= 2p-q-1`, `Pr(B_R) >= p-2q`.

Every bad left swap contains an intervening blocker of one of the two relation types

`(L1) x<v, v||a`, or `(L2) v<a, v||x`,

and every bad right swap contains one of

`(R1) a<w, w||y`, or `(R2) w<y, w||a`.

The left- and right-capable vertex sets are disjoint, and every active blocker lies off any saturated bridge chain containing `x lessdot y`. Its first unpaid step is **individualization/recycling**: a priori the positive blocker mass could be spread over arbitrarily many off-bridge vertices.

A compatible OTHER-account structural input, used for the interpretation of the remaining step, is fleet03/B19's crossed-recycler theorem at commit `ad387a28ee5b6fc514a29662ea5de50d784473f1`: exact-two crossed recycling cannot close on a fixed five/six-vertex core, but a global reuse cycle has not yet been excluded.

## 2. Compact conditional route

Assume a cardinality-minimal width-at-most-three counterexample and work in its inherited transitive strong-majority order `prec_*`.

The current bridged route is now:

1. lead r14 produces the heavy cover `x lessdot y`, `a||x,y`, with middle mass `H/E=p-q>1/3`;
2. B20 converts the excess middle mass into two disjoint, weighted, off-bridge active-blocker families;
3. **new here:** width three compresses every bad left swap to one of at most **three canonical Hasse blockers**, and every bad right swap to one of at most **three canonical Hasse blockers**, without losing a single bad extension;
4. consequently two distinct canonical vertices, one from each side, already carry a total assigned blocker incidence at least `H-E/3`;
5. if strict strong-majority span descent is absent, every one of these canonical blockers lies outside the majority interval `x prec_* a prec_* y`;
6. the assigned partner TP2 theorem then gives an exact adaptive bound converting the active-swap deficit into an actual canonical incomparable-pair minority probability.

Thus the arbitrary-family individualization loophole is closed. The remaining problem is global reuse of this bounded canonical frontier across successive heavy states.

## 3. Canonical fringe sets

For the left pair `(x,a)` define

`T_L = Max{t : t<a and t||x}`,
`U_L = Min{s : x<s and s||a}`.

For the right pair `(a,y)` define

`U_R = Min{u : a<u and u||y}`,
`T_R = Max{r : r<y and r||a}`.

### Lemma 3.1 — width-three Hasse compression

Under `width(P)<=3` and `x lessdot y`, the following hold.

1. Every `t in T_L` satisfies `t lessdot a`, and `|T_L|<=2`.
2. Every `s in U_L` satisfies `x lessdot s`, and `|U_L|<=2`.
3. Every `u in U_R` satisfies `a lessdot u`, and `|U_R|<=2`.
4. Every `r in T_R` satisfies `r lessdot y`, and `|T_R|<=2`.
5. `y in U_L` and `x in T_R`.

#### Proof

Take `t in T_L`. If `t<z<a`, then `z<x` would imply `t<x`, while `x<z` would imply `x<a`; both are impossible. Hence `z||x`, so `z` would lie in the same defining set above `t`, contradicting maximality. Thus `t lessdot a`. The elements of `T_L` are pairwise incomparable and each is incomparable with `x`; therefore `{x} union T_L` is an antichain and width three gives `|T_L|<=2`.

The other three assertions are the order-dual/endpoint analogues. For example, if `s in U_L` and `x<z<s`, then `z<a` would imply `x<a`, while `a<z` would imply `a<s`, contradicting `s||a`; therefore `z||a` and minimality is contradicted. So `x lessdot s`, and `{a} union U_L` is an antichain, giving `|U_L|<=2`.

Finally `x lessdot y` and `y||a` place `y` in the defining set of `U_L`; the cover relation makes it minimal there. Dually `x in T_R`. `square`

Define the **active canonical sets**

`C_L = T_L union (U_L\{y})`,
`C_R = U_R union (T_R\{x})`.

By Lemma 3.1,

`|C_L|<=3`, `|C_R|<=3`.                                        (3.1)

## 4. Every bad swap has a canonical Hasse blocker

### Theorem 4.1 — exact canonical active-blocker compression

For every middle extension `L in H={x<a<y}`:

- the swap `x <-> a` is invalid **iff** at least one member of `C_L` occurs strictly between `x` and `a` in `L`;
- the swap `a <-> y` is invalid **iff** at least one member of `C_R` occurs strictly between `a` and `y` in `L`.

Consequently the B20 bad-event families admit exact partitions over at most three Hasse channels per side.

#### Proof: left side

B20's blocker characterization says that a bad left swap contains an intervening vertex `v` of type L1 or L2.

If `v` is L2, so `v<a` and `v||x`, choose a maximal element `t` of `{z:z<a,z||x}` above `v`. Then `t in T_L`. Since `v<=t<a`, every extension with `x<v<a` also has `x<t<a`; hence `t` is an intervening canonical blocker.

If `v` is L1, so `x<v` and `v||a`, choose a minimal element `s` of `{z:x<z,z||a}` below `v`. Then `s in U_L`, and every extension with `x<v<a` has `x<s<=v<a`. The element `s` cannot equal `y`, because the middle class has `a<y`. Hence `s in U_L\{y}` and is an intervening canonical blocker.

Conversely every member of `T_L` occurring between `x` and `a` is an L2 blocker, and every member of `U_L\{y}` occurring there is an L1 blocker, so the swap is invalid. This proves the left equivalence. The right equivalence is identical with R1/R2 and the extrema `U_R,T_R`. `square`

### Exact weights

For each bad left extension choose, deterministically, the first member of `C_L` encountered between `x` and `a`, and write `lambda_v` for the number assigned to `v`. For the right side choose the first member of `C_R` encountered between `a` and `y`, with weights `rho_w`. Then

`sum_{v in C_L} lambda_v = |B_L|`,
`sum_{w in C_R} rho_w = |B_R|`.                                (4.1)

B20's relation-type disjointness gives `C_L cap C_R = emptyset` after the inactive endpoints `y,x` are removed. Positive-weight members are off the saturated lead bridge.

Combining (4.1) with the B20 lower bounds and (3.1), there exist distinct canonical blockers `v in C_L`, `w in C_R` such that

`lambda_v/E >= (2p-q-1)/3`,                                    (4.2)

`rho_w/E >= (p-2q)/3`.                                         (4.3)

Adding,

`(lambda_v+rho_w)/E >= p-q-1/3 = Pr(H)-1/3`.                   (4.4)

Equation (4.4) is the main individualization statement: **all of the heavy-gap excess above the target `1/3` scale can be charged, in this exact incidence sense, to two distinct canonical off-bridge Hasse channels rather than an arbitrarily diffuse blocker family.**

No assertion is made that `lambda_v` itself is an incomparable-pair probability; it is an exact subevent count and is kept distinct from the pair laws below.

## 5. No-descent polarity: canonical channels point outward

The lead uses the transitive strong-majority order. The heavy edge gives

`x prec_* a prec_* y`.                                         (5.1)

Assume there is no strict strong-majority incomparable subspan inside either `(x,a)` or `(a,y)`.

### Theorem 5.1 — outward canonical blocker lemma

Under that no-descent assumption,

- every `t in T_L` satisfies `t prec_* x`;
- every `r in T_R\{x}` satisfies `r prec_* x`;
- every `s in U_L\{y}` satisfies `y prec_* s`;
- every `u in U_R` satisfies `y prec_* u`.

Thus no positive-weight canonical active blocker lies strictly inside the majority interval from `x` to `y`.

#### Proof

For `t in T_L`, the poset relation `t<a` gives `t prec_* a`. If instead `x prec_* t`, then the incomparable pair `(x,t)` lies strictly inside `x prec_* a`, an authorized span descent. Hence `t prec_* x`.

For `s in U_L\{y}`, the relation `x<s` gives `x prec_* s`, while `s||a`. If `s prec_* a`, `(s,a)` is a strict subspan of `(x,a)`, so no descent forces `a prec_* s`. Because `x lessdot y`, the relation `s<y` is impossible. If `y<s`, then already `y prec_* s`; if `s||y` and `s prec_* y`, then `(s,y)` is a strict subspan of `(a,y)`. Hence again `y prec_* s`.

The arguments for `U_R` and `T_R\{x}` are dual. For the last one, `r<y` and `r||a` first force `r prec_* a`; the cover `x lessdot y` rules out `x<r`, so either `r<x` or `r||x`. In the incomparable case, `x prec_* r` would create a strict subspan of `(x,a)`, hence `r prec_* x`. `square`

This pays a second part of the recycling debt: after span descent is removed, the bounded canonical channel frontier cannot recycle through an interior majority vertex. Any continued reuse must come from the outward fringe.

## 6. Applying the assigned partner TP2 theorem

The preceding compression lets the assigned fleet01/B10 TP2 theorem act on the actual active families.

Assume again no span descent and no balanced pair. Let `c` be the largest minority probability among the canonical incomparable pairs attached to `C_L union C_R`:

- for `t in T_L`, the channel event is `{x<t}`;
- for the possible `s in U_L\{y}`, it is `{s<a}`;
- for `u in U_R`, it is `{u<y}`;
- for the possible `r in T_R\{x}`, it is `{a<r}`.

Theorem 5.1 ensures each displayed event is indeed the minority orientation, so `c<1/3`.

If `T_L` has two members, the assigned partner's same-anchor TP2 inequality gives

`Pr( union_{t in T_L}{x<t} ) <= 2c-c^2`.

The possible single `U_L\{y}` channel contributes at most another `c`; therefore

`Pr(B_L) <= 3c-c^2`.                                           (6.1)

Likewise the two possible `U_R` events share anchor `y`, so TP2 gives the same bound for their union, and the possible single member of `T_R\{x}` contributes at most `c`:

`Pr(B_R) <= 3c-c^2`.                                           (6.2)

Together with the B20 lower bounds,

`3c-c^2 >= max(2p-q-1, p-2q)`.                                (6.3)

Since the two quantities on the right sum to `3(p-q)-1`,

`3c-c^2 >= (3(p-q)-1)/2`.                                      (6.4)

Solving the increasing branch on `0<=c<1/3` gives the adaptive selector

`c >= Phi(h) := (3-sqrt(11-6h))/2`, where `h=Pr(x<a<y)>1/3`.   (6.5)

This is not claimed to close POS3: `Phi(h)` tends to zero as `h` decreases to `1/3`. Its value is that the B20 weighted blocker deficit is now tied to an **actual canonical incomparable-pair probability** through the assigned partner's exact full-extension TP2 law, with only six possible Hasse channels and no unsupported cross-anchor correlation.

## 7. Deterministic regression

The companion standard-library verifier `verify_pos3_canonical_blockers.py` exhausts every distinct naturally labelled transitive closure through six vertices, retains width at most three, and checks every cover/middle triple `x lessdot y`, `a||x,y` with at least one middle extension.

It verifies:

- all four canonical extrema sets have size at most two;
- every extremum is the asserted Hasse neighbour;
- `y in U_L`, `x in T_R`;
- both active canonical sets have size at most three;
- for every middle extension, bad left swap iff a canonical left blocker intervenes, and bad right swap iff a canonical right blocker intervenes.

Captured exact output:

```text
n 2 distinct_natural_posets 2 width_le_3 2 cover_middle_states 0 bad_left_extensions 0 bad_right_extensions 0
n 3 distinct_natural_posets 7 width_le_3 7 cover_middle_states 3 bad_left_extensions 0 bad_right_extensions 0
n 4 distinct_natural_posets 40 width_le_3 39 cover_middle_states 64 bad_left_extensions 19 bad_right_extensions 19
n 5 distinct_natural_posets 357 width_le_3 314 cover_middle_states 1211 bad_left_extensions 1598 bad_right_extensions 1598
n 6 distinct_natural_posets 4824 width_le_3 3339 cover_middle_states 23718 bad_left_extensions 96876 bad_right_extensions 96876
total_bad_left_extensions 98493
total_bad_right_extensions 98493
POS3_CANONICAL_ACTIVE_BLOCKER_COMPRESSION_PASS
```

Executed-byte SHA-256 values:

- `verify_pos3_canonical_blockers.py`: `5599efc24ff794ef1bb00d02ced4bf9b27304e3a24609ac683c4f9ae09b5680a`;
- `verify_pos3_canonical_blockers.out`: `776d1fcd569446d63ad3a4b458cbd33b48ee5c4e01b905fe793c7f447923c12c`.

The finite regression is not a proof of the arbitrary-size theorem; Sections 3--6 are symbolic.

## 8. First remaining implication

The arbitrary-family **individualization** half of B20's unpaid step is now paid: the weighted off-bridge blocker mass can always be rerouted, exactly and without measure change, through at most three canonical Hasse channels per side, all pointing out of the current majority interval unless span descent already occurs.

The first genuinely unpaid global implication is now:

> **CANONICAL-FRINGE REUSE ACYCLICITY.** Along successive heavy bridge/shadow/second-blocker states, prove that the outward canonical Hasse channels from Theorems 4.1--5.1 cannot be reassigned to a finite cycle of previously used fringe vertices while every incomparable pair remains outside `[1/3,2/3]`. A valid proof may terminate in a balanced pair, strict majority-span descent, a width-four contradiction, a proper autonomous/ordinal reduction, or a source-valid multi-distinguisher/non-crossed exit carrying the exact channel weights forward.

The fleet03/B19 crossed-recycler theorem already excludes the stationary exact-two five/six-vertex loop. The new bounded canonical frontier removes diffuse branching as an escape. What is still missing is a well-founded global potential for reuse across different heavy states.

## 9. Status and integrity

- team lead fleet04/B10 r14: **CONSUMED/APPLIED**;
- assigned OTHER-account partner fleet01/B10 r11 TP2: **CONSUMED/APPLIED** in Section 6;
- fleet04/B20 active-blocker weights: **CONSUMED/APPLIED**;
- canonical Hasse compression to at most `3+3` active channels: **PROVED**;
- exact two-vertex incidence localization (4.2)--(4.4): **PROVED**;
- outward-majority polarity absent span descent: **PROVED**;
- adaptive partner-TP2 selector (6.5): **PROVED**;
- global canonical-fringe reuse acyclicity: **OPEN**;
- parent POS3 theorem: **OPEN / NOT PROVED**;
- outcome: `ESSENTIAL_STEP_APPLIED`.

No projected/deletion law was treated as uniform. No static different-anchor positive-association claim was used. No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email/Drive material, paid model/API/Codex call, remote workflow, permission bypass, public posting, or brain-installation action is contained in this report.
