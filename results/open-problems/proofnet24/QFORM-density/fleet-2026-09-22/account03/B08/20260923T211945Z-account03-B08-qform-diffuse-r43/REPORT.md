SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B08, 2026-09-23T21:19:45Z.
attacking: adaptive low-cross-rank alignment receiver: retain original-coordinate product provenance while converting an exact rank-one Schur crossing into a square-root small-ball resource for the physical indefinite-pair logarithmic smoother.

# account03/B08 — exact rank-one Schur-crossing receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T211945Z-account03-B08-qform-diffuse-r43`  
Assignment: diffuse eigenvector case  
Owner continuation acknowledged: `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`  
Owner control at startup: revision `2026-09-22.15`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Classification: `NEW SUPPORTING ANALYTIC THEOREM + NEW R45 COMPILER / FULL TARGET OPEN`.

The unrestricted QFORM conjecture remains OPEN. The global continuous-density conclusion remains OPEN. All random coordinates used below are original independent coordinates, except for linear projections used only through already-proved marginal-density bounds. No Gaussian, log-concavity, moment, bounded-support, connected-support, post-rotation-independence, arbitrary-joint coarea, fiber-supremum, or law-uniform one-dimensional quadratic-phase-decay hypothesis is introduced.

## 1. Source pins and the exact missing implication

The immediate B08 inputs are:

1. `yspennstate/math-open-problems@a3624cdb18747a63e9e6991d83233c30e1664f4b`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260923T190424Z-account03-B08-qform-diffuse-r45/REPORT.md`.
   This pays the two-hub common-plane state when the exact two-hub Schur mismatch has nonzero rank-two area, and separately pays the exact physical-hub block `B=0`.  It leaves singular/near-singular nonzero hub blocks and the rank-at-most-one Schur-mismatch surface.

2. `yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`,
   `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.
   Section 1 proves the exact-rank crossing characteristic-function estimate with arbitrary same-bank functions.  The owner continuation records this projected-crossing bundle as independently reviewed.  I use only the rank-one specialization and the scalar orthonormal-projection density cap `sqrt(2)`.

3. `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`,
   `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.
   Its general physical-indefinite-pair implication says that if, after exact completion of an invertible indefinite physical pair, the remainder `R` satisfies

   `sup_t P(|R-t|<rho) <= H sqrt(rho)` for every `rho>0`,          (1.1)

   then, with `D=|det B|` and `kappa=sigma_min(B)`,

   `||p_Q||_infinity <= 4 sqrt(2H) (D kappa)^(-1/4)`.             (1.2)

   The physical-pair shifts may depend arbitrarily on the remainder variables.  This is essential because the current live correction `QFORM-INDEFINITE-INNOVATION-ARBITRARY-REMAINDER-FALSE-v1` rules out replacing genuine third curvature by a mere slope-innovation condition.

The first missing implication attacked here is therefore precise: **does an exact rank-one original-product crossing supply the square-root small-ball hypothesis (1.1), uniformly over arbitrary same-bank curvature?**  The answer is yes, with an explicit dimension-free constant.

## 2. Rank-one crossing gives square-root small-ball

### Theorem 2.1 — `QFORM-RANK1-CROSSING-SQRT-SMALLBALL-v1`

Let `X` and `Y` be disjoint blocks of original independent scalar random variables, every scalar density bounded by one.  Let `C` be a real matrix of exact rank one with sole nonzero singular value `sigma>0`.  Let `F(X)` and `G(Y)` be arbitrary measurable real functions, finite almost surely, and put

`R = F(X) + 2 X^T C Y + G(Y)`.                                   (2.1)

Then for every `s in R` and every `rho>0`,

`boxed:
 P(|R-s|<rho)
 <= H_1 sigma^(-1/2) sqrt(rho),
 H_1=e^(1/2) 2^(1/4) Gamma(1/4)
     =7.108628442830306... .`                                    (2.2)

The right side may of course be replaced by its minimum with one.

### Proof

Write a thin SVD `C=sigma u v^T`, with `u,v` unit vectors.  The scalar orthonormal projections `u^T X` and `v^T Y` have density caps at most `sqrt(2)`.  This is a statement about the marginal laws of two disjoint source blocks; it does **not** declare any rotated coordinate vector independent.

The exact-rank crossing theorem cited in Section 1 applies with rank `r=1` and arbitrary internal functions `F,G`.  With `M_X,M_Y` denoting the two scalar projection caps, it gives

`|phi_R(t)|
 <= min(1,
        (pi/|t|)^(1/2) (M_X M_Y)^(1/2) sigma^(-1/2))`.            (2.3)

Since `M_X,M_Y<=sqrt(2)`,

`|phi_R(t)| <= min(1, sqrt(2 pi) sigma^(-1/2)|t|^(-1/2)).`       (2.4)

This is a bilinear grouped-product estimate.  It is not the refuted law-uniform pointwise quadratic-phase estimate.

For the interval event use the positive Gaussian majorant

`1_{|x-s|<rho}
 <= exp(1/2) exp(-(x-s)^2/(2 rho^2)).`                            (2.5)

Gaussian Fourier inversion gives

`P(|R-s|<rho)
 <= e^(1/2) rho/sqrt(2pi)
    int_R exp(-rho^2 t^2/2) |phi_R(t)| dt`.                       (2.6)

In (2.6) use the second term of (2.4), which is an upper bound even where it exceeds one.  The remaining integral is explicit:

`int_R exp(-rho^2 t^2/2)|t|^(-1/2) dt
 =2^(1/4) Gamma(1/4) rho^(-1/2).`                                (2.7)

Substitution of (2.7) into (2.6) proves (2.2).  No regularity of `F,G` and no moment of `X,Y` is used. QED.

### Why this is a genuinely diffuse estimate

The theorem spends the **singular value** of the rank-one physical crossing, not one physical coefficient.  For example, if `r=(1,...,1)/sqrt(m)` and

`C=L r r^T`,                                                     (2.8)

then `sigma=L` while every individual physical coefficient is only `L/m`.  Thus (2.2) remains dimension free when every individual cross coefficient tends to zero.

## 3. Physical indefinite pair plus an exact rank-one Schur crossing

### Theorem 3.1 — `QFORM-INDEFINITE-PAIR-RANK1-SCHUR-CROSSING-v1`

Let `H=(H_1,H_2)` be two original independent coordinates with density caps one.  Let `B` be their real symmetric invertible **indefinite** quadratic block, and set

`D=|det B|`, `kappa=sigma_min(B)>0`.                              (3.1)

Let the remaining original coordinates contain two disjoint product banks `X,Y`.  After exact completion of the physical pair `H`, suppose the remainder, after conditioning any additional original coordinates, has the form

`R=F(X)+2X^T C Y+G(Y)`                                          (3.2)

with arbitrary measurable `F,G` and an exact rank-one `C` of sole singular value `sigma>0`.  The translated physical pair may depend arbitrarily on `(X,Y)` and on the conditioned coordinates.

Then the full quadratic form has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <= C_1 (D kappa sigma)^(-1/4),
 C_1=4 sqrt(2 H_1)
    =15.082311168072676... .}`                                   (3.3)

Continuity is not asserted by this argument.

### Proof

Theorem 2.1 supplies (1.1) with

`H=H_1 sigma^(-1/2)`.                                           (3.4)

The completed physical-pair theorem (1.2) explicitly permits the two pair-coordinate shifts to depend on the same variables that define `R`.  Therefore

`||p_Q||_infinity
 <=4 sqrt(2H_1 sigma^(-1/2))(D kappa)^(-1/4)
 =C_1(D kappa sigma)^(-1/4)`.                                   (3.5)

If further original coordinates were conditioned, all newly generated terms are affine or same-bank terms inside `F,G`; the constant in (3.5) is uniform in the conditioned values.  Averaging the conditional densities preserves (3.5). QED.

This theorem is deliberately narrower than the refuted `indefinite pair + arbitrary innovative remainder` mechanism.  The third smoothing resource here is a **literal exact rank-one crossing between two independent original-coordinate banks**, and Theorem 2.1 proves its interval small-ball estimate before it is fed into the pair logarithm.

## 4. Application to the r45 common-plane rank-one mismatch surface

Use the r45 notation.  There are two physical hub coordinates with invertible indefinite block `B`, two disjoint original product banks with full-row-rank arm matrices

`M_1 in R^(2 x m_1)`, `M_2 in R^(2 x m_2)`,                    (4.1)

and, in the exact common-plane/no-transverse-tail state,

`C = M_1^T R_c M_2`.                                            (4.2)

After exact completion of the physical hub pair the light-light crossing is

`C_B = M_1^T J M_2,
 J=R_c-B^(-1).`                                                  (4.3)

r45 paid `rank(J)=2` by aggregate `E_2`.  Assume now

`rank(J)=1`, `j=sigma_1(J)>0`.                                  (4.4)

Put

`beta_r=sigma_2(M_r)>0`, `r=1,2`.                               (4.5)

Write `J=j u v^T` with unit `u,v`.  Then (4.3) is the outer product

`C_B=j (M_1^T u)(M_2^T v)^T`,                                   (4.6)

so its unique nonzero singular value is

`sigma(C_B)=j ||M_1^T u|| ||M_2^T v||
          >= j beta_1 beta_2`.                                  (4.7)

Theorem 3.1 now gives the explicit missing-surface estimate

`boxed:
 ||p_Q||_infinity
 <=15.083 [D kappa j beta_1 beta_2]^(-1/4).}`                    (4.8)

All same-bank quadratic-affine terms are retained.  No physical minor is selected.

At target scale, if for some positive parameters

`kappa>=tau L`,
`beta_1>=eta_1 L`, `beta_2>=eta_2 L`,
`j>=gamma/L`,                                                    (4.9)

then `D>=kappa^2`, hence

`boxed:
 ||p_Q||_infinity
 <=15.083 tau^(-3/4)(gamma eta_1 eta_2)^(-1/4)L^(-1).}`          (4.10)

Thus the determinant-zero Schur-mismatch surface is **not** itself a singular analytic endpoint: whenever its surviving rank-one channel has quantitative product scale, it pays by square-root small-ball plus the pair logarithm.

What (4.8) does **not** do is infer quantitative lower bounds on `beta_1,beta_2,j` from the bare three-large-eigenvalue hypothesis.  In particular, highly anisotropic arms can have fixed area but tiny least singular value.  That structural routing remains necessary.

## 5. A target-valid diffuse family paid uniformly while every physical coefficient vanishes

Take `m>=2`, `L>=1`, and

`r=(1,...,1)/sqrt(m) in R^m`.                                   (5.1)

On original coordinates `(U,V,X_1,...,X_m,Y_1,...,Y_m)` define

`Q_{m,L}=2LUV+2L(r^T X)(r^T Y)`.                                (5.2)

The coefficient matrix is the direct sum of the physical indefinite pair

`[[0,L],[L,0]]`                                                  (5.3)

and the rank-one bipartite block with cross matrix `L r r^T`.  Its nonzero spectrum is exactly

`{-L,-L,L,L}`.                                                   (5.4)

Hence it satisfies the owner target for every `L>=1`.  The rank-one crossing has `sigma=L`, while every individual `X_i-Y_j` coefficient is `L/m`.

For the physical pair,

`D=L^2`, `kappa=L`;                                              (5.5)

therefore Theorem 3.1 yields

`boxed:
 ||p_(Q_{m,L})||_infinity
 <=15.083/L,`                                                    (5.6)

uniformly in `m` and in every admissible product input law.  This is an actual dimension-free diffuse-eigenvector estimate with no moment/support hypothesis and with all individual cross coefficients vanishing as `m -> infinity`.

Continuity of this family is not claimed from the current argument; (5.6) is an essential-supremum result.

## 6. Designated partner account04/B08 applied at an actual inequality

The designated completed partner theorem is

`yspennstate/math-open-problems@abbec61f52e1f4b4d367fd67e73e4d2501ac9c74`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B08/20260923T091414Z-account04-B08-QFORM-r1/REPORT.md`.

For the exact original-coordinate anisotropic family

`Q_(R,L)=L X_0^2+2LR U_1V_1+2L R^(-1)U_2V_2`, `R>=3`,          (6.1)

its grouped rank-two receiver gives the actual inequality

`boxed: ||p_(Q_(R,L))||_infinity <7.251/L.`                     (6.2)

This partner application is complementary to (4.8), not a substitute for it.  In (6.1) the arm singular values are `LR` and `L/R`, so a receiver that pays only the least arm singular value would deteriorate as `R->infinity`, whereas the partner theorem remains uniform because it spends the fixed second-exterior product.  Thus the current B08 picture now has two rigorously different payments:

- diffuse exact rank-one Schur crossing: (3.3)/(4.8), which can remain uniform when every individual coefficient vanishes;
- maximally anisotropic localized fixed-`E_2` direct sum: partner bound (6.2), which remains uniform when the least arm singular value vanishes.

The still-missing step is to route arbitrary coupled survivors into one of these currencies without discarding same-bank or transverse leakage.

## 7. Correction checks

This run explicitly respects the live correction boundary.

- It does not use bounded density to infer pointwise quadratic-phase decay.  Equation (2.3) is the already-proved **bilinear exact-crossing** estimate obtained by complex pushforward and Plancherel.
- It does not use a bounded projection density to control an arbitrary indefinite quadratic pushforward.  The indefinite physical pair is handled by its explicit logarithmic density envelope, and the rank-one remainder is separately proved to satisfy square-root interval small-ball.
- It does not treat a rotated input vector as independent.  The singular vectors of `C` are used only to invoke marginal projection-density caps on two disjoint source blocks.
- It does not discard a coefficient-small tail as a small random error.
- It does not invoke a good single physical minor.
- It does not contradict `QFORM-INDEFINITE-INNOVATION-ARBITRARY-REMAINDER-FALSE-v1`: the arbitrary-remainder statement is false; the exact original-product rank-one crossing in Theorem 2.1 is the additional hypothesis that supplies the missing third curvature.

## 8. Regression computations

`CHECKS.py` / `CHECKS.txt` in this run directory record:

- `H_1=7.108628442830306`;
- `C_1=15.082311168072676`;
- exact nonzero spectrum `{-L,-L,L,L}` for the diffuse model at several dimensions;
- physical cross-entry scale exactly `L/m` in that model;
- 5,000 seeded tests of

  `sigma_1(M_1^T J M_2)
   >=sigma_2(M_1)sigma_2(M_2)sigma_1(J)`                          (8.1)

  for rank-one `J`, with no violation; minimum observed ratio `1.000562653308`.

The checker terminates `QFORM_B08_R43_RANK1_CHECK_PASS`.  These computations are regression evidence only; the proof of (8.1) is the one-line rank-one factorization (4.6)-(4.7).

## 9. Remaining B08 debt

The current exact next implication is

`QFORM-R45-EXACTMATCH-OR-TRANSVERSE-TAIL-PLUS-SINGULAR-HUB-RECEIVER-v1`.

The unpaid configurations are:

1. exact common-plane Schur match `R_c=B^{-1}` (so `J=0`), where the genuine third spectral curvature must be found in the retained same-bank Schur remainder rather than invented from pair innovation;
2. a nonzero transverse light-light tail added to the rank-one common-plane channel, unless it already triggers the reviewed projected-volume theorem;
3. singular or near-singular nonzero physical two-hub blocks;
4. the structural anisotropic transition in which `beta_1 beta_2` is too small for (4.8) but the full survivor is not in the exact partner direct-sum scope.

The latest correction showing that an indefinite pair plus arbitrary innovation can still have a logarithmically unbounded density makes item 1 genuine: a proof must retain the third curvature supplied by the target spectrum.  Full QFORM and global continuity remain OPEN.
