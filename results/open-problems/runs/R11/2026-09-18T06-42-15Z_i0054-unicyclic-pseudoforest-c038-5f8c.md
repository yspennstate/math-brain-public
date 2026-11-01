Model: GPT-5.6 Sol. Reasoning: UNVERIFIED runtime level; GPT-6 / maximum was requested, but the exposed scheduler has no model-family or reasoning-effort selector, so GPT-6 / maximum is not verified or claimed. Metric movement: **`37 -> 38`** distinct nontrivial discrete model classes with complete author-side CTCS(infinity) limit proofs under the frozen equivalence convention. Section-B moves actually tried: **#8 (discretize the boundary mechanism into a finite graph assembly), #17 (recognize the logarithmic coefficient in classical unicyclic random graphs), #23 (use a graph-component mechanism rather than the proposer’s tree/subordinator mechanism)**.

# R11 / I0054 — C038 conditioned five-component unicyclic-pseudoforest fragmentation

Problem/source: David J. Aldous and Svante Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529v3, **Open Problem 18**, intake `I0054`. The source asks for superficially different **discrete** models having the same `CTCS(infinity)` limit and immediately asks whether the source's apparent subordinator approximation can arise in another discrete tree model. Overall source status remains **PARTIAL, not CLOSED** under the owner's protocol.

Repository / branch: `yspennstate/math-open-problems` / `master`. Dated source/literature check: 2026-09-18.

No email/Gmail, Drive, public posting, purchase, permission change, workflow execution, scheduler change, shared-root edit, or peer-track edit was performed.

---

## 1. Continuity, source, ownership, exact topology

I continued from

`runs/R11/2026-09-18T05-40-00Z_i0054-critical-window-ewens-u017-7a6d.md`,

which retained the metric at `37 -> 37`, proved `R11-I0054-U017`, and prescribed the nonrepeating method triple `#8/#17/#23`. I did not restart the class sequence or count another parameter value of an existing class.

Before new mathematics I reread/searched the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/claims/I0054.md`, `operations/NEW_METHODS_2026-09-16.md`, the newest R11 report, the earlier logarithmic-assembly C036 report, the growing-cycle C037 report, the neighbouring P13/I0051 retirement/ownership surface, and the current P26/R11 audit-search surface. The canonical I0054 record still says owner R11 and `PENDING_ADMISSION, not READY`. P13's former Open Problem 9 clade project is distinct and has been retired/rotated; it is not reassigned here. R11's former planar self-avoiding-walk route remains retired.

The current source is arXiv:2303.02529v3, last revised 18 April 2025. Printed page 58 states Open Problem 18:

> Are there superficially different discrete models whose limit is the same CTCS(infinity)?

and immediately asks whether the apparent subordinator approximation can arise in another discrete tree model. The source abstract states that `CTCS(infinity)` is formalized via exchangeable partitions. I therefore retain the frozen strong target used throughout R11: for every fixed `k` and every finite time horizon, convergence of the **entire restriction path** in `D([0,T], P_k)` with Skorokhod `J_1`, followed by convergence in the projective finite-restriction topology. No root-only, tagged-lineage, or fixed-time marginal surrogate is used.

A fresh bounded current-literature search found no announced resolution of exact Open Problem 18. The nearby 2026 results surfaced were Chorbadzhiyska--Minchev--Savov, arXiv:2608.18320 (18 August 2026), which studies the beta-splitting family via homogeneous fragmentations/subordinators and resolves a height problem at the critical parameter, and Heng Ma's September 2026 fragmentation work on extremal separation/clade-count dynamics. This is a bounded negative search, not a novelty certificate.

A current repository search still recovers no qualifying present-package `P26-AUDIT-R11-I0054` end-to-end PASS and no second complete present-package OTHER-track end-to-end PASS. Hence this run cannot close the source problem under the owner's protocol.

### Runtime/model control

The runtime identifies as GPT-5.6 Sol; reasoning effort is not exposed and is therefore `UNVERIFIED`. The exposed scheduler surface has prompt/title, schedule, enabled state, and timing mode, but no model-family selector, reasoning-effort selector, authenticated runtime-routing telemetry, or guaranteed hour-long execution. GPT-6/maximum therefore remains prompt-only. Repository history says a historical P26 `You cannot modify this task` denial later succeeded from an authorized context, whereas another context denied R-series edits. The legitimate repair for any still-denied task is the owning authorized workspace/account surface or platform support exposing those controls, not cloning or bypassing the task. No scheduler modification was attempted.

---

## 2. Move #8 — discretize the logarithmic boundary into a finite graph assembly

U017 identified the `R_N ~ c log N` permutation boundary as an Ewens/PD fragmentation and suggested leaving conditioned permutations. The new route is a finite **graph** object.

Let `T(z)` be the exponential generating function of rooted labelled trees,

\[
T(z)=ze^{T(z)}
=\sum_{n\ge1}n^{n-1}\frac{z^n}{n!}.
\tag{2.1}
\]

A connected labelled **simple unicyclic graph** is an undirected cycle of length at least three with a rooted labelled tree attached at every cycle vertex. Its connected-component EGF is therefore

\[
\boxed{
U(z)
=\frac12\left(
\log\frac1{1-T(z)}-T(z)-\frac{T(z)^2}{2}
\right).
}
\tag{2.2}
\]

Fix `R=5`. For every `N>=15`, let `G_N` be uniform over the labelled simple graphs on `[N]` having exactly five connected components, **each component unicyclic**. Equivalently, `G_N` is uniform on the labelled assembly `SET_5(U)`.

This is a finite discrete graph model; it is not an infinite paintbox or a permutation cycle partition.

---

## 3. Move #17 — the classical `1/4` unicyclic coefficient supplies the CTCS beta shadow

The dominant singularity of `T` is

\[
\rho=e^{-1}.
\]

The standard tree-function expansion is

\[
T(z)=1-\sqrt{2(1-z/\rho)}+O(1-z/\rho).
\tag{3.1}
\]

Hence

\[
1-T(z)=\sqrt{2(1-z/\rho)}\,(1+O(\sqrt{1-z/\rho})),
\]

so (2.2) gives

\[
\boxed{
U(z)=\frac14\log\frac1{1-z/\rho}+O(1)
}
\tag{3.2}
\]

in a standard Delta-domain. Differentiating the singular expansion, for every fixed `m>=1`,

\[
\boxed{
U^{(m)}(z)
=\frac14\frac{(m-1)!}{\rho^m}
(1-z/\rho)^{-m}(1+o(1)).
}
\tag{3.3}
\]

Thus this graph class satisfies the exact hypotheses of the previously proved author-side theorem `R11-I0054-U015` (fixed-component logarithmic-assembly universality), with `theta=1/4`, `rho=e^{-1}`, and `R=5`.

The coefficient `1/4` is classical rather than claimed as new. It also appears in the random-graph literature: Janson's work on cycles/unicyclic components has Poisson--Dirichlet/GEM parameter `1/4`, and Ben-Naim--Krapivsky obtain the critical unicyclic size tail `U_k ~ 1/(4k)`, implying logarithmically many unicyclic components. This was the useful numerical fingerprint that pointed to (2.2)--(3.3).

For completeness, U015 gives the exact specified-visible-partition count. If

\[
\pi=\{B_1,\ldots,B_q\},\qquad |B_a|=n_a,\quad b=\sum_an_a,
\]

then

\[
A_{N,5}(\pi)
=(N-b)![z^{N-b}]
\left(\prod_{a=1}^q U^{(n_a)}(z)\right)
\frac{U(z)^{5-q}}{(5-q)!},
\tag{3.4}
\]

with denominator

\[
A_{N,5}=N![z^N]\frac{U(z)^5}{5!}.
\tag{3.5}
\]

The logarithmic transfer theorem and (3.2)--(3.3) therefore yield

\[
\boxed{
\Pr_N(\pi)
\sim
\frac{4!}{(5-q)!}
\frac{\prod_{a=1}^q(n_a-1)!}{(b-1)!}
(\log N)^{1-q}.
}
\tag{3.6}
\]

For a specified binary support of sizes `i,j`,

\[
\boxed{
\Pr_N(i|j)
\sim \frac{4}{\log N}B(i,j),
\qquad
B(i,j)=\frac{(i-1)!(j-1)!}{(i+j-1)!}.
}
\tag{3.7}
\]

---

## 4. C038 and complete finite-restriction path convergence

Define the exact two-label separation probability

\[
p_{11,N}
:=\Pr\{1,2\text{ lie in different components of }G_N\},
\qquad
\lambda_N:=p_{11,N}^{-1}.
\tag{4.1}
\]

By (3.7),

\[
\lambda_N\sim\frac{\log N}{4}.
\tag{4.2}
\]

Let one raw step have duration

\[
\delta_N=N^{-2}.
\tag{4.3}
\]

**C038** is the following hierarchy. At every raw step, independently for each current nonsingleton block `B`:

1. attempt with probability `a_N=delta_N lambda_N`;
2. on success draw a fresh independent `G_N`;
3. replace `B` by its nonempty intersections with the five connected components of `G_N`;
4. if all labels of `B` lie in one ambient component, the attempt is invisible;
5. all children begin attempting at the next raw step.

### 4.1 Exact legality, without asymptotics

Every connected simple unicyclic graph has at least three vertices. Conditional on a component-size vector

\[
s_1+\cdots+s_5=N,\qquad s_r\ge3,
\]

label exchangeability gives

\[
\Pr\{1,2\text{ separated}\mid(s_r)\}
=\frac{N^2-\sum_rs_r^2}{N(N-1)}.
\tag{4.4}
\]

The sum of squares is maximized at `(N-12,3,3,3,3)`, so

\[
\boxed{
p_{11,N}\ge
\frac{12(2N-15)}{N(N-1)}.
}
\tag{4.5}
\]

Thus `lambda_N` is finite and `delta_N lambda_N<1` for every `N>=15`; C038 is a legitimate finite stochastic hierarchy.

### 4.2 Exact hidden-label lumping

A fixed visible block is always contained in a unique full carrier. If a full proposal fragments that carrier but all visible labels remain in one ambient graph component, the visible state is unchanged and all visible labels pass into one child. The next proposal for that child is fresh and has the same attempt probability because the proposal law depends only on global `N`, not on hidden carrier size. If a visible split occurs, distinct visible children subsequently receive independent proposal streams.

Therefore each fixed restriction is itself exactly Markov, with one-block refinement probabilities given by (3.4)--(3.5). Hidden labels introduce no residual state.

### 4.3 Generator convergence

For a specified binary visible split,

\[
\lambda_N\Pr_N(i|j)\longrightarrow B(i,j).
\tag{4.6}
\]

For every fixed specified `q`-block refinement with `q>=3`, (3.6) and (4.2) give

\[
\lambda_N\Pr_N(\pi)=O((\log N)^{2-q})\longrightarrow0.
\tag{4.7}
\]

Hence for every fixed restriction `[k]`, its finite-state generator satisfies

\[
Q_N^{(k)}\longrightarrow Q_{\rm CTCS}^{(k)}
\tag{4.8}
\]

entrywise and therefore in finite-dimensional operator norm.

With at most `k` visible carriers, simultaneous attempts contribute only

\[
O_k((\delta_N\lambda_N)^2)
\]

per raw step. Thus

\[
P_N^{(k)}
=I+\delta_NQ_N^{(k)}+R_N^{(k)},
\qquad
\|R_N^{(k)}\|_{\rm row,1}
=O_k(\delta_N^2\lambda_N^2).
\tag{4.9}
\]

Over a bounded interval `[0,T]` the accumulated error is

\[
O_{k,T}(\delta_N\lambda_N^2)
=O_{k,T}\left(\frac{(\log N)^2}{N^2}\right)
\longrightarrow0.
\tag{4.10}
\]

The grid mesh `delta_N` also tends to zero. Finite-state uniformization/maximal coupling first couples the raw-step restriction to the continuous-time chain with generator `Q_N^{(k)}`, and generator convergence (4.8) then couples that chain to `CTCS(k)`. Moving a unique grid jump by at most `delta_N` gives the Skorokhod control. Therefore, for every fixed `k` and finite `T`,

\[
\boxed{
\Pi_{N,038}^{[k]}\Longrightarrow\Pi_{\rm CTCS}^{[k]}
\quad\text{in }D([0,T],\mathcal P_k),\ J_1.
}
\tag{4.11}
\]

Exact restriction consistency then gives

\[
\boxed{
\Pi_{N,038}\Longrightarrow\Pi_{\operatorname{CTCS}(\infty)}
}
\tag{4.12}
\]

in the frozen projective finite-restriction topology. This is convergence of the complete partition-valued genealogy, not a root marginal.

Every nonsingleton block eventually splits almost surely because any fixed pair has strictly positive separation probability on each fresh successful proposal. Thus C038 produces a finite rooted hierarchy/tree for every `N>=15`.

---

## 5. Move #23 — finite graph components, not the proposer’s tree/subordinator mechanism

The source itself asks whether its subordinator mechanism can arise in another discrete tree model. C038 reaches the same limiting hierarchy by a different finite mechanism: recursively resampling **five-component simple unicyclic graphs** and intersecting current blocks with their graph connected components.

The finite non-equivalence witness is rigid. At the first successful full-root proposal, all five ambient components are nonempty, so

\[
\boxed{\Pr\{\deg(\text{full root})=5\}=1}
\tag{5.1}
\]

for every `N>=15`.

At the minimum size `N=15`, every unicyclic component has at least three vertices, hence the root component-size multiset is deterministically

\[
\boxed{(3,3,3,3,3)}.
\tag{5.2}
\]

Each size-three component is a triangle, and the exact number of full-root graphs is

\[
\boxed{
\frac{15!}{(3!)^5 5!}=1,401,400.
}
\tag{5.3}
\]

Root arity and this support law are invariant under deterministic leaf relabeling and global time/branch-length rescaling. Earlier retained binary classes have degree two; C034/C035 have deterministic degree three; C036 has deterministic degree four; C037 has deterministic root degree `R_N` diverging with `N` rather than the constant five. The earlier R11 reports record strict-subunit fixed multifurcation witnesses for older nonbinary classes. Thus C038 is a new class under the frozen convention, not merely a relabeling/rescaling or a parameter specialization of the preceding classes.

---

## 6. Exact finite self-check

Only after the route and proof were established did I build the finite checker:

`artifacts/R11/2026-09-18T06-42-15Z_i0054-unicyclic-pseudoforest-c038_checker.py`

created and read back at commit

`c21e04ca5a8d1bd143b9adfe359afca1448a9cfb`.

Its executed output is

`artifacts/R11/2026-09-18T06-42-15Z_i0054-unicyclic-pseudoforest-c038_checker.out`

created and read back at commit

`96a7cd96f1263f312ec11ac567a86a64a777d7cb`.

The checker performs **1,105 exact rational-arithmetic checks** and ends

`ALL_EXACT_CHECKS_PASS`.

It verifies:

1. the EGF (2.2) against an independent direct enumeration formula for connected labelled simple unicyclic graphs through `N=30`; the first counts are `1,15,222,3660,68295,1436568,33779340,880107840` for `n=3,...,10`;
2. the exact `SET_5(U)` assembly counts;
3. the exact visible-partition counting formula (3.4) and complete normalization for every set partition of `b=2,3,4,5`, for every `N=15,...,26`;
4. exact two-label separation and the deterministic bound (4.5);
5. legality of `delta_N lambda_N` on that finite range;
6. the minimum-size root witness `(3,3,3,3,3)` and exact count `1,401,400`;
7. finite exact diagnostics of the pair-normalized binary rates at `N=30`.

The asymptotic theorem is proved on the page from (3.1)--(4.12); the finite diagnostics are a self-check, not the proof of convergence.

---

## 7. Prior art and novelty qualification

The combinatorial ingredients are classical. Connected labelled unicyclic graphs, their cycle-of-rooted-trees EGF, and unicyclic random-graph asymptotics are not claimed as new. In particular, Svante Janson's 2003 work studies cycles and unicyclic components and obtains Poisson--Dirichlet/GEM parameters including `1/4`; Ben-Naim--Krapivsky (2004) obtain the critical tail `U_k ~ 1/(4k)` and logarithmic growth in the number of unicyclic components.

A fresh bounded search for combinations of `unicyclic`, `fragmentation`, `CTCS`, `critical beta-splitting`, and Open Problem 18 did not surface the recursive conditioned-five-component construction above or an announced resolution of exact Open Problem 18. That negative search does not certify publication novelty. The potentially new content is the use of this finite graph assembly as a recursive discrete hierarchy together with the whole-path CTCS(infinity) limit, not the classical graph enumeration.

---

## 8. Status and metric

The stable new author-side claim is

\[
\boxed{\texttt{R11-I0054-C038 = PROVED\_AUTHOR\_SIDE under frozen equivalence}.}
\]

Therefore the frozen metric moves

\[
\boxed{37\to38}.
\]

I do **not** call Open Problem 18 closed. The canonical ownership record remains `PENDING_ADMISSION, not READY`; no qualifying current-package P26 end-to-end PASS and no second independent current-package OTHER-track PASS are recovered. The honest source-level campaign label remains **PARTIAL**.

The next nonrepeating methods are **#9, #13, #30**. The strongest next target is not another fixed logarithmic assembly: try to characterize which **growing-component** unicyclic assemblies retain the CTCS tangent, localize the first obstruction to a finite visible partition, and determine whether the permutation threshold `R_N=o(log N)` is universal across logarithmic assemblies or genuinely model-dependent.

---

## ledger_delta

```yaml
track: R11
source: I0054
source_status: PARTIAL
claim_added: R11-I0054-C038
claim_status: PROVED_AUTHOR_SIDE
metric_name: distinct_nontrivial_discrete_model_classes_with_complete_limit_proof
metric_before: 37
metric_after: 38
movement: 1
methods_used: [8, 17, 23]
next_methods: [9, 13, 30]
checker: artifacts/R11/2026-09-18T06-42-15Z_i0054-unicyclic-pseudoforest-c038_checker.py
checker_commit: c21e04ca5a8d1bd143b9adfe359afca1448a9cfb
checker_output: artifacts/R11/2026-09-18T06-42-15Z_i0054-unicyclic-pseudoforest-c038_checker.out
checker_output_commit: 96a7cd96f1263f312ec11ac567a86a64a777d7cb
exact_checks: 1105
audit_status:
  p26_end_to_end: missing
  second_other_track_end_to_end: missing
ownership: PENDING_ADMISSION
stagnation: reset_by_metric_movement
novelty: UNVERIFIED
```
