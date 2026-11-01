# B05 / A023 — singleton-potential first-revelation amortization

## Outcome

**AUTHOR-PROVED CLASS EXTENSION; INDEPENDENT REVIEW PENDING.**

The mixed-sign (8/3) endpoint theorem cancelled a common disjoint terminal
core only at the completed tree.  This run adds an actual single-use credit
for the logarithmic cusp created at every half-activation.

Define

\[
\phi(h)=2h^2\left(\log_2\frac1h+\frac1{\ln2}\right),
\qquad
\Phi(f)=\sum_i\phi(|\widehat f(\{i\})|).
\]

The exact scalar midpoint charge obeys

\[
R(m)-\frac{R(m-h)+R(m+h)}2\le\phi(h).
\]

Under a fresh fair half-activation,

\[
\Phi(A(q))\le\rho\Phi(q)+M\frac{1-\mathbb Eq}{2},
\quad
\rho=\frac{1+\ln2}{4}<\frac12,
\quad M=\frac2{\ln2}.
\]

With (lambda=4/(1-\ln2)), the identity
(1+\lambda\rho-\lambda/2=0) pays every midpoint logarithm exactly once.

## Restriction-closed theorem

Let (mathcal C) be restriction-closed and satisfy
(G\le aI+bU), (0\le b<1).  Close it under:

- multiplication by arbitrary finite products of signed point defects on
  fresh disjoint blocks;
- fresh fair half-activation; and
- arbitrary physical restrictions.

Every resulting Boolean function (F) satisfies

\[
\boxed{
G(F)\le\left(\max\{a,5\}+\frac8{\ln2(1-\ln2)}\right)I(F)+bU(F).
}
\]

The constant is independent of dimension, depth, point-defect ranks and
activation probabilities, sign changes, the number of rare-defect factors,
and the restriction pattern.  Starting from constants and signed parities
gives the explicit bound

\[
\boxed{G(F)\le42.6126911533\,I(F)}
\]

on a genuinely restriction-closed expanding class.

The proof uses the stronger invariant

\[
G(f)+\lambda\Phi(f)\le A I(f)+bU(f).
\]

Disjoint rare-defect products increase (Phi) only by
(M I); half-activation contracts all inherited singleton credits by
(ho<1/2).  This is the requested explicit single-use ownership mechanism,
not an endpoint-only cancellation.

## Necessary correction to the previous positive tower report

The earlier additive recurrence
(G(F_d)\le2^{-d}G(P)+24) remains useful, but its conversion to a GU'
multiple used (I(F_d)\ge1).  That assertion is false: for a constant seed,
after the balanced first cap and one positive (Q_r) step,

\[
I(F_2)=\frac34+\frac{r+1/2}{2^r}<1\qquad(r\ge6).
\]

Long positive high-rank runs make (I) arbitrarily small.  The new potential
invariant supplies a correct GU' transfer and covers arbitrary sign changes.
The earlier endpoint (U\)-recurrence is not refuted by this correction.

## Verification

The checker passed 950,254 scalar tests, 4,448 exact truth-table identity
checks, 3,058 invariant checks, 11,992 restriction checks, and 48 deeper
generated cases.  Exact Walsh reconstruction errors were below
(9\times10^{-16}).  The finite audit supports but does not replace the
analytic all-parameter proof.

## Exact remaining gap

The new potential removes depth, rarity, sign, and restriction dependence for
fresh disjoint point-defect products, but not variable reuse or coherent
overlap.  In the overlapping case, product additivity of (G,U,I) used in
the invariant is absent.  The next unpaid lemma is an overlap-stable analogue
of

\[
\Phi(Bh)\le\Phi(h)+M I(B)
\]

together with the corresponding signed (U)-composition correction.  Full
FEI remains **OPEN**.
