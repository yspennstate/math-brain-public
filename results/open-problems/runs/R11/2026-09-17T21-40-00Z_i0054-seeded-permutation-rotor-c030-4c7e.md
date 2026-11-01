Model: GPT-5.6 Sol. Reasoning: UNVERIFIED runtime level; GPT-6 / maximum was requested, but no model-family or reasoning-effort selector is exposed, so GPT-6 / maximum is not verified or claimed. Metric movement: `29 -> 30` distinct nontrivial discrete model classes with complete author-side required-limit proofs under the frozen equivalence convention. Section-B moves actually tried: **#10 (derandomize), #14 (find the group acting), #19 (make it an algorithm)**.

Problem/source: David J. Aldous and Svante Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529v3, **Open Problem 18**, intake `I0054`. Overall campaign status remains **PARTIAL, not CLOSED**. This run proves a new discrete class `R11-I0054-C030`, a seeded symmetric-group permutation rotor which replaces C029's fresh random injections by one initial random seed and then a deterministic finite permutation schedule.

Run ID: `2026-09-17T21-40-00Z_i0054-seeded-permutation-rotor-c030-4c7e`  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Dated source/literature check: 2026-09-17

No email/Gmail, Drive, public posting, purchase, permission change, workflow execution, scheduler change, shared-root edit, or peer-track edit was performed.

---

## 1. Continuity, source, ownership, and exact target

I continued from the newest complete R11 report

`runs/R11/2026-09-17T20-40-00Z_i0054-hypergeometric-rotor-c029-5b8e.md`

rather than restarting. It moved the metric `28 -> 29`, proved C029, and recorded #10/#14/#19 as the next nonrepeating methods.

Before research I reread the campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md` and `RESULTS.md`, `operations/claims/I0054.md`, `operations/NEW_METHODS_2026-09-16.md`, the newest R11 report, targeted I0054 prior-attempt searches, and the neighboring P13/I0051 material. The canonical claim remains owned by R11 with status `PENDING_ADMISSION, not READY`; no conflicting I0054 owner was found. P13's I0051/Open Problem 9 clade-covariance track remains distinct. The former planar self-avoiding-walk route remains retired with immutable history.

I reread the current arXiv source itself. It is still v3, revised 18 April 2025. Section 6.3, printed page 58, states Open Problem 18: are there superficially different discrete models whose limit is the same CTCS(infinity)? The next sentence asks whether the source's subordinator-approximation mechanism can arise in another discrete tree model. The paper formalizes CTCS(infinity) via its consistent exchangeable-partition restrictions.

Accordingly the required convergence here is not a root-shape law, a tagged fragment, or a one-time marginal. For every fixed `k`, I prove convergence of the full restriction path in `D([0,T], P_k)` with Skorokhod `J_1` topology for every finite `T`; the mutually consistent limits are the CTCS(k) restrictions and hence determine CTCS(infinity) in the exchangeable-partition/projective sense used by the source.

### Runtime/model-control status

The runtime identifies as GPT-5.6 Sol; reasoning effort is not exposed and is therefore `UNVERIFIED`. The scheduler/control schema available to this environment exposes title/prompt, schedule, enablement and timing mode, but no model-family selector, reasoning-effort selector, authenticated runtime telemetry, or hour-long-duration guarantee. GPT-6/maximum is therefore prompt text only. Root policy records that the historical P26 `You cannot modify this task` error was authorization-context dependent and that a later P26 update succeeded from an authorized context. The legitimate remedy for a still-denied task is its authorized owner/workspace control surface or platform support exposing the missing controls, not cloning or bypassing it. No scheduler change was attempted.

---

## 2. Current literature and prior art

Fresh dated searches used combinations of `Aldous Janson Open Problem 18 CTCS`, `CTCS discrete model beta splitting 2026`, `critical beta-splitting CTCS 2026`, `rotor-router derandomized random walk`, and `k-wise independent permutations group actions`.

The current source remains arXiv:2303.02529v3. The recent Chorbadzhiyska--Minchev--Savov preprint arXiv:2608.18320 studies beta-splitting via homogeneous fragmentations/subordinators and resolves a height question. Heng Ma's September 2026 work arXiv:2609.14329 explicitly addresses Open Problem 4, while arXiv:2609.14325 studies extremal separation/clade dynamics. I found no paper in this bounded search announcing a solution of Open Problem 18. This is a bounded negative search, not proof of worldwide openness and not a novelty certificate.

Rotor-router / Propp-machine derandomizations are classical prior art, as are group-action and k-wise-permutation methods. I make no novelty claim for deterministic rotors, permutation orbits, or the falling-factorial Vandermonde identity. The potentially new content is the particular harmonic symmetric-group rotor below, its exact CTCS cycle generator, and the full partition-path convergence argument.

Repository prior-attempt recovery includes C001--C029. An exact current search still recovers no current-package `P26-AUDIT-R11-I0054` end-to-end PASS and no second complete current-package OTHER-track PASS. Hence the source cannot be called closed under the fleet protocol.

---

## 3. Move #10: derandomize C029's injections

C029 uses a deterministic phase rotor `s=1,...,N-1` but redraws a uniform injection of every activated block into an `N`-site urn. The first attempt here was to replace those injections by cyclic shifts of one deterministic assignment.

That fails already at `N=4`, `s=2`: with red sites `{1,2}`, the four cyclic shifts produce only the adjacent red two-subsets

`{1,2}, {2,3}, {3,4}, {1,4}`,

and never the opposite support `{1,3}`. Thus a cyclic subgroup does not reproduce the hypergeometric support counts. The exact checker records this obstruction.

The repair is to rotor through the full symmetric group. That is factorially large, but size is irrelevant for this existence problem and it gives exact orbit counts rather than an approximation.

---

## 4. C030: the seeded symmetric-group permutation rotor

Fix `N>=3`. Let

`G_N=(g_1,...,g_{N!})`

be any deterministic enumeration of `S_N`, with `g_1=id`. Draw one initial seed permutation

\[
\Sigma_N\sim \operatorname{Unif}(S_N).
\]

This is the only permutation randomness in the construction. The activation coins described below remain random.

For each phase `s=1,...,N-1`, define the deterministic urn with red sites `{1,...,s}` and blue sites `{s+1,...,N}` and

\[
w_{N,s}=\frac{N}{2s(N-s)},\qquad
c_{N,s}=(N-1)w_{N,s}=\frac{N(N-1)}{2s(N-s)}.
\]

The master rotor lists every pair `(s,g)` with `s=1,...,N-1`, `g in G_N`, **twice consecutively**, first all duplicated entries with `s=1`, then `s=2`, and so on. One cycle therefore has

\[
M_N=2(N-1)N!
\]

raw steps. The duplication is not needed for the limit theorem; it creates a transparent finite-law witness separating C030 from C029.

Choose cycle duration and raw mesh

\[
\tau_N=N^{-3},\qquad
\delta_N=\frac{\tau_N}{M_N}
=\frac{1}{2N^3(N-1)N!}.
\]

At rotor entry `(s,g)`, define the global site map

\[
\Phi=g\circ\Sigma_N:[N]\to[N].
\]

For every current nonsingleton tree block `C`, independently activate it with probability

\[
a_{N,s}=\delta_N c_{N,s}.
\]

If activated, color label `ell in C` red iff `Phi(ell)<=s`; if both colors occur, split `C` into its two color classes, otherwise leave it unchanged. Advance to the next rotor entry after the raw step. After the `M_N`-th entry, repeat the same master cycle.

The rule is a finite discrete model. It has no fresh injection, no random locus, no stochastic environment and no random population state. A uniform seed makes its finite law label-exchangeable: relabeling the leaves by `pi` simply replaces `Sigma_N` by `Sigma_N o pi^{-1}`, which is again uniform. Restrictions of a realized `[N]` path to smaller label sets are automatically coherent as restrictions of the same hierarchy.

Activation is valid since `c_{N,s}<=N/2` and `delta_N N/2<1`.

---

## 5. Move #14: the symmetric-group orbit exactly reproduces the hypergeometric law

Fix a seed `sigma`; the proof is quenched in `sigma`. Right multiplication by `sigma` is a bijection of `S_N`, so

\[
\{g\circ\sigma:g\in S_N\}=S_N.
\tag{5.1}
\]

Fix a current block `C` of size `b=i+j` and a specified unordered support `A|C\A` with `|A|=i`. At phase `s`, the fraction of `g in S_N` for which the deterministic colors induced by `g o sigma` realize this support is therefore exactly

\[
h_{N,s}(i,j)
=
\frac{(s)_{\underline i}(N-s)_{\underline j}
+(s)_{\underline j}(N-s)_{\underline i}}
{(N)_{\underline{i+j}}}.
\tag{5.2}
\]

This is exactly C029's hypergeometric support probability, but now it is an orbit count, not a random sampling probability.

Let `Q_N` denote the CTCS(N) generator on labeled partitions. The CTCS rate of this specified support is

\[
B(i,j)=\frac{(i-1)!(j-1)!}{(i+j-1)!}.
\]

The first-order contribution over one C030 rotor cycle equals

\[
\frac{1}{M_N}\sum_{\text{rotor entries}}c_{N,s}
\mathbf 1\{\text{specified support is realized}\}
=
\sum_{s=1}^{N-1} w_{N,s}h_{N,s}(i,j).
\]

As in C029, cancellation of `s(N-s)` and the falling-factorial Vandermonde identity give

\[
\sum_{s=1}^{N-1}
(s-1)_{\underline{i-1}}(N-s-1)_{\underline{j-1}}
=(i-1)!(j-1)!\binom{N-1}{i+j-1},
\]

hence, **for every finite `N>=i+j` and every fixed seed**,

\[
\boxed{
\frac{1}{M_N}\sum_{\text{rotor entries}}c_{N,s}
\mathbf 1\{A|C\setminus A\text{ occurs}\}=B(i,j).
}
\tag{5.3}
\]

Thus the one-cycle averaged first-order generator is exactly `Q_N`.

---

## 6. Move #19: algorithmic whole-path coupling

The exact orbit identity is not enough by itself; one must control multiple jumps inside a rotor cycle and recover the continuous jump times.

### 6.1 Uniform CTCS exit bound

For a CTCS block of size `b`, summing the rates of all unordered split supports gives

\[
\lambda_b
=\frac12\sum_{i=1}^{b-1}\binom bi B(i,b-i)
=\frac b2\sum_{i=1}^{b-1}\frac1{i(b-i)}
=H_{b-1}.
\tag{6.1}
\]

Therefore for any partition `x` of `[N]`,

\[
\lambda(x)=\sum_{C\in x}H_{|C|-1}
\le\sum_{C\in x}(|C|-1)\le N-1.
\tag{6.2}
\]

### 6.2 One rotor cycle

Fix a seed and start a complete rotor cycle from state `x`. For each potential specified split event `e` at raw entry `r`, its first-order probability is `delta_N` times its deterministic activation rate. By (5.3), summing all such hazards over the complete cycle gives exactly

\[
\tau_N\lambda(x)\le \tau_NN.
\tag{6.3}
\]

The same statement holds for every possible post-jump state. Since hazards are nonnegative, the total remaining hazard in any suffix of the rotor cycle is at most the corresponding full-cycle hazard and hence at most `tau_N N`.

It follows by conditioning on the first visible jump that the probability of a second visible jump in the same cycle is at most a universal constant times

\[
(\tau_NN)^2.
\tag{6.4}
\]

This bound also covers two different blocks activating in the same raw step: after exposing one successful visible activation, the total probability of another successful activation among the unexposed decisions is bounded by the remaining cycle hazard. No independence between successive partition states is assumed.

Consequently the exact cycle-boundary transition kernel `C_N^sigma` satisfies, uniformly in the seed and state,

\[
\|C_N^\sigma-[I+\tau_NQ_N]\|_{TV}
\le C\tau_N^2N^2.
\tag{6.5}
\]

For the actual CTCS(N) semigroup, (6.2) gives the analogous short-time expansion

\[
\|e^{\tau_NQ_N}-[I+\tau_NQ_N]\|_{TV}
\le C\tau_N^2N^2.
\tag{6.6}
\]

Hence one cycle of C030 can be maximally coupled to a CTCS(N) interval of length `tau_N` with failure probability at most `C tau_N^2 N^2`.

### 6.3 Bounded physical time and `J_1`

On `[0,T]` there are at most `T/tau_N+1` complete cycles. Union bounding the cycle couplings yields

\[
\Pr\{\text{cycle-boundary disagreement by time }T\}
\le C_T\tau_NN^2
=O_T(N^{-1}).
\tag{6.7}
\]

The probability that either coupled process has two or more visible jumps in any one cycle is bounded by the same order. On the complementary event, move the unique intra-cycle C030 jump, if any, to the corresponding cycle boundary. The time displacement is at most `tau_N=N^{-3}`. Therefore a coupling can be chosen so that

\[
\Pr\!\left\{d_{J_1,[0,T]}
(\Pi_N^{\mathrm{C030}},\Pi_N^{\mathrm{CTCS}(N)})>\tau_N\right\}
=O_T(N^{-1}).
\tag{6.8}
\]

This is stronger than a fixed-`k` generator convergence statement: it couples the entire `[N]` partition path to CTCS(N) on every bounded time interval.

Now fix `k`. Restriction to `[k]` cannot create a path discrepancy, while the CTCS family is consistent under restriction. Thus

\[
\boxed{
\Pi_N^{\mathrm{C030},[k]}
\Longrightarrow \Pi_{\mathrm{CTCS}}^{[k]}
\quad\text{in Skorokhod }J_1,
}
\tag{6.9}
\]

for every fixed `k`. The CTCS(k) limits are mutually consistent and define the exchangeable-partition process CTCS(infinity), so the complete C030 hierarchy converges in the corresponding finite-restriction/projective path topology:

\[
\boxed{
\Pi_N^{\mathrm{C030}}
\Longrightarrow \Pi_{\operatorname{CTCS}(\infty)}.
}
\tag{6.10}
\]

This is the source-required whole genealogy limit, not a marginal substitute.

---

## 7. Finite non-equivalence

C030 is not merely C029 with the injection randomness hidden.

### 7.1 Direct C029 separation

At `N=4`, the first rotor entry is `(s=1,g=id)` and is repeated immediately. For every seed, if the four-label root splits in raw step 1, exactly one leaf is red and its three-leaf sibling block consists entirely of labels mapped to blue sites. Raw step 2 uses the identical map and phase, so this three-leaf child cannot split then. Hence for

`E = {root splits at raw step 1 and its three-leaf child splits at raw step 2}`,

\[
\Pr_{\mathrm{C030}}(E)=0.
\tag{7.1}
\]

For C029 at `N=4`, its phase-1 root activation is `1/8`; the next phase is `s=2`, whose activation probability is `3/32`; every three-site sample from a two-red/two-blue urn is nonmonochromatic. Thus

\[
\Pr_{\mathrm{C029}}(E)=\frac18\frac3{32}=\frac3{256}>0.
\tag{7.2}
\]

### 7.2 Time-rescaling-invariant root-shape witness

A stronger witness uses only the eventual first-root shape. At `N=4`, C030 has

\[
M_4=144,\qquad \tau_4=\frac1{64},\qquad
\delta_4=\frac1{9216},
\]

and activation probabilities

\[
a_1=a_3=\frac1{4608},\qquad a_2=\frac1{6144}.
\]

Write

\[
u=1-a_1=\frac{4607}{4608},\qquad
v=1-a_2=\frac{6143}{6144},\qquad n_*=48.
\]

During one cycle, the probabilities that the first root activation lies in the phase-1, phase-2, or phase-3 group are proportional to

\[
U_1=1-u^{n_*},\quad
U_2=u^{n_*}(1-v^{n_*}),\quad
U_3=(uv)^{n_*}(1-u^{n_*}).
\]

At phases 1 and 3, a particular `1|3` support is selected by one quarter of the permutations; at phase 2, a particular unordered `2|2` support is selected by one third. Repetition of complete cycles multiplies all first-root probabilities by the same geometric survival factor. Hence the exact particular-support ratio is

\[
\boxed{
R_{\mathrm{C030}}
=\frac34\frac{U_1+U_3}{U_2}
=2.0001413147409273\ldots
}
\tag{7.3}
\]

and exact arithmetic proves

\[
\boxed{2<R_{\mathrm{C030}}<\frac{459}{224}.}
\tag{7.4}
\]

The retained binary finite-witness values through C029 are

\[
2,\ \frac75,\ \frac{2699}{1365},\ \frac{2273}{1153},\
\frac{61381}{43765},\ \frac{166094447739}{85563797248},\
\frac{33}{17},\ \frac53,\ \frac{597}{359},\ \frac{18}{11},\
\frac95,\ \frac54,\ \frac{459}{224}.
\]

The exact checker verifies collision with none of them. The remaining retained classes are already separated in immutable R11 history by positive finite multifurcation witnesses, whereas C030 is binary. Root-shape law is invariant under deterministic label relabeling and global branch-time rescaling. Therefore C030 is distinct from C001--C029 under the frozen equivalence convention.

---

## 8. Exact self-check

The substantive checker is

`artifacts/R11/2026-09-17T21-40-00Z_c030_seeded_permutation_rotor_checker.py`

and its archived output is

`artifacts/R11/2026-09-17T21-40-00Z_c030_seeded_permutation_rotor_checker.out`.

It performs **5,133 exact rational/arithmetic checks**. It verifies:

- exhaustive `S_N` orbit counts against the hypergeometric formula for small `N`;
- the exact finite-`N` beta generator identity;
- the falling-factorial Vandermonde identity;
- the CTCS block exit identity `lambda_b=H_{b-1}`;
- the failure of the naive cyclic-shift subgroup;
- the seeded-orbit identity `{g o sigma}=S_N`;
- the zero-versus-`3/256` C030/C029 two-step witness;
- activation and cycle scaling;
- the exact bracket `2<R_C030<459/224`; and
- separation from every retained binary witness through C029.

The executed output ends `ALL_EXACT_CHECKS_PASS` with archived stdout SHA-256

`9ef6ee8b5aee3a9d2777f1f5edb4eeebb3e1049eb7a55be56d6e7573ad4fd4b0`.

These are self-checks, not independent audits.

---

## 9. Status and next route

The new stable author-side claim is

\[
\boxed{\texttt{R11-I0054-C030 = PROVED\_AUTHOR\_SIDE under frozen equivalence}.}
\]

The fixed metric therefore moves

\[
\boxed{29\to30}.
\]

I do **not** call Open Problem 18 closed. The canonical claim remains `PENDING_ADMISSION, not READY`; publication novelty is unverified; and the required current-package P26 end-to-end PASS plus a second independent current-package OTHER-track PASS are still absent. Under the fleet protocol the source status remains **PARTIAL**.

The next nonrepeating methods are **#5, #11, #27**. The next research target is to compress the factorial full-`S_N` rotor. Add a family parameter controlling permutation-design strength (#5), use the representation/group-action dual side to characterize which orbit moments are actually needed (#11), and swap the quantifiers from “exact for every split of all `N` labels” to “for every fixed visible `k`, one small design works uniformly as `N` grows” (#27). A successful version would retain the full CTCS(infinity) limit with a polynomial-size or explicit low-discrepancy permutation schedule.

```yaml
ledger_delta:
  track: R11
  intake: I0054
  source: "Aldous--Janson, arXiv:2303.02529v3, Open Problem 18"
  target: "genuinely different discrete models with the full CTCS(infinity) exchangeable-partition limit"
  metric_name: "number of distinct nontrivial discrete model classes with complete author-side required-limit proofs under frozen equivalence"
  before: 29
  after: 30
  movement: +1
  status: PARTIAL
  methods_used: [10, 14, 19]
  new_claim: "R11-I0054-C030 = PROVED_AUTHOR_SIDE under frozen equivalence"
  claim_registry_status: "PENDING_ADMISSION, not READY"
  p26_current_package_audit: missing
  second_other_track_current_package_audit: missing
  checker: "artifacts/R11/2026-09-17T21-40-00Z_c030_seeded_permutation_rotor_checker.py"
  checker_output: "artifacts/R11/2026-09-17T21-40-00Z_c030_seeded_permutation_rotor_checker.out"
  exact_checks: 5133
  checker_result: "ALL_EXACT_CHECKS_PASS"
  source_resolution_check: "no later Open Problem 18 resolution found in bounded dated search; not a novelty certificate"
  next_methods: [5, 11, 27]
  scheduler_change: false
  shared_root_change: false
  peer_file_change: false
```
