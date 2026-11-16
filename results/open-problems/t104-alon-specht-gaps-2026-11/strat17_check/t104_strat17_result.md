# T104 (Alon Conj. 1.5): the five-vertex classes with arbitrary lower components — STRAT17 result

13 Nov 2026. an agent. Run on Mac mini 1, ~/agent_run/STRAT17 (Codex, normal speed, exited after 17 min of run 2).

## What is proved

PROVED (STRAT17/replay_all.py, 24 exact stages, all PASS; replayed by me from a frozen copy):
1. Split 2+5 and split 3+4 with arbitrary lower components (any number, any size, each with spectrum strictly
   below the common top eigenvalue): T >= 0 for every N >= 7 and in the limit N -> infinity; connected simple top
   carriers give T > 0; any positive lower trace gives T > 0.
2. Five-vertex double carriers with arbitrary lower components, every N >= 7 and infinity, using the STRAT15
   theorem (isolates only) as a black-box premise at zero lower trace.
3. Equality on the closures: two equal edges plus isolates; the double-carrier closure also keeps the balanced
   triangle plus isolates.

Hence, together with STRAT16, every disconnected D = 2 configuration whose top carriers are split 2+2, 2+3, 2+4,
2+5, 3+3, 3+4, or a double carrier on at most five vertices, is closed with arbitrary lower components.

Method. Lower blocks change only M (by s/2, s = lower trace) and add 2 sum mu(1-mu) >= 0. The increment is concave in
the whole lower matrix, so after dropping the spectral term an exact trace interpolation
F_k(s) = (1-s/S)F_k(0) + (s/S)F_k(S) + s(S-s)/k reduces every lower collection at once to s = 0 and s = S
(S = k-6 for the seven-vertex splits, k-4 for the double carrier). Adding a lower edge can lower T* (exact fixtures in
matrix_audit.py), so a one-at-a-time increment argument would be wrong; the endpoint comparison avoids it.
- Splits: at s = k-6, twelve exact Bernstein controls give a 3/10 surplus over the k = 5 baseline; STRAT16's own
  margins are kept, not spent.
- Double carrier, gap trace tau >= 1: the increment coefficient is 2(tau-1)+(h-1) >= 0 (h >= 1 by the eigenvector
  energy identity).
- Double carrier, tau <= 1: with S = a uu^T + b vv^T on the non-top space, two weighted Cauchy inequalities
  (weight sum M0, first moments 1-a and 2-tau) give J >= L/M0, and h >= 8/5 - 3tau/5; the endpoint is
  >= N(tau,a)/(125(4-tau)) with N >= 50/27, so a margin of at least 1/270, k = 5 hardest.

## My independent checks (all PASS)

1. my_replay (strat17_myreplay3.out): replay_all.py rerun by me from a frozen copy taken after Codex exited
   (strat17_freeze2.sha256, 52 files): 24/24 PASS, 58.7 s, 85 MB. Live files byte-identical to the freeze.
   (An earlier freeze taken mid-run failed on a lower_formula.py assert comparing expanded with unexpanded form;
   Codex had already rewritten it. That freeze is void.)
2. my_lower_search.py (float, own code from RESULT.md): 2+5 with lower trace s in [0,k-6], spectral term dropped,
   k = 7..1e6: no negative T; the only value near 0 is the known equality point.
3. my_double_lower_search.py (float, own code from RESULT.md): five-double with s in [0,k-4], k = 5..1e6: no negative
   T; the tight spot is the normalized K5 top at maximal lower trace (T = 0.081, 0.059, 0.045 at k = 5, 6, 7).
4. Hand audit of double_small_gap.py: the script checks the polynomial identities; I re-derived by hand the
   graph-to-scalar steps stated in RESULT.md (moments 1-a and 2-tau because u, v span the non-top space; weight sum
   M0 = tr C/2; the h formula; F >= tau/5), the sign arguments on both t ranges, and monotonicity in z = 1/k.

## Caveats

- The double-carrier result rests on STRAT15 (five-vertex double carrier with isolates, 9,370-box chart) as a
  premise; its cover was not rerun here.
- The identities Y = 4e - 2J and the B >= 0 step are checked in double_small_gap_audit.py at exact fixtures and by
  the general matrix algebra in RESULT.md; I checked them by hand, not by a separate script.

## What is NOT proved (OPEN)

Split 3+5, 4+4, 4+5, 5+5, with isolates or with lower components. Codex set up the 4+4 convex frame (both four-vertex
top vectors fixed) but proved nothing there yet. So the full disconnected D = 2 statement with components of at most
five vertices is still OPEN.

## Files

Tarball STRAT17_final.tgz (395,021 bytes, sha256 365f57a75a19cdfaaed1aaa6e74147adadfd854dcde962fb6c10298481c93a8f)
on Mac mini 1 at ~/agent_run/; pushed under strat17/ with my checks under strat17_check/.
