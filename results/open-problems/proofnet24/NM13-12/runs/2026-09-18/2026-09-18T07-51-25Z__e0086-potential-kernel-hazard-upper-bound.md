Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `C_large = 1/pi -> 1/pi`; Section-B methods actually tried: #1 CHANGE THE CATEGORY, #12 FIND WHAT IS CONSERVED, #24 FIND THE EXTREMAL OBJECT. Status: PARTIAL.**

# NM13-12 — E0086 potential-kernel hazard bound in the source main regime

Date: 2026-09-18 UTC  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Track: `NM13-12`  
Category: `HARD OUTSIDE`  
Canonical source / claim: `E0086` / `operations/claims/E0086.md`  
Canonical dedup key: `favorite_sites::op_2`  
Canonical SHA-256 / shard: `a616b4531a1a18ab6b2369a38d555ba54d6cc8cacdf46404e4e8ee26baeecc2c`, residue `11 mod 13`

## 1. Runtime, controls, continuity, and required reads

The prompt requests `GPT-6 / maximum`. That is not the model that actually ran. The actual model available to this invocation is **GPT-5.6 Sol**. No authenticated reasoning-effort telemetry is exposed, so the reasoning level is **UNVERIFIED**. I do not claim that GPT-6 or maximum reasoning was bound at runtime.

The exposed automation control schema still permits title/prompt, schedule or relative start, timing mode, enabled state, and ordinary task updates. It still exposes **no model-family selector and no reasoning-effort selector**. Making `GPT-6 / maximum` binding would require an owner-authorized product/workspace/API/admin surface that exposes those fields plus authenticated per-run runtime attestation. Repository policy records the historical P26 `You cannot modify this task` result as an authorization-context boundary; the lawful workaround is the owning/otherwise-authorized context or platform/admin support, not cloning the task or bypassing access control. This invocation did not create, edit, disable, or duplicate any schedule and does not claim a support escalation.

Before mathematics I reread or targeted-search-recovered the required current state:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- current canonical claim `operations/claims/E0086.md`;
- the newest own report `proofnet24/NM13-12/runs/2026-09-18/2026-09-18T07-12-00Z__e0086-large-radius-source-correction.md`;
- newest neighboring NM13-11 report `proofnet24/NM13-11/runs/2026-09-18/2026-09-18T07-15-57Z__e0082-row-extremal-dual-lp.md` and newest visible NM13-13 report `proofnet24/NM13-13/runs/2026-09-18/2026-09-18T06-58-37Z__successor-admission-screen-2.md`;
- E0086 intake/source material, old substantive attempt `E0086-A001`, canonical dedup material, current/historical ownership searches, and bounded current literature searches.

Pre-write `master` was observed at `ea60d9802c16435ef9c8504e206ce36462b3bee4`. The predecessor P0483 handoff remains mandatory and was not reopened. E0086 remains exclusively claimed by NM13-12; I found no release, duplicate owner, POSTED closure, or source-specific retirement. Neither P26 nor NM13-13 has a recorded E0086 PASS audit.

The previous E0086 run moved the frozen metric from `UNMEASURED` to `1/pi` by proving the source's large-radius boundary-collapse theorem and refuting the source-displayed `tau_n` equality as written. Its methods #2/#6/#30 are therefore spent and were not repeated here. Its counters were `unchanged_runs=0`, `stuck_recoveries=0`.

## 2. Exact source scope and frozen metric

The source is Izumi Okada, *Topics and problems on favorite sites of random walks*, arXiv:1606.03787, Open Problem 2. For planar simple random walk let

\[
R(n)=\{S_0,\ldots,S_n\},\qquad
K(n,x)=\sum_{i=0}^n\mathbf 1_{\{S_i=x\}},
\]

and for a finite pattern `H`

\[
\partial_H G=\{y\in G:y+H\subset G^c\},\qquad
M_H(n)=\max_{y\in\partial_HR(n)}K(n,y).
\]

The source fixes `M`, takes `\widetilde D_n\in\mathcal H(M)`, asks for the almost-sure asymptotic of `M_{\widetilde D_n}(n)` when the pattern recedes from the origin, and says it is especially interested in

\[
\widetilde D_n\subset D(0,n^\beta)^c\cap D(0,2n^\beta),
\qquad 0<\beta<\tfrac12. \tag{2.1}
\]

The frozen metric is **not changed**:

\[
C_{\rm large}:=\lim_{n\to\infty}
\frac{M_{\widetilde D_n}(n)}{(\log n)^2}
\]

under the separate source large-radius hypothesis `a_n>=n^(1/2+epsilon)`. It remains exactly

\[
C_{\rm large}=\frac1\pi.
\]

The theorems below address the source's main `0<beta<1/2` regime but are subordinate progress; they do not redefine the metric.

## 3. Idea before proof: replace a moving translated boundary by a two-point killed walk

The previous route was geometric: when the pattern lies beyond the whole range, the generalized boundary becomes all of `R(n)`. That route cannot enter `beta<1/2`, because the pattern then lies well inside the diffusive scale.

The new route changes categories. Membership

\[
y\in\partial_{H}R(n)
\]

means that **every** translated point `y+h`, `h in H`, has been avoided up to time `n`. Therefore one may discard all but one displacement `h` and ask a two-point renewal question: how many returns to `y` can occur before the walk first hits `y+h`? In two dimensions that renewal hazard is exactly a potential-kernel quantity. This gives a direct exponential tail on boundary local time and, unlike the previous large-radius argument, remains informative at the source scale `|h|=n^beta`.

No code was written before this idea. The result is analytic and has no finite enumerative core, so no checker was manufactured merely to certify an unchanged frozen metric.

## 4. Exact two-point hazard

Let `\mathfrak a(x)` denote the standard potential kernel of planar simple random walk, normalized by `\mathfrak a(0)=0`. A standard killed-Green identity gives

\[
2\mathfrak a(h)
=
E_0\bigl[\#\{j<T_h:S_j=0\}\bigr],\qquad h\ne0. \tag{4.1}
\]

Indeed, this is the translated form of the usual statement that `2\mathfrak a(h)` is the expected number of visits to the starting point before first hitting the other point. Successive excursions from `0` therefore show that the number of visits before `T_h` is geometric, with success parameter

\[
q(h):=P_0(T_h<T_0)=\frac1{2\mathfrak a(h)}, \tag{4.2}
\]

where both hitting times are positive-time hitting times. Hence

\[
p(h):=P_0(T_0<T_h)=1-q(h)
=1-\frac1{2\mathfrak a(h)}. \tag{4.3}
\]

For simple random walk the potential-kernel asymptotic is

\[
\mathfrak a(h)
=
\frac2\pi\log|h|+\frac{2\gamma+\log8}{\pi}+O(|h|^{-2}). \tag{4.4}
\]

For `|h|` between `n^beta` and `2n^beta`, this is uniformly

\[
\mathfrak a(h)=\frac{2\beta}{\pi}\log n+O_\beta(1),
\qquad
q(h)=\frac{\pi}{4\beta\log n}+O_\beta((\log n)^{-2}). \tag{4.5}
\]

## 5. Finite-time boundary-local-time tail

### Lemma 5.1 — single displacement

For every deterministic `h\in\mathbb Z^2\setminus\{0\}`, every integer `m>=1`, and every `n>=0`,

\[
\boxed{
P\bigl(M_{\{h\}}(n)\ge m\bigr)
\le
(n+1)\left(1-\frac1{2\mathfrak a(h)}\right)^{m-1}.
} \tag{5.1}
\]

#### Proof

If `M_{\{h\}}(n)>=m`, there is a site `y` such that

1. `y` is visited by time `n`;
2. `y+h` is not visited by time `n`;
3. the walk visits `y` at least `m` times by time `n`.

Let `\sigma_y` be the first visit to `y`; necessarily `\sigma_y=k` for some `0<=k<=n`. After time `k`, the walk must make at least `m-1` returns to `y` before its first visit to `y+h`. By translation invariance and the strong Markov property, conditional on `\mathcal F_k`, the probability of `m-1` such successful return excursions is exactly `p(h)^{m-1}`. Dropping the extra requirement that `S_k` be a new site can only enlarge the event. Union-bounding over the `n+1` possible values of `k` gives (5.1). `square`

### Corollary 5.2 — arbitrary finite pattern via one witness

For any nonempty finite pattern `H` and any chosen `h\in H`,

\[
\partial_HR(n)\subseteq\partial_{\{h\}}R(n),
\qquad
M_H(n)\le M_{\{h\}}(n), \tag{5.2}
\]

so the same tail bound applies to `M_H(n)` with any chosen witness displacement `h in H`.

This is the useful extremal reduction: for an upper bound on a complicated moving pattern, one well-chosen forbidden translate is enough.

## 6. Source main regime: a universal in-probability upper constant

### Theorem 6.1

Fix `0<beta<1/2`. Let `\widetilde D_n` be any deterministic nonempty sequence of source-valid patterns satisfying the annular condition (2.1). Then for every `epsilon>0`,

\[
\boxed{
P\left(
\frac{M_{\widetilde D_n}(n)}{(\log n)^2}
>
\frac{4\beta}{\pi}+\epsilon
\right)\longrightarrow0.
} \tag{6.1}
\]

Combining this with the classical planar favorite-site law gives the stronger displayed form

\[
\boxed{
\limsup_{n\to\infty}^{P}
\frac{M_{\widetilde D_n}(n)}{(\log n)^2}
\le
\frac1\pi\min\{1,4\beta\},
} \tag{6.2}
\]

where (6.2) means that every threshold strictly above the right-hand side is exceeded with probability tending to zero.

#### Proof

Choose any deterministic `h_n\in\widetilde D_n`. By (2.1),

\[
n^\beta<|h_n|\le2n^\beta,
\]

so (4.5) holds. Put

\[
m_n=\left\lceil\left(\frac{4\beta}{\pi}+\epsilon\right)(\log n)^2\right\rceil.
\]

Using Corollary 5.2 and `1-x<=e^{-x}`,

\[
\begin{aligned}
P(M_{\widetilde D_n}(n)\ge m_n)
&\le(n+1)(1-q(h_n))^{m_n-1}\\
&\le(n+1)\exp(-q(h_n)(m_n-1))\\
&=n^{-\epsilon\pi/(4\beta)+o(1)}\to0.
\end{aligned}
\]

This proves (6.1). Independently, `M_{\widetilde D_n}(n)<=\max_xK(n,x)` and the planar favorite-site theorem gives

\[
\frac{\max_xK(n,x)}{(\log n)^2}\to\frac1\pi
\quad\text{a.s.}
\]

Taking the better of the two upper bounds gives (6.2). `square`

### Interpretation

This theorem exposes a source-relevant candidate phase boundary at `beta=1/4` for the **upper** constant. It is not a proof of the source asymptotic: no matching lower bound is claimed. For `beta<1/4`, however, it is strictly stronger than the unrestricted favorite-site bound `1/pi`.

## 7. An almost-sure bound controlled by temporal displacement entropy

The obstacle to summing (6.1) over every `n` is not the spatial walk itself; it is the fact that the pattern is allowed to change with `n`. The next result isolates exactly how much temporal variation costs.

Choose once and for all a witness `h_n\in\widetilde D_n`. For dyadic `N_j=2^j`, set

\[
W_j:=\{h_n:N_j\le n<2N_j\},
\qquad
\rho:=\limsup_{j\to\infty}
\frac{\log|W_j|}{\log N_j}. \tag{7.1}
\]

Since every `h_n` lies in a lattice disk of radius `O(N_j^beta)` on such a block,

\[
0\le\rho\le2\beta. \tag{7.2}
\]

### Theorem 7.1

Under the hypotheses of Theorem 6.1,

\[
\boxed{
\limsup_{n\to\infty}
\frac{M_{\widetilde D_n}(n)}{(\log n)^2}
\le
\frac1\pi\min\{1,\,4\beta(1+\rho)\}
\quad\text{a.s.}
} \tag{7.3}
\]

Consequently, without any additional regularity of the moving pattern,

\[
\boxed{
\limsup_{n\to\infty}
\frac{M_{\widetilde D_n}(n)}{(\log n)^2}
\le
\frac1\pi\min\{1,\,4\beta(1+2\beta)\}
\quad\text{a.s.}
} \tag{7.4}
\]

The universal bound (7.4) is strictly better than `1/pi` whenever

\[
\beta<\frac{\sqrt3-1}{4}\approx0.1830127. \tag{7.5}
\]

If the witness displacement is block-frozen, or more generally if `|W_j|=N_j^{o(1)}`, then `rho=0` and (7.3) sharpens to the same upper constant `4beta/pi` as the fixed-time probability bound.

#### Proof

Fix any

\[
c>\frac{4\beta(1+\rho)}\pi.
\]

Let `N=2^j` and

\[
m_N=\lceil c(\log N)^2\rceil.
\]

Suppose that for some `n in [N,2N)` one has `M_{\widetilde D_n}(n)>=m_N`. Choose the prescribed `h_n in W_j`. Then there is a site `y` visited at least `m_N` times by time `n`, while `y+h_n` is unvisited by time `n`. If `k` is the first visit to `y`, then `k<2N` and after time `k` the walk makes at least `m_N-1` returns to `y` before its first hit on `y+h_n`.

Therefore, union-bounding over the at most `2N+1` possible first-visit times and all `h in W_j`,

\[
P\left(\exists n\in[N,2N):M_{\widetilde D_n}(n)\ge m_N\right)
\le
(2N+1)|W_j|\max_{h\in W_j}p(h)^{m_N-1}. \tag{7.6}
\]

Uniformly for `h in W_j`, one has

\[
N^\beta<|h|\le2(2N)^\beta,
\]

so by (4.4)

\[
q(h)=\frac{\pi}{4\beta\log N}+O_\beta((\log N)^{-2}). \tag{7.7}
\]

For every `eta>0`, the definition of `rho` gives eventually `|W_j|<=N^{rho+eta}`. Choose `eta>0` small enough that

\[
1+\rho+\eta<\frac{c\pi}{4\beta}.
\]

Equations (7.6)--(7.7) then give, for some `delta>0` and all sufficiently large `j`,

\[
P\left(\exists n\in[N,2N):M_{\widetilde D_n}(n)\ge m_N\right)
\le N^{-\delta}=2^{-\delta j}. \tag{7.8}
\]

The right side is summable in `j`. Borel--Cantelli therefore implies that almost surely, for all sufficiently large dyadic blocks,

\[
M_{\widetilde D_n}(n)<m_N
\quad\text{for every }N\le n<2N.
\]

Since `log n>=log N`, this yields

\[
\limsup_n\frac{M_{\widetilde D_n}(n)}{(\log n)^2}\le c
\quad\text{a.s.}
\]

Letting `c` decrease to `4beta(1+rho)/pi` and intersecting with the global favorite-site bound `1/pi` proves (7.3). The lattice-point estimate `rho<=2beta` gives (7.4). Solving `4beta(1+2beta)<1` yields (7.5). `square`

## 8. Section-B method accounting

### #1 — CHANGE THE CATEGORY

I replaced the moving generalized-boundary problem by a killed two-point excursion problem. Once a single forbidden translate `y+h` is selected, boundary local time becomes the number of returns to `y` before first hitting `y+h`, which is governed by the planar potential kernel. **Outcome:** exact tail (5.1), then the source-scale upper constants in Theorems 6.1 and 7.1.

### #12 — FIND WHAT IS CONSERVED

At every return to `y` before `y+h`, translation invariance and strong Markov reset exactly the same escape hazard

\[
q(h)=1/(2\mathfrak a(h)).
\]

That hazard is the invariant across excursions. **Outcome:** the local-time tail is genuinely geometric, not merely exponentially bounded by a soft large-deviation argument.

### #24 — FIND THE EXTREMAL OBJECT

For an upper bound, a complicated finite pattern is dominated by one witness displacement because `partial_H R subset partial_{\{h\}}R`. Across a dyadic block, the only additional price is the number of distinct witness displacements. Encoding that as `rho` identifies the extremal temporal-variation cost and yields the universal `rho<=2beta` corollary. **Outcome:** a quantitative almost-sure theorem in the main source regime, plus an explicit obstruction to getting the fixed-time constant uniformly for arbitrary rapidly varying patterns.

These methods are new on E0086 and do not repeat the prior run's #2/#6/#30 triple.

## 9. Dated literature / prior-art check

Search date: **2026-09-18**.

Primary source rechecked: Okada, arXiv:1606.03787, including the PDF page containing Open Problem 2. The source explicitly asks for the asymptotic in the annular `a_n=n^beta`, `0<beta<1/2` regime and separately displays the large-radius conjectural equality corrected in the preceding NM13-12 report.

Current/later-author scope checked with queries equivalent to:

- `"Topics and problems on favorite sites of random walks" Okada Open Problem 2`;
- `"favorite sites" random walk translated boundary Okada 2025 2026`;
- `"Open problem 2" "favorite sites" random walk Okada`;
- `"inner boundary" "favorite sites" random walk planar potential kernel`;
- `"translated boundary" random walk range favorite sites`.

A later author paper, Hao--Li--Okada--Zheng, *Favorite Sites for Simple Random Walk in Two and More Dimensions*, arXiv:2409.00995, studies the number/evolution of ordinary favorite sites; its stated results do not resolve this moving translated-boundary problem. The bounded search did not surface a source-matching later resolution of Open Problem 2 or the bounds proved here. This is **negative bounded evidence only**; publication novelty is **UNVERIFIED** and I do not claim worldwide openness from search failure.

For the potential-kernel input I checked Lawler--Limic, *Random Walk: A Modern Introduction*, Section 4.4: Proposition 4.4.1 gives the killed expected-visit identity behind (4.1), and Theorem 4.4.4 gives the simple-random-walk asymptotic (4.4). Thus the analytic input used above is standard potential theory, not a novelty claim.

## 10. Status, counters, audits, and next route

The parent E0086 source remains **PARTIAL / OPEN**. This run proves a source-relevant upper theorem in the main `0<beta<1/2` regime but does not determine the requested almost-sure asymptotic. In particular, no lower bound matching `4beta/pi` is proved, even for a singleton moving pattern.

The frozen metric did not move:

```text
C_large: 1/pi -> 1/pi
unchanged_runs: 0 -> 1
stuck_recoveries: 0 -> 0
```

This is only the first unchanged run after the metric movement, so Section I is **not** triggered.

Required closure audits remain:

```text
P26: NOT PASSED / no E0086 PASS recovered
NM13-13: NOT PASSED / no E0086 PASS recovered
```

The next high-value mathematical obligation is a **lower bound** in the simplest source-valid class, preferably a singleton or dyadically frozen displacement `h_n` with `|h_n|asymp n^beta`. The concrete target is to decide whether, for `beta<1/4`, one can prove

\[
\liminf\frac{M_{\{h_n\}}(n)}{(\log n)^2}\ge\frac{4\beta}{\pi}
\]

in probability or almost surely under an explicitly frozen regularity assumption before attempting arbitrary moving patterns. The next run should use fresh methods **#11 DUALIZE**, **#20 FIND WHY THE ALGORITHM FAILS**, and **#28 REPLACE FOR ALL WITH FOR TYPICAL**, unless intervening source/literature/ownership evidence changes the target.

No shared root, peer namespace, claim file, workflow, permission, public surface, email/Drive resource, paid compute, or schedule was modified in this invocation.

## 11. Structured ledger delta for P26

```yaml
ledger_delta:
  track: NM13-12
  category: HARD_OUTSIDE
  source_id: E0086
  claim_id: E0086
  canonical_dedup_key: favorite_sites::op_2
  status_before: PARTIAL
  status_after: PARTIAL
  metric_name: C_large
  metric_scope: source large-radius regime a_n >= n^(1/2+epsilon)
  metric_before: 1/pi
  metric_after: 1/pi
  movement: false
  methods_tried:
    - 1
    - 12
    - 24
  method_outcomes:
    1: reduced moving translated-boundary upper tail to a killed two-point excursion problem
    12: exact conserved excursion hazard q(h)=1/(2*potential_kernel(h))
    24: single-witness domination plus dyadic displacement-entropy bound
  new_source_relevant_results:
    - finite-time tail P(M_{h}(n)>=m) <= (n+1)*(1-1/(2*a(h)))^(m-1)
    - annular main-regime in-probability upper constant min(1,4*beta)/pi
    - almost-sure upper constant min(1,4*beta*(1+rho))/pi where rho is dyadic witness-displacement entropy
    - universal almost-sure corollary min(1,4*beta*(1+2*beta))/pi
  unchanged_runs_before: 0
  unchanged_runs_after: 1
  stuck_recoveries_before: 0
  stuck_recoveries_after: 0
  audits:
    P26: NOT_PASSED
    NM13-13: NOT_PASSED
  literature_check_date: 2026-09-18
  literature_result: no source-matching later resolution found in bounded search; novelty UNVERIFIED
  next_target: matching lower bound for singleton or dyadically frozen displacement in beta<1/4 regime
  next_methods:
    - 11
    - 20
    - 28
```
