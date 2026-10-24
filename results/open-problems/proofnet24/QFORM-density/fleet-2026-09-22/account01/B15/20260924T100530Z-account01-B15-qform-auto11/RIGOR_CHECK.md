# Rigor check — account01/B15 20260924T100530Z

Status: supporting regularity theorems checked; full QFORM still OPEN.

## A. Low-leverage contraction algebra

Let `R^T R=I_3`, scale coordinate `i` by `m in (0,1]`, let `r=R_{i,*}^T`, `a=|r|^2`, and `U=S_m R`. Then

`G=U^T U=I-(1-m^2)rr^T`,
`d=det G=1-(1-m^2)a`,
`G^{-1}=I+(1-m^2)d^{-1}rr^T`.

For the whitened frame `W=UG^{-1/2`, the leverage of the scaled row is

`ell_i=m^2 a/d <= a`,

because `d-m^2=(1-a)(1-m^2)>=0`.

For `j!=i`,

`ell_j=a_j+(1-m^2)d^{-1}<r_j,r>^2
      <=a_j[1+(1-m^2)a/d]
      =a_j/d`.

If every original leverage is `<=theta<=1/3`, then

`ell_j<=theta/(1-theta)<=1/2`.

Thus the completed Theorem-F threshold is preserved under arbitrarily severe contraction of one original coordinate.

The three whitened eigenvalue product is

`|det(G^{1/2} Lambda G^{1/2})|=d |det Lambda|`.

Theorem F therefore gives normalized height

`12[d |det Lambda|]^(-1/3)`.

The source-subdensity Jacobian is exactly `m`, because with `x_i=m z_i` and `g(z)=h(mz)`,

`h(x_i)dx_i=m g(z_i)dz_i`, `int g=1`, `g<=1`.

Hence the submeasure height is exactly bounded by

`12 m [d |det Lambda|]^(-1/3)`.

No normalization factor is missing.

## B. Source telescoping constant

For probability densities `f,g`, the residuals `(f-g)_+` and `(g-f)_+` both have mass `delta/2`, where `delta=||f-g||_1`. Each residual output has height at most `C delta/2`; their signed difference therefore has height at most `C delta`, not `2C delta`. Summing coordinate replacements gives `C sum_j delta_j`.

## C. Diffuse-bank full-law constant

For a changed positive-bank factor of submass `u`, the leave-one-out bank sum has cap

`sqrt(2m/(m-1))`.

After convolving the selected subdensity, bank cap is at most

`M_1=u sqrt(2m/(m-1))`.

The untouched positive bank has cap `M_2=sqrt2`. Square pushforwards obey `M_k/sqrt(s)`. Thus

`int_0^t M_1 M_2/[sqrt(u)sqrt(t-u)] du
 =pi M_1 M_2
 =2pi u sqrt(m/(m-1))`.

For a changed negative-bank factor, the already-paid positive two-square receiver has height `2pi`; convolution with a subprobability of mass `u` gives `2pi u`.

Common-part decomposition yields

`||p_F-p_G||_infinity
 <=2pi sqrt(m/(m-1))(Delta_1+Delta_2)+2pi Delta_3`.

At `m=100`, the common coefficient is `2pi sqrt(100/99)=6.314838833996553...`.

## D. Same-height C0 step on the bank family

Let `r` be the bounded probability density of `Y_1^2+Y_2^2` and `h` the `L1` probability density of `-Y_3^2`. Then `p=r*h`. For translations,

`||tau_s p-p||_infinity <= ||r||_infinity ||tau_s h-h||_1 ->0`.

So `p` is uniformly continuous. Since it is also integrable, it vanishes at infinity. Height remains `<=||r||_infinity<=2pi`.

Continuity is downstream of the height payment.

## E. Operator-norm-to-Linfinity obstruction arithmetic

For partner family `m=2`, the base law is supported on `[-1/2,1]`, length `3/2`; hence `||p_0||_infinity>=2/3`.

Adjoin coefficient `e` and use the same extra-coordinate law for both matrices,

`X_0~Uniform[3/e,3/e+1]`.

For `Z=eX_0^2`, monotonicity gives

`||p_Z||_infinity=1/(2e(3/e))=1/6`.

Thus `||p_e||_infinity<=1/6` by convolution. For every translation `c`,

`||p_0-tau_c p_e||_infinity >=2/3-1/6=1/2`.

Meanwhile `||A_e-A_0||_op=e`, so taking arbitrarily small `e` proves failure of any owner-wide operator-norm modulus into canonical-density `L-infinity`, even modulo output translations.

## F. Live-correction audit

The arguments use only original-coordinate scaling, original disjoint-bank independence, and completed integrated Theorem-F/partner estimates. They do not use:

- pointwise one-direction quadratic Fourier decay;
- independence after spectral rotation;
- X-ray/projection-only control of the two-sheet side;
- arbitrary-joint rank-three coarea height;
- conditional density-cap preservation;
- a bounded-size physical carrier extracted from `s_3(A)>=1`.
