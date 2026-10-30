# POS3 fleet02/B10 — exact two-deletion endpoint coupling and blocker-corridor obstruction

**Run:** `20260922T011840Z-b10-pos3-r11`  
**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose uniform-linear-extension ordering probability lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

This run derives an exact adjacent-swap/deletion coupling that keeps every conditioning multiplicity, applies it to the first and last strong-majority block boundaries, and then uses an exact nine-element other-account witness to refute the tempting stronger claim that the resulting fiberwise corridor inequality follows from local width-three/module-prime endpoint geometry alone.

## 1. Fresh source-bound state consumed

The current owner control is revision `2026-09-22.2`, programme `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`, which stops new benchmark/installation work and assigns this slot to POS3. The scientific work below uses the true uniform law on `L(P)` throughout.

The following completed OTHER-account results were read and applied.

1. **Campaign lead `fleet04/B10`**, run `20260922T011127Z-fleet04-B10-POS3-r11`, report blob `1e5a9682e4f90f38484a86e7199428de0b0160f8`. It proves that in any width-three counterexample every element has its strong-majority rank atom with probability `>1/81`, equivalently the exact central three-chain flux cell satisfies `81 W_x(g_b(x),g_c(x)) > E`.
2. **Named partner `fleet03/B11`**, report blob `5b65cb3c68a668e553dc6465252bc6cb82b68b8d`. It proves the exact order-polytope swap-defect identity and the width-three double-blocker certificate. At the first strong-majority block boundary the positive defect has exactly two canonical minimal successor blockers and no predecessor blockers; the last boundary has the dual structure.
3. **`fleet01/B10`**, report blob `3a0d4e63665646adc853bb48192eba0f81629a15`. It gives the exact unit-weight three-chain ideal-state path model and `>E/3` majority-gap heavy-slice normal form, explicitly retaining the third-chain lift multiplicities.
4. **`fleet03/B19`**, run `20260922T010520Z-b19-pos3-r11`, report blob `b32278d17e70387d51be17fd0d0ac912bae48f5e`. Its exact self-dual nine-element module-prime witness has `E=349`, first endpoint pair `(0,1)` with probability `244/349>2/3`, no extremal balanced pair, and only two interior balanced pairs. It already refutes connected/module-prime/endpoint-only light-slice shortcuts.

The new coupling below is independent of the three-chain cover and does not condition on a falsely uniform deletion law.

## 2. Exact two-element deletion fibers

Let `x || y` in a finite poset `P`. Fix a linear extension

`tau in L(P \ {x,y})`

of the remaining `m=|P|-2` elements. Index the `m+1` gaps of `tau` by `0,...,m`. For `z in {x,y}`, define

`ell_z(tau) = max{ position_tau(a) : a <_P z }`, with empty maximum `0`,

`u_z(tau) = min{ position_tau(b)-1 : z <_P b }`, with empty minimum `m`.

The legal insertion gaps for `z` form the integer interval

`I_z(tau)=[ell_z,u_z]`.

This is exact: inserting `z` in any gap in `I_z` and only such a gap preserves all order relations involving `z`.

Write

`N_xy(tau)=# {L in L(P): L restricted to P\{x,y}=tau and x precedes y}`,

and define `N_yx(tau)` dually.

### Lemma 2.1 — exact conditional counts

For every `tau`,

`N_xy(tau) = #{(i,j) in I_x x I_y : i<j} + #{i in I_x cap I_y}`,

`N_yx(tau) = #{(i,j) in I_x x I_y : i>j} + #{i in I_x cap I_y}`.

The equal-gap term occurs in both formulas because if `i=j`, the two incomparable elements can be inserted in either order, producing two distinct extensions.

**Proof.** Delete `x,y` from any extension. Their positions relative to the remaining word determine unique legal gaps `(i,j)`. If `i<j`, only `x<y` results; if `i>j`, only `y<x`; if `i=j`, both internal orders are legal because `x||y`. Conversely every such legal choice reconstructs a unique extension. `□`

Consequently, if

`C(tau)=N_xy(tau)+N_yx(tau)`, `E=e(P)`,

then under the actual uniform law on `L(P)`,

`Pr(restriction=tau)=C(tau)/E`,

and

`Pr(x<y)=sum_tau [C(tau)/E] [N_xy(tau)/C(tau)] = E^{-1} sum_tau N_xy(tau)`.

Thus the induced law on deleted words is generally **weighted by `C(tau)`**, not uniform. The formula retains every conditioning weight exactly.

## 3. First-boundary coupling: unmatched right and left fringes

Assume now that `x,y` form the **first adjacent incomparable boundary** in the transitive strong-majority order of a hypothetical POS3 counterexample, with `x prec_* y`.

By the named-partner endpoint theorem there is no predecessor blocker for this pair. Hence every predecessor of `y` is also a predecessor of `x`:

`Pred(y) subseteq Pred(x)`.

Indeed if `z<y` but `z` were incomparable with `x`, it would be a predecessor blocker, while `x<z<y` is impossible because `x||y`. Therefore for every deleted word `tau`,

`ell_y <= ell_x`.

Set

`I_x=[a,b]`, `I_y=[c,d]`, with `c<=a`.

There are two cases.

### Lemma 3.1 — the nonhelpful case `d<=b`

Put `h=max(0,d-a+1)`. Then

`N_xy = h(h+1)/2`,

`N_yx = |I_x||I_y| - h(h-1)/2`,

and therefore `N_xy<=N_yx`.

**Proof.** An `x<y` completion is exactly a gap pair with `i<=j`. Since `j<=d<=b`, such pairs exist only in the overlap `[a,d]`, giving `1+...+h`. A `y<x` completion is a pair with `i>=j`; subtracting the `i<j` pairs gives the second expression. Since both intervals contain the overlap, `|I_x||I_y|>=h^2`, which yields the inequality. `□`

So a deleted word with `u_y<=u_x` cannot contribute positive bias toward `x<y`.

### Lemma 3.2 — exact nested-fringe coupling when `d>=b`

Now `I_x subseteq I_y`. Put

`n=b-a+1`, `L=a-c`, `R=d-b`.

Then

`N_xy = nR + n(n+1)/2`,

`N_yx = nL + n(n+1)/2`.

Equivalently,

`N_xy-N_yx = n(R-L)`,

and

`N_xy-2N_yx = n [ R - 2L - (n+1)/2 ]`.

**Coupling proof.** Pair the completions whose `y`-gap lies in the common core `[a,b]` by reversing the relative order of the two legal insertion choices; same-gap completions pair with the opposite same-gap internal order. This leaves exactly `nR` unmatched `x<y` completions, obtained by putting `y` in the right fringe `(b,d]`, and exactly `nL` unmatched `y<x` completions, obtained by putting `y` in the left fringe `[c,a)`. The common paired core contributes `n(n+1)/2` to each orientation. `□`

The exact conditional probability in such a fiber is therefore

`q_tau := Pr(x<y | restriction=tau)`

`= [R+(n+1)/2] / [L+R+n+1]`.

In particular,

`q_tau>2/3` iff `R > 2L + (n+1)/2`.

No uniformization or independent-gap approximation has entered this identity.

## 4. Endpoint blocker-corridor theorem

Because a POS3 counterexample has `Pr(x<y)>2/3`,

`sum_tau N_xy(tau) > 2 sum_tau N_yx(tau)`.

Hence some deleted word has `N_xy(tau)>2N_yx(tau)`. Lemma 3.1 excludes `d<=b`, so Lemma 3.2 gives the following necessary condition.

### Theorem 4.1 — first endpoint corridor

In a width-at-most-three POS3 counterexample, let `x prec_* y` be the first adjacent incomparable strong-majority block boundary. Then there exists

`tau in L(P\{x,y})`

for which, writing `I_x=[a,b]`, `I_y=[c,d]`,

`I_x subseteq I_y`

and

`d-b > 2(a-c) + (b-a+2)/2`.      `(EC+)`

Moreover, if `s` is the first successor of `x` appearing in `tau`, then `s` is one of the two canonical minimal successor blockers from the fleet03/B11 theorem.

**Proof of the blocker statement.** Since `d>b`, the first successor of `x` occurs strictly before the first successor of `y`. Thus this element `s` is not above `y`. It cannot be below `y`, because `x<s<y` would imply `x<y`. Hence `s||y`, so `s in S_x(y)`. If some other element of `S_x(y)` were below `s`, it would be an earlier successor of `x` in `tau`, contradiction. Thus `s` is minimal in `S_x(y)`. Width three and the partner's endpoint theorem leave exactly two such canonical blockers. `□`

So an extreme first-boundary majority cannot be supported merely by an abstract union of two blocker events: at least one exact unchanged-conditioning deletion fiber contains a quantitatively long **successor-blocker corridor**.

There is an exact dual statement at the last boundary.

### Theorem 4.2 — last endpoint corridor

Let `x prec_* y` be the last adjacent incomparable strong-majority block boundary in a POS3 counterexample. Then some `tau` has

`I_y subseteq I_x`.

Writing `I_x=[a,b]`, `I_y=[c,d]`, `n=d-c+1`, `L=c-a`, `R=b-d`, one has

`L > 2R + (n+1)/2`.              `(EC-)`

The last predecessor of `y` in that deleted word is one of the two canonical maximal predecessor blockers from the partner theorem.

This follows by the same counting after order duality; explicitly the two counts are

`N_xy=nL+n(n+1)/2`, `N_yx=nR+n(n+1)/2`.

## 5. The tempting local closure is false

A natural next claim would be that width three, connected incomparability, module-primality, and the endpoint double-blocker geometry already force every first-boundary deletion fiber to obey the reverse of `(EC+)`, which would immediately give `Pr(x<y)<=2/3` after summation.

The fleet03/B19 nine-element witness proves that claim false.

For its first endpoint pair `(x,y)=(0,1)`, exact enumeration gives

`E=349`, `#(x<y)=244`, `#(y<x)=105`.

Deleting `0,1` leaves `105` legal words. The archived verifier for this run recomputes all fibers and finds **45** with `N_xy>2N_yx`. The first is

`tau=(2,3,4,5,6,7,8)`,

`I_x=[0,0]`, `I_y=[0,2]`,

`N_xy=3`, `N_yx=1`.

Thus `n=1,L=0,R=2`, and the corridor inequality is strict:

`R=2 > 1 = 2L+(n+1)/2`.

The exact verifier ends with `POS3_B10_ENDPOINT_FIBER_CHECK_PASS`; its script blob is `0e548aa3f932d960b38c8eba5c2d58f2f459cf6f` and output blob is `d0bf55f6acc0b545fcfd46a51f8eb6790567d15b`.

This witness is **not** a counterexample to POS3: it has the interior balanced pairs `(2,3)` and `(5,6)`. Therefore the failure is precisely informative. A proof cannot forbid endpoint corridor fibers using only local endpoint geometry, connectedness, module-primality, or heavy-slice magnitude; it must use the global **absence of balanced pairs at the interior boundaries**.

## 6. Combined exact residual after applying the lead and partner results

A cardinality-minimal POS3 counterexample would now have to satisfy, simultaneously and under the same uniform law:

1. connected incomparability and no proper autonomous nonchain (inherited reductions);
2. one transitive strong-majority order with at least five maximal chain blocks;
3. every relevant one-chain majority-gap marginal has mass `>E/3` (fleet01/B10);
4. every adjacent block boundary has a double-blocker certificate, with exactly two canonical successor blockers at the first boundary and two predecessor blockers at the last (fleet03/B11);
5. every element's joint majority-rank central cell has mass `>E/81` (campaign lead fleet04/B10);
6. the first and last boundaries each admit at least one exact two-deletion fiber satisfying `(EC+)` and `(EC-)` respectively (this run).

The nine-element witness satisfies much of the local geometry but escapes the global counterexample system through its two interior balanced pairs. This isolates the next obligation much more sharply than a generic 'combine blockers' instruction.

> **First unpaid implication.** Use the no-balanced-pair constraints at the *interior consecutive boundaries*, together with the `>E/81` central-cell pinning and the double-blocker system, to show that the endpoint corridor-surplus fibers cannot have positive total weighted excess
>
> `sum_tau [N_xy(tau)-2N_yx(tau)] > 0`
>
> at both ends of the common strong-majority order.

A one-boundary inequality is source-validly refuted above. The next mechanism must couple deletion fibers or signed flux across at least two consecutive boundaries while retaining their actual completion weights.

## 7. Verification, provenance, and scope

Verifier: `verify_pos3_endpoint_fiber.py`.  
Captured output: `verify_pos3_endpoint_fiber.out`.  
The checker uses exact integer enumeration only and validates the cited nine-element witness and the fiber accounting; the general theorems above are proved symbolically and do not depend on finite enumeration.

The first write attempt for the verifier encountered an ordinary concurrent-branch conflict; after refreshing the repository head, the create-only write succeeded without overwriting peer work. A scoped manual privacy/secret review of the new report, script, and output found only mathematical source data and nonsecret content; no credentials, scheduler identifiers, machine paths, benchmark gold, held-out labels, email/Drive data, or private transcripts are present.

**Claim status**
- exact two-deletion weighted-law identity: **PROVED**;
- first/last endpoint corridor theorems: **PROVED**, conditional only on the already-proved counterexample strong-majority/blocker state;
- local claim that endpoint geometry alone forbids a corridor-violating fiber: **REFUTED** by the exact nine-element source-valid witness;
- combined consecutive-boundary incompatibility: **OPEN**;
- parent width-three `1/3–2/3` target: **OPEN / NOT PROVED**.

No novelty or priority claim is made. No benchmark work, brain installation, held-out benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data, email, Drive, public posting, paid model/API/Codex execution, remote workflow, or permission change was used.
