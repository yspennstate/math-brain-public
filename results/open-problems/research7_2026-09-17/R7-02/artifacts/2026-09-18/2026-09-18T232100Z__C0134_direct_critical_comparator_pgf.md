Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# C0134 — direct critical-comparator proof by stationary PGF and a monotone transform

Date: 2026-09-18 UTC  
Slot: `R7-02 Finite Certificate Research`  
Native ID: `6aabe797a39081919acc889f29f4c556`  
Target: `C0134` — Kosygina–Zerner, *Excited random walks: results, methods, open problems*, Problem 5.3  
Run-start master: `53077e74e2d9f443e1efbf1749eca865aa8c612a`  
Fresh master immediately before delivery: `23ea0d6a0918c66d8e0743c0a5abbc24f9ec8a70`  
Previous report: `research7_2026-09-17/R7-02/runs/2026-09-18/2026-09-18T221800Z__report.md`  
Frozen source metric: `M_clause = 2/2` (already saturated; this artifact is an independent checksum, not a third source clause).

This artifact executes the STUCK1 recovery action selected in the preceding report. The methods are **B10 / B13 / B17**. The new mathematical point is a direct proof of the critical finite-support comparator's infinite cycle area, with no invocation of Kosygina–Zerner Theorem 5.4 and with no assumption that an invariant law has finite first moment.

## 1. The finite critical comparator

Fix

\[
0<a\le \frac16,
\]

and let the iid emigration variables `L_n` have law

\[
\mathbb P(L=0)=a,\qquad
\mathbb P(L=2)=1-3a,\qquad
\mathbb P(L=3)=2a.
\tag{1.1}
\]

Then `EL=2`. Let `xi_{n,j}` be iid geometric failure variables

\[
\mathbb P(\xi=k)=2^{-(k+1)},\qquad k\in\mathbb Z_+,
\]

so that

\[
g(s):=\mathbb E s^\xi=\frac1{2-s},\qquad
\mathbb E\xi=1,\qquad \operatorname{Var}(\xi)=2.
\]

Put `S_r=xi_1+...+xi_r`, `S_0=0`, and consider

\[
D_{n+1}=S_{(D_n+1-L_n)_+}.
\tag{1.2}
\]

Starting from zero, let

\[
\sigma:=\inf\{n\ge1:D_n=0\},\qquad
A:=\sum_{0\le n<\sigma}D_n.
\tag{1.3}
\]

The checksum selected by the preceding STUCK1 report is

\[
\boxed{\mathbb E_0 A=\infty.}
\tag{SC}
\]

The proof below is entirely internal to (1.1)–(1.3).

# 2. B10 — DERANDOMIZE: an exact one-variable PGF recurrence

## 2.1 Positive recurrence without a stationary-moment assumption

For every `x>=2`, clipping in `(x+1-L)_+` is harmless because `L<=3`, and therefore

\[
\mathbb E[D_{n+1}\mid D_n=x]
=\mathbb E(x+1-L)=x-1.
\tag{2.1}
\]

Thus the Lyapunov function `V(x)=x` has exact drift `-1` outside the finite set `{0,1}`. The one-step means from 0 and 1 are finite. The chain is irreducible: from 0, the event `L=0` followed by `xi=y` reaches every `y`, and from every finite state there is positive probability that all offspring variables equal zero. Hence the standard countable-state Foster criterion gives positive recurrence and a unique invariant probability `pi`.

Write

\[
p:=\pi(0),\qquad r:=\pi(1),\qquad
\Phi(s):=\sum_{x\ge0}\pi(x)s^x.
\tag{2.2}
\]

No finiteness of `E_pi D` is assumed.

## 2.2 Exact conditional PGFs

Fix an integer `u>=1` and set

\[
s=1-\frac1u,\qquad
g=g(s)=\frac{u}{u+1}=1-\frac1{u+1}.
\tag{2.3}
\]

For `x=0`,

\[
Q_0(s)=1-a+ag.
\tag{2.4}
\]

For `x=1`,

\[
Q_1(s)=1-a+ag^2.
\tag{2.5}
\]

For every `x>=2`,

\[
Q_x(s)
=a g^{x+1}+(1-3a)g^{x-1}+2a g^{x-2}
=A_u g^x,
\tag{2.6}
\]

where

\[
A_u:=ag+(1-3a)g^{-1}+2ag^{-2}
=1+\frac1u+\frac{a(3u+2)}{u^2(u+1)}.
\tag{2.7}
\]

A useful factorization is

\[
\boxed{
A_u=\left(1+\frac1u\right)
\left(1+\frac{a(3u+2)}{u(u+1)^2}\right).
}
\tag{2.8}
\]

Stationarity now gives the exact scalar identity

\[
\Phi(s)
=A_u\bigl(\Phi(g)-p-rg\bigr)
+p(1-a+ag)+r(1-a+ag^2).
\tag{2.9}
\]

Define

\[
\psi(u):=1-\Phi\!\left(1-\frac1u\right).
\tag{2.10}
\]

Then `(2.9)` is exactly

\[
\boxed{
\psi(u)=A_u\psi(u+1)+F_u,
}
\tag{2.11}
\]

with

\[
F_u=
\frac{c_1u^2+c_2u+2a(p-1)}{u^2(u+1)},
\tag{2.12}
\]

where

\[
c_1=p(1+a)+2ar-1,
\qquad
c_2=3ap+2ar-3a+p-1.
\tag{2.13}
\]

This recurrence is exact and used no differentiation of `Phi` at one.

# 3. B13 — FIND WHAT ONLY INCREASES

## 3.1 Normalize away the critical `1+1/u` factor

Let

\[
P_1:=1,
\qquad
P_u:=\prod_{k=1}^{u-1}A_k\quad(u\ge2),
\qquad
T_u:=P_u\psi(u).
\tag{3.1}
\]

Equation `(2.11)` becomes

\[
\boxed{T_{u+1}=T_u-P_uF_u.}
\tag{3.2}
\]

From `(2.8)`,

\[
P_u
=uR_u,
\qquad
R_u:=\prod_{k=1}^{u-1}
\left(1+\frac{a(3k+2)}{k(k+1)^2}\right).
\tag{3.3}
\]

The added terms are nonnegative and summable, so

\[
R_u\uparrow R_\infty\in(1,\infty).
\tag{3.4}
\]

In particular there is a finite constant `C_a` such that

\[
u\le P_u\le C_a u,
\qquad
\frac{P_u}{u}\longrightarrow R_\infty.
\tag{3.5}
\]

Since `Phi(s)->1` as `s↑1`, we have `psi(u)->0`; hence

\[
\frac{T_u}{u}=\frac{P_u}{u}\psi(u)\longrightarrow0.
\tag{3.6}
\]

## 3.2 The boundary identity is forced without `E_pi D<infinity`

Suppose `c_1 != 0`. From `(2.12)`,

\[
F_u\sim\frac{c_1}{u},
\]

and therefore by `(3.5)`

\[
P_uF_u\longrightarrow R_\infty c_1.
\]

Telescoping `(3.2)` and dividing by `u` would then give

\[
\frac{T_u}{u}\longrightarrow -R_\infty c_1,
\]

contradicting `(3.6)`. Consequently

\[
\boxed{p(1+a)+2ar=1.}
\tag{3.7}
\]

This recovers the earlier stationary overshoot identity, but now without assuming that the stationary first moment exists.

Substituting `(3.7)` into `(2.12)` gives the much simpler exact forcing term

\[
\boxed{
F_u
=-\frac{a\bigl((3-2p)u+2(1-p)\bigr)}{u^2(u+1)}.
}
\tag{3.8}
\]

Because `p<1` and `a>0`, this is strictly negative for every `u>=1`. Therefore `(3.2)` supplies the promised monovariant:

\[
\boxed{T_{u+1}>T_u\quad\text{for every }u.}
\tag{3.9}
\]

More quantitatively, using `P_u>=u`,

\[
T_{u+1}-T_u
=P_u(-F_u)
\ge \frac{a(3-2p)}{u+1}.
\tag{3.10}
\]

Thus `T_u` grows at least harmonically and in particular

\[
T_u\longrightarrow\infty.
\tag{3.11}
\]

Combining `(3.5)` and `(3.11)` gives

\[
\boxed{
u\,\psi(u)\longrightarrow\infty.}
\tag{3.12}
\]

There is in fact an exact first-order asymptotic. From `(3.8)` and `(3.5)`,

\[
P_u(-F_u)
\sim \frac{R_\infty a(3-2p)}{u}.
\]

Hence

\[
T_u\sim R_\infty a(3-2p)\log u,
\]

and dividing by `P_u~R_infinity u` yields

\[
\boxed{
1-\Phi\!\left(1-\frac1u\right)
\sim a(3-2\pi(0))\,\frac{\log u}{u}.
}
\tag{3.13}
\]

This is the critical harmonic stationary tail signature expected at the first-moment boundary.

## 3.3 Infinite stationary first moment, proved rather than assumed

For every nonnegative integer `x`,

\[
\frac{1-s^x}{1-s}=1+s+\cdots+s^{x-1}\uparrow x
\qquad(s\uparrow1).
\]

Therefore monotone convergence gives, with `+infinity` allowed,

\[
\lim_{s\uparrow1}\frac{1-\Phi(s)}{1-s}
=\mathbb E_\pi D.
\tag{3.14}
\]

Equation `(3.12)` is exactly divergence of this quotient along `s=1-1/u`, so

\[
\boxed{\mathbb E_\pi D=\infty.}
\tag{3.15}
\]

## 3.4 Convert stationary divergence into first-cycle area divergence

Positive recurrence gives

\[
\mathbb E_0\sigma=\frac1{\pi(0)}<\infty.
\tag{3.16}
\]

For the bounded reward `r_M(x)=x\wedge M`, the elementary regenerative occupation formula at the atom zero gives

\[
\mathbb E_\pi r_M(D)
=
\frac{
\mathbb E_0\sum_{0\le n<\sigma}r_M(D_n)
}{\mathbb E_0\sigma}.
\tag{3.17}
\]

Letting `M→infinity`, the left side increases to `E_pi D=infinity` by `(3.15)`, while the denominator stays finite by `(3.16)`. Hence the truncated cycle rewards diverge, and monotone convergence yields

\[
\boxed{
\mathbb E_0\sum_{0\le n<\sigma}D_n=\infty.
}
\tag{3.18}
\]

This proves `(SC)` directly.

### Theorem 3.1 (direct critical-comparator checksum)

For every `0<a<=1/6`, the chain `(1.2)` with the three-point critical emigration law `(1.1)` is positive recurrent but has infinite invariant first moment and infinite expected first-cycle total progeny. More precisely, if `Phi` is its invariant PGF, then `(3.13)` holds.

No part of this theorem uses Kosygina–Zerner Theorem 5.4, and no finite invariant moment is assumed at any stage.

**B10 outcome: SUCCESS.** The finite-support recursion reduces exactly to `(2.11)`.  
**B13 outcome: SUCCESS.** `T_u=P_u psi(u)` is a strict monovariant with harmonic growth, forcing the stationary first moment and cycle area to diverge.

# 4. B17 — LOOK FOR THE NUMBERS ELSEWHERE: classical migration parameter match

A fresh theorem-level comparison was made with George P. Yanev and Nikolay M. Yanev, *Limit Theorems for Branching Processes with Random Migration Stopped at Zero* (1997), DOI `10.1007/978-1-4612-1862-3_25`.

Their assumptions `(2.1)` require critical offspring mean one, finite offspring variance `2b`, finite immigration mean, and **bounded** family and individual emigration. Their criticality parameter is

\[
\theta=\frac{r\lambda-p_{\rm em}(e_1+e_2)}{b}.
\tag{4.1}
\]

The stopped positive excursion of our comparator fits their bounded-migration architecture as follows.

- Offspring are geometric with variance two, so `b=1`.
- When `L=0` (probability `a`), one extra parent is reproduced. This has the same distribution as ordinary reproduction from the current population plus an independent geometric offspring family, so the immigration probability is `r=a` and the immigration mean is `lambda=1`.
- There is no no-migration case: `q=0`.
- When `L` is 2 or 3 (total probability `p_em=1-a`), respectively one or two parent families are removed before reproduction. Conditional on the emigration regime,

\[
\mathbb P(\eta_1=1)=\frac{1-3a}{1-a},\qquad
\mathbb P(\eta_1=2)=\frac{2a}{1-a},
\]

so

\[
e_1=\frac{1+a}{1-a},\qquad e_2=0.
\]

Consequently

\[
\boxed{
\theta
=a-(1-a)\frac{1+a}{1-a}
=-1.
}
\tag{4.2}
\]

Their Theorem 2.1 then places this comparator in the `theta<0` critical-migration regime and, for a finite-mean initial law, gives a survival exponent corresponding to `beta=(1-theta)^+=2`, together with finite expected lifetime. This matches exactly the exponent underlying the bounded-cookie critical `delta=2` picture.

This is important prior-art information, not a novelty claim. The direct PGF proof in Sections 2–3 is an independent self-contained checksum, but the **critical comparator itself lies squarely in classical bounded-migration theory**.

Equally important, the same 1997 paper does **not** directly settle the arbitrary-`N` scalar theorem used in the cumulative C0134 argument: its displayed assumptions `(2.1)` explicitly impose finite deterministic bounds on the family and individual emigration variables. Arbitrary positive cookie stacks can produce an unbounded `N`. The current R7-02 source-level route therefore still relies on its separate same-mean finite-support convex-order comparison to transfer from arbitrary `N` to the bounded comparator.

The 1997 theorem excerpt inspected here gives survival and conditional population asymptotics; this run does not claim that its displayed theorem alone states our total-cycle-area divergence. Section 3 above supplies that divergence directly.

**B17 outcome: SUCCESS / PRIOR-ART COLLISION ON THE CHECKSUM ONLY.** The exact number `theta=-1` explains the `t^{-2}` life-period exponent and independently locates the comparator in known bounded migration theory. It does not, under the inspected hypotheses, cover the arbitrary unbounded emigration law needed for the full POS1 source extension.

# 5. Fresh source-status check (2026-09-18 UTC)

Primary source checked again:

- Elena Kosygina and Martin P. W. Zerner, *Excited random walks: results, methods, open problems*, Bulletin of the Institute of Mathematics Academia Sinica 8 (2013), Problem 5.3, author PDF `https://www.math.uni-tuebingen.de/user/zerner/pub/KosyginaZerner.pdf`.
- The literal source text has Theorem 5.2 under `(IID)+(BD)+(WEL)` and asks in Problem 5.3 whether `(BD)` can be replaced by `(POS1)`.

Relevant later work checked:

- Omar Chakhtoun, *One-Dimensional Excited Random Walk with Unboundedly Many Excitations Per Site* (PhD dissertation, 2019), CUNY Academic Works. Its public abstract explicitly says the unbounded framework requires a **tail decay estimate on the number of excitations per site**. That public scope is therefore not the unrestricted `(IID)+(WEL)+(POS1)` source statement, but theorem-level comparison remains necessary before any novelty claim.
- Travers (2018) extends one-dimensional excited-walk results to a broad class of Markovian cookie environments. This is relevant context but not, from the inspected statements, an unrestricted arbitrary-iid-positive-stack resolution of Problem 5.3.
- Yanev–Yanev (1997) is now mapped above at theorem-parameter level for the bounded comparator. It requires bounded migration in its displayed `(2.1)` assumptions.

A bounded search dated 2026-09-18 did not locate a paper explicitly advertising a complete solution to the literal Kosygina–Zerner Problem 5.3. This is negative evidence only and is **not** a novelty or openness certificate.

# 6. Consequence for the cumulative C0134 candidate proof

The frozen source metric remains `M_clause=2/2`; this artifact does not manufacture a third clause. What changes is proof risk:

1. the most delicate finite critical comparator no longer depends on importing KZ Theorem 5.4;
2. its infinite cycle area follows from an exact scalar PGF recurrence and monovariant;
3. the classical migration parameter maps to `theta=-1`, independently confirming that this is the correct critical regime;
4. classical bounded-migration theory does not, under the inspected hypotheses, replace the universal convex-order transfer from arbitrary unbounded `N`.

The full source theorem therefore remains **CANDIDATE SOURCE-LEVEL COMPLETE / operationally PARTIAL**, pending theorem-level prior-art reconciliation of the arbitrary-`N` transfer, paper synchronization, and the protocol-required independent P26 plus distinct OTHER-track audits.

# 7. Failed/limited routes and next attack

- B10 did not produce a killed Green matrix in closed form; the stronger useful object was the one-variable invariant-PGF recurrence `(2.11)`.
- B13 succeeds for the finite critical comparator but does not by itself verify the universal convex-order kernel comparison used for arbitrary unbounded `N`.
- B17 reveals that the comparator is classical-shaped; it therefore reduces, rather than increases, any novelty claim about that component. The exact unrestricted source extension still needs a complete prior-art map.

If the target remains active, the next nonrepeating ordinary-method triple is **B11 / B23 / B30**:

- **B11 dualize:** reprove the arbitrary-`N` convex-order transition comparison using only stop-loss test functions and the dual cone, to stress every quantifier;
- **B23 assume the opposite:** try to construct a heavy-tailed `N` with `1<EN<=2` for which the same-mean bounded comparator fails at some finite time or cycle functional;
- **B30 one scale at a time:** truncate unbounded `N` by tail scales and prove a limit theorem for the stopped cycle that either independently validates or breaks the universal transfer.

Metric movement: `2/2 -> 2/2` (**NO MOVEMENT**). Ordinary unchanged-research count: `3 -> 4`.