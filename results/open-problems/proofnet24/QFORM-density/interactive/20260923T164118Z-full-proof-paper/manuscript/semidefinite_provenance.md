# Semidefinite chapter: source provenance and verification

This note is editorial provenance, not part of the mathematical exposition.
The LaTeX chapter makes no claim of literature novelty.

## Sources

- Repository yspennstate/math-open-problems, master:
  proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/semidefinite/REPORT.md.
  Retrieved blob SHA efbae86d6eee22ae94c3d3f7b9792e77100d562d.
  Source for the arbitrary-rank semidefinite theorem, Gram partition,
  ridge marginals, three-event argument, and absolute-spectral-diagonal
  indefinite extension.
- Same record, low_rank_plus_diagonal/REPORT.md,
  blob SHA a921dd7c0698099dadd46bb3f949a23e2bd4b984.
  Source for the separated-nonzero-spectrum threshold argument.
- Same record, audit/REPORT.md,
  blob SHA 977dfa33c65ea2e666a6668e2753a143e8e24f80.
  Used to ensure no pointwise characteristic-function bound or
  outside-range one-sheet argument entered the chapter.

## Central dependencies

The chapter uses the root manuscript labels four:lp and four:volume.
Required Fourier normalization:

    integral |psi(u)|^p du <= 4 pi/sqrt(p), p >= 2.
    |phi_Q(t)|^2 <= exp(k/2) (2 pi)^k |t|^(-k) Z_k^(-1/2)

The second bound assumes a disjoint crossing block with all row
k-volume marginals <= 1/2. All other steps are proved in this chapter.
The spread-frame argument also cites geometric Brascamp--Lieb with keys
BL1976 and Lieb1990. The integrated Fourier inequality follows from the
sharp Hausdorff--Young inequality, including complex input functions.

## Corrections and complete details

- Quantifiers allow every rank, dimension, arbitrary linear and constant
  terms, and eigenvalues below the third of arbitrary size.
- Density bounds are essential bounds. Square-root profiles are formulated
  as measure domination, proving absolute continuity without pointwise
  regularity assumptions.
- Positive-pivot spectral preservation uses a variational subspace proof,
  including singular A.
- The marginal formula follows from a determinant generating function.
  The ridge comparison explicitly handles singular Gram matrices.
- Both Gram second moments and all union-bound probabilities are shown.
- The indefinite threshold uses exact q=23/80 and 4/q^2=25600/529,
  avoiding downward decimal rounding in the source.
- The indefinite density constant is 480 sqrt(e)/23 = 34.408096...;
  the theorem safely states <35, not 34.4.
- Gaussian damping justifies Fresnel inversion for arbitrary rough laws.
- The outside-range one-sheet claim is not used.

## Modest additional deduction

The separated-spectrum theorem improves the source constant304 to130
using the existing threshold argument and the sharper composition bound
proved earlier in the chapter. See research_work/semidefinite_new.md.
This is a constant refinement under the stronger hypothesis that every
nonzero eigenvalue has modulus at least theta and has one sign. It does
not improve the main 17100/lambda_3 statement or settle the indefinite target.

## Verification

- Main PSD constant, using exact K1=4 sqrt(128) and
  K2=4 sqrt(600) K1: 17061.142909583185 <17100.
- Separated-spectrum constant:
  3 sqrt(2) sqrt(120(3+log120)) =129.6957291679615 <130.
- Indefinite three-event failure ratios for k=1,2,3:
  0.9876399593, 0.9821466079, 0.9934393417.
- The full proof chain was independently re-derived during writing.
- The chapter compiles under article with amsmath, amssymb, amsthm,
  mathtools, natbib, and temporary central-lemma stubs.
The root manuscript must resolve those two central references.

## Exact definite rank three

Theorem sd:rank-three adds the complete proof of the range-affine
constant 3e and improves the recorded arbitrary-affine constant82 to58.
The source records are:

- interactive/20260922T231000Z-semidefinite-and-hub-reduction/rank_three_geometry/REPORT.md,
  blob e99b63c3334a0abb24b66460081a49ce4664ad01, Theorem3.1.
- interactive/20260922T225732Z-claude-synthesis/REPORT.md,
  blob 6a5748aa1e93033b78d2c07d81e1468068ea4662, Section6,
  which reproduces the exact-rank-three range-affine constant3e.

The additional dependencies are four:diffuse, four:projection,
geom:definite, and thm:rank-two-affine. The latter has been sharpened
in the manuscript to alpha2<=32sqrt2<46 using the independently checked
rank-one Gaussian-smoothing bound8 in rt:rank-one.
In the heavy-leverage case, a>1/2, the Schur complement has rank two
and both nonzero eigenvalues>=1. The inverse-half-moment bound with
V=20 gives

    sqrt2 [20+46(3+2log20)/20] =57.53072879613092 <58.

The range-affine theorem keeps the one-sided square profile. Projection
cap2 and the definite-pair bound give p_T<=2pi; the one-sided bathtub
integral is2sqrt(2pi), hence the heavy branch is4sqrt(pi)<3e.
The diffuse branch is3e from the sharp Fourier theorem.

The full combined manuscript compiled successfully in a separate
temporary output directory after these additions, with no overfull
boxes. Root-level bibliography and final reference resolution remain
part of the final assembly.
