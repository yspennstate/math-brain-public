SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B15, 2026-09-24T02:31:46Z.
attacking: the principal-pair-degenerate rank-three chamber via a product half-Riesz estimate, then same-constant C0 closure.

# account03/B15 — pair-minor-degenerate triple smoothing and an elementary fixed-instance regularity closure

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T023146Z-account03-B15-qform-auto31`  
Status: `PAIR-MINOR-DEGENERATE-TRIPLE-BOUND_PROVED / ELEMENTARY_FIXED-INSTANCE-LINF-CLOSURE / PARTNER_APPLIED / FULL_QFORM_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and the missing endpoint

The unrestricted owner theorem is still OPEN. This run fills an exact algebraic boundary left by the physical-pair route.

The preceding account03/B15 theorem proved a finite matrix-dependent density bound whenever a rank-at-least-three symmetric matrix has a nonsingular physical `2x2` principal block. For an indefinite block `D` it gives

`||p_Q||_infinity <= 2^(13/4) ( |det D| sigma_min(D) eta(S_D) )^(-1/4)`,

where `S_D` is the Schur complement and `eta(S_D)>0` is one explicit physical Schur coefficient; for a definite block it gives `pi/sqrt(|det D|)`. The source is

`yspennstate/math-open-problems@2f36eb6204ac8598eaf63faed15f9fa7fddffd0c`
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B15/20260923T222614Z-account03-B15-qform-auto27/REPORT.md`.

That argument does not cover matrices for which every physical `2x2` principal determinant is zero. Such matrices can nevertheless have rank three or more; for example

`[[1,1,1],[1,1,-1],[1,-1,1]]`

has eigenvalues `2,2,-1` while all three `2x2` principal determinants vanish.

This run proves a direct product-law smoothing theorem for exactly this pair-minor-degenerate triple. Combined with the preceding pair theorem, it yields an elementary explicit finite `L^infinity` certificate for **every fixed symmetric matrix of rank at least three** under arbitrary independent cap-one inputs. The constants remain matrix-dependent, so this does not solve the owner's universal spectral problem.

## 2. Product small-ball lemma for a bilinear variable

### Lemma 2.1 — `QFORM-PRODUCT-INTERVAL-LOG-v1`

Let `U,V` be independent real random variables with probability densities bounded by one. For every interval `J` of length `ell>0`,

`P(UV in J) <= psi(ell)`,

where

`psi(ell)=1` for `ell>=1/2`, and

`psi(ell)=2 ell [1+log(1/(2 ell))]` for `0<ell<1/2`.

No support, moment, connectedness or smoothness hypothesis is used.

#### Proof

Condition on `U=u`. Multiplication by a nonzero `u` sends the interval `J` to an interval in the `V` variable of length `ell/|u|`, hence

`P(UV in J | U=u) <= min(1, ell/|u|)`.

The function `m_ell(u)=min(1,ell/|u|)` is even and nonincreasing in `|u|`. Among probability densities `0<=f<=1`, the integral of `m_ell` is maximized by filling the centered interval of Lebesgue measure one. Therefore

`E m_ell(U) <= int_{-1/2}^{1/2} min(1,ell/|u|) du`.

For `ell<1/2` this equals

`2 ell + 2 ell int_ell^(1/2) du/u
 =2 ell [1+log(1/(2ell))]`.

For `ell>=1/2` it equals one. QED.

This is stronger than the coarse square-root small-ball bound at the logarithmic endpoint and will be used only inside an integrable half-Riesz layer cake.

## 3. Uniform half-Riesz potential of an affine bilinear product

### Lemma 3.1 — `QFORM-AFFINE-BILINEAR-HALF-RIESZ-v1`

Let `U,V` be independent probability variables with density caps

`||f_U||_infinity<=a`, `||f_V||_infinity<=b`,

where `a,b>0`. Let

`T=cUV+alpha U+beta V+gamma`, `c!=0`.

Then

`boxed( sup_t E (t-T)_+^(-1/2) <= 4 sqrt(2) sqrt(ab/|c|). )`      (3.1)

The convention is that the integrand is zero when `t-T<=0`; changing the sign inside the positive part gives the same estimate after replacing `T` by `-T`.

#### Proof for unit caps and `c=1`

Translations absorb the affine terms because

`UV+alpha U+beta V+gamma
 =(U+beta)(V+alpha)+(gamma-alpha beta)`.

Thus it is enough to estimate `Z=UV+d`. By layer cake,

`E (t-Z)_+^(-1/2)
 =int_0^infinity P(0<t-Z<s^(-2)) ds`.

The event on the right restricts `UV` to an interval of length `ell=s^(-2)`. Lemma 2.1 gives probability at most one for `s<=sqrt(2)` and, for `s>sqrt(2)`, at most

`2 s^(-2) [1+log(s^2/2)]`.

Hence

`E (t-Z)_+^(-1/2)
 <=sqrt(2)+int_(sqrt(2))^infinity 2s^(-2)[1+log(s^2/2)] ds`.

Using

`int_a^infinity s^(-2) ds=1/a`,
`int_a^infinity s^(-2) log s ds=(log a+1)/a`,

with `a=sqrt(2)`, the tail integral is `3sqrt(2)`. Therefore the total is `4sqrt(2)`.

#### Scaling

Set `U'=aU`, `V'=bV`; these new variables have density caps one. Then

`cUV=(c/(ab))U'V'`,

so homogeneity of the half-power kernel multiplies the unit-cap bound by `sqrt(ab/|c|)`. Separate translations remove `alpha,beta`, completing the proof of (3.1). QED.

## 4. The pair-minor-degenerate invertible triple

### Theorem 4.1 — `QFORM-ZERO-PAIR-MINORS-TRIPLE-v1`

Let `X_1,X_2,X_3` be independent real random variables with probability densities bounded by one. Let `B` be a real symmetric `3x3` matrix such that

1. `det B !=0`, and
2. every `2x2` principal determinant vanishes:

`B_ii B_jj-B_ij^2=0` for all `i!=j`.

For arbitrary affine coefficients `r in R^3` and constant `c0`, the variable

`Y=X^T B X+2 r^T X+c0`

has an essentially bounded density and

`boxed( ||p_Y||_infinity
 <=4 ( |det B| max_i |B_ii| )^(-1/4). )`                         (4.1)

In particular the estimate is translation-uniform in every affine coefficient.

### Proof

Because `det B!=0`, no diagonal entry can vanish: if `B_ii=0`, the zero principal-minor identities force `B_ij=0` for every `j`, giving a zero row. Moreover `B_ii B_jj=B_ij^2>0`, so all three diagonal entries have the same sign. Multiplying the whole polynomial by `-1` if needed does not change density height, so assume `B_ii>0`.

Put

`d_i=B_ii>0`, `a_i=sqrt(d_i)`,
`epsilon_ij=B_ij/(a_i a_j) in {+1,-1}`.

The normalized determinant is

`det [[1,e12,e13],[e12,1,e23],[e13,e23,1]]
 =2(e12 e13 e23-1)`.

Since `det B!=0`, necessarily `e12 e13 e23=-1`, and therefore

`|det B|=4 d_1 d_2 d_3`.                                        (4.2)

Independent sign flips of the original variables preserve independence and the density caps and allow us to arrange

`e12=e13=+1`, `e23=-1`.

Scale

`U=a_1 X_1`, `V=a_2 X_2`, `W=a_3 X_3`.

Their density caps are respectively

`c_1=d_1^(-1/2)`, `c_2=d_2^(-1/2)`, `c_3=d_3^(-1/2)`.

In these variables the quadratic part is

`U^2+V^2+W^2+2UV+2UW-2VW
 =(U+V+W)^2-4VW`.                                                 (4.3)

Write the transformed affine part as `l_1 U+l_2 V+l_3 W+c`. Set

`R=U+V+W+l_1/2`.

A direct completion gives

`Y=R^2-4VW+(l_2-l_1)V+(l_3-l_1)W+c'`.                            (4.4)

The last three terms are an affine bilinear function of the independent pair `(V,W)`. Indeed, after separate translations of `V` and `W`, they equal

`-4 V'W'+c''`.                                                    (4.5)

For fixed `V,W`, the variable `R` is only a translate of `U`; hence its conditional density still has cap `c_1`. Therefore the conditional density of `R^2+T(V,W)` satisfies

`p_(Y|V,W)(t) <= c_1 (t-T(V,W))_+^(-1/2)`.                      (4.6)

Averaging (4.6) and applying Lemma 3.1 to the coefficient `c=-4` yields

`||p_Y||_infinity
 <=c_1 *4sqrt(2)*sqrt(c_2 c_3/4)
 =2sqrt(2) c_1 sqrt(c_2 c_3)`.                                   (4.7)

The same argument may pivot on any of the three coordinates, so

`||p_Y||_infinity
 <=min_k 2sqrt(2) d_k^(-1/2) prod_(j!=k)d_j^(-1/4)
 =2sqrt(2) (d_1 d_2 d_3 max_k d_k)^(-1/4)`.

Using (4.2) gives exactly (4.1). QED.

### Conditional ambient version

Let the same block `B` occur as a physical principal block of an arbitrary larger symmetric matrix `A`. Condition only on all original coordinates outside the block. Original-coordinate independence remains intact, and the outside variables create only arbitrary affine coefficients in the selected triple. Therefore the same interval/density estimate (4.1) holds for the full ambient quadratic form, with **no restriction at all** on outside quadratic curvature or cross couplings.

## 5. A complete elementary fixed-matrix `L^infinity` closure for rank at least three

The new theorem plugs the only exact algebraic hole in the preceding physical-pair certificate.

### Proposition 5.1 — principal `2-or-3` dichotomy

Let `A` be real symmetric with `rank(A)>=3`. Then one of the following holds.

**(P2)** Some physical `2x2` principal block is nonsingular.

**(P3deg)** Every physical `2x2` principal determinant vanishes, but some physical `3x3` principal block is nonsingular and has all of its `2x2` principal determinants zero.

#### Proof

If (P2) fails, then for every `i,j`,

`A_ii A_jj=A_ij^2`.                                               (5.1)

If `A_ii=0`, (5.1) forces the entire `i`th row to vanish. Restrict to the nonzero diagonal indices. All diagonal entries there have one common sign; after removing that sign and scaling by `sqrt(|A_ii|)`, the remaining matrix is a symmetric sign matrix `E` with diagonal one and off-diagonal entries `epsilon_ij in {+1,-1}`.

If every triangle satisfies

`epsilon_ij epsilon_ik epsilon_jk=+1`,                            (5.2)

fixing a base vertex `i0` and setting `s_j=epsilon_(i0,j)` gives `epsilon_jk=s_j s_k` for all `j,k`. Hence `E=ss^T` has rank one, contradicting `rank(A)>=3`. Therefore some triangle has sign product `-1`; its normalized determinant is `-4`, so the associated physical `3x3` principal block is nonsingular. This is (P3deg). QED.

### Corollary 5.2 — explicit finite fixed-matrix certificate

Let the coordinates of `X` be independent with densities at most one and let `rank(A)>=3`.

- In case (P2), if the selected nonsingular pair `D` is definite, the elementary ellipse-shell estimate gives

  `||p_Q||_infinity <= pi/sqrt(|det D|)`.

- In case (P2), if `D` is indefinite, let `S_D` be its Schur complement. Since

  `rank(A)=2+rank(S_D)`

  and `rank(A)>=3`, `S_D!=0`. The preceding account03/B15 theorem gives

  `||p_Q||_infinity
   <=2^(13/4)(|det D| sigma_min(D) eta(S_D))^(-1/4)`.

- In case (P3deg), Theorem 4.1 gives

  `||p_Q||_infinity
   <=4(|det B| max_i |B_ii|)^(-1/4)`.

Thus **every fixed symmetric rank-at-least-three matrix has an explicit finite physical-entry density certificate for every cap-one product law**. This is an elementary alternative route to the already completed fixed-matrix bounded-density theorem.

The result is not uniform under only `s_3(A)>=1`: the paying pair/triple physical coefficients can collapse in diffuse families. Hence Proposition 5.1 is a qualitative/fixed-matrix closure, not the missing universal structural theorem.

## 6. Designated partner applied: same-constant `C_0` closure

The completed designated partner result is account04/B15,

`yspennstate/math-open-problems@7b2b0f54db9acbd23a5f69f715178ab666e22d8e`
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260923T221909Z-account04-B15-ruled-trace-c0-r8/REPORT.md`.

Its Theorem 6.1 states that for a fixed cap-one product instance with `rank(A)>=3`, any separately proved interval bound

`P(Q in I)<=M|I|`

upgrades to a canonical representative `p_Q in C_0(R)` with the **same** pointwise height `||p_Q||_infinity<=M`.

Apply it to the actual inequality from Theorem 4.1. If a target/full-rank instance contains a pair-minor-degenerate nonsingular physical triple `B`, then

`boxed( p_Q in C_0(R),
        ||p_Q||_infinity
        <=4(|det B| max_i |B_ii|)^(-1/4). )`                     (6.1)

Applying the same partner theorem to the two (P2) inequalities proves that the complete fixed-matrix certificate in Corollary 5.2 always has a `C_0` representative with zero additional height cost.

This is a genuine use of the partner result at a new inequality. Continuity is not inferred from essential boundedness alone and no class-uniform modulus of continuity is claimed.

## 7. Exact target example missed by every nonsingular-pair route

Take

`B0=[[1,1,1],[1,1,-1],[1,-1,1]]`.

All three physical `2x2` principal determinants are exactly zero, while

`det B0=-4`,

and the eigenvalues are `2,2,-1`. Thus `B0` itself is in the owner's three-large-eigenvalue target and it lies exactly on the singular boundary of every physical-pair argument.

Theorem 4.1 gives, for **every** three independent cap-one input laws and arbitrary affine perturbation,

`boxed( ||p_Q||_infinity <=4*(4)^(-1/4)=2sqrt(2). )`             (7.1)

The partner compiler therefore yields

`boxed( p_Q in C_0(R), ||p_Q||_infinity<=2sqrt(2). )`             (7.2)

This target family is fully rough-law and uses no support, moment, Gaussian, log-concavity or post-rotation independence assumption.

## 8. Absolute continuity, boundedness and continuity kept separate

1. **Absolute continuity.** For any nonzero symmetric `A` and any absolutely continuous joint input law, `Q=X^TAX` is absolutely continuous. Indeed, the critical set `ker A` has Lebesgue measure zero. On `{|grad Q|>1/k}`, coarea applied to `F/|grad Q|` shows that the preimage of every one-dimensional null set has zero input mass; union over `k` and add the null critical set.
2. **Essential boundedness.** The new bound (4.1) and the complete certificate in Section 5 are proved before continuity is invoked.
3. **Continuity.** The completed account04/B15 theorem adds `C_0` only after the interval constant has been paid, with no loss in the constant.
4. **Universal target.** Still OPEN. The remaining problem is to replace matrix-dependent physical certificates by a dimension-free consequence of the spectral assumption `s_3(A)>=1`, necessarily through aggregation in the diffuse/minor-collapse chamber.

## 9. New structural interpretation and next step

The exact algebraic boundary of the physical-pair route is no longer a fixed-instance regularity obstruction. If a nonsingular physical pair exists, the pair/Schur theorem applies; if none exists, rank at least three forces a frustrated sign triangle and Theorem 4.1 applies.

Therefore a future universal proof may safely treat **small** physical pair determinants as a quantitative aggregation problem rather than fear an unhandled exact-zero endpoint. The productive next mechanism is to develop a quantitative stability version of Proposition 5.1: if all physical `2x2` principal determinants are small, show that either a weighted collection of frustrated triangles pays the half-Riesz bound after bank aggregation, or the matrix enters an already-paid diffuse/grouped/ridge branch. The known no-single-minor corrections forbid claiming one raw triangle has a universal coefficient.

No full-QFORM completion or counterexample is claimed here.

## 10. Source/correction discipline

Fresh brain controls at publication refresh: owner-control revision `2026-09-22.15`, QFORM-only, no account03/B15 pause. Relevant live corrections retained include: no post-rotation independence; no uniform pointwise quadratic-phase decay; no naive fiber-sup dimension-free estimate; no fixed fragment-count reduction; no one-raw-minor universal extraction; and the corrected nonzero-square affine-slope failure from account03/B15. None is used as a premise.

The new proofs condition only on original independent coordinates. The only rearrangement step is the one-dimensional bathtub bound in Lemma 2.1, where it is exact for the explicit decreasing kernel `min(1,ell/|u|)` and does not assert interval extremality for the QFORM problem itself.

Execution remains `WITHOUT_VERIFIED_BRAIN`: authenticated repository retrieval/write is not evidence of native mathematical receiver ingestion.
