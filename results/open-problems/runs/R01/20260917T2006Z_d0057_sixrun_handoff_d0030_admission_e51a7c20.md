Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but the exposed runtime/scheduler still provides no authenticated model-family or reasoning-effort selector, so I do not claim GPT-6/maximum. **NO FIXED-METRIC MOVEMENT: `E_geom = 1 -> 1`; D0057 unchanged count `5 -> 6`; `SIX-RUN HANDOFF / ROTATED`; methods #9 RANDOMIZE, #16 COMPUTE SMALL CASES, #25 COUNT THE SAME THING TWICE. Successor D0030 was source/literature/ownership screened and claimed create-only; its new metric starts at `E_phi_rho=0`.**

# R01 — D0057 six-run handoff; successor admission to Bradley Question 2 (D0030)

Run date: 2026-09-17 UTC. Repository / branch: private `yspennstate/math-open-problems` / `master`. Delivery: private GitHub only.

## 0. Continuity, exclusions, whole-repository refresh, and runtime controls

I continued from the newest complete R01 report

`runs/R01/20260917T1857Z_d0057_dissipation_extremals_7c3e91a4.md`

rather than restarting the stale native title.

The required shared entry points were reread before research: `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, and `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`; I also recovered the active D0057 claim, the D-intake rows/attempts relevant to D0057 and the successor screen, and the newest neighboring R02 report.

Continuity/exclusions:

- `I0024` / Aldous–Fill Open Problem 3.44 remains frozen at the previously established exact distortion `C=1`; its formulas, discarded candidate counterexamples, and audit history were not reopened.
- `I0113` remains rotated.
- `G0012` remains rotated after its six-run handoff.
- The old R01 FEI assignment remains retired; P03 owns FEI.
- D0057 is the active predecessor being handed off in this report; its literal source statement is already REFUTED at owner-proof level but has `0/2` independent source-level audits.
- The newest neighboring R02 package is Bradley D0031 and is explicitly `OPEN / PARTIAL` with metric `UNKNOWN -> UNKNOWN`, so it is not a complete neighboring closure package and no audit budget was spent.

The model-control situation is still unchanged. The available task-management surface exposes title/prompt/schedule/timing/enabled controls but no model selector, no reasoning selector, no authenticated completed-run model telemetry, and no guaranteed one-hour execution control. Enforcing GPT-6/maximum would require a product/backend surface that exposes those fields or an authorized platform/support migration. The old P26 `You cannot modify this task` response was authorization-context-specific; the current repository ledger records that a later authorized context succeeded. The legitimate workaround is the owning/authorized context, not duplication or permission bypass. No scheduler change was attempted in this run.

## 1. D0057 literal source and why the fixed metric does not move

Source: Xinxing Chen, Bernard Derrida, Yueyun Hu, Mikhail Lifshits and Zhan Shi, *A max-type recursive model: some properties and open questions*, arXiv:1705.04787 / Springer Proc. Math. Stat. 300 (2019), Conjecture 2.

For fixed integer `m>=2`,

\[
X_{n+1}=\bigl(X_n^{(1)}+\cdots+X_n^{(m)}-1\bigr)_+,
\]

under the printed critical condition

\[
(m-1)\mathbf E[X_0m^{X_0}]=\mathbf E[m^{X_0}]<\infty,
\]

the source conjectures

\[
\mathbf P(X_n=k\mid X_n>0)\to\frac{m-1}{m^k},\qquad k\ge1.
\]

The primary source was rechecked on 2026-09-17. Its current arXiv HTML still states Conjecture 2 exactly in this form and explicitly warns immediately after Conjecture 4 that stronger integrability such as `E[X_0^3 m^{X_0}]<infinity` may be necessary for the conjectures.

The frozen metric is

`E_geom in {0,1}`.

It moved `0 -> 1` in `runs/R01/20260917T1358Z_d0057_lacunary_refutation_4c8e21ab.md`, which constructs a critical source-valid lacunary law for which the conditional laws are not tight. Later R01 runs strengthened and diagnosed that mechanism, but they do not move the literal decision bit beyond `1`. Protocol closure is still unavailable because the source-level refutation has not received two independent OTHER-track audits.

Fresh bounded searches dated 2026-09-17 for the deterministic-`m` conditional law, the exact conjecture, later author work, and recent Derrida–Retaux asymptotics again found no source-matching theorem reversing or superseding this status. Li–Zhang, arXiv:2411.13068 / J. Stat. Phys. 2025, studies a generalized model with **geometric offspring**, not deterministic offspring `m`; Chen–Hu–Shi's sustainability theorem gives the critical survival scale `n^{-2+o(1)}` rather than this exact conditional limit. Negative search is not a novelty certificate.

## 2. Mandatory method #9 — RANDOMIZE: the pivotal-spine route identifies the missing denominator

The most natural way to try to upgrade the exact dissipation identities from the preceding run is to randomize a witness of survival.

For a depth-`n` recursion tree, the root is a monotone function of the `m^n` leaves. On the event `X_n>0`, one may try to select a surviving/pivotal leaf or open root-to-leaf path by a size-biased rule, then expose the environment along that spine. This is directly suggested by the pivotal-vertex/open-path machinery in the critical sustainability work.

The hoped-for implication was:

\[
\text{controlled spine law}
\quad\Longrightarrow\quad
q_{n+1}/q_n=1+o(1),
\]

which would convert the exact conditioned-law shift relation from earlier R01 work into the geometric Yaglom limit under the finite-third-weighted-moment repair.

The route does **not** presently close. The normalization is the random number of eligible witnesses. A survival configuration may have essentially one pivotal continuation or very many, and size-biasing by the witness count changes the environment by a Radon–Nikodym factor for which the current moment identities give no uniform lower/upper control after conditioning on survival. The earlier lacunary construction is an extreme one-witness regime, whereas high-branching configurations can have large multiplicity.

So the new route reduces the missing theorem to a sharper statement:

> prove an anti-clustering/second-moment estimate for pivotal or open-path multiplicity that is uniform on the survival event and survives division by `q_n`.

Without such an estimate, the spine measure can be regular even while the unweighted survival law has sparse local dips. No theorem-sized new claim is made from B9 in this run.

## 3. Mandatory method #16 — exact small case kills the naive monotone-ratio route

The simplest repaired finite-support critical laboratory remains

\[
m=2,\qquad \mathbf P(X_0=0)=\frac45,
\qquad \mathbf P(X_0=2)=\frac15.
\]

It is exactly critical because

\[
\mathbf E[X_0\,2^{X_0}]=\frac85=\mathbf E[2^{X_0}].
\]

I used exact rational arithmetic only to test the concrete candidate that the survival ratios

\[
r_n:=q_{n+1}/q_n,\qquad q_n:=\mathbf P(X_n>0),
\]

might already be monotone or stay on one side of `1` in the easiest finite-support example.

The exact probe gives

\[
q_0=\frac15,\qquad q_1=\frac9{25},\qquad q_2=\frac{113}{625},
\]

and therefore

\[
\frac{q_1}{q_0}=\frac95>1,
\qquad
\frac{q_2}{q_1}=\frac{113}{225}<1.
\]

Thus even this elementary critical law immediately crosses `1`; a proof of `q_{n+1}/q_n\to1` cannot come from a simple global monotonicity or one-sided trapping of the raw ratio.

Exact checker and archived output:

- `artifacts/R01/20260917_d0057_twopoint_probe.py` @ `4c231c639bd1e16b5dccb40372e85196568a4086`;
- `artifacts/R01/20260917_d0057_twopoint_probe.out` @ `a8a8c51dde3a9364f08efc1be34c79946d3be4e2`, ending in `PASS`.

This is a route-killing finite check, not metric movement.

## 4. Mandatory method #25 — COUNT THE SAME THING TWICE: first moments are not enough

The preceding run's exact identity

\[
\sigma_n
=
\epsilon_n-\epsilon_{n+1}+h_m(\epsilon_n),
\qquad
\epsilon_n=\mathbf E[m^{X_n}]-1,
\]

with `sigma_n` comparable to `q_n`, suggests counting the same survival mechanism in two ways: once through the generating-function dissipation, and once through pivotal/open-path witnesses in the tree.

At a schematic level let `W_n` count admissible open/pivotal root-to-leaf witnesses. The source/critical identities and pivotal technology naturally control weighted first moments of witness counts. But

\[
q_n=\mathbf P(W_n\ge1)
\]

is not determined by `E W_n`. To turn the first count into a pointwise survival estimate one needs either bounded multiplicity or a second-moment/Paley–Zygmund estimate uniform in `n`.

That is precisely what is missing: witness multiplicity can vary by orders of magnitude, and the static extremal examples from the preceding run already show that one-time critical moment information can coexist with wildly different survival probabilities. Therefore the double count does not fail because the two sides are hard to write; it fails because there is no uniform inverse-multiplicity estimate linking them.

The useful handoff statement is:

\[
\boxed{
\text{The repaired problem needs dynamic control of witness multiplicity, not another one-time moment identity.}
}
\]

A credible next proof would need a spine/pivotal second-moment theorem or an equivalent dynamic anti-dip estimate across consecutive iterates.

## 5. Six-run handoff — exact blocker, tried routes, missing ingredient, easiest open case, nearest solved work

This is the sixth consecutive complete D0057 run with the literal metric already at `1` and no audit closure, so the CLOSABLE rotation rule now applies. R01 must not spend a seventh research run widening the same package.

### (a) Exact mathematical blocker left behind

The natural repaired question, which is **not substituted for the already-refuted source conjecture**, is

\[
\boxed{
\begin{gathered}
(m-1)\mathbf E[X_0m^{X_0}]=\mathbf E[m^{X_0}]<\infty,\\
\mathbf E[X_0^3m^{X_0}]<\infty
\end{gathered}
\quad\Longrightarrow\quad
\mathcal L(X_n\mid X_n>0)
\Longrightarrow
\left\{\frac{m-1}{m^k}\right\}_{k\ge1}.}
\]

A sufficient local regularity milestone is

\[
\boxed{q_{n+1}/q_n\to1.}
\]

Together with the exact conditioned-law shift identity derived earlier, this selects the geometric fixed point.

### (b) Routes tried and why each stopped

1. **Lacunary remote atoms / attack the printed conjecture.** Successful against the source's minimal hypotheses: it yields conditional non-tightness and refutes the literal Conjecture 2. It necessarily leaves the finite-third-weighted-moment regime when pushed to the required `n^{-2}` bursts, so it does not answer the repaired problem.
2. **CEGM 1984 formal critical profile.** The formal profile contains the right `m=2` constant and Yaglom law, but their derivation assumes smoothness in the iteration index; that is essentially the missing local regularity rather than a proof of it.
3. **Conditioned-law shift/operator formulation.** Exact and useful, but its error contains division by `q_{n+1}`; an unconditioned `O(q_n^2)` error is not enough without an anti-dip lower bound.
4. **One-time moment inequalities / static extremizers.** Explicit critical finite-support families show that the same `epsilon` and third-derivative scales can have radically different `q`; static moment geometry cannot force `q\asymp epsilon^2`.
5. **Exact dissipation/monovariant.** Gives `sum_{n>=N}q_n\asymp1/N`, dyadic density control, and sparsity of macroscopic `epsilon` shocks, but still allows oscillation at the exact `1/n^2` scale where the survival constant lives.
6. **Pivotal spine / double count (this run).** Identifies witness multiplicity as the dynamic obstruction; no uniform second-moment or inverse-multiplicity estimate is yet available.
7. **Raw ratio monotonicity (this run).** Exact finite arithmetic already disproves the simplest monotone/one-sided-ratio hope in the two-point critical example.

### (c) What a successful proof must contain that the tried routes do not

At least one genuinely inter-time estimate preventing dissipation/survival mass from concentrating at sparse times. Equivalent useful forms would be:

- a uniform lower bound on `q_{n+1}` in terms of neighboring averaged survival mass;
- bounded variation / Tauberian regularity of the exact dissipation tail `Sigma_n` at the `1/n^2` scale;
- a pivotal-spine second-moment theorem controlling witness multiplicity conditional on survival; or
- a coupling/contraction for conditioned laws whose constants remain uniform after the division by `q_n`.

### (d) Simplest special case still unproved

\[
m=2,\qquad \mathbf P(X_0=0)=4/5,\qquad \mathbf P(X_0=2)=1/5.
\]

This law is finite support, exactly critical, has every weighted moment finite, and already exhibits nontrivial early ratio oscillation. A rigorous proof of the geometric conditional limit for this one law would be a meaningful repaired-case theorem.

### (e) Nearest solved/partial literature and what it has that is insufficient

- Chen–Hu–Shi, *The sustainability probability for the critical Derrida–Retaux model*, proves the weaker `q_n=n^{-2+o(1)}` scale using pivotal vertices/open paths and coupling. It lacks the exact local constant/ratio regularity needed here.
- Collet–Eckmann–Glaser–Martin's older formal iteration gives the right critical profile for `m=2` after assuming iteration smoothness; it therefore identifies the desired profile but not the missing discrete regularity theorem.
- Li–Zhang 2025 obtains detailed asymptotics in a generalized **geometric-offspring** recursion; it does not preserve the deterministic-`m` source model.

### Protocol status at handoff

Literal D0057: **REFUTED at owner-proof level / NOT CLOSED / 0 of 2 independent source-level audits**.

The source refutation, strengthened consequences, repaired-problem diagnostics, exact probe, and prior-art notes are preserved in immutable R01 history. A future auditor should audit the **literal lacunary source counterexample first**, not the stronger repaired conjecture and not the later exploratory lemmas.

## 6. Successor admission: D0030 / Bradley Question 2

The root `QUEUE.md` currently has no freshly certified READY row that could simply be taken; I therefore did **not** auto-promote a PENDING queue entry. Instead I screened the admitted intake target D0030 end-to-end before making a create-only claim, following the same source/current-status/ownership discipline used by other recent R-series rotations.

### Exact source

Richard C. Bradley, *Basic Properties of Strong Mixing Conditions. A Survey and Some Open Questions*, Probability Surveys **2** (2005), 107–144, arXiv:math/0511078, Question 2, Section 2.3, journal p. 114 / PDF p. 8:

\[
\boxed{\text{If a strictly stationary sequence is }\phi\text{-mixing, must it be }\rho^*\text{-mixing?}}
\]

The primary PDF page was reread on 2026-09-17. Bradley explicitly records his own affirmative conjecture and Walter Philipp's negative expectation.

### Current literature / later-work screen

Bounded dated searches on 2026-09-17 for the exact question, `phi-mixing rho*-mixing`, `phi-mixing implies rho-star mixing`, and later work on interlaced maximal correlation returned Bradley's survey and later papers using the individual mixing coefficients, but no source-matching proof or counterexample. This is negative search evidence only, not a novelty certificate.

The nearby active `D0033` target is the strictly narrower **Markov-chain** special case and is owned by R7-01. R02 owns the different D0031 bilateral-determinism question. D0035, exact prescription of phi coefficients, is already internally refuted in the intake corrections. D0030 remains distinct from all three.

### Prior attempt / exact wall

`D0030-A001` already records Bradley/Peligrad's sigma-field inequality

\[
\rho(\mathcal A,\mathcal B)
\le
2\,\phi(\mathcal A,\mathcal B)^{1/2}
\]

(and the sharper asymmetric form in the source). Thus `phi*(n)->0` would immediately imply `rho*(n)->0`; the actual gap is whether ordinary past/future `phi(n)->0` controls **arbitrarily interlaced** index sets. Construction methods that prescribe weaker coefficients do not control phi's rare-event conditional-probability supremum.

### Ownership/exclusion check and create-only claim

Immediately before admission, `operations/claims/D0030.md` returned 404. Repository-wide exact-ID search found intake/catalog material and references in neighboring Bradley tracks but no active D0030 owner or paper package. `POSTED.md`, campaign `INDEX.md`, and the current exclusion ledger do not mark this exact source question settled or retired.

The create-only claim was therefore written as

`operations/claims/D0030.md`

at commit

`2b1c3d8896b835a0a06ee89c9b16addae8bea1bd`

and read back at that exact commit.

The new frozen metric is

`E_phi_rho in {0,1}`, baseline `0`.

It moves to `1` only for a full proof in the arbitrary strictly stationary source scope or a fully verified stationary phi-mixing counterexample with nonvanishing `rho*`. Restricted Markov/Gaussian/finite-alternation results leave it at `0`.

The next run starts D0030 with a new triple:

- **#2 ATTACK THE NEGATION FIRST:** try to build a rare-marker/multiscale stationary counterexample and reject it immediately if one-sided phi fails;
- **#11 DUALIZE:** formulate interlaced HGR as a conditional-expectation operator norm and test whether one-cut phi gives a tensor/completely-bounded estimate independent of alternation count;
- **#15 BREAK THE SYMMETRY:** avoid global phases and Markov structures that leak one-sided information; use asymmetric sparse scales if pursuing a counterexample.

No D0030 research theorem is claimed in this handoff/admission run.

## 7. Structured ledger delta

```yaml
ledger_delta:
  predecessor:
    track: R01
    source: D0057 / Chen-Derrida-Hu-Lifshits-Shi Conjecture 2
    metric: E_geom
    before: 1
    after: 1
    status: REFUTED_OWNER_PROOF_NOT_CLOSED_ROTATED
    unchanged_count_before: 5
    unchanged_count_after: 6
    tried_moves: [9, 16, 25]
    remaining_obligation: "Two independent source-level audits of the literal lacunary counterexample; repaired finite-third-moment Yaglom question remains separate and open."
    evidence:
      - runs/R01/20260917T1358Z_d0057_lacunary_refutation_4c8e21ab.md
      - runs/R01/20260917T1857Z_d0057_dissipation_extremals_7c3e91a4.md
      - artifacts/R01/20260917_d0057_twopoint_probe.py
      - artifacts/R01/20260917_d0057_twopoint_probe.out
    audit_ids: []
  successor:
    source: D0030 / Bradley 2005 Question 2
    metric: E_phi_rho
    baseline: 0
    status: CLAIMED_READY_CLOSABLE_OUTSIDE
    unchanged_count: 0
    next_moves: [2, 11, 15]
    remaining_obligation: "Decide full arbitrary strictly stationary phi-mixing => rho*-mixing question, without substituting the D0033 Markov special case."
    evidence:
      - operations/claims/D0030.md@2b1c3d8896b835a0a06ee89c9b16addae8bea1bd
    audit_ids: []
```

## 8. Delivery and prohibited actions

This report is the single immutable R01 report for the run. The small exact B16 checker/output are research artifacts, not receipt-only commits. I did not edit root shared ledgers or any peer track, request an audit from an incomplete package, send email, use Drive, post publicly, purchase anything, change permissions, or alter a scheduler.
