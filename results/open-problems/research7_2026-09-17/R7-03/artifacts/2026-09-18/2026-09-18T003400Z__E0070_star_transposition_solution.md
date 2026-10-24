Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning telemetry or binding model/effort selector is exposed.

# E0070 / Björklund Problem 2 — explicit finitary-symmetric star-transposition solution

Date: 2026-09-18 UTC  
Worker: R7-03 Boundary-Case Research  
Canonical target: E0070  
Formal claim: `operations/claims/E0070.md`  
Source: Michael Björklund, *Five remarks about random walks on groups*, arXiv:1406.0763v2, Appendix II §7.1, Problem 2, printed p.24.

## 1. Source problem

Björklund asks for a countable measured group `(G,mu)` and an infinite-index subgroup `H<G` such that the homogeneous space `G/H` has **no nonconstant left (quasi-)mu-harmonic functions whatsoever**. In the paper, a measured group means that `supp(mu)` generates `G` as a semigroup. Left convolution uses the reflected measure `check(mu)`.

The construction below uses a symmetric measure, so `check(mu)=mu` and there is no left/right measure-orientation ambiguity.

## 2. Construction

Let

\[
X=\mathbb N_0=\{0,1,2,\ldots\}.
\]

Let

\[
G=\operatorname{Sym}_{\mathrm{fin}}(X)
\]

be the group of all permutations of `X` with finite support, and let

\[
H=\operatorname{Stab}_G(0)=\{g\in G:g(0)=0\}.
\]

For every integer `n>=1`, put

\[
\tau_n=(0\ n).
\]

Choose any sequence

\[
p_n>0,\qquad \sum_{n=1}^{\infty}p_n=1,
\]

and define a probability measure on `G` by

\[
\mu(\tau_n)=p_n,\qquad n\ge1,
\]

with zero mass elsewhere. A completely explicit choice is

\[
p_n=2^{-n}.
\]

We prove that **every complex-valued, source-valid left constant-defect / quasi-harmonic function on `G/H` is constant**.

## 3. Verification of the measured-group hypotheses

### Lemma 3.1 — `G` is countable

Every finitary permutation has support contained in `{0,1,...,m}` for some finite `m`. Hence

\[
G=\bigcup_{m\ge0}\operatorname{Sym}(\{0,1,\ldots,m\}),
\]

which is a countable union of finite sets. Thus `G` is countable.

### Lemma 3.2 — `supp(mu)` semigroup-generates `G`

Each `tau_n` is an involution. For distinct `i,j>=1`,

\[
\tau_i\tau_j\tau_i=(i\ j),
\]

because conjugating `(0 j)` by `(0 i)` sends the pair `{0,j}` to `{i,j}`. Together with the star transpositions `(0 n)` themselves, this produces **every transposition** of `X` having finite support. Every finitary permutation is a finite product of transpositions. Therefore

\[
\langle \operatorname{supp}(\mu)\rangle_{\rm semigroup}=G.
\]

So `(G,mu)` is a measured group in the exact sense used by the source.

### Lemma 3.3 — `mu` is symmetric

Since every `tau_n` is an involution,

\[
\tau_n^{-1}=\tau_n.
\]

Therefore

\[
\check\mu=\mu.
\]

### Lemma 3.4 — `H` has infinite index and `G/H` is canonically `X`

Define

\[
\Psi:G/H\longrightarrow X,\qquad \Psi(gH)=g(0).
\]

This is well-defined: if `gH=g'H`, then `g'=gh` for some `h in H`, so `g'(0)=g(h(0))=g(0)`. Conversely, if `g(0)=g'(0)`, then `g^{-1}g'` fixes `0`, hence lies in `H`, so `gH=g'H`. It is surjective because `tau_n(0)=n` and the identity sends `0` to `0`.

Thus

\[
G/H\cong\mathbb N_0,
\]

so

\[
[G:H]=\infty.
\]

## 4. Exact induced Markov kernel

Under the bijection above, left multiplication by `tau_n` acts on a state `x in X` exactly as the permutation `tau_n`:

\[
\tau_n\cdot(gH)=(\tau_n g)H
\quad\Longleftrightarrow\quad
x=g(0)\mapsto \tau_n(x).
\]

Because `check(mu)=mu`, the left convolution operator is therefore

\[
(Pu)(x)=\sum_{n\ge1}p_n u(\tau_n x).
\]

At the center `0`, every star transposition sends `0` to its own leaf, so

\[
\boxed{(Pu)(0)=\sum_{n\ge1}p_nu(n).}
\tag{4.1}
\]

At a fixed leaf `k>=1`, only `tau_k` moves `k`, sending it to `0`; every `tau_n` with `n\ne k` fixes `k`. Hence

\[
\boxed{(Pu)(k)=p_k u(0)+(1-p_k)u(k).}
\tag{4.2}
\]

This is the exact infinite-star kernel.

## 5. Full theorem: every integrable constant-defect solution is constant

### Theorem 5.1

Let `u:X->C` be such that the left convolution is source-valid (in particular the center integral in (4.1) is absolutely defined) and suppose for some constant `c in C` that

\[
Pu=u+c.
\tag{5.1}
\]

Then `c=0` and `u` is constant.

Consequently, `G/H` admits no nonconstant left harmonic functions and no nonconstant left quasi-`mu`-harmonic functions in the source sense.

### Proof

Fix a leaf `k>=1`. Combining (4.2) with (5.1) gives

\[
p_k u(0)+(1-p_k)u(k)=u(k)+c.
\]

Subtract `(1-p_k)u(k)` from both sides:

\[
p_k u(0)=p_k u(k)+c.
\]

Since `p_k>0`,

\[
\boxed{u(k)=u(0)-\frac{c}{p_k}.}
\tag{5.2}
\]

Now use source-validity at the center. The probability integral in (4.1) must exist as a complex Lebesgue integral, hence

\[
\sum_{n\ge1}p_n|u(n)|<\infty.
\tag{5.3}
\]

If `c\ne0`, then by (5.2),

\[
p_n|u(n)|
=
|p_nu(0)-c|.
\tag{5.4}
\]

Because `(p_n)` is a positive summable sequence, `p_n->0`. Therefore

\[
|p_nu(0)-c|\longrightarrow |c|>0.
\]

In particular the summands in (5.3) do not even tend to zero, so the series cannot converge. This contradicts source integrability. Hence

\[
\boxed{c=0.}
\]

Returning to (5.2),

\[
u(k)=u(0)\qquad\text{for every }k\ge1.
\]

Therefore `u` is constant on all of `X`. ∎

## 6. Matching the source's quasi-harmonic normalization

The source's group-level definition writes the defect as the single integral appearing at the identity,

\[
\int u(sg)\,d\check\mu(s)
=
u(g)+\int u(s)\,d\check\mu(s).
\]

On a homogeneous space with basepoint `H`, the analogous normalized notion is a special case of (5.1): it has one constant defect determined by the basepoint convolution (and, under the literal normalization, forces the basepoint value to be zero). Theorem 5.1 proves the stronger assertion that **every** source-integrable solution with an arbitrary constant defect is constant. Therefore it covers either standard normalization of quotient quasi-harmonicity and in particular the exact source problem.

For ordinary left harmonicity, simply take `c=0` in Theorem 5.1. No boundedness assumption is used anywhere.

## 7. B2 — attack the negation

Assume a forbidden nonconstant quasi-harmonic function exists. The leaf equation has no flexibility: every leaf value must be

\[
u(k)=u(0)-c/p_k.
\]

Thus the only possible nonconstant candidate is forced to grow like `1/p_k`. But multiplying by the transition mass `p_k` makes every leaf contribute asymptotically the **same nonzero defect** `-c` to the center convolution. Infinite multiplicity, not a delicate tail estimate, destroys integrability. If the defect is zero, every leaf collapses to the center value.

Outcome: the negation is impossible.

## 8. B18 — translate the statement

The group-theoretic problem becomes elementary after choosing a transitive finitary permutation action. The coset bijection

\[
G/H\cong\operatorname{Orb}_G(0)=\mathbb N_0
\]

translates convolution by star transpositions into an infinite-star Markov chain. The hard-looking homogeneous-space harmonicity question then reduces exactly to equations (4.1)–(4.2).

Outcome: a source-level group problem is reduced without loss to a two-row-type Markov kernel.

## 9. B25 — bijection / repeated-defect counting

The coset-orbit bijection is exact, and equation (5.4) exposes the decisive counting invariant. A nonzero defect would appear once per leaf in the center integral:

\[
p_nu(n)=p_nu(0)-c.
\]

There are infinitely many leaves. Hence the defect is counted infinitely many times with asymptotically constant magnitude. This is the global obstruction that finite stars lack and exactly explains why the preceding finite-support impossibility theorem pointed toward infinite support.

Outcome: the infinite-support geometry supplies the missing source construction rather than merely evading the previous obstruction.

## 10. Strengthening and scope

The proof did not use the special choice `p_n=2^{-n}` except to make one explicit probability law. It proves the following family statement:

> For **every** strictly positive probability vector `(p_n)_{n>=1}`, the star-transposition measure on `Sym_fin(N_0)` has the property that the quotient by `Stab(0)` admits no nonconstant source-integrable left constant-defect functions.

This is stronger than needed for Problem 2. The full source question needs only one example; `p_n=2^{-n}` is a completely explicit one.

The result does **not** claim publication novelty. The dated bounded literature search found no explicit source-matching resolution, but a search miss is negative evidence only.

## 11. Protocol status

Mathematical source verdict from this artifact: **PROVED CANDIDATE**.  
Frozen metric: `C_E0070: 0 -> 1`.  
Independent P26 audit: `0/1`.  
Distinct OTHER-track audit: `0/1`.  
Self-contained paper package: not yet created in this run.  
Therefore protocol closure remains open even though the source-level proof is complete on the page.
