Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested but is not authenticated by this runtime.**

# NM13-12 — fourth-moment unbounded-scale near-lattice universality

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-12` / `proofnet24/NM13-12/progress-universality`  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`, current LIVE20 mapping  
Primary applied parent: **P12 unresolved triangular smooth/B4 universality successor**  
T03 coordination: **NM13-03 / NM13-07 read for current boundary only; no lifted-RDT duplication**  
Status: **PARTIAL / NEW AUTHOR-SIDE COMPLETE REAL RANDOM-MATRIX EXTENSION / EXPLICIT UNBOUNDED SCALE-MIXTURE FAMILY SOLVED / INDEPENDENT REVIEW PENDING**

## 0. Compact handoff and exact predecessor boundary

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

There is **no fourth-moment assumption and no positive-moment assumption above variance normalization** in that frozen theorem. Its explicitly unresolved mathematical successor is triangular smooth / bounded-fourth-moment universality without a uniform microscopic finite-convolution ceiling. P12's remaining canonical obligations are independent-audit/final-package gates and are not modified here.

The immediate NM13-12 predecessor,

`2026-09-20T1054Z__p12-random-scale-nearlattice-universality.md`,

proved the real exponent for

`xi_m=(R+sigma_m S_m G)/sqrt(1+sigma_m^2 E S_m^2)`

under the pointwise scale bounds

`0<a_m<=S_m<=b<infinity`

and the effective-floor conditions

`m rho_m^2/log(e/rho_m)->infinity`,

`k_m[log m+log(e/rho_m)]=o(m)`,

where `rho_m=sigma_m a_m/sqrt(1+sigma_m^2 E S_m^2)`.

The upper bound `S_m<=b` was used only to obtain a uniform fourth-order low-frequency expansion and a fixed B4 anti-concentration input. This run removes that pointwise upper support bound entirely.

`POSTED.md` excludes rediscovery/repackaging of the posted bounded-density row-submatrix papers, mesoscopic-spike paper, kernel/ReLU work and zero-margin/Ising results. The claim below is not any of those statements: it treats a triangular iid law whose entry density and every fixed convolution-density ceiling diverge and whose Gaussian smoothing amplitude has **unbounded support**. The exact difference from the immediate predecessor is `S_m<=b` -> `sup_m E S_m^4<infinity`.

## 1. Current T03 coordination, preserved rather than duplicated

The newest relevant T03 companion state on current `master` is:

- `NM13-07`, `2026-09-20__t03-matched-gaussian-recenter-alpha1231963446.md`, gives the current review-pending exact-sphere Gaussian upper endpoint `alpha_U=12.31963446`.
- `NM13-03`, `2026-09-20__t03-variance-deficit-cage-alpha122872222217.md`, gives the stronger complete-third supported point `alpha=12.2872222217`, still **CONDITIONAL** because its outward four-overlap inclusion is incomplete.

Thus the original iid-Gaussian T03 parent is not changed in this run. The current project-supported bracket used here is

`[6.30297437506, 12.31963446]`.

No stationarity, Krawczyk, entropy/Fisher cage, curvature-overlap, or complete-third computation is duplicated below.

## 2. New theorem: lower scale floor plus fourth moment, no upper support

For each `m`, let

- `R` be Rademacher;
- `G~N(0,1)`;
- `S_m` be independent of `(R,G)`, with
  `S_m>=a_m>0` almost surely;
- `sup_m E S_m^4 <= B < infinity`;
- `0<sigma_m<=1`.

Write

`mu_{2,m}=E S_m^2`,

`D_m=sqrt(1+sigma_m^2 mu_{2,m})`,

`rho_m=sigma_m a_m/D_m`,

and define

`xi_m=(R+sigma_m S_m G)/D_m`.                               (2.1)

Let `A_m` have iid real entries distributed as `xi_m`.

### Theorem NM12-P12-UNBOUNDED-SCALE

Assume

`N_m/m -> gamma>1`, `k_m=r_m+1`,

`(US1)  m rho_m^2/log(e/rho_m) -> infinity`,                 (2.2)

and

`(US2)  k_m[log m+log(e/rho_m)] = o(m)`.                    (2.3)

Then

`boxed:`

`(k_m/m) log M^R_{m,r_m}(A_m) ->_P -h(gamma)`.              (2.4)

No deterministic upper bound on `S_m` is assumed.

The proof is by re-establishing, under only the fourth-moment bound, every probabilistic input used by the predecessor's deterministic geometric package: a fixed scalar anti-concentration gap, a density-level local limit on useful spread directions, one- and two-plane upper slabs with the correct projective-angle singularity, and the `k`-dimensional projected small-ball estimate. The only scale penalty remains logarithmic in `1/rho_m`, so (US2) absorbs it exactly as before.

## 3. Distributional facts and uniform fourth moment

Centering and variance are exact:

`E xi_m=0`, `E xi_m^2=1`.                                    (3.1)

Since `E S_m^2 <= sqrt(B)`,

`D_m^2 <= 1+sqrt(B)`.                                        (3.2)

Moreover

`E xi_m^4`
` = [1+6 sigma_m^2 mu_{2,m}+3 sigma_m^4 E S_m^4]/D_m^4`
` <= 1+6 sqrt(B)+3B`.                                        (3.3)

Hence the entry family is uniformly B4. It need not be uniformly subgaussian, and the scale distribution may have arbitrarily long support.

Because `S_m>=a_m`, conditional on `(R,S_m)` each entry is Gaussian with variance at least `rho_m^2`. Therefore each fixed-`m` entry law has a positive `C^infinity` density. Differentiation under the mixture is justified because every conditional Gaussian variance is bounded below by `rho_m^2`; for every derivative order `j`, the conditional derivative sup norm is bounded by `C_j rho_m^{-j-1}`.

The fourth-moment concentration lemma proved in the predecessor remains applicable: if centered `X` has `E X^2=1` and `E X^4<=B_X`, then

`Q_X(1/2) <= sqrt(1-1/(2B_X+6)) < 1`.                        (3.4)

With `B_X=1+6sqrt(B)+3B`, this gives the fixed scalar anti-concentration gap needed by the inherited random-rounding / sparse-kernel geometry.

## 4. Every fixed finite-convolution ceiling diverges when sigma_m -> 0

This verifies that the theorem is genuinely outside frozen P12.

Fix `q>=1`. Let

`L=(2B)^(1/4)`.

By Markov,

`P{S_m<=L} >= 1/2`.                                          (4.1)

Consider the component of the `q`-fold convolution on which every Rademacher variable equals `+1` and every scale is at most `L`. This event has probability at least `4^{-q}`. Conditional on the scales, the sum has common mean `q/D_m` and variance at most

`q sigma_m^2 L^2/D_m^2`.

At the common center its conditional density is therefore at least

`D_m/[sigma_m L sqrt(2 pi q)]`.

All other mixture components are nonnegative, so

`boxed:`

`||f_m^{*q}||_infty`
` >= 4^{-q} D_m/[sigma_m L sqrt(2 pi q)]`
` >= 4^{-q}/[sigma_m (2B)^(1/4) sqrt(2 pi q)].`              (4.2)

Thus for every fixed `q`,

`||f_m^{*q}||_infty -> infinity`                             (4.3)

whenever `sigma_m->0`.

## 5. New analytic core: local-density theorem without bounded scales

Fix `v0>0` and `C0<infinity`. Let deterministic coefficients satisfy

`v=sum_j c_j^2 in [v0,1]`,

`max_j |c_j| <= C0/sqrt(m)`.                                 (5.1)

Let

`Y_m=sum_j c_j xi_{m,j}`

and let `p_m` be its density. Let `phi_v` denote the centered Gaussian density of variance `v`.

### Lemma 5.1 — B4 random-scale local limit

There exist `c,C>0`, depending only on `(v0,C0,B)`, such that

`boxed:`

`||p_m-phi_v||_infty`
` <= C/m + C rho_m^{-1} exp(-c m rho_m^2).`                  (5.2)

Consequently (US1) implies uniform local density lower bounds on every fixed compact interval.

### Proof

Put

`psi_m(z)=E exp(-S_m^2 z^2/2)`.

Then

`hat p_m(t)=prod_j cos(c_j t/D_m)`
`                 psi_m(sigma_m c_j t/D_m)`.                 (5.3)

The only place the predecessor used `S_m<=b` was the Taylor remainder for `psi_m`. The fourth moment gives a truncation-free replacement. For `x>=0`,

`0 <= exp(-x)-1+x <= x^2/2`.                                 (5.4)

Taking `x=S_m^2 z^2/2` gives

`psi_m(z)=1-mu_{2,m}z^2/2+R_m(z)`,
`|R_m(z)| <= B z^4/8`.                                       (5.5)

Because `mu_{2,m}<=sqrt(B)`, for one fixed sufficiently small `eta_B>0` the quantity `psi_m(z)` stays uniformly away from zero when `|z|<=eta_B`, and the elementary expansion `log(1+w)=w+O(w^2)` yields

`log psi_m(z)=-mu_{2,m}z^2/2+O_B(z^4)`.                      (5.6)

Also, uniformly for small `x`,

`log cos x=-x^2/2+O(x^4)`.                                   (5.7)

Choose `eta>0` so that both expansions apply to every factor when `|t|<=eta sqrt(m)`. Summing the quadratic pieces in (5.6)-(5.7) gives exactly

`-[1+sigma_m^2 mu_{2,m}] v t^2/(2D_m^2)=-v t^2/2`.          (5.8)

Furthermore

`sum_j c_j^4 <= (max_j c_j^2) sum_j c_j^2 <= C0^2/m`.       (5.9)

Hence on `|t|<=eta sqrt(m)`,

`log hat p_m(t)=-v t^2/2+E_m(t)`,
`|E_m(t)|<=C t^4/m`.                                         (5.10)

After shrinking `eta`, this gives

`|hat p_m(t)-exp(-v t^2/2)|`
` <= C(t^4/m) exp(-v0 t^2/4)`,                               (5.11)

whose integral is `O(1/m)`.

For high frequencies no upper scale bound is needed. Since `S_m>=a_m`,

`psi_m(z)<=exp(-a_m^2 z^2/2)`.                               (5.12)

Therefore

`|hat p_m(t)|`
` <= exp[-rho_m^2 v t^2/2]`
` <= exp[-v0 rho_m^2 t^2/2]`.                               (5.13)

Thus

`int_{|t|>eta sqrt(m)} |hat p_m(t)|dt`
` <= C rho_m^{-1} exp(-c m rho_m^2)`.                        (5.14)

The Gaussian Fourier tail is `O(exp(-cm))`. Fourier inversion proves (5.2). Under (US1), the second term in (5.2) tends to zero because

`m rho_m^2 / log(e/rho_m) -> infinity`

implies `c m rho_m^2-log(1/rho_m)->infinity` for every fixed `c>0`. QED.

### Corollary 5.2 — microscopic lower slab

The inherited useful-normal geometry supplies a spread coordinate set of linear size with coefficient maximum `O(m^{-1/2})` and a fixed positive squared-mass lower bound. Condition on the complement. Its contribution has bounded second moment, so with fixed positive probability it lies in a fixed compact interval. Lemma 5.1 then gives, uniformly for the bounded shifts appearing in the marked-row construction and every `0<s<=1`,

`P{|<X,u>-z|<=s} >= c s`.                                   (5.15)

There is no Berry--Esseen additive floor and no `rho_m` loss in this lower slab after (US1).

## 6. Upper one-/two-plane bounds and projected small balls

These estimates are actually simpler: the lower scale floor, not an upper scale bound, controls them.

### Lemma 6.1 — one direction

For deterministic unit `u`, conditional on all Rademacher and scale variables,

`<X,u>`

is Gaussian with variance

`(sigma_m^2/D_m^2) sum_i S_i^2 u_i^2 >= rho_m^2`.           (6.1)

Hence

`||f_{<X,u>}||_infty <= (sqrt(2pi)rho_m)^{-1}`,              (6.2)

and

`P{|<X,u>-z|<=s} <= C rho_m^{-1}s`.                          (6.3)

### Lemma 6.2 — two directions

For unit `u,v`, write `r=<u,v>` and `Delta=1-r^2`. Conditional on the scales, the Gaussian covariance of the two projections satisfies

`Sigma >= rho_m^2 [[1,r],[r,1]]`.                            (6.4)

Therefore

`det Sigma >= rho_m^4 Delta`,                                (6.5)

so the conditional and unconditional joint density is at most

`C rho_m^{-2} Delta^{-1/2}`.                                 (6.6)

Consequently a product slab of width `s` has probability at most

`C rho_m^{-2} s^2 Delta^{-1/2}`.                             (6.7)

This preserves the exact projective-angle singularity used by the robust-pair decomposition.

### Lemma 6.3 — k-dimensional projection

Let `P` be any deterministic orthogonal projection of rank `k` and let `Z` be one fresh iid column. Conditional on the Rademacher and scale variables, the Gaussian covariance on `ran(P)` is

`(sigma_m^2/D_m^2) P diag(S_i^2)P`
` >= rho_m^2 I_k`.                                           (6.8)

Hence for every center `y` and radius `r>0`,

`P{||PZ-y||_2<=r} <= (C r/rho_m)^k`.                         (6.9)

No delocalization of `P` is needed.

## 7. Transfer into the row-submatrix exponent

The deterministic/random-rounding geometry in the preceding NM13-12 theorem is unchanged. The transferred hypotheses are now checked explicitly:

1. **center/variance:** exact by (3.1);
2. **coarse scalar anti-concentration:** (3.3)-(3.4);
3. **useful spread-direction microscopic lower slab:** Corollary 5.2;
4. **one-normal upper slab:** (6.3);
5. **robust two-normal/projective-angle pair bound:** (6.7);
6. **fresh-column projected small ball for the lower extreme:** (6.9).

Only the factors `rho_m^{-1}`, `rho_m^{-2}` and `rho_m^{-k}` differ from a fixed-smoothing proof. Their logarithmic costs are already isolated by (US2).

For the lower extreme, at

`t_m=exp[-(h(gamma)+epsilon)m/k_m]`,

(6.9) gives the fresh-column estimate

`P{dist(C_j,H_j)<=sqrt(m)t_m | H_j}`
` <= [C sqrt(m)t_m/rho_m]^{k_m}`.                            (7.1)

Taking logs,

`log RHS`
` <= -(h(gamma)+epsilon)m`
`    +(k_m/2)log m`
`    +k_m log(C/rho_m)`.                                     (7.2)

The candidate entropy is `h(gamma)m+o(m)`. By (US2), the last two terms in (7.2) are `o(m)`, so the `epsilon m` margin wins exactly as in the predecessor.

For the constructive upper extreme, Corollary 5.2 gives a fixed lower slab constant on useful normals, while (6.3) and (6.7) contribute at worst logarithmic penalties `O(log(1/rho_m))` per active codimension. The predecessor's three-tier survivor bookkeeping activates only `O(k_m)` such costs. Hence its total new logarithmic loss is

`O(k_m[log m+log(e/rho_m)])=o(m)`                            (7.3)

by (US2), while the candidate entropy remains `h(gamma)m+o(m)`. Thus the same two-sided exponential law follows, proving (2.4).

No projected coordinates are declared iid, no truncation of the matrix entries is used, and probability is applied only to genuinely fresh original rows/columns after the adaptive geometry has been frozen.

## 8. Concrete unresolved P12-successor application: exponential scale mixture

Let

`E~Exp(1)`, `S=1+E`, `sigma_m=m^{-1/3}`

and define

`xi_m = [R+m^{-1/3}(1+E)G]/sqrt(1+5m^{-2/3})`.              (8.1)

Here the scale is unbounded, so the immediate predecessor `S<=b` theorem does not apply.

The exact scale moments are

`E S^2=5`, `E S^4=65`.                                       (8.2)

The additive noise `SG` is genuinely non-Gaussian:

`Var(SG)=5`,
`E(SG)^4=195`,
`3 Var(SG)^2=75`,

so its fourth cumulant is

`120>0`.                                                      (8.3)

For `0<sigma<=1`, the normalized entry fourth moment is

`F(t)=(1+30t+195t^2)/(1+5t)^2`, `t=sigma^2`.                (8.4)

Since

`F'(t)=20(1+12t)/(1+5t)^3>0`,                                (8.5)

the whole triangular family satisfies

`E xi_m^4 <= F(1)=113/18`.                                   (8.6)

The effective floor is

`rho_m=m^{-1/3}/sqrt(1+5m^{-2/3}) ~ m^{-1/3}`.              (8.7)

Therefore

`m rho_m^2/log(e/rho_m) ~ m^(1/3)/[(1/3)log m] -> infinity`, (8.8)

and whenever `k_m log m=o(m)`,

`k_m[log m+log(e/rho_m)]=o(m)`.                              (8.9)

Thus the new theorem applies throughout the same moderate-surplus regime.

The family is outside frozen P12. Since `P(S<=2)=1-e^{-1}`, the sharper explicit version of (4.2) gives, for every fixed `q`,

`||f_m^{*q}||_infty`
` >= [(1-e^{-1})/2]^q`
`    D_m/[2 sigma_m sqrt(2pi q)]`
` >= c_q m^{1/3} -> infinity`.                               (8.10)

### Before / after for the applied claim

**Before this run:** the explicit iid triangular law (8.1) was not covered by frozen P12 and was not covered by the immediate NM13-12 bounded-scale theorem; its row-submatrix exponential law was **UNKNOWN in the project**.

**After this run, author-side / independent review pending:**

`boxed:`

`(k_m/m) log M^R_{m,r_m}(A_m) ->_P -h(gamma)`               (8.11)

for every `N_m/m->gamma>1` and `k_m log m=o(m)`.

This is the demonstrated parent application. It is not counted as a change to the already frozen P12 theorem statement.

The same proof also retains the predecessor's near-critical smoothing scale: for the present `a=1`, `E S^2=5`, one may take

`sigma_m=(log log m) sqrt(log m/m)`,                          (8.12)

for which (US1) still diverges and every fixed convolution-density ceiling still diverges.

## 9. Separation from posted and preceding results

- **Not the posted Yang--Wen--Shmalo bounded-density theorem:** the present triangular family has `||f_m||_infty` and every fixed `||f_m^{*q}||_infty` diverging.
- **Not the frozen P12 theorem:** no fixed `(q,M)` ceiling exists.
- **Not the immediate NM13-12 random-scale theorem:** `S=1+Exp(1)` has unbounded support, violating `S<=b`.
- **Not the posted kernel/ReLU/zero-margin Ising work:** the object is the minimum singular value over random row submatrices.
- **Not a T03 duplicate:** no lifted-RDT, overlap, stationary, or exact-sphere calculation is used.

A bounded public search dated 20 September 2026 still finds Yang--Wen--Shmalo (arXiv:2608.07410, submitted 7 August 2026) as the nearest row-submatrix universality result: it assumes one fixed centered real bounded-density subgaussian entry law. That is a materially different hypothesis. This is bounded negative evidence only, not a novelty certificate.

## 10. Parent before/after versus theory gain

### Frozen P12 parent

Before: frozen theorem as in Section 0, with the same two protocol-open audit/final-package obligations.

After: **unchanged**. This run does not rewrite or reopen that theorem.

### Applied unresolved successor claim

Before: explicit unbounded-scale family (8.1) **UNKNOWN / uncovered in project**.

After: exponent `-h(gamma)` proved author-side under the same `k_m log m=o(m)` dimension regime; independent review remains pending.

### Demonstrated theory gain

The immediate predecessor required

`S_m<=b` almost surely.

This run replaces that pointwise upper-support hypothesis by only

`sup_m E S_m^4<=B`.

The lower scale floor and effective smoothing conditions remain. Thus the gain is a strict **distributional-class / assumption improvement**, and it is used on an explicit unbounded-support scale mixture.

### T03 parent

Before and after this run:

`alpha_L=6.30297437506`,
`alpha_U=12.31963446`

at the current project-supported/review-pending tier. The stronger NM13-03 third-full point `12.2872222217` remains conditional and is not promoted here.

## 11. Executed checker

Essential sanity code:

`proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/2026-09-20T1158Z__unbounded_scale_nearlattice_check.py`

Archived actual output:

`proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/2026-09-20T1158Z__unbounded_scale_nearlattice_check.out`

The output verifies the exact moments `E S^2=5`, `E S^4=65`, the non-Gaussian fourth cumulant `120`, the sharp explicit B4 bound `113/18`, positivity of its derivative formula, the fixed-`q` convolution lower constants, (US1) growth at benchmark dimensions, a valid (US2) example, and the inherited near-critical smoothing scale. It ends

`ALL_UNBOUNDED_SCALE_NEARLATTICE_CHECKS_PASS`.

The checker is a sanity artifact; the theorem proof is Sections 2--7.

## 12. Residual obstruction and next attack

The remaining obstruction is now narrower. The proof still uses a deterministic **positive lower scale floor** `S_m>=a_m`; this is what gives the universal covariance lower bounds (5.12), (6.1), (6.4), and (6.8).

The next nonduplicating target is to allow `P(S_m=0)>0` or more generally no pointwise lower floor. A plausible route is not another moment Taylor estimate: it requires a random-mask restricted-covariance theorem on the fresh `k_m`-dimensional projection together with a spread-direction Fourier product that turns a positive fraction of active masks into high-frequency decay. Until that restricted-covariance step is proved, Bernoulli--Gaussian smoothing remains **UNKNOWN**, not zero and not silently covered.

## 13. ledger_delta

- worker: `NM13-12`
- track: quantitative universality / random matrices
- parent: P12 unresolved triangular smooth/B4 successor
- frozen_P12_theorem_before: unchanged finite-convolution theorem
- frozen_P12_theorem_after: unchanged
- immediate_predecessor_assumption: `0<a_m<=S_m<=b`
- new_assumption: `S_m>=a_m>0`, `sup_m E S_m^4<=B`, no upper support bound
- strict_gain_type: distributional class / assumption
- new_theorem: `NM12-P12-UNBOUNDED-SCALE`
- smoothing_conditions: `(US1)` and `(US2)`
- explicit_application: `S=1+Exp(1)`, `sigma_m=m^{-1/3}`
- application_before: UNKNOWN / uncovered in project
- application_after: exponent `-h(gamma)` author-side proved, independent review pending
- fixed_q_density_ceiling: diverges like at least `c_q m^{1/3}`
- T03_before: `[6.30297437506, 12.31963446]`
- T03_after: `[6.30297437506, 12.31963446]`
- NM13_03_conditional_point_preserved: `12.2872222217`
- posted_repackaging: no
- code_executed: yes
- checker_terminal: `ALL_UNBOUNDED_SCALE_NEARLATTICE_CHECKS_PASS`
- residual_obstruction: remove positive lower scale floor / Bernoulli-Gaussian masks
- status: PARTIAL / new author-side complete extension / independent review pending
