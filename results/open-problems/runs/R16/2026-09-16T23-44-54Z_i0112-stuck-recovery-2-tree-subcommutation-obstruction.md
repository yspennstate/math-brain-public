Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested in prompt text, but this runtime exposes no model selector, no reasoning-effort selector, and no authenticated telemetry establishing GPT-6/maximum. **NO MOVEMENT:** active R16 metric `W_exp = 1/2 provisional -> 1/2 provisional`; unchanged count `4`; **STUCK_RECOVERY_2**; methods actually tried: **#6 DEFORM TO A POINT YOU CAN SOLVE, #13 FIND WHAT ONLY INCREASES, #21 ASK WHO ELSE HAS THIS SHAPE**.

Problem/source: **R16 / I0112 — Justin Salez (2025), _Modern aspects of Markov chains: entropy, curvature and the cutoff phenomenon_, arXiv:2508.21055v1, Problem 2.3: prove that every bounded-degree vertex-transitive expander sequence exhibits total-variation cutoff.** Status: **PARTIAL / STUCK_RECOVERY_2**.

# R16 — I0112 second stuck recovery: the regular tree kills uniform long-time subcommutation

Run ID: `2026-09-16T23-44-54Z_i0112-stuck-recovery-2-tree-subcommutation-obstruction`  
Repository/branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and mandatory state recovery

I did not restart Beck--Fiala, I0013, or any older R16 assignment. Before research I recovered/read:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- canonical ownership `operations/claims/I0112.md`;
- the newest complete own report `runs/R16/2026-09-16T22-43-00Z_i0112-stuck-recovery-1.md` and the preceding I0112 reports;
- the newest neighboring Salez report `runs/R01/20260916T2302Z_i0113_stuck1_subcommutation_04.md`;
- the newest R12 report `runs/R12/2026-09-16T23-31-37Z_i0060_noise_cost_mismatch_03_5d8a42.md`.

The large JSONL intake corpus cannot be rendered byte-for-byte in one connector response. I recovered the exact I0112 claim/queue/source state and searched the relevant intake/attempt surfaces; I do not claim a fictitious literal reread of every row.

R12's newest report is still `PARTIAL / OPEN` on I0060, with its frozen metric `delta_cert = UNMEASURED -> UNMEASURED`. It is not a complete package, hence `R16_AUDIT_R12=PENDING_NOT_READY`; no audit is fabricated.

A repository search still located no P26 audit and no distinct second-track end-to-end audit of the R16/I0112 synchronous-product package. Those closure dependencies remain pending.

## 2. Current source/literature refresh

The originating Beck--Fiala source is not reopened. Bansal--Jiang, arXiv:2508.03961v2, proves the square-root-order Beck--Fiala bound in the regime `t >= log^2 n` and a polylogarithmically weakened bound below it. Guo--Fang--Lu, arXiv:2609.11189v1 (10 Sep 2026), still explicitly states the stronger Komlos theorem and, as a consequence, for every integer `t>=1`,

\[
\operatorname{disc}(A)<3\sqrt{2\pi t}.
\]

A fresh bounded 16/17 September search found no v2, withdrawal, or proof-specific correction to that preprint. It is recorded as a current primary-literature resolution claim, not as mature referee validation.

For the active I0112 source, the latest directly relevant paper found remains Dylan Altschuler, arXiv:2609.14945 (14 Sep 2026), which proves Gaussian-profile cutoff for every fixed-degree **long-range expander** sequence and explicitly describes this as intermediate progress toward the long-standing conjecture for transitive spectral expanders. Thus Salez Problem 2.3 remains open in the bounded current-status search.

The recovery route selected in the previous report was Francesco Pedrotti--Justin Salez, arXiv:2607.05345v2, _The local product condition implies cutoff_. They define the optimal sub-commutation factor `psi(t)` by

\[
\Gamma P_t f\le \psi(t)P_t\Gamma f,
\]

observe that `psi` is submultiplicative, and in Remark 1 explicitly propose a negative-curvature repair of the form

\[
\psi(t)\le C e^{-2\kappa t},\qquad C>1,\ \kappa>0.
\tag{SC}
\]

Their Remark 2 separately permits a local Poincare constant restricted to the mixing window. The present run tests (SC) first, as prescribed by the prior handoff.

Hermon--Huang--Pedrotti--Salez, arXiv:2409.16869, remains the closest group-information theorem: it gives dimension-free varentropy control for conjugacy-invariant group walks. Its trajectory rearrangement uses conjugacy invariance essentially; arbitrary Cayley walks do not inherit that mechanism.

A bounded prior-art search for combinations of `regular tree`, `sub-commutation`, `carre du champ`, `harmonic function`, `Poisson boundary`, and `Bakry-Emery` found standard literature on harmonic functions/Poisson boundaries and negative graph curvature, but no source explicitly stating the precise `psi(t)->infinity` obstruction proved below. **Novelty is therefore UNVERIFIED**; a negative search is not a novelty certificate.

## 3. Frozen metric and why this is STUCK_RECOVERY_2

The canonical metric is

\[
W_{\exp}:=\inf\Bigl\{w:\text{R16 certifies a new source-admissible family with cutoff window }O((\log|V|)^w)\Bigr\}.
\]

The synchronous direct-product theorem moved this provisionally to `1/2`. A later run proved that every cutoff family of bounded-degree expanders has window at least order `sqrt(log |V|)`, so `1/2` is the absolute possible floor. The two subsequent reports did not clear the remaining prior-art/audit gate or prove a broader source-valid family. The previous report was the first required stuck recovery, with unchanged count `3`; this report has no metric movement, so the unchanged count is `4` and this is **STUCK_RECOVERY_2**, the second and final permitted hard-target recovery before a third stuck episode forces handoff/rotation.

The numerical metric cannot honestly be improved below `1/2`; progress must instead clear the provisional theorem's external-class gate or prove cutoff for a genuinely broader source-admissible class.

## 4. Method #6 — DEFORM TO A POINT YOU CAN SOLVE: why conjugacy averaging is not a safe deformation

The natural deformation is to start with a symmetric Cayley jump law `mu` and interpolate toward a conjugacy-invariant law, where Hermon--Huang--Pedrotti--Salez applies. Two obstacles appear immediately.

First, conjugacy averaging generally replaces a fixed-size generating set by the union of its conjugacy classes. That support may grow with `|G|`, so the deformation can leave the bounded-degree source class before reaching the solvable endpoint.

Second, cutoff itself is not perturbatively stable under arbitrary additive interpolation. Pedrotti--Salez explicitly recall that suitably tuned additive perturbations can destroy cutoff while preserving much of the usual stationary structure, including the classical product condition. Consequently a proof cannot argue merely that a conjugacy-invariant endpoint has cutoff and then continuously deform the jump law back.

This method therefore did not move `W_exp`. The only useful deformation would have to control a **non-equilibrium** quantity (varentropy or the mixing-window local Poincare constant) uniformly along the deformation, rather than spectral gap or stationary comparison alone. No such control was found.

## 5. Method #13 — FIND WHAT ONLY INCREASES: the harmonic martingale energy

The failed deformation suggested testing the proposed relaxed sub-commutation (SC) on the simplest nonamenable transitive local model: the infinite regular tree. Here there is an exact monovariant.

Let `T_d` be the infinite `d`-regular tree, `d>=3`, let `P` be nearest-neighbor averaging, let `L=P-I`, and let

\[
\Gamma f(x)=\frac1{2d}\sum_{y\sim x}(f(y)-f(x))^2.
\]

If `h` is bounded and harmonic (`Lh=0`), then `h(X_t)` is a bounded martingale and

\[
\frac{d}{dt}\operatorname{Var}_o(h(X_t))
=2\,\mathbb E_o\Gamma h(X_t)\ge0.
\tag{5.1}
\]

Thus the martingale variance is the monotone quantity and the evolving Dirichlet energy is exactly its derivative. On a transient tree the martingale converges to a boundary random variable, so its total accumulated energy is finite. This observation turns out to contradict, rather than support, the desired long-time gradient contraction.

## 6. R16-I0112-C11 — PROVED: on the regular tree the Pedrotti--Salez sub-commutation factor diverges

For continuous-time simple random walk on `T_d`, define the optimal factor

\[
\psi_d(t):=\inf\bigl\{c:\Gamma P_t f\le c P_t\Gamma f\text{ pointwise for every bounded }f\bigr\}.
\]

### Theorem C11

For every `d>=3`,

\[
\boxed{\psi_d(t)\longrightarrow\infty\qquad(t\to\infty).}
\tag{C11}
\]

In particular, there do not exist constants `C<infinity` and `kappa>0` such that

\[
\psi_d(t)\le C e^{-2\kappa t}\qquad\forall t\ge0.
\]

### Proof

Fix a root `o` and one distinguished component `A` of `T_d\setminus\{o\}`. Let `h(x)` be the probability that the limiting end of simple random walk started at `x` lies in the boundary cylinder determined by `A`. This is a bounded harmonic function. It can be written explicitly.

Put `r=d(o,x)`. At the root,

\[
h(o)=\frac1d.
\]

If `x` lies in the distinguished branch `A` and `r>=1`, then the probability of ever hitting `o` is `(d-1)^{-r}`. If the walk never returns to `o`, its limiting end is in `A`; if it does return, symmetry gives probability `1/d` of ultimately using `A`. Hence

\[
h_+(r)=1-\frac{(d-1)^{1-r}}d.
\tag{6.1}
\]

If `x` lies in any other root branch, it must hit `o` before its limiting end can lie in `A`, hence

\[
h_-(r)=\frac{(d-1)^{-r}}d.
\tag{6.2}
\]

The radial recurrence

\[
\frac{h_\pm(r-1)+(d-1)h_\pm(r+1)}d=h_\pm(r)
\]

and the root identity verify `Ph=h`, so `Lh=0` and therefore

\[
P_t h=h\qquad(t\ge0).
\tag{6.3}
\]

At the root, the distinguished child has value `(d-1)/d`, while each of the other `d-1` children has value `1/[d(d-1)]`. Therefore

\[
\Gamma h(o)
=\frac1{2d}\left[
\left(\frac{d-2}{d}\right)^2
+(d-1)\left(\frac{d-2}{d(d-1)}\right)^2
\right]
=\frac{(d-2)^2}{2d^2(d-1)}>0.
\tag{6.4}
\]

The same formulas give, for a vertex at distance `r>=1`,

\[
\Gamma h(x)=
\begin{cases}
\displaystyle
\frac{(d-2)^2}{2d^2}(d-1)^{1-2r},&x\in A,\\[2mm]
\displaystyle
\frac{(d-2)^2}{2d^2}(d-1)^{-1-2r},&x\notin A.
\end{cases}
\tag{6.5}
\]

In particular, `Gamma h(x)->0` as `d(o,x)->infinity`. Continuous-time simple random walk on `T_d` is transient and its distance from the root tends to infinity almost surely. Since `Gamma h` is bounded, dominated convergence yields

\[
P_t\Gamma h(o)=\mathbb E_o\Gamma h(X_t)\longrightarrow0.
\tag{6.6}
\]

But (6.3) and (6.4) imply

\[
\Gamma P_t h(o)=\Gamma h(o)>0.
\]

Therefore, by the definition of `psi_d(t)`,

\[
\psi_d(t)
\ge
\frac{\Gamma P_t h(o)}{P_t\Gamma h(o)}
=
\frac{\Gamma h(o)}{P_t\Gamma h(o)}
\longrightarrow\infty.
\]

This proves C11. QED.

There is also an exact energy identity behind the proof. Since `h(X_t)` converges to the Bernoulli indicator of the chosen boundary branch, its limiting variance is

\[
\frac1d\left(1-\frac1d\right)=\frac{d-1}{d^2}.
\]

Integrating (5.1) gives

\[
\boxed{
\int_0^\infty P_s\Gamma h(o)\,ds
=\frac{d-1}{2d^2}.
}
\tag{6.7}
\]

Thus the denominator in the sub-commutation ratio is precisely a vanishing boundary-martingale energy, while the numerator stays fixed because `h` is harmonic.

This theorem is analytic, not a finite enumeration; no checker artifact is warranted. The complete proof is on the page.

## 7. Method #21 — ASK WHO ELSE HAS THIS SHAPE: transfer the tree obstruction back to high-girth finite graphs

The regular tree is not an irrelevant infinite toy. It is the local limit of high-girth `d`-regular graphs, including classical high-girth Ramanujan/transitive expander families. Altschuler's current paper explicitly names Lubotzky--Phillips--Sarnak graphs as logarithmic-girth examples in the positive cutoff class.

This yields a finite-family obstruction to the previous recovery plan.

### R16-I0112-C12 — PROVED: no uniform global relaxed sub-commutation on large-girth families

Let `(G_n,o_n)` be any sequence of finite `d`-regular graphs with `girth(G_n)->infinity`. Let `psi_n(t)` denote the optimal factor in

\[
\Gamma P_t f\le\psi_n(t)P_t\Gamma f.
\]

There do not exist constants `C<infinity`, `kappa>0` such that

\[
\boxed{
\psi_n(t)\le C e^{-2\kappa t}
\qquad\text{for every }n\text{ and every }t\ge0.
}
\tag{C12}
\]

#### Proof

Assume such `C,kappa` exist. Fix a time `t>0`. Take the bounded harmonic function `h` from C11 and truncate/extend it outside the tree ball `B(o,R)` arbitrarily while keeping its values on `B(o,R)`. For continuous-time rate-one simple random walk, the number of jumps by time `t` is Poisson with mean `t`; therefore all quantities

\[
P_t h(o),\quad P_t h(y)\ (y\sim o),\quad P_t\Gamma h(o)
\]

are approximated, uniformly for bounded functions, by the corresponding quantities computed using paths with at most `R-2` jumps, with error tending to zero as `R->infinity`.

For `n` sufficiently large, `girth(G_n)>2R+2`, so the radius-`R+1` ball around `o_n` is exactly the corresponding tree ball. Transfer the truncated test function to that ball and extend it boundedly outside. On trajectories making fewer than `R-2` jumps, the finite-graph and tree computations coincide. Hence, first letting `n->infinity` at fixed `R,t`, and then `R->infinity`, the assumed finite-graph inequality passes to the tree:

\[
\Gamma P_t h(o)
\le C e^{-2\kappa t}P_t\Gamma h(o).
\]

Since `t` was arbitrary, this holds for every `t>=0`, contradicting C11, for which the ratio of the two sides without the prefactor tends to infinity. QED.

C12 is stronger than the negative-curvature calculation from the preceding report. Negative infinitesimal curvature left open the hope that poor short-time behavior could be absorbed into a constant `C`; C12 shows that, on the fundamental high-girth local model, the **long-time** optimal sub-commutation factor goes the wrong way and actually diverges.

Therefore the previous recovery target

\[
\Gamma P_t f\le C e^{-2\kappa t}P_t\Gamma f
\]

with constants depending only on bounded degree and expansion cannot be a universal route to Salez Problem 2.3. This remains true even though high-girth Ramanujan/transitive expander families themselves do exhibit cutoff by known theorems.

## 8. Updated five-part stuck diagnosis

### (a) Exact blocking statement

The source-level obstruction remains the mixing-time information concentration estimate

\[
\boxed{
\operatorname{Var}_{X\sim\mu_{n,t_n}}
\left[
\log\bigl(|V_n|\mu_{n,t_n}(X)\bigr)
\right]
=o(\log^2|V_n|),
\qquad t_n=t_{\rm mix}^{(n)}(\varepsilon),
}
\tag{BLOCK}
\]

for every bounded-degree vertex-transitive expander sequence; equivalently, a sufficiently strong lower bound for the **restricted mixing-window** local Poincare constant would suffice.

### (b) Routes tried and their precise failures

1. Explicit Cartesian/synchronous product constructions prove new structured cutoff families but do not reach arbitrary transitive expanders.
2. Positive Bakry--Emery curvature fails already on high-girth positive examples.
3. The exact Hecke lift preserves the whole information law but yields only `H`-bi-invariance, whereas the sharp group varentropy theorem uses conjugacy invariance.
4. Stationary spectral expansion does not control the evolving heat-kernel-weighted Poincare constant.
5. The first stuck recovery changed category to the evolving weighted network and local-limit AEP, but neither supplied a moving-time `Theta(log N)` estimate.
6. The present run kills the stronger global negative-curvature repair (SC): on the regular tree `psi(t)->infinity`, and therefore no degree/gap-uniform exponentially decaying `psi` estimate can hold on all high-girth expander families.
7. Deforming to conjugacy-invariant walks is unsafe: conjugacy closure can destroy bounded degree, and additive perturbations need not preserve cutoff.

### (c) What a proof now has to contain

A successful general proof must be **time-window-specific**, not a global semigroup gradient contraction. It must exploit that at times near `t_mix=Theta(log N)` the finite heat kernel has already wrapped around the finite quotient, a feature deliberately absent on the infinite tree. In particular, it needs either:

- direct varentropy concentration at the finite mixing scale; or
- a lower bound on `gamma(mu_t)` only for `t` in the transition window, using global finite geometry/transitivity in an essential way.

Any argument that localizes entirely to bounded-radius tree geometry cannot distinguish known cutoff high-girth expanders from the infinite tree obstruction above.

### (d) Simplest source-valid subclass still unproved by R16

The cleanest remaining subclass is still arbitrary fixed-degree **Cayley expanders** with symmetric generators, but now the required method is sharper: it must control the restricted local Poincare/varentropy quantity near mixing without relying on conjugacy invariance or a global relaxed sub-commutation estimate.

### (e) Nearest solved problems and their missing ingredient

- Hermon--Huang--Pedrotti--Salez solve conjugacy-invariant group walks via a trajectory rearrangement unavailable for arbitrary generating sets.
- Pedrotti--Salez reduce cutoff to the non-equilibrium local Poincare constant and explicitly permit restricting it to the mixing window. Their global relaxed-subcommutation suggestion is now ruled out as a universal high-girth route by C11--C12; the **restricted** local-Poincare formulation survives and becomes the more credible target.
- Altschuler proves cutoff for long-range expanders; this uses global volume-growth information beyond ordinary spectral expansion and is therefore not contradicted by the tree harmonic obstruction.

## 9. Recovery choice and next methods

**Chosen recovery: prove the simplest still-unproved special case, but abandon global sub-commutation.**

The final permitted I0112 recovery attempt will target the restricted mixing-window local Poincare constant for fixed-degree Cayley expanders directly. The desired statement is of the form

\[
\inf_{t\in[t_{\rm mix}(1-\varepsilon),\,t_{\rm mix}(\varepsilon)]}
\gamma(\mu_t)\,\log|G|\to\infty,
\]

or a source-valid subclass theorem strong enough to move the provisional family gate.

The next unused Section-B probes on I0112 are:

- **#4 PROVE SOMETHING WEAKER, COMPLETELY:** isolate a nontrivial Cayley-expander subclass characterized by a finite-time heat-kernel regularity condition and prove cutoff directly from the restricted local Poincare inequality;
- **#8 DISCRETIZE:** only after a candidate inequality is written, compute exact generalized-eigenvalue local Poincare constants for small Cayley examples at selected heat-kernel times to search for the obstruction pattern;
- **#25 COUNT THE SAME THING TWICE:** rewrite the evolving weighted Dirichlet form using convolution/path counts and seek a second count that forces boundary mass once the finite walk has wrapped around the group.

If that next invocation again leaves `W_exp` unchanged, it is the **third stuck episode** on this hard target and the controlling policy requires an I0112 handoff and rotation to the next eligible HARD OUTSIDE source. No further I0112 recovery is permitted after that point without a later reassignment carrying a genuinely fresh route.

## 10. R12 audit and model/scheduler escalation

The newest R12 report is I0060/FPP Question 17, status `PARTIAL / OPEN`, with `delta_cert` still `UNMEASURED`. There is no complete R12 package to audit; `R16_AUDIT_R12=PENDING_NOT_READY`.

The model-control situation is unchanged. The exposed scheduler interface supports prompt/title/schedule/timing/enabled-state changes but exposes **no model selector and no reasoning-effort selector**. GPT-6/maximum can therefore only be requested in prompt text, not enforced or authenticated here. Repository policy records that a P26 prompt update succeeded in one authorized context while other task IDs returned `You cannot modify this task`; such denials are ownership/context restrictions. The legitimate remedy is an authorized workspace/task-owner interface or platform support that exposes model/reasoning controls and correct ownership. I did not modify scheduler state and did not attempt a permission bypass.

## 11. Checker/artifact policy

No exact-arithmetic artifact was created. C11 and C12 are theorem-sized analytic claims with complete proofs above; there is no finite numerical core whose correctness would be improved by a checker. This is consistent with the 90/10 policy and avoids creating evidence-of-execution artifacts without metric movement.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  track: R16
  source:
    id: I0112
    author: Justin Salez
    year: 2025
    locator: arXiv:2508.21055v1, Problem 2.3
  target: every bounded-degree vertex-transitive expander sequence exhibits total-variation cutoff
  metric:
    name: W_exp
    before: 1/2 provisional
    after: 1/2 provisional
  movement: NO_MOVEMENT
  unchanged_count: 4
  status: PARTIAL
  stuck_state: STUCK_RECOVERY_2
  methods: [6, 13, 21]
  exact_evidence:
    - R16-I0112-C11: on the infinite d-regular tree, the optimal sub-commutation factor psi_d(t) tends to infinity
    - R16-I0112-C12: no uniform Ce^{-2 kappa t} sub-commutation can hold on all finite d-regular large-girth graph families
  finite_checker: NOT_APPLICABLE_ANALYTIC_PROOF
  audit_ids:
    P26_I0112: PENDING
    second_other_track_I0112: PENDING
    R16_directed_R12: PENDING_NOT_READY
  remaining_obligation: prove a direct mixing-window local-Poincare/varentropy estimate for a genuinely broader source-admissible transitive/Cayley expander class, or hand off after the next unchanged stuck episode
```
