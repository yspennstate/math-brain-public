SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B10, 2026-09-23T03:43:10Z.
attacking: the exact-rank-three small-Pluecker-mass near-null hub/star collar; pay every genuinely transverse second-heavy row, then reduce the remaining arbitrary nonzero-hub geometry by product-preserving complement whitening and at most three original-coordinate deletions.

# account03/B10 r25 — near-null transverse-heavy payment + arbitrary-hub three-deletion collar

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** rank-three coupled case  
**Execution:** `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`  
**Classification:** `NEW SUPPORTING THEOREMS / SECOND-HEAVY O3 SUBBRANCH PAID / FULL TARGET OPEN`.

## 1. Exact target and correction boundary

The target remains unrestricted: independent real physical coordinates `X_i` with probability densities `0<=f_i<=1`, and a real symmetric matrix with at least three eigenvalues of modulus at least one. For the present assigned exact-rank-three work write

`A=R Lambda R^T`, `R^T R=I_3`, `sigma_min(Lambda)>=1`, `D:=|det Lambda|>=1`.

No spectral rotation is treated as preserving independence. No Gaussian, moment, compact-support, log-concavity, connected-support, pointwise Fresnel-decay, arbitrary-joint coarea, conditional projection-density supremum, or single-good-minor assumption is used. Continuity is recorded separately.

The current B10 predecessor actually used is

`yspennstate/math-open-problems@91759f77fcdf696a75d8e6c6ef398c03654b025a`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B10/20260923T023946Z-account03-B10-QFORM-r23b/REPORT.md`.

It proves that the exact-coloop endpoint is already source-matched and paid, `d>=1/64` is paid by a continuous `<24` Pluecker-cross-cut branch, and `d=0` is paid by `<331`. In the only collar `0<d<1/64`, either a scalar pivot already pays, or there is an ORIGINAL physical coordinate `i` with spectral row

`r_i=sqrt(c)e`, `c>1/4`, `||e||=1`,                                      (1.1)

such that

`|A_ii|<1/64`,
`|alpha|:=|e^T Lambda e|=|A_ii|/c<1/16`,                            (1.2)

and the aggregate original-coordinate star obeys

`||A_{i,-i}||_2>sqrt(1023)/64>0.499`.                              (1.3)

The branch is indefinite; the compatible account04/B16 ruled theorem already pays the majority-sign/one-sheet output side. The remaining debt is the minority/two-sheet side with the near-null hub retained exactly.

A newer account03/B19 theorem, source-read at the current master snapshot containing

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260923T030233Z-account03-B19-QFORM-r23/REPORT.md`,

applies (1.3) without deleting the nonzero hub diagonal and gives throughout this collar

`sup_z P(|Q-z|<=eps)<6.729 sqrt(eps)`,                              (1.4)

plus the corresponding quarter-Riesz bound `<5.188`. This is useful but is not yet an `L^infinity` density estimate; the purpose below is to add true linear smoothing on large subbranches.

## 2. New quantitative geometry: a near-null hub cannot have a transverse-heavy near-null partner

### Lemma 2.1 — `QFORM-NEARNULL-WITT-COMPRESSION-v1`

Let `Lambda` be real symmetric `3x3` with `sigma_min(Lambda)>=1`. Let `e` be unit and

`|e^T Lambda e|<1/16`.                                            (2.1)

Let `u` satisfy `||u||<=1` and

`h:=||(I-ee^T)u||^2>=1/4`.                                       (2.2)

Then at least one of

`|e^T Lambda u|>=1/32`,                                          (2.3)

`|u^T Lambda u|>=1/128`                                         (2.4)

holds.

#### Proof

Write

`u=x e+sqrt(h) v`, `v perpendicular e`, `||v||=1`.

Let

`alpha=e^T Lambda e`, `b=e^T Lambda u`, `q=u^T Lambda u`.

In the orthonormal basis `(e,v)` of the plane `E=span(e,u)`, the compression `C=P_E Lambda|_E` is

`C=[[alpha,delta],[delta,zeta]]`,                                 (2.5)

where the identities

`delta=(b-alpha x)/sqrt(h)`,
`zeta=(q-2xb+alpha x^2)/h`                                       (2.6)

follow by expanding the two bilinear forms.

Suppose both (2.3) and (2.4) fail. Since `sqrt(h)>=1/2` and `|x|<=1`,

`|delta|<2(1/32+1/16)=3/16`,                                    (2.7)

and

`|zeta|<4(1/128+2/32+1/16)=17/32`.                              (2.8)

Thus the maximum absolute row sum of `C` is less than

`max{1/16+3/16, 3/16+17/32}=23/32<1`,                            (2.9)

so `||C||op<1`.

But `E` is two dimensional and `E^perp` is one dimensional. The linear map

`P_{E^perp} Lambda|_E:E -> E^perp`

has a nonzero kernel. Choose a unit `z` in that kernel. Then `Lambda z` lies in `E`, hence

`||Lambda z||=||Cz||<1`,                                        (2.10)

contradicting `sigma_min(Lambda)>=1`. QED.

The point is that this argument uses only a two-dimensional compression and the codimension-one kernel; it needs no upper bound on `||Lambda||` and no exact null vector.

## 3. Target payment of every transverse-heavy second row

### Theorem 3.1 — `QFORM-NEARNULL-HUB-TRANSVERSEHEAVY-PAYMENT-v1`

Assume the B10 collar (1.1)-(1.2), and suppose some second physical row `r_j` obeys

`h_j:=||(I-ee^T)r_j||^2>=1/4`.                                  (3.1)

Then the full quadratic form has an essentially bounded density and

`boxed: ||p_Q||_infinity <609.`                                  (3.2)

#### Proof

Apply Lemma 2.1 with `u=r_j`.

### Diagonal alternative

If `|A_jj|>=1/128`, then row leverage `c_j=||r_j||^2>=h_j>=1/4`. The completed exact-rank-three scalar-pivot consequence of the affine half-Riesz theorem gives

`||p_Q||_infinity
 <=128[c_j |A_jj| D]^(-1/4)
 <=128[(1/4)(1/128)]^(-1/4)`
`=128*512^(1/4)
 <608.875.`                                                       (3.3)

### Cross alternative

Otherwise Lemma 2.1 gives `|e^T Lambda r_j|>=1/32`, so the actual physical off-diagonal coefficient is

`|A_ij|=sqrt(c)|e^T Lambda r_j|>1/64`.                            (3.4)

Together with `|A_ii|<1/64` and the present subcase `|A_jj|<1/128`, the physical pair

`B_ij=[[A_ii,A_ij],[A_ij,A_jj]]`

is uniformly indefinite, because

`A_ij^2>1/4096 > |A_ii A_jj|`.                                   (3.5)

Its smaller singular value satisfies

`kappa:=sigma_min(B_ij)
 >= |A_ij|-(|A_ii|+|A_jj|)/2
 >1/64-3/256
 =1/256.`                                                         (3.6)

Now apply the completed compatible **account04/B16** fixed-pair determinant-bank identity from

`yspennstate/math-open-problems@58c23c624db350cf44f0c836daa3582eb7e2d266`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B16/20260922T161909Z-account04-B16-QFORM-r2/REPORT.md`.

At this actual pair it gives

`P_ij:=sum_{k!=i,j}|det A_{ {i,j,k} }|
 =D G_ij`,                                                       (3.7)

where

`G_ij=||r_i||^2||r_j||^2-<r_i,r_j>^2=c h_j>=1/16`.               (3.8)

Hence

`P_ij>=1/16`.                                                     (3.9)

Feed the **total bank**, not an individual minor, into B10 r17's completed `QFORM-INDEFINITE-PAIR-SCHUR-BANK-v1`, source

`yspennstate/math-open-problems@11505bc9c70f8dfc4c587dbdb2ebaeee1dd0ca04`.

It yields

`||p_Q||_infinity
 <=8*2^(3/4)(kappa P_ij)^(-1/4)
 <8*2^(3/4)(1/4096)^(-1/4)`
`=64*2^(3/4)
 <107.635.`                                                       (3.10)

Combining (3.3) and (3.10) proves (3.2). QED.

This closes a genuine part of the newest exact-rank-three O3 obstruction: a second physical row cannot retain one quarter of a direction transverse to the near-null hub without producing a universal density bound. Therefore every still-unpaid B10 collar state may now assume

`boxed: ||(I-ee^T)r_j||^2<1/4 for every j!=i.`                    (3.11)

No continuity claim is made for Theorem 3.1 because the scalar-pivot and aggregate pair-Schur inputs used here were only invoked for essential boundedness.

## 4. New arbitrary-hub complement whitening

The next reduction does **not** use near-nullity. It is a source-preserving statement for every physical hub row in exact rank three.

### Theorem 4.1 — `QFORM-ARBITRARY-HUB-COMPLEMENT-DIFFUSE-v1`

Fix any physical row `r_i` with leverage

`c=||r_i||^2<1`,                                                 (4.1)

and let `C` denote the remaining original coordinates. Put

`G=I_3-r_i r_i^T`.                                               (4.2)

Then

`R_C^T R_C=G`, `det G=1-c`.                                     (4.3)

Define

`V=R_C G^(-1/2)`, `M=G^(1/2) Lambda G^(1/2)`.                   (4.4)

Then

`V^T V=I_3`,
`|det M|=(1-c)D`.                                                (4.5)

If every row `v_j` of `V` obeys `||v_j||^2<=1/2`, then the full `Q` has a bounded continuous density and

`boxed:
||p_Q||_infinity
 <=3e[(1-c)D]^(-1/3).`                                          (4.6)

#### Proof

Condition only on the original physical coordinate `X_i=x`. The remaining variables stay mutually independent with their original density caps. Since `R_C=V G^(1/2)`, the conditional form is exactly

`Q_x=X_C^T V M V^T X_C
      +sum_{j in C} ell_j(x) X_j
      +const(x)`,                                                (4.7)

where the `ell_j(x)` come from the hub-complement cross terms. They are coordinate-separable linear phases in the ORIGINAL independent complement variables.

Apply the established `QFORM-DIFFUSE-SEPARABLE-PHASE-v1` theorem at

`yspennstate/math-open-problems@773b7fb6f0e6a8142066f0bac08d228dfc164fdb`.

For rank three it gives uniformly in `x`

`||p_{Q_x}||_infinity<=3e |det M|^(-1/3)`.                       (4.8)

The same source provides a uniform integrable characteristic-function envelope, so averaging over `X_i` preserves both the bound and continuity. Equations (4.5) and (4.8) give (4.6). QED.

In particular,

`c<=7/8 => ||p_Q||_infinity<=6e<16.310`.                         (4.9)

This is the arbitrary-nonzero-hub extension of the older exact-null complement-whitening branch; the hub self coefficient is never deleted or treated as a small random perturbation.

## 5. New arbitrary-hub three-deletion collar

### Theorem 5.1 — `QFORM-ARBITRARY-HUB-THREE-DELETION-v1`

Use the whitened complement Parseval frame `V` from Section 4. Starting from retained Gram `H_0=I_3`, greedily do the following while `H` is positive definite:

- compute normalized retained leverage `ell_j=v_j^T H^(-1)v_j`;
- if every `ell_j<=1/2`, stop;
- otherwise delete one row with `ell_j>1/2`.

After each deletion check `q=det H`. Then after at most three deletions one of the following holds.

**(A) Product-diffuse stop.** The algorithm stops with

`q>=1/8`,                                                        (5.1)

all normalized retained leverages at most `1/2`, and, after conditioning on the hub and the deleted ORIGINAL coordinates,

`boxed:
||p_Q||_infinity
 <=3e[q(1-c)D]^(-1/3).`                                         (5.2)

If `c<=7/8`, then

`boxed: ||p_Q||_infinity<=12e<32.620`,                           (5.3)

and the density is continuous.

**(B) Finite localization.** A deleted set `D_0` with `1<=|D_0|<=3` satisfies

`det H<1/8`,                                                     (5.4)

and there is a unit vector `a in R^3` with

`boxed:
sum_{j in D_0}<v_j,a>^2>1/2.`                                  (5.5)

If in addition `c<=7/8`, there is a unit **physical spectral** direction `z` such that

`sum_{j in D_0}<r_j,z>^2>=(1-c)/2>=1/16`,                       (5.6)

and hence at least one of those at most three original rows has physical leverage

`||r_j||^2>1/48`.                                                (5.7)

#### Proof

For a deletion of row `v`, the matrix determinant lemma gives

`det(H-vv^T)=det(H)(1-v^T H^(-1)v)=q(1-ell)`.                    (5.8)

Every performed deletion has `ell>1/2`, hence multiplies positive `q` by a factor `<1/2`. Therefore if a deletion ever sends `q` below `1/8`, branch (B) occurs; otherwise three deletions cannot occur while retaining `q>=1/8`. Thus branch (A) is reached before the third deletion or branch (B) occurs by it.

In branch (A), let `V_R` be the retained rows and `H=V_R^T V_R`. Whiten again:

`W=V_R H^(-1/2)`, so `W^T W=I_3`.                               (5.9)

After conditioning on the hub and deleted ORIGINAL coordinates, all deleted cross terms become coordinate-separable linear terms in the retained independent variables. The retained quadratic spectral matrix is

`M_R=H^(1/2) M H^(1/2)`,                                       (5.10)

with

`|det M_R|=q(1-c)D`.                                            (5.11)

The diffuse separable-phase theorem yields (5.2), uniformly in every conditioned value. Equation (5.3) follows from `q>=1/8`, `1-c>=1/8`, `D>=1`. Its uniform integrable Fourier envelope gives continuity after mixing.

For branch (B), since the starting Gram is `I_3`,

`H=I_3-sum_{j in D_0}v_jv_j^T`, `0<=H<=I_3`.                    (5.12)

If every eigenvalue of `H` were at least `1/2`, then `det H>=1/8`. Hence (5.4) supplies a unit `a` with `a^T H a<1/2`, and (5.5) follows from (5.12).

For the physical statement define

`z=G^(-1/2)a / ||G^(-1/2)a||`.                                  (5.13)

Because `r_j=G^(1/2)v_j`,

`sum_{j in D_0}<r_j,z>^2
 = [sum_{j in D_0}<v_j,a>^2]/||G^(-1/2)a||^2`.                  (5.14)

The eigenvalues of `G` are `1,1,1-c`, so

`||G^(-1/2)a||^2<=1/(1-c)`.                                     (5.15)

Equations (5.5), (5.14), and (5.15) give the strict form of (5.6), and pigeonhole over at most three rows gives (5.7). QED.

## 6. Splice into the current B10 exact-rank-three collar

Starting from r23b's only unpaid `0<d<1/64` branch, combine Sections 3-5.

1. The actual physical hub has `c>1/4`, normalized Rayleigh quotient `<1/16`, and star norm `>0.499`.
2. If any second physical row has transverse leverage at least `1/4`, Theorem 3.1 pays the **full** density by `<609`.
3. Hence an unpaid state may assume the new strict transverse-diffuse condition (3.11).
4. If `c<=7/8`, apply Theorem 5.1. Either the full density is continuously bounded by `<12e`, or at most three ORIGINAL residual coordinates carry more than half of a whitened spectral direction; physically they carry at least `1/16` of one direction and one has leverage `>1/48`.
5. If `c>7/8`, the state is a quantitative near-coloop. The exact endpoint `c=1` is already paid by `<153`, but the leakage `1-c>0` with nonzero hub diagonal is not silently replaced by that endpoint.
6. Throughout the remaining branch, account03/B19's source-valid star theorem keeps the square-root small-ball/quarter-Riesz control (1.4).

Therefore the first unpaid exact-rank-three B10 implication is now the strictly smaller

`QFORM-NEARNULL-HUB-LONGITUDINAL-LOCALIZATION-v1`:

> In the small-Pluecker collar, assume `c>1/4`, normalized hub Rayleigh quotient `<1/16`, aggregate star norm `>sqrt(1023)/64`, and **every** second row has transverse leverage `<1/4`. Prove a universal minority-sign density bound in either (i) the near-coloop regime `c>7/8`, or (ii) `c<=7/8` with at most three original residual coordinates carrying more than half of one complement-whitened direction. Retain the nonzero hub square and all longitudinal/transverse overlap exactly.

This is narrower than r23b's generic near-null hub/star payment problem and narrower than the newest exact-rank-three O3 description: the genuinely transverse second-heavy-row case is now removed.

## 7. Fresh newest-source compatibility checks

### 7.1 Latest Claude one-hub record

During this run `math-open-problems` advanced to

`469544eaf917159c10c7b04f661c6e411feb392b`,

adding `single_hub_core/REPORT.md`. Its Theorem 1 proves an interval-hub bound for forms

`2 X_h(L+beta)+lambda V^2+2L<q,X'>+separable`

when the `(L,V)` frame is diffuse. I do **not** use this as the arbitrary-support target theorem: its interval-support hypothesis is an extra condition, and its own later sections explicitly retain an arbitrary-hub slice/maximal-function debt. Its structural message is consistent with (and useful for) the successor above: freeze the genuine product linear form before paying the mixed cross terms, rather than splitting the hub law at a worst conditional density.

### 7.2 New collective-tail package

The required `c2414ef633b9d4b7f04a83e1aeefbe713ed82bba` tail extension was read. Its strongest new gate uses two large singular directions plus a **collective tail** `T2` and requires

`||(I-P)M||op <= sqrt(T2)/15`.                                  (7.1)

For an intrinsically rank-three cross block and `P` the top-two left singular projection, `T2=s_3(M)^2` and the left side is `s_3(M)`, so (7.1) would read `s_3<=s_3/15` and cannot fire when `s_3>0`. Thus that specific collective-tail extension is not falsely claimed to close the exact-rank-three hub collar; it is genuinely aimed at many-direction tails. The baseline volume-stability result remains a valid separate diffuse-cut exit when its stated `s_3` and leverage hypotheses happen to hold.

## 8. Partner status

The exact designated `account04/B10` still had no completed current-QFORM canonical archive at the fresh lookup, so no result is fabricated or awaited. The completed compatible account04/B16 result was applied at the explicit equation (3.7)-(3.9), where it converts the transverse-heavy physical pair into the total determinant bank `P_ij>=1/16`. The proof then spends that **aggregate** bank via B10 r17 rather than selecting a tiny third-coordinate atom.

## 9. Regression check

`VERIFY.py` and `VERIFY_OUTPUT.txt` accompany this report. The deterministic stress run sampled 300000 random indefinite symmetric `3x3` matrices with eigenvalue moduli at least one and random admissible `(e,u)` pairs. It found 1671 fixtures satisfying `|e^T Lambda e|<1/16` and transverse leverage at least `1/4`, with zero violations of Lemma 2.1. The minimum observed normalized threshold ratio was `7.9051`. This is only a regression check; the proof is the exact compression/kernel argument in Section 2.

The numerical branch constants recorded by the checker are

`128*512^(1/4)=608.8740428813932`,
`64*2^(3/4)=107.63474115247546`,
`6e=16.30969097075427`,
`12e=32.61938194150854`.

## 10. Status

- `QFORM-NEARNULL-WITT-COMPRESSION-v1`: **PROVED in this report**.
- `QFORM-NEARNULL-HUB-TRANSVERSEHEAVY-PAYMENT-v1`: **PROVED**, essential boundedness `<609`; continuity not newly claimed.
- `QFORM-ARBITRARY-HUB-COMPLEMENT-DIFFUSE-v1`: **PROVED**, continuous density at the stated determinant scale.
- `QFORM-ARBITRARY-HUB-THREE-DELETION-v1`: **PROVED**, with a continuous `<12e` branch for `c<=7/8` or a three-coordinate localization certificate.
- Exact rank-three QFORM: **OPEN / NOT PROVED**.
- Full arbitrary-dimension QFORM: **OPEN / NOT PROVED**.
- Global continuity: **OPEN separately**.
- Native learned-memory ingestion: **not verified**; execution remains `WITHOUT_VERIFIED_BRAIN`.
