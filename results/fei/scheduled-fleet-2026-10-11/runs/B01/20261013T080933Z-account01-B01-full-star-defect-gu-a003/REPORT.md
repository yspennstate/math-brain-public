# B01 / A003 — full-star point-defect GU' class

**Run:** `20261013T080933Z-account01-B01-full-star-defect-gu-a003`  
**Primary packet:** A003 (Minimal target formulation)  
**Stable gap:** `GU-ASYMMETRY-MISMATCH`  
**Status:** `AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW`; full FEI remains OPEN.

## Result

I proved a new dimension-free GU' endpoint on an expanding,
restriction-closed class with genuine shared-variable interference.

For
\[
 d_n(x)=1-2\mathbf 1_{\{x=0\}},\qquad
 F_n(z,x)=(-1)^{z(x_1+\cdots+x_n)}d_n(x),
\]
let \(\mathcal C_*\) contain all restrictions of these functions, all
affine-quadratic phases, and arbitrary products with disjoint
affine-quadratic phases.  Then every \(f\in\mathcal C_*\) satisfies
\[
 \boxed{\ G(f):=\sum_i[U(f)-\mathbb E U(f\mid x_i)]\le8I(f)\ }.
\]
Thus GU' holds on \(\mathcal C_*\) with \((a,b)=(8,0)\).  Restriction
induction yields \(U(f)\le8I(f)\), and \(H\le2I+2U\) yields
\(H(f)\le18I(f)\).

The previous class allowed an arbitrary seed only when it was disjoint from
the quadratic factor, with a constant depending on the seed.  Here the
quadratic star and one-point defect share all data variables, yet the constant
is independent of \(n\), quadratic rank, and total dimension.

## Why the constant stays uniform

The exact nonzero squared Fourier coefficients of \(F_n\) are
\[
 1/4,1/4,(1/2-2^{1-n})^2,(1/2-2^{1-n})^2,
 \underbrace{4^{1-n},\ldots,4^{1-n}}_{2^n-2}.
\]
This gives \(U(F_n)\le H(F_n)\le4\).  At the same time every physical
coordinate—including the selector and all data coordinates—has influence
exactly \(1/2\), so \(I(F_n)=(n+1)/2\).  Since each coordinate loss is at most
the parent \(U\), \(G(F_n)\le4(n+1)=8I(F_n)\).

The two boundary families arising from selector restriction are also paid:

- the raw defect has an exact closed form for \(U_n\), yielding
  \(G(d_n)<9n2^{-n}<8I(d_n)\);
- the parity-shifted defect has \(H<3\), while every coordinate influence is
  \(1-2^{1-n}\), yielding \(G<6I\).

Restricting a data coordinate of \(F_n\) gives either \(F_{n-1}\) or a pure
affine-quadratic phase.  Therefore the class is restriction closed.  The
accepted quadratic theorem gives \(G(q)\le3I(q)\), and exact disjoint-product
additivity preserves the constant 8 after adjoining arbitrary disjoint
quadratic factors.

The complete proof is in `FULL_STAR_DEFECT_GU.md`.

## Verification

`CHECK_FULL_STAR_DEFECT_GU.py` independently checks:

- the exact full-star spectrum for \(1\le n\le10\);
- all physical influences and \(G\le8I\) on those cases;
- both boundary families for \(1\le n\le14\);
- the explicit restriction identities;
- exact numerical additivity of \(U,G,I\) over all affine-quadratic phases on
  at most three disjoint variables and full-star blocks through \(n=4\).

The finite check is corroboration, not the proof.

## Exact movement and remaining gap

**Previous:** disjoint quadratic-seed transfer with \(G(qg)\le\max\{3,a\}I+bU\)
when the seed already satisfied GU'; arbitrary fixed seeds had constants that
could grow with seed size.  No internally overlapping star/defect family had
a dimension-free GU' proof.

**New:** a shared full-star/point-defect block, all of its restrictions, and
arbitrary disjoint quadratic extensions satisfy GU' with \((a,b)=(8,0)\),
giving the explicit FEI constant 18 on this class.

**Still unpaid:** the proof uses the special spectral collapse
\(U(F_n)=O(1)\) together with \(I(F_n)=\Theta(n)\).  It does not control the
aggregate upper-set asymmetry mismatch for arbitrary changing coherent cores,
where parent \(U\) may grow and the same physical coordinates may be reused
through a hierarchy.  A universal bound with absolute \(a\) and \(b<1\)
remains OPEN.

## Sources and scope pins

- Current control revision: `FULL-FEI-ONLY-20261012`, revision 2026-10-12.1,
  source commit `40210272c19f43fed84f6a67653f9a04b0e11e28`.
- B01 contract: `reports/fei-2026-10-11/assignments/B01.json`.
- Quadratic coordinate theorem: B01 run
  `20261013T061836Z-account01-B01-all-quadratic-gu-a003`, verified receipt
  `d829fca20536446e9855c0ce13be882b9beaf11a`.
- Quadratic-seed transfer: B01 run
  `20261013T071542Z-account01-B01-quadratic-seed-transfer-a003`, canonical
  receipt `32fb7aa3ef89abb7a62bf2229966ffb387eef04f`, Brain receipt
  `bdddd59b338dd97172f19cb7cb31ee62e37b2230`.

## Review and routing

This claim is author-proved but not independently accepted.  Route the exact
class theorem and proof to A086/A094, with B19 as the natural adversarial
review stream.  Consumers should use the theorem only at its stated
restriction-closed scope; it is neither a universal GU' proof nor full FEI.

## Next mathematical move

Replace the full parity star by a rank-\(r\) star or several overlapping star
centres and determine whether a retained lower bound on physical influence
still pays the growing parent \(U\).  The first decisive test is two star
centres sharing the same point defect: either assign each upper-set mismatch
to a disjoint pivotal edge class, or construct a rigorous family in which
\(G/I\) grows with the number of reused centres.
