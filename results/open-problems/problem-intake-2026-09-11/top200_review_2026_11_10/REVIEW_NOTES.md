# Review of the two top-200 lists, started 10 Nov 2026 (an agent, T-20261110-055)

Source: ../top200_probability_2026_10_14/list.jsonl (200 probability rows TOP200_FAMOUS, 200 deep-learning rows
TOP200_DL, 22 retired). Row status table: rows_status.tsv (tools/rows_status.py). Rows with a solved or settled
signal: solved_signals.txt (60 rows). Origin frontier moves were pulled first (113 lines, 5 rows).

His order (10 Nov 05:29): remove the problems we solved, remove rows that do not deserve a place and replace
them, build a third list (top 200 in mathematics generally), then work the rows closest to a solution.

## First pass, probability list (titles read against the literature to mid-2026; each flag still needs the
row's statement read before the verdict is final)

Flagged as solved, claimed or largely settled by others:
- T004 p_c < p_u on nonamenable graphs: claimed by an Oct 2026 preprint (our audit of its section 9 found it sound
  conditional on its sub-power bounds). Verdict pending: remove as claimed, or hold until refereed.
- T067 Kesten-Stigum tightness for reconstruction on trees: Mossel-Sly-Sohn settle q = 3, 4 for large degree. Read statement.
- T070 density conjecture for activated random walk: Hoffman-Johnson-Junge prove it in dimension one. Read statement.
- T076 random band matrices in dimensions two and three: delocalization for W > N^eps proved in 2025
  (Dubova-Yang-Yau-Yin and sequels). Read statement.
- T129 singularity probability of symmetric sign matrices: exponential bound proved (Campos-Jenssen-Michelen-
  Sahasrabudhe); the sharp base is open. Read statement.
- T107 Fyodorov-Hiary-Keating: maximum known to O(1) (Arguin-Bourgade-Radziwill); the limit law is open. Read statement.
- T030 hot spots for convex domains: false in high dimension (de Dios Pont 2024); the planar case is open. Repair statement.
- T180 prophet secretary: our hardness paper (posted 3 Nov) improves a bound; the optimal ratio is open. Keep.

Flagged as not probability (candidates to move to the general-mathematics list and replace here):
T124 T134 T147 T148 T149 T157 T158 T175 T182 T183 T184 T187 T189 T191 T192 T193 T195 T196 T197 T198 T202 T203
T204 T205 T207 T208 T209 T210 T211 T213 T216 (and to check: T121 T145 T152 T166 T173 T199 T206 T172 T185).

## First pass, deep-learning list (from the frontier literature notes)
- Solved by others: T314 (SK sampling for all beta < 1, Sep 2026 preprint), T352 (hidden-state noisy SGD privacy).
- Settled by us on the repaired statement: T255 (shaped-transformer covariance SDE, 17 Oct, triple audit).
- Duplicates: T303 (KLS, duplicate of T018), T363 (duplicate of T269).
- Row as stated already answered in the literature (kept only if a sharper open core is written in):
  T233 T261 T310 and the rows whose literature note begins "narrowed ... answered".

## Still to do
1. Read the statements of every flagged row; write VERDICTS.tsv (id, verdict, reason, source).
2. Replacements: probability problems for each removed probability row; deep-learning problems for each removed DL row.
3. The third list: top 200 open problems in mathematics generally (the moved rows seed it).
4. Closest rows: rank by frontier state (routes proved or narrowed, DAYS shape) and math-brain recall; work them.
