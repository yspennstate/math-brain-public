# Correction to REPORT.md, Section 9

The global conclusion (9.9) is valid, but one sentence in Section 9 attributes the lower-limit input too narrowly.

The displayed liminf inequality (9.2) **alone** does not imply `p_{Q_m}(0) -> 3sqrt(2)`. The needed convergence comes from the stronger mixture expansion proved in Section 6 of the cited partner report `yspennstate/math-open-problems@48e35fac4689f50a415638faba5a6e634b3d0329`:

`p_{Q_m}(0)/(3sqrt(2)) = 1 - m^{-1}[a_0 + sum_j c_j(1-q_j/(3sqrt(2)))] + o(m^{-1})`,

with finite coefficients. That expansion gives `p_{Q_m}(0)->3sqrt(2)`. Combining it with this run's global upper bound `limsup ||p_{Q_m}||_infty<=3sqrt(2)` yields

`||p_{Q_m}||_infty -> 3sqrt(2)`.

No other statement or proof step in REPORT.md changes.
