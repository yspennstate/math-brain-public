# account01/B08 r20 strengthening — parametric gate, cutoff improved from 1/96 to 1/81

This is an immutable strengthening of the r20 handoff; it does not retract the earlier `1/96` theorem and does not change full-target status.

**Canonical strengthened bundle:** `yspennstate/math-open-problems@343e90597bba67c8f06369813514d97e0bf0651a`, same r20 directory, especially `STRENGTHENING_ADDENDUM.md`, `check_strengthening.py`, `CHECK_STRENGTHENING_OUTPUT.txt`, and `CLAIMS_STRENGTHENING.json`.

## `QFORM-SPECTRAL-GATED-PARAMETRIC-SPLIT-v1`

Let `P_kappa=1_{|A|>=kappa}` have rank exactly three, with `0<kappa<1`. Choose `delta,b>0`, let `H={P_ii>delta}`, and put `m=delta/b`, `alpha_m=(1-sqrt(3m))/2`, `rho0=alpha_m*b-kappa`. If

`m<1/3`, `rho0>0`, and

`(sqrt(m/alpha_m)+sqrt(6)kappa/rho0)^2<1/2`,

then either the surviving high-window Gram has minimum eigenvalue at least `b`, in which case the designated account02/B08 perturbative theorem gives a **continuous C_0 density** with

`||p_Q||inf <= 9sqrt(3e)/(2rho0)`,

or some unit high-spectral direction has more than `1-b` of its squared mass on fewer than `3/delta` physical coordinates.

This is the newest Claude Section 5.1 frame split plus the account02/B08 dense-tail payment, now as a reusable parameter theorem.

## Strong clean corollary

Take `kappa=1/81`, `delta=1/32`, `b=1/2`. If the actual spectral window `P=1_{|A|>=1/81}` has rank three, then either

- diffuse: `lambda_min(R_{H^c}^T R_{H^c})>=1/2` and

  `||p_Q||inf < (14580/419)sqrt(3e) = 99.3691029643... <100`, with a continuous C_0 density; or

- localized: a unit `v in Ran P` has `||v_H||^2>1/2`, `|H|<=95`, hence some `|v_i|^2>1/190`.

Exact rational gate verification:

`alpha>17/60`, `rho0>419/3240`,

`sqrt(m/alpha)<8/17`,

`sqrt(6)kappa/rho0<98/419`,

and

`(8/17+98/419)^2 = 25180324/50737129 <1/2`.

Thus the earlier r20 `1/96` cutoff is safely strengthened to `1/81`; the unrestricted theorem remains open, with the same bounded-cardinality localized hybrid as the first B08 gap and with all rank->3 spectral-window cases still outside this branch.
