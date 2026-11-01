# fleet02/B17 — sharp centered-Gaussian envelope and aggregate-minor stress

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner control revision `2026-09-22.5`  
**Run:** `20260922T125054Z-fleet02-B17-QFORM-r11`  
**Assignment:** Sharp constant and witnesses  
**Status:** `NEW SHARP SUPPORTING THEOREM / FULL CONJECTURE OPEN`  

## 1. Full target, live corrections, and first unpaid implication

The full target remains: for arbitrary independent real coordinates with densities bounded by one and arbitrary real symmetric `A` having at least three eigenvalues with modulus at least one, prove one dimension- and law-independent `L^infinity` bound for the density of `X^T A X`, or give a valid counterexample.

I used the live corrections: law-uniform pointwise stationary-phase decay is false for fragmented bounded densities; a single cross minor is not enough; taking a fiber supremum can lose dimension; and rotation destroys coordinate independence. I also consumed the completed partner report `fleet03/B17`, commit `cf171c3ee8e2068e3595e103a416cc26befa68f2`, which proves the rank-three aggregate principal-minor identity

`sum_{|I|=3} |det A_I| = |det Lambda|`

for `A=R Lambda R^T`, `R^T R=I_3`, and applies it to the three-block witness.

The first unpaid sharp-constant implication was: **can a centered diffuse/Lindeberg Gaussian limit compatible with the density-one normalization force a constant strictly larger than `3 sqrt(2)`?** The answer is no. The result below gives the exact sharp Gaussian-limit ceiling and shows that the previously constructed three-block family attains it.

This is a supporting theorem, not the full arbitrary-law conjecture.

## 2. Sharp theorem for centered Gaussian quadratic forms

### Theorem 2.1 — three-mode Gaussian envelope

Let `Z~N(0,I_d)` and let `B` be a real symmetric `d x d` matrix having at least three eigenvalues of modulus at least `s>0`. Then `Z^T B Z` has an essentially bounded density and

`||p_{Z^T B Z}||_infinity <= 1/(2 sqrt(2) s)`.

The constant is sharp already in dimension three: equality holds for

`B=s diag(1,1,-1)`

(and its sign reversal), at level zero.

For a definite three-mode form with all three selected coefficients at least `s` in modulus, the stronger bound

`||p||_infinity <= 1/(s sqrt(2 pi e))`

holds, with equality for `B=s I_3` at level `s`.

### Reduction to three independent modes

Orthogonally diagonalize `B`. Standard Gaussian rotational invariance gives

`Z^T B Z = sum_j mu_j G_j^2`

with independent standard normals. Choose any three coefficients with `|mu_j|>=s`; write their sum as `S` and the remaining independent sum as `T`. Since convolution with a probability law cannot increase an `L^infinity` density norm,

`||p_{S+T}||_infinity <= ||p_S||_infinity`.

It therefore suffices to prove the claim in dimension three.

## 3. Indefinite signature: exact location and sharp cone integral

After a global sign change, write

`S=aG_1^2+bG_2^2-cG_3^2`,

where `a,b,c>=s`.

Set `U=aG_1^2+bG_2^2` and `V=cG_3^2`. The density of `V` is decreasing on `(0,infinity)`. The density of `U` is

`f_U(u)= [1/(2 sqrt(ab))] exp(-u(a+b)/(4ab)) I_0(u|a-b|/(4ab)), u>0`.

Using `I_1(x)<I_0(x)` for `x>0`,

`d/du log f_U(u)
 < [-(a+b)+|a-b|]/(4ab) < 0`,

so `f_U` is decreasing too. Hence, for `x>=0`,

`p_S(x)=int_0^infinity f_U(x+v)f_V(v)dv <= p_S(0)`,

while for `x=-r<0`,

`p_S(-r)=int_0^infinity f_U(u)f_V(u+r)du <= p_S(0)`.

Therefore the global maximum is exactly at zero.

Now compute `p_S(0)` directly from the standard Gaussian density in spherical coordinates. With

`A(phi)=a cos^2(phi)+b sin^2(phi)`,

the cone equation on `S^2` is

`sin^2(theta) A(phi)=c cos^2(theta)`.

The radial delta integral gives the general identity

`p_S(0)= (1/(4 pi)) int_0^{2 pi} [A(phi)(A(phi)+c)]^{-1/2} dphi`.

Since `A(phi)>=s` and `A(phi)+c>=2s`,

`p_S(0) <= (1/(4 pi)) (2 pi)/(s sqrt(2))
          = 1/(2 sqrt(2) s)`.

Equality forces `A(phi)=s` for all `phi` and `c=s`, hence `a=b=c=s`. This proves the sharp indefinite claim.

## 4. Definite signature: a strictly smaller sharp envelope

Let

`S=aG_1^2+bG_2^2+cG_3^2`, `a,b,c>=s`,

and on the sphere set

`A(omega)=a omega_1^2+b omega_2^2+c omega_3^2 >= s`.

For `y>0`, radial integration gives

`p_S(y)= [sqrt(y)/(2(2 pi)^{3/2})]
          int_{S^2} A(omega)^(-3/2) exp[-y/(2A(omega))] domega`.

If `0<y<=3s`, then `A -> A^(-3/2) exp[-y/(2A)]` is decreasing for `A>=s`. Therefore

`p_S(y) <= sqrt(y)/(sqrt(2 pi)s^{3/2}) exp[-y/(2s)]
         <= 1/(s sqrt(2 pi e))`,

with equality at `y=s` when `a=b=c=s`.

If `y>=3s`, the same scalar factor is maximized over `A>=s` at `A=y/3`, so

`p_S(y) <= [3^{3/2} e^{-3/2}]/[sqrt(2 pi) y]
         <= [sqrt(3)e^{-3/2}]/[sqrt(2 pi)s]
         < 1/(s sqrt(2 pi e))`.

Thus the definite branch is strictly less dangerous than the mixed-sign branch.

## 5. Covariance floor forced by density <= 1

If a real random variable `X` has a probability density bounded by one and finite variance, then for any center `m`,

`P(|X-m|<=r)<=2r` for `0<=r<=1/2`.

Taking `m=EX` and integrating the tail,

`Var(X)=int_0^infinity 2r P(|X-EX|>r)dr
       >=int_0^{1/2}2r(1-2r)dr
       =1/12`.

Consequently, if `R` has orthonormal columns and the independent centered coordinates have finite variances `v_i>=1/12`, then

`Cov(R^T X)=R^T diag(v_i)R >= (1/12) I`.

This is exactly attained by centered intervals of length one.

## 6. Corollary: `3 sqrt(2)` is the exact centered Gaussian diffuse-limit ceiling

Let `Y~N(0,Sigma)` in `R^d`, with `Sigma>=sigma^2 I`, and let `A` be symmetric with at least three eigenvalues of modulus at least one. Write `Y=Sigma^{1/2}Z` and

`B=Sigma^{1/2} A Sigma^{1/2}`.

By the singular-value inequality

`s_k(PAQ) >= s_min(P)s_min(Q)s_k(A)`,

`B` has at least three eigenvalues of modulus at least `sigma^2`. Theorem 2.1 therefore gives

`||p_{Y^T A Y}||_infinity <= 1/(2 sqrt(2) sigma^2)`.

In particular, for any centered Lindeberg/diffuse triangular-array Gaussian limit whose covariance is the limit of projected product covariances from density-one inputs, `sigma^2>=1/12`, so

`boxed(||p_limit||_infinity <= 3 sqrt(2))`.

The three-block uniform family

`A_m=diag(J_m/m,J_m/m,-J_m/m)`

has projected covariance exactly `(1/12)I_3` and converges to the equality case. Therefore

`boxed(3 sqrt(2) is the exact sharp constant inside the centered Gaussian diffuse-limit mechanism.)`

This sharpens the earlier lower bound: the same mechanism cannot be pushed above `3 sqrt(2)` by changing centered finite-variance density-one input laws, covariance anisotropy, coefficient anisotropy, or the definite/indefinite signature, once the limit is Gaussian and the covariance floor is retained.

Caveat: this does **not** cover noncentral Gaussian limits without an additional argument, finite non-Gaussian arrays, mesoscopic non-Lindeberg structure, or the full arbitrary-product target.

## 7. Applying the completed fleet03/B17 aggregate-minor identity

For the exact rank-three block witness, the partner theorem gives

`M_3(A_m):=sum_{|I|=3}|det (A_m)_I|=|det diag(1,1,-1)|=1`.

At the same time,

`Q_m => (G_1^2+G_2^2-G_3^2)/12`

and the limiting density at zero is `3 sqrt(2)`.

Therefore any homogeneous rank-three bound that uses **only** aggregate principal determinant mass in the form

`||p_Q||_infinity <= K M_3(A)^(-1/3)`

would necessarily satisfy

`boxed(K >= 3 sqrt(2))`.

This is a direct application of the partner's conserved determinant currency. It rules out `pi` not only as a universal target constant, but also as the coefficient of this natural aggregate-minor homogeneous ansatz.

The partner also showed that the same family has `m^3` equal nonsingular physical triples, each determinant `-m^-3`, so a one-triple inverse-determinant payment grows like `m`. Combining that with the sharp Gaussian-limit calculation isolates the mechanism a successful proof must capture: **aggregate before inversion**, and in the fully diffuse centered regime the correct stress scale is exactly `3 sqrt(2)`, not `pi` and not a growing single-minor cost.

## 8. Exact and finite controls

- `m=1`: the diagonal cube control has `p_Q(0)=pi`.
- `m=2`: the exact six-variable rotated target witness has `p_Q(0)=2pi-7/3=3.9498519738...`.
- `m -> infinity`: the block family tends to the sharp centered-Gaussian value `3sqrt(2)=4.2426406871...`.

Exploratory quadrature for intermediate block sizes was used only as a sanity check and is not needed for any theorem above.

## 9. Remaining full-target implication

The full conjecture is still **OPEN / NOT PROVED**. The next sharp-constant question is no longer whether a centered Gaussian diffuse limit beats `3sqrt(2)`; it cannot. The remaining adversarial mechanisms are:

1. noncentral diffuse limits (unless one proves a Gaussian translation-monotonicity theorem for quadratic densities);
2. mesoscopic/non-Lindeberg product arrays whose projected law is not Gaussian;
3. mixed-leverage matrices where some spectral mass localizes and some delocalizes;
4. higher-rank forms where extra modes interact with the product structure before any Gaussianization/localization split.

A plausible global proof should therefore split localized/mixed-leverage structure from a diffuse aggregate branch, retaining the partner's conserved `M_3` currency before inverse determinant operations. The theorem here supplies a sharp calibration point: any diffuse branch with constant below `3sqrt(2)` is false, while constants far above it are quantitatively nonsharp but may still prove the conjecture.

## 10. Provenance and correction status

- brain control snapshot used before derivation: `16be0cbcda9bb34b64ad7aa47d950b4277d6e9dc`; pre-write control recheck: `330b971e11fe068bfd93d76ce910d28c6e9618cb`; owner control revision unchanged at `2026-09-22.5`;
- partner dependency: `yspennstate/math-open-problems` commit `cf171c3ee8e2068e3595e103a416cc26befa68f2`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B17/20260922T120619Z-fleet03-B17-QFORM-r11/REPORT.md`;
- corrections consumed: `QFORM-POINTWISE-DECAY-FALSE`, `QFORM-FIBER-SUP-DIMENSION-LOSS`, `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`, `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-UNIVERSAL-PI-FALSE-AND-DIFFUSE-BRANCH`, `QFORM-TWOSHEET-XRAY-ONLY-FALSE`;
- no claim here is a full proof or counterexample to the conjecture.
