# r24 addendum — optimal asymmetric numerator split

This addendum sharpens only the numerical square-root small-ball constant in Section 5 of `REPORT.md`. The structural theorems and the full-target status are unchanged.

From Section 4, in the tiny-pair branch,

`sqrt(j) <= 5 delta^2 C + 3 delta U`,

where

`C=||off(A[K,K])||_F`, `U=||A[S,K]||_F^2`.

For any `0<theta<1`, either

`C >= theta sqrt(j)/(5 delta^2)`,                                  (A.1)

or

`U >= (1-theta) sqrt(j)/(3 delta)`.                               (A.2)

The first-compound product-Fourier small-ball theorem gives, after the same physical random cut in the first branch,

`K_C(theta)
 = H_1 [ (1/4)(theta sqrt(j)/(5delta^2))^2 ]^(-1/4)
 = H_1 sqrt(10delta^2/(theta sqrt(j)))`,                           (A.3)

and in the second branch

`K_U(theta)
 = H_1 [ (1-theta)sqrt(j)/(3delta) ]^(-1/4)`.                     (A.4)

Thus the optimal worst-case split is the unique `theta` satisfying

`K_C(theta)=K_U(theta)`.                                           (A.5)

Writing

`r = 3sqrt(j)/(100delta^3)`,                                      (A.6)

this is

`r theta^2+theta-1=0`,

hence

`boxed: theta_* = 2/(1+sqrt(1+4r)).}`                             (A.7)

For the current global localized-overlap-two constants

`delta=1/64`, `j=1/144`,

one has

`r=16384/25`,

`boxed: theta_* = 10/(5+sqrt(65561))
                  =0.038307010417064684... .}`                    (A.8)

At this value the two branch constants coincide and the universal residual half-Riesz/square-root small-ball estimate sharpens to

`boxed:
 sup_t P(|Q-t|<rho)
 <= H_opt sqrt(rho),
 H_opt
 =H_1 sqrt(15/(512 theta_*))
 =6.84697451536321... .}`                                         (A.9)

This replaces the nonoptimized `8.063346501398827...` constant in Section 5.7 of the main report. It still does **not** by itself imply a bounded density; the remaining need is the same genuine-third-curvature splice named there.
