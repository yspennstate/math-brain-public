SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B14, 2026-09-24T04:49:43Z.
attacking: pushforward-height localization — localize an already aggregated random slope by its density height rather than by spatial teeth, then apply the completed fleet02/B14 transverse-vertex theorem to a diffuse exact-target star-square chamber.

# fleet01/B14 — pushforward-height localization and a diffuse rank-three star-square chamber

Run: `20260924T044943Z-fleet01-B14-auto11`.

Status: **NEW ZERO-LOSS LOCALIZATION LEMMA + TARGET-VALID PARTNER APPLICATION / FULL QFORM OPEN / WITHOUT_VERIFIED_BRAIN**.

The owner target remains the unrestricted statement for independent original-coordinate variables with probability densities at most one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one. No moment, centering, support, connectedness, log-concavity, iid, diagonal-basis, or post-rotation-independence assumption is introduced below. The known law-uniform pointwise quadratic Fourier decay is not used.


## 1. A localization object that is already aggregated

Spatially splitting an active law can be disastrous when the analytic compiler contains a sublinear mass power. The designated partner's latest exact-target example makes that explicit: a whole random slope has a uniform certificate, whereas paying its remote teeth separately can cost `sqrt(N)` or diverge for a countable comb. The correct object to localize is therefore not a spatial fragment of the source bank but the **height of the already aggregated one-dimensional slope density**.

For a finite positive measure `eta` on the output line define

`Lambda(eta) := sup_{a<b} eta((a,b))/(b-a)`.

This is positive homogeneous and subadditive; `Lambda(eta)<infinity` implies `eta` has a density bounded a.e. by `Lambda(eta)`.

## 2. New theorem: pushforward-height localization

### Theorem `QFORM-PUSHFORWARD-HEIGHT-LOCALIZATION-v1`

Let `Omega` be a standard Borel space, let `tau` be a finite positive measure on `Omega` with mass `m`, and let `S:Omega->R` be measurable. Assume

`S_# tau = h(s) ds`,     `0<=h<=M<infinity`.                       (2.1)

Let `T` be a positive linear map from finite positive measures on `Omega` to finite positive measures on `R`. Fix `0<alpha<=1`. Suppose that whenever a finite positive measure `nu` has

`S_# nu = 1_E(s) ds`                                           (2.2)

for a measurable finite-measure set `E`, one has the compiler estimate

`Lambda(T nu) <= C |E|^alpha`.                                 (2.3)

Then

`boxed: Lambda(T tau) <= C M^(1-alpha) m^alpha.`                (2.4)

In particular, if `m=M=1`, the **identical constant `C`** holds. There is no dependence on support radius, number of connected components, separation of components, translations, tails, or moments. The sets occurring in the proof may themselves be arbitrarily disconnected and unbounded.

### Proof

Disintegrate `tau` over the map `S`:

`tau(d omega) = K_s(d omega) h(s) ds`,                          (2.5)

where `K_s` is a conditional probability kernel on the fibers `S=s` for `h(s)ds`-a.e. `s`. For `0<u<M`, define the positive finite measure

`nu_u(B) := integral_{h(s)>u} K_s(B) ds`.                       (2.6)

Since `h(s)>u` implies equivalence of `h(s)ds` and `ds` null sets on that region, the fiber support identity gives

`S_# nu_u = 1_{ {h>u} }(s) ds`.                                (2.7)

Write

`m(u):=nu_u(Omega)=|{s:h(s)>u}|`.

Layer cake, now on the pushforward density rather than on the original spatial source, gives the exact measure identity

`tau = integral_0^M nu_u du`,                                  (2.8)

because for every measurable `B`,

`integral_0^M nu_u(B) du
 = integral K_s(B) [integral_0^M 1_{u<h(s)} du] ds
 = integral K_s(B) h(s) ds
 = tau(B)`.

Also

`integral_0^M m(u) du = integral h(s) ds = m`.                  (2.9)

For any interval `I`, positivity and linearity give

`T tau(I)=integral_0^M T nu_u(I) du
 <= C |I| integral_0^M m(u)^alpha du`.

Since `x^alpha` is concave,

`integral_0^M m(u)^alpha du
 <= M^(1-alpha) [integral_0^M m(u) du]^alpha
 = M^(1-alpha)m^alpha`.                                        (2.10)

Taking the interval supremum proves (2.4). QED.

### Why this is different from source-density layer cake

The measure `nu_u` need not be a product law internally. The theorem is useful exactly when the downstream receiver theorem only needs the **aggregate scalar pushforward** `S_#nu_u` and independence of the entire environment from the receiver coordinates. Thus one may first aggregate a large original-coordinate product bank into a one-dimensional random slope, and only then localize its density height. No reciprocal minor or singular kernel is paid on individual spatial teeth.

## 3. The latest designated-partner theorem, in the form used here

Fresh completed partner source:

`fleet02/B14`, canonical proof
`yspennstate/math-open-problems@24ce9b1a9e5691e12a7d9f02d7cf455cb8850862`
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B14/20260924T040328Z-fleet02-B14-QFORM-auto11/REPORT.md`.

Its theorem `QFORM-TRANSVERSE-VERTEX-SUBPROBABILITY-COMPILER-v1` says: if `W,U` are independent probability laws with density caps `K_W,K_U`, `tau` is an independent positive environment measure of mass `m`, and the unnormalized pushforward of `S=S(Z)` has density cap `L_S`, then for arbitrary measurable `Phi(U,Z)`, arbitrary `R(Z)`, and `a!=0`, the output submeasure of

`a(W+Phi(U,Z))^2 + 2S(Z)U + R(Z)`                              (3.1)

satisfies

`boxed: ||p_eta||_inf <= 4 K_W sqrt(K_U/|a|) sqrt(m L_S).`      (3.2)

For a probability environment, `m=1`. Its whole-anchor theorem explains when arbitrary complementary fragmentation is mass-linear; its remote-comb example proves that spatial tooth normalization can instead create a false `sqrt(N)` tax.

Applying Theorem 2 above to (3.2) with `alpha=1/2` reconstructs the whole-slope inequality from flat-height layers with **no loss**: if `S_#tau=h ds`, `||h||_inf<=M_S`, then each `nu_u` has slope cap one and

`Lambda(T nu_u) <= 4 K_W sqrt(K_U/|a|) m(u)^(1/2)`.

Hence

`boxed: ||p_Q||_inf <= 4 K_W sqrt(K_U M_S/|a|).`                (3.3)

This derivation is valid even if `h` has arbitrarily many remote components or unbounded support.

## 4. Actual strict-target application: diffuse star-square chamber

Let `W,U,Z_1,...,Z_m` be mutually independent real variables, each with probability density at most one. Let `c in R^m`,

`r:=||c||_2>0`,

and let `a!=0`. Consider the homogeneous active form

`Q_0 = a(W+U)^2 + 2U c^T Z`.                                   (4.1)

Its original-coordinate matrix is

`A(a,c)= [[a,a,0], [a,a,c^T], [0,c,0_m]]`.                    (4.2)

The `m-1` directions in the `Z`-bank orthogonal to `c` are zero modes. On `span{W,U,c/r}`, the nonzero compression is

`M(a,r)= [[a,a,0],[a,a,r],[0,r,0]]`.                           (4.3)

Changing `Q_0` to `-Q_0` preserves the output-density norm and all eigenvalue moduli, so assume `a>0` below.

The characteristic polynomial is

`p(lambda)=lambda^3-2a lambda^2-r^2 lambda+a r^2`.             (4.4)

Since `det M=-a r^2<0` and `tr M=2a>0`, there is exactly one negative eigenvalue and two positive eigenvalues.

### Lemma: exact three-threshold condition for this chamber

All three nonzero eigenvalues of `M(a,r)` have modulus at least one **iff**

`a>1`,
`r^2 >= (2a-1)/(a-1) = 2 + 1/(a-1)`.                          (4.5)

Proof. The unique negative root is at most `-1` iff

`p(-1)=(a+1)r^2-(2a+1)>=0`.                                  (4.6)

For the smaller positive root to be at least one one needs `p(1)>=0`, once the larger positive root is known to exceed one. The simultaneous inequalities `p(-1)>=0` and `p(1)>=0` force `a>1`: if `a<=1`, the two required ranges of `r^2` are incompatible (and at `a=1`, `p(1)=-1`). For `a>1`, the top-left `2x2` principal block has eigenvalue `2a>2`, so interlacing gives the larger positive root `>1`. Therefore

`p(1)=1-2a+(a-1)r^2>=0`                                      (4.7)

is exactly the smaller-positive-root condition. It is (4.5), and its right side exceeds the threshold in (4.6) by

`2a/(a^2-1)>0`,

so (4.6) is then automatic. QED.

## 5. A quantitative spectral invariant for this chamber

The target condition (4.5) forces a nontrivial lower bound on the **aggregate product** `a r`, even though every individual coordinate coupling `c_j` may be arbitrarily small.

Put `x=r^2>2`. On the boundary of (4.5),

`a=(x-1)/(x-2)`.

For fixed `x`, this is the smallest admissible `a`, so minimize

`F(x)=sqrt(x)(x-1)/(x-2)`,     `x>2`.                          (5.1)

A logarithmic derivative gives

`F'(x)/F(x)=1/(2x)+1/(x-1)-1/(x-2)`.

The critical equation is

`x^2-5x+2=0`.

Only

`x_*=(5+sqrt(17))/2`                                          (5.2)

lies above two, and `F(x)->infinity` at both endpoints `2+` and `infinity`, so this is the global minimum. At the minimizer

`a_*=(7+sqrt(17))/8`,                                         (5.3)

and

`boxed: a r >= mu_* := (1/4)sqrt(71+17sqrt(17))
                    = 2.969562211373718... .`                 (5.4)

This is a spectral consequence of the exact three-large-eigenvalue condition **inside this physical chamber**; it is not claimed for arbitrary matrices.

## 6. Apply fleet02/B14 to the actual quadratic inequality

The standard one-dimensional product-projection theorem for independent cap-one coordinates gives

`||p_{c^T Z}||_inf <= sqrt(2)/||c||_2 = sqrt(2)/r`.             (6.1)

One source-backed occurrence is `yspennstate/math-open-problems@43eab33dc9cd6063c84089b5fc3692abceeadb21`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B01/20260922T200435Z-b01-qform-auto11/REPORT.md`, which cites the Rudelson--Vershynin one-dimensional projection theorem.

In (3.1), take

`Phi(U,Z)=U`,     `S(Z)=c^T Z`,     `R=0`,
`K_W=K_U=1`.

The completed partner theorem gives the **actual output-density inequality**

`||p_Q0||_inf <= 4 sqrt( sqrt(2)/(a r) )
                = 2^(9/4) (a r)^(-1/2).`                      (6.2)

Combining (6.2) with the exact target constraint (5.4),

`boxed:
 ||p_Q0||_inf
 <= C_star
 := 2^(13/4)/(71+17sqrt(17))^(1/4)
 = 2.760395280574895... .`                                    (6.3)

Thus this entire diffuse rank-three, rotated/indefinite chamber has a universal constant below three.

## 7. Arbitrary affine terms and ambient localization cost zero

Let conditioning on arbitrary outside original coordinates produce

`Q = a(W+U)^2 + 2U c^T Z
    + alpha W + beta U + gamma^T Z + eta`.                      (7.1)

Translate only the original independent coordinate `W`:

`W'=W+alpha/(2a)`.

Then

`a(W+U)^2+alpha W
 = a(W'+U)^2-alpha U-alpha^2/(4a)`.                       (7.2)

Hence the remaining `U`-linear term merely translates the slope:

`2U c^T Z +(beta-alpha)U
 = 2U [c^T Z +(beta-alpha)/2]`,                                (7.3)

which leaves its density cap unchanged. The term `gamma^T Z+eta-alpha^2/(4a)` is an arbitrary `R(Z)` allowed by the partner theorem. Therefore (6.2)-(6.3) are uniform over **all affine terms**.

Now embed (4.2) as an original-coordinate principal block of an arbitrary larger symmetric matrix. Condition on all outside original coordinates. Their self-quadratic term becomes a constant and all active--outside couplings become precisely affine terms of the form (7.1). Thus the same constant survives with no outside support/moment/translation cost. Since the active block itself already has three eigenvalues of modulus at least one, Cauchy interlacing places the ambient matrix inside the exact owner target.

This is a localization theorem for a genuine exact-target chamber, not a claim that every target matrix contains such a block.

## 8. Diffuse stress test: every individual coupling vanishes

Take

`a=2`,
`c=(2/sqrt(m))(1,...,1)`,
so `r=2` while `max_j |c_j|=2/sqrt(m)->0`.                       (8.1)

The nonzero compression is

`[[2,2,0],[2,2,2],[0,2,0]]`,

with characteristic polynomial

`lambda^3-4lambda^2-4lambda+8`.

Its eigenvalues are approximately

`-1.6038754716, 1.1099162642, 4.4939592074`,                    (8.2)

so all three remain beyond the threshold uniformly in `m`. The partner/projection bound is

`boxed: ||p_Q||_inf <= 2^(5/4)=2.378414230005442...`            (8.3)

uniformly in dimension. Thus this branch does not rely on one good coordinate minor: the useful resource is the whole bank norm `||c||_2` and its aggregate slope density.

Arbitrary translations or remote fragments in the `Z_j` laws do not alter (6.1). If one nevertheless wants a localization decomposition, Theorem 2 localizes the **aggregate slope density height** after projection and preserves (6.2) exactly; there is no spatial tooth tax.

## 9. What remains unpaid

The unrestricted implication

`three eigenvalues |lambda|>=1  =>  existence of a product-preserving chamber of the form (4.1), or another completed fleet exit`

is not proved. The correction corpus already rules out replacing this by a uniformly conditioned fixed principal minor or a naive cross-rank-three dichotomy. The new contribution is narrower and exact:

1. once a scalar slope has been aggregated, arbitrary distant/unbounded fragments can be localized by **pushforward height** with no loss;
2. the newest fleet02/B14 transverse-vertex theorem plus the product-projection cap yields the explicit `2.760396` chamber constant under the exact three-threshold spectral condition;
3. the chamber includes genuinely diffuse examples in which every individual coupling tends to zero.

The next B14 structural question is whether a general scalar-Schur/hub reduction can expose an aggregate slope before any spatial normalization, with a transverse square coefficient and bank norm whose product is forced by `s_3(A)>=1`, or else route to the existing ridge/pair/grouped-bank exits.

Full QFORM remains **OPEN**.
