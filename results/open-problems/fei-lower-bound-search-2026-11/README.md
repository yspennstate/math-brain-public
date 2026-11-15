# Fourier entropy-influence: exhaustive monotone censuses and structured searches, 10-12 November 2026

This folder is the record of a companion campaign to `../fei-solve-2026-11`. Where that campaign works on the proof
side of the Friedgut-Kalai conjecture, this one computes: it runs exact censuses over every monotone Boolean function
of six and seven variables, anneals over larger monotone functions, and searches spaces of functions invariant under
a chosen group for a balanced function that beats the current lower bound on the constant.

## Results

Every number below is computed twice, once by the C census over integer Walsh tables and once by a numpy recompute of
the leading function from its truth table (`code/merge_census.py`); the two agree to 6e-13.

- Monotone, n = 6, all 7,828,354 functions (weighted count equal to the Dedekind number): max H/I = 3.739764017898;
  max over f of min_i E_i/Inf_i = 2.944495303872; balanced max H/(I-1) = 6.347067498702.
- Monotone, n = 7, all 2,414,682,040,998 functions (six parts, `results/out7_0..5.txt`, merged in
  `results/merged7_first_pass.txt` and `results/merged7_full.txt`): max H/I = 3.804357069772 (AND_7 and OR_7);
  max min_i E_i/Inf_i = 2.954683814183; balanced max H/(I-1) = 6.347067498702, attained only by the six-variable
  maximiser with a dummy variable. No seven-variable monotone balanced function improves on six variables.
- Annealing over monotone functions (`code/mono_search.c`, which reproduces both census maxima on every run) gives
  lower bounds min_i E_i/Inf_i >= 3.3047 at n = 8 and >= 3.4011 at n = 10. Read as formulas (`code/minterms.py`), the
  leaders are read-once trees and a 5 x 2 tribes function, a class the monotone tower bound of the companion paper
  already covers.
- Group-invariant searches for the general (non-monotone) lower bound: one search per structure (graphs, designs,
  affine and projective groups, with or without coin variables), each listed in `STATE.md` with its best slack against
  the record. None goes above it. The symmetry group of the record function has exactly three index-2 subgroups; the
  inclusion of the affine GF(9) group among them was checked by machine (`code/ap9_in_k33.py`), and searches in
  those spaces reach the record's level and no further.

The general lower bound on the constant stays at 6.521845710923 and the conjecture stays open.

## Layout

- `STATE.md`: the running log, newest block first, with the reading of each search as it ended. Run-time machine
  details have been removed.
- `code/`: the census and search programs (C for the inner loops, Python for checks, merging and seed generation) and
  the queue scripts that fed them to the worker machines.
- `results/`: census outputs per part, merged tables, search outputs by family (`het`, `hot`, `ms`, `tower`, `zoo`,
  `seeds`, `v4n6`, `v4n7`, `q7`).
- `notes/`: a note on the tower construction.

## Credit

The conjecture is due to Friedgut and Kalai (1996). The lower bound 6.5218 is Numaro's (2026); earlier bounds are due
to O'Donnell, Wright and Zhou (2011) and to Hod. The monotone counts are checked against the Dedekind numbers; the
seven-variable value is due to Church (1965). The largest-influence rule is refuted for monotone functions by the
construction Maj_k(y) OR (x AND [y >= y0]) cited in `STATE.md`. The computations ran as queued CPU jobs; they and
their reading were done by AI agents (Claude) and have not been reviewed by a person.

## Reusing it

`code/mono_census.c` is a complete exhaustive enumerator of monotone functions with Walsh-spectrum statistics and can
be pointed at any spectral functional; `code/merge_census.py` is the independent recompute. The rule used throughout,
that a reported maximum is rebuilt from its explicit truth table before it is quoted, is what kept every number here
reproducible.
