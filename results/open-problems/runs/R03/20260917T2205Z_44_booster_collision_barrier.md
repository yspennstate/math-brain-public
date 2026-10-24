Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED; GPT-6 / maximum was requested in prompt text, but the exposed runtime provides no authenticated applied-model/reasoning telemetry, so GPT-6 maximum is not claimed. F0097 NO MOVEMENT on the frozen source metric: `Omega_3 <= 0.9698` remains; F0097 unchanged count `1 -> 2`. Methods: #9 RANDOMIZE, #20 FIND WHY THE ALGORITHM FAILS, #24 FIND THE EXTREMAL OBJECT.**

# R03 run44 — F0097 random k-SAT: low-collision booster simulation and a superlogarithmic replacement obstruction

Repository / branch: `yspennstate/math-open-problems` / `master`.

Status: **F0097 OPEN / R03 PARTIAL.** The stale native title/prompt still names F0001 / sharp iid Rademacher singularity, but canonical R03 state already handed F0001 off after the third stuck episode in run41 and created exclusive claim `operations/claims/F0097.md`. Under the owner's continuity rule F0001 is not reopened without explicit reassignment.

## 1. Continuity, source, literature, and frozen metric

Before new mathematics I recovered/read `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/claims/F0097.md`, newest own report `runs/R03/20260917T2108Z_43_fractional_cavity_energy.md`, the neighboring R02 F0097 source screen, and intake history including `F0097-A001`. The Ding--Sly--Sun sufficiently-large-`k` theorem remains prior history and is not reset.

The outside source remains Alan Frieze, *Random Structures and Algorithms*, ICM 2014, whose random-k-SAT open-problem slide asks for the precise satisfiability threshold. Primary source PDF: <https://www.math.cmu.edu/users/af1p/Texfiles/Proc.pdf>.

Fresh bounded current-status check dated 2026-09-17/18 UTC:

1. Chatterjee--Coja-Oghlan--Greenhill--Pfenninger--Rolvien--Zakharov--Zampetakis, *The random k-SAT Gibbs uniqueness threshold revisited*, CPC 35 (published online 27 March 2026), states that the satisfiability threshold is known for `k=2` and all sufficiently large `k`, while the small fixed-`k` cases remain unresolved.
2. Gaia Carenini, *The Scaling Window of Random k-SAT*, ECCC TR26-145, 12/16 August 2026, proves for every fixed `k>=3` a central clause window `O(n/log n)`. Section 10 explicitly records the current barrier: an `O(n/log^{1+delta} n)` window for some `delta>0` would imply threshold convergence via Abbe--Montanari, while the present clean-booster/replacement/layer argument only forces a logarithmic scale.
3. A bounded fresh search found no later accepted theorem closing the small-fixed-`k` threshold-existence problem. This is negative search evidence, not a worldwide novelty certificate.

Run42 froze

\[
\theta_{k,n}=\frac1n\min\{m:\Pr(F_k(n,m)\text{ SAT})\le1/2\},\qquad
\Omega_k=\limsup_n\theta_{k,n}-\liminf_n\theta_{k,n}.
\]

R03 tracks the first unresolved case `Omega_3`, target zero. The source-backed bracket remains

\[
\boxed{0\le\Omega_3\le0.9698.}
\]

None of the route lemmas below reduces that limsup--liminf bracket, so the frozen metric has **no movement** and the F0097 unchanged count becomes `2`.

## 2. Method #9 — RANDOMIZE: clean boosters with small collision deficiency are already cheaply simulable

Carenini's Section 10 makes the helper-to-native replacement cost one of the visible losses. I therefore asked a sharper question: when can a *particular deterministic clean booster* be randomized directly, without any generic helper simulation?

Let `A` be a set of `t` distinct proper `k`-clauses involving exactly `r` variables, and define its **collision deficiency**

\[
\boxed{q(A):=kt-r.}
\tag{2.1}
\]

Thus `q=0` exactly when the clause supports are disjoint. Let `X` be any random-k-SAT formula law invariant under variable permutations, and write

\[
\beta_X(A):=\Pr\bigl(X\text{ SAT},\ X\cup A\text{ UNSAT}\bigr).
\]

Let `Y_1,...,Y_t` be independent uniform proper `k`-clauses on `[n]`, with

\[
N_{n,k}=2^k\binom nk
\]

possible clauses.

### R03-C301 — orbit simulation lemma

For every such `A`,

\[
\boxed{
\Pr\bigl(X\text{ SAT},\ X\cup\{Y_1,\ldots,Y_t\}\text{ UNSAT}\bigr)
\ge
\beta_X(A)\,
\frac{(n)_r}{2^{kt}(n)_k^t}.
}
\tag{C301}
\]

#### Proof

Abstract the `r` used variables of `A`. There are `(n)_r` injective maps of those variables into `[n]`. Two injections can yield the same signed clause set only if they differ by an automorphism of the signed hypergraph `A`.

Every variable of `A` belongs to at least one clause. Hence an automorphism is determined by a permutation of the `t` clauses and, for each clause, a permutation of its `k` variable positions. Therefore

\[
|\operatorname{Aut}(A)|\le t!(k!)^t.
\]

Consequently the orbit of distinct injective images has cardinality at least

\[
\frac{(n)_r}{t!(k!)^t}.
\]

For a fixed image `A'`, the ordered tuple `(Y_1,...,Y_t)` has underlying set exactly `A'` with probability `t!/N_{n,k}^t`. The events for distinct image sets are disjoint. Since the law of `X` is invariant under variable permutations, every image has the same boost `beta_X(A)`. Summing over images gives

\[
\beta_X(A)\frac{(n)_r}{t!(k!)^t}\frac{t!}{N_{n,k}^t}
=
\beta_X(A)\frac{(n)_r}{2^{kt}(n)_k^t}.
\]

QED.

If `t=O(K)`, `K=o(sqrt(n))`, and

\[
q(A)\log n=O(K),
\]

then

\[
\log\frac{(n)_r}{2^{kt}(n)_k^t}
\ge -q(A)\log n-k(\log2)t-O(K^2/n)=-O(K),
\]

so the random native block preserves an `exp(-O(K))` fraction of the deterministic boost using only `t=O(K)` clauses.

This is a concrete simplification of the replacement problem: **clean boosters with collision deficiency at most order `K/log n` do not need the generic helper-to-native simulation machinery at all.** The unresolved replacement problem can be localized to collision-rich boosters.

There is a useful hypergraph corollary. In a connected component with `s>=2` clauses, if `v` variables occur, connectivity gives

\[
v\le k+(s-1)(k-1)=1+(k-1)s,
\]

hence its deficiency satisfies `ks-v>=s-1`. Therefore the total number of clauses lying in non-singleton components is at most

\[
\boxed{2q(A).}
\tag{2.2}
\]

So a low-deficiency booster is literally an almost-matching: all but at most `2q(A)` clauses are isolated support components.

I did not locate this exact orbit/deficiency statement in the bounded search. The ingredients are elementary orbit counting, so this is **not** a novelty certificate; it is recorded as a proved route lemma.

## 3. Method #20 — FIND WHY THE ALGORITHM FAILS: simulation improvement alone cannot cross the log barrier in the one-shot architecture

Carenini's concluding calculation has three scales:

- deterministic clean-booster gain at least `exp(-O(K))`;
- helper-to-native simulation cost `D`;
- a universal Boolean-layer response of order `O((D+1)/sqrt(V))`.

The paper correctly identifies all three as possible places where model-specific information could help. But there is a sharper one-shot obstruction worth making explicit.

Suppose, optimistically, that the replacement problem is solved perfectly and `D=1`. If the only deterministic lower bound remains

\[
\text{boost}\ge e^{-aK}
\]

for a fixed `a>0`, and the final contradiction still compares it with a universal layer increment `O(V^{-1/2})`, then necessarily

\[
e^{-aK}\lesssim V^{-1/2},
\]

which yields only

\[
\boxed{K\ge \frac{1}{2a}\log V-O(1).}
\tag{C302}
\]

More generally `D=\exp(o(K))` changes only lower-order terms:

\[
e^{-aK}\lesssim \frac{e^{o(K)}}{\sqrt V}
\quad\Longrightarrow\quad
K\ge \left(\frac1{2a}+o(1)\right)\log V.
\]

Therefore **subexponential or even constant-cost simulation, by itself, cannot produce `K >> log V` inside the same one-shot inequality**. To reach the Abbe--Montanari `log^{1+delta}` denominator frontier, at least one further ingredient is required:

1. a stronger deterministic booster whose gain is `exp(-o(K))` (or better), or
2. a genuinely model-specific layer response substantially sharper than `V^{-1/2}` on the relevant family, or
3. a multiscale/non-one-shot argument in which gains accumulate without paying the same universal layer estimate once.

This is not a claim that Carenini's suggested simulation direction is wrong; rather, it isolates what an improved simulation theorem must be paired with in order to improve the *order* of the final window.

## 4. Method #24 — FIND THE EXTREMAL OBJECT: a single helper atom defeats generic superlog replacement

The preceding calculation says replacement cannot be the whole story. I then searched for the extremal set showing why a generic helper-to-native theorem itself becomes misleading at superlogarithmic `K`.

Work in the atomic Boolean model on `m` variables. Let

\[
B=\{x\in\{0,1\}^m:x_1=\cdots=x_{k-1}=0\},
\]

a full codimension-`(k-1)` cylinder.

A uniform helper from Carenini's family `U^{(k-1)}_{m,2}` contains `B` iff it is exactly this cylinder. Thus

\[
\boxed{
\Pr(Q\supseteq B)=\frac1{2^{k-1}\binom m{k-1}}=\Theta(m^{-(k-1)}).
}
\tag{4.1}
\]

If `K/log m -> infinity`, then for every fixed `C>0`,

\[
\Theta(m^{-(k-1)})\gg e^{-CK}.
\]

So at superlog `K`, a putative booster probability on the `e^{-CK}` scale can be completely carried by this single helper atom.

Now compare with `D=o(m)` independent native `k`-clauses. A random clause support intersects the fixed `k-1` coordinates with probability `O(1/m)`, so among `D=o(m)` clauses there is no such intersection with probability `1-o(1)`. Conditional on that event, restricting the clauses to `B` gives exactly `D` ordinary random proper `k`-clauses on the `m-k+1` free variables. Random `k`-SAT with `o(m)` clauses is satisfiable with probability `1-o(1)` (for example by the fixed-positive-density satisfiable regime used in Carenini's Proposition 7.4, followed by the standard fixed-size/monotonicity transfer). Hence

\[
\boxed{
\Pr(\text{the }D\text{ native clauses cover }B)=o(1)
\qquad(D=o(m)).
}
\tag{C303}
\]

Thus there is a concrete obstruction to any *generic* statement of the form “an `e^{-CK}` helper-cover probability automatically implies comparable cover probability from `o(m)` native clauses” once `K>>log m`. Additional structure of the actual booster is indispensable.

Together C301 and C303 divide the booster world in a useful way:

- **low collision deficiency:** direct orbit randomization already works at `exp(-O(K))` cost;
- **generic atom/cylinder behavior:** helper coverage can be much larger than what a sublinear native block can reproduce;
- therefore the genuinely source-relevant unresolved class is **collision-rich clean boosters with enough global structure to avoid the cylinder-atom obstruction**.

This is a more concrete remaining object than “improve the coupling”.

## 5. What moved mathematically, and what did not

The source metric did not move:

\[
\boxed{0\le\Omega_3\le0.9698.}
\]

Therefore the honest status is **F0097 OPEN / R03 PARTIAL / frozen metric unchanged / unchanged count 2**.

The research state did sharpen in a different, non-metric sense:

1. C301 removes all low-collision clean boosters from the generic replacement bottleneck.
2. C302 proves that better simulation alone cannot change the logarithmic *order* in the existing one-shot comparison.
3. C303 gives an explicit helper atom showing why a generic superlog helper-to-native theorem is false without additional booster structure.

The next useful theorem would therefore not be another cavity identity or another generic replacement bound. It should be a **collision-rich booster structure theorem**. A concrete target is:

> If a clean atomic `k`-SAT booster of size `t=O(K)` has `q(A) >> K/log n`, then either its boosting effect is already carried by a smaller local obstruction/minimal unsatisfiable witness, or the collision core forces a model-specific response strong enough to beat the universal `V^{-1/2}` layer loss.

This is not yet proved.

## 6. Methods attempted and next moves

- **#9 RANDOMIZE:** succeeded in producing C301 and localizing generic replacement to collision-rich boosters.
- **#20 FIND WHY THE ALGORITHM FAILS:** C302 shows the exact one-shot order barrier; constant/subexponential simulation alone remains logarithmic.
- **#24 FIND THE EXTREMAL OBJECT:** the codimension-`(k-1)` cylinder gives C303, a concrete extremizer obstructing generic superlog replacement.

The next planned triple is **#3 PROVE SOMETHING STRONGER, #15 BREAK THE SYMMETRY ON PURPOSE, #25 COUNT THE SAME THING TWICE**. The intended route is to split a collision-rich booster into its isolated matching part and collision core, then count formula/embedding pairs in two directions to see whether a large boost forces a smaller witness or an atypically strong layer derivative.

If the frozen metric also fails to move on the next run, F0097 will reach three consecutive unchanged runs and the owner's Section-I stuck protocol must trigger; this report does not reset that count.

## 7. Runtime / control boundary

The exposed task-control interface still has no model-family or reasoning-effort selector and no authenticated applied-model telemetry. `GPT-6 / maximum` remains prompt-only. The historical P26 `You cannot modify this task` result is an authorization/workspace-boundary issue; repository edits cannot repair it and no permission bypass is attempted.

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
unchanged_count_before: 1
unchanged_count_after: 2
methods: [9, 20, 24]
new_claims:
  - R03-C301 orbit simulation lemma for low-collision clean boosters
  - R03-C302 one-shot logarithmic barrier even under ideal/subexponential simulation
  - R03-C303 codimension-(k-1) helper-atom obstruction to generic superlog replacement
next_methods: [3, 15, 25]
F0001_state: handed_off_OPEN_PARTIAL_not_reopened
```
