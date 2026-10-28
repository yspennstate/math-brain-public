SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B20, 2026-09-23T03:15:11Z.
attacking: the co-heavy two-rank-two aggregate obstruction by an exact generalized-eigen normal form, with a product-preserving payment of the singular partition endpoint using account04/B20.

# account03/B20 r23 — generalized-eigen skeleton for the 1+2+2 O3 obstruction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Proof closure and keeper  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED STRUCTURAL REDUCTION AND TARGET-LEVEL ENDPOINT / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository transport is not native learned-memory ingestion.  
**Continuity:** not proved by the new endpoint; the full continuity request remains open.

## 1. Source boundary


The immediate exact-rank-three source is account03/B19 r22,
`yspennstate/math-open-problems@d0d68512c0e8ddaa3893134fdfc03e2214a751aa`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260923T020435Z-account03-B19-QFORM-r22/REPORT.md`.
It reduces a 1+2+2 O3 chamber to one rank-one source bank and two rank-two source banks, and in the failed-grouped-exit chamber gives the exact transverse quantities used below.

The newest complementary co-heavy source is account01/B19 r12,
`yspennstate/math-open-problems@8519812f42a34ba2612f61ff2d4c8fbbfad8c6ee`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B19/20260923T025504Z-account01-B19-QFORM-r12/REPORT.md`.
It shows that small individual grouped determinants do not force a single good physical row; instead co-heavy rows concentrate on the common intersection line of the two rank-two source planes.

The designated partner actually used is account04/B20 r4,
`yspennstate/math-open-problems@f97aa31585b7b547a116d4580f898576af4e0842`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B20/20260923T011956Z-account04-B20-QFORM-r4/REPORT.md`.
Its cap-sensitive partitioned cross-transverse inequality is applied at an actual numerical scale in Section 5.

The rank-one-bank Schur theorem used for the complementary endpoint is account03/B19 r19, immutable at
`yspennstate/math-open-problems@2492c23f859cfea78eb7b1c74f45ae4c5611de87`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260922T223200Z-account03-B19-QFORM-r19/REPORT.md`.

No post-rotation independence, arbitrary-joint coarea, conditional-cap-as-independence, law-uniform pointwise Fresnel decay, one-good-minor selection, or small-coefficient perturbation is used.

## 2. Exact 1+2+2 frame setup

Work in an exact-rank-three core

`A=R M R^T`, `R^T R=I_3`, `M=M^T`, `s_min(M)>=1`.

Partition original-coordinate spectral rows into disjoint source banks `H,G_1,G_2` and assume

`S_H=sum_(h in H) u_h u_h^T = lambda v v^T`,

where `0<lambda<=1`, `|v|=1`, while

`S_j=sum_(i in G_j) u_i u_i^T`, `rank(S_j)=2`, `j=1,2`.

Parseval is

`lambda vv^T+S_1+S_2=I_3`.                                      (2.1)

Put

`D:=I-lambda vv^T=S_1+S_2`.                                    (2.2)

For the moment assume `0<lambda<1`, so `D` is positive definite. Let `P=I-vv^T` and define the transverse compressions

`A_j=(P S_j P)|_(v^perp)`, `d_j=det A_j`,

and

`m=1-d_1-d_2`.                                                   (2.3)

These are exactly the currencies in account03/B19 r22. In its failed grouped-determinant branch one has

`d_1<m/4`, `d_2<m/4`;                                             (2.4)

hence `m>2/3`.

## 3. New exact normal form

### Theorem 3.1 — `QFORM-O3-TWORANK2-GENERALIZED-EIGEN-SKELETON-v1`

For `0<lambda<1`, set

`T=D^(-1/2) S_1 D^(-1/2)`.                                      (3.1)

Then there are an orthonormal basis `(e_1,e_*,e_0)` of `R^3` and a scalar `q in (0,1)` such that

`T=e_1e_1^T+q e_*e_*^T`,                                        (3.2)

`I-T=e_0e_0^T+(1-q)e_*e_*^T`.                                   (3.3)

Consequently

`S_1=D^(1/2)(e_1e_1^T+q e_*e_*^T)D^(1/2)`,                      (3.4)

`S_2=D^(1/2)(e_0e_0^T+(1-q)e_*e_*^T)D^(1/2)`.                   (3.5)

The two bank planes therefore have the exact common line

`Ran(S_1) intersect Ran(S_2)=span(D^(1/2)e_*)`.                  (3.6)

Moreover, writing

`x=(v.e_0)^2`, `y=(v.e_1)^2`, `z=(v.e_*)^2`,                    (3.7)

one has the exact identities

`d_1=q x`,                                                       (3.8)

`d_2=(1-q)y`,                                                    (3.9)

`m=(1-q)x+q y+z`.                                                (3.10)

#### Proof

From `0<=S_1<=D`, congruence by `D^(-1/2)` gives `0<=T<=I`. Congruence preserves rank, so `rank(T)=2`. Also

`I-T=D^(-1/2)S_2D^(-1/2)`

has rank two. Thus `T` has exactly one zero eigenvalue and, because `I-T` has exactly one zero eigenvalue, exactly one unit eigenvalue. Its third eigenvalue is strictly between zero and one. This proves (3.2)-(3.5).

Because `D^(1/2)` is invertible,

`Ran(S_1)=D^(1/2)span(e_1,e_*)`,
`Ran(S_2)=D^(1/2)span(e_0,e_*)`,

which proves (3.6).

On `v^perp`, `D^(1/2)` is the identity. Hence the transverse compression of `S_1` is the compression of `T`. For a symmetric `3x3` matrix, the determinant of its compression to `v^perp` is `v^T adj(T)v`. Since the eigenvalues of `T` in the displayed basis are `(1,q,0)`,

`adj(T)=q e_0e_0^T`.

Therefore `d_1=q(v.e_0)^2=qx`. Similarly `I-T` has eigenvalues `(0,1-q,1)` and

`adj(I-T)=(1-q)e_1e_1^T`,

which gives `d_2=(1-q)y`. Finally `x+y+z=1`, so

`1-qx-(1-q)y=(1-q)x+qy+z`,

proving (3.10). QED.

This is deterministic spectral algebra only. The vectors `e_1,e_*,e_0` are not declared to be independent random coordinates.

## 4. Robust near-complementarity forces the rank-one companion toward the common generalized line

Let `g,h` be the least positive eigenvalues of `S_1,S_2` respectively. The singular-value inequality applied to

`S_1=(D^(1/2)T^(1/2))(D^(1/2)T^(1/2))^T`

gives

`g=lambda_2(S_1)<=||D^(1/2)||^2 lambda_2(T)=q`,                   (4.1)

because `||D||=1`. Similarly

`h<=1-q`.                                                         (4.2)

Thus the robust packet

`g,h>=1/3`                                                        (4.3)

forces

`1/3<=q<=2/3`.                                                    (4.4)

### Corollary 4.1 — quantitative common-line alignment

Assume (2.4) and (4.3). Then

`boxed: (v.e_*)^2>1/4.`                                           (4.5)

#### Proof

By (3.8)-(3.10), (2.4) says

`qx<m/4`, `(1-q)y<m/4`.                                          (4.6)

Hence

`x<m/(4q)`, `y<m/[4(1-q)]`.                                      (4.7)

Substitute these into `m=(1-q)x+qy+z`:

`z>m [1-(1-q)/(4q)-q/(4(1-q))]`.                                (4.8)

Put `u=q(1-q)`. From (4.4), `u>=2/9`, and the bracket in (4.8) is

`3/2-1/(4u)>=3/8`.                                                (4.9)

Also adding the two inequalities in (4.6) gives

`d_1+d_2<m/2`.

Since `d_1+d_2=1-m`, this implies `m>2/3`. Therefore

`z>(2/3)(3/8)=1/4`. QED.

Thus the newest account01/B19 statement that co-heavy rows cluster on the intersection line now has an exact bank-level coordinate: the line is `span(D^(1/2)e_*)`, and in the robust failed-grouped-exit chamber the rank-one companion direction has coefficient greater than `1/2` along the corresponding generalized eigenvector.

The actual Euclidean angle to the physical common line is also explicit. If

`ell=D^(1/2)e_*/||D^(1/2)e_*||`,

then

`|v.ell|^2=(1-lambda)z/(1-lambda z)`.                            (4.10)

Consequently either

`lambda>3/4`, in which case the total longitudinal variance carried by the two rank-two banks is

`v^T(S_1+S_2)v=1-lambda<1/4`,                                   (4.11)

or

`lambda<=3/4`, in which case (4.5),(4.10) give

`boxed: |v.ell|^2>1/16.`                                         (4.12)

This is a clean split between an approximate longitudinal/transverse partition and a genuinely three-bank common-line geometry. No perturbative density claim is inferred from (4.11).

## 5. The singular partition endpoint lambda=1 is completely paid

The normal form above deliberately excluded `lambda=1`; this boundary can be paid rather than left singular.

If `lambda=1`, then (2.1) gives

`S_1+S_2=P=I-vv^T`.                                              (5.1)

Positivity implies `S_1v=S_2v=0`. Since both have rank two, both bank planes equal `v^perp`. Thus the original-coordinate leaves split exactly into

- the rank-one source bank `H`, whose normalized aggregate scalar `Z` has density cap `L_0<=sqrt(2)`, and
- the disjoint source `G_1 union G_2`, whose two-dimensional orthogonal product projection `Y` has joint density cap `M_0<=2`.

The two banks are genuinely independent because they are disjoint original-coordinate sets.

Write the effective matrix in the orthogonal splitting `v direct_sum v^perp` as

`B=[[t,b^T],[b,C]]`, `t=v^TMv`, `D_0=|det M|>=1`.                (5.2)

### Case 1: `|t|<=1/2`

Apply the completed designated-partner account04/B20 r4 cap-sensitive inequality (its equation (3.1)) to the genuine independent aggregate scalar and transverse product receiver. Its spectral lemma gives

`P_cross>= (1-|t|)D_0>=D_0/2`.                                  (5.3)

With `L_0<=sqrt(2)` and `M_0<=2`, the actual substitution is

`||p_Q||_infinity
 <=103680^(1/3)(L_0M_0)^(2/3)(D_0 P_cross)^(-1/6)`
` <=103680^(1/3) 2^(7/6) D_0^(-1/3)`
` <105.463`.                                                      (5.4)

This is the required equation-level use of account04/B20, not merely a citation.

### Case 2: `|t|>1/2`

Apply account03/B19 r19 `QFORM-RANKONE-BANK-SCHUR-PIVOT-v1` to the whole bank `H`. Here `lambda=1`, so

`||p_Q||_infinity
 <=16sqrt(60)[|t|D_0]^(-1/4)`
` <=16sqrt(60)2^(1/4)`
` =147.384939...<148`.                                           (5.5)

Combining (5.4)-(5.5):

`boxed: lambda=1 implies ||p_Q||_infinity<148.`                   (5.6)

This is an essential-density statement. Neither source supplies enough here to promote (5.6) to a full continuous-density conclusion, so continuity is not claimed.

## 6. What is newly closed and the exact next debt

The co-heavy 1+2+2 obstruction now has an exact geometry rather than only qualitative plane language:

1. for `0<lambda<1`, the two rank-two banks are exactly a private/common/private generalized-eigen skeleton `(e_1,e_*,e_0)` with one scalar `q`;
2. in the robust failed-grouped-exit chamber `g,h>=1/3`, the generalized common-line coefficient obeys `(v.e_*)^2>1/4`;
3. either the actual common line has fixed angle to the rank-one companion (`lambda<=3/4`), or the total mixed longitudinal leakage of the two rank-two banks is `<1/4` (`lambda>3/4`);
4. the singular exact-partition endpoint `lambda=1` is no longer a debt: it has the universal target-level cap `<148`.

The first unpaid implication is therefore

`QFORM-O3-COMMONLINE-OVERLAP-PAYMENT-v1`:

for `0<lambda<1`, use the exact skeleton above together with the account01/B19 co-heavy intersection-line concentration to pay either the fixed-angle common-line branch or the small-but-nonzero longitudinal-leakage branch while preserving original-coordinate product provenance. A valid proof must aggregate the shared leaves before taking any reciprocal local coefficient. In particular, one may not replace the shared longitudinal/transverse leaves by independent variables merely because their projection density is bounded.

The weak-bank limits `g<1/3` or `h<1/3`, arbitrary-extra-spectrum splice, and other global N3/O3 routing debts remain separate. No full solution or counterexample is asserted.

## 7. Full-target status

The unrestricted conjecture remains `OPEN / NOT PROVED / NOT DISPROVED`. The new theorem is a source-valid supporting reduction plus a fully paid exact endpoint. Full-target continuity remains open.
