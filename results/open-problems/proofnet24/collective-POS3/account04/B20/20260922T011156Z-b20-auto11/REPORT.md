# POS3 account04/B20 — nested-fringe defect formula and majority-block corridor pinning

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair with ordering probability in `[1/3,2/3]` under the uniform law on all linear extensions.  
**Parent status after this report:** **OPEN / NOT PROVED**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact state consumed

This run follows `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. The later owner allocation supersedes the old brain-installation and benchmark duties; no new installation or benchmark work was performed.

The designated team lead `account04/B10` had no archived `proofnet24/collective-POS3/account04/B10/` report at the scientific read snapshot, so no lead result is fabricated. The required named OTHER-account input is the newest complete assigned-partner result:

- `account01/B19`, `proofnet24/collective-POS3/account01/B19/20260922T004631Z-b19-pos3-r11/REPORT.md`, Git blob `c2f771152d5be6943cce6872c500ca81c572e962`.

That report proves the exact arbitrary-deleted-chain lift recurrence. For a deleted chain `C={c_1<...<c_m}`, each `q in Q=P\C` has a feasible prefix-count interval

`I(q)=[lambda(q),rho(q)] subset {0,...,m}`,

and a lift of `tau=(q_1,...,q_n) in L(Q)` is exactly a nondecreasing sequence `t_1<=...<=t_n` with `t_i in I(q_i)`. For an adjacent incomparable swap `(...,u,v,...) <-> (...,v,u,...)`, conditioning on the outside prefix counts reduces the local comparison to two truncated integer intervals. The report proves a reflection/short-gap formula, shows every endpoint-ordered pair has context-independent sign, and identifies **nested profile pairs** as the only swaps whose sign can depend on the outside context. It also gives a genuine width-two family showing that the one-element `|Delta W|<=1` bound does not extend to arbitrary deleted-chain length.

I also retain these exact compatible collective inputs:

- `account01/B10`, blob `3a0d4e63665646adc853bb48192eba0f81629a15`: exact three-chain ideal-path/edge-flux encoding and, in a no-balanced counterexample, the cumulative strong-majority-gap inequalities `sum_{t<g}W(t)<E/3` and `sum_{t<=g}W(t)>2E/3`.
- `account03/B10`, blob `388ac28e375df4e7a49f72ffbf540f362e03696e`: every element of a hypothetical width-three counterexample has probability at least `1/19683` of occupying its exact strong-majority rank.
- `account04/B19`, blob `ce30dae79d698103f026d4d871033238489b1fb1`: a cardinality-minimal counterexample has no proper autonomous nonchain.
- `account02/B19`, blob `3b3dd10f434e411cb2387a156e3a891f19f624fb`: a 15-element connected module-prime POS3-positive witness shows that local heavy peaks plus pinned central atoms do not replace the full cumulative-band constraints.

Thus the current proof route must retain the exact weighted chain-corridor defects and the full cumulative strong-majority information.

## 2. Compact conditional end-to-end route

Assume a counterexample exists and choose one of minimum cardinality. The inherited collective reductions permit a width-exactly-three, incomparability-connected core with no proper autonomous nonchain and a transitive strong-majority linear extension `L_*`. Fix a three-chain cover and delete one chain `C`; the remaining poset `Q` has width at most two, but the induced law on `L(Q)` has density proportional to the exact lift multiplicity `W_C` rather than being uniform.

A width-two exchange/path proof would close the induction if its adjacent incomparable swaps could be charged under these exact weights. The partner report reduces every local swap to an explicit interval comparison and shows that only nested `C`-profiles can have context-dependent sign. The first unpaid universal step is therefore not a generic distortion bound. It is a charge for the nested-profile defect that preserves the strong-majority cumulative bands.

The two results below make that charge more rigid. First, a nested local defect has an exact two-boundary closed form rather than merely a sign/short-gap description. Second, an arbitrarily long strong-majority chain block has more than one third of all full extensions in a single canonical gap relative to either other chain, so a proof need not pay a separate `1/3` loss for every element of the block.

## 3. Exact two-fringe formula for a nested profile swap

Take one conditioned local swap from the account01/B19 recurrence. Suppose after common truncation by the outside prefix window `[L,U]` the two feasible intervals are

`A=[a,b]`, `B=[c,d]`,

with `B subseteq A`, so `a<=c<=d<=b`. Write

`ell = c-a`  and  `r = b-d`,

for the surviving lower and upper fringe lengths of the less constrained interval `A` around `B`. Let

`N_AB = #{(s,t) in A x B : s<=t}`,

`N_BA = #{(s,t) in A x B : t<=s}`.

### Theorem 3.1 — nested defect is exactly lower fringe minus upper fringe

For every such truncated nested pair,

`N_AB - N_BA = |B| (ell-r)`.                                      (3.1)

Hence the local swap sign is exactly the sign of the surviving lower-fringe/upper-fringe imbalance. In the original untruncated profile notation `I(v) subseteq I(u)`, the lower fringe depends only on the preceding prefix boundary `L`, while the upper fringe depends only on the following boundary `U` (subject to feasibility).

### Proof

For each fixed `t in B`, because `B subseteq A`,

`#{s in A:s<=t}=t-a+1`

and

`#{s in A:t<=s}=b-t+1`.

Subtracting and summing over the consecutive interval `B=[c,d]` gives

`N_AB-N_BA = sum_(t=c)^d (2t-a-b)`

`= |B|[(c+d)-(a+b)]`

`= |B|[(c-a)-(b-d)]`

`= |B|(ell-r)`.

This also recovers the partner report's midpoint sign rule because `(c+d)-(a+b)=ell-r`. `□`

### Corollary 3.2 — exact global signed boundary decomposition

Using the partner report's prefix/suffix weights `P(L),S(U)`, every nested-profile adjacent-swap defect is

`W_C(...,u,v,...)-W_C(...,v,u,...)`

`= sum_(L,U) P(L) S(U) |B_(L,U)| [ell(L)-r(U)]`,                  (3.2)

where only feasible outside states are included.

Thus context sensitivity is a difference of two genuine boundary-fringe contributions. There is no interior or hidden scalar distortion term. This is stronger bookkeeping than a universal Lipschitz estimate, which the partner report correctly refuted.

## 4. Majority-block corridor pinning

The second result uses only the inherited strong-majority order and the exact uniform extension law.

Let `C_a,C_b` be two chains in a fixed three-chain cover. Let

`X=(x_1<...<x_r) subset C_a`

be a contiguous `C_a` block in the strong-majority order `L_*`; no element of another chain occurs between `x_1` and `x_r` in `L_*`. Let

`g = #{y in C_b : y precedes X in L_*}`.

For a uniformly random full linear extension `L`, let

`J_b(x)=#{y in C_b:y precedes x in L}`.

### Theorem 4.1 — whole-block canonical-gap mass exceeds one third

If `P` has no balanced incomparable pair, then

`Pr( J_b(x_i)=g for every i=1,...,r ) > 1/3`.                    (4.1)

This lower bound is independent of the block length.

### Proof

Because the `x_i` form a chain,

`J_b(x_1)<=...<=J_b(x_r)`

in every linear extension. Therefore failure of the event in (4.1) is exactly the union of

`A={J_b(x_1)<g}` and `B={J_b(x_r)>g}`.                           (4.2)

If `g=0`, event `A` is empty. If `g>0`, let `y^-` be the `g`-th element of `C_b`, the last `C_b` element before the block in `L_*`. Then

`A = {x_1 precedes y^-}`.

Since `L_*` is a linear extension, either `y^-<x_1` in the poset, in which case `A` is impossible, or `y^-||x_1`. In the latter case the no-balanced-pair assumption and the strong-majority orientation `y^-` before `x_1` give `Pr(A)<1/3`.

Similarly, if `g=|C_b|`, event `B` is empty. Otherwise let `y^+` be the `(g+1)`-st element of `C_b`, the first `C_b` element after the block in `L_*`. Then

`B = {y^+ precedes x_r}`.

Either `x_r<y^+` in the poset and `B` is impossible, or the pair is incomparable and the strong-majority orientation `x_r` before `y^+` gives `Pr(B)<1/3`.

Using (4.2),

`Pr(all J_b(x_i)=g) = 1-Pr(A union B)`

`>= 1-Pr(A)-Pr(B) > 1/3`.

`□`

### Corollary 4.2 — block-heavy corridor in the exact three-chain path system

In the account01/B10 three-chain path encoding, for every maximal same-chain block of `L_*` and either other chain separately, more than `E/3` complete paths keep the other-chain coordinate fixed at its canonical strong-majority value throughout all additions from that block.

This strictly strengthens the one-element heavy-slice statement for blocks of length greater than one: the intersection of all their canonical-gap events still has mass greater than `E/3`; the lower bound does not decay with the number of block elements.

## 5. Application to the partner's nested-profile obligation

The partner result says nested profiles are the only adjacent swaps for which the sign can depend on outside chain-prefix state. Equation (3.2) now identifies that dependence exactly as a **lower-boundary charge minus an upper-boundary charge**. Theorem 4.1 simultaneously shows that, along each strong-majority same-chain block, more than one third of the complete extension mass stays in one canonical gap with respect to the deleted/other chain.

Consequently an end-to-end proof no longer needs to control an arbitrary product of local distortion factors along a long block. Its remaining obligation can be localized to block boundaries:

> **Two-fringe block charge.** In the connected, nonchain-module-free width-three minimal-counterexample core, sum (3.2) over the adjacent cross-chain swaps required by a width-two exchange/path. Use the cumulative strong-majority band inequalities and the `>E/3` whole-block canonical-corridor masses to prove that the total lower-fringe charge cannot exceed the total upper-fringe charge in every strong-majority direction (and vice versa in the reverse direction), unless some pair involving the deleted chain already lies in `[1/3,2/3]`.

This is still unpaid. The new point is that the context-sensitive term has only two boundary components and arbitrarily long majority blocks can be treated by two endpoint minority events rather than one loss per element.

The account02/B19 witness warns against weakening this to local peak sizes or a single pinned atom: it satisfies those weaker local constraints while remaining POS3-positive and violates many full cumulative bands. Any next charge must therefore use the full cumulative inequalities from account01/B10.

## 6. Exact regression checks

`verify_nested_fringe_block_pinning.py` performs two independent standard-library checks.

1. It exhausts `27,027` nested integer-interval/common-window cases for chain length through eight and verifies exactly
   `N_AB-N_BA=|B|(ell-r)`.
2. It enumerates all `6,294` linear extensions of the published 15-element account02/B19 witness and checks the block event identity
   `pinned = not(left_boundary_crossing or right_boundary_crossing)`
   for all `26` maximal-block/other-chain cases, together with the exact complement count and union bound. The smallest observed pinned mass in that witness is `2366/6294=1183/3147`.

The witness has balanced pairs, so the observed `>1/3` values are regression data only; they are not used to prove Theorem 4.1. The theorem is the analytic endpoint argument above.

Executed terminal output:

`nested_interval_window_cases 27027`

`nested_closed_form PASS`

`extensions 6294`

`block_other_chain_cases 26`

`all_complement_identities PASS`

`all_union_bounds PASS`

`minimum_observed_pinned (11,) other_chain 0 gap 2 count 2366 fraction 1183/3147`

`corresponding_bad_counts 1756 2172 3928`

`POS3_NESTED_FRINGE_AND_BLOCK_PINNING_REGRESSION_PASS`

## 7. Status and next recipient

- Exact nested two-fringe defect formula (3.1): **PROVED**.
- Global weighted decomposition (3.2): **PROVED** by conditioning and summation.
- Whole-majority-block canonical-gap lower bound (4.1): **PROVED**, conditional only on the standard no-balanced-counterexample strong-majority order already established in the inherited POS3 state.
- Full POS3 target: **OPEN / NOT PROVED**.
- Run classification: `ESSENTIAL_STEP_APPLIED`.

The next recipient should combine the two-fringe decomposition with account01/B10's full cumulative band inequalities across consecutive strong-majority blocks. The decisive next question is simultaneous two-boundary conservation across the two other chains, not another per-element heavy-slice estimate or a constant-distortion bound.

No novelty/priority claim is made. No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data, email, Drive, paid/remote model execution, workflow dispatch, public release, production-state mutation, or broad mixed-domain memory was used.
