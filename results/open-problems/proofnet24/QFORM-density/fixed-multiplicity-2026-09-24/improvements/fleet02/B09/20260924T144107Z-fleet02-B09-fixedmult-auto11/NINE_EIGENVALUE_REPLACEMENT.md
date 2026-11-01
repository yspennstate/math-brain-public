# fleet02/B09 — complete nine-eigenvalue replacement proof

Run: `20260924T144107Z-fleet02-B09-fixedmult-auto11`  
Status: **COMPLETE REPLACEMENT PROOF, independently reconstructed in this run**.  
Pinned baseline: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

This proof lowers the fixed multiplicity from 17 to 9. It preserves arbitrary dimension, signature, remaining spectrum, affine terms, and arbitrary independent real coordinate laws with only a density cap. It does **not** solve the unrestricted three-eigenvalue conjecture.

## Theorem

Let `X=(X_1,...,X_n)` have independent real coordinates with densities bounded by `K<infinity`. Let `A=A^T`, and let `b,c` be arbitrary. If

` s_9(A) >= s > 0,`

then `Q=X^TAX+b^TX+c` has an essentially bounded density satisfying

`boxed: ||p_Q||_infinity <= 6010 K^2/s.`

The proof below is normalized first to `K=s=1` and uses the baseline parameters

`eta=1/100`, `kappa=1/80^2`.

## Audited baseline dependencies

The separate B09 full audit for this run checks all of these at the pinned source:

1. Fourier inversion and the Riesz half-potential formula (`lem:fourier`, `lem:riesz`).
2. Product-projection density cap `e^(d/2)` (`lem:projection`), with the harmless summation wording repair recorded in the audit.
3. Integrated scalar Fourier powers (`lem:scalar-fourier`).
4. Schur spectral count (`lem:schur`).
5. Scalar square profile, definite pair, hyperbolic pair and quarter-power/logarithmic potential (`lem:square`, `lem:definite`, `lem:hyperbola`, `lem:quarter`), with the missing standing product-law hypothesis in `lem:quarter` explicitly restored.
6. Disjoint-volume structural proposition and fair random cut (`prop:volume`, `lem:cut`). In particular, under no pivot, `s_(4k-3)(A)>=1` implies `V_k(A)>=kappa^k` for `k<=5`.

The only new analytic input needed for threshold nine is proved next.

## 1. Grouped hub-light product-Fourier compiler

Fix a literal original-coordinate cut `[n]=I disjoint-union J`. Choose a subset `H subset I` of `k` physical rows and put `I_0=I\H`. Let

`P=A[H,J]`

have row rank `k`; use `S=(det(P P^T))^(1/2)`, with the convention `S=1` for `k=0`. Let `Pi` be the orthogonal projection of `R^J` onto the row space of `P`, and set

`C=A[I_0,J](I-Pi)`.

For `ell>=1`, define

`E_ell(C)=sum_(|T|=ell) det(C_T C_T^T)`

where `T` ranges over `ell` physical rows of `I_0`. Assume `E_ell(C)>0`. Put

`w_T = det(C_T C_T^T)/E_ell(C)`,
`alpha_i = sum_(T contains i) w_T`.

Thus `w` is a probability law on `ell`-subsets and `sum_i alpha_i=ell`. Assume

`alpha_i <= 1/2` for every residual physical row.

Let `d=k+ell`. Then, for the full quadratic polynomial, retaining all same-bank quadratic terms and affine terms,

`|phi_Q(t)| <= min(1, K_(k,ell) |t|^(-d/2))`,

with

`K_(k,ell)
 = pi^(d/2) 2^(ell/4) e^((k+2ell)/4)
   (ell^ell/ell!)^(1/4)
   S^(-1/2) E_ell(C)^(-1/4).`                         (1.1)

If `d>2`, Fourier inversion gives

`||p_Q||_infinity
 <= [d/(d-2)] 2^(ell/(2d)) e^((k+2ell)/(2d))
    (ell^ell/ell!)^(1/(2d))
    S^(-1/d) E_ell(C)^(-1/(2d)).`                    (1.2)

### Proof

Orthogonally change only the deterministic `k`-dimensional hub integral so that the hub-to-`J` cross matrix is represented by its nonzero singular directions. This does not assert independence after rotation: the full `k`-dimensional hub vector has joint density bounded by one because the original physical `X_H` has joint product density bounded by one and the hub rotation has determinant one.

Write the full phase in the form

`F(X_H) + 2 <W, M X' + beta> + R(X')`,

where `X'=(X_(I_0),X_J)`, `W` is the rotated hub vector, the `J`-restriction of `M` has the same nonzero singular values as `P`, and `R` contains **all** residual same-bank curvature and affine terms.

Push the complex measure `exp(itF)dP_H` to `W`. Its density `a_t` satisfies `|a_t|<=p_W`, hence `||a_t||_2^2<=1`. Plancherel and scaling give

`int |hat a_t(2t(l+beta))|^2 dl <= (pi/|t|)^k`.       (1.3)

Push `exp(itR)dP_(X')` to `M X'`, obtaining a complex density `mu_t`. Cauchy--Schwarz gives

`|phi_Q(t)|^2 <= (pi/|t|)^k ||mu_t||_2^2`.            (1.4)

To estimate the last norm, first mollify the pushforward and condition on the residual left bank `X_(I_0)`. Expand the square using an independent copy `X'_J` of the right bank only. Pure left-bank phases cancel; pure right-bank phases have modulus one. With `D=X_J-X'_J`, the coordinates of `D` are independent and each has a cap-one density. Integration in the original independent residual left coordinates produces scalar Fourier factors

`prod_i |psi_i(2t <a_i,D>)|`,                           (1.5)

while the mollifier gives a probability kernel in the variable `P D`. Here `a_i` is row `i` of the residual cross block `A[I_0,J]`.

Decompose every residual row as

`a_i=c_i+lambda_i P`,

where `c_i` is orthogonal to the row space of `P`; the rows `c_i` are precisely the rows of `C`. The `lambda_i P D` term is only a shift once the kernel variable `P D` is fixed.

Use weighted Holder with the subset weights `w_T`. Since

`prod_i q_i = prod_T (prod_(i in T) q_i^(1/alpha_i))^(w_T)`,

each Holder factor involves exactly one `ell`-subset `T`. The linear map

`D -> (P D, (<c_i,D>)_(i in T))`

has Gram determinant

`S^2 det(C_T C_T^T)`.

After normalizing its rows, the audited product-projection lemma bounds its density by

`e^(d/2) / [S sqrt(det(C_T C_T^T))]`.                 (1.6)

Since `alpha_i<=1/2`, the audited scalar Fourier-power estimate at `p=1/alpha_i>=2` gives, uniformly in all shifts,

`int |psi_i(2t(y+u))|^(1/alpha_i) dy
 <= pi sqrt(2e alpha_i)/|t|`.                          (1.7)

Therefore the `T`-factor is at most

`e^(d/2) [pi sqrt(2e)/|t|]^ell
 prod_(i in T) sqrt(alpha_i)
 / [S sqrt(det(C_T C_T^T))]`.                          (1.8)

Taking the `w_T` geometric mean, the determinant factors are exactly

`E_ell(C)^(-1/2) exp(H(w)/2)`,

and the marginal factors are

`exp((1/2) sum_i alpha_i log alpha_i)`.

To bound their product, sample `T~w` and then order its `ell` elements uniformly. The entropy of the ordered tuple is `H(w)+log(ell!)`. Each position has distribution `alpha_i/ell`, so entropy subadditivity yields

`H(w)+sum_i alpha_i log alpha_i
 <= ell log ell - log(ell!)`.                           (1.9)

Combining (1.4), (1.8), and (1.9), and passing through the harmless approximate-identity limit, gives (1.1). For `d>2`,

`int_R min(1,K |t|^(-d/2)) dt
 = [2d/(d-2)] K^(2/d)`.

Fourier inversion cancels the remaining factor of `pi` and gives (1.2). No probability squaring is used in the final small-ball conclusion; arbitrary same-bank curvature remains inside the complex pushforward throughout. QED.

### Exact-rank terminal form

If `r` promoted physical rows cross the opposite product bank through a rank-`r` matrix `P` and no residual projected row is needed, the same complex-pushforward/Plancherel argument gives

`|phi_Q(t)| <= min(1,
 pi^(r/2)e^(r/4) [det(PP^T)]^(-1/4)|t|^(-r/2)).`       (1.10)

Hence

`r=3: ||p_Q||_infinity <= 3 sqrt(e) [det(PP^T)]^(-1/6)`,

and the audited Riesz formula gives

`r=2: sup_a E|Q-a|^(-1/2)
 <=4 sqrt(2)e^(1/4)[det(PP^T)]^(-1/8).`                (1.11)

## 2. Any third crossing volume gives a density

Let `M` be an arbitrary literal physical cross block and

`Z=E_3(M)>0`.

For row `i`, let `J_i` be the sum of all three-row Gram determinants containing `i`. Then `sum_i J_i=3Z`.

If every `J_i/Z<=1/2`, apply (1.2) with `(k,ell,d)=(0,3,3)`. This gives

`||p_Q||_infinity <= C_3 Z^(-1/6)`,

where

`C_3=3 sqrt(2)e(9/2)^(1/6)=14.818337662843...`.        (2.1)

Suppose instead `J_i>Z/2` for some row `w=m_i`. Promote that **physical** row and project every other row orthogonally off `w`, obtaining residual rows `C`. Gram--Schmidt gives the exact identity

`J_i=||w||^2 E_2(C)`.                                  (2.2)

If the canonical `E_2(C)` row marginals are all at most `1/2`, apply (1.2) with `(k,ell,d)=(1,2,3)`; the currency is exactly the product in (2.2), so the result is `<10.958 Z^(-1/6)`.

If a residual physical row is heavy, promote it too. Let `P_2` be the two promoted rows and let `C_2` be all remaining rows after orthogonal projection off their span. A second Gram--Schmidt identity gives

`H_ij:=det(P_2P_2^T) ||C_2||_F^2 > J_i/2 > Z/4`.       (2.3)

If all one-volume residual marginals are at most `1/2`, (1.2) at `(k,ell,d)=(2,1,3)` gives `<8.264 Z^(-1/6)`.

Otherwise one residual row carries more than half of `||C_2||_F^2`; promote it. The Gram determinant of the resulting three physical rows satisfies

`det(P_3P_3^T)>H_ij/2>Z/8`.                             (2.4)

The exact-rank `r=3` bound (1.11) then gives `<7 Z^(-1/6)`.

All branches are therefore dominated by (2.1):

`boxed: ||p_Q||_infinity <= C_3 E_3(M)^(-1/6),
        C_3<14.819.`                                    (2.5)

This conclusion retains all same-bank phases and arbitrary affine terms.

## 3. Any second crossing volume gives a full half potential

Let `Z=E_2(M)>0` for a literal cross block. If all canonical row marginals are at most `1/2`, (1.1) with `(k,ell,d)=(0,2,2)` gives

`|phi_Q(t)| <= min(1,
 pi e 2^(3/4) Z^(-1/4)|t|^(-1)).`                      (3.1)

The audited Riesz estimate and the exact integral

`int_R |t|^(-1/2) min(1,L/|t|) dt = 8 sqrt(L)`          (3.2)

give

`sup_a E|Q-a|^(-1/2) <= C_2 Z^(-1/8)`,

where

`C_2=8 sqrt(e) 2^(-1/8)=12.095072570796...`.            (3.3)

If one row is heavy, promote it and project the remainder. Its incident two-volume is

`K_i=||w||^2 ||C||_F^2 > Z/2`.                          (3.4)

If the residual one-volume marginals are all at most one half, apply (1.1) with `(k,ell,d)=(1,1,2)` and (3.2); the resulting bound is `<9.79 Z^(-1/8)`. Otherwise a second promoted physical row has Gram determinant

`det(P_2P_2^T)>K_i/2>Z/4`,                              (3.5)

and the exact-rank-two bound (1.11) gives `<8.64 Z^(-1/8)`. Hence in every branch

`boxed: sup_a E|Q-a|^(-1/2) <= C_2 E_2(M)^(-1/8),
        C_2<12.096.`                                    (3.6)

This is a full fractional-potential estimate, not a rank-two density claim.

## 4. Complete normalized `s_9` proof

Assume `K=s=1` and `s_9(A)>=1`.

### No coordinate pivot

The audited baseline spectral-to-volume proposition at order `k=3` gives

`V_3(A)>=kappa^3`.

The fair original-coordinate cut supplies a literal cross block `M` with

`E_3(M)>=4^(-3)kappa^3`,

so

`E_3(M)^(-1/6)<=2 kappa^(-1/2)=160`.

By (2.5),

`||p_Q||_infinity <=160 C_3
 =2370.93402605488... <2400`.                            (4.1)

### Scalar pivot

Suppose `|A_hh|>=eta`. Completing the square in the original coordinate `X_h` leaves a Schur complement `S` with at least eight eigenvalues of modulus at least one.

If `S` has an `eta`-pivot, the audited baseline pivot proposition needs only two surviving large eigenvalues and gives truncated half potential `<=600`; the tail outside distance one contributes at most one. Thus the full Schur half potential is `<=601`.

If `S` has no `eta`-pivot, then certainly `s_5(S)>=1`. Apply the audited baseline structural proposition at `k=2` and the fair cut:

`E_2(M_S)>=4^(-2)kappa^2`.

Using (3.6),

`sup_a E|R-a|^(-1/2)
 <= C_2 (4^(-2)kappa^2)^(-1/8)
 = C_2 sqrt(160)
 =152.99191115498... <153`.                              (4.2)

Hence in either subcase the full Schur half potential is at most `601`. The audited scalar-square profile gives

`||p_Q||_infinity <= eta^(-1/2)*601 = 6010`.             (4.3)

### Two-coordinate pivot

If no scalar pivot was chosen but a definite principal pair has determinant magnitude at least `eta`, the audited definite-pair lemma gives

`||p_Q||_infinity <= pi/sqrt(eta)=10pi<32`.              (4.4)

If the pair is indefinite, its Schur complement retains at least seven eigenvalues of modulus at least one, hence operator norm at least one. The audited hyperbolic-envelope plus quarter-power logarithmic-potential argument therefore applies verbatim and gives

`||p_Q||_infinity<251`.                                  (4.5)

These alternatives exhaust the normalized problem, and the largest bound is (4.3). Thus

`||p_Q||_infinity<=6010` whenever `s_9(A)>=1`.            (4.6)

## 5. Scaling

For general density cap `K` and spectral scale `s`, put `Y=KX` and

`Qtilde=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c`.

The coordinates of `Y` have densities bounded by one, `s_9(A/s)>=1`, and

`Q=(s/K^2)Qtilde`.

Therefore

`boxed: ||p_Q||_infinity <= 6010 K^2/s.`

This completes the threshold-nine replacement proof.

## 6. Dependency map and lower-threshold boundary

`baseline Fourier/Riesz + product projection + scalar Fourier powers`
` -> grouped hub-light compiler (Section 1)`
` -> marginal-free E_3 density and E_2 half-potential receivers (Sections 2–3)`
` -> baseline V_3/V_2 structural forcing + random cut`
` -> no-pivot and scalar-pivot branches`
` + baseline definite/indefinite pair branches`
` -> s_9 theorem`
` -> scaling K^2/s`.

The B09 rank audit shows why the old `4r+1` bookkeeping cannot simply be changed by one at the terminal seed, and exact rank-sharp symmetric examples rule out naive `3r -> 2r` or `r -> r-1` improvements. Current repository work further localizes `s_8` to a no-pivot overlap-one/two-sided near-singular collar. I found no complete uniform receiver for that collar in this run, so I make **no `s_8` theorem claim**.

The unrestricted three-eigenvalue conjecture remains OPEN.
