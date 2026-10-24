Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6/maximum was requested, but authenticated runtime metadata does not establish that setting, so I do not claim it.

# P26 / LIVE20 T08 — graph-square shell-entropy transfer and non-LRE Cayley cutoff family

**Status:** `CANDIDATE_FULL` for the restricted transfer theorem and graph-square application proved below, pending later independent review; **PARTIAL / OPEN** for Salez Problem 2.3. Worldwide publication novelty is **UNVERIFIED**.

Repository/branch: `yspennstate/math-open-problems` / `master`.
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.
Report root: `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/`.
Fresh pre-report master observed after the two sanity-check artifact commits: `5efba4da8f75c59b26aa58b4eeff6f188b8f1dda`.

## 0. Compact handoff and coordination with historical C28

The preceding P26 T08 runs established two exact local transfer mechanisms.

1. **Line graphs.**  An incidence intertwining transfers the rate-one continuous-time walk on a line graph to the base walk at a deterministic time scale and gives an exact TV sandwich.  This yielded a vertex-transitive spectral-expander cutoff class outside long-range expansion.
2. **Finite equal fibers / lexicographic blow-ups.**  For `X=G o F` with fixed regular fiber, P26 proved an exact semigroup decomposition, entropy chain rule, and
   `d_G(a t) <= d_X(t) <= d_G(a t)+exp(-a t)`.  Applying it to a cubic Ramanujan base gave a 7-regular vertex-transitive non-LRE cutoff family.

The LIVE20 successor of historical C28 is `NM13-01`.  I read its newest substantive report,

`proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/2026-09-20T01-22-00Z__truncation-arc-radial-cutoff.md`

(blob `2873709009a74df48f803bbcdf963628c54bfc96`, creation commit `b7f710b5c4982e2dce39de9bab2f4b9f74563cb5`).  NM13-01 has now moved beyond the line-graph overlap and proved cutoff for **non-lumpable truncation/replacement-product graphs** using persistent port memory, a two-state radial Markov-additive process, and arc-transitivity to synchronize directed NBRW sectors.  Its recorded next route is finitely many directed-edge orbit types.

Accordingly P26 does **not** continue finite fibers, line graphs, or port-memory truncations here.  The complementary route in this run keeps the **same vertex set** and changes the jump geometry: take the ordinary graph square and transfer NBRW shell entropy through an exact covering-tree shell decomposition.  There are no fibers, quotient variables, or port states.

I also read the current PROB10-08 pre-entropic-LRE report.  It proves that Altschuler's entropy mechanism only needs tree-rate growth up to `n exp(-rho_n)`, and it explicitly refutes deriving such maximal tree-rate growth from transitivity plus spectral expansion by the two-copy expander obstruction.  The route below therefore does not attempt that false implication.

## 1. Exact source convention and current literature boundary

Justin Salez, *Modern aspects of Markov chains: entropy, curvature and the cutoff phenomenon*, arXiv:2508.21055v1 (28 August 2025), defines the continuous-time chain from a stochastic matrix `P` by independent mean-one exponential holding times:

\[
H_t=e^{t(P-I)}
=e^{-t}\sum_{k\ge0}\frac{t^kP^k}{k!}.
\tag{1.1}
\]

Problem 2.3 states literally:

> Prove that all vertex-transitive expanders exhibit cutoff.

Here an expander sequence has diverging size, uniformly bounded degree, and spectral gap bounded away from zero.

Two newer exact-scope results remain important.

* Dylan J. Altschuler, arXiv:2609.14945v1, submitted 14 September 2026, proves cutoff with an explicit Gaussian profile for every fixed-degree **long-range expander** sequence.  The same paper proves the strict hierarchy
  \[
  \text{Ramanujan}\Longrightarrow\text{long-range expansion}
  \Longrightarrow\text{spectral expansion},
  \]
  with neither converse.  Thus long-range expansion is not a synonym for the source hypothesis.
* Francesco Pedrotti--Justin Salez, arXiv:2607.05345 (July 2026), prove that replacing the equilibrium Poincare constant by their non-equilibrium constant `gamma_*` gives a universal window bound `O(1/gamma_*)` under their standard regularity assumptions.  This does not presently supply a lower bound on `gamma_*` from vertex transitivity plus spectral expansion alone.

The only Altschuler input needed below is Proposition 3.1: for a fixed-degree fixed-`c` long-range expander `G` on `n` vertices, if `K_j(x,.)` is the endpoint law of length-`j` NBRW and

\[
j_n:=\min\{j\ge1:d(d-1)^{j-1}\ge n\},
\tag{1.2}
\]

then, uniformly in `x` and all `j>=j_n`,

\[
H(K_j(x,\cdot))\ge \log n-C_{d,c}\log\log n.
\tag{1.3}
\]

### Bounded prior-art check, 20 September 2026

I searched current indexed material for combinations of `graph square random walk cutoff`, `graph power random walk cutoff expander`, `distance-2 random walk cutoff`, and `square of Ramanujan graph random walk mixing`.  I recovered graph-power expansion work (notably Kwok--Lau, APPROX/RANDOM 2014) and standard graph-power references, but no theorem matching the exact continuous-time graph-square cutoff/shell-entropy transfer below.  This is only bounded negative evidence.  It is **not** a priority certificate, so worldwide novelty remains UNVERIFIED.

For the concrete application I use the classical Lubotzky--Phillips--Sarnak Ramanujan Cayley graphs.  Their published family has fixed degree `d=p+1`, Ramanujan spectrum, and girth asymptotically at least `(4/3) log_{d-1} n`; in particular, for every fixed degree in the family, the girth eventually exceeds four.  Altschuler's 2026 theorem makes every Ramanujan graph long-range expanding.

## 2. Parent-problem before / after

### Parent problem before this run

Salez Problem 2.3 was OPEN.  Current positive classes in the repository/literature included Ramanujan and long-range expanders, a pre-entropic weakening of LRE, line-graph transfer families, finite lexicographic blow-ups, and NM13-01 truncation/replacement-product families.  Those local constructions already show that output long-range expansion is not necessary for cutoff, but all of P26's own mechanisms so far used a nontrivial auxiliary local state or fiber.

### Parent problem after this run

Salez Problem 2.3 remains OPEN.  The proved source-compatible scope is enlarged by the following same-vertex, finite-range class.

> **Graph-square theorem.**  Let `(G_n)` be fixed-degree vertex-transitive graphs with girth at least five, uniform one-sided spectral gap, and an NBRW endpoint-entropy front of deficit `a_n=o(sqrt(log n))` at the tree entropic radius.  Then the ordinary graph squares `X_n=G_n^2`, equipped with their own rate-one continuous-time SRW, exhibit cutoff with an `O(sqrt(log n))` window at an explicit center.  If the bases are fixed-constant long-range expanders, Altschuler gives `a_n=O(log log n)`.

Applied to any fixed-degree LPS Ramanujan Cayley family, this gives vertex-transitive spectral expanders `G_n^2` which are **provably not long-range expanders** yet have cutoff.  For the degree-six LPS family, the outputs are 36-regular Cayley graphs and the center is

\[
\frac{9}{13}\log_5 n,
\]

with window `O(sqrt(log n))`.

This is a source-level class extension, not a checker count or auxiliary estimate.

## 3. A quantitative shell-entropy transfer criterion

The first new theorem is independent of graph squares.

Let `X` be a finite regular graph on `n` vertices, `Q` its discrete SRW kernel, `pi` uniform, and

\[
H_t=e^{t(Q-I)}.
\]

Assume its one-sided spectral gap is at least `eta>0`.  Suppose a walk started at `x` admits, at some time `t`, a convex shell decomposition

\[
\delta_xH_t=\sum_{r\ge0}p_t(r)\nu_r,
\tag{3.1}
\]

where the probability weights `p_t(r)` come from a radial process `R_t`.  Suppose further that for some threshold `L` and entropy deficit `a`,

\[
D(\nu_r\|\pi)\le a\qquad(r\ge L).
\tag{3.2}
\]

### Lemma 3.1 — entropy cleanup at a spectral gap

For any probability law `mu` on a finite regular reversible chain of gap at least `eta`,

\[
\boxed{
\|\mu H_s-\pi\|_{TV}
\le \sqrt{\frac{D(\mu\|\pi)}{4\eta s}}
\qquad(s>0).
}
\tag{3.3}
\]

#### Proof

Write `f_u=d(mu H_u)/d pi`.  Entropy dissipation gives

\[
-\frac d{du}D(\mu H_u\|\pi)
=\mathcal E_Q(f_u,\log f_u).
\]

The pointwise inequality

\[
(a-b)(\log a-\log b)\ge4(\sqrt a-\sqrt b)^2
\]

and Poincare imply

\[
\mathcal E_Q(f_u,\log f_u)
\ge4\eta\operatorname{Var}_\pi(\sqrt{f_u}).
\]

Also, by Cauchy--Schwarz,

\[
\|\mu H_u-\pi\|_{TV}^2
\le\operatorname{Var}_\pi(\sqrt{f_u}).
\]

Total variation is nonincreasing under `H_u`; integrating from `0` to `s` yields

\[
D(\mu\|\pi)
\ge4\eta s\,\|\mu H_s-\pi\|_{TV}^2.
\]

This is (3.3).  `QED`

### Theorem 3.2 — shell-entropy transfer

Under (3.1)--(3.2), for every `s>0`,

\[
\boxed{
\|\delta_xH_{t+s}-\pi\|_{TV}
\le
\Pr(R_t<L)+\sqrt{\frac{a}{4\eta s}}.
}
\tag{3.4}
\]

#### Proof

Run the chain for time `t` and then time `s`.  For every good shell `r>=L`, Lemma 3.1 gives TV at most `sqrt(a/(4 eta s))`; every bad shell costs at most one.  Convexity of TV in the initial law gives (3.4).  `QED`

This criterion is useful exactly at the cutoff scale.  If the radial front crosses `L_n` around `T_n` in a window `w_n`, the chain has a uniform gap, and the shell entropy deficit is `a_n=o(w_n)`, choose any cleanup time

\[
a_n\ll s_n\ll w_n.
\tag{3.5}
\]

Then the entropy cleanup is invisible on the radial window.  Quantitatively, without taking an asymptotic intermediate scale, (3.4) says that fixed-precision mixing costs only an additional

\[
O_\varepsilon(a_n/\eta)
\tag{3.6}
\]

after the radial front.  Thus a radial window `w_n` transfers to a TV window `O(w_n+a_n/eta)`; in the application below `a_n=O(log log n)` and `w_n=Theta(sqrt(log n))`.

## 4. Graph squares: exact transition algebra

Let `G` be a connected simple `d`-regular graph, `d>=3`, with girth at least five.  Its ordinary graph square `X=G^2` has the same vertex set, and two distinct vertices are adjacent in `X` iff their `G`-distance is one or two.

The girth assumption has two consequences:

1. no distance-two vertex is already adjacent to the root (no triangles), and
2. every distance-two vertex has a unique length-two path from the root (no four-cycles).

Hence `X` is exactly `D=d^2` regular.

Let `A` be the adjacency matrix of `G` and `P=A/d` its SRW kernel.  Since `A^2` has diagonal `d`, zero on adjacent pairs, and value one exactly on distance-two pairs,

\[
A_X=A^2+A-dI.
\tag{4.1}
\]

Dividing by `d^2` gives the exact square-walk kernel

\[
\boxed{
Q=P^2+\frac1dP-\frac1dI.
}
\tag{4.2}
\]

Therefore in Salez's rate-one convention

\[
\boxed{
H_t^X
=\exp\{t(Q-I)\}
=\exp\{t(P^2-I)\}\,
 \exp\{(t/d)(P-I)\}.
}
\tag{4.3}
\]

The two factors commute because both are polynomials in `P`.  Equation (4.3) is not a mere time-rescaling of the base walk: the new process superposes a rate-one `P^2` clock and a rate-`1/d` `P` clock at generator level.

### 4.1 Spectral-gap transfer

If `lambda` is a normalized eigenvalue of `P`, then the corresponding `Q` eigenvalue is

\[
q(lambda)=lambda^2+\frac{lambda}{d}-\frac1d.
\tag{4.4}
\]

The key factorization is

\[
\boxed{
1-q(lambda)=(1-lambda)\left(1+lambda+\frac1d\right).
}
\tag{4.5}
\]

Suppose the one-sided base gap is `1-lambda_2(P)>=gamma`.  Every nonconstant eigenvalue lies in `[-1,1-gamma]`; hence

\[
1+lambda+\frac1d\ge\frac1d,
\]

and (4.5) gives

\[
\boxed{
\operatorname{gap}(G^2)\ge\frac\gamma d.
}
\tag{4.6}
\]

Notably, no lower bound away from `-1` is needed.  A bipartite base causes no problem: `lambda=-1` is sent to `1-2/d<1`.

If `G` is vertex-transitive then `G^2` is vertex-transitive, since every automorphism preserves graph distance.

## 5. Exact covering-tree shell representation

Let `T_d` be the `d`-regular tree.  Because `G` has girth at least five, the universal covering map `T_d -> G` induces a graph covering

\[
T_d^2\longrightarrow G^2.
\tag{5.1}
\]

Indeed, the neighbors of a tree vertex in `T_d^2` are its tree-distance-one and tree-distance-two vertices; girth at least five makes their images distinct and exhausts the distance-one/two neighbors of the image vertex in `G`.

Lift the rate-one continuous-time SRW on `X=G^2` to rate-one continuous-time SRW on `T_d^2`, start at a root `o`, and let

\[
R_t=d_{T_d}(o,Y_t).
\]

The root stabilizer in `Aut(T_d)` acts transitively on each sphere and preserves the `T_d^2` walk.  Therefore, conditional on `R_t=r`, the lifted endpoint is uniform on the ordinary tree sphere of radius `r`.

Projecting a uniform tree sphere of radius `r` to `G` is exactly the endpoint law `K_r^G(x,.)` of an ordinary length-`r` nonbacktracking walk on the base.  Consequently we have the exact identity

\[
\boxed{
\delta_xH_t^{G^2}
=\sum_{r\ge0}\Pr(R_t=r)K_r^G(x,\cdot).
}
\tag{5.2}
\]

This is the central transfer mechanism.  The graph-square walk has different local dynamics and a different radial speed from base SRW, but its conditional shell laws are **exactly the base NBRW endpoint laws** whose entropy Altschuler controls.

Combining (5.2), (4.6), and Theorem 3.2 gives an immediately reusable criterion.

### Corollary 5.1 — graph-square entropy criterion

Assume `G` has girth at least five and one-sided gap at least `gamma`.  If

\[
H(K_r^G(x,\cdot))\ge\log n-a
\qquad(x\in V,\ r\ge L),
\tag{5.3}
\]

then for all `t,s>0`,

\[
\boxed{
\max_x\|\delta_xH_{t+s}^{G^2}-\pi\|_{TV}
\le
\Pr(R_t<L)+
\sqrt{\frac{da}{4\gamma s}}.
}
\tag{5.4}
\]

No line-graph incidence map, finite fiber, quotient lumping, or arc-transitivity is used.

## 6. Radial speed and square-root concentration on `T_d^2`

For ordinary discrete SRW on `T_d^2`, when the current tree radius is at least two, the exact counts of possible radial increments are

\[
\begin{array}{c|ccccc}
\Delta R&-2&-1&0&+1&+2\\ \hline
\#&1&1&d-2&d-1&(d-1)^2.
\end{array}
\tag{6.1}
\]

The total is `d^2`.  Therefore the bulk radial drift per jump is

\[
\boxed{
v_d
=\frac{-2-1+(d-1)+2(d-1)^2}{d^2}
=\frac{(d-2)(2d+1)}{d^2}>0.
}
\tag{6.2}
\]

Since the continuous-time chain makes a rate-one Poisson number of jumps, `v_d` is also the macroscopic radial speed per unit continuous time.

The exact second moment of the bulk increment is

\[
\mathbb E\xi^2
=\frac{4d^2-7d+8}{d^2}.
\tag{6.3}
\]

For the cutoff-window theorem only concentration, rather than the full radial CLT, is needed.

### Lemma 6.1 — radial concentration

There are constants `C_d,c_d>0` such that, for `t` large and `A>=1`,

\[
\Pr\left(|R_t-v_dt|>A\sqrt t\right)
\le C_de^{-c_dA^2}+C_de^{-c_dA\sqrt t}.
\tag{6.4}
\]

#### Proof

For the discrete jump chain write

\[
m(r)=\mathbb E[R_{k+1}-R_k\mid R_k=r].
\]

By (6.1), `m(r)=v_d` for every `r>=2`.  Hence

\[
M_m:=R_m-\sum_{k<m}m(R_k)
\tag{6.5}
\]

is a martingale with bounded increments, while

\[
\sum_{k<m}(m(R_k)-v_d)
\tag{6.6}
\]

is supported only on visits to radii `0` and `1`.

Those boundary visits have an exponential tail.  To see this, let `xi` have the bulk increment law (6.1).  Since `E xi=v_d>0`, for some sufficiently small `theta>0`,

\[
\phi(theta):=\mathbb E e^{-\theta\xi}<1.
\]

Thus `e^{-theta R_m}` is a supermartingale while `R_m>=2`.  Starting from radius two and stopping on first entrance into `{0,1}`, optional stopping gives a return probability at most `e^{-theta}<1`.  From the finite boundary set `{0,1}` there is a fixed positive chance, depending only on `d`, to exit to radius at least two in boundedly many steps.  Consequently the number of boundary excursions, and their total length, have an exponential tail.

Azuma applied to (6.5), together with the exponential tail of (6.6), gives

\[
\Pr(|R_m-v_dm|>A\sqrt m)
\le C_de^{-c_dA^2}+C_de^{-c_dA\sqrt m}.
\]

Finally, if `N_t~Poi(t)` is the number of jumps by continuous time `t`, Poisson Chernoff bounds control `|N_t-t|` on the same square-root scale.  Substituting `m=N_t` gives (6.4).  `QED`

## 7. Cutoff theorem for graph squares of entropy-rich bases

Put

\[
q=d-1,
\qquad
L_n=\log_q n,
\qquad
T_n=\frac{L_n}{v_d}
=\frac{d^2}{(d-2)(2d+1)}\log_{d-1}n.
\tag{7.1}
\]

### Theorem 7.1 — graph-square cutoff transfer

Fix `d>=3`, `gamma>0`.  Let `(G_n)` be connected `d`-regular graphs with

1. girth at least five for all sufficiently large `n`;
2. one-sided spectral gap at least `gamma`;
3. for `j_n` from (1.2), a uniform NBRW entropy front
   \[
   H(K_j^{G_n}(x,\cdot))\ge\log n-a_n
   \qquad(x\in V(G_n),\ j\ge j_n),
   \tag{7.2}
   \]
   where
   \[
   a_n=o(\sqrt{\log n}).
   \tag{7.3}
   \]

Then the rate-one continuous-time SRW on `X_n=G_n^2` has total-variation cutoff at `T_n` with window `O(sqrt(log n))`.  More precisely, for every fixed `epsilon in (0,1)` there is `C_epsilon<infinity` such that

\[
\boxed{
|t_{mix}^{X_n}(\epsilon)-T_n|
\le C_\epsilon\sqrt{\log n}
}
\tag{7.4}
\]

for all sufficiently large `n`.

If the bases are vertex-transitive, so are the outputs.  If the bases are fixed-constant long-range expanders, Altschuler gives `a_n=O(log log n)`, so (7.3) holds.

#### Proof: upper side

Choose a deterministic cleanup scale `s_n` satisfying

\[
a_n\ll s_n\ll\sqrt{L_n}.
\tag{7.5}
\]

For Altschuler's `a_n=O(log log n)` one may take `s_n=(log log n)^2`.

At time

\[
t=T_n+A\sqrt{L_n},
\]

apply (5.4) to the first `t-s_n` units and then clean up for `s_n`.  Since `j_n=L_n+O_d(1)` and `s_n=o(sqrt(L_n))`, Lemma 6.1 gives, for every fixed sufficiently large `A`,

\[
\limsup_{n\to\infty}
\Pr(R_{t-s_n}<j_n)
\le C_de^{-c_dA^2}.
\tag{7.6}
\]

The entropy term in (5.4) is

\[
\sqrt{\frac{d a_n}{4\gamma s_n}}=o(1).
\tag{7.7}
\]

Hence

\[
\limsup_{n\to\infty}d_{X_n}(T_n+A\sqrt{L_n})
\le C_de^{-c_dA^2}.
\tag{7.8}
\]

Letting `A` grow gives the post-cutoff side and, for fixed `epsilon`, an upper mixing-time bound `T_n+O_epsilon(sqrt(L_n))`.

#### Proof: lower side

At

\[
t=T_n-A\sqrt{L_n},
\]

set

\[
r_n=\left\lfloor L_n-\frac{v_dA}{2}\sqrt{L_n}\right\rfloor.
\tag{7.9}
\]

The mean radial location is `v_dt=L_n-v_dA sqrt(L_n)`, so Lemma 6.1 yields

\[
\limsup_{n\to\infty}\Pr(R_t\ge r_n)
\le C_de^{-c_d'A^2}.
\tag{7.10}
\]

On `{R_t<r_n}`, the projected endpoint lies in the ordinary base ball `B_{G_n}(x,r_n)`.  The universal degree bound gives

\[
\pi(B_{G_n}(x,r_n))
\le C_d\frac{(d-1)^{r_n}}n
\le C_d(d-1)^{-(v_dA/2)\sqrt{L_n}+O_d(1)}
=o(1).
\tag{7.11}
\]

Therefore

\[
\liminf_{n\to\infty}d_{X_n}(T_n-A\sqrt{L_n})
\ge1-C_de^{-c_d'A^2}.
\tag{7.12}
\]

Letting `A` grow gives the pre-cutoff side and the lower half of (7.4).  Since `sqrt(log n)=o(log n)`, this is cutoff.  `QED`

## 8. The outputs are spectral expanders but not long-range expanders

The preceding theorem is not merely reapplying Altschuler to the output graphs.

Let `X_n=G_n^2`, so its degree is

\[
D=d^2.
\]

Every `X_n` step changes base distance by at most two.  Thus, for every vertex `x` and integer `r`,

\[
B_{X_n}(x,r)\subseteq B_{G_n}(x,2r),
\]

and hence

\[
|B_{X_n}(x,r)|
\le C_d(d-1)^{2r}.
\tag{8.1}
\]

On the other hand, a fixed-constant long-range expansion bound for the `D`-regular output, applied to a singleton before saturation, would demand order

\[
(D-1)^r=(d^2-1)^r.
\tag{8.2}
\]

But

\[
\frac{(d-1)^2}{d^2-1}
=\frac{d-1}{d+1}<1.
\tag{8.3}
\]

Take for example

\[
r_n=\left\lfloor\frac12\log_{d^2-1}n\right\rfloor.
\]

Then `(d^2-1)^{r_n}` is of order `sqrt(n)` and lies safely below saturation, whereas (8.1)--(8.3) imply

\[
\frac{|B_{X_n}(x,r_n)|}{(d^2-1)^{r_n}}
\le C_d\left(\frac{d-1}{d+1}\right)^{r_n}
\longrightarrow0.
\tag{8.4}
\]

Thus no uniform positive LRE constant exists for `(X_n)`.

At the same time (4.6) gives a fixed spectral gap.  This exhibits the distinction demanded by T08 in the strongest possible way inside the application: the output class is vertex-transitive and spectrally expanding, but it fails the long-range expansion hypothesis quantitatively.

## 9. Concrete new class: squares of LPS Ramanujan Cayley graphs

Take a fixed-degree Lubotzky--Phillips--Sarnak Ramanujan Cayley family `(G_n)`.  The classical construction gives fixed degree `d=p+1`, Ramanujan spectrum, and girth growing at least logarithmically (indeed asymptotically at least `(4/3)log_{d-1}n`).  Therefore for large `n` the girth is at least five.

Altschuler's September 2026 theorem gives fixed-constant long-range expansion for the base Ramanujan graphs, so Proposition 3.1 gives the entropy front (7.2) with

\[
a_n=O(\log\log n).
\]

All hypotheses of Theorem 7.1 hold.  The square graphs

\[
X_n=G_n^2
\]

have the following properties simultaneously:

* the **same vertex set** as `G_n`;
* fixed degree `d^2`;
* Cayley, hence vertex-transitive;
* a fixed one-sided spectral gap by (4.6);
* no fixed long-range expansion constant by Section 8;
* rate-one continuous-time cutoff at
  \[
  \frac{d^2}{(d-2)(2d+1)}\log_{d-1}n
  \]
  with window `O(sqrt(log n))`.

For the concrete LPS choice `p=5`, hence `d=6`, this becomes a family of **36-regular vertex-transitive Cayley spectral expanders**, outside long-range expansion, with bulk radial speed

\[
v_6=\frac{13}{9}
\]

and cutoff center

\[
\boxed{
T_n=\frac9{13}\log_5n
}
\tag{9.1}
\]

with `O(sqrt(log n))` window.

This class is structurally different from the existing P26 line graphs and lexicographic blow-ups and from NM13-01 truncations: the operation introduces no new vertices or local hidden state.  It changes the jump law on the original Cayley group by adjoining all base distance-two moves.

## 10. Essential executed sanity check

Before saving this report I executed an exact rational-arithmetic checker and archived both code and output.

Code:

`proofnet24/P26-progress-cutoff-transfer/artifacts/2026-09-20/2026-09-20_05-01-42__graph_square_transfer_checker.py`

creation commit:

`198630cb8e2d57e2451b49bf8755ff5582881976`.

Output:

`proofnet24/P26-progress-cutoff-transfer/artifacts/2026-09-20/2026-09-20_05-01-42__graph_square_transfer_checker.out`

creation commit:

`d1baf1103c741ce1a1010bd95e42d1e86f6ab620`.

The checker independently verifies:

* on the Petersen graph, `A_{G^2}=A^2+A-dI` exactly and `deg(G^2)=d^2`;
* for every `3<=d<=12`, the exact radial counts (6.1), drift
  `(d-2)(2d+1)/d^2`, and second moment `(4d^2-7d+8)/d^2`;
* the exact spectral factorization (4.5) over a rational grid;
* the strict branching mismatch `(d-1)^2<d^2-1`;
* the concrete `d=6` values `degree=36`, `v=13/9`, center multiplier `9/13`.

The archived output ends

`P26_T08_GRAPH_SQUARE_TRANSFER_EXACT_PASS`.

This finite checker is only a sanity check of the algebra; the asymptotic cutoff proof is Sections 3--9.

## 11. Mechanism-level advance, separated from parent-scope advance

The parent-scope advance is the new non-LRE transitive cutoff family in Section 9.

The mechanism-level advance is different and reusable:

1. **Shell entropy rather than quotient entropy.**  The exact decomposition (5.2) says a finite-range walk can inherit NBRW endpoint entropy even when it is not a quotient, lift, or deterministic time-change of base SRW.
2. **One-sided spectral transfer is exact.**  The polynomial identity (4.5) shows that graph squaring actually kills the bipartite `-1` obstruction and preserves a uniform one-sided gap with explicit factor `1/d`.
3. **Quantitative entropy-to-TV transfer.**  Theorem 3.2 turns shell KL deficit `a_n` into only `O(a_n/eta)` fixed-precision cleanup time.  When `a_n=o(sqrt(log n))`, the entropy cost disappears inside the natural radial `sqrt(log n)` window.
4. **Maximal local branching is unnecessary.**  The output branching base is `d^2-1`, while actual ball growth inherited from the base is at most `(d-1)^{2r}`.  The ratio decays exponentially in radius, yet cutoff survives.

This directly addresses the T08 distinction between spectral and long-range expansion: the proof uses long-range expansion only on an **ancestor/base** to manufacture shell entropy, then transfers that entropy to an output whose own geometry violates LRE.

## 12. Residual obstruction and failed-route history

The full Salez problem remains open.  The remaining obstruction is no longer local decoration: line graphs, lexicographic fibers, non-lumpable truncations, and now same-vertex distance-two rewiring all preserve cutoff under explicit hypotheses.

What is still missing is a theorem that creates an entropy-rich shell/front **directly from arbitrary vertex transitivity plus a spectral gap**, without assuming an LRE ancestor or a special finite-state radial model.  PROB10-08's two-copy obstruction shows that any route insisting on maximal tree-rate ball growth is too strong.

No recovery route failed in this run.  The graph-square route succeeded on its first substantive execution, so the PROGRESS20 forced-switch rule is not triggered.

## 13. Next attack

The next P26 attack is the natural same-vertex extension which remains complementary to NM13-01's finite-orbit port-memory program:

> Treat fixed graph powers `G^{<=m}` for `m>=3` under girth `>2m`.  Derive the exact distance-polynomial kernel, prove a uniform spectral-gap transfer from the base one-sided gap, compute the universal-tree radial drift, and show that the conditional radial shells remain ordinary NBRW endpoint laws.  If successful, this yields a finite-range isotropic transfer theorem rather than a one-off square construction.

A second, more source-directed step would then ask which finite-range isotropic walk kernels can be produced canonically from an arbitrary vertex-transitive spectral expander without invoking tree-rate volume growth.

## 14. ledger_delta

```text
parent: T08 / Salez arXiv:2508.21055 Problem 2.3
source_status_before: OPEN
source_status_after: OPEN / PARTIAL
source_closure_claim: none

mechanism_before:
  line-graph incidence transfer + finite equal-fiber/lexicographic transfer
mechanism_after:
  quantitative shell-entropy transfer + exact graph-square shell decomposition

new_restricted_theorem:
  input: d-regular girth>=5, one-sided gap>=gamma,
         NBRW entropy deficit a_n=o(sqrt(log n)) beyond j_n
  output: X_n=G_n^2, degree d^2
  output_gap: >= gamma/d
  cutoff_center: [d^2/((d-2)(2d+1))] log_{d-1} n
  cutoff_window: O(sqrt(log n))
  exact_continuous_time: H_t=exp(t(Q-I))

proved_application:
  base: fixed-degree LPS Ramanujan Cayley family
  output: graph squares, same vertex set
  properties: vertex-transitive, spectral expander, not LRE, cutoff
  concrete_d6_output_degree: 36
  concrete_d6_center: (9/13) log_5 n
  concrete_window: O(sqrt(log n))

companion_coordination:
  historical_C28_successor: NM13-01
  NM13-01_route: non-lumpable truncation / finite directed-edge orbit memory
  P26_route_this_run: same-vertex isotropic graph powers / shell entropy
  duplication: no

sanity_code_commit: 198630cb8e2d57e2451b49bf8755ff5582881976
sanity_output_commit: d1baf1103c741ce1a1010bd95e42d1e86f6ab620
worldwide_priority: UNVERIFIED
next_attack: fixed powers G^{<=m}, m>=3
```

End of complete P26 substantive T08 report.
