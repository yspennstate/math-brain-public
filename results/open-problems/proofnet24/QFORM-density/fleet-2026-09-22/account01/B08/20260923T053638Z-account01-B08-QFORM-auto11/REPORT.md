SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B08, 2026-09-23T05:36:38.962978Z.
attacking: a basis-invariant self-dual diffuse curvature transfer, then spending the resulting physical cross scale through account02/B08's latest fractional-volume/star-nested router.

# account01/B08 — self-dual diffuse transfer and a basis-invariant 1/3-leverage router

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T053638Z-account01-B08-QFORM-auto11`  
Status: `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_STRUCTURAL_THEOREM / DESIGNATED_PARTNER_APPLIED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`; repository retrieval/write is not native learned-memory ingestion.

The unrestricted quadratic-form bounded-density conjecture remains OPEN. The new result is a genuine diffuse branch: it assumes a rank-three reducing spectral subspace whose physical-coordinate leverage is bounded, and it keeps every coefficient and every spectral direction outside that subspace inside the actual physical child/cross blocks. It does not assume moments, compact support, connected support, iid laws, Gaussianity, log-concavity, or independence after a spectral rotation. Continuity is asserted only on the explicitly paid partner branches below.

Fresh owner control was read from `yspennstate/math-research-brain@dc95d149ba6057b0cea20701ab5017e4decccfcf`; OWNER CONTROL remains revision `2026-09-22.15`, with QFORM the sole research target. The live correction inbox was refreshed at that source. In addition, the fresh structural correction `QFORM-BALANCED-FIXED-PACKET-EXTRACTION-FALSE-v1` was read from `yspennstate/math-open-problems@551cf0474a03aec13d999ee9632619ede59c17ff`: the bare three-large-eigenvalue hypothesis does not force a fixed-scale finite physical packet, even in an exact-rank-three balanced-sign chamber. The theorem below does not make that forbidden inference; it first aggregates curvature at the level of a full physical cut.

## 1. Sources actually used

### 1.1 Previous B08 sharp transfer

The algebraic input is the completed B08 theorem `QFORM-SHARP-BALANCED-CURVATURE-TRANSFER-v1`, source

`yspennstate/math-open-problems@6723dbae37e95ed017ab4f14415eb0196d54e72a`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B08/20260923T050942Z-account01-B08-QFORM-auto11/REPORT.md`.

For three genuine orthonormal eigenvectors `R`, `AR=R Lambda`, `min_j |lambda_j|>=L`, and a physical cut `I|J` whose frame Gramians satisfy

`alpha I_3 <= G:=R_I^T R_I, H:=R_J^T R_J <= (1-alpha)I_3`,

put

`rho=sqrt(alpha/(1-alpha))`.

For each `m=1,2,3` and every `0<c<L rho`, either the child `A[I,I]` has at least `m` eigenvalues of modulus at least `c`, or the ACTUAL physical cross block `B=A[I,J]` has

`s_(4-m)(B)>rho(L rho-c)`.                                      (1.1)

The same statement holds with `I,J` reversed. The same source proves the finite-dimensional floating half-paving: if

`mu=max_i ||R_{i,*}||_2^2 <1/sqrt(6)`,                         (1.2)

there is a physical cut with

`alpha=1/2-sqrt(3/2)mu`.                                       (1.3)

For completeness, Section 2 rederives the identity needed here, so the new optimization can be checked without trusting a hidden change of normalization.

### 1.2 Latest designated partner account02/B08

The newest completed account02/B08 result available on fresh main is

`QFORM-FRACTIONAL-VOLUME-SELF-MATCHED-ROUTER-v1`,

source `yspennstate/math-open-problems@2e8dce7760ed0b7dc1ab1be7b9d82ecc3c7b7df1`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/20260923T050537Z-account02-B08-qform-diffuse-r21-ead7cd5c/REPORT.md`.

For an ORIGINAL-coordinate cross block `B`, write

`Z3=e3(B^T B)=sum_{|S|=|T|=3} det B[S,T]^2`.                    (1.4)

With `h=163/250`, `q=163/125`, if `Z3>=zeta^6`, then either the full ambient quadratic form has a continuous `C_0` density with

`||p_Q||_infinity < C_F/zeta`,
`C_F=3e/[(3-2q)sqrt(q)]=18.2175879095827...`,                  (1.5)

or there are a physical anchor row `i` and column `a` with

`Z_ia>(38/125)Z3`,                                              (1.6)

and on each side independently either the corresponding physical star norm exceeds `zeta`, or a residual nested packet exceeds `(19/125)Z3`.

The same partner report gives two scale-preserving tail compilers used below. If `s2(B)>b`, then either

`dist_F(B,{rank<=2})<b/8`,                                     (1.7)

or a completed `D5` branch gives a continuous density with

`||p_Q||_infinity < 48.627765612849/b`,                         (1.8)

or `s3(B)>b/120`, in which case `Z3>b^6/14400` and (1.5)-(1.6) apply at `zeta=b/14400^(1/6)`. If `s1(B)>b`, then either

`dist_F(B,{rank<=1})<b/8`,                                     (1.9)

or a completed `D5` branch gives

`||p_Q||_infinity <84.779241503085/b`,                          (1.10)

or `s2(B)>b/120`. Applying the two-cross compiler once more at `b2=b/120` gives either a rank-two tube `dist_F(B,{rank<=2})<b2`, a continuous `D5` bound

`||p_Q||_infinity <13.964658591666/b2`,                         (1.11)

or `s3(B)>b2/15`, hence `Z3>b2^6/225` and the router applies at `zeta=b2/225^(1/6)`.

These are equation-level uses of the designated partner theorem, not merely citations.

## 2. Exact balanced-cut identity

Let `R` have three orthonormal columns and satisfy

`A R=R Lambda`, `min_j |lambda_j|>=L`.                          (2.1)

For a physical cut `I|J`, set

`G=R_I^T R_I`, `H=R_J^T R_J=I_3-G`.                            (2.2)

Assume

`alpha I_3<=G,H<=(1-alpha)I_3`, `0<alpha<1/2`.                 (2.3)

Define

`U=R_I G^(-1/2)`, `V=R_J H^(-1/2)`,                           (2.4)

so `U,V` have orthonormal columns. With `B=A[I,J]`, put

`C=U^T A[I,I]U`,
`K=U^T B V`,
`T=H^(1/2)G^(-1/2)`,
`S=G^(1/2)Lambda G^(-1/2)`.                                    (2.5)

Restricting (2.1) to `I` and substituting `R_I=UG^(1/2)`, `R_J=VH^(1/2)` gives the exact identity

`boxed: C+K T=S.`                                               (2.6)

Since the eigenvalues of `G` lie in `[alpha,1-alpha]`,

`s3(S)>=L sqrt(alpha/(1-alpha))=L rho`,                         (2.7)

where

`rho=sqrt(alpha/(1-alpha))`.                                   (2.8)

Because `H=I-G` commutes with `G`,

`||T||<=sqrt((1-alpha)/alpha)=rho^(-1)`.                       (2.9)

If the child has fewer than `m` eigenvalues outside `(-c,c)`, then its compression `C` also has fewer than `m`: otherwise Cauchy interlacing, applied separately to positive and negative Ritz values, would force at least the same total number of ambient child eigenvalues of modulus at least `c`. Thus `s_m(C)<c`. The singular-value sum inequality with indices `m` and `4-m` gives

`L rho <=s3(S)<=s_m(C)+s_(4-m)(KT)`,                            (2.10)

and (2.9) implies

`s_(4-m)(B)>=s_(4-m)(K)>rho(L rho-c)`.                          (2.11)

This recovers (1.1) while retaining every unselected spectral direction of `A` in the ACTUAL blocks.

## 3. New theorem: choose the unique self-dual scale

The preceding transfer has two currencies at a chosen child threshold `c`:

`child scale = c`,
`cross scale = rho(L rho-c)`.                                  (3.1)

The old half-budget choice `c=L rho/2` is convenient but does not maximize the scale that is guaranteed in either branch. The common guaranteed currency is

`F(c)=min{c, rho(L rho-c)}`, `0<c<L rho`.                       (3.2)

The first term is strictly increasing in `c`, the second strictly decreasing, so the maximum occurs uniquely at their intersection:

`c=rho(L rho-c)`.                                               (3.3)

Solving gives

`boxed: d=L rho^2/(1+rho).}`                                   (3.4)

At this choice,

`rho(L rho-d)=d`.                                               (3.5)

### Theorem 3.1 — `QFORM-SELF-DUAL-REDUCING-PROJECTION-LADDER-v1`

Let `E` be a three-dimensional reducing subspace of a real symmetric matrix `A`, and assume every eigenvalue of `A|_E` has modulus at least `L>0`. Let `P_E` be its orthogonal projection and set

`mu=max_i (P_E)_{ii}<1/sqrt(6)`.                               (3.6)

Put

`alpha=1/2-sqrt(3/2)mu`,
`rho=sqrt(alpha/(1-alpha))`,
`d=L rho^2/(1+rho)`.                                           (3.7)

Then there is an ORIGINAL-coordinate cut `I|J` such that, for each child `K in {I,J}` and each `m=1,2,3`, at least one of

1. `A[K,K]` has at least `m` eigenvalues of modulus at least `d`;
2. the ACTUAL cross block `B=A[I,J]` satisfies

`boxed: s_(4-m)(B)>d`                                          (3.8)

holds.

Equivalently, if `k_K` denotes the number (capped at three) of eigenvalues of `A[K,K]` of modulus at least `d`, then

`k_K<=2  ==>  s_(3-k_K)(B)>d`.                                 (3.9)

If `k=min(k_I,k_J)<=2`, (3.9) holds with that `k`; otherwise **both** physical children retain three actual eigenvalues of modulus at least `d`.

#### Proof

Choose an orthonormal eigenbasis `R` of the reducing subspace `E`. Then

`||R_{i,*}||_2^2=(P_E)_{ii}`,                                  (3.10)

so the finite-dimensional floating theorem applies with the basis-invariant leverage `mu`, producing a cut satisfying (2.3) with (3.7). Apply (2.11) at `c=d`. Identity (3.5) makes the cross threshold exactly `d`, proving (3.8). Apply the same argument after swapping `I,J`. QED.

### Basis-invariant high-spectral-window corollary

Let

`P_L=1_{|A|>=L}`                                                (3.11)

be the full spectral projection onto eigenvalues of modulus at least `L`. If

`rank P_L>=3`, `max_i(P_L)_{ii}<=mu<1/sqrt(6)`,                (3.12)

choose any three eigenvectors from that spectral subspace and let `E` be their span. Since `P_E<=P_L` as orthogonal projections,

`(P_E)_{ii}<= (P_L)_{ii}<=mu`.                                 (3.13)

Therefore Theorem 3.1 applies. This statement is invariant under basis changes inside repeated eigenspaces: it is formulated through the full spectral projection first, then selects a genuine reducing three-subspace. No independence is claimed after this spectral selection; all probabilistic work remains on the physical coordinate cut.

## 4. Clean universal numbers at high-spectral leverage <=1/3

Assume the basis-invariant condition

`max_i (P_L)_{ii}<=1/3`.                                       (4.1)

Then the worst-case floating constants are attained at `mu=1/3`:

`alpha=(3-sqrt(6))/6=0.0917517095361370...`,                   (4.2)

`rho=sqrt(3)-sqrt(2)=0.317837245195782...`,                     (4.3)

and

`boxed: d=tau L,  tau=rho^2/(1+rho)=0.0766562902983031...>3/40.` (4.4)

The former half-budget common cross scale was

`(rho^2/2)L=0.0505102572168219...L`.

Thus the self-dual choice enlarges the guaranteed common child/cross currency by the factor

`2/(1+rho)=1.51763809020504...`.                               (4.5)

This is not merely a constant optimization inside an already paid statement: it materially strengthens every downstream inverse-scale bound and every physical determinant packet emitted by the partner router.

## 5. Actual application of account02/B08 at the new scale

Use the cut from Theorem 3.1 and put `k=min(k_I,k_J)`.

### 5.1 k=0: three actual cross directions

Then

`s3(B)>d`, hence `Z3>d^6`.                                     (5.1)

Apply the designated partner router (1.5)-(1.6) with `zeta=d`. Either the FULL ambient form has a continuous `C_0` density and

`boxed: ||p_Q||_infinity <237.653/L <238/L,`                    (5.2)

or there are physical anchors `(i,a)` with

`Z_ia>(38/125)Z3>6.16822735163e-8 L^6`,                        (5.3)

and on each side either the anchor star norm is greater than

`d>0.07665629029 L`,                                            (5.4)

or a residual nested packet is greater than

`3.08411367582e-8 L^6`.                                        (5.5)

This is a direct equation-level use of the latest account02/B08 theorem.

### 5.2 k=1: one child direction, two cross directions

Now `s2(B)>d`. The partner's two-cross compiler gives one of:

1. the genuine tube

`dist_F(B,{rank<=2})<d/8=0.00958203628729 L`;                   (5.6)

2. a continuous `D5` density bound

`||p_Q||_infinity<634.362/L`;                                   (5.7)

3. `s3(B)>d/120`, hence `Z3>d^6/14400`.

In case 3 set

`zeta1=d/14400^(1/6)=0.0155413013942 L`.                        (5.8)

The latest router then gives either

`boxed: ||p_Q||_infinity<1172.205/L<1173/L`                     (5.9)

with a continuous `C_0` density, or an anchor packet larger than

`4.28349121641e-12 L^6`,                                       (5.10)

and on each side a star norm `>zeta1` or a nested packet larger than

`2.14174560821e-12 L^6`.                                       (5.11)

Thus outside the explicit rank-two Frobenius tube, the k=1 branch is either already continuously paid or converted to a fully physical star/nested aggregate.

### 5.3 k=2: two child directions, one cross direction

Now `s1(B)>d`. The partner's one-cross compiler gives one of:

1. the genuine tube

`dist_F(B,{rank<=1})<d/8=0.00958203628729 L`;                   (5.12)

2. a continuous `D5` density bound

`||p_Q||_infinity<1105.966/L`;                                  (5.13)

3. `s2(B)>b2=d/120=0.000638802419153 L`.

Apply the two-cross compiler at `b2`. It gives a rank-two tube

`dist_F(B,{rank<=2})<b2`,                                      (5.14)

or a continuous `D5` bound

`||p_Q||_infinity<21860.686/L`,                                 (5.15)

or `s3(B)>b2/15`. In the last case

`Z3>b2^6/225`,
`zeta2=b2/225^(1/6)=0.000259021689903 L`.                       (5.16)

The latest router therefore gives either

`boxed: ||p_Q||_infinity<70332.288/L<70333/L`                   (5.17)

with a continuous `C_0` density, or an anchored packet larger than

`9.18100826563e-23 L^6`,                                       (5.18)

with each side carrying a star norm `>zeta2` or a nested packet larger than

`4.59050413281e-23 L^6`.                                       (5.19)

The constants are intentionally ugly but dimension-free and law-free. The point is structural: the full true cross block is either close to rank one/two, is analytically paid, or carries a concrete aggregate physical packet before any reciprocal minor is selected.

### 5.4 k=3: bilateral retained-three branch

If `k=3`, then **both** principal physical children have three actual eigenvalues of modulus at least `d`. This is not declared paid. A naive recursive use would lose a factor `d/L<1` at every depth, and the fresh account03/B11 correction shows that one cannot replace the collective branch by a fixed-scale finite local packet under the bare spectral hypothesis.

This is now the clean surviving diffuse debt: aggregate a high-cardinality physical bank before local inversion, or prove a non-multiplicative recursion/energy monotonicity that spends the two retained-three children without repeated scale loss.

## 6. Why this does not conflict with the newest fixed-packet correction

The fresh account03/B11 family has every fixed physical `2x2` second singular value tending to zero, despite three large global eigenvalues. Therefore any conclusion of the form “three large eigenvalues force one bounded-cardinality child packet at fixed scale” is false.

Theorem 3.1 asserts something different. Under a diffuse **spectral projection** hypothesis it first forms a full original-coordinate cut and conserves spectral curvature between (i) the complete principal child and (ii) the complete cross operator. The partner theorem then aggregates the entire squared-minor law before it ever selects an anchor. If concentration occurs, the anchor/nested object is an output of the aggregate volume law, not an assumed fixed local minor. The correction therefore narrows the next step but does not challenge any implication proved here.

## 7. Scope and first unpaid implication

The full target is still open. The present result proves a quantitatively stronger and basis-invariant diffuse routing theorem under

`max_i [1_{|A|>=L}]_{ii}<=1/3`.                                (7.1)

Its paid branches establish a continuous `C_0` density with explicit constants. The low-rank tubes, star/nested states, and bilateral retained-three branch are not yet universally paid here. Essential boundedness or continuity is not claimed for those structural survivors merely from this report.

The first unpaid implication is

`QFORM-SELFDUAL-BANK-AGGREGATE-CLOSURE-v1`:

> Starting from the self-dual cut at scale `d>=3L/40`, pay the bilateral retained-three branch or the emitted low-rank/star/nested branch by a high-cardinality ORIGINAL-coordinate aggregation that does not multiply scale losses and does not delete a small matrix tail. A valid closure should convert collective bank curvature into a bounded-density innovation before reciprocal determinant payment, in the manner demanded by `QFORM-BALANCED-FIXED-PACKET-EXTRACTION-FALSE-v1`.

This changes mechanism rather than repeating the previous fixed-packet attempt.

## 8. Computation record

`CHECK.py` and `CHECK_OUTPUT.txt` in this immutable run directory verify the exact self-dual identity, `tau>3/40`, and every displayed numerical constant. The output ends

`QFORM_B08_SELFDUAL_ROUTER_CHECK_PASS`.

No Monte Carlo evidence is used in any theorem. No scheduler state, notifications, email, account permissions, public visibility, remote workflow, installation, paid API, or other research assignment was changed.
