# fleet02/B18 — independent review of the nine-direction replacement, with counterexample boundaries

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Baseline manuscript pin: commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

Lower-threshold proof audited here: fleet02/B01 `QFORM-FIXED-MULTIPLICITY-9-B01-REVIEWED-v1`, file blob `7ad10848181dcbd9b962803bd7f61e2bf446907a`, read from live master after independently completing the baseline audit.

## Verdict

**PASS after two explicit endpoint conventions recorded below.** The reviewed replacement proves, with all baseline hypotheses unchanged,

\[
 s_9(A)\ge s>0\quad\Longrightarrow\quad
 \|p_{X^TAX+b^TX+c}\|_\infty\le 6010\,K^2/s.
\]

No global continuity theorem is claimed. No moment, support, iid, sign, log-concavity, diagonal-basis, exact-rank, leverage, or post-rotation-independence assumption is added. This file is an independent B18 review, not a self-awarded release certificate. The unrestricted three-eigenvalue conjecture remains open.

The two endpoint issues in the reviewed B01 writeup are **minor notation/exposition gaps with complete zero-loss repairs**:

1. If a subset marginal `alpha_i=0`, the expression `1/alpha_i` is undefined. Repair: omit that factor before weighted Holder, using `|psi_i|<=1`. The positive-marginal indices still satisfy the Holder exponent identity. This changes no constant.
2. The order-three balanced branch uses the formal `k=0` case of the grouped compiler. Repair: treat the hub bank as absent, set the empty singular-value product to one and the zero-dimensional density cap to one, or run the light-bank half of the same proof directly. Again no constant changes.

With those conventions explicit, I find no unpaid implication in the nine-direction argument.

## 1. Grouped product-Fourier compiler — independent reconstruction

Let `H,I,J` be disjoint original-coordinate banks, `W` a `k`-dimensional orthogonal projection of `X_H` with density cap `M_H`, and

`Q=F(X_H)+2<W,M X'+beta>+R(X')`, `X'=(X_I,X_J)`.

Assume `M_J` has row rank `k`, let `S` be the product of its nonzero singular values, and put

`C=(A_R)_[I,J](I-Pi_row(M_J))`.

For weighted `ell`-row Gram minors, write `Z_ell=sum_T det(C_T C_T^T)`, `w_T=det(C_T C_T^T)/Z_ell`, and `alpha_i=P_w(i in T)`. After dropping zero-marginal factors, assume `0<alpha_i<=1/2`.

### Hub-bank L2 step — PASS

Push `e^{itF}dP_H` to `W`. Its complex density `a_t` satisfies `|a_t|<=p_W`, hence `||a_t||_2^2<=M_H`. Plancherel at scale `2t` gives

`int |hat a_t(2t(l+beta))|^2 dl <= M_H (pi/|t|)^k`.

Pushing the remaining phase to `MX'` with complex density `mu_t` and applying Cauchy--Schwarz yields

`|phi_Q(t)|^2 <= M_H(pi/|t|)^k ||mu_t||_2^2`.

### Light-bank reduction — PASS

Regularize the conditional pushforward, condition on one literal value `X_I=x`, expand the squared `L2` norm using only an independent copy of the `J` bank, and then average over the original independent `I` coordinates. Pure `I` phases cancel; pure `J` phase differences have modulus one. With `D=X_J-X'_J`, the surviving cross phase is

`2 x^T(A_R)_[I,J]D`,

so the `I` average gives the literal product of scalar characteristic functions `prod_i |psi_i(2t<a_i,D>)|`. The regularizer contributes a probability kernel in `M_JD`. The coordinates of `D` remain independent and have density caps at most one. Uniform mollified `L2` bounds pass to the limiting complex pushforward by weak compactness/lower semicontinuity.

No conditional density cap is turned into independence, and no rotated coordinates are declared independent.

### Weighted subset step — PASS

Decompose `a_i=c_i+lambda_i M_J`, with `c_i` orthogonal to `row(M_J)`. For a positive-weight `ell`-set `T`, the stacked map

`D -> (M_JD,(<c_i,D>)_{i in T})`

has Gram determinant exactly

`S^2 det(C_T C_T^T)`.

The baseline product-projection lemma therefore gives density cap

`e^(d/2)/(S sqrt(det(C_T C_T^T)))`, `d=k+ell`.

Weighted Holder and the baseline scalar Fourier-power estimate at `p_i=1/alpha_i` give

`int |psi_i(2t(y+u))|^(1/alpha_i)dy <= pi sqrt(2e alpha_i)/|t|`.

The determinant geometric mean is `Z_ell^(-1/2) exp(H(w)/2)`. Uniformly order `T`; entropy subadditivity gives

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!)`.

Thus

`|phi_Q(t)| <= min(1,K_{k,ell}|t|^(-(k+ell)/2))`,

with

`K_{k,ell}=M_H^(1/2) pi^((k+ell)/2) 2^(ell/4) e^((k+2ell)/4)
             (ell^ell/ell!)^(1/4) S^(-1/2) Z_ell^(-1/4)`.

For `d=k+ell>2`, direct inversion gives

`||p_Q||_infinity <= [d/(d-2)] M_H^(1/d) 2^(ell/(2d)) e^((k+2ell)/(2d))
 (ell^ell/ell!)^(1/(2d)) S^(-1/d) Z_ell^(-1/(2d))`.

All exponents and Fourier factors were independently recomputed.

## 2. Terminal exact-rank bounds — PASS

With `r` promoted literal physical rows and no residual projected crossing, the same argument, discarding aligned residual phases by modulus, gives

`|phi(t)| <= min(1, pi^(r/2)e^(r/4) det(PP^T)^(-1/4)|t|^(-r/2))`.

Therefore

- `r=3`: `||p||_infinity <=3 sqrt(e) det(PP^T)^(-1/6)`;
- `r=2`: `sup_a E|Q-a|^(-1/2) <=4 sqrt(2)e^(1/4) det(PP^T)^(-1/8)`.

Same-bank and affine phases remain retained inside the complex pushforward.

## 3. Marginal-free order-three receiver — PASS

For a literal cross block `M`, let `Z=E_3(M)` and let `J_i` be incident third-volume mass. `sum_i J_i=3Z`.

The finite promotion tree is exact:

1. all `J_i/Z<=1/2`: use `(k,ell)=(0,3)`;
2. a heavy row `w`: Gram--Schmidt gives `J_i=||w||^2 E_2(C)`; if residual second-volume marginals are balanced, use `(1,2)`;
3. a second heavy row: with promoted pair `P`, `H_ij=det(PP^T)||C_2||_F^2>J_i/2`; if first-volume marginals are balanced, use `(2,1)`;
4. a third heavy row yields `det(P_3P_3^T)>H_ij/2` and the terminal rank-three bound.

The largest constant is

`C_3=3 sqrt(2)e(9/2)^(1/6)=14.818337662843...`,

so

`||p_Q||_infinity <= C_3 E_3(M)^(-1/6)`.

The other branch constants independently recompute to `<10.958`, `<8.264`, and `<7` after the heavy-mass factors.

## 4. Marginal-free order-two full half-potential — PASS

The one-dimension-lower promotion tree gives

`sup_a E|Q-a|^(-1/2) <= C_2 E_2(M)^(-1/8)`,

with

`C_2=8 sqrt(e)2^(-1/8)=12.095072570796486...`.

The promoted branch constants recompute to `9.787976518...` and `8.637858959...`, so `C_2` dominates.

This is deliberately a half-potential theorem, not a rank-two density theorem.

## 5. Complete nine-direction theorem — PASS

Normalize `K=s=1` and keep `eta=1/100`, `kappa=1/6400`.

- **No pivot:** the audited baseline spectral-to-volume theorem at `k=3` gives `V_3>=kappa^3`; a fair original-coordinate cut gives `E_3>=4^-3 kappa^3`, hence `E_3^-1/6<=160`. The new receiver gives `160 C_3=2370.93402605488...<2400`.
- **Scalar pivot:** the Schur complement retains at least eight unit spectral directions. If it has any baseline pivot, the audited pivot proposition gives truncated half-potential `<=600`, hence full `<=601`. If it has no pivot, then `s_5>=1`; baseline `k=2` volume plus a fair cut gives `E_2>=4^-2 kappa^2`, and the new receiver gives `C_2 sqrt(160)=152.99191115498...<153`. Thus the scalar square profile costs at most `eta^-1/2*601=6010`.
- **Definite pair:** the baseline joint-density argument gives `<32`.
- **Indefinite pair:** Schur leaves at least seven unit directions, hence operator norm at least one; the baseline hyperbolic/log-potential branch applies verbatim and gives `<251`.

The maximum is `6010`. Rescaling `Y=KX` gives exactly `6010 K^2/s`.

### Closed dependency map

The replacement imports only already-audited baseline Fourier/Riesz identities, geometric BL/product projection/scalar Fourier powers, Schur and pivot estimates, and the disjoint-minor sampling/completion/spectral-to-volume/fair-cut skeleton. The grouped compiler is proved directly from those pieces; the order-three and order-two receivers are finite physical-row promotion trees. It does not depend on the baseline 17-direction theorem itself.

## 6. Counterexample boundaries

### 6.1 Generic order-two density endpoint is FALSE

Let `U,V` be independent uniform variables on `[-1,1]`; their densities are `1/2<=1`. The density of `U^2` is

`f(s)=1/(2 sqrt(s))`, `0<s<1`.

Therefore the density of the indefinite rank-two quadratic `U^2-V^2` at zero has the lower/formal convolution value

`int_0^1 f(s)^2 ds = (1/4)int_0^1 ds/s = infinity`.

So a theorem asserting a universal bounded density from an arbitrary indefinite rank-two physical quadratic packet is false. This is exactly why the order-two receiver above is used only for a half-potential. It does **not** disprove an eight-eigenvalue theorem, which has additional structure.

### 6.2 The `4r+1` terminal count cannot be changed to `4r` from the interpolation rank bounds alone

Consider

```
A = [[-2,-1,-6,-9],
     [-1, 0, 1, 1],
     [-6, 1,-8,-1],
     [-9, 1,-1, 2]],
S={1}, T={2}  (one-based).
```

Here `B=A[S,T]=[-1]`. The manuscript interpolation is

```
P = [[-2,-1,-6,-9],
     [ 0, 0, 0, 0],
     [ 2, 1, 6, 9],
     [ 2, 1, 6, 9]],
```

and the completion gives

```
D=diag(0,0,-14,-7),
E[3,4]=-10, E[4,3]=-7,
R=[[-2,-1,-6,-9],
   [-1, 0, 1, 1],
   [-6, 1, 6, 9],
   [-9, 1, 6, 9]].
```

Exact ranks are

`rank P=1`, `rank R=3`, `rank R[L,L]=1`, but `rank(D+R)=4`.

Taking four block-diagonal copies gives the saturated `r=4` algebraic pattern

`rank P=4`, `rank R=12`, `rank R[L,L]=4`, `rank(D+R)=16`.

Thus the inequalities `rank R<=3r` and `rank R[L,L]<=r` by themselves cannot replace the manuscript's `4r+1` contradiction by `4r`. This is **not** a counterexample to a 16- or eight-direction density theorem: the displayed matrix is not asserted to satisfy the normalized no-pivot hypotheses. It is a counterexample to the naive proof strengthening that changes only the rank count.

## 7. Threshold conclusion

This review accepts the complete **nine-eigenvalue** replacement, with the two endpoint conventions made explicit above. I do **not** claim eight. The current eight-direction debt is genuinely overlap-sensitive: a rank-two half-potential alone cannot be promoted to a density bound, while the terminal structural collar carries more information than a bare rank-two packet. A valid eight-direction theorem would need a new product-preserving receiver that spends that extra overlap/multi-bank geometry without dividing by a possibly vanishing physical diagonal.

The unrestricted three-eigenvalue QFORM problem remains open.
