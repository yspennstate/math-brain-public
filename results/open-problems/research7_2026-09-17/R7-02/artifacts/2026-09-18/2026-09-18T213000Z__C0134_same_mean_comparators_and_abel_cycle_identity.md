Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# C0134 — same-mean bounded comparators, obstruction to stochastic order, and an exact Abel cycle identity

Date of research run: 2026-09-18 UTC  
Slot: `R7-02 Finite Certificate Research`  
Native ID: `6aabe797a39081919acc889f29f4c556`  
Target: `C0134` — Kosygina–Zerner, *Excited random walks: results, methods, open problems*, Problem 5.3  
Run-start master: `dc922c9242336667fca4a28e3cd2ac314144f372`  
Fresh master immediately before delivery work: `447a09e59d44fb317efd96aac5512a09ccf3a309`  
Previous report: `research7_2026-09-17/R7-02/runs/2026-09-18/2026-09-18T203500Z__report.md` @ `d0161dc0f9df99cbcc89ada68d5eeb941daf406c`  
Previous artifact: `research7_2026-09-17/R7-02/artifacts/2026-09-18/2026-09-18T202800Z__C0134_cycle_reward_proof_and_stackwise_coupling.md` @ `f1728df73e24db5aad416f61c336085032bbcc38`

Frozen source metric remains `M_clause = 2/2`. This artifact hardens and shortens the already candidate-complete argument; it does not pretend that proof simplification is a third source clause.

## 1. Source scope and the scalar chain

Kosygina–Zerner Theorem 5.2 proves under `(IID)+(BD)+(WEL)` that the one-dimensional excited random walk has

\[
 v=0\quad\text{for }\delta\in[-2,2],
 \qquad
 v>0\quad\text{for }\delta>2.
\]

Problem 5.3 asks whether `(BD)` can be replaced by `(POS1)`. In the positive-cookie branch this is exactly

\[
 \delta\le2\Longrightarrow v=0,
 \qquad
 \delta>2\Longrightarrow v>0.
\tag{1}
\]

The cumulative R7-02 reduction Bernoulliizes a positive stack, writes the number of deterministic-right marks as an integer-valued random variable `N`, and front-loads these marks. At finite drift,

\[
 \mu:=\mathbb E N=\delta,
 \qquad
 p_0:=\mathbb P(N=0)>0.
\tag{2}
\]

The front-loaded backward chain is

\[
 Z^N_{n+1}=S_{(Z^N_n+1-N_n)_+},
 \qquad
 S_r:=\xi_1+\cdots+\xi_r,
\tag{3}
\]

where the `N_n` are iid copies of `N` and the `\xi` are iid geometric random variables on `\mathbb Z_+` with

\[
 \mathbb P(\xi=k)=2^{-(k+1)},
 \qquad \mathbb E\xi=1.
\]

The previous report established on one stackwise coupling that the original backward chain dominates this front-loaded chain at every generation, hence dominates its first-cycle length and total progeny. Therefore it suffices for zero speed to prove that the front-loaded chain has infinite expected first-cycle total progeny.

The present run uses methods **B6 / B20 / B25**.

# 2. Method B6 — DEFORM TO A POINT YOU CAN SOLVE

## 2.1 New result: a bounded comparator with exactly the same drift for every `1<mu<2`

The previous argument handled `1<\mu<2` by artificially adding emigration until the mean became exactly two. That works, but it hides the mechanism. There is in fact a direct bounded solved comparator at the **same** value of `\mu`.

### Lemma 2.1 (three-point same-mean comparator below the endpoint)

Let `N` be nonnegative integer-valued with

\[
 1<\mu:=\mathbb E N<2,
 \qquad
 p_0:=\mathbb P(N=0)>0.
\]

Set

\[
 a:=\min\left\{\frac{p_0}{2},\frac{2-\mu}{4}\right\}>0
\tag{4}
\]

and define `L_\mu` on `{0,1,2}` by

\[
 \begin{aligned}
 \mathbb P(L_\mu=0)&=a,\\
 \mathbb P(L_\mu=1)&=2-\mu-2a,\\
 \mathbb P(L_\mu=2)&=\mu-1+a.
 \end{aligned}
\tag{5}
\]

Then all three probabilities are nonnegative, `\mathbb E L_\mu=\mu`, `\mathbb P(L_\mu=0)>0`, and

\[
 \boxed{L_\mu\le_{\rm cx}N.}
\tag{6}
\]

### Proof

The probabilities in (5) sum to one. From `a\le(2-\mu)/4`,

\[
 2-\mu-2a\ge\frac{2-\mu}{2}>0,
\]

and `\mu-1+a>0`. Their mean is

\[
 (2-\mu-2a)+2(\mu-1+a)=\mu.
\]

For integrable integer-valued variables of equal mean, convex order is equivalent to the stop-loss inequalities

\[
 \mathbb E(X-k)_+\le \mathbb E(Y-k)_+,
 \qquad k=0,1,2,\ldots.
\tag{7}
\]

At `k=0` there is equality because both means equal `\mu`. At `k=1`,

\[
 \mathbb E(L_\mu-1)_+
 =\mathbb P(L_\mu=2)
 =\mu-1+a,
\]

while

\[
 \mathbb E(N-1)_+
 =\mathbb EN-\mathbb P(N\ge1)
 =\mu-1+p_0
 \ge\mu-1+a.
\]

For every `k\ge2`, the left side of (7) is zero. Hence (6). `\square`

## 2.2 Endpoint comparator at `mu=2`

At `\mu=2`, no distribution supported on `{0,1,2}` can simultaneously have positive mass at zero and mean two. This is the exact structural reason the endpoint needs one extra support point.

The previous run's comparator is therefore not an arbitrary trick but the minimal endpoint deformation. Let

\[
 a:=\min\left\{\frac{p_0}{2},\frac16\right\}
\]

and define

\[
 \mathbb P(L_2=0)=a,
 \qquad
 \mathbb P(L_2=2)=1-3a,
 \qquad
 \mathbb P(L_2=3)=2a.
\tag{8}
\]

Then `\mathbb EL_2=2`, `\mathbb P(L_2=0)>0`, and the exact stop-loss calculation already proved gives

\[
 \boxed{L_2\le_{\rm cx}N.}
\tag{9}
\]

Indeed,

\[
 \mathbb E(L_2-1)_+=1+a
 \le1+p_0=\mathbb E(N-1)_+,
\]

\[
 \mathbb E(L_2-2)_+=2a
 \le2p_0+\mathbb P(N=1)
 =\mathbb E(N-2)_+,
\]

and higher comparator stop losses vanish.

## 2.3 Why these are solved points

For `1<\mu<2`, the environment whose first `L_\mu` cookies are deterministic-right and whose later cookies are fair is iid across sites, has bounded depth two, satisfies `(WEL)` because `\mathbb P(L_\mu=0)=a>0`, and has drift parameter exactly `\mu`.

At `\mu=2`, the analogous environment based on `L_2` has bounded depth three, satisfies `(WEL)`, and has drift exactly two.

Thus both comparators lie **inside the bounded model already solved by the source**, not inside a new restricted theorem invented here. Kosygina–Zerner Theorem 5.4 gives for the corresponding first-cycle length `\sigma^L` and total progeny `A^L`

\[
 \mathbb P(\sigma^L>n)\sim C_1 n^{-\mu},
 \qquad
 \mathbb P(A^L>n)\sim C_2 n^{-\mu/2}.
\tag{10}
\]

Hence for every `1<\mu\le2`,

\[
 \boxed{\mathbb E\sigma^L<\infty,
 \qquad
 \mathbb EA^L=\infty.}
\tag{11}
\]

The first statement follows because `\mu>1`; the second follows because `\mu/2\le1`.

This replaces the old two-step route

`mu<2 -> add emigration until mean 2 -> compare to critical chain`

by the direct route

`mu -> same-mean bounded source model -> exact source tail theorem`.

**B6 outcome: successful.** The full scalar interval `1<\mu\le2` now has a same-mean bounded comparator, piecewise with support `{0,1,2}` below the endpoint and `{0,2,3}` at the endpoint.

# 3. Method B20 — FIND WHY THE OBVIOUS ALGORITHM FAILS

The obvious comparison algorithm would try to replace `N` by a bounded emigration law that is pathwise smaller or larger and then use ordinary stochastic monotonicity. At fixed mean that route is generically impossible.

### Lemma 3.1 (same mean kills nontrivial stochastic domination)

If nonnegative integrable integer-valued `X,Y` satisfy

\[
 X\le_{\rm st}Y,
 \qquad
 \mathbb EX=\mathbb EY<\infty,
\]

then `X` and `Y` have the same distribution.

### Proof

For nonnegative integer-valued variables,

\[
 \mathbb EY-\mathbb EX
 =\sum_{k\ge1}
 \bigl(\mathbb P(Y\ge k)-\mathbb P(X\ge k)\bigr).
\tag{12}
\]

Every summand is nonnegative under stochastic domination. The sum is zero because the means agree, so every summand is zero. Thus all tails, hence the laws, agree. `\square`

Therefore a distinct same-mean bounded comparator can **never** be obtained by ordinary stochastic domination. The critical example makes the obstruction concrete. Let

\[
 \mathbb P(N=0)=\frac13,
 \qquad
 \mathbb P(N=3)=\frac23.
\]

Then `\mathbb EN=2`. Formula (8) gives `a=1/6` and

\[
 \mathbb P(L_2=0)=\frac16,
 \quad
 \mathbb P(L_2=2)=\frac12,
 \quad
 \mathbb P(L_2=3)=\frac13.
\]

At threshold one,

\[
 \mathbb P(L_2\ge1)=\frac56>\frac23=\mathbb P(N\ge1),
\]

so `L_2\not\le_{\rm st}N`. At threshold three,

\[
 \mathbb P(N\ge3)=\frac23>\frac13=\mathbb P(L_2\ge3),
\]

so `N\not\le_{\rm st}L_2`. They are stochastically incomparable.

What survives is exactly the order adapted to the branching kernel. If `\varphi` is increasing convex and

\[
 h(r):=\mathbb E\varphi(S_r),
\]

then `h` is increasing and convex in `r`. Consequently

\[
 n\longmapsto h((x+1-n)_+)
\]

is convex, and `L\le_{\rm cx}N` implies

\[
 K_L\varphi(x)\le K_N\varphi(x),
\tag{13}
\]

where

\[
 K_N\varphi(x)
 :=\mathbb E\varphi(S_{(x+1-N)_+}).
\]

The kernel also preserves increasing convexity in `x`, so induction yields

\[
 \boxed{Z^L_n\le_{\rm icx}Z^N_n\quad\forall n.}
\tag{14}
\]

In particular,

\[
 \mathbb E Z^L_n\le\mathbb E Z^N_n.
\tag{15}
\]

Thus convex order is not decorative machinery. It is precisely what remains available after the same-mean constraint rules out every nontrivial pathwise emigration ordering.

**B20 outcome: successful.** The failed algorithm is now identified exactly: ordinary stochastic domination cannot compare a distinct bounded law at the same mean. The correct replacement is convex order because the clipped random-sum transition is convex in the emigration variable.

# 4. Method B25 — COUNT THE SAME THING TWICE

The preceding report used a renewal-reward theorem to pass from cycle reward to fixed-time means. This run derives the needed identity directly and, more cleanly, works with Abel means. No invariant distribution and no Cesaro/uniform-integrability step is required.

## 4.1 Exact first-return convolution

Let `Z` be any of the scalar chains (3), started from zero, and let

\[
 \sigma:=\inf\{n\ge1:Z_n=0\}.
\]

For a nonnegative reward `r`, define

\[
 u_n:=\mathbb E_0 r(Z_n),
 \qquad
 b_n:=\mathbb E_0[r(Z_n);\ \sigma>n],
 \qquad
 f_k:=\mathbb P_0(\sigma=k).
\tag{16}
\]

Split trajectories according to the first return to zero. On `{\sigma=k\le n}`, the strong Markov property at `k` restarts an independent copy from zero. Therefore

\[
 \boxed{
 u_n=b_n+\sum_{k=1}^n f_k u_{n-k}.
 }
\tag{17}
\]

This is literally one expected reward counted in two ways: trajectories that have not yet completed their first cycle, and trajectories whose first cycle ended at time `k`.

For `0<s<1`, put

\[
 U_r(s):=\sum_{n\ge0}u_n s^n,
 \quad
 B_r(s):=\sum_{n\ge0}b_n s^n,
 \quad
 F(s):=\sum_{k\ge1}f_k s^k=\mathbb E_0s^\sigma.
\]

Tonelli applied to the nonnegative terms in (17) gives the exact transform identity

\[
 \boxed{
 U_r(s)=\frac{B_r(s)}{1-F(s)}.
 }
\tag{18}
\]

Moreover

\[
 B_r(s)
 =\mathbb E_0\sum_{n<\sigma}r(Z_n)s^n.
\tag{19}
\]

If `\mathbb E\sigma<\infty`, then

\[
 \frac{1-F(s)}{1-s}\longrightarrow\mathbb E\sigma
 \qquad(s\uparrow1).
\tag{20}
\]

If in addition the cycle reward

\[
 A_r:=\sum_{n<\sigma}r(Z_n)
\]

is integrable, monotone convergence in (19) gives

\[
 B_r(s)\longrightarrow\mathbb EA_r.
\]

Consequently

\[
 \boxed{
 \lim_{s\uparrow1}
 (1-s)\sum_{n\ge0}\mathbb E_0r(Z_n)s^n
 =\frac{\mathbb EA_r}{\mathbb E\sigma}.
 }
\tag{21}
\]

Equation (21) is the exact Abel-form cycle-reward identity needed here.

## 4.2 Infinite cycle reward detected without an invariant law

Apply (21) to the bounded comparator `D=Z^L` with truncated rewards

\[
 r_R(x):=x\wedge R.
\]

Since `r_R\le R` and `\mathbb E\sigma_D<\infty`, its cycle reward is integrable. Thus

\[
 \lim_{s\uparrow1}(1-s)
 \sum_{n\ge0}\mathbb E_0(D_n\wedge R)s^n
 =\frac{\mathbb E\sum_{n<\sigma_D}(D_n\wedge R)}{\mathbb E\sigma_D}.
\tag{22}
\]

By (11), the numerator increases to `\mathbb EA_D=\infty` as `R\to\infty`. Since `D_n\ge D_n\wedge R`, for every `K<\infty` one may choose `R` so large that the right side of (22) exceeds `K`. Therefore

\[
 \boxed{
 \lim_{s\uparrow1}(1-s)
 \sum_{n\ge0}\mathbb E_0D_n s^n=\infty.
 }
\tag{23}
\]

Now let `Z=Z^N`. Fixed-time increasing-convex domination (15) gives

\[
 \boxed{
 \lim_{s\uparrow1}(1-s)
 \sum_{n\ge0}\mathbb E_0Z_n s^n=\infty.
 }
\tag{24}
\]

It remains only to know that `\mathbb E\sigma_Z<\infty`. Since `\mathbb EN=\mu>1`, monotone convergence gives an `M<\infty` with

\[
 \mathbb E(N\wedge M)>1.
\]

The chain with bounded emigration `N\wedge M` is the backward chain of a bounded source-valid environment. Theorem 5.4 gives its return tail exponent `\mathbb E(N\wedge M)>1`, hence finite mean return time. Since `N\ge N\wedge M`, the `N`-chain has at least as much emigration and may be coupled below the truncated chain, so

\[
 \mathbb E\sigma_Z<\infty.
\tag{25}
\]

Suppose for contradiction that the untruncated cycle area

\[
 A_Z:=\sum_{n<\sigma_Z}Z_n
\]

had finite expectation. Use (21) with the unbounded reward `r(x)=x`. This is legitimate under the supposition `\mathbb EA_Z<\infty`; also each fixed-time mean is finite because

\[
 \mathbb E[Z_{n+1}\mid Z_n=x]
 =\mathbb E(x+1-N)_+\le x+1,
\]

so `\mathbb EZ_n\le n` from `Z_0=0` and the power series is finite for every `s<1`. Equation (21) would give

\[
 \lim_{s\uparrow1}(1-s)
 \sum_{n\ge0}\mathbb E_0Z_n s^n
 =\frac{\mathbb EA_Z}{\mathbb E\sigma_Z}<\infty,
\]

contradicting (24). Hence

\[
 \boxed{\mathbb EA_Z=\infty.}
\tag{26}
\]

This proves the random-emigration theorem directly for every

\[
 \boxed{1<\mathbb EN\le2,\qquad\mathbb P(N=0)>0.}
\tag{27}
\]

No invariant distribution appears anywhere in this proof, and the previous auxiliary operation of adding emigration when `\mathbb EN<2` is no longer needed.

**B25 outcome: successful.** First-return decomposition gives an exact transform identity, and Abel divergence transfers from the bounded comparator to the arbitrary law by fixed-time increasing-convex domination.

# 5. Consequence for the source argument

The cumulative source proof can now be stated in a shorter dependency chain.

1. **`delta>2`, including `delta=infinity`.** Truncate each positive stack after depth `M` and replace its tail by fair cookies. For some finite `M`, the truncated drift exceeds two. The bounded source theorem gives positive speed to the truncation, and cookie monotonicity gives positive speed to the original environment.

2. **`1<delta<=2`.** Bernoulliization gives iid emigration variables `N` with `EN=delta`; `(WEL)` plus finite drift gives `P(N=0)>0`. The same-mean bounded comparator theorem plus the Abel cycle argument gives infinite expected total progeny for the front-loaded scalar chain. The already established stackwise front-loading coupling gives at least as much total progeny in the original backward chain. The source regeneration identity then forces zero speed.

3. **`delta<=1`.** This is the recurrent/non-right-transient source regime under positive cookies; the source strong law gives speed zero.

Thus the mathematical candidate conclusion remains

\[
 \boxed{
 \delta\le2\Longrightarrow v=0,
 \qquad
 \delta>2\Longrightarrow v>0
 }
\tag{28}
\]

under the full `(IID)+(WEL)+(POS1)` hypotheses of Problem 5.3.

The frozen metric stays `2/2`: this run simplified and independently re-grounded the difficult clause rather than adding a source clause.

# 6. Prior-art/source checks dated 2026-09-18

The primary source was re-read at its current author PDF. Problem 5.3 still appears immediately after Theorem 5.2. The source defines `(WEL)` as positive probability that every cookie transition probability in each direction is strictly positive. Its Theorem 5.4 gives exactly the bounded life-cycle tail exponents used above. The source itself remarks that, as of its writing, the large branching-process-with-migration literature did not seem to include its particular backward-process setting.

A fresh bounded literature check sharpened, but did not eliminate, prior-art risk:

- **Travers (2018),** *Excited Random Walk in a Markovian Environment*, proves threshold results for a large Markovian class. Its model is structured and does not by its abstract state the arbitrary iid site-stack theorem of Problem 5.3.
- **Chakhtoun (2019),** *One-Dimensional Excited Random Walk with Unboundedly Many Excitations Per Site*, publicly describes an unbounded-excitation theorem under a tail-decay estimate on the number of excitations. The full dissertation endpoint returned HTTP 403 in this run. In accordance with the permission rule, no bypass was attempted, so theorem-level overlap remains **UNVERIFIED**.
- **Yanev (2015),** *Critical Controlled Branching Processes and Their Relatives*, surveys migration processes. The main Section 3 model displayed in the accessible arXiv text removes the offspring of one individual with probability `p`, rather than an arbitrary iid number `N`; its cited 1995/1997 random-migration line is more general and remains a genuine collision risk. The accessible survey text contains survival/conditional-limit theorems but no searchable `total progeny` theorem matching (26).
- **Yanev–Yanev (1995/1997)** allow random family and individual emigration in a broader stopped-at-zero migration model. Accessible abstracts emphasize non-extinction probabilities and conditional limits; they do not suffice to certify that (26) is new or known. Full theorem-level comparison remains mandatory.
- **Carper (arXiv:2609.06311, submitted 5 September 2026)** treats geometric emigration and computes life-period/stationary-mean quantities for that special model. It is relevant but does not state an arbitrary-emigration theorem in its abstract.

A bounded search miss is not a novelty certificate. No novelty claim is made here.

# 7. Failures, exact remaining gaps, and status

### What failed

- A pathwise same-mean bounded emigration comparison is impossible except in the trivial equal-law case; Lemma 3.1 proves the obstruction exactly.
- Publicly accessible metadata is still insufficient for theorem-by-theorem exclusion of the Yanev–Yanev/Vatutin/Kaverin migration literature.
- The Chakhtoun full-text route is blocked by HTTP 403 and was not bypassed.

### What is now stronger

- Every `1<mu<2` law gets a direct bounded comparator at the **same** mean. The critical endpoint gets the minimal support enlargement needed to keep positive mass at zero.
- The scalar transfer theorem is now proved by the exact Abel first-return identity, without invariant laws and without invoking Cesaro renewal reward as a black box.
- The reason convex order, rather than stochastic order, is needed is now a theorem rather than intuition.

### Status

Mathematical source status: **CANDIDATE SOURCE-LEVEL COMPLETE**.  
Operational status: **PARTIAL**.

The operational label cannot advance to `PROVED` until at least:

1. theorem-level prior-art reconciliation is complete enough to distinguish a new proof from a known result;
2. the self-contained paper package is synchronized to the direct same-mean/Abel proof;
3. the required independent P26 audit and one distinct OTHER-track audit both actually pass.

No shared `RESULTS.md`, `QUEUE.md`, or `POSTED.md` edit is made by this worker.

Because the frozen metric remains `2/2`, this is the third consecutive ordinary no-movement run (`2 -> 3`). Under the owner protocol, the **next** R7-02 research iteration must be the Section-I thinking-only stuck diagnosis rather than a fourth ordinary proof-hardening run.