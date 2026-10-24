Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO MOVEMENT in the frozen metric `lim Delta_dual,n`: `0 -> 0`; Section-I recovery succeeded on the prescribed simplest special case; methods actually used: B4 PROVE SOMETHING WEAKER COMPLETELY, B12 FIND WHAT IS CONSERVED, B25 COUNT THE SAME THING TWICE.**

# HARD7-04 bounded research iteration — exact tree-census lower bound in the bounded three-point subcase

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / source OPEN / STUCK1 recovery completed.**

## 1. Continuity, ownership, required reads, and capability honesty

I resumed the admitted target `VDH-8.3-DUALITY`; I did not restart admission, return to I0049/P0157, or change another schedule. The exclusive claim remains `operations/claims/VDH-8.3-DUALITY.md`, owned by `HARD7-04`.

The primary source remains Remco van der Hofstad, *Stochastic processes on random graphs*, preliminary monograph dated 4 August 2026, Notes on Section 8.3, printed p. 245 / PDF p. 255, where the finite-third-moment barely-supercritical configuration-model discussion asks: **“Does the discrete duality principle still hold?”**

Before doing new mathematics I re-read/recovered the controlling files `operations/hard7_2026-09-18/CONTROL.md`, `operations/NEW_METHODS_2026-09-16.md`, and `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; the active claim; the latest own checkpoint `2026-09-19T1130Z__vdh_stuck1_tree_count_port.md`; the preceding sharp-upper report; and the newest indexed neighboring HARD7-03/HARD7-05 reports. I also checked the intake/queue state through repository search rather than pretending to render every large JSONL byte-for-byte. No competing claim, release, posting, or source-resolution record for `VDH-8.3-DUALITY` was found.

The scheduler/runtime capability statement remains unchanged: the exposed scheduler schema has no model selector or reasoning-effort selector. GPT-6/maximum is prompt-requested only. This runtime identifies as GPT-5.6 Sol; reasoning level is not exposed and is therefore UNVERIFIED. The historical `You cannot modify this task` failures are ownership/context restrictions; the compliant workaround remains using an authorized owning context or platform support, never bypassing the restriction or duplicating a task. I did not probe or mutate any other schedule in this run.

## 2. Fresh source/current-literature check — 19 September 2026

I refreshed the exact-source/literature searches around `barely supercritical configuration model second largest component`, `configuration model discrete duality`, and `largest subcritical component given degree sequence`.

The directly relevant literature still has the same division of labor:

- van der Hofstad--Janson--Luczak (Random Structures & Algorithms, 2019) gives precise barely-supercritical giant-component asymptotics but does not determine the source's requested second-largest component;
- Coulson--Perarnau, *Largest component of subcritical random graphs with given degree sequence*, Electronic Journal of Probability 28 (2023), arXiv:2111.11780, gives general configuration-model **upper bounds**, asymptotically tight for certain degree sequences, but not the uniform matching lower theorem needed here;
- Hatami--Molloy (2012) locates the scaling window/order for given degree sequences, not the sharp barely-subcritical logarithmic lower constant used below;
- the van der Hofstad--Luczak--Spencer 2D Hamming-graph result is model-specific evidence for discrete duality, not a theorem for the deterministic-degree configuration model.

A bounded search on 19 September 2026 found no later paper closing the exact source scope, and no hit giving the specific bounded `{1,2,3}` tree-census theorem below. This is bounded negative evidence only, not a worldwide novelty certificate.

## 3. Frozen metric and Section-I recovery choice

The frozen admission metric remains

\[
\Delta_{\rm dual,n}
=\left|\frac{1-\nu_n^{\rm dual}}{\varepsilon_n}-1\right|.
\]

Earlier runs proved `Delta_dual,n -> 0`, so the metric is already at its mathematical floor. This run therefore records honestly

`lim Delta_dual,n: 0 -> 0` — **NO MOVEMENT**.

The preceding STUCK1 report chose exactly one recovery action: **port the Erdős--Rényi tree-component census / second-moment mechanism to the simplest bounded-degree configuration-model special case**. This run executes that recovery instead of generating another upper-bound lemma.

The special case singled out in that report has degrees in `{1,2,3}` with limiting proportions

\[
(p_1,p_2,p_3)=\left(\frac38,\frac12,\frac18\right),
\]

critical mean `mu_*=7/4`, and

\[
R_* = \frac{\mathbb E[D(D-2)^2]}{\mathbb ED}=\frac37.
\]

For deterministic triangular arrays with

\[
Q_n=\frac{-n_1+3n_3}{L_n}=-\varepsilon_n<0,
\qquad
\varepsilon_n\downarrow0,
\qquad
N_n=n\varepsilon_n^3\to\infty,
\]

the new theorem is

\[
\boxed{
\forall\delta>0:\quad
\mathbb P\!\left(
L_1<(1-\delta)\frac{6}{7\varepsilon_n^2}\log(n\varepsilon_n^3)
\right)\to0.
}
\tag{3.1}
\]

This is the exact lower leading constant in the simplest subcritical special case. It is **PARTIAL**, not a solution of the full post-giant finite-third-moment source question.

The complete proof is archived at

`artifacts/hard7_2026-09-18/HARD7-04/2026-09-19T1230Z__vdh_bounded_threepoint_lower_bound.md`

created at commit `ec3c0092d94e5e598d1b07b64c5296e5cab6969b`.

## 4. B4 — PROVE SOMETHING WEAKER, COMPLETELY

The previous blocker was not the Cramér rate; it was existence/decorrelation below the extremal threshold. I therefore froze the cleanest nontrivial source-relevant subcase instead of weakening the constant.

If a tree component of order `k` contains `a,b,c` vertices of degrees `1,2,3`, then the degree sum identity forces

\[
a=c+2,\qquad b=k-2c-2.
\]

Let `X_{k,c}` count such tree components. Exact Prüfer/tree pairing enumeration gives

\[
\mathbb E X_{k,c}
=\binom{n_1}{c+2}
 \binom{n_2}{k-2c-2}
 \binom{n_3}{c}
 (k-2)!2^{k-2c-2}3^c
 \frac{(L_n-2k+1)!!}{(L_n-1)!!}.
\tag{4.1}
\]

Rewriting (4.1) with the size-biased probabilities `q_{r,n}=r n_r/L_n` turns the tree census into a local large-deviation probability for `k` iid size-biased degrees conditioned to sum to `2k-2`, multiplied by an explicit finite-population correction.

Exponential tilting to mean degree `2` yields

\[
I_n=\frac{\varepsilon_n^2}{2R_*}+o(\varepsilon_n^2).
\]

A uniform finite-support local CLT on the tilted three-atom law gives, after restricting to `O(sqrt(k))`-typical profiles,

\[
\mathbb E T_k\ge c n k^{-5/2}e^{-I_n k}.
\tag{4.2}
\]

Summing over a size window of width `J_n=floor(epsilon_n^{-2})` beginning at

\[
K_n=(1-\delta)\frac{2R_*}{\varepsilon_n^2}\log N_n
\]

produces

\[
\mathbb E Z_n
\ge \frac{N_n^{\delta+o(1)}}{(\log N_n)^{5/2}}\to\infty.
\tag{4.3}
\]

The window is essential: using one exact size loses the factor that compensates the `epsilon_n^2` prefactor in the most slowly barely-subcritical regimes.

**B4 outcome: success.** The simplest special case from the STUCK1 obstruction report is now proved with the sharp lower leading constant.

## 5. B12 — FIND WHAT IS CONSERVED

The proof hinges on a cancellation hidden in two conservation laws.

First, a tree has total degree `2(k-1)`, which is exactly the profile constraint `n_1(tree)=n_3(tree)+2`.

Second, at criticality the size-biased law `q_r=r p_r/mu` has mean degree `2`. Therefore

\[
\sum_r\frac{q_r^2}{p_r}
=\frac{\mathbb E D^2}{\mu^2}
=\frac2\mu.
\tag{5.1}
\]

For the present law,

\[
\mu=\frac74,
\quad
q=\left(\frac3{14},\frac47,\frac3{14}\right),
\quad
\sum_r q_r^2/p_r=\frac87=\frac2\mu.
\]

This identity cancels the leading `k^2/n` finite-population penalty in the first moment. Away from criticality by `Q_n=-epsilon_n`, the residual coefficient is only `O(epsilon_n)`, so at the target scale

\[
\varepsilon_n k^2/n
=O((\log N_n)^2/N_n)=o(1).
\]

Exactly the same invariant cancels the leading `k ell/n` term in the two-component correlation ratio.

**B12 outcome: success.** The obstruction was not arbitrary dependence: criticality itself supplies the cancellation needed to keep the finite-population census asymptotically Erdős--Rényi-like on the logarithmic extreme scale.

## 6. B25 — COUNT THE SAME THING TWICE

For two prescribed good tree profiles `m,m'` of sizes `k,ell`, the exact ratio of the joint disjoint-component expectation to the product of the one-component expectations factorizes into a vertex-sampling term and a pairing term:

\[
V_n(m,m')
=\prod_{r=1}^3
\frac{(n_r)_{m_r+m'_r}}{(n_r)_{m_r}(n_r)_{m'_r}},
\]

\[
P_n(k,\ell)
=\frac{(L_n-2k-2\ell+3)!!(L_n-1)!!}
{(L_n-2k+1)!!(L_n-2\ell+1)!!}.
\]

The logarithm is

\[
\log(V_nP_n)
=\frac{k\ell}{n}
\left[
\frac2{\mu_n}-\sum_r\frac{\alpha_{r,n}^2}{p_{r,n}}
\right]
+o(1),
\]

uniformly in the good window. By the conserved critical identity above, the bracket is `O(epsilon_n)`, while profile fluctuations contribute only `O((log N_n)^{3/2}/N_n)` and cubic finite-population terms only `O((log N_n)^3/N_n^2)`. Hence

\[
V_nP_n=1+o(1)
\]

uniformly. Summation gives

\[
\mathbb E[Z_n(Z_n-1)]\le(1+o(1))(\mathbb E Z_n)^2,
\]

so `Var(Z_n)/(E Z_n)^2 -> 0` and `P(Z_n=0)->0`. This proves (3.1).

**B25 outcome: success.** The Erdős--Rényi second-moment mechanism ports because the two exact counts reveal the same critical cancellation in both first and second moments.

## 7. Exact finite sanity check

The exact checker

`artifacts/hard7_2026-09-18/HARD7-04/2026-09-19T1230Z__tree_census_exact_check.py`

was created at commit `fbfaa8d30be2e62d333039d3964da745e3c9dfa3`. It brute-forces every pairing in four small `{1,2,3}` degree sequences and matches (4.1) exactly. It also verifies the critical rational cancellation `8/7=2/(7/4)`.

Archived output:

`artifacts/hard7_2026-09-18/HARD7-04/2026-09-19T1230Z__tree_census_exact_check.out`

commit `0962846d3d618ec011daef83f3be616d50f4a851`, ending

`ALL_EXACT_CHECKS_PASS = True`.

This checker is a sanity check for the exact finite identities; the asymptotic theorem is proved on the page and is not certified merely by finite enumeration.

## 8. Remaining source obligation and next Section-I state

The full source obligation remains the matching lower bound for the **actual random post-giant residual degree sequence** under only the finite-third-moment source assumptions:

\[
\forall\delta>0:\quad
\mathbb P\!\left(
L_1^{post}<
(1-\delta)\frac{2R_*}{\varepsilon_n^2}\log(n\varepsilon_n^3)
\right)\to0.
\]

What changed is the blocker. The abundance/decorrelation mechanism itself is no longer missing in the bounded-support model. The remaining issue is now **uniform truncation of the exact tree census/local lower estimate and the two-component cancellation when the post-giant residual maximum degree may be as large as `O(epsilon_n^{-1} log N_n)` under the sharp exponential collar**.

The frozen metric nevertheless remains at `0`, so under the literal Section-I rule this track is still stagnant in its fixed metric. The next HARD7-04 run should therefore be treated as **STUCK2 thinking/recovery** unless an owner/platform instruction supersedes it: record the narrowed obstruction and choose one recovery, with the natural candidate being to port the bounded-support census through a growing cutoff and prove that the discarded high-degree mass changes both Cramér/local-CLT and second-moment coefficients only by `o(1)`.

No closure, paper package, or audit request is made.

### ledger_delta

```yaml
track: HARD7-04
target: VDH-8.3-DUALITY
owner: HARD7-04
source_status: OPEN
research_status: PARTIAL
section_I:
  previous: STUCK1
  this_run: RECOVERY1_SUCCESS_ON_SIMPLEST_SPECIAL_CASE
  next_if_no_owner_override: STUCK2_THINKING
metric:
  name: Delta_dual_n = abs((1-nu_dual_n)/epsilon_n - 1)
  before_this_run: asymptotic_limit_0
  after_this_run: asymptotic_limit_0
  movement: NO_MOVEMENT
methods: [B4, B12, B25]
new_result:
  type: theorem_sized_partial
  scope: deterministic barely-subcritical configuration models with degrees in {1,2,3} and limiting law (3/8,1/2,1/8)
  statement: "L1 >= (1-o_p(1)) (6/(7 epsilon_n^2)) log(n epsilon_n^3)"
  proof_artifact: artifacts/hard7_2026-09-18/HARD7-04/2026-09-19T1230Z__vdh_bounded_threepoint_lower_bound.md
finite_check:
  script_commit: fbfaa8d30be2e62d333039d3964da745e3c9dfa3
  output_commit: 0962846d3d618ec011daef83f3be616d50f4a851
  output_tail: ALL_EXACT_CHECKS_PASS = True
closure: false
audits_requested: 0
```
