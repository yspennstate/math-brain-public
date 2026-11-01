Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED**; this was not GPT-6 at maximum and I do not claim otherwise. **NO MOVEMENT: frozen metric `A_forest = 4/3 -> 4/3`; fifth consecutive unchanged run after the source-threshold improvement. STUCK RECOVERY 1 continues with the already selected recovery `PORT THE TECHNIQUE FROM THE NEAREST SOLVED ANALOGUE`. Methods actually tried: B4, B20, B30.**

**Problem/source:** Giacomo Aletti, Andrea Collevecchio, Irene Crimaldi, Maria Deijfen, Steffen Dereich, Andrea Ghiglietti, Remco van der Hofstad, Mark Holmes, Daniel Kious, Victor Kleptsyn, Bas Lodewijks, Peter Mörters, Bruno Schapira (2025), *Open Problems in Stochastic Reinforcement Models*, Open Problem 12 (`P0082`): improve the finite-graph WARM forest threshold `alpha > 2`.  
**Track/root:** P13 / `proofnet24/P13-outside-successor`.  
**Exclusive claim:** `operations/claims/P0082.md`, native slot `6aa7b253b37c8191b693d8dc79298d37`.  
**Category:** CLOSABLE OUTSIDE.  
**Status:** source strict-threshold answer mathematically PROVED at `A_forest=4/3`, but **NOT CLOSURE-CERTIFIED**. The critical endpoint work below is auxiliary and earns zero source-metric credit.

# 1. Continuity and controlling state

The retired P13 I0051 / Aldous--Janson clade-covariance project remains retired and was not reopened. Before doing new mathematics I recovered the current P0082 claim, the owner directive at anchor commit `749da260517828ed311f6f1b1af74915c054bdf3`, `operations/NEW_METHODS_2026-09-16.md`, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the P0082 intake/catalog history, all prior P13 successor reports, and the current P14 neighbour state. The compact root `RESULTS.md` still has an older P13 row, so it is not used to overwrite the newer immutable P0082 history. P13 does not edit shared root ledgers.

The canonical P0082 claim still belongs exclusively to this native slot. Its frozen source-faithful metric is

\[
A_{\rm forest}:=\inf\left\{A:\;\begin{array}{l}
\text{for every finite graph, every allowed positive firing-rate vector, and every }\alpha>A,\\
\text{every not-linearly-unstable WARM equilibrium has forest support}
\end{array}\right\}.
\]

The first successor run proved `P13-P0082-WARM-FOREST-4OVER3-01`: `A_forest<=4/3`; the source itself supplies the matching uniform-triangle obstruction for every `alpha<4/3`. Thus

\[
\boxed{A_{\rm forest}=4/3.}
\]

No endpoint strengthening, spectral refinement, or auxiliary stochastic lemma is counted as movement of this metric.

The immediately preceding report is

`proofnet24/P13-outside-successor/runs/2026-09-17/2026-09-17T22-31-35Z__stuck-recovery-01-continuation.md`

(blob `d3bd9fe157963283267bafd7bfd880bef6a671ee`). It proved the auxiliary exact pair-difference martingale transforms at the symmetric critical triangle and, after a localized application of Wei's martingale-transform theorem, established the following two necessary conditions for endpoint convergence. Put

\[
x_*=(1/3,1/3,1/3),
\qquad
x_1=\frac13+2u,
\quad x_2=\frac13-u+v,
\quad x_3=\frac13-u-v,
\]

and use the isotropic complex coordinate

\[
w:=\frac{v}{\sqrt3},\qquad z:=u+iw,\qquad \rho:=|z|.
\]

Then, modulo a null set,

\[
X_n\to x_*
\quad\Longrightarrow\quad
P_n^{12},P_n^{23},P_n^{31}\to0,
\tag{1.1}
\]

and

\[
X_n\to x_*
\quad\Longrightarrow\quad
\sum_n\gamma_{n+1}\rho_n^2=\infty.
\tag{1.2}
\]

Here the `P_n^{ij}` are the exact predictable transverse multipliers from the previous report and `gamma_n` is the WARM stochastic-approximation step, asymptotic to `1/n`.

This run does not re-prove those facts. It asks what (1.1)--(1.2) force geometrically and why the current algorithm still does not close the endpoint.

# 2. Fresh source and literature check -- 18 September 2026 local / 17 September UTC

The primary source PDF was opened and its relevant pages visually checked again:

`https://www.matrix-inst.org.au/wp_Matrix2016/wp-content/uploads/2023/Aletti.pdf`

On printed page 10, after stating that finite-graph WARM converges to an equilibrium that cannot be linearly unstable and recalling the `alpha>2` forest theorem, the source states:

> Open Problem 12 Improve the lower bound `alpha>2` for which every connected component is a tree.

The same page records that on the uniform triangle an edge dies almost surely for `alpha>4/3` but not for `alpha<4/3`; the next page says the lower bound cannot in general be below `4/3` and says perhaps `alpha>4/3` is sharp. This reconfirms that the strict source question is exactly the one already answered by `P13-P0082-WARM-FOREST-4OVER3-01`; equality is an optional strengthening, not a missing source quantifier.

Fresh bounded queries included

- `"Open Problems in Stochastic Reinforcement Models" "Open Problem 12" WARM alpha 4/3`,
- `"WARM" forest "4/3" reinforcement Holmes Kleptsyn 2026`,
- exact Holmes--Kleptsyn 2017 title,
- exact van der Hofstad--Holmes--Kuznetsov--Ruszel title plus triangle/`4/3`,
- exact Wei 1993 title,
- exact Brandière 1998 title.

The search again recovered the 2025 source, Holmes--Kleptsyn's 2017 theorem with universal forest threshold `alpha>2`, the 2016 graph-competition paper, Wei's 1993 non-atomic martingale-transform paper, and Brandière's 1998 pathological-trap paper. No later primary paper stating the universal finite-WARM `alpha>4/3` forest theorem or resolving exact Open Problem 12 was found in this bounded search. This is **bounded negative evidence only**, not proof of worldwide openness or a novelty certificate.

Wei's publisher abstract confirms the relevant shape: a sufficient condition for a martingale-transform limit to have a continuous distribution and a zero-regression-derivative stochastic-approximation application with logarithmic rate. Brandière's publisher abstract confirms that singular equilibria and other pathological traps are the intended regime of that paper. Neither source by itself supplies the angular theorem needed below.

# 3. B4 -- prove something weaker, completely: endpoint convergence forces macroscopic angular wandering

The previous report left the blocker as the possibility of a very irregular endpoint-convergent path with divergent radial square energy. B4 asks for a complete theorem that characterizes such a path more sharply, without pretending it moves the source metric.

Let

\[
\omega=e^{2\pi i/3}.
\]

The Taylor expansions of the three exact pair multipliers from the previous report become especially symmetric in the isotropic coordinate `z=u+iw`:

\[
\begin{aligned}
\lambda_{23}(z)&=3\operatorname{Re}(z)-3|z|^2+O(|z|^3),\\
\lambda_{12}(z)&=3\operatorname{Re}(\omega z)-3|z|^2+O(|z|^3),\\
\lambda_{31}(z)&=3\operatorname{Re}(\omega^2 z)-3|z|^2+O(|z|^3).
\end{aligned}
\tag{3.1}
\]

The common quadratic term is exactly the earlier identity `3u^2+v^2=3|z|^2`; the three linear terms are the three `120`-degree projections.

Define, after a sufficiently late deterministic starting index `N_0`,

\[
Z_n:=\sum_{k=N_0}^{n-1}\gamma_{k+1}z_k,
\qquad
E_n:=\sum_{k=N_0}^{n-1}\gamma_{k+1}|z_k|^2.
\tag{3.2}
\]

## Proposition `P13-P0082-ENDPOINT-ANGULAR-WANDERING-05`

Modulo the same null set as in the preceding Wei reduction, on the event `X_n -> x_*` one has

\[
\boxed{
\limsup_{n\to\infty}\frac{|Z_n|}{E_n}\le2.
}
\tag{3.3}
\]

In particular, on that event the nonzero directions `z_n/|z_n|` cannot eventually lie in **any fixed angular arc of width strictly less than `pi`**. Hence an endpoint-convergent path cannot eventually remain in one incoming sector, one outgoing sector, one `120`-degree sector, or any neighborhood of a single deterministic separatrix.

### Proof

By (1.2), endpoint convergence implies

\[
E_n\to\infty.
\tag{3.4}
\]

For each `j in {0,1,2}`, write `P_n^{(j)}` for the corresponding pair multiplier in (3.1). Its logarithm satisfies

\[
\log P_n^{(j)}
=\log P_{N_0}^{(j)}
+\sum_{k=N_0}^{n-1}
\log\bigl(1+\gamma_{k+1}\lambda_j(z_k)\bigr).
\tag{3.5}
\]

On the convergence event, `z_k->0`. Since `lambda_j(z)=O(|z|)` near zero and `sum gamma_k^2<infinity`, the quadratic error in `log(1+y)=y+O(y^2)` is summable:

\[
\sum_k\gamma_{k+1}^2\lambda_j(z_k)^2<\infty.
\tag{3.6}
\]

The cubic remainder in (3.1) is negligible relative to `E_n`. Indeed, for every `epsilon>0`, eventually `|z_k|<=epsilon`, and therefore

\[
\sum_{k=N}^{n-1}\gamma_{k+1}|z_k|^3
\le
\epsilon\sum_{k=N}^{n-1}\gamma_{k+1}|z_k|^2.
\tag{3.7}
\]

Because `E_n->infinity`, (3.7) implies

\[
\sum_{k=N_0}^{n-1}\gamma_{k+1}O(|z_k|^3)=o(E_n).
\tag{3.8}
\]

Combining (3.1), (3.5)--(3.8), uniformly over the finite set of three multipliers,

\[
\boxed{
\log P_n^{(j)}
=3\operatorname{Re}(\omega^j Z_n)-3E_n+o(E_n).
}
\tag{3.9}
\]

For every complex number `Z`, three unit vectors separated by `120` degrees satisfy

\[
\max_{j=0,1,2}\operatorname{Re}(\omega^j Z)\ge\frac{|Z|}{2}.
\tag{3.10}
\]

The previous report proved that endpoint convergence forces all three `P_n^{(j)}->0`. Hence

\[
\max_j\log P_n^{(j)}\to-\infty.
\tag{3.11}
\]

If (3.3) failed, some `delta>0` and subsequence would satisfy `|Z_n|> (2+delta)E_n`. Along that subsequence, (3.9)--(3.10) give

\[
\max_j\log P_n^{(j)}
\ge
\frac32|Z_n|-3E_n+o(E_n)
\ge
\frac{3\delta}{2}E_n+o(E_n)\to+\infty,
\]

contradicting (3.11). This proves (3.3).

Now suppose, for contradiction, that from some index onward every nonzero `z_k` lies in a fixed angular arc of width `ell<pi`. Let `eta` be the unit vector pointing to the center of that arc and put

\[
c:=\cos(\ell/2)>0.
\]

Then on the tail

\[
\operatorname{Re}(\overline\eta z_k)\ge c|z_k|.
\tag{3.12}
\]

Choose a later `N` so that

\[
\delta_N:=\sup_{k\ge N}|z_k|<c/3.
\tag{3.13}
\]

This is possible because `z_k->0`. Put

\[
A_n:=\sum_{k=N}^{n-1}\gamma_{k+1}|z_k|,
\qquad
E_{N,n}:=\sum_{k=N}^{n-1}\gamma_{k+1}|z_k|^2.
\]

Then

\[
E_{N,n}\le\delta_N A_n,
\qquad
A_n\ge\frac{E_{N,n}}{\delta_N}.
\tag{3.14}
\]

Since removing a finite prefix from (3.4) leaves `E_{N,n}->infinity`, equations (3.12)--(3.14) imply

\[
|Z_n|
\ge \operatorname{Re}(\overline\eta Z_n)
\ge cA_n-O(1)
\ge\frac{c}{\delta_N}E_{N,n}-O(1).
\tag{3.15}
\]

Because `c/delta_N>3`, (3.15) contradicts the universal upper ratio (3.3). Therefore no such tail arc exists. `square`

### B4 outcome

This is a complete auxiliary theorem, not a renamed source result. It disproves the simplest special-case hope from the previous report: an endpoint-convergent trajectory **cannot** eventually align with one incoming separatrix. If convergence occurs, it must retain macroscopic angular wandering arbitrarily late while its radius tends to zero.

That is genuine narrowing of the endpoint obstruction, but it earns **zero** movement of `A_forest` because the strict source theorem was already sharp.

# 4. B20 -- find why the multiplier algorithm fails: balanced three-sector tours evade it exactly at quadratic order

The prior algorithm was: each pair difference has a transverse multiplier; perhaps one multiplier must expand, contradicting (1.1). Proposition 3.3 shows why no fixed sector can persist, but it does not itself rule out repeated sector switching. B20 asks for the precise evasion mechanism.

At a fixed small radius `rho`, consider the three directions

\[
z=\rho,\qquad z=\rho\omega,\qquad z=\rho\omega^2.
\tag{4.1}
\]

Their vector sum is zero. Consequently, if a path spends equal `gamma*rho`-weighted mass in these three directions over a macrocycle, then for every `j`

\[
\sum_{\rm macrocycle}
\gamma\,3\operatorname{Re}(\omega^jz)=0.
\tag{4.2}
\]

But the common quadratic term in all three multiplier expansions has the same sign:

\[
-3\sum_{\rm macrocycle}\gamma|z|^2<0.
\tag{4.3}
\]

Thus a sufficiently balanced tour through the three sectors can make **all three** multiplier logarithms decrease simultaneously:

\[
\Delta\log P^{(j)}
=-3\sum_{\rm macrocycle}\gamma\rho^2
+\text{higher-order imbalance},
\qquad j=0,1,2.
\tag{4.4}
\]

If the radial energy in (1.2) diverges while these linear projections continue to cancel, (4.4) is fully compatible with all three `P_n^{(j)}->0`.

This is not claimed to be an actual WARM trajectory. It is the exact reason the **multiplier-only algorithm fails**: the three positive linear directions can be cyclically permuted and averaged away, whereas the negative quadratic term is rotation-invariant and accumulates. Any endpoint proof must therefore show that the genuine WARM dynamics/noise cannot execute the increasingly balanced angular tours required by (4.2).

### B20 outcome

Worked as failure analysis. The residual problem is no longer vaguely “angular switching.” The only way to satisfy the known necessary conditions is a tail with persistent macroscopic angular wandering whose weighted first angular moment is small compared with its divergent weighted second radial moment:

\[
\left|\sum_{k<n}\gamma_{k+1}z_k\right|
\le (2+o(1))
\sum_{k<n}\gamma_{k+1}|z_k|^2.
\tag{4.5}
\]

Since `|z_k|->0`, an unbalanced single-sector tail would make the left side much larger than the right side. Thus cancellation is not optional; it is quantitatively forced.

# 5. B30 -- one scale and one direction at a time: the monkey-saddle has an adiabatic sector coordinate, but the divergent-energy regime destroys its conservation

The preceding stuck report derived the local critical normal form. In the isotropic coordinate it can be written one order more informatively as

\[
\boxed{
\dot z
=-\frac32\overline z^{\,2}
-3|z|^2z
+O(|z|^4).
}
\tag{5.1}
\]

The leading quadratic flow has an exact conserved quantity

\[
J(z):=\operatorname{Im}(z^3)=|z|^3\sin(3\theta).
\tag{5.2}
\]

Indeed, for `dot z=-(3/2)\bar z^2`,

\[
\frac{d}{dt}J(z(t))
=\operatorname{Im}\left(3z^2\dot z\right)
=\operatorname{Im}\left(-\frac92|z|^4\right)=0.
\tag{5.3}
\]

This explains geometrically why the three symmetry rays are special: `J=0` is their union, and a deterministic orbit of the pure quadratic model can reach the origin only on that zero level.

However the next term in the actual critical WARM field is decisive. Substituting (5.1) into the derivative of `J` gives

\[
\boxed{
\frac{d}{dt}J
=-9|z|^2J+O(|z|^6).
}
\tag{5.4}
\]

So `J` is only adiabatically conserved. The damping factor suggested by (5.4) is

\[
\exp\left(-9\int|z(t)|^2dt\right).
\tag{5.5}
\]

But the endpoint necessary condition (1.2) is exactly the stochastic-approximation analogue of an **infinite** `|z|^2` time integral. Thus the regime that survived the Wei reduction is precisely the regime in which the cubic correction can erase the leading invariant. The conservation law by itself cannot rule out endpoint convergence.

This is a useful negative result about the route: one cannot freeze the quadratic normal form for arbitrarily many scales and argue that nonzero `J` persists.

There is nevertheless a clean scale separation for the stochastic perturbation. Since `J` is cubic,

\[
\nabla J=O(\rho^2),\qquad D^2J=O(\rho).
\tag{5.6}
\]

The WARM one-step noise is bounded. Therefore, on a tail beginning at index `n` and contained in a radial shell `rho<=delta`, the martingale part of the `J` increment has quadratic variation bounded by a constant multiple of

\[
\sum_{k\ge n}\gamma_{k+1}^2\rho_k^4
\le C\frac{\delta^4}{n},
\tag{5.7}
\]

so its `L^2` size is `O(delta^2/sqrt(n))`. The second-order Taylor bias is bounded by

\[
C\sum_{k\ge n}\gamma_{k+1}^2\rho_k
=O\left(\frac{\delta}{n}\right).
\tag{5.8}
\]

Compared with the natural shell size `|J|~delta^3`, both quantities are negligible whenever

\[
\delta\sqrt n\to\infty.
\tag{5.9}
\]

Thus the next attack can be localized sharply:

- **mesoscopic radial scales** `rho >> n^{-1/2}`: stochastic resetting of `J` is small relative to the cubic sector coordinate, so one should compare the deterministic damping (5.4) with the amount of angular travel demanded by B4;
- **noise scale** `rho \lesssim n^{-1/2}`: the angular/sector coordinate can be reset by one-step noise, but such radii contribute very little to the divergent energy sum (1.2) unless the process repeatedly exits back to larger scales.

I do **not** promote this scale split to a theorem ruling out the endpoint. It is the B30 reduction that tells the next run where a proof must live.

### B30 outcome

Worked as a localization/diagnosis, not as a metric-moving claim. The leading conserved quantity exists, but the same infinite radial energy forced by the previous run destroys exact conservation at the first nonlinear correction. The promising scale is therefore the range above `n^{-1/2}`, where the sector coordinate is robust to noise but its deterministic damping is still measurable.

# 6. Exact blocker after this run

The optional endpoint question remains

\[
\mathbb P_{K_3,p\equiv1,\alpha=4/3}(X_n\to x_*)\stackrel?=0.
\tag{6.1}
\]

The surviving hypothetical path must now satisfy **all** of the following:

\[
\boxed{
\begin{gathered}
X_n\to x_*,\\
\sum_n\gamma_{n+1}|z_n|^2=\infty,\\
P_n^{12},P_n^{23},P_n^{31}\to0,\\
\limsup_n\frac{|\sum_{k<n}\gamma_{k+1}z_k|}
{\sum_{k<n}\gamma_{k+1}|z_k|^2}\le2,\\
\text{the nonzero tail directions are not contained in any fixed arc of width }<\pi.
\end{gathered}
}
\tag{6.2}
\]

Equivalently: any exceptional convergence must approach the critical point while continuing to make macroscopic angular excursions whose first-order projections cancel to the scale of the quadratic radial energy. A one-sector or asymptotically aligned path is now rigorously excluded.

What a proof still lacks is a theorem showing that the **actual** WARM angular dynamics and bounded martingale noise cannot sustain those increasingly balanced tours while `rho_n->0`. This is a much narrower obstruction than at the start of STUCK RECOVERY 1.

The simplest unresolved case is still the pure uniform triangle at exact `alpha=4/3`; no larger graph or rate asymmetry is involved.

The nearest solved analogue remains Wei 1993's one-dimensional zero-derivative Robbins--Monro setting. Its scalar order/sign structure eliminates angular cancellation completely. That is exactly what is missing here. Brandière's singular-trap framework is geometrically closer, but no checked theorem from the accessible primary text has yet supplied the required multiscale angular exclusion.

# 7. Source metric, stagnation, and rotation rule

Frozen metric before: `A_forest=4/3`.  
Frozen metric after: `A_forest=4/3`.  
Movement: **NO MOVEMENT**.  
Consecutive unchanged runs after the source-threshold improvement: **5**.

The source strict problem remains **mathematically PROVED / NOT CLOSURE-CERTIFIED**. The fifth unchanged run does not yet trigger the six-run closable rotation, so the claim remains active for one more run. If the next invocation again leaves the frozen source metric unchanged and no closure-status gate changes through qualifying audits/prior-art evidence, the owner rule requires a P0082 handoff/rotation rather than a third hour of endpoint refinement. The metric will not be renamed to reset that clock.

The next three unused method moves, if a final pre-rotation mathematical attack is warranted, are **B7 (take the limit), B12 (find what is conserved), B29 (add the points at infinity / compactify the angular dynamics)**. Concretely, the route is to blow up around `z=0` at mesoscopic radial scales, use `J=Im(z^3)` together with the radial Lyapunov coordinate rather than the leading normal form alone, and compactify direction/radius so that a balanced three-sector tour becomes an invariant boundary object that can be tested against the genuine WARM transition law.

# 8. Audit and neighbour state

Repository searches still found **no** P26 end-to-end P0082 audit and **no** distinct OTHER-track end-to-end P0082 audit. Self-checks and P13's own endpoint work do not count. Publication-level prior-art clearance also remains open; the dated searches above are bounded negative evidence only.

P13's directed secondary duty remains P14. The already completed P14 component audits are retained rather than repeated. The current P14 neighbour is now on Fernley--Jacob contact-process target G0007 and is in its own HARD recovery cycle; no new P14 claim required a duplicate P13 audit this run.

Because no finite universal claim was introduced here, no decorative exact checker was created. Proposition 3.3 has a full analytic proof on this page; B20 and B30 are explicitly labeled failure analysis / route reduction where appropriate.

# 9. Structured ledger_delta for P26

```yaml
ledger_delta:
  track: P13
  native_slot: 6aa7b253b37c8191b693d8dc79298d37
  canonical_id: P0082
  source: "Aletti et al. (2025), Open Problems in Stochastic Reinforcement Models, Open Problem 12"
  category: CLOSABLE_OUTSIDE
  metric:
    name: A_forest
    before: "4/3"
    after: "4/3"
    movement: "no movement"
    unchanged_streak: 5
  source_status: "PROVED mathematically / NOT CLOSURE-CERTIFIED"
  auxiliary_progress:
    id: P13-P0082-ENDPOINT-ANGULAR-WANDERING-05
    statement: "At alpha=4/3 on the uniform triangle, endpoint convergence forces |sum gamma z|/(sum gamma |z|^2) to have limsup at most 2 and forbids eventual confinement of the nonzero directions to any fixed angular arc of width < pi."
    status: PROVED_AUXILIARY
    source_metric_credit: 0
  methods_tried: [4, 20, 30]
  selected_stuck_recovery: "port the technique from the nearest solved analogue"
  exact_blocker: "rule out an endpoint-convergent path with divergent radial energy and persistent balanced macroscopic angular tours"
  next_methods: [7, 12, 29]
  rotation_rule: "next unchanged source-metric run reaches six and must handoff/rotate absent qualifying closure-gate movement"
  audits:
    p26_end_to_end: MISSING
    other_track_end_to_end: MISSING
    p14_component_duty: "previous completed audits retained; no redundant repeat"
  prior_art:
    status: "bounded dated search only; publication novelty/clearance remains open"
  retired_exclusions:
    - "P13 I0051 Aldous-Janson clade covariance remains retired"
```

# 10. Delivery discipline

This invocation writes only this immutable own-track report. No root ledger, peer file, historical report, claim ownership file, email/Gmail, Drive item, public post, paid compute, credential/permission setting, workflow, or schedule is modified. The scheduler/model interface still does not provide a binding model-family or reasoning-effort selector; GPT-6/maximum remains prompt-requested only, while this report truthfully records the actual model identity available to the run and an UNVERIFIED reasoning level.
