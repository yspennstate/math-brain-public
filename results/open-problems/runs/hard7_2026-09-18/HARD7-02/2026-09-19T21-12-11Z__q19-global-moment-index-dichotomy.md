Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. **Movement: `T_corr=3 -> 4`. Methods tried: B8/B16/B26. New theorem-sized PARTIAL result: over the entire Condition-C2 class, the radial moment index is exactly `infinity` on pure coordinate-axis support and exactly `alpha` as soon as the angular measure has any positive off-axis mass; hence arbitrarily small off-axis contamination creates a sharp moment-index jump. Campbell--O'Rourke Question 1.9 remains OPEN because exact tail constants, directional tails and the full profile are not classified.**

# HARD7-02 — Campbell--O'Rourke Question 1.9: a global moment-index dichotomy

Status: **PARTIAL / source Question 1.9 remains OPEN under bounded current-literature search / theorem candidate proved on-page from the preceding HARD7-02 results, with an exact algebra self-check but no independent audit.**

Frozen metric:

`T_corr = number of explicit non-i.i.d., non-Hermitian C2 dependence families for which the full asymptotic radial tail exponent/class of mu_{alpha,theta} is rigorously determined`.

Before: `T_corr=3`.

After: **`T_corr=4`**. The added unit is the unbalanced two-axis C2 family (and, by the earlier phase quotient, its arbitrary-axis-phase extension), whose radial tail is an exact dilation of the iid exponential-tail law. I count that class once, not once per parameter. The main new result of this run is stronger than the one-unit metric movement: it identifies the critical radial moment index on the whole C2 angular class.

## 1. Continuity, ownership, fleet state and capability honesty

I resumed the exclusive active claim

`operations/claims/CAMPBELL-OROURKE-2022-Q1.9.md`

from the newest completed checkpoint

`runs/hard7_2026-09-18/HARD7-02/2026-09-19T20-13-38Z__q19-off-axis-mass-tail-exponent.md`.

Before research I re-read the controlling files

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the current Q1.9 claim and newest HARD7-02 reports;
- the C0026--C0032 / heavy-tail neighborhood in the `probability_1000_intake_*/problems.jsonl` material through repository search;
- the neighboring R7-06/C0032 terminal handoff and current Campbell--O'Rourke claim aliases.

No collision, posting, external resolution, or ownership release of Question 1.9 was found. The distinct C0032 problem concerns the explicit density of the **iid** heavy-tailed circular law and is not an alias of Question 1.9. No shared root ledger and no other track's file was edited.

The runtime capability situation remains unchanged: the exposed scheduling/runtime surface has no binding model selector, no reasoning-effort selector, no authenticated effort telemetry and no guaranteed-duration control. `GPT-6 / maximum` therefore remains prompt-requested only. Changing that would require a platform/backend surface that actually exposes binding model/effort controls. Historical `You cannot modify this task` responses are permission-context failures; the compliant workaround for any still-refused task is an authorized owner/account/workspace context, ownership transfer, or platform support, never a duplicate schedule or permission bypass. No scheduler mutation was attempted in this run.

No Gmail, Drive, public posting, paid compute, workflow execution, force push, permission bypass, or schedule creation/modification was performed.

## 2. Primary source and current-status refresh

Primary source:

Andrew Campbell and Sean O'Rourke, *Spectrum of Heavy-Tailed Elliptic Random Matrices*, Electronic Journal of Probability **27** (2022), paper 127, arXiv:2010.01261v3, DOI `10.1214/22-EJP849`.

Primary links:

- https://arxiv.org/html/2010.01261v3
- https://arxiv.org/abs/2010.01261
- https://doi.org/10.1214/22-EJP849

Definition 1.3 uses a finite angular measure `theta_d` on the unit sphere of `C^2` and regular-variation index `0<alpha<2`. Condition C2 additionally requires that the support of `theta_d` is not contained in a complex hyperplane and that `a_n/n^(1/alpha) -> c>0`. Theorem 1.6 gives the deterministic limiting ESD `mu_{alpha,theta_d}`.

Section 1.3 states exactly:

> **Question 1.9.** How does the tail behavior of `mu_{alpha,theta_d}` vary with respect to `theta_d`?

Immediately before the question the authors state that the iid limiting ESD has an exponential tail, whereas the Hermitian limiting ESD has the same tail behavior as the entries. They also note earlier that the iid heavy-tailed non-Hermitian limit has finite moments of every order.

Fresh bounded searches on 19--20 September 2026 used the exact title/authors and the terms `Question 1.9`, `theta_d`, `mu_{alpha,theta_d}`, tail behavior, moment index, heavy-tailed elliptic, PWIT and 2023--2026 follow-up terms. They recovered the 2022 source, Campbell--O'Rourke's later Levy--Khintchine random-Laplacian paper, the 2025 sparse-elliptic work, and unrelated elliptic-law papers, but no located paper claiming a general resolution of Question 1.9 or the dichotomy below. This is bounded negative evidence, not a worldwide novelty certificate.

## 3. Idea-before-code checkpoint

The mathematical route was written before any checker at

`runs/hard7_2026-09-18/HARD7-02/2026-09-19T21-12-11Z__idea-before-code-q19-global-tail-index-dichotomy.md`

commit

`a292d6f6fd9291b1d75ec8327be4be25ad6bef2f`.

The new invariant is the **radial moment index**

`p_*(theta) := sup { p>0 : int_C |z|^p mu_{alpha,theta}(dz) < infinity }`.      (3.1)

The previous run determined the logarithmic radial tail exponent for positive off-axis mass, but that exponent alone does **not** determine whether the critical `alpha`-moment is finite. For example, an `r^(-alpha)(log r)^(-2)` tail has exponent `alpha` and can have finite critical moment. The integrated-tail lower bound proved in the previous run contains the missing endpoint information.

## 4. Inputs already proved in the HARD7-02 chain

I use three preceding on-page results, all still awaiting independent audit.

### 4.1 Positive off-axis mass: subcritical moments and integrated-tail lower bound

For a probability angular measure `theta` satisfying C2 with

`rho_off(theta) := theta({(w_1,w_2): w_1 w_2 != 0}) > 0`,            (4.1)

the preceding report proves, writing

`F_theta(r) := mu_{alpha,theta}({|z|>r})`,                           (4.2)

that

`int |z|^p mu_{alpha,theta}(dz) < infinity` for every `0<p<alpha`,   (4.3)

and that for some `A>0,r_0<infinity`,

`V_theta(r) := int_r^infinity F_theta(t) dt/t >= A r^(-alpha)`      (4.4)

for all `r>=r_0`.

The same report also proves the exact logarithmic power exponent `alpha`.

### 4.2 Complete axis-support classification

Earlier Question-1.8 work proves that if a C2 angular probability measure is supported on the two coordinate circles and has first-axis mass `p in (0,1)`, then

`mu_{alpha,theta} = (D_{k_{alpha,p}})_# mu_alpha`,                  (4.5)

where `mu_alpha` is the iid Bordenave--Caputo--Chafai limiting law and

`k_{alpha,p}^alpha = 2(2p-1)/log(p/(1-p))`,                         (4.6)

with the continuous value `1` at `p=1/2`. Arbitrary phase distributions on the two axes disappear under the proved gauge quotient.

The finite-mass form is also known from the chain: for axis masses `A,B>0`, the output scale satisfies

`kappa_alpha(A,B)^alpha = 2(A-B)/(log A-log B) = 2 L(A,B)`.         (4.7)

### 4.3 Mass normalization does not change the moment index

The earlier mass-homogeneity theorem says multiplying the angular measure by `m>0` dilates the limiting ESD by `m^(1/alpha)`. A nonzero deterministic dilation changes moment values but not which positive moments are finite. Therefore it is enough below to normalize a finite `theta_d` to a probability measure.

## 5. Main theorem: the whole C2 class has only two radial moment indices

### Theorem 5.1 — global C2 radial-moment-index dichotomy

Let `0<alpha<2`, and let `theta_d` be a finite nonzero angular measure arising under Campbell--O'Rourke Condition C2. Put

`rho_off(theta_d) := theta_d({(w_1,w_2): w_1 w_2 != 0})`.           (5.1)

Then

`p_*(theta_d) = infinity` if `rho_off(theta_d)=0`,                  (5.2)

while

`p_*(theta_d) = alpha` if `rho_off(theta_d)>0`.                     (5.3)

More precisely:

1. in the axis case every positive radial moment is finite and the full radial tail is an exact dilation of the source's iid exponential-tail law;
2. in the positive-off-axis case every radial moment of order `<alpha` is finite, the `alpha`-moment is infinite, every moment of order `>alpha` is infinite, and the logarithmic radial tail exponent is `alpha`.

#### Proof

Normalize `theta_d` by its total mass; by Section 4.3 this leaves `p_*` unchanged.

**Case 1: `rho_off=0`.** The set

`O := {(w_1,w_2): w_1 w_2 !=0}`

is relatively open in the unit sphere. If `theta(O)=0`, no point of `supp(theta)` can belong to `O`, because any such point would possess a positive-measure neighborhood contained in `O`. Hence

`supp(theta) subset {w_1=0} union {w_2=0}`.                         (5.4)

Condition C2(i) forces positive mass on both coordinate axes; otherwise the support lies in one complex hyperplane. The complete axis-support theorem (4.5)--(4.7) therefore applies. The source identifies the balanced reference law `mu_alpha` with the iid heavy-tailed circular limit and states that this law has an exponential tail and finite moments of every order. A deterministic nonzero dilation preserves those properties. Thus

`p_*(theta)=infinity`.                                              (5.5)

**Case 2: `rho_off>0`.** Equation (4.3) already gives

`p_*(theta) >= alpha`.                                              (5.6)

It remains to decide the critical moment, which was not decided by the previous tail-exponent statement alone.

Assume for contradiction that

`M_alpha := int |z|^alpha mu_{alpha,theta}(dz) < infinity`.         (5.7)

Layer cake gives

`M_alpha = alpha int_0^infinity t^(alpha-1) F_theta(t) dt`.         (5.8)

Hence the tail integral

`H(r) := int_r^infinity t^(alpha-1)F_theta(t)dt`                    (5.9)

satisfies `H(r)->0` as `r->infinity`.

For `t>=r>0`,

`1/t <= t^(alpha-1)/r^alpha`,                                      (5.10)

because the difference is exactly

`(t^alpha-r^alpha)/(r^alpha t) >=0`.                               (5.11)

Therefore

`V_theta(r) = int_r^infinity F_theta(t)dt/t`
`           <= r^(-alpha) H(r)`,                                  (5.12)

so

`r^alpha V_theta(r) -> 0`.                                         (5.13)

This contradicts the preceding theorem's lower bound (4.4), which gives

`r^alpha V_theta(r) >= A>0`                                        (5.14)

for every sufficiently large `r`. Thus

`int |z|^alpha mu_{alpha,theta}(dz)=infinity`.                      (5.15)

If some `p>alpha` moment were finite, then `|z|^alpha <= 1+|z|^p` would make the `alpha`-moment finite, another contradiction. Consequently all `p>=alpha` moments diverge, while all `p<alpha` moments are finite. Hence

`p_*(theta)=alpha`.                                                 (5.16)

This proves the dichotomy. `QED`

### Why this is genuinely stronger than the previous exponent theorem

Knowing only

`-log F(r)/log r -> alpha`

does not determine the `alpha`-moment. The new argument uses the stronger integrated-tail obstruction (4.4) to settle the endpoint exactly. Thus Theorem 5.1 is not a relabeling of the preceding exponent statement.

## 6. B8 — discretize: the infinite-dimensional tail-index problem collapses to one Boolean support statistic

For the specific scalar invariant `p_*`, the entire angular-measure space collapses to

`rho_off(theta)=0` versus `rho_off(theta)>0`.                        (6.1)

There is no third moment-index regime compatible with C2:

- `rho_off=0` forces pure two-axis support and `p_*=infinity`;
- `rho_off>0` forces `p_*=alpha`.

This is a legitimate discretization because it is proved for the exact limiting law, not inferred from a finite matrix or sampled path.

**B8 outcome: success.** The radial moment-index part of Question 1.9 has a complete two-state classifier.

## 7. B16 — minimal atomic support patterns

The dichotomy survives the smallest exact C2 support patterns.

### 7.1 Pure-axis two-atom family

For

`theta_p = p delta_(1,0) + (1-p) delta_(0,1)`, `0<p<1`,             (7.1)

C2(i) holds because the two atoms span `C^2`. If `p !=1/2`, this is a non-iid, non-Hermitian source-valid family. The earlier exact axis law gives

`mu_{alpha,theta_p}=(D_{k_{alpha,p}})_# mu_alpha`,                  (7.2)

so its tail is exponential up to deterministic radial scaling and

`p_*(theta_p)=infinity`.                                            (7.3)

For the concrete exact point `p=1/4`,

`k_{alpha,1/4}^alpha = 1/log 3`.                                   (7.4)

This family supplies the fourth unit in `T_corr`.

### 7.2 Minimal off-axis C2 pattern

Let

`u=(1,0)`, `v=(1,1)/sqrt(2)`,

and

`theta=(delta_u+delta_v)/2`.                                       (7.5)

The two atoms are not contained in one complex line, so C2(i) holds. Since `v_1 v_2 !=0`,

`rho_off(theta)=1/2>0`.                                             (7.6)

Theorem 5.1 gives

`p_*(theta)=alpha`.                                                  (7.7)

More generally, any finite atomic C2 angular law with at least one positive-weight off-axis atom lies in the same moment-index regime.

**B16 outcome: success.** Exhaustive small-support intuition has no sporadic intermediate moment-index case: the first admissible off-axis atom already triggers the critical index `alpha`.

## 8. B26 — hunt the sporadic boundary: a singular transition at zero off-axis mass

Two boundary tests could have invalidated the Boolean classifier. Neither does.

### 8.1 Extreme axis imbalance

For every `0<p<1`, however small, `theta_p` remains C2 and

`p_*(theta_p)=infinity`.                                            (8.1)

As `p downarrow0`, the earlier exact scale tends to zero only logarithmically, but every positive moment remains finite for each fixed `p>0`. The endpoint `p=0` itself is excluded by C2(i), so there is no hidden source-valid finite moment index at the axis boundary.

### 8.2 Arbitrarily small off-axis contamination

Fix any C2 axis law `theta_axis` and any angular probability law `nu_off` assigning positive mass to `O={w_1w_2!=0}`. For `0<epsilon<=1`, put

`theta_epsilon=(1-epsilon)theta_axis+epsilon nu_off`.               (8.2)

Because `theta_axis` already spans `C^2`, every `theta_epsilon` satisfies C2(i), and

`rho_off(theta_epsilon)>0` for every `epsilon>0`.                   (8.3)

Therefore

`p_*(theta_epsilon)=alpha` for every `epsilon>0`,                   (8.4)

whereas

`p_*(theta_0)=infinity`.                                            (8.5)

Since `theta_epsilon` converges weakly to `theta_0`, the map

`theta -> p_*(theta)`                                               (8.6)

has a genuine jump at the pure-axis boundary. This statement is only about the moment-index functional; it does **not** assert discontinuity of the full limiting ESD in any topology.

**B26 outcome: success.** There is no sporadic intermediate regime near zero off-axis mass. Any positive contamination, however small, already destroys all moments of order `>=alpha`.

## 9. Exact self-check, after the mathematics

Only after the idea/proof was written did I add the small exact symbolic self-check

`artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T21-12-11Z__q19-moment-index-check.py`

commit

`956ffee2a4559a0ddf503c5669fa84962165a207`,

with archived output

`artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T21-12-11Z__q19-moment-index-check.out`

commit

`020b93d6b99c7a88b79a46458eddb1277098b5f7`.

It checks exactly the factorization behind (5.10)--(5.11) and the concrete axis scale (7.4), ending

`ALL_EXACT_CHECKS_PASS = True`.

This is a **self-check**, not an independent audit and not a substitute for the analytic layer-cake proof.

## 10. What this answers and what remains open

This run gives a complete answer to one coarse but source-natural part of Question 1.9:

**the exact critical radial moment order of `mu_{alpha,theta_d}` is determined solely by whether `theta_d` places any mass off the two coordinate axes.**

Equivalently, within C2 the moment index has only the two values `infinity` and `alpha`.

It does **not** close the full source question. At least the following remain genuinely unresolved here:

1. the sharp asymptotic constant in the off-axis radial tail;
2. possible slowly varying corrections to `r^(-alpha)`;
3. directional tail exponents/constants and anisotropy, which the source explicitly highlights;
4. a full classification of tail profiles among different positive-off-axis angular measures.

Therefore the correct status remains **PARTIAL**, not PROVED and not REFUTED.

## 11. Section-B accounting and next route

- **B8 GO THE OTHER WAY AND DISCRETIZE — success.** For the moment-index functional, reduced arbitrary C2 angular laws to the exact Boolean invariant `rho_off=0` versus `>0`.
- **B16 COMPUTE EVERY SMALL CASE — success.** The minimal two-atom C2 patterns realize exactly the two global regimes and no third one.
- **B26 HUNT THE SPORADIC CASE — success.** Extreme axis imbalance stays all-moments, while arbitrarily small positive off-axis contamination immediately gives critical index `alpha`.

This triple differs from the previous B1/B20/B27 triple as required.

A useful next triple, if the source remains active, is **B5/B17/B30**: introduce a small off-axis contamination parameter `epsilon`, look for the first tail constant or slowly varying correction that survives after the universal exponent/moment-index collapse, and localize one radial scale at a time. The goal should be a genuinely quantitative `epsilon`-dependent asymptotic, not another family label or checker.

## 12. Ledger delta

```yaml
track: HARD7-02
source: Campbell--O'Rourke 2022 Question 1.9
claim: operations/claims/CAMPBELL-OROURKE-2022-Q1.9.md
status: PARTIAL
metric: T_corr
before: 3
after: 4
new_source_relevant_family: unbalanced C2 axis-supported family; exponential radial tail up to exact dilation
new_general_theorem: p_*(theta)=infinity iff rho_off(theta)=0; p_*(theta)=alpha iff rho_off(theta)>0
methods: [B8, B16, B26]
independent_audits: 0
closure: false
next: B5/B17/B30; seek epsilon-dependent sharp tail constant or slowly varying correction
```
