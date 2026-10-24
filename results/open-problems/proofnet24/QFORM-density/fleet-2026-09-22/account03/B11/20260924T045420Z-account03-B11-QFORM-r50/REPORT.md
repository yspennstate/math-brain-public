SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B11, 2026-09-24T04:54:20Z.
attacking: the punctured same-source near-coloop collar by combining the exact Schur pseudodeterminant blow-up with a chirped shared-hub/rank-two transverse Fourier receiver, retaining the nonzero pivot exactly.

# account03/B11 r50 — chirped shared-hub rank-two transverse receiver and exact puncture-volume identity

Programme: `QFORM-DENSITY-3EIG-20260922`.
Assignment: indefinite signatures `(2,1)` and `(1,2)`.
Status: **NEW ANALYTIC RECEIVER / NEW EXACT SCHUR-PUNCTURE VOLUME IDENTITY / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**.
Execution: **WITHOUT_VERIFIED_BRAIN**.
Continuity: the new receiver gives a continuous `C_0` density in its stated scope; full-target continuity remains open.

The unrestricted owner conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. This report does not use Gaussianity, log-concavity, moments, compact or connected support, post-rotation independence, law-uniform pointwise van-der-Corput decay, arbitrary-joint coarea, conditional-cap-as-independence, deletion of a small nonzero coefficient, or a numerical histogram as proof.

The immediate predecessor is account03/B11 r49, `yspennstate/math-open-problems@506a01e6b5026fd7f703ad5b7f2e6ad08b9277c3`, which proves that the nonlinear exact-cancellation law from r48 has infinite all-direction X-ray norm and therefore cannot be the orthogonal product projection occurring in the true hard chamber. The present run changes mechanism: rather than trying to promote X-ray control alone, it keeps the original source banks and proves a direct `L^2 -> L^2` Fourier operator estimate.

The newest designated account04/B11 input is `QFORM-SPECTRAL-SCHUR-PSEUDODET-v1`, canonical report `yspennstate/math-open-problems@28cbe14c4381d5f1b58145b29bbcc160b4d2ea5c`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B11/20260924T041708Z-account04-B11-schur-pseudodet-r1/REPORT.md`. For exact rank three, a nonzero physical pivot `a=A_hh`, hub leverage `q_h`, and Schur complement `S`, it proves

`Delta_2(S)=q_h Delta_3(A)/|a|`, hence `|a| Delta_2(S)=q_h Delta_3(A)`.

That identity is applied below to an actual density inequality.

## 1. General product-preserving analytic receiver

Let `H`, `X_L`, and `X_R` be mutually independent source banks. The scalar `H` is a literal ORIGINAL coordinate. The coordinates within `X_L` and within `X_R` are independent and have scalar densities at most one; no projected coordinates inside a bank are asserted independent.

After conditioning on any outside ORIGINAL coordinates, write

`Q = a H^2 + 2 H(c^T X_L + r^T X_R) + F_L(X_L) + F_R(X_R) + 2 X_L^T A_LR X_R`,  (1.1)

where `a != 0`, `c != 0`, `r != 0`, and `F_L,F_R` are arbitrary real quadratic-affine phases on their own banks. Any conditioned affine term in `H` is also allowed.

Put `alpha=||c||`, `beta=||r||`, `e=c/alpha`, `f=r/beta`, and define the physical Schur cross

`N = A_LR - c r^T/a`.                                      (1.2)

Assume `rank N <= 2`. Suppose there are orthonormal pairs `v_1,v_2` in `e^perp` and `z_1,z_2` in `f^perp` such that all of `N` is carried by the three-dimensional source projections

`(u,x_1,x_2)=(e^T X_L, v_1^T X_L, v_2^T X_L)`,
`(v,y_1,y_2)=(f^T X_R, z_1^T X_R, z_2^T X_R)`,              (1.3)

and the transverse `2 x 2` block `B=(v_i^T N z_j)` is invertible. Let

`D_perp = |det B| > 0`.                                     (1.4)

Let the ordinary three-dimensional projection densities in (1.3) have caps `M_L,M_R`. The weighted affine-fiber Brascamp--Lieb theorem already proved in the fleet gives `M_L,M_R <= e^(3/2)` for genuine orthonormal projections of cap-one product banks.

### Theorem 1.1 — `QFORM-CHIRPED-HUB-RANK2-TRANSVERSE-L1-v1`

Under (1.1)--(1.4), the law of `Q` has a continuous `C_0` density and

`|phi_Q(t)| <= min{1, pi^(3/2) sqrt(M_L M_R) sqrt(|a|/(alpha beta D_perp)) |t|^(-3/2)}`,  (1.5)

and hence

`boxed: ||p_Q||_infinity <= 3 (M_L M_R)^(1/3) (|a|/(alpha beta D_perp))^(1/3).`  (1.6)

For genuine cap-one product banks, `M_L,M_R<=e^(3/2)` and therefore

`boxed: ||p_Q||_infinity <= 3 e (|a|/(alpha beta D_perp))^(1/3).`      (1.7)

The theorem is sign-free in `a` and in the Schur two-plane, so it applies equally to signatures `(2,1)` and `(1,2)`.

### Proof

In the coordinates (1.3), write the `3 x 3` matrix of `N` as

`N_3 = [[n00,p^T],[q,B]]`.                                  (1.8)

Because `rank N_3<=2` and `B` is invertible,

`n00 = p^T B^(-1) q`.                                       (1.9)

Make determinant-one shears inside the two independent source banks,

`x' = x + B^(-T) p u`,
`y' = y + B^(-1) q v`.                                      (1.10)

They leave the star scalars `u,v` unchanged and have Jacobian one. Equation (1.9) gives the exact identity

`[u,x]^T N_3 [v,y] = (x')^T B y'`.                          (1.11)

Thus the entire Schur cross is converted into a rank-two transverse bilinear form without discarding any coefficient. Every same-bank term produced by (1.10) remains inside `F_L` or `F_R` and only changes a unit-modulus bank phase.

The ORIGINAL crossing is `A_LR=N+c r^T/a`. Hence the hub/cross terms become

`a H^2 +2H(alpha u+beta v)+2 alpha beta uv/a+2(x')^T B y'`. (1.12)

Put `s=alpha u+beta v`. Since

`2 alpha beta uv/a = s^2/a-alpha^2u^2/a-beta^2v^2/a`,        (1.13)

the separated squares are absorbed into the bank phases. If `gamma H` is the conditioned hub-linear term, the scalar-hub kernel is

`J_t(s)=exp(i t s^2/a) int f_H(h) exp(i t[a h^2+2hs+gamma h]) dh`. (1.14)

This retains the nonzero pivot exactly.

With angular Fourier transform `hat J(xi)=int J(s)e^(-i xi s)ds`, the Fresnel integral gives

`hat J_t(xi)=omega(t,a) sqrt(pi |a|/|t|) exp(-i a xi^2/(4t)) phi_H(a xi+t gamma)`,  (1.15)

where `|omega|=1`. Consequently

`||hat J_t||_infinity <= sqrt(pi |a|/|t|)`.                  (1.16)

No pointwise quadratic-phase decay is used; only `|phi_H|<=1`.

The star operator `(T_*g)(u)=int J_t(alpha u+beta v)g(v)dv` therefore satisfies

`||T_*||_(2->2) <= sqrt(pi |a|/(|t| alpha beta))`.           (1.17)

The transverse two-dimensional bilinear Fourier operator

`(T_Bg)(x)=int exp(i2t x^T B y)g(y)dy`                       (1.18)

has exact norm

`||T_B||_(2->2)=pi/(|t| sqrt(D_perp))`.                      (1.19)

Push the phase-twisted source measures on the two banks to the three displayed coordinates. Their complex densities satisfy `|g_{L,t}|<=p_L`, `|g_{R,t}|<=p_R`, hence

`||g_{L,t}||_2<=sqrt(M_L)`, `||g_{R,t}||_2<=sqrt(M_R)`.      (1.20)

Combining (1.17)--(1.20) yields (1.5). If

`K=pi^(3/2) sqrt(M_LM_R) sqrt(|a|/(alpha beta D_perp))`,     (1.21)

then exactly

`int_R min(1,K|t|^(-3/2))dt=6K^(2/3)`.                      (1.22)

Fourier inversion gives (1.6), and `phi_Q in L^1` gives the continuous `C_0` representative. QED.

The mechanism is explicit: the nonzero hub square plus its forced aligned Schur crossing supplies one half-power `|t|^(-1/2)` through the chirped transform; the two transverse Schur directions supply `|t|^(-1)`. Their product is the integrable `|t|^(-3/2)`.

## 2. Exact puncture geometry of a nonzero physical pivot

Now let `A` have exact rank three, with its three nonzero eigenvalue magnitudes at least `s>0`. Fix a literal coordinate `h` with

`a=A_hh!=0`, `q=q_h=||P_(Ran A)e_h||^2 in (0,1)`.             (2.1)

Write

`A=[[a,l^T],[l,C]]`, `S=C-l l^T/a`, `t=l/a`.                (2.2)

Then `S` has rank two. Write

`S=V Lambda V^T`, `V^T V=I_2`.                              (2.3)

Let `tau=||P_(Ran V)^perp t||`. Because `q<1`, `tau>0`; put

`p=P_(Ran V)^perp t/tau`, `R=[p,V]`, so `R^TR=I_3`, and write `t=tau p+Vb`. (2.4)

### Lemma 2.1 — leverage is exactly the puncture size

`boxed: q=1/(1+tau^2), tau^2=(1-q)/q.`                       (2.5)

Proof. The square-completion identity is

`Q_A(h,z)=a(h+t^Tz)^2+z^T S z`.                              (2.6)

Inside `span{e_h,p,V}`, the vector

`n=(-tau e_h+p)/sqrt(1+tau^2)`                               (2.7)

is an exact unit kernel vector. Every other kernel direction is residual and orthogonal to `e_h`. Hence

`q=1-|<e_h,n>|^2=1/(1+tau^2)`. QED.

## 3. Exact transverse Schur-volume identity

Partition all residual ORIGINAL coordinates into disjoint banks `I,J`. Put

`Gamma_I=R_I^T R_I`, `Gamma_J=R_J^T R_J=I_3-Gamma_I`,        (3.1)

and assume both are positive definite. Define

`c=l_I=a t_I`, `r=l_J=a t_J`, `alpha=||c||`, `beta=||r||`.   (3.2)

Let `P_c,P_r` project off these star directions. The Schur cross is

`N=S[I,J]=V_I Lambda V_J^T`.                                 (3.3)

### Theorem 3.1 — `QFORM-SCHUR-PUNCTURE-TRANSVERSE-VOLUME-v1`

The transverse cross `P_c N P_r` has rank two and its two-singular-value product is

`boxed: D_perp = Delta_2(S) |a|^2 tau^2 sqrt(det Gamma_I det Gamma_J)/(alpha beta).`  (3.4)

Equivalently,

`alpha beta D_perp = |a|^2 tau^2 Delta_2(S) sqrt(det Gamma_I det Gamma_J)`.  (3.5)

Using the designated account04/B11 Schur identity and Lemma 2.1,

`boxed: alpha beta D_perp = |a|(1-q)Delta_3(A) sqrt(det Gamma_I det Gamma_J).`  (3.6)

Thus the `1/|a|` Schur-curvature explosion exactly cancels the near-null pivot in the Fourier receiver. Only the true leverage defect `1-q` and physical bank-volume factor remain.

Proof. For one bank, Gram base-height gives

`alpha^2 det(V_I^T P_c V_I)=det([c,V_I]^T[c,V_I])`.          (3.7)

The columns `[c,V_I]` are obtained from `R_I=[p_I,V_I]` by a coefficient matrix of determinant `a tau`. Hence

`det(V_I^T P_c V_I)=|a|^2 tau^2 det Gamma_I/alpha^2`.        (3.8)

Likewise

`det(V_J^T P_r V_J)=|a|^2 tau^2 det Gamma_J/beta^2`.         (3.9)

For `P_c V_I Lambda V_J^T P_r`, the product of its two nonzero singular values equals

`|det Lambda| sqrt(det(V_I^T P_c V_I) det(V_J^T P_r V_J))`. (3.10)

Since `|det Lambda|=Delta_2(S)`, (3.4)--(3.5) follow. The designated partner theorem supplies

`|a|Delta_2(S)=qDelta_3(A)`,                                 (3.11)

and `tau^2=(1-q)/q`; substituting gives (3.6). QED.

This is the required actual application of the newest account04/B11 result.

## 4. Density corollary: the physical pivot cancels completely

Theorem 1.1 applies to the split `I|J`, because `S` has rank two and (3.4) is positive. Each displayed bank triple is an honest orthonormal projection of a disjoint ORIGINAL product bank. The weighted affine-fiber Brascamp--Lieb theorem gives

`M_I,M_J<=e^(3/2)`.                                          (4.1)

Insert (3.6) into (1.7):

### Corollary 4.1 — punctured two-bank density compiler

`boxed: ||p_Q||_infinity <= 3e[(1-q)Delta_3(A) sqrt(det Gamma_I det Gamma_J)]^(-1/3).`  (4.2)

The density is continuous and `C_0`. If all three nonzero eigenvalue magnitudes are at least `s`, then

`boxed: ||p_Q||_infinity <= (3e/s)[(1-q)sqrt(det Gamma_I det Gamma_J)]^(-1/3).`  (4.3)

There is **no factor of `|a|`**. Therefore the nonzero-pivot puncture is not intrinsically singular in the pivot size; the exact Schur two-volume blow-up pays it.

## 5. Diffuse residual frame: explicit MSS branch

The rows `r_j` of `R=[p,V]` form a Parseval frame. If

`delta=max_j ||r_j||^2`                                     (5.1)

and `g(delta)=1/2-delta-sqrt(2delta)>0`, the completed two-part MSS partition supplies `I,J` with

`Gamma_I>=g(delta)I_3`, `Gamma_J>=g(delta)I_3`.              (5.2)

Hence

`sqrt(det Gamma_I det Gamma_J)>=g(delta)^3`.                 (5.3)

Corollary 4.1 gives

`boxed: ||p_Q||_infinity <= [3e/g(delta)] [(1-q)Delta_3(A)]^(-1/3) <= [3e/g(delta)](1-q)^(-1/3)/s.` (5.4)

For `delta<=1/36`,

`g(1/36)=0.23651996182670637...`,
`3e/g(1/36)=34.47846609814707...`,                            (5.5)

so

`boxed: ||p_Q||_infinity <34.479(1-q)^(-1/3)/s.`             (5.6)

At the control value `1-q=1/64`, this is `<137.914/s`.

This is not a final ultracoloop bound because it diverges as `q->1`. Its structural value is that the small physical pivot has disappeared entirely: the first unpaid scalar is now the leverage defect `1-q`, not `|a|`.

## 6. Rank-two logarithmic control

For independent centered unit uniforms,

`p_(2XY)(z)=log(1/(2|z|)), 0<|z|<1/2`.                       (6.1)

That logarithm is the correct two-direction obstruction. In the present receiver, the literal hub plus forced aligned Schur crossing supply `|t|^(-1/2)`, while two transverse Schur directions supply `|t|^(-1)`, giving `|t|^(-3/2)`. The partner identity shows the transverse curvature grows exactly fast enough to neutralize a near-null nonzero hub pivot. Thus the rank-two logarithm cannot be blamed on pivot size in this branch.

## 7. Remaining implication

This run does **not** prove the full exact-rank-three theorem and does not address arbitrary additional nonseparable spectrum. The next B11 endpoint is

`QFORM-ULTRACOLOOP-RANK2-TO-RANK1-INTERPOLATION-v1`:

> in the same-source nonzero-pivot exact-rank-three collar, obtain a bound uniform as `q->1` by interpolating the present rank-two-transverse chirped receiver with the already-paid rank-one/low-residual-rank endpoint, without deleting the vanishing longitudinal puncture or conditioning on a projected variable.

After the MSS diffuse split, the only loss in (5.4) is `(1-q)^(-1/3)`. A successful successor must replace that reciprocal defect by a rank-one transverse currency that survives at `q=1`, or perform a product-preserving recut. The r49 X-ray theorem remains an exclusion of the exact nonlinear cancellation falsifier, but X-ray control alone is not promoted to a density theorem.

Arbitrary additional spectrum remains a separate bridge. Full-target continuity remains open.

## 8. Verification

`VERIFY.py` in this directory performs three deterministic checks:

1. 4,994 random rank-two `3 x 3` cross matrices with invertible transverse block verify `n00=p^T B^(-1)q` and the exact shear reduction; maximum observed absolute error `<1.2e-11`.
2. 5,000 random residual orthonormal three-frames and partitions verify (3.4); maximum observed relative error `<1.1e-11`.
3. 2,000 random exact-rank-three indefinite matrices verify the designated-partner Schur pseudodeterminant identity; maximum observed relative error `<1.3e-14`.

It also reproduces `g(1/36)=0.23651996182670637...`, `3e/g=34.47846609814707...`, and the `1-q=1/64` value `137.9138643925883...`. The computation is corroborative only; the arguments above are analytic.

## 9. Source/status pins

- Fresh owner control before publication: `yspennstate/math-research-brain/main`, OWNER CONTROL revision `2026-09-22.15`; QFORM only; no later stop/reassignment observed.
- Immediate B11 predecessor: `yspennstate/math-open-problems@506a01e6b5026fd7f703ad5b7f2e6ad08b9277c3`.
- Designated account04/B11 Schur identity: `yspennstate/math-open-problems@28cbe14c4381d5f1b58145b29bbcc160b4d2ea5c`.
- Product-projection Brascamp--Lieb cap `e^(k/2)`: `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`.
- MSS two-part frame bound: source-matched in the fleet, including account01/B08 r27.
- Live corrections retained: pointwise-decay false; arbitrary-joint coarea false; fiber-sup dimension loss; no independence after rotation; conditional-cap-not-independence; cross-minor-alone false; X-ray-only trace control false.

Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.
Full-target continuity: **OPEN**.
