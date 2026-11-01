# fleet01/B19 — independently reviewed nine-eigenvalue improvement

Run: `20260924T135026Z-fleet01-B19-fixed-mult-audit`  
Baseline: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Status: **proved candidate improvement in this B19 reconstruction; not a self-awarded independent-validation certificate.** The unrestricted three-eigenvalue conjecture remains open.

## Theorem

Let `X=(X_1,...,X_n)` have independent real coordinates with probability densities bounded by `K<infinity`. Let `A=A^T` be arbitrary, let `b in R^n`, `c in R`, and assume

` s_9(A) >= s > 0.`

Then `Q=X^T A X+b^T X+c` has an essentially bounded density and

`boxed: ||p_Q||_infinity < 3078 K^2/s.`

The no-pivot branch has a continuous `C_0` density. Global continuity is not asserted. All signs, all remaining spectrum, arbitrary affine terms and arbitrary rough independent coordinate laws are retained.

The proof below combines the audited baseline with the grouped physical product-Fourier compiler first written in fleet03/B04 and the constant-sharpening idea in fleet03/B13. I independently reconstructed the equations needed from both rather than accepting their labels as validation.

## 1. Marginal-free order-three and order-two crossing receivers

Let `M` be a literal original-coordinate cross block of a quadratic polynomial; all same-bank quadratic phases and all affine terms are retained. Put

`E_k(M)=e_k(M M^T)`.

The fleet03/B04 grouped compiler proves, and I independently checked at the equation level, the two unconditional physical-crossing estimates

`boxed: ||p_Q||_infinity <= C3 E_3(M)^(-1/6),`

`C3 = 3 sqrt(2) e (9/2)^(1/6) = 14.818337662843...`,

and

`boxed: sup_a E |Q-a|^(-1/2) <= C2 E_2(M)^(-1/8),`

`C2 = 8 sqrt(e) 2^(-1/8) = 12.095072570796...`.

The first conclusion has an integrable characteristic-function envelope and hence a continuous `C_0` density. The second is a half-potential estimate, not a rank-two density claim.

### 1.1 Equation-level reconstruction of the grouped compiler

The general compiler has disjoint physical banks `H,I,J`. A `k`-dimensional physical projection `W` of `X_H` has density cap `M_H`; the opposite light variables enter through a rank-`k` linear map with nonzero singular-value product `S`. After projecting residual crossing rows orthogonally away from that rank-`k` row space, let `C_T` denote an `ell`-row residual submatrix and

`Z_ell = sum_{|T|=ell} det(C_T C_T^T)>0`.

Give each `ell`-set weight

`w_T=det(C_T C_T^T)/Z_ell`,

and let `alpha_i=P_w(i in T)`. If `alpha_i<=1/2`, then with `d=k+ell`,

`|phi_Q(t)| <= min(1,K_{k,ell}|t|^(-d/2))`,

where

`K_{k,ell}
 = M_H^(1/2) pi^(d/2) 2^(ell/4) e^((k+2ell)/4)
   (ell^ell/ell!)^(1/4) S^(-1/2) Z_ell^(-1/4).`

I checked the proof as follows.

1. Push the complex measure `exp(itF)dP_H` to `W`. Its density `a_t` satisfies `|a_t|<=p_W`, hence `||a_t||_2^2<=M_H`. Plancherel after the scale `2t` gives

   `int |hat a_t(2t(y+beta))|^2 dy <= M_H (pi/|t|)^k`.

2. Push `exp(itR)dP_light` to the opposing rank-`k` linear variable. Regularize the resulting complex measure by convolution, expand its `L^2` norm with an independent copy of the physical `J` bank, and condition on the difference `D=X_J-X'_J`. Pure `J` phases have modulus one and the `I` coordinates produce physical one-dimensional characteristic factors. The difference coordinates remain independent with cap-one densities. The regularized kernel in the rank-`k` variable is a probability density, so the estimate is uniform in the regularization; weak `L^2` compactness closes the limit.

3. For a sampled residual set `T`, decompose each residual row as its component in the rank-`k` row space plus an orthogonal component `c_i`. The map

   `D -> (M_JD,(<c_i,D>)_{i in T})`

   has Gram determinant

   `S^2 det(C_T C_T^T)`.

   The baseline product-projection theorem therefore gives its density cap

   `e^(d/2)/(S sqrt(det(C_T C_T^T)))`.

4. Weighted Holder uses the powers `1/alpha_i>=2`. The baseline scalar Fourier-power estimate gives

   `int |psi_i(2t(y+u))|^(1/alpha_i) dy
    <= pi sqrt(2e alpha_i)/|t|`.

5. The determinant-weighted geometric mean is exactly

   `Z_ell^(-1/2) exp(H(w)/2)`,

   while the marginal factors contribute `exp((1/2)sum_i alpha_i log alpha_i)`. Ordering a random sampled `ell`-set uniformly and using entropy subadditivity gives

   `H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!)`.

Combining these identities and the first Plancherel factor gives the stated `K_{k,ell}`. If `d>2`, integration of the envelope yields

`||p_Q||_infinity
 <= [d/(d-2)] M_H^(1/d) 2^(ell/(2d)) e^((k+2ell)/(2d))
    (ell^ell/ell!)^(1/(2d)) S^(-1/d) Z_ell^(-1/(2d)).`

No random-variable rotation is used.

### 1.2 Removing leverage restrictions at order three

Let `Z=E_3(M)`. If every physical row carries at most half the canonical three-volume mass, apply the preceding estimate at `(k,ell,d)=(0,3,3)` to get the constant `C3` directly.

If a row `w` carries incident mass `J_i>Z/2`, project all other physical rows orthogonally off `w`, obtaining `C`. Gram-Schmidt gives the exact identity

`J_i=||w||^2 E_2(C)`.

If the residual order-two row marginals are diffuse, use `(k,ell,d)=(1,2,3)`. Otherwise promote a second physical row. If `P` is the two-row promoted matrix and `C_2` is the remainder after projection off its row space, the heavy marginal identity is

`det(PP^T) ||C_2||_F^2 > J_i/2 > Z/4`.

Use `(k,ell,d)=(2,1,3)` if the remaining one-volume is diffuse. If one more physical row is heavy, the promoted three-row Gram determinant exceeds `Z/8`, and the exact-rank-three physical crossing estimate

`||p_Q||_infinity <=3 sqrt(e) det(P_3P_3^T)^(-1/6)`

closes the branch. The four constants are respectively `<14.819`, `<10.958`, `<8.264`, and `<7`, so `C3` dominates.

The order-two promotion is identical one level lower: diffuse `E_2`, one promoted row plus diffuse residual one-volume, or a promoted physical pair. The exact-rank-two Riesz estimate is

`sup_a E|Q-a|^(-1/2)
 <=4 sqrt(2) e^(1/4) det(PP^T)^(-1/8)`,

and every branch is bounded by `C2 E_2(M)^(-1/8)`.

Thus the two receivers above are valid for every literal physical cross block, with arbitrary same-bank curvature and affine phases retained.

## 2. Independent sharpening of the pivot half-potential

Keep the baseline parameters

`eta=1/100`, `kappa=1/80^2`.

The baseline proof rounds several constants. The following sharpenings retain every hypothesis.

### 2.1 Exact singular kernel

For

`J(d)=int_{-1}^1 |x|^(-1/2)|x-d|^(-1/2) dx`,

symmetry reduces to `d>0`. Direct substitutions give

- if `0<d<=1`,

  `J(d)=2 asinh(d^(-1/2))+pi+2 acosh(d^(-1/2));`

- if `d>=1`,

  `J(d)=2 asinh(d^(-1/2))+2 asin(d^(-1/2)).`

For `0<d<=1`, put `y=d^(-1/2)>=1`. Since

`asinh y < log((1+sqrt2)y)`, `acosh y <=log(2y)`,

we obtain

`J(d) < pi+2log(2+2sqrt2)+4log y < 7+2log(1/d)`.

For `d>=1`, both inverse functions increase with `d^(-1/2)<=1`, so `J(d)<=2asinh1+pi<7`. Hence

`boxed: J(d)<7+2log_+(1/|d|).`

### 2.2 Quarter-power logarithmic constant

The exact coefficient in the baseline Gaussian-smoothing calculation is

`Cq=2^(5/8) pi^(-1/4) e^(3/8) Gamma(3/8)`.

A fully elementary bound gives `Cq<9/2`. On `[0,1]`, the even Taylor truncation

`e^{-x} <= 1-x+x^2/2-x^3/6+x^4/24`

and on `[1,infinity)`, `x^(-5/8)<=1`, yield

`Gamma(3/8)<1250243/592515 + e^(-1)<5/2`;

the last inequality uses `e>8/3`. Also

`2^(5/8)<31/20`, `pi^(-1/4)<19/25` (already from `pi>3`), and `e^(3/8)<3/2`, so the coefficient is in fact below

`(31/20)(19/25)(3/2)(5/2)<9/2`.

Thus the quarter-power lemma may be sharpened to

`P{|R-a|<rho} <= min(1,(9/2)(rho/L)^(1/4))`,

and for `L>=1`,

`boxed: sup_a E log_+(1/|R-a|) <= L0*=4+4log(9/2).`

### 2.3 All physical pivots

At a scalar pivot, the exact profile and the sharpened `J` bound give

`H(Q) <=10[7+2L0*] <278`.

At a definite pair,

`H(Q)<=40pi<126`.

At an indefinite pair with `D=|det B|>=1/100`, retain the exact hyperbolic middle constant `(15/2)log2`. Integration of the shifted logarithmic kernel gives

`H(Q)<=D^(-1/2)[8+30log2+4log(16sqrt D)].`

Writing `y=sqrt D>=1/10`, the right side is decreasing in `y`, so

`H(Q)<=10[8+30log2+4log(8/5)].`

For an entirely rational numerical certification, let

`r1=13863/20000`, `r2=117501/250000`.

The seventh positive Taylor partial sums of `exp(r1)` and `exp(r2)` exceed `2` and `8/5` respectively, so `log2<r1`, `log(8/5)<r2`. Since

`30r1+4r2=22.674516<22.675`,

we obtain

`boxed: every eta-pivot under the two-direction hypothesis has H(Q)<306.75.`

This proof is independent of the numerical assertion in the peer note.

## 3. Nine large eigenvalues suffice

Normalize to `K=s=1` and assume `s_9(A)>=1`.

### 3.1 No physical pivot

The audited baseline spectral-to-volume proposition with `k=3` gives

`V_3(A)>=kappa^3`.

A fair original-coordinate cut has a literal cross block `M` with

`E_3(M)>=4^(-3) kappa^3`,

hence

`E_3(M)^(-1/6)<=2 kappa^(-1/2)=160`.

The marginal-free order-three receiver gives

`||p_Q||_infinity <=160 C3
 =2370.934026...<2371`.

This branch has a continuous `C_0` density.

### 3.2 Scalar physical pivot

Suppose `|A_hh|>=eta`. Complete the square only in the original variable `X_h`. By the audited Schur count, the Schur complement `S` retains at least eight unit-scale eigenvalue magnitudes.

If `S` has an `eta`-pivot, the strengthened pivot result above gives truncated half-potential `<306.75`; the tail `|R-a|>1` costs at most one, so

`sup_a E|R-a|^(-1/2)<307.75`.

If `S` has no pivot, then `s_5(S)>=1`. The baseline proposition at `k=2` and a fair cut yield

`E_2(M_S)>=4^(-2)kappa^2`.

The marginal-free order-two receiver gives

`sup_a E|R-a|^(-1/2)
 <=C2 sqrt(160)
 =152.991911...<153`.

Thus in all scalar-pivot subcases the Schur half-potential is `<307.75`. The square profile contributes `eta^(-1/2)=10`, so

`boxed: ||p_Q||_infinity<3077.5<3078.`

### 3.3 Pair pivots

For a definite physical pair, the baseline two-dimensional bound gives

`||p_Q||_infinity<=10pi<32`.

For an indefinite physical pair, the Schur complement retains at least seven unit-scale eigenvalues, hence operator norm at least one. The baseline hyperbolic-pair/logarithmic-potential argument already gives `<251`, far below the scalar-pivot maximum.

These cases exhaust the normalized theorem.

### 3.4 Scaling

For general `K,s`, put `Y=KX` and

`Qtilde=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c`.

Then `s_9(A/s)>=1`, the coordinates of `Y` have density cap one, and

`Q=(s/K^2)Qtilde`.

Therefore

`boxed: ||p_Q||_infinity<3078 K^2/s.`

## 4. Dependency map and review status

Dependencies are closed by:

1. the baseline manuscript lemmas audited independently in this B19 run;
2. the grouped physical product-Fourier compiler of fleet03/B04, whose Plancherel, product-projection, weighted-Holder, entropy and physical-row promotion equations were independently reconstructed in Section 1 here;
3. the sharpened pivot calculations rederived in Section 2 here.

No Gaussian-only, bounded-support, diagonal, exact-rank, leverage-restricted, post-rotation-independence or smooth-density hypothesis has been introduced.

This B19 report is one genuinely separate complete mathematical review of the nine-eigenvalue replacement argument. It does **not** mark the candidate independently validated; the owner's release gate still requires two genuinely separate complete reviews to be reconciled.

## 5. Why I do not claim eight

The same interpolation route has a real terminal collar at multiplicity eight. In the no-pivot state, if the order-three conclusion fails (`V_3<kappa^3`), the lower-order baseline propositions force `V_1>=kappa`, `V_2>=kappa^2`, so the unique bad sampled ratio is `r=2`. The audited completion then has

`||E||_F<=3/80`, `rank R<=6`, `rank R[L,L]<=2`.

From `s_8(A)>=1`, singular-value perturbation gives

`s_2(D)>=77/80`.

If three entries of `D` exceeded

`beta=eta+2(1/7+3/80)=519/1400`,

the corresponding `3x3` block of `R[L,L]` would be strictly diagonally dominant, contradicting rank at most two. Hence

`s_3(D)<=519/1400`.

The singular-value sum inequality then forces

`s_6(R)>=77/80-519/1400=1657/2800`.

Thus all six available global correction directions are genuinely active while the restricted block remains rank two. The exact rank bounds are simultaneously sharp even inside the no-pivot entry regime (direct sums of `(1/200)[[0,1,1],[1,0,1],[1,1,1]]` realize `rank R=3r` and `rank R[L,L]=r`). Consequently a bookkeeping-only `3r ->2r` improvement is impossible.

Peer work further extracts determinant chains and nested physical stars from this `s_8` chamber, but no reviewed receiver presently consumes those currencies under arbitrary rough product laws. I therefore classify

`8 eigenvalues => universal density bound`

as **GAP / NOT PROVED in this run**, not as false.

The strongest unconditional multiplicity reduction I can support end-to-end here is therefore **17 -> 9**, with constant `<3078 K^2/s`.
