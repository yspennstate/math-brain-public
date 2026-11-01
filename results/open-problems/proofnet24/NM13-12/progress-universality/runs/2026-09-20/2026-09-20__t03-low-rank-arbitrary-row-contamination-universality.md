Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested but is not authenticated by this runtime.**

# NM13-12 progress-universality — low-rank arbitrary-row contamination resilience for T03

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-12`  
Progress root: `proofnet24/NM13-12/progress-universality/`  
Owner policy: `operations/PROGRESS20_2026-09-20.md`  
Parent application: T03 negative spherical perceptron at `kappa=-1`  
Status: **PARTIAL / NEW FINITE-N THEOREM PROVED / DISTRIBUTIONAL-CLASS GAIN / ORIGINAL PURE-GAUSSIAN T03 BRACKET NOT MOVED BY THIS RUN**

## 1. Compact handoff: P12, predecessor theorem, and exclusions

The latest canonical P12 report on current `master` is

`proofnet24/P12-smooth-iid/runs/2026-09-17/2026-09-17T18-20-03Z__run-report.md`.

Its frozen mathematical theorem is unchanged. For `F in {R,C}`, with `d_R=1`, `d_C=2`, if `A_m in F^{N_m x m}` has iid centered variance-one entries with density `f_m`, and there exist one fixed integer `q>=1` and one fixed `M<infinity` such that

`sup_m ||f_m^{*q}||_infinity <= M`,

while

`N_m/m -> gamma>1`, `k_m=r_m+1`, and `k_m log m=o(m)`,

then

`(k_m/m) log M^F_{m,r_m}(A_m) ->_P -h(gamma)/d_F`.

There is **no fourth-moment assumption and no positive-moment assumption above variance normalization** in that theorem. Fixed bounded-density laws are included with `q=1`. The mathematical successor still outside P12 is triangular smooth / bounded-fourth-moment universality without one uniform microscopic finite-convolution smoothing hypothesis. P12's own remaining obligations are audit/package gates, not an author-side theorem gap.

`POSTED.md` excludes rediscovery of the row-submatrix papers, mesoscopic-spike paper, kernel / neural-means work, ReLU work, and zero-margin / Ising perceptron capacity. Nothing in this report is a least-singular-value row-submatrix theorem, a kernel statement, ReLU statement, or zero-margin result.

### NM13-12 predecessor

The immediately preceding NM13-12 theorem was the spectral-quantile covariance sandwich. For deterministic positive-definite `Sigma` with eigenvalues

`0<lambda_1<=...<=lambda_N`,

it proved, for `kappa<0`,

`p_iso(M,d,kappa/sqrt(u)) <= p_Sigma(M,N,kappa) <= p_iso(M,N,kappa/sqrt(ell))`

whenever `u>=lambda_d` and `0<ell<=lambda_1`.

That theorem allowed `rank(Sigma-I)=N` and unbounded top eigenvalues, but **every row was still Gaussian with the same covariance**. The new theorem below is a strict distributional-class extension: it permits an additional linear number of completely arbitrary, even infinite-variance, non-Gaussian constraints, provided their row span has controlled rank. No density, moment, tail, independence-among-contaminants, radial, or elliptical assumption is imposed on those rows.

## 2. Exact T03 parent and coordination

The source T03 model remains

- `M=floor(alpha N)`;
- `g_a iid N(0,I_N)`;
- `||sigma||_2=sqrt(N)` exactly;
- `<g_a,sigma> >= -sqrt(N)` for all constraints;
- fixed `alpha`, `N->infinity`.

Equivalently, with `x=sigma/sqrt(N)`, one seeks `x in S^{N-1}` with `Gx>=-1`.

The last fully reported repository bracket entering this run is

`alpha_L = 6.30297437506`,
`alpha_U = 12.78437096216`,
`W = 6.48139658710`.

NM13-03 has now proved a stationary-branch transport theorem and numerically supported a source-level `alpha=12.33` candidate, but explicitly leaves directed continuum enclosure pending.

NM13-07 has, during this run, added a stronger interval artifact

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_alpha1275_interval_contraction.out`

whose executed output ends

`CERTIFIED_ALPHA_U 12.75`,
`CERTIFIED_PSI_LOWER 0.0150497744619429886066833`,
`ALL_INTERVAL_CONTRACTION_CHECKS_PASS`.

I do **not** silently promote the parent ledger from that artifact alone: as of the last peer search in this invocation, the latest NM13-07 report still predates this interval artifact and no new peer report had yet completed the source-theorem transfer. The universality theorem below is independent of that bookkeeping boundary. If the NM13-07 `12.75` transfer is promoted, its upper endpoint immediately transfers to the new contaminated class; if NM13-03 later certifies `12.33`, that endpoint transfers as well.

This route does not duplicate either peer: they are certifying the isotropic second-full RDT stationary system; this report proves a semi-random row-contamination comparison by subspace geometry and Gaussian rotational invariance.

## 3. New finite-N theorem: arbitrary-row contamination plus spectral-quantile Gaussian core

For an `m x N` matrix `A`, a `k x N` matrix `B`, and `kappa<=0`, write

`SAT(A,B;kappa)`

for the event that there exists `x in S^{N-1}` such that

`A x >= kappa 1_m`
and
`B x >= kappa 1_k`.

Let `G` be an iid standard Gaussian `m x N` matrix. Let `Sigma` be deterministic positive definite, and let `B` be deterministic or random **independent of `G`**. Suppose

`rank(B) <= r`.

Let the eigenvalues of `Sigma` be

`0<lambda_1<=...<=lambda_N`.

Choose `d0` with `1<=d0<=N`, and numbers `u,ell>0` such that

`lambda_d0 <= u`,
`lambda_1 >= ell`.

Assume `d0>r`.

### Theorem NM12-ROWCONTAM

For every finite `m,k,N`, every `kappa<=0`, and every such `Sigma,B`,

`p_iso(m,d0-r,kappa/sqrt(u))`
`<= P{ SAT(G Sigma^{1/2}, B; kappa) }`
`<= p_iso(m,N,kappa/sqrt(ell))`.                         (3.1)

The probability is over `G` and, when random, `B`.

No assumption is made on:

- the number `k` of contaminant rows;
- their norms;
- their marginal distributions;
- existence of their means or variances;
- independence among contaminant rows;
- density or anti-concentration of contaminant entries.

Only independence of the contaminant block from `G` and the row-span rank bound enter the proof.

### Proof: lower comparison

Condition on `B` when it is random. Let `E` be the spectral subspace of `Sigma` spanned by the bottom `d0` eigenvectors. Then

`Sigma|_E <= u I_E`.

Let

`F = E intersect ker(B)`.

By the codimension inequality,

`dim(F) >= d0-r`.

Choose an `(d0-r)`-dimensional subspace `F0 subset F`, and let `Q` be an `N x (d0-r)` matrix with orthonormal columns spanning `F0`.

For every `z`, `BQz=0`. Define the compressed covariance

`C = Q^T Sigma Q`.

Since `range(Q) subset E`,

`0 < C <= u I`.

Conditional on `B`, the Gaussian core restricted to `F0` has the distribution

`G Sigma^{1/2} Q  =_d  H C^{1/2}`,

where `H` is an iid standard Gaussian `m x (d0-r)` matrix.

Now suppose `z in S^{d0-r-1}` satisfies

`H z >= kappa/sqrt(u)`.

Set

`w=C^{-1/2}z`,
`y=w/||w||`,
`s=1/||w||`.

Because `C<=uI`,

`||w||^2 = <z,C^{-1}z> >= 1/u`,

hence

`s<=sqrt(u)`,

and

`C^{1/2}y = s z`.

For a row coordinate with `(Hz)_a>=0`,

`s(Hz)_a >= 0 >= kappa`.

For a row coordinate with `(Hz)_a<0`, the inequality `s<=sqrt(u)` gives

`s(Hz)_a >= sqrt(u)(Hz)_a >= kappa`.

Therefore

`H C^{1/2} y >= kappa 1_m`.

The ambient vector `x=Qy` lies on `S^{N-1}`, satisfies the Gaussian-core constraints, and also satisfies

`Bx=0 >= kappa`.

Thus, pathwise after conditioning on `B`,

`SAT(H,kappa/sqrt(u)) subset SAT(G Sigma^{1/2},B;kappa)`.

Taking probabilities proves the lower inequality in (3.1).

### Proof: upper comparison

If `x in S^{N-1}` satisfies the full system, it in particular satisfies

`G Sigma^{1/2}x >= kappa 1_m`.

Put

`t=||Sigma^{1/2}x||`,
`z=Sigma^{1/2}x/t`.

Since `Sigma>=ell I`,

`t>=sqrt(ell)`.

Therefore

`Gz >= (kappa/t)1_m >= (kappa/sqrt(ell))1_m`

because `kappa<=0`. Hence full feasibility implies isotropic Gaussian feasibility at margin `kappa/sqrt(ell)`, proving the upper bound.

QED.

## 4. Why this is a strict new universality extension

Set `B` absent and `r=0`: Theorem NM12-ROWCONTAM reduces to the preceding spectral-quantile covariance theorem.

The converse reduction is impossible. With `B` present, the full constraint matrix is no longer Gaussian, elliptical, iid-entry, iid-row, or even finite-variance in general. For example, `B` may have iid Cauchy coefficients inside a fixed low-dimensional row span. The previous covariance theorem says nothing about such extra constraints.

The extension is also stronger than an `o(N)`-row contamination result. The number of arbitrary rows may be `Theta(N)` or larger; only their **rank** costs dimension. This is the quantitative gain:

- `rho_Sigma`: fraction of Gaussian-core spectral directions discarded;
- `rho_B`: contaminant row-span rank fraction;
- `epsilon`: spectral inflation of the retained Gaussian-core bulk.

At `kappa=-1`, the lower comparison benchmark is

`A_L(rho_Sigma,rho_B,epsilon)`
`= (1-rho_Sigma-rho_B) / Phi(-1/sqrt(1+epsilon))`.          (4.1)

Near `(0,0,0)`,

`A_L`
`= L - L(rho_Sigma+rho_B) - C_epsilon epsilon`
`  + O((rho_Sigma+rho_B)epsilon + epsilon^2)`,              (4.2)

where

`L=1/Phi(-1)=6.302974375068753...`

and

`C_epsilon=phi(1)/(2 Phi(-1)^2)=4.806444282078035...`.

Thus arbitrary-row rank loss enters at exactly the same first-order dimensional cost as deleting spectral directions.

## 5. Concrete unresolved T03 extension: full-rank anisotropic Gaussian core plus one linear density of Cauchy contaminants

Fix total load `alpha>1`.

### Gaussian core

Let

`m_N=floor((alpha-1)N)`.

Take the same genuinely full-rank covariance family introduced in the predecessor run. Let

`s_N=floor(N^(3/4))`,
`d0_N=N-s_N`,
`epsilon_N=N^(-1/3)`,

and define `Sigma_N` in a deterministic orthonormal basis by

`lambda_j = 1 + epsilon_N * j/(d0_N+1)`,  `1<=j<=d0_N`,

while

`lambda_j = exp(N^(1/10))`,  `d0_N<j<=N`.

Then:

- every eigenvalue differs from `1`, so `rank(Sigma_N-I)=N`;
- `lambda_1>1`;
- `lambda_d0_N<1+epsilon_N`;
- `s_N/N -> 0`;
- `epsilon_N -> 0`;
- `||Sigma_N||_op -> infinity`.

### Contaminant block

Let

`r_N=floor(N^(2/3))`,
`K_N=N`.

Fix any deterministic `N x r_N` matrix `R_N` with orthonormal columns. Let `H_N` be a `K_N x r_N` matrix of iid standard Cauchy variables, independent of the Gaussian core, and set

`B_N = H_N R_N^T`.

Then

`rank(B_N) <= r_N=o(N)`,

but there are **exactly `N` contaminant constraints**, and their entries need not have a first moment or a variance.

The full model is:

find `x in S^{N-1}` such that

`G_N Sigma_N^{1/2} x >= -1`
and
`B_N x >= -1`.

Its total number of constraints is

`m_N+K_N = alpha N + o(N)`.

This is a concrete semi-random heavy-tailed negative spherical perceptron. Its exact threshold is not known.

### Rigorous lower implication

Theorem NM12-ROWCONTAM gives

`P{SAT full model}`
`>= p_iso(m_N, d0_N-r_N, -1/sqrt(1+epsilon_N))`.

Since

`(d0_N-r_N)/N -> 1`
and
`epsilon_N -> 0`,

the Montanari--Zhong--Zhou fixed-margin LP theorem yields, for every fixed

`alpha < 1 + 1/Phi(-1)`,

SAT with probability tending to one.

Thus

`alpha_c^{contam} >= 1 + 6.302974375068753...`
`                    = 7.302974375068753...`.               (5.1)

The varying-margin step does not assume a triangular MZZ theorem: for any fixed `alpha<1+L`, choose a fixed harder margin `-1+eta` whose LP threshold still exceeds `alpha-1`; for sufficiently large `N`, `-1/sqrt(1+epsilon_N)<-1+eta`, and the finite-dimensional comparison transfers that fixed-margin witness.

### Rigorous upper implication

Because `Sigma_N>=I`, any full-system witness would imply an isotropic Gaussian witness for the `m_N` Gaussian-core constraints at margin `-1`. Therefore the retained rigorous isotropic T03 upper theorem gives

`alpha > 1 + 12.78437096216`
`      = 13.78437096216`

implies UNSAT with probability tending to one. Hence

`alpha_c^{contam} <= 13.78437096216`.                        (5.2)

Combining (5.1) and (5.2),

`boxed: 7.302974375068753...`
`       <= alpha_c^{contam}`
`       <= 13.78437096216.`                                 (5.3)

The width is exactly the retained pure-Gaussian width, because the linear-density contaminant block contributes one unit of total constraint density but costs only `o(N)` dimensions.

If NM13-07's `12.75` interval certificate is promoted to the pure-Gaussian source theorem, (5.2) immediately sharpens to

`alpha_c^{contam} <= 13.75`.

If NM13-03's `12.33` candidate is later outward-certified, the same transfer gives

`alpha_c^{contam} <= 13.33`.

No new heavy-tail or anisotropic calculation would be required.

## 6. Executed sanity checker

Source:

`proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/t03_lowrank_row_contamination_check.py`

Archived output:

`proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/t03_lowrank_row_contamination_check.out`

The executed output ends `ALL_CHECKS_PASS`.

It verifies:

- `L=6.302974375068753`;
- retained width arithmetic;
- shifted limiting bracket `[7.302974375068753,13.78437096216]`;
- the first-order epsilon coefficient `4.806444282078035`;
- exact-integer values of `floor(N^(3/4))` and `floor(N^(2/3))` for benchmark sizes;
- finite lower-comparison densities converging toward the limiting shifted endpoint.

Representative finite lower guarantees for the concrete model are:

- `N=10^6`: total-density lower comparison `6.995142406689`;
- `N=10^9`: `7.256458584103`;
- `N=10^12`: `7.295561048147`.

These are theorem-comparison benchmarks, not claims about finite-`N` sharp thresholds.

## 7. Parent before/after versus demonstrated theory gain

### Original pure-Gaussian T03 parent

Last fully reported bracket before this run:

`[6.30297437506, 12.78437096216]`,
width `6.48139658710`.

After **this NM13-12 run**:

same fully reported bracket.

This run does not claim that arbitrary-row universality narrows the original pure-Gaussian source interval. The new NM13-07 interval artifact is recorded separately as coordination evidence and is not silently promoted without its report-level source transfer.

### New theory/application gain

Before:

- spectral-quantile universality applied only when **all constraints were Gaussian** with one deterministic covariance;
- no theorem covered a linear number of arbitrary heavy-tailed contaminant constraints.

After:

- finite-N comparison (3.1) allows any number of arbitrary contaminant rows with only a rank penalty;
- contaminants may have no moments at all;
- the theorem composes with full-rank covariance deformation;
- a concrete model with `N` Cauchy constraints of rank `N^(2/3)` plus a full-rank anisotropic Gaussian core with unbounded operator norm inherits a rigorous threshold bracket shifted by exactly one unit in total density.

That is a strict distributional-class and dimension-regime extension, not a repackaging of the P12 row-submatrix theorem or the earlier radial/covariance-only results.

## 8. Literature boundary

Dated bounded search: 2026-09-20.

Queries included variants of:

- `"spherical perceptron" semi-random adversarial constraints Gaussian`;
- `"perceptron" adversarial contamination constraints Gaussian sphere`;
- `"spherical perceptron" heavy-tailed constraints universality`.

The search recovered the standard negative spherical perceptron sources and unrelated universality results, but did not surface a primary theorem matching the exact finite-N low-rank arbitrary-row contamination sandwich above. This is bounded negative evidence only, not a novelty certificate.

The source model remains El Alaoui--Sellke `arXiv:2010.15811`; the fully lifted upper-bound route remains Stojnic `arXiv:2312.16531`; the rigorous LP lower threshold used in the application is Montanari--Zhong--Zhou `arXiv:2110.15824`.

## 9. Residual obstruction and next nonduplicating attack

For the pure T03 source, the obstacle is still the peer stationarity certificate, not universality.

For the new universality line, the sharp next question is different:

> How much **full-rank** arbitrary row contamination can be tolerated when the contaminant block has small stable rank or small singular-value tail but no exact low-rank row span?

The present proof uses `ker(B)` exactly. A genuine successor must replace exact annihilation by a quantitative almost-kernel and track the resulting negative-margin error. A promising target is a singular-value quantile theorem in which only `o(N)` singular directions of `B` exceed a vanishing threshold. That would move from exact low rank to approximate low rank without touching NM13-03/NM13-07's RDT route.

No peer file, historical report, shared root ledger, schedule, permission, workflow, email, Drive object, paid compute, or public resource was modified.

```yaml
ledger_delta:
  worker: NM13-12
  parent: T03
  status: "PARTIAL / NEW FINITE-N UNIVERSALITY THEOREM / DISTRIBUTIONAL-CLASS GAIN"
  p12_latest_report: "proofnet24/P12-smooth-iid/runs/2026-09-17/2026-09-17T18-20-03Z__run-report.md"
  p12_scope:
    entries: "iid centered variance-one with densities f_m"
    microscopic_smoothing: "fixed q and M with sup_m ||f_m^{*q}||_infinity <= M"
    aspect: "N_m/m -> gamma>1"
    surplus: "k_m=r_m+1, k_m log m=o(m)"
    fourth_moment: "not assumed"
    unresolved_successor: "triangular smooth/B4 universality without uniform microscopic finite-convolution smoothing"
  original_parent_metric:
    quantity: "rigorous pure-Gaussian T03 bracket"
    before: "[6.30297437506,12.78437096216]"
    after: "[6.30297437506,12.78437096216]"
    movement_by_this_run: "none"
  peer_coordination:
    NM13-03: "stationary transport supports candidate alpha_U=12.33; outward enclosure pending"
    NM13-07: "new interval artifact outputs CERTIFIED_ALPHA_U 12.75 and ALL_INTERVAL_CONTRACTION_CHECKS_PASS; no newer report-level source transfer found during this invocation"
  theorem:
    name: "NM12-ROWCONTAM"
    finite_N_lower: "p_iso(m,d0-r,kappa/sqrt(u))"
    finite_N_upper: "p_iso(m,N,kappa/sqrt(ell))"
    new_assumption_gain: "arbitrary independent contaminant block; any row count; only rank(B)<=r; no moments/density/tail assumptions"
  application:
    model: "full-rank anisotropic Gaussian core + N Cauchy contaminant rows of rank floor(N^(2/3))"
    total_density_shift_beta: "1"
    lower: "7.302974375068753..."
    upper: "13.78437096216"
    exact_threshold: "UNKNOWN"
  artifacts:
    checker: "artifacts/t03_lowrank_row_contamination_check.py"
    output: "artifacts/t03_lowrank_row_contamination_check.out"
    output_tail: "ALL_CHECKS_PASS"
  next_attack: "replace exact low-rank contaminant span by a quantitative singular-value almost-kernel"
```
