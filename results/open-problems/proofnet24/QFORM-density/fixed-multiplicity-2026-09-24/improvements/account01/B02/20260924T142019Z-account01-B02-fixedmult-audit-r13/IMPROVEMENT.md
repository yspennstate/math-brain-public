# account01/B02 r13 — complete threshold-nine theorem with constant 4880

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T142019Z-account01-B02-fixedmult-audit-r13`  
Baseline source: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, `manuscript.tex` blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

This file gives a complete replacement argument lowering the fixed multiplicity from 17 to **9**, while preserving every hypothesis, and sharpens the height constant to **4880**. It uses only baseline lemmas independently audited in the sibling B02 audit plus the new lemmas proved here.

## Theorem B02-9

Let `X=(X_1,...,X_n)` have independent real coordinates with probability densities `f_i` satisfying `0<=f_i<=K` almost everywhere, `0<K<infinity`. Let `A=A^T` be any real symmetric matrix, `b` any real vector and `c` any real scalar. If

` s_9(A) >= s > 0,`

then

`Q=X^TAX+b^TX+c`

has a Lebesgue density satisfying

`boxed: ||p_Q||_infinity <= 4880 K^2/s.`

The theorem is uniform in dimension, signature, all remaining eigenvalues, affine terms and coordinate laws. No continuity conclusion is claimed globally. The no-pivot branch below has a continuous `C_0` density; the pivot branches are proved by measure domination and only essential boundedness is asserted.

We first prove the normalized case `K=s=1`, retaining the baseline constants

`eta=1/100`, `kappa=1/80^2`.

## 1. Grouped product-Fourier compiler

The key replacement for the baseline order-five endpoint is an order-three receiver that aggregates physical crossing volume before paying any reciprocal local minor.

Let `H,I,J` be disjoint sets of original coordinates. Let `X_H` be independent of `X'=(X_I,X_J)`. Let `W` be a `k`-dimensional linear image of `X_H` whose density is bounded by `M_H`. Consider

`Q=F(X_H)+2 <W, M X'+beta>+R(X')`,                                      (1.1)

where `F` is arbitrary measurable, `R` is an arbitrary real quadratic polynomial, and the restriction `M_J` has row rank `k`. Let `S>0` be the product of the nonzero singular values of `M_J` (for `k=0`, set `S=1`). Write the rows of the cross block of `R` from `I` to `J` as `a_i`, and decompose

`a_i=c_i+lambda_i M_J`,

where `c_i` is orthogonal to the row space of `M_J`. Let `C` be the matrix with rows `c_i`.

For an integer `ell>=1`, set

`Z_ell = sum_{|T|=ell} det(C_T C_T^T)>0`,

where the sum is over physical row subsets. Put

`w_T=det(C_T C_T^T)/Z_ell`,  `alpha_i=sum_{T containing i} w_T`.

Assume every nonzero marginal satisfies `alpha_i<=1/2`; rows with `alpha_i=0` can be discarded because their Fourier factors have modulus at most one. Put `d=k+ell`.

### Lemma 1 — grouped Fourier estimate

For `t!=0`,

`|phi_Q(t)| <= min(1,K_{k,ell}|t|^(-d/2))`,                    (1.2)

where

`K_{k,ell}=M_H^(1/2) pi^(d/2) 2^(ell/4) e^((k+2ell)/4)
            (ell^ell/ell!)^(1/4) S^(-1/2) Z_ell^(-1/4).`        (1.3)

If `d>2`, Fourier inversion gives

`||p_Q||_infinity <= [d/(d-2)] M_H^(1/d) 2^(ell/(2d))
 e^((k+2ell)/(2d)) (ell^ell/ell!)^(1/(2d))
 S^(-1/d) Z_ell^(-1/(2d)).`                                    (1.4)

#### Proof

Push the complex measure `exp(itF)dP_H` through `W`. It has a complex density `a_t` satisfying pointwise `|a_t|<=p_W`, whence

`||a_t||_2^2 <= ||p_W||_infinity ||p_W||_1 <= M_H.`             (1.5)

Push `exp(itR)dP_{X'}` through the `k`-dimensional variable `MX'`; denote the resulting complex density by `mu_t`. From (1.1), Fourier transforming only the `W` variable gives

`phi_Q(t)=int hat a_t(2t(l+beta)) mu_t(l) dl`.

Cauchy-Schwarz and baseline Plancherel therefore give

`|phi_Q(t)|^2 <= M_H (pi/|t|)^k ||mu_t||_2^2.`                  (1.6)

It remains to bound the light-bank `L^2` norm without rotating random coordinates. Condition on the original variables `X_I`. Translation of the output by the `M_I X_I` part does not change an `L^2` norm. Mollify the conditional phase-weighted pushforward of `X_J` by a compact approximate identity and expand its squared `L^2` norm with an independent copy `X'_J`. Let

`D=X_J-X'_J`.

The coordinates of `D` are independent and each has density at most one, by the baseline convolution lemma. The pure `I` phase cancels between the two copies; the pure `J` phase has modulus one after absolute values. The `I-J` cross phase is linear in each original `X_i`, so integrating the independent `X_i`, `i in I`, produces the factors

`prod_i |psi_i(2t <a_i,D>)|`,

where every `psi_i` is the characteristic function of a cap-one one-dimensional law. The mollifier square supplies a nonnegative probability-density kernel `rho_delta(M_JD)`. Thus, before the limit,

`||mu_t||_2^2 <= int rho_delta(M_JD)
                      prod_i |psi_i(2t<a_i,D>)| dP_D.`           (1.7)

The bound obtained below is uniform in `delta`; weak `L^2` compactness/lower semicontinuity passes it to the unmollified pushforward. When `k=0` the kernel is absent and the same argument is simply the direct light-bank square.

Apply weighted Holder to (1.7), with weights `w_T`. Because

`sum_{T containing i} w_T/alpha_i=1`,

the product is the weighted geometric mean of integrals in which the factor for `i in T` is raised to power `1/alpha_i`.

For a fixed `T`, use the linear map

`D -> (M_JD,(<c_i,D>)_{i in T}).`

Its row Gram determinant is exactly

`S^2 det(C_T C_T^T)`.                                           (1.8)

Indeed the `c_i` lie orthogonally to the row space of `M_J`. For a general full-row-rank linear map `L`, write `L=(LL^T)^(1/2)U^T` with `U^TU=I`; the baseline product-projection lemma and a deterministic change of variables show that `LD` has density bounded by

`e^(d/2)/sqrt(det(LL^T)).`

Therefore the joint variable in (1.8) has density cap

`e^(d/2)/(S sqrt(det(C_T C_T^T))).`                              (1.9)

For `alpha_i<=1/2`, the baseline integrated scalar Fourier-power estimate at `p=1/alpha_i>=2`, including the scale `2t`, gives uniformly in the shift `u`,

`int_R |psi_i(2t(y+u))|^(1/alpha_i) dy
 <= pi sqrt(2e alpha_i)/|t|.`                                   (1.10)

Integrating first in the `ell` residual coordinates and then in the kernel coordinate gives for the `T`-term

`e^(d/2) [pi sqrt(2e)/|t|]^ell
 prod_{i in T} sqrt(alpha_i)
 /[S sqrt(det(C_T C_T^T))].`                                    (1.11)

Now take the weighted geometric mean. Since

`det(C_T C_T^T)=Z_ell w_T`,

the determinant factors contribute

`Z_ell^(-1/2) exp(H(w)/2)`,

while the marginal factors contribute

`exp[(1/2)sum_i alpha_i log alpha_i]`.

To bound their product, sample `T` with law `w` and then order its `ell` elements uniformly. The ordered tuple has entropy `H(w)+log(ell!)`. Each position has law `alpha_i/ell`. Entropy subadditivity gives

`H(w)+log(ell!) <= ell[-sum_i (alpha_i/ell)log(alpha_i/ell)]
                 = -sum_i alpha_i log alpha_i + ell log ell`.

Hence

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!).`       (1.12)

Combining (1.11)-(1.12),

`||mu_t||_2^2 <= e^(d/2)[pi sqrt(2e)/|t|]^ell
 S^-1 Z_ell^-1/2 (ell^ell/ell!)^1/2.`                           (1.13)

Insert (1.13) into (1.6) and take square roots. The powers combine exactly to (1.3), proving (1.2).

For `d>2`, write `a=K_{k,ell}^{2/d}`. The majorant in (1.2) is `min(1,(a/|t|)^(d/2))`, whose integral is `2ad/(d-2)`. Baseline Fourier inversion contributes `1/(2*pi)`. Since `K_{k,ell}^{2/d}` contains one factor `pi`, that factor cancels and gives exactly (1.4). QED.

### Lemma 2 — terminal exact-rank crossing

Suppose `r` literal original coordinates form one bank and cross an independent product bank through a row-rank `r` block `P`, with arbitrary same-bank quadratic and affine phases retained. Then

`|phi_Q(t)| <= min(1, pi^(r/2)e^(r/4)
 [det(PP^T)]^(-1/4)|t|^(-r/2)).`                                (1.14)

Consequently

`r=3: ||p_Q||_infinity <=3 sqrt(e)[det(PP^T)]^(-1/6)`,          (1.15)

and

`r=2: sup_a E|Q-a|^(-1/2)
      <=4 sqrt(2)e^(1/4)[det(PP^T)]^(-1/8).`                    (1.16)

#### Proof

Push the arbitrary phase on the `r` literal coordinates to that coordinate vector. Its density cap is one, hence the complex density has `L^2` norm at most one. Push the phase-weighted opposite bank through `PX`; the total variation is dominated by the ordinary projected law, whose density is bounded by `e^(r/2)/sqrt(det(PP^T))` by the baseline projection lemma plus deterministic scaling. Cauchy-Schwarz and Plancherel at scale `2t` give (1.14). For `r=3`, integrate `min(1,K|t|^-3/2)` and divide by `2*pi`; for `r=2`, insert `min(1,K/|t|)` into the baseline Riesz formula and use `int_R min(1,K/|t|)|t|^-1/2 dt=8 sqrt(K)`. This yields (1.15)-(1.16). QED.

## 2. Marginal-free order-three crossing volume gives a density

For a literal original-coordinate cross block `M` with rows `m_i`, put

`Z=E_3(M)=e_3(MM^T)>0`.

For each physical row `i`, let `J_i` be the sum of all three-row Gram determinants containing `i`. Then

`sum_i J_i=3Z`.                                                  (2.1)

### Proposition 3

For the full quadratic polynomial, with arbitrary same-bank and outside phases retained,

`boxed: ||p_Q||_infinity <= C_3 Z^(-1/6),`

where

`C_3=3 sqrt(2)e(9/2)^(1/6)=14.818337662843...`.                 (2.2)

This branch has a continuous `C_0` density.

#### Proof

If every `J_i/Z<=1/2`, use Lemma 1 with `(k,ell,d)=(0,3,3)`, `M_H=S=1`. Formula (1.4) gives exactly the constant `C_3` in (2.2).

Otherwise select a row `w=m_i` with `J_i>Z/2` and promote the literal coordinate `X_i` to the hub. Orthogonally project every remaining row off `w`, obtaining residual row matrix `C`. Gram-Schmidt gives the exact aggregate identity

`J_i=||w||^2 e_2(CC^T).`                                        (2.3)

If every order-two residual row marginal is at most one half, apply Lemma 1 with `(k,ell,d)=(1,2,3)`. Here `S=||w||` and `Z_2=e_2(CC^T)`, so the product of scale factors is `J_i^-1/6`; the numerical coefficient is `<10.958`, hence below `C_3 Z^-1/6`.

If a residual physical row `j` carries more than half the `E_2(C)` mass, promote it. Let `P` be the two promoted rows and let `C_2` be every remaining row projected orthogonally off `row(P)`. A second Gram-Schmidt identity gives

`H_ij=det(PP^T)||C_2||_F^2 > J_i/2 > Z/4`.                      (2.4)

If every order-one marginal of `C_2` is at most one half, Lemma 1 with `(k,ell,d)=(2,1,3)` gives a coefficient `<8.264` times `H_ij^-1/6`, again below the bound (2.2).

Finally, if some residual row carries more than half of `||C_2||_F^2`, promote that row too. The resulting literal three-row block `P_3` satisfies

`det(P_3P_3^T)>H_ij/2>Z/8`.                                     (2.5)

Lemma 2 with `r=3` gives a coefficient `<7` times `Z^-1/6`. Thus all promotion branches obey (2.2). Each branch supplied an integrable characteristic-function majorant, so inversion also gives a continuous density vanishing at infinity. QED.

## 3. Marginal-free order-two crossing volume gives a half potential

For a literal cross block `M`, put

`Z=E_2(M)=e_2(MM^T)>0`.

### Proposition 4

For the full quadratic polynomial,

`boxed: sup_a E|Q-a|^(-1/2) <= C_2 Z^(-1/8),`

where

`C_2=8 sqrt(e)2^(-1/8)=12.095072570796...`.                     (3.1)

#### Proof

If every canonical `E_2` row marginal is at most one half, Lemma 1 at `(k,ell,d)=(0,2,2)` gives

`|phi_Q(t)| <= min(1,L/|t|),`

`L=pi e 2^(3/4) Z^-1/4`.                                        (3.2)

The baseline Riesz inequality and

`int_R min(1,L/|t|)|t|^-1/2 dt=8 sqrt(L)`                       (3.3)

give exactly (3.1).

If a row `w=m_i` carries incident order-two mass `K_i>Z/2`, project all other rows off `w`. The exact identity is

`K_i=||w||^2||C||_F^2`.                                         (3.4)

If the residual order-one marginals are all at most one half, use Lemma 1 with `(k,ell,d)=(1,1,2)` and (3.3); the resulting coefficient is

`8*2^(-3/8)e^(3/8) K_i^-1/8 <9.79 Z^-1/8`.

If a residual row is heavy, promote it. The literal two-row Gram determinant then satisfies

`D>K_i/2>Z/4`.                                                   (3.5)

Lemma 2 with `r=2` gives `<8.64 Z^-1/8`. Both are smaller than `C_2 Z^-1/8`. QED.

This is a half-potential theorem only; it is not an order-two bounded-density theorem.

## 4. Sharpen the baseline pivot half-potential constant

The baseline manuscript rounds two elementary constants more aggressively than necessary. Retaining the constants already proved there improves the scalar-pivot branch.

### Lemma 5 — sharper one-direction logarithmic potential

If a quadratic polynomial `R=X^TSX+linear+constant` has `||S||>=1`, then

`sup_a E log_+(1/|R-a|) <= L_*:=4+4 log(40/3).`                  (4.1)

#### Proof

In the baseline proof of the quarter-power concentration lemma, before the last rounding, the coefficient is bounded by

`2^(5/8) pi^(-1/4)e^(3/8) Gamma(3/8) <40/3`.

This is already proved there from `Gamma(3/8)<=8/3+e^-1<10/3`, `2^(5/8)<2`, `e^(3/8)<2`, and `pi^-1/4<1`. Therefore

`P{|R-a|<rho} <= min(1,(40/3) rho^(1/4))`                       (4.2)

when `||S||>=1`. Layer cake gives

`E log_+(1/|R-a|)
 =int_0^infinity P{|R-a|<e^-u}du
 <=int_0^infinity min(1,(40/3)e^-u/4)du
 =4+4log(40/3).`                                                (4.3)

QED.

### Lemma 6 — sharper singular kernel

For `d!=0`, the baseline kernel proof actually yields

`J(d)=int_-1^1 |x|^-1/2|x-d|^-1/2 dx
 <=8+2 sqrt(2) log_+(1/|d|).`                                   (4.4)

#### Proof

The baseline near region `|x|<=2|d|` is bounded by the scaled explicit integral `<8`. On the complement, `|x-d|>=|x|/2`, hence the integrand is at most `sqrt(2)/|x|`. Integrating on the positive and negative parts of `[-1,1]` gives at most

`2 sqrt(2) log_+(1/(2|d|)) <=2 sqrt(2)log_+(1/|d|)`.            (4.5)

QED.

### Proposition 7 — improved pivot half potential

If a symmetric quadratic part has at least two eigenvalues of modulus at least one and contains an `eta=1/100` pivot in the baseline sense, then

`H(Q):=sup_a E[|Q-a|^-1/2 1_{|Q-a|<=1}] <487.`                  (4.6)

Hence its full half potential is `<488`.

#### Proof

For a scalar pivot `|A_ii|>=eta`, the exact conditional square profile and Lemma 6 give

`H(Q) <= eta^-1/2 [8+2 sqrt(2)L_*]`.

Using (4.1),

`10[8+2 sqrt(2)(4+4log(40/3))]
 =486.1923614333... <487.`                                      (4.7)

For a definite pair, the baseline bound is `4*pi*eta^-1/2=40*pi<126<487`.

For an indefinite pair with determinant magnitude `D>=eta`, the baseline conditional hyperbolic estimate and logarithmic-kernel bound give

`D^-1/2[32+4log_+(16 sqrt D)]`.

Using `D^-1/2<=10` on the constant term and

`sup_{D>0} D^-1/2 log_+ D=2/e`,

this is at most

`10(32+4log16)+4/e=432.3751...<433<487.`                         (4.8)

These exhaust the pivot alternatives. Outside `|Q-a|<=1`, the kernel `|Q-a|^-1/2` is at most one, so the full half potential is `<488`. QED.

## 5. Proof of Theorem B02-9 in the normalized case

Assume `K=s=1` and `s_9(A)>=1`.

### Case 1: no coordinate pivot

Apply the audited baseline no-pivot spectral-to-volume proposition with `k=3`. Since `4k-3=9`,

`V_3(A)>=kappa^3`.                                               (5.1)

The fair original-coordinate cut gives a literal cross block `M` with

`E_3(M)>=4^-3 kappa^3`.                                         (5.2)

Therefore

`E_3(M)^(-1/6) <=2 kappa^-1/2=160`.                             (5.3)

Proposition 3 yields

`||p_Q||_infinity <=160 C_3
 =2370.93402605488...<2400<4880.`                                (5.4)

This branch has a continuous `C_0` density.

### Case 2: scalar pivot

Suppose `|A_hh|>=eta`. Completing the square in the original coordinate `X_h`, the audited Schur spectral-count lemma leaves at least eight eigenvalues of modulus at least one in the exact Schur complement `S`.

If `S` contains an `eta`-pivot, Proposition 7 applies because it has at least two large eigenvalues. The full half potential of the Schur quadratic remainder is `<488`.

If `S` has no `eta`-pivot, then `s_5(S)>=1`. Apply the baseline spectral-to-volume proposition with `k=2` and then the fair-cut lemma. A literal cross block `M_S` satisfies

`E_2(M_S)>=4^-2 kappa^2`.                                       (5.5)

Proposition 4 then gives

`sup_a E|R-a|^-1/2
 <=C_2(4^-2 kappa^2)^(-1/8)
 =C_2 sqrt(160)
 =152.99191115498...<153<488.`                                  (5.6)

Thus in either subcase the Schur remainder has full half potential `<488`. The baseline scalar-square profile therefore gives

`||p_Q||_infinity < eta^-1/2 *488 = 4880.`                      (5.7)

### Case 3: definite two-coordinate pivot

Condition on the complement. The audited baseline definite-pair lemma gives

`||p_Q||_infinity <=pi/sqrt(eta)=10pi<32<4880.`                 (5.8)

### Case 4: indefinite two-coordinate pivot

Its exact Schur complement loses at most two large directions, so from `s_9(A)>=1` it retains at least seven and in particular has operator norm at least one. The audited hyperbolic-pair envelope and Lemma 5 control the conditional critical-value logarithm. Even the baseline coarser calculation gives `<251`, so certainly

`||p_Q||_infinity<251<4880.`                                    (5.9)

The scalar, definite-pair, indefinite-pair and no-pivot alternatives exhaust the normalized problem. This proves

`||p_Q||_infinity<=4880`                                        (5.10)

(the strict inequalities above permit the non-strict rounded statement).

## 6. Scaling to arbitrary `K,s`

Set `Y=KX`. Each coordinate of `Y` has density bounded by one. Define

`Qtilde=Y^T(A/s)Y+(K/s)b^T Y+(K^2/s)c`.

Then `s_9(A/s)>=1` and

`Q=(s/K^2)Qtilde`.

Applying (5.10) to `Qtilde` and transforming a one-dimensional density under scalar multiplication yields

`boxed: ||p_Q||_infinity <=4880 K^2/s.`                          (6.1)

This proves Theorem B02-9.

## 7. Dependency map

The new proof uses the following baseline results, all independently reconstructed in the sibling B02 audit:

- Fourier convention, Plancherel/inversion and Riesz half-potential normalization (`lem:fourier`, `lem:riesz`).
- Geometric rank-one Brascamp–Lieb and product-projection density cap (`thm:bl`, `lem:projection`).
- Integrated scalar Fourier powers and difference-density cap (`lem:scalar-fourier`).
- Schur spectral count (`lem:schur`).
- Scalar square profile, definite and hyperbolic pair estimates, quarter-power concentration (`lem:square`, `lem:definite`, `lem:hyperbola`, `lem:quarter`).
- Disjoint-volume interpolation, completion, no-pivot spectral-to-volume conversion, and fair coordinate cut (`lem:sampling`, `lem:completion`, `prop:volume`, `lem:cut`).
- Elementary singular kernels (`lem:kernels`).

The new work consists of Lemmas 1–2, Propositions 3–4, the retained-constant Lemmas 5–6/Proposition 7, and the threshold-nine assembly.

## 8. Review state and lower-threshold frontier

This B02 report is an independent complete reconstruction of the threshold-nine proof. A separate complete PASS review exists from account01/B16 at commit `54ec2a651d854563f8db0d92c4c3426f76551786`. Thus the owner-requested **two separate complete review evidence condition is met** for this mathematical candidate (B16 plus B02). This is not formal verification, journal peer review, or a self-authorized release decision; concurrent findings still require owner/release-gate reconciliation.

I did not prove a theorem under `s_8(A)>=s`. The strongest exact eight-direction reduction currently available says that in the no-pivot branch either order-three disjoint volume is already large and Proposition 3 pays it, or a quantitative overlap-one/two-sided physical collar remains. A general receiver for that collar when the shared physical diagonal is zero or arbitrarily small is still missing. Therefore 9 is the lowest complete threshold proved here; 8 remains an explicit open proof obligation, and the unrestricted three-direction conjecture remains open.

Model: GPT-5.6 Sol. Effort/reasoning telemetry: UNKNOWN/not exposed.
