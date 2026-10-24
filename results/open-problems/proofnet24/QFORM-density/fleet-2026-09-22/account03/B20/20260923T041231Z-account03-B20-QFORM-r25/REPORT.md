SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B20, 2026-09-23T04:12:31Z.
attacking: the current small-Pluecker collar's second-gradient/rank-one-alignment debt, by turning failure of rank-one alignment into a fixed aggregate physical two-gradient packet and then paying its diffuse rank-three exit; also applying account04/B20's conditioned-whitened theorem at the collar scale.

# account03/B20 r25 — quantitative stable-alignment compiler and diffuse volume exit

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Proof closure and keeper  
**Classification:** `ESSENTIAL_STEP_APPLIED / NEW STRUCTURAL COMPILER + PAID TARGET BRANCHES / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository access is not native receiver-memory ingestion.  
**Continuity:** proved only in the two diffuse branches identified below; not proved for the unrestricted target.

## 1. Fresh source boundary

Fresh publication control is `yspennstate/math-research-brain@e8a9f6d7b937e36d4c491a2872dad2c281341436`, OWNER CONTROL revision `2026-09-22.15`, QFORM only, no B20 pause.

The immediate collar source is account03/B19 r23, canonical `yspennstate/math-open-problems@80403bc0adff2c5e8278848674c81448e9782e44`, path
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260923T030233Z-account03-B19-QFORM-r23/REPORT.md`.  In the remaining exact-rank-three small-Pluecker collar it supplies an ORIGINAL physical hub `i` such that

`c_i=||u_i||^2>1/4`,
`|A_ii|<1/64`,
`M:=||A[i,-i]||_2>sqrt(1023)/64`,

unless an earlier scalar-pivot branch already pays the density.

The freshest B19 r25 checkpoint, `yspennstate/math-open-problems@0c70646cf7135c489a17d42ad86f46448b36b883`, path
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260923T040358Z-account03-B19-QFORM-r25/CHECKPOINT.md`, gives the stable star-row alignment identity used below.  I rederive the quantitative consequence needed here rather than treating its numerical checker as proof.

The analytic volume receiver is the completed three-volume theorem at `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, path
`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.  In its q=4/3 form, if an original-coordinate cross block `B` has third-volume `Z=e3(BB^T)>0` and its row third-volume marginals are at most `2/3`, then the whole quadratic-plus-affine law has a bounded continuous density with

`||p_Q||_infinity <= (9 sqrt(3)e/2) Z^(-1/6)`.

The designated partner actually used is account04/B20 r2, canonical `yspennstate/math-open-problems@94bf446b8547b1124a37033e940ef594c460b64f`, path
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B20/20260922T141640Z-account04-B20-QFORM-r2/REPORT.md`.  Its conditioned-whitened theorem gives a continuous density `<27/delta` after conditioning ORIGINAL coordinates whenever the residual selected-frame Gram has spectral floor `delta` and every whitened residual leverage is at most `1/32`.

All arguments below remain in original physical coordinates.  No rotated random coordinates are declared independent; no arbitrary-joint rank-three coarea lemma, worst-fiber supremum, pointwise Fresnel decay, or one-good-minor inference is used.

## 2. Stable star-row alignment, with an explicit aggregate lower bound

Write the exact-rank-three collar matrix around its physical hub as

`A = [[a,m^T],[m,H]]`,

where `m=A[i,-i]`, `M=||m||_2`, and the residual original-coordinate set is `J`.  Thus

`M^2>1023/4096`.                                                   (2.1)

For every `j in J`, delete coordinate `j` and define the physical two-gradient area

`Delta_j^2
 = ||m_{-j}||_2^2 ||H[j,-j]||_2^2
   - <m_{-j},H[j,-j]>^2`.                                        (2.2)

By Lagrange's identity,

`Delta_j^2
 = sum_{k<l; k,l != j}
   (m_k H_jl - m_l H_jk)^2`.                                     (2.3)

Assume first that the hub star has no `3/4`-dominant physical atom:

`m_j^2 <= (3/4)M^2` for every j.                                  (2.4)

Then `||m_{-j}||^2>=M^2/4` for every j.  Put

`alpha_j=<H[j,-j],m_{-j}>/||m_{-j}||^2`,
`e_jk=H_jk-alpha_j m_k` for k != j.                               (2.5)

Orthogonal projection gives the exact identity

`sum_{k!=j} e_jk^2 = Delta_j^2/||m_{-j}||^2`.                    (2.6)

Hence, with `E0=sum_j sum_{k!=j}e_jk^2`,

`E0 <= (4/M^2) sum_j Delta_j^2`.                                  (2.7)

Symmetry of H implies, on the support of m and with `beta_j=alpha_j/m_j`,

`m_j m_k (beta_j-beta_k)=e_kj-e_jk`.                              (2.8)

The weighted variance identity therefore gives a scalar `theta` satisfying

`sum_{j:m_j!=0} m_j^2(beta_j-theta)^2 <= 2E0/M^2`.               (2.9)

Zero entries of m are handled directly from symmetry as in the B19 checkpoint.  Combining (2.5), (2.9), and `(x+y)^2<=2x^2+2y^2` yields

`||Off(H-theta m m^T)||_F^2 <= 8E0
 <= (32/M^2) sum_j Delta_j^2`.                                   (2.10)

This is the quantitative stable-alignment inequality, now at the concrete collar scale.

## 3. New deterministic compiler: either a large adjusted diagonal or fixed two-gradient energy

Define the rank-at-most-two matrix

`L = [[0,m^T],[m,theta m m^T]]`,                                  (3.1)

and the diagonal matrix

`D_* = diag(a, H_jj-theta m_j^2 : j in J)`.                       (3.2)

Let `E_*` have zero hub row and column and residual block

`Off(H-theta m m^T)`.

Then exactly

`A = L + D_* + E_*`,                                              (3.3)

and `rank(L)<=2` because its range is contained in the span of the hub basis vector and `[0;m]`.

Since this is the exact-rank-three collar and all three nonzero singular values have size at least one,

`dist_op(A,{rank<=2})=s_3(A)>=1`.                                 (3.4)

Taking the particular rank-two competitor L gives

`||D_*+E_*||_op>=1`.                                              (3.5)

Therefore one of the following must hold:

1. `||D_*||_op>1/2`; or
2. `||E_*||_op>=1/2`.

In the second case, (2.10) gives

`1/4 <= ||E_*||_op^2 <= ||E_*||_F^2
 <= (32/M^2) sum_j Delta_j^2`,

hence

`sum_j Delta_j^2 >= M^2/128
 > 1023/524288`.                                                   (3.6)

This proves the new structural statement

### Theorem 3.1 — `QFORM-COLLAR-STABLE-ALIGNMENT-COMPILER-v1`

In the nondominant-star collar (2.4), either

`boxed(||D_*||_op>1/2)`                                          (3.7)

or

`boxed(sum_j Delta_j^2>1023/524288)`.                             (3.8)

The conclusion is dimension-free and is an aggregate statement; no individual `Delta_j` is selected.

## 4. Product-preserving cut compiler and a paid continuous-density exit

Assume the aggregate alternative (3.8).  Independently assign every residual original coordinate to sets `J_1,J_2` with probability `1/2`.  For every summand in (2.3), the event

`j in J_1,  k,l in J_2`

has probability `1/8`.  Thus some deterministic physical partition satisfies

`sum_{j in J_1} sum_{k<l in J_2}
 (m_k H_jl-m_l H_jk)^2
 > 1023/4194304`.                                                 (4.1)

Take the actual original-coordinate cross block

`B=A[{i} union J_1, J_2]`.                                       (4.2)

Every term in (4.1) is the square of a physical `2x2` minor of B.  Cauchy--Binet therefore gives

`Delta_2(B):=e_2(BB^T)>1023/4194304`.                             (4.3)

Because A has exact rank three, `rank(B)<=3`.

Now suppose this captured B additionally satisfies the two quantitative gates

`s_3(B)>=1/64`,                                                   (4.4)

`max_r (P_range(B))_rr <=1/2`.                                   (4.5)

The volume-marginal matrix W from the completed q=4/3 three-volume theorem obeys `0<=W<=P_range(B)`, so every row inclusion marginal is at most `1/2<2/3`; hence that theorem applies.

Let the three nonzero squared singular values of B be

`lambda_1>=lambda_2>=lambda_3>0`.

Since rank(B)<=3,

`Delta_2(B)
 =lambda_1 lambda_2+lambda_1 lambda_3+lambda_2 lambda_3
 <=3 lambda_1 lambda_2`,                                         (4.6)

while (4.4) gives

`lambda_3>=1/4096`.                                               (4.7)

Thus the third-volume satisfies

`Z=lambda_1 lambda_2 lambda_3
 >= [Delta_2(B)/3](1/4096)
 > (1023/4194304)/(3*4096)`.                                     (4.8)

The q=4/3 theorem gives a **continuous** density with

`||p_Q||_infinity
 <= (9 sqrt(3)e/2) Z^(-1/6)
 < 408`.                                                          (4.9)

The numerical constant is only a convenience; the exact universal expression in (4.9) is the theorem.

### Corollary 4.1 — `QFORM-COLLAR-DIFFUSE-THIRD-VOLUME-EXIT-v1`

In the stable-alignment aggregate branch, every cut satisfying (4.4)-(4.5) is completely paid with a continuous density `<408`.  Hence any still-unpaid nondominant-star state with `||D_*||op<=1/2` must force, for every aggregate-energy cut supplied above, at least one of

`s_3(B)<1/64` or `max_r(P_range(B))_rr>1/2`.                      (4.10)

This is the precise low-cross-rank / localized-leverage residue of the current stability problem.

## 5. Designated account04/B20 result applied at an actual collar inequality

The collar hub is itself a selected-frame row `u_i` with leverage `c_i=||u_i||^2>1/4`.  Consider the subbranch

`c_i<=3/4`.                                                       (5.1)

Condition only the ORIGINAL hub coordinate `X_i`.  In the exact rank-three frame the residual Gram is

`S=I-u_i u_i^T`,                                                  (5.2)

so

`delta=lambda_min(S)=1-c_i>=1/4`.                                (5.3)

If every residual original row satisfies the exact whitened-leverage gate

`u_j^T S^(-1)u_j <=1/32`,                                        (5.4)

then account04/B20 r2 applies directly and gives a continuous density with

`||p_Q||_infinity <27/delta <=108`.                              (5.5)

This is the required equation-level partner application; no partner hypothesis is extended beyond its proved scope.

If (5.4) fails, choose j with `u_j^T S^(-1)u_j>1/32`.  Since `S^(-1)<=delta^(-1)I`,

`c_j=||u_j||^2>delta/32>=1/128`.                                 (5.6)

For the exact-rank-three core `A=UMU^T` with `s_min(M)>=1`,

`sum_k A_jk^2=u_j^T M^2u_j>=c_j>1/128`.                          (5.7)

Thus either `|A_jj|>=1/32`, in which case the completed exact-rank-three scalar-pivot theorem gives

`||p_Q||_infinity
 <128[(1/128)(1/32)]^(-1/4)=1024`,                               (5.8)

or

`||A[j,-j]||_2^2
 >1/128-1/1024
 =7/1024`.                                                        (5.9)

The latter is a second fixed-strength physical star.  Applying the completed heavy-hub compound-energy theorem to this row gives an aggregate second-gradient packet: either its one-overlap energy is `>7/2048`, or its fully disjoint energy is `>7/2048`; in the disjoint case a physical random cut captures

`Delta_2>7/16384`.                                                (5.10)

Therefore the designated-partner split sharpens the live collar as follows:

- if `1/4<c_i<=3/4`, either the collar is paid continuously by `<108`, or a second physical row carries a fixed scalar-pivot or compound-energy resource;
- the only collar states not reached by this conditioning step are the near-coloop side `c_i>3/4` and the explicit nondiffuse residual alternatives just described.

## 6. What this closes and the exact next debt

The freshest B19 task asked for quantitative stability of the failure of all two-physical-gradient areas.  The present run proves and applies the first needed implication in that route:

1. away from a single `3/4`-dominant star atom, failure of exact rank-one alignment is not qualitative: if the aligned diagonal remainder is at most `1/2`, then the total physical two-gradient energy is at least `1023/524288`;
2. a deterministic original-coordinate cut captures `Delta_2>1023/4194304` before any reciprocal local coefficient is selected;
3. if this cut has a diffuse rank-three cross range at scale `1/64`, the full target law is paid continuously by `<408`;
4. independently, conditioning the current hub pays every `c_i<=3/4` state satisfying the partner's exact whitened-diffuse criterion by `<108`; failure forces a second quantitative physical resource.

The first unpaid implication is now narrower:

`QFORM-COLLAR-ALIGNED-DIAGONAL-OR-LOWRANK-LOCALIZED-PAYMENT-v1`:

> pay the surviving collar when either the adjusted diagonal `D_*` has operator norm `>1/2`, or every aggregate-energy cut is forced into `s_3<1/64` / row-leverage `>1/2`; separately splice the `3/4`-dominant star atom and near-coloop `c_i>3/4` endpoints into the already-developed pair/bank mechanisms.  The proof must continue to aggregate before taking reciprocals and must preserve original-coordinate product provenance.

The exact all-areas-zero endpoint remains paid by B19 r25's finite-line compression (`K<=7`); the present theorem supplies a positive-distance quantitative route away from that endpoint.

## 7. Correction boundary and full-target status

No statement here uses bounded density of a rotated projection as a substitute for product provenance.  The q=4/3 volume theorem is invoked only on an actual original-coordinate cross block and is itself product-preserving.  The account04/B20 conditioning is only on original coordinates.  The new deterministic stable-alignment compiler is matrix algebra.

The unrestricted conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**.  No new counterexample is produced.  The full continuous-density conclusion remains open; continuity is proved in the paid volume branch (4.9) and the conditioned-whitened branch (5.5), but not in the remaining collar or in the unrestricted target.
