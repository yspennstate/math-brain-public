Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED**; this was not GPT-6 at maximum and I do not claim otherwise. **NO MOVEMENT: frozen metric `A_forest = 4/3 -> 4/3`; fourth consecutive unchanged run after the source-threshold improvement. STUCK RECOVERY 1 continues with the already selected recovery `PORT THE TECHNIQUE FROM THE NEAREST SOLVED ANALOGUE`. Methods actually tried: B18, B21, B22.**

**Problem/source:** Giacomo Aletti, Andrea Collevecchio, Irene Crimaldi, Maria Deijfen, Steffen Dereich, Andrea Ghiglietti, Remco van der Hofstad, Mark Holmes, Daniel Kious, Victor Kleptsyn, Bas Lodewijks, Peter Mörters, Bruno Schapira (2025), *Open Problems in Stochastic Reinforcement Models*, Open Problem 12 (`P0082`): improve the finite-graph WARM forest threshold `alpha > 2`.  
**Track/root:** P13 / `proofnet24/P13-outside-successor`.  
**Exclusive claim:** `operations/claims/P0082.md`, native slot `6aa7b253b37c8191b693d8dc79298d37`.  
**Category:** CLOSABLE OUTSIDE.  
**Status:** source strict-threshold answer mathematically PROVED at `A_forest=4/3`, but **NOT CLOSURE-CERTIFIED**; the auxiliary critical-endpoint question below remains outside the source metric.

# 1. Continuity and state recovered before research

The retired P13 I0051/Aldous--Janson clade-covariance project was not reopened. Before new mathematics I reread the controlling owner directive at anchor commit `749da260517828ed311f6f1b1af74915c054bdf3`, `operations/NEW_METHODS_2026-09-16.md`, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the canonical `P0082` claim, all four earlier P13 successor reports, the current P14 neighbour report, and the P0082 intake/attempt history. Repository search again found no P26 end-to-end P0082 audit and no distinct research-track end-to-end P0082 audit. The compact shared `RESULTS.md` still contains older native-slot descriptions; this attacking worker did not edit it.

The source strict theorem already proved by P13 is unchanged:

> For every finite graph, every allowed positive firing-rate vector, and every `alpha > 4/3`, every not-linearly-unstable WARM equilibrium has forest support. Combined with the source's finite-graph convergence/non-convergence-to-linearly-unstable input, every surviving connected component is a tree.

The source itself gives the matching lower obstruction: on the uniform triangle the all-three-edge regime persists below `4/3`, while an edge dies for `alpha>4/3`. Hence the frozen strict universal threshold is already saturated:

\[
A_{\rm forest}=\frac43.
\]

No auxiliary endpoint result is counted as movement of this metric.

The newest prior P13 report (`2026-09-17T21-04-57Z__stuck-recovery-01.md`) was the required first stuck-recovery report. It selected **PORT THE TECHNIQUE** and reduced the strongest optional endpoint question to a zero-derivative stochastic-approximation problem on the uniform triangle:

\[
\mathbb P_{K_3,\,p\equiv1,\,\alpha=4/3}
\left(X_n\to x_*\right)\stackrel{?}=0,
\qquad x_*=(1/3,1/3,1/3).
\tag{1.1}
\]

That endpoint is not required to answer Open Problem 12 as stated. It is being used only to stress-test sharpness and the closure package. The previous report obtained the local monkey-saddle normal form and predicted that a convergent ODE-like path should have radial size of order `1/log n` and a transversely expanding multiplier of order `(log n)^2`. The present run ports Wei's 1993 martingale-transform mechanism far enough to eliminate the need to assume that precise rate.

# 2. Fresh source and literature check -- 17 September 2026 UTC

The source PDF was read directly again. Its finite-WARM paragraph says that `X(t)` converges to an equilibrium which cannot be linearly unstable; cites the known `alpha>2` forest theorem; states **Open Problem 12: improve the lower bound `alpha>2` for which every connected component is a tree**; then records the uniform-triangle transition at `4/3` and says perhaps `alpha>4/3` is sharp. The source is the 2025 MATRIX Annals chapter, DOI `10.1007/978-3-031-76738-8_29`.

The bounded current search used, among others, the queries

- `"Open Problems in Stochastic Reinforcement Models" "Open Problem 12" WARM reinforcement forest alpha 4/3`,
- `"alpha > 4/3" WARM forest`,
- `"Strongly reinforced Polya urns with graph-based competition" 4/3 WARM 2026`,
- `"Proof of the WARM whisker conjecture" forest 4/3 reinforcement 2026`,
- `"Martingale transforms with non-atomic limits and stochastic approximation" Wei`,
- `"Some Pathological Traps for Stochastic Approximation" singular equilibria Brandière`.

The search recovered the 2016 triangle/stability paper of van der Hofstad--Holmes--Kuznetsov--Ruszel, the Holmes--Kleptsyn 2017 `alpha>2` / `alpha>25` finite-WARM theorem, the later infinite-WARM papers, the 2025 source, Wei's 1993 martingale-transform paper, and Brandière's 1998 singular/pathological-trap paper. No later primary paper claiming the universal finite-WARM `4/3` forest theorem or a resolution of Open Problem 12 was found. This is **bounded negative evidence only**, not proof of global openness or novelty.

Two literature points materially affect this run.

1. C. Z. Wei, *Martingale transforms with non-atomic limits and stochastic approximation*, PTRF 95 (1993), Theorem 3.1: for a predictable martingale transform whose noise satisfies the local Marcinkiewicz--Zygmund condition, the limiting transform is non-atomic when the tail quadratic mass of its predictable coefficients is comparable to a positive predictable scale. Wei's Section 2 also constructs counterexamples showing that arbitrary predictable coefficients can create atoms/degenerate limits even under apparently rich noise. Therefore coefficient regularity must be proved, not assumed.
2. Wei's Theorem 4.2 proves a `log n` scale in a one-dimensional Robbins--Monro problem when the regression derivative vanishes and the leading restoring drift is quadratic. This is the nearest solved quantitative analogue to one incoming ray of the WARM critical triangle. Brandière 1998 explicitly treats singular equilibria and other pathological traps, but the accessible publisher material this run exposed the abstract/introduction rather than the complete theorem hypotheses. I therefore do **not** claim that a Brandière theorem applies to (1.1).

# 3. B18 -- say the endpoint in another language: an exact transverse martingale transform

The useful change of language is from the two-dimensional nonlinear stochastic approximation to an **exact one-dimensional predictable martingale transform for each pair difference**.

Consider the uniform triangle at `alpha=4/3`. Label the three normalized edge weights `x_1,x_2,x_3`, with `x_1+x_2+x_3=1`, and put

\[
a=x_1^\alpha,\qquad b=x_2^\alpha,\qquad c=x_3^\alpha.
\]

If `pi_i(x)` is the conditional probability that the next reinforcement is put on edge `i`, then

\[
\pi_2(x)
=\frac13\left(\frac{b}{a+b}+\frac{b}{b+c}\right),
\qquad
\pi_3(x)
=\frac13\left(\frac{c}{a+c}+\frac{c}{b+c}\right).
\]

Subtracting gives the **exact factorization**

\[
\boxed{
\pi_2-\pi_3
=\frac{b-c}{3}
\left[
\frac{a}{(a+b)(a+c)}+\frac1{b+c}
\right].
}
\tag{3.1}
\]

Thus `pi_2-pi_3` is divisible by `d:=x_2-x_3` even away from the symmetry line. Define the continuous function

\[
G_{23}(x)
:=\frac{1}{3}
\frac{x_2^\alpha-x_3^\alpha}{x_2-x_3}
\left[
\frac{x_1^\alpha}
{(x_1^\alpha+x_2^\alpha)(x_1^\alpha+x_3^\alpha)}
+\frac1{x_2^\alpha+x_3^\alpha}
\right],
\tag{3.2}
\]

where the divided difference is extended continuously at `x_2=x_3`, and set

\[
\lambda_{23}(x):=G_{23}(x)-1.
\tag{3.3}
\]

At `x_*`, `G_{23}(x_*)=3\alpha/4=1`, hence `lambda_{23}(x_*)=0` exactly at `alpha=4/3`.

Let the total initial edge mass be `T_0`, so the stochastic-approximation step is

\[
\gamma_{n+1}=\frac{1}{T_0+n+1}.
\]

Let `J_{n+1}` be the edge reinforced at step `n+1` and define

\[
\varepsilon_{n+1}^{23}
:=
\mathbf 1_{\{J_{n+1}=2\}}
-\mathbf 1_{\{J_{n+1}=3\}}
-(\pi_2(X_n)-\pi_3(X_n)).
\tag{3.4}
\]

Then `E[epsilon_{n+1}^{23}|F_n]=0` and, using (3.1), the pair difference obeys the **exact**, remainder-free recursion

\[
\boxed{
 d_{n+1}^{23}
=\bigl(1+\gamma_{n+1}\lambda_{23}(X_n)\bigr)d_n^{23}
+\gamma_{n+1}\varepsilon_{n+1}^{23}.
}
\tag{3.5}
\]

This is stronger than the previous normal-form heuristic because there is no untracked nonlinear transverse remainder.

Fix `N` and define the predictable multiplier

\[
P_N^{23}=1,
\qquad
P_{n+1}^{23}=P_n^{23}
\bigl(1+\gamma_{n+1}\lambda_{23}(X_n)\bigr).
\tag{3.6}
\]

As long as the factors are positive, division of (3.5) by (3.6) gives

\[
\boxed{
M_{n+1}^{23}=M_n^{23}
+q_{n+1}^{23}\varepsilon_{n+1}^{23},
\qquad
M_n^{23}:=\frac{d_n^{23}}{P_n^{23}},
\quad
q_{n+1}^{23}:=\frac{\gamma_{n+1}}{P_{n+1}^{23}}.
}
\tag{3.7}
\]

Hence the transverse coordinate is exactly a predictable martingale transform. The same construction holds cyclically for pairs `31` and `12`.

Near `x_*`, the conditional noise is uniformly nondegenerate. Indeed

\[
\mathbb E[(\varepsilon_{n+1}^{23})^2\mid\mathcal F_n]
=\pi_2+\pi_3-(\pi_2-\pi_3)^2
\longrightarrow \frac23,
\tag{3.8}
\]

and `E[|epsilon_{n+1}^{23}||F_n] -> 2/3`. Thus, in a sufficiently small fixed neighbourhood `U` of `x_*`, the original WARM noise satisfies the local M--Z bounds needed by Wei.

**B18 outcome:** worked. The optional endpoint has an exact one-dimensional martingale-transform coordinate for each pair; the earlier worry about controlling a nonlinear transverse remainder disappears completely.

# 4. B21 -- port Wei's non-atomicity theorem: tail-square comparability is automatic after localization

The previous report expected that one would first have to prove the precise asymptotic `P_n ~ (log n)^2`. That is unnecessarily strong. Wei's theorem only needs regular tail quadratic mass, and that follows from the fact that `lambda(x_*)=0`.

## Lemma 4.1 (slow multiplier implies Wei tail comparability)

Fix a pair, suppress the pair superscript, and choose a neighbourhood `U` so small that

\[
|\lambda(x)|\le \eta
\quad(x\in U),
\qquad 0<\eta<1/10.
\tag{4.1}
\]

Let `P` satisfy (3.6) while the process is in `U`; after the first exit, freeze the multiplier (`lambda=0`). Then for all sufficiently large `m>=n`,

\[
C^{-1}\left(\frac mn\right)^{-2\eta}
\le \frac{P_m}{P_n}
\le C\left(\frac mn\right)^{2\eta}
\tag{4.2}
\]

for a deterministic `C`, and therefore

\[
\boxed{
 c\,\frac1{nP_n^2}
\le
\sum_{j=n}^{\infty}\frac{\gamma_{j+1}^2}{P_{j+1}^2}
\le
 C\,\frac1{nP_n^2}.
}
\tag{4.3}
\]

### Proof

For large `k`, `|gamma_{k+1} lambda_k|<1/2`, so

\[
|\log(1+\gamma_{k+1}\lambda_k)|
\le 2\eta\gamma_{k+1}.
\]

Summing from `n` to `m-1` and using

\[
\sum_{k=n}^{m-1}\gamma_{k+1}
=\log(m/n)+O(1/n)
\]

gives (4.2), after changing a constant. Since `gamma_j` is comparable to `1/j`, (4.2) yields upper and lower bounds for each summand in (4.3) by constant multiples of

\[
\frac{1}{P_n^2j^2}\left(\frac jn\right)^{\pm4\eta}.
\]

Both comparison series have order `1/n` because `4 eta<1`. This proves (4.3). QED.

The predictable scale in Wei's Theorem 3.1 can therefore be taken as

\[
b_n^2=\frac1{nP_n^2}.
\tag{4.4}
\]

This is the key technical gain of the run: **no radial rate has to be known to verify Wei's coefficient hypothesis.**

## Proposition 4.2 (endpoint convergence forces collapse of every transverse multiplier)

For the uniform triangle at `alpha=4/3`, define the three multipliers `P_n^{12},P_n^{23},P_n^{31}` by (3.6) after any fixed sufficiently late starting time. Then, modulo a null set,

\[
\boxed{
X_n\to x_*
\quad\Longrightarrow\quad
P_n^{12}\to0,
\qquad P_n^{23}\to0,
\qquad P_n^{31}\to0.
}
\tag{4.5}
\]

### Proof

It is enough to prove the assertion for pair `23`; the other two follow by cyclic symmetry.

Choose `U` satisfying (4.1), small enough also that the conditional second moment of `epsilon^{23}` is bounded above and its conditional first absolute moment is bounded below by a positive constant. For an integer `N`, let `tau` be the first exit time from `U` after `N`.

To make the use of Wei completely legitimate rather than conditioning on a future event, enlarge the probability space by an independent Rademacher sequence. Define a localized process as follows:

- before `tau`, use the actual `lambda_{23}(X_n)` and actual WARM martingale difference `epsilon_{n+1}^{23}`;
- after `tau`, put `lambda=0` and replace the noise by the independent Rademacher difference.

The resulting coefficients `q_n=gamma_n/P_n` are predictable. Lemma 4.1 gives Wei's tail-square condition globally for the localized transform. The local M--Z condition holds before `tau` by the choice of `U` and after `tau` by the Rademacher replacement. Hence Wei's Theorem 3.1 implies that the localized martingale-transform limit has a continuous, in particular non-atomic, distribution.

On the event

\[
E_N:=\{X_n\in U\ \hbox{for every }n\ge N\}
\cap\{X_n\to x_*\},
\]

the localization never changes the original WARM recursion. Suppose additionally that `limsup P_n^{23}>0`. Then there are `rho>0` and an infinite subsequence `n_j` with `P_{n_j}^{23}>=rho`. Since `d_{n_j}^{23}->0`,

\[
M_{n_j}^{23}=d_{n_j}^{23}/P_{n_j}^{23}\to0.
\]

But the martingale transform converges, so its full limit must equal zero. The non-atomicity just proved gives

\[
\mathbb P(E_N\cap\{\limsup P_n^{23}>0\})=0.
\]

On `X_n->x_*`, some `E_N` occurs. Taking the countable union over `N` shows that, outside a null set, convergence to `x_*` forces `limsup P_n^{23}=0`, hence `P_n^{23}->0`. QED.

**B21 outcome:** worked substantially. Wei's theorem ports cleanly after predictable localization. The previous residual obligation `prove P_n ~ (log n)^2 and control a nonlinear remainder` was too strong; both pieces have now been removed.

# 5. A second consequence: any exceptional convergence must have divergent radial energy

The three multiplier collapses in (4.5) impose a strong quantitative condition on any hypothetical endpoint-convergent path.

Use the coordinates of the previous report,

\[
x_1=\frac13+2u,
\qquad
x_2=\frac13-u+v,
\qquad
x_3=\frac13-u-v.
\tag{5.1}
\]

A direct Taylor division of the exact pair formulas at `alpha=4/3` gives

\[
\begin{aligned}
\lambda_{12}
&=-\frac32u-\frac32v-(3u^2+v^2)+O(r^3),\\
\lambda_{23}
&=3u-(3u^2+v^2)+O(r^3),\\
\lambda_{31}
&=-\frac32u+\frac32v-(3u^2+v^2)+O(r^3),
\end{aligned}
\tag{5.2}
\]

where `r=sqrt(u^2+v^2)`. Summing cancels the entire linear part:

\[
\boxed{
\lambda_{12}+\lambda_{23}+\lambda_{31}
=-3(3u^2+v^2)+O(r^3).
}
\tag{5.3}
\]

For sufficiently small `r`, the right side is bounded above and below by negative constant multiples of `r^2`.

Let

\[
\Pi_n=P_n^{12}P_n^{23}P_n^{31}.
\]

Because `lambda_p=O(r)` and `sum gamma_n^2<infinity`, the expansion `log(1+y)=y+O(y^2)` together with (5.3) gives, on any path eventually remaining near `x_*`,

\[
\boxed{
\log \Pi_n
=\log\Pi_N
-\Theta\!\left(\sum_{k=N}^{n-1}\gamma_{k+1}r_k^2\right)
+O(1).
}
\tag{5.4}
\]

The `O(1)` term is uniformly finite because

\[
\sum_k\gamma_{k+1}^2\lambda_p(X_k)^2<\infty.
\]

By Proposition 4.2, endpoint convergence forces all three `P_n^p->0`, hence `Pi_n->0`. Equation (5.4) therefore yields the new necessary condition

\[
\boxed{
X_n\to x_*
\quad\Longrightarrow\quad
\sum_{n}\gamma_{n+1}\,
\bigl\|X_n-x_*\bigr\|^2=\infty
\quad\text{a.s. on the convergence event, modulo a null set.}
}
\tag{5.5}
\]

(up to harmless equivalence of the Euclidean norm and `r` in the two-dimensional simplex tangent plane).

This is strikingly opposite to the deterministic incoming-separatrix heuristic. The monkey-saddle ODE gives `r(t)~const/t` along an incoming ray, and with stochastic-approximation time `t~log n` this predicts `r_n~const/log n`, for which

\[
\sum_n\frac{r_n^2}{n}<\infty.
\]

Thus an exceptional stochastic trajectory converging to the critical triangle, if it exists at all, cannot have the natural ODE-like critical rate. It must approach slowly/irregularly enough to accumulate **infinite radial square energy**.

# 6. B22 -- read the failures, not the successes

Wei's Section 2 is directly useful here because it explains what would have made the B21 route invalid. Predictable martingale-transform coefficients can be adapted to the past so that a transform has an arbitrary or even degenerate limit despite nontrivial martingale-difference noise. Therefore the slogan "nondegenerate noise implies no atom" is false.

The repair is exactly Lemma 4.1: in the WARM transverse factorization the coefficients cannot adapt arbitrarily while the path remains near `x_*`, because their multiplicative logarithmic derivative is `gamma_n lambda(X_n)` and `lambda(X_n)` is uniformly small. That forces the tail-square regularity required by Wei.

Brandière's 1998 paper is another warning against overgeneralization. Its abstract/introduction explicitly includes singular equilibria and repulsive regions among the pathological traps it studies, but the complete theorem hypotheses were not accessible from the publisher text inspected this run. I therefore record it as the nearest structural literature and **do not** claim a theorem import.

**B22 outcome:** worked as a failure analysis. It removed one false shortcut and, more importantly, showed that the exact WARM multiplier structure supplies precisely the condition missing from Wei's counterexamples.

# 7. New exact blocker after the port

The selected stuck recovery is still **PORT THE TECHNIQUE FROM THE NEAREST SOLVED ANALOGUE**. It made real progress, but it does not yet prove the optional endpoint (1.1).

The blocker is now much simpler than in the previous report. Proposition 4.2 and (5.5) show that any endpoint-convergent path must lie in the exceptional regime

\[
\boxed{
X_n\to x_*
\quad\text{and}\quad
\sum_n\gamma_{n+1}\|X_n-x_*\|^2=\infty.
}
\tag{7.1}
\]

Therefore it would suffice to prove the converse energy statement on the convergence event,

\[
\boxed{
X_n\to x_*
\quad\Longrightarrow\quad
\sum_n\gamma_{n+1}\|X_n-x_*\|^2<\infty.
}
\tag{7.2}
\]

or any weaker statement forcing at least one pair multiplier `P_n^{ij}` not to tend to zero.

What a proof must contain that the present routes still lack is a **multivariate zero-derivative rate/sector theorem**: convergence to this cubic-gradient critical point must force enough asymptotic alignment with one incoming separatrix to recover finite radial square energy. Wei's one-dimensional Theorem 4.2 supplies exactly that type of `log n` rate on a single restoring ray, but it does not control angular motion among the three sectors. Brandière is structurally closer, but no applicable theorem was verified from the accessible text.

The simplest still-unproved special case is: prove (7.2) under the additional assumption that the trajectory is eventually confined to one fixed incoming sector. That is weaker than the full endpoint question but would isolate the only remaining difficulty as infinite sector switching.

The nearest solved analogue remains Wei 1993 Theorem 4.2: one-dimensional zero-derivative Robbins--Monro has a `log n` convergence scale. What it has that the WARM critical triangle lacks is a scalar order/sign structure eliminating angular switching.

# 8. Metric/status and closure gates

Frozen source metric before: `A_forest=4/3`.  
Frozen source metric after: `A_forest=4/3`.  
Movement: **NO MOVEMENT**.  
Unchanged streak after the source-threshold improvement: **4 consecutive runs**.  
Source strict problem: **mathematically PROVED / NOT CLOSURE-CERTIFIED**.  
Auxiliary endpoint statement (1.1): **OPEN**, with the new reduction (4.5), (5.5).

No P26 end-to-end audit of P0082 and no distinct OTHER-track end-to-end audit were found in the bounded repository search. No previous P14 component audit was repeated merely to generate activity. Final publication-level prior-art clearance also remains open. Hence no closure label and no paper package are authorized yet.

The next three unused method moves will be **B4 (prove something weaker completely), B20 (find why the algorithm fails), B30 (one scale/sector at a time)**. Concretely: first prove finite radial energy under eventual confinement to a single incoming sector; then identify the exact mechanism by which repeated sector switching could defeat that proof; finally localize the switching process by dyadic radial scales.

# 9. Delivery / ledger delta

This run writes only this immutable P13 report. No redundant checker was created because the new claims are analytic and their proofs are on this page. No root ledger, peer file, historical report, claim ownership file, email/Gmail, Drive item, public post, paid compute, permission, workflow, or schedule was modified.

```yaml
ledger_delta:
  track: P13
  native_slot: 6aa7b253b37c8191b693d8dc79298d37
  canonical_id: P0082
  source: "Aletti et al. (2025), Open Problems in Stochastic Reinforcement Models, Open Problem 12"
  category: CLOSABLE_OUTSIDE
  metric:
    name: A_forest
    before: "4/3"
    after: "4/3"
    movement: "no movement"
    unchanged_streak: 4
  source_status: "PROVED mathematically / NOT CLOSURE-CERTIFIED"
  auxiliary_progress:
    id: P13-P0082-ENDPOINT-WEI-REDUCTION-04
    statement: "At alpha=4/3 on the uniform triangle, convergence to the symmetric critical equilibrium forces all three exact transverse multipliers to tend to zero and forces divergent radial square energy."
    status: PROVED_AUXILIARY_REDUCTION
    source_metric_credit: 0
  methods_tried: [18, 21, 22]
  selected_stuck_recovery: "port the technique from the nearest solved analogue"
  next_methods: [4, 20, 30]
  audits:
    p26_end_to_end: MISSING
    other_track_end_to_end: MISSING
    p14_component_duty: "previous completed audits retained; no redundant repeat"
  prior_art:
    status: "bounded search only; no final novelty clearance"
  retired_exclusions:
    - "P13 I0051 Aldous-Janson clade covariance remains retired"
```
