# PROB10-06 exact-checker re-execution receipt

After the immutable run report was written, the persisted source

`artifacts/prob10_2026-09-20/PROB10-06/20260920T1440Z_weighted_branchgap_check.py`

was re-executed in the current Python runtime using exact `fractions.Fraction` decisions. The execution completed successfully in 14.67 seconds and reproduced the archived substantive output exactly:

```text
WEIGHTED_BRANCHGAP_CHECK
RECT_PASS lambda=[12/5,2587/1000] p=[3/4,1]
visited=2615 accepted=1308 max_depth=28
speed_product_upper<999/1000
weighted_contraction_rho_s<99/100
worst_product_upper_float=0.998975869580471
worst_rho_s_upper_float=0.989481822302885
derivative_margin=4000/31214569
log_truncation=> E[B_N-B] <= (2587/1400)*(99/100)^N
HARD_CORNER_BASE_PRODUCT_float=0.999887580458478
HARD_CORNER_REFINED_PRODUCT_float=0.994297690358478
TYPE_VECTOR_CORNER_SLACK=239/8000
ROUNDING_GRID=1e-9 TYPE_VECTOR_ITERATIONS=30
ALL_EXACT_CHECKS_PASS
```

The elapsed-time line was emitted only by the execution wrapper and is not part of the checker source or archived mathematical output. The decimal lines are diagnostics; the accepting comparisons are exact rational inequalities.

This is a self-check, not an independent audit. It does not change the report's `PARTIAL / OPEN parent` status.