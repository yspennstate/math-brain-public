Model: GPT-5.6 Sol. Reasoning: UNVERIFIED runtime level; GPT-6 / maximum was requested, but the exposed scheduler has no model-family or reasoning-effort selector, so GPT-6 / maximum is not verified or claimed. Metric movement: `35 -> 36` distinct nontrivial discrete model classes with complete author-side required-limit proofs under the frozen equivalence convention. Section-B moves actually tried: **#5 (add a parameter), #20 (find why the algorithm/generalization fails), #27 (swap the quantifiers)**.

# R11 / I0054 — U015 logarithmic-assembly compiler and C036 conditioned four-component 2-factor fragmentation

Problem/source: David J. Aldous and Svante Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529v3, **Open Problem 18**. The source asks whether superficially different discrete models can have the same `CTCS(infinity)` limit and immediately asks whether the source's subordinator mechanism can arise in another discrete tree model. Overall source status remains **PARTIAL, not CLOSED**. This run proves the structural theorem `R11-I0054-U015` and one new genuinely different discrete class `R11-I0054-C036` with a complete finite-restriction Skorokhod `J_1` / projective convergence proof and an executed exact checker.

Repository / branch: `yspennstate/math-open-problems` / `master`. Dated source/literature check: 2026-09-18.

No email/Gmail, Drive, public posting, purchase, permission change, workflow execution, scheduler change, shared-root edit, or peer-track edit was performed.

---

## 1. Continuity, source, ownership, topology, and current exclusions

I continued from

`runs/R11/2026-09-18T02-40-00Z_i0054-random-mapping-c035-6e21.md`,

which moved the metric `34 -> 35`, proved C035/U014, used `#1/#16/#25`, and recorded `#5/#20/#27` as the next triple. I did not restart or rederive the preceding model sequence.

Before new mathematics I reread/searched the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/claims/I0054.md`, `operations/NEW_METHODS_2026-09-16.md`, the newest R11 state, the neighboring P13/I0051 ownership history, and the current P26 audit-search surface. The canonical I0054 record still says owner R11 and `PENDING_ADMISSION, not READY`. P13's old Open Problem 9 clade-covariance target remains distinct and is now recorded as retired in the P13 successor history; it is not reassigned here. R11's old planar self-avoiding-walk route remains retired.

The current source PDF is arXiv:2303.02529v3, dated 17 April 2025 / posted as v3 on 18 April 2025. Printed page 58 states Open Problem 18 and asks for superficially different discrete models with the same `CTCS(infinity)` limit. The source abstract says `CTCS(infinity)` is formalized via exchangeable partitions. I therefore preserve R11's frozen strong convergence criterion: for every fixed `k` and finite `T`, the entire restriction path converges in `D([0,T], P_k)` with Skorokhod `J_1`, followed by convergence in the projective finite-restriction topology. No root-only or tagged-lineage surrogate is used.

A fresh bounded literature search found no announced Open Problem 18 resolution. The recent papers found were Chorbadzhiyska--Minchev--Savov, arXiv:2608.18320 (18 Aug 2026), on beta-splitting via homogeneous fragmentations/subordinators and a height problem, and Heng Ma, arXiv:2609.14329 (13 Sep 2026), which explicitly answers Aldous--Janson Open Problem 4. This is a bounded negative search, not a novelty certificate.

---

## 2. Move #5 — add a parameter: fixed component count in a logarithmic labelled assembly

The C034 permutation and C035 random-mapping calculations have the same hidden analytic shape. This run isolates it.

Let `C(z)` be the EGF of a labelled connected-component class. Assume that for some `rho>0`, `theta>0`, in a standard Delta-domain at `rho`,

\[
C(z)=\theta\log\frac1{1-z/\rho}+O(1),
\tag{2.1}
\]

and, for every fixed `m>=1`,

\[
C^{(m)}(z)
=\theta\frac{(m-1)!}{\rho^m}(1-z/\rho)^{-m}(1+o(1)).
\tag{2.2}
\]

Fix an integer `R>=2`. On `[N]`, sample uniformly from the labelled `SET_R(C)` class: exactly `R` connected components of type `C`.

For `b` distinguished visible labels and a **specified** visible set partition

\[
\pi=\{B_1,\ldots,B_q\},\qquad |B_a|=n_a,\quad q\le R,\quad \sum_a n_a=b,
\]

the labelled exponential formula gives the exact count

\[
\boxed{
A_{N,R}(\pi)
=(N-b)![z^{N-b}]
\left(\prod_{a=1}^q C^{(n_a)}(z)\right)
\frac{C(z)^{R-q}}{(R-q)!}.
}
\tag{2.3}
\]

The denominator is

\[
A_{N,R}=N![z^N]\frac{C(z)^R}{R!}.
\tag{2.4}
\]

Thus `p_{N,R}(pi)=A_{N,R}(pi)/A_{N,R}` is the exact visible restriction law.

The standard logarithmic transfer estimate is

\[
[z^n](1-z/\rho)^{-b}
\left(\log\frac1{1-z/\rho}\right)^m
\sim
\rho^{-n}\frac{n^{b-1}}{(b-1)!}(\log n)^m,
\tag{2.5}
\]

for fixed `b>=1,m>=0`. Also

\[
[z^N]\frac{C(z)^R}{R!}
\sim
\frac{\theta^R}{(R-1)!}\,\rho^{-N}\frac{(\log N)^{R-1}}{N}.
\tag{2.6}
\]

Substitution of (2.2) into (2.3), followed by (2.5), yields the structural restriction law

\[
\boxed{
p_{N,R}(\pi)
\sim
\frac{(R-1)!}{(R-q)!}
\frac{\prod_{a=1}^q(n_a-1)!}{(b-1)!}
(\log N)^{1-q}.
}
\tag{2.7}
\]

The singular amplitude `theta` and radius `rho` cancel completely.

In particular, for one specified unordered binary support `A|A^c`, `|A|=i`, `|A^c|=j`,

\[
\boxed{
p_{N,R}^{(2)}(i,j)
\sim \frac{R-1}{\log N}B(i,j),
\qquad
B(i,j)=\frac{(i-1)!(j-1)!}{(i+j-1)!}.}
\tag{2.8}
\]

For `q>=3`, a specified `q`-block visible refinement has probability of order `(log N)^{1-q}`.

This is the core of **U015: fixed-component logarithmic-assembly universality**.

---

## 3. Move #20 — identify the actual boundary instead of counting a parameter variation

The first obvious consequence of (2.7) is that C035 itself extends from three conditioned random-mapping components to every fixed `R>=2`. I checked that extension exactly in a separate exploratory checker. But I do **not** count `R=4 random mappings` as a new model class: it is only a parameter specialization of the already-counted C035 mechanism, and counting it would game the frozen metric.

The same calculation identifies two genuine boundaries.

1. `R=1` fails completely: there is never a nontrivial root split.
2. The proof above is **fixed-R**. It does not justify a growing component count `R=R_N`; the transfer estimates and constants in (2.7) were not proved uniformly in `R`. No growing-R claim is made.

So the useful conclusion is not an infinite tally of `R` values. It is the universality theorem: **any genuinely different logarithmic labelled assembly with a fixed component count has the same binary beta shadow after the correct rare-event acceleration.**

The exploratory fixed-R random-mapping checker was actually executed and archived. Its corrected output records `500` exact checks and `ALL_EXACT_CHECKS_PASS`; it is supporting evidence for this boundary analysis, not a metric increment.

---

## 4. Move #27 — swap the quantifiers: prove the compiler first, then choose a genuinely different finite object

Instead of proving one more random-mapping instance, prove:

> For every fixed `R>=2` and every labelled component class satisfying (2.1)--(2.2), every fixed finite visible restriction has the CTCS generator after normalization by its exact two-label separation probability.

Define

\[
p_{11,N}:=p_{N,R}^{(2)}(1,1),
\qquad
\lambda_N:=p_{11,N}^{-1}
\sim\frac{\log N}{R-1}.
\tag{4.1}
\]

Let raw-step duration be

\[
\delta_N=N^{-2}.
\tag{4.2}
\]

At every raw step, every current nonsingleton block attempts independently with probability

\[
a_N=\delta_N\lambda_N.
\tag{4.3}
\]

On an attempt, sample a fresh ambient `SET_R(C)` object on `[N]` and refine the block by the nonempty intersections with its `R` ambient connected components.

Exactly as in U014, hidden labels lump out: a visible block always lies in a unique full carrier; an invisible full refinement merely moves all visible labels into one child; the next proposal is fresh and the attempt probability depends only on global `N`. Hence each fixed visible restriction is itself exactly Markov and independent of hidden carrier sizes.

For a specified visible `q`-block refinement `pi`, its accelerated rate is

\[
\lambda_Np_{N,R}(\pi).
\tag{4.4}
\]

By (2.7)--(4.1), binary rates converge to

\[
\boxed{B(i,j),}
\tag{4.5}
\]

while for every fixed `q>=3`,

\[
\lambda_Np_{N,R}(\pi)
\sim
\frac{(R-2)!}{(R-q)!}
\frac{\prod_a(n_a-1)!}{(b-1)!}
(\log N)^{2-q}
\longrightarrow0.
\tag{4.6}
\]

For a fixed restriction `[k]`, let `Q_N^{(k)}` be the finite-state generator formed from one visible block refinement at a time. Then

\[
Q_N^{(k)}\longrightarrow Q_{\rm CTCS}^{(k)}
\tag{4.7}
\]

entrywise, hence in norm.

Multiple current blocks can attempt in one raw step, but with at most `k` visible blocks their total contribution is

\[
O_k(a_N^2)=O_k(\delta_N^2\lambda_N^2).
\tag{4.8}
\]

Thus the exact one-step kernel satisfies

\[
P_N^{(k)}
=I+\delta_NQ_N^{(k)}+R_N^{(k)},
\qquad
\|R_N^{(k)}\|_{\rm row,1}
=O_k(\delta_N^2\lambda_N^2).
\tag{4.9}
\]

Over `T/delta_N` steps the accumulated discrepancy is

\[
O_{k,T}(\delta_N\lambda_N^2)
=O_{k,T}\left(\frac{(\log N)^2}{N^2}\right)\to0.
\tag{4.10}
\]

The grid mesh `delta_N` tends to zero. A finite-state uniformization/maximal-coupling argument therefore couples the raw-step restriction to the continuous-time chain with generator `Q_N^{(k)}` with failure probability tending to zero on each bounded interval; finite-state generator convergence in (4.7) then couples that chain to `CTCS(k)`. Moving a unique grid jump by at most `delta_N` gives Skorokhod control. Hence

\[
\boxed{
\Pi_N^{[k]}\Longrightarrow\Pi_{\rm CTCS}^{[k]}
\quad\text{in }J_1
}
\tag{4.11}
\]

for every fixed `k` and finite time horizon. Exact restriction consistency then gives convergence to `CTCS(infinity)` in the frozen projective finite-restriction topology.

That completes U015.

---

## 5. C036 — conditioned four-component simple 2-regular graph / 2-factor hierarchy

Now instantiate U015 with a genuinely different combinatorial object.

A connected labelled simple 2-regular graph on `m>=3` vertices is an undirected `m`-cycle. There are `(m-1)!/2` such cycles. Therefore its connected-component EGF is

\[
\boxed{
C_2(z)
=\sum_{m\ge3}\frac{z^m}{2m}
=\frac12\left(\log\frac1{1-z}-z-\frac{z^2}{2}\right).
}
\tag{5.1}
\]

This is classical labelled-combinatorics machinery; I make no novelty claim for (5.1), random 2-factors, or logarithmic singularity analysis.

Equation (5.1) satisfies U015 with `rho=1`, `theta=1/2`. Fix `R=4`. For each `N>=12`, let `G_N` be uniform over all labelled **simple 2-regular graphs on `[N]` with exactly four connected components**. Define

\[
p_{11,N}=\Pr\{1,2\text{ lie in different components of }G_N\},
\quad
\lambda_N=p_{11,N}^{-1},
\quad
\delta_N=N^{-2}.
\tag{5.2}
\]

C036 is the following discrete hierarchy. At every raw step, independently for every current nonsingleton block `B`:

1. attempt with probability `delta_N lambda_N`;
2. on success draw a fresh independent `G_N`;
3. replace `B` by its nonempty intersections with the four connected components of `G_N`;
4. if all labels of `B` land in one component, the attempt is invisible;
5. children are processed starting at the next raw step.

The attempt probability is legitimate. Conditional on four component sizes `s_1+...+s_4=N`, each `s_i>=3`, two fixed labels are separated with probability

\[
\frac{N^2-\sum_i s_i^2}{N(N-1)}.
\tag{5.3}
\]

This is minimized at `(N-9,3,3,3)`, giving

\[
p_{11,N}\ge
\frac{9(2N-12)}{N(N-1)}.
\tag{5.4}
\]

Therefore `lambda_N=O(N)` even before asymptotics and `delta_N lambda_N<1`; U015 sharpens this to `lambda_N~(log N)/3`.

Every nonsingleton block eventually splits almost surely because any fixed pair has positive separation probability on every successful fresh proposal. Thus C036 defines a finite rooted hierarchy/tree for every `N>=12`.

From U015,

\[
\boxed{
\Pi_{N,036}^{[k]}\Longrightarrow\Pi_{\rm CTCS}^{[k]}
\text{ in }J_1\quad\forall k,
}
\tag{5.5}
\]

and therefore

\[
\boxed{
\Pi_{N,036}\Longrightarrow\Pi_{\operatorname{CTCS}(\infty)}
}
\tag{5.6}
\]

in the frozen projective topology.

This is not a root marginal: (5.5) is convergence of the complete finite-restriction path.

---

## 6. Exact finite non-equivalence witness

C036 has a particularly rigid finite witness.

At the full root `[N]`, every successful proposal has exactly four nonempty connected components, so the first proper root has degree exactly four with probability one. Relabeling and global branch/time rescaling preserve root degree. This already separates C036 from the source binary model and from C034/C035, whose full roots have degree three.

At the minimum size `N=12`, every simple 2-regular connected component has at least three vertices, so four components force the component-size multiset

\[
\boxed{(3,3,3,3)}
\tag{6.1}
\]

with probability one. The exact number of such labelled graphs is

\[
\boxed{
\frac{12!}{(3!)^4 4!}=15400.
}
\tag{6.2}
\]

The executed checker reproduces this count exactly. This finite support constraint is impossible in the conditioned-random-mapping family because mapping components may be singletons, and it is not a relabeling or time rescaling of the original model.

A repository search of preceding R11 finite witnesses finds degree-four vertices in some earlier variable-arity constructions (for example the Pitman--Yor and SC-nCRP routes) only as part of a nondegenerate arity law; C036's full-root degree is deterministically four and its `N=12` root-size support is the singleton `(3,3,3,3)`. I therefore credit one new model class, not the uncounted `R=4` random-mapping parameter variation.

---

## 7. Exact checker and executed evidence

The substantive C036 checker is

`artifacts/R11/2026-09-18T03-40-00Z_c036_2regular_checker.py`.

It was actually executed before archival. The archived output is

`artifacts/R11/2026-09-18T03-40-00Z_c036_2regular_checker.out`.

It performs **820 exact rational-arithmetic checks**. It verifies:

- the connected labelled cycle EGF coefficient `(m-1)!/2m! = 1/(2m)` through `m=30`;
- exact integer conditioned-four-component counts over `12<=N<=40`;
- the `N=12` four-triangle count `15400`;
- exact two-label same/different normalization and the deterministic pair-separation lower bound through `N=60`;
- `delta_N lambda_N<1` exactly through that range;
- complete exact visible set-partition normalization for `b=3,4` over `12<=N<=30`;
- exact finite normalized binary/multifurcation rates at `N=20,50,100,200`;
- the CTCS beta targets `B(1,2)=1/2`, `B(2,2)=1/6`.

The output ends

`ALL_EXACT_CHECKS_PASS`.

Creation/readback commits:

- checker: `aaa703eeea7ad176d20ec1c62d8ba5c4c19d9b7d`;
- output: `64a77d69671bd935c7b06f3ecba077a1e728945b`.

The exploratory fixed-R random-mapping checker/output are also preserved under `artifacts/R11/2026-09-18T03-40-00Z_c036_fixed_r_mapping_checker.*`. Its executed corrected output records `500` exact checks. No metric credit is taken for that parameter variation.

---

## 8. Prior-art qualification

Simple 2-regular graphs / 2-factors are classical. Standard labelled-combinatorics sources give exactly

\[
C_2(z)=\tfrac12(\log(1/(1-z))-z-z^2/2),
\]

and random-regular-graph literature routinely uses the fact that a 2-regular graph is a disjoint union of cycles. Those ingredients and the exponential formula are folklore/standard and are **not** claimed as new.

Likewise, C034 and C035 already showed two specific logarithmic assemblies (permutation cycles and random-mapping components). The potentially new result here is the source-facing **logarithmic-assembly compiler U015**, plus its use to produce this recursive conditioned-four-component 2-factor hierarchy and the whole-path CTCS limit. The bounded dated search found no paper announcing this construction or a solution of Open Problem 18. That negative search is not a novelty certificate.

---

## 9. Status, closure gate, and model-control issue

The stable author-side claims are

\[
\boxed{\texttt{R11-I0054-U015 = PROVED\_AUTHOR\_SIDE}}
\]

and

\[
\boxed{\texttt{R11-I0054-C036 = PROVED\_AUTHOR\_SIDE under frozen equivalence}.}
\]

The fixed metric therefore moves

\[
\boxed{35\to36}.
\]

I am **not** calling Aldous--Janson Open Problem 18 closed. The canonical claim still says `PENDING_ADMISSION, not READY`, and a fresh repository search still recovers neither a current-package `P26-AUDIT-R11-I0054` end-to-end PASS nor a second independent current-package OTHER-track PASS. Source-level campaign status remains **PARTIAL**.

The scheduler/model-control limitation is still unchanged. The exposed scheduler management schema offers title/prompt, schedule, timing mode and enabled state, but no model-family selector, reasoning-effort selector, authenticated completed-run model telemetry, or guaranteed-duration control. GPT-6/maximum therefore remains prompt text only. Enforcing it would require an authorized product/workspace control surface or platform/backend change exposing persistent model/reasoning fields plus per-run routing attestation. Historical `You cannot modify this task` responses, including P26, are authorization boundaries; the permitted remedy is the authorized owning context or platform support, not cloning or bypassing the task. No scheduler modification was attempted.

---

## 10. Structured ledger delta

```yaml
ledger_delta:
  worker: R11
  source: I0054
  source_status: PARTIAL
  metric_name: distinct_nontrivial_discrete_model_classes_with_complete_required_limit_proof
  metric_before: 35
  metric_after: 36
  movement: +1
  new_theorem: R11-I0054-U015
  new_model: R11-I0054-C036
  new_model_description: conditioned-four-component simple-2-regular-graph / 2-factor fragmentation
  proof_scope: full fixed-k J1 path convergence plus projective CTCS(infinity) convergence
  finite_checker: artifacts/R11/2026-09-18T03-40-00Z_c036_2regular_checker.py
  finite_checker_output: artifacts/R11/2026-09-18T03-40-00Z_c036_2regular_checker.out
  exact_checks: 820
  checker_result: ALL_EXACT_CHECKS_PASS
  audits_required: 2
  p26_current_package_audit: missing
  second_other_track_current_package_audit: missing
  closure: false
```

Next nonrepeating methods: **#6 (deform to a solvable point), #12 (find what is conserved), #24 (find the extremal object)**. The next research target is the boundary deliberately left open here: allow the ambient component count `R=R_N` to grow with `N`, derive the sharp uniform transfer regime, and decide the largest growth scale for which the CTCS binary generator survives while all higher-arity rates still vanish.
