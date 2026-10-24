Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding selector is exposed.

# C0134 — critical random-emigration theorem by convex order

Run date: 2026-09-18. Slot: `R7-02`. Canonical target: `C0134`.

Captured run-start master: `faef3a064e4ebc94c0414d616fd4da79138e3008`.
Fresh ownership recheck before delivery: master `311bf135f62608a39dee0f009ea4fda297685fc2`; `operations/claims/C0134.md` still names R7-02 / native ID `6aabe797a39081919acc889f29f4c556`.
Previous substantive report: `research7_2026-09-17/R7-02/runs/2026-09-18/2026-09-18T173512Z__report.md`.
Previous main artifact: `research7_2026-09-17/R7-02/artifacts/2026-09-18/2026-09-18T173258Z__C0134_frontloading_reduction_and_geometric_emigration.md` @ creation commit `73e81758400e788e06a1787a153458b38d0ac384`.

## 1. Source target and cumulative state

Kosygina–Zerner, *Excited random walks: results, methods, open problems*, arXiv:1204.1895v2 (2012; journal version 2013), Problem 5.3, asks whether the bounded-cookie assumption `(BD)` in Theorem 5.2 can be replaced by `(POS1)` while retaining `(IID)+(WEL)`. In the positive one-dimensional branch the full source target is

\[
\delta\le 2\Longrightarrow v=0,
\qquad
\delta>2\Longrightarrow v>0,
\]

where

\[
\delta=\mathbb E\sum_{i\ge1}(2p_i-1),\qquad p_i=\omega(0,+1,i)\ge \frac12.
\]

The preceding R7-02 work already proved:

1. the full `delta>2` clause, including `delta=+infinity`, by finite-depth monotone truncation;
2. every finite `delta<2` zero-speed case follows from the single endpoint `delta=2` by strengthening finitely many cookie coordinates to a critical environment and using speed monotonicity;
3. at `delta=2`, Bernoulliization plus front-loading reduces the endpoint to the scalar random-emigration statement `RE(2)` below.

The frozen metric before this run is therefore `M_clause=1/2`.

## 2. The exact remaining scalar statement

Let `N` be an arbitrary nonnegative integer-valued random variable satisfying

\[
\mathbb E N=2,\qquad \mathbb P(N=0)>0.
\]

Let `xi_{n,j}` be iid geometric random variables on `{0,1,2,...}` with

\[
\mathbb P(\xi=k)=2^{-(k+1)},\qquad \mathbb E\xi=1,
\]

independent of iid copies `N_n` of `N`. Define

\[
Z_{n+1}=\sum_{j=1}^{(Z_n+1-N_n)_+}\xi_{n,j}. \tag{RE}
\]

The previous run proved that the critical source clause is equivalent to:

> **RE(2).** The positive recurrent chain (RE) has invariant law `pi_N` with
> \[
> \mathbb E_{\pi_N} Z=+\infty.
> \]

This file proves RE(2) for every allowed `N`.

# Method B7 — why a direct truncation limit is the wrong closure mechanism

A first idea is to truncate `N` and try to pass the bounded critical theorem to a limit. That does not by itself control the invariant first moment. Infinite means are not stable under weak convergence: a sequence of probability laws can have infinite first moment for every index and still converge weakly to a finite-mean law. Thus even a perfect finite-dimensional convergence argument for truncated stationary chains would leave exactly the quantity needed for speed uncontrolled unless one also proves a truncation-uniform lower tail.

Rather than manufacture such a tail estimate, the useful conclusion is to seek **one bounded critical law which is below every admissible `N` in the order naturally preserved by the branching kernel**. This converts the limiting problem into a finite comparison problem.

Outcome: the naive B7 limit route is rejected, but it identifies the right replacement object.

# Method B21 — import increasing-convex order into the random-emigration kernel

The relevant order is increasing-convex order after one reverses emigration into the number of surviving progenitors.

## 3. A universal bounded critical comparator

Put

\[
p_0:=\mathbb P(N=0)>0,
\qquad
a:=\min\left\{\frac{p_0}{2},\frac16\right\}>0.
\]

Define a bounded random variable `N_*` by

\[
\mathbb P(N_*=0)=a,
\qquad
\mathbb P(N_*=2)=1-3a,
\qquad
\mathbb P(N_*=3)=2a. \tag{3.1}
\]

Then `N_*` is supported on `{0,2,3}`, has `P(N_*=0)=a>0`, and

\[
\mathbb E N_*=2(1-3a)+3(2a)=2. \tag{3.2}
\]

### Lemma 3.1 — `N_*` is below `N` in convex order

\[
\boxed{N_*\le_{cx}N.} \tag{3.3}
\]

**Proof.** Both variables have mean two. For nonnegative integer-valued variables, equal means plus the stop-loss inequalities

\[
\mathbb E[(X-k)_+]\le \mathbb E[(Y-k)_+],\qquad k=0,1,2,\ldots, \tag{3.4}
\]

are equivalent to `X<=cx Y`. This follows directly from the discrete representation of a convex function as an affine function plus a nonnegative linear combination of the hinges `(x-k)_+` (equivalently, from the nonnegativity of its second differences).

For `k=0`, both stop-loss transforms equal the common mean `2`.
For `k=1`,

\[
\mathbb E[(N-1)_+]
=\mathbb E N-\mathbb P(N\ge1)
=1+p_0,
\]

whereas

\[
\mathbb E[(N_*-1)_+]=(1-3a)+2(2a)=1+a\le1+p_0.
\]

For `k=2`, equality of the mean to two gives

\[
\mathbb E[(N-2)_+]=\mathbb E[(2-N)_+]=2p_0+\mathbb P(N=1)\ge2a,
\]

while

\[
\mathbb E[(N_*-2)_+]=2a.
\]

For every integer `k>=3`, the left side for `N_*` is zero. The real-threshold inequalities follow by linear interpolation between consecutive integers because stop-loss transforms of integer-valued laws are affine on each interval `[k,k+1]`. This proves (3.3). `□`

## 4. Random sums turn convex order of emigration into increasing-convex order of population

Let

\[
S_r:=\xi_1+\cdots+\xi_r,\qquad S_0=0,
\]

with iid nonnegative geometric `xi_j` as above. For a nonnegative increasing convex function `phi` on the nonnegative integers define

\[
h(r):=\mathbb E\,\phi(S_r). \tag{4.1}
\]

### Lemma 4.1 — `h` is increasing and convex on the nonnegative integers

It is increasing because `S_{r+1}=S_r+xi_{r+1}>=S_r` under the natural coupling.

For convexity, set

\[
g(s):=\mathbb E[\phi(s+\xi)-\phi(s)].
\]

For each fixed `k>=0`, convexity of `phi` implies

\[
s\mapsto \phi(s+k)-\phi(s)
\]

is nondecreasing; averaging over `xi` shows that `g` is nondecreasing. Hence

\[
h(r+1)-h(r)=\mathbb E g(S_r)
\]

is nondecreasing in `r`, because `S_{r+1}>=S_r` under the same coupling. Thus `h` is convex. `□`

For an emigration law `L`, write its one-step operator as

\[
(K_L\phi)(x)
:=\mathbb E\,\phi\left(S_{(x+1-L)_+}\right). \tag{4.2}
\]

### Lemma 4.2 — pointwise kernel comparison

For every increasing convex `phi`,

\[
\boxed{K_{N_*}\phi(x)\le K_N\phi(x)\quad\text{for all }x\ge0.} \tag{4.3}
\]

**Proof.** By Lemma 4.1, `h` is increasing and convex. For fixed `x`,

\[
q_x(n):=(x+1-n)_+
\]

is convex in `n`. Since composition of a convex nondecreasing function with a convex function is convex,

\[
n\mapsto h(q_x(n))
\]

is convex. Apply `N_*<=cx N`. `□`

### Lemma 4.3 — both kernels preserve increasing convexity in the state

If `phi` is increasing convex, then `x -> K_L phi(x)` is increasing convex for every emigration law `L`.

**Proof.** For fixed `l`, `x -> (x+1-l)_+` is increasing convex. Compose with the increasing convex `h` from Lemma 4.1 and then average in `l`. `□`

### Proposition 4.4 — finite-time increasing-convex domination

Let `D` be the chain with emigration `N_*`, and `Z` the chain with emigration `N`, both started at zero. Then for every `n`,

\[
\boxed{D_n\le_{icx} Z_n.} \tag{4.4}
\]

**Proof.** At time zero the laws agree. Suppose the order holds at time `n`. For increasing convex `phi`, Lemma 4.2 and then Lemma 4.3 give

\[
\begin{aligned}
\mathbb E\phi(D_{n+1})
&=\mathbb E[(K_{N_*}\phi)(D_n)]\\
&\le \mathbb E[(K_N\phi)(D_n)]\\
&\le \mathbb E[(K_N\phi)(Z_n)]\\
&=\mathbb E\phi(Z_{n+1}).
\end{aligned}
\]

Induction proves (4.4). In particular, taking `phi(x)=x`,

\[
\mathbb E_0 D_n\le \mathbb E_0 Z_n \quad\text{for every finite }n. \tag{4.5}
\]
`□`

# Method B30 — localize all unbounded emigration into a three-point bounded model

The preceding order comparison becomes decisive because `N_*` is itself a source-valid bounded cookie environment.

## 5. The comparator is exactly a bounded critical cookie model

At each site, sample `N_*` independently. Put deterministic-right cookies in positions `1,...,N_*` and fair cookies thereafter. Then:

- `(IID)` holds by construction;
- `(BD)` holds with deterministic bound `M=3`;
- `(POS1)` holds;
- the drift parameter is
  \[
  \delta_*=\mathbb E N_*=2;
  \]
- `(WEL)` holds in the exact Kosygina–Zerner sense. For the `+1` direction all transition probabilities are positive. For the `-1` direction, on the event `N_*=0` (probability `a>0`) every cookie is fair, so every left transition probability is positive.

Its backward branching chain is exactly `D`.

By the published bounded-cookie Theorem 5.2, this ERW has speed zero at `delta_*=2`. By the standard backward-branching speed identity used in the proof of that theorem,

\[
v_* = \frac{1}{1+2\,\mathbb E_{\pi_*}D}
\]

when the invariant first moment is finite, while an infinite invariant first moment gives zero speed. Hence

\[
\boxed{\mathbb E_{\pi_*}D=+\infty.} \tag{5.1}
\]

The chain `D` is irreducible: from zero, the event `N_*=0` followed by one geometric offspring reaches every nonnegative state with positive probability, and from any state all geometric offspring can be zero. It is aperiodic because `P_0(D_1=0)>0`. Since `delta_*=2>1`, the standard bounded backward-BLP theorem gives positive recurrence. Therefore

\[
\mathcal L_0(D_n)\longrightarrow \pi_*.
\]

For each cutoff `R`, bounded convergence on the countable state space gives

\[
\mathbb E_0[D_n\wedge R]\longrightarrow \mathbb E_{\pi_*}[D\wedge R]. \tag{5.2}
\]

Since the right side increases to `+infinity` as `R->infinity`, (5.2) implies

\[
\boxed{\mathbb E_0D_n\longrightarrow+\infty.} \tag{5.3}
\]

Indeed, given `A<infinity`, choose `R` with `E_{pi_*}(D wedge R)>2A`, then take `n` large enough that the left side of (5.2) exceeds `A`.

## 6. RE(2) follows for every integrable critical emigration law

For arbitrary `N` with `EN=2` and `P(N=0)>0`, the previous R7-02 run established positive recurrence of (RE): choose `M` with `E[min(N,M)]>1`; the corresponding bounded-emigration chain is positive recurrent, and the full `N` chain is pathwise no larger and returns to zero no later. Let its invariant law be `pi_N`.

The kernel is stochastically monotone in the state: if `x<=y`, use the same `N` and the same geometric sequence; then

\[
(x+1-N)_+\le(y+1-N)_+
\]

and the random sum from `x` is no larger than that from `y`.

Assume for contradiction that

\[
\mathbb E_{\pi_N}Z<\infty. \tag{6.1}
\]

Couple a chain `Z^(0)` started from zero with a stationary chain `Z^(pi)` started from `pi_N`, using the same randomness. Since `0<=Z_0^(pi)`, monotonicity gives

\[
Z_n^{(0)}\le Z_n^{(\pi)}\quad\text{for all }n,
\]

and therefore

\[
\mathbb E_0 Z_n\le \mathbb E_{\pi_N}Z<\infty
\quad\text{uniformly in }n. \tag{6.2}
\]

But Proposition 4.4 and (5.3) give

\[
\mathbb E_0 Z_n\ge \mathbb E_0D_n\longrightarrow+\infty, \tag{6.3}
\]

contradicting (6.2). Hence

\[
\boxed{\mathbb E_{\pi_N}Z=+\infty.} \tag{6.4}
\]

This proves RE(2) in full.

## 7. Return from RE(2) to the original critical cookie environment

For completeness, recall the exact reduction from the preceding run.

For a critical positive stack put

\[
d_i=2p_i-1\in[0,1],
\]

and, conditional on the stack, independently mark cookie `i` with

\[
A_i\sim\mathrm{Bernoulli}(d_i).
\]

A marked cookie is treated as deterministic-right and an unmarked cookie as fair. Mixing gives exactly the original Bernoulli success probability

\[
d_i+(1-d_i)/2=p_i,
\]

so this enlargement does not change the ERW or backward-BLP law. Let

\[
N=\sum_i A_i.
\]

Tonelli gives `EN=delta=2`, hence `N<infinity` almost surely. The source `(WEL)` condition in the left direction says that with positive probability every original left transition probability is positive, i.e. every `p_i<1`. On that event every `d_i<1`; since `sum_i d_i<infinity` almost surely, the infinite product

\[
\prod_i(1-d_i)
\]

is positive. It is the conditional probability of `N=0`, so

\[
P(N=0)>0.
\]

Now move all deterministic successes to the front, preserving the order of fair coins. Every prefix then has at least as many successes as before, so for every required success count `m`,

\[
F_m^{\rm front}\le F_m^{\rm original}.
\]

Thus the front-loaded backward chain is pathwise no larger than the original one. RE(2) gives infinite invariant mean for the front chain. The same finite-time/stationary comparison used in Section 6 forces infinite invariant mean for the original critical backward chain. Hence the critical ERW has

\[
\boxed{v=0\qquad(\delta=2).} \tag{7.1}
\]

## 8. The two remaining parameter regimes

### 8.1 `delta<2`

The preceding run constructed a source-valid critical strengthening of any finite-`delta<2` environment by changing only finitely many cookie coordinates. One convenient form is

\[
p_i^+=p_i+a_i(1-p_i),\qquad 0\le a_i\le\frac12,
\]

for finitely many indices, chosen so that

\[
\sum_i a_i\,\mathbb E[1-(2p_i-1)]=2-\delta.
\]

Because `sum_i E[2p_i-1]=delta<infinity`, the terms `E[1-(2p_i-1)]` tend to one, so such a finite choice exists. The strengthening remains `(IID)+(WEL)+(POS1)` and has drift two. Monotonicity of speed gives

\[
0\le v\le v^+=0,
\]

so `v=0` for every `delta<2`.

### 8.2 `delta>2`, including `delta=+infinity`

Put

\[
\delta_M=\mathbb E\sum_{i=1}^M(2p_i-1).
\]

By monotone convergence `delta_M` increases to `delta`; hence some finite `M` has `delta_M>2`. Replace all cookies after `M` by fair cookies. The resulting bounded environment has positive speed by Theorem 5.2. The original environment dominates it, so speed monotonicity gives `v>0`.

Combining the three regimes yields the full source statement:

\[
\boxed{
\delta\le2\iff v=0,
\qquad
\delta>2\iff v>0,
}
\]

under `(IID)+(WEL)+(POS1)` in the positive branch requested by Problem 5.3.

Accordingly the frozen mathematical metric moves

\[
\boxed{M_{\rm clause}:1/2\longrightarrow2/2.}
\]

This is a **candidate complete source-level proof**, not yet an operational `PROVED` closure under the owner protocol: independent audits and full prior-art reconciliation are still required.

# 9. Dated prior-art check — 2026-09-18

The original/current source remains Kosygina–Zerner, arXiv:1204.1895v2, where Theorem 5.2 assumes `(IID)+(BD)+(WEL)` and Problem 5.3 asks whether `(BD)` can be replaced by `(POS1)`.

The bounded search in this run found the following relevant later work.

1. **Omar Chakhtoun, 2019 dissertation, _One-Dimensional Excited Random Walk with Unboundedly Many Excitations Per Site_.** Its public abstract says it assumes a **tail decay estimate** on the number of excitations per site and obtains ballisticity/zero-speed criteria in that wider class. This is important prior art but does not, at abstract level, state the assumption-free `(IID)+(WEL)+(POS1)` result proved above. Full-thesis theorem-by-theorem comparison is still required before any novelty claim.
2. **Tuan-Minh Nguyen, 2022, _Speed of Excited Random Walks with Long Backward Steps_.** The paper proves a critical multi-type Galton–Watson theorem with deterministic emigration vector and uses it to solve its own `delta=2` model. It is structurally close but not the arbitrary random-emigration statement RE(2).
3. **Patrick Carper, arXiv:2609.06311 (submitted 2026-09-05), _A Branching Process with Geometric Emigration and the “Have Your Cookie and Eat It” Random Walk_.** It treats geometric emigration, matching the exact special family solved in the preceding R7-02 run, not arbitrary integrable `N`.
4. Classical branching-with-emigration papers by Vatutin (1977/1978 translation), Kaverin (1991 translation), Nagaev–Khan, and Yanev–Mitov are close enough that their exact hypotheses and conclusions must be inspected before claiming that RE(2), or the convex-order reduction, is new.

No bounded search located a later source explicitly stating a full resolution of Kosygina–Zerner Problem 5.3 with **no tail assumption** beyond `(IID)+(WEL)+(POS1)`. That is negative evidence only and is not a novelty certificate.

# 10. Method outcomes and next obligations

- **B7 (take the limit):** direct truncation does not preserve the critical infinite stationary mean without a uniform tail estimate; rejected as the closing mechanism.
- **B21 (import a technique):** increasing-convex/stop-loss order gives a kernel order respected by the random-sum branching transition.
- **B30 (localize/glue):** every admissible critical emigration law dominates, in the needed kernel order, a single bounded three-point critical law `{0,2,3}`. The bounded theorem then forces divergence for the arbitrary law.

Mathematical status: **candidate source-level complete proof; operationally PARTIAL pending closure protocol**.

Remaining non-mathematical/source-validation obligations before `PROVED` may be entered by the coordinator:

1. full prior-art reconciliation, especially Chakhtoun 2019 and the classical random-emigration literature;
2. actual independent P26 audit;
3. one distinct OTHER-track independent audit;
4. self-contained source-scoped paper package and audit of every imported source theorem/hypothesis.

No finite computational core is used in the closing argument; therefore no exact-arithmetic checker is mathematically applicable to the proof itself.
