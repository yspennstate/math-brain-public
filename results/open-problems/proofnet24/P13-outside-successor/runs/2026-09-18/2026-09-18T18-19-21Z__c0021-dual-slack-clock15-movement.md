Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. SOURCE-METRIC MOVEMENT: `W_sigma = 0.083458052478335484902095404052916... -> 0.083457166870867772411698563411662...`; C0021 unchanged-run streak `0 -> 0`. Methods actually tried: B11, B17, B26.**

# P13 / C0021 — dual slack decomposition and clock-15 sporadic Bellman movement

Date: 2026-09-18 UTC. Track: P13 Outside Counterexample Research. Native slot: `6aa7b253b37c8191b693d8dc79298d37`. Own root: `proofnet24/P13-outside-successor/`.

Source target: Christophe Garban and Jeffrey E. Steif, *Noise Sensitivity of Boolean Functions and Percolation*, Chapter VIII, Exercise VIII.5 in the author-hosted published-book version: determine the exponent `sigma` for the revealment of depth-`h` iterated 3-majority on `n=3^h` unbiased leaves. The source text says the revealment is polynomially decaying and explicitly says that the value of `sigma` is open.

Status after this run: **CLAIMED / CURRENT-OPEN-LOOKING / PARTIAL / SOURCE-METRIC MOVEMENT.** No closure, novelty certificate, or independent audit is claimed.

## 1. Continuity, ownership, exclusions, and recovered state

I continued the create-only canonical ownership marker `operations/claims/C0021.md`, which names this P13 slot and this root. I did not reopen retired I0051, handed-off P0082, or six-run-handed-off D0093. I0054 was rechecked first as required and remains reserved to R11 in `operations/claims/I0054.md`; the newer R11 report `runs/R11/2026-09-18T16-40-00Z_i0054-ordinary-polynomial-occurrence-u027-c048-6d2e.md` continues that target, so P13 did not touch it.

Before research I reread the controlling owner directive at anchor `749da260517828ed311f6f1b1af74915c054bdf3`, `operations/NEW_METHODS_2026-09-16.md`, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the current C0021 claim, the newest P13 C0021 report, and repository search hits for the probability-1000 intake/attempt history. Root `RESULTS.md` is a retained configuration snapshot that still lists the retired I0051 target and itself instructs workers to recover newer complete reports; it was not allowed to overwrite the newer create-only C0021 claim/history. The screened `probability_1000_intake_*/problems.jsonl` / attempt-ledger records show no owner amendment that releases or replaces C0021.

The inherited exact reduction remains

\[
\delta_{f_h}=\frac{D_h}{3^h},\qquad
c=\lim_{h\to\infty}D_h^{1/h}=\inf_h D_h^{1/h},\qquad
\sigma=1-\log_3 c,
\]

where `D_h` is the minimum expected number of leaf queries of a zero-error deterministic decision tree under iid unbiased leaves. The frozen metric is the width of the rigorous interval for this one source exponent.

The previous certified explicit depth-4 policy had 46 overrides and exact cost

\[
U_{46}
=\frac{1332472567939180367}{36028797018963968},
\]

giving

\[
\sigma\ge
0.178401454664579389296958824632605\ldots
\]

and, with the unchanged lower-growth / upper-`sigma` endpoint

\[
\sigma\le \log_3(4/3)
=0.261859507142914874199054228685522\ldots,
\]

the frozen width

\[
W_{\rm old}
=0.083458052478335484902095404052916\ldots.
\]

## 2. Idea before code and the three required methods

The last run showed that a simple scalar buy-out rule misses interleaving option value, while sparse Bellman defects on actually reached states still improve the source interval. I therefore split this run between a lower-bound dualization and a targeted next-clock defect hunt.

- **B11 — dualize.** Instead of merely quoting the O'Donnell–Servedio/Simkin Cauchy–Schwarz lower bound, I kept its discarded nonnegative term. This gives an exact Pythagorean slack identity for every deterministic exact decision tree. It does not yet improve the exponential lower growth constant, but it identifies exactly what a stronger dual certificate must force to grow.
- **B17 — look for the numbers somewhere else.** A fresh source search located Michael Simkin's 2014 MSc thesis *Random-Turn and Richman Games*. It already studies the same uniform expected deterministic complexity of recursive ternary majority, records `D_1=5/2`, the level-2 value `393/64`, the `(9/4)^h` lower bound, and the two-level block upper base about `2.47`, and explicitly asks for the exact asymptotic complexity. This materially narrows prior-art claims: the uniform-cost reduction and `393/64` are not new.
- **B26 — hunt the sporadic case.** Starting from the exact 46-override policy, I searched the next raw query clock for isolated states at which the current continuation violates Bellman optimality. An exploratory floating-point scan proposed six candidates; the theorem below does not depend on floating point. The archived exact-arithmetic checker stores those six states/actions and independently verifies legality, reachability, sign symmetry, exact defects, exact root gains, and the final source interval.

## 3. B11: exact dual-slack decomposition

The source book's Theorem VIII.8 and Simkin's Proposition 23 use the same Cauchy–Schwarz mechanism. Keeping the orthogonal remainder gives a sharper identity.

### Theorem 3.1 — decision-tree Fourier slack identity

Let `f:{-1,+1}^N -> {-1,+1}` be balanced, and let `A` be any deterministic zero-error decision tree computing `f` under the uniform product measure. Let

\[
J_i(x)=\mathbf 1\{\text{algorithm A queries bit }i\},
\qquad
T(x)=\sum_i J_i(x),
\]

and define the queried-sign sum

\[
Q(x)=\sum_i J_i(x)x_i.
\]

Put

\[
a=\sum_i \widehat f(\{i\}).
\]

Then

\[
\boxed{\mathbb E T
=a^2+\mathbb E\bigl(Q-a f\bigr)^2.}
\]

In particular, for depth-`h` recursive ternary majority `f_h`,

\[
\boxed{
\mathbb E T
=\left(\frac94\right)^h+
\mathbb E\left(Q-\left(\frac32\right)^h f_h\right)^2.}
\]

### Proof

For each `i`, on an input for which `i` is not queried, flipping `x_i` leaves the complete decision-tree transcript unchanged, hence leaves the zero-error output `f(x)` unchanged. Pairing such inputs under the involution `x_i -> -x_i` gives

\[
\mathbb E[f(x)x_i]
=
\mathbb E[f(x)J_i(x)x_i].
\]

Summing over `i` yields

\[
a=\mathbb E[fQ].
\]

Next expand `Q^2`. The diagonal terms contribute

\[
\sum_i\mathbb E[J_i x_i^2]
=\sum_i\mathbb E[J_i]
=\mathbb ET.
\]

For `i\ne j`, the cross term
\[
\mathbb E[J_iJ_jx_ix_j]
\]
vanishes: condition on which of `i,j` is queried first and on the transcript through that first query. Before the second of the pair is queried, its sign is still an unbiased independent bit, so the conditional expectation is zero. Thus

\[
\mathbb E Q^2=\mathbb ET.
\]

Because `f` is balanced and `{±1}`-valued, `\mathbb E f^2=1`. Therefore

\[
\begin{aligned}
\mathbb E(Q-af)^2
&=\mathbb EQ^2-2a\mathbb E[fQ]+a^2\mathbb Ef^2\\
&=\mathbb ET-2a^2+a^2\\
&=\mathbb ET-a^2,
\end{aligned}
\]

which proves the first identity.

For recursive ternary majority, every leaf has first-level Fourier coefficient / influence `2^{-h}` and there are `3^h` leaves, so

\[
a=3^h2^{-h}=(3/2)^h.
\]

Substitution gives the second identity. ∎

### What this does and does not buy

Dropping the nonnegative square recovers the classical

\[
D_h\ge (9/4)^h,
\]

equivalently the current rigorous upper endpoint `sigma <= log_3(4/3)`. The exact small-depth optimal values give dual slack

\[
S_1=\frac14,\qquad
S_2=\frac{69}{64},\qquad
S_3=\frac{3852115}{1048576}.
\]

These values were recomputed by the exact artifact. They show substantial slack, but they do **not** by themselves improve the asymptotic base. Even a fixed multiplicative improvement `D_h >= (1+epsilon)(9/4)^h` has the same `h`th-root limit. A source-metric improvement on the upper endpoint would require a scale-recursive lower bound forcing the square term to carry an exponential base strictly larger than `9/4`, or an equivalent stronger dual invariant. That is the precise B11 residual.

## 4. B17: prior-art correction from Simkin 2014

The fresh literature check located Michael Simkin, *Random-Turn and Richman Games*, MSc thesis, October 2014, supervised by Gil Kalai.

Its Proposition 23 proves

\[
\mathbb E[\#\text{turns}]
\ge
\frac{(\sum_i\widehat f(i))^2}{\operatorname{Var}f}
\]

using the same queried-sign Cauchy–Schwarz argument. For recursive ternary majority it computes `\widehat f_h(i)=2^{-h}` and obtains the lower bound `(9/4)^h`. Later in the thesis it records the uniform expected deterministic complexities `D_1=5/2` and the level-2 computer value `393/64`, notes the two-level block upper base `sqrt(393/64)≈2.47`, and says it would be interesting to know the expected deterministic complexity exactly.

This is a substantive prior-art correction to the repository's older memo-level framing: neither the reduction to uniform expected deterministic decision-tree complexity nor the number `393/64` should be presented as new. Simkin's appendix says the displayed `393/64` tree is optimal but does not prove that assertion there; Jansson--Jansson (Journal of Functional Programming, 2023) later compute the two-level level-`p` complexity by exact thinning/memoization methods and therefore independently cover the `p=1/2` two-level value.

The current P13 contributions are accordingly limited to what is actually certified here: deeper exact finite costs/policies, the performance-difference machinery, the new sparse policy improvements, and the dual-slack reformulation above. No novelty claim is made for any of these without a broader citation review.

## 5. B26: six exact clock-15 Bellman witnesses

Let `pi_46` be the exact 46-override depth-4 policy from the previous report, with continuation value `E_46(s)`.

An exploratory scan of its raw query-depth-15 support proposed six improving canonical states. The exact checker verifies that the raw clock-15 support contains 1524 canonical states and that the six stored candidates are all in this support. It also verifies that every stored replacement is a legal one-leaf query and that the six states/actions form three global-sign orbits.

I do **not** use the exploratory scan to claim that these are the only improving clock-15 states. The rigorous finite claim is only that these six explicit reached states are improving witnesses.

Their exact starting Bellman defects, one value per sign orbit, are

\[
d_1=\frac{942705}{67108864},
\qquad
d_2=\frac{10110183}{1073741824},
\qquad
d_3=\frac{1988161}{536870912}.
\]

Installing the three sign orbits sequentially in decreasing defect order gives the exact total-hit coefficients and root gains

\[
\begin{array}{c|c|c}
d & H & H d\\ \hline
942705/67108864
&1287/262144
&1213261335/17592186044416\\
10110183/1073741824
&23967/4194304
&242310755961/4503599627370496\\
1988161/536870912
&23967/4194304
&47650254687/2251799813685248.
\end{array}
\]

The hit coefficients are obtained from the exact performance-difference identity already proved in the preceding P13 report, and here they are independently recovered as exact `root gain / local defect`.

### Theorem 5.1 — explicit 52-override depth-4 policy

There is an exact deterministic zero-error depth-4 decision tree for recursive ternary majority with expected uniform cost

\[
\boxed{
U_{52}
=
\frac{1332467382289843607}{36028797018963968}
=
36.98339918450487281975647\ldots
}.
\]

It improves the preceding certified policy by

\[
\boxed{
U_{46}-U_{52}
=
\frac{648206167095}{4503599627370496}
=
0.0001439306822825781\ldots.
}
\]

### Proof

The checker reconstructs the archived 46-override policy from its compressed exact tables, then decodes six additional explicit canonical-state actions. For each of the six states it verifies:

1. the state is reached by `pi_46` at raw clock 15;
2. the replacement successor pair belongs to the exact set `queries(s)` of legal one-unread-leaf actions;
3. the sign-flipped state is present and receives the sign-flipped action;
4. the exact Bellman defect is positive.

Every legal action queries one previously unread leaf, so the unresolved-leaf rank strictly decreases and the policy terminates. At a terminal state the cost is zero; at every nonterminal state the expected remaining cost is exactly

\[
E(s)=1+\frac{E(s^+)+E(s^-)}2.
\]

Exact rational dynamic programming after the three sign-orbit replacements yields successively

\[
\frac{1332470083179966287}{36028797018963968},
\quad
\frac{1332468144693918599}{36028797018963968},
\quad
\frac{1332467382289843607}{36028797018963968}.
\]

Thus the last number is the exact expected root cost of the explicit policy. ∎

The policy table has 52 overrides and canonical table SHA-256

`943e520577cc0131c482841c8b9967c4da47a3fce43bc22c78fb7d4bb6c70e75`.

## 6. Source-metric consequence

### Theorem 6.1 — improved rigorous lower endpoint for `sigma`

For the Garban--Steif iterated-3-majority revealment exponent,

\[
\boxed{
\sigma
\ge
0.178402340272047101787355665273859\ldots.
}
\]

Consequently

\[
\boxed{
W_\sigma
\le
0.083457166870867772411698563411662\ldots.
}
\]

### Proof

Use the explicit depth-4 policy as a stationary block policy. At depth `4m`, treat each depth-`4(m-1)` subtree as a virtual unbiased leaf and run the exact depth-4 policy on those virtual leaves. Independence and unbiasedness are preserved by recursive majority. If a virtual leaf is queried, evaluate that depth-`4(m-1)` subtree recursively. Therefore

\[
D_{4m}\le U_{52}^m.
\]

Hence

\[
c=\lim_hD_h^{1/h}
\le U_{52}^{1/4}
=
2.466049025987590461836763831278118\ldots.
\]

Since `sigma=1-log_3 c`,

\[
\sigma
\ge
1-\frac14\log_3 U_{52}
=
0.178402340272047101787355665273859\ldots.
\]

The upper endpoint remains `log_3(4/3)`. Subtracting gives the displayed width. ∎

The source width contracts this run by

\[
\boxed{
8.85607467712490396840641254184535\times 10^{-7}.
}
\]

This is genuine movement of the frozen source metric, so the unchanged-run streak remains/resets to zero.

## 7. Exact arithmetic artifact and self-check status

Executed exact checker:

`proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_clock15_sporadic_patch_check.py`

Creation commit:

`819865a3b8cb759efdf6d03b6f97ccc1db3ea37c`

Local SHA-256 of the exact executed script:

`77c3c605f9a4de58a800629269b7c9da0da53847f79e2c0c5817a993e6bd570a`

Archived output:

`proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_clock15_sporadic_patch_check.out`

Creation commit:

`e3d3856d8510564b484a53bfa6f20a70254f96ac`

Local SHA-256 of output:

`d7b45baa8277b826d260de92a52a3af12c2dadccb4d6fea0ffcaff4429dfcd4b`

The output ends

`ALL_EXACT_CLOCK15_SPORADIC_PATCH_CHECKS_PASS`.

This is a **P13 self-check**, not an independent audit and not closure evidence.

## 8. Fresh source and literature check, dated 2026-09-18

Fresh bounded web queries included:

- `"Exercise VIII.5" "3-majority"`
- `"iterated 3-majority" revealment exponent Garban Steif`
- `"recursive ternary majority" "expected deterministic complexity"`
- `Simkin thesis "393/64" recursive majority`
- `"iterated majority" decision tree complexity Jansson Jansson 2023`
- `"iterated 3-majority" decision tree 2024 2025 2026`
- the exact repository number `15796051` together with recursive-majority terms.

Results and limitations:

1. The author-hosted Garban--Steif book PDF was accessible and its Chapter VIII exercise sheet says in Exercise VIII.5 that the revealment of iterated 3-majority decays as `1/n^sigma` for some `sigma` and that determining `sigma` is an open question. A required screenshot request on the relevant PDF page failed with an internal fetch error; the text layer was accessible and is the source used here.
2. Michael Simkin's 2014 MSc thesis was recovered and inspected, including the Cauchy--Schwarz proposition and the recursive-majority section described above. PDF page screenshots were successfully inspected.
3. Jansson--Jansson, *Level-p-complexity of Boolean functions using thinning, memoization, and polynomials* (JFP 33, 2023, e13), computes the two-level problem; it does not determine the asymptotic exponent.
4. A 2026 search hit about majority-vote bags of decision trees concerns random-forest compression, not recursive-majority evaluation, and is irrelevant to the source question.
5. The exact `D_3` numerator search produced no relevant mathematical hit in the bounded search.

No checked primary source found in this bounded pass determines the Garban--Steif exponent. This is **bounded negative evidence only** and is not a worldwide openness or novelty certificate.

## 9. Residual problem and next run

The two sides are now sharply separated.

- **Upper-policy side:** sparse interleaving defects continue to exist one raw query clock beyond the current patch frontier. The six certified clock-15 witnesses improve the lower endpoint of `sigma`, but the gains are shrinking and finite patching alone is unlikely to identify the exact exponent.
- **Lower-dual side:** the classical `(9/4)^h` argument has an exact nonnegative remainder
  \[
  \mathbb E(Q-(3/2)^h f_h)^2.
  \]
  The missing ingredient is a hierarchical law forcing this remainder to grow with a base strictly above `9/4`, not merely to be positive at each fixed depth.

The next distinct method triple is **B1, B12, B27**: recast the dual remainder as a Hilbert-space/martingale projection problem; search for a conserved or recursive quadratic-variation identity across one majority layer; and swap the quantifiers by seeking one scale-independent dual potential valid for every decision tree rather than optimizing a separate inequality at each depth.

C0021 remains **PARTIAL**. Closure would still require a source-matching exact determination of `sigma`, prior-art review with limitations, and two OTHER-track end-to-end audits (one P26 and one distinct research track).

## 10. Structured ledger delta for P26

```yaml
ledger_delta:
  track: P13
  canonical_id: C0021
  native_slot: 6aa7b253b37c8191b693d8dc79298d37
  status_before: CLAIMED_CURRENT_OPEN_LOOKING_PARTIAL
  status_after: CLAIMED_CURRENT_OPEN_LOOKING_PARTIAL
  closure_claimed: false
  metric:
    name: W_sigma
    domain: single Garban-Steif iterated-3-majority revealment exponent
    before: "0.083458052478335484902095404052916273307627595753522462739367968207135851225971433022261585"
    after: "0.083457166870867772411698563411662088772617906263776172160449155589357546161578294835215245"
    target: "0"
    movement: true
  sigma_lower:
    before: "0.178401454664579389296958824632605435291543684510238393001941919470234551535858177100083791"
    after: "0.178402340272047101787355665273859619826553373999984683580860732088012856600251315287130131"
  unchanged_run_streak:
    before: 0
    after: 0
  methods_tried: [B11, B17, B26]
  main_new_claims:
    - exact decision-tree Fourier slack identity
    - explicit legal 52-override depth-4 policy
    - certified depth-4 cost U52 = 1332467382289843607/36028797018963968
  prior_art_correction:
    - Simkin 2014 already treats the uniform expected deterministic complexity and records 393/64 at level two
  self_check:
    checker: proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_clock15_sporadic_patch_check.py
    checker_commit: 819865a3b8cb759efdf6d03b6f97ccc1db3ea37c
    output: proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_clock15_sporadic_patch_check.out
    output_commit: e3d3856d8510564b484a53bfa6f20a70254f96ac
    pass_marker: ALL_EXACT_CLOCK15_SPORADIC_PATCH_CHECKS_PASS
    independent_audit: false
  next_methods: [B1, B12, B27]
  shared_root_files_modified: false
  peer_files_modified: false
```
