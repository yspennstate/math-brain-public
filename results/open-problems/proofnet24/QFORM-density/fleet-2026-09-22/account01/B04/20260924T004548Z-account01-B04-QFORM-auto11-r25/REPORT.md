SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B04, 2026-09-24T00:45:48Z.
attacking: the small-pair overlap-two endpoint — splice the forced half-Riesz packet with genuine third curvature using product-space conditioning, and test whether a logarithmic/first-compound convolution yields a density bound without selecting a vanishing local coefficient.

# account01/B04 r25 — conditioned spectral-window exit for the overlap-two small-pair collar

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement  
Status: **NEW SUPPORTING THEOREM + TARGET-LEVEL SMALL-PAIR SUBBRANCH PAID / FULL TARGET OPEN**  
Regularity: the new spectral-window branch below has a **continuous `C_0` density**; the complementary coupling-heavy half-Riesz branch still does not by itself yield a bounded density.  
Independent review: pending.  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

No random coordinate is rotated. Every conditioning step fixes only original independent coordinates. No pointwise law-uniform quadratic-phase decay, arbitrary-joint coarea theorem, conditional-density-cap inheritance, moment assumption, compact support, Gaussianity, log-concavity, or perturbative deletion of a rough random remainder is used.

## 1. Fresh source boundary


The immediately preceding B04 run is

`yspennstate/math-open-problems@016b7981bb82bfc2847c47e42949708877c003d1`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B04/20260924T001509Z-account01-B04-QFORM-auto11-r24/REPORT.md`.

Its current overlap-two small-pair state has a physical pair `S={r,s}` with

`|A_rr|,|A_ss|<1/64`, `|A_rs|<1/32`, `J_2(S)>=1/144`,             (1.1)

and exact block notation

`A=[[B,W],[W^T,C]]`,                                                (1.2)

where `B=A[S,S]`, `W=A[S,S^c]`, `C=A[S^c,S^c]`. It proved the singular-safe identity

`J_2(S)=||off(det(B) C-W^T adj(B) W)||_F^2`.                       (1.3)

The fresh designated partner is account02/B04 r16,

`yspennstate/math-open-problems@779dc7079332af772c3445c0f58dbb5a59b504cf`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/20260924T001554Z-account02-B04-QFORM-auto11-r16/REPORT.md`.

Its completed diffuse-curvature argument combines physical residual paving with the marginal-free cross-`E_3` Fourier theorem. If `E=U Lambda U^T`, `rank E=r>=3`, `beta=max_i||u_i||^2`, `sigma=s_3(E)>0`, and `r beta<1`, the post-conditioning quadratic form is bounded by

`||p||_infinity <=2 C_* /[(1-sqrt(r beta)) sigma]`,                (1.4)

where

`C_*=8.4530212255281768747...`.                                    (1.5)

The proof explicitly permits arbitrary induced affine terms after conditioning original coordinates.

A second source used below is the one-scale ridge/spectral-window theorem

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`

`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

At unit scale, if a symmetric matrix has three eigenvalues of magnitude at least one and the spectral projection onto all eigenspaces with `|lambda|>=1/64` has diagonal at most `1/32`, its full quadratic form has a `C_0` density bounded by

`288 sqrt(3e)/13 <64`.                                             (1.6)

The proof is an integrated product-Fourier/ridge estimate; arbitrary affine terms are allowed.

## 2. New theorem: conditioning an arbitrary physical bank preserves the spectral-window exit

### Theorem `QFORM-CONDITIONED-SPECTRAL-WINDOW-EXIT-v1`

Let `[n]=H disjoint_union L` be a partition of the original independent coordinates and write

`A=[[A_HH,R],[R^T,C]]`.                                            (2.1)

Assume `C` has at least three eigenvalues of magnitude at least `s>0`. Let `P_s` be the spectral projection of `C` onto all eigenspaces with

`|lambda(C)|>=s/64`.                                               (2.2)

If

`max_(i in L) (P_s)_(ii) <=1/32`,                                 (2.3)

then for every independent cap-one product input law the **full ambient form**

`Q=X^T A X`                                                        (2.4)

has a continuous density vanishing at infinity and

`boxed:
 ||p_Q||_infinity
 <= [288 sqrt(3e)/(13 s)].}`                                      (2.5)

No condition is imposed on `A_HH` or on the cross block `R`.

### Proof

Condition on the original variables `X_H=h`. Product independence of `X_L` is unchanged. The conditional polynomial is

`Q_h=X_L^T C X_L + 2 h^T R X_L + c(h)`.                           (2.6)

Divide by `s` and apply the unit-scale spectral-window theorem to `C/s`. Its high spectral projection is exactly `P_s`; the induced term `(2/s)h^T R X_L+c(h)/s` is affine, hence inside the theorem's allowed coordinate-separable perturbations. Therefore, uniformly in `h`,

`||p_(Q_h)||_infinity <=288 sqrt(3e)/(13s)`.                       (2.7)

Averaging the conditional densities proves the same essential-supremum bound for `Q`.

For continuity, use the proof rather than only its endpoint norm: the ridge argument supplies an `L^1(dt)` characteristic-function majorant depending only on `C/s` and the fixed spectral-window constants, not on the affine vector generated by `h`. Thus

`|phi_Q(t)| <= E_h |phi_(Q_h)(t)| <= g_s(t)`                       (2.8)

for one `g_s in L^1(R)`. Fourier inversion gives a `C_0` density. QED.

The point is that rough couplings to conditioned coordinates cost **nothing**: they become affine phases, so a genuine third-curvature packet on the untouched product bank can be spent before any small physical pair is inverted.

## 3. Deterministic spectral inheritance from a small physical pair

The next lemma turns the bare `s_3(A)>=1` hypothesis into third curvature on the complement whenever the pair-to-complement crossing is not too large.

### Lemma `QFORM-SMALLPAIR-COMPLEMENT-S3-INHERITANCE-v1`

With block form (1.2), put

`b=||B||_op`, `u=||W||_op`.                                       (3.1)

If `s_3(A)>=1`, then

`boxed:
 s_3(C) >= 1-eta(b,u),
 eta(b,u)=[b+sqrt(b^2+4u^2)]/2.}`                                 (3.2)

The right side is useful whenever `u^2<1-b`.

### Proof

Let

`A_0=diag(0_2,C)`,
`E=A-A_0=[[B,W],[W^T,0]]`.                                        (3.3)

For a unit vector `(x,y)`,

`|<(x,y),E(x,y)>|
 <=b||x||^2+2u||x||||y||`.                                        (3.4)

The maximum of the right side on `||x||^2+||y||^2=1` is the top eigenvalue of the scalar matrix

`[[b,u],[u,0]]`,                                                   (3.5)

namely `eta(b,u)`. Since `E` is symmetric,

`||E||_op<=eta(b,u)`.                                              (3.6)

Singular values are 1-Lipschitz in operator norm, so

`s_3(A_0)>=s_3(A)-||E||_op>=1-eta(b,u)`.                           (3.7)

The two zero coordinates in `A_0` do not affect its third singular value; hence `s_3(A_0)=s_3(C)`. QED.

## 4. Target-level compiler for the current overlap-two small-pair state

In (1.1), elementary row-sum control gives

`||B||_op <=3/64`.                                                  (4.1)

Split according to the aggregate pair-to-leaf crossing energy.

### Branch A: coupling-heavy

If

`||W||_F^2 >=1/4`,                                                 (4.2)

then the completed first-compound product-Fourier theorem applied to the literal cut `S | S^c` gives

`sup_t P{|Q-t|<rho}
 <= H_1 ||W||_F^(-1/2) sqrt(rho)`                                  (4.3)

with

`H_1=2^(3/4)e^(1/4)Gamma(1/4)=7.829376757708328...`.

Thus

`boxed:
 sup_t P{|Q-t|<rho}
 <= sqrt(2) H_1 sqrt(rho)
 =11.07241079567981... sqrt(rho).}`                               (4.4)

This remains only a half-Riesz/square-root small-ball certificate. By the live correction forbidding “half-Riesz plus a bare square” as a universal density compiler, **no bounded-density conclusion is claimed from (4.4)**.

### Branch B: coupling-light

Assume instead

`||W||_F^2<1/4`.                                                    (4.5)

Then `u<1/2`, and (3.2), (4.1) give

`s_3(C) >= s_*`,                                                   (4.6)

where the exact constant is

`boxed:
 s_* =1-[3/64+sqrt((3/64)^2+1)]/2
     =(125-sqrt(4105))/128
     =0.4760134850112079... .}`                                    (4.7)

The overlap packet also forces enormous complement curvature. From (1.3),

`sqrt(J_2(S))
 <= |det B| ||off C||_F + ||adj B||_op ||W||_F^2`.                 (4.8)

Under (1.1),

`|det B|<=5/4096`, `||adj B||_op<=3/64`.                           (4.9)

Using `sqrt(J_2)>=1/12` and (4.5),

`1/12 <(5/4096)||off C||_F+3/256`,                                (4.10)

so

`boxed: ||off C||_F >176/3=58.666666... .}`                        (4.11)

Now let `P_*` project onto all eigenspaces of `C` with

`|lambda(C)|>=s_*/64`.                                             (4.12)

If

`max_i(P_*)_ii<=1/32`,                                             (4.13)

Theorem 2 with `s=s_*` proves the **full ambient** estimate

`boxed:
 ||p_Q||_infinity
 <=288 sqrt(3e)/(13s_*)
 =132.90390686367482... ,
 p_Q in C_0(R).}`                                                  (4.14)

Hence every still-unpaid localized overlap-two small-pair state now lies in one of only three explicit bins:

1. the coupling-heavy half-Riesz packet (4.2)-(4.4);
2. the paid continuous-density spectral-window branch (4.5), (4.13);
3. a coupling-light but **high spectral-window leverage** complement, where (4.6), (4.11) hold and some original coordinate has `(P_*)_ii>1/32`.

The small pair itself is therefore no longer an obstruction in the coupling-light/diffuse-curvature sector.

## 5. A genuinely rotated indefinite singular-collar stress family

The next family shows why the new branch is qualitatively different from paying a reciprocal tiny pair scale.

Let `m=256` and choose six orthonormal Walsh vectors

`r_1,...,r_6 in R^256`,                                           (5.1)

each having coordinates `+/-1/16`. For `0<epsilon<1/64`, set

`B_epsilon=epsilon [[1,1],[1,-1]]`,                               (5.2)

`a=1/4`,

`W=a [r_5^T; r_6^T]`,                                             (5.3)

and

`L_epsilon=1/(32 epsilon^2)`,                                     (5.4)

`C_epsilon=L_epsilon(r_1r_1^T+r_2r_2^T-r_3r_3^T-r_4r_4^T)`.       (5.5)

Finally define the 258-dimensional physical matrix

`A_epsilon=[[B_epsilon,W],[W^T,C_epsilon]]`.                       (5.6)

This is genuinely rotated and indefinite: the four Walsh directions `r_1,...,r_4` remain exact eigenvectors of `A_epsilon` with eigenvalues

`{L_epsilon,L_epsilon,-L_epsilon,-L_epsilon}`.                    (5.7)

Thus the owner spectral hypothesis holds with enormous room for every sufficiently small epsilon. No spectral coordinate is treated as an independent random variable; the eigenvectors are used only to certify the deterministic matrix.

Every physical diagonal is small:

`diag C_epsilon=0`,                                                (5.8)

because the four Walsh squares are identical and the signs in (5.5) cancel, while the two pair diagonals are `+epsilon,-epsilon`. The pair off-diagonal is also `epsilon<1/32`. Every pair-to-leaf entry is nonzero with magnitude `a/16=1/64`.

### Exact overlap-two packet

For this pair,

`det B_epsilon=-2epsilon^2`,                                      (5.9)

and `C_epsilon` is Frobenius-orthogonal to `W^T adj(B_epsilon) W`; because `diag C_epsilon=0`, the same is true after applying `off`. Moreover

`||C_epsilon||_F^2=4L_epsilon^2`.                                 (5.10)

Therefore the exact numerator identity gives

`J_2(S)
 =16 epsilon^4 L_epsilon^2
  +||(off)(W^T adj(B_epsilon)W)||_F^2`                             (5.11)

and hence, by (5.4),

`boxed: J_2(S)>=1/64>1/144.}`                                     (5.12)

The second term is explicitly

`(255/64)epsilon^2 a^4`,                                          (5.13)

so there is no hidden cancellation.

Thus this family lies literally in the localized small-pair overlap-two collar while `det B_epsilon ->0`.

### New conditional Fourier estimates

The high spectral projection of `C_epsilon` is

`P=sum_(k=1)^4 r_k r_k^T`,                                        (5.14)

with every physical diagonal

`P_ii=4/256=1/64<1/32`.                                           (5.15)

Theorem 2 applied at the **actual complement scale** `s=L_epsilon` gives

`boxed:
 ||p_(X^T A_epsilon X)||_infinity
 <=[288 sqrt(3e)/(13L_epsilon)]
 =2024.4496600890511... epsilon^2,
 p in C_0.}`                                                       (5.16)

So the certificate gets stronger as the physical pair becomes singular; it spends the compensating third curvature instead of inverting the pair.

There is an even sharper literal-cut product-Fourier bound. Partition the 256 leaves by a seventh Walsh character. Then the crossing block of `C_epsilon` has four singular values exactly `L_epsilon/2`. Hence

`E_3=4(L_epsilon/2)^6=L_epsilon^6/16`.                             (5.17)

Conditioning the two pair variables and applying `QFORM-THIRDCOMPOUND-CROSS-PROMOTION-v1` gives

`boxed:
 ||p_(X^T A_epsilon X)||_infinity
 <=6^(4/3) 2^(2/3)/L_epsilon
 =553.8238349980446... epsilon^2,
 p in C_0.}`                                                       (5.18)

This retains the entire arbitrary pair-to-leaf affine shift after conditioning.

For comparison, the preceding fixed-pair receiver scales in the wrong direction here. Since

`kappa(B_epsilon)=sqrt(2)epsilon`, `J_2>=1/64`,                    (5.19)

its coarse bound behaves like

`<=29.02951843729316... epsilon^(-1/4)`.                           (5.20)

Thus the new route is a genuine **curvature-compensation mechanism**: local pair conditioning deteriorates, while product-Fourier smoothing on the complement improves like `epsilon^2`.

At the concrete value `epsilon=1/128`,

`L_epsilon=512`,                                                   (5.21)

and the three bounds are

`spectral-window: 0.12356260132379462...`,                        (5.22)

`explicit cross-E3: 0.03380272430407989...`,                      (5.23)

while the small-pair reciprocal certificate is roughly two orders of magnitude larger.

## 6. Required account02/B04 result applied at an actual inequality

Apply the completed account02/B04 r16 diffuse-curvature theorem to the **same conditioned leaf equation** in the family above. Here

`rank(C_epsilon)=4`,
`beta=1/64`,
`sigma=s_3(C_epsilon)=L_epsilon`,
`r beta=1/16`.                                                     (6.1)

All pair terms have become affine after conditioning, precisely as allowed in the partner proof. Therefore (1.4) yields

`boxed:
 ||p_(X^T A_epsilon X)||_infinity
 <=2C_*/[(1-1/4)L_epsilon]
 =(8C_*/3)L_epsilon^(-1)
 =(256C_*/3)epsilon^2.}`                                          (6.2)

Numerically,

`(256C_*/3)=721.3244779117378...`.                                 (6.3)

At `epsilon=1/128`, the actual partner inequality is

`boxed: ||p_Q||_infinity <= C_*/192
 =0.04402615221629259... .}`                                      (6.4)

The explicit Walsh cross-`E_3` certificate (5.23) is about 23 percent sharper on this special carrier, while the partner theorem is more flexible because it requires only diffuse residual range rather than the explicit seventh-character split.

## 7. What remains

This run does **not** solve full QFORM. In the current localized overlap-two small-pair compiler, the remaining mathematical debt is now sharper:

`QFORM-SMALLPAIR-COUPLING-OR-HIGHLEVERAGE-ROUTING-v1`.

After (4.14), every unpaid state has either

- `||W||_F^2>=1/4`, with the explicit first-compound half-Riesz certificate (4.4), or
- `||W||_F^2<1/4`, `s_3(C)>=s_*`, `||off C||_F>176/3`, and a high spectral-window-leverage original coordinate `(P_*)_ii>1/32`.

The next proof should route these two concentration mechanisms into the completed physical-hub, rank-two affine half-Riesz + independent square, pair-log, projected-crossing, or grouped-bank endpoints. The live corrections show why one must not simply convolve (4.4) with a bare square or perturbatively delete the nonzero near-null pair curvature.

Claim IDs proposed for review:

- `QFORM-CONDITIONED-SPECTRAL-WINDOW-EXIT-v1`;
- `QFORM-SMALLPAIR-COMPLEMENT-S3-INHERITANCE-v1`;
- `QFORM-OVERLAP2-SMALLPAIR-DIFFUSE-COMPLEMENT-EXIT-v1`.

Full QFORM: **OPEN**. Full-target continuity: **OPEN**. New spectral-window and explicit cross-`E_3` branches: **continuous `C_0` density proved**.
