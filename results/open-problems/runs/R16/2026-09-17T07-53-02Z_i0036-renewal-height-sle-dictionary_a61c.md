Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested in prompt text, but this runtime exposes no authenticated model selector, reasoning-effort selector, or applied-effort telemetry, so GPT-6/maximum is not claimed. **NO MOVEMENT:** `epsilon_bridge: 9e-10 -> 9e-10`; supported unchanged count `0 -> 1`. Methods actually tried: **#18 SAY IT IN ANOTHER LANGUAGE, #13 FIND WHAT ONLY INCREASES, #21 ASK WHO ELSE HAS THIS SHAPE**.

# R16 HARD OUTSIDE — I0036 / Schramm Problem 2.1: bridge decay as renewal-height growth, and the exact SLE bridge-exponent dictionary

Date: 2026-09-17 UTC.  
Repository/branch: `yspennstate/math-open-problems` / `master`.  
Current source status: **PARTIAL / OPEN**.  
This run's mathematical status: **new repository consequence of the existing R16 bridge bound; underlying renewal structure is classical; publication novelty is not claimed**.

## 1. Continuity and frozen metric

I continued from the newest complete R16 report

`runs/R16/2026-09-17T06-52-00Z_i0043-handoff_i0036-bridge-exponent-9e10_4f2a.md`.

That report completed the mandatory rotation away from I0043 after two stuck recoveries, created the exclusive R16 claim `operations/claims/I0036.md`, and proved

\[
B_T\le 1000\,T^{-\varepsilon},\qquad
\varepsilon=9\cdot 10^{-10},\qquad T\ge1,
\tag{1.1}
\]

for the critical hexagonal-lattice bridge partition function in the Krachun--Panagiotis normalization. It moved the fixed metric from the published `1e-10` to `9e-10` and reset the unchanged count to zero.

The fixed metric remains

`epsilon_bridge` = the largest explicit exponent `epsilon>0` for which R16 has a complete proof of an all-`T` bound `B_T <= C_epsilon T^{-epsilon}` with explicit finite `C_epsilon` in the same normalization.

I do **not** change that metric merely because a consequence of (1.1) is proved below. Hence the metric is honestly unchanged this run.

## 2. Required repository/source recovery

Before new mathematics I recovered/read:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and the controlling owner directive;
- newest own R16 report above;
- current exclusive claim `operations/claims/I0036.md`;
- the neighboring R09 admission report that originally screened I0036 as current-looking HARD;
- the old R11 planar-SAW renewal report `runs/R11/2026-09-16T14-40-03Z_saw-quantitative-renewal-trace-b7c2.md`, specifically to avoid silently duplicating its length-renewal calculations. That R11 route studied renewal **times/lengths** under the Kesten law; the present route concerns the additive **vertical height** whose renewal mass is the critical height-`T` bridge partition function.

The intake corpus is too large to render row by row through the connector, so I used the exact I0036 intake/claim plus current source/ownership searches rather than pretending a literal model-visible reread of every JSONL row.

The source remains Oded Schramm, *Conformally invariant scaling limits: an overview and a collection of problems*, ICM 2006, arXiv:math/0602151, Problem 2.1: prove that the infinite half-plane planar self-avoiding walk has a small-mesh scaling limit and identify it with `SLE_8/3`.

Fresh dated search again found no fixed-lattice source-closing proof. Krachun--Panagiotis, arXiv:2310.17299, remains a strong partial input: polynomial critical bridge decay plus quantitative sub-ballisticity. A bounded negative search is not a global novelty certificate.

## 3. Beck--Fiala stale-title refresh

The native title still names Beck--Fiala, so I checked the source status rather than silently relying on an older report.

Bansal--Jiang, arXiv:2508.03961v2, prove `O(sqrt(t))` for `t >= log^2 n`, together with a weaker polylogarithmic-loss bound below that regime, and their results are polynomial-time algorithms.

Guo--Fang--Lu, arXiv:2609.11189v1, submitted 2026-09-10, state a `3 sqrt(2 pi)` dimension-free Komlos signing theorem and explicitly deduce

\[
\operatorname{disc}(A)<3\sqrt{2\pi t}
\]

for every finite set system of maximum element degree `t>=1`, with no restriction on `n`. This is a very recent primary-preprint resolution claim, not mature refereed validation.

A separate 2026-09-14 preprint by Guillen--Kobzar proves a **complex/unit-modulus** Komlos variant. It is not a Boolean-sign substitute and is not used here; the owner instruction explicitly forbids switching the Boolean-sign problem to vector/complex signs.

Under the continuity/exclusion rule R16 therefore remains on its admitted I0036 successor rather than restarting Beck--Fiala from a stale scheduler title.

## 4. Method #18 — say the bridge estimate in renewal language

The Kesten bridge decomposition is exactly the right language for (1.1).

Let `I` be the set of irreducible half-plane bridges in the same hexagonal-lattice critical normalization, and let

\[
Q(\eta)=x_c^{|\eta|},\qquad \eta\in I,
\]

where `x_c=1/mu`. Kesten's relation says

\[
\sum_{\eta\in I}x_c^{|\eta|}=1,
\]

so `Q` is a probability law. Alberts--Duminil-Copin review this exact discrete decomposition before constructing its SLE analogue: an infinite half-plane SAW is an i.i.d. concatenation of irreducible bridges under `Q`, and bridge endpoints are renewal points.

Let

\[
H(\eta)=\text{vertical strip-height increment of the irreducible bridge }\eta,
\]

and let `H_1,H_2,...` be iid copies. Put

\[
S_0=0,\qquad S_k=H_1+\cdots+H_k.
\]

Because the bridge decomposition is unique, heights add under concatenation, and critical weights multiply, the critical partition function of bridges of height `T` is exactly the renewal mass

\[
\boxed{
B_T=\sum_{k\ge1}\Pr(S_k=T),\qquad T\ge1,
}
\tag{4.1}
\]

with `B_0=1` for the empty concatenation. This is classical renewal structure, not a new theorem claim.

Define the renewal counting function

\[
N(T)=\max\{k:S_k\le T\}
\]

and renewal function

\[
U(T)=\mathbb E[N(T)+1].
\]

Summing (4.1) gives the exact identity

\[
\boxed{
U(T)=\sum_{s=0}^T B_s.
}
\tag{4.2}
\]

Thus the R16 bridge estimate is immediately a quantitative theorem about the vertical renewal process of the infinite half-plane SAW, not merely a partition-function estimate detached from Schramm's source.

From (1.1), for all integers `T>=1`,

\[
\begin{aligned}
U(T)
&\le 1+1000\sum_{s=1}^T s^{-\varepsilon}\\
&\le 1+\frac{1000}{1-\varepsilon}T^{1-\varepsilon}\\
&\le C_\varepsilon T^{1-\varepsilon},
\end{aligned}
\tag{4.3}
\]

where

\[
C_\varepsilon:=1+\frac{1000}{1-\varepsilon}.
\tag{4.4}
\]

This is the first useful translation: the expected number of irreducible-bridge renewals below height `T` is at most order `T^{1-epsilon}`.

## 5. Method #13 — a monotone height observable forced to diverge polynomially

The natural monotone scale observable is the truncated irreducible-bridge height

\[
m(T):=\mathbb E[H\wedge T].
\]

It is nondecreasing in `T`. The following elementary renewal lemma converts an upper bound on `U(T)` into a lower bound on `m(T)`.

### Lemma R16-I0036-C02

For every positive-integer-valued renewal increment `H` and every integer `T>=1`,

\[
\boxed{
m(T)\ge \frac{T}{8U(T)}.
}
\tag{5.1}
\]

Consequently, for the critical hexagonal irreducible-bridge height and the R16 exponent `epsilon=9e-10`,

\[
\boxed{
\mathbb E[H\wedge T]
\ge
\frac{1}{8C_\varepsilon}T^{\varepsilon}
\qquad(T\ge1).
}
\tag{5.2}
\]

In particular, `E H = infinity`, with an explicit polynomial lower rate for the divergence of the truncated mean.

### Proof

Fix `T` and put

\[
m=m(T),\qquad x=\frac{T}{2m}.
\]

If `x<2`, then `m>T/4`. Since `U(T)>=1`,

\[
m>\frac T4\ge\frac{T}{8U(T)},
\]

so (5.1) holds.

Assume now `x>=2` and set

\[
K=\lfloor x\rfloor.
\]

Then `K>=x/2`. For every integer `k` with `2<=k<=K`, let

\[
Y_i=H_i\wedge T.
\]

We have

\[
\mathbb E\sum_{i=1}^kY_i=km\le Km\le xm=T/2.
\]

Markov's inequality therefore gives

\[
\Pr\!\left(\sum_{i=1}^kY_i\le T\right)\ge\frac12.
\tag{5.3}
\]

On the event in (5.3), no `H_i` can exceed `T`: if some `H_i>T`, then `Y_i=T`, and because `k>=2` and all height increments are positive integers, the other `Y_j` contribute at least one, forcing the truncated sum to exceed `T`. Hence on (5.3),

\[
S_k=\sum_{i=1}^kH_i=\sum_{i=1}^kY_i\le T.
\]

Thus

\[
\Pr(S_k\le T)\ge\frac12
\qquad(2\le k\le K).
\]

Using `U(T)=sum_{k>=0} P(S_k<=T)`, we obtain

\[
U(T)\ge 1+\frac{K-1}{2}=\frac{K+1}{2}\ge\frac K2\ge\frac x4=\frac{T}{8m}.
\]

Rearranging proves (5.1). Combining (5.1) with (4.3) yields (5.2). ∎

This statement is an elementary consequence of classical renewal structure plus the R16 bridge bound; I make no publication-novelty claim for the abstract renewal lemma.

### A second direct consequence: lower quantiles of renewal heights

For every `k,T`,

\[
\{S_k\le T\}\subseteq\{N(T)\ge k\},
\]

so Markov's inequality gives

\[
\boxed{
\Pr(S_k\le T)
\le \frac{\mathbb E N(T)}{k}
\le \frac{U(T)}{k}
\le \frac{C_\varepsilon T^{1-\varepsilon}}{k}.
}
\tag{5.4}
\]

Thus the `k`-th bridge renewal height has a rigorous one-sided superlinear scale: for any fixed `delta in (0,1)`, whenever

\[
C_\varepsilon T^{1-\varepsilon}\le\delta k,
\]

we have `P(S_k<=T)<=delta`. Equivalently, its lower quantiles grow at least like

\[
k^{1/(1-\varepsilon)}.
\tag{5.5}
\]

With `epsilon=9e-10`, this exponent is only microscopically above one, but it is now in exactly the variable that the continuum SLE bridge decomposition predicts.

## 6. Method #21 — the same renewal exponent appears in SLE_8/3

The strongest conceptual connection this run is to Alberts--Duminil-Copin, *Bridge Decomposition of Restriction Measures*, arXiv:0909.0203 / J. Stat. Phys. 140 (2010).

They construct the continuum analogue of Kesten's bridge decomposition. For a chordal restriction measure of exponent `alpha_restr<1`, the set of bridge heights is the closed range of a stable subordinator of index

\[
\beta=2-2\alpha_{\rm restr}.
\tag{6.1}
\]

Lawler--Schramm--Werner identify chordal `SLE_8/3` with restriction exponent

\[
\alpha_{\rm restr}=5/8.
\]

Therefore the `SLE_8/3` bridge-height regenerative set has stable index

\[
\boxed{\beta=2-2(5/8)=3/4.}
\tag{6.2}
\]

Alberts--Duminil-Copin also show that the continuum irreducible-bridge height tail under their sigma-finite bridge measure scales with this stable law, and explicitly emphasize that the vertical-height distribution is the principal property they can determine.

For a renewal/stable process of index `beta`, the renewal mass has the power-law exponent

\[
u_T\asymp T^{\beta-1}=T^{-(1-\beta)}.
\]

Hence the SLE bridge decomposition predicts

\[
\boxed{B_T\asymp T^{-1/4},}
\tag{6.3}
\]

exactly the exponent Krachun--Panagiotis themselves cite as the SLE prediction.

This yields an exact exponent dictionary:

\[
\boxed{
\varepsilon_{\rm bridge}=1-\beta,
\qquad
\text{renewal-height scale exponent}=\frac1\beta=\frac1{1-\varepsilon_{\rm bridge}}.
}
\tag{6.4}
\]

The conjectural SLE value `epsilon_bridge=1/4` corresponds to `beta=3/4` and `S_k` scale `k^{4/3}`. The present rigorous R16 value `epsilon_bridge=9e-10` corresponds, via (5.4), to a one-sided renewal-height exponent `1/(1-9e-10)`.

This does **not** prove convergence to the stable subordinator, and it does not improve the frozen bridge exponent. What it does is place the current quantitative theorem on the same observable as the continuum target.

## 7. Why this still does not give curve tightness

I specifically tested whether the renewal reformulation could be fed directly into a standard random-curve compactness theorem.

Aizenman--Burchard prove that suitable scale-invariant bounds on repeated crossings of annuli imply Hölder regularity and tightness/precompactness of random curves. That is the kind of mechanism needed for the **existence** half of Schramm Problem 2.1.

The bridge-renewal estimate above is insufficient by itself. It only records the vertical levels at which the entire future path lies above the current bridge line. Between two consecutive renewal heights, a single irreducible bridge can make many lateral excursions and many crossings of a Euclidean annulus. Sparse vertical renewals therefore do not imply an annulus multi-crossing bound.

This is not merely a bookkeeping complaint. Alberts--Duminil-Copin explicitly note that, even in their continuum bridge decomposition, the vertical height law is essentially the one principal property of irreducible bridges they can determine and that much more about bridge geometry remains difficult. That is exactly the missing information in the discrete route.

A source-relevant next target is therefore a **shape estimate for one critical irreducible bridge**, for example a uniform aspect-ratio tail of the schematic form

\[
Q\!\left(
W(\eta)\ge R h
\;\middle|\;
H(\eta)\in[h,2h]
\right)
\le C R^{-\rho}
\tag{7.1}
\]

for some explicit `rho>0`, uniformly in large `h`, where `W` is horizontal diameter. A repeated-annulus-crossing estimate would be even better. Combined with the renewal-height sparsity, such a theorem has a plausible path to Aizenman--Burchard tightness. Without a shape bound, another manipulation of `B_T` alone is unlikely to move the scaling-limit source.

I do **not** claim (7.1); it is the newly isolated missing theorem.

## 8. What moved and what did not

The frozen metric did not move:

\[
\boxed{
epsilon_{\rm bridge}:9\cdot10^{-10}\longrightarrow9\cdot10^{-10}.
}
\]

Supported unchanged count becomes `1`.

Substantive mathematical progress this run is instead structural:

1. the R16 `B_T` theorem is recast exactly as an upper bound on a renewal mass;
2. it yields the complete quantitative consequence
   \[
   E[H\wedge T]\ge [8C_\varepsilon]^{-1}T^\varepsilon;
   \]
3. it yields the lower-quantile renewal-height bound (5.4);
4. the SLE bridge decomposition gives the exact exponent dictionary `epsilon=1-beta`, with target `beta=3/4`;
5. the failure to reach tightness is localized to irreducible-bridge **shape**, not renewal height.

That is useful enough to retain, but it is **PARTIAL** and does not justify metric relabeling.

## 9. Next methods if I0036 continues

Do not repeat `18,13,21` next run. The most useful fresh triple is:

- **#24 FIND THE EXTREMAL OBJECT:** among irreducible bridges of a fixed height, identify configurations maximizing horizontal diameter / annulus crossings and see whether the parafermionic observable penalizes them;
- **#15 BREAK THE SYMMETRY ON PURPOSE:** condition on a bridge with a large one-sided lateral excursion rather than using symmetric strip sums, to expose a directional observable;
- **#25 COUNT THE SAME THING TWICE:** count bridges with a large lateral excursion once by irreducible-height decomposition and once by a cut-and-reflect / parafermionic boundary decomposition.

The concrete milestone is not another tiny optimization of `epsilon_bridge`; it is any uniform positive-power control of irreducible-bridge aspect ratio or repeated annulus crossings compatible with the critical Kesten law.

## 10. Validation / artifacts

No checker artifact was created this run. The new result is an infinite renewal-theoretic implication with a full proof on the page, not a finite enumeration. The only numerical value used is the already certified previous-run `epsilon=9e-10` bridge theorem.

The prior exact bridge-exponent certificate remains in

`artifacts/R16/2026-09-17T06-45-00Z_i0036_bridge_exponent_exact.py`

and its archived output; this run does not create a redundant receipt-only artifact.

No closure is claimed. I0036 remains **PARTIAL / OPEN** and lacks the source-level theorem and required outside audits.

## 11. Model/reasoning and task-permission status

The exposed scheduler/task schema still offers title/prompt, schedule or relative start, timing mode, enablement and task identity, but **no model-family field and no reasoning-effort field**. GPT-6/maximum therefore remains a prompt request only; this run's actual model is GPT-5.6 Sol and reasoning level is UNVERIFIED.

The historical P26 `You cannot modify this task` error was context-dependent: current `RESULTS.md` records that the P26 prompt update later succeeded from a different authorized owning context. The compliant workaround is an authorized owner/workspace context or platform support, not permission bypass or duplicate tasks. Actually enforcing GPT-6/maximum would require the product/workspace scheduler/API to expose model and reasoning controls plus authenticated runtime telemetry.

No scheduler modification was attempted.

## 12. Prohibited-action audit

No email/Gmail, Drive write, public posting, purchase, permission change, workflow execution, scheduler mutation, shared-root edit, peer-track edit, force-push, or new schedule was performed.

## 13. Structured ledger_delta

```yaml
ledger_delta:
  track: R16
  source_id: I0036
  source: "Schramm ICM 2006 Problem 2.1, half-plane planar SAW scaling limit to SLE_8/3"
  state: PARTIAL_OPEN
  ownership: "operations/claims/I0036.md; R16 exclusive"
  metric: epsilon_bridge
  before: 9e-10
  after: 9e-10
  unchanged_count_before: 0
  unchanged_count_after: 1
  methods_this_run: [18, 13, 21]
  retained_claims:
    - "B_T <= 1000 T^(-9e-10) for all T>=1, from previous R16 report"
  new_internal_claims:
    - id: R16-I0036-C02
      statement: "For the critical irreducible bridge height H, E[min(H,T)] >= T/(8 U(T)) >= [8 C_epsilon]^-1 T^epsilon, where U(T)=sum_{s<=T}B_s and C_epsilon=1+1000/(1-epsilon)."
      status: PROVED_ON_PAGE_INTERNAL_CONSEQUENCE
      novelty: UNVERIFIED_NOT_CLAIMED
    - id: R16-I0036-C03
      statement: "P(S_k <= T) <= C_epsilon T^(1-epsilon)/k, giving one-sided renewal-height lower quantile exponent 1/(1-epsilon)."
      status: PROVED_ON_PAGE_INTERNAL_CONSEQUENCE
      novelty: UNVERIFIED_NOT_CLAIMED
  nearest_continuum_shape:
    source: "Alberts--Duminil-Copin, arXiv:0909.0203"
    fact: "SLE_8/3 restriction exponent 5/8 -> bridge-height stable subordinator index 3/4 -> predicted bridge renewal exponent 1/4"
  obstruction:
    statement: "renewal-height control alone does not bound repeated Euclidean annulus crossings inside one irreducible bridge"
    next_required_object: "uniform irreducible-bridge shape/aspect-ratio or annulus-crossing estimate"
  next_methods: [24, 15, 25]
  checker: NONE_ANALYTIC_FULL_PROOF_ON_PAGE
  bech_fiala_refresh:
    bansal_jiang: "arXiv:2508.03961v2; O(sqrt(t)) for t>=log^2 n, weaker sparse regime, algorithmic"
    guo_fang_lu: "arXiv:2609.11189v1; claims all-t Boolean Komlos consequence disc < 3 sqrt(2 pi t); very recent preprint"
    complex_sign_note: "Guillen--Kobzar 2026 complex/unit-modulus result is not substituted for Boolean signs"
  delivery: PRIVATE_GITHUB_ONLY
```
