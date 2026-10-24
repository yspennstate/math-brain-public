# B19 POS3 — global chain-profile determinant and a width-three repeated-return counterexample

Outcome: `ESSENTIAL_STEP_APPLIED`  
Parent target: **OPEN / NOT PROVED**  
Execution context: `WITHOUT_VERIFIED_BRAIN`

## Source-bound inputs consumed

Fresh owner control was read at commit `b798d25bb0bc4b4cb91ba09e33bee4858068d599`, revision `2026-09-22.2`, programme `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. The later owner control supersedes the historical installation language, so this run did no installation or benchmark work.

Named OTHER-account mathematics used directly:

1. **account02/B10 run `20260922T064948Z-b10-a11`**, handoff blob `bc7b56b0f40e2a1a1ff27f0a8f85b61465d60f12`. Its exact first-boundary theorem identifies the overload as a failed-swap defect, localizes reverse defects to at most four Hasse channels, and proves immediate old-endpoint return uses a disjoint full-extension reservoir. Its residual is `POS3-RAY-RETURN-FRESH-MASS-v1`.
2. **campaign lead account04/B10 r17**, handoff blob `f5a263be6f1255619bc09574c10833602f1b8b85`. It resolves comparable same-ray blockers by a strict strip and anti-aligned incomparable blockers by a positive anchor-free minority, leaving the coherent aligned width-saturating three-antichain gate (`COHERENT-GATE EXIT`).

The previous B19 run proposed that fixed-profile variation diminution might force a genuinely new profile endpoint before a second return. This run audits that implication rather than assuming it.

## 1. Exact prefix/suffix factorization for an adjacent chain-profile swap

Delete a chain `C={c_1<...<c_m}` and put `Q=P\C`. Every `q in Q` has the exact admissible chain-prefix interval

`I(q)=[lambda(q),rho(q)] subset {0,...,m}`.

Fix a linear-extension skeleton of `Q` in which incomparable elements `u,v` are adjacent. Write

`A=I(u)`, `B=I(v)`.

Let `p_s` be the exact number of admissible chain-state assignments on the prefix ending at state `s`, and let `q_t` be the exact number of admissible assignments on the suffix beginning at state `t`. Define cumulative prefix/suffix weights

`U_j = sum_{s<=j} p_s`,

`V_j = sum_{t>=j} q_t`.

Then the exact numbers of full lifts of the two adjacent skeletons are

`N(uv)=sum_{x in A} sum_{y in B, x<=y} U_x V_y`,

`N(vu)=sum_{y in B} sum_{x in A, y<=x} U_y V_x`.

This follows simply by choosing the two chain-prefix states `x,y`: there are `U_x` legal prefix assignments ending no later than `x`, and `V_y` legal suffix assignments beginning no earlier than `y`. These factors are independent once `x,y` are fixed. No projected law on `L(Q)` is replaced by a uniform law.

### 1.1 Endpoint-ordered profiles

Suppose

`A=[a,b]`, `B=[c,d]`, with `a<=c<=b<=d`.

Set `L=[a,c-1]`, `O=[c,b]`, `R=[b+1,d]`, and abbreviate

`U_X=sum_{j in X} U_j`, `V_X=sum_{j in X} V_j`.

All contributions inside `O x O` cancel under relabelling. The surviving ordered regions are exactly `L x O`, `L x R`, `O x R`. Therefore

`N(uv)-N(vu) = U_L V_O + U_L V_R + U_O V_R >= 0`.

Thus the fixed-direction theorem survives with completely arbitrary exact prefix and suffix multiplicities.

### 1.2 Nested profiles: determinant formula

Now suppose

`A=[a,b] subset B=[c,d]`.

Set `L=[c,a-1]` and `R=[b+1,d]`. Again the `A x A` contribution cancels exactly. The only positive excess consists of an inner state followed by a right-tail state; the only negative excess consists of a left-tail state followed by an inner state. Hence

`Delta := N(uv)-N(vu) = U_A V_R - U_L V_A`.       (1)

This is the global weighted version of the previous one-fiber formula `o(r-ell)`. It compresses *all* outside-skeleton multiplicities into four nonnegative scalar pressures. In particular, when all four terms are positive,

`Delta >= 0  iff  V_R/V_A >= U_L/U_A`.

So a nested return is a competition between one exact right-suffix pressure and one exact left-prefix pressure; profile endpoints alone do not determine the sign.

## 2. The endpoint-freshness inference is false

The preceding run correctly proved that each fixed interval-transfer operator is variation diminishing as a function of its boundary-state coordinate. It does **not** follow that the scalar determinant (1), evaluated after successive insertions, can reverse sign only once. Successive insertions change the cumulative pressure vector itself.

Here is an explicit source-valid width-three family realizing a `+,-,+` defect sequence while reusing exactly the same profile endpoint.

Take the deleted chain

`C: c1 < c2 < c3`.

For `k=0,1,2`, let the remaining elements be covered by two chains

`D: p1 < p2 < p3 < u < s2`,

`E_k: j1 < ... < jk < v < s1 < s3`,

with the obvious omission of the `j` elements when `k=0`. There are no cross-relations between `D` and `E_k` except those forced transitively through `C`. Assign chain-prefix profiles

`I(p1)=[0,1]`,

`I(p2)=I(p3)=[0,2]`,

`I(ji)=[0,1]` for every inserted `ji`,

`I(u)=[1,2]`,

`I(v)=I(s1)=I(s3)=[0,3]`,

`I(s2)=[2,3]`.

Equivalently, profile `[lambda,rho]` means `c_i<q` for `i<=lambda`, `q<c_i` for `i>=rho+1`, and incomparability with the intervening chain elements. Along each of `D,E_k` both profile endpoints are nondecreasing, so these relations are consistent. Since the whole poset is the union of the three chains `C,D,E_k`, its width is at most three; the verifier finds width exactly three.

Fix the valid `Q`-skeleton

`tau_k = p1,p2,p3,j1,...,jk,u,v,s1,s2,s3`

and its adjacent swap `tau'_k` obtained by replacing `u,v` by `v,u`. The two elements are incomparable because their profiles overlap and they lie in different `Q`-chains.

The exact chain-lift counts are

- `k=0`: `W_C(tau_0)=93`, `W_C(tau'_0)=91`, defect `+2`;
- `k=1`: `W_C(tau_1)=85`, `W_C(tau'_1)=86`, defect `-1`;
- `k=2`: `W_C(tau_2)=102`, `W_C(tau'_2)=101`, defect `+1`.

The inserted element has the *same profile* `[0,1]` on both insertions. The nested pair profiles remain `A=[1,2] subset B=[0,3]` throughout. There is no new `lambda` or `rho` endpoint at the second reversal.

The determinant formula explains the numbers exactly. The suffix pressure is fixed at

`(V_A,V_R)=(11,1)`,

while `(U_A,U_L)` evolves as

`(13,1) -> (10,1) -> (12,1)`.

Thus (1) gives

`13-11=+2`, `10-11=-1`, `12-11=+1`.

This is a genuine width-three poset construction, not an arbitrary nonnegative DP vector. The full-poset extension counts are respectively `4290`, `11546`, `25770`; in every member of the family the incomparable pair `(c3,s2)` is exactly balanced with half the extensions in each order. Therefore these are **not** counterexamples to POS3. They are a counterexample only to the intermediate claim that a second same-ray return must change a chain-profile endpoint.

## 3. Consequence for the team proof architecture

The source-valid `+,-,+` family means the proposed residual

`POS3-COHERENT-ENDPOINT-REUSE-EXCLUSION`

is false if interpreted as an endpoint-only theorem. The fixed-profile variation-diminishing statement remains valid in its actual scope—sign variation across a boundary-state vector at one stage—but it cannot by itself forbid repeated temporal return after the state distribution is updated.

This correction makes the account02/B10 result more important, not less: its immediate-return theorem is expressed in **actual full-extension mark sets**, not merely in profile endpoints. The correct residual must retain that mass identity.

### New first essential missing implication: `POS3-COHERENT-MARKED-MASS-NONRECYCLING`

At the account04/B10 coherent aligned three-antichain gate, prove that every second-or-later same-ray return satisfies at least one of:

1. its failed-swap mark packet is disjoint from the previously charged outbound packet (or admits an injection into a genuinely fresh full-extension reservoir);
2. the return strictly decreases the canonical strong-majority span / reaches an already controlled opposite-ray or exact-two state;
3. a balanced pair or proper autonomous/ordinal reduction occurs.

Profile-endpoint freshness is **not** a valid substitute for item 1.

## 4. Compact conditional end-to-end argument

A minimal-counterexample route now has a clean conditional form.

1. Enter the established exact-two corridor and stop at the first non-exact-two boundary under the original uniform full-extension law.
2. Apply account02/B10 `a11`: the overload is an exact failed-swap defect, one of at most four Hasse channels carries the required outbound marks, and immediate return cannot reuse those marked extensions.
3. Apply lead account04/B10 r17: comparable same-ray blockers have a strict strip; anti-aligned incomparable blockers produce an anchor-free positive minority; only the coherent aligned gate remains.
4. Use (1) to represent every chain-deletion nested swap in that gate with its exact prefix/suffix pressures. Do **not** infer monotonicity from unchanged endpoints; the family in section 2 forbids that shortcut.
5. **If `POS3-COHERENT-MARKED-MASS-NONRECYCLING` holds**, each nonterminal coherent return either consumes a new disjoint full-extension packet or strictly descends a finite structural parameter. Since `L(P)` and the poset are finite, this process cannot continue indefinitely. It must hit balance or one of the already controlled reduction/exit alternatives, contradicting a minimal counterexample.

Thus the first missing implication is no longer an endpoint-reuse statement; it is a full-extension marked-mass nonrecycling statement.

## 5. Verification

A deterministic standard-library verifier checks independently:

- the three exact skeleton lift pairs `(93,91)`, `(85,86)`, `(102,101)`;
- the determinant pressures `(13,1,11,1)`, `(10,1,11,1)`, `(12,1,11,1)`;
- width exactly three for all three constructed posets;
- validity of both adjacent `Q`-skeleton orders and incomparability of `u,v`;
- full linear-extension totals `4290`, `11546`, `25770`;
- exact half-probability for `(c3,s2)` in each family member.

The captured regression output ends

`POS3_NESTED_PRESSURE_RETURN_COUNTEREXAMPLE_PASS`.

The symbolic theorem in section 1 is proved independently of the computation; the computation is regression and construction verification only.

## 6. Honest status

POS3 remains open. This run contributes a stronger exact chain-insertion recurrence and, more importantly, removes an incorrect potential shortcut before it can enter a full proof. The team should preserve the valid spatial variation-diminishing lemma but should **not** use it to claim temporal endpoint nonreuse. The next proof step must track actual marked full-extension mass (or a strict finite structural descent) through the lead's coherent gate.
