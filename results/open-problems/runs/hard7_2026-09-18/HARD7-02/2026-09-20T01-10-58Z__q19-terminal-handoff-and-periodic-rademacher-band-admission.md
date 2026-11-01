Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. **Q1.9 final-recovery outcome: no source-metric movement, `T_corr=4 -> 4`, so the second/final Section-I recovery cycle is exhausted and Campbell–O'Rourke Question 1.9 is handed off rather than continued. Fresh admitted target: Yi Han's September-2026 periodic hard-indicator discrete band circular-law problem; certified exponent bound `beta_band <= 8/9 -> beta_band <= 8/9` (no source-threshold movement). New mathematics: an exact PWIT half-angle one-branch Poisson pushforward for the Q1.9 handoff, a deterministic cyclic-band zero-forcing theorem, and a uniform Gaussian-smoothing `W_2` bridge reducing the discrete circular-law gap to the hard edge. Methods on the terminal Q1.9 recovery: B4/B7/B30. Methods on the fresh target: B2/B6/B30.**

# HARD7-02 — terminal Q1.9 handoff and admission of the periodic Rademacher band circular-law target

Status: **PARTIAL / Q1.9 RELEASED after Section-I exhaustion / fresh Han-2026 target OPEN and ACTIVE.**

## 1. Continuity, repository read, ownership, and capability honesty

This bounded run began from the newest HARD7-02 checkpoint

`runs/hard7_2026-09-18/HARD7-02/2026-09-20T00-14-17Z__q19-stuck2-rde-product-phase-tail.md`.

That report is the second permitted HARD Section-I recovery cycle on Campbell–O'Rourke Question 1.9. It records `T_corr=4 -> 4` after the two preceding ordinary runs also failed to move the frozen metric, and it requires the next recovery to either move the metric or hand off rather than manufacture another radial lemma.

At run start I re-read or refreshed:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the active Q1.9 claim `operations/claims/CAMPBELL-OROURKE-2022-Q1.9.md`;
- the newest HARD7-02 Q1.9 chain and the predecessor Q1.8 release/reassignment record;
- repository searches for Campbell–O'Rourke aliases, heavy-tail neighbors, the C0032 terminal handoff, random-band/circular-law claims, arXiv `2609.01295`, and the exact `Bernoulli scalar-indicator bands circular law` phrase;
- the relevant intake/search surfaces available through repository search. Large JSONL intake files are connector-truncated, so I do not claim a semantic line-by-line reread of every intake row; exact target/alias searches and the current canonical claim registry were checked before the fresh reservation.

No existing claim or posting for the exact fresh Han-2026 periodic Rademacher scalar-indicator target was located. A create-only canonical reservation was therefore made at

`operations/claims/HAN-2026-PERIODIC-RADEMACHER-BAND-CIRCULAR-LAW.md`.

No peer claim was overwritten. No shared root ledger, neighboring track, workflow, permissions, Gmail, Drive, public destination, or scheduler setting was changed.

The model/scheduler capability situation is unchanged. The exposed scheduling interface has ordinary task/prompt/schedule/enabled controls, but no binding model selector, no reasoning-effort selector, no authenticated reasoning-effort telemetry, and no guaranteed execution-duration field. `GPT-6 / maximum` is therefore prompt-requested only. A genuine fix requires a product/backend interface exposing binding model and effort controls or an authorized account/workspace context where those controls exist. Historical `You cannot modify this task` errors (including the recorded P26 case) are permission-context failures; the compliant workaround is the owning/authorized context, ownership transfer, or platform support, not duplication or bypass. No scheduler mutation was attempted in this run.

## 2. Campbell–O'Rourke Q1.9: final recovery before release

Primary source: Andrew Campbell and Sean O'Rourke, *Spectrum of Heavy-Tailed Elliptic Random Matrices*, EJP 27 (2022), paper 127, arXiv:2010.01261v3.

Exact source question:

> **Question 1.9.** How does the tail behavior of `mu_{alpha,theta_d}` vary with respect to `theta_d`?

The frozen HARD7-02 metric was

`T_corr = number of explicit non-i.i.d., non-Hermitian C2 dependence families whose full asymptotic radial tail exponent/class is rigorously determined by this track`.

Before this run: `T_corr=4`.

After this run: **`T_corr=4` — no movement.**

The preceding chain already proved considerably more than the four-family count suggests: pure-axis support has the iid-type light tail, every positive-off-axis C2 law has radial logarithmic exponent `alpha`, the radial moment index is `infinity` versus `alpha` on the two sides, and a two-sided Pareto envelope `c_theta r^{-alpha} <= mu(|z|>r) <= C_alpha r^{-alpha}` holds in the off-axis regime. What remains source-visible is directional regular variation / the actual tail measure, not another radial family.

A bounded 20 September 2026 current-literature refresh again recovered the 2022 source, related later Campbell–O'Rourke work, Carpenter–O'Rourke sparse elliptic work, and neighboring heavy-tail literature, but no located paper claiming the general directional tail measure for Question 1.9. This remains bounded negative evidence only.

### 2.1 Idea before calculation: stop asking an eigenvalue to survive and calculate the raw resonance point process exactly

The STUCK2 report identified a candidate half-angle rule from Proposition 4.12's bipartized resolvent RDE. For a large spectral point `z=R e^{i phi}`, the one-branch phase algebra predicts that a branch with angular mark `w=(w_1,w_2)` resonates in spectral direction `phi` when

`arg(w_1 w_2) = 2 phi (mod 2pi)`,

and its radial threshold scales as

`r sqrt(|w_1 w_2|) ~ R`.

The missing theorem was whether this local algebra survives the full recursive background and Hermitization. Before attempting that, this run asks a weaker but exact question: what is the **raw PWIT point process** after transforming each branch to exactly those predicted resonance coordinates?

### 2.2 B7/B30/B4 — exact half-angle pushforward theorem for raw PWIT branches

Let the radial PWIT intensity be

`m_alpha(dr)=alpha r^(-alpha-1) dr`,

and let the angular mark have law `theta`. Put `p(w)=w_1 w_2`. For `p(w)!=0`, choose one measurable square root

`u(w)^2=p(w)/|p(w)|`.

Attach an independent sign `sigma in {+1,-1}` and transform

`(r,w,sigma) -> (s,d)`,

`s=r sqrt(|p(w)|)`, `d=sigma u(w)`.

Define

`kappa_hat_theta(A)`
` = integral |w_1w_2|^(alpha/2) [1_A(u(w))+1_A(-u(w))]/2 theta(dw)`.

Then the Poisson mapping theorem plus the exact change of variables `s=r sqrt(|p|)` gives the image intensity

`alpha s^(-alpha-1) ds kappa_hat_theta(dd)`.

Therefore, for every Borel direction set `A`, the number `N_R(A)` of raw branches satisfying `s>R` and `d in A` is **exactly** Poisson with mean

`lambda_R(A)=R^(-alpha) kappa_hat_theta(A)`.

In particular,

`0 <= lambda_R(A)-P(N_R(A)>=1) <= lambda_R(A)^2/2`,

and

`P(N_R(A)>=2) <= lambda_R(A)^2/2`.

Conditional on a selected branch with `s>R`, the overshoot `s/R` has the Pareto tail `t^(-alpha)`, and the direction is distributed according to the normalized restriction of `kappa_hat_theta`; the two coordinates are independent because the intensity factorizes.

Full derivation is archived at

`artifacts/hard7_2026-09-18/HARD7-02/2026-09-20T01-10-58Z__q19-pwit-tail-map-and-band-zero-forcing.md`.

This is a rigorous auxiliary theorem and sharpens the STUCK2 heuristic: the candidate half-angle measure is not merely dimensional/phase algebra; it is exactly the intensity measure of single raw PWIT branches at the predicted resonance scale, and multiple raw branches are `O(R^{-2alpha})` on every fixed angular set.

It **does not** prove the spectral tail measure. The unpaid steps are unchanged in substance: under the rare resonance conditioning, replace the child resolvent by its free leading value with `o(1)` relative error, show the truncated recursive background changes the relevant phase/magnitude only at `o(R^{-alpha})` tail-measure scale, and pass through `eta downarrow 0` plus Hermitization to the planar ESD. Those steps are exactly where nonnormality/recursive feedback lives.

**B7 outcome:** success at the raw limiting-object level; the exact limiting marked Poisson intensity is identified.

**B30 outcome:** success at one radial/angular scale; one-branch and two-branch orders are exact.

**B4 outcome:** a weaker theorem is completely proved, but it does not move the source metric because `T_corr` counts completed tail classes, not raw PWIT branch laws.

### 2.3 Section-I decision: hand off Q1.9

This final recovery still leaves `T_corr=4`. The previous checkpoint was STUCK2, the second permitted hard-target recovery cycle. Under the controlling contract, HARD7-02 must not create a third stuck episode on the same problem. It therefore releases Q1.9 with all results and the new exact raw-branch theorem preserved.

The handoff obstruction is now as sharp as I can make it:

> Prove that the exact raw marked-PWIT intensity `alpha s^{-alpha-1}ds kappa_hat_theta(dd)` is preserved to first order by the recursive child-resolvent feedback and by the `eta downarrow 0` Hermitization map, or identify the recursive renormalization of `kappa_hat_theta`.

This release is **not** a proof, refutation, known-result declaration, publication claim, or abandonment of the mathematics. It is the mandatory Section-I rotation after two recovery cycles.

## 3. Fresh target admission: periodic Rademacher hard-indicator band circular law

Primary source: Yi Han, *The circular law for non-Hermitian random band matrices: optimal bandwidth, periodic profile and discrete law*, arXiv:2609.01295v2, revised **8 September 2026**.

The source abstract states:

> “From a universality perspective, it is conjectured that the circular law holds whenever `W_N -> infinity`.”

For the periodic hard-indicator profile, Han proves the optimal `W_N->infinity` threshold under bounded-density assumptions. For a discrete periodic **full-block** model the paper proves the circular law when `W_N >> log N`. The paper's remaining-regime discussion says the optimal non-block Bernoulli regime remains open and appears to require new discrete anti-concentration or an annealed interface argument.

### 3.1 Frozen exact model

Let the indices be `Z/NZ`, let `W_N<N/2`, put `L_N=2W_N+1`, and set

`X_N(i,j) = epsilon_ij/sqrt(L_N)` if `dist_N(i,j)<=W_N`,

`X_N(i,j)=0` otherwise,

where the `epsilon_ij` are independent symmetric Rademacher variables.

The exact target is:

`W_N -> infinity  =>  mu_{X_N} => circular law in probability`.

No bounded-density replacement, Gaussian entry law, block-tridiagonal/full-block geometry, or finite-size experiment counts as the source target.

### 3.2 Current literature and baseline

The fresh bounded search through 20 September 2026 found:

1. Han 2024, arXiv:2410.16457: for arbitrary doubly stochastic band-like variance profiles, symmetric subgaussian atoms satisfy the circular law when the bandwidth exponent `gamma>8/9`. This includes the frozen Rademacher hard-indicator profile and supplies the current verified discrete baseline.
2. Han 2025, arXiv:2508.18143: improves to `W>=N^(1/2+c)` for general band-like profiles under bounded-density assumptions; the no-density exception is a special block-band setting, so it does not lower the frozen scalar Rademacher baseline.
3. Han 2026 v2, arXiv:2609.01295: proves optimal `W->infinity` for bounded-density periodic hard-indicator profiles and proves a near-optimal discrete result `W>>log N` for a different periodic full-block model, while explicitly leaving optimal non-block Bernoulli regimes open.

Repository exact-title/arXiv/alias searches found no active claim or posting for the frozen target. The create-only claim is

`operations/claims/HAN-2026-PERIODIC-RADEMACHER-BAND-CIRCULAR-LAW.md`.

Define

`beta_band = inf{ beta: for every eps>0, the frozen circular law is rigorously known whenever W_N>=N^(beta+eps) eventually }`.

What is **certified**, rather than assumed, is

`beta_band <= 8/9`.

The source conjecture is `beta_band=0`.

**Before this run:** certified upper bound `8/9`.

**After this run:** certified upper bound **`8/9` — no movement.**

The two auxiliary results below do not by themselves lower the exponent, so I do not convert them into a threshold claim.

## 4. B2 — attack the negation: can narrow periodic support force localized singularity?

The first counterexample search asks whether the conjecture could fail for a trivial structural reason when `W_N` grows slowly: zero rows, repeated supports, or a kernel vector confined to a small cyclic set.

Zero rows are impossible because every row has exactly `L_N` nonzero Rademacher entries. For `W_N<N/2`, adjacent cyclic row supports are distinct, so the usual repeated-row-support mechanism is absent. More importantly, there is an exact deterministic zero-forcing bound.

### Theorem 4.1 — deterministic support lower bound

Let `A` be any matrix with the same cyclic hard-indicator support, with **arbitrary nonzero** values on every in-band site. If `Av=0` and `v!=0`, then

`|supp(v)| > N/(2W+1)`.

**Proof.** Put `S=supp(v)`, `|S|=k`. If `k<=N/L`, write the cyclic gaps between consecutive support points. Their total number of empty vertices is `N-k`, so one gap has at least

`(N-k)/k = N/k - 1 >= L-1`

empty vertices. If `s` is the support point immediately before that gap, the cyclic interval of length `L`,

`{s,s+1,...,s+L-1}`,

meets `S` only at `s`. This interval is exactly the support of the band row centered at `s+W`. That row equation is `a_{r,s}v_s=0`, impossible because both factors are nonzero. `QED`

For the frozen Rademacher matrix this holds on **every realization**, not just with high probability.

At a power bandwidth `W=N^gamma`, any exact null vector must therefore use more than order `N^(1-gamma)` coordinates. At the conjectural slowly growing scale `W=log N`, it must use more than order `N/log N` coordinates. Thus the most naive localized-kernel counterexample is impossible precisely where sparsity is strongest.

This is useful but does not control approximately sparse vectors, which are what least-singular-value/Hermitization arguments must eventually handle.

A second negation diagnostic is also worth recording. Reducing Rademacher entries modulo `2` destroys all sign randomness because `+1=-1 (mod 2)`: the random matrix collapses to the deterministic cyclic band mask. Therefore a finite-field proof that relies on randomness mod `2` cannot work for this target. This is a method obstruction, not a real singularity obstruction; odd primes or real small-ball estimates retain the randomness.

**B2 outcome:** no source counterexample found; exact localized null vectors below `N/(2W+1)` are ruled out, while the mod-2 test identifies a false proof route.

## 5. B6 — deform from the solved bounded-density model and isolate the only nonuniform step

The September-2026 source solves the same periodic hard-indicator geometry for bounded-density atoms. This suggests deforming a Rademacher atom into a smoothed one without changing the variance profile.

Couple

`xi_t=(epsilon+sqrt(t) g)/sqrt(1+t)`,

with `epsilon` Rademacher and `g` standard real Gaussian, and define `X_t` by replacing every in-band atom with `xi_t/sqrt(L)`. For every fixed `t>0`, `xi_t` has mean zero, variance one, bounded density and all moments. Hence Han's 2026 hard-indicator theorem gives the circular law for `X_t` under merely `W_N->infinity`.

The key quantitative question is whether the Hermitized singular-value measures remain close as `t downarrow 0` uniformly in `N`.

They do, away from the logarithmic hard edge.

### Theorem 5.1 — uniform singular-value Wasserstein bridge

For every `z in C`, under the natural coupling,

`E W_2(nu_{N,z}^{(t)},nu_{N,z}^{(0)})^2 <= q(t)`

with

`q(t)=2(1-(1+t)^(-1/2)) <= t`,

where `nu_{N,z}^{(t)}` is the empirical singular-value measure of `X_t-zI`.

**Proof.** Mirsky's inequality gives

`sum_j (s_j(X_t-zI)-s_j(X_0-zI))^2 <= ||X_t-X_0||_HS^2`.

For one in-band entry the mean-square difference is

`L^(-1)[((1+t)^(-1/2)-1)^2+t/(1+t)]`
`=L^(-1) 2(1-(1+t)^(-1/2))`.

There are exactly `NL` in-band entries. Hence

`E ||X_t-X_0||_HS^2=Nq(t)`.

Divide by `N` and couple ordered singular values. `QED`

Consequently every 1-Lipschitz singular-value statistic differs in expectation by at most `sqrt(t)`, uniformly in `N,W,z`.

Full derivation and the exact algebra for `q(t)` are archived at

`artifacts/hard7_2026-09-18/HARD7-02/2026-09-20T01-10-58Z__band-gaussian-smoothing-singular-value-bridge.md`.

This is a much sharper diagnosis than “density is used somewhere.” The bounded-density-to-Rademacher deformation is **uniformly stable for every bounded Lipschitz observable of the Hermitized spectrum**. The only nonuniform functional needed for Girko is `log s` at `s=0`.

A sufficient remaining bridge is therefore a discrete hard-edge uniform-integrability statement, for almost every fixed `z`, such as

`lim_{delta downarrow 0} limsup_N P( int_(0,delta) |log s| nu_{N,z}^{(0)}(ds) > eps ) = 0`.

With that estimate, truncate `log` on `[delta,M]`, use Theorem 5.1, use the known circular law for fixed `t>0`, and send `t downarrow 0`, `delta downarrow 0`, `M up infinity`. Thus the deformation route reduces the fresh source target to exactly the discrete hard-edge issue emphasized by Han's paper.

**B6 outcome:** substantial success but no exponent movement. The deformation debt is localized to hard-edge log-integrability; nonnormal eigenvalue continuity is never invoked.

## 6. B30 — localize by support scale and interface scale

The zero-forcing theorem suggests a clean decomposition for future runs.

1. **Exactly sparse vectors:** support `<=N/(2W+1)` is impossible deterministically.
2. **Mesoscopically compressible vectors:** support just above `N/W` up to a fixed fraction of `N` is the first genuine discrete anti-concentration regime. Here each row sees only a window of the vector, so inverse Littlewood–Offord information must propagate along the cycle.
3. **Incompressible vectors:** standard distance-to-span/small-ball ideas become plausible, but must be made uniform over the `N/W` interfaces and over shifts `z`.
4. **Hard edge:** even nonsingularity is insufficient; Girko requires a quantitative count/integrability of all very small singular values.

The natural next quantitative object is not another global checker but an **interface small-ball exponent**: for a vector class with at least `rho W` genuinely active coordinates in every window of length comparable to `W`, prove an odd-prime or real Littlewood–Offord bound per separated row and determine whether its product beats the entropy of the vector net uniformly when `W>>log N`. If that closes, the full-block `W>>log N` threshold may become accessible for the scalar hard-indicator geometry; below logarithmic bandwidth one would need the source's proposed annealed-interface mechanism rather than a union-bound net.

**B30 outcome:** a precise scale decomposition and first exact support threshold, but no circular-law exponent improvement yet.

## 7. Source-level before/after and auxiliary delta

### Campbell–O'Rourke Question 1.9

- Frozen metric before: `T_corr=4`.
- Frozen metric after: `T_corr=4`.
- Source status: **OPEN / PARTIAL**.
- Auxiliary delta: exact raw-PWIT half-angle marked intensity and `O(R^{-2alpha})` two-branch bound proved.
- Contract consequence: second/final recovery exhausted, so **handoff/release**.

### Han 2026 periodic Rademacher hard-indicator circular law

- Fresh certified source threshold before: `beta_band <= 8/9`.
- After: **`beta_band <= 8/9` — no movement**.
- Source conjecture: `beta_band=0` (`W_N->infinity`).
- Auxiliary delta 1: every exact null vector has support `>N/(2W_N+1)` deterministically.
- Auxiliary delta 2: Gaussian smoothing changes Hermitized singular-value ESMs by expected `W_2^2 <= 2(1-(1+t)^(-1/2)) <= t`, uniformly in `N,W,z`.
- Exact remaining bridge on this route: discrete hard-edge log-uniform-integrability / mesoscopic small-singular-value control.

No finite simulation was used and no sampled curvature/fit is being promoted as asymptotic evidence. The two new finite-dimensional inequalities are proved for all dimensions/parameters on the page; no numerical checker was needed.

## 8. Next run

Resume the fresh Han-2026 claim, not Q1.9. Do not return to the old radial Q1.9 chain unless another owner later reassigns it after a genuinely new route.

Use a different triple from B2/B6/B30. The most promising next choices are:

- B11: dualize the hard-edge logarithmic integral to counting singular values below dyadic thresholds;
- B19: formulate an explicit odd-prime/interface exposure algorithm along the cyclic band;
- B20: identify the exact failure mode of that algorithm — entropy of arithmetic structure versus accumulated small-ball gain — before attempting a net proof.

The first concrete target is a theorem for mesoscopically compressible vectors that strictly improves the deterministic support-only statement and is uniform for the shifted matrices `X_N-zI`; only an estimate strong enough to feed the hard-edge logarithmic sum counts as movement toward the source conjecture.
