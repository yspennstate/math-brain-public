Model: GPT-5.6 Sol. Reasoning: UNVERIFIED runtime level; the scheduler exposes no model selector or reasoning selector, so GPT-6 / maximum was not verified and is not claimed. Metric movement: `UNMEASURED -> 1` distinct model class with a complete author-side convergence proof under the frozen equivalence convention. Section-B moves actually tried: **2 (attack the negation), 18 (change language), 25 (count twice)**.
Problem/source: David J. Aldous and Svante Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529v3 (18 April 2025), **Open Problem 18**, intake `I0054`. Overall campaign status: **PARTIAL**; mathematical claim `R11-I0054-C001` below is author-side **PROVED under the frozen equivalence convention**, but prior-art/naturality clearance and the two required OTHER-track audits are not complete.

# R11 I0054 — a harmonic-grid paintbox model converging to CTCS(infinity)

Run ID: `2026-09-16T16-40-00Z_i0054-harmonic-grid-paintbox-7c3a`  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Dated source/status check: 2026-09-16

No Gmail/email, Drive, public posting, purchase, workflow execution, permission change, scheduler change, peer-file edit, or shared-root edit was performed.

---

## 1. Repository continuity, ownership, admission, and model-control status

Before research I read or searched the required current control state:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- exclusive reservation `operations/claims/I0054.md`;
- the exact I0054 intake row under `probability_1000_intake_I_20260914/problems.jsonl` and its repository mirror;
- newest R11 report `runs/R11/2026-09-16T15-41-34Z_saw-stuck1-port-kp-5f72.md`;
- newest neighboring critical-beta-splitting report `proofnet24/P13-closure-clades/runs/2026-09-16/2026-09-16_19-04-03__run-report.md`;
- repository-wide searches for `I0054`, `Open Problem 18`, `CTCS(infinity)`, and critical-beta-splitting attempts.

The ownership record says R11 owns the provisional I0054 reservation, native task `6aa7b68c70c481919b1a131eb67b6b24`; P13's Open Problem 9 clade-covariance target is distinct. I found no competing I0054 owner or existing repository attempt claiming a different-model convergence theorem. `POSTED.md` and the campaign settled index do not list Open Problem 18 as posted or settled.

The canonical claim file still says `PENDING_ADMISSION, not READY` because the shared operational record has not been reconciled by its designated maintainer. This run completed the research-side missing checks described below; R11 does not edit shared claims/queue/root ledgers. The owner's current prompt explicitly assigns I0054 to this R11 slot, so I proceeded after checking that no ownership or posted-scope conflict exists.

### Actual runtime/model control

The current runtime identifies this worker as **GPT-5.6 Sol**; reasoning level is **UNVERIFIED**. The exposed scheduler/update interface has fields for title, prompt, schedule, enablement and timing mode, but no model selector and no reasoning-effort selector. Thus writing “GPT-6 / maximum” in prompt text does not install or verify those settings.

The current operations policy records that native modification probes for P26, P01 and P03 returned `You cannot modify this task.` The allowed workaround is **not** to bypass the restriction or create duplicate jobs: the relevant task/account/workspace owner must change it through an authorized interface, or platform support must expose/repair that control. No such external support action is performed here, and this run makes no scheduler change.

---

## 2. Source-exact target and the convergence object

The current source is arXiv:2303.02529v3, dated 18 April 2025. Its Open Problem 18 asks:

> Are there superficially different discrete models whose limit is the same CTCS(infinity)?

and immediately points to the subordinator approximation as the apparently characteristic mechanism.

It is important not to silently substitute a tagged-leaf law or a fixed-time marginal. The source's own formalization of CTCS(infinity) is the **entire exchangeable partition process**

\[
(\Pi(t),t\ge 0)
\]

on partitions of `N`: labels `i,j` are in the same block at time `t` iff their branchpoint height exceeds `t`. The source explicitly contrasts this with the Brownian CRT: CTCS(infinity) is formalized by exchangeable partitions and is *not* supplied with a standard Gromov--Hausdorff--Prokhorov random-metric-space topology.

Accordingly, the theorem below proves convergence of the whole partition-valued path in a projective Skorokhod topology, not only convergence of one tagged fragment or one fixed-time partition.

Part III, arXiv:2412.09655, identifies the exact homogeneous-fragmentation jump rates. If `pi={A,A^c}` is a nontrivial two-block partition of `[m]`, with `|A|=i`, then

\[
q_{\pi}
 =\frac{(i-1)!(m-i-1)!}{(m-1)!}
 =B(i,m-i).
\tag{2.1}
\]

It also identifies the binary dislocation measure as the push-forward, for `x in [1/2,1)`, of

\[
\frac{dx}{x(1-x)},
\]

or equivalently the symmetric version on `(0,1)`

\[
\boxed{\nu(dx)=\frac{dx}{2x(1-x)}.}
\tag{2.2}
\]

This exact rate/dislocation description is the language used in the construction below.

---

## 3. Current literature / prior-attempt screen

Dated bounded searches on 2026-09-16 included the exact phrases and combinations

- `"Open Problem 18" "CTCS" critical beta-splitting discrete models`;
- `"superficially different discrete models" "CTCS"`;
- `"same CTCS" discrete model fragmentation`;
- `critical beta-splitting 2026 homogeneous fragmentation discrete model limit`;
- the source title plus later-author and citing-paper searches.

The source v3 still lists Open Problem 18. The later Aldous--Janson Part III paper develops the exact exchangeable-fragmentation representation and dislocation measure but does not advertise a superficially different finite discrete model as an answer to Open Problem 18. Brandenberger--Chin--Mossel (2025) concerns harmonic descent and CLTs. Chorbadzhiyska--Minchev--Savov, arXiv:2608.18320 (18 August 2026), treats the beta-splitting family via homogeneous fragmentations and potential theory and resolves a height-related open problem, not Open Problem 18. September 2026 critical-beta-splitting papers found in bounded searches concern extremal separation/clade dynamics rather than a different-model CTCS(infinity) limit.

**Prior-art warning.** The mechanism used below is not claimed to be new machinery. Homogeneous fragmentation via paintboxes/dislocation measures is standard, and Part III Remark 4.6 explicitly relates the critical dislocation density to the older beta-splitting random-split-point construction. Atomic approximation of a dislocation measure is a natural/folklore idea. I did **not** locate this exact harmonic-grid model stated as an answer to Open Problem 18, but a negative bounded search is not a novelty certificate. This is one reason the campaign label remains PARTIAL and no paper package is created.

---

## 4. Immutable handoff of R11's retired planar-SAW route

The old R11 planar self-avoiding-walk slot is retired from this worker assignment exactly as instructed; its history remains immutable in the earlier `runs/R11/` reports.

The last SAW report was

`runs/R11/2026-09-16T15-41-34Z_saw-stuck1-port-kp-5f72.md`.

Its retained fixed metric was

\[
(a,C,n_0)=(2,1,1)
\]

for the original uniform nearest-neighbor SAW on `Z^2`, with unchanged-count 3. The exact blocker was a uniform small-speed strengthening of Duminil-Copin--Hammond,

\[
\Pr(R_n>vn)\le \exp(-c_0 n v^\kappa)
\]

for some finite `kappa`, uniformly as `v downarrow 0`; the simplest selected special case was an exponentially small tail at radius `n^(7/8)`. No SAW exponent closure was claimed. The old reports and artifacts are preserved and are not overwritten or folded into the I0054 metric.

---

## 5. Move 2 — ATTACK THE NEGATION FIRST

Before trying to prove convergence, I tested simple alternative fragmentation mechanisms against necessary finite-restriction invariants.

### 5.1 Flat-bias paintbox fails

Take the superficially natural alternative `nu_flat(dx)=dx` on `(0,1)`, split labels by iid Bernoulli(`x`), and ignore trivial all-one-color marks. A particular unordered split with sizes `i,m-i` then has limiting rate

\[
q^{\rm flat}(m,i)
 =\int_0^1\left[x^i(1-x)^{m-i}+x^{m-i}(1-x)^i\right]dx
 =2B(i+1,m-i+1).
\]

At `m=4`,

\[
q^{\rm flat}(4,1)=\frac1{10},\qquad
q^{\rm flat}(4,2)=\frac1{15},
\]

so the shape-rate ratio is `3/2`. The CTCS(infinity) target ratio is

\[
\frac{q(4,1)}{q(4,2)}
 =\frac{1/3}{1/6}=2.
\]

No deterministic global time rescaling can change this ratio. Thus the simplest flat-bias model cannot have the required limit.

### 5.2 Reverse the beta(2,1) coalescent does not immediately solve the finite-model problem

The source itself notes that the beta(2,1) coalescent has the same tagged singleton-frequency subordinator, but explicitly warns that the correspondence does not carry over to finite restrictions in the naive way. Thus the matching tagged subordinator is a necessary clue, not a complete answer to Open Problem 18.

**Outcome of move 2:** the target remembers the singular harmonic factor `1/[x(1-x)]`; matching only a generic fragmentation/coalescent shape or the tagged subordinator is too weak.

---

## 6. Move 18 — SAY IT IN ANOTHER LANGUAGE

The exchangeable-fragmentation language suggests replacing the singular continuous dislocation measure (2.2) by finite atomic Riemann sums.

### Definition: harmonic-grid paintbox fragmentation tree (HGPF)

For each integer `N>=2`, put

\[
x_j=\frac jN,\qquad 1\le j\le N-1,
\]

and define the finite symmetric atomic measure

\[
\boxed{
\nu_N
 =\frac1N\sum_{j=1}^{N-1}
 \frac{1}{2x_j(1-x_j)}\,\delta_{x_j}.
}
\tag{6.1}
\]

Start with one block `[N]`. Each existing block evolves independently as follows. At Poisson marks with intensity measure `nu_N`, choose the mark's grid bias `x_j`; color every label in the block independently Bernoulli(`x_j`); if both colors occur, replace the block by the two color classes, unordered; if all labels get the same color, the mark is invisible and the block is unchanged. Continue until all blocks are singletons.

The genealogy of these finitely many labels, with each split time as its branchpoint height, is a finite random rooted binary tree with real edge lengths. Its combinatorial state space is discrete; the continuously distributed edge lengths are retained because CTCS(infinity) is a continuous-time limit object.

Call the partition path `Pi_N(t)`.

---

## 7. Move 25 — COUNT THE SAME SPLIT TWICE

Fix a finite block of `m` sampled labels and a particular unordered bipartition `pi={A,A^c}` with `|A|=i`.

### 7.1 HGPF rate

A grid mark `x_j` creates this particular partition with probability

\[
x_j^i(1-x_j)^{m-i}+x_j^{m-i}(1-x_j)^i.
\]

Therefore its HGPF rate is

\[
\begin{aligned}
q_N(m,i)
&=\frac1{2N}\sum_{j=1}^{N-1}
\frac{x_j^i(1-x_j)^{m-i}+x_j^{m-i}(1-x_j)^i}
{x_j(1-x_j)}\\
&=\frac1N\sum_{j=1}^{N-1}
 x_j^{i-1}(1-x_j)^{m-i-1},
\end{aligned}
\tag{7.1}
\]

where the second equality uses symmetry of the grid under `j <-> N-j`.

For fixed `m,i`, (7.1) is an ordinary Riemann sum, so

\[
q_N(m,i)\longrightarrow
\int_0^1x^{i-1}(1-x)^{m-i-1}dx
=B(i,m-i).
\tag{7.2}
\]

### 7.2 The same target rate from CTCS

Part III derives the rate of the same particular unordered split directly from the CTCS finite-block split law and obtains exactly

\[
q_\pi=B(i,m-i).
\tag{7.3}
\]

It independently obtains the same value by integrating the binary paintbox probability against the dislocation measure `dx/[x(1-x)]` on `[1/2,1)`.

Thus the target transition rate has been counted in two languages, and the HGPF transition rate is a finite Riemann discretization of exactly that common quantity.

**Outcome of moves 18+25:** this produces a concrete finite model class whose whole finite-restriction generators converge to the CTCS(infinity) generator.

---

## 8. R11-I0054-C001 — whole-process convergence to CTCS(infinity)

**STATUS: PROVED under the frozen equivalence convention; external novelty/source-intent and independent audits pending.**

### Theorem

Let `(Pi_N(t),t>=0)` be the HGPF partition process on `[N]` defined by (6.1), extended to a partition of `N` by declaring labels greater than `N` singleton blocks. Let `(Pi(t),t>=0)` be the Aldous--Janson CTCS(infinity) exchangeable partition process.

For every fixed `k`, the restriction

\[
(\Pi_N^{[k]}(t),t\ge0)
\]

converges in distribution, as `N->infinity`, in Skorokhod `J_1` topology on càdlàg paths with values in the finite partition set `P_k`, to

\[
(\Pi^{[k]}(t),t\ge0).
\]

Moreover, if the full partition-path space is given the projective metric

\[
d_{\rm proj}(\omega,\eta)
=\sum_{k\ge1}2^{-k}
\bigl(1\wedge d_{J_1,k}(\omega^{[k]},\eta^{[k]})\bigr),
\tag{8.1}
\]

using any standard bounded `J_1` metric on `D([0,infinity),P_k)`, then

\[
\boxed{\Pi_N\Longrightarrow\Pi}
\tag{8.2}
\]

in this projective Skorokhod topology. Since the separation time of each pair of labels is its branchpoint height, this is convergence to the source's full CTCS(infinity) tree formalization, not merely a tagged-fragment or fixed-time marginal limit.

### Proof

**Step 1: restriction of HGPF is itself a homogeneous fragmentation.**

Fix `k` and take `N>=k`. A paintbox mark on a block containing sampled labels restricts to iid Bernoulli(`x_j`) colors on those sampled labels. Marks which do not separate the sampled labels are invisible to the restriction. After any mark, the Poisson/memoryless construction and independent evolution of descendant blocks imply that future visible marks on each sampled block have the same law as if the process had been built directly on `[k]` using `nu_N`. Therefore `Pi_N^[k]` is a finite-state continuous-time Markov fragmentation whose transition rates are the `q_N(m,i)` in (7.1).

**Step 2: generator convergence.**

Let `Q_N^(k)` be the generator on `P_k`. If a state `rho` moves to `rho'` by splitting one block `B` of size `m` into the particular two subsets `A,B\A`, with `|A|=i`, then

\[
Q_N^{(k)}(\rho,\rho')=q_N(m,i).
\]

All other off-diagonal transitions are zero. By (7.2), for every such transition

\[
Q_N^{(k)}(\rho,\rho')\to B(i,m-i).
\]

There are finitely many states and transitions for fixed `k`, so convergence is uniform over all entries. Diagonal entries converge because they are minus the finite sum of off-diagonal rates.

Part III equations (4.5)--(4.6) identify the CTCS(infinity) restriction generator `Q^(k)` with exactly these limiting rates. Thus

\[
Q_N^{(k)}\to Q^{(k)}
\tag{8.3}
\]

entrywise (indeed uniformly on the finite matrix).

**Step 3: path-level `J_1` convergence for fixed `k`.**

A visible fragmentation of `[k]` can make at most `k-1` jumps before reaching the all-singleton absorbing state. We give an explicit jump coupling.

At a nonabsorbing state `rho`, let

\[
\lambda_N(\rho)=-Q_N^{(k)}(\rho,\rho),
\qquad
\lambda(\rho)=-Q^{(k)}(\rho,\rho).
\]

By (8.3), `lambda_N(rho)->lambda(rho)>0`. Use the same `E~Exp(1)` to generate holding times

\[
H_N=E/\lambda_N(\rho),\qquad H=E/\lambda(\rho),
\]

so `H_N->H` almost surely.

Order the finitely many possible next states. Their transition probabilities are

\[
p_N(\rho,\rho')=Q_N^{(k)}(\rho,\rho')/\lambda_N(\rho)
\]

and converge to `p(rho,rho')`. Use one common `U~Uniform(0,1)` and inverse cumulative probabilities to select the next state. Except when `U` hits one of finitely many limiting cumulative boundaries, an event of probability zero, the selected next states agree for all sufficiently large `N`.

Iterate this construction. There are at most `k-1` visible jumps, so with probability one the entire finite sequence of states eventually agrees and every corresponding jump time converges. For càdlàg paths in a finite discrete state space this implies

\[
\Pi_N^{[k]}\to\Pi^{[k]}
\]

in `J_1` under the coupling, hence convergence in distribution.

**Step 4: upgrade from every finite restriction to the complete exchangeable-partition path.**

The source formalizes CTCS(infinity) by the entire consistent family of restrictions of `Pi(t)`. Metric (8.1) gives that projective object an explicit convergence topology.

Fix `epsilon>0` and choose `K` so that

\[
\sum_{k>K}2^{-k}<\epsilon/2.
\]

For `N>=K`, apply Step 3 to the `[K]` restriction. Under its jump coupling, the `[K]` paths converge in probability in `J_1`; all smaller restrictions are deterministic images of that same coupled path and converge simultaneously. Hence the first `K` terms in (8.1) converge to zero in probability, while the remaining tail is deterministically below `epsilon/2`. Therefore

\[
d_{\rm proj}(\Pi_N,\Pi)\to0
\]

in probability under these couplings, which implies (8.2).

**Step 5: recover the tree, not only a marginal partition statistic.**

For labels `a,b`, define

\[
H_{a,b}=\inf\{t:\ a\text{ and }b\text{ lie in different blocks of }\Pi(t)\}.
\]

This is exactly the branchpoint height separating the two leaves. On every finite label set the nested partition path and all its split times reconstruct the rooted clade genealogy and its edge lengths. Thus convergence of the full projective partition path is convergence to the same CTCS(infinity) object in the formalism chosen by Aldous--Janson.

This completes the proof. `square`

---

## 9. Frozen equivalence convention and a strict non-equivalence certificate

For this track I freeze the required convention as follows.

Two finite-model families are called equivalent only if, for every `N`, one can obtain one partition-valued path law from the other by (i) a deterministic permutation of leaf labels and (ii) multiplication of all times by one deterministic positive scalar (allowed to depend on `N`). No other transformation is quotiented out.

Under this convention HGPF is **not** a relabeling or rescaling of the original CTCS family.

At `N=4`, the HGPF specific rates are exactly

\[
q_4(4,1)=\frac7{32},\qquad
q_4(4,2)=\frac5{32},
\]

so

\[
\frac{q_4(4,1)}{q_4(4,2)}=\frac75.
\tag{9.1}
\]

For CTCS(4), equation (2.1) gives

\[
q(4,1)=\frac13,\qquad q(4,2)=\frac16,
\]

and hence ratio `2`. A relabeling preserves the split-shape class `1|3` versus `2|2`, while a global time rescaling multiplies all rates by the same scalar. Therefore the ratio is invariant under the frozen equivalence, and

\[
\boxed{7/5\ne2}
\]

proves strict non-equivalence.

This is a finite exact certificate for distinctness; it is not being used to infer convergence.

---

## 10. What is genuinely achieved, and what remains

### Mathematical achievement under the track's frozen convention

The HGPF class is a concrete finite random-tree model family, not a relabeling or time-rescaling of CTCS(N), and the proof above gives convergence of the **whole exchangeable partition process**, including branchpoint times, to CTCS(infinity). Therefore the tracked mathematical quantity moves from `UNMEASURED` to

\[
\boxed{1}
\]

distinct model class with a complete author-side limit proof.

I record this claim as

`R11-I0054-C001 = PROVED under frozen equivalence / campaign PARTIAL`.

### Why I do not call Open Problem 18 closed

1. The source says “superficially different,” an intentionally informal naturality criterion. HGPF is engineered by discretizing the exact dislocation measure identified in Part III. The owner's metric supplies a precise weaker/frozen equivalence convention under which it is genuinely different, but an independent auditor should decide whether this sufficiently matches the authors' intended phrase.
2. The general homogeneous-fragmentation/paintbox mechanism is established theory. The exact harmonic-grid construction was not found in the bounded search, but novelty is not independently certified.
3. Fleet closure requires two independent OTHER-track audits, including P26, and neither has audited this new theorem.
4. Therefore no `paper_*` closure package is created this run.

---

## 11. Exact finite checker and its scope

Executed checker:

`artifacts/R11/2026-09-16T16-40-00Z_i0054-harmonic-grid-paintbox-7c3a_checker.py`

Archived output:

`artifacts/R11/2026-09-16T16-40-00Z_i0054-harmonic-grid-paintbox-7c3a_checker_output.txt`

The checker uses exact `fractions.Fraction` arithmetic and verifies:

- source beta-rate and harmonic-total identities for `m=2,...,20`;
- equality of the direct atomic-paintbox rate and the symmetrized Riemann-sum formula;
- the exact `N=4` non-equivalence witness `7/5 != 2`;
- the flat-bias counterexample invariant `3/2 != 2`;
- exact pair/triple visible split rates for `N=2,...,100`;
- diagnostic exact rate tables through `N=128`.

It explicitly prints that finite calculations do **not** establish asymptotic convergence; the convergence theorem is proved on the page above.

Executed-output SHA-256:

`6796856504e61d090076a9ca5f94e3a4e1905c3b36e067dc02c41cbd651c0fb7`.

Artifact creation/readback commits:

- checker creation `4370bae913bc9767f06f6724e3fe51a80e1956bb`;
- checker-output creation `f159f99533b6f3fc564d676f75e54fa7d0e45ec3`.

---

## 12. Research assessment and next methods

The productive route was not to manipulate the original recursive split probabilities directly. The key change was **Move 18**: view CTCS(infinity) as a homogeneous exchangeable fragmentation, where the entire target is encoded in one singular dislocation measure. That made **Move 25** an exact beta-integral identity and exposed a finite atomic approximation. **Move 2** was useful because flat bias and the beta(2,1) reversal show which much easier constructions fail to preserve the finite-restriction generator.

If this track continues before audit feedback, the next three new-method numbers should be **6 (deform to a solvable point), 21 (ask who else has this shape), 29 (add the points at infinity)**, rather than repeating 2/18/25. The highest-value task would be adversarial prior-art/naturality analysis: determine whether a standard fragmentation approximation theorem already makes HGPF essentially known, and whether one can replace the engineered harmonic grid by a more naturally generated discrete combinatorial model while preserving the same generator limit.

---

## 13. Structured ledger_delta

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
  target: "A genuinely different finite discrete tree model whose whole limit object is CTCS(infinity)"
  metric: "number of distinct nontrivial discrete model classes with a complete proof of the required CTCS(infinity) limit, modulo deterministic relabeling and global time rescaling only"
  before: UNMEASURED
  after: 1
  movement: true
  unchanged_count: UNKNOWN
  mathematical_status: PARTIAL
  claim:
    id: R11-I0054-C001
    status: "PROVED under frozen equivalence convention; campaign closure not certified"
    model_class: "harmonic-grid paintbox fragmentation trees (HGPF)"
    convergence: "whole exchangeable partition path in projective Skorokhod topology"
  exact_evidence:
    checker: "artifacts/R11/2026-09-16T16-40-00Z_i0054-harmonic-grid-paintbox-7c3a_checker.py"
    checker_commit: "4370bae913bc9767f06f6724e3fe51a80e1956bb"
    output: "artifacts/R11/2026-09-16T16-40-00Z_i0054-harmonic-grid-paintbox-7c3a_checker_output.txt"
    output_commit: "f159f99533b6f3fc564d676f75e54fa7d0e45ec3"
    output_sha256: "6796856504e61d090076a9ca5f94e3a4e1905c3b36e067dc02c41cbd651c0fb7"
  audits:
    P26: PENDING
    other_track: PENDING
  prior_art:
    status: "BOUNDED_SEARCH_COMPLETE_FOR_RUN; FINAL_CLEARANCE_PENDING"
    warning: "homogeneous fragmentation and dislocation-measure approximation are standard/folklore; exact HGPF answer not located"
  ownership:
    owner: R11
    canonical_claim: "operations/claims/I0054.md"
    canonical_claim_status: "PENDING_ADMISSION; shared record not edited by R11"
  old_R11_SAW:
    disposition: "immutable handoff / retired from this slot"
    last_report: "runs/R11/2026-09-16T15-41-34Z_saw-stuck1-port-kp-5f72.md"
    last_metric: "(a,C,n0)=(2,1,1), unchanged-count=3"
```

**No source-level closure claim is made.**
