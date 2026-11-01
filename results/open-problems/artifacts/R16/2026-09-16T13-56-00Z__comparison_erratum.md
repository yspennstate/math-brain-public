# R16 finite-t comparison correction

This immutable artifact corrects one sentence in `runs/R16/2026-09-16T13-56-00Z__bf-dtv-sparse-bound.md`.

The report says that for every `t>=17` the coarse estimate

`R_t < 3 sqrt(2 pi t) < 2t-3`

already proves that the support-sensitive radius beats the Bednarchak–Helm linear bound. The threshold in that *coarse comparison* is actually `t>=18`, not `t>=17`:

- at `t=17`, `3 sqrt(34 pi) = 31.005279... > 31 = 2t-3`;
- at `t=18`, `3 sqrt(36 pi) = 31.904169... < 33 = 2t-3`;
- the difference `2t-3-3 sqrt(2 pi t)` is strictly increasing for `t>=18`, since its derivative as a real function is `2 - (3 sqrt(2 pi))/(2 sqrt(t)) > 0` there.

The theorem and tracked bound are unchanged. The exact radius itself already wins at `t=17`, as certified by the exact checker:

`R_17 = 1418338704709387740294 / 48661191875666868481 = 29.147...`,

so `ceil(R_17)-1 = 29 < 31 = 2t-3`.

Thus the correct statement is:

- the integerized support-sensitive term first strictly beats `2t-3` at `t=16`;
- `t=16,17` are verified directly from the exact rational formula;
- for every `t>=18`, the simpler inequality `R_t < 3 sqrt(2 pi t) < 2t-3` proves the comparison uniformly.
