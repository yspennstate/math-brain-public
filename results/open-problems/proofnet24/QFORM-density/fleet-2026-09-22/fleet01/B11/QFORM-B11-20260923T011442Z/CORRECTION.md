# Scope correction / edge case

Theorem 2.1 in `REPORT.md` should be read after discarding any index with spectral row `r_i=0`. Such an original variable is absent from `Q` because the corresponding row and column of `A=RMR^T` are zero, so conditioning/discarding it changes neither the quadratic form nor its law. For every remaining index `r_i!=0`, invertibility of `T` gives a nonzero null vector `z_i=T r_i`, and the signed Veronese parametrisation used in the proof is valid. Equivalently one may allow `q_i=(0,0)` for a zero row, but the nonzero formulation in the report is cleaner after this harmless deletion.

No other statement or constant in the report changes.
