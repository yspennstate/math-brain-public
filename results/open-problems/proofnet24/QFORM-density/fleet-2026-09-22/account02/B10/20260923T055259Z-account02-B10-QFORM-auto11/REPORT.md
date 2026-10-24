SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B10, 2026-09-23T05:52:59Z.
attacking: the exact-rank-three near-null nonzero coloop collar, using the ruled one-sheet theorem and the designated partner's mixed-transverse excision while preserving original-coordinate product provenance.

# account02/B10 auto11 — constant hub Pluecker packet in the high-slope survivor, and a target-valid local-certificate collapse family

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** rank-three coupled case; complementary constructions/source-valid counterexamples  
**Run id:** `20260923T055259Z-account02-B10-QFORM-auto11`  
**Fresh owner control resolved before work:** `yspennstate/math-research-brain@b54c03bdbc451f9ec5399cf8dddbf80af4428d7e`, OWNER CONTROL revision `2026-09-22.15`; final control was refreshed again before publication.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_LEMMA / SOURCE-VALID LOCAL-CERTIFICATE OBSTRUCTION / FULL QFORM OPEN`.

The exact target is unchanged: arbitrary independent real original-coordinate inputs with one-dimensional densities at most one, and an arbitrary real symmetric matrix with at least three eigenvalues of modulus at least one. No moment, support, log-concavity, identical-law, diagonal-basis, spectral-coordinate independence, or post-rotation independence assumption is used. Continuity is separate from the essential-density question.

## 1. First unpaid implication

The first unpaid implication is now

`QFORM-HIGHSLOPE-HUBPACKET-BANK-PAYMENT-v1`:

> In the designated-partner exact-rank-three near-coloop survivor, use one of the constant aggregate hub-transverse Pluecker packets proved below to control the **two-sheet** output side while retaining original-coordinate product provenance. A proof may not pigeonhole the packet into a single physical pivot, pair, or triple: Section 5 gives a target-valid family in the exact survivor where every such local certificate tends to zero while the aggregate packet stays constant.

The required `e5f71d79eff325201dd0274053d20268ce65b837` ruled theorem already pays the one-sheet side. Thus the debt isolated here is genuinely the minority/two-sheet trace of the same product projection, not the cone or one-sheet geometry.

## 2. Sources actually consumed

### 2.1 Required Claude package

I read the pinned package

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`, including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

The completed result used at a real inequality below is its ruled one-sheet theorem. For an exact rank-three form with signature `(2,1)` and spectral magnitudes at least one, the density on the one-sheet side, including the cone level, obeys

`p_Q(t) <= pi sqrt(2)`                                              (2.1)

for the unit spectral scale. Its proof uses line integrals of the actual three-dimensional product projection and bounds those line integrals by two-dimensional marginals of the ORIGINAL product source; it does not assert independence after spectral rotation.

The same package records why an arbitrary bounded three-dimensional joint density is not an admissible surrogate: shell concentration defeats the discarded-product coarea bound. That correction is respected throughout.

### 2.2 Designated partner account03/B10

The latest completed designated-partner result found at the source refresh is account03/B10 r24,

`QFORM-NEARCOLOOP-MIXED-TRANSVERSE-EXCISION-v1`,

canonical mathematics

`yspennstate/math-open-problems@06f180467d43940acc1f939e216db2e23b7d7c88`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B10/20260923T044329Z-account03-B10-QFORM-r24/REPORT.md`.

It consumes earlier B10 exits and reduces a still-unpaid exact-rank-three state to

`A=R Lambda R^T`, `R^T R=I_3`, `sigma_min(Lambda)>=1`, `D=|det Lambda|>=1`,

`r_0=sqrt(c)e`, `c>63/64`, `rho=1-c<1/64`,                       (2.2)

and complementary physical rows

`r_j=s_j e+w_j`, `w_j perpendicular e`,

`sum_j s_j^2=rho`, `sum_j s_j w_j=0`, `sum_j w_jw_j^T=I_2`.       (2.3)

Every complementary transverse row has squared transverse leverage `<1/4`. Let `M` be the genuinely mixed rows (`s_j!=0` and `w_j!=0`), and put

`rho_M=sum_(j in M)s_j^2`, `H_M=sum_(j in M)w_jw_j^T`,

`eta=||H_M||op`.                                                    (2.4)

The partner proves a real output bound

`eta<=7/8  ==>  ||p_Q||infinity <425`.                             (2.5)

Hence I consume (2.5) and work only in its sole survivor

`eta>7/8`, `rho_M<1/64`.                                           (2.6)

Its exact cancellation then yields opposite mixed slopes. If `v` is a top eigenvector of `H_M`, `z_j=(v dot w_j)/s_j`, and `p_j=s_j^2/rho_M`, then

`sum p_j z_j=0`, `sum p_j z_j^2=eta/rho_M>56`,                    (2.7)

so some `z_+>0>z_-` satisfy `z_+|z_-|>56`. I do not try to pay one such pair locally; Section 5 shows that this would lose the dimension-free scale.

## 3. New exact lemma: the hub incident Pluecker mass never becomes small

The near-coloop parameter `rho` can tend to zero, but the three-dimensional exterior volume through the hub does **not** tend to zero.

### Lemma 3.1 — `QFORM-NEARCOLOOP-HUB-PLUCKER-PACKET-v1`

Assume only the Parseval geometry (2.2)-(2.3). Then

`boxed: sum_(j<k; j,k!=0) det(r_0,r_j,r_k)^2 = c.`                (3.1)

Equivalently, since exact rank three gives

`det A[S,S]=det(Lambda) det(R_S)^2`,                               (3.2)

the aggregate absolute physical principal-determinant mass over all triples containing the hub is

`boxed: sum_(j<k; j,k!=0) |det A[{0,j,k},{0,j,k}]| = D c >= c.`    (3.3)

**Proof.** In the orthogonal decomposition `R e direct_sum e^perp`, adding a multiple of the hub direction to either leaf does not change the determinant with the hub. Hence

`det(r_0,r_j,r_k)^2 = c det(w_j,w_k)^2`.                           (3.4)

By the transverse Parseval identity in (2.3) and two-dimensional Cauchy--Binet,

`sum_(j<k) det(w_j,w_k)^2
 =det(sum_j w_jw_j^T)
 =det I_2
 =1`.                                                             (3.5)

Multiplying by `c` proves (3.1); (3.2) gives (3.3). QED.

The point is structural: the near-coloop is not losing rank-three volume. It is losing **localization** of that volume.

## 4. New packet topology forced by the partner high-slope survivor

Split the complementary transverse rows into the partner's mixed bank `M` and its complement `T`; rows in `T` may be pure transverse or pure longitudinal, but pure longitudinal rows have `w_j=0` and are harmless. Set

`H=H_M=sum_(j in M) w_jw_j^T`.

Then the transverse Gram of `T` is `I_2-H`. Let the eigenvalues of `H` be

`eta>=xi>=0`.                                                       (4.1)

Define three hub-incident packets by whether the two leaves lie in `M,M`, in `M,T`, or in `T,T`:

`P_MM=sum_(j<k in M) det(r_0,r_j,r_k)^2`,

`P_MT=sum_(j in M,k in T) det(r_0,r_j,r_k)^2`,

`P_TT=sum_(j<k in T) det(r_0,r_j,r_k)^2`.                          (4.2)

Then

`boxed: P_MM=c eta xi,`                                            (4.3)

`boxed: P_MT=c[eta(1-xi)+xi(1-eta)],`                              (4.4)

`boxed: P_TT=c(1-eta)(1-xi).`                                      (4.5)

In particular `P_MM+P_MT+P_TT=c`, recovering (3.1).

**Proof.** The same-set formulas are Cauchy--Binet:

`P_MM=c det H`, `P_TT=c det(I-H)`.                                 (4.6)

For the cross packet, use in two dimensions

`det(x,y)^2=||x||^2||y||^2-(x dot y)^2`.

Summing over `j in M,k in T` gives

`P_MT/c
 =tr(H) tr(I-H)-tr(H(I-H))`.                                    (4.7)

Diagonalize `H`; (4.7) becomes

`eta(1-xi)+xi(1-eta)`, proving (4.4). QED.

Now consume the partner inequality (2.5). In an unpaid state `eta>7/8`. Therefore there is a universal packet dichotomy:

- if `xi>=1/2`, then

  `P_MM=c eta xi > 7c/16`;                                        (4.8)

- if `xi<1/2`, then

  `P_MT >= c eta(1-xi) > 7c/16`.                                  (4.9)

Since `c>63/64`, in either case the relevant aggregate Pluecker packet exceeds

`(7/16)(63/64)=441/1024 >0.4306`.                                 (4.10)

Thus the high-slope survivor has a **constant bank-level rank-three resource**. What is missing is an analytic receiver that spends this packet without first extracting one determinant.

This sharpens the partner's first unpaid implication. The remaining geometry is not merely “two opposite high slopes”; it is either

1. a hub plus a full-rank mixed transverse bank carrying packet `>7c/16`, or
2. a hub plus one mixed and one pure-transverse bank carrying cross packet `>7c/16`.

Both statements are formulated on disjoint sets of ORIGINAL coordinates; no random spectral rotation has been performed.

## 5. Target-valid family inside the exact high-slope survivor: every local certificate collapses

The packet dichotomy cannot be converted to a single uniformly good physical pivot, pair, or triple. The following exact target family lies inside the partner's sole survivor and spreads the constant packet over quadratically many tiny triples.

### Proposition 5.1 — `QFORM-HIGHSLOPE-LOCAL-CERTIFICATE-COLLAPSE-v1`

For every even integer `m>=64` there is an exact-rank-three matrix `A_m` with nonzero spectrum `{1,1,-1}` satisfying the partner near-coloop survivor, with

`c=127/128`, `rho=1/128`, `rho_M=1/256`, `eta=15/16`,              (5.1)

and mixed-slope product

`z_+|z_-|=240>56`,                                                  (5.2)

such that

`max_i |(A_m)ii| <= 1/m`,                                          (5.3)

`max_(i<j) |det A_m[{i,j},{i,j}]| <= 2/m`,                         (5.4)

`max_(|S|=3) |det A_m[S,S]| <= c/m^2 <1/m^2`,                     (5.5)

while the exact hub packet stays

`sum_(j<k;j,k!=0)|det A_m[{0,j,k},{0,j,k}]|=c=127/128`.            (5.6)

Moreover the required ruled theorem gives, for arbitrary admissible independent cap-one inputs,

`boxed: p_(X^T A_m X)(0) <= pi sqrt(2).`                           (5.7)

Hence this is not a QFORM counterexample. It is a source-valid counterexample to any proof step that tries to pay the partner high-slope survivor by extracting one uniformly conditioned physical pivot, pair, or triple from the constant aggregate packet.

### Construction

Work in a spectral orthonormal basis `(e,v,u)`. Put

`epsilon=1/m`, `s=sqrt(1-epsilon^2)`,

`Lambda_m = [[-epsilon,0,s],[0,1,0],[s,0,epsilon]].`               (5.8)

The `(e,u)` block has trace zero and determinant `-1`, so its eigenvalues are `+1,-1`; the `v` eigenvalue is `+1`. Therefore

`spec Lambda_m={1,1,-1}`, `Lambda_m^2=I_3`, `|det Lambda_m|=1`.     (5.9)

Use `4m+1` physical rows. First the hub

`r_0=sqrt(127/128)e`.                                               (5.10)

Next the mixed bank consists of `m` rows

`r_j=sqrt(1/(256m)) e + sigma_j sqrt(15/(16m)) v`,                 (5.11)

where exactly half of the signs `sigma_j` are `+1` and half are `-1`. Add three pure banks, each of size `m`:

`r_j^L=sqrt(1/(256m))e`,                                           (5.12)

`r_j^V=sqrt(1/(16m))v`,                                            (5.13)

`r_j^U=(1/sqrt(m))u`.                                               (5.14)

Let `R_m` be the matrix with these rows and define

`A_m=R_m Lambda_m R_m^T`.                                          (5.15)

### Parseval and exact partner state

The spectral masses are

`e:` `127/128 +1/256+1/256=1`,

`v:` `15/16+1/16=1`,

`u:` `1`.                                                          (5.16)

The only possible cross Gram contribution is from the mixed bank, and it vanishes because `sum sigma_j=0`. Thus

`R_m^T R_m=I_3`.                                                    (5.17)

Consequently `A_m` has exactly the nonzero spectrum (5.9).

The hub has

`c=127/128>63/64`, `rho=1-c=1/128<1/64`,

`alpha=e^T Lambda_m e=-1/m`, so `|alpha|<1/16`.                    (5.18)

Every complementary transverse squared row norm is `<1/4` for `m>=64`. The partner's genuinely mixed set is exactly the bank (5.11), and

`rho_M=m(1/(256m))=1/256`,                                        (5.19)

`H_M=m(15/(16m)) vv^T=(15/16)vv^T`,                               (5.20)

so

`eta=15/16>7/8`.                                                    (5.21)

For its top eigenvector `v`, every mixed slope is

`z_j=(v dot w_j)/s_j=sigma_j sqrt((15/16)/(1/256))
    =sigma_j sqrt(240)`.                                           (5.22)

Thus opposite signs satisfy the exact numerical partner obstruction

`z_+|z_-|=240>56`.                                                  (5.23)

This applies the partner r24 survivor inequalities to an actual target matrix, rather than merely restating the theorem.

### Collapse of all scalar pivots

For a spectral row `x=x_e e+x_v v+x_u u`,

`x^T Lambda_m x
 =-epsilon x_e^2+x_v^2+2s x_e x_u+epsilon x_u^2`.                  (5.24)

The hub pivot has magnitude

`epsilon c=c/m<1/m`.                                               (5.25)

A mixed-row pivot is

`15/(16m) - 1/(256m^2) <1/m`.                                    (5.26)

The pure `V`, `U`, and `L` pivots have magnitudes respectively

`1/(16m)`, `1/m^2`, `1/(256m^2)`.                                 (5.27)

This proves (5.3).

### Collapse of all physical pairs

Because `Lambda_m` is a symmetric orthogonal matrix, for arbitrary row vectors `x,y`

`|x^T Lambda_m x|<=||x||^2`,

`|x^T Lambda_m y|<=||x|| ||y||`.                                  (5.28)

Hence the determinant of the associated physical `2x2` Gram block obeys

`| (x^T Lambda_m x)(y^T Lambda_m y)-(x^T Lambda_m y)^2 |
 <=2||x||^2||y||^2`.                                               (5.29)

Every non-hub row in (5.11)-(5.14) has squared norm at most `1/m`, whereas the hub has squared norm `c<1`. Thus (5.4) follows. The scale is real, not merely an upper-bound artefact: for the hub and any pure `U` row,

`det A_m[{0,U},{0,U}] = -c/m`.                                    (5.30)

So even the strongest pair is only order `1/m`.

### Collapse of all physical triples, despite constant total packet

For every physical triple `S`, exact rank three and (5.9) give

`|det A_m[S,S]|=det(R_{m,S})^2`.                                  (5.31)

If `S` contains the hub, the other two row norms are at most `m^(-1/2)`, so Hadamard gives

`|det A_m[S,S]|<=c/m^2`.                                          (5.32)

If the hub is absent, the stronger bound `<=1/m^3` holds. This proves (5.5).

On the other hand, the packet identity (3.3) gives exactly (5.6). In this explicit rank-one `H_M` case the distribution is especially transparent. A hub + mixed row + pure-`U` row has determinant magnitude

`c (15/16)/m^2`,                                                   (5.33)

and there are `m^2` such mixed--`U` choices, whose aggregate is

`c(15/16)`.                                                        (5.34)

The remaining pure-`V`--pure-`U` hub triples contribute `c/16`, so the total is exactly `c`. Thus a constant exterior packet can be spread over `Theta(m^2)` principal triples, each of size `Theta(m^(-2))`.

### Required ruled theorem applied at an actual density inequality

The form `A_m` has exact nonzero spectrum `{1,1,-1}` and the source variables are still the original independent cap-one coordinates. Therefore the ruled one-sheet theorem from the required `e5f71d...` package applies directly, with unit spectral scale, to the cone level:

`p_(X^T A_m X)(0) <= pi sqrt(2)`.                                  (5.35)

This is the promised actual use of a completed result from the required source package. No projected coordinates are declared independent. The theorem itself controls the relevant line integrals through marginals of the original product source.

Thus (5.3)-(5.6) are an obstruction to a proof interface, not an unbounded-density construction. In fact the same family is uniformly paid on the entire one-sheet half-line by the same ruled theorem. What remains is its two-sheet side, exactly matching the owner proof map.

## 6. Relation to the nonzero-null interpolation

The family (5.8)-(5.15) also makes the nonzero-null nature explicit:

`alpha=-1/m ->0`, while `c=127/128` is fixed and the physical hub star stays macroscopically coupled. Since `Lambda_m^2=I`,

`sum_(j!=0) (A_m)_(0j)^2
 =(A_m^2)_(00)-(A_m)_(00)^2
 =c-epsilon^2 c^2
 ->c`.                                                             (6.1)

So the hub is not decoupling as its scalar quadratic pivot tends to zero.

The exact-null endpoint `alpha=0` is already paid elsewhere in the current graph by a product-valid independent-scalar/dependent-projection kernel. The prior B10 minority-discriminant theorem pays fixed nonzero minority Rayleigh scale but has a factor `|alpha|^(-1/4)`; on (5.18) that bound grows like `m^(1/4)`. Equation (5.35) shows that this growth is not intrinsic on the cone. The missing two-sheet interpolation must retain aggregate bank information that the scalar discriminant loses.

The construction also respects the live correction that a bounded dependent projected pair is not a replacement for original product provenance. Here the only density conclusion (5.35) is obtained from a theorem proved for the actual product projection, not from an arbitrary-joint density cap.

## 7. What the new packet lemma rules in and rules out

The packet theorem gives a clean structural fork after the partner's `<425` moderate-overlap exit:

1. `xi>=1/2`: the **mixed bank itself** has full transverse rank and the hub + two-mixed aggregate packet is `>7c/16`.
2. `xi<1/2`: the mixed bank is effectively one-transverse-direction heavy, but its cross packet with the pure-transverse remainder is `>7c/16`.

The explicit family realizes the second case with `xi=0` and shows that the packet may be arbitrarily delocalized. Therefore the next analytic theorem must spend the packet at bank level. A route based on “choose the best pair/triple and pay its reciprocal determinant” necessarily loses at least a power of `m` on this family.

The result does **not** prove that every aggregate packet has a dimension-free two-sheet trace. That is exactly the unpaid implication. Nor does it claim a counterexample to QFORM: the required ruled theorem supplies the uniform cone/one-sheet bound (5.35).

## 8. Deterministic regression

`CHECK.py` and `CHECK_OUTPUT.txt` in this immutable run directory verify the Parseval identity, the spectrum of `Lambda_m`, the scalar and pair bounds, a representative hub-triple scale, the exact packet value `127/128`, and the exact slope product `240` for `m=64,128,256`. The checker ends `STATUS=PASS`. The arbitrary-`m` proposition is proved by the formulas above; the finite checks are only regression diagnostics.

## 9. Final status

- Full arbitrary-spectrum QFORM target: **OPEN**.
- Full exact-rank-three target: **OPEN**.
- Required ruled-side theorem: **CONSUMED at the concrete inequality (5.35)**.
- Designated partner r24 moderate-overlap theorem: **CONSUMED at (2.5)**; its sole high-slope survivor is the state analyzed here.
- `QFORM-NEARCOLOOP-HUB-PLUCKER-PACKET-v1`: **PROVED**.
- High-slope packet dichotomy `(P_MM>7c/16) OR (P_MT>7c/16)`: **PROVED**.
- `QFORM-HIGHSLOPE-LOCAL-CERTIFICATE-COLLAPSE-v1`: **PROVED as an exact target-valid obstruction to local-certificate extraction**, not a QFORM counterexample.
- First unpaid implication: **`QFORM-HIGHSLOPE-HUBPACKET-BANK-PAYMENT-v1`**, specifically on the two-sheet side and with original-coordinate product provenance retained.