SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B09, 2026-09-24T05:44:43Z.
attacking: the fixed-literal-hub one-overlap packet in the singular-pair survivor, by an exact rank-one leaf-curvature Plucker factorization and whole-bank one-hub smoothing before any reciprocal minor is paid.

# account01/B09 r31 — fixed-hub rank-one Omega1 Plucker compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **NEW SUPPORTING THEOREM / ESSENTIAL STEP APPLIED / FULL QFORM OPEN**  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains OPEN / not proved / not disproved. Full-target continuity remains OPEN separately. No Gaussian, moment, compact-support, connected-support, log-concavity, iid, post-rotation independence, law-uniform pointwise quadratic-phase decay, worst-fiber supremum, or deletion of a small random quadratic term is used below.


## 1. Immediate debt from r30

The preceding B09 report

`yspennstate/math-open-problems@5eb1e8fee3156a3cd6615dcde33f117ba54445b8`

proved in the diffuse exact singular-pair collar that either a disjoint physical third-volume branch is paid, or a macroscopic one-overlap third-compound packet is localized to one of the two literal hub coordinates, or the matrix enters an exact/near diagonal-plus-rank-four form. In particular its first unpaid implication was

`QFORM-SINGULARPAIR-FIXEDHUB-OMEGA1-OR-DIAGLOWRANK-SP-v1`.

This run pays a nontrivial fixed-hub piece of that debt: when the completed same-leaf non-diagonal curvature seen by the fixed hub has rank one, the entire one-overlap packet factors through the Plucker law of one physical two-plane. A whole-bank one-hub theorem from account02/B09 then gives either a direct continuous-density bound or a strong literal-coordinate localization certificate.

## 2. Setup: one literal hub and rank-one completed leaf curvature

Fix one literal original coordinate `h` and a disjoint leaf bank `L`. After conditioning only genuinely outside ORIGINAL coordinates, suppose the active principal block has the form

`A[{h} union L,{h} union L]
 = [[a,c^T],[c,D+lambda v v^T]],`                                  (2.1)

where

- `a` is arbitrary real;
- `c in R^L` is the actual physical star;
- `D` is arbitrary diagonal in the ORIGINAL leaf coordinates;
- `lambda !=0`;
- `v` is a unit vector in `R^L`.

Arbitrary affine terms produced by outside conditioning are allowed. No claim is made that every target matrix has this form; it is the rank-one member of the diagonal-plus-low-rank survivor isolated by the preceding B09 reduction.

For unordered two-subsets `I={i,j}` and `J={k,l}` of `L`, with the coordinates listed in increasing order, define the fixed-hub anchored minor

`d_(I,J)=det A[{h} union I,{h} union J].`                          (2.2)

We restrict below to `I cap J=empty`, precisely the one-shared third-compound geometry: the row and column triples share only the literal hub `h`.

Put

`w_ij=c_i v_j-c_j v_i`.                                          (2.3)

## 3. Exact anchored-minor factorization

### Theorem `QFORM-FIXEDHUB-RANK1-OMEGA1-PLUCKER-v1`, algebraic part

For every disjoint leaf pair `I={i,j}`, `J={k,l}`,

`boxed: d_(I,J)=-lambda w_ij w_kl.`                               (3.1)

The physical hub scalar `a` and the arbitrary leaf diagonal `D` disappear exactly.

### Proof

Because `I` and `J` are disjoint, the physical diagonal `D` has zero `I x J` block. Thus the relevant `3 x 3` matrix is

`[[a,             c_k,             c_l],
  [c_i, lambda v_i v_k, lambda v_i v_l],
  [c_j, lambda v_j v_k, lambda v_j v_l]].`                        (3.2)

The lower-right `2 x 2` block has rank one, so its determinant vanishes. Expanding the remaining two cofactors gives

`d_(I,J)
 =-lambda(c_i v_j-c_j v_i)(c_k v_l-c_l v_k),`                    (3.3)

which is (3.1). QED.

This identity is useful precisely because it aggregates before inversion: every disjoint physical leaf pair is retained.

## 4. The fixed-hub Omega1 currency is exactly a Plucker collision statistic

Let

`theta=dist(c,span{v})`.                                         (4.1)

If `theta=0`, then every `w_ij=0`, hence the fixed-hub disjoint-leaf one-overlap currency below is zero. Assume `theta>0` and put

`z=[c-(c^T v)v]/theta`.                                          (4.2)

Then `v,z` are orthonormal. Let `U=[v,z]`, viewed as a physical `|L| x 2` frame. Its rank-two Plucker basis law is

`p_I=det(U_I)^2`, `|I|=2`.                                      (4.3)

Since

`det(U_{ij})=(v_i c_j-v_j c_i)/theta=-w_ij/theta`,               (4.4)

we have

`boxed: p_I=w_I^2/theta^2,    sum_I p_I=1.`                      (4.5)

Let `I,J` be iid draws from this basis law and set

`rho=P{I cap J=empty}
    =sum_(I cap J=empty) p_I p_J.`                               (4.6)

Define the ordered fixed-hub disjoint-leaf one-overlap currency

`Omega_(1,h)^dis
 =sum_(I,J: I cap J=empty) d_(I,J)^2.`                           (4.7)

Equations (3.1) and (4.5) give the exact identity

`boxed:
 Omega_(1,h)^dis
 =lambda^2 theta^4 rho.`                                         (4.8)

Thus this anchored third-compound packet is not merely bounded by a curvature/star invariant; it *is* the product of the one-hub analytic scale `( |lambda| theta^2 )^2` and the physical Plucker disjointness probability.

## 5. Analytic payment from the completed account02/B09 one-hub theorem

The completed designated-partner theorem used here is account02/B09's

`QFORM-ONEHUB-PLUCKER-SMOOTHING-v1`,

canonical source

`yspennstate/math-open-problems`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260923T074200Z-account02-B09-QFORM-r13/REPORT.md`.

For a literal hub with leaf block `D+sum_(s=1)^r lambda_s v_s v_s^T`, actual star `c`, augmented frame Gram matrix `G`, and two-basis disjointness probability `rho>0`, it proves a continuous density with

`||p_Q||_infinity
 <= ((r+2)/r) exp((r+1)/(r+2))
    [rho det(G) prod_s |lambda_s|]^(-1/(r+2)),`                  (5.1)

and the identical coefficient gives the interval estimate. Arbitrary hub self-curvature, outside couplings, outside quadratic terms, and affine terms remain allowed.

Apply it to (2.1) with `r=1`. Because `v` is unit,

`det G=dist(c,span v)^2=theta^2`.                                (5.2)

Hence, whenever `rho>0`, the full form in this scope has a continuous `C_0` density and

`boxed:
 ||p_Q||_infinity
 <= 3 e^(2/3) [rho |lambda| theta^2]^(-1/3).`                    (5.3)

Using (4.8),

`boxed:
 ||p_Q||_infinity
 <= 3 e^(2/3) rho^(-1/6)
    [Omega_(1,h)^dis]^(-1/6).`                                  (5.4)

The same right side times `|J|` bounds `P{Q in J}` for every interval `J`. There is no probability-squaring or square-root decoupling loss in the final small-ball estimate.

## 6. Diffusion-versus-localization fork with a universal threshold

The remaining factor in (5.4) is itself geometrically informative. Let

`alpha_i=P{i in I}`                                             (6.1)

be the coordinate marginals of the rank-two Plucker basis law. Since `U=[v,z]` has orthonormal columns,

`alpha_i=v_i^2+z_i^2`,
`sum_i alpha_i=2`.                                               (6.2)

By the union bound for two iid bases,

`1-rho
 =P{I cap J != empty}
 <=sum_i P{i in I and i in J}
 =sum_i alpha_i^2
 <=2 max_i alpha_i.`                                             (6.3)

Therefore, for every fixed `delta in (0,1)`, at least one of the following holds:

**(A) diffuse whole-bank payment:** `rho>=delta`, in which case

`boxed:
 ||p_Q||_infinity
 <=3 e^(2/3) delta^(-1/6)
   [Omega_(1,h)^dis]^(-1/6),`                                   (6.4)

with a continuous density and the same linear interval bound;

**(B) literal physical localization:** some original leaf coordinate `i` satisfies

`boxed:
 v_i^2+z_i^2 > (1-delta)/2.`                                    (6.5)

This is a source-coordinate certificate, not a rotated-random-variable statement.

A convenient numerical choice is `delta=1/4`. Then either

`boxed:
 ||p_Q||_infinity
 <= 3*2^(1/3)*e^(2/3)
    [Omega_(1,h)^dis]^(-1/6)
 <7.362 [Omega_(1,h)^dis]^(-1/6),`                              (6.6)

or some literal leaf coordinate has augmented-plane leverage

`boxed: v_i^2+z_i^2>3/8.`                                       (6.7)

This is the main new theorem of the run.

### Direct splice into r30's fixed-hub branch

In the r30 fork, if the winning fixed-hub one-overlap packet obeys

`Omega_(1,h)^dis >=13/48`                                       (6.8)

and its completed non-diagonal leaf curvature is rank one as in (2.1), then either

`boxed: ||p_Q||_infinity<9.153`                                 (6.9)

with a continuous density and `P{Q in J}<9.153|J|`, or the physical localization certificate (6.7) holds.

Thus the rank-one fixed-hub Omega1 branch is no longer an unstructured aggregate-minor obstruction: the only unpaid endpoint is a strongly localized augmented curvature/star two-plane.

## 7. Why the localization alternative is the correct endpoint

No lower bound on a single physical minor follows from aggregate Omega1 alone. Formula (4.8) makes the obstruction exact: if the two-plane Plucker law is highly collision-prone, the whole-bank smoothing theorem necessarily pays a factor `rho^(-1/6)`, but collision-proneness itself forces a large physical row leverage by (6.3). This is precisely the kind of finite physical localization that can be promoted to an additional hub in the existing grouped-coordinate machinery.

Conversely, when every physical row of the augmented plane is diffuse, `rho` cannot collapse. For example, if `max_i(v_i^2+z_i^2)<=q0<1/2`, then

`rho>=1-2q0`,                                                    (7.1)

and (5.4) immediately gives

`||p_Q||_infinity
 <=3 e^(2/3)(1-2q0)^(-1/6)
   [Omega_(1,h)^dis]^(-1/6).`                                   (7.2)

This is an aggregate-before-inversion statement and avoids the already-refuted `one good tiny minor` mechanism.

## 8. Required designated account02/B09 result applied to an actual target inequality

I also apply the newer completed designated-partner result

`QFORM-ROUGH-STAR-UNIFORM-SQRT-SMALLBALL-v1`
plus its pair-log splice,

`yspennstate/math-open-problems@9ccee3f9a64a934c026786b63baca551ef0ba743`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260924T042556Z-account02-B09-QFORM-auto11-r17/REPORT.md`.

For an invertible indefinite literal physical pair `B`, put

`D_B=|det B|`, `kappa=sigma_min(B)`. If its exact Schur remainder is

`R=sX^2+2X<m,Z>+bX+G(Z)+c`, `m!=0`,                              (8.1)

then, uniformly in the scalar curvature `s` and arbitrary same-bank phase `G`, the partner theorem gives

`||p_Q||_infinity
 <13.831 [D_B kappa ||m||_2]^(-1/4),`                           (8.2)

with the same coefficient in the interval bound. Continuity is not claimed by this pair-log splice.

Apply it to independent cap-one inputs in

`Q_*=2UV+5X^2+2XZ_1+3Z_2^2.`                                   (8.3)

The literal physical pair `(U,V)` has

`B=[[0,1],[1,0]]`, `D_B=kappa=1`.                               (8.4)

The Schur remainder has `m=e_1`, `||m||=1`, scalar curvature `s=5`, and arbitrary-phase slot `G(Z)=3Z_2^2`. Hence

`boxed:
 ||p_(Q_*)||_infinity<13.831,
 P{Q_* in J}<13.831 |J|.`                                       (8.5)

The matrix spectrum is

`{1,-1,3,(5+sqrt(29))/2,(5-sqrt(29))/2}`.                       (8.6)

Thus this is an actual target-valid inequality: at least the eigenvalues `1,-1,3` have modulus at least one, and the dense/scalar-curvature slots are retained exactly.

## 9. Deterministic checks

A numerical regression with eight leaf coordinates, random unit `v`, arbitrary random `c`, arbitrary diagonal `D`, arbitrary hub scalar `a`, and `lambda=2.3` gave:

- maximum error in (3.1) over all ordered disjoint leaf-pair pairs: `6.66e-16`;
- `sum_I p_I=1.0000000000000002`;
- `rho=0.4082919436249993`;
- direct `Omega_(1,h)^dis=175.99627343944675`;
- formula `lambda^2 theta^4 rho=175.99627343944638`;
- discrepancy `3.69e-13`.

These computations are checks only; the proof above is exact.

The threshold constant in (6.6) is

`3*2^(1/3)*e^(2/3)=7.361973353764773`,                          (9.1)

and with `Omega>=13/48` the resulting value is `9.1525874838...`.

The partner-example nontrivial two-by-two block has eigenvalues

`(5+sqrt(29))/2=5.1925824036...`,
`(5-sqrt(29))/2=-0.1925824036...`,                               (9.2)

consistent with (8.6).

## 10. Exact remaining B09 debt

The full QFORM conjecture remains OPEN. The first B09 implication after this run is

`QFORM-FIXEDHUB-HIGHLEVERAGE-OR-RANK234-OMEGA1-v1`:

> In the singular-pair survivor, route the new rank-one fixed-hub localization endpoint `max_i(v_i^2+z_i^2)>3/8` through a literal promoted hub without dividing by a small scalar pivot; and extend the exact fixed-hub Omega1 Plucker compiler from completed leaf rank one to completed ranks two through four (or force a disjoint crossing / already-paid carrier exit).

The rank-one diffuse branch is paid end-to-end with an `O(|J|)` estimate; the higher-rank and strongly localized branches are not claimed solved.

## 11. Integrity and privacy note

The changed-file allowlist for this run consists only of this mathematical report and its adjacent deterministic check file in the authorized private QFORM worker root, plus the matching private brain handoff/memory/status records. A manual narrow scan found no credentials, account secrets, unrelated personal material, financial/client data, benchmark answers, or public-release content. No installation, remote workflow, permission expansion, email, push notification, task creation, schedule mutation, or public release is performed.
