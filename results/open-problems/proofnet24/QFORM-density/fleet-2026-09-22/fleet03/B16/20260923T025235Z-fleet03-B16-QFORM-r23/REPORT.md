SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B16, 2026-09-23T02:52:35Z.
attacking: the residual exact-rank-three near-null core by combining the partner disjoint-Pluecker parameter with a heavy/light mixed-minor generating identity, then forcing one source-valid dominant heavy star before nonlinear payment.

# fleet03/B16 r23 — mixed Pluecker star / transverse-escape compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Projection-product interaction  
**Status:** `NEW SUPPORTING STRUCTURAL THEOREM / ONE TRANSVERSE-HEAVY SUBBRANCH CLOSED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Repository transport was authenticated; native learned-memory receiver ingestion was not verified.  
**Continuity:** not proved by the new theorem or the new pair closure below.

## 1. Scope and source boundary

The full owner target remains OPEN: for every dimension, every independent real coordinate family with probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove one universal essential-density bound for `X^T A X`, or give a counterexample. Global continuity is separately OPEN.

This run works inside the exact-rank-three residual chamber isolated by fleet03/B16 r22, `QFORM-EXACT-R3-FINITE-HEAVY-CORE-v1`, canonical source

`yspennstate/math-open-problems@980f2e67036908408a0c33b8eb6bf1a7e2f233e6:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B16/20260923T022430Z-fleet03-B16-QFORM-r22/REPORT.md`.

Write

`A=R Lambda R^T`, `R^T R=I_3`, `min_s |lambda_s|>=1`,

and `r_i^T` for row `i` of `R`, `c_i=||r_i||^2`. Put

`H={i:c_i>1/64}`, `L=H^c`,
`G_H=sum_(i in H) r_i r_i^T`, `G_L=I-G_H`.

The residual chamber used below satisfies

`d<1/64`, `lambda_max(G_H)>1/2`, `det G_H<1/64`,                  (1.1)

and, because the r22 heavy-pivot exit has failed,

`|A_ii|<1/4096` for every `i in H`.                               (1.2)

Here `d` is the disjoint-Pluecker probability from the completed designated partner fleet04/B16 theorem `QFORM-RULED-PLUECKER-ENDPOINT-v1`, canonical source

`yspennstate/math-open-problems@b111363ff02b67015d14db35482e0150591744cd:proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B16/20260922T231542Z-fleet04-B16-QFORM-r1/REPORT.md`.

That theorem is used at an actual inequality below: its `d>=1/64` branch gives `||p_Q||_infinity<=24`, so the only branch considered here is the complementary `d<1/64` branch. Its majority-sign one-sheet inequality `pi sqrt(2)` also remains available after the structural reduction below.

Live corrections were retained: no arbitrary-joint 3D coarea theorem, no conditional-projection-height moment, no post-rotation independence, no receiver-only fiber supremum, and no law-uniform pointwise quadratic-phase decay is used.

## 2. Exact heavy/light Pluecker generating polynomial

For every physical triple `S`, put

`w_S=det(R_S)^2`.

Cauchy-Binet gives `sum_S w_S=1`. For `q=0,1,2,3`, let

`m_q=sum_{|S cap H|=q} w_S`.                                      (2.1)

### Lemma 2.1 — `QFORM-HEAVY-LIGHT-PLUECKER-POLYNOMIAL-v1`

For every `t>=0`,

`boxed: det(G_L+t G_H)=sum_(q=0)^3 m_q t^q.`                     (2.2)

Consequently

`m_0=det G_L`, `m_3=det G_H`,                                    (2.3)

and the total mixed Pluecker mass is

`boxed: m_1+m_2=1-det G_H-det G_L.`                              (2.4)

#### Proof

Scale every row of `R_H` by `sqrt(t)` and leave every row of `R_L` unchanged. The Gram matrix of the resulting `n x 3` matrix is `G_L+tG_H`. Cauchy-Binet expands its determinant as the sum of squared `3x3` row minors. A triple with exactly `q` heavy rows acquires squared scaling factor `t^q`, proving (2.2). Setting `t=0` and reading the cubic coefficient gives (2.3); setting `t=1` and using `G_H+G_L=I` gives (2.4). QED.

Because `lambda_max(G_H)>1/2`, one eigenvalue `h_1` of `G_H` exceeds `1/2`. Hence

`det G_L=prod_a (1-h_a)<1/2`.                                     (2.5)

Together with `det G_H<1/64`, (2.4) yields the uniform mixed-bank lower bound

`boxed: m_1+m_2>31/64.`                                          (2.6)

Therefore one of the two mixed classes has mass

`boxed: m:=max(m_1,m_2)>31/128.`                                 (2.7)

This is an aggregate-before-inversion statement; no individual reciprocal minor has been paid.

## 3. Small disjoint mass forces a dominant HEAVY star

The prescribed-row Cauchy-Binet identity is

`boxed: sum_(S contains i) w_S=c_i.`                              (3.1)

Indeed, after rotating spectral coordinates so `r_i=sqrt(c_i)e_1`, Cauchy-Binet on the two-dimensional orthogonal complement gives exactly (3.1). Equivalently it is the diagonal of the rank-three projection `RR^T` written in volume-sampling form.

Fix a mixed class `C` of mass `m>31/128` as in (2.7), and draw two independent Pluecker triples `S,T` conditioned on `S,T in C`. Since the unconditional disjoint probability is `d<1/64`,

`P(S cap T=empty | S,T in C)
 <= d/m^2
 < (1/64)/(31/128)^2
 =256/961.`                                                       (3.2)

Thus

`P(S cap T !=empty | S,T in C)>705/961.`                         (3.3)

### Case 1: `C=HLL`

Let

`p_i=P(i in S | S in C)`, `i in H`,
`q_l=P(l in S | S in C)`, `l in L`.

Then `sum_H p_i=1`, `sum_L q_l=2`. For every light coordinate, (3.1) and `c_l<=1/64` give

`m q_l<=c_l<=1/64`, hence `q_l<2/31`.                            (3.4)

By the union bound for the event that two triples share a coordinate,

`P(S cap T !=empty | C,C)
 <=sum_H p_i^2+sum_L q_l^2`.                                      (3.5)

Using (3.4),

`sum_L q_l^2 <=(max q_l) sum_L q_l <4/31=124/961`.               (3.6)

Therefore (3.3) implies

`sum_H p_i^2>581/961`.                                           (3.7)

Since `sum_H p_i=1`, some heavy coordinate satisfies `p_i>581/961`, and its absolute class packet obeys

`boxed: sum_(S in HLL, i in S) w_S
 =m p_i
 > (31/128)(581/961)
 =581/3968.`                                                      (3.8)

### Case 2: `C=HHL`

Now let `p_i`, `i in H`, be heavy-coordinate incidences and `q_l`, `l in L`, the single light-coordinate incidences. Then

`sum_H p_i=2`, `sum_L q_l=1`.

Again `m q_l<=c_l<=1/64`, so `q_l<2/31` and

`sum_L q_l^2<2/31=62/961`.                                       (3.9)

Equations (3.3),(3.5),(3.9) give

`sum_H p_i^2>643/961`.                                           (3.10)

Since `sum_H p_i=2`, some heavy coordinate satisfies

`p_i>643/1922`, and therefore

`boxed: sum_(S in HHL, i in S) w_S
 > (31/128)(643/1922)
 =643/7936.`                                                      (3.11)

Combining (3.8) and (3.11) proves the main structural theorem.

### Theorem 3.2 — `QFORM-MIXED-PLUECKER-DOMINANT-STAR-v1`

In residual chamber (1.1), there is an original heavy coordinate `i` and one of the two mixed classes `C in {HLL,HHL}` such that

`boxed: mu_i^C:=sum_(S in C, i in S) w_S > c_*:=643/7936.`       (3.12)

If the dominant class is `HLL`, the stronger lower bound `581/3968` holds.

For the actual principal-minor packet,

`sum_(S in C, i in S) |det A_S|
 =|det Lambda| mu_i^C
 >=mu_i^C>c_*`,                                                    (3.13)

because every exact-rank-three principal determinant has the common-sign form

`det A_S=det Lambda det(R_S)^2`.

This converts a diffuse residual Pluecker cloud into one fixed original-coordinate star without any dimension-dependent pigeonhole factor.

## 4. The dominant star is quantitatively near-null

By (3.1), `c_i>=mu_i^C>c_*`. Since `i in H`, the failed heavy-pivot exit (1.2) gives `|A_ii|<1/4096`. Put

`e=r_i/sqrt(c_i)`, `alpha=e^T Lambda e=A_ii/c_i`.

Then

`boxed: |alpha|<1/(4096 c_*)=31/10288<0.003014.`                  (4.1)

Write, in the spectral basis `e perp e^perp`,

`Lambda=[[alpha,beta^T],[beta,C]]`.

Since every singular value of `Lambda` is at least one,

`||Lambda e||^2=alpha^2+||beta||^2>=1`.

Hence

`boxed: ||beta||>sqrt(1-(31/10288)^2)>0.999995.`                  (4.2)

Thus the entire residual exact-rank-three debt can be anchored at a fixed original physical coordinate carrying at least `c_*=0.081023...` spectral leverage, at least `c_*` mixed determinant-bank mass, a normalized Rayleigh pivot below `0.003014`, and essentially unit cross coupling to the transverse spectral plane.

## 5. Transverse-heavy escape from the dominant star is already paid

For `j!=i`, set

`h_j=||(I-ee^T)r_j||^2`.

Suppose some `h_j>1/2`. Then `j` is itself heavy, so (1.2) gives `|A_jj|<1/4096`. The two-row spectral Gram determinant is

`G_ij=c_i h_j>c_*/2=:g_*`.                                       (5.1)

Let `H_ij` be the `2x2` row Gram matrix. Since `tr H_ij<=2`,

`lambda_min(H_ij)>g_*/2=c_*/4=:m_*`.                             (5.2)

Exactly as in fleet03/B16 r14 `QFORM-NESTED-HEAVY-PAIR-PIVOT-CLOSURE-v1`, orthonormalizing the two spectral rows and applying Cauchy interlacing to the compression of `Lambda` gives for the original physical pair block `B=A_{ {i,j},{i,j} }`

`||B||_op>m_*`.                                                   (5.3)

Put `delta=1/4096`. Writing `B=[[a,b],[b,d]]`, (1.2),(5.3) imply

`|b|>m_*-delta`,
`kappa:=sigma_min(B)>m_*-2delta=:k_*`,                            (5.4)

and `det B<0`; hence the pair is invertible indefinite. Numerically

`c_*=643/7936=0.08102318548...`,
`g_*=0.04051159274...`,
`m_*=0.02025579637...`,
`k_*=0.01976751512...`.                                          (5.5)

For exact rank three the fixed-pair determinant bank satisfies

`P_ij=sum_(k!=i,j)|det A_{ijk}|
 =|det Lambda| G_ij>g_*`.                                       (5.6)

The narrow pair-log/rank-one-remainder calculation re-derived in B16 r14 gives

`||p_Q||_infinity
 <=8 sqrt(5) (P_ij kappa)^(-1/4)`
` <8 sqrt(5)(g_* k_*)^(-1/4)`
` =106.3388941...<107.`                                          (5.7)

Therefore:

### Corollary 5.1 — `QFORM-DOMINANT-STAR-TRANSVERSE-HEAVY-ESCAPE-v1`

In residual chamber (1.1), after choosing the dominant heavy star of Theorem 3.2, either

`boxed: ||p_Q||_infinity<107`,                                   (5.8)

or every residual transverse row satisfies

`boxed: h_j<=1/2 for all j!=i.`                                  (5.9)

The second alternative is exactly the transverse-diffuse product-linear regime where the modulation-stable Wiener mechanism of fleet03/B06 is source-valid. No conditional-density substitute has been made here.

## 6. Equation-level use of the designated partner and what remains

The designated fleet04/B16 theorem is used twice, not bibliographically:

1. its actual inequality `d>=1/64 => ||p_Q||_infinity<=24` removes that branch before (3.2);
2. in the complementary indefinite residual chamber, its one-sheet estimate still gives

`ess sup_(majority-sign levels) p_Q <= pi sqrt(2)`               (6.1)

(with sign reversed for signature `(1,2)`).

Thus the remaining exact-rank-three debt after this run is narrower than r22 chamber E:

> **`QFORM-DOMINANT-NEAR-NULL-STAR-TRANSVERSE-DIFFUSE-v1`.** There is a fixed original coordinate `i` with `c_i>643/7936`, normalized Rayleigh coefficient `|alpha_i|<31/10288`, cross-plane coefficient `||beta_i||>0.999995`, and mixed principal-determinant packet `>643/7936`; all residual transverse leverages relative to `r_i` are at most `1/2`. Prove the minority-sign density bound by combining the modulation-stable product-projection/Wiener estimate with the nonlinear quadratic integration, without replacing the true product-linear leakage by a conditional cap.

At the exact `alpha_i=0` endpoint, fleet03/B06 already supplies a modulation-stable `|t|^-3/4` characteristic-function bound, an `L^2` density, and a uniform half-Riesz potential in precisely the transverse-diffuse product-linear state. The missing step is an `L^infinity` transducer stable through small nonzero `alpha_i`, not another receiver-only coarea bound.

Arbitrary additional spectral components remain a separate interface to the full owner target. Global continuity also remains open.

## 7. Status

New result `QFORM-MIXED-PLUECKER-DOMINANT-STAR-v1`: **PROVED as a supporting exact-rank-three structural theorem** from Cauchy-Binet, the partner disjointness parameter, and the r22 heavy/light compiler.

New result `QFORM-DOMINANT-STAR-TRANSVERSE-HEAVY-ESCAPE-v1`: **PROVED as a supporting density closure** using the source-valid B16 pair-log/rank-one remainder argument; the explicit bound is `<107`.

Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
Continuous density for the unrestricted target: **OPEN**.
