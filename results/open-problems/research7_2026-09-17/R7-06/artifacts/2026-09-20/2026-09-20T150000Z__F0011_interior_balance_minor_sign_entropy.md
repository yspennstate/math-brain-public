# F0011 — interior rank-two lifts are asymptotically balanced and have subquadratic sign entropy

Date: 2026-09-20 UTC  
Role: C05 / R7-06 `Random Matrix Spectral Entropy`  
Canonical target: F0011 / Van H. Vu, *Recent progress in combinatorial random matrix theory*, Conjecture 9.4  
Status: **PROVED PARTIAL** toward the outside source, pending later independent review

## 1. Source target and inherited point

Vu's Conjecture 9.4 concerns the symmetric Rademacher matrix `M_n^sym`, with independent fair signs on and above the diagonal:

\[
\Pr\bigl(\operatorname{Spec}(M_n^{\rm sym})\subset\mathbb Z\bigr)
=2^{-(1/2+o(1))n^2}.
\]

Equivalently, the total number of labelled symmetric sign matrices with integral spectrum should be `2^{o(n^2)}`. The source quantifier is the total integral-spectrum event, not a fixed spectrum. The present line remains the centered two-eigenvalue / symmetric-Hadamard bridge and does not close the source conjecture.

The latest C05 theorem reduced the rank-two symplectic support in the inherited `|r-lambda|=4`, `q=o(r)`, `q>4` shell to

\[
T=\begin{pmatrix}A&B\\C&F\end{pmatrix},
\qquad
D=T-S^T=\begin{pmatrix}0&J_m\\J_m&0\end{pmatrix},
\qquad d=2m=r-q,
\]

with

\[
T,S\in\{-1,0,1\}^{2m\times2m},
\qquad TS=ST=sI,
\qquad s=\frac r4-\varepsilon,
\qquad \varepsilon\in\{+1,-1\}.
\]

The integer inverse equations force block regularity

\[
A\mathbf1=F\mathbf1=\alpha\mathbf1,
\qquad
B\mathbf1=\beta\mathbf1,
\qquad
C\mathbf1=\gamma\mathbf1,
\]

and the same column sums, with `B,C` binary and

\[
\boxed{\beta+\gamma=m,\qquad \alpha^2=s+\beta\gamma.}
\tag{1.1}
\]

They also force

\[
AA^T+BB^T=sI+\beta J,
\qquad
CC^T+FF^T=sI+\gamma J,
\tag{1.2}
\]

\[
AC^T+BF^T=\alpha J,
\tag{1.3}
\]

and the transposed column analogues. The preceding run excluded the quotient endpoints `beta=0,m` in the actual `q=o(r)` anchor geometry but left the interior two-class family open.

This note proves that the surviving interior quotient is in fact forced into a shrinking window around balance and that, after the binary support is fixed, the signs of the two ternary diagonal blocks contribute only `2^{o(r^2)}` entropy.

---

## 2. Exact support regularity of the ternary diagonal blocks

Take the diagonal of the first equation in (1.2). Since every row of the binary `B` contains exactly `beta` ones,

\[
\|A_i\|_2^2+\beta=s+\beta,
\]

hence

\[
\boxed{\|A_i\|_2^2=s.}
\tag{2.1}
\]

Because `A` is ternary, every row of `A` has exactly `s` nonzero entries. The column equation

\[
A^TA+C^TC=sI+\gamma J
\]

and the fact that every column of the binary `C` has weight `gamma` give the column version. Therefore

\[
\boxed{|A|\mathbf1=s\mathbf1,\qquad |A|^T\mathbf1=s\mathbf1.}
\tag{2.2}
\]

The same argument gives

\[
\boxed{|F|\mathbf1=s\mathbf1,\qquad |F|^T\mathbf1=s\mathbf1.}
\tag{2.3}
\]

Put `a:=|alpha|`. Since every row and column of `A` has exactly `s` signs summing to `alpha`, after one global majority-sign normalization each row and each column contains exactly

\[
\boxed{\nu:=\frac{s-a}{2}}
\tag{2.4}
\]

minority signs. The same is true for `F`. In particular `a<=s` and `a congruent s (mod 2)`.

---

## 3. A constant-intersection packing lemma

We use the following elementary lemma.

**Lemma.** Let `z_1,...,z_t in {0,1}^v` have constant weight `k` and constant pairwise intersection `lambda`:

\[
|\operatorname{supp}z_i|=k,
\qquad
|\operatorname{supp}z_i\cap\operatorname{supp}z_j|=\lambda
\quad(i\ne j).
\]

If `k^2>v lambda`, then

\[
\boxed{
 t\le \frac{v(k-\lambda)}{k^2-v\lambda}.
}
\tag{3.1}
\]

**Proof.** Let `d_j` be the column degrees of the `t x v` incidence matrix. Then

\[
\sum_j d_j=tk,
\qquad
\sum_j d_j^2=tk+t(t-1)\lambda.
\]

Cauchy--Schwarz gives

\[
\frac{t^2k^2}{v}
\le tk+t(t-1)\lambda.
\]

After rearranging,

\[
t(k^2-v\lambda)\le v(k-\lambda),
\]

which is (3.1). `square`

This is a quantitative Fisher-type bound: a large constant-intersection family can exist only when the denominator `k^2-v lambda` is correspondingly small.

---

## 4. Anchor classes turn the top and bottom halves into constant-intersection families

The inherited C05 anchor geometry partitions each defect half into at most `2q` refined row classes with the following property: for two rows in one refined class, the product of the `A`-signs on every common nonzero `E=0` coordinate is one fixed sign, independent of the column. The analogous statement holds for `F` in the bottom half.

Take two distinct top-half rows `i,j` in one refined class. Write

\[
a_{ij}:=|\operatorname{supp}A_i\cap\operatorname{supp}A_j|,
\qquad
b_{ij}:=(BB^T)_{ij}.
\]

Anchor coherence gives

\[
A_i\cdot A_j=\sigma_{ij}a_{ij},
\qquad \sigma_{ij}\in\{+1,-1\}.
\]

On the other hand, (1.2) gives

\[
A_i\cdot A_j=\beta-b_{ij}\ge0.
\]

If `sigma_ij=+1`, then `a_ij=beta-b_ij`. If `sigma_ij=-1`, nonnegativity forces both sides to vanish, so again `a_ij+b_ij=beta`. Therefore, for the binary concatenated support row

\[
W_i:=\bigl(\mathbf1_{\operatorname{supp}A_i},\,B_i\bigr)\in\{0,1\}^{2m},
\]

we have

\[
\boxed{|W_i|=s+\beta,\qquad |W_i\cap W_j|=\beta.}
\tag{4.1}
\]

Thus every refined top class is an exact constant-intersection family with parameters

\[
(v,k,\lambda)=(2m,s+\beta,\beta).
\]

Likewise every refined bottom class, using

\[
Z_i:=\bigl(C_i,\mathbf1_{\operatorname{supp}F_i}\bigr),
\]

has

\[
\boxed{|Z_i|=s+\gamma,\qquad |Z_i\cap Z_j|=\gamma.}
\tag{4.2}
\]

---

## 5. New theorem I — the interior quotient is forced asymptotically to `beta=gamma=m/2`

For the top classes, the denominator in (3.1) is

\[
\begin{aligned}
\Phi_\beta
&:=(s+\beta)^2-2m\beta\\
&=(\beta-(m-s))^2+m(2s-m).
\end{aligned}
\tag{5.1}
\]

In the inherited shell

\[
2s-m=\frac q2-2\varepsilon>0
\]

because `q>4`, so `Phi_beta>0`. The class bound gives

\[
t\le\frac{2ms}{\Phi_\beta}.
\tag{5.2}
\]

At most `2q` refined top classes cover the `m` top rows, hence

\[
 m\le2q\frac{2ms}{\Phi_\beta},
\]

or

\[
\boxed{\Phi_\beta\le4qs.}
\tag{5.3}
\]

Applying the same argument to the bottom classes gives

\[
\boxed{\Phi_\gamma:=(s+\gamma)^2-2m\gamma\le4qs.}
\tag{5.4}
\]

Set

\[
h:=s-\frac m2=\frac q4-\varepsilon>0,
\qquad
x:=\beta-\frac m2,
\qquad
\gamma=\frac m2-x.
\]

Then

\[
\Phi_\beta=(x+h)^2+2mh,
\qquad
\Phi_\gamma=(x-h)^2+2mh.
\]

Since

\[
\max\{|x+h|,|x-h|\}=|x|+h,
\]

(5.3)--(5.4) imply the exact quantitative balance bound

\[
\boxed{
(|x|+h)^2+2mh\le4qs.
}
\tag{5.5}
\]

Equivalently,

\[
\boxed{
\left|\beta-\frac m2\right|
\le
\sqrt{4qs-2mh}-h.
}
\tag{5.6}
\]

The same bound holds for `gamma` by symmetry. Since `h=O(q)` and `q=o(m)`, this yields

\[
\boxed{
\beta=\frac m2+O(\sqrt{mq}),
\qquad
\gamma=\frac m2+O(\sqrt{mq}).
}
\tag{5.7}
\]

In particular,

\[
\boxed{\beta/m\to1/2,\qquad \gamma/m\to1/2.}
\tag{5.8}
\]

So the actual anchor geometry removes not only the exact weighing endpoints. It removes **every linearly unbalanced interior quotient** in the entropy-dangerous `q=o(r)` branch.

This is a genuinely stronger use of the anchor partition than the preceding endpoint exclusion.

---

## 6. New theorem II — the ternary diagonal blocks have only `O(q)` minority signs per row and column

From (1.1), with `a=|alpha|`,

\[
a^2=s+\beta\gamma
=s+\frac{m^2}{4}-x^2.
\tag{6.1}
\]

Since `s=m/2+h`,

\[
s^2-a^2
=mh+h^2-\frac m2-h+x^2.
\tag{6.2}
\]

For all sufficiently large instances in the `q=o(m)` regime we may assume `q<=m`. Then `h<=q/2`, `s<=m`, and (5.5) gives `x^2<=4qs-2mh<=4qm`. Therefore

\[
0\le s^2-a^2
\le mh+h^2+x^2
\le \frac{qm}{2}+\frac{q^2}{4}+4qm
\le \frac{19}{4}qm.
\tag{6.3}
\]

Since `s+a>=s>=m/2`,

\[
\boxed{s-a\le\frac{19}{2}q.}
\tag{6.4}
\]

Consequently the minority-sign degree (2.4) satisfies the concrete bound

\[
\boxed{\nu\le5q}
\tag{6.5}
\]

for all sufficiently large inherited instances.

Thus, after one majority-sign normalization, both `A` and `F` are `s`-regular ternary matrices whose negative-support graph has row and column degree only `O(q)=o(m)`.

---

## 7. New theorem III — the signs contribute only subquadratic entropy once the support is fixed

Fix the binary supports

\[
P:=|A|,
\qquad
Q:=|F|.
\]

Each row of `A` has exactly `nu<=5q` minority locations among its `s` support locations, and the same is true for `F`. Ignoring the additional column constraints only enlarges the count, so the number of possible signings is at most

\[
2\binom{s}{\nu}^{2m}.
\tag{7.1}
\]

Using the standard binomial bound,

\[
\log_2\binom{s}{\nu}
\le \nu\log_2\!\left(\frac{es}{\nu}\right),
\]

we obtain

\[
\boxed{
\log_2 N_{\rm sign}
=O\!\left(mq\log\left(\frac mq+2\right)\right)
=o(m^2).
}
\tag{7.2}
\]

Therefore, on this rank-two support, **quadratic entropy cannot come from the ternary signs**. Up to `2^{o(r^2)}` overhead, it is entirely a binary-support problem.

This statement is stronger than merely saying that the anchor masks themselves have subquadratic description length: the integer Gram equations force the *actual minority signs inside every row and column* to have vanishing density.

---

## 8. Corollary — a two-sided near-Hadamard support matrix

After the majority normalization write

\[
A=P-2N_A,
\qquad
F=Q-2N_F,
\]

where every row and column of `N_A,N_F` has degree `nu<=5q`. Let

\[
X:=|T|=\begin{pmatrix}P&B\\C&Q\end{pmatrix}
\in\{0,1\}^{2m\times2m}.
\tag{8.1}
\]

For two distinct top rows, (1.2) gives

\[
(PP^T+BB^T)_{ij}
=
\beta
+2(PN_A^T+N_AP^T)_{ij}
-4(N_AN_A^T)_{ij}.
\]

Each correction term is bounded by `nu`, so

\[
\boxed{
\left|(PP^T+BB^T)_{ij}-\beta\right|\le8\nu\le40q.
}
\tag{8.2}
\]

The bottom-half analogue holds with `gamma`. The mixed equation becomes

\[
PC^T+BQ^T
=aJ+2N_AC^T+2BN_F^T,
\]

hence

\[
\boxed{
0\le (PC^T+BQ^T)_{ij}-a\le4\nu\le20q.
}
\tag{8.3}
\]

Define the centered sign support matrix

\[
H:=2X-J_{2m}.
\tag{8.4}
\]

The top row weight of `X` is `s+beta`, the bottom row weight is `s+gamma`, and `s-a=2nu`. Substituting (8.2)--(8.3) gives a uniform off-diagonal correlation bound

\[
\boxed{
|\langle H_i,H_j\rangle|\le170q
\qquad(i\ne j).
}
\tag{8.5}
\]

The column Gram equations give the same estimate for distinct columns. Since `q=o(m)`, every admissible lift therefore produces a square sign matrix whose rows and columns are pairwise `o(m)`-correlated.

So the remaining binary-support problem is now a sharply constrained **two-sided near-Hadamard** problem, not an arbitrary dense binary orientation.

This does not itself give a subquadratic count: when `q` is much larger than `sqrt(m)`, `o(m)` correlations alone are too weak to exclude random-like sign behavior. The exact low-complexity anchor partition and the inverse equations must still be used.

---

## 9. What this removes, and the next missing theorem

The previous rank-two theorem left all interior quotient triples

\[
1\le\beta,\gamma\le m-1,
\qquad
\beta+\gamma=m,
\qquad
\alpha^2=s+\beta\gamma
\]

as possible entropy carriers. The present theorem removes most of that region:

\[
\boxed{
\beta,\gamma=\frac m2+O(\sqrt{mq}),
\qquad
|\alpha|=s-O(q),
\qquad
\nu=O(q).
}
\tag{9.1}
\]

Moreover the sign choices inside `A,F` cost only `2^{o(r^2)}`. Any surviving quadratic entropy must therefore live in the **binary support matrix** `X=|T|`, subject simultaneously to:

1. two class degrees `s+beta` and `s+gamma` that are `m+o(m)`;
2. two-sided row and column correlations `O(q)=o(m)` after centering;
3. the inherited `q`-block anchor structure;
4. the exact signed inverse relation `TS=ST=sI`;
5. the finite-field inverse-transpose / dual-code shadow from the preceding binary-support theorem.

The next useful target is a support-entropy theorem that uses the `q` anchor classes **together with** the near-Hadamard support correlations. A natural route is a stability/recursion dichotomy: either a refined class is far from saturating the constant-intersection packing bound and pays a definite entropy loss, or near-saturation forces a smaller exact/near design block whose squared dimensions contract.

The bounded-rank `q<=4` Hadamard/D-optimal branch, higher arithmetic shells, indefinite defects, the full centered two-eigenvalue count, and finally Vu's total integral-spectrum conjecture remain open.

The singular/corank endpoint of the original sign cross-block remains included throughout: this argument uses only the already singular-safe contrast-core equations and never inverts the original cross-block.

---

## 10. Current literature boundary (bounded check)

A bounded current search on 20 September 2026 did not surface a resolution of Vu's exact Conjecture 9.4. This is negative-search evidence only, not an openness or novelty certificate.

Relevant nearby literature still includes:

* Asaf Ferber, Vishesh Jain and Yufei Zhao, *On the number of Hadamard matrices via anti-concentration*, Combinatorics, Probability and Computing 31 (2022), DOI `10.1017/S0963548321000377`: a constant quadratic improvement for general Hadamard enumeration, not a `2^{o(n^2)}` count.
* Tuomo Valtonen, *Classification of Symmetric Hadamard Matrices Up to Order 32*, arXiv `2608.06920`, updated 10 September 2026: finite classification through order 32, not an asymptotic entropy theorem.
* Damek Davis, *Counting partial Hadamard matrices in the cubic regime*, arXiv `2603.30013` (31 March 2026): precise rectangular partial-Hadamard asymptotics in a cubic regime, not the present near-square symmetric fixed-spectrum fiber.

No external novelty claim is made for the elementary constant-intersection inequality itself. The project advance is its use with the source-specific anchor classes to force the surviving F0011 quotient to balance, followed by the `O(q)` minority-sign and subquadratic sign-entropy consequences.
