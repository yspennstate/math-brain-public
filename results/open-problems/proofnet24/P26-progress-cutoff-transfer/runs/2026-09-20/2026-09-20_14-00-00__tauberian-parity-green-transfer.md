Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — no authenticated runtime metadata establishes a separate maximum-effort setting.**

# P26 / LIVE20 T08 — Tauberian parity-smoothed Green transfer and pure odd-distance bipartite cutoff

**Parent status:** `PARTIAL / OPEN` for Salez Problem 2.3 before this run; `PARTIAL / OPEN` after this run.

**Restricted theorem status:** `CANDIDATE_FULL` for Theorems A–C below, pending later independent review.

**Publication novelty:** `UNVERIFIED`. A bounded repository search for `pure odd distance bipartite cutoff` and bounded web searches for `exact distance three graph random walk cutoff Ramanujan`, `distance-3 graph cutoff random walk Ramanujan`, and variants did not recover a matching ordinary-SRW theorem. This is negative evidence only, not a priority certificate.

Repository/branch: `yspennstate/math-open-problems` / `master`.
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.
Run root: `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/`.

## 0. Compact handoff, failed-route preservation, and C28/NM13-01 split

The newest own substantive report read before this run was

`2026-09-20_13-00-56__all-distance-spherical-green-transfer.md`.

It proved an all-fixed-distance spherical/Chebyshev transfer for exact even ancestor distances on the non-Ramanujan Eisenstein `(9,3)` Cayley bigraph family. Its next attack explicitly asked for a short-radius positive average / Tauberian shell-Green criterion rather than another one-off exact distance. That is the route executed here.

Two inherited obstructions are preserved rather than silently erased:

1. the proposed Ihara / first-repeated-directed-edge tangle decomposition remains unproved;
2. raw pointwise NBRW shell `L^2` can be too stringent for total-variation cutoff. The class constructed below gives a particularly clean reason: every pointwise shell has a permanent bipartition mode and hence `chi^2 >= 1`, while a two-shell positive average cancels that mode exactly.

The newest relevant historical-C28 successor report read is NM13-01's

`2026-09-20T10-30-00Z__normalizing-voltage-two-front-cutoff.md`.

NM13-01 now controls an algebraic/hidden-coordinate route: normalizing voltage lifts, two macroscopic TV fronts, and growing hidden state spaces without paying the old hidden `L^2` cardinality budget. P26 stays complementary: shell Green functions, positive radial averaging, covering-tree radial clocks, and spectral filters. Nothing below uses the voltage-lift mechanism.

There is no three-unchanged-run trigger: the preceding run enlarged the exact-distance hierarchy, while the present run changes the transfer mechanism from **pointwise late-shell Green control** to **positive averaged-shell Green control plus radial Tauberian smoothing**.

## 1. Exact source convention and current exact boundary

Justin Salez, `arXiv:2508.21055v1` (submitted 28 August 2025), defines the continuous-time chain by inserting independent mean-one exponential waiting times between discrete jumps. Thus if `P` is the discrete transition matrix,

\[
H_t=e^{t(P-I)}=e^{-t}\sum_{k\ge0}\frac{t^kP^k}{k!}.
\tag{1.1}
\]

Problem 2.3 is exactly:

> Prove that all vertex-transitive expanders exhibit cutoff.

Here an expander sequence has diverging size, uniformly bounded degree and one-sided spectral gap bounded away from zero.

The fresh checked external boundary on 20 September 2026 remains materially narrower:

* Dylan J. Altschuler, `arXiv:2609.14945`, submitted 14 September 2026, proves an explicit Gaussian-profile cutoff theorem for every fixed-degree **long-range expander** sequence. His Definition 1.3 requires, for some fixed `c>0`,
  \[
  |B(S,r)|\ge \min\{3n/4,c|S|(d-1)^r\}
  \]
  for all sets and radii. The paper proves the strict hierarchy
  \[
  \text{Ramanujan}\Longrightarrow\text{long-range}\Longrightarrow\text{spectral},
  \]
  with neither converse. Long-range expansion is therefore not synonymous with the hypothesis of Salez Problem 2.3.
* Francesco Pedrotti and Justin Salez, `arXiv:2607.05345`, submitted 6 July 2026, prove a universal cutoff-window bound `O(1/gamma_*)` in terms of a non-equilibrium Poincare quantity. The checked statement does not derive the required `gamma_*` estimate merely from vertex transitivity plus an ordinary fixed spectral gap.

The root `POSTED.md` exclusions were read. In particular, nothing below reopens the posted Salez Problem 2.4 / Abelian Cayley product-condition result.

## 2. Parent before/after and mechanism-level advance

### Parent problem before

Salez Problem 2.3 was `OPEN / PARTIAL`. P26 had proved several source-valid transitive spectral-but-not-long-range cutoff classes using pointwise entropy or Green control of NBRW endpoint shells. The latest exact-distance theorem still required the late shell itself to have small Green excess (or to be repairable by a separate spectral cleanup).

### Parent problem after

Salez Problem 2.3 remains `OPEN / PARTIAL`; no theorem from arbitrary transitivity plus spectral expansion is claimed.

The proved restricted scope is strictly enlarged to a class for which the old pointwise Green hypothesis is **false at every radius**: for every fixed odd `m>=3`, ordinary rate-one continuous-time SRW on the pure exact-distance-`m` graph of a bipartite degree-six Ramanujan Cayley family has an explicit Gaussian cutoff profile. The first concrete member `m=3` is a 150-regular bipartite vertex-transitive Cayley spectral expander, is not long-range expanding, and cuts off at

\[
\frac{75}{194}\log_5 N+O(1)
\]

with a `Theta(sqrt(log N))` Gaussian window.

### Mechanism-level movement

The new mechanism is a **Tauberian positive shell average**. Instead of asking each late shell `nu_r` to be close to equilibrium, average a short block

\[
\bar\nu_r=\sum_{j=0}^{J}a_j\nu_{r+j},\qquad a_j\ge0,\quad\sum_j a_j=1.
\]

The actual law can be replaced by the averaged-shell mixture at a cost equal to the total-variation change produced by convolving the radial law with `a`. If the radial front is smooth on the scale `J=o(window)`, that cost is negligible. This permits cancellation **before squaring in the Green function**.

For the application below the filter is only

\[
(a_0,a_1)=(1/2,1/2).
\]

On a bipartite base the NBRW parity mode has eigenvalue `(-1)^r`; the two-shell average annihilates it exactly. Pointwise shell `chi^2` never tends to zero, but the averaged-shell `chi^2` does after only `O(log log N)` extra radial layers. The exact continuous-time convention is essential: Poissonization smooths the radial parity, whereas in discrete time the radial law has fixed parity and a unit shift stays at TV distance one.

## 3. Theorem A — Tauberian averaged-shell Green transfer

Let `X_n` be a finite transitive chain with uniform stationary law `pi_n`, run in the exact rate-one convention (1.1). Suppose from each start `x` there is an exact shell representation

\[
\mu_{n,t}^x:=\delta_xH_t
=\sum_{r\ge0}p_{n,t}(r)\nu_{n,r}^x,
\qquad p_{n,t}(r)=\Pr(R_t=r).
\tag{3.1}
\]

Fix a probability vector `a=(a_0,...,a_J)` and define

\[
\bar\nu_{n,r}^x:=\sum_{j=0}^{J}a_j\nu_{n,r+j}^x.
\tag{3.2}
\]

Extend `p_{n,t}(r)=0` for `r<0` and define the one-sided convolution

\[
(p_{n,t}*a)(s):=\sum_{j=0}^{J}a_jp_{n,t}(s-j).
\tag{3.3}
\]

Let `ell_n` be an entropic radius. Assume that for `h>=0`

\[
\sup_x\sup_{r\ge ell_n+h}
\chi^2(\bar\nu_{n,r}^x\Vert\pi_n)\le \bar G_n(h),
\tag{3.4}
\]

and that every original shell of radius at most `ell_n-h` is supported in a set `A_{n,x}(ell_n-h)` with

\[
\sup_x\pi_n(A_{n,x}(ell_n-h))\le L_n(h).
\tag{3.5}
\]

Then

\[
\boxed{
\Pr(R_t\le ell_n-h)-L_n(h)
\le d_n(t)
}
\tag{3.6}
\]

and

\[
\boxed{
 d_n(t)
\le
\|p_{n,t}-p_{n,t}*a\|_{TV}
+\Pr(R_t<ell_n+h)
+\frac12\sqrt{\bar G_n(h)}.
}
\tag{3.7}
\]

### Proof

The lower bound is the usual shell-support test. Put `A=A_{n,x}(ell_n-h)`. By (3.1),

\[
\mu_{n,t}^x(A)\ge\Pr(R_t\le ell_n-h),
\]

whereas `pi_n(A)<=L_n(h)`. Testing total variation against `A` gives (3.6).

For the upper bound define the averaged-shell mixture

\[
\widetilde\mu_{n,t}^x
:=\sum_{r\ge0}p_{n,t}(r)\bar\nu_{n,r}^x.
\tag{3.8}
\]

Using (3.2) and changing index,

\[
\widetilde\mu_{n,t}^x
=\sum_{s\ge0}(p_{n,t}*a)(s)\nu_{n,s}^x.
\tag{3.9}
\]

The map sending a mixing law on the shell index to the corresponding mixture of the probability kernels `nu_s^x` is a Markov kernel, hence contracts total variation. Therefore

\[
\|\mu_{n,t}^x-\widetilde\mu_{n,t}^x\|_{TV}
\le \|p_{n,t}-p_{n,t}*a\|_{TV}.
\tag{3.10}
\]

Now split (3.8) at `ell_n+h`. The early part costs at most its total mass `Pr(R_t<ell_n+h)`. For each late averaged shell, Cauchy--Schwarz gives

\[
\|\bar\nu_{n,r}^x-\pi_n\|_{TV}
\le\frac12\sqrt{\chi^2(\bar\nu_{n,r}^x\Vert\pi_n)}
\le\frac12\sqrt{\bar G_n(h)}.
\]

Convexity of TV and (3.10) prove (3.7). `QED`

### Quantitative window corollary

Suppose a radial front has location `ell_n/v`, width `w_n`, and a CLT on that width. If there is a choice `J_n=o(w_n)` and positive filters `a^{(n)}` supported on `[0,J_n]` such that, uniformly for `t=ell_n/v+O(w_n)`,

\[
\|p_{n,t}-p_{n,t}*a^{(n)}\|_{TV}=o(1),
\tag{3.11}
\]

and there exists `h_n=o(w_n)` with

\[
\bar G_n(h_n)+L_n(h_n)=o(1),
\tag{3.12}
\]

then the chain has the same limit profile as the radial front.

A useful elementary sufficient condition for (3.11) is shift smoothness. If

\[
\Delta_n(t):=\|p_{n,t}-p_{n,t}(\cdot-1)\|_{TV},
\]

then by telescoping and convexity,

\[
\|p_{n,t}-p_{n,t}*a\|_{TV}
\le \Delta_n(t)\sum_{j=0}^{J}ja_j
\le J\Delta_n(t).
\tag{3.13}
\]

Thus `Delta_n(t)=O(1/w_n)` permits any `J=o(w_n)` positive shell filter without changing the window.

## 4. Bipartite Ramanujan shells: pointwise Green fails, two-shell Green succeeds

Let `B_N` be a connected bipartite 6-regular vertex-transitive Ramanujan graph with `N` vertices and girth tending to infinity. We construct a concrete Cayley sequence in Section 8. Put `q=5`, and let

\[
P=A/6
\]

be normalized adjacency. Let `K_r` be the endpoint kernel of length-`r` nonbacktracking walk started at a vertex (uniform first edge, then uniform nonbacktracking choices). Then

\[
K_r=p_r(P),
\tag{4.1}
\]

where

\[
p_0=1,\qquad p_1=x,\qquad
p_2(x)=\frac{6x^2-1}{5},
\tag{4.2}
\]

and for `r>=2`,

\[
p_{r+1}(x)=\frac{6x p_r(x)-p_{r-1}(x)}5.
\tag{4.3}
\]

Because `B_N` is bipartite, `-1` is an eigenvalue of `P` and induction in (4.2)--(4.3) gives

\[
p_r(-1)=(-1)^r.
\tag{4.4}
\]

### Pointwise obstruction

Vertex transitivity makes the diagonal of `K_r^2` constant, hence

\[
\chi^2(K_r(x,\cdot)\Vert\pi)
=\operatorname{tr}(K_r^2)-1
=\sum_{i=2}^{N}p_r(\lambda_i)^2.
\tag{4.5}
\]

The bipartition eigenvalue contributes exactly one, so

\[
\boxed{
\chi^2(K_r(x,\cdot)\Vert\pi)\ge1
\quad\text{for every }r.
}
\tag{4.6}
\]

Indeed `K_r(x,.)` is supported on a single parity class, so its TV distance from uniform is at least `1/2`. Thus the preceding pointwise late-shell Green hypothesis cannot make the shell error vanish on this class.

### Two-shell parity filter

Define

\[
\bar K_r:=\frac12(K_r+K_{r+1}),
\qquad
\bar p_r(x):=\frac12(p_r(x)+p_{r+1}(x)).
\tag{4.7}
\]

Equation (4.4) gives the exact cancellation

\[
\boxed{\bar p_r(-1)=0.}
\tag{4.8}
\]

All remaining nontrivial eigenvalues of a bipartite Ramanujan graph lie in

\[
|\lambda|\le\rho:=\frac{\sqrt5}{3}.
\tag{4.9}
\]

For such `lambda`, write `z=3lambda/sqrt(5) in [-1,1]`. The standard nonbacktracking Chebyshev formula is

\[
p_r(\lambda)
=\frac{5^{1-r/2}}6
\left(
U_r(z)-\frac15U_{r-2}(z)
\right),
\tag{4.10}
\]

with `U_{-1}=0`. Since `|U_j(z)|<=j+1`,

\[
|p_r(\lambda)|
\le\left(r+\frac23\right)5^{-r/2}
\le(r+1)5^{-r/2}.
\tag{4.11}
\]

Therefore

\[
|\bar p_r(\lambda)|
\le (r+2)5^{-r/2}.
\tag{4.12}
\]

Applying the same transitive trace identity as in (4.5), now to `bar K_r`, and using (4.8),

\[
\chi^2(\bar K_r(x,\cdot)\Vert\pi)
=\sum_{\lambda_i\notin\{1,-1\}}\bar p_r(\lambda_i)^2
\le N(r+2)^2 5^{-r}.
\tag{4.13}
\]

Let

\[
L_N=\lceil\log_5 N\rceil.
\tag{4.14}
\]

Since `N5^{-L_N}<=1`, and `(r+2)^2 5^{-r}` decreases for all relevant large `r`,

\[
\boxed{
\sup_{r\ge L_N+h}
\chi^2(\bar K_r(x,\cdot)\Vert\pi)
\le (L_N+h+2)^2 5^{-h}.
}
\tag{4.15}
\]

This is the required averaged Green estimate.

### Quantitative cleanup cost

For fixed `epsilon>0`, taking

\[
h_{N,\epsilon}
=2\log_5 L_N+2\log_5(4/\epsilon)+O(1)
\tag{4.16}
\]

makes the Green term in Theorem A at most `epsilon` for all large `N`. Thus the Green repair costs only

\[
\boxed{O(\log\log N+\log(1/\epsilon))}
\tag{4.17}
\]

radial layers, which is negligible relative to the `sqrt(log N)` front width.

## 5. Pure odd-distance graphs and their spectrum

Fix an odd integer `m>=3`. Once `girth(B_N)>2m`, define `Y_{N,m}` on the **same vertex set** by

\[
x\sim_{Y_{N,m}}y
\quad\Longleftrightarrow\quad
\operatorname{dist}_{B_N}(x,y)=m.
\tag{5.1}
\]

The girth assumption ensures that each distance-`m` endpoint is reached by a unique nonbacktracking path of length `m`, so `Y_{N,m}` is regular of degree

\[
\boxed{D_m=6\,5^{m-1}.}
\tag{5.2}
\]

Every automorphism of `B_N` preserves distance, hence `Y_{N,m}` is vertex-transitive; if `B_N` is Cayley, so is `Y_{N,m}`.

The normalized SRW kernel of `Y_{N,m}` is exactly

\[
\boxed{Q_m=K_m=p_m(P).}
\tag{5.3}
\]

Since `m` is odd, `p_m(-1)=-1`: the output itself is bipartite. This is harmless in the continuous-time convention because the generator eigenvalue is `-2` on that mode.

For the Ramanujan bulk, (4.11) gives

\[
|p_m(\lambda)|\le(m+1)5^{-m/2}<1
\qquad(m\ge3).
\tag{5.4}
\]

The function on the right decreases for `m>=1`. Thus `1` is the unique eigenvalue equal to one, `Y_{N,m}` is connected, and its **one-sided** normalized spectral gap satisfies

\[
\boxed{
\operatorname{gap}(Y_{N,m})
\ge1-(m+1)5^{-m/2}>0.
}
\tag{5.5}
\]

This is exactly the spectral-expander notion in Salez Problem 2.3; no absolute gap is being claimed.

For the first new case `m=3`,

\[
p_3(x)=\frac{36x^3-11x}{25}.
\tag{5.6}
\]

Exact optimization on `[-sqrt(5)/3,sqrt(5)/3]` gives

\[
\sup |p_3|=\frac{3\sqrt5}{25},
\tag{5.7}
\]

so

\[
\boxed{
\operatorname{gap}(Y_{N,3})
\ge1-\frac{3\sqrt5}{25}
=0.7316718427\ldots .
}
\tag{5.8}
\]

The exact checker independently verifies (5.6)--(5.8).

## 6. Exact shell representation and radial clock

Lift rate-one SRW on `Y_{N,m}` to the exact-distance-`m` graph of the universal cover `T_6`. Let `R_t` be the ordinary tree distance from the root.

The stabilizer of the root in `Aut(T_6)` is transitive on each ordinary sphere. Because exact-distance-`m` adjacency is invariant under this stabilizer, conditional on `R_t=r` the lifted endpoint is uniform on the sphere of radius `r`. Projecting through the covering `T_6 -> B_N` gives exactly the NBRW endpoint kernel `K_r`. Therefore

\[
\boxed{
\delta_xH_t^{Y_{N,m}}
=\sum_{r\ge0}\Pr(R_t=r)K_r(x,\cdot).
}
\tag{6.1}
\]

This is the shell decomposition to which Theorem A is applied with

\[
\bar\nu_r=\frac12(K_r+K_{r+1}).
\]

### Interior radial increments

At a tree vertex of radius at least `m`, classify an exact-distance-`m` endpoint by the number `a` of initial edges, `0<=a<=m`, followed toward the root before the path turns outward. The radial increment is

\[
\xi_m=m-2a.
\tag{6.2}
\]

Writing `q=5`, the exact multiplicities are

\[
N_0=q^m,
\qquad
N_a=(q-1)q^{m-a-1}\quad(1\le a<m),
\qquad
N_m=1.
\tag{6.3}
\]

Their sum is

\[
q^m+q^{m-1}=6\,5^{m-1}=D_m.
\]

A finite geometric-sum calculation gives

\[
\mathbb E a
=\frac{q(1-q^{-m})}{q^2-1},
\]

hence the exact speed

\[
\boxed{
v_m
=m-\frac{2q(1-q^{-m})}{q^2-1}
=m-\frac5{12}(1-5^{-m})>0.
}
\tag{6.4}
\]

The compound-Poisson second-moment rate is the explicit finite sum

\[
\boxed{
M_{2,m}
=\frac{1}{D_m}
\left[
q^m m^2
+\sum_{a=1}^{m-1}(q-1)q^{m-a-1}(m-2a)^2
+m^2
\right].
}
\tag{6.5}
\]

The radial chain differs from this translation-invariant increment process only in the finite set of radii `<m`. Since `v_m>0`, a small exponential Lyapunov function `e^{-theta R}` gives geometric tails for returns to that finite boundary region. Consequently the total boundary correction is `O_P(1)` and the rate-one Poissonized radial chain obeys

\[
\boxed{
\frac{R_t-v_mt}{\sqrt{M_{2,m}t}}
\Longrightarrow N(0,1).
}
\tag{6.6}
\]

The use of `M_{2,m}=E xi_m^2`, rather than `Var(xi_m)`, is forced by the rate-one Poisson clock: for a compound-Poisson sum, the variance rate is `E xi_m^2`.

## 7. Continuous-time parity smoothing of the radial law

The remaining hypothesis of Theorem A is the Tauberian error

\[
\Delta_m(t)
:=\|\mathcal L(R_t)-\mathcal L(R_t+1)\|_{TV}.
\tag{7.1}
\]

For every fixed odd `m`,

\[
\boxed{\Delta_m(t)=O_m(t^{-1/2}).}
\tag{7.2}
\]

### Proof

Outside the finite boundary region, the radial process is a compound-Poisson walk with jump law (6.2)--(6.3). Positive drift plus the exponential Lyapunov estimate implies that there are `c_m,C_m>0` such that, with probability at least `1-C_me^{-c_mt}`, the process is at radius `>=c_mt` at time `t/2` and the free increment process run during `[t/2,t]` never reaches the boundary. On that event the second-half evolution can be coupled exactly to an independent free compound-Poisson increment sum `S_{t/2}`. The coupling failure is exponentially small.

Because `m` is odd, the increment `+1` occurs: it corresponds to

\[
a=(m-1)/2,
\]

and has a fixed positive probability `alpha_m`. Poisson thinning therefore decomposes

\[
S_s=N_s+Z_s,
\]

where `N_s ~ Pois(alpha_m s)` and `N_s` is independent of `Z_s`. Convolution contracts total variation, so

\[
\|\mathcal L(S_s)-\mathcal L(S_s+1)\|_{TV}
\le
\|\mathrm{Pois}(\alpha_ms)-[\mathrm{Pois}(\alpha_ms)+1]\|_{TV}.
\tag{7.3}
\]

For a Poisson law, unimodality telescopes the right side to its maximal point mass, hence it is `O_m(s^{-1/2})` by Stirling. Mixing over the first-half position cannot increase TV, and adding the exponentially small coupling failure proves (7.2). `QED`

This is where Salez's exact continuous-time convention is used in an essential way. In discrete time, every exact odd-distance step flips radial parity, so at a fixed number of steps the radial law and its unit shift have disjoint supports and TV distance one. The rate-one Poisson clock randomizes the number-of-jumps parity and creates the `t^{-1/2}` smoothing in (7.2).

## 8. Theorem B — cutoff for all fixed pure odd distances on bipartite Ramanujan covers

Let `G_n` be any nonbipartite degree-six LPS Ramanujan Cayley sequence of logarithmic girth, and let `B_N` be its canonical bipartite double cover. Concretely, if

\[
G_n=\mathrm{Cay}(\Gamma_n,S_n),
\]

then

\[
B_N=\mathrm{Cay}(\Gamma_n\times C_2,\{(s,1):s\in S_n\}).
\tag{8.1}
\]

The cover is connected because `G_n` is nonbipartite, is bipartite and Cayley, has the same degree six, and has spectrum

\[
\{\pm\lambda_i(G_n)\}.
\]

Thus its only trivial bipartite eigenvalues are `+1,-1`, while every other normalized eigenvalue lies in `[-sqrt(5)/3,sqrt(5)/3]`. A graph covering cannot decrease girth, so the girth still tends to infinity.

Fix any odd `m>=3` and form `Y_{N,m}` by (5.1). Then the sequence is a bounded-degree vertex-transitive Cayley spectral expander by Section 5.

Let

\[
L_N=\lceil\log_5N\rceil.
\]

For the upper bound in Theorem A take the parity filter `(1/2,1/2)`. Equations (4.15) and (7.2) give, uniformly for

\[
t=L_N/v_m+O(\sqrt{L_N}),
\]

\[
\|p_t-p_t*a\|_{TV}=O(L_N^{-1/2}),
\tag{8.2}
\]

while choosing

\[
h_N=3\log_5L_N
\tag{8.3}
\]

gives

\[
\bar G_N(h_N)=o(1).
\tag{8.4}
\]

For the lower bound, every shell `K_r(x,.)` with `r<=L_N-h` is supported in the ordinary base ball `B_{B_N}(x,L_N-h)`. The universal degree bound gives

\[
|B_{B_N}(x,L_N-h)|\le C5^{L_N-h},
\]

so

\[
\pi(B_{B_N}(x,L_N-h))\le C'5^{-h}.
\tag{8.5}
\]

Thus the lower error also vanishes for (8.3). Since `h_N=o(sqrt(L_N))`, Theorem A and the radial CLT (6.6) squeeze total variation to the radial Gaussian front.

### Theorem B

For every fixed odd `m>=3`,

\[
\boxed{
 d_{Y_{N,m}}\!\left(
 \frac{L_N}{v_m}+z\sqrt{L_N}
 \right)
 \longrightarrow
 \Phi\!\left(-\frac{z}{\tau_m}\right),
 \qquad
 \tau_m^2=\frac{M_{2,m}}{v_m^3}.
}
\tag{8.6}
\]

Consequently

\[
\boxed{
 t_{mix}^{Y_{N,m}}(\epsilon)
 =\frac{L_N}{v_m}
 +\tau_m\Phi^{-1}(1-\epsilon)\sqrt{L_N}
 +o(\sqrt{L_N}).
}
\tag{8.7}
\]

The Green/Tauberian overhead is explicitly only

\[
O(\log\log N+\log(1/\epsilon)),
\]

strictly smaller than the `Theta(sqrt(log N))` radial window.

## 9. Theorem C — concrete new 150-regular class at pure distance three

Take `m=3`. The exact radial increment multiplicities from (6.3) are

\[
\begin{array}{c|rrrr}
\Delta R&-3&-1&1&3\\ \hline
\#&1&4&20&125.
\end{array}
\tag{9.1}
\]

The output degree is

\[
D_3=150.
\]

The exact radial moments are

\[
\boxed{v_3=\frac{194}{75}},
\qquad
\boxed{M_{2,3}=\frac{193}{25}},
\tag{9.2}
\]

and hence

\[
\boxed{
\tau_3^2
=\frac{M_{2,3}}{v_3^3}
=\frac{3256875}{7301384}
=0.4460626916\ldots .
}
\tag{9.3}
\]

Therefore the pure distance-three Cayley graphs satisfy

\[
\boxed{
T_N=\frac{75}{194}\log_5N+O(1)
}
\tag{9.4}
\]

and the explicit limit profile

\[
\boxed{
 d_{Y_{N,3}}\!\left(
 T_N+z\sqrt{\log_5N}
 \right)
 \longrightarrow
 \Phi\!\left(
 -z\sqrt{\frac{7301384}{3256875}}
 \right).
}
\tag{9.5}
\]

The normalized one-sided spectral gap is at least

\[
1-\frac{3\sqrt5}{25}>0.7316.
\tag{9.6}
\]

This class is structurally distinct from the preceding P26 applications: it uses a **pure odd sphere on a bipartite ancestor**, so the output remains bipartite and every individual NBRW shell stays macroscopically far from uniform. The proof succeeds because consecutive shell averaging cancels the parity mode and the continuous-time radial law is Tauberian-smooth.

## 10. These outputs are spectral but not long-range

For fixed odd `m>=3`, one output step moves exactly `m` edges in the degree-six base. Hence

\[
B_{Y_{N,m}}(x,r)\subseteq B_{B_N}(x,mr),
\]

and the universal degree bound gives

\[
|B_{Y_{N,m}}(x,r)|\le C_m5^{mr}.
\tag{10.1}
\]

The output degree is `D_m=6*5^{m-1}`, so the tree branching benchmark in Altschuler's Definition 1.3 is

\[
q_{out}=D_m-1=6\,5^{m-1}-1.
\]

For every `m>=2`,

\[
5^m<6\,5^{m-1}-1=q_{out}.
\tag{10.2}
\]

Take

\[
r_N=\left\lfloor\frac12\log_{q_{out}}N\right\rfloor.
\]

Then `q_out^{r_N}=Theta(sqrt(N))`, so for large `N` the `3N/4` cap in the LRE definition is inactive, while

\[
\frac{|B_{Y_{N,m}}(x,r_N)|}{q_{out}^{r_N}}
\le C_m\left(\frac{5^m}{q_{out}}\right)^{r_N}
\longrightarrow0.
\tag{10.3}
\]

Thus no fixed `c>0` can satisfy long-range expansion. In the concrete distance-three class the competing branching bases are

\[
125<149.
\]

Therefore Theorem C gives a genuine bounded-degree vertex-transitive **spectral-but-not-long-range** cutoff class; it is not covered by Altschuler's output hypothesis.

## 11. Exact executed sanity check

The exact checker executed in this run is

`2026-09-20_14-00-00__tauberian-parity-green-check.py`.

Its archived output is

`2026-09-20_14-00-00__tauberian-parity-green-check.out`.

It certifies the finite/algebraic core:

* degree `150`;
* radial multiplicities `{-3:1,-1:4,1:20,3:125}`;
* `v=194/75`, `M2=193/25`, `tau^2=3256875/7301384`;
* `p_3(x)=x(36x^2-11)/25`;
* exact Ramanujan-bulk maximum `3sqrt(5)/25` and gap `1-3sqrt(5)/25`;
* `p_3(-1)=-1` and exact consecutive-shell parity cancellation;
* the general drift formula through independent exact enumeration for distances `1,...,15`;
* strict branching mismatch `125<149`.

The terminal marker is

`P26_T08_TAUBERIAN_PARITY_GREEN_EXACT_PASS`.

The checker does not substitute for the analytic Tauberian, Green-trace or radial-coupling arguments above.

## 12. Residual obstruction and next attack

This run removes a real but specific obstruction: **negative oscillatory modes need not be controlled pointwise**. A positive shell filter can cancel or damp them before the Green square is taken, and the exact continuous-time Poissonization pays only a negligible radial smoothing cost.

The remaining parent obstruction is now more sharply one-sided. Positive exceptional NBRW modes do not oscillate, so a positive short average cannot cancel a polynomially large sector whose decay rate is genuinely slower than the Ramanujan rate. Arbitrary vertex transitivity plus ordinary spectral expansion still does not supply the required near-entropic Green control for those modes.

The next P26 attack should therefore optimize a short positive polynomial filter

\[
A(z)=\sum_{j=0}^{J}a_jz^j,
\qquad a_j\ge0,
\qquad J=o(\sqrt{\log n}),
\]

against the **negative** exceptional roots of the NBRW recurrence and prove a filtered Green criterion depending only on the remaining positive exceptional spectral mass. The decisive target is a theorem of the form: if the positive exceptional sector has weighted defect `exp(o(sqrt(log n)))`, while the negative sector is arbitrary subject to the ordinary spectral gap, then cutoff follows. This would separate the genuinely dangerous positive spectrum from the parity/oscillation artifacts and remains complementary to NM13-01's voltage/hidden-coordinate likelihood program.

No switch away from T08 is triggered: the present run proves both a new transfer theorem and a new source-valid transitive class.

## 13. Failed-route history carried forward

* Ihara / first-repeated-directed-edge tangle control: **UNRESOLVED**, not counted as progress.
* Universal pointwise NBRW shell `L^2` from transitivity plus gap: **FAILED as a route**, with earlier product obstructions and the present permanent bipartite `chi^2>=1` obstruction.
* Maximal tree-rate ball growth from transitivity plus gap: **FAILED as a general implication**; Altschuler explicitly proves spectral expansion does not imply LRE.
* Crude exceptional-mode counting: useful only in restricted regimes; weighted and now filtered mechanisms are strictly more flexible.

## 14. ledger_delta

```yaml
ledger_delta:
  parent: T08 / Salez arXiv:2508.21055 Problem 2.3
  parent_before: OPEN / PARTIAL
  parent_after: OPEN / PARTIAL
  source_convention: rate-one continuous time H_t = exp(t(P-I))
  exact_scope_boundary:
    - Altschuler arXiv:2609.14945 (2026-09-14): fixed-degree long-range expanders; LRE strictly stronger than spectral expansion
    - Pedrotti-Salez arXiv:2607.05345 (2026-07-06): non-equilibrium-Poincare/local-product window criterion
  mechanism_progress:
    theorem: positive Tauberian averaged-shell Green transfer
    quantitative_error: TV(radial law, positive short convolution) + late averaged-shell chi-square
    demonstrated_gain: cancels the permanent bipartite NBRW parity mode before squaring
    continuous_time_role: radial unit-shift TV = O(t^{-1/2}); discrete-time parity would give shift TV = 1
    cleanup_overhead: O(log log N + log(1/epsilon)) radial layers
  class_progress:
    class: pure exact odd-distance-m graphs, fixed odd m>=3, on canonical bipartite double covers of degree-six nonbipartite LPS Ramanujan Cayley graphs
    output_properties:
      - bounded degree and vertex-transitive Cayley
      - bipartite
      - uniform one-sided spectral gap
      - not long-range expanding
      - Gaussian total-variation cutoff in exact Salez continuous time
    first_new_member:
      m: 3
      degree: 150
      gap_lower: 1 - 3*sqrt(5)/25
      center: (75/194) log_5 N + O(1)
      radial_variance_rate: 193/25
      profile_tau_squared: 3256875/7301384
      branching_obstruction: 125 < 149
  pointwise_green_obstruction:
    statement: chi^2(K_r(x,.),uniform) >= 1 for every r because p_r(-1)^2=1
    repaired_by: (K_r + K_{r+1})/2, which annihilates the -1 mode exactly
  c28_coordination: NM13-01 owns normalizing-voltage/two-front hidden-coordinate transfer; P26 owns shell-Green/radial-filter transfer
  not_counted_as_advances:
    - source rechecks
    - unchanged parent OPEN status
    - commit/checker receipts
    - unresolved Ihara tangle proposal
  failed_routes_preserved:
    - pointwise universal NBRW L2 from transitivity + gap
    - maximal tree-rate/LRE growth from transitivity + gap
    - unproved Ihara first-repeat tangle route
  residual_obstruction: positive exceptional NBRW spectral mass can still have genuinely sub-Ramanujan decay and cannot be canceled by positive short averaging
  next_attack: filtered Green theorem using short positive polynomial filters to eliminate negative exceptional modes, leaving only a weighted positive-exceptional defect to control
```

End of complete P26 substantive T08 report.
