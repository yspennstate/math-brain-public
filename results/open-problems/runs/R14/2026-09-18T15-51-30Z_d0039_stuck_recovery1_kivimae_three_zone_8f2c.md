Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT on D0039: `B_spectrum: 2 -> 2`; authoritative shared stagnation count remains UNKNOWN. SECTION-I STUCK-RECOVERY-1/2. Methods actually used: #6 DEFORM TO A POINT YOU CAN SOLVE, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #22 READ THE FAILURES, NOT THE SUCCESSES.**

# R14 HARD OUTSIDE — D0039 stuck recovery 1: the root-Palm three-zone route

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / source problem OPEN.** This is the required first Section-I recovery after three consecutive post-move `2 -> 2` D0039 reports. In accordance with the hard-task rule, this run is a **thinking run**: it does not manufacture another auxiliary theorem, does not add a checker, and does not promote any new route algebra to a proved claim. The terminal handoffs of the negative-margin spherical perceptron, H0017, and Bradley D0036 remain in force.

The active exclusive target remains `operations/claims/D0039.md`: Bálint Virág, *Operator limits of random matrices*, ICM 2014 / arXiv:1804.06953, Section 4, Question 1, asking whether the semi-infinite beta-Hermite spectral measure has the same multifractal spectrum as a Gaussian multiplicative cascade with the same Hausdorff dimension.

The frozen metric remains

`B_spectrum = 2`.

Level 3 still requires a **proved nonzero-width interval** of beta-4 local-dimension level sets whose Hausdorff dimensions agree with the matched GMC spectrum. No such interval is proved here.

## 1. Continuity, exclusions, ownership, and fresh source/literature screen

Before research I reread/recovered:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and the current owner policy;
- `operations/claims/D0039.md`;
- the newest R14 report `runs/R14/2026-09-18T15-08-50Z_d0039_reciprocal_dirichlet_charge_insertion_5e8a.md` and the preceding D0039 reports;
- the neighboring R15 D0039 source screen;
- the D0039 intake/correction records surfaced by repository search.

The repository state still records D0039 as an exclusive R14 HARD_OUTSIDE claim, with no posting/source closure. The root R-series ledger is stale and still carries the old perceptron assignment; it explicitly instructs workers to recover the newer complete report rather than reset to that stale row. The shared numeric stagnation field therefore remains `UNKNOWN`; I do not replace it with a guessed fleet value.

Fresh bounded literature checks on 2026-09-18 again found no source-matching theorem closing Virág's **beta-Hermite** question. The closest current ingredients are:

1. **Pax Kivimae, EJP 29 (2024), arXiv:2012.09969**, *Gaussian multiplicative chaos for Gaussian orthogonal and symplectic ensembles*. Besides the small-power GSE GMC theorem, the paper proves an arbitrary-positive-power GOE/GSE/GUE fractional-moment relation and, crucially, a two-point **subcritical merging** version for points separated by more than `N^{-gamma}`, `gamma<1`.
2. **Junnila--Lambert--Webb, arXiv:2209.06548**, *Multiplicative chaos measures from thick points of log-correlated fields*. Their general route turns suitable exponential-moment asymptotics into thick-point/GMC measures; the CUE verification uses merging Fisher--Hartwig asymptotics.
3. **Lambert--Paquette, arXiv:2508.01458 (2025)**, which gives a bulk description of the Gaussian-beta characteristic polynomial simultaneously resolving the local Sine-beta component and the global/mesoscopic log-correlated component.
4. **Weiyang Fang, arXiv:2609.11543 (submitted 2026-09-10)**, which proves fourth-order Sine-beta fusion asymptotics and derivative-moment bounds in the fused local environment. Its finite-particle transfer at arbitrary beta remains conditional at the level relevant here; it does not itself give the beta-4 root-Palm multiscale theorem needed below.

This is a bounded current-status search, not a worldwide novelty certificate.

## 2. Required stuck item (a): the exact blocking statement

The preceding run reduced the stochastic obstruction to the derivative-only Gaussian-quadrature weights

\[
\widetilde q_{j,n}
=
\frac{|D_n'(\xi_{j,n})|^{-2}}
{\sum_{\ell=1}^{n}|D_n'(\xi_{\ell,n})|^{-2}},
\tag{2.1}
\]

where `xi_{j,n}` are the beta-4 quadrature roots. The deterministic CMS-Moran lemma is already on file, so a source-relevant level-3 advance now requires the following type of statement for **some nondegenerate interval** `I subset (1/4,1/2)`:

\[
\boxed{
\begin{gathered}
\#\{j:\ \widetilde q_{j,n}=n^{-x+o(1)}\}
=n^{\frac12-(x-\frac34)^2+o(1)}
\quad\text{for every }x\in I,\\[1mm]
\text{with quenched two-scale parent/child concentration strong enough to build}\newline
\text{the nested CMS-Moran tree at the corresponding quadrature cells.}
\end{gathered}}
\tag{DERIV-GMC_4(I)}
\]

The one-level exponent count alone is insufficient. The **two-scale quenched child estimate** is the part no route has supplied.

If `DERIV-GMC_4(I)` is proved, the already-established deterministic reduction converts it into

\[
\dim_H\{E:d_{\mu_4}(E)=\alpha\}
=1-\frac12(\alpha-\tfrac32)^2,
\qquad \alpha=2x,\ x\in I,
\tag{2.2}
\]

which would move `B_spectrum` from 2 to 3. Equation (2.2) remains conditional in this report.

## 3. Required stuck item (b): every route tried and the precise failure

The relevant route ledger is now short enough to state without hiding the blocker.

### Route 1: fixed-energy beta-4 kernel LDP

R14's level-2 work gives a speed-`log n` LDP at `E=0` for the positive Christoffel-kernel observable with the bulk quadratic rate. **Failure:** a deterministic-energy LDP is not a quenched count theorem at the random Gaussian-quadrature roots and has no parent/child nesting information.

### Route 2: two-phase / tangent branching

The two-phase paired-CGF calculation exhibits the correct logarithmic overlap law in a tangent model. **Failure:** it is a tangent-phase calculation; it does not prove an actual-energy, random-root, exponentially tilted multiscale statement.

### Route 3: subordinate/Weyl alignment

Jitomirskaya--Last gives the right conceptual local-dimension language. **Failure:** converting a single first-kind growth exponent to local dimension requires a complementary solution/alignment variable. This made the direct route strictly harder than necessary.

### Route 4: Gaussian quadrature + CMS

The exact quadrature weights and Chebyshev--Markov--Stieltjes inequalities directly bracket the true infinite spectral mass. **Success:** this removed the Weyl-alignment variable. **Failure:** it left a stochastic theorem for the quadrature-weight field.

### Route 5: reciprocal Dirichlet endpoint layer

The previous run proved that the independent endpoint Dirichlet/Gamma factor is polynomial-exponent neutral on the target window. **Success:** the endpoint layer is not the obstruction. **Failure:** the root derivative field (2.1) remains.

### Route 6: one-root marked-charge insertion

The exact identity from the preceding run converts one marked inverse-derivative moment into a **positive characteristic-polynomial insertion** in a one-particle-smaller same-potential beta-4 ensemble. **Success:** this connects the root field to current GSE moment technology. **Failure:** one marked root gives no two-scale child correlations.

### Route 7: import Kivimae's GSE GMC theorem verbatim

This is the first failure exposed sharply in the present recovery. In the one-root Palm identity, an inverse-derivative tilt `t` produces characteristic-polynomial power

\[
p=4-2t.
\tag{3.1}
\]

For the concrete interior test exponent selected below, `t=3/4` and hence `p=5/2`. Kivimae's **GMC convergence theorem itself** works only in its small-power/subcritical range; `p=5/2` is outside that range. Therefore the GSE GMC theorem cannot simply be quoted after Palm insertion. What survives and remains useful is the paper's **fractional-moment relation**, which permits arbitrary positive insertion powers, and its two-point merging estimate.

### Route 8: import Kivimae's two-point merging proposition

This gets much closer. For equal positive powers and two bulk points with

\[
|\lambda_1-\lambda_2|>N^{-\gamma},\qquad 0<\gamma<1,
\tag{3.2}
\]

Kivimae proves a uniform GOE/GSE/GUE moment relation with error of order

\[
O\!\left(\max\{N^{-1/6},N^{\gamma-1}\log N\}\right).
\tag{3.3}
\]

**Failure:** after the standard bulk rescaling, adjacent beta-Hermite roots live at the microscopic `N^{-1}` scale, where `N|\lambda_1-\lambda_2|=O(1)`. Kivimae explicitly remarks that the deterioration there is expected to be an artifact of the method, but Proposition 2.10 does not cover that microscopic collision regime.

### Route 9: use Fang's Sine-beta fusion theorem as the missing microscopic bridge

Fang now gives unusually sharp local fusion information and derivative moments in the Sine-beta/Hua--Pickrell environment. **Failure:** the presently available finite-particle transfer at arbitrary beta is not the full unconditional beta-4, random-root, exponentially tilted, nested two-scale estimate required by (2.1). It is a relevant local input, not the missing global theorem.

### Route 10: apply Junnila--Lambert--Webb directly

JLW need suitable exponential-moment asymptotics for the field and use merging Fisher--Hartwig control to pass to thick points/GMC. **Failure:** our field is sampled at **random roots under a Palm shift**, and the desired object is a quenched nested quadrature tree rather than a deterministic Lebesgue-mesh chaos measure. The JLW theorem is a template once the Palm/root moment estimates exist; it does not supply those estimates.

## 4. Method #22 — READ THE FAILURES: Kivimae already shows how not to solve the microscopic gap

The most useful finding of this recovery is not a new lemma; it is that Kivimae's own proof does **not** insist on a perfect microscopic merging theorem.

Kivimae's Proposition 2.10 treats the subcritical merging zone (3.2). His Remark 2.12 says the apparent divergence when `N|lambda_1-lambda_2|=O(1)` is expected to be a proof artifact. In the GMC proof, the two-point integral is then split into three zones:

1. a separated/far zone, handled by the standard moment relation;
2. an intermediate merging zone, handled by Proposition 2.10;
3. a very-near-diagonal zone, handled crudely by Cauchy--Schwarz plus one-point moment bounds in the `L^2` range.

This changes the R14 target materially. The next attempt should **not** try to prove a full microscopic beta-4 fusion theorem before doing anything else. It should try to reproduce this same three-zone estimate **after Palm insertion** and ask whether the very-near-root pairs can be discarded by a crude moment bound on a nonzero exponent window.

That is precisely the sort of move the previous route was missing.

## 5. Method #17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE: freeze a concrete interior exponent

The cleanest test point is

\[
x=\frac38,\qquad \alpha=2x=\frac34.
\tag{5.1}
\]

For the target bulk rate

\[
I(x)=(x-\tfrac34)^2,
\]

this gives

\[
I(3/8)=\frac9{64},\qquad
c_{\rm der}(3/8)=\frac12-\frac9{64}=\frac{23}{64},
\tag{5.2}
\]

and the target Hausdorff dimension is

\[
2c_{\rm der}(3/8)=\frac{23}{32}.
\tag{5.3}
\]

The corresponding positive heavy-weight tilt suggested by the quadratic rate is

\[
t=2(\tfrac34-x)=\frac34,
\tag{5.4}
\]

so the one-root Palm charge (3.1) is

\[
p=4-2t=\frac52.
\tag{5.5}
\]

These numbers expose both the opportunity and the obstruction:

- `p=5/2` is too large for a verbatim application of Kivimae's GSE **GMC convergence** theorem;
- the arbitrary-positive-power **moment relation** remains the relevant part of Kivimae's technology;
- `I=9/64<1/4` lies safely inside the second-moment regime that R14's earlier branching calculation identified as the natural window for a Paley--Zygmund/Frostman construction.

Equations (5.1)--(5.5) select the simplest serious special case. They are a diagnostic/target selection, not a proof of the root-field spectrum.

## 6. Method #6 — DEFORM TO A SOLVABLE POINT: two ways to avoid exact microscopic fusion

There are now two credible deformations away from the unresolved adjacent-root regime.

### 6.1 The stronger route: Kivimae's three-zone split

For the second moment of a root-Palm counting/Frostman measure, split root pairs by their rescaled separation exactly as Kivimae does for the GSE chaos:

- far pairs: use the arbitrary-power fractional-moment relation;
- intermediate pairs `N^{-gamma} << Delta << 1`: use the subcritical merging proposition;
- microscopic pairs `Delta=O(N^{-1})`: do **not** seek exact asymptotics; prove their total contribution negligible using a one-point high-moment bound plus the fact that only `O(1)` near neighbors occur per root.

If this closes at `x=3/8`, it would prove a meaningful one-exponent root-count theorem without solving the full fusion problem. To reach `B_spectrum=3`, that one exponent would then have to be widened to an interval and upgraded to nested quenched child counts.

### 6.2 Backup route: mesoscopic quadrature blocks

Group `N^delta` adjacent roots into a block for fixed small `delta>0`. Its rescaled width is of order `N^{-1+delta}`, which is inside Kivimae's subcritical merging regime after choosing a fixed `gamma<1` compatible with `delta`. The block aggregation costs at most an `N^{delta}` polynomial factor. One could try to prove the exponent law for every fixed `delta`, then let `delta downarrow0` in a diagonal construction.

**Failure still present:** Kivimae's proposition is stated for fixed `gamma<1`; taking `delta downarrow0` across scales requires a quantitative two-parameter argument, and the block sums still need parent/child control. This is a deformation plan, not a proved escape.

## 7. The two-root Palm algebra that the port must formalize (NOT PROMOTED)

The one-root marked identity is already proved in the preceding report. The natural two-root analogue is transparent at the density level: marking distinct eigenvalues `x,y` in a beta-4 gas contributes

- a marked-pair Vandermonde factor `|x-y|^4`;
- two inverse-derivative tilts, each contributing `|x-y|^{-2t}`;
- interactions with every remaining particle of powers `|x-z|^{4-2t}|y-z|^{4-2t}`.

Thus the route should lead, after the exact same-potential partition-function bookkeeping is carried out, to a two-root Palm integral with the schematic core

\[
|x-y|^{4-4t}
\;\mathbb E_{N-2}^{(N)}
\left[|D_{N-2}(x)D_{N-2}(y)|^{4-2t}\right].
\tag{7.1}
\]

I deliberately do **not** label (7.1) a theorem in this thinking-only recovery. The next mathematical run must write the full normalization, ordered/unordered pair convention, and potential rescaling correctly before using it. The point of (7.1) here is only to show that the desired second moment has exactly the same two-point positive-characteristic-polynomial shape treated by Kivimae away from the microscopic diagonal.

## 8. Required stuck item (c): what a proof must contain that no route currently contains

A proof moving `B_spectrum` must now contain **all three** of the following, not another fixed-energy cumulant lemma:

1. **Two-root Palm normalization.** An exact same-potential beta-4 identity for two marked inverse-derivative tilts, with the finite-`N` partition-function factors and scaling convention matched to the GSE moment theorem.
2. **A root-Palm three-zone second-moment bound.** At least on one compact tilt interval, the far and intermediate zones must inherit Kivimae-type moment asymptotics, while the microscopic `N Delta=O(1)` pairs must be shown negligible by a crude integrable bound or else handled by genuine fusion asymptotics.
3. **A quenched/nested conversion.** Annealed one- and two-point moments must be converted into enough same-environment parent/child concentration for the CMS-Moran tree. A one-scale expected count is not `DERIV-GMC_4(I)`.

No route so far contains item 3, and items 1--2 have not yet been written in the exact beta-Hermite root-Palm normalization.

## 9. Required stuck item (d): simplest special case still unproved

The simplest source-relevant special case now worth isolating is:

\[
\boxed{
\beta=4,\quad \alpha=\frac34\ (x=\frac38):\qquad
\dim_H\{E:d_{\mu_4}(E)=3/4\}=\frac{23}{32}\ ?
}
\tag{9.1}
\]

Even the weaker precursor

\[
\#\{j:\widetilde q_{j,n}=n^{-3/8+o(1)}\}
=n^{23/64+o(1)}
\tag{9.2}
\]

with a two-scale second-moment/branching bound is not proved. This is the correct simplest test because it lies strictly inside the previously identified `L^2` window and maps to the concrete Palm charge `p=5/2`.

## 10. Required stuck item (e): nearest solved problem and what it has that D0039 lacks

The nearest solved shape is now **Kivimae's beta=4 GSE characteristic-polynomial GMC theorem and its proof**, supplemented by the Junnila--Lambert--Webb exponential-moment-to-thick-point framework.

What Kivimae has that D0039 lacks:

- deterministic spatial integration rather than a random-root Palm mesh;
- exact GOE/GSE/GUE fractional-moment relations in the relevant finite ensemble;
- a subcritical two-point merging theorem;
- a successful three-zone `L^2` argument that avoids needing exact microscopic merging asymptotics.

What D0039 additionally requires:

- the **Palm charge shift** generated by conditioning on an eigenvalue and inserting inverse derivatives;
- random-root counts/weights rather than a Lebesgue-density chaos;
- a same-environment multiscale nesting theorem compatible with Gaussian quadrature/CMS.

Lambert--Paquette gives the right local/global decomposition for the Gaussian-beta characteristic polynomial, and Fang supplies new Sine-beta fusion information, but neither presently supplies this complete root-Palm/nested bridge.

## 11. Exactly one recovery choice

**Recovery choice: PORT THE TECHNIQUE FROM THE NEAREST SOLVED PROBLEM.**

The technique to port is not “Kivimae GMC” as a black box. It is the **three-zone second-moment architecture** of Kivimae's proof, inserted after the exact root-Palm change of measure and then fed into the already-proved CMS-Moran deterministic reduction.

This recovery does not yet move the metric. It has, however, replaced the overly strong missing obligation “prove full microscopic beta-4 fusion at random roots” by a weaker and more targeted question:

> Can the microscopic pair contribution be discarded by a Kivimae-style one-point moment bound at `x=3/8`, so that only the already-covered separated/subcritical-merging zones remain?

That is the question the second permitted recovery should answer before D0039 is handed off.

## 12. Next methods and hard-task limit

If D0039 is still unchanged at the next invocation, that invocation is **STUCK-RECOVERY-2/2**. It should freeze the concrete special case (9.1), write the exact two-root Palm normalization, and attempt the three-zone second-moment estimate rather than widening the target.

The next nonrepeating Section-B triple is:

- **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT:** use the tilt parameter around the concrete `t=3/4` point and determine the maximal open tilt window in which the very-near-diagonal contribution is integrable;
- **#25 COUNT THE SAME THING TWICE:** derive the root-pair second moment both from marked beta-4 density/Palm insertion and from the quadrature-weight count, forcing all powers and normalizations to agree;
- **#30 ONE SCALE, ONE DIRECTION AT A TIME:** first prove or refute the one-scale `x=3/8` second-moment statement before attempting a full interval or multiscale Frostman tree.

If the same blocking obligation survives that second recovery and no independent metric movement intervenes, the next stuck episode must terminally hand D0039 off and rotate to an ownership-clear HARD_OUTSIDE successor. No third recovery is authorized.

## 13. Structured ledger_delta

```yaml
ledger_delta:
  track: R14
  lane: HARD_OUTSIDE
  target: D0039
  source: "Balint Virag, Operator limits of random matrices, ICM 2014 / arXiv:1804.06953, Section 4, Question 1"
  status: PARTIAL
  metric:
    name: B_spectrum
    before: 2
    after: 2
    movement: false
  authoritative_shared_stagnation_count: UNKNOWN
  own_post_move_flat_sequence: 4
  section_I_this_run: STUCK_RECOVERY_1_OF_2
  methods_used: [6, 17, 22]
  thinking_run: true
  new_theorem_claims: 0
  new_finite_claims: 0
  checker: none
  blocker:
    name: DERIV-GMC_4
    statement: "quenched multiscale parabola and parent/child concentration for normalized inverse derivative weights at beta 4 on a nonzero-width x interval"
  recovery_choice: "PORT_THE_TECHNIQUE_FROM_NEAREST_SOLVED_PROBLEM"
  port_target: "Kivimae GSE three-zone second-moment/GMC argument, after root-Palm insertion, followed by the existing CMS-Moran transfer"
  simplest_unproved_case:
    beta: 4
    local_dimension_alpha: "3/4"
    derivative_weight_exponent_x: "3/8"
    target_count_exponent: "23/64"
    target_Hausdorff_dimension: "23/32"
    diagnostic_tilt_t: "3/4"
    Palm_characteristic_polynomial_power: "5/2"
  precise_failures:
    - "fixed-energy LDP has no random-root or nested child counts"
    - "direct Kivimae GSE GMC theorem is outside its small-power range after the Palm charge shift"
    - "Kivimae subcritical merging theorem stops before microscopic N*Delta=O(1) root separation"
    - "Fang fusion does not currently provide the complete arbitrary-beta finite-particle root-Palm/nested estimate"
    - "JLW needs exponential-moment input for the root-Palm field rather than supplying it"
  key_new_route_diagnosis:
    - "Kivimae's proof itself avoids exact microscopic merging by a three-zone split and a crude near-diagonal L2 bound"
    - "test whether the same architecture makes adjacent-root fusion unnecessary on an interior beta-4 exponent window"
  literature_refresh_utc: "2026-09-18"
  no_source_matching_full_solution_found_in_bounded_search: true
  next_section_I_if_unchanged: STUCK_RECOVERY_2_OF_2
  next_methods: [5, 25, 30]
  shared_roots_edited: false
  peer_files_edited: false
  email: false
  drive: false
  public_posting: false
  permissions_changed: false
  workflow_executed: false
  scheduler_modified: false
```

## 14. Model / scheduler-control note

The limitation recorded by repository policy is still the limitation of the exposed task surface: prompt/title/schedule/timing/enabled controls exist, but no binding model-family selector, reasoning-effort selector, guaranteed-runtime field, or authenticated completed-run model telemetry is exposed. Thus `GPT-6 / maximum` remains prompt text only here and cannot truthfully be reported as applied.

The historical `You cannot modify this task` response is an authorization-context boundary. The lawful workaround remains the authorized owning/admin context or platform support; this worker did not bypass permissions, duplicate a schedule, or mutate scheduler state.
