# Addendum — critical loss in the naive decoupled-L3 implementation

This addendum addresses the newer owner-control template that starts from the exact symmetrization/decoupling identity. It does **not** refute that identity or the full QFORM conjecture. It proves that one tempting implementation — normalize the conditional `V_j|U_j`, take absolute values, apply coordinatewise `L^3` Hausdorff-Young, and then average in `U` — has an unavoidable logarithmic loss even in the diagonal target case.

## 1. Exact one-coordinate decoupling objects

Let `X,X'` be iid with cap-one density `f`. Put

`U=X-X'`, `V=X+X'`.

The density of `U` is

`g(u)=int_R f(x)f(x-u)dx`.                                    (1.1)

For `g(u)>0`, the conditional density of `V|U=u` is

`h_u(v)= f((v+u)/2) f((v-u)/2) / [2 g(u)]`.                   (1.2)

Hence

`||h_u||_infinity <= [2g(u)]^(-1)`.                           (1.3)

Let

`psi_u(s)=E[exp(i s V)|U=u]`.

Hausdorff-Young with exponents `3/2 -> 3` gives

`||psi_u||_3 <= (pi/g(u))^(1/3)`,                             (1.4)

because `||h_u||_(3/2) <= [2g(u)]^(-1/3)` and the nonunitary Fourier constant is `(2pi)^(1/3)`. Therefore, after the scalar rescaling `s=t a`,

`||psi_u(a .)||_3^3 <= pi / [|a| g(u)]`.                      (1.5)

For the diagonal three-variable form `Q=X_1^2+X_2^2+X_3^2`, the exact identity is

`|phi_Q(t)|^2
 = E_U product_(j=1)^3 psi_(U_j)(t U_j)`.                    (1.6)

Taking absolute values before the `U` average and applying Holder in `t` gives the majorant

`int_R |phi_Q(t)|^2 dt
 <= pi [ I(f) ]^3`,                                            (1.7)

where

`I(f)=int_R g(u)^(2/3) |u|^(-1/3) du`.                        (1.8)

Thus the naive normalized-conditional `L^3` route is only useful if `I(f)` is uniformly bounded. The next section shows it is not.

## 2. A target-valid family with critical logarithmic growth

For `R>e`, let `L=log R` and take

`f_R(x)=1_[1,R](x)/(x L)`.                                    (2.1)

This is a probability density and `f_R<=1`. For `0<u<R-1`, direct integration gives the exact difference density

`g_R(u)
 = [1/(L^2 u)] log( ((R-u)(1+u))/R )`.                        (2.2)

Indeed,

`g_R(u)=L^(-2) int_(1+u)^R dx/[x(x-u)]`
`       =(L^(-2)/u)[log(R-u)-log R+log(1+u)]`.

For `4<=u<=R/2`,

`(R-u)/R >=1/2`

and

`log(u/2)>= (1/2)log u`.

Hence

`g_R(u) >= [log u]/[2 L^2 u]`.                                (2.3)

Substituting (2.3) into (1.8), and using only the positive half-line,

`I(f_R)
 >= 2^(-2/3) L^(-4/3)
    int_4^(R/2) (log u)^(2/3) du/u`
` = [3/(5*2^(2/3))] L^(-4/3)
   [ (log(R/2))^(5/3) - (log 4)^(5/3) ]`.                    (2.4)

Consequently

`I(f_R) ~ [3/(5*2^(2/3))] (log R)^(1/3)`,                    (2.5)

and the coordinatewise-decoupling majorant in (1.7) grows at least on the order of

`pi I(f_R)^3 ~ (27 pi/500) log R`.                             (2.6)

This divergence occurs inside the exact diagonal QFORM target family.

## 3. The exact oscillatory integral remains uniformly bounded

The divergence above is purely a loss of the **proof interface**, not of the target quantity. By `QFORM-TRANSLATED-FRESNEL-LP-v1` from the main report of this run, each one-dimensional quadratic phase satisfies

`||E exp(i t X_j^2)||_3 <= (32 pi)^(1/3)`

for every cap-one input law. Since the diagonal characteristic function factors before symmetrization,

`int_R |phi_Q(t)|dt <= 32 pi`                                  (3.1)

uniformly in `R`; independently, the classical same-sign square convolution gives the sharper density bound `pi`.

Therefore the decoupled conditional normalization followed by absolute-value `L^3` averaging destroys exactly the cancellation needed at the critical exponent.

## 4. Precise consequence for the live decoupling programme

The identity (1.6) remains valid and may still be useful. What is ruled out is the following intermediate mechanism:

> normalize each `V_j|U_j`, bound its time `L^3` norm separately by its conditional density cap, take absolute values, and then average the resulting reciprocal `g(U_j)` costs coordinatewise.

Any successful decoupling proof must instead keep the unnormalized overlap kernels

`K_f(u,s)=g(u) psi_u(s)
         =int f(x)f(x-u) exp(i s(2x-u)) dx`                   (4.1)

coupled across `u` and `s`, or exploit cancellation before the critical `U` integration. The universal mixed identity

`int_R int_R |K_f(u,s)|^2 ds du
 <= pi`                                                        (4.2)

follows from Plancherel and `f<=1`, but by itself does not close the full theorem; its useful synthesis with the three-large-eigenvalue geometry remains unpaid.

This is consistent with the earlier source correction `QFORM-ABSOLUTE-AMBIGUITY-HOLDER-LOG-LOSS`; the present derivation pins the same obstruction directly to the newly emphasized conditional-decoupling `L^3` template and provides the exact critical weight and asymptotic growth.
