# B11 / A052 — upward-potential persistence on critical restriction frontiers

**Run:** `20261012T042052Z-fleet01-B11-a052-u-persistence`  
**Primary packet:** A052 (Critical-source structure)  
**Attempt:** `A052-U-PERSISTENCE-3`  
**Claim:** `B11-A052-U-PERSISTENCE-v1`  
**Gap:** `G-CRITICAL-U-PAYMENT`  
**Status:** analytic structural theorem PROVED pending independent review; universal upper payment OPEN; full FEI OPEN.

## Frozen objective and prior value

The prior A052 result identified the coordinate slack

`s_i = Delta_i H - R Inf_i`

as the influence-weighted child ratio deficit, but supplied no bound connecting
that slack to the live FEI-equivalent upward potential `U`. The public owner
target asks whether the established critical profile can force `U<=K I` on
finite-dimensional maximizers.

This run pins the exact consequence that the current profile actually proves,
without reversing an inequality: small critical slack forces `U` to persist on
the physical restriction frontier.

## New theorem

Let `R` dominate `H(g)/I(g)` on a family of physical restrictions `g`, and set
`delta(g)=R I(g)-H(g)`. Averaging the full Theorem G inequality, including its
variance and normalization terms, gives

`E U(g) >= (R-2) E I(g)/2 - E delta(g)/2 + E Var(g) + E b(g)/2`,

where `b(g)=(1-Var(g)) log2(1/(1-Var(g)))`.

For the two children of a descendant-critical source, `E delta` is exactly the
A052 slack `s_i`. This is therefore a source-complete bridge from critical
slack to `U`, not a new assumption.

For an `n`-dimensional maximizer with ratio `c_n`, retain each coordinate with
probability `t` and assign the rest uniformly. The proved extremizer deficit
bound then yields

`E U(f_{J,X}) >= [(c_n-2)t/2 - (1-t)/ln 2] I(f)`

plus the two explicit nonnegative terminal terms `E Var` and `E b/2`.

Equivalently, under influence-biased sampling of the restriction frontier,
the mean `U/I` is at least

`a_t=(c_n-2)/2-(1-t)/(t ln 2)`.

Since every descendant has `0<=U/I<=H/I<=c_n`, the influence mass with
`U/I>=theta` is at least `(a_t-theta)/(c_n-theta)` for every
`0<=theta<a_t`. Thus a high-ratio maximizer cannot shed its upward-potential
hardness on almost all of a near-full restriction frontier.

## Why this matters and what it does not prove

This theorem joins three audited pieces that previously sat separately:

1. A052 exact child surplus;
2. Theorem C's random-restriction deficit control;
3. the full `H`-to-`U` inequality, with all terminal terms retained.

It supplies a quantitative stopping-frontier obstruction: any proposed
critical-pruning proof must transport a positive mass of `U`-hard children,
not merely one high-ratio child. It also prevents the invalid inference that
criticality itself gives an upper bound on `U`.

The direction is persistence, not payment. It does **not** establish
`U(f)<=K I(f)` and therefore does not settle FEI. The next unpaid step is an
independent upper-set asymmetry, pivotal-height, or GU' budget that contradicts
this persistent frontier when `c_n` is large.

## Controls and verification

- Constant restrictions are included with `H=I=U=Var=b=0`.
- Equal-ratio tensor products can have zero slack; the theorem then correctly
  propagates hardness and claims no tensor gain.
- Point defects and read-once AND/OR formulas can saturate Theorem G, so no
  coefficient was improved.
- The proof uses genuine physical restrictions. Abstract support components,
  weighted spectra, and arbitrary probability laws are not substituted.
- `python3 verify_u_persistence.py` exhaustively checks every one-coordinate
  instance on every descendant-critical Boolean function through four bits,
  and the binomial restriction statement on every finite-dimensional maximizer
  through four bits at `t=1/4,1/2,3/4,1`.

## Sources actually used

- Owner control revision `2026-10-12.1`, source commit
  `40210272c19f43fed84f6a67653f9a04b0e11e28`.
- B11 assignment blob `faaa0875ddb129d134bb62abb513f3795e88b590`.
- A052 critical-slack proof blob `33850b3519c3e04e8ea1e59eef7d7d8ffe956b8a`.
- U-universal notes blob `3b0636c653c7818368eeb204011c3e1ff21c234e`:
  Theorem G and Theorem C(ix).
- Independent U-route referee blob
  `87326516f71374bb2b37d593952be7ec581ee0f1`, which confirms both dependencies
  (with only the irrelevant `n=1` edge correction to Theorem C(ii)).

No literature novelty claim is made.

## Routing

Route to A055, A087, A090, A094, A096, A099 and B20. Independent review has
not been performed. A052 remains ACTIVE because its universal `U`-payment
target is open.

