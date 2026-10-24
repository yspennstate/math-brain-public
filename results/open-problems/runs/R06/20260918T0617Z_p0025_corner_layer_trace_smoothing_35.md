Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO MOVEMENT on P0025: `E_disk: 0 -> 0`, unchanged count `4 -> 5`; Section-B methods #7 TAKE THE LIMIT, #19 MAKE IT AN ALGORITHM, #28 REPLACE FOR ALL WITH TYPICAL.**

# R06 — P0025 exterior-disc synchronous coupling / corner-layer L1 drift and trace smoothing

Run ID: `20260918T0617Z_p0025_corner_layer_trace_smoothing_35`
Repository / branch: `yspennstate/math-open-problems` / `master`
Track: `R06`, lane `CLOSABLE OUTSIDE`

## 0. Continuity and frozen predecessor states

This run continues the create-only R06 claim

`operations/claims/P0025.md`

for Krzysztof Burdzy, *My favorite open problems*, Problem 5(ii), rather than reopening any rotated predecessor.

The literal source question, rechecked on 2026-09-18, remains:

> If `D` is the complement of a non-degenerate closed disc, is it true that with positive probability `limsup_{t->infinity}|X_t-Y_t|>0` for a synchronous coupling of reflected Brownian motions?

The frozen source metric remains the binary source-resolution bit

`E_disk = 1`

only when the literal question is completely proved or refuted on the page. It remains `0`.

The original R06 scheduler title still names Lyons--Peres Question 6.20 / intake I0056. That source is **not** reopened. Its exact original question is retained:

> What is `Phi_V(G)` for regular, co-regular plane graphs `G`? What are `Phi_E(G)` and `Phi_V(G)` for more general transitive, plane graphs `G`?

The frozen admissible pentagonal case remains the `{5,5}` regular co-regular hyperbolic tessellation under the outer vertex-boundary normalization

`Phi_V(G)=inf_{nonempty finite K} |partial_V K|/|K|`,

with certified interval `[sqrt(5),sqrt(5)]`, width `0`. This is only `PARTIAL` for the full Lyons--Peres question. The triangular/codegree-3 and quadrangular/codegree-4 cases already covered by Haslegrave--Panagiotis, DOI `10.1002/rsa.20946`, remain prior art and are not relabeled as new.

The rotated BENJ three-source target is also not reopened.

## 1. Required repository, source, neighboring-state and literature read

Before the new attack I reread/recovered:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- `operations/claims/P0025.md`;
- newest R06 state `runs/R06/20260918T0521Z_p0025_stuck_regeneration_34.md`;
- predecessor technical reports 32 and 33 for the exact peanut conformal map, the corrected Cranston--Le Jan sign audit, the tangent Mellin strip and the Lamperti compiler;
- the neighboring Burdzy Problem 5(i) ownership record `operations/claims/P0024.md` / R19 state.

Fresh dated source/literature checks on 2026-09-18 included:

1. Burdzy's live problem page `https://sites.math.washington.edu/~burdzy/open_mathjax.php`, which still displays Problem 5(ii) as open.
2. M. Cranston and Y. Le Jan, *On the noncoalescence of a two point Brownian motion reflecting on a circle*, Ann. IHP Probab. Stat. 25 (1989), 99--107; exterior equations and Theorem 2 were reread from the Numdam PDF.
3. K. Burdzy, Z.-Q. Chen, P. Jones, *Synchronous couplings of reflected Brownian motions in smooth domains* (2006), for the bounded-domain Lyapunov context.
4. K. Burdzy, *Differentiability of stochastic flow of reflected Brownian motions* (2009), for the bounded-domain excursion/projection mechanism.
5. Current boundary-trace / Dirichlet-to-Neumann literature, including Kwaśnicki's 2024 harmonic-extension survey and recent reflected-diffusion trace work, only as background for the standard trace-process language used below.

Bounded exact-phrase/current searches did not locate a later primary source resolving Problem 5(ii), nor the specific corner-layer constants derived below. This is dated negative evidence, **not** a novelty certificate.

## 2. Idea written before validation

Run 34 identified the main obstruction as the need for a regeneration/entrance law for the scale-free modulator, not an all-state pointwise drift bound.

The three new moves were chosen to attack that exact obstruction.

- **#7 TAKE THE LIMIT.** Write the limiting boundary-local-time trace on the exterior circle explicitly. It is the Cauchy trace with a closed transition density, so after any positive burn-in its angular law is smoothed.
- **#28 REPLACE FOR ALL WITH TYPICAL.** Return to the exact Cranston--Le Jan corrected drift and ask whether its pointwise corner singularity is small after integration against any bounded-density boundary law. The target is an `L1`, not `L-infinity`, estimate.
- **#19 MAKE IT AN ALGORITHM.** If those two pieces work, build an explicit scale-band procedure: enter a compact modulator set, burn in the boundary trace, run until the log separation exits a band, and iterate. This should replace the unrealistically strong all-state one-block condition from run 33.

The key question for this run is therefore not whether the corrected drift is pointwise `O(z)` -- it is not -- but whether the entire bad corner layer has only `O(z)` mass.

## 3. Exact Cranston--Le Jan corrected drift on one exposed arc

Scale the forbidden disc to radius one. Use the Cranston--Le Jan exterior coordinates `(x,y,z)` with `z>0` equal to half the particle separation and

`x^2+(|y|-z)^2 >= 1`.

Write

`t=|y|`,
`L=x^2+(y-1)^2`,
`N=x^2+(y+1)^2`,
`u=log(LN)`.

The exact exterior calculation on p. 107 of Cranston--Le Jan gives, before the finite-time noncoalescence stopping time,

`d u + 2 dz/z = dM + F(x,y,z) dphi`,

where

`F=(x^2+y^2-t z)(L^{-1}+N^{-1})
   -4(LN)^{-1}(y^2-t z)
   -1
   -(LN)^{-1} t z (2t-z)^2.`

This is the mixed-sign expression whose sign was correctly retracted in run 33; no global sign is assumed here.

On the support of `dphi`, the reduced state is on the peanut boundary,

`x^2+(t-z)^2=1`.

Using that identity,

`L=2-2t+2tz-z^2`,
`N=2+2t+2tz-z^2`,

and direct algebra gives the one-variable factorization

\[
\boxed{
 f_z(t):=F|_{\partial}
 =\frac{z(z-2t)(2t^2-tz+z^2-2)}
 {(2-2t+2tz-z^2)(2+2t+2tz-z^2)} .
}
\]

This factorization is the starting point for the new estimate. It is an identity, not a sign claim.

On the upper exposed unit-circle arc write

`t=z+sin theta`,
`-a_z <= theta <= pi+a_z`,
`a_z=arcsin z`.

Because the arc has radius one, `d sigma=d theta`.

## 4. #28 — a new `L1` corner-layer lemma

### Proposition 4.1 — the pointwise singularity is integrably `O(z)`

There is an absolute constant `C` such that for every `0<z<=1/2`, on one exposed arc,

\[
\boxed{
 \int_{-a_z}^{\pi+a_z}
 |f_z(z+\sin\theta)|\,d\theta
 \le C z .
}
\]

Moreover the signed and total-variation first-order constants exist and are

\[
\boxed{
 \lim_{z\downarrow0}\frac1z
 \int f_z(z+\sin\theta)d\theta
 =-\left(\frac{3\pi}{2}-2\right),
}
\]

and

\[
\boxed{
 \lim_{z\downarrow0}\frac1z
 \int |f_z(z+\sin\theta)|d\theta
 =\frac{3\pi}{2}+2 .
}
\]

The lower exposed arc has the same values by symmetry, so the whole peanut boundary has twice these integrals.

### Proof

Put

`s=1+z-t=1-sin theta`.

Substituting `t=1+z-s` in the factored formula gives exactly

\[
 f_z=
 -\frac{z(2+z-2s)
 (2s^2-3sz-4s+2z^2+3z)}
 {(2s(1-z)+z^2)
  (4+4z+z^2-2s(1+z))}.
\]

For `0<z<=1/2` and the exposed arc, the second denominator is bounded away from zero except at the opposite endpoint where the numerator is simultaneously harmless; splitting a fixed small endpoint neighborhood if desired gives the same uniform estimate. The displayed rational expression implies

\[
 |f_z|\le C z\frac{s+z}{s+z^2}
 \le C z + C\frac{z^2}{s+z^2}.
\]

Near the top point `theta=pi/2`, with `h=theta-pi/2`,

`s=1-cos h` is comparable to `h^2` for `|h|<=1`; away from that point it is bounded below. Therefore

\[
 \int\frac{z^2}{s+z^2}\,d\theta
 \le C z,
\]

which proves the uniform `L1` estimate.

For the sharp first-order constants, there are two asymptotic regions.

**Bulk.** For every fixed `theta in (0,pi)` with `theta != pi/2`, direct substitution yields

\[
 \frac{f_z(z+\sin\theta)}{z}\to\sin\theta.
\]

Thus the regular bulk contributes

\[
 \int_0^\pi \sin\theta\,d\theta=2
\]

to the signed first-order coefficient, and also `2` to the total-variation coefficient.

**Corner layer.** Set

`theta=pi/2+z v`.

Then

`s=1-cos(zv)=z^2v^2/2+O(z^4v^4)`

for fixed `v`, and the exact rational formula above gives

\[
 f_z\!\left(z+\sin\left(\frac\pi2+zv\right)\right)
 \longrightarrow
 -\frac{3}{2(1+v^2)}.
\]

The preceding bound supplies domination after the change of variables. Hence the top boundary layer contributes

\[
 -\frac32\int_{-\infty}^{\infty}\frac{dv}{1+v^2}
 =-\frac{3\pi}{2}
\]

to the signed coefficient, and `3pi/2` to the total variation. The small exposed endpoint extensions have vanishing first-order contribution. Adding bulk and corner terms yields exactly

`2-3pi/2 = -(3pi/2-2)`

and

`2+3pi/2`.

`QED`

### Why this matters

The difficult corner is genuinely pointwise: at the top simultaneous-contact state one has

`f_z -> -3/2`.

So no correct proof can demand `|f_z|<=Cz` uniformly. Proposition 4.1 shows that this bad state is confined to a width-`O(z)` boundary layer and that the **entire** mixed-sign coefficient has only `O(z)` boundary `L1` mass.

Consequently, if an entrance/contact law `mu_z` on the peanut boundary has density bounded by `M` with respect to arclength, uniformly for small `z`, then

\[
 \boxed{
 E_{\mu_z}|f_z|\le C M z.
 }
\]

This is exactly the scale `exp(-U)` allowed by the run-33 Lamperti compiler with `U=-log z`.

This proposition is an R06 derivation. I did not locate it in the bounded literature search; novelty is `UNVERIFIED`.

## 5. #7 — solve the limiting modulator smoothing exactly

At zero separation the modulator reduces to the boundary point of reflected Brownian motion on the exterior unit circle, viewed in boundary-local-time clock.

For the boundary Fourier mode `e^{in theta}`, its bounded harmonic extension to `r>1` is

`r^{-|n|} e^{in theta}`.

Taking the inward normal derivative at `r=1` gives the Dirichlet-to-Neumann eigenvalue `-|n|`. Thus the boundary trace has generator `-|D|` and semigroup multipliers

`e^{-|n| ell}`.

Equivalently, after any positive trace time `ell>0`, the angle transition density is the circular Cauchy / Poisson kernel

\[
\boxed{
 p_\ell(\theta,\varphi)
 =\frac{1}{2\pi}
 \frac{\sinh\ell}{\cosh\ell-\cos(\varphi-\theta)} .
}
\]

In particular,

\[
\boxed{
 \sup_{\theta,\varphi}p_\ell(\theta,\varphi)
 =\frac1{2\pi}\coth(\ell/2)<\infty .
}
\]

This boundary-trace description is standard Dirichlet-to-Neumann/Cauchy-process machinery; it is **not** claimed as new. Its role here is different: it gives the exact limiting smoothing mechanism needed by the `L1` corner lemma.

Combining the two displays shows that in the limiting, arclength-smoothed modulator model, the expected absolute corrected drift generated by the entire corner geometry is `O(z)` after any fixed positive trace-time burn-in.

## 6. #19 — explicit band/regeneration algorithm suggested by the two lemmas

The previous all-state target required a conditional drift estimate from every angular/contact state. Proposition 4.1 shows why that was unnecessarily strong.

A more realistic proof algorithm is now concrete.

### Step A — geometric band

For current half-separation `z`, work until the separation exits a fixed logarithmic band

`[z e^{-A}, z e^{A}]`.

If the process exits during the burn-in, record the band move immediately; no drift estimate is needed on that block.

### Step B — trace burn-in

If it remains in the band, run the boundary trace for a fixed positive amount `ell_0`. In the zero-separation model the exact Poisson kernel above makes the modulator density bounded by

`M_0=(2pi)^{-1} coth(ell_0/2)`

independently of the incoming angle.

### Step C — use `L1`, not pointwise, drift control

Once a finite-separation analogue of this bounded-density statement is established, Proposition 4.1 immediately makes the mixed-sign Cranston--Le Jan corrected drift `O(z)` in expectation over the block. The simultaneous-contact corner no longer needs separate pointwise control.

### Step D — compare the martingale part

Run 31/33 already identify the tangent log cocycle as critical with variance rate `2 log 2`, and provide inverse moments of all orders `<1`. A finite-separation block comparison must preserve a nondegenerate second moment and a `2+delta` moment after the burn-in.

### Step E — iterate scales

Then the run-33 Lyapunov/Lamperti compiler applies to the corrected logarithmic separation: positive drift of order `z^eta` with nondegenerate variance cannot drive `U=-log z` to `+infinity`. This would imply that the particle separation does not converge to zero and hence would imply the source's positive-limsup conclusion.

This is an algorithmic proof architecture, not a completed proof. The source metric therefore does not move.

## 7. The remaining blocker is now narrower

The corner singularity itself is no longer the main unknown. The exact remaining analytic obligation is a **finite-separation trace-smoothing theorem** for the *moving* reduced state:

> There exist `ell_0,M,C<infinity` and a source-valid stopping/band convention such that, whenever `z` is sufficiently small and has not exited its fixed log band during the burn-in, the post-burn-in contact/modulator law has density at most `M` with respect to the relevant peanut-boundary arclength (or another reference measure for which Proposition 4.1 has the same `O(z)` integral bound), and the tangent martingale variance/moment estimates are perturbed by at most `O(z^eta)`.

Run 32 gets unusually close to this: for **frozen** separation, its exact conformal map sends the peanut boundary excursion Dirichlet form to the universal Cauchy form, while the physical speed measure is an `O(z)` perturbation in total variation. What is still missing is controlling the fact that `z` and the moving frame change during the same block.

The new result removes one previously feared failure mode: the simultaneous-contact corner does **not** carry order-one averaged drift under any uniformly bounded-density entrance law. Its entire contribution is integrably first order in `z`.

## 8. Status and stuck accounting

The source problem is **OPEN** and R06 status is **PARTIAL**. No source-level proof or refutation is claimed.

The frozen metric remains

`E_disk: 0 -> 0`.

The unchanged count is

`4 -> 5`.

This run followed the recovery action selected in run 34 rather than repeating the thinking-only inventory. If the next P0025 source-level attempt is also unchanged, it will be the sixth unchanged run and the CLOSABLE rotation/handoff rule applies; R06 must not produce a seventh local lemma on P0025.

The next method triple, if one final P0025 attack is made before rotation, is:

- **#4 PROVE SOMETHING WEAKER, COMPLETELY** — prove the finite-separation bounded-density smoothing theorem for the frozen peanut or for a stopped moving block, with exact source-faithful stopping rules;
- **#16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE** — solve the stopped generator/heat-kernel problem for a discretized modulator only if it directly tests the smoothing claim, not as a substitute for a theorem;
- **#22 READ THE FAILURES, NOT THE SUCCESSES** — inspect precisely where Burdzy 2009 uses boundedness and whether each use is replaced by the exterior trace/conformal estimates already on file.

## 9. Model / scheduler control status

The exposed scheduler/task-control interface still offers prompt/title, schedule or relative start, timing mode, and enabled state. It exposes **no binding model-family selector, no reasoning-effort selector, no guaranteed hour-long execution field, and no authenticated applied-run model telemetry**.

Therefore GPT-6 / maximum remains a prompt request only. This report accurately states the model available to this run as GPT-5.6 Sol and the reasoning level as UNVERIFIED.

The historical P26 response `You cannot modify this task` was context/authorization-specific: repository implementation records show a later authorized context could update P26's prompt. That does not create model/reasoning controls. Enforcing GPT-6 / maximum would require an authorized product/backend scheduler surface exposing persistent model/reasoning fields and authenticated completed-run telemetry. No permission bypass or replacement task is attempted here.

## 10. Structured ledger delta

```yaml
ledger_delta:
  track: R06
  lane: CLOSABLE_OUTSIDE
  source:
    canonical_id: P0025
    author: Krzysztof Burdzy
    work: My favorite open problems
    locator: Problem 5(ii), Convergence of synchronous couplings
    source_question: exterior-disc synchronous reflected Brownian coupling; positive probability of positive limsup separation
    source_status: OPEN
    source_rechecked: 2026-09-18
  metric:
    name: E_disk
    before: 0
    after: 0
    meaning: binary literal-source-resolution bit
  status_before: PARTIAL
  status_after: PARTIAL
  unchanged_count_before: 4
  unchanged_count_after: 5
  tried_moves: [7, 19, 28]
  new_results:
    - exact factorization of the mixed-sign Cranston-Le Jan corrected drift on the peanut boundary
    - boundary L1 bound integral |f_z| = O(z)
    - sharp one-arc signed asymptotic coefficient -(3*pi/2-2)
    - sharp one-arc total-variation coefficient 3*pi/2+2
    - exact limiting exterior-circle boundary-trace Poisson/Cauchy smoothing kernel recovered as standard machinery
  remaining_obligation: >-
    Prove a finite-separation, moving-state trace-smoothing/bounded-density theorem over a stopped log-separation band, together with preservation of the critical tangent variance/moment estimates; then feed those estimates into the existing Lamperti recurrence compiler and bridge from fixed source-valid starting points.
  next_moves: [4, 16, 22]
  closure: false
  closure_audits: []
  evidence:
    - operations/claims/P0025.md
    - runs/R06/20260918T0521Z_p0025_stuck_regeneration_34.md
    - runs/R06/20260918T0421Z_p0025_mellin_lamperti_33.md
    - runs/R06/20260918T0321Z_p0025_peanut_conformal_trace_32.md
    - Cranston-Le Jan, Ann. IHP 25 (1989), 99-107
    - Burdzy, EJP 14 (2009), arXiv:0806.0119
  prior_art_note: >-
    Finite-time exterior noncoalescence is Cranston-Le Jan prior art; zero-separation boundary trace as a Cauchy/Dirichlet-to-Neumann process is standard. The corner-layer factorization and sharp L1 constants were not located in the bounded dated search, but literature novelty is UNVERIFIED.
  original_I0056_retained:
    regime: H_{5,5}
    normalization: outer vertex boundary
    interval: '[sqrt(5), sqrt(5)]'
    width: 0
    parent_source_status: PARTIAL
    exclusions: Haslegrave-Panagiotis triangular/quadrangular cases
```
