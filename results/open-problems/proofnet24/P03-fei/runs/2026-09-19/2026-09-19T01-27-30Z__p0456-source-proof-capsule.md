Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.**

**NO SOURCE-LEVEL COEFFICIENT-METRIC MOVEMENT; NEW SELF-CONTAINED SOURCE-AUDIT CAPSULE.** The three admitted coefficient metrics remain saturated at `c_LK^cert=a_LK^fine=b_LK^sqrt=0`; no stuck count is manufactured from saturation, and HARD recoveries remain `0/2`. This run uses fresh Section-B methods **#4 PROVE SOMETHING WEAKER, COMPLETELY, #19 MAKE IT AN ALGORITHM, #22 READ THE FAILURES, NOT THE SUCCESSES**. The substantive advance is to compress the source-matching Claims 288/289 into one auditor-sized proof whose interaction branches and component estimates are explicit and whose connectivity step no longer imports the old Claim-278/280 large-component envelope as a black box.

# P03 / P0456 run report — self-contained source-matching proof capsule

Run timestamp: **2026-09-19T01:27:30Z**  
Track: **P03**  
Canonical target: **P0456**  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Category: **HARD OUTSIDE**

---

## 1. Continuity, controls, audit-first screen, and source status

The exclusive assignment remains

`operations/claims/P0456.md`,

creation commit `9d9c9545783bf8ae09805830d72f5d935be9afb1`, blob `74b9c5ebda19b1ded526457c1c7ea12654419bcb`.

The newest complete P03 report entering this run was

`proofnet24/P03-fei/runs/2026-09-19/2026-09-19T00-27-09Z__p0456-bivariate-rare-event-crosscheck.md`,

creation commit `7054579cffed69a9f404594d52210da9786fbcbd`, blob `6256a48b2ba38ec5dd291619e45f9653ebf091b9`; its exact-commit readback recovered `**End of complete run report.**`.

I preserve Claims 274, 276, 278, 280, 282, 284, 286 and Claims 288--300.

This run reread/recovered root `README.md`, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, current `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`, the canonical P0456 claim, the newest P03 report, the fixed-root interaction and small-component proofs, the neighboring P0457 ownership record, the current P26 directory and newest P26 report, and the current P04 run directory state. Large connector-rendered policy/root surfaces are truncated and therefore were not byte-for-byte reread; exact paths and scoped reads/searches were used for every mathematical dependency below.

### 1.1 Fresh incoming outside-audit screen

A newer P26 report has appeared:

`proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_03-56-31__run-report.md`,

creation commit `c8bcf0be3f194acbac0a4af4a25810e26c94217e`, blob `6bce41029beea87cab702d1b0e46705672421f44`.

It audits **P04/I0101 Claim 42 (six-channel escape conservation)**, not P0456. Fresh repository searches for `P0456` together with `PASS`, `audit`, Claim 288, and Claim 289 still recover no P26 or genuinely distinct OTHER-track full-chain P0456 audit. P04 has no `2026-09-19` run directory; its terminal mathematical state remains rotation-stopped, so there is no new P04 successor theorem to audit and I do not fabricate a repeat audit.

Therefore the closure gate remains

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2`.

Self-audits do not count. No paper folder and no source-CLOSED label are created.

### 1.2 Fresh source / current-literature check

The primary source remains Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, *Journal of Applied Probability* 63(2) (June 2026), 552--579, DOI `10.1017/jpr.2025.10051`, published online 18 December 2025.

Fresh Cambridge retrieval on 19 September 2026 again verifies the literal model: iid Uniform[0,1] edge weights on `K_n`, and an edge survives exactly when it is among the `k` lowest incident weights at **both** endpoints. Section 1.1 still states that connectivity is unknown in the displayed band

`log n - 0.5 loglog n sqrt(log n) <= k <= log n + 0.5 loglog n sqrt(log n)`,

and says the gap arises from analytically simpler sufficient conditions. Lemmas 10--14 and Theorems 3--6 remain the relevant source comparison points.

Fresh bounded searches for the exact DOI/title/authors and for 2026 bilateral-preference Poisson/isolated-vertex/connectivity updates recovered the Cambridge article and bibliographic copies but no later source-matching constant-window or Poisson theorem. This is dated bounded negative evidence only; **publication novelty remains UNVERIFIED**.

Neighboring P0457 is a distinct diameter problem owned by NM13-04 and is not duplicated here.

---

## 2. New claim: the source-matching audit capsule

### Claim `P03-P0456-SOURCE-AUDIT-CAPSULE-301`

**Status:** `PROVED / SELF-AUDIT-CAPSULE / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

Fix `C<infinity`. Uniformly over integers

`|k-log n|<=C`,

let `I_v` be the isolation indicator and `Z_n=sum_v I_v`. Then:

1. for every fixed `r>=1` and every fixed distinct roots `v_1,...,v_r`,

   `P(I_{v_1}=...=I_{v_r}=1)=e^{-rk}(1+o_C(1))`;             (2.1)

2. with `lambda_n=n e^{-k}`,

   `d_TV(Law(Z_n),Poisson(lambda_n)) -> 0` uniformly on the displayed window;   (2.2)

3. the probability of a nontrivial component tends to zero uniformly:

   `P(exists component of size 2,...,floor(n/2))=o_C(1)`;     (2.3)

4. hence

   `P(LK(n,k) connected)=exp(-lambda_n)+o_C(1)`.             (2.4)

In particular, if `k-log n->c`, then `Z_n => Poisson(e^{-c})` and connectivity tends to `exp(-e^{-c})`.

This is the source-matching content of Claims 288/289, repackaged for an outside auditor. It deliberately excludes Claims 290 and 293--300 and all first/second-correction material.

---

## 3. #4 PROVE SOMETHING WEAKER, COMPLETELY — the only analytic lemma the capsule needs

The proof uses one local rejection lemma. It is stated broadly enough to survive every bounded interaction defect used later.

### Lemma 3.1 (clean and bounded-omission marked saddle)

Let `k=log n+O(1)`. Let `m=n+O(1)` proposal edges and `N=n+O(k)` possible outside competitors be iid Uniform[0,1]. Let

`q_h(x)=P(Bin(N,x)>=h)`,

`Q_h(x)=int_0^x q_h(u)du`,

with `h=k-d` for fixed `d>=0`.

(a) If all first `p=k-a` proposal edges, with fixed `a>=0`, are required to be rejected using at least `h` outside competitors, then

`M_{p,h}=e^{-h}(1+o_C(1)).`                                  (3.1)

(b) More generally, if a fixed number of arbitrary deadlines among the first `p` are omitted and every remaining deadline may have its required outside-competitor count lowered by a fixed amount, the probability of satisfying all remaining rejection constraints is

`<= exp[-k+o_C(k)].`                                         (3.2)

#### Proof

Let `B_h~Beta(h,N-h+1)`. Beta-binomial duality gives

`q_h(x)=P(B_h<=x)`,

and therefore

`Q_h(x)=E[(x-B_h)_+]`.                                       (3.3)

Write `mu=E B_h=h/(N+1)` and note `sd(B_h)=O(sqrt(k)/n)`.

For the clean event, rank integration followed by one integration by parts gives

`M_{p,h}=(m)_{p+1}/p! int_0^1 Q_h(x)^p(1-x)^(m-p-1)dx`.      (3.4)

Replacing `B_h` by its mean yields an exact beta integral; after `x=mu+(1-mu)y` it equals

`(1-mu)^m(1+o(1))=e^{-h}(1+o(1))`,                           (3.5)

where the fixed difference `k-p=a` only changes a rational factor tending to one.

To control the replacement error, split at

`x_0=mu+k/(2N)`.

For `x>=x_0`, a fixed Chernoff lower-tail bound for the beta/binomial dual gives

`R_h(x):=E[(B_h-x)_+] <= O(sqrt(k)/n)e^{-gamma k}`            (3.6)

for some fixed `gamma>0`; hence

`sup_{x>=x_0} p R_h(x)/(x-mu)=o(1)`,                         (3.7)

so `Q_h(x)^p=(x-mu)^p(1+o(1))` uniformly there. For `x<=x_0`, after `x=mu+zk/N`, the normalized log-integrand loses a fixed positive multiple of `k`, since `log z-z+1<0` uniformly for `z<=1/2`; the `O(sqrt(k)/n)` beta fluctuation cannot recover this loss. Thus (3.5) is asymptotically exact and proves (a).

For (b), after conditioning on the relevant order-statistic deadline, omitting at most `D` arbitrary constraints means that among the first `k-O(1)` proposal points at most `D+O(1)` may be unmarked. The conditional binomial tail is bounded by

`C_D k^D [Q_h(t)/t]^{k-O(1)}`.                               (3.8)

Integrating against the order-statistic density gives an integral of the form

`C_D k^D int t^D Q_h(t)^{k-O(1)}(1-t)^{m-k}dt`.              (3.9)

The same split (3.6)--(3.7) incurs only `exp(o(k))`; after mean replacement the extra fixed power `t^D` expands into finitely many exact beta integrals, each `O(e^{-h})`. Hence the whole expression is

`exp[-h+o(k)]=exp[-k+o(k)]`,                                 (3.10)

uniformly for fixed defects. This proves the lemma. `square`

The point is that **the omitted deadlines may be arbitrary ranks**. No interaction witness is ever assumed to occur at a favorable proposal position.

---

## 4. #19 MAKE IT AN ALGORITHM — finite interaction exploration for `r` isolated roots

Fix distinct roots `R={v_1,...,v_r}`, with `r` fixed. Temporarily remove the `binom(r,2)` root-root edges from their preference orders. For root `a`, expose the ordered first `k` nonroot proposal labels

`L_{a,1},...,L_{a,k}`

and proposal deadlines

`D_{a,1}<...<D_{a,k}`.

The following finite checklist is the entire dependence analysis.

### Step A — selected-label equality partition

The `rk` ordered labels form independent without-replacement arrays from `N=n-r` labels. Identify equal labels across different roots. If the equality partition has `m` blocks, define collision excess

`c=rk-m`.

For every compatible fixed partition `pi`, exactly

`P(pi)=(N)_m/(N)_k^r`.                                       (4.1)

Thus a witness-labelled collision pattern of excess `c` has probability `n^{-c+o(1)}`; summing its at most `(rk)^{2c}` witnesses still costs `n^{-c+o(1)}`. A triple collision contributes two repeats, exactly as it should.

### Step B — threshold guard

Choose fixed `D_0>r+2`, then choose `L` so large that

`rho(L):=L-1-log L > r+D_0+3`.

Let `G_L` be the event that all root `k`th nonroot thresholds are at most `Lk/n`. Standard order-statistic Chernoff gives

`P(G_L^c)=o(e^{-rk} n^{-D_0}).`                              (4.2)

### Step C — active internal edges

On `G_L`, scan every unique edge which can contaminate an outside-only rejection list.

* A selected--selected edge is active if its weight is below an applicable proposal deadline. A prescribed such edge costs at most `2Lk/n`.
* If `u` is selected by root `a` but not by root `b`, the root-selected cross edge `{v_b,u}` is conditioned to be nonselected at `b`. Given root-`b` threshold `T_b=t`, its weight is exactly Uniform[`t`,1]. Hence for any applicable deadline `D<=Lk/n`,

  `P(W(v_b,u)<=D | T_b=t, u nonselected at b)=((D-t)_+)/(1-t)=O_L(k/n)`.   (4.3)

* Each temporarily deleted root-root edge is early with probability at most `2Lk/n`.

Let `q` be the number of unique active selected/root-selected edges and `p` the number of early root-root edges. Define total defect complexity

`K=c+q+p`.                                                    (4.4)

For every fixed witness-labelled skeleton of complexity `d`,

`P(skeleton,G_L)<=n^{-d+o(1)}`,                              (4.5)

and the number of fixed-`d` witness-labelled skeletons is `k^{O_{r,d}(1)}=n^{o(1)}`. Sequential exposure therefore gives

`P(G_L,K>=D_0)<=n^{-D_0+o(1)}=o(e^{-rk}).`                   (4.6)

### Step D — disjointize bounded nonzero skeletons

If `1<=K<D_0`, do this deterministically:

1. in each repeated-label block retain one occurrence and omit every other attached rejection deadline;
2. for every active internal edge omit every deadline for which it could serve as a competitor;
3. for each early root-root edge omit the bounded number of root deadlines whose ranks can shift when it is reinserted.

Only `O_{r,D_0}(1)` deadlines per root are omitted.

Now comes the exact stopping rule: rejection of proposal `{v_a,u}` is determined only by the **raw weights in the star of `u`** below `D_{a,i}`. It never asks whether those competitor edges themselves survive the bilateral rule. Hence exploration stops after one selected-neighbour star. After the omissions above, every remaining rejection list uses edges from one distinct selected label to the external set

`V \ (R union all selected labels)`,

and those edge sets are literally disjoint.

Lemma 3.1(b) then gives conditional rejection cost `exp[-rk+o(k)]`. Combining with (4.5), all positive bounded-complexity skeletons together contribute

`e^{-rk+o(k)} n^{-1+o(1)}=o(e^{-rk}).`                       (4.7)

### Step E — zero skeleton

If `K=0`, every selected label is distinct, no internal/cross edge can help before a deadline, and root-root edges do not alter the selected sets. Actual isolation then forces the clean outside rejection event. The outside lists are disjoint, and Lemma 3.1(a) gives

`P(all roots isolated,K=0)<=e^{-rk}(1+o_C(1)).`              (4.8)

For the matching lower bound require: all labels distinct; `G_L`; every root-root edge later than `Lk/n`; and every selected neighbor has `k` lighter competitors in the external pool. This event implies all roots are isolated. Distinct labels cost `1-O_r(k^2/n)`, root-root lateness costs `1-O_r(k/n)`, and the clean rejection blocks are independent with probability `e^{-k}(1+o_C(1))` each. The marked saddle mass outside `G_L` is negligible at the `e^{-rk}` scale. Therefore

`P(all roots isolated)>=e^{-rk}(1-o_C(1)).`                  (4.9)

Equations (4.2), (4.6)--(4.9) prove (2.1) for every fixed `r`, including `r=1`. In particular the one-root isolation asymptotic is not a separate heuristic:

`P(I_v)=e^{-k}(1+o_C(1)).`                                   (4.10)

This checklist is finite, terminates at depth one, and assigns a probability cost to every nonclean branch.

---

## 5. Poisson law, including uniform total variation on fixed windows

For every fixed `r`, (2.1) gives

`E[(Z_n)_r]=(n)_r e^{-rk}(1+o_C(1)).`                         (5.1)

Take any sequence with `|k-log n|<=C`. By compactness, every subsequence has a further subsequence along which

`k-log n -> c in [-C,C]`.

Along that subsequence, (5.1) converges to `e^{-rc}` for every fixed `r`, the factorial moments of `Poisson(e^{-c})`. The first moment is uniformly bounded, so the sequence is tight; the Poisson law is moment-determinate. Hence

`Z_n => Poisson(e^{-c})`.                                    (5.2)

Because the state space is countable, weak convergence implies pointwise convergence of the probability mass functions, and Scheffe's lemma gives total-variation convergence to `Poisson(e^{-c})`. Also `lambda_n=ne^{-k}->e^{-c}`, so Poisson laws with parameters `lambda_n` converge in total variation to the same limit. If uniform convergence in (2.2) failed, a bad subsequence would contradict this subsequence argument. Thus (2.2) holds uniformly for every fixed `C`.

This avoids the known logical failure of using only one- and two-point asymptotics: the capsule proves **all fixed factorial moments**.

---

## 6. Literal nontrivial-component elimination — self-contained capsule version

This section deliberately avoids mean-degree inference.

### 6.1 Sizes `2<=r<=6`: external proposals, independent of tree conditioning

Fix `r in {2,...,6}`. Let `G^+` be the global event that every vertex's `k`th incident order statistic is at most `Lk/n`, where fixed `L` has `L-1-log L>2`. A union bound over the order-statistic Chernoff estimate gives `P((G^+)^c)=o(1)`.

If a fixed `r`-set `S` is a connected component on `G^+`, it contains a spanning tree `T`, and every tree edge has weight at most `Lk/n`. For a fixed labelled `S,T`, the `r-1` tree edges are distinct iid uniforms, so

`P(tree edges all early)<=(Lk/n)^{r-1}.`                     (6.1)

Now **ignore all internal edges of `S`** when ordering proposals from each `v in S`, and set

`p_0=k-(r-1)`.

The first `p_0` external proposal edges are necessarily among the global first `k` incident edges, because at most `r-1` internal edges can precede them. If `S` is a component, every such external proposal must be rejected by its outside endpoint.

Crucially, the external proposal/rejection edge families are independent of the internal tree-edge weights. Apply the same finite interaction algorithm of Section 4 to the `r p_0` external proposal slots. Since `p_0=k-O_r(1)`, Lemma 3.1 and the same skeleton costs give, for any fixed `D`,

`P(all external blocks rejected)<=e^{-rk+o(k)}+n^{-D+o(1)}.` (6.2)

Take `D=3`. Summing over at most `binom(n,r)r^{r-2}` labelled sets and Cayley trees gives

`P(exists r-component,G^+)`
` <= binom(n,r)r^{r-2}(Lk/n)^{r-1}[e^{-rk+o(k)}+n^{-3+o(1)}]`
` = n^{1-r+o(1)}k^{r-1}+n^{-2+o(1)}k^{r-1}`
` =o(1).`                                                     (6.3)

Together with `P((G^+)^c)=o(1)`, sizes `2,...,6` vanish.

The important point is that no tree-edge value is conditioned on when external proposal ranks are defined. This removes the historical tree-conditioning bias.

### 6.2 Sizes `7<=r<=n/2`: one global two-sided threshold envelope, paid once

Here is a compact direct argument that replaces the old Claims 278/280 component envelope inside this capsule.

Let `T_v` be the global `k`th smallest incident weight and put

`a=5/32`, `b=32/5`.

Define

`H={ a k/(n-1) <= T_v <= b k/(n-1) for every vertex v }`.    (6.4)

For one vertex,

`P(T_v<a k/(n-1)) <= exp[-(a-1-log a+o(1))k]`,              (6.5)

`P(T_v>b k/(n-1)) <= exp[-(b-1-log b+o(1))k]`.              (6.6)

Numerically,

`a-1-log a = 1.0125479903... >1`,

`b-1-log b = 3.5437020096... >1`.

Since `k=log n+O(1)`, a union bound over all `n` vertices gives

`P(H^c)=o(1)`.                                               (6.7)

On `H`, if a set `S` of size `r` is a component, some spanning tree of `S` has every edge weight at most `bk/(n-1)`: a retained edge is below both endpoint `k`th thresholds. Conversely every crossing edge between `S` and `S^c` must have weight at least `ak/(n-1)`, because an edge below that value is below both endpoint thresholds and would be bilaterally retained. Tree edges and crossing edges are disjoint independent uniform variables. Hence

`P(exists r-component,H)`
` <= binom(n,r) r^{r-2} [bk/(n-1)]^{r-1}`
`    * [1-ak/(n-1)]^{r(n-r)}.`                               (6.8)

For each fixed `r=7,...,12`, the logarithm of the right side is

`(1-5r/32)log n+O_r(loglog n)`,                              (6.9)

which tends to `-infinity` because `5r/32>1`.

For `13<=r<=n/2`, use `binom(n,r)<=(en/r)^r` and `(n-r)/(n-1)>=1/2` for large `n`. Equation (6.8) is at most

`C n/(bk r^2) [b e k exp(-ak/2)]^r`.                         (6.10)

Since `a/2=5/64` and `k=log n+O(1)`, the bracket is

`q_n=O(k n^{-5/64})=o(1)`.                                  (6.11)

Therefore

`sum_{r=13}^{floor(n/2)} P(exists r-component,H)`
` <= C n/k * q_n^{13}/(1-q_n)`
` = n^{-1/64+o(1)}=o(1).`                                    (6.12)

Combining (6.3), (6.7), (6.9), and (6.12) proves (2.3) entirely under the literal bilateral-preference definition. The global threshold failure event is paid **once**, before summing component sizes.

---

## 7. Connectivity and Claim-289 uniformity

A disconnected graph either has an isolated vertex or a component of size between `2` and `n/2`. By (2.3),

`P(connected)=P(Z_n=0)+o_C(1)`.                              (7.1)

Uniform total variation (2.2) gives

`P(Z_n=0)=exp(-lambda_n)+o_C(1)`,                            (7.2)

so (2.4) follows. If `k-log n->c`, then `lambda_n->e^{-c}` and the limiting connectivity probability is `exp(-e^{-c})`.

This is the exact source-matching conclusion. No mean-degree implication is used anywhere.

---

## 8. #22 READ THE FAILURES, NOT THE SUCCESSES — historical weak points and where the capsule repairs them

I audited the proof by starting from the recorded failures rather than from its final statements.

### Failure 1: shared selected-label rejection lists

**Old danger:** two roots can propose to the same outside label, so their rejection lists are not independent.

**Repair:** exact equality partitions (4.1). A label occurring in `q` root blocks contributes collision excess `q-1`; duplicate deadlines are omitted before factorization. Every repeat costs a power of `n`.

### Failure 2: root-selected cross edges are not fresh Uniform[0,1]

**Old danger:** after conditioning that a label was not selected at root `b`, its edge weight is biased upward.

**Repair:** use the exact conditional law Uniform[`T_b`,1], equation (4.3). This still costs `O(k/n)` for every relevant deadline and is the correct conditional probability.

### Failure 3: vague “complete interaction patterns”

**Old danger:** bounded-complexity strata are not literally finite because proposal ranks vary with `k`.

**Repair:** witness-labelled skeletons are explicitly `k^{O(D)}=n^{o(1)}`. Their codimension is the integer `K=c+q+p`, and every branch has cost `n^{-K+o(1)}`.

### Failure 4: hidden recursive dependence

**Old danger:** rejecting one proposal might appear to require recursively exploring whether competitor edges themselves survive.

**Repair:** it does not. Rejection counts **raw incident weights**. The exact dependency radius is one selected-neighbour star. After disjointization there is no unexplored “late influence.”

### Failure 5: pair asymptotics do not imply Poisson

**Old danger:** one- and two-point probabilities can match Poisson while the count is not Poisson; the earlier exact 0/2-subset counterexample demonstrates this.

**Repair:** Section 4 proves (2.1) for **every fixed `r`**, and Section 5 uses the full factorial-moment sequence. No pair-only inference remains.

### Failure 6: naive Stein dependency graph is effectively complete

**Old danger:** isolation indicators have no useful sparse deterministic dependency graph.

**Repair:** the capsule does not use a dependency graph or generic local-dependence rhetoric. Factorial moments are sufficient. Claims 293--294 remain independent self-checks, not dependencies of Claim 301.

### Failure 7: tree-conditioning bias for small components

**Old danger:** conditioning tree edges to be light can bias the proposal ranks used to reject crossing edges.

**Repair:** Section 6.1 orders **external proposals after deleting all internal component edges**. The first `k-(r-1)` external proposals are among the global first `k` regardless of internal weights, and their edge families are independent of the tree edges.

### Failure 8: repeated global `o(1)` terms while summing component sizes

**Old danger:** a threshold-envelope failure probability cannot be paid once per component size.

**Repair:** the two-sided event `H` in Section 6.2 is imposed globally and its `o(1)` complement is paid exactly once before the entire sum over `7<=r<=n/2`.

No new P26 objection to P0456 exists in the current repository. I found no unstated uniformity assumption in the capsule: all analytic estimates are uniform for fixed `C`, fixed root count, and fixed defect complexity.

---

## 9. Directed P03 -> P04 duty

The current P04 `2026-09-19` run directory is absent, and the newest P26 report confirms P04 remains rotation-stopped while auditing a preserved historical I0101 theorem. There is therefore no genuinely new accessible P04 successor claim to audit this run. I do not repeat an old audit merely to fill the slot.

---

## 10. Cumulative status, exact remaining obligation, and `ledger_delta`

Preserved source-matching chain:

- `P03-P0456-POISSON-CRITICAL-WINDOW-288 = PROVED / SOURCE-MATCHING-CANDIDATE-COMPLETE / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`;
- `P03-P0456-UNIFORM-POISSON-INTERACTION-REPAIR-289 = PROVED / SELF-AUDIT-REPAIR / SOURCE-MATCHING-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`;
- Claim 290 marked PPP;
- Claims 291--300 supporting self-audit/strengthening kernels;
- new `P03-P0456-SOURCE-AUDIT-CAPSULE-301 = PROVED / SELF-AUDIT-CAPSULE / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

Protocol state:

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2 / CLAIM_301_SOURCE_CAPSULE_READY`.

Exact remaining obligation is unchanged but now narrower for an auditor: P26 and one genuinely distinct OTHER track must independently verify Lemma 3.1, the finite interaction algorithm in Section 4, the factorial-moment-to-uniform-TV passage, and the literal component proof in Section 6. Any gap found by either audit overrides all strengthening claims. Only after both passes may P03 create the source-matching paper folder and request closure through P26's shared-ledger process.

`ledger_delta` for P26:

```yaml
track: P03
source: P0456
status: SOURCE_MATCHING_CANDIDATE_COMPLETE_AUDIT_PENDING
new_claim: P03-P0456-SOURCE-AUDIT-CAPSULE-301
new_claim_status: PROVED_SELF_AUDIT_CAPSULE_SUPPORTING
independent_audits_found: 0/2
source_closed: false
paper_package_created: false
metrics:
  c_LK_cert: 0_saturated
  a_LK_fine: 0_saturated
  b_LK_sqrt: 0_saturated
stuck_increment: 0
hard_recoveries: 0/2
outside_audit_request:
  - verify bounded-omission marked saddle uniformly on |k-log n|<=C
  - verify explicit collision/active-edge/root-root skeleton codimension and disjointization
  - verify all-fixed-r factorial moments imply uniform TV by subsequence compactness
  - verify small-component external-proposal argument and global two-sided threshold envelope for all larger sizes
```

---

## 11. Next state

The mathematical source claim should now receive outside scrutiny rather than more high-order self-strengthening. On the next run, incoming P26/OTHER audits still take absolute priority. If none exist, the next useful work is to adversarially attack Claim 301 as an auditor would: isolate the exact constants in the global threshold envelope, check the bounded-omission lemma under the most hostile rank placement, and try to construct a finite interaction configuration not captured by `K=c+q+p`. No new coefficient window or correction term should be pursued until that audit surface has been exhausted.

The requested GPT-6/maximum setting remains prompt-only in the exposed scheduler/task controls. This run actually used GPT-5.6 Sol; reasoning metadata is UNVERIFIED. No permission denial occurred. GitHub only; no Gmail/email, Drive, public posting, workflow execution, paid compute, access changes, peer-file edits, or additional schedules.

**End of complete run report.**