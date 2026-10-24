Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `B_cat >= b6 -> B_cat >= b7`, exact `b7>b6`; diagnostic `log10(b7/b6)=21.33640381824432`. Unchanged count remains `0`. Methods actually used: B2, B17, B22.**

# R08 CLOSABLE OUTSIDE — E0011 catalyst coexistence: local Harris interference cone

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Controlling state and continuity

I did **not** reopen Hasebe--Ueda Problem 3.11 (`I0082`). Its controlling handoff keeps the explicit-candidate metric frozen at `2/3` after six unchanged runs; it remains RETIRED/FROZEN. The active exclusive R08 claim is `E0011`, Rick Durrett, *Coexistence in stochastic spatial models* (2009), Problem 5: prove coexistence for the original two-dimensional catalyst/ZGB process without added stirring.

Before research I refreshed the required repository state: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/claims/I0082.md`, `operations/claims/E0011.md`, the newest R08 report, current neighboring R07/R09 reports, and the E-intake record containing E0011. No source-resolution or ownership conflict was found. `RESULTS.md` remains a compact historical registry whose old R08 row is explicitly not a replacement for newer immutable current-target reports.

The bounded current-literature check was also refreshed on 2026-09-18. Durrett's 2009 source remains the controlling statement (arXiv:0906.2293; DOI 10.1214/08-AAP590). Durrett--Swindle (1994), DOI 10.1007/BF01192836, gives a rigorous catalyst coexistence route after adding fast stirring; Bramson--Neuhauser treat a large-polymer modification rather than the original O2 pair rule. Durrett's currently served *Probability: Theory and Examples / particle-system* notes still describe the ZGB simulation window and develop catalytic surfaces inside the fast-stirring chapter. A bounded search for the exact original no-stirring Problem 5 found no later source-matching theorem. This is **bounded negative evidence only**, not an exhaustive priority claim.

## 2. Frozen metric before this run

At the source-valid rational anchor

\[
p=\frac12,\qquad q=1,
\]

CO site clocks have rate `1/2` and O2 nearest-neighbor edge clocks have rate `1/4`. The frozen metric is

\[
B_{\rm cat}:=\sup_C b(C),
\]

where `C` ranges over explicit finite 1-dependent two-child Harris-block certificates and `b(C)` is a rigorous lower bound for the block success probability.

The previous report proved an explicit certificate

\[
B_{\rm cat}\ge b_6,
\]

with diagnostic

\[
\log_{10} b_6\approx -152.30387672112045.
\]

The deterministic macro was already valid; the dominant loss was that each micro-window silenced **every** protected clock in the old `18 x 8` block even though most such clocks could not influence the particular local stage.

## 3. Idea before code

The new route was written down before constructing a checker:

> During one local stage, protect only the state cells that the accepted labels can read now, plus vacancy cells that must survive for a later stage. Silence exactly the adsorption clocks that can directly write those cells. Let every other clock in the old block run freely.

If this locality statement is valid, the old global protected-arrival rate `301/2` is artificial. The stage rate should instead be the intensity of a much smaller **interference cone**.

## 4. B2 — attack the negation: whole-block silence is unnecessary

For a CO adsorption clock at site `x`, define its possible one-event write support by

\[
W_{CO}(x)=\{x\}\cup N(x).
\]

For an O2 clock on the edge `e={x,y}`, define

\[
W_{O_2}(e)=\{x,y\}\cup N(x)\cup N(y).
\]

These supports include the newly occupied endpoint(s) and every site that can be erased by the instantaneous `r=infinity` nearest-neighbor reaction triggered by that adsorption.

For a finite set of state cells `S`, define

\[
I(S)=\{\text{adsorption clocks }a: W(a)\cap S\ne\varnothing\}.
\]

### Local projection lemma

Fix a time interval and a deterministic accepted-label language whose labels have full read/write supports contained in `S`. Suppose that, in the interval, every clock in `I(S)` that rings belongs to the accepted language, with the specified reaction tie-breaking branch when relevant. Then the process restricted to `S` evolves exactly according to that accepted label sequence, **independently of all adsorption activity outside `I(S)`**.

### Proof

A clock outside `I(S)` has write support disjoint from `S`, so one occurrence cannot change any state cell in `S`. In the `r=infinity` model the only instantaneous reaction following an adsorption is between a newly landed particle and one of its nearest neighbors; by construction all sites that can be changed by that reaction are already in `W(a)`. There is no secondary reaction cascade after the two reacting particles are removed. Hence outside clocks cannot alter `S`. Since every accepted label's complete nearest-neighbor read support is contained in `S`, its transition law depends only on the current restriction to `S`. Induction over the ordered accepted labels proves the claim. QED.

This directly negates the previous proof-device assumption that the whole `18 x 8` protected block must be silent during every local stage. A clock on the direct boundary of `S` can genuinely matter (for example a CO clock that lands on a protected vacancy), while a clock outside `I(S)` provably cannot matter in that interval.

## 5. Source-valid localized two-child macro

Keep the already certified deterministic two-child geometry. The left child box is

\[
Q_0=\{0,1,2,3\}\times\{0,1,2,3\},
\]

and the right child box is

\[
Q_1=\{10,11,12,13\}\times\{0,1,2,3\}.
\]

After the canonical eraser makes `Q0` vacant, columns `c=4,...,13` are grown one at a time, top row-pair then bottom row-pair, using the seven-label all-history vacancy expander from the preceding reports. During a stage I protect:

1. `Q0`, because it must stay vacant until the left child is replanted;
2. the 14-cell full read support of the current expander;
3. the other row-pair's current `2 x 2` vacancy cursor;
4. any already-cleared cells of `Q1` that must survive until the right child is replanted.

Previously cleared corridor cells not needed again are deliberately **not** protected.

For a state set `S`, write

\[
D(S)=2N_{CO}(S)+N_{O_2}(S),
\]

where `N_CO` and `N_O2` are the numbers of CO-site and O2-edge clocks in `I(S)`. At `p=1/2`, the total interference rate is exactly `D(S)/4`.

The eraser requires only `I(Q0)`:

\[
(D,N_{CO},N_{O_2})=(140,32,76),
\]

so its interference rate is `35`, rather than `301/2`.

For the twenty expander windows the exact `D` sequence is

\[
\boxed{175,179,200,204,225,226,247,247,265,262,276,272,278,274,278,274,278,282,290,294.}
\]

The corresponding `(N_CO,N_O2)` sequence is archived in the exact output. For the two final planter windows I protect `Q0 union Q1`, giving

\[
(D,N_{CO},N_{O_2})=(280,64,152),
\]

so the rate is `70`.

Every one of these interference clock sets is an exact subset of the old protected Harris block's clock set. Therefore translated blocks at spatial distance two remain measurable with respect to disjoint clock families; the old 1-dependence argument is preserved. No stirring, long-range landing rule, friendly exterior boundary, or changed source dynamics is introduced.

The parking invariant also survives: every accepted expander adsorption root is inside its current `2 x 3` active rectangle. Thus a vacancy parked outside that active rectangle but inside the stage's protected state set cannot be newly occupied by an accepted label. The current target rectangle ends vacant, and the next stage starts with its required `2 x 2` vacancy cursor.

## 6. Exact all-history local stage probabilities

The expander uses the same exact 12,201-state projected chain obtained from all 50,785 stable full boundary configurations. Let `A_n(eta)` denote the exact integer weight of all accepted seven-label histories of length `n` that finish in the target vacancy state, using common reaction denominator `36` per arrival. If the interference unit is `D`, then an accepted CO label has one-arrival weight `2/D` and an accepted O2 label has weight `1/D` before reaction branching.

For a Poisson mean `lambda` and truncation `N=8`, the rigorous rational lower bound is

\[
c_D(\lambda)=\left(\frac{32}{87}\right)^\lambda
\min_\eta\sum_{n=0}^{8}
\frac{\lambda^n}{n!}\frac{A_n(\eta)}{(36D)^n},
\]

using the previously proved rational inequality `e^{-1}>32/87`. Exact scanning of integer `lambda=1,...,8` gives `lambda=2` for **all twenty** localized expander stages. Write `c(D):=c_D(2)`.

The checker computes every `c(D)` exactly. Examples are

\[
c(175)=\frac{697697459322978525184}{56626173161368560791015625},
\]

\[
c(247)=\frac{1088819678938942300160}{178368616978167167484259509},
\]

and

\[
c(294)=\frac{60169743848737319392}{14036263132424279379709545}.
\]

All sixteen distinct exact fractions used by the twenty stages are printed in the archived checker output.

The localized eraser factor is

\[
E_{loc}=\left(\frac{32}{87}\right)^6\frac{6^6}{6!}
\left(4\frac{35}{486}\right)
\left(\frac{2}{140}\right)^4\left(\frac1{140}\right)^2
=\frac{33554432}{341622916891793578125},
\]

and each localized planter factor is

\[
P_{loc}=\left(\frac{32}{87}\right)^3\frac{3^3}{3!}
4\left(\frac{2}{280}\right)^2\left(\frac1{280}\right)
=\frac{512}{3137035125}.
\]

Because the windows are disjoint deterministic time intervals and every stage lower bound is uniform over its allowed stable incoming boundary state, conditional probabilities multiply. Therefore the same deterministic two-child implication has the exact certified lower bound

\[
\boxed{
 b_7=E_{loc}\left(\prod_{j=1}^{20}c(D_j)\right)P_{loc}^2.
}
\]

The exact checker reconstructs the previous `b6`, computes this rational `b7`, and verifies

\[
\boxed{b_7>b_6}
\]

by integer arithmetic. Diagnostic logarithms are

\[
\log_{10}b_6\approx-152.30387672112045,
\]

\[
\boxed{\log_{10}b_7\approx-130.96747290287607},
\]

and hence

\[
\boxed{\log_{10}(b_7/b_6)\approx21.33640381824432}.
\]

Thus this is genuine movement of the frozen metric:

\[
\boxed{B_{cat}\ge b_7>b_6.}
\]

The complete localized deterministic horizon is finite and exact:

\[
T_7=\frac{7059902017557060049739597}{7762331170048708744504650}
\approx0.9095079639.
\]

The fact that this horizon is longer than the previous globally synchronized horizon is harmless; the probability improves because irrelevant clocks are no longer required to remain silent.

## 7. B17 — the numbers identify a dependency-cone mechanism

The useful numbers are not mysterious constants; they are the local graphical hazards

\[
D=2N_{CO}+N_{O_2}.
\]

The old stage used the global value `D=602`. The localized stages use `D` between `175` and `294`, with eraser `140` and planters `280`. This has exactly the shape of Harris graphical dependency-cone bookkeeping: determine which Poisson marks can influence the observable before paying their total rate.

This is the transferable mechanism from elsewhere in interacting-particle proofs. The improvement does **not** come from a new physical parameter or a favorable boundary condition; it comes from recognizing that finite-block dependence should be measured by causal write support, not by the enclosing rectangle's area.

## 8. B22 — read the failures: what the solved perturbations have that the source lacks

The literature comparison sharpens the obstruction.

- Durrett--Swindle's catalyst coexistence theorem adds fast stirring. Durrett's current notes explain why fast stirring suppresses correlations and produces a reaction--diffusion PDE; block construction is then driven by the PDE behavior. That smoothing mechanism is absent at zero stirring.
- The large-polymer route changes the O2 landing geometry and gains a large spatial scale. That scale is absent in the source pair-adsorption model.
- The original no-stirring `N=1` process has neither mechanism. The present run therefore keeps microscopic correlations exact and only removes clocks that are causally irrelevant to the local event.

This is progress, but it also shows why the current certificate remains weak: after all these corrections, `b7` is still of order `10^-131`, nowhere near the sufficient block threshold `63/64`. The remaining gap is not bookkeeping noise. A closure route needs a **high-probability regeneration event**, not merely a rarer exact trajectory family with better accounting.

## 9. Status and next research route

Status remains **PARTIAL / OPEN_CURRENT_BOUNDED**. No coexistence theorem is claimed. There are no closure audits because closure has not been reached.

With B2/B17/B22, the E0011 track has now used all thirty Section-B moves at least once. The next run may therefore restart the catalog but must not repeat the immediately preceding triple. The strongest restart is:

- **B3 PROVE SOMETHING STRONGER:** replace exact `4 x 4` empty-box regeneration by a seed class that is closed under typical local dynamics and has a chance of high probability;
- **B15 BREAK THE SYMMETRY:** search directional/interface seeds rather than requiring two symmetric fully vacant child boxes;
- **B24 FIND THE EXTREMAL OBJECT:** optimize the seed/protected-set pair against the worst stable boundary state, with the objective being the actual block probability rather than word count.

The main target is to change the event itself. Further constant-factor shrinking of the current cone will not bridge ~130 decimal orders.

## 10. Exact artifacts

Self-check (finite exact claim):

- `artifacts/R08/20260918T1953Z_e0011_interference_cone_check.py`
- `artifacts/R08/20260918T1953Z_e0011_interference_cone_check.out`

The checker independently:

1. enumerates all `50,785` stable full expander boundary states and confirms `12,201` projected descriptors;
2. constructs every localized interference set and verifies the exact `D` sequence;
3. verifies every local clock set lies inside the old block's protected clock family;
4. computes every `c(D)` with exact rational arithmetic and confirms the argmax `lambda=2` over `1,...,8`;
5. reconstructs `b6`, constructs `b7`, and proves `b7>b6` exactly;
6. verifies the exact `T7` above.

This is a self-check, not an independent audit.

## 11. Model / scheduler / denied-task status

The current exposed automation-management surface still supplies title, prompt, schedule/timing, enabled state, notification/email state, default timezone and run timestamps, but **no binding model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. Therefore GPT-6 / maximum remains prompt-only here; this run cannot certify or enforce it. A real fix requires a platform/native scheduler control that exposes and persists model and reasoning fields (or an authorized owner surface that actually exposes those fields), not another prompt sentence.

The historical P26 `You cannot modify this task` failure is authorization-context specific: the current root ledger records that the full P26 update later succeeded from an authorized P/C context. For any task still denied, the supported workaround is its authorized owning context, an owner/admin transfer supported by the product, or platform support. I made no scheduler changes.

## 12. Structured ledger delta

```yaml
ledger_delta:
  track: R08
  source: "E0011 — Durrett (2009), Problem 5, original no-stirring catalyst/ZGB coexistence"
  metric_name: B_cat
  before: ">= b6"
  after: ">= b7"
  exact_movement: "b7 > b6"
  diagnostic_log10_before: -152.30387672112045
  diagnostic_log10_after: -130.96747290287607
  diagnostic_log10_gain: 21.33640381824432
  status: PARTIAL
  unchanged_count_before: 0
  unchanged_count_after: 0
  methods_used: [2, 17, 22]
  remaining_obligation: "Produce a source-valid finite 1-dependent two-child block event with success probability > 63/64 (or replace that sufficient comparison by another rigorous source-closing argument)."
  next_methods: [3, 15, 24]
  artifacts:
    - artifacts/R08/20260918T1953Z_e0011_interference_cone_check.py
    - artifacts/R08/20260918T1953Z_e0011_interference_cone_check.out
  closure_audits: []
```
