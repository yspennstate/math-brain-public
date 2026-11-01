# fleet02/B15 auto11 improvement — complete nine-eigenvalue replacement, with B15 regularity scope

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T140615Z-fleet02-B15-fixedmult-auto11`  
Audited baseline: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Baseline blob / SHA-256: `183ccd294763214e6a707e8d4749ff9a8cf7006d` / `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

This file is a complete replacement argument for the **fixed-multiplicity threshold nine**. It preserves arbitrary dimension, signature, remaining spectrum, affine terms, and arbitrary independent rough coordinate densities. It does not solve the unrestricted three-eigenvalue conjecture.

## Theorem

Let `X=(X_1,...,X_n)` have independent real coordinates with densities bounded by `K<infinity`. Let `A=A^T`, `b in R^n`, `c in R`, and suppose

` s_9(A) >= s > 0.`

Then `Q=X^TAX+b^TX+c` has an essentially bounded density. A conservative reconstruction gives

`||p_Q||_infinity <= 6010 K^2/s`.

Retaining sharper constants already implicit in the same analytic steps improves this to

`boxed: ||p_Q||_infinity < 3078 K^2/s.`

Global continuity is not used to obtain either height bound and is not claimed by this proof. The no-pivot Fourier branch does have a `C_0` density because its characteristic function is integrable.

## Closed dependency map

From the audited baseline manuscript this proof uses only:

1. Fourier/Gaussian/Riesz normalization, lines 91–160.
2. Schur spectral count, lines 183–207.
3. Geometric Brascamp–Lieb, product projections, and scalar Fourier powers, lines 221–301.
4. Scalar-square, definite-pair, hyperbolic-pair, and quarter-power/log-potential estimates, lines 404–525.
5. No-pivot interpolation/spectral-to-volume theorem and fair coordinate cut, lines 528–630, at orders two and three only.

The order-five density endpoint is completely replaced by the grouped receiver below. The new order-two receiver is used only for a half-potential, never as a rank-two density theorem.

---

## 1. Grouped product-Fourier receiver

Let `H,I,J` be disjoint sets of **original coordinates**. Let `W` be a `k`-dimensional linear image of `X_H` having a density cap `M_H`. Write the quadratic polynomial, after collecting same-bank terms, as

`Q = F(X_H) + 2 <W, M_I X_I + M_J X_J + beta>
     + R_I(X_I) + 2 sum_(i in I) X_i <a_i,X_J> + R_J(X_J),`

where `F,R_I,R_J` are arbitrary measurable phases arising from the original quadratic/affine polynomial. Assume `M_J` has row rank `k`. Let

`S = product of the k nonzero singular values of M_J`

(with `S=1` when `k=0`). Let `c_i` be the orthogonal projection of the physical crossing row `a_i` onto `row(M_J)^perp`, and let `C` be the matrix with rows `c_i`.

For `ell>=1`, define

`Z_ell = sum_(|T|=ell) det(C_T C_T^T)`.

Assume `Z_ell>0`, set

`w_T = det(C_T C_T^T)/Z_ell`,
`alpha_i = sum_(T contains i) w_T`,

and suppose every positive `alpha_i<=1/2`. Put `d=k+ell`.

### Claim 1.1 — characteristic-function envelope

For every `t!=0`,

`|phi_Q(t)| <= min(1,K_(k,ell)|t|^(-d/2))`,

where

`K_(k,ell)
 = M_H^(1/2) pi^(d/2) 2^(ell/4) e^((k+2ell)/4)
   (ell^ell/ell!)^(1/4) S^(-1/2) Z_ell^(-1/4).`

### Proof: hub `L^2` step

Push the complex measure `exp(itF)dP_H` under `W`. It has a density `a_t` with

`|a_t(w)|<=p_W(w)`, hence `||a_t||_2^2<=M_H`.

Push `exp(itR)dP_(I,J)` under the `k`-dimensional linear map

`L=M_I X_I+M_JX_J`

to a complex density `mu_t`. Absolute continuity follows because `M_J` has full row rank and the `J` coordinates have a product density; equivalently one may insert a compact approximate identity and pass by lower semicontinuity.

Then, up to a harmless sign convention,

`phi_Q(t)=int hat(a_t)(2t(l+beta)) mu_t(l) dl`.

Cauchy–Schwarz and Plancherel at scale `2t` give

`|phi_Q(t)|^2
 <= [int |hat(a_t)(2t(l+beta))|^2 dl] ||mu_t||_2^2
 <= M_H (pi/|t|)^k ||mu_t||_2^2.`

No independence is asserted in the projected `W` or `L` variables.

### Proof: light-bank `L^2` step

Condition on the literal coordinates `X_I=x`. Translation of the projected output by `M_Ix` preserves `L^2`, and Jensen in the Hilbert space `L^2` gives

`||mu_t||_2^2 <= E_(X_I) ||mu_(t,x)||_2^2`,

where `mu_(t,x)` is the complex pushforward of the `J`-law under `M_JX_J`.

To justify expansion for rough laws, convolve this pushforward with a probability approximate identity. Expanding its squared norm uses an independent copy only of `X_J`. Put `D=X_J-X'_J`; its coordinates are independent and each difference density is bounded by one. The pure `I` phase cancels, the pure `J` phase has modulus one, and integration over the original independent `X_i`, `i in I`, produces

`prod_i |psi_i(2t<a_i,D>)|`,

where `psi_i` is the characteristic function of `X_i`. The regularizer appears only as a probability kernel in `M_JD`; all estimates below are uniform in it, so lower semicontinuity removes it at the end.

### Proof: determinant-weighted subsets

Write

`a_i=c_i+lambda_i M_J`, `c_i perpendicular row(M_J)`.

For every positive-weight `ell`-set `T`, the linear map

`D -> (M_JD,(<c_i,D>)_(i in T))`

has full row rank `d` and Gram determinant

`S^2 det(C_T C_T^T)`.

Indeed the `c_i` block is orthogonal to the rows of `M_J`. Applying the baseline product-projection lemma to a general full-row-rank map (normalize its row Gram matrix first) gives density cap

`e^(d/2) / [S sqrt(det(C_T C_T^T))]`.

Let `h_i(D)=|psi_i(2t<a_i,D>)|`. Because

`prod_i h_i = prod_T [prod_(i in T) h_i^(1/alpha_i)]^(w_T),`

weighted Holder applies. For fixed `T`, after conditioning on the `M_JD` coordinate, translations by `lambda_i M_JD` do not affect the one-dimensional integral, and `1/alpha_i>=2`. The baseline scalar Fourier-power lemma therefore gives exactly

`int_R |psi_i(2t(y+u))|^(1/alpha_i) dy
 <= pi sqrt(2e alpha_i)/|t|.`

Thus the `T`-term is bounded by

`[e^(d/2)/(S sqrt(det(C_T C_T^T)))]
 * [pi^ell (2e)^(ell/2) |t|^-ell]
 * prod_(i in T) alpha_i^(1/2).`

Take the `w_T`-geometric mean. Since

`det(C_T C_T^T)=w_T Z_ell`,

the determinant factor becomes

`Z_ell^(-1/2) exp(H(w)/2)`.

The `alpha` factors become

`exp[(1/2) sum_i alpha_i log alpha_i]`.

To bound their product, choose `T` with law `w` and then order its `ell` elements uniformly. The ordered tuple has entropy `H(w)+log(ell!)`. Each position has marginal probability `alpha_i/ell`; entropy subadditivity therefore gives

`H(w)+log(ell!)
 <= ell log ell - sum_i alpha_i log alpha_i`,

or

`H(w)+sum_i alpha_i log alpha_i
 <= ell log ell-log(ell!).`

Consequently

`||mu_t||_2^2
 <= e^(d/2) S^-1 Z_ell^-1/2
    pi^ell (2e)^(ell/2)
    (ell^ell/ell!)^(1/2) |t|^-ell.`

Insert this into the hub estimate and take a square root. This is Claim 1.1.

### Claim 1.2 — density endpoint for `d>2`

If `d>2`, direct integration of

`min(1,K|t|^(-d/2))`

at the transition `t_0=K^(2/d)` gives

`int_R min(1,K|t|^(-d/2)) dt
 = 2d/(d-2) K^(2/d).`

Fourier inversion therefore yields

`||p_Q||_infinity
 <= [d/(d-2)] M_H^(1/d) 2^(ell/(2d)) e^((k+2ell)/(2d))
    (ell^ell/ell!)^(1/(2d)) S^(-1/d) Z_ell^(-1/(2d)).`

Because the envelope is integrable, this receiver actually gives a `C_0` density for the rough law itself.

### Claim 1.3 — half-potential endpoint for `d=2`

When `d=2`, the envelope is `min(1,K/|t|)`. The audited Riesz inequality gives

`sup_a E|Q-a|^-1/2
 <= (2pi)^-1/2 * [2 int_0^K t^-1/2 dt + 2K int_K^infinity t^-3/2 dt]
 = (8/sqrt(2pi)) sqrt(K).`

Substituting `K_(k,ell)` gives

`4 sqrt(2) M_H^(1/4) 2^(ell/8) e^((k+2ell)/8)
 (ell^ell/ell!)^(1/8) S^-1/4 Z_ell^-1/8.`

This is a half-potential statement only.

---

## 2. Terminal exact-rank receivers

If `r` literal physical coordinates cross an independent product bank through an `r x |J|` matrix `P` of row rank `r`, absorb all same-bank quadratic/affine terms into complex pushforwards. The same `L^2`/Plancherel argument, with no residual `I` packet, gives

`|phi_Q(t)|
 <= min(1, pi^(r/2)e^(r/4)[det(PP^T)]^-1/4 |t|^-r/2).`

Therefore:

- `r=3`: `||p_Q||_infinity <= 3 sqrt(e) [det(PP^T)]^-1/6`;
- `r=2`: `sup_a E|Q-a|^-1/2 <= 4 sqrt(2)e^(1/4)[det(PP^T)]^-1/8`.

Again, there is no post-rotation independence claim.

---

## 3. Marginal-free `E_3` density receiver

For a literal original-coordinate crossing matrix `M` with rows `m_i`, write

`E_3(M)=sum_(i<j<l) det Gram(m_i,m_j,m_l)=:Z>0.`

Let `J_i` be the incident third-volume mass, so `sum_i J_i=3Z`.

### Case 3a: no heavy row

If every `J_i/Z<=1/2`, Claim 1.2 applies with `(k,ell,d)=(0,3,3)`. It gives

`||p_Q||_infinity
 <= C_03 Z^-1/6`,

where

`C_03 = 3 sqrt(2) e (9/2)^(1/6)
      = 14.818337662843...`.

### Case 3b: one heavy row

If `J_i>Z/2`, put `w=m_i` and project every other row orthogonally off `w`, obtaining rows `c_j`. Gram–Schmidt gives the exact identity

`J_i = ||w||^2 E_2(C).`

If every residual incident `E_2` marginal is at most half its packet, Claim 1.2 with `(k,ell)=(1,2)` applies. Its packet is

`S^2 Z_2 = ||w||^2 E_2(C)=J_i>Z/2`.

After the factor `2^(1/6)` for `J_i>Z/2`, its constant is

`3 sqrt(2)e^(5/6)2^(1/6)=10.958...<C_03`.

### Case 3c: two promoted rows

If a residual row `c_j` is heavy for `E_2(C)`, project the remaining rows further off `span(w,m_j)` to rows `d_l`. With `P` the two promoted physical rows,

`H_ij := det(PP^T) sum_l ||d_l||^2 > J_i/2 > Z/4.`

This is again exact Gram–Schmidt: the incident residual two-volume equals `||c_j||^2 sum_l||d_l||^2`, and `det(PP^T)=||w||^2||c_j||^2`.

If the residual one-volume packet is light, Claim 1.2 with `(k,ell)=(2,1)` gives, after the factor `4^(1/6)`, constant `8.264...<C_03`.

### Case 3d: exact three-row terminal

If some residual row is heavy for the one-volume packet, promoting it gives a literal three-row Gram determinant

`G > H_ij/2 > Z/8.`

The exact-rank-three receiver gives

`3 sqrt(e) G^-1/6
 < 3 sqrt(e) 8^(1/6) Z^-1/6
 =6.995... Z^-1/6<C_03 Z^-1/6.`

The four cases are exhaustive. Hence

`boxed: ||p_Q||_infinity <= C_3 E_3(M)^(-1/6),`

with

`C_3=3 sqrt(2)e(9/2)^(1/6)=14.818337662843...`.

---

## 4. Marginal-free `E_2` half-potential receiver

Repeat the same promotion argument one dimension lower. Put

`E_2(M)=Z>0`, `J_i=incident pair-volume`, `sum_iJ_i=2Z`.

- If every `J_i/Z<=1/2`, Claim 1.3 with `(k,ell)=(0,2)` gives

  `C_02 Z^-1/8`, `C_02=8 sqrt(e)2^-1/8=12.095072570796...`.

- If `J_i>Z/2`, promote row `i`; exact Gram–Schmidt gives `J_i=||w||^2E_1(C)`. If the residual one-volume packet is light, `(k,ell)=(1,1)` plus the `2^(1/8)` heavy factor gives `9.788... Z^-1/8<C_02 Z^-1/8`.

- If a residual row is heavy, promoting it yields a literal two-row Gram determinant `G>Z/4`. The exact-rank-two half-potential receiver gives `8.638... Z^-1/8<C_02 Z^-1/8`.

Therefore

`boxed: sup_a E|Q-a|^-1/2 <= C_2 E_2(M)^(-1/8),`

`C_2=8 sqrt(e)2^-1/8=12.095072570796...`.

This receiver is deliberately **not** a bounded-density theorem.

---

## 5. Assemble the nine-eigenvalue theorem: conservative constant `6010`

Normalize `K=s=1` and keep the baseline parameters

`eta=1/100`, `kappa=1/80^2`.

### 5a. No pivot

If `A` has no `eta`-pivot and `s_9(A)>=1`, the audited baseline spectral-to-volume theorem at order three gives

`V_3(A)>=kappa^3`.

A fair original-coordinate cut gives a literal crossing block `M` with

`E_3(M)>=4^-3 kappa^3`,

so

`E_3(M)^(-1/6)<=2 kappa^-1/2=160`.

The new `E_3` receiver gives

`||p_Q||_infinity <=160 C_3=2370.934026...<2400`.

This branch has a continuous `C_0` density because the receiver supplies an integrable characteristic-function majorant directly for the rough law.

### 5b. Scalar pivot

Suppose `|A_hh|>=eta`. Complete the square in the literal original coordinate `X_h`. The Schur complement `S` retains at least eight unit-scale eigenvalue magnitudes.

If `S` has an `eta`-pivot, the audited baseline pivot theorem needs only two unit-scale directions and gives truncated half-potential `H(R)<=600`. Outside `|R-a|<=1`, the kernel is at most one, so

`sup_a E|R-a|^-1/2 <=601`.

If `S` has no pivot, then in particular `s_5(S)>=1`. The baseline order-two spectral-to-volume theorem and a fair cut give

`E_2(M_S)>=4^-2 kappa^2`,

hence

`E_2(M_S)^(-1/8)<=sqrt(160)`.

The new order-two receiver gives

`sup_a E|R-a|^-1/2
 <= C_2 sqrt(160)
 =152.991911...<153`.

Thus the full Schur half-potential is at most `601` in every scalar-pivot subcase. The conditional square profile costs `eta^-1/2=10`, so

`||p_Q||_infinity<=6010`.

### 5c. Definite pair

A definite principal pair with determinant magnitude at least `eta` has conditional density at most

`pi/sqrt(eta)=10pi<32`.

### 5d. Indefinite pair

An indefinite principal pair removes two coordinates, so its Schur complement retains at least seven unit-scale eigenvalue magnitudes and in particular operator norm at least one. The audited hyperbolic envelope plus the one-direction logarithmic-potential bound gives the baseline `<251` estimate.

The maximum of the four branches is `6010`.

### 5e. Scaling

For general `K,s`, let `Y=KX`; its coordinate densities are bounded by one. Define

`Q_tilde=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c`.

Then `s_9(A/s)>=1` and

`Q=(s/K^2)Q_tilde`.

Density scaling gives

`||p_Q||_infinity<=6010 K^2/s`.

This completes a replacement proof at multiplicity nine without weakening any hypothesis.

---

## 6. Sharpening the same proof to `<3078 K^2/s`

The multiplicity reduction does not need sharper pivot constants, but they are available inside the same analytic mechanism. I independently reconstructed them here.

### 6a. Sharper singular kernel

For

`J(d)=int_-1^1 |x|^-1/2 |x-d|^-1/2 dx`,

symmetry reduces to `d>0`. Direct substitutions give, for `0<d<=1`,

`J(d)=2 asinh(d^-1/2)+pi+2 acosh(d^-1/2)`,

and for `d>=1`,

`J(d)=2 asinh(d^-1/2)+2 asin(d^-1/2)`.

For `z>=1`,

`asinh z+acosh z <=2 log(2z)`;

after exponentiating this reduces to

`(1+sqrt(1+u))(1+sqrt(1-u))<=4`, `u=z^-2`,

which follows from `sqrt(1+u)+sqrt(1-u)<=2` and `sqrt(1-u^2)<=1`. Hence

`boxed: J(d)<7+2 log_+(1/|d|).`

### 6b. Quarter-power coefficient `16 -> 9/2`

The exact off-diagonal Gaussian-smoothing coefficient before the manuscript rounds it is

`C_q=2^(5/8) pi^-1/4 e^(3/8) Gamma(3/8)`.

On `[0,1]`, the even fourth Taylor truncation is an upper bound for `e^-x`; on `[1,infinity)`, `x^-5/8<=1`. Thus

`Gamma(3/8)
 < 8/3-8/11+4/19-4/81+1/105+e^-1
 < 5/2`.

Also `2^(5/8)<31/20`, `pi^-1/4<19/25`, `e^(3/8)<3/2`, whence

`C_q < (31/20)(19/25)(3/2)(5/2)=1767/400<9/2`.

The direct diagonal branch has coefficient `4`, so globally

`P{|R-a|<rho}
 <= min(1,(9/2)(rho/L)^(1/4))`.

For `L>=1`, layer cake gives

`L_0^*:=sup_a E log_+(1/|R-a|)
 <=4+4 log(9/2)`.

### 6c. Sharper hyperbolic constant

The exact branch estimate in the audited hyperbolic proof, before rounding `15 log2/2` up to `6`, is

`p_q(z)
 <=D^-1/2[(15/2)log2+log_+(16sqrt(D)/|z-v|)].`

### 6d. Sharper pivot half-potential

With `eta=1/100`:

- scalar pivot:

  `H(Q)<=10[7+2L_0^*]=10[15+8log(9/2)]=270.327...`;

- definite pair: `H(Q)<=40pi=125.664...`;

- indefinite pair:

  `H(Q)<=D^-1/2[8+30log2+4log(16sqrt D)]`, `D>=1/100`.

  With `y=sqrt D>=1/10`, the bracket divided by `y` is decreasing because its derivative numerator is `4-[8+30log2+4log(16y)]<0`. The maximum is therefore

  `10[8+30log2+4log(8/5)]
   =306.744299...<306.75`.

For a rational certification of the last decimal comparison, `log2<13863/20000` and `log(8/5)<117501/250000`; the seventh positive Taylor partial sums of the exponentials already exceed `2` and `8/5`, respectively. These bounds give `<306.75` directly.

Thus every pivot under two surviving unit directions has

`H(Q)<306.75`.

### 6e. Nine-direction branches with sharpened constants

- no pivot: unchanged `<2371`;
- scalar pivot: if Schur has a pivot, full half-potential `<307.75`; if not, the `E_2` receiver gives `<153`. Therefore outer square profile gives `<3077.5`;
- definite pair: `<32`;
- indefinite pair: using the sharpened hyperbolic constant and `L_0^*`, the worst at `D=1/100` is `<157`.

Hence

`boxed: ||p_Q||_infinity <3078 K^2/s whenever s_9(A)>=s>0.`

---

## 7. B15 regularity scope and rough approximation

The proof above pays **height first**.

- In the no-pivot `E_3` branch, the actual rough-law characteristic function has an integrable `|t|^-3/2` envelope. Fourier inversion therefore gives a bounded continuous `C_0` density directly.
- In scalar/definite/indefinite pivot branches, the proof is conditional measure domination plus Tonelli. It gives an essential density cap. No continuity conclusion is needed or used.

If one mollifies the original coordinate densities, product `L^1` convergence implies total-variation convergence of the joint laws, and deterministic quadratic pushforward contracts total variation. A uniform interval bound therefore passes to the rough law with no loss. But this does not pass continuity: smooth cap-one densities can converge in `L^1` to `1_[0,1]`, whose density is discontinuous. Thus a separate common Fourier envelope or other regularity theorem is required before claiming continuity in a pivot branch.

---

## 8. Why this proof stops at nine

The present interpolation mechanism itself saturates at eight in the order-three no-pivot endpoint. For the worst bad-ratio seed `r=2`, the completion has

`rank R<=3r=6`, `rank R[L,L]<=r=2`.

Under only `s_8>=1`, global rank subtraction forces only `8-6=2` large diagonal residual coordinates. A `2 x 2` diagonally dominant block can have rank exactly two, so there is no contradiction with the restricted rank bound. Under `s_9`, three such coordinates are forced and the contradiction closes. Constants cannot repair this count.

Nor can one replace the missing order-three density endpoint by an order-two density theorem. Let `U,V` be independent uniform variables on `[-1,1]`, each with density `1/2<=1`. Then `U^2` has density `1/(2sqrt s)` on `(0,1)`, and for `R=U^2-V^2`,

`p_R(0)=int_0^1 [1/(2sqrt s)]^2 ds=infinity`.

Thus an indefinite rank-two quadratic can have a genuine logarithmic density singularity. The new `E_2` receiver is correctly used only for a half-potential. A threshold-eight proof needs additional overlap/cycle/multi-bank product structure, not merely an `E_2` lower bound or absolute Fourier inversion.

## Status

- Pinned 17-eigenvalue baseline: **PASS** in the sibling audit, with the local undefined-notation repair `A/B -> S`.
- Complete fixed-multiplicity reduction proved here: **nine eigenvalues**, constant `<3078 K^2/s`.
- Threshold eight: **OPEN in this argument**.
- Unrestricted three-eigenvalue conjecture: **OPEN**.
- Global continuity for every nine-eigenvalue pivot branch: **not claimed by this proof**.
