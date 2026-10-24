# account01/B07 — independent full review of the nine-eigenvalue improvement

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T133059Z-account01-B07-fixedmult-audit-r12`  
Baseline source: `7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

I completed the baseline 790-line audit before using the later threshold-lowering artifacts. I then independently reconstructed the grouped product-Fourier argument and the promotion trees described in the account03/B04 candidate and the account02/B04 rough-limit repair.

## Verdict

**PASS in this independent reconstruction of the unconditional nine-eigenvalue theorem.**

> Let `X_i` be independent real random variables with densities bounded by `K`, let `A=A^T` be arbitrary, and let `b,c` be arbitrary. If `s_9(A)>=s>0`, then `Q=X^TAX+b^TX+c` has an essentially bounded density and
> 
> `||p_Q||_infinity <= (2010+1200 log 16) K^2/s < 5338 K^2/s`.

The no-pivot Fourier branch has a continuous density. Global continuity is not asserted for the pivot branches.

This is not the unrestricted three-eigenvalue theorem. The eight-eigenvalue case remains open after the currently known overlap-one/two-sided-collar reduction.

## 1. Grouped product-Fourier compiler

Take disjoint original-coordinate sets `H,I,J`. Let `W=L_H X_H` be a `k`-dimensional orthogonal projection of `X_H` with density cap `M_H`, and write

`Q=F(X_H)+2<W,M X'+beta>+R(X')`, `X'=(X_I,X_J)`,

where `F` is arbitrary measurable, `R` is an arbitrary quadratic/affine polynomial, and `M_J` has row rank `k`. Let `S` be the product of the nonzero singular values of `M_J`.

Write each physical row `a_i` of the `I x J` cross block of the quadratic part of `R` as

`a_i=c_i+lambda_i M_J`, with `c_i` orthogonal to `row(M_J)`.

For an integer `ell>=1`, define

`Z_ell=sum_{|T|=ell} det(C_T C_T^T)`,

and the probability weights `w_T=det(C_T C_T^T)/Z_ell`. Let `alpha_i=sum_{T contains i}w_T`, assume `alpha_i<=1/2`, and put `d=k+ell`.

### 1.1 Hub Plancherel step

Push the complex measure `e^{itF}dP_H` through `W`; its density `a_t` obeys `|a_t|<=p_W`, hence `||a_t||_2^2<=M_H`.

Push `e^{itR}dP_{X'}` through `y=M X'`; call its complex density `mu_t`. Plancherel and Cauchy--Schwarz give

`|phi_Q(t)|^2 <= M_H (pi/|t|)^k ||mu_t||_2^2`.                 (1)

No projected-coordinate independence is used.

### 1.2 Rough-law light-bank step

Condition on `X_I=x`. For rigor, convolve the conditional complex pushforward through `M_J X_J` with a compact probability approximate identity `rho_eps`. Hilbert-space Jensen bounds the squared norm of the global smoothed mixture by the average conditional squared norms.

Expanding each conditional squared norm with an independent copy `X'_J`, then averaging in `x` before taking absolute values, cancels pure-`I` phases and leaves pure-`J` phases with modulus one. With `D=X_J-X'_J`, the original physical independence gives

`E_x ||nu_{eps,x}||_2^2
 <= E_D [kappa_eps(M_JD) prod_i |psi_i(2t<a_i,D>)|]`,            (2)

where `kappa_eps=rho_eps*tilde(rho_eps)` is a probability density and each `psi_i` is the characteristic function of the original cap-one law of `X_i`.

The bound derived below is independent of `eps`. On the Fourier side,

`||nu_x||_2^2 <= liminf_{eps->0} ||nu_x*rho_eps||_2^2`

because `hat rho_eps ->1` and `|hat rho_eps|<=1`; Fatou then passes the uniform estimate to the unsmoothed pushforward. This is the needed rough-law limit and introduces no moment, support or smoothness assumption.

### 1.3 Weighted determinant aggregation

Discard rows with `alpha_i=0`, whose Fourier factors are at most one. The exact identity

`prod_i |psi_i| = prod_T [prod_{i in T}|psi_i|^(1/alpha_i)]^(w_T)`

and generalized Holder reduce (2) to fixed-`T` integrals.

For such a `T`, the physical map

`D -> (M_JD,(<c_i,D>)_{i in T})`

has Gram determinant

`S^2 det(C_T C_T^T)`.

The baseline product-projection lemma therefore gives density cap

`e^(d/2)/[S sqrt(det(C_T C_T^T))]`.

Since `alpha_i<=1/2`, the baseline scalar Fourier-power lemma at `p=1/alpha_i>=2`, including the scale `2t`, gives

`int |psi_i(2t(y+u))|^(1/alpha_i)dy
 <= pi sqrt(2e alpha_i)/|t|`.                                  (3)

Consequently the fixed-`T` integral is at most

`e^(d/2) [pi sqrt(2e)/|t|]^ell
 prod_{i in T} sqrt(alpha_i)
 /[S sqrt(det(C_T C_T^T))]`.                                   (4)

The weighted determinant factor is

`Z_ell^(-1/2) exp(H(w)/2)`.

Uniformly order the random `ell`-subset `T`. Its entropy is `H(w)+log(ell!)`; every ordered position has marginal `alpha_i/ell`. Entropy subadditivity gives

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!)`.       (5)

Combining (1)--(5) gives

`|phi_Q(t)| <= min(1,K_{k,ell}|t|^(-d/2))`,                     (6)

where

`K_{k,ell}=M_H^(1/2) pi^(d/2) 2^(ell/4) e^((k+2ell)/4)
             (ell^ell/ell!)^(1/4) S^(-1/2) Z_ell^(-1/4)`.

If `d>2`, direct integration and Fourier inversion give

`||p_Q||_infinity <= [d/(d-2)] M_H^(1/d) 2^(ell/(2d))
 e^((k+2ell)/(2d)) (ell^ell/ell!)^(1/(2d))
 S^(-1/d) Z_ell^(-1/(2d))`.                                    (7)

The `k=0` case is the same proof with no hub-Plancherel variables.

## 2. Marginal-free `E_3` density receiver

For a literal physical cross block `M`, put `Z=E_3(M)=e_3(MM^T)>0`. Let `J_i` be the total three-row Gram mass containing physical row `i`; `sum_i J_i=3Z`.

If every `J_i/Z<=1/2`, apply (7) at `(k,ell,d)=(0,3,3)`:

`||p||_infinity <= C_3 Z^(-1/6)`,

`C_3=3 sqrt(2)e(9/2)^(1/6)=14.818337662843...`.                 (8)

If some row `w` is heavy, exact coefficient-space Gram--Schmidt gives

`J_i=||w||^2 e_2(CC^T)`.                                       (9)

If the residual order-two marginals are diffuse, apply `(k,ell,d)=(1,2,3)`. If a residual physical row is heavy, promote it; for the two-row hub matrix `P`, exact Gram--Schmidt gives

`H_ij=det(PP^T)||C_2||_F^2 > J_i/2 > Z/4`.                     (10)

If the residual one-volume is diffuse, apply `(2,1,3)`. If a third residual row is heavy, its literal three-row Gram determinant is `>H_ij/2>Z/8`, and (7) at `(3,0,3)` gives the exact-rank-three terminal estimate.

The constants in all promoted branches are smaller than `C_3`; hence (8) holds with no marginal hypothesis. Every branch has an integrable characteristic-function majorant, so this receiver gives a continuous density.

## 3. Marginal-free `E_2` half-potential receiver

For `Z=E_2(M)>0`, the same promotion tree has at most one hub before the terminal rank-two branch.

In the diffuse `(k,ell,d)=(0,2,2)` branch, (6) becomes

`|phi(t)| <= min(1,L/|t|)`,

`L=pi e 2^(3/4) Z^(-1/4)`.

The baseline Riesz inequality and

`int_R |t|^(-1/2) min(1,L/|t|) dt = 8 sqrt(L)`

give

`sup_a E|Q-a|^(-1/2) <= C_2 Z^(-1/8)`,

`C_2=8 sqrt(e) 2^(-1/8)=12.095072570796...`.                   (11)

If one row is heavy, Gram--Schmidt gives `||w||^2||C||_F^2>Z/2`. The diffuse residual `(1,1,2)` branch gives a smaller constant. If the residual one-volume has a heavy row, the promoted two-row determinant exceeds `Z/4`, and the terminal `(2,0,2)` Plancherel/Riesz estimate is also smaller. Thus (11) is unconditional.

## 4. Assembly under nine large singular values

Normalize `K=s=1` and retain the baseline `eta=1/100`, `kappa=1/80^2`.

### No pivot

The audited baseline spectral-to-volume theorem at order three uses exactly `s_9(A)>=1` and gives

`V_3(A)>=kappa^3`.

A fair physical cut gives

`E_3(M)>=4^(-3)kappa^3`, hence `E_3(M)^(-1/6)<=160`.

By (8),

`||p_Q||_infinity <=160 C_3=2370.934026...<2400`.               (12)

### Scalar pivot

A scalar pivot leaves at least eight unit-scale Schur directions. Let the Schur polynomial be `R`.

If `R` has a pivot, the baseline pivot-half-potential proof yields the sharper explicit bound

`H(R)<=200+120 log16`,

and the tail outside distance one contributes at most one:

`sup_a E|R-a|^(-1/2) <=201+120 log16`.                           (13)

If `R` has no pivot, then in particular `s_5(R)>=1`. The audited baseline spectral-to-volume proposition at order two plus a random cut gives an `E_2` cross block with

`E_2^(-1/8)<=sqrt(160)`.

By (11), its full half-potential is at most

`C_2 sqrt(160)=152.991911...`,                                  (14)

which is smaller than (13).

The outer square profile contributes `eta^(-1/2)=10`; therefore

`||p_Q||_infinity <=2010+1200 log16
 =5337.106466...<5338`.                                         (15)

### Pair pivots

A definite pair has conditional density at most `10pi<32`. An indefinite pair loses only two Schur directions; at least seven remain, so the baseline logarithmic-critical-value argument has its required nonzero Schur direction and stays below `251`.

Thus (15) is the largest normalized branch.

### Scaling

For general `K,s`, set `Y=KX` and

`Qtilde=Y^T(A/s)Y+(K/s)b^T Y+(K^2/s)c`.

Then `Q=(s/K^2)Qtilde`, proving

`||p_Q||_infinity <=(2010+1200 log16)K^2/s <5338K^2/s`.

## 5. Review gate and lower-threshold status

This B07 reconstruction is a genuinely separate full mathematical review from the existing account01/B16 review at commit `54ec2a651d854563f8db0d92c4c3426f76551786`. An additional account02/B04 derivation/rough-limit repair also exists. Thus the mathematical nine-direction candidate now has at least two separate full-review artifacts. I do **not** mutate any owner-level release flag here; reconciliation/release synthesis remains a separate repository-control action.

I also checked the current eight-direction structural reduction: if the order-three no-pivot volume is not already large, the sharp `r=2` completion forces quantitative overlap-one third-minor mass and a two-sided pair collar. That reduction is sound, but no dependence-safe arbitrary-curvature receiver for the zero/near-zero common-diagonal collar is proved here. Therefore this run rigorously lowers the complete theorem from 17 to **9**, not to 8.