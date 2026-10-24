Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated binding model/effort selector or runtime telemetry is exposed.

# F0011 — balanced low-corank cuts and an all-corank sign-Gram reduction

Date: 2026-09-19 UTC  
Role: C05 / R7-06, native ID `6aabe827777c8191a43330b4a87d481d`  
Target: Van H. Vu, *Recent progress in combinatorial random matrix theory*, Conjecture 9.4  
Status: **PROVED PARTIAL** toward the source conjecture; no source-level closure or novelty claim.

## 1. Source and inherited bottleneck

For the symmetric Rademacher matrix `M_n^sym` (the diagonal and upper-triangular entries are independent fair signs, with symmetry below the diagonal), Vu's Conjecture 9.4 asks for

\[
\Pr\bigl(\operatorname{Spec}(M_n^{\rm sym})\subset\mathbb Z\bigr)
=2^{-(1/2+o(1))n^2}.
\tag{1.1}
\]

The latest R7-06 checkpoint reduced the clean two-eigenvalue boundary to half-completion equations. Write `N=2r` and

\[
H=\begin{pmatrix}P&C\\C^T&D\end{pmatrix}=H^T\in\{\pm1\}^{N\times N},
\qquad H^2=N I_N.
\tag{1.2}
\]

Then

\[
P^2+CC^T=NI_r,\qquad PC+CD=0,\qquad C^TC+D^2=NI_r.
\tag{1.3}
\]

For a fixed first half `P`, put

\[
K_P:=NI_r-P^2=CC^T.
\tag{1.4}
\]

The previous report handled positive-definite sign Gram fibers exactly and proved a generic corank-one completion bound, but left repeated nonzero singular values as a possible exceptional singular locus. The purpose here is to remove that exception **for the conditioned half-completion problem**, and then prove that every matrix in the two-eigenvalue family has some balanced cut whose cross block has only `O(sqrt N)` corank. This makes the entire singular endpoint a subquadratic overhead relative to positive-definite sign-Gram fibers.

The remaining global obstacle after this reduction is explicit: one still needs a subquadratic theorem for positive-definite sign-Gram fibers together with a way of controlling the entropy of the principal half `P`. The latter cannot be paid naively.

---

## 2. Exact sign-Gram counting with repetitions: the singular formula

Let

\[
\mathcal V_r=\{[x]:x\in\{\pm1\}^r,\ [x]=\{x,-x\}\},
\qquad A_{[x]}:=xx^T.
\]

For a positive-semidefinite matrix `K` which has at least one square sign root, define the set of multiplicity decompositions

\[
\mathfrak M_r(K):=
\left\{m:\mathcal V_r\to\mathbb Z_{\ge0}:
\sum_{v\in\mathcal V_r}m_v=r,
\quad
\sum_{v\in\mathcal V_r}m_v A_v=K
\right\}.
\tag{2.1}
\]

Also write

\[
R_r(K):=\#\{C\in\{\pm1\}^{r\times r}:CC^T=K\}.
\]

### Theorem 2.1 — exact all-corank sign-Gram formula

For every such `K`, singular or nonsingular,

\[
\boxed{
R_r(K)=
2^r\sum_{m\in\mathfrak M_r(K)}
\frac{r!}{\prod_{v\in\mathcal V_r}m_v!}.
}
\tag{2.2}
\]

#### Proof

Let the columns of `C` be `c_1,...,c_r`. Their sign classes determine multiplicities

\[
m_v=\#\{j:[c_j]=v\}.
\]

Then `sum_v m_v=r` and

\[
CC^T=\sum_{j=1}^r c_jc_j^T
=\sum_v m_vA_v,
\]

so `m in \mathfrak M_r(K)`. Conversely, for a fixed `m in \mathfrak M_r(K)`, choose which column positions carry each sign class. There are exactly

\[
\frac{r!}{\prod_v m_v!}
\]

such class assignments. Each of the `r` individual columns then has two independent sign representatives, and changing the sign of a column does not change its rank-one Gram contribution. Thus each class assignment yields exactly `2^r` sign matrices with Gram `K`. Distinct assignments or sign choices give distinct matrices. Summing over `m` proves (2.2). ∎

When `K>0`, every sign root is invertible, so no two columns can agree up to sign. Hence all `m_v` are `0` or `1`, and (2.2) reduces to the support formula from the preceding run. The point of (2.2) is that singularity is represented exactly by repeated/correlated sign classes rather than being excluded.

---

## 3. A cube-section entropy lemma

The following elementary fact will control the endpoint freedom once `C` is fixed.

### Lemma 3.1 — an affine `d`-flat contains at most `2^d` cube vertices

If `L` is an affine subspace of `R^M` of dimension `d`, then

\[
\boxed{|L\cap\{\pm1\}^M|\le2^d.}
\tag{3.1}
\]

#### Proof

Write `L=x_0+W`, with `dim W=d`. Since `W` is a `d`-dimensional linear space, there exist `d` coordinate functionals whose restrictions to `W` are linearly independent; equivalently, projection onto some `d` coordinates is injective on `W`, hence on `L`. Every point of `L cap {+-1}^M` projects to one of at most `2^d` sign patterns on those coordinates, and injectivity prevents two points from sharing a pattern. ∎

---

## 4. Fixed first half: every corank is controlled by a Gram fiber plus endpoint dimension

Fix a symmetric sign matrix `P` and a sign matrix `C` satisfying (1.4), and let

\[
k:=\operatorname{corank}C,
\qquad F:=\ker C,
\qquad \dim F=k.
\]

### Proposition 4.1 — endpoint affine dimension

For fixed `(P,C)`, the family of symmetric real matrices `D` satisfying

\[
PC+CD=0
\tag{4.1}
\]

is either empty or an affine space of dimension at most

\[
\boxed{\binom{k+1}{2}.}
\tag{4.2}
\]

Consequently the number of **sign** matrices `D` satisfying (4.1) is at most

\[
\boxed{2^{\binom{k+1}{2}}.}
\tag{4.3}
\]

The same bound remains valid after also imposing `C^TC+D^2=NI`, and therefore for actual two-eigenvalue completions.

#### Proof

If `D,D'` are two symmetric solutions then

\[
C(D-D')=0.
\]

Thus every column of the symmetric matrix `X:=D-D'` belongs to `F`. Since `X=X^T`, its range is contained in `F` and it vanishes on `F^\perp`. Therefore `X` is precisely a symmetric operator supported on `F`. The vector space of such operators is naturally `Sym(F)` and has dimension `k(k+1)/2`. Hence all symmetric solutions form an affine translate of a subspace of that dimension. Identify symmetric matrices with their upper-triangular coordinates and apply Lemma 3.1 to obtain (4.3). Additional equations only shrink the family. ∎

### Corollary 4.2 — conditioned half-completion bound

Let `K_P=NI-P^2` have rank `r-k`. Then the number of sign pairs `(C,D)` completing this **fixed** first half `P` is at most

\[
\boxed{
R_r(K_P)\,2^{\binom{k+1}{2}}.
}
\tag{4.4}
\]

This bound has no distinct-singular-value hypothesis. In particular, the repeated-nonzero-singular-value locus left over in the preceding corank-one argument is not an independent obstruction once `P` is conditioned on.

---

## 5. Rank-deficient sign-Gram roots reduce to positive-definite sign-Gram roots

Define the worst positive-definite square sign-Gram fiber

\[
R_r^+:=
\max\left\{
R_r(L):L>0,\ L=BB^T\text{ for some }B\in\{\pm1\}^{r\times r}
\right\}.
\tag{5.1}
\]

### Theorem 5.1 — singular-to-positive Gram reduction

If `K` is a positive-semidefinite `r x r` matrix of rank `r-k` admitting a sign root, then

\[
\boxed{
R_r(K)
\le
\binom{r}{k}\,2^{2rk}\,R_r^+.
}
\tag{5.2}
\]

#### Proof

Take a sign root `C` of `K` and set `d=r-k`. Choose canonically an ordered set `I` of `d` column positions for which the corresponding `r x d` submatrix `B=C_I` has full column rank; for example, take the lexicographically first such position set. Let `E` denote the ordered list of the remaining `k` sign columns. Then

\[
BB^T=CC^T-EE^T=K-EE^T.
\tag{5.3}
\]

Because the sign cube spans `R^r`, every proper linear subspace misses some sign vector. Starting from `range(B)`, choose `k` sign columns one at a time outside the span already generated, obtaining an `r x k` sign matrix `F` such that

\[
\widetilde C=[B\ F]
\]

is invertible. We may choose the extension deterministically from `B`; for counting it is harmless to allow all at most `2^{rk}` possible ordered `F`.

For fixed `K,E,F`, the positive-definite Gram matrix of `\widetilde C` is fixed:

\[
\widetilde L
=\widetilde C\widetilde C^T
=BB^T+FF^T
=K-EE^T+FF^T>0.
\tag{5.4}
\]

There are at most `R_r^+` sign matrices with that Gram. The data `(I,E,F,\widetilde C)` recover `B` as the first `d` columns of `\widetilde C` and hence recover the original `C` by reinserting `B` in positions `I` and the stored columns `E` elsewhere. Thus this is an injective encoding of roots, after fixing a deterministic extension rule. Counting permissively,

- at most `binom(r,k)` choices for `I`;
- at most `2^{rk}` choices for `E`;
- at most `2^{rk}` choices for `F`;
- at most `R_r^+` choices for `\widetilde C` once `K,E,F` are fixed.

Multiplication proves (5.2). ∎

### Corollary 5.2 — fixed-`P` all-corank bound

For the half-completion equations (1.3), if `corank C=k`, then for fixed `P`

\[
\boxed{
\#\{(C,D)\text{ sign completions of }P\}
\le
\binom{r}{k}
2^{2rk+\binom{k+1}{2}}
R_r^+.
}
\tag{5.5}
\]

So a singular cut is inexpensive whenever one can force `k=o(r)`.

---

## 6. A leverage-to-information-set lemma

The next step shows that for **every** symmetric two-eigenvalue sign matrix there is a balanced cut with `k=O(sqrt N)`. The mechanism is deterministic and depends only on the nearly flat diagonal of an eigenspace projector.

Let `U` be a subspace of `R^N`, with orthogonal projector `Pi`, and let `M_U` be its coordinate matroid: for `A subseteq [N]`,

\[
r_U(A):=\dim \pi_A(U)=\operatorname{rank}\Pi[A,A].
\tag{6.1}
\]

### Lemma 6.1 — flat leverage gives two large disjoint information sets

Assume

\[
\Pi_{ii}\ge \frac12-\eta\qquad(1\le i\le N),
\tag{6.2}
\]

and `dim U<=N/2`. Then there are disjoint coordinate sets `I_1,I_2`, each independent in `M_U`, such that

\[
\boxed{|I_1|+|I_2|\ge N(1-2\eta).}
\tag{6.3}
\]

If `N=2r`, they can be extended to a balanced partition `[N]=S sqcup T`, `|S|=|T|=r`, satisfying

\[
\boxed{r_U(S)+r_U(T)\ge N(1-2\eta).}
\tag{6.4}
\]

#### Proof

Every eigenvalue of the principal compression `Pi[A,A]` lies in `[0,1]`. Therefore its rank is at least its trace, and (6.2) gives

\[
r_U(A)\ge \operatorname{tr}\Pi[A,A]
\ge \left(\frac12-\eta\right)|A|.
\tag{6.5}
\]

Apply the standard matroid-union rank formula to two copies of `M_U`. The maximum cardinality of a set which is the disjoint union of two `M_U`-independent sets is

\[
\min_{A\subseteq[N]}
\left(N-|A|+2r_U(A)\right).
\tag{6.6}
\]

Using (6.5), every term in (6.6) is at least

\[
N-|A|+(1-2\eta)|A|
=N-2\eta|A|
\ge N(1-2\eta),
\]

which proves (6.3). Since each independent set has size at most `dim U<=r`, choose a size-`r` set `S` containing `I_1` and disjoint from `I_2`, and put `T=[N]\setminus S`. Then `I_2 subseteq T`, so

\[
r_U(S)+r_U(T)\ge |I_1|+|I_2|,
\]

giving (6.4). ∎

The only external ingredient in this lemma is the classical matroid-union rank formula; the quantitative estimate is entirely the leverage bound (6.5).

---

## 7. Every symmetric two-eigenvalue sign matrix has a balanced `O(sqrt N)`-corank cut

Now assume the integral two-eigenvalue situation

\[
H=H^T\in\{\pm1\}^{N\times N},
\qquad H^2=NI,
\qquad q:=\sqrt N\in\mathbb Z.
\tag{7.1}
\]

Let the multiplicities of `+q` and `-q` be `r+delta` and `r-delta`, after swapping signs if necessary, where `N=2r` and `delta>=0`. The trace gives

\[
2q\delta=|\operatorname{tr}H|\le N,
\qquad
\boxed{\delta\le q/2}.
\tag{7.2}
\]

Let `U` be the smaller eigenspace, so

\[
\dim U=r-\delta.
\]

Its orthogonal projector is one of

\[
\Pi=\frac12(I\pm H/q).
\]

Because every diagonal entry of `H` is `+-1`,

\[
\boxed{
\Pi_{ii}\ge \frac12-\frac1{2q}.
}
\tag{7.3}
\]

### Theorem 7.1 — balanced low-corank cut

There exists a balanced partition `[N]=S sqcup T`, `|S|=|T|=r`, such that for the cross block

\[
C:=H[S,T]
\]

we have

\[
\boxed{
\operatorname{corank}C\le q-\delta\le \sqrt N.
}
\tag{7.4}
\]

#### Proof

Apply Lemma 6.1 to `U` with `eta=1/(2q)`. We obtain a balanced partition with

\[
r_U(S)+r_U(T)\ge N-q.
\tag{7.5}
\]

We now compute the cross-block corank exactly in terms of these two coordinate ranks.

Identify `R^S` with vectors supported on `S`. A vector `x in R^S` belongs to `ker C^T` exactly when `Hx` is also supported on `S`. Let

\[
W:=\{x\in R^S:Hx\in R^S\}.
\]

Since `H^2=NI`, `W` is `H`-invariant: if `x in W`, then `Hx in R^S` and `H(Hx)=Nx in R^S`. Hence, because `H` is symmetric with only the eigenspaces `U` and `U^perp`,

\[
W=(U\cap R^S)\oplus(U^\perp\cap R^S).
\tag{7.6}
\]

Thus `dim W=corank C`. The first term has dimension

\[
\dim(U\cap R^S)
=\dim U-r_U(T)
=r-\delta-r_U(T).
\tag{7.7}
\]

The coordinate matroid of `U^perp` is the dual of the coordinate matroid of `U`. Therefore

\[
r_{U^\perp}(T)
=|T|-\dim U+r_U(S)
=r-(r-\delta)+r_U(S)
=\delta+r_U(S).
\tag{7.8}
\]

Consequently

\[
\dim(U^\perp\cap R^S)
=\dim U^\perp-r_{U^\perp}(T)
=(r+\delta)-(\delta+r_U(S))
=r-r_U(S).
\tag{7.9}
\]

Adding (7.7) and (7.9),

\[
\operatorname{corank}C
=N-\delta-r_U(S)-r_U(T)
\le q-\delta
\le q,
\]

where the first inequality is (7.5). This proves (7.4). ∎

### Remarks

1. The proof does **not** assume a generic spectrum for the cross block and does not exclude repeated nonzero singular values.
2. The partition depends on `H`; for counting, selecting a canonical good partition costs at most `binom(N,N/2)=2^{O(N)}`, which is subquadratic.
3. The theorem is stronger when the two eigenvalue multiplicities are imbalanced: the allowed corank falls from `q` to `q-delta`.

---

## 8. Main reduction: the entire singular endpoint is subquadratic relative to positive Gram fibers

For a good cut from Theorem 7.1 put `k=corank C<=sqrt N`, `r=N/2`, and fix the principal half `P=H[S,S]`. Corollary 5.2 gives

\[
\#\{(C,D)\text{ completing this }P\}
\le
R_r^+
\binom{r}{k}
2^{2rk+\binom{k+1}{2}}.
\tag{8.1}
\]

Since

\[
2rk=Nk\le N^{3/2},
\]

\[
\binom{k+1}{2}=O(N),
\]

and

\[
\log_2\binom{r}{k}=O(k\log N)=O(\sqrt N\log N),
\]

we obtain the uniform estimate

\[
\boxed{
\#\{(C,D)\text{ completing a fixed }P\text{ across a good cut}\}
\le
R_{N/2}^+\,2^{N^{3/2}+O(N+\sqrt N\log N)}.
}
\tag{8.2}
\]

Thus, at the quadratic entropy scale relevant to Vu's conjecture, **singular/corank endpoint behavior costs only `o(N^2)` bits beyond the worst positive-definite sign-Gram fiber**. This is the promised all-corank reduction. The repeated-singular-value exception from the preceding corank-one theorem has disappeared from the conditioned completion problem.

This is genuine structural progress, but it does not solve the source problem.

---

## 9. Why this still does not close the fixed-spectrum count

There are two distinct remaining obstructions.

### 9.1 Positive-definite sign-Gram fibers are already Hadamard-hard

At the orthogonal Gram point `K=rI`, the sign roots are exactly the order-`r` Hadamard matrices. Therefore a theorem

\[
R_r^+=2^{o(r^2)}
\tag{9.1}
\]

would in particular prove the still-open subquadratic Hadamard-count bound. Ferber–Jain–Zhao prove a nontrivial constant improvement over the trivial quadratic exponent and explicitly note that `H(r)=2^{o(r^2)}` would already require important new ideas. So (9.1) should not be treated as a routine local lemma.

### 9.2 The principal-half seed still carries quadratic ambient entropy

Even if (9.1) were available, a naive sum over all symmetric sign matrices `P` costs

\[
2^{r(r+1)/2}=2^{N^2/8+O(N)},
\]

which is not subquadratic. Hence a local completion theorem by itself is insufficient. A global proof needs either:

- a strong restriction on which principal halves `P` can occur in an integral spectral fiber;
- a many-cut/double-counting theorem which amortizes the seed entropy across many low-corank cuts; or
- a direct entropy inequality coupling `P` to its Gram fiber rather than counting the two independently.

This is now the cleanest bridge target: **convert the existence of many nearly full coordinate information sets into a global encoding in which the seed plus Gram-root ambiguity uses `o(N^2)` bits.**

---

## 10. Reusable covariance/entropy lemmas

Two statements above are potentially reusable outside F0011.

1. **Leverage-to-two-information-sets.** If a covariance/projector subspace has all coordinate leverage scores at least `1/2-eta`, then two disjoint coordinate information sets cover at least `N(1-2eta)` coordinates, and for even `N` they extend to balanced halves with the same rank-sum lower bound.
2. **Affine cube entropy.** A `d`-dimensional affine constraint set supports at most `2^d` sign configurations.

These statements are deterministic. They do not by themselves prove the Gaussian tensor type-2 conjecture or the random-graph Lovasz-theta constant, but they provide a clean way to turn flat leverage/covariance structure into controlled coordinate rank loss and then into discrete entropy bounds.

---

## 11. Source metric and next attack

The fixed full-source metric does not move in this run:

\[
\boxed{N_{\rm exact}:9\to9.}
\]

No complete `n=10` census was attempted because the progress-first owner directive prioritizes the missing arbitrary-size bridge.

The intermediate obligation **does** move:

> singular half-completion obstruction: `generic corank-one only, repeated-singular locus unresolved`  
> `->` **all coranks reducible to positive-definite Gram fibers with at most `2^{N^{3/2}+O(N+sqrt(N) log N)}` conditioned overhead after a balanced good cut.**

The next mathematical attack should therefore target the global seed/Gram coupling, not singular-value casework: prove a many-good-cut entropy inequality, or exhibit a family showing that such a local-to-global reduction cannot be subquadratic. A parallel route is to identify a non-Hadamard structural condition under which positive-definite Gram fibers have `2^{o(r^2)}` roots and then show that the complementary Hadamard-like locus has additional global rigidity.
