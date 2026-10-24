SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B16, 2026-09-22T21:10:47Z.
attacking: grouped product projection before the curved quadratic pushforward, with two independent full-dimensional spectral banks.

# account01/B16 — grouped L2-Fresnel bridge

Status: `ESSENTIAL_STEP_APPLIED`; full QFORM OPEN / NOT PROVED; continuity open in full generality. Execution: `WITHOUT_VERIFIED_BRAIN`.

Source controls at start: `yspennstate/math-research-brain@b02969f5b8e9c9313119bc8cc62bb41a4d09983d`, OWNER CONTROL revision `2026-09-22.15`; refreshed before publication at `4b9e16afc8d1cbd72e438e6468b065451b2c437b`, same programme. Assignment: projection-product interaction. Live corrections consumed: arbitrary-joint coarea false; positive conditional projection-height moments false; projected coordinates are not independent after rotation; scalar residual conditional-sup gate false; absolute phase-Wiener and coordinatewise mixed-BL routes cannot be used as universal interfaces.

Designated partner actually consumed: account02/B16 `20260922T203148Z-account02-B16-QFORM-auto11`, canonical report `yspennstate/math-open-problems@484069f14f49a3303befbe62863d950e67c809e1:proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260922T203148Z-account02-B16-QFORM-auto11/REPORT.md`. It proves (i) the mixed ambiguity/section-mass BL sufficient estimate, (ii) the exact barrier `Theta<=4` on `A_m=[1] direct_sum J_m/m direct_sum (-J_m/m)`, and (iii) the source-grouped bound `||p_Qm||_infinity<=pi sqrt(2)`. The present theorem implements its prescribed repair: group original product coordinates before taking an absolute Fourier norm.

## Theorem 1 — QFORM-GROUPED-L2-FRESNEL-v1

Let `[n]=I_1 disjoint_union ... disjoint_union I_r`, and let the original coordinate blocks `X_{I_g}` be independent. Let `E_g` be linear subspaces of `R^3` of dimensions `d_g`, and let `Y_g=T_g X_{I_g}` take values in `E_g`. Assume each `Y_g` has a density `rho_g` with respect to Lebesgue measure on `E_g` satisfying `||rho_g||_infinity<=M_g`.

Let `Lambda` be a real invertible symmetric `3x3` matrix and let `H_g(X_{I_g})` be arbitrary measurable real functions. Put

`Q=(Y_1+...+Y_r)^T Lambda (Y_1+...+Y_r)+sum_g H_g(X_{I_g})`.

Assume the geometric L2 Brascamp--Lieb estimate

`int_(R^3) prod_g F_g(P_{E_g} xi) dxi <= B prod_g ||F_g||_(L2(E_g))`                 (1)

holds for all nonnegative `F_g`, and necessarily `sum_g d_g=6` by scaling. Then `Q` has a bounded continuous density and

`||p_Q||_infinity <= 3 |det Lambda|^(-1/3) B^(2/3) prod_g M_g^(1/3)`.               (2)

### Proof

For fixed `t`, define the complex pushforward measure

`mu_(g,t)(B)=E[ 1_{Y_g in B} exp(i t H_g(X_{I_g})) ]`.

It is absolutely continuous with density `a_(g,t)` satisfying `|a_(g,t)|<=rho_g`, hence

`||a_(g,t)||_1<=1`, `||a_(g,t)||_2<=M_g^(1/2)`.

With Fourier convention `hat a(xi)=int exp(i xi.y)a(y)dy`, Plancherel gives

`||hat a_(g,t)||_2 <= (2pi)^(d_g/2) M_g^(1/2)`.                       (3)

Because the source blocks are genuinely independent,

`phi_Q(t)=int exp(i t y^T Lambda y) c_t(y)dy`,

where `c_t=mu_(1,t)*...*mu_(r,t)` as a complex convolution on `R^3`, and

`hat c_t(xi)=prod_g hat a_(g,t)(P_(E_g)xi)`.

Applying (1), (3), and `sum d_g=6`,

`||hat c_t||_1 <= B (2pi)^3 prod_g M_g^(1/2)`.                        (4)

Fourier inversion for `c_t` and the Fresnel identity, regularized first by `exp(-eps |y|^2)` and then letting `eps downarrow0`, give for `t!=0`

`|phi_Q(t)| <= pi^(3/2) |t|^(-3/2) |det Lambda|^(-1/2) B prod_g M_g^(1/2)`.  (5)

Together with `|phi_Q(t)|<=1`, write the coefficient in (5) as `K`. Then

`int_R |phi_Q(t)|dt <= int_R min(1,K|t|^(-3/2))dt = 6 K^(2/3)`.       (6)

Fourier inversion therefore gives a bounded continuous density and

`||p_Q||_infinity <= (1/(2pi))*6K^(2/3)=3 |det Lambda|^(-1/3) B^(2/3) prod_g M_g^(1/3)`.

This proves (2).

## Corollary 2 — two full product banks

Let `U` be `n x 3` with orthonormal columns, rows `u_i^T`, and split the original coordinates into two disjoint blocks `I,J`. Put

`S_I=sum_(i in I) u_i u_i^T`, `S_J=I_3-S_I`.

Assume both are positive definite. Let `Y_I=U_I^T X_I`, `Y_J=U_J^T X_J`. The sharp product-marginal theorem of Livshyts--Paouris--Pivovarov gives, after normalizing each frame,

`||p_(Y_I)||_infinity <= 2^(3/2)/sqrt(det S_I)`,
`||p_(Y_J)||_infinity <= 2^(3/2)/sqrt(det S_J)`.                     (7)

Apply Theorem 1 with `E_I=E_J=R^3`, `B=1`. For arbitrary block-separable perturbations `H_I(X_I)+H_J(X_J)`,

`boxed(||p_Q||_infinity <= 6 |det Lambda|^(-1/3) (det S_I det S_J)^(-1/6))`.  (8)

In particular, if `S_I,S_J >= alpha I_3` and `|det Lambda|>=1`, then

`boxed(||p_Q||_infinity <= 6/alpha)`.                                (9)

Unlike a conditional projected-density supremum, this argument never conditions on a thin spectral fiber. It uses the unconditional product-projection theorem on each independent physical block and then performs the curved quadratic integration jointly.

## Corollary 3 — a quantitative diffuse split

Assume `max_i ||u_i||^2 <= 1/20`. Color the rows independently with Bernoulli(1/2), and write

`S_I-I/2=sum_i (xi_i-1/2)u_i u_i^T`.

Matrix Bernstein has `R<=delta/2`, variance proxy `sigma^2<=delta/4`, so

`P(||S_I-I/2||>=1/4) <= 6 exp(-3/(28 delta))`.

At `delta=1/20`, the right side is `<0.704<1`; hence a deterministic split exists with

`(1/4)I_3 <= S_I,S_J <= (3/4)I_3`.                                  (10)

Therefore every rank-three spectral quadratic with `max_i ||u_i||^2<=1/20`, and more generally every such large spectral quadratic plus an arbitrary perturbation that is block-separable across this split, satisfies

`boxed(||p_Q||_infinity <=24)`                                       (11)

and has a continuous density. For exact rank three this is a source-product proof of the diffuse branch; its main added value over earlier exact-rank-three results is stability under arbitrary group-separable extra quadratic/linear terms.

## Designated-partner stress family applied at inequality level

For the partner family

`A_m=[1] direct_sum (J_m/m) direct_sum (-J_m/m)`, `spec(A_m)={1,1,-1}`,

put `Y_+=m^(-1/2)sum_(B+)X_j`, `Y_-=m^(-1/2)sum_(B-)X_j`. The partner's source-valid product-projection estimate gives `||p_Y+||_infinity,||p_Y-||_infinity<=sqrt(2)`. Since the three source banks are disjoint,

`p_(X_0^2)(s)<=s^(-1/2)`, `p_(Y_+^2)(s)<=sqrt(2)s^(-1/2)` for `s>0`,

and hence

`||p_(X_0^2+Y_+^2)||_infinity <= sqrt(2) int_0^r [s(r-s)]^(-1/2)ds = pi sqrt(2)`.

Convolution with the independent law of `-Y_-^2` preserves this bound, so

`boxed(||p_(Q_m)||_infinity<=pi sqrt(2))`.                            (12)

Thus the partner's exact `Theta<=4` coordinatewise-BL obstruction is not a density obstruction. Corollary 2 handles the complementary geometry in which two physical banks each already carry all three spectral directions; (12) handles the sparse rank-one-bank extreme. The remaining structural gap is the mixed-rank/overlapping-bank passage.

## What remains unpaid

The full conjecture is not proved. In a general full-rank matrix, after selecting three large spectral directions, the residual quadratic form need not be block-separable across any favorable split; cross-block residual terms couple the two complex pushforward measures and destroy the exact convolution used in Theorem 1. The next target is therefore:

`QFORM-GROUPED-L2-FRESNEL-CROSSBLOCK-v1`: control a cross-block residual `2 X_I^T C X_J` while retaining enough of the two-bank L2 Fourier budget to keep the `|t|^(-3/2)` Fresnel decay, or prove an exhaustive reduction forcing either (a) a favorable group-separable split, (b) the already-paid physical-pair/ridge branch, or (c) the partner's rank-one bank aggregation branch.

No full-target status is promoted from this supporting theorem.
