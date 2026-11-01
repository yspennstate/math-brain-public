Model: GPT-5.6 Sol. Reasoning: UNVERIFIED runtime level; GPT-6 / maximum was requested, but no model-family or reasoning-effort selector is exposed, so GPT-6 / maximum is not verified or claimed. Metric movement: `23 -> 24` distinct nontrivial discrete model classes with complete author-side whole-limit proofs under the frozen equivalence convention. Section-B moves actually tried: **#6 (deform to a solved point), #12 (find what is conserved), #24 (find the extremal object)**.

Problem/source: David J. Aldous and Svante Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529v3, **Open Problem 18**, intake `I0054`. Overall campaign status remains **PARTIAL, not CLOSED**. This run proves a sparse-deformation transfer theorem `R11-I0054-U008` and a new finite-locus shared-parent pedigree class `R11-I0054-C024`. The canonical claim remains `PENDING_ADMISSION, not READY`; publication novelty remains unverified; the source's informal word “superficially” still requires independent judgment; and the required P26 plus second OTHER-track end-to-end audits remain absent.

# R11 I0054 — a sparse extremal shared-parent pedigree deformation still converges to CTCS(infinity)

Run ID: `2026-09-17T15-40-00Z_i0054-sparse-shared-parent-c024-6a1f`  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Dated source/literature check: 2026-09-17

No email/Gmail, Drive, public posting, purchase, permission change, workflow execution, scheduler change, shared-root edit, or peer-track edit was performed.

---

## 1. Continuity, source, ownership, and current state

I continued from the newest complete R11 report

`runs/R11/2026-09-17T14-40-48Z_i0054-finite-locus-shared-victim-c023-b7e2.md`

rather than restarting. That report moved the metric `22 -> 23`, proved C023 and U007, and prescribed the nonrepeating triple `#6/#12/#24`; those are the three methods used here.

Before new mathematics I read/recovered the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/claims/I0054.md`, `operations/NEW_METHODS_2026-09-16.md`, the newest R11 report, the newest neighboring P13/I0051 state, current exact I0054 audit searches, and targeted intake/source/ownership hits. The GitHub connector is bounded/search-oriented and does not expose a credible byte-for-byte “read the entire private repository” operation, so I do not pretend to have manually reread every file or all roughly 780 intake rows. The exact I0054 claim/source/history needed for this run was recovered directly.

The canonical I0054 claim still says owner `R11`, source arXiv:2303.02529v3 Open Problem 18, and status `PENDING_ADMISSION, not READY`. P13 remains the distinct Open Problem 9 clade-count problem and is not reassigned. R11's old planar self-avoiding-walk route remains retired with immutable history.

The current primary source remains arXiv v3, dated 17 April 2025 / revised 18 April 2025. On PDF page 58 the source asks:

> Open Problem 18. Are there superficially different discrete models whose limit is the same CTCS(infinity)?

and immediately says that the key feature appears to be the subordinator approximation and asks whether it can arise in another discrete tree model. The same paper and Part III formalize CTCS(infinity) through consistent exchangeable partitions. Accordingly the target here remains convergence of every fixed finite restriction as an entire partition-valued path in Skorokhod `J_1`, followed by convergence in the projective finite-restriction topology. A root marginal, tagged fragment, height law, or one-time split law is not accepted as the target.

### Runtime/model-control status

The runtime identifies as GPT-5.6 Sol; reasoning effort is not exposed and is therefore `UNVERIFIED`. The available scheduler interface exposes title/prompt, schedule, enablement, and timing mode but no model-family or reasoning-effort field. GPT-6/maximum remains prompt-only. Current repository policy records permission/context failures such as `You cannot modify this task`; the legitimate remedy is an authorized owner/workspace control surface or platform support, not cloning/bypassing the task. No scheduler modification was attempted in this run.

---

## 2. Dated literature / prior-art screen

The current source still contains Open Problem 18. The 2026 homogeneous-fragmentation paper of Chorbadzhiyska--Minchev--Savov studies beta-splitting asymptotics, tagged subordinators, heights and related quantities; Heng Ma's September 2026 work addresses other Aldous--Janson questions. I did not find a later paper announcing a discrete-model resolution of Open Problem 18. This is a bounded negative search, **not** a novelty certificate.

The population-genetic ingredients are not new. Esser--Probst--Baake study finite-locus Moran recombination and linkage disequilibria. King--Wakeley--Carmi show that even unlinked loci can retain weak correlations through a shared population pedigree. The potentially new claim here is only the particular **sparse extremal shared-parent deformation of the C023 finite-locus hierarchy and its full CTCS limit**, together with the abstract sparse-deformation transfer lemma below.

A current exact repository search still recovers no `P26-AUDIT-R11-I0054` end-to-end current-package PASS and no second complete current-package OTHER-track PASS.

---

## 3. Move #6 — deform C023 toward a genuinely shared-parent pedigree

C023 has one victim site shared by the whole genome in each population generation, but its parent choices are independent across loci. The next natural deformation is to introduce genuine shared-parent pedigree events.

Retain C023's scales

\[
m_N=\lceil N^{1/4}\rceil,\qquad
\Delta_N=\alpha_N=\frac1{m_N},\qquad
L_N=N,
\tag{3.1}
\]

and mutation probability

\[
\mu_N=\frac{\alpha_N}{N+2\alpha_N}.
\tag{3.2}
\]

Define the new pedigree-event probability

\[
\boxed{\rho_N=\Delta_N^3.}
\tag{3.3}
\]

There are `N` population sites and `L_N=N` binary loci, initially independent with the C023 stationary one-locus law

\[
\nu_{N,\alpha}(x)
=
\frac{(\alpha)_{|x|}(\alpha)_{N-|x|}}{(2\alpha)_N}.
\tag{3.4}
\]

Each raw generation proceeds in the following order.

1. Choose one victim site `V_r` uniformly from `[N]`.
2. Toss `S_r ~ Bernoulli(rho_N)`.
3. If `S_r=0`, every locus independently chooses a parent uniformly from all `N` sites, copies that allele, mutates with probability `mu_N`, and writes the result at the shared victim. This is the C023 population update.
4. If `S_r=1`, choose **one common parent** `P_r` uniformly from `[N]\{V_r}`. Every locus copies its allele from that same parent site, with independent mutation bits, into the common victim.
5. After the population update, each current nonsingleton tree block hashes independently and uniformly into the finite locus pool, samples distinct population sites uniformly without replacement, and splits by the two sampled allele colors if nonmonochromatic.

Thus rare generations use a literal shared parent across the entire finite genome. The population is persistent; it is not restarted after a tree split.

The query-after-update convention is only a one-step placement choice. If the `S_r=1` branch is deleted, fixed-victim reversibility from C023 implies that each ordinary update preserves the exact one-locus law (3.4), conditionally on the victim sequence, so the finite-pool U007 proof still gives the same CTCS limit for this query-after-update baseline.

---

## 4. Theorem U008 — sparse-deformation stability

The useful result from move #6 is more general than C024.

### Theorem U008

For each `N` let `X_N` and `Y_N` be discrete-time processes with raw step duration `Delta_N`. Suppose they can be coupled from the same initial visible state so that, conditional on having agreed through raw step `r`, their next raw updates can be chosen equal with probability at least `1-rho_N`, uniformly in the common past. Assume

\[
\Delta_N\to0,
\qquad
\frac{\rho_N}{\Delta_N}\to0.
\tag{4.1}
\]

If for every fixed `k`, the rescaled finite restriction `X_N^[k]` converges in Skorokhod `J_1` on bounded intervals to a càdlàg limit `X^[k]`, then `Y_N^[k]` has the same limit. If the finite restrictions are projectively consistent, the same conclusion holds in the projective finite-restriction topology.

### Proof

Fix `k,T` and couple the two processes as above. There are at most

\[
M_N(T)=\left\lceil\frac{T}{\Delta_N}\right\rceil+1
\]

raw updates by physical time `T`. A union bound at the first disagreement gives

\[
P\{X_N^{[k]}\neq Y_N^{[k]}\text{ somewhere on }[0,T]\}
\le M_N(T)\rho_N
\le \left(\frac{T}{\Delta_N}+2\right)\rho_N
\longrightarrow0.
\tag{4.2}
\]

Hence the laws of the two restricted paths on `D([0,T])` have total-variation distance tending to zero. Convergence of one therefore implies convergence of the other in `J_1`. For the projective metric, fix a finite restriction large enough that the deterministic metric tail is below an arbitrary epsilon, apply the finite-restriction statement there, then let epsilon decrease. `QED`.

For C024,

\[
\frac{\rho_N}{\Delta_N}=\Delta_N^2\to0.
\tag{4.3}
\]

Couple C024 to the query-after-update C023 baseline with identical victims, ordinary parent choices, mutations, hashes and tree samples until the first `S_r=1` generation. Equation (4.2) then applies directly. The baseline satisfies U007 because

\[
L_N\Delta_N^2
=
\frac{N}{\lceil N^{1/4}\rceil^2}
\longrightarrow\infty,
\tag{4.4}
\]

and its fresh-locus split probabilities obey

\[
p_N(i,j)
=
\frac{2(\alpha_N)_i(\alpha_N)_j}{(2\alpha_N)_{i+j}}
=
\Delta_N B(i,j)+O_{i+j}(\Delta_N^2).
\tag{4.5}
\]

Therefore for every fixed `k`,

\[
\boxed{
\widehat\Pi_{N,\mathrm{C024}}^{[k]}
\Longrightarrow
\Pi_{\mathrm{CTCS}}^{[k]}
\quad\text{in }J_1,
}
\tag{4.6}
\]

and hence

\[
\boxed{
\widehat\Pi_{N,\mathrm{C024}}
\Longrightarrow
\Pi_{\operatorname{CTCS}(\infty)}
}
\tag{4.7}
\]

in the full projective finite-restriction topology.

This is a whole-genealogy convergence argument. The proof does not infer the limit from a stationary split marginal.

---

## 5. Move #12 — the conserved distinction is parent-sharing excess

The deformation is small in physical time but is not a relabeling or time-rescaling of C023 at finite `N`.

For two distinct loci, let `P^(1),P^(2)` be the parental site indices used in one population reproduction event, and define the **parent-sharing excess**

\[
\chi_N
:=P(P^{(1)}=P^{(2)})-\frac1N.
\tag{5.1}
\]

In C023, parents are independent uniform sites, so

\[
\chi_N^{\mathrm{C023}}=0.
\tag{5.2}
\]

In C024,

\[
P(P^{(1)}=P^{(2)})
=(1-\rho_N)\frac1N+\rho_N,
\]

and therefore

\[
\boxed{
\chi_N^{\mathrm{C024}}
=\rho_N\left(1-\frac1N\right)>0.
}
\tag{5.3}
\]

A deterministic relabeling of population sites or loci preserves equality of parental indices, and a global rescaling of branch/time units does not change the within-event coupling. Thus the zero/nonzero value of this finite-event dependence is an exact model-level invariant under the frozen equivalence convention.

Because the campaign has so far preferred tree-visible finite witnesses, I also computed one below; (5.3) is not used as the sole separation certificate.

---

## 6. Move #24 — common-parent coupling is the extremal positive pedigree coupling

Among all couplings of two uniform parent indices on `[N]`, the common-parent coupling is the maximally positively linked one.

Let `P_1,P_2` each be uniform on `[N]` under an arbitrary coupling, and let `phi:[N]->R` have uniform mean zero. Then Cauchy--Schwarz gives

\[
\operatorname{Cov}(\phi(P_1),\phi(P_2))
\le
\sqrt{E\phi(P_1)^2E\phi(P_2)^2}
=
\operatorname{Var}_{U_N}(\phi).
\tag{6.1}
\]

The common-parent coupling `P_1=P_2` attains equality simultaneously for every `phi`. In particular

\[
P(P_1=P_2)\le1,
\tag{6.2}
\]

with equality for the shared-parent event, whereas independent parents have equality probability `1/N`.

Thus C024 does not introduce an arbitrary weak correlation mechanism: with probability `rho_N` it inserts the **extremal positive parent coupling**, and with probability `1-rho_N` it uses the independent C023 coupling. The asymptotic CTCS limit survives because the frequency of these extremal events is `o(Delta_N)`.

This identifies a clean obstruction for the next route. A non-sparse shared pedigree cannot be treated by U008; one must instead exploit mixing/recombination or prove that its accumulated linkage contribution is negligible by a separate mechanism.

---

## 7. Exact tree-visible finite non-equivalence witness

At `N=4`,

\[
m_4=2,\qquad
\alpha_4=\Delta_4=\frac12,
\qquad
\mu_4=\frac1{10},
\qquad
\rho_4=\frac18.
\tag{7.1}
\]

For a particular four-label support, the ordinary C023 stationary law gives

\[
p_{13}^{(0)}=\frac5{64},
\qquad
p_{22}^{(0)}=\frac3{64},
\qquad
\frac{p_{13}^{(0)}}{p_{22}^{(0)}}=\frac53.
\tag{7.2}
\]

For one shared-parent event, exact enumeration over the sixteen one-locus configurations, four victims, three allowed common parents, and the mutation bit gives

\[
p_{13}^{(1)}=\frac3{40},
\qquad
p_{22}^{(1)}=\frac{11}{240},
\qquad
\frac{p_{13}^{(1)}}{p_{22}^{(1)}}=\frac{18}{11}.
\tag{7.3}
\]

Since the first tree query occurs after that population update, C024's first-generation particular-support probabilities are

\[
p_{13}
=\frac78\frac5{64}+\frac18\frac3{40}
=\boxed{\frac{199}{2560}},
\tag{7.4}
\]

and

\[
p_{22}
=\frac78\frac3{64}+\frac18\frac{11}{240}
=\boxed{\frac{359}{7680}}.
\tag{7.5}
\]

Hence the exact first-generation split-support ratio is

\[
\boxed{
R_{\mathrm{C024}}
=\frac{597}{359}
\approx1.66295264624.
}
\tag{7.6}
\]

In particular

\[
R_{\mathrm{C024}}-R_{\mathrm{C023}}
=\frac{597}{359}-\frac53
=\boxed{-\frac4{1077}}\neq0.
\tag{7.7}
\]

The checker also compares (7.6) against every retained binary-class witness from the current R11 history:

\[
2,\quad \frac75,\quad \frac{2699}{1365},\quad
\frac{2273}{1153},\quad \frac{61381}{43765},\quad
\frac{166094447739}{85563797248},\quad \frac{33}{17},\quad \frac53,
\]

and finds no collision. The remaining retained classes are already separated by positive finite multifurcation witnesses. The particular-support ratio is preserved by deterministic leaf relabeling and by a global branch/time rescaling.

Therefore the stable author-side class claim is

\[
\boxed{\texttt{R11-I0054-C024 = PROVED\_AUTHOR\_SIDE under frozen equivalence}.}
\tag{7.8}
\]

Together with U008, the fixed metric moves

\[
\boxed{23\longrightarrow24}.
\tag{7.9}
\]

---

## 8. Exact self-check

The exact-arithmetic checker is

`artifacts/R11/2026-09-17T15-40-00Z_c024_sparse_shared_parent_check.py`

creation/readback commit `b503ad4ad8186fbeccf2778b87d84c64429850a1`.

Its archived output is

`artifacts/R11/2026-09-17T15-40-00Z_c024_sparse_shared_parent_check.out`

creation/readback commit `dbacb459f8eb4ea3a0acb11a6195bdf9cd16c2c3`.

The executed checker performed **4,001 exact rational checks**. It verifies fixed-victim invariance for the ordinary C023 update over `N=2,...,8`, the U008 scaling identities, the parent-sharing excess formula, the full `N=4` shared-parent transition enumeration, the exact probabilities (7.2)--(7.7), and noncollision with every retained binary witness. The output ends

`ALL_EXACT_CHECKS_PASS`.

Recorded hashes:

- checker SHA-256: `e0bcec91c5ee8db22f3ff2edece7e827f1619be97322c3a3620b50d92ec79c9e`;
- stdout SHA-256: `25b6e752d6357c0fbe6f7f40ed8b6555704dc133a52ba93e3ac9236968ed9e2a`.

This is a **self-check**, not an independent audit.

---

## 9. Why the source is still not called closed

I do **not** promote Open Problem 18 to CLOSED.

1. `operations/claims/I0054.md` remains `PENDING_ADMISSION, not READY`.
2. No `P26-AUDIT-R11-I0054` current-package end-to-end PASS is recovered.
3. No second independent current-package OTHER-track PASS is recovered.
4. The source deliberately says “superficially different”; independent source-intent review remains necessary.
5. C024 is mathematically distinct under the frozen convention, but its shared-parent events are deliberately sparse enough to vanish under the U008 coupling. It is therefore a useful universality theorem/example, but **less source-facing as a natural alternative model than C021--C023**. I do not hide that qualification.
6. The current literature search is bounded and does not certify novelty.

Accordingly the source-level status remains **PARTIAL** even though U008 and C024 are complete author-side arguments.

---

## 10. What the three methods taught us

- **#6 — deform to a point you can solve:** a rare-deformation transfer principle is enough to carry the full `J_1`/projective CTCS limit from C023 to a genuine shared-parent pedigree model.
- **#12 — find what is conserved:** the parent-sharing excess `chi_N` cleanly detects finite pedigree coupling and is invariant under the frozen relabeling/rescaling convention.
- **#24 — find the extremal object:** common-parent reproduction is the extremal positive coupling of uniform parent choices; C024 mixes that extremal event with the independent-parent mechanism.

The next genuinely hard step is now sharply isolated: replace `rho_N=o(Delta_N)` by a non-sparse shared-parent/two-parent pedigree and prove that recombination or another averaging mechanism kills the accumulated linkage without appealing to the trivial no-event coupling.

Next nonrepeating methods recorded for that route: **#14 (find the group acting), #20 (find why the algorithm fails), #28 (replace for-all with typical)**.

---

```yaml
ledger_delta:
  track: R11
  intake: I0054
  source: "Aldous--Janson, arXiv:2303.02529v3, Open Problem 18"
  target: "genuinely different discrete models with full CTCS(infinity) exchangeable-partition limit"
  metric_name: "number of distinct nontrivial discrete model classes with complete whole-limit proof under frozen relabeling/rescaling equivalence"
  before: 23
  after: 24
  movement: true
  unchanged_streak_after: 0
  source_status: PARTIAL
  new_claims:
    - "R11-I0054-U008 = PROVED_AUTHOR_SIDE (sparse-deformation stability)"
    - "R11-I0054-C024 = PROVED_AUTHOR_SIDE under frozen equivalence"
  construction: "finite-locus persistent Moran genome with rare extremal common-parent events, rho_N=Delta_N^3"
  full_limit: "for every fixed k, J1 convergence of partition path; projective CTCS(infinity) convergence"
  finite_witness:
    N: 4
    p13: "199/2560"
    p22: "359/7680"
    ratio: "597/359"
    difference_from_C023: "-4/1077"
  exact_checker: "artifacts/R11/2026-09-17T15-40-00Z_c024_sparse_shared_parent_check.py"
  exact_output: "artifacts/R11/2026-09-17T15-40-00Z_c024_sparse_shared_parent_check.out"
  exact_checks: 4001
  self_check_result: ALL_EXACT_CHECKS_PASS
  p26_end_to_end_audit: ABSENT
  second_other_track_audit: ABSENT
  canonical_claim: "PENDING_ADMISSION, not READY"
  novelty: UNVERIFIED
  methods_actual: [6, 12, 24]
  next_methods: [14, 20, 28]
  next_obligation: "non-sparse shared-parent/two-parent pedigree: prove or refute that recombination makes accumulated linkage negligible"
```
