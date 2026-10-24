# r28 correction addendum — exact-slope comparison in Section 5

This addendum corrects only the inequality-direction explanation surrounding equations (5.10)-(5.11) of `REPORT.md`. The new shear-determinant theorem, determinant identities, target-valid family, and bound (5.9) are unchanged.

For the odd-`N` trigonometric frame, every exact slope class is a singleton and

`m_* = max_j u_j^2`.

Since `sum_j u_j^2=1` and `u_j^2<=2/N`,

`1/N <= m_* <= 2/N`.

For the scaled family `2H_epsilon`, `mu'=8`. The designated account04/B05 theorem therefore has right-hand side

`51.6*(8*m_*)^(-1/3)`,

which lies between

`51.6*(N/16)^(1/3)` and `51.6*(N/8)^(1/3)`.

Thus the partner theorem's actual displayed estimate is `Theta(N^(1/3))` on this family and is not uniform as `N->infinity`. A valid one-sided consequence is

`||p_Q||_infinity < 51.6*(N/8)^(1/3)`

from `m_*>=1/N`. The phrase in the original report saying that the scale followed from the *upper* bound `m_*<=2/N` should be read only as an order-of-magnitude comparison, not as an upper-bound deduction. This addendum records the correct direction before final handoff.
