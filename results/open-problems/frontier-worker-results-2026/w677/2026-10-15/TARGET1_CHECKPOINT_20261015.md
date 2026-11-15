# T127 target1 checkpoint 2026-10-15T03:33:48.540389+00:00

STATE: WORKING. The full ordinary T3/T4 problem remains OPEN. Positive linear exact-law lower mean growth is UNPROVED.

Current exact-version findings:
- C26_absorbing_extinction_floor v1: independently checked proof; audit PASS.
- C27_joint_response_queue v2: independently checked proof; audit PASS.
- C28_fixed_cap_sterile_barriers v1: independently checked proof; audit PASS.
- C29_logarithmic_caps v2: numerical evidence; audit PASS.
- C30_linear_truncated_mean_criterion v1: independently checked proof; audit PASS.
- C31_unequal_cap_response_operator v1: independently checked proof; audit PASS.
- C32_forced_input_child_coverage v1: proof (unaudited); audit pending.

C31v1 has its OWN construction PASS; C29v1 PASS excluded that construction and covered its distinct16-root stage. C29v2 is a separate24-root numerical update with no transferred verdict. C27v1 is superseded by independently passed v2.
C28 closes all fixed/bounded-cap ordinary lower models at p=1/4. C31 validates growing deterministic depth budgets. C30 would turn a positive limsup E[R_H]/H into ordinary recurrence, but supplies no positive value.

| p | H | reps | M | mean R1 | between-run SD | ratio to (H+2)/3 |
|---|---:|---:|---:|---:|---:|---:|
| 1/4 | 20 | 3 | 4000 | 2.6894167 | 0.12146459 | 0.36673864 |
| 1/4 | 32 | 3 | 4000 | 5.84075 | 0.42451818 | 0.51536029 |
| 1/4 | 64 | 3 | 4000 | 15.656167 | 0.26248111 | 0.71164394 |
| 1/4 | 128 | 3 | 4000 | 34.898 | 0.799878 | 0.80533846 |
| 6/25 | 20 | 3 | 4000 | 1.5385833 | 0.027046642 | 0.20980682 |
| 6/25 | 32 | 3 | 4000 | 1.75225 | 0.0074035464 | 0.15461029 |
| 6/25 | 64 | 3 | 4000 | 2.2344167 | 0.085617001 | 0.10156439 |
| 6/25 | 128 | 3 | 4000 | 3.96875 | 0.16234762 | 0.091586538 |

The denominator is the ordinary p=1/4 all-active expectation ceiling. At6/25 it is a comparison baseline; the sharper geometric ceiling is in C29v2. These ratios and bars are numerical evidence, not confidence enclosures.

| p | H | completed reps | M | mean R1 | between-run SD | ratio to (H+2)/3 |
|---|---:|---:|---:|---:|---:|---:|
| 1/4 | 20 | 3 | 16000 | 2.7381667 | 0.09476800070874833 | 0.37338636 |
| 1/4 | 64 | 3 | 16000 | 16.008167 | 0.2809335326008327 | 0.72764394 |

M16000 stability campaign: 6/6 complete root artifacts. Partial populations are excluded. Inherited empirical-law bias remains unbounded even if all six finish.

Known-degree numerical calibration (three M2000 replicates each):
- d2 H20: mean8.0205, replica SD0.23578220882840153; full phase recurrent.
- d2 H64: mean25.775667, replica SD1.0116227475365185; full phase recurrent.
- d5 H20: mean0.56766667, replica SD0.028759056544562327; full phase transient.
- d5 H64: mean0.5595, replica SD0.028226760352544875; full phase transient.

For the physical parent-step p, strict below-quarter recurrence is impossible for original-path T3 lower models by the all-active first moment. The target is the boundary1/4. Transformed SFM parameters must not be confused with physical p.
10 queued bundles/37 cards. No store integration, publication or git mutation.

NEXT: Target2: frontier-check an exact finite-block SITE-counting upper comparison via C3. C32 forced-input coverage is queued; actual input delivery and the C30 linear mean bound remain open. M16000 is complete.
Refresh using save_target1_checkpoint_v2.py. The old checkpoint writer is obsolete. Do not build another fixed/bounded-cap lower model, refine S_m, or add another finite-cap T4 obstruction.
