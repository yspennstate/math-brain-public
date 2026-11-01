# C0134 — direct cycle-reward proof, global stackwise coupling, and prior-art risk map

Date: 2026-09-18  
Slot: R7-02  
Target: C0134 — Kosygina–Zerner, *Excited random walks: results, methods, open problems*, Problem 5.3  
Run-start master: `6a41a631247300f5812aeb9b8f3f2095ba9a8392`  
Fresh pre-delivery master inspected: `038d0cb1a35767c0a1343f35464c774a1075aa07`  
Frozen metric: `M_clause = 2/2` before this artifact and `2/2` after it.  
Methods: **B4 / B22 / B27**.

This note strengthens the existing candidate source-level proof.  It does **not** change the source metric because both source clauses were already proved in the preceding run.  Its main purpose is to remove invariant-law machinery from the critical random-emigration comparison and to make the Bernoulliization/front-loading step a single stackwise coupling valid simultaneously for every success level and every generation.

## 1. Source endpoint already isolated

For the positive-cookie branch of Problem 5.3 the source asks whether the bounded-depth hypothesis `(BD)` in Theorem 5.2 can be replaced by `(POS1)`, retaining `(IID)+(WEL)`.  Since `(POS1)` forces nonnegative total drift, the source-matching statement is

\[
\delta\le 2\Longrightarrow v=0,
\qquad
\delta>2\Longrightarrow v>0.
\tag{1}
\]

The supercritical clause was already proved by finite-depth truncation and monotonicity.  The recurrent range `0<=delta<=1` is already covered by the source recurrence theorem plus its deterministic strong law.  The only nontrivial range is therefore `1<delta<=2`.

The preceding reports reduced that range to a scalar chain.  This note makes that reduction and its critical proof more robust.

# Method B27 — swap the quantifiers: one stackwise coupling works for all success levels at once

## 2. Bernoulliization of one deterministic positive stack

Fix a deterministic cookie stack

\[
p=(p_i)_{i\ge1},\qquad p_i\in[1/2,1],
\]

and write

\[
d_i:=2p_i-1\in[0,1].
\]

On one probability space take independent marks and fair bits

\[
A_i\sim\operatorname{Bernoulli}(d_i),
\qquad
C_i\sim\operatorname{Bernoulli}(1/2),
\]

with the two families independent.  Define

\[
B_i:=A_i+(1-A_i)C_i.
\]

Then, conditional on `p`, the variables `B_i` are independent and

\[
P(B_i=1\mid p)=d_i+(1-d_i)/2=p_i.
\]

Thus `(B_i)` is exactly the original cookie-toss sequence in law.

Let

\[
N:=\sum_{i\ge1}A_i.
\tag{2}
\]

When the stack has finite total drift, `N<infinity` almost surely.

Delete the deterministic-success marks from their original positions, retain the fair bits `C_i` with `A_i=0` in their original relative order, and place the `N` deterministic successes before that fair subsequence.  Conditional on the marks, the retained fair subsequence is still an iid fair sequence and is independent of `N` because the marks use only the `A_i` while the values use only the independent `C_i`.

Denote by `F_m^orig` the number of failures before the `m`-th success in `(B_i)`.  Denote by

\[
G_r:=\xi_1+\cdots+\xi_r,
\qquad G_0:=0,
\]

the failures before the `r`-th success in the retained fair sequence, where the gaps `xi_j` are iid geometric on `{0,1,2,...}` with

\[
P(\xi_j=k)=2^{-(k+1)},\qquad E\xi_j=1.
\]

### Lemma 2.1 (simultaneous front-loading inequality)

On the coupling above,

\[
\boxed{
F_m^{\rm orig}\ge G_{(m-N)_+}
\quad\text{for every }m\ge1
}
\tag{3}
\]

simultaneously.

### Proof

Move the deterministic-success symbols leftward one adjacent transposition at a time, always swapping a deterministic success past the symbol immediately preceding it.  Such a swap cannot decrease the number of successes in any prefix of the sequence.  Therefore, after every swap, the location of the `m`-th success can only move left, so the number of failures preceding that success can only decrease.  Once every deterministic success has been moved to the front, the first `N` successes require zero failures, and for `m>N` the remaining requirement is exactly the `(m-N)`-th success of the retained fair sequence.  Its failure count is `G_{m-N}`.  This proves (3) for all `m` on the same realization.  ∎

The point of (3) is the quantifier order: this is not a separate stochastic comparison for each fixed `m`; one realization satisfies every `m` simultaneously.

## 3. Global generation-by-generation coupling

Apply the construction independently at each site/generation.  Let `N_n` be the number of deterministic marks at generation `n`, and let `G_n(r)` be the corresponding fair failure sum.  Define the scalar front-loaded chain

\[
Z_0=0,
\qquad
Z_{n+1}=G_n\bigl((Z_n+1-N_n)_+\bigr).
\tag{4}
\]

Let `V` be the original Bernoulliized backward chain,

\[
V_0=0,
\qquad
V_{n+1}=F^{\rm orig,n}_{V_n+1}.
\tag{5}
\]

### Lemma 3.1 (global domination)

The two chains may be coupled so that

\[
\boxed{V_n\ge Z_n\quad\text{for every }n\ge0}
\tag{6}
\]

on every realization.

### Proof

The claim is true at `n=0`.  Suppose `V_n>=Z_n`.  By (3), applied at generation `n`,

\[
V_{n+1}
=F^{\rm orig,n}_{V_n+1}
\ge
G_n((V_n+1-N_n)_+).
\]

The map `r -> G_n(r)` is nondecreasing, hence

\[
G_n((V_n+1-N_n)_+)
\ge
G_n((Z_n+1-N_n)_+)
=Z_{n+1}.
\]

Induction proves (6).  ∎

Let

\[
\sigma_X:=\inf\{n\ge1:X_n=0\},
\qquad
A_X:=\sum_{n=0}^{\sigma_X-1}X_n
\tag{7}
\]

for either chain started at zero.  From (6), if `V_n=0` then `Z_n=0`, so `sigma_Z<=sigma_V`.  For every `n<sigma_Z`, `V_n>=Z_n`; therefore

\[
\boxed{
\sigma_V\ge\sigma_Z,
\qquad
A_V\ge A_Z
}
\tag{8}
\]

pathwise.

This removes the need for any invariant distribution of the original infinite-stack backward chain.  In fact (6) is stronger than the preceding run's first-cycle-only formulation.

# Method B4 — prove the critical scalar cycle theorem directly, without stationary means

## 4. Scalar chain and the universal bounded comparator

For a nonnegative integer-valued emigration law `L`, write

\[
Z^{L}_{n+1}
=
\sum_{j=1}^{(Z^L_n+1-L_n)_+}\xi_{n,j},
\qquad Z^L_0=0,
\tag{9}
\]

where the `L_n` are iid copies of `L` and the `xi` are iid geometric `(1/2)` gaps as above.

Suppose now that

\[
EN=2,
\qquad
p_0:=P(N=0)>0.
\tag{10}
\]

Set

\[
a:=\min\{p_0/2,1/6\},
\]

and define

\[
P(N_*=0)=a,
\qquad
P(N_*=2)=1-3a,
\qquad
P(N_*=3)=2a.
\tag{11}
\]

Then `EN_*=2`, and the stop-loss computation from the preceding run gives

\[
\boxed{N_*\le_{cx}N.}
\tag{12}
\]

For completeness, at the only nontrivial integer thresholds,

\[
E(N-1)_+=1+p_0\ge1+a=E(N_*-1)_+,
\]

and

\[
E(N-2)_+=2p_0+P(N=1)\ge2a=E(N_*-2)_+.
\]

Above threshold two the comparator stop loss vanishes.

If `phi` is increasing and convex and `S_r=xi_1+...+xi_r`, then

\[
h(r):=E\phi(S_r)
\]

is increasing and convex in the integer variable `r`.  Indeed,

\[
h(r+1)-h(r)
=E[\phi(S_r+\xi)-\phi(S_r)],
\]

and for each fixed nonnegative increment `k`, convexity of `phi` makes

\[
s\mapsto\phi(s+k)-\phi(s)
\]

nondecreasing.  Since `S_r` increases under the natural coupling, the increments of `h` are nondecreasing.

Consequently the transition kernel

\[
(K_L\phi)(x)=E\phi(S_{(x+1-L)_+})
\]

preserves increasing convex functions in `x`, and (12) implies

\[
K_{N_*}\phi(x)\le K_N\phi(x).
\tag{13}
\]

Induction from zero therefore gives the fixed-time comparison

\[
\boxed{
Z^{N_*}_n\le_{icx} Z^N_n
\quad\text{for every }n,
}
\tag{14}
\]

in particular

\[
E_0 Z^{N_*}_n\le E_0 Z^N_n.
\tag{15}
\]

The preceding manuscript used invariant laws after (15).  The next argument avoids them completely.

## 5. A renewal-reward lemma

Let `X` be any regenerative chain started at the atom zero, and let

\[
\sigma=\inf\{n\ge1:X_n=0\}
\]

have finite mean.  For a nonnegative reward `r`, define the reward in one cycle

\[
R_r:=\sum_{n=0}^{\sigma-1}r(X_n).
\]

Whenever `E R_r<infinity`, the elementary renewal-reward theorem gives

\[
\boxed{
\lim_{T\to\infty}
\frac1T\sum_{n=0}^{T-1}E_0 r(X_n)
=
\frac{E R_r}{E\sigma}.
}
\tag{16}
\]

A short justification is as follows.  Successive return cycles are iid.  The expected total reward accumulated before time `T` is trapped between the rewards of the completed cycles and the rewards of the completed cycles plus the current cycle.  The renewal theorem gives `E N(T)/T -> 1/E sigma`; summing the iid cycle rewards up to `N(T)` and `N(T)+1` gives the same limiting ratio.  For bounded `r` the conclusion also follows directly from the almost-sure renewal-reward theorem and bounded convergence.

We will use (16) only with either a bounded reward or under the explicit contradiction hypothesis that the one-cycle total reward has finite expectation.

## 6. The comparator forces divergent Cesàro population without an invariant law

Let

\[
D:=Z^{N_*}.
\]

The law `N_*` is exactly a bounded source-valid cookie environment: the first `N_*` cookies are deterministic-right and all later cookies are fair.  It has bounded depth three, drift two, and satisfies `(WEL)` because `P(N_*=0)=a>0`.  By the source bounded theorem its speed is zero.  The source backward/regeneration identities give

\[
E\sigma_D<\infty,
\qquad
E A_D=\infty,
\tag{17}
\]

where `A_D=sum_{n<sigma_D}D_n`.  The second conclusion follows because finite `E A_D`, together with finite positive `E sigma_D`, would make the regeneration-time denominator finite and hence the speed strictly positive.

For `R>=1`, use the bounded reward

\[
r_R(x)=x\wedge R
\]

and define

\[
A_D^{(R)}:=\sum_{n=0}^{\sigma_D-1}(D_n\wedge R).
\]

Then `A_D^{(R)}<=R sigma_D`, so it is integrable, and by (16)

\[
\lim_{T\to\infty}
\frac1T\sum_{n<T}E_0(D_n\wedge R)
=
\frac{E A_D^{(R)}}{E\sigma_D}.
\tag{18}
\]

Monotone convergence and (17) imply

\[
E A_D^{(R)}\uparrow E A_D=\infty.
\]

Since `D_n>=D_n wedge R`, (18) gives, for every `R`,

\[
\liminf_{T\to\infty}
\frac1T\sum_{n<T}E_0D_n
\ge
\frac{E A_D^{(R)}}{E\sigma_D}.
\]

Letting `R->infinity`,

\[
\boxed{
\lim_{T\to\infty}
\frac1T\sum_{n<T}E_0D_n
=\infty.
}
\tag{19}
\]

No invariant measure has been invoked.

## 7. Direct proof of infinite critical cycle reward for arbitrary `N`

Let

\[
Z:=Z^N.
\]

First, `E sigma_Z<infinity`.  Indeed, because `E(N wedge M) -> 2`, choose finite `M` with

\[
E(N\wedge M)>1.
\]

The front-loaded bounded-cookie chain with emigration `N wedge M` is positive recurrent in the right-transient bounded regime.  Since `N>=N wedge M`, the `N`-chain has at least as much emigration and is pathwise no larger under the natural coupling, hence its return time to zero is no larger and has finite mean.

Now (15) and (19) imply

\[
\lim_{T\to\infty}
\frac1T\sum_{n<T}E_0Z_n
=\infty.
\tag{20}
\]

Suppose for contradiction that

\[
E A_Z<\infty.
\]

Apply (16) with `r(x)=x`.  The contradiction hypothesis is exactly the integrability condition on the cycle reward, and `E sigma_Z<infinity`, so

\[
\lim_{T\to\infty}
\frac1T\sum_{n<T}E_0Z_n
=
\frac{E A_Z}{E\sigma_Z}<\infty,
\]

contradicting (20).  Therefore

\[
\boxed{
E A_Z=\infty
\quad\text{whenever }EN=2\text{ and }P(N=0)>0.
}
\tag{21}
\]

This proves the critical random-emigration statement directly at the one-cycle level.  It avoids invariant distributions, convergence to stationarity, invariant first moments, and uniform-integrability issues.

## 8. The full transient zero-speed interval `1<EN<=2`

If

\[
1<\mu:=EN<2,
\]

choose an integer `L>2-mu`, an independent Bernoulli variable `B` with

\[
P(B=1)=(2-\mu)/L,
\]

and put

\[
N^+:=N+LB.
\]

Then `EN^+=2`, `P(N^+=0)>0`, and `N^+>=N` pathwise.  More emigration makes the scalar chain smaller, hence its first cycle is dominated:

\[
A_{N}\ge A_{N^+}
\]

under a common offspring coupling.  By (21), `E A_{N^+}=infinity`; therefore

\[
\boxed{
E A_N=\infty
\quad\text{for every }1<EN\le2,\ P(N=0)>0.
}
\tag{22}
\]

Again no invariant distribution is used.

## 9. Return to arbitrary positive cookie stacks

For an iid positive cookie environment with finite drift `delta`, Bernoulliization gives an iid integer-valued `N` with

\[
EN=\delta.
\]

When `delta<infinity`, Tonelli gives `N<infinity` almost surely.  The left part of `(WEL)` has positive probability of a stack with `p_i<1` for every `i`; on that event all `d_i<1`, and `sum_i d_i<infinity` almost surely.  Therefore

\[
\prod_i(1-d_i)>0
\]

on a positive-probability environment event, so after averaging

\[
P(N=0)>0.
\tag{23}
\]

If `1<delta<=2`, (22) gives infinite expected total progeny for the front-loaded scalar chain.  The global stackwise coupling (8) then yields

\[
E A_V\ge E A_Z=\infty.
\]

The source backward-jump/regeneration identity in the right-transient `(IID)+(WEL)+(POS1)` regime expresses the regeneration time as the finite regeneration displacement plus twice this total backward population.  Hence `E A_V=infinity` forces

\[
v=0.
\]

Together with source recurrence for `delta<=1` and the already-proved finite-depth truncation argument for `delta>2`, this recovers the full source conclusion (1).

The mathematical statement remains candidate source-level complete.  Operational status remains `PARTIAL` until prior art and both required independent audits are completed.

# Method B22 — read the failures / map the nearest prior-art collision

The current proof no longer needs to import a classical random-emigration theorem, but prior art can still subsume the scalar theorem or the full cookie theorem.  The bounded search dated 2026-09-18 produced the following risk map.

1. **Kosygina–Zerner source (2012/2013).**  Immediately after defining the life-cycle quantities and their regeneration connection, the survey says that many existing branching-process-with-migration papers did not appear to contain the particular setting required for their bounded-cookie proof.  This is historical evidence only, not a 2026 novelty certificate.

2. **Omar Chakhtoun, PhD dissertation, CUNY Graduate Center, 2019, _One-Dimensional Excited Random Walk with Unboundedly Many Excitations Per Site_.**  The public repository abstract explicitly says the model is studied while **requiring a tail decay estimate on the number of excitations per site**, and that ballisticity/zero-speed criteria are proved under that wider class.  Thus the public abstract does not state the unrestricted `(IID)+(WEL)+(POS1)` theorem above.  The CUNY PDF endpoint returned HTTP 403 in this run, so theorem-by-theorem comparison of the full dissertation is still **UNVERIFIED**, and no novelty conclusion is drawn from the abstract alone.  Landing page: https://academicworks.cuny.edu/gc_etds/3030/

3. **V. A. Vatutin, _A Critical Galton–Watson Branching Process with Emigration_, Theory Probab. Appl. 22 (1978), 465–481, DOI 10.1137/1122058; S. V. Kaverin, _A Refinement of Limit Theorems for Critical Branching Processes with Emigration_, Theory Probab. Appl. 35 (1991), 574–580, DOI 10.1137/1135080.**  These are the closest classical emigration titles.  The accessible publisher pages did not expose enough theorem text to certify whether their update order, immigration offset, emigration law, and life-cycle moment conclusions contain (21).  They remain unresolved prior-art risk.

4. **N. M. Yanev and G. P. Yanev, _Critical Branching Processes with Random Migration_ (1995), DOI 10.1007/978-1-4612-2558-4_5, and related random-migration work.**  Its public abstract studies processes stopped at zero with random family/individual emigration, no migration, or state-dependent immigration.  This is potentially the **highest classical collision risk** for the scalar theorem because the migration is random and the process is explicitly killed at zero.  The abstract alone does not show that the exact recursion `(9)` or the mean-two total-progeny conclusion `(21)` is covered.  Full-text comparison is required before any novelty claim.

5. **T.-M. Nguyen, _Speed of Excited Random Walks with Long Backward Steps_, J. Stat. Phys. (2022).**  Its critical branching theorem uses a multi-type process with a deterministic emigration vector.  This is structurally nearby but not an immediate statement for arbitrary iid integer-valued `N` in (9).

6. **Georg Braun, _On supercritical branching processes with emigration_, J. Appl. Probab. 59 (2022).**  The abstract studies supercritical Galton–Watson reproduction with iid emigration and extinction/lifetime questions.  Our offspring law is critical and the recursion has the `+1` before emigration, so no direct implication was identified from the accessible abstract.

7. **Patrick Carper, arXiv:2609.06311 (5 September 2026), _A Branching Process with Geometric Emigration and the “Have Your Cookie and Eat It” Random Walk_.**  This treats a special geometric-emigration law.  It overlaps the exact calibration family computed in an earlier R7-02 run, not visibly the arbitrary-`N` theorem (21).

The search therefore does **not** certify novelty.  It does sharpen the remaining literature task: the two highest-value full-text comparisons are Chakhtoun 2019 and the Yanev/Vatutin critical random-emigration line.  A negative search is not evidence that those theorems fail to subsume the present one.

# 10. What changed in this run

- The fixed source metric remains `M_clause: 2/2 -> 2/2` because the source conclusion was already candidate-complete.
- The critical scalar proof is now available in a form that never uses an invariant law or invariant first moment: bounded comparator `->` divergent truncated renewal rewards `->` divergent Cesaro population `->` contradiction with finite cycle reward.
- Bernoulliization/front-loading is strengthened to a single **stackwise, all-success-level, all-generation** coupling, yielding `V_n>=Z_n` globally and hence first-cycle domination directly.
- The prior-art risk map identifies Yanev’s random-migration line, together with Chakhtoun’s inaccessible full dissertation, as the most important unresolved collision checks.
- There is no finite computational core in this theorem, so no checker was manufactured.

## Remaining gaps / operational obligations

1. Full theorem-level comparison with Chakhtoun’s 2019 dissertation remains blocked by the public PDF endpoint returning HTTP 403 during this run; the public abstract is not enough.
2. Full theorem-level comparison with Vatutin/Kaverin/Yanev random-emigration papers remains incomplete from accessible abstracts/index pages.
3. No actual independent P26 audit of C0134 has yet been recovered.
4. No distinct OTHER-track independent audit of C0134 has yet been recovered.
5. The existing paper package should be synchronized to use the direct cycle-reward proof rather than its older invariant-law presentation before any external use.

Operational status: **PARTIAL**.  Mathematical status: **candidate source-level complete, strengthened proof**.