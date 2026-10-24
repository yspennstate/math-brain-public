# B17 / A084 — explicit rare-bias completion for the two-bit half-tax kernel

**Status:** PROVED at the stated two-bit scope, pending independent review. **Full FEI remains OPEN.**

## Frozen candidate and prior boundary

The selected claim is the two-bit Boolean AND inequality

\[
J_A\le M_A+\tfrac12\Delta_A
\]

for every `0<p<=1/2` and `0<=q<=1`. The previous rigorous continuum coverage included the complete strip `1/64<=p<=0.49` for all `q`, plus separately proved balanced collars. The rare-bias theorem had only a nonexplicit existence radius, so it did not join to the certified strip.

Primary packet: **A084 (Continuum parameters)**. Attempt: `A084-RARE-TAIL-1`. Stable gap: `FEI-GAP-TWO-BIT-HALF-TAX`. Claim version: `B17-A084-RARE-TAIL-v1`.

## New theorem

For the exact margin

\[
D(p,q)=M_A+\frac12\Delta_A-J_A,
\]

the result is

\[
\boxed{D(p,q)>0\quad\text{for every }0<p\le1/64,\ 0\le q\le1.}
\]

Thus the rare-`p` transition is now fully covered, with no dependence of the constant `1/2` or the cutoff on `q`.

## Analytic compactness reduction

In natural-log units, the singular margin is factored exactly as

\[
\frac{(\ln2)D(p,q)}p=A(p,q)\ln\frac1p+F(p,q),
\]

where

\[
A(p,q)=8(q-1/4)^2+p\,[4q(1-q)-4q^2]\ge0
\]

throughout `0<=p<=1/64`, `0<=q<=1`. The proof of nonnegativity is an explicit quadratic discriminant calculation. The remainder `F` is rewritten using continuous divided differences so it extends to `p=0` without a `0/0` term. Therefore

\[
\frac{(\ln2)D(p,q)}p\ge A(p,q)\ln64+F(p,q)=E_{64}(p,q),
\]

and `E_64` is continuous on the closed rectangle `[0,1/64]x[0,1]`.

The 80-digit directed-rounding certificate proves

\[
E_{64}>0.01161006005382538799
\]

on that entire rectangle. It visited 175 boxes, accepted 88 leaves, reached depth 8, and had zero unresolved boxes. No grid inference and no floating-point sign decision is used.

## Before/after and exact GU implication

- **Before:** the rare-bias result held only for an unspecified sufficiently small `p`; the explicit certified region started at `p=1/64`.
- **After:** the two regions join exactly at `p=1/64`, and the entire rare tail is proved for every second bias including `q=0,1`.
- **Removed dependence:** the joining radius is explicit and uniform in `q`; zero/deterministic endpoints are included through the continuous normalized chart.

This is a local GU input, not the universal GU theorem. If a higher-arity restriction assembly proves that the corresponding `M_A` terms telescope/cancel and that `sum Delta_A<=I(f)` with no physical-coordinate reuse, then the half-tax inequalities imply

\[
G(f)\le\tfrac12 I(f),
\]

so `(a,b)=(1/2,0)` would close GU and yield `H(f)<=3I(f)` through the source-reviewed reduction. Those higher-arity and global single-use premises are still OPEN. A two-bit certificate alone does not establish them.

## Scope and next unpaid step

The theorem covers every parameter omitted by the rare-`p` boundary, but not the remaining near-balanced endpoint strips `0.49<p<=0.5`, `q` near `0` or `1`. More importantly, it does not cover arbitrary block arity or prove nonreuse in a full restriction tree.

The next mathematical step is to normalize the equality-corner strips by their exact cusp scale and complete the two-bit continuum; the next GU-level step is to test whether the half-tax coefficient survives a genuine three-bit prime gate and to expose the exact non-telescoping remainder.

Requested independent reviewers: A085, A090, and A094. No independent acceptance is claimed.

