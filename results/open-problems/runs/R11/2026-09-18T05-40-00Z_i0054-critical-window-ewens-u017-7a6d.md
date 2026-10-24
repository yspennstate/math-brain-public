Model: GPT-5.6 Sol. Reasoning: UNVERIFIED runtime level; GPT-6 / maximum was requested, but the exposed scheduler does not supply a model-family or reasoning-effort selector, so GPT-6 / maximum is not verified or claimed. Metric movement: **NO MOVEMENT, `37 -> 37`** distinct nontrivial discrete model classes with complete author-side CTCS(infinity) limit proofs under the frozen equivalence convention. Section-B moves actually tried: **#7 (take the critical limit), #18 (say the boundary process in Ewens/Poisson--Dirichlet language), #29 (compactify the phase parameter)**.

# R11 / I0054 — U017 critical-window Ewens boundary for conditioned permutations

Problem/source: David J. Aldous and Svante Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529v3, **Open Problem 18**. The source asks whether superficially different discrete models can have the same `CTCS(infinity)` limit and immediately asks whether the source's subordinator-like mechanism can arise in another discrete tree model. Overall source status remains **PARTIAL, not CLOSED**.

Repository / branch: `yspennstate/math-open-problems` / `master`. Dated source/literature check: 2026-09-18.

No email/Gmail, Drive, public posting, purchase, permission change, workflow execution, scheduler change, shared-root edit, or peer-track edit was performed.

---

## 1. Continuity, source, ownership, and exact topology

I continued from

`runs/R11/2026-09-18T04-40-41Z_i0054-growing-cycle-permutation-c037-7c41.md`,

which moved the fixed metric `36 -> 37`, proved `R11-I0054-U016` and `R11-I0054-C037`, and explicitly queued the nonrepeating method triple `#7/#18/#29`. I did not restart the class sequence or rederive earlier models.

Before new research I reread/searched the required campaign surfaces available through the GitHub connector:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/claims/I0054.md` and `operations/NEW_METHODS_2026-09-16.md`;
- the newest R11 report and the earlier Ewens/conditioned-permutation R11 reports;
- the neighboring P13/I0051 ownership/history surface;
- the current P26/R11 audit-search surface;
- targeted intake/queue hits for I0054;
- the current arXiv v3 source, recent later papers, and the closest classical Ewens/permutation-fragmentation literature.

The canonical I0054 claim still records R11 as owner and `PENDING_ADMISSION, not READY`. The old R11 planar self-avoiding-walk route remains retired. P13's old Aldous--Janson Open Problem 9 clade project is distinct and has since been retired/rotated; it is not reassigned here.

The current source is still arXiv:2303.02529v3, revised 18 April 2025. In Section 6.3 it asks:

> Are there superficially different discrete models whose limit is the same CTCS(infinity)?

and immediately asks whether the apparent subordinator approximation can arise in another discrete tree model. The paper formalizes `CTCS(infinity)` through consistent exchangeable partitions. I therefore retain the strong frozen convergence target used by R11 throughout: for every fixed `k` and finite `T`, convergence of the **entire restriction path** in `D([0,T],P_k)` with Skorokhod `J_1`, followed by convergence in the projective finite-restriction topology. No root-only or fixed-time marginal is substituted.

A fresh bounded literature screen found:

1. Chorbadzhiyska--Minchev--Savov, arXiv:2608.18320 (18 August 2026), treating beta-splitting via homogeneous fragmentations/subordinators and resolving a height problem, not Open Problem 18;
2. Heng Ma, arXiv:2609.14329 (13 September 2026), resolving Aldous--Janson Open Problem 4 on discrete-time height, not Open Problem 18;
3. Gnedin--Pitman, *Poisson representation of a Ewens fragmentation process* (arXiv:math/0608307), constructing an exchangeable consistent fragmentation with Ewens(theta) time marginals;
4. Goldschmidt--Martin--Spano, *Fragmenting random permutations* (arXiv:0712.0556), constructing a fragmentation whose `k`-block marginal is the cycle partition of a uniform permutation conditioned to have `k` cycles.

Thus Ewens partitions, Poisson--Dirichlet paintboxes, conditioned cycle partitions, and permutation fragmentations are classical prior art. The potentially new statement below is the **critical `R_N ~ c log N` limit of the R11 recursive conditioned-permutation hierarchy and its explicit interpolation between CTCS and instantaneous star-shattering**. I found no announced Open Problem 18 resolution in the bounded dated search. That negative search is not a novelty certificate.

A current exact repository search still recovers no qualifying present-package `P26-AUDIT-R11-I0054` end-to-end PASS and no second complete present-package OTHER-track PASS. Hence this run cannot close the source problem under the owner's protocol.

### Runtime/model control

The runtime identifies as GPT-5.6 Sol; reasoning effort is not exposed and is therefore `UNVERIFIED`. The exposed scheduler/update surface has prompt/title, schedule, enabled state and timing mode, but no model-family or reasoning-effort selector and no authenticated runtime-routing telemetry. GPT-6/maximum is prompt-only. Repository history records that a P26 edit that once returned `You cannot modify this task` later succeeded from an authorized context, whereas R-series edits were denied in another context. The legitimate remedy is therefore the owning authorized account/workspace surface or platform support that exposes the missing controls, not cloning or bypassing a denied task. No scheduler modification was attempted here.

---

## 2. Starting exact identity from U016

Let a uniform permutation of `[N]` be conditioned to have exactly `R=R_N` cycles. For integers `a>=1`, define

\[
E_r^{(a)}(N)
:=e_r\left(\frac1a,\frac1{a+1},\ldots,\frac1{N-1}\right).
\tag{2.1}
\]

For a fixed visible set of `b` labels and a **specified** visible cycle partition

\[
\pi=\{B_1,\ldots,B_q\},\qquad |B_j|=n_j,\quad \sum_jn_j=b,
\]

U016 proved the exact finite identity

\[
\boxed{
 p_{N,R}(\pi)
 =
 \frac{\prod_{j=1}^q(n_j-1)!}{(b-1)!}
 \frac{E_{R-q}^{(b)}(N)}{E_{R-1}^{(1)}(N)}.
}
\tag{2.2}
\]

For two visible labels,

\[
 p_{11,N}
 =\frac{E_{R-2}^{(2)}(N)}{E_{R-1}^{(1)}(N)},
\qquad
\lambda_N:=p_{11,N}^{-1}.
\tag{2.3}
\]

The preceding run proved that the pair-normalized hierarchy converges to CTCS exactly when `R_N=o(log N)`. It did not identify the limit on the sharp boundary `R_N ~ c log N`. That is the target of this run.

---

## 3. Move #7 — take the genuine critical limit `R_N/log N -> c`

Fix `a>=1`. The generating function of (2.1) is

\[
F_{a,N}(z)
:=\sum_{r\ge0}E_r^{(a)}(N)z^r
=\prod_{j=a}^{N-1}\left(1+\frac zj\right)
=\frac{\Gamma(N+z)\Gamma(a)}{\Gamma(N)\Gamma(a+z)}.
\tag{3.1}
\]

The coefficient asymptotic needed at logarithmic degree is the following.

### Lemma 3.1 (logarithmic-degree elementary-symmetric coefficient)

If `m_N/log N -> c` with `0<c<infinity`, then for each fixed integer `a>=1`,

\[
\boxed{
E_{m_N}^{(a)}(N)
=\frac{(\log N)^{m_N}}{m_N!}
  \frac{\Gamma(a)}{\Gamma(a+c)}
  (1+o(1)).
}
\tag{3.2}
\]

#### Proof

Put `L=log N` and `r_N=m_N/L`, so `r_N->c`. Introduce independent Bernoulli variables `X_j`, `a<=j<N`, with

\[
\Pr(X_j=1)=\frac{r_N}{j+r_N}.
\]

For `S_N=sum X_j`, the probability generating function is

\[
\mathbb E[t^{S_N}]
=\frac{F_{a,N}(r_Nt)}{F_{a,N}(r_N)},
\]

hence exactly

\[
\Pr(S_N=m_N)
=\frac{E_{m_N}^{(a)}(N)r_N^{m_N}}{F_{a,N}(r_N)}.
\tag{3.3}
\]

Because `r_N` remains in a compact subset of `(0,infinity)`, the digamma expansion gives

\[
\mu_N:=\mathbb ES_N
=\sum_{j=a}^{N-1}\frac{r_N}{j+r_N}
=m_N+O(1),
\tag{3.4}
\]

and

\[
\operatorname{var}S_N
=\sum_{j=a}^{N-1}\frac{r_Nj}{(j+r_N)^2}
=m_N+O(1).
\tag{3.5}
\]

The standard local central limit theorem for a triangular array of independent Bernoulli variables applies: the variance tends to infinity, the span is one, and no summand carries a nonvanishing fraction of the total variance. Since `m_N-mu_N=O(1)=o(sqrt(m_N))`,

\[
\Pr(S_N=m_N)
=\frac{1+o(1)}{\sqrt{2\pi m_N}}.
\tag{3.6}
\]

For `Z_N~Poisson(m_N)`, Stirling gives the same local probability,

\[
\Pr(Z_N=m_N)
=\frac{1+o(1)}{\sqrt{2\pi m_N}}.
\tag{3.7}
\]

Using `m_N=Lr_N`, equations (3.3), (3.6), and (3.7) yield

\[
\frac{E_{m_N}^{(a)}(N)}{L^{m_N}/m_N!}
=
F_{a,N}(r_N)e^{-Lr_N}
\frac{\Pr(S_N=m_N)}{\Pr(Z_N=m_N)}.
\tag{3.8}
\]

Finally, from the gamma-product form (3.1), uniformly for bounded `r_N`,

\[
F_{a,N}(r_N)e^{-Lr_N}
=\frac{\Gamma(N+r_N)}{\Gamma(N)N^{r_N}}
 \frac{\Gamma(a)}{\Gamma(a+r_N)}
\longrightarrow
\frac{\Gamma(a)}{\Gamma(a+c)}.
\tag{3.9}
\]

Substitution into (3.8) proves (3.2). `square`

### Critical-window restriction law

Now assume

\[
\boxed{\frac{R_N}{\log N}\longrightarrow c\in(0,\infty).}
\tag{3.10}
\]

Apply Lemma 3.1 to the numerator and denominator of (2.2). For fixed `q,b`,

\[
\frac{E_{R_N-q}^{(b)}(N)}{E_{R_N-1}^{(1)}(N)}
\sim
(\log N)^{1-q}
\frac{(R_N-1)!}{(R_N-q)!}
\frac{\Gamma(b)\Gamma(c+1)}{\Gamma(b+c)}.
\tag{3.11}
\]

Since

\[
(\log N)^{1-q}\frac{(R_N-1)!}{(R_N-q)!}
\longrightarrow c^{q-1},
\tag{3.12}
\]

(2.2) gives

\[
\boxed{
 p_{N,R_N}(\pi)
\longrightarrow
\frac{c^q\Gamma(c)}{\Gamma(c+b)}
\prod_{j=1}^q\Gamma(n_j).
}
\tag{3.13}
\]

The right side is exactly the **Ewens sampling formula with parameter `c`** for the specified partition `pi`.

This identifies the boundary rather than merely proving CTCS fails there.

In particular,

\[
p_{11,N}\longrightarrow\frac{c}{c+1},
\qquad
\lambda_N\longrightarrow\lambda_c:=\frac{c+1}{c}.
\tag{3.14}
\]

---

## 4. Move #18 — the limiting object is a Poisson--Ewens / PD(0,c) fragmentation

Say the result in partition language rather than permutation language.

Let `Pi_c` have the Ewens(`c`) partition law. Equivalently, on an infinite exchangeable block, `Pi_c` is the paintbox partition generated by a `PD(0,c)` mass partition. Give each current nonsingleton block proposal times from a Poisson process of rate

\[
\lambda_c=\frac{c+1}{c}.
\tag{4.1}
\]

At each proposal, independently refine that block according to a fresh Ewens(`c`) / `PD(0,c)` partition; a one-block restriction is simply invisible on that finite restriction.

For a specified nontrivial partition `pi={B_1,...,B_q}` of a block of size `b`, `q>=2`, the generator rate is

\[
\begin{aligned}
q_c(\pi)
&=\frac{c+1}{c}
  \frac{c^q\Gamma(c)}{\Gamma(c+b)}
  \prod_{j=1}^q\Gamma(n_j)\\
&=\boxed{
\frac{c^{q-2}\prod_{j=1}^q(n_j-1)!}
     {\prod_{r=2}^{b-1}(c+r)}
}.
\end{aligned}
\tag{4.2}
\]

(The denominator is an empty product when `b=2`.)

This normalization has a useful invariant: any specified pair of labels is separated at rate exactly one. That is immediate from `lambda_c * c/(c+1)=1`.

For a specified binary split of sizes `i,j`,

\[
\boxed{
q_c(i,j)
=\frac{(i-1)!(j-1)!}
       {\prod_{r=2}^{i+j-1}(c+r)}.
}
\tag{4.3}
\]

On three labels,

\[
q_c(1\mid 23)=\frac1{c+2},
\qquad
q_c(1\mid2\mid3)=\frac{c}{c+2}.
\tag{4.4}
\]

Thus every finite `c>0` is genuinely **not CTCS**: CTCS has the corresponding rates `1/2` and `0`. This gives a much more informative explanation of the U016 obstruction than the previous one-sided bound.

The process in (4.2) is a standard-type homogeneous exchangeable paintbox fragmentation driven by `PD(0,c)` dislocations. This language also clarifies the relationship to prior art: Gnedin--Pitman construct a different Ewens fragmentation whose **time marginals** are Ewens. Here Ewens/PD is the **jump dislocation law** of a recursive continuous-time fragmentation obtained as the critical boundary of conditioned permutations. I do not claim Ewens or PD machinery itself as new.

---

## 5. Whole-path convergence at the boundary

Use exactly the recursive finite model of U016, but now assume (3.10). Give one raw generation duration

\[
\delta_N=N^{-2}.
\tag{5.1}
\]

Each current nonsingleton full block attempts independently with probability

\[
a_N=\delta_N\lambda_N.
\tag{5.2}
\]

On an attempt, draw a fresh uniform permutation of `[N]` conditioned to have `R_N` cycles and refine the block by its nonempty intersections with those cycles.

The exact visible-lumping argument from U016 remains unchanged. A visible block lies inside one full carrier; a full refinement that keeps all visible labels in one ambient cycle is invisible and merely transfers those labels into one child. The next proposal is fresh and its attempt probability depends only on global `N`, not hidden carrier size. Therefore every fixed visible restriction is itself an exact time-homogeneous Markov chain.

For fixed `k`, (3.13)--(3.14) imply entrywise convergence of the finite-state generator:

\[
Q_N^{(k)}\longrightarrow Q_c^{(k)}.
\tag{5.3}
\]

Since `lambda_N -> lambda_c<infinity`, the one-step kernel satisfies uniformly over the finite partition state space

\[
P_N^{(k)}
=I+\delta_NQ_N^{(k)}+O_k(\delta_N^2).
\tag{5.4}
\]

Over `O(T/delta_N)` steps, the accumulated multiple-attempt/Euler discrepancy is `O_{k,T}(delta_N)->0`. A maximal coupling with the continuous-time chain generated by `Q_c^{(k)}` therefore succeeds on `[0,T]` with probability tending to one, and moving a discrete jump to the corresponding grid boundary changes its time by at most `delta_N`. Hence

\[
\boxed{
\Pi_{N}^{[k]}
\Longrightarrow
\Pi_c^{[k]}
\quad\text{in Skorokhod }J_1
}
\tag{5.5}
\]

for every fixed `k` and finite `T`.

The Ewens sampling formula is exactly deletion-consistent, so the generators `Q_c^{(k)}` are projectively consistent. Therefore the finite-restriction limits define one exchangeable fragmentation `Pi_c` on `N`, and

\[
\boxed{
\Pi_N\Longrightarrow\Pi_c
}
\tag{5.6}
\]

in the same projective finite-restriction path topology used for the CTCS claims.

---

## 6. Move #29 — compactify the boundary parameter

Formula (4.2) extends continuously to the two natural endpoints at the level of finite generators.

### Endpoint `c=0`: CTCS

For `q=2`,

\[
\lim_{c\downarrow0}q_c(\pi)
=\frac{(n_1-1)!(n_2-1)!}{(b-1)!}
=B(n_1,n_2),
\tag{6.1}
\]

while for every `q>=3`,

\[
\lim_{c\downarrow0}q_c(\pi)=0.
\tag{6.2}
\]

Thus

\[
\boxed{Q_c^{(k)}\longrightarrow Q_{CTCS}^{(k)}\quad(c\downarrow0)}.
\tag{6.3}
\]

This recovers U016 conceptually: `R_N=o(log N)` is precisely the approach to the `c=0` endpoint.

### Endpoint `c=infinity`: star-shattering

In (4.2), the numerator has degree `q-2` in `c` and the denominator degree `b-2`. Hence as `c->infinity`, every nontrivial rate vanishes unless `q=b`. For the all-singletons partition (`q=b`),

\[
q_c(\{1\}|\cdots|\{b\})\longrightarrow1.
\tag{6.4}
\]

So the compactified endpoint is the **star-shattering process**: every nonsingleton block waits an independent `Exp(1)` time and then disintegrates into singletons.

I am deliberately **not** claiming here that every finite conditioned-permutation regime with `R_N/log N -> infinity` converges to this endpoint; that would require a separate uniform coefficient analysis. The proved compactification concerns the explicit critical-window limit family `Q_c`, `0<c<infinity`, and its generator endpoints.

Combining Sections 3--6 gives the new theorem.

> **U017 (critical-window conditioned-permutation interpolation).**  Consider the pair-normalized recursive hierarchy whose fresh proposal on `[N]` is a uniform permutation conditioned to have exactly `R_N` cycles. If `R_N/log N -> c in (0,infinity)`, then the complete finite-restriction paths converge in `J_1`, and projectively, to the exchangeable Poisson--Ewens/`PD(0,c)` fragmentation with rates (4.2). This limit is not CTCS for any `c>0`. As `c downarrow 0`, its finite generators converge to the CTCS generator; as `c -> infinity`, the limiting generator family converges to star-shattering.

This sharpens U016 from an `if and only if` CTCS threshold into an explicit phase-boundary law.

---

## 7. Why the tracked metric does not move

The owner's metric counts **new discrete model classes whose required limit is CTCS(infinity)**.

U017 is a real theorem, but it does not create a 38th class:

- for every fixed `c>0`, the limit has a positive ternary rate `c/(c+2)` on three labels, so the required CTCS limit fails;
- the `c=0` approach is exactly the subcritical `R_N=o(log N)` regime already covered by U016/C037;
- counting a different subcritical sequence `R_N` as a new model would only be a parameter specialization of the already counted conditioned-permutation class;
- C002 and C019 already occupy other Ewens/CRP mechanisms, so relabelling the same boundary by Ewens terminology would also be metric gaming.

Therefore the honest fixed metric is

\[
\boxed{37\longrightarrow37\quad\text{(NO MOVEMENT).}}
\tag{7.1}
\]

This run is nevertheless non-stuck research: the preceding run moved the metric, and this run completely identifies the sharp boundary process rather than adding bookkeeping to an unchanged claim.

---

## 8. Exact finite self-check

A substantive exact-arithmetic checker was written **after** the new theorem route was obtained, executed, and archived as

`artifacts/R11/2026-09-18T05-40-00Z_i0054-u017-critical-window-checker.py`

creation commit

`4b829ad520dd986cf32da72d7c2dfde7e404a5b7`.

Its archived stdout is

`artifacts/R11/2026-09-18T05-40-00Z_i0054-u017-critical-window-checker.out`

creation/readback commit

`258ccc6ed40220751d424aed50f61ec64361acbc`.

It performs **36,625 exact checks** using only `fractions.Fraction` for arithmetic. In particular it:

1. exhaustively enumerates every permutation for `N=3,...,7` and verifies the exact conditioned restriction formula (2.2) for visible restrictions through four labels;
2. verifies exact Ewens(`c`) EPPF normalization on small labelled sets for `c=1/2,1,3/2,2`;
3. verifies the exact pair-separation probability `c/(c+1)`;
4. verifies the closed pair-normalized generator formula (4.2);
5. verifies the `c=0` binary CTCS endpoint and higher-arity vanishing order;
6. verifies the degree comparison that leaves only all-singletons at the `c=infinity` endpoint.

The output ends

`ALL_EXACT_CHECKS_PASS`.

Archived hashes:

- checker source SHA-256: `494c66a6c345626ba89a66bdaf68ec083483ab3a4bff468b16197637fc7e1fee`;
- stdout SHA-256: `65359e72c66280a6753eda85f9e85b130bf4506251f893801b0590352e00d3d2`.

This is a self-check, not an independent audit.

---

## 9. Claim/status and next route

New author-side claim:

\[
\boxed{\texttt{R11-I0054-U017 = PROVED_AUTHOR_SIDE}.}
\]

No new `C0xx` model claim is assigned because the fixed CTCS metric did not move.

Open Problem 18 itself remains **PARTIAL** under the campaign protocol. The required current-package P26 end-to-end audit and a second independent OTHER-track end-to-end audit are still not recovered, and the canonical ownership record is still `PENDING_ADMISSION, not READY`. The source's deliberately informal phrase “superficially different” also remains a source-intent issue for eventual external presentation.

The next nonrepeating methods are:

- **#8 (discretize):** seek a finite fixed-weight/set-partition or forest proposal whose low-order law converges to the `Q_c` dislocation family and then has a genuinely different `c downarrow 0` CTCS tangent, rather than another conditioned-permutation parameterization;
- **#17 (look for the same numbers elsewhere):** search labelled forests, assemblies, Stirling structures, and random set partitions for the exact denominator `prod_{r=2}^{b-1}(c+r)` and beta-kernel tangent;
- **#23 (do what the proposer did not expect):** deliberately avoid subordinators and permutations and ask whether a finite random-graph/component model has `Q_c` as a critical visible law, then take its `c downarrow0` tangent. A new metric class is counted only if its discrete mechanism is genuinely distinct under the frozen convention and the full projective `J_1` CTCS proof closes.

---

```yaml
ledger_delta:
  track: R11
  intake: I0054
  source: "Aldous--Janson arXiv:2303.02529v3 Open Problem 18"
  metric_name: "distinct nontrivial discrete model classes with complete CTCS(infinity) limit proof under frozen equivalence"
  before: 37
  after: 37
  movement: "NO MOVEMENT"
  status: PARTIAL
  new_claims:
    - id: R11-I0054-U017
      status: PROVED_AUTHOR_SIDE
      statement: "critical R_N/log N -> c conditioned-permutation hierarchy converges projectively in J1 to explicit Poisson--Ewens/PD(0,c) fragmentation; c downarrow 0 gives CTCS generator and c -> infinity gives star-shattering generator endpoint"
  new_model_class: null
  exact_checker:
    path: artifacts/R11/2026-09-18T05-40-00Z_i0054-u017-critical-window-checker.py
    output: artifacts/R11/2026-09-18T05-40-00Z_i0054-u017-critical-window-checker.out
    checks: 36625
    result: ALL_EXACT_CHECKS_PASS
  stagnation_count: UNKNOWN
  closure_blockers:
    - "canonical claim remains PENDING_ADMISSION, not READY"
    - "current-package P26 end-to-end PASS not recovered"
    - "second independent current-package OTHER-track end-to-end PASS not recovered"
    - "publication novelty/source-intent remains externally unverified"
  next_methods: [8, 17, 23]
```
