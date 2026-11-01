# F0011 — arithmetic stratification, punctured partial-Hadamard anchor classes, and a codimension-two completion branch

Date: 2026-09-20 UTC  
Role: C05 / R7-06 `Random Matrix Spectral Entropy`  
Canonical target: F0011 / Van H. Vu, *Recent progress in combinatorial random matrix theory*, Conjecture 9.4  
Status: **PROVED PARTIAL** toward the outside source, pending later independent review. No source-level closure or external novelty claim is made.

## 1. Exact source and inherited bottleneck

Vu's Conjecture 9.4 concerns the symmetric Rademacher matrix `M_n^sym`, with independent fair signs on and above the diagonal:

\[
\Pr\bigl(\operatorname{Spec}(M_n^{\rm sym})\subset\mathbb Z\bigr)
=2^{-(1/2+o(1))n^2}.
\]

Equivalently, the total number of labelled symmetric sign matrices with integral spectrum should be `2^{o(n^2)}`. The source quantifier is the total integral-spectrum event, not a fixed spectrum. The present line remains a restricted centered two-eigenvalue / symmetric-Hadamard bridge.

The latest own report is

`research7_2026-09-17/R7-06/runs/2026-09-20/2026-09-20T151000Z__report.md`.

It reduced the entropy-dangerous rank-two support in the inherited semidefinite `|r-lambda|=4`, `q=o(r)`, `q>4` shell to

\[
T=\begin{pmatrix}A&B\\C&F\end{pmatrix},
\qquad
D=T-S^T=\begin{pmatrix}0&J_m\\J_m&0\end{pmatrix},
\qquad
2m=r-q,
\]

with

\[
T,S\in\{-1,0,1\}^{2m\times2m},
\qquad TS=ST=sI,
\qquad s=\frac r4-\varepsilon,
\qquad \varepsilon\in\{+1,-1\}.
\]

The off-diagonal blocks `B,C` are binary and regular with degrees `beta,gamma`; the diagonal ternary blocks `A,F` have common row/column sum `alpha`. The exact quotient identities are

\[
\boxed{\beta+\gamma=m,\qquad \alpha^2=s+\beta\gamma.}
\tag{1.1}
\]

Writing `a:=|alpha|`, the exact support theorem gives `s` nonzeros in every row and column of `A,F`, and after one majority-sign normalization every row and column has exactly

\[
\boxed{\nu=(s-a)/2}
\tag{1.2}
\]

minority signs. The previous run proved `nu<=5q` and reduced all remaining quadratic entropy to the binary support.

It also proved that each refined top anchor class consists of binary rows

\[
W_i=(|A_i|,B_i)\in\{0,1\}^{2m}
\]

with

\[
|W_i|=s+\beta,
\qquad
|W_i\cap W_j|=\beta\quad(i\ne j),
\tag{1.3}
\]

and the bottom classes have the analogous parameters `(2m,s+gamma,gamma)`. There are at most `2q` refined row classes in each half, and the transposed anchor geometry gives the same statement for refined column classes.

This note extracts two new consequences from that exact structure: a discrete Diophantine stratification of the quotient/minority degree, and an exact conversion of every refined anchor class into a punctured partial Hadamard system. It then completely identifies the unique zero-minority rank-two subbranch with a codimension-two partial Hadamard that always completes to a full Hadamard matrix.

---

## 2. Preliminary arithmetic: `r` is divisible by four

Because `T,S` are integral and `TS=sI`, the scalar `s` is an integer. Since

\[
s=\frac r4-\varepsilon
\]

with integer `epsilon`, we have

\[
\boxed{4\mid r.}
\tag{2.1}
\]

Put

\[
\delta:=\beta-\gamma.
\]

From `beta+gamma=m` and (1.1),

\[
\boxed{
\delta^2+(2\alpha)^2=m^2+4s.
}
\tag{2.2}
\]

Also write

\[
h:=s-\frac m2=\frac q4-\varepsilon,
\qquad
L:=4h=q-4\varepsilon.
\tag{2.3}
\]

Because `q>4`, `L>0` in both signs of the shell. Note the exact identities

\[
\boxed{4s=2m+L=r-4\varepsilon.}
\tag{2.4}
\]

---

## 3. New theorem A — exact Diophantine stratification of the balanced quotient

The previous run gave only the soft window

\[
\beta=\frac m2+O(\sqrt{mq}),
\qquad
\gamma=\frac m2+O(\sqrt{mq}),
\qquad
\nu=O(q).
\]

The integral circle (2.2) discretizes this much more sharply.

Because `q=o(m)`, for every sufficiently large inherited instance

\[
m^2+4s<(m+2)^2.
\tag{3.1}
\]

Hence `2a=2|alpha|<m+2`. Since `2a` is even, there are two parity cases.

### 3.1. `m` even

Then `q congruent 0 (mod 4)` by `4|(2m+q)`. Put

\[
M:=\frac m2,
\qquad
H:=h=\frac q4-\varepsilon\in\mathbb Z_{\ge0}.
\]

Since `2a<=m`, there is an integer `k>=0` such that

\[
\boxed{a=M-k.}
\tag{3.2}
\]

Equation (1.2) becomes

\[
\boxed{2\nu=H+k.}
\tag{3.3}
\]

In particular `H+k` is even. Since the inherited theorem gives `nu<=5q`,

\[
\boxed{k=O(q).}
\tag{3.4}
\]

As `delta` is even, put `x:=delta/2`. Substituting (3.2) into (2.2) gives the exact square equation

\[
\boxed{
x^2=(2k+1)M+H-k^2.
}
\tag{3.5}
\]

Thus the quotient is not a continuous `O(sqrt(mq))` window: it lies on `O(q)` explicit integral square shells indexed by `k`.

### 3.2. `m` odd

Then `q congruent 2 (mod 4)`. Put

\[
M:=\frac{m+1}{2},
\qquad
H:=h-\frac12=\frac{q-2}{4}-\varepsilon\in\mathbb Z_{\ge0}.
\]

Since `2a` is even and `2a<m+2`, there is an integer `k>=0` such that

\[
\boxed{a=M-k.}
\tag{3.6}
\]

Again

\[
\boxed{2\nu=H+k,\qquad k=O(q).}
\tag{3.7}
\]

Now `delta` is odd, and (2.2) becomes

\[
\boxed{
\delta^2=1+4\bigl(H+k(m+1-k)\bigr).
}
\tag{3.8}
\]

Equivalently,

\[
\boxed{
\frac{\delta^2-1}{4}=H+k(m+1-k).
}
\tag{3.9}
\]

Again only `O(q)` Diophantine shells are possible.

### 3.3. Minority signs are actually `Theta(q)`, except for one explicit branch

Equations (3.3) and (3.7) give the lower bound

\[
\boxed{\nu\ge H/2.}
\tag{3.10}
\]

Together with the inherited `nu<=5q`, the minority degree is therefore of order `q` throughout the growing-defect regime, rather than merely being bounded above by `O(q)`.

More precisely, `nu=0` forces `H=0` and `k=0`. The even-`m` case cannot have `H=0` when `q>4`. In the odd-`m` case,

\[
H=0
\iff
\frac{q-2}{4}-\varepsilon=0.
\]

With `q>4`, this has the unique solution

\[
\boxed{\varepsilon=+1,\qquad q=6.}
\tag{3.11}
\]

Thus:

\[
\boxed{
\nu=0
\text{ occurs in the rank-two }q>4\text{ shell only for the positive shell }q=6.
}
\tag{3.12}
\]

This exact exceptional branch will be completed in Section 6.

---

## 4. New theorem B — every refined anchor class is a punctured partial Hadamard system

Take one refined top anchor class `R` of size `t`. For its rows `W_i` from (1.3), define centered sign vectors

\[
y_i:=2W_i-\mathbf 1_{2m}\in\{\pm1\}^{2m}.
\tag{4.1}
\]

Since `|W_i|=s+beta` and `|W_i cap W_j|=beta`,

\[
\begin{aligned}
y_i\cdot y_j
&=4|W_i\cap W_j|-2|W_i|-2|W_j|+2m\\
&=4\beta-4(s+\beta)+2m\\
&=2m-4s\\
&=-L
\qquad(i\ne j),
\end{aligned}
\tag{4.2}
\]

while `||y_i||^2=2m`.

Append to every row the same `L=q-4epsilon` signs `+1`:

\[
\widetilde y_i:=(y_i,\mathbf1_L)
\in\{\pm1\}^{2m+L}.
\tag{4.3}
\]

Then for `i ne j`,

\[
\widetilde y_i\cdot\widetilde y_j=-L+L=0,
\]

and

\[
||\widetilde y_i||^2=2m+L=4s.
\]

Therefore:

\[
\boxed{
\widetilde Y_R\in\{\pm1\}^{t\times 4s},
\qquad
\widetilde Y_R\widetilde Y_R^T=4sI_t.
}
\tag{4.4}
\]

So every refined top anchor class is exactly a **partial Hadamard matrix of width `4s=r-4epsilon` after a common tail of `q-4epsilon` columns is restored**. The bottom classes satisfy the same theorem because their centered inner product is also

\[
4\gamma-4(s+\gamma)+2m=-L.
\]

By the transposed anchor theorem, the same construction applies to all refined column classes.

This is stronger than saying the surviving support is merely near-Hadamard: inside every anchor class, the correlations can be removed **exactly** by restoring a common tail whose length is the original Gram scalar defect `q-4epsilon`.

### Converse inside one class

Conversely, suppose a sign family in `4s` columns has pairwise orthogonal rows, its final `L` columns are all `+1`, and the punctured first `2m` coordinates have the prescribed common row sum corresponding to weight `s+beta`. Deleting the common tail gives (4.2), hence constant Hamming distance `2s`; the fixed row weight then recovers `|W_i cap W_j|=beta`. Thus the refined-class condition is exactly a **common-tail puncturing of a partial Hadamard family**, plus the fixed row-sum constraint.

---

## 5. New theorem C — anchor-class dimensions already have a contracting square-sum profile when `q` grows

The Gram matrix of the unbordered centered rows in a class of size `t` is

\[
G_t=(2m+L)I_t-LJ_t.
\tag{5.1}
\]

Its eigenvalue in the all-ones direction is

\[
2m-L(t-1).
\]

Positive semidefiniteness therefore forces

\[
\boxed{
t\le 1+\frac{2m}{L}
=1+\frac{2m}{q-4\varepsilon}.
}
\tag{5.2}
\]

Let the nonempty refined top-row class sizes be `t_1,...,t_ell`, so `sum_i t_i=m`. Then

\[
\boxed{
\ell\ge
\frac{m(q-4\varepsilon)}{2m+q-4\varepsilon}.
}
\tag{5.3}
\]

In the inherited `q=o(m)` regime this is

\[
\boxed{\ell\ge(1/2-o(1))(q-4\varepsilon).}
\tag{5.4}
\]

Thus the anchor partition is not only bounded above by `2q`; it is forced to have order `q` nonempty refined classes.

Moreover,

\[
\sum_i t_i^2
\le
\left(1+\frac{2m}{q-4\varepsilon}\right)m,
\]

so

\[
\boxed{
\sum_i t_i^2
\le
m+\frac{2m^2}{q-4\varepsilon}.
}
\tag{5.5}
\]

The same estimate holds for the bottom-row classes and for both families of refined column classes.

Therefore, along every sequence with

\[
q\to\infty,
\qquad q=o(m),
\]

we obtain the genuine square-dimension contraction

\[
\boxed{
\sum_i t_i^2=o(m^2).
}
\tag{5.6}
\]

This does **not** yet prove the desired entropy recursion: the cross-class gluing data are not shown here to have subquadratic entropy. But it proves that the natural anchor-class child dimensions themselves already satisfy exactly the square-sum contraction needed by such a recursion. The remaining theorem must control only the gluing between these punctured partial-Hadamard pieces.

### Relation to the 2026 partial-Hadamard counting regime

Damek Davis, *Counting partial Hadamard matrices in the cubic regime*, arXiv:2603.30013 (31 March 2026), proves precise asymptotics for `n x 4t` partial Hadamard matrices when `t/n^3` tends to infinity, and also in a sufficiently large constant cubic regime.

Here an anchor class of size `t_i` gives a `t_i x 4s` partial Hadamard matrix. By (5.2),

\[
t_i\le (2+o(1))\frac m q,
\qquad s=(1/2+o(1))m.
\]

Hence

\[
\frac{s}{t_i^3}
\ge
\Omega\left(\frac{q^3}{m^2}\right).
\tag{5.7}
\]

Consequently, when

\[
q/m^{2/3}\to\infty,
\]

every growing anchor class lies in Davis's solved cubic-or-better partial-Hadamard regime. This is a real literature bridge, but it is only classwise: Davis's theorem does not count the simultaneous row/column gluing imposed by the C05 inverse equations, so it does not by itself close the shell.

---

## 6. New theorem D — the unique zero-minority branch reduces to a full Hadamard matrix of order `r-4`

By (3.12), `nu=0` is possible only when

\[
\varepsilon=+1,
\qquad q=6,
\qquad m\text{ odd}.
\tag{6.1}
\]

Then

\[
s=\frac{m+1}{2},
\qquad H=0,
\qquad k=0.
\]

Equation (3.8) gives

\[
\delta^2=1.
\]

Thus, after possibly swapping the two halves,

\[
\boxed{
\beta=s,\qquad \gamma=s-1,
\qquad a=|\alpha|=s.
}
\tag{6.2}
\]

Because `nu=0`, the ternary diagonal blocks have only one sign on their support. After the majority normalization, the entire support matrix

\[
X=|T|\in\{0,1\}^{2m\times2m}
\]

contains all remaining information up to the already-subquadratic anchor data.

Define

\[
H:=2X-J_{2m}\in\{\pm1\}^{2m\times2m}.
\tag{6.3}
\]

The exact support Gram equations give:

* distinct rows in the same half have centered inner product `-2`;
* rows in opposite halves have centered inner product `0`;
* every row has norm squared `2m`.

Indeed the within-half value is `2m-4s=-2`, while the mixed support intersection is exactly `s`, giving centered mixed product zero.

Append two columns to `H` as follows:

* every top-half row receives tail `(1,1)`;
* every bottom-half row receives tail `(1,-1)`.

Call the resulting matrix `Y`. Then `Y` has

\[
N:=2m+2=4s=r-4
\]

columns and `N-2=2m` rows. The added tails contribute `+2` within either half and `0` across halves. Therefore

\[
\boxed{
Y\in\{\pm1\}^{(N-2)\times N},
\qquad YY^T=NI_{N-2}.
}
\tag{6.4}
\]

So the unique zero-minority rank-two branch produces a codimension-two partial Hadamard matrix of order `N=r-4`.

### Codimension-two completion lemma

**Lemma.** Let `N` be divisible by four. Every

\[
Y\in\{\pm1\}^{(N-2)\times N}
\quad\text{with}\quad
YY^T=NI_{N-2}
\]

extends by two sign rows to an `N x N` Hadamard matrix.

**Proof.** Put

\[
P:=I_N-\frac1N Y^TY.
\]

Since the rows of `Y/sqrt(N)` are orthonormal, `P` is the orthogonal projector onto their two-dimensional orthogonal complement. Its diagonal is

\[
P_{ii}=1-\frac{N-2}{N}=\frac2N.
\]

Set

\[
R:=\frac N2 P.
\]

Then `R` is positive semidefinite of rank two with diagonal one. For `i ne j`,

\[
R_{ij}=-\frac12(Y^TY)_{ij}.
\]

The dot product of two sign columns of length `N-2` is even, so `R` is integral. Positive semidefiniteness and unit diagonal give `|R_ij|<=1`; hence

\[
R_{ij}\in\{-1,0,1\}.
\]

Represent `R` as the Gram matrix of `N` unit vectors in `R^2`. Pairwise inner products in `{-1,0,1}` force all vectors to lie on two orthogonal lines, with signs. The two nonzero eigenvalues of `R=(N/2)P` are both `N/2`; therefore exactly `N/2` vectors lie on each line.

After an orthogonal change of basis and recording the line signs, construct `z_1,z_2 in {+/-1}^N` by assigning `(z_{1i},z_{2i})=(sigma_i,sigma_i)` on the first line and `(tau_i,-tau_i)` on the second. Then

\[
z_1\cdot z_2=0,
\qquad
z_1z_1^T+z_2z_2^T=NP,
\]

so both rows lie in the orthogonal complement of the rows of `Y`. Stacking `z_1,z_2` under `Y` gives a full Hadamard matrix. `square`

Applying the lemma to (6.4):

\[
\boxed{
\text{every }q=6,\ \varepsilon=+1,\ \nu=0\text{ root yields a Hadamard matrix of order }r-4.
}
\tag{6.5}
\]

The completion is unique up to the usual signed permutation of the two complementary rows. Encoding which two rows/columns are the completion/tail coordinates, which `m` rows form each half, and the fixed `q=6` anchor data costs only `2^{O(r log r)}` possibilities. Therefore, if `H(N)` denotes the number of labelled Hadamard matrices of order `N`, the number of C05 roots in this subbranch obeys

\[
\boxed{
N_{q=6,\nu=0}(r)
\le
2^{O(r\log r)} H(r-4).
}
\tag{6.6}
\]

Using the Ferber--Jain--Zhao nontrivial Hadamard-count upper bound immediately gives a strict quadratic entropy saving for this branch, although not the `2^{o(r^2)}` bound required for source closure.

This is an actual recursive identification, not merely a similarity: the exceptional zero-minority branch is a two-row deletion of a full Hadamard problem at order `r-4`.

---

## 7. What this run rules out and what it leaves

The run materially narrows the rank-two interior branch in four ways.

1. The quotient/minority parameters lie on `O(q)` explicit Diophantine square shells, not a continuous `O(sqrt(mq))` window.
2. Except for the single positive-shell `q=6` branch, the minority-sign degree has a positive lower bound of order `q`; the perturbation is sparse on the `m^2` scale but is not allowed to vanish.
3. Every refined row and column anchor class is exactly a common-tail puncturing of a partial Hadamard family of width `4s=r-4epsilon`.
4. If `q->infinity`, the sum of squared refined-class dimensions is `o(m^2)`, so the natural class recursion has the correct contraction profile. The missing step is now explicitly the **cross-class gluing entropy**.
5. The unique zero-minority branch is completely reduced to a full Hadamard matrix of order `r-4`, with only subquadratic auxiliary encoding.

This also identifies a failed intermediate reduction: it would be incorrect to declare the classwise partial-Hadamard decomposition itself sufficient for source entropy. Even Davis's 2026 asymptotic, which applies classwise for `q>>m^(2/3)`, leaves the simultaneous cross-class row/column gluing uncontrolled. That gluing is precisely where the exact inverse equations must next be used.

The singular/corank endpoint remains included. No inversion of the original sign cross-block `C` was used; all arguments occur inside the inherited contrast-core system where `TS=sI` is already valid.

---

## 8. Next attack

The next theorem should attack the gluing rather than re-count individual classes.

For `q->infinity`, use the exact square-sum contraction (5.6) and seek a block-recursion theorem showing that, after `2^{o(r^2)}` quotient data, every off-diagonal interaction between anchor classes is determined by child partial-Hadamard pieces whose squared dimensions sum to `o(m^2)`.

For bounded `q`, use the Diophantine index `k` and the exact regular minority degree `nu=(H+k)/2`. The case `nu=0` is now removed into a smaller full Hadamard instance. The first unresolved bounded-defect cases therefore have `nu>=1`; their negative supports are `nu`-regular bipartite graphs and decompose into `nu=O(1)` matchings. The concrete next question is whether the inverse equations force those matching perturbations to be finite-rank trades of the `q=6` Hadamard completion, or whether they generate a genuinely new group-divisible design family.

A counterfamily in the latter direction would also be useful, because it would identify the correct recursive atom rather than repeatedly treating every bounded defect as a perturbation of Hadamard.

---

## 9. Current literature positioning

A bounded current search on 20 September 2026 did not surface a resolution of Vu's exact Conjecture 9.4; this is negative-search evidence only.

Relevant boundaries used here:

* Asaf Ferber, Vishesh Jain, Yufei Zhao, *On the number of Hadamard matrices via anti-concentration*, Combinatorics, Probability and Computing 31 (2022), 455--477. This gives the first nontrivial quadratic improvement for square Hadamard counting, not a `2^{o(n^2)}` count.
* Damek Davis, *Counting partial Hadamard matrices in the cubic regime*, arXiv:2603.30013, submitted 31 March 2026. Theorem 1.1 gives a precise asymptotic for `n x 4t` partial Hadamards for `t>=C_0 n^3`, and the paper states that below the cubic scale the asymptotics remain open.
* The balancedly-splittable Hadamard/design literature is structurally adjacent to the punctured-class theorem, but no external classification result is invoked in the proofs above.

---

## 10. Frozen metric and obligation ledger

Frozen full-source finite metric remains

\[
\boxed{N_{\rm exact}:9\to9.}
\]

No small-order census was run.

Obligation ledger:

- exact Vu source statement and total-spectrum quantifier: preserved;
- latest C05 rank-two integer theorem recovered first: yes;
- singular/corank endpoint: retained;
- quotient balance window: sharpened to explicit Diophantine shells;
- minority-sign degree: sharpened from `O(q)` to a two-sided `Theta(q)` scale except one explicit branch;
- refined anchor classes: identified exactly as common-tail punctured partial Hadamards;
- class square-sum profile: proved contracting for `q->infinity`;
- unique zero-minority branch: reduced to full Hadamard order `r-4` via a proved codimension-two completion lemma;
- cross-class gluing entropy: **OPEN**;
- bounded-defect `nu>=1` matching perturbations: **OPEN**;
- full centered two-eigenvalue count: **OPEN**;
- Vu Conjecture 9.4: **OPEN**.
