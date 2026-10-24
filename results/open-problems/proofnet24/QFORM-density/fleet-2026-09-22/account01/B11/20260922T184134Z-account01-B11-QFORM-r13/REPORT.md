# account01/B11 — support-separated parabolic banks and an exact overlap obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260922T184134Z-account01-B11-QFORM-r13`  
Assignment: indefinite signatures `(+,+,-)` / `(+,-,-)`  
Outcome: `ESSENTIAL_STEP_APPLIED / FULL TARGET OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Target and conditional end-to-end reduction

The target is the full arbitrary-dimensional statement: for independent real coordinates with probability densities bounded by one and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove a universal finite essential bound for the density of `X^T A X`, or construct a valid target-level counterexample. Continuity is a separate desired conclusion.

For the exact-rank-three indefinite chamber, the preceding B11 run proved a uniform local closure whenever one physical spectral pair has area `G_ij=||r_i x r_j||^2 >=1/4`; the remaining chamber was many small pair areas. A natural conditional route is:

1. close a uniformly strong physical pair by the previous B11 cross-dominated / scalar-pivot alternatives;
2. if no strong pair exists, aggregate original coordinates before paying reciprocal minor costs;
3. if the three spectral directions split into one original-coordinate bank independent of a transverse two-dimensional bank, apply the parabolic smoothing theorem below;
4. otherwise use a diffuse/ridge certificate, or prove a genuinely dependence-safe overlapping-bank estimate.

This run attacks item 3 exactly and then tests whether the required support separation is automatic. It is not: an explicit exact-target Fourier-frame family has all physical pair areas tending to zero and admits no spectral `1+2` decomposition with disjoint original-coordinate supports. Thus the first unpaid implication is sharpened to an overlapping-bank parabolic estimate, not merely “find banks.”

No pointwise oscillatory decay, rotated conditional-density cap, arbitrary-joint coarea estimate, or best-principal-minor selector is used.

## 2. Source-pinned partner results actually used

The assigned partner `account02/B11` supplied two completed results used quantitatively here.

1. One-dimensional projection cap, canonical proof commit `245a4e2a4414294fbb20b9dd4f292f6b001e5aa2`: if independent cap-one variables are linearly combined with coefficient vector of Euclidean norm one, the resulting density is at most `sqrt(e)`.

2. Parabolic weak-`L^{3/2}` smoothing, canonical proof commit `e32368258f33ea03369d23721742345e6f22447f`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B11/20260922T152031Z-account02-B11-qform-r18-a91c/REPORT.md`: if `Z` is independent of `(V,W)`, `||p_Z||_infinity<=L`, and `(V,W)` has joint density at most `M`, then

`T=2ZW+V^2`

has

`||p_T||_infinity <= 3*2^(4/3)*(LM)^(2/3)`.

The same account02/B11 projection work gives the two-dimensional isotropic projection cap `e`.

The partner’s latest bank theorem, canonical proof commit `d56d97c85ced819f45ddad0987deaa5eb4b53cdc`, is a special case of the grouped theorem below and is used as a consistency check.

## 3. New theorem: support-separated scalar bank versus transverse plane

### Theorem 3.1

Let the independent cap-one original coordinates be partitioned into disjoint sets `I,J`. Let

`Z = sum_{i in I} u_i X_i`,
`V = sum_{j in J} v_j X_j`,
`W = sum_{j in J} w_j X_j`,

where `u` is nonzero and `v,w` are linearly independent. Put

`sigma = ||u||_2`,
`Delta = sqrt(||v||_2^2 ||w||_2^2 - <v,w>^2)>0`.

For nonzero real `alpha,beta`, define

`T = 2 alpha Z W + beta V^2`.

Then `T` has an essentially bounded density and

`||p_T||_infinity <= C_sep ( |alpha| sigma sqrt(|beta|) Delta )^(-2/3)`,        (3.1)

where

`C_sep = 3*2^(4/3)*e < 20.549`.

The same estimate holds after adding arbitrary affine terms `rZ+sV+tW+c`.

### Proof

Normalize the scalar coefficients. The account02/B11 one-dimensional projection theorem gives

`||p_Z||_infinity <= sqrt(e)/sigma`.                                      (3.2)

For the pair let

`G = [[||v||^2,<v,w>],[<v,w>,||w||^2]].`

Whitening by `G^(-1/2)` turns `(V,W)` into a two-dimensional isotropic projection of the independent coordinates indexed by `J`. Hence the account02/B11 two-dimensional projection theorem and the Jacobian formula give

`||p_(V,W)||_infinity <= e/sqrt(det G) = e/Delta`.                         (3.3)

Because `I` and `J` are disjoint, `Z` is genuinely independent of `(V,W)`, exactly the provenance required by the live corrections.

If `beta>0`, set

`Z' = alpha Z`, `V'=sqrt(beta)V`, `W'=W`.

Then

`||p_Z'||_infinity <= sqrt(e)/( |alpha| sigma)`,
`||p_(V',W')||_infinity <= e/(sqrt(beta) Delta)`.

Applying the partner parabolic weak-`L^{3/2}` theorem yields

`||p_T||_infinity
 <= 3*2^(4/3) [ e^(3/2)/( |alpha| sigma sqrt(beta) Delta) ]^(2/3)
 = 3*2^(4/3)e ( |alpha| sigma sqrt(beta) Delta)^(-2/3).`

If `beta<0`, apply the positive-square case to `-T`; the density norm is unchanged.

For affine terms, successively translate `W` by `r/(2alpha)`, `V` by `s/(2beta)`, and `Z` by the resulting coefficient of `W` divided by `2alpha`. These translations preserve all density caps and the `I/J` independence. Only an additive constant remains. This proves (3.1).

### Checks against prior branches

- If `Z` is one untouched original coordinate and `(V,W)` is a two-dimensional Parseval projection, (3.1) gives the previous null-endpoint constant `3*2^(4/3)e^(2/3)<14.724` after using the sharper scalar cap `1` instead of `sqrt(e)`.
- If `W` is one untouched original coordinate and `V` is a normalized disjoint linear bank, the pair density factorizes and the sharper partner bank bound `3*2^(4/3)e^(1/3)<10.551` is recovered.

Thus the theorem is the exact grouped-coordinate closure promised by the partner’s `BANK-SEPARATION` implication whenever the needed support split really exists.

No continuity claim is made from this argument; the conclusion here is essential boundedness.

## 4. Exact target family showing bank separation is not automatic

Fix `1/2<=c<1` and an integer `m>=5`. Put `theta_j=2*pi*j/m` and define an `(m+1) x 3` matrix `U` by the rows

`r_0=(sqrt(c),0,0)`,

`r_(j+1)=(a,b cos(theta_j),b sin(theta_j)),  0<=j<m`,

where

`a=sqrt((1-c)/m)`, `b=sqrt(2/m)`.

The elementary trigonometric identities

`sum cos(theta_j)=sum sin(theta_j)=sum cos(theta_j)sin(theta_j)=0`,
`sum cos(theta_j)^2=sum sin(theta_j)^2=m/2`

show exactly that

`U^T U = I_3`.                                                            (4.1)

Let

`H0=[[0,0,1],[0,1,0],[1,0,0]]`,
`A=U H0 U^T`.

Since `H0` has eigenvalues `{1,1,-1}` and `U` is an isometry on `R^3`, the nonzero eigenvalues of `A` are exactly `{1,1,-1}`. Hence this is an exact target-class rank-three form of signature `(+,+,-)`; negation gives `(+,-,-)`.

Writing `Z,V,W` for the three spectral projections,

`Q=X^TAX=2ZW+V^2`,

with

`Z=sqrt(c)X_0+a sum_j X_(j+1)`,
`V=b sum_j cos(theta_j) X_(j+1)`,
`W=b sum_j sin(theta_j) X_(j+1)`.                                       (4.2)

The heavy row has leverage `c` and is exactly null for the quadratic metric:

`A_00=r_0^T H0 r_0=0`.                                                    (4.3)

At the same time its bilinear export is macroscopic:

`A_(0,j+1)=sqrt(2c/m) sin(theta_j)`,
`sum_j A_(0,j+1)^2=c`.                                                    (4.4)

So this lies directly in the heavy-null / many-small-pair geometry rather than an easy diagonal branch.

## 5. Every physical spectral pair is small

For the heavy row and an outside row,

`G_(0,j+1)=||r_0 x r_(j+1)||^2 = 2c/m`.                                  (5.1)

Every outside row has squared norm

`||r_(j+1)||^2=(3-c)/m`.

Therefore for two outside rows,

`G_(j+1,k+1)<=||r_(j+1)||^2 ||r_(k+1)||^2=((3-c)/m)^2`.                   (5.2)

Consequently

`max_{i<j} G_ij <= max(2c/m,((3-c)/m)^2) ->0`.                            (5.3)

Thus the previous B11 strong-pair closure cannot become dimension-free on this family by choosing one physical pair. This is the exact situation in which grouped aggregation is required.

## 6. Strong obstruction: no exact product-preserving `1+2` spectral support split

The obstruction is basis-invariant inside the three-dimensional spectral subspace.

Any vector `g` in `range(U)` has outside coordinates of the form

`g_(j+1)=A+B cos(theta_j)+C sin(theta_j)`.                                (6.1)

A nonzero trigonometric polynomial of this degree has at most two zeros among the `m` equally spaced angles: after writing it as `A+R cos(theta-phi)`, the equation equals zero at at most two points on a full circle. If (6.1) vanishes identically, then `A=B=C=0`, and because `a,b>0` the spectral coefficient vector is zero. Hence

**every nonzero vector in `range(U)` has at most two zero outside coordinates.**   (6.2)

Suppose there were a spectral decomposition into a nonzero scalar direction `g` and a two-dimensional transverse plane spanned by independent nonzero vectors `h,k` such that

`supp(g) cap (supp(h) union supp(k)) = empty`.                             (6.3)

By (6.2), `g` is nonzero on at least `m-2>=3` outside coordinates. Then both `h` and `k` must vanish on those at least three outside coordinates. By (6.2), each must be zero, a contradiction.

Therefore no change of spectral basis produces one nonzero spectral direction supported on original coordinates disjoint from a complementary two-dimensional spectral plane. In particular, the independence hypothesis needed by Theorem 3.1 cannot be obtained by an exact product-preserving linear `1+2` regrouping in this family.

This is a source-valid counterexample to the intermediate structural implication

`many-small-pair heavy-null frame => exact scalar-bank / transverse-plane support separation`.

It is **not** a counterexample to the quadratic-form density conjecture.

## 7. Even-m block identity: the dependence can be localized without lying about conditional independence

For `m=2M`, pair antipodal coordinates `j` and `j+M`, and write

`S_j=X_(j+1)+X_(j+M+1)`,
`D_j=X_(j+1)-X_(j+M+1)`, `0<=j<M`.

The blocks `(S_j,D_j)` are independent across `j`. If the two original marginal densities in block `j` are `f_j,g_j`, then the exact transformed joint density is

`h_j(s,d)=(1/2) f_j((s+d)/2) g_j((s-d)/2) <=1/2`.                         (7.1)

Since `theta_(j+M)=theta_j+pi`, (4.2) becomes

`Z=sqrt(c)X_0+a sum_{j<M} S_j`,
`V=b sum_{j<M} cos(theta_j) D_j`,
`W=b sum_{j<M} sin(theta_j) D_j`.                                       (7.2)

Thus the entire forbidden overlap is localized into **independent two-dimensional cap-one-half blocks**: the longitudinal coordinate uses the `S` component of each block and the transverse plane uses the `D` component. This is exact and preserves arbitrary fragmented original laws.

Crucially, (7.1) does not imply a bounded conditional density of `S_j` given `D_j`; the live conjugate-variable correction forbids that step. The correct next mechanism is a block-level parabolic/Brascamp-Lieb estimate using the independent joint blocks themselves.

## 8. Rank-two logarithmic control and the third-direction debt

Deleting `V^2` from (4.2) leaves a rank-two saddle `2ZW`. For centered uniforms in a genuinely independent two-coordinate saddle this has the required logarithmic singularity at zero. Theorem 3.1 explains the clean separated case: the third square changes the saddle kernel to the partner’s weak-`L^{3/2}` parabolic kernel, and a bounded transverse pair density makes it integrable.

The Fourier-frame family shows the exact remaining difficulty: the third direction still has the right parabolic geometry, but the longitudinal residual and transverse pair share every outside original coordinate. One cannot replace this overlap by conditional independence. The third direction must remove the logarithm **jointly with product-source aggregation**.

## 9. First essential missing implication

`QFORM-OVERLAP-PARABOLIC-BLOCK-COMPILER-v1`:

For independent two-dimensional blocks `(S_j,D_j)` with joint densities bounded by an absolute constant, plus an independent cap-one scalar `X_0`, prove a dimension-free density bound for the structured parabolic form (7.2), uniformly over the number of blocks, coefficients satisfying the Fourier/Parseval identities, and all admissible block laws arising from independent scalar pairs; or derive an equally strong product-preserving reduction to an already proved ridge/diffuse/full-matrix-pair branch.

A proof of a suitably invariant version would close the explicit heavy-null overlap obstruction and is a concrete step toward the many-small-pair compiler. The unrestricted full-spectrum conjecture still requires the global aggregate-before-inversion passage recorded in current research.

## 10. Scope, continuity, and integrity

What is proved here:

- the quantitative support-separated theorem (3.1), using completed account02/B11 results at actual inequalities;
- an exact target-class `(+,+,-)` / `(+,-,-)` Fourier-frame family with all physical pair areas tending to zero;
- a proof that this family has no exact disjoint-support scalar-versus-plane spectral factorization in any spectral basis;
- an exact antipodal block representation localizing the overlap into independent two-dimensional blocks with joint density cap `1/2`.

What is not proved:

- a universal density bound for that overlapping Fourier-frame family under all admissible laws;
- the unrestricted exact-rank-three theorem;
- the arbitrary-extra-spectrum theorem;
- continuity in the new branches.

The full conjecture therefore remains `OPEN`.

Operational/source note: final control refresh used the current QFORM-only owner control (revision `2026-09-22.11`) and the live correction inbox. No scheduler mutation, notification change, external paid model, public release, or unrelated data was used. Repository access is not native learned-memory ingestion; execution remains `WITHOUT_VERIFIED_BRAIN`.
