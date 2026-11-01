Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated binding model/effort selector or runtime telemetry is exposed.

# F0011 — exact `n=9` census, two-affine-basis normal form, and a half-completion localization theorem

Date: 2026-09-19 UTC  
Slot: `R7-06`  
Canonical target: `F0011`, Van H. Vu, *Recent progress in combinatorial random matrix theory*, Conjecture 9.4.  
Methods in this ordinary run: **B10 / B25 / B28**.  
Status: **PARTIAL**. The source asymptotic remains OPEN under bounded current checks.

## 1. Exact finite movement: `N_exact = 8 -> 9`

The frozen metric is the largest `n` for which every diagonal-switching-normalized symmetric sign matrix has been classified exactly as integral-spectrum or non-integral-spectrum, with exact counts. The preceding certificate stopped at `n=8`. The new checker

`2026-09-19T220900Z__F0011_n9_exact_census.cpp`

exhausts `n=9` and ends `ALL_EXACT_ASSERTIONS_PASS`.

### Theorem 1.1 — exact order-nine census

Among the

\[
2^{9+\binom 82}=2^{37}=137438953472
\]

diagonal-switching-normalized symmetric `{+1,-1}` matrices of order `9`, exactly

\[
\boxed{3,685,058}
\]

have integral spectrum. Hence the exact order-nine probability, in either the normalized transversal or the full symmetric Rademacher model, is

\[
\boxed{
\frac{3,685,058}{2^{37}}
=
\frac{1,842,529}{68,719,476,736}
\approx 2.68123258\times 10^{-5}.
}
\]

Exactly `124` integral spectra occur. The largest switching-normalized labeled fixed-spectrum fiber has size

\[
\boxed{317,520},
\]

and this maximum occurs for the two sign-opposite spectra

\[
(-4,-4,-2,-2,-1,2,2,4,4),
\]

and

\[
(-4,-4,-2,-2,1,2,2,4,4).
\]

#### Proof / exact-certificate completeness

Diagonal conjugation by a sign diagonal matrix preserves spectrum. Modulo the global `-I`, this action has size `2^8`; every orbit has a unique representative whose first-row off-diagonal entries are all `+1`. The remaining off-diagonal signs are therefore a labeled graph on eight vertices, and the nine diagonal signs are arbitrary. Thus the normalized space has `2^28 * 2^9 = 2^37` points.

The checker generates all unlabeled graphs on at most eight vertices by canonical augmentation. If representatives for all `(k-1)`-vertex isomorphism classes are known, deleting one vertex from any `k`-vertex graph reaches one such class; adjoining a new vertex with every possible neighborhood therefore reaches every `k`-vertex graph. Canonicalization is exact because isomorphisms preserve degrees, and the code enumerates every permutation inside each equal-degree class. The resulting class counts are

\[
1,1,2,4,11,34,156,1044,12346
\]

through order eight. For each order-eight representative `G`, it computes `|Aut(G)|` exactly and weights the representative by

\[
\frac{8!}{|\operatorname{Aut}(G)|}.
\]

The weighted graph mass is exactly `2^28`, so no labeled residual graph is omitted or duplicated in the aggregate.

It remains to decide integrality without floating arithmetic. If `M` is a `9 x 9` sign matrix with integral eigenvalues `lambda_1,...,lambda_9`, then Gershgorin gives `|lambda_i|<=9`, and

\[
\sum_i\lambda_i^2=\operatorname{tr}(M^2)=81.
\]

Moreover `M mod 2 = J_9`. Since `J_9^2=J_9` over `F_2`,

\[
\chi_{J_9}(x)=x^8(x-1),
\]

so exactly one integer eigenvalue is odd. Together with the exact trace constraint this leaves only `258` nondecreasing candidate integral spectra.

For every normalized matrix the checker computes the exact integer power sums

\[
p_k=\operatorname{tr}(M^k),\qquad 1\le k\le9.
\]

It uses the identities

\[
p_3=25\sum_i M_{ii}+6\sum_{i<j<k}M_{ij}M_{jk}M_{ki}
\]

and, for `i ne j`,

\[
(M^2)_{ij}=M_{ij}(M_{ii}+M_{jj})+
\sum_{k\ne i,j}M_{ik}M_{kj},
\qquad (M^2)_{ii}=9,
\]

then integer matrix products for the remaining traces. Newton's identities imply that `p_1,...,p_9` determine the monic characteristic polynomial. Therefore a matrix has integral spectrum exactly when its nine power sums equal one of the `258` candidate tuples. The executed output checks the total mass, candidate count, and final census and terminates `ALL_EXACT_ASSERTIONS_PASS`. ∎

This is genuine movement of the frozen metric, not closure of Vu's asymptotic conjecture.

---

## 2. Starting point for B10/B25/B28

The final STUCK2 recovery isolated the cleanest source-valid obstruction: the maximal-binary-rank, two-eigenvalue symmetric-Hadamard branch. Write

\[
n=4t^2,\qquad t\text{ even},\qquad
m=2t^2-1,\qquad r=m+1=2t^2,
\]

so `n=2r` and `m` is odd. After normalization, the exact Hadamard equations produce a binary matrix `N` of order `2m+1` with

\[
N^2=0,\qquad N\mathbf1=0,\qquad
\operatorname{rank}_{\mathbf F_2}N=m.
\tag{2.1}
\]

The preceding run proved that an adapted basis can be chosen so that

\[
\boxed{N=XX^T}
\tag{2.2}
\]

with `X` a `(2m+1) x m` full-column-rank binary matrix. If the rows of `X` are `p_1,...,p_{2m+1}` and `p_0=0`, then

\[
Q=\{p_0,p_1,\ldots,p_{2m+1}\}\subset\mathbf F_2^m,
\qquad |Q|=2m+2=2r,
\]

and the normalized symmetric Hadamard is the principal Walsh matrix

\[
H_Q=\bigl((-1)^{x\cdot y}\bigr)_{x,y\in Q}.
\tag{2.3}
\]

The remaining difficulty is to count such `Q` in a fixed trace/spectrum fiber.

---

## 3. B10 — DERANDOMIZE: every exact object splits into two affine bases

The previous fixed-external-basis anti-concentration estimate lost its gain because the useful basis was chosen adaptively from `Q`. The following theorem makes that adaptive choice completely explicit.

### Theorem 3.1 — self-dual matroid / two-affine-basis normal form

Assume (2.1)-(2.2), and define the length-`2m+2` binary code

\[
C=\{(u,0):u\in\operatorname{im}X\}
+\langle(\mathbf1,1)\rangle.
\tag{3.1}
\]

Then:

1. `C` is self-dual of dimension `r=m+1`.
2. The columns of a generator matrix of `C` are precisely the affine lifts `(p,1)`, `p in Q`.
3. If `I={0,b_1,...,b_m}` is any affine basis contained in `Q`, then its complement `J=Q\I` is also an affine basis.
4. After sending `I` to `{0,e_1,...,e_m}` and row-reducing the lifted generator, one obtains

\[
\boxed{[I_r\mid T]},\qquad TT^T=I_r.
\tag{3.2}
\]

Thus, after one internal affine basis is selected, the entire mod-two complement is parametrized by an orthogonal matrix `T in O(r,2)` whose columns are disjoint from the standard basis.

#### Proof

From `N^2=0` and `N=XX^T`,

\[
X(X^TX)X^T=0.
\]

Because `X` has full column rank, multiplying by a left inverse of `X` and its transpose gives

\[
X^TX=0.
\tag{3.3}
\]

Likewise `N\mathbf1=X(X^T\mathbf1)=0` and injectivity of `X` give

\[
X^T\mathbf1=0.
\tag{3.4}
\]

A generator matrix for `C` is

\[
G_C=
\begin{pmatrix}
X^T&0\\
\mathbf1^T&1
\end{pmatrix}.
\tag{3.5}
\]

Equations (3.3)-(3.4), together with `2m+2=0` in `F_2`, give

\[
G_CG_C^T=0.
\]

The rows are independent and there are `m+1=r=(2m+2)/2` of them. Hence `C` is self-orthogonal of half the ambient dimension, so `C=C^\perp`.

The columns in (3.5) are `(p_i,1)` for the rows `p_i` of `X`, together with `(0,1)`, exactly the affine lifts of the points of `Q`.

Now let `I={0,b_1,...,b_m}` with `b_1,...,b_m` a linear basis. Its lifted columns are independent: if

\[
\alpha_0(0,1)+\sum_{i=1}^m\alpha_i(b_i,1)=0,
\]

then the first `m` coordinates imply every `alpha_i=0` for `i>=1`, and then the last coordinate gives `alpha_0=0`. Thus the `I`-block of `G_C` is invertible. Reorder columns so `I` comes first and row-reduce to

\[
[I_r\mid T].
\]

Self-duality gives

\[
0=[I_r\mid T][I_r\mid T]^T=I_r+TT^T,
\]

hence `TT^T=I_r`. In particular `T` is invertible, so the complementary `r` columns are also independent. Their underlying points therefore form an affine basis `J`. ∎

### Corollary 3.2 — explicit point parametrization

Put the selected affine basis in coordinates

\[
I_0=\{0,e_1,\ldots,e_m\}\subset\mathbf F_2^m.
\]

Define

\[
\phi(z)=(1+\mathbf1^Tz,z)\in\mathbf F_2^{r}.
\tag{3.6}
\]

The map `phi` is a bijection from `F_2^m` to the odd-weight vectors in `F_2^r`, and it sends the lifted points of `I_0` to the standard basis of `F_2^r`. Consequently every complement has the form

\[
J_T=\{\phi^{-1}(Te_j):0\le j\le m\},
\tag{3.7}
\]

for an orthogonal `T`, with the additional disjointness condition `T\{e_j\}\cap\{e_j\}=emptyset` required because `Q` is a set.

This is the desired derandomization: the adaptive-basis ambiguity is no longer an uncontrolled choice among all of `GL(m,2)`; it is an exact self-dual information-set decomposition.

---

## 4. The exact real constraint after the binary derandomization

The mod-two self-dual code is not the full Hadamard condition. The missing real/integer information can nevertheless be written in one exact equation.

Let the chosen original basis be the columns of `R in GL(m,2)`. In normalized affine coordinates `p=Rz`, the original dot product becomes

\[
p\cdot q=z^TGw,
\qquad G=R^TR.
\tag{4.1}
\]

Since `m` is odd, `G` is a nonsingular symmetric binary form. In affine-lift coordinates define

\[
\widetilde G=
\begin{pmatrix}
0&0\\
0&G
\end{pmatrix}
\in\operatorname{Sym}_r(\mathbf F_2).
\tag{4.2}
\]

Let

\[
S_T=\{e_0,\ldots,e_m\}\cup\{Te_0,\ldots,Te_m\}.
\]

Then the exact symmetric sign matrix is

\[
\boxed{
H(G,T)_{x,y}=(-1)^{x^T\widetilde G y},
\qquad x,y\in S_T.
}
\tag{4.3}
\]

Write `wt` for Hamming weight in `F_2^r`.

### Theorem 4.1 — exact weight-complement criterion

The matrix `H(G,T)` is Hadamard if and only if

\[
\boxed{
\operatorname{wt}(\widetilde G u)
+
\operatorname{wt}(T^T\widetilde G u)
=r
}
\tag{4.4}
\]

for every nonzero difference

\[
u=x+y,\qquad x\ne y,\quad x,y\in S_T.
\]

Moreover the exact two-eigenvalue spectrum is fixed by the trace

\[
\boxed{
\tau(G,T)=\sum_{x\in S_T}(-1)^{x^T\widetilde Gx}.
}
\tag{4.5}
\]

#### Proof

For distinct `x,y in S_T`, the inner product of their rows is

\[
\sum_{z\in S_T}(-1)^{(x+y)^T\widetilde Gz}.
\]

Split `S_T` into the standard basis and its `T`-image. With

\[
\omega(a)=\sum_{j=0}^m(-1)^{a_j}=r-2\operatorname{wt}(a),
\]

the row inner product is

\[
\omega(\widetilde G(x+y))+
\omega(T^T\widetilde G(x+y)).
\]

It vanishes exactly when the two displayed Hamming weights sum to `r`, proving (4.4). The diagonal entry indexed by `x` is `(-1)^{x^T\widetilde Gx}`, so (4.5) is the trace. A symmetric Hadamard of order `n=2r=4t^2` has eigenvalues `+2t` and `-2t`; their multiplicities are determined by the trace. ∎

Thus the remaining hard count is now a count of pairs `(G,T)` satisfying an explicit finite-system weight constraint, modulo the coordinate/gauge equivalences already identified.

---

## 5. B25 — COUNT THE SAME THING TWICE: what basis double-counting can and cannot save

The previous run proved a fixed-external-basis rarity of roughly

\[
2^{-m(m+1)/2+O(m)}
\]

for the simultaneous Fourier-zero constraints. A naive attempt was to union over every ordered basis of `F_2^m` and divide by the number of bases inside a completed `Q`.

### Proposition 5.1 — internal-basis multiplicity is subquadratic entropy

Every `Q` of size `2m+2` contains at most

\[
(2m+1)_m<(2m+2)^m
\]

ordered linear bases after fixing the zero point. Hence

\[
\boxed{
\log_2 B(Q)=O(m\log m)
}
\tag{5.1}
\]

for the number `B(Q)` of such internal bases.

On the other hand

\[
|GL(m,2)|
=
\prod_{j=0}^{m-1}(2^m-2^j)
=
2^{m^2+O(1)}.
\tag{5.2}
\]

Therefore the fixed-basis saving of approximately `m^2/2` bits cannot be turned into a subquadratic global bound merely by charging every completed set to all of its internal bases: the greatest multiplicity correction available from that incidence relation is only `O(m log m)` bits.

#### Proof

There are only `2m+1` nonzero points in `Q`; an ordered basis is an ordered `m`-tuple of distinct nonzero points, proving the first inequality. Formula (5.2) is the standard exact count of ordered bases. The entropy comparison follows immediately. ∎

Theorem 3.1 does improve the *shape* of the double count: after an information set is chosen, the complement lies in an orthogonal-group orbit rather than arbitrary `GL`. But the orthogonal group itself still has quadratic logarithmic size by the standard finite-classical-group order formulas. The missing saving must therefore come from the exact coupling (4.4), not from basis multiplicity alone.

---

## 6. B28 — REPLACE FOR ALL WITH TYPICAL: generic half-completion localizes to cospectral mates

Order the two affine bases first and second and write the exact real sign matrix as

\[
H=
\begin{pmatrix}
P&C\\
C^T&D
\end{pmatrix},
\qquad P=P^T,\quad D=D^T,
\tag{6.1}
\]

with all three blocks `r x r`. The Hadamard equation `H^2=2r I` gives

\[
P^2+CC^T=2rI,
\tag{6.2}
\]

\[
PC+CD=0,
\tag{6.3}
\]

\[
C^TC+D^2=2rI.
\tag{6.4}
\]

Set

\[
K_P=2rI-P^2.
\tag{6.5}
\]

### Proposition 6.1 — exact Gram-square-root obstruction

Every exact completion satisfies

\[
\boxed{CC^T=K_P.}
\tag{6.6}
\]

Consequently `K_P` is positive semidefinite and

\[
\boxed{\det K_P=(\det C)^2}
\tag{6.7}
\]

is a nonnegative perfect square integer. These conditions depend only on the first half `P`.

If `K_P` is positive definite, then `C` is invertible and

\[
\boxed{D=-C^{-1}PC.}
\tag{6.8}
\]

Thus `D` is similar to `-P` and

\[
\operatorname{Spec}(D)=-\operatorname{Spec}(P).
\tag{6.9}
\]

In particular an invertible-cross completion has

\[
\boxed{\operatorname{tr}H=0.}
\tag{6.10}
\]

Hence every nonzero-trace two-eigenvalue fiber lies entirely on the algebraic boundary `det C=0`, equivalently `det K_P=0`, for *every* two-affine-basis split furnished by Theorem 3.1.

#### Proof

Equations (6.6) and (6.7) are (6.2) and determinants. If `K_P` is positive definite then `CC^T` is positive definite, so `C` is invertible; (6.3) gives (6.8). Similarity gives (6.9), and taking traces yields `tr D=-tr P`, proving (6.10). ∎

This is a sharp generic/exceptional split: fixed fibers with nonzero trace cannot live in the invertible-cross generic branch at all.

### Theorem 6.2 — simple-spectrum generic completion bound conditional on the second half

Assume `K_P` is positive definite and `P` has simple real spectrum. Fix a symmetric real matrix `D` with

\[
\operatorname{Spec}(D)=-\operatorname{Spec}(P).
\]

Then there are at most

\[
\boxed{2^r}
\]

real matrices `C` satisfying simultaneously

\[
PC+CD=0,
\qquad CC^T=K_P.
\tag{6.11}
\]

Therefore the number of sign-matrix completions for this fixed pair `(P,D)` is also at most `2^r`.

#### Proof

Choose orthogonal diagonalizations

\[
P=U\Lambda U^T,
\qquad
D=V(-\Lambda)V^T,
\]

where the distinct eigenvalues of `P` have been ordered so the spectra match. Put `Y=U^TCV`. Equation `PC+CD=0` becomes

\[
\Lambda Y-Y\Lambda=0.
\]

Because all diagonal entries of `Lambda` are distinct, `Y` must be diagonal. Since `K_P` is the polynomial `2rI-P^2`, the second equation in (6.11) becomes

\[
YY^T=
\operatorname{diag}(2r-\lambda_1^2,\ldots,2r-\lambda_r^2).
\]

Positive definiteness makes each entry positive, and each diagonal entry of `Y` therefore has exactly two possible signs:

\[
Y_{ii}=\pm\sqrt{2r-\lambda_i^2}.
\]

There are at most `2^r` choices. ∎

### Corollary 6.3 — where the generic quadratic entropy can still hide

On the simple-spectrum, invertible-cross branch, once `P` is fixed the cross block costs only `O(r)` bits **per chosen cospectral second half**. Thus any quadratic entropy remaining in that generic branch must lie in the number of symmetric sign matrices `D` cospectral with `-P`.

This is a genuine localization, not a solution: no uniform `2^{o(r^2)}` theorem for those cospectral sign mates has been proved here. Importing such a statement without proof would simply replace F0011 by another hard spectral-counting problem. The repeated-spectrum or singular-cross exceptional branch also remains uncontrolled.

---

## 7. Relation to current literature and noncircularity

Goldberger and Strassler, *A practical algorithm for completing half-Hadamard matrices using LLL* (J. Algebraic Combinatorics 55 (2022), 217-244, DOI 10.1007/s10801-021-01077-z), study exactly the half-Hadamard completion / integer Gram-square-root shape. Their algorithm applies from half size under stated practical assumptions and depends on an unproved conjecture about LLL performance; it is not a rigorous uniform asymptotic count of the present fibers.

Damek Davis, *Counting partial Hadamard matrices in the cubic regime*, arXiv:2603.30013 (submitted 2026-03-31), obtains precise asymptotics in a much more rectangular regime; it does not cover the present half-square self-principal regime.

Alexander Van Werde, *Finding all cospectral mates over a number field*, arXiv:2608.12410 (2026-08-11), gives a finite algorithm and sufficient spectral-determination conditions using discriminants and Krylov spaces. This is methodologically relevant to Corollary 6.3, but it does not supply the uniform subquadratic fixed-fiber count needed here, especially on repeated-spectrum/singular branches.

Aida Abiad, Nils van de Berg and Robin Simoens, *Switching methods of level 2 for the construction of cospectral graphs*, available online 2026-08-26 in *Linear Algebra and its Applications*, shows that structured cospectral families continue to arise from nontrivial rational-orthogonal switching. This reinforces the need to count, not merely detect, cospectral mates.

No novelty claim is made from a bounded search miss. The statements in Sections 3-6 are proved here as restricted structural results; they do not establish Vu's source asymptotic.

---

## 8. What changed mathematically

The run produced four durable facts.

1. The frozen finite metric moves for the first time since the two stuck recoveries:
   \[
   \boxed{N_{\rm exact}:8\to9.}
   \]
2. The adaptive-basis ambiguity on the maximal-rank Hadamard core has an exact self-dual normal form: every exact object splits into **two affine bases**, with complement encoded by an orthogonal matrix.
3. The full real Hadamard condition is the explicit weight-complement equation (4.4), so the mod-two orthogonal parameter is not free.
4. On the generic simple-spectrum/invertible-cross branch, half-completion costs only `O(r)` bits once the second half is fixed; nonzero-trace fibers are forced onto the singular-cross boundary.

The source conjecture remains **PARTIAL / OPEN**. Because `N_exact` moved, the post-STUCK2 no-movement streak resets rather than triggering the mandatory handoff. Both HARD stuck recoveries remain consumed; any future third unchanged streak must therefore hand off without a new STUCK recovery.
