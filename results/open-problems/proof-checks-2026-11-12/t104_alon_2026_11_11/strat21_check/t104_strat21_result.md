# T104 STRAT21: split 5+5 with arbitrary lower components (an agent audit, 13 Nov 2026)

Claim (Codex STRAT21, gpt-6.1-sol high, normal speed, Mac mini 1, exit 0 at 21:10 Mac time): for disconnected D=2 graphs whose
two top carriers are connected five-vertex parts, T >= 0 for every N >= 10 and for N -> infinity, with isolates or arbitrary
lower components (of any size); two connected top carriers give T > 0; equality only at two equal edges plus isolates in the
selected-projector closure; positive lower trace is strict. With STRAT15's full-cover theorem kept as a premise, this closes the
disconnected D=2 case of Alon's Conjecture 1.5 when every component has at most five vertices. Full statement and proof:
STRAT21/RESULT.md (54-stage exact replay, replay_all.py).

How it closes:
- every pair with a rank<=2 five-part (R5) or a five-tree against a rank<=3 five-part: transferred from the proved edge+five
  theorem at k=5 to k=8 with the second five-part fixed (its trace-square and Y terms cancel exactly), extra T* >= 1/100;
  Bernstein controls with rational PSD coefficient matrices.
- the rank-three zero-edge endpoint Z5: F25 >= 1/5 by a matrix SOS (one 52-dim free block, nine 28-dim edge blocks, six 7-dim
  box blocks; every Gram entry an integer over 8e10, each an integer-factor product plus a diagonally dominant residual).
- the last pair: T* >= 2/5 - 9/50 = 11/50 at k=8.
- lowers: trace interpolation with cap k-9 (nontrivial lowers start at k=10).

My checks:
1. Freeze: 202 files hashed on mini1 after Codex exited (strat21_freeze.sha256); the laptop copy matches (202 of 202); the
   live tree still matched the freeze after my replay. The freeze left out every file named codex.log, but Codex hashes
   inherited20/codex.log (a copy of STRAT20's log) as a proof input; its sha256 685976f0... equals STRAT20/codex.log, so the
   input is genuine. My first replay copy lacked it and stopped at once; the second copy kept it.
2. Replay: fresh copy, framework python 3.13, SymPy 1.13.1, replay_all.py: 54 of 54 stages PASS (46 inherited, 8 new), 393 s,
   423 MB peak (strat21_myreplay.out/.time). All 145 hash fields in my replay_summary.json equal Codex's; only timings differ
   (cmp21.py, cmp21.out). The run waited on a 25 percent free-memory gate (strat21_gated.sh).
3. Independent NUMERICAL search (my_55_search.py, my own code from the STRAT17/18 formula, adapted from my 4+5 search, not
   Codex's scripts), 30 SLSQP starts per scale, seed 1113:
   - K5+K5 at N=10: T = 0.03515625 = 9/256; at infinity 0.375 = 3/8; with lowers at s=k-9, k=10,11,12,20 my values equal
     Codex's F_k(k-9)/M^2 = 2(k-3)(4k+3)/(5k^2) / ((k-1)/2)^2 to ten digits (0.0594567901 at k=10).
   - isolates, k = 8, 9, 10, 12, 20, 1e6: the minimiser is K5+K5 every time (all twenty edges at weight 1/5), minima
     0.0351563, 0.0722222, 0.102, 0.146875, 0.237375, 0.374997. No negative value.
   - lowers (lower trace s free in [0, k-9]), k = 10, 11, 12, 20: minimiser K5+K5 at s = k-9 every time, minima equal to the
     fixture values above. At k = 1e6 the best point is 1.1e-11 at s = k-9 (K5+K5 gives 6.4e-12; SLSQP stopped near it on the
     flat 1/k^2 scale), positive.
   Corroboration only, not proof.

What it does not cover: actual D>2 top multiplicity beyond the selected-projector closure; top carriers of six or more vertices;
the connected D=2 cases outside the STRAT15 cover (kept as a premise, not rerun).
