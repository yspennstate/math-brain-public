# records_additions

Raw numbers found on this PC on 2026-09-16 that are not in `records/` and that `refresh_p9.py` could
be taught to read, plus a derived recomputation of quantities the paper quotes from `records/`.
Nothing here was fetched from the DGX (unreachable); nothing was renamed or reshaped. Fields are as
the producing script wrote them. See `../DATA_ADDITIONS.md` for what each number means and whether
it should enter the paper.

## offbox_scratchpad/  (laptop measurements, session 3b7c05d5, 2026-09-15)

Each JSON is accompanied by the script that wrote it (and the console log where one was kept).
None carries a `kind` field; a new kind would have to be declared if `refresh_p9.py` is to read them.

| file | what | designs | status of the source memory |
|---|---|---|---|
| `veronese_local3.json` (+`.py`) | sphere-input traceless-block construction of the leave-one-out normal: `v2..v5` = d^{k-1} Tr(A^{2k}) for k=2..5, `vse*` their s.e., `g*`/`gse*` the same for the generic (isotropic Gaussian rows) arm, `edge`, `gedge` at d=8,12,16,24,32,40 | n = 54477, 39487, 24801, 7373, 2650, 925 | verified (`the_semicircle_conjecture_survives_a_second_row_law_and_isotropy_is_schur_2026_09_15`) |
| `veronese_local2.json` (+`.py`) | earlier, smaller run of the same construction (n=150 per d, d=6..16); superseded by local3 | 150 | verified |
| `kurtosis_law2_d24.json`, `kurt2.log` (+`kurtosis_law2.py`) | rows with independent coordinates at d=24 (m=299): excess over Catalan (`e2..e5`, s.e. `se2..se5`) for uniform, Gaussian, Laplace and three-point laws at matched kurtosis `kappa`; `nz` = nonzero coordinates per row | 17,752-74,015 per arm | verified (`the_fourth_moment_alone_sets_the_semicircle_correction_2026_09_15`) |
| `kurtosis_law_d14.json`, `kurt.log` (+`kurtosis_law.py`) | the same at d=14 (m=104); these are the numbers behind tex lines 680-685 | ~1e5 per arm | verified |
| `matched_kurtosis_d14.json` (+`matched_kurtosis.py`) | Veronese r=1 vs i.i.d. rows matched on kurtosis 3+24/d vs Wishart-like rows with r=2,4,8 rank-one summands, d=14; behind tex lines 671-677 | 17,291-100,572 | verified |
| `kurtosis_null_direction.json` (+`kurtosis_of_the_null_direction.py`) | sphere construction: kurtosis of the row along a typical direction (`kappa_typ`) and along the null direction (`kappa_null`), with the two variances, at d=8,10,14,20; behind tex line 662 (d=20 only) | 12,753-97,056 | verified |
| `vh2.log` (+`vanhandel_params2.py`) | Brailovskaya-van Handel parameters of the Veronese Gram at d=10..44: measured `||E Z^2||` (biased high, see DATA_ADDITIONS item 14), `sigma`, `R(max)`, `R(p99)`. The exact sigma is `sqrt((p-1)(d^2+13d+14)/2)`. | 40k-80k samples per d | provisional (`the_veronese_hard_edge_is_a_van_handel_matrix_concentration_problem_2026_09_15`) |

## vit_base_spectra_2026_09_16/  (laptop, session b79dd98c, 2026-09-16 03:51)

Every singular
value of five weight matrices of timm `vit_base_patch16_224.augreg2_in21k_ft_in1k`, with the
Marchenko-Pastur edges from each matrix's own entry standard deviation. The counts above the upper
edge (67, 78, 36, 78, 2 of 768) were recounted from the JSON on 2026-09-16 and agree with the README.
Status: verified (`the_vit_spectra_were_never_saved_so_i_measured_them_2026_09_16`). Measured for a
film, not for this paper.

## derived/  (computed from ../records on 2026-09-16; regenerate with the script)

`recompute_from_records.py` reads only `../../records/*.json` and writes:

- `moments_by_rowlaw.json` - the semicircle ladder per (rowlaw, d), the mixture that
  `table_moments` currently prints, and intercept fits on the pure Veronese ladder (count-weighted as
  in `refresh_p9._wls`, and inverse-variance weighted).
- `hardedge_ladder.json` - per d: s_min(Z)/s_min([b,H]) statistics, Kolmogorov-Smirnov distances of
  p s_min^2 for Z, [b,H], H against 1-exp(-sqrt t - t/2) with the 95 percent critical value, the
  reduction's b-moment predictions against the measured ones, lower-tail percentiles, overlaps,
  and the inverse-first-moment block statistics for both Z and [b,H].
- `gap2_certificates.json` - per (d,h): in-window and best certificates with their delta_L, the two
  V/sigma^2 derivations, tau_sum, the exact-form fields; the constants written into the lane files;
  and tab:t3 averaged over all 36 designs at d=10, h=1.
- `cgec_arms.json` - unit-column vs raw-column arms per (d, Delta), and the Hermite constants.
- `correction_lanes.json` - every correction lane: best ridge, gains in squared risk and in the
  loader's physical metric, the sign of the margin at each ridge, eta and its bound, identity error.
- `gap_blocks.json` - the within-block delta ladders at every (d, h, k) with inversion counts.
- `prune_blocks.json` - beta split into its three block suprema.

These are derived tables, not records; they exist so the writer can audit `DATA_ADDITIONS.md` without
re-deriving it.
