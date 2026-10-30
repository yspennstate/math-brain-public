# fleet02/B05 r13 — independent B05 reconstruction of the nine-eigenvalue replacement

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T135740Z-fleet02-B05-fixedmult-audit-r13`  
Pinned baseline: commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.  
Candidate cross-check source read after the independent baseline audit: fleet01/B07 blob `974f935ea42a5f8f6dcdeb6255b0ca64d7d59ffd`, together with the fleet03/B04 grouped-compiler report. The proof below was reconstructed equation-by-equation with the B05 product-projection/rough-slice lens rather than accepting their PASS labels.

## Verdict

**PASS in this independent reconstruction of a complete unconditional nine-eigenvalue theorem.**

> If `X_i` are independent real random variables with densities bounded by `K`, `A=A^T` is arbitrary, `b,c` are arbitrary, and `s_9(A)>=s>0`, then `Q=X^TAX+b^TX+c` has an essentially bounded density and
>
> `||p_Q||_infinity <= (2010+1200 log 16) K^2/s < 5338 K^2/s`.

The no-pivot Fourier branch has a continuous density. No continuity claim is made for all pivot branches. This theorem is not the unrestricted three-eigenvalue QFORM conjecture. I do not claim a theorem at multiplicity eight here.

## Dependency map

The replacement uses only the following already-audited baseline results from the pinned manuscript:

1. geometric BL (`thm:bl`) and product-projection density (`lem:projection`), including the full-row-rank corollary `||p_{LX}||_infinity<=e^(d/2)/sqrt(det(LL^T))`;
2. scalar Fourier powers (`lem:scalar-fourier`), Fourier inversion and the half-Riesz inequality (`lem:fourier`, `lem:riesz`);
3. Schur spectral count (`lem:schur`), scalar square profile, definite and indefinite pair estimates, and the logarithmic potential from `lem:quarter`;
4. the no-pivot spectral-to-volume proposition (`prop:volume`) and random cut (`lem:cut`) at orders two and three.

The only new analytic input is the grouped product-Fourier compiler proved next, followed by two finite promotion trees that eliminate its marginal hypotheses.

## 1. Grouped product-Fourier compiler with rough-law limit

Let `H,I,J` be disjoint sets of **original coordinates**. Let

`W=L_H X_H in R^k`, with `L_H L_H^T=I_k`,

and suppose its density has cap `M_H`. Write `X'=(X_I,X_J)` and

`Q=F(X_H)+2 <W,M X'+beta>+R(X')`,

where `F` is arbitrary measurable, `R` is an arbitrary quadratic/affine polynomial, and the `J`-column block `M_J` has row rank `k`. Put

`S=sqrt(det(M_J M_J^T))`,

the product of its nonzero singular values. For every physical row `a_i`, `i in I`, of the `I x J` cross block of the quadratic part of `R`, decompose

`a_i=c_i+lambda_i M_J`, `c_i perpendicular row(M_J)`.

For `ell>=1`, define

`Z_ell=sum_{|T|=ell} det(C_T C_T^T)`,

where `C_T` has rows `c_i`, `i in T`. Assume `Z_ell>0`, set

`w_T=det(C_T C_T^T)/Z_ell`, `alpha_i=sum_{T contains i} w_T`,

and suppose every nonzero `alpha_i<=1/2`. Put `d=k+ell`.

### 1.1 Hub Plancherel

Push the complex measure `e^{itF(X_H)} dP_H` through `W`. It has density

`a_t(w)=E[e^{itF(X_H)} | W=w] p_W(w)`

in the usual Radon--Nikodym sense, so `|a_t|<=p_W` and

`||a_t||_2^2<=||p_W||_infinity ||p_W||_1<=M_H`.

Push `e^{itR(X')}dP_{X'}` through `y=M X'`; since `M_J` has row rank `k`, the probability pushforward is absolutely continuous by the full-row-rank projection lemma, hence the complex pushforward has a density `mu_t`. Fourier pairing, Cauchy--Schwarz, Plancherel, and the dilation `xi=2t w` give exactly

`|phi_Q(t)|^2 <= M_H (pi/|t|)^k ||mu_t||_2^2`.                 (1)

No component of `W` is declared independent of another component. Only its joint density cap is used.

### 1.2 Light-bank `L2` estimate without smoothness

Condition on `X_I=x`. Let `nu_x` be the conditional complex pushforward through `M_J X_J`. Its `L2` norm need not be known a priori, so convolve with a compact probability approximate identity `rho_eps`; put `kappa_eps=rho_eps*tilde(rho_eps)`.

Hilbert-space Jensen bounds the squared norm of the smoothed mixture by the mean squared conditional norms. Expand each squared norm with an independent copy `X'_J`. If `D=X_J-X'_J`, the pure-`I` phase cancels, the pure-`J` phase has modulus one, and averaging in the original independent `X_i`, `i in I`, before taking absolute values gives

`E_x ||nu_x*rho_eps||_2^2
 <= E_D [ kappa_eps(M_J D) prod_{i in I} |psi_i(2t<a_i,D>)| ]`,   (2)

where `psi_i` is the characteristic function of the original law of `X_i`. The coordinates of `D` are independent and have densities bounded by one.

The bound below is uniform in `eps`. On the Fourier side `hat rho_eps ->1` and `|hat rho_eps|<=1`; Fatou gives

`||nu_x||_2^2 <= liminf_{eps->0} ||nu_x*rho_eps||_2^2`

with extended values, and another Fatou/Jensen step passes the uniform estimate to the unsmoothed mixture. Thus (2) introduces no support, moment, continuity, or density-slice assumption.

### 1.3 Weighted physical projection

Rows with `alpha_i=0` have Fourier factors at most one and are discarded. For the rest, write `q_i=|psi_i(2t<a_i,D>)|`. The exact weighted-subset identity is

`prod_i q_i = prod_T [prod_{i in T} q_i^(1/alpha_i)]^(w_T)`.

If some `q_i=0`, this is justified by replacing every `q_i` by `q_i+delta`, applying generalized Holder, and sending `delta` down to zero; no `0^0` convention is needed.

For fixed `T`, the physical linear map

`D -> (M_JD, (<c_i,D>)_{i in T}) in R^d`

has Gram determinant

`S^2 det(C_T C_T^T)`.

Indeed the `c_i` rows are orthogonal to `row(M_J)`. The full-row-rank product-projection corollary therefore gives its joint density cap

`e^(d/2)/[S sqrt(det(C_T C_T^T))]`.

Using this cap in the fixed-`T` expectation, integrate first over the `ell` scalar coordinates. The shifts `lambda_i M_JD` are harmless translations. Since `alpha_i<=1/2`, the audited scalar Fourier-power lemma with `p=1/alpha_i` and scale `2t` gives

`int_R |psi_i(2t(y+u))|^(1/alpha_i) dy
 <= pi sqrt(2e alpha_i)/|t|`.                                  (3)

Because `kappa_eps` is a probability density, the remaining `M_JD` integral costs one. Hence the fixed-`T` bound is

`e^(d/2) [pi sqrt(2e)/|t|]^ell
 prod_{i in T} sqrt(alpha_i)
 /[S sqrt(det(C_T C_T^T))]`.                                   (4)

Taking the weighted geometric mean in Holder produces

`Z_ell^(-1/2) exp( H(w)/2 + (1/2) sum_i alpha_i log alpha_i )`.

Uniformly order the random `ell`-subset `T`. The ordered tuple has entropy `H(w)+log(ell!)`, while every ordered position has marginal `alpha_i/ell`. Entropy subadditivity yields

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!)`.       (5)

Combining (1)--(5) and taking the required square root gives

`|phi_Q(t)| <= min(1,K_{k,ell}|t|^(-d/2))`,                    (6)

where

`K_{k,ell}=M_H^(1/2) pi^(d/2) 2^(ell/4) e^((k+2ell)/4)
             (ell^ell/ell!)^(1/4) S^(-1/2) Z_ell^(-1/4)`.

When `k=0`, the same expanded-square argument has no hub variable and the zero-dimensional kernel is one; (6) is unchanged. For `d>2`, direct integration of the envelope and Fourier inversion give

`||p_Q||_infinity <= [d/(d-2)] M_H^(1/d) 2^(ell/(2d))
 e^((k+2ell)/(2d)) (ell^ell/ell!)^(1/(2d))
 S^(-1/d) Z_ell^(-1/(2d))`.                                    (7)

All sets promoted below are literal disjoint original-coordinate sets, so the only independence ever used is the original product independence.

## 2. Marginal-free third-volume density receiver

Let `M` be a physical cross block and

`Z=E_3(M)=sum_{|T|=3} det(M_T M_T^T)>0`.

Let `J_i` be the total three-row Gram mass through row `i`, so `sum_i J_i=3Z`.

If every `J_i/Z<=1/2`, apply (7) with `(k,ell,d)=(0,3,3)`:

`||p_Q||_infinity <= C_3 Z^-1/6`,

`C_3=3 sqrt(2) e (9/2)^(1/6)=14.818337662843...`.               (8)

If some physical row `w` is heavy, promote its **original coordinate** to `H`. Orthogonal Gram--Schmidt in coefficient space gives exactly

`J_w=||w||^2 E_2(C)`.

If the residual order-two weights are diffuse, use `(1,2,3)`. If one residual physical row is heavy, promote that literal coordinate as a second hub; then

`det(PP^T) E_1(C)>Z/4`.

If the remaining order-one weights are diffuse, use `(2,1,3)`. Otherwise promote the third literal coordinate, obtaining a three-row Gram determinant `>Z/8`, and use `(3,0,3)`.

The four worst constants after spending the guaranteed currency are, respectively,

`14.81834`, `10.95772`, `8.26354`, `6.99494`.

Thus (8) holds **without any marginal hypothesis**. Each branch has an integrable characteristic-function envelope, so this receiver gives a continuous density.

## 3. Marginal-free second-volume half-potential receiver

Let `Z=E_2(M)>0`. The same promotion tree has at most one promoted hub before the terminal two-row branch.

In the diffuse `(0,2,2)` branch, (6) gives

`|phi_Q(t)| <= min(1,L/|t|)`,

`L=pi e 2^(3/4) Z^-1/4`.

The audited half-Riesz inequality and

`int_R |t|^-1/2 min(1,L/|t|) dt=8 sqrt L`

give

`sup_a E|Q-a|^-1/2 <= C_2 Z^-1/8`,

`C_2=8 sqrt(e) 2^-1/8=12.095072570796...`.                     (9)

If one row is heavy, promote it and use `(1,1,2)` with currency `>Z/2`; if the remaining row-volume is heavy, use terminal `(2,0,2)` with two-row determinant currency `>Z/4`. The corresponding constants after currency loss are `9.78798` and `8.63786`, both below `C_2`. Therefore (9) is unconditional.

## 4. Assembly from nine singular directions

Normalize `K=s=1`, with the manuscript values

`eta=1/100`, `kappa=1/80^2`.

### 4.1 No pivot

The audited baseline `prop:volume` at order three uses exactly `s_9(A)>=1` and gives

`V_3(A)>=kappa^3`.

A fair original-coordinate cut gives a physical cross block with

`E_3(M)>=4^-3 kappa^3`, hence `E_3(M)^-1/6<=160`.

By (8),

`||p_Q||_infinity <=160 C_3=2370.934026...<2400`.               (10)

### 4.2 Scalar pivot

A scalar pivot leaves at least eight unit-scale Schur directions. Let the Schur polynomial be `R`.

If `R` has a pivot, re-reading the three branches of the audited baseline `prop:pivot-H` gives the sharper common bound

`H(R)<=200+120 log16`:

the scalar subbranch is exactly `eta^-1/2(8+3(4+4log16))`, while the definite and indefinite pair subbranches are smaller. Adding the outside-unit tail gives

`sup_a E|R-a|^-1/2 <=201+120 log16`.                            (11)

If instead `R` has no pivot, `s_8(R)>=1` implies `s_5(R)>=1`. Apply the audited no-pivot spectral-to-volume proposition at order two and a random cut:

`E_2^-1/8<=sqrt(160)`.

Then (9) gives

`sup_a E|R-a|^-1/2 <= C_2 sqrt(160)=152.991911...`,              (12)

which is smaller than (11). The outer square profile costs `eta^-1/2=10`, so

`||p_Q||_infinity <=2010+1200 log16
 =5337.106466...<5338`.                                         (13)

### 4.3 Pair pivots

A definite pair has conditional density at most `pi/sqrt(eta)=10pi<32`.

An indefinite pair loses at most two Schur directions; at least seven remain. The baseline hyperbolic envelope needs only one nonzero Schur direction to control the random critical value logarithm, so its normalized branch remains below the baseline `251` bound. The exceptional critical graph causes no issue because the application is through nonnegative test functions and Tonelli, not through a pointwise conditional-density selection.

Thus (13) is the largest branch.

### 4.4 Scaling

For general `K,s`, set `Y=KX` and

`Qtilde=Y^T(A/s)Y+(K/s)b^T Y+(K^2/s)c`.

The coordinates of `Y` have densities at most one, `s_9(A/s)>=1`, and

`Q=(s/K^2)Qtilde`.

Therefore

`boxed: ||p_Q||_infinity <=(2010+1200 log16) K^2/s <5338 K^2/s.`

This closes every branch with the original arbitrary affine terms, signs, dimension, remaining spectrum, and rough coordinate laws.

## 5. B05 adversarial checks on the new proof

- The grouped compiler never conditions on a rotated projection and then reuses its unconditional density cap. The only projection bound is for a linear image of an original product bank, used as a joint marginal density.
- Heavy-row promotions move **literal original coordinates** into the hub set. Coefficient-space Gram--Schmidt is algebra only; it creates no new random-coordinate independence.
- The rough conditional pushforward is mollified before an `L2` expansion and passed to the limit by Fourier-side Fatou. There is no hidden smoothness or support hypothesis.
- The pivot branches inherit the baseline measure-level exceptional-slice handling. In particular, a logarithmically infinite critical point of a hyperbolic product does not invalidate the a.e. density bound after Tonelli averaging.
- The counterexamples in the sibling audit show that all four cautions are necessary: conditional projection caps can blow up, hyperbolic products have logarithmic critical singularities, and squares have inverse-square-root singularities.

## 6. Why this run stops at nine

The current order-three no-pivot mechanism has an exact algebraic barrier at a sampled order-two seed: global `rank R<=6` but restricted `rank R[L,L]<=2`. To force three large diagonal entries outside the seed by the existing rank shift requires at least `6+3=9` large singular directions. With eight directions only two are forced, which does not contradict restricted rank two.

A separate current structural reduction shows that multiplicity eight leaves a quantitative overlap-one/two-sided collar, but no product-preserving arbitrary-curvature receiver for its zero/near-zero common-diagonal chamber has been proved in this review. Therefore lowering from 17 to **9** is complete here; lowering to 8 is `UNCHECKED/OPEN`, not asserted.

## Review status

This is an independent fleet02/B05 proof reconstruction after a fresh complete baseline audit. Other workers' reports were used as candidate statements to attack, not as proof certificates. I do not mutate any owner-level release status. The unrestricted three-eigenvalue conjecture remains open.
