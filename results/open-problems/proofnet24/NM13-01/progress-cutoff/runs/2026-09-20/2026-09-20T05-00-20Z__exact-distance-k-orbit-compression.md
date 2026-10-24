Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** No authenticated runtime metadata establishes GPT-6 or a maximum-effort setting.

# NM13-01 / LIVE20 T08 — pure exact-distance-k cutoff and canonical stabilizer-orbit information compression

**Parent status:** `PARTIAL / OPEN` for Salez Problem 2.3.

**Restricted results in this report:** `CANDIDATE_FULL` pending later independent review.

**Publication novelty:** `UNVERIFIED`. The exact-distance-k theorem for `k>=3` and the way it is combined here with the transitivity quotient are new to the checked repository state. Bounded literature searches did not locate this exact cutoff theorem, but that is not a worldwide priority certificate. The orbit-lumping lemma itself is elementary representation/lumping folklore in spirit; no novelty claim is made for it.

Repository/branch: `yspennstate/math-open-problems` / `master`.
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.
Run root: `proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/`.
Pre-write master observed before this run's writes: `9270e2fb95326f9f340a824c635ad86a6d08b356`.

## 0. Short continuity handoff and division of labor

LIVE20 assigns NM13-01 to T08. The older pre-LIVE P0292 terminal handoff is preserved and untouched.

The newest own substantive report before this run was

`2026-09-20T04-22-00Z__incidence-strong-product-trace-obstruction.md`.

It proved cutoff for the non-LRE incidence-strong class `G boxtimes L(G)` and, more importantly for continuity, refuted the preceding raw output-degree NBRW-trace route as a necessary mechanism: an explicit degree-76 cutoff family has polynomially large raw NBRW collision trace at the output entropic radius. Its remaining T08 obstruction was to find a factor/conditional-information object stable under such local/product inflation without assuming an externally supplied decomposition.

The newest relevant P26 report read for this run is

`proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_06-57-44__distance2-green-shell-transfer.md`.

P26 proves a collision/Green shell-transfer theorem and applies it to the **pure exact-distance-two** graph of a high-girth Ramanujan base. I do not duplicate that class. This run takes the distinct transitivity/spherical-polynomial route, proves all fixed **pure exact-distance-k** classes for `k>=3`, and then proves a canonical stabilizer-orbit quotient which preserves the entire point-start mixing curve and information statistics exactly.

There are therefore two substantive advances:

1. a new source-valid non-LRE class, the pure exact-distance-`k` graphs for every fixed `k>=3`, with an explicit Gaussian profile and `Theta(sqrt(log n))` window; and
2. removal of the preceding structural obstruction “where does the useful factor come from?”: every vertex-transitive graph has a canonical stabilizer-orbit factor which loses **no** total-variation or likelihood-ratio information from a point start.

The remaining obstruction after this run is not factor extraction. It is controlling the possibly high-rank quotient using only transitivity plus a spectral gap.

## 1. Source convention and current primary boundary

The source was rechecked on 20 September 2026.

Justin Salez, `arXiv:2508.21055v1` (28 August 2025), defines continuous time by independent mean-one exponential holding times, hence for a discrete transition kernel `T`,

\[
P_t=e^{t(T-I)}
   =e^{-t}\sum_{m\ge0}\frac{t^mT^m}{m!}.
\tag{1.1}
\]

His Problem 2.3 is exactly:

> Prove that all vertex-transitive expanders exhibit cutoff.

Here the graph sequence has diverging size, uniformly bounded degree, and spectral gaps bounded away from zero.

The relevant newer primary boundary is unchanged but important.

* Dylan J. Altschuler, `arXiv:2609.14945v1`, submitted 14 September 2026, proves Gaussian-profile cutoff for every fixed-degree fixed-constant **long-range-expander** sequence. The paper proves the strict hierarchy
  \[
  \text{Ramanujan}\Longrightarrow\text{long-range expansion}
  \Longrightarrow\text{spectral expansion},
  \]
  with neither converse. Thus LRE is strictly stronger than the hypothesis in Salez Problem 2.3.
* Francesco Pedrotti and Justin Salez, `arXiv:2607.05345`, submitted 6 July 2026, prove that a local-product / non-equilibrium-Poincare condition implies cutoff. No checked statement there derives the needed condition solely from vertex transitivity and an ordinary spectral gap.
* The high-girth Ramanujan input class below is nonempty: the standard LPS Cayley families give fixed-degree vertex-transitive Ramanujan sequences with logarithmic girth, and one may take a non-bipartite degree-six subfamily as already used in the checked P26 T08 work.

Bounded searches on 20 September 2026 for combinations of `exact-distance graph random walk cutoff`, `distance-3 graph cutoff`, `Ramanujan exact-distance walk cutoff`, and repository searches for `J={3}` / `exact-distance-three` did not recover the theorem below. This is negative search evidence only.

The posted Abelian-Cayley/Product-Condition Problem-2.4 material remains excluded and is not reopened.

## 2. Parent problem before / after

### Before this run

Salez Problem 2.3 was `OPEN`. Checked positive scope included Altschuler's LRE theorem and several repository classes outside fixed LRE: line graphs, truncations, finite/twisted fibers, graph/strong products, same-vertex distance rewiring, and P26's pure exact-distance-two class under Ramanujan/high-girth input.

### After this run

Salez Problem 2.3 remains `OPEN`.

The proved scope expands as follows.

> **Theorem A — fixed pure exact-distance-k cutoff.**
> Fix integers `d>=3` and `k>=2`. Let `(G_n)` be connected non-bipartite `d`-regular vertex-transitive Ramanujan graphs with `|V(G_n)|=n->infinity` and `girth(G_n)->infinity`. For all sufficiently large `n`, let `Y_n^[k]` be the graph on the same vertex set in which two distinct vertices are adjacent iff their distance in `G_n` is exactly `k`.
>
> Write `q=d-1` and
> \[
> v_{d,k}
> :=k-\frac{2q}{d(q-1)}(1-q^{-k})
> =k-\frac{2(d-1)}{d(d-2)}(1-(d-1)^{-k}).
> \tag{2.1}
> \]
> Let `xi` have law
> \[
> \Pr(\xi=k)=\frac qd,
> \qquad
> \Pr(\xi=k-2j)=\frac{q-1}{dq^j}\quad(1\le j<k),
> \qquad
> \Pr(\xi=-k)=\frac1{dq^{k-1}},
> \tag{2.2}
> \]
> and put
> \[
> a_{d,k}:=\mathbb E[\xi^2].
> \tag{2.3}
> \]
> Then the rate-one continuous-time SRW on `(Y_n^[k])` has the Gaussian total-variation profile
> \[
> \boxed{
> d_{Y_n^{[k]}}\!\left(
> \frac{\log_q n}{v_{d,k}}+z\sqrt{\log_q n}
> \right)
> \longrightarrow
> \Phi\!\left(-z\frac{v_{d,k}^{3/2}}{\sqrt{a_{d,k}}}\right)
> }
> \tag{2.4}
> \]
> for every fixed real `z`. In particular it has cutoff at
> \[
> T_n=\frac{\log_{d-1}n}{v_{d,k}}
> \tag{2.5}
> \]
> with `Theta(sqrt(log n))` window.
>
> The output sequence is vertex-transitive and a uniform spectral expander, but it fails every fixed long-range-expansion constant.

P26 already supplied `k=2` by a different Green/shell proof. The **new theorem scope credited to this run is `k>=3`**.

For the explicit degree-six, `k=3` case,

\[
\deg(Y_n^{[3]})=150,
\qquad
v_{6,3}=\frac{194}{75},
\qquad
a_{6,3}=\frac{193}{25},
\tag{2.6}
\]

so

\[
\boxed{
T_n=\frac{75}{194}\log_5 n,
}
\tag{2.7}
\]

and

\[
\boxed{
 d_{Y_n^{[3]}}(T_n+z\sqrt{\log_5 n})
 \longrightarrow
 \Phi\!\left(-z\sqrt{\frac{7301384}{3256875}}\right).
}
\tag{2.8}
\]

The profile coefficient is approximately `1.49728`.

## 3. Exact-distance kernels are NBRW spherical polynomials

Fix a finite connected `d`-regular graph `G`, normalized adjacency/SRW kernel `P`, and `q=d-1`. Let `K_r(x,.)` denote the endpoint law of a length-`r` nonbacktracking walk which chooses its first neighbor uniformly and then each nonbacktracking continuation uniformly. Put

\[
p_0(x)=1,\qquad p_1(x)=x,
\tag{3.1}
\]

and for `r>=2`,

\[
p_r(x)=\frac d q x p_{r-1}(x)-\frac1q p_{r-2}(x).
\tag{3.2}
\]

The usual last-step decomposition of nonbacktracking paths gives the exact operator identity

\[
\boxed{K_r=p_r(P).}
\tag{3.3}
\]

If `girth(G)>2k`, then every length-`k` nonbacktracking path is a geodesic and two such paths from a common start cannot have the same endpoint. Hence the pure exact-distance-`k` graph is simple and

\[
D_k=dq^{k-1}
\tag{3.4}
\]

regular, and its discrete SRW kernel is exactly

\[
\boxed{Q_k=K_k=p_k(P).}
\tag{3.5}
\]

Vertex transitivity of `G` passes to `Y^[k]` because automorphisms preserve graph distance.

## 4. Uniform spectral expansion of the output

For

\[
x=\frac{2\sqrt q}{d}\cos\theta,
\]

the recurrence (3.2) gives

\[
\boxed{
 p_r(x)=q^{-r/2}
 \left[
 \frac2d\cos(r\theta)
 +\frac{d-2}{d}\frac{\sin((r+1)\theta)}{\sin\theta}
 \right],
}
\tag{4.1}
\]

with the endpoint values interpreted by continuity. Since

\[
\left|\frac{\sin((r+1)\theta)}{\sin\theta}\right|\le r+1,
\]

we obtain the Ramanujan-interval envelope

\[
|p_r(x)|
\le
B_{d,r}:=
q^{-r/2}\frac{2+(d-2)(r+1)}d.
\tag{4.2}
\]

For every fixed `r>=2`, `B_{d,r}<1`. Indeed the numerator is

\[
d+(d-2)r,
\]

while Bernoulli's inequality gives

\[
dq^{r/2}
=d(1+d-2)^{r/2}
\ge d+\frac{dr}{2}(d-2)
>d+r(d-2).
\tag{4.3}
\]

Because the nontrivial normalized spectrum of a non-bipartite Ramanujan `G_n` lies in

\[
\left[-\frac{2\sqrt q}{d},\frac{2\sqrt q}{d}\right],
\]

(3.5) and (4.2) imply

\[
|\lambda_i(Q_k)|\le B_{d,k}<1
\quad(i\ge2).
\tag{4.4}
\]

Thus the output is a uniform **absolute** spectral expander; in particular

\[
\operatorname{gap}(Y_n^{[k]})\ge1-B_{d,k}>0.
\tag{4.5}
\]

For `d=6,k=3`,

\[
B_{6,3}=\frac3{5\sqrt5},
\tag{4.6}
\]

so the gap is at least `1-3/(5 sqrt(5))`.

## 5. These exact-distance graphs are not fixed-constant LRE

Every edge of `Y^[k]` joins vertices at base distance exactly `k`, so

\[
B_{Y^{[k]}}(x,r)\subseteq B_G(x,kr).
\tag{5.1}
\]

The universal-tree volume bound therefore yields

\[
|B_{Y^{[k]}}(x,r)|\le C_d q^{kr}.
\tag{5.2}
\]

On the other hand the output degree is `D_k=dq^{k-1}` and hence its tree branching benchmark is

\[
D_k-1=q^k+q^{k-1}-1>q^k.
\tag{5.3}
\]

Suppose a fixed `c>0` made the output sequence `c`-long-range expanding. Apply the LRE inequality to the singleton `{x}` at

\[
r_n=\left\lfloor\frac12\log_{D_k-1}n\right\rfloor.
\]

For large `n` its required lower bound is `c(D_k-1)^{r_n}`, while (5.2) gives at most `C_d q^{kr_n}`. Their ratio is bounded by

\[
\frac{C_d}{c}
\left(\frac{q^k}{D_k-1}\right)^{r_n}\longrightarrow0,
\]

contradiction. Therefore no fixed positive LRE constant is possible.

This is why Theorem A is a genuine theorem-scope extension beyond merely applying Altschuler's LRE theorem to the output graph.

## 6. Exact spherical-power radialization

This is the main transitivity-independent algebraic step behind the new class.

Let `T_d` be the infinite `d`-regular tree rooted at `o`. Its spherical averaging operator at radius `r` is exactly `p_r(P_T)`. Consider the discrete distance-`k` walk on `T_d`: from the current vertex choose uniformly one of the `dq^{k-1}` vertices at tree distance `k`. Let

\[
R_m=d_{T_d}(o,X_m).
\]

By radial symmetry there are coefficients

\[
a_{m,r}=\Pr(R_m=r)
\]

such that, as operators on the tree,

\[
p_k(P_T)^m=\sum_r a_{m,r}p_r(P_T).
\tag{6.1}
\]

The spectrum of `P_T` contains an interval, so equality of the two finite-degree polynomials on that spectrum implies the polynomial identity

\[
\boxed{
p_k(z)^m=\sum_r a_{m,r}p_r(z).}
\tag{6.2}
\]

Substituting the transition matrix `P` of **any** finite `d`-regular graph gives

\[
\boxed{
K_k^m=\sum_r\Pr(R_m=r)K_r.
}
\tag{6.3}
\]

Poissonizing (6.3), exactly in Salez's convention, yields

\[
\boxed{
 e^{t(K_k-I)}
 =\sum_r\Pr(R_t=r)K_r,
}
\tag{6.4}
\]

where now `R_t=R_{N_t}` and `N_t~Pois(t)` is independent.

Thus the continuous-time exact-distance-`k` walk on the finite graph is an **exact mixture of ordinary NBRW endpoint shells**, with radial weights supplied by the tree distance-`k` process. No approximation or tree-likeness of the finite graph is used in (6.4).

## 7. Radial drift and Gaussian fluctuations

When `R_m>=k`, one distance-`k` tree jump changes the radius by an increment `xi` with law (2.2). To see this, let `j` be the number of initial edges of the chosen length-`k` geodesic that run toward the root. There are:

* `q^k` choices with `j=0`, giving probability `q/d` and increment `k`;
* `(q-1)q^{k-j-1}` choices for `1<=j<k`, giving probability `(q-1)/(dq^j)` and increment `k-2j`;
* one fully inward path with `j=k`, giving probability `1/(dq^{k-1})` and increment `-k`.

A direct finite geometric sum gives

\[
\boxed{
\mathbb E\xi
=k-\frac{2q}{d(q-1)}(1-q^{-k})=v_{d,k}>0.
}
\tag{7.1}
\]

The second moment is the explicit finite sum

\[
\boxed{
 a_{d,k}
 =\frac qd k^2
 +\sum_{j=1}^{k-1}\frac{q-1}{dq^j}(k-2j)^2
 +\frac{k^2}{dq^{k-1}}.
}
\tag{7.2}
\]

For completeness, the boundary at radii `<k` does not affect `sqrt(t)` fluctuations. Couple the chain to iid copies `(xi_j)` of the far increment so that actual and iid increments agree whenever the current radius is at least `k`. Since `E xi>0` and `xi` is bounded, there exists a small `theta>0` with

\[
\mathbb E e^{-\theta\xi}<1.
\]

The standard exponential-supermartingale argument implies that, from radius `r>=k`, the probability ever to return below `k` is at most `C e^{-\theta r}`. From the finite boundary set there is a fixed positive probability to make finitely many outward moves and thereafter never return. Consequently the total number of boundary visits has a geometric tail. Each boundary visit changes the coupled displacement by at most `2k`, so

\[
R_m=\sum_{j=1}^m\xi_j+O_{\mathbb P}(1).
\tag{7.3}
\]

Therefore the ordinary iid CLT gives

\[
\frac{R_m-v_{d,k}m}{\sqrt{\operatorname{Var}(\xi)m}}
\Longrightarrow N(0,1).
\]

For the rate-one Poissonization, the compound-Poisson variance per unit time is the **second moment** `E xi^2=a_{d,k}`, so

\[
\boxed{
\frac{R_t-v_{d,k}t}{\sqrt{a_{d,k}t}}
\Longrightarrow N(0,1).
}
\tag{7.4}
\]

uniformly for the `O(sqrt(log n))` time shifts used below. The tight boundary correction is negligible on that scale.

## 8. NBRW shell collision on a transitive Ramanujan base

For a vertex-transitive `d`-regular graph, the row `K_r(x,.)` has start-independent chi-square distance. Since `K_r=p_r(P)` is symmetric,

\[
\begin{aligned}
1+\chi^2(K_r(x,\cdot)\|\pi)
&=n\sum_yK_r(x,y)^2\\
&=n(K_r^2)(x,x)\\
&=\operatorname{tr}(K_r^2)
 =\sum_{i=1}^n p_r(\lambda_i)^2.
\end{aligned}
\]

Since `p_r(1)=1`,

\[
\boxed{
\chi^2(K_r(x,\cdot)\|\pi)
=\sum_{i=2}^n p_r(\lambda_i)^2.
}
\tag{8.1}
\]

For a non-bipartite Ramanujan graph, (4.2) gives

\[
\chi^2(K_r(x,\cdot)\|\pi)
\le C_d n(r+1)^2q^{-r}.
\tag{8.2}
\]

Let

\[
\ell_n:=\log_q n,
\qquad
h_n:=4\log_q\ell_n.
\tag{8.3}
\]

For all `r>=ell_n+h_n`, the right-hand side of (8.2) is `O(ell_n^{-2})`; hence by Cauchy-Schwarz,

\[
\sup_{r\ge\ell_n+h_n}
\|K_r(x,\cdot)-\pi\|_{TV}=o(1).
\tag{8.4}
\]

For the opposite side, every endpoint of an `r`-step NBRW lies in the base ball `B_G(x,r)`, and the universal tree bound gives

\[
\frac{|B_G(x,\ell_n-h_n)|}{n}
\le C_d q^{-h_n}=o(1).
\tag{8.5}
\]

Thus shells before `ell_n-h_n` live on a set of asymptotically negligible stationary mass.

## 9. Proof of the Gaussian cutoff profile

Write `H_t=e^{t(K_k-I)}` for the source-convention semigroup on `Y_n^[k]`. By (6.4),

\[
\delta_xH_t
=\sum_r\Pr(R_t=r)K_r(x,\cdot).
\tag{9.1}
\]

Using (8.4) and convexity of total variation,

\[
d_{Y_n^{[k]}}(t)
\le
\Pr(R_t<\ell_n+h_n)+o(1).
\tag{9.2}
\]

For the lower bound let

\[
A_n=B_G(x,\ell_n-h_n).
\]

Equation (8.5) gives `pi(A_n)=o(1)`, while (9.1) gives

\[
\delta_xH_t(A_n)
\ge\Pr(R_t\le\ell_n-h_n).
\]

Therefore

\[
d_{Y_n^{[k]}}(t)
\ge
\Pr(R_t\le\ell_n-h_n)-o(1).
\tag{9.3}
\]

Set

\[
T_n=\ell_n/v_{d,k},
\qquad
t=T_n+z\sqrt{\ell_n}.
\]

Because `h_n=o(sqrt(ell_n))`, the radial CLT (7.4) gives both

\[
\Pr(R_t<\ell_n+h_n)
\longrightarrow
\Phi\!\left(-z\frac{v_{d,k}^{3/2}}{\sqrt{a_{d,k}}}\right)
\]

and the same limit for the lower probability in (9.3). Squeezing proves (2.4). This completes Theorem A. `QED`

### Degree-six, k=3 arithmetic

For `d=6,q=5,k=3`, the far increment law is

\[
\Pr(\xi=3)=\frac56,
\quad
\Pr(\xi=1)=\frac2{15},
\quad
\Pr(\xi=-1)=\frac2{75},
\quad
\Pr(\xi=-3)=\frac1{150}.
\]

Hence

\[
v=\frac{194}{75},
\qquad
a=\frac{193}{25},
\qquad
\frac{v^3}{a}=\frac{7301384}{3256875},
\]

which proves (2.7)--(2.8).

## 10. Canonical stabilizer-orbit quotient: transitivity supplies the factor

The preceding report's remaining general obstruction was the absence of a canonical conditional/factor object on an arbitrary transitive graph. There is an exact answer at the level relevant to point-start mixing.

> **Theorem B — exact stabilizer-orbit information compression.**
> Let `X` be a finite connected `d`-regular vertex-transitive graph, let `Gamma<=Aut(X)` act transitively, fix a root `o`, and put `H=Gamma_o`. Let
> \[
> \mathcal O_0,\ldots,\mathcal O_m
> \]
> be the `H`-orbits on `V(X)`, with `O_0={o}`. Then SRW is strongly lumpable with respect to this orbit partition. If `bar P` is the quotient kernel and
> \[
> \bar\pi_i=|\mathcal O_i|/|V(X)|,
> \]
> then for every `t>=0`, writing
> \[
> \mu_t=\delta_o e^{t(P-I)},
> \qquad
> \bar\mu_t=\delta_0e^{t(\bar P-I)},
> \]
> one has, for every `x in O_i`,
> \[
> \boxed{
> \mu_t(x)=\frac{\bar\mu_t(i)}{|\mathcal O_i|},
> \qquad
> \frac{\mu_t(x)}{\pi(x)}
> =\frac{\bar\mu_t(i)}{\bar\pi_i}.
> }
> \tag{10.1}
> \]
> Consequently
> \[
> \boxed{
> \|\mu_t-\pi\|_{TV}
> =\|\bar\mu_t-\bar\pi\|_{TV}
> }
> \tag{10.2}
> \]
> for every time, and every `f`-divergence, relative entropy, chi-square distance, and the full distribution/variance of the information random variable `log(mu_t/pi)` are exactly preserved by the quotient.

### Proof

If `x,x'` lie in the same stabilizer orbit, choose `h in H` with `hx=x'`. Each orbit `O_j` is `H`-invariant and `h` is an automorphism, so the number of neighbors of `x` in `O_j` equals the number of neighbors of `x'` in `O_j`. Thus

\[
\bar P(i,j):=P(x,O_j),\qquad x\in O_i,
\tag{10.3}
\]

is well-defined: this is strong lumpability.

The point mass `delta_o` is `H`-invariant and `P` commutes with `H`, hence `mu_t` is `H`-invariant for every `t`; it is constant on each `O_i`. Its orbit masses evolve exactly by the quotient semigroup, proving the first identity in (10.1). Uniform stationarity gives `pi(x)=1/n` and `bar pi_i=|O_i|/n`, proving the likelihood-ratio identity.

Now sum within each orbit:

\[
\frac12\sum_{x\in V}|\mu_t(x)-1/n|
=\frac12\sum_i|\bar\mu_t(i)-\bar\pi_i|,
\]

which is (10.2). Any `f`-divergence is an expectation under `bar pi` of the same likelihood ratio appearing in (10.1), and the information random variable under `mu_t` is likewise the pullback of the quotient information variable. This proves all stated identities. `QED`

Because the graph is vertex-transitive, every starting vertex has the same TV curve. Therefore (10.2) is not merely a root-specific lower bound: it is the **entire worst-start mixing curve**.

## 11. Extra structure inherited by the orbit quotient

The quotient is not arbitrary.

1. **Gap does not get worse.** A quotient eigenfunction lifts to an `H`-invariant function on `V`. Hence the quotient spectrum is the spectrum of `P` restricted to the invariant subspace, and
   \[
   \boxed{\operatorname{gap}(\bar P)\ge\operatorname{gap}(P).}
   \tag{11.1}
   \]

2. **Bounded integral transition types.** If each vertex in `O_i` has `c_{ij}` neighbors in `O_j`, then
   \[
   \bar P(i,j)=c_{ij}/d,
   \qquad c_{ij}\in\{0,1,\ldots,d\}.
   \tag{11.2}
   \]
   In particular each quotient state has at most `d` positive off-diagonal destinations.

3. **Adjacent orbit masses cannot jump by more than d.** Edge counting gives
   \[
   |O_i|c_{ij}=|O_j|c_{ji}.
   \]
   Whenever `i` and `j` communicate,
   \[
   \boxed{
   \frac1d\le\frac{\bar\pi_j}{\bar\pi_i}
   =\frac{c_{ij}}{c_{ji}}\le d.
   }
   \tag{11.3}
   \]

Thus any counterexample to Salez Problem 2.3 must already produce non-cutoff in a reversible quotient chain with uniform gap, bounded out-degree, transitions in multiples of `1/d`, and locally bounded stationary-mass ratios.

This is the transitivity-specific mechanism sought here. It is complementary to P26's shell/Green transfer: P26 moves entropy through a supplied radial/shell representation, whereas Theorem B says that arbitrary transitivity itself supplies an exact **information-preserving quotient** before any entropy estimate is attempted.

It also sharpens the lessons of the two recent obstructions. The incidence-strong example showed that raw NBRW chi-square can be polynomially excessive despite cutoff. The affine stress test in neighboring T08 work showed that even the actual ambient heat-kernel chi-square/L2 transition can occur much later than the relevant TV scale. Theorem B identifies the natural object that does not lose TV information: the stabilizer-orbit likelihood-ratio chain, not the full ambient collision norm.

## 12. What remains genuinely open

Theorem B removes factor **existence**, not factor **complexity**. Its quotient can still have `Theta(n)` states; for a regular automorphism action the root stabilizer is trivial and the quotient is the original graph. Therefore I do **not** claim that (11.1)--(11.3) by themselves imply cutoff.

The residual obligation is now precise:

> Prove that, for stabilizer-orbit quotient chains arising from bounded-degree vertex-transitive spectral expanders, the information random variable has the concentration required by Salez's varentropy criterion; or find an additional canonical transitivity statistic which forces such concentration.

A promising next test is the affine Haiman family from the neighboring T08 obstruction report: ambient chi-square is polynomially late there. Computing the full-automorphism stabilizer quotient and its information variance would determine whether the quotient actually discards the offending high-multiplicity L2 pollution or whether a still finer Shannon mechanism is needed.

## 13. Executed exact sanity checks

The checker

`2026-09-20T05-00-20Z__exact_distance_k_orbit_checker.py`

was executed before persistence, using exact `Fraction` arithmetic. The archived output is

`2026-09-20T05-00-20Z__exact_distance_k_orbit_checker.out`.

It verifies:

* the polynomial spherical-mixture identity
  \[
  p_k^m=\sum_r\Pr(R_m=r)p_r
  \]
  exactly for `d in {3,4,6,8}`, `k in {2,3,4}`, and `m<=5`;
* the exact drift and second-moment arithmetic;
* `B_{d,k}<1` and the strict branching separation `D_k-1>q^k` in those cases;
* the degree-six, `k=3` constants in (2.6)--(2.8);
* exact equality of full-state and stabilizer-orbit total variation for eight discrete steps of SRW on the 3-cube, using the root-stabilizer Hamming-weight quotient.

The output ends

`ALL_EXACT_CHECKS_PASS`.

These finite checks are sanity checks for the algebra, not substitutes for the asymptotic proofs above.

## 14. Ledger delta and next attack

Machine-readable delta:

`2026-09-20T05-00-20Z__ledger_delta.json`.

Compact delta:

* parent source: Salez `arXiv:2508.21055v1`, Problem 2.3;
* parent status before/after: `OPEN -> OPEN`;
* source-level gain: pure exact-distance-`k` cutoff for every fixed `k>=3` on non-bipartite vertex-transitive Ramanujan high-girth bases, with explicit center/profile/window and proof that outputs are spectral but not fixed-LRE;
* mechanism gain: exact spherical-power radialization plus exact stabilizer-orbit preservation of point-start TV and information statistics;
* obstruction removed: no external factor decomposition is needed to represent the full transitive mixing curve;
* remaining obstruction: quotient rank may still be `Theta(n)`; derive quotient varentropy concentration from transitivity + expansion;
* failed/retired route preserved: raw ambient NBRW trace is not necessary, as proved in the predecessor; no attempt is made to revive it;
* next attack: apply Salez's varentropy criterion directly on the quotient and exploit the integral transition alphabet (11.2), local stationary-ratio bound (11.3), and uniform quotient gap (11.1), first stress-testing the affine high-multiplicity family.

No historical or peer file, shared root ledger, scheduler, permission, workflow, email/Drive object, or public surface was modified.
