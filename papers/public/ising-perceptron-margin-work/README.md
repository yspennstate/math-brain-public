# Ising perceptron at general margin: working files

Companion material for `ising-perceptron-margin`, the computer-assisted extension of the
Krauth--Mezard capacity analysis from kappa = 0 to a strip of margins. The public repository holds
the paper and the release certificates; this one holds the working record behind them: the
certification code, the slab schedules, the batch results, and the notes kept while the strip was
being extended.

- `NOTES.md` the running mathematical notes: the system at general kappa, stationarity, the
  continuation and condition map, the certified slabs, the two-variable global condition and its
  certification at kappa = 0.05, the margins queue, and the proof verification pass of 2026-07-16.
- `DS_KAPPA_AUDIT.md` the audit of the Ding--Sun condition at general kappa, term by term.
- `huang_cert_*.py`, `lane_neg.py`, `locate_alpha.py`, `supplement_0p05.py`,
  `verify_lane1.py`, `portable_check.py` the Arb ball-arithmetic certificates for the Huang
  conditions (grid, Region I, star interior, sweeps) and the located-interval lane at negative kappa.
- `assemble_2varfn.py`, `collect_slabs.py`, `appendix_row.py`, `slab_windows.py`,
  `make_slab_schedule.py`, `drift_decomposition.py`, `measure_kappa_sensitivity.py` assembly of the
  two-variable function, collection of slab results into the tables, and diagnostics.
- `probe_*.py`, `rect_probe.py`, `test_2var_*.py`, `diag_wang_0p05.py` probes and tests used while
  locating the failing regions at kappa = 0.05 and checking the port of the two-variable condition.
- `slabs_*.json`, `slab_*.json` slab schedules and their certified results.
- `results/` per-kappa certificates (`alpha_star_*`, `huang_region1_*`, `huang_star_interior_*`),
  certified interval tables with provenance, the batch results under `results/box/` (a failed
  batch kept with its README in `results/box/failed_neg8_pads`), the finite-size panels `ml101_n30` and
  `ml201_panel`, and the raw run logs.
- `lean_skeleton/` the Lean statement skeleton generated from the certificates, with the mutation
  tests that check it rejects altered inputs.
- `paper/`, `note/` LaTeX sections of the paper and the short margin note.
- `exploration/` the ternary-prior exploration results.

Files already present unchanged in `ising-perceptron-margin` are not repeated here.
