Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested but is not authenticated by this runtime.**

# NM13-12 — random-scale near-lattice universality beyond deterministic Gaussian smoothing

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-12` / `proofnet24/NM13-12/progress-universality`  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`, current LIVE20 mapping  
Primary applied parent: **P12 unresolved triangular smooth-universality successor**  
T03 coordination: **NM13-03 / NM13-07 consumed only for current boundary; no duplicate lifted-RDT work**  
Status: **PARTIAL / NEW AUTHOR-SIDE COMPLETE REAL RANDOM-MATRIX EXTENSION / NEW EXPLICIT TRIANGULAR SCALE-MIXTURE FAMILY SOLVED / INDEPENDENT REVIEW PENDING**

## 0. Compact handoff and exact predecessor boundary

### Frozen P12 theorem, source-exact

The latest canonical P12 report remains

`proofnet24/P12-smooth-iid/runs/2026-09-17/2026-09-17T18-20-03Z__run-report.md`.

Its retained theorem is unchanged. For `F in {R,C}`, let `A_m in F^{N_m x m}` have iid centered variance-one entries with density `f_m`. Assume one fixed integer `q>=1` and one uniform finite constant `M` satisfy

`sup_m ||f_m^{*q}||_infty <= M`,

and assume

`N_m/m -> gamma>1`, `k_m=r_m+1`, `k_m log m=o(m)`.

Then

`(k_m/m) log M^F_{m,r_m}(A_m) ->_P -h(gamma)/d_F`,

where `d_R=1`, `d_C=2` and

`h(gamma)=gamma log gamma-(gamma-1)log(gamma-1)`.

There is **no fourth-moment assumption and no positive-moment assumption above variance normalization** in this frozen theorem. The explicitly retained mathematical successor remains triangular smooth / bounded-fourth-moment universality without a uniform microscopic finite-convolution ceiling. The protocol-open independent-audit obligations of frozen P12 are not altered here.

### Immediate NM13-12 predecessor

The preceding report

`2026-09-20T0951Z__p12-vanishing-noise-nearlattice-universality.md`

proved the real row-submatrix exponent for the single triangular law

`xi_m=(R+sigma_m G)/sqrt(1+sigma_m^2)`

under

`m sigma_m^2/log(e/sigma_m)->infinity`,

`k_m[log m+log(e/sigma_m)]=o(m)`.

Its decisive analytic input was a density-level local limit obtained from the Gaussian Fourier factor, plus exact one-/two-plane and projected-small-ball estimates from the same deterministic Gaussian smoothing variance.

The next obstruction recorded there was to replace this deterministic Gaussian smoothing by a genuine non-Gaussian small-noise class with quantitative Fourier-tail control. This run executes that extension.

### POSTED boundary

`POSTED.md` excludes the posted bounded-density row-submatrix papers, mesoscopic-spike paper, kernel/ReLU work and zero-margin Ising/perceptron work from duplicate research. The theorem below is not a rephrasing of those claims. It treats a triangular iid law whose entry density and every fixed convolution-density ceiling diverge, and whose additive noise is itself a non-Gaussian Gaussian scale mixture. The public Yang--Wen--Shmalo theorem still assumes one fixed bounded-density subgaussian entry law and square candidates.

---

## 1. Current T03 coordination, preserved rather than duplicated

The newest relevant companion states read during this run are:

- `NM13-07`: `2026-09-20__t03-entropy-dissipation-sharp-microextend.md` rigorously/source-supports the exact-sphere Gaussian upper endpoint

`alpha_U=12.3196348278`,

and develops a positive entropy-dissipation representation for the complete-third c-sector. Its complete-third waypoint remains conditional pending an outward root certificate.

- `NM13-03`: `2026-09-20__t03-curvature-overlap-alpha1228722223.md` proves a new curvature-overlap sandwich and supports the complete-third candidate

`alpha=12.28722223`,

still **CONDITIONAL** because the outward four-dimensional directed enclosure is not complete.

Therefore the exact iid-Gaussian T03 parent is not changed by this run. The current rigorous/source-supported bracket used here is

`[6.30297437506, 12.3196348278]`.

No stationarity, Krawczyk, entropy-dissipation or curvature-overlap calculation is duplicated below.

---

## 2. New random-scale triangular law

For each `m`, let

- `R` be Rademacher;
- `G~N(0,1)`;
- `S_m` be independent of `(R,G)` and satisfy

`0<a_m <= S_m <= b`

almost surely, for one fixed finite `b`;
- `0<sigma_m<=1`.

Write

`mu_{2,m}=E S_m^2`,

`D_m=sqrt(1+sigma_m^2 mu_{2,m})`,

and define

`xi_m := (R+sigma_m S_m G)/D_m`.                            (2.1)

The entries of `A_m` are iid copies of `xi_m`. The scale variables are resampled independently entry by entry, so this remains an iid triangular matrix model.

Define the **effective Gaussian floor**

`rho_m := sigma_m a_m / D_m`.                               (2.2)

The new point is that, conditional on `S_m`, the smoothing variance fluctuates from entry to entry. Unless `S_m` is almost surely constant, the additive noise `S_m G` is not Gaussian.

### Elementary distributional properties

Centering and variance normalization are exact:

`E xi_m=0`, `E xi_m^2=1`.                                   (2.3)

Since `S_m<=b`, the laws are uniformly subgaussian. Also

`E xi_m^4`
` = [1+6 sigma_m^2 mu_{2,m}+3 sigma_m^4 E S_m^4] / D_m^4`
` <= 1+6b^2+3b^4`.                                         (2.4)

Thus this is a uniformly bounded-fourth-moment smooth triangular family whenever `a_m>0`.

For each fixed `m`, conditioning on `(R,S_m)` shows that the law is a mixture of Gaussians with variance at least `rho_m^2`, hence it has a positive `C^infinity` density.

---

## 3. Every fixed finite-convolution ceiling still diverges

Assume `sigma_m->0`. Fix an integer `q>=1`, and let `f_m` be the density of (2.1).

Consider the event that all `q` Rademacher variables equal `+1`, which has probability `2^{-q}`. Conditional also on the scales `S_1,...,S_q`, the normalized `q`-fold sum is Gaussian with mean

`q/D_m`

and variance

`(sigma_m^2/D_m^2) sum_{i=1}^q S_i^2`.

At the common center `q/D_m`, its density is

`D_m / [sigma_m sqrt(2 pi sum_i S_i^2)]`

and `sum_i S_i^2 <= q b^2`. All other mixture components are nonnegative. Hence

`boxed:`

`||f_m^{*q}||_infty`
` >= 2^{-q} D_m/(sigma_m b sqrt(2 pi q))`
` >= 2^{-q}/(sigma_m b sqrt(2 pi q)).`                      (3.1)

Therefore

`||f_m^{*q}||_infty -> infinity`                             (3.2)

for every fixed `q` whenever `sigma_m->0`.

So the new class is genuinely outside the frozen `(q,M)` P12 theorem.

---

## 4. Uniform coarse anti-concentration from the fourth moment

The inherited geometry needs only a fixed scalar anti-concentration gap and the normalized second moment. The deterministic-Gaussian predecessor proved that gap by separating its two conditional means. That argument is no longer appropriate when the random scale can be large. A moment argument removes this restriction.

### Lemma 4.1 — variance/fourth-moment concentration gap

Let `X` be centered with

`E X^2=1`, `E X^4<=B`.

Then

`boxed:`

`Q_X(1/2) := sup_z P{|X-z|<=1/2}`
` <= sqrt(1-1/(2B+6)) < 1.`                                 (4.1)

#### Proof

Let `X'` be an independent copy and put `Z=(X-X')^2`. Then

`E Z=2`,

`E Z^2=E(X-X')^4=2E X^4+6(E X^2)^2 <=2B+6`.                (4.2)

Paley--Zygmund at level `Z>1=(1/2)E Z` gives

`P{|X-X'|>1} >= 1/(2B+6)`.                                  (4.3)

If an interval of radius `1/2` has mass `q`, the event that both copies lie in that interval has probability `q^2` and implies `|X-X'|<=1`. Thus

`q^2 <= 1-1/(2B+6)`.                                        (4.4)

Taking the supremum over interval centers proves (4.1). QED.

By (2.4), Lemma 4.1 applies uniformly to `xi_m`. This verifies the inherited coarse random-rounding / sparse-kernel input without using a bounded density.

---

## 5. Random-scale local-density theorem

The main new analytic step is that the local central limit remains uniform even though the additive noise is a non-Gaussian scale mixture and its smallest conditional variance may itself depend on `m`.

### Lemma 5.1 — spread local limit under a random Gaussian scale

Fix constants `v0>0`, `C0<infinity` and the scale ceiling `b<infinity`. Let deterministic coefficients satisfy

`v=sum_j c_j^2 in [v0,1]`,

`max_j |c_j| <= C0/sqrt(m)`.                                (5.1)

Let

`Y_m=sum_j c_j xi_{m,j}`

for independent copies of (2.1), and let `p_m` be its density. Let `phi_v` be the centered Gaussian density of variance `v`. There are constants `c,C>0`, depending only on `(v0,C0,b)`, such that

`boxed:`

`||p_m-phi_v||_infty`
` <= C/m + C rho_m^{-1} exp(-c m rho_m^2).`                 (5.2)

Consequently, if

`(RS1)  m rho_m^2 / log(e/rho_m) -> infinity`,              (5.3)

then for each fixed `L<infinity` there is `c_L>0` such that, for all sufficiently large `m`, uniformly over every coefficient vector satisfying (5.1),

`inf_{|x|<=L} p_m(x) >= c_L`.                               (5.4)

#### Proof

Let

`psi_m(z)=E exp(-S_m^2 z^2/2)`.

The characteristic function of one entry is

`phi_{xi_m}(t)=cos(t/D_m) psi_m(sigma_m t/D_m)`.             (5.5)

Hence

`hat p_m(t)=prod_j cos(c_j t/D_m)`
`                 psi_m(sigma_m c_j t/D_m).`                (5.6)

**Low frequencies.** Because `S_m<=b`, uniformly for sufficiently small `|z|`,

`log psi_m(z)=-(mu_{2,m}/2)z^2+O_b(z^4)`.                   (5.7)

Also

`log cos x=-x^2/2+O(x^4)`                                   (5.8)

uniformly for small `|x|`. Choose `eta>0`, depending only on `(C0,b,v0)`, so that both expansions hold for every factor whenever `|t|<=eta sqrt(m)`. Since

`D_m^2=1+sigma_m^2 mu_{2,m}`,                               (5.9)

the two quadratic terms add exactly to

`-v t^2/2`.                                                  (5.10)

Moreover

`sum_j c_j^4 <= (max_j c_j^2) sum_j c_j^2 <= C0^2/m`.       (5.11)

Thus on the low-frequency region

`log hat p_m(t)=-v t^2/2+E_m(t)`,

`|E_m(t)| <= C t^4/m`.                                      (5.12)

Shrink `eta` if needed so that `|E_m(t)|<=v0 t^2/4`. Then

`|hat p_m(t)-exp(-v t^2/2)|`
` <= C (t^4/m) exp(-v0 t^2/4)`,                             (5.13)

whose integral is `O(1/m)`.

**High frequencies.** Since `S_m>=a_m`,

`psi_m(z)<=exp(-a_m^2 z^2/2)`.                              (5.14)

Therefore, using only `|cos|<=1`,

`|hat p_m(t)|`
` <= exp[-(sigma_m^2 a_m^2/(2D_m^2)) v t^2]`
` <= exp[-(v0/2) rho_m^2 t^2].`                             (5.15)

Hence

`int_{|t|>eta sqrt(m)} |hat p_m(t)| dt`
` <= C rho_m^{-1} exp(-c m rho_m^2).`                       (5.16)

The corresponding tail of `exp(-v t^2/2)` is `O(exp(-c m))`. Fourier inversion gives (5.2).

Under (RS1), for every fixed `c>0`,

`rho_m^{-1} exp(-c m rho_m^2)->0`,                           (5.17)

so the right side of (5.2) tends to zero. The Gaussian family `phi_v`, `v in[v0,1]`, has a positive minimum on each compact interval, yielding (5.4). QED.

### Corollary 5.2 — microscopic lower slab

The frozen useful-normal geometry supplies a spread set of linear size with coefficients `O(m^{-1/2})` and a fixed positive squared-mass lower bound. Apply Lemma 5.1 to that spread set and condition on the complement. The complement has variance at most one, so with fixed positive probability its contribution lies in a fixed bounded interval by Chebyshev. On that event (5.4) yields, uniformly for the bounded shifts in the marked-row construction and all microscopic `0<s<=1`,

`P{|<X,u>-z|<=s} >= c s`.                                   (5.18)

There is no additive Berry--Esseen floor and no `rho_m` loss in the lower slab once (RS1) holds.

---

## 6. Exact one-plane and two-plane upper bounds

The random scale does not destroy the sharp projective-angle singularity.

### Lemma 6.1 — one direction

Let `u` be deterministic and unit. Conditional on all Rademacher and scale variables,

`<X,u>`

is Gaussian with variance

`(sigma_m^2/D_m^2) sum_i S_i^2 u_i^2 >= rho_m^2`.           (6.1)

Therefore its unconditional density satisfies

`||f_{<X,u>}||_infty <= (sqrt(2pi) rho_m)^{-1}`,             (6.2)

and

`P{|<X,u>-z|<=s} <= C rho_m^{-1}s`.                         (6.3)

### Lemma 6.2 — two directions

Let `u,v` be unit, `r=<u,v>` and `Delta=1-r^2>0`. Conditional on the Rademacher and scale variables, the Gaussian covariance of

`(<X,u>,<X,v>)`

is

`Sigma=(sigma_m^2/D_m^2) sum_i S_i^2 [u_i;v_i][u_i,v_i]`.

Since `S_i^2>=a_m^2`,

`Sigma >= rho_m^2 [[1,r],[r,1]]`                            (6.4)

in positive-semidefinite order. Hence

`det Sigma >= rho_m^4 Delta`.                               (6.5)

The conditional Gaussian density, and therefore the mixture density, is bounded by

`C rho_m^{-2} Delta^{-1/2}`.                                (6.6)

Thus

`P{|<X,u>-z1|<=s, |<X,v>-z2|<=t}`
` <= C rho_m^{-2} Delta^{-1/2} s t`.                        (6.7)

This is exactly the determinant singularity required by the frozen ordinary/medium/bad pair decomposition.

---

## 7. Arbitrary-subspace projected small ball

The lower extreme needs an estimate after conditioning on all other columns, where the relevant `k`-dimensional subspace is arbitrary. The Gaussian scale mixture still gives it pathwise after conditioning on the scales.

### Lemma 7.1

Let `Z in R^n` have independent coordinates distributed as (2.1), and let `P:R^n->R^k` have orthonormal rows. Conditional on the Rademacher and scale variables, `PZ` is Gaussian with covariance

`C=(sigma_m^2/D_m^2) P diag(S_1^2,...,S_n^2) P^T`

and

`C >= rho_m^2 I_k`.                                        (7.1)

Therefore

`||f_{PZ}||_infty <= (2pi rho_m^2)^{-k/2}`                 (7.2)

and, for every `r>0`,

`P{||PZ-y||_2<=r} <= (C r/rho_m)^k`.                        (7.3)

No coordinate alignment, delocalization or fixed convolution is used.

---

## 8. Main theorem

Assume

`(RS1) m rho_m^2/log(e/rho_m) -> infinity`,                 (8.1)

and

`(RS2) k_m[log m+log(e/rho_m)] = o(m)`.                     (8.2)

### Theorem NM12-RS-RMT — random-scale near-lattice universality

Let `A_m in R^{N_m x m}` have iid entries (2.1), with `S_m` allowed to vary with `m` subject only to

`0<a_m<=S_m<=b<infinity`,

and let

`N_m/m->gamma>1`, `k_m=r_m+1`.

If (RS1)--(RS2) hold, then

`boxed:`

`(k_m/m) log M^R_{m,r_m}(A_m) ->_P -h(gamma)`.              (8.3)

This strictly extends the predecessor deterministic-Gaussian smoothing theorem, corresponding to `S_m=1` almost surely.

### Proof — lower extreme

Fix a candidate `(m+k_m-1) x m` row submatrix `B`. If `sigma_min(B)<=t`, the inherited negative-second-moment step implies that for some column `C_j`,

`dist(C_j,H_j)<=sqrt(m)t`,                                  (8.4)

where `H_j` is the span of the other columns.

Condition on all other columns. The fresh column `C_j` is independent. Choose any `k_m`-dimensional subspace of `H_j^perp` and project onto it. Lemma 7.1 gives

`P{dist(C_j,H_j)<=sqrt(m)t | H_j}`
` <= [C sqrt(m)t/rho_m]^{k_m}.`                             (8.5)

There are `m` possible columns and

`log binom(N_m,m+k_m-1)=h(gamma)m+o(m)`                     (8.6)

candidate row sets. Set

`t=exp[-(h(gamma)+epsilon)m/k_m]`.                          (8.7)

The logarithm of the union bound is at most

`-epsilon m`
` + O(k_m log m)`
` + O(k_m log(e/rho_m))`
` + o(m)`,                                                   (8.8)

which tends to `-infinity` by (RS2). Therefore

`P{M_{m,r_m}(A_m) <= exp[-(h(gamma)+epsilon)m/k_m]} ->0`.    (8.9)

### Proof — constructive upper extreme

The predecessor report records exactly which frozen P12/P13 modules are distribution-free after the entry-law inputs are supplied:

1. random-rounding / sparse-kernel / fresh-private-block tube geometry requires a fixed scalar anti-concentration gap and second-moment normalization;
2. useful-normal spread and robust two-plane geometry are frozen before any probability is applied to a fresh original row;
3. the survivor induction uses a lower useful-normal slab of order `s`, an upper one-normal slab, the `Delta^{-1/2}` pair estimate, and tunably small geometry-failure probabilities;
4. all polynomial medium losses are absorbed when their logarithm times `k_m` is `o(m)`.

Here `E xi_m^2=1` and Lemma 4.1 gives the fixed anti-concentration gap, so item 1 transfers. Corollary 5.2 gives the same lower slab as the frozen proof. Lemmas 6.1--6.2 replace the upper fresh-row estimates by

`C rho_m^{-1}s`                                             (8.10)

and

`C rho_m^{-2} Delta^{-1/2} st`.                             (8.11)

Thus the old ordinary/medium/bad pair bookkeeping changes only by powers of `rho_m^{-1}`. Conservatively its total additional cost across `k_m` stages is

`exp{O(k_m log m+k_m log(e/rho_m))}=exp(o(m))`               (8.12)

by (RS2).

Choose as in the frozen construction

`h(gamma)-epsilon < lambda < h(beta)`

for some `1<beta<gamma`, and width

`s=k_m^{-1/2} exp(-lambda m/k_m)`.                           (8.13)

All strict exponential inequalities in the survivor proof are unchanged because (8.12) is subexponential on the `m` scale. The fresh-row reservoir supplies the required `k_m=o(m)` successful stages with probability tending to one, and the final candidate satisfies

`sigma_min <= sqrt(k_m)s = exp(-lambda m/k_m)`.             (8.14)

Letting `lambda` increase to `h(gamma)-epsilon` gives

`P{M_{m,r_m}(A_m) > exp[-(h(gamma)-epsilon)m/k_m]} ->0`.    (8.15)

Together with (8.9), this proves (8.3). QED.

### Complete transferred-hypothesis check

- iid entries within each `m`: yes; `(R,S_m,G)` is independently resampled per entry;
- centering: exact;
- variance one: exact by `D_m`;
- uniform fourth moment: (2.4);
- fixed scalar anti-concentration gap: Lemma 4.1;
- smooth density for each `m`: Gaussian mixture with conditional variance at least `rho_m^2>0`;
- useful-direction lower microscopic slab: Corollary 5.2 under (RS1);
- one-direction upper slab: Lemma 6.1;
- two-direction projective-angle singularity: Lemma 6.2, with exactly `Delta^{-1/2}`;
- arbitrary-subspace lower-extreme small ball: Lemma 7.1;
- freshness: every probabilistic slab/small-ball estimate is applied only after adaptive geometry is frozen and to a fresh original iid row/column, exactly as in the inherited proof;
- new per-stage cost: only logarithmic in `rho_m^{-1}`, absorbed by (RS2);
- no finite-convolution ceiling: not assumed, and Section 3 proves it fails in the concrete vanishing-noise regime.

---

## 9. Concrete unresolved successor claim solved

Take

`S ~ Uniform[1,2]`,

independent of `(R,G)`, and

`sigma_m=m^{-1/3}`.                                         (9.1)

Then

`E S^2=7/3`, `E S^4=31/5`,                                 (9.2)

and

`rho_m = m^{-1/3}/sqrt(1+(7/3)m^{-2/3}) ~ m^{-1/3}`.        (9.3)

The noise `SG` is genuinely non-Gaussian: its fourth cumulant is

`3[E S^4-(E S^2)^2] = 34/15 >0`.                            (9.4)

The normalized entry law is `C^infinity`, uniformly subgaussian and uniformly bounded-fourth-moment. In fact for `sigma<=1`, its fourth moment is increasing in `sigma^2` and at `sigma=1` equals

`3.024`.                                                     (9.5)

For each fixed convolution order `q`, (3.1) gives

`||f_m^{*q}||_infty >= c_q m^{1/3} -> infinity`.            (9.6)

Thus this family was outside every fixed-`(q,M)` frozen P12 theorem and also outside the immediate predecessor theorem, whose additive noise was exactly Gaussian with deterministic scale.

Now

`m rho_m^2/log(e/rho_m) ~ m^{1/3}/[(1/3)log m] -> infinity`, (9.7)

and when `k_m log m=o(m)`,

`k_m[log m+log(e/rho_m)]=o(m)`.                             (9.8)

Therefore Theorem NM12-RS-RMT proves

`boxed:`

`(k_m/m) log M^R_{m,r_m}(A_m) ->_P -h(gamma)`               (9.9)

throughout the same moderate-surplus regime `k_m log m=o(m)`.

The same theorem reaches the near-critical explicit scale

`sigma_m=(log log m) sqrt(log m/m)`                          (9.10)

for `S~Uniform[1,2]`: then `rho_m~sigma_m` and (RS1) still holds because the ratio is asymptotic to a positive constant times `(log log m)^2`.

---

## 10. Before / after accounting

### Applied P12-successor claim

**Before this run:** the explicit iid triangular law

`xi_m=[R+m^{-1/3} S G]/sqrt(1+(7/3)m^{-2/3})`, `S~Unif[1,2]`,

was **UNKNOWN / not covered** by frozen P12 and not covered by the deterministic-Gaussian NM13-12 predecessor. Every fixed finite-convolution ceiling diverges like `m^{1/3}`.

**After this run:** the real row-submatrix exponent (9.9) is proved author-side under the source moderate-surplus regime. Independent review is still pending.

This is a strict **distributional-class gain**: deterministic Gaussian smoothing is replaced by arbitrary entrywise Gaussian scale mixtures with `0<a_m<=S_m<=b`, controlled only through the effective floor `rho_m`.

### Frozen P12 theorem / protocol metric

The frozen theorem itself is not rewritten and its independent-audit protocol metric is unchanged. This run proves a successor extension; it does not claim to satisfy the missing P26 audit or the final packaging obligation.

### Original T03 parent

No NM13-12 T03 movement occurs in this run. Before and after, the rigorous/source-supported bracket used from the companions is

`[6.30297437506, 12.3196348278]`.

The `NM13-03` complete-third point `12.28722223` remains CONDITIONAL pending outward directed enclosure and is not promoted here.

---

## 11. Essential executed sanity checker

Executed artifact:

`proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/2026-09-20T1054Z__random_scale_nearlattice_check.py`

Archived output:

`proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/2026-09-20T1054Z__random_scale_nearlattice_check.out`

The execution checks:

- `E S^2=7/3`, `E S^4=31/5`;
- strict non-Gaussian noise fourth cumulant `34/15`;
- the normalized fourth-moment value `3.024` at `sigma=1`;
- positive explicit fixed-`q` convolution blow-up constants;
- growth of the (RS1) ratio at `sigma=m^{-1/3}`;
- decay of the (RS2) normalized cost for a sample `k=m^{0.4}`;
- the near-critical `(log log m)sqrt(log m/m)` smoothing scale;
- a strict fixed anti-concentration gap from Lemma 4.1.

The archived output ends

`ALL_RANDOM_SCALE_NEARLATTICE_CHECKS_PASS`.

Checker commit: `15becdc74afc73b49fa7fdad938f3ef557db550f`.  
Output commit: `c42e0652dbe38f2d373aa1a0e241f521e169abce`.

---

## 12. Honest residual obstruction and next nonduplicating attack

This theorem still uses a **strict Gaussian variance floor** inside the random scale mixture. The condition `S_m>=a_m>0` is what gives both the arbitrary-subspace projected-density bound and the global Fourier tail. It does not reach smoothing laws with no Gaussian component, Bernoulli-Gaussian noise with an atom at zero scale, or the unsmoothed Rademacher endpoint.

The next genuinely new obstruction is therefore not another deterministic scale calculation. It is to permit `P(S_m=0)>0` (or more generally no deterministic lower scale floor) by proving that a random coordinate mask remains quantitatively nondegenerate on the adaptive `k_m`-dimensional orthogonal complements and on the useful one-/two-plane normals. A successful theorem there would replace the worst-case floor `rho_m` by a high-probability restricted covariance lower bound and would strictly enlarge the near-lattice class again.

A bounded literature check during this run recovered Yang--Wen--Shmalo arXiv:2608.07410 as the current public bounded-density subgaussian row-submatrix theorem; no matching row-submatrix theorem for this vanishing random-scale near-lattice class surfaced. This is bounded negative evidence, not a novelty certificate.

---

## 13. ledger_delta

- worker: `NM13-12`
- track: quantitative universality / random matrices
- primary parent: P12 triangular smooth-universality successor
- frozen_P12_hypotheses: centered variance-one iid; fixed `q`; uniform `sup ||f_m^{*q}||_inf<infinity`; `N_m/m->gamma>1`; `k_m log m=o(m)`
- frozen_P12_positive_moment_assumption_above_variance: none
- unresolved_successor: triangular smooth/B4 universality without uniform microscopic finite-convolution smoothing
- immediate_predecessor: deterministic Gaussian smoothing `S=1`
- new_theorem: random-scale Gaussian-mixture smoothing with `0<a_m<=S_m<=b` and effective floor `rho_m=sigma_m a_m/D_m`
- new_conditions: `m rho_m^2/log(e/rho_m)->infinity`; `k_m[log m+log(e/rho_m)]=o(m)`
- strict_gain_type: distributional class / assumption
- concrete_new_family: `S~Unif[1,2]`, `sigma_m=m^{-1/3}`
- concrete_before: UNKNOWN / outside frozen P12 and outside predecessor deterministic-Gaussian theorem
- concrete_after: row-submatrix exponent `-h(gamma)` PROVED author-side in real case
- finite_convolution_ceiling_for_concrete_family: diverges as `c_q m^{1/3}` for every fixed `q`
- t03_parent_before: `[6.30297437506,12.3196348278]`
- t03_parent_after: `[6.30297437506,12.3196348278]`
- nm13_03_latest_consumed: curvature-overlap theorem; `12.28722223` CONDITIONAL
- nm13_07_latest_consumed: entropy-dissipation compiler; rigorous/source-supported `12.3196348278`
- posted_claim_repackaged: no
- checker_status: PASS
- independent_review: pending
- residual_obstruction: remove deterministic positive Gaussian scale floor; Bernoulli-Gaussian / zero-scale mask case

# END_NM13_12_RANDOM_SCALE_NEARLATTICE_2026_09_20T1054Z
