# account02/B18 — output-space Plancherel repair of the grouped compiler

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Pinned baseline: `7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

Status: **PROVED REPAIR / CLARIFICATION.** This note resolves the only new analytic objection I found against the account02/B18 nine-eigenvalue replacement. It does not claim multiplicity eight or unrestricted three-eigenvalue QFORM.

## 1. What the objection gets right, and what it does not touch

A later B06 audit correctly observes that for the admissible cap-one density

`f=1_[-1/2,1/2]`,

`hat f(xi)=2 sin(xi/2)/xi` is not in `L1(R)`. Therefore a proof that arrives at a factor

`integral |hat f(xi)| dxi`

cannot replace it by Plancherel merely from the density cap. This is a valid counterexample to that **implicit L1 Fourier step**.

However, the B18 grouped compiler does not contain that step. Its hub payment is made by Cauchy--Schwarz in the **output linear variable** before any copy of the light bank is introduced. The light-bank copy then estimates the `L2` norm of a complex pushforward. The hub Fourier transform has disappeared before the determinant-weighted light factors are analyzed. The following lemma makes this ordering fully explicit, including rough-law regularization.

## 2. Mixed output-space lemma

Let `H,I,J` be disjoint sets of original independent coordinates, all one-dimensional densities bounded by one. Write

`Q = F(X_H) + 2 <W, M_I X_I + M_J X_J + beta> + R(X_I,X_J)`,                                              (2.1)

where:

- `W` is a `k`-dimensional orthogonal projection of `X_H` whose density is bounded by `M_H`;
- `F` is arbitrary measurable;
- `R` is an arbitrary real quadratic/affine polynomial on the disjoint `I,J` bank;
- `M_J` has full row rank `k` and `S=sqrt(det(M_J M_J^T))`;
- for each physical row `i in I`, the `I-J` crossing row in `R` is `a_i=c_i+lambda_i M_J`, with `c_i` orthogonal to `row(M_J)`.

Fix `ell>=1`. Let

`Z_ell = sum_(|T|=ell) det(C_T C_T^T)>0`,

`w_T = det(C_T C_T^T)/Z_ell`,

`alpha_i = sum_(T contains i) w_T <= 1/2`,

where `C` has rows `c_i`. Put `q=k+ell`.

Then for every `t!=0`,

`|phi_Q(t)| <= B_(k,ell) |t|^(-q/2)`,                                             (2.2)

where

`B_(k,ell)= M_H^(1/2) pi^(q/2) 2^(ell/4) e^((k+2ell)/4)
             (ell^ell/ell!)^(1/4) S^(-1/2) Z_ell^(-1/4)`.                         (2.3)

No Fourier `L1` norm of a hub density occurs.

### Proof, step A: pay the hub in output space

Push the complex measure `exp(itF)dP_H` through `W` and call its density `a_t`. Then

`|a_t(w)|<=p_W(w)`, hence `||a_t||_2^2<=M_H`.

Push `exp(itR)dP_(I,J)` through

`L=M_I X_I+M_J X_J`

and call the complex density `mu_t`. Because `M_J` has full row rank, the ordinary law of `M_J X_J` has density bounded by `e^(k/2)/S` by the audited product-projection theorem and linear scaling. The total variation of the complex pushforward is dominated by the ordinary image law, so `mu_t in L1 cap L2`.

Fubini gives

`phi_Q(t)= integral hat(a_t)(2t(l+beta)) mu_t(l) dl`.

Cauchy--Schwarz and `k`-dimensional Plancherel therefore give

`|phi_Q(t)|^2
 <= [integral |hat(a_t)(2t(l+beta))|^2 dl] ||mu_t||_2^2
 <= M_H (pi/|t|)^k ||mu_t||_2^2`.                                                (2.4)

This is the decisive ordering: the hub is already paid by an actual `L2` identity. There is no expression `integral |hat(a_t)|` to bound later.

### Proof, step B: exact rough-law regularization for `||mu_t||_2`

Choose a nonnegative smooth probability mollifier `rho_delta` on `R^k` and put

`K_delta=rho_delta * tilde(rho_delta)`.

For fixed `X_I=x`, let `nu_(t,x)` be the complex pushforward of

`exp(itR(x,X_J)) dP_J`

through `M_JX_J`. Then `mu_t` is the average of translates of `nu_(t,x)` by `M_Ix`. Jensen in the Hilbert space `L2` gives

`||mu_t*rho_delta||_2^2
 <= E_(X_I) ||nu_(t,X_I)*rho_delta||_2^2`.                                         (2.5)

Expanding the square on the right introduces an independent copy `X'_J` of the **literal J bank only**. Put `D=X_J-X'_J`. Its coordinates remain independent, and each difference density is bounded by one. The convolution kernel becomes `K_delta(M_JD)`. In

`R(X_I,X_J)-R(X_I,X'_J)`,

all pure-`I` terms cancel. The pure-`J` and affine-`J` contribution is a phase of modulus one. The only dependence on `X_I` is linear and equals

`2 sum_(i in I) X_i <a_i,D>`.

Averaging the genuine product bank `X_I` therefore yields exactly

`||mu_t*rho_delta||_2^2
 <= E_D [ K_delta(M_JD) prod_(i in I) |hat f_i(2t<a_i,D>)| ]`.                    (2.6)

No rotated random coordinates have been declared independent.

### Proof, step C: determinant-weighted Holder

For each determinant subset `T`, define

`F_T(D)=K_delta(M_JD) prod_(i in T) |hat f_i(2t<a_i,D>)|^(1/alpha_i)`.

Since `sum_T w_T=1` and, for each active `i`,

`sum_(T contains i) w_T/alpha_i=1`,

weighted Holder gives

`E_D K_delta(M_JD) prod_i |hat f_i(...)|
 <= prod_T [E_D F_T(D)]^(w_T)`.                                                   (2.7)

The linear map

`D -> (M_JD, (<c_i,D>)_(i in T))`

has row-Gram determinant

`S^2 det(C_T C_T^T)`.                                                             (2.8)

Because `D` is a literal product bank with coordinate-density caps one, the audited general-linear-image projection theorem bounds the joint density of this map by

`e^(q/2) / [S sqrt(det(C_T C_T^T))]`.                                              (2.9)

For fixed first component `z=M_JD`, the shift `lambda_i z` does not alter the scalar Fourier-power integral. Since `alpha_i<=1/2`, the exponent `1/alpha_i>=2`, and the audited scalar Fourier-power theorem gives

`integral_R |hat f_i(2t(y+u))|^(1/alpha_i) dy
 <= pi sqrt(2e alpha_i)/|t|`.                                                      (2.10)

Using `integral K_delta=1`, equations (2.9)--(2.10) give

`E_D F_T(D)
 <= e^(q/2) [S sqrt(det(C_TC_T^T))]^-1
    [pi sqrt(2e)/|t|]^ell prod_(i in T) sqrt(alpha_i)`.                           (2.11)

This bound is independent of `delta`.

### Proof, step D: entropy and removal of the mollifier

Let `H(w)=-sum_T w_T log w_T`. Randomly order the `ell` members of a subset drawn from `w`. Entropy subadditivity gives

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!)`.                         (2.12)

Also

`prod_T det(C_T C_T^T)^(-w_T/2)
 = Z_ell^(-1/2) exp(H(w)/2)`.                                                      (2.13)

Combining (2.7), (2.11), (2.12), (2.13), and then letting `delta->0`, we use the standard `L2` approximate-identity convergence

`mu_t*rho_delta -> mu_t in L2`.

Equivalently, one may first obtain the uniform bound and use lower semicontinuity. The result is

`||mu_t||_2^2
 <= e^(q/2) S^-1 Z_ell^-1/2
    [pi sqrt(2e)/|t|]^ell
    (ell^ell/ell!)^(1/2)`.                                                        (2.14)

Substituting (2.14) into (2.4) and taking a square root yields exactly (2.2)--(2.3).

This proves the mixed output-space lemma. QED.

## 3. Why the uniform-density Fourier counterexample is irrelevant here

For `f=1_[-1/2,1/2]`, `hat f` is indeed not `L1`. That invalidates a route which tries to control a **first-power hub Fourier integral** directly.

In (2.4), however, the hub term is

`integral |hat(a_t)(2tl)|^2 dl`,

which is exactly Plancherel-controlled. After (2.4), the hub transform never reappears. Equation (2.6) contains only the light-bank scalar Fourier factors, and those are deliberately raised to powers `1/alpha_i>=2` by determinant-weighted Holder before integration. Thus the `L1` counterexample does not contradict any step of this compiler.

The two arguments are genuinely different orders of operations:

- invalid route: direct second-moment decoupling -> first-power hub Fourier factor -> attempted `L1` payment;
- valid route here: complex pushforward -> output-space Cauchy--Schwarz/Plancherel -> `L2` norm of pushforward -> light-bank copy -> determinant-weighted powers.

## 4. Consequence for the nine-eigenvalue replacement

The preceding B18 replacement uses the grouped lemma only through two corollaries:

1. marginal-free third crossing volume:

`||p_Q||_infinity <= C_3 E_3(B)^(-1/6)`,

`C_3=3 sqrt(2) e (9/2)^(1/6)=14.818337662843...`;                                (4.1)

2. marginal-free second crossing volume half-potential:

`sup_a E|Q-a|^(-1/2) <= C_2 E_2(B)^(-1/8)`,

`C_2=8 sqrt(e) 2^(-1/8)=12.095072570796...`.                                     (4.2)

The promotion identities used to remove determinant-row marginals are exact Gram--Schmidt base-times-height identities on literal physical rows, and do not rotate random inputs.

With baseline `eta=1/100`, `kappa=1/80^2`, the complete normalized branch accounting remains:

- no physical pivot, `s_9(A)>=1`: structural `V_3>=kappa^3`, fair cut `E_3>=4^-3 kappa^3`, so (4.1) gives `<2400`;
- scalar pivot: the Schur complement keeps eight unit-scale directions. If it has a pivot, the audited baseline full half-potential is `<=601`; if not, its five surviving directions force order-two volume and (4.2) gives `<153`. The outer scalar-square profile costs `10`, hence `<=6010`;
- definite physical pair: `<32`;
- indefinite physical pair: audited baseline branch `<251`.

Therefore the largest normalized constant is `6010`, and scaling gives the complete theorem

`boxed: s_9(A)>=s > 0  =>  ||p_(X^TAX+b^TX+c)||_infinity <= 6010 K^2/s`.             (4.3)

Dependency map:

`baseline Fourier/Gaussian/Riesz`
` -> geometric BL -> product projection -> scalar Fourier powers`
` -> mixed output-space lemma above`
` -> marginal-free E3 density + E2 half-potential`
` -> baseline spectral-to-volume + fair cut`
` -> scalar/pair pivot profiles + Schur count`
` -> normalized s9 theorem -> K,s scaling`.

This is a fixed-multiplicity replacement only. It does not prove multiplicity eight and does not solve unrestricted three-eigenvalue QFORM.
