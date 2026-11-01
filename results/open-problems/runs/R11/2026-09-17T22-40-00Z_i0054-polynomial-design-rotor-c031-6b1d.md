Model: GPT-5.6 Sol. Reasoning: UNVERIFIED runtime level; GPT-6 / maximum was requested, but no model-family or reasoning-effort selector is exposed, so GPT-6 / maximum is not verified or claimed. Metric movement: `30 -> 31` distinct nontrivial discrete model classes with complete author-side required-limit proofs under the frozen equivalence convention. Section-B moves actually tried: **#5 (add a parameter and differentiate/read its effect), #11 (dualize), #27 (swap the quantifiers)**.

Problem/source: David J. Aldous and Svante Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529v3, **Open Problem 18**, intake `I0054`. Overall campaign status remains **PARTIAL, not CLOSED**. This run proves a new discrete class `R11-I0054-C031`, a deterministic polynomial-size approximate-design rotor whose full finite restrictions converge to `CTCS(infinity)`.

Run ID: `2026-09-17T22-40-00Z_i0054-polynomial-design-rotor-c031-6b1d`  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Dated source/literature check: 2026-09-17 UTC / 2026-09-18 Jerusalem local date

No email/Gmail, Drive, public posting, purchase, permission change, workflow execution, scheduler change, shared-root edit, or peer-track edit was performed.

---

## 1. Continuity, source, ownership, and exact topology

I continued from the newest complete R11 report

`runs/R11/2026-09-17T21-40-00Z_i0054-seeded-permutation-rotor-c030-4c7e.md`

rather than restarting. That report moved the frozen metric `29 -> 30`, proved C030, and recorded #5/#11/#27 as the next nonrepeating method triple. Those are the methods used here.

Before research I read/recovered the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/claims/I0054.md`, `operations/NEW_METHODS_2026-09-16.md`, the newest R11 report, the newest neighboring Aldous--Janson clade report under P13/I0051, targeted intake hits for the exact I0054 row under `probability_1000_intake_I_20260914/problems.jsonl`, and repository-wide I0054/audit/ownership searches. The GitHub connector gives bounded file/search views rather than a credible byte-for-byte operation over every object in the repository, so I do not pretend to have manually reread every one of roughly 780 intake rows. The exact source/claim/current-target continuity surfaces were recovered.

The canonical reservation remains

- owner: `R11`;
- source: arXiv:2303.02529v3, Open Problem 18;
- status: `PENDING_ADMISSION, not READY`.

No competing I0054 owner was found. P13's former I0051/Open Problem 9 clade-count problem is a distinct source target and is not reassigned here. The old R11 planar self-avoiding-walk route remains retired with its immutable history.

I reread the current arXiv PDF. On printed page 58 (PDF page index 57), Open Problem 18 still asks:

> Are there superficially different discrete models whose limit is the same CTCS(infinity)?

The next sentence says that the key feature of the authors' model seems to be the subordinator approximation and asks whether this can arise in another discrete tree model. The abstract and Part III formalize the `CTCS(infinity)` object through consistent exchangeable partitions.

Accordingly the convergence notion used below is the source-relevant one: for every fixed `k` and finite `T`, convergence of the entire restriction path in `D([0,T], P_k)` with Skorokhod `J_1` topology, followed by convergence in the projective finite-restriction topology to the exchangeable-partition process `CTCS(infinity)`. A root law or tagged-lineage marginal is not substituted for this.

### Runtime/model-control status

The runtime identifies as GPT-5.6 Sol. Reasoning effort is not exposed and is therefore `UNVERIFIED`. The scheduler/control schema available in this environment exposes title/prompt, schedule, enablement and timing mode, but no model-family selector, reasoning-effort selector, authenticated runtime-model telemetry, or guaranteed hour-long execution. GPT-6/maximum is therefore prompt text only. The old P26 `You cannot modify this task` event was authorization-context dependent in the repository history; the valid remedy for a still-denied task is the authorized owner/workspace control surface or platform support, not cloning or bypassing the task. No scheduler modification was attempted in this run.

---

## 2. Current literature and prior-art screen

Fresh dated web searches used combinations of `Aldous Janson Open Problem 18 CTCS`, `same CTCS infinity discrete model`, `critical beta-splitting CTCS 2026`, `almost k-wise independent permutations`, `epsilon approximation set systems`, and `splitters derandomization`.

The current source remains arXiv:2303.02529v3. The recent Chorbadzhiyska--Minchev--Savov preprint arXiv:2608.18320 studies the beta-splitting family through homogeneous fragmentations/subordinators and resolves a height problem; Heng Ma's arXiv:2609.14329 explicitly answers Aldous--Janson Open Problem 4. I found no paper in the bounded search announcing a resolution of Open Problem 18. This is a bounded negative search, not a novelty certificate.

The derandomization ingredients are not new. Naor--Schulman--Srinivasan's splitter framework and the later almost-k-wise permutation literature, including Alon--Lovett, explicitly study small deterministic/pseudorandom families that reproduce low-order marginals. I make no novelty claim for Hoeffding sampling, epsilon-approximations, splitters, almost-k-wise independence, or the probabilistic method. The potentially new part is the particular harmonic subset-design rotor below and its full `CTCS(infinity)` path-limit argument.

A current repository search still recovers no current-package `P26-AUDIT-R11-I0054` end-to-end PASS and no second complete current-package OTHER-track PASS. Therefore the source cannot be called closed under the fleet protocol.

---

## 3. Move #5: add the design-depth and discrepancy parameters

C030 derandomized C029 by cycling through the entire symmetric group `S_N`; its exact orbit identity is powerful but costs a factorial rotor period. The first question here was whether exact orbit equality is actually needed.

Introduce two parameters:

\[
K_N:=\min\{N,\max(2,\lfloor\log_2N\rfloor)\},
\qquad
\varepsilon_N:=N^{-3}.
\tag{3.1}
\]

`K_N` is the largest cylinder size that the deterministic environment must reproduce, while `epsilon_N` is the allowed error. The crucial observation is that projective convergence only asks for every **fixed** `k`; therefore it suffices that

\[
K_N\to\infty,
\qquad
\varepsilon_N H_{N-1}\to0.
\tag{3.2}
\]

Exact `N`-wise uniformity at each finite `N` is unnecessary.

For phase `s in {1,...,N-1}`, let `U_{N,s}` denote the uniform law on the `s`-subsets of `[N]`. For disjoint `A,B subset [N]`, with `a=|A|`, `b=|B|`, its cylinder probability is

\[
U_{N,s}\{A\subset R,\ B\cap R=\varnothing\}
=
\frac{(s)_{\underline a}(N-s)_{\underline b}}
{(N)_{\underline{a+b}}}.
\tag{3.3}
\]

We seek a finite multiset `F_{N,s}` of `s`-subsets whose empirical law approximates every such cylinder with `a+b<=K_N` to additive error `epsilon_N`.

---

## 4. Move #27: one deterministic family works for all cylinders simultaneously

The quantifier swap is the main existence step. Instead of choosing a good sample separately for each cylinder, choose one family that is simultaneously good for **every** phase and every cylinder of order at most `K_N`.

Let

\[
C_N:=(2N)^{K_N+2}.
\tag{4.1}
\]

The number of all phase/cylinder constraints is

\[
D_N=(N-1)\sum_{r=1}^{K_N}\binom Nr2^r
\le C_N.
\tag{4.2}
\]

Define `L_N` to be

\[
L_N:=2+\left\lceil\log_2(2C_N)\right\rceil
\tag{4.3}
\]

and choose

\[
M_N:=N^6L_N+1.
\tag{4.4}
\]

For each phase `s`, sample `M_N` independent uniform `s`-subsets. For any fixed cylinder, Hoeffding gives

\[
P\{ |\widehat p-p|>\varepsilon_N\}
\le2\exp(-2M_N\varepsilon_N^2)
=2\exp(-2M_N/N^6).
\tag{4.5}
\]

Union bounding all constraints gives

\[
P\{\text{some cylinder fails}\}
\le2C_N\exp(-2M_N/N^6).
\tag{4.6}
\]

Because `M_N>N^6L_N`, `e>2`, and `2C_N<=2^{L_N-2}`,

\[
2C_N\exp(-2M_N/N^6)
<2C_N2^{-2L_N}
\le2^{-L_N-2}<1.
\tag{4.7}
\]

Thus a simultaneous good family exists.

This is converted into an entirely deterministic object: among all tuples of multisets

\[
(\mathcal F_{N,1},\ldots,\mathcal F_{N,N-1})
\]

of size `M_N` satisfying all cylinder inequalities, choose the lexicographically first one, and list each multiset itself in lexicographic order. The search is finite; (4.7) proves the admissible set is nonempty.

Since `K_N=O(log N)` and `L_N=O((log N)^2)`, one phase uses

\[
M_N=O(N^6(\log N)^2)
\tag{4.8}
\]

entries. The full deterministic rotor below has only

\[
(N-1)M_N=O(N^7(\log N)^2)
\tag{4.9}
\]

entries, polynomial rather than the `2(N-1)N!` entries of C030.

---

## 5. C031: deterministic polynomial-design rotor

For each `N>=3`, fix the lexicographically first good families from Section 4. The environment cycles deterministically through all pairs

\[
(s,R),\qquad
s=1,\ldots,N-1,
\quad R\in\mathcal F_{N,s},
\tag{5.1}
\]

in the fixed lexicographic order.

Let

\[
w_{N,s}=\frac{N}{2s(N-s)},
\qquad
c_{N,s}=(N-1)w_{N,s}
=\frac{N(N-1)}{2s(N-s)}.
\tag{5.2}
\]

Choose a complete-cycle duration

\[
\tau_N=N^{-2}
\tag{5.3}
\]

and raw mesh

\[
\delta_N=rac{\tau_N}{(N-1)M_N}.
\tag{5.4}
\]

At raw rotor entry `(s,R)`, every current nonsingleton tree block `C` independently activates with probability

\[
a_{N,s}=\delta_Nc_{N,s}.
\tag{5.5}
\]

If activated, color a label red iff it lies in `R`, blue otherwise, and split `C` into the two color classes if both are nonempty. Then advance to the next deterministic rotor entry.

The rule uses no random injection, no random seed permutation, no random population/locus environment and no stochastic phase process. Its only randomness is in the block-activation coins. Since `c_{N,s}<=N/2`, the activation probability is valid for all `N>=3`.

Restriction to a visible label set causes no hidden-state problem. A visible block has exactly one carrier block in the full hierarchy; hidden-only splits merely change that carrier. Both the activation probability and deterministic coloring of the visible labels depend only on `(s,R)` and on the visible labels themselves, not on the hidden content of the carrier. Thus every fixed finite restriction is governed by the same rotor rule.

---

## 6. Move #11: dual cylinder discrepancy controls the generator

Define the order-`K` cylinder discrepancy seminorm between probability measures on `s`-subsets by

\[
\|\nu-U_{N,s}\|_{\mathrm{cyl},K}
:=
\sup_{\substack{A\cap B=\varnothing\\|A|+|B|\le K}}
\left|
\nu\{A\subset R,\ B\cap R=\varnothing\}
-
U_{N,s}\{A\subset R,\ B\cap R=\varnothing\}
\right|.
\tag{6.1}
\]

This is the useful dual formulation: the split-generator entries are linear functionals of the environment law against two such cylinder indicators.

Fix a visible block `C` of size `i+j<=K_N` and one specified unordered support `A|C\A`, `|A|=i`. Let `\widehat h_{N,s}(i,j;A,C)` be the empirical fraction of `R in F_{N,s}` which colors exactly `A` red and its complement blue, or vice versa. The construction gives

\[
|\widehat h_{N,s}-h_{N,s}(i,j)|\le2\varepsilon_N,
\tag{6.2}
\]

where the exact hypergeometric probability is

\[
h_{N,s}(i,j)=
\frac{(s)_{\underline i}(N-s)_{\underline j}
+(s)_{\underline j}(N-s)_{\underline i}}
{(N)_{\underline{i+j}}}.
\tag{6.3}
\]

The cycle-averaged first-order C031 rate of that support is

\[
\widehat q_N(i,j;A,C)
=
\sum_{s=1}^{N-1}w_{N,s}\widehat h_{N,s}(i,j;A,C).
\tag{6.4}
\]

C029/C030's exact falling-factorial Vandermonde identity gives

\[
\sum_{s=1}^{N-1}w_{N,s}h_{N,s}(i,j)=B(i,j),
\tag{6.5}
\]

with `B(i,j)=(i-1)!(j-1)!/(i+j-1)!`, the specified CTCS split rate. Also

\[
\sum_{s=1}^{N-1}w_{N,s}=H_{N-1}.
\tag{6.6}
\]

Therefore

\[
\boxed{
|\widehat q_N(i,j;A,C)-B(i,j)|
\le2\varepsilon_NH_{N-1}
\le\frac{2}{N^2}.
}
\tag{6.7}
\]

The last inequality uses `H_{N-1}<=N` and `epsilon_N=N^{-3}`.

This yields a reusable compiler statement.

### U011 — cylinder-discrepancy rotor compiler

Suppose deterministic finite fixed-size subset schedules satisfy

\[
K_N\to\infty,
\qquad
\varepsilon_NH_{N-1}\to0,
\qquad
\tau_N\to0,
\tag{6.8}
\]

and each order-`K_N` cylinder discrepancy is at most `epsilon_N`. Then the corresponding harmonic rotor, with one complete environment cycle of physical duration `tau_N`, converges on every fixed finite restriction to CTCS in `J_1`, hence projectively to `CTCS(infinity)`.

C031 is the explicit deterministic choice

\[
K_N=\lfloor\log_2N\rfloor\ (\text{clipped below by }2),
\quad
\varepsilon_N=N^{-3},
\quad
\tau_N=N^{-2}.
\tag{6.9}
\]

---

## 7. Complete whole-path convergence proof

Fix `k` and `T`. For all sufficiently large `N`, `k<=K_N`. Let `Q^{(k)}` be the CTCS generator on the finite set `P_k`, and let `\widehat Q_N^{(k)}` be the cycle-averaged first-order generator of the C031 restriction.

There are at most `2^k` proper binary supports from any one visible block and finitely many blocks in a state. Equation (6.7) therefore gives, for a constant depending only on `k`,

\[
\boxed{
\|\widehat Q_N^{(k)}-Q^{(k)}\|_{\mathrm{row},1}
\le \frac{C_k}{N^2}.
}
\tag{7.1}
\]

In particular all C031 visible exit rates on `P_k` are bounded by a constant `R_k` independent of large `N`.

Consider one complete rotor cycle. Summing the nonnegative first-order visible hazards over the cycle gives at most `R_k\tau_N`. Conditional on a first visible jump, every possible post-jump visible state again has full-cycle hazard at most `R_k\tau_N`; hence the probability of two or more visible jumps in one cycle is `O_k(\tau_N^2)`. This also covers simultaneous activations of distinct visible blocks in one raw step.

Consequently the exact cycle-boundary kernel `C_N^{(k)}` satisfies

\[
C_N^{(k)}
=I+\tau_N\widehat Q_N^{(k)}+O_k(\tau_N^2)
\tag{7.2}
\]

uniformly over visible starting states. The CTCS semigroup has

\[
e^{\tau_NQ^{(k)}}
=I+\tau_NQ^{(k)}+O_k(\tau_N^2).
\tag{7.3}
\]

Combining (7.1)--(7.3), one C031 cycle can be maximally coupled to a CTCS(k) interval of length `tau_N` with failure probability

\[
O_k\!\left(\frac{\tau_N}{N^2}+\tau_N^2\right).
\tag{7.4}
\]

There are `O(T/tau_N)` cycles on `[0,T]`, so

\[
P\{\text{cycle-boundary disagreement by }T\}
=
O_{k,T}(N^{-2}+\tau_N)
=O_{k,T}(N^{-2}).
\tag{7.5}
\]

The probability that any cycle contains two or more visible jumps is `O_{k,T}(\tau_N)=O_{k,T}(N^{-2})`. On the complementary event, move a C031 intra-cycle jump to its cycle boundary; its time displacement is at most `tau_N=N^{-2}`. Hence a coupling exists with

\[
\Pr\!\left\{
 d_{J_1,[0,T]}(
 \Pi_N^{\mathrm{C031},[k]},
 \Pi_{\mathrm{CTCS}}^{[k]})
 >\tau_N
\right\}
=O_{k,T}(N^{-2}).
\tag{7.6}
\]

Therefore

\[
\boxed{
\Pi_N^{\mathrm{C031},[k]}
\Longrightarrow
\Pi_{\mathrm{CTCS}}^{[k]}
\quad\text{in }J_1
}
\tag{7.7}
\]

for every fixed `k`. The limiting finite restrictions are exactly the mutually consistent CTCS(k) restrictions, so in the standard summable projective metric built from the finite-restriction `J_1` metrics,

\[
\boxed{
\Pi_N^{\mathrm{C031}}
\Longrightarrow
\Pi_{\operatorname{CTCS}(\infty)}.
}
\tag{7.8}
\]

This is the complete required genealogy limit.

---

## 8. Finite non-equivalence under the frozen convention

The frozen equivalence convention identifies only deterministic leaf relabelings and global branch/time rescalings of an existing finite model.

C031 has a simple invariant separating it from the immediately preceding exact-rotor classes and, structurally, from the earlier random-environment classes. By construction

\[
M_N=N^6L_N+1\equiv1\pmod N.
\tag{8.1}
\]

At phase `s=1`, every rotor entry is a singleton subset. If the phase-1 singleton occupation counts were label-uniform, every label would occur exactly `M_N/N` times, impossible because `N` does not divide `M_N`. Thus the finite environment is not label-exchangeable.

More sharply, goodness for the cylinder `{1} subset R` implies

\[
\frac{\#\{R\in\mathcal F_{N,1}:1\in R\}}{M_N}
\ge\frac1N-\frac1{N^3}>0.
\tag{8.2}
\]

Since the phase-1 multiset is listed lexicographically, its first entry is therefore `{1}`. At the **first raw step**, conditional on a root activation, the C031 split support is deterministically

\[
\{1\}\mid\{2,\ldots,N\}.
\tag{8.3}
\]

C030's corresponding first-step support is uniform over the `N` singleton supports because of its uniform seed; C029 uses a fresh uniform injection; C028 uses iid Bernoulli paintbox colors. No deterministic leaf relabeling converts a point mass on one singleton support into those positive-entropy laws, and global time rescaling does not alter conditional split support. The primitive C031 environment also has polynomial cycle size `O(N^7 log^2 N)`, versus C030's factorial symmetric-group rotor. Under the frozen convention this is a genuinely different finite model class rather than a relabeling or rescaling of C030 or the original CTCS construction.

The earlier R11 classes C001--C027 already have their own immutable finite witnesses separating them from the rotor classes; C031 introduces a new deterministic approximate-design mechanism rather than reusing any of those transition kernels.

Accordingly

\[
\boxed{
\texttt{R11-I0054-C031 = PROVED\_AUTHOR\_SIDE under frozen equivalence.}
}
\tag{8.4}
\]

and the fixed metric moves

\[
\boxed{30\to31.}
\tag{8.5}
\]

---

## 9. Exact self-check

I wrote and executed the substantive exact checker

`artifacts/R11/2026-09-17T22-40-00Z_c031_polynomial_design_check.py`

creation commit `adc820adb26983161f20138ec506df1208f0b50c`.

Its archived output is

`artifacts/R11/2026-09-17T22-40-00Z_c031_polynomial_design_check.out`

creation commit `d130db83034d2b5a3d280dbd44e0fc22a78ee594`.

The checker performs **917 exact integer/rational checks**. It verifies on `3<=N<=40`:

- the exact number of phase/cylinder constraints is below the analytic `C_N` envelope;
- the dyadic form of the Hoeffding-union existence inequality;
- `M_N == 1 (mod N)` and `gcd(M_N,N)=1`;
- positivity forcing every good phase-1 family to use each singleton label;
- `sum_s w_{N,s}=H_{N-1}` exactly;
- the exact envelope `2 epsilon_N H_{N-1} <= 2/N^2`;
- the finite hypergeometric/Vandermonde beta-kernel identity for a grid of `N,i,j` values.

The output ends `ALL_EXACT_CHECKS_PASS`. The locally executed stdout SHA-256 is

`219ef25cadc5a1a9a1f5d75c56dbbccb7f731abd90e0458f0b8d6db7fe1c8b9c`.

This is a **self-check**, not an independent audit.

---

## 10. Closure status and remaining obligations

I am **not** calling Aldous--Janson Open Problem 18 closed.

The mathematical author-side claim C031 has a complete convergence proof above, but fleet closure still requires:

1. the source-matching full argument and exact finite certificate — present author-side here/history;
2. a current prior-art search — bounded negative search recorded, but publication novelty remains unverified;
3. one independent end-to-end audit from P26 — **not recovered**;
4. a second independent end-to-end audit from a different track — **not recovered**;
5. independent judgment that C031/C030-style derandomizations satisfy the source's deliberately informal phrase “superficially different.”

The canonical `operations/claims/I0054.md` status therefore remains `PENDING_ADMISSION, not READY`, and the source-level campaign status remains **PARTIAL**.

---

## 11. What the three methods actually accomplished

- **#5, add a parameter:** replacing “exact all-orders orbit uniformity” by the pair `(K_N, epsilon_N)` exposed the true projective requirement `K_N -> infinity` and `epsilon_N H_N -> 0`. This cut the rotor from factorial size to polynomial size.
- **#11, dualize:** cylinder discrepancy is the dual norm naturally seen by the split generator. The CTCS rate error becomes the one-line estimate `2 epsilon_N H_{N-1}`.
- **#27, swap the quantifiers:** Hoeffding plus one union bound produces a **single** deterministic family simultaneously good for every phase and every order-`K_N` cylinder. Choosing the lexicographically first good family removes the probabilistic seed entirely.

This is real movement rather than another checker-only run.

---

## 12. Next nonrepeating route

The next methods recorded are **#10, #21, #30**.

The strongest next target is to replace the nonconstructive “lexicographically first good family” by an **explicit efficiently computable** small sample space, using splitter / almost-k-wise permutation technology or an explicit fixed-size analogue. A successful route should retain `K_N -> infinity`, polynomial rotor size, and the complete `J_1` projective proof while giving a closed-form or polynomial-time environment generator. If explicit fixed-size designs force a loss, localize exactly which cylinder orders/scales fail and determine the weakest explicit pseudorandomness sufficient for CTCS.

```yaml
ledger_delta:
  track: R11
  source: "Aldous--Janson, arXiv:2303.02529v3, Open Problem 18"
  intake: I0054
  target: "genuinely different discrete models with the full CTCS(infinity) exchangeable-partition limit"
  metric_name: "number of distinct nontrivial discrete model classes with complete author-side required-limit proofs under frozen equivalence"
  before: 30
  after: 31
  movement: true
  status: PARTIAL
  methods_used: [5, 11, 27]
  new_claims:
    - "R11-I0054-U011 = PROVED_AUTHOR_SIDE (cylinder-discrepancy rotor compiler)"
    - "R11-I0054-C031 = PROVED_AUTHOR_SIDE under frozen equivalence"
  claim_registry_status: "PENDING_ADMISSION, not READY"
  closure:
    p26_complete: false
    second_other_complete: false
    source_closed: false
  ownership:
    claim_file: operations/claims/I0054.md
    owner: R11
    collision_found: false
  artifacts:
    checker: artifacts/R11/2026-09-17T22-40-00Z_c031_polynomial_design_check.py
    checker_commit: adc820adb26983161f20138ec506df1208f0b50c
    output: artifacts/R11/2026-09-17T22-40-00Z_c031_polynomial_design_check.out
    output_commit: d130db83034d2b5a3d280dbd44e0fc22a78ee594
    output_sha256: 219ef25cadc5a1a9a1f5d75c56dbbccb7f731abd90e0458f0b8d6db7fe1c8b9c
  next_methods: [10, 21, 30]
  next_obligation: "explicit constructive polynomial-size fixed-weight pseudorandom rotor, or a proved obstruction identifying the necessary cylinder pseudorandomness"
```
