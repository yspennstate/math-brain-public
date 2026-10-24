Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime model/effort telemetry or binding selector is exposed.

# P0429 — exponential service: exact square-root threshold for the busy/idle projection

Target: Mor Harchol-Balter, *Open problems in queueing theory inspired by datacenter computing* (Queueing Systems 97, 2021), Section 5 limited fork–join threshold, with the model of Wang–Harchol-Balter–Jiang–Scheller-Wolf–Srikant, *Delay Asymptotics and Bounds for Multi-Task Parallel Jobs* (Queueing Systems 91, 2019).

This artifact is **PARTIAL relative to the source**. It proves an exact threshold for the busy/idle projection in the exponential-service case, not yet for the full stationary workload vector under every finite-second-moment service law.

## Setup

There are `n` FCFS servers. Parent jobs arrive at rate

\[
\Lambda_n=\frac{n\lambda}{k},
\]

and each parent selects a uniform `k`-subset of the servers, sending one task to every selected server. In this artifact task service times are exponential with rate `\mu`, and

\[
\rho:=\frac{\lambda}{\mu}\in(0,1).
\]

Let `N_i` be the stationary queue length at server `i` and

\[
B_i:=\mathbf 1_{\{N_i>0\}}.
\]

Each marginal `N_i` is exactly geometric,

\[
P(N_i=m)=(1-\rho)\rho^m,
\qquad m\ge0,
\]

so `P(B_i=1)=\rho`.

For a fixed tagged set `K` of cardinality `k`, write

\[
P^{\rm busy}_{n,k}:=\mathcal L((B_i)_{i\in K}),
\qquad
Q_k:=\operatorname{Ber}(\rho)^{\otimes k}.
\]

The theorem proved below is

\[
\boxed{
 d_{\rm TV}(P^{\rm busy}_{n,k},Q_k)\to0
 \quad\Longleftrightarrow\quad
 \frac{k^2}{n}\to0.
}
\]

The implication from the full workload law to the busy projection is immediate by data processing. Therefore, in exponential service, full stationary workload independence can hold only if `k=o(sqrt(n))`.

---

# 1. B12 — a conservation identity that fixes an exact cross covariance

Define the total number of tasks and total number of busy servers by

\[
M:=\sum_{i=1}^n N_i,
\qquad
B:=\sum_{i=1}^n B_i.
\]

The queue-length chain is positive recurrent for `\rho<1`; all moments used below are finite because `n` is finite and every marginal is geometric.

A parent arrival raises `M` by exactly `k`, while a service completion lowers `M` by one. Service completions occur at total rate `\mu B`. Stationarity applied to `M` gives

\[
0=\frac{n\lambda}{k}\,k-\mu E B,
\]

hence

\[
\boxed{E B=n\rho.}
\]

Apply the stationary generator to `M^2`. An arrival changes `M^2` by

\[
(M+k)^2-M^2=2kM+k^2,
\]

and a departure changes it by

\[
(M-1)^2-M^2=-2M+1.
\]

Therefore

\[
0
=2n\lambda E M+n\lambda k
-2\mu E[MB]+\mu E B.
\]

Using `E B=n\lambda/\mu`, this becomes

\[
2\mu E[MB]
=2n\lambda E M+n\lambda(k+1).
\]

Since `E M\,E B=E M\,n\lambda/\mu`, the first term cancels when we subtract the product of the means, giving the exact identity

\[
\boxed{
\operatorname{Cov}(M,B)
=\frac{n\rho(k+1)}2.
}
\]

By exchangeability, for `i\ne j` there is a common value

\[
c_{NB}:=\operatorname{Cov}(N_i,B_j).
\]

Also

\[
\operatorname{Cov}(N_i,B_i)
=E N_i-E N_i\,E B_i
=\frac{\rho}{1-\rho}(1-\rho)
=\rho.
\]

Thus

\[
\operatorname{Cov}(M,B)
=n\rho+n(n-1)c_{NB}.
\]

Combining with the exact conservation identity yields

\[
\boxed{
\operatorname{Cov}(N_i,B_j)
=\frac{\rho(k-1)}{2(n-1)},
\qquad i\ne j.
}
\]

This identity is exact for every finite `n,k` in the exponential model.

## Association and an exact upper bound for busy-busy covariance

The stationary queue-length vector is associated. A direct graphical proof is available here: use independent Poisson clocks for every parent-arrival subset and independent potential-service clocks at every server. Starting from the zero state, each queue length at fixed time is coordinatewise nondecreasing in all arrival primitives and coordinatewise nonincreasing in the service primitives. Reverse the order of each independent service primitive; then all queue-length coordinates are coordinatewise nondecreasing functions of an independent family. Hence the finite-time vector is associated. The positive recurrent stationary law is a weak limit of these laws, and association is closed under weak convergence.

Consequently, for `i\ne j`,

\[
0\le \operatorname{Cov}(B_i,B_j).
\]

Moreover `N_i-B_i=(N_i-1)_+` is nondecreasing in `N_i`, so association gives

\[
\operatorname{Cov}(N_i-B_i,B_j)\ge0.
\]

Therefore

\[
\boxed{
0\le c_{BB}:=\operatorname{Cov}(B_i,B_j)
\le\operatorname{Cov}(N_i,B_j)
=\frac{\rho(k-1)}{2(n-1)}.
}
\]

It follows that

\[
\boxed{
\operatorname{Var}(B)
\le
n\rho(1-\rho)+\frac{n\rho(k-1)}2.
}
\]

The previous R7-01 linear-response calculation gives, for `k=o(n)`,

\[
c_{BB}
=\rho^2 C_{\rho,\mu}\,\lambda\frac{k-1}{n-1}
+O\!\left(\frac{k^2}{n^2}\right),
\]

where

\[
C_{\rho,\mu}
=\int_0^\infty
\langle Z,P_tZ\rangle_\pi^2\,dt>0,
\qquad
Z=\frac{B_1}{\rho}-1.
\]

The exact covariance upper bound improves the previous spectral upper bound on this constant. Dividing by `(k-1)/(n-1)` and letting this ratio tend to zero gives

\[
\boxed{
\frac{(1-\rho)^2}{2\rho^2\mu}
\le C_{\rho,\mu}
\le\frac1{2\rho^2\mu}.
}
\]

Equivalently, if

\[
a_{\rho,\mu}:=\rho^2 C_{\rho,\mu}\lambda,
\]

then

\[
\boxed{
\frac{\rho(1-\rho)^2}{2}
\le a_{\rho,\mu}
\le\frac\rho2.
}
\]

Hence whenever `k\to\infty` and `k=o(n)`,

\[
\boxed{
\frac{\operatorname{Var}(B)}{nk}
\longrightarrow a_{\rho,\mu}>0.
}
\]

So the full-system busy fraction fluctuates on the scale `sqrt(k/n)`, not the independent-server scale `n^{-1/2}`.

---

# 2. B18 — finite exchangeability turns the problem into hypergeometric sampling from a random environment

Because the stationary `n`-server law is invariant under every permutation of the servers, conditional on `B=m` the set of busy servers is uniform among the `m`-subsets of `[n]`.

Thus, conditional on

\[
P_n:=\frac Bn,
\]

the tagged busy vector is a sample of `k` entries **without replacement** from a population having busy fraction `P_n`.

Let `\widetilde P_{n,k}` be the mixture obtained by instead taking `k` iid `\operatorname{Ber}(P_n)` variables conditional on `P_n`.

Sampling indices with replacement and without replacement can be coupled until the first repeated index. Therefore

\[
\boxed{
 d_{\rm TV}(P^{\rm busy}_{n,k},\widetilde P_{n,k})
\le \frac{k(k-1)}{2n}.
}
\]

Now compare the mixture `\widetilde P_{n,k}` with `Q_k=\operatorname{Ber}(\rho)^{\otimes k}`. For Bernoulli laws, write the Hellinger affinity

\[
A(p,\rho)
:=\sqrt{p\rho}+\sqrt{(1-p)(1-\rho)}.
\]

With the convention `H^2=1-A`, product affinity gives

\[
H^2(\operatorname{Ber}(p)^{\otimes k},Q_k)
=1-A(p,\rho)^k
\le k(1-A(p,\rho)).
\]

Also

\[
1-A(p,\rho)
=\frac12\left[(\sqrt p-\sqrt\rho)^2
+(\sqrt{1-p}-\sqrt{1-\rho})^2\right]
\le\frac{(p-\rho)^2}{2\rho(1-\rho)}.
\]

Squared Hellinger distance is convex in its first argument, hence

\[
H^2(\widetilde P_{n,k},Q_k)
\le\frac{k\operatorname{Var}(P_n)}{2\rho(1-\rho)}.
\]

Since `d_TV\le\sqrt2 H`, the covariance bound from Section 1 gives

\[
\begin{aligned}
d_{\rm TV}(\widetilde P_{n,k},Q_k)
&\le
\sqrt{\frac{k\operatorname{Var}(P_n)}{\rho(1-\rho)}}\\
&\le
\sqrt{
\frac{k\left[(1-\rho)+(k-1)/2\right]}
{n(1-\rho)}
}.
\end{aligned}
\]

Combining with the without-replacement coupling,

\[
\boxed{
 d_{\rm TV}(P^{\rm busy}_{n,k},Q_k)
\le
\frac{k(k-1)}{2n}
+
\sqrt{
\frac{k\left[(1-\rho)+(k-1)/2\right]}
{n(1-\rho)}
}.
}
\]

Therefore

\[
\boxed{
\frac{k^2}{n}\to0
\quad\Longrightarrow\quad
 d_{\rm TV}(P^{\rm busy}_{n,k},Q_k)\to0.
}
\]

This is already a strict improvement over the cubic source-wide workload scale for this observable: the busy/idle projection remains asymptotically independent throughout `k=o(sqrt(n))`.

---

# 3. B7 — the square-root boundary is also necessary for the busy projection

The only remaining issue is whether the preceding upper bound is merely an artefact. It is not.

## 3.1 Fixed-dimensional perturbation and low-order moment bounds

Take any fixed `r` selected servers. Their queue-length process is autonomous. Let `T_i` denote the operator that adds one task to coordinate `i`. If `A` is a nonempty subset of the `r` selected coordinates, the rate at which a parent job hits every coordinate of `A` is

\[
\gamma_{|A|}
=\lambda\frac{(k-1)_{|A|-1}}{(n-1)_{|A|-1}}.
\]

Möbius inversion of exact-hit rates gives the selected-coordinate arrival generator in the exact form

\[
L_r
=L_0+
\sum_{\substack{A\subseteq[r]\\ |A|\ge2}}
\gamma_{|A|}
\prod_{i\in A}(T_i-I),
\]

where `L_0` is the generator of `r` independent M/M/1 queues.

Put

\[
\varepsilon:=\frac{k-1}{n-1}.
\]

For fixed `r`, `\gamma_b=O_r(\varepsilon^{b-1})`. On `L^2(\pi^{\otimes r})` every shift is bounded, while the mean-zero inverse of `-L_0` has norm at most the reciprocal of the M/M/1 spectral gap

\[
(\sqrt\mu-\sqrt\lambda)^2.
\]

Therefore, for sufficiently small `\varepsilon`, the stationary density relative to `\pi^{\otimes r}` has a convergent Neumann expansion in the hyperedge perturbations above.

Crucially, the product resolvent does not enlarge coordinate support. A term can have nonzero inner product with

\[
X_A:=\prod_{i\in A}(B_i-\rho)
\]

only if the union of its perturbation hyperedges covers every coordinate of `A`, because any uncovered coordinate contributes `E_\pi(B_i-\rho)=0`.

Hence, uniformly for distinct fixed indices as `\varepsilon\to0`,

\[
E[(B_i-\rho)(B_j-\rho)] = O(\varepsilon),
\]

\[
E[(B_i-\rho)(B_j-\rho)(B_\ell-\rho)] = O(\varepsilon^2),
\]

and

\[
E[(B_i-\rho)(B_j-\rho)(B_\ell-\rho)(B_m-\rho)] = O(\varepsilon^2).
\]

For four distinct coordinates the order `\varepsilon^2` is sharp as an order bound because two disjoint pair interactions already cover all four coordinates.

## 3.2 A uniform fourth-moment bound in the critical window

For `m` selected coordinates set

\[
S_m:=\sum_{i=1}^m(B_i-\rho).
\]

Assume

\[
m\varepsilon\le T
\]

for a fixed finite `T`, with `\varepsilon\to0`. Expanding `E S_m^4` by the number of distinct indices and using

\[
(B_i-\rho)^2
=\rho(1-\rho)+(1-2\rho)(B_i-\rho),
\]

together with the low-order bounds above gives

\[
\begin{aligned}
E S_m^4
&=O(m)
+O(m^2)
+O(m^3\varepsilon)
+O(m^4\varepsilon^2)\\
&=O_T(m^2).
\end{aligned}
\]

Thus

\[
\boxed{
\sup E\left(\frac{S_m}{\sqrt m}\right)^4<\infty
\qquad\text{whenever }m\varepsilon\le T.
}
\]

## 3.3 TV separation when the square-root condition fails

From the previous R7-01 two-queue linear response,

\[
c_{BB}
=a_{\rho,\mu}\varepsilon+O(\varepsilon^2),
\qquad
a_{\rho,\mu}>0.
\]

Hence

\[
\frac{\operatorname{Var}(S_m)}m
=\rho(1-\rho)+(m-1)c_{BB}.
\]

Suppose first that `k=o(n)` but `k^2/n` does not tend to zero. Along a subsequence there is `\delta>0` such that `k^2/n\ge\delta`. Choose a fixed `0<c<\delta` and

\[
m=\left\lfloor c\frac nk\right\rfloor.
\]

Then eventually `m\le k`, `m\to\infty`, and

\[
m\varepsilon\to c.
\]

Therefore

\[
\frac{\operatorname{Var}_{P}(S_m)}m
\to \rho(1-\rho)+a_{\rho,\mu}c,
\]

whereas under the independent product law

\[
\frac{\operatorname{Var}_{Q}(S_m)}m
=\rho(1-\rho).
\]

The fourth-moment bound above holds uniformly for both laws. Let

\[
Y_m:=\frac{S_m}{\sqrt m},
\qquad
f_R(y):=\min(y^2,R).
\]

Uniform fourth moments imply uniform integrability of `Y_m^2`: for fixed large `R`,

\[
\sup E[Y_m^2\mathbf 1_{\{Y_m^2>R\}}]
\le \frac{\sup E Y_m^4}{R}.
\]

Choose `R` so large that this tail contribution is smaller than `a_{\rho,\mu}c/8` under both laws. Then for all sufficiently large indices in the subsequence,

\[
|E_P f_R(Y_m)-E_Q f_R(Y_m)|
\ge \frac{a_{\rho,\mu}c}{2}.
\]

Since `0\le f_R\le R`,

\[
d_{\rm TV}(P_m,Q_m)
\ge \frac{a_{\rho,\mu}c}{4R}>0.
\]

The `m`-coordinate law is a marginal of the original `k`-coordinate tagged law, so data processing gives the same positive lower bound for the full tagged busy vector along that subsequence.

If `k/n` does not tend to zero, then the two-coordinate common-parent rate

\[
\gamma=\lambda\frac{k-1}{n-1}
\]

stays bounded away from zero along a subsequence. The two-coordinate stationary busy covariance is then strictly positive, while it is zero under `Q_2`; the two-coordinate marginal alone prevents total-variation convergence.

Combining both cases proves the converse:

\[
\boxed{
 d_{\rm TV}(P^{\rm busy}_{n,k},Q_k)\to0
 \quad\Longrightarrow\quad
 \frac{k^2}{n}\to0.
}
\]

Together with Section 2,

\[
\boxed{
 d_{\rm TV}(P^{\rm busy}_{n,k},\operatorname{Ber}(\rho)^{\otimes k})\to0
 \iff
 k=o(\sqrt n).
}
\]

---

# 4. Orthogonal diagnostic: chi-square already breaks at the square-root window

The preceding TV proof used fourth moments. There is also a short `L^2` diagnostic.

Under `Q_k`, define

\[
Z_i:=\frac{B_i-\rho}{\sqrt{\rho(1-\rho)}}.
\]

The products `Z_A=\prod_{i\in A}Z_i` form an orthonormal Walsh basis. If `h=dP^{\rm busy}_{n,k}/dQ_k`, Parseval yields

\[
\chi^2(P^{\rm busy}_{n,k}\|Q_k)
=\sum_{\varnothing\ne A\subseteq[k]}
(E_P Z_A)^2.
\]

Keeping only the pair coefficients,

\[
\boxed{
\chi^2(P^{\rm busy}_{n,k}\|Q_k)
\ge
\binom{k}{2}
\left[
\frac{c_{BB}}{\rho(1-\rho)}
\right]^2.
}
\]

If `k^2/n\to\tau\in(0,\infty)`, then `c_{BB}\sim a_{\rho,\mu}k/n`, so

\[
\liminf\chi^2(P^{\rm busy}_{n,k}\|Q_k)
\ge
\frac{a_{\rho,\mu}^2\tau^2}
{2\rho^2(1-\rho)^2}
>0.
\]

Thus the square-root boundary is visible already at the pair-Walsh level.

---

# 5. Consequence for P0429 and exact remaining gap

For exponential service we now know:

1. the full workload vector is independent only if its busy projection is independent;
2. the busy projection has the exact threshold `k=o(sqrt(n))`;
3. therefore full exponential-service workload independence **requires** `k=o(sqrt(n))`;
4. R7-01 already proved full workload independence for every finite-second-moment service law under `k^3/n->0`, hence in particular for exponential service under `k=o(n^(1/3))`.

The remaining exponential-service workload gap is therefore

\[
\boxed{
 n^{1/3}\ \text{(proved full-workload sufficiency)}
 \quad\text{versus}\quad
 n^{1/2}\ \text{(proved necessary scale from the busy projection)}.
}
\]

The source-wide frozen metric `M_alpha` remains `1/3` because deterministic/atomic service already forces the universal cubic threshold. This artifact does not redefine that metric.

A natural next question is whether the full exponential-service queue-length/workload law itself admits an `L^2` perturbation bound of order `k^2/n`; the exact product-law residual from the preceding run strongly suggests that route. That is not proved here.

## Dated source/prior-art check — 2026-09-19

Fresh bounded searches recovered the Wang et al. 2018/2019 limited fork–join paper and Harchol-Balter's 2021 open-problems article, plus later adjacent fork–join/datacenter papers, but no later theorem matching the exact growing-`k` stationary-independence threshold. Wang et al. explicitly prove steady-state workload association and the `k=o(n^(1/4))` full-workload TV theorem; their simulations examine `n^(1/3)`, `n^(1/2)`, `n^(2/3)` and `n^(9/10)` regimes. Search failure is negative evidence only, not a novelty certificate.

No claim of source closure is made by this artifact.