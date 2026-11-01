# B01 / A003 — branched tensor/activation GU' closure

## Outcome

**AUTHOR-PROVED RESTRICTION-CLOSED CLASS EXTENSION; INDEPENDENT REVIEW PENDING.**

The independently reviewed singleton potential is subadditive under the
disjoint product of **any** two Boolean factors.  Consequently the B05
one-spine/point-defect construction extends to arbitrary finite branched
disjoint product/activation trees.

If a restriction-closed base class satisfies

\[
G\le aI+bU,\qquad 0\le b<1,
\]

then its closure under arbitrary disjoint products, fresh fair
half-activation, and restrictions satisfies

\[
G(F)\le A_*I(F)+bU(F),
\quad
A_*=\max\{a,8/3\}+\frac8{\ln2(1-\ln2)}.
\]

Restriction induction therefore gives

\[
U(F)\le\frac{A_*}{1-b}I(F),\qquad
H(F)\le\left(2+\frac{2A_*}{1-b}\right)I(F).
\]

Starting from constants and signed characters yields the explicit universal
constant on this class

\[
\boxed{H(F)<82.558716,I(F)}.
\]

The proof also improves the activation/root price from `5` to `8/3`.  It uses
the reviewed `R(t)<=1` on `[-1,0]`; on `[0,1]`, convexity of `R'` and a
tangent estimate at `1/2` give `R'(t)>-4/3`, hence
`R(t)<=(4/3)(1-t)`.

## Verification

The independent checker passed:

- 200,001 scalar root-price checks;
- 12,000 disjoint-product identity/potential checks;
- 241 recursively generated branched functions;
- 482 activation checks;
- 964 invariant/endpoint checks; and
- 2,868 physical restriction checks.

## Exact scope

The new operation is arbitrary disjoint tensoring of already generated
members, allowing genuine branching rather than a single activated spine with
point-defect side factors.  The theorem is uniform in dimension, branching,
depth, sign, and dyadic rarity and is genuinely restriction-closed.

It does not handle biased selectors or any reused/shared physical variable.
The universal aggregate upper-set asymmetry mismatch therefore remains open.
Full FEI remains **OPEN**.

