# Hybrid subcritical ridge + cross-two tail theorem

Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: `account01/B03`  
Run: `account01-B03-20260922T181633Z-r13`  
Status: **ESSENTIAL_STEP_APPLIED / FULL TARGET OPEN / WITHOUT_VERIFIED_BRAIN**

## 1. Exact target and fresh source state

The target remains: for every dimension, independent real coordinates `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^T A X` has a density with universally bounded essential supremum, or give a valid counterexample. Continuity is a separate requested conclusion.

Fresh control before the derivation was `yspennstate/math-research-brain@d4c3b6e2da0616173d467b0f100cfdc4c60c5e46`, OWNER CONTROL revision `2026-09-22.11`; QFORM is the sole research target and no later stop was observed at that refresh.

The relevant corrections consumed are:

- law-uniform pointwise one-dimensional van-der-Corput/Fresnel decay is false;
- conditioning a difference on its conjugate sum does not preserve a density cap;
- the arbitrary-joint rank-three coarea bound is false;
- positive moments of full-vector conditional projection-density caps can diverge;
- the new worst-condition scalar bridge `sup_b ||p_{Q3|Q_rest=b}||_infinity` is false (account03/B16 and account02/B01 source-valid counterexamples); weighted/mixture formulations remain possible;
- no universal single good physical pivot plus disjoint cross-two certificate follows from the three-large-eigenvalue hypothesis.

No refuted statement is used below.

## 2. Dependencies, including the required named partner

### 2.1 Ridge envelope already proved by this worker

From `yspennstate/math-open-problems@c301be6b21f382934962aeb4c019b713377eac2f`, path

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B03/account01-B03-20260922T164925Z-r12/REPORT.md`,

a dependence-safe regularized cross-block argument gives the following. For a residual quadratic form `R`, a physical cross block `B`, a parameter `gamma>0`, and

`K = B B^T (gamma^2 I+B B^T)^(-1)`,  `theta=tr K`,

`D_ridge = det(I+B B^T/gamma^2)`,

if `1<=q<=2` and `max_i K_ii<=q/2`, then

`|phi_R(t)| <= min(1,(t0/|t|)^beta)`,

where

`beta = theta/(2q)`,

`t0 = [L_q/(2 gamma)] D_ridge^(-1/(2 theta))`,

`L_q = pi e sqrt(2/q)`.

The previous run integrated this only when `beta>1/2` for the half-Riesz kernel. The point of the present run is to cross the threshold `beta<=1/2` by retaining an independent-copy cross-two tail.

### 2.2 Named partner account02/B03 actually applied

The completed partner theorem is account02/B03 run `20260922T171110Z-account02-B03-QFORM-r12`, canonical mathematics

`yspennstate/math-open-problems@18acc1aad6a7d8d9e7538807afbb1a453d7e529b`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B03/20260922T171110Z-account02-B03-QFORM-r12/REPORT.md`.

For any residual quadratic form `R` in independent cap-one coordinates, if disjoint physical two-sets `I,J` have an invertible cross block `C=S[I,J]` with

`Delta=|det C|>0`,

then the exact sum/difference pair law and four-dimensional Plancherel give

`|phi_R(t)|^2 <= min(1, pi^2 Delta^(-1)|t|^(-2))`.

Therefore

`|phi_R(t)| <= min(1,t2/|t|)`,  where  `t2=pi Delta^(-1/2)`.     (2.1)

This is the named OTHER-account result applied below. It keeps the dependence inside each `(X_i-X_i',X_i+X_i')` pair and uses no false conditional cap.

## 3. Hybrid fractional-time lemma

Let a real random variable `R` have characteristic function `phi`. Assume, for some `t0,t2>0` and `beta>0`,

`|phi(t)| <= min(1,(t0/|t|)^beta,t2/|t|)`                     (3.1)

for `t!=0`.

Define the half-Riesz potential

`H(R)=sup_z E |z-R|^(-1/2)`.

The Fourier transform identity

`hat{|x|^(-1/2)}(t)=sqrt(2 pi)|t|^(-1/2)`

in the convention `hat h(t)=int exp(i t x)h(x)dx`, together with Gaussian smoothing and Fatou exactly as in the cited r12 report, gives

`H(R) <= (1/sqrt(2 pi)) int_R |t|^(-1/2)|phi(t)| dt`

`      = sqrt(2/pi) J`,                                        (3.2)

where

`J=int_0^infinity t^(-1/2)|phi(t)|dt`.

The extra tail `t2/t` makes this finite even when the ridge exponent is at or below the former threshold `beta=1/2`.

### 3.1 Subcritical case `0<beta<1/2`

Put

`a=1/2-beta`,

`alpha=beta/[2(1-beta)]`,

`delta=(1-2 beta)/[2(1-beta)] = a/(1-beta)`.

Then `alpha+delta=1/2`. Let `M=max(t0,t2)`. I claim

`J <= [4+1/(1/2-beta)] t0^alpha M^delta`.                       (3.3)

Proof. If `t2<=t0`, use `1` on `(0,t0)` and `t2/t` on `(t0,infinity)`:

`J <= 2 sqrt(t0)+2 t2/sqrt(t0) <=4 sqrt(t0)`.

Since `M=t0` and `alpha+delta=1/2`, (3.3) follows.

Now suppose `t2>t0`. Set

`T=(t2/t0^beta)^(1/(1-beta))`.

Then `T>t0`, and splitting at `t0,T`,

`J <= 2 sqrt(t0)
      + t0^beta int_(t0)^T t^(-beta-1/2)dt
      + t2 int_T^infinity t^(-3/2)dt`.

Dropping the negative lower-end term from the middle integral gives

`J <=2 sqrt(t0) + [1/a] t0^beta T^a +2 t2 T^(-1/2)`.

The definition of `T` gives

`t2 T^(-1/2)=t0^beta T^a`,

and

`t0^beta T^a = t0^alpha t2^delta >= sqrt(t0)`.

Thus

`J <= [4+1/a] t0^alpha t2^delta`,

which is (3.3). QED.

Combining with (3.2),

`H(R) <= sqrt(2/pi)[4+1/(1/2-beta)]
         t0^[beta/(2(1-beta))]
         max(t0,t2)^[(1-2beta)/(2(1-beta))]`.                  (3.4)

The local determinant penalty is therefore strictly weaker than the standalone `Delta^(-1/4)` payment whenever `beta>0`. Since `t2=pi Delta^(-1/2)`, the exponent of `Delta^(-1)` in (3.4), in the regime `t2>=t0`, is only

`(1-2beta)/[4(1-beta)]`,                                      (3.5)

which decreases continuously from `1/4` at `beta=0` to `0` as `beta` increases to `1/2`.

### 3.2 Critical case `beta=1/2`

If `t2<=t0`, the same elementary split gives `J<=4 sqrt(t0)`.

If `t2>t0`, set

`T=t2^2/t0`.

Then

`J <=2 sqrt(t0)
    + sqrt(t0) int_(t0)^T dt/t
    +2t2/sqrt(T)`

` =4 sqrt(t0)+2 sqrt(t0) log(t2/t0)`.

Hence, uniformly,

`J <= 2 sqrt(t0)[2+log_+(t2/t0)]`,                             (3.6)

and therefore

`H(R) <= 2 sqrt(2/pi) sqrt(t0)
         [2+log_+(t2/t0)]`.                                   (3.7)

Thus the strict condition `theta>q` from the previous ridge half-Riesz theorem is **not** a hard analytic barrier. At the exact threshold `theta=q` (`beta=1/2`), any genuine physical cross-two collision tail closes the half-Riesz integral, with only logarithmic dependence on the local determinant scale.

### 3.3 Supercritical comparison

For completeness, if `beta>1/2`, the local tail is unnecessary and

`J <= [2+1/(beta-1/2)] sqrt(t0)`,                              (3.8)

recovering the qualitative content of the previous ridge theorem. The new content is (3.4) and especially the endpoint (3.7).

## 4. Linear small-ball consequence after one physical square

Suppose the full quadratic form admits an exact original-coordinate completion

`Q=d(Z+h(W))^2+R(W)`,  `d!=0`,                                (4.1)

where `Z` is one original coordinate, independent of the remaining original coordinates `W`, and has density at most one. Conditional on `W`,

`p_(Q|W)(y) <= |d|^(-1/2)|y-R(W)|^(-1/2)`.

Therefore

`||p_Q||_infinity <= |d|^(-1/2) H(R)`.                        (4.2)

Combining (4.2) with (3.4) or (3.7) gives a **linear interval small-ball estimate** even in the ridge-subcritical and ridge-critical regimes, provided the same residual has a valid account02/B03 cross-two tail.

In particular, at the exact ridge threshold `theta=q`,

`||p_Q||_infinity
 <= |d|^(-1/2) 2 sqrt(2/pi) sqrt(t0)
    [2+log_+( pi Delta^(-1/2)/t0 )]`.                          (4.3)

This proves essential boundedness/absolute continuity in the stated branch. It does **not** by itself prove continuity.

## 5. Required partner application: the m=2 endpoint of the singleton-plus-two-banks family

Consider the mandatory obstruction family

`A_m=[1] direct_sum J_m/m direct_sum (-J_m/m)`.

The previous r12 report handled all `m>=3` by a strict ridge certificate, but at `m=2` the natural balanced residual cut lies exactly on the former threshold and r12 invoked a separate two-variable endpoint theorem.

The new hybrid argument closes this endpoint using the named account02/B03 collision theorem itself.

Pivot the singleton (`d=1`). For `m=2`, split each two-point bank one-versus-one. The residual cross block is

`C=diag(1/2,-1/2)`,

so

`Delta=|det C|=1/4`,  `t2=pi Delta^(-1/2)=2pi`.               (5.1)

Use the same block for the regularized ridge certificate with

`gamma=1/2`, `q=1`.

Then

`K=(1/2)I_2`, `theta=1=q`, `D_ridge=4`,                       (5.2)

so `beta=1/2`, and

`t0 = [pi e sqrt(2)/(2 gamma)] D_ridge^(-1/(2 theta))
    = pi e/sqrt(2)`.                                          (5.3)

Hence

`t2/t0 = 2 sqrt(2)/e = 1.0405201900...`.                      (5.4)

Using (3.7),

`H(R)
 <= 2 sqrt(2/pi) sqrt(pi e/sqrt(2))
    [2+log(2 sqrt(2)/e)]`

` = 7.998443... < 8`.                                        (5.5)

Since the singleton pivot has `d=1`,

`||p_(Q_2)||_infinity < 8`.                                  (5.6)

This is a genuine use of the partner's dependence-safe pair-collision bound at the exact effective-dimension threshold. It improves the previous r12 endpoint bound `32` and shows that the strict inequality `theta>q` was an artifact of integrating the ridge envelope alone, not a true barrier once the collision tail is retained.

For `m>=3`, the already-proved strict ridge branch remains available; for `m=1`, the diagonal theorem applies. This family is still only a structural control, not the full conjecture.

## 6. What this changes in the full proof search

The previous analytic branch required `theta>q` behind a physical square. The present theorem enlarges it to a quantitative **hybrid cone**:

- `theta>q`: ridge alone pays the half-Riesz kernel;
- `theta=q`: a cross-two tail pays the missing logarithmic endpoint by (3.7);
- `theta<q`: the same tail still closes the half-Riesz integral, with determinant exponent (3.5), which becomes arbitrarily small as `theta/q` approaches one from below.

Thus a future structural reduction does not need a uniform local cross-two determinant whenever the ridge effective dimension is nearly critical. It is enough to control the tradeoff

`(q-theta) * log(1/Delta)`

at the appropriate scale (more precisely the power in (3.5), with the logarithmic endpoint (3.7)). This is a strictly weaker structural obligation than paying `Delta^(-1/4)` in isolation.

The first unpaid implication remains global and structural: from only three eigenvalues of modulus at least one, force a product-preserving alternative that provides either a direct ridge/cross-rank-three branch, a physical square plus the new hybrid ridge/cross-two tradeoff, or a grouped/hyperbolic branch. The known singleton-plus-two-banks and Pluecker/pivot-support examples forbid asserting one fixed local certificate universally.

The new scalar worst-conditioning route from owner revision 2026-09-22.11 is also now refuted by source-valid examples, so no `sup_b` conditional-density premise is used here; any scalar-residual synthesis must average before taking a worst fiber.

## 7. Verification

The calculus was checked independently by direct symbolic differentiation of the split-bound objective and by numerical evaluation of the `m=2` endpoint. The numerical constants are:

`t0 = 6.038503978383308`,

`t2 = 6.283185307179586`,

`t2/t0 = 1.040520190045778`,

`H(R) <= 7.998442995283726`.

These checks only verify the algebra/numerics; Sections 3--5 contain the proof.

## 8. Status

**ESSENTIAL_STEP_APPLIED.** The hybrid time integral is proved and removes the strict ridge half-Riesz threshold when a dependence-safe cross-two tail is present. It does not supply the missing exhaustive matrix decomposition, so the full QFORM conjecture remains **OPEN**. Continuity is not proved in the square/hybrid branch.
