# r24 addendum — exact overlap-mass threshold for fragment-uniform fiber aggregation

This note isolates the quantitative condition a future unnormalized sum/difference theorem must satisfy in order to survive arbitrary fragment geometry.

Let `E` be measurable with `|E|=1`, let `X,X'` be iid with density `1_E`, and put

\[
m_E(u)=|E\cap(E-u)|.
\]

Then `m_E` is the density of `U=X-X'`. Since `0<=m_E<=1` and `integral m_E=1`, for every `gamma>=1`,

\[
\boxed{\int_{\mathbb R}m_E(u)^\gamma\,du\le1.}
\]

Thus one full power of the unnormalized overlap mass is always integrable, with universal constant one; any higher power is also harmless.

The exponent `1` is sharp under the owner's arbitrary-fragment hypotheses.

## Theorem — QFORM-OVERLAP-MASS-INTEGRABILITY-THRESHOLD-v1

For compact finite-union sets `E` of measure one,

\[
\boxed{
\sup_E\int m_E(u)^\gamma\,du
\begin{cases}
=+\infty,&0\le\gamma<1,\\
\le1,&\gamma\ge1.
\end{cases}}
\]

For negative `gamma`, the integral may already diverge at ordinary overlap endpoints, so no fragment-uniform bound is available there either.

### Proof of sharpness below one power

Use

\[
E_N=\bigcup_{k=1}^N[4^k,4^k+1/N],\qquad \ell=1/N.
\]

As in the main r24 report, all off-diagonal difference clusters are disjoint, and on each one

\[
m_N(d_{jk}+w)=\ell-|w|,\qquad |w|<\ell.
\]

The diagonal cluster is

\[
m_N(u)=1-N|u|,\qquad |u|<\ell.
\]

For every `gamma>-1`, direct integration gives the exact identity

\[
\boxed{
\int m_N(u)^\gamma\,du
=
\frac{2}{\gamma+1}
\left[
\left(1-\frac1N\right)N^{1-\gamma}+\frac1N
\right].
}
\]

Hence for `0<=gamma<1` this grows like

\[
\frac{2}{\gamma+1}N^{1-\gamma}\to\infty.
\]

At `gamma=1` the formula equals one, as it must since `m_N` is a probability density. For `gamma>1`, the elementary inequality `m_E^gamma<=m_E` proves the universal bound one for every `E`. ∎

## Consequence for conditional-cap normalization

The exact conditional cap after the sum/difference transform is

\[
M(u)=\frac1{2m_E(u)}.
\]

Suppose a normalized fiber theorem pays `M(u)^alpha` with `alpha>0`. Multiplying back by the conditioning density `m_E(u)` produces

\[
m_E(u)M(u)^\alpha
=2^{-\alpha}m_E(u)^{1-\alpha}.
\]

The overlap exponent has dropped from the safe threshold `1` to `1-alpha<1`, and the theorem above shows that arbitrary fragments make the resulting integral nonuniform (or divergent if the exponent is at most `-1`).

Therefore the precise design requirement for an aggregate-before-normalization proof is:

> after all fiber estimates are combined with the conditioning measure, every independently conditioned overlap variable must retain at least one full power of its overlap mass, unless additional coupled cancellation is used before absolute values.

This is stronger and more actionable than the statement that conditional caps can blow up. It identifies the exact power at which fragment-uniformity is lost.

## Relation to account04/B14 r6

The r6 four-coordinate leakage theorem has common-cap homogeneity `M^2`. If inserted only after normalized conjugate conditioning, this necessarily removes positive overlap powers and crosses below the safe exponent one. The r24 cap-only obstruction proves that no monotone anisotropic bookkeeping of cap numbers alone fixes this. A successful use of r6 inside the decoupled route would need a new **unnormalized overlap-weighted leakage theorem** or a coupled estimate performed before fiber normalization.
