# T384 marked endpoint Poisson process, independent product initialization, and boundary integral

Assume `0<alpha<2`. Within each iid pair `(U_i,W_i)`, the coordinates are independent standard symmetric `alpha`-stable variables with characteristic function `exp(-|t|^alpha)`. Put `c=Gamma(alpha)sin(pi alpha/2)/pi`, `beta=alpha/2`, `a_m=m^(1/alpha)`, `b_m=(m log m)^(1/alpha)`, and `d_m=m^(2/alpha)`. Define

`N_m=sum_{i=1}^m delta_(W_i/a_m,U_i)` on `E=(R\{0})xR`,

`F_m=b_m^(-1)sum_{i=1}^m W_i(U_i)_+`, and `C_m=d_m^(-1)sum_{i=1}^m (U_i)_+^2`.

**Joint limit.** In the vague point-process topology on E, jointly with the real coordinates,

`(N_m,F_m,C_m) => (N,F,C)`,  (1)

where N is a Poisson random measure with intensity

`mu(dz,du)=alpha c |z|^(-1-alpha) dz P_U(du)` on each half-axis `z>0` and `z<0`, and **N, F, C are mutually independent**. Their transforms are

`E exp(itF)=exp(-c |t|^alpha)`, `E exp(-sC)=exp(-c Gamma(1-beta)s^beta)` for `s>=0`.  (2)

The normalization follows from the standard one-sided stable tail `P(W>x)~c x^(-alpha)`, which also holds for `-W`; this constant is recorded in [Bednorz–Łochowski–Martynek, arXiv:1802.00612v3](https://arxiv.org/html/1802.00612v3), Introduction. The product tail and the full four-coordinate joint-limit proof are in the local [T384_joint_limit.md](T384_joint_limit.md); the argument below makes independence from the **entire marked point process** explicit.

## Marginal Poisson limit with marks

Regular variation of W gives `mP(W/a_m>z)->c z^(-alpha)` and `mP(W/a_m<-z)->c z^(-alpha)` for each `z>0`, so `mP(W/a_m in dz)` converges vaguely away from zero to `alpha c |z|^(-1-alpha)dz` on each half-axis. For any nonnegative continuous compactly supported `g` on E, independence of W and U yields

`m E[1-exp(-g(W/a_m,U))] -> int_E [1-exp(-g(z,u))]mu(dz,du)`.  (3)

Indeed, integrate first in u, then use vague convergence of the W-tail measures; the integrated test function is continuous with compact z support. Thus the iid Laplace functional

`E exp(-<g,N_m>)=[1-E(1-exp(-g(W/a_m,U)))]^m -> exp(-int(1-exp(-g))dmu)`,

the PPP Laplace functional. This identifies a genuine mark law `P_U`: an endpoint W jump does not rescale its U mark. The vague topology alone does not control marks escaping to infinity, but for any `eta,L>0`, the expected number of observations with `|W|/a_m>eta` and `|U|>L` is at most `C eta^(-alpha)P(|U|>L)`; the analogous PPP expectation is `2c eta^(-alpha)P(|U|>L)`. Letting L grow supplies the needed mark truncation whenever a functional uses all marks.

## Why N is independent of F and C

First retain only jumps of F exceeding a fixed `epsilon>0` and jumps of C exceeding a fixed `delta>0`: write `F_m^(epsilon)=sum (W_iU_{i,+}/b_m)1_{|W_iU_{i,+}|>epsilon b_m}` and `C_m^(delta)=sum (U_{i,+}^2/d_m)1_{U_{i,+}^2>delta d_m}`. For `g` as above, let eta>0 be the minimum |z| in its support. A W-endpoint observation contributes negligibly to a simultaneous F jump:

`m P(|W|>eta a_m, |W U_+|>epsilon b_m)->0`.  (4)

To prove this, fix `L>eta`. On `|W|>L a_m` the limsup is at most `C L^(-alpha)`. On `eta a_m<|W|<=L a_m`, a product jump forces `U_+>(epsilon/L)(log m)^(1/alpha)`, an event of probability tending to zero independently of W, while `mP(|W|>eta a_m)=O(1)`. Send m and then L to infinity.

Similarly, independence of U and W gives

`m P(|W|>eta a_m, U_+^2>delta d_m)=O(m^(-1))->0`.  (5)

Finally, `mP(|WU_+|>epsilon b_m,U_+^2>delta d_m)->0`: split `U_+>L a_m` (limsup `O(L^(-alpha))`) and `sqrt(delta)a_m<U_+<=L a_m`, where a product jump forces `|W|>(epsilon/L)(log m)^(1/alpha)`; its probability tends to zero independently of U. Thus no one sample has two retained coordinates asymptotically.

The exact one-sided product-tail calculation gives

`P(WU_+>t)=P(WU_+<-t) ~ alpha c^2 t^(-alpha)log t`,

and hence `mP(WU_+/b_m>x)->c^2 x^(-alpha)` and the same for the negative tail. Also `mP(U_+^2/d_m>x)->c x^(-beta)`. Consequently the large-jump Lévy measures are `nu_F(dx)=alpha c^2 |x|^(-1-alpha)dx` on each half-axis and `nu_C(dx)=beta c x^(-1-beta)dx` on the positive half-axis.

For the triple `(N_m,F_m^(epsilon),C_m^(delta))`, expand the one-sample transform

`E exp{-g(W/a_m,U)+it(WU_+/b_m)1_{|WU_+|>epsilon b_m}-s(U_+^2/d_m)1_{U_+^2>delta d_m}}`.

After multiplying its deviation from 1 by m, the terms for N, F, and C converge separately to their Poisson/Lévy integrals by (3) and the tail limits. Every mixed term is bounded by a constant times one of the cross probabilities (4)–(5) or the F/C version, hence tends to zero. Raising the one-sample transform to the mth power yields the **product** of the PPP Laplace functional and the two truncated compound-Poisson transforms. This proves independence at fixed cutoffs, not merely marginal convergence.

The cutoff removal is quantitative. The product-tail upper bound `P(|WU_+|>t)<=Ct^(-alpha)(1+log t)` and symmetry of `WU_+` imply

`limsup_m E[(F_m-F_m^(epsilon))^2] <= C epsilon^(2-alpha)`;  (6)

the discarded terms have mean zero and independence across i, so no centering is missing even when `alpha>=1`. Since `P(U_+^2>t)<=Ct^(-beta)` and `beta<1`,

`sup_m E[C_m-C_m^(delta)] <= C delta^(1-beta)`.  (7)

Chebyshev/Markov and then `epsilon,delta->0` give (1), with independence from N retained. Evaluating the two axis Lévy integrals gives (2): a symmetric Lévy tail constant `c^2` corresponds to exponent `c|t|^alpha`, and a positive beta-stable tail constant c to Laplace exponent `c Gamma(1-beta)s^beta`.

## The boundary integral is finite and a fixed-s continuous-mapping limit

For fixed real `y` and `s>=0`, define

`H_1(s)=int_E z^2 1_{u>0}1_{u+(y-F)zs>0} N(dz,du)`.  (8)

Its small-z part obeys the exact unconditional estimate

`E[int_{|z|<=epsilon} z^2 1_{u>0,u+(y-F)zs>0}dN] <= int_{|z|<=epsilon} z^2 dmu`

`= (2 alpha c/(2-alpha)) epsilon^(2-alpha)`.  (9)

This is also a uniform-in-s upper bound, since the indicator is at most one. For `|z|>R`, the PPP has any atom with probability at most `mu(|z|>R)=2c R^(-alpha)`; there are a.s. finitely many such atoms and each has finite z. Thus (8) is finite a.s. despite potentially infinite expectation from its largest atom.

The finite-m counterpart, with F_m substituted for F in (8) and N_m for N, has a small-z expectation at most

`m/a_m^2 E[W^2 1_{|W|<=epsilon a_m}] <= C epsilon^(2-alpha)`  (10)

for all sufficiently large m (indeed a suitably enlarged C works uniformly); its probability of an atom `|z|>R` is at most `C R^(-alpha)`. These bounds do not use independence between F_m and N_m, because they simply discard the indicators.

On an annulus `epsilon<=|z|<=R` with marks `|u|<=L`, there are finitely many limit atoms. The only boundary discontinuities of the integrand at a fixed s are `u=0` and `u+(y-F)zs=0` (and the artificial truncation boundaries). The stable mark U has a continuous law, and F is independent of N, so the intensity/conditional mark law assigns each boundary probability zero, even for `s=0`. Choose continuity cutoffs epsilon,R,L, apply the joint continuous-mapping theorem to `(N_m,F_m,C_m)`, then let `L,R->infinity` and `epsilon->0` using the mark-tail estimate and (9)–(10). Therefore, for each fixed s,

`(F_m,C_m,H_{1,m}(s)) => (F,C,H_1(s))`,  (11)

and the same holds jointly for any finite list of fixed times. Equation (11) does **not** claim path-space convergence of `s↦H_{1,m}(s)`; that requires an explicit topology and control of jump-time alignment. The small-z truncation bounds here are uniform in s and can be used in that separate argument.

**Unpaid steps:** none for (1)–(11) at fixed times under the stated iid assumptions. A boundary-layer **dynamical** replacement of the finite-m first-layer weights by `u+(y-F)zs`, or a whole-path kernel theorem, is not implied by this initialization/point-process result.
