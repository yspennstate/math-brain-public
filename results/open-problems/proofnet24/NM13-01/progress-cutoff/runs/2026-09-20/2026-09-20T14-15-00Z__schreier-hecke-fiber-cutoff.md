Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — no separately authenticated maximum-effort metadata is exposed.

# NM13-01 / LIVE20 T08 — Schreier-Hecke stochastic fibers and a canonical lossless transitive lift

**Parent status:** `PARTIAL / OPEN` for Salez Problem 2.3 before this run and after this run.

**Restricted theorem status:** `CANDIDATE_FULL` for Theorems A--D and the explicit degree-18 family below, pending later independent review.

**Publication novelty:** `UNVERIFIED`. The transfer/class and the way they are combined are new relative to the repository state read in this run. Coset/Hecke descriptions of transitive graphs are classical, so no priority claim is made for the abstract representation-theoretic language.

Repository/branch: `yspennstate/math-open-problems` / `master`.
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.
Run root: `proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/`.

## 0. Short handoff, preserved obstruction, and partner split

The latest complete own report read was

`2026-09-20T13-02-22Z__conditional-fiber-supercritical-cutoff.md`.

It proved an exact two-growing-quotient / conditional-residual-fiber transfer. Its cross-fiber kicks were still right translations, hence `L^2` isometries. The report narrowed the parent obstruction to this: a general vertex-transitive expander need not visibly present a normal quotient with a small residual fiber, and a useful transitivity argument should not assume such a quotient in advance.

This run changes the attack materially. First, it replaces translation kicks by arbitrary **doubly stochastic orbital kernels** on a homogeneous space. Those kicks may be singular, may have zero spectral gap, and may fail to commute strongly with the only genuinely mixing fiber operator. Second, it proves that every finite vertex-transitive graph has a canonical **lossless stabilizer/Hecke lift** to a group walk, even when the stabilizer is nonnormal. Hence absence of an algebraic group/factor representation is no longer the correct obstruction.

The newest relevant partner report read was

`proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_15-59-31__partitioned-green-clique-insertion-transfer.md`.

P26 now has a quotient-conditioned Green/shell theorem and applies it to clique-inserted Ramanujan graphs whose individual shells never approach global equilibrium. That is a covering-space / Green-function / radial-clock mechanism. The present run is complementary: it uses homogeneous-space orbitals, stochastic fiber contraction, variance decomposition and an exact Hecke lift. No P26 shell estimate is used.

The root `POSTED.md` exclusion registry was read. In particular, the posted Salez Problem 2.4 Abelian-Cayley product-condition manuscript is not reopened.

## 1. Exact source convention and current primary boundary

Justin Salez, `arXiv:2508.21055`, defines the continuous-time chain by inserting independent mean-one exponential waiting times between discrete jumps. Thus for discrete transition matrix `P`,

\[
H_t=e^{-t}\sum_{k\ge0}\frac{t^kP^k}{k!}=e^{t(P-I)}.
\tag{1.1}
\]

Problem 2.3 is exactly

> Prove that all vertex-transitive expanders exhibit cutoff.

The source takes an expander sequence to have diverging size, uniformly bounded degree and spectral gaps bounded away from zero.

Fresh primary-source screening on 20 September 2026 leaves the exact target open.

* Dylan J. Altschuler, `arXiv:2609.14945`, submitted 14 September 2026, proves an explicit Gaussian cutoff profile for every fixed-degree **long-range expander** sequence and proves the strict hierarchy
  \[
  \text{Ramanujan}\Longrightarrow\text{long-range expansion}\Longrightarrow\text{spectral expansion},
  \]
  with neither converse. Thus long-range expansion is not interchangeable with the arbitrary spectral-expander hypothesis in Salez Problem 2.3.
* Francesco Pedrotti and Justin Salez, `arXiv:2607.05345`, submitted 6 July 2026, prove a local-product / non-equilibrium-Poincare cutoff criterion. The checked result does not derive the required non-equilibrium constant from vertex transitivity plus an ordinary fixed spectral gap.
* Tali Kaufman and Alexander Lubotzky, `arXiv:1108.2960`, Theorem 3, construct `(q+1)`-regular edge-transitive Ramanujan Cayley graphs on `PSL_2(q^alpha)` / `PGL_2(q^alpha)` for `q^alpha>17`. We use the degree-six `q=5` family.
* Lubetzky--Peres, `arXiv:1507.04725`, gives cutoff for regular non-bipartite Ramanujan graphs. In the rate-one continuous-time convention, Poissonization preserves the center and only contributes square-root-order fluctuations, so for degree six the center is `(3/2) log_5 n` with `Theta(sqrt(log n))` window. This source-convention dependency was already established and used in earlier NM13-01 runs and is preserved here.

## 2. Original problem before / after versus mechanism progress

### Original problem before

Salez Problem 2.3 was `OPEN`. NM13-01 already had several bounded-degree vertex-transitive spectral-but-not-LRE cutoff classes, including normalizing voltages, noncommuting translation fibers and conditional residual fibers. The latest theorem still assumed a visible exact quotient/fiber organization and used fiber kicks that were permutations of the residual state space.

### Original problem after

Salez Problem 2.3 remains `OPEN`. No theorem below asserts a cutoff for an arbitrary vertex-transitive spectral expander.

The restricted source-valid scope is enlarged by a degree-18 vertex-transitive family with all of the following properties simultaneously:

1. fixed ordinary spectral gap at least
   \[
   \boxed{\frac{2(3-\sqrt5)}9=0.1697626716\ldots};
   \tag{2.1}
   \]
2. source-continuous-time cutoff at
   \[
   \boxed{T_n=\frac94\log_5 n
   =\frac94\log_5 N_n+O(1)};
   \tag{2.2}
   \]
3. window
   \[
   \boxed{O(\sqrt{\log N_n})};
   \tag{2.3}
   \]
4. failure of every fixed positive long-range-expansion constant;
5. cross-fiber kernels that are genuine stochastic averages rather than permutations;
6. a cross kernel with **zero** one-sided spectral gap;
7. a persistent noncommutation certificate
   \[
   \boxed{\|[K,R]\|_{2\to2}=\frac{\sqrt2}{3}}.
   \tag{2.4}
   \]

Items 5--7 are the mechanism-level advance. They explicitly lie outside the hypotheses of the previous translation/isometry and common-gap switched-fiber transfers.

## 3. The stochastic-fiber transfer

Let

\[
G=\operatorname{Cay}(\Gamma,S),\qquad |S|=d,
\]

be a finite connected undirected Cayley graph. Let `F` be a finite set of cardinality `m`, equipped with its uniform law `pi_F`.

For every `s in S`, let `K_s` be a Markov kernel on `F` with the following properties:

* `K_s` is doubly stochastic;
* every row has exactly `k` nonzero entries, each equal to `1/k`;
* `K_{s^{-1}}=K_s^T`.

Let `R` be the SRW kernel of a simple `r`-regular undirected graph on `F`, and suppose

\[
\operatorname{gap}(R)\ge\eta>0.
\tag{3.1}
\]

Construct a graph `H` on `Gamma x F` by declaring two kinds of edges:

* **cross edges:** `(g,x)` is adjacent to `(gs,y)` whenever `K_s(x,y)>0`;
* **refresh edges:** `(g,x)` is adjacent to `(g,y)` whenever `R(x,y)>0`.

Assume the displayed supports define a simple graph. It is then regular of degree

\[
D=kd+r.
\tag{3.2}
\]

Put

\[
a=\frac{kd}{D},\qquad b=\frac rD.
\tag{3.3}
\]

All continuous-time chains use (1.1).

### Lemma 3.1 — arbitrary doubly stochastic kicks cost no `L^2` energy

Let `K` be a doubly stochastic kernel on a finite uniform space. Then on centered functions,

\[
\|Kf\|_{2,\pi_F}\le\|f\|_{2,\pi_F}.
\tag{3.4}
\]

The same holds for `K^T`.

#### Proof

By Jensen,

\[
(Kf(x))^2\le K(f^2)(x).
\]

Average in `x`. Double stochasticity makes the uniform law invariant, hence

\[
\sum_x\pi_F(x)(Kf(x))^2
\le\sum_x\pi_F(x)K(f^2)(x)
=\sum_y\pi_F(y)f(y)^2.
\]

Transposition preserves double stochasticity. `QED`

This is strictly weaker than being a permutation/isometry. The kernel may be singular and may have several invariant subspaces.

### Lemma 3.2 — pathwise fiber contraction

Fix arbitrary cross times and arbitrary labels `s_1,...,s_q`. Between the cross times let the fiber evolve by the rate-`b` refresh semigroup

\[
\exp(bs(R-I)).
\]

At cross time `i`, apply `K_{s_i}` (or its transpose according to row/column convention). If `f_t` is the density with respect to `pi_F`, then

\[
\boxed{
\|f_t-1\|_2\le e^{-b\eta t}\|f_0-1\|_2.
}
\tag{3.5}
\]

#### Proof

Every cross kick contracts `L^2` by Lemma 3.1. On a refresh interval of length `u`, the spectral-gap inequality gives

\[
\|e^{bu(R-I)}g\|_2\le e^{-b\eta u}\|g\|_2
\]

for mean-zero `g`. Multiplying all interval factors gives `e^{-b eta t}`, since the refresh semigroup runs continuously between the instantaneous cross events and the interval lengths sum to `t`. No commutation is used. `QED`

From a point mass on an `m`-point uniform space,

\[
\|f_0-1\|_2=\sqrt{m-1}.
\]

Cauchy--Schwarz therefore yields the pathwise bound

\[
\boxed{
\|\mathcal L(X_t^F\mid\hbox{complete cross path})-\pi_F\|_{TV}
\le\frac12\sqrt{m-1}\,e^{-b\eta t}.
}
\tag{3.6}
\]

### Theorem A — stochastic-fiber TV sandwich

Let `d_G,d_H` be worst-start TV distances. Then for every `t>=0`,

\[
\boxed{
 d_G(at)
 \le d_H(t)
 \le d_G(at)+\frac12\sqrt{m-1}\,e^{-b\eta t}.
}
\tag{3.7}
\]

#### Proof

Poisson thinning separates the `kd` cross edges from the `r` refresh edges. Cross events occur at rate `a`; conditioned on a cross event, its base label is uniform in `S`. Hence the base projection is exactly source rate-one SRW on `G` run for time `at`. Projection cannot increase TV, proving the lower bound.

For the upper bound condition on the complete base cross path: all cross times and generator labels. The remaining fiber law is precisely the time-ordered stochastic evolution in Lemma 3.2, so it is within the quantity in (3.6) of uniform, uniformly over the conditioned path. Replace that conditional fiber law by `pi_F` and average. The resulting joint law is `mu^G_{at} otimes pi_F`; the replacement costs at most (3.6), and the remaining TV distance is exactly `d_G(at)`. `QED`

### Corollary 3.3 — cutoff transfer

Suppose `G_n` has source-continuous-time cutoff at center `T_n` with window `w_n=o(T_n)`, and the fiber parameters `m,k,r,eta` are fixed. Then `H_n` has cutoff at

\[
\boxed{T_n^H=T_n/a}
\tag{3.8}
\]

with window `O(w_n/a+1)`. If the base has a limiting profile on scale `w_n` and `w_n->infinity`, the output has the same profile after the deterministic time rescaling by `a`.

Indeed the error term in (3.7) is exponentially small at times of order `T_n`, while the lower and upper base terms coincide asymptotically.

## 4. Spectral expansion survives stochastic cross averaging

### Theorem B — gap transfer

If `gamma_G=gap(G)`, then

\[
\boxed{
\operatorname{gap}(H)\ge\min\{a\gamma_G,b\eta\}.
}
\tag{4.1}
\]

#### Proof

For `f(g,x)` define the fiber average

\[
\bar f(g)=\mathbb E_{x\sim\pi_F}f(g,x).
\]

Variance decomposes as

\[
\operatorname{Var}(f)
=\mathbb E_g\operatorname{Var}_F(f(g,\cdot))
+\operatorname{Var}_G(\bar f).
\tag{4.2}
\]

The refresh part of the normalized output Dirichlet form is at least

\[
b\eta\,\mathbb E_g\operatorname{Var}_F(f(g,\cdot)).
\tag{4.3}
\]

For a fixed base generator `s`, let `X` be uniform on `F` and conditionally let `Y` have law `K_s(X,.)`. Double stochasticity makes `Y` uniform. Jensen gives

\[
\mathbb E(f(g,X)-f(gs,Y))^2
\ge
\big(\bar f(g)-\bar f(gs)\big)^2.
\tag{4.4}
\]

Averaging in `g,s` shows that the cross contribution is at least

\[
a\,\mathcal E_G(\bar f,\bar f)
\ge a\gamma_G\operatorname{Var}_G(\bar f).
\tag{4.5}
\]

Combine (4.2)--(4.5). `QED`

The point is important: **no positive gap is required for any `K_s`**. The only strict fiber contraction may come from `R`.

## 5. A fixed nonnormal Schreier fiber with exact strong noncommutation

Take

\[
J=S_4,\qquad H=\langle(12)\rangle,
\qquad F=J/H.
\tag{5.1}
\]

Thus `|F|=12`; `H` is nonnormal. Put

\[
r_A=(13),\qquad r_B=(14),\qquad r_C=(13)(24)
\]

and

\[
D_i=Hr_iH\qquad(i=A,B,C).
\tag{5.2}
\]

Each `D_i` has four elements, is inverse-closed, and is the union of two right `H`-cosets. Define the orbital kernel `K_i` on `J/H` by

\[
K_i(xH,yH)
=\frac1{|D_i|}
\big|\{d\in D_i:xdH=yH\}\big|.
\tag{5.3}
\]

Because `D_i` is `H`-bi-invariant, this is independent of the representative `x`. Each `K_i` is a symmetric doubly stochastic two-neighbor kernel. Their supports are pairwise disjoint. Therefore

\[
R=\frac13(K_A+K_B+K_C)
\tag{5.4}
\]

is the SRW kernel of a simple six-regular graph on `F`.

The exact checker computes

\[
\chi_R(\lambda)
=\frac1{19683}\lambda^2(\lambda-1)(3\lambda-1)^3(3\lambda+1)^6,
\tag{5.5}
\]

so

\[
\boxed{\operatorname{gap}(R)=\frac23}.
\tag{5.6}
\]

In contrast,

\[
\chi_{K_A}(\lambda)
=\frac1{256}(\lambda-1)^4(2\lambda+1)^8,
\tag{5.7}
\]

so `K_A` has eigenvalue `1` of multiplicity four and hence one-sided gap zero. It is not a permutation kernel: every row averages two states.

Finally,

\[
\chi_{[K_A,R]^*[K_A,R]}(\lambda)
=\frac1{531441}\lambda^6(9\lambda-2)^6,
\]

hence

\[
\boxed{
\|[K_A,R]\|_{2\to2}=\frac{\sqrt2}{3}.
}
\tag{5.8}
\]

For comparison the pairwise orbital commutators satisfy

\[
\|[K_A,K_B]\|_{2\to2}
=\|[K_A,K_C]\|_{2\to2}
=\|[K_B,K_C]\|_{2\to2}
=\frac1{\sqrt2}.
\tag{5.9}
\]

Thus this fiber is neither a hidden translation model nor a common-gap switched model; the failure persists at fixed operator norm.

## 6. Explicit degree-18 spectral-but-not-LRE cutoff family

Let

\[
G_n=\operatorname{Cay}(\Gamma_n,S_n),\qquad |S_n|=6,
\]

be the `q=5` Kaufman--Lubotzky Ramanujan Cayley family, with `n=|Gamma_n|`. On

\[
V(H_n)=\Gamma_n\times S_4/H
\tag{6.1}
\]

use `K_s=K_A` for every base generator `s`, and use the six-regular refresh graph (5.4). A cross base edge therefore has two fiber continuations. The output degree is

\[
D=2\cdot6+6=18,
\tag{6.2}
\]

with

\[
a=\frac23,\qquad b=\frac13.
\tag{6.3}
\]

The action of `Gamma_n x S_4` by

\[
(\gamma,j):(g,xH)\mapsto(\gamma g,jxH)
\tag{6.4}
\]

preserves both the cross orbital relation and the refresh orbital relations, and is transitive. Hence `H_n` is vertex-transitive. Connectivity follows from base connectivity plus refresh connectivity.

### 6.1 Spectral gap

For a six-regular Ramanujan graph,

\[
\gamma_G\ge1-\frac{2\sqrt5}{6}
=\frac{3-\sqrt5}{3}.
\]

Theorem B and (5.6) give

\[
\operatorname{gap}(H_n)
\ge
\min\left\{
\frac23\frac{3-\sqrt5}{3},
\frac13\frac23
\right\}
=
\boxed{\frac{2(3-\sqrt5)}9}.
\tag{6.5}
\]

Thus the output is a bounded-degree spectral-expander sequence.

### 6.2 Cutoff center and window

The preserved source-continuous Ramanujan theorem gives

\[
T_n^G=\frac32\log_5 n,
\qquad
w_n^G=O(\sqrt{\log n}).
\tag{6.6}
\]

Apply Corollary 3.3 with `a=2/3`:

\[
\boxed{
T_n^H=\frac94\log_5 n,
\qquad
w_n^H=O(\sqrt{\log n}).
}
\tag{6.7}
\]

Since

\[
N_n=|V(H_n)|=12n,
\]

this is exactly

\[
\boxed{
T_n^H=\frac94\log_5N_n+O(1),
\qquad
w_n^H=O(\sqrt{\log N_n}).
}
\tag{6.8}
\]

At the cutoff center, the fiber error from Theorem A is

\[
\frac12\sqrt{11}\exp\left[-\frac29\cdot\frac94\log_5n\right]
=rac12\sqrt{11}\,n^{-1/(2\log 5)},
\tag{6.9}
\]

which is polynomially small. Numerically the exponent is

\[
\frac1{2\log5}=0.3106674672\ldots .
\]

### 6.3 Failure of long-range expansion

Projection to the base is 1-Lipschitz in graph distance. Every base vertex has only 12 fiber states. Therefore for every radius `r`,

\[
|B_{H_n}((g,xH),r)|
\le 12|B_{G_n}(g,r)|
\le C\,5^r,
\tag{6.10}
\]

where the last bound is the universal tree-growth upper bound for a six-regular graph.

The output has degree 18, so the long-range-expansion tree benchmark is `17^r`. Put

\[
r_n=\left\lfloor\frac12\log_{17}N_n\right\rfloor.
\tag{6.11}
\]

Then `17^{r_n}=N_n^{1/2+o(1)}` and the ball in (6.10) is still `o(N_n)`, while

\[
\frac{|B_{H_n}(x,r_n)|}{17^{r_n}}
\le
N_n^{-\beta+o(1)},
\qquad
\boxed{
\beta=\frac12\left(1-\frac{\log5}{\log17}\right)
=0.2159695164\ldots>0.
}
\tag{6.12}
\]

Hence for every fixed `c>0`, the singleton-set long-range-expansion inequality fails at radius `r_n` for all sufficiently large `n`. This family is therefore not contained in Altschuler's fixed-constant LRE class.

## 7. Canonical lossless Hecke lift of every transitive graph

The explicit class still has a designed product coordinate. The next statement addresses the more general structural obstruction from the previous run.

### Theorem C — every transitive SRW is a stabilizer-bi-invariant group walk

Let `X` be a finite connected `d`-regular vertex-transitive graph. Choose any transitive subgroup

\[
A\le\operatorname{Aut}(X),
\]

fix a root `o`, and let

\[
H=A_o
\]

be its stabilizer. Identify

\[
V(X)\cong A/H,
\qquad gH\longmapsto go.
\tag{7.1}
\]

Define

\[
D=\{a\in A:ao\sim o\}.
\tag{7.2}
\]

Then:

1. `D` is `H`-bi-invariant and inverse-closed;
2. `|D|=d|H|`;
3. if `mu` is uniform on `D`, then right multiplication by an independent `mu`-increment, projected from `A` to `A/H`, is exactly one step of SRW on `X`;
4. if the group walk starts from the uniform law on `H`, its projection starts from `o`.

#### Proof

If `a o` is adjacent to `o` and `h_1,h_2 in H`, then

\[
h_1ah_2o=h_1ao\sim h_1o=o,
\]

so `H D H=D`. Undirectedness gives `D^{-1}=D`: from `ao~o`, apply `a^{-1}` to obtain `o~a^{-1}o`.

The map `a -> ao` sends `D` onto the `d` neighbors of `o`, and every fiber is a right coset of `H`, of size `|H|`. Hence `|D|=d|H|`.

From coset `gH`, an increment `a in D` sends the projection to `gaH`. For each neighbor of `go`, exactly `|H|` elements of `D` produce its coset, so the projected transition probability is `|H|/(d|H|)=1/d`. Starting uniformly on `H` projects to `H=o`. `QED`

This is the canonical `H`-bi-invariant / Hecke description; normality of `H` is not required.

### Theorem D — exact information isometry of the lift

Let `nu_t` be the source-continuous-time law on `A` from initial law `Unif(H)` under the step measure `mu` above. Let `bar nu_t` be its projection to `A/H`, which by Theorem C is exactly root-start SRW on `X`. Let `pi_A` and `bar pi` be the uniform laws on `A` and `A/H`.

Then `nu_t` is right-`H`-invariant for every `t`, and for every `z in gH`,

\[
\boxed{
\frac{\nu_t(z)}{\pi_A(z)}
=
\frac{\bar\nu_t(gH)}{\bar\pi(gH)}.
}
\tag{7.3}
\]

Consequently, for every `t`:

\[
\boxed{
\|\nu_t-\pi_A\|_{TV}
=
\|\bar\nu_t-\bar\pi\|_{TV};
}
\tag{7.4}
\]

more generally every `f`-divergence agrees exactly, including relative entropy and `chi^2`; and the information random variables

\[
\log\frac{\nu_t(Z_t)}{\pi_A(Z_t)}
\quad\hbox{and}\quad
\log\frac{\bar\nu_t(X_t)}{\bar\pi(X_t)}
\tag{7.5}
\]

have exactly the same distribution. In particular their varentropies are equal.

#### Proof

The initial uniform law on `H` is right-`H`-invariant. The step measure is right-`H`-invariant because `D H=D`. Convolution therefore preserves right-`H` invariance in discrete time, and Poissonization preserves it in continuous time.

Thus `nu_t` is constant on each right coset. Since every coset has `|H|` elements,

\[
\nu_t(z)=\frac{\bar\nu_t(gH)}{|H|},
\qquad z\in gH.
\]

Also

\[
\pi_A(z)=\frac1{|A|},
\qquad
\bar\pi(gH)=\frac{|H|}{|A|}.
\]

Dividing gives (7.3). Summing any function of this likelihood ratio over each coset proves the equality of all `f`-divergences; sampling under `nu_t` proves the distributional identity (7.5). `QED`

## 8. What obstruction has actually been removed?

The preceding conditional-fiber run left two intertwined concerns: perhaps a general transitive expander has no usable algebraic factor at all, and perhaps non-permutation hidden dynamics destroys the clean pathwise transfer.

Both are now narrowed sharply.

First, Theorem A shows that permutation/isometry kicks are unnecessary. Cross dynamics may be **singular, zero-gap, stochastic averaging**, and may have a fixed nonzero commutator with the refresh operator. The explicit Schreier fiber certifies all of these features simultaneously.

Second, Theorems C--D show that every transitive graph already has a canonical exact algebraic realization as a nonnormal stabilizer quotient of a group walk, with **no loss whatsoever in TV or information statistics**. Thus “there is no quotient/factor representation” cannot be the fundamental obstruction to Salez Problem 2.3.

The remaining obstruction is more precise and genuinely representation-theoretic: in the canonical lift the stabilizer `H` may be huge and nonnormal, the `H`-bi-invariant convolution operator may live in a high-dimensional noncommutative Hecke algebra, and there need not be a separated uniformly gapped refresh component to which Theorem A can be applied. The next route should therefore work inside the permutation representation `Ind_H^A(1)`: either extract a bounded-complexity dissipative component forced by the graph spectral gap, or control the exact likelihood-ratio varentropy of the subgroup-uniform Hecke walk directly from matrix coefficients. This connects naturally to Salez's varentropy criterion while remaining complementary to P26's Green/shell mechanism.

## 9. Sanity checks

The executed exact checker is

`2026-09-20T14-15-00Z__schreier-hecke-fiber-check.py`

with archived output

`2026-09-20T14-15-00Z__schreier-hecke-fiber-check.out`.

It verifies exactly:

* `|S_4/H|=12` and all three double cosets have size four;
* each orbital kernel is symmetric two-regular;
* the refresh characteristic polynomial (5.5) and gap `2/3`;
* the zero-gap characteristic polynomial (5.7) of `K_A`;
* `||[K_A,R]||=sqrt(2)/3` and pairwise orbital commutator norm `1/sqrt(2)`;
* degree 18, rates `a=2/3`, `b=1/3`, gap bound (6.5), center coefficient `9/4`, fiber-error exponent and positive non-LRE exponent.

It also builds an 84-state finite toy model over `K_7` and numerically checks the continuous-time TV sandwich at five times. Those finite computations are only sanity checks; they are not used as evidence for the asymptotic theorem. The output ends

`ALL_EXACT_AND_SANITY_CHECKS_PASS`.

## 10. Handoff

**Parent source status:** `OPEN -> OPEN`.

**New restricted theorem:** degree-18 vertex-transitive spectral-but-not-LRE Schreier-fiber cutoff class at `(9/4) log_5 N + O(1)` with `O(sqrt(log N))` window, together with the general stochastic-fiber transfer allowing zero-gap noncommuting averaging kicks.

**Mechanism advance:** every transitive SRW has a canonical stabilizer-bi-invariant Hecke lift preserving TV and the full information-variable law exactly; lack of a normal/product quotient is no longer the right obstruction.

**Residual obstruction:** force useful dissipation/varentropy control inside a potentially large noncommutative stabilizer Hecke algebra using only bounded degree, transitivity and ordinary spectral expansion.

**Next attack:** decompose `Ind_H^A(1)` into isotypic blocks and seek a transitivity-specific estimate on the distribution of point-start likelihood across blocks; in parallel, test whether a fixed spectral gap forces a bounded number of high-mass Hecke orbitals to supply a uniformly dissipative component after conditioning on a small orbit-type chain.
