Independent check of C0033D Theorem 2 (the family Q_r with diagonal 1/2 and off-diagonals +-ir).

hess_qr.py: the full nine-dimensional entropy Hessian at Q_r by central finite differences (mpmath, 60 digits), from the
atom formula p_S = (-1)^{|S^c|} det(Q - I_{S^c}) alone. Negative definite at r = 0.05, 0.15, 0.25, 0.285, 0.2885
(hess_qr.out).

margin_qr.py: the Hessian on the invariant plane T = alpha I + beta (J_3 - I), by finite differences (80 digits), against
the Fisher matrix (11) of the report. The Hessian equals -(F + L tr T^2) + L (tr T)^2 to 1e-27 or better, and the margin
computed from it, 1 - 9 L (J^{-1})_{11}, agrees with formula (12)-(13) to twelve digits and tends to 4/(L+4)
(margin_qr.out). Both halves of Theorem 2 are confirmed.
