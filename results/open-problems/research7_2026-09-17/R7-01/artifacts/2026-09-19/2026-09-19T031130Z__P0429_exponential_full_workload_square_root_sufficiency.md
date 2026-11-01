Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# P0429 — full-workload square-root sufficiency for exponential service

Date: 2026-09-19 UTC  
Slot: `R7-01`  
Canonical target: `P0429`  
Native ID: `6aabe777361481919c9e614646464772`  
Source: Mor Harchol-Balter, *Open problems in queueing theory inspired by datacenter computing*, Queueing Systems 97 (2021), Section 5, with the limited fork–join model of Wang–Harchol-Balter–Jiang–Scheller-Wolf–Srikant, *Delay Asymptotics and Bounds for Multi-Task Parallel Jobs*, Queueing Systems 91 (2019), arXiv:1710.00296.

## Scope and status

The cumulative R7-01 work already proves, under the full source assumption of an arbitrary iid service law with finite second moment,

\[
 k^3/n\to0
 \quad\Longrightarrow\quad
 d_{\rm TV}(P_{n,k},\pi_\lambda^{\otimes k})\to0,
\]

and an allowed atomic service law shows that the universal power exponent cannot exceed `1/3`. Thus the frozen source-wide metric remains

\[
\boxed{M_\alpha=1/3.}
\]

This artifact does **not** redefine or move that metric. It resolves the simplest case isolated by the preceding STUCK1 report: **exponential service, full stationary queue-length/workload vector, and `k^2/n -> 0`**. It proves a genuine source-valid special-case theorem, hence remains `PARTIAL` relative to the full finite-second-moment source question.

The proof executes the selected recovery action with methods B3/B11/B21: prove a stronger `L^2` likelihood-ratio estimate, dualize the stationary equation into a product-chain Dirichlet form, and use the shape of quantitative propagation-of-chaos estimates only as methodological guidance. The argument below is self-contained for this model and does not import a theorem whose hypotheses fail for the common-arrival jump operator.

---

## Theorem

Fix `0 < rho < 1` and exponential task service times of rate `mu`, with marginal arrival rate `lambda=rho*mu`. Let `P^N_{n,k}` be the stationary law of the queue-length vector of any `k=k(n)` tagged queues in the limited fork–join system, and let

\[
 q_k=\pi^{\otimes k},\qquad
 \pi(m)=(1-\rho)\rho^m,\quad m\in\mathbb Z_+,
\]

be the product stationary law of `k` independent M/M/1 queues. Let `P^W_{n,k}` be the corresponding stationary workload-vector law and let `Q^W_k` be the product M/M/1 workload law.

Then there is a finite constant `C_rho` depending only on `rho` (and the time-scale normalization through `lambda,mu`) such that, whenever `k^2/n` is sufficiently small,

\[
\boxed{
 d_{\rm TV}(P^N_{n,k},q_k)
 \le C_\rho\frac{k^2}{n},
}
\tag{T1}
\]

and

\[
\boxed{
 d_{\rm TV}(P^W_{n,k},Q^W_k)
 \le C_\rho\frac{k^2}{n}.
}
\tag{T2}
\]

In particular,

\[
\boxed{
 k^2/n\to0
 \quad\Longrightarrow\quad
 d_{\rm TV}(P^W_{n,k},Q^W_k)\to0.
}
\tag{T3}
\]

Thus exponential service admits full-workload stationary asymptotic independence throughout `k=o(sqrt(n))`. No converse at the square-root scale is claimed here.

A fully explicit, deliberately crude version of (T1) is obtained below.

---

# 1. Exact generator decomposition

For exponential service the tagged queue-length vector is an autonomous continuous-time Markov chain on `Z_+^k`. Put

\[
(S_if)(x)=f(x+e_i),\qquad U_i=S_i-I.
\]

Let `L_0` be the generator of `k` independent M/M/1 queues, each with arrival rate `lambda` and service rate `mu`. The true tagged generator has the exact form

\[
\boxed{
L=L_0+W,
\qquad
W=\sum_{b=2}^k \gamma_b
       \sum_{\substack{B\subseteq[k]\\|B|=b}}
       \prod_{i\in B}U_i,
}
\tag{1.1}
\]

where

\[
\boxed{
\gamma_b
=\lambda\frac{(k-1)_{b-1}}{(n-1)_{b-1}}.
}
\tag{1.2}
\]

Indeed, expand every simultaneous parent-arrival shift as
`prod_{i in A}(I+U_i)-I`. The coefficient of `prod_{i in B}U_i` is the rate at which a parent contains every queue in `B`, namely

\[
\frac{n\lambda}{k}\frac{(k)_b}{(n)_b}
=\lambda\frac{(k-1)_{b-1}}{(n-1)_{b-1}}.
\]

For `b=1` this is exactly `lambda`, so all singleton terms are already contained in `L_0`; the interaction starts at `b=2`.

The product law `q_k` is reversible for `L_0`. Write

\[
H=-L_0.
\]

All Hilbert-space norms and adjoints below are in `L^2(q_k)`.

---

# 2. One-coordinate identities

For one geometric coordinate let `S f(m)=f(m+1)` and `U=S-I`. Since

\[
\|Sf\|_{L^2(\pi)}^2
=\rho^{-1}\sum_{m\ge1}\pi(m)|f(m)|^2,
\]

we have

\[
\|S\|\le\rho^{-1/2},
\qquad
\boxed{\|U\|=\|U^*\|\le c_\rho:=1+\rho^{-1/2}.}
\tag{2.1}
\]

Moreover

\[
U^*1=z,
\qquad
z(m)=\rho^{-1}{\bf1}_{\{m>0\}}-1,
\]

so

\[
E_\pi z=0,
\qquad
\boxed{\|z\|_2^2=v_\rho:=\frac{1-\rho}{\rho}.}
\tag{2.2}
\]

If `g` is mean zero, then `U^*g` is also mean zero, because

\[
\langle1,U^*g\rangle=\langle U1,g\rangle=0.
\tag{2.3}
\]

For the one-dimensional M/M/1 generator `L_1`, reversibility gives the exact Dirichlet form

\[
\boxed{
\langle f,-L_1f\rangle_\pi
=\lambda\|Uf\|_2^2.
}
\tag{2.4}
\]

Its `L^2(pi)` spectral gap is

\[
\boxed{
g_\rho=(\sqrt\mu-\sqrt\lambda)^2>0.}
\tag{2.5}
\]

---

# 3. ANOVA decomposition of the product chain

Let `H_0` be the mean-zero subspace of `L^2(pi)`. The product Hilbert space has the orthogonal Hoeffding/ANOVA decomposition

\[
L^2(q_k)
=\bigoplus_{A\subseteq[k]}\mathcal H_A,
\]

where a function in `H_A` is mean zero in every coordinate of `A` and constant in every coordinate outside `A`.

If `|A|=r`, the product generator is the sum of the coordinate generators, hence on `H_A`

\[
\boxed{H\ge r g_\rho.}
\tag{3.1}
\]

The constant sector is `r=0`; all centered functions lie in the direct sum of the sectors `r>=1`.

The crucial structural fact is that `U_i^*` has only two actions on ANOVA support:

* if `i notin A`, then it sends the constant in coordinate `i` to `z_i`, thereby **creating** coordinate `i`, with norm exactly `sqrt(v_rho)`;
* if `i in A`, then it preserves mean-zero status in coordinate `i`, with operator norm at most `c_rho` by (2.1)–(2.3).

This turns the common-arrival adjoint into a controlled support-creation operator.

---

# 4. Dimension-uniform relative-form bound for one b-body interaction

Define

\[
T_b
:=\sum_{\substack{B\subseteq[k]\\|B|=b}}
   \prod_{i\in B}U_i^*.
\tag{4.1}
\]

We prove

\[
\boxed{
\|H^{-1/2}T_bH^{-1/2}\|_{2\to2}
\le \frac{A_\rho^b}{g_\rho}\,k^{b-1},
\qquad b\ge2,
}
\tag{4.2}
\]

for the explicit choice

\[
\boxed{
A_\rho
=2\max\{1,\ c_\rho,\ 2e\sqrt{v_\rho}\}.
}
\tag{4.3}
\]

Here `H^{-1/2}` is understood on the centered subspace.

### Proof of (4.2)

Fix an input ANOVA support `A` with `|A|=r>=1`. In a term indexed by `B`, let

\[
s=|B\setminus A|,
\qquad
m=|B\cap A|=b-s.
\]

Thus `s` coordinates are newly created and the output support has size `r+s`.

Fix an output support `C=A union J`, where `J` is an `s`-subset of `[k]\setminus A`. Summing over the choice of the `m` internal coordinates in `A`, the block `H_A -> H_C` has norm at most

\[
M_{r,s}
=\binom rm c_\rho^m v_\rho^{s/2}.
\tag{4.4}
\]

For this fixed `r,s`, each input support has `binom{k-r}{s}` possible outputs, while each output support has `binom{r+s}{s}` possible predecessors. The standard row/column-degree estimate for a block operator matrix therefore gives

\[
\|T_b:\mathcal H^{(r)}\to\mathcal H^{(r+s)}\|
\le
M_{r,s}
\sqrt{\binom{k-r}{s}\binom{r+s}{s}},
\tag{4.5}
\]

where `H^(r)=oplus_{|A|=r}H_A`.

Using (3.1) on the input and output gives

\[
\|H^{-1/2}T_bH^{-1/2}:\mathcal H^{(r)}\to\mathcal H^{(r+s)}\|
\le
\frac{M_{r,s}}{g_\rho\sqrt{r(r+s)}}
\sqrt{\binom{k-r}{s}\binom{r+s}{s}}.
\tag{4.6}
\]

If `s=0`, then `m=b` and

\[
(4.6)
\le
\frac{c_\rho^b}{b!g_\rho}r^{b-1}
\le
\frac{c_\rho^b}{b!g_\rho}k^{b-1}.
\tag{4.7}
\]

If `s>=1`, use

\[
\binom rm\le\frac{r^m}{m!},\quad
\binom{k-r}s\le\frac{(k-r)^s}{s!},\quad
\binom{r+s}s\le\frac{(r+s)^s}{s!},
\]

and `r+s <= (s+1)r`. Then (4.6) is at most

\[
\frac{c_\rho^m v_\rho^{s/2}}{m!s!g_\rho}
(s+1)^{(s-1)/2}
 r^{m+(s-2)/2}(k-r)^{s/2}.
\tag{4.8}
\]

The two powers in the last product add to

\[
m+(s-2)/2+s/2=m+s-1=b-1,
\]

and both are nonnegative for the admissible `b>=2`. Hence

\[
r^{m+(s-2)/2}(k-r)^{s/2}\le k^{b-1}.
\tag{4.9}
\]

Finally, the elementary bound `s! >= (s/e)^s` gives

\[
\frac{(s+1)^{(s-1)/2}}{s!}
\le (2e)^s,
\qquad s\ge1.
\tag{4.10}
\]

For each fixed `s`, different input ANOVA levels map to different output levels, so taking the supremum over `r` is legitimate. Summing the `s=0,...,b` pieces and using `b+1<=2^b` yields exactly (4.2) with (4.3). QED.

The loss in `A_rho` is intentionally crude. What matters is the **dimension dependence `k^(b-1)` rather than `k^b`**; the missing factor of `k` is supplied by the product-chain energy through the two `H^{-1/2}` factors.

---

# 5. Summing every interaction order

Let `K=W^*` denote the `L^2(q_k)` adjoint of the interaction. From (1.1),

\[
K=\sum_{b=2}^k\gamma_bT_b.
\tag{5.1}
\]

Assume `k<=n/2`. Then for every `b<=k`,

\[
\frac{k-j}{n-j}\le\frac{2k}{n},
\qquad 1\le j\le b-1,
\]

so

\[
\boxed{
\gamma_b\le\lambda\left(\frac{2k}{n}\right)^{b-1}.
}
\tag{5.2}
\]

Put

\[
\delta=\frac{k^2}{n}.
\]

Combining (4.2) and (5.2),

\[
\begin{aligned}
\theta_{n,k}
&:=\|H^{-1/2}KH^{-1/2}\|\\
&\le\frac{\lambda}{g_\rho}
\sum_{b=2}^k A_\rho^b(2\delta)^{b-1}.
\end{aligned}
\]

Therefore, whenever `2 A_rho delta < 1`, the finite geometric sum is bounded by

\[
\boxed{
\theta_{n,k}
\le
\frac{2\lambda A_\rho^2}{g_\rho}
\frac{\delta}{1-2A_\rho\delta}.
}
\tag{5.3}
\]

In particular,

\[
\boxed{\theta_{n,k}=O_\rho(k^2/n).}
\tag{5.4}
\]

This is the dimension-uniform relative-form estimate that the STUCK1 report identified as the missing ingredient. It treats **all** common-parent subset sizes, not just fixed pairs.

---

# 6. Exact forcing and its H^{-1/2} norm

Let

\[
D=K1.
\]

Since `U_i^*1=z_i`, the earlier exact stationarity-score identity is recovered:

\[
\boxed{
D
=\sum_{b=2}^k\gamma_b
  \sum_{|B|=b}\prod_{i\in B}z_i.
}
\tag{6.1}
\]

Different subsets give orthogonal ANOVA monomials, hence

\[
\boxed{
\|D\|_2^2
=\sum_{b=2}^k
\binom kb\gamma_b^2v_\rho^b.
}
\tag{6.2}
\]

For an explicit bound define

\[
\varepsilon=\frac{k^3}{n^2}.
\]

Using `binom{k}{b}<=k^b` and (5.2), the `b`-th term of (6.2) is at most

\[
\lambda^2 4^{b-1}v_\rho^b
\delta^2\varepsilon^{b-2}.
\]

Thus, if `4v_rho epsilon<1`,

\[
\boxed{
\|D\|_2^2
\le
\frac{4\lambda^2v_\rho^2\delta^2}
{1-4v_\rho\varepsilon}.
}
\tag{6.3}
\]

Every term of `D` lies in ANOVA level at least two, so by (3.1),

\[
\boxed{
\eta_{n,k}:=\|H^{-1/2}D\|_2
\le
\frac{\sqrt2\lambda v_\rho\delta}
{\sqrt{g_\rho}\sqrt{1-4v_\rho\varepsilon}}.
}
\tag{6.4}
\]

---

# 7. B11: solve the stationary equation by coercivity

Let `r=dP^N_{n,k}/dq_k` and formally write `r=1+h`. The relative stationary equation is

\[
(L_0+K)(1+h)=0,
\]

or equivalently

\[
\boxed{(H-K)h=D.}
\tag{7.1}
\]

We now make this rigorous without assuming in advance that the true stationary density is in `L^2`.

Work on the centered form domain of `H`, with norm `||H^(1/2)f||_2`. Define

\[
a(f,g)
=\langle H^{1/2}f,H^{1/2}g\rangle
-\langle f,Kg\rangle.
\]

By (5.3),

\[
|\langle f,Kg\rangle|
\le
\theta_{n,k}
\|H^{1/2}f\|_2\|H^{1/2}g\|_2.
\tag{7.2}
\]

Hence if `theta_{n,k}<1`, the form is coercive:

\[
\operatorname{Re}a(f,f)
\ge(1-\theta_{n,k})\|H^{1/2}f\|_2^2.
\tag{7.3}
\]

The forcing satisfies

\[
|\langle f,D\rangle|
\le\eta_{n,k}\|H^{1/2}f\|_2.
\tag{7.4}
\]

Lax–Milgram therefore yields a unique centered form-domain solution `h` of (7.1), with

\[
\boxed{
\|H^{1/2}h\|_2
\le\frac{\eta_{n,k}}{1-\theta_{n,k}}.
}
\tag{7.5}
\]

The product spectral gap gives `H>=g_rho` on centered functions, so

\[
\boxed{
\|h\|_2
\le
\frac{\sqrt2\lambda v_\rho\delta}
{g_\rho(1-\theta_{n,k})\sqrt{1-4v_\rho\varepsilon}}.
}
\tag{7.6}
\]

### Identification with the actual stationary probability

The Lax–Milgram solution initially gives a finite **signed** measure

\[
\nu(x)=q_k(x)(1+h(x)).
\]

It has total mass one because `h` is centered, and finite total variation because `h in L^2(q_k)`.

Testing (7.1) against finitely supported functions gives the coordinate stationary equations `nu L=0`. For `k<=n/2`, every tagged queue has a strictly positive singleton-arrival rate, departures have positive rate whenever a queue is nonempty, and the tagged chain is irreducible. The stable limited fork–join system has its usual stationary probability `P^N_{n,k}`. For an irreducible positive recurrent continuous-time chain, the transition probabilities satisfy

\[
P_t(x,y)\to P^N_{n,k}(y)
\]

for every `x,y`. Since `nu` is a finite signed invariant measure,

\[
\nu(y)
=\sum_x\nu(x)P_t(x,y)
\longrightarrow
P^N_{n,k}(y)\sum_x\nu(x)
=P^N_{n,k}(y),
\]

where dominated convergence uses `sum_x|nu(x)|<infinity`. Thus

\[
\boxed{\nu=P^N_{n,k}.}
\tag{7.7}
\]

In particular the true stationary density really is `1+h` and the `L^2` estimate above applies to it; positivity did not have to be assumed in the variational construction.

Finally,

\[
\begin{aligned}
d_{\rm TV}(P^N_{n,k},q_k)
&=\frac12\|h\|_{L^1(q_k)}\\
&\le\frac12\|h\|_{L^2(q_k)}.
\end{aligned}
\]

Combining with (7.6),

\[
\boxed{
 d_{\rm TV}(P^N_{n,k},q_k)
\le
\frac{\lambda v_\rho}{\sqrt2\,g_\rho}
\frac{\delta}
{(1-\theta_{n,k})\sqrt{1-4v_\rho\varepsilon}}.
}
\tag{7.8}
\]

Together with (5.3), this is an explicit `O_rho(k^2/n)` bound whenever `k^2/n` is sufficiently small. This proves (T1).

---

# 8. Transfer from queue lengths to the full workload vector

For exponential service, conditional on the queue-length vector `N=(N_1,...,N_k)`, memorylessness and independence of the service marks give an independent coordinatewise workload kernel:

* if `N_i=0`, then `W_i=0`;
* if `N_i=m>=1`, then `W_i` is a sum of `m` independent `Exp(mu)` variables, i.e. a `Gamma(m,mu)` variable.

The same product Markov kernel maps the true stationary queue-length vector to `P^W_{n,k}` and maps `q_k` to the product M/M/1 workload law `Q^W_k`. Total variation contracts under a Markov kernel, so

\[
\boxed{
 d_{\rm TV}(P^W_{n,k},Q^W_k)
\le d_{\rm TV}(P^N_{n,k},q_k).
}
\tag{8.1}
\]

Equations (7.8) and (8.1) prove (T2) and (T3).

---

# 9. What moved mathematically, and what did not

The preceding STUCK1 report isolated the desired schematic bound

\[
\|H^{-1/2}KH^{-1/2}\|
\lesssim_\rho k^2/n.
\]

Equation (5.3) proves it, with all interaction orders summed. Consequently the earlier one-bit busy/idle square-root sufficiency theorem has now been upgraded to the **entire stationary queue-length and workload vectors** for exponential service.

What does **not** move is the frozen universal source metric `M_alpha=1/3`: atomic service is part of the source class and already gives a sharp cubic obstruction. The new theorem is therefore mathematically stronger but source-wide metric-neutral.

The remaining exponential-service question is the converse at and above the square-root scale. Earlier work proves a fixed-pair covariance of order `k/n` and an order-one busy-count variance inflation when `k^2/n` is order one, but variance or chi-square inflation alone is not a total-variation lower bound. A critical-window bounded-test-function limit or CLT remains missing.

---

# 10. B21 prior-art / method-shape check, dated 2026-09-19

A bounded current search recovered the Wang et al. source (arXiv:1710.00296 / Queueing Systems 91 (2019)) and Harchol-Balter's 2021 open-problems article, but did not surface a later theorem settling the exact growing-`k` stationary-independence threshold. This is negative evidence only, not a novelty certificate.

The search also recovered Daniel Lacker, *Hierarchies, entropy, and quantitative propagation of chaos for mean field diffusions* (Probability and Mathematical Physics 4 (2023), arXiv:2105.02983), where local `k`-particle relative entropy estimates of order `(k/n)^2` are obtained for a class of mean-field diffusions under a functional inequality, as well as later relative-entropy propagation-of-chaos work. These are **methodological analogues only**. They do not directly cover the present simultaneous batch-arrival jump generator, and no external theorem is used to justify (4.2)–(7.8).

Primary URLs checked:

- https://arxiv.org/abs/1710.00296
- https://www.pdl.cmu.edu/PDL-FTP/CloudComputing/QUESTA21.pdf
- https://arxiv.org/abs/2105.02983

---

# 11. Exact remaining gap and next attack

The full source remains `PARTIAL`, because the exponential theorem does not determine the maximal scale for every finite-second-moment service law and does not establish a converse for atomless service.

The clean next problem is:

> If exponential service satisfies `k^2/n -> tau in (0,infinity)`, prove or refute that the full stationary law stays a positive total-variation distance from the independent product law.

The next attack should exploit exchangeability and the busy count rather than repeat the now-solved sufficiency operator problem. A promising route is to identify limiting factorial moments/cumulants of the busy count at the square-root window and obtain a bounded statistic separating it from `Binomial(k,rho)`.

No finite certificate is involved in this theorem-sized result; the proof is written above rather than replaced by a numerical checker.
