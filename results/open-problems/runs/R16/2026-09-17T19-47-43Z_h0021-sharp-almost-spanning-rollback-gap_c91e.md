Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested in prompt text, but this runtime exposes no authenticated model-family selector, reasoning-effort selector, or applied-effort telemetry, so GPT-6/maximum is not claimed. **NO METRIC MOVEMENT:** H0021 `Delta_near: 2 -> 2`; supported H0021 unchanged count `1 -> 2`. Methods actually tried: **#3 PROVE SOMETHING STRONGER, #11 DUALIZE, #24 FIND THE EXTREMAL OBJECT**.

# R16 HARD OUTSIDE — H0021: sharp-density almost-spanning universality and the exact rollback-capacity gap

Date: 2026-09-17 UTC. Repository/branch: `yspennstate/math-open-problems` / `master`.

Active source: H0021 = Asaf Cohen Antonir, Lyuben Lichev, Maksim Zhukovskii, *Universality in random graphs via optimal linking systems: trees and beyond*, arXiv:2608.06358v1 (6 August 2026), Conjecture 1.4.

Source status after this run: **OPEN / PARTIAL / ACTIVE HARD OUTSIDE**. The source conjecture is not solved here. The frozen metric remains `Delta_near=2`.

## 1. Continuity, ownership, exclusions, and current source check

I continued from the newest complete R16 report

`runs/R16/2026-09-17T18-47-04Z_h0021-subcubic-core-entropy-route_a7c4.md`

rather than restarting the stale native Beck--Fiala title or reopening the handed-off I0036 SAW target.

Before doing mathematics I recovered/read the required campaign surfaces: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, the canonical R16 claim `operations/claims/H0021.md`, the newest R16 report, and the neighboring H0023 linking-system reports. In particular, P20's H0023 run ended after six unchanged substantive runs with the source still OPEN/PARTIAL; its final diagnosis is a fixed-permutation path-certificate hypergraph whose mean incidence operator has only the forced balance kernel, but whose quenched local clustering and perfect-completion problem remain unresolved. H0023 is therefore a baseline/neighbor, not a solved black box I can import.

A fresh 2026-09-17 search of the exact H0021 title, authors, arXiv id and Conjecture 1.4 recovered only arXiv:2608.06358v1 and no later source-matching proof. The source still states:

\[
G\!\left(n,(1+\varepsilon)\frac{\ln n}{n}\right)
\quad\text{should whp be }\mathcal T_{n,\Delta}\text{-universal}
\]

for every fixed `epsilon>0` and integer `Delta>=2`. The paper proves the conclusion at `C ln n/n` for a sufficiently large absolute `C`; its current `psi=1` linking-system proof allows `C<2000`, not `1+epsilon`.

The stale Beck--Fiala comparison was also refreshed. Bansal--Jiang arXiv:2508.03961v2 gives the conjectured square-root order for `t>=log^2 n` and a weaker bound below that regime. Guo--Fang--Lu arXiv:2609.11189v1 (10 September 2026) explicitly claims the full real Komlos bound `3 sqrt(2 pi)` and hence `disc(A)<3 sqrt(2 pi t)` for every integer `t>=1`, with no `n` restriction. I retain the operational label **fresh primary-preprint full-resolution claim; not mature refereed consensus**, so the stale Beck--Fiala title is not used to restart old R16 work.

## 2. Frozen metric

`Delta_near` is the largest integer `D>=2` for which R16 has a complete source-matching proof that, for every fixed `epsilon>0`, whp

\[
G\!\left(n,(1+\varepsilon)\frac{\ln n}{n}\right)
\]

contains every `n`-vertex tree of maximum degree at most `D`.

Before this run: `Delta_near=2`.

After this run:

\[
\boxed{\Delta_{\rm near}=2.}
\]

The result below is an almost-spanning theorem and therefore does **not** move the fixed source metric. It does, however, reduce the missing part of the source conjecture to a quantitatively explicit `Theta(n loglog n/log n)` absorption window.

## 3. #3 PROVE SOMETHING STRONGER — a complete sharp-density almost-spanning theorem for every fixed maximum degree

The previous run focused on `Delta=3`. The stronger statement below works for every fixed `Delta>=3` and uses the source's constant-degree rollback lemma rather than its large-`d` rollback proposition.

### Theorem R16-H0021-ASP

Fix constants `c>1` and an integer `Delta>=3`, and set

\[
p=c\frac{\ln n}{n},
\qquad
 t=\left\lceil\frac{2\ln\ln n}{p}\right\rceil.
\tag{3.1}
\]

Then with high probability `G~G(n,p)` simultaneously contains **every** tree `T` of maximum degree at most `Delta` and order

\[
|V(T)|\le n-(4\Delta+3)t-1.
\tag{3.2}
\]

Equivalently, since

\[
t=\left(\frac{2}{c}+o(1)\right)
\frac{n\ln\ln n}{\ln n},
\]

whp `G(n,c ln n/n)` is universal for all fixed-`Delta` trees of order at most

\[
\boxed{
 n-\left(\frac{8\Delta+6}{c}+o(1)\right)
 \frac{n\ln\ln n}{\ln n}.
}
\tag{3.3}
\]

For the first unresolved source case `Delta=3`, this becomes

\[
\boxed{
 n-\left(\frac{30}{c}+o(1)\right)
 \frac{n\ln\ln n}{\ln n}.
}
\tag{3.4}
\]

I do **not** claim literature novelty for this corollary. It is obtained by combining elementary sharp-density random-graph expansion with Lemma 6.15 of the source (itself quoted there from Montgomery). The point for R16 is that it is a complete theorem on the page and changes the remaining research obligation from an `n`-vertex embedding problem into an explicit `O(n loglog n/log n)` completion problem.

### Proof

Write `L=ln n` and `ell=ln ln n`. We prove a host event depending only on `G`, then invoke the deterministic Lemma 6.15 for every target tree simultaneously.

#### Step 1: `G` is `t`-joined whp

The source's equation (17) gives, for any `t`,

\[
\Pr(G\text{ is not }t\text{-joined})
\le
\exp\!\left(t\left(2\ln\frac{en}{t}-pt\right)\right).
\tag{3.5}
\]

For (3.1),

\[
pt=2\ell+o(1),
\]

while

\[
\ln\frac{en}{t}
=\ell-\ln\ell+O(1).
\]

Hence

\[
2\ln\frac{en}{t}-pt
=-2\ln\ell+O(1)\to-\infty.
\]

As `t->infinity`, the right side of (3.5) is `o(1)`. Thus `G` is `t`-joined whp.

#### Step 2: constant-factor expansion of every set of size at most `2t`

We claim that whp

\[
|N_G(X)|\ge 2\Delta |X|
\qquad\forall X\subseteq[n],\quad 1\le |X|\le2t.
\tag{3.6}
\]

Here `N_G(X)` denotes the external vertex-neighborhood of `X`.

Fix `X` with `|X|=s`. Then

\[
Y_X:=|N_G(X)|\sim
\operatorname{Bin}(n-s,q_s),
\qquad
q_s=1-(1-p)^s.
\]

We split the range of `s`.

**Range I: `1<=s<=n/L^2`.** Uniformly in this range `ps=o(1)`, so

\[
q_s=(1+o(1))ps,
\qquad
\mu_s:=\mathbb EY_X=(c+o(1))sL.
\]

Since `Delta` is fixed, `2Delta s/mu_s=O(1/L)`. The standard binomial lower-tail estimate in the regime `r/mu->0` gives

\[
\Pr(Y_X<2\Delta s)
\le
\exp\big(-(c-o(1))sL+O(s\ell)\big).
\tag{3.7}
\]

There are at most `(en/s)^s` choices of `X`. Therefore the total probability of a bad set in Range I is at most

\[
\sum_{s\le n/L^2}
\exp\big(-(c-1-o(1))sL\big)=o(1),
\tag{3.8}
\]

because `c>1` is fixed.

**Range II: `n/L^2<=s<=1/p`.** Here `ps<=1`, and

\[
q_s\ge1-e^{-ps}\ge \frac{ps}{2}.
\]

For large `n`, `n-s>=n/2`, so

\[
\mu_s\ge \frac{nps}{4}=\frac{c}{4}sL.
\]

Thus `2Delta s<=mu_s/2` for large `n`, and Chernoff gives

\[
\Pr(Y_X<2\Delta s)
\le e^{-\mu_s/8}
\le \exp(-c sL/32).
\]

But now

\[
\ln(en/s)\le 1+2\ell=o(L),
\]

so summing over all `X` in Range II is again `o(1)`.

**Range III: `1/p<=s<=2t`.** Now `ps>=1`, hence

\[
q_s\ge1-e^{-1}>1/2.
\]

Since `t=o(n)`, for all such `s` and large `n`,

\[
\mu_s\ge n/3,
\qquad
2\Delta s=o(n)\le\mu_s/2.
\]

Therefore

\[
\Pr(Y_X<2\Delta s)\le e^{-n/24}.
\]

The total number of sets of size at most `2t` is

\[
\exp\big(O(t\ln(n/t))\big)
=\exp\left(O\left(\frac{n(\ln\ln n)^2}{\ln n}\right)\right)
=e^{o(n)},
\]

so the Range III union bound is `o(1)`. This proves (3.6).

#### Step 3: a singleton is `(2Delta,t)`-extendable

Fix any host vertex `w` and let `R` be the graph with vertex set `{w}` and no edges. For every nonempty `X` with `|X|<=2t`, (3.6) gives

\[
|N_G(X)\setminus V(R)|
\ge 2\Delta |X|-1.
\tag{3.9}
\]

If `w notin X`, the right side of the `(2Delta,t)`-extendability inequality is `(2Delta-1)|X|`, and (3.9) is sufficient because `|X|>=1`. If `w in X`, the correction term in Definition 2.11 is

\[
-\big(|N_R(w)|-1\big)=1,
\]

so the required right side is `(2Delta-1)|X|+1`, while the external neighborhood already excludes `w` and (3.6) gives `2Delta|X|`, again sufficient. Hence `{w}` is `(2Delta,t)`-extendable in `G`.

#### Step 4: invoke the deterministic constant-degree rollback lemma

Lemma 6.15 of the source states: if `G` is `t`-joined, `R` is `(2Delta,t)`-extendable with maximum degree at most `Delta`, and

\[
|V(R)|+|V(T)|\le |V(G)|-4\Delta t-3t,
\]

then any rooted tree `T` of maximum degree at most `Delta` can be embedded rooted at any chosen `w in V(R)`, while preserving `(2Delta,t)`-extendability.

Take `R={w}`. Conditions (3.5)--(3.9) hold on one host event independent of `T`. Thus every rooted tree with

\[
|V(T)|\le n-(4\Delta+3)t-1
\]

embeds. Since the same deterministic host event works for every target tree and every root choice, this is simultaneous universality over the whole family. This proves (3.2), and (3.3)--(3.4) follow from (3.1). `QED`.

## 4. #11 DUALIZE — where the existing rollback architecture necessarily loses the sharp coefficient

The theorem above also isolates an exact scale collision in the source's *other* rollback tool, Proposition 2.13.

That proposition requires

\[
d\ge\frac{\ln n}{\ln\ln n}
\tag{4.1}
\]

and reserves a margin

\[
10dt+\ln n.
\tag{4.2}
\]

Suppose one tries to run the same `t`-joined union-bound engine as source equation (17) at

\[
p=c\frac{\ln n}{n}
\]

and writes

\[
t=a\frac{\ln\ln n}{p}
\tag{4.3}
\]

for a constant `a`. Then

\[
2\ln(en/t)-pt
=(2-a)\ln\ln n-2\ln\ln\ln n+O(1).
\tag{4.4}
\]

Thus this particular certification route cannot take any fixed `a<2`; asymptotically it needs `a>=2-o(1)`. Combining (4.1)--(4.3), its reserved fraction obeys

\[
\frac{10dt}{n}
\ge
\frac{10a}{c}+o(1)
\ge
\frac{20}{c}-o(1).
\tag{4.5}
\]

Therefore, **within Proposition 2.13 plus the source's equation-(17) `t`-joined certificate, no amount of constant tuning can reach any density coefficient `c<20` for an `n-o(n)` tree**: the mandated rollback reserve already exceeds the entire vertex set. This is a proof-architecture obstruction, not a lower bound on H0021 and not a claim that `t`-joinedness itself requires `c>=20`.

The source's actual parameters are even more expensive: it takes `t=4 ln ln n/p1`, applies Proposition 2.13 in independent subgraphs, and its extendability union bound is stated for `C>=4000`; it explicitly enforces inequalities such as `10dt<=n/400` only by taking `C` large.

The key contrast is Lemma 6.15. It needs only constant extendability parameter `2Delta` and reserves

\[
(4\Delta+3)t
=O\left(\frac{n\ln\ln n}{\ln n}\right)=o(n),
\]

which is exactly why Section 3 closes at sharp `c>1` for almost-spanning trees. In dual language: **small-set expansion is not the sharp-density bottleneck; the bottleneck is the final capacity/completion step once the rollback slack has shrunk to `Theta(n loglog n/log n)`.**

There is a second, independent warning against direct constant-optimisation of the source proof. If `G(n,p)` is split into an independent layer with edge-probability `theta p` and `theta c<1`, that layer has isolated vertices whp (its expected isolated-vertex count is `n^{1-theta c+o(1)}`). Such a layer cannot satisfy even singleton constant-factor extendability. Hence at `c=1+epsilon`, any proof that needs several independent constant-fraction layers each with global extendability must be reorganised: one main layer must retain essentially the whole connectivity-threshold mass, or edges must be recycled/deferred rather than permanently split.

## 5. #24 FIND THE EXTREMAL OBJECT — the remaining problem is now an absorption problem on exactly the hard structural scale

The preceding R16 run constructed the uniformly subdivided cubic-core family. For natural path scale

\[
k\asymp\frac{\ln n}{\ln\ln n},
\]

those trees have

\[
L\sim\frac{n}{2k}
=\Theta\left(\frac{n\ln\ln n}{\ln n}\right)
\]

leaves and no bare `k`-path. That is exactly the structural middle regime identified by the source.

Theorem R16-H0021-ASP now shows that at the conjectured sharp density, for `Delta=3` every such tree can be embedded except for at most

\[
q=(15+o(1))t
=\left(\frac{30}{c}+o(1)\right)
\frac{n\ln\ln n}{\ln n}
\tag{5.1}
\]

vertices. Thus the remaining scale `q` is not an artefact: it is the same order as the number of leaves/branch vertices in the exact uniformly subdivided cubic-core obstruction.

This gives a sharper target than the previous full-tree conditional-tail idea.

### Absorption target A3

For `p=(1+epsilon)ln n/n` and

\[
t=(2+o(1))\frac{\ln\ln n}{p},
\]

prove a common high-probability host property which has the following deterministic consequence:

> every `(6,t)`-extendable embedding of a connected subcubic subtree `T0 subset T` with `|V(T)\setminus V(T0)|<=15t+1` can be completed to a spanning embedding of `T`.

A3 plus the theorem above would imply `Delta_near>=3` and therefore move the frozen metric.

The important point is that A3 is **strictly weaker** than H0023's all-permutations spanning linking-system conjecture. It asks only for completion of a tree-structured deficit attached to an already embedded extendable core. The H0023 path-hypergraph work says not to expect a naive perfect matching/nibble to finish automatically: quenched local clustering and perfect completion are real barriers. But the tree structure of the deficit gives information absent from the arbitrary-permutation problem, and it is now the information R16 should exploit.

A fresh fixed-parent/fixed-reservoir final matching is still impossible at this scale, as proved in the preceding R16 run: for reservoir size `q=Theta(n loglog n/log n)`, one has `pq=Theta(loglog n) << log q`, so a fresh `G(q,q,p)` contains many isolated reserved vertices. Therefore A3 must choose attachment images adaptively, use augmenting paths/switches, or reuse the extendability of the already embedded core; it cannot be a one-shot matching on two predetermined `q`-sets.

## 6. Prior art and novelty qualification

The theorem in Section 3 deliberately reuses a published deterministic lemma (source Lemma 6.15, quoted there from Montgomery). The random-graph part is an elementary union-bound/large-deviation argument. I therefore make **no novelty claim** for the almost-spanning statement without a broader literature search.

A bounded search recovered the older nearly/almost-spanning universality literature (Friedman--Pippenger; Haxell; Alon--Krivelevich--Sudakov; Balogh--Csaba--Pei--Samotij; Conlon--Ferber--Nenadov--Skoric) and the sharp fixed-tree results of Hefetz--Krivelevich--Szabo, but did not recover an exact statement matching (3.3) at `p=c ln n/n` with deficit `O(n ln ln n/ln n)` simultaneously for every fixed-degree tree. This is bounded negative evidence only.

For R16, the durable contribution of this run is therefore not an asserted new paper theorem but the **quantitative reduction**:

\[
\text{H0021 at }\Delta=3
\quad\Longleftarrow\quad
\text{complete only an }O(n\ln\ln n/\ln n)\text{-vertex tree deficit},
\]

together with the exact explanation that the large-`d` rollback route loses the sharp coefficient through `10dt`, while the constant-`d` rollback route survives.

## 7. Verification policy

No finite computational claim was needed in this run, so no checker was manufactured merely for bookkeeping. The theorem-sized claims are proved on the page. The only externally imported mathematical statement used in the proof is the deterministic Lemma 6.15 exactly as stated in arXiv:2608.06358v1 (where it is attributed to Montgomery [70, Corollary 3.7]). The `t`-joined bound is the source's displayed equation (17), and the remaining random-graph expansion proof is written above.

## 8. Outcome, stuck state, and next genuinely different methods

Metric outcome:

`Delta_near: 2 -> 2` — **no movement**.

Supported H0021 unchanged count:

`1 -> 2`.

This is not yet a stuck run under the three-unchanged rule.

What changed mathematically:

- a complete sharp-density, almost-spanning universality theorem now holds for **every fixed Delta**, not only subcubic trees;
- for `Delta=3` the missing vertex budget is explicit: `(30/(1+epsilon)+o(1)) n loglog n/log n`;
- the source's large-`d` rollback architecture has an internal coefficient floor `c>=20` when paired with its equation-(17) `t`-joined certificate, so constant optimisation of Proposition 2.13 cannot reach the conjectured `1+epsilon` regime;
- the source's constant-`d` Lemma 6.15 does survive at sharp density, proving expansion itself is not the obstruction;
- the unresolved task is now a final `Theta(n loglog n/log n)` tree-structured absorption/completion problem, weaker than an all-permutations linking system.

The next H0021 triple must not repeat `#3,#11,#24`. I record:

- **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT:** introduce an explicit residual fraction/routing-depth parameter and optimise the completion window rather than the full proof constant;
- **#13 FIND WHAT ONLY INCREASES:** search for a deficit/augmenting-path potential that guarantees an adaptive completion procedure terminates while preserving extendability;
- **#21 ASK WHO ELSE HAS THIS SHAPE:** compare the residual completion problem with online bipartite matching, cuckoo-hashing/augmenting-path arguments, and tree-indexed absorption, rather than with arbitrary-permutation linking systems.

If the fixed metric is unchanged once more, the supported H0021 streak reaches three and the next invocation must execute `STUCK_RECOVERY_1 / thinking-only` rather than manufacture another incremental lemma.

## 9. Model and scheduler-control status

The scheduler-control situation remains the same as the controlling repository ledger: the exposed task interface can carry prompt/title/schedule/timing/enabled state but exposes no authenticated model-family selector or reasoning-effort selector. GPT-6/maximum is therefore prompt-only in this run. Actual enforcement would require a product/workspace scheduler/API which exposes those selectors and authenticated runtime telemetry.

The historical P26 `You cannot modify this task` event is not a current mathematical blocker: the repository records a later successful P26 update from an authorized P/C context, while a different context denied R-series edits. The compliant workaround for any still-denied task is its owning workspace/context or platform support, not permission bypass or duplicate scheduling. No scheduler state was changed in this run.

## 10. Structured ledger_delta (own immutable report only)

```yaml
ledger_delta:
  track: R16
  active_target: H0021
  source: "Cohen Antonir--Lichev--Zhukovskii, arXiv:2608.06358v1, Conjecture 1.4"
  source_status: OPEN
  research_status: PARTIAL_ACTIVE_HARD_OUTSIDE
  metric: Delta_near
  before: 2
  after: 2
  movement: false
  supported_unchanged_before: 1
  supported_unchanged_after: 2
  methods: [3, 11, 24]
  new_complete_result: "Sharp-density almost-spanning universality: for fixed c>1, Delta>=3, all Delta-bounded trees of order <= n-(4Delta+3)t-1 with t=ceil(2 loglog n/p), p=c log n/n"
  subcubic_deficit: "(30/c+o(1)) n loglog n/log n"
  architecture_obstruction: "Proposition 2.13 + equation-(17) t-joined certificate forces normalized 10dt reserve >=20/c-o(1)"
  remaining_obligation: "tree-structured completion/absorption of O(n loglog n/log n) vertices from a (6,t)-extendable core"
  next_methods: [5, 13, 21]
  next_stuck_trigger_if_no_movement: STUCK_RECOVERY_1
  shared_roots_modified: false
  peer_files_modified: false
  scheduler_modified: false
  email_or_drive: false
```
