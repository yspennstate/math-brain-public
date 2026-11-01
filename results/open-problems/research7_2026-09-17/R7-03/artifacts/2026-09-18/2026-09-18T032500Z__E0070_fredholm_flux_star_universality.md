Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# E0070 / Björklund Problem 2 — Fredholm exact sequence, homogeneous-space flux, and star-kernel universality

Date: 2026-09-18 UTC  
Worker: R7-03 Boundary-Case Research  
Native ID: `6aabe7be74008191b526b109ee4e9e80`  
Source: Michael Björklund, *Five remarks about random walks on groups*, arXiv:1406.0763v2 (2014), Appendix II §7.1, Problem 2, printed p.24.  
Frozen metric: `C_E0070=1` before this note and still `1` after it.

This note strengthens and reorganizes the already-complete E0070 source candidate. It does **not** count as an independent audit and does not change the binary source-completion metric. The immediately preceding R7-03 triple was B3/B15/B29. The three new methods here are **B1 / B12 / B26**.

## 1. Recalled source-valid star quotient

Let

\[
X=\mathbb N_0,\qquad
G=\operatorname{Sym}_{\rm fin}(X),\qquad
H=\operatorname{Stab}_G(0).
\]

For `n>=1` let `tau_n=(0 n)`. Choose any strictly positive probability vector `(p_n)` and put

\[
\mu(\tau_n)=p_n,\qquad \sum_{n\ge1}p_n=1.
\]

The quotient `G/H` is identified with `X`, and the induced left convolution operator is

\[
(Pu)(0)=\sum_{n\ge1}p_nu(n),
\tag{1.1}
\]

\[
(Pu)(n)=p_nu(0)+(1-p_n)u(n),\qquad n\ge1.
\tag{1.2}
\]

The source integrability needed at the root is

\[
\sum_{n\ge1}p_n|u(n)|<\infty.
\tag{1.3}
\]

The previous run proved the exact range

\[
\operatorname{Ran}(P-I)=
\left\{d\in\ell^1(X):\sum_{x\in X}d(x)=0\right\}
\tag{1.4}
\]

on the natural source domain, and proved that the kernel consists exactly of constants. We now identify the Banach/Fredholm structure behind (1.4), then show that its conservation law is forced for every homogeneous-space walk, and finally classify every homogeneous-space kernel whose off-diagonal quotient graph is a star.

---

## 2. B1 — change category: an exact Banach-space Fredholm complex

Define the Banach space

\[
\mathcal D_p=
\left\{u:X\to\mathbb C:
|u(0)|+\sum_{n\ge1}p_n|u(n)|<\infty
\right\}
\tag{2.1}
\]

with norm

\[
\|u\|_{\mathcal D_p}=|u(0)|+\sum_{n\ge1}p_n|u(n)|.
\]

Let `A=P-I`. Introduce the weighted gradient coordinates

\[
z_n=p_n(u(n)-u(0)),\qquad n\ge1.
\tag{2.2}
\]

### Theorem 2.1 — `D_p` is exactly `C ⊕ ell^1` in weighted-gradient coordinates

The map

\[
\Phi:\mathcal D_p\longrightarrow \mathbb C\oplus\ell^1(\mathbb N),
\qquad
\Phi(u)=(u(0),z)
\tag{2.3}
\]

is a Banach-space isomorphism. Its inverse is

\[
\Phi^{-1}(a,z)(0)=a,
\qquad
\Phi^{-1}(a,z)(n)=a+\frac{z_n}{p_n}.
\tag{2.4}
\]

#### Proof

For `u in D_p`,

\[
\sum_n|z_n|
\le \sum_np_n|u(n)|+|u(0)|\sum_np_n
=\sum_np_n|u(n)|+|u(0)|,
\]

so `z in ell^1`. Conversely, if `(a,z) in C\oplus ell^1`, then

\[
\sum_np_n\left|a+\frac{z_n}{p_n}\right|
\le |a|+\sum_n|z_n|<\infty.
\]

Moreover

\[
\|\Phi u\|\le 2\|u\|_{\mathcal D_p},
\qquad
\|\Phi^{-1}(a,z)\|_{\mathcal D_p}
\le 2|a|+\|z\|_1
\le2\|(a,z)\|,
\]

so both maps are bounded. ∎

In these coordinates the Poisson defect becomes completely rigid:

\[
A\Phi^{-1}(a,z)
=
\left(\sum_{n\ge1}z_n,-z_1,-z_2,\ldots\right).
\tag{2.5}
\]

Indeed, the leaf defect is `p_n(u(0)-u(n))=-z_n`, while the root defect is

\[
\sum_np_nu(n)-u(0)=\sum_nz_n.
\]

Define

\[
J:\ell^1(\mathbb N)\to\ell^1(X),
\qquad
Jz=\left(\sum_nz_n,-z_1,-z_2,\ldots\right).
\tag{2.6}
\]

Then `A=J\circ\pi_z\circ\Phi`.

### Theorem 2.2 — exact Fredholm sequence

Let

\[
\Sigma:\ell^1(X)\to\mathbb C,
\qquad
\Sigma(d)=\sum_{x\in X}d(x).
\tag{2.7}
\]

Then

\[
\boxed{
0\longrightarrow\mathbb C
\longrightarrow\mathcal D_p
\xrightarrow{\ A\ }
\ell^1(X)
\xrightarrow{\ \Sigma\ }
\mathbb C
\longrightarrow0
}
\tag{2.8}
\]

is an exact sequence of Banach spaces and bounded operators, where the first map sends a scalar to the corresponding constant function.

Consequently:

\[
\ker A=\mathbb C\mathbf 1,
\tag{2.9}
\]

\[
\operatorname{Ran}A=\ker\Sigma,
\tag{2.10}
\]

`Ran A` is closed, its codimension is one, and

\[
\boxed{\operatorname{ind}A=\dim\ker A-\operatorname{codim Ran}A=1-1=0.}
\tag{2.11}
\]

#### Proof

The kernel statement follows immediately from (2.5): `Az=0` forces `z=0`, hence `u` is constant. The range of `J` is contained in `ker Sigma` because

\[
\Sigma(Jz)=\sum_nz_n-\sum_nz_n=0.
\]

Conversely, if `d in ell^1(X)` satisfies `Sigma(d)=0`, set `z_n=-d_n`. Then

\[
\sum_nz_n=-\sum_{n\ge1}d_n=d_0,
\]

so `Jz=d`. Thus `Ran A=ker Sigma`. Since `Sigma` is a bounded nonzero functional, its kernel is a closed codimension-one subspace. Exactness at the two copies of `C` is immediate. ∎

### Adjoint/cokernel computation

Under the coordinates `D_p ~= C\oplus ell^1`, the dual is `C\oplus ell^infty`. For `h=(h_0,h_1,...) in ell^infty(X)`,

\[
\langle h,Jz\rangle
=
\sum_{n\ge1}(h_0-h_n)z_n.
\tag{2.12}
\]

Hence

\[
A^*h=(0,(h_0-h_n)_{n\ge1})
\tag{2.13}
\]

in the dual `C\oplus ell^infty` coordinates, and therefore

\[
\boxed{\ker A^*=\mathbb C\mathbf1.}
\tag{2.14}
\]

Thus the one-dimensional cokernel of `A` is literally generated by the conserved total-mass functional. The source rigidity is a Fredholm alternative of index zero: constants are the only homogeneous solutions, and total mass is the only obstruction to solving an `ell^1` Poisson equation.

A nonzero constant defect `c\mathbf1` is not in `ell^1(X)` because `X` is infinite. Hence no nonzero constant defect can lie in `Ran A`; after `c=0`, (2.9) forces `u` constant.

**B1 outcome: SUCCESS.** The proof is not merely a leafwise calculation: the source domain carries an exact two-term Fredholm complex with one-dimensional kernel and cokernel.

---

## 3. B12 — find what is conserved: every homogeneous-space kernel preserves counting measure

The finite-star artifact observed a conservation law for the explicit symmetric example. That conservation is much more general and does **not** depend on symmetry of `mu`.

Let `(G,mu)` be any countable measured group and let `X=G/H` be any countable homogeneous space. Let `P` be the left quotient kernel induced by `check(mu)`:

\[
P(x,y)=\check\mu\{s\in G:sx=y\}.
\tag{3.1}
\]

### Theorem 3.1 — quotient kernels are doubly stochastic

For every `x,y in X`, `P(x,y)>=0`, and

\[
\boxed{\sum_yP(x,y)=1,\qquad \sum_xP(x,y)=1.}
\tag{3.2}
\]

Thus counting measure on `G/H` is always a stationary sigma-finite measure for the quotient walk.

#### Proof

The row identity is stochasticity. For the column identity, use Tonelli and the fact that every fixed `s in G` acts on `X` by a bijection:

\[
\begin{aligned}
\sum_xP(x,y)
&=\sum_x\int_G\mathbf1_{\{sx=y\}}\,d\check\mu(s)\\
&=\int_G\left(\sum_x\mathbf1_{\{sx=y\}}\right)d\check\mu(s)\\
&=\int_G1\,d\check\mu(s)=1.
\end{aligned}
\]

For each fixed `s` there is exactly one `x=s^{-1}y`, which gives the third equality. ∎

This remains true for nonsymmetric `mu`: `P` is a convex combination of permutation matrices, and each permutation preserves counting measure.

### Theorem 3.2 — exact finite-set flux identity

Let `F subset X` be finite and let `u` be such that all quotient convolutions in the displayed formula are absolutely defined. Then

\[
\boxed{
\sum_{x\in F}(Pu-u)(x)
=\sum_{y\notin F}u(y)\sum_{x\in F}P(x,y)
-\sum_{y\in F}u(y)\sum_{x\notin F}P(x,y).
}
\tag{3.3}
\]

#### Proof

Start from

\[
\sum_{x\in F}(Pu-u)(x)
=\sum_yu(y)\left(\sum_{x\in F}P(x,y)-\mathbf1_F(y)\right).
\]

For `y in F`, column stochasticity gives

\[
\sum_{x\in F}P(x,y)-1=-\sum_{x\notin F}P(x,y),
\]

while for `y notin F` the coefficient is simply `sum_{x in F}P(x,y)`. This is (3.3). ∎

The right side is the signed `u`-flux across the finite boundary. In particular, if

\[
Pu-u=c
\tag{3.4}
\]

is a constant defect, then every finite `F` satisfies

\[
\boxed{|F|c=\operatorname{Flux}_F(u).}
\tag{3.5}
\]

Therefore any exhaustion `(F_N)` for which

\[
\frac{|\operatorname{Flux}_{F_N}(u)|}{|F_N|}\to0
\tag{3.6}
\]

forces `c=0`.

For the explicit star construction, take `F_N={0,1,...,N}`. Formula (3.3) becomes exactly

\[
(N+1)c
=\sum_{n>N}p_n(u(n)-u(0)),
\tag{3.7}
\]

whose right side tends to zero by source integrability. Thus the previous tail-flux proof is the concrete manifestation of a **universal homogeneous-space conservation law**.

The Fredholm cokernel `Sigma` in Section 2 is the infinite-volume algebraic shadow of this same counting-measure invariant.

**B12 outcome: SUCCESS.** Conservation is not an accident of symmetric star transpositions; every quotient random walk is bistochastic because the group acts by permutations.

---

## 4. B26 — hunt the sporadic case: classify every homogeneous-space pure star kernel

The previous construction used a very special group and a symmetric measure. A natural possible sporadic failure would be a **directed star**: perhaps a nonsymmetric measured group could produce different root-to-leaf and leaf-to-root probabilities and admit a hidden quasi-harmonic solution.

The next theorem rules this out completely at the quotient-kernel level.

### Theorem 4.1 — star-kernel universality for homogeneous-space walks

Let `(G,mu)` be a countable measured group, let `H<G` have infinite index, and let `X=G/H`. Let `o=H`. Assume the off-diagonal support graph of the quotient kernel `P` is a star centered at `o`, meaning

\[
P(i,j)=0\qquad
\text{for all distinct }i,j\in X\setminus\{o\}.
\tag{4.1}
\]

Then there exist `r in [0,1)` and strictly positive numbers `(p_i)_{i\ne o}` with

\[
r+\sum_{i\ne o}p_i=1
\tag{4.2}
\]

such that

\[
\boxed{
P(o,o)=r,\quad
P(o,i)=P(i,o)=p_i,\quad
P(i,i)=1-p_i.
}
\tag{4.3}
\]

In particular, **every homogeneous-space pure star kernel is automatically reversible with respect to counting measure**, even if the ambient measure `mu` is nonsymmetric.

Moreover, every quotient function `u` for which the convolution is absolutely defined at the root and which satisfies

\[
Pu=u+c
\tag{4.4}
\]

for a constant `c` must have `c=0` and must be constant.

#### Proof: irreducibility

Because `supp(mu)` semigroup-generates `G`, `supp(check(mu))=supp(mu)^{-1}` also semigroup-generates `G`: if `g^{-1}=s_1\cdots s_m` with each `s_j in supp(mu)`, then

\[
g=s_m^{-1}\cdots s_1^{-1}
\]

is a positive word in `supp(check(mu))`.

Since the `G`-action on `G/H` is transitive, the quotient Markov chain is therefore irreducible. Under the star support assumption, any path from `o` to a leaf `i` must use the direct edge `o->i`, and any return path must use `i->o`. Hence

\[
P(o,i)>0,\qquad P(i,o)>0
\tag{4.5}
\]

for every leaf `i`.

#### Proof: no directed-star asymmetry

Set

\[
a_i=P(o,i),\qquad b_i=P(i,o).
\]

By row stochasticity at leaf `i`,

\[
P(i,i)=1-b_i.
\tag{4.6}
\]

By Theorem 3.1, the column sum at `i` is also one. Because no distinct leaf can enter `i`,

\[
1=P(o,i)+P(i,i)=a_i+1-b_i,
\]

so

\[
\boxed{a_i=b_i=:p_i>0.}
\tag{4.7}
\]

Writing `r=P(o,o)`, the root row sum gives (4.2), and (4.3) follows.

There is an even more microscopic way to see why no sporadic directed case exists. Since `P` is a positive convex combination of the permutation actions of elements in `supp(check(mu))`, the zero pattern (4.1) forces every supported permutation of `X` to be either the identity or a single transposition `(o i)`: a supported permutation fixing `o` cannot move any leaf to a different leaf, hence is the identity on `X`; a supported permutation moving `o` to `i` must, by bijectivity and the forbidden leaf-to-leaf moves, swap `o` and `i`. Thus the quotient walk is necessarily a mixture of identity and root-leaf transpositions.

#### Proof: rigidity

The leaf equation in (4.4) is

\[
c=p_i(u(o)-u(i)),
\]

hence

\[
u(i)=u(o)-\frac{c}{p_i}.
\tag{4.8}
\]

Because there are infinitely many leaves and `sum_i p_i=1-r<infty`, one has `p_i->0` along every enumeration escaping finite sets. If `c!=0`, then

\[
p_i|u(i)|=|p_iu(o)-c|\longrightarrow |c|.
\tag{4.9}
\]

Absolute convergence of the root convolution requires

\[
r|u(o)|+\sum_{i\ne o}p_i|u(i)|<\infty,
\tag{4.10}
\]

but (4.9) makes the series diverge. Therefore `c=0`. Equation (4.8) then gives `u(i)=u(o)` for every leaf, so `u` is constant. ∎

### Corollary 4.2 — a larger explicit source family with arbitrary holding probability

The original `Sym_fin(N_0)` construction can be enlarged. For any

\[
0\le r<1,
\qquad
p_n>0,
\qquad
r+\sum_{n\ge1}p_n=1,
\]

put

\[
\mu_{r,p}=r\,\delta_e+\sum_{n\ge1}p_n\,\delta_{(0\,n)}.
\tag{4.11}
\]

Its support still semigroup-generates `Sym_fin(N_0)` because every star transposition has positive mass. Its quotient kernel is exactly (4.3), and Theorem 4.1 proves the literal source rigidity for every member of this whole infinite-dimensional family.

Thus the identity atom is another harmless parameter: neither its size nor the decay profile of `(p_n)` requires fine tuning.

**B26 outcome: SUCCESS.** The most obvious sporadic exception — an asymmetric directed star arising from a nonsymmetric group walk — cannot exist. The quotient geometry itself forces symmetry and the same integrability obstruction.

---

## 5. Relationship among the three methods

The three new views are the same rigidity mechanism at different levels.

1. **B1 / functional analysis.** `P-I` is Fredholm of index zero on the exact source domain. Constants span its kernel; total mass spans its cokernel.
2. **B12 / homogeneous-space geometry.** Total mass is conserved because every group element acts on `G/H` by a permutation, so every quotient kernel is doubly stochastic.
3. **B26 / zero-pattern rigidity.** If that bistochastic quotient has a pure-star off-diagonal graph, the zero pattern plus irreducibility forces it to be a symmetric mixture of root-leaf transpositions, after which source integrability kills every nonzero constant defect.

This closes a possible logical loophole in the earlier proof architecture: the conservation functional is not imported from the symmetry of the chosen ambient measure. It is intrinsic to homogeneous-space random walks.

---

## 6. Metric, status, and remaining obligations

Frozen metric:

\[
C_{E0070}\in\{0,1\},
\]

where `1` means an explicit source-valid construction and complete source-level written proof exist. It was already `1` before this run and remains

\[
\boxed{C_{E0070}:1\to1\quad\text{NO MOVEMENT}.}
\]

The new theorems materially strengthen the proof architecture but cannot move a binary metric already at its maximum.

Mathematical status remains **PROVED CANDIDATE / protocol closure open**. No mathematical gap in the source-level construction is currently identified by R7-03 self-review. Closure is not claimed because the required independent audits are still absent:

- independent P26 full-proof audit: `0/1`;
- distinct OTHER-track full-proof audit: `0/1`;
- publication novelty: `UNVERIFIED`.

R7-03 self-review is neither audit.

This is the third consecutive ordinary E0070 run with the already-saturated binary metric unchanged, so the ordinary unchanged count becomes `3`. Under the controlling protocol, the **next** R7-03 iteration must be the prescribed thinking-only stuck diagnosis rather than a fourth ordinary strengthening run. That diagnosis should treat the exact blocking obligations honestly: source proof presently complete internally, but independent audit/novelty closure remains outside this worker's self-review.

---

## 7. Dated source/literature check — 2026-09-18 UTC

- The primary arXiv record `1406.0763` still lists v2, last revised **7 July 2014**, as the current version.
- The source remains Michael Björklund, *Five remarks about random walks on groups*, Appendix II §7.1 Problem 2.
- Björklund's later *Random walks on countable groups* (Israel J. Math. 217 (2017), arXiv:1502.04038) concerns Liouville/drift, Poisson boundaries and weak mixing; the retrieved title/abstract does not state a resolution of Appendix II Problem 2.
- Bounded searches using the exact source title, exact Problem-2 wording, `G/H`, `quasi-harmonic`, homogeneous-space harmonic functions, finitary symmetric groups and star transpositions did not locate a later explicit source-matching resolution or the construction above.
- Recent star-transposition literature located in the bounded search concerns finite symmetric-group shuffles / Gray codes rather than Björklund's infinite homogeneous-space quasi-harmonic problem.

These search misses are **negative evidence only**. They do not certify novelty or worldwide openness.
