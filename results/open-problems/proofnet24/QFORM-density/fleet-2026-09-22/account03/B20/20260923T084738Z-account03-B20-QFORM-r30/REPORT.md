SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B20, 2026-09-23T08:47:38Z.
attacking: the fresh finite double-coloop survivor by compiling it into either a quantitatively full finite physical core or three disjoint original-coordinate packets carrying three orthogonal spectral directions.

# account03/B20 r30 — finite double-coloop to three-packet compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Proof closure and keeper  
**Control at start:** `yspennstate/math-research-brain@fa94e318691b6afc620478d2d99c0086d8502629`, OWNER CONTROL revision `2026-09-22.15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** `ESSENTIAL_STEP_APPLIED / NEW PRODUCT-PRESERVING STRUCTURAL COMPILER / FULL QFORM OPEN`.

The unrestricted conjecture remains OPEN. No Gaussian, log-concave, moment, support, diagonal-basis, or post-rotation independence hypothesis is introduced. All packets below are sets of ORIGINAL coordinates, so packet independence is genuine. Continuity is recorded separately from essential boundedness.

## 1. Fresh incoming state

The newest compatible closure input is account02/B20 r25:

`yspennstate/math-open-problems@1ed18b869e338fb93f2cf0572928ab124d8e34aa`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B20/20260923T082458Z-account02-B20-QFORM-r25/REPORT.md`.

Inside the exact-rank-three chamber it writes

`A=R M R^T`, `R^T R=I_3`, `M=M^T`, `s_min(M)>=1`,              (1.1)

and proves that every still-unpaid normalized-heavy state has an ORIGINAL-coordinate core `K`, `|K|<=126`, such that for

`T=sum_(i in K) r_i r_i^T`,                                    (1.2)

`lambda_1(T)>15/16`, `lambda_3(T)<1/64`.                       (1.3)

It also proves, from the pinned exact-rank-three leverage theorem, that every still-unpaid state contains an ORIGINAL physical row `h` with

`c_h:=||r_h||^2>1/2`.                                           (1.4)

Its finite-core theorem will also be used below: if an ORIGINAL core `K'`, `|K'|=m`, has

`sum_(i in K') r_i r_i^T >= kappa I_3`,                         (1.5)

then

`||p_Q||_infinity <= 2 sqrt(6 pi m)/kappa`.                    (1.6)

The fresh account03/B19 r28 result independently identifies normalized near-coloops as one of the two exact-rank-three rank-two-cross endpoints, so the compiler below is aimed at the current live obstruction rather than an obsolete branch.

## 2. A rank-one update lemma with an exact constant

### Lemma 2.1

Let `T>=0` on `R^3`, let `v` be a unit eigenvector for `lambda_3(T)`, and suppose

`lambda_2(T)>=a>0`.                                             (2.1)

If `r` obeys `||r||<=1` and

`|<r,v>|^2>=b`,                                                 (2.2)

then

`lambda_min(T+r r^T) >= ab/(1+a)`.                             (2.3)

#### Proof

Since the two eigenvalues on `v^perp` are at least `a`,

`T >= a(I-vv^T)`.                                               (2.4)

Write `r=s+t v`, `s perp v`. On the line in `v^perp` perpendicular to `s`, the matrix on the right of

`T+r r^T >= a(I-vv^T)+r r^T`                                  (2.5)

has eigenvalue `a`. On `span{s,v}` its determinant is `a t^2>=ab`, while its trace is

`a+||r||^2<=a+1`.                                               (2.6)

Hence its smaller eigenvalue is at least determinant divided by trace, namely `ab/(1+a)`. This is also at most `a`, so (2.3) follows on all of `R^3`. QED.

For `a=1/16`, `b=1/8`,

`ab/(1+a)=1/136`.                                               (2.7)

## 3. Main theorem — double-coloop to finite core or three original-coordinate packets

### Theorem 3.1 — `QFORM-DOUBLECOLOOP-THREEPACKET-COMPILER-v1`

Assume (1.1)-(1.4). Then at least one of the following holds.

**FINITE CORE PAYMENT.** There is an ORIGINAL-coordinate set `K'` with `|K'|<=127` such that

`sum_(i in K') r_i r_i^T >= (1/136) I_3`,                      (3.1)

and consequently

`boxed(||p_Q||_infinity <= 272 sqrt(762 pi) <13309).`           (3.2)

This branch proves an essentially bounded density; continuity is not claimed from the cited finite-core theorem.

**THREE-PACKET PRODUCT STRUCTURE.** The complete set of ORIGINAL coordinates admits a disjoint partition

`[n]=B_1 disjoint_union B_2 disjoint_union B_3`                 (3.3)

and there is an orthonormal spectral basis `(e_1,e_2,e_3)` such that

`boxed(sum_(i in B_k) <r_i,e_k>^2 >= c_*  for k=1,2,3),`        (3.4)

with the universal constant

`c_* = 453/4096 = 0.110595703125`.                              (3.5)

Because the `B_k` are original-coordinate packets, the three source banks are mutually independent before any deterministic spectral bookkeeping.

#### Proof

Diagonalize the deterministic Gram `T` from (1.2): choose orthonormal eigenvectors `(v_1,v_2,v_3)` with eigenvalues `lambda_1>=lambda_2>=lambda_3`. Equation (1.3) gives

`lambda_1>15/16`, `lambda_3<1/64`.                              (3.6)

Every row of a Parseval frame obeys `||r_i||^2<=1` because `RR^T` is an orthogonal projection.

### Case I: `h notin K`

The complement carries less than `1/16` mass in `v_1`, so

`|<r_h,v_1>|^2 <=1-lambda_1<1/16`.                             (3.7)

First suppose

`lambda_2>=1/16`, `|<r_h,v_3>|^2>=1/8`.                        (3.8)

Apply Lemma 2.1 with `a=1/16`, `b=1/8`. The augmented ORIGINAL core

`K'=K union {h}`                                                (3.9)

has size at most `127` and Gram at least `I/136`. Equation (1.6) therefore gives

`||p_Q||_infinity <= 2 sqrt(6 pi 127)*136
 =272 sqrt(762 pi)
 =13308.2615037...<13309`,                                      (3.10)

which is the finite-core branch.

Now retain `lambda_2>=1/16` but suppose instead

`|<r_h,v_3>|^2<1/8`.                                           (3.11)

Using (1.4), (3.7), and (3.11),

`|<r_h,v_2>|^2
 >1/2-1/16-1/8
 =5/16`.                                                        (3.12)

Take

`B_1=K`, `B_2={h}`, `B_3=K^c\{h}`,
`e_1=v_1`, `e_2=v_2`, `e_3=v_3`.                               (3.13)

Then the directional packet masses are respectively

`>15/16`, `>5/16`, `>1-1/64-1/8=55/64`,                       (3.14)

all larger than `c_*`.

It remains to treat `lambda_2<1/16`. Put `O=K^c`. Along `v_2,v_3`, the total masses in `O` are

`A=1-lambda_2>15/16`, `B=1-lambda_3>63/64`.                    (3.15)

For `i in O` define

`a_i=<r_i,v_2>^2`, `b_i=<r_i,v_3>^2`.                           (3.16)

Because `a_i+b_i<=||r_i||^2<=1`,

`a_i b_i <=(a_i+b_i)^2/4 <=(a_i+b_i)/4`.                       (3.17)

Hence

`sum_i a_i b_i <=(A+B)/4`.                                     (3.18)

Randomly split `O=U disjoint_union V` by independent fair coins. Then

`E[(sum_(i in U)a_i)(sum_(j in V)b_j)]
 = (AB-sum_i a_i b_i)/4
 >= (AB-(A+B)/4)/4
 >453/4096`.                                                     (3.19)

Thus one deterministic split satisfies product `>453/4096`. Each factor is at most one, so each factor itself is `>453/4096`. Taking

`B_1=K`, `B_2=U`, `B_3=V`,
`e_1=v_1`, `e_2=v_2`, `e_3=v_3`                                (3.20)

proves (3.4).

### Case II: `h in K`

Since `v_3` is the minimum-eigenvalue direction of the core,

`|<r_h,v_3>|^2 <=lambda_3<1/64`.                               (3.21)

Therefore the transverse vector

`q=Proj_(v_3^perp) r_h`                                         (3.22)

satisfies

`||q||^2>1/2-1/64=31/64`.                                      (3.23)

Put `e_1=q/||q||`, choose `e_2` as the unit vector in `v_3^perp` orthogonal to `e_1`, and put `e_3=v_3`. Then the singleton packet `{h}` carries `>31/64` mass in `e_1`, while `r_h` has exactly zero `e_2` component.

On `O=[n]\{h}`, the total `e_2` mass is therefore exactly `A=1`, while the total `e_3` mass is

`B=1-|<r_h,v_3>|^2>63/64`.                                     (3.24)

Applying the same random-split computation as (3.17)-(3.19) yields a split `O=U disjoint_union V` with both

`sum_(i in U)<r_i,e_2>^2 >125/1024`,
`sum_(i in V)<r_i,e_3>^2 >125/1024`.                            (3.25)

Indeed the product expectation is bounded below by

`[1*(63/64)-(1+63/64)/4]/4=125/1024`.                          (3.26)

Take `B_1={h}`, `B_2=U`, `B_3=V`. Since

`125/1024 =500/4096 >453/4096`,                                 (3.27)

(3.4) follows. This completes the proof. QED.

## 4. Why this is product-preserving and what it does not prove

The compiler never rotates the random source variables. The spectral vectors `e_k` are deterministic directions used only to measure how much of each Parseval frame direction is carried by each original-coordinate packet. Independence comes solely from the disjoint physical index sets `B_1,B_2,B_3`.

The packet lower bounds do **not** by themselves force a nonzero one-row-from-each third-volume. A target-valid frame counterexample to that shortcut is

`u=(e_1+e_2)/sqrt(2)`, `v=(e_1-e_2)/sqrt(2)`,

with packet rows

`B_1:{u/sqrt(2)}`, `B_2:{u/sqrt(2)}`, `B_3:{v,e_3}`.            (4.1)

Their outer products sum to `I_3`. Packet one carries `1/4` in `e_1`, packet two carries `1/4` in `e_2`, and packet three carries `1` in `e_3`, yet every triple taking one row from each packet has determinant zero because the first two packet ranges coincide. Thus a naive packet-mass-to-E3 implication is false; the next receiver must use range alignment/mixed-row information, not merely (3.4).

## 5. Designated account04/B20 result applied at an actual inequality

The completed account04/B20 theorem `QFORM-PARTITIONED-NEAR-NULL-HYBRID-v1`, scientific source

`yspennstate/math-open-problems@f97aa31585b7b547a116d4580f898576af4e0842`,

applies to an exact-rank-three Parseval frame containing a physical row

`r_h=sqrt(c_h)e`, `c_h>=1/2`,                                   (5.1)

provided every other physical row is **exactly** either longitudinal to `e` or transverse to `e`. If

`a=e^T M e`, `|a|<=1/2`,                                       (5.2)

then, because `|det M|>=1`, the partner theorem gives the actual endpoint inequality

`boxed(||p_Q||_infinity
 <=103680^(1/3) 2^(7/6)|det M|^(-1/3)
 <105.463).`                                                     (5.3)

Thus the partitioned near-null overlap of the double-coloop heavy-row branch is already paid. On the complementary large-Rayleigh side `|a|>1/2`, the same physical row has

`|A_hh|=c_h|a|>1/4`,                                            (5.4)

which routes to the existing physical scalar-pivot branch. I do not extend account04/B20's theorem to approximately partitioned rows.

Consequently every unpaid double-coloop state surviving Theorem 3.1 and the existing scalar-pivot branch must exhibit genuine longitudinal/transverse **mixed physical rows** relative to its leverage-`>1/2` row. This matches, rather than evades, the live account04/B20 scope boundary.

## 6. New first unpaid implication

The former `QFORM-RANK2CROSS-DOUBLECOLOOP-PAYMENT-v1` debt is reduced to

`QFORM-THREEPACKET-MIXED-RANGE-PAYMENT-v1`:

- an ORIGINAL-coordinate partition into three independent packets,
- three orthonormal spectral directions with packet directional masses at least `453/4096`,
- a physical row of leverage `>1/2`,
- failure of the exact longitudinal/transverse partition, hence a genuinely mixed residual physical row,
- and no permission to delete small transverse pieces or assume independence after spectral rotation.

A promising next mechanism is a quantitative Hall/mixed-discriminant dichotomy for the three packet Grams: large mixed discriminant feeds an existing third-volume receiver; small mixed discriminant must force two packet ranges close to a common line, where the remaining mixed-row obstruction can be attacked directly. The exact-zero mixed-discriminant endpoint is already a rank-Hall alignment statement, but a dimension-free quantitative stability estimate is still required.

The unrestricted QFORM conjecture remains OPEN / NOT PROVED / NOT DISPROVED. Global continuity remains OPEN. This run proves continuity only on the designated partner overlap (5.3), while the finite-core branch (3.2) is recorded only as an essential `L^infinity` density bound.
