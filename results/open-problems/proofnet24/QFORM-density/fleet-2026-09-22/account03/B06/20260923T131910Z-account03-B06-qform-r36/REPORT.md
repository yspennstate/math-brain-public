SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B06, 2026-09-23T13:19:10Z.
attacking: no-fresh-scalar shared-bank curved-fiber payment: absorb a translated square built from the same original-coordinate product bank into the scalar discriminant before any conditional-density or fiber-supremum loss.

# account03/B06 r36 — same-bank translated-square discriminant invariance

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: curved fiber integration  
Status: **NEW SUPPORTING THEOREMS + SAME-BANK TARGET COLLAR / FULL QFORM OPEN**  
Continuity: **not proved by the new general theorems; only essential boundedness is asserted below.**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh state and source-valid inputs

At startup the authorized `yspennstate/math-research-brain` main branch was read fresh. OWNER CONTROL remained revision `2026-09-22.15`, programme revision `2026-09-22.5`, with QFORM as the sole mathematical target. `AGENTS.md`, `scheduled_tasks/README.md`, `fleet.json`, `roles.json`, `PROTOCOL.md`, the QFORM `MANIFEST.json`, `CURRENT_RESEARCH.md`, `CLAIMS.json`, live `CORRECTION_INBOX.json`, `MEMORY_PROTOCOL.md`, and the account03/B06 assignment were read. The full conjecture remained marked OPEN.

The live corrections used here forbid law-uniform pointwise quadratic-phase decay, post-rotation independence, arbitrary-joint rank-three coarea, positive moments of worst conditional projection caps, unrestricted fiber suprema, and extraction of one uniformly good physical minor. The argument below keeps the original product coordinates until after the curved scalar root calculation.

The exact designated partner directory `account04/B06` remained absent in both the brain handoff tree and the canonical QFORM mathematics tree, so no theorem from that slot is fabricated. A compatible completed account04/B18 theorem is applied at an actual equation in Section 4.

The source-valid inputs actually used are:

1. `QFORM-RANK2-AFFINE-HALF-RIESZ-v1`, canonical source
   `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`,
   `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.
   If `P` has two orthonormal columns, `Lambda` is invertible symmetric `2 x 2`, `b` is any original-coordinate vector, and the inputs are independent with density caps one, then

   `sup_t E |(P^T Z)^T Lambda(P^T Z)+b^T Z-t|^(-1/2)
      <=128 |det Lambda|^(-1/4)`.

   When `b` lies in `range(P)`, the constant improves to `16 sqrt(30)`.

2. account03/B06 r32, canonical source
   `yspennstate/math-open-problems@9583647ef39bb355508b8f8fb49f05ded8b594f2`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260923T094916Z-account03-B06-qform-r32/REPORT.md`.
   Its affine null-scalar weak-`L^(3/2)` theorem says: if `X` has density cap `L`, is independent of a possibly dependent pair `(C,D)` of joint density cap `M`, and `b g !=0`, then

   `2 b X C + a C^2 +2 e C D+g D^2+affine`

   has density cap

   `3(2LM)^(2/3)|b^2 g|^(-1/3)`.

   The same report records the product-projection pair bound

   `||p_(u.Z,v.Z)||_infinity <=2/sqrt(det Gram(u,v))`.

3. account04/B18 `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, canonical source
   `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T113729Z-account04-B18-qform-r1/REPORT.md`.
   If a base `R` has density cap `M` and, conditionally on the base source, a translated scalar has density cap `L`, then

   `R+a V_R^2`

   has density cap

   `2 L sqrt(M/|a|)`.

   It does not require independence between the numerical base value and the translated square.

The new mechanism changes the r35 interface: the final square below contains no fresh scalar direction at all. It is built from the same product bank that supplies the dependent pair.

## 2. Main theorem: same-bank translated square disappears into the discriminant

Let `X` be a real random variable with probability density bounded by `L_X`. Let

`Z=(Z_1,...,Z_m)`

have independent coordinates, each with density at most one. Let `W` be an auxiliary source, and assume `X`, `Z`, and `W` are mutually independent source objects. Let `u,v in R^m` be linearly independent and set

`U=u.Z`, `V=v.Z`,
`G=det Gram(u,v)>0`.                                                  (2.1)

Let `H=H(Z,W)` be completely arbitrary measurable. Put

`Y=gamma X+H`,                                                       (2.2)

with `gamma!=0`. Let `beta,k!=0`, and let `delta_0,theta,zeta` be arbitrary reals. Let `ell(W) in R^m` and `R(W) in R` be arbitrary measurable functions of `W`. Define

`Q = delta_0 Y^2 +2k UY
    + beta (V+theta Y+zeta U)^2
    + ell(W).Z+R(W)`.                                                (2.3)

Define the **effective scalar pivot**

`Delta := delta_0+beta theta^2`.                                    (2.4)

### Theorem 2.1 — `QFORM-SAMEBANK-TRANSLATED-SQUARE-DISCRIMINANT-v1`

If `Delta!=0`, then `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <=128 (L_X/|gamma|)
      [k^2 |beta Delta| G]^(-1/4).`                                 (2.5)

If, almost surely in `W`, `ell(W)` lies in `span{u,v}` (in particular if `ell=0`), then

`boxed:
 ||p_Q||_infinity
 <=16 sqrt(30) (L_X/|gamma|)
      [k^2 |beta Delta| G]^(-1/4).`                                 (2.6)

The constants are completely independent of `theta` and `zeta` except through the single scalar `Delta`.

### Proof

Expand the shared-bank square. Put

`C=(k+beta theta zeta)U+beta theta V`,
`D=V+zeta U`.                                                       (2.7)

Then exactly

`Q=Delta Y^2+2CY+beta D^2+ell(W).Z+R(W)`.                           (2.8)

Fix `(Z,W)=(z,w)` and a target value `t`. Since the original scalar `X` is genuinely independent of `(Z,W)`, the conditional variable

`Y=gamma X+H(z,w)`

has density at most

`L_Y=L_X/|gamma|`.                                                   (2.9)

The equation `Q=t` is a scalar quadratic in `Y`. Its discriminant divided by four is

`mathcal D
 = C^2+Delta[t-beta D^2-ell(w).z-R(w)]`.                    (2.10)

At each simple root the absolute derivative is `2 sqrt(mathcal D)`. Summing the two root contributions therefore gives

`p_(Q|Z,W)(t|z,w)
 <= L_Y 1_{mathcal D>0} mathcal D^(-1/2)`.                          (2.11)

The crucial fact is already visible: the arbitrary same-bank translation `H(Z,W)` has disappeared before any fiber supremum or conditional projection density is introduced.

Write the two coefficient vectors in the `(U,V)` plane as

`w=(k+beta theta zeta, beta theta)`,
`q=(zeta,1)`.                                                       (2.12)

The quadratic part of `mathcal D` in `(U,V)` is

`(U,V) [ w w^T-Delta beta q q^T ] (U,V)^T`.                         (2.13)

For two vectors in dimension two,

`det(w w^T-c q q^T)=-c det(w,q)^2`.                                (2.14)

Here an exact cancellation occurs:

`det(w,q)
 =(k+beta theta zeta)-beta theta zeta
 =k`.                                                               (2.15)

Hence

`det[ w w^T-Delta beta q q^T ]=-beta k^2 Delta`.                    (2.16)

Now choose an orthonormal physical frame `P` spanning `span{u,v}`. Passing from `(U,V)` to `P^T Z` multiplies the determinant by the squared area of `(u,v)`, namely

`G=det Gram(u,v)`.                                                   (2.17)

Thus the exact rank-two determinant currency left after the scalar root calculation is

`|det Lambda|=k^2 |beta Delta| G`.                                  (2.18)

The term `-Delta ell(w).Z` in (2.10) is an arbitrary original-coordinate affine term. Apply `QFORM-RANK2-AFFINE-HALF-RIESZ-v1` to (2.11), uniformly in the scalar shift `Delta(R(w)-t)`, obtaining (2.5). If `ell(w)` lies in `span{u,v}`, the affine term lies in the rank-two projection range and the improved `16 sqrt(30)` source bound gives (2.6). Averaging in `W` preserves the estimate. QED.

### Interpretation

The determinant identity (2.16) is the weighted curved-fiber replacement sought in this run. The square `beta(V+theta Y+zeta U)^2` is allowed to share **all** of `Y` and `U`; no scalar from a disjoint bank is reserved for final smoothing. Its coupling shear does not degrade the residual curved determinant. It changes only the effective pivot `Delta=delta_0+beta theta^2`; the entire `zeta` dependence cancels from the area currency.

## 3. Effective-pivot cancellation: exact in-plane payment or genuine third curvature

The only singular point of Theorem 2.1 is the exact algebraic cancellation

`Delta=0`.                                                          (3.1)

At this endpoint (2.8) becomes

`Q=2CY+beta D^2+ell(W).Z+R(W)`.                                    (3.2)

The map from `(U,V)` to `(C,D)` has coefficient matrix

`T=[[k+beta theta zeta, beta theta],
    [zeta,                1        ]]`,                              (3.3)

and therefore

`det T=k`,
`det Gram(c,d)=k^2 G`,                                               (3.4)

where `c,d` are the original-coordinate coefficient vectors of `C,D`.

### Theorem 3.1 — `QFORM-EFFECTIVE-PIVOT-CANCELLATION-INPLANE-v1`

Assume `Delta=0`. Suppose that for almost every `W=w`, the shared translation and affine term are contained in this same physical pair plane:

`H=a(w)C+b(w)D+h_0(w)`,
`ell(w).Z=m(w)C+n(w)D`.                                              (3.5)

Then `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <=3*4^(2/3) L_X^(2/3)
   [k^2 gamma^2 |beta| G]^(-1/3).`                                  (3.6)

### Proof

Condition on `W=w`. Expanding `2C(gamma X+H)` turns (3.2) into

`2 gamma X C + alpha C^2+2 eta C D+beta D^2+mu C+nu D+constant`,     (3.7)

for coefficients depending on `w`. The pair `(C,D)` is independent of `X` as a pair and is a linear image of the untouched product vector `Z`. By the product-projection pair theorem and (3.4),

`||p_(C,D)||_infinity <=2/(|k| sqrt(G))`.                            (3.8)

Apply the affine null-scalar weak-`L^(3/2)` theorem from r32 with scalar coefficient `gamma` and `D^2` coefficient `beta`. It gives exactly (3.6), uniformly in `w`. QED.

Thus cancellation of the scalar pivot does not recreate the logarithmic rank-two obstruction when all shared translations stay in the paid plane.

### Theorem 3.2 — `QFORM-EFFECTIVE-PIVOT-CANCELLATION-TRANSVERSE-CURVATURE-v1`

Still assume `Delta=0`, and now suppose the shared translation is linear in the product bank. Decompose its coefficient vector as

`h=a c+b d+w`,
`w perpendicular to span{c,d}`.                                    (3.9)

Let `W_0=w.Z`. The quadratic-in-`Z` portion of `2CH+beta D^2` has exact rank three whenever `w!=0`, and its signed pseudodeterminant is

`boxed:
 pdet(B_h)=-beta k^2 G ||w||^2.`                                   (3.10)

### Proof

In the three linear coordinates `(C,D,W_0)`, the quadratic matrix is

`S=[[2a,b,1],
    [ b,beta,0],
    [ 1,0,0]]`.                                                     (3.11)

A direct expansion gives

`det S=-beta`.                                                       (3.12)

The three original-coordinate coefficient vectors are `c,d,w`, with `w` orthogonal to the first two. Hence

`det Gram(c,d,w)
 =det Gram(c,d) ||w||^2
 =k^2 G ||w||^2`.                                                    (3.13)

For a full-column-rank coefficient matrix `C_0`, the nonzero eigenvalue product of `C_0 S C_0^T` equals `det(S)det(C_0^T C_0)`. Equations (3.12)-(3.13) give (3.10). QED.

So a genuinely transverse same-bank translation is not a perturbation to delete: at the exact effective-pivot cancellation it manufactures an explicit third-curvature volume. Existing diffuse-rank-three/ridge theorems may pay this when their leverage/spectral-balance hypotheses hold. Their failure is an explicit high-leverage or spectral-imbalance branch, not a loss of the translation.

## 4. Completed account04 theorem applied at an actual inequality

There is a sharper branch of Theorem 2.1 when

`beta Delta<0`                                                      (4.1)

and `ell(W)` lies in `span{u,v}`. Complete the scalar square in (2.8):

`Q
 =Delta (Y+C/Delta)^2
  + [ beta D^2-C^2/Delta+ell(W).Z+R(W) ]`.                          (4.2)

The bracketed base is a definite rank-two quadratic polynomial of `(U,V)`. Its `2 x 2` quadratic determinant in `(U,V)` coordinates is

`-beta k^2/Delta>0`.                                                (4.3)

The pair `(U,V)` has joint density cap `2/sqrt(G)`. The elementary definite two-dimensional coarea bound therefore gives the bracketed base density cap

`M <= 2 pi sqrt(|Delta|)/( |k| sqrt(|beta| G) )`.                   (4.4)

Conditioned on the base value, the square coordinate

`Y+C/Delta
 =gamma X+[H+C/Delta]`                                              (4.5)

is a mixture of translations of the genuinely independent scalar `gamma X`, hence has conditional density cap `L_X/|gamma|`.

Apply the completed account04/B18 dependence-safe square theorem to the **actual identity** (4.2). It gives

`boxed:
 ||p_Q||_infinity
 <=2 sqrt(2pi) (L_X/|gamma|)
      [k^2 |beta Delta| G]^(-1/4).`                                 (4.6)

This theorem does not require the numerical base and translated square to be independent. The exact designated `account04/B06` artifact was absent, so (4.6) is credited only to the compatible completed account04/B18 result actually used.

## 5. A genuinely all-same-bank target family

The new theorem applies to a family in which the final smoothing square has **no disjoint source bank**.

Let `t,u,v in R^m` be orthonormal deterministic vectors, let `Z_1,...,Z_m` and `X_0` be independent cap-one original coordinates, and put

`T=t.Z`, `U=u.Z`, `V=v.Z`,
`Y=sqrt(c) X_0+sqrt(1-c) T`,                                        (5.1)

with `c in (0,1)`. The deterministic coefficient vectors of `(Y,U,V)` in the original coordinate space are orthonormal, but the random variables are generally dependent because `T,U,V` use the **same** product bank `Z`.

For `delta>=0`, let `k=sqrt(1+delta)` and define

`Q^+ = delta Y^2+2k UY+(V+theta Y+zeta U)^2`.                       (5.2)

For `eta>=0`, let `k=sqrt(1+eta)` and define

`Q^- = -eta Y^2+2k UY+(V+theta Y+zeta U)^2`.                        (5.3)

When `theta=zeta=0`, the spectra in the orthonormal frame `(Y,U,V)` are respectively

`{1+delta,-1,1}` and `{1,-(1+eta),1}`.                              (5.4)

Let

`rho=sqrt(theta^2+zeta^2)`.                                         (5.5)

Relative to the uncoupled matrices, the added shear has matrix

`Delta_r=
 [[theta^2,theta zeta,theta],
  [theta zeta,zeta^2,zeta],
  [theta,zeta,0]]`.                                                  (5.6)

Its eigenvalues are exactly

`0, (rho^2 +/- rho sqrt(rho^2+4))/2`,                               (5.7)

so

`epsilon(rho)=||Delta_r||op
 =(rho^2+rho sqrt(rho^2+4))/2<1`

if and only if

`rho<1/sqrt(2)`.                                                     (5.8)

Weyl therefore leaves all three coupled eigenvalue moduli at least `1-epsilon(rho)`. Dividing the whole form by `1-epsilon(rho)` gives a genuine target matrix with all three eigenvalue moduli at least one, and the density norm is multiplied by `1-epsilon(rho)<=1`. Thus any bound below for the unscaled form is automatically a valid bound for the target-valid rescaling.

For this family

`G=1`, `L_X=1`, `gamma=sqrt(c)`,                                    (5.9)

and the effective pivot is

`Delta_+=delta+theta^2`,
`Delta_-=theta^2-eta`.                                               (5.10)

Take the live near-coloop collar

`c>63/64`.                                                          (5.11)

Whenever

`|Delta_+|>=1/64`

or

`|Delta_-|>=1/64`,                                                   (5.12)

Theorem 2.1 with the improved in-range constant gives, using `k^2>=1`,

`boxed:
 ||p_Q||_infinity
 <16 sqrt(30) sqrt(64/63) 64^(1/4)
 =249.8304186748...<249.831.`                                       (5.13)

On the opposite-sign negative-family branch

`Delta_-<=-1/64`,                                                    (5.14)

Section 4 instead gives the much sharper account04-spliced estimate

`boxed:
 ||p_Q||_infinity
 <2 sqrt(2pi) sqrt(64/63) 64^(1/4)
 =14.2917244947...<14.292.`                                         (5.15)

These are exact target-valid all-same-bank examples after the harmless spectral scaling (5.8). The final square shares `Y` and `U` and its `V` direction comes from the same original product bank as `T,U`; no fresh smoothing bank remains.

The only unclosed part of this family left by Theorem 2.1 is the explicit effective-pivot slab

`|Delta|<1/64`.                                                      (5.16)

At exact cancellation, Theorems 3.1-3.2 describe the two mechanisms available. In this family the shared translation from `Y` contains the transverse direction `sqrt(1-c)t`; hence the exact rank-three currency (3.10) is nonzero whenever `c<1`, although it can become small as `c` tends to one. No claim is made that this alone supplies a universal bound without a further balance/leverage argument.

## 6. Finite checks and mathematical status

The exact algebra is the proof. A deterministic numerical checker, recorded separately in `CHECKS.md`, performed 1,000 random tests of

`det(w w^T-Delta beta q q^T)=-beta k^2 Delta`

and 1,000 random tests of the transverse pseudodeterminant identity (3.10). Maximum relative discrepancies were respectively `2.21e-14` and `5.25e-13`. It also evaluates the collar constants in (5.13)-(5.15).

This run does **not** prove the full QFORM conjecture and does not prove a continuous representative in the new branches. It removes the specific need for a fresh square scalar whenever the effective pivot `Delta` is quantitatively nonzero, and it turns exact cancellation into either a completed in-plane weak-`L^(3/2)` payment or an explicit rank-three transverse volume.

The next exact B06 debt is:

`QFORM-EFFECTIVE-PIVOT-NEARZERO-TRANSVERSE-BALANCE-v1` — starting from `|Delta|<1/64` and the exact transverse currency `|beta|k^2G||w||^2`, route spectral imbalance or physical high leverage into an aggregate product-bank receiver without deleting the nonzero third direction and without taking a worst conditional fiber density.

Full target: **OPEN / NOT PROVED / NOT DISPROVED.**  
Universal continuity: **OPEN.**
