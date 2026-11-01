Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `B_cat >= b20_global -> B_cat >= b21_desc > (20/3) b20_global`; the exact corridor replacement factor is `20250376323381968973878014720115467974667656528406168989928376556656242171778902900194077764678732746446886563465969472 / 3035407598828408687586052566685944043089858522392691278993631382621774633640859988880503257952761490410138991736595541`, approximately `6.671386185894147`; diagnostic `log10` bound improves `-49.25315461739025 -> -48.42893853604687`; unchanged count remains `0`. Methods actually used: B18, B20, B27.**

# R08 CLOSABLE OUTSIDE — E0011 catalyst/ZGB: descriptor-carrying corridor and protected guard memory

Run date: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Active target: **E0011**, Rick Durrett, *Coexistence in stochastic spatial models* (2009), Problem 5, original two-dimensional no-stirring catalyst/ZGB process.  
Status after this run: **PARTIAL / source OPEN under bounded current-literature checking**.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, ownership, and stale native title

I continued from the newest complete R08 report `runs/R08/20260919T1232Z_e0011_global_fixed_top_b20_3d7a9e.md` and its exact global-uniformization checker rather than restarting from the stale scheduler title.

The controlling later ownership file is `operations/claims/E0011.md`. It assigns E0011 exclusively to R08 and explicitly records Hasebe--Ueda Problem 3.11 / `I0082` as **RETIRED/FROZEN at `2/3` after six supported unchanged runs**. I0082 was therefore not reopened. The old R08 FPP route, posted Hasebe--Ueda Problem 3.3, and R19's distinct stable-law convolution work remain excluded from this slot.

Before research I refreshed/recovered the current campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the I0082 and E0011 claims, the newest own R08 report/checker, and the newest neighboring R07/R09 lifecycle reports. R07 is at a terminal successor-admission gate after its I0077 handoff; R09 is also at a successor gate. Neither owns E0011.

The large intake ledgers are too large to render byte-for-byte through the connector in one response. I used exact-ID/source/ownership searches and the current claim/queue state rather than falsely claiming a visual reread of every unrelated intake row.

## 2. Fresh bounded source/current-literature check

The dated search was refreshed on 2026-09-19 for the exact Durrett Problem 5 / catalyst / ZGB / no-stirring scope and recent 2025--2026 ZGB work.

- Durrett, arXiv:0906.2293 / Ann. Appl. Probab. 19 (2009), still presents nine challenging open problems and is the source for E0011.
- Fernandes--da Silva, arXiv:2501.07066 (2025), studies a modified ZGB model in which CO is allowed to **desorb**.
- Andrade--Girardi, Phys. Rev. E 114, 024136, published 18 August 2026, studies a ZGB extension with **reactive sulfur**.

Those recent papers do not prove coexistence for the exact original no-stirring source process. I found no later primary source-matching theorem in this bounded search. This is bounded negative evidence only, not a worldwide-open or novelty certificate.

## 3. Entering metric and the information discarded by b20

The frozen metric remains

\[
B_{\rm cat}:=\sup_C b(C),
\]

where `C` ranges over complete source-valid finite protected two-child Harris-block certificates at the rational anchor `p=1/2`.

The entering certified bound is

\[
B_{\rm cat}\ge b_{20,\rm global},
\qquad
\log_{10}b_{20,\rm global}\approx-49.25315461739025.
\]

The `b20_global` recursion already merged the eight post-bootstrap corridor modules into one fixed deterministic top. Its remaining deliberate loss was at stage handoff. If `s` was a target descriptor for stage `j`, the continuation was replaced by

\[
\min_{t\in E_{j+1}}U_{j+1}(n,t),
\tag{3.1}
\]

forgetting the actual descriptor produced by the preceding random history.

Equation (3.1) is source-valid, but it lets the exterior rewrite coordinates whose values have just been observed inside the protected overlap. B18 asks whether this loss can be removed without changing the universal quantifier.

## 4. B18 — replace the scalar reset by an exact compatibility relation

For two consecutive horizontal modules, the next local frame is the current local frame translated by one lattice column. If `c` is a next-frame state coordinate, it corresponds to the current coordinate `c+(1,0)`.

The persistent 14-cell descriptor has exactly ten such state-to-state overlaps:

\[
\begin{aligned}
(-2,0)&\leftarrow(-1,0), &(-2,1)&\leftarrow(-1,1),\\
(-1,-1)&\leftarrow(0,-1),&(-1,0)&\leftarrow(0,0),\\
(-1,1)&\leftarrow(0,1),&(-1,2)&\leftarrow(0,2),\\
(0,-1)&\leftarrow(1,-1),&(0,0)&\leftarrow(1,0),\\
(0,1)&\leftarrow(1,1),&(1,0)&\leftarrow(2,0).
\end{aligned}
\tag{4.1}
\]

Two further geometric overlaps land only in the old untracked `FULL` halo, so I deliberately leave them free; this makes the relation weaker and therefore conservative.

For a target state `s`, define

\[
R_x(s):=\{t\in E_{\rm beh}:t\text{ agrees with }s\text{ on all ten pairs in (4.1)}\}.
\]

The six required target vacancies at current columns `-1,0,1` become the next generated-shield vacancies at columns `-2,-1,0`, so every actual translated stable continuation belongs to `R_x(s)`.

The correct boundary condition is therefore

\[
U_j(n,s)=\min_{t\in R_x(s)}U_{j+1}(n,t),
\qquad s\in A,
\tag{4.2}
\]

for the five literal horizontal transitions `h3->h4`, ..., `h7->h8`.

The first exact checker compared (4.2) to the old scalar-reset recursion on the same common clock `H=7992`, same deterministic horizon, same hazards, and same entrance classes. It regenerated `12,201` base entrances and `1,743` generated-shield entrances. Relation-aware coefficients dominate the scalar coefficients for every tick `0<=n<=40` and are strictly larger at exactly

\[
\boxed{n=19,20,\ldots,29}.
\]

Using only this horizontal memory would already improve the exact fixed-top corridor factor by `1.2733950027459777...`, and the exact arithmetic check proves that factor is greater than `5/4`.

That was useful, but B20 exposed a larger piece of forgotten state at the two guard turns.

## 5. B20 — why naive guard gluing initially fails

The guard modules are rotated, not literal horizontal translates. Their physical frame maps at spacing `L=8` are

\[
D(x,y)=(5+y,-x)
\]

for `g_down`, and

\[
U(x,y)=(4+y,x+1)
\]

for `g_up`.

A naive relation using only the six-vacancy `g_down` target is insufficient. The next `g_up` base class needs global sites `(4,0),(4,1),(5,0),(5,1)` vacant. The `g_down` target directly supplies the two `x=5` vacancies, but not the two `x=4` vacancies. In the local `g_down` descriptor those latter coordinates are `(-1,-1)` and `(0,-1)`.

This was the exact reason the first full guard-relation attempt produced an empty continuation signature: the stagewise local class had forgotten a genuine earlier corridor invariant.

## 6. The protected guard invariant

Let

\[
L_*:=\{(4,0),(4,1)\}.
\]

These two sites are first cleared by the horizontal `h4` target. They are also part of the final right-child protection buffer: `(4,1)` is the future child-CO site and `(4,0)` is its nearest neighbor. In the already-certified one-column geometry, every later horizontal protected set `h5,...,h8` contains `L_*`, and the `g_down` protected set contains the same child buffer.

Therefore, on the existing good Harris event,

\[
\boxed{(4,0),(4,1)\text{ remain vacant from }h4\text{ success through }g_\downarrow.}
\tag{6.1}
\]

No extra clock is suppressed and no new probability factor is introduced; (6.1) is information already guaranteed by the old protected event but discarded by the coarse entrance class.

This lets us replace the old `g_down` entrance class by the still-universal refined class

\[
E_\downarrow:\quad
(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1)\text{ vacant}.
\tag{6.2}
\]

Exact stable enumeration gives `|E_down|=2107` projected descriptors. The checker also verifies dynamically that the two extra coordinates `(-1,-1),(0,-1)` remain zero throughout the accepted `g_down` transition closure: accepted local adsorption roots cannot fill them, and every other interfering clock is already cemetery/failure in the same protected event.

At `g_down` success, its target supplies global columns `x=5,6` at rows `0,1`, while (6.1) supplies column `x=4`. Thus the actual `g_up` entrance has all six sites `{4,5,6} x {0,1}` vacant. In the `g_up` frame this is the refined class

\[
E_\uparrow:
(-1,0),(-1,1),(0,0),(0,1),(-1,2),(0,2)\text{ vacant},
\tag{6.3}
\]

with exact projected count `|E_up|=1743`.

The frame-overlap relations contain 10 coordinates for horizontal handoffs, 8 for `h8->g_down`, and 9 for `g_down->g_up`. The exact checker finds a compatible continuation for every target signature encountered.

## 7. B27 — universal quantifier in the correct order

The refinement does **not** replace the universal exterior by a favorable continuation. The order is: a protected random history produces a concrete target descriptor `s`; deterministic translation/rotation identifies the already observed overlap and the already-protected invariant sites; the exterior may choose **any** stable completion consistent with those facts; all later random histories are summed from that completion; and the Bellman value takes the minimum over those compatible completions.

Thus

\[
U_j(n,s)=\min_{t\in R_j(s)}U_{j+1}(n,t),
\tag{7.1}
\]

where `R_j(s)` contains every source-admissible stable continuation consistent with information physically fixed by the past event. Because `R_j(s)` is a subset of the old unrestricted entrance class, (7.1) can only raise the lower bound, but remains universal.

## 8. Exact fixed-top value

The refined backward chain uses the same eight stages and hazards `(150,167,178,187,197,201,218,222)`, common denominator `H=36*222=7992`, Poisson mean `lambda=429/20`, and deterministic time `T=143/370`. No physical Harris clock, spatial dependency set, or time horizon changes.

The exact descriptor checker has state-closure sizes:

- `g_up`: 1743 entrances, 26727 closure states;
- `g_down`: 2107 entrances, 31747 closure states;
- `h8`: 1743 entrances, 26299 closure states;
- `h3,...,h7`: 1743 entrances, 26771 closure states each.

The new exact common-tick fingerprints include

\[
m_0(18)=7010019266899452093151813293834240,
\]

\[
m_0(22)=149036073249956064814277118517341597733075449544704,
\]

\[
m_0(30)=8111684503865718191864242693800517125264745846773497015016916132473237059665920,
\]

and

\[
m_0(40)=8690529272431987101422310455185602929040312282298619013715273938401623782311851179648115578639167199903744.
\]

Using only the nonnegative terms `18<=n<=40` and exactly the same rational lower bound for `e^{-429/20}` as `b20_global`, the new rigorous corridor probability is

\[
\boxed{P_{\rm desc}=\frac{545463244285540695942015201925777994061697368171136921490714742697824329752268940195255955292431351662433721074404369251854402902909903343634639871925217501509}{582193154455203644179600026681016804451057807118892396907462406116250385773925198960673377107050434594335162049931454407958179823075232020480000000000000000000000000000000000000000000000000000000}.}
\tag{8.1}
\]

The archived arithmetic checker reconstructs the preceding exact `P_global` and proves

\[
\frac{P_{\rm desc}}{P_{\rm global}}
=
\frac{20250376323381968973878014720115467974667656528406168989928376556656242171778902900194077764678732746446886563465969472}{3035407598828408687586052566685944043089858522392691278993631382621774633640859988880503257952761490410138991736595541}
>\frac{20}{3}.
\tag{8.2}
\]

Numerically this ratio is `6.671386185894147...`, with `log10` gain `0.8242160813433799...`.

## 9. Frozen metric movement

Define

\[
\boxed{b_{21,\rm desc}:=b_{20,\rm global}\frac{P_{\rm desc}}{P_{\rm global}}.}
\]

Every upstream/downstream factor from the sound `b20_global` certificate is unchanged; only the source-valid lower bound on the same post-bootstrap corridor event is strengthened. Hence

\[
\boxed{B_{\rm cat}\ge b_{21,\rm desc}>\frac{20}{3}b_{20,\rm global}.}
\]

For diagnostic scale only,

\[
\boxed{\log_{10} b_{21,\rm desc}\approx-48.42893853604687.}
\]

This is genuine frozen-metric movement, so the supported unchanged count remains/reset at `0`.

The target is still **PARTIAL**, not solved. A block probability on the scale `10^-49` is still astronomically below the sufficient `63/64` threshold. This result is important because it identifies and removes an avoidable adversarial reset, not because the present rare-cylinder architecture is near closure.

## 10. What the three methods taught

**B18 SAY IT IN ANOTHER LANGUAGE — succeeded.** Stage handoff is better represented as a compatibility relation between local descriptors than as a scalar worst-case number. Carrying observed overlap alone already gives a `1.273...x` corridor improvement.

**B20 FIND WHY THE ALGORITHM FAILS — succeeded.** Naive relation gluing at the guard turn initially failed because the local stage class had discarded the long-lived child-buffer vacancies `(4,0),(4,1)`. Recovering that exact invariant strengthens the guard entrance classes without paying any new probability cost.

**B27 SWAP / AUDIT THE QUANTIFIERS — succeeded.** The universal exterior is minimized only after conditioning on deterministic overlap and previously protected sites. It may choose any compatible completion, but cannot rewrite information generated by the good event itself.

## 11. Exact artifacts and self-check status

Idea-before-code:
- `artifacts/R08/20260919T1327Z_e0011_descriptor_gluing_idea.md`

Horizontal descriptor diagnostic:
- `artifacts/R08/20260919T1327Z_e0011_horizontal_descriptor_glue_check.cpp`
- `artifacts/R08/20260919T1327Z_e0011_horizontal_descriptor_glue_check.out`
- `artifacts/R08/20260919T1327Z_e0011_horizontal_descriptor_glue_arithmetic.py`
- `artifacts/R08/20260919T1327Z_e0011_horizontal_descriptor_glue_arithmetic.out`

Stronger guard-refined computation:
- `artifacts/R08/20260919T1327Z_e0011_guard_refined_descriptor_check.cpp`
- `artifacts/R08/20260919T1327Z_e0011_guard_refined_descriptor_check.out`
- `artifacts/R08/20260919T1327Z_e0011_descriptor_chain_arithmetic.py`
- `artifacts/R08/20260919T1327Z_e0011_descriptor_chain_arithmetic.out`

Executed outputs report `PASS`. These are **self-checks only**; no independent OTHER-track audit credit is claimed.

## 12. Next research route

The factor `6.67x` confirms that preserving generated information matters, but it is still a constant gain inside an event whose total probability is microscopic. The next run should attack repetition/amplification rather than polish this finite corridor.

Next nonrepeating methods:
- **B9 RANDOMIZE:** search for many spatially separated or time-separated regeneration attempts inside one protected macroblock instead of demanding one prescribed rare corridor history.
- **B17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE:** compare the exact lower-transition/regeneration structure with restart/minorization constructions for contact processes, oriented percolation and imprecise Markov chains, looking for an amplification lemma that converts one modest local success probability into a high block probability.
- **B22 READ THE FAILURES, NOT THE SUCCESSES:** inspect the original catalyst/ZGB proof obstacles and later rigorous discussions for the precise reason zero-stirring block constructions fail, to avoid rebuilding another exponentially rare cylinder.

The intended measurable question is whether one can construct a protected family of repeated attempts whose failure probability decays geometrically while the spatial dependency footprint remains finite. That is capable of changing scale; another one-stage constant optimization is not.

## 13. Model / scheduler control truth

The exposed scheduler interface supplies task prompt/title, schedule or start offset, enabled state and timing mode. It exposes **no binding model-family selector, no reasoning-effort selector, no guaranteed-duration field, and no authenticated completed-run model/effort telemetry**. Therefore `GPT-6 / maximum` remains prompt text only. This run actually identifies as GPT-5.6 Sol with reasoning level UNVERIFIED and does not claim otherwise.

The historical P26 `You cannot modify this task` response is an authorization/context boundary, not something a repository edit can repair. The lawful workaround is the task's authorized owning context, a supported ownership/admin transfer, or platform support. No scheduler modification was attempted.

## 14. Structured ledger delta

```yaml
ledger_delta:
  worker: R08
  lane: CLOSABLE_OUTSIDE
  active_source:
    id: E0011
    source: "Rick Durrett, Coexistence in stochastic spatial models (2009), Problem 5"
    scope: "original two-dimensional no-stirring catalyst/ZGB process"
  stale_native_source:
    id: I0082
    status: "RETIRED/FROZEN"
    frozen_metric: "2/3"
    reopened: false
  metric: B_cat
  metric_before: "B_cat >= b20_global"
  metric_after: "B_cat >= b21_desc"
  exact_definition: "b21_desc = b20_global * P_desc/P_global"
  exact_ratio: "20250376323381968973878014720115467974667656528406168989928376556656242171778902900194077764678732746446886563465969472/3035407598828408687586052566685944043089858522392691278993631382621774633640859988880503257952761490410138991736595541"
  exact_comparison: "> 20/3"
  ratio_decimal_diagnostic: 6.671386185894147
  log10_before_diagnostic: -49.25315461739025
  log10_after_diagnostic: -48.42893853604687
  unchanged_before: 0
  unchanged_after: 0
  methods: [18, 20, 27]
  new_facts:
    - "ten persistent descriptor coordinates can be carried across each literal horizontal stage translation"
    - "protected child-buffer vacancies (4,0),(4,1) survive into and through g_down"
    - "refined g_down entrance has 2107 projected stable descriptors"
    - "refined g_up entrance has 1743 projected stable descriptors"
    - "frame overlap counts are 10 horizontal, 8 h8-to-down, 9 down-to-up"
    - "exact fixed-top corridor factor improves by >20/3 over b20_global corridor factor"
  status: PARTIAL
  source_closed: false
  checker_status: PASS_SELF_CHECK
  independent_audit_credit_this_run: 0
  shared_root_edit: false
  scheduler_changed: false
  next_methods: [9, 17, 22]
```
