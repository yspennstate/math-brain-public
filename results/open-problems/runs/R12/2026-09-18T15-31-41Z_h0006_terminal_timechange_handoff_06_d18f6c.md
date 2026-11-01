Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO MOVEMENT: H0006 `FSS_layers = 2/3 -> 2/3`; FINAL POST-RECOVERY H0006 EXECUTION ATTEMPT, followed by TERMINAL HANDOFF. Methods actually used: #5 ADD A PARAMETER AND DIFFERENTIATE/RESCALE, #7 TAKE THE LIMIT, #22 READ THE FAILURES.**

# R12 HARD OUTSIDE — H0006 final post-recovery attempt: exact clock-scaling symmetry exposes a source first-passage formula error; terminal handoff

Repository / branch: private `yspennstate/math-open-problems`, `master`.
Deployment: `NEW-METHODS-2026-09-16`.
Run status after this report: **H0006 OPEN / PARTIAL / TERMINAL_HANDOFF**.
Frozen metric before/after: **`FSS_layers = 2/3 -> 2/3`**.
Canonical claim at run start: `operations/claims/H0006.md`.
Next H0006 recovery permitted for R12: **false**.
Rotation disposition after the handoff: **`ROTATION_WAIT / NO_SUCCESSOR_CLAIMED`** after a fresh ownership/admission sweep described below.

This report is the single post-recovery execution attempt authorized by

`runs/R12/2026-09-18T14-39-33Z_h0006_stuck_recovery_02_b6f82d.md`.

That report used the second and final Section-I recovery and reserved methods #5/#7/#22. It stated that if the attempt did not move layer 3, H0006 must be terminally handed off rather than receive a third stuck recovery. I obey that instruction here. I do **not** reopen the stale native-title target I0102/Randomstrasse Conjecture 28, which R12 already terminally handed off with best R12 uniform certificate `(a,C,p0)=(1/2,1,5)`, and I do not reopen the terminal I0115 line.

---

## 1. Required continuity and source/current-status checks

Before new reasoning I recovered the current campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the H0006 claim, the newest R12/H0006 report, and current neighboring/ownership records. Root `RESULTS.md` still contains an old R12/I0102 row, but the controlling policy says to recover the newest complete own-track report rather than reset to a stale shared-root row.

The exact H0006 source remains Achyut Kumar, *Threshold cascades of interacting diffusions on unimodular random trees: a conditional branching-process universality theorem, the annealed pressure, and the dimension of the failed boundary*, arXiv:2608.15987v1, submitted 17 August 2026. Section 12.3 open problem (4) still reads, in substance, “Finite-size scaling on `G_n`. Quasi-stationary theory for the cutoff `xi=(1-rho(M))^{-1}` against the finite size `n`; the window near criticality.” The arXiv record still exposes only v1 in the bounded 18 September check.

The later Kumar–Duddala companion arXiv:2608.21125v1 (21 August 2026) treats front propagation/Bramson correction and continuous-type limit theory. Its stated scope does not close finite-size scaling on `G_n`.

The frozen H0006 metric remains the number of three nested source-valid finite-size layers proved with an explicit crossover law:

1. one-type Bethe/Galton–Watson subclass — done;
2. general finite-type Galton–Watson skeleton — done;
3. the actual finite-graph interacting-diffusion cascade on `G_n`, uniformly through the relevant near-critical window — not done.

Thus the honest metric entering this report is `2/3`.

---

# 2. Method #5 — add a clock-speed parameter: exact symmetry of the source SDE

The previous recovery proposed making the one-contact killed OU dynamics “fast” relative to the critical finite-population frontier and then averaging the once-contacted reservoir toward a quasi-stationary profile. The first thing to test is whether the source model actually contains such a free fast parameter.

In the homogeneous one-type notation, the source SDE is

\[
 d s_t^{(v)}=
 \left[-\alpha s_t^{(v)}+\gamma\sum_{u\sim v}\sigma(s_t^{(u)}-\theta_{uv})\right]dt
 + b\,dW_t^{(v)}.
\tag{2.1}
\]

More generally each type has its own `alpha_d,b_d,gamma_{d->d'}`; the following argument applies after multiplying all rates by the same positive constant.

Fix `c>0` and define a new parameter family

\[
\alpha^{(c)}=c\alpha,\qquad
\gamma^{(c)}=c\gamma,\qquad
b^{(c)}=\sqrt c\,b,
\tag{2.2}
\]

with thresholds, initial states and the graph unchanged. If `s` solves (2.1), set

\[
Y_t^{(v)}:=s_{ct}^{(v)}.
\]

Brownian scaling gives `B_t^{(v)}:=c^{-1/2}W_{ct}^{(v)}` as independent standard Brownian motions, and therefore

\[
 dY_t^{(v)}=
 \left[-c\alpha Y_t^{(v)}+c\gamma\sum_{u\sim v}\sigma(Y_t^{(u)}-\theta_{uv})\right]dt
 +\sqrt c\,b\,dB_t^{(v)}.
\]

Hence

\[
\boxed{
\{s_t^{(c)}:t\ge0\}\ \stackrel{d}=\ \{s_{ct}:t\ge0\}.
}
\tag{2.3}
\]

This is an exact path-law identity, not an asymptotic statement. In particular every threshold-crossing order, the eventual failed cluster, and every event that ignores the absolute physical clock are invariant under (2.2). The failure times are simply divided by `c`.

The source's dissipative ratio is also invariant:

\[
\kappa^{(c)}
=\frac{c\gamma L_\sigma\Delta}{c\alpha}
=\kappa.
\tag{2.4}
\]

For the directed OU edge problem the equilibrium shift is `m=c_uv/alpha`; because the forcing `c_uv` scales with `gamma`, both numerator and denominator acquire the same factor `c`, so `m` is invariant. Likewise

\[
\mu=\frac{b^2}{2\alpha}
\]

is invariant under (2.2).

### Consequence for the proposed QSD shortcut

The most obvious “take alpha large” version of the previous recovery is therefore a gauge transformation if the dimensionless cascade law is kept fixed: increasing all dynamical rates as in (2.2) merely changes the physical clock. It cannot create new mixing **relative to the cascade itself**, because the second-contact times, killed-OU relaxation and threshold events are all accelerated by the same factor.

One can instead send `alpha` to infinity while leaving `gamma,b` fixed, but that changes `kappa`, the equilibrium shifts, noise scale and transmission probabilities, hence moves to a different source parameter family. Retuning thresholds/noise/coupling to stay near `rho(M)=1` is a genuine additional singular double scaling. A theorem in such a family could be an interesting restricted result, but it would not establish layer 3 of the frozen H0006 metric for the source's fixed-dynamics finite-size window.

So method #5 does not close the layer, but it identifies a real obstruction: **the source has no free common-speed parameter that makes the survivor reservoir fast while leaving the critical cascade law unchanged.**

---

# 3. A stronger exact diagnostic found by #5: equation (3) as printed is inconsistent with the SDE

The clock symmetry gives an immediate internal check on the source's displayed directed first-passage formula. This check uncovered a source-level formula problem that should be preserved for any future H0006 worker.

The source writes the directed OU process as

\[
 dX_t=-\alpha(X_t-m)dt+b\,dW_t,
\qquad \mu=\frac{b^2}{2\alpha},
\tag{3.1}
\]

and its equation (3) displays a two-boundary hitting probability using

\[
W(z;h)=\int_0^h e^{-\alpha y^2/\mu}\,dy.
\tag{3.2 source display}
\]

As printed, (3.2) cannot be the exact hitting formula for (3.1).

There are two independent exact reasons.

## 3.1 Generator/scale-function derivation

Let `a<x<bnd` be the lower and upper boundaries and

\[
u(x)=\Pr_x(\tau_{bnd}<\tau_a).
\]

Then `u` solves the elementary boundary-value problem

\[
\frac{b^2}{2}u''(x)-\alpha(x-m)u'(x)=0,
\qquad
u(a)=0,\quad \nu(bnd)=1.
\tag{3.3}
\]

Since `b^2/2=alpha mu`, division by `alpha` gives

\[
\mu u''(x)-(x-m)u'(x)=0.
\]

Putting `v=u'`,

\[
\frac{v'(x)}{v(x)}=\frac{x-m}{\mu},
\]

so

\[
 v(x)=C\exp\!\left(\frac{(x-m)^2}{2\mu}\right).
\]

Imposing the two boundary values yields the exact formula

\[
\boxed{
\Pr_x(\tau_{bnd}<\tau_a)
=
\frac{\displaystyle\int_a^x
 \exp\!\left(\frac{(y-m)^2}{2\mu}\right)dy}
{\displaystyle\int_a^{bnd}
 \exp\!\left(\frac{(y-m)^2}{2\mu}\right)dy}.
}
\tag{3.4}
\]

This is the usual scale-function formula for a stable OU diffusion. The exponent has the opposite sign from the source display and, after writing `mu=b^2/(2 alpha)`, contains no separate extra factor `alpha/mu` of the form shown in (3.2).

## 3.2 Exact clock-invariance check

Under the exact symmetry (2.2), `m` and `mu` remain fixed, so the true hitting probability (3.4) is invariant, as it must be because the primed process is only a time change.

By contrast the source display (3.2) contains `alpha/mu`. Under (2.2), `alpha/mu` is multiplied by `c` although all barrier distances and `m,mu` are unchanged. Thus the printed formula changes under a transformation that provably changes only the clock. This is an immediate contradiction.

Accordingly:

\[
\boxed{
\text{Equation (3) in arXiv:2608.15987v1, as displayed, has a sign/normalisation/integration-form error.}
}
\tag{3.5}
\]

This statement concerns the **printed auxiliary formula**, not H0006 itself. It does not refute the finite-size-scaling open problem.

---

# 4. Method #7 — take the limit: the printed small-noise Laplace step also fails as written

The source's Proposition 10.1 makes the inconsistency even more visible. It writes, for `lambda=alpha/mu`, an integral of the form

\[
\int_0^h e^{-\lambda y^2}\,dy
\]

and then says this integral is dominated by its upper endpoint, giving

\[
\frac{1}{2\lambda h}e^{-\lambda h^2}.
\tag{4.1 source proof step}
\]

For fixed `h>0` this is not the asymptotic of the displayed integral. Exactly,

\[
\int_0^h e^{-\lambda y^2}\,dy
=\lambda^{-1/2}\int_0^{h\sqrt\lambda}e^{-z^2}\,dz,
\]

hence as `lambda->infinity`,

\[
\boxed{
\int_0^h e^{-\lambda y^2}\,dy
\sim \frac{\sqrt\pi}{2\sqrt\lambda}.
}
\tag{4.2}
\]

The expression in (4.1) is instead the familiar leading asymptotic for a **Gaussian tail** `int_h^infinity e^{-lambda y^2}dy`, not for an integral beginning at zero. Thus Proposition 10.1's displayed endpoint-Laplace step is false as written.

This is useful for H0006 continuity because the source itself uses equation (3) to map SDE parameters to the entries of `M`. The branching-process statements that depend only abstractly on a valid matrix `M` and its Perron root can be reformulated after correcting the edge hitting probabilities, but any numerical or small-noise formula that uses the printed (3) must be rechecked. In particular, R12's layer-1/layer-2 finite-size exponents were derived from the branching law as a function of `rho(M)` and do **not** require the erroneous printed OU integral; those exponents are not withdrawn by this diagnostic.

A future source-level audit should distinguish three statements:

1. the SDE itself (well-defined);
2. the correct OU scale-function hitting probability (3.4);
3. the source's displayed equation (3) / Proposition 10.1 asymptotic (requires correction).

I did not find a later arXiv version correcting this in the bounded 18 September search. This is not a claim about worldwide novelty; it is an exact consistency check against the current v1.

---

# 5. Why the `c->infinity` limit does not provide layer 3

Taking the common-speed parameter `c->infinity` in (2.2) looks at first like the desired fast-mixing limit, but (2.3) shows it is exactly trivial after rescaling time. The path in state space and the sequence of failures do not change in law.

Therefore an averaging proof for the once-contacted survivor reservoir cannot be justified by saying merely that OU mean reversion is fast. What matters is a **relative** spectral gap between survivor-state relaxation and the arrival of later failed-neighbor contacts in the same dimensionless time units. Common acceleration leaves that ratio unchanged.

A genuine fast-slow theorem would need an additional small parameter `epsilon` entering schematically as

\[
\mathcal G^{(\epsilon)}
=\epsilon^{-1}\mathcal G_{\rm survivor}
+\mathcal G_{\rm front}
\]

while preserving the source-critical one-parent transmission law to leading order. No such separation follows from `N->infinity` or from the common OU clock parameter alone.

The previous recovery's desired state-space-collapse estimate

\[
\mu_N(t)=W_N(t)\nu_t+\mathcal E_N(t),
\qquad \|\mathcal E_N(t)\|=O_P(N^{1/3}),
\]

therefore remains an unsupported target in the fixed source model. The present run found no mechanism forcing it at the needed scale.

---

# 6. Method #22 — read the failures: what the closest solved theories have that H0006 lacks

The source itself gives the sharpest description of its current failure. Theorem 11.5 proves dissipative front decoupling with a cluster-volume accumulation factor and, at criticality conditioned on cluster size `n`, requires a joint limit of the form

\[
 n\,\varepsilon(\delta_n)\to0.
\]

Immediately afterward the paper states that uniformity through the critical window would require replacing the cluster-volume factor `n` by the active-front width `sqrt(n)` and says explicitly that the exploration telescoping does not see this improvement. Thus the missing estimate is already recognized by the source: the problem is not another GW asymptotic, but a front-local error accounting theorem.

The previous R12 recovery compared this with Florian Simatos, *State space collapse for critical multistage epidemics*, Adv. Appl. Probab. 47 (2015), 715–740. Simatos has a finite-dimensional staged epidemic state and proves a critical diffusion approximation with genuine state-space collapse. That proof has an explicit population-scaled slow manifold. Kumar's finite-graph SDE instead carries continuous survivor states and adaptive reinjection/second-contact histories; R12 has not produced an intrinsic manifold contraction at the `N^{-1/3}` characteristic-error scale.

Quasi-stationary killed-diffusion theory can prove convergence of normalized killed-process laws or regenerated empirical occupation measures under appropriate assumptions, but that is not by itself the needed statement here. The reservoir is continuously and adaptively injected by the same critical front whose statistics we are trying to derive. The common-speed symmetry above also shows that simply increasing `alpha` at fixed dimensionless cascade parameters does not create the absent separation.

So the nearest solved theories contain one of two ingredients that H0006 still lacks:

- an explicit finite-dimensional population state with a provable collapse manifold; or
- an externally imposed fast-slow scaling that makes averaging rigorous.

The source model, at fixed near-critical dynamics, has neither ingredient currently proved.

---

# 7. Final status of the layer-3 obligation

The exact layer-3 blocking statement inherited from the two stuck recoveries remains unchanged. For a source-valid finite-population frontier coordinate `A_N(j)` tuned by

\[
N^{1/3}(\rho(M_N)-1)\to\lambda,
\]

one still needs, through `j<=T N^{2/3}`,

\[
\sup_{j\le TN^{2/3}}
\left|
\mathbb E[\Delta A_N(j)\mid\mathcal F_j]
-c_1(\rho(M_N)-1)-\Gamma_2\frac jN
\right|
=o_P(N^{-1/3}),
\tag{7.1}
\]

and

\[
\sup_{j\le TN^{2/3}}
\left|
\operatorname{Var}(\Delta A_N(j)\mid\mathcal F_j)-\sigma^2
\right|
=o_P(1),
\tag{7.2}
\]

plus Lindeberg/tightness and control/collapse of the source's continuous history state.

The present run neither proves (7.1)–(7.2) nor finds a substitute that implies them. The common-clock deformation does not create a fast variable, and the source's own critical-window proof still accumulates the error over cluster volume instead of front width.

Therefore the frozen metric honestly remains

\[
\boxed{FSS_{\rm layers}=2/3\longrightarrow2/3.}
\]

No narrower fast-slow family, source-formula correction, or auxiliary OU lemma is relabelled as layer 3.

---

# 8. Terminal H0006 handoff

This was the one permitted post-recovery execution attempt after Section-I recovery 2 of 2. It did not move the frozen metric. Under the owner's HARD-target protocol, R12 may not run a third H0006 stuck recovery or continue manufacturing auxiliary lemmas on the same source obligation.

**Terminal disposition:**

- source problem: **OPEN**;
- R12 result: **PARTIAL** (`2/3` layers);
- R12 status on H0006 after this report: **TERMINAL_HANDOFF**;
- `next_H0006_recovery_permitted_for_R12: false`;
- exact new handoff fact: common-rate acceleration is only a time change and cannot supply QSD/front timescale separation;
- exact source correction: equation (3) and the Proposition 10.1 Gaussian-integral step are inconsistent with the displayed OU SDE as written;
- remaining source-valid obligation: derive the finite-population predictable characteristics/front-width error control for the actual interacting diffusion, retaining the contact-history state or proving a genuine source-intrinsic collapse mechanism.

A fresh future assignee should **not** restart with the scalar second-contact surrogate, whole-cluster TV to an infinite GW tree, or “take alpha large” without first specifying a nontrivial dimensionless fast-slow scaling. The most promising genuinely new route would be a direct measure-valued martingale problem for the contact-age/state reservoir, or a front-local influence decomposition that achieves the source's requested `sqrt(n)` rather than `n` accumulation.

---

# 9. Rotation / admission screen after terminal handoff

I performed the required current ownership screen rather than stealing a merely PENDING queue row. The current root queue still says newly certified READY entries are zero and that PENDING is not dispatch authority. A direct current sweep found, among the plausible HARD/CLOSABLE rows near the front:

- `I0078` — canonical claim exists, owned by C27;
- `I0035` — provisional exclusive reservation exists, owned by C31;
- `I0068` — canonical claim exists, owned by P19;
- `I0066` — canonical claim exists, owned by P15;
- `I0007` — canonical HARD claim exists in another native slot;
- `I0008` — canonical HARD claim exists in another native slot;
- `I0061` — already received a multi-run attempt and terminal rotation/handoff in another track; not a fresh successor;
- `I0062` — canonical claim exists in another track;
- `I0048` — substantial R08 work/current gate records already exist; not fresh unowned inventory;
- `I0050` — no canonical claim was found, but current queue/gate records explicitly reject the queued scope as a clean fresh successor because later work/source-scope issues remain unresolved.

I therefore did **not** create a fictitious successor claim. R12 leaves this run in

`ROTATION_WAIT / NO_SUCCESSOR_CLAIMED`.

The next R12 invocation must continue successor admission from an unscreened or materially changed HARD OUTSIDE candidate, checking exact source, current primary literature, later-author papers, prior attempts, aliases and exclusive ownership before any create-only claim. It must not resume H0006, I0115, I0102, or the earlier excluded R12 I0060 line without an explicit new owner instruction.

---

# 10. Method accounting

## #5 ADD A PARAMETER AND DIFFERENTIATE/RESCALE

**Tried:** introduce the common dynamical speed `c` in `alpha,gamma,b` and see whether increasing OU relaxation yields a QSD averaging parameter.

**Outcome:** exact Brownian time-change identity (2.3). The parameter is a clock gauge at fixed dimensionless cascade law, not a source of relative mixing. It also exposes the printed first-passage formula inconsistency.

## #7 TAKE THE LIMIT

**Tried:** `c->infinity` and the source's printed `lambda->infinity` first-passage asymptotic.

**Outcome:** the common-speed limit is exactly trivial after time rescaling; separately, the displayed Gaussian integral in Proposition 10.1 has the wrong endpoint asymptotic as written. No finite-size layer is gained.

## #22 READ THE FAILURES, NOT THE SUCCESSES

**Tried:** compare the remaining bridge with the source's own critical-window failure and with state-space-collapse/QSD literature.

**Outcome:** the missing ingredient is not a further branching theorem. It is front-local predictable-characteristics control or an actual collapse theorem for the continuous contact-history reservoir. Existing solved models supply a finite-dimensional collapse state or an external fast-slow parameter; H0006 currently supplies neither at fixed source dynamics.

No exact-arithmetic checker was created because the substantive new claims are symbolic Itô/time-change and ODE/scale-function identities valid for all positive parameters, with no finite computational core.

---

# 11. Prior-art / novelty discipline

Fresh bounded search on 18 September 2026 covered:

- the current arXiv record for Kumar, arXiv:2608.15987v1 (17 Aug 2026);
- Kumar–Duddala, arXiv:2608.21125v1 (21 Aug 2026);
- Simatos, *State space collapse for critical multistage epidemics*, Adv. Appl. Probab. 47 (2015), 715–740;
- standard OU first-passage / scale-function literature, including older Ricciardi–Sato/Nobile–Ricciardi–Sacerdote lines and modern OU first-passage work;
- killed-diffusion quasi-stationary approximation literature.

The scale-function solution (3.4) and Brownian time-rescaling mechanism are classical diffusion facts. I make **no novelty claim** for either. The fleet-relevant point is only that applying these classical checks to the current source v1 reveals an internal inconsistency in the printed directed hitting formula and invalidates the proposed “common alpha speedup gives new QSD separation” route.

A negative bounded search is not a worldwide novelty certificate.

---

# 12. Model/scheduler control and historical P26 permission issue

The control limitation remains exactly as the repository policy records it. The exposed scheduled-task interface provides prompt/title, schedule/timing, timing mode and enablement controls, but no binding model-family field, no reasoning-effort field and no authenticated completed-run telemetry. Thus `GPT-6 / maximum` remains a request in prompt text only. This report truthfully records the model surfaced in this run as GPT-5.6 Sol and the reasoning level as UNVERIFIED.

Making GPT-6/maximum enforceable would require product/runtime support for binding model and reasoning selectors plus authenticated per-run applied-model/effort telemetry. A repository prompt edit cannot supply that guarantee.

The historical P26 native response `You cannot modify this task` is an authorization/context boundary, not something to bypass. The legitimate workaround is an authorized owning account/workspace/context or platform support. Current root history also records that P26 was later successfully updated from another authorized context; a denial in one context does not authorize duplicating the schedule or changing permissions.

No scheduler state, email, Drive item, public posting, purchase, permission, workflow or peer-track file was changed in this run.

---

## Structured `ledger_delta`

```yaml
ledger_delta:
  track: R12
  category: HARD_OUTSIDE
  target_before: H0006
  source: arXiv:2608.15987v1 Section 12.3 Open Problem (4)
  metric: FSS_layers
  before: "2/3"
  after: "2/3"
  movement: none
  methods: [5, 7, 22]
  substantive_new_fact:
    - "common scaling alpha->c alpha, gamma->c gamma, b->sqrt(c)b is an exact time change"
    - "source equation (3) / Proposition 10.1 Gaussian-integral step is inconsistent with the displayed OU SDE as written"
  source_problem_status: OPEN
  r12_scope_status: PARTIAL
  handoff: TERMINAL_HANDOFF
  recovery_count_completed: 2
  post_recovery_execution_completed: true
  next_H0006_recovery_permitted_for_R12: false
  successor_claimed: false
  rotation_status: ROTATION_WAIT_NO_SUCCESSOR_CLAIMED
  next_action: "screen an unscreened/materially-changed HARD OUTSIDE candidate; do not resume H0006/I0115/I0102"
  shared_root_edit: false
  peer_file_edit: false
  scheduler_change: false
```
