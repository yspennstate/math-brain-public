Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO MOVEMENT in the frozen metric `lim Delta_dual,n`: `0 -> 0`; methods actually used: B6 DEFORM TO A POINT YOU CAN SOLVE, B20 FIND WHY THE ALGORITHM FAILS, B25 COUNT THE SAME THING TWICE. Source status: PARTIAL / OPEN.**

# HARD7-04 bounded research iteration — Cramér-collar sharp upper bound

Repository / branch: private `yspennstate/math-open-problems` / `master`.

## 1. Continuity, ownership and required state

I resumed the admitted target rather than restarting admission or returning to I0049/P0157. The exclusive claim remains

`operations/claims/VDH-8.3-DUALITY.md`,

owned by `HARD7-04`, status OPEN / ADMITTED.

The primary source remains Remco van der Hofstad, *Stochastic processes on random graphs*, preliminary monograph dated **4 August 2026**, Notes on Section 8.3, printed p. 245 / PDF p. 255:

`https://rhofstad.win.tue.nl/Saint_Flour_SPoRG_Grundlehre.pdf`.

The source asks, after noting that high-degree vertices should be swallowed by the unique giant and that the second-largest component is expected to look Erdős--Rényi-like:

> “Does the discrete duality principle still hold?”

The retained scope is the deterministic-degree configuration model with

\[
\nu_n=1+\varepsilon_n,\qquad
\varepsilon_n\downarrow0,\qquad
\varepsilon_n n^{1/3}\to\infty,
\]

finite convergent third degree moment, positive limiting mean, and the source's nondegenerate critical limiting degree law.

The frozen admission metric remains

\[
\Delta_{\rm dual,n}:=
\left|\frac{1-\nu_n^{\rm dual}}{\varepsilon_n}-1\right|.
\]

Its admission baseline was `UNMEASURED`; earlier runs proved its asymptotic limit is zero and lifted the drift reflection to the exact post-giant remainder. Thus this run begins at the metric's floor and cannot honestly move it below zero.

Before new mathematics I reread/recovered the controlling files `operations/hard7_2026-09-18/CONTROL.md`, `operations/NEW_METHODS_2026-09-16.md`, and `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; the active claim; the complete indexed HARD7-04 checkpoint chain through `2026-09-19T0938Z__vdh_sharp_hub_stripping.md`; targeted intake/alias records around I0049 and the active claim; and newest visible neighboring HARD7-03/HARD7-05 reports. The intake collections are too large to render literally in one connector response, so I used indexed/source/claim searches rather than falsely claiming a byte-for-byte dump. No canonical ownership collision, release, posted equivalent, or source-resolution record was found for `VDH-8.3-DUALITY`.

## 2. Fresh source and current-literature check — 19 September 2026

The 4 August 2026 source PDF was re-opened directly. Its Notes on Section 8.3 still state that the work with Janson and Luczak does not determine the supercritical second-largest component and explicitly ask the discrete-duality question.

I also refreshed bounded searches for the exact source wording, `barely supercritical second largest configuration model`, and `configuration model discrete duality`. The directly relevant sharp subcritical paper remains:

- Matthew Coulson and Guillem Perarnau, *Largest component of subcritical random graphs with given degree sequence*, Electronic Journal of Probability 28 (2023), DOI `10.1214/23-EJP921`, arXiv `2111.11780`.

The older van der Hofstad--Luczak--Spencer 2D Hamming-graph theorem is model-specific evidence for discrete duality, not a solution of the deterministic-degree configuration-model question. The bounded 19 September search found no later theorem closing the exact source scope. This is **bounded negative evidence only**, not a worldwide novelty certificate.

## 3. Previous checkpoint

The two immediately preceding VDH checkpoints established:

1. the sleeping remainder at a lawful completed-component stopping boundary is an **exact configuration model** on its random residual degree sequence;
2. w.h.p. its largest component is the original graph's `C_{2,n}`;
3. its criticality satisfies
   \[
   Q_n^{post}=-\varepsilon_n+o_p(\varepsilon_n),
   \qquad
   R_n^{post}\to_p R_*:=\frac{\mathbb E[D(D-2)^2]}{\mathbb ED}>0;
   \]
4. the stopping time obeys `tau_n/epsilon_n -> 2/R_*` in probability and sleeping vertices are contained in the independent exponential-clock survivor set;
5. the sharp residual hub cutoff is
   \[
   \frac{\varepsilon_n\Delta_n^{post}}{\log(n\varepsilon_n^3)}
   \le \frac{R_*}{2}+o_p(1),
   \]
   and the constant is source-validly sharp.

The last item showed that the tempting inheritance `Delta |Q|=o(R)` required by the strongest simple Coulson--Perarnau black-box theorem is genuinely false in the full source class. The preceding report therefore nominated the distinct triple **B6/B20/B25**, which is the triple used here.

---

## 4. New mathematics — sharp Erdős--Rényi-scale upper constant

Put

\[
N_n=n\varepsilon_n^3\to\infty.
\]

The substantive result of this run is the following theorem.

### Theorem

For every fixed `delta>0`,

\[
\boxed{
\mathbb P\!\left(
|C_{2,n}|>
(1+\delta)\frac{2R_*}{\varepsilon_n^2}
\log(n\varepsilon_n^3)
\right)\to0.
}
\tag{4.1}
\]

Equivalently, for the largest component `L_1^{post}` of the exact post-giant remainder,

\[
\boxed{
L_1^{post}\le
(1+o_p(1))\frac{2R_*}{\varepsilon_n^2}\log N_n.
}
\tag{4.2}
\]

This is **PARTIAL**, not source closure: the matching lower bound is not proved.

The complete proof is in

`artifacts/hard7_2026-09-18/HARD7-04/2026-09-19T1030Z__vdh_cramer_collar_upper_bound.md`,

created at commit

`021e6d7733b0166de01b4b8929d64d834789c2a6`

and read back successfully at that commit.

### B6 — DEFORM TO A POINT YOU CAN SOLVE

For every fixed `lambda<2/R_*`, the post-giant clock thinning gives the new exponential collar

\[
\boxed{
\frac{\varepsilon_n}{n}
\sum_{v\in S_n^{post}}d_v^4e^{\lambda\varepsilon_n d_v}
\to_p0,
}
\tag{4.3}
\]

and

\[
\frac1n\sum_{v\in S_n^{post}}d_ve^{\lambda\varepsilon_n d_v}=O_p(1).
\tag{4.4}
\]

This is stronger than a raw fourth-moment statement in the direction actually needed: on the shrinking Cramér window `theta=O(epsilon_n)`, it implies a uniform third-derivative remainder for the size-biased increment mgf. Therefore, if `eta_n=\widehat D_n^{post}-2`, its mgf satisfies uniformly on `0<=theta<=lambda epsilon_n`, for any `lambda in (1/R_*,2/R_*)`,

\[
\phi_n'(\theta)=-\varepsilon_n+R_*\theta+o_p(\varepsilon_n),
\]

\[
\phi_n(\theta)=1-\varepsilon_n\theta+\frac{R_*}{2}\theta^2+o_p(\varepsilon_n^2).
\]

Hence its Cramér minimizer and rate are

\[
\theta_n=(1+o_p(1))\frac{\varepsilon_n}{R_*},
\qquad
I_n=(1+o_p(1))\frac{\varepsilon_n^2}{2R_*}.
\tag{4.5}
\]

**B6 outcome: success.** The raw fourth-moment obstruction disappears after deforming to the exponentially collared residual law on the scale actually used by the large-deviation argument.

### B20 — FIND WHY THE ALGORITHM FAILS

The existing exploration route needs a `t^{-1/2}` upper bound on point masses of the exponentially tilted iid exploration walk. General local-CLT hypotheses are awkward here because the post-giant family is triangular and its raw fourth moment need not stay bounded.

The replacement is an elementary two-atom lemma: if an integer-valued variable has two fixed distinct atoms, each with probability at least `c>0`, then for iid copies

\[
\sup_z\mathbb P(Y_1+\cdots+Y_t=z)\le C_c t^{-1/2}.
\tag{4.6}
\]

The proof splits the law into a positive-weight fair two-atom mixture plus a residual law, conditions on the number of mixture draws, and invokes the maximal binomial atom bound.

At criticality, `E[D(D-2)]=0` and `R_*>0`; therefore the limiting degree law has positive mass at degree `1` and at some fixed degree `k>=3`. The post-giant size-biased increment consequently retains fixed atoms at `-1` and `k-2`, and an `O(epsilon_n)` exponential tilt preserves positive lower bounds on them. Thus (4.6) gives the required anti-concentration **without** a fourth-moment local CLT or stable-lattice assumption.

**B20 outcome: success.** The local-CLT obstruction was stronger than necessary; two retained fixed atoms suffice for the upper-tail argument.

### B25 — COUNT THE SAME THING TWICE

For

\[
K_n=\left\lfloor(1+\delta/2)
\frac{2R_*}{\varepsilon_n^2}\log N_n\right\rfloor,
\]

the finite-population exploration through `K_n` pairings is dominated by an iid skip-free walk `beta_n`. If `M_n` is the total residual half-edge count and

\[
A_n=\frac{M_n}{M_n-2K_n+1}=1+o(\varepsilon_n),
\]

define

\[
P(\beta_n=\ell)=A_nP(\eta_n=\ell),\quad\ell\ge0,
\]

\[
P(\beta_n=-1)=A_nP(\eta_n=-1)-(A_n-1).
\]

This is a probability law for large `n`, and it stochastically dominates every actual exploration increment through `K_n`: positive tails can increase by at most the finite-population denominator factor `A_n`, while collision increments are `-2` and only reduce the queue.

Its exact mgf relation is

\[
\phi_{\beta,n}(\theta)
=A_n\phi_n(\theta)-(A_n-1)e^{-\theta},
\]

so it has the same leading Cramér rate

\[
I_{\beta,n}=(1+o_p(1))\frac{\varepsilon_n^2}{2R_*}.
\]

For a walk starting from root degree `s`, the cyclic/Kemperman identity plus the two-atom anti-concentration gives

\[
P(\tau_s\ge K_n)
\le
\frac{Cs e^{\theta_{\beta,n}s}}
{I_{\beta,n}K_n^{3/2}}
 e^{-I_{\beta,n}K_n}.
\tag{4.7}
\]

Now count components larger than `(1+delta)2R_* epsilon_n^{-2} log N_n` first by components and then by their vertices. The `1/K_n` double-count factor and (4.7) yield

\[
E[Z_n\mid d^{post}]
\le
\frac{Ce^{-I_{\beta,n}K_n}}
{I_{\beta,n}K_n^{5/2}}
\sum_{v\in S_n^{post}}d_ve^{\theta_{\beta,n}d_v}.
\]

The exponential collar makes the final sum `O_p(n)`. Since

\[
I_{\beta,n}K_n=(1+\delta/2+o_p(1))\log N_n,
\]

and

\[
\frac{n}{I_{\beta,n}K_n^{5/2}}
=O_p\left(\frac{N_n}{(\log N_n)^{5/2}}\right),
\]

one gets

\[
E[Z_n\mid d^{post}]
=O_p\left(\frac{N_n^{-\delta/3}}{(\log N_n)^{5/2}}\right)\to_p0.
\]

Thus `P(Z_n>0)->0`, proving (4.1).

**B25 outcome: success.** The two counts expose the exact compensating factor `N_n=n epsilon_n^3` and recover the leading upper coefficient `2R_*`.

---

## 5. Remaining obligation and Section-I state

The source is still OPEN on this track. The missing matching direction is

\[
\boxed{
\forall\delta>0:\quad
\mathbb P\!\left(
L_1^{post}<
(1-\delta)\frac{2R_*}{\varepsilon_n^2}\log N_n
\right)\to0.
}
\tag{5.1}
\]

The proof above explains a plausible route but does not fill it. A first-moment abundance calculation below the threshold is insufficient because candidate-root component events overlap strongly. The new concrete obstruction is a uniform **lower** excursion estimate plus collision/overlap control for the triangular exponentially collared law. At the target length `t~epsilon_n^{-2}log N_n`, a Brownian-excursion scale suggests exploration area `t^{3/2}` and therefore normalized collision exposure

\[
\frac{t^{3/2}}n
\asymp
\frac{(\log N_n)^{3/2}}{N_n}\to0,
\]

but this is only a route heuristic here; no conditioned-excursion theorem is claimed.

Frozen metric accounting:

`lim Delta_dual,n: 0 -> 0` — **NO MOVEMENT**.

This is the **third consecutive no-movement run** after the frozen metric reached its floor. I do not reset the counter merely because a new theorem was obtained. Under Section I, the **next HARD7-04 invocation must be a STUCK1 thinking/recovery run** for `VDH-8.3-DUALITY`: it must write the five-part obstruction report and choose exactly one recovery action. The most promising candidate is to port the lower-tail/excursion-counting mechanism from the nearest solved Erdős--Rényi / sharp subcritical configuration-model setting, but that choice belongs in the mandated Section-I run after the full obstruction comparison is recorded.

No closure, no paper package, and no audit request are made.

## 6. Verification / artifact accounting

The proof artifact was created at

`021e6d7733b0166de01b4b8929d64d834789c2a6`

and read back successfully at that exact commit. No finite exhaustive claim was introduced, so I did not spend the run manufacturing a checker. The theorem-sized claim is written in full in the artifact.

### ledger_delta

```yaml
track: HARD7-04
target: VDH-8.3-DUALITY
owner: HARD7-04
source_status: OPEN
research_status: PARTIAL
metric:
  name: Delta_dual_n = abs((1-nu_dual_n)/epsilon_n - 1)
  admission_baseline: UNMEASURED
  before_this_run: asymptotic_limit_0
  after_this_run: asymptotic_limit_0
  movement: NO_MOVEMENT
  unchanged_streak_at_floor: 3
new_result:
  type: theorem_sized_partial
  statement: "for every fixed delta>0, P(C2 > (1+delta) 2 R_* epsilon^-2 log(n epsilon^3)) -> 0"
  artifact: artifacts/hard7_2026-09-18/HARD7-04/2026-09-19T1030Z__vdh_cramer_collar_upper_bound.md
  artifact_commit: 021e6d7733b0166de01b4b8929d64d834789c2a6
methods:
  - B6
  - B20
  - B25
remaining_obligation: "matching lower bound / full discrete-duality scaling; requires lower conditioned-excursion estimate and overlap/collision control"
next_protocol_state: STUCK1_REQUIRED
closure: false
```

## 7. Model / scheduler-control truth

The actual runtime identifies as **GPT-5.6 Sol** and exposes no authenticated reasoning-effort level, so the reasoning field is **UNVERIFIED**. This is not GPT-6 maximum.

The requested GPT-6/maximum setting remains prompt text only. The exposed automation-management interface provides title, prompt, schedule/timing mode and enabled state, but no binding model-family selector, no reasoning-effort selector, and no guaranteed execution-duration field. Making GPT-6/maximum binding would require an owner-authorized product/workspace/API control that persists model family and reasoning effort into execution routing and returns runtime attestation; that control is not exposed in this environment.

The historical `You cannot modify this task` response for a P26 scheduler ID is an authorization/ownership boundary. The lawful workaround is modification from the task's owning/authorized account/workspace context or platform/admin support. A repository edit cannot repair native scheduler ownership, and duplicating the task would violate the owner's collision rules. I did not modify, create, reactivate, or disable any schedule in this run.
