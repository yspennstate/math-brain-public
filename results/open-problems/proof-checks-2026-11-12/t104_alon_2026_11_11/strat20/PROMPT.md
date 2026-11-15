# STRAT20: T104 split 4+5 (a connected four-vertex carrier and a connected five-vertex carrier), with isolates and then with arbitrary lower components, every N >= 9; then set up 5+5 if time remains

Context:
- Read-only, do not edit: ../STRAT19/ (RESULT.md in full; setup45.py and setup45_checks.json, which already carry the
  separate K_u concavity to 4+5 including fixed lower trace, the moment bounds M0=(7-tau)/2, h=31/20-d, 0<=B<=d<=11/20,
  the lower-trace cap S=k-8 at k>=9, and the 24 connected endpoint types; transfer35.py, tree35.py, lower35.py,
  symbolic35.py, audit35.py, symmetric35.py as the 3+5 pattern; inherited18/ with STRAT18's 4+4 four-part machinery and
  STRAT17/16's five-part machinery: the 252 K_u coefficient matrices, the rank-two / rank-three extreme classification,
  padding monotonicity, the exact rational SOS certificates). Copy into this folder whatever you reuse; replay must not
  depend on files outside this folder except by byte-identical copies whose hashes you record.
- Already covered: disconnected extremes of either part reduce to proved smaller split classes (3+5, 4+4, 2+5, 3+4 and
  smaller) with isolates or arbitrary lowers (STRAT16-19). OPEN: the 24 connected 4+5 endpoint types (four-side star4,
  path4, rank<=2 A4 at scale zero or maximum; five-side star5, path5, fork5, rank<=2 A5 at scale zero or maximum, and the
  rank-three zero-edge scale endpoint), and the maximal lower-trace endpoint.
- Hint from 3+5: the rank<=3 five-part transferred from the proved 2+5 theorem by comparing functionals at shifted k with
  B<=d; try the same transfer from the proved 3+5 (or 4+4) theorem before building new SOS certificates.

Task:
1. For each connected endpoint-pair family of 4+5 with isolates, prove T >= 0 for every N >= 9 and N -> infinity, with
   exact rational certificates in positive parameters and k = 7+z, z >= 0 (concavity in scale, padding monotonicity making
   the smallest k hardest, exact SOS, positive-coefficient or Bernstein certificates with a recorded margin). Name the
   equality set (expect only the two-equal-edges limit; record the margin at K4+K5 and at the equal-flux tree pairs).
2. Then lower components: STRAT17's trace interpolation with S = k-8, prove the maximal-trace endpoint nonnegative,
   reusing the step-1 margins without spending them where possible. Check K4+K5 at maximal lower trace first.
3. If 4+5 closes and time remains, set up 5+5 the same way and say which families remain.
4. If T < 0 at a feasible rational point for an integer N >= 9, that is a COUNTEREXAMPLE to T104: report it with an exact
   replay and stop.
5. Write replay_all.py replaying every new certificate exactly (SymPy rationals / Fraction), run it, record time and peak
   memory, and hash every proof input in replay_summary.json.
6. State exactly what is proved and what remains of the disconnected D = 2 statement with components of at most five vertices.

Rules: label every statement PROVED (exact replay script named), NUMERICAL, or OPEN. An LP or float search may find
candidates; no PROVED statement trusts floats. 2 worker processes at most and peak memory under 1.5 GB in total (this Mac is
shared, about 27 percent memory free; use sparse or block ansatz first and a memory guard on every solver call). Disk is
nearly full: outputs under 500 MB, no large caches. Append to LOG.md after each step and keep RESULT.md current. Do not edit
anything under ../STRAT19, ../STRAT18, ../STRAT17, ../STRAT16 or ../STRAT15. No subagents. Normal speed only.
Coordination: the parent agent an agent holds the mesh claim for this workspace (topic:t104-strat20-mini1-workspace);
you do not need to write the mesh database, and a sandbox refusal to write it is not a reason to stop.
