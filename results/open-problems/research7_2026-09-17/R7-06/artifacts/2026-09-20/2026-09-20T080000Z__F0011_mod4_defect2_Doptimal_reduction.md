Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated binding model/effort selector or runtime telemetry is exposed.

# F0011 — mod-4 rigidity of low-rank Gram defects and exact classification of the first nontrivial defect layer

Date: 2026-09-20 UTC  
Role: C05 / R7-06, current registry native ID `6aabe827777c8191a43330b4a87d481d`  
Canonical target: F0011 / Van H. Vu, *Recent progress in combinatorial random matrix theory*, Conjecture 9.4  
Status: **PROVED PARTIAL** toward the source conjecture, pending later independent review. No source-level closure or external novelty claim.

## 1. Source target and inherited reduction

Vu's Conjecture 9.4 states for the symmetric Rademacher matrix `M_n^sym` (independent fair signs on and above the diagonal, completed by symmetry)

\[
\Pr\bigl(\operatorname{Spec}(M_n^{\rm sym})\subset\mathbb Z\bigr)
=2^{-(1/2+o(1))n^2}.
\tag{1.1}
\]

Equivalently, the total number of labelled symmetric sign matrices with integral spectrum is `2^{o(n^2)}`. The source does **not** impose a fixed spectrum; the fixed-spectrum language below is a project reduction.

The active restricted family is the centered two-eigenvalue slice

\[
H=H^T\in\{\pm1\}^{N\times N},\qquad H^2=NI,
\tag{1.2}
\]

on the integral branch `sqrt(N) in Z`. Write `N=2r` and take a balanced cut

\[
H=\begin{pmatrix}P&C\\ C^T&D\end{pmatrix}.
\tag{1.3}
\]

The preceding C05 report proved that every entropy-near-extremal fixed-half-rowspace fiber has a dominant cross-Gram eigenvalue `lambda` with

\[
K:=CC^T=\lambda I+R,
\qquad \operatorname{rank}R=q=o(r),
\tag{1.4}
\]

\[
\lambda\in2\mathbb Z,
\qquad
|\lambda-r|\le\frac{rq}{r-q},
\tag{1.5}
\]

and simultaneously

\[
P^2=(2r-\lambda)I-R,
\qquad 0\preceq K\preceq2rI.
\tag{1.6}
\]

Because `2r` is an even perfect square, write `2r=(2t)^2`; hence

\[
\boxed{r=2t^2\text{ is even}.}
\tag{1.7}
\]

The missing question was whether (1.4) really collapses to a Hadamard core plus low-complexity defect data. This note proves a strong arithmetic restriction valid in all dimensions and completely classifies `q=1` and `q=2`. The outcome is informative: defect one is impossible, while defect two already lands on the classical Ehlich--Wojtas saturated D-optimal family in one branch. Thus a Hadamard-only recursion is too narrow.

---

## 2. A mod-4 rank lemma for every even-order sign Gram matrix

Let `C in {+-1}^{r x r}` with `r` even and put `K=CC^T`. For row `i`, let `b_i in {0,1}^r` record the positions at which the row of `C` equals `-1`, and let

\[
w_i:=|b_i|\pmod2.
\tag{2.1}
\]

For every pair `i,j`,

\[
K_{ij}
= r-2|b_i|-2|b_j|+4\langle b_i,b_j\rangle.
\tag{2.2}
\]

Since `r` is even, division by two followed by reduction modulo two gives

\[
\frac{K_{ij}}2
\equiv
\frac r2+w_i+w_j
\pmod2.
\tag{2.3}
\]

Therefore, over `F_2`,

\[
\boxed{
\frac K2
\equiv
\left(\frac r2\bmod2\right)J
+w\mathbf1^T+\mathbf1w^T.
}
\tag{2.4}
\]

The right side has column space contained in `span{1,w}`. Hence

\[
\boxed{
\operatorname{rank}_{\mathbb F_2}(K/2)\le2.
}
\tag{2.5}
\]

This is an exact parity skeleton for **every** square sign matrix of even order; no invertibility, spectral simplicity or Hadamard assumption is used.

### Theorem 2.1 — low real-rank defect forces `lambda` to be divisible by four

Assume

\[
R=K-\lambda I,\qquad \lambda\in2\mathbb Z,\qquad
q:=\operatorname{rank}_{\mathbb R}R.
\tag{2.6}
\]

If `lambda = 2 (mod 4)`, then

\[
\boxed{q\ge r-2.}
\tag{2.7}
\]

Equivalently,

\[
\boxed{q<r-2\Longrightarrow \lambda\equiv0\pmod4.}
\tag{2.8}
\]

#### Proof

The matrix `R/2` is integral. Reducing modulo two and using (2.4), if `lambda/2` is odd then

\[
R/2\equiv I+L\pmod2,
\qquad \operatorname{rank}_{\mathbb F_2}L\le2.
\]

Therefore

\[
\operatorname{rank}_{\mathbb F_2}(R/2)
\ge r-\operatorname{rank}_{\mathbb F_2}L
\ge r-2.
\]

For an integer matrix, rank after reduction modulo two cannot exceed its rank over `Q` (a nonzero minor modulo two is an odd, hence nonzero, integer minor). Thus

\[
r-2\le\operatorname{rank}_{\mathbb F_2}(R/2)
\le\operatorname{rank}_{\mathbb Q}(R/2)=q.
\]

This proves (2.7)-(2.8). ∎

### Consequence for the inherited F0011 branch

In (1.4), `q=o(r)`, so eventually `q<r-2`. Hence the repeated cross-Gram scalar satisfies the stronger arithmetic condition

\[
\boxed{\lambda\in4\mathbb Z.}
\tag{2.9}
\]

The same conclusion applies to the repeated scalar `2r-lambda` of `P^2`, consistently with `2r` being divisible by four.

This improves the preceding `lambda in 2Z` conclusion without any determinant estimate and remains valid at the singular/corank endpoint.

---

## 3. Defect one is impossible

### Theorem 3.1

In the inherited integral two-eigenvalue branch, for every sufficiently nontrivial order (`r>=4`),

\[
\boxed{\operatorname{rank}(CC^T-\lambda I)\ne1.}
\tag{3.1}
\]

#### Proof

Suppose `q=1`. By Theorem 2.1, `lambda` is divisible by four. The inherited localization (1.5) gives

\[
|r-\lambda|\le\frac r{r-1}<2.
\tag{3.2}
\]

If `r=2 (mod 4)`, an even integer `r` is distance at least two from every multiple of four, contradicting (3.2).

If `r=0 (mod 4)`, (3.2) forces `lambda=r`. Thus `R=K-rI` is symmetric rank one with zero diagonal. Any real symmetric rank-one matrix has the form `sigma vv^T`; zero diagonal forces `sigma v_i^2=0` for every `i`, hence `R=0`, contradicting rank one.

Therefore `q=1` cannot occur. ∎

So the first genuinely non-Hadamard low-rank layer is `q=2`.

---

## 4. Exact classification of defect two

Assume from now on

\[
q=2,\qquad r\ge6.
\tag{4.1}
\]

Theorem 2.1 again gives `lambda in 4Z`, while (1.5) gives

\[
|r-\lambda|\le\frac{2r}{r-2}<4.
\tag{4.2}
\]

Set

\[
\delta:=r-\lambda=R_{ii}\quad\text{for every }i.
\tag{4.3}
\]

### Case A: `r=0 (mod 4)`

Then `delta=0` by (4.2). Thus `R` is symmetric, rank two, and has zero diagonal.

### Theorem 4.1 — zero-diagonal rank-two defects are exactly weighted bipartite rank-one couplings

After a simultaneous permutation of rows and columns, there is a partition

\[
[r]=A\sqcup B\sqcup Z
\tag{4.4}
\]

such that

\[
\boxed{
R=
\begin{pmatrix}
0&X&0\\
X^T&0&0\\
0&0&0
\end{pmatrix},
\qquad \operatorname{rank}X=1.
}
\tag{4.5}
\]

Moreover `X` has even integer entries.

#### Proof

A nonzero real symmetric rank-two matrix with trace zero has one positive and one negative eigenvalue. Hence it can be written

\[
R=xy^T+yx^T
\tag{4.6}
\]

with linearly independent real vectors `x,y`. The diagonal condition says

\[
0=R_{ii}=2x_i y_i
\tag{4.7}
\]

for every `i`. Thus each coordinate lies in one of three classes: `x_i !=0,y_i=0`; `x_i=0,y_i!=0`; or both zero. These are precisely `A,B,Z`. Equation (4.6) then has the block form (4.5), with `X=x_A y_B^T` of rank one. Since `R=CC^T-rI` and `r` is even, every off-diagonal entry of `R` is an even integer. ∎

Hence the rows of `C` split into two internally orthogonal families (plus possible zero-defect rows), and every nonzero cross-correlation factors through one rank-one matrix.

There is also an arithmetic determinant constraint. Let `sigma>0` be the unique singular value of `X`. Then the nonzero eigenvalues of `R` are `+-sigma`, so

\[
\det K=r^{r-2}(r^2-\sigma^2)=\det(C)^2.
\tag{4.8}
\]

Because `r-2` is even, `r^{r-2}` is an integer square. Therefore

\[
\boxed{r^2-\sigma^2=d^2\text{ for some }d\in\mathbb Z_{\ge0}.}
\tag{4.9}
\]

Thus the defect-two singular value lies on an integral Pythagorean shell with hypotenuse `r`; there are only divisor-function-many possible values of `sigma^2`, although the corresponding sign roots may still be numerous.

### Case B: `r=2 (mod 4)`

Now `delta` is congruent to `2 (mod 4)`, so (4.2) forces

\[
\boxed{\delta\in\{-2,+2\}.}
\tag{4.10}
\]

#### Theorem 4.2 — complete signed two-block classification

Up to a simultaneous signed permutation of rows and columns,

\[
\boxed{
R=+2\,\operatorname{diag}(J_a,J_b)
}
\tag{4.11}
\]

when `delta=+2`, and

\[
\boxed{
R=-2\,\operatorname{diag}(J_a,J_b)
}
\tag{4.12}
\]

when `delta=-2`, where `a,b>=1`, `a+b=r`.

Furthermore:

- in the `+2` case necessarily `a=b=r/2`;
- in the `-2` case necessarily `|a-b|<=2`, hence `a,b` are `r/2,r/2` or `r/2-1,r/2+1` in either order.

#### Proof

Let `alpha,beta` be the two nonzero eigenvalues of `R`.

If `delta=+2`, then `lambda=r-2` and

\[
alpha+beta=\operatorname{tr}R=2r.
\]

Because `0<=K<=2rI`, each defect eigenvalue lies in

\[
-(r-2)\le alpha,beta\le r+2.
\]

If one were nonpositive, the other would be at least `2r`, exceeding `r+2` for `r>2`. Hence `R` is positive semidefinite.

If `delta=-2`, then `lambda=r+2`, `alpha+beta=-2r`, and the same spectral interval argument shows both are negative; thus `-R` is positive semidefinite.

In either case put `S=+-R/2` with the sign chosen so that `S` is PSD. Then `S` is an integer PSD matrix of rank two with diagonal one. By Cauchy--Schwarz,

\[
|S_{ij}|\le1,
\]

so every entry belongs to `{-1,0,1}`. Write `S=XX^T` with unit row vectors `x_i in R^2`. Their pairwise inner products are only `-1,0,1`; therefore any two rows are equal, opposite, or orthogonal. After flipping row signs and permuting indices, all rows of `X` are either one unit vector `e_1` or an orthogonal unit vector `e_2`. Since rank is two, both occur. This gives (4.11)-(4.12).

For the block sizes, consider first the `+2` case. The two exceptional eigenvalues of

\[
K=(r-2)I+2\operatorname{diag}(J_a,J_b)
\]

are `r-2+2a` and `r-2+2b`. The complementary block equation `P^2=2rI-K>=0` implies each is at most `2r`, hence

\[
a,b\le r/2+1.
\]

Since `a+b=r`, write `a=r/2+s`, `b=r/2-s` with `s in {-1,0,1}`. Now

\[
\det K=(r-2)^{r-2}\,4\bigl((r-1)^2-s^2\bigr).
\tag{4.13}
\]

The factor `(r-2)^{r-2}` is a square. Since `det K=det(C)^2`, the integer `(r-1)^2-s^2` must be a square. If `|s|=1`, this number is `r(r-2)=4u(u-1)` with `r=2u`; because consecutive coprime integers `u,u-1` have square product only when both are squares, the only consecutive-square possibility is `0,1`, excluded by `r>=6`. Thus `s=0`, proving `a=b=r/2`.

For the `-2` case,

\[
K=(r+2)I-2\operatorname{diag}(J_a,J_b).
\]

Its exceptional eigenvalues are `r+2-2a` and `r+2-2b`; positivity gives `a,b<=r/2+1`. Together with `a+b=r`, this is equivalent to `|a-b|<=2`. ∎

---

## 5. The positive defect-two branch is exactly the Ehlich--Wojtas saturated D-optimal Gram form

In the `r=2 (mod 4)`, `delta=+2` branch, Theorem 4.2 yields

\[
\boxed{
CC^T=(r-2)I+2\operatorname{diag}(J_{r/2},J_{r/2}).
}
\tag{5.1}
\]

Therefore

\[
|\det C|
=(2r-2)(r-2)^{(r-2)/2}.
\tag{5.2}
\]

This is exactly the classical Ehlich--Wojtas upper bound for `r x r` sign matrices when `r=2 (mod 4)`. Hence:

\[
\boxed{
q=2,\ r=2\pmod4,\ r-\lambda=+2
\Longrightarrow
C\text{ is a saturated D-optimal design.}
}
\tag{5.3}
\]

Conversely, the equality case of the Ehlich--Wojtas bound has precisely the Gram form (5.1), up to signed permutation, so it is exactly this defect-two Gram layer.

This identification is important for the F0011 strategy. The first nonzero defect does **not** generically become “a Hadamard matrix after deleting `O(q)` rows or columns.” At `q=2`, one of the canonical branches is already the classical saturated D-optimal problem, for which infinite construction families are known and whose enumeration is itself nontrivial. A Hadamard-only recursive ansatz is therefore false as a structural classification; the recursive palette must at least include Hadamard and Ehlich--Wojtas/D-optimal nodes.

This is consistent with classical maximal-determinant literature. Ehlich and Wojtas independently proved the `n=2 (mod 4)` determinant bound and its optimal Gram form; modern summaries and D-optimal-design papers record (5.1) as the equality structure. No novelty is claimed for that classical equality characterization. The new project deduction is that the C05 principal-angle defect parameter **forces** the entire `q=2,+2` near-Hadamard branch into exactly that classical class.

---

## 6. Counting consequence at the Gram-skeleton level

The defect-two Gram matrices themselves have only subquadratic description complexity.

- In Case A (`r=0 mod 4`), choose the partition `A,B,Z` in at most `3^r` ways. A rank-one integer matrix `X` with entries in `[-r,r]` is determined by one nonzero row and one nonzero column together with a pivot, giving at most `2^{O(r log r)}` possibilities.
- In Case B (`r=2 mod 4`), the signed two-block form is determined by a bipartition and row switching, hence by only `2^{O(r)}` bits.

Thus

\[
\boxed{
\#\{K:K=CC^T,\ \operatorname{rank}(K-\lambda I)\le2\}
=2^{O(r\log r)}.
}
\tag{6.1}
\]

This does **not** count the sign roots inside one Gram fiber; the `q=2,+2` fiber is D-optimal-hard just as `q=0` is Hadamard-hard. The result nevertheless removes Gram-skeleton entropy at the first two defect levels and identifies the precise remaining object that has to be counted.

---

## 7. What changed and the next bridge

Before this note, the near-extremal obstruction was

\[
CC^T=\lambda I+R,
\qquad \operatorname{rank}R=q=o(r),
\qquad \lambda\in2\mathbb Z,
\qquad |\lambda-r|=O(q).
\]

Now:

1. whenever `q<r-2`, the scalar is automatically `lambda in 4Z`;
2. `q=1` is impossible;
3. `q=2` is completely classified;
4. for `r=2 (mod 4)`, the positive defect-two branch is exactly the saturated Ehlich--Wojtas D-optimal family;
5. the singular endpoint is included: the `delta=-2` branch permits the balanced or one-off-balanced block sizes, with the one-off case having a zero exceptional Gram eigenvalue.

The next structural target should therefore not be “extract a Hadamard core.” A better target is an **Ehlich-block recursion theorem**: for fixed `q=o(r)`, show that a rank-`q` constant-diagonal integral Gram defect decomposes, after signed permutation, into `O(q)` low-complexity correlation blocks plus a residual defect of smaller rank, or construct a counterfamily. If such a decomposition exists with squared block sizes contracting under recursion, Hadamard and saturated D-optimal nodes become the first two exact atoms of a finite extremal-design palette.

A parallel entropy target is to adapt the Ferber--Jain--Zhao inhomogeneous anti-concentration argument to count sign roots uniformly inside these low-rank block-Gram classes, using the fact that the Gram skeleton itself now costs only `2^{O(r log r)}` bits at `q<=2`.

---

## 8. Literature check, 20 September 2026

- Canonical source: Van H. Vu, *Recent progress in combinatorial random matrix theory*, Probability Surveys 18 (2021), Conjecture 9.4, arXiv:2005.02797, DOI 10.1214/20-PS346.
- Ferber--Jain--Zhao, *On the number of Hadamard matrices via anti-concentration*, CPC 31 (2022), 455--477, DOI 10.1017/S0963548321000377, gives the currently relevant general nontrivial Hadamard-count upper bound and explicitly notes that `2^{o(n^2)}` would require new ideas.
- The `n=2 (mod 4)` maximal determinant equality form (5.1) is classical Ehlich--Wojtas theory; modern D-optimal-design literature records the same Gram structure and known infinite construction families.
- A bounded fresh search on 20 September 2026 did not surface a proof of Vu's exact Conjecture 9.4. This is negative search evidence only, not a worldwide openness or novelty certificate.

## 9. Frozen metric

No small-order census was run.

\[
\boxed{N_{\rm exact}:9\to9.}
\]

Mathematical movement is instead the exact low-rank classification above: the unresolved `q=o(r)` branch now has its first two defect levels settled, and the first non-Hadamard level is identified with a classical extremal-design family rather than left as an amorphous low-rank perturbation.
