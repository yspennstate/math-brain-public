SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B08, 2026-09-23T21:49:09Z.
attacking: an explicit full-matrix physical-pair gate, followed by the near-singular exact-Schur-match endpoint of the diffuse/common-plane hybrid.

# account02/B08 r28 — a 619/L physical-pair gate and an exact-match diffuse stress family

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: diffuse eigenvector case / complementary constructions and source-valid counterexamples  
Designated partner: `account03/B08`  
Owner continuation acknowledged: `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`  
Owner control at startup and pre-write refresh: revision `2026-09-22.15`, QFORM only  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: `NEW SUPPORTING FULL-AMBIENT ROUTER + QUANTIFIED HYBRID + TARGET-VALID EXACT-MATCH STRESS FAMILY / FULL TARGET OPEN`.

The unrestricted QFORM conjecture remains OPEN. Essential boundedness is the target below; continuity is stated only where the Fourier theorem actually supplies it. Every random coordinate remains an ORIGINAL independent cap-one coordinate. No moment, bounded-support, connected-support, log-concavity, Gaussianity, post-rotation independence, arbitrary-joint coarea bound, coefficient-small random-error deletion, or uniformly good single minor is assumed.

## 1. First unpaid implication after this run

The first unpaid B08 implication is now

`QFORM-NEARSINGULAR-EXACTMATCH-DIFFUSE-THIRD-CURVATURE-COMPILER-v1`.

At spectral scale `L`, the new router below pays **every invertible physical 2x2 principal block with least singular value at least `L/64` by `<619/L`**. In the current common-plane descendant, the newest rank-free first-compound receiver additionally pays every nonzero pair-Schur crossing `N` once

`b epsilon^2 nu >= 4.28*10^(-7)`,                              (1.1)

where

`b=s_1(B)/L`, `epsilon=sigma_min(B)/L`, `nu=||N||_F/L`.

Thus the genuinely unpaid common-plane chamber is quantitatively narrow:

`epsilon<1/64`,
`b epsilon^2 nu <4.28*10^(-7)`,                                (1.2)

including the exact endpoint `N=0`. The stress family in Section 5 shows that (1.2) is not empty even when both arm areas stay exactly one and **every** physical two-coordinate principal block lies below the `1/64` gate. In that family the missing third curvature is a diffuse same-bank square. Therefore a successful next receiver must aggregate that third curvature before paying a reciprocal near-singular hub factor; it cannot demand a well-conditioned physical pair.

## 2. Pinned inputs actually used

### 2.1 Required fixed source

The owner-required fixed source is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

I read `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. Three completed statements are used below at equations:

1. **Schur spectral retention.** If `A` has at least `k` eigenvalues of modulus at least one and an invertible physical two-coordinate principal block `B` is completed, `A/B` retains at least `k-2` eigenvalues of modulus at least one. Scaling gives the same statement at any spectral scale `L`.
2. **Arbitrary-rank quadratic small ball.** For independent cap-one inputs and arbitrary affine terms,

   `sup_w P(|Z^T S Z + ell^T Z+c-w|<rho)
    <=5 (rho/||S||op)^(1/4).`                                  (2.1)

3. **Fresnel--Brascamp--Lieb Theorem F.** For an exact rank-three form whose orthonormal eigenframe has every physical leverage at most `1/2`,

   `||p_Q||infty <=12 |lambda_1 lambda_2 lambda_3|^(-1/3)`,      (2.2)

   and the proof gives an `L^1` characteristic function and hence a continuous `C_0` density.

The physical indefinite-pair logarithmic envelope is the completed pair theorem at

`math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`,
`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

### 2.2 Newest designated-partner state

The newest compatible `account03/B08` report read in this run is

`math-open-problems@5d188af909a000338bfbb259d93eca33ba6124c2`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260923T211945Z-account03-B08-qform-diffuse-r43/REPORT.md`.

It consumes the stronger rank-free first-compound theorem from `account01/B04` and records the current common-plane identity. Its r45 predecessor is

`math-open-problems@a3624cdb18747a63e9e6991d83233c30e1664f4b`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260923T190424Z-account03-B08-qform-diffuse-r45/REPORT.md`.

In that state two original physical hubs have block `B`; two disjoint product banks have full-row-rank arm matrices `M_1,M_2`; and

`S_r=s_1(M_r)s_2(M_r)>L^2/(64 sqrt(896)), r=1,2`.               (2.3)

The physical cross bank has the exact decomposition

`C=M_1^T R_c M_2+T`, `P_1TP_2=0`,                              (2.4)

where `P_r` projects onto the row space of `M_r`. After exact completion of an invertible physical hub pair,

`N=M_1^T(R_c-B^(-1))M_2+T`.                                    (2.5)

The strongest new analytic receiver I use is `account01/B04` r20,

`math-open-problems@202572bac02518f01c712763376277ba45ab5e0b`,
`.../account01/B04/20260923T212739Z-account01-B04-QFORM-auto11-r20/REPORT.md`,

which proves, with no rank assumption on `N`,

`||p_Q||infty
 <=15.829 (D kappa)^(-1/4) ||N||_F^(-1/4),`                    (2.6)

for an invertible indefinite physical pair, where `D=|det B|` and `kappa=sigma_min(B)`. Arbitrary same-bank quadratic terms and outside affine terms are retained.

## 3. New full-matrix physical-pair gate

### Theorem 3.1 — `QFORM-THREEEIG-PHYSICAL-PAIR-619-GATE-v1`

Let `A` be real symmetric with at least three eigenvalues of modulus at least `L>0`, and let `B=A[H,H]` be any invertible `2x2` principal block on two ORIGINAL coordinates. If

`sigma_min(B)>=L/64`,                                           (3.1)

then for every independent cap-one product source the full ambient quadratic form, including arbitrary remaining spectrum and arbitrary affine terms, has an essentially bounded density satisfying

`boxed: ||p_Q||infty <619/L.`                                   (3.2)

If `B` is definite, the stronger bound `<202/L` holds.

### Proof: definite pair

For a definite pair the completed two-coordinate ellipse estimate gives

`||p_Q||infty <=pi/sqrt(|det B|).`                              (3.3)

For a `2x2` invertible matrix, `sqrt(|det B|)>=sigma_min(B)`. Hence (3.1) gives

`||p_Q||infty <=64pi/L <202/L`.                                 (3.4)

Outside coordinates are simply conditioned; the estimate is uniform in the induced affine shift.

### Proof: indefinite pair

Put

`D=|det B|`, `kappa=sigma_min(B)`.                              (3.5)

Complete the pair exactly. The residual variables are still original independent coordinates and the residual quadratic coefficient is the Schur complement

`S=A/B`.                                                         (3.6)

Apply the fixed-source Schur spectral-retention lemma to `A/L`. Since `A` has three absolute eigenvalues at least `L`, `S` has at least one absolute eigenvalue at least `L`, so

`||S||op>=L`.                                                    (3.7)

The fixed-source arbitrary-rank small-ball theorem (2.1), including all induced affine terms, therefore gives uniformly in the center `w`

`P(|R-w|<rho)<=min(1,5(rho/L)^(1/4)).`                          (3.8)

The physical-pair logarithmic envelope says that for every `r>0`, almost everywhere in `s`,

`p_Q(s)
 <=2sqrt(2)/r
  +D^(-1/2) E log_+(2r^2/(kappa|s-R|)).`                        (3.9)

Set

`a=2r^2/kappa`,
`c=5(a/L)^(1/4)`.                                               (3.10)

Layer cake and (3.8) yield

`E log_+(a/|s-R|)
 <=int_0^infty min(1,c e^(-u/4))du.`                            (3.11)

When `c>=1`, the right side is exactly bounded by

`4log c+4=4(1+log c)`.                                          (3.12)

Choose the optimizing scale

`r=sqrt(2) kappa`.                                               (3.13)

Then

`c=5sqrt(2)(kappa/L)^(1/4)`.                                   (3.14)

Under (3.1), `c>=5/2`, so (3.12) applies. Also `sqrt(D)>=kappa`. Substitution into (3.9) gives

`||p_Q||infty
 <=[6+4log(5sqrt(2)(kappa/L)^(1/4))]/kappa.`                    (3.15)

Write `y=kappa/L`. The function

`F(y)=[6+4log(5sqrt(2)y^(1/4))]/y`                              (3.16)

is decreasing for `y>=1/64`: its numerator equals `6+4log(5sqrt(2))+log y`, so

`F'(y)=[1-(6+4log(5sqrt(2))+log y)]/y^2<0`                      (3.17)

on that interval. Hence the worst endpoint is `y=1/64`, where

`F(1/64)=64[6+4log(5/2)]
       =618.5704273597837... <619.`                              (3.18)

Equations (3.15)-(3.18) prove (3.2). QED.

### Meaning of the gate

This theorem is genuinely full-matrix: it does not assume that the Schur residual has rank one, rank two, a diagonal basis, or any small tail. The entire complementary spectrum is retained through (3.7)-(3.8). It turns the current localized/diffuse hybrid into an explicit actual physical gate:

- a physical pair with `sigma_min>=L/64` is paid by `<619/L`;
- otherwise **every** physical `2x2` principal block has least singular value `<L/64` (or is singular).

Continuity is not claimed from this logarithmic/small-ball proof.

## 4. Quantifying the newest common-plane survivor

Assume now the partner common-plane state (2.3)-(2.5) and that the selected physical pair is invertible indefinite. Define the dimensionless quantities

`b=s_1(B)/L`,
`epsilon=kappa/L`,
`nu=||N||_F/L`.                                                 (4.1)

Because `D=s_1(B)kappa`,

`D kappa=b epsilon^2 L^3`,
`||N||_F=nu L`.                                                  (4.2)

The rank-free partner receiver (2.6) becomes

`boxed:
 ||p_Q||infty
 <=15.829 (b epsilon^2 nu)^(-1/4) L^(-1).`                      (4.3)

Thus the same `<619/L` benchmark is reached whenever

`b epsilon^2 nu
 >=(15.829/619)^4
 =4.2761341...*10^(-7).`                                        (4.4)

It is safe to use the rounded threshold

`b epsilon^2 nu >=4.28*10^(-7)`.                               (4.5)

Combining Theorem 3.1 and (4.5), every still-unpaid common-plane state obeys (1.2).

There is also an exact orthogonality identity that makes `nu` transparent. Since

`M_1^T(R_c-B^(-1))M_2=P_1[M_1^T(R_c-B^(-1))M_2]P_2`            (4.6)

and `P_1TP_2=0`, the two summands in (2.5) are Frobenius-orthogonal. Hence

`boxed:
 ||N||_F^2
 =||M_1^T(R_c-B^(-1))M_2||_F^2+||T||_F^2.}`                    (4.7)

Consequently the nonzero-tail and nonzero-Schur-mismatch branches are not separate analytic debts any longer: their combined first-compound energy is exactly what (4.3) spends. What survives (at this benchmark) is simultaneous near-singularity of the hub and near-vanishing of the entire post-Schur physical crossing.

## 5. Exact target-valid stress family inside the remaining endpoint

The preceding reduction would be much weaker if the exact-match state were an algebraic fiction. It is not. The following family simultaneously has:

- exactly three nonzero target eigenvalues;
- robust arm areas equal to one;
- exact Schur match `N=0`;
- arbitrarily small hub-pair conditioning;
- every physical `2x2` principal block below the `1/64` gate;
- arbitrary cap-one product sources; and
- nevertheless a uniform continuous density bound from the required fixed-source Theorem F.

### Construction — `QFORM-EXACTMATCH-DIFFUSE-THIRD-CURVATURE-STRESS-v1`

Let `m=2^q` and choose three distinct normalized Sylvester-Hadamard rows

`r_1,r_2,q in R^m`,                                              (5.1)

so they are orthonormal and every coordinate has magnitude `m^(-1/2)`. Put

`M=[r_1^T; r_2^T] in R^(2xm)`,                                  (5.2)

so

`MM^T=I_2`, `Mq=0`, `s_1(M)s_2(M)=1`.                           (5.3)

Fix `0<epsilon<1/64` and set

`B=diag(epsilon,-epsilon)`.                                     (5.4)

On original coordinates partitioned as

`H (2 coordinates)`, `J_1 (m coordinates)`, `J_2 (m coordinates)`,

define

`K=M^T B^(-1)M`                                                  (5.5)

and

`A_(m,epsilon)=
 [[ B,    M,          M        ],
  [ M^T,  K+q q^T,    K        ],
  [ M^T,  K,          K        ]].`                              (5.6)

This is exactly the common-plane model with

`M_1=M_2=M`, `R_c=B^(-1)`, `T=0`.                               (5.7)

After completing the selected hub pair, the Schur residual is simply

`diag(q q^T,0)` on `J_1 direct_sum J_2`;                        (5.8)

in particular the pair-Schur crossing is

`N=0`.                                                           (5.9)

The third curvature has not vanished: it is the diffuse same-bank square `(q^T X_(J_1))^2`.

### Exact spectrum

Put

`F=[I_2; M^T B^(-1); M^T B^(-1)]`.                              (5.10)

Then the part of (5.6) without `q q^T` is

`A_0=F B F^T`.                                                   (5.11)

Using `MM^T=I_2` and `B^(-2)=epsilon^(-2)I_2`,

`F^T F=I_2+2B^(-2)=(1+2/epsilon^2)I_2`.                         (5.12)

Moreover the embedded vector `q_tilde=(0_H,q,0)` is unit and orthogonal to both columns of `F`, because `Mq=0`. Thus the exact nonzero spectrum of (5.6) is

`boxed:
 spec_nonzero(A_(m,epsilon))
 ={ Lambda,-Lambda,1 },
 Lambda=epsilon+2/epsilon.`                                     (5.13)

For `0<epsilon<=1`, `Lambda>=3`; hence (5.6) is a genuine target matrix with three eigenvalues of modulus at least one and no additional nonzero spectrum.

### Every physical pair can be below the new gate

The hub pair itself has least singular value `epsilon<1/64`. For a hub-light physical pair, test the unit vector on the light coordinate. Since the arm entry has magnitude `m^(-1/2)` and every light diagonal has magnitude at most `1/m`,

`sigma_min(pair)
 <=sqrt(1/m+1/m^2)
 <=sqrt(2/m).`                                                   (5.14)

For two light coordinates, note that

`K_jk=(r_1j r_1k-r_2j r_2k)/epsilon`,
`|K_jk|<=2/(epsilon m)`,
`K_jj=0`,                                                        (5.15)

and the added `q q^T` contributes at most `1/m` entrywise. Hence every light-light `2x2` principal block has

`||pair||op<=6/(epsilon m)`.                                    (5.16)

Therefore if

`m>max(8192,384/epsilon)`                                       (5.17)

(and `m` is a Hadamard power of two), then **every** physical `2x2` principal block of `A_(m,epsilon)` has least singular value `<1/64`.

For example, at

`epsilon=1/128`, `m=65536`,                                     (5.18)

the three deterministic upper bounds are

`0.0078125`, `0.00390628`, and `0.01171875`,                    (5.19)

all strictly below `1/64=0.015625`.

Thus Theorem 3.1 is a genuine router, not a solution: a target-valid exact-match diffuse state survives it.

## 6. Required fixed-source result applied to the actual obstruction family

The family (5.6) is not a QFORM counterexample. The fixed-source Theorem F pays it uniformly and transparently.

Normalize the two columns of `F` in (5.10) and append `q_tilde`. By (5.12), these are an orthonormal eigenframe for the three nonzero eigenvalues. Its physical leverage is explicit.

For either hub coordinate,

`ell_H=1/(1+2/epsilon^2)
     =epsilon^2/(epsilon^2+2)
     <=1/3`.                                                      (6.1)

For a `J_1` coordinate,

`ell_(J_1,j)
 =1/m + 2/[m(epsilon^2+2)]
 <=2/m`.                                                         (6.2)

For a `J_2` coordinate,

`ell_(J_2,j)=2/[m(epsilon^2+2)]<=1/m`.                           (6.3)

Hence for `m>=4` every leverage is at most `1/2`. Theorem F applies to the **whole exact rank-three matrix** (5.6), without rotating the random inputs, and gives

`boxed:
 ||p_(X^T A_(m,epsilon) X)||infty
 <=12 Lambda^(-2/3),
 Lambda=epsilon+2/epsilon.}`                                    (6.4)

In particular this is universally at most

`12*3^(-2/3)<5.77` for `0<epsilon<=1`,                           (6.5)

and the Fourier proof supplies a continuous `C_0` density. At the concrete stress point (5.18),

`Lambda=256.0078125`,
`||p||infty<=0.297632`.                                          (6.6)

This is the required fixed-source theorem applied to a real target-valid inequality/obstruction. It also isolates the missing mechanism: the exact-match branch can be paid by **collective diffuse third-curvature geometry even when every physical two-coordinate pivot is weak**.

## 7. What was actually learned about the hybrid

The combination of Theorem 3.1, the newest partner/rank-free receiver, and the stress family yields a cleaner B08 endpoint than the previous rank-one/rank-two mismatch split:

1. **Well-conditioned physical pair:** paid full-ambient by `<619/L`, regardless of the rest of the matrix.
2. **Near-singular pair but nontrivial pair-Schur crossing:** paid by (4.3) once `b epsilon^2 nu` exceeds `4.28e-7` at the same benchmark.
3. **Near-singular plus tiny/zero pair-Schur crossing:** genuine residual endpoint. In exact match, the third target curvature can live as diffuse same-bank curvature, as (5.6) proves. It cannot be manufactured by pair innovation, and it cannot be discarded.

The remaining receiver should therefore combine a near-singular two-hub geometry with a **collective same-bank spectral direction** before paying reciprocal `kappa`. The target-valid family (5.6) gives a mandatory regression test: any proposed compiler that blows up as `epsilon->0` while `m` grows as in (5.17) is missing the successful diffuse aggregation already captured by Theorem F.

The general arbitrary-matrix problem is still open because a general near-singular exact-match state need not have the clean exact-rank-three/eigenframe leverage structure of (5.6); it may carry arbitrary complementary spectrum, non-diagonal same-bank curvature, and additional conditioned affine terms. Small operator tails cannot be deleted under the source assumptions.

## 8. Correction boundary and scope checks

- No post-rotation independence is used. Spectral vectors in Section 6 are used only inside the proved Fresnel--Brascamp--Lieb theorem; the product law remains in original coordinates.
- No uniform scalar quadratic-phase decay is asserted. The only Fourier decay used is the completed multidimensional Theorem F on its exact leverage hypotheses.
- No arbitrary-joint coarea inequality is used.
- No worst conditional projection-density moment is used.
- No coefficient-small quadratic perturbation is dropped.
- No single physical minor is asserted to be uniformly good; Section 5 explicitly constructs a target family in which all physical pair gates fail.
- The arbitrary-rank small-ball theorem is used only after exact Schur completion, on the full residual with its actual operator norm supplied by the retained eigenvalue.
- Continuity is separate: Theorem 3.1 and (4.3) prove essential boundedness only; the explicit stress family gets continuity from Theorem F.

## 9. Deterministic constants / regression values

The exact calculations used in this report give

`64[6+4log(5/2)] = 618.5704273597837`,                           (9.1)

`(15.829/619)^4 = 4.276134139674674*10^(-7)`,                   (9.2)

and for `(epsilon,m)=(1/128,65536)`:

`hub pair upper scale       =0.0078125`,
`hub-light sigma_min bound =0.00390627980221`,
`light-light op bound      =0.01171875`,
`max hub leverage          =3.05166468308*10^(-5)`,
`max J_1 leverage          =3.05171124779*10^(-5)`,
`Lambda                    =256.0078125`,
`Theorem-F density bound   =0.297631641944`.

These arithmetic checks support the displayed constants; the universal arguments are the proofs above.

## 10. Status

This run proves a new quantitative full-ambient physical-pair router, narrows the current common-plane hybrid to the near-singular/near-exact-match chamber, and supplies a target-valid diffuse exact-match family that survives every physical-pair gate while being uniformly paid by the required fixed source. It does **not** prove or disprove the unrestricted conjecture.

First next step: prove `QFORM-NEARSINGULAR-EXACTMATCH-DIFFUSE-THIRD-CURVATURE-COMPILER-v1` with arbitrary complementary spectrum and arbitrary same-bank curvature, reducing to Theorem F on the stress family (5.6) without assuming independence after rotation.
