SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B06, 2026-09-23T10:22:06Z.
attacking: the transverse exact-rank-three survivor from r32: split high physical leverage into a paid conditioned diffuse remainder or a bounded-cardinality original-coordinate hub, retaining the full rank-three quadratic matrix.

# account03/B06 r33 — conditional light-frame compiler for the transverse rank-three survivor

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Curved fiber integration  
Status: **NEW SUPPORTING THEOREM / FULL QFORM OPEN / FULL CONTINUITY OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.


## 1. Source-valid inputs

### 1.1 r32 transverse curvature

The predecessor is

`yspennstate/math-open-problems@9583647ef39bb355508b8f8fb49f05ded8b594f2`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260923T094916Z-account03-B06-qform-r32/REPORT.md`.

For the null-pivot transverse shared translation, r32 produces the exact-rank-three ORIGINAL-coordinate quadratic matrix

`B_h=C S C^T`,

with

`|pdet(B_h)|=|beta| k^2 G ||w||^2`.                                 (1.1)

Its first unpaid branch was `QFORM-NULLPIVOT-TRANSVERSE-HIGHLEVERAGE-OR-IMBALANCE-v1`: when the whole range is not diffuse enough for the existing regularized-determinant theorem, isolate a bounded physical hub or a product-preserving receiver without deleting the nonzero third direction.

### 1.2 Diffuse full-range theorem

The completed supporting theorem is

`yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`

`proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`.

If an exact-rank-three symmetric matrix has all three nonzero singular values at least `sigma>0` and the coordinate diagonal of its ENTIRE range projection is at most `1/32`, then the corresponding quadratic form of independent cap-one ORIGINAL coordinates, even after arbitrary coordinate-separable measurable additions, has a continuous `C_0` density with

`||p||_infinity <= C0/sigma`,

where

`C0=96e/(7sqrt(2))=26.3604413359... <27`.                           (1.2)

The coordinate-separable allowance includes the affine terms created by conditioning other original coordinates.

### 1.3 Exact-rank-three physical-pivot theorem

The completed theorem `QFORM-RANK3-ALL-RESIDUAL-ORIENTATIONS-v1` is

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

For an exact-rank-three block `B=U Lambda U^T`, physical leverage `ell_i=||u_i||^2`, and nonzero physical pivot `a_i=B_ii`, it gives

`||p||_infinity <=128 [ell_i |a_i| |det Lambda|]^(-1/4)`.             (1.3)

It permits arbitrary outside couplings through the induced affine term.

### 1.4 Account04 result actually applied

The designated `account04/B06` QFORM directory is still absent at the fresh repository check, so no theorem from that exact slot is invented. I use the compatible completed account04/B18 theorem instead:

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T113729Z-account04-B18-qform-r1/REPORT.md`.

Its dependence-safe square smoothing says that if a base variable has density cap `M`, and conditionally on the base source an untouched scalar has density cap one before a translated square, then

`||p_{R+aV^2}||_infinity <=2 sqrt(M/|a|)`,                            (1.4)

without requiring independence between the base value and the translated square.

## 2. Main deterministic split

Let

`B=U Lambda U^T`,  `U^T U=I_3`,                                     (2.1)

be any real symmetric exact-rank-three matrix in ORIGINAL coordinates. Write the physical row vectors of `U` as `u_i^T`, put

`ell_i=||u_i||^2`,                                                   (2.2)

and let

`s=s_3(B)=min_j |lambda_j|>0`.                                       (2.3)

Fix a parameter `0<theta<1` and define the heavy and light physical sets

`H={i: ell_i>theta/32}`,  `L=H^c`.                                  (2.4)

Put

`M_L=U_L^T U_L`,  `M_H=U_H^T U_H=I_3-M_L`.                          (2.5)

Because `sum_i ell_i=3`,

`|H|<96/theta`.                                                      (2.6)

There are now two exhaustive cases.

### Case D: the light frame still spans quantitatively

Suppose

`M_L >= theta I_3`.                                                  (2.7)

Then condition on every ORIGINAL coordinate `X_H`. The remaining `X_L` stay independent with their original density caps. The conditional quadratic matrix on the light bank is

`B_LL=U_L Lambda U_L^T`;                                             (2.8)

all heavy-light couplings become affine functions of `X_L`, and the heavy-heavy part becomes a scalar translation.

Define

`V=U_L M_L^(-1/2)`.                                                  (2.9)

Then `V^T V=I_3` and

`B_LL=V Lambda_L V^T`,
`Lambda_L=M_L^(1/2) Lambda M_L^(1/2)`.                              (2.10)

For every singular-value index,

`s_j(Lambda_L)>=lambda_min(M_L) s_j(Lambda)>=theta s_j(Lambda)`,     (2.11)

by the standard singular-value inequality under left/right multiplication by invertible matrices. In particular all three nonzero singular values of `B_LL` are at least `theta s`.

For a light physical coordinate `i`, the leverage of the whitened range is

`||v_i||^2=u_i^T M_L^(-1)u_i
 <= ell_i/theta
 <=1/32`.                                                           (2.12)

Thus the entire conditional light range satisfies the diffuse theorem. Uniformly in the conditioned heavy values,

`||p_(Q|X_H)||_infinity <= C0/(theta s)`.                            (2.13)

The theorem's characteristic-function majorant is independent of the affine coefficients generated by the conditioning; alternatively one can average the uniformly bounded continuous conditional densities and use dominated convergence. Hence the unconditional output has a continuous density and the same cap:

`boxed: ||p_Q||_infinity <= C0/(theta s).`                           (2.14)

No quadratic tail on the light bank was deleted: the full matrix `B_LL` is retained and whitened only at the deterministic frame level.

### Case H: failure of the light span forces a finite physical hub

If (2.7) fails, choose a unit vector `z in R^3` with

`z^T M_L z<theta`.                                                   (2.15)

Then

`boxed: sum_(i in H) (u_i dot z)^2=z^T M_H z>1-theta.`               (2.16)

So a set of fewer than `96/theta` ORIGINAL coordinates captures more than `1-theta` of one genuine spectral-range direction. This is a deterministic bounded-cardinality hub certificate; no probabilistic projection density or physical minor is selected.

## 3. High-leverage hub: pivot or robust grouped star

The finite hub can be sharpened further before any local reciprocal payment.

For every physical coordinate `i`,

`||B e_i||^2=u_i^T Lambda^2 u_i >=s^2 ell_i`.                        (3.1)

Write

`a_i=B_ii`,
`b_i=B[H_i^c,{i}]`, i.e. the complete off-diagonal physical star from `i`. (3.2)

Then

`a_i^2+||b_i||_2^2=||B e_i||^2`.                                    (3.3)

For every `i in H`, (2.4) and (3.1) imply

`||B e_i||>s sqrt(theta/32)`.                                       (3.4)

Consequently at least one of the two grouped currencies satisfies

`|a_i| >= s sqrt(theta)/8`

or

`||b_i||_2 >= s sqrt(theta)/8`.                                     (3.5)

The point is that the alternative uses the WHOLE off-diagonal star norm; it does not pick a vanishing individual edge.

If there exists `i in H` satisfying the scalar-pivot alternative, then (1.3), together with

`ell_i>theta/32`,
`|a_i|>=s sqrt(theta)/8`,
`|det Lambda|>=s^3`,                                                 (3.6)

gives

`ell_i |a_i| |det Lambda| > theta^(3/2) s^4/256`.                    (3.7)

Therefore

`boxed: ||p_Q||_infinity <=512 theta^(-3/8) s^(-1).`                 (3.8)

If no heavy coordinate satisfies that pivot alternative, then every heavy coordinate obeys

`boxed: ||b_i||_2>s sqrt(theta)/8.`                                  (3.9)

Thus the genuinely unpaid high-leverage branch is no longer an unspecified failure of a leverage gate. It is a finite ORIGINAL-coordinate hub of size `<96/theta`, carrying `>1-theta` of a spectral direction, whose every heavy row has a quantitatively nontrivial complete off-diagonal star.

## 4. Concrete collar theta=1/2

Take

`theta=1/2`.                                                         (4.1)

Then

`H={i:ell_i>1/64}`,  `|H|<192` (hence at most 191).                   (4.2)

Exactly one of the following holds:

1. **Conditioned diffuse light bank:** `M_L>=I_3/2`, and

   `boxed: ||p_Q||_infinity <=2C0/s
          =52.7208826719.../s <53/s`,                               (4.3)

   with a continuous density.

2. **Paid heavy scalar pivot:** some `i in H` has

   `|B_ii|>=s/(8sqrt(2))`,                                          (4.4)

   and

   `boxed: ||p_Q||_infinity
          <=512*2^(3/8)/s
          =663.981851982.../s <664/s`.                              (4.5)

3. **Near-isotropic robust-star hub:** there is a unit `z` for which

   `sum_(i in H)(u_i dot z)^2>1/2`,                                 (4.6)

   and every `i in H` satisfies

   `|B_ii|<s/(8sqrt(2))`,
   `||B[H_i^c,{i}]||_2>s/(8sqrt(2))`.                               (4.7)

This is `QFORM-RANK3-LIGHT-DIFFUSE-OR-191-STAR-HUB-v1`.

It is exactly the high-leverage/imbalance compiler requested by r32: diffuse high-dimensional geometry is paid after conditioning only a bounded heavy bank, while failure is compressed to a bounded physical hub with quantitative grouped-star curvature. The result is scale-correct in `s=s_3(B)` and makes no assumption that `s` is comparable to the geometric mean of the three singular values.

For the r32 transverse matrix `B_h`, equation (1.1) remains available simultaneously:

`|pdet(B_h)|=|beta|k^2G||w||^2=s_1(B_h)s_2(B_h)s_3(B_h)`.             (4.8)

Thus if `s_3(B_h)` itself is tiny, this is an explicit spectral-imbalance survivor rather than an untracked loss of curvature.

## 5. Actual account04/B18 splice

On branch 1 above, suppose an untouched original scalar `T` with density cap one enters through an actual translated square

`Q_*=Q+a_0[T+Psi]^2`,  `a_0!=0`,                                   (5.1)

where `Psi` may depend arbitrarily on the base source. Apply account04/B18 (1.4) to the genuine equation (5.1) with the base cap (4.3). No independence between the value `Q` and the translated square is asserted or required. This gives

`||p_(Q_*)||_infinity
 <=2 sqrt(2C0/(|a_0|s))
 =14.521829... /sqrt(|a_0|s).`                                     (5.2)

This is the completed account04 result applied at an actual inequality. The exact designated partner `account04/B06` remains unavailable and is not fabricated.

## 6. Checks and stress tests

The deterministic arithmetic checks are saved beside this report. In addition, 1000 random Parseval 3-frames with dimensions between 100 and 999 were tested at `theta=1/2`. In every instance either the light Gram had minimum eigenvalue below `1/2`, in which case the computed hub directional mass was above `1/2`, or the light Gram exceeded `1/2`, in which case the maximum whitened light leverage was at most `1/32`. There were zero violations; the largest observed whitened leverage in the diffuse branch was `0.0299630...`. These finite checks are sanity tests only; equations (2.5)-(2.16) are the proof.

## 7. Remaining implication

The full QFORM conjecture is still OPEN / NOT PROVED / NOT DISPROVED.

The first B06 debt is now

`QFORM-191-STAR-HUB-PRODUCT-RECEIVER-v1`:

> In branch (4.6)-(4.7), retain the full quadratic matrix and use the finite heavy bank plus the complete star norms before selecting local edges. Either route a robust heavy-to-light star packet into the weighted affine-fiber / grouped-bank / rank-two half-Riesz machinery, or show that concentration of those stars inside the <=191 heavy coordinates forces a bounded-cardinality physical pair or null-bank certificate already paid by an existing theorem. Separately, if `s_3(B_h)` is very small relative to the exact product currency (4.8), exploit the resulting large two-volume `s_1s_2=|pdet|/s_3` without discarding the third direction.

Continuity is proved in the conditioned-diffuse branch, but not by the pivot theorem and therefore not for the full target.
