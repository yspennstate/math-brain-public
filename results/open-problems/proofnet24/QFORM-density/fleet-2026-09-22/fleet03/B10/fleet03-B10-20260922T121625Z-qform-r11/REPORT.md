# fleet03/B10 — rank-three coupled case: optimized Schur smoothing and an aggregate hyperbolic closure

**Run:** `fleet03-B10-20260922T121625Z-qform-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** `Rank-three coupled case`  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREMS / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and fresh source state

The target is one universal constant `C<infinity` such that, for every dimension, every independent real coordinate family with densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues satisfying `|lambda_j(A)|>=1`, the law of `X^T A X` has essential density at most `C`.

The live corrections were enforced: no law-uniform pointwise Fresnel decay, no spectral-coordinate independence, no naive fiber-supremum completion, and no reciprocal local-minor averaging. The named fleet04/B10 partner had no completed current-QFORM handoff at both the startup and prepublication reads, so no partner result is invented. I instead apply two completed compatible sources: fleet01/B10's heavy-row Schur theorem and fleet03/B09's source-valid two-dimensional projection-density cap, together with the current interactive cross-block/diffuse state.

The fleet01/B10 source is `math-open-problems@0a73ea76664e609dd164a3e0f397230ae8c17d4f`, which proves, in the residual-diffuse heavy-row branch, an `L^3` density estimate for the rank-two Schur remainder. The fleet03/B09 source is `math-open-problems@41fc39eccdd44a0dcae6619676bf41f5ea21bb3e`; its use of the Livshyts--Paouris--Pivovarov projection theorem gives density at most `2` for any two-dimensional orthogonal projection of the original product law.

## 2. A dependence-tolerant hyperbolic-square theorem

The first new lemma removes independence between the two variables that supply the hyperbolic partner and the third square. Independence is retained only where it is actually available in the original coordinates.

### Theorem 2.1 — `QFORM-DEPENDENT-PAIR-HYPERBOLIC-SQUARE-v1`

Let `X` be a real random variable with probability density `f_X<=1`. Let `(Y,Z)` be an arbitrary two-dimensional random vector, independent of `X`, with a joint probability density `h` satisfying `||h||_infinity<=H`. Let `a,b` be nonzero and let `F,theta:R->R` be arbitrary measurable functions. Then

`T = 2 a X Y + F(Y) + b (Z+theta(Y))^2`

has an essentially bounded density and

`||p_T||_infinity <= 3*2^(2/3) H^(2/3) |a|^(-2/3) |b|^(-1/3)`.        (2.1)

No independence of `Y` and `Z` is assumed.

#### Proof

Write `m(y)=int h(y,z) dz`, so `m>=0` and `int m=1`. Fix an output point `t` and decompose its density contribution as `p_T(t)=int j_t(y)dy`.

First integrate in `z`. For fixed `(x,y)`, the two roots of the square map and the bound `h<=H` give

`int h(y,z) delta(t-2axy-F(y)-b(z+theta(y))^2) dz`

` <= H |b|^(-1/2) [sigma(t-2axy-F(y))]_+^(-1/2)`,

where `sigma=sign(b)`. The sharp one-sided rearrangement bound for a probability density bounded by one gives

`int f_X(x)[s-2axy]_+^(-1/2)dx <= sqrt(2) |a|^(-1/2)|y|^(-1/2)`.

Hence

`j_t(y) <= sqrt(2) H |ab|^(-1/2)|y|^(-1/2)`.                         (2.2)

Second, integrate in `x` first. For `y!=0`, the map is affine in `x`, so

`j_t(y) <= m(y)/(2|a||y|)`.                                           (2.3)

For any `R>0`, use (2.2) on `|y|<=R` and (2.3) outside. Since

`int_{-R}^R |y|^(-1/2)dy=4 sqrt(R)`

and `int m=1`,

`p_T(t) <= [4 sqrt(2)H/sqrt(|ab|)] sqrt(R) + [1/(2|a|R)]`.            (2.4)

Minimizing the right side in `R` yields exactly

`3*2^(2/3) H^(2/3)|a|^(-2/3)|b|^(-1/3)`.

The estimate is independent of `t`; the same disintegration proves absolute continuity. QED.

This is strictly more dependence-tolerant than the previously completed physical-coordinate theorem `QFORM-HYPERBOLIC-SQUARE-v1`: only the isolated variable `X` must remain independent of the pair `(Y,Z)`.

## 3. New closed rank-three boundary case: a leverage-one isotropic physical pivot

Consider rank exactly three

`A=U Lambda U^T`, `U^T U=I_3`, `|lambda_k|>=1`.

Let physical row `u_i` have leverage one: `||u_i||^2=1`. Write `e=u_i`, and suppose it is isotropic for the spectral quadratic form:

`alpha=e^T Lambda e=0`.                                                (3.1)

Because the frame is Parseval and `||u_i||=1`, every other row is orthogonal to `e`. Put `beta=P_{e^perp}Lambda e`, `B=||beta||`. Since `Lambda` is invertible, `B>0`; in fact `B=||Lambda e||>=1`. Choose an orthonormal basis `(f,g)` of `e^perp` with `f=beta/B`. In the basis `(e,f,g)`,

`Lambda = [[0,B,0],[B,r,s],[0,s,tau]]`.                               (3.2)

Its determinant is

`det Lambda = -B^2 tau`,                                                (3.3)

so

`B^2 |tau|=|det Lambda|>=1`.                                            (3.4)

Define the residual spectral coordinates

`Y=sum_{j!=i} <u_j,f> X_j`, `Z=sum_{j!=i}<u_j,g>X_j`.

The coefficient vectors of `Y,Z` are orthonormal in the original residual coordinate space. Therefore the completed fleet03/B09/Livshyts--Paouris--Pivovarov projection estimate gives their joint density cap

`||p_(Y,Z)||_infinity <=2`.                                             (3.5)

Moreover `X_i` is independent of `(Y,Z)`. The entire quadratic form is exactly

`Q=2B X_iY+rY^2+2sYZ+tau Z^2`

` =2B X_iY +(r-s^2/tau)Y^2 + tau(Z+(s/tau)Y)^2`.                       (3.6)

Apply Theorem 2.1 with `H=2`, `a=B`, `b=tau`. Using (3.4),

`||p_Q||_infinity`

` <=3*2^(4/3)(B^2|tau|)^(-1/3)`

` <=3*2^(4/3) < 7.560`.                                                 (3.7)

Thus the exact leverage-one/isotropic-pivot rank-three branch is now closed for arbitrary original-coordinate input densities bounded by one, despite the fact that the projected pair `(Y,Z)` need not be independent.

## 4. Optimizing the inherited heavy-row Schur estimate

Now use the completed fleet01/B10 heavy-row setup. Let `u_i=sqrt(c)e` with `c>1/2`, `alpha=e^T Lambda e !=0`, and assume every residual leverage in `e^perp` is at most `1/2`. Fleet01/B10 proves that after completing the heavy coordinate,

`Q=a(X_i+s)^2+R`, `a=c alpha`,

and the rank-two Schur remainder has

`||p_R||_3 <= (3e)^(2/3) D^(-1/3)`, `D=|det Lambda|/|alpha|`.           (4.1)

It also proves the one-sided envelope

`p_Q(y) <= |a|^(-1/2) int_0^infinity u^(-1/2)p_R(y-sign(a)u)du`.        (4.2)

The previous source split (4.2) at `u=1`. Optimizing the split gives a strictly stronger estimate. For arbitrary `R0>0`, Holder on `(0,R0)` and mass one on the tail give

`int_0^infinity u^(-1/2)p_R(y-sign(a)u)du`

` <= (12e)^(2/3)D^(-1/3) R0^(1/6)+R0^(-1/2)`.                         (4.3)

The minimum occurs at

`R0=(3/K)^(3/2)`, `K=(12e)^(2/3)D^(-1/3)`,

and equals

`4*3^(-3/4)K^(3/4)`.

Hence

`||p_Q||_infinity`

` <= [8 sqrt(e)/3^(1/4)] c^(-1/2)|alpha|^(-1/4)|det Lambda|^(-1/4)`.   (4.4)

The numerical prefactor is `10.022058...`. Since `c>1/2` and `|det Lambda|>=1`,

`||p_Q||_infinity <14.174 |alpha|^(-1/4)`.                             (4.5)

At the old cutoff `|alpha|>=1/2`, this improves the inherited `<22.419` constant to `<16.856`. More importantly, the singularity of this mechanism near the isotropic pivot is reduced from `|alpha|^(-1/2)` to `|alpha|^(-1/4)`.

This still does **not** close `alpha->0`; Section 3 closes only the genuinely product-preserving boundary case `c=1, alpha=0`.

## 5. Exact original-coordinate resource in the remaining small-alpha branch

The small-alpha branch carries a substantial aggregate physical row resource that does not require residual diffuseness.

Let `b=(A_ij)_{j!=i}`. Since

`A_ii=c alpha`

and

`(A^2)_ii=u_i^T Lambda^2u_i=c||Lambda e||^2>=c`,

we have the exact identity/inequality

`||b||_2^2=c||Lambda e||^2-c^2 alpha^2 >= c(1-c alpha^2)`.              (5.1)

Therefore, whenever `c>1/2` and `|alpha|<1/2`,

`||b||_2^2 > 7/16`.                                                     (5.2)

At the exact isotropic pivot `alpha=0`, the geometry is sharper. With `beta`, `B`, `f`, `g` as above but now allowing any `c>1/2`, define the physical residual vector

`z_j=<u_j,g>`, `j!=i`.

Then `||z||_2=1`, `z perpendicular b`, and if `C=A[-i,-i]`,

`z^T C z=tau`,

while

`||b||_2^2=cB^2`, `det Lambda=-B^2 tau`.                               (5.3)

Consequently

`||b||_2^2 |z^T C z| = c |det Lambda| >= c >1/2`.                     (5.4)

This is an exact **zero-pivot plus transverse-curvature aggregate certificate** in the original physical coordinate space. It is the rank-one analogue of the current fleet02/B20 zero-pivot packet theorem, but with the missing third-direction curvature recorded explicitly rather than replaced by a local minor.

## 6. What remains unpaid

The rank-three target is still OPEN. The first genuinely narrowed obstruction is now:

`QFORM-ONE-HEAVY-ISOTROPIC-LEAKAGE-v1`.

For a heavy row `c in (1/2,1)` with `alpha=0`, write the residual rows as

`u_j=s_j e+w_j`,

so `sum s_j^2=1-c`, `sum s_j w_j=0`, and the two-dimensional `w_j` form a Parseval frame. In the normalized spectral basis above the form is

`Q=2B( sqrt(c)X_i + T )Y + rY^2+2sYZ+tau Z^2`,                       (6.1)

where `T=sum s_jX_j` is generally dependent on `(Y,Z)`. The exact invariants are

`B^2|tau|=|det Lambda|>=1`,                                            (6.2)

and the physical certificate (5.4).

When `c=1`, `T=0` and Theorem 2.1 closes the branch. For `c<1`, simply absorbing `T` into `X_i` destroys the one independence relation used in Theorem 2.1. A bounded joint spectral density is known to be insufficient (the current cone-shell falsifier), so this dependence cannot be discarded.

The next target is therefore a product-preserving **one-zero-pivot plus aggregate transverse-curvature theorem** that uses the original independent residual coordinates and the orthogonality identities `sum s_j w_j=0`, rather than a spectral joint-density surrogate or a reciprocal local minor. Proving that theorem would close the exact `alpha=0` heavy-row obstruction; (4.4) already handles every fixed nonzero `alpha` quantitatively.

## 7. Scope

- Theorem 2.1: proved.
- Leverage-one isotropic rank-three branch: proved with density cap `<7.560`.
- Optimized Schur estimate (4.4): proved from the completed fleet01/B10 remainder theorem.
- Aggregate zero-pivot/transverse-curvature certificate (5.4): proved.
- Arbitrary heavy `c<1`, `alpha=0`: open.
- Rank exactly three in full generality: open.
- The owner's arbitrary-rank target with possible additional small eigenvalues: open.

No projected variables were declared independent, no pointwise oscillatory-decay claim was used, and no local reciprocal-minor average was used.
