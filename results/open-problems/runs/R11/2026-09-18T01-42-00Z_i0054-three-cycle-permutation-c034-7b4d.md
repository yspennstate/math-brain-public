Model: GPT-5.6 Sol. Reasoning: UNVERIFIED runtime level; GPT-6 / maximum was requested, but the exposed scheduler has no model-family or reasoning-effort selector, so GPT-6 / maximum is not verified or claimed. Metric movement: `33 -> 34` distinct nontrivial discrete model classes with complete author-side required-limit proofs under the frozen equivalence convention. Section-B moves actually tried: **#4 (prove something weaker, completely), #17 (look for the numbers somewhere else), #26 (hunt the sporadic case)**.

# R11 / I0054 — C034 conditioned-three-cycle permutation fragmentation

Problem/source: David J. Aldous and Svante Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529v3, **Open Problem 18**. The source asks whether superficially different discrete models can have the same `CTCS(infinity)` limit. Overall source status remains **PARTIAL, not CLOSED**. This run proves a new discrete class `R11-I0054-C034` with a complete finite-restriction `J_1` / projective convergence argument and an executed exact finite checker, but the canonical reservation is still `PENDING_ADMISSION, not READY` and the required independent audits are absent.

Run ID: `2026-09-18T01-42-00Z_i0054-three-cycle-permutation-c034-7b4d`  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Dated source/literature check: 2026-09-18

No email/Gmail, Drive, public posting, purchase, permission change, workflow execution, scheduler change, shared-root edit, or peer-track edit was performed.

---

## 1. Continuity, ownership, source, and topology

I continued from the newest completed R11 report

`runs/R11/2026-09-18T00-40-00Z_i0054-geometric-budget-rotor-c033-8f2a.md`

rather than restarting. That report moved the frozen metric `32 -> 33`, proved C033/U012, and used `#3/#7/#22`. This run deliberately used the nonrepeating triple `#4/#17/#26`.

Before new research I recovered the current campaign surfaces available through the GitHub connector: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/claims/I0054.md`, `operations/NEW_METHODS_2026-09-16.md`, the newest R11 report, the neighboring P13/I0051 record/search surface, current R11 commit history, and current I0054/audit searches. The connector does not provide a credible byte-for-byte traversal of every object in every intake JSONL, so I do not pretend to have manually reread all roughly 780 intake rows. Exact source/owner/history/exclusion/audit surfaces were recovered directly.

The canonical reservation still records R11 as owner and says `Status: PENDING_ADMISSION, not READY`. P13/I0051 remains a distinct Aldous--Janson clade-count problem and is not reassigned here. R11's old planar self-avoiding-walk route remains retired with its immutable handoff/history.

I reread the current primary source PDF. It is still arXiv:2303.02529v3 (18 Apr 2025). Printed page 58 states:

> Open Problem 18. Are there superficially different discrete models whose limit is the same CTCS(infinity)?

and immediately asks whether the source model's subordinator approximation can arise in another discrete tree model. The source abstract and Part III describe `CTCS(infinity)` through consistent exchangeable partitions. As in C001--C033, the source-facing convergence target here is therefore stronger than a root marginal: for every fixed `k` and finite `T`, prove whole-path convergence in `D([0,T],P_k)` with Skorokhod `J_1`, then pass to the projective exchangeable-partition limit.

For a block of size `b=i+j` and a specified unordered split `A|A^c`, `|A|=i`, the CTCS particular-split rate is

\[
q_b(A\mid A^c)=B(i,j)=\frac{(i-1)!(j-1)!}{(b-1)!},
\]

and the total CTCS exit rate is

\[
\frac12\sum_{i=1}^{b-1}{b\choose i}B(i,b-i)=H_{b-1}.
\]

### Runtime / scheduler control

The actual runtime identifies as GPT-5.6 Sol. Reasoning effort is not exposed and is therefore `UNVERIFIED`. The exposed scheduler/update schema offers prompt/title, schedule, enablement, and timing mode, but no model-family selector, reasoning-effort selector, authenticated runtime-model telemetry, or hour-long execution guarantee. Thus GPT-6/maximum remains prompt text rather than an enforceable setting. Repository policy records that a historical P26 `You cannot modify this task` result was authorization-context dependent; a still-denied task must be handled from its authorized owning workspace/control surface or platform support, not by cloning/bypassing it. This research run made no scheduler change.

---

## 2. Current literature / prior-art screen

Fresh dated searches checked the current Aldous--Janson source, 2026 critical-beta-splitting papers, conditioned random permutations, and random-permutation fragmentation.

Relevant findings:

1. Aldous--Janson Open Problem 18 remains present in the current v3 PDF.
2. Chorbadzhiyska--Minchev--Savov, arXiv:2608.18320 (18 Aug 2026), study beta-splitting trees through homogeneous fragmentations/subordinators and resolve a critical height problem, not Open Problem 18.
3. Heng Ma, arXiv:2609.14329 (13 Sep 2026), explicitly resolves Aldous--Janson Open Problem 4; arXiv:2609.14325 studies extremal separation/clade dynamics, not alternative discrete models with the full CTCS(infinity) limit.
4. Goldschmidt--Martin--Spano, *Fragmenting random permutations* (ECP 2008; arXiv:0712.0556), is directly relevant prior art: it proves existence of a fragmentation process whose `k`-block marginal is the cycle partition of a uniform permutation conditioned to have exactly `k` cycles. Thus **conditioned cycle partitions and fragmentation couplings are not new ingredients**.
5. Stirling-number / Feller-Chinese-restaurant formulas for the number of cycles of a uniform random permutation are classical and are not claimed as new.

The construction below is different from the Goldschmidt--Martin--Spano inter-`k` fragmentation: C034 repeatedly samples **independent ambient permutations conditioned to have exactly three cycles**, uses them as recursive tree-split proposals, and accelerates the proposal clock at the harmonic scale `H_{N-1}/2`. The bounded searches did not find this CTCS-limit construction or an announced resolution of exact Open Problem 18. This is a bounded negative search, **not a novelty certificate**.

A fresh repository search still recovers no current-package `P26-AUDIT-R11-I0054` end-to-end PASS and no second complete current-package OTHER-track PASS. Older scoped checks of earlier C00x/U00x components are not audits of C034 or of the whole present package.

---

## 3. Move #17 — the beta kernel is hidden in a three-cycle conditioning law

This is the new way in.

Let `sigma_N` be a uniform random permutation of `[N]`, and let `K_N` be its number of cycles. Condition on

\[
K_N=3.
\]

Restrict the cycle partition to a fixed visible set `[b]`. Write the visible partition as `pi={B_1,...,B_q}` with block sizes `n_1,...,n_q`, `q<=3`.

For an unconditioned uniform permutation of `[b]`, the probability of this **specified** cycle partition is

\[
\Pr(\Pi_b=\pi)=\frac{\prod_{a=1}^q(n_a-1)!}{b!}.
\tag{3.1}
\]

Use the Feller/Chinese-restaurant construction. The restriction to `[b]` is uniform on `S_b`, while future customers `b+1,...,N` start new cycles independently with probabilities `1/m`. Thus

\[
K_N=K_b+S_{b,N},
\qquad
S_{b,N}=\sum_{m=b+1}^{N}I_m,
\quad I_m\sim\operatorname{Bernoulli}(1/m),
\tag{3.2}
\]

with the future indicators independent of the visible permutation.

Put

\[
H=H_{N-1},\qquad
H^{(2)}=H_{N-1}^{(2)}=\sum_{m=1}^{N-1}\frac1{m^2},
\qquad
D_N=H^2-H^{(2)}.
\tag{3.3}
\]

The cycle-count generating function gives

\[
\Pr(K_N=3)=\frac1N e_2\!\left(1,\frac12,\ldots,\frac1{N-1}\right)
=\frac{D_N}{2N}.
\tag{3.4}
\]

For the tail count,

\[
\Pr(S_{b,N}=\ell)=\frac bN e_\ell\!\left(\frac1b,\frac1{b+1},\ldots,\frac1{N-1}\right).
\tag{3.5}
\]

### Exactly two visible cycles

For a specified unordered visible split `A|A^c`, `|A|=i`, `|A^c|=j`, `b=i+j`, equations (3.1)--(3.5) give

\[
\boxed{
 p_{N}^{(2)}(i,j)
 =2B(i,j)\frac{H-H_{b-1}}{D_N}.
}
\tag{3.6}
\]

The key number from the CTCS source has appeared without putting a beta kernel into the finite model by hand.

### Exactly three visible cycles

For a specified three-block partition with sizes `i,j,ell`, `i+j+ell=b`,

\[
\boxed{
 p_N^{(3)}(i,j,\ell)
 =\frac{2}{D_N}
 \frac{(i-1)!(j-1)!(\ell-1)!}{(b-1)!}.
}
\tag{3.7}
\]

There are no visible refinements of degree greater than three.

This is the useful sporadic feature: conditioning on exactly **three** ambient cycles leaves a first-order binary shadow on every fixed finite restriction, while the truly ternary part is one logarithmic order smaller.

---

## 4. Move #26 — exploit the sporadic `K_N=3` case

Take

\[
\boxed{
\lambda_N=\frac{H_{N-1}}2,
\qquad
\delta_N=N^{-2},
\qquad
a_N=\delta_N\lambda_N.
}
\tag{4.1}
\]

The acceleration is rational at every finite `N` and `a_N<1` for all `N>=3`.

Multiplying (3.6) by `lambda_N` gives the exact particular-binary-split rate

\[
\boxed{
q_N^{(2)}(i,j)
=B(i,j)\frac{H(H-H_{b-1})}{D_N}.
}
\tag{4.2}
\]

Since `H->infinity` while `H^{(2)}` stays bounded,

\[
\frac{H(H-H_{b-1})}{H^2-H^{(2)}}\longrightarrow1
\qquad(b\text{ fixed}),
\tag{4.3}
\]

so

\[
\boxed{q_N^{(2)}(i,j)\to B(i,j).}
\tag{4.4}
\]

The ternary rate from (3.7) is

\[
\boxed{
q_N^{(3)}(i,j,\ell)
=\frac{(i-1)!(j-1)!(\ell-1)!}{(b-1)!}
\frac{H}{D_N}
\longrightarrow0.
}
\tag{4.5}
\]

Thus a **genuinely ternary finite model** becomes the binary CTCS process on every fixed restriction. This is more source-facing than another perturbation of a binary finite model.

---

## 5. C034 — conditioned-three-cycle permutation hierarchy

For each `N>=3`, define a discrete-time fragmentation of `[N]` as follows.

At every raw step and for every current nonsingleton block `B`, independently:

1. toss an attempt coin with probability `a_N=delta_N lambda_N`;
2. if the attempt fails, leave `B` unchanged;
3. if it succeeds, draw an independent uniform permutation `sigma` of the ambient set `[N]` conditioned on `K(sigma)=3`;
4. replace `B` by the nonempty intersections of `B` with the three cycles of `sigma`;
5. if only one intersection is nonempty, this is an invisible/no-change attempt;
6. children are first processed at the next raw step.

Give one raw step physical duration `delta_N=N^{-2}`.

This is a finite, explicit, wholly discrete model. At the full root `B=[N]`, every successful attempt produces exactly **three nonempty children** because the ambient permutation has exactly three cycles.

### Almost-sure completion

Fix a nonsingleton block `B` and two distinct labels `x,y` in it. Among permutations with three cycles there exist permutations placing `x,y` in different cycles, hence the probability a successful attempt properly refines `B` is strictly positive. Attempts are independent from step to step with positive probability `a_N`; therefore `B` eventually splits almost surely. Each proper split strictly increases the number of blocks and there are at most `N-1` such increases before singletons. Hence the full finite hierarchy completes almost surely.

---

## 6. U013 — exact restriction/lumping theorem for ambient cycle proposals

The hidden-label issue is unusually clean here.

### Theorem U013

Fix `N` and a visible subset `S`. In C034, conditional on the entire visible history, each current visible block evolves exactly as follows: independently toss an attempt coin with probability `a_N`; on success, sample the restriction to that visible block of a fresh ambient uniform permutation conditioned on three cycles; split according to the nonempty visible cycle intersections.

In particular, the law of the visible process is independent of the sizes and histories of its hidden carrier blocks.

### Proof

At any raw time, every visible block `C` is contained in a unique current full carrier `B`. The attempt probability `a_N` does not depend on `|B|`. On an attempt, the ambient conditioned permutation is sampled fresh and independently of `B` and of the past.

If that permutation splits `B` but is monochromatic on `C` (all visible labels lie in one ambient cycle), the visible partition does not change and all labels of `C` pass into a unique child carrier. At the next raw step, that child again receives the same attempt probability `a_N` and, on success, a fresh ambient conditioned permutation. Thus an invisible hidden split leaves no residual state visible to `C`.

If the permutation has two or three nonempty cycle intersections with `C`, then those are exactly the visible children. Distinct visible blocks lie in distinct full carriers and use independent attempt coins/permutations. Induction over raw steps proves the claim. `QED`.

This exact lumping is the main reason to use an ambient `[N]` permutation rather than conditioning separately on the current carrier size.

---

## 7. Move #4 — prove the fixed-restriction theorem completely, then project

Fix `k`. By U013, the `[k]` restriction is an honest finite-state Markov chain on partitions of `[k]`.

Let `Q_N^{(k)}` be its one-step first-order rate matrix: a specified binary refinement receives rate (4.2), a specified ternary refinement rate (4.5), and the diagonal is minus the total visible exit rate.

For every fixed `k`, (4.4)--(4.5) imply entrywise, hence norm, convergence

\[
\boxed{Q_N^{(k)}\longrightarrow Q_{\rm CTCS}^{(k)}.}
\tag{7.1}
\]

Because the finite state space is fixed, the row sums of `Q_N^{(k)}` are uniformly bounded for all sufficiently large `N`.

In one raw step several current visible blocks may attempt simultaneously. With at most `k` nonsingleton blocks, a union bound gives

\[
\Pr(\text{at least two visible carriers attempt in one step})
=O_k(a_N^2).
\tag{7.2}
\]

Hence the exact one-step kernel `P_N^{(k)}` satisfies

\[
\boxed{
P_N^{(k)}
=I+\delta_NQ_N^{(k)}+R_N^{(k)},
\qquad
\|R_N^{(k)}\|_{\rm row,1}
=O_k(\delta_N^2\lambda_N^2).
}
\tag{7.3}
\]

Over a physical interval `[0,T]` there are `O(T/delta_N)` raw steps, so the accumulated error between the exact chain and the Euler chain with kernel `I+delta_N Q_N^{(k)}` is bounded by

\[
O_{k,T}(\delta_N\lambda_N^2)
=O_{k,T}\!\left(\frac{(\log N)^2}{N^2}\right)
\longrightarrow0.
\tag{7.4}
\]

Now compare the Euler chain with the CTMC having generator `Q_N^{(k)}`. Since the exit rates are uniformly bounded and `delta_N->0`, the usual geometric-to-exponential coupling gives `J_1` error going to zero on every bounded interval. Finally, because `Q_N^{(k)}->Q_CTCS^{(k)}` on a finite state space, uniformization with one common dominating Poisson clock couples the `Q_N^{(k)}` CTMC to the CTCS restriction with mismatch probability tending to zero on `[0,T]`.

Therefore

\[
\boxed{
\Pi_{N,034}^{[k]}
\Longrightarrow
\Pi_{\rm CTCS}^{[k]}
\quad\text{in }J_1
}
\tag{7.5}
\]

for every fixed `k` and finite `T`.

The models are exchangeable and their finite restrictions are exactly consistent. For any finite `K`, convergence of the `[K]` path controls all coordinates `k<=K`, while the tail of the retained projective metric is at most `2^{-K}`. Letting first `N->infinity` and then `K->infinity` yields

\[
\boxed{
\Pi_{N,034}
\Longrightarrow
\Pi_{\operatorname{CTCS}(\infty)}
}
\tag{7.6}
\]

in the projective finite-restriction path topology.

This is the full partition-valued genealogy limit required by the frozen R11 criterion, not a tagged-fragment or root-only limit.

---

## 8. Exact finite non-equivalence

C034 has an unusually strong finite witness.

For `N=3`, the only permutation with exactly three cycles is the identity `(1)(2)(3)`. Therefore, after suppressing waiting raw steps,

\[
\boxed{
\Pr_{\rm C034}(\deg(\text{first root})=3)=1.
}
\tag{8.1}
\]

More generally, for every `N>=3`, the full root `[N]` has degree exactly three at its first successful attempt, with probability one.

This is invariant under deterministic relabeling and global time/branch-length rescaling. It immediately separates C034 from the original binary critical beta-splitting model and from the retained binary R11 classes. The immutable R11 history records strict subunit degree-three witnesses for the earlier multifurcating classes (for example C002 `1/10`, C003 `1/22`, C004 `1/6`, C005 `1/728`, C006 `1/7`, C007/C008 `1/71`, C013 `35/1296`, C015 `2/17`), with later retained comparisons separating their remaining collisions. No prior retained R11 class has deterministic degree-three first root. Thus C034 is a new class under the frozen equivalence convention.

---

## 9. Exact self-check

The substantive checker is

`artifacts/R11/2026-09-18T01-42-00Z_i0054-three-cycle-permutation-c034-7b4d_checker.py`

created at commit

`c526e60a71b2b2c7e4b29e56e9a99b08d9ca034b`.

Its executed output is

`artifacts/R11/2026-09-18T01-42-00Z_i0054-three-cycle-permutation-c034-7b4d_checker_output.txt`

created at commit

`7a93e9faf887afe4f6144be802cc4f3a8de346c8`.

Clean stdout SHA-256:

`c36426e2ccb05e54d16bc8b20db25ddf005a268a0e508303d734ed6547fd9396`.

It performs **35,701 exact checks** and ends

`ALL_EXACT_CHECKS_PASS`.

In particular it:

- exhaustively enumerates every permutation with exactly three cycles for `N=3,...,8` and verifies 244 exact visible-partition probabilities against (3.6)--(3.7) and the one-block formula;
- verifies `P(K_N=3)=D_N/(2N)` by exact enumeration;
- verifies 20,362 exact binary/ternary rate identities;
- verifies the CTCS total exit-rate identity for `b=2,...,40`;
- checks exact monotone convergence direction on finite rational grids;
- certifies the `N=3` root-degree-three witness `1`;
- verifies full-root arity three on 15,023 conditioned permutations through `N=8`.

This is a self-check, not an independent audit.

---

## 10. Claim/status and metric

The stable new author-side claims are

\[
\boxed{\texttt{R11-I0054-U013 = PROVED\_AUTHOR\_SIDE}}
\]

and

\[
\boxed{\texttt{R11-I0054-C034 = PROVED\_AUTHOR\_SIDE under frozen equivalence}}.
\]

Therefore the fixed metric moves

\[
\boxed{33\longrightarrow34}.
\]

I am **not** calling Aldous--Janson Open Problem 18 closed. The current package still lacks the required P26 end-to-end PASS and the second independent OTHER-track PASS; the canonical reservation remains `PENDING_ADMISSION, not READY`; and the source phrase “superficially different” still deserves independent source-intent review. The honest source-level status remains **PARTIAL**.

---

## 11. What the three methods actually did

- **#17 — look for your numbers somewhere else:** the beta split rate appears as the first visible shadow of a uniform permutation conditioned to have three cycles; equation (3.6) is the exact bridge.
- **#26 — hunt the sporadic case:** `K_N=3` is special because visible degree two has probability order `1/H_N`, visible degree three order `1/H_N^2`, and no higher degree is possible. After `H_N/2` acceleration, binary CTCS survives and ternary events disappear.
- **#4 — prove something weaker, completely:** rather than start from an infinite-tree assertion, prove exact hidden-label lumping and the full finite-`k` generator/J1 theorem first; the projective CTCS(infinity) limit then follows cleanly.

### Next nonrepeating methods

The next triple recorded is **#1, #16, #25**. The highest-value next direction is not another clock perturbation. Change category from permutations to **random mappings / functional digraphs or random set partitions**, compute small cases exactly, and ask whether another classical conditioned component-count law has a binary `B(i,j)` first shadow. If so, seek a double-counting identity that gives the CTCS generator without importing the permutation-cycle formula.

---

## ledger_delta

```yaml
track: R11
source: I0054
status: PARTIAL
metric_name: distinct_nontrivial_discrete_model_classes_with_complete_required_limit_proof
before: 33
after: 34
movement: "+1"
new_model: "C034 conditioned-three-cycle permutation fragmentation"
new_theorem: "U013 exact ambient-cycle restriction/lumping theorem"
model_status: "PROVED_AUTHOR_SIDE"
source_status: "PARTIAL"
methods_used: [4, 17, 26]
next_methods: [1, 16, 25]
checker: "artifacts/R11/2026-09-18T01-42-00Z_i0054-three-cycle-permutation-c034-7b4d_checker.py"
checker_commit: "c526e60a71b2b2c7e4b29e56e9a99b08d9ca034b"
output: "artifacts/R11/2026-09-18T01-42-00Z_i0054-three-cycle-permutation-c034-7b4d_checker_output.txt"
output_commit: "7a93e9faf887afe4f6144be802cc4f3a8de346c8"
output_sha256: "c36426e2ccb05e54d16bc8b20db25ddf005a268a0e508303d734ed6547fd9396"
audits_required:
  p26_end_to_end: "NOT_RECOVERED"
  second_other_track_end_to_end: "NOT_RECOVERED"
closure: false
```
