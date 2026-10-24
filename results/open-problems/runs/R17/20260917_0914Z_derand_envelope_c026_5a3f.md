Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6/maximum was requested, but the exposed scheduler still has no model or reasoning selector. MOVEMENT: certified width 0.03361318654239782538084052 -> 0.033613186542397825380217. Methods tried: 2, 10, 25.

# R17 run 2026-09-17 09:14Z — C026 deterministic-floor cone and active-envelope probe

Status: **PARTIAL**. Source problem: **OPEN**.

## 1. Continuity, source and exclusion checks

I continued from the newest R17 report, `runs/R17/20260917_0814Z_c025_activepf_71e3.md` @ `a561047638ca0904e36387f79619d68df0605c9e`; I did not restart the Lueker construction.

I also re-read the controlling campaign/exclusion material (`probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, and `operations/NEW_METHODS_2026-09-16.md`). No posted/excluded result closes the binary Chvatal-Sankoff source target. R18's neighboring HUW target is already packaged and audit-complete, so there was no reason to spend this run duplicating an audit.

Fresh dated source check, 2026-09-17:

- arXiv:2212.01582 (Tiskin) still describes determination of the binary Chvatal-Sankoff coefficient as unresolved.
- arXiv:2407.10925 (Heineman et al.) still states exact Chvatal-Sankoff constants as open and gives the rigorous binary lower endpoint `0.792665992`.
- Exact-string searches for the sharpened `0.826279178542397825...` endpoint found no accessible mathematical source. This is **not** a novelty certificate; publication priority is **UNVERIFIED**.

The fixed source, alphabet, distribution and normalization are unchanged: two independent iid uniform binary strings. Independent Bernoulli matching was not used.

## 2. Metric before this run

The retained lower endpoint is

\[
L=0.792665992=\frac{99083249}{125000000}.
\]

C025 had certified

\[
U_{025}
=\frac{20656979463559945634521013}
       {25000000000000000000000000}
=0.82627917854239782538084052,
\]

hence

\[
W_{025}=U_{025}-L
=0.03361318654239782538084052.
\]

The C025 exact parameter was

\[
z_*=\frac{320896250000000001555829}{10^{24}}.
\]

The finite operator remains Lueker's true dependent-string history-8 automaton with `6,419,109` reachable states. Its regenerated transition table again matched the already-recorded SHA-256

`c6d12e75e87b7c6b00a95f0c7f3580fa1cdee4996ce690a2f922f7eaeea1fbd1`.

## 3. New idea before code: derandomize the positive witness

C025 used seeded stochastic rounding of an approximate Perron direction. That rounding is legitimate because the final all-state cone scan was exact, but it raises a natural negation to attack:

> Is the stochastic rounding actually helping the certified cone maximum, or can a deterministic lattice projection do better?

I therefore fixed the same true-string `h=8` operator and the same exact `z_*`, recomputed a deterministic approximate Perron direction by power iteration, and then used the completely deterministic integer projection

\[
V_i=\max\{1,\lfloor S v_i\rfloor\},
\qquad S=18\cdot 10^{18}.
\]

The power iteration is only a **search device**. No floating-point inequality is used in the theorem. Once the integer vector is frozen, every component ratio is recomputed with exact multiprecision integer/rational arithmetic.

This is Section-B move **10 (DERANDOMIZE)**. It also implements move **2 (ATTACK THE NEGATION)** against the implicit hypothesis that the seeded C025 rounding was already locally optimal.

## 4. Exact all-state cone certificate C026

The new checker is

`artifacts/R17/20260917_0914Z_derand_envelope_c026_exact_cone_checker.cpp`

creation commit `82a270a6f17019755f25b9ecf8417de31170bd95`.

Its executed output is

`artifacts/R17/20260917_0914Z_derand_envelope_c026_exact_cone_checker_output.txt`

creation commit `8c002502a24fc0eab230b6df4a59a7631eaaf006`.

The exact scan covers all `6,419,109` states. It gives maximum state `3194724` and minimum state `4591190`, and certifies

\[
A_8(z_*)V\le \lambda_{026}V
\]

componentwise with

\[
\lambda_{026}=
\frac{
276956593963024041276868865537229787866977713766800486192609348116933979994322388660419915295651421954345692954069536680021619448973121399254142401074736761271584886999617569305776597906676298472939031374055058917968076875499146958477
}{
810234905961502854639100242552083250335501200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
}.
\]

The same positive vector also yields the exact lower Collatz ratio

\[
\lambda_-=
\frac{4121657586976442629438294470492434483997550276517824511136431669}
{12057885315542350480000000000000000000000000000000000000000000000},
\]

but this lower ratio is only a diagnostic on the fixed finite operator. It is **not** a lower bound on `gamma_2`.

The archived exact cone output ends

`ALL_EXACT_CHECKS_PASS`.

The checker's printed `bound_display` is intentionally not used for the theorem, because it is only a `long double` display. The endpoint conversion below is separately certified with exact rational arithmetic.

## 5. Exact endpoint conversion

Lueker's finite-history theorem, already reconstructed and used in C018--C025, says that a positive cone certificate

\[
A_8(z)V\le\lambda V
\]

implies

\[
\gamma_2\le
\frac{2[-\log(2z)]}{-\log \lambda}.
\]

The exact endpoint compiler is

`artifacts/R17/20260917_0914Z_derand_envelope_c026_endpoint_checker.py`

creation commit `e9e1760cdda5aba8eab7f8733b76836c6751c952`.

Its executed output is

`artifacts/R17/20260917_0914Z_derand_envelope_c026_endpoint_checker_output.txt`

creation commit `20108f8d2bb19418bf982ba9fc98c808849f11e2`.

For rational `0<x<1`, it uses

\[
-\log x
=2\sum_{k\ge0}\frac{u^{2k+1}}{2k+1},
\qquad
u=\frac{1-x}{1+x},
\]

with the positive exact tail bound

\[
0<
-\log x-2\sum_{k=0}^{m-1}\frac{u^{2k+1}}{2k+1}
\le
\frac{2u^{2m+1}}{(2m+1)(1-u^2)}.
\]

All comparisons are performed with exact rational arithmetic. The compiler proves

\[
0.82627917854239782538021644568448013670833752422751206674481599629926276786166567341407227834069877064572400353
< B_{026}
\]

and

\[
B_{026}<
0.82627917854239782538021644568448013670833752422751206674481599629926276786166567341407228685690047859582836126.
\]

Therefore the rational number

\[
\boxed{
U_{026}=\frac{826279178542397825380217}{10^{24}}
=0.826279178542397825380217
}
\]

is a rigorous deterministic upper endpoint.

The endpoint output ends

`ALL_EXACT_CHECKS_PASS`.

## 6. Metric movement

The new certified interval is

\[
\boxed{
0.792665992\le\gamma_2\le0.826279178542397825380217
}.
\]

The tracked width is now

\[
\boxed{
W_{026}
=\frac{33613186542397825380217}{10^{24}}
=0.033613186542397825380217
}.
\]

The exact decrease from C025 is

\[
\boxed{
U_{025}-U_{026}
=\frac{3897}{6250000000000000000000000}
=6.2352\times10^{-22}.
}
\]

This is extremely small, but it is genuine movement in the fixed deterministic metric, so the unchanged count resets to `0`.

## 7. Method 25: count the same thing twice — active-envelope attempt

For a **fixed integer witness** `V`, each component ratio can be grouped by `|l|`. The 30 raw transition contributions therefore collapse into eight exponent bins. Each row ratio is then an explicit rational function of `z` rather than an opaque sparse-matrix entry.

This suggested balancing two rows that appeared active on opposite sides of the C025 parameter. Their exact aggregates were:

- state `6344889`: `V_i=309609522704343234`, bins `[1027745979060680115,0,0,0,0,0,0,0]`;
- state `47135`: `V_i=17999999999999999999`, bins `[36000000000000000000,54559440304542574507,42866587258095872038,38212706030658790842,36426635438757865337,35908533776756180663,35829146632172178647,35823695067767376140]`.

Their equality reduces to one explicit degree-7 polynomial:

`1687856253362891199909536911687638*z^7 + 24579015943513551175117916611959744*z^6 + 160409208284668555266907324733395716*z^5 + 552984463474709353812450687784783170*z^4 + 1440885945549497748553671613111227864*z^3 + 3620218650762389279324332443651244746*z^2 - 24245607077441419196065371493885655523*z + 7353484805735885644972254020939319885`.

The root near the current parameter is approximately

`0.32089625000000000167321265257368488...`.

However, the decisive all-state exact probe at

\[
z=\frac{3208962500000000016732}{10^{22}}
\]

showed that the global maximum is state `3194724`, not either member of that pair. Thus a two-row balance is **not** the global active envelope at this microscopic scale.

This is the outcome of Section-B move **25 (COUNT THE SAME THING TWICE)**: the binning is useful, but the simplest two-active-row gluing fails. The next finite attack should enumerate the actual top active rows and construct the piecewise-rational maximum envelope, rather than balance only two visually active constraints.

## 8. What was learned from the three methods

### 2 — ATTACK THE NEGATION FIRST

The C025 seeded stochastic rounding was not endpoint-optimal. A deterministic floor projection produces a strictly smaller exact all-state maximum and therefore a smaller certified `U`.

### 10 — DERANDOMIZE

The final C026 witness has no random seed and no confidence statement. Candidate generation is deterministic, and the theorem rests solely on an exact componentwise cone scan plus exact rational logarithm enclosures.

### 25 — COUNT THE SAME THING TWICE

Grouping transitions by `|l|` turns every frozen-witness row ratio into an explicit low-degree rational function of `z`. The first two-row balance failed because a third state takes over globally. This failure identifies the correct next object: the full finite active-row envelope.

## 9. Prior art / novelty qualification

The source problem is not claimed solved. The new number is an R17 self-certified strengthening of the Lueker-history-8 upper certificate, not a determination of `gamma_2`.

A bounded current search did not locate this sharpened endpoint in accessible literature. That negative search does not establish novelty or priority. **Publication priority remains UNVERIFIED.**

No independent outside audit of C026 was performed in this run. Closure criteria are therefore not in view even apart from the source problem remaining open.

## 10. Scheduler/model-control status

The exposed task interface still supplies prompt/title, scheduling/timing, enabled state and notification/email settings, but **no model field and no reasoning-effort field**. Accordingly, GPT-6/maximum remains prompt-only and cannot be enforced from this scheduler surface. The actual model on this run is GPT-5.6 Sol; reasoning telemetry is UNVERIFIED.

The root `RESULTS.md` also records that the old P26 `You cannot modify this task` event was context/ownership-specific: a later authorized P/C context succeeded in updating P26, while other contexts denied some task edits. The legitimate workaround is therefore the owning/authorized workspace context or product/platform support, not a permission bypass or duplicate task. I made no scheduler changes this run.

## 11. Next research direction

C026 removes stochastic rounding as a necessary ingredient and shows that more seed sweeps are not the right next step. The strongest next finite route is:

1. retain the true dependent-string `h=8` operator and the exact C026 witness;
2. enumerate the top exact row-ratio functions in a rational neighborhood of `z_*` using the eight `|l|` bins;
3. construct the full piecewise-rational active envelope and optimize its maximum exactly or with outward-certified algebraic intervals;
4. if this envelope proves the `h=8` gain is exhausted at a negligible scale, change the canonical/history construction rather than manufacture more endpoint digits.

The only Section-B method never yet used anywhere on R17 after this run is #17; a future run should include it, together with two nonconsecutive methods applied to genuinely new routes.

## ledger_delta

```yaml
ledger_delta:
  track: R17
  source: "Chvatal-Sankoff binary longest-common-subsequence constant"
  metric: "certified interval width U-L"
  lower_endpoint: "0.792665992"
  upper_before: "0.82627917854239782538084052"
  upper_after: "0.826279178542397825380217"
  width_before: "0.03361318654239782538084052"
  width_after: "0.033613186542397825380217"
  exact_upper_decrease: "3897/6250000000000000000000000"
  upper_decrease_decimal: "6.2352e-22"
  status: PARTIAL
  source_status: OPEN
  unchanged_count: 0
  methods: [2, 10, 25]
  remaining_obligation: "Move beyond microscopic fixed-h=8 witness slack: certify the full active-row rational envelope in z, or change the canonical/history construction."
  evidence:
    - "artifacts/R17/20260917_0914Z_derand_envelope_c026_exact_cone_checker.cpp @ 82a270a6f17019755f25b9ecf8417de31170bd95"
    - "artifacts/R17/20260917_0914Z_derand_envelope_c026_exact_cone_checker_output.txt @ 8c002502a24fc0eab230b6df4a59a7631eaaf006"
    - "artifacts/R17/20260917_0914Z_derand_envelope_c026_endpoint_checker.py @ e9e1760cdda5aba8eab7f8733b76836c6751c952"
    - "artifacts/R17/20260917_0914Z_derand_envelope_c026_endpoint_checker_output.txt @ 20108f8d2bb19418bf982ba9fc98c808849f11e2"
  independent_audits: []
```
