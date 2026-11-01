SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B06, 2026-09-23T05:26:43Z.
attacking: aggregate a whole original-coordinate off-diagonal row before reciprocal curved-fiber payment, in the low-third-volume star/tube branch.

# fleet02/B06 — non-null star quarter-Riesz payment and hyperbola-row aggregation

**Run:** `b06-20260923T052643Z-e284cc399d47`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Curved fiber integration  
**Status:** `ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED`; full QFORM remains `OPEN / NOT PROVED / NOT DISPROVED`; continuity is not proved by the new endpoint.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and first unpaid implication

For every dimension, arbitrary independent real inputs with one-dimensional probability densities at most one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, the target is one universal essential bound for the density of `Q=X^TAX`, or a valid counterexample.

This run continues the preceding B06 non-null-star checkpoint `math-open-problems@15b22e8dad5d1e86b5f5ab85417ed611c9cd8e44`. That checkpoint obtained a subcritical fractional-potential estimate for a single genuine original-coordinate scalar coupled to a product-derived linear form, but had not yet converted it into a matrix-level aggregate curvature payment or exhibited a target family that forces aggregation.

The first unpaid implication attacked here is:

> In the low-third-volume / rank-two-or-star survivor, can one retain the original product law and pay a curved hyperbolic fiber from an **aggregate off-diagonal row norm**, without selecting one physical edge and without taking a worst fiber supremum?

The answer is yes for an exact zero-diagonal hyperbolic pair followed by an arbitrary Schur remainder having one nonzero off-diagonal physical row. The proof is dimension-free and keeps all remaining quadratic and affine terms.

## 2. Source-valid inputs actually applied

### 2.1 Newest Claude coordinate-hyperbola peel

From `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`, Lemma 4.3:

if a physical pair has `A_ii=A_jj=0`, `A_ij=mu!=0`, then after completing that pair in the ORIGINAL coordinates,

`D(Q):=||p_Q||_infinity <= 2^(3/4) kappa |mu|^(-3/4) H_(1/4)(S)`,       (2.1)

where `S` is the full Schur remainder, `H_alpha(S)=sup_t E|S-t|^(-alpha)`, and

`kappa=sup_(y>0) log(1+y)/sqrt(y)=0.804742...`.                         (2.2)

This is the completed result from the required Claude package that is applied at a real inequality in this run. It retains the conditional product structure of the two physical pivot coordinates and does not assume independence after a spectral rotation.

The required companion `RESULTS.md` and `COUNTEREXAMPLE_SEARCH.md` at the same commit were also read. In particular, the latter's physical-coordinate fiber identity and its warning that delocalized target families defeat one-local-block selection are consistent with the aggregate route used below; no numerical or one-sheet result is promoted beyond its stated scope.

### 2.2 Weighted product projection, already proved by B06

From `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`, this slot's theorem `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1` says that for an orthonormal `k`-frame `R`, the projection `R^T X` of independent cap-one coordinates has density cap at most `exp(k/2)`. For `k=1`, every normalized linear form in original independent coordinates therefore has density cap at most `sqrt(e)`. This is a weighted product-fiber integral, not an unrestricted fiber maximum.

### 2.3 Designated partner fleet03/B06 r25

The fresh completed partner result is

`yspennstate/math-open-problems@1e7aa194ee0cd3c2981afdeb2ddf66acf53b87fe`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260923T041802Z-fleet03-B06-qform-r25/REPORT.md`.

Its `QFORM-THIRD-VOLUME-L3-NOLEVERAGE-v1` proves, for an original-coordinate cross block `B`,

`||p_R||_3 <= [3^(3/2)e^(2/3)/2^(2/3)] Delta_3(B)^(-1/9)`,             (2.3)

with no leverage gate, and its dependence-safe outer-square splice gives

`||p_Q||_infinity <=4sqrt(2e)3^(3/8)|a|^(-1/2)Delta_3(B)^(-1/12)`.      (2.4)

In the partner's transverse chamber, `Delta_3(B)>=G^6/6400` therefore pays

`||p_Q||_infinity <29.230/sqrt(|a|G)`.                                 (2.5)

Thus the remaining B06 geometry must include genuinely low-third-volume objects. Section 6 below gives an exact target family with residual `Delta_3=0` and vanishing individual edges, and pays it by the new aggregate-row theorem instead.

## 3. Non-null scalar-star concentration with all dependence retained

### Theorem 3.1 — `QFORM-NONNULL-STAR-QUARTER-RIESZ-v1`

Let `X` be independent of an arbitrary random element `Y`. Assume `X` has density at most `K`, and let `Z=z(Y)` have a one-dimensional density at most `L`. Let `W=w(Y)` be arbitrary measurable and finite almost surely. For every real `a`, put

`T=aX^2+2XZ+W`.                                                        (3.1)

Then every interval `I` of length `eps` satisfies

`boxed: P(T in I) <=2 sqrt(2 K L eps).`                                (3.2)

Consequently, for every `0<alpha<1/2`,

`boxed: H_alpha(T)<=16^alpha (KL)^alpha/(1-2alpha),`                    (3.3)

and in particular

`boxed: H_(1/4)(T)<=4(KL)^(1/4).`                                      (3.4)

No independence between `Z` and `W` is assumed. The coefficient `a` may be zero, arbitrarily small, or arbitrarily large.

### Proof of (3.2)

If `a=0`, split according to `|Z|<=r`. The first part costs at most `2Lr`. On `|Z|>r`, conditioning on `Y` makes `x ->2Zx+W` affine; the preimage of `I` has length at most `eps/(2r)`, so the conditional probability is at most `K eps/(2r)`. Thus

`P(T in I)<=2Lr+K eps/(2r)<=2 sqrt(KL eps)`                             (3.5)

after optimization, which is stronger than (3.2).

Now suppose `a!=0` and write

`T=a(X+Z/a)^2 + W-Z^2/a`.                                               (3.6)

Because `X` and `Z` are independent, `U=X+Z/a` has density cap

`m:=min(K,|a|L)`.                                                       (3.7)

On `|U|<=r`, pay `2mr`. On `|U|>r`, condition on `Y`. On each of the two monotone branches of `a(x+Z/a)^2`, the derivative has magnitude at least `2|a|r`; across both branches, the preimage of `I` has total length at most `eps/(|a|r)`. Hence

`P(T in I)<=2mr+K eps/(|a|r)
          <=2 sqrt(2mK eps/|a|)
          <=2 sqrt(2KL eps)`,                                          (3.8)

proving (3.2).

### Proof of (3.3)

For fixed `t`, the interval `{|T-t|<rho}` has length `2rho`, so (3.2) gives

`P(|T-t|<rho)<=min(1,4 sqrt(KL rho)).`                                  (3.9)

Layer cake yields

`E|T-t|^(-alpha)
 =int_0^infinity P(|T-t|<s^(-1/alpha)) ds
 <=int_0^infinity min(1,A s^(-1/(2alpha))) ds`,                        (3.10)

where `A=4sqrt(KL)`. Since `alpha<1/2`, the last integral equals

`A^(2alpha)/(1-2alpha)=16^alpha(KL)^alpha/(1-2alpha)`.                  (3.11)

Taking the supremum in `t` proves (3.3), and `alpha=1/4` gives (3.4). QED.

## 4. A matrix-level weighted product replacement for a fiber supremum

### Corollary 4.1 — `QFORM-OFFDIAGONAL-ROW-QUARTER-RIESZ-v1`

Let

`S(X)=X^T C X+b^T X+c`                                                  (4.1)

be any quadratic-plus-affine form of independent cap-one original coordinates. Fix coordinate `k` and set

`sigma_k=(sum_(j!=k) C_kj^2)^(1/2)`.                                  (4.2)

If `sigma_k>0`, then

`boxed: H_(1/4)(S) <=4 e^(1/8) sigma_k^(-1/4).`                        (4.3)

### Proof

Write

`S=C_kk X_k^2+2X_k Z+W`,                                               (4.4)

where

`Z=sum_(j!=k) C_kj X_j+b_k/2`                                         (4.5)

and `W` contains every remaining quadratic, affine and constant term. The variable `X_k` is genuinely independent of `(Z,W)`. The normalized coefficient vector in (4.5) has Euclidean norm one, so the weighted product-projection theorem gives

`||p_Z||_infinity <=sqrt(e)/sigma_k`.                                  (4.6)

Apply Theorem 3.1 with `K=1`, `L=sqrt(e)/sigma_k`. Equation (3.4) becomes exactly (4.3). QED.

This is the desired weighted product-structure replacement: all coefficients in an original physical row are aggregated into `sigma_k` **before** the reciprocal quarter power is taken. No individual edge is selected, no spectral coordinate is declared independent, and no conditional fiber maximum is integrated.

## 5. Splice with the Claude hyperbola peel

### Theorem 5.1 — `QFORM-HYPERBOLA-ROW-AGGREGATION-v1`

Let a quadratic-plus-affine form have an exact physical pair `(i,j)` with

`A_ii=A_jj=0`, `A_ij=mu!=0`.                                          (5.1)

Complete that pair as in the source theorem, and let `S` be the full Schur remainder on the remaining original coordinates. If some row `k` of the quadratic matrix of `S` has off-diagonal norm `sigma_k>0`, then

`boxed:
 ||p_Q||_infinity
 <=2^(11/4) kappa e^(1/8)
   (|mu|^3 sigma_k)^(-1/4).`                                           (5.2)

Numerically the universal coefficient is `<6.135`.

### Proof

Apply the completed Claude inequality (2.1) and then Corollary 4.1:

`D(Q)
 <=2^(3/4)kappa |mu|^(-3/4) H_(1/4)(S)
 <=2^(3/4)kappa |mu|^(-3/4) [4e^(1/8)sigma_k^(-1/4)]`,                 (5.3)

which is (5.2). QED.

The remaining self-curvature, all other rows, all affine terms, and all additional spectrum inside `S` are retained. This is an essential-density statement; continuity is not claimed here.

## 6. Exact target adversary to single-edge extraction, and its repair

For every `N>=1`, let `A_N` be the block diagonal matrix consisting of

`H=[[0,1],[1,0]]`                                                       (6.1)

and the `(N+1)`-vertex star

`S_N=[[0,v^T],[v,0_N]]`, `v=(1/sqrt(N),...,1/sqrt(N))`.                (6.2)

Equivalently,

`Q_N=2X_1X_2 +(2/sqrt(N)) X_3 sum_(j=4)^(N+3) X_j`.                   (6.3)

The spectrum of `H` is `{1,-1}`. Since `||v||_2=1`, the spectrum of `S_N` is `{1,-1,0,...,0}`. Hence

`spec(A_N)={1,-1,1,-1,0,...,0}`,                                      (6.4)

so this is an exact target family with four eigenvalues of modulus one.

Every individual star edge has magnitude `N^(-1/2)->0`. Therefore the proposed intermediate reduction

> a low-third-volume star/tube survivor must contain one dimension-free physical coupling edge

is false even inside the exact QFORM target.

At the same time the aggregate center-row norm is

`sigma_3=(sum_(j=4)^(N+3) A_3j^2)^(1/2)=1`.                           (6.5)

Peel the physical hyperbolic pair `(1,2)`. Because the blocks are independent at the matrix level, its Schur remainder is exactly `S_N`. Theorem 5.1 gives, for **every** independent cap-one input law,

`boxed: ||p_(X^T A_N X)||_infinity
        <=2^(11/4) kappa e^(1/8)<6.135,`                               (6.6)

uniformly in `N`.

This family also sits exactly outside the partner's third-volume receiver: regarding the star as the cross block from its center to its leaves, that block has rank one, so

`Delta_3=0`.                                                           (6.7)

Thus partner r25's large-`Delta_3` theorem and the present theorem are genuinely complementary rather than duplicate payments. The r25 branch pays quantitative third-volume; the family (6.1)-(6.7) shows that its zero-third-volume survivor cannot be discarded and that aggregate one-row product structure can still pay it without a good local edge.

Classification of this construction: `CANDIDATE_REFUTED` for the single-edge extraction mechanism, **not** a counterexample to QFORM.

## 7. Endpoint obstruction: why the quarter-Riesz exponent cannot simply be raised

Theorem 3.1 deliberately stops below `alpha=1/2`. This is necessary under unchanged assumptions. Let independent

`X,C ~ Uniform[-1/2,1/2]`                                              (7.1)

and take

`T=X^2+2XC+C^2=(X+C)^2`.                                               (7.2)

Then

`E|T|^(-1/2)=E|X+C|^(-1)=infinity`,                                   (7.3)

because the density of `X+C` is positive at zero. Therefore a universal claim of the form

`H_(1/2)(aX^2+2XZ+W) <= C(K,L)`                                       (7.4)

is false, even for two independent cap-one uniforms and perfectly regular compact support. This repairs the tempting but invalid attempt to feed a single non-null star directly into a square peel, whose endpoint needs `H_(1/2)`.

Classification: `CANDIDATE_REFUTED` for the half-Riesz endpoint, not for the full QFORM conjecture.

## 8. Relation to the exact-null theorem and current proof map

The completed fleet02/B16 theorem at
`math-open-problems@5bf3d5e6765ecd1dd091fc7d862f6f04211c530f`
pays an exact null scalar against an arbitrary dependent projected pair by a weak-`L^(3/2)` kernel. The present theorem does something different but complementary: it permits an arbitrary nonzero scalar quadratic coefficient `a`, keeps the scalar genuinely independent, and replaces an arbitrary pair-density hypothesis by a **product-derived one-dimensional projection cap**. Its output is the subcritical `H_(1/4)` currency needed by a physical hyperbolic pair.

The current B06 case map is therefore:

1. partner r25: a quantitative `Delta_3` packet after an outer square is paid by (2.4)-(2.5);
2. exact zero-diagonal hyperbolic pair + Schur remainder with nonzero aggregate off-diagonal row: paid by (5.2);
3. exact target stars can have `Delta_3=0` and every individual edge tending to zero, but are still paid by (6.6);
4. a single non-null star does **not** furnish a universal half-Riesz endpoint, by (7.1)-(7.4).

The first unpaid implication is now:

`QFORM-LOW-DELTA3-NONZERO-DIAGONAL-OR-DIAGONAL-SCHUR-v1`:

in the surviving low-third-volume/rank-two tube, when no exact zero-diagonal physical hyperbola is available or every such Schur remainder is diagonal in the original coordinates, combine the nonzero physical diagonals, the product-preserving rank-two aggregate currencies, and the third large spectral direction without requiring a good single minor or a half-Riesz star endpoint.

## 9. Corrections and scope preserved

This proof does not use law-uniform pointwise quadratic Fresnel decay, independence after spectral rotation, unrestricted spectral-fiber suprema, arbitrary-joint coarea, positive moments of worst conditional projection caps, a universally good physical minor, or deletion of a small nonzero tail. The exact original-coordinate independence needed in Theorem 3.1 is stated and retained. The full conjecture and universal continuity conclusion remain open.

Independent review status: none performed for the new Theorems 3.1, 4.1 or 5.1 in this run; they are supporting analytic results pending review, not a full-proof candidate.
