Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# C0130 — exact finite-core gluing and monotone truncation continuity for i.i.d. positive infinite cookie stacks

Target: `C0130`, Elena Kosygina and Martin P. W. Zerner, *Excited random walks: results, methods, open problems*, Problem 3.12, printed p. 13.

Date: 2026-09-18.

Status: **PARTIAL relative to the full source.** This note closes the monotone neutral-tail truncation gap isolated in the preceding R7-05 run for the entire **i.i.d. positive-cookie transient subclass, including genuinely infinite stacks and allowing cookies of strength 1**. It does not cover arbitrary stationary-ergodic spatial dependence, so it is not a source-level solution of Problem 3.12.

The admission-fixed metric remains

`M_closed` = largest finite cookie depth `M` for which there is an evidenced exact closed escape-probability formula valid for every i.i.d. bounded cookie-stack law neutral after visit `M` in the transient regime.

That metric was already saturated over all finite depths, so the present theorem does not redefine or move it:

\[
M_{\rm closed}=\infty\quad\text{over finite i.i.d. depths, unchanged.}
\]

The mathematical advance is instead that the finite-depth formulas now converge to the escape probability of every transient i.i.d. positive infinite stack, with an explicit boundary-error bound.

---

## 1. Source scope and cumulative inputs

Write the right-jump probabilities in a site stack as

\[
(p_1,p_2,\ldots),\qquad p_i\in[1/2,1].
\]

The stacks are i.i.d. from site to site; arbitrary dependence among the coordinates inside one stack is allowed. Put

\[
\alpha_i=2p_i-1\in[0,1],
\qquad
\delta=\mathbb E\sum_{i\ge1}\alpha_i\in[0,\infty].
\]

Assume the nontrivial right-transient case `delta>1`. This is a subclass of the source's `(SE)+(POS_1)` branch of Theorem 3.10; the source permits unbounded positive stacks there. The exceptional deterministic stack `(1,1/2,1/2,...)`, for which `delta=1` but the walk marches right forever, is trivial for the escape question and can be handled separately.

For `M>=1`, let `omega^(M)` be the neutral-tail truncation

\[
p_i^{(M)}=
\begin{cases}
p_i,&i\le M,\\
1/2,&i>M.
\end{cases}
\tag{1.1}
\]

and let `p_esc^(M)` be the corresponding annealed never-return probability. Let `p_esc^(infinity)` denote the probability for the full infinite stack.

The preceding R7-05 run proved only monotonicity

\[
p_{\rm esc}^{(M)}\uparrow p_*\le p_{\rm esc}^{(\infty)}
\]

and isolated the possible strict inequality as the minimax/continuity obstruction

\[
\sup_M\inf_N a_{M,N}\stackrel?=\inf_N\sup_M a_{M,N}.
\]

The present note proves equality for the i.i.d. positive subclass.

Two cumulative facts are reused at their proved scope:

1. For every finite-depth i.i.d. `(BD)+(WEL)` law with drift greater than one, R7-05 proved exact forward/backward Siegmund duality. If `g(k)` is the survival probability of the forward chain from population `k`, then

\[
g(k)=\sum_{j=0}^{k-1}\pi_j,
\qquad
1-g(k)=\sum_{j\ge k}\pi_j,
\tag{1.2}
\]

where `pi` is the stationary law of the backward branching chain. In particular `g(k)\uparrow1`.

2. For every finite i.i.d. cookie depth satisfying `(BD)+(WEL)`, R7-05 proved an exact finite-dimensional signed-resolvent formula for `p_esc`.

No claim from a dependent-environment report is used in the proof below.

---

## 2. Forward chain and an identity that does not require bounded depth

At a fresh site expose the cookie coin sequence `xi_1,xi_2,...`, with `xi_i=1` for a right-step success and `xi_i=0` for a failure. Conditional on the stack, these coin tosses are independent with success probabilities `p_i`.

For `k>=1`, let

\[
S_k=\text{number of successes before the }k\text{-th failure}.
\]

If the `k`-th failure never occurs, set `S_k=+infinity`. Let the forward chain be

\[
V_{n+1}=S^{(n+1)}_{V_n},
\qquad V_0=k,
\tag{2.1}
\]

where each generation uses an independent site stack and its coin sequence; `0` is absorbing and `+infinity` is declared surviving. Define

\[
h(k)=\mathbb P_k(V_n>0\ \forall n),
\tag{2.2}
\]

and similarly `h_M` for the neutral-tail truncation.

### Lemma 2.1 — the escape/survival identity persists for infinite positive i.i.d. stacks

For the full right-transient i.i.d. positive environment,

\[
\boxed{
 p_{\rm esc}^{(\infty)}=\mathbb E[p_1]h(1).
}
\tag{2.3}
\]

For every sufficiently large `M` with truncated drift greater than one,

\[
\boxed{
 p_{\rm esc}^{(M)}=\mathbb E[p_1]h_M(1).
}
\tag{2.4}
\]

#### Proof

Let `F_m` be the number of failures before the `m`-th success in the same coin sequence. Pathwise, with the convention `S_k=+infinity` when necessary,

\[
\{F_{i+1}<k\}=\{S_k\ge i+1\}.
\tag{2.5}
\]

Thus the backward kernel `P` for `Z_{n+1}=F_{Z_n+1}` and the forward kernel `Q` for (2.1) are Siegmund dual:

\[
PH=HQ^T,
\qquad H(i,k)=1_{\{i<k\}}.
\tag{2.6}
\]

This statement uses neither bounded cookie depth nor weak ellipticity.

Now start the excited walk at `1` and let `T_a` be the first hit of `a`. Reading a successful crossing of `[0,n]` backwards gives the standard exact finite-interval identity

\[
\mathbb P_1(T_n<T_0)=\mathbb P_0(Z_{n-1}=0).
\tag{2.7}
\]

Again this is a finite pathwise coin-stack identity; bounded depth is not used. Applying the `n-1` step version of (2.6) at `(i,k)=(0,1)` gives

\[
\mathbb P_0(Z_{n-1}=0)=\mathbb P_1(V_{n-1}>0).
\tag{2.8}
\]

Under `delta>1`, Theorem 3.10 of the source gives right transience. Hence the decreasing events `{T_n<T_0}` converge, up to a null set, to `{T_0=infinity}`. Since zero is absorbing for `V`, the events `{V_{n-1}>0}` decrease to forward survival. Therefore

\[
\mathbb P_1(T_0=\infty)=h(1).
\tag{2.9}
\]

A no-return path from the origin must first step to `+1`; a first step to `-1` must cross zero again before a right-transient walk tends to `+infinity`. The stack at zero is independent of the positive half-line, so multiplying (2.9) by `E[p_1]` yields (2.3). The same proof applies to every right-transient truncation and yields (2.4). QED.

---

# 3. Method B30 — localize: an exact `2K-2` visibility radius

The key new observation is that the forward process below population `K` cannot see arbitrarily deep into a cookie stack.

Fix `K>=2`. Censor one forward step into the finite outcome set

\[
\mathcal C_K=\{0,1,\ldots,K-1,H\},
\]

where `H` means an output in `[K,infinity]`.

### Lemma 3.1 — exact finite-core visibility

For every starting population `1<=k<K`, the censored outcome

\[
\Phi_K(S_k)=
\begin{cases}
S_k,&S_k<K,\\
H,&S_k\ge K
\end{cases}
\tag{3.1}
\]

is completely determined by the first at most

\[
\boxed{k+K-1\le2K-2}
\tag{3.2}
\]

coin tosses at that site.

#### Proof

Run the coin sequence until either the `k`-th failure occurs or the `K`-th success occurs. If the `k`-th failure occurs first and exactly `j<K` successes have appeared, then the stopping time is `j+k<=K-1+k<=2K-2` and the censored value is exactly `j`. If the `K`-th success occurs first, the censored value is `H`, and that stopping time is at most `K+k-1<=2K-2`. These are the only possibilities. QED.

### Corollary 3.2 — full and truncated stopped kernels are identical

If

\[
M\ge2K-2,
\tag{3.3}
\]

then the full infinite-stack chain and the `M`-truncated chain have exactly the same one-step censored transition kernel from every state `1,...,K-1`. Consequently they have exactly the same law up to the stopping time

\[
\tau_K=\inf\{n:V_n=0\text{ or }V_n\ge K\}.
\tag{3.4}
\]

No approximation and no ellipticity assumption is used here.

Moreover, for every positive stack and every `1<=k<K`,

\[
\mathbb P_k(V_1\ge K)\ge2^{-K},
\tag{3.5}
\]

because the event that the first `K` tosses are all successes has conditional probability at least `2^{-K}`. Hence

\[
\mathbb P_k(\tau_K>n)\le(1-2^{-K})^n,
\tag{3.6}
\]

so `tau_K<infinity` almost surely for both the full and truncated chains, even when some cookie strengths equal one.

Let

\[
a_K(k)=\mathbb P_k(V_{\tau_K}\ge K)
\tag{3.7}
\]

for this common stopped core. In particular `a_K(1)` is simultaneously the full-stack and every `M>=2K-2` truncation probability of reaching the high boundary before zero.

This is the gluing object missing from the preceding minimax formulation.

---

# 4. A common strictly elliptic transient baseline

The exact core identity is useful only if the survival boundary at large population can be controlled uniformly in `M`. Positivity supplies such a baseline.

Let

\[
d_m=\mathbb E\sum_{i=1}^m\alpha_i.
\tag{4.1}
\]

By monotone convergence, `d_m` increases to `delta>1`, so choose a finite `m_0` with

\[
d_{m_0}>1.
\tag{4.2}
\]

Choose

\[
t_0\in(1/d_{m_0},1).
\tag{4.3}
\]

From the original random stack construct the finite-depth weakened stack

\[
q_i=
\begin{cases}
1/2+t_0(p_i-1/2),&1\le i\le m_0,\\
1/2,&i>m_0.
\end{cases}
\tag{4.4}
\]

Then

\[
1/2\le q_i\le(1+t_0)/2<1,
\qquad
\delta_q=t_0d_{m_0}>1.
\tag{4.5}
\]

Thus the i.i.d. `q` environment is finite-depth, weakly (indeed uniformly in the failure direction) elliptic, and right transient. Let `g(k)` be its forward survival probability. The cumulative finite-depth Siegmund theorem gives a stationary backward law `pi^q` with

\[
\boxed{
 g(k)=\sum_{j=0}^{k-1}\pi^q_j,
 \qquad
 1-g(k)=\sum_{j\ge k}\pi^q_j\downarrow0.
}
\tag{4.6}
\]

For every `M>=m_0`, both the original `M`-truncation and the full stack dominate `q` coordinatewise under the natural sitewise coupling. The map from a coin stack to `S_k` is monotone in every success probability. Hence their forward chains dominate the `q`-chain, and for every `k`,

\[
\boxed{
h_M(k)\ge g(k),\qquad h(k)\ge g(k).}
\tag{4.7}
\]

All three survival functions are nondecreasing in the initial population.

---

# 5. Method B11 — dualize the boundary error into one stationary tail

We can now convert the exact core gluing into a quantitative continuity theorem.

### Theorem 5.1 — quantitative monotone truncation continuity

For every `K>=2` and every

\[
M\ge\max\{m_0,2K-2\},
\]

one has

\[
\boxed{
0\le h(1)-h_M(1)
\le 1-g(K)
=\sum_{j\ge K}\pi^q_j.
}
\tag{5.1}
\]

Consequently, with

\[
K_M=\lfloor M/2\rfloor+1,
\tag{5.2}
\]

for all sufficiently large `M`,

\[
\boxed{
0\le p_{\rm esc}^{(\infty)}-p_{\rm esc}^{(M)}
\le
\mathbb E[p_1]
\sum_{j\ge K_M}\pi^q_j
\longrightarrow0.
}
\tag{5.3}
\]

In particular,

\[
\boxed{
p_{\rm esc}^{(M)}\uparrow p_{\rm esc}^{(\infty)}.}
\tag{5.4}
\]

Thus the minimax gap isolated in the preceding run vanishes for every transient i.i.d. positive infinite cookie stack.

#### Proof

Fix `K` and `M` as above. By Corollary 3.2, the full and truncated chains have the same stopped law at `tau_K`, hence the same number `a_K(1)` in (3.7).

For either survival function `r` equal to `h` or `h_M`, bounded harmonicity and `tau_K<infinity` give

\[
r(1)=\mathbb E_1[r(V_{\tau_K});V_{\tau_K}\ge K].
\tag{5.5}
\]

On the high-boundary event, monotonicity in initial population and (4.7) yield

\[
r(V_{\tau_K})\ge g(V_{\tau_K})\ge g(K),
\tag{5.6}
\]

while trivially `r<=1`. Therefore both `h(1)` and `h_M(1)` lie in the same interval

\[
\boxed{
 a_K(1)g(K)\le r(1)\le a_K(1).
}
\tag{5.7}
\]

The full stack dominates its truncation, so `h(1)>=h_M(1)`. Subtracting the two bounds in (5.7),

\[
0\le h(1)-h_M(1)
\le a_K(1)(1-g(K))
\le1-g(K),
\]

which is (5.1). Equation (4.6) gives the stationary-tail form.

Take `K=K_M`. Then `2K_M-2<=M`, while `K_M->infinity`, so (4.6) makes the right side tend to zero. Finally multiply by the common first-step factor `E[p_1]` from Lemma 2.1 to obtain (5.3) and (5.4). QED.

### What this theorem does and does not use

The theorem requires no uniform ellipticity of the original infinite stack and permits `p_i=1`. Uniform ellipticity appears only in the deliberately weakened finite baseline `q`, where it is manufactured by the factor `t_0<1`. The argument uses positivity crucially twice: to couple every truncation above the same baseline and to obtain the universal high-boundary exit probability (3.5).

---

# 6. Method B5 — add an excitation parameter: radial continuity, including degenerate endpoints

The preceding theorem suggests a second continuity statement that is useful for actually importing the finite-depth formulas when some original cookies have strength one.

For `t in [0,1]`, define the globally weakened stack

\[
p_i(t)=\frac12+t\left(p_i-\frac12\right).
\tag{6.1}
\]

Choose `t_0,m_0` as in Section 4. For every `t in [t_0,1]`, the `t`-environment dominates the same finite-depth baseline `q`, and is right transient.

Let `h_t(k)` be its forward survival probability. For fixed `K`, let `a_K(t)` be the probability of hitting `[K,infinity]` before zero.

### Lemma 6.1 — finite-core dependence on `t` is continuous

For fixed `K`, the censored one-step kernel on `{1,...,K-1}` depends only on the first `2K-2` cookie tosses. Conditional on a stack, every cylinder probability is a finite product of terms linear in `t`; after averaging over the stack law, every censored transition probability is continuous in `t`.

Let `R_K(t)` be the substochastic matrix of transitions that remain inside `{1,...,K-1}`. By (3.5), uniformly in `t`,

\[
\|R_K(t)\|_{\infty}\le1-2^{-K}.
\tag{6.2}
\]

Hence

\[
(I-R_K(t))^{-1}=\sum_{n\ge0}R_K(t)^n
\tag{6.3}
\]

converges uniformly, and the finite-core hitting probability `a_K(t)` is continuous on `[t_0,1]`.

### Theorem 6.2 — radial continuity of escape probability

The map

\[
t\longmapsto p_{\rm esc}(t)
\]

is continuous on `[t_0,1]`, including at `t=1` even when the original stack has cookies of strength one.

#### Proof

Exactly as in (5.7), for every `t in [t_0,1]`,

\[
a_K(t)g(K)\le h_t(1)\le a_K(t).
\tag{6.4}
\]

Thus for `s,t in [t_0,1]`,

\[
|h_t(1)-h_s(1)|
\le |a_K(t)-a_K(s)|+1-g(K).
\tag{6.5}
\]

First choose `K` so that `1-g(K)` is arbitrarily small; then use continuity of `a_K` in the finite-dimensional core. This proves continuity of `h_t(1)`. The first-step factor `E[p_1(t)]` is affine in `t`, so Lemma 2.1 gives continuity of `p_esc(t)`. QED.

### Tail-only deformation has zero finite-core derivative

There is an even sharper localization statement. Suppose a parameter changes only cookie coordinates with index greater than `L`. If

\[
L\ge2K-2,
\]

then Lemma 3.1 implies that the entire stopped core below `K` is independent of that parameter. Therefore

\[
\boxed{\frac{d}{dt}a_K(t)=0}
\tag{6.6}
\]

wherever the derivative notation is meaningful, and more invariantly `a_K(t)` is exactly constant. All sensitivity to such a tail deformation is pushed behind the high-population boundary, where its total effect is at most `1-g(K)`.

This is a precise answer to the B5 question “where can a deep cookie affect escape?”: not inside a population core whose visibility radius ends before that cookie.

---

# 7. Consequence: a convergent exact representation from the finite-depth formulas

For a fixed truncation depth `M`, apply the radial weakening (6.1). For every `t<1` sufficiently close to one, the depth-`M` stack is `(IID)+(BD)+(WEL)`, so the cumulative R7-05 all-finite-depth signed-resolvent theorem gives an exact finite-dimensional value; denote it by

\[
\mathcal F_M(t).
\]

Theorem 6.2 gives

\[
\boxed{
p_{\rm esc}^{(M)}=\lim_{t\uparrow1}\mathcal F_M(t).}
\tag{7.1}
\]

Theorem 5.1 then yields the two-stage source-valid representation

\[
\boxed{
p_{\rm esc}^{(\infty)}
=\lim_{M\to\infty}\lim_{t\uparrow1}\mathcal F_M(t),}
\tag{7.2}
\]

with the explicit outer error control

\[
0\le p_{\rm esc}^{(\infty)}-p_{\rm esc}^{(M)}
\le
\mathbb E[p_1]
\sum_{j\ge\lfloor M/2\rfloor+1}\pi^q_j.
\tag{7.3}
\]

This is substantially stronger than the previous mere lower-envelope statement. It is still **PARTIAL** relative to Problem 3.12 because the source's `(SE)+(POS_1)` branch permits arbitrary stationary-ergodic spatial dependence, not just i.i.d. stacks.

---

# 8. Why the same proof does not immediately solve arbitrary `(SE)+(POS_1)`

For dependent spatial stacks one can carry the shifted environment as part of the forward state, and Lemma 3.1 remains pathwise true. Thus the local visibility radius survives. The new obstruction is different and sharper than the previous generic minimax statement.

After the stopped process reaches population `>=K`, the future spatial environment is sampled under an **exit-biased conditional law**. In the i.i.d. case, independence makes every future site fresh and the common baseline survival is the scalar `g(K)`. Under arbitrary stationary-ergodic dependence there is no reason for a uniform bound

\[
\inf_{\eta}\inf_{j\ge K}h_q(\eta,j)\longrightarrow1.
\tag{8.1}
\]

Indeed long nearly-neutral blocks can have positive conditional probability in stationary-ergodic environments. The gluing step would require an averaged or conditional replacement for (8.1) that is stable under the law of the high-boundary exit environment.

So the remaining source-level problem is no longer “do finite cookie depths approximate infinite depth?” in the i.i.d. positive case. It is to control the **environment seen at the finite-core exit** under general stationary dependence.

This is the exact issue to diagnose if the frozen metric remains unchanged for the third consecutive ordinary run.

---

# 9. Dated literature check — 2026-09-18

Primary source rechecked: Kosygina–Zerner, arXiv:1204.1895 / 2013 survey, Theorem 3.10 and Problem 3.12. The source explicitly allows `(SE)+(POS_1)` without bounded-depth in branch (3.9), and asks in Problem 3.12 to compute the never-return probability.

Zerner (2005), *Multi-excited random walks on integers*, was already checked in the preceding run: Theorem 18 gives the source-cited two-cookie formula, while the paper separately asks about continuity of return probability in the environment. Theorem 5.1 above settles one specific monotone truncation continuity direction for the i.i.d. positive infinite-stack subclass; it is not claimed to resolve Zerner's full continuity question.

Nicholas Travers (2018), *Excited Random Walk in a Markovian Environment*, EJP 23, Article 43, remains the closest dependent-environment analogue located. Its abstract explicitly says the general stationary-ergodic setting is substantially less understood and develops a broad Markovian class; the bounded search did not locate a general escape-probability formula matching Problem 3.12.

Amir–Berger–Orenshtein (2016) solves the one-dimensional directional-transience zero-one-law problem under stationary ergodic elliptic hypotheses, not Problem 3.12's quantitative escape probability.

A bounded 2026-09-18 search for `Problem 3.12`, `escape probability`, `never return`, and return-probability continuity in one-dimensional excited random walks did not surface a later full source-level computation. This remains negative evidence only; no publication-novelty claim is made.

---

# 10. Method outcomes and exact status

- **B5 — add a parameter and differentiate:** successful. Global excitation scaling is continuous all the way to potentially degenerate `p_i=1` endpoints, and a tail-only deformation has exactly zero effect on the finite stopped core once its first changed cookie lies beyond depth `2K-2`.
- **B11 — dualize:** successful. The continuity error is bounded by the stationary tail of one deliberately weakened finite-depth backward chain:
  \[
  p_{\rm esc}^{(\infty)}-p_{\rm esc}^{(M)}
  \le E[p_1]\,\pi^q([\lfloor M/2\rfloor+1,\infty)).
  \]
- **B30 — one scale at a time:** successful. Population core `<K` has the exact cookie-depth visibility radius `2K-2`, giving an identical stopped kernel for the full stack and all sufficiently deep truncations.

Full-source verdict: **PARTIAL / OPEN**. The arbitrary stationary-ergodic `(SE)+(POS_1)` branch remains unsolved. No independent P26 or distinct OTHER-track audit is claimed, and no source-level paper package is being promoted.
