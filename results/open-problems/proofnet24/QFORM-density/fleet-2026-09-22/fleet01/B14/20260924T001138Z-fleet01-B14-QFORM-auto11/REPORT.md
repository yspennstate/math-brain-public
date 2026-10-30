SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B14, 2026-09-24T00:11:38Z.
attacking: mass-sensitive whole-product localization for the completed fleet02/B14 hyperbolic-log-plus-square theorem; optimize the logarithmic envelope before any fragment normalization.

# fleet01/B14 — optimized whole-product / square localization

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: new proved supporting theorem and strict-target ambient corollary; the full unrestricted QFORM conjecture remains OPEN.
Execution: `WITHOUT_VERIFIED_BRAIN` (repository transport and source retrieval occurred; native receiver-memory ingestion was not observed).

## 1. Source premise actually used

The designated partner source is the completed fleet02/B14 report

`math-open-problems@010ccf4cdc4f0b07d0a443eba99fd147e6feab65:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B14/20260923T235641Z-fleet02-B14-QFORM-auto11b/REPORT.md`.

Its proved theorem `QFORM-HYPERBOLIC-LOG-PLUS-SQUARE-CLOSURE-v1` gives, for independent cap-one probability variables U,V,Y and arbitrary affine coefficients,

`Q = 2 a U V + lambda Y^2 + alpha U + beta V + gamma Y + eta`,

`||p_Q||_infinity <= |a|^{-1} + 8 / sqrt(|a lambda|)`.

The proof supplies two ingredients that will be retained but sharpened here: (i) a translation-uniform logarithmic envelope for the whole product, and (ii) the square level-set estimate

`|{y: |tau-y^2|<delta}| <= 2 sqrt(2 delta)`.

No pointwise Fourier decay is used.

## 2. Tunable product envelope for subprobability pieces

Let `u,v` be nonnegative densities on R with

`0<=u,v<=1`, `int u = m`, `int v = n`,

where `0<m,n<=1`. Let `Z=UV` denote the pushforward of the product submeasure `u(x)v(y) dx dy` under multiplication. For `z!=0`,

`h(z) = int u(x) v(z/x) dx/|x|`.

### Lemma 2.1 — two-threshold logarithmic envelope

For every `R,S>0`,

`h(z) <= m/R + n/S + 2 log_+(RS/|z|)`.

Proof. If `|z|<RS`, split the integral into

`|x|>=R`, `|z|/S <= |x| < R`, `|x|<|z|/S`.

The first part is at most `m/R`. On the middle part discard both densities and integrate `dx/|x|`, obtaining `2 log(RS/|z|)`. On the last part substitute `y=z/x`; then `|y|>S` and the contribution is at most `n/S`. If `|z|>=RS`, split only at `|x|=R`; on the second part the same substitution gives `|y|>=|z|/R>=S`, so the two tail bounds give `m/R+n/S`. This proves the formula in both regimes.

For fixed `P=RS`, AM-GM optimization gives

`inf_{RS=P} (m/R+n/S) = 2 sqrt(mn/P)`,

attained at `R=sqrt(mP/n)`, `S=sqrt(nP/m)`. Writing `P=q^2`,

`h(z) <= 2 sqrt(mn)/q + 2 log_+(q^2/|z|)` for every `q>0`.

After arbitrary translations of U,V and the scaling `H=2aUV`, `a!=0`, the affine product completion

`2aUV+alpha U+beta V = 2a(U+beta/(2a))(V+alpha/(2a)) - alpha beta/(2a)`

therefore yields the translation-uniform subprobability envelope

`p_H(x) <= sqrt(mn)/(|a|q) + |a|^{-1} log_+(2|a| q^2/|x-x0|)`

for a harmless deterministic output shift `x0` and every `q>0`.

This uses masses and the cap only. Fragment locations, support diameter and moments do not occur.

## 3. A mass-sensitive logarithmic square potential

Let `w` be a nonnegative density with `0<=w<=1` and mass `r in (0,1]`. For `A,c>0`, define

`I = int w(y) log_+(A/|t-c y^2|) dy`.

Completing an arbitrary linear term in y merely translates w, so it suffices to use this form.

For every `delta>0`,

`|{y: |tau-y^2|<delta}| <= 2 sqrt(2 delta)`.

Hence layer cake gives

`I <= int_0^infinity min(r, K exp(-s/2)) ds`,

where

`K = 2 sqrt(2A/c)`.

The integral is explicit:

`I <= 2 K` if `K<=r`,

and

`I <= 2 r (1+log(K/r))` if `K>=r`.

Equivalently, with

`psi_r(K) = K` for `K<=r`, and `psi_r(K)=r(1+log(K/r))` for `K>=r`,

we have

`I <= 2 psi_r(K)`.

This is the partner's square-potential argument with the previously unused trivial mass bound `mu(E)<=r` retained before integration. For probability laws it replaces a pure square-root payment by a logarithmic payment once the small-ball envelope exceeds one.

## 4. Main theorem: mass-sensitive hyperbolic-plus-square localization

Let `u,v,w` be independent subprobability densities bounded by one, with masses `m,n,r`, and let `a lambda !=0`. Consider the pushforward submeasure under

`Q = 2aUV + lambda Y^2 + alpha U + beta V + gamma Y + eta`,

with arbitrary real affine coefficients. Its output density `p_Q^(sub)` satisfies the following bound.

Set

`theta = 2 sqrt(|a| m n / |lambda|) / r`.

Then

`||p_Q^(sub)||_infinity <= (2r/|a|) Phi(theta)`,

where

`Phi(theta) = 2 sqrt(theta)` for `0<theta<=1`,

`Phi(theta) = 2 + log(theta)` for `theta>=1`.

### Proof

Use the product envelope from Section 2 and convolve against the square submeasure. For an arbitrary `q>0`, the constant part contributes

`r sqrt(mn)/(|a| q)`.

For the logarithmic part, take

`A=2|a| q^2`, `c=|lambda|`.

Section 3 gives `K=4q sqrt(|a|/|lambda|)` and therefore

`|a| ||p_Q^(sub)||_infinity <= r sqrt(mn)/q + 2 psi_r(4q sqrt(|a|/|lambda|)).`

Put

`x = 4q sqrt(|a|/|lambda|)/r`.

Then the right side becomes

`4 sqrt(|a|/|lambda|) sqrt(mn)/x + 2r psi_1(x)`.

Since

`theta = 2 sqrt(|a|/|lambda|) sqrt(mn)/r`,

this equals

`2r theta/x + 2r psi_1(x)`.

If `theta<=1`, the minimizing point lies in `x<=1` and is `x=sqrt(theta)`, giving `4r sqrt(theta)`. If `theta>=1`, the minimizing point lies in `x>=1` and is `x=theta`, giving `2r(2+log theta)`. Divide by `|a|` to obtain the stated formula.

The optimization is exact for this envelope. No support/moment/translation parameter is introduced.

## 5. Probability corollary and improved strict-target constant

For probability marginals `m=n=r=1`, write `A0=|a|`, `L0=|lambda|`. Then `theta=2 sqrt(A0/L0)` and the theorem becomes

`||p_Q||_infinity <= 4 sqrt(2) A0^{-3/4} L0^{-1/4}` when `L0>=4A0`,

and

`||p_Q||_infinity <= A0^{-1} [4+2 log 2 + log(A0/L0)]` when `L0<=4A0`.

The two formulas agree at `L0=4A0`, where both equal `4/A0`.

If `A0>=1` and `L0>=1`, then in the first regime the bound is at most 4. In the second regime it is maximized at `L0=1` and then decreases with `A0>=1`, so

`||p_Q||_infinity <= 4 + 2 log 2 = 5.38629436111989...`.

Thus the completed partner bound 9 improves, on exactly the same affine-uniform branch, to

`boxed: ||p_{2aUV+lambda Y^2+affine}||_infinity <= 4+2 log 2`

whenever `|a|,|lambda|>=1`.

This improvement comes solely from two safe localization choices: optimize the product split scale before taking a positive envelope, and retain the total-mass cap in the square layer cake before integrating.

## 6. Ambient zero-tax localization

Suppose a full symmetric matrix in original independent coordinates contains the principal block

`B = [[0,a,0],[a,0,0],[0,0,lambda]]`

on retained variables `(U,V,Y)`, with `|a|,|lambda|>=1`. All couplings to every outside original coordinate and all outside self-curvature are arbitrary.

Condition on the outside original coordinates. On every conditioning fibre they produce only coefficients `alpha,beta,gamma,eta` in the retained variables. The theorem above is uniform in these coefficients, hence every conditional output density is bounded by `4+2 log 2`. Averaging gives

`boxed: ||p_{X^T A X}||_infinity <= 4+2 log 2`.

This is a constant-preserving localization lemma in the literal sense: arbitrary outside translations, remote fragments, unbounded support, outside moments and outside quadratic curvature cost zero. The retained block itself has eigenvalues `{a,-a,lambda}`; by principal-submatrix interlacing the ambient form belongs to the owner's three-large-eigenvalue target.

More generally, if the outside law is decomposed into any finite or countable collection of subprobability pieces of masses `s_j`, the j-th unnormalized output piece is bounded by `s_j(4+2 log 2)` and the sum is exactly bounded by `4+2 log 2`. Thus outside fragmentation is mass-linear and zero-tax.

## 7. What happens if the active square is fragmented first

The same theorem quantifies, rather than hides, the cost of fragmenting a certificate-active coordinate. Take the strict target `a=lambda=1`, keep U,V whole, and split the Y-law into subprobability pieces of masses `r_j` with `sum r_j=1`. Here

`theta_j = 2/r_j >=2`,

so the j-th piece obeys

`||p_j||_infinity <= 2 r_j [2+log(2/r_j)].`

Summing positive piecewise certificates gives

`sum_j ||p_j||_infinity <= 4 + 2 log 2 + 2 H(r)`,

where

`H(r)=sum_j r_j log(1/r_j)`

is Shannon entropy. For N equal fragments this becomes

`4 + 2 log 2 + 2 log N`.

The whole-law certificate is only `4+2 log 2`. Therefore distant active fragments themselves are harmless, but *normalizing/splitting the active square before paying the logarithmic product singularity creates an entropy tax*. The new mass-sensitive estimate improves the much worse fragment-first square-root payment, but it also proves that this positive cellwise route is not constant-preserving under arbitrary active refinement.

This is compatible with fleet02/B14's earlier translation-frame/peak-mass diagnosis: translations are free; concentration and proof order are the debt.

## 8. Scope and remaining implication

This report does not prove full QFORM and does not claim continuity. It does not use pointwise quadratic Fourier decay, post-rotation independence, bounded support, bounded diameter, a fixed number of fragments, moments, log-concavity or arbitrary-joint coarea.

The first unpaid structural implication is now:

`QFORM-OPTIMIZED-LOG-SQUARE-EXTRACTION-OR-AGGREGATE-EXIT-v1` — from bare `s_3(A)>=1`, before active fragmentation, force either a whole original-coordinate hyperbolic pair plus a genuinely disjoint square with quantitative scales, to which the `4+2 log 2` branch applies, or one of the already completed aggregate ridge/volume/hub/pair/receiver exits. The hard overlap remains the case in which the third curvature is generated by the same active bank as the rank-two product.

The law-class localization debt for translations, tails, remote outside fragments and unbounded supports is absent in this branch; the remaining debt is matrix-structural and active-bank overlap.
