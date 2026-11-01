Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT on newly reassigned P0157: inherited `Q_m=m^{-1}+O(m^{-2})->0`, now sharpened to `Q_m=m^{-1}-5/(12m^2)-m^{-3}+O(m^{-4})->0`; substantive source-route movement is much stronger: the fixed coefficient-three stress family is extended to a growing staircase with `L_1/(K_mH_m)->1` and `K_m->infinity`, hence `L_1/H_m->infinity` while `H_m/E_m->infinity`. Methods actually used by R14 on this fresh reassignment: #5 ADD A PARAMETER, #9 RANDOMIZE, #3 PROVE SOMETHING STRONGER.**

# R14 HARD OUTSIDE — P0157 growing staircase obstruction

Run date: 2026-09-19 UTC. Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / SOURCE OPEN.** This run does not reopen the negative-margin spherical perceptron, H0008, or any other terminally handed-off R14 target.

## 1. Continuity, release, and exclusive reassignment

The preceding R14 report is

`runs/R14/2026-09-19T10-56-40Z_h0008_terminal_handoff_successor_gate_4f2a.md`.

It correctly completed the terminal H0008 handoff after both allowed Section-I recoveries and identified P0157 as the strongest released HARD inventory item then visible.

At this run I reread/scoped the required current repository state before doing mathematics:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and the current owner directive;
- the newest R14 terminal report;
- `operations/claims/P0157.md`;
- the substantive HARD7-04 P0157 chain, including the multi-hub route refutation, absorbing hub kernel, four-hub exclusion / three-hub witness, exact three-hub occurrence, STUCK2 mass-transfer report, and compensated-queue `L_1/H_m->3` theorem;
- neighboring admission-delta reports that had observed P0157's release but had not taken ownership;
- the current posting/exclusion registry and bounded source/literature searches.

The canonical P0157 claim still said

`Owner: UNASSIGNED AFTER HARD7-04 HANDOFF`

and `SOURCE OPEN / PARTIAL / RELEASED BY HARD7-04 AFTER SECTION-I EXHAUSTION`. No competing live P0157 owner appeared in the bounded repository-wide ownership search. Unlike the previous R14 run, the current owner instruction itself requires rotation after a terminal hard-task handoff; explicit release plus a current collision-free ownership screen is therefore enough to make the canonical reassignment rather than create a shadow alias.

I updated the existing canonical file, not a duplicate:

`operations/claims/P0157.md`

so that the owner is now **R14**. The update commit is

`7abf1fbdd95124206987d7641b60c320c9e252b4`.

It was read back at that commit before this report was written.

This reassignment preserves every HARD7-04 result and both of that worker's consumed stuck recoveries as historical state. It does **not** give R14 permission to replay that exhausted route. R14 starts from the handoff diagnosis and must bring a genuinely fresh construction.

## 2. Exact outside source and fresh current-literature screen

Canonical source family retained from the claim:

Remco van der Hofstad, *Stochastic processes on random graphs*, Saint-Flour notes / preliminary monograph dated **4 August 2026**, discussion after the finite-third-moment critical-window theorems, historical Open Problem 4.13 / current Section 8.3 notes.

Use

\[
\delta_n:=1-\nu_n>0,
\qquad
\nu_n=\frac{\sum_i d_i(d_i-1)}{\sum_i d_i},
\]

with `delta_n->0` and `n delta_n^3->infinity`. The source contrasts the high-degree scale

\[
H_n=\frac{d_{\max}}{\delta_n}
\]

with the Erdős--Rényi extreme scale

\[
E_n=\delta_n^{-2}\log(n\delta_n^3)
\]

and suggests a phase transition within the barely-subcritical finite-third-moment regime.

Fresh bounded queries dated 2026-09-19 included combinations of

- `barely subcritical configuration model largest component finite third moment 2026`,
- `configuration model largest component high degree vertices barely subcritical crossover`,
- `configuration model multiple high-degree vertices subcritical largest component`,
- the exact Coulson--Perarnau title and source terminology.

The search again recovered Matthew Coulson and Guillem Perarnau, *Largest component of subcritical random graphs with given degree sequence*, arXiv:2111.11780 / EJP 28 (2023). Their abstract states strong CM upper bounds that are asymptotically tight for certain degree sequences and improve earlier barely-subcritical bounds, but it does not state the full finite-third-moment two-scale transition retained as open in the repository's August 2026 source record.

The search also recovered 2026 work on **different** random-graph models, including Mörters--Schleicher's largest subcritical component in preferential-attachment-type inhomogeneous random graphs, and older/adjacent Norros--Reittu results. These are useful shape analogies but are not the deterministic-degree configuration model of P0157. No source-matching 2026 theorem closing the residual surfaced in the bounded search. This is bounded negative evidence, not a worldwide novelty certificate.

## 3. Frozen metric and why it does not move

The canonical P0157 metric is the local branching-surrogate fluctuation ratio

\[
Q_n
=\frac{\operatorname{Var}(T_n)}{(d_{\max}/\delta_n)^2}
=\frac{\sigma_n^2}{d_{\max}\delta_n},
\]

where `sigma_n^2=Var(xi_n)` for the forward offspring law.

HARD7-04 had already established, on its explicit degree-`{1,3,m^2}` stress family,

\[
Q_m=m^{-1}+O(m^{-2})\to0.
\]

The new family below preserves the same `Q_m`, now with exact rational formula and expansion

\[
Q_m
=m^{-1}-\frac5{12}m^{-2}-m^{-3}+O(m^{-4})\to0.
\]

Therefore the **fixed metric does not move**. The substantive progress is instead a certified obstruction showing that this metric, together with `H_m/E_m`, is radically insufficient for the source theorem.

This is R14's first fresh-route run after canonical reassignment, so the current R14 route's unchanged counter is `1`; the previous owner's `2/2` recoveries remain preserved as historical exhausted-route state rather than being erased.

## 4. New theorem-sized route result: an unbounded integer staircase

The full written self-check is

`artifacts/R14/p0157_growing_integer_staircase_obstruction.md`

created at

`eb15c0066e022bf842dccff8faddfb23cc2b3ace`.

The theorem is as follows.

Let `m->infinity` through even integers and set

\[
K=K_m=\left\lfloor\sqrt{\frac{\log m}{\log\log m}}\right\rfloor,
\]

\[
n=8m^{2K+6},\qquad M=m^{2K-1},\qquad d=m^2,
\]

\[
x=3m^{2K+5}+\frac{M}{4}(d-1)^2,
\]

and degree counts

\[
N_d=M,
\qquad
N_3=2m^{2K+6}-x,
\qquad
N_1=6m^{2K+6}+x-M.
\]

Then the configuration model satisfies

\[
\boxed{\frac{L_1}{K_mH_m}\xrightarrow{\mathbb P}1,}
\qquad H_m=\frac d{\delta_m},
\tag{4.1}
\]

and, if `H_max` is the maximum number of designated degree-`d` hubs in one component,

\[
\boxed{\mathbb P(H_{\max}=K_m)\to1.}
\tag{4.2}
\]

At the same time

\[
\boxed{
H_m/E_m\to\infty,
\qquad Q_m\to0,
\qquad L_1/H_m\to\infty\text{ in probability}.
}
\tag{4.3}
\]

So the fixed coefficient-three example is not an isolated pathology. It is one point on a staircase whose height can diverge while the source's two classical scalar scales separate ever more strongly in the nominal high-degree direction.

## 5. Exact family algebra

The construction is designed so that the old fixed-`K=3` cancellation survives for a growing `K`. The total half-edge count factors exactly as

\[
\ell
=\frac{m^{2K-1}}2
(24m^7-12m^6-m^4+4m^2-3),
\tag{5.1}
\]

while

\[
\ell-\sum_vd_v(d_v-1)=12m^{2K+5}.
\tag{5.2}
\]

Therefore

\[
\delta_m
=\frac{24m^6}{24m^7-12m^6-m^4+4m^2-3}
\sim m^{-1},
\tag{5.3}
\]

**independently of `K` after cancellation**.

The empirical degree law still tends to

\[
P(D=1)=3/4,\qquad P(D=3)=1/4,
\]

and the hub contribution to the third moment is exactly

\[
\frac{Md^3}{n}=\frac1{8m}\to0.
\]

Thus the third moments converge and the family remains inside the intended finite-third-moment regime.

Because

\[
\log(n\delta_m^3)=(2K+3+o(1))\log m,
\]

we have

\[
\frac{H_m}{E_m}
\sim\frac{m}{(2K+3)\log m}\to\infty.
\tag{5.4}
\]

The exact local variance calculation gives the `K`-independent formula

\[
Q_m=
\frac{
576m^{14}-528m^{13}-456m^{12}-240m^{11}+118m^{10}
+336m^9-151m^8-144m^7+20m^6+70m^4-42m^2+9
}{24m^8(24m^7-12m^6-m^4+4m^2-3)},
\tag{5.5}
\]

which yields the expansion in Section 3.

## 6. Method #5 — add a parameter: turn coefficient three into a moving threshold

The old stress family fixed the number of hubs at the connectivity threshold at three. The new parameter `K=K_m` is inserted into the *number of hubs and ambient graph size*, while deliberately leaving `delta_m`, the limiting degree law, and `Q_m` asymptotically unchanged.

Let

\[
a_m=\frac{6N_3}{\ell}=1-\frac1m+O(m^{-2}).
\]

The bulk-mediated connection scale between two prescribed hubs is

\[
\frac{d^2}{\ell(1-a_m)}
=\Theta(m^{-(2K+1)}).
\]

Since there are `M=m^{2K-1}` hubs, the first-moment power of `m` for an `r`-hub tree is exactly

\[
\boxed{2K+1-2r.}
\tag{6.1}
\]

Thus

\[
r=K:\quad m^{+1},
\qquad
r=K+1:\quad m^{-1}.
\tag{6.2}
\]

That moving `+1/-1` exponent gap is the staircase mechanism.

Outcome of #5: **successful**. The old fixed-three example extends to a tunable, slowly diverging threshold without changing the local branching metric.

## 7. Method #9 — randomize: path-witness second moment gives the lower hub threshold

Take an ordered `K`-tuple of distinct hubs and connect consecutive hubs by internally vertex-disjoint degree-three paths, each with length in `[m,2m]`. If the total path length is `R` and there are `q=R-(K-1)` internal degree-three vertices, the exact witness first moment is

\[
\mathbb EZ_K
=(M)_K d^K(d-1)^{K-2}
\sum_{r_1,\dots,r_{K-1}=m}^{2m}
\frac{(N_3)_q6^q}
{(\ell-1)(\ell-3)\cdots(\ell-(2R-1))}.
\tag{7.1}
\]

Because `K log K=o(log m)` and `R=O(Km)`, all finite-population corrections are uniform `1+o(1)`. Hence

\[
\mathbb EZ_K
=(1+o(1))m
\left(\frac{e^{-1}-e^{-2}}{12}\right)^{K-1}.
\tag{7.2}
\]

Our choice `K=sqrt(log m/log log m)+O(1)` makes the right-hand side tend to infinity.

Conditioned on one witness, the residual active queue is `O(Km^2)`, its mean exploration time is `O(Km^3)`, and the per-pairing unseen-hub hazard is `O(m^{-5})`; therefore the chance of acquiring an extra hub is `O(Km^{-2})=o(1)`. The residual cycle probability is also `o(1)`. Let `Z_K^g` count witnesses whose host is a tree containing exactly those `K` hubs.

For two disjoint witness skeletons, exact perfect-matching factorization gives

\[
\mathbb ED_K^0=(1+o(1))(\mathbb EZ_K)^2.
\]

A good tree host supports at most the two orientations of its unique `K`-hub path, so pointwise

\[
(Z_K^g)^2\le2Z_K^g+D_K^0.
\]

The second-moment inequality yields

\[
\boxed{P(Z_K^g>0)\to1.}
\tag{7.3}
\]

Hence some component has at least `K` hubs whp.

Outcome of #9: **successful**. Random witness counting remains stable even though `K` itself diverges.

## 8. Method #3 — prove something stronger: exclude `K+1` hubs and prove the mass asymptotic

### 8.1 No `K+1`-hub component

If a component contains `r=K+1` hubs, prune a minimal connecting tree to exactly those `r` hubs, suppress ordinary relative-degree-two vertices, and obtain a core with `t` ordinary degree-three branch vertices (`0<=t<=r-2`) and `e=r+t-1` core edges.

There are at most

\[
\exp(O(K\log K))
\]

labeled core topologies. Expanding each core edge into a degree-three chain and summing chain lengths gives the expectation bound

\[
\exp(O(K\log K))
M^r\left(\frac{d^2}{\ell(1-a_m)}\right)^{r-1}
O((d(1-a_m))^{-t}).
\tag{8.1}
\]

At `r=K+1`, the base factor is `Theta(m^{-1})`, each branch contributes another `O(m^{-1})`, and `exp(O(K log K))=m^{o(1)}`. Long core segments (`>=m^2`) are globally negligible because their expected count is at most

\[
\exp\{O(K\log m)-cm\}=o(1).
\]

Therefore

\[
\boxed{P(H_{\max}\ge K+1)\to0.}
\tag{8.2}
\]

Together with (7.3), `P(H_max=K)->1`.

### 8.2 Mass is `K H_m`

Reuse, but do not merely quote, the compensated queue

\[
C_t=A_t-dH_t.
\]

Its increments stay in `{-2,-1,+1}` and its exact drift is

\[
\mu_t=
\frac{-\ell\delta_m-Md^2-3R_{3,t}+R_{1,t}-2C_t+2}
{\ell-2t-1}.
\tag{8.3}
\]

Uniformly for `t=O(KH_m)`,

\[
\mu_t=-(1+o(1))\delta_m,
\]

with the matching upper drift while `H_t<=K`. The compensated martingale has bounded increments, so a deviation of order `Kd` over `O(KH_m)` steps has probability

\[
\exp\{-\Theta(Km)\}.
\tag{8.4}
\]

This beats union over all `n` vertices because `log n=O(K log m)=o(Km)`.

Using `H_max<=K` whp, (8.4) gives the global upper bound

\[
L_1\le(1+\varepsilon)KH_m\quad\text{whp}.
\]

Condition on a good `K`-hub path witness. Its compensated initial queue is only `O(Km)=o(Kd)`. Premature extinction before `(1-eps)KH_m` forces a negative compensated-martingale deviation of order `eps Kd`, again with cost `exp{-Theta_eps(Km)}`. Multiplying by the total expected witness count still gives `o(1)`. Since a good witness exists whp,

\[
L_1\ge(1-\varepsilon)KH_m\quad\text{whp}.
\]

This proves

\[
\boxed{L_1/(KH_m)\to1\text{ in probability}.}
\tag{8.5}
\]

Outcome of #3: **successful**. The stronger statement is not merely that the coefficient can differ from one; it can diverge under the same local metric and while `H/E->infinity`.

## 9. Exact checker

Only after the route theorem was written did I build a finite exact-arithmetic self-check for the family algebra:

`artifacts/R14/p0157_growing_staircase_exact.py`

created at commit

`3d7e25ece140c0c7e14bbd733336a8d4f981281f`.

It checks `k=2,...,8` and `m in {10,12,20}` using Python `Fraction` arithmetic, verifying:

- exact integrality/nonnegativity on the sanity grid;
- (5.1) and (5.2);
- exact `delta_m` cancellation;
- exact `K`-independence of `Q_m` on each checked slice;
- the hub third-moment identity `Md^3/n=1/(8m)`;
- the first-moment exponent identity `2K+1-2r`, including `+1` at `r=K` and `-1` at `r=K+1`.

Executed output is archived at

`artifacts/R14/p0157_growing_staircase_exact.out`

commit

`af3f40eaf1b887ea3f63e25d824b52aec55fbffd`,

and ends

`ALL_EXACT_CHECKS_PASS`.

The checker is explicitly a **self-check of finite algebra**, not a certificate for the asymptotic probability theorem.

## 10. Interpretation and source status

The new family simultaneously satisfies

\[
\delta_m\sim m^{-1},
\quad n\delta_m^3\to\infty,
\quad n^{-1}\sum_vd_v^3\to15/2,
\]

\[
H_m/E_m\to\infty,
\quad Q_m\sim m^{-1}\to0,
\quad L_1/H_m\sim K_m\to\infty.
\]

So two scalar quantities that looked natural after the first P0157 runs—`H/E` and the one-root concentration scalar `Q`—cannot possibly characterize the broad finite-third-moment high-degree side by themselves.

The missing information is a global upper-tail connectivity object: roughly, the marked point process of near-maximal degrees together with the rank-one connection kernel generated by the barely-subcritical bulk. The previous HARD7-04 absorbing-kernel result already points at

\[
\kappa_{ij}\approx\frac{d_id_j}{\ell\delta_H}.
\]

The next source-level route should therefore aim at a theorem in which the largest component mass is a functional of the connected components of this marked hub kernel plus the bulk-mass map, with the ER extreme term entering when no hub-kernel component dominates.

This is **PARTIAL**, not REFUTED or PROVED. The source prose asks for the correct crossover, not the false stronger rule that `H/E->infinity` forces `L_1/H->1` or even a universally bounded ratio.

## 11. Method-catalogue honesty

The reassigned target comes with a very long inherited HARD7-04 history. That predecessor had already exercised essentially the full 30-item method catalogue in various fixed-`K` attacks. Thus a literal demand for three method numbers never seen anywhere in P0157's historical folder is no longer satisfiable without inventing history.

For this **fresh R14 reassignment**, the actual new-route triple is #5 / #9 / #3. It does not repeat R14's preceding #18 / #20 / #30 terminal-handoff triple. The mathematical uses here are genuinely different from the inherited fixed-`K` runs: #5 makes the stress coefficient itself diverge, #9 performs a moving-`K` random witness second moment, and #3 upgrades a finite-coefficient obstruction to an unbounded-ratio theorem.

## 12. Model / scheduler / permissions truth

Actual model in this invocation: **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6 or verified maximum reasoning.

The exposed automation-control schema in this runtime permits task prompt/title, schedule or relative start, timing mode, and enabled state. It exposes **no bindable model-family field and no reasoning-effort field**, and it gives no authenticated per-run model/effort attestation or guaranteed hour-long duration. Therefore `GPT-6 / maximum` is still prompt text only here.

Making it enforceable requires an owner-authorized product/workspace/admin/API surface that actually persists model-family and reasoning-effort settings into task execution and reports them back as runtime telemetry.

The historical P26 `You cannot modify this task` result remains an authorization-context issue. Current repository deployment records say P26 was later successfully updated from another authorized context. The lawful workaround for a task that still returns that denial is its owning/admin-authorized context or platform support; there is no permission bypass. I made no scheduler or permission change in this run.

## 13. Structured ledger delta

```yaml
ledger_delta:
  worker: R14
  category: HARD_OUTSIDE
  runtime_model: GPT-5.6 Sol
  reasoning_level: UNVERIFIED
  requested_model: GPT-6
  requested_reasoning: maximum

  predecessor_source_id: H0008
  predecessor_state: TERMINALLY_HANDED_OFF_PREVIOUS_RUN
  predecessor_reopened: false

  source_id: P0157
  source_owner_before: UNASSIGNED_AFTER_HARD7_04_HANDOFF
  source_owner_after: R14
  canonical_claim: operations/claims/P0157.md
  reassignment_commit: 7abf1fbdd95124206987d7641b60c320c9e252b4
  source_status: SOURCE_OPEN
  worker_status: PARTIAL

  fixed_metric: Q_n=sigma_n^2/(d_max*delta_n)
  fixed_metric_before: m^-1+O(m^-2)->0_on_inherited_stress_family
  fixed_metric_after: m^-1-(5/12)m^-2-m^-3+O(m^-4)->0_on_growing_staircase_family
  fixed_metric_movement: NO_LIMIT_MOVEMENT
  r14_new_route_unchanged_count: 1
  prior_owner_hard_recoveries: 2/2_EXHAUSTED_AND_PRESERVED

  section_B_methods_actual: [5, 9, 3]
  theorem_candidate: L1/(K_m*H_m)->1_with_K_m=floor(sqrt(log_m/loglog_m))
  theorem_companion: P(H_max=K_m)->1
  source_route_obstruction: H_m/E_m->infinity_and_Q_m->0_but_L1/H_m->infinity

  proof_artifact: artifacts/R14/p0157_growing_integer_staircase_obstruction.md
  proof_artifact_commit: eb15c0066e022bf842dccff8faddfb23cc2b3ace
  checker: artifacts/R14/p0157_growing_staircase_exact.py
  checker_commit: 3d7e25ece140c0c7e14bbd733336a8d4f981281f
  checker_output: artifacts/R14/p0157_growing_staircase_exact.out
  checker_output_commit: af3f40eaf1b887ea3f63e25d824b52aec55fbffd
  checker_result: ALL_EXACT_CHECKS_PASS
  independent_audits: 0
  closure_claimed: false

  current_literature_screen_date: 2026-09-19
  source_matching_resolution_found: false_in_bounded_search
  novelty_claimed: false

  shared_roots_edited: false
  peer_files_edited: false
  scheduler_changed: false
  email_or_drive_used: false
  public_posting_used: false
```

## 14. Net result / next obligation

R14 now has a lawful exclusive HARD OUTSIDE successor and a genuinely new route result rather than another successor-gate receipt. The main theorem-sized self-check says that the source's nominal high-degree regime can contain a growing hub-connectivity staircase: `H/E->infinity` and local concentration `Q->0` coexist with `L_1/H->infinity`.

The next useful obligation is no longer another special family. It is to formulate and attack a **general marked-hub reduction**: under source finite-third-moment hypotheses, identify sufficient conditions under which the induced hub-connectivity graph is approximated by the rank-one kernel `d_i d_j/(ell delta_H)` strongly enough that its largest weighted component, after the bulk-mass map, gives `L_1` to relative error. That is the route capable of turning the obstruction into a corrected crossover theorem.
