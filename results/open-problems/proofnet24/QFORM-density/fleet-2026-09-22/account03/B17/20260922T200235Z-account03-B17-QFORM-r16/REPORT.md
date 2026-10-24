SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B17, 2026-09-22T20:02:35Z.
attacking: fixed spectral-floor sharp witnesses via a sharp product-law variance rigidity theorem, plus a strict fourth-Gaussian-mode gap below 3sqrt(2).

# account03/B17 — sharp spectral-tail variance rigidity and a fourth-mode Gaussian gap

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260922T200235Z-account03-B17-QFORM-r16`  
Assignment: sharp constant and witnesses  
Status: `NEW SUPPORTING THEOREMS / FULL CONJECTURE OPEN`  
Execution memory: `WITHOUT_VERIFIED_BRAIN`

## 1. Target and correction discipline

The full target remains the unrestricted essential-density conjecture for `Q=X^T A X` under independent one-dimensional density caps `f_i<=1` and at least three eigenvalues `|lambda(A)|>=1`. No Gaussian, moment, compact-support, or eigenbasis-independence assumption is inserted into the full target.

This run does **not** use the refuted arbitrary-joint coarea estimate, any worst conditional-density cap, the false law-uniform pointwise stationary-phase estimate, or a single-minor/cross-rank dichotomy. The new variance theorem below is stated in its honest finite-fourth-moment scope; the completed extreme-product reduction is then used to apply it to compact finite-fragment extremizers. The full density conjecture remains open because a lower bound on output variance does not by itself upper-bound a density peak.

The prepublication control refresh observed `yspennstate/math-research-brain@ceeebe9f3013c73e7622acac19fe2d5e26789b67`, OWNER CONTROL revision `2026-09-22.15`, with QFORM still the sole target and no B17 pause/stop.

## 2. A sharp one-dimensional residual-quadratic inequality

### Lemma 2.1 — cap-one quadratic residual floor

Let `X` be any real random variable with probability density `0<=f<=1`. For every `alpha,beta in R`, in the extended sense,

`E (X^2-alpha X-beta)^2 >= 1/180`.

The constant `1/180` is sharp. Equality is attained by a unit interval law after the appropriate translation and choice of `alpha,beta`.

### Proof

Complete the square. Put `h=alpha/2` and `d=beta+h^2`. After translating the density by `h`, it is enough to prove

`int_R (x^2-d)^2 f(x) dx >= 1/180`

for every `d in R`, `0<=f<=1`, `int f=1`.

For fixed `d`, the bathtub principle says the minimum over such densities is attained by an indicator of a measurable set of length one on which the weight

`w_d(x)=(x^2-d)^2`

is smallest.

There are exactly two geometries.

**Case 1: `d<=1/8`.** The length-one lowest sublevel set is the centered interval `[-1/2,1/2]`. Indeed a sublevel set is

`{|x^2-d|<=s}`;

when the inner radius has collapsed, length one forces `sqrt(d+s)=1/2`, i.e. `s=1/4-d`, and the collapse condition `d<=s` is exactly `d<=1/8`. Hence

`I(d)=int_{-1/2}^{1/2}(x^2-d)^2 dx
     =d^2-d/6+1/80`.

This quadratic is minimized at `d=1/12`, giving

`I(1/12)=1/180`.

**Case 2: `d>1/8`.** The lowest sublevel set is a symmetric shell

`[-b,-a] union [a,b]`,

with `a>0`, `b-a=1/2`, and

`d=(a^2+b^2)/2`.

Writing `b=a+1/2`, exact integration gives

`2 int_a^b (x^2-d)^2 dx
 = (80a^2+40a+7)/960
 = 1/180 + a^2/12+a/24+1/576
 > 1/180`.

Thus the global minimum is exactly `1/180`. Equality in Case 1 occurs for the centered unit interval with `d=1/12`; undoing the translation gives the asserted equality family. `QED`

This lemma is stronger than the usual variance floor `Var(X)>=1/12`: it says that no affine function can approximate the quadratic `X^2` in `L^2` under a cap-one law better than the unit interval does.

## 3. Main theorem: sharp Frobenius variance rigidity for product inputs

### Theorem 3.1 — `Var(X^T A X) >= ||A||_F^2/180`

Let `X_1,...,X_n` be independent real random variables with densities at most one and finite fourth moments. Let `A=(a_ij)` be real symmetric and put `Q=X^T A X`. Then

`Var(Q)
 >= (1/180) sum_i a_ii^2
    +(1/36) sum_{i<j} a_ij^2
 >= (1/180)||A||_F^2`.

The universal Frobenius constant `1/180` is sharp, including inside the QFORM target class.

### Proof

Let `mu_i=E X_i`, `xi_i=X_i-mu_i`, and `sigma_i^2=E xi_i^2`. The density cap implies the sharp variance floor

`sigma_i^2>=1/12`.

Expand and center the quadratic form:

`Q-EQ
 = sum_i g_i(xi_i)
   +2 sum_{i<j} a_ij xi_i xi_j`,

where

`g_i(x)=a_ii(x^2-sigma_i^2)+2(A mu)_i x`.

All displayed summands are pairwise orthogonal in `L^2`: different one-coordinate terms are independent and centered; a one-coordinate term against a two-coordinate term leaves a centered factor in the other coordinate; and two distinct pair terms leave at least one coordinate to the first power. Therefore

`Var(Q)=sum_i E g_i(xi_i)^2
        +4 sum_{i<j} a_ij^2 sigma_i^2 sigma_j^2`.

If `a_ii!=0`, Lemma 2.1 applied after dividing by `a_ii` gives

`E g_i(xi_i)^2>=a_ii^2/180`;

if `a_ii=0` the same inequality is trivial. Also

`4 sigma_i^2 sigma_j^2 >=4(1/12)^2=1/36`.

This proves the first bound. Since

`||A||_F^2=sum_i a_ii^2+2 sum_{i<j}a_ij^2`,

the second follows immediately.

For sharpness, take independent `X_i~Unif[-1/2,1/2]` and diagonal `A`. Then

`Var(X_i^2)=1/80-(1/12)^2=1/180`,

so

`Var(X^T A X)=||A||_F^2/180`.

In particular the constant cannot be improved even for target matrices with three coefficients of magnitude at least one. `QED`

### Corollary 3.2 — spectral-count rigidity

For every `delta>0`, let

`N_delta(A)=#{j: |lambda_j(A)|>=delta}`.

Under the hypotheses of Theorem 3.1,

`Var(Q) >= delta^2 N_delta(A)/180`,

hence, whenever `Var(Q)<=V`,

`N_delta(A)<=180V/delta^2`.

This is basis-free because `||A||_F^2=sum_j lambda_j(A)^2`.

### Corollary 3.3 — fixed tail floor forces linearly growing output variance

Assume the QFORM spectral condition and, for some `0<delta<=1`, every eigenvalue after the three designated large modes also has magnitude at least `delta`. Then

`Var(Q)>= [3+(n-3)delta^2]/180`.

This lower bound is exact: for iid centered unit intervals and

`A=diag(1,1,-1, eps_4 delta,...,eps_n delta)`, `eps_j in {+1,-1}`,

one has equality

`Var(Q)=[3+(n-3)delta^2]/180`.

Thus a growing-dimensional witness whose output remains on a bounded variance scale cannot carry a fixed positive spectral floor in all noncore directions. Quantitatively, if one insists on the canonical Gaussian-witness variance scale `V=1/24`, then

`sum_j lambda_j^2 <= 180/24 = 7.5`,

so after paying the three unit core modes the remaining squared spectral mass is at most `4.5`; consequently at most `floor(4.5/delta^2)` extra modes can have magnitude at least `delta`.

This answers the preceding B17 run's fixed-spectral-floor question in a sharp variance sense. It does **not** prove a density gap: a distribution can have large variance and still have a high narrow local peak plus distant tails.

## 4. Completed account04 mathematics applied to the theorem

No completed current-QFORM artifact from the designated partner `account04/B17` was visible at the fresh shared/canonical scans, so none is invented. I apply the compatible completed `account04/B14` extreme-product theorem instead:

- repository: `yspennstate/math-open-problems`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260922T114319Z-b14-qform-extreme-reduction-r1/REPORT.md`;
- result: for every fixed output interval, the sharp small-ball problem over cap-one product densities reduces without loss to product indicators `1_{E_i}`, `|E_i|=1`; compact finite unions of intervals suffice by total-variation approximation.

Every compact finite-fragment approximant has finite fourth moments, so Theorem 3.1 applies to the exact extreme-product search. Therefore any sequence of compact extreme-product witnesses with

`Var(X^TAX)<=V`

and a fixed spectral threshold `delta` satisfies the actual inequality

`N_delta(A)<=180V/delta^2`.

Equivalently, an unbounded-dimensional extreme-product witness carrying a fixed nonzero spectral floor must have output variance tending to infinity. This materially narrows the sharp-witness search while preserving arbitrary fragment positions and separations.

The limitation is explicit: the extreme-product reduction does not supply a uniform output-variance bound, so this is a witness/proof constraint rather than a proof of QFORM.

## 5. A strict fourth-Gaussian-mode gap below `3 sqrt(2)`

The completed Gaussian work shows that `3sqrt(2)` is the ceiling for Gaussian projection limits. The following quantitative refinement shows how a persistent fourth spectral mode moves the canonical Gaussian stress strictly below that ceiling.

### Proposition 5.1 — canonical fourth-mode gap

Let `Z_1,...,Z_4` be iid standard normal, let

`T=Z_1^2+Z_2^2-Z_3^2`,

and let `R=lambda Z_4^2` with `|lambda|>=delta>0`. Let `W` be any random variable independent of `(T,R)`. For `sigma>0`, set

`Q=sigma^2(T+R)+W`.

Then `Q` has a bounded continuous density and

`||p_Q||_infinity
 <= [1/(2sqrt(2)sigma^2)]
    [1-eta(1-exp(-delta/4))]`,

where

`eta=P(Z^2>1)=2(1-Phi(1))=0.317310507862914...`.

At the density-one Gaussian variance floor `sigma^2=1/12`,

`||p_Q||_infinity
 <=3sqrt(2)[1-eta(1-exp(-delta/4))]`.

For `delta=1` this is

`||p_Q||_infinity <=3.944854676307543... <3sqrt(2)`.

### Proof

Let `M=1/(2sqrt(2))`. Since `Z_1^2+Z_2^2` is `chi^2_2`, direct convolution with `Z_3^2` gives the exact density

`p_T(t)=M exp(-t/2)`, `t>=0`,

and, writing `t=-a<0`,

`p_T(-a)=M exp(a/2) erfc(sqrt(a))`.

The elementary inequality `erfc(x)<=exp(-x^2)` for `x>=0` yields

`p_T(t)<=M exp(-|t|/2)` for every real `t`.

Therefore

`p_{T+R}(x)<=M E exp(-|x-R|/2)`.

Put `a=delta/2`. The random variable `Z^2` has a decreasing density on `(0,infinity)`, so the mass of any interval of length at most one is at most `P(Z^2<=1)=1-eta`. Since `R=lambda Z^2`, every interval of length `delta` has `R`-mass at most `1-eta`. Hence for every `x`,

`P(|R-x|<a)<=1-eta`,

and consequently

`E exp(-|x-R|/2)
 <=(1-eta)+eta exp(-a/2)
 =1-eta(1-exp(-delta/4))`.

Scaling by `sigma^2` multiplies density by `sigma^-2`; convolution with the independent `W` cannot increase an `L^infinity` norm and preserves continuity of the bounded continuous core density. `QED`

This is not a theorem for arbitrary product inputs. It is a sharp-witness barrier: the canonical `3sqrt(2)` Gaussian mechanism requires every additional independent Gaussian spectral mode to vanish if one wants to approach the ceiling through this architecture.

## 6. Implication for the sharp-constant search

The two new statements point in the same direction from opposite sides:

1. for arbitrary cap-one **product** inputs with finite fourth moments, a fixed spectral tail forces quadratic output variance at least `||A||_F^2/180`, sharply;
2. for the canonical isotropic **Gaussian** sharp mechanism, even one fourth mode of fixed magnitude creates an explicit strict density gap below `3sqrt(2)`.

Thus the previous full-rank lower-bound construction, whose noncore eigenvalues tend to zero, is not merely a cosmetic singular perturbation. Any attempt to beat or sharply attain `3sqrt(2)` with a persistent high-dimensional spectral tail must use a genuinely non-Gaussian/high-variance mechanism or exploit local concentration together with remote mass; it cannot simply be a bounded-scale Gaussian/CLT continuation with a fixed tail floor.

A nonredundant next B17 attack is therefore: construct or rule out a **high-variance, locally concentrated extreme-product witness** with a fixed spectral tail. The correct quantity to track is simultaneous interval concentration and tail variance, not variance alone. One promising exact question is whether the cap-one product structure forces a tradeoff of the form

`K(Q) * Phi(Var(Q), spectral_tail) <= universal`,

with `Phi` bounded away from zero in the fixed-floor regime. No such tradeoff is proved here.

## 7. Regularity and full-target status

- Theorem 3.1 is a variance theorem; it proves neither absolute continuity nor continuity of the full QFORM output.
- Proposition 5.1 has a bounded continuous Gaussian-core density in its stated scope.
- The full unrestricted essential-density theorem remains `OPEN / NOT PROVED`.
- The owner's additional full-target continuity conclusion remains separately `OPEN`.

No claim of novelty priority is made.
