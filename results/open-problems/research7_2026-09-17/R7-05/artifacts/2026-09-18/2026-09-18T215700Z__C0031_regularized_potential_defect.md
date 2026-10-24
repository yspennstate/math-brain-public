Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# C0031 — exact lower-log defect, atomic obstruction screen, and smoothing reduction

Target: Bordenave–Chafaï, *Around the circular law*, Section 6.6 remark after Theorem 6.2: upgrade the heavy-tailed eigenvalue ESD convergence from in probability to almost sure without imposing bounded density.

Frozen source metric: `BC_AS=0` before and after this artifact. Nothing below is a full source resolution.

Notation. Let `a_n` be the source normalization (regularly varying with index `1/alpha`, `0<alpha<2`), let

`A_n = a_n^{-1} X_n`,

and for fixed `z in C` let `s_1 >= ... >= s_n >= 0` be the singular values of `A_n-zI`. Write

`nu_{n,z} = n^{-1} sum_j delta_{s_j}`.

The source already supplies convergence of the Hermitized singular-value laws and the upper-log control needed away from zero; its explicit unresolved difficulty is the logarithm near zero.

## 1. B2 — attack the negation: atomic singularity is not the obvious counterexample

The source permits distributions without a bounded density, including laws with atoms. A first possible obstruction to almost-sure convergence is therefore that an admissible atomic heavy-tailed law might make the matrices exactly singular infinitely often.

The simplest mechanisms are nevertheless summable for every fixed nondegenerate entry law.

Let `xi,xi'` be independent copies of one entry and define

`rho := P(xi=xi') = sum_x P(xi=x)^2`,

where the sum runs over atoms. Since the law is nondegenerate, `rho<1`. For two specified independent rows of an `n x n` iid matrix,

`P(row_i=row_j)=rho^n`.

Hence

`P(some pair of equal rows) <= n(n-1) rho^n / 2`,

and

`sum_n P(some pair of equal rows) < infinity`.

Similarly, if `q=P(xi=0)<1`,

`P(some zero row) <= n q^n`,

again summable. Borel–Cantelli therefore shows that neither repeated rows nor zero rows can by themselves produce infinitely many singular dimensions under the standard nested iid-array coupling.

This does **not** prove summability of the full singularity probability. More complicated arithmetic linear dependencies remain possible. It does rule out the two most immediate atom-based counterexample mechanisms and makes the source's small-singular-value obstruction genuinely quantitative rather than merely an exact-zero issue.

A later-literature check also prevents a false shortcut. Livshyts (J. Analyse Math. 145 (2021), arXiv:1811.07038) proves sharp square-matrix small-ball estimates under bounded concentration plus regularized moment/column-size hypotheses. For a fixed alpha-stable-domain law with `alpha<2`, the Euclidean size of an iid column is naturally order `n^{1/alpha}` rather than `sqrt(n)`, so the square corollaries normalized at variance scale do not directly furnish the source-scope summable hard-edge estimate. Yi Han's 2024/2025 Lévy least-singular-value result gives arbitrarily high polynomial probability, but for strict rectangular aspect ratio `N/n -> a>1`, not the square hard edge. Thus the admission is not invalidated by those papers.

## 2. B11 — dualize the missing lower-log control

For `eta>0`, define the regularized logarithmic potential

`U_{n,eta}(z) := -(1/2) int log(s^2+eta^2) d nu_{n,z}(s)`.

Whenever `A_n-zI` is nonsingular, the true potential is

`U_n(z) := - int log s d nu_{n,z}(s)`.

For Lebesgue-a.e. `z`, simultaneous nonsingularity for all `n` holds for every fixed matrix realization, because the exceptional set is the countable union of the finite spectra.

Define the regularization defect

`R_{n,eta}(z) := U_n(z)-U_{n,eta}(z)`

`= int (1/2) log(1+eta^2/s^2) d nu_{n,z}(s) >= 0`.

This defect has an exact representation in terms of the small-singular-value counting function

`F_{n,z}(t):=nu_{n,z}([0,t])`:

`R_{n,eta}(z) = int_0^infinity F_{n,z}(t) * eta^2/[t(t^2+eta^2)] dt`.      (2.1)

### Proof of (2.1)

For fixed `s>0`,

`f_eta(s):=(1/2)log(1+eta^2/s^2)`

has `f_eta(infinity)=0` and

`-f_eta'(t)=eta^2/[t(t^2+eta^2)]`.

Therefore

`f_eta(s)=int_s^infinity eta^2/[t(t^2+eta^2)] dt`.

Integrate against `nu_{n,z}` and apply Tonelli (all terms are nonnegative):

`int f_eta(s)dnu(s)
 = int_0^infinity nu([0,t]) eta^2/[t(t^2+eta^2)]dt`.

If there is mass at zero, both sides are `+infinity`, so the identity remains correct in the extended sense.

### Consequence

The source's unresolved issue can be stated without singling out `s_n`: after the already-established fixed-`eta` Hermitization limit, the missing pathwise interchange is precisely the vanishing of the nonnegative defects

`lim_{eta downarrow 0} limsup_{n to infinity} R_{n,eta}(z)=0`              (2.2)

for Lebesgue-a.e. `z`, almost surely.

Thus a summable lower bound on the single least singular value is only one sufficient mechanism. Equation (2.1) shows a potentially weaker route: control the **integrated singular-count profile** `F_{n,z}(t)` near zero. A rare extremely small `s_n` costs only mass `1/n`; it is dangerous only when its logarithmic depth compensates that `1/n`, or when a larger cloud of small singular values accumulates.

For example, if on an event one has a cutoff `tau_n>0`, no singular values below `tau_n`, and for `tau_n<=t<=1`

`F_{n,z}(t) <= C t^gamma`

with some `gamma>0`, then (2.1) gives, for `tau_n<eta<1`,

`R_{n,eta}(z)
 <= C int_{tau_n}^eta t^{gamma-1}dt
    + C eta^2 int_eta^1 t^{gamma-3}dt
    + eta^2/2`.

Hence the profile portion is `O(eta^{min(gamma,2)})` (with the usual `eta^2 log(1/eta)` at `gamma=2`), apart from the effect of how far the cutoff `tau_n` lies below `eta`. This identifies a concrete way to beat the crude strategy "make P(s_n<n^{-c}) summable": prove a high-probability small-singular **count profile** plus only enough control on the logarithmic depth of the final few singular values.

This is the main new mathematical reduction of the run.

## 3. B5 — add a parameter: fixed-eta potentials are robust under density smoothing

The source already proves the desired almost-sure eigenvalue theorem when the entry distribution has bounded density. A natural idea is to smooth the entry law and then remove the smoothing. Direct eigenvalue comparison is unsafe for nonnormal matrices. The regularized potential, however, is quantitatively stable.

For an `n x n` complex matrix `M`, set

`Phi_eta(M):=(1/(2n)) log det(MM^*+eta^2 I)`.

### Lemma (Frobenius Lipschitz estimate)

For all matrices `M,N` and `eta>0`,

`|Phi_eta(M)-Phi_eta(N)| <= ||M-N||_F/(2 eta sqrt(n))`.                 (3.1)

### Proof

Along `M_t=M+t(N-M)`, differentiation gives

`d/dt Phi_eta(M_t)
 = (1/n) Re Tr[(M_t M_t^*+eta^2 I)^{-1} M_t (N-M)^*]`.

The singular values of `(M_t M_t^*+eta^2 I)^{-1}M_t` are

`s/(s^2+eta^2) <= 1/(2eta)`.

Its Frobenius norm is therefore at most `sqrt(n)/(2eta)`. Cauchy–Schwarz for the Hilbert–Schmidt inner product yields (3.1) after integration in `t`.

Now couple the original entries `xi` with smoothed entries `xi^(sigma)=xi+sigma g`, where `g` is standard Gaussian and `sigma>0` is fixed. This smoothed law has bounded density and remains in the same alpha-stable domain of attraction, so the source's bounded-density clause applies to the corresponding matrices. At normalized matrix scale,

`A_n^(sigma)-A_n = sigma a_n^{-1} G_n`.

By the strong law for Gaussian squares,

`||G_n||_F = n(1+o(1))` almost surely (under the natural infinite-array coupling). Therefore from (3.1), for every fixed `eta>0`,

`|U_{n,eta}^{(sigma)}(z)-U_{n,eta}(z)|
 <= [sigma/(2eta)] * [sqrt(n)/a_n] * (1+o(1))`.

Because `a_n` is regularly varying with index `1/alpha>1/2`,

`sqrt(n)/a_n -> 0`.

Consequently

`U_{n,eta}^{(sigma)}(z)-U_{n,eta}(z) -> 0` almost surely              (3.2)

for every fixed `sigma,eta>0`.

So bounded-density approximation completely transfers the **regularized** logarithmic potentials to the original nonsmooth law. The smoothing parameter is not the hard part.

### Why this does not close C0031

The unregularized eigenvalue potential is highly unstable for nonnormal matrices. Passing from (3.2) to `eta=0` is exactly the defect problem (2.2). Tiny perturbations can move nonnormal eigenvalues macroscopically, so one cannot replace this with a deterministic eigenvalue-continuity argument. In other words, Gaussian smoothing plus source bounded-density convergence reaches the same wall from the opposite direction: all fixed-eta information is robust, and **only the pathwise removal of eta remains**.

This is useful because it rules out a broad class of redundant future attacks: any route that merely regularizes the entry density but does not give new lower-log information cannot settle the source endpoint.

## 4. Current strongest formulation of the target

Combining B11 and B5, the source problem is reduced to a positive quantity. For a.e. `z`, the fixed-eta potentials can be obtained either directly from the source's singular-value-law convergence or via bounded-density smoothing. What is still needed is an almost-sure estimate forcing

`lim_{eta downarrow0} limsup_n
 int_0^infinity F_{n,z}(t) eta^2/[t(t^2+eta^2)] dt = 0`.              (4.1)

This suggests a different next attack from the intake's raw least-singular-value Borel–Cantelli route: estimate a **dyadic lower-tail energy**

`E_n(z;J) := sum_{j>=J} 2^{-j}??`

more naturally in logarithmic coordinates. Setting `t=e^{-u}` in the dangerous `t<=eta` range, (2.1) is comparable to

`int_{log(1/eta)}^infinity F_{n,z}(e^{-u}) du`.

Thus the mathematically relevant object is the area under the small-singular counting curve on log scale. It may be summable/concentrated even when the event concerning the single smallest singular value is not.

## 5. Literature/status check made during this run

- Bordenave–Chafaï, arXiv:1109.3343v4 / Probability Surveys 9 (2012): general heavy-tail ESD convergence in probability; bounded-density special case almost surely; explicit statement that the general a.s. upgrade is believed but not reached due to slow small-singular-value controls.
- Livshyts, arXiv:1811.07038 / J. Analyse Math. 145 (2021): sharp square small-ball results under bounded concentration and moment/size hypotheses; does not directly supply the fixed-law alpha-stable square estimate needed here.
- Livshyts–Tikhomirov–Vershynin, arXiv:1909.04219 / Ann. Probab. 49 (2021): square estimate under uniform anti-concentration and an `E||A||_HS^2=O(n^2)` hypothesis; the infinite-second-moment alpha-stable regime falls outside that hypothesis.
- Yi Han, arXiv:2412.06246 (2024/2025): arbitrarily high polynomial confidence at the correct alpha-stable scale for `N/n -> a>1`; square hard edge not covered.
- Dabagia–Fernandez, arXiv:2408.14389 (2024/2025): near-optimal rectangular estimates under `2+beta` moments, or anti-concentration in a rectangular theorem; does not by itself settle the square infinite-variance endpoint.

A bounded search did not find a full source-scope resolution. This is negative evidence only, not a novelty/open-status certificate.

## 6. Next attack

Frozen metric remains `BC_AS=0`.

The most promising next mathematical object is the block/dyadic lower-log energy in (4.1), not another checker for `s_n` alone. Three nonrepeating next methods proposed for the following ordinary run: B6 deform from the bounded-density solved case while tracking (4.1); B18 translate (4.1) into dyadic counts of negative singular-value logs; B25 double-count row-to-random-subspace distance events to control the aggregate count profile rather than only the minimum.
