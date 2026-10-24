Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested in prompt text, but this runtime exposes no authenticated model-family selector, reasoning-effort selector, or applied-effort telemetry, so GPT-6/maximum is not claimed. **NO METRIC MOVEMENT:** H0022 `A_cyc(1+epsilon): UNMEASURED -> UNMEASURED`; supported H0022 substantive unchanged count `0 -> 1`; methods actually used: **#2 ATTACK THE NEGATION FIRST, #18 SAY IT IN ANOTHER LANGUAGE, #24 FIND THE EXTREMAL OBJECT**.

# R16 HARD OUTSIDE — H0022 first substantive run: first-moment extremal type, type-entropy reduction, and two exact route obstructions

Date: 2026-09-18 UTC. Repository/branch: `yspennstate/math-open-problems` / `master`.

Active source: H0022 = Asaf Cohen Antonir, Lyuben Lichev, Maksim Zhukovskii, *Universality in random graphs via optimal linking systems: trees and beyond*, arXiv:2608.06358v1 (6 August 2026), Section 1.6, **Conjecture 1.5 (cycle-factor universality)**.

Source status after this run: **OPEN / PARTIAL METHOD PROGRESS**. No source theorem is claimed proved or refuted.

## 1. Continuity, exclusions, ownership, and source refresh

This run continues from

`runs/R16/2026-09-18T00-46-50Z_h0021-spread-capacity-handoff-h0022_91e4.md`

and the active exclusive claim

`operations/claims/H0022.md`.

It does **not** restart the stale Beck--Fiala scheduler title, handed-off I0036, or handed-off H0021. The preceding R16 run exhausted the two allowed HARD recoveries on H0021, preserved a complete handoff, and created the H0022 claim. The fixed H0022 metric is therefore the one in that claim, not the stale native title's discrepancy quantity.

Before new mathematics I reread/recovered the required campaign surfaces: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, the H0022 claim, the newest own R16 report, the H-intake verification, and the neighboring H0023/P20 final report. The neighbor is useful because H0023's all-permutation linking-system route already isolated growing-uniformity and perfect-completion barriers; H0022 should not silently re-run that stronger quantifier.

A fresh bounded current-source search on 2026-09-18 still finds arXiv:2608.06358v1 as the current primary source and no later source-matching proof of Conjecture 1.5. This is dated bounded evidence, not a worldwide openness or novelty certificate.

The source itself explicitly states that determining thresholds for the existence of `C_ell`-factors for all `ell=omega(1)` remains open, then conjectures that for every fixed `epsilon>0` and every integer

\[
\ell\ge (1+\epsilon)\frac{\log n}{\log\log n},
\]

whp

\[
G\!\left(n,(1+\epsilon)\frac{\log n}{n}\right)
\]

is universal for every `n`-vertex cycle factor of girth at least `ell`. The same paper proves only a large-constant baseline: for sufficiently large absolute `C`, girth at least `100 log n/loglog n` suffices at density `C log n/n`, together with a more general order-level theorem for `C(log n)^psi/n`.

The older fixed-girth theorem of Ferber--Kronenberg--Luh gives the correct order for **fixed** cycle length, not the growing `ell ~ log n/loglog n` regime. Glebov--Krivelevich count Hamilton cycles down to the Hamiltonicity threshold, but that controls one cycle type, not all long-cycle partitions. I found no prior source in the bounded search containing the elementary first-moment envelope proved below; I make **no publication-novelty claim** for it.

## 2. Frozen metric

For fixed `c>1`, `A_cyc(c)` is the smallest constant `A` for which R16 has a complete proof that

\[
G(n,c\log n/n)
\]

is whp universal for every `n`-vertex cycle factor whose cycles all have length at least

\[
A\frac{\log n}{\log\log n},
\]

with every restriction on `c`, `A`, divisibility, and asymptotic quantifier retained. If no R16 proof exists at a given `c`, the value is `UNMEASURED`, not infinity.

Before this H0022 run:

`A_cyc(1+epsilon) = UNMEASURED`.

After this run:

`A_cyc(1+epsilon) = UNMEASURED`.

The source target is

\[
A_{\rm cyc}(1+\epsilon)\le 1+\epsilon
\qquad\text{for every fixed }\epsilon>0.
\]

The new results below isolate the extremal first-moment type and rule out two naive proof architectures, but do not produce a complete universality theorem; hence the fixed metric does not move.

## 3. #2 ATTACK THE NEGATION FIRST — exact first moment for every cycle type

A cycle-factor is determined up to isomorphism by an integer partition

\[
\lambda=(\lambda_1,\ldots,\lambda_m),
\qquad
\lambda_i\ge 3,
\qquad
\sum_i\lambda_i=n.
\]

Let `r_s` be the multiplicity of the part `s` in `lambda`. Let `F_lambda` denote this unlabeled cycle-factor type, and let `X_lambda` be the number of labeled copies of `F_lambda` in `G(n,p)`.

### Lemma 1 (exact count and expectation)

The number of labeled copies of `F_lambda` in `K_n` is

\[
N_\lambda
=
\frac{n!}
{2^m\left(\prod_{i=1}^m\lambda_i\right)
 \left(\prod_{s\ge3}r_s!\right)}.
\]

Consequently, because every cycle factor has exactly `n` edges,

\[
\boxed{
\mathbb E X_\lambda
=
\frac{n!\,p^n}
{2^m\left(\prod_i\lambda_i\right)
 \left(\prod_s r_s!\right)}.
}
\]

### Proof

Partition `[n]` into vertex sets of sizes `lambda_1,...,lambda_m`, dividing by `r_s!` for permutations of equal-sized parts. On a labeled set of size `s`, the number of undirected cycles is `(s-1)!/2`. Thus

\[
\frac{n!}{\prod_i\lambda_i!\prod_s r_s!}
\prod_i\frac{(\lambda_i-1)!}{2}
=
\frac{n!}
{2^m\prod_i\lambda_i\prod_s r_s!}.
\]

Each copy needs exactly `n` independent graph edges, giving the expectation formula. `square`

### Equal-short-cycle stress family

Assume `k | n` and set `m=n/k`. For the `C_k`-factor type,

\[
\boxed{
\mathbb E X_k
=
\frac{n!}{(2k)^m m!}\,p^n.
}
\]

Put

\[
p=c\frac{\log n}{n},\qquad c>1\text{ fixed}.
\]

Stirling's formula gives

\[
\log\mathbb E X_k
=
n\left[
\log(c\log n)-1
-\frac{\log(2n)-1}{k}
\right]
+O(\log n).
\]

Hence the exact first-moment transition scale for this stress family is

\[
\boxed{
 k_{\rm FM}(c,n)
 :=
 \frac{\log(2n)-1}{\log(c\log n)-1}
 =
 (1+o(1))\frac{\log n}{\log\log n}.
}
\]

For every fixed `eta>0`, along divisibility subsequences on which

\[
k\le(1-\eta)k_{\rm FM}(c,n),
\]

we have

\[
\log\mathbb E X_k=-\Omega_\eta(n\log\log n),
\]

and therefore by Markov's inequality whp no `C_k`-factor exists.

This does **not** refute H0022: the source asks for `k` a fixed multiplicative factor **above** the leading `log n/loglog n` scale. What it does is identify a sharper, `c`-dependent second-order first-moment boundary than the source's rough `(1-o(1)) log n/loglog n` obstruction.

A useful expansion is obtained by setting

\[
k=a\frac{\log n}{\log\log n}
\]

with fixed `a>0`. Then

\[
\frac1n\log\mathbb E X_k
=
\left(1-\frac1a\right)\log\log n
+\log c-1+o(1).
\]

In particular, at the exact leading coefficient `a=1`, the constant `log c-1` still matters, while any fixed `a>1` wins by order `n loglog n`.

## 4. #24 FIND THE EXTREMAL OBJECT — a uniform first-moment envelope over all admissible types

The equal-short-cycle calculation is not merely one example. It controls the entire first-moment lower envelope.

Fix an integer `ell>=3` and let

\[
M:=\left\lfloor\frac n\ell\right\rfloor.
\]

Let `lambda` be **any** cycle type all of whose parts are at least `ell`, and let it contain `m` cycles. Then `m<=M`.

Write

\[
D_\lambda
:=
2^m\prod_i\lambda_i\prod_s r_s!,
\]

so `E X_lambda=n!p^n/D_lambda`.

By AM--GM,

\[
\prod_i\lambda_i\le\left(\frac nm\right)^m,
\]

and trivially

\[
\prod_s r_s!\le m!.
\]

Therefore

\[
D_\lambda
\le
2^m\left(\frac nm\right)^m m!
=:g(m).
\]

The sequence `g(m)` is strictly increasing over the relevant range, since

\[
\frac{g(m+1)}{g(m)}
=
2n\left(\frac{m}{m+1}\right)^m
>
\frac{2n}{e}>1.
\]

Thus `D_lambda<=g(M)`, and we obtain the following uniform theorem.

### Lemma 2 (uniform first-moment lower envelope)

For every cycle type `lambda` with minimum cycle length at least `ell`,

\[
\boxed{
\mathbb E X_\lambda
\ge
\frac{n!p^n}
{2^M(n/M)^M M!}.
}
\]

For `p=c log n/n`, Stirling gives

\[
\boxed{
\log\mathbb E X_\lambda
\ge
n[\log(c\log n)-1]
-M[\log(2n)-1]
-O(\log n).
}
\]

If

\[
\ell=a\frac{\log n}{\log\log n}
\]

for a fixed `a>1`, then uniformly over **every** admissible type,

\[
\boxed{
\log\mathbb E X_\lambda
\ge
n\left[
\left(1-\frac1a\right)\log\log n
+\log c-1+o(1)
\right].
}
\]

At the exact source parameters `a=c=1+epsilon`,

\[
\boxed{
\inf_{\lambda:\,\min\lambda_i\ge\ell}
\log\mathbb E X_\lambda
\ge
\left(\frac{\epsilon}{1+\epsilon}+o(1)\right)
 n\log\log n.
}
\]

So at the conjectured sharp density **every admissible cycle type has exponentially enormous expected copy count**. There is no first-moment counterexample hidden among irregular mixtures of long cycle lengths.

When `ell | n`, the equal `C_ell`-factor has `M=n/ell` cycles and attains the denominator `g(M)` exactly. Hence on these divisibility subsequences the factor consisting of as many shortest allowed cycles as possible is the exact first-moment extremal object. This justifies treating equal-short factors as the canonical negation stress test, rather than an arbitrary example.

This is a route result, not a proof of existence: huge expectation does not control the very strong dependence between copies.

## 5. #18 SAY IT IN ANOTHER LANGUAGE — universality is over integer partitions, not endpoint permutations

The key quantifier difference between H0022 and neighboring H0023 is now useful.

H0023 asks a single host graph to realize **every endpoint permutation** in a linking system. H0022 asks only for one copy of every **isomorphism type** of cycle factor. Such types are just integer partitions of `n` with all parts at least `ell`.

The total number of integer partitions satisfies

\[
p(n)=\exp(O(\sqrt n)),
\]

so H0022 has only `exp(O(sqrt n))` target types, enormously fewer than the factorially many endpoint permutations in H0023. This opens a route that genuinely bypasses Conjecture 1.6: prove an extremely strong fixed-type lower tail and union-bound over cycle structures.

However, two exact obstructions show that the naive version of that plan is wrong.

### 5.1 Common-host obstruction: unconditional type tails can never be exponentially small

Every spanning cycle factor requires every vertex to have degree at least two. For any fixed vertex `v`,

\[
\Pr(v\text{ is isolated})
=(1-p)^{n-1}
=n^{-c+o(1)}
\]

when `p=c log n/n`.

Therefore, for **every** cycle type `lambda`,

\[
\boxed{
\Pr(X_\lambda=0)
\ge
n^{-c+o(1)}.
}
\]

In particular, no unconditional estimate of the form

\[
\Pr(X_\lambda=0)\le e^{-\omega(\sqrt n)}
\]

can possibly hold. Thus an unconditional union bound over the `exp(O(sqrt n))` types is structurally impossible even if all type-specific difficulties were solved: all types share the same polynomially rare low-degree host failures.

The correct quantifier swap must first factor out a **common good-host event** `H_n` (at minimum `delta(G)>=2`, and likely also robust expansion / typical degree information), and seek a conditional estimate such as

\[
\sup_{\lambda:\min\lambda_i\ge\ell}
\Pr(X_\lambda=0\mid H_n)
\le
\exp[-\omega(\sqrt n)].
\]

Since `P(H_n)=1-o(1)` at every fixed `c>1`, this conditional route would be enough for universality while allowing the common polynomial tail outside `H_n`.

This is the same logical phenomenon that appeared in R16's previous tree-universality attack, but here the type space is only `exp(O(sqrt n))`, making the conditional-union route quantitatively much more plausible.

### 5.2 Exact obstruction to the plain unconditioned second moment

Fix a type `lambda` and let `F,F'` be independent uniformly random labeled copies of that type in `K_n`. Put

\[
K:=|E(F)\cap E(F')|.
\]

Because every factor has exactly `n` edges and the uniform copy distribution is edge-transitive,

\[
\Pr(e\in F')
=\frac{n}{\binom n2}
=\frac{2}{n-1}
\]

for every fixed host edge `e`. Hence

\[
\boxed{
\mathbb E K
=\frac{2n}{n-1}.
}
\]

For

\[
X_\lambda=\sum_F {\bf1}_{\{F\subseteq G\}},
\]

we have the exact identity

\[
\frac{\mathbb E X_\lambda^2}
{(\mathbb E X_\lambda)^2}
=
\mathbb E_{F,F'}[p^{-K}].
\]

Since `x -> p^{-x}` is convex,

\[
\boxed{
\frac{\mathbb E X_\lambda^2}
{(\mathbb E X_\lambda)^2}
\ge
p^{-2n/(n-1)}
=
\left(\frac{n}{c\log n}\right)^{2+o(1)}
\longrightarrow\infty.
}
\]

Therefore the **plain, unconditioned bounded-relative-variance / Paley--Zygmund approach is impossible for every cycle type**, including the extremal equal-short type. This is not a theorem that all second-moment ideas fail; it identifies exactly what a successful moment method must remove or condition away: overlap clustering and common host fluctuations.

Together, Sections 5.1 and 5.2 say the next method should not be "compute the variance more carefully". It should be a conditional / quenched argument after removing the common host obstruction, most naturally through degree/edge-count conditioning, switchings, a truncated-cluster expansion, or an entropy argument on a typical host.

## 6. What the three methods actually taught us

### #2 — negation-first

No cycle-length mixture beats the short equal-cycle stress family at first-moment level. The source's leading coefficient `1` is real: below the explicit `k_FM(c,n)` scale, equal-short factors disappear by first moment. At the source's `(1+epsilon)` scale, however, first moments are overwhelmingly positive.

### #24 — extremal object

The worst first-moment type is "as many shortest allowed cycles as arithmetic permits"; when divisibility is exact, the `C_ell`-factor attains the uniform denominator envelope exactly. Thus future negative tests should begin with this family, not with exotic length mixtures.

### #18 — new language

Cycle-factor universality is a problem over `exp(O(sqrt n))` integer partitions, not an all-permutation routing problem. That is a major quantitative simplification relative to H0023. But the union must occur **conditional on one common good-host event**, and the naive unconditioned second moment provably has diverging relative variance.

These conclusions are compatible with the primary source: it explicitly says even the existence threshold for `C_ell`-factors for all growing `ell` is still open, and it proposes optimal linking systems only as a possible intermediate route rather than an equivalence.

## 7. Nearest tools and the surviving route

Three nearby pieces of literature look genuinely relevant, but none currently closes the source target.

1. **Glebov--Krivelevich (2013):** at the Hamiltonicity threshold the random graph already has exponentially many Hamilton cycles. This shows that severe copy-count dependence can be overcome for the one-cycle type, but it does not give prescribed long cycle structures.

2. **Modern hypergraph nibble bounds:** Gould--Kelly (arXiv:2511.11375, 2025) sharpen Vu's quantitative nearly-perfect matching theory using the full codegree sequence. For a `C_ell`-factor, the natural hypergraph has original graph vertices as vertices and graph `ell`-cycles as hyperedges. At the source scale its expected degree is polynomial (`n^{epsilon+o(1)}` for the equal-short stress family), while edge-conditioned pair codegrees are smaller by roughly a `log n` factor. This makes a growing-uniformity nibble worth testing. But a near-perfect matching alone does not give a factor; an exact absorber/perfect-completion mechanism remains indispensable.

3. **Entropy for cycle factors in regular graphs:** Christoph--Draganić--Girão--Hurley--Michel--Müyesser (2025) show that a random cycle factor in any directed `d`-regular graph has `O(n log d/d)` cycles on average. At `d~log n` this is the same *number-of-cycles scale* `n loglog n/log n` as H0022, but it does not prescribe the individual cycle lengths and therefore is not a substitute for the conjecture.

The strongest next route is therefore:

> condition on a common typical host event (or an appropriate degree/edge-count exposure), then prove a **uniform fixed-cycle-type lower tail** by switchings or a truncated moment / hypergraph-matching argument; only after that union over the `exp(O(sqrt n))` cycle structures.

A useful first test is the equal-short type, because Lemma 2 proves it is first-moment extremal. If a conditional argument cannot handle that family, it cannot prove H0022.

The next nonrepeating Section-B triple is:

- **#9 RANDOMIZE:** randomize over copies of one fixed extremal type inside a typical host rather than over stronger endpoint-permutation systems;
- **#11 DUALIZE:** formulate the fixed-type completion obstruction as a fractional/perfect-matching or switching-flow dual problem after conditioning away common degree failures;
- **#25 COUNT THE SAME THING TWICE:** double-count factor/switching pairs to seek a uniform conditional lower tail and to identify the precise overlap clusters that survive degree conditioning.

No checker is manufactured in this run. The new claims are all-integer/all-`n` analytic statements with full proofs on the page; there is no finite computational claim whose certification would justify spending the run on an artifact.

## 8. H0022 status and stuck accounting

This is the **first** substantive H0022 run after admission.

Metric before: `A_cyc(1+epsilon)=UNMEASURED`.

Metric after: `A_cyc(1+epsilon)=UNMEASURED`.

Supported H0022 substantive unchanged count:

`0 -> 1`.

No stuck recovery is triggered. The next run should test the conditional fixed-type route rather than write another lemma about the same raw first moment.

## 9. Beck--Fiala stale-title refresh

The stale native title is still not an appropriate R16 research target, but its requested comparison was refreshed.

- Bansal--Jiang, arXiv:2508.03961v2, proves the conjectured `O(sqrt(t))` order for `t >= log^2 n`, while below that regime its bound has additional logarithmic losses. Thus their theorem alone does **not** supply one uniform all-`t,n` Beck--Fiala bound.
- Guo--Fang--Lu, arXiv:2609.11189v1, submitted 10 September 2026, explicitly claims the stronger real Komlós theorem with constant `3 sqrt(2 pi)` and deduces

\[
\operatorname{disc}(A)<3\sqrt{2\pi t}
\]

for every integer `t>=1`, with no restriction on `n`.
- Karingula--Lovett, ECCC TR26-188, posted 17 September 2026, gives a separately authored elementary simplification of that Komlós proof with constant `36`, which independently yields a complete uniform `36 sqrt(t)` Beck--Fiala consequence.

These last two items are extremely recent preprint/technical-report results rather than mature refereed consensus, so this report distinguishes **current stronger resolution claims** from settled publication history. They nevertheless make it inappropriate for R16 to abandon its valid H0022 successor and restart the stale 1981 title.

## 10. Model/scheduler control status

The model-control limitation remains unchanged in the exposed task-control surface. The available controls are prompt/title, schedule or relative start, timing mode, enabled state, and task identity; there is no binding model-family field, no reasoning-effort field, and no authenticated applied-model receipt. Thus GPT-6/maximum remains a request in prompt text only. Enforcing it would require an authorized product/workspace scheduler or API exposing those selectors plus runtime telemetry.

The historical P26 `You cannot modify this task` event is not a current universal failure: root `RESULTS.md` records that a later update succeeded from an authorized P/C context. For any task that still returns such an error, the compliant workaround is the owning workspace/account context or platform support, never duplication or permission bypass.

No scheduler state, shared root ledger, peer research file, email, Drive content, public post, purchase, permission, or workflow was changed in this run.

## 11. Structured ledger delta (own immutable report only)

```yaml
ledger_delta:
  track: R16
  allocation: HARD_OUTSIDE
  active_target: H0022
  source: "Cohen Antonir--Lichev--Zhukovskii, arXiv:2608.06358v1, Conjecture 1.5"
  source_status: OPEN
  metric_name: A_cyc(c)
  metric_scope: "smallest proved fixed girth coefficient A for universality at p=c log n/n, all restrictions retained"
  metric_before_at_c_1_plus_epsilon: UNMEASURED
  metric_after_at_c_1_plus_epsilon: UNMEASURED
  metric_movement: false
  supported_substantive_unchanged_before: 0
  supported_substantive_unchanged_after: 1
  recovery_count_on_H0022: 0
  methods_used: [2, 18, 24]
  new_results:
    - "Exact labeled-copy/expectation formula for every cycle-length partition."
    - "Explicit equal-short-cycle first-moment transition k_FM(c,n)=(log(2n)-1)/(log(c log n)-1)."
    - "Uniform first-moment lower envelope over all girth>=ell cycle-factor types; equal C_ell factors attain it on divisibility subsequences."
    - "At source parameters every admissible type has log expectation at least (epsilon/(1+epsilon)+o(1)) n loglog n."
    - "Common-host obstruction: every fixed-type failure probability is at least polynomial because an isolated fixed vertex kills every factor."
    - "Exact unconditioned second-moment obstruction: EX^2/(EX)^2 >= p^{-2n/(n-1)}."
  next_methods: [9, 11, 25]
  next_obligation: "Condition on one common typical-host exposure and obtain a uniform fixed-type lower tail strong enough to union over exp(O(sqrt n)) cycle structures; begin with the equal-short first-moment extremal type."
  closure: false
```
