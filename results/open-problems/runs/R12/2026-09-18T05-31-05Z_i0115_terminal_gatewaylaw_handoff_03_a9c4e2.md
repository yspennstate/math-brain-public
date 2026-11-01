Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested in prompt text, but the exposed runtime does not provide authenticated applied-model/reasoning-effort telemetry or a binding model/reasoning selector, so I do not claim GPT-6 / maximum. **NO MOVEMENT: I0115 `K_explicit=1 -> 1`; FINAL ALLOWED I0115 RESEARCH ATTEMPT, followed by TERMINAL HANDOFF. Methods actually used: #8 DISCRETIZE, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #25 COUNT THE SAME THING TWICE.**

# R12 / I0115 — exact conditional gateway law inside the published Poisson-road master event; terminal HARD handoff

Repository / branch: `yspennstate/math-open-problems`, `master`.
Deployment: `NEW-METHODS-2026-09-16`.
Status after this run: **OPEN / PARTIAL / TERMINAL_HANDOFF**.
Canonical active claim at run start: `operations/claims/I0115.md`.

## 1. Continuity: do not reopen the stale Paley title

The native task text still names Randomstrasse Conjecture 28 / I0102, but the newer immutable R12 history controls. The I0102 terminal handoff

`runs/R12/2026-09-17T22-49-01Z_i0102_terminal_stuck_handoff_15_8e3a71.md`

froze the best R12 uniform certificate at `(a,C,p0)=(1/2,1,5)` and recorded `next_I0102_recovery_permitted: false`. R12 subsequently claimed I0115, Aldous's SIRSN Open Problem 27, by the create-only file `operations/claims/I0115.md`. I therefore do **not** reopen Paley and do not reset any I0102 stagnation count.

The active frozen I0115 metric is

`K_explicit` = largest `k>=1` for which one single genuine SIRSN has a proved explicit full law of every `span(z1,...,zj)`, `1<=j<=k`, for every deterministic general-position configuration, consistently in `j`.

Before this run: `K_explicit=1`.
After this run: `K_explicit=1`.

The immediately preceding report

`runs/R12/2026-09-18T04-32-03Z_i0115_stuck_recovery_02_6d9b41.md`

was **STUCK RECOVERY 2 OF AT MOST 2**. It selected one final source-relevant special case: extract a canonical one-annulus gateway for the actual Kahn/Kendall geodesic, defined by finite Poisson line/speed windows, and compute its conditional law explicitly. It reserved moves #8/#17/#25 and stated that if this attempt failed to move `K_explicit`, I0115 must be terminally handed off rather than receive a third stuck recovery. This run obeys that instruction.

## 2. Required repository / source recovery

Before new reasoning I reread or recovered the current campaign index and ranking, root `POSTED.md`, root `RESULTS.md`, current `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the I0115 claim, the latest R12 report, neighboring I0115 screening records, and the earlier I0102 terminal handoff. Root `RESULTS.md` still contains the older frozen R12/I0102 line, but the owner policy expressly requires continuing from newer complete own-track reports and create-only claims rather than overwriting history from a stale root row.

Fresh source/literature check dated 2026-09-18 recovered Blanc--Curien--Kahn, *Geodesics in planar Poisson road random metric*, Proc. London Math. Soc. 131 (2025), e70070. Their Lemma 5 master event already proves substantially more geometry than my previous stuck report had credited to an explicit finite-window construction: on a positive-probability event `G`, there is a **unique** fast road `(ell_0,v_0)` crossing two prescribed small balls, and every actual geodesic crossing the relevant annulus drives along this road through a canonical cut point `z`, the orthogonal projection of `e1/2` onto `ell_0`.

Crucially, the paper rewrites the master event as

`G = (Gamma<=t) ∩ Inner ∩ Outer ∩ Junction' ∩ D ∩ E`,

where `Junction'` is the event that there is exactly one road with speed in `[24,25)` crossing the two prescribed balls, and explicitly states that these six events are independent. Thus the conditional distribution of the canonical cut point on `G` can be extracted exactly from the single Poisson atom in `Junction'`. I did not find that explicit formula stated in the paper during the bounded search; that is **not** a novelty certificate.

## 3. New exact consequence: closed-form law of the published canonical gateway on `G`

Everything in this section is a direct Poisson/integral consequence of the published master-event construction. It is not asserted to be a new theorem of the Poisson-road model.

Work in the planar model (`d=2`) with the normalization of Blanc--Curien--Kahn. Let

`a = 2/3`

and let `delta` be the small radius used for their two Junction balls centered at `-a e1` and `+a e1`.

Parameterize an unoriented line, up to the usual null boundary identifications, by

\[
\ell_{\theta,s}=\{x\in\mathbb R^2:x\cdot n_\theta=s\},
\qquad n_\theta=(\cos\theta,\sin\theta),
\qquad 0\le \theta<\pi.
\]

Their invariant line measure satisfies `mu(<B(0,r)>)=2r`, hence in these coordinates

\[
\boxed{\mu(d\ell)=\frac1\pi\,d\theta\,ds.}
\]

Indeed, integrating over `|s|<=r` gives `(1/pi)*pi*(2r)=2r`.

Define the geometric Junction line set

\[
A_\delta=\{\ell:\ell\cap \overline B(-ae_1,\delta)\ne\varnothing,
\ \ell\cap \overline B(ae_1,\delta)\ne\varnothing\}.
\]

A line `ell_{theta,s}` lies in `A_delta` iff

\[
|s-a\cos\theta|\le\delta,
\qquad |s+a\cos\theta|\le\delta.
\]

Equivalently,

\[
|\cos\theta|\le \frac\delta a,
\qquad
|s|\le \delta-a|\cos\theta|.
\]

Put

\[
\varepsilon=\frac\delta a=\frac{3\delta}{2},
\qquad
\alpha=\arcsin\varepsilon.
\]

The exact line measure of `A_delta` is therefore

\[
\begin{aligned}
M_\delta:=\mu(A_\delta)
&=\frac1\pi\int_0^\pi 2(\delta-a|\cos\theta|)_+\,d\theta\\
&=\boxed{\frac4\pi\left[\delta\arcsin\!\left(\frac{3\delta}{2}\right)
-\frac23\left(1-\sqrt{1-\frac{9\delta^2}{4}}\right)\right]}.
\end{aligned}
\]

### Proof of the integral

By symmetry about `pi/2`, the support in the first half interval is `theta in [arccos(epsilon), pi/2]`; hence

\[
\int_0^\pi 2(\delta-a|\cos\theta|)_+d\theta
=4\int_{\arccos\varepsilon}^{\pi/2}(\delta-a\cos\theta)d\theta.
\]

Since `pi/2-arccos(epsilon)=arcsin(epsilon)` and `sin(arccos epsilon)=sqrt(1-epsilon^2)`, the displayed formula follows.

The planar road intensity is

\[
\nu=c\,\mu(d\ell)\,v^{-\beta}dv,
\qquad
c=\kappa_1^{-1}(\beta-1)=\frac{\beta-1}{2},
\qquad \beta>2.
\]

Therefore the Poisson mean of roads in the exact Junction window

\[
A_\delta\times[24,25)
\]

is

\[
\begin{aligned}
\Lambda_J
&=\frac{\beta-1}{2}M_\delta\int_{24}^{25}v^{-\beta}dv\\
&=\boxed{\frac{M_\delta}{2}
\left(24^{1-\beta}-25^{1-\beta}\right)}.
\end{aligned}
\]

Thus the exact probability of the published event `Junction'` (exactly one atom in this window) is

\[
\boxed{\mathbb P(\mathsf{Junction}')=\Lambda_J e^{-\Lambda_J}.}
\]

Conditioned on `Junction'`, let `(Theta,S,V)` be the unique atom. The line geometry and speed are independent, and their exact laws are

\[
\boxed{
f_\Theta(\theta)=\frac{2(\delta-a|\cos\theta|)_+}{\pi M_\delta},
\quad 0\le\theta<\pi,
}
\]

\[
\boxed{
S\mid \Theta=\theta\sim
\mathrm{Unif}\big[-(\delta-a|\cos\theta|),\ \delta-a|\cos\theta|\big],
}
\]

and

\[
\boxed{
f_V(v)=
\frac{(\beta-1)v^{-\beta}}
{24^{1-\beta}-25^{1-\beta}},
\quad 24\le v<25.
}
\]

The canonical gateway in the published proof is the orthogonal projection of

\[
q=\frac12e_1
\]

onto `ell_{Theta,S}`. Hence it has the explicit sampling formula

\[
\boxed{
Z=q+\left(S-\frac12\cos\Theta\right)
(\cos\Theta,\sin\Theta).
}
\]

This is already an explicit full pushforward description of the gateway location.

## 4. Why conditioning on the *entire* master event does not alter this law

Blanc--Curien--Kahn explicitly decompose their master event into the intersection of six independent events:

\[
G=(\Gamma\le t)\cap \mathsf{Inner}\cap\mathsf{Outer}
\cap\mathsf{Junction}'\cap D\cap E.
\]

The unique Junction atom `(Theta,S,V)`, and therefore `Z`, is measurable with respect to the Poisson restriction to `A_delta × [24,25)`. The five other displayed factors are measurable with respect to disjoint Poisson restrictions (or the independent low-speed part used for `Gamma`) exactly as arranged in their proof. Therefore, for every bounded measurable test function `F`,

\[
\begin{aligned}
\mathbb E[F(\Theta,S,V,Z)\mid G]
&=\mathbb E[F(\Theta,S,V,Z)\mid \mathsf{Junction}'].
\end{aligned}
\]

Thus

\[
\boxed{
\mathcal L(\Theta,S,V,Z\mid G)
=\mathcal L(\Theta,S,V,Z\mid\mathsf{Junction}')
}
\]

with the closed forms above.

This completes the exact conditional-gateway-law special case selected by STUCK2. It is a genuine advance in the **explicitness of the handoff state** relative to the preceding R12 reports, but it does **not** move the frozen source metric: it describes the actual geodesic only on one positive-probability master event, not the complete law of `span(z1,z2)`.

## 5. #8 DISCRETIZE — what worked and what failed

The intended #8 move was to replace the non-explicit low-speed travel control in the published event by a finite deterministic connector scaffold. The finite-window part works better than expected: `Junction'`, `D`, `E`, `Inner`, and `Outer` are already formulated by finitely specified geometric line/speed windows, and the Junction variable reduces to the two continuous coordinates `(theta,s)` plus one speed coordinate. This is enough to compute its law exactly; no numerical discretization is needed.

But a **finite road scaffold cannot replace `Gamma` for the uniform endpoint-access statement used by the master event**. The reason is geometric and exact. A finite union of affine roads is a closed set of two-dimensional Lebesgue measure zero and meets a boundary circle in finitely many points unless a degenerate coincidence occurs. The master-event bound must connect **every** boundary point `x` to nearby scaffold/ring-road points in the Poisson-road metric. A generic boundary point lies on none of finitely many prescribed roads. In Kendall's metric, access from such a point is achieved by an infinite accumulation of roads of successively smaller speeds near the endpoint, precisely the low-speed environment controlled by `Gamma`; there is no positive off-road speed that a finite deterministic road graph could use to start from an arbitrary generic `x`.

So the finite-scaffold replacement fails for a structural reason: finite Poisson occupancy windows can force the macroscopic bottleneck, but they cannot uniformly supply microscopic access from a continuum of possible endpoints. Any exact replacement must itself be countably multiscale (or summarize that infinite low-speed environment by a new random variable with an explicit law).

This failure is the key terminal obstruction to turning the one-shell formula into a finite-state regeneration kernel.

## 6. #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE — Poisson records versus genuine renewal

The Junction atom is exactly a finite-window Poisson record/top-atom object. Its mean `Lambda_J`, its exactly-one probability `Lambda_J exp(-Lambda_J)`, and its conditional atom law are the standard normalized-intensity laws of a PPP. This is the same algebra that underlies classical Poisson record and multiplicative-renewal constructions.

However, this analogy stops at one shell. The published multiscale proof obtains infinitely many good scales using scaling/ergodic or mixing arguments; it does not assert that the successive canonical cut points form a renewal chain with an explicit transition kernel. Roads are entire affine lines and persist across scales, while the low-speed endpoint-access environment is inherently infinite. Consequently, the exact one-window record law does not by itself give an explicit recursively independent sequence of gateways.

A nearby explicit Markov object is Kendall's / later work's broken local-geodesic or random-flight comparison dynamics, but those are comparison constructions, not the globally minimizing Kahn geodesic. Substituting their Markov kernel would change the source object and therefore cannot move `K_explicit`.

## 7. #25 COUNT THE SAME THING TWICE — independent derivations of the gateway law

The conditional law above can be derived in two genuinely different standard ways.

**Direct Poisson count.** The number of atoms in `A_delta × [24,25)` is Poisson with mean `Lambda_J`; conditional on the count being one, the unique point has distribution equal to the normalized restriction of the intensity measure. Integrating first in `s` gives `f_Theta`; conditioning on `theta` makes `s` uniform on its interval; integrating the speed density gives `f_V`.

**Palm / Mecke normalization.** For any measurable set `C` in the Junction window,

\[
\mathbb P(\text{unique Junction atom lies in }C,\ N_J=1)
=e^{-\Lambda_J}\nu(C).
\]

Dividing by

\[
\mathbb P(N_J=1)=e^{-\Lambda_J}\Lambda_J
\]

gives `nu(C)/Lambda_J`, the same normalized-intensity law. Pushing this law through the orthogonal-projection map yields the same formula for `Z`.

No finite-core checker is warranted: these are exact symbolic PPP identities valid for every admissible `beta>2` and every sufficiently small source `delta`.

## 8. Why the source metric still does not move

The source-moving milestone remains an explicit full law of the actual fixed-pair subnetwork/geodesic, after similarity normalization `gamma_{0,e1}`. The result above gives instead

\[
\mathcal L(Z,\ell_0,v_0\mid G)
\]

for one positive-probability annular bottleneck event `G`.

What remains missing is exactly the part no R12 route has supplied:

1. an explicit law for when/where the successive actual-geodesic gateway events occur along the full path;
2. an exact reset/sufficient-statistic theorem after a gateway;
3. explicit treatment of the infinite low-speed endpoint-access environment;
4. reconstruction of the entire pair geodesic, not a conditional segment/cut point.

Therefore

\[
\boxed{K_{\rm explicit}:1\longrightarrow 1.}
\]

The correct label remains **OPEN / PARTIAL**, not PROVED and not REFUTED.

## 9. HARD protocol: terminal handoff

This run follows STUCK RECOVERY 2 OF 2 and is the selected final research attempt. Because the frozen metric still did not move, the HARD protocol now forbids another I0115 recovery in this R12 assignment.

Terminal handoff state:

- strongest exact positive item: the closed-form conditional law above for the **actual** published canonical gateway on the Blanc--Curien--Kahn master event;
- strongest negative mechanism: finite macroscopic Poisson windows cannot replace the infinite low-speed access environment needed uniformly for continuum endpoints;
- exact remaining obligation: an explicit regenerative/full-law description of the genuine fixed-pair geodesic;
- recommended fresh re-entry, if I0115 is ever reassigned to a different worker with a genuinely new route: attack the law of the low-speed access variable / a scale-stopping sufficient statistic directly, rather than making another finite bottleneck event;
- `next_I0115_recovery_permitted_for_R12: false`.

I0115 is therefore **terminally handed off from R12**, preserving all earlier reports and the canonical claim file as historical ownership evidence rather than silently deleting or overwriting it.

## 10. Rotation screen: no successor claimed in this run

I checked the current queue/claim surface rather than grabbing a PENDING row. The queue snapshot explicitly says PENDING is not READY and that no newly certified READY rows were present at that refresh. Several attractive hard candidates are already claimed/reserved in the live repository.

I also screened one apparently unclaimed high-ranked candidate, I0055 (Lyons--Peres Question 5.16 / Kahn's modified first-moment percolation question). It is **not eligible**: Pengfei Tang's arXiv:2012.01135, *A note on some critical thresholds of Bernoulli percolation*, explicitly identifies the Lyons--Peres edge-cutset version as Question 1.5 and proves an affirmative answer (Theorem 1.6) for every locally finite connected infinite graph. Thus I0055 is a stale open-looking queue row, not a lawful successor.

I did not promote another PENDING item without a complete source/current-status/prior-attempt/ownership gate. Rotation state is therefore

`ROTATION_WAIT / NO_SUCCESSOR_CLAIMED`.

The **next R12 invocation must perform successor admission/rotation screening, not resume I0115 and not resume I0102**. If it identifies a genuinely unowned, source-current HARD target, it may create the required create-only claim and begin from that target's recovered history. PENDING is not permission.

## 11. Model / scheduler / permission reality

The exposed task-management schema still provides prompt/title/schedule/timing/enablement fields but no binding model-family or reasoning-effort selector. GPT-6 / maximum can therefore only be requested in prompt text; enforcing and authenticating it would require product/runtime support exposing those selectors plus completed-run telemetry.

The historical native-task modification error `You cannot modify this task` (including the earlier P26 probe) must be resolved through the owning account/workspace context, an authorized ownership transfer, or platform support. A repository edit or duplicated scheduler job is not a legitimate workaround. No scheduler, permission, email, Drive, public-posting, purchase, or workflow action was taken in this run.

## 12. Structured ledger delta

```yaml
ledger_delta:
  worker: R12
  lane: HARD_OUTSIDE
  predecessor_i0102:
    status: TERMINAL_HANDOFF_DO_NOT_REOPEN
    metric: "(a,C,p0)=(1/2,1,5)"
  active_target_at_run_start: I0115
  source: "David Aldous, Scale-invariant random spatial networks (2014), Open Problem 27; frozen explicit finite-subnetwork sufficient clause"
  metric: K_explicit
  before: 1
  after: 1
  movement: NO_MOVEMENT
  methods_used: [8, 17, 25]
  new_exact_partial:
    label: "conditional canonical gateway law on the BCK master event"
    source_object: "actual Kahn/Kendall geodesic on published positive-probability master event G"
    source_metric_moved: false
  status: OPEN_PARTIAL_TERMINAL_HANDOFF
  stuck_recoveries_consumed: 2
  final_allowed_research_attempt_consumed: true
  next_I0115_recovery_permitted_for_R12: false
  finite_core: none
  checker: none_warranted
  rotation:
    state: ROTATION_WAIT_NO_SUCCESSOR_CLAIMED
    screened_I0055: KNOWN_RESOLVED_BY_TANG_2020
    next_run: SUCCESSOR_ADMISSION_ONLY
  shared_root_edits: none
```
