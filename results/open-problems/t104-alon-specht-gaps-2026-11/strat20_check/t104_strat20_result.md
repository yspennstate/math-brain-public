# T104 STRAT20: split 4+5 with arbitrary lower components (an agent audit, 13 Nov 2026)

Claim (Codex STRAT20, gpt-6.1-sol high, normal speed, Mac mini 1, ended 19:36 Mac time): for disconnected D=2 graphs whose two
top carriers are a connected four-vertex part and a connected five-vertex part, T >= 0 for every N >= 9 and for N -> infinity,
with isolates or arbitrary lower components; two connected top carriers give T > 0; equality only at two equal edges plus
isolates in the selected-projector closure; positive lower trace is strict. Split 5+5 is set up (36 ordered endpoint-pair
types) but its signs are OPEN. Full statement and proof in STRAT20/RESULT.md (46-stage exact replay, replay_all.py).

How it closes:
- every pair with a rank<=2 four-part or a rank<=3 five-part: transferred from the proved 2+5 theorem at k=5 to k=7, keeping
  the five-part fixed (its trace-square and Y terms cancel exactly; B5 <= d5 pays the -8/35 change), extra T* >= 1/100.
- the six four-tree / five-tree pairs: cleared numerators with only positive coefficients in seven fluxes and z = k-7
  (23,715 to 38,574 terms), affine inverse-padding derivative makes k = 7 hardest.
- lowers: STRAT17 trace interpolation with S = k-8; F_k(k-8) >= F_7(0) + 1/4 uniformly, eighteen Bernstein controls.

My checks:
1. Freeze: 165 files hashed on mini1 after Codex exited (strat20_freeze.sha256); the laptop copy matches (0 mismatches);
   the live tree still matched the freeze after my replay (0 mismatches).
2. Replay: fresh copy, framework python 3.13, replay_all.py: 46 of 46 stages PASS, 193 s, 136 MB peak
   (strat20_myreplay.out/.time). All 106 hash fields in my replay_summary.json equal Codex's (cmp20.out).
3. Independent NUMERICAL search (my_45_search.py, my own code from the STRAT17/18 formula, adapted from my 3+5 search, not
   Codex's scripts):
   - K4+K5 at N=9: T = 0.0412328197 = 99/2401; at infinity 0.40816 = 20/49, both as Codex states.
   - SLSQP, 30 random starts per k, isolates k = 7, 8, 9, 11, 20, 1e6: the minimiser is K4+K5 every time (all six and all
     ten edges at weight 1/4 and 1/5), minima 0.0412328, 0.0860969, 0.121189, 0.172542, 0.277653, 0.408161. No negative value.
   - lowers (lower trace s free in [0, k-8]), k = 9, 10, 11, 20: minimiser K4+K5 at s = k-8 every time, minima 0.0696759
     (= 301/4320), 0.0573827, 0.048, 0.0151163, equal to Codex's F_k(k-8) = (k-3)(31k+22)/(20k^2) divided by M^2,
     M = (k-1)/2. At k = 1e6 the best point is 9.1e-12 at s = k-8 (K4+K5 gives 6.2e-12; SLSQP stopped near it on the
     flat scale 1/k^2), positive. No negative value anywhere.
   Corroboration only, not proof.

What it does not cover: the connected 5+5 split (STRAT21, queued on mini1 behind the heavy lock, 13 Nov 19:4x Mac time);
actual D>2 top multiplicity beyond the selected-projector closure; components of six or more vertices.
