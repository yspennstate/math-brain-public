# POS3 fleet02/B19 — canonical heavy-state reciprocity and an exact greedy ray-return 2-cycle

**Run:** `20260922T064049Z-fleet02-B19-pos3-06d9849e`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has incomparable `x,y` with `1/3 <= Pr(x<y) <= 2/3` under the uniform law on all full linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

Every probability and active weight below is computed from the original uniform law on all full linear extensions. No deletion- or projection-induced law is renamed uniform.

## 1. Fresh collective state actually consumed

Fresh owner control is revision `2026-09-22.2` under `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`; the owner stop on new brain-installation and benchmark work is respected.

The latest complete campaign-lead result consumed is:

- **fleet04/B10 r15**, science commit `0c95533fce3b4870b16ede500442a0209df3d9b6`, report `proofnet24/collective-POS3/fleet04/B10/20260922T061407Z-B10-POS3-r15/REPORT.md`, report blob `b0864fe6d45a6285e0226b3eec10a2272a8eeae1`.

It proves that, after strong-majority span descent is exhausted, the canonical active blockers of a heavy cover state lie on the two outer strong-order rays. In its low-endpoint branch an outer ray carries `>2E/11` marked defect incidence and a concrete outward Hasse channel carries `>2E/33`. Its first unpaid implication is **RAY-RETURN EXCLUSION**: the outward packet must not recycle through previously exposed strong-order territory forever without balance, span descent, width-four contradiction, autonomous/ordinal reduction, or a controlled structural exit.

The named partner actually consumed is:

- **fleet03/B10 r11**, `proofnet24/collective-POS3/fleet03/B10/b10-20260922t061504z-r11/REPORT.md`, report blob `85fb81cdcbd72f87bcfca53e30f060a83770a1f6`.

It proves that the exact-two recurrence reaches the first actual non-exact boundary with **zero probability defect**: `B=E+K-A_prev-3A` exactly. In a same-polarity no-balanced boundary the genuine structural overload is `K-B=A_prev+3A-E>0`. Thus extra distinguishers must convert already-existing charge structurally; they do not first appear as an additive correction to the boundary-pair probability.

I also consume the newest compatible canonical-blocker result:

- **fleet04/B19**, science commit `9bdccf1abda0b25bb605c57079ed0786dbe77148`, report `proofnet24/collective-POS3/fleet04/B19/B19-20260922T061559Z-r45/REPORT.md`, report blob `7e142965f79f76b8a3ffb05da2c82080fbae50d2`.

It compresses every heavy-state bad swap to at most three canonical Hasse channels per side and proves their outward strong-order polarity when balance/span descent is absent. It names the global residual **CANONICAL-FRINGE REUSE ACYCLICITY**.

The exact 11-element core used below was first certified in my earlier source-bound report at science commit `c4c7985fe13db68f080c2c0b0def2bbe29888a52`, report blob `1669d5b58e69dac26d16cd6a942a5b30eb4eb82a`. The present run changes mechanism: it does not repeat the earlier local two-witness overlap argument. It analyzes the *current canonical heavy-state transition graph* and derives a general reciprocity lemma plus a new positive-weight ray-return cycle.

## 2. Conditional end-to-end route and the exact missing implication

Assume POS3 is false and take a cardinality-minimal no-balanced width-three counterexample. The current collective route is:

1. reach a heavy cover state `S=(x lessdot y; a)` with `a||x,y`, `Pr(x<a)>2/3`, `Pr(y<a)<1/3`, hence `Pr(x<a<y)>1/3`;
2. compress all failed-swap mass to the bounded canonical Hasse frontier;
3. after span descent is exhausted, orient every positive canonical blocker onto an outer strong-order ray;
4. recycle the exact charge through the next heavy / exact-two / boundary state;
5. prove the recycled charge cannot return indefinitely without one of the allowed exits.

The first unpaid step is not merely “find an acyclic local state graph.” The lemma below shows that two of the canonical channel types have a **built-in reciprocal return edge**. Therefore any valid end-to-end proof must use quantitative weights and/or the global no-balanced hypothesis, not graph-theoretic direction alone.

## 3. General reciprocal cover-pivot lemma

Use the canonical notation from fleet04/B19 for a heavy state `S=(x lessdot y; a)`:

`T_L = Max{t : t<a and t||x}`,

`U_R = Min{u : a<u and u||y}`.

The Hasse-compression theorem gives `t lessdot a` for `t in T_L` and `a lessdot u` for `u in U_R`.

### Lemma 3.1 — left blockers generate a heavy state with a structural return channel

Suppose `t in T_L` and `Pr(t<x)>2/3`; in the lead's no-balance/no-span branch this is exactly the outward polarity `t prec_* x`. Then

`S_t := (t lessdot a; pivot x)`

is itself a heavy cover state:

`Pr(t<x)>2/3`,

`Pr(a<x)=1-Pr(x<a)<1/3`.

Moreover the original cover successor `y` belongs to `U_R(S_t)`. Indeed `x lessdot y` and `y||a`, so `y` is a minimal element of `{u:x<u, u||a}`. The Hasse edge associated with this canonical return channel is exactly `x lessdot y`, with pivot `a`, i.e. the original state `S`.

Thus a left `T_L` transition has a canonical two-edge structural return available.

### Lemma 3.2 — right blockers are dual

Suppose `u in U_R` and `Pr(y<u)>2/3`, the outward polarity in the lead's no-balance/no-span branch. Then

`S_u := (a lessdot u; pivot y)`

is heavy because

`Pr(a<y)=1-Pr(y<a)>2/3`,

`Pr(u<y)<1/3`.

The original cover predecessor `x` lies in `T_L(S_u)`, since `x lessdot y` and `x||a`. Its Hasse edge with the new pivot is the original cover `x lessdot y`. So the right transition has the same reciprocal return structure.

### Consequence

A proof of the lead's `RAY-RETURN EXCLUSION` cannot use “the canonical Hasse state graph is acyclic” as its potential: reciprocal return edges are forced by the defining cover geometry itself. What remains to prove is a **quantitative return-exclusion theorem**: a return edge must lose/redistribute enough exact active weight, expose a balanced secondary pair, create span descent, or trigger one of the other authorized structural exits.

This is compatible with the named partner's zero-defect boundary theorem: there is no missing additive correction available to break the return automatically. The obstruction is structural/weighted.

## 4. Exact autonomous-prime width-three witness

Let `P` have vertices `0,...,10` and transitive-reduction covers

`0<1, 0<5, 1<2, 1<6, 1<10, 2<3, 4<1, 4<5, 5<3, 5<6, 6<7, 8<9, 8<0, 9<5, 9<10, 10<3, 10<7`.

The chains

`(0<1<2<3)`, `(4<5<6<7)`, `(8<9<10)`

cover `P`, while `{0,4,9}` is a 3-antichain, so `width(P)=3`. Exact checking shows both comparability and incomparability graphs are connected and there is **no nontrivial proper autonomous subset**. Thus the core is connected and autonomous-prime.

There are exactly

`E=e(P)=515`

uniform linear extensions.

## 5. Heavy state S0 and its unique heaviest outward channel

Take

`S0=(x,y,a)=(5,6,10)`.

Here `5 lessdot 6`, `10||5,6`, and exact full-extension counts give

`Pr(5<10)=374/515 > 2/3`,

`Pr(6<10)=161/515 < 1/3`,

`Pr(5<10<6)=213/515 > 1/3`.

The exact canonical sets are

`T_L={1}`, `U_L={6}`, `U_R={3}`, `T_R={5}`,

so the active sets are

`C_L={1}`, `C_R={3}`.

Using the deterministic first-canonical-blocker assignment from fleet04/B19, the exact active weights are

`lambda_1=72`, `rho_3=52`.

Thus `t=1` is the **unique heaviest** canonical channel. It is genuinely outward:

`Pr(1<5)=387/515 > 2/3`.

There is no strong-majority vertex strictly inside either local interval `(5,10)` or `(10,6)`.

Because `1 lessdot 10`, recycling this heaviest left channel by Lemma 3.1 produces

`S1=(1,10; pivot 5)`.

## 6. Heavy state S1 and exact return to S0

For

`S1=(x,y,a)=(1,10,5)`, exact counts give

`Pr(1<5)=387/515 > 2/3`,

`Pr(10<5)=141/515 < 1/3`,

`Pr(1<5<10)=246/515 > 1/3`.

The exact canonical sets are

`T_L={9}`, `U_L={2,10}`, `U_R={6}`, `T_R={1}`,

hence

`C_L={2,9}`, `C_R={6}`.

The deterministic active weights are

`lambda_2=55`, `lambda_9=63`, `rho_6=105`.

Therefore `u=6` is the **unique heaviest** canonical channel. It points outward on the right:

`Pr(10<6)=354/515 > 2/3`, equivalently `Pr(6<10)=161/515 <1/3`.

Again there is no strong-majority vertex strictly inside either local interval `(1,5)` or `(5,10)`.

Since `5 lessdot 6`, Lemma 3.2 recycles this channel to

`(5,6; pivot 10)=S0`.

So the local heaviest-channel selector has the literal positive-weight two-cycle

`S0 --72--> S1 --105--> S0`.

The active weight even **increases** on the first return step, from `72` to `105`, so raw selected-channel weight is not a monotone potential either.

## 7. Why this does not refute POS3 or the lead theorem

The verifier checks **all 15 incomparable-pair probabilities**. Exactly five are balanced:

`(0,4):188/515`,

`(0,9):319/515`,

`(2,6):66/103`,

`(2,10):49/103`,

`(3,7):277/515`.

Thus `P` is a POS3-positive instance, not a counterexample.

The point is more precise. At both heavy states the **attached canonical channel probabilities** selected by the greedy rule are unbalanced, and the chosen channels are outward with no local strong-span interior. Nevertheless the cycle persists. At `S1`, the balanced pair `(2,10)=49/103` is a *secondary cross-pair* associated with the non-heaviest `U_L` blocker `2`; it is exactly the type of pair that the outward-polarity proof must inspect to orient the whole frontier in a genuine no-balanced candidate.

Therefore the full no-balanced hypothesis remains capable of killing this witness, but only if the proof uses the **entire canonical frontier and its secondary cross-pairs**, not a single heaviest packet path.

## 8. Ordinal-sum amplification and asymmetric sizes

For arbitrary `k>=1` and `s,t>=0`, define

`Q(k,s,t) = C_s op P op ... op P op C_t`

with `k` copies of `P` in ordinal sum. Then

- `width(Q)=3`;
- every incomparable pair lies inside one `P` block;
- every internal pair probability is exactly the corresponding probability above;
- `e(Q)=515^k`;
- a local active weight in one block is multiplied by the common factor `515^(k-1)`;
- each block therefore retains the same greedy canonical two-cycle.

The proof is immediate from the uniform law: every extension of an ordinal sum is the forced concatenation of one independently chosen extension from each factor, with the prefix/suffix chains forced. Hence neither arbitrarily large finite size nor asymmetric chain padding repairs the local greedy return. The padded examples are of course ordinal-decomposable, which is an authorized exit in the minimal-counterexample route; the 11-element core itself is autonomous-prime and indecomposable by the exact checks above.

## 9. Exact executable certificate

Authoritative verifier:

`verify_canonical_heavy_greedy_2cycle.py`

Executed/source SHA-256:

`13b1e77b3891327ee4aea1a077cde7e00d107e7d9067c3657ada6586f94d57a2`

Captured exact output:

`verify_canonical_heavy_greedy_2cycle.out`

Output SHA-256:

`03087188a963226b9e59363f38986dfd0741b8666b30dc2473c0e9371a4f9c3a`

Terminal marker:

`POS3_CANONICAL_HEAVY_GREEDY_2CYCLE_PASS`.

The executable independently reconstructs the transitive closure, enumerates all 515 full linear extensions with unit weight, certifies exact width three, the three-chain cover and 3-antichain, connected comparability/incomparability graphs, autonomous-primality, all 15 incomparable-pair probabilities, both canonical frontiers, deterministic active weights, absence of local strong-order interior vertices at both states, and the exact two transitions.

## 10. Accepted gate and next exact implication

**Accepted before -> after.** Before this run, the lead/current canonical-blocker route had narrowed the global residual to ray-return / canonical-fringe reuse acyclicity. After this run:

- a symbolic reciprocal cover-pivot lemma proves that canonical `T_L` and `U_R` transitions carry a structural return edge by construction;
- an exact connected autonomous-prime width-three instance realizes a **positive-weight, unique-heaviest-channel two-cycle** with no local strong-span interior;
- the return weight can increase, so neither graph distance nor raw selected weight is a valid local potential;
- the cycle is broken only by looking beyond the greedy channel to the full frontier, where a secondary balanced cross-pair exists.

The first essential missing implication is therefore sharpened to:

> **FRONTIER-COMPLETE QUANTITATIVE RETURN EXCLUSION.** In a cardinality-minimal no-balanced width-three candidate, track all canonical primary channel weights together with the secondary cross-pairs needed to certify their outward polarity. Prove that every reciprocal return either exposes a balanced secondary pair, forces strict majority-span descent / width four / autonomous-or-ordinal reduction, or transfers a strictly controlled conserved charge to a genuinely new frontier. A proof following only the largest canonical channel cannot work.

The named partner's exact zero-boundary-defect theorem means this must be a structural/charge argument rather than an additive correction to the next pair probability.

Parent POS3 remains **OPEN**. No novelty or priority claim is made.

## 11. Integrity

No biased induced distribution was treated as uniform and no finite census is claimed to close the arbitrary-size theorem. No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email, Drive, public posting, paid model/API/Codex use, remote workflow, permission change, or brain-installation action appears here.
