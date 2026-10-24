SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B08, 2026-09-23T15:19:01Z.
attacking: localized-triangle plus second-arm receiver with arbitrary curvature; seek a product-preserving physical-coordinate reduction that complements diffuse multihub estimates.

# account03/B08 r39 — Pluecker-cut diffuse Schur receiver and near-rank-three volume bridge

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T151901Z-account03-B08-qform-diffuse-r39`  
Owner control refreshed before publication: `yspennstate/math-research-brain@a3aba1241783fd49b15577902e851180b7af9102`, OWNER CONTROL revision `2026-09-22.15`  
Assignment: diffuse eigenvector case / quantitative inequalities and rigorous computations  
Status: `NEW SUPPORTING TARGET-LEVEL IMPLICATIONS / FULL TARGET OPEN / INDEPENDENT REVIEW PENDING`  
Execution: `WITHOUT_VERIFIED_BRAIN`

The unrestricted conjecture remains OPEN. Global continuity remains OPEN. The input assumptions are exactly the owner target: independent real coordinates with one-dimensional density caps at one; no Gaussianity, moments, compactness, log-concavity, identical laws, or spectral-coordinate independence. Every cut below is in ORIGINAL coordinates.

The main new point is a product-preserving bridge from a *diffuse low-rank scalar Schur residual* to the already-completed aggregate `E_2` receiver. The bridge is deterministic and dimension-free. It does not choose one reciprocal minor. A second theorem applies the newest required `c2414...` volume-stability result to a near-rank-three Schur residual after an original-coordinate random cut. Together they remove two genuinely diffuse low-rank leakage states left by r38.

## 1. Sources used at equations

1. Immediate B08 predecessor:  
   `yspennstate/math-open-problems@1a70497363989dfea9fa4ce9e515fa279677df69`  
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260923T131815Z-account03-B08-qform-diffuse-r38/REPORT.md`.  
   It routes scalar-Schur cancellation of an anisotropic physical core into a localized physical triangle and leaves the aligned/high-leverage low-rank receiver as an explicit debt.

2. Aggregate scalar-Schur `E_2` receiver:  
   `yspennstate/math-open-problems@2cb64b71f8aafa0892547dffebcf6af647ea7c64`  
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260923T102108Z-account03-B08-qform-diffuse-r32/REPORT.md`.  
   If a genuine original scalar pivot has coefficient `a!=0` and its exact Schur residual contains an ORIGINAL-coordinate cross block `M` with `E_2(M)>0`, then

   `||p_Q||_infinity < C_E2 |a|^(-1/2) E_2(M)^(-1/8)`,

   where

   `C_E2 = 36.44334493792993...`.                              (1.1)

   Arbitrary residual self-curvature and unused couplings are retained. Continuity is not asserted by this route.

3. Newest required volume-stability result:  
   `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`  
   `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.  
   For a literal physical cross block `M=M0+E`, if `s3(M0)>=c`, the row-range projection of `M0` has diagonal at most `1/2`, and `||E||op<=c/16`, then the corresponding quadratic-affine form has a continuous `C_0` density bounded by

   `||p||_infinity < 23/c`.                                    (1.2)

   Arbitrary within-bank phases and outside couplings are retained.

4. Designated partner account04/B08:  
   `yspennstate/math-open-problems@abbec61f52e1f4b4d367fd67e73e4d2501ac9c74`  
   `proofnet24/QFORM-density/fleet-2026-09-22/account04/B08/20260923T091414Z-account04-B08-QFORM-r1/REPORT.md`.  
   For every `R>=3`, every `L>0`, and every admissible product input,

   `Q_(R,L)=L X_0^2+2LR U_1V_1+2L R^(-1)U_2V_2`

   satisfies

   `||p_(Q_(R,L))||_infinity < 7.251/L`.                        (1.3)

   This is used below as the localized control endpoint, not extrapolated beyond its stated scope.

The live corrections were reread before publication. In particular no pointwise Fresnel decay, post-rotation independence, arbitrary-joint coarea bound, one-heavy-row square absorption, or automatic pre/post-Schur `E_2` transfer is used.

## 2. A dependence-safe square lemma at the `L^infinity` endpoint

This elementary endpoint will be used only after a residual density has already been proved.

### Lemma 2.1

Let `R` be a real random variable with density `g` satisfying `||g||_infinity<=H`. Let `V` be another real variable such that, conditionally on `R=r`, the law of `V` has a density bounded by one. Then for every `a!=0`,

`T=R+aV^2`

has an essentially bounded density with

`||p_T||_infinity <= 2sqrt(2) |a|^(-1/2) H^(1/2)`.             (2.1)

### Proof

For fixed `r`, the density of `aV^2` is bounded by `|a|^(-1/2)y^(-1/2)` on its appropriate half-line. Hence for a.e. `t`, after orienting the half-line according to `sign(a)`,

`p_T(t) <= |a|^(-1/2) integral_0^infinity g(t-sign(a)u) u^(-1/2) du`.

For any `delta>0`, the part `0<u<delta` is at most `2H sqrt(delta)` and the far part is at most `delta^(-1/2)` because `g` has mass one. Choosing `delta=(2H)^(-1)` gives (2.1). QED.

For an original scalar Schur completion, `V=X_0+m(Z)` and `R=R(Z)`. Since `X_0` is independent of the residual original coordinates `Z`, conditioning on any value of `R(Z)` merely mixes translates of the cap-one density of `X_0`; therefore the required conditional cap remains one.

## 3. Exact rank-two Schur residual: a Pluecker random-cut theorem

Let

`A=[[a,b^T],[b,C]]`, `a!=0`,                                    (3.1)

where the first coordinate is an ORIGINAL independent coordinate, and define the exact scalar Schur residual

`S=C-bb^T/a`.                                                    (3.2)

Put

`A0=[[a,b^T],[b,bb^T/a]]`.                                      (3.3)

Then `rank(A0)=1` and

`A-A0=diag(0,S)`.                                                (3.4)

The singular-value rank-approximation principle therefore yields

`s_3(A) <= s_2(S)`.                                              (3.5)

Thus if the full target has `s_3(A)>=L`, then

`s_2(S)>=L`.                                                     (3.6)

Assume first that `rank(S)=2`. Write

`S=U Lambda U^T`, `U^T U=I_2`,                                  (3.7)

where `Lambda=diag(lambda_1,lambda_2)` contains the two signed nonzero eigenvalues. By (3.6),

`|lambda_1|,|lambda_2|>=L`.                                     (3.8)

For each original residual coordinate `i`, let

`ell_i=||U_{i,*}||_2^2`, `mu=max_i ell_i`.                       (3.9)

### Lemma 3.1 — Pluecker half-cut

If `mu<1/2`, there exists a partition of the residual ORIGINAL coordinates into `I,J` such that, with

`G_I=U_I^T U_I`, `G_J=U_J^T U_J`,                               (3.10)

one has

`det(G_I)det(G_J) >= (1-2mu)/16`.                               (3.11)

#### Proof

For `i<j`, define

`w_ij=det(U[{i,j},:])^2`.                                       (3.12)

Cauchy-Binet gives

`sum_(i<j) w_ij=1`.                                             (3.13)

For a fixed row `i`, the contraction identity gives

`sum_(j!=i) w_{min(i,j),max(i,j)}=ell_i`.                       (3.14)

Indeed

`sum_j det(u_i,u_j)^2
 =||u_i||^2 sum_j||u_j||^2 - sum_j <u_i,u_j>^2
 =2ell_i-ell_i=ell_i`,

because `sum_j u_j u_j^T=I_2`.

Now independently place every coordinate into `I` or `J` with probability `1/2`. Cauchy-Binet again gives

`det G_I=sum_{P subset I, |P|=2} w_P`,
`det G_J=sum_{Q subset J, |Q|=2} w_Q`.                          (3.15)

A pair `P` and pair `Q` can contribute simultaneously only when they are disjoint; then the probability is `1/16`. Hence

`E[det G_I det G_J]
 =(1/16) sum_(P cap Q=empty) w_Pw_Q`.                           (3.16)

The ordered mass of intersecting pair-pairs is at most

`sum_i (sum_(P contains i)w_P)^2
 =sum_i ell_i^2
 <=mu sum_i ell_i
 =2mu`.                                                          (3.17)

Since the total ordered mass is one, (3.16) is at least `(1-2mu)/16`. Therefore some deterministic partition satisfies (3.11). QED.

### Lemma 3.2 — exact second-volume identity

For the physical cross block

`M=S[I,J]=U_I Lambda U_J^T`,                                    (3.18)

one has

`E_2(M)=lambda_1^2 lambda_2^2 det(G_I)det(G_J)`.                (3.19)

This follows by expanding every physical `2x2` minor:

`det M[R,T]=det(U_R) det(Lambda) det(U_T)`

for `R subset I`, `T subset J`, `|R|=|T|=2`, and summing squares with Cauchy-Binet.

Combining (3.8), (3.11), and (3.19),

`E_2(M) >= (1-2mu)L^4/16`.                                     (3.20)

### Theorem 3.3 — exact rank-two diffuse Schur receiver

Under (3.1)-(3.9), if `rank(S)=2` and `mu<1/2`, then

`||p_Q||_infinity
 < C_E2 [16/(1-2mu)]^(1/8) |a|^(-1/2)L^(-1/2)`.               (3.21)

If in addition `|a|>=tau L`,

`boxed:
 ||p_Q||_infinity
 < C_E2 [16/(1-2mu)]^(1/8) tau^(-1/2)L^(-1).
`                                                                    (3.22)

At the convenient diffuse threshold `mu<=1/4`,

`boxed:
 ||p_Q||_infinity < 56.204 tau^(-1/2)L^(-1).
`                                                                    (3.23)

This is essential boundedness. Continuity is not asserted.

The exact-rank-two theorem is genuinely aggregate: no single physical minor is selected. A very anisotropic rank-two residual is permitted; only the *spectral frame leverage* is required to be diffuse.

## 4. Near-rank-two residual: a robust physical-cut receiver

The exact identity above can be made perturbation-stable without ever claiming that a pre-Schur minor survives the Schur update.

Let `S0` be the top-two spectral truncation of `S`, with orthonormal frame `U` and leverage `mu=max_i||U_{i,*}||^2`. Write

`S=S0+E`, `||E||op=s_3(S)`.                                     (4.1)

Assume

`mu<=1/8`.                                                       (4.2)

For a random half-partition, put again `G_I=U_I^TU_I`. Since

`G_I-(1/2)I_2=(1/2)sum_i eps_i u_i u_i^T`,                     (4.3)

independence of the signs gives

`E ||G_I-(1/2)I_2||_F^2
 =(1/4)sum_i ||u_i u_i^T||_F^2
 =(1/4)sum_i ell_i^2
 <=mu/2
 <=1/16`.                                                       (4.4)

Hence some partition obeys

`||G_I-(1/2)I_2||op<=1/4`,                                     (4.5)

and therefore

`G_I >=(1/4)I_2`, `G_J>= (1/4)I_2`.                            (4.6)

The reference cross block

`M0=S0[I,J]`                                                     (4.7)

then satisfies

`s_2(M0)>= (1/4)s_2(S)>=L/4`.                                  (4.8)

The actual post-Schur cross block is

`M=S[I,J]=M0+E[I,J]`,                                           (4.9)

and a coordinate submatrix cannot have larger operator norm than the full matrix, so

`||E[I,J]||op<=s_3(S)`.                                         (4.10)

If

`s_3(S)<=eta L`, `0<=eta<1/4`,                                 (4.11)

Weyl gives

`s_2(M)>=(1/4-eta)L`.                                           (4.12)

Consequently

`E_2(M)>=s_1(M)^2s_2(M)^2>=s_2(M)^4
 >=(1/4-eta)^4 L^4`.                                           (4.13)

Applying (1.1) proves:

### Theorem 4.1 — near-rank-two diffuse Schur receiver

If the full matrix has `s_3(A)>=L`, an ORIGINAL scalar pivot satisfies `|a|>=tau L`, the exact scalar Schur residual has

`max_i leverage_i(top-two eigenspace)<=1/8`,

and

`s_3(S)<=eta L< L/4`,

then

`boxed:
 ||p_Q||_infinity
 < C_E2 tau^(-1/2)(1/4-eta)^(-1/2)L^(-1).
`                                                                    (4.14)

At `eta=1/15`,

`boxed:
 ||p_Q||_infinity <85.114 tau^(-1/2)L^(-1).
`                                                                    (4.15)

Thus the low-third-singular-value Schur leakage state is completely paid whenever its leading two-dimensional residual eigenspace is genuinely diffuse. Failure of this branch forces either a small/zero physical pivot, a residual third singular value above the chosen threshold, or top-two leverage above `1/8` on an actual original residual coordinate.

## 5. Apply the newest `c2414...` theorem to the near-rank-three Schur branch

This section is the required equation-level application of the newest volume-stability result.

Assume now that the Schur residual has three substantial singular directions. Let `S0` be its top-three spectral truncation,

`S0=U Lambda U^T`, `U^TU=I_3`,                                 (5.1)

and suppose the top-three row leverage obeys

`mu_3=max_i ||U_{i,*}||^2 <=1/16`.                              (5.2)

For a random half-partition,

`G_I-(1/2)I_3=(1/2)sum_i eps_i u_i u_i^T`,

and

`E||G_I-(1/2)I_3||_F^2
 =(1/4)sum_i ell_i^2
 <=(3mu_3)/4`.                                                  (5.3)

Therefore some partition has

`||G_I-(1/2)I_3||op <= sqrt(3mu_3/4) <=sqrt(3)/8`.              (5.4)

Define

`g_3=1/2-sqrt(3)/8=(4-sqrt(3))/8
   =0.283493649053890...`.                                      (5.5)

Then

`G_I>=g_3 I_3`, `G_J>=g_3 I_3`.                                (5.6)

The reference cross block

`M0=S0[I,J]=U_I Lambda U_J^T`                                  (5.7)

has

`s_3(M0)>=g_3 s_3(S)`.                                         (5.8)

Its row range equals `range(U_I)`, whose physical-coordinate projection has diagonal

`u_i^T G_I^(-1)u_i <= ell_i/g_3 <= (1/16)/g_3 <1/2`.          (5.9)

Let the remaining spectral tail be `E=S-S0`. If

`s_4(S)=||E||op <= g_3 s_3(S)/16`,                             (5.10)

then the actual physical cross block `M=S[I,J]` satisfies

`||M-M0||op<=g_3s_3(S)/16`.                                    (5.11)

All hypotheses of `QFORM-THREEVOLUME-STABILITY-v1` at `c2414...` now hold with

`c=g_3s_3(S)`.                                                  (5.12)

Hence the residual quadratic-affine variable `R(Z)` has a continuous `C_0` density satisfying

`||p_R||_infinity <23/[g_3s_3(S)]`.                             (5.13)

Now reinsert the original scalar square using Lemma 2.1. If

`|a|>=tau L`, `s_3(S)>=beta L`,                                (5.14)

then

`||p_Q||_infinity
 <2sqrt(2)(tau L)^(-1/2)
   [23/(g_3 beta L)]^(1/2)`

and therefore

`boxed:
 ||p_Q||_infinity
 < 2sqrt(46/g_3) tau^(-1/2) beta^(-1/2)L^(-1)
 <25.477 tau^(-1/2) beta^(-1/2)L^(-1).
`                                                                    (5.15)

This proves `QFORM-DIFFUSE-NEARRANK3-SCHUR-VOLUME-v1` in its stated scope. The residual density in (5.13) is continuous `C_0`; continuity of the final output in (5.15) is **not** asserted because the scalar pivot input density itself is only assumed measurable and bounded.

This application is correction-safe. The volume theorem is applied to a literal original-coordinate cross block of the exact Schur residual polynomial; the scalar square is reintroduced by the dependence-safe kernel bound. No small coefficient is deleted as a small random variable.

## 6. Designated partner result applied to the complementary localized endpoint

The designated account04/B08 family, scaled by `L`, is

`Q_(R,L)=L X_0^2+2LR U_1V_1+2L R^(-1)U_2V_2`, `R>=3`.          (6.1)

The partner theorem gives the actual target inequality

`boxed: ||p_(Q_(R,L))||_infinity<7.251/L.`                      (6.2)

For this family the scalar Schur residual after the `X_0` pivot is the hyperbolic direct sum with eigenvalues `+LR,-LR,+L/R,-L/R`. Its top-two eigenspace is exactly the physical span of `U_1,V_1`; hence its maximum original-coordinate leverage is one. Therefore the new diffuse gates (4.2) and (5.2) correctly reject this maximally localized endpoint, while the completed partner theorem pays it directly.

This is the intended complementarity: the present run pays low-rank Schur geometry when its spectral frame is spread across original coordinates; the designated partner pays a sharp grouped endpoint when the same kind of two-arm currency is concentrated on a few original coordinates. No partner statement is extrapolated to the arbitrary-leakage case.

## 7. What changed in the r38 proof map

The r38 survivor after scalar-Schur cancellation was described as an aligned/high-leverage low-rank state. The present run splits that state more sharply.

With a quantitative original scalar pivot `|a|>=tau L` and `s_3(A)>=L`:

1. **Exact rank-two Schur residual, diffuse frame:** paid by Theorem 3.3 for every `mu<1/2`; at `mu<=1/4`, bound `<56.204 tau^(-1/2)/L`.
2. **Near-rank-two Schur residual, diffuse frame:** if top-two leverage `<=1/8` and `s_3(S)<=L/15`, paid by Theorem 4.1 with `<85.114 tau^(-1/2)/L`.
3. **Near-rank-three Schur residual, strongly diffuse frame:** if top-three leverage `<=1/16`, `s_3(S)>=beta L`, and `s_4(S)<=g_3s_3(S)/16`, the newest `c2414...` result plus Lemma 2.1 gives `<25.477 tau^(-1/2)beta^(-1/2)/L`.
4. **Maximally localized two-arm direct sum:** the designated account04/B08 theorem gives `<7.251/L` on its exact scope.

Thus the low-rank leakage obstruction is no longer a single undifferentiated state. The remaining B08 debt is concentrated in:

- small or zero physical scalar pivots;
- high original-coordinate leverage in the leading Schur eigenspaces outside already-paid localized grouped models;
- the middle/high-tail regime where `s_3(S)` is substantial but the fourth and further singular directions are not a small perturbation of a diffuse rank-three frame;
- arbitrary localized triangle plus extra couplings when no completed physical-pair/grouped theorem applies.

Those cases require a grouped-coordinate or ridge/collective-tail reduction; they are not solved here.

## 8. Checks

`CHECKS.py` and `CHECKS.txt` in this run directory test the two exact matrix identities and the cut constants. The deterministic seeded suite checked:

- 400 random rank-two frames, exhaustive physical half-cuts: zero violations of (3.11);
- exact `E_2=lambda_1^2lambda_2^2 det(G_I)det(G_J)` to maximum absolute numerical error `8.33e-16`;
- 400 random rank-two/rank-three frames, exhaustive cuts: zero violations of the Frobenius-balancing existence bound;
- constants:
  - `56.203321077351` for (3.23),
  - `85.113316667678` for (4.15),
  - `g_3=0.283493649054`,
  - `25.476352215552` for (5.15) at `beta=tau=1`.

The checker terminates `QFORM_B08_R39_CHECK_PASS`. These finite tests are regression checks only; the proofs above are analytic.

## 9. Scope and status

The unrestricted theorem is **OPEN**. No counterexample to the owner target was found. Essential boundedness is proved in the branches (3.22), (4.14), and (5.15). The residual variable in the `c2414...` branch has a continuous `C_0` density, but continuity of the final scalar-square-reinserted output is not proved under arbitrary cap-one pivot laws.

Repository use occurred. Verified native brain retrieval/receiver use did not occur, so status remains `WITHOUT_VERIFIED_BRAIN`.
