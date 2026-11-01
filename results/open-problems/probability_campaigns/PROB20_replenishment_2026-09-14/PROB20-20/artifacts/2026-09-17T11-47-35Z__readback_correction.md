# Readback correction for 2026-09-17T11-47-35Z report

Report creation commit: `689332416e6d078afa62c053137409cfc8a7e81c`.

Exact-commit readback found one **typesetting-only** error in Theorem 12.1, equation (12.8). The immutable report displays

```text
Y_(1)/n_j <= K_{n_j}/n_j + rac{C_{n_j}}{n_j}.
```

The intended and mathematically used inequality is

\[
\frac{Y_{(1)}}{n_j}
\le
\frac{K_{n_j}}{n_j}
+
\frac{C_{n_j}}{n_j}.
\]

The surrounding prose states exactly this inequality: if the maximum is at most `K_n`, the first term suffices; otherwise the maximum is one of the summands in `C_n`. No theorem, bound, proof step, metric value, or status changes. The original report remains immutable.