SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B11, 2026-09-24T02:11:27Z.
attacking: the exact-rank-three null-pivot near-coloop chamber: convert the residual two-dimensional Parseval frame into two original-coordinate banks and expose the exact sparse crossing that contains the third direction.

# fleet03/B11 r47 — null-hub two-bank sparse crossing compiler

Programme: `QFORM-DENSITY-3EIG-20260922`.
Assignment: indefinite signatures `(2,1)` / `(1,2)`.
Status: **NEW STRUCTURAL REDUCTION / LARGE-ROW BRANCH PAID / DESIGNATED PARTNER APPLIED / SAME-RUN OVERCLAIM CORRECTED / FULL QFORM OPEN**.
Execution: **WITHOUT_VERIFIED_BRAIN**.

The unrestricted owner conjecture remains OPEN. This report proves an exact bank-crossing identity and an elementary two-bank paving theorem for the exact-rank-three null-pivot near-coloop chamber. It also pays the complementary large-row branch by the completed fleet04/B11 pair-area receiver. The diffuse two-bank branch is reduced to a sparse three-by-three crossing normal form, but is NOT closed here.

No post-rotation independence, Gaussian/log-concave/moment/support assumption, conditional-density cap, arbitrary-joint coarea lemma, pointwise law-uniform van-der-Corput bound, or deletion of a small nonzero quadratic term is used.

## 0. Same-run correction: why the first draft did not close the chamber

An earlier same-run draft incorrectly applied the r44 shared-hub tensor theorem from the fact that the **doubly star-orthogonal crossing**

`C=P_{c_L}A[L,R]P_{r_R}`

has rank one. That inference was too strong. The physical theorem in r44 assumes the WHOLE interbank block `N=A[L,R]` has rank one; under that hypothesis determinant-one shears collapse all interbank terms to one transverse bilinear factor. In the present null-hub geometry, `C` is indeed rank one, but `N` can have additional star-aligned terms. Those terms are small only through the leverage defect and cannot be deleted under the target's arbitrary input laws.

Accordingly, the former `<260/s` closure claim from the first draft is withdrawn. The exact identities and paving lemma below survive; they now identify precisely what extra crossing remains to be handled.

## 1. Sources and inherited results

Immediate normal-form predecessor:

- `yspennstate/math-open-problems@12e2174445fbc824279bf1376da1346454d7060a`
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B11/20260924T002432Z-fleet03-B11-QFORM-r45/REPORT.md`.

It gives the exact null-pivot spectral normal form used below.

The r44 shared-hub tensor receiver, whose scope is respected here, is:

- `yspennstate/math-open-problems@388ba1f1ccf6a89dad0ca0a0fdb71d281ad6239b`
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B11/20260923T231333Z-fleet03-B11-QFORM-r44/REPORT.md`.

Its physical application assumes a whole rank-one interbank block and then gives a continuous density with a `T^{-1/6}` bound. This report does not invoke it outside that premise.

The completed designated partner result is fleet04/B11 r6:

- `yspennstate/math-open-problems@30555c1ca97752e10f5089ccd95f8514c704be5a`
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B11/20260923T131400Z-fleet04-B11-extension-mass-r6/REPORT.md`.

For a physical pair `S={i,j}`, with `g_S=||r_i wedge r_j||^2`, it proves

`d_{S,k}=|det M| ((r_i wedge r_j) dot r_k)^2`,

`sum_k d_{S,k}=|det M| g_S`,

`W_2(S)=(sum_k d_{S,k})^2-sum_k d_{S,k}^2`.

The same fleet04/B11 line records the completed full-line pair-area compiler

`||p_Q||_infinity <= 128 sqrt(2)/(s sqrt(g_S))`,                  (1.1)

where `s=min |lambda(M)|`.

## 2. Exact null-hub coordinates

Let

`A=R M R^T`, `R^T R=I_3`,

where `M` is invertible symmetric of signature `(2,1)` or `(1,2)` and

`s=min_a |lambda_a(M)|>0`.

Fix an ORIGINAL physical coordinate `i` with

`q=||r_i||^2 >= 63/64`, `A_ii=r_i^T M r_i=0`.

Put

`e1=r_i/sqrt(q)`, `kappa=||M e1||`, `e2=M e1/kappa`,

and complete to an orthonormal spectral basis `(e1,e2,e3)`. Then

`M=[[0,kappa,0],[kappa,d,e],[0,e,c]]`,

and

`kappa^2 |c|=|det M| >= s^3`.                                    (2.1)

For each residual physical row `j!=i`, write

`r_j = sqrt(1-q) t_j e1 + y_j e2 + z_j e3`.                      (2.2)

Parseval gives

`sum t_j^2=sum y_j^2=sum z_j^2=1`,

`sum t_j y_j=sum t_j z_j=sum y_j z_j=0`.                         (2.3)

Thus `t=(t_j)`, `y=(y_j)`, `z=(z_j)` are orthonormal vectors in the residual physical-coordinate space. In particular the two-vectors

`u_j=(y_j,z_j)`

form an exact two-dimensional Parseval frame:

`sum_{j!=i} u_j u_j^T=I_2`.                                     (2.4)

The physical hub-star coefficient and exterior area are

`A_ij=sqrt(q) kappa y_j`,                                        (2.5)

`g_{ij}=||r_i wedge r_j||^2=q(y_j^2+z_j^2)=q||u_j||^2`.          (2.6)

Equation (2.6) immediately routes any large residual two-frame row into the designated partner receiver.

## 3. First exact identity: the doubly star-orthogonal crossing is rank one

Take any partition of the residual ORIGINAL coordinates into disjoint banks `L,R`. Define

`y_L=(y_j)_{j in L}`, `z_L=(z_j)_{j in L}`, `t_L=(t_j)_{j in L}`,

and similarly on `R`. The hub-star vectors are

`c_L=A[L,i]=sqrt(q) kappa y_L`,

`r_R=A[i,R]^T=sqrt(q) kappa y_R`.                                (3.1)

Let

`P_L=I-y_L y_L^T/||y_L||^2`,
`P_R=I-y_R y_R^T/||y_R||^2`

when the denominators are nonzero. Then

`C:=P_L A[L,R]P_R`.

Because `P_L R_L e2=0` and `P_R R_R e2=0`, both sides of `M` may be compressed to `e2^perp`. From the null-hub canonical matrix,

`P_{e2^perp} M P_{e2^perp}=c e3 e3^T`.                           (3.2)

Therefore exactly

`boxed: C=c(P_L z_L)(P_R z_R)^T`.                               (3.3)

Hence the crossing left after removing the two physical star directions always has rank at most one. This is an exact coefficient identity, not an analytic approximation.

Define partial two-frame Grams

`G_L=sum_{j in L}u_j u_j^T`, `G_R=I_2-G_L`,

and `D_L=det G_L`, `D_R=det G_R`. When the partial Grams are positive definite,

`||y_L||^2 ||P_L z_L||^2=D_L`,
`||y_R||^2 ||P_R z_R||^2=D_R`.                                  (3.4)

Consequently the r44 tensor currency that would be available if the WHOLE interbank block were rank one has the exact geometric value

`T_geom:=||c_L||^2||r_R||^2||C||_F^2`

`boxed: T_geom=q^2 kappa^4 c^2 D_LD_R=q^2|det M|^2D_LD_R.`       (3.5)

Equation (3.5) is a geometric identity only. It is not, by itself, permission to apply r44.

## 4. Elementary two-bank paving of the residual two-frame

### Lemma 4.1 — `QFORM-2D-PARSEVAL-TWOBANK-PAVING-v1`

Let `u_j in R^2` satisfy

`sum_j u_j u_j^T=I_2`

and assume

`max_j ||u_j||^2<=delta<1/2`.

Then there is a partition `L,R` such that every eigenvalue of both `G_L` and `G_R` is at least

`m(delta)=1/2-sqrt(delta/2)>0`.                                  (4.1)

Hence

`D_L,D_R>=m(delta)^2`.                                           (4.2)

### Proof

Choose independent Bernoulli variables `xi_j` with mean `1/2` and put

`G_L=sum_j xi_j u_j u_j^T`.

Then `E G_L=I_2/2`. Independence of the centered summands gives

`E||G_L-I_2/2||_F^2`
` =(1/4)sum_j||u_j u_j^T||_F^2`
` =(1/4)sum_j||u_j||^4`
` <=(delta/4)sum_j||u_j||^2`
` =delta/2`.                                                     (4.3)

Therefore some realization has

`||G_L-I_2/2||_op<=||G_L-I_2/2||_F<=sqrt(delta/2)`.

Since `G_R=I_2-G_L`, both partial Grams have spectrum contained in

`[1/2-sqrt(delta/2),1/2+sqrt(delta/2)]`.

This proves the lemma. QED.

For the convenient threshold

`delta=1/8`,

one obtains

`G_L,G_R >= (1/4)I_2`,

`D_L,D_R>=1/16`,                                                 (4.4)

and hence from (3.5)

`T_geom>=q^2|det M|^2/256>=q^2s^6/256`.                          (4.5)

Again, (4.5) is a structural currency, not yet a density theorem because star-aligned leakage remains.

## 5. The complementary large-row branch is paid

If some residual row satisfies

`||u_j||^2>=1/8`,

then by (2.6)

`g_{ij}>=q/8>=63/512`.

Applying the completed fleet04/B11 full-line pair-area theorem (1.1) at this actual inequality gives

`boxed:
 ||p_Q||_infinity
 <=128sqrt(2)/(s sqrt(63/512))
 =4096/(sqrt(63)s)
 <516.05/s.`                                                     (5.1)

Thus the only null-hub near-coloop state left after this run is the diffuse two-frame chamber

`max_j||u_j||^2<1/8`,                                           (5.2)

where the paving (4.4) is available.

No continuity statement is imported from the pair-area theorem; (5.1) is an essential-density bound.

## 6. Second exact identity: sparse crossing normal form in the diffuse chamber

Take the partition from Lemma 4.1. Put

`Y=||y_L||`, `Z=||y_R||`,

`v_L=P_L z_L/||P_L z_L||`, `v_R=P_R z_R/||P_R z_R||`.

Since `G_L,G_R` are positive definite, all these quantities are defined and nonzero. Now remove from `t_L` the span of `y_L,z_L` and from `t_R` the span of `y_R,z_R`:

`tau_L=P_{span(y_L,z_L)^perp}t_L`,
`tau_R=P_{span(y_R,z_R)^perp}t_R`.                               (6.1)

When nonzero, normalize these to physical coefficient directions `w_L,w_R`.

Use the three bank projection coordinates

- `Y1` along `y_L`, `Y2` along `v_L`, `Y3` along `w_L`;
- `Z1` along `y_R`, `Z2` along `v_R`, `Z3` along `w_R`.

These are orthonormal linear projections inside the two disjoint ORIGINAL-coordinate banks. Same-bank quadratic terms are retained as arbitrary bank phases.

From (3.3), the entire star-orthogonal-by-star-orthogonal block is one-dimensional, so before any shear the only such term is

`sigma Y2 Z2`,

with

`boxed: sigma=c||P_Lz_L|| ||P_Rz_R||`.                           (6.2)

Moreover `w_R` has spectral image purely in the `e1` direction, and `w_L` likewise. Since `Me1=kappa e2`, the exact star-to-extra-bank coefficients are

`boxed:
 lambda_R=kappa sqrt(1-q) ||y_L|| ||tau_R||,`

`boxed:
 lambda_L=kappa sqrt(1-q) ||y_R|| ||tau_L||.`                    (6.3)

The coefficients linking `Y1` to `Z2` and `Y2` to `Z1` can be removed by determinant-one triangular shears inside the two bank projection coordinates because `sigma!=0`. These shears do not delete any term; they merely replace the bank phases by new arbitrary phases and change the `Y1Z1` coefficient.

After those exact shears, the interbank crossing has the sparse form

`boxed:
 2[ Delta Y1Z1 + sigma Y2Z2 + lambda_R Y1Z3 + lambda_L Y3Z1 ].` (6.4)

There are no `Y2Z3`, `Y3Z2`, or `Y3Z3` terms. Here `Delta` is an arbitrary real coefficient produced by the exact shear.

Thus the diffuse null-hub chamber has been reduced to one shared physical hub, two source-disjoint banks, one robust transverse rank-one crossing `sigma Y2Z2`, and at most two one-sided star-aligned punctures whose coefficients carry the exact factor `sqrt(1-q)`.

The point of (6.4) is that it exposes precisely why (3.3) does not by itself trigger r44: the terms `lambda_R Y1Z3`, `lambda_L Y3Z1`, and `Delta Y1Z1` can keep the WHOLE interbank block above rank one.

The leverage defect still enters quantitatively. Relative to the hub-star coefficients

`alpha=sqrt(q)kappa||y_L||`, `beta=sqrt(q)kappa||y_R||`,          (6.5)

one has

`|lambda_R|/|alpha|=sqrt((1-q)/q)||tau_R||<=1/sqrt(63)`,

`|lambda_L|/|beta|=sqrt((1-q)/q)||tau_L||<=1/sqrt(63)`.          (6.6)

These ratios are small but are NOT discarded.

## 7. Designated fleet04/B11 extension-mass theorem applied directly

The partner theorem gives an independent quantitative description of the same diffuse chamber.

Fix any residual leaf `j` and `S={i,j}`. From (2.2),

`(r_i wedge r_j) dot r_k`
` =sqrt(q)(y_j z_k-z_j y_k)`.

Hence

`d_{S,k}=|det M|q(y_jz_k-z_jy_k)^2`.                             (7.1)

Under the diffuse hypothesis (5.2),

`(y_jz_k-z_jy_k)^2`
` <=||u_j||^2||u_k||^2`
` <(1/8)||u_j||^2`.

Since

`T_S=sum_kd_{S,k}=|det M|q||u_j||^2`,

we get the actual partner inequality

`max_kd_{S,k}<T_S/8`.                                           (7.2)

Substituting (7.2) into fleet04/B11's exact second-moment identity yields

`boxed:
 W_2(S)>=(7/8)T_S^2
       =(7/8)|det M|^2 g_{ij}^2.`                               (7.3)

Thus the surviving chamber is genuinely diffuse in the partner's extension-star sense as well; it is not secretly a one-coordinate extension packet.

## 8. Rank-two logarithm and the third-direction mechanism now isolated

The mandatory control remains

`p_{2XY}(t)=log(1/(2|t|))`

for independent centered unit uniforms. The shared-hub rank-two saddle gives the familiar logarithmic endpoint.

This run identifies exactly where the third direction lives in the null-hub chamber:

1. if one physical residual row carries significant transverse area, the partner pair-area theorem pays it directly;
2. otherwise the residual two-frame can be split into two original-coordinate banks with uniformly positive transverse Gram determinants;
3. after projecting away the two hub-star directions, the third spectral direction is exactly one rank-one bilinear crossing `sigma Y2Z2`, with geometric currency (3.5);
4. the only remaining obstruction consists of the two star-aligned puncture terms in (6.4), each carrying the explicit leverage-defect factor `sqrt(1-q)` but not legally discardable.

So the third direction does not vanish. The unresolved issue is a stability theorem for the shared-hub tensor estimate under these two exact one-sided punctures.

## 9. First unpaid implication after r47

The next B11 target is

`QFORM-SPARSE-SHAREDHUB-PUNCTURE-RECEIVER-v1`:

> For three mutually independent source banks `H`, `L`, `R`, with arbitrary same-bank phases and crossing exactly of the form
>
> `2H(alpha Y1+beta Z1)`
> `+2[Delta Y1Z1+sigma Y2Z2+lambda_R Y1Z3+lambda_L Y3Z1]`,
>
> prove a universal density bound from the quantitative lower bound on the transverse currency and the ratios
> `|lambda_R|/|alpha|, |lambda_L|/|beta| <=1/sqrt(63)`,
> without deleting the punctures and without using a conditional-density cap.

A successful theorem here would close the remaining exact-rank-three null-pivot near-coloop chamber. The nonzero-heavy-pivot chamber and arbitrary additional nonseparable spectrum remain separate bridges to the full target.

No new continuity theorem is claimed for the whole chamber in this run. Full QFORM and full-target continuity both remain OPEN.

## 10. Verification

The verifier checks the exact rank-one double-projection identity, the geometric currency identity (3.5), the two-bank paving numerically on random diffuse Parseval frames, the sparse crossing zero pattern and puncture coefficients, and the partner extension-mass inequality. Finite numerical checks are supporting verification only; the structural proofs above are analytic.
