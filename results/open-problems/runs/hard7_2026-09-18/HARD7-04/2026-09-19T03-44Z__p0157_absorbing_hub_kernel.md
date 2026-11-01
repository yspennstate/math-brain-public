Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. HARD7-04 frozen metric has no movement, `Q_m=m^{-1}+O(m^{-2})->0` before and after; methods B7 / B19 / B29.**

# HARD7-04 bounded research iteration — P0157 absorbing hub kernel

Date: 2026-09-19 UTC. Repository/branch: `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / source OPEN.** The previous run refuted the over-strong universal one-hub route, not van der Hofstad's source question. This run follows its prescribed new direction: replace the scalar `d_max/delta` route by a marked upper-tail interaction object. The substantive result is an exact rank-one hub kernel in an absorbing branching surrogate together with a graph-level sufficient criterion preventing mergers among a chosen high-degree tail set.

## 1. Continuity and repository state

I resumed canonical claim `operations/claims/P0157.md`, owned exclusively by HARD7-04. I did not restart admission and did not return to I0049.

Before doing new mathematics I reread/recovered:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/claims/P0157.md`;
- the full indexed HARD7-04 checkpoint chain, with newest predecessor `2026-09-19T02-30Z__p0157_multihub_route_refutation.md`;
- the preceding graph theorem `artifacts/hard7_2026-09-18/HARD7-04/p0157_finite_population_hub_lln.md`;
- newest neighboring HARD7-03 checkpoint `20260919T0325Z__d0025-general-k-site-disorder-plateau.md`;
- newest neighboring HARD7-05 checkpoint `2026-09-19T0252Z__stuck1_endpoint_consistency.md`;
- repository-wide `P0157`, source-phrase, owner, and alias searches.

The intake collections are too large to render byte-for-byte through the connector in one response, so I used the indexed queue/intake entries plus canonical claim and alias searches rather than pretending a literal full-file read. No release, collision, posted equivalent, or competing owner surfaced. P0157 remains HARD7-04's active target.

## 2. Source and current-literature refresh

Primary source rechecked directly:

Remco van der Hofstad, *Stochastic processes on random graphs*, preliminary monograph dated **4 August 2026**, Notes on Section 8.3, printed p. 245 / PDF p. 255:

`https://rhofstad.win.tue.nl/Saint_Flour_SPoRG_Grundlehre.pdf`.

The page still explicitly calls the finite-third-moment subcritical configuration-model behavior an interesting open problem. It recalls Janson's strictly subcritical high-degree law, predicts persistence of the `d_max/(1-nu)` behavior sufficiently far below criticality when `d_max` is sufficiently large, contrasts it with the Erdős--Rényi barely-subcritical scale close to the `n^{-1/3}` window, and says this suggests a phase transition within the subcritical regime.

A bounded literature refresh dated 2026-09-19 used the source phrase and combinations of `barely subcritical configuration model`, `largest component`, `high degree vertices`, `connection probability`, and `finite third moment`. It again recovered:

- S. Janson, *The largest component in a subcritical random graph with a power law degree distribution*, Ann. Appl. Probab. 18 (2008), DOI `10.1214/07-AAP490`;
- M. Coulson and G. Perarnau, *Largest component of subcritical random graphs with given degree sequence*, arXiv `2111.11780`, EJP 28 (2023), DOI `10.1214/23-EJP921`;
- standard rank-one/in\-homogeneous-random-graph kernels as a nearby language, but no located source that closes van der Hofstad's exact finite-third-moment crossover question or supplies the two-sided marked-hub approximation needed below.

Coulson--Perarnau already give strong barely-subcritical upper bounds under their own assumptions; this run does not relabel such a solved regime as new. The negative search is bounded evidence only, not a novelty certificate.

## 3. Frozen metric — no movement

The admission metric remains

\[
Q_n=\frac{\operatorname{Var}(T_n)}{(d_{\max}/\delta_n)^2}
=\frac{\sigma_n^2}{d_{\max}\delta_n}.
\]

On the explicit multi-hub stress family of the preceding run,

\[
Q_m=m^{-1}+O(m^{-2})\to0.
\]

This run does not alter that scalar:

\[
\boxed{Q_m:m^{-1}+O(m^{-2})\to0\quad\longrightarrow\quad m^{-1}+O(m^{-2})\to0.}
\]

That is deliberate. The previous counterexample showed the scalar is too local: it certifies self-averaging for each hub but misses the multiplicity of comparable hubs. The new mathematics therefore studies the missing interaction structure without falsely renaming the metric.

## 4. B7 — take the limit: derive the absorbing hub kernel

Let `H` be any deterministic marked tail set and `B=[n]\\H`. Define

\[
S_H=\sum_{h\in H}d_h,
\qquad
A_H=\sum_{\{i,j\}\subset H}d_i d_j,
\]

and the bulk deficit after treating `H` as absorbing,

\[
\delta_H
=1-\frac1\ell\sum_{v\in B}d_v(d_v-1)
=\delta+\frac1\ell\sum_{h\in H}d_h(d_h-1).
\tag{4.1}
\]

Consider the ideal with-replacement branching exploration of a half-edge of hub `i`: a hit on target hub `j` is success, a hit on another marked stub is absorbing failure for that branch, and a bulk vertex `v` produces `d_v-1` descendants.

If `x_j` is the one-particle probability of eventually hitting `j`, then exactly

\[
x_j=\frac{d_j}{\ell}
+\frac1\ell\sum_{v\in B}d_v\{1-(1-x_j)^{d_v-1}\}.
\tag{4.2}
\]

Using

\[
rx-\binom r2x^2\le1-(1-x)^r\le rx
\]

and the finite-third-moment hypotheses gives, uniformly over marked targets,

\[
\boxed{x_j=\frac{d_j}{\ell\delta_H}(1+o(1)).}
\tag{4.3}
\]

The source assumptions imply

\[
\frac{d_{\max}}{\ell\delta^2}=o(1),
\qquad
\frac{d_{\max}^2}{\ell\delta}=o(1),
\]

so `d_i x_j=o(1)` uniformly. Starting the ideal process from the `d_i` root half-edges therefore yields

\[
\boxed{
 p^{\rm BP}_{ij}
 =\frac{d_i d_j}{\ell\delta_H}(1+o(1)).
}
\tag{4.4}
\]

Thus the first-order hub interaction kernel is rank one:

\[
\boxed{\kappa_{ij}=d_i d_j/(\ell\delta_H).}
\tag{4.5}
\]

This is an exact derivation in the absorbing branching surrogate, not a claim that actual CM hub connections are independent.

**B7 outcome:** successful. The heuristic `d_i d_j/(ell delta)` from the preceding run acquires the correct absorbing correction `delta_H` and a written proof in the canonical branching limit.

## 5. B19 — make it an algorithm: a graph-level marked-hub merger bound

The useful constructive question is: given a selected tail set `H`, can the actual configuration model certify that distinct marked hubs remain in distinct components?

The answer is yes under a concrete two-term condition. The new theorem proved in the artifact is

\[
\boxed{
\mathbb P(\exists\text{ component containing two vertices of }H)
\le
\frac{4A_H}{3\ell\delta_H}
+\frac{32S_H}{\ell\delta^2}
}
\tag{5.1}
\]

for all sufficiently large `n` under the source finite-third-moment/barely-subcritical assumptions.

The proof has two pieces.

**Short marked-to-marked paths.** Let `R=floor(ell delta/8)`. A shortest path between two marked vertices has all internal vertices in `B`. The exact configuration-model pairing probability gives

\[
E N_r
\le
\frac{A_H\{\ell(1-\delta_H)\}^{r-1}}
{(\ell-1)(\ell-3)\cdots(\ell-(2r-1))}.
\]

For `r<=R`, every denominator factor is at least `ell(1-delta/4)`, so summing the geometric series gives

\[
E\sum_{r\le R}N_r
\le\frac{A_H}{\ell(\delta_H-\delta/4)}
\le\frac{4A_H}{3\ell\delta_H}.
\tag{5.2}
\]

**Long paths.** Exploring from a marked root `h`, the exact active-half-edge drift satisfies

\[
b_t\le-\delta/2
\qquad(t\le\ell\delta/4)
\]

because total excess is `-ell delta` and every removed vertex has `d(d-2)>=-1`. Stopping at `tau_h wedge R` gives

\[
E(\tau_h\wedge R)\le 2d_h/\delta,
\]

and hence

\[
P(\tau_h>R)\le32d_h/(\ell\delta^2).
\tag{5.3}
\]

Union over `h in H` and combine with (5.2) to obtain (5.1).

Therefore

\[
\frac{A_H}{\ell\delta_H}\to0,
\qquad
\frac{S_H}{\ell\delta^2}\to0
\tag{5.4}
\]

is a rigorous sufficient **no-merger criterion** for the actual configuration model.

**B19 outcome:** successful. This is the first graph-level tail-profile condition on this track that distinguishes a family of many comparable hubs from a single maximal root. It is one-sided and therefore not yet the desired crossover theorem.

## 6. B29 — add the points at infinity: the missing boundary has two axes

For the previous explicit stress family

\[
n=8m^{12},\qquad M=m^5,\qquad d=m^2,
\qquad \ell\sim12m^{12},\qquad\delta\sim m^{-1},
\]

choose `H` to contain all `M` hubs. Then

\[
S_H=m^7,
\qquad
A_H\sim\tfrac12m^{14},
\qquad
\delta_H\sim m^{-1}.
\]

Two different kernel diagnostics emerge:

\[
\Lambda_H:=\frac{A_H}{\ell\delta_H}
\sim\frac{m^3}{24}\to\infty,
\tag{6.1}
\]

but

\[
\rho_H:=\frac{\sum_{h\in H}d_h^2}{\ell\delta_H}
\sim\frac1{12m^2}\to0.
\tag{6.2}
\]

So **global pair intensity diverges while every local hub degree vanishes**. This is the clean boundary that the scalar `H_n/E_n` could not see.

For equal hubs, the branching-kernel edge scale is

\[
p_m\sim\frac1{12m^7}.
\]

In the independent rank-one surrogate, the first-moment scale for a `k`-hub tree is

\[
M^k p_m^{k-1}\asymp m^{7-2k}.
\tag{6.3}
\]

Hence two-hub contacts have scale `m^3`, three-hub trees scale `m`, and four-hub trees scale `m^{-1}`. This points to a sharp **three-hub boundary object** for this family. It is a heuristic for the actual dependent graph, not a proof that `L_1/H_m` tends to three.

**B29 outcome:** successful as a route selector. The next proof obligation is now specific: establish a two-sided actual-CM approximation to the rank-one marked-hub graph, or at minimum prove the three-hub merger lower bound and four-hub exclusion for the explicit family.

## 7. What changed mathematically

The previous run showed that `d_max` and `delta` alone cannot yield a universal one-hub largest-component upper law. This run supplies the replacement structure rather than another scalar lemma:

1. the absorbing bulk has effective deficit `delta_H`;
2. its exact branching surrogate yields the rank-one kernel `d_i d_j/(ell delta_H)`;
3. the actual CM obeys the rigorous no-merger upper bound (5.1);
4. the previous stress family sits in the mixed regime `Lambda_H->infinity` but `rho_H->0`, exposing why fixed-hub and global-maximum statements diverge.

The complete theorem/proof artifact is

`artifacts/hard7_2026-09-18/HARD7-04/p0157_hub_connection_kernel.md`

created at commit `f631775d0878b9d7c72fd6caa55ea5f747115146` and read back successfully from that commit.

No finite exhaustive claim was made, so no checker was manufactured merely for bookkeeping. The theorem-sized arguments are on the page. They remain self-checks pending independent review.

## 8. Capability honesty

The scheduler capability situation is **still unchanged** in the exposed native interface. It permits title, prompt, schedule/timing mode and enabled state, but exposes no model selector, no reasoning-effort selector and no guaranteed run duration. GPT-6/maximum therefore remains a prompt request only. This invocation identifies as GPT-5.6 Sol; authenticated reasoning telemetry is unavailable, so the reasoning level is UNVERIFIED.

To make GPT-6/maximum a genuine scheduler guarantee rather than prompt text, the platform would have to expose and honor model and reasoning fields in the native automation schema (or platform support would have to change the task's runtime configuration). A repository edit cannot do that.

The historical `You cannot modify this task` result for a P26 scheduler ID is a permission/context issue. Repository state records that P26 was later editable from another authorized context. The correct workaround for any currently denied task is the authorized account/workspace/context or platform support; do not bypass the denial and do not create a duplicate task. I did not create, modify, disable, or reactivate any schedule.

## 9. Checkpoint / ledger delta

```yaml
ledger_delta:
  track: HARD7-04
  target: P0157
  source_status: OPEN
  worker_status: PARTIAL
  frozen_quantity: Q_n = sigma_n^2/(d_max*delta_n)
  before_on_stress_family: Q_m = m^-1 + O(m^-2) -> 0
  after_on_stress_family: Q_m = m^-1 + O(m^-2) -> 0
  movement: none
  methods: [B7, B19, B29]
  substantive_result_1: "absorbing branching surrogate has rank-one hub kernel kappa_ij = d_i*d_j/(ell*delta_H)(1+o(1))"
  substantive_result_2: "actual CM merger probability <= 4 A_H/(3 ell delta_H) + 32 S_H/(ell delta^2)"
  new_diagnostics: "Lambda_H=A_H/(ell delta_H), rho_H=sum_H d_h^2/(ell delta_H)"
  stress_family: "Lambda_H~m^3/24 -> infinity while rho_H~1/(12m^2) -> 0"
  artifact: artifacts/hard7_2026-09-18/HARD7-04/p0157_hub_connection_kernel.md
  artifact_commit: f631775d0878b9d7c72fd6caa55ea5f747115146
  next_obligation: "two-sided actual-CM marked-hub approximation; first explicit target: three-hub lower bound plus four-hub exclusion in the m-family"
  next_methods: [B4, B10, B16]
```

No shared root ledger was edited; the structured delta is for the designated maintainer. No email or Drive action was taken.
