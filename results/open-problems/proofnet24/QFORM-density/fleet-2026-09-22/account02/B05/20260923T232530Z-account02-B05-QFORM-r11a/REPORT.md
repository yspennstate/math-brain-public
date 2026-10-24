SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B05, 2026-09-23T23:25:30.947403Z.
attacking: QFORM-HUB-TWOBANK-AGGREGATE-WEDGE-v1 — use the fresh account03/B05 scalar-bank split to remove the diffuse scalar chamber, then compile the surviving heavy scalar source into an exact pseudodeterminant/cofactor star and pay every quantitatively nonzero physical pivot.

# account02/B05 r11a — scalar-heavy cofactor compiler for the ratio packet

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control at startup: `yspennstate/math-research-brain@2d1283ce51c85471974e907e0289a5e6cee1dfa3`, revision `2026-09-22.15`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **PROVED SUPPORTING THEOREM / HEAVY-SCALAR NONNULL-PIVOT COLLAR PAID / FULL QFORM OPEN**  
Continuity: not claimed by the new pivot payment; continuity remains separate.

The first unpaid implication is now

`QFORM-SCALAR-HEAVY-NULLSTAR-AGGREGATOR-v1`:

> in the exact-rank-three ratio packet, after the fresh scalar-diffuse and first-bank-heavy exits have fired, retain a literal heavy scalar source whose physical diagonal is zero or quantitatively near zero and spend its **aggregate principal-determinant star** before selecting/inverting a single physical triple. In the indefinite pair subbranch the survivor is simultaneously near-singular in the pair metric. The star mass is computed exactly below; no small source tail may be deleted.

This is narrower than the predecessor `QFORM-HUB-TWOBANK-AGGREGATE-WEDGE-v1`: the newest partner theorem removes the whole two-scalar-diffuse chamber, and the calculation below removes every heavy-scalar branch with a quantitative nonzero pivot.

## 1. Sources and live corrections actually used

Fresh designated partner:

`yspennstate/math-open-problems@18cfc90035b4e40e649f4a260cf6c7b454584d0b`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260923T223923Z-account03-B05-QFORM-r34/REPORT.md`.

Its exact Schur factorization and three-bank crossing theorem are used in Section 5.

The nonzero physical-pivot analytic receiver is the completed theorem

`QFORM-RANK3-ALL-RESIDUAL-ORIENTATIONS-v1`, source

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

For an exact-rank-three physical block `A=VMV^T`, `V^TV=I_3`, a physical coordinate `i` of leverage `c_i`, and `A_ii != 0`, it proves, uniformly in every outside affine coupling,

`||p_Q||_(infinity,ess) <= 128 [c_i |A_ii| |det M|]^(-1/4)`.       (1.1)

The required pinned source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

was reread through `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. Its completed Theorem F pays every exact-rank-three diffuse spectral frame by `<=12`; its Theorem C pays the ruled one-sheet side of signature `(2,1)` by `<=pi sqrt(2)`. The counterexample search reports no target-valid counterexample.

Live corrections remain binding: no arbitrary-joint 3D coarea, no post-rotation independence, no conditional-cap-as-independence, no unrestricted curved-fiber supremum, no deletion of a small random coefficient tail, and no interval-to-Borel promotion.

## 2. Fresh ratio packet in factor coordinates

Use the exact packet of account03/B05 r34. The first original product bank gives a two-dimensional Parseval projection

`V=(S,R)^T=Gamma^T X`, `Gamma^T Gamma=I_2`.

Two mutually disjoint original product banks give normalized scalar projections

`Y=sum_j eta_j U_j`, `sum_j eta_j^2=1`,
`Z=sum_k zeta_k W_k`, `sum_k zeta_k^2=1`.

The compressed homogeneous matrix is

`H=[[C,P],[P^T,B]]`,

with `B` invertible and

`C-P B^(-1) P^T = lambda m e_1 e_1^T`,
`mu=|det B| |lambda|`.                                               (2.1)

Set

`A=B^(-1)P^T`,
`L=lambda m`,
`D=diag(L,B)`,

and

`K=[[1,0,0,0],
    [A11,A12,1,0],
    [A21,A22,0,1]]`.                                                 (2.2)

Then r34 proves exactly

`H=K^T D K`, `|det D|=mu m`.                                        (2.3)

Following the preceding r31 notation, the second column of `A` is

`z=B^(-1)(r,s)^T=(z_1,z_2)^T`,

so

`A12=z_1`, `A22=z_2`.                                                (2.4)

The physical coefficient map into the latent variables `(S,R,Y,Z)` has Gram `I_4`: the first-bank columns are orthonormal and the two scalar source coefficient vectors are normalized on disjoint supports. Therefore a rank-three factor of the full active physical matrix is

`R_phys = Phi K^T`,

and its factor Gram is

`G=R_phys^T R_phys=K K^T`.                                           (2.5)

No transformed random coordinates are declared independent here; (2.5) is only deterministic coefficient geometry.

## 3. Exact pseudodeterminant and scalar-source leverage identities

A direct multiplication gives

`G = [[1, A11, A21],
      [A11, 1+A11^2+A12^2, A11*A21+A12*A22],
      [A21, A11*A21+A12*A22, 1+A21^2+A22^2]]`.                      (3.1)

The three key determinants are

`det G = 1+A12^2+A22^2 = 1+z_1^2+z_2^2`,                            (3.2)

`cof_22(G)=1+A22^2=1+z_2^2`,                                       (3.3)

`cof_33(G)=1+A12^2=1+z_1^2`.                                       (3.4)

Let `Delta_3` denote the product of the absolute values of the three nonzero eigenvalues of the full active physical rank-three matrix. Orthogonalizing the columns of `R_phys` in (2.5) gives

`boxed: Delta_3 = |det D| det G
                 = mu m (1+z_1^2+z_2^2).`                          (3.5)

Now fix a literal original source coordinate `U_j` in the `Y` bank. Its factor row is exactly

`r_(Y,j)=eta_j e_2`.

Its spectral leverage is therefore

`c_(Y,j)=eta_j^2 e_2^T G^(-1)e_2
         =eta_j^2 (1+z_2^2)/(1+z_1^2+z_2^2)`.                       (3.6)

Multiplying (3.6) by (3.5) cancels the potentially bad global factor Gram:

`boxed: c_(Y,j) Delta_3 = eta_j^2 mu m (1+z_2^2).`                  (3.7)

Similarly, for a literal `Z`-source coordinate,

`boxed: c_(Z,k) Delta_3 = zeta_k^2 mu m (1+z_1^2).`                 (3.8)

These identities are exact. In particular a large residual ratio coefficient can only improve the corresponding scalar-source spectral currency; it never costs a reciprocal factor.

## 4. Exact aggregate principal-determinant star

Equations (3.7)-(3.8) have a useful physical interpretation which does not select a small minor.

For any exact-rank-three matrix written `A=VMV^T` with `V^TV=I_3`, Cauchy-Binet gives

`det A_T = det(M) det(V_T)^2`

for every physical triple `T`. Hence, for every physical coordinate `i`,

`sum_(T: |T|=3, i in T) |det A_T|
 = |det M| sum_(T contains i) det(V_T)^2
 = c_i |det M|`.                                                     (4.1)

The last equality is the standard volume-sampling inclusion identity; equivalently it is `v_i^T adj(V^TV)v_i` with `V^TV=I`.

Combining (4.1) with (3.7)-(3.8) yields the new aggregate-star formulas

`boxed:
 sum_(u<v, u,v != Y_j) |det A_{ {Y_j,u,v} }|
 = eta_j^2 mu m (1+z_2^2),
`                                                                           (4.2)

and

`boxed:
 sum_(u<v, u,v != Z_k) |det A_{ {Z_k,u,v} }|
 = zeta_k^2 mu m (1+z_1^2).
`                                                                           (4.3)

Every term has the same determinant sign before absolute values because the active matrix has exact rank three. Thus (4.2)-(4.3) are genuine aggregate curvature masses, not triangle-inequality artifacts.

This is exactly the currency needed at a zero physical pivot: the previous B05 theorem `QFORM-NULL-PIVOT-DET-ONLY-v1` pays any **individual** nonzero triple containing that zero pivot by `C_0 |det A_T|^(-1/3)`, `C_0<7.762`. Equations (4.2)-(4.3) show what remains when that curvature is diffusely spread over many triples: aggregate first, then invert. Selecting one term before aggregation would reintroduce a dimension-dependent reciprocal-minor loss.

## 5. Heavy scalar source with a nonzero physical pivot is paid

Write

`B=[[a,c],[c,d]]`.                                                   (5.1)

For a `Y`-source coordinate `U_j`, the physical diagonal is

`A_(Y_j,Y_j)=eta_j^2 a`.                                             (5.2)

Apply the completed orientation-free pivot theorem (1.1) and then (3.7): whenever `a != 0`,

`||p_Q||_(infinity,ess)
 <=128 [eta_j^4 mu m |a| (1+z_2^2)]^(-1/4).`                        (5.3)

For a `Z`-source coordinate, whenever `d != 0`,

`||p_Q||_(infinity,ess)
 <=128 [zeta_k^4 mu m |d| (1+z_1^2)]^(-1/4).`                       (5.4)

Define

`q_Y=max_j eta_j^2`, `q_Z=max_k zeta_k^2`.                          (5.5)

If `q_Y>3/4`, choose a maximizing literal source coordinate. Then

`boxed:
 ||p_Q||_(infinity,ess)
 < (128*2/sqrt(3)) [mu m |a|(1+z_2^2)]^(-1/4).
`                                                                           (5.6)

The identical statement with `Y,a,z_2` replaced by `Z,d,z_1` holds when `q_Z>3/4`.

A useful fixed collar is obtained by the dimensionless threshold

`mu m |a|(1+z_2^2) >= 1/64`.                                       (5.7)

Then every heavy-`Y` instance obeys

`boxed: ||p_Q||_(infinity,ess) < 418.047.`                           (5.8)

The same constant holds for the heavy-`Z` collar.

The conclusion permits arbitrary outside coordinates and affine terms because theorem (1.1) is uniform under conditioning the outside original coordinates. No continuity assertion is imported from that theorem.

## 6. Fresh account03/B05 r34 applied to the actual survivor

The newest designated partner theorem gives two exits before (5.6) is even needed.

First, if a first-bank Schur weight satisfies `xi_h^2>=1/2`, its completed exact-slope receiver gives

`||p_Q||_infinity <51.6 (mu m/2)^(-1/3)`.                           (6.1)

Second, if no such first-bank row exists, r34 splits the first bank and **both scalar source banks**. It proves

`||p_Q||_infinity
 <=6 [16/(sqrt(3) mu m sqrt((1-q_Y)(1-q_Z)))]^(1/3)`                (6.2)

on the exact-cross branch. Together with (6.1), in the standard ratio packet `m>=3/20`, the entire scalar-diffuse chamber

`q_Y<=3/4`, `q_Z<=3/4`                                               (6.3)

is bounded by

`boxed: ||p_Q||_infinity <122.358 mu^(-1/3).`                        (6.4)

Thus a packet which survives the fresh partner theorem must have **no first-bank Schur row of weight at least `1/2` and at least one literal scalar source of squared coefficient greater than `3/4`**. Equations (5.6)-(5.8) then pay every such heavy scalar unless its own physical pivot currency is quantitatively near zero.

For the indefinite scalar-pair subbranch one can localize still further using the completed aggregate rank-two-bank/two-scalar-bank theorem (`account03/B05 r19`):

`||p_Q||_infinity <= C_19 [kappa(B) mu m]^(-1/4),
 C_19=8*2^(3/4)*sqrt(5)=30.0848247447...`                            (6.5)

where `kappa(B)=sigma_min(B)`. Hence

`kappa(B) mu m >=1/64`                                               (6.6)

already gives

`boxed: ||p_Q||_infinity <85.093.`                                   (6.7)

Consequently, in the indefinite ratio-pair chamber, a genuinely unpaid packet after the present run must satisfy simultaneously

1. no first-bank Schur coefficient has squared weight `>=1/2`;
2. `q_Y>3/4` or `q_Z>3/4`;
3. `kappa(B) mu m <1/64`;
4. for every heavy `Y` source, `mu m |a|(1+z_2^2)<1/64`, and for every heavy `Z` source, `mu m |d|(1+z_1^2)<1/64`.

This is the promised heavy-scalar near-null/near-singular chamber.

## 7. Required pinned e5f result applied to a real obstruction

The pinned `e5f71d79...` package proves Theorem F: an exact-rank-three active form whose original-coordinate spectral leverages are all at most `1/2` has

`boxed: ||p_Q||_infinity <=12.`                                      (7.1)

Thus the scalar-heavy source geometry above is only a genuine obstruction after the physical leverage-diffuse gate has already failed. Equations (3.6)-(3.8) quantify that failure in the ratio packet instead of treating `q_Y` or `q_Z` as spectral leverage by fiat.

For signature `(2,1)`, the same pinned source separately gives on the ruled side

`boxed: p_Q(s)<=pi sqrt(2), s>=0.`                                   (7.2)

Therefore the remaining scalar-heavy null-star work is genuinely complementary convex/two-sheet geometry (together with the definite signature), not a reproof of the ruled one-sheet estimate. The pinned counterexample search found no target-valid counterexample; (5.8) additionally excludes a quantitatively nonzero heavy scalar pivot as a counterexample mechanism.

## 8. Meaning of the remaining debt

At an exact heavy-`Y` zero pivot `a=0`, formula (4.2) can still carry order-one total determinant mass even though every individual physical triple may have a tiny determinant. The determinant-only null-pivot theorem pays a selected triple, but selecting first can lose with dimension. Conversely, the partner r34 crossing pays aggregate banks only when both scalar source banks can be split with quantitative mass; a single nearly atomic scalar bank removes one side of that crossing.

The missing theorem must therefore combine these two facts at the **aggregate** level:

- one literal independent scalar hub carries a zero/near-zero diagonal;
- its whole principal-determinant star has the exact mass (4.2) or (4.3);
- the third curvature must be retained jointly with the original-product banks before any reciprocal determinant or maximal-set operation.

This is precisely `QFORM-SCALAR-HEAVY-NULLSTAR-AGGREGATOR-v1`. A theorem depending on the star sum itself, or an equivalent source-preserving Fourier/coarea receiver, would bridge the exact zero and small-nonzero scalar pivot without the forbidden half-Riesz-only perturbation.

## 9. Integrity

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains open. No moments, support, log-concavity, diagonal-basis assumption, rotated independence, arbitrary-joint coarea estimate, or perturbative deletion is used. The algebraic identities (3.2)-(3.4) and numerical constants were independently checked. Independent mathematical review of this new theorem is **PENDING**.
