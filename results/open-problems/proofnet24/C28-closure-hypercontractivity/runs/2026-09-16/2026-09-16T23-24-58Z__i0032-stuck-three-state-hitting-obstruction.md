Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED; this was not GPT-6 at maximum, and I do not claim otherwise. **NO MOVEMENT — frozen I0032 comparison factor remains `2 -> 2`; unchanged-run count `3 -> 4`; this is the required Section-I STUCK / THINKING-ONLY run, with no new C28 theorem claim. Section-B moves: 7, 12, 29.**

# C28 — STUCK RECOVERY 1: the matched-hitting route meets a three-state boundary obstruction

Repository / branch: `yspennstate/math-open-problems` / `master`.
Own root: `proofnet24/C28-closure-hypercontractivity`.
Run date: 2026-09-16 UTC / 2026-09-17 local campaign date.
Allocation/status: CLOSABLE OUTSIDE, **CLAIMED / PENDING_ADMISSION / NOT READY**.
Delivery: private GitHub only. No email/Gmail, Drive, public posting, paid compute, access change, peer-file edit, shared-ledger edit, or new schedule.

## 1. Continuity, source gate, ownership, and reserve

I continued from the newest durable C28 report

`proofnet24/C28-closure-hypercontractivity/runs/2026-09-16/2026-09-16T22-34-47Z__i0032-threshold-hitting-bridge.md`

rather than restarting. At run start I reread or exact-searched the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, canonical claim `operations/claims/I0032.md`, the exact I0032 intake/history surface, the own C28 report chain, the newest C29 report, and the Paley reserve handoff. The large intake/attempt JSONL mirrors are connector-truncated, so the intake/history check is honestly recorded as targeted exact-ID/source-phrase recovery rather than a claim of rendering every JSONL byte.

The canonical claim still has **Owner C28 / CLAIMED / PENDING_ADMISSION — NOT READY**. No competing canonical I0032 claim was recovered. The queue still lists I0032 as a pending candidate, not READY. The older compact `RESULTS.md` successor row is stale relative to the six complete C28 mathematical reports and does not reset the supported metric.

### Exact source scope, rechecked visually

Aldous–Fill §8.4.2 works with a finite irreducible reversible continuous-time chain and defines

\[
N(s)=\|P_s\|_{2\to\infty}.
\]

The source says that `N` decreases continuously from `pi_*^{-1/2}` to `1`, and asks — explicitly with comparison in mind — to characterize in terms of the Dirichlet form `E` the time `s*` at which `N(s)=2`. Open Problem 8.23 is exactly “Characterize `s*` in terms of `E`.” The subsequent finite-`q` hypercontractive thresholds `s_q` are distinct quantities. I rechecked the official source page visually in this run rather than relying only on intake prose.

The working total-domain convention remains

\[
s_*:=\inf\{s\ge0:\|P_s\|_{2\to\infty}\le2\},
\]

which agrees with the source root when positive.

### Paley-ETF remains HARD RESERVE

The prior Paley conditioning attack remains untouched in **HARD RESERVE**. Preserve exactly

\[
\kappa_*
=6.6575355565204281495\ldots
\]

at `(p,m)=(73,14)`, strict exact two-swap local maximality against all `161070` exchange-radius-two neighbors, the proved common neighbor upper bound `6.603863488301192967...`, every archived exact certificate and failed route, and the governing quantifier correction: **one badly conditioned finite submatrix, even a certified local extremum, does not refute an existential assertion that some asymptotic family is uniformly well conditioned.**

## 2. Frozen metric and why this run is thinking-only

The frozen full-source-class candidate remains the already-fixed binary state-anchored dyadic local-spectral threshold `S_anch,2(E)`. The proved comparison is

\[
 s_*\le S_{\rm anch,2}(\mathcal E)\le2s_*,
\]

and factor `2` is already known sharp for this candidate. Therefore

\[
\boxed{2\longrightarrow2}.
\]

The immediately preceding run made the third consecutive no-movement report. Under Section I, this invocation must therefore be a **thinking run with no new C28 theorem-sized claim**. I obey that constraint: the three-state calculations below are a route diagnostic and candidate counterexample to be formalized or killed in the next ordinary run; they are **not assigned a claim ID and are not promoted to PROVED/REFUTED status here**.

## 3. Exact statement that blocks

The previous run identified the threshold-matched hitting profile

\[
\rho_x^{(a)}:=\inf\left\{t\ge0:
\mathbf P_x(T_{A^c}>t)
\le \pi(A)+a\sqrt{\pi(A)\pi(A^c)}
\quad\forall A,\ 0<\pi(A)\le\tfrac12
\right\},
\]

\[
\rho^{(a)}:=\max_x\rho_x^{(a)},
\]

proved

\[
\rho^{(\sqrt3)}\le s_*,
\qquad
s_*=\tau_2(\sqrt3),
\]

and showed exact zero-boundary matching at `pi_*=1/4`.

The blocking statement is therefore

\[
\boxed{
\exists C<\infty\ ?\quad
s_*\le C\,\rho^{(\sqrt3)}
\quad\text{for every finite irreducible reversible continuous-time chain.}
}
\tag{3.1}
\]

The principal outcome of this thinking run is that (3.1) now looks **false**, for a very small and source-admissible reason. I do not promote that diagnosis to a theorem in this run.

## 4. Every current-target route tried, and the precise failure

1. **Ordinary spectral-profile integral.** It gives a static Dirichlet-form object, but the known spectral-profile/uniform-mixing sharpness phenomena force logarithmic losses and do not yield the desired source-normalized constant-factor characterization on the full class.

2. **State-anchored dyadic local spectrum.** This succeeds uniformly:
   \[
   s_*\le S_{\rm anch,2}\le2s_*.
   \]
   But the factor `2` is sharp for that candidate, so it cannot move the frozen metric, and the hard dyadic cutoffs are unstable under small perturbations that move spectral mass across a bin boundary.

3. **Finite smooth/resolvent replacement.** For fixed depth `n`, the refresh-chain calculation gives an unbounded ratio `S_n/s_*`; finite implicit-Euler cascades have polynomial high-frequency tails, whereas heat flow has exponential damping.

4. **Infinite resolvent depth.** It converges to `e^{-2tL}` and hence reconstructs `s_*` exactly, but that simply rebuilds the semigroup and is tautological relative to the source's comparison-motivated request.

5. **Standard Hermon–Peres hitting characterization.** Their theorem characterizes the conventional `tau_2(1/2)`, while the source parameter is exactly `tau_2(sqrt(3))`. On the asymmetric two-state boundary family, `tau_2(1/2)/s_*` and the standard `rho^{(1/2)}/s_*` diverge as `pi_*` approaches `1/4`, so threshold-blind transplantation is impossible.

6. **Threshold-matched hitting profile.** The previous run proved the source-exact one-sided inequality `rho^{(sqrt(3))} <= s_*`, exact matching of the zero set, and asymptotic ratio one on the two-state approach from below. This was the most promising new route. The present three-state diagnostic indicates that its reverse comparison fails because sets of stationary mass just **above** `1/4` become invisible to the matched survival constraint while still carrying a near-threshold slow mode.

7. **Comparison-sensitive hard-band smoothing.** The tension remains structural: hard spectral localization sees the near-threshold residual but is perturbation-unstable; finite smooth filters are perturbation-friendly but leak too much high-frequency mass. No route so far combines exponential spectral localization with a static comparison-stable Dirichlet description.

## 5. Section-B move 7 — take the boundary limit

I looked directly at a three-state symmetric family approaching the source boundary from the **other side** of `pi=1/4`.

Let

\[
\Omega=\{0,1,2\},\qquad
\pi_0=\pi_1=\frac p2,\qquad
\pi_2=1-p,
\]

with

\[
\frac14<p<\frac12,
\qquad
u:=4p-1>0,
\qquad
c:=\nu^2.
\]

Take reversible conductances

\[
w_{01}=\frac p2,
\qquad
w_{02}=w_{12}=c,
\]

and rates `q_ij=w_ij/pi_i` before an optional global source-normalizing time rescaling. This gives

\[
q_{01}=q_{10}=1,
\qquad
q_{02}=q_{12}=\frac{2c}{p},
\qquad
q_{20}=q_{21}=\frac{c}{1-p}.
\]

If one insists on the Aldous–Fill unit-rate Poissonization convention, divide the whole generator by

\[
R_p:=1+\frac{2c}{p}.
\]

Then every exit rate is at most one and `P=I+Q/R_p` is stochastic. Both `s_*` and the hitting time below are multiplied by the same `R_p`, so their ratio is unchanged. Thus the diagnostic is not an artifact of a time normalization.

As `p` decreases to `1/4` from above, the two-state rare cluster `{0,1}` has mass just above the point where the `sqrt(3)` survival threshold becomes vacuous. This is the boundary object that the previous two-state family, approaching from below, could not see.

## 6. Section-B move 12 — use the conserved symmetry sectors

The exchange symmetry `0 <-> 1` splits the centered space into two invariant one-dimensional sectors. Exact scratch algebra gives

\[
\lambda_f=2+\frac{2c}{p}
\]

for the antisymmetric mode `(1,-1,0)`, and

\[
\lambda_s=\frac{2c}{p(1-p)}
\]

for the rare-cluster-versus-common mode.

For a rare starting point, the exact two-mode `L_2` expression is

\[
d_{2,0}(t)^2
=
\frac{1-p}{p}e^{-2\lambda_s t}
+
\frac1p e^{-2\lambda_f t}.
\tag{6.1}
\]

The common starting point has only the slow mode,

\[
d_{2,2}(t)^2
=
\frac{p}{1-p}e^{-2\lambda_s t}<3,
\]

so it is already below the source threshold at time zero for this parameter range.

The crucial exact gap is

\[
3-\frac{1-p}{p}
=\frac{4p-1}{p}
=\frac{\nu}{p}.
\tag{6.2}
\]

If the slow mode is essentially frozen, the fast mode must decay all the way to this shrinking gap. The corresponding reference time is

\[
t_0
:=
\frac{1}{2\lambda_f}\log\frac1\nu.
\tag{6.3}
\]

Because `c=nu^2`,

\[
\lambda_s t_0=O\!\left(\nu^2\log\frac1\nu\right)\to0,
\qquad
\lambda_f\to2.
\]

At `t_0` the fast term in (6.1) is exactly the gap in (6.2), while the slow term has decreased slightly, so the source crossing occurs no later than `t_0`. Conversely, for every fixed `eta in (0,1)`, at `(1-eta)t_0` the fast excess is of order `nu^(1-eta)`, whereas the slow-mode loss is only `O(nu^2 log(1/nu))`; the former dominates. This strongly indicates

\[
s_*\sim t_0\sim\frac14\log\frac1\nu.
\tag{6.4 diagnostic only}
\]

Again: (6.4) is recorded here as the output of the stuck-route analysis, not as a promoted theorem claim.

## 7. Section-B move 29 — add the boundary point where the hitting constraint switches off

For the matched threshold define

\[
g(u):=u+\sqrt3\sqrt{u(1-u)}.
\]

The elementary boundary identity is

\[
g(u)\ge1\iff u\ge\frac14.
\tag{7.1}
\]

In the three-state family, the only eligible sets of stationary mass at most `1/2` that can contain a rare starting state are the singleton and the rare cluster. The cluster has mass `p>1/4`, so by (7.1) its required survival upper bound is at least `1` and therefore vacuous. The singleton has mass `p/2<1/4`, and its exact survival probability is

\[
\mathbf P_0(T_{\{0\}^c}>t)
=
\exp\left[-\left(1+\frac{2c}{p}\right)t\right].
\]

Thus the scratch diagnostic for the matched profile is

\[
\rho^{(\sqrt3)}
=
\frac{-\log g(p/2)}{1+2c/p}
\longrightarrow
-\log g(1/8)
=
\log\frac{8}{1+\sqrt{21}},
\tag{7.2}
\]

a finite positive constant, while the source threshold appears to diverge logarithmically as in (6.4).

The proposed reverse comparison (3.1) therefore appears to fail already on this symmetric three-state family. The mechanism is conceptually sharp: the matched hitting profile forgets a metastable set immediately after its mass crosses `1/4`, but `s_*` still detects how a small fast spectral residue must decay relative to the vanishing gap between the slow-mode mass and the source threshold `3`.

This is the main research value of the run. I deliberately did **not** turn it into a theorem in a run whose protocol forbids new theorem claims.

## 8. What a successful characterization now has to contain

If the three-state diagnostic is formalized next run, any viable replacement for the matched hitting profile must contain something absent from every route so far:

- it must see sets of mass just **above** `1/4`, even though the source-matched one-set survival inequality is already vacuous there;
- it must record the **residual spectral mass relative to the threshold gap**, not just a relaxation scale or an exit time;
- it must retain exponential-in-energy localization strongly enough to avoid the finite-resolvent polynomial-tail obstruction;
- it must nevertheless remain stable enough under comparison of Dirichlet forms that it is not merely the semigroup written in disguise.

A plausible category for future work is therefore an **anchored threshold-residue/capacity profile**: a statewise variational object that keeps both the mass of a near-critical cluster and the amount of energy/spectral residue outside its slow sector. No such object is claimed here.

## 9. Simplest special case still unproved

The simplest unresolved finite obligation is no longer an arbitrary chain. It is exactly the source-normalized three-state family above:

\[
\boxed{
\pi=(p/2,p/2,1-p),
\quad
w_{01}=p/2,
\quad
w_{02}=w_{12}=(4p-1)^2,
\quad
p\downarrow1/4+.
}
\tag{9.1}
\]

The next ordinary research run should either prove rigorously from the exact formulas that

\[
\frac{s_*}{\rho^{(\sqrt3)}}\to\infty,
\tag{9.2}
\]

or find the flaw before any broader construction is attempted. That is strictly simpler and more informative than adding another general comparison lemma.

## 10. Nearest solved problem and the ingredient it has that this source threshold lacks

The nearest solved result remains **Hermon–Peres, PTRF 170 (2018), 769–800**, which gives a constant-factor hitting-time characterization of the conventional continuous-time reversible `L_2` mixing time `tau_2(1/2)` and an extremal log-Sobolev characterization.

Their standard-threshold argument can strengthen the hitting condition and then absorb a relaxation-time error. In the source-matched `sqrt(3)` problem, the zero-time boundary `pi_*=1/4` changes the geometry: a set of mass just above `1/4` already has a vacuous matched survival constraint, while a residual mode can still delay `tau_2(sqrt(3))` by an arbitrarily large logarithmic amount. In other words, the Hermon–Peres proof has a **uniform margin away from the source's singular threshold** that the adapted problem lacks.

This explains why merely changing `1/2` to `sqrt(3)` in their theorem is not a cosmetic threshold modification.

## 11. Literature refresh and limitations

Dated fresh searches on 16–17 September 2026 included:

- `"Open Problem 8.23" Aldous Fill hypercontractivity Dirichlet form`;
- `"A characterization of L2 mixing and hypercontractivity via hitting times and maximal inequalities" Hermon Peres`;
- `"Aldous-Fill" "Open Problem 8.23" hypercontractivity 2025 2026`;
- `"Sensitivity of mixing times of Cayley graphs" "Open Problem 8.23"`;
- `"Open Problem 8.23" "Dirichlet form" mixing Markov 2025 2026`;
- `"Characterize s*" "Dirichlet form" Markov chain 2025 2026`.

They recovered the official Aldous–Fill statement, Hermon–Peres (2018), and Hermon–Kozma’s *Sensitivity of mixing times of Cayley graphs* (published online 18 July 2023; CJM 76(4), 2024), which explicitly cites Aldous–Fill Open Problem 8.23 in its robustness discussion. I did not locate a later source-exact resolution in the bounded 2025–2026 search. This remains **negative-search evidence only**, not proof of worldwide openness or a novelty certificate.

The official Aldous–Fill PDF page containing the problem was visually checked successfully. The Hermon–Peres bibliographic/source text was accessible; no claim in this report depends on an unverified OCR-only formula from an inaccessible image.

## 12. Section-I choice and next moves

I choose exactly one Section-I recovery action:

\[
\boxed{\textbf{REFUTE INSTEAD OF PROVE}.}
\]

The next ordinary C28 run should first formalize or kill the three-state family (9.1) as a counterexample to the reverse matched-hitting comparison. Only if that diagnostic fails should the route return to a positive comparison proof.

The next three Section-B moves, all untried on I0032 in the recovered move history, are:

- **B2 ATTACK THE NEGATION FIRST:** turn (9.1) into an exact source-normalized counterexample, with complete inequalities rather than asymptotic numerics;
- **B15 BREAK THE SYMMETRY ON PURPOSE:** perturb the `0<->1` symmetry after the exact case is understood, to decide whether the obstruction is structural or a symmetry degeneracy;
- **B28 REPLACE FOR ALL WITH FOR TYPICAL:** if the universal hitting comparison fails, identify the exact margin/nonvacuity condition under which a restricted threshold-matched theorem might still hold; any such result remains PARTIAL and cannot move the frozen full-class factor unless it feeds a new full-class characterization.

## 13. Directed second-audit duty — C29

I audited C29's actual newest theorem-sized claim, not an older one-defect result:

`proofnet24/C29-closure-brownian-shapes/runs/2026-09-16/2026-09-16T22-35-54Z__dc34-centered-two-defect-exact-hull.md`.

Verdict:

\[
\boxed{\texttt{C28-AUDIT-C29-DC34-CENTERED-TWO-DEFECT-10 = PASS}}
\]

**claim-scoped**.

The audited setup has `alpha>1`, centered spike `delta>1/4`, `q=4 delta-1>0`, and two defective mixed cells. I independently checked the following parts against the report and the archived symbolic checker:

1. On every fixed third-direction line `t=r-alpha s`, each defective restriction is a convex quadratic with coefficient `alpha q`, and the asserted endpoint chord correction
   \[
   \alpha q(s-s_0)(s_1-s)
   \]
   reproduces all six stated replacement formulas.

2. The linewise slope gaps have the asserted signs on the **actual existence domains** of the regimes. In particular the northwest-to-middle and middle-to-southeast gaps reduce to the recorded factors involving `r-1/2`, `r-alpha/2`, `alpha+2-2r`, `alpha-r`, and `alpha+1/2-r`; the central-line jump is downward. Hence no longer chord spanning both defects is forced.

3. In every formula region `partial_ss V=0`, while the only nonzero pure `t`-second derivatives are `-2q/alpha` in the two middle chord regimes. The four slanted regime-change factorizations give downward coordinate derivative jumps on their stated sign domains.

4. Across `s=1/2` and `t=1/2`, the coordinate derivative jumps are also downward. The two middle-regime inequalities use precisely the geometric existence bounds `s>=1/(2 alpha)` and `s<=1-1/(2 alpha)`; these are present in the checker and close the only nontrivial signs.

5. Therefore the constructed `V` is separately concave in the three prescribed directions. Minimality follows because every `D`-concave majorant must first dominate the coordinatewise envelope `U`, and then on every third-direction line dominate the least concave majorant just verified. Together with the previously established lower-envelope dependency, this yields the claimed centered five-point semialgebraic, finitely laminated hull.

The archived checker code at

`proofnet24/C29-closure-brownian-shapes/artifacts/2026-09-16T22-35-54Z__centered_two_defect_symbolic.py`

matches these identities, and its archived output ends `ALL_EXACT_SYMBOLIC_CHECKS_PASS`.

This PASS covers **only** `C29-DC34-CENTERED-TWO-DEFECT-SEMIALGEBRAIC-09`: the centered two-defect five-point semialgebraic/finitely-laminated hull. It does **not** settle Randomstrasse Conjecture 34, does not move C29's frozen metric, and does not certify C29 admission/READY status or any asymmetric two-defect family not covered by the theorem.

## 14. ledger_delta for P26

```text
track=C28
target=I0032 / Aldous-Fill Open Problem 8.23
source_parameter=s_*:=inf{s>=0: ||P_s||_{2->infinity}<=2}=tau_2(sqrt(3))
source_class=finite irreducible reversible continuous-time chains
frozen_candidate=S_anch,2(E) / binary state-anchored dyadic local-spectral threshold
metric_before=2
metric_after=2
movement=no movement
unchanged_run_count_before=3
unchanged_run_count_after=4
protocol=STUCK / THINKING-ONLY; no new C28 theorem claim
moves_used=7,12,29
selected_section_I_action=refute instead of prove
strategy_diagnostic=symmetric three-state family with rare-cluster mass p>1/4 appears to make s_*/rho^(sqrt(3)) unbounded; NOT PROMOTED AS A CLAIM THIS RUN
next_moves=2,15,28
status=PARTIAL / CLAIMED / PENDING_ADMISSION / NOT READY
paley_etf_reserve=unchanged; kappa_*=6.6575355565204281495... at (73,14), existential quantifier correction preserved
second_audit=C28-AUDIT-C29-DC34-CENTERED-TWO-DEFECT-10=PASS claim-scoped
shared_ledger_edit=none
peer_file_edit=none
```

## 15. Model / scheduler control

Actual runtime metadata available to this report identifies GPT-5.6 Sol; reasoning effort is UNVERIFIED. The exposed task-control interface still has task text/title, timing/schedule, enabled state and notification controls, but no model-family selector and no reasoning-effort selector. Therefore `GPT-6 / maximum` remains prompt-only rather than enforceable here. Making it enforceable requires scheduler/backend or enclosing-runtime support that exposes, persists, and verifies those fields. A historical `You cannot modify this task` response is an ownership/permission-context boundary; the supported workaround is authorized owner/admin/coordinator action in the owning workspace or platform support, never a permission bypass or duplicate task.
