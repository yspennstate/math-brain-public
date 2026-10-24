# POS3 account03/B19 — exact five-label corridor-transfer recurrence

**Run:** `20260922T040111Z-b19-pos3-r11`  
**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Inherited finite frontier:** `n_bal=14` (unchanged).  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

No brain-installation or benchmark work was performed. Every probability statement below refers to the original uniform law on the full linear-extension set of the stated poset. Whenever vertices are deleted, the deletion skeleton is used only as an exact partition of the full extension set; its induced multiplicities are retained and it is never replaced by a uniform law.

## 1. Exact collective state consumed

The named partner result actually consumed is account04/B10,

`proofnet24/collective-POS3/account04/B10/20260922T034709Z-B10-POS3-r12/REPORT.md`,
source-bound coordination blob `35d96ce67d701ea97c2156db9edd58dd339873b7`.

Its crossed-neighborhood theorem says that for incomparable `x,y` with

`Pred(x) subseteq Pred(y)` and `Succ(y) subseteq Succ(x)`,

putting `D=Pred(y)\Pred(x)` and `U=Succ(x)\Succ(y)` gives, under the original full uniform law,

`2 Pr(x<y)-1 = Pr((exists d in D: x<d) OR (exists u in U: u<y))`.

In the inherited strict-chain/no-internal-descent branch, width three compresses this to at most one canonical lower fringe event and two upper fringe events, so a strong endpoint exports nonzero mass to an outward fringe pair. Its exact next obligation is to control **repeated** canonical fringe export globally rather than by another local pigeonhole argument.

A second named other-account result used essentially is account02/B10's crossed-corridor theorem, source-bound handoff blob `ae1e8c39613f3870a8984a36f8612bae0762bf12`. For an exact-two-distinguisher corridor, its deletion-skeleton word counts satisfy

`A=C`, `X<=A`, `Y<=A`, `Z<=min(X,Y)`, and `W=0` in the comparable-outer case,

without uniformizing the skeleton law. In particular the endpoint minority is the word count `A/E`.

The present run attacks the first missing repeated-export implication by keeping one more canonical lower export in the same exact deletion calculation.

## 2. Two consecutive exact-two crossed states

Consider five distinct elements `e,d,x,y,u` in a finite poset `P`. Assume the current canonical crossed state `(x,y)` has exactly the singleton neighborhood discrepancies

`Pred(y)=Pred(x) union {d}`,  
`Succ(x)=Succ(y) union {u}`,

and the next canonical lower-fringe state `(d,x)` is itself crossed with exactly

`Pred(x)=Pred(d) union {e}`,  
`Succ(d)=Succ(x) union {y}`.

Thus `x||y`, `d||x`, `e||d`, and the forced relations include

`e<x`, `e<y`, `d<y`, `d<u`, `x<u`.

The relation `d<u` is forced because `u in Succ(x)` and, at the next crossed state, `Succ(x) subseteq Succ(d)`.

Delete the five displayed vertices and fix **an arbitrary exact linear-extension skeleton** `tau` of the remaining poset. No probability distribution is placed on skeletons. Let `w_j(tau)` be the number of lifts of this fixed skeleton with one of the following eight relative orders of the five special labels:

`P1=e d x y u`,  
`P2=e d x u y`,  
`P3=e d y x u`,  
`P4=e x d y u`,  
`P5=e x d u y`,  
`P6=d e x y u`,  
`P7=d e x u y`,  
`P8=d e y x u`.

These are exactly the possible five-label words under the displayed relations.

### Theorem 2.1 — exact five-label transfer

For every fixed residual skeleton `tau`,

`w1=w3=w4`,  
`w2=w5`,  
`w6=w8`.

Consequently, after summing with the **actual lift multiplicities** over all residual skeletons, if the current account02/B10 six-word counts are

`(A,C,X,Y,Z,W)`

for the words

`A=d y x u`, `C=d x y u`, `X=d x u y`,  
`Y=x d y u`, `Z=x d u y`, `W=x u d y`,

and the next state's corresponding counts are `(A',C',X',Y',Z',W')`, then

`C=A`, `W=0`,

and the exact transfer is

`A' = Y+Z`,  
`X' = Y`,  
`Y' = A+X-Y-Z`,  
`Z' = A-Y`,  
`C'=A'`, `W'=0`.                                      (2.1)

In particular the integer

`K = A+Z`                                                   (2.2)

is conserved by every consecutive exact-two canonical lower-fringe continuation.

### Proof

For the fixed residual skeleton `tau`, the exact-two hypotheses imply that every residual vertex has the same relation to `x` as to `y`, and the same relation to `d` as to `x`. Hence `d,x,y` have the **same exact admissible gap interval** relative to `tau`.

In `P1` and `P3`, interchange the adjacent labels `x,y` while leaving their numerical gaps fixed. Their external admissible intervals are identical and the resulting five-label word still respects every displayed special relation. This is a bijection, so `w1=w3`.

Likewise interchanging adjacent `d,x` in `P1` and `P4` gives `w1=w4`; interchanging `d,x` in `P2` and `P5` gives `w2=w5`; and interchanging `x,y` in `P6` and `P8` gives `w6=w8`.

Now simply erase `e` from the eight five-label words to collect the current four-label classes:

`A=w3+w8`, `C=w1+w6`, `X=w2+w7`, `Y=w4`, `Z=w5`, `W=0`.

Erase `u` and use the next-state labels `(a',b',d',u')=(x,d,e,y)`:

`A'=w4+w5`, `X'=w3`, `Y'=w6+w7`, `Z'=w8`, `W'=0`.

Substituting the bijections gives (2.1). Finally,

`A'+Z'=(Y+Z)+(A-Y)=A+Z`,

which proves (2.2). Because every identity holds **before** summing over skeletons, arbitrary corridor multiplicities are retained exactly. `square`

## 3. Second-order minority-count recurrence

Let a run of consecutive exact-two lower-fringe continuations have common total extension count `E`, endpoint-minority word counts `A_i`, and conserved `K`.

From (2.1),

`A_(i+1)=Y_i+Z_i`, `Z_i=K-A_i`,

so

`Y_i=A_i+A_(i+1)-K`.

The previous transfer also gives

`X_i=Y_(i-1)=A_(i-1)+A_i-K`.

Since `W_i=0` and `C_i=A_i`,

`E = 2A_i + X_i + Y_i + Z_i`.

Therefore every interior exact-two corridor state satisfies the exact integer recurrence

`A_(i-1) + 3 A_i + A_(i+1) = E + K`.               (3.1)

Equivalently,

`A_(i+1)=E+K-3A_i-A_(i-1)`.

This is the first genuinely global constraint obtained for repeated canonical fringe export: once two consecutive endpoint minority counts and `K` are fixed, every further exact-two continuation is forced. There is no freedom to choose each local corridor independently.

The characteristic roots of the centered homogeneous recurrence are `(-3 +/- sqrt(5))/2`; this observation is **not** promoted to a termination theorem. The remaining proof must combine (3.1) with endpoint/boundary inequalities or with the branches where exact-two crossed continuation ceases.

## 4. Targeted exact adversary and regression

To test whether a simple bounded-step termination statement could replace the global recurrence, this run performed exact ideal-state enumeration of a targeted width-three poset on vertices `0,...,11` with transitive-reduction covers

`(0,1),(0,10),(1,2),(1,5),(2,3),(3,6),(3,11),(4,5),(4,11),(5,6),(6,7),(8,1),(8,9),(9,2),(9,10),(10,3),(10,5)`.

It has exactly `E=833` uniform linear extensions, width exactly three, and transitive strict-majority order

`8,0,9,4,1,10,2,5,3,6,11,7`.

There are **four consecutive** exact-two crossed/no-internal-descent canonical lower-fringe states:

| i | `(x,y)` | `(d,u)` | `N(x<y)` | `(A,C,X,Y,Z,W)` | `K=A+Z` |
|---|---|---|---:|---|---:|
| 0 | `(10,2)` | `(1,5)` | `568/833` | `(265,265,90,159,54,0)` | 319 |
| 1 | `(1,10)` | `(9,2)` | `620/833` | `(213,213,159,142,106,0)` | 319 |
| 2 | `(9,1)` | `(0,10)` | `585/833` | `(248,248,142,124,71,0)` | 319 |
| 3 | `(0,9)` | `(8,1)` | `638/833` | `(195,195,124,195,124,0)` | 319 |

The three observed transfers agree exactly with (2.1). The interior recurrence has

`E+K=833+319=1152`,

and indeed

`265+3*213+248=1152`,  
`213+3*248+195=1152`.

At the next left fringe pair, `(8,0)`, the reverse/minority count is exactly

`N(0<8)=319=K`,

so `(0,8)` is balanced. The exact balanced-pair list is

`(0,8):319/833`, `(1,4):377/833`, `(3,5):416/833`, `(4,9):352/833`, `(6,11):486/833`.

Thus this poset is **not** a POS3 counterexample. It does, however, rigorously refute any attempted lemma that repeated exact-two crossed canonical export must terminate after at most one, two, or three local steps. The fourth continuation is real, and the balanced escape occurs only afterward.

The deterministic verifier re-enumerates all 833 extensions, verifies width, all incomparable-pair counts needed above, the majority order, all four singleton discrepancy identities, all six-word counts, the three transfer equations, the invariant `K`, the second-order recurrence, and the balanced exit.

- verifier SHA-256: `e700b909fbef4cf4b34096aa44379ee172f1f57c5b13a3167f9b71b7f6407a1a`
- captured-output SHA-256: `c988f8e9b36e01a314402a33ed0aefd0aea6e6a9065aa384514ba2962e67bf34`
- terminator: `POS3_B19_CORRIDOR_TRANSFER_PASS`

## 5. What this pays, and the first remaining implication

The named partner's first missing global implication asked for a mechanism controlling **repeated** canonical fringe export. Theorem 2.1 and (3.1) pay a nontrivial part of that implication:

> an exact-two crossed lower-fringe chain is governed by one conserved integer `K` and a rigid second-order recurrence on its endpoint minority counts.

This is stronger than another one-step union or pigeonhole estimate and is immune to the biased-deletion-law trap because it is proved skeleton by skeleton before weighting.

It does **not** yet prove POS3. A minimal counterexample could leave this recurrence through a state with three or more distinguishers, through the non-crossed successor branch, or through another structural exit before a minority count reaches the balanced interval.

The next exact obligation for the lead is therefore:

> combine (3.1), the conserved `K`, and the first/last exact corridor boundary cells with the existing width-three block/cumulative-band constraints to prove that any maximal exact-two corridor chain either reaches `E/3 <= A_i <= 2E/3` (a balanced pair), creates a strict span descent, or exits into one of the separately controlled multi-distinguisher/non-crossed branches with a quantitative charge sufficient to finish that branch.

The 833-extension witness should be retained as a regression guard: any proposed fixed-step termination claim shorter than four continuations is false.

No target-level closure, novelty, priority, finite-frontier advance, or verified brain use is claimed.
