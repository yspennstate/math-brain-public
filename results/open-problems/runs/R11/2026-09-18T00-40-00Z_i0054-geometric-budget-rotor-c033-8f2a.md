Model: GPT-5.6 Sol. Reasoning: UNVERIFIED runtime level; GPT-6 / maximum was requested, but no model-family or reasoning-effort selector is exposed, so GPT-6 / maximum is not verified or claimed. Metric movement: `32 -> 33` distinct nontrivial discrete model classes with complete author-side required-limit proofs under the frozen equivalence convention. Section-B moves actually tried: **#3 (prove something stronger), #7 (take the limit), #22 (read the failures)**.

# R11 / I0054 — C033 geometric-budget rotor

Problem/source: David J. Aldous and Svante Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529v3, **Open Problem 18**. The source asks whether superficially different discrete models can have the same `CTCS(infinity)` limit. Overall campaign status remains **PARTIAL, not CLOSED**. This run proves a new discrete class `R11-I0054-C033`: a finite-field rotor whose color environment is deterministic and whose dynamic randomness is compressed to one integer-valued geometric budget per eventual internal tree node.

Run ID: `2026-09-18T00-40-00Z_i0054-geometric-budget-rotor-c033-8f2a`  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Dated source/literature check: 2026-09-18 UTC/local campaign date

No email/Gmail, Drive, public posting, purchase, permission change, workflow execution, scheduler change, shared-root edit, or peer-track edit was performed.

---

## 1. Continuity, ownership, source, and topology

I continued from the newest complete R11 report

`runs/R11/2026-09-17T23-47-12Z_i0054-polynomial-character-rotor-c032-5a7e.md`,

rather than restarting. That report moved the frozen metric `31 -> 32`, proved C032, and recorded the nonrepeating triple `#3/#7/#22`; those are the three methods actually used here.

Before new research I recovered the current campaign controls from:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- canonical reservation `operations/claims/I0054.md`;
- the newest R11 report and the current neighboring Aldous--Janson/P13 history;
- targeted intake/history searches for I0054 and repository-wide ownership/audit searches.

The canonical I0054 reservation still says `Owner: R11` and `Status: PENDING_ADMISSION, not READY`. No competing current I0054 owner was recovered. The former P13/I0051 clade-covariance problem is a different Aldous--Janson question; repository restoration history now records that P13's old I0051 target was retired/replaced, and it is not reassigned here. R11's old self-avoiding-walk route remains retired with its immutable history.

The GitHub connector gives bounded search/fetch access rather than a credible byte-for-byte traversal of every one of the roughly 780 intake rows. I therefore do **not** claim an invisible exhaustive reread of every JSONL object. The exact I0054 source/claim, prior R11 attempts, neighboring ownership, current exclusions, and audit surfaces were recovered.

I reread the current primary source PDF itself. The arXiv record is still v3, dated 17 April 2025 / revised 18 April 2025. Printed page 58, Section 6.3, says:

> **Open Problem 18.** Are there superficially different discrete models whose limit is the same CTCS(infinity)?

The next sentence says that the key feature of the authors' model seems to be their subordinator approximation and asks whether this can arise in another discrete tree model. The abstract and Section 5 describe `CTCS(infinity)` through compatible finite restrictions / exchangeable partitions.

The source does not itself prescribe a Skorokhod metric. R11's frozen source-facing criterion remains the stronger precise one used in C001--C032: for every fixed `k` and finite `T`, prove convergence of the **whole restriction path** in `D([0,T],P_k)` with Skorokhod `J_1`, then use exact restriction consistency to obtain projective convergence to the exchangeable-partition process `CTCS(infinity)`. A root split marginal, tagged fragment, or finite-time distribution is not enough.

### Runtime/model-control status

The runtime identifies as GPT-5.6 Sol; reasoning effort is not exposed and is therefore `UNVERIFIED`. The automation schema available here exposes prompt/title, schedule, enablement and timing mode, but no model-family or reasoning-effort selector and no authenticated runtime-model telemetry. Thus GPT-6/maximum remains a prompt request, not an enforceable or verified setting. The repository also records that the old P26 `You cannot modify this task` response was authorization-context dependent and that a later authorized context did modify P26. For any still-denied task, the valid route is the authorized owning workspace/control surface or platform support, not cloning or bypassing the task. The current owner instruction forbids scheduler changes in this research run, so none was attempted.

---

## 2. Dated current-literature / prior-art screen

Fresh searches used combinations of `Aldous Janson CTCS infinity Open Problem 18`, `same CTCS infinity discrete model`, `critical beta-splitting 2026`, and deterministic/rotor-router analogues of random walks.

The current source remains arXiv:2303.02529v3. Recent relevant papers include:

- Chorbadzhiyska--Minchev--Savov, arXiv:2608.18320 (18 August 2026), on beta-splitting trees via homogeneous fragmentations/subordinators; its abstract says that at the critical parameter it resolves a **height** open problem of Aldous--Janson;
- Heng Ma, arXiv:2609.14329 (13 September 2026), which explicitly answers Aldous--Janson **Open Problem 4** on discrete-time tree height;
- Heng Ma, arXiv:2609.14325 (13 September 2026), on extremal separation and clade-count dynamics;
- Aldous--Janson Part III, arXiv:2412.09655, on the exchangeable-partition representation and fringe tree.

I found no announced resolution of exact Open Problem 18 in this bounded dated search. This is **not a novelty certificate**.

Move #22 also looked at the known rotor-router / Propp-machine literature. Rotor-router systems are classical deterministic analogues of random walks and can approximate occupation counts or expectations very well. That prior art is relevant to the deterministic-environment part of C028--C032, and I make no novelty claim for rotor-router derandomization itself. The issue in this run is different: a completely deterministic labeled tree law is a point mass, so it cannot converge in law to a nondegenerate `CTCS(k)` distribution without introducing randomness somewhere (or randomizing the observation/initial seed, which is still randomness). This failure is what led to the geometric-budget construction below.

A fresh exact repository search still recovers no current-package `P26-AUDIT-R11-I0054` end-to-end PASS and no second complete current-package OTHER-track PASS. Older scoped checks of earlier C00x/U00x components are not promoted to audits of the present package.

---

## 3. Move #22 first: why the fully deterministic clock route fails

C032 already has an explicit deterministic color environment. Its only repeated randomness consists of independent Bernoulli activation coins at every raw rotor entry. The tempting next step is to replace those coins by a deterministic periodic activation schedule.

There are two obstructions.

### 3.1 A fully deterministic labeled model has a Dirac law

If the input labels, rotor, and activation schedule are all deterministic, then for every fixed `N` the entire labeled tree is deterministic. Any restriction to `[k]` therefore has a Dirac distribution. A weak limit of such a fixed deterministic path sequence can only be a Dirac limit along convergent subsequences. But `CTCS(k)` is nondegenerate already for `k=3` and has genuine exponential holding times. Thus **literal total derandomization cannot give the requested distributional limit**.

This is not contradicted by rotor-router theory: those models derandomize random-walk *averages/counts* while comparing deterministic trajectories with random expectations. They do not turn a deterministic labeled object into a nondegenerate law without a random initial condition or random observation.

### 3.2 A periodic clock does not have memorylessness

A deterministic periodic threshold also leaves a phase/residual-life variable. After conditioning on survival, the residual phase is not distributed as it was at birth. Hidden splits can then change the law seen by a finite restriction, and the clean restriction consistency used throughout R11 is lost.

So the missing property is not another small discrepancy estimate. It is **memorylessness under deleting invisible work**.

That observation is the entry point for C033.

---

## 4. C033: the geometric-budget finite-field rotor

Retain the deterministic C032 color rotor exactly.

For each `N>=3`, let

\[
p=p_N:=\min\{q\ge N:q\text{ prime}\},
\qquad
 d=d_p:=\min\{p-1,\max(2,\lfloor\log_2p\rfloor)\}.
\]

Embed the labels `[N]` as distinct elements of `F_p`. For `a,t in F_p`, set

\[
Y_t(a)=\sum_{r=0}^{d-1} a^r t^{r+1}\pmod p,
\]

and for `1<=s<=p-1` define the deterministic red set

\[
R_{s,t}=\{a\in[N]:Y_t(a)\in\{0,1,\ldots,s-1\}\}.
\]

The rotor cycles through all `(s,t)` lexicographically. Put

\[
w_{p,s}:=\frac{p}{2s(p-s)},
\qquad
c_{p,s}:=(p-1)w_{p,s},
\]

and choose

\[
\tau_N=p^{-2},
\qquad
\delta_N=\frac{\tau_N}{p(p-1)}.
\]

C032 gave a current block an independent Bernoulli activation at every entry, with probability

\[
h_{p,s}:=\delta_Nc_{p,s}.
\tag{4.1}
\]

C033 eliminates that stream of coins.

Define the finite integer

\[
D_p:=\operatorname{lcm}_{1\le s\le p-1}\bigl(2s(p-s)\bigr),
\]

and

\[
\rho_N:=\frac{\delta_N}{D_p},
\qquad
M_{p,s}:=D_pc_{p,s}
=\frac{D_pp(p-1)}{2s(p-s)}\in\mathbb N.
\tag{4.2}
\]

The identity

\[
M_{p,s}\rho_N=h_{p,s}
\tag{4.3}
\]

is exact.

### One random budget per block

When a nonsingleton block `B` is born, draw exactly one independent integer

\[
G_B\sim\operatorname{Geom}(\rho_N),
\qquad
P(G_B=m)=\rho_N(1-\rho_N)^{m-1},\quad m=1,2,\ldots.
\tag{4.4}
\]

At a rotor entry `(s,t)`:

1. if the deterministic coloring `R_{s,t}` is monochromatic on `B`, do nothing and do not alter the budget;
2. if it is nonmonochromatic and the remaining budget exceeds `M_{p,s}`, subtract `M_{p,s}` and leave `B` unsplit;
3. if it is nonmonochromatic and the remaining budget is at most `M_{p,s}`, split `B` into its red and blue children; each nonsingleton child receives one fresh independent geometric budget.

Children born during an entry are first processed at the following raw entry, as in the earlier rotor classes.

A full binary tree on `N` leaves has exactly `N-1` internal nodes. Consequently **the entire C033 tree uses exactly `N-1` independent geometric random variables**, one for each eventual internal block, instead of an unbounded stream of raw-step activation coins. All colors and all rotor phases are deterministic.

### Almost sure completion

The pair-separation lemma from C032 remains deterministic. For distinct labels `a!=b`,

\[
Y_t(a)-Y_t(b)
\]

is a nonzero polynomial in `t`: its `t^2` coefficient is `a-b`, and its degree is `<p`. Hence for some `t` the two score values differ, and some threshold `s` separates them. Every nonsingleton block therefore has at least one nonmonochromatic rotor entry in every cycle.

A geometric budget is finite almost surely, and each complete cycle removes a positive integer amount of budget from every still-unsplit nonsingleton block. Thus every block eventually splits almost surely. Recursing through finitely many descendants produces a full binary hierarchy almost surely.

---

## 5. U012: exact geometric-budget restriction/lumping compiler

This is the main theorem of the run.

### Theorem U012

Consider any deterministic sequence of colorings of a finite labeled set, with a positive integer quota `M_e` attached to each environment entry `e`. Give every newly born nonsingleton block an independent `Geom(rho)` budget. A block spends quota `M_e` only when entry `e` colors that block nonmonochromatically, and splits when its residual budget is at most the quota.

Then for every fixed visible label set `S`, after integrating out hidden labels and hidden-only splits, the restricted partition process is **exactly equal in law** to the following visible process:

- at entry `e`, every current visible nonsingleton block that is nonmonochromatically colored splits independently with probability

\[
a_e'=1-(1-\rho)^{M_e};
\tag{5.1}
\]

- monochromatic visible blocks do not split.

In particular, the restricted law depends only on the deterministic colors of visible labels and not on the hidden carrier history.

### Proof

The discrete geometric distribution satisfies the exact memoryless identity

\[
P(G>m+n\mid G>m)=P(G>n),
\qquad m,n\ge0.
\tag{5.2}
\]

Induct on raw rotor entries and maintain the invariant:

> conditional on the visible history, every current visible block has a unique full carrier whose residual budget is `Geom(rho)`, and these residual budgets are independent across distinct visible carriers.

It holds at birth.

Fix a visible block `B` and its full carrier `C` at one entry with quota `M`.

**Case 1: the visible coloring of `B` is nonmonochromatic.** Then the full coloring of `C` is also nonmonochromatic. The visible block splits iff the carrier budget `G<=M`, which has probability

\[
P(G\le M)=1-(1-\rho)^M.
\]

Conditional on `G>M`, the residual `G-M` is a fresh `Geom(rho)` by (5.2). If a split occurs, the visible children lie in distinct full children, which by construction receive fresh independent geometric budgets.

**Case 2: the visible coloring of `B` is monochromatic.** If the full carrier is also monochromatic, nothing happens and its budget remains geometric. If hidden labels make the full carrier nonmonochromatic, either `G>M`, in which case `G-M` is again a fresh geometric residual, or `G<=M`, in which case the full carrier splits **invisibly** to `B`: all visible labels of `B` enter the same child, and that child receives a fresh geometric budget. In every subcase the visible state is unchanged and its new carrier again has a fresh `Geom(rho)` residual.

Because full carrier blocks have independent budgets, independence across visible blocks is preserved. This completes the induction and proves (5.1) exactly. `QED`.

### Why this matters here

Applying U012 to C033 gives the exact effective visible activation probability

\[
a'_{p,s}=1-(1-\rho_N)^{M_{p,s}}.
\tag{5.3}
\]

Thus hidden splits do not create an uncontrolled clock bias. This is precisely what a deterministic periodic budget lacked.

---

## 6. C033 differs from C032 by only second order per rotor cycle

Let

\[
h_{p,s}=M_{p,s}\rho_N=\delta_Nc_{p,s}
\]

be C032's linear activation probability. By the elementary Bonferroni bounds,

\[
0\le h_{p,s}-a'_{p,s}
= M\rho-\bigl[1-(1-\rho)^M\bigr]
\le {M\choose2}\rho^2
\le \frac{h_{p,s}^2}{2}.
\tag{6.1}
\]

Since `c_{p,s}<=p/2`,

\[
h_{p,s}\le h_{\max}
=\frac{\tau_N}{2(p-1)}.
\tag{6.2}
\]

There are `p(p-1)` rotor entries per cycle, so even the crude all-entry bound gives

\[
\sum_{s,t}|a'_{p,s}-h_{p,s}|
\le
\frac{p(p-1)}2h_{\max}^2
=
\tau_N^2\frac{p}{8(p-1)}
=O(\tau_N^2).
\tag{6.3}
\]

Therefore replacing all C032 linear activation coins by the C033 geometric-budget effective probabilities perturbs one complete cycle only at second order.

---

## 7. Complete finite-restriction generator and `J_1` convergence proof

Fix a visible restriction `[k]`. Let `P_k` be its finite partition state space.

For an entry `e=(s,t)`, let `A_e^{(k)}` be the bounded first-order split operator determined by the deterministic C032/C033 coloring on `[k]`. U012 makes the C033 restriction a finite-state time-inhomogeneous Markov chain with independent block decisions and entry split probability `a'_{p,s}`.

The sum of visible first-order hazards over one full rotor cycle is `O_k(tau_N)`. One way to see this is to dominate `a'_{p,s}<=h_{p,s}` and use the C032 cycle calculation: for every fixed block size `b<=k`, the `h`-weighted nonmonochromatic rates converge to the finite CTCS exit rate `H_{b-1}`. Hence the total first-order mass across the finitely many current blocks is uniformly bounded by `C_k tau_N`.

It follows by expanding the product of the entry kernels that the probability of two or more visible split events inside one cycle is

\[
O_k(\tau_N^2).
\tag{7.1}
\]

Consequently the exact C033 one-cycle kernel satisfies

\[
C_{N,033}^{(k)}
=I+\sum_e a'_e A_e^{(k)}+O_k(\tau_N^2).
\tag{7.2}
\]

By (6.3), replacing `a'_e` by `h_e` costs only `O_k(tau_N^2)` in row total variation. Therefore

\[
C_{N,033}^{(k)}
= I+\tau_N Q_N^{(k)}+O_k(\tau_N^2),
\tag{7.3}
\]

where `Q_N^{(k)}` is exactly the C032 cycle-averaged first-order generator.

The C032 proof already established, from the finite-field character estimate and harmonic averaging, that for each fixed `k`

\[
Q_N^{(k)}\longrightarrow Q_{\rm CTCS}^{(k)}
\tag{7.4}
\]

entrywise (equivalently in any finite-dimensional operator norm). In particular, for a specified unordered `i|j` support the limiting rate is

\[
B(i,j)=\int_0^1x^{i-1}(1-x)^{j-1}\,dx.
\tag{7.5}
\]

Combining (7.3)--(7.4),

\[
C_{N,033}^{(k)}
=I+\tau_NQ_{\rm CTCS}^{(k)}+o_k(\tau_N).
\tag{7.6}
\]

Since `tau_N=p_N^{-2}->0`, the cycle-boundary chain is the usual finite-state Euler approximation to the CTCS restriction. Over `O(T/tau_N)` cycles, maximal coupling gives convergence of jump destinations and holding times on every bounded interval.

Moreover, by (7.1),

\[
P(\text{some cycle in }[0,T]\text{ has two or more visible jumps})
=O_{k,T}(\tau_N)\to0.
\tag{7.7}
\]

On the complementary event, moving each intra-cycle jump to its cycle boundary changes every jump time by at most `tau_N`. Hence

\[
\boxed{
\Pi_{N,033}^{[k]}
\Longrightarrow
\Pi_{\rm CTCS}^{[k]}
\quad\text{in Skorokhod }J_1
}
\tag{7.8}
\]

for every fixed `k` and finite time horizon.

U012 also gives exact finite-restriction consistency in law. The compatible family (7.8) therefore yields

\[
\boxed{
\Pi_{N,033}
\Longrightarrow
\Pi_{\operatorname{CTCS}(\infty)}
}
\tag{7.9}
\]

in the projective finite-restriction topology.

This is the complete partition-valued genealogy limit required by R11's frozen interpretation of the source problem.

---

## 8. Move #7: the geometric budget has the correct exponential continuum clock

There is a second, conceptual way to see why C033 is natural. If

\[
G_\rho\sim\operatorname{Geom}(\rho),
\]

then for every `x>=0`,

\[
P(\rho G_\rho>x)
=(1-\rho)^{\lfloor x/\rho\rfloor}
\longrightarrow e^{-x}.
\tag{8.1}
\]

Thus

\[
\rho G_\rho\Longrightarrow\operatorname{Exp}(1).
\tag{8.2}
\]

C033 can be viewed as giving each block one discrete memoryless amount of latent work. The deterministic rotor consumes that work only at nonmonochromatic opportunities. After rescaling, the one integer budget becomes the exponential memoryless clock needed by CTCS. Equation (7.3) makes this heuristic rigorous at the full finite-restriction path level.

---

## 9. Move #3: a stronger randomness-compression statement

C033 proves more than the existence of one further finite model.

For a full `N`-leaf hierarchy, C032 potentially consults an unbounded sequence of independent Bernoulli activation coins before the tree finishes. C033 has the same CTCS(infinity) limit while using exactly

\[
\boxed{N-1}
\]

independent integer-valued random variables for the entire tree. Everything else--the prime field, score functions, color sets, phase order, quotas, and budget consumption--is deterministic.

So the new reusable statement is:

\[
\boxed{
\texttt{R11-I0054-U012 = PROVED\_AUTHOR\_SIDE: geometric-budget restriction/lumping compiler.}
}
\]

It converts an entrywise rare-activation fragmentation with rational probabilities into a one-budget-per-block model, preserving each visible restricted law up to an explicit second-order activation transform and, under a vanishing-cycle hypothesis, preserving the full CTCS limit.

---

## 10. Exact finite non-equivalence certificate

The new class is not merely C032 under a label permutation or global time rescaling.

### 10.1 Direct N=3 difference from C032

At `N=3`,

\[
p=3,\quad d=2,\quad \tau=\frac19,\quad
\delta=\frac1{54},\quad D_3=4,\quad \rho=\frac1{216}.
\]

At a phase with `s=1`, the quota is `M=6`. C032's linear activation probability is

\[
h=\frac1{36}.
\]

C033's exact geometric-budget activation probability is

\[
a'=1-\left(\frac{215}{216}\right)^6
=
\frac{2788659027791}{101559956668416}.
\]

The exact strict gap is

\[
\boxed{
\frac1{36}-a'
=
\frac{32450879665}{101559956668416}>0.
}
\tag{10.1}
\]

This already proves a finite-law difference from C032.

### 10.2 Time-rescaling-invariant root-shape witness

For stronger comparison with all retained binary classes, the checker exactly enumerates the first root split of four visible labels in the `N=5` model. Its exact rational ratio

\[
R_{033}
=
\frac{P(\text{one specified }1|3\text{ root support})}
       {P(\text{one specified }2|2\text{ root support})}
\]

has a 1959-digit numerator and denominator; the complete exact fraction is formed internally by the checker and its canonical `numerator/denominator` string has SHA-256

`ac2d6da7805264ee858c8b2b5a7f758a093953dd233294db414e809ca4ecaaf2`.

Exact rational comparison gives

\[
\boxed{
\frac{11}{5}<R_{033}<R_{032}
}
\tag{10.2}
\]

with

\[
R_{033}=2.223070558035084\ldots,
\qquad
R_{032}
=\frac{7703418956282489179517201}
{3464343821016000000000000}
=2.223630030469459\ldots .
\]

Every retained exact binary root-ratio witness through C029 is `<11/5`; C030 has the previously certified bracket `2<R_C030<459/224<11/5`. C031 is separated directly by its first-entry behavior: conditional on activation, its first rotor entry gives a nontrivial singleton split, whereas the `(s,t)=(1,0)` entry of C033 is monochromatic and cannot split the root. C032 is separated by (10.2). The remaining retained classes are already separated in the immutable R11 history by finite multifurcation witnesses.

The ratio (10.2) is a tree-shape statistic, so deterministic label relabeling and global branch/time rescaling cannot remove the distinction.

Therefore

\[
\boxed{
\texttt{R11-I0054-C033 = PROVED\_AUTHOR\_SIDE under frozen equivalence.}
}
\]

---

## 11. Exact self-check

A new exact-arithmetic self-check was written **after** the route had produced U012/C033 and was then executed. It performs 3,243 checks covering:

- integer quota integrality `M_{p,s}`;
- the exact identity `M_{p,s}rho_N=delta_N c_{p,s}`;
- exact Bonferroni inequalities for `1-(1-rho)^M`;
- the closed all-entry error envelope
  `tau_N^2 p/[8(p-1)]`;
- exact discrete-geometric memorylessness for many rational `rho,m,n`;
- deterministic pair separation in the polynomial color rotor;
- the `N=3` finite activation witness (10.1);
- exact `N=5` root-support enumeration and the strict rational bracket (10.2);
- exact comparison with all archived binary root witnesses through C029 and the archived C030/C032 brackets.

Artifacts:

- `artifacts/R11/2026-09-18T00-40-00Z_c033_geometric_budget_rotor_checker.py`
- `artifacts/R11/2026-09-18T00-40-00Z_c033_geometric_budget_rotor_checker.out`

The archived output ends

`ALL_EXACT_CHECKS_PASS`.

Recorded hashes:

- checker SHA-256: `569de454048699e353dc6fdbdd4cf0f185fd07f97696232c6f42cb9d572c69f2`;
- clean stdout SHA-256: `787c4b69860564584f823343b596de2a93c6ed0a2e8a1c588392823dba36f539`.

The checker source was created/read back at commit `5432cd4d43b3f7627660888ea517d90bff035b5e`; the archived output was created/read back at `4aca55a88a1027deef1bf3a546aa5ccb6bf0d6fb`.

This is a **self-check**, not either of the two required independent closure audits.

---

## 12. Status and closure discipline

The fixed metric genuinely moves

\[
\boxed{32\longrightarrow33}.
\]

The source-level campaign status nevertheless remains **PARTIAL**. Reasons:

1. canonical `operations/claims/I0054.md` remains `PENDING_ADMISSION, not READY`;
2. the source deliberately says “superficially different”, so source-intent/admissibility deserves independent review even though C033 is finitely inequivalent under the frozen convention;
3. no current-package `P26-AUDIT-R11-I0054` end-to-end PASS was recovered;
4. no second independent current-package OTHER-track PASS was recovered;
5. the dated prior-art search is bounded and does not certify publication novelty.

I therefore do **not** call Aldous--Janson Open Problem 18 closed.

The geometric distribution, its memoryless property, elementary Bonferroni bounds, finite-state Euler convergence, and rotor-router philosophy are standard/folklore ingredients. No novelty claim is made for them. The potentially new content is U012, the specific one-geometric-budget-per-internal-node C033 construction, and its complete projective `J_1` convergence proof to CTCS(infinity).

---

## 13. Structured ledger delta

```yaml
ledger_delta:
  track: R11
  lane: CLOSABLE_OUTSIDE
  source: "Aldous--Janson arXiv:2303.02529v3 Open Problem 18 / I0054"
  metric_name: "number of distinct nontrivial discrete model classes with complete author-side full CTCS(infinity) limit proofs under frozen equivalence"
  before: 32
  after: 33
  movement: +1
  unchanged_count_after: 0
  status: PARTIAL
  new_claims:
    - id: R11-I0054-U012
      status: PROVED_AUTHOR_SIDE
      statement: "exact geometric-budget restriction/lumping compiler"
    - id: R11-I0054-C033
      status: PROVED_AUTHOR_SIDE
      statement: "finite-field geometric-budget rotor with exactly N-1 independent geometric budgets converges projectively in finite-restriction J1 to CTCS(infinity)"
  exact_self_check: "ALL_EXACT_CHECKS_PASS (3243 checks)"
  closure_audits:
    p26: MISSING_CURRENT_PACKAGE
    second_other_track: MISSING_CURRENT_PACKAGE
  admission: PENDING_ADMISSION_NOT_READY
  next_methods: [4, 17, 26]
```

---

## 14. Next nonrepeating route

The next method triple is **#4, #17, #26**: prove something weaker completely, look for the numbers somewhere else, and hunt the sporadic case.

The strongest next target is **not** another cosmetic rotor variant. C033 has reduced dynamic randomness to `N-1` integer variables. The next worthwhile question is whether one can quantify a genuine lower bound on the amount of randomness needed for a discrete model to converge to nondegenerate CTCS restrictions, and then find a construction close to that bound--for example a single finite seed whose deterministic expansion supplies all block clocks without collapsing finite-restriction independence. A complete entropy lower bound for even the `k=3`/`k=4` restrictions, together with one matching explicit finite-seed construction, would explain what cannot be derandomized rather than merely adding another class.
