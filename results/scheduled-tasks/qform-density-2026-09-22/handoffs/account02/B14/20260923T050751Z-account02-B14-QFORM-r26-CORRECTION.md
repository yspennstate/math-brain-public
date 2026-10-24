# account02/B14 r26 correction handoff

A readback audit found one quantifier/inequality wording issue in the immutable r26 report and handoff. The mathematics and constants are unchanged.

For a bank statistic `W_j=a_j^T V^(j)`, the abstract rescaling may use any chosen cap `eta_j >= ||p_(W_j)||inf`, with `Y_j=eta_j W_j` and `r_j=gamma_j/eta_j`. The abstract theorem remains

`||p_Q||inf <= C4/min(nu,max_j |r_j|)`.

For the universal product-projection consequence, **choose**

`eta_j := sqrt(2)/||a_j||_2`.

Then the exact relation is

`r_j = gamma_j ||a_j||_2/sqrt(2)`,

so

`r_* = 2^(-1/2) max_j |gamma_j| ||a_j||_2`.

The original report's `r_* >= ...` phrase should not be read as holding for an arbitrarily inflated certified `eta_j`; it is the canonical explicit choice above that yields the universal consequence. All subsequent bounds, including the `sqrt(d)` selection estimate and the target-valid Claude-Theorem-H obstruction, are unchanged.

Canonical correction addendum: `yspennstate/math-open-problems@19de5b5fc1dcc88d0bad7ce28f7857ae40a8e545`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260923T050751Z-account02-B14-QFORM-r26/CORRECTION.md`.
