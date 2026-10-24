# T384 positive-correlation same-sign entrance and selected square mass

**Status:** exact frozen-grid classification and original-mark mass law. This is a restricted internal result, not a proof of the residual-coupled path after an axis crossing. Actual backend metadata is UNKNOWN; `gpt-6-sol max` was requested. No external priority claim is made.

Dependencies: `../../20261023T232238Z/BOUNDARY_GRID.md` for the strict pre-step endpoint recursion, the independent primitive `(F,C,N)`, and the original-coordinate stable marks; `../../20261023T232238Z/MACRO_COMPACTNESS.md` for the separate macroscopic transfer bounds; and `../../20261024T021857Z/{ALL_MIXED_LIMIT.md,GLOBAL_REFLECTION.md,DIRECTIONS.md}` for the scope at a later mixed-sign crossing. The same-sign theorem below is deterministic conditional on a frozen residual and does not invoke reflection.

## Exact classifier, including axes

Let `G=[[1,rho],[rho,1]]`, `0<rho<1`, `gamma>0`, `v_0=(x_0,y_0)=Xu`, and

\[
v_{n+1}=v_n+\gamma zG D(v_n)R,
\qquad D(v)=\operatorname{diag}(1_{v_1>0},1_{v_2>0}). \tag{1}
\]

Fix `R_1,R_2>0`. Then:

* If `z>0`, a row with `x_0<=0,y_0<=0` is stationary and dead. Every row with `x_0>0` **or** `y_0>0` reaches `++` after finitely many steps and stays `++` forever. No genericity assumption is needed for this dichotomy. In particular, an initially zero coordinate is off but is activated if the other coordinate is positive.
* If `z<0`, every row reaches the closed nonpositive quadrant after finitely many steps and stays dead. This includes a row starting `++`, a single-gate row, and an initially dead row. The terminal pair is strictly negative for generic original marks, though the exact classifier uses `<=0` and does not need that extra condition.

For explicit bounds, put `w=|z|` and let `k` denote the coordinate other than `j`. In the positive-`z` active case, at least one gate remains on: every active projection strictly increases. At each step,

\[
v_{n+1,j}-v_{n,j}\ge \delta_j
:=\gamma w\min(R_j,\rho R_k)>0. \tag{2}
\]

Thus the first `++` state occurs no later than `N_+=max_j N_j^+`, where `N_j^+=0` if `v_{0,j}>0` and otherwise

\[
N_j^+=\left\lfloor\frac{-v_{0,j}}{\delta_j}\right\rfloor+1. \tag{3}
\]

For `z<0`, both coordinates are nonincreasing, and whenever coordinate `j` is positive it decreases by at least `gamma*w*R_j` in one step. Hence the dead state occurs no later than

\[
N_- = \max_j \left\lceil\frac{(v_{0,j})_+}{\gamma wR_j}\right\rceil. \tag{4}
\]

These are finite integer bounds even at exact pre-step axis hits. Once `++` is reached in the first case, each increment is `gamma*z*G R`, whose coordinates are strictly positive. Once both gates are off in the second case, every later increment is zero.

The sign mirror is immediate from the product `zR` in (1): for `R_1,R_2<0`, replace `R` by `-R` and `z` by `-z`. Consequently **negative** `z` rows with any initially active projection reach and retain `++`, while **positive** `z` rows die. No swap of the two input coordinates is involved.

For generic marked-Poisson atoms, every finite tested projection is an initial projected mark plus a gate-word-dependent constant. Since `X` has rank two and `U` has a density, each finite axis equality belongs to a null affine hyperplane. A countable union over gate words, times and atoms is null. Thus the finite `++` and strictly negative death states provide open, perturbation-robust certificates at every generic atom. If a later *varying* residual and retained output weight keep their same signs, `++` remains invariant for the growing-sign population, while a dead row remains exactly dead. This observation by itself does not justify a macroscopic selection theorem through an axis crossing.

## Exact original-mark selected mass

Let

\[
A(u)=\mathbf1\{(Xu)_1>0\ \text{or}\ (Xu)_2>0\},\qquad
\pi_X=\Pr_U(A(U)=1)=1-\Pr_U(XU\in(-\infty,0]^2). \tag{5}
\]

For a positive initial residual, the frozen surviving square mass is

\[
P_+=\int_{z>0}z^2 A(u)\,N(dz,du); \tag{6}
\]

for a negative initial residual it is `P_-` with `z<0` in (6). The two variables are iid and independent because the positive and negative halves of `N` are independent. They are also independent of `(F,C)` and hence of `R=y-F`, under the joint primitive in `BOUNDARY_GRID.md`. Write `p=alpha/2` and `c_alpha=Gamma(alpha)sin(pi alpha/2)/pi`. The intensity of `N` is `alpha*c_alpha*|z|^{-1-alpha} dz P_U(du)`, so independent thinning and the substitution `s=z^2` give the exact Laplace law

\[
\mathbb E e^{-\lambda P_\pm}
=\exp\{-\pi_X c_\alpha\Gamma(1-p)\lambda^p\},\qquad \lambda\ge0. \tag{7}
\]

Thus each is a finite, strictly positive, positive `alpha/2`-stable mass. Its law is independent of the critical multiplier `gamma` and of the value of `R` within either open same-sign quadrant. The probability `pi_X` belongs to the **original-coordinate projection mark law**. It is not in general a function of the Gram correlation `rho` alone.

Here is a computable exact formula which retains that mark law. For iid positive `p`-stable `S_l` with Laplace transform `E exp(-tS_l)=exp(-t^p)`, and independent standard normal `H_l`, the variables `sqrt(2S_l)H_l` are iid standard symmetric `alpha`-stable. Conditional on `S`, the two projections are centered Gaussian with random correlation

\[
\rho_S=\frac{\sum_l S_l x_{1l}x_{2l}}
{\sqrt{(\sum_l S_l x_{1l}^2)(\sum_l S_l x_{2l}^2)}}.
\]

For centered bivariate normals, the negative-orthant probability is `1/4+arcsin(q)/(2pi)` at correlation `q`: its derivative in `q` is `1/(2pi*sqrt(1-q^2))` and its value at `q=0` is `1/4`. Conditional Gaussian orthant integration followed by averaging therefore yields

\[
\boxed{\displaystyle
\pi_X=\frac34-\frac{1}{2\pi}\mathbb E_S[\arcsin(\rho_S)] .} \tag{8}
\]

The rank-two condition makes `|rho_S|<1` almost surely. In particular `1/2<pi_X<1`. Formula (8) is an *average of conditional Gaussian angles*, not the generally false shortcut `3/4-arcsin(rho)/(2pi)`. The latter follows only when the conditional correlation is constant (for example the Gaussian `alpha=2` limit or an appropriately elliptical stable mark), which independent original-coordinate `alpha`-stable marks do not generally satisfy.

Here is a rigorous same-Gram counterexample to the fixed-angle shortcut. Take `alpha=1`, `d=2`, `rho=1/2`. Let `X_A` have rows `(1,0)`, `(1/2,sqrt(3)/2)`, and `X_B` have rows `(sqrt(3)/2,1/2)`, `(sqrt(3)/2,-1/2)`. Both have the same Gram matrix. The positive scale variables can be represented as `S_l=1/(2J_l^2)` with independent standard normals `J_l` (also independent of the conditional Gaussian variables above). Hence `T=sqrt(S_2/S_1)=|J_1/J_2|` has half-Cauchy density `2/[pi(1+t^2)]` and the same law as `1/T`. Put `a=1/sqrt(3)` and `A=E[atan(aT)]`. In (8), the conditional correlations for `X_A` and `X_B` are respectively `1/sqrt(1+3T^2)` and `(3-T^2)/(3+T^2)`. Their arcsines are `atan(a/T)` and `pi/2-2atan(aT)`. Inversion symmetry of `T` therefore gives the **exact** identities

\[
\pi_{X_A}=\frac34-\frac{A}{2\pi},\qquad
\pi_{X_B}=\frac12+\frac{A}{\pi}. \tag{9}
\]

These differ strictly, without numerical quadrature. Because `a^2<1`, both `atan(aT)+atan(a/T)` and `2atan(a)` lie in `(0,pi/2)`. Their tangents are respectively `a(T+T^{-1})/(1-a^2)` and `2a/(1-a^2)`. Since `T+T^{-1}>2` almost surely, the first angle is strictly larger. But `2atan(a)=pi/3`; taking expectations and using the inversion law yields `A>pi/6`. Also `A<pi/4`, since `a<1` and `atan(T)` is uniform on `(0,pi/2)`. Substitution in (9) gives `pi_{X_A}<2/3<pi_{X_B}`. The fixed-Gram Gaussian-angle shortcut would assign `2/3` to **both**, so it is false for these original-coordinate Cauchy marks. For an optional numerical check, `../code/i01_mark_probability_quad.py` and `../outputs/i01_mark_probability_quad.txt` report approximately `0.65237132` and `0.69525736`; the strict conclusion rests on the analytic inequality above.

## Consequence and boundary of this result

If all selected rows are tracked only while the residual remains in its initial positive quadrant, their finite entrance and full-gate increments suggest the local action `Q=C+P_+ G`; the negative quadrant uses `C+P_- G`. Deterministically `Q_12=C_12+rho P_\pm>0` almost surely, since `P_\pm>0`. Accordingly the constant-`Q` flow `r(t)=exp(-Qt)R` either stays same-sign at every finite time or, at its first residual-axis hit, crosses transversally into a mixed quadrant: the zero coordinate has derivative `-Q_12` times the still-positive coordinate (with the mirrored sign in the negative quadrant). An invertible matrix exponential prevents simultaneous finite-time extinction of both coordinates.

This does **not** identify the actual network after that hit. Surviving endpoints then carry positive inherited projections; the earlier mixed-quadrant reflected equation starts from those inherited states, not from a fresh zero endpoint. A path law through and beyond the crossing needs a separate finite-cutoff matching and relay argument. The exact-rational script `../code/i01_entrance_check.py` and its executed output `../outputs/i01_entrance_check.txt` check (1)–(4), absorption/persistence, strict-gate axis behavior, and the sign mirror over a finite grid; they are checks, not a substitute for the proof above.
