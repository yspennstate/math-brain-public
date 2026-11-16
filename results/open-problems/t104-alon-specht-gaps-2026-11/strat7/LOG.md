NUMERICAL / PROVED research log

2026-11-13 approximately 03:26 +04. Task received: prove T >= 0 for every disconnected
weighted graph on N = 6 vertices with D = 2, then extend if possible.
Read PREVIOUS_RESULT_STRAT4.md, the notation in PREVIOUS_RESULT.md, and terms.py.
All work stays in this folder; no network or language-model workers are used.
Global brain/mesh/checklist commands are omitted because they write outside this folder.

NUMERICAL: Embedding the previous rational four-vertex sparse family at l=32/5
into six vertices gives T about 0.02830994 and quotient about 0.05840684.
This is a discovery check only.

PROVED (derivation to be audited): for any fixed nonzero graph padded to N vertices,
put B = sum_ij Pi_ij (lambda I-L)_ij^2 and h = sum_i Pi_ii L_ii.
Then X1 and S5 do not depend on N, X2=2N B/(N-2), and
X3=(1-lambda)[D(N-1)(N-4)lambda-2D(N-2)+2N h]/(N-2)^2.
The identities use Pi 1=0 and Pi(lambda I-L)=0.

2026-11-13 03:42 +04.
NUMERICAL: explore.py sampled every relevant partition and both spectral origins.
optimize.py then ran 80 SLSQP starts per nontrivial mode. No negative T found.
The least retained quotient is about 0.05719818 in 4+1+1 (also approached
in 4+2 when the inactive edge tends to zero). Raw optimizer records allow
weight residuals around 1e-11; these will be polished before reporting.

PROVED: four_vertex_certificate.py proves the four-vertex double carrier,
with or without an inactive edge, for every N>=6 after padding with isolates.
It uses separate strict concavity in the internal spectral gap g and inactive
edge eigenvalue t, then four endpoint coefficient checks on the ordered cone.
Five negative coefficients in one endpoint disappear on six ordered subcones.

PROVED: triangle_certificate.py proves the two-triangle split case (and its
triangle + edge + isolate boundary), padded to every N>=6. Four endpoint
polynomials have nonnegative rational coefficients.

PROVED: tree_certificate.py proves a weighted four-vertex tree plus a tied
top edge, with arbitrary added isolates. Its star and path numerators have
126 and 108 nonnegative coefficients respectively.

PROVED: concavity_certificate.py proves concavity in the four-vertex Laplacian
with its selected unit top eigenvector fixed. One coefficient matrix failed
on the unsplit cone; all 84 matrices pass on each of six ordered subcones.
split_boundary_certificate.py proves the boundary where the four-vertex
component has top multiplicity >=2 but only one of its top eigenvectors is
selected alongside the tied edge. All 84 concavity, 84 zero-gap endpoint,
and 198 maximal-gap endpoint coefficient matrices are positive semidefinite
by exact principal minors. This closes the 4+2 split case by extreme points.

NUMERICAL: moment_lp.py tried a relaxation of the five-vertex carrier using
fourth moments, cubic Gram bounds, and edge-weight moment inequalities. The
relaxation has negative lower bounds in large parts of the feasible range;
this is failure of that relaxation, not a counterexample. The 5+1 structure
remains unresolved at this checkpoint.

2026-11-13 03:57 +04.
PROVED: RESULT.md now contains the component derivations, the exact certificate
construction, the fixed-projector extreme-point proof for 4+2 split, the
equality classification in all covered structures, and the precise remainder.
The only unresolved N=6 structure is 5+1, outside the additional region below.

PROVED: scale_certificate.py covers a five-vertex double carrier when its
larger normalized internal gap a<=11/25, padded to any N>=6. It uses a
16-vertex elementary moment polytope, a cubic square completion, Bernstein
coefficients in a, exact quadratic minima in b/a, and nonnegative coefficients
in N-6. The uniform coefficient margin is 94/3125 after multiplying by (N-2)^2.

PROVED: The combined replay ran every exact script successfully, sequentially;
cumulative peak RSS was 78.9 MiB, below 1 GB. Scalar and matrix endpoint
certificates now also check the strict coefficients needed for equality.
exact_audit.py has independent rational matrix checks at several padding sizes.

NUMERICAL: All polished retained candidates have nonnegative computed weights
and D=2 to the terms.py tolerance. The least repaired quotient is
0.0571981925501984 in 4+1+1. No negative graph was found. The full 5+1
proof, full N=6 equality classification, and the unrestricted all-N extension
remain unfinished; this is explicitly stated in RESULT.md.

PROVED: Final audit rerun also passes after adding independent checks of the
full 5+1 moment formula, the selected-projector boundary matrix, and the
concavity quadratic part. All seven replay stages pass; final cumulative
peak RSS is 88.7 MiB. No claim of a full proof is made.
