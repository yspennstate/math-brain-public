Model: GPT-5.6 Sol. Reasoning: UNVERIFIED runtime level; GPT-6 / maximum was requested, but no model-family or reasoning-effort selector is exposed, so GPT-6 / maximum is not verified or claimed. Metric movement: `22 -> 23` distinct nontrivial discrete model classes with complete author-side whole-limit proofs under the frozen equivalence convention. Section-B moves actually tried: **#9 (randomize), #21 (ask who else has this shape), #30 (one scale at a time)**.

Problem/source: David J. Aldous and Svante Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529v3, **Open Problem 18**, intake `I0054`. Overall campaign status remains **PARTIAL, not CLOSED**. This run proves a new finite-locus class `R11-I0054-C023` and a finite-pool compiler theorem `R11-I0054-U007`. The canonical claim remains `PENDING_ADMISSION, not READY`; publication novelty remains unverified; the source's informal word “superficially” still requires independent judgment; and the required P26 plus second OTHER-track end-to-end audits remain absent.

# R11 I0054 — a finite-locus shared-victim Moran/recombination hierarchy converges to CTCS(infinity)

Run ID: `2026-09-17T14-40-48Z_i0054-finite-locus-shared-victim-c023-b7e2`  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Dated source/literature check: 2026-09-17

No email/Gmail, Drive, public posting, purchase, permission change, workflow execution, scheduler change, shared-root edit, or peer-track edit was performed.

---

## 1. Continuity, source, ownership, and current repository state

I continued from the newest complete immutable R11 report

`runs/R11/2026-09-17T13-46-48Z_i0054-multilocus-moran-c022-8f31.md`

rather than restarting. That report moved the fixed metric `21 -> 22`, proved C022, and prescribed the nonrepeating triple `#9/#21/#30`; those are the three methods used here.

Before new mathematics I recovered/read the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, current root-ledger/queue search surfaces, `operations/claims/I0054.md`, `operations/NEW_METHODS_2026-09-16.md`, the newest R11 I0054 report, the neighboring P13/I0051 ownership record and latest P13 report, and current searches for I0054 audit identifiers. The large intake JSONL collections cannot be rendered byte-for-byte through the connector in one response, so I do not claim a manual reread of all roughly 780 rows; targeted exact-source/ownership searches recovered the relevant I0054 surface.

The canonical I0054 claim still says owner `R11`, source arXiv:2303.02529v3 Open Problem 18, and status `PENDING_ADMISSION, not READY`. P13/I0051 remains the distinct Open Problem 9 clade-count problem and is not reassigned here. R11's old planar-SAW route remains retired with immutable history. Root R-series ledger material remains partly stale relative to the current I0054 immutable reports; I did not edit shared roots.

The current arXiv source remains v3, revised 18 April 2025. Section 6.3 still asks whether there are “superficially different discrete models whose limit is the same CTCS(infinity)” and immediately points to the characteristic subordinator approximation as the feature one might reproduce in another discrete tree model. The same source describes CTCS(infinity) via the consistent exchangeable-partition system. Thus the target retained here is the strong one used in recent R11 runs: for every fixed `[k]`, convergence of the entire partition-valued genealogy path in Skorokhod `J_1`, then convergence in the projective finite-restriction topology. A tagged-leaf, height, root-shape, or one-time marginal limit is insufficient.

For a block of size `b=i+j` and a specified unordered split `A|A^c`, `|A|=i`, the CTCS infinitesimal rate is

\[
q_b(A\mid A^c)=B(i,j)=\frac{(i-1)!(j-1)!}{(b-1)!}.
\tag{1.1}
\]

### Runtime/model-control status

The runtime identifies as GPT-5.6 Sol; reasoning effort is not exposed and is therefore `UNVERIFIED`. The task interface available here exposes title/prompt, schedule, enablement, and timing mode, but no model-family or reasoning-effort field. GPT-6/maximum is therefore prompt text only. The current operations policy records permission-context failures such as `You cannot modify this task`; the legitimate remedy is the authorized owner/workspace control surface or platform support, not cloning or bypassing the existing task. This run made no scheduler modification attempt, as the deployment instruction forbids it.

---

## 2. Current literature / prior-art screen

The dated search checked the original arXiv source, later 2026 beta-splitting work, and finite-locus Moran/recombination literature. The source still contains Open Problem 18. Heng Ma's arXiv:2609.14329 explicitly resolves Open Problem 4 (height), not Open Problem 18. Recent homogeneous-fragmentation/subordinator work on the beta-splitting family likewise studies height/asymptotic questions rather than announcing a new discrete-model answer to Open Problem 18.

The population-genetic machinery below is not claimed as new. Bobrowski--Wojdyla--Kimmel (J. Math. Biol. 2010) study a Moran model with mutation, drift, and recombination over multiple loci. Esser--Probst--Baake, arXiv:1502.05194 / J. Math. Biol. 2016, study a finite-locus Moran model with recombination and a partition-valued ancestral process. Related work emphasizes that genuinely shared pedigrees can leave residual dependence even between unlinked loci. Accordingly the potentially new claim here is only the **specific finite-pool shared-victim/free-recombination compiler and its full CTCS(infinity) hierarchy limit**, not Moran models, recombination, stationary beta-binomial laws, or partition-valued ancestry themselves.

The bounded search did not locate this specific C023 construction or a later paper claiming Open Problem 18. This is a bounded negative search, **not a novelty certificate**.

An exact repository search still recovers no current-package `P26-AUDIT-R11-I0054` end-to-end PASS and no second complete current-package OTHER-track PASS.

---

## 3. Move #9 — randomize the infinite-locus injection into a finite locus pool

C022 avoided all locus reuse by assigning every `(raw time, tree block)` a fresh locus from a countably infinite independent family. The natural question is whether one can replace that idealization by a genuinely finite genome without reintroducing order-one temporal correlations.

The first attack was to randomize locus assignment. If there are `L_N` loci and every visible tree query hashes independently and uniformly into that finite pool, then on a fixed `[k]` restriction and physical time interval `[0,T]`, the number of queried loci is at most

\[
M_{N,k,T}\le k\left(\left\lceil\frac{T}{\Delta_N}\right\rceil+1\right).
\tag{3.1}
\]

Therefore the birthday bound gives

\[
P(\text{a visible queried locus is reused by time }T)
\le \binom{M_{N,k,T}}2\frac1{L_N}
=O_{k,T}\!\left(\frac1{L_N\Delta_N^2}\right).
\tag{3.2}
\]

This immediately identifies the right finite-pool regime:

\[
\boxed{L_N\Delta_N^2\longrightarrow\infty.}
\tag{3.3}
\]

The key remaining issue is that distinct loci should remain independent even though they live in one persistent population and share demographic events. The next section supplies an exact mechanism.

---

## 4. C023 construction — finite loci, one persistent population, shared deaths, free-recombining parents

For each `N`, define

\[
m_N=\lceil N^{1/4}\rceil,\qquad
\alpha_N=\Delta_N=\frac1{m_N},\qquad
L_N=N,
\tag{4.1}
\]

and mutation probability

\[
\mu_N=\frac{\alpha_N}{N+2\alpha_N}.
\tag{4.2}
\]

There are `N` population sites and exactly `L_N=N` binary loci. At locus `\ell`, write the allele configuration as

\[
X_r^{(\ell)}\in\{0,1\}^N.
\]

Initially the loci are independent with common exchangeable law

\[
\nu_{N,\alpha}(x)
=
\frac{(\alpha)_{|x|}(\alpha)_{N-|x|}}{(2\alpha)_N},
\tag{4.3}
\]

for each specific binary configuration `x`. Consequently the count `S=|x|` has beta-binomial law

\[
\pi_{N,\alpha}(s)
=
\binom Ns\frac{(\alpha)_s(\alpha)_{N-s}}{(2\alpha)_N}.
\tag{4.4}
\]

### Tree query

For every pair `(raw generation r, current nonsingleton tree block B)`, sample an independent hash

\[
H_{r,B}\sim\mathrm{Unif}\{1,\ldots,L_N\}.
\tag{4.5}
\]

At locus `H_{r,B}`, inject the labels of `B` uniformly without replacement into the `N` population sites. If both alleles appear, split `B` by its two colors; if the sample is monochromatic, leave `B` unchanged. Different blocks use independent hashes, but collisions are allowed. One raw generation has physical duration `\Delta_N`.

### Persistent finite-locus population update

After all tree queries at raw generation `r`, choose one victim site

\[
V_r\sim\mathrm{Unif}[N]
\]

**shared by every locus**. At each locus independently choose a parent `P_{r,\ell}\sim\mathrm{Unif}[N]`, copy its allele, flip it with probability `\mu_N`, and replace the allele at the common victim `V_r`.

Thus the genome is finite and persistent. Loci share the same death/demographic event, while the parent copied at each locus is independent: this is a maximal-free-recombination Moran mechanism with a common victim schedule. The population is not restarted after a tree split.

---

## 5. Move #21 — exact fixed-victim reversibility is the decoupling mechanism

Finite-locus Moran/recombination models are known, so the issue is not to rename that literature but to identify what makes this particular hierarchy analyzable. The useful identity is stronger than ordinary stationary balance: **every fixed-victim kernel separately preserves the same locus law**.

Fix a victim site `v`. Suppose `x_v=0` and `x` has `s` ones. Under one locus update with victim `v`, the probability that `v` becomes `1` is

\[
p_+(s)
=\mu+(1-2\mu)\frac{s}{N}
=\frac{\alpha+s}{N+2\alpha}.
\tag{5.1}
\]

For `x+e_v`, whose total number of ones is `s+1`, the probability that `v` becomes `0` is

\[
p_-(s+1)
=\frac{\alpha+N-s-1}{N+2\alpha}.
\tag{5.2}
\]

Meanwhile

\[
\frac{\nu_{N,\alpha}(x+e_v)}{\nu_{N,\alpha}(x)}
=
\frac{\alpha+s}{\alpha+N-s-1}
=
\frac{p_+(s)}{p_-(s+1)}.
\tag{5.3}
\]

Hence the fixed-victim kernel `K_v` is reversible with respect to `\nu_{N,\alpha}` for **every** `v`.

This has a crucial consequence. Conditional on the entire common victim sequence

\[
(V_0,V_1,\ldots),
\]

the locus processes use independent parent/mutation randomness, and each deterministic composition of the kernels `K_{V_r}` preserves `\nu_{N,\alpha}`. Therefore at every collection of times,

\[
\boxed{\text{distinct locus processes remain independent, with each queried-time marginal exactly }\nu_{N,\alpha},\text{ conditional on the full victim history}.}
\tag{5.4}
\]

This is why the common death schedule creates real finite-population coupling without destroying the fresh-locus calculation.

A more biologically literal shared-parent/two-parent pedigree does **not** have this exact fixed-environment invariance: fixing the parents biases the one-locus kernel, so common pedigree randomness can induce cross-locus dependence. That is the next harder route, not something claimed solved here.

---

## 6. Exact fresh-locus split law

Fix a visible block of size `b=i+j` and a specified unordered support `A|A^c`, `|A|=i`. If the queried locus has `s` red sites, sampling without replacement gives

\[
r_{N,s}(i,j)
=
\frac{
(s)_{\underline i}(N-s)_{\underline j}
+(s)_{\underline j}(N-s)_{\underline i}
}{(N)_{\underline b}}.
\tag{6.1}
\]

Averaging under (4.4) gives the exact beta-binomial predictive identity

\[
\boxed{
p_{N,\alpha}(i,j)
=E_\pi r_{N,S}(i,j)
=\frac{2(\alpha)_i(\alpha)_j}{(2\alpha)_b}.
}
\tag{6.2}
\]

Since `\Delta_N=\alpha_N`, division by the CTCS rate gives

\[
\frac{p_{N,\alpha_N}(i,j)}{\Delta_N B(i,j)}
=
\frac{
\prod_{r=1}^{i-1}(1+\alpha_N/r)
\prod_{r=1}^{j-1}(1+\alpha_N/r)
}{
\prod_{r=1}^{b-1}(1+2\alpha_N/r)
}.
\tag{6.3}
\]

For every fixed `b`, this is `1+O_b(\alpha_N)`, hence

\[
\boxed{
p_{N,\alpha_N}(i,j)
=\Delta_N B(i,j)+O_b(\Delta_N^2).
}
\tag{6.4}
\]

Restriction consistency holds in law. Restricting a uniform injection of a hidden block to its visible labels is again a uniform injection. An invisible hidden split leaves exactly one carrier block for every visible block. Its later hash is a new independent uniform hash. Hidden queries never modify genome loci, so they cannot contaminate the visible locus pool.

---

## 7. Move #30 — three scales and the finite-pool compiler U007

The proof separates three scales that should not be conflated:

1. **CTCS tangent scale:** `\Delta_N=\alpha_N\to0`, yielding (6.4).
2. **Finite-pool birthday scale:** `L_N\Delta_N^2\to\infty`, making query reuse negligible on every fixed visible time window.
3. **Common-environment scale:** exact fixed-victim reversibility (5.3), which makes distinct loci conditionally iid stationary despite the shared death schedule.

This gives the following reusable statement.

### Theorem U007 (finite-pool fresh-source compiler)

Let a fixed-`k` discrete hierarchy make at most `C_k` source queries per raw step of duration `\Delta_N`. Suppose there are `L_N` source coordinates, each query selects a uniform coordinate independently, and conditional on a common environment history the source coordinates are independent with the same stationary query law. Suppose that, if every query were forced to use a fresh source coordinate, the one-step hierarchy kernel satisfies uniformly over its finite state space

\[
P_{N,\mathrm{fresh}}^{(k)}
=I+\Delta_NQ^{(k)}+O_k(\Delta_N^2).
\tag{7.1}
\]

If

\[
\Delta_N\to0,
\qquad
L_N\Delta_N^2\to\infty,
\tag{7.2}
\]

then the actual finite-pool hierarchy converges on every bounded physical-time interval to the continuous-time `Q^{(k)}` chain in Skorokhod `J_1`.

### Proof

Fix `T`. The number of source queries by time `T` is at most `C_{k,T}/\Delta_N`. By the union bound,

\[
P(\mathcal C_{N,k,T})
\le
\frac{C_{k,T}}{L_N\Delta_N^2},
\tag{7.3}
\]

where `\mathcal C` is the event that some queried source coordinate is reused. This tends to zero.

On `\mathcal C^c`, all coordinates actually consulted by the visible restriction are distinct. Conditional on the common environment history, their states at their respective query times are independent with the stationary query law. Thus, on this event, the complete visible hierarchy path can be coupled **exactly** to the fresh-source hierarchy through time `T`.

Now compare the fresh-source chain with the Euler chain having kernel `I+\Delta_NQ^{(k)}`. From (7.1), maximal coupling of each raw step fails with probability `O_k(\Delta_N^2)`. There are `O(T/\Delta_N)` steps, so total failure probability is `O_{k,T}(\Delta_N)\to0`. The Euler chain is a finite-state approximation to the continuous-time `Q^{(k)}` chain: its geometric holding times multiplied by `\Delta_N` converge jointly to the corresponding exponentials, and its jump probabilities converge to the normalized off-diagonal rates. Since the state space is finite, this yields `J_1` convergence. Combining the two couplings proves U007. `\square`

### Application to C023

For a `[k]` restriction there are at most `k` current visible blocks, so the query bound in U007 holds. By (6.4), a specified proper split has the required CTCS probability to first order; the probability that two different visible blocks split in one raw generation is `O_k(\Delta_N^2)`. Therefore

\[
\left\|P_{N,\mathrm{fresh}}^{(k)}
-\left(I+\Delta_NQ_{\rm CTCS}^{(k)}\right)\right\|_{\rm TV}
=O_k(\Delta_N^2).
\tag{7.4}
\]

Our choices satisfy

\[
L_N\Delta_N^2
=
\frac{N}{\lceil N^{1/4}\rceil^2}
\longrightarrow\infty.
\tag{7.5}
\]

Hence, for every fixed `k`,

\[
\boxed{
\widehat\Pi_N^{[k]}
\Longrightarrow
\Pi_{\rm CTCS}^{[k]}
\quad\text{in }J_1.
}
\tag{7.6}
\]

Finally use the projective finite-restriction metric. Given `\varepsilon>0`, choose `K` so the metric tail from restrictions above `K` is below `\varepsilon`; convergence of the first `K` restrictions follows from the preceding finite-dimensional construction and consistency. Thus

\[
\boxed{
\widehat\Pi_N
\Longrightarrow
\Pi_{\operatorname{CTCS}(\infty)}
}
\tag{7.7}
\]

for the complete exchangeable-partition genealogy.

This is the required whole-limit statement, not a weaker marginal.

---

## 8. Exact finite non-equivalence certificate

At `N=4`,

\[
m_4=2,\qquad
\alpha_4=\Delta_4=\frac12,
\qquad
L_4=4,
\qquad
\mu_4=\frac1{10}.
\]

The exact stationary count law is

\[
\left(
\frac{35}{128},\frac5{32},\frac9{64},\frac5{32},\frac{35}{128}
\right).
\tag{8.1}
\]

For a specified four-label root support,

\[
p_4(1,3)=\frac5{64},
\qquad
p_4(2,2)=\frac3{64},
\]

so the particular-support ratio is

\[
\boxed{R_{C023}=\frac53.}
\tag{8.2}
\]

The retained binary-class finite ratios are

\[
2,\quad
\frac75,\quad
\frac{2699}{1365},\quad
\frac{2273}{1153},\quad
\frac{61381}{43765},\quad
\frac{166094447739}{85563797248},\quad
\frac{33}{17},
\]

for the original finite CTCS model and C001, C009, C010, C020, C021, C022 respectively. `5/3` differs exactly from every one. The remaining retained classes are separated in the immutable R11 history by positive finite multifurcation witnesses, whereas a single C023 block split is binary. Root-support law is invariant under deterministic relabeling and global branch-length rescaling. Thus C023 is a genuinely distinct class under the frozen convention.

There is also a direct finite-pool reuse witness separating the mechanism from C022. For a two-label block at `N=4`, let

\[
g(s)=\frac{s(s-1)+(N-s)(N-s-1)}{N(N-1)}
\]

be the no-split probability given count `s`. Exactly,

\[
E g=\frac34,
\qquad
\operatorname{Var}(g)=\frac5{64}.
\]

The centered `g` is an eigenfunction of the one-locus Moran count kernel with

\[
\lambda_2
=1-\frac{4\alpha+2}{N(N+2\alpha)}
=\frac45.
\]

Two consecutive hashes hit the same locus with probability `1/L=1/4`. Therefore

\[
P(T>2)
=\left(\frac34\right)^2
+\frac14\frac45\frac5{64}
=\frac{37}{64},
\]

and

\[
\boxed{
\Xi_{C023}:=\frac{P(T>2)}{P(T>1)^2}=\frac{37}{36}>1.
}
\tag{8.3}
\]

C022, which never reuses a locus, has the corresponding fresh-source ratio exactly `1`. Equation (8.3) is not needed for the frozen-equivalence separation, but verifies that C023 has genuinely new finite-pool temporal structure rather than merely a renamed fresh-locus model.

Accordingly the stable author-side claims are

\[
\boxed{\texttt{R11-I0054-U007 = PROVED\_AUTHOR\_SIDE}}
\]

and

\[
\boxed{\texttt{R11-I0054-C023 = PROVED\_AUTHOR\_SIDE under frozen equivalence}},
\]

and the fixed metric moves

\[
\boxed{22\longrightarrow23}.
\]

---

## 9. Exact finite self-check

Only after the route and proof were written did I build the exact checker

`artifacts/R11/2026-09-17T14-40-48Z_c023_finite_locus_checker.py`

and execute it using `fractions.Fraction` arithmetic. Its archived output is

`artifacts/R11/2026-09-17T14-40-48Z_c023_finite_locus_checker.out`.

The checker performs **11,707 exact rational checks** covering fixed-victim detailed balance, beta-binomial normalization, the exact predictive split identity, the product/tangent formula, the finite-pool asymptotic scale, the full `N=4` stationary and root-support witness, exact separation from all retained binary classes, and the same-locus reuse eigenfunction calculation. It ends

`ALL_EXACT_CHECKS_PASS`.

Checker creation commit: `9a64ff249eaef433c3ad90c3c5b6b3df6b473d0d`.  
Output creation commit: `1f5fe6a9eb50f986522d5eb9ff05ede63c783429`.

These are self-checks, not independent audits.

---

## 10. Status and remaining obligations

I am **not** calling Aldous--Janson Open Problem 18 closed.

The source-level campaign status remains **PARTIAL** because:

1. `operations/claims/I0054.md` is still `PENDING_ADMISSION, not READY`;
2. no current-package `P26-AUDIT-R11-I0054` end-to-end PASS was recovered;
3. no second independent current-package OTHER-track end-to-end PASS was recovered;
4. the bounded literature search is not a novelty certificate;
5. independent reviewers still need to judge the source's deliberately informal “superficially different” criterion.

The research result of this run is nonetheless substantive: C023 removes C022's countably infinite fresh-locus idealization, replaces it by `N` persistent loci with actual reuse and a shared demographic death schedule, and proves that the finite source pool becomes invisible in the whole CTCS genealogy limit under the sharp birthday-scale sufficient condition `L_N\Delta_N^2\to\infty`.

The next harder target is a genuinely shared-parent/two-parent pedigree or finite recombination graph, where conditional product stationarity fails and residual linkage/pedigree correlations must be bounded rather than eliminated exactly.

Next nonrepeating Section-B methods recorded: **#6 (deform to a solvable point), #12 (find what is conserved), #24 (find the extremal object)**.

---

```yaml
ledger_delta:
  track: R11
  intake: I0054
  source: "Aldous--Janson, arXiv:2303.02529v3, Open Problem 18"
  target: "genuinely different discrete models with the full CTCS(infinity) exchangeable-partition genealogy limit"
  metric_name: "number of distinct nontrivial discrete model classes with complete author-side whole-limit proofs under frozen equivalence"
  before: 22
  after: 23
  movement: "+1"
  new_class: "C023 finite-locus shared-victim free-recombination Moran hierarchy"
  new_theorem: "U007 finite-pool fresh-source compiler"
  class_status: "PROVED_AUTHOR_SIDE"
  source_status: "PARTIAL_NOT_CLOSED"
  admission: "PENDING_ADMISSION_NOT_READY"
  exact_checker: "artifacts/R11/2026-09-17T14-40-48Z_c023_finite_locus_checker.py"
  exact_output: "artifacts/R11/2026-09-17T14-40-48Z_c023_finite_locus_checker.out"
  checker_result: "ALL_EXACT_CHECKS_PASS"
  audits_required: "P26 end-to-end + one distinct OTHER-track end-to-end"
  audits_recovered_current_package: 0
  next_methods: [6, 12, 24]
```
