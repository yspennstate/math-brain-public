# Density of a finite return time for the diagonal candidate

**Status:** deterministic lemma proved below. Its probabilistic application concerns the *candidate* constant-`Q` clock on a fixed initial outer-cone branch. It does not establish the phase of a finite-width network return or the accuracy of that return time at order `1/L_m`.

Let `Q` be a fixed symmetric positive-definite `2 x 2` matrix with `Q_12 >= 0`, and let `R=(R_1,R_2)>0`. Define

\[
r(t)=e^{-Qt}R,\qquad I(t)=\int_0^t r(s)\,ds=A_Q(t)R,\qquad
A_Q(t)=\int_0^t e^{-Qs}\,ds.
\]

Each `I_j` is positive for all sufficiently small positive `t`. Let `T` be the first positive zero of either `I_j` after that initial interval, and set `T=+infinity` if there is none. Every finite `T` is a unique, **transversal** return of exactly one coordinate `j`: `I_j(T)=0`, `r_j(T)<0`, and `I_{3-j}(T)>0`. If `Q_12=0`, then `T=+infinity`.

To prove the sign assertion for `Q_12>0`, write the two eigenvalues as `0<lambda_-<lambda_+`. Each residual component has the form

\[
r_j(t)=a_j e^{-\lambda_-t}+b_j e^{-\lambda_+t}.
\]

This function has at most one zero on the nonnegative line. Indeed, multiplying by `e^{lambda_-t}` leaves `a_j+b_j e^{-(lambda_+-lambda_-)t}`, a monotone function unless `b_j=0`; at a zero its derivative is nonzero because `R_j=r_j(0)>0`. A zero, if present, changes the sign from positive to negative. Hence `I_j` first increases and then, if its residual crosses, strictly decreases. A positive-time zero of `I_j` must occur on that decreasing part, so `r_j(T)<0` and it is the unique positive-time return of `I_j`. Both clocks cannot vanish together: `A_Q(T)` is positive definite, being the integral of positive-definite matrices, so `A_Q(T)R=0` would force `R=0`. At the first return the other clock is therefore strictly positive. For `Q_12=0`, `r_j(t)=R_j e^{-Q_{jj}t}>0`, giving no return.

Suppose now that, conditional on this fixed `Q`, the law of `R` has a density on an open subset of the positive quadrant, such as either strict initial outer ratio cone. The finite-return subprobability law of `T` is absolutely continuous. At a point where coordinate `j` returns, the implicit equation `I_j(T,R)=0` has `partial_t I_j=r_j(T)<0`; it defines a smooth local return-time function. Holding `R_{3-j}` fixed,

\[
\frac{\partial T}{\partial R_j}
=-\frac{[A_Q(T)]_{jj}}{r_j(T)}>0,
\]

because `[A_Q(T)]_{jj}>0`. Thus the return-time map is a submersion on each local chart. The inverse image of a Lebesgue-null set of times has two-dimensional Lebesgue measure zero on that chart, by a local change of variables `(R_j,R_{3-j}) -> (T,R_{3-j})`. Countably many charts cover the finite-return set. Restricting to the event that this is the *first* return only removes points, so the finite-return subprobability measure remains absolutely continuous. If `Q` is random and `R|Q` has a density almost surely on the branch, integrating these conditional null statements gives the same conclusion unconditionally.

In the negative-correlation stopped-law candidate, on either **fixed** strict outer-cone branch, `Q=C+diag(P_1,P_2)`. The branch's masks defining `P_1,P_2` use only the marked endpoint population and which cone was chosen, not the magnitude of `R`; the initialization primitives make that population and `C` independent of `R=y-F`. The latter has a full-dimensional density. Consequently the conditional-density hypothesis holds after restricting `R` to that branch. This pays absolute continuity of the ideal finite candidate return time. By `PHASE_AVERAGING.md`, it permits ideal oscillatory averaging for phases built from `L_m T/gamma` with fixed measurable offsets. It does **not** transfer that averaging to actual width-dependent `T_m`: convergence `T_m -> T` alone is too weak, and the order-one Euler and coupled-network corrections remain unpaid.
