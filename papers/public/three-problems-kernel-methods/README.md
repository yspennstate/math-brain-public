# Three problems in kernel methods: proofs and finite-size measurements

Yitzchak Shmalo, September 2026.

Part I proves three statements about random kernel matrices (the setting and Target 3 in
`paper/p1_setting_t3.tex`, Target 2 in `paper/p1_t2.tex`, Target 1 in `paper/p1_t1.tex`). Part II
measures the same objects at finite size: the moment ladder of the Veronese design against the
Catalan numbers, the spectral edge, and the gap statistics.

- `paper/` the LaTeX source (`kernel_open_problems_numerics.tex` includes the three Part I files) and the compiled PDF.
- `records/` one JSON record per measured design lane.
- `records_additions/` derived tables and the later lanes, with `derived/recompute_from_records.py`, which recomputes the moment tables from `records/` alone.
- `checks/` independent checks of the records (semicircle moments, operator norm, a GOE null, the gap blocks).
- `refresh_p9.py` regenerates the tables and computed numbers of the paper from `records/`, rewrites the .tex in place and audits the result; `python refresh_p9.py --no-build` skips pdflatex. Six values in the Veronese-hardness discussion (`\numVh...`) are not produced by it: on this tree it drops them and its audit reports them as undefined, so keep the shipped .tex unless those values are supplied.
