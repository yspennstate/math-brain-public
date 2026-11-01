Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 / maximum was requested, but no authenticated applied-model / reasoning-effort receipt is exposed, so I do not claim otherwise.

# NM13-12 progress-universality — spectral-quantile full-rank covariance universality for T03

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-12`  
Progress root: `proofnet24/NM13-12/progress-universality/`  
Owner policy: `operations/PROGRESS20_2026-09-20.md`  
Parent application: T03 negative spherical perceptron at `kappa=-1`  
Status: **PARTIAL / NEW FINITE-N THEOREM PROVED / FULL-RANK DIMENSION-REGIME GAIN / ORIGINAL T03 BRACKET UNCHANGED**

## 1. Compact handoff: latest P12 state, exact hypotheses, and the mathematical successor

The latest canonical P12 report on current `master` is

`proofnet24/P12-smooth-iid/runs/2026-09-17/2026-09-17T18-20-03Z__run-report.md`.

This corrects the older continuity shorthand in my preceding report, which named an earlier P12 checkpoint. The theorem itself is unchanged.

For `F in {R,C}`, with `d_R=1`, `d_C=2`, let `A_m in F^{N_m x m}` have iid centered variance-one entries with density `f_m`. Assume one fixed integer `q>=1` and one fixed `M<infinity` such that

`sup_m ||f_m^{*q}||_infinity <= M`,

and

`N_m/m -> gamma>1`,

`k_m=r_m+1`,

`k_m log m=o(m)`.

Then the frozen P12 package proves

`(k_m/m) log M^F_{m,r_m}(A_m) ->_P -h(gamma)/d_F`.

There is **no fourth-moment assumption and no positive-moment assumption above variance normalization**. Fixed bounded-density laws are included with `q=1`. The explicit mathematical successor still outside the theorem is triangular smooth / bounded-fourth-moment universality **without** a uniform microscopic finite-convolution smoothing condition. P12's remaining own-track obligations are independent audit/final-package gates, not a missing author-side lemma.

`POSTED.md` excludes rediscovery of the posted row-submatrix papers, mesoscopic-spike paper, kernel / neural-means work, ReLU work, and zero-margin / Ising perceptron capacity. Nothing below is any of those objects. No least-singular-value minimum over row subsets appears here.

### Predecessor NM13-12 state

The preceding progress-universality runs proved, in order:

1. all-row radial hard-margin comparison;
2. defect-tolerant radial / quantile comparison;
3. low-rank PSD covariance comparison;
4. signed low-rank lower transfer plus a sharp contraction-axis nonuniversality window.

The strongest two-sided covariance statement before this run required

`Sigma=I+B`, `B>=0`, `rank(B)=r`,

and used the exact identity subspace `ker B` to obtain

`p_iso(M,N-r,kappa) <= p_Sigma(M,N,kappa) <= p_iso(M,N,kappa)`.

The signed successor then showed that identity-subspace lower transfer survives arbitrary low-rank sign, but two-sided signed universality fails without spectral control.

This run uses a **materially different spectral-quantile argument**. It removes the low-rank requirement entirely: `rank(Sigma-I)` may equal `N`, while an `N-o(N)` dimensional spectral bulk is only required to lie in a vanishing multiplicative window. The mechanism is a min-max / spectral-subspace comparison, not an identity-kernel argument and not a radial-row argument.

## 2. Exact T03 parent and coordination state

The source T03 model remains exact:

- `M=floor(alpha N)`;
- iid `g_a ~ N(0,I_N)`;
- seek `sigma` with `||sigma||_2=sqrt(N)` exactly;
- `<g_a,sigma> >= -sqrt(N)` for all `a<=M`;
- fixed `alpha`, `N->infinity`.

Equivalently, with `x=sigma/sqrt(N)`, seek `x in S^{N-1}` with

`Gx >= -1`.

Repository-supported rigorous bracket entering this run:

`alpha_L = 6.30297437506`,

`alpha_U = 12.78437096216`,

`W = 6.48139658710`.

### NM13-03 / NM13-07 coordination

NM13-03's current report proves a closed one-dimensional conditional-Gaussian kernel and exhibits an `alpha=12.75` Poincare--Miranda rectangle, but correctly leaves that endpoint review-pending until a directed continuum enclosure is supplied.

NM13-07's newer report proves the tilted-moment tower `J_0,...,J_4`, closes the first Jacobian analytically, and gives a broad deterministic contraction compiler. It likewise leaves the source bracket unchanged because the outward-rounded integral enclosure is not yet finished.

I do not duplicate either stationarity route. The comparison below has a useful coordination consequence: **any future isotropic Gaussian UNSAT endpoint they certify transfers immediately to the full-rank covariance class proved here**, because the upper event inclusion is exact.

## 3. New finite-N theorem — spectral-quantile covariance sandwich

For an `M x N` matrix `A` and `kappa<0`, write

`SAT(A,kappa) := { exists x in S^{N-1}: A x >= kappa 1_M }`.

Let `G` be an iid standard Gaussian `M x N` matrix. For deterministic positive-definite `Sigma`, define

`p_Sigma(M,N,kappa)=P{SAT(G Sigma^{1/2},kappa)}`,

and let `p_iso(M,d,kappa)` be the corresponding isotropic probability for an iid standard Gaussian `M x d` matrix.

Write the eigenvalues of `Sigma` in nondecreasing order

`0<lambda_1<=...<=lambda_N`.

### Theorem NM12-SQ

Fix `1<=d<=N`, `u>=lambda_d`, and `ell<=lambda_1` with `ell>0`. Then for every finite `M,N` and every `kappa<0`,

`p_iso(M,d,kappa/sqrt(u))`

`<= p_Sigma(M,N,kappa)`

`<= p_iso(M,N,kappa/sqrt(ell))`.                         (3.1)

In particular, if

`lambda_1>=1`,

`lambda_{N-r}<=1+epsilon`,

then

`boxed: p_iso(M,N-r,kappa/sqrt(1+epsilon))`

`       <= p_Sigma(M,N,kappa)`

`       <= p_iso(M,N,kappa).`                            (3.2)

No bound on `lambda_N`, `||Sigma||_op`, or `rank(Sigma-I)` is required.

### Proof of the lower inclusion

Let `E` be the span of eigenvectors corresponding to `lambda_1,...,lambda_d`, and let `Q` be an `N x d` matrix with orthonormal columns spanning `E`. Thus

`Sigma|_E <= u I_E`.

Assume `z in S^{d-1}` satisfies

`(GQ) z >= kappa/sqrt(u)`.

Put `y=Qz`, so `||y||=1` and `y in E`. Define

`w=Sigma^{-1/2} y`,

`x=w/||w||`,

`s=1/||w||`.

Then `x in S^{N-1}` and

`Sigma^{1/2} x = s y`.

Because `Sigma|_E <= u I_E`,

`||w||^2 = <y,Sigma^{-1}y> >= 1/u`,

so

`s <= sqrt(u)`.

For each row coordinate `a`, if `(Gy)_a>=0`, then

`s(Gy)_a >= 0 > kappa`.

If `(Gy)_a<0`, then `s<=sqrt(u)` reverses the useful magnitude inequality for a negative number:

`s(Gy)_a >= sqrt(u)(Gy)_a >= kappa`.

Therefore

`G Sigma^{1/2} x = s G y >= kappa 1_M`.

Hence pathwise

`SAT(GQ,kappa/sqrt(u)) subset SAT(G Sigma^{1/2},kappa)`.

Since `Q` is deterministic orthonormal and `G` is iid standard Gaussian, rotational invariance gives `GQ` as an iid standard Gaussian `M x d` matrix. Taking probabilities proves the lower bound.

### Proof of the upper inclusion

Assume `x in S^{N-1}` satisfies

`G Sigma^{1/2} x >= kappa 1_M`.

Set

`y=Sigma^{1/2}x`,

`t=||y||`,

`z=y/t in S^{N-1}`.

Since `Sigma>=ell I`,

`t^2=<x,Sigma x> >= ell`,

so `t>=sqrt(ell)`. Dividing the witness inequalities by `t` gives

`Gz >= (kappa/t) 1_M`.

Because `kappa<0` and `t>=sqrt(ell)`,

`kappa/t >= kappa/sqrt(ell)`.

Thus

`SAT(G Sigma^{1/2},kappa) subset SAT(G,kappa/sqrt(ell))`.

Taking probabilities proves the upper bound and completes (3.1). Taking `d=N-r`, `u=1+epsilon`, `ell=1` gives (3.2). QED.

### Why this strictly improves the predecessor regime

The predecessor PSD theorem needed an exact identity subspace of dimension `N-r`; equivalently `Sigma-I` had low rank. The new theorem only needs a **spectral quantile**:

- all eigenvalues are at least `1` for the clean upper transfer;
- all but `r` eigenvalues are at most `1+epsilon` for the lower transfer.

Every one of those `N-r` bulk eigenvalues may differ from `1`. Therefore `rank(Sigma-I)` may be exactly `N`.

## 4. Quantitative asymptotic corollary at `kappa=-1`

Let `r_N/N -> rho in [0,1)` and suppose

`lambda_1(Sigma_N)>=1`,

`lambda_{N-r_N}(Sigma_N)<=1+epsilon`

for one fixed `epsilon>=0`.

The Montanari--Zhong--Zhou LP success theorem, under the exact iid Gaussian / unit-sphere normalization used by T03, has fixed-margin success threshold

`delta_lin(kappa)=1/Phi(kappa)`.

Apply the lower comparison in dimension

`d_N=N-r_N`.

The effective constraint density there is

`M/d_N -> alpha/(1-rho)`.

Therefore (3.2) and the MZZ fixed-margin theorem give the fully rigorous SAT region

`boxed: alpha < (1-rho) / Phi(-1/sqrt(1+epsilon))`

`       => SAT whp.`                                      (4.1)

The upper side remains exactly the isotropic T03 upper comparison because `Sigma_N>=I`:

`alpha > 12.78437096216 => UNSAT whp.`                    (4.2)

For `epsilon=0`, (4.1) recovers the old low-rank identity-subspace lower transfer. For every `epsilon>0`, however, (4.1) applies to full-rank bulk inflation not covered by that theorem.

### Vanishing spectral-window universality

Now let

`r_N=o(N)`,

`epsilon_N->0`,

`lambda_1(Sigma_N)>=1`,

`lambda_{N-r_N}(Sigma_N)<=1+epsilon_N`.

Then the current rigorous isotropic T03 bracket transfers with **no asymptotic loss**:

`6.30297437506 <= alpha_c^{Sigma} <= 12.78437096216`,       (4.3)

in the standard one-sided threshold sense supplied by the two rigorous parent implications.

The lower proof does not assume a triangular version of MZZ. Fix any

`alpha < 1/Phi(-1)`.

By continuity of `1/Phi(kappa)`, choose a fixed `eta>0` such that

`alpha < 1/Phi(-1+eta)`.

For all sufficiently large `N`,

`-1/sqrt(1+epsilon_N) < -1+eta`

and

`M/(N-r_N) < 1/Phi(-1+eta)`.

MZZ therefore gives an isotropic witness in dimension `N-r_N` at the **harder fixed margin** `-1+eta` whp. That same witness is feasible at the easier margin `-1/sqrt(1+epsilon_N)`, and Theorem NM12-SQ transfers it to the anisotropic model. This proves the lower implication in (4.3) without invoking any unproved uniformity in a varying margin.

The upper implication follows directly from the pathwise event inclusion

`SAT(G Sigma_N^{1/2},-1) subset SAT(G,-1)`

because `Sigma_N>=I`.

## 5. Explicit comparison-rate penalty

The lower comparison itself has an exact quantitative density benchmark

`A_L(rho,epsilon)`

`= (1-rho)/Phi(-1/sqrt(1+epsilon))`.                        (5.1)

At `(rho,epsilon)=(0,0)`,

`L := 1/Phi(-1) = 6.302974375068753...`.

A direct Taylor expansion gives

`A_L(rho,epsilon)`

`= L - L rho - C_epsilon epsilon + O(rho epsilon + epsilon^2)`,

where

`C_epsilon = phi(1)/(2 Phi(-1)^2)`

`          = 4.806444282078035...`.                         (5.2)

Thus the new theorem quantifies the first-order cost of the two genuinely different defects:

- deleting an `rho` fraction of uncontrolled high-eigenvalue directions costs `L rho`;
- inflating the controlled spectral bulk by `epsilon` costs `4.80644... epsilon` to first order.

This is a comparison/certificate rate, not a claimed finite-`N` convergence rate for the unknown exact T03 threshold.

For example, with no discarded directions and fixed `epsilon=0.10`, (4.1) gives the rigorous LP-based anisotropic SAT lower endpoint

`1/Phi(-1/sqrt(1.1)) = 5.876204661581636...`.

## 6. Concrete unresolved application — full-rank covariance with unbounded spikes

Define

`r_N=floor(N^(3/4))`,

`d_N=N-r_N`,

`epsilon_N=N^(-1/3)`.

Let `Sigma_N` be diagonal in a deterministic orthonormal basis with

`lambda_{j,N}=1 + epsilon_N * j/(d_N+1)`,  `1<=j<=d_N`,

and

`lambda_{j,N}=exp(N^(1/10))`,  `d_N<j<=N`.

Then:

1. `lambda_1>1`, so `Sigma_N>=I`;
2. `lambda_{d_N}<1+epsilon_N`;
3. `r_N/N=N^(-1/4)+o(1)->0`;
4. `epsilon_N->0`;
5. **every eigenvalue differs from `1`**, so
   `rank(Sigma_N-I)=N`;
6. `||Sigma_N||_op=exp(N^(1/10))->infinity`.

Therefore neither the old low-rank PSD theorem nor the signed identity-subspace theorem applies: there is no nontrivial exact identity subspace at all.

Theorem NM12-SQ nevertheless proves for the Gaussian negative spherical perceptron with iid rows `N(0,Sigma_N)` that

`6.30297437506 <= alpha_c^{full-rank} <= 12.78437096216`     (6.1)

in the same rigorous one-sided sense as the current isotropic T03 bracket.

This is a strict **dimension-regime extension**: the covariance perturbation rank jumps from `o(N)` in the predecessor theorem to the maximal value `N`, while the operator norm may diverge without bound.

The executed checker evaluates the comparison benchmark for this model. At representative sizes it gives

`N=10^6:  A_L ~= 6.057692640760322`,

`N=10^9:  A_L ~= 6.262756756508267`,

`N=10^12: A_L ~= 6.296191297526177`,

with convergence to `6.302974375068753...` as predicted by (5.2). These are deterministic comparison benchmarks, not empirical threshold estimates.

## 7. Exact difference from posted / predecessor results

This theorem is **not**:

- P12's posted row-submatrix least-singular-value universality theorem;
- the posted mesoscopic-spike random-matrix theorem;
- any neural-kernel or ReLU theorem;
- the posted zero-margin / Ising perceptron result;
- my earlier radial row-rescaling comparison;
- my earlier low-rank covariance identity-subspace theorem.

The new statement concerns exact-radius **negative spherical feasibility** under deterministic full-rank covariance deformation. Its new hypothesis is a high-dimensional spectral quantile rather than low rank or exact identity on a large subspace.

### Transferred hypotheses checked explicitly

For the lower T03 application:

- after choosing the deterministic spectral subspace `E_N`, `GQ_N` is exactly iid standard Gaussian by rotational invariance;
- the witness lives on the exact unit sphere in dimension `d_N`;
- the comparison margin is fixed in the rigorous corollary (or dominated by a fixed harder margin in the vanishing-window corollary);
- `M/d_N` has the required proportional limit;
- no density, finite-convolution, fourth-moment, radial-independence, or approximate-sphere assumption is inserted.

For the upper T03 application:

- `Sigma_N>=I` is exactly verified;
- the pathwise normalization preserves an exact unit-sphere witness;
- the target margin remains exactly `-1`;
- the existing isotropic Gaussian T03 upper theorem is invoked without changing its disorder law or radius.

## 8. Literature boundary checked this run

Bounded search dated 2026-09-20 used variants of

- `negative spherical perceptron anisotropic covariance Gaussian`;
- `spherical perceptron correlated patterns covariance rigorous`;
- `perceptron covariance matrix anisotropic Gaussian threshold rigorous`.

The search recovered older work on correlated Gaussian patterns and Gerace--Krzakala--Loureiro--Stephan--Zdeborova's Gaussian-universality work for perceptrons with random labels / training loss. Those settings differ from the exact negative spherical feasibility event here. It also recovered the standard negative-spherical sources (El Alaoui--Sellke and Stojnic). I did not find, in this bounded search, a primary theorem matching the finite-N spectral-quantile sandwich (3.1). This is bounded negative evidence only, not a novelty certificate.

## 9. Applied parent claim: before / after separated from theory gain

### Original isotropic T03 parent

Certified before:

`[6.30297437506, 12.78437096216]`,

width `6.48139658710`.

Certified after:

`[6.30297437506, 12.78437096216]`,

width `6.48139658710`.

**No isotropic source-bracket movement is claimed.** The `12.75` companion endpoint remains review-pending until the directed integral enclosure is actually completed.

### Demonstrated theory gain

Before this run, the magnitude-free two-sided covariance transfer required `rank(Sigma-I)=o(N)` and an exact identity complement.

After this run, a finite-N spectral-quantile theorem handles covariance matrices with

`rank(Sigma-I)=N`,

an `N-o(N)` bulk in `[1,1+o(1)]`,

and `o(N)` arbitrarily large positive eigenvalue outliers, with an exact probability sandwich and explicit first-order comparison penalty. The concrete full-rank model in Section 6 inherits the full current T03 bracket despite `||Sigma_N||_op->infinity`.

This is the substantive movement of this invocation.

## 10. Essential executed artifact

Checker:

`proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/t03_spectral_quantile_fullrank_check.py`

Archived actual output:

`proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/t03_spectral_quantile_fullrank_check.out`

The output ends `ALL_CHECKS_PASS` and verifies the numerical constants, the first-order coefficient, the explicit full-rank model parameters, and convergence of the deterministic comparison benchmark.

The theorem itself is proved on the page and does not depend on floating-point computation.

## 11. Residual obstruction and next nonduplicating attack

The proved theorem requires `Sigma_N>=I` for the exact same-margin upper transfer. The previous signed-contraction report showed that dropping any lower spectral control is impossible: a tiny near-null sector can create feasible axis witnesses far beyond the isotropic UNSAT endpoint.

The next genuinely open universality boundary is therefore narrower and source-relevant:

> allow a full-rank signed bulk with `lambda_min(Sigma_N)=1-o(1)` and all but `o(N)` eigenvalues in `1+o(1)`, and quantify enough local `kappa`-robustness of the isotropic UNSAT certificate to transfer the upper endpoint without assuming `Sigma_N>=I` exactly.

That route should consume the companions' eventual directed `alpha=12.75` certificate, if completed, rather than duplicate their stationarity work.

No peer file, historical report, shared root ledger, schedule, permission, workflow, public surface, email, Drive resource, or paid-compute resource was modified.

```yaml
ledger_delta:
  worker: NM13-12
  parent: T03
  target: "quantitative universality / anisotropic negative spherical Gaussian perceptron"
  status: "PARTIAL / NEW FINITE-N SPECTRAL-QUANTILE THEOREM / FULL-RANK REGIME GAIN"
  p12_latest_report: "proofnet24/P12-smooth-iid/runs/2026-09-17/2026-09-17T18-20-03Z__run-report.md"
  p12_exact_scope:
    entries: "iid centered variance-one with densities f_m"
    smoothing: "fixed q,M with sup_m ||f_m^{*q}||_infinity <= M"
    aspect: "N_m/m -> gamma>1"
    surplus: "k_m=r_m+1; k_m log m=o(m)"
    fourth_moment: "not assumed"
    unresolved_successor: "triangular smooth/B4 universality without uniform microscopic finite-convolution smoothing"
  source_metric:
    quantity: "rigorous isotropic T03 threshold bracket"
    before: "[6.30297437506, 12.78437096216]"
    after: "[6.30297437506, 12.78437096216]"
    movement: "none"
  theory_gain:
    theorem: "NM12-SQ"
    finite_N: "p_iso(M,d,kappa/sqrt(u)) <= p_Sigma <= p_iso(M,N,kappa/sqrt(ell))"
    previous_regime: "low-rank covariance perturbation with exact identity complement"
    new_regime: "rank(Sigma-I)=N allowed; N-o(N) spectral bulk within 1+o(1); o(N) arbitrarily large positive outliers"
    explicit_rate: "A_L(rho,epsilon)=(1-rho)/Phi(-1/sqrt(1+epsilon)); first-order epsilon coefficient 4.806444282078035"
  concrete_application:
    covariance: "full-rank bulk ramp 1+N^(-1/3) j/(d+1), r=N^(3/4) spikes exp(N^(1/10))"
    rank_Sigma_minus_I: "N"
    operator_norm: "diverges"
    inherited_bracket: "[6.30297437506, 12.78437096216]"
  coordination:
    NM13-03: "closed-kernel/Miranda 12.75 candidate acknowledged; not duplicated"
    NM13-07: "moment-Jacobian/contraction compiler acknowledged; not duplicated"
    transfer: "any future certified isotropic upper endpoint transfers immediately under Sigma>=I"
  artifacts:
    checker: "proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/t03_spectral_quantile_fullrank_check.py"
    output: "proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/t03_spectral_quantile_fullrank_check.out"
    output_status: "ALL_CHECKS_PASS"
  next_attack: "signed full-rank 1-o(1) spectral floor via quantitative kappa-robust upper transfer"
  runtime:
    model: "GPT-5.6 Sol"
    reasoning: "UNVERIFIED"
```
