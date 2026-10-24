Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested in prompt text, but this runtime exposes no authenticated model selector, reasoning-effort selector, or applied-effort telemetry, so GPT-6/maximum is not claimed. **MOVEMENT:** `epsilon_bridge: 9e-10 -> 1/42000000 = 2.38095238095e-8`; supported unchanged count `1 -> 0`. Methods actually tried: **#24 FIND THE EXTREMAL OBJECT, #15 BREAK THE SYMMETRY ON PURPOSE, #25 COUNT THE SAME THING TWICE**.

# R16 HARD OUTSIDE — I0036 / Schramm Problem 2.1: preserve the Krachun–Panagiotis dichotomy and improve the critical bridge exponent

Date: 2026-09-17 UTC.  
Repository/branch: `yspennstate/math-open-problems` / `master`.  
Source-level status: **PARTIAL / OPEN**.  
This run's mathematical status: **new repository proof of a stronger explicit bridge-decay exponent; publication novelty UNVERIFIED**.

## 1. Continuity and fixed metric

I continued from the newest complete R16 report

`runs/R16/2026-09-17T07-53-02Z_i0036-renewal-height-sle-dictionary_a61c.md`.

The active exclusive claim is `operations/claims/I0036.md`. The source is Oded Schramm, *Conformally invariant scaling limits: an overview and a collection of problems*, ICM 2006, arXiv:math/0602151, Problem 2.1: prove existence of the small-mesh scaling limit of the infinite half-plane planar self-avoiding walk and identify it with `SLE_{8/3}`.

The frozen R16 metric remains

`epsilon_bridge` = the largest explicit exponent `epsilon>0` for which R16 has a complete all-`T` proof, in the critical hexagonal-lattice normalization of Krachun–Panagiotis, of

`B_T <= C_epsilon T^{-epsilon}` for every integer `T>=1`, with an explicit finite constant `C_epsilon`.

The predecessor report retained the R16 value `epsilon_bridge=9e-10`. This run proves the stronger value

\[
\boxed{\epsilon_{\rm bridge}\ge \frac1{42,000,000}=2.38095238095\times10^{-8}.}
\]

The unchanged counter therefore resets to zero.

## 2. Repository/source recovery and current-status check

Before the proof I recovered/read the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the current I0036 claim, the newest R16 report, the R09 admission trail for I0036, and current searches over the intake/history corpus. The connector does not make a literal rendering of all roughly 780 JSONL rows practical, so I did not pretend to have model-visible copies of every row; the exact I0036 source/claim and the intake-derived R09 admission report were recovered, and repository-wide source/ownership searches found no competing owner.

The former neighboring R11 planar-SAW work is historical: R11 has since rotated to another outside target, so there is no current ownership collision. I0036 remains exclusively R16-owned.

Fresh literature checks on 2026-09-17 found that Dmitrii Krachun and Christoforos Panagiotis, *Quantitative sub-ballisticity of self-avoiding walk on the hexagonal lattice*, is now a peer-reviewed Annals of Probability article, 54(3) (2026), 1109–1125, DOI `10.1214/24-AOP1730`, published 31 May 2026. Its Theorem 2 gives the published baseline

\[
B_T\le100T^{-10^{-10}}.
\]

A bounded search for a later explicit improvement of that bridge exponent did not locate one. That negative search is not a novelty certificate, so the result below is labeled publication novelty **UNVERIFIED**.

The stale scheduler title was also refreshed rather than silently trusted. Bansal–Jiang, arXiv:2508.03961v2, give efficient `O(sqrt(t))` Beck–Fiala bounds for `t>=log^2 n` and weaker sparse-regime bounds. Guo–Fang–Lu, arXiv:2609.11189v1, submitted 10 September 2026, state a dimension-free `3 sqrt(2 pi)` Komlós signing theorem and explicitly deduce

\[
\operatorname{disc}(A)<3\sqrt{2\pi t}
\]

for every integer `t>=1`, without an `n` restriction. That remains a very recent primary-preprint resolution claim rather than mature refereed validation. Under the owner continuity/exclusion rule I therefore continue the admitted I0036 successor rather than restarting Beck–Fiala from the historical task title.

## 3. Source inequalities retained exactly

Write `D_T` and `G_k` in the notation of Krachun–Panagiotis. I use four published facts.

First, Lemma 2.2 gives

\[
\sum_{k\ge T}G_k\le c_G D_{2T-1},
\qquad
c_G:=\frac{\cos(\pi/8)}{2\cos(3\pi/8)}=\frac{1+\sqrt2}{2}.
\tag{3.1}
\]

Second, Lemma 2.3 says `(D_T)` is nonincreasing and

\[
B_T\le \cos(\pi/8)D_T<D_T.
\tag{3.2}
\]

Third, their Section 3.2 gives, for every integer `T>=1`, one of two geometric cases. In case (a), Lemma 3.2 states

\[
T D_{10T}^{2}
\le 256\sqrt2\,
\frac{D_{\lceil(T+1)/2\rceil}}{D_{4T}}
\left(\sum_{i=0}^{T}D_i\right)
\left(\sum_{\ell=T}^{7T}G_\ell\right).
\tag{3.3}
\]

In case (b), Lemma 3.3 states

\[
T^2D_{18T}^{3}
\le 2^{15}
\left(
\frac{D_{\lceil(T+1)/2\rceil}}{D_{10T}}
\sum_{i=0}^{\lfloor5T/2\rfloor}D_i
\right)^2
\left(\sum_{k=T}^{21T}G_k\right).
\tag{3.4}
\]

The published proof coarsens these asymmetric alternatives into a fifth-power recurrence before running its analytical induction. The new move is to **not perform that coarsening**.

## 4. The new theorem

### Theorem R16-I0036-C03

For the critical hexagonal-lattice bridge partition function of Krachun–Panagiotis,

\[
\boxed{
D_T\le1000\,T^{-1/42,000,000}
\quad\text{and hence}\quad
B_T\le1000\,T^{-1/42,000,000}
\qquad(T\ge1).
}
\tag{4.1}
\]

In particular, the frozen metric moves from `9e-10` to `1/42000000`.

### Proof

Set

\[
\varepsilon=\frac1{42,000,000},\qquad
M=2,625,000,\qquad
A=1000,
\qquad
q:=22^{-M\varepsilon}=22^{-1/16}.
\tag{4.2}
\]

Let

\[
E_s:=22^{Ms}\qquad(s\ge0).
\]

We prove simultaneously that

\[
D_k\le A k^{-\varepsilon}\quad(1\le k\le E_s)
\tag{4.3}
\]

and the stronger endpoint estimate

\[
D_{E_s}\le qA E_s^{-\varepsilon}.
\tag{4.4}
\]

#### Base case

Since `D_1<=D_0=sec(pi/8)<11/10` and `q>1/2`,

\[
D_1<\frac{11}{10}<500<qA.
\]

Thus (4.3)–(4.4) hold at `s=0`.

#### Induction setup

Assume (4.3)–(4.4) at level `s-1`. Put

\[
T_0=E_{s-1},\qquad K=E_s=22^M T_0.
\]

Before proving the endpoint estimate at `K`, monotonicity already fills the whole intervening interval. Indeed, for `T_0<=k<=K`,

\[
D_k\le D_{T_0}
\le qA T_0^{-\varepsilon}
=A K^{-\varepsilon}
\le A k^{-\varepsilon}.
\tag{4.5}
\]

Together with the induction hypothesis this establishes the global bound (4.3) all the way through `K`; it may therefore be used below for every numerator and partial sum that occurs at the selected scale.

By (3.1), monotonicity, and (4.4) at `T_0`,

\[
\sum_{k\ge T_0}G_k
\le c_G D_{2T_0-1}
\le c_G D_{T_0}
\le c_G qA T_0^{-\varepsilon}.
\tag{4.6}
\]

For `j=0,1,...,M-1`, let

\[
T_j=22^jT_0.
\]

The integer bands `[T_j,21T_j]` are pairwise disjoint because `21T_j<T_{j+1}`. Counting the same tail through these `M` disjoint bands, some `j=j_0` satisfies

\[
\sum_{k=T}^{21T}G_k
\le \frac{c_G qA}{M}T_0^{-\varepsilon},
\qquad T:=T_{j_0}.
\tag{4.7}
\]

This is method #25 in its useful form: one global tail count selects a scale on which either original geometric alternative can be exploited.

We also need a uniform partial-sum estimate. Put `C_0=D_0=sec(pi/8)`. From (4.3), for every integer `R>=1`,

\[
\sum_{i=0}^{R}D_i
\le C_0+A\sum_{i=1}^{R}i^{-\varepsilon}
\le A K_1 R^{1-\varepsilon},
\tag{4.8}
\]

where

\[
K_1:=\frac{1+C_0/A}{1-\varepsilon}
<\frac{501}{500}.
\tag{4.9}
\]

The elementary trigonometric bounds used here and below are

\[
C_0<\frac{11}{10},\qquad
c_G<\frac{121}{100},\qquad
\sqrt2<\frac32.
\tag{4.10}
\]

At the selected `T`, the source geometry is in exactly one of cases (a),(b).

### Case (a)

Define

\[
R_a:=\frac{D_{\lceil(T+1)/2\rceil}}{D_{4T}}.
\]

This ratio is the extremal object singled out by method #24.

**Large-ratio branch.** If `R_a>2`, then

\[
D_K\le D_{4T}
<\frac12D_{\lceil(T+1)/2\rceil}
\le \frac A2\,2^{\varepsilon}T^{-\varepsilon}
\le \frac A2\,2^{\varepsilon}T_0^{-\varepsilon}.
\tag{4.11}
\]

Because `2M\varepsilon=1/8` and `\varepsilon<1/8`,

\[
2^{\varepsilon}22^{1/8}
<2^{1/8}22^{1/8}=44^{1/8}<2,
\]

so (4.11) is strictly at most

\[
A22^{-1/8}T_0^{-\varepsilon}
=qA K^{-\varepsilon}.
\tag{4.12}
\]

Thus a large denominator ratio is not a nuisance to be bounded away: it is itself the desired contraction.

**Small-ratio branch.** If `R_a<=2`, apply the original Lemma 3.2, (4.7), and (4.8). Since the shorter `G`-sum from `T` to `7T` is at most the selected band,

\[
\begin{aligned}
D_K^2
&\le D_{10T}^2\\
&\le \frac{256\sqrt2\cdot2}{T}
\left(AK_1T^{1-\varepsilon}\right)
\left(\frac{c_GqA}{M}T_0^{-\varepsilon}\right)\\
&=\frac{C_a}{M}\,qA^2T^{-\varepsilon}T_0^{-\varepsilon},
\end{aligned}
\tag{4.13}
\]

where

\[
C_a:=256\sqrt2\cdot2\,c_GK_1.
\]

Using (4.9)–(4.10),

\[
C_a<\frac{2,909,808}{3,125},
\qquad
\frac{C_a}{M}<\frac12<22^{-3/16}.
\tag{4.14}
\]

Also `T>=T_0`. Hence

\[
D_K^2
<22^{-3/16}q A^2T_0^{-2\varepsilon}
=22^{-1/4}A^2T_0^{-2\varepsilon}
=\left(qAK^{-\varepsilon}\right)^2.
\tag{4.15}
\]

This closes case (a).

### Case (b)

Define

\[
R_b:=\frac{D_{\lceil(T+1)/2\rceil}}{D_{10T}}.
\]

**Large-ratio branch.** If `R_b>2`, exactly the same direct-drop argument gives

\[
D_K\le D_{10T}
<\frac12D_{\lceil(T+1)/2\rceil}
\le qAK^{-\varepsilon}.
\tag{4.16}
\]

**Small-ratio branch.** If `R_b<=2`, use the original Lemma 3.3. Since

\[
\sum_{i=0}^{\lfloor5T/2\rfloor}D_i
\le AK_1\left(\frac{5T}{2}\right)^{1-\varepsilon},
\]

we obtain

\[
\begin{aligned}
D_K^3
&\le D_{18T}^3\\
&\le
\frac{2^{15}\cdot 2^2}{T^2}
\left(AK_1(5T/2)^{1-\varepsilon}\right)^2
\left(\frac{c_GqA}{M}T_0^{-\varepsilon}\right)\\
&\le \frac{C_b}{M}\,qA^3T^{-2\varepsilon}T_0^{-\varepsilon},
\end{aligned}
\tag{4.17}
\]

where it is enough to take

\[
C_b:=2^{15}\cdot 2^2\,c_GK_1^2\left(\frac52\right)^2.
\]

The exact rational upper bound is

\[
C_b<\frac{15,550,013,952}{15,625},
\qquad
\frac{C_b}{M}<\frac{19}{50}.
\tag{4.18}
\]

The remaining comparison is exact:

\[
\frac{19}{50}<22^{-5/16},
\tag{4.19}
\]

because (4.19) is equivalent to

\[
22^5\,19^{16}<50^{16},
\]

and the two exact integers are

\[
1,486,520,899,087,326,613,638,167,392
<
1,525,878,906,250,000,000,000,000,000.
\]

Therefore, again using `T>=T_0`,

\[
D_K^3
<22^{-5/16}qA^3T_0^{-3\varepsilon}
=22^{-3/8}A^3T_0^{-3\varepsilon}
=\left(qAK^{-\varepsilon}\right)^3.
\tag{4.20}
\]

This closes case (b).

In either source case, (4.4) holds at `E_s=K`, completing the induction. Thus `D_T<=1000T^{-epsilon}` for every integer `T>=1`. Finally (3.2) gives the same bound for `B_T`. ∎

## 5. What each new-method move contributed

### #24 — FIND THE EXTREMAL OBJECT

The published recurrence contains the ratios

\[
\frac{D_{\lceil(T+1)/2\rceil}}{D_{4T}},
\qquad
\frac{D_{\lceil(T+1)/2\rceil}}{D_{10T}}.
\]

The prior coarsening treats them as quantities to eliminate. The key observation is the opposite: when either ratio is large, its denominator is already smaller than the numerator by a fixed factor, giving the required geometric contraction directly. The difficult branch is therefore the bounded-ratio branch, where Lemma 3.2 or 3.3 becomes much stronger.

### #15 — BREAK THE SYMMETRY ON PURPOSE

Cases (a) and (b) have genuinely different powers (`D^2` versus `D^3`) and different denominator ratios. Combining them into the universal fifth-power Corollary 3.1 discards this asymmetry. Retaining the two source cases separately is what permits the much shorter geometric block `M=2,625,000` and the exponent `1/42,000,000`.

### #25 — COUNT THE SAME THING TWICE

The bands `[T_j,21T_j]` are disjoint. Their total mass is bounded once by the global tail (Lemma 2.2), and again one chosen band is fed into the relevant local geometric inequality. This pigeonhole count produces the `1/M` gain without requiring a new combinatorial construction.

## 6. Exact finite certificate

The only finite/arithmetic core is the constant comparison. I wrote and executed an exact `Fraction` checker; no floating-point inequality is used in any assertion.

Checker:

`artifacts/R16/2026-09-17T08-55-29Z_i0036_dichotomy_bridge_1over42m_check.py`

creation commit: `8d5189f6964a5bc7452ffdb433fade8ebff11c24`

Archived output:

`artifacts/R16/2026-09-17T08-55-29Z_i0036_dichotomy_bridge_1over42m_check.out`

creation commit: `4db14b984c111d8b935a5eaf84ab08859c5b5c24`

The output ends

`ALL_EXACT_CHECKS_PASS`.

The checker verifies, among other exact comparisons,

- `M*epsilon=1/16`;
- `K1_upper=894600/893617<501/500`;
- `Ca/M=121242/341796875<1/2<22^(-3/16)`;
- `Cb/M=647917248/1708984375<19/50<22^(-5/16)`;
- the direct-drop inequality and base endpoint bound.

The theorem-sized argument itself is written in full above; the checker is only the arithmetic certificate, not a substitute for the proof.

## 7. Prior-art and scope discipline

The source paper explicitly says its constants were not optimized. A fresh bounded search found the published Krachun–Panagiotis paper and no later paper advertising an improved explicit bridge exponent. I did not find this dichotomy-preserving optimization in that bounded search. This does **not** establish worldwide novelty or priority.

The result remains **PARTIAL** with respect to Schramm Problem 2.1. It does not prove tightness of rescaled half-plane SAW, conformal invariance, uniqueness of subsequential limits, or identification with `SLE_{8/3}`. It only strengthens a source-relevant quantitative bridge observable.

No closure package is created. P26 and a second independent source-level audit remain pending; no source closure is claimed.

## 8. What should be attacked next

The previous R16 run already showed that bridge-height decay translates into a vertical renewal sparsity bound, but that vertical renewals alone do not control Euclidean annulus crossings because one irreducible bridge can make large lateral excursions.

The next run should therefore **not** spend its 90% research budget shaving another small constant from the same block induction. The next source-relevant milestone is a quantitative shape estimate for an irreducible critical bridge, for example an upper tail for horizontal span conditional on height, strong enough to feed an Aizenman–Burchard multi-crossing criterion.

Next methods, not used yet on I0036:

- **#12 FIND WHAT IS CONSERVED:** search the parafermionic surgery for an observable that survives conditioning on bridge height while controlling lateral span;
- **#20 FIND WHY THE ALGORITHM FAILS:** formulate the attempted annulus-crossing deduction from renewal levels and isolate the exact irreducible-bridge excursion event that breaks it;
- **#28 REPLACE FOR ALL WITH TYPICAL:** seek a high-probability aspect-ratio bound for a critical irreducible bridge rather than a deterministic one.

## 9. Model/reasoning and scheduler-control status

The situation is still the one recorded in `RESULTS.md` and `operations/NEW_METHODS_2026-09-16.md`: the exposed scheduler mutation surface has controls for task text/title, timing/schedule, enablement and timing mode, but no model-family field, no reasoning-effort field and no authenticated applied-effort telemetry. GPT-6/maximum can therefore be requested in prompt text only in this context.

To actually enforce GPT-6/maximum, an authorized product/workspace scheduler or API must expose those selectors and runtime telemetry, or the workspace/platform owner must migrate/repair the task to such a surface. A historical `You cannot modify this task` response is an ownership/context authorization failure, not a mathematical one; `RESULTS.md` records that P26 was later updated successfully from another authorized context. I made no scheduler change and did not attempt a permission bypass.

## 10. Structured ledger delta

```yaml
ledger_delta:
  track: R16
  lane: HARD_OUTSIDE
  target: I0036
  source: Schramm ICM 2006 Problem 2.1
  metric: epsilon_bridge
  before: 9e-10
  after: 1/42000000
  after_decimal: 2.380952380952381e-8
  movement: true
  unchanged_count_before: 1
  unchanged_count_after: 0
  status: PARTIAL_OPEN
  theorem_id: R16-I0036-C03
  theorem_scope: "critical hexagonal-lattice bridge partition function B_T <= 1000 T^(-1/42000000), all integer T>=1"
  finite_certificate:
    checker: artifacts/R16/2026-09-17T08-55-29Z_i0036_dichotomy_bridge_1over42m_check.py
    checker_commit: 8d5189f6964a5bc7452ffdb433fade8ebff11c24
    output: artifacts/R16/2026-09-17T08-55-29Z_i0036_dichotomy_bridge_1over42m_check.out
    output_commit: 4db14b984c111d8b935a5eaf84ab08859c5b5c24
    result: ALL_EXACT_CHECKS_PASS
  audits:
    P26: PENDING
    second_other_track: PENDING
  next_methods: [12, 20, 28]
```

No shared root ledger, peer-track file, email, Drive content, public post, purchase, permission, workflow or scheduler state was modified.
