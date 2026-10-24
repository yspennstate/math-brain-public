# POS3 account03/B19 — latent balanced corridor mass and an asymptotically sharp family

**Run:** `20260922T045925Z-b19-pos3-r12`  
**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Inherited finite frontier:** `n_bal=14` (unchanged).  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

No brain-installation or benchmark work was performed. Every probability statement below refers to the original **uniform law on all linear extensions of the full poset**. Deletion skeletons are used only as exact partitions of that full extension set, with their actual lift multiplicities retained; no induced deletion law is replaced by a uniform law.

## 1. Exact collective state consumed

The named partner result actually consumed is account04/B10:

- coordination blob `35d96ce67d701ea97c2156db9edd58dd339873b7`;
- source report `proofnet24/collective-POS3/account04/B10/20260922T034709Z-B10-POS3-r12/REPORT.md`, blob `4759a4ecb5f2963a3d190f66fc6728459bb1a46e`.

Its crossed-neighborhood theorem proves that if `x||y`, `Pred(x) subseteq Pred(y)` and `Succ(y) subseteq Succ(x)`, then with `D=Pred(y)\Pred(x)` and `U=Succ(x)\Succ(y)`,

`2 Pr(x<y)-1 = Pr((exists d in D: x<d) OR (exists u in U: u<y))`.

In the inherited width-three strict-chain/no-internal-descent branch this exports more than `1/9` of the full extension mass through a canonical fringe pair (more than `1/6` when the upper discrepancy is singleton). Its first unpaid implication is global: repeated fringe export must terminate in balance/span descent or be charged through a non-crossed/multi-distinguisher exit.

A named other-account result used essentially is account02/B10's exact crossed-corridor calculation, source-bound coordination handoff blob `ae1e8c39613f3870a8984a36f8612bae0762bf12`. For a singleton lower/upper discrepancy with comparable outer distinguishers, its six four-label word counts

`A=d y x u`, `C=d x y u`, `X=d x u y`, `Y=x d y u`, `Z=x d u y`, `W=x u d y`

obey `A=C`, `X<=A`, `Y<=A`, `Z<=min(X,Y)`, `W=0`, skeleton by skeleton before summation. The endpoint minority count is `A`.

The immediately preceding B19 run proved the exact five-label transfer for **two consecutive** exact-two crossed states. In the notation below it obtained a conserved integer `K=A+Z` and the recurrence

`A_(i-1)+3A_i+A_(i+1)=E+K`.

This run attacks the missing global implication by asking what quantitative range `K` itself is forced to occupy and whether a stronger fixed-margin bound on `K` could close the corridor.

## 2. Setup: two consecutive exact-two crossed states

Let `e,d,x,y,u` be distinct elements of a finite poset `P` and assume

`Pred(y)=Pred(x) union {d}`,  
`Succ(x)=Succ(y) union {u}`,                              (2.1)

and the next canonical lower-fringe state satisfies

`Pred(x)=Pred(d) union {e}`,  
`Succ(d)=Succ(x) union {y}`.                              (2.2)

Then `x||y`, `d||x`, `e||d`, `y||u`, and `d<u`.

Delete the five displayed elements and fix an arbitrary exact residual linear-extension skeleton `tau`. Let `w_j(tau)` be the lift count for the eight possible five-label words

`P1=e d x y u`,  
`P2=e d x u y`,  
`P3=e d y x u`,  
`P4=e x d y u`,  
`P5=e x d u y`,  
`P6=d e x y u`,  
`P7=d e x u y`,  
`P8=d e y x u`.

The previous exact transfer established, for every fixed `tau`,

`w1=w3=w4`, `w2=w5`, `w6=w8`.                            (2.3)

No probability distribution on skeletons is used.

## 3. New swap injections and the latent-mass theorem

### Lemma 3.1 — the previously uncontrolled seventh word is dominated twice

For every fixed residual skeleton,

`w7 <= w2` and `w7 <= w6`.                                 (3.1)

Also

`w2 <= w1`.                                                  (3.2)

### Proof

Take a lift of `P7=d e x u y`.

First exchange the positions of `d` and `e`, leaving every other label fixed. This produces the special-label order `P2=e d x u y`. The exchange cannot cross a predecessor of `e`: if a crossed residual element `z` satisfied `z<e`, then `z<e<x`, hence `z in Pred(x)\{e}=Pred(d)`, contradicting that `z` lay after `d` in the original extension. It cannot cross a successor of `d`: if crossed `z` satisfied `d<z`, then `z` is not the special element `y`, so (2.2) gives `x<z`, contradicting that `z` lay before `e<x`. Thus the exchange preserves every order relation and is injective. Hence `w7<=w2`.

Second exchange the positions of `u` and `y` in the same `P7` lift, producing `P6=d e x y u`. A crossed predecessor `z<y` other than the already-earlier special `d` lies in `Pred(x)` by (2.1), contradicting that it lay after `u>x`. A crossed successor `u<z` is a successor of `x`; since `z!=u`, (2.1) makes it a successor of `y`, contradicting that it lay before `y`. This is again an injective order-preserving exchange, so `w7<=w6`.

Finally the identical `u,y` exchange sends every `P2=e d x u y` lift injectively to `P1=e d x y u`, proving `w2<=w1`. `square`

Because all three maps are defined for each fixed skeleton before any summation, arbitrary deletion-fiber multiplicities are retained exactly.

### Theorem 3.2 — conserved `K` is already a balanced-sized latent mass

Sum the fixed-skeleton counts over all residual skeletons with their actual lift multiplicities and put

`a=w1=w3=w4`, `b=w2=w5`, `c=w6=w8`, `t=w7`.

Then

`E = 3a+2b+2c+t`,                                            (3.3)

and for the current exact-two state

`A=a+c`, `Z=b`, `K=A+Z=a+b+c`.                               (3.4)

The new injections give `t<=min(b,c)` and `b<=a`. Therefore

`3K-E = b+c-t > 0`.                                         (3.5)

In particular

`K > E/3`.                                                    (3.6)

If the current exact-two endpoint belongs to a hypothetical POS3 counterexample and is oriented so that `A` is its minority count, then `A<E/3`. By `b<=a<=A`,

`K=A+b <= 2A < 2E/3`.                                       (3.7)

Hence every pair of consecutive exact-two crossed states in the no-balanced branch carries a conserved integer satisfying

`E/3 < K < 2E/3`.                                            (3.8)

That is, the corridor already carries a **balanced-sized exact mass**, even though `K` is not yet known to be the ordering count of an actual incomparable pair.

To justify the strict sign in (3.5), note that `d||e`; hence some full linear extension has `d<e` and therefore contributes to one of `P6,P7,P8`. Since `w6=w8=c` and `t<=c`, this forces `c>0` after summation. Thus `b+c-t>=c>0` if `t<=b`, or directly `b+c-t>=max(b,c)>0`.

### Why this is the useful global reduction

The previous second-order recurrence showed that a long exact-two corridor cannot choose its local minority counts independently. Theorem 3.2 now identifies the invariant it transports: in a hypothetical counterexample, `K` itself is already numerically in the target `[E/3,2E/3]` window. The missing proof obligation is therefore not to manufacture a fixed positive margin. It is to **realize or dominate this latent `K` by an actual incomparable-pair ordering event at a maximal corridor boundary**, or to show that any exit into the multi-distinguisher/non-crossed branch carries an equivalent `K`-sized charge.

## 4. Targeted exact family: no fixed margin above `1/3` is available

A stronger shortcut would be to hope for a universal margin such as `K>=3E/8`. Exact counting disproves that, and an explicit width-three family shows that the lower bound `K>E/3` is asymptotically sharp.

For every integer `m>=0`, define `P_m` on core vertices `e,d,x,y,u` and, when `m>=1`, a residual chain

`r_1 < r_2 < ... < r_m`

by taking the transitive closure of

`e<x`, `e<y`, `d<y`, `d<u`, `x<u`,                           (4.1)

and

`e<r_1<...<r_m<u`.                                           (4.2)

There are no additional generating relations. For `m>=1`, `P_m` has width exactly three: `{d,x,r_1}` is a three-antichain, while the residual vertices form a chain and the core has width two relative to any one residual element.

The states `(x,y)` and `(d,x)` satisfy exactly (2.1) and (2.2), so they are two consecutive exact-two crossed states.

Put

`p=C(m+3,3)`, `q=C(m+2,2)`, `r=m+1`.

Direct gap counting gives the six current-state word counts

`(A,C,X,Y,Z,W) = (p+q, p+q, q+r, p, q, 0)`.                 (4.3)

For completeness, these counts follow by interleaving the fixed three- or two-label word with the chain `e<r_1<...<r_m` before `u`:

- for `A=d y x u` and `C=d x y u`, the count is `C(m+4,3)-(m+2)=p+q`;
- for `X=d x u y`, it is `C(m+3,2)-1=q+r`;
- for `Y=x d y u`, `e` must occur before `x`, leaving `C(m+3,3)=p` choices;
- for `Z=x d u y`, the analogous count is `C(m+2,2)=q`;
- `W=0` because `d<u` is forced.

Consequently

`E_m = 3p+4q+r`,                                              (4.4)

`K_m = p+2q`,                                                 (4.5)

and the exact excess over the threshold is

`3K_m-E_m = (m+1)^2`.                                        (4.6)

Thus

`K_m/E_m = 1/3 + (m+1)^2/(3E_m) -> 1/3` from above.          (4.7)

So **no universal positive constant gap above `1/3` can be extracted from the conserved `K` alone**.

## 5. Exact ideal-state certificate at `m=8`

The run's deterministic ideal-state verifier reconstructs `P_m` and checks (4.3)-(4.4) for every `m=0,...,8`. At the targeted first simple violation of the tempting `3/8` strengthening, `m=8` has

`E=684`, width exactly `3`,

`(A,C,X,Y,Z,W)=(210,210,54,165,45,0)`,

and

`K=255`, `3K-E=81`, while `8K=2040 < 2052=3E`.              (5.1)

Hence

`K/E = 255/684 = 85/228 < 3/8`,                              (5.2)

while still `K/E>1/3` as Theorem 3.2 requires.

Both exact-two corridor endpoint minority counts are `210/684=35/114<1/3`; thus the two local endpoint pairs themselves remain outside the balanced interval. The same poset nevertheless has balanced pairs elsewhere; for example `(d,r_2)` has ordering count `306/684`. Therefore this family is **not** a POS3 counterexample. It is a counterexample only to the stronger fixed-margin strategy.

The verifier uses exact ideal-state dynamic programming for linear-extension counts, verifies the structural discrepancy identities and width, recomputes all required word counts and balanced-pair counts, and checks the closed formulas.

- verifier Git blob: `589a3feec44a995a338f6caee34f15d0ff089949`
- verifier SHA-256: `5acd36351aca6edc335e52953ead03ced2b36e557ac2774e0082c659e1d9ec36`
- captured-output Git blob: `5a6410fe488acd7e7f76bfb149a8ffb1a2fad70b`
- captured-output SHA-256: `24f4e3e243e26833feae2427d6dd2ac0acbc43d5c846a1da2ab8658eb88f49a6`
- terminator: `POS3_B19_LATENT_K_SHARPNESS_PASS`

## 6. First remaining global implication

The exact-two corridor branch is now reduced further. In a hypothetical minimal width-three counterexample:

1. every consecutive exact-two corridor segment carries a conserved `K` with `E/3<K<2E/3`;
2. `K` can approach `E/3` arbitrarily closely even in explicit width-three examples, so a fixed-slack argument is unavailable;
3. local endpoint minorities can remain below `E/3` while this latent `K` persists.

The first missing implication is therefore:

> **LATENT-K BOUNDARY REALIZATION.** For a maximal exact-two crossed canonical-fringe corridor in the inherited minimal-counterexample structure, prove that at one endpoint either (i) an incomparable pair has ordering count in `[K,2E/3)` or complementary count in the same balanced range, (ii) the corridor exits by strict strong-majority span descent, or (iii) the multi-distinguisher/non-crossed exit receives an exact disjoint charge of total at least `K` that can be converted, using the width-three channel budget/cumulative-band constraints, into a balanced pair.

The family `P_m` is a regression guard for this step: any proof that instead assumes `K` has a fixed margin above `E/3` is false. The account04/B10 non-crossed-successor branch remains separately unpaid and must not be silently folded into the exact-two theorem.

## 7. Status and scope

- New per-skeleton swap injections `w7<=w2`, `w7<=w6`, `w2<=w1`: **PROVED**.
- Latent balanced-mass theorem `E/3<K<2E/3` in a no-balanced consecutive exact-two branch: **PROVED**.
- Explicit width-three family with `K/E -> 1/3` from above: **PROVED by direct counting formulas**, with exact ideal-state verification through `m=8`.
- Stronger shortcut `K>=3E/8`: **REFUTED** by the exact `m=8` certificate.
- POS3: **OPEN / NOT PROVED**.
- Finite frontier: `n_bal=14`, unchanged.

Scoped provenance/privacy review: the committed files contain only mathematical statements, deterministic verifier code/output, repository-relative source references and nonsecret logical run labels. No credentials, scheduler identifiers, machine paths, private transcripts, email/Drive content, paid model/API calls, remote workflows, public posting or permission changes were used.
