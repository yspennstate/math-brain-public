Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — HARD7-04 frozen metric **no movement**, \(Q_n=\sigma_n^2/(d_{\max}\delta_n)\to\sigma_n^2/(d_{\max}\delta_n)\); methods **B2, B4, B18**. GPT-6/maximum was requested in prompt text, but this runtime exposes no authenticated GPT-6/maximum selector or reasoning telemetry.

# HARD7-04 bounded research iteration — P0157 maximal-root cycle defect

Date: 2026-09-18 UTC. Repository/branch: `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL; source OPEN.** This is the second P0157 run after the P0150 source-correction handoff. The frozen source metric has one consecutive no-movement run after its preceding exact identification; this is not a section-I stuck run.

## 1. Continuity and repository state read before research

I resumed canonical claim `operations/claims/P0157.md`, owned by HARD7-04. I read the controlling files

- `operations/hard7_2026-09-18/CONTROL.md`,
- `operations/NEW_METHODS_2026-09-16.md`,
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`,
- `probability_campaign_2026_09/INDEX.md`,
- `probability_campaign_2026_09/RANKING.md`,
- root `POSTED.md`, root `RESULTS.md`, and root `QUEUE.md`,
- the latest own checkpoint `runs/hard7_2026-09-18/HARD7-04/2026-09-18T21-27-46Z__p0150_handoff_p0157_hub_concentration.md`,
- the newest neighboring HARD7-03 and HARD7-05 reports found in the repository search,
- the `probability_1000_intake_claude_20260907/problems.jsonl` intake ledger and the P0157 ranking/tiers entries.

A fresh repository collision search still shows `P0157` exclusively owned by HARD7-04; neighboring admission screens explicitly recognize that ownership. I found no release, duplicate owner, or posted equivalent statement.

The prior checkpoint established the source scales
\[
H_n=\frac{d_{\max}}{\delta_n},\qquad
E_n=\delta_n^{-2}\log(n\delta_n^3),\qquad
\delta_n:=1-\nu_n>0,
\]
and the branching-surrogate identity
\[
Q_n:=\frac{\operatorname{Var}(T_n)}{H_n^2}
=\frac{\sigma_n^2}{d_{\max}\delta_n}.
\]
That remains the fixed metric. I did not replace it with an easier quantity.

## 2. Primary-source/current-status refresh

The current primary source remains Remco van der Hofstad, *Stochastic processes on random graphs*, preliminary monograph dated **4 Aug 2026**, Notes on Section 8.3, printed p. 245 / PDF page 255. The page was re-read visually as a PDF in this run. It explicitly calls the finite-third-moment barely-subcritical configuration-model behavior an **open problem**, contrasting the strictly subcritical maximal-degree scale with the Erdos–Renyi barely-subcritical scale and predicting a phase transition within the subcritical regime.

The source assumptions used here are also explicit in the same monograph: Conditions 2.5(a)-(c) give empirical degree convergence with positive finite mean and second moment, and Theorem 8.4 uses the finite-third-moment strengthening \(\mathbb E[D_n^3]\to\mathbb E[D^3]<\infty\). The source's barely-subcritical discussion has \(\varepsilon_n=\nu_n-1<0\); this track continues to use \(\delta_n=-\varepsilon_n>0\) so the hub scale is positive.

I reran current-status searches for `barely subcritical configuration model finite third moment phase transition`, `largest barely subcritical component configuration model`, and tree/cycle/acyclic variants. The strongest directly relevant later paper I recovered is Coulson–Perarnau, *Largest component of subcritical random graphs with given degree sequence*, EJP 28 (2023), DOI 10.1214/23-EJP921: it proves subcritical upper bounds asymptotically tight for certain degree sequences, not the full finite-third-moment crossover still stated open in the 4 Aug 2026 source. I found no later theorem closing the source statement. This is a bounded search, not a claim of exhaustive absence.

## 3. Ninety-percent research: B2, B4, B18

### B2 — attack the negation / collision counterexample first

The previous run's branching calculation could fail on the graph if a component of hub scale \(d_{\max}/\delta_n\) self-intersects often. A deliberately hostile exponent test makes this look plausible: with
\[
d_{\max}\asymp n^{1/3},\qquad \delta_n=n^{-0.30},
\]
the source is outside the critical window because \(n\delta_n^3=n^{0.10}\to\infty\), yet the hub exploration length is about \(n^{0.633}\). A naive birthday heuristic \(T^2/n\) then diverges like \(n^{0.266}\), apparently threatening the branching picture.

That heuristic is wrong for the actual pairing process. A surplus edge is created with probability proportional to the **active frontier** \(A_t\), not to the total number of already discovered vertices. The relevant collision budget is therefore the queue area \(\sum_t A_t\), not \(T^2\).

### B18 — say it in another language: exact active-half-edge queue

For a chosen maximal-degree vertex \(v_n\) of degree \(d_n=d_{\max}\), I rewrote the configuration-model component exploration as an exact queue. Let \(A_t\) be the active half-edges after \(t\) pairings and \(\tau=\inf\{t:A_t=0\}\). If \(U_t\) are unseen vertices and \(\ell_n=\sum_i d_i\), then for \(t<\tau\)
\[
(\ell_n-2t-1)\,\mathbb E[\Delta A_t\mid\mathcal F_t]
=
\sum_{i\in U_t}d_i(d_i-2)-2(A_t-1).
\tag{3.1}
\]
Since
\[
\sum_i d_i(d_i-2)=-\ell_n\delta_n
\]
and each discovered non-root vertex contributes at least \(-1\), at most \(t\) such vertices have been discovered. Hence
\[
\sum_{i\in U_t}d_i(d_i-2)\le-\ell_n\delta_n+t.
\tag{3.2}
\]
Up to any horizon \(T\le\ell_n\delta_n/4\), this gives the uniform negative drift
\[
\mathbb E[\Delta A_t\mid\mathcal F_t]\le-\delta_n/2.
\tag{3.3}
\]
Under \(\sum_i d_i^3\le Cn\) and \(\ell_n\ge cn\), the same exact pairing decomposition gives a uniform conditional second-moment bound
\[
\mathbb E[(\Delta A_t)^2\mid\mathcal F_t]\le B(c,C).
\tag{3.4}
\]

### B4 — prove a weaker graph theorem completely

Rather than attempting the full \((1+o_{\mathbb P}(1))d_{\max}/\delta_n\) law immediately, I closed the precise cycle obstruction. Summing the first- and second-moment queue inequalities gives
\[
\mathbb E[T\wedge\tau]\le\frac{2d_n}{\delta_n},
\tag{3.5}
\]
and
\[
\delta_n\,\mathbb E\!\left[\sum_{0\le t<T\wedge\tau}A_t\right]
\le d_n^2+\frac{2Bd_n}{\delta_n}.
\tag{3.6}
\]
At pairing time \(t\), the exact probability that the partner half-edge is already active is
\[
\frac{A_t-1}{\ell_n-2t-1},
\]
so, for \(T\le\ell_n\delta_n/4\),
\[
\mathbb P(N_{\rm cyc}(T)\ge1)
\le
\frac{4d_n^2}{\ell_n\delta_n}
+
\frac{8Bd_n}{\ell_n\delta_n^2}.
\tag{3.7}
\]
Finite third moment gives \(d_n=O(n^{1/3})\), while \(n\delta_n^3\to\infty\) gives \(n^{1/3}\delta_n\to\infty\). Therefore both terms in (3.7) vanish.

Choose
\[
K_n\asymp\left(\frac{\ell_n\delta_n^2}{d_n}\right)^{1/2}\to\infty,
\qquad
T_n=\left\lceil K_n\frac{d_n}{\delta_n}\right\rceil.
\]
Then \(T_n\le\ell_n\delta_n/4\) eventually and (3.5) yields
\[
\mathbb P(\tau>T_n)\le 2/K_n.
\]
Combining with (3.7) gives the quantitative auxiliary defect bound
\[
\boxed{
\mathbb P\bigl(\mathcal C(v_n)\text{ is cyclic}\bigr)
=O\!\left(\frac1{n^{1/3}\delta_n}\right)=o(1).
}
\tag{3.8}
\]
The same drift argument with fixed \(M\) also proves
\[
\mathbb P\!\left(|\mathcal C(v_n)|>1+M\frac{d_n}{\delta_n}\right)\le\frac2M
\]
for all sufficiently large \(n\), so \(|\mathcal C(v_n)|/(d_n/\delta_n)\) is tight.

A full proof, including the exact conditional drift/variance algebra and stopping argument, is archived at
`artifacts/hard7_2026-09-18/HARD7-04/p0157_max_degree_component_tree_like.md`.

No finite enumeration was claimed, so no finite exact-arithmetic checker was manufactured. The theorem-sized claim is proved on the page instead, as required.

## 4. What actually changed

The fixed admission metric did **not** move:
\[
Q_n:\quad \frac{\sigma_n^2}{d_{\max}\delta_n}
\longrightarrow
\frac{\sigma_n^2}{d_{\max}\delta_n}.
\]

But a real source-route obstruction did move. Before this run, the graph-versus-branching gap still included the possibility that the hub exploration accumulated surplus pairings on its long \(d_{\max}/\delta_n\) time scale. After (3.8), that mechanism is eliminated under the source's finite-third-moment barely-subcritical assumptions: a chosen maximal-degree component is a tree with probability \(1-o(1)\), even in exponent regimes where the naive \(T^2/n\) collision count diverges.

The remaining obligation is therefore narrower: **finite-population degree depletion/drift**, not self-intersection, must be controlled sharply enough to upgrade tightness to the source's predicted hub law
\[
|\mathcal C(v_{\max})|
=\frac{d_{\max}}{\delta_n}(1+o_{\mathbb P}(1))
\]
in the hub-dominated regime, and then a global argument must compare it against the Erdos–Renyi extreme scale. This run does not prove either of those statements.

## 5. Prior-art honesty

The active-half-edge exploration, drift bounds and martingale technology are classical, and closely related inequalities occur in Coulson–Perarnau's prescribed-degree analysis. I do **not** claim (3.8) is a novel theorem merely because the bounded searches did not surface this exact maximal-root formulation. The useful research content here is the route diagnosis: the frightening birthday-collision mechanism is provably the wrong obstruction, and the source problem should be attacked through finite-population drift/degree depletion instead.

## 6. Runtime/model-selector and task-modification status

The current automation interface still exposes scheduling fields such as prompt/title/schedule/timing mode/enabled state, but **no model selector, no reasoning-effort selector, no authenticated runtime reasoning telemetry, and no guaranteed run duration**. Thus GPT-6 maximum remains text-requested only in this environment. Changing that would require a platform/API surface that actually exposes model and reasoning controls or authenticated execution metadata; it cannot be achieved by a GitHub edit or by adding prompt text.

The repository's current `RESULTS.md` also corrects the older P26 permission incident: P26's full update succeeded in one authorized exposed context, while other contexts recorded `You cannot modify this task` for scheduler IDs they did not have permission to edit. The lawful workaround for any ID that still returns that error is to use an authorized native context/owner that has edit permission or obtain platform support. I did not bypass the denial by cloning, reactivating, or creating another task.

## 7. Ledger delta / checkpoint

```yaml
track: HARD7-04
canonical_claim: P0157
owner: HARD7-04
source_status: OPEN
research_status: PARTIAL
frozen_metric: Q_n = sigma_n^2/(d_max * delta_n)
before: sigma_n^2/(d_max * delta_n)
after: sigma_n^2/(d_max * delta_n)
movement: false
unchanged_count_on_P0157: 1
methods_this_run: [B2, B4, B18]
auxiliary_progress:
  maximal_root_cycle_probability: "UNMEASURED -> O((n^(1/3) delta_n)^(-1)) = o(1)"
  maximal_root_size: "uncontrolled graph-level -> tight on d_max/delta_n scale"
closure: false
audits_requested: 0
next_obligation: finite-population degree-depletion control strong enough for the hub LLN, then global hub-vs-ER crossover
next_candidate_methods: [B6, B11, B24]
```

The schedule remains active; no other schedule was created, modified, disabled or reactivated.
