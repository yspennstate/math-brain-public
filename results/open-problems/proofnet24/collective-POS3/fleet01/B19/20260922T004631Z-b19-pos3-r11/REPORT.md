# POS3 fleet01/B19 — arbitrary-chain swap-defect recurrence

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair with ordering probability in `[1/3,2/3]` under the uniform law on all linear extensions.  
**Parent status after this report:** **OPEN / NOT PROVED**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact collective state consumed

This run continues the assigned chain-deletion/insertion route and does not return to the superseded brain-installation work.

The prior fleet01/B19 report, blob `2c2a46da29d5b4114b5a7f71e6b0072d27b9c437`, proved the exact insertion-corridor multiplicity

`W_C(tau)=#{s_1<=...<=s_m : a_j(tau)<=s_j<=b_j(tau)}`

for a deleted chain `C={c_1<...<c_m}` and `tau in L(P\C)`, together with exact pair numerators. It also disproved the false uniform-deletion shortcut and a universal bounded-density rescue.

**Named OTHER-account result consumed and applied:** fleet04/B20, report blob `514b9fca62e570479d8cc8d0e5c3469468286d2c`, `proofnet24/collective-POS3/fleet04/B20/20260922T001111Z-b20-auto11/REPORT.md`. For a *single* deleted element it proves that one adjacent incomparable swap changes `W` by at most one, gives a canonical neighboring-fiber injection, and explicitly leaves the arbitrary-chain generalization open. The present report solves that local arbitrary-chain generalization in its correct form and shows that the literal `|Delta W|<=1` extension is false.

I also used fleet02/B11 blob `b71c5087c4982769946c31f1ec76242bf297fe17` (minimal counterexample may be taken incomparability-connected), fleet04/B19 blob `ce30dae79d698103f026d4d871033238489b1fb1` (a minimal counterexample has no proper autonomous nonchain), fleet01/B10 blob `3a0d4e63665646adc853bb48192eba0f81629a15` (exact three-chain edge flux and `>e(P)/3` heavy-slice normal form), and the fresh fleet03/B11 blob `5b65cb3c68a668e553dc6465252bc6cb82b68b8d` (double-blocker certificate and a source-valid refutation of a purely local mixed-blocker closure).

At the checked scientific snapshot, the assigned partner `fleet02/B10` had not yet delivered a collective POS3 artifact, so no partner result was fabricated or awaited.

## 2. Compact conditional end-to-end route

Suppose a counterexample exists and choose one of minimum cardinality. The cited collective reductions permit us to work in a width-exactly-three, incomparability-connected core with no proper autonomous nonchain. Fix one chain `C` of a three-chain cover and put `Q=P\C`; then `width(Q)<=2`.

The uniform law on `L(P)` projects to the exact weighted law

`mu(tau) = W_C(tau) / sum_sigma W_C(sigma)`

on `L(Q)`. Thus the known width-two balanced-pair theorem cannot simply be applied under the uniform law and lifted. A valid induction would close if one could control how `W_C` changes under the adjacent incomparable swaps used by a width-two path/exchange argument, while separately allowing a balanced pair involving `C` itself.

The new result below gives the exact arbitrary-chain local swap defect. It shows that all context-independent swaps admit a canonical fiber injection, identifies the unmatched lifts exactly as a short-gap band, and proves that the only possible context-sensitive swaps are **nested chain-profile swaps**. Therefore the first genuinely unpaid implication is no longer “understand arbitrary insertion weights” in general; it is to control the aggregate nested-profile/short-gap defects in the connected module-prime heavy-slice core.

## 3. Dual chain-prefix recurrence

Let

`C={c_1<...<c_m}` and `Q=P\C`.

For each `q in Q`, define

`lambda(q)=max({j : c_j<q} union {0})`,

`rho(q)=min({j-1 : q<c_j} union {m})`,

and the integer interval

`I(q)=[lambda(q),rho(q)] subset {0,...,m}`.

The interval is nonempty: if `c_i<q<c_j`, then `i<j`.

Fix `tau=(q_1,...,q_n) in L(Q)`. In a lift `L in L(P)` restricting to `tau`, let

`t_i = #{c in C : c precedes q_i in L}`.

Then

`0<=t_1<=...<=t_n<=m`

and `t_i in I(q_i)` for every `i`.

### Theorem 3.1 — dual exact fiber recurrence

Restriction to `Q` gives a bijection

`{L in L(P): L|_Q=tau}`

`<-> {t_1<=...<=t_n : t_i in I(q_i)}`.

Consequently

`W_C(tau)=#{t_1<=...<=t_n : t_i in I(q_i)}`.

**Proof.** A lift clearly gives the stated nondecreasing sequence. If `c_j<q_i`, then at least the first `j` chain elements precede `q_i`, so `t_i>=lambda(q_i)`. If `q_i<c_j`, then at most `j-1` chain elements precede `q_i`, so `t_i<=rho(q_i)`.

Conversely, from an admissible sequence insert `c_1,...,c_{t_1}`, then `q_1`, then the next `t_2-t_1` chain elements, then `q_2`, and so on, finally appending the remaining chain elements. The interval inequalities enforce every `C`--`Q` comparability, while `tau` and the chain order enforce the internal relations. The two constructions are inverse. `□`

Thus, with

`D_1(t)=1{t in I(q_1)}`

and

`D_i(t)=1{t in I(q_i)} sum_{s<=t} D_{i-1}(s)`,

we have

`W_C(tau)=sum_t D_n(t)`.

This is an `O(mn)` prefix-sum recurrence dual to the earlier insertion-vector recurrence. The advantage is that an adjacent swap changes only two neighboring interval constraints.

## 4. Exact arbitrary-chain adjacent-swap defect

Let

`tau=(...,u,v,...)`

with `u||v` adjacent in a linear extension of `Q`, and let `tau'` swap them. Fix all chain-prefix coordinates outside these two positions. Let `L` be the preceding prefix count (or the lower sentinel `0`) and `U` the following prefix count (or the upper sentinel `m`). Put

`A=I(u) cap [L,U]=[alpha,beta]`,

`B=I(v) cap [L,U]=[gamma,delta]`

when both are nonempty. The number of local completions in the two orders is

`N_uv(A,B)=#{(a,b) in A x B : a<=b}`,

`N_vu(A,B)=#{(a,b) in A x B : b<=a}`.

### Lemma 4.1 — reflected midpoint comparison

Set

`Delta=(gamma+delta)-(alpha+beta)`.

If `Delta>=0`, then

`N_uv>=N_vu`,

and in fact

`N_uv-N_vu = #{(a,b) in A x B : 0<=b-a<Delta}`.      (4.1)

If `Delta<=0`, the symmetric formula holds after exchanging `A,B` and the order labels.

**Proof.** Assume `Delta>=0`. Reflect a reverse-order pair `b<=a` by

`a' = alpha+beta-a`,

`b' = gamma+delta-b`.

Then `a' in A`, `b' in B`, and

`b'-a' = Delta+(a-b)>=0`,

so `(a',b')` is a forward-order pair. Reflection is injective. Moreover a forward pair `(a',b')` has a reverse-pair preimage iff

`b'-a'>=Delta`.

Hence the image consists exactly of the forward pairs outside the band `0<=b'-a'<Delta`, proving (4.1). `□`

This is the exact arbitrary-chain replacement for a one-element `|Delta W|<=1` rule.

### Theorem 4.2 — context-independent monotonicity for ordered chain profiles

Suppose

`lambda(u)<=lambda(v)` and `rho(u)<=rho(v)`.

Then

`W_C(...,u,v,...) >= W_C(...,v,u,...)`.

More precisely, after conditioning on every outer prefix sequence, the defect is the nonnegative short-gap count in (4.1), and the global difference is the sum of those short-gap counts with their exact prefix/suffix multiplicities.

**Proof.** Common truncation by `[L,U]` preserves both endpoint inequalities, so `alpha<=gamma` and `beta<=delta`, hence `Delta>=0` for every feasible outer context. Apply Lemma 4.1 in each context and sum. `□`

The reverse endpoint order gives the reverse inequality. Thus every endpoint-ordered adjacent swap has an explicit lift injection even for an arbitrarily long deleted chain.

## 5. Exact prefix/suffix defect recurrence

Let `P_r(L)` count feasible prefix vectors through the position immediately before `u` whose last value is `L`, and let `S_{r+2}(U)` count feasible suffix vectors beginning immediately after `v` whose first value is `U`; use the natural sentinels at the two ends. Then

`W_C(tau)=sum_{L<=U} P_r(L) S_{r+2}(U) N_uv(L,U)`,

`W_C(tau')=sum_{L<=U} P_r(L) S_{r+2}(U) N_vu(L,U)`.

For ordered profiles the exact defect is therefore

`W_C(tau)-W_C(tau')`

`= sum_{L<=U} P_r(L) S_{r+2}(U)`

`  * #{(a,b) in A_{L,U} x B_{L,U}: 0<=b-a<Delta_{L,U}}`.      (5.1)

Formula (5.1) is the usable induction bookkeeping: every local loss is represented by an actual set of lifts, not by an uncontrolled density ratio.

## 6. Only nested profiles can have context-dependent swap sign

### Lemma 6.1 — incomparable profiles overlap

If `u||v` in `Q`, then `I(u) cap I(v)` is nonempty.

**Proof.** If `rho(u)<lambda(v)`, then `rho(u)<m`, so

`u<c_{rho(u)+1}<=c_{lambda(v)}<v`,

contradicting `u||v`. The opposite separation similarly forces `v<u`. `□`

Therefore for an incomparable pair the two intervals either have endpoint order in one direction, endpoint order in the other direction, or one interval is properly nested inside the other. By Theorem 4.2 the first two cases have context-independent swap sign. Hence:

> **The only possible context-sensitive adjacent swaps are nested-profile swaps.**

For a nested pair, truncation can genuinely reverse the midpoint order. For example `I(u)=[0,4]`, `I(v)=[1,3]`: on the outer window `[0,2]` the `uv` order is favored, while on `[2,4]` the `vu` order is favored. Thus a global argument must retain the outer prefix state; one scalar weight per element cannot capture the defect.

### Lemma 6.2 — strict nesting produces canonical chain blockers

Suppose `I(v) subset I(u)`.

- If `lambda(v)>lambda(u)`, then `c_{lambda(v)}<v` and `c_{lambda(v)}||u`.
- If `rho(v)<rho(u)`, then `v<c_{rho(v)+1}` and `c_{rho(v)+1}||u`.

**Proof.** The displayed comparabilities follow from the definitions. For the first, `c_{lambda(v)}` cannot lie below `u` because then `lambda(u)>=lambda(v)`, and cannot lie above `u` because then `rho(u)<=lambda(v)-1<rho(v)`, contradicting nesting. Thus it is incomparable with `u`. The second statement is dual. `□`

So the nested-profile obstruction is the chain-corridor version of the blocker geometry isolated by fleet03/B11. If both containments are strict, one gets a predecessor and successor blocker around the more constrained element. The fresh fleet03/B11 six-element example proves that this mixed local blocker pattern alone does **not** force a balanced pair. The remaining proof must therefore use the simultaneous global system, not a one-boundary argument.

## 7. Genuine source-valid counterexample to the naive arbitrary-chain Lipschitz extension

The fleet04/B20 theorem has `|Delta W|<=1` when the deleted chain has one element. That bound does **not** extend to arbitrary chain length.

Let

`C={c_1<...<c_m}`

and add two elements `u,v` such that `u` is incomparable with every element of `C` and with `v`, while every `c_j<v`. This poset has width two. Deleting `C` leaves the two-element antichain `Q={u,v}`.

Here

`I(u)=[0,m]`, `I(v)=[m,m]`.

For `tau=uv`, `t_v=m` and `t_u` may be any of `0,...,m`, so

`W_C(uv)=m+1`.

For `tau'=vu`, monotonicity forces `t_v=t_u=m`, so

`W_C(vu)=1`.

Therefore a **single adjacent incomparable swap** has

`|W_C(uv)-W_C(vu)|=m`,

and the neighboring-fiber ratio is `m+1`, unbounded even in width two.

This is not a counterexample to POS3. It is a source-valid counterexample to the tempting arbitrary-chain extension of the one-element local Lipschitz/factor-two rule. Any global proof that pays each adjacent swap by a universal constant is therefore impossible.

## 8. Verification

The companion standard-library verifier

`verify_pos3_chain_swap_defect.py`

checks the proved formulas independently. Executed with site initialization disabled to keep the run dependency-free, it reports:

- `34,683` exhaustive ordered/truncated interval cases through `m<=8`, verifying the sign and exact short-gap formula (4.1);
- `3,579` small source-poset fiber cases with `m,n<=3`, comparing the dual recurrence against direct enumeration of all full linear extensions;
- the width-two single-swap family for `m=1,...,8`, with defects exactly `1,...,8`.

Terminal line:

`POS3_CHAIN_SWAP_DEFECT_CHECK_PASS`.

These computations are regression checks only; the mathematical claims above are proved by explicit bijections/reflections.

## 9. First essential missing implication after this run

The arbitrary-chain local recurrence is no longer the missing object. The first unpaid implication is now the following global transfer problem.

> **Nested-profile defect charge.** In the connected, module-prime, width-three minimal-counterexample core, choose a chain `C` from a three-chain cover and `Q=P\C` of width at most two. Use a valid width-two pair-selection/exchange on `Q`. Prove that the exact short-gap defects (5.1), together with the context-sensitive defects from nested `C`-profiles, can be charged to pair events involving `C` strongly enough that either (i) some `Q`--`C` pair has probability in `[1/3,2/3]`, or (ii) the two corridor-weighted orientation masses for some incomparable pair in `Q` differ by at most a factor two.

The new theorems reduce this obligation sharply:

1. nonnested swaps already have a canonical exact injection and a known-sign short-gap defect;
2. only nested profiles can change sign with the surrounding chain-prefix state;
3. strict nesting creates the same predecessor/successor blocker geometry that the fresh fleet03/B11 theorem shows cannot be resolved one boundary at a time;
4. the unbounded single-swap family rules out any universal local Lipschitz payment.

Thus the next attack should combine nested-profile defects across the simultaneous heavy-slice/double-blocker system, rather than attempt another uniform-law or constant-distortion shortcut.

## 10. Claim status

- Dual chain-prefix fiber recurrence for arbitrary deleted chain: **PROVED**.
- Exact local midpoint/reflection comparison: **PROVED**.
- Exact short-gap formula for an endpoint-ordered adjacent swap: **PROVED**.
- Context-independent monotonicity for endpoint-ordered profiles: **PROVED**.
- Incomparable-profile overlap and nested-profile classification: **PROVED**.
- Strict nesting implies explicit chain blockers: **PROVED**.
- Arbitrary-chain extension `|Delta W|<=1`: **REFUTED** by a width-two family with one-swap defect `m`.
- Universal local factor-two neighboring-fiber bound: **REFUTED** by the same family.
- Nested-profile global defect charge: **OPEN**.
- Width-three `1/3–2/3` parent target: **OPEN / NOT PROVED**.

No novelty or priority claim is made. No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data, email, Drive, public posting, paid model/API/Codex execution, remote workflow, or permission change was used.
