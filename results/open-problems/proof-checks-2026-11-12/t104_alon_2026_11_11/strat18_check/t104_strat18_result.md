# T104 (Alon Conj. 1.5): split 4+4 with arbitrary lower components - STRAT18 result

13 Nov 2026, 16:5x +04. an agent. Codex on Mac mini 1, ~/agent_run/STRAT18 (normal speed, exited 16:49 +04).

## What is proved

PROVED (STRAT18/replay_all.py, 32 exact stages: 24 inherited from STRAT17, 8 new):
1. Split 4+4 (two connected four-vertex carriers, each holding one top eigenvalue) satisfies T >= 0 for every
   integer N >= 8 and for fixed graphs padded to N -> infinity, with isolates or ARBITRARY lower components
   (lower component size not bounded by five).
2. Two connected simple four-vertex top carriers give T > 0; any positive lower trace gives T > 0.
3. On the selected-projector closure, equality occurs exactly at two equal edges plus isolates.
4. Setup for 3+5 (triangle corner reduction and K_u concavity) is in place; its signs are OPEN.

Method: fix both top vectors; T* separately concave on K_u x K_v; four-vertex extremes are trees (star, path) or
rank <= 2. Tree pairs: exact flux parametrisation, numerators with 4,536-6,075 rational coefficients, all positive
at k = 6+z. Rank boundary: seven corner families, coefficientwise PSD with T* margin 1/100. Inverse padding
derivative PSD at both endpoints, so k = 6 is hardest. Maximal lower trace: F_k(k-7) >= F_6(0) + 3/10 by twelve
exact Bernstein controls. Disconnected extremes go to the already proved 3+4, 2+4 and smaller classes.

## My independent checks (all PASS)

1. Frozen STRAT18 after Codex exited (70 files hashed, strat18_freeze.sha256), reran replay_all.py from the
   freeze: 32/32 PASS, 127 s, 105 MB peak. Live folder byte-identical to the freeze afterwards.
2. Read by hand the PSD routine behind boundary44.py and padding44.py: exact symmetric elimination that rejects a
   negative pivot and a zero pivot with a nonzero row; each script asserts zero failures, and replay_all fails a
   stage on a nonzero return code.
3. my_44_search.py (float search written from the STRAT17 formula, not Codex's code): no negative T. With lowers
   the tight spot is K4+K4 at maximal lower trace, T* about 1.7 at k = 1e6, so T decays only through the
   normalisation; zeros found only at two equal edges.

## Caveats

- Still rests on STRAT15's 9,370-box cover through the inherited stages (not rerun).
- No uniform positive margin as N -> infinity: T -> 0 like 1/M^2 at maximal lower trace.

## What is NOT proved (OPEN)

Split 3+5, 4+5 and 5+5, with or without lower components. The disconnected D = 2 statement with components of at
most five vertices needs those three classes.
