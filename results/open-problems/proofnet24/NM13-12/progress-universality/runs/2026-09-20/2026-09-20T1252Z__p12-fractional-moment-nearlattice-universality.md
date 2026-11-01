Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested but is not authenticated by this runtime.**

# NM13-12 — fractional-moment near-lattice universality below B4

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-12` / `proofnet24/NM13-12/progress-universality`  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`, current LIVE20 mapping  
Primary applied parent: **P12 unresolved triangular universality successor**  
T03 coordination: **NM13-03 / NM13-07 read for current boundary only; no lifted-RDT duplication**  
Status: **PARTIAL / NEW AUTHOR-SIDE COMPLETE REAL RANDOM-MATRIX EXTENSION / EXPLICIT INFINITE-THIRD-AND-FOURTH-MOMENT TRIANGULAR FAMILY SOLVED / INDEPENDENT REVIEW PENDING**

## 0. Compact handoff, exact P12 state, and route change

The latest canonical P12 report remains

`proofnet24/P12-smooth-iid/runs/2026-09-17/2026-09-17T18-20-03Z__run-report.md`.

Its frozen theorem is unchanged. For `F in {R,C}`, let `A_m in F^{N_m x m}` have iid centered variance-one entries with density `f_m`. Assume one fixed integer `q>=1` and one uniform finite constant `M` satisfy

`sup_m ||f_m^{*q}||_infty <= M`,

and assume

`N_m/m -> gamma>1`, `k_m=r_m+1`, `k_m log m=o(m)`.

Then

`(k_m/m) log M^F_{m,r_m}(A_m) ->_P -h(gamma)/d_F`,

where `d_R=1`, `d_C=2` and

`h(gamma)=gamma log gamma-(gamma-1)log(gamma-1)`.

There is **no fourth-moment assumption and no positive-moment assumption above variance normalization** in the frozen theorem. Its explicit mathematical successor remains triangular smooth / B4 universality without a uniform microscopic finite-convolution ceiling. P12's remaining canonical obligations are independent-audit/final-package gates, not a missing author-side theorem.

The immediate NM13-12 predecessor,

`2026-09-20T1158Z__p12-unbounded-scale-nearlattice-universality.md`,

proved the real exponent for

`xi_m=(R+sigma_m S_m G)/sqrt(1+sigma_m^2 E S_m^2)`

under a deterministic positive scale floor `S_m>=a_m>0`, a **uniform fourth moment** `sup_m E S_m^4<infinity`, and the effective-floor rate conditions stated below. It had already removed every pointwise upper support bound on `S_m`.

Its recorded next route was to remove the positive floor via Bernoulli--Gaussian masks. I tested that mechanism first. The obstruction is real: with `P(S_m=0)>0`, the fresh-column projected Gaussian covariance can vanish on sparse directions, while conditioning on a good mask introduces an additive bad-mask probability that is not automatically of order `t^{k_m}` at the exponentially small row-submatrix scale. A successful no-floor theorem therefore needs new restricted-covariance/delocalization input, not the predecessor's projection estimate. I preserve that obstruction and change method here.

This run instead removes the **B4 requirement itself**. The low-frequency Fourier argument is rebuilt with a fractional `2+delta` remainder and the coarse anti-concentration input is rebuilt with generalized Paley--Zygmund. This allows entry laws with **infinite third and fourth absolute moments** while retaining the same smoothing and dimension regime.

`POSTED.md` excludes rediscovery/repackaging of the posted bounded-density row-submatrix paper, mesoscopic-spike work, kernel/ReLU work, and zero-margin/Ising perceptron results. The theorem below is not any of those claims: it treats a triangular law outside every fixed finite-convolution density ceiling and, in the concrete application, outside B3 and B4.

## 1. T03 companion state, preserved rather than duplicated

The newest companion reports on current `master` are:

- `NM13-07`, `2026-09-20__t03-monotone-csector-sharp-tangent-alpha123196344462.md`, which moves the review-pending directed exact-sphere Gaussian upper endpoint to `12.3196344462` and develops a separate monotone third-full c-sector compiler.
- `NM13-03`, `2026-09-20__t03-stein-hsi-alpha1228722222161.md`, which supports the stronger complete-third point `12.28722222161` but explicitly leaves it CONDITIONAL because outward four-overlap inclusion is not yet directed-certified.

Thus the original iid-Gaussian T03 parent is not changed in this NM13-12 run. Its current project-supported directed bracket is

`[6.30297437506, 12.3196344462]`.

No stationarity, Krawczyk, c-sector entropy, Stein-HSI, matched-Gaussian, or complete-third calculation is duplicated below.

## 2. New theorem: only a normalized `2+delta` scale moment

Fix one `delta in (0,2]`. For each `m`, let

- `R` be Rademacher;
- `G~N(0,1)`;
- `S_m` be positive and independent of `(R,G)`, with `S_m>=a_m>0` almost surely;
- `0<sigma_m<infinity`.

Write

`mu_{2,m}=E S_m^2`,

`D_m=sqrt(1+sigma_m^2 mu_{2,m})`,

`rho_m=sigma_m a_m/D_m`,

and

`Lambda_{delta,m}`
` = sigma_m^(2+delta) E S_m^(2+delta) / D_m^(2+delta)`.       (2.1)

Define

`xi_m=(R+sigma_m S_m G)/D_m`.                                (2.2)

Let `A_m` have iid real entries distributed as `xi_m`.

### Theorem NM12-P12-FRACTIONAL-MOMENT

Assume

`sup_m Lambda_{delta,m} <= L < infinity`,                    (2.3)

`N_m/m -> gamma>1`, `k_m=r_m+1`,

`(FM1)  m rho_m^2/log(e/rho_m) -> infinity`,                 (2.4)

and

`(FM2)  k_m[log m+log(e/rho_m)] = o(m)`.                    (2.5)

Then

`boxed:`

`(k_m/m) log M^R_{m,r_m}(A_m) ->_P -h(gamma)`.              (2.6)

The assumption is on the **normalized `2+delta` moment of the smoothing component**, not on a raw fourth moment of `S_m`. In particular `E S_m^4` may be infinite, and for `delta<1`, even `E S_m^3` may be infinite.

The proof imports only the deterministic/random-rounding geometry already completed in the immediate predecessor. Every distributional input used by that package is re-proved below under (2.3): center/variance, a fixed scalar concentration gap, the microscopic lower slab on useful spread normals, the one- and two-plane upper slabs with the exact projective-angle singularity, and the fresh-column `k`-dimensional projected small-ball estimate.

## 3. Center, variance, and a uniform `2+delta` entry moment

Let `r=2+delta`. Center and variance are exact:

`E xi_m=0`, `E xi_m^2=1`.                                    (3.1)

Using `|x+y|^r <= 2^(r-1)(|x|^r+|y|^r)` and `D_m>=1`,

`E |xi_m|^r`
` <= 2^(r-1)[D_m^(-r)`
`      + sigma_m^r E S_m^r E|G|^r / D_m^r]`
` <= 2^(r-1)[1+L E|G|^r] =: B_delta,L.                       (3.2)

Thus the entries have a uniform `2+delta` moment even though they need not have a third or fourth moment.

Because `S_m>=a_m`, conditional on `(R,S_m)` the Gaussian variance is at least `rho_m^2`. Hence every fixed-`m` entry law has a positive `C^infinity` density. For derivative order `j`, the conditional Gaussian derivative sup norm is bounded by `C_j rho_m^{-j-1}`, so differentiation under the mixture is legitimate.

## 4. Fractional-moment anti-concentration lemma

The predecessor used B4 only to manufacture a fixed scalar concentration gap for the sparse-kernel/random-rounding geometry. B4 is unnecessary.

### Lemma 4.1

Fix `delta>0`. If `X` is centered, `E X^2=1`, and

`E|X|^(2+delta) <= B`,

then there is `c=c(delta,B)>0` such that

`Q_X(1/2) <= sqrt(1-c) < 1`.                                (4.1)

Here `Q_X(s)=sup_z P{X in [z,z+s]}`.

### Proof

Let `X'` be an independent copy, put

`Z=(X-X')^2`, `p=1+delta/2`.

Then `E Z=2`, while

`E Z^p = E|X-X'|^(2+delta) <= 2^(2+delta) B`.                (4.2)

On the event `A={Z>1/4}`,

`E[Z 1_A] >= E Z-1/4 = 7/4`.                                (4.3)

Holder gives

`7/4 <= (E Z^p)^(1/p) P(A)^((p-1)/p)`,

hence

`P(A) >= c(delta,B)>0`.                                      (4.4)

If an interval `I` has length `1/2`, then on `{X,X' in I}` one has `|X-X'|<=1/2`. Therefore

`P(X in I)^2 <= P(|X-X'|<=1/2) <= 1-c`,

which proves (4.1). QED.

By (3.2), this supplies exactly the fixed concentration gap required by the inherited geometry.

## 5. New analytic core: fractional local-density theorem

Fix `v0>0` and `C0<infinity`. Let deterministic coefficients satisfy

`v=sum_j c_j^2 in [v0,1]`,

`max_j |c_j| <= C0/sqrt(m)`.                                 (5.1)

Let

`Y_m=sum_j c_j xi_{m,j}`

and let `p_m` be its density. Let `phi_v` be the centered Gaussian density of variance `v`.

### Lemma 5.1 — fractional-moment local limit

There are constants `c,C>0`, depending only on `(v0,C0,delta,L)`, such that

`boxed:`

`||p_m-phi_v||_infty`
` <= C m^(-delta/2)
`    + C rho_m^(-1) exp(-c m rho_m^2)`.                      (5.2)

This recovers the predecessor's `O(m^-1)` term when `delta=2`, but remains sufficient for every fixed `delta>0`.

### Proof

Put

`psi_m(z)=E exp(-S_m^2 z^2/2)`.

The characteristic function is

`hat p_m(t)=prod_j cos(c_j t/D_m)`
`                 psi_m(sigma_m c_j t/D_m)`.                 (5.3)

Set `alpha=delta/2 in (0,1]`. For every `x>=0`,

`0 <= exp(-x)-1+x <= x^(1+alpha)`.                           (5.4)

Indeed, for `0<=x<=1`, Taylor gives a bound by `x^2/2<=x^(1+alpha)`; for `x>=1`, the left side is at most `x<=x^(1+alpha)`.

With `x=S_m^2 z^2/2`,

`psi_m(z)`
` =1-mu_{2,m}z^2/2`
`   +O_delta(E S_m^(2+delta)|z|^(2+delta)).`                 (5.5)

For `z=sigma_m c_j t/D_m`, the normalized remainder in (5.5) is bounded by

`C_delta Lambda_{delta,m}|c_j t|^(2+delta)`.                (5.6)

Also

`mu_{2,m} z^2`
` = [sigma_m^2 mu_{2,m}/D_m^2] c_j^2 t^2`
` <= c_j^2 t^2`.                                             (5.7)

Therefore, for one fixed sufficiently small `eta>0`, whenever `|t|<=eta sqrt(m)`, every factor is uniformly close enough to one that `log(1+w)=w+O(w^2)` applies. We obtain

`log psi_m(sigma_m c_j t/D_m)`
` = -[sigma_m^2 mu_{2,m}/(2D_m^2)]c_j^2 t^2`
`   +O(c_j^4 t^4)`
`   +O_delta,L(|c_j t|^(2+delta)).`                          (5.8)

The Rademacher factor obeys

`log cos(c_j t/D_m)`
` =-[c_j^2 t^2/(2D_m^2)] + O(c_j^4 t^4).`                    (5.9)

Summing the quadratic pieces gives **exactly**

`-[1+sigma_m^2 mu_{2,m}]v t^2/(2D_m^2)=-v t^2/2`.           (5.10)

Moreover

`sum_j c_j^4 <= C0^2/m`,                                    (5.11)

and

`sum_j |c_j|^(2+delta)`
` <= (max_j |c_j|)^delta sum_j c_j^2`
` <= C0^delta m^(-delta/2)`.                                (5.12)

Hence

`log hat p_m(t)=-v t^2/2+E_m(t)`,                            (5.13)

with

`|E_m(t)|`
` <= C[t^4/m + m^(-delta/2)|t|^(2+delta)]`.                 (5.14)

Choose `eta` smaller if necessary. On `|t|<=eta sqrt(m)`, the right side is at most `(v0/4)t^2`. Therefore

`|hat p_m(t)-exp(-v t^2/2)|`
` <= C[t^4/m+m^(-delta/2)|t|^(2+delta)] exp(-v0 t^2/4)`.    (5.15)

Its integral is `O(m^(-delta/2))` (the `m^-1` piece is smaller).

For high frequencies, the positive scale floor alone is enough. Since `S_m>=a_m`,

`psi_m(z)<=exp(-a_m^2 z^2/2)`.                              (5.16)

Thus

`|hat p_m(t)|`
` <= exp[-rho_m^2 v t^2/2]
` <= exp[-v0 rho_m^2 t^2/2]`.                               (5.17)

Consequently

`int_{|t|>eta sqrt(m)} |hat p_m(t)|dt`
` <= C rho_m^(-1) exp(-c m rho_m^2)`.                       (5.18)

The Gaussian Fourier tail is `O(exp(-cm))`. Fourier inversion yields (5.2). QED.

### Corollary 5.2 — microscopic lower slab

Under (FM1), the right side of (5.2) tends to zero. The inherited useful-normal geometry supplies a linear-size spread coordinate set with coefficient maximum `O(m^-1/2)` and fixed positive squared mass. Conditioning on its complement exactly as in the predecessor, Lemma 5.1 gives, uniformly for the bounded shifts used by the marked-row construction and all `0<s<=1`,

`P{|<X,u>-z|<=s} >= c s`.                                   (5.19)

There is no Berry--Esseen additive floor. The slower `m^(-delta/2)` density convergence costs nothing at the exponential scale because only convergence to a positive compact-interval density floor is needed.

## 6. Upper slabs and fresh-column projection bounds are unchanged

These estimates never used B4; they use only the positive scale floor.

### Lemma 6.1 — one direction

For deterministic unit `u`, conditional on all Rademacher and scale variables,

`<X,u>`

is Gaussian with variance at least `rho_m^2`. Therefore

`||f_{<X,u>}||_infty <= (sqrt(2pi)rho_m)^(-1)`,              (6.1)

and

`P{|<X,u>-z|<=s} <= C rho_m^(-1)s`.                         (6.2)

### Lemma 6.2 — two directions

For unit `u,v`, let `r=<u,v>` and `Delta=1-r^2`. Conditional on the scales, the Gaussian covariance satisfies

`Sigma >= rho_m^2 [[1,r],[r,1]]`.                            (6.3)

Hence

`det Sigma >= rho_m^4 Delta`,                                (6.4)

so the conditional and unconditional joint density is at most

`C rho_m^(-2) Delta^(-1/2)`.                                (6.5)

Thus a product slab of width `s` has probability at most

`C rho_m^(-2)s^2 Delta^(-1/2)`.                             (6.6)

The projective-angle singularity is exactly the one used by the robust-pair decomposition.

### Lemma 6.3 — `k`-dimensional projected small ball

Let `P` be any deterministic orthogonal projection of rank `k` and let `Z` be one fresh iid column. Conditional on its Rademacher and scale coordinates, the Gaussian covariance on `ran(P)` is

`(sigma_m^2/D_m^2) P diag(S_i^2)P >= rho_m^2 I_k`.           (6.7)

Therefore, for every center `y` and radius `r>0`,

`P{||PZ-y||_2<=r} <= (C r/rho_m)^k`.                        (6.8)

No delocalization of `P` is required.

## 7. Transfer into the row-submatrix exponent

The immediate predecessor already completed the deterministic/random-rounding package. Under the present weaker moment assumption, its distributional inputs are now verified as follows:

1. **center/variance:** (3.1);
2. **fixed scalar anti-concentration:** Lemma 4.1 and (3.2);
3. **useful-normal microscopic lower slab:** Corollary 5.2;
4. **one-normal upper slab:** Lemma 6.1;
5. **two-normal upper slab with the required angle singularity:** Lemma 6.2;
6. **fresh-column lower-extreme estimate:** Lemma 6.3.

For the lower extreme, after freezing the other columns of an `(m+k_m-1) x m` candidate, the orthogonal complement has dimension `k_m` and is independent of the fresh column. At the target scale

`t_m=exp[-(h(gamma)+eps)m/k_m]`,

(6.8) gives a per-candidate contribution bounded by

`(C sqrt(m)t_m/rho_m)^(k_m)`.

The candidate count contributes `exp(h(gamma)m+o(m))`; the non-Gaussian penalty contributes only

`O(k_m[log m+log(e/rho_m)])=o(m)`

by (FM2). This yields the same lower-exponent side as the frozen theorem.

For the constructive upper side, Corollary 5.2 gives the same positive microscopic hit probability on useful spread normals, while (6.2) and (6.6) give the same survivor and robust-pair envelopes with multiplicative penalties `rho_m^-1` and `rho_m^-2`. Across the inherited amplification argument these again cost only

`O(k_m[log m+log(e/rho_m)])=o(m)`.

Therefore the deterministic package closes unchanged and proves (2.6).

A useful quantitative point is that **the smoothing boundary is not worsened by lowering the moment from 4 to `2+delta`**. For every fixed `delta>0`, the predecessor's near-critical choice

`rho_m=(log log m) sqrt(log m/m)`

still has (FM1), while the local-density error `m^(-delta/2)` still vanishes. Thus the moment weakening changes only a polynomial convergence rate inside the local-limit lemma, not the final admissible `rho_m` or `k_m` regime.

## 8. Concrete unresolved probability claim solved: smooth triangular law with infinite third and fourth moments

Take a fixed Pareto scale

`P(S>s)=s^(-5/2),  s>=1`,

so `S>=1` almost surely. Its moments are

`E S^2 = (5/2)/(1/2)=5`,

`E S^(9/4) = (5/2)/(1/4)=10`,

while

`E S^3=E S^4=infinity`.                                     (8.1)

Let

`sigma_m=m^(-1/3)`,

`D_m=sqrt(1+5m^(-2/3))`,

and

`xi_m=(R+m^(-1/3) S G)/D_m`.                                (8.2)

Apply Theorem 2 with `delta=1/4`. Then

`Lambda_{1/4,m}`
` =10 m^(-3/4)/D_m^(9/4) <= 10`,                            (8.3)

and

`rho_m=m^(-1/3)/D_m`.                                       (8.4)

Hence

`m rho_m^2/log(e/rho_m) ~ m^(1/3)/[(1/3)log m] -> infinity`,

while (FM2) is exactly implied by `k_m log m=o(m)`.

The entry law is centered, variance one and `C^infinity`, but

`E|xi_m|^3=infinity`, `E xi_m^4=infinity`                    (8.5)

for every `m` because the Gaussian scale mixture inherits the Pareto tail. It is therefore outside the immediate B4 predecessor by a strict moment-class separation.

It is also outside the frozen P12 finite-convolution hypothesis. For any fixed `q`, consider the component on which all `q` Rademachers equal `+1` and all `q` scales satisfy `S_i<=2`. Since

`P(S<=2)=1-2^(-5/2)>0`,

the component has fixed positive weight

`w_q=[(1/2)(1-2^(-5/2))]^q`.                                (8.6)

At the common center `q/D_m`, conditional on those scales the sum is Gaussian with variance at most

`4q sigma_m^2/D_m^2`.

Therefore

`||f_m^{*q}||_infty`
` >= w_q D_m/[2 sigma_m sqrt(2pi q)]`
` >= c_q m^(1/3) -> infinity`.                              (8.7)

Thus no fixed pair `(q,M)` from frozen P12 applies.

Nevertheless the new theorem gives

`boxed:`

`(k_m/m) log M^R_{m,r_m}(A_m) ->_P -h(gamma)`               (8.8)

throughout the full moderate-surplus regime `k_m log m=o(m)`.

### Applied-parent before / after

For the explicit law (8.2):

- **before this run:** `UNKNOWN / uncovered` by frozen P12 and by all earlier NM13-12 near-lattice theorems, because every fixed finite-convolution density ceiling diverges and the entry law has no finite third or fourth absolute moment;
- **after this run:** the row-submatrix exponent (8.8) is proved author-side, pending later independent review.

The frozen canonical P12 theorem itself is not rewritten or relabeled; its statement remains unchanged.

## 9. Exact theory gain, separate from the application

The demonstrated theorem-level movement is

`uniform B4 of the random scale / entry`

`        -->`

`one fixed normalized (2+delta)-moment for arbitrary delta>0`.

More precisely, the predecessor required `sup E S_m^4<infinity`; this run requires only (2.3), which is enough to bound a normalized entry `2+delta` moment and may hold when `E S_m^3=E S_m^4=infinity`.

The local-density rate changes from

`O(m^-1)+O(rho^-1 exp(-cm rho^2))`

to

`O(m^(-delta/2))+O(rho^-1 exp(-cm rho^2))`,

but the final exponent theorem keeps the same `rho_m` and `k_m` regimes because any fixed `delta>0` makes the first term vanish.

This is not a new version of the posted bounded-density theorem. The public Yang--Wen--Shmalo 2026 theorem assumes one fixed centered real **subgaussian bounded-density** entry law; (8.2) is triangular, has every fixed convolution-density ceiling diverging, and has polynomial tails with infinite third/fourth moments.

## 10. Sanity checker and executed output

Executed checker:

`proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/p12_fractional_moment_nearlattice_checker.py`

creation commit `4e21d432872577cf5cadbb584bfafb48f42fbd39`.

Archived actual stdout:

`proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/p12_fractional_moment_nearlattice_checker.out`

creation commit `be91987f67851577bca1f9460c728a246a5f4bf3`.

The output verifies the exact Pareto moments, infinite third/fourth moments, the fractional exponential remainder over a wide logarithmic grid, the effective-floor rate growth, normalized `9/4`-moment decay, fixed-`q` convolution blow-up constants, the generalized Paley--Zygmund concentration gap, and the retained near-critical smoothing scale. It ends

`ALL_FRACTIONAL_MOMENT_CHECKS_PASS`.

The checker is a sanity artifact only; the theorem proof is the analytic argument in Sections 3--7.

## 11. Residual obstruction and next attack

The generic triangular smooth/B4 successor is still **not solved**. The new theorem remains structured: an independent Gaussian component with a deterministic positive scale floor is used to suppress high-frequency resonances and to give the exact fresh-column projected covariance floor.

The honest remaining obstruction is still the no-floor case, for example Bernoulli--Gaussian smoothing with `P(S_m=0)>0`. The next nonduplicating route should prove a random-mask restricted-covariance statement on the actual fresh `k_m`-dimensional orthogonal complements, exploiting the project's sparse-kernel/useful-normal geometry strongly enough that the mask failure probability is absorbed at the `t^{k_m}` scale rather than appearing as an additive error. If that cannot be obtained, the alternate route is to replace the deterministic floor by a quantitative lower-tail condition on `S_m` and derive a multiplicative projected-small-ball estimate directly from the random covariance determinant.

## ledger_delta

```yaml
worker: NM13-12
run_date: 2026-09-20
parent: P12 unresolved triangular universality successor
status: PARTIAL
new_theorem: NM12-P12-FRACTIONAL-MOMENT
frozen_p12_changed: false
source_exact_frozen_hypotheses:
  iid: true
  centered: true
  variance_one: true
  density: true
  fixed_q_uniform_convolution_Linf: true
  aspect: N_m/m -> gamma > 1
  surplus: k_m=r_m+1, k_m log m=o(m)
new_assumption_gain:
  before: positive scale floor plus uniform fourth moment
  after: positive scale floor plus one normalized (2+delta)-moment, any fixed delta>0
new_local_density_rate: O(m^(-delta/2) + rho_m^-1 exp(-c m rho_m^2))
final_rho_regime_changed: false
final_dimension_regime_changed: false
concrete_application:
  scale: Pareto(shape=5/2, xmin=1)
  sigma_m: m^(-1/3)
  finite_entry_moment: 9/4
  infinite_entry_abs_third: true
  infinite_entry_fourth: true
  fixed_q_convolution_ceiling: diverges_like_m^(1/3)
  before: UNKNOWN/uncovered
  after: exponent -h(gamma) proved author-side
T03:
  lower: 6.30297437506
  directed_upper_before: 12.3196344462
  directed_upper_after: 12.3196344462
  nm13_03_conditional: 12.28722222161
  nm13_12_movement: none
posted_repackaging: false
failed_route_preserved: Bernoulli-zero-scale mask needs new restricted-covariance input
checker_commit: 4e21d432872577cf5cadbb584bfafb48f42fbd39
output_commit: be91987f67851577bca1f9460c728a246a5f4bf3
independent_review_pending: true
```
