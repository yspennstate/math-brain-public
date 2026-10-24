Model actually running: **GPT-5.6 Sol. Reasoning/effort level: UNVERIFIED** — no separately authenticated maximum-effort metadata is exposed.

# NM13-01 / LIVE20 T08 — synchronous tensor-product cutoff under one common Poisson clock

**Parent status before:** `PARTIAL / OPEN` for Salez Problem 2.3.

**Parent status after:** `PARTIAL / OPEN` for Salez Problem 2.3. The parent conjecture is not claimed solved.

**Restricted theorem status:** `CANDIDATE_FULL` for Theorems A--D and the degree-36 application below, pending later independent review.

**Publication novelty:** `UNVERIFIED`. A bounded dated search found classical work on Cartesian-product continuous-time walks and the standard Ramanujan cutoff theorem, but no checked theorem matching the categorical/tensor graph-power, common-Poisson-clock cutoff transfer below. This is negative evidence only and is not a priority claim.

Repository/branch: `yspennstate/math-open-problems` / `master`.

Controlling policy: `operations/PROGRESS20_2026-09-20.md`.

Run root: `proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/`.

## 0. Compact handoff and partner split

The newest own substantive report read before this run was

`2026-09-20T15-20-00Z__eisenstein-halved-nbrw-cutoff.md`.

It proved cutoff for left-halved Eisenstein Cayley bigraphs by a direct bi-Cayley incidence/NBRW-shell transfer. Its remaining general obstruction was structural: an arbitrary transitive spectral expander need not visibly possess a bounded local block cover or sharply mixing geodesic factor.

The newest relevant companion P26 report read was

`proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_17-59-36__cartesian-multifront-green-transfer.md`.

P26 proves an exact **Cartesian** continuous-time factorization and a Green-shell multifront theorem. In a Cartesian power, the coordinates have independent continuous-time clocks, and the limiting TV profile is an order statistic of independent radial fronts.

The present run deliberately changes mechanism. It studies the **categorical/tensor graph product**, whose source-continuous semigroup does *not* factor into independent coordinate semigroups. Instead, all coordinates share exactly one Poisson jump clock. Thus their jump counts are perfectly synchronized. The proof below shows that such maximal timing dependence still cannot destroy cutoff for a fixed number of sharp Ramanujan factors. No Green-function estimate or shell cleanup from P26 is used.

The existing `POSTED.md` exclusion for Salez Problem 2.4 / the Abelian-Cayley product-condition manuscript is respected and not reopened.

## 1. Exact source problem and current primary boundary

Justin Salez, `arXiv:2508.21055v1` (28 August 2025), defines continuous time by inserting independent mean-one exponential holding times. If `P` is the discrete transition matrix, then

\[
H_t=e^{t(P-I)}=e^{-t}\sum_{m\ge0}\frac{t^mP^m}{m!}.
\tag{1.1}
\]

Problem 2.3 is exactly:

> Prove that all vertex-transitive expanders exhibit cutoff.

A fresh 20 September 2026 source check leaves this open.

* Dylan J. Altschuler, `arXiv:2609.14945v1`, submitted 14 September 2026, proves cutoff with an explicit Gaussian profile for every fixed-degree **long-range expander** sequence. His paper proves the strict hierarchy
  \[
  \text{Ramanujan}\Longrightarrow\text{long-range expansion}\Longrightarrow\text{spectral expansion},
  \]
  with neither converse. Long-range expansion is therefore genuinely stronger than the spectral-expander hypothesis in Salez Problem 2.3.
* Francesco Pedrotti--Justin Salez, `arXiv:2607.05345` (6 July 2026), prove a local-product / non-equilibrium-Poincare sufficient mechanism. The checked theorem does not derive its non-equilibrium constant from vertex transitivity plus an ordinary fixed spectral gap alone.
* Eyal Lubetzky--Yuval Peres, `arXiv:1507.04725`, prove discrete-time cutoff on every nonbipartite fixed-degree Ramanujan graph at
  \[
  T_n^{\rm disc}=\frac d{d-2}\log_{d-1}n
  \tag{1.2}
  \]
  with a `Theta(sqrt(log n))` window and an explicit Gaussian profile. This is the discrete-time input used below; the source-continuous tensor statement is proved separately rather than silently identifying the two conventions.

## 2. Original problem before / after

### Before this run

Salez Problem 2.3 was open. NM13-01 had several source-valid vertex-transitive spectral-but-not-LRE cutoff classes, most recently the Eisenstein-halved class. P26 had just shown that a fixed **Cartesian** power of a shell-Green cutoff sequence has cutoff under independent coordinate continuous-time clocks.

### After this run

Salez Problem 2.3 remains open.

The strict new proved scope is:

> **Synchronous categorical powers.** Let `(G_n)` be any fixed-degree nonbipartite Ramanujan Cayley sequence and let `k>=2` be fixed. Form the categorical/tensor graph power
> \[
> Y_n=G_n^{\times_{\rm cat} k}.
> \]
> Then `(Y_n)` is a bounded-degree vertex-transitive spectral-expander sequence, it fails every fixed positive long-range-expansion constant, and rate-one continuous-time SRW in Salez's convention has cutoff at an explicit center with `O(sqrt(log |V(Y_n)|))` window.

If `G_n` has degree `d`, order `n`, and `N=n^k`, then

\[
\boxed{
T_N=\frac{d}{k(d-2)}\log_{d-1}N
}
\tag{2.1}
\]

and the window is

\[
\boxed{O(\sqrt{\log N}).}
\tag{2.2}
\]

For a nonbipartite degree-six Ramanujan Cayley sequence and `k=2`, the outputs are **36-regular Cayley graphs** with

\[
\boxed{
\operatorname{gap}(Y_n)\ge 1-\frac{\sqrt5}{3}
=\frac{3-\sqrt5}{3}
=0.2546440075\ldots,
}
\tag{2.3}
\]

and

\[
\boxed{
T_N=\frac34\log_5N,
\qquad
w_N=O(\sqrt{\log N}).
}
\tag{2.4}
\]

Classical LPS constructions provide explicit nonbipartite six-regular Ramanujan Cayley sequences along suitable congruence classes, so this is an explicit source-valid class.

## 3. The categorical power and its exact common-clock representation

Let `G` be a finite simple `d`-regular graph with transition kernel `P`. Its `k`-fold categorical/tensor power has vertex set `V(G)^k`, with

\[
(x_1,\ldots,x_k)\sim(y_1,\ldots,y_k)
\quad\Longleftrightarrow\quad
x_i\sim y_i\quad\text{for every }i.
\tag{3.1}
\]

It is `d^k`-regular and its discrete SRW kernel is exactly

\[
\boxed{Q=P^{\otimes k}.}
\tag{3.2}
\]

If `G=Cay(\Gamma,S)`, then

\[
\boxed{
G^{\times_{\rm cat}k}=Cay(\Gamma^k,S^k),
}
\tag{3.3}
\]

so the output is an ordinary Cayley graph and in particular vertex-transitive.

If `G` is connected and nonbipartite, `P` is irreducible and aperiodic. Hence for every pairs `x_i,y_i` there is an `M` such that `P^m(x_i,y_i)>0` for all `m>=M` and all `i`; therefore

\[
Q^m(x,y)=\prod_iP^m(x_i,y_i)>0
\]

for all sufficiently large common `m`. Thus the categorical power is connected.

Under Salez's exact continuous-time convention,

\[
H_t^Y=e^{t(P^{\otimes k}-I)}
=e^{-t}\sum_{m\ge0}\frac{t^m}{m!}(P^m)^{\otimes k}.
\tag{3.4}
\]

Equivalently:

* draw one `N_t~Poisson(t)`;
* conditional on `N_t=m`, run `k` independent copies of the **discrete** base walk for exactly `m` steps.

The word "one" matters. Every coordinate has exactly the same jump count `N_t`. The source-continuous semigroup is generally **not**

\[
(e^{t(P-I)})^{\otimes k}.
\]

That latter factorization is the Cartesian-product mechanism treated by P26; (3.4) is a different, maximally synchronized process.

## 4. Theorem A — exact common-clock TV transfer

Let

\[
d_G^{\rm disc}(m)=\max_x\|\delta_xP^m-\pi\|_{\rm TV},
\qquad
d_G^{\rm ct}(t)=\max_x\|\delta_xH_t^G-\pi\|_{\rm TV},
\]

and let `d_{Y,k}^{ct}` denote the source-continuous distance on `Y=G^{x_cat k}`. Then for every integer `m_0>=0`,

\[
\boxed{
d_G^{\rm ct}(t)
\le d_{Y,k}^{\rm ct}(t)
\le
\Pr(\operatorname{Poi}(t)<m_0)+k\,d_G^{\rm disc}(m_0).
}
\tag{4.1}
\]

### Proof

For the lower bound, project `Y` to any coordinate. By (3.4), that coordinate has law

\[
e^{-t}\sum_m\frac{t^m}{m!}\delta_xP^m
=\delta_xe^{t(P-I)}.
\]

Projection cannot increase TV distance, giving the first inequality.

For the upper bound, condition on `N_t=m`. Starting from `x=(x_1,...,x_k)`, the conditional law is

\[
\mu_{m,x}=\bigotimes_{i=1}^k\delta_{x_i}P^m.
\tag{4.2}
\]

The elementary product-TV bound gives

\[
\left\|\mu_{m,x}-\pi^{\otimes k}\right\|_{\rm TV}
\le\sum_{i=1}^k
\|\delta_{x_i}P^m-\pi\|_{\rm TV}
\le k d_G^{\rm disc}(m).
\tag{4.3}
\]

TV distance contracts under a Markov kernel, hence `d_G^{disc}(m)` is nonincreasing in `m`. On the event `m>=m_0`, (4.3) is at most `k d_G^{disc}(m_0)`; on its complement use the trivial bound one. Average over the Poisson clock to obtain (4.1). `QED`

The estimate is deliberately insensitive to correlations in the coordinate **times**: there is only one clock.

## 5. Theorem B — spectral expansion survives under absolute spectral control

Let the eigenvalues of the symmetric base kernel be

\[
1=\lambda_1,\lambda_2,\ldots,\lambda_n,
\]

and assume

\[
\max_{j\ge2}|\lambda_j|\le\rho<1.
\tag{5.1}
\]

The eigenvalues of `P^{tensor k}` are precisely

\[
\lambda_{i_1}\cdots\lambda_{i_k}.
\tag{5.2}
\]

Any nontrivial product contains at least one nontrivial factor, hence has absolute value at most `rho`. Therefore

\[
\boxed{\operatorname{gap}(Y)\ge1-\rho.}
\tag{5.3}
\]

For a nonbipartite `d`-regular Ramanujan graph,

\[
\rho\le\frac{2\sqrt{d-1}}d,
\tag{5.4}
\]

so the tensor powers are uniform spectral expanders.

This also identifies a genuine limitation of the operation. A **one-sided** base gap alone does not control eigenvalues near `-1`; multiplying two such eigenvalues can create a positive eigenvalue near `+1`. The theorem therefore uses the absolute spectral bound supplied by nonbipartite Ramanujan bases rather than pretending arbitrary spectral expansion is automatically tensor-stable.

## 6. Theorem C — source-continuous cutoff for fixed Ramanujan tensor powers

Let `(G_n)` be a nonbipartite `d`-regular Ramanujan sequence, `n=|V(G_n)|`, and fix `k`. Put

\[
\ell_n=\log_{d-1}n,
\qquad
T_n=\frac d{d-2}\ell_n.
\tag{6.1}
\]

Lubetzky--Peres give discrete-time cutoff of `G_n` at `T_n` with window `O(sqrt(ell_n))`. We prove that `Y_n=G_n^{x_cat k}` has **source-continuous** cutoff at the same numeric time `T_n`, again on a square-root window.

### 6.1 Late side

Fix `A>0` and take

\[
t_n^+(A)=T_n+A\sqrt{\ell_n},
\qquad
m_0=\left\lfloor T_n+\frac A2\sqrt{\ell_n}\right\rfloor.
\tag{6.2}
\]

Theorem A gives

\[
d_{Y_n,k}^{\rm ct}(t_n^+(A))
\le
\Pr(\operatorname{Poi}(t_n^+(A))<m_0)
+k d_{G_n}^{\rm disc}(m_0).
\tag{6.3}
\]

Because `T_n` is `Theta(ell_n)`, the Poisson standard deviation is `Theta(sqrt(ell_n))`, while its mean exceeds `m_0` by `(A/2)sqrt(ell_n)+O(1)`. A Poisson CLT or Chernoff bound therefore gives

\[
\lim_{A\to\infty}\limsup_{n\to\infty}
\Pr(\operatorname{Poi}(t_n^+(A))<m_0)=0.
\tag{6.4}
\]

The Lubetzky--Peres window theorem gives likewise

\[
\lim_{A\to\infty}\limsup_{n\to\infty}
d_{G_n}^{\rm disc}(m_0)=0.
\tag{6.5}
\]

Hence

\[
\boxed{
\lim_{A\to\infty}\limsup_{n\to\infty}
d_{Y_n,k}^{\rm ct}(T_n+A\sqrt{\ell_n})=0.
}
\tag{6.6}
\]

### 6.2 Early side: a source-continuous tree-radial lower bound

The lower half must respect the source convention rather than cite a discrete-time statement blindly.

Lift SRW from a vertex of `G_n` to the universal `d`-regular tree. Away from the root, the discrete radial increment has law

\[
\xi=\begin{cases}
+1,&\text{with probability }(d-1)/d,\\
-1,&\text{with probability }1/d,
\end{cases}
\tag{6.7}
\]

with drift

\[
v=\mathbb E\xi=\frac{d-2}{d}.
\tag{6.8}
\]

Let `N_t~Poi(t)` and

\[
S_t=\sum_{j=1}^{N_t}\xi_j.
\tag{6.9}
\]

Then

\[
\mathbb ES_t=vt,
\qquad
\operatorname{Var}(S_t)=t\mathbb E\xi^2=t.
\tag{6.10}
\]

Couple the actual reflected radial process `R_t` by using these increments away from zero and replacing a proposed step at zero by the forced `+1`. Then

\[
R_t=S_t+C_t,
\qquad C_t\ge0.
\tag{6.11}
\]

Starting from level one, the probability ever to return to zero is `1/(d-1)`. By the strong Markov property, the total number of boundary corrections has a geometric tail, so there are constants `c_d,C_d>0` with

\[
\Pr(C_t>u)\le C_de^{-c_du}
\quad\text{uniformly in }t.
\tag{6.12}
\]

Now set

\[
t_n^-(A)=T_n-A\sqrt{\ell_n}.
\tag{6.13}
\]

Then

\[
\mathbb ES_{t_n^-}
=\ell_n-vA\sqrt{\ell_n}.
\tag{6.14}
\]

By Chebyshev and (6.12),

\[
\Pr\left(
R_{t_n^-}
>\ell_n-\frac{vA}{2}\sqrt{\ell_n}
\right)
\le \frac{C_d}{A^2}+o_n(1).
\tag{6.15}
\]

Indeed, except on an exponentially small event `C_t>(vA/4)sqrt(ell_n)`, such an overshoot forces `S_t-ES_t>(vA/4)sqrt(ell_n)`, whose probability is `O_d(A^{-2})` because `Var(S_t)=Theta(ell_n)`.

If the lifted radius is at most `r`, its projection to `G_n` lies in the ordinary graph ball `B(x,r)`. For every `d`-regular graph,

\[
|B(x,r)|\le1+d\sum_{j=0}^{r-1}(d-1)^j
\le C_d(d-1)^r.
\tag{6.16}
\]

At

\[
r_n=\ell_n-\frac{vA}{2}\sqrt{\ell_n},
\]

its stationary mass is

\[
\pi_n(B(x,r_n))
\le C_d(d-1)^{-\frac{vA}{2}\sqrt{\ell_n}}
=o_n(1).
\tag{6.17}
\]

Testing TV on this ball yields

\[
\liminf_{n\to\infty}d_{G_n}^{\rm ct}(t_n^-(A))
\ge1-\frac{C_d}{A^2}.
\tag{6.18}
\]

The coordinate projection in Theorem A then gives the same lower bound for `Y_n`. Consequently

\[
\boxed{
\lim_{A\to\infty}\liminf_{n\to\infty}
d_{Y_n,k}^{\rm ct}(T_n-A\sqrt{\ell_n})=1.
}
\tag{6.19}
\]

Combining (6.6) and (6.19) proves cutoff with `O(sqrt(ell_n))` window. Since `N=n^k`,

\[
\ell_n=\frac1k\log_{d-1}N,
\]

which gives (2.1)--(2.2). `QED`

## 7. Theorem D — the class is not long-range expanding

Let `Y=G^{x_cat k}`. Every categorical-product path of length at most `r` projects in each coordinate to a base path of length at most `r`. Therefore

\[
B_Y((x_1,\ldots,x_k),r)
\subseteq
\prod_{i=1}^kB_G(x_i,r).
\tag{7.1}
\]

Using (6.16),

\[
\boxed{
|B_Y(x,r)|\le C_{d,k}(d-1)^{kr}.
}
\tag{7.2}
\]

The output degree is

\[
D=d^k,
\]

so Altschuler's LRE benchmark has branching factor

\[
D-1=d^k-1.
\]

But for every `d>=3,k>=2`,

\[
(d-1)^k<d^k-1.
\tag{7.3}
\]

Take

\[
r_N=\left\lfloor\frac12\log_{D-1}N\right\rfloor.
\tag{7.4}
\]

Then `(D-1)^{r_N}=N^{1/2+o(1)}`, so for every fixed positive candidate LRE constant the relevant minimum in the LRE definition is the tree-growth term, while

\[
\frac{|B_Y(x,r_N)|}{(D-1)^{r_N}}
\le N^{-\beta_{d,k}+o(1)},
\tag{7.5}
\]

where

\[
\boxed{
\beta_{d,k}
=\frac12\left(
1-\frac{\log((d-1)^k)}{\log(d^k-1)}
\right)>0.
}
\tag{7.6}
\]

Thus every fixed positive LRE constant fails.

For `d=6,k=2`, the actual ball-growth base is `25`, the degree-36 LRE benchmark is `35`, and

\[
\boxed{
\beta_{6,2}
=\frac12\left(1-\frac{\log25}{\log35}\right)
=0.047319169713057\ldots>0.
}
\tag{7.7}
\]

Hence the degree-36 outputs are vertex-transitive **spectral** expanders with cutoff but are quantitatively outside Altschuler's long-range-expander class.

## 8. Mechanism-level obstruction removed

The source-level conjecture has not changed, but one specific obstruction has.

P26's newest Cartesian multifront theorem obtains exact independence of coordinate continuous-time clocks. It was therefore still plausible that strong timing dependence among several sharp macroscopic factors could broaden or destroy cutoff once exact semigroup factorization disappears.

The categorical power is the opposite extreme: every coordinate makes exactly `N_t` jumps, so the coordinate jump counts have correlation one. Formula (3.4) shows that the semigroup cannot be split into independent continuous-time factors. Nevertheless Theorem A reduces the entire synchronization penalty to the single scalar Poisson fluctuation

\[
N_t-t=O_P(\sqrt t).
\]

When the discrete front already has `O(sqrt(T_n))` width, this shared-clock noise lives on the same scale and does not destroy cutoff. Therefore:

> **Removed obstruction.** Exact independent-clock factorization is not necessary for cutoff of a fixed number of sharp transitive factors; even perfect common-clock synchronization preserves a square-root cutoff window.

This argument is transitivity/Cayley specific in its output construction and complementary to P26's entropy/Green-shell transfer: it uses neither shell Green smallness nor independent radial order statistics.

The remaining obstruction toward Salez Problem 2.3 is narrower. A general vertex-transitive spectral expander need not decompose into finitely many synchronous factors at all. Moreover Theorem B exposes a parity issue: ordinary one-sided expansion does not rule out eigenvalues near `-1`, and tensoring can turn two negative modes into a slow positive mode. A natural next NM13 route is therefore to analyze **coupled stabilizer-orbital / Hecke kernels without product structure**, seeking either (i) a finite-rank synchronous-factor approximation forced by transitivity, or (ii) direct source-continuous suppression of negative/parity modes together with exact likelihood-varentropy control.

## 9. Sanity checks

Executed checker:

`2026-09-20T16-04-21Z__check_synchronous_tensor.py`

Archived output:

`2026-09-20T16-04-21Z__check_synchronous_tensor.out`

The script verifies:

1. the exact degree-six tensor-square constants;
2. the tensor-product spectrum on `K_4`;
3. the exact common-Poisson representation
   \[
   e^{t(P\otimes P-I)}
   =e^{-t}\sum_m\frac{t^m}{m!}(P^m\otimes P^m);
   \]
4. the coordinate marginal identity with source-continuous base SRW;
5. the finite-state TV sandwich (4.1) at several times; and
6. the positive non-LRE exponent.

The archived output ends

`ALL_EXACT_AND_SANITY_CHECKS_PASS`.

These finite computations are sanity checks only; the asymptotic cutoff theorem is proved in Sections 4--7.

## 10. Before/after ledger and next attack

**Original target:** OPEN before, OPEN after. No general vertex-transitive-expander cutoff theorem is claimed.

**Strict restricted gain:** fixed categorical powers of nonbipartite Ramanujan Cayley graphs are now proved to have source-continuous cutoff with an explicit center and `O(sqrt(log N))` window; the degree-six tensor square gives an explicit degree-36 spectral-but-not-LRE class.

**Mechanism gain:** perfect common-clock synchronization is no longer a candidate obstruction to cutoff for a fixed number of sharp factors.

**Preserved limitation:** the argument requires absolute spectral control to keep tensor powers expanding. It does not convert arbitrary one-sided transitive spectral expansion into that hypothesis.

**Next transitivity-specific attack:** move from genuine products to a single transitive graph whose root stabilizer has several coupled suborbits. Seek a block decomposition of the Hecke kernel in which a bounded number of macroscopic orbital coordinates share one source Poisson clock but are not independent; prove a common-clock transfer under a quantitative off-block leakage bound. If that fails, use the exact lossless stabilizer lift from the 14:15 NM13 report and target the negative-spectrum/parity sector directly.

Publication novelty remains `UNVERIFIED`, and the restricted theorem remains `CANDIDATE_FULL` pending independent review.
