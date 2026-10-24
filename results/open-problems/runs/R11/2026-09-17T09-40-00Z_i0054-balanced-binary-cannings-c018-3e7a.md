Model: GPT-5.6 Sol. Reasoning: UNVERIFIED runtime level; GPT-6 / maximum was requested in prompt text, but the exposed scheduler has no model-family or reasoning-effort selector, so GPT-6 / maximum is not verified or claimed. Metric movement: `17 -> 18` distinct nontrivial discrete model classes with complete author-side whole-limit proofs under the frozen equivalence convention. Section-B moves actually tried: **#10 (derandomize), #14 (find the group acting), #21 (ask who else has this shape)**.

Problem/source: David J. Aldous and Svante Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529v3 (18 April 2025), **Open Problem 18**, intake `I0054`. Overall campaign status remains **PARTIAL, not CLOSED**. The new class `R11-I0054-C018` below has a complete author-side whole-path convergence argument and exact finite self-check, but the canonical claim is still `PENDING_ADMISSION, not READY`; the source's deliberately informal word “superficially” still needs independent source-intent judgment; and the required P26 plus second OTHER-track end-to-end audits are absent.

# R11 I0054 — balanced-binary Cannings genealogies give CTCS(infinity)

Run ID: `2026-09-17T09-40-00Z_i0054-balanced-binary-cannings-c018-3e7a`  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Dated source/literature check: 2026-09-17

No email/Gmail, Drive, public posting, purchase, permission change, workflow execution, scheduler change, shared-root edit, or peer-track edit was performed.

---

## 1. Continuity, source, ownership, topology

I continued from the newest completed R11 report

`runs/R11/2026-09-17T08-42-35Z_i0054-polya-cannings-u005-c017-a7f2.md`

rather than restarting. That run moved the metric `16 -> 17`, proved the Pólya-Cannings class C017, and prescribed the nonrepeating method triple `#10/#14/#21`; those are the methods used here.

Before new research I recovered the required campaign surfaces available through the bounded GitHub connector: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/claims/I0054.md`, `operations/NEW_METHODS_2026-09-16.md`, the newest R11 report, the neighboring P13/I0051 status, and targeted intake/audit/ownership hits. The connector does not expose a credible byte-for-byte “read the whole repository” operation, so I do not pretend to have manually reread every intake row. The exact I0054 source/owner record and current R11 history were recovered directly.

The canonical claim remains:

- owner: `R11`;
- source: Aldous--Janson v3, Open Problem 18;
- status: `PENDING_ADMISSION, not READY`.

P13 remains on the distinct current-v3 Open Problem 9 clade-count/joint-law target. The old R11 planar self-avoiding-walk route remains retired with its immutable history preserved.

I rechecked the current v3 source. Section 6.3 still states:

> Open Problem 18. Are there superficially different discrete models whose limit is the same CTCS(infinity)?

and immediately asks whether the key subordinator approximation can arise in another discrete tree model. The current arXiv record says v3 was last revised 18 April 2025. The source formalizes CTCS(infinity) through consistent exchangeable partitions, so the target here remains convergence of the **whole partition path**, not a tagged height or one-dimensional marginal.

For each fixed restriction `[k]` the path topology is Skorokhod `J_1`; the full projective metric is

\[
d_{\rm proj}(\omega,\eta)
=\sum_{k\ge1}2^{-k}\bigl(1\wedge d_{J_1,k}(\omega^{[k]},\eta^{[k]})\bigr).
\]

For a visible block of size `b=i+j` and a specified unordered split `A|A^c`, `|A|=i`, the CTCS particular-split rate is

\[
q_b(A\mid A^c)=B(i,j)
=\frac{(i-1)!(j-1)!}{(b-1)!}.
\]

### Runtime/model control

The actual runtime identifies as GPT-5.6 Sol. Reasoning effort is not exposed and is therefore `UNVERIFIED`. The scheduler/update surface available to this worker offers prompt/title, schedule, enabled state, and timing mode, but no model-family or reasoning-effort field. GPT-6/maximum is prompt text only. The repository policy also records that `You cannot modify this task` can be permission/context dependent. The legitimate fix is the authorized task/account/workspace-owner interface that owns the task and exposes the desired control, or a platform/support change. I did not clone, bypass, or modify any scheduler task.

---

## 2. Dated current-literature and prior-art screen

The bounded 2026-09-17 screen checked the current Aldous--Janson v3 source, current 2026 critical-beta-splitting papers, and combinations of `CTCS`, `critical beta splitting`, `Cannings`, `fixed offspring vector`, `exchangeable offspring`, `random permutation`, `matching`, `Kingman`, `fragmentation`, and `discrete model`.

Relevant prior art found:

1. Cannings models are classical: an offspring vector is exchangeable, nonnegative, sums to population size, and generations are independent in the fixed-population model. I make no novelty claim for that framework or for Kingman-domain genealogy criteria.
2. Modern work on exchangeable coalescents explicitly notes that randomly permuting the entries of a fixed offspring-size vector renders it exchangeable and hence gives a Cannings model. Thus the **population mechanism below is squarely within known Cannings theory**; I do not claim the balanced `0/2` offspring vector itself as a new population-genetics model.
3. Chorbadzhiyska--Minchev--Savov, arXiv:2608.18320 (18 Aug 2026), embed the beta-splitting family in homogeneous fragmentation and analyze tagged subordinators/heights; the abstract says the critical result resolves an open problem, but it is a height-related one, not Open Problem 18.
4. Ma, arXiv:2609.14329 (13 Sep 2026), resolves Aldous--Janson Open Problem 4 on the discrete-time height, not Open Problem 18.

I found no current paper in this bounded search claiming the specific rare-mark/common-refinement hierarchy below as a resolution of Open Problem 18. This is a **bounded negative search, not a novelty certificate**.

Repository audit search still finds only scoped R10 checks of older C002--C007/U001 components. An exact search for `P26-AUDIT-R11-I0054` returns no result, and no second complete current-package OTHER-track audit is recovered.

---

## 3. Move #10 — derandomize the offspring counts

C017 used a random Pólya/Dirichlet-multinomial offspring vector. The new idea is to remove that source of randomness almost completely.

Fix population size `N`. In each forward population generation use the following deterministic family-size multiset:

- if `N` is even: `N/2` parents have exactly two offspring and `N/2` parents have zero offspring;
- if `N` is odd: `(N-1)/2` parents have two offspring, one parent has one offspring, and `(N-1)/2` parents have zero offspring.

Randomize only by a fresh uniform permutation of the parent labels and a uniform assignment of the `N` labelled offspring positions to the resulting family blocks. Equivalently, the offspring positions form a uniform perfect matching when `N` is even, and a uniform near-perfect matching plus one singleton when `N` is odd; the family blocks are then injectively assigned to parent labels.

This is a neutral Cannings model with an exchangeable offspring vector, but the vector's multiset is deterministic. No parent ever has more than two offspring.

Call this the **balanced-binary Cannings population**.

---

## 4. Move #14 — the symmetric-group action gives the genealogy exactly

The symmetric group action on the uniformly matched offspring positions makes the finite ancestral collision law explicit.

For two specified sampled offspring, the one-generation coalescence probability is

\[
\boxed{
c_N=
\begin{cases}
\dfrac1{N-1},&N\text{ even},\\[4pt]
\dfrac1N,&N\text{ odd}.
\end{cases}}
\tag{4.1}
\]

For even `N`, the partner of the first offspring is uniform among the other `N-1`; for odd `N`, the first offspring is paired with probability `(N-1)/N`, and conditional on being paired its partner is uniform among `N-1` positions.

More generally, for `h` specified disjoint sampled pairs,

\[
\Pr(\text{all }h\text{ pairs coalesce})=
\begin{cases}
\displaystyle
\frac1{(N-1)(N-3)\cdots(N-(2h-1))},&N\text{ even},\\[8pt]
\displaystyle
\frac1{N(N-2)\cdots(N-2h+2)},&N\text{ odd}.
\end{cases}
\tag{4.2}
\]

This is proved by exposing the required pairs sequentially in the uniform matching/near-matching. In particular, for every fixed sample size `r`, the probability of two or more simultaneous pair collisions is `O_r(c_N^2)`. Triple mergers have probability exactly zero because every family has size at most two.

Hence the finite ancestral partition kernel satisfies

\[
\boxed{K_{N,r}=I+c_NG_r+O_r(c_N^2),}
\tag{4.3}
\]

where `G_r` is the Kingman generator normalized so that each specified pair merges at rate one.

This is also exactly sampling-consistent at fixed `N`: trace any finite sample through the same exchangeable uniform matching, then delete any subset of the sampled labels. The resulting visible parent partition has the same law as tracing that smaller visible sample directly. Hidden sample labels merely disappear from the restriction.

The exact checker enumerates all perfect/near-perfect matchings for `3 <= N <= 9` and verifies (4.2), then checks the two-pair `O(c_N^2)` ratio exactly through `N=100`; the maximum checked ratio is exactly `3` (at `N=4`).

---

## 5. Move #21 — the known Cannings shape plus U005 gives a new CTCS compiler

The previous R11 report proved the general **Kingman-domain ancestral compiler theorem** `R11-I0054-U005`. Its hypotheses are precisely the shape exposed by (4.3): if an exchangeable, sampling-consistent ancestral chain obeys

\[
K_{N,m}=I+c_NG_m+O_m(c_N^2),\qquad c_N\to0,
\]

and, writing `J_{N,m}` for the number of active-lineage marking opportunities before the MRCA,

\[
c_N^2\,\mathbb E J_{N,m}^2=O_m(1),
\]

then independently marking each active ancestral lineage with probability

\[
u_N=\frac{\delta_Nc_N}{2},\qquad \delta_N\to0,
\]

and taking the common refinement of all marked descendant bipartitions yields CTCS(infinity) in the full projective finite-restriction `J_1` topology.

For completeness, the second-moment hypothesis is immediate here. Whenever at least two ancestral lineages remain, choose any two of them. They coalesce in the next population generation with probability exactly `c_N`. Therefore the waiting time until **some** lineage-count decrease is stochastically dominated by a geometric(`c_N`) variable. There are at most `m-1` strict decreases before the MRCA. If `T_{N,m}` is the number of population generations to the MRCA, then it is stochastically dominated by a sum of `m-1` geometric(`c_N`) variables, and

\[
J_{N,m}\le mT_{N,m}.
\]

Consequently

\[
\boxed{c_N^2\,\mathbb E J_{N,m}^2=O_m(1).}
\tag{5.1}
\]

All U005 hypotheses are therefore verified directly.

---

## 6. C018 — the balanced-binary Cannings mutation-refinement hierarchy

Set

\[
\delta_N=\frac1N,
\qquad
u_N=\frac{\delta_Nc_N}{2}
=
\begin{cases}
\dfrac1{2N(N-1)},&N\text{ even},\\[4pt]
\dfrac1{2N^2},&N\text{ odd}.
\end{cases}
\tag{6.1}
\]

For every current nonsingleton hierarchy block `B`, independently in every raw hierarchy generation:

1. place its labels at distinct offspring positions in a fresh size-`N` balanced-binary Cannings population;
2. trace their ancestry backward through fresh independent balanced-binary generations until their MRCA;
3. before every parental-allocation step, independently mark every currently active ancestral lineage with probability `nu_N`;
4. a mark on a lineage carries the subset `S subset B` of present labels descending from that lineage;
5. at the MRCA, refine `B` by the common refinement of all nontrivial marked bipartitions `S | B\S`;
6. if there is no nontrivial marked split, leave `B` unchanged;
7. use independent genealogies for distinct current blocks and later raw hierarchy generations.

One raw hierarchy generation has physical duration `delta_N`.

Finite C018 is not simply the original beta-splitting tree with a rescaled edge clock. Its primitive finite population has deterministic balanced binary family sizes; multiple rare ancestral marks in one raw hierarchy generation can still create multifurcating refinement vertices.

---

## 7. Complete whole-path convergence proof

U005's branch-potential calculation uses the Kingman identity

\[
\mathbb E L_{m,i}=\frac2i
\]

for total branch length subtending `i` leaves. By exchangeability, a specified `i`-subset `A` therefore has potential `2/[i\binom mi]`, and including the complementary orientation `j=m-i` gives

\[
\frac{2}{i\binom mi}+\frac{2}{j\binom mj}
=2B(i,j).
\]

For a Kingman-domain ancestral chain with time scale `c_N`, the corresponding discrete ancestral opportunity potential is

\[
\frac{2}{c_N}B(i,j)+O_m(1).
\]

Multiplication by `nu_N=delta_N c_N/2` yields, for every specified unordered split,

\[
\boxed{
\Pr_N(A\mid A^c\text{ generated by one relevant mark})
=\delta_NB(i,j)+O_m(\delta_Nc_N).
}
\tag{7.1}
\]

By (5.1), two or more relevant marks in one genealogy have probability

\[
\Pr(M\ge2)
\le \frac{\nu_N^2}{2}\mathbb E J_{N,m}^2
=O_m(\delta_N^2).
\tag{7.2}
\]

Exact sampling consistency lets these estimates hold after restricting an arbitrarily larger hidden block to any fixed visible set. Therefore, for every fixed `[k]`, uniformly conditional on the hidden history,

\[
\boxed{
\left\|
P_N^{(k)}(\rho,\cdot)
-\left(I+\delta_NQ_{\rm CTCS}^{(k)}\right)(\rho,\cdot)
\right\|_{\rm TV}
=O_k(\delta_Nc_N+\delta_N^2).
}
\tag{7.3}
\]

On a bounded physical-time interval there are `O(1/delta_N)` raw generations. Iterated conditional maximal coupling thus gives total discrepancy

\[
O_k(c_N+\delta_N)=O_k(N^{-1})\longrightarrow0.
\tag{7.4}
\]

The comparison Euler chain `I+delta_N Q_CTCS^{(k)}` has `delta_N`-scaled geometric holding times converging to the correct exponential holding times and exactly the CTCS jump kernel. A `k`-label fragmentation has at most `k-1` proper visible refinements. Hence

\[
\widehat\Pi_N^{[k]}\Longrightarrow\Pi_{\rm CTCS}^{[k]}
\]

in Skorokhod `J_1` for every fixed `k`. Passing through `d_proj` gives

\[
\boxed{
\widehat\Pi_N\Longrightarrow\Pi_{\operatorname{CTCS}(\infty)}.
}
\tag{7.5}
\]

Thus `R11-I0054-C018` has the required **whole exchangeable-partition genealogy limit**, not only a marginal or tagged-fragment limit.

---

## 8. Exact finite non-equivalence witness

At `N=3`, the family-size multiset is `(2,1,0)`. Therefore three sampled population individuals deterministically become two ancestral lineages after the first backward generation: one uniformly chosen sibling pair and one singleton.

Here

\[
\delta_3=\frac13,\qquad c_3=\frac13,\qquad \nu_3=\frac1{18},\qquad a:=1-\nu_3=\frac{17}{18}.
\]

Let `T` be the number of two-lineage population generations before coalescence. Then `T` is geometric with success probability `1/3`, and

\[
L:=\mathbb E[a^{2T}]
=\frac{c_3a^2}{1-(1-c_3)a^2}
=\frac{289}{394}.
\tag{8.1}
\]

No visible refinement occurs exactly when none of the three initial lineages is marked and neither later two-lineage branch is ever marked, so

\[
\boxed{
P(\text{no visible refinement})
=a^3L
=\frac{1419857}{2297808}.
}
\tag{8.2}
\]

For a raw degree-three common refinement, either at least two of the three singleton lineages are marked before the deterministic `3 -> 2` merger, or exactly one member of the eventual sibling pair is marked initially and a later two-lineage mark supplies the transverse bipartition. Hence

\[
\begin{aligned}
P(\deg=3\text{ raw})
&=3\nu_3^2a+\nu_3^3
 +2\nu_3a^2(1-L)\\
&=\boxed{\frac{40589}{1148904}}.
\end{aligned}
\tag{8.3}
\]

The remaining visible mass is binary:

\[
P(\deg=2\text{ raw})
=\boxed{\frac{265591}{765936}}.
\tag{8.4}
\]

Suppressing zero-change hierarchy generations, the first visible root therefore satisfies

\[
\boxed{
P_{C018}(\deg(\text{first visible root})=3)
=\frac{81178}{877951}
\approx0.0924630190.
}
\tag{8.5}
\]

The retained `N=3` witnesses for C001--C017 are

\[
0,\frac1{10},\frac1{22},\frac16,\frac1{728},\frac17,
\frac1{71},\frac1{71},0,0,\frac2{105},
\frac{21521}{4909716},\frac{35}{1296},\frac{14}{2201},
\frac2{17},\frac{40589}{352998},\frac{70135}{515173}.
\]

The new value differs from all of them. The historical C007/C008 tie at `N=3` was already separated by their `N=4` invariant. Root-degree law is invariant under deterministic relabeling and global branch-length rescaling, so C018 is distinct under the frozen convention.

Therefore

\[
\boxed{\texttt{R11-I0054-C018 = PROVED author-side under frozen equivalence}}
\]

and the tracked metric moves

\[
\boxed{17\longrightarrow18}.
\]

---

## 9. Exact certificate

The exact-arithmetic checker was executed only after the mathematical route was established. It performs **241 exact checks**:

- exact matching/near-matching probabilities through `N=9`;
- the two-pair `O(c_N^2)` bound through `N=100`;
- the deterministic family-size / no-triple-merger property through `N=100`;
- the complete exact `N=3` root-degree witness;
- comparison against all retained C001--C017 `N=3` witnesses.

Archived checker:

`artifacts/R11/2026-09-17T09-40-00Z_i0054-balanced-binary-cannings-c018-3e7a_checker.py`

creation/readback commit:

`be0b5119113c49685f21485ea94bea3e9bda703a`

Local script SHA-256:

`4aef8a548d53d9c1af0ea6a2ce530cf53fb50214072f81f6c8126d79c89db7dd`

Archived output:

`artifacts/R11/2026-09-17T09-40-00Z_i0054-balanced-binary-cannings-c018-3e7a_checker_output.txt`

creation/readback commit:

`e2c177cadd62832f2a33b28b3cecb3adb4280499`

Raw stdout SHA-256:

`3fc4ffeb7314eebdfad61aaf9408338385ecd32017d0703cb01aa2a0b149090b`

The archived output ends

`TOTAL_EXACT_CHECKS=241`  
`ALL_EXACT_CHECKS_PASS`.

These are author self-checks, not independent audits.

---

## 10. What the three methods contributed

### #10 DERANDOMIZE — success

The random offspring-frequency mechanism of C017 was not essential. A deterministic balanced `0/2` (plus one `1` for odd population size) family-size vector, randomized only by exchangeable labels, already lies in the Kingman domain and compiles to CTCS after rare ancestral marking.

### #14 FIND THE GROUP ACTING — success

The action of the symmetric group reduces the entire one-generation ancestral law to uniform perfect/near-perfect matchings. That gives exact formulas (4.1)--(4.2), zero triple mergers, and direct `O(c_N^2)` control of simultaneous pair mergers without invoking an external asymptotic theorem.

### #21 ASK WHO ELSE HAS THIS SHAPE — success, with a novelty warning

Classical Cannings theory is exactly the surrounding language. Modern coalescent work explicitly treats a randomly permuted fixed offspring vector as a Cannings model. Therefore the finite population mechanism and its Kingman-domain behavior should be presented as classical/folklore-level population-genetic structure. The potentially new claim is only the **rare ancestral mark + common-refinement compiler and its full CTCS(infinity) hierarchy limit**. A bounded negative search does not certify publication novelty.

---

## 11. Closure status and next route

I am **not calling Aldous--Janson Open Problem 18 closed**. Missing closure obligations are unchanged:

1. canonical admission is still `PENDING_ADMISSION, not READY`;
2. no `P26-AUDIT-R11-I0054` end-to-end current-package PASS is recovered;
3. no second independent OTHER-track end-to-end current-package PASS is recovered;
4. independent source-intent judgment is still needed for the word “superficially.”

The mathematical metric nevertheless moves because C018 has a complete author-side convergence proof and a frozen-convention finite non-equivalence certificate.

For the next run, the nonrepeating section-B triple is **#15 (break symmetry on purpose), #5 (add a parameter and differentiate), #29 (add the points at infinity)**. The strongest next target is **not** C019 by another cosmetic Cannings offspring vector. It is to revisit the one-process obstruction from C016 and ask whether a natural many-locus/recombining population supplies the missing quenched self-averaging, so that one forward population/pedigree — rather than a freshly restarted genealogy in every hierarchy block — produces the CTCS hazards intrinsically. A useful failure would be an exact obstruction showing why recombination still cannot wash out the random single-genealogy hazard.

---

```yaml
ledger_delta:
  track: R11
  intake: I0054
  source: "Aldous--Janson, arXiv:2303.02529v3, Open Problem 18, Section 6.3"
  target: "genuinely different discrete models with full CTCS(infinity) exchangeable-partition limit"
  metric_name: "number of distinct nontrivial discrete model classes with complete author-side whole-limit proof under frozen relabeling/rescaling equivalence"
  metric_before: 17
  metric_after: 18
  movement: true
  new_claim: "R11-I0054-C018"
  new_class: "balanced-binary Cannings mutation-refinement hierarchy"
  claim_status: "PROVED_AUTHOR_SIDE"
  campaign_status: "PARTIAL"
  canonical_admission: "PENDING_ADMISSION_NOT_READY"
  methods_tried: [10, 14, 21]
  exact_checks: 241
  checker_output: "ALL_EXACT_CHECKS_PASS"
  stagnation_count: "UNKNOWN"
  closure_missing:
    - "P26 end-to-end I0054 audit"
    - "second independent OTHER-track end-to-end current-package audit"
    - "independent source-intent/admission judgment"
  next_methods: [15, 5, 29]
  next_target: "one-process recombining/many-locus quenched self-averaging construction or exact obstruction"
```
