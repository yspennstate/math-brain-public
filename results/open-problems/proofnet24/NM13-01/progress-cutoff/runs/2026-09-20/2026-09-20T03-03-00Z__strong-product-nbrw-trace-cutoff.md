Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** No authenticated runtime metadata establishes a maximum-effort setting.

# NM13-01 / LIVE20 T08 — strong-product cutoff outside LRE and an exact transitive NBRW collision criterion

**Parent status:** `PARTIAL / OPEN` for Salez Problem 2.3.

**Restricted results in this report:** `CANDIDATE_FULL` pending later independent review.

**Publication novelty:** `UNVERIFIED`. The theorems below are new to the repository after the bounded searches recorded here; I do not claim worldwide novelty.

Repository/branch: `yspennstate/math-open-problems` / `master`.
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.
Run root: `proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/`.

## 0. Short continuity handoff and why this route is different

LIVE20 assigns NM13-01 to T08. The pre-LIVE20 P0292 admission history and terminal handoff remain preserved and are not altered.

The three preceding NM13-01 T08 runs proved, respectively:

1. cutoff for line graphs of fixed-degree edge-transitive long-range expanders, via incidence intertwining and constant-rate decay of endpoint-invisible modes;
2. cutoff for graph truncations of fixed-degree arc-transitive long-range expanders, via a non-lumpable two-state port/radial Markov-additive process; and
3. cutoff transfer through fixed twisted finite-group Cayley extensions, where macroscopic moves apply noncommuting fiber permutations while local fiber noise contracts pathwise in `L^2`.

The newest relevant P26 report is

`proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_05-01-42__graph-square-shell-entropy-transfer.md`.

P26 there treats **same-vertex graph squares** `G^2` through a shell-entropy transfer criterion. Historical R16 work already proved the standard fixed Cartesian-product theorem and a separate synchronous direct/tensor-square theorem. Therefore this run does **not** count Cartesian products, tensor products, finite fibers, line graphs, truncations, or graph squares as new work.

The new source-valid class below is the **strong graph square**

\[
G\boxtimes G,
\]

which is the union of the Cartesian and direct/tensor edges. Its continuous-time walk has three Poisson event types: first-coordinate-only, second-coordinate-only, and genuinely synchronous two-coordinate moves. It is neither the independent-coordinate Cartesian chain nor the single-clock tensor chain.

The mechanism-level route is also new relative to the preceding NM13-01 run. That run reduced the general transitive problem to controlling marginal nonbacktracking endpoint entropy and proposed an automorphism-orbit-averaged collision/Green kernel. Here that kernel is made **exact**: vertex transitivity turns its worst-start `chi^2` collision into a scalar spectral trace of the ordinary adjacency operator. This removes the directed-edge-orbit/start dependence from that obstruction.

## 1. Exact source convention and fresh primary boundary

Justin Salez, *Modern aspects of Markov chains: entropy, curvature and the cutoff phenomenon*, arXiv:2508.21055v1 (28 August 2025), defines continuous time from a stochastic matrix `T` by

\[
P_t=e^{t(T-I)}=e^{-t}\sum_{k\ge0}\frac{t^kT^k}{k!},
\]

that is, independent mean-one exponential holding times. His Problem 2.3 states:

> Prove that all vertex-transitive expanders exhibit cutoff.

Here an expander sequence has diverging size, uniformly bounded degree, and spectral gaps bounded away from zero.

Fresh checks on 20 September 2026 recover the following current primary boundary.

* Dylan J. Altschuler, *Long-range expanders: construction and cutoff*, arXiv:2609.14945v1, submitted 14 September 2026, proves cutoff with an explicit Gaussian profile for every fixed-degree fixed-constant long-range-expander sequence. The same paper proves the strict hierarchy
  \[
  \mathrm{Ramanujan}\Longrightarrow\mathrm{long\mbox{-}range\ expansion}
  \Longrightarrow\mathrm{spectral\ expansion},
  \]
  with neither converse. Thus long-range expansion is **not** equivalent to the hypothesis in Salez Problem 2.3.
* Francesco Pedrotti and Justin Salez, *The local product condition implies cutoff*, arXiv:2607.05345 (6 July 2026), give a universal cutoff-window mechanism in terms of their non-equilibrium constant `gamma_*`. No checked theorem there derives the required `gamma_*` lower bound solely from vertex transitivity plus an ordinary spectral gap.
* The classical Lubetzky--Peres Ramanujan theorem supplies the fixed-degree discrete-time Gaussian profile used below. Altschuler extends that profile mechanism to LRE under a uniform lower spectral edge.

The exact posted Abelian-Cayley Problem-2.4 material is not reopened.

### Bounded prior-art / repository check

I searched the repository for `strong graph product`, `strong product cutoff`, and neighboring T08 product constructions. This recovered historical Cartesian and synchronous direct/tensor products but no strong-product cutoff theorem. I also searched current indexed literature for combinations of `strong product graph random walk cutoff`, `strong graph product mixing cutoff`, and `Cayley strong product cutoff Ramanujan`. I found general strong-product graph theory and existing Ramanujan/complex cutoff literature, but not the exact theorem below. This is bounded negative evidence only.

## 2. Parent problem before / after

### Original problem before this run

Salez Problem 2.3 was `OPEN`. Positive scope available in the literature/repository included Ramanujan and long-range expanders, pre-entropic weakenings of LRE, historical Cartesian and synchronous tensor products, line graphs, finite lexicographic/twisted extensions, NM13-01 truncations, and P26 same-vertex graph squares.

### Original problem after this run

Salez Problem 2.3 remains `OPEN`. The proved source-compatible scope is enlarged by the following class.

> **Strong-product class.** Let `(G_n)` be a fixed-degree vertex-transitive `c`-long-range-expander sequence with a uniform lower spectral edge. Then the strong squares `H_n=G_n\boxtimes G_n`, equipped with their own rate-one continuous-time SRW, are bounded-degree vertex-transitive spectral expanders, fail every fixed long-range-expansion constant, and exhibit total-variation cutoff with an explicit `O(sqrt(log |V(H_n)|))` window.

For a `d`-regular base of size `n`, `q=d-1`, the cutoff center is

\[
\boxed{
T_n=
\frac{d(d+2)}{(d+1)(d-2)}\log_q n
=
\frac{d(d+2)}{2(d+1)(d-2)}\log_q |V(H_n)|.
}
\tag{2.1}
\]

Nonbipartite fixed-degree Ramanujan Cayley families give explicit source-valid examples.

This is a theorem-scope gain. It does not close the parent conjecture.

## 3. Strong graph squares

Let `G=(V,E)` be a finite connected simple `d`-regular graph, `d>=3`, and write `P=A/d` for SRW on `G`.

The **strong square** `H=G\boxtimes G` has vertex set `V^2`; distinct `(x_1,x_2)` and `(y_1,y_2)` are adjacent iff in each coordinate the entries are equal or adjacent in `G`, and at least one coordinate changes.

Its adjacency matrix is

\[
A_H=A\otimes I+I\otimes A+A\otimes A.
\tag{3.1}
\]

Hence its degree is

\[
D=2d+d^2=d(d+2).
\tag{3.2}
\]

Put

\[
\alpha=\frac1{d+2},\qquad
\beta=\frac d{d+2},\qquad
 a=\alpha+\beta=\frac{d+1}{d+2}.
\tag{3.3}
\]

Then the discrete SRW kernel on `H` is exactly

\[
\boxed{
Q=\alpha(P\otimes I)+\alpha(I\otimes P)+\beta(P\otimes P).
}
\tag{3.4}
\]

Thus one rate-one jump chooses one of three types:

* first coordinate only, probability `alpha`;
* second coordinate only, probability `alpha`;
* both coordinates, probability `beta`.

In a both-coordinate jump the two chosen base neighbors are independent and uniform.

If `G` is vertex-transitive, `H` is vertex-transitive under the coordinatewise automorphism action. If `G` is Cayley, then `H` is Cayley on the direct-product group.

## 4. Spectral expansion of the strong square

Assume the one-sided base gap satisfies

\[
1-\lambda_2(P)\ge\gamma>0.
\tag{4.1}
\]

### Proposition 4.1

The one-sided spectral gap of `H` satisfies

\[
\boxed{
\operatorname{gap}(H)\ge\frac{\gamma}{d+2}.
}
\tag{4.2}
\]

### Proof

Let `E_K` denote the Dirichlet form of a reversible kernel `K` with respect to uniform measure on `V^2`. From (3.4),

\[
\mathcal E_Q
=
\alpha\mathcal E_{P\otimes I}
+
\alpha\mathcal E_{I\otimes P}
+
\beta\mathcal E_{P\otimes P}.
\tag{4.3}
\]

The last term is nonnegative. Let

\[
R=\frac12(P\otimes I+I\otimes P).
\]

Its eigenvalues are `(lambda_i+lambda_j)/2`, so its second eigenvalue is at most `(1+lambda_2(P))/2`; therefore

\[
\operatorname{gap}(R)\ge\gamma/2.
\]

Since

\[
\mathcal E_{P\otimes I}+
\mathcal E_{I\otimes P}=2\mathcal E_R,
\]

we obtain

\[
\mathcal E_Q(f,f)
\ge \alpha\gamma\operatorname{Var}(f)
=\frac{\gamma}{d+2}\operatorname{Var}(f).
\]

This proves (4.2). `QED`

So every fixed-degree strong square of a spectral-expander sequence is again a spectral-expander sequence.

## 5. Strong squares are quantitatively outside long-range expansion

The strong-product metric is exactly

\[
d_H((x_1,x_2),(y_1,y_2))
=
\max\{d_G(x_1,y_1),d_G(x_2,y_2)\}.
\tag{5.1}
\]

Consequently

\[
B_H((x_1,x_2),r)
=B_G(x_1,r)\times B_G(x_2,r).
\tag{5.2}
\]

For every `d`-regular graph and `q=d-1`, the universal-tree bound gives

\[
|B_G(x,r)|\le C_d q^r.
\tag{5.3}
\]

Therefore

\[
|B_H(z,r)|\le C_d^2 q^{2r}.
\tag{5.4}
\]

But `H` has degree `D=d^2+2d`, so the tree branching benchmark in the LRE definition is

\[
Q_H=D-1=d^2+2d-1.
\]

Since

\[
q^2=(d-1)^2<d^2+2d-1=Q_H,
\tag{5.5}
\]

choose

\[
r_n=\left\lfloor\frac12\log_{Q_H}|V(H_n)|\right\rfloor.
\]

Then `Q_H^{r_n}` is of order `|V(H_n)|^{1/2}`, safely below the macroscopic saturation range in the LRE singleton test, but

\[
\frac{|B_{H_n}(z,r_n)|}{Q_H^{r_n}}
\le C_d^2
\left(\frac{q^2}{Q_H}\right)^{r_n}
\longrightarrow0.
\tag{5.6}
\]

Thus no fixed positive LRE constant can hold for the strong-square sequence. This is a strict source-scope extension beyond Altschuler's theorem, not a relabeling of LRE.

## 6. Main strong-product cutoff theorem

Let `(G_n)` be a sequence of `d`-regular vertex-transitive `c`-long-range expanders, with fixed `d,c`, `n=|V(G_n)|->infinity`. Assume also a uniform lower spectral edge

\[
\lambda_{\min}(P_n)\ge-1+\eta
\tag{6.1}
\]

for some fixed `eta>0`. This is exactly the extra periodicity exclusion in Altschuler's discrete-time Gaussian-profile theorem and is satisfied, for example, by nonbipartite fixed-degree Ramanujan families.

Set

\[
q=d-1,\qquad
L_n=\log_q n,\qquad
v=\frac{d-2}{d},\qquad
\tau_n=\frac{L_n}{v}=\frac d{d-2}L_n.
\tag{6.2}
\]

Let `H_n=G_n\boxtimes G_n` and let `D_n(t)` denote worst-start TV distance for **rate-one continuous-time SRW on `H_n`**.

### Theorem 6.1 — strong-product cutoff

With `a=(d+1)/(d+2)`, put

\[
T_n=\frac{\tau_n}{a}
=\frac{d(d+2)}{(d+1)(d-2)}L_n.
\tag{6.3}
\]

Then

\[
\lim_{c\to\infty}\limsup_{n\to\infty}
D_n(T_n+c\sqrt{L_n})=0,
\tag{6.4}
\]

and

\[
\lim_{c\to\infty}\liminf_{n\to\infty}
D_n(T_n-c\sqrt{L_n})=1.
\tag{6.5}
\]

Hence `(H_n)` has total-variation cutoff in Salez's continuous-time convention, at center (6.3), with window `O(sqrt(log n))=O(sqrt(log |V(H_n)|))`.

### Proof: upper side

Poisson-thin the rate-one jump process according to the three types in Section 3. Let

\[
N_{10}\sim\operatorname{Pois}(\alpha t),\quad
N_{01}\sim\operatorname{Pois}(\alpha t),\quad
N_{11}\sim\operatorname{Pois}(\beta t)
\]

be independent. The total numbers of base steps taken by the two coordinates are

\[
K_1=N_{10}+N_{11},\qquad
K_2=N_{01}+N_{11}.
\tag{6.6}
\]

Thus each marginal is

\[
K_i\sim\operatorname{Pois}(at),
\tag{6.7}
\]

although `K_1,K_2` are correlated through `N_{11}`.

Conditional on the three counts, all base-neighbor labels are independent, including the two labels at a simultaneous move. Hence from `(x_1,x_2)` the conditional endpoint law is exactly

\[
P_n^{K_1}(x_1,\cdot)\otimes P_n^{K_2}(x_2,\cdot).
\tag{6.8}
\]

Let

\[
d_n(k)=\max_x\|P_n^k(x,\cdot)-\pi_n\|_{\rm TV}.
\]

For product laws,

\[
\|\mu_1\otimes\mu_2-\nu_1\otimes\nu_2\|_{\rm TV}
\le
\|\mu_1-\nu_1\|_{\rm TV}
+
\|\mu_2-\nu_2\|_{\rm TV}.
\tag{6.9}
\]

Fix `c>0` and take

\[
t=T_n+c\sqrt{L_n}.
\]

Then

\[
at=\tau_n+ac\sqrt{L_n}.
\]

Set

\[
m_n=\left\lfloor\tau_n+\frac{ac}{2}\sqrt{L_n}\right\rfloor.
\]

Since `Var(K_i)=at=Theta(L_n)`, Chebyshev already gives

\[
\Pr(K_i<m_n)\le \frac{C_d}{c^2}+o(1)
\tag{6.10}
\]

for a degree-dependent constant `C_d`.

Discrete-time TV is nonincreasing under further Markov steps. Therefore (6.8)--(6.10) and convexity imply

\[
D_n(t)
\le
\Pr(K_1<m_n\ \text{or}\ K_2<m_n)
+2d_n(m_n)
\le
\frac{2C_d}{c^2}+2d_n(m_n)+o(1).
\tag{6.11}
\]

Altschuler's Theorem 1.12 gives the Gaussian cutoff profile for the base LRE sequence at `tau_n` with window `Theta(sqrt(L_n))`, uniformly in the start. Consequently

\[
\lim_{c\to\infty}\limsup_{n\to\infty}d_n(m_n)=0.
\]

Equation (6.11) proves (6.4).

### Proof: lower side

Project `H_n` onto its first coordinate. At a global jump the first coordinate moves with probability

\[
a=\alpha+\beta=\frac{d+1}{d+2}
\]

and otherwise stays. Hence its continuous-time generator is exactly

\[
a(P_n-I).
\tag{6.12}
\]

So at strong-product time `t`, the first-coordinate marginal is rate-one base SRW run for time `at`. Projection contracts total variation, hence

\[
D_n(t)\ge d_n^{\rm ct}(at).
\tag{6.13}
\]

Take

\[
t=T_n-c\sqrt{L_n},\qquad
s=at=\tau_n-ac\sqrt{L_n}.
\]

Lift the base continuous-time walk to the infinite `d`-regular tree. Let `R_s` be its distance from the root. For the embedded discrete radial walk, away from zero the `+1/-1` probabilities are `q/d` and `1/d`, so the drift is `v=(d-2)/d`. If `N_s~Pois(s)` is the number of jumps, the standard reflected-walk decomposition is

\[
R_s=vN_s+(1-v)L_{N_s}+M_{N_s},
\tag{6.14}
\]

where `M` is a bounded-increment martingale and `L` counts visits to the root. Starting from radius one, the return probability is `1/q`, so `L_\infty` has an exponential tail. Since `N_s-s=O_P(sqrt(s))` and `M_{N_s}=O_P(sqrt(s))`, (6.14) gives, quantitatively,

\[
R_s=vs+O_P(\sqrt{s})
=L_n-avc\sqrt{L_n}+O_P(\sqrt{L_n}).
\tag{6.15}
\]

For

\[
r_n=\left\lfloor L_n-\frac{avc}{2}\sqrt{L_n}\right\rfloor,
\]

Chebyshev/Azuma applied to (6.14) yields

\[
\lim_{c\to\infty}\liminf_{n\to\infty}\Pr(R_s\le r_n)=1.
\tag{6.16}
\]

Whenever `R_s\le r_n`, the projected finite-graph walk lies in `B_{G_n}(x,r_n)`. By the universal degree bound,

\[
\pi_n(B_{G_n}(x,r_n))
\le C_d\frac{q^{r_n}}n
\le C_d q^{-(avc/2)\sqrt{L_n}+O(1)}
\longrightarrow0.
\tag{6.17}
\]

Thus the first-coordinate TV distance tends to one on the early side, first `n->infinity` and then `c->infinity`. Equations (6.13)--(6.17) prove (6.5). `QED`

### Explicit nonempty family

Take any fixed-degree nonbipartite vertex-transitive Ramanujan Cayley sequence with a uniform lower spectral edge, for example a suitable LPS-type subfamily. Altschuler proves Ramanujan implies LRE. The strong squares are Cayley graphs on the direct-product groups, have fixed degree `d^2+2d`, have uniform gap by Proposition 4.1, fail LRE by Section 5, and satisfy Theorem 6.1.

## 7. Removing the previous orbit-collision obstruction

The preceding NM13-01 report left the following mechanism-level target:

> construct an automorphism-orbit-averaged NBRW collision/Green kernel whose estimate is independent of directed-edge orbit bookkeeping.

For **marginal NBRW endpoint entropy**, vertex transitivity makes this exact and scalar.

Let `G` now be any finite simple `d`-regular graph, `d>=3`, with adjacency matrix `A`, normalized SRW matrix `P=A/d`, and `q=d-1`.

Let `M_r(x,y)` be the number of nonbacktracking paths of length `r` from `x` to `y`. Then

\[
M_1=A,
\qquad
M_2=A^2-dI,
\tag{7.1}
\]

and for `r>=3`,

\[
M_r=A M_{r-1}-q M_{r-2}.
\tag{7.2}
\]

The normalized NBRW endpoint kernel is

\[
K_r=\frac{M_r}{d q^{r-1}}.
\tag{7.3}
\]

Define polynomials `p_r` by

\[
p_1(z)=z,
\qquad
p_2(z)=\frac{d z^2-1}{q},
\tag{7.4}
\]

and for `r>=3`,

\[
p_r(z)=\frac d q z p_{r-1}(z)-\frac1q p_{r-2}(z).
\tag{7.5}
\]

Then (7.1)--(7.3) give the exact identity

\[
\boxed{K_r=p_r(P).}
\tag{7.6}
\]

### Theorem 7.1 — exact transitive collision trace

Assume `G` is vertex-transitive on `n` vertices. Let

\[
1=\lambda_1,\lambda_2,\ldots,\lambda_n
\]

be the eigenvalues of `P`. Then for every start `x` and every `r>=1`,

\[
\boxed{
\chi^2(K_r(x,\cdot)\|\pi)
=
\sum_{i=2}^n p_r(\lambda_i)^2.
}
\tag{7.7}
\]

Consequently

\[
\boxed{
H(K_r(x,\cdot))
\ge
\log n-
\log\!\left(1+\sum_{i=2}^n p_r(\lambda_i)^2\right).
}
\tag{7.8}
\]

Both quantities are independent of `x`.

### Proof

Because `K_r` is a real polynomial in the symmetric matrix `P`, it is symmetric. Therefore

\[
\sum_y K_r(x,y)^2=(K_r^2)(x,x).
\tag{7.9}
\]

Vertex transitivity implies that every diagonal entry of `K_r^2`, itself an automorphism-invariant polynomial in `P`, is equal. Hence

\[
(K_r^2)(x,x)=\frac1n\operatorname{tr}(K_r^2).
\tag{7.10}
\]

Since `pi=1/n`,

\[
\chi^2(K_r(x,\cdot)\|\pi)
=n\sum_yK_r(x,y)^2-1
=\operatorname{tr}(K_r^2)-1.
\tag{7.11}
\]

Diagonalizing `P` and using `p_r(1)=1` gives

\[
\operatorname{tr}(K_r^2)-1
=
\sum_{i=2}^n p_r(\lambda_i)^2,
\]

which is (7.7).

For any law `mu` on an `n`-point uniform space,

\[
D(\mu\|\pi)
=\mathbb E_\mu\log(n\mu(Y))
\le
\log\mathbb E_\mu[n\mu(Y)]
=
\log(1+\chi^2(\mu\|\pi))
\tag{7.12}
\]

by Jensen. Since `D(mu||pi)=log n-H(mu)`, equations (7.7) and (7.12) give (7.8). `QED`

### Interpretation

No arc transitivity, edge transitivity, or directed-edge orbit Markov chain is needed for the **marginal** collision estimate. Vertex transitivity alone turns the worst-start collision problem into the global adjacency-spectral statistic

\[
\mathcal C_r(G):=\sum_{i=2}^n p_r(\lambda_i)^2.
\tag{7.13}
\]

Equivalently,

\[
1+\mathcal C_r(G)
=n\Pr(Y_r=Y_r'),
\]

where `Y_r,Y_r'` are independent NBRWs started from the same vertex. This is the desired orbit-averaged collision kernel, with no orbit bookkeeping left.

## 8. A complete transitivity-specific spectral-trace cutoff criterion

The trace identity is not merely descriptive; combined with Salez-continuous-time entropy cleanup it yields a full sufficient theorem.

Let `(G_n)` be `d`-regular vertex-transitive graphs, fixed `d>=3`, with

\[
1-\lambda_2(P_n)\ge\gamma>0.
\tag{8.1}
\]

Put `q=d-1` and

\[
j_n=\min\{j>=1:dq^{j-1}\ge n\}.
\tag{8.2}
\]

Thus `j_n=log_q n+O_d(1)`.

### Theorem 8.1 — NBRW spectral-trace criterion

Assume that for some fixed `A<infinity`, uniformly for every `r>=j_n`,

\[
\boxed{
\sum_{i=2}^n p_r(\lambda_i(P_n))^2
\le(\log n)^A.
}
\tag{8.3}
\]

Then rate-one continuous-time SRW on `(G_n)` has total-variation cutoff at

\[
\boxed{
\frac d{d-2}\log_{d-1}n
}
\tag{8.4}
\]

with window `O(sqrt(log n))`.

### Proof

By Theorem 7.1, every NBRW shell law `K_r(x,.)`, `r>=j_n`, has relative-entropy deficit at most

\[
a_n:=A\log\log n+O(1).
\tag{8.5}
\]

We first record the continuous-time cleanup estimate. Let `H_s=e^{s(P_n-I)}`. For any initial law `mu`, entropy dissipation and the pointwise inequality

\[
(a-b)(\log a-\log b)
\ge4(\sqrt a-\sqrt b)^2
\]

give

\[
-\frac d{ds}D(\mu H_s\|\pi)
\ge4\gamma\operatorname{Var}_\pi\sqrt{d(\mu H_s)/d\pi}.
\tag{8.6}
\]

Hellinger/TV comparison gives

\[
\|\mu H_s-\pi\|_{\rm TV}^2
\le
\operatorname{Var}_\pi\sqrt{d(\mu H_s)/d\pi}.
\tag{8.7}
\]

TV is nonincreasing in time. Integrating (8.6) from `0` to `s` and using (8.7) yields

\[
\boxed{
\|\mu H_s-\pi\|_{\rm TV}
\le
\sqrt{\frac{D(\mu\|\pi)}{4\gamma s}}.
}
\tag{8.8}
\]

Choose

\[
s_n=(\log\log n)^2=o(\sqrt{\log n}).
\tag{8.9}
\]

Lift continuous-time SRW to the infinite `d`-regular tree and let `R_t` be tree distance from the root. Root symmetry gives the exact shell mixture

\[
\delta_xH_t
=
\sum_{r>=0}\Pr(R_t=r)K_r(x,\cdot).
\tag{8.10}
\]

Run first for `t-s_n` and then for `s_n`. Every shell with `r>=j_n` has entropy deficit at most `a_n`, so (8.8), (8.9), and convexity give

\[
\|\delta_xH_t-\pi\|_{\rm TV}
\le
\Pr(R_{t-s_n}<j_n)
+O\!\left((\log\log n)^{-1/2}\right).
\tag{8.11}
\]

The same reflected-tree decomposition as (6.14) gives

\[
R_t=vt+O_P(\sqrt t),
\qquad v=(d-2)/d,
\tag{8.12}
\]

with constants depending only on `d`. Taking

\[
t=\frac1v\log_q n+c\sqrt{\log n}
\]

in (8.11) shows that the upper TV distance tends to zero as first `n->infinity` and then `c->infinity`.

For the lower side take

\[
t=\frac1v\log_q n-c\sqrt{\log n}
\]

and

\[
r_n=\left\lfloor\log_q n-\frac{vc}{2}\sqrt{\log_q n}\right\rfloor.
\]

By (8.12), `Pr(R_t<=r_n)` tends to one as `c->infinity`, uniformly in large `n`. The projected finite walk is then inside a ball of stationary mass at most

\[
C_d q^{r_n}/n=o(1).
\]

Therefore TV tends to one on the early side. This proves cutoff at (8.4) with `O(sqrt(log n))` window. `QED`

### What obstruction has actually been removed?

Before this run, a plausible route was blocked by the need to control separate directed-edge orbit sectors and then average their collisions. Theorem 7.1 shows that for the marginal NBRW endpoint distribution this is unnecessary: **vertex transitivity itself performs the averaging exactly**. The full entropy obligation is now the scalar spectral trace (8.3).

This does **not** prove (8.3) from an ordinary spectral gap. The naive bound

\[
\mathcal C_r(G)
\le n\max_{i>=2}|p_r(\lambda_i)|^2
\]

is generally too crude at the entropic radius. The remaining general-conjecture obstruction is therefore sharply localized:

> control the **empirical spectral mass** through the nonbacktracking polynomials at the entropic radius, using vertex transitivity plus expansion, rather than controlling the worst eigenvalue or demanding ambient tree-rate volume growth.

This is complementary to P26's entropy/Green-function work: P26 controls shell entropy by geometric/Green transfer, whereas (7.7)--(8.3) convert the transitive marginal collision problem into an exact spectral-trace statistic.

## 9. Sanity checks actually executed

A pure-Python exact-rational checker was executed and archived:

`proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/2026-09-20T03-03-00Z__strong_product_nbrw_exact.py`

Output:

`proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/2026-09-20T03-03-00Z__strong_product_nbrw_exact.out`

It verifies exactly:

1. on `K_4`, the strong-product kernel identity (3.4), degree `D=15`, and coordinate generator rate `a=4/5`;
2. the strict branching separation `(d-1)^2 < D-1` (`4<14` for `d=3`);
3. on `K_4` and `K_{3,3}`, the identity
   \[
   n\sum_yK_r(x,y)^2-1=\operatorname{tr}(K_r^2)-1
   \]
   for `r=1,...,6`, using exact fractions.

Terminal marker:

`ALL_EXACT_CHECKS_PASS`.

These finite checks are sanity checks only; the asymptotic theorems are proved analytically above.

## 10. Failed/cleared routes and next attack

### Cleared as duplication

* Fixed Cartesian products: already proved historically in R16 and standard product-chain theory.
* Synchronous direct/tensor squares: already proved historically in R16.
* Same-vertex graph squares: current P26 route.
* Fixed fibers / twisted finite extensions: already handled by P26/NM13-01.

### Current remaining obstruction

The parent conjecture still requires a mechanism that works for an arbitrary bounded-degree vertex-transitive spectral expander. Theorem 8.1 reduces one concrete route to (8.3), but no proof here shows that an ordinary gap forces that polylogarithmic trace.

### Next mathematically distinct attack

Study

\[
\mathcal C_r(G)=\sum_{i=2}^n p_r(\lambda_i)^2
\]

through **transitivity-constrained empirical spectral measures**, not the extremal eigenvalue. The immediate target is a moment/return-probability inequality showing that spectral mass outside the tree interval can only contribute `polylog(n)` to `C_{j_n}` under an additional source-natural transitivity condition strictly weaker than LRE; failing that, construct a transitive expander family showing (8.3) can fail despite cutoff, which would decisively redirect the general route.

## 11. Compact ledger delta

A machine-readable ledger delta for this run is saved at

`proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/2026-09-20T03-03-00Z__ledger_delta.json`.

Summary:

* source before/after: `OPEN -> OPEN`;
* theorem-scope movement: **yes**, strong-product non-LRE transitive expander class with explicit center and square-root window;
* mechanism movement: **yes**, exact vertex-transitive NBRW collision trace plus a complete spectral-trace cutoff criterion;
* finite experiments promoted to asymptotic theorem: **no**;
* publication novelty: `UNVERIFIED`;
* peer/audit status: not waited on; restricted theorems are `CANDIDATE_FULL` pending later independent review.
