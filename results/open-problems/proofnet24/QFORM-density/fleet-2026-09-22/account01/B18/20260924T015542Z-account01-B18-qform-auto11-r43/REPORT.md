# account01/B18 — zero-self singleton with rank-one complement curvature

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260924T015542Z-account01-B18-qform-auto11-r43`  
**Role:** Literature-to-proof transfer  
**Status:** `PROVED SUPPORTING TARGET-LEVEL THEOREM / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B18, 2026-09-24T01:55:42Z.
attacking: the newest account02/B18 zero-self near-rank-one / unit-complement collar; transfer a primary bounded-density theorem into a source-preserving cross-plus-curvature implication and quantify the actual remaining collar.

## 1. Scope and live correction boundary

The owner target remains unrestricted: independent real original coordinates with one-dimensional densities at most one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. Full QFORM remains open. This run proves a complete target-valid subbranch and applies a completed account02/B18 result to an actual inequality.

No moment, support, log-concavity, iid, centering, smoothness, post-rotation independence, arbitrary-joint coarea estimate, worst conditional-density cap, fixed-good-minor assertion, or deletion of a small nonzero quadratic term is used. Continuity is tracked separately and is not claimed by the new theorem.

The newest account02/B18 theorem `QFORM-ZEROSELF-COMPLEMENT-NORM-FUNNEL-v1` shows that for an ORIGINAL-coordinate split

`A=[[0,B],[B^T,C]]`,

with `s=s_3(A)` and `c=||C||op<s`, the second singular value of `B` obeys

`beta_2(B)^2 >= s(s-c)`,

and hence a completed two-cross-direction theorem gives

`||p_Q||infinity <= 2 sqrt(pi)/sqrt(s(s-c))`.

Its sharp boundary example is

`A_*=[[0,1,0],[1,0,0],[0,0,1]]`,

where `c=s=1` and the cross block has only rank one. The partner explicitly identifies the next debt as transferring the resulting unit complement curvature into a product-preserving receiver. The theorem below closes the entire **rank-one complement-curvature** version of that boundary, not just the displayed 3x3 endpoint.

## 2. Primary source matched at exact hypotheses

The external theorem used is Galyna Livshyts, Grigoris Paouris and Peter Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, Theorem 1.1 (Israel J. Math. 216 (2016), 877–889).

If `Y=(Y_1,...,Y_m)` has a genuine product probability density with each one-dimensional factor bounded by one and `W` is any `2 x m` matrix with orthonormal rows, then the two-dimensional marginal `WY` has joint density bounded by `2`. No moment, bounded-support, log-concavity, iid, centering, symmetry, or smoothness assumption is present. This is used only as a **joint density cap**; the two projected coordinates are never declared independent.

For a full-rank `2 x m` matrix `L`, whitening gives the immediate corollary

`||p_(LY)||infinity <= 2/sqrt(det(LL^T))`.                           (2.1)

Indeed `W=(LL^T)^(-1/2)L` has orthonormal rows and `LY=(LL^T)^(1/2)WY`. If `m=2`, the same bound is immediate directly from the original product density under a linear change of variables (with the sharper constant one before the harmless factor two), so there is no endpoint issue.

For literature scope comparison, Herry--Malicet--Poly's quadratic-form regularity results assume iid inputs representable as sufficiently smooth functions of a Gaussian field; those hypotheses do not match the owner's arbitrary non-iid rough cap-one class. I found no exact published theorem in this targeted check that closes all owner quantifiers. This is a hypothesis comparison only, not a novelty claim.

## 3. Completed designated-partner theorem actually used

The completed account02/B18 report at

`yspennstate/math-open-problems@ba2e2fbc9d22196f83c4ae35080e7f3d23a55fa1`

proves `QFORM-CAPPED-SCALAR-DEPENDENT-PAIR-v1`, by scaling the source-pinned account02/B16 null-scalar kernel.

If `S` has density cap `K`, `(C,D)` is independent of `S` and has arbitrary joint density cap `M`, and `beta,gamma` are nonzero, then

`T=2 beta S C + alpha C^2 + 2 delta C D + gamma D^2`

has an essentially bounded density with

`||p_T||infinity <= 3 (2 M K)^(2/3) |beta^2 gamma|^(-1/3).`          (3.1)

The coordinates `C,D` may be dependent. This is exactly the dependence pattern needed below.

## 4. New theorem: zero-self singleton + arbitrary rank-one complement

### Theorem `QFORM-ZEROSELF-RANK1-COMPLEMENT-CLOSURE-v1`

Let `X_0,Y_1,...,Y_m` be independent real random variables with probability densities bounded by one. Let `v in R^m` be a unit vector, `b in R^m`, and `c in R`. Consider

`A = [[0, b^T], [b, c v v^T]]`                                      (4.1)

and

`Q = 2 X_0 <b,Y> + c <v,Y>^2`.                                      (4.2)

Assume `A` has at least three eigenvalues of modulus at least `s>0`. Since `rank(A)<=3`, it then has exactly three nonzero eigenvalues. Then `Q` has an essentially bounded density and

`boxed: ||p_Q||infinity <= 3*4^(2/3)/s
                         = 7.559526299369239.../s.`                  (4.3)

In particular, at the owner's normalization `s=1`, every such target matrix satisfies

`||p_Q||infinity < 7.560`.                                           (4.4)

No continuity conclusion is asserted by this argument.

### Proof

Put

`a=<b,v>`,

`b_perp=b-a v`,

`rho=||b_perp||`.

If `rho=0`, then `b` is parallel to `v` and the range of `A` is contained in the two-dimensional span of the singleton coordinate and `v`, contradicting the existence of three nonzero eigenvalues. Hence `rho>0`. Also `c!=0`.

Let `w=b_perp/rho`. In the orthonormal range basis `(e_0,v,w)`, the restriction of `A` is

`H=[[0,a,rho],[a,c,0],[rho,0,0]]`.                                  (4.5)

A direct determinant expansion gives

`det H = -c rho^2`.                                                   (4.6)

Because all remaining directions are killed by `A`, the three nonzero eigenvalues of `A` are exactly the eigenvalues of `H`. Therefore

`|c| rho^2 = |det H|
            = |lambda_1 lambda_2 lambda_3|
            >= s^3`.                                                 (4.7)

Now define the two linear aggregates of the ORIGINAL `Y` bank

`C=<b,Y>`, `D=<v,Y>`.                                                (4.8)

Their coefficient matrix is

`L=[b^T;v^T]`,

and

`det(LL^T)=||b||^2||v||^2-<b,v>^2=rho^2`.                           (4.9)

By the source-valid whitening corollary (2.1), `(C,D)` has joint density cap

`M <= 2/rho`.                                                        (4.10)

The scalar `X_0` remains genuinely independent of the whole pair `(C,D)` because it is a disjoint ORIGINAL coordinate. Apply the completed account02/B18 theorem (3.1) with

`S=X_0`, `K=1`, `beta=1`, `alpha=delta=0`, `gamma=c`.

Then

`||p_Q||infinity
 <= 3 (2M)^(2/3)|c|^(-1/3)
 <= 3 (4/rho)^(2/3)|c|^(-1/3)
 = 3*4^(2/3)(|c|rho^2)^(-1/3)
 <= 3*4^(2/3)/s`,                                                   (4.11)

where the last inequality is (4.7). QED.

### Range-affine extension

The same bound survives deterministic affine terms in the three aggregate variables `X_0,<b,Y>,<v,Y>`. The quadratic `3 x 3` aggregate matrix is invertible (its determinant is `-c` after using `C=<b,Y>` as a coordinate), so a deterministic completion-of-squares translation removes such affine terms; translating the scalar separately and translating the pair jointly preserve the scalar/pair independence and density caps. This does **not** authorize arbitrary affine terms in directions of `Y` outside `span{b,v}`.

## 5. Actual application to the partner's sharp boundary endpoint

For

`A_*=[[0,1,0],[1,0,0],[0,0,1]]`,

we have `b=(1,0)`, `v=(0,1)`, `c=1`, `rho=1`, and spectrum `{-1,1,1}`. Thus Theorem 4 already gives

`||p_(X^T A_* X)||infinity <= 3*4^(2/3)<7.560`.                     (5.1)

But here the pair `(C,D)=(X_1,X_2)` consists of two literal ORIGINAL coordinates, so its joint product density has cap `M<=1`, sharper than the generic LPP cap `2`. Applying the completed account02/B18 inequality (3.1) directly gives the actual endpoint inequality

`boxed: ||p_(2X_0X_1+X_2^2)||infinity
       <= 3*2^(2/3)
       = 4.762203155904598... .`                                    (5.2)

This explicitly spends the designated partner theorem on the model state where its newest complement-norm funnel has `beta_2(B)=0` and therefore cannot itself produce a two-cross-direction estimate.

## 6. What this removes from the live obstruction

The newest partner funnel leaves a collar in which a zero-self physical bank has nearly rank-one cross coupling and the complement carries nearly unit curvature. The present theorem shows that the **exact rank-one complement-curvature endpoint is completely paid**, even when the complement direction `v` is arbitrarily delocalized in the original coordinates and even when `<b,v>` is arbitrary.

The mechanism is determinant-based but not a fixed-minor argument:

`three spectral directions  ==>  |c| ||P_(v^perp)b||^2 >= s^3`,      (6.1)

while LPP converts exactly the same transverse quantity into the pair-density denominator

`||p_(<b,Y>,<v,Y>)||infinity <= 2/||P_(v^perp)b||`.                 (6.2)

The exponents match the partner's null-scalar kernel and cancel to scale `s^(-1)`. The longitudinal component `<b,v>` disappears completely.

Therefore a genuine zero-self boundary obstruction must now involve at least one of the following:

1. complement curvature of rank at least two, or
2. an ambient/outside coupling whose induced affine term uses `Y` directions outside `span{b,v}`, or
3. a nonzero self block / source-entangled remainder not covered by the exact null-scalar receiver.

The full conjecture remains OPEN. In particular, (4.3) is not an ambient principal-block theorem under arbitrary outside conditioning; such conditioning may create a linear form of `Y` outside the two aggregate directions and the completed partner kernel does not permit replacing that dependence by a conditional density cap.

## 7. Continuity and source status

- Essential density bound: **proved** in the exact scope above.
- Continuity: **not claimed** by this new argument.
- Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.
- Primary theorem: Livshyts--Paouris--Pivovarov Theorem 1.1, exact product/cap hypotheses matched.
- Completed designated partner actually used: account02/B18 `QFORM-CAPPED-SCALAR-DEPENDENT-PAIR-v1`, source commit `ba2e2fbc9d22196f83c4ae35080e7f3d23a55fa1`, itself based on account02/B16 `QFORM-NULL-SCALAR-DEPENDENT-PAIR-v1` at `5bf3d5e6765ecd1dd091fc7d862f6f04211c530f`.
- Latest account02/B18 funnel actually applied/contextualized: `QFORM-ZEROSELF-COMPLEMENT-NORM-FUNNEL-v1`, commit `a105f60a5c5a1980a71eb45cc44e91f64acdb3fa`.
- I did not find an exact prior published solution to all owner quantifiers and make no literature-novelty claim for this supporting theorem.
