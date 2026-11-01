Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# P0169 — degree-five sparse duals, a twelve-variable rigidity reduction, and top-support obstructions

Target: Ryan O'Donnell, *Open Problems in Analysis of Boolean Functions* (2012), PDF p. 9, **“Linear Coefficients versus Total Degree.”**

Methods this iteration: **B6 / B12 / B26**.  Frozen source metric entering and leaving this artifact: `D_weak=4`.  The results below do **not** prove or refute the complete degree-five case; they reduce the first possible counterexample substantially and give two exact all-dimensional obstructions that it must satisfy.

## 1. Setup and the dyadic gap at degree five

Let

\[
f:\{-1,1\}^n\to\{-1,1\},\qquad \deg f\le 5,
\]

and write `a_S=\widehat f(S)`.  Flip input coordinates so that every nonzero singleton coefficient is nonnegative.  This preserves Booleanity and Fourier degree, and turns the source quantity into

\[
L(f):=\sum_i a_{\{i\}}=\sum_i |\widehat f(\{i\})|.
\]

The previously proved Boolean coefficient-granularity lemma says that every nonconstant Fourier coefficient of a Boolean degree-`d` function belongs to `2^{1-d} Z`.  Hence at degree five

\[
a_{\{i\}}\in \frac1{16}\mathbb Z,
\qquad
L(f)\in \frac1{16}\mathbb Z.
\tag{1.1}
\]

Moreover

\[
\left(\frac{35}{16}\right)^2=\frac{1225}{256}<5
<\frac{1296}{256}=\left(\frac{36}{16}\right)^2.
\tag{1.2}
\]

Therefore any counterexample to the source inequality `L(f)<=sqrt(5)` must satisfy the discrete jump

\[
\boxed{L(f)\ge \frac{36}{16}=\frac94.}
\tag{1.3}
\]

This gap is used repeatedly below.

## 2. Exact Hamming-layer representation for degree at most five

Let `h:{-1,1}^m->{-1,1}` have degree at most five.  On the Hamming layer with exactly `k` negative coordinates, let `b_k` be the number of points where `h=+1`.  Permutation averaging preserves the signed singleton sum.  Set

\[
r_k=\frac{b_k}{\binom mk}.
\]

The symmetrized function has degree at most five, so `r_k` is the restriction to `k=0,...,m` of a polynomial of degree at most five.  Write it in normalized Newton form

\[
r(k)=\sum_{j=0}^{5}u_j\frac{\binom{k}{j}}{\binom{m}{j}}.
\tag{2.1}
\]

Multiplying by `\binom mk` and using

\[
\binom mk\frac{\binom kj}{\binom mj}=\binom{m-j}{k-j}
\]

gives

\[
b_k=\sum_{j=0}^{5}u_j\binom{m-j}{k-j}.
\tag{2.2}
\]

The first six equations are triangular with diagonal one, so every `u_j` is an integer for an actual Boolean function, although the next two identities need only linearity.

If `K~Bin(m,1/2)`, then

\[
L(h)=\mathbb E\!\left[h(X)(m-2K)\right]
     =2\,\mathbb E\!\left[r(K)(m-2K)\right],
\]

because `E(m-2K)=0`.  Also

\[
\mathbb E\!\left[\frac{\binom Kj}{\binom mj}(m-2K)\right]
=-\frac{j}{2^j}.
\]

Consequently

\[
\boxed{L(h)=-u_1-u_2-\frac34u_3-\frac12u_4-\frac5{16}u_5.}
\tag{2.3}
\]

The exact checker archived with this run verifies the sparse representations below by matching all six Newton-basis coefficients in (2.3), using `fractions.Fraction` only.

## 3. B26: an exact eleven-variable dual and a complete `m<=11` theorem

For `m=11`, the following identity is exact for every degree-at-most-five Boolean function:

\[
\boxed{
L(h)=\frac{b_0-b_{11}}{16}+\frac{b_3-b_8}{80}.
}
\tag{3.1}
\]

Indeed, substituting (2.2) into the right-hand side and collecting `u_0,...,u_5` gives exactly the coefficient vector

\[
(0,-1,-1,-3/4,-1/2,-5/16),
\]

which is (2.3).  This is also checked coefficient-for-coefficient by the archived exact script.

Since `0<=b_k<=\binom{11}{k}`,

\[
L(h)
\le \frac1{16}+\frac{\binom{11}{3}}{80}
=\frac1{16}+\frac{165}{80}
=\boxed{\frac{17}{8}}.
\tag{3.2}
\]

And

\[
\left(\frac{17}{8}\right)^2=\frac{289}{64}<5.
\]

Padding a function with dummy variables does not alter its degree or singleton sum.  Hence (3.2) proves

\[
\boxed{
\deg h\le5,\quad h\text{ depends on at most 11 coordinates}
\quad\Longrightarrow\quad
L(h)\le\frac{17}{8}<\sqrt5.
}
\tag{3.3}
\]

This is a complete finite-dimensional theorem, not an extrapolation from enumeration.

## 4. All-dimensional active-support reduction

Return to an arbitrary oriented degree-five Boolean function `f` and let

\[
A=\{i:a_{\{i\}}>0\},\qquad |A|=q.
\]

Fix all coordinates outside `A`.  If the outside assignment is `y`, denote the resulting Boolean function on `A` by `f_y`.  For each `i in A`, averaging the restricted singleton coefficient over uniform `y` returns the original coefficient:

\[
\mathbb E_y\,\widehat{f_y}(\{i\})=a_{\{i\}}.
\]

Therefore

\[
\mathbb E_y\sum_{i\in A}\widehat{f_y}(\{i\})=L(f).
\tag{4.1}
\]

Some restriction has signed singleton sum at least `L(f)`.  If `q<=11`, (3.3) forces that sum to be at most `17/8<sqrt(5)`.  Thus every source counterexample must obey

\[
\boxed{|A|\ge12.}
\tag{4.2}
\]

More generally, applying the same argument to any chosen `T subset A` of size eleven gives the local inequality

\[
\boxed{
\sum_{i\in T}a_{\{i\}}\le\frac{17}{8}
\qquad (|T|=11).
}
\tag{4.3}
\]

Equation (4.3) is valid in arbitrary ambient dimension.

## 5. B26: exact twelve-variable dual and the isolated `9/4` obstruction

For `m=12`, a second exact identity is

\[
\boxed{
L(h)=
\frac{13}{288}(b_0-b_{12})
+\frac1{180}(b_3-b_9)
+\frac1{480}(b_4-b_8).
}
\tag{5.1}
\]

Again, substitution of (2.2) gives exactly the six coefficients in (2.3); the archived exact script checks this over the full Newton basis.

Using only `0<=b_k<=\binom{12}{k}` yields

\[
\begin{aligned}
L(h)
&\le \frac{13}{288}
 +\frac{\binom{12}{3}}{180}
 +\frac{\binom{12}{4}}{480}\\
&=\frac{13}{288}+\frac{220}{180}+\frac{495}{480}
=\boxed{\frac{331}{144}}.
\end{aligned}
\tag{5.2}
\]

Now

\[
\frac{331}{144}<\frac{37}{16}.
\]

Because `L(h)` is a multiple of `1/16`, (5.2) sharpens discretely to

\[
\boxed{L(h)\le\frac{36}{16}=\frac94}
\qquad (m=12).
\tag{5.3}
\]

This does **not** prove the source inequality at twelve variables, because `9/4>sqrt(5)`.  Instead it isolates a single possible violating lattice value.

### Rigidity if a twelve-active-coordinate counterexample exists

Suppose an arbitrary source counterexample has exactly twelve active singleton coordinates.  By (4.1), one outside restriction has signed mass `>sqrt(5)`.  Reorient the twelve remaining coordinates.  Its `l1` singleton mass is at least that signed mass, while (5.3) applies after reorientation.  The dyadic gap (1.2) therefore forces

\[
L=\frac94.
\tag{5.4}
\]

Let its oriented singleton coefficients be `a_1,...,a_12`.  Restrict coordinate `j` to `+1` and `-1`.  The average of the two signed singleton sums on the remaining eleven coordinates is

\[
L-a_j.
\]

Each eleven-variable restriction is bounded by `17/8` from (3.2).  Hence

\[
\frac94-a_j\le\frac{17}{8},
\]

so

\[
\boxed{a_j\ge\frac18\quad\text{for every }j=1,...,12.}
\tag{5.5}
\]

Thus the smallest possible active-support counterexample is not arbitrary: it must have exactly total singleton mass `9/4`, with all twelve singleton coefficients at least `1/8` and all of them dyadic multiples of `1/16`.

## 6. B6: deformation to degree four through a weighted top-degree vertex cover

Let `H_5` be the 5-uniform hypergraph on the active coordinates whose edges are the 5-sets `S` with `a_S != 0`.

Let `C` be **any** vertex cover of `H_5`.  Fix the coordinates in `C`.  Every degree-five monomial uses at least one coordinate of `C`, so after restriction every resulting function on the coordinates outside `C` has Fourier degree at most four.

The previous R7-02 theorem at degree four is uniform in the number of variables and states that every Boolean degree-four function has signed singleton sum at most `2`.  Hence, for every assignment `y` to `C`,

\[
\sum_{i\notin C}\widehat{f_y}(\{i\})\le2.
\]

Average over `y`.  Restricted singleton coefficients average to the original ones, giving

\[
\boxed{
\sum_{i\notin C}a_{\{i\}}\le2
\qquad\text{for every vertex cover }C\text{ of }H_5.
}
\tag{6.1}
\]

If `f` violates the degree-five source inequality, then `L(f)>=9/4` by (1.3), and therefore every such cover satisfies

\[
\boxed{
\sum_{i\in C}a_{\{i\}}\ge\frac14.
}
\tag{6.2}
\]

This is a genuine all-dimensional obstruction.  It is deliberately stated as a **weighted** cover condition; it does not by itself imply an unweighted covering-number lower bound.

## 7. B12: exact top-degree convolution constraints from `f^2=1`

Booleanity gives `f^2=1`, so for every nonempty `R`,

\[
0=\widehat{f^2}(R)
 =\sum_{S\subseteq[n]} a_S a_{S\triangle R}.
\tag{7.1}
\]

Because `a_S=0` for `|S|>5`, the largest symmetric-difference sizes become especially rigid.

### Ten-set identity

Fix `|R|=10`.  If both `|S|<=5` and `|S triangle R|<=5`, equality in the triangle-size bound forces `S subset R`, `|S|=5`, and `S triangle R=R\S`.  Thus

\[
\boxed{
\sum_{\substack{S\subset R\\|S|=5}} a_S a_{R\setminus S}=0
\qquad(|R|=10).
}
\tag{7.2}
\]

In particular, a 10-set cannot contain exactly one complementary pair of nonzero top-degree coefficients: at least one further complementary partition must participate so that the signed products cancel.

### Nine-set identity

Fix `|R|=9`.  The same size argument leaves exactly the `(4,5)` and `(5,4)` complementary pairs.  Pairing the two orientations gives

\[
\boxed{
\sum_{\substack{S\subset R\\|S|=4}} a_S a_{R\setminus S}=0
\qquad(|R|=9).
}
\tag{7.3}
\]

Equations (7.2)-(7.3) are exact source-level algebraic constraints on the top two Fourier layers.  They provide the cancellation condition that a future attempt must combine with the weighted-cover obstruction (6.2).

## 8. Exact checker and what it certifies

The exact checker is

`research7_2026-09-17/R7-02/artifacts/2026-09-19/p0169_degree5_sparse_dual_checker.py`.

It uses Python `fractions.Fraction` and verifies:

1. the Newton-basis objective vector (2.3);
2. identity (3.1) coefficient-for-coefficient;
3. the exact bound `17/8` and `289/64<5`;
4. identity (5.1) coefficient-for-coefficient;
5. the exact continuous bound `331/144`;
6. `331/144<37/16` and the dyadic gap `(35/16)^2<5<(36/16)^2`;
7. the equality-rigidity numerical gap `9/4-17/8=1/8`.

The archived execution output ends with `ASSERTIONS_PASS`.  These exact checks support the finite algebra above; the all-dimensional conclusions (4.2), (4.3), (6.1), (6.2), (7.2), and (7.3) are written proofs and are not inferred from computation.

## 9. Status and exact remaining gap

The frozen source metric remains

`D_weak: 4 -> 4` (**NO MOVEMENT**).

The source quantifies over all `d` and all ambient dimensions, so the degree-five case is still unproved and unrefuted.  What this iteration establishes is substantially narrower search geometry:

- any counterexample must have at least twelve active singleton coordinates;
- an exactly-twelve-active-coordinate counterexample must have singleton mass exactly `9/4` and every singleton coefficient at least `1/8`;
- every eleven active singleton coefficients carry total mass at most `17/8`;
- every vertex cover of the top-degree support hypergraph has singleton weight at least `1/4` in a counterexample;
- the level-five support obeys the exact complementary-cancellation identities (7.2)-(7.3).

The simplest unresolved case is therefore the existence or impossibility of the twelve-variable rigidity object just described.  The sparse Hamming-layer dual alone stops at `9/4`, strictly above `sqrt(5)`; the weighted-cover and convolution identities have not yet been combined into a contradiction.

If the next research iteration proceeds on P0169, the nonrepeating planned methods are **B5 / B15 / B28**: introduce a bias parameter and extract a derivative/variance constraint at the isolated `9/4` boundary; deliberately break permutation symmetry in the twelve-variable rigidity object; and analyze random restrictions of the level-five support to convert the weighted-transversal obstruction into a quantitative loss of singleton mass.
