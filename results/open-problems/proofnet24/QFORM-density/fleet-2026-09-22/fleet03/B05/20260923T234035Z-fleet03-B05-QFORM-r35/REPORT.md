SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B05, 2026-09-23T23:40:35Z.
attacking: QFORM-SCALAR-HEAVY-PIVOT-CROSSING-v1 — retain one literal heavy scalar source coordinate and recover the missing third crossing direction from an asymmetric first-bank Pluecker aggregate before any reciprocal coarea payment.

# fleet03/B05 r35 — scalar-heavy pivot compensation by an asymmetric rank-three crossing

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: quadratic coarea / equivalent interval bound preserving arbitrary original-product densities  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING PRODUCT-PRESERVING DENSITY/CONTINUITY THEOREM; FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**  
Full-target continuity: **OPEN**. Continuity is proved on the exact-cross branch below; the designated partner exact-slope branch supplies essential boundedness only.

## 1. Source discipline and scope


The live ratio-packet source is

`yspennstate/math-open-problems@b0299facc04ea0c03276dddb1a12c027aed5a946`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B05/20260923T033640Z-fleet01-B05-QFORM-r26/REPORT.md`.

The immediate predecessor is

`yspennstate/math-open-problems@18cfc90035b4e40e649f4a260cf6c7b454584d0b`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B05/20260923T223923Z-fleet03-B05-QFORM-r34/REPORT.md`.

The determinant-sensitive exact-rank-three crossing refinement used below is

`yspennstate/math-open-problems@95f94696393b5ad8b0def71fa0d93082de92bd85`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B05/20260923T193756Z-fleet03-B05-QFORM-r31/REPORT.md`,

built on the exact-cross Fourier theorem

`yspennstate/math-open-problems@51d2edb29d7a4c150e4d47ed3a6685875a8483ae`

`proofnet24/QFORM-density/interactive/20260923T194300Z-exact-cross-rank-fourier/REPORT.md`.

The designated partner result actually applied in Section 7 is

`yspennstate/math-open-problems@59c6ff7db9aceb8b575abe0e064ebeda06f6f77f`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B05/20260923T041255Z-fleet04-B05-dominant-slope-r2/REPORT.md`.

It proves, in the ratio-packet notation, that if `m_*` is the largest exact physical slope-class mass and `mu=|det B||lambda|`, then

`||p_Q||_infinity < 51.6 (mu m_*)^(-1/3)`.                        (1.1)

The result below is a scoped branch theorem inside the ratio-packet reduction. It is not asserted to cover every symmetric matrix with three large eigenvalues.

## 2. Ratio packet and Schur factorization

After conditioning only original coordinates outside the three active, mutually independent product banks, write

`V=(S,R)^T=Gamma^T X`, `Gamma^T Gamma=I_2`,

and let the other two disjoint original-coordinate banks supply normalized scalar projections

`Y=sum_j eta_j U_j`, `sum_j eta_j^2=1`,

`Z=sum_k zeta_k W_k`, `sum_k zeta_k^2=1`.

The active homogeneous coefficient matrix is

`H=[[C,P],[P^T,B]]`,                                               (2.1)

with real symmetric `C,B`, invertible `B`, and

`C-P B^(-1) P^T = lambda m e1 e1^T`.                              (2.2)

Put

`mu=|det B||lambda|`, `L=lambda m`, `A=B^(-1)P^T`.                (2.3)

Write

`A=[[A11,A12],[A21,A22]]`.                                        (2.4)

As in r34 define

`K=[[1,0,0,0],
    [A11,A12,1,0],
    [A21,A22,0,1]]`,

`D=diag(L,B)`.                                                     (2.5)

Then the Schur identity gives exactly

`H=K^T D K`, `|det D|=mu m`.                                      (2.6)

Let the rows of the first-bank Parseval frame be

`g_i=(xi_i,rho_i)`, `sum_i g_i g_i^T=I_2`.                        (2.7)

In the ratio construction

`xi_i=u_i/sqrt(m)`.                                                (2.8)

Define

`q_xi=max_i xi_i^2`,
`q_Y=max_j eta_j^2`,
`q_Z=max_k zeta_k^2`.                                              (2.9)

The r34 diffuse-scalar theorem deteriorates as `q_Y` or `q_Z` tends to one because it split each scalar source bank across both sides. The present run keeps one heavy literal scalar source coordinate intact and obtains the missing opposite-side dimension from **two first-bank rows** through the exact Schur factor.

## 3. Exact one-side Schur-factor Gram determinant

For any subset of first-bank original coordinates, let

`G=sum_i g_i g_i^T`,
`s=e1^T G e1=sum_i xi_i^2`,
`d=det G`.                                                         (3.1)

Suppose the same side of a physical cut receives total squared coefficient masses

`y^2=sum eta_j^2`, `z^2=sum zeta_k^2`                              (3.2)

from the Y and Z source banks. Its Schur-factor Gram is

`F=K diag-block(G,y^2,z^2) K^T`.                                  (3.3)

### Lemma 3.1 — exact compensation identity

`boxed:
 det F = s y^2 z^2 + d (A22^2 y^2 + A12^2 z^2).
`                                                                     (3.4)

#### Proof by Cauchy-Binet

After the map `K`, a first-bank physical row `g_i=(xi_i,rho_i)` becomes

`w_i=(xi_i, A11 xi_i+A12 rho_i, A21 xi_i+A22 rho_i)`,             (3.5)

while a Y-source row becomes a multiple of `e2` and a Z-source row a multiple of `e3`.

Every nonzero `3x3` physical minor belongs to one of three classes.

1. One first row + one Y row + one Z row has determinant `xi_i eta_j zeta_k`. Summing its square gives `s y^2 z^2`.
2. Two first rows + one Y row have determinant, up to sign,
   `A22 eta_j det(g_i,g_l)`. Their squared sum is `A22^2 y^2 d`.
3. Two first rows + one Z row have determinant, up to sign,
   `A12 zeta_k det(g_i,g_l)`. Their squared sum is `A12^2 z^2 d`.

Three first rows vanish because the image of the first-bank frame has rank at most two; all repeated-scalar classes vanish because the scalar rows are collinear. Cauchy-Binet therefore gives (3.4) exactly. QED.

The new terms in (3.4) are the compensation missed by the coarse r34 lower bound `det F>=s y^2 z^2`: even if one scalar bank is completely absent on one side, two first-bank rows can generate the missing third dimension through `A12` or `A22`.

A symbolic expansion independently returns

`det F = g11*y2*z2 +(g11*g22-g12^2)(A22^2*y2+A12^2*z2)`;

see `CHECKS.txt`. The proof above, not the symbolic check, is the argument.

## 4. Asymmetric first-bank Pluecker split

The heavy-scalar construction needs one side to contribute only the Schur-direction mass `s`, while the opposite side contributes a two-dimensional first-bank determinant.

For `i<j` put

`w_ij=det(g_i,g_j)^2`.                                             (4.1)

Since the frame is Parseval,

`sum_{i<j} w_ij=det(sum_i g_i g_i^T)=1`.                           (4.2)

Randomly put every first-bank original coordinate into `I` with probability `1/2` and let `J` be the complement. Put

`s_I=sum_{i in I} xi_i^2`, `d_J=det(sum_{j in J}g_j g_j^T)`.       (4.3)

### Lemma 4.1 — asymmetric Pluecker split

`boxed:
 E[s_I d_J]
 = (1/8) sum_{j<k} w_jk (1-xi_j^2-xi_k^2)
 >= (1-2q_xi)/8.
`                                                                     (4.4)

Hence if `q_xi<1/4`, some deterministic original-coordinate split satisfies

`boxed: s_I d_J >= 1/16.`                                         (4.5)

#### Proof

Use `d_J=sum_{j<k}w_jk 1_{j,k in J}` and expand `s_I d_J`. For a fixed Pluecker edge `{j,k}`, the term `xi_i^2` contributes only when `i` is distinct from `j,k`; then the event `i in I`, `j,k in J` has probability `1/8`. Thus

`E[s_I d_J]
 =(1/8)sum_{j<k}w_jk sum_{i notin{j,k}}xi_i^2`
`=(1/8)sum_{j<k}w_jk(1-xi_j^2-xi_k^2)`.                           (4.6)

Since every `xi_i^2<=q_xi`, use (4.2) to obtain the lower bound. If `q_xi<1/4`, the expectation is strictly larger than `1/16`, so a split satisfying (4.5) exists. QED.

This is different from the symmetric r31 split `sqrt(det G_I det G_J)`: it remains useful even when only one side needs two first-bank directions.

## 5. Scalar source split lemma

For completeness, if `a_j` are normalized scalar-projection coefficients, `sum a_j^2=1`, and `q=max a_j^2`, a Bernoulli half split with squared mass `T` has

`E[T(1-T)]=(1/4)(1-sum_j a_j^4)>=(1/4)(1-q)`.                    (5.1)

Hence a deterministic split exists with

`boxed: sqrt(T(1-T)) >= (1/2)sqrt(1-q).`                          (5.2)

This is a split of literal original source coordinates, so independence of the two sides is genuine.

## 6. Heavy-Y pivot receiver

Choose a literal Y-source coordinate `j0` attaining

`eta_j0^2=q_Y`.                                                    (6.1)

Assume first

`q_xi<1/4`.                                                        (6.2)

Choose the first-bank split `I,J` from Lemma 4.1. Put the single heavy Y coordinate `j0` on the left and **all** remaining Y source coordinates on the right. Split the Z source bank by Lemma 5.1, and denote the square roots of its left/right coefficient masses by `z_L,z_R`, so

`z_L z_R >= (1/2)sqrt(1-q_Z)`.                                    (6.3)

The physical left/right cut is therefore

left = `(first I, Y_j0, Z_L sources)`,
right = `(first J, all Y except j0, Z_R sources)`.                 (6.4)

Let `F_L,F_R` be the two Schur-factor Grams. Lemma 3.1 gives

`det F_L >= s_I q_Y z_L^2`,                                      (6.5)

and

`det F_R >= d_J [A22^2(1-q_Y)+A12^2 z_R^2]`.                     (6.6)

Therefore

`sqrt(det F_L det F_R)`
` >= sqrt(s_I d_J q_Y) z_L
     sqrt(A22^2(1-q_Y)+A12^2 z_R^2)`.                             (6.7)

Put `p=z_L z_R`. Since `z_R^2<=1`, one has `z_L^2>=p^2`; hence

`z_L^2[A22^2(1-q_Y)+A12^2 z_R^2]`
` >= p^2[A22^2(1-q_Y)+A12^2]`.                                   (6.8)

Combining (4.5), (6.3), and (6.8),

`boxed:
 sqrt(det F_L det F_R)
 >= (1/8) sqrt(q_Y(1-q_Z))
    sqrt(A12^2+A22^2(1-q_Y)).
`                                                                     (6.9)

Now use the exact r34 crossing-volume identity. Since

`H=K^T D K`, `|det D|=mu m`,

the product `Delta` of the three nonzero singular values of the **physical original-coordinate cross block** is

`Delta=mu m sqrt(det F_L det F_R)`.                               (6.10)

Thus

`boxed:
 Delta_Y >= (mu m/8) Omega_Y,
 Omega_Y := sqrt(q_Y(1-q_Z))
            sqrt(A12^2+A22^2(1-q_Y)).
`                                                                     (6.11)

Whenever `Omega_Y>0`, this cut has exact crossing rank three. The determinant-sensitive exact-cross theorem gives

`boxed:
 ||p_Q||_infinity
 <= 6 [8/(mu m Omega_Y)]^(1/3).
`                                                                     (6.12)

Moreover the characteristic function is integrable in this branch, so the density is bounded and **continuous**.

No density of the dependent pair `(S,R)` is conditioned. All splitting occurred in original coordinate banks before the crossing was paid.

## 7. Symmetric heavy-Z pivot and designated partner branch

Interchanging Y and Z gives

`boxed:
 Delta_Z >= (mu m/8) Omega_Z,
 Omega_Z := sqrt(q_Z(1-q_Y))
            sqrt(A22^2+A12^2(1-q_Z)),
`                                                                     (7.1)

and, whenever `Omega_Z>0`,

`boxed:
 ||p_Q||_infinity
 <=6 [8/(mu m Omega_Z)]^(1/3),
`                                                                     (7.2)

again with a continuous density.

The only first-bank case excluded from Sections 6-7 is `q_xi>=1/4`. Here the designated fleet04/B05 result applies at an actual inequality. By (2.8), if `xi_h^2>=1/4`, then

`u_h^2=m xi_h^2>=m/4`.                                             (7.3)

The literal original coordinate `h` is itself an exact physical slope class, so the partner exact-slope mass obeys

`m_*>=u_h^2>=m/4`.                                                 (7.4)

Insert (7.4) into the completed partner theorem (1.1):

`boxed:
 ||p_Q||_infinity
 <51.6 (mu m/4)^(-1/3)
 =51.6 [4/(mu m)]^(1/3).
`                                                                     (7.5)

For the standard ratio packet from fleet01/B05 r26,

`m>=3/20`,                                                         (7.6)

so

`boxed:
 ||p_Q||_infinity <154.161 mu^(-1/3).
`                                                                     (7.7)

This is the required actual use of the designated partner result. Its theorem does not itself assert continuity, so continuity is not claimed for this alternative.

## 8. Combined theorem and a concrete scalar-heavy chamber

Define

`Omega=max(Omega_Y,Omega_Z)`.                                      (8.1)

### Theorem `QFORM-SCALAR-HEAVY-PIVOT-CROSSING-v1`

For every active ratio packet satisfying (2.1)-(2.9), one of the following holds:

1. `q_xi>=1/4`, in which case the essential density bound (7.5) holds by the designated fleet04/B05 exact-slope theorem; or
2. `q_xi<1/4` and `Omega>0`, in which case

`boxed: ||p_Q||_infinity <=6 [8/(mu m Omega)]^(1/3)`              (8.2)

and `Q` has a bounded continuous density.

The theorem is invariant under arbitrary signs of `B` and `lambda`; only `mu=|det B||lambda|` enters.

A useful concrete branch is obtained when one scalar bank is heavy and the other is diffuse. Suppose, for example,

`q_Y>=3/4`, `q_Z<=3/4`,

and

`sqrt(A12^2+A22^2(1-q_Y)) >=1/4`.                                (8.3)

Then

`Omega_Y >= sqrt(3)/16`,                                          (8.4)

so in the `q_xi<1/4` branch

`Delta_Y >= (sqrt(3)/128) mu m`                                  (8.5)

and

`||p_Q||_infinity
 <=6 [32/(sqrt(3) mu m (1/4))]^(1/3)`.                           (8.6)

Using `m>=3/20`,

`boxed: ||p_Q||_infinity <47.389 mu^(-1/3)`                       (8.7)

on this exact-cross branch. Together with (7.7), the **whole** chamber (8.3), with no restriction on `q_xi`, has

`boxed: ||p_Q||_infinity <154.161 mu^(-1/3).`                     (8.8)

The symmetric statement holds with Y/Z exchanged and the corresponding currency from (7.1). If additionally `mu>=1`, (8.8) is a numerical universal bound `<154.161` on this chamber.

## 9. What this resolves and the precise remaining factor

The r34 scalar-diffuse crossing paid both scalar directions by splitting both scalar source banks. It therefore lost control as `q_Y` or `q_Z` approached one. The present theorem shows that this loss is not intrinsic when only one scalar bank becomes concentrated. A single heavy literal scalar carrier can stay intact; the opposite side recovers the third crossing dimension through the two-first-row terms

`d A22^2 y^2` and `d A12^2 z^2`                                   (9.1)

in the exact identity (3.4).

Thus the next B05 debt is narrower:

`QFORM-DOUBLE-HEAVY-SCALAR-COLLAPSED-CURRENCY-v1`.

A genuinely surviving packet must avoid the partner branch `q_xi>=1/4` and simultaneously make the useful scalar-pivot currencies in (6.11) and (7.1) small. This can happen when both scalar projections become nearly literal (`q_Y,q_Z->1`), because there is then almost no scalar tail to place on the opposite side, or when the relevant Schur-factor couplings `A12,A22` collapse in the weighted combinations above. In the exact literal-literal endpoint `q_Y=q_Z=1`, both `Omega_Y` and `Omega_Z` vanish identically, even though the full rank-three curvature may remain.

The next receiver must therefore retain the two literal scalar pivots **jointly** with a two-sided first-bank Pluecker resource, or spend the third curvature through a product-sensitive half-Riesz/coarea mechanism before conditioning creates a rank-two saddle. It cannot first isolate an indefinite rank-two conditional density: the current B05 correction stream contains explicit logarithmic saddle obstructions to that interface.

This is a precise missing factor, not a counterexample to QFORM.

## 10. Verification and status

`CHECKS.txt` records:

- exact symbolic verification of (3.4);
- exhaustive finite diagnostics of the expectation identity (4.4) on 200 random Parseval frames, with maximum floating residual `1.67e-16`;
- the numerical constants in (7.7) and (8.7).

No finite computation, Monte Carlo histogram, or numerical experiment is used as proof.

**Full QFORM status:** OPEN / NOT PROVED / NOT DISPROVED.  
**Full-target continuity:** OPEN.  
**Branch continuity:** proved on the exact-cross alternative; not claimed on the partner exact-slope alternative.  
**Native brain status:** `WITHOUT_VERIFIED_BRAIN`; repository reads/writes are not native learned-memory ingestion.
