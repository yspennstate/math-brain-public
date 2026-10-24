# E0070 / Björklund Problem 2 — weighted duality and infinite-support obstructions

Date: 2026-09-17 UTC  
Worker: R7-03 Boundary-Case Research  
Scope: substantive admission-stage mathematics only; **E0070 is not admitted or claimed by R7-03**.

## Source scope

Michael Björklund, *Five remarks about random walks on groups*, arXiv:1406.0763v2 (2014), Appendix II §7.1, Problem 2, PDF p. 24:

> Construct a countable measured group `(G,mu)` and an infinite-index subgroup `H<G` such that `G/H` admits no nonconstant left `(quasi-)mu`-harmonic functions whatsoever.

The current arXiv record remains v2, last revised 7 July 2014. The source defines a left quasi-harmonic function by a constant-defect convolution equation. The results below continue the previous R7-03 theorem that **finitely supported generating measures can never solve Problem 2**.

Throughout, put `X=G/H` and use the left transition kernel induced by `check(mu)`:

\[
P(x,y)=\check\mu\{s\in G:sx=y\}.
\]

Then a left quasi-`mu`-harmonic function is a function `u` for which `Pu-u` is constant, with rowwise absolute integrability.

---

## Theorem A — exact weighted Hahn–Banach criterion for the constant-defect equation

Let `(G,mu)` be a countable measured group, let `H<G` have infinite index, and let `P` be the induced kernel above. Let

\[
v:X\to[1,\infty)
\]

satisfy

\[
Pv(x):=\sum_yP(x,y)v(y)<\infty\qquad(x\in X).
\]

For a signed sequence `z` on `X`, write

\[
\|z\|_{1,v}:=\sum_y |z_y|v(y).
\]

For finitely supported `a:X\to\mathbb R`, define

\[
T a:=aP-a,
\]

viewed as an element of `ell^1_v(X)`.

Then the following are equivalent for a constant `C<\infty`.

1. There exists `u:X->R` such that
   \[
   Pu-u=1
   \]
   pointwise and
   \[
   |u(y)|\le C v(y)\qquad(y\in X).
   \]

2. Every finitely supported signed `a` satisfies
   \[
   \boxed{\left|\sum_xa_x\right|\le C\,\|aP-a\|_{1,v}.}
   \]

Equivalently, if

\[
\kappa_v:=\inf\left\{\|aP-a\|_{1,v}:a\in c_{00}(X),\ \sum_xa_x=1\right\},
\]

where `a` is allowed to be signed, then

\[
\boxed{\kappa_v>0}
\]

is equivalent to the existence of a `v`-controlled forbidden quasi-harmonic function with constant defect `1`.

### Proof

For `x\in X`, let

\[
r_x:=P(x,\cdot)-\delta_x\in\ell^1_v(X).
\]

The first step is injectivity of `T` on `c_00(X)`. Suppose `Ta=0` for a finitely supported `a`. At a point `y`, coefficient comparison gives

\[
a_y=\sum_xa_xP(x,y)=\int_G a_{s^{-1}y}\,d\check\mu(s).
\]

If `M=max a>0`, choose `y` with `a_y=M`. The right side is a convex combination of numbers at most `M`, so

\[
a_{s^{-1}y}=M
\]

for every `s` in `supp(check(mu))`. Iteration propagates the value `M` through the whole `G`-orbit of `y`, because the support generates `G` as a semigroup. That orbit is `X`, which is infinite, contradicting finite support of `a`. If `max a=0` and `a` is nonzero, the same argument at the negative minimum gives the contradiction. Hence `a=0` and `T` is injective.

Assume (1). For finite `a`, rowwise `v`-integrability justifies the finite/infinite sum interchange:

\[
\sum_xa_x
=\sum_xa_x(Pu-u)(x)
=\sum_y(aP-a)_yu(y).
\]

Therefore

\[
\left|\sum_xa_x\right|
\le \sup_y\frac{|u(y)|}{v(y)}\sum_y|(aP-a)_y|v(y)
\le C\|aP-a\|_{1,v},
\]

which is (2).

Conversely, assume (2). Because `T` is injective, the rule

\[
L(Ta):=\sum_xa_x
\]

is a well-defined linear functional on `T(c_00(X))`. Condition (2) says that `L` has norm at most `C` in `ell^1_v`. Hahn–Banach extends `L` to a continuous functional on all of `ell^1_v(X)`. The dual of this weighted `ell^1` space is the space of functions `u` with

\[
\sup_y |u(y)|/v(y)\le C,
\]

with pairing `z -> sum_y z_yu(y)`. Thus for every `x`,

\[
1=L(r_x)=\sum_y(P(x,y)-\delta_x(y))u(y)=Pu(x)-u(x).
\]

The condition `Pv(x)<infty` and `|u|<=Cv` gives absolute convergence of every row sum, so `u` is source-admissible. This proves (1). `square`

### Meaning

The previous finite-support proof produced an algebraic functional on the row span. Theorem A identifies **exactly** what is missing when the transition rows are infinite: one needs a weight for which that algebraic functional is continuous. Thus the infinite-support problem is not merely “repeat Hahn–Banach”; it is a quantitative coercivity problem for the weighted defect `aP-a`.

---

## Theorem B — unweighted coercivity always fails

For every stochastic kernel `P` on a countable set and every starting state `o`, there exist finitely supported probability vectors `a_n` such that

\[
\boxed{\|a_nP-a_n\|_1\longrightarrow0.}
\]

Consequently, the quantity `kappa_v` from Theorem A always satisfies

\[
\boxed{\kappa_1=0.}
\]

### Proof

Set

\[
b_n=\frac1n\sum_{k=0}^{n-1}\delta_oP^k.
\]

Then `b_n` is a probability vector in `ell^1` and

\[
b_nP-b_n=\frac{\delta_oP^n-\delta_o}{n},
\]

so

\[
\|b_nP-b_n\|_1\le\frac2n.
\]

Because finitely supported probability vectors are dense in the probability simplex in `ell^1`, choose a finitely supported probability `a_n` with

\[
\|a_n-b_n\|_1\le\frac1n.
\]

Markov operators contract total variation, hence

\[
\|a_nP-a_n\|_1
\le \|b_nP-b_n\|_1
   +\|(a_n-b_n)P\|_1
   +\|a_n-b_n\|_1
\le\frac4n.
\]

Therefore the defect tends to zero. `square`

### Meaning

This gives a constructive reason that the finite-support algebraic functional cannot extend boundedly to ordinary `ell^1`: a bounded extension would create a bounded solution of `Pu-u=1`, while the Cesaro measures above explicitly drive the dual coercivity constant to zero. Any successful infinite-support continuation must therefore use a genuinely nontrivial growth weight `v`.

---

## Theorem C — real-character obstruction, valid for infinite support

Suppose there exists a nonzero homomorphism

\[
\chi:G\to\mathbb R
\]

such that `chi(H)=0` and

\[
\int_G|\chi(s)|\,d\mu(s)<\infty.
\]

Then Björklund Problem 2 cannot hold for `(G,mu,H)`.

### Proof

Because `chi(H)=0`,

\[
u(gH):=\chi(g)
\]

is well defined on `G/H`. It is nonconstant. Moreover,

\[
\begin{aligned}
Pu(gH)
&=\int_Gu(sgH)\,d\check\mu(s)\\
&=\chi(g)+\int_G\chi(s)\,d\check\mu(s)\\
&=u(gH)-\int_G\chi(t)\,d\mu(t).
\end{aligned}
\]

Absolute integrability of `chi` makes the convolution source-valid. Hence `u` is a nonconstant left quasi-`mu`-harmonic function. `square`

### Finite-first-moment corollary

Assume additionally that `G` is finitely generated and `mu` has finite first moment in a word metric. Every real character of `G` is Lipschitz in the word metric, so every real character is `mu`-integrable. Thus any candidate solution of Problem 2 must satisfy

\[
\boxed{\operatorname{Hom}(G/\!\langle\!\langle H\rangle\!\rangle,\mathbb R)=0.}
\]

If the quotient by the normal closure of `H` is finitely generated, its abelianization must therefore be finite. In particular, an infinite normal abelian quotient with finite first moment can never solve Problem 2.

This is not claimed novel; it is a direct source-compatible obstruction that becomes useful only after the finite-support route has been eliminated.

---

## Residual structure after the two R7-03 runs

Any still-plausible source-level construction must now evade all of the following:

1. **Finite support is impossible** (previous R7-03 theorem).
2. **Any `mu`-integrable real character annihilating `H` is impossible** (Theorem C).
3. **Any row-integrable weight `v` with `kappa_v>0` is impossible** (Theorem A), because it manufactures `Pu-u=1`.
4. The unweighted route cannot certify such a function because `kappa_1=0` universally (Theorem B).
5. Independently, the source already requires the bounded left harmonic sector on `G/H` to be trivial.

So the actual infinite-support escape regime is sharply localized: the candidate must have trivial bounded boundary, no integrable descending character, and failure of weighted defect coercivity for every admissible growth weight one can use to control the convolution.

A natural future hard-target metric, **if another worker lawfully admits E0070 as HARD**, is

\[
\sup_v\kappa_v
\]

over an explicitly frozen class of row-integrable weights. R7-03 does **not** adopt that metric here because this slot is restricted to CLOSABLE admission and E0070 remains HARD.

## Dated literature check

Checked 2026-09-17 UTC.

- Primary record: arXiv:1406.0763v2; submitted 3 June 2014, last revised 7 July 2014.
- A bounded exact-title/problem search located later papers citing Björklund's notes, including 2025 work on Poisson boundaries, but no explicit source-matching resolution of Appendix II Problem 2.
- A 2025 preprint on Lipschitz Liouville/affine rigidity concerns controlled-growth harmonic functions and does not, in the bounded search performed here, state a solution of the full homogeneous-space “no nonconstant harmonic or quasi-harmonic functions whatsoever” problem.

These are **negative search results only**, not proof of current openness and not a novelty certificate for the lemmas above.
