# B12 / A056 — exact GU cocycle for one biased child

Run: `20261013T162122Z-fleet01-B12-gu-biased-child`  
Attempt: `A056-GU-BIASED-CHILD-03`  
Gap: `B12-A056-GU-COMPOSITION-v1`  
Status: **EXACT BIASED-CHILD FORMULA AND COMPLETE-TREE COCYCLE PROVED BY CONTRIBUTOR; UNIVERSAL RESERVE BOUND OPEN**

## Main result

Let an arbitrary Boolean outer gate be decomposed in one input as

\[
g(y,z)=a(z)+yb(z),\qquad \beta=\|b\|_2^2=\operatorname{Inf}_y(g),
\]

and substitute an arbitrary disjoint Boolean child `h` of mean `mu` into
that input.  This run constructs an explicit scalar potential
`Theta_{g,y}(mu)` and proves

\[
\boxed{U(g(h,z))=\beta U(h)+\Theta_{g,y}(\mu)}.
\]

Thus the complete dependence on the nonconstant spectrum of the biased child
is exactly `beta U(h)`; the composition defect depends on the child only
through its mean.

For every physical child coordinate `i`, with restricted means `mu_-` and
`mu_+`, subtraction gives the signed cocycle

\[
\boxed{
\Delta_iU(g(h,z))
=\beta\Delta_iU(h)
+\Theta(\mu)-\frac{\Theta(\mu_-)+\Theta(\mu_+)}2.}
\]

No nonzero-bias, separation, sign, or regularity hypothesis is used.

## Complete adaptive hierarchy

For every complete adaptive restriction tree on the child block, the entire
coherent composition defect telescopes exactly:

\[
\sum_vw_vR_v
=\Theta(\mu)
-\frac{1+\mu}{2}\Theta(1)
-\frac{1-\mu}{2}\Theta(-1).
\]

This endpoint-centered reserve is independent of child dimension, Fourier
shape, hierarchy depth, and adaptive query order, and unchanged cylinder
queries have zero charge.  It is the upper-mass analogue of the earlier raw
entropy Doob potential, now at the exact `U` functional required by GU.

## Exact formula

Writing `a_T,b_T` for the Fourier coefficients on the remaining outer
variables, define

\[
B_T=\sum_{R\supseteq T}b_R^2,
\quad
C_T(\mu)=\sum_{R\supseteq T}
\big((a_R+\mu b_R)^2+(1-\mu^2)b_R^2\big).
\]

The cap is affine in the bias:

\[
C_T(\mu)=\sum_{R\supseteq T}(a_R^2+b_R^2+2\mu a_Rb_R).
\]

The complete definition and proof of `Theta` are in
`GU_BIASED_CHILD_COCYCLE.tex`.

## Why this matters

The previous run proved the balanced root chain rule and solved parity inner
blocks, where restriction stays balanced until a terminal step.  This run
handles an arbitrary biased Boolean child and shows that the feared changing
coherent remainder is not a high-dimensional spectral object at this scope:
it is a one-dimensional endpoint-centered cocycle.

The newer B19/A091 review independently accepted the product-biased block
identity and proved that a rare-bias tax of order `p log(1/p)` is genuinely
necessary in its setting.  The present result respects that correction: it
does not discard the bias term, but carries it exactly in `Theta` and cancels
it only through the physical hierarchy telescope.

## Candidate payment and tests

The remaining scalar conjecture is

\[
\overline\Theta_{g,y}(\mu)
\le3\beta(1-\mu^2),
\]

or locally

\[
\Theta(\mu)-\tfrac12\Theta(\mu_-)-\tfrac12\Theta(\mu_+)
\le3\beta\operatorname{Inf}_i(h).
\]

This run does **not** label either inequality proved.  Exhaustive finite tests
found no falsifier:

- 205,344 exact biased-composition formula checks;
- 555,024 normalized local-defect checks;
- maximum observed normalized defect `2.280249404938720832...`;
- margin below the candidate constant 3: `0.719750595061279167...`;
- 37,728 complete-tree cocycle checks;
- every outer Boolean gate through arity three;
- every child Boolean function through dimension three;
- no random seed.

Walsh coefficients, means, and influences are exact rational values;
logarithms use 90-digit decimal arithmetic.  These checks are **NUMERICAL** at
their finite scope.

## Previous/new bound and scope

- Previous: the balanced root chain rule did not survive generic child
  restriction because the two children became biased.
- New: the full defect is an exact scalar Doob cocycle, with no dimension,
  depth, query-order, collision-ratio, or child-spectrum factor.
- Still unpaid: a uniform influence bound for the endpoint-centered scalar
  reserve.  The candidate constant 3 is numerically supported but unproved.

The theorem covers one arbitrary biased child, an arbitrary outer gate, and
fresh remaining outer bits or disjoint nonempty parity characters.  Multiple
simultaneously biased non-character children and overlapping physical inputs
remain outside its proved scope.

## Next action

Prove or refute the scalar semiconcavity inequality for
`overline Theta`.  The caps are affine in `mu`, so the promising analytic
route is to differentiate the endpoint-centered formula and combine the
Boolean identities `a^2+b^2=1`, `ab=0` with the sharp kernel convexity bound.
Any proof must retain the rare-bias endpoint terms accepted by B19/A091.

Independent review is not observed.  Universal GU and full FEI remain open.

