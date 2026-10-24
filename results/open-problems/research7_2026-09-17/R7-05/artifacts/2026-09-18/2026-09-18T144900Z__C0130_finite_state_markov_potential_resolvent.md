Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# C0130 — finite-state spatial Markov environments: weighted-cocycle asymptotics and an exact finite escape resolvent

Date: 2026-09-18  
Slot: R7-05 Sharp Inequality Research  
Native ID: `6aabe805f32881919992996e1c5cfad6`  
Target: `C0130`, Elena Kosygina and Martin P. W. Zerner, *Excited random walks: results, methods, open problems*, Problem 3.12.  
Status of this artifact: **PARTIAL relative to the full source, but a complete theorem for a new source-valid finite-state spatial-Markov subclass.**

This note continues

- `research7_2026-09-17/R7-05/artifacts/2026-09-18/2026-09-18T140250Z__C0130_all_finite_depth_signed_resolvent_theorem.md`, which computes the whole `(IID)+(BD)+(WEL)` branch at every finite cookie depth; and
- `research7_2026-09-17/R7-05/artifacts/2026-09-18/2026-09-18T141900Z__C0130_spatial_periodic_transfer_resolvent.md`, which proves an exact phase-lifted transfer reduction for spatial-periodic positive environments.

The frozen metric `M_closed` is already saturated at all finite i.i.d. depths. It therefore does **not** move in this note. The purpose here is to attack the genuinely dependent `(SE)+(POS_1)` side rather than manufacture a new metric.

Methods in this research step: **B1 / B12 / B28**.

---

## 1. Source scope and current literature check

The current arXiv version of Kosygina--Zerner is `arXiv:1204.1895v2` (last revised 2012-10-08). Problem 3.12 still asks:

> Compute in the transient case the probability `P_0[forall n>=1: X_n != 0]` never to return to the starting point.

The problem sits immediately after Theorem 3.10, whose one-dimensional transience criteria include the positive stationary-ergodic branch and the bounded i.i.d. branch. The exact source problem therefore is not exhausted by the all-finite-depth i.i.d. theorem above.

The key later source used here is Nicholas F. Travers, *Excited Random Walk in a Markovian Environment*, EJP 23 (2018), paper 43, arXiv:1611.01681v3. Travers considers spatial Markov chains of bounded elliptic cookie stacks. His Assumption (A) asks that the forward stack chain and the reversed stack chain be uniformly ergodic; every irreducible aperiodic finite-state chain satisfies this. Travers extends the i.i.d. transience threshold and develops the joint forward branching process `(U_n,S_n)` under the averaged law.

Fresh bounded searches on 2026-09-18 for Problem 3.12, the exact never-return probability, Markovian spatial environments, and later author/citing work recovered Travers and the Amir--Berger--Orenshtein directional-transience zero-one law, but did **not** recover a later paper computing the general escape probability or the finite-state spatial-Markov formula proved below. This is negative evidence only; novelty and worldwide openness remain **UNVERIFIED**.

---

## 2. The source-valid finite-state Markov subclass

Let `S={1,...,d}` be finite. Let `(S_x)_{x in Z}` be a stationary irreducible aperiodic Markov chain with transition matrix `K` and stationary row vector `pi`:

\[
\pi K=\pi,
\qquad \pi_s>0.
\]

State `s` carries a deterministic positive elliptic stack of common finite height `M`:

\[
\omega_s=(p_{s,1},\ldots,p_{s,M},1/2,1/2,\ldots),
\qquad \frac12\le p_{s,i}<1.
\]

Allowing state-dependent heights is equivalent after padding with `1/2`, so a common `M` loses nothing for the finite-state bounded class.

Put

\[
\alpha_{s,i}=2p_{s,i}-1\in[0,1),
\qquad
\delta_s=\sum_{i=1}^M\alpha_{s,i},
\qquad
\bar\delta=\sum_s\pi_s\delta_s.
\]

Assume

\[
\boxed{\bar\delta>1.}\tag{2.1}
\]

The spatial law is stationary and ergodic and satisfies the positive-cookie hypothesis. The finite state space plus ellipticity gives uniform ellipticity automatically. Thus this is a genuine subclass of the source's positive stationary-ergodic transient regime.

For each state define

\[
T(z)=\frac1{2-z},
\qquad
B_s(z)=\prod_{i=1}^M\bigl((1-\alpha_{s,i})+\alpha_{s,i}z\bigr).
\tag{2.2}
\]

Then `B_s` is an honest pgf and

\[
B_s'(1)=\delta_s.
\tag{2.3}
\]

The exact one-site calculation from the cumulative finite-depth theorem says that, for the forward branching chain, every row with population `k>=M` has pgf

\[
\boxed{P_s(k;z)=T(z)^k B_s(z).}\tag{2.4}
\]

Declare (2.4) at **all** `k>=0` to define an auxiliary transition law `Q_s`. Because all `alpha_{s,i}` lie in `[0,1)`, this auxiliary law is a genuine probability law, not merely a signed kernel.

Lift the environment state into the chain. The true annealed kernel is

\[
\mathsf K((r,k),(s,j))=K(r,s)P_s(k,j),
\tag{2.5}
\]

and the auxiliary kernel is

\[
\mathsf Q((r,k),(s,j))
=K(r,s)[z^j]\bigl(T(z)^kB_s(z)\bigr).
\tag{2.6}
\]

The same finite-depth recursion used in the i.i.d. theorem yields:

### Lemma 2.1 — finite defect survives Markov dependence

Let

\[
\mathcal B=\{(s,k):s\in\mathcal S,\ 1\le k<M\}.
\tag{2.7}
\]

Then `R=Q-K` has nonzero rows only in the finite set `B`. In the row `(s,k)`, the population-coordinate discrepancy is supported only at `0<=j<=M-k`.

#### Proof

For a fixed stack state `s`, the one-cookie recursion is purely local: it compares the true number of successes before the `k`-th failure to the algebraic tail law and does not use independence across spatial sites. It gives equality for `k>=M` and a polynomial discrepancy of degree at most `M-k` for `k<M`. Multiplication by the environment transition probability `K(r,s)` only attaches a finite state label. QED.

Thus the remaining difficulty is to understand the low-state Green kernel of `Q` under Markov dependence.

---

## 3. B1 — change category: from scalar hypergeometric products to a matrix transfer cocycle

For a row vector of terminal-state pgfs define

\[
f_n^{(r,k)}(z)_s
=
\sum_{j\ge0}
\mathsf Q^n((r,k),(s,j))z^j.
\]

Let

\[
D_B(z)=\operatorname{diag}(B_1(z),\ldots,B_d(z)).
\]

### Theorem 3.1 — exact finite-dimensional transfer product

For every `n>=1`,

\[
\boxed{
 f_n^{(r,k)}(z)
 =T^n(z)^k e_r^T
 K D_B(T^{n-1}(z))
 K D_B(T^{n-2}(z))\cdots
 K D_B(z).
}
\tag{3.1}
\]

#### Proof

For `n=1`, conditional on `S_1=s`, the auxiliary offspring pgf is `T(z)^kB_s(z)`, hence

\[
f_1(z)=T(z)^k e_r^T K D_B(z).
\]

If `f_n` is known, one more step gives

\[
f_{n+1}(z)=f_n(T(z))K D_B(z),
\]

because, conditional on current population `J` and next stack state `s`, the next pgf is `T(z)^J B_s(z)`. Substitution of the induction hypothesis gives (3.1). QED.

Now conjugate `T` by

\[
u=\frac1{1-z},
\qquad
T^m(z)=1-\frac1{u+m}.
\tag{3.2}
\]

Define

\[
b_s(v)=B_s\!\left(1-\frac1v\right)
=
\prod_{i=1}^M\left(1-\frac{\alpha_{s,i}}v\right),
\qquad
D(v)=\operatorname{diag}(b_s(v)).
\tag{3.3}
\]

Then the nontrivial transfer matrix in (3.1) is

\[
\boxed{
A_n(u)=K D(u+n-1)K D(u+n-2)\cdots K D(u).
}
\tag{3.4}
\]

The periodic theorem diagonalized this product residue class by residue class. In the Markov setting the matrices do not commute. Equation (3.4) is therefore the correct new object.

---

## 4. Reverse the product and expose a weighted Markov additive functional

Let `K^*` be the stationary time reversal,

\[
K^*(a,b)=\frac{\pi_bK(b,a)}{\pi_a}.
\tag{4.1}
\]

For a path `s_0=r,s_1,...,s_n=t`, stationarity gives

\[
\prod_{m=1}^nK(s_{m-1},s_m)
=
\frac{\pi_t}{\pi_r}
\prod_{m=1}^nK^*(s_m,s_{m-1}).
\tag{4.2}
\]

Therefore, if `(R_j)` has transition `K^*` and starts at `R_0=t`,

\[
\boxed{
[A_n(u)]_{r,t}
=
\frac{\pi_t}{\pi_r}
\mathbb E_t^*\!\left[
\mathbf1_{\{R_n=r\}}
\prod_{j=0}^{n-1} b_{R_j}(u+j)
\right].
}
\tag{4.3}
\]

This identity is exact. The matrix-cocycle problem has become a weighted additive-functional problem for a finite Markov chain.

---

## 5. B12 — conserved mean drift plus a Poisson coboundary gives the exact power `n^{-bar(delta)}`

Uniformly for `s` and for `v>=1`,

\[
\log b_s(v)
=-\frac{\delta_s}{v}+r_s(v),
\qquad
|r_s(v)|\le \frac{C}{v^2}.
\tag{5.1}
\]

This follows by expanding the finite product in (3.3), using ellipticity to keep every factor uniformly positive at `v>=1`.

Write

\[
f(s)=\delta_s-\bar\delta.
\]

Since `pi f=0` and `K^*` is a finite irreducible aperiodic chain, the Poisson equation

\[
\boxed{(I-K^*)g=f,\qquad \pi g=0}
\tag{5.2}
\]

has a unique mean-zero solution.

Let

\[
a_j=(u+j)^{-1}
\]

and define the martingale difference

\[
D_{j+1}=g(R_{j+1})-(K^*g)(R_j).
\tag{5.3}
\]

Then

\[
f(R_j)=g(R_j)-g(R_{j+1})+D_{j+1}.
\tag{5.4}
\]

Hence

\[
\begin{aligned}
\sum_{j=0}^{n-1}a_j f(R_j)
={}&a_0g(R_0)-a_{n-1}g(R_n)\\
&+\sum_{j=1}^{n-1}(a_j-a_{j-1})g(R_j)
+\sum_{j=0}^{n-1}a_jD_{j+1}.
\end{aligned}
\tag{5.5}
\]

The first three terms converge absolutely because `g` is bounded and

\[
\sum_{j\ge1}|a_j-a_{j-1}|<\infty.
\]

The martingale term converges almost surely and in `L^2`, because `D_j` is bounded and

\[
\sum_{j\ge0}a_j^2<\infty.
\]

More is true. Hoeffding's lemma applied conditionally gives, for each fixed real `theta`,

\[
\sup_{n,t}
\mathbb E_t^*\exp\!\left(
\theta\sum_{j=0}^{n-1}a_jD_{j+1}
\right)<\infty.
\tag{5.6}
\]

Thus the centered weighted drift sum in (5.5) converges with uniformly bounded exponential moments, uniformly over the finitely many initial states.

Now put

\[
W_n(u)=\prod_{j=0}^{n-1}b_{R_j}(u+j).
\]

Using (5.1),

\[
\log W_n(u)
=-\bar\delta\sum_{j=0}^{n-1}\frac1{u+j}
-\sum_{j=0}^{n-1}a_jf(R_j)
+\sum_{j=0}^{n-1}r_{R_j}(u+j).
\tag{5.7}
\]

The last series converges absolutely, and

\[
\sum_{j=0}^{n-1}\frac1{u+j}
=\log n+c(u)+o(1).
\tag{5.8}
\]

Equations (5.5)--(5.8) give the following.

### Theorem 5.1 — pathwise Markov transfer asymptotic

For every initial state `t` and every fixed `u>=1`, there is a finite strictly positive random variable `L_t(u)` such that

\[
\boxed{
 n^{\bar\delta}W_n(u)\longrightarrow L_t(u)
}
\tag{5.9}
\]

almost surely and in `L^q` for some `q>1` (indeed for every fixed finite `q` after changing the uniform exponential-moment constant).

In particular

\[
\boxed{
\mathbb E_t^*[W_n(u)]
\sim C_t(u)n^{-\bar\delta},
\qquad
0<C_t(u)<\infty.
}
\tag{5.10}
\]

#### Proof of the `L^q` assertion

After adding `bar(delta) log n`, the logarithm in (5.7) is a deterministic bounded term plus the negative of (5.5) plus an absolutely convergent uniformly bounded remainder. The only genuinely random unbounded partial sum is the martingale in (5.5), whose exponential moments are uniformly bounded by (5.6). Therefore `n^{bar(delta)}W_n(u)` has a uniform `L^q` bound for every fixed finite `q`, and the almost-sure limit is uniformly integrable. Positivity follows because every factor `b_s(v)` is strictly positive. QED.

### Corollary 5.2 — rank-one Perron mode for the noncommutative transfer product

For every `r,t`,

\[
\boxed{
 n^{\bar\delta}[A_n(u)]_{r,t}
\longrightarrow \pi_t C_t(u).
}
\tag{5.11}
\]

Equivalently,

\[
\boxed{
 n^{\bar\delta}A_n(u)
\longrightarrow
\mathbf 1\,v(u)^T,
\qquad
v_t(u)=\pi_tC_t(u)>0.
}
\tag{5.12}
\]

#### Proof

By (4.3), it remains to prove

\[
n^{\bar\delta}
\mathbb E_t^*[\mathbf1_{\{R_n=r\}}W_n(u)]
\to \pi_r C_t(u).
\]

The normalized product converges in `L^1` to `L_t(u)`. Approximate `L_t(u)` in `L^1` by a function of the finite prefix `(R_0,...,R_N)`. For fixed `N`, finite-state mixing of `K^*` gives asymptotic independence of that prefix from `R_n`, with terminal probability `pi_r`. Then send first `n->infinity` and afterward `N->infinity`. Finally multiply by `pi_t/pi_r` in (4.3). QED.

This is the exact analogue, for a genuinely noncommutative finite-state cocycle, of the scalar `n^{-bar(delta)}` Pochhammer law in the periodic theorem.

---

## 6. Fixed low-population Green entries are summable

To extract a fixed population coefficient we need derivatives at `z=0`, hence at `u=1`.

For every integer `m>=1`, finite state and ellipticity give

\[
\sup_s
\left|\frac{d^m}{dv^m}\log b_s(v)\right|
\le \frac{C_m}{v^{m+1}},
\qquad v\ge1.
\tag{6.1}
\]

Therefore

\[
\sup_n
\left|\partial_u^m\log W_n(u)\right|<\infty
\]

for each fixed `m`, and Faà di Bruno's formula yields the pathwise bound

\[
\boxed{|\partial_u^mW_n(u)|\le C_mW_n(u).}
\tag{6.2}
\]

The same estimate remains true after inserting the terminal-state indicator in (4.3). Consequently every fixed `u`-derivative of every entry of `A_n(u)` is `O(n^{-bar(delta)})`.

Because `u=(1-z)^{-1}`, each fixed `z`-derivative at `z=0` is a finite linear combination of fixed `u`-derivatives at `u=1`. The prefactor

\[
T^n(z)^k=\left(1-\frac1{u+n}\right)^k
\]

has uniformly bounded fixed derivatives and its positive-order derivatives actually gain powers of `n^{-1}`. Thus:

### Theorem 6.1 — low-state potential bound

For every fixed start `(r,k)` and fixed target `(t,j)`,

\[
\boxed{
\mathsf Q^n((r,k),(t,j))=O_{r,k,t,j}(n^{-\bar\delta}).
}
\tag{6.3}
\]

Hence, when `bar(delta)>1`,

\[
\boxed{
G(x,y):=\sum_{n\ge0}\mathsf Q^n(x,y)<\infty
}
\tag{6.4}
\]

for every fixed finite-population target `y`.

This proves the exact potential-kernel statement that the preceding periodic report identified as the missing ingredient for spatial Markov dependence.

---

## 7. B28 — typical environments: dependence changes the prefactor, not the exponent

The argument above gives more than an annealed estimate. Under the stationary reversed environment process,

\[
\boxed{
 n^{\bar\delta}
\prod_{j=0}^{n-1}
B_{R_j}\!\left(1-\frac1{u+j}\right)
\longrightarrow L(u,R)\in(0,\infty)
}
\tag{7.1}
\]

for almost every spatial Markov environment trajectory.

Thus the critical exponent `bar(delta)` is **quenched along a typical environment path** for this transfer observable. Markov dependence survives in the random multiplicative prefactor `L`, but it does not renormalize the power law.

This is the useful content of B28 here. Instead of trying to control every adversarial environment sequence, we identify the full-measure class generated by the stationary Markov law and prove the exponent pathwise there.

The periodic theorem appears as the zero-variance special case in which the centered coboundary/martingale term in (5.5) collapses to a deterministic periodic correction.

---

## 8. Exact finite escape-resolvent formula; no unproved uniqueness lemma remains

The preceding periodic artifact stopped one step short of a complete subclass theorem because it invoked a standard survival-solution uniqueness statement. For the finite-state Markov class, that input can be eliminated entirely by stopping on the finite defect set.

Let

\[
\mathcal Z=\{(s,0):s\in\mathcal S\},
\qquad
\mathcal A=\mathcal B\cup\mathcal Z.
\tag{8.1}
\]

Since every target in `A` has finite population, (6.4) implies that the finite Green block

\[
G_{AA}=(G(a,a'))_{a,a'\in A}
\]

is finite entrywise. Standard first-return decomposition on a finite transient set gives

\[
G_{AA}=(I-F_A)^{-1},
\tag{8.2}
\]

so `G_AA` is invertible.

For `x notin A`, define the auxiliary first-entrance row vector

\[
H_A(x,\cdot)=P_x^{\mathsf Q}(X_{\tau_A}=\cdot,\tau_A<\infty).
\]

First-entrance decomposition gives

\[
\boxed{H_A(x,\cdot)=G_{xA}G_{AA}^{-1}.}
\tag{8.3}
\]

Define, for every positive-population state `x`,

\[
H(x,b)=
\begin{cases}
1,&x=b\in B,\\
0,&x\in A\setminus B,\\
[H_A(x,\cdot)]_b,&x\notin A,
\end{cases}
\tag{8.4}
\]

and

\[
r(x)=
\begin{cases}
0,&x\in A,\\
1-\sum_{a\in A}[H_A(x,\cdot)]_a,&x\notin A.
\end{cases}
\tag{8.5}
\]

Thus `r(x)` is the auxiliary probability of avoiding the whole finite set `A` forever, while `H(x,b)` is the probability of first entering `A` through boundary state `b`.

Let

\[
s(x)=P_x^{\mathsf K}(U_n>0\text{ for all }n\ge0)
\tag{8.6}
\]

be true forward-process survival.

### Lemma 8.1 — first-defect decomposition

For every `x` with positive population,

\[
\boxed{
s(x)=r(x)+\sum_{b\in B}H(x,b)s(b).}
\tag{8.7}
\]

#### Proof

Before the first visit to `A=B union Z`, the true and auxiliary kernels coincide because their discrepancy is supported on `B`. If the common path first enters `Z`, survival fails. If it first enters `B` at `b`, the strong Markov property gives future survival probability `s(b)`. If it never enters `A`, then it never enters `Z` and never touches a discrepancy row, so the true and auxiliary paths coincide forever and survival occurs. These three disjoint possibilities give (8.7). QED.

Now let `K_B` denote the true one-step kernel out of the finite set `B`. Define the finite vector and matrix

\[
a_b=\sum_y\mathsf K(b,y)r(y),
\tag{8.8}
\]

\[
M_{bc}=\sum_y\mathsf K(b,y)H(y,c).
\tag{8.9}
\]

Applying (8.7) after the first true step from `b` gives

\[
\boxed{(I-M)s_B=a.}
\tag{8.10}
\]

Crucially, invertibility is elementary here. Because `B` is finite and every cookie is elliptic, there is

\[
\varepsilon_0=
\min_{b\in B}
P_b^{\mathsf K}(U_1=0)>0.
\tag{8.11}
\]

The row sum of `M` is at most the probability that the first true step does **not** hit `Z`, hence

\[
\sum_c M_{bc}\le1-\varepsilon_0.
\tag{8.12}
\]

Therefore

\[
\rho(M)\le\|M\|_\infty\le1-\varepsilon_0<1,
\]

and

\[
\boxed{
s_B=(I-M)^{-1}a=\sum_{m\ge0}M^m a.}
\tag{8.13}
\]

No asymptotic boundary condition or uniqueness theorem is being assumed.

Finally (8.7) computes `s(s,1)` for every environment state `s`. If the origin stack state is `r~pi`, the first step to the right has probability `p_{r,1}`, and conditional on that step the stack at site `1` has state `s` with probability `K(r,s)`. Hence the never-return probability is

\[
\boxed{
 p_{\rm esc}
 =
\sum_{r\in S}\pi_r p_{r,1}
\sum_{s\in S}K(r,s)
\left[
 r((s,1))+\sum_{b\in B}H((s,1),b)s_B(b)
\right],
}
\tag{8.14}
\]

where `s_B` is the explicit finite solution (8.13), and every `H` and `r` entry is obtained from the convergent transfer-Green series (3.1), (6.4), and the finite inverse (8.3).

### Theorem 8.2 — complete finite-state spatial-Markov positive formula

Under the hypotheses of Section 2 and `bar(delta)>1`, equation (8.14) is an exact convergent finite-dimensional computation of the source escape probability for the entire finite-state spatial-Markov, bounded, positive elliptic subclass.

Every infinite object entering (8.14) is a Green series whose `n`-th term is given explicitly by the finite matrix product (3.1) and decays as `O(n^{-bar(delta)})`; hence the computation has a proved convergence rate. No stationary-law truncation or unproved infinite-dimensional solve remains.

---

## 9. What this does and does not settle

This theorem strictly extends the spatial-periodic subclass: a deterministic cycle is a special finite-state Markov environment after phase lifting, while here `K` may be any irreducible aperiodic finite transition matrix.

It also supplies the precise object requested by the preceding report: the periodic scalar Pochhammer product is replaced by a noncommutative transfer cocycle, and the conserved stationary mean drift is separated from dependence by the Poisson equation. The `n^{-bar(delta)}` mode survives with a rank-one Perron limit.

It **does not** close Kosygina--Zerner Problem 3.12 in full. The source's positive stationary-ergodic branch permits much more general dependence and unbounded cookie stacks. In those settings:

1. there need not be a finite Markov state carrying the spatial dependence;
2. the Poisson equation need not have a bounded solution;
3. a uniform finite defect set may disappear when stack heights are unbounded.

The present theorem therefore remains **PARTIAL** relative to the full outside source.

The frozen metric also stays

\[
\boxed{M_{\rm closed}=\infty\quad\text{(all finite i.i.d. depths)},}
\]

so this run records **NO MOVEMENT** in that metric despite the genuine dependent-environment extension.

---

## 10. Exact failures and the next mathematical boundary

The three methods have now isolated three distinct levels:

- **B1:** finite-state Markov dependence is not an infinite-dimensional obstacle; it is a finite matrix cocycle.
- **B12:** the noncommutative cocycle has an exact `n^{-bar(delta)}` Perron mode because the centered drift is a Poisson coboundary plus a square-summable martingale.
- **B28:** the same exponent holds pathwise for typical stationary Markov environment trajectories; dependence changes the prefactor, not the power.

The remaining full-source obstruction is now sharper. The next extension should not repeat matrix-transfer algebra. It should replace the bounded finite-state Poisson solution by an ergodic-projective criterion for a general stationary sequence. A plausible sufficient condition is a source-valid summable-mixing hypothesis under which

\[
\sum_{j\ge0}\frac{\delta(S_j)-\bar\delta}{u+j}
\]

converges with enough exponential integrability to reproduce Sections 5--6. The deeper obstacle is then unbounded cookie depth, which destroys the finite defect `B` even if the weighted-cocycle asymptotic survives.

No full-source PROVED label, closure audit request, or novelty claim is made here.