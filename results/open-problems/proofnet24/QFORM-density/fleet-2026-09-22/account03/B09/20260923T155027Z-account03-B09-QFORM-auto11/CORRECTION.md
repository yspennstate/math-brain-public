# Correction to the early SUBSTANTIVE checkpoint

The theorem statements and analytic constants in `SUBSTANTIVE.md` are unchanged. One final arithmetic line in the target-valid regression was misstated.

For the regression, the concentrated branch has the *actual* selected low-row mass `z_k=Z2=2`, so the sharper direct bound is

    4 sqrt(2) e^(1/4) z_k^(-1/8)
    = 4 sqrt(2) e^(1/4) 2^(-1/8)
    = 6.660699798151631...,

not `7.263544...` as typed in the checkpoint. The number `7.263544...` equals the direct prefactor `4 sqrt(2)e^(1/4)` before the factor `2^(-1/8)`, and also equals the weaker dichotomy constant `Cc*2^(-1/8)` after paying only the generic `z_k>=Z/2` loss. `CHECK_OUTPUT.txt` records the corrected arithmetic.

This correction strengthens the regression and does not alter the stated universal dichotomy constants `Cc<7.921`, `Cd<13.728`, the wedge identity, or the remaining gap.
