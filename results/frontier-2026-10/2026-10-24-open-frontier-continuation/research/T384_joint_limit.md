# T384 joint initialization limit

Fix `0<alpha<2`, put `beta=alpha/2`, and let all `(U_i,W_i)` be iid pairs of independent symmetric standard `alpha`-stable variables, normalized by `E exp(itU)=E exp(itW)=exp(-|t|^alpha)`. Set

`b_m=(m log m)^(1/alpha)`, `d_m=m^(2/alpha)=m^(1/beta)`, and for one pair

`X=W U_+`, `Z_A=W^2 1_{U>0,W>0}`, `Z_B=W^2 1_{U>0,W<0}`, `Z_C=U_+^2`.

Then `F_m=b_m^(-1)sum X_i`, `(A_m,B_m,C_m)=d_m^(-1)sum(Z_Ai,Z_Bi,Z_Ci)`. Define

`c_alpha=Gamma(alpha) sin(pi alpha/2)/pi` and `h_beta=Gamma(1-beta)`.

**Claim.** The four variables converge jointly to independent `(F,A,B,C)` with characteristic/Laplace transforms

`E exp(itF)=exp(-c_alpha |t|^alpha),`

`E exp(-s A)=E exp(-s B)=exp(-(c_alpha/2) h_beta s^beta),`

`E exp(-s C)=exp(-c_alpha h_beta s^beta)` for `s>=0`.

Thus F is symmetric `alpha`-stable with scale `c_alpha^(1/alpha)` in the stated characteristic-function normalization. A and B have one-sided tail constants `c_alpha/2`, C has `c_alpha`; these are the tails of their limiting positive `beta`-stable variables. Their sum `H=A+B+C` has transform `exp(-2 c_alpha h_beta s^beta)`, and the joint convergence includes `H_m=A_m+B_m+C_m`.

The stable-law tail input is `P(U>t)=P(W>t)~c_alpha t^(-alpha)` and an upper bound `P(|U|>t)+P(|W|>t)<=C t^(-alpha)` for `t>=1`. The normalization and asymptotic are given in [Bednorz–Łochowski–Martynek, arXiv:1802.00612v3](https://arxiv.org/html/1802.00612v3), Introduction, tail formulas, or [arXiv:2008.04423v1](https://arxiv.org/html/2008.04423v1), preliminaries. No result on products of stable variables or multidimensional convergence is assumed below.

## Exact product-tail constant

Symmetry of W makes X symmetric. For `t->infinity`,

`P(X>t)=E[1_{U>0} P(W>t/U | U)] ~ alpha c_alpha^2 t^(-alpha) log t`.  (1)

To justify the asymptotic rather than merely its order, take `h(t)=log t` and split U into `(0,h)`, `[h,t/h]`, `(t/h,t]`, and `(t,infinity)`. The first and third pieces are `O(t^(-alpha)log h)` by the stable tail bound and `E[U_+^alpha 1_{U_+<=v}]=O(1+log v)`; the last piece is `O(t^(-alpha))`. On `[h,t/h]`, both U and t/U tend to infinity uniformly. Uniform convergence of `x^alpha P(W>x)` to `c_alpha` gives its contribution as

`(c_alpha+o(1)) t^(-alpha) E[U_+^alpha 1_{h<=U_+<=t/h}]`.

Integration by parts and `P(U>u)~c_alpha u^(-alpha)` show the truncated moment is `alpha c_alpha (log t-2 log h)+o(log t)`, proving (1). The negative tail is identical. Consequently, for every `x>0`,

`m P(X>b_m x) -> c_alpha^2 x^(-alpha)`, and `m P(X< -b_m x) -> c_alpha^2 x^(-alpha)`,  (2)

since `m b_m^(-alpha) log b_m -> 1/alpha`. The upper estimate `P(|X|>t)<=C t^(-alpha)(1+log t)` also holds for `t>=e`.

For the positive endpoint variables, independence of U and W gives, for `x>0`,

`m P(Z_A>d_m x), m P(Z_B>d_m x) -> (c_alpha/2)x^(-beta)`,  (3)

and `m P(Z_C>d_m x) -> c_alpha x^(-beta)`. Their tails are bounded by `Ct^(-beta)` at every positive t after increasing C.

## Two-coordinate large jumps vanish

For any fixed `epsilon,delta>0`,

`m P(|X|>epsilon b_m, Z_A+Z_B>delta d_m) ->0`, and

`m P(|X|>epsilon b_m, Z_C>delta d_m) ->0`.  (4)

For the first claim, `Z_A+Z_B>delta d_m` requires `U>0, |W|>sqrt(delta)m^(1/alpha)`. Choose `L>sqrt(delta)`. The part `|W|>L m^(1/alpha)` has limsup at most `C L^(-alpha)` after multiplying by m. In the remaining part, `|X|>epsilon b_m` forces `U>(epsilon/L)(log m)^(1/alpha)`, whose probability tends to zero independently of W, while `mP(|W|>sqrt(delta)m^(1/alpha))` stays bounded. First send m to infinity, then L to infinity. Interchange U and W for the second claim, observing that `Z_C>delta d_m` requires `U>sqrt(delta)m^(1/alpha)`. Also,

`m P(Z_A+Z_B>delta d_m, Z_C>delta d_m) <= m P(|W|>sqrt(delta)m^(1/alpha))P(U>sqrt(delta)m^(1/alpha)) ->0`.  (5)

The events `Z_A>0` and `Z_B>0` are disjoint within a single observation. Equations (4)–(5) show that every limiting large-jump measure is supported on the four coordinate axes. They are the precise separation of product jumps from W and U endpoint extremes; mere marginal tightness would not imply it.

## Poisson convergence of truncated sums

Fix `epsilon,delta>0` and retain only `|X_i|>epsilon b_m` in F and only `Z_{Ji}>delta d_m` in each `J=A,B,C`. By (2)–(3), the rescaled one-observation measures on each axis converge vaguely away from zero to Lévy measures

`nu_F(dx)=alpha c_alpha^2 |x|^(-1-alpha)dx` on each of the positive and negative half-axes,

`nu_A(dx)=nu_B(dx)=beta(c_alpha/2)x^(-1-beta)dx`, and `nu_C(dx)=beta c_alpha x^(-1-beta)dx` on `(0,infinity)`.  (6)

Equations (4)–(5) eliminate simultaneous retained coordinates. For bounded test functions supported on retained jumps, the iid-product formula `[E exp(i t X_1/b_m 1_{|X_1|>epsilon b_m}-sum_J s_J Z_{J1}/d_m 1_{Z_{J1}>delta d_m})]^m` therefore converges to the exponential of the **sum** of four axis integrals. Large jumps above an additional R may first be removed; their total probability is `O(R^(-alpha)+R^(-beta))` by (2)–(3), so R can then tend to infinity. The resulting truncated limits are independent compound-Poisson sums. In particular, neither W-sign marking nor the shared U-positive indicator creates a residual joint jump.

To remove the cutoffs, the small-X sum is centered by W symmetry. The product upper-tail bound and tail integration imply, for every fixed epsilon,

`limsup_{m->infinity} (m/b_m^2) E[X^2 1_{|X|<=epsilon b_m}] <= C epsilon^(2-alpha)`.  (7)

Thus its normalized sum is negligible in probability as `epsilon->0`, uniformly in sufficiently large m, by Chebyshev. For any `J=A,B,C`, positivity and the `beta`-tail bound give

`sup_m (m/d_m) E[Z_J 1_{Z_J<=delta d_m}] <= C delta^(1-beta)`,  (8)

so the discarded normalized positive sums vanish in probability as `delta->0` by Markov. The converging-together argument from (6)–(8) proves joint convergence to independent infinitely divisible limits without Gaussian parts or drift (F is symmetric; the positive variables have finite small-jump first moment because `beta<1`).

Finally, the one-sided tail constant K corresponds to Lévy density `beta K x^(-1-beta)` and Laplace exponent `K Gamma(1-beta)s^beta`. The symmetric Lévy density `alpha K |x|^(-1-alpha)` on each half-axis has characteristic exponent `-(K/c_alpha)|t|^alpha`: this follows by integrating `2 alpha K int_0^infinity (cos(tx)-1)x^(-1-alpha)dx`, or by comparing with the standard symmetric stable law whose one-sided tail constant is c_alpha. Insert `K=c_alpha^2` for F and the three K's in (3) to obtain the transforms in the claim.

**Unpaid steps:** None for this finite-dimensional joint limit under the stated iid-within-pair, standard symmetric-stable assumptions. This proof does not cover dependence between U and W, a different stable normalization, or any later dynamical claim in T384.
