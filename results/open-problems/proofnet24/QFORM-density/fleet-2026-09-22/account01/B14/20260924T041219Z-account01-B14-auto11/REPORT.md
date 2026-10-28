SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B14, 2026-09-24T04:12:19Z.
attacking: concave height-layer localization — replace unsafe spatial fragment normalization by density superlevel decomposition, then apply the completed account02/B14 subprobability overlap theorem before summing.

# account01/B14 — concave height localization for rough translated slope laws

Run: `20260924T041219Z-account01-B14-auto11`
Programme: `QFORM-DENSITY-3EIG-20260922`
Role: translations and localization
Control programme revision: `2026-09-22.5`
Status: **NEW SUPPORTING LOCALIZATION THEOREM + TARGET-VALID PARTNER APPLICATION / FULL QFORM OPEN**
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains OPEN. The result below does not assume a bounded support, moments, a connected support, or a finite number of fragments. It is deliberately compatible with the live corrections `QFORM-BOUNDED-DIAMETER-LOCALIZATION-FALSE` and `QFORM-NO-UNIFORM-FRAGMENT-COUNT-BATHTUB-v1`. It does not use the refuted law-uniform pointwise quadratic Fourier decay.

## 1. The new mechanism: density height, not spatial pieces

For a finite positive measure `eta` on `R`, write

`Lambda(eta):=sup_(a<b) eta((a,b))/(b-a)`.

If `Lambda(eta)<infinity`, then `eta` is absolutely continuous and its density has essential supremum at most `Lambda(eta)`. Conversely, for an absolutely continuous `eta`, `Lambda(eta)=||p_eta||_infinity`.

### Theorem `QFORM-CONCAVE-HEIGHT-LOCALIZATION-v1`

Fix `0<alpha<=1`. Let `T` be a positive linear map from finite positive measures on `R` to finite positive output measures on `R`. Suppose that for every measurable finite-measure `E subset R`,

`Lambda(T(1_E dx)) <= C |E|^alpha`.                                      (1)

Then every measurable `f` with `0<=f<=1` and finite mass `M=int f` satisfies

`boxed: Lambda(T(f dx)) <= C M^alpha`.                                  (2)

The constant is exactly the same `C`.

#### Proof

For `s in (0,1)`, set

`E_s={x:f(x)>s}`, `m(s)=|E_s|`.

For every `s>0`, `m(s)<infinity`, because `s m(s)<=M`. Layer cake gives, as positive measures,

`f(x)dx = int_0^1 1_(E_s)(x) dx ds`,
`int_0^1 m(s) ds=M`.                                                     (3)

Let `I` be any bounded interval. Positivity, linearity, Tonelli and (1) give

`T(f dx)(I)
 =int_0^1 T(1_(E_s)dx)(I) ds
 <=C |I| int_0^1 m(s)^alpha ds`.                                        (4)

Because `u^alpha` is concave and the `s`-interval has measure one,

`int_0^1 m(s)^alpha ds <= (int_0^1 m(s) ds)^alpha=M^alpha`.              (5)

Divide (4) by `|I|` and take the supremum over `I`. QED.

### Conditional / arbitrary-shift form

The same proof works for a family `T_omega` when (1) holds with the same `C` for every conditioning parameter `omega`. After proving (2) conditionally, average over `omega`. Consequently, deterministic or outside-dependent translations cost zero whenever the indicator estimate is translation-uniform.

This is distinct from spatial fragment summation. Spatial decomposition into disjoint pieces with a sublinear mass power `m^alpha`, `alpha<1`, can diverge. Height decomposition uses nested superlevel sets and Jensen, so every exponent `0<alpha<=1` is zero-tax.

### Multimarginal version

If a positive multilinear output compiler obeys

`Lambda(T(1_(E_1)dx,...,1_(E_k)dx)) <= C prod_j |E_j|^(alpha_j)`,
`0<alpha_j<=1`,

then for `0<=f_j<=1`, `M_j=int f_j`,

`boxed: Lambda(T(f_1dx,...,f_kdx)) <= C prod_j M_j^(alpha_j)`.           (6)

Indeed, apply layer cake in each coordinate and Jensen separately.

## 2. Completed designated-partner theorem actually used

The completed `account02/B14` source used here is:

- canonical math commit `a8f9df9160d57a99c5c134b7c0e52400c0c80bd9`;
- path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260924T020607Z-account02-B14-QFORM-auto11/REPORT.md`;
- theorem `QFORM-OVERLAP-SLOPE-SUBPROBABILITY-HOMOGENEITY-v1`.

In its notation, keep the probability slice `(X,L,Y_phase)` with

`ess sup_l |F_t(l)| <= A |t|^(-1/2)`.

The source states the following for a positive slope-bank law `tau` of mass `0<m<=1`, whose slope pushforward has density cap `L_0`. For

`Q=H(X)+2XL+Y_phase+2X S(Z)+R(Z)`,

the partner proves a continuous density for the output submeasure `eta` with

`boxed: ||p_eta||_infinity <= 5 pi^(-1/5) A^(2/5) m^(3/5) L_0^(2/5)`.   (7)

The proof is the completed two-Plancherel estimate

`|hat eta(t)| <= min{m, pi sqrt(A m L_0) |t|^(-5/4)}`.                  (8)

### Finite-mass extension needed for height localization

A superlevel set of a cap-one probability density can have Lebesgue measure larger than one, so I do **not** silently apply the partner's stated `m<=1` theorem outside its scope. Instead, inspect its completed proof: every step (the bounds `||g_t||_1<=m`, `||g_t||_infinity<=L_0`, hence `||g_t||_2^2<=mL_0`, the Plancherel estimate, the trivial Fourier bound `|hat eta|<=m`, and the exact envelope integral) is valid for every finite `m>0`. Therefore the identical formula (7) holds for **all finite positive masses** `m`. This is `QFORM-OVERLAP-SLOPE-FINITE-MASS-EXTENSION-v1`; no new analytic input beyond the source proof is needed.

This finite-mass extension is essential below, because `m(s)=|{f_Z>s}|` need not be at most one.

## 3. Apply the partner theorem to a rough arbitrary slope law

Let `X,L,Z` be independent real random variables with arbitrary probability densities

`0<=f_X,f_L,f_Z<=1`,

and let `Y~Unif[-1/2,1/2]` be independent. Allow arbitrary affine coefficients `alpha,beta,gamma,delta,eta in R`, and set

`Q=2X(L+Z)+Y^2+alpha X+beta L+gamma Z+delta Y+eta`.                    (9)

First verify the slice constant uniformly in the affine shifts. Completing the square,

`Y^2+delta Y=(Y+delta/2)^2-delta^2/4`.

For every interval `J` of length one and every `t !=0`,

`|int_J exp(i t u^2) du| <=4 |t|^(-1/2)`.                             (10)

For `T=|t|<=16`, this is the trivial `1<=4T^(-1/2)`. If `T>16`, put `a=T^(-1/2)`. The part of `J intersect [-a,a]` has length at most `2a`. On a positive tail interval `[u,v] subset [a,infinity)`, integration by parts gives

`|int_u^v exp(iT x^2)dx| <=1/(T u)<=a`,                               (11)

and reflection gives the same bound on a negative tail. Thus the central part plus at most two tails is at most `4a`.

Hence the partner slice transform is

`F_t(l)=f_L(l) exp(i t beta l) E exp(i t(Y^2+delta Y))`

and satisfies

`ess sup_l |F_t(l)| <=4 |t|^(-1/2)`;                                  (12)

therefore `A=4`.

Now localize the *arbitrary rough law of `Z` by density height*. Let

`E_s={z:f_Z(z)>s}`, `m(s)=|E_s|`.

For the positive slope measure `1_(E_s)(z)dz`, the slope map is simply `S(z)=z`, so its pushforward density cap is exactly at most

`L_0=1`,                                                               (13)

independent of the location, diameter, number of connected components, or separation of `E_s`. The linear term `gamma Z` is absorbed in the partner's arbitrary phase `R(Z)`.

Applying (7), with the finite-mass extension above, to the actual output measure `eta_s` gives

`||p_(eta_s)||_infinity <=5 pi^(-1/5)4^(2/5)m(s)^(3/5)`.               (14)

Because

`f_Z(z)dz=int_0^1 1_(E_s)(z)dz ds`

and `int_0^1m(s)ds=1`, the new theorem with `alpha=3/5` yields

`boxed: ||p_Q||_infinity <=5 pi^(-1/5)4^(2/5)
       =6.924111078456212...`.                                         (15)

This is the required actual partner application. It is uniform over every admissible `f_Z`, including unbounded support, arbitrarily distant fragments, infinitely many fragments, and no moments. Translating `Z` by an arbitrary deterministic amount changes neither (13) nor the constant.

## 4. Full-target ambient localization chamber

Consider the original-coordinate principal block on `(X,L,Z,Y)`

`A_*=[[0,1,1,0],
      [1,0,0,0],
      [1,0,0,0],
      [0,0,0,1]]`.                                                     (16)

Its spectrum is

`spec(A_*)={sqrt(2),1,0,-sqrt(2)}`.                                   (17)

Thus it already has three eigenvalues of modulus at least one.

Now embed `A_*` as a principal block of an arbitrary larger real symmetric matrix

`A=[[A_*,C],[C^T,D]]`,                                                  (18)

with completely arbitrary `C,D`. Let the outside original coordinates `W` be independent of `(X,L,Z,Y)`, with arbitrary cap-one marginals and no moment/support hypotheses. Condition on `W=w`. Then

`X_all^T A X_all
 =2X(L+Z)+Y^2
  +alpha(w)X+beta(w)L+gamma(w)Z+delta(w)Y+eta(w)`.                     (19)

Equation (15) is uniform in all five affine coefficients, so

`||p_(Q|W=w)||_infinity <=6.924111078456212...`

for every `w`. Averaging conditional measures preserves the same interval bound, and therefore

`boxed: ||p_(X_all^T A X_all)||_infinity <=6.924111078456212...`.      (20)

Cauchy interlacing applied to (17) shows that every matrix (18) remains inside the owner's exact three-large-eigenvalue target.

Scope: `X,L,Z` and every outside marginal are arbitrary cap-one laws; `Y` is the one retained uniform receiver-square coordinate used to provide the half-order slice estimate. Thus (20) is a genuine rotated/indefinite target-valid chamber, not the full arbitrary-law theorem.

## 5. Why this fixes the partner's fragment-first barrier

The partner exhibited

`f_N=1_(E_N)`, `E_N=union_(j=1)^N [4^j,4^j+1/N]`.

If one splits spatially tooth-by-tooth, each piece has mass `1/N` but slope cap `1`, and (7) summed over pieces grows like `N^(2/5)`.

Height localization behaves differently. Since `f_N` is an indicator,

`{f_N>s}=E_N`, `m(s)=1`, `0<s<1`.

Thus (14) integrates to the unchanged constant `6.924111...`, regardless of `N` or the tooth locations.

The distinction is exact:

- **spatial localization:** a sublinear mass exponent generally causes a concavity tax;
- **density-height localization:** the same sublinear exponent is harmless because Jensen is applied over the unit height parameter before any spatial normalization.

No bounded-diameter or fixed-fragment-count statement is inferred.

## 6. What remains open

`QFORM-CONCAVE-HEIGHT-LOCALIZATION-v1` removes one proof-interface obstruction: rough cap-one slope laws need not be normalized into spatial fragments before applying a subprobability overlap theorem. It does **not** manufacture the slice half-order estimate from the bare spectral hypothesis. In particular, the live global problem still needs a product-preserving structural reduction which, from only `s_3(A)>=1`, enters a whole-law receiver/ridge/bank/pair chamber with the required aggregate slice and slope controls for fully arbitrary marginals.

The next B14 step is to apply the same height-localization principle to a partner chamber in which the half-order slice certificate itself is generated from arbitrary cap-one product coordinates, rather than from the retained uniform square used in (9)-(20).

## 7. Source and integrity notes

Fresh current controls and the live correction inbox were read before publication. The designated partner theorem was read from its immutable canonical math source, not only from a handoff. No refuted arbitrary-joint coarea, post-rotation independence, bounded-diameter localization, fixed-fragment-count localization, or law-uniform pointwise quadratic Fourier decay is used.

Changed-file allowlist for this run is restricted to this worker's unique math report, handoff, memory snapshot, own latest pointer, and own run login/start/finish/receipt files. Manual fallback privacy review found only mathematical/control metadata and no credentials, signed download URLs, machine paths, private financial material, or permission changes.
