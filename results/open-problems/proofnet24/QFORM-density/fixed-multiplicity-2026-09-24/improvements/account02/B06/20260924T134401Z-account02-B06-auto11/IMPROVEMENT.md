SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B06, 2026-09-24T13:44:01Z.
attacking: complete threshold-nine replacement reconstruction and graph-regularizer edge cases.

# account02/B06 auto11 improvement

Pinned baseline: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

## Theorem A — complete nine-eigenvalue replacement

Let the coordinates of `X` be independent real variables with densities bounded by `K`. Let `A=A^T`, `b,c` be arbitrary, and assume `s_9(A)>=s>0`. Then `Q=X^TAX+b^TX+c` has an essentially bounded density and

`||p_Q||_infinity <= 6010 K^2/s`.

No sign, moment, support, smoothness, iid, log-concavity, diagonal-basis, exact-rank, leverage, or post-rotation-independence hypothesis is used. Global continuity is not claimed. This theorem does not solve the unrestricted three-eigenvalue conjecture.

### Dependency map

The proof uses from the pinned manuscript: Fourier/Riesz inversion (lines 91–160), Schur spectral count (183–207), geometric BL/product projections/scalar Fourier powers (221–301), scalar/definite/hyperbolic pivot profiles and quarter-power/log potential (404–525), spectral-to-volume interpolation and random cut (528–645). It replaces the order-five no-pivot endpoint by the following two grouped receivers.

### Grouped weighted-subset receiver

Take disjoint original-coordinate banks `H,I,J`. Let `W` be a `k`-dimensional linear image of `X_H` with density cap `M_H`, and write

`Q=F(X_H)+2<W,M X'+beta>+R(X')`, `X'=(X_I,X_J)`,

with arbitrary measurable `F`, arbitrary quadratic/affine `R`, and `M_J` of row rank `k`. Let `S` be the product of the nonzero singular values of `M_J`. Project the physical `I-J` crossing rows of `R` orthogonally off `row(M_J)` and call the residual row matrix `C`. For `ell>=1`, put

`Z_ell=sum_{|T|=ell} det(C_T C_T^T)`, `w_T=det(C_T C_T^T)/Z_ell`,

and inclusion marginals `alpha_i=sum_{T contains i}w_T`. If all positive `alpha_i<=1/2`, and `d=k+ell`, then

`|phi_Q(t)| <= min(1,K_{k,ell}|t|^(-d/2))`,

where

`K_{k,ell}=M_H^(1/2) pi^(d/2) 2^(ell/4) e^((k+2ell)/4)
              (ell^ell/ell!)^(1/4) S^(-1/2) Z_ell^(-1/4)`.

Proof reconstruction: push `exp(itF)dP_H` to `W`; its density has modulus at most `p_W`, hence squared `L^2` norm at most `M_H`. Plancherel at scale `2t` contributes `M_H(pi/|t|)^k`. For the light bank, condition on the literal `I` coordinates and square the pushforward with an independent copy only of `X_J`; pure `I` phases cancel and pure `J` phases have modulus one. The remaining literal `I` integrations produce scalar Fourier factors `psi_i(2t<a_i,D>)`, where `D=X_J-X'_J` has independent cap-one coordinates.

For each determinant-weighted `ell`-subset `T`, decompose `a_i=c_i+lambda_i M_J` with `c_i` perpendicular to `row(M_J)`. The map

`D -> (M_JD,(<c_i,D>)_(i in T))`

has squared Jacobian/Gram determinant

`S^2 det(C_T C_T^T)`.

The pinned product-projection lemma therefore gives density cap `e^(d/2)/(S sqrt(det(C_TC_T^T)))`. Weighted Holder uses powers `1/alpha_i`; the scalar Fourier-power estimate at that exponent gives exactly

`int |psi_i(2t(y+u))|^(1/alpha_i)dy <= pi sqrt(2e alpha_i)/|t|`.

The determinant-weighted geometric mean is `Z_ell^(-1/2) exp(H(w)/2)`. Uniformly order a sampled subset; entropy subadditivity gives

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!)`.

Combining these formulas and taking the square root after the hub Plancherel step gives the displayed `K_{k,ell}`. For `d>2`, integrating the envelope and Fourier inversion gives

`||p_Q||_infinity <= [d/(d-2)] M_H^(1/d) 2^(ell/(2d)) e^((k+2ell)/(2d))
 (ell^ell/ell!)^(1/(2d)) S^(-1/d) Z_ell^(-1/(2d))`.

No rotated random coordinates are declared independent.

### Marginal-free `E_3` density receiver

For a literal crossing matrix `M`, let `Z=E_3(M)=e_3(MM^T)>0`. If every physical row carries at most half the incident third-volume mass, the grouped receiver at `(k,ell)=(0,3)` applies. Otherwise promote a heavy literal row `w`; exact Gram–Schmidt gives

`J_i=||w||^2 e_2(CC^T)`.

If the residual `E_2` packet has a heavy row, promote it; then

`H_ij=det(PP^T)||C_2||_F^2>J_i/2`.

If the residual one-volume packet has a heavy row, promote it too and obtain a literal three-row Gram determinant `>H_ij/2`. Thus the four cases are paid by `(0,3)`, `(1,2)`, `(2,1)`, or an exact-rank-three crossing. The worst constant is

`C_3=3 sqrt(2) e (9/2)^(1/6)=14.818337662843...`,

so

`||p_Q||_infinity <= C_3 E_3(M)^(-1/6)`.

### Marginal-free `E_2` half-potential receiver

The same promotion tree one dimension lower gives

`sup_a E|Q-a|^(-1/2) <= C_2 E_2(M)^(-1/8)`,

with

`C_2=8 sqrt(e) 2^(-1/8)=12.095072570796...`.

This is intentionally a half-potential statement, not a rank-two density theorem.

### Assemble the nine-eigenvalue theorem

Normalize `K=s=1`, and retain the manuscript parameters `eta=1/100`, `kappa=1/80^2`.

1. No pivot: `s_9(A)>=1` and the pinned spectral-to-volume proposition at order three give `V_3>=kappa^3`. A fair original-coordinate cut gives `E_3>=4^-3 kappa^3`, hence `E_3^(-1/6)<=160`. Therefore

`||p_Q||_infinity <=160 C_3=2370.934026...<2400`.

2. Scalar pivot: completing one original coordinate leaves a Schur complement with at least eight unit-scale directions. If that Schur complement has a pivot, the pinned pivot theorem gives truncated half potential at most `600`; the outside-unit tail costs at most one, so the full half potential is at most `601`. If it has no pivot, then `s_5>=1`; the order-two spectral-to-volume proposition and a fair cut give `E_2>=4^-2 kappa^2`, hence the new receiver gives

`sup_a E|R-a|^(-1/2) <= C_2 sqrt(160)=152.991911...<153`.

Thus the full Schur half potential is at most `601` in all scalar-pivot subcases. The square profile costs `eta^-1/2=10`, giving `6010`.

3. Definite pair: the pinned polar-Jacobian estimate gives `10*pi<32`.

4. Indefinite pair: the Schur complement retains at least seven unit-scale directions, so its operator norm is at least one; the pinned hyperbolic/log-potential calculation gives `<251`.

The maximum is `6010`. For general `K,s`, put `Y=KX` and apply the normalized theorem to `A/s`; since `Q=(s/K^2)Qtilde`, density scaling proves Theorem A.

## Theorem B — diagonal anisotropic graph regularizers cannot improve the determinant majorant

This is the new B06 result.

In the pinned graph-BL proof, replace the scalar regularizer `alpha I` by an arbitrary positive diagonal coordinate regularizer

`Q^2=diag(q_1^2,...,q_d^2)`, `q_j>0`,

and set

`H=Q^2+a^2M^TM`, `C=2*pi*e`.

Define the frame weights

`c_j=q_j^2 e_j^T H^{-1}e_j`, `d_i=a^2m_i^T H^{-1}m_i`, `theta=sum_i d_i=sum_j(1-c_j)`.

Repeating the exact Jacobian/BL/Fourier-power calculation gives the fourth-power majorant

`I_Q <= det(H)^(-1/2) (prod_j q_j^(c_j)) C^theta`.

Write `q_j=C e^{y_j}`, `D_y=diag(e^{-y_j})`, and

`G=(a/C)^2 M^TM`, `P_y=I+D_y G D_y`.

After factoring `Q` out of `H`, all powers of `C` cancel and

`log I_Q <= F(y)-y dot r(y)`,

where

`F(y)=-1/2 log det(P_y)`, `r_j(y)=1-c_j`.

Direct differentiation gives the exact identity

`partial_j F(y)=1-(P_y^{-1})_{jj}=r_j(y)`.

Now use Cauchy–Binet/principal-minor expansion:

`det(P_y)=sum_{S subset [d]} det(G_{S,S}) exp(-2 sum_{j in S} y_j)`.

Because `G` is positive semidefinite, every coefficient is nonnegative. Therefore `log det(P_y)` is a log-sum-exp of affine functions and is convex; hence `F` is concave. The tangent inequality for a concave function gives

`F(0) <= F(y)+grad F(y) dot (0-y)=F(y)-y dot r(y)`.

Thus

`I_Q >= exp(F(0))=det(I+(a/C)^2 M^TM)^(-1/2)`

at the level of the derived upper-bound majorant. Equality is attained by `q_j=C` for all `j`, i.e.

`Q=C I`, `alpha=C^2=(2*pi*e)^2`.

So the manuscript's isotropic regularizer is a global minimizer among **all positive diagonal coordinate regularizers**, even if the `q_j` are chosen after seeing `t` and `M`. Boundary choices `q_j->0` or infinity cannot beat it by continuity/lower limits from positive `q_j`.

A sanity check over 6,000 random matrices/scales/anisotropic vectors found no violation; the proof above is exact and does not depend on that diagnostic.

### Consequence

The graph-BL determinant mechanism cannot lower its polynomial Fourier exponent by scalar or coordinate-anisotropic regularizer retuning. In particular a rank-four crossing remains at the `|t|^{-1}` density-inversion endpoint after the fourth root. Any threshold-eight or lower proof needs new product-structure information (for example a repeated-anchor/overlap-one receiver), not a better choice of graph regularizer.

Current next obligation: `QFORM-S8-OVERLAP-ONE-PRODUCT-RECEIVER-v1`. Threshold eight remains open. The unrestricted three-eigenvalue problem remains open.