# account02 / B18 r13 — independent complete audit of the nine-eigenvalue replacement

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Status: **PASS as a complete mathematical replacement proof in this independent B18 review.** This does not overwrite the owner-pinned 17-lineage source and is not a public-release action.

## Theorem independently reconstructed

Let `X_1,...,X_n` be independent real variables with probability densities bounded by `K<infinity`. Let `A=A^T` be arbitrary real symmetric and let `b,c` be arbitrary. If

` s_9(A)>=s>0,`

then

`Q=X^TAX+b^TX+c`

has an essentially bounded density satisfying

`boxed: ||p_Q||_infinity <= 6010 K^2/s.`

No Gaussianity, moments, bounded support, iid, log-concavity, sign restriction, diagonal-basis assumption, exact rank, leverage condition, or post-rotation independence is introduced. Global continuity is not claimed; the no-pivot Fourier branch below is `C_0`, while the pivot branches are used only through measure domination.

The proof below is reconstructed from the pinned baseline manuscript plus the grouped product-Fourier idea first recorded in account03/B04 commit `8ff490c177d0cd7d6f33130f1431785e312a9d10`. I checked every new constant and promotion identity rather than treating that report as a black box.

## 1. Normalization and baseline inputs

Normalize to `K=s=1`, and keep the baseline parameters

`eta=1/100`, `kappa=1/80^2`.

The baseline proof, audited separately in this same B18 run, supplies:

1. the geometric rank-one BL inequality with constant one;
2. the product-projection bound `||p_{U^TX}||_infinity<=e^(d/2)`;
3. scalar Fourier powers `int |hat f|^p <= 2*pi*sqrt(2e)/sqrt(p)` for `p>=2`;
4. Fourier/Riesz inversion;
5. the Schur spectral count `N_S(t)>=N_A(t)-k` (valid literally, including singular ambient matrices);
6. scalar/definite/indefinite physical-pivot profiles;
7. spectral-to-disjoint-volume: no pivot and `s_(4r-3)>=1` imply `V_r>=kappa^r` for `r<=5`;
8. fair-coordinate-cut identity `E Z_r(A[I,J])=4^-r V_r(A)`.

All of these retain original-coordinate product provenance.

## 2. Grouped product-Fourier compiler

Take disjoint original-coordinate banks `H,I,J`. Let `W` be a `k`-dimensional orthogonal projection of `X_H` with density cap `M_H`. Write the full form as

`Q=F(X_H)+2<W,M X'+beta>+R(X')`, `X'=(X_I,X_J)`,

where `F` is arbitrary measurable, `R` is arbitrary quadratic/affine, and the restriction `M_J` has row rank `k`. Let `S` be the product of the nonzero singular values of `M_J`.

Project the physical `I-J` crossing rows of the quadratic part of `R` orthogonally off `row(M_J)` and call the residual row matrix `C`. For `ell>=1`, set

`Z_ell=sum_(|T|=ell) det(C_T C_T^T)>0`,

`w_T=det(C_T C_T^T)/Z_ell`,

and inclusion marginals `alpha_i=P_w{i in T}`. Assume `alpha_i<=1/2`; put `d=k+ell`.

### Compiler claim

For `t!=0`,

`|phi_Q(t)| <= min(1,K_(k,ell)|t|^(-d/2))`,

where

`K_(k,ell)=M_H^(1/2) pi^(d/2) 2^(ell/4) e^((k+2ell)/4)
            (ell^ell/ell!)^(1/4) S^(-1/2) Z_ell^(-1/4).`

For `d>2`,

`||p_Q||_infinity <= [d/(d-2)] M_H^(1/d) 2^(ell/(2d))
 e^((k+2ell)/(2d)) (ell^ell/ell!)^(1/(2d))
 S^(-1/d) Z_ell^(-1/(2d)).`

### Proof audit

Push `e^{itF}dP_H` to `W`; its complex density `a_t` satisfies `|a_t|<=p_W`, hence `||a_t||_2^2<=M_H`. Plancherel after the dilation `xi=2t(l+beta)` gives exactly

`int |hat a_t(2t(l+beta))|^2 dl <= M_H (pi/|t|)^k`.

Push `e^{itR}dP_X'` to the linear variable `M X'` and call the complex density `mu_t`. Cauchy--Schwarz yields

`|phi_Q(t)|^2 <= M_H (pi/|t|)^k ||mu_t||_2^2`.

For rough laws, mollify this pushforward. Expanding the square introduces an independent copy only of the literal `J` bank. If `D=X_J-X'_J`, its coordinates are still independent and cap one. Cauchy--Schwarz in the literal `I` product bank cancels the pure-`I` phase and produces physical scalar characteristic functions. The mollified `L^2` norm is bounded by integrals of the form

`E[kappa(M_JD) prod_i |psi_i(2t<a_i,D>)|]`,

with `kappa` a probability-density approximate identity. This bound is uniform, so weak lower semicontinuity/Fatou passes to `mu_t`; no smoothness premise is inserted.

Write each crossing row `a_i=c_i+lambda_i M_J`, with `c_i` perpendicular to `row(M_J)`. Weighted Holder over determinant subsets gives `T`-integrals with exponent `1/alpha_i`. The map

`D -> (M_JD,(<c_i,D>)_(i in T))`

has Gram determinant

`S^2 det(C_TC_T^T)`.

The baseline general-linear-image form of the product-projection estimate therefore gives joint density cap

`e^(d/2)/[S sqrt(det(C_TC_T^T))]`.

Because `alpha_i<=1/2`, the scalar Fourier-power lemma at `p=1/alpha_i` gives

`int |psi_i(2t(y+u))|^(1/alpha_i) dy
 <= pi sqrt(2e alpha_i)/|t|`.

The determinant-weighted geometric mean contributes

`Z_ell^-1/2 exp(H(w)/2)`,

while the marginal factors contribute

`exp[(1/2)sum_i alpha_i log alpha_i]`.

Order a random `ell`-subset uniformly. Entropy subadditivity gives

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!)`:
indeed `H(ordered)=H(w)+log(ell!)`, while each ordered coordinate has law `alpha_i/ell`, so the sum of its `ell` marginal entropies is `-sum alpha_i log alpha_i+ell log ell`.

Combining these estimates and taking the square root gives the displayed `K_(k,ell)` exactly. Finally

`int_R min(1,K|t|^-d/2)dt = [2d/(d-2)] K^(2/d)`

and Fourier inversion cancels the factor `pi`, proving the density estimate. All rotations here are deterministic Gram/Jacobian operations, never claims of independence of projected random coordinates.

## 3. Exact-rank terminals

If `r` literal physical rows cross a product bank through a rank-`r` matrix `P`, the same complex-pushforward/Plancherel argument gives

`|phi(t)| <= min(1, pi^(r/2)e^(r/4) det(PP^T)^(-1/4)|t|^(-r/2)).`

Therefore

`r=3: ||p||_infinity <= 3 sqrt(e) det(PP^T)^(-1/6)`,

and

`r=2: sup_a E|Q-a|^-1/2 <= 4 sqrt(2)e^(1/4) det(PP^T)^(-1/8)`.

Same-bank quadratic and affine phases remain inside the complex pushforwards.

## 4. Marginal-free third crossing volume

For a literal cross matrix `B`, set

`Z=E_3(B)=e_3(BB^T)`.

Let `J_i` be the incident determinant mass of triples containing physical row `i`; `sum_i J_i=3Z`.

- If every `J_i/Z<=1/2`, use the compiler at `(k,ell,d)=(0,3,3)`.
- If `J_i>Z/2`, promote that literal row `w`. Project the other rows off `w`; exact Gram--Schmidt gives
  `J_i=||w||^2 e_2(CC^T)`.
- If a residual row is heavy for this `E_2`, promote it. For the two promoted rows `P` and residual `C_2`, exact base-times-height gives
  `H_ij=det(PP^T)||C_2||_F^2>J_i/2>Z/4`.
- If a final residual row is heavy for one-volume, the literal three-row Gram determinant is `>H_ij/2>Z/8` and the exact-rank-three terminal applies.

The compiler parameters along the four branches are `(0,3)`, `(1,2)`, `(2,1)`, and the rank-three terminal. The largest coefficient is

`C_3=3 sqrt(2)e(9/2)^(1/6)=14.818337662843...`.

Thus, with no row-marginal assumption,

`boxed: ||p_Q||_infinity <= C_3 E_3(B)^(-1/6).`

Every branch has an `L^1` characteristic-function envelope, so this receiver gives a `C_0` density.

## 5. Marginal-free second crossing volume

For `Z=E_2(B)>0`, use the same promotion tree one order lower.

- diffuse `E_2`: compiler `(k,ell,d)=(0,2,2)` gives a `|t|^-1` envelope;
- one heavy physical row: promote it and use `(1,1,2)` if the residual one-volume is diffuse;
- heavy residual row: use the exact-rank-two terminal.

The Riesz identity and

`int_R min(1,L/|t|)|t|^-1/2 dt=8 sqrt(L)`

give the uniform half-potential

`boxed: sup_a E|Q-a|^-1/2 <= C_2 E_2(B)^(-1/8),`

with

`C_2=8 sqrt(e)2^(-1/8)=12.095072570796...`.

This is a half-potential theorem, not a rank-two bounded-density theorem.

## 6. Complete nine-direction proof

Continue with `K=s=1`.

### No physical pivot

If `A` has no `eta`-pivot and `s_9(A)>=1`, the audited baseline structural theorem at order three gives

`V_3(A)>=kappa^3`.

A fair original-coordinate cut supplies `B=A[I,J]` with

`E_3(B)>=4^-3 kappa^3`,

hence `E_3(B)^(-1/6)<=160`. Therefore

`||p_Q||_infinity <=160 C_3=2370.93402605488...<2400`.

### Scalar pivot

If `|A_hh|>=eta`, complete the square only in the original scalar `X_h`. The Schur complement retains at least eight unit-scale eigenvalue moduli.

If that Schur complement has a physical pivot, the audited baseline pivot proposition requires only two large directions and gives truncated half-potential at most `600`; the tail outside unit distance contributes at most one, so the full half-potential is `<=601`.

If it has no pivot, then it has at least five unit-scale directions. The structural theorem at order two and a fair cut give

`E_2>=4^-2 kappa^2`.

The new order-two receiver gives

`sup_a E|R-a|^-1/2
 <= C_2 (4^-2 kappa^2)^(-1/8)
 = C_2 sqrt(160)
 =152.99191115498...<153`.

Thus in both scalar-pivot subbranches the Schur remainder has full half-potential `<=601`. The scalar square profile costs `eta^-1/2=10`, giving

`||p_Q||_infinity<=6010`.

### Two-coordinate pivot

A definite principal pair of determinant modulus at least `eta` gives direct conditional density `<=pi/sqrt(eta)=10pi<32`.

For an indefinite pair, the Schur complement retains at least seven unit-scale directions, hence operator norm at least one. The audited hyperbolic-pair envelope plus the quarter-power logarithmic-potential bound gives `<251` exactly as in the baseline manuscript.

The no-pivot, scalar, definite-pair and indefinite-pair alternatives exhaust the normalized problem, and `6010` is the largest bound.

## 7. Scaling

For general `K,s`, put `Y=KX` and

`Qtilde=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c=(K^2/s)Q`.

The coordinates of `Y` are cap one and `s_9(A/s)>=1`. Density scaling therefore gives

`boxed: ||p_Q||_infinity<=6010 K^2/s.`

This is a complete replacement theorem with its constants and dependency map. It does not use the order-five branch of the 17-eigenvalue proof.

## 8. Dependency map

`baseline Fourier/Gaussian/Riesz`
` -> baseline geometric BL -> baseline product projections -> baseline scalar Fourier powers`
` -> grouped compiler -> marginal-free E_3 density + marginal-free E_2 half-potential`
` -> [baseline k=3 structural volume + fair cut] for no-pivot`
` -> [baseline Schur + pivot profiles + k=2 structural volume] for scalar pivot`
` -> pair pivots`
` -> normalized s_9 theorem -> K,s scaling`.

No external paper is a hidden dependency: the exact analytic estimates are proved in the baseline/compiler chain. BCCT and RV are antecedent citations only; their primary-source scopes were separately verified in the B18 audit.

## 9. Why I do not lower nine to eight

The present structural argument can fail at `s_8` only in the terminal order-two sampled seed. The audited terminal reduction gives a rank-six global correction with a rank-two restriction, two large diagonal directions outside the seed, and a uniformly invertible physical two-coordinate block in the interpolant; all three nominal rank-two pieces of the global correction are quantitatively saturated. This is substantially narrower than an arbitrary no-pivot matrix, but no complete bounded-density receiver for it is currently proved.

Analytically, the generic order-two grouped compiler has total smoothing dimension `d=2` and only a `|t|^-1` Fourier envelope: enough for the negative-half-potential after multiplying by `|t|^-1/2`, but not enough for direct `L^1` inversion. A recent potential-to-log fusion shows that this order-two Schur currency cancels the logarithmic part of the small indefinite-pair singularity, leaving the nonlogarithmic `6D^-1/2` term and aggregate-to-local provenance as the live obstruction. That is real progress, but not a complete `s_8` proof.

Therefore the lowest complete threshold I certify in this run is **9**. Threshold eight and the unrestricted three-eigenvalue problem remain OPEN.
