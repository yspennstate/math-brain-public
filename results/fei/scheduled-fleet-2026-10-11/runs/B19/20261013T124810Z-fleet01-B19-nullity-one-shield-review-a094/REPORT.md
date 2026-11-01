# B19 / A094 independent review — nullity-one arbitrary-core shield

## Verdict

**`B05_A023_NULLITY_ONE_SHIELD_v1` is independently accepted at its declared
scope.**  No proof repair is required.

For every \(M\in\mathbb F_2^{s\times m}\) with
\(\operatorname{rank}M=m-1=:r\), every Boolean core \(D\), every affine
phase and every physical orientation of the kernel, the function
\[
P(x,y)=(-1)^{x^TMy+a\cdot x+b\cdot y+c}D(y)
\]
has a squared Fourier law uniform on exactly \(2^{2r}\) atoms.  Thus
\[
H(P)=2r,\quad U(P)\le2r,\quad I_x(P)\ge r/2,\quad I_y(P)\ge r/2.
\]
For every finite adaptive/pruned restriction tree querying only physical
\((x,y)\)-variables and every common disjoint Boolean factor \(h\),
\[
U(Ph)-\sum_\ell w_\ell U(P_\ell h)
\le4I_x(P),\qquad
U(Ph)-\sum_\ell w_\ell U(P_\ell h)
\le2I(P).
\]

## Independent proof audit

The two-point-fiber argument is exact in the original physical basis.  For
each admissible \(\alpha\), precisely one parity class of
\(\beta\cdot v\) survives, independent of the density or orientation of
the kernel vector \(v\) and independent of the core signs.  The count and
normalization are therefore exactly \(2^{2r}\) atoms of mass \(2^{-2r}\).

The influence bounds also survive an arbitrary core.  Every nonzero row of
\(M\) gives an \(x\)-influence of \(1/2\).  For a nonzero column, fixing
\(y\) leaves a nonconstant character of \(x\); averaging over \(x\)
therefore gives \(y\)-influence \(1/2\) despite the factor
\(D(y+e_j)/D(y)\).  Rank \(r\) forces at least \(r\) nonzero physical rows
and columns.

The tree statement is an endpoint telescope, not a nodewise positivity or
single-event ownership theorem.  The complete signed node sum is root
\(U\) minus weighted leaf \(U\), and nonnegativity of leaf \(U\) closes the
bound.  A common disjoint \(h\) cancels by exact tensor additivity.

## Independent verification

The checker was written independently and imports none of the author's code.
It passed:

- all 372 rank-\((m-1)\) binary matrices with \(m,s\le3\);
- all 86,556 matrix/core pairs and 173,112 exact fiber-spectrum instances;
- 1,008 direct truth-table/Walsh reconstructions comprising 10,836 nonzero
  atoms;
- 1,008 exact physical-influence audits;
- 400 branch-dependent adaptive/pruned trees;
- 480 direct disjoint tensor-additivity checks.

The largest sampled ratios were \(U/I_x=2\) and \(U/I=1\).  These numerical
values are controls, not a proof of the stronger constants.

## Class extension and source overlap

The previously accepted arbitrary-core result required full column rank.
This theorem adds every nullity-one matrix without parameter dependence;
together the reviewed class is \(\operatorname{rank}M\ge m-1\).  It allows
arbitrary core bias, defect count and overlap, tree depth, reveal order and
leaf rarity, subject to one fixed shield and one common disjoint retained
factor.

Potapov's 18 September 2026 manuscript already proves FEI for plateaued
Boolean functions.  The flat/plateaued spectrum is therefore not treated as
a novelty claim.  That endpoint result does not supply the campaign's
upper-set \(U\) identity, physical control/data ledger or retained-\(U\)
tree statement.  No priority claim is approved.

## Exact limitation and next unpaid step

The theorem does **not** provide nodewise nonnegative credit, allow
leaf-dependent or shared-variable terminal cores, or establish the universal
GU inequality.  When nullity is at least two, an arbitrary four-point (or
larger) fiber of \(D\) may have several unequal Walsh masses.  The exact
unpaid term is the conditional fiber-spectrum entropy
\[
\mathbb E_\alpha H\!\left(\widehat{D|_{y_\alpha+\ker M}}^{\,2}\right).
\]
It still needs a dimension-independent single-use payment by physical
data-core influence plus retained terminal \(U\), without a basis change or
descendant reuse.

Full FEI remains **OPEN**.
