# STRAT21: T104 split 5+5 (two connected five-vertex carriers), with isolates and then with arbitrary lower components, every N >= 10; the last open class of the disconnected D=2 statement with components of at most five vertices

Context:
- Read-only, do not edit: ../STRAT20/ (RESULT.md in full; setup55.py and setup55_checks.json, which already carry the
  separate K_u concavity to 5+5 including fixed lower trace, the moment bounds M0=(8-tau)/2, 0<=tau<=6, h=8/5-d,
  0<=B<=d<=3/5, the first k = 8 (N=10), nontrivial lowers first at k=10 (N=12) with cap S=k-9, the six endpoint choices per
  side (star5, path5, fork5, rank<=2 A5 at scale zero or maximum, the rank-three zero-edge endpoint covering twelve
  supports) and the 36 ordered / 21 unordered endpoint-pair types, and a positive K5+K5 fixture; transfer45.py, tree45.py,
  lower45.py, symbolic45.py, audit45.py, symmetric45.py as the 4+5 pattern; inherited19/ with the 3+5, 4+4 and 2+5
  machinery and STRAT17/16's five-part machinery: the 252 K_u coefficient matrices, the rank-two / rank-three extreme
  classification, padding monotonicity, the exact rational SOS certificates). Copy into this folder whatever you reuse;
  replay must not depend on files outside this folder except by byte-identical copies whose hashes you record.
- Already covered: disconnected extremes of either part reduce to proved smaller split classes (4+5, 3+5, 4+4, 2+5 and
  smaller) with isolates or arbitrary lowers (STRAT16-20). OPEN: the connected 5+5 endpoint-pair types and the maximal
  lower-trace endpoint.
- Hint from 3+5 and 4+5: a rank<=3 five-part (tau5<=2, B5<=d5<=3/10) transferred from the proved 2+5 theorem by comparing
  functionals at shifted k with B<=d, which cancels that part's trace-square and Y terms exactly; tree pairs closed by
  positive-coefficient numerators in the fluxes and z, with k smallest hardest by the affine inverse-padding derivative.
  Try a transfer from the proved 4+5 theorem (or 2+5) for every pair with at least one rank<=3 side before new SOS work;
  the tree-tree pairs (star5, path5, fork5 on both sides: six unordered pairs) are the expected hard core.

Task:
1. For each connected endpoint-pair family of 5+5 with isolates, prove T >= 0 for every N >= 10 and N -> infinity, with
   exact rational certificates in positive parameters and k = 8+z, z >= 0 (concavity in scale, padding monotonicity making
   the smallest k hardest, exact SOS, positive-coefficient or Bernstein certificates with a recorded margin). Name the
   equality set (expect only the two-equal-edges limit; record the margin at K5+K5 and at the equal-flux tree pairs).
2. Then lower components: STRAT17's trace interpolation with S = k-9, prove the maximal-trace endpoint nonnegative,
   reusing the step-1 margins without spending them where possible. Check K5+K5 at maximal lower trace first.
3. If T < 0 at a feasible rational point for an integer N >= 10, that is a COUNTEREXAMPLE to T104: report it with an exact
   replay and stop.
4. Write replay_all.py replaying every new certificate exactly (SymPy rationals / Fraction), run it, record time and peak
   memory, and hash every proof input in replay_summary.json.
5. State exactly what is proved and what remains of the disconnected D = 2 statement with components of at most five
   vertices, and of T104 beyond it (actual top multiplicity D>2 outside the selected-projector closure, components of six
   or more vertices).

Rules: label every statement PROVED (exact replay script named), NUMERICAL, or OPEN. An LP or float search may find
candidates; no PROVED statement trusts floats. 2 worker processes at most and peak memory under 1.5 GB in total (this Mac is
shared; use sparse or block ansatz first and a memory guard on every solver call). Disk is nearly full: outputs under
500 MB, no large caches. Append to LOG.md after each step and keep RESULT.md current. Do not edit anything under ../STRAT20,
../STRAT19, ../STRAT18, ../STRAT17, ../STRAT16 or ../STRAT15. No subagents. Normal speed only.
Coordination: the parent agent an agent holds the mesh claim for this workspace (topic:t104-strat21-mini1-workspace);
you do not need to write the mesh database, and a sandbox refusal to write it is not a reason to stop.
