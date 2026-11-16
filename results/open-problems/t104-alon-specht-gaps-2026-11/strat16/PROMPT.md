# STRAT16: T104 split simple top carrier 2+5 (an edge and a connected five-vertex component, each carrying one top eigenvalue) plus isolated vertices, every N >= 7

Context:
- STRAT7/ (copied here): the disconnected N = 6 classes. Read STRAT7/RESULT.md in full, especially formula (1) (the functional T,
  the padding identities X2, X3 in k = N-2 or k = 4+u), the 3+3 / 3+2+1 triangle-corner argument (4), and "The 4+2 split case":
  fix the selected top vector u of the larger component, the convex set
      K_u = {A: symmetric PSD, entrywise >= 0, A1 = 1, Au = 0},
  concavity of T* on K_u (concavity_certificate.py, quadratic form (5) on the variation space spanned by K V K^T), reduction to
  extreme points (rank <= 2 boundary (6) via split_boundary_certificate.py; connected rank-three extreme points are trees, handled
  by tree_certificate.py), and the equality analysis. STRAT7's padding remark: a fixed-graph theorem in the variable k = 4+u,
  u >= 0, holds for every N.
- Read-only, do not copy or edit: ../STRAT15/ (the 5+1 class for every N >= 7: the five-vertex chart, exact_bernstein.py,
  local_uniform.py, replay_all.py, RESULT.md) and ../STRAT15/STRAT14/ (connected n = 5, D = 2). Use them for the five-vertex
  parametrisation and for exact Bernstein / Farkas tooling.
- What is still open (STRAT15/RESULT.md line 124): split simple top carriers 2+5, 3+4, 3+5, 4+4, 4+5, 5+5; double carriers with
  nontrivial lower components; 2+3, 2+4, 3+3 splits with an extra nontrivial lower component. This run takes 2+5 with isolates.

Task:
1. Set up the 2+5 split class: G = edge (weight scaled so its top eigenvalue equals the top eigenvalue of the five-vertex
   component C5 after normalisation) + connected C5 whose top eigenvalue is simple and equals the edge's + N-7 isolated vertices,
   D = 2, every N >= 7 (k = N-2 >= 5, write k = 5+u, u >= 0, and include u -> infinity). Write T for this class from formula (1)
   exactly, as STRAT7 did for 4+2, and state which boundary graphs (top multiplicity rising above two) are included.
2. Follow the 4+2 split method one size up: fix the unit zero-sum top vector u of C5, the convex set K_u of 5x5 matrices, and prove
   T* concave on K_u for every N >= 7 by an exact certificate on the variation space {E: E1 = Eu = 0} (dimension 6 symmetric 3x3 V,
   with an explicit rational spanning matrix K on ordered cones of u, as STRAT7 did with six ordered subcones). If concavity fails
   somewhere, say where (exact point) and switch method on that part (e.g. a finer cone split, or the STRAT15 chart).
3. Classify the extreme points of K_u for n = 5: the rank <= 2 boundary (J5/5 + g vv^T type), and the higher-rank extreme points
   (count free directions as STRAT7 did; connected extreme points of rank r have few edges: list the possible trees and sparse
   graphs on five vertices with a positive top vector u). Certify T > 0 (or >= 0 with the equality set named) on each family with
   exact rational polynomials in positive parameters and k = 5+u, nonnegative coefficients after the needed substitutions.
4. Disconnected extreme points reduce to classes already proved (name the STRAT7 or STRAT15 statement each one uses) or to S5 = 0.
5. Equality: determine the equality set in this class (expect only the two-edge and balanced-triangle limits; prove it or say OPEN).
6. If T < 0 at a feasible rational point for an integer N >= 7, that is a COUNTEREXAMPLE to T104: report it with an exact replay
   and stop.
7. Write replay_all.py replaying every new certificate in exact arithmetic (SymPy rationals / Fraction), run it, record the time.
8. If 2+5 closes and time remains, do 3+4 the same way (fix the top vector of the four-vertex part; the triangle side as in (4)).
9. State exactly what is proved and what remains of the disconnected D = 2 statement with components of at most five vertices.

Rules: label every statement PROVED (exact replay script named), NUMERICAL, or OPEN. An LP or float search may find candidates;
no PROVED statement trusts floats. 4 worker processes at most, peak memory under 2.5 GB, this Mac is shared and its disk is 92%
full: keep outputs under 2 GB, no large caches. Append to LOG.md after each step and keep RESULT.md current. Do not edit STRAT7/
(copy what you reuse) or anything under ../STRAT15. Normal speed only.
