# fleet02/B12 auto11b — complete nine-eigenvalue replacement, sharpened to 5338, plus paired-kernel endpoint

Pinned baseline: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

This is a complete replacement proof for multiplicity nine, preserving the baseline quantifiers. It independently rechecks the grouped product-Fourier argument and sharpens the dominant scalar-pivot arithmetic from `6010` to `<5338`. It does **not** claim multiplicity eight or the unrestricted three-eigenvalue conjecture.

## Theorem

Let `X=(X_1,...,X_n)` have independent real coordinates with densities bounded by `K`. Let `A=A^T`, `b in R^n`, `c in R`, and suppose

` s_9(A) >= s > 0.`

Then `Q=X^TAX+b^TX+c` has an essentially bounded density satisfying

`boxed: ||p_Q||_infinity < 5338 K^2/s.`

The no-pivot Fourier branch has a continuous `C_0` density; global continuity is not claimed.

## Dependency map

Audited baseline lines:
- Fourier inversion / Riesz: 91--160.
- Schur spectral count and rank perturbation: 161--207.
- product-projection density: 258--282.
- scalar Fourier powers: 284--301.
- scalar square / definite pair / hyperbola / quarter-power: 404--525.
- no-pivot spectral-to-volume: 582--619.
- fair original-coordinate cut: 621--630.
- singular kernels / pivot half-potential: 654--714.

New analytic compiler below:

`product projection + scalar Fourier powers`
` -> grouped product-Fourier lemma`
` -> marginal-free E_3 density + E_2 full half-potential`
` + baseline no-pivot interpolation/cut`
` + baseline pivot endpoints`
` -> complete s_9 density theorem`.

No support, moment, iid, sign, log-concavity, diagonal-basis, exact-rank, leverage or post-rotation-independence hypothesis is added.

Use throughout the normalized proof

`eta=1/100`, `kappa=1/80^2`.

## 1. Grouped product-Fourier lemma

Let `H,I,J` be disjoint literal original-coordinate banks. Let `W` be a `k`-dimensional orthogonal projection of `X_H` with density cap `M_H`. Write the quadratic polynomial in the form

`Q = F(X_H)+2<W,M_IY+M_JZ+beta>+R_I(Y)+2Y^T C_0 Z+R_J(Z)`,

where `Y=X_I`, `Z=X_J`; all displayed same-bank phases may be arbitrary. Suppose `M_J` has row rank `k`, and let `S` be the product of its `k` nonzero singular values (`S=1` if `k=0`). Orthogonally project each row of `C_0` off `row(M_J)` and call the resulting row matrix `C`.

For `ell>=1`, put

`Z_ell=sum_{|T|=ell} det(C_T C_T^T)>0`,
`w_T=det(C_T C_T^T)/Z_ell`,
`alpha_i=sum_{T contains i}w_T`,

and assume every `alpha_i<=1/2`. Put `d=k+ell`.

Then for `t!=0`,

`|phi_Q(t)| <= min(1,K_{k,ell}|t|^(-d/2))`,

where

`K_{k,ell}=M_H^(1/2) pi^(d/2) 2^(ell/4) e^((k+2ell)/4)
             (ell^ell/ell!)^(1/4) S^(-1/2) Z_ell^(-1/4)`.

If `d>2`,

`||p_Q||_infinity <= [d/(d-2)] M_H^(1/d) 2^(ell/(2d)) e^((k+2ell)/(2d))
 (ell^ell/ell!)^(1/(2d)) S^(-1/d) Z_ell^(-1/(2d)).`

### Proof

Push the complex measure `e^(itF)dP_H` to `W`; its density `a_t` satisfies `|a_t|<=p_W` and hence `||a_t||_2^2<=M_H`. Push the remaining complex measure to `l=M_IY+M_JZ`, obtaining density `mu_t`. Plancherel at frequency scale `2t` gives

`|phi_Q(t)|^2 <= M_H (pi/|t|)^k ||mu_t||_2^2`.

Condition on the original `Y`. Hilbert-space Jensen gives `||mu_t||_2^2<=E_Y||tau_{t,Y}||_2^2`. Insert the Gaussian Fourier cutoff `e^(-epsilon|xi|^2)`. Expanding with an independent copy `Z'` and averaging over `Y` yields an expectation over `D=Z-Z'` of

`kappa_epsilon(M_JD) prod_i |hat f_i(2t<a_i,D>)|`,

where each difference coordinate has density at most one and `a_i` is the corresponding row of `C_0`.

Use weighted Holder with determinant weights `w_T`. For each `T`, the map

`D -> (M_JD,(<c_i,D>)_{i in T})`

has Gram determinant `S^2 det(C_TC_T^T)`. The audited product-projection lemma therefore gives density cap

`e^(d/2)/[S sqrt(det(C_TC_T^T))]`.

Because `1/alpha_i>=2`, the audited scalar Fourier-power lemma, including the `2t` scale, gives

`int |hat f_i(2t(y+u))|^(1/alpha_i)dy <= pi sqrt(2e alpha_i)/|t|`.

The determinant geometric mean is

`Z_ell^(-1/2) exp(H(w)/2)`,

while the row marginals contribute

`exp[(1/2)sum_i alpha_i log alpha_i]`.

Ordering a random `ell`-subset with law `w` uniformly and using entropy subadditivity gives

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!)`.

After taking square roots, these factors give exactly `K_{k,ell}`. Monotone convergence removes the Gaussian cutoff. Finally

`int_R min(1,K|t|^(-d/2))dt = [2d/(d-2)]K^(2/d)`,

and the Fourier inversion factor `1/(2pi)` cancels the `pi` in `K^(2/d)`, proving the density formula. All conditioning is on literal original coordinates.

## 2. Exact-rank endpoints

For `r` literal physical coordinates crossing a disjoint product bank through a rank-`r` matrix `P`, arbitrary same-bank/affine phases retained, the same Plancherel argument gives

`|phi(t)| <= min(1, pi^(r/2)e^(r/4) det(PP^T)^(-1/4)|t|^(-r/2)).`

For `r=3`, direct envelope integration yields

`||p||_infinity <= 3 sqrt(e) det(PP^T)^(-1/6).`

For `r=2`, the audited Riesz identity yields only the full half-potential statement

`sup_a E|Q-a|^(-1/2) <= 4 sqrt(2)e^(1/4) det(PP^T)^(-1/8).`

The distinction is essential: rank two is not promoted to a density endpoint.

## 3. Marginal-free E3 density receiver

Let `Z=E_3(M)=e_3(MM^T)>0` for a literal original-coordinate cross block. If every row carries at most half of the determinant-squared `E_3` mass, apply the grouped lemma at `(k,ell,d)=(0,3,3)`.

If a row `w` is heavier than one half, project the other rows off `w`; exact Gram--Schmidt gives

`J_i=||w||^2 e_2(CC^T)>Z/2`.

If the residual `E_2` marginals are all at most one half, apply `(1,2,3)`. Otherwise promote a second row. With promoted two-row matrix `P` and remaining rows projected off its span,

`det(PP^T)||C_2||_F^2 > Z/4`.

If the residual one-volume marginals are light, apply `(2,1,3)`; otherwise promote a third row, whose literal three-row Gram determinant exceeds `Z/8`, and use the exact rank-three endpoint.

The largest constant among all four branches is the diffuse `(0,3,3)` constant

`C_3=3 sqrt(2)e(9/2)^(1/6)=14.818337662843...`,

so

`boxed: ||p_Q||_infinity <= C_3 E_3(M)^(-1/6).`

## 4. Marginal-free E2 full half-potential receiver

The same promotion tree one dimension lower gives

`boxed: sup_a E|Q-a|^(-1/2) <= C_2 E_2(M)^(-1/8),`

where

`C_2=8 sqrt(e) 2^(-1/8)=12.095072570796... .`

For the diffuse branch `(0,2,2)`, the characteristic envelope has coefficient

`L=pi e 2^(3/4) E_2(M)^(-1/4)`,

and

`int_R |t|^(-1/2) min(1,L/|t|)dt = 8 sqrt(L)`.

One heavy row uses `(1,1,2)`; a second heavy row terminates at the exact physical rank-two half-potential endpoint. This is deliberately not an `L^infinity` density theorem.

## 5. Complete nine-eigenvalue proof

Normalize `K=s=1` and assume `s_9(A)>=1`.

### No pivot

If `A` has no `eta`-pivot, the audited spectral-to-volume proposition at order `k=3` gives

`V_3(A)>=kappa^3`.

The fair literal coordinate cut gives a physical cross block `M` with

`E_3(M)>=4^(-3)kappa^3`,

hence

`E_3(M)^(-1/6)<=2 kappa^(-1/2)=160`.

Therefore

`||p_Q||_infinity <=160 C_3
 =2370.93402605488... .`

### Scalar pivot

Suppose `|A_hh|>=eta`. Completing the square in the literal coordinate `X_h` leaves a Schur complement `S` with at least eight eigenvalues of modulus at least one.

If `S` has an `eta`-pivot, re-read the three branches of the audited pivot half-potential proof instead of rounding them all to `600`.

The scalar-subpivot branch is

`H(S) <= eta^(-1/2)(8+3L_0)`,

with `L_0=4+4 log16`, hence

`H(S) <=10(20+12 log16)
       =532.7106466687737... .`

The definite-pair branch is at most `40pi`, and the indefinite-pair branch is at most

`10(32+4 log16)+4/e
 =432.375066654277... .`

Thus every pivoted `S` satisfies

`H(S) <=10(20+12 log16)`.

Outside `|S-a|<=1`, the kernel is at most one, so

`sup_a E|S-a|^(-1/2)
 <= 1+10(20+12 log16)
 =533.7106466687737... .`

If `S` has no pivot, then certainly `s_5(S)>=1`. The audited order-two spectral-to-volume proposition and fair cut give

`E_2(M_S)>=4^(-2)kappa^2`,

so Section 4 gives

`sup_a E|S-a|^(-1/2)
 <= C_2 sqrt(160)
 =152.99191115498024...`,

which is smaller.

The conditional scalar-square profile therefore gives

`||p_Q||_infinity
 <= eta^(-1/2)[1+10(20+12log16)]
 =5337.106466687737... <5338.`

This is the dominant branch.

### Definite pair

A definite physical pair with determinant modulus at least `eta` gives directly

`||p_Q||_infinity <= pi/sqrt(eta)=10pi<32.`

### Indefinite pair

An indefinite pair removes two coordinates, so its Schur complement retains at least seven unit spectral directions and in particular has operator norm at least one. The audited hyperbolic logarithmic envelope and quarter-power logarithmic potential therefore apply exactly as in the baseline main proof, giving

`||p_Q||_infinity
 <=10(10+5log16)+1/e <251.`

All four branches are exhaustive, so the normalized bound is `<5338`.

For general `K,s`, set `Y=KX` and

`Q_tilde=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c`.

Then `s_9(A/s)>=1` and `Q=(s/K^2)Q_tilde`. Scalar density scaling gives

`boxed: ||p_Q||_infinity <5338 K^2/s.`

This completes the replacement theorem.

## 6. B12 paired-source endpoint for the multiplicity-eight frontier

After the first legitimate symmetrization of one original coordinate with density `f<=1`, its unsplit paired source is

`G(u,v)=(1/2)f((v+u)/2)f((v-u)/2)`.

Let `(U,V)=(X-X',X+X')`, with `X'` an independent copy. Then `UV=X^2-X'^2`. Applying the audited determinant-one hyperbolic-pair kernel and adding the tail outside unit distance gives the safe integrated estimate

`boxed: sup_a intint G(u,v)|uv-a|^(-1/2)du dv
        <=33+4log16 <45.`

More generally, for `gamma!=0`,

`sup_a intint G(u,v)|gamma uv-a|^(-1/2)du dv
 <=(33+4log16)|gamma|^(-1/2).`

This is source-valid for arbitrary rough cap-one `f` and does not normalize any conditional slice.

Two tempting stronger inferences are false:

1. For uniform `f=1_{[-1/2,1/2]}`, `G=1/2` on `|u|+|v|<=1`. The normalized conditional density of `V|U=u` equals `1/[2(1-|u|)]` and is unbounded as `|u|->1`. Thus a paired slice is not a cap-one conditional law.

2. A uniform fiberwise half-potential does not combine automatically with an outer scalar square. If `R_0` is any cap-one quadratic law with finite full half-potential but unbounded logarithmic density (the explicit rank-two opposite-sign construction provides one) and `R_h=R_0-gamma h^2`, then every fiber has the same half-potential norm while `gamma H^2+R_H=R_0` remains unbounded. A future overlap-one proof must therefore control the fiber critical shift, not merely the separate kernel norms.

These are proof-interface obstructions, not counterexamples to multiplicity eight.

## 7. Threshold status

Multiplicity nine is proved above with the original arbitrary-density hypotheses and explicit constant `<5338 K^2/s`. Multiplicity eight remains open in the current route because the no-pivot terminal carries overlap-one determinant currency through a shared physical coordinate. The paired-source half-potential is a valid ingredient, but the dependence-safe density receiver is still missing.

The unrestricted three-eigenvalue QFORM conjecture remains OPEN.
