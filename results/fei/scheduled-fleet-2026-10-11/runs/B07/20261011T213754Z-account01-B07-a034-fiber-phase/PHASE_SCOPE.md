# A034 phase-energy scope ledger

## Exact setting

- Physical domain: disjoint cubes `{-1,1}^X × {-1,1}^Y` with all coordinates independent and uniform.
- Function: genuine Boolean sign `f ∈ {-1,1}`.
- Spectral law: `P(R,T)=fhat(R,T)^2`; arbitrary dependence among the spectral `Y` coordinates is allowed.
- Degree: every nonzero coefficient has integer `X`-degree `|R|≤d`, `d≥1`.
- New structural condition: for every positive-mass `R`, at most `K` sets `T` have `fhat(R,T)≠0`.

## What is paid

The proof preserves the exact chain rule

`H(f)=H(p_X)+H(S_Y|S_X)`.

The marginal term is paid once by

`H(p_X) ≤ (2/ln 2) I_Y(f)+2(d−1)−E_y Gamma_d(f_y)`.

The conditional term is then paid independently by the support inequality

`H(S_Y|S_X) ≤ log_2 K`.

No influence appearing in the marginal estimate is charged again to the conditional term.

## Boolean-only deficit

For every physical slice, Boolean degree granularity gives

`c_R(y)=2^(1−d)m_R(y)`, `m_R(y)∈Z`, and `sum_R m_R(y)^2=4^(d−1)`.

Hence

`H(f_y)=2(d−1)−Gamma_d(f_y)`,

where `Gamma_d=4^(1−d) sum_R m_R^2 log_2(m_R^2)≥0`. This identity fails for an arbitrary normalized spectral probability vector and is not a relaxation of Boolean realizability.

## Fixed-cyclic-marginal tensor test

For a fixed seed `f(X,Y)` and arbitrary Boolean `g(Z)` on disjoint coordinates,

`F=f·g` has `Fhat(R,T,U)=fhat(R,T) ghat(U)`.

Therefore:

- the `X` marginal and `X`-degree are unchanged;
- each positive `X`-fiber support is multiplied by `|supp(ghat)|`;
- `H_F(S_{Y∪Z}|S_X)=H_f(S_Y|S_X)+H(g)`.

For `g^{⊗t}`, the support multiplier is `|supp(ghat)|^t`. If `H(g)>0`, this grows at least as `2^t`, so fixed `K` excludes the arbitrary-tensor embedding. If `|supp(ghat)|=1`, `g` is a character and has zero spectral entropy. The exclusion is an exact support statement and does not assume FEI.

## Stability actually proved

- adjoining dummy physical variables: `d,K` unchanged;
- permuting variables within blocks: `d,K` unchanged;
- multiplying by a `Y`-character: each fiber is translated, so `K` is unchanged;
- disjoint products: degree bounds add and fiber-support bounds multiply.

Restrictions can merge Fourier frequencies and unions can enlarge support. No hereditary restriction-closure claim is made. The variance reserve `Var(f)≥ν` must also be rechecked after operations that may change the mean.

## Restricted FEI consequence

If `Var(f)≥ν>0`, Poincaré gives `I(f)≥ν`, and therefore

`H(f) ≤ [2/ln2+(2(d−1)+log_2 K)/ν] I(f)−E Gamma_d`.

For balanced functions, `ν=1`. This is dimension independent for fixed `(d,K,ν)` and includes unbounded-dimensional examples such as `f(x,y)=x_1 χ_T(y)`, for which `(d,K,ν)=(1,1,1)` regardless of `|T|`.

## What remains open

Full FEI remains open. Arbitrary Boolean functions need not have bounded `d`, bounded fiber support `K`, or a fixed variance reserve. No universal representation into fiber-sparse pieces with globally paid labels, ranks, or activation costs is proved here.
