Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested but is not authenticated by this runtime.**

# NM13-12 — vanishing-Gaussian near-lattice universality beyond the frozen finite-convolution ceiling

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-12` / `proofnet24/NM13-12/progress-universality`  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`, current LIVE20 mapping  
Primary applied parent: **P12 unresolved triangular smooth-universality successor**  
T03 coordination: **NM13-03 / NM13-07 consumed only for current boundary; no duplicate lifted-RDT work**  
Status: **PARTIAL / NEW AUTHOR-SIDE COMPLETE REAL RANDOM-MATRIX EXTENSION / EXPLICIT PREVIOUSLY-UNCOVERED TRIANGULAR LAW SOLVED / INDEPENDENT REVIEW PENDING**

## 0. Compact continuity handoff and why the method changes now

### Frozen P12 state, source-exact

The latest canonical P12 report is

`proofnet24/P12-smooth-iid/runs/2026-09-17/2026-09-17T18-20-03Z__run-report.md`.

Its retained theorem is exactly this. For `F in {R,C}`, let `A_m in F^{N_m x m}` have iid centered variance-one entries with density `f_m`. Assume one **fixed** integer `q>=1` and one **uniform finite** constant `M` satisfy

`sup_m ||f_m^{*q}||_infty <= M`,

and assume

`N_m/m -> gamma>1`, `k_m=r_m+1`, `k_m log m=o(m)`.

Then

`(k_m/m) log M^F_{m,r_m}(A_m) ->_P -h(gamma)/d_F`,

with `d_R=1`, `d_C=2` and

`h(gamma)=gamma log gamma-(gamma-1)log(gamma-1)`.

There is **no fourth-moment assumption and no positive-moment assumption above variance normalization** in that frozen theorem. The explicitly retained mathematical successor is triangular smooth / bounded-fourth-moment universality without a uniform microscopic finite-convolution smoothing ceiling. The protocol-open P12 audit obligations are not reopened here.

### Immediate NM13-12 predecessor

The previous NM13-12 report is

`2026-09-20T0904Z__t03-deficit-compensated-safe-hull-universality.md`.

It proved a deterministic negative-margin row-augmentation theorem and improved a dependent non-Gaussian T03 extension, but did not move the original Gaussian T03 parent. Several recent NM13-12 runs have deliberately produced distinct T03 extensions while the source parent itself stayed fixed. In accordance with the owner anti-stagnation rule, this run changes method and parent application: it attacks the **actual P12 successor obstruction**, namely vanishing microscopic smoothing in a smooth triangular near-lattice law.

### POSTED boundary

`POSTED.md` excludes the already written row-submatrix papers from duplicate research. The claim below is not those theorems. The posted/public Yang--Wen--Shmalo theorem and the frozen P12 theorem require a fixed bounded-density / fixed finite-convolution microscopic ceiling. Here the entry density and every fixed convolution-density ceiling diverge to infinity. The precise new statement is a vanishing-Gaussian regularization theorem with an explicit smoothing scale.

---

## 1. Current T03 coordination — preserved, not duplicated

The newest companion states on `master` during this run are:

- `NM13-03`: `2026-09-20__t03-transport-lsi-alpha122872223.md` proves the Gaussian transport/log-Sobolev c-sector cage and supports the complete-third point `alpha=12.2872223`, still **CONDITIONAL** because the outward four-dimensional root enclosure is missing.
- `NM13-07`: `2026-09-20__t03-entropy-dissipation-sharp-microextend.md` proves positive variance-dissipation representations for both difficult c-sector entropies and strictly moves the directed-interval complete-second upper endpoint to

`alpha_U = 12.3196348278`.

Thus the current review-pending rigorous/source-supported exact-sphere Gaussian T03 bracket is

`[6.30297437506, 12.3196348278]`.

This run does not alter it and does not reproduce either peer's lifted-RDT stationarity work. The T03 parent before and after NM13-12 is therefore exactly the same bracket above.

---

## 2. New triangular near-lattice law

Let `R` be a Rademacher variable, let `G~N(0,1)` be independent, and for a deterministic sequence `sigma_m in (0,1]` define

`xi_m := (R + sigma_m G)/sqrt(1+sigma_m^2)`.                 (2.1)

Let `A_m` have iid entries with this law.

The law is centered and variance one. Its density is a two-Gaussian mixture and hence `C^infinity`. It is uniformly subgaussian for `sigma_m<=1`, and

`E xi_m^4 = (1+6 sigma_m^2+3 sigma_m^4)/(1+sigma_m^2)^2`,   (2.2)

so in particular the fourth moments are uniformly bounded by `3`.

This family is nevertheless outside frozen P12 whenever `sigma_m->0`.

### Proposition 2.1 — every fixed finite-convolution ceiling diverges

Fix any integer `q>=1`. Let

`p_q := max_j 2^{-q} binom(q,j) >0`.

The `q`-fold sum of (2.1) is a Gaussian mixture whose component centers are the lattice values of the sum of `q` Rademachers and whose common standard deviation is

`sigma_m sqrt(q/(1+sigma_m^2))`.

At a center carrying mass `p_q`, all mixture contributions are nonnegative, so

`||f_m^{*q}||_infty`
` >= p_q sqrt(1+sigma_m^2)/(sigma_m sqrt(2 pi q))`.          (2.3)

Hence for every fixed `q`,

`||f_m^{*q}||_infty -> infinity` whenever `sigma_m->0`.      (2.4)

Therefore no fixed `(q,M)` frozen-P12 hypothesis can cover this triangular family.

---

## 3. Main theorem — vanishing-noise near-lattice row-submatrix universality

Assume

`(VN1)  m sigma_m^2 / log(e/sigma_m) -> infinity`,           (3.1)

and

`(VN2)  k_m [log m + log(e/sigma_m)] = o(m)`.               (3.2)

The second condition reduces to the frozen `k_m log m=o(m)` regime for every polynomial or polylogarithmic smoothing scale.

### Theorem NM12-VN-RMT

Let `A_m in R^{N_m x m}` have iid entries (2.1), with

`N_m/m -> gamma>1`, `k_m=r_m+1`,

and suppose (VN1)--(VN2). Then

`boxed:`

`(k_m/m) log M^R_{m,r_m}(A_m) ->_P -h(gamma)`.              (3.3)

No uniform bounded-density or fixed finite-convolution ceiling is assumed; indeed (2.4) says those ceilings fail when `sigma_m->0`.

The proof reuses only the already frozen distribution-free geometry/survivor modules and replaces the microscopic analytic inputs by the new explicit Gaussian-smoothing lemmas below.

---

## 4. Uniform scalar anti-concentration despite `||f_m||_infty -> infinity`

### Lemma 4.1

For every `0<sigma<=1`, the law

`xi=(R+sigma G)/sqrt(1+sigma^2)`

satisfies

`Q_xi(1/2) := sup_z P{|xi-z|<=1/2} <= 3/4`.                 (4.1)

### Proof

Conditioned on `R=+1` or `R=-1`, `xi` is Gaussian with common variance and means

`mu_+ = +1/sqrt(1+sigma^2)`,

`mu_- = -1/sqrt(1+sigma^2)`.

Their separation is

`|mu_+-mu_-| = 2/sqrt(1+sigma^2) >= sqrt(2) > 1`.           (4.2)

An interval of radius `1/2` has length `1`, so it contains at most one of the two conditional means. If it contains one mean, that Gaussian component contributes at most `1` conditionally, while for the other component the interval lies entirely on one side of its mean and therefore contributes at most `1/2`. If it contains neither mean, each component contributes at most `1/2`. Averaging the two equally weighted components proves (4.1). QED.

This exactly supplies the fixed scalar anti-concentration gap required by the inherited random-rounding / sparse-kernel / tube geometry. The normalized second moment is already one.

---

## 5. New quantitative local-density lemma at vanishing smoothing scale

The difficult constructive direction needs a **lower microscopic slab probability** with no Berry--Esseen additive floor. The Gaussian component in (2.1) gives this down to nearly the `sqrt(log m/m)` scale.

### Lemma 5.1 — spread Rademacher-Gaussian local limit

Fix constants `v0>0` and `C0<infinity`. For each `m`, let `J_m` be any index set and deterministic coefficients `a_j` satisfy

`v := sum_{j in J_m} a_j^2 in [v0,1]`,

`max_{j in J_m}|a_j| <= C0/sqrt(m)`.                         (5.1)

Let

`Y_m = sum_{j in J_m} a_j xi_{m,j}`

with independent copies of (2.1). Let `p_m` be its density and let `phi_v` be the centered Gaussian density of variance `v`. Then there exist constants `c,C>0`, depending only on `(v0,C0)`, such that

`||p_m-phi_v||_infty`
` <= C/m + C sigma_m^{-1} exp(-c m sigma_m^2)`.              (5.2)

Consequently, under (VN1), for every fixed `L<infinity` there is `c_L>0` such that for all sufficiently large `m`, uniformly over all coefficient vectors obeying (5.1),

`inf_{|x|<=L} p_m(x) >= c_L`.                                (5.3)

### Proof

The characteristic function is

`hat p_m(t)`
` = exp[- sigma_m^2 v t^2/(2(1+sigma_m^2))]`
`   prod_j cos(a_j t/sqrt(1+sigma_m^2)).`                    (5.4)

Choose `eta>0` depending only on `C0` so that

`|a_j t|/sqrt(1+sigma_m^2) <= 1/4`

whenever `|t|<=eta sqrt(m)`.

For `|x|<=1/4`, the elementary Taylor remainder gives constants `C1<infinity` such that

`0 <= -log cos x - x^2/2 <= C1 x^4`.                         (5.5)

Because the explicit Gaussian factor in (5.4) plus the quadratic terms from the cosines add to exactly `-v t^2/2`, (5.5) gives on the low-frequency region

`hat p_m(t)=exp(-v t^2/2-R_m(t))`,

`0<=R_m(t)<=C2 t^4 sum_j a_j^4`
`               <=C3 t^4/m`,                                (5.6)

where the last inequality uses

`sum_j a_j^4 <= (max_j a_j^2) sum_j a_j^2 <= C0^2/m`.

Therefore

`|hat p_m(t)-exp(-v t^2/2)|`
` <= C4 (t^4/m) exp(-v0 t^2/2)`                              (5.7)

throughout the low-frequency region; the same estimate is harmless near its endpoint because the Gaussian factor is exponentially small. Integrating (5.7) gives an `O(1/m)` contribution.

For `|t|>eta sqrt(m)`, discard all cosine factors in modulus and use only the independent Gaussian smoothing:

`|hat p_m(t)|`
` <= exp[-sigma_m^2 v0 t^2/(2(1+sigma_m^2))]`
` <= exp[-(v0/4) sigma_m^2 t^2]`.                            (5.8)

The resulting Gaussian tail integral is bounded by

`C sigma_m^{-1} exp(-c m sigma_m^2)`.                        (5.9)

The corresponding tail of `exp(-v t^2/2)` is `O(exp(-c m))`. Fourier inversion now gives (5.2).

Under (VN1), for every fixed `c>0`,

`sigma_m^{-1} exp(-c m sigma_m^2) ->0`,                      (5.10)

because `m sigma_m^2/log(e/sigma_m)->infinity`. Thus the right side of (5.2) vanishes. Since `v in [v0,1]`, the family of target Gaussian densities has a strictly positive minimum on each compact interval `[-L,L]`; (5.3) follows. QED.

### Corollary 5.2 — useful-normal lower slab

The inherited useful-normal geometry supplies a spread set of linear size with coefficients between constant multiples of `m^{-1/2}` and with a fixed positive coefficient-mass lower bound. Apply Lemma 5.1 to that spread set. Condition on the complementary coordinates. Their variance is at most one, so a fixed bounded-shift event has fixed positive probability by Chebyshev. On that event, (5.3) gives, uniformly for all microscopic `0<s<=1`,

`P{|<X,u>-z|<=s} >= c s`                                    (5.11)

for the bounded shifts used in the inherited marked-row construction. The constant `c>0` is independent of `m` and `sigma_m` once `m` is large.

This is exactly the no-additive-floor lower slab input needed by the constructive upper extreme.

---

## 6. Exact upper projection bounds from the Gaussian component

Let `X` be one fresh iid row with entries (2.1).

### Lemma 6.1 — one direction

For every deterministic unit vector `u`, conditional on the Rademacher coordinates,

`<X,u>` is Gaussian with variance

`sigma_m^2/(1+sigma_m^2)`.

Therefore its unconditional density is a Gaussian mixture with

`||f_{<X,u>}||_infty <= sqrt(1+sigma_m^2)/(sqrt(2pi)sigma_m)`
`                      <= C sigma_m^{-1}`,                   (6.1)

and hence

`P{|<X,u>-z|<=s} <= C sigma_m^{-1} s`.                       (6.2)

### Lemma 6.2 — two directions

For deterministic unit vectors `u,v`, write

`rho=<u,v>`, `Delta=1-rho^2`.

Conditional on the Rademacher coordinates, the pair

`(<X,u>,<X,v>)`

is Gaussian with covariance

`[sigma_m^2/(1+sigma_m^2)] [[1,rho],[rho,1]]`.

For `Delta>0` its density is therefore bounded by

`C sigma_m^{-2} Delta^{-1/2}`.                               (6.3)

Thus for any shifts and widths `s,t>0`,

`P{|<X,u>-z1|<=s, |<X,v>-z2|<=t}`
` <= C sigma_m^{-2} Delta^{-1/2} s t`.                       (6.4)

When the directions are too close for (6.4) to be useful, (6.2) supplies the inherited bad-pair one-slab estimate.

These bounds hold for adaptive normals once their defining old rows are frozen, because probability is applied only to a genuinely fresh row.

---

## 7. Lower extreme — complete proof with explicit new penalty

Fix one candidate

`B in R^{(m+k-1) x m}`

and suppose `sigma_min(B)<=t`. The negative second-moment identity implies that for some column `C_j`,

`dist(C_j,H_j) <= sqrt(m) t`,                                (7.1)

where `H_j` is the span of the other columns.

Condition on all other columns. The fresh column `C_j` is independent. Choose any `k`-dimensional subspace of `H_j^perp` and let `P` be its orthogonal projection. Conditional on the Rademacher part of `C_j`,

`P C_j`

is a `k`-dimensional Gaussian with covariance

`[sigma_m^2/(1+sigma_m^2)] I_k`.

Therefore

`||f_{P C_j}||_infty <= (C/sigma_m)^k`.                      (7.2)

Multiplying by the volume of the `k`-ball of radius `sqrt(m)t` gives

`P{dist(C_j,H_j)<=sqrt(m)t | H_j}`
` <= [C sqrt(m) t/sigma_m]^k`.                               (7.3)

No sparse-basis extraction, finite-convolution density bound, or exceptional geometry event is needed on this branch.

There are `m` columns and

`log binom(N_m,m+k_m-1)=h(gamma)m+o(m)`                      (7.4)

candidate row sets. Take

`t=exp[-(h(gamma)+epsilon)m/k_m]`.                           (7.5)

The logarithm of the union bound is at most

`-epsilon m`
` + O(k_m log m)`
` + O(k_m log(e/sigma_m))`
` + o(m)`,                                                   (7.6)

which tends to `-infinity` by (VN2). Hence

`P{M_{m,r_m}(A_m) <= exp[-(h(gamma)+epsilon)m/k_m]} ->0`.    (7.7)

This proves the lower extreme.

---

## 8. Constructive upper extreme — transferred geometry, new microscopic estimates

The frozen P12/P13 proof architecture separates distribution-free geometry from the microscopic fresh-row estimates. The canonical finite-convolution report records the following exact dependency facts that are used here:

1. the tunable random-rounding / sparse-kernel / fresh-private-block tube geometry needs a fixed scalar anti-concentration gap and the normalized second moment;
2. useful-normal spread and robust adaptive two-plane geometry are frozen before probability is applied to fresh original rows;
3. the three-tier survivor mechanism needs a lower one-normal slab of order `s`, an upper one-normal slab, the projective-angle pair bound, and tunably small geometry-failure probabilities;
4. in the frozen theorem all polynomial medium losses are absorbed because `k_m log m=o(m)`.

Lemma 4.1 and `E xi_m^2=1` verify item 1 uniformly. The inherited geometry therefore yields the same useful normals, robust-pair decomposition, tunable weak-tube failure exponent, and linear fresh-row reservoir.

For the fresh-row analytic inputs, Corollary 5.2 gives the **same** uniform lower slab

`P{|<X,u>-z|<=s} >= c s`                                    (8.1)

with no `sigma_m` loss. Lemmas 6.1--6.2 replace the frozen upper estimates by

`C sigma_m^{-1} s`                                          (8.2)

for one direction and

`C sigma_m^{-2} Delta^{-1/2} s t`                           (8.3)

for robust pairs.

Consequently the inherited ordinary / medium / bad pair bookkeeping is changed only by multiplicative powers of `sigma_m^{-1}`. Conservatively, the old polynomial medium factor may be replaced by

`C m^3 sigma_m^{-2}`                                        (8.4)

and the bad one-slab factor by

`C sigma_m^{-1}`.                                           (8.5)

Now choose exactly as in the frozen proof

`h(gamma)-epsilon < lambda < h(beta)`

for some `1<beta<gamma`, then choose the intermediate bad-pair exponent strictly between `lambda` and the overlap-entropy rate. Set the marked-row width

`s = k_m^{-1/2} exp(-lambda m/k_m)`.                         (8.6)

Every successful stage keeps at least `c s` of the useful survivor set by (8.1). Across all `k_m` stages, the additional factors introduced by (8.4)--(8.5) contribute at most

`exp{ O(k_m log m + k_m log(e/sigma_m)) } = exp(o(m))`       (8.7)

by (VN2). They therefore do not alter any of the strict exponential inequalities between `lambda`, the bad-pair rate, and `h(beta)`. The tunable weak-geometry failure exponent is unchanged because Lemma 4.1 supplies a fixed anti-concentration gap independent of `sigma_m`.

Thus the entire three-tier survivor induction closes with the same exponential rate. A linear unused-row reservoir supplies the `k_m=o(m)` successful stages with probability tending to one, and at the end

`sigma_m(candidate) <= sqrt(k_m)s = exp(-lambda m/k_m)`.    (8.8)

Letting `lambda` increase to `h(gamma)-epsilon` gives

`P{M_{m,r_m}(A_m) > exp[-(h(gamma)-epsilon)m/k_m]} ->0`.    (8.9)

Together with (7.7), this proves Theorem NM12-VN-RMT.

### Hypothesis audit of every transferred module

- **freshness:** unchanged; all slab/pair probabilities are applied only after adaptive normals/planes are frozen and use a new original iid row;
- **centering:** exact by symmetry of (2.1);
- **variance:** exactly one;
- **uniform scalar anti-concentration:** Lemma 4.1;
- **useful-direction microscopic lower slab:** Corollary 5.2 under (VN1);
- **one-plane upper slab:** Lemma 6.1;
- **two-plane determinant singularity:** Lemma 6.2 has exactly `Delta^{-1/2}`;
- **geometry failure:** inherited random-rounding input uses only the fixed anti-concentration gap plus second moment, both verified;
- **moderate surplus:** every new `sigma_m` cost is logarithmic per stage and is absorbed by (VN2);
- **no projected-coordinate iid assumption:** none is used;
- **no matrix truncation:** none is used;
- **real scope only:** proved here; no complex analogue is claimed.

---

## 9. Concrete unresolved successor solved: `sigma_m=m^{-1/3}`

Take

`sigma_m = m^{-1/3}`.                                        (9.1)

Then

`m sigma_m^2/log(e/sigma_m)`
` = m^{1/3}/[1+(1/3)log m] -> infinity`,                    (9.2)

so (VN1) holds. Moreover

`log(e/sigma_m)=1+(1/3)log m`,

so the **same frozen moderate-surplus condition** `k_m log m=o(m)` implies (VN2).

By Proposition 2.1, for every fixed `q`,

`||f_m^{*q}||_infty >= c_q m^{1/3} -> infinity`,             (9.3)

so the frozen P12 theorem is genuinely unavailable. Nevertheless Theorem NM12-VN-RMT proves

`boxed:`

`(k_m/m) log M^R_{m,r_m}(A_m) ->_P -h(gamma)`               (9.4)

throughout the full frozen moderate-surplus regime.

### Applied-parent before / after

**Before this run:** this explicit smooth, uniformly subgaussian, uniformly bounded-fourth-moment triangular near-lattice family lay outside the P12 `(FC)` theorem for every fixed convolution power. Its row-submatrix exponent was **UNKNOWN / not covered** by the retained project theorem.

**After this run:** (9.4) is proved author-side for the entire family, with the same `k_m log m=o(m)` dimension regime.

This is the concrete successor application. It does not relabel the already posted fixed-density row-submatrix theorem as new.

---

## 10. Quantitative smoothing-rate gain

The local-density proof is substantially sharper than merely treating `sigma_m=m^{-1/3}`. Condition (VN1) allows smoothing essentially down to a logarithmic factor above `m^{-1/2}`.

For example, let

`sigma_m = L_m sqrt(log m/m)`,                               (10.1)

where `L_m->infinity` slowly and `sigma_m<=1`; for the concrete choice `L_m=log log m`,

`m sigma_m^2/log(e/sigma_m) ~ 2 L_m^2 -> infinity`.          (10.2)

Also `log(e/sigma_m)=O(log m)`, so frozen `k_m log m=o(m)` still implies (VN2). Hence Theorem NM12-VN-RMT covers, for instance,

`sigma_m=(log log m) sqrt(log m/m)`.                         (10.3)

At this scale every fixed convolution-density ceiling diverges at least like

`c_q sqrt(m/log m)/(log log m)`.                             (10.4)

Thus the demonstrated theory gain is not just one extra law: it is a quantitative vanishing-smoothing window approaching the lattice endpoint.

---

## 11. Relation to current literature and to the posted boundary

A bounded fresh search on 20 September 2026 recovered:

- Yang--Wen--Shmalo, arXiv:2608.07410 (submitted 7 August 2026): centered real **bounded-density subgaussian** row submatrices, fixed entry law / fixed density control, square candidates;
- Shmalo, arXiv:2607.06249: Gaussian row-submatrix theorem;
- Wang, arXiv:2211.03975: smoothed analysis / quantitative universality for the smallest singular value of one random matrix, not the exponential minimum over all row submatrices studied here.

No matching theorem for the triangular vanishing-noise near-lattice extreme-row-submatrix statistic surfaced in that bounded search. This is bounded dated negative evidence, not a novelty certificate.

The exact new difference from the posted row-submatrix results is therefore:

`fixed microscopic density/convolution ceiling`

is replaced, for the explicit near-lattice family (2.1), by

`m sigma_m^2/log(e/sigma_m)->infinity`

plus the logarithmic moderate-surplus budget (VN2), even though all fixed convolution-density ceilings diverge.

---

## 12. Sanity checks and executed artifacts

Executed checker:

`proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/2026-09-20T0951Z__vanishing_noise_nearlattice_check.py`

creation commit:

`dbdbd99d787b2afe4c297f6440af90d6ce752046`.

Archived actual output:

`proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/2026-09-20T0951Z__vanishing_noise_nearlattice_check.out`

creation commit:

`8e565f20c41ea44172a6f3b03917cd476da59f89`.

The checker verifies:

1. the exact fourth-moment formula and uniform bound;
2. explicit `1/sigma` divergence of fixed-`q` convolution peaks;
3. (VN1)--(VN2) numerics for `sigma=m^{-1/3}`;
4. the near-critical `L sqrt(log m/m)` smoothing scale;
5. exact binomial-Gaussian mixture density at zero for flat directions, converging numerically to `1/sqrt(2pi)`;
6. the uniform `Q_xi(1/2)<=3/4` argument.

The archived output ends

`ALL_VANISHING_NOISE_CHECKS_PASS`.

The numerical density values are sanity checks only; the theorem uses the analytic Fourier proof in Section 5.

---

## 13. What moved, what did not, residual obstruction, next attack

### Original frozen P12 theorem

Unchanged. Its source-exact `(FC)` statement remains valid as previously frozen; this report adds a distinct theorem and does not rewrite historical P12 files.

### Concrete P12-successor application

Strict movement:

`smoothed Rademacher with sigma_m=m^{-1/3}`

moved from **UNKNOWN / outside every fixed-(q,M) P12 theorem** to **PROVED AUTHOR-SIDE** with the same moderate-surplus exponent and regime.

### Demonstrated theory gain

A new quantitative local-density mechanism plus exact Gaussian-component projection bounds prove the row-submatrix exponent for vanishing smoothing as small as, e.g.,

`(log log m) sqrt(log m/m)`,

while the entry law approaches a discrete Rademacher lattice and every fixed finite-convolution density ceiling diverges.

### T03 parent

No NM13-12 movement. The current project bracket consumed for coordination remains

`[6.30297437506, 12.3196348278]`.

### Residual obstruction

This does **not** prove arbitrary triangular smooth/bounded-fourth-moment universality. The lower-density Lemma 5.1 uses an independent Gaussian component whose smoothing kills lattice resonances above frequency `sqrt(m)`. If

`m sigma_m^2` is only of order `log(1/sigma_m)` or smaller, the high-frequency Fourier tail in (5.9) is not forced to vanish by this argument. Completely unsmoothed or non-Gaussian-smoothed near-lattice laws therefore remain open.

### Next nonduplicating attack

Replace the Gaussian component by a general small independent noise with quantitative characteristic-function decay and determine the weakest condition on its Fourier tail that still yields (5.2). The target is a noise law whose variance may vanish at the same near-`sqrt(log m/m)` scale but is non-Gaussian, followed by a complex analogue if the two-dimensional projection kernel can be closed without importing the posted complex Gaussian theorem.

---

## 14. `ledger_delta`

```yaml
ledger_delta:
  worker: NM13-12
  date: 2026-09-20
  primary_parent: P12_unresolved_triangular_smooth_successor
  status: PARTIAL
  frozen_P12_state:
    hypothesis: "fixed q; uniform sup_m ||f_m^{*q}||_infty<=M; centered variance one; N_m/m->gamma>1; k_m log m=o(m)"
    conclusion: "(k_m/m) log M^F_{m,r_m} -> -h(gamma)/d_F"
    changed: false
  new_theorem:
    name: NM12-VN-RMT
    law: "xi_m=(R+sigma_m G)/sqrt(1+sigma_m^2)"
    assumptions:
      - "m sigma_m^2 / log(e/sigma_m) -> infinity"
      - "k_m [log m + log(e/sigma_m)] = o(m)"
      - "N_m/m -> gamma>1"
    conclusion: "(k_m/m) log M^R_{m,r_m} -> -h(gamma) in probability"
  strict_scope_gain:
    fixed_q_FC: "fails for every fixed q when sigma_m->0; ||f_m^{*q}||_infty >= c_q/sigma_m"
    explicit_solved_family: "sigma_m=m^{-1/3}"
    near_critical_example: "sigma_m=(log log m)*sqrt(log m/m)"
    dimension_regime: "same k_m log m=o(m) for the explicit polynomial/polylog scales"
  applied_parent_before: "UNKNOWN / not covered for sigma_m=m^{-1/3}"
  applied_parent_after: "PROVED AUTHOR-SIDE with exponent -h(gamma)"
  T03_parent_before_after: "[6.30297437506, 12.3196348278], unchanged by NM13-12"
  peer_coordination:
    NM13-03: "alpha=12.2872223 third-full supported CONDITIONAL; transport-LSI cage"
    NM13-07: "rigorous/source-supported alpha_U=12.3196348278; entropy-dissipation compiler"
  residual_obstruction: "remove independent Gaussian smoothing / close Fourier resonances at or below the sqrt(log m/m) scale"
  next_attack: "general small-noise Fourier-decay theorem; then complex analogue"
  checker_commit: dbdbd99d787b2afe4c297f6440af90d6ce752046
  output_commit: 8e565f20c41ea44172a6f3b03917cd476da59f89
  runtime_model: GPT-5.6_Sol
  runtime_reasoning: UNVERIFIED
```
