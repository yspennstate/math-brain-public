# T104 STRAT19: split 3+5 with arbitrary lower components (an agent audit, 13 Nov 2026)

Claim (Codex STRAT19, gpt-6.1-sol high, normal speed, Mac mini 1, 18:16-18:32 Mac time): for disconnected D=2 graphs whose
two top carriers are a connected triangle-part and a connected five-vertex part, T >= 0 for every N >= 8 and for N -> infinity,
with isolates or arbitrary lower components; equality only at two equal edges plus isolates; positive lower trace is strict.
Full statement and proof in strat19/RESULT.md (39-stage exact replay, replay_all.py).

How it closes:
- rank(A5) <= 3 five-parts: transferred from the proved 2+5 theorem at k=5 to 3+5 at k=6 (same five-part, its trace-square
  and Y moments cancel; B5 <= d5 pays the -2/15 change), extra margins 1/20 (three-path corner) and 73/675 (balanced triangle)
  on top of the inherited 1/400000. No new SOS solve.
- the three five-trees against both triangle corners: six cleared numerators with only positive coefficients in the fluxes
  and z = k-6 (858 to 5982 terms each), padding derivative makes k = 6 hardest.
- lowers: STRAT17 trace interpolation with S = k-7; F_k(k-7) >= F_6(0) + 1/4 uniformly, twelve Bernstein controls.

My checks:
1. Freeze: 132 files hashed on mini1 after Codex exited (strat19_freeze.sha256); laptop copy matches; the live tree still
   matched the freeze after my replay.
2. Replay: fresh copy, framework python 3.13, replay_all.py: 39 of 39 stages PASS, 103 s, 100 MB peak
   (strat19_myreplay.out/.time). All 87 hash fields in my replay_summary.json equal Codex's (cmp19.out).
3. Independent NUMERICAL search (my_35_search.py, my own code from the STRAT17/18 formula, not Codex's scripts):
   - K3+K5 at N=8: T = 0.0460905350 = 56/1215, at infinity 0.4444444 = 4/9, both as Codex states.
   - SLSQP, 30 random starts per k, isolates k = 6, 7, 8, 10, 20, 1e6 and lowers k = 8, 9, 10, 20, 1e6: see mine_35_search.out.
     No negative value. Isolates: the minimiser is K3+K5 except the known two-equal-edges zero (found at k=8).
     Lowers at k=8: minimum 0.0807823 at K3+K5 with maximal lower trace s=1, equal to Codex's 95/1176.
     Lowers at k = 9, 10, 20: minima 0.0654321, 0.0539259, 0.014253, all K3+K5 at s = k-7, each equal to Codex's
     F_k(k-7) = 2(k-3)(11k+7)/(15k^2) divided by M^2. At k = 1e6 the minimum is 7e-12 at s = k-7: T* stays near 22/15 while
     the 1/M^2 normalisation sends T to 0. Strict T > 0 at each N, no uniform margin as N -> infinity (as in 4+4).
   Corroboration only, not proof.

What it does not cover: 4+5 and 5+5 connected splits (STRAT20, queued on mini1 behind the heavy lock); actual D>2 top
multiplicity beyond the selected-projector closure.
