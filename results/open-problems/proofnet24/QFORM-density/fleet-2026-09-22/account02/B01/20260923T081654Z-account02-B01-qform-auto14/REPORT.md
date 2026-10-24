# account02/B01 auto14 — weighted-Fourier spending of a source-disjoint off-diagonal packet

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Oscillatory replacement / complementary constructions and source-valid counterexamples  
Run: `20260923T081654Z-account02-B01-qform-auto14`  
Status: **NEW SUPPORTING ANALYTIC RECEIVER + PAID TARGET FAMILIES / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and correction boundary

The full conjecture remains open. The target is: for every dimension, every collection of independent real random variables with probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal essential bound for the density of `Q=X^TAX`, or give a valid counterexample.

No moment, Gaussian, log-concavity, compact-support, connected-support, diagonal-basis, or post-rotation independence hypothesis is added below. The phase-aligned fragmented-support construction still refutes every law-uniform positive-power **scalar pointwise** quadratic-phase decay estimate. The proof here instead combines two product-preserving averaged-frequency estimates in disjoint original-coordinate banks.

The early checkpoint for this run is commit `68f59d83eaa14f5118d7383ec25764dfcc44681f`, same directory, `CHECKPOINT.md`.

## 2. Source-valid inputs

### 2.1 Global off-diagonal sub-half-Riesz predecessor

The immediately relevant B01 predecessor is

`yspennstate/math-open-problems@5a4923fcec8db7b5f5b7a14e5762c3291b02d299`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260923T060557Z-account02-B01-qform-auto11/REPORT.md`.

It proves, for

`S=X^T C X+b^T X+c`, `F(C)=sum_(i!=j) C_ij^2`,

and every `0<beta<1/2`,

`H_beta(S)<=C_beta F(C)^(-beta/2)`.

Its proof is a fair-cut dichotomy: an order-one determinant/Brascamp--Lieb Fourier envelope in the diffuse-row case, and aggregate random-slope Plancherel in the heavy-row case. The present run returns to those **pre-Riesz absolute Fourier envelopes** and spends them directly.

The underlying mixed-order envelope is source-pinned at

`yspennstate/math-open-problems@21cf221fb1e8b99c99298fb11a0d5a41a8382aba`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B01/20260923T054511Z-account01-B01-qform-auto11b/REPORT.md`.

### 2.2 Rank-two two-bank Plancherel envelope

The newest completed designated partner is

`yspennstate/math-open-problems@e8c8cc633f1fe33ec6b568f80c5c7f68a105a159`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260923T073210Z-auto11/REPORT.md`.

For disjoint original-coordinate banks `I,J`, an exact rank-two physical cross matrix `K` with nonzero singular values `kappa_1,kappa_2`, and arbitrary same-bank measurable phases on both sides, its two-dimensional projection/Plancherel calculation proves uniformly in all affine shifts

`|psi(t)| <= min(1, 2 pi/(|t| sqrt(kappa_1 kappa_2))).`             (2.1)

This `1/|t|` is not asserted to be integrable by itself.

### 2.3 Required newest Claude/Fourier package

The required source directory was read at its pinned root `e5f71d79eff325201dd0274053d20268ce65b837` and at the compatible current master state observed in this run, `ea74e48ffbe5b01fae3d7331bed439c526f0879d`:

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

Its Theorem D is applied quantitatively in Section 7 below. The source explicitly preserves the pointwise-decay correction and keeps the unrestricted conjecture open.

## 3. New absolute weighted-Fourier theorem

### Theorem 3.1 — `QFORM-GLOBAL-OFFDIAG-WEIGHTED-FOURIER-v1`

Let `C=C^T`, let the physical coordinates be independent with densities at most one, and allow an arbitrary affine term:

`S=X^T C X+b^T X+c`.

Put

`F=F(C)=sum_(i!=j) C_ij^2`.

If `F>0`, then for every `0<beta<1/2`,

`W_beta(S):=integral_R |t|^(beta-1)|phi_S(t)| dt`

satisfies

`boxed: W_beta(S) <= K_beta F^(-beta/2),`                           (3.1)

where

`K_beta = 2 exp(beta/2)(4 pi)^beta/[beta(1-2 beta)].`              (3.2)

This is strictly prior to the Riesz transform: no `Gamma(beta)` or cosine denominator is paid.

### Proof

Take a fair independent two-colouring of the physical coordinates and let `M=C[I,J]`. With the ordered convention in `F`,

`E ||M||_F^2=F/4`,

so some cut has

`E_1:=||M||_F^2>=F/4`.                                              (3.3)

Use the natural order-one edge law `omega(i,j)=M_ij^2/E_1`.

**Diffuse-row branch.** If every row marginal is at most `1/2`, the completed mixed-order determinant/BL envelope with mean order one gives

`|phi_S(t)|<=min(1,B_D |t|^-1/2)`,

`B_D=exp(1/4)(2 pi)^(1/2) E_1^-1/4`.                              (3.4)

**Heavy-row branch.** If some row marginal exceeds `1/2`, its Euclidean norm `rho` satisfies `rho^2>E_1/2`. Conditioning all other coordinates on its side, the completed random-slope Plancherel theorem gives

`|phi_S(t)|<=min(1,B_H |t|^-1/2)`,

`B_H=sqrt(pi C_1/rho)`, `C_1<=sqrt(2)`.                            (3.5)

Both estimates retain arbitrary same-bank quadratic phases and arbitrary affine shifts.

For any `B>0` and `0<beta<1/2`, splitting at `t=B^2` gives the exact identity

`integral_R |t|^(beta-1) min(1,B|t|^-1/2) dt`

`=2 B^(2beta)/[beta(1-2beta)].`                                   (3.6)

In the diffuse branch, (3.4), (3.6), and `E_1>=F/4` give exactly (3.1)-(3.2). In the heavy branch, `rho^2>E_1/2`, `C_1<=sqrt(2)`, and (3.3) give the same bound without the harmless factor `exp(beta/2)`, hence the diffuse constant dominates. QED.

The exclusion of `beta=1/2` is genuine: the high-frequency integral in (3.6) becomes logarithmic at the endpoint.

## 4. New receiver: rank-two bicore plus an arbitrary source-disjoint off-diagonal quadratic packet

### Theorem 4.1 — `QFORM-RANK2-CROSS-PLUS-OFFDIAG-PACKET-v1`

Partition the original independent coordinates into disjoint banks `I,J,D,W`. Assume there are no quadratic cross terms between `D` and `I union J`; all couplings to `W` are arbitrary. Let

`K=A[I,J]`

have exact rank two with nonzero singular values `kappa_1,kappa_2`, and put

`Delta=kappa_1 kappa_2>0`.

Let `C=A[D,D]` and assume

`F_D:=sum_(r!=s in D) C_rs^2>0`.

The self blocks on `I` and `J` are completely arbitrary; the self block `C` on `D` is completely arbitrary; `A[W,W]` and every `W` coupling are arbitrary. Then `Q=X^TAX` has a continuous `C_0` density and, for every `0<beta<1/2`,

`boxed: ||p_Q||_infinity`

`<= D_beta Delta^(-1/[2(1+beta)]) F_D^(-beta/[2(1+beta)]),`       (4.1)

where

`D_beta=(1+beta)/(pi beta)`
`       * [2 pi exp(beta/2)(4 pi)^beta/(1-2beta)]^(1/(1+beta)).`   (4.2)

At `beta=1/4`,

`D_(1/4)=22.103418361512958...`, and therefore

`boxed: ||p_Q||_infinity`
`       <=22.104 Delta^(-2/5) F_D^(-1/10).`                        (4.3)

### Proof

Condition on `X_W=w`. All `W` couplings become affine shifts. Because there are no `I/J-D` quadratic cross terms, the conditional form splits into independent active pieces

`Q|w = R_w(X_I,X_J)+S_w(X_D)+c(w)`,

where

`R_w=F_w(X_I)+G_w(X_J)+2 X_I^T K X_J`

with arbitrary same-bank phases, and `S_w` has fixed quadratic part `C` and an arbitrary `w`-dependent affine term.

By the two-bank Plancherel envelope (2.1), uniformly in `w`,

`|phi_{R_w}(t)|<=min(1,A/|t|)`,

`A=2 pi Delta^-1/2`.                                               (4.4)

By Theorem 3.1, uniformly in `w`,

`integral_R |t|^(beta-1)|phi_{S_w}(t)| dt`
`<=K_beta F_D^(-beta/2).`                                         (4.5)

For any `T>0`, triangle inequality and Tonelli give

`||phi_Q||_1`
`<=2T + A T^-beta K_beta F_D^(-beta/2).`                           (4.6)

Indeed, for `|t|>T`, `|t|^-1<=T^-beta |t|^(beta-1)`. No pointwise decay of the `D` packet is used.

Let

`B=A K_beta F_D^(-beta/2)`.

The exact minimizer of `2T+B T^-beta` is

`T=(beta B/2)^(1/(1+beta))`,

and the minimum is

`2(1+beta)T/beta`.                                                 (4.7)

Fourier inversion gives `||p_Q||_infinity<=(2pi)^-1||phi_Q||_1`; substituting (3.2), (4.4), and (4.7) gives (4.1)-(4.2). Since `phi_Q in L^1`, the density has a continuous representative vanishing at infinity. QED.

**Scaling check.** `Delta` has matrix scale two and `F_D` has matrix scale two. The exponents in (4.1) total

`-1/(1+beta)-beta/(1+beta)=-1`,

as required for a density bound.

## 5. A third spectral packet can be spent without extracting a square

### Corollary 5.1 — source-disjoint spectral-packet receiver

In Theorem 4.1, suppose the symmetric packet `C` has at least one eigenvalue of modulus at least `s>0` and

`max_(r in D)|C_rr|<=delta<s`.

Then

`F_D=||C-diag C||_F^2>=(s-delta)^2`.                               (5.1)

Indeed, Mirsky's singular-value inequality gives

`||C-diag C||_F^2 >= sum_j (s_j(C)-s_j(diag C))^2`,

and the first term alone is at least `(s-delta)^2`.

Thus at `beta=1/4`,

`boxed: ||p_Q||_infinity`
`<=22.104 Delta^-2/5 (s-delta)^-1/5.`                              (5.2)

In particular, if `Delta>=1`, `s>=1`, and `delta<=1/2`, then

`boxed: ||p_Q||_infinity <25.391.`                                (5.3)

This is the promised spend of the global sub-half-Riesz currency: the third source-disjoint packet need not be a scalar square, rank one, semidefinite, or have a bounded density of its own. It only needs aggregate off-diagonal energy, and a disjoint large spectral direction plus small packet diagonals supplies that energy automatically.

## 6. Concrete obstruction/construction: two singular curved rank-two packets smooth each other

For each integer `m>=1`, take eight mutually independent size-`m` original-coordinate banks. For `r=1,2`, let

`A_r,B_r,C_r,D_r`

be the normalized sums `m^-1/2` times the coordinates in their respective banks, and define

`T_r=(A_r+C_r)^2-(B_r-D_r)^2`,

`Q_m=T_1+T_2`.                                                     (6.1)

Each coefficient block of `T_r` is `u_+u_+^T-u_-u_-^T`, with `||u_+||^2=||u_-||^2=2` and `u_+ perp u_-`. Hence

`spec(T_r coefficient)={2,-2,0,...,0}`,

and therefore

`spec(Q_m coefficient)={2,-2,2,-2,0,...,0}`.                      (6.2)

So every `Q_m` satisfies the exact QFORM spectral hypothesis.

Every physical diagonal has magnitude `1/m`. Every physical off-diagonal entry has magnitude either `0` or `1/m`; direct rank-one inspection shows every physical `2x2` principal determinant has magnitude at most `1/m^2`. Thus for every fixed no-pivot threshold `tau>0`, the family lies in strict N3 once `m>1/tau`.

Treat `T_1` as the active bicore with

`I=A_1 union B_1`, `J=C_1 union D_1`.

Its cross matrix has singular values `1,1`, so `Delta=1`; the same-bank curvatures `A_1^2-B_1^2` and `C_1^2-D_1^2` are retained exactly. Treat `T_2` as the source-disjoint packet. Its coefficient matrix has Frobenius norm squared `8`, while the squared diagonal norm is `4/m`, hence

`F_D=8-4/m>=4`.                                                    (6.3)

Theorem 4.1 at `beta=1/4` gives the uniform target-level bound

`boxed: ||p_{Q_m}||_infinity`
`<=22.1034183616 (8-4/m)^(-1/10)`
`<19.243.`                                                        (6.4)

This holds for every admissible cap-one product law and every `m`.

There is a useful endpoint phenomenon at `m=1`. If all eight scalar inputs are iid `Uniform[-1/2,1/2]`, then each individual `T_r` has **unbounded** density at zero. Indeed `A_r+C_r` and `B_r-D_r` have triangular density `g(z)=1-|z|` on `[-1,1]`, so their squares have density

`h(w)=w^-1/2-1`, `0<w<1`.

Hence the density of `T_r=W_1-W_2` at zero is

`p_{T_r}(0)=integral_0^1 h(w)^2 dw=infinity`.                     (6.5)

Nevertheless the independent sum `T_1+T_2` has the universal bounded continuous density (6.4). Thus neither summand need have bounded density; the gain is genuinely an **integrated-frequency interaction** between a borderline `1/|t|` bicore and a sub-half weighted Fourier packet.

This is not a counterexample to QFORM; it is a counterexample to the tempting intermediate requirement that the third source-disjoint packet itself first have a bounded density.

## 7. Required newest Claude result applied to the same family

For the cut

`I_0=A_1 union B_1 union A_2 union B_2`,
`J_0=C_1 union D_1 union C_2 union D_2`,

the physical cross matrix is the orthogonal direct sum of four rank-one modes, so its four nonzero singular values are all one. Therefore

`Z=e_3(M^T M)=4`.                                                  (7.1)

For the natural order-three volume law, a given singular mode is selected with probability `3/4`; inside that mode every one of its `m` physical rows has equal squared weight `1/m`. Hence every `I_0` row marginal is

`alpha_i=3/(4m)`.                                                  (7.2)

For `m>=2`, `alpha_i<=1/2`, so Theorem D from the required `20260922T211500Z-decoupling-brascamp-lieb` source applies **at an actual inequality**:

`boxed: ||p_{Q_m}||_infinity`
`<=6 sqrt(e) 4^(-1/6)`
`=7.8515456385... .`                                              (7.3)

At `m=1`, the natural marginals are exactly `3/4`: the original Theorem-D gate fails, its D' extension requires `h<3/4`, and `D_5` vanishes because the cross rank is four. The new weighted-Fourier receiver still gives (6.4). This endpoint comparison is not a claim that all other paid branches fail there; it records a concrete complementary range of the new mechanism.

## 8. Newest designated partner result applied and compared

The completed account03/B01 theorem `QFORM-RANK2-CROSS-PLUS-SQUARE-L3-v1` gives, for a source-disjoint scalar square,

`||p_Q||_infinity`
`<9.927 Delta^(-3/8)(|lambda| sigma^2)^(-1/4).`                    (8.1)

Apply it to the target-valid family

`Q_m^sq=T_1+E^2`,

where `E` is a normalized sum on a ninth independent size-`m` bank. The bicore has `Delta=1`, while the square has `lambda=1` and projection-vector norm `sigma=1`. Its coefficient matrix has nonzero spectrum `{2,-2,1}`, so it satisfies the exact target, and for large `m` it is again strict N3. The partner theorem gives

`boxed: ||p_{Q_m^sq}||_infinity<9.927.`                           (8.2)

This comparison is exactly complementary. The partner square theorem covers `F_D=0`, where Theorem 4.1 has no currency; Theorem 4.1 covers arbitrary off-diagonal quadratic packets, including packets with singular output densities, without extracting any scalar square.

## 9. What changed in the proof map

The previous unpaid analytic obligation was `QFORM-GLOBAL-SUBHALF-RIESZ-SPEND-v1`: a global `H_beta`, `beta<1/2`, was available in strict N3, but the endpoint `beta=1/2` diverged and did not itself imply bounded density.

The present run pays a substantial source-disjoint version of that obligation. The correct object to spend is not only `H_beta`; it is the stronger pre-Riesz absolute weighted Fourier moment (3.1). A two-bank rank-two bicore supplies the missing `1/|t|` factor. Their product is integrable after the elementary frequency split (4.6).

The first unpaid structural implication is now

`QFORM-WEIGHTED-FOURIER-OVERLAP-ROUTING-v1`:

> In an arbitrary remaining strict-N3 state, route the global off-diagonal weighted-Fourier currency to either (i) a quantitatively nondegenerate **source-disjoint** rank-two bicore as in Theorem 4.1, (ii) the designated partner's source-disjoint square receiver, (iii) the overlapping transverse Fresnel receiver from the immediately preceding B01 run, or (iv) another already-paid volume/hub/ridge/pair/grouped-square/exact-null branch, before paying a reciprocal tiny local determinant. The genuinely unpaid configuration is where every candidate third currency substantially overlaps both active cross banks and no existing augmented-frame transversality gate is quantitative.

This is structural/exhaustive debt, not another attempt to pass `beta` to `1/2`. Full QFORM is **not proved or disproved**, and there is no full candidate with two independent end-to-end reviews.
