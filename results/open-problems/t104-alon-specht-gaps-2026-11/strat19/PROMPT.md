# STRAT19: T104 split 3+5 (a connected three-vertex carrier and a connected five-vertex carrier), with isolates and then with arbitrary lower components, every N >= 8; then set up 4+5 if time remains

Context:
- Read-only, do not edit: ../STRAT18/ (RESULT.md in full; setup35.py, which already reduces the triangle part to its corners
  and transfers the five-part K_u concavity to 3+5 including fixed lower trace; algebra44.py, tree44.py, boundary44.py,
  padding44.py, lower44.py, symbolic44.py, audit44.py as the 4+4 pattern; inherited17/ with STRAT17's lower_formula.py
  trace interpolation and STRAT16's 2+5 machinery: the 252 K_u coefficient matrices, the rank-two / rank-three extreme
  classification of the five-part, padding monotonicity F'(z) <= -3I/50, the exact rational SOS certificates). Copy into
  this folder whatever you reuse; replay must not depend on files outside this folder except by byte-identical copies whose
  hashes you record.
- Already covered: disconnected extremes of either part reduce to proved smaller split classes (2+5, 3+4, 2+4, 3+3 and
  smaller) with isolates or arbitrary lowers (STRAT16-18). OPEN: the connected 3+5 families, triangle corner x five-part
  extreme (rank <= 2 and rank-three five-part extremes), and the maximal lower-trace endpoint.

Task:
1. For each connected endpoint-pair family of 3+5 with isolates, prove T >= 0 for every N >= 8 and N -> infinity, with
   exact rational certificates in positive parameters and k = 6+z, z >= 0 (the STRAT16/STRAT18 pattern: concavity in scale,
   padding monotonicity making the smallest k hardest, exact SOS, PSD-coefficient or Bernstein certificates with a recorded
   margin). Name the equality set (expect only the two-equal-edges limit; record the margin at K3+K5 and at the balanced
   configurations).
2. Then lower components: apply STRAT17's trace interpolation (S = k-7 for the eight-vertex split with nontrivial lowers)
   and prove the maximal-trace endpoint nonnegative, reusing the step-1 margins without spending them where possible.
   (A float search on 4+4 found the tight spot with lowers at the two complete tops with maximal lower trace; check K3+K5
   there first.)
3. If 3+5 closes and time remains, set up 4+5 the same way and say which families remain.
4. If T < 0 at a feasible rational point for an integer N >= 8, that is a COUNTEREXAMPLE to T104: report it with an exact
   replay and stop.
5. Write replay_all.py replaying every new certificate exactly (SymPy rationals / Fraction), run it, record time and peak
   memory, and hash every proof input in replay_summary.json.
6. State exactly what is proved and what remains of the disconnected D = 2 statement with components of at most five vertices.

Rules: label every statement PROVED (exact replay script named), NUMERICAL, or OPEN. An LP or float search may find
candidates; no PROVED statement trusts floats. 2 worker processes at most and peak memory under 1.5 GB in total (this Mac is
shared, about 35 percent memory free; use sparse or block ansatz first and a memory guard on every solver call). Disk is
nearly full: outputs under 500 MB, no large caches. Append to LOG.md after each step and keep RESULT.md current. Do not edit
anything under ../STRAT18, ../STRAT17, ../STRAT16 or ../STRAT15. No subagents. Normal speed only.
Coordination: the parent agent an agent holds the mesh claim for this workspace (topic:t104-strat19-mini1-workspace);
you do not need to write the mesh database, and a sandbox refusal to write it is not a reason to stop.
