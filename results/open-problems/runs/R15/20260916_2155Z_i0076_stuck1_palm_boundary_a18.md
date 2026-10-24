Model actually run: **GPT-5.6 Sol. Reasoning: UNVERIFIED** — GPT-6 / maximum was requested, but the exposed runtime/scheduler surface has no authenticated model-family selector and no reasoning-effort selector; I do not claim otherwise. **NO METRIC MOVEMENT: active positive-route gates `2/4 -> 2/4`; unchanged count `3 -> 4`; mandatory THINKING-ONLY STUCK RUN. Section-B moves tried: #1 CHANGE THE CATEGORY, #10 DERANDOMIZE, #25 COUNT THE SAME THING TWICE.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958, PTRF 160 (2014), Problem 7.2; intake I0076.

Status: **OPEN / PARTIAL / STUCK-RECOVERY-1.** No new theorem, lemma, finite certificate, or source-level closure is claimed in this report. The purpose of this run is to obey the three-unchanged-run protocol, identify the exact missing structure, and choose one genuinely different recovery route.

# 1. Continuity, source scope, exclusions, and current ownership

Before thinking about a new route I reread/rechecked current `master`:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, root `RESULTS.md`, and `QUEUE.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/new_methods_2026-09-16/DEPLOYMENT.md`;
- `operations/FLEET_2026-09-16.md`, `operations/RFLEET_2026-09-16.md`, and `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- newest own report `runs/R15/20260916_2056Z_i0076_two_ray_smoothing_a17.md` and the a11--a16 history;
- newest same-source neighbouring report `runs/R07/20260916T2124Z_i0077_positive_seam_gauges_05.md`, which owns distinct Problem 7.8 / I0077;
- newest visible R17 report `runs/R17/20260916_2114Z_lowerprecision_6b2e.md`;
- targeted repository/intake searches for I0076 / Problem 7.2 and nearby Burdzy--Scheutzow attempts.

The large `probability_1000_intake_*/problems.jsonl` family cannot be rendered exhaustively row-by-row through the connector without truncation. I therefore record the whole-intake reread as **PARTIAL / targeted due connector limits**, while the exact I0076 ownership, source statement, previous R15 attempts, Problem-7.5 exclusion, and neighboring I0077 ownership were directly rechecked. `QUEUE.md` continues to assign I0076 to R15. Problem 7.5 is settled/excluded; Problem 7.2 is not in `INDEX.md` or `POSTED.md` as settled or posted.

The primary arXiv PDF was rechecked directly this run. Definition 2.1 says:

- FBM: there exist random times `S_n -> -infinity` a.s. such that for every n, `(X_{S_n+t}-X_{S_n})_{t>=0}` is standard Brownian motion;
- BBM: `(X_{-t})_{t in R}` is FBM;
- 2BM: there exists a random time S such that the centered forward and centered backward halves at S are independent standard Brownian motions.

Problem 7.2 asks exactly: if X is FBM and BBM and there is a random real time T such that the **two entire centered half-processes**

`F_t = X_{T+t}-X_T`, `G_t = X_{T-t}-X_T`, `t>=0`,

are independent, must X be 2BM? There is no stopping-time hypothesis on T and no Brownian-marginal hypothesis at T.

Current-status searches dated 2026-09-16 UTC included:

- `"Forward Brownian Motion" "Problem 7.2" Burdzy Scheutzow`;
- `"Burdzy" Scheutzow "Problem 7.2" "Forward Brownian Motion"`;
- `"Forward Brownian Motion" independent past future random time Brownian`;
- later-author / citing-paper searches around Burdzy and Scheutzow;
- Thorisson continuous-time shift coupling;
- Last--Mörters--Thorisson unbiased Brownian shifts / Palm allocations;
- splitting-time / Palm / mass-stationarity searches.

The original publication page still lists the 2014 PTRF paper as the relevant completed publication. I found no accessible later paper explicitly claiming a resolution of exact Problem 7.2. This is **bounded negative evidence only**, not a proof of present-day openness and not a novelty certificate.

# 2. Metric continuity and current candidate state

The original frozen source-Theorem-6.1 counterexample candidate `X_BS` is permanently eliminated as a counterexample. Its terminal source-witness score is still `3/4`:

1. FBM — source-proved;
2. BBM — source-proved;
3. source independence at some random T — **disproved for this candidate** by R15;
4. failure of 2BM — source-proved.

After that elimination R15 made the one transparent positive-route metric switch permitted by the owner contract:

- P1 invariant-event / shift-coupling compiler — **PROVED**;
- P2 complete discrete FRW+BRW analogue — **PROVED**;
- P3 remove the genuinely continuous anticipative-phase obstruction under the exact source hypotheses — **OPEN**;
- P4 source conclusion + closure package / two independent audits — **OPEN**.

The active metric is therefore `2/4`.

The a16 alternating Brownian-prefix/BES dual family remains the current **counterexample test candidate**, without replacing the active positive metric. Its diagnostic score remains `3/4`: FBM, BBM and exact source independence at T=0 are proved; non-2BM is open.

The three preceding positive-route runs a15, a16, a17 all left the active metric at `2/4`. Therefore section I requires this run to be a thinking-only stuck report. I do not turn a new reformulation into metric movement.

# 3. Exact blocking statement

Let `mu = mu_- tensor mu_+` be the rooted law at the source-independent seam T. In a17, for a fixed `L>0`, an independent `U~Unif[0,L]` and the common physical root `T+U` give a rooted law `nu_L` such that

\[
\nu_L\big|_{\mathcal F_{[-L,\infty)}}\ll
P\big|_{\mathcal F_{[-L,\infty)}},
\qquad
\nu_L\big|_{\mathcal F_{(-\infty,L]}}\ll
P\big|_{\mathcal F_{(-\infty,L]}},
\tag{B1}
\]

where P is two-sided Wiener law.

P1 reduces the positive solution to equality on the continuous re-rooting invariant sigma-field `I`. The exact blocker is therefore

\[
\boxed{
\text{(B1) + original seam product structure + FBM + BBM}
\quad ?\Longrightarrow\quad
\nu_L|_{\mathcal I}=P|_{\mathcal I}.
}
\tag{BLOCK}
\]

Separate absolute continuity on the two complementary rays does not by itself imply absolute continuity, or invariant-field equality, on their join. A singular two-remote-tail joining can in principle be invisible to either ray marginal. The source independence is before the common re-rooting and does not automatically survive as a product decomposition at `T+U`.

# 4. Full failed-route inventory and the precise failure of each

This is the required stuck inventory rather than another incremental lemma.

## Route A — source Theorem-6.1 process as the counterexample

The source already supplied FBM, BBM and non-2BM. R15 first tried to add the missing source-independence witness. The natural central seam fails because the construction copies large discrete blocks across the seam. The list argument then ruled out every integer/skeleton seam. Finally the tail-lock argument ruled out **every real random seam** for this candidate.

Failure reason: the mechanism that makes this process non-2BM also creates long-range anti-independence, so the fourth needed counterexample obligation cannot be added.

## Route B — direct discrete positive proof

R15 proved the exact discrete analogue: FRW + BRW + independent halves at an arbitrary integer random seam implies 2RW. The key null-set argument succeeds because the witness-to-seam offset takes countably many integer values.

Failure reason in continuous time: `T-S_n` is a real, arbitrarily anticipative shift. A path-selected uncountable shift can concentrate a Wiener path on a Wiener-null set. The countable union argument has no continuous analogue without an additional domination/Palm structure.

## Route C — one-sided external phase randomization

The a15 uniform-phase argument adds an independent uniform phase and makes the shifted future law Wiener-absolutely-continuous; the analogous past statement also holds.

Failure reason: independently repairing the two halves produces an artificial glue, not one common physical re-rooting of the original process.

## Route D — alternating Brownian-prefix/BES dual candidate

The a16 construction cross-pairs reversible Brownian prefixes and Bessel terminal excursions. It satisfies FBM, BBM and exact independence at T=0. Paired blocks form an infinite-mean strongly decomposable renewal structure.

Failure reason: source Remark 7.6 would give non-2BM if the renewal boundaries were measurably shift-covariant / path-identifiable, but recurrent Brownian-looking paths contain many competing crossing chains. No intrinsic boundary recovery has been proved.

## Route E — enrich the discrete skeleton by whole Brownian exit cells

The full stopped exit-cell law is singular to the time-reversed/recentered cell law. The fair terminal sign is reversal-friendly, but the continuous orientation/last-zero phase is not.

Failure reason: attaching the full cell mark destroys the reversal symmetry that made P2 work. A sign-only discretization loses exactly the continuous phase one needs to control.

## Route F — two-ray same-root smoothing

The a17 theorem upgrades one-sided smoothing to complementary rays at the **same** common randomized root. This localizes any remaining defect to a singular relation between the two remote tails.

Failure reason: two overlapping marginal laws can both be absolutely continuous while the joint law is singular. PR2 does not control the joining of the remote tails or the invariant sigma-field.

## Route G — excursion-count labels as identifiable markers

Replacing elementary first-hit pieces by the r-th successful excursion looked like a way to encode boundaries.

Failure reason: by strong Markov the r-labelled piece is only a deterministic rebracketing of the same elementary alternating pieces. The label is gauge, not path geometry, and gives no intrinsic seam marker.

## Route H — ordinary independent-piece / inverse-local-time / marked-excursion pastings

Several simpler pastings were tested before a16. Reversible iid stopped Brownian pieces tend either to regenerate honest 2BM boundaries or to lose BBM under reversal. Inverse-local-time constructions naturally rebuild ordinary Brownian behavior; marked terminal excursions put the distinguished object on the wrong side under reversal.

Failure reason: ordinary independent-piece pasting is too Markovian. A genuine counterexample would have to encode anticipative dependence without destroying both FBM and BBM.

# 5. Move #1 — CHANGE THE CATEGORY: recast BLOCK as Palm / mass-stationarity

The nearest machinery does not treat Problem 7.2 as a Brownian-path identity; it treats re-rooting as a group action and random origins as Palm points.

Thorisson's continuous-time shift-coupling theorem links shift coupling to agreement on the re-rooting invariant sigma-field. Last--Mörters--Thorisson's unbiased-shift work starts from a stationary sigma-finite Brownian measure and invariant random measures, then uses allocation rules and Palm/cycle-stationarity to choose an unbiased root.

This recasting clarifies the missing object. To port that machinery without circularity, Problem 7.2 would need a **canonical shift-covariant random measure of candidate roots**, say `Xi_X(dt)`, extracted from the source process itself, with enough intensity/Palm structure that the law rooted at a typical Xi-point is related to the independent-seam law.

The source hypotheses do not presently supply such an object:

- FBM witness sequences are existential and noncanonical;
- different witness sequences can be arbitrarily sparse;
- the independent seam T is existential and need not be an intrinsic measurable function of the unrooted path;
- no finite positive intensity or stationary random measure is supplied.

Therefore the direct Palm port currently becomes circular: the allocation theorems assume a stationary ambient measure or invariant random measures whose Palm version can be identified, while stationarity/2BM is essentially what Problem 7.2 asks us to obtain.

**Outcome of move #1:** useful change of category, but no proof. It identifies the absence of a canonical mass-stationary root measure as the exact structural gap.

# 6. Move #10 — DERANDOMIZE: try to turn the external uniform phase into a physical path rule

A15/A17 use an external uniform U to wash out an anticipative phase. A tempting derandomization is to choose U from the path itself by a translation-equivariant allocation rule.

The unbiased-shift literature shows how such derandomization can work when one already has two invariant random measures of equal intensity to balance. Here there is no source-given invariant measure representing “admissible Problem-7.2 roots.” Picking U by an arbitrary path functional can reintroduce the very Wiener-null concentration that external uniformization removed.

The a16 test candidate exhibits the same obstruction concretely: its useful renewal boundaries would give a natural point measure **if** they were path-identifiable, but identifiability is exactly the open fourth-obligation problem.

**Outcome of move #10:** failed at the first required input. A path-measurable common phase is not just a deterministic replacement for U; constructing it without bias is equivalent to supplying the missing covariant Palm structure.

# 7. Move #25 — COUNT THE SAME THING TWICE: attempted Campbell / mass-transport balance

The natural double count is to send unit mass from every ordinary time/root to a Brownian witness origin, and then compare the mass seen from a typical root with the mass seen from a typical witness. Under a stationary point/random-measure model this is exactly where Campbell/Palm formulas become powerful.

For Problem 7.2 the count is not well-defined from the hypotheses. The FBM/BBM witnesses are only **there exists a sequence**. They need not form a measurable, translation-covariant locally finite set; they need not have positive finite density; and selecting one witness sequence may require extra randomness not intrinsic to the path. Therefore neither side of a Campbell identity has a source-defined intensity.

The independent seam T also does not repair this: one isolated random root does not produce a stationary point process of such roots.

**Outcome of move #25:** the failed double count pinpoints the same missing datum from another direction — a canonical invariant intensity measure of usable roots.

# 8. What a successful proof must contain that no current route contains

A positive proof needs one of the following genuinely new ingredients, neither of which is presently available:

1. **Canonical-root/Palm route.** Construct from every source-admissible X a measurable shift-covariant sigma-finite random measure `Xi_X` on time, with a usable finite positive intensity or mass-stationary analogue, and prove that the independent-seam rooted law is its Palm law (or at least agrees with two-sided Wiener law on invariant events). Then a Thorisson/Last--Mörters--Thorisson allocation could plausibly produce one physical re-rooting.

2. **Invariant-tail route.** Prove directly that every re-rooting-invariant event is already determined, modulo null sets, by one of the two PR2 rays in a way that FBM/BBM and the original seam product law force its Wiener 0/1 value. No such invariant-tail generation theorem is known in the current argument.

A negative solution would instead need an explicit process whose remote negative and positive tails carry a shift-invariant singular relation, while the unshifted halves at one finite T remain exactly independent and while both FBM and BBM witnesses still exist. No present pasting construction achieves all four simultaneously.

# 9. Simplest special case still unproved

The most useful narrow case for the chosen recovery is:

> Assume the exact hypotheses of Problem 7.2 and, in addition, that the independent seams form (or T is sampled from) a **measurable shift-covariant locally finite random measure/set `Xi` of finite positive intensity**, with the rooted law at a typical Xi-point equal to the Palm law of Xi. Must X be 2BM?

This is substantially stronger than the source hypothesis because Problem 7.2 gives only one existential seam. It is nevertheless the simplest unproved case in which the Palm/allocation machinery has its basic inputs. I do **not** claim this special case is solved here.

A second concrete special case, on the negative/counterexample side, remains the a16 alternating-dual candidate: prove or disprove path-identifiability of its paired infinite-mean renewal boundaries. That is also unproved, but it is not the recovery chosen for the next run.

# 10. Nearest solved problems and the ingredient they have that Problem 7.2 lacks

## Thorisson 1994 — continuous-time shift coupling

Thorisson proves the continuous-time analogue linking shift-coupling to time-average total variation and the invariant sigma-field. This is exactly the abstract compiler used in P1.

**What it has that BLOCK lacks:** a criterion phrased after invariant-field agreement is already available; Problem 7.2 still needs that agreement to be established from FBM+BBM+one independent seam.

## Last--Mörters--Thorisson 2014 — unbiased shifts of Brownian motion

They characterize unbiased Brownian shifts by allocation rules balancing invariant mixtures of Brownian local-time measures. Their framework uses a stationary sigma-finite Brownian measure and Palm/mass-stationarity of invariant random measures.

**What it has that BLOCK lacks:** canonical invariant random measures with a refined Campbell/Palm identity and controlled intensities. Problem 7.2 supplies no canonical invariant root measure.

## Pitman--Tang / related Brownian spacetime-shift embeddings

Nearby Brownian embedding work uses Palm/local structure and a specifically constructed shift to embed a target path fragment inside Brownian motion.

**What it has that BLOCK lacks:** a concrete stationary/Palm target event or random measure that tells the algorithm where admissible roots live.

The nearest-literature comparison therefore supports one precise diagnosis rather than a vague “Palm theory might help”: **the missing bridge is construction of a source-intrinsic covariant root measure, not another Brownian local estimate.**

# 11. Required recovery choice

Under the stuck protocol I choose exactly one recovery:

**PORT THE TECHNIQUE FROM THE NEAREST SOLVED PROBLEM.**

The next mathematical attack will port Thorisson / Last--Mörters--Thorisson Palm-allocation machinery to the simplest finite-intensity covariant-seam special case in Section 9. The first obligation will be to write the source-special-case law as a Palm law and determine whether a balancing allocation yields invariant-field equality without assuming stationarity of X in advance.

If that port is circular even in the finite-intensity special case, that failure will be documented explicitly rather than hidden behind another Brownian lemma.

The next Section-B methods, not used in this run, are planned as:

- #5 ADD A PARAMETER AND DIFFERENTIATE: introduce seam intensity / smoothing scale and inspect the zero-intensity or large-scale limit;
- #24 FIND THE EXTREMAL OBJECT: identify the most singular two-tail joining compatible with the PR2 ray constraints and seam product law;
- #29 ADD THE POINTS AT INFINITY: compactify the two remote tails so the residual joining becomes a boundary object on which invariant events can be studied.

# 12. R17 independent-audit trigger

The newest visible R17 report is `runs/R17/20260916_2114Z_lowerprecision_6b2e.md`. It explicitly says the exact binary Chvatal--Sankoff constant remains OPEN and its run is PARTIAL / NO METRIC MOVEMENT. It is not a closure package. Therefore the instruction for R15 to independently audit R17 is **not triggered**, and no audit verdict is invented.

# 13. Model / scheduler control status

The requested `GPT-6 / maximum` setting is still **not verifiable or settable through the exposed scheduler interface**. The repository's current deployment/follow-up records and the actual tool surface agree: the editable task fields are prompt/title, schedule or relative start, timing mode, and enabled state. There is no model-family field, no reasoning-effort field, no authenticated completed-run telemetry, and no guaranteed full-hour execution switch.

Therefore prompt text can request GPT-6 / maximum, but it cannot establish that runtime configuration. To make this verifiable would require a product/platform scheduler surface that persists model and reasoning fields **and** exposes authenticated run metadata confirming them, or an owning workspace UI/API with those controls. This worker cannot add such fields itself.

The historical P26 task-modification denial is also unchanged in scope: `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md` records an attempted refresh of the P26 native ID returning `You cannot modify this task`. Another authorized context later handled P/C updates, so the denial is a permission/ownership-context boundary rather than a mathematical blocker. The legitimate workaround is the owning authorized account/workspace/context or an owner/platform permission/support change. Creating a duplicate scheduler task is not an authorized bypass. No scheduler modification was attempted in this run.

# 14. Old R15 Cugliandolo--Kurchan handoff

The former R15 CK-aging assignment remains retired with its preserved OPEN handoff. This run neither revives nor edits that personal/research line.

# 15. Ledger delta

```yaml
ledger_delta:
  track: R15
  source: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion (2014), arXiv:1302.6958, Problem 7.2; intake I0076"
  target: "Decide whether FBM + BBM + source-exact independence of centered half-processes at an arbitrary random real T implies 2BM"
  original_counterexample_metric:
    name: "four source-witness obligations for frozen Theorem-6.1 candidate"
    terminal_value: "3/4; candidate eliminated because independence obligation is false"
  current_test_candidate:
    name: "a16 alternating Brownian-prefix/BES dual family"
    diagnostic_value: "3/4; non-2BM obligation open"
  active_metric:
    name: "positive-route gates P1/P2/P3/P4 proved"
    before: "2/4"
    after: "2/4"
    movement: "NO MOVEMENT"
  unchanged_count_before: 3
  unchanged_count_after: 4
  status: "OPEN / PARTIAL / STUCK-RECOVERY-1"
  tried_moves:
    - "1 CHANGE THE CATEGORY: Palm/mass-stationarity reformulation; failed because source hypotheses do not supply a canonical invariant root measure or intensity"
    - "10 DERANDOMIZE: tried to replace external uniform smoothing phase by a path-equivariant allocation; failed because the required balancing measure is exactly the missing Palm structure"
    - "25 COUNT THE SAME THING TWICE: Campbell/mass-transport count of witness roots versus ordinary roots; failed because FBM/BBM witness sequences are existential/noncanonical and have no source-defined intensity"
  blocking_formula: "(two complementary PR2 ray ACs + original seam product structure + FBM + BBM) ?=> equality with 2BM on the re-rooting invariant sigma-field"
  missing_ingredient: "source-intrinsic shift-covariant root random measure / Palm law, or a direct invariant-tail generation theorem"
  simplest_unproved_case: "Problem 7.2 plus a finite-positive-intensity shift-covariant seam random measure whose typical-seam law is its Palm law"
  recovery_choice: "PORT TECHNIQUE: Thorisson continuous-time shift coupling + Last-Morters-Thorisson allocation/Palm machinery on the finite-intensity covariant-seam special case"
  evidence:
    - "runs/R15/20260916_2056Z_i0076_two_ray_smoothing_a17.md"
    - "runs/R15/20260916_1952Z_i0076_alternating_dual_candidate_a16.md"
    - "runs/R15/20260916_1653Z_i0076_shiftcoupling_discrete_a14.md"
    - "primary arXiv:1302.6958 Definition 2.1 and Problem 7.2 rechecked 2026-09-16 UTC"
    - "Thorisson, PTRF 99 (1994), 477-483, DOI 10.1007/BF01206228"
    - "Last-Morters-Thorisson, Ann. Probab. 42 (2014), 431-463, DOI 10.1214/13-AOP832"
  audits:
    - "retained scoped R14 audit of the old candidate-elimination theorem: R14-AUDIT-R15-I0076-T1-03 = PASS; not a source-closure audit"
    - "P26 source-closure audit: not requested/not available because no closure package exists"
    - "R17 audit duty: not triggered; newest R17 package remains OPEN/PARTIAL"
  finite_checker_this_run: "none; mandatory thinking-only stuck run contains no new finite claim"
  next_methods: [5, 24, 29]
```

No checker was manufactured for an unchanged metric and no numerical path simulation was used as verification of Brownian laws. No shared root, peer file, Gmail, email, Drive, public posting, purchase, permission, or scheduler change was made.
