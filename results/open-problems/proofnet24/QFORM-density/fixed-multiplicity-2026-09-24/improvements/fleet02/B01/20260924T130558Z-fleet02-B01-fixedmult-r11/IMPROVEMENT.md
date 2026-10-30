# fleet02/B01 improvement — complete nine-eigenvalue replacement and exact eight-direction boundary

Run: `20260924T130558Z-fleet02-B01-fixedmult-r11`  
Baseline manuscript: source commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.  
Live `master` observed during the run through `8a2a3a4bfcb01b398f35ee2db350a6188bf2395c` before this file was created.

## Result

After independently auditing the 790-line 17-direction manuscript, I independently reconstructed and checked a complete reduction to **nine** spectral directions. The proof below preserves every theorem quantifier.

### Theorem `QFORM-FIXED-MULTIPLICITY-9-B01-REVIEWED-v1`

Let `X=(X_1,...,X_n)` have independent real coordinates with densities `0<=f_i<=K`, where `0<K<infinity`. Let `A=A^T` be arbitrary, and let `b,c` be arbitrary. If

` s_9(A)>=s>0,`

then `Q=X^TAX+b^TX+c` has an essentially bounded density and

` ||p_Q||_infinity <= 6010 K^2/s.`

No global continuity conclusion is claimed. No Gaussian/log-concavity, moment, support, sign, diagonal-basis, exact-rank, leverage, or post-rotation-independence hypothesis is added.

This is a complete replacement proof, not an inference from the 17-direction theorem. The baseline pivot analysis is retained; the order-five no-pivot endpoint is replaced by a marginal-free order-three product-Fourier receiver, and the scalar-pivot Schur remainder uses a marginal-free order-two half-potential receiver.

The source repository also contains other workers' nine-direction derivations/reviews. They were used only as source-backed comparison after the algebra below was reconstructed; their PASS labels are not substituted for this review.

## 1. Normalization

It suffices to prove the theorem for `K=s=1`. At the end put `Y=KX` and

`Qtilde=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c`.

Then every `Y_i` has density at most one, `s_9(A/s)>=1`, and

`Q=(s/K^2)Qtilde`.

Thus a normalized constant `C` becomes exactly `C K^2/s`.

Keep the manuscript parameters

`eta=1/100`, `kappa=1/80^2=1/6400`.

## 2. Grouped product-Fourier lemma, with the delicate pushforward step made explicit

Let `H,I,J` be disjoint original-coordinate banks. Let `W` be a `k`-dimensional orthogonal projection of `X_H` with density bounded by `M_H`. Let `X'=(X_I,X_J)` and consider

`Q=F(X_H)+2<W,M X'+beta>+R(X')`,

where `F` is arbitrary measurable, `R` is an arbitrary quadratic polynomial, and the `J` restriction `M_J` has row rank `k`. Let `S` be the product of the nonzero singular values of `M_J`. Write

`C=(A_R)_[I,J](I-Pi_row(M_J)).`

For `ell>=1`, let

`Z_ell=sum_{|T|=ell} det(C_T C_T^T)>0`,
`w_T=det(C_T C_T^T)/Z_ell`,
`alpha_i=P_w(i in T)`.

Assume every `alpha_i<=1/2`, and put `d=k+ell`.

### Lemma 2.1

For `t!=0`,

`|phi_Q(t)| <= min(1,K_{k,ell}|t|^{-d/2})`,

where

`K_{k,ell}=M_H^(1/2) pi^(d/2) 2^(ell/4) e^((k+2ell)/4)
             (ell^ell/ell!)^(1/4) S^(-1/2) Z_ell^(-1/4).`          (2.1)

If `d>2`, Fourier inversion gives

`||p_Q||_infinity
 <= [d/(d-2)] M_H^(1/d) 2^(ell/(2d)) e^((k+2ell)/(2d))
    (ell^ell/ell!)^(1/(2d)) S^(-1/d) Z_ell^(-1/(2d)).`           (2.2)

### Proof

Push the complex measure `e^{itF}dP_H` to `W`. Its density `a_t` satisfies `|a_t|<=p_W`, whence

`||a_t||_2^2<=M_H`.

With the manuscript Fourier convention, `k`-dimensional Plancherel and the scale `2t` give

`int |hat a_t(2t(l+beta))|^2 dl <= M_H (pi/|t|)^k.`              (2.3)

Push `e^{itR}dP_{X'}` by the linear map `MX'`; call the resulting complex density `mu_t`. Then

`phi_Q(t)=int hat a_t(2t(l+beta)) mu_t(l) dl`,

so Cauchy--Schwarz gives

`|phi_Q(t)|^2<=M_H(pi/|t|)^k ||mu_t||_2^2.`                      (2.4)

The only delicate point is the full-form estimate for `||mu_t||_2`. Here is the product-safe derivation. Condition first on one value `X_I=x`. Let `mu_{t,x}` be the complex pushforward of `e^{itR(x,X_J)}dP_J` by `M_Ix+M_JX_J`. Convexity of the squared `L^2` norm gives

`||mu_t||_2^2 <= E_{X_I} ||mu_{t,X_I}||_2^2.`                    (2.5)

Use a compactly supported approximate identity if desired before expanding the square. For fixed `x`, expansion uses only an independent copy `X'_J` of the `J` bank; there is no copied `I` bank. Consequently the pure `I` part of `R` cancels exactly, while the difference of pure `J` phases has modulus one. Writing `D=X_J-X'_J`, the cross term in `R` is

`2 x^T (A_R)_[I,J] D`.

Averaging (2.5) over the original independent `X_i`, `i in I`, therefore gives scalar characteristic functions evaluated at the literal cross-row forms. The approximate identity contributes a probability kernel in `M_JD`. Thus uniformly in the regularizer one obtains

`E_D [ kappa(M_JD) prod_i |psi_i(2t<a_i,D>)| ]`,                (2.6)

where `kappa` is a probability density, each `psi_i` is the characteristic function of a cap-one original `I`-coordinate law, and `a_i` is the corresponding row of `(A_R)_[I,J]`. This derivation is why no conditional cap or post-rotation independence is needed.

Decompose

`a_i=c_i+lambda_i M_J`,

with `c_i` orthogonal to `row(M_J)`. For an `ell`-set `T`, the map

`D -> (M_JD,(<c_i,D>)_{i in T})`

has Gram determinant

`S^2 det(C_T C_T^T).`                                           (2.7)

The manuscript product-projection lemma, applied to the independent cap-one coordinates of `D`, therefore bounds the density of this `d`-dimensional linear image by

`e^(d/2)/[S sqrt(det(C_T C_T^T))].`                              (2.8)

Weighted Holder with weights `w_T` produces powers `1/alpha_i`. Since `alpha_i<=1/2`, the manuscript scalar Fourier-power theorem at `p=1/alpha_i>=2`, with the scaling `2t`, gives

`int |psi_i(2t(y+u))|^(1/alpha_i)dy
 <= pi sqrt(2e alpha_i)/|t|.`                                   (2.9)

Hence the `T` term is bounded by

`e^(d/2)[pi sqrt(2e)/|t|]^ell
 prod_{i in T} sqrt(alpha_i)
 /[S sqrt(det(C_T C_T^T))].`                                    (2.10)

The determinant-weight geometric mean is

`Z_ell^(-1/2) exp(H(w)/2)`

because `det(C_T C_T^T)=w_T Z_ell`. The marginal factors give

`exp[(1/2)sum_i alpha_i log alpha_i]`.

To close the dimension-free entropy factor, sample `T~w` and then a uniform random ordering `(I_1,...,I_ell)` of its elements. Its entropy is `H(w)+log(ell!)`. Subadditivity gives

`H(w)+log(ell!) <= sum_{j=1}^ell H(I_j)`.

The average law of each ordered coordinate has probabilities `alpha_i/ell`; concavity of entropy plus symmetry gives

`sum_j H(I_j) <= ell H(alpha/ell)
               =ell log ell-sum_i alpha_i log alpha_i`.

Therefore

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!).`        (2.11)

Combining (2.4)--(2.11), then removing the approximate identity by the lower-semicontinuity/`L^2` limit, gives (2.1). Finally

`int_R min(1,K|t|^{-d/2})dt = [2d/(d-2)]K^(2/d)`

for `d>2`; the manuscript inversion normalization `1/(2pi)` gives (2.2). QED.

### Terminal exact-rank forms

The same complex-pushforward/Plancherel proof with no residual projected crossing gives, for `r` literal physical rows crossing a product bank through full-row-rank block `P`, arbitrary same-bank and affine phases retained,

`|phi(t)|<=min(1,pi^(r/2)e^(r/4)det(PP^T)^(-1/4)|t|^(-r/2)).`    (2.12)

Consequently

`r=3: ||p||_infinity <=3 sqrt(e) det(PP^T)^(-1/6),`              (2.13)

and the manuscript Riesz formula gives

`r=2: sup_a E|Q-a|^(-1/2)
      <=4 sqrt(2)e^(1/4) det(PP^T)^(-1/8).`                      (2.14)

## 3. Marginal-free third crossing volume

For a literal original-coordinate crossing block `M`, define

`Z=E_3(M)=e_3(MM^T)>0`.

For each physical row `i`, let `J_i` be the sum of all three-row Gram determinants containing `i`. Then

`sum_i J_i=3Z.`                                                  (3.1)

If every `J_i/Z<=1/2`, Lemma 2.1 with `(k,ell,d)=(0,3,3)` gives

`||p_Q||_infinity <= C_3 Z^(-1/6),`
`C_3=3 sqrt(2)e(9/2)^(1/6)=14.818337662843... .`                 (3.2)

If some `J_i>Z/2`, promote that literal row. Let `w` be the row and project all other rows orthogonally off `w`, obtaining `C`. Gram--Schmidt gives the exact aggregate identity

`J_i=||w||^2 e_2(CC^T).`                                        (3.3)

If the `E_2(C)` row marginals are all at most `1/2`, Lemma 2.1 at `(k,ell,d)=(1,2,3)` gives a constant `<10.958 Z^(-1/6)`.

Otherwise promote a residual heavy row `j`. If `P` is the two promoted rows and `C_2` denotes all remaining rows projected off `row(P)`, then

`H_ij=det(PP^T)||C_2||_F^2>J_i/2>Z/4.`                          (3.4)

If every residual one-volume marginal is at most `1/2`, Lemma 2.1 at `(2,1,3)` gives `<8.264 Z^(-1/6)`. If one residual row is heavy, the three promoted rows have

`det(P_3P_3^T)>H_ij/2>Z/8`,                                     (3.5)

and (2.13) gives `<3sqrt(2e)Z^(-1/6)<7Z^(-1/6)`.

Therefore, without any row-leverage condition,

`boxed: ||p_Q||_infinity <=C_3 E_3(M)^(-1/6).`                   (3.6)

Every branch here has an integrable characteristic-function envelope, so this fixed-crossing conclusion is continuous; that local regularity will not be promoted to the whole theorem.

## 4. Marginal-free second crossing volume gives a full half potential

For a literal cross block put

`Z=E_2(M)=e_2(MM^T)>0.`

If every canonical row marginal is at most `1/2`, Lemma 2.1 with `(0,2,2)` gives

`|phi(t)|<=min(1,pi e 2^(3/4) Z^(-1/4)|t|^(-1)).`               (4.1)

Since

`int_R |t|^(-1/2) min(1,L/|t|)dt=8sqrt(L)`,

the manuscript Riesz formula yields

`sup_a E|Q-a|^(-1/2)<=C_2 Z^(-1/8),`
`C_2=8 sqrt(e)2^(-1/8)=12.095072570796... .`                    (4.2)

If one physical row carries incident mass `K_i>Z/2`, project the other rows off it. Then

`K_i=||w||^2||C||_F^2.`                                         (4.3)

If residual one-volume marginals are all at most `1/2`, Lemma 2.1 at `(1,1,2)` plus the same Riesz integral gives `<9.79 Z^(-1/8)`. Otherwise a second promoted physical row has Gram determinant

`D>K_i/2>Z/4`,                                                   (4.4)

and (2.14) gives `<8.64 Z^(-1/8)`. Thus

`boxed: sup_a E|Q-a|^(-1/2)<=C_2 E_2(M)^(-1/8).`                 (4.5)

**Counterexample boundary.** This is intentionally a half-potential theorem, not a density theorem. For independent uniform variables, `2XY` has a logarithmically divergent density at zero, so any attempt to promote (4.5) to a generic rank-two bounded-density statement is false.

## 5. Nine spectral directions: full proof

Assume `K=s=1` and `s_9(A)>=1`.

### 5.1 No `eta`-pivot

The audited manuscript spectral-to-volume proposition with `k=3` applies exactly at `4k-3=9`:

`V_3(A)>=kappa^3.`                                               (5.1)

The audited fair original-coordinate cut gives a literal block `M=A[I,J]` with

`E_3(M)>=4^(-3)kappa^3.`                                        (5.2)

Hence

`E_3(M)^(-1/6)<=2 kappa^(-1/2)=160`,

and (3.6) gives

`||p_Q||_infinity<=160 C_3
 =2370.93402605488...<2400.`                                     (5.3)

### 5.2 Scalar pivot

If `|A_hh|>=eta`, complete the square in the literal original coordinate `X_h`. The manuscript Schur theorem leaves at least eight unit spectral directions in the remainder `S`.

If `S` has an `eta`-pivot, the audited manuscript pivot proposition requires only two large directions and gives truncated half-potential `<=600`; adding at most one from `|R-a|>1` gives full half-potential `<=601`.

If `S` has no `eta`-pivot, then `s_5(S)>=1`. Apply the audited spectral-to-volume proposition with `k=2` and the fair cut:

`E_2(M_S)>=4^(-2)kappa^2.`                                      (5.4)

By (4.5),

`sup_a E|R-a|^(-1/2)
 <=C_2(4^(-2)kappa^2)^(-1/8)
 =C_2 sqrt(160)
 =152.99191115498...<153.`                                      (5.5)

Thus every scalar-pivot Schur remainder has full half-potential `<=601`. The audited conditional square profile therefore gives

`||p_Q||_infinity<=eta^(-1/2)*601=6010.`                         (5.6)

No independence between the completed square and `R` is used.

### 5.3 Definite two-coordinate pivot

Condition on the complement and apply the manuscript definite-pair theorem:

`||p_Q||_infinity<=pi/sqrt(eta)=10pi<32.`                        (5.7)

### 5.4 Indefinite two-coordinate pivot

The Schur count leaves at least seven unit directions, hence in particular operator norm at least one. The manuscript hyperbolic envelope and quarter/logarithmic-potential theorem therefore apply verbatim, giving

`||p_Q||_infinity<251.`                                         (5.8)

These four alternatives exhaust the normalized problem. The maximum is `6010`, proving the normalized theorem. Section 1 then yields

`boxed: ||p_Q||_infinity<=6010 K^2/s.`                           (5.9)

## 6. Closed dependency map

Only the following audited baseline ingredients are imported:

1. Fourier normalization / inversion and Riesz formula (`lem:fourier`, `lem:riesz`).
2. Geometric BL, product projection and scalar Fourier powers (`thm:bl`, `lem:projection`, `lem:scalar-fourier`).
3. Schur spectral count and scalar/definite/hyperbolic pivot estimates (`lem:schur`, `lem:square`, `lem:definite`, `lem:hyperbola`, `lem:quarter`, `prop:pivot-H`).
4. Nonsymmetric disjoint-minor interpolation, spectral-to-volume and fair cut (`lem:sampling`, `lem:completion`, `prop:volume`, `lem:cut`).

New Lemma 2.1 is proved above from items 1--2. Sections 3--4 are finite literal-row promotion trees from Lemma 2.1 and the exact-rank endpoint (2.12). Section 5 combines those with items 3--4. There is no dependency on the 17-direction main theorem itself, no dependency on a rotated product law, and no hidden conditional-density-cap assumption.

## 7. How far can this run rigorously lower the multiplicity?

**Complete theorem: nine.** I do not claim eight.

A newer source-backed structural calculation on live `master` isolates the exact multiplicity-eight no-pivot boundary. I independently checked its rank/sampling arithmetic because it directly tests whether the nine proof can be pushed one step farther. Under no `eta`-pivot and `s_8(A)>=1`, either `V_3>=kappa^3` (then Section 3 already pays the density), or one obtains a terminal collar with

`V_2>=kappa^2`,

`Omega_1>=c_*^2 kappa^2`,

`Xi_2>=(delta_*^2/2) kappa^2`,

where

`epsilon_*=sqrt(18kappa)=3sqrt(2)/80`,
`c_*=1-epsilon_*`,
`delta_*=(1-epsilon_*-eta)^2-(sqrt(eta^2+eta)+epsilon_*)^2
        =97/100-(297sqrt(2)+3sqrt(202))/4000
        =0.85433514019...>0.`

The derivation is sound: `V_3<kappa^3` forces `V_2>=kappa^2`; determinant-squared sampling at order two and Markov retain at least half the seed mass with `||E||_F<=epsilon_*`; rank `R<=6` plus `s_8(A-E)>=1-epsilon_*` forces two large `D` entries in the seed complement; bordered determinants create `Omega_1`, and the exact factorization

`P[H,H]=A[H,T] B^(-1) A[S,H]`

plus strict determinant lower bound `delta_*` creates `Xi_2`.

This is a **PASS structural reduction**, not an eight-direction density theorem. The remaining implication is a genuine **GAP**:

`QFORM-EIGHT-OVERLAP1-TWOSIDED-COLLAR-RECEIVER`:
convert the quantitative overlap-one/two-sided collar (`Omega_1`,`Xi_2`) into a dimension-free bounded-density estimate while retaining arbitrary same-bank curvature and allowing the common physical diagonal to be zero.

The existing scalar-overlap receivers can lose a reciprocal factor in that common diagonal, which is allowed to vanish. `Xi_2` alone is also not automatically an order-three disjoint crossing volume; the shared physical hub is precisely the obstruction. Therefore claiming `s_8` at this point would leave an unpaid analytic implication.

The unrestricted three-eigenvalue conjecture remains open and is not claimed here.

## Review status

This run supplies one independent end-to-end baseline review plus one independent reconstruction of the nine-direction replacement. The live repository also contains source-backed separate nine-direction reviews, but owner/B20 synthesis decides release/promotion state. This file does not rewrite the pinned 17-direction manuscript or self-award a release certificate.
