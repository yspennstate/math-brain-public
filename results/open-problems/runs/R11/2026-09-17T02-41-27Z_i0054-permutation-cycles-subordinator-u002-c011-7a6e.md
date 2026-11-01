Model: GPT-5.6 Sol. Reasoning: UNVERIFIED runtime level; GPT-6 / maximum was requested in prompt text, but no model-family or reasoning-effort selector is exposed, so GPT-6 / maximum is not claimed. Metric moved 10 -> 11. Methods actually tried: #12 FIND WHAT IS CONSERVED; #23 DO WHAT THE PROPOSER DID NOT EXPECT; #27 SWAP THE QUANTIFIERS.

Problem/source: David J. Aldous and Svante Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529v3 (18 April 2025), Open Problem 18, intake `I0054`.

# R11 I0054 — permutation-cycle fragmentation and a tagged-subordinator completeness criterion

## Status and continuity

**Status after this run: PARTIAL for campaign closure.** The frozen mathematical metric moves from 10 to 11 distinct nontrivial discrete model classes with complete author-side whole-path proofs. The canonical ownership file still literally says `PENDING_ADMISSION, not READY`; the source's informal word "superficially" has not been independently adjudicated; and the two required OTHER-track end-to-end audits, one from P26, do not exist for the new C011 theorem. I therefore do not call Open Problem 18 closed and do not create a paper package.

I continued from the newest R11 report

`runs/R11/2026-09-17T01-40-00Z_i0054-sweepstakes-anchor-c010-41d6.md`

rather than restarting. That report moved the metric 9 -> 10 and prescribed the nonrepeating method triple #12/#23/#27 used here.

Before new mathematics I recovered the current campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/claims/I0054.md`, the owner directive, the newest R11 report, the newest neighboring P13/I0051 report, and current I0054 audit searches. The claim remains provisionally exclusive to R11 but `PENDING_ADMISSION, not READY`. No competing I0054 owner and no posted/settled Open Problem 18 scope appeared. The root `RESULTS.md` R-series table is explicitly stale and instructs workers to recover complete own reports before replacing old values, so the supported baseline is C010's immutable metric 10, not the old SAW row.

The retired planar self-avoiding-walk route remains untouched. P13's Open Problem 9 / I0051 clade-count problem remains distinct.

## Current source and literature check

I rechecked the actual arXiv v3 PDF on 2026-09-17 UTC. Section 6.3, PDF page 58, still asks Open Problem 18: whether superficially different discrete models can have CTCS(infinity) as the same limit, and immediately identifies the subordinator approximation as the feature that might reappear in another discrete tree model. The overview states that CTCS(infinity) is formalized by a consistent process of exchangeable partitions, so the target here remains the complete partition-valued genealogy rather than a tagged fragment or a one-time marginal.

I also rechecked Aldous--Janson Part III, arXiv:2412.09655v1. Section 4.5 gives the binary CTCS dislocation measure as the push-forward of

\[
\widetilde\nu(dx)=\frac{dx}{x(1-x)},\qquad x\in[1/2,1),
\]

and computes the particular split rate as `B(i,m-i)`. Remark 4.7 explicitly notes that general homogeneous-fragmentation theory relates the tagged-fragment moment/Laplace transform to the dislocation measure, and conversely can recover the CTCS dislocation measure from the tagged formula. That is important prior art for U002 below: I do **not** claim the general tagged-fragment/dislocation correspondence is new.

A fresh bounded search covered current Aldous--Janson followups, homogeneous fragmentations, random-permutation cycle fragmentation/split-merge dynamics, Stirling cycle counts, and combinations of `CTCS`, `two cycles`, `random permutation`, and `fragmentation tree`. The 2026 beta-splitting followups I found treat the original beta-splitting family, heights, clades, or fragmentation asymptotics, not a resolution of exact Open Problem 18. Random-permutation cycle and transposition fragmentation dynamics are classical. I did not locate the specific paired two-cycle/common-refinement hierarchy below or its CTCS limit. This is a bounded dated search, not a novelty certificate.

---

# Method #12 — find what is conserved

Two invariants emerged.

The first is elementary but decisive: the **exactly-two-cycle sector of a uniform permutation already contains the CTCS beta kernel**.

Fix a block `B` of size `m`, and a particular unordered bipartition `A | A^c` with `|A|=i`. The number of permutations of `B` whose two cycles have supports exactly `A` and `A^c` is

\[
(i-1)!(m-i-1)!.
\]

Therefore for a uniform `sigma in S_m`,

\[
\boxed{
\Pr(\text{cycles}(\sigma)=\{A,A^c\})
=\frac{(i-1)!(m-i-1)!}{m!}
=\frac1m B(i,m-i).
}
\tag{12.1}
\]

Summing over all two-cycle permutations recovers the classical Stirling identity

\[
\#\{\sigma\in S_m:\#\text{cycles}(\sigma)=2\}
=(m-1)!H_{m-1},
\]

so

\[
\Pr(\#\text{cycles}=2)=\frac{H_{m-1}}m.
\tag{12.2}
\]

Thus multiplying the proposal intensity by `m` simultaneously removes the unwanted `1/m` in every particular split and in the total harmonic rate.

The second invariant is more conceptual: **within the conservative binary homogeneous-fragmentation class, the tagged-fragment subordinator is a complete invariant of the dislocation measure.** This is proved explicitly under Method #27 below and gives a source-facing explanation for why Aldous--Janson singled out the subordinator.

---

# Method #23 — a model the proposer did not formulate: paired permutation-cycle refinement

The naive version fails in exactly the right way. If a uniform permutation is allowed to split a block into *all* of its cycles, then at `m=3` the identity permutation gives a three-way split with first-order positive mass. Such a model cannot converge to binary CTCS under a scaling in which one permutation event has first-order rate.

The correction is not to tune component-size weights. Instead, use the classical two-cycle sector as a proposal and allow **two rare proposals to interact** at finite `N`.

## Definition of C011

For each global size `N`, put

\[
\varepsilon_N:=N^{-3},\qquad \Delta_N:=2\varepsilon_N.
\tag{23.1}
\]

At every raw generation and independently for every current nonsingleton block `B` of size `m`:

1. create two independent proposal slots `j=1,2`;
2. activate slot `j` with probability
   \[
   a_{N,m}:=m\varepsilon_N;
   \]
3. if active, draw a uniform random permutation `sigma_j` of `B`;
4. if `sigma_j` has exactly two cycles, retain the unordered bipartition of `B` given by those cycle supports; otherwise that slot is null;
5. if both slots are null, leave `B` unchanged;
6. if exactly one slot is nonnull, split `B` into its two cycle supports;
7. if both slots are nonnull, split `B` according to the **common refinement** of the two bipartitions, i.e. all nonempty intersections of one cycle from the first proposal with one cycle from the second proposal.

All current blocks update independently. One raw generation has physical duration `Delta_N`. The common refinement has at most four children, and incompatible successful proposals can create genuine 3- or 4-way vertices at finite `N`.

This is a random-permutation cycle model, not an RRT/Cayley/BST cut model and not a Poisson--Dirichlet/Ewens partition draw. No component-size correction weights are inserted.

---

# Exact hidden-label projection

The finite restriction must work through arbitrary unobserved labels, not merely when the block itself has fixed size.

Let a visible sampled block `C`, `|C|=b`, lie inside a hidden block `B`, `|B|=m>=b`. Let `A subset C`, `|A|=i`, be a particular visible side.

For one proposal slot and a hidden side `U subset B`, `|U|=s`, with `U cap C=A`, equation (12.1) and activation probability `m epsilon_N` give

\[
\Pr(\text{that slot proposes }U|U^c)
=m\varepsilon_N\frac1m B(s,m-s)
=\varepsilon_N B(s,m-s).
\tag{23.2}
\]

There are `binom(m-b,s-i)` choices of `U` of size `s` with intersection `A`. Orienting the hidden split by the side whose visible intersection is `A` counts each induced visible split exactly once. Hence

\[
\begin{aligned}
\Pr(\text{one slot induces }A|C\setminus A)
&=\varepsilon_N
\sum_{s=i}^{m-b+i}
\binom{m-b}{s-i}B(s,m-s)\\
&=\varepsilon_N B(i,b-i).
\end{aligned}
\tag{23.3}
\]

The last equality is the beta-binomial identity: insert

\[
B(s,m-s)=\int_0^1x^{s-1}(1-x)^{m-s-1}\,dx
\]

and sum the binomial expansion over the hidden labels. The crucial point is that the right side of (23.3) is **independent of hidden size `m`**.

Summing (23.3) over all particular visible binary splits yields one-slot visible-change probability `epsilon_N H_{b-1}`.

---

# Whole-path convergence theorem for C011

## Theorem C011

For the paired permutation-cycle hierarchy above,

\[
\boxed{
\widehat\Pi_N\Longrightarrow\Pi_{\rm CTCS(\infty)}
}
\tag{C11.1}
\]

in the projective finite-restriction Skorokhod topology. Equivalently, for every fixed `k`, the restriction to `[k]` converges in `J_1` to the exact CTCS restriction, and the compatible family of restrictions converges to the complete exchangeable-partition genealogy.

### Proof

Fix `k` and condition on the complete hidden `N`-label history at the beginning of a raw generation. Let `rho` be the current partition of `[k]`, and consider a target CTCS transition `rho -> rho'` consisting of a particular split `A | C\A` inside one visible block `C`, with `|C|=b`, `|A|=i`.

For the unique hidden block containing `C`, equation (23.3) says that one specified proposal slot generates the target visible bipartition with probability exactly

\[
\varepsilon_N B(i,b-i).
\]

If the other slot is inactive, the two choices of the active slot therefore contribute

\[
2\varepsilon_N B(i,b-i)(1-m\varepsilon_N).
\]

Whenever both slots are active, regardless of their cycle counts and common refinement, the total probability is at most

\[
(m\varepsilon_N)^2\le N^2\varepsilon_N^2.
\]

Consequently, uniformly over every hidden history and hidden block size,

\[
\Pr(\rho\to\rho'\mid\mathcal F_N)
=2\varepsilon_N B(i,b-i)
+O(N^2\varepsilon_N^2).
\tag{C11.2}
\]

Different visible blocks update independently. By (23.3), for a visible block of fixed size at most `k`, the probability of a visible change from one slot is `O_k(epsilon_N)`, independent of its hidden size. Therefore simultaneous visible changes in two distinct visible blocks are `O_k(epsilon_N^2)`, and the only larger error is the same-block two-active-slot term already bounded by `O(N^2 epsilon_N^2)`.

Writing `Q^(k)` for the exact CTCS generator on partitions of `[k]`, and recalling `Delta_N=2 epsilon_N`, we obtain the **uniform conditional expansion**

\[
\boxed{
P_N^{(k)}(\rho,\rho'\mid\mathcal F_N)
=\Delta_NQ^{(k)}(\rho,\rho')
+O_k(N^2\varepsilon_N^2)
}
\tag{C11.3}
\]

for every off-diagonal CTCS jump, with the corresponding diagonal expansion and all non-CTCS/multiple visible transitions in the same error budget.

Let

\[
K_N:=I+\Delta_NQ^{(k)}.
\]

Because the estimate is uniform conditional on the hidden past, step-by-step maximal coupling couples the visible process to the Euler chain with per-step failure probability `O_k(N^2 epsilon_N^2)`. Up to fixed physical time `T` there are `O(T/Delta_N)=O(T/epsilon_N)` raw steps. Thus

\[
\Pr(\text{coupling failure before }T)
=O_k(TN^2\varepsilon_N).
\tag{C11.4}
\]

For `epsilon_N=N^-3`,

\[
N^2\varepsilon_N=N^{-1}\to0.
\]

Hence the visible restriction and its Euler approximation agree on every compact time interval with probability tending to one.

It remains to pass from the Euler chain to the CTCS continuous-time chain. At state `rho`, write

\[
\lambda(\rho):=-Q^{(k)}(\rho,\rho)
=\sum_{C\in\rho}H_{|C|-1}.
\]

The number of Euler steps to the next jump is geometric with parameter `Delta_N lambda(rho)`, so its physical holding time converges to `Exp(lambda(rho))`. Conditional on a jump, the next state has probability

\[
Q^{(k)}(\rho,\rho')/\lambda(\rho).
\]

A fragmentation of `k` labels has at most `k-1` visible jumps before absorption. A common-uniform coupling of the finite sequence of holding times and jump states therefore gives

\[
\widehat\Pi_N^{[k]}\Longrightarrow\Pi_{\rm CTCS}^{[k]}
\]

in Skorokhod `J_1`.

Finally use the standard projective metric

\[
d_{\rm proj}(\omega,\eta)
=\sum_{k\ge1}2^{-k}
\bigl(1\wedge d_{J_1,k}(\omega^{[k]},\eta^{[k]})\bigr).
\]

Choose `K` so the deterministic tail `sum_{k>K}2^-k` is arbitrarily small, and use the `[K]` coupling to control all smaller restrictions simultaneously. This gives (C11.1). Pair-separation times recover the branchpoint heights, so this is convergence of the full CTCS(infinity) genealogy in the source's exchangeable-partition formalization, not merely a tagged marginal. QED.

---

# Exact finite non-equivalence: C011 is a genuinely new frozen class

Every C011 raw split is the common refinement of at most two bipartitions, hence

\[
\boxed{\text{finite outdegree in C011 is at most }4.}
\tag{23.4}
\]

Degree four occurs with positive probability. At `N=4`, `epsilon_4=1/64` and a slot activates with probability `4/64=1/16`. A specified `2|2` cycle bipartition is realized by exactly one permutation out of `4!`, so one specified crossing proposal has probability

\[
\frac1{16}\frac1{24}=\frac1{384}.
\]

Two fixed crossing `2|2` proposals, in either order, have probability

\[
\boxed{\frac1{73728}>0,}
\tag{23.5}
\]

and their common refinement is four singletons.

This degree-cap invariant separates C011 from all ten previously counted classes under the frozen equivalence convention:

- original CTCS, C001, C009 and C010 are binary at finite `N`;
- C003 has maximum finite outdegree 3;
- C002 and C004 assign positive probability to partitions with five or more blocks when `m>=5`;
- C005--C008 are multi-edge-cut tree/path models and have positive probability of at least five components at `m=5`.

Thus no deterministic relabeling or global branch-length rescaling can identify C011 with an earlier class.

A second exact witness at `N=3` is useful for checking the construction. Here `epsilon_3=1/27`, a slot activates with probability `1/9`, and each of the three particular `1|2` cycle bipartitions occurs in a slot with probability `1/54`. Therefore

\[
P(\text{no visible proposal})=(17/18)^2=289/324,
\]

\[
P(\text{raw degree 3})=6(1/54)^2=1/486,
\]

and after suppressing waiting generations,

\[
\boxed{P(\deg(\mathrm{root})=3\mid\text{first visible split})=2/105.}
\tag{23.6}
\]

Hence the frozen metric moves

\[
\boxed{10\longrightarrow11.}
\]

The stable new model claim is

\[
\boxed{\texttt{R11-I0054-C011 = PROVED author-side under frozen equivalence}.}
\]

---

# Method #27 — swap the quantifiers: tagged-subordinator completeness in the binary class

Instead of proving the entire fragmentation law separately for each future candidate, characterize **all** conservative binary homogeneous fragmentation limits by their tagged spine.

## Proposition U002 (binary tagged-spine identifiability)

Let `Pi` be a conservative homogeneous exchangeable fragmentation with zero erosion and dislocation measure supported on binary mass partitions

\[
s_x=(x,1-x,0,\ldots),\qquad x\in[1/2,1).
\]

Let `P_t` be the asymptotic frequency of the block containing a uniformly tagged initial label and let

\[
Y_t=-\log P_t.
\]

Then the Levy measure `kappa` of the subordinator `Y` uniquely determines the binary dislocation measure `nu`.

### Proof

At a binary dislocation with masses `(x,1-x)`, the tag follows the larger child with probability `x` and the smaller child with probability `1-x`. Hence the Levy measure of `Y` satisfies the measure identity

\[
\kappa(dy)
=\int_{1/2}^1
\left[
 x\,\delta_{-\log x}(dy)
 +(1-x)\,\delta_{-\log(1-x)}(dy)
\right]\nu(dx).
\tag{27.1}
\]

For `0<y<log 2`, only the larger-child term can contribute because `x>=1/2` while `1-x<=1/2`. Therefore, for every Borel `E subset (1/2,1)`,

\[
\boxed{
\nu(E)=\int_{\{-\log x:x\in E\}}e^y\,\kappa(dy).
}
\tag{27.2}
\]

The possible atom at `x=1/2` is also determined, because at an equal split both tagged choices give jump `log 2`, so

\[
\nu(\{1/2\})=\kappa(\{\log2\}).
\]

Thus `kappa` determines `nu` uniquely. QED.

For CTCS, Aldous--Janson give the tagged Levy density

\[
\kappa_{\rm CTCS}(dy)
=\frac{e^{-y}}{1-e^{-y}}\,dy.
\tag{27.3}
\]

On `0<y<log2`, set `x=e^{-y}`. Pulling (27.3) back and applying (27.2) gives

\[
\boxed{
\nu(dx)=\frac{dx}{x(1-x)},\qquad x\in[1/2,1),
}
\tag{27.4}
\]

with no atom at `1/2`, exactly the CTCS dislocation measure in Aldous--Janson Part III. Consequently its particular finite split rates are

\[
\int_{1/2}^1
\left[x^i(1-x)^{m-i}+x^{m-i}(1-x)^i\right]
\frac{dx}{x(1-x)}
=B(i,m-i).
\]

General homogeneous-fragmentation theory says zero erosion plus the dislocation measure determines the process. Hence **within the conservative binary homogeneous class, the CTCS tagged subordinator determines the entire CTCS(infinity) fragmentation law.**

This is a source-facing specialization and elementary inversion of known fragmentation theory, not claimed as a new foundational theorem: Part III Remark 4.7 explicitly points to the converse transform.

## Corollary: a spine-to-tree convergence criterion

Let a sequence of exchangeable discrete tree/fragmentation models, after time rescaling, be tight in the projective finite-restriction topology. Suppose every subsequential limit is a conservative homogeneous **binary** exchangeable fragmentation with zero erosion, and suppose the tagged-fragment process in every subsequential limit has the CTCS subordinator law (27.3). Then every subsequential limit has dislocation measure (27.4) by U002 and therefore equals CTCS(infinity). Hence the entire sequence converges to CTCS(infinity).

This changes the research burden for future natural models: one may prove tightness + binary homogeneous fragmentation structure + **one tagged-spine limit**, rather than recomputing every finite split rate. That is precisely the direction suggested by the wording immediately following Open Problem 18.

---

# Exact checker

Only after the permutation-cycle mechanism was identified did I build a finite exact checker:

`artifacts/R11/2026-09-17T02-41-27Z_c011_permutation_cycle_checker.py`

Creation/readback commit:

`0ce8a7fe48b890d52a312f4326ac320168b05c6a`.

Executed output:

`artifacts/R11/2026-09-17T02-41-27Z_c011_permutation_cycle_checker.out`

Creation/readback commit:

`22862d514cb19438ec20b02a2cbcce4921fc3b4a`.

The checker exhaustively enumerates permutation cycle decompositions through `m=8`, checks every two-cycle support count, checks 2,600 exact hidden beta-projection identities, 4,494 activated-slot compiler identities, the `2/105` degree-three witness, the positive degree-four witness `1/73728`, and the exact `N^2 epsilon_N=1/N` interaction scale. It records 8,601 exact checks and ends

`ALL_EXACT_CHECKS_PASS`.

Output SHA-256:

`3f87f67e606167da5e3f5b4936f2a075f9d2f7f9cf56f29db7c224f5f4938d7c`.

The checker certifies the finite combinatorial core only; the asymptotic whole-path theorem is proved above on the page.

---

# Prior art and source-intent caveat

The combinatorial ingredients `(i-1)!` cycle counts and unsigned Stirling numbers of the first kind are classical. Random-permutation cycle split/merge dynamics are also classical. The binary tagged-fragment/dislocation transform is general homogeneous-fragmentation theory and is explicitly invoked by Aldous--Janson Part III, Remark 4.7.

What I did **not** find in the bounded current search is the paired rare exactly-two-cycle proposal model with common-refinement interactions, its full projective CTCS limit theorem, or this specific use as an Open Problem 18 answer. Negative search is not novelty certification.

C011 is more source-facing than another inverse-profile weighted tree: it is built from a standard, unweighted combinatorial object (uniform permutations), and the beta kernel falls out of cycle counting. Nevertheless the `exactly two cycles` filter and rare pairing are deliberate design choices. Whether Aldous--Janson would regard this as sufficiently "superficially different" remains an independent source-intent judgment. The campaign therefore remains PARTIAL pending audits rather than declaring closure after one worker's construction.

# Audit status

A fresh repository search still finds only scoped R10 passes for earlier C002--C007 components. No P26 end-to-end I0054 audit, no second OTHER-track end-to-end audit of the current source-level package, and no C009/C010/C011 audit were found. Older scoped passes are not promoted into C011 evidence.

No paper package was created.

# Runtime-control status

The scheduler limitation remains unchanged. The interface exposed to this worker provides prompt/title, schedule, enablement and timing mode, but no model-family or reasoning-effort selector. Therefore GPT-6 / maximum remains a prompt request rather than verified runtime telemetry. The current repository operations record also shows that historical `You cannot modify this task` errors were permission/context dependent: P26 later succeeded in an authorized context, while R-series edits were denied in another. The legitimate remedy is an authorized task/account/workspace-owner control surface that owns the existing task and exposes model/reasoning controls, or a platform/product change/support intervention. Bypassing permission boundaries or cloning a denied task is not a valid workaround. This run made no scheduler changes, as required by the deployment.

# Next new-method triple

Do not repeat #12/#23/#27 next run. Record:

- **#16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE** — classify small finite combinatorial species whose one-event split coefficients already equal or approach the beta kernel without tuning;
- **#18 SAY IT IN ANOTHER LANGUAGE** — translate the tagged-subordinator criterion into regenerative compositions / occupancy gaps to exploit the 2026 balls-in-boxes representation;
- **#26 HUNT THE SPORADIC CASE** — search for natural models that satisfy the tagged-spine criterion but fail binary/tightness assumptions, to identify the exact boundary of the universality statement.

The next high-value goal is not metric inflation by trivial Euler variants. It is a natural model for which U002 reduces the proof to a genuine subordinator approximation, matching the source's own hint.

```yaml
ledger_delta:
  track: R11
  intake: I0054
  source: Aldous-Janson arXiv:2303.02529v3 Open Problem 18
  metric_name: number_of_distinct_nontrivial_discrete_model_classes_with_complete_required_limit_proof
  metric_before: 10
  metric_after: 11
  movement: true
  status: PARTIAL
  new_claims:
    - id: R11-I0054-C011
      label: PROVED_author_side_under_frozen_equivalence
      statement: paired rare uniform-permutation two-cycle common-refinement hierarchy converges to CTCS(infinity) in projective finite-restriction Skorokhod topology
    - id: R11-I0054-U002
      label: PROVED_source_facing_specialization_of_known_fragmentation_theory
      statement: in conservative zero-erosion homogeneous binary fragmentations, the tagged-fragment subordinator Levy measure uniquely determines the dislocation measure; CTCS tagged Levy density forces dx/[x(1-x)]
  exact_artifacts:
    checker: artifacts/R11/2026-09-17T02-41-27Z_c011_permutation_cycle_checker.py
    checker_commit: 0ce8a7fe48b890d52a312f4326ac320168b05c6a
    output: artifacts/R11/2026-09-17T02-41-27Z_c011_permutation_cycle_checker.out
    output_commit: 22862d514cb19438ec20b02a2cbcce4921fc3b4a
    output_sha256: 3f87f67e606167da5e3f5b4936f2a075f9d2f7f9cf56f29db7c224f5f4938d7c
    exact_checks: 8601
  source_current_check: PASS_bounded_2026-09-17
  ownership: R11_provisional_exclusive_PENDING_ADMISSION_not_READY
  audits_required: 2
  audits_complete_for_C011: 0
  paper_package: none
  old_SAW_route: retired_preserved
  P13_I0051: distinct_not_reassigned
  runtime_model: GPT-5.6_Sol
  runtime_reasoning: UNVERIFIED
  requested_model: GPT-6_maximum_prompt_only
  next_methods: [16, 18, 26]
```
