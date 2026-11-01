# Correction addendum — canonical choice of the bank density cap

This addendum corrects one quantifier/inequality wording in `REPORT.md`; it does **not** change the theorem, proof mechanism, target-valid stress family, or any numerical constant.

In Section 2, `eta_j` may indeed be **any chosen upper bound** satisfying

`||p_(W_j)||_infinity <= eta_j`,

and then `Y_j=eta_j W_j`, `r_j=gamma_j/eta_j` gives the abstract bound

`||p_Q||inf <= C4/min(nu,max_j |r_j|)`.

However, the later sentence

`Using only the universal projection caps gives r_* >= (1/sqrt(2)) max_j |gamma_j| ||a_j||_2`

should be read with the **canonical explicit choice**

`eta_j := sqrt(2)/||a_j||_2`.

For this choice the correct relation is the exact identity

`r_j = gamma_j ||a_j||_2/sqrt(2)`,

hence

`r_* = (1/sqrt(2)) max_j |gamma_j| ||a_j||_2`.

One should not infer the displayed lower bound for an arbitrarily inflated certified cap `eta_j`; choosing a larger-than-needed cap only weakens the rescaled coupling. Since the proof is free to use the universal product-projection bound itself as the chosen `eta_j`, every subsequent universal consequence in the report is unchanged.

The `R=(sum_j r_j^2)^(1/2)` formulation is likewise understood for the chosen caps used in the rescaling. The target-valid family in Section 4 uses scalar cap-one variables directly and is unaffected.
