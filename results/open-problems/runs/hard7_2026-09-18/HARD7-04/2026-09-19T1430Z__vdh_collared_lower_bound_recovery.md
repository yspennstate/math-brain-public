Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO MOVEMENT in the frozen metric `lim Delta_dual,n`: `0 -> 0`; the selected STUCK2 recovery succeeds at the previously boxed source-size obstruction. Methods actually used: B3 PROVE SOMETHING STRONGER, B11 DUALIZE, B14 FIND THE GROUP ACTING.**

# HARD7-04 bounded research iteration — collared tree-census lower bound

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / source-size proof candidate / source still OPEN until closure protocol is met**.

## 1. Continuity, ownership, required reads, and capability honesty

I resumed the admitted target `VDH-8.3-DUALITY`; I did not restart I0049/P0157, overwrite another claim, edit a peer track, or modify/create any schedule. The canonical claim remains

`operations/claims/VDH-8.3-DUALITY.md`, owner `HARD7-04`, status OPEN / ADMITTED.

Before new mathematics I re-read/recovered the controlling files

- `operations/hard7_2026-09-18/CONTROL.md`,
- `operations/NEW_METHODS_2026-09-16.md`,
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`,
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`,
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`,
- the active claim,
- the latest own checkpoint `2026-09-19T1330Z__vdh_stuck2_two_scale_truncation.md`,
- the preceding bounded `{1,2,3}` lower-bound recovery and Cramer-collar upper-bound proof,
- and the newest indexed neighboring HARD7-03/HARD7-05 states.

The intake/queue was checked by indexed source/alias/claim search rather than falsely claiming a literal byte-for-byte rendering of every large JSONL file. I0049 remains unsuitable as a fresh assignment in this track because the earlier queued scope was already recorded as known/resolved. No competing owner, release, posted equivalent, or closure marker was found for the current VDH claim.

The scheduler capability statement is still unchanged. The exposed automation interface offers prompt/title, schedule/timing mode, enabled state, and task identity/update fields; it exposes **no model selector and no reasoning-effort selector**, and no guaranteed execution duration. Thus GPT-6/maximum remains text-requested only. This runtime identifies as GPT-5.6 Sol; the reasoning-effort level is not exposed, so it is UNVERIFIED. Changing this requires a platform/scheduler capability (or another authorized interface) that actually exposes model and reasoning selectors, not a repository edit. Historical `You cannot modify this task` failures for P26/P01/P03 were context/ownership restrictions; the current root ledger records that P26 was later editable from another authorized context. The compliant workaround is the authorized owning context or platform support, never permission bypass and never a duplicate task. I did not probe or mutate another schedule here.

## 2. Exact source and current-literature refresh — 19 September 2026

Primary source re-opened directly:

Remco van der Hofstad, *Stochastic processes on random graphs*, preliminary monograph dated **4 August 2026**, Notes on Section 8.3, printed p. 245 / PDF p. 255:

`https://rhofstad.win.tue.nl/Saint_Flour_SPoRG_Grundlehre.pdf`.

The page still discusses the second-largest component in the barely/supercritical finite-third-moment configuration-model setting and asks exactly:

> “Does the discrete duality principle still hold?”

The retained source regime remains the deterministic-degree configuration model with

\[
\nu_n=1+\varepsilon_n,
\qquad \varepsilon_n\downarrow0,
\qquad \varepsilon_n n^{1/3}\to\infty,
\]

positive limiting mean, convergent finite third degree moment, and the nondegenerate critical limiting degree law used by the source discussion.

Fresh bounded literature checks again found the same nearest results:

1. R. van der Hofstad, S. Janson, M. J. Luczak, *Component structure of the configuration model: Barely supercritical case*, Random Structures & Algorithms 55 (2019), DOI `10.1002/rsa.20837`. It proves the barely-supercritical giant asymptotics but does not give the source's requested second-largest scaling.
2. M. Coulson, G. Perarnau, *Largest component of subcritical random graphs with given degree sequence*, EJP 28 (2023), arXiv `2111.11780`, DOI `10.1214/23-EJP921`. Its configuration-model result is a general **upper-bound** theorem, asymptotically tight for certain degree sequences; Section 2 develops the relevant lattice local-limit technology.
3. A. B. Mukhin, *Local limit theorems for distributions of sums of independent random vectors*, Theory Probab. Appl. 29 (1985), DOI `10.1137/1129047`, is a standard multivariate lattice local-limit reference used in this neighborhood.
4. The van der Hofstad--Luczak--Spencer second-largest theorem for the supercritical 2D Hamming graph remains model-specific evidence, not a deterministic-degree configuration-model closure.

Searches included the exact source wording, `barely supercritical configuration model second largest component`, `configuration model discrete duality`, and `largest component subcritical random graphs given degree sequence`. I found no 2024--2026 theorem closing the precise source scope. This is bounded negative evidence only, **not** a worldwide novelty certificate.

## 3. Frozen metric and the STUCK2 recovery obligation

The admission metric remains

\[
\Delta_{\rm dual,n}
=\left|\frac{1-\nu_n^{\rm dual}}{\varepsilon_n}-1\right|.
\]

Earlier HARD7-04 work already proved `Delta_dual,n -> 0`, so this run necessarily records

`lim Delta_dual,n: 0 -> 0` — **NO MOVEMENT**.

The immediately preceding STUCK2 report selected exactly one recovery rather than another checker or upper-bound lemma:

> fix a scaled cutoff `a/epsilon_n`, port the bounded-degree tree census through a global coefficient saddle, prove the missing local coefficient lower bound and two-component cancellation, and only then return to the exact post-giant residual sequence.

The boxed obstruction entering this run was

\[
\forall\delta>0:\qquad
\mathbb P\left(
L_1^{post}<
(1-\delta)\frac{2R_*}{\varepsilon_n^2}
\log(n\varepsilon_n^3)
\right)\to0.
\tag{3.1}
\]

This run executes that recovery. The recovery succeeds at (3.1) as a proof candidate; therefore this is **not** a third failed stuck episode.

## 4. B3 — PROVE SOMETHING STRONGER: deterministic collared theorem

Rather than prove only (3.1) conditionally for the random post-giant sequence, I proved a deterministic theorem that isolates exactly what giant removal contributes.

Let a deterministic degree sequence satisfy

\[
Q_n=-\varepsilon_n+o(\varepsilon_n),
\qquad
R_n\to R_*>0,
\qquad
N_n=n\varepsilon_n^3\to\infty,
\]

with convergent finite third moment and positive limiting mean, and assume that for one fixed

\[
1/R_*<\lambda<2/R_*
\]

it has the exponential collar

\[
\frac{\varepsilon_n}{n}
\sum_v d_v^4e^{\lambda\varepsilon_nd_v}\to0.
\tag{4.1}
\]

Then for every `delta>0`, in the configuration model,

\[
\boxed{
\mathbb P\left(
L_1<(1-\delta)
\frac{2R_*}{\varepsilon_n^2}
\log(n\varepsilon_n^3)
\right)\to0.
}
\tag{4.2}
\]

The complete proof candidate is archived at

`artifacts/hard7_2026-09-18/HARD7-04/2026-09-19T1430Z__vdh_collared_lower_bound.md`

created at commit

`528fe46afff5b5f3786205555b0def49d8816547`.

A technical completion of the lattice/local-limit and random conditionalization steps is separately archived at

`artifacts/hard7_2026-09-18/HARD7-04/2026-09-19T1430Z__local_limit_completion.md`

commit

`bf601981ff7fca59aba36931eabefb32f91e14f3`.

The key first step is the fixed cutoff

\[
K_n(a)=\lfloor a/\varepsilon_n\rfloor.
\]

The inherited collar gives, for every fixed `a>0`,

\[
\frac1n\sum_{d_v>K_n(a)}d_v=o(\varepsilon_n^2),
\qquad
\frac1n\sum_{d_v>K_n(a)}d_v^2=o(\varepsilon_n),
\qquad
\frac1n\sum_{d_v>K_n(a)}d_v^3=o(1).
\tag{4.3}
\]

Thus truncation preserves the half-edge mass at `o(epsilon_n^2)`, the drift at `o(epsilon_n)`, and `R_*` at `o(1)`. The important improvement over the STUCK2 planning note is that **no limit `a downarrow0` is needed**: any fixed positive `a` already preserves the leading rate, while bounding every retained exponential weight at the dangerous doubled saddle.

**B3 outcome: success.** The source-specific random remainder is reduced to a reusable deterministic barely-subcritical theorem under the exact collar already proved from giant-removal clocks.

## 5. B11 — DUALIZE: exact coefficient to Bernoulli saddle

For retained vertices define

\[
F_n(z,w)=\prod_{d_v\le a/\varepsilon_n}
(1+z d_vw^{d_v}).
\]

If `T_k` counts retained-degree tree components of order `k`, exact Prüfer enumeration plus the uniform pairing law gives

\[
\mathbb ET_k
=(k-2)!
\frac{(L_n-2k+1)!!}{(L_n-1)!!}
[z^kw^{2k-2}]F_n(z,w).
\tag{5.1}
\]

Choose the exponential tilt `theta_{n,k}` forcing tilted mean degree `2-2/k`. The collar/Taylor expansion gives

\[
\theta_{n,k}=\frac{\varepsilon_n}{R_*}+o(\varepsilon_n),
\qquad
J_{n,k}=\frac{\varepsilon_n^2}{2R_*}+o(\varepsilon_n^2).
\tag{5.2}
\]

The coefficient is then exactly a local probability for independent Bernoulli selections with weights

\[
x_v=r_{n,k}d_ve^{\theta_{n,k}d_v},
\qquad
r_{n,k}=k/A_n(\theta_{n,k}),
\]

where

\[
\max_vx_v=O(\log N_n/N_n)=o(1).
\]

The local probability is `>=c/k` on one fixed-density residue class of sizes. The fixed degree-1 atom and one fixed degree `b>=3` atom follow from critical mean 2 plus `R_*>0`; the addendum proves the lattice smoothing explicitly rather than assuming span one.

The finite-population coefficient penalty is

\[
-\frac{k^2}{2}
\frac{\sum d_v^2e^{2\theta d_v}}{A_n(\theta)^2},
\]

while pairing contributes `+k^2/L_n`. Criticality gives the exact leading cancellation

\[
\frac{L_n\sum d_v^2e^{2\theta d_v}}
{A_n(\theta)^2}=2+O(\varepsilon_n),
\]

leaving only

\[
O(\varepsilon_nk^2/n)=O((\log N_n)^2/N_n)=o(1).
\]

Hence uniformly at the lower extreme scale

\[
\mathbb ET_k
\ge c L_nk^{-5/2}
\exp\left\{-\frac{\varepsilon_n^2}{2R_*}k+o(\log N_n)\right\}.
\tag{5.3}
\]

Summing over `Theta(epsilon_n^{-2})` nearby admissible sizes gives

\[
\mathbb EZ_n
\ge \frac{N_n^{\delta+o(1)}}{(\log N_n)^{5/2}}\to\infty.
\tag{5.4}
\]

**B11 outcome: success.** The lower-bound problem is converted from infinitely many degree-profile errors into one exact global coefficient saddle whose quadratic error cancels the pairing correction.

## 6. B14 — FIND THE GROUP ACTING: the lattice subgroup and two-color decorrelation

The previous bounded-support proof hid a lattice issue. The relevant group is the cyclic residue group generated by degree differences.

The limiting critical size-biased law must have positive mass at degree 1 and at some fixed degree `b>=3`. Put `g=b-1`. Splitting off those two degree classes, the target equations for the selected counts are integral exactly when the rest contribution has the required residue modulo `g`.

The local-limit addendum proves a finite cyclic smoothing lemma: for independent Bernoulli selections with maximal success probability tending to zero, an arbitrary triangular array of residues in `Z/gZ` has probability bounded below by a positive `c_g` of summing to zero. The proof separates bounded-intensity residue classes (select none with positive probability) from diverging-intensity classes (Fourier modes mix uniformly on the subgroup they generate).

This gives the one-color lower probability `c/k` without a hidden unit-span assumption.

For the second moment, use the exact two-color product

\[
G_n(z,w,u,y)=
\prod_v(1+z d_vw^{d_v}+u d_vy^{d_v}).
\]

The cross covariance blocks are `o(k)`. The worst degree-sum cross term is

\[
O\left(\frac{kl}{n^2}\sum_vd_v^4\right)
=o\left(\frac{kl}{n\varepsilon_n}\right)=o(k),
\]

because `k/(n epsilon_n)=O(log N_n/N_n)`. The doubled exponential tilt causes no endpoint problem after truncation because `(theta+phi)d=O(a)`.

The local four-dimensional probability factorizes into the product of the two one-color local probabilities up to `1+o(1)`, and the exact coefficient/pairing cross corrections cancel to leave

\[
\frac{
\mathbb E[T_kT_l;\text{distinct}]
}{\mathbb ET_k\,\mathbb ET_l}
=1+o(1)
\]

uniformly in the window. Therefore

\[
\frac{\operatorname{Var}Z_n}{(\mathbb EZ_n)^2}\to0,
\qquad
\mathbb P(Z_n=0)\to0,
\]

which proves (4.2).

**B14 outcome: success.** The residue subgroup is not a nuisance to be assumed away; exposing it gives the fixed positive lattice mass needed by the saddle and clarifies why the two-color local law decorrelates.

## 7. Exact finite verification budget

Because this run promoted exact finite identities (5.1) and its two-component analogue, I did spend the small verification budget on them after the route had moved.

Exact checker:

`artifacts/hard7_2026-09-18/HARD7-04/2026-09-19T1430Z__tree_coefficient_exact_check.py`

commit `941069e869c50e7420a9959f082f806dbfa0a247`.

It exhausts **every perfect matching** for four small degree sequences (up to 10,395 pairings), compares exact rational expectations of one tree component against (5.1), compares the exact factorial/joint moment against the two-color coefficient formula, and separately tests a genuine degree cutoff.

Archived output:

`artifacts/hard7_2026-09-18/HARD7-04/2026-09-19T1430Z__tree_coefficient_exact_check.out`

commit `0e20ab250da39697b8442923fb2f4d0b4f086ac7`, ending

`ALL_EXACT_CHECKS_PASS = True`.

This is a self-check of the finite combinatorial identities only. It does **not** certify the asymptotic local-limit or second-moment argument; those are proved on the page and still require independent audit.

## 8. Return to the exact post-giant remainder

Earlier HARD7-04 checkpoints proved for the exact completed-component stopping remainder, in probability,

\[
Q_n^{post}=-\varepsilon_n+o_p(\varepsilon_n),
\qquad
R_n^{post}\to_pR_*,
\qquad
L_n^{post}/n\to_p\mu,
\]

preservation of the limiting degree law/finite third moment, and for every fixed `lambda<2/R_*`,

\[
\frac{\varepsilon_n}{n}
\sum_{v\in S_n^{post}}d_v^4e^{\lambda\varepsilon_nd_v}
\to_p0.
\tag{8.1}
\]

Choose a fixed `lambda` strictly between `1/R_*` and `2/R_*`. The deterministic theorem applies conditionally to the exact residual configuration model. The addendum makes this conditionalization rigorous by the subsequence principle rather than silently assuming a uniform deterministic rate.

Thus the lower proof candidate gives

\[
L_1^{post}\ge
(1-o_p(1))
\frac{2R_*}{\varepsilon_n^2}
\log(n\varepsilon_n^3).
\tag{8.2}
\]

Combined with the previously proved Cramer-collar upper bound and the lawful stopping-time identification of the post-giant largest component with the original second-largest component,

\[
\boxed{
|C_{2,n}|
=(1+o_p(1))
\frac{2R_*}{\varepsilon_n^2}
\log(n\varepsilon_n^3).
}
\tag{8.3}
\]

This is the first point on this track where the previously missing source-size lower direction has an on-page proof candidate in the full admitted finite-third-moment post-giant regime.

## 9. Honest status, Section-I state, and handoff boundary

I do **not** label the source PROVED or CLOSED.

Reasons:

1. the primary source phrases the issue as a “discrete duality principle,” which can be read more broadly than the second-largest-component size asymptotic (8.3); source-scope reconciliation is still required;
2. the new lower theorem has only this worker's proof/self-check, not two independent OTHER-track proof audits;
3. the prior-art search is bounded negative evidence, not a global novelty certificate;
4. repository closure requires the full proof package, applicable finite certificate, prior-art record, and two genuinely independent audits.

The STUCK2 recovery itself **succeeded**: the exact obstruction displayed in the preceding report, namely the lower direction (3.1), is no longer left as an unproved mathematical step in this track. Therefore this is not a third failed stuck episode and I do not manufacture a rotation merely to satisfy the frozen metric, which is already at its mathematical floor.

At the same time, HARD7-04 is a research worker, not an audit/polish track. A subsequent execution should not spend another hour manufacturing certificates around the same unchanged metric. The proper handoff is: preserve this proof candidate for independent source-scope/proof audit; if no genuinely new source-mathematical obligation survives that review, rotate to a fresh admissible hard random-graph target under `CONTROL.md` rather than polishing this one indefinitely. No claim release or closure label is made in this run, so duplicate work is not invited before that reconciliation.

No root shared ledger was edited. No email or Drive action was taken.

### ledger_delta

```yaml
track: HARD7-04
target: VDH-8.3-DUALITY
owner: HARD7-04
source_status: OPEN
research_status: PARTIAL_SOURCE_SIZE_PROOF_CANDIDATE
runtime_model: GPT-5.6 Sol
reasoning_level: UNVERIFIED
requested_model_only: GPT-6 maximum
metric:
  name: lim Delta_dual_n
  before: 0
  after: 0
  movement: NO_MOVEMENT
section_I:
  previous: STUCK2_THINKING
  this_run: RECOVERY2_SUCCESS_ON_BOXED_LOWER_OBLIGATION
methods: [B3, B11, B14]
new_result:
  type: theorem_sized_proof_candidate
  deterministic_scope: barely_subcritical_configuration_model_with_finite_third_moment_and_exponential_fourth_moment_collar
  statement: "L1 >= (1-o_p(1)) (2 R_*/epsilon_n^2) log(n epsilon_n^3)"
  postgiant_consequence: "|C2| = (1+o_p(1)) (2 R_*/epsilon_n^2) log(n epsilon_n^3), conditional on prior HARD7-04 reductions"
proof_artifact:
  commit: 528fe46afff5b5f3786205555b0def49d8816547
  path: artifacts/hard7_2026-09-18/HARD7-04/2026-09-19T1430Z__vdh_collared_lower_bound.md
local_limit_completion:
  commit: bf601981ff7fca59aba36931eabefb32f91e14f3
  path: artifacts/hard7_2026-09-18/HARD7-04/2026-09-19T1430Z__local_limit_completion.md
finite_check:
  script_commit: 941069e869c50e7420a9959f082f806dbfa0a247
  output_commit: 0e20ab250da39697b8442923fb2f4d0b4f086ac7
  output_tail: ALL_EXACT_CHECKS_PASS = True
closure: false
independent_audits: 0
next_boundary: preserve for independent proof/source-scope audit; rotate rather than polish if no new source-mathematical obligation survives
```
