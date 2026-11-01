Model: GPT-5.6 Sol. Reasoning: UNVERIFIED runtime level; GPT-6 / maximum was requested, but the exposed scheduler has no model-family or reasoning-effort selector, so GPT-6 / maximum was not verified and is not claimed. Metric movement: `2 -> 3` distinct nontrivial discrete model classes with complete author-side CTCS(infinity) limit proofs under the frozen equivalence convention. Section-B moves actually tried: **22 (read failures / near-prior art), 23 (do what the proposer did not expect), 26 (hunt the sporadic finite case)**.

Problem/source: David J. Aldous and Svante Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529v3 (18 April 2025), **Open Problem 18**, intake `I0054`. Overall campaign status remains **PARTIAL**: the new mathematical claim `R11-I0054-C003` below is author-side **PROVED under the frozen equivalence convention**, but final prior-art/source-intent clearance and the two required OTHER-track closure audits are not complete.

# R11 I0054 — a near-critical ternary Gibbs/Dirichlet fragmentation tree converges to CTCS(infinity)

Run ID: `2026-09-16T18-41-35Z_i0054-gibbs-dirichlet-tangent-d3f7`  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Dated source/status check: 2026-09-16

No Gmail/email, Drive, public posting, paid compute, workflow execution, permission change, scheduler mutation, peer-file edit, or shared-root edit was performed.

---

## 1. Continuity, repository read, ownership, and runtime controls

I continued from the newest immutable R11 report rather than restarting:

`runs/R11/2026-09-16T17-42-08Z_i0054-ncrp-tangent-8b6e.md`.

That report proved `R11-I0054-C002`: the small-concentration standard nested Chinese restaurant process (SC-nCRP) has the whole CTCS(infinity) exchangeable-partition process as its accelerated-depth limit. The tracked metric moved `1 -> 2`; the two counted author-side classes before this run were:

1. `R11-I0054-C001`: harmonic-grid paintbox fragmentation (HGPF);
2. `R11-I0054-C002`: small-concentration nested Chinese restaurant process (SC-nCRP).

Before new research I read/searched the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the exclusive claim `operations/claims/I0054.md`, the I-intake ledger and exact I0054 repository hits, the newest R11 report, and the newest neighboring P13 clade-covariance report. The large JSONL intake surfaces are exposed through bounded connector views; I do **not** claim an invisible byte-for-byte manual reread of every roughly 780 intake rows. The exact I0054 source/ownership record and current neighboring ownership were checked.

`operations/claims/I0054.md` still says:

- Owner: R11, native task `6aa7b68c70c481919b1a131eb67b6b24`;
- Status: `PENDING_ADMISSION, not READY`;
- P13's Open Problem 9 / I0051 clade-covariance target is distinct.

I did not mutate this coordinator-owned claim. The direct owner prompt assigns I0054 to R11 and requires the missing research-side source/current-literature/prior-attempt/ownership checks to be completed; those checks were done in the two preceding R11 runs and refreshed here. I found no competing I0054 owner and no posted/settled exclusion.

The retired planar-SAW R11 history remains immutable, with its handoff at:

`runs/R11/2026-09-16T15-41-34Z_saw-stuck1-port-kp-5f72.md`.

### Actual model/scheduler controls

The actual runtime identifies this worker as GPT-5.6 Sol; reasoning level is not exposed and is therefore `UNVERIFIED`. The scheduler interface available to this context exposes title/prompt, schedule, enabled state and timing mode. It exposes **no model-family field and no reasoning-effort field**. Prompt text can request GPT-6 / maximum but cannot install or verify it.

The current operations policy records native modification probes returning `You cannot modify this task` in some contexts, including P26/P01/P03, and states not to bypass the restriction or clone jobs. The allowed repair is through an authorized task/account/workspace-owner interface that owns the existing native task, or platform support exposing/fixing the control. No scheduler change was attempted.

---

## 2. Exact source object and current-status screen

The current arXiv record remains v3, revised 18 April 2025. Open Problem 18 states:

> Are there superficially different discrete models whose limit is the same CTCS(infinity)?

The next sentence says that the key feature seems to be the subordinator approximation and asks whether it can arise in another discrete tree model.

I therefore continue to require convergence of the **whole CTCS(infinity) object**, not only a tagged fragment or one-dimensional subordinator.

Aldous--Janson Part III, arXiv:2412.09655, formalizes CTCS(infinity) by the nested exchangeable partition process

`(Pi(t), t>=0)`.

For each finite `n`, the restriction `(Pi^[n](t))` determines when every clade splits and how it splits; conversely CTCS(n) determines this partition process. Ignoring left/right order, the whole partition process determines the complete growth process and is another representation of CTCS(infinity).

For a particular finite partition `pi` of `[m]`, its CTCS jump rate is:

- `q_pi=0` if `|pi|>=3`;
- if `pi={A,A^c}`, `|A|=i`,
  `q_pi = B(i,m-i) = (i-1)!(m-i-1)!/(m-1)!`.

The total split rate of an `m`-block is `H_{m-1}`.

The explicit convergence topology used below is the same strong topology retained in C001/C002: `J_1` Skorokhod convergence on every finite partition restriction, assembled through the projective metric

`d_proj(omega,eta)=sum_{k>=1} 2^{-k}(1 wedge d_{J1,k}(omega^[k],eta^[k]))`.

This topology is my explicit formalization for convergence of the source's whole exchangeable-partition path; I do not attribute the name `projective J_1` to Aldous--Janson. It is strictly stronger than proving only a tagged or fixed-time marginal.

### Dated current-literature search

On 2026-09-16 I searched combinations including:

- `"Open Problem 18" CTCS Aldous Janson`;
- `"CTCS(infinity)" discrete model`;
- `"Gibbs fragmentation" "critical beta-splitting"`;
- `"Gibbs fragmentation tree" CTCS`;
- `"Dirichlet" fragmentation CTCS`;
- `"multifurcating" "critical beta-splitting"`;
- `"nested Chinese restaurant" CTCS beta-splitting`;
- recent critical-beta-splitting papers through September 2026.

The current source still prints Open Problem 18. Recent 2026 papers by Chorbadzhiyska--Minchev--Savov and Heng Ma study homogeneous-fragmentation asymptotics / extremal separation and clade dynamics, not an alternative finite discrete model convergence theorem answering Open Problem 18. A bounded negative search is **not** a worldwide novelty certificate.

The crucial older prior art found this run is McCullagh--Pitman--Winkel, *Gibbs fragmentation trees*, Bernoulli 14 (2008), 988--1002, arXiv:0704.0945. It supplies the natural model class used below. Importantly, Aldous--Janson v3 themselves cite this paper in their beta-splitting discussion and note that it characterizes the consistent binary Gibbs class. Thus this is not a literature connection the proposers were unaware of; the potentially new point is specifically the **multifurcating near-boundary accelerated limit**, which makes final source-intent scrutiny essential.

---

## 3. Move 22 — READ THE NEAR-PRIOR ART: the candidate already exists as a Gibbs fragmentation tree

McCullagh--Pitman--Winkel (MPW) study consistent Markovian fragmentation trees. Their Theorem 8 identifies the multifurcating Gibbs families with the two-parameter Ewens--Pitman / Poisson--Dirichlet models. In the finite-arity case they allow

`alpha_MPW < 0`, `theta_MPW = -q alpha_MPW`, `q>=3`,

and state that the associated dislocation measure is a symmetric finite-dimensional Dirichlet law

`Dirichlet(-alpha_MPW,...,-alpha_MPW)`.

Thus, writing

`epsilon = -alpha_MPW > 0`,

the `q`-ary model has a Dirichlet(`epsilon`,...,`epsilon`) paintbox at a branch point.

This matters for Open Problem 18: the third candidate is not an engineered discretization built from the CTCS dislocation measure. It is a named, published multifurcating Markov-branching model from 2008. Later work has even used Gibbs fragmentation trees as priors for hierarchical network models (for example Herlau--Morup--Schmidt, ICML 2013), providing an external modeling language unrelated to the critical beta-splitting program.

The new result below is the **near-boundary CTCS limit**, not the existence of Gibbs fragmentation trees themselves.

---

## 4. Move 23 — DO WHAT THE PROPOSER DID NOT EXPECT: leave the binary class

Before accepting the multifurcating model, I tested the most obvious binary version and rejected it.

Take `q=2` and a symmetric `Beta(epsilon,epsilon)` routing vector. MPW's binary characterization says the binary Gibbs models are exactly Aldous beta-splitting, with dislocation density proportional to

`x^beta (1-x)^beta dx`.

The `Beta(epsilon,epsilon)` density is proportional to

`x^(epsilon-1)(1-x)^(epsilon-1) dx`.

Hence

`beta = epsilon-1`.

So the binary Dirichlet route is simply the ordinary Aldous beta-splitting family approaching the critical value `beta=-1`; it is **not** a genuinely different model and is not counted.

The unexpected move is therefore to take fixed arity `q=3`. Finite trees then have genuine ternary vertices, even though the accelerated small-`epsilon` limit becomes binary because all three-way refinements are second order.

---

## 5. The ternary Dirichlet-environment discrete model

For each `N>=2`, set

`epsilon_N = 1/(2N)`,
`delta_N = 2 epsilon_N = 1/N`.

Take the infinite rooted ternary skeleton. At every node `u`, independently sample

`V_u=(V_{u,1},V_{u,2},V_{u,3}) ~ Dirichlet(epsilon_N,epsilon_N,epsilon_N)`.

Place `N` labelled particles at the root. Conditional on the environment, each particle at node `u` independently chooses child `j` with probability `V_{u,j}`. Repeat independently down the skeleton.

Let `Pi_N(r)` be the partition of `[N]` into common prefixes after `r` raw levels. Consecutive levels at which a sampled block remains unsplit are degree-one stretches. Give each raw level length `delta_N=1/N` and suppress degree-one vertices in the finite observed genealogy.

Define the rescaled càdlàg partition path

`hat Pi_N(t) := Pi_N(floor(N t))`.

This is a genuinely discrete-depth random tree model. Conditional on the random environment, it is a ternary random trie / split-tree construction; after suppressing no-change levels, its finite shape is exactly on MPW's `q=3`, `alpha_MPW=-epsilon_N`, `theta_MPW=3 epsilon_N` Gibbs-fragmentation ray.

I count the whole fixed-finite-arity Dirichlet/Gibbs mechanism as **one** model class; I do not inflate the metric by counting `q=4,5,...` separately.

---

## 6. Exact one-level partition law

Consider one current block containing `m` sampled labels. Let a **particular unlabeled set partition** of that block have `r<=3` parts `A_1,...,A_r`, with sizes `n_1,...,n_r`.

There are `3^{\underline r}=3!/(3-r)!` injections of these parts into distinct child labels. The Dirichlet moment formula gives

`E[prod_{l=1}^r V_l^{n_l}] = prod_l (epsilon)_{n_l}/(3 epsilon)_m`,

where `(x)_s=x(x+1)...(x+s-1)`.

Therefore

\[
\boxed{
p_\epsilon(n_1,\ldots,n_r)
=
3^{\underline r}
\frac{\prod_{\ell=1}^r(\epsilon)_{n_\ell}}
{(3\epsilon)_m}.
}
\tag{6.1}
\]

This is exactly the Poisson--Dirichlet / Ewens--Pitman EPPF with discount

`d=-epsilon`

and strength

`theta=3 epsilon`.

That exact identification is checked exhaustively for small labelled partitions in the finite self-check.

### No visible split

For `r=1`,

\[
p_\epsilon(m)
=
3\frac{(\epsilon)_m}{(3\epsilon)_m}
=
\prod_{j=1}^{m-1}\frac{j+\epsilon}{j+3\epsilon}.
\]

Hence

\[
p_\epsilon(m)
=
1-2\epsilon H_{m-1}+O_m(\epsilon^2)
=
1-\delta H_{m-1}+O_m(\delta^2),
\tag{6.2}
\]

where `delta=2 epsilon`.

### A particular binary split

For a particular `A|A^c` with `|A|=i`,

\[
\begin{aligned}
p_\epsilon(A|A^c)
&=
6\frac{(\epsilon)_i(\epsilon)_{m-i}}{(3\epsilon)_m}\\
&=
2\epsilon
\frac{(i-1)!(m-i-1)!}{(m-1)!}
+O_m(\epsilon^2)\\
&=
\delta B(i,m-i)+O_m(\delta^2).
\end{aligned}
\tag{6.3}
\]

### A ternary split

Every particular three-block split has three numerator rising factorials, and therefore

\[
p_\epsilon(A_1|A_2|A_3)=O_m(\epsilon^2)=O_m(\delta^2).
\tag{6.4}
\]

So the first-order tangent is exactly the CTCS binary generator.

---

## 7. `R11-I0054-C003` — ternary Gibbs/Dirichlet fragmentation converges to CTCS(infinity)

**STATUS: PROVED author-side under the frozen equivalence convention; campaign remains PARTIAL pending closure audits and final prior-art/source-intent review.**

### Theorem

Let `hat Pi_N` be the ternary Dirichlet-environment partition path above with `epsilon_N=1/(2N)` and raw level length `1/N`. Let `Pi` be the Aldous--Janson CTCS(infinity) exchangeable partition process.

For every fixed `k`,

\[
\widehat\Pi_N^{[k]}
\Longrightarrow
\Pi^{[k]}
\tag{7.1}
\]

in Skorokhod `J_1` as `N -> infinity`.

Moreover, in the projective metric

\[
d_{\rm proj}(\omega,\eta)
=
\sum_{k\ge1}2^{-k}
(1\wedge d_{J_1,k}(\omega^{[k]},\eta^{[k]})),
\tag{7.2}
\]

\[
\boxed{
\widehat\Pi_N\Longrightarrow\Pi.
}
\tag{7.3}
\]

Hence the complete reduced ternary Gibbs/Dirichlet genealogy, with raw generation lengths scaled by `1/N`, converges to the whole CTCS(infinity) limit object in its exchangeable-partition representation.

### Proof

#### Step 1: fixed restrictions are time-homogeneous Markov chains

Fix `k`, and take `N>=k`.

At raw depth `r`, distinct blocks of `Pi_N^[k](r)` occupy distinct ternary skeleton nodes. All descendant Dirichlet vectors at those nodes are independent and have the same `Dirichlet(epsilon_N,epsilon_N,epsilon_N)` law.

Therefore, conditional on the current partition `rho`, every current block refines independently according to (6.1). The `[k]` restriction is a finite-state time-homogeneous Markov chain in raw depth.

#### Step 2: its one-step matrix has the CTCS tangent

Let `P_N^(k)` be the one-raw-level transition matrix and put `delta_N=1/N=2 epsilon_N`.

For a current state `rho`, each block `B` of size `m` stays intact with probability

`1-delta_N H_{m-1}+O_k(delta_N^2)`.

If `rho'` is obtained by splitting exactly one current block `B` according to one particular binary partition `A|B\A`, (6.3), multiplied by the no-change probabilities of all other blocks, gives

\[
P_N^{(k)}(\rho,\rho')
=
\delta_N B(|A|,|B\setminus A|)
+
O_k(\delta_N^2).
\tag{7.4}
\]

Any other strict transition contains either a ternary refinement of one block or visible refinements in at least two current blocks. By (6.4) and independence its probability is `O_k(delta_N^2)`.

Thus, uniformly on the finite state space,

\[
\boxed{
P_N^{(k)}
=
I+\delta_N Q^{(k)}+O_k(\delta_N^2),
}
\tag{7.5}
\]

where `Q^(k)` has exactly the Aldous--Janson CTCS particular binary rates `B(i,m-i)` and diagonal rate minus `sum_{B in rho} H_{|B|-1}`.

By Part III, `Q^(k)` is exactly the generator of `Pi^[k]`.

#### Step 3: explicit holding-time / jump-chain coupling

At a nonabsorbing state `rho`, set

\[
\lambda(\rho)=\sum_{B\in\rho}H_{|B|-1}.
\]

From (7.5), the probability of any visible change during one raw generation is

\[
s_N(\rho)
=
\delta_N\lambda(\rho)+O_k(\delta_N^2).
\tag{7.6}
\]

While the visible state remains `rho`, every new raw depth exposes fresh independent Dirichlet vectors below the current occupied skeleton nodes. Hence the number `G_N` of raw generations to the next visible change is geometric with parameter `s_N(rho)`.

For every `t>=0`,

\[
P(\delta_N G_N>t)
=
(1-s_N(\rho))^{\lfloor t/\delta_N\rfloor+O(1)}
\longrightarrow
e^{-\lambda(\rho)t}.
\tag{7.7}
\]

So

\[
\delta_NG_N
\Longrightarrow
{\rm Exp}(\lambda(\rho)).
\tag{7.8}
\]

Conditioned on a visible change, for every CTCS-admissible next state `rho'`,

\[
P(\rho_{\rm next}=\rho'\mid\text{visible change})
\longrightarrow
\frac{Q^{(k)}(\rho,\rho')}{\lambda(\rho)}.
\tag{7.9}
\]

The total conditional probability of a ternary transition or simultaneous visible refinements is only `O_k(delta_N)` and tends to zero.

Couple holding times by common uniform quantiles and next states by common uniforms on the finite transition tables. At every matched state, the holding times converge and the next states agree with probability tending to one.

Every visible refinement increases the number of blocks, so both processes have at most `k-1` visible jumps before all `k` labels are singletons. A finite union bound therefore gives agreement of the entire state sequence with probability tending to one and convergence of all matched jump times.

For càdlàg paths in a finite discrete state space this gives `J_1` convergence, proving (7.1).

#### Step 4: projective convergence

Fix `eta>0`. Choose `K` so that

\[
\sum_{k>K}2^{-k}<\eta/2.
\]

For `N>=K`, use the Step-3 coupling on `[K]`. Every smaller restriction is a deterministic restriction of the same `[K]` path, so all first `K` projective coordinates converge simultaneously. The remaining deterministic metric tail is below `eta/2`.

Therefore

\[
d_{\rm proj}(\widehat\Pi_N,\Pi)\to0
\]

in probability under the coupling, proving (7.3).

#### Step 5: recovery of the tree

For finite labels `a,b`, their branchpoint height is the first time at which they belong to different blocks. The nested finite partition paths record every split and split time. Aldous--Janson Part III proves that, after ignoring left/right child order, the whole partition process determines the entire CTCS growth process.

Hence (7.3) is convergence of the source's full limit-tree representation, not a tagged-subordinator substitute.

This completes the proof.

---

## 8. Move 26 — SPORADIC FINITE CASES certify strict non-equivalence

The frozen equivalence convention retained from C001/C002 identifies models only under deterministic leaf relabeling and multiplication of all times by one deterministic positive scalar. Such transformations preserve vertex outdegrees.

### Against original CTCS and HGPF

Take `N=3`. Then `epsilon_N=1/6`.

The probability that the three labels choose three different children at the **first raw level** is, exactly,

\[
6\frac{(1/6)^3}{(1/2)_3}
=
\boxed{\frac{2}{135}}>0.
\tag{8.1}
\]

Thus the reduced ternary model has a degree-three root with positive probability.

Original DTCS/CTCS is binary, and HGPF is binary by construction. Therefore the new model is not obtained from either by deterministic relabeling or global time rescaling.

### Against SC-nCRP

The ternary model has maximum vertex outdegree `3`, deterministically.

For the SC-nCRP C002 at `N=4`, `theta_N=1/4`, the exact Ewens probability that the first level partitions all four labels into four singleton blocks is

\[
\boxed{\frac1{585}}>0.
\tag{8.2}
\]

Hence SC-nCRP has a degree-four root with positive probability, while the ternary Dirichlet model never has degree four.

Therefore C003 is also strictly non-equivalent to C002 under the frozen convention.

I do **not** count each fixed arity `q>=3` as a separate metric class; all such fixed-finite-arity Dirichlet/Gibbs deformations are treated as one class.

---

## 9. Relation to the source's subordinator clue

Open Problem 18 specifically asks whether the subordinator approximation can arise in another discrete tree model.

C003 proves something stronger than a tagged-frequency statement: its entire partition path converges to the CTCS homogeneous fragmentation. Therefore the tagged clade-frequency process and its logarithmic subordinator are inherited as marginals of the limiting whole process.

At the infinitesimal level the mechanism is visible already in (6.2)--(6.4): a small symmetric ternary Dirichlet law spends almost all of its mass near a simplex vertex, while first-order excursions involve exactly two occupied children and reproduce the beta-function CTCS split rates. Genuine ternary events are one order smaller and disappear in the accelerated limit.

This is precisely a discrete multifurcating route by which the source's binary subordinator structure emerges.

---

## 10. Prior-art assessment: stronger than C001/C002, but not final novelty clearance

This run materially changed the prior-art picture.

### Known

- MPW (2008) already define the relevant multifurcating Gibbs fragmentation trees and identify the finite-arity negative-discount ray with a symmetric Dirichlet dislocation law.
- Aldous--Janson v3 already cite MPW in their own beta-splitting discussion. Therefore I do **not** claim that importing Gibbs fragmentation is itself novel or unexpected to the proposers.
- Their binary case is exactly Aldous beta-splitting; this is why `q=2` was rejected.
- Gibbs fragmentation trees have been used in later hierarchical-network models, so the model class has an independent applied identity.

### Not found in the bounded search

I did not find a paper stating the simultaneous near-boundary / accelerated-depth theorem

`q=3 Gibbs fragmentation with alpha_MPW -> 0-  ==>  CTCS(infinity)`

in the full exchangeable-partition path sense proved above, nor a paper explicitly advertising this as an answer to Aldous--Janson Open Problem 18.

This is **not** a worldwide novelty certificate. In particular, the convergence proof is a finite-state rare-event / generator-tangent argument once the correct Gibbs ray is identified. An independent prior-art auditor must decide whether this scaling limit is already implicit or explicit in fragmentation theory and whether it satisfies the source's intentionally informal phrase "superficially different."

---

## 11. Existing independent audit state

A repository search now finds one distinct OTHER-track audit of the preceding C002 theorem:

`R10-AUDIT-R11-I0054-C002-GENERATOR-20260916`.

Its recorded result is:

`PASS for the mathematical generator/convergence core; prior-art/source-intent clearance is not audited here.`

That is useful but claim-scoped: it audits C002, not the new C003 theorem, and it is not a P26 closure audit.

I found no completed P26 end-to-end audit of C001/C002/C003. Therefore Open Problem 18 is **not called CLOSED** in this report and no `paper_*` closure package is created.

---

## 12. Exact finite self-check

Executed exact checker:

`artifacts/R11/2026-09-16T18-41-35Z_i0054-gibbs-dirichlet-tangent-d3f7_checker.py`

Creation/readback commit:

`834862080397659e7d6f283a40c0422526d8984d`.

Archived clean stdout:

`artifacts/R11/2026-09-16T18-41-35Z_i0054-gibbs-dirichlet-tangent-d3f7_checker_output.txt`

Creation/readback commit:

`92b499b074be4104cdbe1321b91b0c8486d04593`.

Executed-output SHA-256:

`5ba9aa5133725f15154c8eba083f903cc795fc13386107120334ac5f71d234a7`.

The checker uses only exact `Fraction` arithmetic and verifies:

1. exact normalization of the ternary Dirichlet partition law through `n=7` for three rational concentrations;
2. exact equality with the Poisson--Dirichlet / Ewens--Pitman EPPF on `d=-epsilon, theta=3epsilon` for 3,465 labelled-partition instances;
3. 550 exact first-order no-change / binary CTCS coefficient identities;
4. the exact finite degree witnesses `2/135`, `1/585`, and zero 4-way probability for `q=3`;
5. the exact `q=2` beta-splitting split-weight identity on 162 rational instances.

The checker explicitly does **not** prove the asymptotic convergence theorem. That proof is written in Section 7.

---

## 13. Metric / status

Under the frozen equivalence convention, the metric moves

\[
\boxed{2\longrightarrow3.}
\]

The three counted classes are:

1. HGPF (C001): harmonic-grid binary paintbox fragmentation;
2. SC-nCRP (C002): small-concentration nested Chinese restaurant process, unbounded finite branching;
3. TDGF (C003): near-critical finite-arity (`q=3`) Dirichlet/Gibbs fragmentation / random-environment ternary trie, maximum degree 3.

The new class is not counted multiple times for different `q`.

Stable new claim:

`R11-I0054-C003 = PROVED author-side under frozen equivalence`.

Overall source/campaign label:

`PARTIAL`.

The remaining closure obligations are independent audits (including P26) and final source-intent/prior-art clearance.

---

## 14. What the three new-method moves did

- **22 — read the failures / near-prior art:** found that the correct candidate is not novel as a model; it is exactly the finite-arity Gibbs fragmentation class of McCullagh--Pitman--Winkel. This improves naturality and prevents a false novelty claim.
- **23 — do what the proposer did not expect:** the binary Dirichlet model collapses back to Aldous beta-splitting and was rejected. Moving to a **multifurcating** ternary model gives genuinely different finite trees whose higher-degree events vanish at first order.
- **26 — hunt the sporadic finite case:** exact `N=3` and `N=4` degree-support witnesses rule out frozen-equivalence to original CTCS/HGPF and SC-nCRP.

The next nonrepeating Section-B triple, if research continues before audits arrive, is:

**1 (change category), 17 (look for the numbers somewhere else), 27 (swap the quantifiers).**

A particularly useful next question is whether the same beta-function tangent appears in a non-fragmentation discrete structure (for example a random combinatorial data structure or allocation model) without first building a recursive exchangeable partition. That would be substantially stronger evidence of universality than another nearby Gibbs ray.

---

## 15. Structured `ledger_delta`

```yaml
ledger_delta:
  track: R11
  intake: I0054
  source:
    authors: [David J. Aldous, Svante Janson]
    title: "The Critical Beta-splitting Random Tree II: Overview and Open Problems"
    arxiv: "2303.02529v3"
    source_date: "2025-04-18"
    locator: "Open Problem 18, section 6.3"
  target: "A genuinely different discrete tree model whose whole limit object is CTCS(infinity)"
  metric: "number of distinct nontrivial discrete model classes with complete proof of the required CTCS(infinity) limit, modulo deterministic relabeling and global deterministic time rescaling only"
  before: 2
  after: 3
  movement: true
  unchanged_count: 0
  mathematical_status: PARTIAL
  methods: [22, 23, 26]
  claims:
    retained:
      - id: R11-I0054-C001
        model_class: "harmonic-grid paintbox fragmentation (HGPF)"
        status: "PROVED author-side under frozen equivalence"
      - id: R11-I0054-C002
        model_class: "small-concentration nested Chinese restaurant process (SC-nCRP)"
        status: "PROVED author-side under frozen equivalence"
    new:
      id: R11-I0054-C003
      model_class: "near-critical ternary Dirichlet/Gibbs fragmentation (TDGF)"
      status: "PROVED author-side under frozen equivalence; audits/prior-art clearance pending"
      parameters: "q=3, epsilon_N=1/(2N), raw level length=1/N"
      limit: "whole exchangeable-partition path in projective Skorokhod topology"
  exact_evidence:
    - "artifacts/R11/2026-09-16T18-41-35Z_i0054-gibbs-dirichlet-tangent-d3f7_checker.py @ 834862080397659e7d6f283a40c0422526d8984d"
    - "artifacts/R11/2026-09-16T18-41-35Z_i0054-gibbs-dirichlet-tangent-d3f7_checker_output.txt @ 92b499b074be4104cdbe1321b91b0c8486d04593"
    - "checker stdout sha256 5ba9aa5133725f15154c8eba083f903cc795fc13386107120334ac5f71d234a7"
  audit_ids:
    existing_scoped:
      - "R10-AUDIT-R11-I0054-C002-GENERATOR-20260916: PASS generator/convergence core only"
    c003: []
    required_missing:
      - "P26 end-to-end audit"
      - "one complete distinct OTHER-track audit of C003/source match"
  prior_art:
    known_model: "McCullagh--Pitman--Winkel (2008) Gibbs fragmentation trees; finite-arity negative-discount ray has symmetric Dirichlet dislocation law"
    bounded_search_result: "no explicit C003 near-boundary CTCS(infinity) scaling theorem located"
    novelty_certificate: false
  ownership:
    repository_claim: "R11 provisional exclusive I0054 reservation; PENDING_ADMISSION not READY"
    competing_owner_found: false
  next_methods: [1, 17, 27]
```
