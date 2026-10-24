SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B07, 2026-09-23T05:35:59Z.
attacking: coordinate-minor selection via three-sample determinant-volume routing, one-sided cross-fiber payment of four-coordinate cores, and a quantitative physical bi-coloop reduction.

# account01/B07 r17 — three-sample volume routing to a physical bi-anchor

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: coordinate minor selection / aggregate-before-inversion  
Status: `ESSENTIAL_STEP_APPLIED / NEW PHYSICAL BICOLOOP REDUCTION / FULL QFORM OPEN / WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture is not proved in this run. The new result is a dimension-free deterministic/analytic reduction for the current physical cross-block branch. It combines a newly available three-sample determinant-volume compiler with the designated partner account02/B07 cross-fiber theorem and then proves a new quantitative fact: if both determinant laws are forced into their near-coloop endpoints, the corresponding **actual physical row and column norms are automatically large**, yielding a substantial physical edge or a substantial complete incident `2x2` determinant bank. No individual tiny minor is selected or reciprocated.

## 1. Sources actually used

Fresh brain control at the beginning of this run was on OWNER CONTROL revision `2026-09-22.15`, with QFORM as the sole research target and no B07 pause. The run remains `WITHOUT_VERIFIED_BRAIN`; repository retrieval is not native learned-memory ingestion.

Mathematical sources:

1. **Designated partner account02/B07, latest completed compatible run.**  
   `yspennstate/math-open-problems@67a5863d5e97c6b27499ccf7690d6008965f62c3`,  
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260923T033624Z-account02-B07-fd9b69f8f3ff/REPORT.md`.  
   On the live four-bank branch it supplies
   
   `Z:=E3(M) >= (theta^2/6) F^6`, `F=||M||_F`,                 (1.1)
   
   together with the scale relation `F>kappa/Lambda` after the preceding large-star exit fails, and the fifth-volume small alternative
   
   `E5(M)<eta_* F^10`, `eta_*=theta^6/(120*3072^2)`,          (1.2)
   
   when the D5 exit does not fire. The concrete live collar used by that run is `theta=1/16`, `kappa=1/(256 sqrt(3))`, `Lambda=1`.

2. **Designated partner account02/B07 cross-fiber theorem.**  
   `yspennstate/math-open-problems@5266d24ea98d9bb5902c51a92eca0e3e38112e39`,  
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260922T193347Z-b07-639234ec/REPORT.md`.  
   If a physical cross block `B` has exactly `r` physical rows, full row rank `r>=3`, then the **full ambient quadratic form**, retaining arbitrary self blocks, outside couplings, affine terms and extra spectrum, has a continuous density with
   
   `||p_Q||_infinity <= sqrt(e) r/(r-2) det(BB^T)^(-1/(2r))`. (1.3)
   
   I apply this below at `r=3` to an actual row triple selected from a determinant-weighted four-row core.

3. **Three-sample volume compiler and stability, account02/B02.**  
   `yspennstate/math-open-problems@d6730c301e46e6337bc3b32e30eb3d04f07dc90b`,  
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260923T050831Z-account02-B02-QFORM-auto11-f98b4bb5/REPORT.md`.  
   For the canonical squared-`3x3`-minor row law of a physical cross block with `Z=E3(M)>0`, let
   
   `delta_R=P(R1 cap R2 cap R3=empty)`                         (1.4)
   
   for three iid row triples. If `delta_R>0`, the full form has a continuous density with
   
   `||p_Q||_infinity <= (9 sqrt(3)e/2) delta_R^(-1/6) Z^(-1/6)`. (1.5)
   
   If `delta_R<1/1024`, with `epsilon=1/4`, then either some physical row is a near coloop,
   
   `E3(M[I\{i},J])<Z/4`,                                      (1.6)
   
   or some four-row set `H` carries
   
   `E3(M[H,J]) >= (1-rho_0)Z`,                                (1.7)
   
   where
   
   `rho_0=167809/1016064=0.1651559350...`.                     (1.8)
   
   The same result applies to columns by transposition.

4. **Physical edge-or-incident-E2 algebra, account03/B07.**  
   `yspennstate/math-open-problems@287729053a28e2b51caa113509e7136c01e3e79d`,  
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260923T033734Z-account03-B07-qform-r23/REPORT.md`, Lemma `QFORM-PHYSICAL-ROWCOL-EDGE-OR-E2-v1`. If
   
   `M=[[b,r^T],[c,D]]`, `a=||row_i(M)||`, `d=||col_j(M)||`, `F=||M||_F`,
   
   then either
   
   `|b|>ad/(4F)`,                                             (1.9)
   
   or
   
   `||r||||c|| >=(15/16)ad`,
   `sqrt(Z_ij)>= (11/16)ad`,                                  (1.10)
   
   where
   
   `Z_ij=sum_{k!=i,l!=j} det M[{i,k},{j,l}]^2`.               (1.11)

5. **Own preceding Schur-compound sandwich.**  
   `yspennstate/math-open-problems@885b55c191d2964c24a21d8c5d806e32f24cdb53`, same B07 fleet root, r15. It proves for fixed physical row/column anchors `(i,j)` and all invertible incident physical `2x2` pivots with determinant `d_kl` and Schur residual `S_kl`,
   
   `H_(t+2)^(i,j) <= sum d_kl^2 E_t(S_kl) <=(t+1)^2 H_(t+2)^(i,j)`. (1.12)

Current source corrections are respected: no law-uniform pointwise quadratic stationary phase, no independence after spectral rotation, no arbitrary-joint rank-three coarea, no positive conditional-density-moment gate, and no one-small-minor reciprocal extraction are used.

## 2. Canonical third-volume law

Let `M=A[I,J]` be a physical cross block between disjoint original-coordinate banks. Put

`Z=E3(M)=sum_{|R|=|C|=3} det M[R,C]^2>0`,
`F=||M||_F`.                                                    (2.1)

Define the canonical probability law

`w(R,C)=det M[R,C]^2/Z`.                                       (2.2)

Its row and column inclusion marginals are

`alpha_i=P_w(i in R)`, `beta_j=P_w(j in C)`.                   (2.3)

Let `delta_R` be the probability that three iid row triples drawn from the row marginal of `w` have empty common intersection. Let `delta_C` be the analogous column quantity.

The new reduction starts by applying the three-sample theorem separately to rows and columns. A transpose does not rotate random coordinates: it merely exchanges the two already-disjoint original-coordinate banks.

## 3. First paid branch: genuine three-sample disjointness

If

`delta_R>=1/1024` or `delta_C>=1/1024`,                         (3.1)

then (1.5), on the corresponding side, gives the continuous-density estimate

`boxed:
 ||p_Q||_infinity
 <= (9 sqrt(3)e/2) 1024^(1/6) Z^(-1/6)
 <67.265 Z^(-1/6).
`                                                                  (3.2)

On the partner branch (1.1),

`Z^(-1/6) <= (6/theta^2)^(1/6) F^(-1)`,                       (3.3)

so after the inherited `F>kappa/Lambda`, this is a genuine dimension-free full-form bound

`||p_Q||_infinity
 <67.265 (6/theta^2)^(1/6) Lambda/kappa`.                      (3.4)

At `theta=1/16`, `kappa=1/(256sqrt(3))`, `Lambda=1`, the numerical cap is `<101310`. The size of this constant is irrelevant here; the point is that this entire determinant-support-diffuse branch is already paid with continuity and without a coordinate-minor reciprocal.

Thus an unpaid survivor may assume

`delta_R<1/1024`, `delta_C<1/1024`.                             (3.5)

## 4. Second paid branch: a four-coordinate determinant core

Apply the quantitative stability theorem (1.6)-(1.8) to the row law. Suppose it takes the four-row alternative, so `H` has at most four physical rows and

`E3(M[H,J]) >=(1-rho_0)Z`.                                    (4.1)

By Cauchy--Binet, this third-volume is the sum over the at most four physical row triples inside `H`:

`E3(M[H,J])
 =sum_{R subset H, |R|=3} det(M[R,J]M[R,J]^T).`                (4.2)

Hence some actual physical row triple `R_0 subset H` obeys

`D_(R_0):=det(M[R_0,J]M[R_0,J]^T)
 >=(1-rho_0)Z/4`.                                              (4.3)

In particular `M[R_0,J]` has full row rank three. Apply the **designated partner account02/B07 theorem (1.3)** at `r=3`. This pays the entire ambient form, not a truncated toy form:

`boxed:
 ||p_Q||_infinity
 <=3 sqrt(e) D_(R_0)^(-1/6)
 <=3 sqrt(e) [4/((1-rho_0)Z)]^(1/6)
 <6.423 Z^(-1/6).
}`                                                                  (4.4)

The density is continuous. On the partner collar this becomes

`||p_Q||_infinity
 <6.423 (6/theta^2)^(1/6) Lambda/kappa`.                       (4.5)

At the concrete `theta=1/16`, `kappa=1/(256sqrt(3))`, `Lambda=1`, this is `<9673`.

The same argument applies if the column stability theorem produces a four-column core, by transposition and using the corresponding one-sided partner theorem. Therefore a genuinely unpaid survivor of (3.5) must take the **near-coloop alternative on both sides**.

This is the required actual use of the designated partner result: the determinant-weighted four-coordinate stability packet is converted into the explicit inequality (4.4), with the full ambient quadratic form and all same-bank curvature retained.

## 5. New lemma: a third-volume coloop forces a large physical row

The near-coloop alternative has a stronger geometric consequence than merely a large determinant marginal.

### Lemma 5.1 — `QFORM-E3-MARGINAL-TO-PHYSICAL-ROW-NORM-v1`

For every real matrix `M`, every physical row `i`, and `Z=E3(M)`,

`alpha_i Z <= (1/2)||row_i(M)||_2^2 F^4`.                      (5.1)

Consequently, if

`Z >=(theta^2/6)F^6` and `alpha_i>3/4`,                        (5.2)

then

`boxed: ||row_i(M)||_2 > (theta/2)F.`                          (5.3)

The identical statement holds for columns.

### Proof

Let the physical row vectors be `m_1,...,m_p`. Summing the squared `3x3` minors first over columns gives

`alpha_i Z
 =sum_{k<l; k,l!=i} det Gram(m_i,m_k,m_l).`                     (5.4)

For every pair `(k,l)`, the squared three-volume is bounded by the squared length of `m_i` times the squared two-volume of the other pair:

`det Gram(m_i,m_k,m_l)
 <=||m_i||^2 ||m_k wedge m_l||^2`.                             (5.5)

Therefore

`alpha_i Z
 <=||m_i||^2 E2(M[-i,:])
 <=||m_i||^2 E2(M).`                                           (5.6)

If the squared singular values of `M` are `lambda_a`, then

`E2(M)=sum_{a<b}lambda_a lambda_b
 <=(1/2)(sum_a lambda_a)^2
 =F^4/2`.                                                       (5.7)

This proves (5.1). Under (5.2),

`||m_i||^2
 >=2 alpha_i Z/F^4
 >(3/2)(theta^2/6)F^2
 =theta^2F^2/4`,                                               (5.8)

which gives (5.3). QED.

This is a direct bridge from determinant-law concentration to an **actual original-coordinate physical norm**. No singular vector is selected and no coordinate rotation is made.

## 6. Main new reduction: diffuse volume or a strong physical bi-anchor

We can now combine Sections 3--5.

### Theorem 6.1 — `QFORM-TRIPLE-VOLUME-TO-PHYSICAL-BIANCHOR-v1`

Assume the live cross-block lower bound

`Z=E3(M)>=(theta^2/6)F^6`.                                     (6.1)

Then at least one of the following occurs.

**A. Three-sample Fourier payment.**  
The full form has a continuous density satisfying (3.2).

**B. Four-coordinate one-sided payment.**  
The full form has a continuous density satisfying (4.4).

**C. Physical bi-coloop survivor.**  
There are an actual physical row `i` and actual physical column `j` such that

`alpha_i>3/4`, `beta_j>3/4`,                                  (6.2)

hence

`boxed:
 ||row_i(M)||>(theta/2)F,
 ||col_j(M)||>(theta/2)F.
}`                                                                  (6.3)

Moreover the complete anchored third-volume packet obeys

`boxed:
 H3^(i,j)
 :=sum_{R contains i,C contains j, |R|=|C|=3} det M[R,C]^2
 >Z/2.
}`                                                                  (6.4)

### Proof

If either three-sample disjointness probability is at least `1/1024`, Section 3 applies. Otherwise apply the stability theorem to both row and column laws. A four-coordinate outcome on either side is paid by Section 4. Thus the survivor has row and column near-coloops. Since

`1-alpha_i=E3(M[I\{i},J])/Z<1/4`,                              (6.5)

and similarly for `beta_j`, (6.2) follows, then Lemma 5.1 gives (6.3). Finally, under the probability law (2.2), the union bound gives

`P(i in R, j in C)
 >=alpha_i+beta_j-1>1/2`.                                      (6.6)

Multiplying by `Z` proves (6.4). QED.

The significance is that the earlier vague “support-diffuse bi-anchor” survivor is now a quantitative **physical** object: two actual original-coordinate stars each have norm at least `theta F/2`, and more than half of all third-volume determinant currency passes through them jointly.

## 7. Compile the physical bi-anchor to edge or incident E2

Write the actual matrix around the anchors of Theorem 6.1 as

`M=[[b,r^T],[c,D]]`,                                           (7.1)

and set

`a=||row_i(M)||`, `d=||col_j(M)||`.                            (7.2)

By (6.3),

`ad>theta^2 F^2/4`.                                            (7.3)

Apply the general physical edge-or-E2 lemma (1.9)-(1.10). We obtain the new concrete alternative:

### Corollary 7.1 — `QFORM-BICOLOOP-EDGE-OR-INCIDENT-E2-v1`

In survivor C, either

`boxed: |M_ij| > theta^2 F/16`,                                (7.4)

or

`boxed:
 ||M[i,-j]||_2 ||M[-i,j]||_2
 >15 theta^2 F^2/64,
}`                                                                  (7.5)

and simultaneously

`boxed:
 sqrt(Z_ij)
 >11 theta^2 F^2/64,
}`                                                                  (7.6)

where `Z_ij` is the **complete** incident physical `2x2` squared-minor bank (1.11).

At the concrete live `theta=1/16`, these become

`|M_ij|>F/4096`,                                               (7.7)

or

`||M[i,-j]|| ||M[-i,j]|| >15F^2/16384`,                       (7.8)

`sqrt(Z_ij)>11F^2/16384`.                                      (7.9)

These constants are much stronger than the preceding generic bicore compiler because determinant near-coloop concentration itself forces the physical row/column norms.

If one also uses the inherited four-bank scale `C R F>kappa`, the edge branch carries the dimension-free product

`C R |M_ij| > theta^2 kappa/16`.                               (7.10)

No claim is made here that (7.4) or (7.5)-(7.6) alone already close the density theorem under arbitrary same-bank curvature; the corresponding product-preserving receiver remains a genuine analytic debt.

## 8. Strengthening the determinant-weighted Schur mixture

On the same physical bi-anchor, (6.4) improves the preceding r15 Schur-mixture constants.

From the Schur-compound sandwich (1.12), with

`Sigma_1=sum d_kl^2 E1(S_kl)`, `Sigma_3=sum d_kl^2 E3(S_kl)`,

we have

`Sigma_1>=H3^(i,j)>Z/2`,                                       (8.1)

`Sigma_3<=16E5(M)`.                                            (8.2)

Assume additionally that the partner D5 exit failed, so (1.2) holds. Define

`nu(k,l)=d_kl^2 E1(S_kl)/Sigma_1`.                             (8.3)

Then

`E_nu[E3(S)/E1(S)]
 <=16E5/H3
 <32E5/Z
 <192 eta_* theta^(-2)F^4
 =(8/5) theta^4 F^4/3072^2.`                                  (8.4)

By Markov, a set `G` carrying at least one half of the determinant-extension law satisfies

`E3(S)/E1(S)
 <(16/5) theta^4 F^4/3072^2`,                                 (8.5)

while its unnormalized currency obeys

`boxed:
 sum_G d_kl^2 E1(S_kl)
 >Z/4
 >=theta^2F^6/24.
}`                                                                  (8.6)

This improves the preceding r15 aggregate lower bound `theta^2F^6/36` to `theta^2F^6/24`.

Keep the same small-energy threshold

`rho_s=theta^2/(16sqrt(5))`.                                   (8.7)

For a good pivot with `s=E1(S)>=rho_s F^2`, (8.5) gives

`E3(S)/s^3 <1/2304`.                                           (8.8)

The existing elementary tail-to-third-volume inequality says that if

`T2(S):=dist_F(S,{rank<=2})^2 >=delta s`,

then

`E3(S)>=(delta^2/6)s^3`.                                       (8.9)

Taking `delta=1/(8sqrt(6))` and using (8.8) yields

`boxed:
 T2(S)<s/(8sqrt(6)),
 dist_F(S,{rank<=2})
 <(8sqrt(6))^(-1/2)||S||_F
 <0.225901 ||S||_F.
}`                                                                  (8.10)

Thus at least the currency (8.6) lies on physical `2x2` pivots whose Schur residual is either

`||S||_F < theta F/(4*5^(1/4))`,                               (8.11)

or lies within a relative `0.225901` Frobenius tube of rank two. This sharpens the previous `1/4` tube while increasing the guaranteed aggregate currency.

Again the determinant square remains attached to the pivot before any inversion; this is essential in the diffuse-third-direction stress examples.

## 9. What is now left for B07

The coordinate-minor selection problem on this live branch has been reduced to a substantially narrower endpoint:

1. a genuinely three-sample-diffuse determinant law is already continuously density-paid;
2. a near four-coordinate determinant support is already continuously density-paid by the designated partner's one-sided cross-fiber theorem;
3. otherwise there are **actual physical** row/column anchors with norms `>theta F/2`, joint anchored `E3` mass `>Z/2`, and hence either the strong physical edge (7.4) or the strong incident-E2/two-star resource (7.5)-(7.6);
4. if D5 also failed, more than `theta^2F^6/24` of determinant-extension currency sits on physical `2x2` pivots whose Schur residual is small-energy or within `0.225901` of rank two.

The first unpaid implication is therefore

`QFORM-BICOLOOP-EDGE-E2-SCHUR-MIXTURE-RECEIVER-v1`:

prove a product-preserving full-form density/half-Riesz estimate from either the edge-times-outer-stars resource or the incident-E2-plus-inner-stars resource, or spend the determinant-weighted Schur family (8.6) **before reciprocal inversion**, while retaining arbitrary same-bank quadratic curvature and the true nonzero residual tail.

This is not a claim that the full QFORM conjecture is solved. Global continuity remains open; continuity is proved only on paid branches A and B above. The structural survivor itself carries no new continuity conclusion.

## 10. Exact constants / regression status

The exact rational constants used in the three-sample stability collar are

`eta=1/256`, `tau=128/3969`, `rho_0=167809/1016064`.

The numerical values used above are

`rho_0=0.165155935059...`,
`(9sqrt(3)e/2)1024^(1/6)=67.26424664...`,
`3sqrt(e)[4/(1-rho_0)]^(1/6)=6.42210793...`,
`(8sqrt(6))^(-1/2)=0.2259005009...`.

A finite exact/integer regression checker is saved beside this report. It checks the row-marginal norm inequality on deterministic integer matrices and the displayed rational constant identities. These checks are only regression evidence; the proof above is analytic.
