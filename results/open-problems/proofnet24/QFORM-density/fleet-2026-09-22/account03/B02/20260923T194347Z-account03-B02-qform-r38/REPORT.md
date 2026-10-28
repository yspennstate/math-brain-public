SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B02, 2026-09-23T19:43:47Z.
attacking: the V1 overlap-one compound stratum: compile a zero/small shared diagonal pivot into an exact two-sided shared-hub transverse packet, then pay the non-rank-one transverse branch by marginal-free one-hub projected-E2 Fourier smoothing.

# account03/B02 r38 — overlap-one zero-pivot shared-hub compiler and integrated-Fourier exit

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Integrated Fourier estimate  
**Status:** `NEW SUPPORTING THEOREM / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval is not native learned-memory ingestion.  
**Continuity:** proved on the new Fourier branch below; full-target continuity remains OPEN.  
**Target-wide unweighted Fourier-L1 criterion:** OPEN / not refuted.

The exact owner target is unchanged: independent ORIGINAL real coordinates with one-dimensional densities bounded by one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No Gaussianity, moments, compact support, connected support, log-concavity, post-rotation independence, or diagonal-basis independence is inserted.

## 1. Fresh source state and inputs actually used


The immediate B02 predecessor is

`QFORM-COMPOUND-STRATUM-V0-FOURIER-L1-v1`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T190108Z-account03-B02-qform-r37/REPORT.md`.

It writes the complete third compound as

`e3(A^2)=V0+V1+V2+V3 >=1`,

where `Vr` is squared third-minor mass with row/column support intersection size `r`, and pays the `V0` branch by a genuine unweighted Fourier-L1 estimate. Thus an overlap stratum must be attacked next.

The overlap-one pivot compiler actually used below is account03/B04

`QFORM-OVERLAP1-PIVOT-PAIRVOLUME-v1`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/20260923T085949Z-account03-B04-qform-auto11-r30/REPORT.md`.

For a shared physical coordinate `i`, it defines

`Delta_i=sum det A[{i} union P,{i} union Q]^2`,

summed over disjoint residual two-sets `P,Q`, proves `V1=sum_i Delta_i`, and, for `a_i=A_ii !=0`, obtains the essential-density bound

`||p_Q||_infinity <=37.241966 (|a_i|^2 Delta_i)^(-1/8)`.

That theorem deliberately does not claim continuity from its square-peel interface. The present run attacks the complementary zero/small-pivot geometry rather than repeating the nonzero-pivot proof.

The main analytic input is the fresh marginal-free one-hub projected-two-volume theorem, independently written in account03/B01 and account02/B03. I use the account03/B01 source

`QFORM-ONEHUB-E2-MARGINAL-GATE-REMOVAL-v1`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260923T173320Z-auto11-heavyrowpromotion/REPORT.md`.

If one ORIGINAL hub `Y` couples to a light-bank vector `m` and, after projecting a light cross block away from `m`, its complete physical second volume is `Z2>0`, then with

`R_hub=||m||^2 Z2`

one has a continuous `C0` density and

`||p_Q||_infinity <= C_h R_hub^(-1/6)`,

`C_h=3*2^(7/6)*exp(1/3)=9.39913188784886...`.                    (1.1)

Retracing its three promotion cases gives the single safe high-frequency envelope

`|phi_Q(t)| <= min{1,K_h R_hub^(-1/4)|t|^(-3/2)}`,               (1.2)

with

`K_h=2^(7/4) pi^(3/2) exp(1/2)=30.87980451778735...`.            (1.3)

Indeed (1.3) is the exact first-case constant; the promoted `(k,ell)=(2,1)` and exact-rank-three terminal branches have smaller coefficients after their exterior identities are substituted. Therefore

`integral_R |phi_Q(t)|dt <=2 pi C_h R_hub^(-1/6)`.                (1.4)

The designated partner is account04/B02

`QFORM-ZERO-DIAGONAL-TRIPLE-CONTINUITY-v1`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B02/20260922T193108Z-account04-B02-QFORM-r2/REPORT.md`.

Whenever a nonsingular physical zero-diagonal principal triple `H0` exists, it supplies

`integral_R |phi_Q(t)|^2dt <=L0 |det H0|^(-1/3)`,
`L0=6 pi 2^(2/3)=29.92180489898403...`.                           (1.5)

Section 6 applies (1.5) at an actual new inequality.

## 2. One overlap-one slice and a random oriented cut

Fix a physical coordinate `i`. Put `K=[n]\{i}` and

`a=A_ii`, `v=A[K,i]`.

For disjoint residual two-sets `P,Q subset K`, define

`d_(P,Q)=det A[{i} union P,{i} union Q]`.                          (2.1)

The overlap-one slice is

`Delta_i=sum_(P cap Q=empty) d_(P,Q)^2`.                           (2.2)

Now independently color every coordinate of `K` left or right with probability `1/2`, obtaining `K=L disjoint_union R`. Write the corresponding physical coefficients as

`c=A[L,i]`, `r=A[i,R]`, `N=A[L,R]`.                               (2.3)

Define the oriented overlap mass

`D_i(L,R)
 =sum_(P subset L,Q subset R, |P|=|Q|=2)
   det [[a,r_Q^T],[c_P,N[P,Q]]]^2`.                                (2.4)

A fixed ordered disjoint pair `(P,Q)` survives precisely when `P subset L` and `Q subset R`, probability `2^-4=1/16`. Hence

`E_(L|R) D_i(L,R)=Delta_i/16`.                                    (2.5)

Therefore some actual ORIGINAL-coordinate cut satisfies

`boxed: D_i(L,R)>=Delta_i/16.`                                    (2.6)

No coordinate is duplicated as a random input: the shared coordinate `i` stays a single physical hub. The left/right split is only among the residual original coordinates.

## 3. Exact shared-hub transverse identity

For the cut (2.3), let

`P_c=I-cc^T/||c||^2`, `P_r=I-rr^T/||r||^2`                       (3.1)

when `c,r` are nonzero, and define the transverse physical crossing

`C=P_c N P_r`.                                                     (3.2)

Put

`u=||c||^2`, `w=||r||^2`, `F2=||C||_F^2`,
`T=u w F2`.                                                        (3.3)

### Lemma 3.1 — `QFORM-V1-SHAREDHUB-TRANSVERSE-IDENTITY-v1`

For `a=0`, the entire oriented overlap-one mass is exactly

`boxed: D_i(L,R)=T
 =||c||^2||r||^2||P_c N P_r||_F^2.`                              (3.4)

For arbitrary `a`,

`boxed:
 sqrt(D_i(L,R))
 <= |a| sqrt(E2(N)) + sqrt(T),
}`                                                                  (3.5)

where `E2(N)=e2(N^T N)`. Consequently

`boxed:
 max{a^2 E2(N),T} >= D_i(L,R)/4.
}`                                                                  (3.6)

Combining with (2.6), for a maximizing cut

`max{a^2E2(N),T}>=Delta_i/64`,                                     (3.7)

while at the exact zero-pivot endpoint `a=0` the stronger statement is

`boxed: T=D_i(L,R)>=Delta_i/16.`                                  (3.8)

### Proof

For each residual pair `P={p1,p2}`, `Q={q1,q2}`, Laplace expansion along the shared hub gives

`d_(P,Q)=a det N[P,Q]-z_(P,Q)`,                                   (3.9)

where

`z_(P,Q)=r_Q^T adj(N[P,Q]) c_P`.                                  (3.10)

View the two arrays `(det N[P,Q])_(P,Q)` and `(z_(P,Q))_(P,Q)` in their common Euclidean coefficient space. The first has squared norm `E2(N)`. Minkowski therefore yields (3.5) once the squared norm of the second array is identified with `T`.

For that identification, define exterior maps `L_c:x -> c wedge x` and `L_r:y -> r wedge y`. The coefficient array `(z_(P,Q))` is, up to harmless signs from pair ordering, the matrix of

`L_c N L_r^*`.                                                     (3.11)

The standard exterior identities are

`L_c^*L_c=||c||^2 P_c`,
`L_r^*L_r=||r||^2 P_r`.                                           (3.12)

Hence cyclicity of trace gives

`sum_(P,Q) z_(P,Q)^2
 =||L_c N L_r^*||_HS^2`
` =||c||^2||r||^2 Tr(P_r N^T P_c N P_r)`
` =||c||^2||r||^2||P_cNP_r||_F^2=T`.                              (3.13)

When `a=0`, (3.9) immediately gives (3.4). If both terms in (3.6) were `<D_i/4`, the right side of (3.5) would be `<sqrt(D_i)`, impossible. QED.

This identity is algebraically the same exterior operation that appears for two *distinct* zero-edge anchors, but here it is used only as coefficient algebra. The shared physical coordinate is never copied into two independent banks, so no false independence is introduced.

## 4. Convert the exact zero-pivot packet to a one-hub E2 resource

Assume from now on `a=0` and use a cut satisfying (2.6), so `T=D_i(L,R)>0`. In particular `c,r,C` are nonzero.

Let the squared singular values of `C` be `s_1^2>=s_2^2>=...`, and define its stable rank

`rho=||C||_F^2/s_1^2 >1`                                         (4.1)

on the non-rank-one branch. Set

`gamma(rho)=(rho-1)/(2rho)`.                                      (4.2)

Then

`E2(C)
 =1/2[(sum s_j^2)^2-sum s_j^4]
 >=1/2[F2^2-s_1^2 F2]
 =gamma(rho) F2^2.`                                               (4.3)

There are two legitimate one-hub orientations.

* Use the same physical hub `X_i`, put the `R` bank on the hub-coupling side, and take `m=r`. The projected crossing is `N P_r`; define

  `Z_R=E2(NP_r)` and `R_R=w Z_R`.                                 (4.4)

* Transpose the light banks, put `m=c`, and define

  `Z_L=E2(P_cN)` and `R_L=u Z_L`.                                 (4.5)

Since left or right multiplication by an orthogonal projection cannot increase any singular value, applying the additional projection that produces `C=P_cNP_r` can only decrease the complete second singular-value symmetric function. Thus

`Z_R>=E2(C)`, `Z_L>=E2(C)`.                                      (4.6)

Let

`R_* =max{R_L,R_R}`.                                               (4.7)

Using (4.3)-(4.6),

`R_* >=max(u,w) gamma(rho) F2^2`.                                 (4.8)

Introduce the dimensionless two-star dominance ratio

`b=min(u,w)/F2`.                                                   (4.9)

Because `T=uwF2`, (4.8) is exactly

`boxed: R_* >= [gamma(rho)/b] T.`                                 (4.10)

This is the first essential implication of the run. It converts the shared-overlap determinant mass into a genuine **disjoint-light-bank projected E2** resource for the same one physical hub, except for two transparent degeneracies: `rho downarrow 1` (transverse crossing becomes rank one) or `b -> infinity` (both star arms dominate the transverse scale).

Combining (3.8) and (4.10),

`boxed:
 R_* >= [gamma(rho)/(16 b)] Delta_i.
}`                                                                  (4.11)

## 5. Main integrated-Fourier theorem for the zero-pivot V1 slice

### Theorem 5.1 — `QFORM-V1-ZEROPIVOT-SHAREDHUB-E2-L1-v1`

Assume `A_ii=0`, `Delta_i>0`, and for the cut supplied by (2.6) the transverse matrix `C=P_cNP_r` has stable rank `rho>1`. Let `b` be (4.9). Then the full ambient quadratic form, with arbitrary same-bank curvature, outside couplings and affine terms, has a continuous `C0` density satisfying

`boxed:
 ||p_Q||_infinity
 <= C_h [16 b/gamma(rho)]^(1/6) Delta_i^(-1/6),
}`                                                                  (5.1)

and a genuine unweighted integrated-Fourier bound

`boxed:
 integral_R |phi_Q(t)|dt
 <=2 pi C_h [16 b/gamma(rho)]^(1/6) Delta_i^(-1/6).
}`                                                                  (5.2)

Moreover the characteristic function obeys the safe high-frequency envelope

`boxed:
 |phi_Q(t)|
 <=min{1,K_h [16 b/gamma(rho)]^(1/4)
                Delta_i^(-1/4)|t|^(-3/2)}.
}`                                                                  (5.3)

### Proof

Choose the orientation achieving `R_*` in (4.7). It is a literal one-original-hub plus projected-E2 packet, so the marginal-free source theorem (1.1)-(1.4) applies with `R_hub=R_*`; arbitrary curvature on every retained bank is permitted. Substitute (4.11). This proves (5.1)-(5.3). QED.

A useful fixed-geometry corollary is obtained from

`rho>=2  => gamma(rho)>=1/4`,
`b<=1`.                                                            (5.4)

Then

`R_*>=Delta_i/64` and therefore

`boxed:
 ||p_Q||_infinity <=2 C_h Delta_i^(-1/6)
 =18.79826377569772... Delta_i^(-1/6),
}`                                                                  (5.5)

`boxed:
 integral_R |phi_Q(t)|dt
 <=4 pi C_h Delta_i^(-1/6)
 =118.11297475595016... Delta_i^(-1/6).
}`                                                                  (5.6)

Thus an exact zero diagonal shared coordinate is **not** by itself an overlap-one obstruction. The only zero-pivot slice left by this theorem is quantitatively either near rank one after both star directions are projected out (`rho` near one), or two-star dominated (`b` large), or the overlap mass is globally spread over many shared coordinates so that no single `Delta_i` is target-scale.

## 6. Designated account04/B02 result applied at an actual new inequality

Assume, on the same zero-pivot branch, that the full physical matrix contains a nonsingular zero-diagonal principal triple `H0`. The designated account04/B02 theorem gives (1.5).

Use the one-hub envelope before substituting (4.11):

`|phi_Q(t)|<=min{1,A |t|^(-3/2)}`,
`A=K_h R_*^(-1/4)`.                                                (6.1)

For every `T0>0`, Cauchy-Schwarz on `[-T0,T0]` and direct integration of the tail give

`||phi_Q||_1
 <=sqrt(2 L T0)+4A T0^(-1/2)`,                                   (6.2)

where `L=L0 |det H0|^(-1/3)`. The optimizer is

`T0=4A/sqrt(2L)`,                                                  (6.3)

and therefore

`||phi_Q||_1 <=4 A^(1/2)(2L)^(1/4)`.                              (6.4)

Fourier inversion yields the new hybrid inequality

`boxed:
 ||p_Q||_infinity
 <=C_hyb |det H0|^(-1/12) R_*^(-1/8),
}`                                                                  (6.5)

with

`C_hyb=2^(61/24) 3^(1/4) exp(1/4)
     =9.83947303316740...`.                                        (6.6)

Substitute (4.11):

`boxed:
 ||p_Q||_infinity
 <=C_hyb [16 b/gamma(rho)]^(1/8)
   |det H0|^(-1/12) Delta_i^(-1/8).
}`                                                                  (6.7)

At the clean `rho>=2`, `b<=1` threshold,

`boxed:
 ||p_Q||_infinity
 <=16.54795520315212...
   |det H0|^(-1/12) Delta_i^(-1/8).
}`                                                                  (6.8)

This is an equation-level use of the designated partner theorem. It is not needed for continuity (Theorem 5.1 already gives `phi in L1`), but it improves the overlap-slice exponent when the independent zero-diagonal-triple `L2_t` credit is also present.

## 7. Relation to the global V1 stratum and what remains

Recall from r37 and account03/B04 that

`V1=sum_i Delta_i`.                                                (7.1)

If the global compound alternative has `V1>=1/4` and there is a zero-diagonal shared coordinate `i` carrying a fraction `eta` of the V1 mass,

`Delta_i>=eta V1`,                                                 (7.2)

with a maximizing cut satisfying `rho>=2` and `b<=1`, then Theorem 5.1 gives

`||p_Q||_infinity
 <=2C_h (eta V1)^(-1/6)
 <=2C_h (eta/4)^(-1/6)`.                                          (7.3)

So the overlap-one programme has moved past the mere statement "the shared pivot may be zero." The remaining V1 debt is now explicitly one of:

1. **spread shared-coordinate mass:** every `Delta_i/V1` is small;
2. **nonzero-pivot spread:** the mass is carried by many nonzero physical diagonals, where the existing square-peel theorem is individually valid but an aggregate integrated-Fourier compiler is still missing;
3. **rank-one transverse collar:** for the zero-pivot heavy slices, `sr(P_cNP_r)` is close to one;
4. **two-star-dominated collar:** `min(||c||^2,||r||^2)` is large compared with `||P_cNP_r||_F^2`.

The stress family in the fleet shows that such low-rank common-hub geometry is real and cannot simply be discarded as a small perturbation; separate grouped/rank-two receivers are the appropriate next mechanism.

The full conjecture is **not** proved by this reduction. `V2` and `V3` are also still separate global strata unless paid by other current workers.

## 8. Correction audit

This run does **not** use any of the currently forbidden interfaces:

- no law-uniform scalar van-der-Corput or Fresnel pointwise decay;
- no arbitrary-joint coarea estimate;
- no positive moment of conditional projection heights;
- no independence after rotating random coordinates;
- no deletion of a small coefficient tail on unbounded inputs;
- no promotion of a cross-only Schur packet to a true symmetric Schur packet;
- no fiber-sup integration with dimension loss;
- no single tiny physical minor is inverted.

The only orthogonal projections in Sections 3-5 are deterministic coefficient projections used to state singular values/exterior volumes. The analytic one-hub theorem itself promotes only literal original independent coordinates.

## 9. Deterministic regression and arithmetic audit

A seeded finite checker (`seed=20260923`) tested 1,000 random rectangular packets with sizes between `2x2` and `6x6`. It verified:

- the exact zero-pivot identity (3.4), maximum relative discrepancy `1.50e-15`;
- the general Minkowski inequality (3.5), no violation beyond `1.55e-14` floating-point tolerance;
- the resource lower bound (4.10), no violation beyond `1.07e-14` floating-point tolerance;
- the minimum observed ratio `R_*/[(gamma/b)T]` was `1.2127`.

A second exact-cut enumeration on 30 random symmetric `7x7` matrices averaged all `2^6` residual colorings and verified (2.5) with maximum relative discrepancy `8.19e-16`.

These computations are diagnostics only. The proof is the exterior-algebra/Cauchy-Binet argument above.

Constants independently recomputed:

`C_h=9.39913188784886`,
`2 C_h=18.79826377569772`,
`4 pi C_h=118.11297475595016`,
`K_h=30.87980451778735`,
`L0=29.92180489898403`,
`C_hyb=9.83947303316740`,
`64^(1/8) C_hyb=16.54795520315212`.

## 10. Publication state and next exact B02 obligation

The full universal QFORM target remains **OPEN**. Full-target continuity remains OPEN. A target-wide uniform bound on the unweighted integral `integral |phi_Q|` remains **OPEN / not refuted**.

This run proves a genuine unweighted Fourier-L1 estimate on a previously unpaid piece of the overlap-one stratum: exact zero shared pivot + quantitative non-rank-one transverse crossing, with arbitrary same-bank curvature retained.

The next B02 mechanism is

`QFORM-V1-ZEROPIVOT-RANK1-OR-TWOSTAR-DOMINATED-L1-v1`:

start from the exact identity `Delta-cut=||c||^2||r||^2||P_cNP_r||_F^2` and pay either `sr(P_cNP_r)<2` or `min(||c||^2,||r||^2)>||P_cNP_r||_F^2` by a rank-one-compatible common-hub/grouped-bank receiver. Do not duplicate the shared hub into independent banks and do not delete the transverse tail.

MODEL self-report: GPT-5.6 Sol. Configured model/thinking fields are not exposed in the fresh account03 inventory; `reasoning_effort_configured=UNKNOWN_NOT_EXPOSED`, requested maximum actually supported. Provider reasoning-token and pure-thinking-time telemetry are not exposed.