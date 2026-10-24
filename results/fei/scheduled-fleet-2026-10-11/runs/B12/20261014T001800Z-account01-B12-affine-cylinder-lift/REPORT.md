# B12 / A058 — affine-cylinder source lifting

## Outcome

**PROVED a dimension-free lifting theorem for affine disagreement supports
with internal physical directions.  Independent review pending.**

Write an affine support as

\[
 A=\{-1,1\}^T\times A',
\]

where every remaining physical coordinate is transverse to the affine set
`A'`.  An arbitrary signing of this support has the form

\[
 b(x,y)=1_{A'}(y)g_y(x).
\]

If every Boolean fiber `g_y` satisfies FEI with constant `C`, then

\[
 \boxed{\mathcal E(b)
 \le C\mathcal I_T(b)+4\mathcal I_M(b)
 \le\max\{C,4\}\mathcal I(b).}
\]

The constant is independent of the ambient dimension, affine codimension,
density, number of labels, overlap multiplicity, sign variation, and
restriction depth.  The transverse constant `4` is sharp for point support.

This strictly extends the preceding theorem, which required every coordinate
to be transverse.  The new class permits an arbitrary number of internal
coordinates and arbitrary variation of the Boolean fiber across the oblique
affine labels.  It also includes coordinate subcubes: FEI for the internal
Boolean signing lifts across the sparse support without worsening a constant
`C>=4`.

## Mechanism

If `A'` has dimension `d`, codimension `r`, and density `p=2^{-r}`, the
complete coherent spectrum has the exact joint-law representation

\[
 \mathcal E(b)=2rp+pH(Q).
\]

The marginal of `Q` is the mixture of the fiber spectral laws.  Revealing the
affine label costs at most `d` bits, and the remaining quotient frequency
costs at most another `d` bits:

\[
 H(Q)\le2d+\mathbb E_yH(g_y).
\]

Both label costs are paid once by the exact transverse boundary influence

\[
 \mathcal I_M(b)=\frac{(r+d)p}{2}.
\]

The internal influence is exactly

\[
 \mathcal I_T(b)=p\mathbb E_yI(g_y).
\]

This is a genuine joint posterior payment: it does not assume Fourier-sector
orthogonality and does not recharge by affine-label count or hierarchy depth.

Combining it with the previous affine-support collision inequality gives

\[
 \mathcal E(hb)\le H(F)+\mathcal E(b)
 \le H(F)+C\mathcal I_T(b)+4\mathcal I_M(b)
\]

for the corresponding Boolean overlap realization `F=a+hb`.

## Verification

`CHECK.py` uses integer Walsh transforms and verifies:

- the exact joint-spectrum identity;
- the exact internal/transverse influence decomposition;
- the two-stage posterior entropy bound;
- the split and uniform FEI inequalities.

It passed 12,493 affine-cylinder signings: 8,568 exhaustive and 3,925
deterministic sampled cases, including 11,861 cases with both internal and
oblique directions.  Point-support equality was checked in dimensions
1 through 12.

## Stress controls and limitations

- Point support attains `4`, so the transverse constant cannot improve.
- Arbitrary sign variation across affine labels is included.
- Physical restrictions preserve the support structure when the fiber class
  is itself restriction hereditary.
- X007 is not contradicted: its support is non-affine.
- When there is no transverse boundary, the theorem reduces to the assumed
  fiber FEI statement; it does not circularly prove FEI for arbitrary fibers.

## Remaining universal gap

Non-affine disagreement supports still need either a decomposition into
affine cylinders whose posterior labels share one boundary budget, or a
direct joint activation credit.  The next target is a two-piece gluing lemma
that tracks the extra label bit by the physical edge boundary between pieces,
with X007 and the signed-mask tensor family as mandatory controls.

Full FEI remains **OPEN**.

