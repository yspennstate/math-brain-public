# STRAT18: T104 split 4+4 (two connected four-vertex top carriers), with isolates and then with arbitrary lower components, every N >= 8; then split 3+5 if time remains

Context:
- Read-only, do not edit: ../STRAT17/ (RESULT.md in full; split44_setup.py, the fixed-vector 4+4 frame: both unit top vectors
  u, v fixed, T* separately concave on K_u x K_v by the inherited four-part certificate, each block reduced to its two trees,
  rank-at-most-two A4 boundaries, or disconnected extremes; first padding size N = 8, k = 6+z; lower_formula.py, the exact
  trace interpolation that reduces any lower collection to lower trace 0 and its maximum; split_endpoint_certificate.py;
  inherited16/ with STRAT16's 3+4 proof, split34_*.py, prior_concavity4.py, prior_four.py, verify_sos.py,
  padding_monotonicity.py). Copy into this folder whatever you reuse; replay must not depend on files outside this folder
  except by byte-identical copies whose hashes you record.
- Already covered (STRAT17 RESULT.md): disconnected 4+4 extremes (they reduce to 3+4 or 2+4 with isolates or lowers).
  OPEN: the connected endpoint-pair families tree/tree, tree/rank-at-most-two, rank-at-most-two/rank-at-most-two.

Task:
1. For each connected endpoint-pair family of 4+4 with isolates, prove T >= 0 for every N >= 8 and N -> infinity, with
   exact rational certificates in positive parameters and k = 6+z, z >= 0 (the STRAT16 3+4 pattern: concavity in scale,
   padding monotonicity making the smallest k hardest, exact SOS or Bernstein certificates with a recorded margin).
   Name the equality set (expect only the two-equal-edges limit; check whether the balanced square or another symmetric
   4+4 configuration is an equality or near-equality point and record its margin).
2. Then lower components: apply STRAT17's trace interpolation (S = k-7 for the eight-vertex split with nontrivial lowers)
   and prove the maximal-trace endpoint nonnegative, reusing the step-1 margins without spending them where possible.
3. If 4+4 closes and time remains, set up 3+5 the same way (triangle reduced to its corners, the five-part through the
   STRAT16 K_u concavity) and say which families remain.
4. If T < 0 at a feasible rational point for an integer N >= 8, that is a COUNTEREXAMPLE to T104: report it with an exact
   replay and stop.
5. Write replay_all.py replaying every new certificate exactly (SymPy rationals / Fraction), run it, record time and peak
   memory, and hash every proof input in replay_summary.json.
6. State exactly what is proved and what remains of the disconnected D = 2 statement with components of at most five vertices.

Rules: label every statement PROVED (exact replay script named), NUMERICAL, or OPEN. An LP or float search may find
candidates; no PROVED statement trusts floats. 2 worker processes at most and peak memory under 1.5 GB in total (this Mac is
shared, about 30 percent memory free; use sparse or block ansatz first and a memory guard on every solver call). Disk is
nearly full: outputs under 500 MB, no large caches. Append to LOG.md after each step and keep RESULT.md current. Do not edit
anything under ../STRAT17, ../STRAT16 or ../STRAT15. No subagents. Normal speed only.
Coordination: the parent agent an agent holds the mesh claim for this workspace (topic:t104-strat18-mini1-workspace);
you do not need to write the mesh database, and a sandbox refusal to write it is not a reason to stop.
