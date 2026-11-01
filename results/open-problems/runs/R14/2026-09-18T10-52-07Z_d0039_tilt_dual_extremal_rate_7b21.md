Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT on D0039: `B_spectrum: 1 -> 1`; authoritative stagnation count remains UNKNOWN. Methods actually used: #5 ADD A PARAMETER AND DIFFERENTIATE, #11 DUALIZE, #24 FIND THE EXTREMAL OBJECT.**

# R14 HARD OUTSIDE — D0039 beta-Hermite multifractal spectrum, tilt/dual/extremal-rate run

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and ownership

I did **not** reopen the negative-margin spherical perceptron, H0017, or D0036. Their R14 hard-task handoffs remain controlling. The active exclusive R14 claim is still `operations/claims/D0039.md`.

D0039 is Bálint Virág, *Operator limits of random matrices*, ICM 2014 / arXiv:1804.06953, Section 4, Question 1. For the semi-infinite beta-Hermite Jacobi matrix `J_beta`, let `mu_beta` be the spectral measure at the first coordinate. Virág records the almost-sure Hausdorff dimension `(1-2/beta)^+` and asks whether `mu_beta` and a Gaussian multiplicative cascade with the same Hausdorff dimension have the same fractal / multifractal spectrum.

I reread the campaign `INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the active D0039 claim, the newest R14 report, the D-intake row, and the closest neighboring D0039 screen (`runs/R15/20260917_2008Z_successor_admission_d0039_j39.md`). The neighboring report independently identifies the same missing object: a speed-`log n` transfer-amplitude / Jitomirskaya--Last large-deviation principle in the real-line beta-Hermite model.

A bounded fresh literature search on 2026-09-18 checked Virág's source statement, Breuer's random-Jacobi proof of the exact dimension, Alberts--Normand's circular-beta norm LDP, Lambert--Paquette's 2025 Gaussian-beta characteristic-polynomial asymptotics, and recent 2026 random-Jacobi spectral-measure papers. I found no later primary source closing Virág's **beta-Hermite** question. Chhaibi--Najnudel concerns the circular beta / OPUC measure, not this Jacobi measure. Nakano--Trinh--Trinh (arXiv:2601.13674) concerns the high-temperature regime `beta*N -> 2c`, not fixed beta here.

Primary / near-primary navigation used this run:

- Virág, ICM 2014, exact Question 1: https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM2014.4/ICM2014.4.pdf
- J. Breuer, *Spectral and Dynamical Properties of Certain Random Jacobi Matrices with Growing Parameters*, arXiv:0708.0670.
- Alberts--Normand, *Dimension Results for the Spectral Measure of the Circular Beta Ensembles*, arXiv:1912.07788 / Ann. Appl. Probab. 32 (2022).
- Lambert--Paquette, *Bulk asymptotics of the Gaussian beta-ensemble characteristic polynomial*, arXiv:2508.01458 (2025).

This is bounded current-status evidence, not a worldwide novelty certificate.

## 2. Frozen metric

The active claim fixes

`B_spectrum in {0,1,2,3}`.

The previous run rigorously earned `B_spectrum=1` through the exact Christoffel--Darboux / nested-characteristic-polynomial bridge. Level 2 requires a **rigorous speed-`log n` LDP with an explicit rate function** for the positive fixed-energy kernel / phase-derivative observable at `beta=4, E=0`. A candidate rate, a CLT, terminal characteristic-polynomial LDP, or numerical fit does not count.

Before: `B_spectrum=1`.  
After: `B_spectrum=1`.

So this run is **NO MOVEMENT** under the frozen metric.

## 3. #5 ADD A PARAMETER AND DIFFERENTIATE — the tilt has a hard wall

Let `p_k` be the `mu_beta`-orthonormal first-kind polynomials and

`K_n(0,0)=sum_{k=0}^n p_k(0)^2`.

Use Lambert--Paquette / Dumitriu--Edelman normalization for the infinite nested Jacobi matrix: diagonal variables are Gaussian and the first off-diagonal is

`c_1 = a_1/sqrt(beta)`,  with  `a_1 ~ chi_beta`,

independent of the first diagonal variable `d_0`. At `E=0`,

`p_1(0) = -d_0/c_1`.

Therefore `K_n(0,0) >= p_1(0)^2` for every `n>=1`.

### Proposition 3.1 (exact finite-prefix moment wall)

For every `n>=1`,

`E[K_n(0,0)^t] = infinity` for every `t >= beta/2`.

For every fixed finite `n`, the same moment is finite for `0 <= t < beta/2`.

#### Proof

The chi density at zero is `const * x^{beta-1}(1+O(x^2))`. Hence

`E[c_1^{-2t}] < infinity  iff  beta-2t > 0`.

Since `d_0` is an independent nondegenerate Gaussian, `E|d_0|^{2t}` is finite and positive for every finite `t>=0`; the lower bound `K_n^t >= |d_0/c_1|^{2t}` proves divergence at and above `beta/2`.

For `t<beta/2`, each finite-degree `p_k(0)` is a polynomial in finitely many diagonal variables divided by `c_1...c_k`. All Gaussian positive moments are finite, and for every `j>=1`, `c_j` has chi parameter `beta*j`, so the required negative moment of `c_j` is finite because `t<beta/2 <= beta*j/2`. The finite sum defining `K_n`, together with the elementary finite-sum inequality for powers, gives finiteness. QED.

At `beta=4`, the critical tilt is therefore exactly

`t_c=2`.

This is not a technical nuisance: any annealed speed-`log n` Gärtner--Ellis route for the **unconditioned** kernel must see a non-steep endpoint at `t=2`. The preceding R14 run saw the same phenomenon inside the exact gamma-product factor `Q_n`; Proposition 3.1 shows that it is already intrinsic to `K_n` itself.

### The bulk tilt suggested by Breuer's Prüfer expansion

Breuer's critical random-Jacobi parameters for beta-Hermite are

`eta_1=1/2`, `eta_2=0`, `Lambda=1/beta`.

His Proposition 2.3 gives, for every fixed energy and fixed initial angle,

`log R_n^2 / log n -> eta_1 + Lambda = 1/2 + 1/beta` almost surely.

At `E=0`, the deterministic comparison phase is especially simple: `k_n=pi/2` exactly. Write `phi_n = bar(theta)_{n-1}`. In Breuer's notation, to first order in `j^{-1/2}`,

`A_j = 2 sqrt(2/beta) Y_j / sqrt(j) + O(j^{-1})`,

`B_j = sqrt(2/beta) X_j / sqrt(j) + O(j^{-1})`,

where `E X_j=E Y_j=0`, `Var X_j=1`, `Var Y_j=1/4+O(j^{-1})`, and the fresh `(X_j,Y_j)` are independent of the past phase. Expanding Breuer's exact amplitude recursion (his (2.17), with (2.36)--(2.39)) gives the leading centered increment

`xi_j = -sqrt(2/beta)/sqrt(j) * [ X_j sin(2 phi_j) + 2 Y_j cos(2 phi_j) ]`.

The key cancellation is exact at leading order:

`E[xi_j^2 | F_{j-1}] = 2/(beta*j) + O(j^{-2})`,

because

`Var[X_j sin(2phi)+2Y_j cos(2phi)] = sin^2(2phi)+cos^2(2phi)+O(j^{-1})`.

The phase-independent harmonic drift is `1/2+1/beta`; the remaining order-`1/j` drift is a multiple of `cos(2phi_j)`. Because `E=0` gives a `pi/2` phase advance, that oscillatory drift changes sign on the next step up to an `O_P(j^{-1/2})` error.

Thus the **candidate bulk logarithmic cumulant** for `L_n:=log R_n^2` is

`psi_bulk(t) = (1/2+1/beta)t + t^2/beta`.

At `beta=4`,

`psi_bulk(t)=3t/4+t^2/4`.

This formula is **not promoted to an LDP theorem in this report**. What is proved above is the leading conditional variance identity and the exact moment wall. The missing upgrade is a uniform exponentially-integrable control of the two-step Taylor remainder under exponential tilt; Breuer's published argument is almost-sure / law-of-large-numbers scale, not the exponential-equivalence statement needed here.

## 4. #11 DUALIZE — two exact reductions of the positive kernel

### 4.1 Christoffel variational dual

The Christoffel function is

`lambda_n(E)=1/K_n(E,E)`

and satisfies the exact extremal principle

`lambda_n(E) = min { int |P(x)|^2 d mu_beta(x) : deg(P)<=n, P(E)=1 }`.

The unique minimizer is

`P_n^*(x)=K_n(x,E)/K_n(E,E)`.

So a lower-tail event for `K_n` is an upper-tail event for the minimum energy needed to interpolate the value one at `E`. This is the natural dual object for eventual conversion to local-mass exponents; it also makes clear that a terminal characteristic polynomial alone cannot determine the source spectrum.

### 4.2 Exact pathwise reduction to Breuer's amplitude

Breuer's equation (2.14) states that, for fixed initial angle, eventually almost surely,

`R_j^2` is comparable to `tilde(a)_j^2 (p_j^2+p_{j+1}^2)`.

For beta-Hermite, `tilde(a)_j^2 ~ (beta/2) j`. Hence there are random finite `J` and random constants `0<c<C<infinity` such that for all `j>=J`,

`c R_j^2/j <= p_j(0)^2+p_{j+1}(0)^2 <= C R_j^2/j`.

Summing and using that every interior `p_k^2` occurs in at most two adjacent pairs yields

`K_N(0,0) asymp_omega 1 + sum_{j=J}^{N-1} R_j(0)^2/j`.

In particular,

`log K_N(0,0) = log(1+sum_{j<=N} R_j(0)^2/j) + O_omega(1)`.

This is a complete pathwise reduction of the **positive** kernel to one positive harmonic sum of the Prüfer amplitude. It removes the sign/zero problem of individual characteristic polynomials. It is also the precise real-line analogue of the positive norm observable used by Alberts--Normand in the circular model.

This reduction alone is not a speed-`log n` LDP: an a.s. random comparison constant is not automatically exponentially negligible under the annealed disorder law. But it identifies exactly which strengthening is needed.

## 5. #24 FIND THE EXTREMAL OBJECT — explicit candidate rate and the finite-prefix branch

Assume for the moment the missing logarithmic-time process LDP:

`Y_N(s) := log R_{floor(N^s)}(0)^2 / log N`,  `0<=s<=1`,

with speed `log N` and Cameron--Martin action

`I_path(y) = (beta/4) int_0^1 [ y'(s) - a ]^2 ds`,

where

`a = 1/2 + 1/beta`,

for absolutely continuous paths with `y(0)=0` (and infinity otherwise).

The harmonic-sum reduction in Section 4 says that the kernel exponent is the logarithmic-scale maximum of this path. Indeed, a multiplicative block `j in [N^s,N^{s+ds}]` has harmonic weight `sum 1/j ~ ds log N`, which has zero exponent; hence

`log K_N/log N` contracts to `sup_{0<=s<=1} y(s)`.

### Lemma 5.1 (the deterministic contraction is explicit)

For `x>=0`,

`inf { I_path(y): y(0)=0, sup y = x } = (beta/4)(x-a)^2`.

For `x<0` the cost is infinity because `K_N>=1`.

#### Proof

For any admissible path with `sup y=x`, choose `tau` with `y(tau)=x` up to an arbitrarily small approximation. Cauchy--Schwarz gives

`int_0^tau (y'-a)^2 ds >= (x-a tau)^2/tau`.

The remaining action is nonnegative. Minimizing the right side over `0<tau<=1` under the constraint that the path does not exceed `x` gives `tau=1` for the minimizing straight path; equivalently one may vary `tau` directly and check that any early hit followed by a constrained continuation costs at least the straight interpolation. The path `y(s)=xs` attains `(x-a)^2`. Multiplication by `beta/4` gives the claim. QED.

Thus the **bulk-only candidate** is

`I_bulk,beta(x) = (beta/4) (x - (1/2+1/beta))^2`,  `x>=0`.

At `beta=4`:

`I_bulk,4(x) = (x-3/4)^2`.

### The finite-prefix extremizer changes the far upper tail

Proposition 3.1 forces an additional mechanism. A polynomial boost `h>=0` supplied by an anomalously small first off-diagonal has speed-`log n` cost `(beta/2)h`, while the remaining tail can realize a bulk exponent `y`. The natural annealed extremal problem is therefore the infimal convolution

`I_ann,beta(x) = inf_{0<=y<=x} [ I_bulk,beta(y) + (beta/2)(x-y) ]`.

This minimization is exact algebra. Let `x_* = a+1 = 3/2+1/beta`. Then

`I_ann,beta(x) =`

- `(beta/4)(x-a)^2`, for `0<=x<=x_*`;
- `(beta/2)x - (beta+1)/2`, for `x>=x_*`.

At `beta=4` this becomes the explicit piecewise candidate

`I_ann,4(x) =`

- `(x-3/4)^2`, for `0<=x<=7/4`;
- `2x-5/2`, for `x>=7/4`;
- `infinity`, for `x<0`.

The two branches meet tangentially at `x=7/4` with value `1` and slope `2`, exactly the critical tilt `t_c=2` from Proposition 3.1.

**Important label:** this is a proved variational consequence of the stated process-LDP input, plus an exact finite-prefix moment obstruction; it is **not yet a proved LDP for `K_N`**. Therefore `B_spectrum` does not move.

This calculation also clarifies the source-level geometry. The linear far-tail branch is an **annealed finite-prefix artifact**: changing finitely many Jacobi coefficients can multiply polynomial solutions by a large random constant but cannot alter the almost-sure local scaling exponent of a fixed infinite realization. A multifractal-spectrum proof should therefore separate (i) the quenched / tail large deviations that survive finite-prefix conditioning from (ii) annealed fixed-energy rare events generated by the first few coefficients.

## 6. The exact missing lemma is now one two-step statement

At `beta=4,E=0`, set `L_n=log R_n^2` and pair the steps. The route to `B_spectrum=2` is reduced to proving the following uniform tilted estimate (or a statement strong enough to imply it):

`PAIR-CGF_4:` for every compact `T subset R`, there is `C_T<infinity` such that for all large `m`, uniformly in the incoming projective phase,

`| log E[ exp( t (L_{2m}-L_{2m-2}) ) | F_{2m-2} ] - (3t/4+t^2/4)/m | <= C_T m^{-3/2}`

for `t in T`.

Why this is the right lemma:

1. `E=0` gives the exact deterministic phase increment `pi/2` before the `O(m^{-1/2})` random perturbation, so the order-`1/m` `cos(2phi)` drift cancels between the two members of a pair.
2. The leading martingale variance is phase-free because `Var X=1` and `Var(2Y)=1+O(1/m)`.
3. The chi and Gaussian entries have uniform exponential moments at the `m^{-1/2}` scale, while the probability of a large relative chi deviation is exponentially small in `m`.
4. Summing an `O(m^{-3/2})` conditional-CGF error is finite. Tower iteration would then give the correct log-Laplace limits on every logarithmic interval.
5. Standard exponential-tightness estimates for the paired martingale would promote the finite-dimensional limits to the required logarithmic-time path LDP, after which Section 5 gives the kernel rate by contraction.

What is still missing is item 4's prerequisite: a **fully written uniform remainder proof under the tilted one-step law**, including the effect of the first-step tilt on the second-step phase. Breuer proves the relevant Taylor expansion for almost-sure asymptotics, but not this tilted uniform estimate. Lambert--Paquette give a powerful fixed-energy martingale approximation, but the current theorem statement does not provide the speed-`log n` exponential-equivalence bound needed to substitute for `PAIR-CGF_4`.

That is the single obstruction carried forward. I do not label it proved.

## 7. Relation to the closest solved circular problem

Alberts--Normand prove for the circular-beta spectral measure a speed-`log n` LDP for the corresponding positive orthogonal-polynomial norm. In their normalization the unweighted-angle rate is

`I_CbetaE(x) = (beta/8)(x-1-2/beta)^2`, `x>=0`.

Their argument works because the OPUC recursion turns the logarithmic norm into a process whose large deviations can be controlled directly from the independent Verblunsky coefficients. The beta-Hermite calculation above shows exactly what replaces that mechanism:

- real-line EFGP amplitude `R_n`;
- paired `pi/2` phase cancellation at `E=0`;
- variance coefficient `2/beta` rather than `4/beta`;
- the positive harmonic-sum reduction `K_N asymp sum R_j^2/j`;
- and an annealed finite-prefix moment wall at `t=beta/2`.

So the circular theorem is a genuine blueprint, but copying its final parabola in degree coordinates would be unjustified.

## 8. Outcome of the three methods

**#5 ADD A PARAMETER AND DIFFERENTIATE.** The tilt parameter exposes an exact obstruction: `E K_n^t` ceases to exist at `t=beta/2` (at beta 4, `t=2`). The leading Breuer conditional cumulants predict `3t/4+t^2/4` in the bulk at beta 4, but an exponential-equivalence proof is still needed.

**#11 DUALIZE.** The Christoffel variational principle and Breuer's EFGP identity give two positive formulations. Most usefully, `K_N(0,0)` is pathwise comparable to `1+sum R_j(0)^2/j`; this removes characteristic-polynomial zeros and reduces level 2 to a positive amplitude process.

**#24 FIND THE EXTREMAL OBJECT.** The Cameron--Martin contraction is explicit. It predicts the bulk parabola `(x-3/4)^2` at beta 4 and, once the exact prefix wall is included, a tangential linear branch `2x-5/2` beyond `x=7/4`. This is a candidate until `PAIR-CGF_4` is proved.

## 9. Status and next moves

Status: **OPEN / PARTIAL**.  
Metric: `B_spectrum=1` unchanged.  
No numerical endpoint or heuristic rate is counted as a rigorous metric advance.

This is the first unchanged D0039 run after the preceding metric move; the shared authoritative stagnation field remains `UNKNOWN`, so I do not invent a numeric fleet count.

The next triple must differ from `5,11,24`. The most promising fresh moves are:

- **#7 TAKE THE LIMIT:** prove `PAIR-CGF_4` and pass to the logarithmic-time diffusion/path LDP rather than another terminal CLT;
- **#10 DERANDOMIZE:** for the LDP lower bound, replace a change-of-measure existence argument by an explicit deterministic Cameron--Martin control of the paired phase/amplitude recursion;
- **#25 COUNT THE SAME THING TWICE:** derive the same kernel exponent simultaneously from the EFGP harmonic sum and the Christoffel--Darboux Wronskian/phase derivative, using the equality to audit all normalization constants and isolate finite-prefix factors.

If three consecutive D0039 runs leave the same metric / obligation unchanged, the Section-I stuck protocol will trigger. It has not triggered on this run.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  worker: R14
  lane: HARD_OUTSIDE
  source_id: D0039
  source: "Virag, Operator limits of random matrices, ICM 2014, Question 1"
  target: "beta-Hermite spectral-measure multifractal spectrum versus matched Gaussian multiplicative cascade"
  status: "OPEN / PARTIAL"
  metric:
    name: B_spectrum
    before: 1
    after: 1
    movement: false
    authoritative_stagnation_count: UNKNOWN
  methods: [5, 11, 24]
  proved_this_run:
    - "For every finite n>=1, E[K_n(0,0)^t]=infinity for t>=beta/2 and is finite for 0<=t<beta/2."
    - "Pathwise eventually, K_N(0,0) is comparable to 1+sum_{j<=N} R_j(0)^2/j."
    - "Conditional on the stated quadratic path LDP, the bulk contraction rate is (beta/4)(x-(1/2+1/beta))^2 for x>=0."
    - "The finite-prefix infimal convolution has a tangential linear branch; at beta=4 the candidate is (x-3/4)^2 up to x=7/4 and 2x-5/2 afterwards."
  not_proved:
    - "PAIR-CGF_4 uniform tilted two-step remainder estimate"
    - "speed-log n process LDP for beta-Hermite EFGP amplitude"
    - "speed-log n LDP for K_N itself"
    - "energy-uniform level-set Hausdorff spectrum"
  fixed_energy_candidate_beta4:
    typical_kernel_exponent: "3/4"
    bulk_rate: "(x-3/4)^2"
    critical_tilt: "2"
    annealed_candidate_rate: "(x-3/4)^2 for 0<=x<=7/4; 2x-5/2 for x>=7/4"
    label: "candidate / conditional, not a B_spectrum endpoint"
  exact_remaining_obligation: "prove PAIR-CGF_4 (or equivalent exponential approximation), then process LDP and positive-kernel contraction"
  prior_art_boundary:
    - "Breuer 2008: almost-sure transfer exponents / exact Hausdorff dimension, no multifractal LDP"
    - "Alberts--Normand 2022: circular-beta norm LDP, not beta-Hermite Jacobi"
    - "Lambert--Paquette 2025: bulk characteristic-polynomial martingale asymptotics, no stated speed-log n positive-kernel LDP"
    - "Chhaibi--Najnudel 2026: circular beta/GMC, not source closure"
  next_methods: [7, 10, 25]
  checker: none
  checker_reason: "No finite combinatorial claim; this run is analytic. No certificate was manufactured for an unchanged metric."
  audit_ids: []
  shared_roots_edited: false
  peer_files_edited: false
  email: false
  drive: false
  public_posting: false
  scheduler_modified: false
```

## 11. Model / scheduler control

The exposed automation/task interface still does **not** provide a binding model-family selector, reasoning-effort selector, guaranteed-duration field, or authenticated completed-run model telemetry. Therefore `GPT-6 / maximum` remains prompt text only, and this report does not claim it actually ran.

The historical P26 `You cannot modify this task` failure was an authorization-context boundary; later repository reconciliation records that P26 could be updated from an authorized owning P/C context. The lawful workaround for any task that still refuses modification is the authorized owning/admin context or platform support, not permission bypass or duplicate scheduling.

No scheduler, permission, workflow, email, Drive, or public-posting action was attempted in this run.
