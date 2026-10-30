# QFORM B17 — fragmented dense-cone witness

Run: `20260923T171805Z-fleet04-B17-QFORM-r5`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **NEW SUPPORTING ANALYTIC WITNESS; FULL QFORM OPEN**  
Continuity: not claimed.

## Result

Let

\[
A={1\over6}\begin{pmatrix}
1&1&-2&-2&-2&-2\\
1&1&-2&-2&-2&-2\\
-2&-2&1&1&-2&-2\\
-2&-2&1&1&-2&-2\\
-2&-2&-2&-2&1&1\\
-2&-2&-2&-2&1&1
\end{pmatrix}.
\]

For `eta=10^{-3}` and any `R>1`, let the six independent physical
coordinates have the common probability density

\[
f_{R}(x)=\mathbf 1_{[-(1-\eta)/2,(1-\eta)/2]}(x)
          +\mathbf 1_{[R,R+\eta]}(x).
\]

Both support components are nonempty and disjoint, `0<=f_R<=1`, and
`\int f_R=1`.  Thus every physical marginal is genuinely fragmented;
the gap and support diameter may be arbitrarily large.

### Theorem `QFORM-DENSE-FRAGMENTED-MAIN-CELL-v1`

For `Q=X^TAX`,

\[
\operatorname{spec}(A)=\{1,1,-1,0,0,0\}
\]

and the density at the cone tip obeys

\[
\boxed{p_Q(0)\ge (1-\eta)^4 p_*(0)
>4.0468426965>4,}
\]

where `p_*(0)` is the exact centered-unit-cube value of fleet01/B17,

\[
p_*(0)=4.06307061680603726012548\ldots .
\]

Hence disconnected, arbitrarily separated cap-one supports in all six
original coordinates do not destroy the finite dense shared-sign
amplification.  This is not a counterexample to the conjecture and does not
improve the stronger diffuse lower obstruction `3\sqrt2`.

## Proof

The fleet01/B17 loading matrix has two copies of `e_j/\sqrt2` for each of
three banks and is Parseval.  Its three-dimensional core is the Householder
matrix `I-2nn^T`, `n=(1,1,1)/\sqrt3`; therefore the displayed physical matrix
has the exact spectrum stated above.

The product density expands into 64 nonnegative rectangular pieces.  Keep
only the piece on the main cube

\[
C_\eta=[-(1-\eta)/2,(1-\eta)/2]^6.
\]

The coarea density contribution at zero from this piece is

\[
I_\eta=\int_{C_\eta}\delta(x^TAx)\,dx.
\]

Put `x=(1-\eta)z`.  Since the dimension is six and the phase is homogeneous
of degree two,

\[
dx=(1-\eta)^6dz,\qquad
\delta(x^TAx)=(1-\eta)^{-2}\delta(z^TAz),
\]

so

\[
I_\eta=(1-\eta)^4
\int_{[-1/2,1/2]^6}\delta(z^TAz)\,dz
=(1-\eta)^4p_*(0).
\]

All other mixture pieces make nonnegative contributions, proving the lower
bound.  With `eta=10^{-3}`, directed decimal arithmetic gives

\[
(0.999)^4(4.06307061680603726012548)
=4.04684269651429455070\ldots>4.
\]

The argument uses only original-coordinate independence and an exact
positive component.  It does not use post-rotation independence,
arbitrary-joint coarea bounds, a numerical histogram, moment assumptions, or
a bounded-fragment reduction.

## Actual fleet01/B17 input and what changed

The exact base value and matrix are from
`yspennstate/math-open-problems@e83d0cc194d791acf31d6c86245204887cfd8171`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B17/20260923T144233Z-fleet01-B17-QFORM-auto11/REPORT.md`.
The later fleet01/B17 classification at commit
`829192412f2a2d84e72b4bed91115fc5fab68401` identifies fragmented and
off-zero mechanisms as unpaid.  The present theorem applies the exact dense
witness to a new law class: every physical marginal is disconnected with an
arbitrarily remote second component.  It does not settle genuinely balanced
fragment weights, off-zero peaks, the hybrid/convex upper bound, or arbitrary
additional spectrum.

## Remaining gap

The full conjecture remains open.  This calculation excludes one possible
escape in the witness search—namely that the known dense amplification is an
artifact of connected interval laws—but it supplies neither an unbounded
family nor a universal upper bound.  The live adversarial frontier is
balanced fragmentation/off-zero alignment in genuinely shared rows and the
interaction with extra spectrum.

