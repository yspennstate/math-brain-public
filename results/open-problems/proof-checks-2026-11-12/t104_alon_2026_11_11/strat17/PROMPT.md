# STRAT17: T104 lower components for the five-vertex classes: split 2+5, split 3+4 and the five-vertex double carrier, each with extra nontrivial lower components, every N >= 7

Context:
- Read-only, do not edit: ../STRAT16/ (RESULT.md in full; lower_components.py, which closes split 2+3, 2+4, 3+3 and the
  four-vertex double carrier with arbitrary lower components by increment lemmas plus convex reductions; the 2+5 and 3+4
  isolate-only proofs: algebra.py formula (1), concavity_certificate.py, rank-two / rank-three / disconnected certificates,
  split34_*.py, verify_sos.py, padding_monotonicity.py, replay_all.py). ../STRAT16/STRAT7/ holds STRAT7 (formula (1),
  padding identities, the 4+2 split method). ../STRAT15/ is the five-vertex double carrier with isolates for every N >= 7
  (chart, exact Bernstein tooling, local_uniform.py). Copy into this folder whatever you reuse; replay must not depend on
  files outside this folder except by byte-identical copies whose hashes you record.
- What is open (../STRAT16/RESULT.md, OPEN): (a) five-vertex double carriers with any nontrivial lower component;
  (b) split 2+5 and 3+4 with additional nontrivial lower components; (c) split 3+5, 4+4, 4+5, 5+5. This run takes (b) first,
  then (a), then 4+4 if time remains.

Task:
1. State the general form of T for a top carrier (split 2+5, split 3+4, or a five-vertex double carrier) plus an arbitrary
   collection of lower components (each lower component's Laplacian has spectrum strictly below the top eigenvalue after
   normalisation; components of at most five vertices), from STRAT7 formula (1). Write the lower contribution exactly, as
   lower_components.py did (the B_lower, h, M and Y increments), and state which closures (lower eigenvalue rising to the
   top) are included.
2. Prove the increment lemma for (b): adding one lower component to a 2+5 or 3+4 configuration does not decrease T
   (or decreases it by at most a quantity the isolate-only certificate's margin absorbs). Name precisely which part of
   the STRAT16 margin you use; the isolate-only proof has equality only at two equal edges, so say how the increment
   behaves near that equality point. Reduce several lower components to one at a time, or to the worst single one, by
   an exact argument (convexity in the lower part, or a monotone padding identity like STRAT16's F'(z) <= -3I/50).
3. If the increment is not sign-definite, follow the STRAT16 convex method: fix the top vectors, prove concavity of T* in
   the lower component's matrix on its own convex set, reduce to its extreme points (lower components of at most five
   vertices: edges, paths, stars, triangles, the rank <= 2 families), and certify each family with exact rational
   polynomials in positive parameters and k = 5+z, z >= 0, including z -> infinity.
4. Then (a): the five-vertex double carrier plus lower components. STRAT15 proved it with isolates through a chart with
   9,370 boxes; do NOT redo that cover. Look for an increment lemma that reuses STRAT15's statement as a black box (the
   lower contribution as a perturbation of the padded functional). If the only route is a new cover, say so, size it,
   and stop on (a).
5. Equality: name the equality set in each closed class (expect none beyond the two-equal-edges limit).
6. If T < 0 at a feasible rational point for an integer N >= 7, that is a COUNTEREXAMPLE to T104: report it with an exact
   replay and stop.
7. Write replay_all.py replaying every new certificate in exact arithmetic (SymPy rationals / Fraction), run it, record
   the time and peak memory, and record the hashes of every proof input in replay_summary.json.
8. If (b) and (a) close and time remains, set up 4+4 with isolates the STRAT16 way (both four-vertex top vectors fixed).
9. State exactly what is proved and what remains of the disconnected D = 2 statement with components of at most five vertices.

Rules: label every statement PROVED (exact replay script named), NUMERICAL, or OPEN. An LP or float search may find
candidates; no PROVED statement trusts floats. 2 worker processes at most and peak memory under 1.5 GB in total (this Mac
is shared and has about 27 percent memory free; STRAT16 breached its limit with dense SOS attempts of 3.3 GB, so use the
sparse or block ansatz first and put a memory guard on every solver call). Disk is 92 percent full: outputs under 500 MB,
no large caches. Append to LOG.md after each step and keep RESULT.md current. Do not edit anything under ../STRAT16 or
../STRAT15. No subagents. Normal speed only.
