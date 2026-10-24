# POS3 account04/B11 — bounded variance does not bound the exact-two / two-witness corridor

**Run:** `20260922T051337Z-B11-pos3-r15`  
**Outcome:** `CANDIDATE_REFUTED`  
**Parent target:** every finite nonchain poset of width at most three has incomparable `x,y` with `1/3 <= Pr(x<y) <= 2/3` under the uniform law on all linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

The candidate refuted here is **not POS3**. It is a tempting local termination step for the exceptional high-comparability / bounded-variance residue: that width three, bounded incomparability range, uniformly bounded rank variance, and the assigned partner's compulsory two external witnesses should force a lead-type repeated exact-two corridor to terminate after a bounded number of steps. The family below has `pi=7`, rank variance at most `49/4`, and arbitrarily many consecutive locally unbalanced exact-two states; moreover every corresponding heavy cover flip attains the partner's two-witness lower bound with equality. The family escapes only at its far boundary, where an actual balanced pair appears.

Thus bounded variance and bounded local witness arity do **not** provide the missing global charging theorem. A valid proof of POS3 must use the global no-balanced hypothesis at the maximal corridor boundary (or an equivalent exact flux / latent-mass invariant), not local compactness.

## 1. Exact collective state consumed

Only the essential completed state was read.

1. **Team lead account04/B10, latest complete version.**  
   `proofnet24/collective-POS3/account04/B10/20260922T041420Z-B10-POS3-r13/REPORT.md`, blob `6acb56ae36d1cf3c59af1b9d22cc1b0cb2f70f44`. After internal strong-majority span descent is exhausted in the strict delayed-predecessor corridor, it produces a canonical incomparable pair whose minority probability lies in `(1/6,1/3)`; in the small-minority branch it produces two canonical Hasse blockers. Its unpaid step is global `1/6 -> 1/3` amplification/charging.

2. **Assigned partner account01/B19, newest complete version used directly.**  
   `proofnet24/collective-POS3/account01/B19/20260922T044807Z-pos3-r11-b19/REPORT.md`, blob `003d2bf0593cb55f11738f50d68509413bb8d234`. It gives the exact three-chain `F*G` flux formulas and proves the **cover two-witness theorem**: if `x lessdot y` and `b||x,y`, then a strong flip `Pr(x<b)>2/3`, `Pr(y<b)<1/3` in a no-balanced poset forces at least two distinct external relation distinguishers beyond `x,y`. Its stated first unpaid implication is to prevent indefinite reuse of those two witness channels along the lead corridor.

3. **Previous account04/B11 bounded-variance localization.**  
   `proofnet24/collective-POS3/account04/B11/20260922T041135Z-B11-pos3-r14/REPORT.md`. It proves, in a hypothetical counterexample, that any canonical pair with minority `>1/6` has strong-majority index distance at most `3570`, and that the assigned partner's first-element tilt has a `<1/81` deep contribution beyond `kappa=37`. These are localization statements, not a bound on total corridor length.

4. **Earlier account04/B11 `pi=7` family.**  
   `proofnet24/collective-POS3/account04/B11/B11-20260922T011236Z-pos3-r12/REPORT.md`, commit `81bb20f56ed6517b28ec635950a2a8c4de57898e`. It constructs the interval-order family reused below and proves width three, connected and prime incomparability graph, `pi=7`, rank variance at most `49/4`, and at most eight legal one-element insertion gaps. That run only refuted a finite-kernel shortcut; the present run derives the exact full linear-extension law and exposes an arbitrarily long lead/partner-type probability corridor inside the same family.

## 2. Conditional end-to-end route and the candidate tested

Assume for contradiction that POS3 has a cardinality-minimal width-three counterexample. The lead reduces a hard branch to repeated strict crossed states carrying minority mass above `1/6`. The assigned partner converts a strong cover flip into at least two external witness channels. The preceding B11 work adds bounded rank variance / bounded strong-majority radius.

A tempting next implication would be:

> **False local termination candidate.** There is a universal `L` such that width three plus bounded `pi`, bounded rank variance, lead-type exact-two local minorities, and the partner's two-witness cover condition force a balanced pair / span descent / structural exit within `L` consecutive corridor steps.

If true, this would nearly turn the exceptional high-comparability residue into a bounded local argument. Sections 3--7 give an arbitrary-size source-valid counterexample to this implication. Importantly, the examples are **not** POS3 counterexamples: the far boundary is balanced. Therefore the only conclusion is that the *global no-balanced boundary condition* is essential.

## 3. The `pi=7` interval family

For `N>=8`, let

`I_i=[i,i+5/4]`, `i=0,...,N-1`,

and

`J=[5/4,27/4]`.

Let `R_N` be the interval order with path elements `v_i` represented by `I_i` and hub `h` represented by `J`, ordered by strict interval separation.

Then

- `v_i || v_{i+1}`;
- `v_i < v_j` whenever `j>=i+2`;
- `h || v_0,...,v_6`;
- `h < v_i` for every `i>=7`.

Hence the incomparability graph is the path on `v_0,...,v_{N-1}` plus a hub adjacent exactly to `v_0,...,v_6`. The earlier B11 report proves `width(R_N)=3`, `pi(R_N)=7`, connectedness, module-primality, and no proper nontrivial autonomous subset.

For any element `z`,

`rank(z)=|Pred(z)|+1+#{w||z : w precedes z}`.

Thus its rank support has diameter at most `pi(z)<=7`, and Popoviciu gives

`Var(rank(z)) <= 49/4`.                                      (3.1)

This bound is uniform in `N`.

## 4. Exact weighted-matching model for all linear extensions

Ignore `h` momentarily. Because `v_i<v_j` for `j>=i+2`, a linear extension of the path vertices is obtained uniquely from

`v_0,v_1,...,v_{N-1}`

by reversing a matching of disjoint adjacent pairs. Thus path extensions are in bijection with matchings of the path edges `(i,i+1)`.

For a fixed path matching, `h` must be inserted before the first path element with index at least seven. There are exactly

- `7` legal insertion gaps if the matching contains edge `(6,7)`;
- `8` legal insertion gaps otherwise.

There are `F_{N+1}` path matchings in total and exactly

`F_7 F_{N-7}=13 F_{N-7}`

of them contain `(6,7)`. Therefore, with `F_0=0,F_1=1`, the exact number of full linear extensions is

`E_N = e(R_N) = 8 F_{N+1} - 13 F_{N-7}`.                    (4.1)

Put `E_7=168`, `E_8=259`. Equation (4.1), or the Fibonacci recurrence directly, gives

`E_{n+1}=E_n+E_{n-1}` for `n>=8`.                            (4.2)

Consequently

`s_n:=E_{n+1}/E_n`

satisfies `s_{n+1}=1+1/s_n`. Since

`3/2 < 259/168 < 2`,

induction gives

`3/2 < s_n < 2` for every `n>=7`.                            (4.3)

## 5. Arbitrarily many exact-two crossed states with fixed nontrivial minority

For every

`7 <= i <= N-3`,

one has the exact neighborhood equalities

`Pred(v_{i+1}) = Pred(v_i) union {v_{i-1}}`,                  (5.1)

`Succ(v_i) = Succ(v_{i+1}) union {v_{i+2}}`.                 (5.2)

Thus `(v_i,v_{i+1})` is precisely an **exact-two crossed comparable-fringe state**, with lower witness `v_{i-1}` and upper witness `v_{i+2}`. There are `N-9` consecutive such states.

Let

`q_i = Pr(v_{i+1}<v_i)`.                                      (5.3)

For `i>=7`, a path matching containing edge `(i,i+1)` splits into an independent right path matching and a left copy of the weighted family. Hence its exact weighted numerator is

`Q_{N,i}=E_i F_{N-i-1}`.                                     (5.4)

Set `j=N-i-1`. The recurrence (4.2) gives the Fibonacci addition identity

`E_N = F_{j+1} E_{i+1} + F_j E_i`.                           (5.5)

For every exact-two state, `j>=2`, and therefore

`q_i`
` = E_i F_j / E_N`
` = 1 / [1 + (F_{j+1}/F_j)(E_{i+1}/E_i)]`.                  (5.6)

For `j>=2`,

`3/2 <= F_{j+1}/F_j <= 2`,

while (4.3) gives

`3/2 < E_{i+1}/E_i < 2`.

Therefore

`9/4 < (F_{j+1}/F_j)(E_{i+1}/E_i) < 4`,

and hence every one of the `N-9` consecutive states satisfies

`1/5 < q_i < 4/13 < 1/3`.                                    (5.7)

So the exact local minority is not merely positive: it stays in a fixed interval strictly inside the lead's `(1/6,1/3)` terminal window for an **arbitrarily long** corridor, while `pi=7` and every rank variance is at most `49/4`.

This already refutes a bounded-length conclusion from local difficulty/variance alone.

## 6. Direct application of the assigned partner: the two-witness lower bound is sharp at every step

Now fix

`7 <= i <= N-4`,

and set

`x=v_i`, `b=v_{i+1}`, `y=v_{i+2}`.

Because no element lies strictly between `v_i` and `v_{i+2}`, one has the cover

`x lessdot y`,

while `b||x,y`. Using (5.7),

`Pr(x<b)=1-q_i > 9/13 > 2/3`,                                (6.1)

`Pr(y<b)=q_{i+1} < 4/13 < 1/3`.                              (6.2)

The adjacent inversion events at edges `i` and `i+1` are mutually exclusive, because the path inversion set is a matching. Therefore the partner's literal cover-crossing flux is

`Pr(x<b<y)=1-q_i-q_{i+1} > 1-8/13 = 5/13 > 1/3`.             (6.3)

Thus every such index realizes exactly the assigned partner's **heavy cover flip** geometry.

Even more, its external witness bound is attained with equality. Let `D(r,s)` denote the partner's set of vertices whose three-valued relation to `r` differs from their relation to `s`. Directly from the path relations,

`D(x,b) = {v_{i-1}, y}`,                                     (6.4)

`D(y,b) = {x, v_{i+3}}`.                                     (6.5)

Hence

`(D(x,b)\{y}) union (D(y,b)\{x}) = {v_{i-1},v_{i+3}}`,       (6.6)

of cardinality exactly two.

So for `N-10` consecutive heavy cover flips, the account01/B19 cover two-witness theorem is **sharp at every step**: there are exactly two external channels, not merely at least two. Since `N` is arbitrary, width three + `pi=7` + uniformly bounded rank variance + exact two-witness heavy flux do not bound the length of repeated witness reuse.

This is the requested direct use of the assigned partner result: the family calibrates its exact lower bound and shows that the missing charging lemma cannot be replaced by a local arity/radius argument.

## 7. The escape is global and occurs at the maximal boundary

The last adjacent pair is different. For `i=N-2`, the upper witness is absent and (5.4) gives

`q_{N-2}=E_{N-2}/E_N`
`       =1/(1+E_{N-1}/E_{N-2})`.                              (7.1)

Using (4.3),

`1/3 < q_{N-2} < 2/5`.                                       (7.2)

Thus the far boundary pair `(v_{N-2},v_{N-1})` is **balanced**.

This is exactly why `R_N` does not refute POS3, and it isolates the missing implication cleanly. An arbitrarily long interior can satisfy all the local lead/partner geometry and bounded-variance/high-comparability constraints. What destroys the would-be counterexample is a **global maximal-boundary event**, not a bounded number of local steps.

In a genuine no-balanced minimal counterexample the corridor cannot terminate in this one-distinguisher boundary fashion. It must instead leave the exact-two class through a multi-distinguisher/non-crossed exit, a strict strong-majority span descent, or another globally controlled boundary. The proof still owed to the campaign is to show that one of those exits realizes or transports enough exact flux to force balance.

This dovetails with the other completed exact-corridor result in the collective archive: consecutive exact-two states carry a conserved latent mass `K` and a second-order endpoint-count recurrence. The present family shows why the **boundary realization of that global mass**, not a local finite-depth argument, is the right next target.

## 8. Deterministic verification

`verify_pi7_corridor.py` independently performs exact ideal-state linear-extension counting for `N=8,...,14`, checks the closed formula (4.1), and checks every adjacent-inversion numerator (5.4). It then checks the inequalities (5.7), (6.1)--(6.3), and (7.2) for all relevant indices through `N=200`, and verifies the exact two-witness sets on a representative `N=30` family member.

Verifier blob: `455bb107b380d7c94c3fc40660f2cb0ddc506119`.  
Captured-output blob: `f59c9133c68ec0dd94f0e406216174dd1a05b41a`.

Exact captured output:

```text
POS3_PI7_CORRIDOR_CHECK_PASS
small_exact_totals [(8, 259), (9, 427), (10, 686), (11, 1113), (12, 1799), (13, 2912), (14, 4711)]
bulk_exact_two_checks 18336
heavy_cover_flip_checks 18145
balanced_boundary_checks 191
N30_max_incomparability_degree 7
```

The finite computation is regression evidence only. The arbitrary-`N` conclusions are proved by the weighted-matching bijection and exact Fibonacci formulas above.

## 9. Exact status and source-bound handoff

- Width three, `pi=7`, rank variance `<=49/4` for `R_N`: **PROVED / inherited and reapplied**.
- Exact extension formula `E_N=8F_{N+1}-13F_{N-7}`: **PROVED**.
- `N-9` consecutive exact-two states with `1/5<q_i<4/13`: **PROVED**.
- `N-10` consecutive heavy cover flips with sandwich mass `>5/13` and **exactly two** external partner witnesses: **PROVED**.
- Balanced far boundary `1/3<q_{N-2}<2/5`: **PROVED**.
- Candidate local bounded-corridor termination from width/range/variance/two-witness data: **REFUTED**.
- POS3: **OPEN / NOT PROVED**.

**First essential missing implication.** At a maximal exact-two / heavy-flux corridor in a hypothetical cardinality-minimal no-balanced width-three core, prove a **boundary charge realization theorem**: the conserved exact corridor flux / latent mass must either become the ordering count of an incomparable pair in `[E/3,2E/3]`, or a multi-distinguisher/non-crossed exit must receive a disjoint charge large enough to force such a pair, unless there is strict strong-majority span descent or a valid autonomous/ordinal reduction. The `R_N` family is a regression guard: no proof may replace this global boundary step by a fixed local corridor-length bound, even under `pi=7` and rank variance `<=49/4`.

No brain installation or benchmark work was performed. No authenticated brain retrieval/context use occurred. No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email, Drive data, paid model/API/Codex execution, remote workflow, public posting, permission change, or production-brain mutation was used.
