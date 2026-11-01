# C0134 — regeneration bridge, life-cycle domination, and a stronger scalar theorem

Date: 2026-09-18  
Slot: R7-02 Finite Certificate Research  
Native ID: `6aabe797a39081919acc889f29f4c556`  
Repository / branch: private `yspennstate/math-open-problems` / existing `master`  
Target: `C0134` — Kosygina–Zerner Problem 5.3  
Classification: **CLOSABLE OUTSIDE**  
Mathematical status: **candidate source-level complete; operationally PARTIAL pending prior-art reconciliation and two independent audits**

## 1. Purpose of this note

The preceding artifact

`research7_2026-09-17/R7-02/artifacts/2026-09-18/2026-09-18T183000Z__C0134_convex_order_critical_closure.md`

proved the random-emigration statement `RE(2)` and then returned to the original cookie environment through a stationary-law comparison. The present run stress-tests that last bridge against the literal source and removes an unnecessary assumption from it.

The main new point is:

> **one never needs to prove that the original un-front-loaded backward branching chain has a finite-mean return cycle or even invoke its stationary law.**

Instead, the source's regeneration identities translate speed directly into the expected **single-cycle total progeny** of the backward chain. Front-loading gives a pathwise domination of entire killed life cycles, so the infinite cycle reward of the scalar random-emigration chain transfers immediately to the original unbounded cookie chain.

This run uses three new Section-B methods relative to the immediately preceding `B7/B21/B30` triple:

- **B3 — prove something stronger:** prove a scalar zero-speed theorem for every front-loaded emigration law with `1 < E N <= 2`, not only `E N=2`;
- **B12 — find what is conserved:** derive the exact stationary overshoot identity for any hypothetical finite-mean invariant law;
- **B18 — say it in another language:** translate the source ballisticity question exactly into finiteness/divergence of one backward-branching life-cycle reward.

The frozen source metric is already saturated at `M_clause=2/2`; therefore this run is **NO MOVEMENT** on that metric despite strengthening and repairing the proof architecture.

## 2. Literal source audit: where bounded depth is and is not used

Primary source: Elena Kosygina and Martin P. W. Zerner, *Excited random walks: results, methods, open problems*, arXiv:1204.1895v2 (2012; journal version 2013), Problem 5.3, printed p. 20.

The current arXiv v2 was re-read on 2026-09-18. Four source facts matter.

### 2.1 Recurrence/transience under positive cookies is already unbounded-stack

Theorem 3.10 has a branch `(3.9)` assuming `(SE)+(POS_1)` (apart from one explicit degenerate stack). Under that branch the walk is recurrent for `delta in [-1,1]`, transient right for `delta>1`, and transient left for `delta<-1`.

Thus for Problem 5.3's `(IID)+(WEL)+(POS_1)` setting, no `(BD)` hypothesis is needed to know that every `delta>1` case is right transient. The excluded deterministic stack `(1,1/2,1/2,...)` is incompatible with left `(WEL)` when it occurs with probability one, and in any case has `delta=1`, not the critical ballistic endpoint `delta=2`.

### 2.2 The strong law is also already unbounded-stack

Theorem 4.1 states that `(SE)+(POS_1)` implies a strong law with deterministic speed `v in [0,1]`. Hence every source-valid environment considered here has a speed before any branching argument begins.

### 2.3 Regeneration needs IID+WEL, not bounded depth

Lemma 4.5 gives the regeneration structure in dimension one under `(IID)+(WEL)` once right transience has positive probability. It also gives

`E[X_{tau_2}-X_{tau_1}] < infinity`.

Theorem 4.6 then gives

\[
 v = \frac{E[X_{\tau_2}-X_{\tau_1}]}{E[\tau_2-\tau_1]},
\]

with the convention that the ratio is zero when the denominator is infinite.

### 2.4 The backward-chain combinatorics precede the bounded-depth step

In the source's proof sketch of Theorem 5.2, the coin-tossing representation is introduced first. For each site `k`, let `F_m^(k)` be the number of failures before the `m`-th success in that site's cookie coin sequence, and define

\[
V_0=0,\qquad V_{j+1}=F_{V_j+1}^{(j)}.
\tag{2.1}
\]

The exact identification of the finite backward jump-count vector with `(V_0,...,V_n)` is derived before the bounded-cookie representation is used. The source invokes `(BD)` only afterward, when it writes all offspring past a deterministic cookie depth `M` as fair `Geom(1/2)` variables.

Therefore (2.1) itself, and the combinatorial relation of its life cycle to a regeneration block, are valid for an arbitrary positive infinite stack.

This is the key source-scope check: the present proof imports the source's regeneration machinery only at hypotheses where the source itself does not require `(BD)`.

## 3. B18 — exact translation: speed is a life-cycle total-progeny question

Let

\[
\sigma^V:=\inf\{j\ge1:V_j=0\},\qquad
A^V:=\sum_{j=0}^{\sigma^V-1}V_j.
\tag{3.1}
\]

For a right-transient iid environment, the usual backward-jump counting gives, for one regeneration block,

\[
\sigma^V\ \stackrel d=\ X_{\tau_2}-X_{\tau_1},
\tag{3.2}
\]

and

\[
A^V\ \stackrel d=
\frac{\tau_2-\tau_1-(X_{\tau_2}-X_{\tau_1})}{2}.
\tag{3.3}
\]

A direct derivation of (3.3) is useful because it makes clear there is no hidden depth assumption. During a nearest-neighbor path segment with net displacement `r`, every left jump must eventually be compensated by a right jump, so if `L` is the number of left jumps then the elapsed time is exactly `r+2L`. The backward process records, site by site, precisely those left jumps; summing the generation populations over a life cycle gives `L`. This proves (3.2)-(3.3) using only the coin-tossing construction, iid fresh stacks across successive spatial sites, and right transience.

Combining (3.2)-(3.3),

\[
\tau_2-\tau_1\ \stackrel d=\ \sigma^V+2A^V.
\tag{3.4}
\]

Lemma 4.5 gives `E sigma^V<infinity`, because its law is the regeneration displacement. Consequently Theorem 4.6 becomes the exact criterion

\[
\boxed{
 v
 =
 \frac{E\sigma^V}{E\sigma^V+2EA^V}
}
\tag{3.5}
\]

with the denominator allowed to be infinite. In particular,

\[
\boxed{v=0\quad\Longleftrightarrow\quad EA^V=\infty}
\tag{3.6}
\]

throughout the right-transient source branch.

This is the cleanest language for the endpoint. It eliminates any need to transfer an invariant distribution from the front-loaded chain to the original chain.

**B18 outcome: SUCCESS.** The original source problem is reduced exactly to a one-cycle reward divergence, at source-valid hypotheses.

## 4. Bernoulliization and front-loading at finite drift

Write the right-jump probability of the `i`-th cookie in a stack as `p_i>=1/2` and put

\[
d_i:=2p_i-1\in[0,1].
\tag{4.1}
\]

On an auxiliary probability space, independently over cookie indices conditionally on the stack, sample

\[
A_i\sim\operatorname{Bernoulli}(d_i).
\]

If `A_i=1`, make the `i`-th auxiliary coin a deterministic success; if `A_i=0`, make it a fair coin. Then

\[
P(\text{auxiliary success at }i\mid p_i)
=d_i+(1-d_i)/2=p_i,
\]

and independence across indices is preserved. Thus the entire conditional cookie coin sequence, hence every `F_m` and the backward chain (2.1), has exactly its original law after annealing over the auxiliary marks.

Let

\[
N:=\sum_{i\ge1}A_i.
\tag{4.2}
\]

When `delta=E\sum_i d_i<infinity`, Tonelli gives

\[
EN=\delta,
\tag{4.3}
\]

and in particular `N<infinity` almost surely.

The left-direction `(WEL)` condition implies

\[
P[p_i<1\ \forall i]>0.
\]

On this event, all `d_i<1`. Since `sum_i d_i<infinity` almost surely at finite `delta`, the product

\[
\prod_i(1-d_i)
\]

is strictly positive there. This product is exactly the conditional probability that every mark vanishes. Hence

\[
\boxed{P(N=0)>0.}
\tag{4.4}
\]

Now move all `N` deterministic-success marks to the front of the sequence while preserving the relative order of all fair coin outcomes. Moving a sure success to an earlier position cannot increase the number of failures before any prescribed success number. Repeating the move gives, simultaneously for every `m`,

\[
\boxed{F_m^{\rm front}\le F_m^{\rm orig}.}
\tag{4.5}
\]

After front-loading, the first `N` outcomes are sure successes and the remaining outcomes are fair. Therefore its backward chain is

\[
Z_{n+1}
=\sum_{j=1}^{(Z_n+1-N_n)_+}\xi_{n,j},
\tag{4.6}
\]

where `N_n` are iid copies of `N` and `xi` are iid geometric random variables on `{0,1,...}` with

\[
P(\xi=k)=2^{-(k+1)},\qquad E\xi=1.
\tag{4.7}
\]

Using the same site randomness, (4.5), the monotonicity of `m -> F_m`, and induction on generations give a pathwise comparison up to the first return of the front chain:

\[
V_n^{\rm orig}\ge Z_n^{\rm front}.
\tag{4.8}
\]

In particular the original chain cannot hit zero before the front chain, and therefore

\[
\boxed{
\sigma^{\rm orig}\ge\sigma^{\rm front},\qquad
A^{\rm orig}\ge A^{\rm front}
}
\tag{4.9}
\]

pathwise for the corresponding first life cycles.

This pathwise cycle comparison is the proof repair supplied by the present run.

## 5. Critical scalar theorem `RE(2)`, now stated in the form actually needed

We restate the previous convex-order result in a life-cycle form.

### Theorem 5.1 — critical random-emigration cycle divergence

Let `N` be any nonnegative integer-valued random variable such that

\[
EN=2,\qquad P(N=0)>0.
\tag{5.1}
\]

Let `Z` be (4.6), started from zero, and let

\[
\sigma:=\inf\{n\ge1:Z_n=0\},\qquad
A:=\sum_{n=0}^{\sigma-1}Z_n.
\tag{5.2}
\]

Then

\[
\boxed{EA=\infty.}
\tag{5.3}
\]

### Proof

Set `p_0=P(N=0)` and

\[
a=\min\{p_0/2,1/6\}.
\]

Define `N_*` by

\[
P(N_*=0)=a,\qquad
P(N_*=2)=1-3a,\qquad
P(N_*=3)=2a.
\tag{5.4}
\]

Then `EN_*=2`. Moreover `N_*<=_{cx}N`. Indeed, the two means agree and the integer stop-loss transforms satisfy

\[
E(N-1)_+=1+p_0\ge1+a=E(N_*-1)_+,
\]

\[
E(N-2)_+=E(2-N)_+=2p_0+P(N=1)\ge2a=E(N_*-2)_+,
\]

and for every integer `k>=3`, `E(N_*-k)_+=0<=E(N-k)_+`. Piecewise linearity between integer thresholds completes the convex-order proof.

For an increasing convex test function `phi`, let

\[
S_r:=\xi_1+\cdots+\xi_r,\qquad h(r):=E\phi(S_r).
\]

The increments `h(r+1)-h(r)` are nondecreasing because `S_r` is stochastically increasing and, for convex `phi`, the map

\[
x\mapsto E[\phi(x+\xi)-\phi(x)]
\]

is nondecreasing. Thus `h` is increasing and convex.

For an emigration law `L`, define

\[
(K_L\phi)(x)=E\phi(S_{(x+1-L)_+}).
\tag{5.5}
\]

For fixed `x`, `l -> h((x+1-l)_+)` is convex, while for fixed `l`, `x -> h((x+1-l)_+)` is increasing convex. Hence convex order gives

\[
K_{N_*}\phi(x)\le K_N\phi(x),
\]

and `K_N` preserves increasing convexity. If `D` denotes the chain with emigration `N_*`, induction therefore yields

\[
D_n\le_{icx}Z_n\qquad(n\ge0).
\tag{5.6}
\]

In particular

\[
E_0D_n\le E_0Z_n.
\tag{5.7}
\]

The law `N_*` is exactly the backward emigration law of the bounded iid cookie model having `N_*` deterministic-right cookies followed by fair cookies. This environment has depth at most three, drift two, and satisfies source `(WEL)` because `P(N_*=0)=a>0`. The source bounded theorem gives speed zero at drift two. The source regeneration identity (3.5) therefore gives infinite expected cycle reward for `D`.

The same bounded theory gives `E sigma_D<infinity`; hence the renewal-reward formula for its positive recurrent atom at zero gives an invariant law `pi_*` with

\[
E_{\pi_*}D
=\frac{E_0\sum_{n<\sigma_D}D_n}{E_0\sigma_D}
=\infty.
\tag{5.8}
\]

The comparator is aperiodic because it has a positive one-step return probability to zero. Therefore its law from zero converges to `pi_*`. For each `R`, bounded convergence on the countable state space gives

\[
E_0(D_n\wedge R)\to E_{\pi_*}(D\wedge R),
\]

and then `R->infinity` shows

\[
E_0D_n\to\infty.
\tag{5.9}
\]

The arbitrary critical `Z` is positive recurrent. Choose `M` so large that

\[
E(N\wedge M)>1.
\]

The chain with bounded emigration `N\wedge M` is the backward chain of a bounded positive-cookie environment with drift greater than one; the bounded source branching theorem gives it finite mean return time. Since `N>=N\wedge M`, the chain with emigration `N` is pathwise no larger and returns to zero no later.

Let `pi_N` be its invariant law. If `E_{pi_N}Z<infinity`, stochastic monotonicity in the population state allows a zero-started chain to be coupled below a stationary-started chain, so

\[
E_0Z_n\le E_{\pi_N}Z<\infty
\]

uniformly in `n`. This contradicts (5.7) and (5.9). Thus

\[
E_{\pi_N}Z=\infty.
\tag{5.10}
\]

Finally the renewal-reward identity at state zero gives

\[
E_{\pi_N}Z
=\frac{E_0A}{E_0\sigma}.
\]

The denominator is finite by positive recurrence, so (5.10) forces `E_0A=infinity`. This proves (5.3). QED.

The theorem is exactly the previous `RE(2)`, but the cycle-reward conclusion is what is needed for the literal source bridge.

## 6. B3 — stronger theorem for every `1 < E N <= 2`

The critical theorem extends immediately to all transient subcritical-ballisticity means without any cookie-coordinate strengthening.

### Theorem 6.1 — scalar front-loaded zero-speed range

Let `N` be nonnegative integer-valued with

\[
1<\mu:=EN\le2,\qquad P(N=0)>0,
\tag{6.1}
\]

and let `Z` be (4.6). Then its first-cycle total progeny satisfies

\[
\boxed{EA=\infty.}
\tag{6.2}
\]

### Proof

If `mu=2`, this is Theorem 5.1. Suppose `1<mu<2`. Pick an integer

\[
L>2-\mu
\]

and an independent Bernoulli variable `B` with

\[
P(B=1)=q:=\frac{2-\mu}{L}\in(0,1).
\]

Define

\[
N^+:=N+LB.
\tag{6.3}
\]

Then

\[
EN^+=2,
\qquad
P(N^+=0)=P(N=0)(1-q)>0,
\tag{6.4}
\]

and `N^+>=N` pathwise.

Use the same geometric offspring variables for the two chains. Since more emigration means fewer reproducing particles,

\[
Z_n^{(N)}\ge Z_n^{(N^+)}
\]

up to the first return of the `N^+` chain. Hence

\[
\sigma_N\ge\sigma_{N^+},
\qquad
A_N\ge A_{N^+}
\]

pathwise. Theorem 5.1 gives `EA_{N^+}=infinity`; therefore `EA_N=infinity`. QED.

This stronger scalar result subsumes the earlier finite-coordinate strengthening route for the entire transient zero-speed interval `1<delta<=2`.

**B3 outcome: SUCCESS.** The endpoint theorem self-propagates downward in `delta` through an explicit emigration augmentation.

## 7. B12 — the conserved stationary overshoot identity

The scalar chain also has a simple exact invariant that is useful for checking any proposed finite-mean stationary calculation.

Suppose the front-loaded chain with `mu=EN>1` has an invariant law `pi` with finite first moment, and let `Z~pi` be independent of the next emigration variable `N`. Since the offspring mean is one,

\[
E[Z_{n+1}\mid Z,N]=(Z+1-N)_+.
\]

Use the identity

\[
(z+1-n)_+=z+1-n+(n-z-1)_+.
\tag{7.1}
\]

Stationarity and integrability then give

\[
EZ
=EZ+1-\mu+E(N-Z-1)_+,
\]

or

\[
\boxed{E(N-Z-1)_+=\mu-1.}
\tag{7.2}
\]

At the critical mean `mu=2`, every hypothetical finite-mean invariant law would have to satisfy

\[
E(N-Z-1)_+=1.
\tag{7.3}
\]

For the three-point comparator (5.4), (7.3) becomes the finite boundary identity

\[
\boxed{\pi(0)(1+a)+2a\,\pi(1)=1.}
\tag{7.4}
\]

This identity is not by itself a contradiction, so B12 does not replace the convex-order theorem. It is nevertheless an exact invariant and an independent diagnostic: any proposed finite-mean stationary formula failing (7.2) is automatically wrong.

**B12 outcome: exact invariant found; diagnostic only, not a closure route by itself.**

## 8. Return to Problem 5.3 with no stationary-law assumption on the original chain

We can now prove the positive source statement by cases.

### 8.1 `0 <= delta <= 1`

Under `(IID)+(WEL)+(POS_1)`, source Theorem 3.10 applies through its `(SE)+(POS_1)` branch and gives recurrence. Source Theorem 4.1 gives existence of a deterministic speed. A recurrent nearest-neighbor walk visits the origin infinitely often, so along that subsequence `X_n/n=0`; hence the deterministic speed is

\[
\boxed{v=0.}
\tag{8.1}
\]

### 8.2 `1 < delta <= 2`

Bernoulliization produces an iid site emigration count `N` with

\[
EN=\delta,\qquad P(N=0)>0.
\]

Theorem 6.1 gives infinite expected total progeny for the front-loaded cycle:

\[
EA^{\rm front}=\infty.
\]

The pathwise life-cycle domination (4.9) gives

\[
EA^{\rm orig}\ge EA^{\rm front}=\infty.
\]

Source Theorem 3.10 gives right transience, Lemma 4.5 gives finite expected regeneration displacement, and the exact translation (3.5) gives

\[
\boxed{v=0.}
\tag{8.2}
\]

No stationary law for the original un-front-loaded backward chain is invoked.

### 8.3 `delta>2`, including `delta=infinity`

Define the finite-depth truncation

\[
p_i^{(M)}=
\begin{cases}
p_i,&i\le M,\\1/2,&i>M.\end{cases}
\]

Its drift is

\[
\delta_M=E\sum_{i=1}^M(2p_i-1)\uparrow\delta.
\]

Choose `M` with `delta_M>2`. The truncated law is iid, bounded depth, and weakly elliptic; Theorem 5.2 gives a positive speed `v_M>0`. The original cookie environment is coordinatewise stronger than its truncation, both laws have strong laws by Theorem 4.1, and source Proposition 4.2 gives

\[
\boxed{v\ge v_M>0.}
\tag{8.3}
\]

Combining (8.1)-(8.3),

\[
\boxed{
\delta\le2\Longrightarrow v=0,
\qquad
\delta>2\Longrightarrow v>0
}
\tag{8.4}
\]

under the full positive-cookie source hypotheses `(IID)+(WEL)+(POS_1)`.

This is precisely the positive branch obtained by replacing `(BD)` with `(POS_1)` in source Theorem 5.2, which is what Problem 5.3 asks in the only branch compatible with `(POS_1)`.

## 9. What this run fixes relative to the previous closure artifact

The previous artifact's final bridge said that infinite invariant mean of the front-loaded chain, together with stationary domination, forces infinite invariant mean of the original critical backward chain. That route is plausible but asks for more Markov-chain structure on the original unbounded backward chain than is necessary.

The present argument replaces it with the strictly simpler chain of implications

\[
EA^{\rm front}=\infty
\stackrel{\text{pathwise cycle domination}}{\Longrightarrow}
EA^{\rm orig}=\infty
\stackrel{\text{source regeneration}}{\Longrightarrow}
v=0.
\]

All three arrows are source-valid without a bounded-depth assumption. This removes the only proof-engineering concern found in the exact source reread.

A second simplification is that `delta<2` no longer needs a finite-coordinate cookie strengthening. The scalar augmentation `N -> N+LB` proves the full `1<delta<2` range directly after Bernoulliization.

## 10. Prior-art check, 2026-09-18

Fresh bounded searches were run for the literal Kosygina–Zerner Problem 5.3, unbounded positive cookies and the `delta=2` ballisticity threshold, and critical branching processes with random emigration.

Relevant hits:

1. **Omar Chakhtoun, 2019 dissertation, _One-Dimensional Excited Random Walk with Unboundedly Many Excitations Per Site_.** Its public CUNY abstract explicitly says the model requires a **tail decay estimate on the number of excitations per site**. Thus its public statement is a restricted unbounded-stack theorem, not evidence for the unrestricted `(IID)+(WEL)+(POS_1)` source scope here.
2. **Nicholas Travers, 2018, _Excited Random Walk in a Markovian Environment_.** This extends thresholds to a substantial Markovian-environment class and explicitly contrasts it with the more general stationary-ergodic setting. It is not an unrestricted iid arbitrary-positive-stack resolution identified by the search.
3. **Kosygina–Peterson, 2015, _Excited random walks with Markovian cookie stacks_.** This treats finite-state Markovian structure within each iid site stack, a structured infinite-stack class rather than arbitrary positive stacks.
4. **Carper, 2026, geometric-emigration preprint.** This concerns the special geometric-emigration family already isolated in the preceding R7-02 run.
5. Classical branching-with-migration literature includes Vatutin's critical Galton–Watson process with emigration and Yanev–Mitov's random migration processes. Publicly indexed descriptions expose models with specific migration mechanisms (for example migration in `{-1,0,1}` in the Yanev–Mitov life-period paper), not yet a theorem whose displayed hypotheses subsume arbitrary nonnegative `N` in (4.6).

This remains **bounded search evidence only**. In particular, the full hypotheses of the classical emigration papers and the complete Chakhtoun dissertation still need direct comparison before any novelty claim. This note makes no novelty claim.

## 11. Metric, status, and next attack

Frozen metric:

`M_clause` = number of the two full source clauses proved under complete `(IID)+(WEL)+(POS_1)` hypotheses.

Before this run: `2/2`.  
After this run: `2/2`.

\[
\boxed{M_{\rm clause}:2/2\to2/2\quad\text{NO MOVEMENT}.}
\]

The ordinary unchanged-research count therefore advances from `0` to `1`, even though the proof architecture is materially stronger.

Mathematical status remains **candidate source-level complete**. Operational status remains **PARTIAL** because owner closure additionally requires a dated prior-art reconciliation, an actual independent P26 audit, a distinct OTHER-track audit, and the final self-contained paper package with those corrections integrated.

The next nonrepeating mathematical/prior-art attack should use **B4 / B22 / B27**:

- B4: prove a small self-contained direct version of the life-cycle theorem without stationary distributions, to see whether the convex-order stationary detour can be eliminated entirely;
- B22: read the failure/limitation hypotheses in the classical emigration literature and Chakhtoun's dissertation rather than relying on abstracts;
- B27: swap the quantifiers in the Bernoulliization/front-loading step and test whether a quenched per-stack comparison is possible, isolating exactly where annealing over stacks is essential.
