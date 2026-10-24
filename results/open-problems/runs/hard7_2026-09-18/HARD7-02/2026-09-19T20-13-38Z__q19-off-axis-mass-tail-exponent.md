Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. **Movement: `T_corr=2 -> 3`. Methods tried: B1/B20/B27. New theorem-sized PARTIAL result: every C2 angular probability law with positive off-axis mass has exact radial tail exponent `alpha`; in particular every positive-thickness Campbell--O'Rourke Figure-2 angular law has exponent `alpha`, while the zero-thickness endpoint is the known exponentially tailed i.i.d.-type law. Source Question 1.9 remains OPEN.**

# HARD7-02 — Campbell--O'Rourke Question 1.9: positive off-axis angular mass forces the input power exponent

Status: **PARTIAL / source Question 1.9 remains OPEN under bounded current-literature search / theorem candidate has a complete on-page proof and an exact finite-algebra self-check, but no independent audit.**

Frozen metric:

`T_corr = number of explicit non-i.i.d., non-Hermitian C2 dependence families for which the full asymptotic radial tail exponent/class of mu_{alpha,theta} is rigorously determined`.

Before: `T_corr=2`.

After: **`T_corr=3`**, counting the positive-thickness Campbell--O'Rourke Figure-2 family as one new explicit source family. The general theorem below is not used to inflate the metric by infinitely many units.

## 1. Continuity, ownership, repository state, and capability honesty

I resumed the active exclusive canonical claim

`operations/claims/CAMPBELL-OROURKE-2022-Q1.9.md`

and the latest completed checkpoint

`runs/hard7_2026-09-18/HARD7-02/2026-09-19T19-14-06Z__q19-balanced-phase-amplitude-band-exponent.md`.

At run start I re-read:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the active Q1.9 claim and newest own Q1.9 reports;
- repository-wide Campbell--O'Rourke/Q1.9/claim aliases;
- the neighboring C0032 terminal handoff `research7_2026-09-17/R7-06/handoffs/2026-09-19T095800Z__C0032_terminal_handoff.md`.

Ownership remains exclusive to HARD7-02. C0032 is the distinct i.i.d. heavy-tailed circular-law explicit-density problem and is in terminal handoff; it is not an equivalent claim. No canonical claim was overwritten and no shared root ledger was edited.

The runtime capability situation is unchanged in the exposed interface: task title, prompt, schedule/timing mode, enabled state and ordinary run controls are available, but there is **no binding model selector, no reasoning-effort selector, no authenticated effort telemetry and no guaranteed-duration field**. Thus `GPT-6 / maximum` is prompt-requested only; this run cannot honestly claim it. A real change would require a product/backend surface exposing binding model/effort controls or an authorized account/workspace context in which those controls exist. Historical `You cannot modify this task` responses for P26/P01/P03 were permission-context failures. The compliant workaround is an owning/authorized context, ownership transfer or platform support, never a duplicate task or permission bypass. Repository records say P26 later became editable from another authorized context; that does not imply all historical denials are globally resolved. No scheduler mutation was attempted here.

No Gmail, Drive, public posting, paid compute, workflow execution, force push, neighboring-track edit, permission bypass or schedule change was performed.

## 2. Exact source statement and bounded current-literature refresh

Primary source:

Andrew Campbell and Sean O'Rourke, *Spectrum of Heavy-Tailed Elliptic Random Matrices*, Electronic Journal of Probability **27** (2022), paper 127, arXiv:2010.01261v3, DOI `10.1214/22-EJP849`.

Section 1.3 asks exactly:

> **Question 1.9.** How does the tail behavior of `mu_{alpha,theta_d}` vary with respect to `theta_d`?

Definition 1.3 is the C1 joint regular-variation hypothesis with index `0<alpha<2` and angular/spectral measure `theta_d`; Definition 1.4 is C2, including the nondegeneracy condition that no nonzero linear form annihilates the angular support and the normalization `a_n/n^(1/alpha)->c>0`. Theorem 1.6 states that under C2 the empirical spectral distribution converges in probability to deterministic `mu_{alpha,theta_d}`, depending only on `(alpha,theta_d)`.

The source contrasts two endpoint regimes: the balanced axis-supported i.i.d. case has a much lighter, exponential limiting tail, while the Hermitian case inherits the heavy-tail behavior of the entries. Figure 2 studies the real angular family

`W=(cos omega,sin omega)`,

where `omega` is uniform on the four axis angles `{0,pi/2,pi,3pi/2}` thickened by a uniform interval `[-b pi/4,b pi/4]`; the paper plots positive values such as `b=0.1` and `b=0.5`.

Primary source checked this run: `https://arxiv.org/html/2010.01261v3`.

Fresh bounded searches dated 19 September 2026 used the exact title/authors, exact `Question 1.9` wording, `theta_d`, `mu_{alpha,theta_d}`, `tail behavior`, `heavy-tailed elliptic`, `PWIT`, and 2023--2026 follow-up terms. They recovered the 2022 source; Campbell--O'Rourke, *Spectrum of Lévy--Khintchine Random Laplacian Matrices*, J. Theor. Probab. 37 (2024); Carpenter--O'Rourke, *The Limiting Spectral Distribution for Sparse Elliptic Random Matrices*, arXiv:2508.04891 (2025); and recent finite-variance elliptic-law work. I did **not** locate a paper claiming a general resolution of Question 1.9 or the criterion below. This is bounded negative evidence, not a worldwide novelty certificate.

## 3. B1 — change category: from orbit geometry to off-axis support

The preceding run proved exponent `alpha` for balanced Haar-phase amplitude bands. Its proof looked as if a circle action were essential. Instead, integrate first over the **radial Pareto overshoot** of one selected large edge. The determinant becomes a quadratic polynomial in one real variable, so phase symmetry disappears from the argument.

The resulting angular invariant is much coarser than a group orbit:

`theta({w=(w_1,w_2): w_1 w_2 != 0})`.

The axis-supported endpoint is exactly the case in which this quantity is zero. Any positive off-axis mass contains a positive-measure sector bounded uniformly away from `w_1w_2=0`, and that sector is enough to generate a polynomial tail in the limiting ESD.

**B1 outcome: success.** The relevant category is not “Haar angular law versus non-Haar law”; it is “purely axis-supported versus positive off-axis mass,” at least for the power exponent.

## 4. Main theorem

### Theorem 4.1 — positive off-axis mass forces exponent `alpha`

Let `0<alpha<2`. Let `theta` be a probability measure on the unit sphere of `C^2` satisfying the C2(i) nondegeneracy condition of Campbell--O'Rourke. Assume

`rho_off := theta({(w_1,w_2): w_1 w_2 != 0}) > 0`.                (4.1)

Then the Campbell--O'Rourke limiting spectral law satisfies

`lim_{r->infinity} [-log mu_{alpha,theta}({|z|>r})]/log r = alpha`. (4.2)

This theorem is source-relevant but does **not** close Question 1.9: purely axis-supported angular laws, sharp tail constants, and a complete classification of all possible non-polynomial regimes remain outside its scope.

### Proof, Step 1: choose a positive-product sector

Because

`{w_1w_2 !=0} = union_{m>=1} {|w_1w_2| >= 1/m}`,

(4.1) implies that there is a `delta>0` such that

`E_delta := {|w_1w_2| >= delta}`,   `rho := theta(E_delta)>0`.     (4.3)

Campbell--O'Rourke Theorem 1.6 says the limit depends only on `(alpha,theta)`. It is therefore enough to use the exact representative

`R=U^(-1/alpha)`, `U~Uniform(0,1)`, `W~theta`,                    (4.4)

with `R,W` independent, pair

`(xi_1,xi_2)=R W`,                                                  (4.5)

diagonal variable `zeta=0`, and normalization

`a_n=n^(1/alpha)`.                                                  (4.6)

For every continuity set `D` of `theta` and all sufficiently large `n`,

`n P(W in D, R>=r a_n)=theta(D) r^(-alpha)`,                       (4.7)

so C1 is exact and C2(ii) has constant `c=1`; C2(i) is assumed. The choice `zeta=0` is harmless because the limiting law is determined by `(alpha,theta)`.

### Step 2: every radial moment below `alpha`

Put

`beta=alpha/2 in (0,1)`.                                           (4.8)

For either coordinate and

`Z=R^2 |W_i|^2`,

we have for every `y>0`

`P(Z>y) <= y^(-beta)`.                                              (4.9)

Indeed for `y>=1`, condition on `W_i` and use `|W_i|<=1`; for `0<y<1`, the right side exceeds one.

A fixed row has independent off-diagonal pairs across different unordered edges, so its squared Euclidean norm is bounded by

`S_n := n^(-1/beta) sum_{j=1}^{n-1} Z_j`,                          (4.10)

where the summands need not be identically distributed but all satisfy (4.9).

For `n>=2`, `t>=1`, let

`T=(t/2)n^(1/beta)`.                                                (4.11)

The large-summand part satisfies

`P(max_j Z_j>T) <= 2^beta t^(-beta)`.                              (4.12)

Also, uniformly in `j`,

`E[Z_j 1_{Z_j<=T}] <= 1 + T^(1-beta)/(1-beta)`.                    (4.13)

Hence Markov gives

`P(n^(-1/beta) sum_j Z_j 1_{Z_j<=T}>t/2)`
`<= 2 n^(1-1/beta)t^(-1) + [2^beta/(1-beta)] t^(-beta)`
`<= [2+2^beta/(1-beta)] t^(-beta)`,                                (4.14)

because `beta<1`, `n>=2`, `t>=1`. Combining (4.12) and (4.14),

`P(S_n>t) <= C_beta t^(-beta)`,                                    (4.15)

where one may take

`C_beta=2+2^beta+2^beta/(1-beta)`.                                 (4.16)

Fix `0<p<alpha` and put `q=p/2<beta`. Tail integration gives a uniform finite bound

`E S_n^q <= 1 + q C_beta/(beta-q) =: M_p`.                         (4.17)

For `0<p<2`, Weyl log-majorization and the Schatten/row inequality give for every finite matrix

`sum_k |lambda_k(A_n)|^p <= sum_k s_k(A_n)^p`
`<= sum_i ||Row_i(A_n)||_2^p`.                                     (4.18)

Taking expectations and dividing by `n`,

`E int |z|^p mu_{A_n}(dz) <= M_p`.                                (4.19)

Theorem 1.6 gives weak convergence in probability of `mu_{A_n}` to deterministic

`mu:=mu_{alpha,theta}`.

Apply convergence to `min(|z|^p,K)` and then monotone convergence in `K` to obtain

`int |z|^p mu(dz) <= M_p`, `0<p<alpha`.                            (4.20)

Writing

`F(r)=mu({|z|>r})`,                                                 (4.21)

Markov gives

`F(r) <= M_p r^(-p)`.                                               (4.22)

Therefore

`liminf_{r->infinity} [-log F(r)]/log r >= alpha`.                 (4.23)

### Step 3: good exceedance edges form an exact sparse Erdős--Rényi graph

Fix `s>=1`. Call an unordered edge `e={i,j}` **good** when both

`R_e > s n^(1/alpha)` and `W_e in E_delta`.                        (4.24)

By independence and the exact Pareto representative,

`P(e good)=rho/(s^alpha n)`.                                       (4.25)

Thus the graph `G_s` of good edges is exactly

`G(n,rho/(s^alpha n))`.                                            (4.26)

Let `M_s` be its isolated edges and `m_s=|M_s|`. They are pairwise vertex-disjoint. The exact expectation is

`E[m_s/n]`
`= [(n-1)rho/(2s^alpha n)] (1-rho/(s^alpha n))^(2(n-2))`
`-> rho e^(-2rho/s^alpha)/(2s^alpha)`.                             (4.27)

Conditional on an edge being good, write

`R_e=s n^(1/alpha)Y`,                                               (4.28)

where

`P(Y>y)=y^(-alpha)`, `y>=1`,                                       (4.29)

and `Y` is independent of the conditional angular mark `W in E_delta`.

## 5. B20 — why phase peeling was the wrong algorithm

Fix one selected isolated good edge `e={i,j}`, a spectral parameter `z`, and condition on all matrix randomness except its overshoot `Y` and angular mark `W=(w_1,w_2)`.

In the characteristic matrix `zI-A_n`, the selected directed entries are linear in `Y`. A determinant term can use neither, exactly one, or both. Therefore

`D(Y):=det(zI-A_n)=A+s C(W)Y-s^2 w_1w_2 B Y^2`,                   (5.1)

where

`B=det(zI-A_n^{\setminus{i,j}})`.                                  (5.2)

The exact generic 4x4 symbolic identity for the quadratic coefficient was checked after the idea checkpoint; see Section 9.

If `B=0`, any lower bound with `log|B|=-infinity` is trivial. Assume `B!=0`. Since `W in E_delta`, `w_1w_2!=0`, so factor

`D(Y)=-s^2w_1w_2 B (Y-r_1)(Y-r_2)`                                (5.3)

for some `r_1,r_2 in C`.

The key anti-concentration estimate is one-dimensional and phase-free.

### Lemma 5.1 — Pareto logarithmic anti-concentration

For `Y` satisfying (4.29),

`inf_{c in C} E log|Y-c| >= -2alpha`.                              (5.4)

**Proof.** Since

`|Y-c| >= |Y-Re(c)|`,

it is enough to consider real centers. The logarithm can be negative only where `|y-Re(c)|<1`. The Pareto density is

`alpha y^(-alpha-1) 1_{y>=1} <= alpha`.                           (5.5)

Because `log|t|<0` for `|t|<1`, replacing the density by its upper bound lowers the integral. Hence the negative contribution is at least

`alpha int_{-1}^1 log|t| dt = -2alpha`,                            (5.6)

while the complement contributes nonnegatively. `QED`

Applying Lemma 5.1 twice in (5.3), and using `|w_1w_2|>=delta`, gives

`E_Y log|D(Y)|`
`>= 2log s + log delta -4alpha + log|B|`.                          (5.7)

This is the decisive improvement over the previous phase-Haar proof: **no averaging in phase and no angular symmetry is used at all.**

Iterate (5.7) over all pairwise-disjoint isolated good edges. After truncating logarithms below and passing monotonically across the finitely many root singularities,

`E_selected log|det(zI-A_n)|`
`>= m_s K_s + log|det(zI-A_n^{\setminus V(M_s)})|`,               (5.8)

with

`K_s=2log s+log delta-4alpha`.                                     (5.9)

**B20 outcome: success.** The old algorithm failed outside Haar-phase families only because it integrated the wrong random variable. Radial Pareto peeling survives arbitrary angular phase laws. The actual obstruction is now the disappearance of the quadratic coefficient when `w_1w_2=0`.

## 6. Circular potential lower bound

For every finite matrix `M`, Jensen's formula gives

`(1/(2pi)) int_0^{2pi} log|det(re^{it}I-M)|dt`
`= sum_j log max(r,|lambda_j(M)|)`.                                (6.1)

Define

`V_n(r)=(1/n) sum_j log^+(|lambda_j(A_n)|/r)`.                     (6.2)

Circle-average (5.8). The `(n-2m_s)`-dimensional minor contributes at least `(n-2m_s)log r`. After subtracting `n log r`,

`E V_n(r) >= E[m_s/n](K_s-2log r)`.                               (6.3)

Choose

`c_delta := exp((log delta-4alpha-1)/2)`
`         = sqrt(delta) exp(-2alpha-1/2)`                          (6.4)

and set

`r=c_delta s`.                                                      (6.5)

Then exactly

`K_s-2log r = 1`.                                                   (6.6)

The p-moment bound (4.19) gives uniform integrability of `log^+(|z|/r)` over the finite ESDs: for any fixed `p in (0,alpha)`,

`sup_n E int_{|z|>L} log^+(|z|/r) mu_{A_n}(dz)`
`<= [sup_{u>L} log^+(u/r)/u^p] M_p ->0`.                          (6.7)

Hence Theorem 1.6, first with bounded truncations and then (6.7), yields

`E V_n(r) -> V(r):=int log^+(|z|/r) mu(dz)`.                      (6.8)

Combining (4.27), (6.3), and (6.6), for every `s>=1`,

`V(c_delta s) >= rho e^(-2rho/s^alpha)/(2s^alpha)`.               (6.9)

Equivalently, for `r>=c_delta`,

`V(r) >= [rho c_delta^alpha/2] r^(-alpha)`
`        * exp[-2rho(c_delta/r)^alpha]`.                           (6.10)

In particular, for all `r>=c_delta`,

`V(r) >= A r^(-alpha)`,                                             (6.11)

where one may take

`A=(rho c_delta^alpha/2)e^(-2rho)>0`.                              (6.12)

## 7. B27 — swap the quantifiers and recover the pointwise tail

The previous theorem said: for each specially symmetric angular family, prove exponent `alpha` separately.

The new statement swaps the quantifiers: **one geometric criterion works for every C2 angular law satisfying it.** Namely positive off-axis mass is enough.

Layer cake gives

`V(r)=int_r^infinity F(t) dt/t`.                                   (7.1)

Fix `0<p<alpha` and choose `gamma>alpha/p`. By monotonicity of `F` and (4.22),

`V(r)`
`<= int_r^{r^gamma} F(t)dt/t + int_{r^gamma}^infinity M_p t^(-p)dt/t`
`<= (gamma-1)log r F(r) + (M_p/p) r^(-p gamma)`.                  (7.2)

Since `p gamma>alpha`, the second term is at most `(A/2)r^(-alpha)` for all sufficiently large `r`. Comparing (6.11) and (7.2),

`F(r) >= [A/(2(gamma-1))] r^(-alpha)/(log r)`                      (7.3)

for all sufficiently large `r`. Therefore

`limsup_{r->infinity} [-log F(r)]/log r <= alpha`.                 (7.4)

Together with (4.23), this proves (4.2). `QED`

**B27 outcome: success.** The previous family-by-family theorem becomes a uniform sufficient criterion over an arbitrary angular class.

## 8. Direct answer for the source's Figure-2 interpolation family

Let `theta_b` be the angular law used in Campbell--O'Rourke Figure 2:

`omega=K+T`,                                                        (8.1)

where `K` is uniform on `{0,pi/2,pi,3pi/2}` and `T` is uniform on `[-b pi/4,b pi/4]`, and

`W=(cos omega,sin omega)`.                                         (8.2)

For every `b>0`, the angular law gives mass one to `w_1w_2!=0`, because the axes are only finitely many zero-probability points under the continuous thickening. Its support contains non-collinear directions, so C2(i) holds. It is non-i.i.d. because the two entries share the same heavy radial variable and angular mark; it is non-Hermitian except on a null subset of angles.

Theorem 4.1 therefore gives, for every `0<alpha<2` and every `b>0`,

`lim_{r->infinity} [-log mu_{alpha,theta_b}({|z|>r})]/log r = alpha`. (8.3)

At the exact endpoint `b=0`, `theta_0` is the balanced four-axis angular law. Campbell--O'Rourke identify that law with the i.i.d.-type limiting ESD, whose radial tail is exponential rather than a finite power exponent.

Thus this explicit source interpolation has a sharp qualitative discontinuity:

`b=0`: exponential-tail class;

`every b>0`: polynomial-tail exponent exactly `alpha`.             (8.4)

This is a concrete partial answer to the source's question “how does the tail behavior vary with respect to `theta_d`?” It also directly refutes a naive smooth-interpolation heuristic between the i.i.d. and Hermitian endpoint tail classes.

The metric moves `T_corr=2 -> 3` by counting the positive-thickness Figure-2 family as one explicit new source family.

## 9. Exact finite-algebra self-check

The idea was committed **before** code at

`runs/hard7_2026-09-18/HARD7-02/2026-09-19T20-13-38Z__idea-before-code-q19-log-product-criterion.md`

commit

`b63bf5b6c3d3e590d7c5093052481bfa0b4ed1d7`,

and read back successfully.

After that checkpoint, the finite algebra was exact-symbolically self-checked in

`artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T20-13-38Z__q19-log-product-check.py`

commit

`7b9626c4bcfd5373f77fae552abef6af83e5aabe`,

with archived output

`artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T20-13-38Z__q19-log-product-check.out`

commit

`2f686b2b2c2a2429f5a182c0602a158ea15e59ed`.

Both were read back successfully. The output ends

`ALL_EXACT_CHECKS_PASS = True`.

It checks exactly:

1. the selected-edge determinant is quadratic in the radial overshoot;
2. its `Y^2` coefficient is `-s^2 w_1w_2` times the endpoint-deleted principal minor;
3. `int_{-1}^1 log|t|dt=-2`;
4. the scale choice (6.4) makes the potential bracket exactly one.

This is a **self-check**, not an independent audit, and does not replace the written proof.

## 10. What remains open

Question 1.9 is **not closed** by Theorem 4.1. Among the remaining source-level issues are:

1. classification of purely axis-supported angular laws beyond the balanced i.i.d. endpoint;
2. whether mixed or singular angular laws admit sharper tail constants or slowly varying corrections;
3. a necessary-and-sufficient angular criterion for exponential versus power-law versus other tail classes;
4. exact leading asymptotics of `r^alpha F(r)` where a power tail occurs.

The present theorem establishes a broad sufficient condition and pins down a source interpolation family exactly at the exponent/class level. It does not claim a full answer to all `theta_d`.

## 11. Section-B accounting

- **B1 CHANGE THE CATEGORY — success.** Replaced orbit/Haar geometry by the support dichotomy `theta(w_1w_2!=0)>0` versus pure axis support.
- **B20 FIND WHY THE ALGORITHM FAILS — success.** The phase-peeling obstruction was artificial; integrating the radial Pareto overshoot gives a quadratic determinant and removes phase symmetry. The genuine obstruction is vanishing reciprocal product on the axis.
- **B27 SWAP THE QUANTIFIERS — success.** Upgraded separate symmetric-family arguments to one sufficient criterion valid for every C2 angular probability law with positive off-axis mass.

These differ from the preceding B14/B15/B4 triple.

A useful next triple, if Q1.9 remains active, is **B8/B16/B26**: discretize the purely axis-supported exceptional class without mistaking finite evidence for an asymptotic proof; compute all minimal atomic support patterns exactly; and hunt sporadic axis/mixed cases that may separate exponential from polynomial tails.

## 12. Structured ledger delta

- `track`: `HARD7-02`
- `source_target`: Campbell--O'Rourke (2022), Question 1.9
- `canonical_claim`: `operations/claims/CAMPBELL-OROURKE-2022-Q1.9.md`
- `metric`: `T_corr`
- `before`: `2`
- `after`: `3`
- `status`: `PARTIAL`
- `movement`: `YES`
- `new_result`: exact radial exponent `alpha` for every C2 angular probability law with positive off-axis mass; source Figure-2 family has exponent `alpha` for every `b>0`, contrasting with exponential `b=0`
- `source_status`: `OPEN` under bounded 2026-09-19 current-literature search
- `audits`: `0/2` for this theorem candidate
- `self_check`: exact finite algebra PASS, not an independent audit
- `next_methods`: `B8/B16/B26`

The unchanged streak remains zero because the frozen quantity moved. Section I is not triggered this run. No paper folder is created because the source problem remains open and the theorem has not received the required independent audits.