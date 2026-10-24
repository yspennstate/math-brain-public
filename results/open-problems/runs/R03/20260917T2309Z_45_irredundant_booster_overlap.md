Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED; GPT-6 / maximum was requested in prompt text, but the exposed runtime provides no authenticated applied-model/reasoning telemetry, so GPT-6 maximum is not claimed. F0097 NO MOVEMENT on the frozen source metric: `Omega_3 <= 0.9698` remains; F0097 unchanged count `2 -> 3`. Methods: #3 PROVE SOMETHING STRONGER, #15 BREAK THE SYMMETRY ON PURPOSE, #25 COUNT THE SAME THING TWICE.**

# R03 run45 — F0097 random k-SAT: essential clean boosters force mesoscopic two-replica correlation

Repository / branch: `yspennstate/math-open-problems` / `master`.

Status: **F0097 OPEN / R03 PARTIAL.** The native title/prompt still names F0001 / sharp iid Rademacher singularity, but canonical R03 state handed F0001 off after the third stuck episode in run41 and created exclusive claim `operations/claims/F0097.md`. That claim explicitly says R03 must not return to F0001 without reassignment. I therefore preserve the F0001 handoff and continue F0097.

## 1. Continuity, source, literature, and frozen metric

Before new mathematics I recovered/read the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, the controlling owner directive, `operations/claims/F0097.md`, newest own report `runs/R03/20260917T2205Z_44_booster_collision_barrier.md`, and the neighboring R02 F0097 admission report. I did not reset the F0097 stagnation count or the earlier `F0097-A001` history.

The outside source remains Alan Frieze, *Random Structures and Algorithms*, ICM-era survey/proceedings article. Its open-problems list asks to **find the precise threshold for satisfiability of random k-SAT**. Primary source:

- https://www.math.cmu.edu/users/af1p/Texfiles/Proc.pdf

Fresh current-status check dated 2026-09-17/18 UTC:

1. Chatterjee--Coja-Oghlan--Greenhill--Pfenninger--Rolvien--Zakharov--Zampetakis, *The random k-SAT Gibbs uniqueness threshold revisited*, CPC 35 (online 27 March 2026), states that the satisfiability threshold is known precisely for `k=2` and for sufficiently large `k`, while for `3 <= k < k_0` even existence of a uniform satisfiability threshold remains open.
2. Gaia Carenini, *The Scaling Window of Random k-SAT*, ECCC TR26-145 (16 August 2026), proves an `O(n/log n)` window for every fixed `k>=3`. This still does not imply convergence of the threshold location; the paper identifies the `n/log^{1+delta} n` scale as the frontier relevant to the Abbe--Montanari reduction.
3. A bounded fresh search did not locate a later accepted source-matching proof for small fixed `k`. This is negative search evidence, not a novelty certificate.

R03's frozen metric remains

\[
\theta_{k,n}=\frac1n\min\{m:\Pr(F_k(n,m)\text{ SAT})\le1/2\},\qquad
\Omega_k=\limsup_n\theta_{k,n}-\liminf_n\theta_{k,n},
\]

with the first unresolved case `Omega_3`, target zero. The conservative rigorous bracket remains

\[
\boxed{0\le \Omega_3\le 4.4898-3.52=0.9698.}
\]

The lower endpoint is the Hajiaghayi--Sorkin `3.52` theorem and the upper endpoint is the Diaz--Kirousis--Mitsche--Perez-Gimenez `4.4898` theorem. No route below narrows this limsup--liminf interval, so the metric has no movement and the unchanged count becomes `3`.

## 2. Setup inherited from runs43--44

Let `X` be a permutation-invariant random `k`-SAT formula. A deterministic **clean booster** `A` is a satisfiable finite set of proper `k`-clauses for which

\[
\beta_X(A):=\Pr(X\text{ SAT},\ X\cup A\text{ UNSAT})
\]

is non-negligible on the booster scale. Run44 introduced the collision deficiency

\[
q(A)=k|A|-|\operatorname{supp}A|
\]

and proved the orbit lower bound C301. If `|A|=O(K)` and `q(A)\log n=O(K)`, direct randomization already loses only `exp(-O(K))`. Hence the unresolved case is collision-rich.

This run asks what collision-richness buys analytically instead of trying another replacement lemma.

## 3. Method #3 — PROVE SOMETHING STRONGER: every booster contains an exponentially strong essential sub-booster

The ordinary statement “A boosts unsatisfiability” does not say that all clauses of `A` matter. Strengthen it by forcing clausewise essentiality on a fixed positive-probability subevent.

### R03-C304 — essential sub-booster extraction

Let `A` be any satisfiable set of `t>=1` clauses and put `beta=beta_X(A)`. Then there exists a nonempty subset `B subseteq A` such that

\[
\boxed{
\Pr\bigl(X\text{ SAT},\ X\cup B\text{ UNSAT},\
X\cup(B\setminus\{C\})\text{ SAT for every }C\in B\bigr)
\ge \frac{\beta}{2^t-1}.
}
\tag{C304}
\]

In particular

\[
\beta_X(B)\ge \frac{\beta_X(A)}{2^t-1}.
\]

Thus an `exp(-O(K))` clean booster of size `O(K)` has a fixed **essential** clean sub-booster of size `O(K)` that remains `exp(-O(K))` strong.

#### Proof

On each outcome in

\[
E_A=\{X\text{ SAT},\ X\cup A\text{ UNSAT}\}
\]

choose, by a fixed deterministic tie-breaking order, an inclusion-minimal nonempty `B_X subseteq A` such that `X union B_X` is unsatisfiable. Nonemptiness follows because `X` itself is satisfiable. Minimality gives

\[
X\cup(B_X\setminus\{C\})\text{ SAT}\qquad(C\in B_X).
\]

There are at most `2^t-1` possible nonempty values of `B_X`. The events `{B_X=B}` partition `E_A`, so one fixed `B` has probability at least `beta/(2^t-1)`. Since `B subseteq A` and `A` is satisfiable, `B` is clean. QED.

This reduction is elementary and is likely folklore in sharp-threshold/booster arguments; I make no novelty claim. Its value here is that it gives a fixed structural object to which collision and overlap information can be attached without losing the exponential booster scale.

## 4. Method #15 — BREAK THE SYMMETRY: the extracted booster is an irredundant subcube family with private solutions

Fix the `B` from C304 and an outcome in the C304 event. For each `C in B`, choose a satisfying assignment

\[
\sigma_C\models X\cup(B\setminus\{C\}).
\]

Because `X union B` is unsatisfiable, `sigma_C` must violate `C`. Therefore `sigma_C` satisfies every clause of `B` except `C`.

Let `S=supp(B)`, `r=|S|`, and let `H_C subseteq {0,1}^S` be the codimension-`k` subcube of local assignments that violate `C`. Then

\[
\sigma_C|_S\in H_C\setminus\bigcup_{D\in B,\ D\ne C}H_D.
\]

Hence the forbidden subcubes `{H_C:C in B}` form an **irredundant family**: each has a private point. Since `B` is satisfiable, choose `sigma_*` satisfying all of `B`; after flipping coordinates according to `sigma_*`, the origin lies outside every `H_C`. The asymmetry is now explicit:

- the origin is a common allowed point;
- every forbidden subcube has its own private point;
- on the selected random-formula event, the union of these blockers covers the entire projected solution set of `X`.

This is exactly the geometry behind minimally/irredundantly constrained clause sets. Kullmann--Zhao describe minimally unsatisfiable clause sets as irredundant subcube covers of the Boolean cube; here the cover is relative to the random solution projection and `B` itself remains satisfiable. I use that literature only as adjacent language, not as a claim that C304 is new.

A small exact consequence is

\[
2^r\ge |B|+1,
\]

because the `|B|` private local points and the common satisfying point are all distinct. This is not source-scale progress, but it rules out treating a collision-rich booster as an arbitrary multiset of clauses: after essential extraction it is an irredundant signed `k`-uniform subcube system.

## 5. Method #25 — COUNT THE SAME THING TWICE: booster strength equals a forced mesoscopic two-replica excess

The preceding geometry yields a quantitative statistic that can be counted both as a local chi-square divergence and as an overlap moment.

For a satisfiable formula `X`, let `mu_X` be the uniform measure on its satisfying assignments. For `S subseteq [n]`, `|S|=r`, let `mu_{X,S}` be its marginal on `S`, and let `U_S` be uniform on `{0,1}^S`. Define

\[
\mathcal C_r(X)
:=\frac1{\binom nr}\sum_{|S|=r}\chi^2(\mu_{X,S}\|U_S),
\]

and put `C_r(X)=0` when `X` is unsatisfiable.

Let `Q_B subseteq {0,1}^S` be the local assignments satisfying `B`, and

\[
q_B=\frac{|Q_B|}{2^r}.
\]

Since `B` is clean and nonempty, `0<q_B<1`.

### R03-C305 — booster-to-overlap inequality

For every fixed clean booster `B` supported on `r` variables,

\[
\boxed{
\beta_X(B)
\le \frac{1-q_B}{q_B}\,\mathbb E\mathcal C_r(X).
}
\tag{C305a}
\]

Equivalently,

\[
\boxed{
\mathbb E\mathcal C_r(X)
\ge \beta_X(B)\frac{q_B}{1-q_B}.
}
\tag{C305b}
\]

If `B` is the sub-booster extracted from a `t`-clause booster `A`, then `r<=kt` and `q_B>=2^{-r}`, so

\[
\boxed{
\mathbb E\mathcal C_r(X)
\ge \frac{\beta_X(A)}{2^t-1}\,2^{-r}
\ge \beta_X(A)\,2^{-(k+1)t}.
}
\tag{C305c}
\]

Thus any `exp(-O(K))` booster of size `O(K)` forces an `exp(-O(K))` amount of **mesoscopic local correlation** at some radius `r=O(K)`.

#### Proof of the chi-square step

On the event `X SAT` and `X union B UNSAT`, no satisfying assignment of `X` can have its restriction to `S` in `Q_B`. Hence

\[
\mu_{X,S}(Q_B)=0.
\]

Among all probability measures on a finite uniform space that assign zero mass to a set of uniform measure `q`, the chi-square divergence from uniform is minimized by the uniform measure on the complement. The minimum is

\[
q+\frac{q^2}{1-q}=\frac{q}{1-q}.
\]

Therefore, pointwise on the boosting event,

\[
\chi^2(\mu_{X,S}\|U_S)\ge \frac{q_B}{1-q_B}.
\]

Taking expectations and using permutation invariance of the law of `X` (so every fixed `r`-set has the same expected marginal chi-square as the average over all `r`-sets) proves C305a--b. Since `B` has at least one satisfying local assignment, `q_B>=2^{-r}`; combine with C304 and `r<=kt` for C305c. QED.

### R03-C306 — exact overlap/Fourier double count

Let `sigma,tau` be independent samples from `mu_X`, and let

\[
A(\sigma,\tau)=|\{i:\sigma_i=\tau_i\}|
\]

be their agreement count. Then for every satisfiable `X`,

\[
\boxed{
\mathcal C_r(X)+1
=
2^r\,\mathbb E_{\sigma,\tau\sim\mu_X}
\frac{\binom{A(\sigma,\tau)}r}{\binom nr}.
}
\tag{C306a}
\]

Indeed, for fixed `S`,

\[
\sum_z\mu_{X,S}(z)^2=\Pr(\sigma_S=\tau_S),
\]

and averaging over all `r`-subsets gives the hypergeometric factor above.

There is also the exact Fourier form. Put `f_X=2^n mu_X` and use the uniform-cube Fourier coefficients `hat f_X(T)`. Then

\[
\boxed{
\mathcal C_r(X)
=
\sum_{j=1}^r
\frac{\binom rj}{\binom nj}
\sum_{|T|=j}\widehat f_X(T)^2.
}
\tag{C306b}
\]

This follows because the density of the `S`-marginal is the conditional expectation of `f_X` onto coordinates `S`, and Parseval leaves exactly Fourier sets `T subseteq S`.

The identity connects directly to run43. Its one-clause defect `D(X)` is exactly

\[
D(X)=2^{-k}\mathcal C_k(X).
\]

Run43's fractional-martingale budget therefore controls weighted **fixed-level** correlation `C_k`, while C305 says a strong essential booster forces correlation at a potentially **mesoscopic level** `C_r`, with `r=O(K)`.

That is the concrete missing bridge:

\[
\boxed{
\text{strong booster}\Longrightarrow \mathcal C_{O(K)}\text{ non-negligible},
\qquad
\text{available energy budget controls only }\mathcal C_k.
}
\]

A generic downward implication `C_r -> C_k` is false for arbitrary cube measures because correlation can live entirely at Fourier levels `k+1,...,r`. Therefore the next useful theorem has to use the **k-CNF solution-set structure**, not probability-measure inequalities alone.

## 6. What this changes in the route, and what it does not

Runs43--44 left two apparent obstacles: low-collision boosters and generic helper replacement. Combining C301 with C304--C306 gives a cleaner dichotomy for an exponentially strong booster:

1. Extract an essential irredundant sub-booster `B` at only `exp(-O(K))` loss.
2. If its collision deficiency is small, C301 directly randomizes it at `exp(-O(K))` cost.
3. If it is collision-rich, C305 forces mesoscopic two-replica/Fourier correlation in the random formula's solution measure.

Thus the unresolved object is no longer an arbitrary collision-rich clause set. It is an **irredundant collision-rich booster whose boost forces `C_r` at `r=O(K)`**, and the remaining analytic problem is a model-specific propagation or energy estimate for that mesoscopic correlation.

This does **not** yet narrow

\[
0\le\Omega_3\le0.9698.
\]

In particular, C305 gives an `exp(-O(K))` correlation signal, but at the superlogarithmic scale needed for threshold convergence it is not yet known how to convert that signal into either a contradiction with the run43 energy budget or a stronger random-clause boost. So the honest status is **F0097 OPEN / R03 PARTIAL / frozen metric unchanged / unchanged count 3**.

## 7. Stuck trigger

This is the third consecutive F0097 run without movement of the frozen metric. Under Section I, **the next R03 run must be the first F0097 thinking-only stuck recovery**: no new theorem/checker should be manufactured there.

Its blocker should be stated as a single implication problem:

\[
\boxed{
\mathcal C_{r_n}(F_n)\ge e^{-O(r_n)}
\text{ at }r_n\asymp K_n
\quad\Longrightarrow\quad
\text{enough fixed-level/native response to force }K_n\gg\log n,
}
\]

for near-critical random `k`-SAT solution measures, with `k=3` the first target. Generic measures do not satisfy such a downward-correlation principle; any successful proof must exploit the CNF geometry or a multiscale clause-exposure invariant.

The next thinking-only triple is **#22 READ THE FAILURES, #21 ASK WHO ELSE HAS THIS SHAPE, #5 ADD A PARAMETER**. The intended literature comparison is with sharp-threshold booster proofs, irredundant subcube families/minimal unsatisfiability, and replica-overlap/free-energy interpolation, looking specifically for a mechanism that transfers mesoscopic overlap energy to bounded-local observables.

## 8. Runtime / control boundary

The exposed task-control interface still supplies prompt/title/schedule/timing/enabled controls but no model-family selector, no reasoning-effort selector, and no authenticated applied-model telemetry. `GPT-6 / maximum` therefore remains prompt-only. Repository edits cannot change that. The historical P26 `You cannot modify this task` event was authorization/context dependent; the lawful workaround is an owning/authorized workspace or platform support, not task duplication or permission bypass.

No email, Drive action, public posting, purchase, permission change, workflow execution, scheduler edit, shared-root edit, or peer-file edit was made.

## ledger_delta

```yaml
track: R03
canonical_target: F0097
lane: HARD_OUTSIDE
source_status: OPEN
worker_status: PARTIAL
frozen_metric: Omega_3
metric_before: '<= 0.9698'
metric_after: '<= 0.9698'
movement: false
unchanged_count_before: 2
unchanged_count_after: 3
methods: [3, 15, 25]
new_claims:
  - R03-C304 essential clean sub-booster extraction with exp(-O(K)) strength retained
  - R03-C305 booster-to-mesoscopic-chi-square lower bound
  - R03-C306 exact overlap/Fourier double count for average r-marginal chi-square
finite_claims: 0
checker: none
stuck_triggered_for_next_run: true
next_run_mode: SECTION_I_THINKING_ONLY_RECOVERY_1
next_methods: [22, 21, 5]
F0001:
  status: OPEN_PARTIAL_HANDED_OFF
  reopened: false
shared_roots_edited: false
peer_files_edited: false
email: false
drive: false
public_posting: false
scheduler_modified: false
```
