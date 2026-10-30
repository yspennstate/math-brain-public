SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B04, 2026-09-24T09:47:46Z.
attacking: exact optimization of the zero-self random-slope pair compiler, then package the result as an aggregate Schur-numerator row certificate on the low-tetrad clique boundary.

# fleet01/B04 r34 — exact zero-self optimizer and Schur-numerator row certificate

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Product Fourier rearrangement  
Status: **NEW CLOSED-FORM OPTIMIZATION + NEW SCHUR-NUMERATOR COROLLARY / FULL QFORM OPEN**  
Regularity: essential boundedness only in this branch; continuity is **not** proved here.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source boundary and mechanism change

Fresh owner control on `yspennstate/math-research-brain/main` remains revision `2026-09-22.15`, QFORM-only. The unrestricted theorem remains open.

I initially tried to prove a zero-self Schur-row random-slope theorem from scratch. A source search found that the analytic mechanism itself is already completed in fleet02/B14 r33:

- repository/commit: `yspennstate/math-open-problems@9c77bae76f0d884fc60a2ffee86ad6269b79d690`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B14/20260923T095834Z-fleet02-B14-QFORM-r33/REPORT.md`;
- result: `QFORM-RANDOM-SLOPE-MASS-HOMOGENEITY-v1`.

Accordingly I do **not** claim the random-slope compiler as new. I changed the mechanism target to the first unpaid algebraic/optimization step: evaluate its one-parameter infimum exactly, then rewrite the optimized certificate in the Schur-numerator variables used by the current B04 low-tetrad funnel. The source search did not find this closed form or the determinant-free row-energy corollary.

I also use the standard sharp one-dimensional product-projection estimate recorded in the completed B04 sources: if `a!=0` and `Y` has independent cap-one coordinates, then

`||p_(a^T Y)||_infinity <= sqrt(2)/||a||_2.`                         (1.1)

The designated fleet02/B04 partner result actually applied below is r21:

- repository/commit: `yspennstate/math-open-problems@bb6e1a7e2e46a3434649dfd1b6a4afe94d25e7fa`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/9a73ca69-5439-45c6-9b34-581521e6e6a2/REPORT.md`.

That report classifies the exact zero-disjoint-tetrad clique family and proves that every physical crossing has rank at most two; it also demonstrates the localized principal-triple receiver on the same family.

No pointwise law-uniform quadratic Fourier decay, post-rotation independence, arbitrary-joint coarea, moments, support radius, connected support, Gaussianity, or perturbative deletion of a small random quadratic term is used below.

## 2. Input compiler from fleet02/B14 r33

Let an outer pair of **original** independent coordinates have invertible indefinite symmetric block `B`. Put

`D=|det B|`, `kappa=sigma_min(B)>0`.                                (2.1)

After exact completion of this physical pair, suppose a remaining original coordinate `X` is an exact zero-self hub and the residual has the form

`Y = X S(V)+R(V)`,                                                  (2.2)

where `X` is independent of the bank `V`, `p_X<=1`, `R` is arbitrary and may be maximally correlated with `S`, and the scalar slope `S(V)` has density cap `H`.

Fleet02/B14 r33 proves

`||p_Q||_infinity`
` <= inf_(z>0) [ 8 sqrt(H/(kappa z)) + D^(-1/2) Omega_0(z) ],`       (2.3)

where

`Omega_0(z)=z[2+log(1/z)]`, `0<z<=1`,
`Omega_0(z)=log z+2`,       `z>=1`.                                 (2.4)

The rest of this report starts from the already-proved formula (2.3).

## 3. Exact optimization

Define the dimensionless parameter

`rho = 8 sqrt(D H/kappa)`.                                          (3.1)

Factoring `D^(-1/2)` in (2.3) gives

`||p_Q||_infinity <= D^(-1/2) Phi(rho)`,                            (3.2)

with

`Phi(rho)=inf_(z>0) [rho z^(-1/2)+Omega_0(z)].`                    (3.3)

### Theorem 3.1 — `QFORM-ZEROSELF-RANDOM-SLOPE-EXACT-OPTIMIZER-v1`

For every `rho>0`,

`boxed:`
`Phi(rho)=`
`  exp(-y)(4+3y),                         0<rho<=2,`
`  4+2 log(rho/2),                        rho>=2,`                   (3.4)

where for `0<rho<=2`, `y=y(rho)>=0` is the unique solution of

`rho = 2(1+y) exp(-3y/2).`                                         (3.5)

Equivalently,

`y(rho)=-1-(2/3) W_(-1)( -(3rho/4) exp(-3/2) ).`                   (3.6)

Here `W_(-1)` is the lower real Lambert branch.

### Proof

For `z>=1`, differentiate

`rho z^(-1/2)+log z+2`.

The critical equation is

`sqrt(z)=rho/2`.                                                     (3.7)

It lies in the branch exactly when `rho>=2`. Substitution gives

`Phi(rho)=4+2 log(rho/2)`.                                         (3.8)

For `0<z<=1`, differentiate

`rho z^(-1/2)+z[2-log z]`.

The critical equation is

`rho =2 z^(3/2)[1-log z].`                                         (3.9)

Writing `y=-log z>=0` yields (3.5). The function

`2(1+y)e^(-3y/2)`

is strictly decreasing from `2` to `0`, so the solution is unique for `0<rho<=2`. Since the objective tends to infinity as `z downarrow0`, and its derivative at `z=1` has sign `1-rho/2`, this critical point is the global minimum. At it,

`rho z^(-1/2)=2z(1+y)`,
`Omega_0(z)=z(2+y)`,

hence

`Phi(rho)=z(4+3y)=e^(-y)(4+3y)`.                                   (3.10)

At `rho=2`, both branches give `4`. Equation (3.6) is the direct Lambert inversion of (3.5). QED.

This is an exact evaluation of the already-proved r33 variational certificate; it is not a new proof of the underlying random-slope theorem.

## 4. A scale-homogeneous fourth-root envelope

The exact optimizer also has a useful elementary envelope. For every `z>0`,

`boxed: Omega_0(z) <= 2 sqrt(z).`                                  (4.1)

Indeed, write `t=|log z|>=0`. In either branch,

`Omega_0(z)/sqrt(z) = e^(-t/2)(2+t) <=2`,                          (4.2)

because the derivative in `t` is `-(t/2)e^(-t/2)`.

Using (4.1) in (2.3) and optimizing `A/x+Bx` with `x=sqrt(z)` gives

`boxed:`
`||p_Q||_infinity <= 8 [ H/(D kappa) ]^(1/4).`                    (4.3)

This is weaker than the exact function (3.4), but it is closed-form, scale homogeneous, and uniformly no larger than the earlier displayed choice `z=1` in r33 by AM-GM.

## 5. Schur-numerator row certificate

Now start from an arbitrary real symmetric physical matrix, isolate an invertible indefinite physical pair `H`, and write

`A = [[B,C^T],[C,D_0]],`
`S = D_0-CB^(-1)C^T,`
`N_H = det(B) S.`                                                   (5.1)

Let `i` be a remaining **original coordinate** such that

`(N_H)_(ii)=0`,
`R_i := ||(N_H)_(i,K\{i})||_2 >0.`                                 (5.2)

Since `det(B)!=0`, this is exactly `S_ii=0`. If `a` denotes the off-diagonal row of `S` at `i`, then

`||a||_2=R_i/D`.                                                    (5.3)

Including arbitrary conditioning-generated affine terms, the residual polynomial has the exact form

`X_i [ beta + 2 a^T X_(K\{i}) ] + R_0(X_(K\{i})).`                (5.4)

No term is dropped. The bank variables in (5.4) are the remaining original independent coordinates. By (1.1), the slope has density cap

`H_i <= 1/(sqrt(2)||a||_2)=D/(sqrt(2)R_i).`                        (5.5)

The function `Phi` is increasing in `rho` because it is the infimum over `z` of functions increasing in `rho`. Therefore Theorem 3.1 gives the following.

### Theorem 5.1 — `QFORM-SCHUR-NUMERATOR-ZERODIAG-ROW-v1`

Under (5.1)-(5.2), with

`rho_i = 2^(11/4) D / sqrt(kappa R_i),`                             (5.6)

one has

`boxed:`
`||p_Q||_infinity <= D^(-1/2) Phi(rho_i).`                         (5.7)

In particular, the determinant cancels completely from the simpler fourth-root form:

`boxed:`
`||p_Q||_infinity`
` <= 2^(23/8) [ kappa R_i ]^(-1/4).`                               (5.8)

The entire physical Schur-numerator row is aggregated before inversion. A single entry may tend to zero while `R_i` stays fixed.

The theorem is exact-zero in the self coefficient. It does **not** treat a small nonzero `(N_H)_(ii)` as a perturbation. The live correction corpus makes that distinction essential under unbounded inputs.

Continuity is not claimed. The source compiler and the present argument prove essential boundedness.

## 6. Genuinely rotated indefinite zero-tetrad clique example

Use the completed fleet02/B04 r21 clique family, but choose the exact zero-Schur-diagonal member

`B=[[3,1],[1,-3]],`
`u=(1,1,1,1)^T,`
`v=(1/10,1/5)^T,`
`d=-2, tau=2,`
`S=d I_4+tau u u^T=2(J_4-I_4),`
`C=u v^T,`
`D_0=S+C B^(-1) C^T.`                                             (6.1)

Since

`B^(-1)=B/10`,
`v^T B^(-1)v=-1/200`,                                              (6.2)

we get

`D_0=-2I_4+(399/200)J_4`.                                         (6.3)

Thus the full six-coordinate matrix is

`A_dagger =`
`[[3,1,1/10,1/10,1/10,1/10],`
` [1,-3,1/5,1/5,1/5,1/5],`
` [1/10,1/5,-1/200,399/200,399/200,399/200],`
` [1/10,1/5,399/200,-1/200,399/200,399/200],`
` [1/10,1/5,399/200,399/200,-1/200,399/200],`
` [1/10,1/5,399/200,399/200,399/200,-1/200]].`                    (6.4)

Every physical entry is nonzero. The matrix is therefore genuinely non-diagonal in the independent coordinates.

### Target check

Let `A_0=diag(B,S)`. Its spectrum is

`{-sqrt(10), -2,-2,-2, sqrt(10), 6}.`                              (6.5)

Moreover

`||C||_op=1/sqrt(5)`,
`||CB^(-1)C^T||_op=1/50`,                                         (6.6)

so

`||A_dagger-A_0||_op <= 1/sqrt(5)+1/50 <0.468.`                    (6.7)

Weyl therefore gives

`min_j |lambda_j(A_dagger)| > 2-0.468 >1.53.`                      (6.8)

Hence all six eigenvalues have modulus greater than one. This is strongly inside the owner's exact target.

### Partner r21 structure actually applied

For this member of the partner family,

`tau+v^T B^(-1)v =399/200 !=0.`                                    (6.9)

Therefore the completed fleet02/B04 r21 classification applies: `A_dagger` is diagonal plus one signed rank-one matrix plus the single physical edge `12`, and hence

`rank A_dagger[I,J] <=2`

for every disjoint physical cut `I,J`. In particular every physical `E_3` crossing currency is exactly zero. This example is therefore on the partner's genuine zero-tetrad / cross-volume blind spot, not an easy positive-`E_3` case.

The pair Schur numerator is

`N_H=det(B)S=-20(J_4-I_4).`                                        (6.10)

Thus every residual Schur diagonal is zero and every row has aggregate off-diagonal norm

`R_i=20 sqrt(3).`                                                   (6.11)

For `D=10` and `kappa=sqrt(10)`, (5.6) gives

`rho_i`
` = 8 sqrt( 5/(2 sqrt(15)) )`
` = 6.4274273515572138365... >2.`                                  (6.12)

The exact high-`rho` branch of (5.7) therefore yields

`boxed:`
`||p_(X^T A_dagger X)||_infinity`
` <= (1/sqrt(10)) [4+2 log(rho_i/2)]`
` = 2.0032568402692141275... .`                                    (6.13)

The simpler determinant-free form (5.8) gives

`2.2675850328589159810...`.                                        (6.14)

### Same-matrix partner inequality

The partner r21 localized principal-triple endpoint also applies directly. On physical residual coordinates `{3,4,5}`, the principal block is

`-2I_3+(399/200)J_3`,                                              (6.15)

with eigenvalues

`-2,-2,797/200.`                                                    (6.16)

The exact principal-block theorem used in r21 therefore gives

`boxed: ||p_(X^T A_dagger X)||_infinity <= 3 sqrt(pi)`
`       =5.3173615527165480819... .`                               (6.17)

Thus on the same target-valid, fully dense, all-cross-rank-at-most-two matrix, the optimized zero-self product-rearrangement certificate improves the displayed partner principal-triple certificate by a factor

`2.654358365751022...`.                                             (6.18)

This comparison is scoped to this matrix; it is not a claim that the present receiver globally subsumes the partner's principal-curvature mechanism.

## 7. What remains

The new row certificate pays an exact zero-diagonal Schur-numerator clique row at aggregate scale. It does not solve the quantitative low-tetrad stability problem, because a near-clique can have a small but nonzero Schur self coefficient and that coefficient cannot be deleted perturbatively under arbitrary unbounded inputs.

The first successor suggested by this run is

`QFORM-LOW-TETRAD-EXACTZERO-ROW-OR-ARBITRARYSELF-ROUTING-v1`:

> In the current low-disjoint-tetrad Schur-numerator chamber, force either (i) one exact/structurally forced zero-self row with target-scale aggregate row energy, so (5.7) applies; (ii) a target-scale arbitrary-self random-slope row paid by the already-completed fleet02/B14 r34 compiler; or (iii) the partner's principal-curvature / grouped-square / fixed-pair / renewed-volume exits. The difficult step is quantitative stability without replacing a small nonzero self coefficient by zero.

The unrestricted three-large-eigenvalue conjecture remains **OPEN**. Full-target continuity remains **OPEN**.

## 8. Integrity

No scheduler/task identity/cadence state, notification/email setting, public visibility, permission, paid model/API, cross-account authentication, installation, FEI work, or unrelated data was changed. Repository usage and native brain ingestion remain distinct; execution status is `WITHOUT_VERIFIED_BRAIN`.
