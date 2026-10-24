# MOC4 account03/B08 r11b — exact upper-facet refutation and forest-Givens convex lift

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex normal 4-by-4 Marcus–de Oliveira determinant hull  
**Worker:** account03/B08  
**Outcome:** `CANDIDATE_REFUTED + ESSENTIAL_STEP_APPLIED` at the auxiliary-route level; the parent MOC4 target remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact current target and peer state used

For complex normal 4-by-4 matrices `A,B`, with spectra `a_1,...,a_4` and `b_1,...,b_4`, the target is

\[
\det(A+B)\in \operatorname{conv}\{v_\sigma(a,b):\sigma\in S_4\},\qquad
v_\sigma(a,b)=\prod_{i=1}^4(a_i+b_{\sigma(i)}).
\]

This run directly consumed two completed peer results.

1. The team lead account03/B07 report `MOC4-DRURY-UPPER-FACET-v1`, scientific report commit `d88d24810cbff886676fd38134b24233050c0314`, reduced one sufficient route to the 288 exceptional Drury-facet inequalities
\[
u(F_{\rho_1,\rho_2})\le \max_\sigma F(\sigma),\qquad F(\sigma)=\Re(\eta v_\sigma),
\]
with one explicit representative
\[
3u(f)=f(2134)+f(3214)+f(1432)+f(4321)-f(1234).
\]
2. The assigned other-account partner account04/B09 report at scientific commit `6c116abdc4e257434eef09e52608ab5e34c3c49c` refuted an unrestricted common `(P,R)` permutation lift and proved the exact structured coefficient identities, including `det Gtilde=-(1/2) Delta(a) Delta(b)`. This run therefore did not return to a spectrum-independent bistochastic lift.

A newer lead handoff published during this invocation, `MOC4-PARITY-SLACK-v1`, replaces the upper-facet route by an exact six-fiber mixed-support reduction. The upper-facet refutation below remains useful because it permanently closes the preceding sufficient cone route rather than leaving it as an apparent alternative.

## 2. Exact generic refutation of `MOC4-DRURY-UPPER-FACET-v1`

Take support direction `eta=1` and the exact Gaussian-integer spectra

\[
\begin{aligned}
a&=(-76+69i,\ 12+8i,\ -143i,\ -i),\\
b&=(-13+85i,\ 49+4i,\ -140+117i,\ 40-16i).
\end{aligned}
\]

Both spectra are simple and all eight displayed spectral values are nonzero. Exact enumeration gives 24 distinct complex permutation products `v_sigma`, and their 24 real parts are also distinct. Hence the support maximum for `F(sigma)=Re(v_sigma)` is unique. It occurs at `sigma=4321` with

\[
M=F(4321)=44,569,469.
\]

For the exceptional Drury functional above, the five needed exact real parts are

\[
\begin{array}{c|r}
\sigma & F(\sigma)\\ \hline
2134&44,318,564\\
3214&41,579,094\\
1432&37,803,352\\
4321&44,569,469\\
1234&32,810,794.
\end{array}
\]

Therefore

\[
3u(F)=135,459,685,
\]
and
\[
3\bigl(u(F)-M\bigr)=135,459,685-3(44,569,469)=1,751,278>0.
\]
Thus

\[
\boxed{u(F)-M=\frac{1,751,278}{3}>0.}
\]

Equivalently, for `g=M-F`,

\[
u(g)=M-u(F)=-\frac{1,751,278}{3}<0,
\]
so `g` is not in the nonnegative Drury cylinder cone used by that sufficient route.

This **refutes `MOC4-DRURY-UPPER-FACET-v1` as a universal spectral inequality**, including on a simple, nonzero, uniquely exposed generic spectrum. It does **not** refute MOC4: failure of this cone certificate only means that the determinant support inequality, if true, needs the more detailed unitary/structured mechanism now being pursued by the lead's parity-slack reduction.

## 3. New exact theorem: a large true-unitary family has an honest convex lift

The assigned B08 task is to search for genuine unitary/spectrum counterexample candidates. The following theorem removes a broad finite-mixing family from that search.

### Theorem (`MOC4-GIVENS-FOREST-LIFT-v1`)

Let `T` be a forest on the coordinate set `{1,...,n}`. List distinct edges `e_1,...,e_m` of `T` in an arbitrary order and, for each `e_k={p_k,q_k}`, let `G_k` be a two-level `SU(2)` unitary supported on those two coordinates, with active block

\[
\begin{pmatrix}
\alpha_k&-\overline{\beta_k}\\
\beta_k&\overline{\alpha_k}
\end{pmatrix},\qquad |\alpha_k|^2+|\beta_k|^2=1.
\]

Set
\[
U=G_1G_2\cdots G_m.
\]
Define the determinantal quasidistribution
\[
\mu_\sigma(U)=\operatorname{sgn}(\sigma)\prod_{i=1}^n u_{i,\sigma(i)}.
\]
Then every `mu_sigma(U)` is real and nonnegative, the nonzero coefficients are indexed by subsets of the forest edges, and

\[
\{\mu_\sigma(U):\mu_\sigma\ne0\}
=
\left\{
\prod_{k=1}^m |\alpha_k|^{2(1-\epsilon_k)}|\beta_k|^{2\epsilon_k}:
\epsilon\in\{0,1\}^m
\right\},
\]
with the natural subset-to-permutation indexing. In particular
\[
\sum_\sigma\mu_\sigma=\prod_{k=1}^m(|\alpha_k|^2+|\beta_k|^2)=1.
\]
For nondegenerate gates all `2^m` subset weights are positive.

Consequently, for every pair of complex spectra `a,b`,
\[
\det(D_a+UD_bU^*)=\sum_{\sigma\in S_n}\mu_\sigma(U)\prod_i(a_i+b_{\sigma(i)})
\]
is an **actual convex combination** of the permutation products. In particular MOC4 holds for every 4-by-4 coupling unitary that admits such a one-use forest-Givens factorization.

### Proof

Induct on `m`. The statement is trivial for `m=0`. Let the last forest edge be `e_m={p,q}` and write `U=U'G_m`. Because removing an edge from a forest separates its endpoints, `p` and `q` lie in distinct connected components `C_p,C_q` of the graph formed by the first `m-1` edges. Every earlier two-level rotation acts inside one of those components, hence `U'` is block diagonal with respect to the component partition.

Right multiplication by `G_m` changes only columns `p,q`. For a row in `C_p`, the new `p`-column entry acquires the factor `alpha_m` and the new `q`-column entry the factor `-conj(beta_m)`; for a row in `C_q`, the corresponding factors are `beta_m` and `conj(alpha_m)`.

A nonzero determinant-permutation monomial has only two possibilities.

* **No crossing between `C_p` and `C_q`.** Then column `p` is used from `C_p` and column `q` from `C_q`. Relative to a nonzero permutation monomial of `U'`, the product acquires `alpha_m conj(alpha_m)=|alpha_m|^2`, with no sign change.
* **One crossing each way.** Since `p,q` are the only columns that connect the two blocks after multiplication, bijectivity forces exactly one `C_p` row to use column `q` and exactly one `C_q` row to use column `p`. Swapping those two target columns produces a unique nonzero block-preserving permutation monomial of `U'`. The entry product contributes `(-conj(beta_m)) beta_m=-|beta_m|^2`, while the target-column transposition flips the permutation sign by another factor `-1`. The quasidistribution coefficient therefore acquires `+|beta_m|^2`.

There are no other nonzero crossing patterns. Hence each preceding coefficient splits into two nonnegative children with multipliers `|alpha_m|^2` and `|beta_m|^2`. Iterating gives the stated product weights. Since a subset of edges of a forest is again a forest, the corresponding ordered products of the chosen edge transpositions are distinct; equivalently, each nontrivial connected component of a chosen edge subset yields one cycle on exactly its vertex set. Thus the subset indexing has no collisions in the nondegenerate case. Summing the weights gives one.

Finally, because every `G_k` has determinant one, `U in SU(n)`. The standard determinantal expansion
\[
\det(D_a+UD_bU^*)=\sum_\sigma \mu_\sigma(U)v_\sigma(a,b)
\]
then turns the nonnegative normalized `mu` into the asserted convex representation. QED.

## 4. Consequence for genuine finite-mixing counterexample search

For `n=4`, any word of three **distinct** two-level rotations whose support edges form a spanning tree is automatically inside the 24-vertex hull for every spectra and every gate phase. Thus the previous one-plane result is not isolated: all one-use acyclic mixing is harmless.

This narrows a genuine finite-mixing adversary. A counterexample produced by a Givens word cannot arise from the one-use forest mechanism; it must involve a cycle in the interaction graph, a repeated edge, or a different representation whose determinantal quasidistribution is not covered by the theorem.

The forest condition is genuinely restrictive. For the real rotation
\[
R=\begin{pmatrix}3/5&-4/5\\4/5&3/5\end{pmatrix}
\]
and the four-edge word on `(12),(23),(34),(14)`, the interaction graph contains one cycle. Exact rational arithmetic still gives `sum mu_sigma=1`, but the minimum coefficient is
\[
\boxed{-\frac{186624}{9765625}<0.}
\]
(and several coefficients are negative). This is **not** a counterexample to MOC4; it only shows that the automatic positive-lift proof can break as soon as a cycle is introduced.

## 5. Exact verification

The companion standard-library verifier performs three independent finite checks:

1. exact Gaussian-integer arithmetic for the upper-facet witness, including all 24 vertices, uniqueness of the maximizing real part, and the positive gap `1,751,278/3`;
2. exact symbolic polynomial expansion for all 16 labeled spanning trees of `K_4` and all 6 orders of their three edges (96 words): each word has exactly eight nonzero determinant quasidistribution monomials, each with coefficient `+1` and even gate-variable exponents, and their sum is exactly `prod_k(c_k^2+s_k^2)`;
3. exact `Fraction` arithmetic for the four-edge cycle witness and the negative minimum `-186624/9765625`.

These finite checks support the algebraic theorem; they are not a substitute for its induction proof.

## 6. Current proof chain and next obligation

The parent MOC4 problem remains open. The run changes the shared search in two ways:

- the prior universal Drury upper-facet sufficient condition is now rigorously dead, so it should not be used as an alternative closure route;
- the true-unitary adversary search can exclude all one-use forest-Givens words exactly.

The current lead has moved to `MOC4-PARITY-SLACK-v1`, an exact six-fiber condition using the structured mixed-support block. A high-value next B08 attack is therefore: search the first genuinely cyclic/repeated-edge true-unitary family, with simple complex spectra and a common separating support direction, while checking the lead's exact six-fiber/parity-slack quantity. Failure of that sufficient gate is not itself a MOC4 counterexample; a target-level disproof still requires a determinant support value strictly beyond all 24 permutation products in one direction.

Recommended recipients: account03/B07 lead, assigned partner account04/B09, account01/B07, account02/B07, account04/B08, and account03/B20.

No benchmark gold/keys, credentials, scheduler identifiers, machine paths, unrelated private material, email/Drive/public dispatch, paid API/model, Codex, or remote workflow was used.
