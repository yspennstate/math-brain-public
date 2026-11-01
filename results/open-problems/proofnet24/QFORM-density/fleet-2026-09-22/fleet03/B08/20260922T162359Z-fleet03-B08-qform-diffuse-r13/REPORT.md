# fleet03/B08 — ridge-Lp plus physical-square closure below the L-infinity ridge threshold

**Run:** `20260922T162359Z-fleet03-B08-qform-diffuse-r13`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Initial owner revision:** `2026-09-22.5`; **pre-publication revision:** `2026-09-22.6` (same sole QFORM target; later control honored)  
**Assignment:** Diffuse eigenvector case  
**Classification:** `PROVED_SUPPORTING_THEOREM / TARGET-RELEVANT HYBRID BRANCH / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and mechanism change

The full target remains: for every dimension, independent real coordinates with probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove one universal finite essential density bound for `Q=X^TAX`, or give a valid target counterexample. Continuity is a separately requested strengthening.

This run preserves the live corrections. It uses neither law-uniform pointwise stationary-phase decay, post-rotation independence, unrestricted fiber suprema, nor a claimed universal good small principal minor. The preceding B08 run used a fractional-`q` ridge theorem to obtain an `L^infinity` conclusion only when the ridge effective dimension `theta` exceeded `2q`. The present run changes mechanism: first extract an `L^p`, `p>2`, density from the ridge Fourier envelope already when `theta>q`; then spend one genuine original-coordinate scalar square to upgrade that `L^p` density to `L^infinity`. Thus one physical pivot halves the ridge effective-dimension threshold required by this route.

The analytic source is the complete one-scale ridge theorem

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`

at

`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

For an original-coordinate cross block `B`, scale `gamma>0`, and `q in [1,2]`, define

`K=B B^T (gamma^2 I+B B^T)^(-1)`, `theta=tr K`, `D=det(I+B B^T/gamma^2)`.

If `max_i K_ii<=q/2`, that theorem proves

`|phi_R(t)| <= min(1,(t0/|t|)^beta)`,

with

`beta=theta/(2q)`,
`t0=L_q/(2 gamma) D^(-1/(2theta))`,
`L_q=pi e sqrt(2/q)`.

The theorem was originally inverted in `L^1`, requiring `theta>2q`. The new observation is to invert it in fractional `L^s` instead.

The designated partner `fleet04/B08` still has no completed current-QFORM handoff or scientific directory at the source-bound refresh, so no theorem is attributed to that worker. A compatible completed fleet04 theorem is nevertheless applied quantitatively in Section 6: fleet04/B18 `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, scientific commit `441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`.

## 2. Ridge Fourier envelope implies an L^p output below the L-infinity threshold

### Lemma 2.1 — `QFORM-RIDGE-LP-BELOW-ENDPOINT-v1`

Suppose a real random variable `R` has characteristic function satisfying

`|phi_R(t)| <= min(1,(t0/|t|)^beta)`

for some `t0>0`, `beta>0`. Let `1<s<=2` and assume `beta s>1`. Put `p=s/(s-1)`. Then `R` has a density in `L^p` and

`||p_R||_p
 <= C_s (2pi)^(-1/s)
    [2 t0 beta s/(beta s-1)]^(1/s)`,                         (2.1)

where

`C_s=s^(1/(2s))/p^(1/(2p)) <=1`

is the sharp Beckner Hausdorff--Young factor for the Fourier convention `hat f(t)=int exp(itx)f(x)dx`.

### Proof

The envelope gives exactly

`int_R |phi_R(t)|^s dt
 <= 2 t0 + 2 int_(t0)^infinity (t0/t)^(beta s)dt
 = 2 t0 beta s/(beta s-1)`.                                  (2.2)

Since `s<=2`, inverse Hausdorff--Young yields an `L^p` inverse Fourier transform and

`||p_R||_p <= C_s(2pi)^(-1/s)||phi_R||_s`,

which together with (2.2) proves (2.1). Since a characteristic function with an `L^p` inverse represents the underlying probability law distributionally, this inverse is the density of `R`. QED.

For the ridge theorem, `beta=theta/(2q)`. Consequently, if `theta>q`, then one can choose `s<2` sufficiently close to two so that `beta s>1`. This is strictly weaker than the `theta>2q` condition needed for direct `L^1` Fourier inversion.

## 3. General dependent-square smoothing from an L^p base

### Lemma 3.1 — `QFORM-DEPENDENT-SQUARE-LP-SMOOTHING-v1`

Let `R` have density `p_R in L^p` for some `p>2`, and write

`s=p/(p-1) in (1,2)`, `M=||p_R||_p`.

Assume that, for almost every `r`, the conditional law of a real variable `V` given `R=r` has a density bounded by one. No independence of `R` and `V` is required. For `a!=0`, let

`T=R+aV^2`.

Then `T` has an essentially bounded density and

`boxed(
 ||p_T||_infinity
 <= 2 |a|^(-1/2) (1-s/2)^(-1/2) M^(s/2).
)`                                                               (3.1)

### Proof

For `a>0`, the conditional density of `aV^2` is bounded by

`a^(-1/2) u^(-1/2) 1_(u>0)`.

Hence

`p_T(t)<=a^(-1/2) int_(r<t) p_R(r)(t-r)^(-1/2)dr`.              (3.2)

Fix `L>0`. Holder with conjugate exponents `p,s` on the near part gives

`int_0^L p_R(t-u)u^(-1/2)du
 <= M [int_0^L u^(-s/2)du]^(1/s)
 = M(1-s/2)^(-1/s)L^(1/s-1/2)`.                                (3.3)

The far part is at most `L^(-1/2)||p_R||_1=L^(-1/2)`. Put

`A=M(1-s/2)^(-1/s)`

and choose `L=A^(-s)`. Then the two terms are equal and their sum is

`2 A^(s/2)=2(1-s/2)^(-1/2)M^(s/2)`.

Multiplying by `a^(-1/2)` gives (3.1). Reflection handles `a<0`. QED.

At `p=3`, hence `s=3/2`, (3.1) becomes

`||p_T||_infinity <=4 |a|^(-1/2)||p_R||_3^(3/4)`,

exactly recovering the completed `QFORM-DEPENDENT-SQUARE-L3-SMOOTHING-v1` constant from fleet01/B11. Thus the general formula is consistent with an independently completed worker theorem at that exponent.

## 4. Main hybrid theorem: one physical square plus ridge effective dimension > q

Let `A` be written around one ORIGINAL coordinate as

`A=[[a,b^T],[b,C]]`, `a!=0`,

and define the Schur complement

`S=C-bb^T/a`.

Writing the remaining independent coordinates as `Y`, exact completion of the square in the original coordinate gives

`Q=Y^T S Y + a(X_0+a^(-1)b^T Y)^2`.                            (4.1)

Let `B=S[I,J]` be any cross block on a partition of some original residual coordinates, and form its ridge quantities `K,theta,D` at scale `gamma`.

### Theorem 4.1 — `QFORM-PIVOT-PLUS-RIDGE-LP-v1`

Assume for some `q in [1,2]`

`max_i K_ii<=q/2`.

Choose `s in (1,2)` satisfying

`theta s>2q`.                                                     (4.2)

Put

`beta=theta/(2q)`,
`t0=pi e sqrt(2/q)/(2gamma) * D^(-1/(2theta))`,
`p=s/(s-1)`.

Then `Q` has an essentially bounded density and

`boxed(
 ||p_Q||_infinity
 <= (2/sqrt(pi)) |a|^(-1/2)(1-s/2)^(-1/2) C_s^(s/2)
    [ t0 * beta s/(beta s-1) ]^(1/2).
)`                                                               (4.3)

In particular, the existence of a usable `s<2` requires only

`theta>q`,                                                         (4.4)

whereas direct ridge `L^infinity` inversion requires `theta>2q`.

### Proof

Apply the source ridge characteristic-function theorem to

`R=Y^T S Y`.

Lemma 2.1 gives

`M:=||p_R||_p
 <= C_s(2pi)^(-1/s)[2t0 beta s/(beta s-1)]^(1/s)`.              (4.5)

In (4.1), set `V=X_0+a^(-1)b^T Y`. Because `X_0` is independent of all components of `Y`, conditioning on `R=r` makes the law of `V` a mixture of translations of the original density of `X_0`. Hence its conditional density remains bounded by one. Lemma 3.1 applies. Raising (4.5) to the power `s/2` and simplifying the factors of `2pi` gives exactly (4.3). QED.

The conclusion here is **essential boundedness / absolute continuity**. This argument does not by itself establish a continuous representative, so no continuity claim is made for Theorem 4.1.

## 5. Two diffuse ridge directions now suffice after a scalar pivot

### Corollary 5.1 — `QFORM-PIVOT-PLUS-TWO-RIDGE-DIRECTIONS-v1`

Assume the residual cross block `B` has at least two singular values at least `sigma>0`. Set

`gamma=sigma/sqrt(6)`

and suppose

`max_i (K_gamma)_ii<=1/2`.                                      (5.1)

Then

`boxed(
 ||p_Q||_infinity
 <= 4 sqrt((9/2)sqrt(3e)) / sqrt(|a| sigma)
 < 14.34 / sqrt(|a| sigma).
)`                                                               (5.2)

### Proof

Use `q=1`, `s=3/2`. Two singular values at least `sigma` imply

`theta>=2 sigma^2/(gamma^2+sigma^2)=12/7`.

Thus `beta>=6/7` and

`beta s>=9/7`,
`beta s/(beta s-1)<=9/2`.                                       (5.3)

Also `log D>=theta`, hence

`t0<=pi sqrt(e/2)/gamma = pi sqrt(3e)/sigma`.                    (5.4)

Substitute (5.3)-(5.4) into (4.3), use `1-s/2=1/4` and `C_(3/2)<=1`, and obtain (5.2). QED.

This is the main new geometric payment: after one genuine physical scalar pivot, only **two** diffuse residual cross directions are needed. A three-cross-direction `L^1` certificate is no longer necessary.

The choice `gamma=sigma/sqrt(6)` is also the optimizer of this simple two-singular-value `q=1,s=3/2` bound: writing `gamma=c sigma`, admissibility needs `c^2<1/2`, and the controlling denominator is `c(1-2c^2)`, maximized at `c=1/sqrt(6)`.

## 6. Concrete localized-pivot + diffuse-residual branch and fleet04 application

Suppose the residual Schur matrix has a two-dimensional large spectral component

`S=R Lambda R^T+E`, `R^TR=I_2`,

with both singular values of `Lambda` at least one,

`mu=max_i ||r_i||^2<=1/32`,
`||E||op<=1/64`.                                                     (6.1)

The signed physical-coordinate partition lemma from the preceding B08 work gives a partition `I|J` with both selected-frame Gram matrices at least

`alpha=(1-sqrt(2mu))/2 >=3/8`.                                      (6.2)

Hence the selected residual cross block `B0` has two singular values at least `alpha`. For the actual block `B=B0+E[I,J]`,

`sigma>=alpha-1/64 >=23/64`.                                        (6.3)

The range projection of `B0` has coordinate leverage at most

`ell<=mu/alpha <=1/12`.                                             (6.4)

At `gamma=sigma/sqrt(6)`, the source ridge perturbation inequality yields

`max_i K_ii
 <= [sqrt(1/12)+sqrt(6)/23]^2
 < [29/100+107/1000]^2
 = (397/1000)^2
 <1/2`.                                                             (6.5)

(`396/1000` also works if sharper decimal certificates are used; the displayed `397/1000` keeps the rational check elementary.) Therefore Corollary 5.1 applies.

If in addition the physical pivot obeys the fixed-scale certificate

`|a|>=1/312`,                                                        (6.6)

then

`||p_Q||infinity <423`,                                              (6.7)

and a completely coarse rational estimate using only `e<3` gives the safe bound

`boxed(||p_Q||infinity<434)`.                                       (6.8)

Indeed (5.2) squared is at most `72 sqrt(3e)/(|a|sigma)<216/(|a|sigma)`, while (6.3),(6.6) give `|a|sigma>=23/19968`; thus the square of the bound is less than `216*19968/23<434^2`.

This connects directly to the completed fleet03/B12 target-level reduction: failure of its diffuse `|lambda|>=1/39` spectral-window branch forces an original coordinate with either `|A_ii|>1/312` or off-diagonal column norm `>1/312`. Theorem 4.1 now closes a nontrivial part of that heavy branch whenever the scalar-pivot alternative occurs and its Schur residual retains two diffuse large directions as in (6.1). The off-diagonal-only alternative and the non-diffuse Schur residual remain unpaid.

### Actual fleet04 theorem application

On the stronger residual ridge branch `theta>2q`, the source ridge theorem itself gives a residual `L^infinity` cap `M`. The completed fleet04/B18 theorem `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1` then applies directly to (4.1):

`||p_Q||infinity <=2 sqrt(M/|a|)`.                                  (6.9)

For the standard three-singular-value `q=1`, `gamma=sigma/sqrt(6)` certificate,

`M<=9 sqrt(3e)/(2sigma)`,

so the actual fleet04 result yields

`boxed(
 ||p_Q||infinity
 <= 3 sqrt(2)(3e)^(1/4)/sqrt(|a|sigma)
 <7.17/sqrt(|a|sigma).
)`                                                                    (6.10)

This is a literal application of completed fleet04 mathematics to an inequality, not a nominal citation. The designated fleet04/B08 result was unavailable, and no such result is fabricated.

## 7. What this changes and what remains

The new threshold `theta>q` is the substantive advance. It shows that a localized original coordinate is not merely an obstruction to diffuse ridge arguments: its square can supply the missing half-order smoothing and reduce the residual ridge demand from three effective directions to just over one `q`-unit of effective dimension. In the clean `q=1` corollary, two well-spread residual directions suffice.

This does **not** prove the full conjecture. A complete proof still needs an exhaustive product-preserving reduction showing that every target matrix either enters a ridge-certified diffuse branch, has a usable scalar pivot with enough residual ridge mass, or enters another already-controlled grouped-coordinate/star/bank mechanism. The singleton-plus-two-banks correction prevents replacing this with a naive one-good-minor or rank-three-cut dichotomy.

The next B08 obligation is therefore `QFORM-HEAVY-ROW-TO-PIVOT-OR-RIDGE-v1`: starting from the fixed-scale heavy physical row supplied by the spectral-window failure, prove an exhaustive inequality that either extracts a scalar pivot with `theta_res>1` at an admissible ridge scale, or pays the off-diagonal-heavy row by a grouped-coordinate bilinear/bank estimate. The full universal QFORM conjecture remains **OPEN / NOT PROVED**.

## 8. Verification scope

The companion checker verifies the exact rational margins in (6.2)--(6.8), the numerical constants in (5.2),(6.7),(6.10), and the optimization point `c=1/sqrt(6)`. It is arithmetic regression evidence only. The analytic proof is Sections 2--6 plus the source ridge theorem and the cited completed fleet04 smoothing theorem.
