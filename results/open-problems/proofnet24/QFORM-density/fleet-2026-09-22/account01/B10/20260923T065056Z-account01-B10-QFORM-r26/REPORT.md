SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B10, 2026-09-23T06:50:56Z.
attacking: near-null nonzero coloop interpolation via an exact Schur-square/Fresnel factorization, preserving original-coordinate product structure.

# account01/B10 r26 — Schur-aligned leaf Fresnel interpolation for a nonzero near-null pivot

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: arbitrary exact-rank-three coupled case  
Status: `ESSENTIAL_STEP_APPLIED / NEW_SUPPORTING_THEOREM / NEW UNIFORM COLLAR EXIT / FULL TARGET OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted QFORM conjecture remains OPEN. This report proves a new nonzero-pivot exact-rank-three theorem whose constant is independent of the size of the physical pivot, applies it to a genuine near-coloop collar, and uses the latest designated-partner account02/B10 construction and the newest volume-stability theorem at actual density inequalities. No post-rotation independence, arbitrary-joint coarea inequality, worst conditional density, moment/support assumption, or law-uniform pointwise oscillatory decay is used. The new theorem gives a continuous density in its scope.

## 1. Fresh source boundary


Current required sources consumed in this run include:

1. Claude's Fresnel--Brascamp--Lieb package
   `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`
   `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`.
   Its twisted one-dimensional Fourier `L^p` bound and geometric BL argument are used below, but in a new **Schur-aligned leaf frame** where the physical hub is deliberately not charged an `L^p` exponent.

2. The newest volume-stability package
   `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`
   `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`
   and `PEER_TAIL_EXTENSION.md`.
   Its baseline `M=M0+E` theorem is applied in Section 7 to the designated partner's explicit target family.

3. Latest completed designated-partner `account02/B10` result found at the source refresh:
   `yspennstate/math-open-problems@328f5b408292534e743f31c7d2114b55b3aa0699`
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B10/20260923T055259Z-account02-B10-QFORM-auto11/REPORT.md`.
   It proves a constant hub Pluecker packet in the high-slope near-coloop survivor and supplies a target-valid local-certificate-collapse family with spectrum `{1,1,-1}`. The family is used quantitatively below.

The exact-null scalar/dependent-pair endpoint from account02/B16 remains paid at
`5bf3d5e6765ecd1dd091fc7d862f6f04211c530f`; it is not reproved here. The present mechanism requires a nonzero physical pivot.

## 2. Exact Schur-square factorization in ORIGINAL coordinates

Let `A` be a real symmetric matrix of exact rank three. Single out original coordinate `0` and write

`A = [[a,g^T],[g,B]]`,                                              (2.1)

where `a=A_00 !=0`. Since congruence elimination at a nonzero scalar pivot preserves rank,

`S:=B-gg^T/a`                                                       (2.2)

has rank exactly two. Choose `V` with two orthonormal columns and an invertible symmetric `2x2` matrix `L` such that

`S=V L V^T`.                                                        (2.3)

Then, identically in the original random coordinates,

`Q=X^T A X
   =(1/a)(aX_0+g^T X_L)^2+(V^T X_L)^T L(V^T X_L)`.                 (2.4)

Arbitrary affine and constant terms may be appended; they only translate the one-dimensional Fourier arguments used below.

Introduce deterministic coefficient rows in `R^3`

`b_0=(a,0,0)`,
`b_j=(g_j,v_j)`, `j in L`,                                        (2.5)

and the diagonal spectral matrix

`M=diag(1/a,L)`.                                                    (2.6)

Then

`A=\widetilde R M \widetilde R^T`,                                 (2.7)

where `\widetilde R` has rows `b_i`. Define

`Gamma=sum_i b_i b_i^T`,
`H=sum_(j in L)b_j b_j^T=Gamma-b_0b_0^T`.                          (2.8)

Because `A` has exact rank three and `M` is invertible, `Gamma>0`. Put

`c=b_0^T Gamma^(-1)b_0`.                                           (2.9)

This is exactly the physical leverage of coordinate `0` in `range(A)`: any two full-column-rank factorizations of the same rank-three range differ by an invertible deterministic column map, and leverage is invariant under such a map.

If `c<1`, the determinant lemma gives

`boxed: det H=(1-c)det Gamma.`                                     (2.10)

Let

`D=product of the three nonzero eigenvalue magnitudes of A`.

Writing `\widetilde R=U Gamma^(1/2)` with `U^T U=I_3`, the nonzero spectral matrix of `A` is congruent to `Gamma^(1/2)M Gamma^(1/2)`. Hence

`boxed: D=|det M| det Gamma=|det(L/a)|det Gamma.`                   (2.11)

Combining (2.10)-(2.11),

`boxed: |det(L/a)| det H=D(1-c).`                                  (2.12)

This exact cancellation is the reason the theorem below is independent of the small nonzero scalar pivot `a`.

## 3. New theorem — Schur-aligned leaf Fresnel bound

### Theorem 3.1 — `QFORM-SCHUR-ALIGNED-LEAF-FRESNEL-v1`

Assume the exact-rank-three setting of Section 2, with `a!=0` and `c<1`. Suppose `H>0` and every **leaf** row satisfies

`boxed: b_j^T H^(-1)b_j <=1/2.`                                    (3.1)

Then for arbitrary independent original-coordinate inputs with densities at most one, and arbitrary affine/constant perturbations, `Q` has a bounded continuous density vanishing at infinity and

`boxed: ||p_Q||_infinity <=12 [D(1-c)]^(-1/3).`                    (3.2)

No lower bound on `|a|` occurs.

### Proof

Fix `t!=0`. Fresnel-linearize the three quadratic squares in (2.4), equivalently the diagonal spectral variables in (2.6). With the same regularization/dominated-convergence argument as the completed Claude Theorem F, the characteristic function obeys

`|phi_Q(t)|
 <= product_(k=1)^3 (4 pi |t mu_k|)^(-1/2)
    integral_(R^3) |hat h_0(b_0 dot z)| product_(j in L)|hat h_j(b_j dot z)| dz`,      (3.3)

where `mu=(1/a,eigenvalues(L))`, and each `h_i(x)=f_i(x)exp(it ell_i x)` for the relevant affine coefficient. Thus `|h_i|=f_i`, `||h_i||_1=1`, and

`|hat h_0|<=1`.                                                     (3.4)

The crucial move is to discard only the **hub Fourier factor**, not a leaf direction. Change variables by `H` in the remaining integral. Put

`q_j=H^(-1/2)b_j`, `d_j=||q_j||^2`.                                (3.5)

Then

`sum_j q_jq_j^T=I_3`, `sum_j d_j=3`, and by hypothesis `d_j<=1/2`.  (3.6)

For `d_j>0` let `u_j=q_j/sqrt(d_j)` and apply geometric Brascamp--Lieb to

`F_j(s)=|hat h_j(sqrt(d_j)s)|^(1/d_j)`.                             (3.7)

The completed twisted one-dimensional Fourier lemma used by Theorem F gives, because `1/d_j>=2`,

`integral |hat h_j(xi)|^(1/d_j) dxi <=4 pi sqrt(d_j)`.              (3.8)

Therefore

`integral F_j <=4 pi`,                                             (3.9)

and geometric BL yields

`integral_(R^3) product_j |hat h_j(q_j dot y)| dy <=(4 pi)^3`.      (3.10)

Undoing the `H` change of variables gives

`integral_(R^3) product_j |hat h_j(b_j dot z)| dz
 <=(4 pi)^3 det(H)^(-1/2)`.                                        (3.11)

Substitute (3.4),(3.11) into (3.3):

`|phi_Q(t)|
 <=(4 pi)^(3/2)|t|^(-3/2)
    [|det(L/a)|det H]^(-1/2)`.                                     (3.12)

By (2.12),

`boxed:
 |phi_Q(t)| <=(4 pi)^(3/2)|t|^(-3/2)[D(1-c)]^(-1/2).`              (3.13)

Together with `|phi_Q|<=1`, this is integrable. If

`K=(4 pi)^(3/2)[D(1-c)]^(-1/2)`,

then

`integral_R min(1,K|t|^(-3/2))dt=6K^(2/3)`.                        (3.14)

Fourier inversion therefore gives

`||p_Q||_infinity
 <=(1/(2pi))6K^(2/3)
 =12[D(1-c)]^(-1/3)`.                                              (3.15)

The `L^1` characteristic function supplies a continuous representative vanishing at infinity. QED.

### Scope check

The proof never rotates the random variables. `V`, `H^(-1/2)` and the Schur factorization act only on deterministic coefficient space. Brascamp--Lieb is applied directly to the independent ORIGINAL leaf coordinates. The hub source is used only through `|hat h_0|<=1`, so no forbidden `L^p` exponent below two is demanded from the near-coloop coordinate.

## 4. The gate in the near-coloop spectral geometry

Return to the current exact-rank-three near-coloop frame

`A=R Lambda R^T`, `R^T R=I_3`,
`r_0=sqrt(c)e`,
`r_j=s_j e+w_j`, `w_j perpendicular e`,                            (4.1)

with

`rho=1-c>0`,
`sum_j s_j^2=rho`,
`sum_j s_jw_j=0`,
`sum_j w_jw_j^T=I_2`.                                               (4.2)

Because the Schur coefficient frame and `R` have the same three-dimensional column range, they differ by an invertible deterministic column map. The leaf leverage in (3.1) is therefore invariant and can be computed from

`G_L=sum_(j!=0) r_jr_j^T=I-r_0r_0^T
     =rho ee^T+P_(e^perp)`.                                        (4.3)

Consequently

`boxed:
 b_j^T H^(-1)b_j
 =r_j^T G_L^(-1)r_j
 =s_j^2/rho+||w_j||^2.`                                            (4.4)

Thus Theorem 3.1 applies whenever

`max_j [s_j^2/rho+||w_j||^2] <=1/2`.                               (4.5)

This is a coefficient condition on original physical rows; it does not assert independence of `(sum s_jX_j, sum w_jX_j)`.

## 5. A uniform near-null collar exit

In the exact-rank-three owner target, the three nonzero eigenvalues have magnitudes at least one, so

`D>=1`.                                                            (5.1)

Hence Theorem 3.1 gives

`||p_Q||_infinity <=12 rho^(-1/3)`.                                (5.2)

The active near-coloop reduction has `rho<1/64`. On the quantitative slice

`1/128 <=rho<1/64`,                                                 (5.3)

condition (4.5) therefore gives the **uniform target-level exit**

`boxed: ||p_Q||_infinity <=12*128^(1/3)<60.477.`                   (5.4)

This is a bounded continuous density conclusion. The estimate is uniform as the physical pivot `a=A_00` tends to zero through nonzero values; only the true coloop parameter `rho` is charged.

The mechanism is genuinely different from the previous B10 regression-deletion runs: no conditional density supremum or reciprocal local minor is used.

## 6. Exact classification of failure of the leaf gate

The current near-coloop predecessor also has

`||w_j||^2<1/4`                                                     (6.1)

for every complementary physical row in the hard survivor. If (4.5) fails at row `j`, then

`s_j^2/rho >1/4`.                                                   (6.2)

Because `sum_j s_j^2/rho=1`, there can be at most three such rows. Therefore the nonzero-pivot near-coloop debt now has the exact alternative:

1. **leaf-diffuse collar:** all normalized leaf leverages are at most `1/2`; if `rho>=1/128`, it is paid by (5.4);
2. **finite heavy-leaf obstruction:** at most three original leaf coordinates violate the gate, each carrying more than one quarter of the total longitudinal leakage;
3. **ultra-near punctured collar:** `0<rho<1/128`, where (5.2) is not yet a universal bound although the exact endpoint `rho=0` is separately paid.

Thus the remaining interpolation problem is no longer a generic high-dimensional leaf cloud.

## 7. Required application of the designated partner and the newest volume theorem

The latest account02/B10 report constructs, for every even `m>=64`, an exact target family with

`spec(A_m)={1,1,-1}`, `D=1`,
`c=127/128`, `rho=1/128`,                                           (7.1)

and rows in the spectral basis `(e,v,u)`:

- hub: `sqrt(127/128)e`;
- `m` mixed rows: `sqrt(1/(256m))e + sigma_j sqrt(15/(16m))v`, with half signs each way;
- `m` pure-longitudinal rows: `sqrt(1/(256m))e`;
- `m` pure-v rows: `sqrt(1/(16m))v`;
- `m` pure-u rows: `m^(-1/2)u`.

The partner proves that all individual physical pivot/pair/triple certificates tend to zero while the aggregate hub Pluecker packet stays `127/128`.

### 7.1 Apply Theorem 3.1 to the partner family

Using (4.4), the normalized leaf leverages are exactly

- mixed: `1/(2m)+15/(16m)=23/(16m)`;
- pure longitudinal: `1/(2m)`;
- pure v: `1/(16m)`;
- pure u: `1/m`.

For `m>=64` all are `<1/2`, so the gate holds. Equation (5.4) gives the **actual full-output inequality**

`boxed:
 ||p_(X^T A_m X)||_infinity
 <=12*128^(1/3)
 =60.4762103949... <60.477.`                                       (7.2)

This is uniform in `m` and applies to arbitrary independent cap-one input laws. It controls both output sides and supplies a continuous density. Hence the designated partner's family is a genuine obstruction to local certificate extraction but **not** to aggregate Schur-aligned Fresnel smoothing.

This is the required equation-level use of the designated account02/B10 result.

### 7.2 Apply the newest volume-stability theorem to the same target

To consume the newest required package independently, split only the partner's three pure leaf banks. Let `I` contain `m/2` rows from each of the pure-longitudinal, pure-v and pure-u banks, and let `J` contain every other coordinate (including the hub and all mixed rows). Then

`G_I=R_I^T R_I=diag(1/512,1/32,1/2)`,
`G_J=I-G_I=diag(511/512,31/32,1/2)`.                               (7.3)

For `M_cross=A[I,J]=R_I Lambda R_J^T`, `R_J` has rank three and therefore the row-space projection of `M_cross` is the column-space projection of `R_I`. Every row in `I` has leverage exactly

`2/m <=1/32<1/2`.                                                   (7.4)

The three nonzero singular values of `M_cross` are those of

`C=G_I^(1/2) Lambda G_J^(1/2)`.                                    (7.5)

The partner's `Lambda` is an orthogonal involution, so

`||C||^2 <= ||G_I|| ||G_J||=(1/2)(511/512)=511/1024`.              (7.6)

Moreover

`|det C|=sqrt(det G_I det G_J)=sqrt(511*31)/32768`.                (7.7)

Thus

`s_3(M_cross)
 >= |det C|/||C||^2
 =sqrt(31)/(32 sqrt(511))
 =0.00769698107... .`                                               (7.8)

Apply the newest volume-stability theorem with `M0=M_cross`, `E=0`,

`a_0=sqrt(31)/(32 sqrt(511))`.

Its hypotheses are verified by (7.4),(7.8), hence independently

`boxed:
 ||p_(X^T A_m X)||_infinity
 <23/a_0
 =23*32 sqrt(511)/sqrt(31)
 <2989.`                                                            (7.9)

This bound is weaker than (7.2), but it is an actual application of the newest source to a live B10 target family and gives a second product-preserving Fourier route with a continuous density. No small random perturbation is invoked.

## 8. What remains unpaid

The full arbitrary exact-rank-three theorem is still OPEN, so the full owner conjecture is OPEN. The result above does **not** justify taking `rho->0`: arbitrary unbounded product inputs prevent treating the longitudinal leakage as a small random perturbation. The exact endpoint `rho=0` and a punctured collar require different analytic information.

The first B10 obligation after this run is

`QFORM-ULTRANEAR-COLOOP-FINITE-HEAVYLEAF-INTERPOLATION-v1`:

> In the nonzero-pivot near-coloop survivor, close `0<rho<1/128` and/or the at-most-three normalized-heavy-leaf branch, while retaining the exact account02/B10 aggregate hub packet and original-coordinate product provenance. The proof must interpolate to the separately paid exact-null scalar/dependent-pair kernel without assuming coefficient-smallness makes a random quadratic perturbation small.

A promising next mechanism is a finite-hub mixed Fresnel/hyperbolic argument: the gate failure has already localized the problematic longitudinal leakage to at most three physical leaves, while the remaining leaf cloud is diffuse in the Schur-aligned coefficient frame. The new theorem above supplies the diffuse half of that decomposition.

## 9. Regularity and review status

Theorem 3.1 and all applications in Sections 5 and 7 prove a **continuous bounded density**, because the characteristic function has an explicit `L^1` majorant. No continuity statement is claimed for branches covered only by older essential-density kernels.

Independent end-to-end review of this new theorem has not yet occurred. It is a supporting theorem, not a full candidate proof. The full target would still require every remaining sign/degeneracy/higher-rank case plus two actual independent reviews.
