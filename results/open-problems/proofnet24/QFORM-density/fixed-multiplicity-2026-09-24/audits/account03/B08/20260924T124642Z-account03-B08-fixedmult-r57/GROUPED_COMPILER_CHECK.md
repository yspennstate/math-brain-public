# account03/B08 r57 — direct check of the B04 grouped product-Fourier compiler

Source checked: `yspennstate/math-open-problems@8ff490c177d0cd7d6f33130f1431785e312a9d10`, Section 1 of the account03/B04 nine-eigenvalue candidate.

Status: **PASS for the identities and constants used by the nine-eigenvalue proof.** This note is independent of the alternative reconstruction through older r18/r30 theorem statements in `AUDIT.md`.

## 1. Complex hub pushforward and Plancherel

Let the `k`-dimensional hub projection be `W`, with density cap `M_H`. Push `exp(itF)dP_H` to `W`; if its complex density is `a_t`, then pointwise `|a_t|<=p_W`, while `||a_t||_1<=1`. Hence

`||a_t||_2^2 <= ||a_t||_infinity ||a_t||_1 <= M_H`.

With the manuscript Fourier convention, the affine change `xi=2t(l+beta)` gives exactly

`int |hat a_t(2t(l+beta))|^2 dl <= M_H (pi/|t|)^k`.

Cauchy--Schwarz against the complex pushforward `mu_t` of the light-bank phase therefore gives

`|phi_Q(t)|^2 <= M_H (pi/|t|)^k ||mu_t||_2^2`.

No independence is asserted after the deterministic `k`-dimensional SVD/orthogonal coordinate change used to compute a Jacobian.

## 2. Weighted-subset identity

After the standard independent-copy expansion in the `J` bank, let `D=X_J-X_J'`. Its coordinates remain independent and each difference density is bounded by one. For residual physical rows `c_i`, define

`d_T=det(C_T C_T^T)`, `Z_ell=sum_{|T|=ell} d_T`, `w_T=d_T/Z_ell`,

and inclusion marginals

`alpha_i=sum_{T contains i} w_T`.

The exact exponent identity is

`prod_i g_i = prod_T (prod_{i in T} g_i^(1/alpha_i))^(w_T)`,

because for each `i`, `sum_{T contains i} w_T/alpha_i=1`. Weighted Holder therefore applies with the stated powers.

For each `T`, the map

`D -> (M_J D,(<c_i,D>)_{i in T})`

has Gram determinant

`S^2 d_T`,

where `S` is the product of the nonzero singular values of `M_J`: the `c_i` are the components orthogonal to `row(M_J)`, so the block Gram determinant factors by orthogonal projection. The baseline product-projection lemma thus supplies pushforward density cap

`e^(d/2)/(S sqrt(d_T))`, `d=k+ell`.

At `p_i=1/alpha_i>=2`, the manuscript scalar Fourier-power bound and the change of variables `u=2t(y+shift)` give

`int |psi_i(2t(y+shift))|^(1/alpha_i) dy <= pi sqrt(2e alpha_i)/|t|`.

Thus the `T` integral is bounded by

`e^(d/2) [pi sqrt(2e)/|t|]^ell prod_{i in T} sqrt(alpha_i)/(S sqrt(d_T))`.

## 3. Entropy factor

The weighted geometric mean of the determinant denominators is exactly

`prod_T d_T^(-w_T/2)=Z_ell^(-1/2) exp(H(w)/2)`.

The marginal factors are exactly

`prod_T prod_{i in T} alpha_i^(w_T/2)=exp((1/2)sum_i alpha_i log alpha_i)`.

To bound their product, sample `T~w` and then uniformly order its `ell` elements as `(I_1,...,I_ell)`. Then

`H(I_1,...,I_ell)=H(w)+log(ell!)`,

while every positional marginal is `P(I_j=i)=alpha_i/ell`. Entropy subadditivity gives

`H(w)+log(ell!) <= ell H(alpha/ell)
 = -sum_i alpha_i log alpha_i + ell log ell`.

Therefore

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!)`,

exactly the candidate's (1.9). No dimension-dependent factor is hidden here.

## 4. Characteristic-function constant

Combining the previous steps gives

`||mu_t||_2^2 <= e^(d/2) pi^ell (2e)^(ell/2) |t|^(-ell)
                 S^(-1) Z_ell^(-1/2) (ell^ell/ell!)^(1/2)`.

Multiplication by the hub Plancherel factor and square root yields

`|phi_Q(t)| <= min(1,K_{k,ell}|t|^(-d/2))`,

with exactly

`K_{k,ell}=M_H^(1/2) pi^(d/2) 2^(ell/4) e^((k+2ell)/4)
            (ell^ell/ell!)^(1/4) S^(-1/2) Z_ell^(-1/4)`.

For `d>2`, the crossing time is `t_0=K^(2/d)` and

`int_R min(1,K|t|^(-d/2)) dt
 =2d/(d-2) K^(2/d)`.

The Fourier inversion factor `(2pi)^(-1)` cancels the `pi` contributed by `K^(2/d)`, giving exactly candidate formula (1.2).

## 5. Promotion identities used at orders three and two

For a physical crossing-row family `b_i`, if row `i` has canonical `ell`-volume inclusion marginal above `1/2`, write `w=b_i` and project all other rows orthogonally off `w`. Gram--Schmidt gives the exact base-times-height recursion; at the first two orders used here this is

`J_i=||w||^2 e_2(CC^T)`

and, after a second promoted physical row,

`H_ij=det(PP^T)||C_2||_F^2`.

Thus promotion never divides by a selected small local minor. Each promoted hub is made of actual original coordinates. For `k=1`, its density cap is one. For `k=2` or `3`, the deterministic left-SVD is a full-dimensional orthogonal change within exactly those physical hub coordinates, so the joint density sup remains at most one by Jacobian one; no rotated-coordinate independence is needed.

The terminal exact-rank two/three crossing estimates are the same physical-coordinate Plancherel bounds already proved in the manuscript/source chain. Hence the finite promotion trees used to remove row-marginal assumptions at `E_3` and `E_2` preserve the full same-bank phases and all affine terms.

## 6. Numerical specializations used by the nine-eigenvalue proof

At `(k,ell,d)=(0,3,3)`, formula (1.2) gives the candidate's conservative constant

`C_3=3 sqrt(2) e (9/2)^(1/6)=14.8183376628...`.

The earlier completed promotion theorem gives the stronger `6^(4/3)=10.902723557...`; either suffices.

At the critical two-volume endpoint, the completed r30 theorem gives

`sup_a E|R-a|^(-1/2) <=8(2e)^(1/4) Z_2^(-1/8)`.

With the manuscript random-cut lower bounds,

`E_3>=4^-3 kappa^3` gives the no-pivot density `<1744.436`,

and

`Z_2>=4^-2 kappa^2` gives the Schur half-potential `<154.519`.

Both are below the independently checked pivot bottleneck `<311` and therefore support the final `<3110` normalized theorem.

No live correction in the refreshed correction inbox contradicts any interface used above.
