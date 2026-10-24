# account02/B02 early substantive checkpoint — adaptive fractional-volume gate

Programme: `QFORM-DENSITY-3EIG-20260922`. Full target remains open.

I independently checked the analytic constants and endpoints in `math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba:proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

For an original-coordinate cross block `M=A[I,J]`, let `Z=e_3(M^T M)` and let `alpha_i` be the row third-volume marginals. If `1<=q<3/2` and `max alpha_i<=q/2`, sharp Hausdorff--Young plus the volume-sampling Brascamp--Lieb determinant bound gives

`||p_Q||_inf <= [3e/((3-2q)sqrt(q))] Z^(-1/6)`.

The endpoint `alpha_i=q/2` is allowed because the scalar output Hausdorff--Young exponent is then exactly 2; the strict condition is only `q<3/2`, which is the time-integrability threshold. Recomputing the envelope integral gives exactly the displayed constant.

A small optimization was not used in the source report. Suppose a projection `P` obeys `max_i P_ii<=1/2` and

`d := sqrt(3) ||(I-P)M||_op / kappa`,  `kappa=s_3(M)`.

The source matrix estimate gives

`sqrt(alpha_i) <= sqrt(P_ii)+d sqrt(1-P_ii) <= (1+d)/sqrt(2)`

whenever `d<=1`. Hence `max alpha_i <= (1+d)^2/2`. The smallest admissible Jensen exponent is therefore

`q=(1+d)^2`.

It is time-integrable exactly when

`d < d_* := sqrt(3/2)-1 = 0.2247448713...`.

Substitution yields the adaptive bound

`||p_Q||_inf <= C(d) Z^(-1/6)`,

`C(d)=3e / [(1+d)(1-4d-2d^2)]`.

Thus the source's fixed choice `q=4/3` is a convenient certificate, not the endpoint. For a perturbation `M=M0+E`, `s_3(M0)>=a`, `max diag(P_range(M0))<=1/2`, put `theta=||E||_op/a`. Since `kappa>=(1-theta)a`, the adaptive route works for

`theta < theta_* := d_*/(sqrt(3)+d_*) = 0.1148535199...`.

A clean quantitative corollary is

`||E||_op <= a/10  =>  ||p_Q||_inf < 48.670/a`.

This enlarges the proved perturbation window from `a/16` to `a/10` at the cost of a larger, still universal, constant. The same optimization applies to the collective-tail certificate with `d=sqrt(3) epsilon/sqrt(T2)`; with `P` the top-two left singular projection, it only needs `T2/s_3(M)^2 > 3/d_*^2 = 59.3938769...` for some finite bound, rather than the source's convenient threshold 225.

Next step in this run: combine this adaptive D'/tail exit with the latest designated partner `account03/B02` Schur-gap theorem on the low-tail exact-rank-two endpoint, and isolate the remaining high-leverage / critical-alignment packet without discarding same-bank curvature.
