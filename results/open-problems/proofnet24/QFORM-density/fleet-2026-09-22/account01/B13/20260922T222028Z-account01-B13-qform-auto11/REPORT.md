SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 01, slot B13, 2026-09-22T22:20:28Z.
attacking: the one-heavy/two-transverse-bank endpoint by a phase-adapted slope-offset estimate and an exact-graph/null-pivot one-bank closure.

# account01/B13 auto11 — phase-adapted slope-offset lifting and one-bank exact-graph null-pivot closure

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T222028Z-account01-B13-qform-auto11`  
**Assignment:** Extremal product laws  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_TARGET_LEVEL_BRANCH / FULL-QFORM-OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

The full quadratic-form bounded-density conjecture remains OPEN. This report proves two source-coherent supporting statements. First, it upgrades the designated partner account02/B13 derivative-splitting theorem from a literal joint `L^infinity` assumption on the slope-offset pair to the weaker phase-adapted slanted-rectangle norm that its proof actually uses. Second, in the exact-rank-three near-null two-bank geometry, it shows that an **exact graph bank** already closes the null heavy-pivot endpoint by itself: the other bank and every other original coordinate may be conditioned away. No global light-cloud graph assumption is needed.

The argument keeps original-coordinate independence. It does not use arbitrary-joint coarea, conditional projection-density moments, post-rotation independence, a fixed good physical minor, law-uniform pointwise quadratic oscillatory decay, bounded support/diameter, a fixed fragment count, or the refuted one-heavy-square absorption mechanism.

## 1. Fresh dependencies and correction boundary

Fresh protected control remained owner revision `2026-09-22.15`, QFORM only. The full claim is still recorded OPEN. The live correction inbox was reread immediately before publication.

The designated partner actually applied is account02/B13. Two completed partner results are used.

1. `QFORM-SLOPE-OFFSET-LINF-v1`, canonical source

   `yspennstate/math-open-problems@fe0f6c26b4439e342a22a86450c8781b7543c9ec`,

   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260922T222622Z-account02-B13-extremal-741150/REPORT.md`.

   If `X` is independent of `(S,C)`, `||p_X||_infinity<=L`, `||p_(S,C)||_infinity<=M`, and

   `T=aX^2+bX+lambda S X+C`, `lambda!=0`,

   then

   `||p_T||_infinity<=4 sqrt(LM/|lambda|)`.

   Its proof splits according to the physical derivative `|2aX+b+lambda S|` and, in the small-derivative region, uses only a two-dimensional slope-offset rectangle estimate.

2. `QFORM-PRODUCT-BANGBANG-REDUCTION-v1`, canonical source

   `yspennstate/math-open-problems@604a08009638981da254a72f09a24dd50e3a3c94`.

   For every bounded measurable slab kernel, the supremum over arbitrary independent densities `0<=f_j<=1`, `int f_j=1`, equals the supremum over product indicators `1_{E_j}`, `|E_j|=1`. No single-interval, centered, bounded-diameter, or fixed-fragment conclusion is made.

The exact-rank-three geometric input is account03/B13 r17,

`yspennstate/math-open-problems@eac866b378f5c54411a55f7eb49f89336a4701ae`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B13/20260922T213118Z-account03-B13-qform-r17/REPORT.md`.

In its hard residual one has one heavy original coordinate `i`,

`r_i=sqrt(c)u`, `c>3/10`,

and two disjoint light original-coordinate banks `L_1,L_2`. For either bank write

`r_j=t_j u+p_j`, `p_j in u^perp`,

and

`G_a=sum_(j in L_a) p_j p_j^T >= kappa I_2`, `kappa=7/800`.

It also uses the exact regression decomposition

`t_j=w_a^T p_j+e_j`,
`sum e_j p_j=0`,
`rho_a=sum e_j^2`.

The completed zero-pivot nonlinear input used below is account01/B18
`QFORM-ZEROPIVOT-1PLUS2-DENSITY-v1`, canonical

`yspennstate/math-open-problems@dd94932dae1791af1bca9396c062e17d0e55142a`.

For a cap-one scalar independent of an arbitrary two-dimensional vector with joint density cap `M`, a nonsingular symmetric zero-pivot `3x3` quadratic matrix `H` gives density at most

`6 M^(2/3)|det H|^(-1/3)`.

The original written theorem is homogeneous quadratic. Section 3 below proves the affine extension needed after conditioning outside original coordinates, with the same constant.

## 2. The partner derivative split only needs a slanted-rectangle norm

For `0<alpha<=1` define the phase-adapted rectangle seminorm of a random pair `(S,C)` by

`R_alpha(S,C)`
` := sup P(S in J, C+theta S in I) / (|J| |I|^alpha)`,

where the supremum runs over all finite intervals `J,I` of positive length and every `theta in R`.

### Theorem 2.1 — `QFORM-SLOPE-OFFSET-EXPONENT-LIFT-v1`

Let `X` be independent of `(S,C)` with `||p_X||_infinity<=L`. Let

`T=aX^2+bX+lambda S X+C`, `lambda!=0`.

If

`R_alpha(S,C)<=M_alpha`,

then for every interval `I` of length `ell`,

`boxed: P(T in I)
 <=4 sqrt(L M_alpha/|lambda|) ell^((1+alpha)/2).`                 (2.1)

For `alpha=1` this is exactly the designated partner's density theorem, but the hypothesis is weaker than a literal joint-density cap because it tests only slanted rectangles of the form actually generated by the phase.

#### Proof

Fix `R>0` and split according to

`D(x,s)=2ax+b+lambda s`.

On `|D|<=R`, for fixed `x`, the variable `s` lies in an interval of length `2R/|lambda|`. The slab condition

`a x^2+b x+lambda sx+C in I`

is equivalent, for this fixed `x`, to

`C+(lambda x)S in I_x`

for an interval `I_x` of length `ell`. Therefore the definition of `R_alpha` gives

`P(T in I, |D|<=R)
 <=(2M_alpha R/|lambda|) ell^alpha`.                              (2.2)

On `|D|>R`, fix `(s,c)`. The quadratic in `x` has at most two monotone branches; on each branch the inverse derivative is at most `1/R`. Hence the total preimage length of a slab of length `ell` is at most `2ell/R`, and

`P(T in I, |D|>R)<=2L ell/R`.                                   (2.3)

Combining,

`P(T in I)<=2M_alpha R ell^alpha/|lambda|+2L ell/R`.

Choose

`R=sqrt(L|lambda|/M_alpha) ell^((1-alpha)/2)`.

The two terms coincide and (2.1) follows. QED.

This is a direct mathematical application of the latest account02/B13 proof mechanism, not merely a citation. It identifies the exact object that can replace the too-strong global `L^infinity` cap of `(S,C)`.

## 3. Affine zero-pivot 1+2 theorem

Conditioning original coordinates outside an active block produces arbitrary affine terms. The following extension makes the zero-pivot compiler directly usable without a hidden translation assumption.

### Theorem 3.1 — `QFORM-AFFINE-ZEROPIVOT-1PLUS2-v1`

Let `X` have density at most one and be independent of a two-dimensional vector `Y` having arbitrary joint density cap `M`. Let

`H=[[0,ell^T],[ell,B]]`

be real symmetric and nonsingular. For arbitrary `d in R^3` and `c_0 in R`,

`Q=(X,Y)^T H(X,Y)+2d^T(X,Y)+c_0`

has a continuous density satisfying

`boxed: ||p_Q||_infinity<=6 M^(2/3)|det H|^(-1/3).`             (3.1)

#### Proof

Rotate only the already-joint two-dimensional `Y` space so that `ell=(L,0)`, `L>0`. This does not assert independence inside `Y` and preserves its joint density cap. Write `Y=(u,v)` and the lower block as `[[b11,b12],[b12,b22]]`. Nonsingularity gives

`det H=-L^2 b22`, so `beta:=b22!=0`.

Apply the determinant-one shear

`w=v+(b12/beta)u`.

The joint density of `(u,w)` still has cap `M`. Completing the square in `w` removes its affine term by a fixed translation. The form becomes

`Q=beta w^2+alpha u^2+(2Lu+gamma)X+eta u+c_1`,                  (3.2)

for constants `alpha,gamma,eta,c_1`. Put

`u_0=-gamma/(2L)`.

For almost every fixed `u`, let `h_u(t)` be the unnormalised output density after integrating in `(X,w)`.

**Away from the coupling zero.** For fixed `(u,w)`, the map in `X` is affine with slope `2L(u-u_0)`. If `m(u)` is the `u`-marginal of the transformed pair density,

`h_u(t)<=m(u)/(2L|u-u_0|)`.                                    (3.3)

**Near the coupling zero.** For fixed `(X,u)`, the square `beta w^2` has the usual two-root density envelope

`M/(sqrt(|beta|) sqrt(|s|))`.

The cap-one rearrangement estimate

`sup_a int f_X(x)|a-cx|^(-1/2)dx<=2sqrt(2)|c|^(-1/2)`

with `c=2L(u-u_0)` yields

`h_u(t)<=2M [|beta|L]^(-1/2)|u-u_0|^(-1/2)`.                    (3.4)

Split the `u`-integral at `|u-u_0|=r`. Equation (3.4) gives

`8M sqrt(r)/sqrt(|beta|L)`

inside, while (3.3), using `int m=1`, gives

`1/(2Lr)`

outside. Optimising `A/r+B sqrt(r)` yields

`p_Q(t)<=6 M^(2/3)(|beta|L^2)^(-1/3)
       =6 M^(2/3)|det H|^(-1/3)`.

The same integrable split gives dominated convergence in `t`; hence the density is continuous. QED.

The only new point relative to the earlier homogeneous theorem is that the zero of the coupling is translated from `u=0` to `u=u_0`; the determinant payment and exponents are unchanged.

## 4. One exact graph bank already closes the null-pivot endpoint

Return to the account03/B13 hard exact-rank-three geometry. Fix either light bank `L_a`. Assume only

`rho_a=sum_(j in L_a)e_j^2=0`.                                    (4.1)

Then every `e_j=0`, so

`t_j=w_a^T p_j` for all `j in L_a`.                              (4.2)

Thus the whole bank spectral vector is an exact graph over its two-dimensional transverse projection.

Let

`Z=sum_(j in L_a) p_j X_j in u^perp`.

Because the original coordinates in `L_a` are independent and cap one, the two-dimensional product-marginal theorem gives

`||p_Z||_infinity<=2/sqrt(det G_a)<=2/kappa=1600/7`.             (4.3)

Define the graph map

`T_a z=z+(w_a^T z)u`.

Equation (4.2) says

`sum_(j in L_a) r_j X_j=T_a Z`.                                 (4.4)

Now condition on **all original coordinates outside** `{i} union L_a`. The remaining variables are the untouched original scalar `X_i` and the bank projection `Z`; hence `X_i` is genuinely independent of the whole vector `Z`. The conditioning contributes only affine and constant terms.

Choose an orthonormal basis `(u,e_1,e_2)` of spectral space. The active spectral map from `(x,z_1,z_2)` is

`F=[sqrt(c)u, T_a e_1, T_a e_2]`.

In this basis its matrix is triangular,

`[[sqrt(c), w_1, w_2],
  [0,       1,   0],
  [0,       0,   1]]`,

so

`det F=sqrt(c)`.                                                  (4.5)

Let

`H=F^T Lambda F`.

Then

`det H=c det Lambda`.                                            (4.6)

Moreover the heavy physical pivot is

`H_11=c alpha`, `alpha=u^T Lambda u`.                            (4.7)

Therefore, in the exact null-pivot case

`alpha=0`,                                                       (4.8)

`H` is a nonsingular zero-pivot `3x3` matrix, because

`|det H|=c|det Lambda|>=c>3/10`.                                 (4.9)

Apply Theorem 3.1 with the pair cap (4.3). Uniformly in every outside conditioning value,

`||p_Q||_infinity
 <=6 (2/kappa)^(2/3) (c|det Lambda|)^(-1/3)
 <6 (1600/7)^(2/3)(10/3)^(1/3)
 =335.0622191722... .`                                           (4.10)

Averaging the conditional densities preserves the same bound.

### Theorem 4.1 — `QFORM-ONEBANK-EXACTGRAPH-NULLPIVOT-CLOSURE-v1`

In the account03/B13 hard exact-rank-three two-bank geometry, if the heavy spectral pivot is exactly null, `u^T Lambda u=0`, and **either one** of the two light banks has zero longitudinal regression residual `rho_a=0`, then for every admissible cap-one product input law

`boxed: ||p_Q||_infinity<335.063.`                               (4.11)

The density is continuous on this conditioned exact-rank-three branch.

The other light bank does not need to be a graph and need not have any small conditional density: it is simply conditioned away in original coordinates. This is the structural gain over a global-light-cloud graph endpoint.

## 5. Direct use of the latest slope-offset gate on the same branch

The exact graph geometry also supplies the phase-adapted slanted-rectangle control requested by the latest account02/B13 handoff.

Rotate only the joint `Z`-plane so that the heavy-to-bank cross vector points along the first coordinate. In variables `(x,s,y)`, the active zero-pivot quadratic matrix has the form

`H=[[0,L,0],[L,m11,m12],[0,m12,beta]]`,

with

`|det H|=L^2 |beta|`.                                            (5.1)

Let `M_0=||p_(S,Y)||_infinity`, so `M_0<=2/kappa`. Write the bank offset, including arbitrary affine terms, as

`C=m11 S^2+2m12 SY+beta Y^2+d_sS+d_yY+c`.

For every fixed `s`, every `theta`, and every interval `I` of length `ell`, the set of `y` satisfying

`C+theta S in I`

has length at most

`2 sqrt(ell/|beta|)`.                                           (5.2)

Hence for every `S`-interval `J`,

`P(S in J, C+theta S in I)
 <=2M_0 |J| sqrt(ell/|beta|)`.                                  (5.3)

Thus Theorem 2.1 applies with

`alpha=1/2`, `M_(1/2)=2M_0/sqrt(|beta|)`, `lambda=2L`,

and gives the explicit target-valid intermediate bound

`boxed:
P(Q in I)
 <=4 M_0^(1/2)|det H|^(-1/4)|I|^(3/4).`                         (5.4)

Using `M_0<=2/kappa` and `|det H|>3/10`,

`P(Q in I)<81.713 |I|^(3/4)`.                                  (5.5)

This is an actual application of the designated partner's derivative/slope-offset mechanism to the live two-bank geometry. The affine zero-pivot theorem of Section 3 then improves the same exact-graph/null-pivot branch from exponent `3/4` to the linear estimate (4.11). The reason the stronger step is possible is that the exact graph provides the full two-dimensional joint bank density before any reciprocal derivative is paid.

## 6. Geometric extremal-product formulation

Apply the designated account02/B13 bang-bang theorem to the new linear estimate. In the branch of Theorem 4.1, for every collection of arbitrary measurable sets `E_j subset R` with `|E_j|=1` and every interval `J`,

`boxed:
|{x in product_j E_j : x^T A x in J}| <335.063 |J|.`            (6.1)

Conversely, the partner theorem transfers this slab inequality with zero loss to all independent cap-one product densities. No interval, centering, bounded-diameter, or bounded-fragment restriction is present.

This is the B13 geometric sublevel-set conclusion for the newly closed endpoint.

## 7. Exact scope and first unpaid implication

The result closes only the exact-rank-three branch

`alpha=0` and `min(rho_1,rho_2)=0`

inside the already-reduced one-heavy/two-transverse-bank geometry. It does **not** prove the full exact-rank-three theorem, and it does not address arbitrary additional spectral directions.

The first remaining endpoint is therefore genuinely two-sided:

`QFORM-NEARNULL-TWOBANK-POSITIVE-RESIDUAL-CLOSURE-v1`:

> retain `|alpha|` small but nonzero or `rho_1,rho_2>0`, and use the two banks' transverse curvature plus residual leakage to obtain a linear slab bound without conditioning a projected variable and without dividing by an individual diffuse coefficient.

Theorem 2.1 identifies a precise sufficient currency for that step: a linear (`alpha=1`) phase-adapted slanted-rectangle estimate for the actual slope-offset pair, or a replacement nonlinear estimate that integrates the two residual leakages before reciprocal derivative payment. The exact-graph/null-pivot endpoint no longer needs to be included in that interpolation.

After exact rank three is closed, arbitrary additional spectrum remains a separate full-target bridge.

## 8. Status

- `QFORM-SLOPE-OFFSET-EXPONENT-LIFT-v1`: **PROVED**.
- `QFORM-AFFINE-ZEROPIVOT-1PLUS2-v1`: **PROVED**.
- `QFORM-ONEBANK-EXACTGRAPH-NULLPIVOT-CLOSURE-v1`: **PROVED SUPPORTING TARGET-LEVEL BRANCH**.
- designated account02/B13 slope-offset mechanism: **APPLIED TO (5.4)**.
- designated account02/B13 bang-bang theorem: **APPLIED TO (6.1)**.
- full exact-rank-three conjecture: **OPEN**.
- full owner QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.

No numerical experiment is used as proof. The displayed constants come from exact inequalities; decimal values are only evaluations.
