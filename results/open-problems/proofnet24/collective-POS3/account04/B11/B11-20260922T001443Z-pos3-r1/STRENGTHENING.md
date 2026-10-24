# Strengthening — effective boundary width two gives a `1/81` canonical rank atom

This note supersedes only the numerical constants in Sections 3--5 and 8 of `REPORT.md`; all weaker statements there remain correct.

## Observation

Keep the notation of Theorem 3.1 in `REPORT.md`.  Let

`A=max(D_x)`, `B=min(U_x)`

and remove boundary elements whose relation to `x` is already forced by the poset:

`A_i={a in A : a || x}`, `B_i={b in B : b || x}`.

Every member of `A\A_i` satisfies `a<x` deterministically, and every member of `B\B_i` satisfies `x<b` deterministically.  Therefore

`{A precedes x precedes B} = {A_i precedes x precedes B_i}`.

Now `A_i union {x}` is an antichain, as is `B_i union {x}`.  Since the ambient width is at most three,

`|A_i|<=2` and `|B_i|<=2`.

If both sets are nonempty, every `a in A_i,b in B_i` satisfies

`Pr(a precedes x)>2/3`, `Pr(x precedes b)>2/3`,

so

`Pr(a precedes x precedes b)>1/3`

by the union bound.  Apply the boundary-product lemma from `REPORT.md` directly to the reduced sets `A_i,B_i` (that probability lemma does not require them to be the full maximal/minimal boundaries).  Then

`Pr(A precedes x precedes B)`
` = Pr(A_i precedes x precedes B_i)`
` >= product_{a in A_i,b in B_i} Pr(a precedes x precedes b)`
` > (1/3)^(|A_i||B_i|)`
` >= 1/81`.

As before, this event forces every element of `D_x` before `x` and every element of `U_x` after `x`; hence, with `k_x=|D_x|+1`,

`Pr(f(x)=k_x)>1/81`.

If `D_x` is empty, only the incomparable members of `B=min(U_x)` need stochastic control.  There are at most two of them.  Shepp's XYZ inequality gives

`Pr(f(x)=1) >= Pr(x precedes B_i) > (2/3)^2 = 4/9`.

The case `U_x` empty is symmetric.

## Sharpened corollaries for a hypothetical POS3 counterexample

For every `x`,

`q(x):=max_k Pr(f(x)=k) > 1/81`.

At either endpoint of the inherited strong-majority total order,

`q(x)>4/9`.

Splicing this into the assigned partner account01/B19 one-element deletion recurrence improves the counterexample-specific mean insertion-multiplicity bounds to

`e(P)/e(P-x) < 81`

for every element, and

`e(P)/e(P-x) < 9/4`

at the two strong-majority endpoints.

Equivalently, for uniform `tau in L(P-x)`,

`E[W_x(tau)]<81`,

with endpoint mean `<9/4`.

Likewise, in account01/B10's exact three-chain path model the canonical `x` edge carries more than `E/81` full paths, and an endpoint canonical edge carries more than `4E/9`.

The revised deterministic regression uses these stronger constants and still passes all `3275` qualifying local `(P,x)` cases through `n<=6`; the smallest observed canonical rank atom is `1/5` and the smallest observed one-sided atom is `10/19`.

No claim is made that `1/81` is optimal.  The improvement comes solely from deleting deterministic comparable boundary members before applying the two-sided product inequality; it does not assume any unproved finite-kernel or uniform-deletion property.
