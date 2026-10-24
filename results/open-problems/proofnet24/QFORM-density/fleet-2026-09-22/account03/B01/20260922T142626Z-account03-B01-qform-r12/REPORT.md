# QFORM account03/B01 — sharp dependent-square smoothing and signed-Fejer transfer

Programme: `QFORM-DENSITY-3EIG-20260922`  
Control revision: `2026-09-22.5`  
Run: `20260922T142626Z-account03-B01-qform-r12`  
Assignment: `Oscillatory replacement`  
Status: `PROVED_SUPPORTING_THEOREM / IMPROVED_EXISTING_BRANCH / FULL_TARGET_OPEN / WITHOUT_VERIFIED_BRAIN`

## 1. Exact target, current corrections, and mechanism change

The full target remains open: for every dimension, every independent real coordinates with one-dimensional probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove one universal finite essential bound for the density of `Q=X^T A X`, or give a valid counterexample. Continuity of a representative is a separate stronger conclusion.

This run changes mechanism from the preceding B01 rank-two Hausdorff--Young calculation. It uses an exact one-sided fractional-integral inequality, then transfers the result into the signed Fejer interface supplied by the assigned partner `account04/B01`.

The phase-aligned counterexample is preserved. For a prescribed nonzero frequency `s` and arbitrarily small `delta>0`, one may choose a density-one indicator on a measurable set of measure one contained in

`{x: dist(s x^2,2 pi Z)<=delta}`,

which has infinite Lebesgue measure. Then `Re E exp(i s X^2)>=cos(delta)`. Hence no positive law-uniform pointwise decay in `s` follows from the density cap alone. This report does not use such a bound.

The live absolute-Wiener correction is also preserved: bounded output density does not imply `phi_Q in L^1`, even for the diagonal three-square control. The present route never requires an absolute `L^1` Fourier estimate. It also does not assume independence after spectral rotation, a good local minor forced by the three-eigenvalue hypothesis, or any moment/support/log-concavity condition.

## 2. Sharp one-sided fractional-integral inequality

Let `p>2` and let `q=p/(p-1) in (1,2)`. Put

`A_q = Gamma(2-q) Gamma(q+1)`

and

`K_p = [2/(2-q)] * [(2-q)/q]^(q/2) * sqrt(A_q).`       (2.1)

### Lemma 2.1 — `QFORM-HALF-INTEGRAL-LP-L1-v1`

If `h>=0`, `integral h=1`, and `||h||_p<=M`, then

`sup_x integral_0^infinity h(x-u) u^(-1/2) du
 <= K_p M^(p/[2(p-1)]).`                                (2.2)

For `p=3`,

`K_3 = 2 sqrt(pi) / 3^(1/4) = 2.6935473741...`.         (2.3)

Moreover, the constant in (2.3) is sharp under only the two constraints `||h||_1=1` and `||h||_3=M`.

### Proof

Let `k(u)=u^(-1/2)` for `u>0`. For every `lambda>0`,

`k(u) <= lambda + (k(u)-lambda)_+`.

Therefore, by Holder,

`integral_0^infinity h(x-u) k(u) du
 <= lambda + M ||(k-lambda)_+||_q`.                    (2.4)

A direct substitution `u=lambda^(-2) z` gives

`||(k-lambda)_+||_q^q
 = lambda^(q-2) int_0^1 (z^(-1/2)-1)^q dz`.             (2.5)

With `z=t^2`,

`int_0^1 (z^(-1/2)-1)^q dz
 =2 int_0^1 t^(1-q)(1-t)^q dt
 =2 B(2-q,q+1)
 =Gamma(2-q)Gamma(q+1)=A_q`.                            (2.6)

Thus (2.4) becomes

`lambda + M A_q^(1/q) lambda^(-(2-q)/q)`.              (2.7)

Write `alpha=(2-q)/q`. Its minimum is attained at

`lambda_*=(alpha M A_q^(1/q))^(1/(1+alpha))`.

Since `1/(1+alpha)=q/2=p/[2(p-1)]`, substitution gives exactly (2.1)-(2.2).

For `p=3`, `q=3/2` and

`A_(3/2)=Gamma(1/2)Gamma(5/2)=3 pi/4`,

which simplifies (2.1) to (2.3).

To see sharpness at `p=3`, fix `lambda>0` and on the negative half-line set, in the variable `u=-x>0`,

`h(-u)=c (u^(-1/2)-lambda)_+^(1/2)`,

with zero density elsewhere. The support is `0<u<lambda^(-2)`. Exact beta integrals give

`int h = c (pi/4) lambda^(-3/2)`,

`int h^3 = c^3 (3 pi/4) lambda^(-1/2)`,

and

`int_0^infinity h(-u) u^(-1/2) du = c pi lambda^(-1/2)`.

Choosing `c=4 lambda^(3/2)/pi` normalizes the mass. Then

`||h||_3^3 = 48 lambda^4/pi^2`.

For prescribed `M`, take

`lambda = sqrt(pi) M^(3/4)/(2*3^(1/4))`.

The last displayed half-integral is `4 lambda`, exactly

`[2 sqrt(pi)/3^(1/4)] M^(3/4)`.

Hence (2.3) cannot be improved if one uses only the probability normalization and the `L^3` norm. QED.

## 3. Dependence-safe square smoothing with the sharp constant

### Theorem 3.1 — `QFORM-DEPENDENT-SQUARE-LP-SHARP-v1`

Let `R` have a probability density `h` with `||h||_p<=M`, where `p>2`. Let `V` be a real random variable, not assumed independent of `R`, such that for almost every `r` the conditional law of `V|R=r` has a density bounded by one. Let `d!=0` and

`T=R+d V^2`.

Then `T` has an essentially bounded density and

`||p_T||_infinity
 <= K_p |d|^(-1/2) M^(p/[2(p-1)]).`                    (3.1)

In particular,

`||p_T||_infinity
 <= [2 sqrt(pi)/3^(1/4)] |d|^(-1/2) ||h||_3^(3/4).`   (3.2)

This improves the previously used dependence-safe constant `4` in the `L^3` square-smoothing lemma to the sharp abstract constant `2 sqrt(pi)/3^(1/4)<2.694`.

### Proof

Assume first `d>0`. If `g_r` is the conditional density of `V|R=r`, then for `s>0` the conditional density of `dV^2` is

`[g_r(sqrt(s/d))+g_r(-sqrt(s/d))]/[2 sqrt(d s)]
 <= d^(-1/2) s^(-1/2).`                                (3.3)

Disintegration therefore gives, for almost every `t`,

`p_T(t)
 <= d^(-1/2) int_{r<t} h(r)(t-r)^(-1/2) dr`.           (3.4)

Lemma 2.1 proves (3.1). If `d<0`, reflect the one-sided kernel. The `p=3` value is (2.3). QED.

The theorem proves an essential density bound. It does **not**, by itself, prove a continuous representative.

## 4. Applying the preceding B01 averaged-frequency theorem

The preceding account03/B01 run proved `QFORM-DIFFUSE-AVERAGED-LP-v1`. In its rank-two form, let `S` be an `m x 2` matrix with orthonormal columns and row leverages at most `1/2`; let `Gamma` be invertible symmetric; let `X_j` be independent with densities at most one; and allow arbitrary one-coordinate measurable potentials. Write

`R=(S^T X)^T Gamma(S^T X)+sum_j V_j(X_j)`,

`B(S)=prod_{c_j>0}(1-c_j)^(-(1-c_j)/2) <= e`,

`Delta=|det Gamma|`.

For every `p>2`, that theorem is equivalently

`||p_R||_p
 <= (p B(S))^((p-1)/p) Delta^(-(p-1)/(2p)).`    (4.1)

Now add one original independent physical coordinate `X_0`, with arbitrary measurable shift `m(X)`, and define

`Q=d (X_0+m(X))^2 + R`, `d!=0`.                         (4.2)

Conditional on `R=r`, the law of `X_0+m(X)` is a mixture of translations of the original density of `X_0`, hence still has density at most one. Theorem 3.1 applies. Since

`[(p-1)/p] * [p/(2(p-1))]=1/2`

and

`[(p-1)/(2p)] * [p/(2(p-1))]=1/4`,

we obtain the whole smoothing ladder

`||p_Q||_infinity
 <= K_p sqrt(p B(S)) |d|^(-1/2) Delta^(-1/4), p>2.`    (4.3)

Taking the clean value `p=3` gives

`||p_Q||_infinity
 <= 2 sqrt(pi) 3^(1/4) sqrt(B(S))
      |d|^(-1/2) Delta^(-1/4)`                         (4.4)

and hence, using `B(S)<=e`,

`||p_Q||_infinity
 <= 2*3^(1/4)*sqrt(pi e)
      |d|^(-1/2) Delta^(-1/4)
 < 7.692 |d|^(-1/2) Delta^(-1/4).`                     (4.5)

This is a genuinely coupled third-direction theorem: the square shift may depend arbitrarily on the rank-two variables. It does not require convolution independence between `R` and the square term.

## 5. Quantitative improvement of the current localized-diffuse spectral branch

A completed proof-assembly result from account03/B19 supplies the exact rank-three spectral-Schur identity used here. For a rank-exactly-three form

`Q_0=X^T R Lambda R^T X`, `R^T R=I_3`,

fix an original coordinate `i`, let `v` be the `i`th row of `R`, put

`c=|v|^2>0`, `a=v^T Lambda v`,

and assume `a!=0`. The source proves an original-coordinate decomposition

`Q_0=a(X_i+m(Y))^2 + Y^T T Y`,                          (5.1)

where `T` has rank two and

`|pdet T| = c |det Lambda|/|a|`.                        (5.2)

If the whitened residual two-frame has every row leverage at most `1/2`, (4.5) applies with `d=a` and `Delta=|pdet T|`. Therefore

`boxed(
 ||p_Q0||_infinity
 <= 2*3^(1/4)*sqrt(pi e)
    (|a| c |det Lambda|)^(-1/4)
 )`                                                     (5.3)

with numerical constant

`2*3^(1/4)*sqrt(pi e)=7.6918797590...`.

The existing theorem on exactly this branch used the earlier square-smoothing constant `4`, producing

`4 sqrt(3e)=11.4226760335...`.

Thus (5.3) lowers the analytic constant on that already-valid structural branch by the exact factor

`sqrt(pi)/(2*3^(1/4)) = 0.6733868435...`.               (5.4)

The structural hypothesis has **not** been weakened: the full target still needs a dimension-free aggregation/extraction argument on mixed-leverage and near-isotropic residual configurations.

## 6. Assigned partner account04/B01 applied: exact signed-Fejer cap

The assigned partner `account04/B01` has now completed `QFORM-SIGNED-FEJER-EXACT-INTERFACE-v1`. For a probability law `mu` with characteristic function `phi`, it defines

`D_T mu(y)
 =(1/(2 pi)) int_{-T}^T (1-|t|/T)
   Re(exp(-i t y) phi(t)) dt`,                          (6.1)

and proves the exact equivalence

`||p_mu||_infinity = sup_{T>0,y} D_T mu(y)`             (6.2)

whenever `mu` has a bounded density; conversely a uniform cap on all `D_T` implies such a density. This is a signed triangular average and is strictly weaker than absolute Fourier `L^1` control.

Applying (6.2) to (4.4) gives the actual inequality

`sup_{T>0,y} D_T law(Q)(y)
 <= 2 sqrt(pi) 3^(1/4) sqrt(B(S))
      |d|^(-1/2) Delta^(-1/4).`                        (6.3)

On the spectral-Schur branch this becomes

`sup_{T>0,y} D_T law(Q_0)(y)
 <= 2*3^(1/4)*sqrt(pi e)
    (|a|c|det Lambda|)^(-1/4).`                        (6.4)

This is a direct application of the named partner theorem, not a citation-only use. It shows that the averaged-frequency rank-two resource from the previous B01 run can be converted, through a dependence-safe physical square, into the **exact signed Fejer quantity equivalent to the target density bound** on this branch. No absolute time integral is introduced.

The partner also proves that a uniform Fejer cap alone establishes only an essentially bounded density; continuity needs a separate local-uniform convergence argument. Accordingly (6.3)-(6.4) do not promote continuity.

## 7. What remains unpaid

The full conjecture is **OPEN**. The current live corrections rule out replacing the remaining step by a uniformly good fixed principal minor or a single Schur rank-two extraction. The source-valid residual is still the global product-preserving aggregation problem: from only three large eigenvalues, force enough averaged rank-two/third-direction resource, or another signed-Fejer mechanism, without paying a dimension-dependent reciprocal minor and without assuming independence after rotation.

This run improves the analytic cost once a diffuse rank-two residual plus physical square pivot has been obtained. It does not prove that every target matrix admits that certificate. In particular it does not pay the known high-cardinality family where every fixed local certificate degenerates but aggregate cross structure remains large.

A useful next B01 question is therefore whether the half-integral ladder can be applied **before** selecting a single pivot, by averaging several conditional square pivots inside the signed Fejer quantity. That would attack the live aggregation obstruction rather than optimize another already-local branch.

## 8. Source pins

- Fresh controls: `yspennstate/math-research-brain`, programme `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`.
- Assigned partner account04/B01: `yspennstate/math-open-problems@a3693ed6d50e8e4143b2f33bf997c5de2cb52d79`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B01/20260922T141507Z-b01-qform-fejer-r1/REPORT.md`.
- Previous account03/B01 averaged-frequency theorem: `yspennstate/math-open-problems@d54e3a5d40a1d9837d39a1e525781fcf44ec0d9d`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260922T123142Z-qform-r11/REPORT.md`.
- Account03/B19 rank-three spectral-Schur/localized-diffuse branch: current repository report `proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/account03-B19-20260922T123215Z-186f53a8/REPORT.md`; the exact decomposition and old constant are consumed only at their proved scope.

No credential, scheduler identifier, machine path, private transcript, email content, public release, remote workflow, paid model/API call, or unrelated private data is included. Repository retrieval is not native learned-memory ingestion; this run is `WITHOUT_VERIFIED_BRAIN`.
