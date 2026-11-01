SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B08, 2026-09-23T13:18:15Z.
attacking: aligned-or-localized multihub leakage receiver — remove the diagonal-light restriction with exact-rank-two grouped Fourier/E2 smoothing and route scalar-Schur cancellation into a physical localized triangle.

# fleet03/B08 r38 — leakage-stable anisotropic-core receiver and scalar-Schur cancellation router

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T131815Z-fleet03-B08-qform-diffuse-r38`  
Owner control: revision `2026-09-22.15`  
Assignment: diffuse eigenvector case / quantitative inequalities and rigorous computations  
Status: `NEW SUPPORTING TARGET-LEVEL ROUTER / FULL TARGET OPEN / INDEPENDENT REVIEW PENDING`  
Execution: `WITHOUT_VERIFIED_BRAIN`

The unrestricted conjecture remains OPEN. Global continuity remains OPEN. All arguments below stay in ORIGINAL independent coordinates and assume only one-dimensional density caps `0<=f_i<=1`. No Gaussianity, moments, compact support, connected support, log-concavity, iid assumption, post-rotation independence, arbitrary-joint coarea lemma, law-uniform pointwise quadratic-phase decay, fiber-supremum estimate, or unproved pre/post-Schur determinant transfer is used.

The new contribution is narrow but directly addresses the r37 debt. The two-hub low-rank branch does **not** need the r37 diagonal-light hypothesis for higher-integrability: the already-completed exact-rank-two grouped Fourier theorem retains arbitrary same-bank quadratic curvature. Combined with the aggregate `E_2` theorem, this yields a leakage-stable receiver for an anisotropic physical `2x2` core even when arbitrary extra cross/tail entries are present. When an outer scalar Schur completion threatens to cancel that core, an exact determinant identity routes failure into a physical localized three-link packet rather than silently assuming `E_2` survives.

## 1. Source-valid inputs actually used at equations

### 1.1 Immediate B08 predecessor

`yspennstate/math-open-problems@58b2a0752f409dd48ae5e39851ac84f13be4470b`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260923T122051Z-fleet03-B08-qform-diffuse-r37/REPORT.md`.

It proves `QFORM-MULTIHUB-TRANSVERSE-FRESNEL-v1`: for physical hubs `H`, light block `D+S Lambda S^T`, transverse coupling `C_perp=(I-SS^T)C`, and augmented row leverage at most `1/2`, the full conditional form has a continuous `C_0` density with an explicit determinant bound. Its two-hub/no-child corollary is

`||p_Q||_infinity <=4 det(C^T C)^(-1/4)`

when the light-light block is diagonal and the normalized row leverage is at most `1/2`. The explicit r37 debt was arbitrary non-diagonal same-bank light curvature in the aligned/high-leverage low-rank survivor.

### 1.2 Exact rank-two cross-bank theorem with arbitrary self curvature

`yspennstate/math-open-problems@1287456c9a709f8c3f117c23faa46e75f4560d01`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260922T194649Z-fleet03-B06-qform-r17/REPORT.md`.

For disjoint ORIGINAL banks `I,J`, after conditioning outside coordinates,

`Q(U,V)=F(U)+2U^T C V+G(V)+c`,

where `F,G` are arbitrary quadratic-affine functions and `rank(C)=2`, the source proves an `L^3` density. If one active bank consists of exactly two physical coordinates and `Pi_2(C)=sigma_1(C)sigma_2(C)`, then

`||p_Q||_3 <= 3^(2/3)e^(1/3) Pi_2(C)^(-1/3)`.                 (1.1)

The arbitrary self blocks are retained inside complex conditional amplitudes; they are not discarded.

If in addition a genuine ORIGINAL scalar square completion with coefficient `a!=0` is present, its dependence-safe square transducer gives

`||p_Q||_infinity
 < 7.829 |a|^(-1/2) Pi_2(C)^(-1/4)`.                           (1.2)

Continuity is not asserted by this route.

### 1.3 Grouped double-incident rank-two theorem

`yspennstate/math-open-problems@c248abc9be918698c6d5a68108c615ba1c4790b3`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/B08-20260922T204103Z-1dd824/REPORT.md`.

For an exact-rank-two physical cross block `C`, fixed physical row `j` and column `r`, and

`Delta_jr(C)=sum_(k!=j,s!=r) det C[{j,k},{r,s}]^2`,

it proves, retaining arbitrary same-side quadratic-affine terms,

`||p_R||_3 <= 3^(2/3)2^(1/3) Delta_jr(C)^(-1/6)`.              (1.3)

With a genuine outer square `a!=0`,

`||p_Q||_infinity <= C_grp |a|^(-1/2) Delta_jr(C)^(-1/8)`,     (1.4)

where

`C_grp=(2^(4/3)+1)sqrt(3)2^(1/4)
      =7.250055108887958...`.                                  (1.5)

This is important here because it shows that the designated partner's anisotropic endpoint can retain arbitrary same-bank curvature without paying a single reciprocal minor.

### 1.4 Arbitrary-rank aggregate E2 theorem

`yspennstate/math-open-problems@2cb64b71f8aafa0892547dffebcf6af647ea7c64`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260923T102108Z-fleet03-B08-qform-diffuse-r32/REPORT.md`.

For any literal ORIGINAL-coordinate cross block `M` of an otherwise arbitrary quadratic-affine form, with

`E_2(M)=sum_(|R|=|T|=2) det(M[R,T])^2>0`,

the full output has

`||p_Q||_(9/4) <7 E_2(M)^(-5/36)`.                             (1.6)

After a genuine scalar Schur completion with coefficient `a!=0`, if the **post-Schur** residual contains such a block, then

`||p_Q||_infinity
 < C_E2 |a|^(-1/2) E_2(M)^(-1/8)`,                            (1.7)

with

`C_E2=2sqrt(10)7^(9/10)=36.44334493792993...`.                 (1.8)

All same-bank curvature, extra residual cross couplings, and extra spectrum are retained. The source explicitly does not claim that pre-Schur `E_2` survives a rank-one Schur update.

### 1.5 Newest required volume result

The current newest volume package is

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,

`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/`.

The part applied below is its perturbative diffuse exit: if an actual physical cross block has a rank-three reference `M0` with `s3(M0)>=a`, range leverage at most `1/2`, and operator error at most `a/16`, then the full ambient output has a continuous density `<23/a`, with arbitrary self blocks and outside couplings retained.

### 1.6 Designated partner fleet04/B08

`yspennstate/math-open-problems@abbec61f52e1f4b4d367fd67e73e4d2501ac9c74`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B08/20260923T091414Z-fleet04-B08-QFORM-r1/REPORT.md`.

For

`Q_R=X_0^2+2R U_1V_1+2R^(-1)U_2V_2`, `R>=3`,

the partner proves

`||p_(Q_R)||_infinity<7.251`                                   (1.9)

for every admissible product law. This is the exact anisotropic fixed-`E_2` endpoint. The partner report left arbitrary same-bank leakage and general added cross/tail interactions outside its stated theorem.

## 2. First closure: r37's diagonal-light restriction disappears at L3 level

Let `H={1,2}` be exactly two ORIGINAL hub coordinates, `L` a disjoint arbitrary light bank, and let `C=A[H,L]` have rank exactly two. Condition only coordinates outside `H union L`. The retained conditional form is

`Q(U,V)=F(U)+2U^T C V+G(V)+c`,                                 (2.1)

where `F` and `G` are **arbitrary** quadratic-affine functions. Thus all non-diagonal same-bank light curvature is retained.

Since the hub bank has exactly two physical coordinates, apply (1.1). If

`G_C=C C^T`                                                     (2.2)

then

`sigma_1(C)sigma_2(C)=sqrt(det G_C)`.                           (2.3)

Therefore

`boxed:
 ||p_Q||_3
 <=3^(2/3)e^(1/3)[det(C C^T)]^(-1/6).
`                                                                    (2.4)

Equivalently, in the r37 transpose convention where `C` is light-by-two,

`boxed:
 ||p_Q||_3
 <=3^(2/3)e^(1/3)[det(C^T C)]^(-1/6).
`                                                                    (2.5)

This requires **no row-leverage gate and no diagonal-light assumption**. It is not yet an `L^infinity` conclusion, but it removes the exact interface left by r37 at the correct fractional level.

If a disjoint original scalar square completion with coefficient `a` is available and this exact-rank-two cross bank is in its residual, (1.2) gives

`boxed:
 ||p_Q||_infinity
 <7.829 |a|^(-1/2)[det(C C^T)]^(-1/8).
`                                                                    (2.6)

The conclusion here is essential boundedness; continuity is not claimed.

## 3. A physical 2x2 core gives a leakage-stable certificate

The previous statement can be strengthened and made stable under added cross/tail entries.

Let `D` be a literal physical `2x2` submatrix of a post-Schur residual cross block `M`, and suppose

`|det D|>=delta L^2`,                                           (3.1)

with `delta>0` and scale `L>0`.

### 3.1 Exact-rank-two residual

If the whole physical cross block has rank exactly two, choose one row and one column of `D` as the incident anchors. Its squared determinant is one term of `Delta_jr(M)`, so

`Delta_jr(M)>=det(D)^2>=delta^2 L^4`.                            (3.2)

If the genuine outer scalar coefficient obeys

`|a|>=tau L`,                                                   (3.3)

then (1.4) gives

`boxed:
 ||p_Q||_infinity
 <= C_grp tau^(-1/2) delta^(-1/4) L^(-1).
`                                                                    (3.4)

All same-bank quadratic-affine terms are arbitrary.

### 3.2 Arbitrary-rank residual with arbitrary appended cross/tail entries

No rank assumption is needed for the aggregate theorem. Because `E_2(M)` is the sum of squared physical `2x2` minors,

`E_2(M)>=det(D)^2>=delta^2 L^4`.                                (3.5)

Therefore (1.7) gives

`boxed:
 ||p_Q||_infinity
 < C_E2 tau^(-1/2) delta^(-1/4) L^(-1).
`                                                                    (3.6)

This is the desired **leakage-stable** part: once a physical core survives in the exact post-Schur residual, arbitrary extra rows/columns and extra cross/tail entries cannot destroy its contribution to `E_2`, because the squared minor remains one nonnegative summand. Arbitrary same-bank curvature and all other residual couplings are already allowed by the source theorem.

This statement does not assert that arbitrary coefficient perturbations preserve the target's three-large-eigenvalue property. Its role is conditional inside the full target proof: whenever an actual target matrix reaches this post-Schur configuration, the analytic payment is valid.

## 4. Apply the designated partner result, then strengthen its leakage scope

Scale the partner family by `L>0`:

`Q_(R,L)=L X_0^2+2LR U_1V_1+2L R^(-1)U_2V_2`, `R>=3`.          (4.1)

Its matrix has eigenvalues

`{L,+LR,-LR,+L/R,-L/R}`,                                       (4.2)

so for `L>=1` it is target-admissible, and by density scaling the designated fleet04/B08 theorem gives the actual inequality

`boxed: ||p_(Q_(R,L))||_infinity<7.251/L.`                      (4.3)

Now write the physical cross core

`D_R=L diag(R,R^(-1))`,                                        (4.4)

so

`det D_R=L^2`.                                                  (4.5)

The grouped theorem (1.4) applies to this same exact-rank-two core with `a=L` and gives

`boxed:
 ||p_Q||_infinity
 <=C_grp/L
 =7.2500551088.../L
 <7.251/L,
`                                                                    (4.6)

**even when arbitrary same-side quadratic-affine terms are present on the two arm banks**, provided the post-completion cross block remains exact rank two. Thus the same numerical partner-scale endpoint survives the previously excluded same-bank curvature.

If arbitrary additional post-Schur cross/tail entries enlarge the residual cross block but retain the physical core `D_R` literally, then (3.5) gives `E_2(M)>=L^4`, and (3.6) gives

`boxed:
 ||p_Q||_infinity<36.45/L.
`                                                                    (4.7)

This is not as sharp as (4.6), but it is rank-insensitive and retains arbitrary added cross/tail couplings and arbitrary same-bank curvature.

So the partner's anisotropic fixed-`E_2` obstruction is no longer an obstruction to same-bank curvature or to **appended** cross/tail leakage. The only remaining issue is leakage caused by the outer scalar completion itself, which can subtract a rank-one matrix from the core. That cancellation is handled next by an exact router rather than by an invalid survival assertion.

## 5. Exact scalar-Schur cancellation router for the anisotropic core

Take a genuine outer physical scalar with

`a=epsilon L`, `epsilon in {+1,-1}`, `L>0`,                     (5.1)

and the pre-completion anisotropic physical core

`D_R=L diag(R,R^(-1))`, `R>=3`.                                (5.2)

Let the outer coordinate couple to the two row-side core coordinates by

`u=(u_1,u_2)^T`                                                 (5.3)

and to the two column-side core coordinates by

`v=(v_1,v_2)^T`.                                                (5.4)

After the **exact scalar Schur completion**, the physical `2x2` cross core is

`D_R' = D_R - u v^T/a
     = L diag(R,R^(-1)) - epsilon u v^T/L`.                     (5.5)

### Lemma 5.1 — exact determinant identity

The matrix determinant lemma gives

`boxed:
 det D_R'
 =L^2[1-epsilon( u_1v_1/(L^2R) + R u_2v_2/L^2 )].
`                                                                    (5.6)

This identity is exact; no perturbative expansion is used.

Fix any threshold `0<theta<1`.

### Branch A: the physical core survives

If

`|det D_R'|>=theta L^2`,                                       (5.7)

then `D_R'` is a literal post-Schur physical minor. Hence, for an arbitrary-rank residual cross block containing it,

`E_2(M)>=theta^2 L^4`,                                         (5.8)

and the arbitrary-rank receiver gives

`boxed:
 ||p_Q||_infinity
 < C_E2 theta^(-1/4)L^(-1).
`                                                                    (5.9)

If the residual cross block is exact rank two, the grouped receiver improves this to

`boxed:
 ||p_Q||_infinity
 <=C_grp theta^(-1/4)L^(-1).
`                                                                    (5.10)

### Branch B: Schur cancellation forces a localized physical triangle

If instead

`|det D_R'|<theta L^2`,                                        (5.11)

then (5.6) and the reverse triangle inequality imply

`|u_1v_1/(L^2R)+R u_2v_2/L^2|>1-theta`.                        (5.12)

Therefore at least one of the two actual physical channels satisfies

`boxed:
 |u_1v_1|/(L^2R)>(1-theta)/2
`                                                                    (5.13a)

or

`boxed:
 R|u_2v_2|/L^2>(1-theta)/2.
`                                                                    (5.13b)

If the two arm coefficients are

`h_1=LR`, `h_2=L/R`,                                            (5.14)

this is equivalently

`boxed:
 exists i in {1,2}: |u_i v_i| > [(1-theta)/2] L |h_i|.
`                                                                    (5.15)

Thus cancellation of the aggregate post-Schur `E_2` currency cannot disappear without leaving a **genuine original-coordinate localized triangle**: the outer-to-row coefficient `u_i`, outer-to-column coefficient `v_i`, and the corresponding arm coefficient `h_i` obey the scale-invariant product relation (5.15).

This is exactly the kind of aligned/high-leverage state r37 routed to but did not quantify. No spectral rotation and no selection among a dimension-growing family is involved; there are only the two physical partner channels.

### Convenient threshold theta=1/2

At `theta=1/2`, Branch A yields

`boxed:
 ||p_Q||_infinity<43.34/L
`                                                                    (5.16)

for arbitrary residual cross rank, because

`C_E2 2^(1/4)=43.3386850947...`,                                (5.17)

and

`boxed:
 ||p_Q||_infinity<8.622/L
`                                                                    (5.18)

in exact rank two, because

`C_grp 2^(1/4)=8.6218171197...`.                                (5.19)

Failure forces

`boxed:
 exists i: |u_i v_i| > L|h_i|/4.
`                                                                    (5.20)

The new router therefore converts the dangerous statement “rank-one Schur leakage may cancel the core” into a concrete two-case theorem with an explicit paid branch and an explicit localized survivor.

## 6. Apply the newest fractional-volume result to the high-rank leakage branch

The newest required `c2414...` volume theorem gives a continuity upgrade on a genuine diffuse high-rank subbranch of the arbitrary-rank residual from Section 3.

Let `M` be the exact **post-Schur** physical cross block. Let `M_0` be its top-three singular-value truncation. Suppose for some `rho>0`

`s_3(M)>=rho L`,                                                (6.1)

`s_4(M)<=s_3(M)/16`,                                           (6.2)

and the physical row leverage of `range(M_0)` is at most `1/2`.  (6.3)

Then `||M-M_0||op=s_4(M)<=s_3(M)/16`, so the newest source applies with `a=s_3(M)` and gives

`boxed:
 ||p_Q||_infinity<23/s_3(M)<=23/(rho L),
 p_Q in C_0(R).
`                                                                    (6.4)

This is an actual application of the newest volume-stability theorem to the leakage state. It retains arbitrary self blocks and outside couplings. If its spectral-tail/leverage hypotheses fail, Sections 3 and 5 still supply the `E_2` essential-boundedness receiver whenever the physical core survives. Thus the newest volume result is a **continuous diffuse exit**, while the new Schur router isolates the non-diffuse cancellation state.

## 7. What has been closed and what remains

### Closed in this run

1. **r37 diagonal-light interface at fractional level.** Exact two-hub/rank-two cross geometry has an `L^3` output density with arbitrary non-diagonal same-bank light curvature, no leverage gate: (2.4)-(2.5).

2. **Outer-square exact-rank-two payment.** With a genuine scalar square, the same branch is `L^infinity`, (2.6), again retaining arbitrary same-bank curvature.

3. **Designated partner same-bank leakage.** The partner anisotropic core keeps its `<7.251/L` scale under arbitrary same-side quadratic-affine terms in the exact-rank-two residual, by (4.6).

4. **Appended cross/tail leakage.** If the post-Schur residual contains the anisotropic physical core, arbitrary additional cross/tail entries are paid by aggregate `E_2`, giving `<36.45/L`, (4.7).

5. **Outer-Schur cancellation is quantified.** Either the core determinant survives and yields an explicit `L^infinity` bound, or one of two original-coordinate physical triangles satisfies (5.15). No pre/post-Schur survival assumption is made.

6. **Newest volume theorem applied.** A top-three diffuse/tail-separated post-Schur residual gets the continuous bound (6.4).

### Still open

The unrestricted QFORM conjecture is **OPEN**. The remaining B08 obstruction after this run is now sharper:

`QFORM-LOCALIZED-TRIANGLE-PLUS-SECOND-ARM-RECEIVER-v1` — OPEN.

Starting from the localized cancellation packet

`|u_i v_i| > c L |h_i|`

with `c=1/4` at the convenient threshold, consume the full quadratic form while retaining arbitrary diagonal/off-diagonal curvature on the three physical coordinates, the second anisotropic arm, arbitrary additional spectrum, and every unused coupling. A proof must not infer a well-conditioned principal pair merely from one large off-diagonal product: pair determinants can cancel against diagonals. The exact-rank-two/grouped and `E_2` results above already pay the complementary core-survival states, so the next run should attack this localized triangle rather than redo the diffuse volume calculation.

Continuity is proved only on the c2414 diffuse volume subbranch in Section 6 (and the older r37 diffuse branch), not on the grouped-square or aggregate-`E_2` branches.

## 8. Finite checks

`CHECKS.py` and `CHECKS.txt` are committed beside this report. They record:

- `C_grp=7.250055108887958`;
- one-bank-two-coordinate source constant `7.828119185258699`;
- aggregate-`E_2` scalar-Schur constant `36.44334493792993`;
- theta=`1/2` constants `8.621817119651388` and `43.33868509468467`;
- 5,000 seeded tests of the exact determinant identity (5.6), maximum relative-like numerical error `1.414e-14`;
- zero violations of the theta=`1/2` cancellation router.

The checker terminates `QFORM_B08_R38_CHECK_PASS`. These finite checks verify algebra/constants only; they are not proof of the universal theorem.

## 9. Scope and review status

The new implications are supporting results pending independent review. No full-solution claim is made, so the two required end-to-end full-proof reviews are not yet applicable. Repository publication is durable transport, not verified native learned-memory ingestion. Status remains `WITHOUT_VERIFIED_BRAIN`.
