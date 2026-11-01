# fleet03/B10 r11 — independent constants/audit pass and threshold-nine reconstruction

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T131348Z-fleet03-B10-FIXMULT-r11`  
Role lens: all constants, exact arithmetic, adversarial finite examples; fleet03 emphasis on exact identities and alternative derivations.  
Canonical baseline manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, declared SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.  
Fresh `master` observed immediately before publication through `d2ae3d3878703809e7d7b70cf47f0db7a6740553`.

## Executive verdict

**Baseline 790-line manuscript: PASS in this independent mathematical review.** I reread the complete source and rechecked all dependencies used by the fixed-multiplicity theorem. I found no fatal mathematical defect in the stated seventeen-eigenvalue theorem. The singular-ambient Schur-complement paragraph is valid as written once its final “continuity” sentence is read in terms of the ordered absolute eigenvalues/singular values; a competing report that labels the moving threshold a gap is overly cautious. I give the explicit one-line order-statistic argument below.

**Nine-eigenvalue improvement: PASS in this independent reconstruction.** I independently checked the grouped product-Fourier compiler, its physical-row promotion tree, the order-three density receiver, the order-two half-Riesz receiver, and their use with the manuscript interpolation theorem. Thus

\[
 s_9(A)\ge s>0
 \Longrightarrow
 X^TAX+b^TX+c\text{ has an essentially bounded density.}
\]

The repository already contains two genuinely separate full PASS reconstructions of this nine-direction candidate, fleet01/B16 at `54ec2a651d854563f8d7249ff9a8cf7006d` **(note: see correction below for the exact commit)** and fleet03/B08 at `c02a08f19d010e508578695a5906744fdbcfcd70`; the canonical source addendum at `fe715611a677e15c0498e2284284b540651218f5` records the two-review condition as met. The exact fleet01/B16 commit is `54ec2a651d854563f8db0d92c4c3426f76551786`. I do not unilaterally alter the owner's release baseline here.

**New result of this B10 run:** the same nine-eigenvalue proof admits the simpler sharpened universal constant

\[
\boxed{\ \|p_{X^TAX+b^TX+c}\|_\infty<2600\,K^2/s.\ }
\]

This improves the previously recorded `<3110 K^2/s` nine-direction constant. It uses no new probabilistic assumption. The improvement comes from (i) an exact sharper singular-kernel inequality, (ii) the already independently derived rational certificate for the quarter-power coefficient, and (iii) a new optimized physical-coordinate tail split in the hyperbolic pair estimate.

Global continuity is **not** proved: the no-pivot order-three Fourier branch is `C_0`, while the pivot branches are used through measure domination. The unrestricted three-eigenvalue conjecture remains open.

## 1. Complete baseline source audit

I reread all 790 source lines and reconstructed the proof chain. Status below concerns the literal baseline source.

| Source range | Status | Independent check |
|---|---|---|
| 1–83 | PASS | The theorem quantifiers retain arbitrary dimension, signature, affine terms, remaining spectrum, and arbitrary independent cap-`K` coordinate laws. Scaling target is `K^2/s`. |
| 84–168 | PASS | Gaussian inversion, Plancherel, power-envelope integration, and the half-Riesz normalization are consistent with `hat f(t)=int e^{itx}f(x)dx`. |
| 169–217 | PASS | Nonsymmetric singular-value perturbation is valid. The Schur count is valid for invertible and singular ambient matrices; strict diagonal dominance is standard and is used only as a rank contradiction. |
| 221–301 | PASS | Heat-flow Brascamp–Lieb sign and limits check. Product projection uses a deterministic orthogonal change only in the integral and never claims rotated independence. Scalar Fourier powers use genuine independent signed copies. |
| 302–400 | PASS | Decoupling powers two/four, graph-frame Jacobians, entropy factors, `alpha=(2pi e)^2`, determinant exponent `-1/8`, and Cauchy–Binet volume coefficients rederive correctly. |
| 401–525 | PASS | Square profile, definite pair, hyperbolic coarea, original-coordinate tail control, quarter-power concentration, and logarithmic potential are all dependence-safe. |
| 526–630 | PASS | Ordered disjoint-minor sampling, nonsymmetric interpolation support, global `rank R<=3r`, restricted `rank R[L,L]<=r`, zero diagonal `E`, and zero seed diagonal `D` are correct. |
| 632–724 | PASS | The `4k-3` spectral-to-volume conversion, random-cut factor `4^{-k}`, no-pivot analytic consequences, singular kernels, pivot half-potential, and nine-direction half-potential all close with the stated hypotheses. |
| 726–790 | PASS | Main theorem case split and general `K,s` scaling are correct. The source properly declines to claim the three-eigenvalue theorem or global continuity. |

No mathematical source range remains `UNCHECKED` in this run.

### 1.1 The disputed singular Schur limit is valid as written

Let `S_epsilon` be the Schur complement associated with `A+epsilon I`. The manuscript establishes

\[
N_{S_\varepsilon}(t-|\varepsilon|)\ge N_A(t)-k.
\]

Put `m=N_A(t)-k`. If `m<=0` there is nothing to prove. Otherwise the preceding inequality is exactly

\[
s_m(S_\varepsilon)\ge t-|\varepsilon|,
\]

where `s_m` is the `m`-th ordered absolute eigenvalue (singular value, because `S_epsilon` is symmetric). Since `S_epsilon -> S` in operator norm, singular-value continuity gives

\[
s_m(S)=\lim_{\varepsilon\to0}s_m(S_\varepsilon)\ge t.
\]

Therefore `N_S(t)>=m`. The fact that the threshold moves is harmless because both sides converge through a **closed** inequality. No count-continuity assertion at a discontinuity is required. A fixed-`delta` proof is also valid, but it is a clarification rather than a necessary repair.

This agrees with the dedicated fleet02/B11 Schur audit, which explicitly checked equality-at-threshold cases and found the manuscript argument valid.

## 2. Independent reconstruction of the nine-direction compiler

The candidate source is fleet03/B04 at `8ff490c177d0cd7d6f33130f1431785e312a9d10`. I did not use its PASS label as a premise; I rechecked the compiler algebra.

Let `H,I,J` be disjoint original-coordinate banks. A `k`-dimensional projection `W` of `X_H` has density cap `M_H`. For

\[
Q=F(X_H)+2\langle W,MX'+\beta\rangle+R(X'),\qquad X'=(X_I,X_J),
\]

assume the `J` restriction `M_J` has row rank `k`, singular-value product `S`, and residual projected cross rows `C`. For an `ell`-subset Gram-volume law

\[
w_T=\det(C_TC_T^T)/Z_\ell,
\qquad \alpha_i=P(i\in T),
\]

with every `alpha_i<=1/2`, set `d=k+ell`.

Push `e^{itF}dP_H` to `W`. Its complex density `a_t` obeys `|a_t|<=p_W`, hence `||a_t||_2^2<=M_H`. `k`-dimensional Plancherel at scale `2t` gives

\[
\int|\widehat a_t(2t(l+\beta))|^2dl\le M_H(\pi/|t|)^k.
\]

For the light bank, condition first on the entire original `I` bank. Expanding the squared `L^2` norm requires only an independent copy of the `J` bank; pure `I` terms cancel, pure `J` phases have modulus one, and `D=X_J-X'_J` retains independent cap-one coordinates. Thus the remaining integral has the product-safe form

\[
E_D\left[\kappa(M_JD)\prod_i|\psi_i(2t\langle a_i,D\rangle)|\right].
\]

Write `a_i=c_i+lambda_i M_J` with `c_i` perpendicular to the row space of `M_J`. For each `ell`-subset `T`, the map

\[
D\mapsto (M_JD,(\langle c_i,D\rangle)_{i\in T})
\]

has Gram determinant `S^2 det(C_TC_T^T)`. The manuscript product-projection lemma gives density cap

\[
e^{d/2}/[S\sqrt{\det(C_TC_T^T)}].
\]

Weighted Hölder produces Fourier powers `1/alpha_i>=2`; the manuscript scalar Fourier-power lemma at scale `2t` gives

\[
\int |\psi_i(2t(y+u))|^{1/\alpha_i}dy
\le \pi\sqrt{2e\alpha_i}/|t|.
\]

Finally, if the sampled `ell`-set is uniformly ordered, entropy subadditivity gives

\[
H(w)+\sum_i\alpha_i\log\alpha_i
\le \ell\log\ell-\log(\ell!).
\]

These steps reproduce

\[
|\phi_Q(t)|\le
\min\{1,K_{k,\ell}|t|^{-d/2}\},
\]

with the candidate's explicit `K_{k,ell}`. For `d>2`, direct integration plus Fourier inversion gives the claimed bounded-density formula. All conditioning is on original product coordinates; no spectral-coordinate independence is introduced.

### 2.1 Marginal-free order-three receiver

For a literal physical crossing block `M`, let `Z=E_3(M)=e_3(MM^T)`. If all canonical row marginals are at most one half, use `(k,ell)=(0,3)`. If one physical row is heavy, promote that original coordinate and use the exact Gram–Schmidt identity

\[
J_i=\|w\|^2 e_2(CC^T).
\]

If a second residual row is heavy, promote it and obtain

\[
H_{ij}=\det(PP^T)\|C_2\|_F^2>J_i/2.
\]

If a final one-volume row is heavy, three promoted physical rows satisfy

\[
\det(P_3P_3^T)>Z/8.
\]

The four branches are therefore paid by `(0,3)`, `(1,2)`, `(2,1)`, or an exact-rank-three crossing estimate. This reproduces the marginal-free bound

\[
\|p_Q\|_\infty\le
3\sqrt2\,e(9/2)^{1/6}E_3(M)^{-1/6}<15E_3(M)^{-1/6}.
\]

The older completed third-compound receiver in the repository gives the sharper coefficient `6^(4/3)`; either version is enough for the nine-direction theorem.

### 2.2 Marginal-free order-two half potential

The same promotion tree one dimension lower gives

\[
\sup_a E|Q-a|^{-1/2}
\le 8\sqrt e\,2^{-1/8}E_2(M)^{-1/8}<13E_2(M)^{-1/8}.
\]

This is a half-potential theorem, not a rank-two bounded-density theorem.

## 3. Nine large eigenvalues close all cases

Normalize `K=s=1`, with `eta=1/100`, `kappa=1/80^2`.

**No pivot.** The baseline `4k-3` proposition at `k=3` gives `V_3(A)>=kappa^3`. A fair physical cut gives a crossing block with

\[
E_3(M)\ge4^{-3}\kappa^3,
\qquad E_3(M)^{-1/6}\le160.
\]

The self-contained candidate coefficient is `<15`, so this branch is `<2400`; the older completed receiver gives the stronger `<160*6^(4/3)<1920`. It has a `C_0` density.

**Scalar pivot.** The scalar Schur complement keeps at least eight unit spectral directions. If that complement has a pivot, the improved pivot half-potential theorem proved below gives full half potential `<260`. If it has no pivot, then `s_5>=1`; the baseline proposition at `k=2`, followed by a fair cut, gives

\[
E_2\ge4^{-2}\kappa^2,
\qquad E_2^{-1/8}=\sqrt{160}.
\]

The order-two receiver gives less than

\[
13\sqrt{160}<13^2=169<260.
\]

Thus in either subcase the Schur remainder has full half potential `<260`, and the scalar square profile gives

\[
\|p_Q\|_\infty<10\cdot260=2600.
\]

**Definite pair.** Direct conditional density is `<10pi<40`.

**Indefinite pair.** The order-two Schur count leaves at least seven unit spectral directions, hence one; the manuscript hyperbolic/log-potential density argument applies and is `<251` already.

Therefore the normalized nine-direction theorem has constant `<2600`. Scaling `Y=KX` and `Q=(s/K^2)Qtilde` yields `<2600 K^2/s`.

## 4. New exact constant sharpening: pivot half potential `<260`

### 4.1 Exact singular-kernel improvement

For

\[
J(d)=\int_{-1}^1|x|^{-1/2}|x-d|^{-1/2}dx,
\]

symmetry gives `J(-d)=J(d)`. For `0<d<=1`, direct substitutions give

\[
J(d)=2\operatorname{arsinh}(d^{-1/2})+\pi+2\operatorname{arcosh}(d^{-1/2}).
\]

Set `r=d^{-1/2}>=1`. Then

\[
\operatorname{arsinh}r+\operatorname{arcosh}r-2\log r
=\log\!\left[(1+\sqrt{1+r^{-2}})(1+\sqrt{1-r^{-2}})\right]
\le\log4,
\]

because `sqrt(1+a)+sqrt(1-a)<=2` and `sqrt(1-a^2)<=1`. Therefore

\[
J(d)\le \pi+4\log2+2\log(1/d)<6+2\log(1/d).
\]

The last strict inequality follows from `pi<22/7` and `log2<5/7`.

For `d>=1`,

\[
J(d)=2\operatorname{arsinh}(d^{-1/2})+2\arcsin(d^{-1/2})
\le2\operatorname{arsinh}1+\pi<6.
\]

Hence, for all `d!=0`,

\[
\boxed{\ J(d)<6+2\log_+(1/|d|).\ }
\]

### 4.2 Rational quarter-power certificate reused and rechecked

The exact coefficient in the manuscript's quarter-power concentration lemma is

\[
C_q=2^{5/8}\pi^{-1/4}e^{3/8}\Gamma(3/8).
\]

The preceding fleet03/B10 run proved, and this run rechecked, the fully rational envelope

\[
C_q<35/8.
\]

For completeness the ingredients are:

- `2^(5/8)<31/20` because `31^8-32*20^8=33,691,037,441>0`;
- `pi^(-1/4)<19/25` from `pi>3` and `3*19^4-25^4=338>0`;
- `e^(3/8)<22/15`, using `e<87/32<11/4` and `64*22^8-1331*15^8=100,848,484,429>0`;
- `Gamma(3/8)<12665/5016<81/32`, obtained from `e^{-x}<=1-x+x^2/2` on `[0,1]`, `x^{-5/8}<=1` on `[1,infinity)`, and `e^{-1}<3/8`.

Their product is

\[
(31/20)(19/25)(22/15)(81/32)=174933/40000<35/8.
\]

Moreover

\[
\log(35/8)<119/80,
\]

because the positive exponential series through order five at `119/80` exceeds `35/8` by the exact rational amount

\[
12608176999/393216000000>0.
\]

Thus for any quadratic remainder with operator norm at least one,

\[
\sup_a E\log_+\frac1{|R-a|}
\le4+4\log(35/8)<199/20.
\]

At a scalar pivot, the new kernel bound therefore gives the truncated half potential

\[
H(Q)<10\left(6+2\cdot\frac{199}{20}\right)=259.
\]

### 4.3 New optimized hyperbolic-pair tail split

In one hyperbola branch write

\[
w(t)=u e^t+v e^{-t},\qquad |u|=|v|=\rho_0.
\]

Choose an original coordinate `i` with `|u_i|>=rho_0/sqrt2`. Instead of forcing the backward exponential to be at most one half of the forward term, fix

\[
q=2/9.
\]

For

\[
T_1=\frac12\log(\sqrt2/q)=\log3-\frac14\log2,
\]

all `t>=T_1` satisfy `|v_i|e^{-t}<=q|u_i|e^t`. Hence

\[
|w_i(t)|\ge(1-q)|u_i|e^t,
\qquad
|w_i'(t)|\ge\frac{1-q}{1+q}|w_i(t)|,
\]

so the tail change of variables costs only

\[
\frac{1+q}{1-q}=\frac{11}{7}.
\]

Take

\[
T=\max\left(T_1,\log\frac1{(1-q)|u_i|}\right).
\]

Since `|u_i|>=sqrt(delta Lambda)/(2sqrt2)`, the exact max identity gives

\[
T\le T_1+\frac12\log_+\frac{72\sqrt2/49}{\delta\Lambda}.
\]

The positive tail is at most `(11/7)log2`; the negative tail is identical after choosing a large coordinate of `v`. Therefore each hyperbola branch is bounded by

\[
C_0+\log_+\frac{72\sqrt2/49}{|\delta|\Lambda},
\]

where

\[
C_0=2\log3+\frac{37}{14}\log2.
\]

Using `Lambda>=2/sqrt D`, the conditional density improves to

\[
p(z)\le D^{-1/2}\left(C_0+\log_+\frac{(36\sqrt2/49)\sqrt D}{|z-v|}\right).
\]

The manuscript logarithmic-kernel integral then gives

\[
H_{\rm ind}(D)
\le D^{-1/2}\left(4C_0+8+4\log_+((36\sqrt2/49)\sqrt D)\right).
\]

For `D>=eta=1/100` this expression is decreasing in `sqrt D`: below the activation point it is a constant divided by `sqrt D`; above it the derivative numerator is `4-(8+4C_0)-4log(...)<0`. Also `(36sqrt2/49)/10<1`. Therefore the maximum is at `D=1/100`, where

\[
H_{\rm ind}<10(8+4C_0).
\]

Elementary exponential-series bounds give `log2<7/10` and `log3<11/10`:

\[
e^{7/10}>1+7/10+(7/10)^2/2+(7/10)^3/6=12013/6000>2,
\]

and the order-five Taylor lower sum for `e^{11/10}` is `36015101/12000000>3`. Hence `C_0<81/20` and

\[
\boxed{\ H_{\rm ind}<242.\ }
\]

The definite-pair branch stays `<160`. Consequently every pivot under the manuscript's two-direction hypothesis has

\[
H(Q)<259,
\qquad
\sup_aE|Q-a|^{-1/2}<260.
\]

This is the only new constant input needed for the `<2600` nine-direction theorem.

## 5. Adversarial endpoint checks

### 5.1 `L^2` density does not control the square-root potential

This blocks a tempting but false shortcut from the thirteen-direction `L^2` theorem to a bounded-density scalar-pivot theorem. For integer `N>=4`, define

\[
q_N(x)=N^{-1/2}x^{-1/2}\mathbf1_{[e^{-N},1]}(x),
\qquad
m_N=\int q_N=\frac{2(1-e^{-N/2})}{\sqrt N}\le1,
\]

and let

\[
p_N(x)=q_N(x)+(1-m_N)\mathbf1_{[2,3]}(x).
\]

Then `p_N` is a probability density, the two pieces have disjoint supports, and

\[
\|p_N\|_2^2=1+(1-m_N)^2\le2,
\]

while

\[
\int |x|^{-1/2}p_N(x)dx\ge
N^{-1/2}\int_{e^{-N}}^1x^{-1}dx=\sqrt N\to\infty.
\]

Thus an `L^2` remainder alone cannot pay a completed physical square at the endpoint.

### 5.2 The raw interpolation rank bounds are genuinely sharp

The preceding B10 audit constructed the no-pivot block

\[
A=(1/20)\begin{pmatrix}0&-1&-1\\-1&0&-1\\-1&-1&0\end{pmatrix}.
\]

For seed `S={1}`, `T={2}`, `L={3}`, the completion has `E=0`, global `rank R=3`, and restricted `rank R[L,L]=1`. Direct sums give exact `3r` and `r` simultaneously. Therefore reducing the multiplicity below nine cannot come merely from lowering those two universal rank constants. Under eight directions, the terminal `r=2` count can force only two large residual diagonal coordinates, exactly matching the restricted rank two. A new overlap-aware receiver or an additional structural consequence is required.

## 6. Status

- Literal seventeen-direction baseline: **PASS** in this run.
- Nine-direction replacement theorem: **PASS** in this run, with two earlier independent full PASS reconstructions already present in the repository.
- New same-threshold constant from this run: **`<2600 K^2/s` under `s_9(A)>=s`**.
- Multiplicity eight: **OPEN**; raw rank bookkeeping and order-two density endpoints do not close it.
- Full three-eigenvalue conjecture: **OPEN**.
- Global continuity: **OPEN**; no-pivot nine-direction branch is `C_0`, pivot branches are only essentially bounded here.
