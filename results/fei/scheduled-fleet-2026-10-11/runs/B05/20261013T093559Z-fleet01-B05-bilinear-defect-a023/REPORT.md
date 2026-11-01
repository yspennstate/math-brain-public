# B05 / A023 — arbitrary-rank bilinear control sharing a point defect

Run: `20261013T093559Z-fleet01-B05-bilinear-defect-a023`  
Primary packet: **A023 (Amortized rarity budget)**  
Stable gap: `B05_RARE_REFUNDS`  
Claim version: `B05_A023_BILINEAR_DEFECT_v1`  
Status: **AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW**  
Full FEI: **OPEN**

## Result

The preceding shared-variable theorem allowed one selector centre. This run
removes that parameter restriction completely.

For \(x\in\mathbb F_2^s\), \(y\in\mathbb F_2^m\), and any binary matrix
\(M\) of rank \(r\ge1\), define
\[
P(x,y)=(-1)^{x^TMy+a\cdot x+b\cdot y+c}
       (1-2\mathbf1_{\{y=0\}}).
\]
For any arbitrary Boolean terminal core \(h\) on a disjoint block, every
finite adaptive/pruned restriction tree on the \(P\)-variables satisfies
\[
\boxed{
U(Ph)-\sum_\ell w_\ell U((Ph)_\ell)
\le\frac{25}{4}I_{x,y}(P).
}
\]
The base family also satisfies
\[
U(P)\le H(P)\le\frac{25}{4}I(P).
\]
The constant is independent of the number of centres, matrix rank, all row
and column overlaps, dimensions, affine phases, restriction depth/order, and
terminal-core complexity.

## General pattern

Although the selectors may overlap arbitrarily, the one-point defect changes
the Fourier vector only in one selector-frequency layer. If \(r=\operatorname{rank}M\)
and \(k=m-r\), the exact entropy is
\[
H(P)=2r+2^{-r}E_k,
\]
where
\[
E_k=h_2(4,2^{-k}(1-2^{-k}))
 +4,2^{-k}(1-2^{-k})\log_2(2^k-1),
\]
with \(E_0=0\), and \(E_k<9/4\) uniformly. At least \(r\) selector rows
are nonzero, so their physical influence is at least \(r/2\). This pays the
entire spectrum with the constant \(25/4\). Disjoint additivity then retains
the arbitrary leaf packet \(U(h)\) exactly once.

This replaces the four-exceptional-atom calculation for one star by an exact
rank/codimension formula valid for arbitrarily many coherent centres.

## Verification

`CHECK_BILINEAR_DEFECT.py` independently checks exact Walsh spectra, the
entropy formula, physical influences, \(U\le H\), and the \(25/4\) bound. It
exhausts every binary matrix through size \(3\times3\) under four affine
placements, adds 240 seeded larger matrices (including dependent and repeated
rows), and checks the analytic rank/codimension inequalities through rank 32
and codimension 64. The finite work corroborates; it does not replace the
all-parameter proof in `PROOF.md`.

## Movement and precise remaining gap

**Previous:** one selector star with arbitrary support shared a point defect;
the complete-tree constant was 4.

**New:** an arbitrary number of selector centres with arbitrary bilinear
overlap share the same point defect, with complete-tree constant \(25/4\).
No constant grows with the number of centres or rank.

**Still unpaid:** the proof has one point-defect cylinder. Two or more defect
cylinders create several exceptional Fourier layers whose principal upper
filters may intersect; a general nonflat shared core has no such layer
formula. The bound also uses the root special-block influence, not only the
directions actually queried by a pruned tree. These are the next universal
obligations. Full FEI remains OPEN.

## Sources and routing

- Current control revision: `FULL-FEI-ONLY-20261012`, revision 2026-10-12.1,
  source commit `40210272c19f43fed84f6a67653f9a04b0e11e28`.
- B05 compact contract: `reports/fei-2026-10-11/assignments/B05.json`.
- Predecessor shared-star package:
  `20261013T084137Z-fleet01-B05-star-defect-shared-a023`, canonical package
  commit `224c35caa8ea6dca47f3ac8be1af5797e52fd17b`, independently unreviewed.
- Exact disjoint tensor additivity and \(U\le H\) are used only at their
  standard scopes. No external literature novelty claim is made.

Route to A087/A094 for independent proof review and to B01/B18/B20 as a
new restriction-stable GU/FEI class. The next B05 move is two point-defect
cylinders: derive the exceptional-layer intersection law and test whether its
entropy excess remains bounded by nonreused source influence.
