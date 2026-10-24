SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B06, 2026-09-23T18:19:04Z.
attacking: the ultra-thin two-single-hub survivor; convert the robust opposite-star/cofactor packet into a weighted curved-fiber bound or a sharper finite-hub reduction without dropping the nonzero tail.

# account03/B06 r41 — reciprocal physical anchoring of the projected rank-one survivor

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** revision `2026-09-22.15`, programme revision `2026-09-22.5`  
**Assignment:** Curved fiber integration  
**Status:** `NEW SUPPORTING STRUCTURAL THEOREM + <347 PAID BRANCH / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and source-valid inputs

The exact target remains: independent ORIGINAL real coordinates with probability densities bounded by one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No moment, support, iid, Gaussian, log-concavity, connected-support, sign, finite-rank, or independence-after-rotation hypothesis is introduced. The desired continuous representative is tracked separately from essential boundedness.

This run continues the literal ORIGINAL-coordinate r40 packet at

`yspennstate/math-open-problems@a867a320432a932e279f704d60b0c833ff4acbd5`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260923T171937Z-account03-B06-qform-r40/REPORT.md`.

The completed account04 theorem actually applied is

`yspennstate/math-open-problems@c6f29397b3d45a7cf7ab67633a5451767b478912`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B20/20260923T142031Z-account04-B20-QFORM-r10/REPORT.md`.

In the no-moderate-diagonal branch it supplies an ORIGINAL-coordinate cut `[n]=J disjoint_union K`, `N=A[J,K]`, with

`E:=||N||_F^2 > E0:=11907/16384`.                                  (1.1)

The exact designated `account04/B06` canonical QFORM directory was still absent at the source check, so no result is fabricated for that slot. The compatible completed account04/B20 result above is used at the actual inequality (1.1).

The analytic receiver used is account03/B01's row-marginal-free one-hub projected-E2 theorem,

`yspennstate/math-open-problems@585b5a3ca7e887e5cd16f45ea49056d548361dfb`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260923T173320Z-auto11-heavyrowpromotion/REPORT.md`.

For a literal original hub with hub-to-bank vector `m`, projected crossing `C`, and `Z=e_2(CC^T)>0`, it proves a continuous `C_0` density with

`||p_Q||_infinity <= C_E2 (||m||^2 Z)^(-1/6)`,                     (1.2)

where

`C_E2=3*2^(7/6)*exp(1/3)=9.3991318878...`.

Its underlying arbitrary-rank projected-crossing theorem is independently checked at

`yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

The live corrections are retained: no arbitrary-joint coarea cap, no positive moment of worst conditional projection-density caps, no law-uniform pointwise quadratic-phase decay, no independence after rotation, no unrestricted spectral-fiber supremum, no one-good-minor extraction, and no deletion of a small nonzero quadratic tail on arbitrary unbounded inputs. The newest Claude `(SP)` single-hub conditional-adaptation estimate remains OPEN and is not used.

## 2. The r40 ultra-thin packet

Let the squared singular values of `N` be `x1>=x2>=...>=0`. The r40 survivor has

`Z2:=e_2(N^TN) > (31/2048)E^2`,                                    (2.1)

and both determinant-pair disjointness probabilities are below `1/256`. Hence r40 supplies one literal physical row `i in J` and one literal physical column `a in K` whose determinant-pair inclusion marginals satisfy

`alpha_i>3/5`, `beta_a>3/5`.                                       (2.2)

Their dominant top-two singular-plane leverages exceed `19/32`. In particular, using the absolute floor `x2>E0/64`, the full row and column cross-star norms satisfy

`||N[i,K]||^2, ||N[J,a]||^2 > M0^2`,                               (2.3)

where

`M0^2=(19/32)(E0/64)=226233/33554432
      =0.006742268800735474...`.                                   (2.4)

The large mutual-edge branch `|A_ia|>=1/32` was already paid in r40 by the completed physical-pair theorem (`||p_Q||_infinity<547`). Therefore this run studies only

`|b|:=|A_ia|<1/32`.                                                  (2.5)

Nothing below removes the nonzero ultra-thin singular tail.

## 3. Exact weighted row-projection identities

Permute the anchors first and write

`N=[[b,r^T],[c,D]]`.                                                 (3.1)

Let

`m=(b,r)`, `M^2=||m||^2`,
`C=N[i^c,K](I-P_m)`, `S=||C||_F^2`,                                (3.2)

where `P_m` is orthogonal projection onto `span(m)` in the literal `K` coefficient space. For a remaining physical row `y`, put

`z=y(I-P_m)`, so `z perpendicular m`.                               (3.3)

### Lemma 3.1 — full row-pair volume after projection

The complete squared-minor mass involving row `i` is

`W_i:=sum_(j!=i) sum_(|T|=2) det N[{i,j},T]^2 = M^2 S`.             (3.4)

Proof. For each `j`, Cauchy--Binet/Lagrange gives

`sum_(|T|=2)det N[{i,j},T]^2=||m wedge y_j||^2`.

Replacing `y_j` by its orthogonal residual `z_j` does not change the wedge and gives `||m wedge z_j||^2=M^2||z_j||^2`. Sum over `j`. QED.

Since `W_i=alpha_i Z2`, (2.1)-(2.2), `M^2<=E`, and (1.1) imply

`S > (3/5)(31/2048)E = (93/10240)E > S0`,                           (3.5)

with

`S0=1107351/167772160=0.006600326299667359...`.                     (3.6)

This lower bound uses the complete determinant-pair law before selecting the physical anchor.

### Lemma 3.2 — anchored cofactor equals weighted projected-column energy

Let

`Z_ia=sum_(j!=i,beta!=a) det N[{i,j},{a,beta}]^2`.                  (3.7)

Then exactly

`boxed: Z_ia = b^2 S + M^2 ||C e_a||_2^2.`                         (3.8)

Proof. For one residual row `z=(z_a,z_tail)`, the anchored minor vector is

`f=b z_tail-z_a r`.                                                  (3.9)

Because `z perpendicular m`,

`r dot z_tail=-b z_a`.                                              (3.10)

Therefore

`||f||^2
 =b^2||z_tail||^2-2b z_a(r dot z_tail)+||r||^2 z_a^2
 =b^2||z||^2+(b^2+||r||^2)z_a^2
 =b^2||z||^2+M^2 z_a^2`.                                           (3.11)

Summing (3.11) over every remaining physical row proves (3.8). QED.

This identity is valid also at `b=0`; no division by the anchor edge occurs.

## 4. The opposite physical anchor carries at least 18.849% of the whole projected crossing

Normalize all squared `2x2` minors of `N` by `Z2` to a joint law on physical row pairs and column pairs. Let

`theta=P(i in row-pair AND a in column-pair)=Z_ia/Z2`.              (4.1)

By the union bound and (2.2),

`theta >= alpha_i+beta_a-1 > alpha_i-2/5`.                          (4.2)

Using (3.4),

`Z_ia/(M^2S)=theta/alpha_i
 >1-(2/5)/alpha_i
 >1/3`.                                                             (4.3)

Combine (3.8), (4.3), (2.3)-(2.5):

`||C e_a||^2/S
 >1/3-b^2/M^2
 >1/3-(1/1024)/M0^2
 =42643/226233`.                                                     (4.4)

Thus

`boxed: ||C e_a||^2 > 0.1884915109... ||C||_F^2.`                  (4.5)

This is the main new weighted replacement. It does not maximize a curved fiber or select an individual minor. The entire row-pair volume and the entire joint anchored cofactor bank are first aggregated; only then does the product-coordinate label `a` emerge.

## 5. Either the projected two-volume pays, or the survivor is >99.72% rank one and reciprocally anchored

Choose the fixed universal threshold

`epsilon=2^-24`.                                                     (5.1)

### Paid branch

If

`e_2(CC^T)>=epsilon`,                                                (5.2)

then apply the completed account03/B01 theorem (1.2). By (2.3),

`||p_Q||_infinity
 <=C_E2(M^2 epsilon)^(-1/6)
 <C_E2(M0^2 epsilon)^(-1/6)
 =345.9978359... <347.`                                             (5.3)

The cited theorem gives a continuous `C_0` density in this branch. All same-bank curvature and every nonzero tail direction remain in the full ambient form.

### Rank-one survivor

Assume instead

`e_2(CC^T)<epsilon`.                                                 (5.4)

Let `y1>=y2>=...` be the squared singular values of `C` and

`tau=sum_(k>=2)y_k=S-y1`.                                           (5.5)

Since

`S^2=sum_k y_k^2+2e_2(CC^T) <= y1 S+2epsilon`,                     (5.6)

we have

`tau<2epsilon/S<2epsilon/S0
    =20/1107351
    =1.8061120638e-5`.                                              (5.7)

More importantly,

`tau/S < 2epsilon/S0^2
 =3355443200/1226226237201
 =0.002736398144...`.                                               (5.8)

Hence the leading singular direction carries more than

`1-0.002736399 > 99.7263%`                                         (5.9)

of the complete projected crossing energy.

Let `v1` be a leading right singular vector of `C`. From the singular expansion,

`||C e_a||^2
 =sum_k y_k |(v_k)_a|^2
 <=y1 |(v1)_a|^2+tau`.                                              (5.10)

Equations (4.4), (5.8), and `y1<=S` give

`|(v1)_a|^2
 >(42643/226233)
  -(3355443200/1226226237201)`

`=4327778067649/23298298506819
 =0.185755112820...`.                                               (5.11)

Therefore

`boxed: |(v1)_a|^2>0.1857551,  |(v1)_a|>0.430993.`                  (5.12)

So failure of the `<347` projected-E2 receiver does not leave a diffuse rank-one direction: the leading residual direction places more than 18.57% of its squared mass on the already identified opposite ORIGINAL coordinate `a`.

## 6. Transpose and the reciprocal-anchor theorem

Apply the same argument to `N^T`, using the physical column anchor `a` as the literal hub and row anchor `i` as the opposite coordinate. Put

`n=N[J,a]`,
`C_a=N^T[K\{a},J](I-P_n)`.                                         (6.1)

The same absolute star floor (2.3) holds. Therefore either

`e_2(C_a C_a^T)>=2^-24`,                                            (6.2)

and the full ambient form again has a continuous density with

`||p_Q||_infinity<347`,                                             (6.3)

or `C_a` is more than `99.7263%` rank one in Frobenius energy and a leading right singular vector `u1` satisfies

`boxed: |(u1)_i|^2>0.1857551,  |(u1)_i|>0.430993.`                  (6.4)

### Theorem 6.1 — `QFORM-ULTRATHIN-RECIPROCAL-PROJECTED-ANCHOR-v1`

Under the r40 simultaneous low-disjointness ultra-thin packet and the unpaid mutual-edge branch `|A_ia|<1/32`, one of the following occurs:

1. the full ambient quadratic form has a continuous `C_0` density with `||p_Q||_infinity<347`; or
2. both one-hub projected crossing matrices are quantitatively rank one: each has at most `0.27364%` of its Frobenius energy outside the leading singular direction, and each leading residual singular direction is reciprocally pinned to the opposite literal physical anchor with squared coordinate mass `>0.1857551`.

No nonzero singular tail of `A` or `N` is set to zero. No spectral-coordinate independence is asserted.

## 7. How this advances the curved-fiber route

The remaining r40 obstruction had two robust opposite stars and a robust cofactor bank, but it was still possible that the projected crossing theorem failed because its two-volume was tiny. Theorem 6.1 converts that failure into a much narrower geometric state: the projected crossings are almost rank one **and their leading directions are not free rotations**; they are quantitatively attached to the opposite original coordinates `i,a`.

The next exact B06 debt is

`QFORM-RECIPROCAL-RANK1-TWOHUB-RECEIVER-v1`:

retain the two physical hubs `i,a`, the `>0.43099` reciprocal projected anchors, the robust opposite stars from r40, arbitrary same-bank quadratic curvature, and the complete nonzero ultra-thin tail; prove that either a two-hub-plus-one-crossing grouped theorem has a universal parameter, or route the exact limiting double-star packet through a dependence-safe curved two-hub receiver. The small hub block must be kept exactly; it cannot be treated as a small random perturbation without moment assumptions.

## 8. Checks and status

`check_r41.py` verifies the exact rational constants and tests (3.4), (3.8) on 1,000 random matrices. Maximum normalized discrepancies were `1.10e-15` and `6.01e-16`. These are sanity checks only; Sections 3--6 are the proofs.

**Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED. Global continuity remains OPEN.** Continuity is proved here only on the projected-E2 paid branch through the cited account03/B01 theorem. This run remains `WITHOUT_VERIFIED_BRAIN`: repository source retrieval and publication occurred, but no authenticated native mathematical-memory receiver use was established.
