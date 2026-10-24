Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated binding model/effort selector or runtime telemetry is exposed.

# F0011 — finite-alphabet compression of rich cube sections and a principal-angle fixed-subspace entropy theorem

Date: 2026-09-20 UTC  
Role: C05 / R7-06, native ID `6aabe827777c8191a43330b4a87d481d`  
Canonical target: F0011 / Van H. Vu, *Recent progress in combinatorial random matrix theory*, Conjecture 9.4  
Status: **PROVED PARTIAL** toward the source conjecture, pending later independent review. No source-level closure or external novelty claim.

## 1. Exact source and inherited bottleneck

For the symmetric Rademacher matrix `M_n^sym` (upper-triangular and diagonal entries independent fair signs, lower triangle filled by symmetry), Vu's Conjecture 9.4 asks

\[
\Pr\bigl(\operatorname{Spec}(M_n^{\rm sym})\subset\mathbb Z\bigr)
 =2^{-(1/2+o(1))n^2}.
\tag{1.1}
\]

Since the labelled ensemble has `2^{n(n+1)/2}` elements, this is equivalent to proving that the number of labelled symmetric sign matrices with integral spectrum is `2^{o(n^2)}`.

The active boundary problem is the symmetric Hadamard / centered two-eigenvalue slice

\[
H=H^T\in\{\pm1\}^{N\times N},\qquad H^2=NI,
\tag{1.2}
\]

usually with `N=2r` and, on the centered branch, `tr H=0`.

The previous C05 theorem supplied two ingredients.

1. Every centered completed matrix has a balanced cut with macroscopic mixed energy, so an exact endpoint cut is not intrinsic.
2. If a `d`-dimensional row-tail subspace `V<=R^n` has cube deficiency

\[
\sigma(V):=d-\log_2|V\cap\{\pm1\}^n|\le s,
\]

then, after choosing `d` pivot coordinates, each remaining coordinate depends on at most `(8/pi)4^s` pivots. For an orthogonal sign tail this gives

\[
R=Y[I_d\ A],\qquad Y^TY=n(I+AA^T)^{-1},
\tag{1.3}
\]

with column-sparse `A`.

What was missing was an actual entropy bound for the family of such rich subspaces, and a basis-free bound on the number of symmetric Hadamard completions after the half-rowspace itself is fixed. This note proves both.

---

## 2. Finite-alphabet theorem for hypercube-rich sign-spanned subspaces

Let `V<=R^n` have dimension `d`, put

\[
Q(V)=V\cap\{\pm1\}^n,
\]

and assume that `Q(V)` spans `V`. This spanning assumption is automatic in the Hadamard row-tail application because `V` contains `d` linearly independent sign rows.

Assume

\[
|Q(V)|\ge 2^{d-s}.
\tag{2.1}
\]

Choose a set `I` of `d` coordinates for which the projection `pi_I:V->R^d` is an isomorphism. After permuting coordinates, write the subspace as the graph

\[
V=\{(x,A^Tx):x\in\mathbb R^d\},
\qquad [I_d\ A].
\tag{2.2}
\]

For a nonpivot coordinate `j`, let

\[
L_j(x)=a_j\cdot x,
\]

where `a_j` is the corresponding column of `A`.

The preceding hypercube-rich lemma gives

\[
|\operatorname{supp}(a_j)|\le t,
\qquad
 t:=\min\left(d,\left\lceil\frac8\pi4^s\right\rceil\right).
\tag{2.3}
\]

The new point is that the nonzero coefficients come from a finite rational alphabet depending only on `t`.

### Theorem 2.1 — finite coefficient alphabet

Define

\[
D_t:=\left\lceil t^{t/2}\right\rceil,
\qquad
\mathcal R_t:=\left\{\frac pq:p,q\in\mathbb Z,\ q\ne0,\ |p|,|q|\le D_t\right\}.
\tag{2.4}
\]

Then every coefficient of every column `a_j` belongs to `\mathcal R_t`. In particular,

\[
|\mathcal R_t|\le (2D_t+1)^2.
\tag{2.5}
\]

#### Proof

Fix a nonpivot coordinate and let `S=supp(a_j)`, `|S|=k<=t`. The pivot images

\[
X:=\pi_I(Q(V))\subseteq\{\pm1\}^d
\]

span `R^d`, because `Q(V)` spans `V` and `pi_I` is an isomorphism. Therefore the restricted vectors `x|_S`, `x in X`, span `R^S`. Choose `k` points `x^(1),...,x^(k) in X` whose restrictions to `S` form an invertible `k x k` sign matrix `M`.

For each selected point, the original vector belongs to the sign cube, so

\[
L_j(x^{(u)})\in\{\pm1\}.
\]

Let `z in {+-1}^k` collect these values. The nonzero coefficient vector satisfies exactly

\[
M a_{j,S}=z.
\tag{2.6}
\]

By Cramer's rule each coordinate is a ratio of two integer determinants. Hadamard's determinant inequality gives, for both denominator and numerator,

\[
|\det M|\le k^{k/2}\le t^{t/2},
\qquad
|\det M_i(z)|\le k^{k/2}\le t^{t/2}.
\tag{2.7}
\]

The denominator is nonzero. Hence every coefficient lies in `R_t`. ∎

### Corollary 2.2 — entropy of rich sign-spanned subspaces

For fixed pivot set `I`, each nonpivot coordinate form has at most

\[
B(d,t):=
\sum_{k=1}^{t}\binom dk |\mathcal R_t|^k
\tag{2.8}
\]

possibilities (adding the zero form, if desired, changes this by one). Therefore the number of `d`-dimensional sign-spanned subspaces `V<=R^n` satisfying (2.1) is at most

\[
\boxed{
\binom nd\,\bigl(1+B(d,t)\bigr)^{n-d}.
}
\tag{2.9}
\]

Consequently

\[
\boxed{
\log_2 \#\mathcal V_{n,d}(s)
\le
n+O\!\left((n-d)\bigl[t\log(d+1)+t^2\log(t+2)\bigr]\right).
}
\tag{2.10}
\]

#### Proof

Once the pivot set and all nonpivot coefficient columns are fixed, the graph (2.2) is fixed. For a support of size `k`, choose its coordinates and then `k` coefficients from `R_t`; summing over `k<=t` yields (2.8). Also

\[
\log_2|\mathcal R_t|=O(t\log(t+2)),
\]

so the logarithm of (2.8) is `O(t log(d+1)+t^2 log(t+2))`. Finally `log_2 binom(n,d)<=n`. ∎

### Corollary 2.3 — subquadratic description regime

If `d=Theta(n)` and

\[
16^s(s+1)=o(n),
\tag{2.11}
\]

then

\[
\boxed{\#\mathcal V_{n,d}(s)=2^{o(n^2)}.}
\tag{2.12}
\]

In particular, for every fixed `epsilon>0`, the sufficient condition

\[
s\le\left(\frac14-\epsilon\right)\log_2 n
\tag{2.13}
\]

implies (2.12).

This converts the preceding qualitative sparse normal form into an actual source-scale entropy theorem for the family of near-Odlyzko-saturated subspaces.

---

## 3. A support-core sharpening

The sparse supports cannot be arbitrarily spread when the deficiency is small.

Call a coordinate form `L(x)` **nontrivial** if its support has size at least two. For such a form,

\[
\Pr_{\varepsilon\in\{\pm1\}^{d}}
\bigl(L(\varepsilon)\in\{\pm1\}\bigr)\le\frac34.
\tag{3.1}
\]

Indeed, for support size two, if both `a+b` and `a-b` belonged to `{+-1}`, then one coefficient would be zero, contradicting support size two; hence the acceptance probability is at most `1/2`. For support size `k>=3`, the union of two atoms is bounded by the Littlewood-Offord/Sperner estimate

\[
2^{1-k}\binom{k}{\lfloor k/2\rfloor}\le\frac34.
\tag{3.2}
\]

Suppose `m` nontrivial coordinate forms have pairwise disjoint supports. Their acceptance events are independent. Since every pivot image of a cube point must satisfy all coordinate constraints, (2.1) implies

\[
2^{-s}\le (3/4)^m.
\]

Therefore

\[
\boxed{
m\le \frac{s}{\log_2(4/3)}.}
\tag{3.3}
\]

Taking a maximal matching of the family of nontrivial supports, the union of its members is a hitting set `U` for every nontrivial support. Hence there is a pivot-coordinate core satisfying

\[
\boxed{
|U|\le
 t\left\lceil\frac{s}{\log_2(4/3)}\right\rceil
}
\tag{3.4}
\]

that intersects every nontrivial coordinate dependence.

There is also a deficiency gap: if any nontrivial coordinate occurs, then (3.1) already gives

\[
\boxed{\sigma(V)\ge\log_2(4/3).}
\tag{3.5}
\]

At deficiency zero, all coordinate forms are signed single pivots, recovering the exact smaller-Hadamard recursion from the preceding report.

---

## 4. Fixed half-rowspace: a principal-angle entropy theorem

The second new ingredient is basis-free and automatically keeps the singular/corank endpoint visible.

Let `N=2r`. Fix the coordinate half-space

\[
E=\operatorname{span}(e_{r+1},...,e_{2r})\subset\mathbb R^{2r},
\qquad F=E^\perp.
\]

For a symmetric Hadamard matrix `H`, put

\[
Q:=H/\sqrt N.
\]

Then

\[
Q=Q^T,\qquad Q^2=I,
\]

so `Q` is a symmetric orthogonal involution. Let

\[
V:=QE.
\tag{4.1}
\]

This is exactly the span of the `r` rows of `H` indexed by the chosen half (equivalently, after transposition symmetry, their normalized column space).

Let the principal angles between `E` and `V` have:

- angle `0` with multiplicity `a`;
- angle `pi/2` with multiplicity `b`;
- distinct interior angles `theta in (0,pi/2)` with multiplicities `m_theta`.

Thus

\[
a+b+\sum_\theta m_\theta=r.
\tag{4.2}
\]

### Theorem 4.1 — fixed-subspace completion dimension

For fixed `E` and fixed `V`, all symmetric orthogonal involutions `Q` satisfying `QE=V` lie in a linear subspace of matrix space of dimension

\[
\boxed{
L(V)=a(a+1)+b^2+
\sum_{\theta\in(0,\pi/2)}\frac{m_\theta(m_\theta+1)}2.
}
\tag{4.3}
\]

Consequently the number of symmetric Hadamard matrices `H` with this fixed half-rowspace `V` is at most

\[
\boxed{2^{L(V)}.}
\tag{4.4}
\]

#### Proof

Use the CS decomposition for the pair `(E,V)`. The ambient space splits orthogonally into blocks indexed by principal angles.

**Angle 0.** Here `E_0=E cap V` and `F_0=F cap V^perp` both have dimension `a`. Symmetry and `QE=V` force both subspaces to be invariant. The two restrictions of `Q` are symmetric orthogonal involutions. Their linear spans are contained in `Sym(E_0)` and `Sym(F_0)`, of dimensions `a(a+1)/2` each. Total contribution: `a(a+1)`.

**Angle pi/2.** Here `E_1=E cap V^perp` and `F_1=F cap V` both have dimension `b`. In suitable coordinates every admissible `Q` has block form

\[
\begin{pmatrix}0&R^T\\R&0\end{pmatrix},
\tag{4.5}
\]

with `R:E_1->F_1` orthogonal. This family lies in a linear space naturally isomorphic to `Hom(E_1,F_1)`, dimension `b^2`.

**Interior angle theta.** Let `E_theta` have dimension `m=m_theta`; the pair `(E,V)` determines a canonical isometry `J_theta:E_theta->F_theta`. Every admissible symmetric involution on this block has the form

\[
Q_\theta(S)=
\begin{pmatrix}
\cos\theta\,S & \sin\theta\,S J_\theta^T\\
\sin\theta\,J_\theta S & -\cos\theta\,J_\theta S J_\theta^T
\end{pmatrix},
\tag{4.6}
\]

where `S` is a symmetric orthogonal operator on `E_theta`. Conversely these are precisely the possibilities. Formula (4.6) is linear in the symmetric matrix `S`, so the block family lies in a linear space of dimension `m(m+1)/2`.

The CS blocks are orthogonal direct summands, so the dimensions add and give (4.3).

Finally scale by `sqrt N`. Every valid `H` is a sign point in this `L(V)`-dimensional linear subspace of `R^{N x N}`. A linear `L`-flat meets the sign cube in at most `2^L` points: choose `L` coordinate functionals whose restrictions are injective, and project. This proves (4.4). ∎

---

## 5. Principal angles are exactly the singular/corank data of the cut

Write the normalized block decomposition relative to `F oplus E`:

\[
Q=\frac1{\sqrt N}
\begin{pmatrix}P&C\\C^T&D\end{pmatrix}.
\tag{5.1}
\]

The map `Q|_E:E->V` is an isometry. Its projections to `F` and `E` are respectively `C/sqrt N` and `D/sqrt N`. Therefore

\[
\operatorname{singval}(C/\sqrt N)=\{\sin\theta_i\},
\qquad
\operatorname{singval}(D/\sqrt N)=\{\cos\theta_i\}.
\tag{5.2}
\]

In particular,

\[
\boxed{a=\operatorname{corank}C,\qquad b=\operatorname{corank}D.}
\tag{5.3}
\]

Interior principal-angle multiplicities are exactly multiplicities of the corresponding nonzero, nonendpoint singular values of the cross block (equivalently, absolute normalized eigenvalues of `D`).

This is the key singular-endpoint interpretation: corank is not discarded. It contributes explicitly through `a(a+1)` and `b^2` in (4.3).

The earlier balanced-cut theorem proved that every two-eigenvalue symmetric sign matrix with integral eigenvalues has a balanced cut satisfying

\[
\operatorname{corank}C\le\sqrt N.
\tag{5.4}
\]

On such a cut the `a(a+1)` term is only `O(N)`, hence subquadratic. Thus the remaining fixed-`V` quadratic obstruction is not generic singularity of `C`; it is **macroscopic multiplicity of one principal angle**, including possibly the `pi/2` multiplicity `b`.

Define

\[
M(V):=\max\left(b,\max_{\theta\in(0,\pi/2)}m_\theta\right).
\tag{5.5}
\]

Then, using `sum m_theta<=r`,

\[
L(V)
\le a(a+1)+M(V)r+\frac{M(V)+1}{2}r.
\tag{5.6}
\]

Hence if `a=O(sqrt N)` and `M(V)=o(r)`, then

\[
\boxed{L(V)=o(N^2).}
\tag{5.7}
\]

and the fixed-subspace completion count is source-scale subquadratic.

---

## 6. Combined restricted fixed-spectrum theorem

The two new theorems combine without double-counting a basis.

### Theorem 6.1 — low-deficiency, diffuse-angle branch is subquadratic

Fix `epsilon>0`. Consider centered symmetric Hadamard matrices of order `N=2r` for which there exists a balanced cut such that, for the associated half-rowspace `V=QE`, all of the following hold:

1. `a=corank C<=sqrt N`;
2. `sigma(V)<= (1/4-epsilon) log_2 N`;
3. `M(V)=o(r)` uniformly along the family.

Then the number of matrices in this branch is

\[
\boxed{2^{o(N^2)}.}
\tag{6.1}
\]

More generally, condition 2 can be replaced by `16^{sigma(V)}(sigma(V)+1)=o(N)`.

#### Proof

There are at most `binom(N,r)=2^{O(N)}` balanced cuts. Fix one.

Because the selected half-rowspace contains `r` independent sign rows, it is sign-spanned. By Corollary 2.3, the number of possible `V` obeying the deficiency condition is `2^{o(N^2)}`.

For each fixed `V`, Theorem 4.1 and (5.7) give at most `2^{o(N^2)}` symmetric Hadamard completions. Multiplying by the subquadratic number of subspaces and by the `2^{O(N)}` cut choices preserves `2^{o(N^2)}`. ∎

This reaches exactly the asymptotic entropy scale demanded by Vu's conjecture, but **only on a restricted two-eigenvalue branch with the stated structural conditions**. It is not a proof of the source conjecture.

---

## 7. What remains, now localized more sharply

The old gap was “count sparse Gram roots.” The present theorem resolves a substantial portion of that gap and isolates two complementary bad regimes.

### 7.1 High cube deficiency

If every useful cut/row-tail has `sigma(V)` larger than about `(1/4)log N`, the finite-alphabet enumeration no longer by itself gives a subquadratic family of subspaces. A single logarithmic deficiency is also far too small to settle the full entropy problem. What is needed is an accumulation theorem: large deficiency must persist across enough nested row flags/cuts to pay `Omega(N^2)` bits.

### 7.2 Macroscopic principal-angle multiplicity

Even when the half-rowspace family is subquadratic, a fixed `V` may have `M(V)=Theta(r)`. Formula (4.3) shows exactly where quadratic entropy can then reside: a large block of one repeated principal angle. This is a much sharper structural obstruction than “the cross block may be singular.”

The next attack should therefore be a **multiplicity-or-recursion theorem**:

> For a canonical good cut, either the principal-angle multiplicities are `o(r)`, or a block of multiplicity `rho r` forces a smaller sign-Gram / symmetric-Hadamard instance (or another explicitly countable structure) whose squared dimensions contract under recursion.

The good-cut mixed-energy theorem from the preceding run guarantees a linear number of interior modes on a selected centered cut, but it does not prevent those modes from sharing one repeated angle. That repeated-angle branch is now the principal obstruction.

---

## 8. Current literature boundary checked 20 September 2026

Primary source: Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 / Probability Surveys 18 (2021), Conjecture 9.4.

Ferber–Jain–Zhao, *On the number of Hadamard matrices via anti-concentration* (Combinatorics, Probability and Computing, 2021), give a constant quadratic improvement for general Hadamard enumeration; their discussion emphasizes that obtaining `2^{o(n^2)}` would require substantially new ideas.

Damek Davis, *Counting partial Hadamard matrices in the cubic regime*, arXiv:2603.30013 (submitted 31 March 2026), gives precise asymptotics for rectangular partial Hadamard matrices when the column parameter is on/above the cubic scale. This is a different regime and does not settle the square symmetric fixed-spectrum count here.

A bounded fresh search on 20 September 2026 did not surface a proof of Vu's exact Conjecture 9.4. This is negative search evidence only, not an openness or novelty certificate.

---

## 9. Metric and obligation delta

Frozen full-source metric:

\[
\boxed{N_{\rm exact}:9\to9.}
\]

No small-order census was run.

Mathematical obligation changed materially:

- before this run, near-Odlyzko saturation yielded only column sparsity; now it yields a finite rational alphabet and a `2^{o(n^2)}` count of rich sign-spanned subspaces throughout the regime `16^s(s+1)=o(n)`;
- before this run, completion entropy after fixing a half-rowspace was not quantified basis-free; now it is bounded exactly by the principal-angle multiplicity functional (4.3);
- the singular endpoint is retained explicitly through `a=corank C` and `b=corank D`; the earlier low-corank cut theorem makes the `a` contribution automatically subquadratic;
- the low-deficiency plus diffuse-principal-angle branch of the centered two-eigenvalue problem is now `2^{o(N^2)}`;
- the remaining hard geometry is localized to deficiency accumulation and macroscopic repeated principal angles.

Status remains **PROVED PARTIAL** toward F0011, pending later independent review.
