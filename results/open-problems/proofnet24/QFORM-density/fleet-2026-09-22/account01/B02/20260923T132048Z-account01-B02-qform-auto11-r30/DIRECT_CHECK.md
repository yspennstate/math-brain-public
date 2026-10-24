# Direct audit of the only partner endpoint used in r30

The r30 theorem uses account02/B02's grouped cross-Schur theorem only at `k=3,r=0`. This endpoint has a short independent proof, recorded here to guard against importing any stronger unreviewed part of the partner theorem.

Condition on every original coordinate except three source coordinates `x in R^3` and three disjoint receiver coordinates `y in R^3`. Let their literal physical cross block be an invertible `P`. The conditional phase is

`q(x)+r(y)+2 x^T P y`,

where `q,r` may contain arbitrary quadratic and affine terms. Put

`alpha_t(x)=prod_i f_i(x_i) exp(i t q(x))`,
`beta_t(y)=prod_j g_j(y_j) exp(i t r(y))`.

Because each scalar input density is a probability density bounded by one,

`||alpha_t||_2^2 = prod_i int f_i^2 <=1`,
`||beta_t||_2^2  = prod_j int g_j^2 <=1`.

With Fourier convention `hat beta(xi)=int beta(y) exp(i xi.y)dy`, the conditional characteristic function is

`I_t=int alpha_t(x) hat(beta_t)(2t P^T x) dx`.

Cauchy--Schwarz, the change of variables `xi=2tP^T x`, and Plancherel give

`|I_t|
 <= ||alpha_t||_2 [int |hat(beta_t)(2tP^Tx)|^2 dx]^(1/2)`

` <= [(2|t|)^(-3)|det P|^(-1) (2pi)^3]^(1/2)`

` = pi^(3/2)|det P|^(-1/2)|t|^(-3/2)`.

Together with `|I_t|<=1`, uniformly in the outside conditioning,

`|phi_Q(t)| <= min(1, pi^(3/2)|det P|^(-1/2)|t|^(-3/2)).`

Writing `K=pi^(3/2)|det P|^(-1/2)`, the crossover is `T=K^(2/3)=pi|det P|^(-1/3)` and

`int_R min(1,K|t|^(-3/2))dt = 6T = 6pi|det P|^(-1/3).`

Hence Fourier inversion gives

`||p_Q||_infinity <=3|det P|^(-1/3)`

and a continuous density vanishing at infinity. This exactly matches the `k=3,r=0` specialization of account02/B02's completed theorem.

No pointwise one-dimensional van der Corput estimate, no spectral rotation, and no transformed-coordinate independence is used.

For the r30 anchored identity, the selected pivot has `det P_3(i,j)=det(P)S_ij`; therefore the direct endpoint above independently verifies every analytic step after the deterministic inequality `|S_ij|^2 >= (h_r+h_c-1)||S||_F^2`.
