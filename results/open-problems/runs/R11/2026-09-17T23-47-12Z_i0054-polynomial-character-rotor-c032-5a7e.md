Model: GPT-5.6 Sol. Reasoning: UNVERIFIED runtime level; GPT-6 / maximum was requested, but no model-family or reasoning-effort selector is exposed, so GPT-6 / maximum is not verified or claimed. Metric movement: `31 -> 32` distinct nontrivial discrete model classes with complete author-side required-limit proofs under the frozen equivalence convention. Section-B moves actually tried: **#10 (derandomize), #21 (ask who else has this shape), #30 (one prime / one scale / one direction at a time)**.

# R11 / I0054 — C032 polynomial-character rotor

Problem/source: David J. Aldous and Svante Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529v3, **Open Problem 18**. The source asks whether superficially different discrete models can have the same `CTCS(infinity)` limit. Overall campaign status remains **PARTIAL, not CLOSED**. This run proves a new discrete class `R11-I0054-C032`: an explicit finite-field polynomial-character rotor whose full finite restrictions converge to `CTCS(infinity)`.

Run ID: `2026-09-17T23-47-12Z_i0054-polynomial-character-rotor-c032-5a7e`  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Dated source/literature check: 2026-09-17 UTC / 2026-09-18 Jerusalem local date

No email/Gmail, Drive, public posting, purchase, permission change, workflow execution, scheduler change, shared-root edit, or peer-track edit was performed.

---

## 1. Continuity, source, ownership, and topology

I continued from the newest complete R11 report

`runs/R11/2026-09-17T22-40-00Z_i0054-polynomial-design-rotor-c031-6b1d.md`,

which moved the frozen metric `30 -> 31`, proved C031, and recorded #10/#21/#30 as the next nonrepeating method triple. Those are the methods actually used here.

Before new research I recovered the current campaign controls from `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, canonical ownership file `operations/claims/I0054.md`, the newest R11 report, the neighboring P13/I0051 Aldous--Janson report/claim, and repository-wide I0054/audit/history searches. The GitHub connector provides bounded fetch/search views rather than a credible byte-for-byte reread of every repository object, so I do not claim an invisible exhaustive traversal of every intake JSONL row. The exact source target, claim, exclusions, current R11 state, neighboring ownership, and audit surfaces were recovered.

The canonical claim still says:

- owner `R11`;
- source `arXiv:2303.02529v3`, Open Problem 18;
- status `PENDING_ADMISSION, not READY`.

No competing I0054 owner was recovered. P13's I0051/Open Problem 9 clade-count problem remains distinct and is not reassigned. The old R11 self-avoiding-walk route remains historical/retired.

I reread the current arXiv PDF. Printed page 58 still states Open Problem 18:

> Are there superficially different discrete models whose limit is the same CTCS(infinity)?

The following sentence says that the key feature of the authors' model seems to be the subordinator approximation and asks whether this can arise in another discrete tree model. Earlier, Part 5.3 says CTCS(infinity) is formalized using Kingman's theory of exchangeable partitions and defines the time-indexed partition of the positive integers whose finite restrictions are the finite CTCS trees.

The source itself does not name a Skorokhod topology. R11's frozen source-facing criterion is therefore the following precise process-level strengthening: for every fixed `k` and finite `T`, the entire restriction path converges in `D([0,T], P_k)` with Skorokhod `J_1`, and these compatible finite restrictions converge projectively to the exchangeable-partition process `CTCS(infinity)`. No root marginal or tagged-fragment limit is substituted for the full genealogy.

### Runtime/model-control status

The runtime identifies as GPT-5.6 Sol. Reasoning effort is not exposed and is therefore `UNVERIFIED`. The scheduler/control schema visible to this environment exposes title/prompt, schedule, enablement and timing mode, but no model-family selector, reasoning-effort selector, authenticated runtime-model telemetry, or guaranteed hour-long execution. Thus GPT-6/maximum remains a request in prompt text only. Repository evidence also shows that the historical P26 `You cannot modify this task` response was authorization-context dependent: a later authorized context did succeed in updating P26. For any still-denied task the legitimate remedy is the authorized owner/workspace surface or platform support, not cloning or bypassing the task. No scheduler modification was attempted here, in accordance with the current owner instruction.

---

## 2. Current literature and prior-art screen

Fresh searches on 2026-09-17/18 used `Aldous Janson Open Problem 18 CTCS infinity`, `same CTCS infinity discrete model`, `critical beta-splitting CTCS 2026`, `almost k-wise independent permutations`, and `Weil additive character polynomial finite field`.

The current source is still arXiv:2303.02529v3. Chorbadzhiyska--Minchev--Savov, arXiv:2608.18320 (18 August 2026), studies the full beta-splitting family via homogeneous fragmentations/subordinators and resolves a critical height problem. Heng Ma, arXiv:2609.14329 (13 September 2026), answers Aldous--Janson Open Problem 4 on discrete-time tree height. I found no announcement in this bounded search of a resolution of Open Problem 18. This is a bounded negative search, **not** a novelty certificate.

Move #21 deliberately looked outside probability-tree language. The closest machinery is pseudorandomness and finite-field character sums. Kaplan--Naor--Reingold and related work construct small almost-k-wise independent permutation families; this supports the general idea that fixed finite restrictions only need low-order pseudorandomness. For the construction below an even simpler tool is enough: the classical Weil additive-character bound. If `Q in F_p[t]` is nonconstant of degree `D<p`, then for a nontrivial additive character

\[
\left|\sum_{t\in\mathbb F_p} e_p(Q(t))\right|\le (D-1)\sqrt p.
\tag{2.1}
\]

I make no novelty claim for Weil, Fourier inversion, Vandermonde invertibility, Bertrand's postulate, low-order pseudorandomness, or harmonic Riemann sums. The potentially new content is the explicit rotor below and its CTCS whole-path limit.

Current repository search still recovers no current-package `P26-AUDIT-R11-I0054` end-to-end PASS and no second complete current-package OTHER-track PASS. Consequently source closure is not certified.

---

## 3. Move #10: derandomize C031 completely at the environment level

C031 already reduced the factorial symmetric-group rotor C030 to a polynomial-size deterministic approximate design, but the design itself was obtained nonconstructively: a probabilistic-method argument proved that a good fixed-size subset family exists, and C031 chose the lexicographically first good family.

The question in this run was whether one can replace that existence step by a closed algebraic formula and, at the same time, reduce the deterministic rotor period substantially.

The answer is yes. The new environment has only `p_N(p_N-1)=O(N^2)` entries, where `p_N` is the least prime at least `N`.

---

## 4. Move #30: localize to one prime and one fixed restriction

For each `N>=3`, let

\[
p=p_N:=\min\{q\ge N:q\text{ prime}\}.
\tag{4.1}
\]

Bertrand's postulate gives

\[
N\le p<2N.
\tag{4.2}
\]

Embed the leaf labels `[N]` injectively as `0,1,...,N-1` in `F_p`. Put

\[
d=d_p:=\min\{p-1,\max(2,\lfloor\log_2p\rfloor)\}.
\tag{4.3}
\]

Then `d -> infinity` and `d<p`.

For `a,t in F_p`, define the deterministic score

\[
Y_t(a):=\sum_{r=0}^{d-1}a^r t^{r+1}\pmod p.
\tag{4.4}
\]

Use the canonical representatives `0,...,p-1`. For `s=1,...,p-1`, define the red set

\[
R_{s,t}:=\{a\in[N]:Y_t(a)\in\{0,1,\ldots,s-1\}\}.
\tag{4.5}
\]

The deterministic environment cycles lexicographically through

\[
(s,t),\qquad s=1,\ldots,p-1,\quad t\in\mathbb F_p.
\tag{4.6}
\]

Thus the rotor has exactly `p(p-1)=O(N^2)` entries.

Set

\[
w_{p,s}:=\frac{p}{2s(p-s)},
\qquad
c_{p,s}:=(p-1)w_{p,s},
\tag{4.7}
\]

and choose one complete rotor-cycle duration

\[
\tau_N:=p^{-2},
\qquad
\delta_N:=\frac{\tau_N}{p(p-1)}.
\tag{4.8}
\]

At rotor entry `(s,t)`, every current nonsingleton tree block independently activates with probability

\[
a_{p,s}:=\delta_Nc_{p,s}
=\frac{\tau_N w_{p,s}}{p}.
\tag{4.9}
\]

If a block activates, each of its labels is colored red or blue according to membership in `R_{s,t}`; if both colors occur, split the block into the two color classes. Otherwise the block stays intact. Then advance the rotor.

This is a finite discrete random tree model. The environment and every coloring are explicit and deterministic; the only randomness is in the independent activation coins.

### C032 really reaches a full binary tree

A nontrivial point is that the rotor cannot trap a nonsingleton block forever. Take two distinct labels `a!=b`. The score difference

\[
Y_t(a)-Y_t(b)
=\sum_{r=1}^{d-1}(a^r-b^r)t^{r+1}
\tag{4.10}
\]

is a nonzero polynomial because its `t^2` coefficient is `a-b != 0`. Its degree is at most `d<p`, so it cannot vanish for every `t in F_p`. For some `t`, the two score representatives are different; choosing a threshold `s` between them separates the labels. Therefore every nonsingleton block has at least one rotor entry at which its coloring is nonmonochromatic. That entry has positive activation probability, and repeated cycles use independent activation coins, so the block splits almost surely. Recursing through finitely many descendants gives an almost surely finite full binary hierarchy.

Restriction consistency within each `N` is exact in law. A visible block always has a unique carrier block in the full hierarchy. A hidden-only split may change the carrier but does not split the visible block. At the next rotor entry the carrier receives a fresh activation coin with the same probability, while its visible colors depend only on `(s,t)` and the visible labels. Thus hidden labels do not bias the visible restriction.

---

## 5. Move #21: finite-field pseudorandomness for every fixed restriction

Fix distinct labels `a_1,...,a_k` with `k<=d`, and let `xi=(xi_1,...,xi_k) in F_p^k` be nonzero. Then

\[
\sum_{j=1}^k\xi_jY_t(a_j)
=\sum_{r=0}^{d-1}
\left(\sum_{j=1}^k\xi_ja_j^r\right)t^{r+1}.
\tag{5.1}
\]

The first `k` coefficient sums cannot all vanish. Indeed, if

\[
\sum_j\xi_ja_j^r=0,\qquad r=0,\ldots,k-1,
\tag{5.2}
\]

then the Vandermonde matrix `(a_j^r)_{0<=r<k,1<=j<=k}` is invertible and forces `xi=0`, a contradiction. Therefore the polynomial in (5.1) is nonconstant of degree at most `d<p`.

By Weil,

\[
\left|
\mathbb E_{t\in F_p}
 e_p\!\left(\sum_j\xi_jY_t(a_j)\right)
\right|
\le
\beta_p:=\frac{d-1}{\sqrt p}.
\tag{5.3}
\]

So every nontrivial Fourier coefficient of the joint score vector

\[
(Y_t(a_1),\ldots,Y_t(a_k))
\tag{5.4}
\]

is at most `beta_p` in magnitude.

### Interval Fourier norm

Let `I_s={0,...,s-1}` and use normalized Fourier transform on `F_p`. For `xi!=0`,

\[
|\widehat{1_{I_s}}(\xi)|
\le
\frac{1}{p|\sin(\pi\xi/p)|}.
\tag{5.5}
\]

If `m=min(xi,p-xi)<=p/2`, then `sin(pi m/p)>=2m/p`, hence

\[
\|\widehat{1_{I_s}}\|_1
\le 1+H_{(p-1)/2}=:L_p.
\tag{5.6}
\]

The complement indicator has the same bound. Fourier inversion and (5.3) now show that for any prescribed red/blue pattern on `k<=d` distinct labels,

\[
\left|
\Pr_t\{\text{that pattern under }R_{s,t}\}
-
\left(\frac{s}{p}\right)^{r}
\left(1-\frac{s}{p}\right)^{k-r}
\right|
\le
\beta_pL_p^k.
\tag{5.7}
\]

This bound is uniform in the labels and in `s`.

For one specified unordered `i|j` support, `b=i+j<=d`, there are two oriented patterns, so if `h_{p,s,t}(i,j)` denotes its deterministic indicator and `x_s=s/p`, then

\[
\left|
\frac1p\sum_t h_{p,s,t}(i,j)
-
\bigl[x_s^i(1-x_s)^j+x_s^j(1-x_s)^i\bigr]
\right|
\le2\beta_pL_p^b.
\tag{5.8}
\]

---

## 6. The CTCS beta kernel appears after harmonic averaging

Let `q_N(i,j)` be the first-order rate of a fixed specified unordered `i|j` split averaged over one complete C032 rotor cycle. By (4.9),

\[
q_N(i,j)
=
\sum_{s=1}^{p-1}w_{p,s}
\left(\frac1p\sum_{t\in F_p}h_{p,s,t}(i,j)\right).
\tag{6.1}
\]

The Bernoulli comparison has an exact simplification:

\[
\begin{aligned}
&\sum_{s=1}^{p-1}w_{p,s}
\bigl[x_s^i(1-x_s)^j+x_s^j(1-x_s)^i\bigr]\\
&\qquad=
\frac1p\sum_{s=1}^{p-1}
\left(\frac{s}{p}\right)^{i-1}
\left(1-\frac{s}{p}\right)^{j-1}.
\end{aligned}
\tag{6.2}
\]

The two oriented terms become equal after the change `s -> p-s`. Hence the right side is an ordinary Riemann sum and

\[
\frac1p\sum_{s=1}^{p-1}
\left(\frac{s}{p}\right)^{i-1}
\left(1-\frac{s}{p}\right)^{j-1}
=
B(i,j)+O_{i,j}(p^{-1}),
\tag{6.3}
\]

where

\[
B(i,j)=\int_0^1x^{i-1}(1-x)^{j-1}\,dx
=\frac{(i-1)!(j-1)!}{(i+j-1)!}
\tag{6.4}
\]

is exactly the CTCS rate of that specified split.

Also

\[
\sum_{s=1}^{p-1}w_{p,s}=H_{p-1}.
\tag{6.5}
\]

Combining (5.8)--(6.5), for every fixed `b=i+j`, eventually `b<=d`, and uniformly over all specified supports,

\[
\boxed{
|q_N(i,j)-B(i,j)|
\le
O_b(p^{-1})
+
2\frac{d-1}{\sqrt p}L_p^bH_{p-1}
=O_b\!\left(p^{-1/2}(\log p)^{b+2}\right)
\to0.
}
\tag{6.6}
\]

This is the key finite-field derandomization estimate. Unlike C031, no existence theorem or stored approximate design is needed.

---

## 7. Whole-path convergence, not a marginal limit

Fix `k` and let `Q_N^(k)` be the first-order generator on partitions of `[k]` obtained from one C032 cycle. Since the partition state space is finite and (6.6) is uniform over its finitely many possible specified splits,

\[
\|Q_N^{(k)}-Q_{\rm CTCS}^{(k)}\|_{\rm row,1}\longrightarrow0.
\tag{7.1}
\]

The total activation mass for one current block during a complete cycle is

\[
\sum_{s=1}^{p-1}\sum_{t\in F_p}a_{p,s}
=	au_N\sum_{s=1}^{p-1}w_{p,s}
=	au_NH_{p-1}.
\tag{7.2}
\]

A partition of `[k]` has at most `k` blocks. Expanding the product of all raw-step kernels over one cycle therefore gives, uniformly over starting states,

\[
C_N^{(k)}
=
I+\tau_NQ_N^{(k)}
+O_k\bigl(\tau_N^2H_{p-1}^2\bigr).
\tag{7.3}
\]

The genuine CTCS semigroup satisfies

\[
e^{\tau_NQ_{\rm CTCS}^{(k)}}
=
I+\tau_NQ_{\rm CTCS}^{(k)}+O_k(\tau_N^2).
\tag{7.4}
\]

Maximally couple the two chains at cycle boundaries. Over at most `T/tau_N+1` cycles, the probability of any boundary mismatch is at most

\[
T\|Q_N^{(k)}-Q_{\rm CTCS}^{(k)}\|_{\rm row,1}
+O_{k,T}(\tau_NH_{p-1}^2),
\tag{7.5}
\]

which tends to zero because `tau_N=p^{-2}`.

The probability that some cycle up to time `T` contains at least two visible fragmentation jumps is bounded by the same second-order scale

\[
O_{k,T}(\tau_NH_{p-1}^2)=O_{k,T}(p^{-2}\log^2p)\to0.
\tag{7.6}
\]

Away from that event, move the unique intra-cycle C032 jump to the corresponding cycle boundary. This alters its time by at most `tau_N ->0`. Therefore

\[
\boxed{
\Pi_N^{\rm C032,[k]}
\Longrightarrow
\Pi_{\rm CTCS}^{[k]}
\quad\text{in Skorokhod }J_1
}
\tag{7.7}
\]

on every bounded time interval and for every fixed `k`.

Because the finite CTCS restrictions are consistent and C032's restriction law is well-defined as above, the family of limits is the exchangeable-partition process of the source. Thus in the frozen projective finite-restriction topology,

\[
\boxed{
\Pi_N^{\rm C032}
\Longrightarrow
\Pi_{\operatorname{CTCS}(\infty)}.
}
\tag{7.8}
\]

This completes the required limit theorem for C032.

---

## 8. Why C032 is a genuinely new finite model under the frozen convention

The frozen equivalence permits deterministic leaf relabeling and global branch/time rescaling. Both preserve finite root-shape probabilities and zero-versus-positive first-step split events.

At `N=5`, `p=5`, `d=2`, `tau=1/25`, `delta=1/500`. On the four visible labels `{0,1,2,3}`, exact rational enumeration of the deterministic rotor gives one-cycle first-root masses

\[
m_{1|3}
=
\frac{60707555723460827945614074683399}
{4199040000000000000000000000000000},
\tag{8.1}
\]

for the particular support `{0}|{1,2,3}`, and

\[
m_{2|2}
=
\frac{126394002090531799}
{19440000000000000000}
\tag{8.2}
\]

for `{0,1}|{2,3}`. If the root survives an entire cycle, the same deterministic environment repeats and the activation coins are fresh; hence eventual first-split probabilities acquire the same factor `1/(1-S)` and their ratio is

\[
\boxed{
R_{\rm C032}
=
\frac{7703418956282489179517201}
{3464343821016000000000000}
=2.223630030469459\ldots
>
\frac{11}{5}.
}
\tag{8.3}
\]

All retained exact binary root witnesses through C029 are different. The C030 exact checker gives

\[
2<R_{\rm C030}<\frac{459}{224}<\frac{11}{5}<R_{\rm C032},
\tag{8.4}
\]

so C032 is not C030 either.

C031 has an even simpler separating event. Its lexicographically first phase-1 design entry is a singleton set, so conditional on root activation in its first raw step, the root splits nontrivially. In C032 the first entry is `(s,t)=(1,0)`; equation (4.4) gives `Y_0(a)=0` for every label, so every leaf is red and an activation is monochromatic. Thus

\[
P_{\rm C032}(\text{root splits in raw step 1})=0,
\qquad
P_{\rm C031}(\text{root splits in raw step 1})>0.
\tag{8.5}
\]

Relabeling cannot change zero to positive and a global time rescaling cannot alter this discrete transition law. The retained nonbinary classes are already separated in the immutable R11 history by positive finite multifurcation witnesses, while C032 is binary.

Therefore C032 is distinct from every retained C001--C031 class under the frozen equivalence convention.

---

## 9. Exact-arithmetic self-check

I wrote and executed

`artifacts/R11/2026-09-17T23-47-12Z_c032_polynomial_character_rotor_checker.py`.

It performs **85,218 exact checks**. The finite core checks:

- least-prime/Bertrand sanity and `d<p` for `3<=N<=80`;
- the exact harmonic identity `sum_s p/[2s(p-s)] = H_{p-1}`;
- Vandermonde invertibility for all tested distinct tuples through primes `<=31`;
- 700 exact low-order score-pattern count rows;
- C032 activation/coloring sanity;
- the exact `N=5` one-cycle root masses and ratio (8.3);
- six visible nontrivial four-label supports in the `N=5` cycle;
- separation from every retained exact binary root witness through C029;
- the archived C030 bracket; and
- the C031/C032 first-entry zero-versus-positive separation.

The checker intentionally does **not** pretend to machine-prove the classical Weil theorem; equation (2.1) is an explicitly imported published theorem. The executed output ends

`ALL_EXACT_CHECKS_PASS`

with clean stdout SHA-256

`538b9994491ac23c61bd1aade959ed208714cd1631db1dbc584c885cb4c36c2e`.

Checker creation/readback commit: `fda2af7471fbdd2cb04416e8d25369c9670d5444`.  
Output creation/readback commit: `4725734f55ce4fc38fea67b285ae4f89db03e567`.

This is a **self-check**, not an independent audit.

---

## 10. Result and closure status

The new stable author-side claim is

\[
\boxed{
\texttt{R11-I0054-C032 = PROVED\_AUTHOR\_SIDE under frozen equivalence.}
}
\tag{10.1}
\]

The fixed metric therefore moves

\[
\boxed{31\to32.}
\tag{10.2}
\]

This is genuine movement: C032 removes C031's probabilistic-method design existence, gives a closed algebraic schedule, reduces deterministic environment length from `O(N^7(log N)^2)` to `O(N^2)`, and proves the same complete finite-restriction `J_1` / projective CTCS(infinity) limit.

I am **not** calling Aldous--Janson Open Problem 18 closed. The canonical claim remains `PENDING_ADMISSION, not READY`; the current-package P26 end-to-end audit is still absent; a second independent OTHER-track current-package audit is still absent; and publication novelty remains unverified. The source-level campaign label therefore remains **PARTIAL**.

No paper folder is created because the fleet closure conditions have not been met.

---

## 11. What the three methods actually contributed

**#10 — DERANDOMIZE.** Replaced C031's lexicographically chosen probabilistic-method design by the explicit score formula (4.4). Result: a closed deterministic environment with `O(N^2)` rotor length.

**#21 — ASK WHO ELSE HAS THIS SHAPE.** Pseudorandomness suggested asking only for low-order cylinder uniformity. Finite-field character-sum technology then supplied the needed uniform fixed-`k` discrepancy bound through Vandermonde + Weil + interval Fourier norms.

**#30 — ONE PRIME, ONE SCALE, ONE DIRECTION AT A TIME.** Embedded `[N]` into the single nearest prime field `F_p`, proved the estimate for one fixed finite restriction `k`, averaged one harmonic scale at a time, and only then glued the restrictions projectively. This avoided constructing an all-orders finite design.

The next nonrepeating method triple is **#3, #7, #22**. These are the three section-B methods not used in the recent R11 method ledger: prove something stronger, take the limit, and read the failures. A high-value next target is to ask whether the activation coins can also be derandomized—e.g. by a deterministic rare-event schedule with one random global phase—and to identify from the literature exactly where deterministic-clock approximations of independent exponential fragmentation fail. That would test whether one can push C032 from a deterministic environment with stochastic activations to an almost fully deterministic finite tree model without losing the CTCS exponential holding-time structure.

---

```yaml
ledger_delta:
  track: R11
  intake: I0054
  source: "Aldous--Janson, arXiv:2303.02529v3, Open Problem 18"
  lane: CLOSABLE_OUTSIDE
  metric_name: "number of distinct nontrivial discrete model classes with complete author-side full CTCS(infinity) limit proofs under frozen equivalence"
  before: 31
  after: 32
  movement: +1
  new_claim: R11-I0054-C032
  new_class: "explicit polynomial-character finite-field rotor"
  convergence: "every fixed finite restriction in Skorokhod J1; projective exchangeable-partition limit CTCS(infinity)"
  finite_environment_size: "p_N(p_N-1)=O(N^2)"
  exact_checker_status: PASS_SELF_CHECK
  exact_checker_checks: 85218
  source_status: PARTIAL
  campaign_closure: false
  canonical_claim_status: "PENDING_ADMISSION, not READY"
  p26_end_to_end_audit: missing
  second_other_track_audit: missing
  novelty_status: UNVERIFIED
  stagnation_after: 0
  methods_used: [10, 21, 30]
  next_methods: [3, 7, 22]
```
