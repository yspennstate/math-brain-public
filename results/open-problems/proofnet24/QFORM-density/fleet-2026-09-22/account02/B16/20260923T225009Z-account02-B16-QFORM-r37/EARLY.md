# account02/B16 r37 — early substantive calculation

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: projection-product interaction / source-valid complementary constructions  
Full target status: OPEN.

## First unpaid implication

`QFORM-EPSILON-UNIFORM-PHASEWEIGHTED-TTSTAR-v1`: after the newest account03/B16 fragmented-slice obstruction, the surviving bridge must be a genuinely nonperturbative vector-valued/common-frequency argument. Two preliminary facts are now paid below: (i) the punctured two-bank receiver is stable under arbitrary same-bank measurable phases, including quadratic phases, and (ii) no law-uniform comparison `epsilon -> 0` of characteristic functions can close the bridge, even on an exact-rank-three target-valid product family.

## 1. Phase-weighted pushforward lemma

Let `X` be one original-coordinate source bank and let

`Y=(L,V,P)=T X`

have density `g(l,v,p)`. Let `R(X)` be any real measurable function (in the application, an arbitrary same-bank quadratic polynomial), and fix real `t`. Define the complex pushforward measure

`mu_t(E)=E[ exp(i t R(X)) 1_{Y in E} ]`.

Disintegration over `Y` gives a complex density

`h_t(y)=g(y) E[exp(i t R(X)) | Y=y]`,

hence pointwise

`|h_t(y)| <= g(y)`.                                                   (1.1)

Let

`h_{t,zeta}(l,v)= integral exp(i zeta p) h_t(l,v,p) dp`

and let `m(l,v)=integral g(l,v,p)dp`. Then

`|h_{t,zeta}(l,v)| <= m(l,v)`.                                       (1.2)

Consequently, if `||m||_infinity <= M_2`,

`||h_{t,zeta}||_2^2 <= ||m||_infinity integral m <= M_2`,             (1.3)

uniformly in both `t` and `zeta`. With Fourier convention `hat f(xi)=int exp(-i xi x)f(x)dx`, two-dimensional Plancherel therefore gives

`int_R2 |Phi_t(xi,nu,zeta)|^2 dxi dnu <= (2 pi)^2 M_2`,              (1.4)

where `Phi_t` is the full Fourier transform of `h_t`. Likewise, if `||g||_infinity <= M_3`, then

`int_R3 |Phi_t|^2 <= (2 pi)^3 M_3`.                                  (1.5)

Nothing in (1.1)-(1.5) treats the projected coordinates as independent; the phase is allowed to depend arbitrarily on the same original bank.

For an orthonormal two-dimensional product projection of independent cap-one originals, the completed bounded-density projection theorem used in the pinned `e5f71d79...` package gives `M_2<=2`. Hence (1.3) becomes the concrete Hilbert-slice inequality

`sup_(t,zeta) ||h_{t,zeta}||_2 <= sqrt(2)`.                           (1.6)

This is precisely the safe frequency-side replacement for the fixed-`P` physical slice norm that account03/B16 r34 proved can grow like `sqrt(N)`.

## 2. Phase-weighted extension of the punctured two-bank receiver

Let `H`, source bank `A`, and source bank `B` be mutually independent. Let

`Y_i=(L_i,V_i,P_i)`

have density `g_i`, `(L_i,V_i)` marginal `m_i`, and let `R_i` be any real measurable function of the original coordinates of bank `i`. Put

`L=L_A+L_B`, `V=V_A+V_B`, `P=P_A+P_B`,

`K_2=(M_{2,A}M_{2,B})^(1/2)`, `K_3=(M_{3,A}M_{3,B})^(1/2)`,

where `||m_i||_infinity<=M_{2,i}` and `||g_i||_infinity<=M_{3,i}`. Assume the independent hub density has cap `L_H`.

For

`Q = 2 alpha H L + beta L^2 + 2 delta L V + lambda V^2 + 2 epsilon L P`
`    + R_A + R_B + affine`,

with `alpha*epsilon*lambda != 0`, the account03/B16 r30 Fourier proof survives verbatim after replacing each positive bank density by the phase-weighted complex density from Section 1. Indeed, source independence still makes the two complex pushforwards convolve, while (1.4)-(1.5) give exactly the two energy inputs used in r30. Therefore

`||p_Q||_infinity <= 3 [ L_H K_2 K_3 / |alpha epsilon lambda| ]^(1/3).` (2.1)

The law has a continuous `C_0` density on this punctured branch. Thus arbitrary same-bank quadratic phases are not an additional punctured obstruction; only the `epsilon -> 0` bridge remains.

For two original product banks with three-row Gram at least `kappa I_3`, the actual projection theorem gives `M_2<=2/kappa` and `M_3<=2^(3/2)kappa^(-3/2)`, so

`||p_Q||_infinity <= 3*2^(5/6) kappa^(-5/6) |alpha epsilon lambda|^(-1/3).` (2.2)

## 3. Exact target-valid obstruction to perturbative epsilon comparison

There is no law-uniform perturbative characteristic-function bridge from `epsilon != 0` to `epsilon=0`, even for four independent physical coordinates.

For `epsilon>0` let

`R_epsilon = pi/(2 epsilon)`

and take independent cap-one variables

`H,V ~ Unif[0,1]`,
`L,P ~ Unif[R_epsilon,R_epsilon+1]`.

Define

`Q_epsilon = 2 H L + V^2 + 2 epsilon L P`,
`Q_0       = 2 H L + V^2`,

using the SAME source laws for the comparison, and set

`t_epsilon = 1/R_epsilon = 2 epsilon/pi`.

Then uniformly on the product support,

`2 t_epsilon H L = 2H(1+O(1/R_epsilon)) -> 2H`,
`t_epsilon V^2 -> 0`,
`2 epsilon t_epsilon L P = pi + O(epsilon)`.

Hence by dominated convergence

`phi_epsilon(t_epsilon) -> - integral_0^1 exp(2 i h) dh = - e^i sin(1)`,
`phi_0(t_epsilon)       -> + integral_0^1 exp(2 i h) dh = + e^i sin(1)`.

Therefore

`lim_(epsilon downarrow 0) |phi_epsilon(t_epsilon)-phi_0(t_epsilon)| = 2 sin(1)`
`= 1.6829419696...`.                                                 (3.1)

In particular

`liminf_(epsilon downarrow 0) sup_t |phi_epsilon(t)-phi_0(t)| >= 2 sin(1)`. (3.2)

This is a source-valid obstruction caused only by allowed translations of cap-one laws. No moments, centering, support diameter, or tail assumptions are available in the owner target, so the small coefficient `epsilon` cannot be treated as a small perturbation uniformly over admissible laws.

The matrix of `Q_epsilon` in `(H,L,V,P)` is

`[[0,1,0,0],[1,0,0,epsilon],[0,0,1,0],[0,epsilon,0,0]]`,

whose nonzero eigenvalues are

`{1, +sqrt(1+epsilon^2), -sqrt(1+epsilon^2)}`.                       (3.3)

Thus every `epsilon` member is an exact-rank-three instance of the full owner target. This is an obstruction to a proof mechanism, not a QFORM counterexample.

Moreover the completed ruled one-sheet theorem in the pinned `COUNTEREXAMPLE_SEARCH.md` applies to this exact signature and gives the actual density inequality

`p_(Q_epsilon)(s) <= pi sqrt(2)` for a.e. `s>=0`.                    (3.4)

So (3.1)-(3.2) do not indicate density blow-up; they show only that an epsilon-uniform proof cannot be obtained from law-uniform sup-in-time perturbative continuity of characteristic functions.

## 4. Consequence for the newest partner debt

Account03/B16 r34 showed that fixed-`P` physical slicing followed by Minkowski is impossible even for an orthogonal product projection: its required `L^1_P L^2_(L,V)` norm grows like `sqrt(N)`. Section 1 shows the complementary fact that phase-weighted common-`P` frequency slices retain a universal Hilbert cap, even under arbitrary same-bank phases. Section 3 then rules out the next naive move, namely treating the common-frequency shear generated by `epsilon LP` as a uniformly small perturbation of the exact-zero operator.

The remaining mechanism must therefore be genuinely nonperturbative in `epsilon`: keep the common `P` frequency paired across both original-product banks and use the hub/product structure at each `epsilon`, rather than freezing physical `P` or comparing the `epsilon` operator to the zero operator in norm.
