Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# C0130 — finite-state Markov infinite-stack truncation continuity via a phase-corrected Lyapunov function

Date: 2026-09-18  
Slot: R7-05 Sharp Inequality Research  
Native ID: `6aabe805f32881919992996e1c5cfad6`  
Target: `C0130`, Elena Kosygina and Martin P. W. Zerner, *Excited random walks: results, methods, open problems*, Problem 3.12, printed p. 13.  
Status of this artifact: **PARTIAL relative to the full source, but a complete theorem for the finite-state spatial-Markov positive infinite-stack subclass.**

The frozen admission metric remains

`M_closed` = largest finite cookie depth `M` for which an evidenced exact closed escape-probability formula holds for every i.i.d. bounded stack law neutral after visit `M` in the transient regime.

It was already saturated over all finite depths, so this theorem does not redefine or move it:

\[
M_{\rm closed}=\infty \quad\text{over finite i.i.d. depths, unchanged.}
\]

Methods in this recovery run: **B1 / B23 / B24**.

---

## 1. What this note proves

The preceding Section-I diagnosis isolated one precise obstruction. For a full infinite positive stack and its neutral-tail truncation, the two forward branching processes have identical stopped dynamics below population `K` once `M>=2K-2`. Hence all truncation error sits at the random environment seen when the population first exits through the high boundary. In an i.i.d. environment this future is fresh; in a dependent environment it is exit-biased.

This note proves that **finite-state Markov dependence is still tame enough to close that gluing step even for genuinely infinite stacks**. In fact the two-state benchmark selected by the diagnosis extends without additional work to every finite irreducible spatial Markov chain.

The key new mechanism is not another transfer-product calculation. It is a phase-corrected negative-power Lyapunov function for a deliberately weakened finite-depth baseline. The Markov phase corrector solves a finite Poisson equation and absorbs the local variation in cookie drift. The resulting supermartingale gives a uniform-in-phase high-population survival bound. That bound is exactly what the stopped-core identity needs.

The result is quantitative: for every exponent strictly below the stationary drift surplus, the neutral-tail truncation error decays polynomially in the truncation depth.

---

## 2. Source-valid model and notation

Let `S={1,...,d}` be finite. Let `(S_x)_{x\in\mathbb Z}` be a stationary irreducible Markov chain with transition matrix `K` and stationary law `pi`:

\[
\pi K=\pi,
\qquad \pi_s>0.
\tag{2.1}
\]

Aperiodicity may be assumed, as in the selected two-state benchmark, but is not needed for the finite Poisson equation below.

State `s` carries a deterministic **infinite positive cookie stack**

\[
(p_{s,1},p_{s,2},\ldots),
\qquad
\frac12\le p_{s,i}\le1.
\tag{2.2}
\]

Define

\[
\alpha_{s,i}=2p_{s,i}-1\in[0,1],
\qquad
\delta_s=\sum_{i\ge1}\alpha_{s,i}\in[0,\infty],
\tag{2.3}
\]

and the stationary average drift

\[
\bar\delta=\sum_{s\in S}\pi_s\delta_s\in(1,\infty].
\tag{2.4}
\]

We work in the source's right-transient positive-cookie regime. No upper ellipticity assumption `p_{s,i}<=1-kappa` is needed in the theorem below; cookies of strength one are allowed.

For `M>=1`, let the neutral-tail truncation be

\[
p^{(M)}_{s,i}
=
\begin{cases}
p_{s,i},&i\le M,\\
1/2,&i>M.
\end{cases}
\tag{2.5}
\]

Write `p_esc^(infinity)` and `p_esc^(M)` for the corresponding annealed never-return probabilities.

### Forward-process convention

At a site of phase `s`, expose the independent cookie coins with success probabilities `p_{s,1},p_{s,2},...`. For `k>=1`, let `F_s(k)` be the number of successes before the `k`-th failure, with value `+infinity` if the `k`-th failure never occurs. The forward branching population evolves by

\[
V_{n+1}=F_{S_n}(V_n),
\qquad
S_{n+1}\sim K(S_n,\cdot),
\tag{2.6}
\]

with the phase transition coupled independently of the cookie uniforms conditional on `S_n`. This convention uses the current phase's stack and then advances the spatial phase. It is just an index shift of the convention in the preceding finite-state artifact.

Let

\[
h_s(k)=P_{s,k}(V_n>0\text{ for all }n\ge0),
\qquad
h_{M,s}(k)=P^{(M)}_{s,k}(V_n>0\text{ for all }n\ge0).
\tag{2.7}
\]

Positivity of the cookies gives the coordinatewise monotonicity

\[
0\le h_{M,s}(k)\le h_s(k)\le1,
\qquad
h_{M,s}(k)\uparrow\text{ in }M,
\qquad
h_{M,s}(k)\uparrow\text{ in }k.
\tag{2.8}
\]

---

## 3. Exact finite-core visibility survives Markov dependence

Fix `K_0>=2`, and censor a one-site population transition into

\[
\{0,1,\ldots,K_0-1,H\},
\]

where `H` denotes an output at least `K_0`.

Exactly as in the i.i.d. infinite-stack theorem, if the starting population is `1<=k<K_0`, this censored outcome is decided as soon as either the `k`-th failure or the `K_0`-th success appears. Therefore it uses at most

\[
k+K_0-1\le2K_0-2
\tag{3.1}
\]

cookie tosses at the current site.

Hence, whenever

\[
M\ge2K_0-2,
\tag{3.2}
\]

the full and `M`-truncated lifted chains have exactly the same stopped kernel below population `K_0`, including the Markov phase.

Let

\[
\tau_{K_0}
=
\inf\{n\ge0:V_n=0\text{ or }V_n\ge K_0\}.
\tag{3.3}
\]

At every step before `tau_{K_0}`, the event that the first `K_0` coin tosses are all successes has conditional probability at least `2^{-K_0}`. Therefore

\[
P_{s,k}(\tau_{K_0}>n)
\le(1-2^{-K_0})^n
\tag{3.4}
\]

for all phases `s` and all `1<=k<K_0`. Thus `tau_{K_0}<infinity` almost surely, without any independence across sites beyond the finite-state Markov law and without excluding cookies equal to one.

Consequently, for `M>=2K_0-2`, the full and truncated processes have the same joint law of

\[
(S_{\tau_{K_0}},V_{\tau_{K_0}}).
\tag{3.5}
\]

This is the exact gluing interface.

---

## 4. Build one common finite-depth transient baseline

Fix an exponent

\[
0<\beta<\bar\delta-1
\tag{4.1}
\]

when `bar(delta)<infinity`; if `bar(delta)=infinity`, fix any finite `beta>0`.

For `m>=1`, define the truncated average drift

\[
\bar d_m
=
\sum_{s\in S}\pi_s\sum_{i=1}^m\alpha_{s,i}.
\tag{4.2}
\]

By monotone convergence, `bar d_m ↑ bar delta`. Choose `m_0` so large that

\[
\bar d_{m_0}>1+\beta.
\tag{4.3}
\]

Then choose `t\in(0,1)` sufficiently close to one that

\[
\bar\delta_q:=t\bar d_{m_0}>1+\beta.
\tag{4.4}
\]

Define the state-dependent finite-depth weakened stack

\[
q_{s,i}
=
\begin{cases}
\frac12+t\left(p_{s,i}-\frac12\right),&1\le i\le m_0,\\
\frac12,&i>m_0.
\end{cases}
\tag{4.5}
\]

Then

\[
\frac12\le q_{s,i}\le\frac{1+t}{2}<1,
\tag{4.6}
\]

so this baseline is finite-depth and strictly upper elliptic even if the original stack contains deterministic cookies. Its phasewise drift is

\[
\delta_s^q
=t\sum_{i=1}^{m_0}\alpha_{s,i},
\qquad
\sum_s\pi_s\delta_s^q=\bar\delta_q>1+\beta.
\tag{4.7}
\]

For every `M>=m_0`, the coordinatewise ordering is

\[
q_{s,i}\le p^{(M)}_{s,i}\le p_{s,i}
\tag{4.8}
\]

for all `s,i`. Coupling with the same phase chain and the same uniforms therefore gives

\[
g_s(k)\le h_{M,s}(k)\le h_s(k),
\tag{4.9}
\]

where `g_s(k)` is the forward survival probability for the finite-depth baseline `q`.

Thus the whole problem reduces to proving that `g_s(k)` tends to one **uniformly in the finite phase** as `k→infinity`.

---

## 5. B1 — change category: a phase-corrected Lamperti Lyapunov function

The finite-depth baseline has an exact large-population decomposition. Put

\[
\alpha^q_{s,i}=2q_{s,i}-1=t\alpha_{s,i}
\qquad(1\le i\le m_0).
\tag{5.1}
\]

For every `k>=m_0`, the one-step pgf is exactly

\[
E[z^{V_{n+1}}\mid S_n=s,V_n=k]
=T(z)^kB_s^q(z),
\qquad
T(z)=\frac1{2-z},
\tag{5.2}
\]

with

\[
B_s^q(z)
=
\prod_{i=1}^{m_0}
\bigl((1-\alpha^q_{s,i})+\alpha^q_{s,i}z\bigr).
\tag{5.3}
\]

Equivalently, conditional on phase `s`,

\[
V_{n+1}\stackrel d=
G_1+\cdots+G_k+Y_s,
\tag{5.4}
\]

where the `G_i` are i.i.d. geometric random variables counting successes before one fair failure,

\[
P(G_i=j)=2^{-(j+1)},\qquad j\ge0,
\tag{5.5}
\]

and `Y_s` is the sum of independent Bernoulli variables with parameters `alpha^q_{s,1},...,alpha^q_{s,m_0}`, independent of the `G_i`.

Hence, uniformly in the finite phase set,

\[
E[V_{n+1}-k\mid s,k]=\delta_s^q,
\tag{5.6}
\]

\[
E[(V_{n+1}-k)^2\mid s,k]=2k+O(1),
\tag{5.7}
\]

and

\[
E|V_{n+1}-k|^3=O(k^{3/2}).
\tag{5.8}
\]

The geometric summands also give a uniform Chernoff bound

\[
P(|V_{n+1}-k|>k/2\mid s,k)\le C_0e^{-c_0k}.
\tag{5.9}
\]

The phasewise drift need not exceed one. The correct object is therefore not the scalar function `k^{-beta}` but a phase-corrected one.

Because

\[
\pi(\bar\delta_q\mathbf1-\delta^q)=0,
\tag{5.10}
\]

the finite Poisson equation

\[
\boxed{
(I-K)c
=
\beta(\bar\delta_q\mathbf1-\delta^q)
}
\tag{5.11}
\]

has a solution `c`, unique after fixing `pi c=0`.

Choose `a>2||c||_infinity+2` and define

\[
F(s,k)
=(k+a)^{-\beta}
\left(1+\frac{c_s}{k+a}\right).
\tag{5.12}
\]

Then `F(s,k)>0` for every phase and every `k>=0`.

### Lemma 5.1 — uniform one-step expansion

For the baseline chain,

\[
E[F(S_{n+1},V_{n+1})\mid S_n=s,V_n=k]-F(s,k)
\]

has the uniform asymptotic

\[
\boxed{
\beta(\beta+1-\bar\delta_q)
(k+a)^{-\beta-1}
+o(k^{-\beta-1}).
}
\tag{5.13}
\]

In particular, since `beta+1<bar delta_q`, there exists `L<infinity` such that

\[
\boxed{
E[F(S_{n+1},V_{n+1})\mid s,k]\le F(s,k)
\quad\text{for every }s\text{ and }k>L.
}
\tag{5.14}
\]

#### Proof

Write `y=k+a` and `Delta=V_{n+1}-k`. On the event `|Delta|<=k/2`, Taylor expansion gives, uniformly in `s`,

\[
(V_{n+1}+a)^{-\beta}
=
y^{-\beta}
-\beta y^{-\beta-1}\Delta
+\frac{\beta(\beta+1)}2y^{-\beta-2}\Delta^2
+R,
\tag{5.15}
\]

with

\[
E|R|=O(y^{-\beta-3}E|\Delta|^3)
=O(k^{-\beta-3/2}).
\tag{5.16}
\]

On the complement, `F` is bounded and (5.9) makes the contribution exponentially small. Using (5.6)-(5.7),

\[
E[(V_{n+1}+a)^{-\beta}\mid s,k]
=
y^{-\beta}
+\beta(\beta+1-\delta_s^q)y^{-\beta-1}
+o(y^{-\beta-1}).
\tag{5.17}
\]

Likewise

\[
E[(V_{n+1}+a)^{-\beta-1}\mid s,k]
=
y^{-\beta-1}+o(y^{-\beta-1}).
\tag{5.18}
\]

The next phase `t` is sampled from `K(s,\cdot)`, so

\[
\begin{aligned}
E[F(S_{n+1},V_{n+1})\mid s,k]
={}&y^{-\beta}\\
&+y^{-\beta-1}
\left[
\beta(\beta+1-\delta_s^q)+(Kc)_s
\right]
+o(y^{-\beta-1}).
\end{aligned}
\tag{5.19}
\]

Subtract

\[
F(s,k)=y^{-\beta}+c_sy^{-\beta-1}.
\]

By (5.11),

\[
(Kc-c)_s
=
\beta(\delta_s^q-\bar\delta_q),
\tag{5.20}
\]

so the phase dependence cancels exactly and (5.13) follows. QED.

### Theorem 5.2 — uniform high-population safety for the finite-state Markov baseline

For every `beta` satisfying (4.1), there is `C_beta<infinity` such that

\[
\boxed{
1-g_s(k)
\le C_\beta(1+k)^{-\beta}
\qquad
\text{for every phase }s\text{ and every }k\ge1.
}
\tag{5.21}
\]

#### Proof

Take `L` from (5.14) and let

\[
\sigma_L=\inf\{n\ge0:V_n\le L\}.
\tag{5.22}
\]

For `k>L`, the stopped process

\[
F(S_{n\wedge\sigma_L},V_{n\wedge\sigma_L})
\]

is a nonnegative supermartingale. Put

\[
m_L=
\min_{s\in S,\ 0\le j\le L}F(s,j)>0.
\tag{5.23}
\]

Optional stopping gives

\[
m_LP_{s,k}(\sigma_L\le n)
\le
E_{s,k}F(S_{n\wedge\sigma_L},V_{n\wedge\sigma_L})
\le F(s,k).
\tag{5.24}
\]

Letting `n→infinity`,

\[
P_{s,k}(\sigma_L<\infty)
\le
\frac{F(s,k)}{m_L}
\le C_\beta(1+k)^{-\beta}
\tag{5.25}
\]

uniformly in `s`. Extinction requires a visit to population zero and hence a visit to `{0,...,L}`. Therefore

\[
1-g_s(k)
\le P_{s,k}(\sigma_L<\infty),
\]

which gives (5.21). QED.

This is the missing phase-uniform boundary estimate. Its proof uses only the finite-state Poisson corrector; it does not require the environment at a random exit time to be stationary or unbiased.

---

## 6. B23 — the long-persistence counterexample attempt fails for a structural reason

The diagnostic recovery action explicitly required an obstruction-first attempt. The natural candidate is a two-state chain with a long-persistent weak phase `B` and a compensating strong phase `G`. One might hope that conditioning on a high-population exit selects the beginning of an unusually long `B` block, making truncation unsafe even though the stationary average drift is above one.

At the scalar level this is a real obstruction: the local drift `delta_B^q` may be far below one, so `k^{-beta}` alone need not be superharmonic in phase `B`.

But for a finite irreducible Markov chain the persistence bias is exactly a finite Poisson-coboundary effect. Equation (5.11) constructs `c_B,c_G` so that

\[
\beta(\beta+1-\delta_s^q)+(Kc-c)_s
=
\beta(\beta+1-\bar\delta_q)
<0
\tag{6.1}
\]

in **both phases simultaneously**. No choice of finite transition probabilities with stationary average `bar delta_q>1+beta` can evade this cancellation. Long bad runs alter the bounded corrector but cannot change the negative averaged coefficient.

Thus the intended two-state counterexample route fails, and it fails for a theorem-level reason rather than because a numerical search happened not to find parameters.

This also explains where a genuinely general stationary-ergodic counterexample, if one exists, would have to live: in dependence for which the centered drift is not representable by a bounded finite-state Poisson corrector and the random-exit bias can create an unbounded effective correction.

---

## 7. B24 — extremal boundary object: the weakened finite-depth baseline controls every deep tail

Fix the baseline `q` chosen in Section 4. For every `M>=m_0`, every phase `s`, and every population `j`, coordinatewise monotonicity gives

\[
1-h_s(j)
\le1-g_s(j),
\qquad
1-h_{M,s}(j)
\le1-g_s(j).
\tag{7.1}
\]

By Theorem 5.2,

\[
\boxed{
\max\{1-h_s(j),1-h_{M,s}(j)\}
\le C_\beta(1+j)^{-\beta}.
}
\tag{7.2}
\]

Therefore, among the full stack and all sufficiently deep neutral-tail truncations, the largest high-population extinction defect is controlled by a **single finite-depth weakened chain**. For the gluing problem this baseline is the useful extremal object: no optimization over the infinitely many tail cookies is required.

The importance of (7.2) is that it is uniform in phase. The environment seen at `tau_K` may be strongly exit-biased; after conditioning on its phase, (7.2) applies pointwise. The Palm-density/uniform-integrability obstruction from the preceding stuck report disappears completely in finite-state Markov environments.

---

## 8. Main gluing theorem

### Theorem 8.1 — quantitative neutral-tail continuity for finite-state Markov infinite stacks

Assume Sections 2-4. For every finite exponent

\[
0<\beta<\bar\delta-1
\tag{8.1}
\]

(with arbitrary finite `beta>0` if `bar delta=infinity`), there exists `C_beta<infinity` such that, for all sufficiently large `M`,

\[
\boxed{
0\le
\sup_{s\in S}
\bigl(h_s(1)-h_{M,s}(1)\bigr)
\le
C_\beta M^{-\beta}.
}
\tag{8.2}
\]

Consequently

\[
\boxed{
 p_{\rm esc}^{(M)}\uparrow p_{\rm esc}^{(\infty)}
}
\tag{8.3}
\]

and, with a possibly enlarged constant,

\[
\boxed{
0\le p_{\rm esc}^{(\infty)}-p_{\rm esc}^{(M)}
\le C_\beta M^{-\beta}.
}
\tag{8.4}
\]

#### Proof

Set

\[
K_M=\lfloor M/2\rfloor+1.
\tag{8.5}
\]

Then

\[
2K_M-2=2\lfloor M/2\rfloor\le M.
\tag{8.6}
\]

For sufficiently large `M`, also `M>=m_0`. By Section 3, the full and truncated lifted chains started from any phase `s` and population `1` have exactly the same stopped law at `tau_{K_M}`.

For either survival function `r` equal to `h` or `h_M`, harmonicity and almost-sure finiteness of `tau_{K_M}` give

\[
r_s(1)
=
E_{s,1}\left[
 r_{S_{\tau_{K_M}}}(V_{\tau_{K_M}});
 V_{\tau_{K_M}}\ge K_M
\right].
\tag{8.7}
\]

On the high-boundary event, (7.2) yields

\[
1-C_\beta(1+K_M)^{-\beta}
\le
r_{S_{\tau_{K_M}}}(V_{\tau_{K_M}})
\le1.
\tag{8.8}
\]

Let

\[
a_{K_M}(s)
=P_{s,1}(V_{\tau_{K_M}}\ge K_M)
\tag{8.9}
\]

for the common stopped core. Then both `h_s(1)` and `h_{M,s}(1)` lie in the same interval

\[
a_{K_M}(s)
\left[1-C_\beta(1+K_M)^{-\beta}\right]
\le r_s(1)\le a_{K_M}(s).
\tag{8.10}
\]

Since the full stack dominates the truncation,

\[
0\le h_s(1)-h_{M,s}(1)
\le C_\beta(1+K_M)^{-\beta}.
\tag{8.11}
\]

As `K_M` is comparable to `M`, this gives (8.2).

For the excited walk itself, condition on the phase `r` of the origin stack. A no-return trajectory in the right-transient regime must first step to `+1`. Conditional on that step, the phase at site `1` is `s` with probability `K(r,s)`. The standard forward/backward finite-interval identity, which is pathwise and does not use bounded cookie depth, therefore gives

\[
p_{\rm esc}^{(\infty)}
=
\sum_{r,s}
\pi_r p_{r,1}K(r,s)h_s(1),
\tag{8.12}
\]

and, for every sufficiently large transient truncation,

\[
p_{\rm esc}^{(M)}
=
\sum_{r,s}
\pi_r p_{r,1}K(r,s)h_{M,s}(1).
\tag{8.13}
\]

Subtracting and using (8.2) proves (8.4). Monotonicity in `M` gives (8.3). QED.

---

## 9. Corollary: the finite-depth exact resolvents converge to the infinite-stack answer

The preceding finite-state Markov artifact proved an exact finite-dimensional escape-resolvent formula for every finite cookie depth with stationary average drift above one. Denote that exact formula for the depth-`M` truncation by

\[
\mathcal F_M(K,\pi,\{p_{s,i}:i\le M\}).
\tag{9.1}
\]

For all sufficiently large `M`, the truncated average drift is above one, so the formula applies. Theorem 8.1 yields the rigorous limit representation

\[
\boxed{
 p_{\rm esc}^{(\infty)}
=
\lim_{M\to\infty}
\mathcal F_M(K,\pi,\{p_{s,i}:i\le M\}).
}
\tag{9.2}
\]

Moreover, for every `beta<bar delta-1`, the truncation error is `O(M^{-beta})`.

Thus the entire finite-state spatial-Markov positive infinite-stack subclass is now reduced to an explicit sequence of finite-dimensional resolvents with a proved rate of convergence.

This strictly contains the two-state benchmark selected by the stuck diagnosis and removes the benchmark's temporary upper-ellipticity assumption.

---

## 10. Scope, source status, and what remains open

This theorem is **not** a full solution of Kosygina--Zerner Problem 3.12.

It settles the exit-biased gluing problem for finite-state spatial-Markov positive infinite stacks, but the source's `(SE)+(POS_1)` branch allows arbitrary stationary-ergodic spatial dependence. In that generality the centered finite-prefix drift need not admit a bounded Poisson corrector. The current proof uses the finite-state identity

\[
(I-K)c=\beta(\bar\delta_q\mathbf1-\delta^q)
\tag{10.1}
\]

in an essential way.

The precise surviving obstacle is therefore sharper than before:

> For a general stationary-ergodic positive environment, find a replacement for the bounded finite-state phase corrector strong enough to make a negative-power high-population Lyapunov function superharmonic under the exit-biased future law, or construct a stationary-ergodic counterexample showing that no such uniform truncation continuity can hold.

The earlier `phi`-mixing/Gordin transfer theorem controls weighted products along deterministic spatial time, but it does not by itself produce the bounded pointwise corrector used in (5.11). A natural next class is therefore stationary environments for which the finite-prefix drift observable has a bounded coboundary or a sufficiently strong martingale-coboundary decomposition.

---

## 11. Dated literature check — 2026-09-18

Primary source:

- Elena Kosygina and Martin P. W. Zerner, *Excited random walks: results, methods, open problems*, arXiv:1204.1895, Problem 3.12.

Key later dependence paper:

- Nicholas F. Travers, *Excited Random Walk in a Markovian Environment*, Electronic Journal of Probability 23 (2018), paper 43, arXiv:1611.01681. Travers treats a broad spatial-Markov class and emphasizes that general stationary-ergodic environments are substantially less understood.

Related source-problem resolution:

- Gideon Amir, Noam Berger, Tal Orenshtein, *Zero-one law for directional transience of one dimensional excited random walks*, Ann. IHP Probab. Stat. 52 (2016), 47-57. This resolves a directional-transience zero-one question in stationary ergodic elliptic environments, not Problem 3.12's quantitative never-return probability.

A bounded fresh search on 2026-09-18 for the exact Problem 3.12 escape probability, Markovian infinite cookie stacks, stationary-ergodic never-return probability, and later author/follow-up work did not reveal a later general formula matching Theorem 8.1 or a full solution of Problem 3.12. This is **negative search evidence only**, not a claim of novelty or worldwide openness.

---

## 12. Method outcomes and fixed metric

### B1 — change mathematical category

**Outcome: success.** Replaced the exit-biased environment-law problem by a phase-corrected Lamperti/Lyapunov problem. The finite Poisson equation removes phase drift variation and yields the uniform survival estimate (5.21).

### B23 — do what the proposer did not expect

**Outcome: obstruction attempt fails constructively.** A long-persistent two-state weak phase cannot create the desired failure as long as the spatial phase is a finite irreducible Markov chain and the stationary drift surplus is positive. The bounded Poisson corrector cancels the local bad-phase drift at first order.

### B24 — find the extremal object

**Outcome: success.** A single radially weakened finite-depth baseline `q` is the extremal upper bound for the high-population extinction defect of both the full stack and every sufficiently deep truncation. This converts the random exit law into a harmless phase label.

### Frozen metric

\[
\boxed{M_{\rm closed}:\infty\to\infty\quad\text{NO MOVEMENT}.}
\]

The source-level mathematical state remains **PARTIAL / OPEN**.

---

## 13. Next mathematical attack

The next ordinary run must not repeat B1/B23/B24. The most useful next triple is

- **B6 — deform from a solved case:** approximate a dependent stationary process by classes with an explicit bounded corrector and identify exactly which norm of the corrector enters the high-population estimate;
- **B28 — replace for-all by typical:** control the high-population extinction defect only under the exit-induced law rather than uniformly over environments;
- **B30 — one scale at a time:** formulate and prove a gluing theorem under a source-valid quantitative dependence hypothesis (for example a bounded drift-coboundary or strong mixing condition), then isolate precisely what prevents passage to arbitrary `(SE)+(POS_1)`.

The fixed metric is already saturated and therefore does not move in this theorem. Under the owner protocol this is the first ordinary no-movement recovery run after the mandatory post-movement STUCK1 diagnosis; the ordinary unchanged count advances from `3` to `4`.