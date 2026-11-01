# Provenance of the supplementary chapter

The manuscript chapter is `fleet_supplement.tex`. All source paths below are relative to `source_snapshot/fleet` and to the repository directory `proofnet24/QFORM-density/fleet-2026-09-22` at checkpoint `36d0dc0c4ac0910e8d84ae64d443136df86242d5`. Exact links, Git blob IDs and SHA-256 digests are in `fleet_catalogue.json`.

The chapter is an anonymous mathematical exposition. This separate record identifies the working sources and verification scope; it does not assign manuscript authorship or make a priority claim.

## Retained statements and proof changes

| Manuscript label | Source | Verification and changes |
|---|---|---|
| `supp:negative-moment` | Elementary layer cake; also `fleet02/B06/b06-20260923T152436Z-899a8d07c487/REPORT.md`, Lemma 1.1 for d=2,p=1 | Full elementary proof written in arbitrary dimension. No new-literature claim. |
| `supp:null-bank` | `fleet02/B06/b06-20260923T152436Z-899a8d07c487/REPORT.md`, Theorem 2.1 | Full conditional linear-density proof read and reproduced. Uses sharp LPP projection constants in dimensions one and two. Keeps arbitrary crossing rank and arbitrary measurable function on the other bank. |
| `supp:rank-one-pair` | Receiver stated in `fleet03/B01/fleet03-B01-20260923T153212Z-auto11/REPORT.md`, Section 1.2; aggregate consequence in its Theorem 2 | A complete independent proof is supplied from square coarea and two scalar bathtub/negative-moment estimates. The one-sided square kernel improves the recorded constant to `4*2^(1/4)`. Arbitrary complementary curvature is retained. |
| `supp:singular-pair-volume` | Same fleet03/B01 report, Sections 1–2 | The inequality `||w||^4 >= sum_(i!=j)w_i²w_j²` gives the aggregate consequence. The quantity W is explicitly defined rather than importing unexplained packet notation. |
| `supp:spill` | `fleet03/B12/20260923T144737Z-qform-eigenvalue-r35/REPORT.md`, Theorem 1.1 and proof | Complete matrix proof reproduced from `(A²)_HH=C²+BB^T`, spectral truncation and positive rank interlacing. |
| `supp:pair-extraction` | `fleet02/B12/20260923T145451Z-fleet02-B12-QFORM-r36/REPORT.md`, Lemma 2.1 | Complete proof checked. Uses the exact Pluecker sum one, determinant/norm relation in a 2x2 block, and norm-tail erosion. |
| `supp:six-carrier` | Same fleet02/B12 report, Theorem 4.1 | Three exhaustive cases reproduced. The manuscript's improved determinant-only logarithmic pair theorem replaces the older pair constant. Monotonicity in sqrt(D) is proved explicitly. The carrier premise implies six globally large singular values and is not manufactured from the three-eigenvalue conjecture. |
| `supp:anticommutator` | `fleet01/B12/20260923T151555Z-fleet01-B12-QFORM-auto11/REPORT.md`, Theorem 2.1 and Corollaries 3.1–3.3 | Complete square expansion and Loewner-order argument reproduced. Orthogonal spectral and anticommuting additions have zero loss at this certificate level. |
| `supp:rank-reserve`, `supp:adaptive-rank` | `fleet01/B12/20260923T162217Z-fleet01-B12-QFORM-auto11/REPORT.md`, Theorem 1 and Corollary 2 | Source bound valid but its purported necessity of `2 rank(S)` loss is false. A stronger direct rectangular singular-value proof loses only `rank(SP_H)`; full subspace-intersection proof and adaptive threshold consequence included. |
| `supp:signed-reserve` | `fleet03/B12/20260923T154231Z-qform-eigenvalue-r36/REPORT.md`, Theorem 3.1 | Complete positive/negative tail splitting and rank-interlacing proof checked and reproduced. Favorable-sign additions are free on the corresponding signed side. |
| `supp:schur-protection` | `fleet04/B12/20260923T081758Z-fleet04-B12-complementary-schur-shield-r4/REPORT.md`, Theorem 4.1 | Full complementary Schur factorization checked. Manuscript supplies shear singular-value derivation and does not require updated Schur block invertible. |
| `supp:codimension-one` | `fleet02/B12/fleet02-B12-20260922T1251Z-qform-additional-eigenvalue/REPORT.md` | The source's larger constant is unnecessary after the newer finite-core theorem. Interlacing into an arbitrary original four-coordinate block gives `2 sqrt(24 pi)/s`. |
| `supp:interpolation-obstruction` | `fleet04/B19/20260923T071203Z-fleet04-B19-QFORM-r3/REPORT.md`, Theorem 3.1 | Full spike example checked and reproduced, correcting source text-encoding artifacts. This is a counterexample to an analytic implication, not to the conjecture. |
| `supp:moving-ridge` | `fleet04/B19/20260923T151700Z-fleet04-B19-QFORM-r4/REPORT.md`, Section 2 | Full construction checked. Manuscript replaces the source's asymptotic volume statement with elementary explicit bounds and retains the exact matrix spectrum. Independence only of the outer hub is explicitly distinguished from coordinatewise independence. |

## Classical inputs

- LPP2016 supplies the sharp low-dimensional projection constants in the null-bank and random-slope receivers. The proof does not assume independence of projected coordinates.
- Negative-moment, rank-interlacing, Loewner-order, square coarea, and finite-dimensional shear calculations are supplied directly in the text.
- Density conclusions for the coordinate carrier and complementary Schur estimates use `cor:finite-core`, `geom:definite`, `geom:fullpair`, and `four:d-cases` from the manuscript, with all their actual hypotheses checked in the displayed proofs.
- BGKS2024 is cited only as closely related independent-block conditioning methodology, not as a theorem proving the shared-coordinate cases.

## Material exclusions

The frozen-slice Fourier bound in fleet02/B05 13:04 and its affine extension in fleet04/B14 14:14 only provide interval concentration. Their asserted full rough-hub consequence requires a Borel-set profile not established by those arguments. They are not copied as complete universal heavy-null theorems. The valid slice estimates remain in the hub chapter.

Specialized structural gates and numerical witnesses outside this chapter are indexed in `FLEET_COVERAGE_AUDIT.md`. That catalogue is explicit about which source-specific case analyses have not been independently verified. The manuscript itself remains a collection of proved partial results and stated conditional reductions.

## Verification

All added proofs were checked algebraically and for their measure-theoretic scope. The final local static check found no undefined references or citation keys and no duplicate labels across the then-current manuscript. The parent manuscript build performs the combined LaTeX compilation and PDF review. This provenance record does not assert an independent end-to-end proof of the unrestricted conjecture.
