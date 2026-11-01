# B14 / A067 â Boolean degree granularity removes the real BH loss

**Run ID:** `20261012T001125Z-fleet01-B14-A067-boolean-granularity`  
**Primary packet:** A067 (Hypercontractive refinement)  
**Claim:** `B14-A067-BOOLEAN-DEGREE-FEI-v1`  
**Status:** `AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW`  
**Full FEI:** **OPEN**

## 1. Exact objective and prior obstruction

The frozen objective was to locate one logarithmic analytic loss, replace it
using genuine Boolean structure on a measurable regime, and replay the fixed
Renyi and near-Boolean controls.  A066 had already shown that even Fourier
support/parity-zero erasure is full-FEI-hard and does not restore semigroup
entropy monotonicity.  Thus this run uses the strictly stronger hypothesis of
bounded exact Fourier degree.

The generic real Bohnenblust--Hille inequality at exponent

\[
q=\frac{2d}{d+1}
\]

has a factor `C^{sqrt(d log d)}`.  Converting its q-norm estimate into the
Renyi entropy of the squared spectrum at order `d/(d+1)` retains an
`O(d^{3/2} sqrt(log d))` allowance.  The fixed-order Renyi shortcut is also
impossible: the campaign point-defect family has `H_alpha/I -> infinity` for
every fixed `alpha<1`.

## 2. Proved Boolean refinement

Let `f:{-1,1}^n->{-1,1}` have Fourier degree at most `d>=1`.  Put

\[
p_S=\widehat f(S)^2,\qquad
v=\sum_{S\ne\varnothing}p_S=1-p_\varnothing.
\]

Then

\[
\boxed{
H(f)\le 2(d-1)v+p_\varnothing\log_2\frac1{p_\varnothing}
\le \bigl(2(d-1)+\log_2e\bigr)I(f).
}
\]

The first inequality is sharp for the degree-d address function.

### Proof

Boolean MÃ¶bius inversion gives the known granularity law

\[
\widehat f(S)\in2^{1-d}\mathbb Z.
\]

Indeed, `(1-f(1-2z))/2` is a `{0,1}`-valued multilinear polynomial of
degree at most d with integer monomial coefficients.  Substitution
`z_i=(1-x_i)/2` gives the divisibility.

Every nonzero squared coefficient therefore obeys

\[
p_S\ge2^{2-2d}.
\]

For every nonempty S,

\[
p_S\log_2(1/p_S)\le2(d-1)p_S.
\]

Summing and retaining the empty spectral atom proves the first bound.  Also,

\[
(1-v)\log_2\frac1{1-v}\le v\log_2e,
\qquad v\le I(f),
\]

which proves the influence form.  For address, all `2^{2(d-1)}` nonzero
coefficients have magnitude `2^{1-d}` and the empty coefficient vanishes, so
the first inequality is equality.

This is a restricted, degree-dependent FEI theorem.  Its constant still grows
linearly with d and it does not settle full FEI.

## 3. Quantitative separation

For the degree-d AND/point-defect family with `mu=2^-d`,

\[
I=2d\mu,\qquad H/I\to4.
\]

The bare support estimate `H<=d` converts to the coefficient

\[
\frac dI=2^{d-1}
\]

in front of influence.  The Boolean refinement converts it to

\[
2(d-1)+\log_2e.
\]

This is an exponential improvement in the degree-d sparse regime, though it
is not sharp compared with the exact limiting ratio four.

## 4. Obstruction replay

- **Fixed Renyi:** no Renyi inequality is claimed.  At alpha=3/4, the exact
  point-defect ratios printed by the checker rise from 4.5356 at d=4 to
  129.3246 at d=16.
- **Near Boolean:** for the normalized real degree-one spectrum
  `(1-epsilon^2,epsilon^2)`, `H/I~log2(1/epsilon^2)`.  At
  `epsilon^2=2^-20` the ratio is 21.442694.  Booleanity is essential.
- **Addressing:** address saturates the sharp entropy allowance, but its
  influence grows; it is not an FEI counterexample.
- **Rare selectors and parity lifts:** their degree grows.  The result supplies
  no universal constant and does not pay rare logarithmic or semigroup
  variation debts.
- **Actual prime gates:** every fixed-degree gate lies in the proved regime,
  but composition can increase degree, so no unrestricted composition claim
  follows.

## 5. Exact computation

`CHECK.py` exhaustively enumerates every Boolean truth table through four
variables.  It uses integer FWHT values and `fractions.Fraction` for Parseval,
granularity, `v<=I`, and normalization; floating logarithms are used only for
entropy diagnostics.

Results:

- 65,812 truth tables exhausted;
- 65,804 nonconstant functions;
- 329,028 assertions passed;
- zero failures;
- no random seed.

The script also evaluates the AND/point-defect comparison for d=2,...,12,
the fixed-Renyi obstruction, and the real near-Boolean control.

## 6. Literature and novelty boundary

The granularity lemma and sharp support count are known; no novelty is claimed
for them.  Source-exact checks used:

1. Avishay Tal, *Shrinkage of De Morgan Formulae from Quantum Query
   Complexity*, ECCC Report 48 (2014), Fact 2.5 and Corollary 2.7.
2. *A cb-Bohnenblust--Hille inequality with constant one and its applications
   in learning theory*, Mathematische Annalen (2025), Lemma 4.1,
   Proposition 4.2 and Theorem 4.3.  The paper explicitly contrasts the sharp
   Boolean constant with the real `C^{sqrt(d log d)}` factor.

The campaign delta is the explicit influence-weighted Shannon corollary, its
sharp first term, and the controlled comparison required by A067.  It is an
author proof pending independent reconstruction, not an accepted new theorem
or a full-FEI solution.

## 7. Handoff

Route to A088 and A094 for independent proof reconstruction and to A070 for
analytic-route comparison.  The next mathematical target is to replace exact
degree d by a scale-sensitive Boolean tail condition without paying a fixed
Renyi order or a growing degree constant.
