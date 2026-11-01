Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 / maximum was requested, but no authenticated applied-model / reasoning-effort receipt is exposed, so I do not claim otherwise.

# NM13-12 progress-universality — signed low-rank covariance universality boundary and a sharp contraction critical window for T03

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-12`  
Progress root: `proofnet24/NM13-12/progress-universality/`  
Owner policy: `operations/PROGRESS20_2026-09-20.md`  
Parent: T03 negative spherical perceptron at `kappa=-1`  
Status: **PARTIAL / NEW THEOREMS PROVED / STRICT DISTRIBUTIONAL-CLASS GAIN / STRICT NONUNIVERSALITY SEPARATION / ORIGINAL T03 BRACKET UNCHANGED**

## 1. Compact continuity handoff: exact P12 state and what this run does differently

The latest retained P12 proof state is still

`proofnet24/P12-smooth-iid/runs/2026-09-17/2026-09-17T07-17-16Z__run-report.md`.

Its frozen theorem is source-exact as follows. For `F in {R,C}`, with `d_R=1` and `d_C=2`, let `A_m` have iid centered variance-one entries with density `f_m`. Assume one fixed integer `q>=1` and one fixed constant `M<infinity` such that

`sup_m ||f_m^{*q}||_infinity <= M`,

and assume

`N_m/m -> gamma>1`,

`k_m=r_m+1`,

`k_m log m=o(m)`.

Then the frozen package proves

`(k_m/m) log M^F_{m,r_m}(A_m) ->_P -h(gamma)/d_F`.

There is **no fourth-moment assumption** and no positive-moment assumption above variance normalization. The explicitly unresolved mathematical successor is triangular smooth / bounded-fourth-moment universality **without** a uniform microscopic finite-convolution smoothing condition. P12's own remaining obligations are audit/final-package gates, not a missing author-side theorem.

The root `POSTED.md` excludes rediscovery/repackaging of the posted row-submatrix papers, mesoscopic-spike paper, neural-kernel results, ReLU work, and zero-margin/Ising perceptron capacity. This report proves none of those again.

The three preceding NM13-12 progress-universality reports developed, in order:

1. all-row radial hard-margin comparison;
2. defect-tolerant/quantile radial comparison;
3. two-sided low-rank **PSD covariance-spike** comparison.

The third theorem showed, for `Sigma=I+B` with `B>=0` of rank `r`,

`p_iso(M,N-r,kappa) <= p_Sigma(M,N,kappa) <= p_iso(M,N,kappa)`

for `kappa<0`, with no dependence on spike magnitude.

This run does **not** make another radial or PSD-spike variant. It attacks the first missing case identified by that theorem: **signed low-rank covariance deformation, especially covariance contractions.** The result is two-sided in information but deliberately asymmetric in universality:

- the SAT/lower-threshold transfer extends from PSD spikes to **all signed low-rank deformations** that remain positive definite;
- the UNSAT/upper-threshold transfer cannot extend in that generality, and this run proves a sharp logarithmic spectral/rank mechanism showing why.

That is the strict assumption/distributional-class improvement.

## 2. Exact T03 parent and current companion state

Freeze the original source model:

- `M=floor(alpha N)`;
- independent `g_a ~ N(0,I_N)`;
- seek `sigma` with `||sigma||_2=sqrt(N)` exactly;
- `<g_a,sigma> >= -sqrt(N)` for every `a<=M`;
- fixed `alpha` and `N->infinity`.

Equivalently, with `x=sigma/sqrt(N)`, seek `x in S^{N-1}` such that

`Gx >= -1`.

The rigorous repository bracket entering this run is

`alpha_L = 6.30297437506`,

`alpha_U = 12.78437096216`,

`W = 6.48139658710`.

NM13-03 has reduced the complete second-lift kernel to direct one-dimensional Gaussian formulas and found a robust numerical Poincare--Miranda candidate at `alpha=12.75`, but correctly leaves the endpoint review-pending until a directed continuum enclosure is supplied. NM13-07 has subsequently closed the full first Jacobian algebraically with a tilted-moment tower `J_0,...,J_4` and proved a broad deterministic contraction compiler, but likewise does not promote `12.75` without rigorous interval quadrature.

This run is complementary: it does not touch their stationarity equations, numerical root, or interval-certification obligation.

## 3. Signed identity-complement theorem: lower universality survives arbitrary low-rank sign

For an `M x N` matrix `A` and `kappa<0`, write

`SAT(A,kappa) := { exists x in S^{N-1}: Ax >= kappa 1_M }`.

Let `G` be an iid standard Gaussian `M x N` matrix. For a deterministic positive-definite covariance `Sigma`, the anisotropic Gaussian constraint matrix is

`A=G Sigma^{1/2}`.

### Theorem NM12-SIGNED-1 (identity-subspace lower transfer)

Suppose `Sigma` acts as the identity on a deterministic subspace `E` of dimension `d`. Then for every finite `M,N` and every real `kappa`,

`P{SAT(G Sigma^{1/2},kappa)} >= p_iso(M,d,kappa)`,

where `p_iso(M,d,kappa)` is the SAT probability of an iid standard Gaussian `M x d` matrix at the same spherical margin.

In particular, if

`Sigma=I+B`,

`Sigma>0`,

and `B` is an **arbitrary symmetric matrix of rank r** (positive, negative, or indefinite), then

`P{SAT(G Sigma^{1/2},kappa)} >= p_iso(M,N-r,kappa)`.

#### Proof

Let `Q` be an `N x d` matrix with orthonormal columns spanning `E`. Since `Sigma|_E=I`, functional calculus gives

`Sigma^{1/2} Q=Q`.

If `z in S^{d-1}` satisfies

`(GQ)z >= kappa`,

then `x=Qz in S^{N-1}` and

`G Sigma^{1/2}x = G Sigma^{1/2}Qz = GQz >= kappa`.

Hence pathwise

`SAT(GQ,kappa) subset SAT(G Sigma^{1/2},kappa)`.

By rotational invariance, `GQ` is an iid standard Gaussian `M x d` matrix. Taking probabilities proves the first statement.

For `Sigma=I+B`, `ker B` has dimension at least `N-r` and `Sigma` equals the identity on that kernel. Restrict to any `(N-r)`-dimensional subspace of `ker B`. QED.

### Corollary NM12-SIGNED-LOWER

If `rank(B_N)=o(N)` and `I+B_N>0`, then every rigorous isotropic Gaussian SAT lower threshold at fixed `kappa` transfers with no asymptotic loss to `N(0,I+B_N)` rows, **without any sign or operator-norm restriction on `B_N`**.

At `kappa=-1`, the current T03 lower endpoint therefore yields

`alpha < 6.30297437506  =>  SAT whp`

for every positive-definite signed low-rank deformation `I+B_N` with `rank(B_N)=o(N)`.

This is a strict extension of the predecessor PSD-spike theorem on the lower side. The next sections show that a corresponding same-margin upper transfer is false.

## 4. Exact finite-N contracted-eigenvector law

Let `v_1,...,v_r` be orthonormal eigenvectors of `Sigma` with eigenvalues `lambda_1,...,lambda_r>0`. Define `E_j` to be the event that the single spherical vector `x=v_j` satisfies every negative-margin constraint at `kappa=-1`.

### Theorem NM12-AXIS-EXACT

For `M` iid rows `h_a~N(0,Sigma)`,

`P(E_j) = Phi(1/sqrt(lambda_j))^M`.

Moreover the events `E_1,...,E_r` are mutually independent. Consequently

`P{ at least one v_j is feasible }`

`= 1 - product_{j=1}^r [1-Phi(1/sqrt(lambda_j))^M]`.

In particular,

`P{SAT} >= 1 - product_{j=1}^r [1-Phi(1/sqrt(lambda_j))^M]`.

For equal eigenvalues `lambda_j=lambda`, this becomes the exact lower bound

`P{SAT} >= 1 - (1-Phi(1/sqrt(lambda))^M)^r`.

#### Proof

For each row `a` and eigenvector `v_j`, write

`<h_a,v_j> = sqrt(lambda_j) Z_{a,j}`,

where the family `{Z_{a,j}: 1<=a<=M, 1<=j<=r}` is iid standard normal: within a row this follows because the covariance is diagonal in the orthonormal eigenbasis, and rows are independent.

The vector `v_j` is feasible exactly when

`sqrt(lambda_j) Z_{a,j} >= -1`

for every `a`, equivalently

`Z_{a,j} >= -1/sqrt(lambda_j)`

for every `a`. The single-row success probability is `Phi(1/sqrt(lambda_j))`, so independence across rows gives the first formula. Since `E_j` depends only on the coordinate column `{Z_{a,j}:a<=M}`, the `E_j` are independent across `j`. QED.

### Spectral witness criterion

Let

`p_{j,N}=Phi(1/sqrt(lambda_{j,N}))^{M_N}`

and

`S_N=sum_j p_{j,N}`.

Then the exact product formula implies

- if `S_N -> infinity`, then `P{SAT}->1` because `P(no axis witness)<=exp(-S_N)`;
- if `S_N -> 0`, then `P{some axis witness}<=S_N->0`.

The second statement is only the disappearance of this explicit witness mechanism, not an UNSAT theorem for the full model.

This is the quantitative spectral quantity missing from a rank-only universality statement.

## 5. Fixed-rank logarithmic critical window

The exact finite-N law has a sharp asymptotic window already for one contracted eigenvector.

Let `r` be fixed, `M_N=floor(alpha N)`, and suppose all `r` selected contracted eigenvalues are equal to `lambda_N`. Put

`t_N=1/sqrt(lambda_N)`.

### Theorem NM12-AXIS-FIXED-R

If

`t_N^2 = 2 log N - log log N + c + o(1)`,

then

`N * barPhi(t_N) -> exp(-c/2)/sqrt(4 pi)`

and hence

`p_N := Phi(t_N)^{M_N}`

`-> exp[-alpha exp(-c/2)/sqrt(4 pi)]`.

Therefore

`P{at least one of the r eigenvectors is feasible}`

`-> 1 - [1-exp(-alpha exp(-c/2)/sqrt(4 pi))]^r`.

#### Proof

Mills' ratio gives

`barPhi(t) = phi(t)/t * (1+o(1))`

as `t->infinity`. Here

`exp(-t_N^2/2)`

`= N^{-1} (log N)^{1/2} exp(-c/2+o(1))`,

while `t_N=sqrt(2 log N)(1+o(1))`. Thus

`barPhi(t_N)`

`= N^{-1} exp(-c/2)/sqrt(4 pi) * (1+o(1))`.

Write `q_N=barPhi(t_N)`. Since `q_N=O(1/N)`,

`M_N log(1-q_N) = -M_N q_N + O(M_N q_N^2)`

and `M_N q_N^2=O(1/N)->0`. Therefore

`Phi(t_N)^{M_N} -> exp[-alpha exp(-c/2)/sqrt(4 pi)]`.

Insert this in the exact product formula. QED.

### Rank-one destruction of every finite linear-load UNSAT threshold

A more severe contraction makes even one fixed direction feasible with probability tending to one. For example, let

`lambda_N = 1/(3 log N)`.

Then `t_N=sqrt(3 log N)`, and Mills' ratio gives

`barPhi(t_N)=N^{-3/2+o(1)}`.

For every fixed `alpha<infinity`,

`M_N barPhi(t_N)=N^{-1/2+o(1)}->0`,

so

`Phi(t_N)^{M_N}->1`.

Thus a rank-one covariance contraction can make the negative spherical perceptron SAT whp at **every fixed linear constraint density**. This proves that `rank(B_N)=o(N)` by itself can never imply two-sided threshold universality for signed perturbations.

## 6. Polynomial-rank critical surface

The more informative regime balances the rarity of one feasible contracted axis against a polynomial number of contracted axes.

Fix `0<beta<1`, let

`r_N=N^{beta+o(1)}`,

and suppose these `r_N` eigenvalues are equal to `lambda_N`. Put again `t_N=1/sqrt(lambda_N)`.

### Theorem NM12-AXIS-POLY

If

`t_N^2 = 2 log N - 3 log log N + c + o(1)`,

then

`barPhi(t_N)`

`= [exp(-c/2)/sqrt(4 pi)] * (log N)/N * (1+o(1))`.

For `M_N=floor(alpha N)`, define

`a(alpha,c) = alpha exp(-c/2)/sqrt(4 pi)`.

Then one contracted eigenvector is feasible with probability

`p_N = N^{-a(alpha,c)+o(1)}`.

Consequently:

- if `a(alpha,c)<beta`, then the anisotropic perceptron is SAT whp, witnessed by one of the contracted eigenvectors;
- if `a(alpha,c)>beta`, then the probability of any such contracted-axis witness tends to zero.

The exact asymptotic load threshold for this explicit witness mechanism is therefore

`boxed: alpha_axis(beta,c) = beta sqrt(4 pi) exp(c/2)`.

#### Proof

Again use Mills' ratio. The assumed scale gives

`exp(-t_N^2/2)`

`= N^{-1} (log N)^{3/2} exp(-c/2+o(1))`.

Dividing by `t_N sqrt(2 pi)` with `t_N=sqrt(2 log N)(1+o(1))` yields the displayed tail asymptotic.

Thus

`M_N barPhi(t_N)=a(alpha,c) log N + o(log N)`.

Since `barPhi(t_N)=O((log N)/N)`, the quadratic term in

`M_N log(1-barPhi(t_N))`

is `O((log N)^2/N)=o(1)`. Hence

`p_N=Phi(t_N)^{M_N}=N^{-a(alpha,c)+o(1)}`.

By independence,

`P(no axis witness)=(1-p_N)^{r_N}`.

If `a<beta`, then `r_N p_N=N^{beta-a+o(1)}->infinity`, so the no-witness probability is at most `exp(-r_N p_N)->0`. If `a>beta`, the union bound gives `P(any axis witness)<=r_Np_N->0`. QED.

This theorem identifies a sharp **rank--spectral logarithmic critical surface**. The predecessor PSD-spike theorem had no analogue because positive spikes make negative-margin constraints harder rather than creating these near-null easy directions.

## 7. Concrete T03 application: same-alpha rigorous separation

Take a deterministic orthogonal projection `P_N` of rank

`r_N=floor(N^(1/4))`.

Define the contracted covariance

`Sigma_N = I_N - (1-lambda_N) P_N`,

where

`lambda_N = 1 / [2 log N - 3 log log N + 6]`

for all sufficiently large `N` (and define any positive value for finitely many smaller `N`). Then `Sigma_N>0`,

`rank(Sigma_N-I_N)=floor(N^(1/4))=o(N)`,

but its smallest eigenvalue tends to zero.

This model is not covered by the predecessor PSD-spike theorem: `Sigma_N-I_N` is negative semidefinite on the exceptional subspace. It is also not a row-radial model with independent uniform spherical directions; its Gaussian angular law is anisotropic and radius/direction are dependent.

Apply NM12-AXIS-POLY with

`beta=1/4`, `c=6`.

The explicit axis-witness threshold is

`alpha_axis = (1/4) sqrt(4 pi) exp(3)`

`= 17.800343633504454...`.

Therefore:

`alpha < 17.800343633504454  =>  SAT whp`

for this anisotropic contracted Gaussian perceptron.

This is a new rigorous lower threshold for a concrete unresolved anisotropic negative spherical perceptron.

More sharply, take the **same density**

`alpha=12.9`.

For the ordinary isotropic Gaussian T03 model, the existing rigorous upper endpoint gives

`12.9 > 12.78437096216`,

so the model is UNSAT whp.

For the contracted model above,

`a(12.9,6) = 0.18117627762701097... < 1/4`,

so NM12-AXIS-POLY proves SAT whp.

Thus at exactly the same negative margin, exact sphere radius, and linear constraint density,

`isotropic Gaussian: UNSAT whp`,

while

`rank-N^(1/4) contracted Gaussian: SAT whp`.

The proved load separation is not merely epsilon-sized:

`alpha_axis - alpha_U^iso`

`= 17.800343633504454 - 12.78437096216`

`= 5.0159726713444535...`.

The exact SAT/UNSAT threshold of the contracted model is still **UNKNOWN**; unknown is not relabeled as zero or as `alpha_axis`. What is proved is the SAT lower threshold and the same-alpha nonuniversality separation.

## 8. Relation to P12 universality and the exact gain

The frozen P12 row-submatrix theorem uses a uniform microscopic finite-convolution regularity hypothesis to suppress local concentration/resonance. The present T03 calculation exposes an analogous, but geometric, reason that a naive covariance universality statement is false: a low-dimensional near-null covariance sector produces exponentially cheap negative-margin directions, and a polynomial number of such directions amplifies them through an extreme-value transition.

The gain relative to the immediately preceding NM13-12 theorem is exact:

**Before:** two-sided T03 bracket transfer was proved for `Sigma_N=I+B_N` with `B_N>=0`, `rank(B_N)=o(N)`, with arbitrary positive spike magnitude.

**After:**

1. the **SAT/lower** transfer holds for arbitrary signed symmetric `B_N` with `I+B_N>0` and `rank(B_N)=o(N)`, with no operator-norm bound;
2. a complete finite-N product law quantifies the obstruction to the missing upper transfer;
3. the fixed-rank and polynomial-rank logarithmic critical windows are proved;
4. a concrete rank-`N^(1/4)` contraction is proved SAT whp all the way to load `17.8003...`, yielding a rigorous same-alpha separation from isotropic T03 at `alpha=12.9`.

This is a strict distributional-class/assumption extension plus a sharp boundary theorem, not a repackaging of the posted row-submatrix, kernel, ReLU, zero-margin Ising, or mesoscopic-spike results.

## 9. Parent T03 before/after versus demonstrated theory movement

### Original isotropic T03 source metric

Certified before:

`[6.30297437506, 12.78437096216]`, width `6.48139658710`.

Certified after:

`[6.30297437506, 12.78437096216]`, width `6.48139658710`.

**Movement: none.**

I do not count an anisotropic extension as movement of the original iid-standard-Gaussian source bracket, and I do not promote the companions' review-pending `12.75` endpoint.

### Demonstrated theory/application movement

New proved results:

- signed low-rank identity-complement SAT transfer;
- exact independent contracted-axis witness law;
- fixed-rank contraction critical window;
- polynomial-rank rank--spectral critical surface;
- concrete anisotropic T03 SAT lower threshold `17.800343633504454...`;
- same-alpha `12.9` separation: anisotropic SAT whp versus isotropic UNSAT whp.

This is source-connected progress even though the original isotropic bracket is unchanged.

## 10. Literature/status scope

The standard T03 source literature remains about isotropic Gaussian disorder. El Alaoui--Sellke formulate the exact standard-Gaussian spherical model; for negative margin their algorithmic construction is tied to the conjectural FRSB/Parisi description and does not supply the exact full-radius threshold. Stojnic's fully lifted RDT gives a framework and numerical capacity calculations but explicitly requires substantial numerical work for concrete values; NM13-03/NM13-07 are attacking the resulting certification problem rather than assuming those numerics are a final theorem.

A bounded current search also recovered older literature on perceptrons with correlated Gaussian patterns, including replica/statistical-physics storage-capacity calculations. I did **not** locate in that bounded search a rigorous finite-N theorem matching the exact contracted-eigenvector product law and the rank--spectral critical surface above for the negative spherical feasibility problem. This is bounded negative evidence only, not a priority or novelty certificate.

## 11. Essential executed artifact

Checker:

`proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/t03_signed_contraction_axis_certificate.py`

creation commit:

`f4e45b4f5c51fe5c5aa51070edf79411d1454ffe`.

Archived actual output:

`proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/t03_signed_contraction_axis_certificate.out`

creation commit:

`b2f95a202c4a625102e18b705b749e50ca21de75`.

The checker uses the exact finite-N product law; it does not simulate the perceptron. It records

`alpha_axis(1/4,6)=17.800343633504454`,

`alpha_axis-alpha_U^iso=5.0159726713444535`,

and at `alpha=12.9` the exponent

`a=0.18117627762701097 < 1/4`.

It also evaluates finite-`N` convergence and a rank-one `lambda_N=1/(3 log N)` example. Output ends

`ALL_CHECKS_PASS`.

These computations are sanity checks of the proved formulas; the asymptotic arguments themselves are written above.

## 12. Residual obstruction and next nonduplicating attack

The new theorem identifies the exact failure mode of rank-only two-sided universality: covariance eigenvalues approaching zero at logarithmic scale create explicit easy axes.

The next useful universality question is therefore no longer “signed versus PSD?” in the abstract. It is quantitative:

**Can one recover two-sided threshold stability for signed rank-`o(N)` covariance deformations under a genuine lower spectral floor, for example `lambda_min(Sigma_N)>=c>0`, without paying the crude constant-margin loss of the deterministic condition-number sandwich?**

The axis mechanism proved here disappears exponentially when `lambda_min` is bounded below, but that alone does not prove full isotropic threshold universality. A successful route would need a comparison/interpolation bound that uses the fact that only `o(N)` directions are deformed, rather than the worst eigenvalue. That is a distinct next theorem and does not duplicate NM13-03/NM13-07's second-full isotropic certification.

No shared root ledger, peer file, historical report, schedule, permission, workflow, public resource, email, or Drive object was modified.

```yaml
ledger_delta:
  worker: NM13-12
  parent: T03
  assignment: quantitative universality / random-matrix theory
  status: "PARTIAL / NEW THEOREMS PROVED / STRICT DISTRIBUTIONAL NONUNIVERSALITY SEPARATION"
  p12_state:
    theorem: "finite-convolution real/complex moderate-surplus row-submatrix universality"
    assumptions: "centered variance one; fixed q,M with sup ||f_m^{*q}||_inf<=M; N_m/m->gamma>1; k_m log m=o(m)"
    fourth_moment_required: false
    unresolved_successor: "triangular smooth/bounded-fourth-moment universality without uniform microscopic finite-convolution smoothing"
  source_metric:
    name: "original isotropic T03 rigorous threshold bracket"
    before:
      alpha_L: "6.30297437506"
      alpha_U: "12.78437096216"
      width: "6.48139658710"
    after:
      alpha_L: "6.30297437506"
      alpha_U: "12.78437096216"
      width: "6.48139658710"
    movement: "NONE"
  theory_gain:
    signed_identity_complement_lower_transfer: "PROVED for arbitrary symmetric rank-o(N) B with I+B>0"
    contracted_axis_exact_finiteN_law: "PROVED"
    fixed_rank_critical_window: "t_N^2=2 log N-log log N+c"
    polynomial_rank_critical_surface: "alpha_axis(beta,c)=beta sqrt(4pi) exp(c/2)"
  application:
    model: "Sigma_N=I-(1-lambda_N)P_N"
    rank: "floor(N^(1/4))"
    lambda_N: "1/(2 log N-3 log log N+6)"
    proved_SAT_load: "alpha < 17.800343633504454"
    exact_threshold: "UNKNOWN"
    same_alpha_separation:
      alpha: "12.9"
      isotropic: "UNSAT whp by certified alpha_U"
      contracted: "SAT whp by axis witness theorem"
  coordination:
    NM13-03: "closed-kernel / Miranda alpha=12.75 route consumed, not duplicated"
    NM13-07: "tilted-moment Jacobian / contraction route consumed, not duplicated"
  artifacts:
    checker: "proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/t03_signed_contraction_axis_certificate.py"
    output: "proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/t03_signed_contraction_axis_certificate.out"
    output_status: "ALL_CHECKS_PASS"
  next_attack: "two-sided stability for signed rank-o(N) covariance deformations with lambda_min bounded below, using low-rank rather than worst-eigenvalue comparison"
  runtime:
    model: "GPT-5.6 Sol"
    reasoning_level: "UNVERIFIED"
```
