# POS3 B19 r11: augmented strong-majority acyclicity

Status: **ESSENTIAL_STEP_APPLIED; POS3 remains OPEN / NOT PROVED.**

Collective target: every finite nonchain poset of width at most 3 has an incomparable pair x,y whose uniform-linear-extension probability satisfies 1/3 <= Pr(x<y) <= 2/3.

Research mode: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## Consumed partner input

This run materially uses the named partner `account04/B10` r16 same-ray/outward-export result (brain coordination blob `78e86dcdaef62417888ef6d8b66bf3b6d062f2c9`): in the surviving no-balance branch, same-ray recycling inside the present envelope cannot close locally; compulsory distinguisher channels are exported beyond the current strong-majority envelope or strict span descent already occurs.

The first unresolved global issue from the preceding B19 run was cross-envelope vertex reuse: could exported channels later return to an earlier vertex/envelope without producing balance or another authorized exit?

## New theorem: augmented strong-majority relation is acyclic

Let P be a finite poset of width at most w, and let mu be **any** probability measure supported on the linear extensions of P. Define a directed relation R_mu on P by

1. x R_mu y whenever x <_P y; and
2. if x || y, put x R_mu y whenever mu[x<y] > 1 - 1/w.

Then R_mu is acyclic.

### Proof

Assume a directed cycle of minimum length

v_0 R v_1 R ... R v_{m-1} R v_0.

First, no edge of this shortest cycle can be a deterministic comparability. Suppose v_i <_P v_{i+1}. The preceding relation v_{i-1} R v_i has mu[v_{i-1}<v_i] > 1-1/w (deterministic R-edges have probability 1). Since every linear extension with v_{i-1}<v_i also has v_{i-1}<v_{i+1},

mu[v_{i-1}<v_{i+1}] > 1-1/w.

If v_{i-1} || v_{i+1}, this is an R-edge skipping v_i. If they are comparable, the reverse comparability v_{i+1}<_P v_{i-1} is impossible because the displayed event has positive probability, while v_{i-1}<_P v_{i+1} again gives an R-edge skipping v_i. Either case yields a shorter directed cycle, contradiction. Hence every cycle edge is a strict strong-majority edge between incomparable elements.

Second, no nonadjacent cycle pair can be comparable in P. Any such comparability is itself an R-edge in one direction; combining that chord with the oppositely directed proper segment of the original cycle gives a shorter directed cycle. Thus the cycle vertices are pairwise incomparable. Consequently m <= w.

For every individual linear extension, at most m-1 of the cyclic inequalities

v_0<v_1, v_1<v_2, ..., v_{m-1}<v_0

can hold. Averaging under mu gives

sum_i mu[v_i<v_{i+1}] <= m-1.

But every cycle edge is strict strong-majority, so

sum_i mu[v_i<v_{i+1}] > m(1-1/w).

Since m<=w,

m(1-1/w) >= m-1,

contradiction. Therefore R_mu is acyclic. QED.

## Sharpness

The strict threshold is best possible for arbitrary supported laws. Take a 3-element antichain and let mu be uniform on the three linear extensions

012, 120, 201.

Then Pr(0<1)=Pr(1<2)=Pr(2<0)=2/3, so replacing the strict `>2/3` threshold by `>=2/3` creates a directed 3-cycle.

For a hypothetical POS3 counterexample under the original uniform law, every incomparable pair is outside [1/3,2/3], hence exactly one orientation has probability strictly greater than 2/3. Thus the strict threshold is precisely the relevant one.

## Consequence for the cross-envelope recycling problem

For width 3 under the **true full-poset uniform linear-extension law**, orient every incomparable pair toward its >2/3 side and include all poset comparabilities. In a no-balanced candidate this gives a total acyclic order extending P and every strong-majority comparison.

Combining this with the account04/B10 outward-export result gives a genuine global exclusion: any recycler/export trajectory all of whose transitions are forward in this augmented strong-majority order cannot revisit a vertex. Therefore an all-heavy/all-order-forward cross-envelope recycling cycle is impossible.

This does **not** yet prove that every geometric recycler transition furnished by the local channel lemmas is R-forward. Hence it does not finish POS3. Instead it identifies the first unavoidable obstruction more sharply: any surviving cross-envelope reuse must contain a first transition that reverses the augmented strong-majority order (or else exit by an already-authorized descent/reduction).

The theorem is deliberately measure-robust: it holds for any fixed probability law supported on linear extensions. Therefore, when applied inside an exact deletion projection, it remains valid for the actual corridor-weighted/biased law itself. No induced deletion law is replaced by a uniform law.

## Exact regression census

A deterministic exact enumerator checked every distinct naturally labelled transitive closure on n=2,...,6, retained width <=3 posets, enumerated their full uniform linear extensions, formed the augmented >2/3 relation, and found zero acyclicity failures:

- n=2: 2 closures, 2 width<=3, 1 nonchain; failures 0.
- n=3: 7 closures, 7 width<=3, 6 nonchains; failures 0.
- n=4: 40 closures, 39 width<=3, 38 nonchains; failures 0.
- n=5: 357 closures, 314 width<=3, 313 nonchains; failures 0.
- n=6: 4824 closures, 3339 width<=3, 3338 nonchains; failures 0.

The verifier also exactly checks the 2/3 sharpness example above and terminates with `POS3_B19_AUGMENTED_ORDER_ACYCLICITY_PASS`.

Verifier SHA-256: `5110c8b5dfa32334f8621523a153b3faef95a2962c6dc8a685db55c227f45bab`.

Captured output SHA-256: `2505675bf4a669bc87146891c52782fc5acb53b98f419865c67deca62d02eca4`.

The census is regression evidence only; the theorem above is proved for arbitrary finite size and arbitrary supported law.

## First missing implication handed to partner

**SIGN-REVERSING EXPORT CHARGE.** Retain the exact full-poset or exact corridor-weighted law throughout. At the first cross-envelope recycler transition that is not forward in the augmented strong-majority order, prove that the reversal forces at least one of:

- a pair with probability in [1/3,2/3];
- strict strong-majority span descent;
- a four-antichain (impossible at width 3);
- a proper autonomous/ordinal reduction; or
- a non-crossed multi-distinguisher exit carrying enough signed target-scale charge to force one of the preceding outcomes.

This is now the earliest unresolved global implication. No claim that POS3 is solved is made.
