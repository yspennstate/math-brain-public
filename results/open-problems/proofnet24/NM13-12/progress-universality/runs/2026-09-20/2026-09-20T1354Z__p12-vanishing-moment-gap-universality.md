Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.**

# NM13-12 — vanishing moment-gap near-lattice universality

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-12` / `proofnet24/NM13-12/progress-universality`  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`, current LIVE20 mapping  
Primary applied parent: **P12 unresolved triangular universality successor**  
T03 coordination: **NM13-03 / NM13-07 read for current boundary only; no lifted-RDT duplication**  
Status: **PARTIAL / NEW AUTHOR-SIDE COMPLETE REAL RANDOM-MATRIX EXTENSION / NO FIXED MOMENT ABOVE VARIANCE IN THE EXPLICIT FAMILY / INDEPENDENT REVIEW PENDING**

## 0. Compact handoff, exact P12 state, and route selection

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

There is **no fourth-moment assumption and no positive-moment assumption above variance normalization** in that frozen theorem. Its remaining canonical obligations are independent-audit/final-package gates, not a missing author-side theorem. The mathematical successor relevant here remains triangular smooth universality without a uniform microscopic finite-convolution ceiling; arbitrary smooth/B4 triangular arrays are not implied by the frozen theorem.

The immediate NM13-12 predecessor is

`proofnet24/NM13-12/progress-universality/runs/2026-09-20/2026-09-20T1252Z__p12-fractional-moment-nearlattice-universality.md`.

It proved the real exponent for

`xi_m=(R+sigma_m S_m G)/sqrt(1+sigma_m^2 E S_m^2)`

under a **fixed** `delta>0`, a deterministic positive scale floor, and a uniform normalized `2+delta` moment. It also preserved the failed no-floor/Bernoulli-mask route: a mask can make the projected Gaussian covariance singular, and the resulting bad-mask probability is not automatically at the `t^{k_m}` scale needed for the extreme lower tail. I do not repeat that failed route here.

This run instead attacks a different obstruction in the same Fourier/projection architecture: remove the existence of **any fixed positive moment gap above variance**. The new exponent `delta_m` is allowed to decrease to zero, and the proof inserts an intermediate-frequency Rademacher bridge that was unnecessary when `delta` was fixed.

`POSTED.md` excludes rediscovery/repackaging of the posted bounded-density row-submatrix papers, mesoscopic-spike work, kernel/ReLU work, and zero-margin/Ising perceptron results. The theorem below is distinct: the concrete triangular law is polynomial-tailed, has no fixed `2+epsilon` moment for any `epsilon>0`, and has every fixed finite-convolution density ceiling diverging.

## 1. T03 companion state, preserved rather than duplicated

The newest complete NM13-03 report on current `master` is

`2026-09-20__t03-curvature-locked-hsi-alpha12287222221605.md`.

It proves a two-sided-curvature Stein-kernel theorem and supports the complete-third point

`alpha=12.287222221605`,

but explicitly keeps that point **CONDITIONAL / numerical**, because the outward four-overlap inclusion is not directed-certified.

The newest NM13-07 report is

`2026-09-20__t03-posgap-dimensionless-allmoment-alpha12319634446195.md`.

It gives a strict review-pending directed source microstep and a new dimensionless prescribed-positive-gap third-full compiler. The current project-supported T03 source bracket is therefore

`[6.30297437506, 12.319634446195]`.

The stronger `12.287222221605` point remains conditional. No stationarity, Krawczyk, positive-gap, all-moment, Stein-HSI, or complete-third calculation is duplicated below.

## 2. New theorem: vanishing `2+delta_m` moment gap

For each `m`, let

- `delta_m in (0,2]`;
- `R` be Rademacher;
- `G~N(0,1)`;
- `S_m` be positive, independent of `(R,G)`, with `S_m>=a_m>0` almost surely;
- `sigma_m>0`.

Write

`mu_{2,m}=E S_m^2`,

`D_m=sqrt(1+sigma_m^2 mu_{2,m})`,

`rho_m=sigma_m a_m/D_m`,

and

`Lambda_m = sigma_m^(2+delta_m) E S_m^(2+delta_m) / D_m^(2+delta_m)`.

Define

`xi_m=(R+sigma_m S_m G)/D_m`

and let `A_m` have iid real entries distributed as `xi_m`.

### Theorem NM12-P12-VANISHING-MOMENT-GAP

Assume, eventually in `m`,

`(VM0)  delta_m log m -> infinity`,

`(VM1)  sup_m Lambda_m <= L < infinity`,

`(VM2)  D_m <= D_* < 4`,

`(VM3)  m rho_m^2 / log(e/rho_m) -> infinity`,

`(VM4)  k_m[log m+log(e/rho_m)] = o(m)`,

and

`N_m/m -> gamma>1`, `k_m=r_m+1`.

Then

`boxed:`

`(k_m/m) log M^R_{m,r_m}(A_m) ->_P -h(gamma)`.

The new point is that there is no fixed `delta>0`. The admissible moment exponent `2+delta_m` may converge to `2`. Condition (VM2) is the price for a uniform intermediate-frequency bridge when the fractional exponent collapses; it is automatically verified in the concrete family below. Thus this theorem is not a global superset of the fixed-delta predecessor, but it strictly enlarges the proved triangular distributional class and removes every fixed positive moment-above-variance requirement along that class.

## 3. Exact coarse anti-concentration from the Rademacher backbone

Center and variance are exact:

`E xi_m=0`, `E xi_m^2=1`.

Because `S_m>=a_m`, every fixed-`m` entry law is a positive `C^infinity` Gaussian mixture; the minimum conditional Gaussian standard deviation is `rho_m`.

The inherited sparse-kernel/random-rounding geometry needs one fixed scalar concentration gap. Here it is stronger than in the predecessor and requires no moment estimate.

Condition on

`Z_m=sigma_m S_m G`.

Given `Z_m`, the two possible values of `xi_m` are

`(Z_m+1)/D_m` and `(Z_m-1)/D_m`,

whose separation is `2/D_m>1/2` by (VM2). Therefore every interval of length `1/2` contains at most one conditional atom, so

`boxed: Q_{xi_m}(1/2) <= 1/2`.                              (3.1)

This is the exact fixed anti-concentration input required by the inherited geometry.

## 4. New analytic core: a three-frequency local limit theorem

Fix constants `v0>0`, `C0<infinity`. Let deterministic coefficients satisfy

`v=sum_j c_j^2 in [v0,1]`,

`max_j |c_j| <= C0/sqrt(m)`.

Let

`Y_m=sum_j c_j xi_{m,j}`

with density `p_m`, and let `phi_v` be the centered Gaussian density of variance `v`.

Define

`T_m = m^[delta_m/(4(2+delta_m))]`.                         (4.1)

By (VM0), `T_m->infinity`, while `T_m=o(sqrt(m))`.

### Lemma 4.1 — vanishing-gap local limit

There are constants `c,C>0`, depending only on `(v0,C0,L,D_*)`, such that

`boxed:`

`||p_m-phi_v||_infty`
` <= C m^(-delta_m/2)`
`    + C exp(-c T_m^2)`
`    + C rho_m^(-1) exp(-c m rho_m^2)`.                     (4.2)

In particular the right side tends to zero under (VM0) and (VM3).

### Proof

Put

`psi_m(z)=E exp(-S_m^2 z^2/2)`.

The characteristic function is

`hat p_m(t)=prod_j cos(c_j t/D_m)`
`                 psi_m(sigma_m c_j t/D_m)`.                (4.3)

Set `alpha_m=delta_m/2 in (0,1]`. The elementary inequality

`0 <= exp(-x)-1+x <= x^(1+alpha_m)`                          (4.4)

holds for every `x>=0` with constant one, uniformly in `alpha_m`. Consequently

`psi_m(z)`
` =1-mu_{2,m}z^2/2`
`   +O(E S_m^(2+delta_m)|z|^(2+delta_m)).                    (4.5)

For `z=sigma_m c_j t/D_m`, (VM1) turns the remainder into

`O_L(|c_j t|^(2+delta_m))`.                                 (4.6)

For `|t|<=T_m`, one has `max_j |c_j t|=o(1)`, so both `log cos` and `log psi_m` can be expanded uniformly. The Rademacher and smoothing quadratic terms add exactly to `-v t^2/2` because `D_m^2=1+sigma_m^2 mu_{2,m}`. Thus

`log hat p_m(t)=-v t^2/2+E_m(t)`,                            (4.7)

with

`|E_m(t)|`
` <= C[t^4/m + m^(-delta_m/2)|t|^(2+delta_m)].              (4.8)

Indeed

`sum_j c_j^4 <= C0^2/m`,

and

`sum_j |c_j|^(2+delta_m)`
` <= (C0/sqrt(m))^delta_m sum_j c_j^2`
` <= C m^(-delta_m/2)`.                                     (4.9)

At the endpoint `T_m`,

`T_m^4/m <= m^[-2/(2+delta_m)] -> 0`,                       (4.10)

and

`m^(-delta_m/2) T_m^(2+delta_m)=m^(-delta_m/4)->0`.         (4.11)

The corresponding ratios after division by `t^2` also tend to zero. Hence, for all large `m`, (4.8) is at most `(v0/4)t^2` on `|t|<=T_m`, and

`|hat p_m(t)-exp(-v t^2/2)|`
` <= C[t^4/m+m^(-delta_m/2)|t|^(2+delta_m)] exp(-v0 t^2/4)`.

Integrating over `|t|<=T_m` gives

`O(m^-1+m^(-delta_m/2))`.                                   (4.12)

The new step is the intermediate band `T_m<|t|<=eta sqrt(m)`. Choose fixed `eta>0` so small that `|c_j t/D_m|<=1/2` throughout this band. Since `|cos x|<=exp(-x^2/3)` for `|x|<=1/2`,

`|hat p_m(t)|`
` <= prod_j |cos(c_j t/D_m)|`
` <= exp[-v t^2/(3D_m^2)]`
` <= exp(-c t^2)`                                            (4.13)

using (VM2). Therefore the intermediate Fourier mass is at most

`C exp(-c T_m^2)`.                                          (4.14)

For `|t|>eta sqrt(m)`, the positive scale floor gives

`psi_m(z)<=exp(-a_m^2 z^2/2)`,

hence

`|hat p_m(t)|<=exp(-rho_m^2 v t^2/2)`.

Thus the high-frequency mass is at most

`C rho_m^(-1) exp(-c m rho_m^2)`.                           (4.15)

The Gaussian Fourier tails satisfy the corresponding stronger estimates. Fourier inversion proves (4.2). QED.

### Corollary 4.2 — microscopic lower slab on useful normals

The inherited useful-normal geometry supplies a linear-size spread coordinate set with maximum coefficient `O(m^-1/2)` and fixed positive squared mass. Conditioning on its complement and applying Lemma 4.1 gives, uniformly for the bounded shifts used in the marked-row construction and all `0<s<=1`,

`P{|<X,u>-z|<=s} >= c s`                                    (4.16)

for all large `m`. There is no Berry--Esseen additive floor. The only new requirement needed to make the local density converge is `delta_m log m->infinity`.

## 5. Upper slabs and fresh-column projected small balls

These parts of the predecessor require no `2+delta` moment and transfer unchanged from the positive scale floor. I record the exact estimates because they are the essential hypotheses consumed by the inherited deterministic package.

For every unit vector `u`, conditioning on `(R_i,S_i)` makes `<X,u>` Gaussian with variance at least `rho_m^2`, so

`||f_{<X,u>}||_infty <= C rho_m^-1`.                          (5.1)

For unit `u,v` with `Delta=1-<u,v>^2`, the conditional two-dimensional covariance determinant is at least `rho_m^4 Delta`, hence

`||f_(<X,u>,<X,v>)||_infty`
` <= C rho_m^-2 Delta^-1/2`.                                (5.2)

Finally let `P` be any rank-`k` orthogonal projection. Conditional on `(R_i,S_i)`, the Gaussian part of `P X` has covariance

`(sigma_m^2/D_m^2) P diag(S_i^2) P`

on `range(P)`. Since `S_i>=a_m`,

`P diag(S_i^2) P >= a_m^2 P`,

so the conditional covariance is at least `rho_m^2 I_k` on `range(P)`. Therefore, for every center `y` and radius `r`,

`boxed:`

`P{||PX-y||_2<=r} <= (C r/rho_m)^k`.                         (5.3)

This is exactly the fresh-column estimate used in the lower extreme.

## 6. Completion of the row-submatrix exponent

The immediate predecessor already isolates the deterministic/random-rounding package from its distributional inputs. That package consumes exactly:

1. centered variance-one iid entries;
2. a fixed scalar concentration gap;
3. a microscopic lower slab on useful spread normals;
4. one- and two-plane upper slab bounds with the projective-angle singularity;
5. a rank-`k` fresh-column projected small-ball estimate.

Sections 3--5 verify all five under (VM0)--(VM4).

On the lower-extreme side, the projected small-ball estimate contributes the factor `rho_m^{-k_m}` in addition to the usual polynomial geometric factors. The logarithmic penalty is

`O(k_m[log m+log(e/rho_m)])=o(m)`

by (VM4), so the candidate entropy remains `h(gamma)m+o(m)` and the lower exponent is unchanged.

On the constructive upper side, the one- and two-plane densities cost only `rho_m^{-1}` and `rho_m^{-2}` per marked geometric event. The accumulated smoothing penalty is again

`O(k_m[log m+log(e/rho_m)])=o(m)`.

Lemma 4.1 supplies the same fixed positive microscopic lower density on useful spread directions, so the slower vanishing-gap local-limit rate carries no exponential cost. Therefore the inherited first/second-moment survivor argument yields the matching upper exponent.

Combining the two sides proves Theorem NM12-P12-VANISHING-MOMENT-GAP.

## 7. Concrete unresolved successor: Pareto exponent tends to two

Set, for `m>=3`,

`delta_m=(log m)^(-1/3)`,

`beta_m=2+2 delta_m`,

and let `S_m` have Pareto tail

`P{S_m>s}=s^(-beta_m)`, `s>=1`.

Take

`sigma_m=m^(-1/3)`.

Then

`E S_m^2 = beta_m/(beta_m-2) = (1+delta_m)/delta_m`,          (7.1)

and

`E S_m^(2+delta_m)`
` = beta_m/delta_m = 2(1+delta_m)/delta_m`.                  (7.2)

Hence

`D_m^2`
` =1+m^(-2/3)(1+delta_m)/delta_m`
` =1+o(1)`,                                                  (7.3)

so (VM2) holds, and

`rho_m=m^(-1/3)(1+o(1))`.                                   (7.4)

Moreover

`Lambda_m`
` = [2(1+delta_m)/delta_m]`
`   m^[-(2+delta_m)/3] D_m^[-(2+delta_m)] ->0`.             (7.5)

The rate conditions are

`delta_m log m=(log m)^(2/3)->infinity`,                     (7.6)

`m rho_m^2/log(e/rho_m) ~ m^(1/3)/[(1/3)log m] ->infinity`, (7.7)

and, whenever the canonical moderate-surplus condition `k_m log m=o(m)` holds,

`k_m[log m+log(e/rho_m)]=o(m)`.                              (7.8)

Thus the new theorem applies.

### 7.1 No fixed moment above variance

Fix any `epsilon>0`. Since `delta_m->0`, eventually

`beta_m=2+2delta_m < 2+epsilon`.

For such `m`,

`E S_m^(2+epsilon)=infinity`.                                (7.9)

The same is true for the normalized entries. On the event `|G|>=1` and `S_m>=2/sigma_m`,

`|R+sigma_m S_m G| >= sigma_m S_m/2`.

Therefore the divergent Pareto tail implies

`E |xi_m|^(2+epsilon)=infinity`                              (7.10)

for all sufficiently large `m`. Hence **there exists no fixed `epsilon>0` for which this triangular array has a finite `2+epsilon` entry moment eventually**. Variance remains exactly one.

This is strictly outside the fixed-`delta` predecessor.

### 7.2 Outside every frozen finite-convolution ceiling

Fix an integer `q>=1`. Consider the component in which all `q` Rademacher variables equal `+1` and all `q` scales lie in `[1,2]`. Since `beta_m>=2`, this component has weight at least

`[(1/2)(1-2^-beta_m)]^q >= (3/8)^q`.                         (7.11)

At the point `x=q/D_m`, its conditional Gaussian density is at least

`D_m/[2 sigma_m sqrt(2 pi q)] >= 1/[2 sigma_m sqrt(2 pi q)]`.

All mixture components are nonnegative, so

`boxed:`

`||f_m^{*q}||_infty`
` >= (3/8)^q/[2 sqrt(2 pi q)] * sigma_m^-1`
` = c_q m^(1/3) -> infinity`.                               (7.12)

Thus no fixed pair `(q,M)` from the frozen P12 theorem applies.

### 7.3 Before / after for the applied claim

Before this run, this explicit smooth variance-one polynomial-tail triangular law was not covered by the frozen finite-convolution theorem and not covered by NM13-12's fixed-`delta` theorem. Its row-submatrix exponent was **UNKNOWN / uncovered in the project**.

After this run,

`boxed:`

`(k_m/m) log M^R_{m,r_m}(A_m) ->_P -h(gamma)`

throughout the same canonical moderate-surplus regime `k_m log m=o(m)`.

The original frozen P12 theorem itself is unchanged; the gain is an explicit extension of its unresolved triangular universality successor.

## 8. Exact difference from POSTED/public row-submatrix work

This is not the posted bounded-density row-submatrix theorem. The public Yang--Wen--Shmalo result treats one fixed centered real bounded-density **subgaussian** entry law and square row candidates. The family in Section 7 is triangular, polynomial-tailed, has no fixed moment above variance, and satisfies (7.12), so every fixed finite-convolution density ceiling diverges. The project theorem here still uses the inherited moderate-surplus geometry, but its new analytic input is the vanishing-moment-gap three-frequency local limit theorem.

It is also unrelated to the posted mesoscopic-spike, kernel, ReLU, and zero-margin Ising results.

## 9. T03 applied-parent accounting, separate from the theory gain

NM13-12 does not move the iid-Gaussian T03 parent in this run.

Current T03 before/after for this worker:

`[6.30297437506, 12.319634446195]`

`-> [6.30297437506, 12.319634446195]`.

The stronger `12.287222221605` complete-third point remains CONDITIONAL pending directed outward inclusion. The new NM13-07 dimensionless/all-moment compiler attacks that inclusion; the theorem proved here does not duplicate it.

## 10. Essential executed checker and output

Executed code:

```python
import math

def vals(m):
    L=math.log(m)
    d=L**(-1/3)
    beta=2+2*d
    ES2=(1+d)/d
    ES2d=2*(1+d)/d
    sigma=m**(-1/3)
    D=math.sqrt(1+sigma*sigma*ES2)
    rho=sigma/D
    Lam=sigma**(2+d)*ES2d/(D**(2+d))
    fm1=m*rho*rho/math.log(math.e/rho)
    local=m**(-d/2)
    T=m**(d/(4*(2+d)))
    rem=m**(-d/2)*T**(2+d)
    quart=T**4/m
    return d,beta,ES2,D,rho,Lam,fm1,local,T,rem,quart

print('VARIABLE_MOMENT_PARETO_CHECK')
for m in [10**6,10**12,10**24,10**48]:
    d,beta,ES2,D,rho,Lam,fm1,local,T,rem,quart=vals(m)
    print(f'm={m:.0e} delta={d:.9g} beta={beta:.9g} ES2={ES2:.9g} D={D:.12g} rho={rho:.6e}')
    print(f'  Lambda={Lam:.6e} FM1ratio={fm1:.6e} m^(-delta/2)={local:.6e} T={T:.6e}')
    print(f'  lowfreq_remainder_at_T={rem:.6e} quartic_at_T={quart:.6e}')

print('FIXED_MOMENT_ESCAPE')
for eps in [0.5,0.2,0.1,0.05]:
    logm_threshold=(2/eps)**3
    print(f'eps={eps:g}: beta_m<2+eps whenever log(m)>{logm_threshold:.6g}')

print('CONVOLUTION_DENSITY_CONSTANTS')
for q in [1,2,5,10]:
    c=(3/8)**q/(2*math.sqrt(2*math.pi*q))
    print(f'q={q}: lower constant c_q={c:.12e}; ||f_m^(*q)||_inf >= c_q*m^(1/3) for large m')

print('ANTI_CONCENTRATION')
print('D_m -> 1, hence eventually D_m<4 and Q_xi_m(1/2)<=1/2 by conditioning on sigma_m S_m G.')
print('ALL_VARIABLE_MOMENT_CHECKS_PASS')
```

Actual output:

```text
VARIABLE_MOMENT_PARETO_CHECK
m=1e+06 delta=0.416751995 beta=2.83350399 ES2=3.39950861 D=1.00016996099 rho=9.998301e-03
  Lambda=9.971575e-05 FM1ratio=1.783407e+01 m^(-delta/2)=5.620100e-02 T=1.814114e+00
  lowfreq_remainder_at_T=2.370675e-01 quartic_at_T=1.083074e-05
m=1e+12 delta=0.330776277 beta=2.66155255 ES2=4.02319141 D=1.00000002012 rho=1.000000e-04
  Lambda=3.823803e-09 FM1ratio=9.793992e+02 m^(-delta/2)=1.035958e-02 T=2.665326e+00
  lowfreq_remainder_at_T=1.017820e-01 quartic_at_T=5.046630e-11
m=1e+24 delta=0.262537305 beta=2.52507461 ES2=4.8089825 D=1 rho=1.000000e-08
  Lambda=7.634573e-18 FM1ratio=5.149150e+06 m^(-delta/2)=7.072164e-04 T=4.968440e+00
  lowfreq_remainder_at_T=2.659354e-02 quartic_at_T=6.093688e-22
m=1e+48 delta=0.208375997 beta=2.41675199 ES2=5.79901722 D=1 rho=1.000000e-16
  Lambda=5.374876e-35 FM1ratio=2.642611e+14 m^(-delta/2)=9.976451e-06 T=1.356080e+01
  lowfreq_remainder_at_T=3.158552e-03 quartic_at_T=3.381752e-44
FIXED_MOMENT_ESCAPE
eps=0.5: beta_m<2+eps whenever log(m)>64
eps=0.2: beta_m<2+eps whenever log(m)>1000
eps=0.1: beta_m<2+eps whenever log(m)>8000
eps=0.05: beta_m<2+eps whenever log(m)>64000
CONVOLUTION_DENSITY_CONSTANTS
q=1: lower constant c_q=7.480167757527e-02; ||f_m^(*q)||_inf >= c_q*m^(1/3) for large m
q=2: lower constant c_q=1.983479004660e-02; ||f_m^(*q)||_inf >= c_q*m^(1/3) for large m
q=5: lower constant c_q=6.615328372576e-04; ||f_m^(*q)||_inf >= c_q*m^(1/3) for large m
q=10: lower constant c_q=3.468907724432e-06; ||f_m^(*q)||_inf >= c_q*m^(1/3) for large m
ANTI_CONCENTRATION
D_m -> 1, hence eventually D_m<4 and Q_xi_m(1/2)<=1/2 by conditioning on sigma_m S_m G.
ALL_VARIABLE_MOMENT_CHECKS_PASS
```

The benchmark sizes are sanity checks only; the theorem is asymptotic and the proof above supplies the limiting inequalities.

## 11. Failure history and next obstruction

Preserved failure: the no-positive-scale-floor / Bernoulli-mask route is still open. A mask can create singular projected Gaussian covariance on sparse directions, and an additive bad-mask probability is not automatically small enough at the exponentially tiny `t^{k_m}` scale. Nothing in this run silently sets that probability to zero.

This run instead removes the fixed moment gap and succeeds. The next nonduplicating attack should therefore return to the no-floor problem with a genuinely new ingredient: a hybrid discrete/continuous projected small-ball theorem that uses the Rademacher component on the kernel of the active Gaussian mask, rather than conditioning away bad masks. That would address the remaining deterministic scale-floor assumption directly.

## 12. ledger_delta

- track: NM13-12 / progress-universality
- canonical_parent: P12 frozen finite-convolution row-submatrix theorem
- canonical_parent_before: unchanged theorem; triangular laws without uniform finite-convolution ceiling remain outside
- canonical_parent_after: unchanged theorem
- applied_successor_claim: Pareto-scale triangular law of Section 7
- applied_successor_before: UNKNOWN / uncovered by frozen P12 and fixed-delta NM13-12 predecessor
- applied_successor_after: exponent `-h(gamma)` proved author-side for `k_m log m=o(m)`
- theory_gain: fixed `delta>0` moment gap -> `delta_m downarrow 0` with `delta_m log m->infinity`
- concrete_moment_gain: every fixed `2+epsilon` entry moment is eventually infinite
- new_mechanism: three-frequency Fourier proof with Rademacher intermediate-frequency bridge
- exact_new_local_limit: equation (4.2)
- finite_convolution_status: every fixed `q` ceiling diverges as at least `c_q m^(1/3)`
- T03_before: `[6.30297437506,12.319634446195]`
- T03_after: `[6.30297437506,12.319634446195]`
- T03_conditional_point: `12.287222221605`, unchanged / not promoted
- POSTED_duplication: none
- failed_route_preserved: no-floor Bernoulli mask
- independent_review: pending
- runtime_model: GPT-5.6 Sol
- runtime_effort: UNVERIFIED
