# Exact geometry of attainable fixed points

Research note, 14 September 2026. This is the complete fixed-point geometry and sensitivity argument from [agent049](agents/049.md), independently read and checked by the parent. It characterizes which probability vectors can be fixed points in every dimension, and improves a quantitative four-type estimate. Historical novelty and optimality of the final sensitivity constant are not asserted.

For \(n\ge3\), a symmetric strictly non-Volterra quadratic stochastic operator has the form
\[
V_P(x)_k=\sum_{i,j=1}^nP_{ij,k}x_ix_j,\qquad
P_{ij,k}=P_{ji,k}\ge0,\quad\sum_kP_{ij,k}=1,\quad
P_{ij,k}=0\quad(k\in\{i,j\}).
\]
For four types, write \(p(P)\) for the unique simplex fixed point, whose existence and uniqueness are proved in the [main note](FOUR_TYPE_UNIQUENESS.md). For coefficient arrays use the full row norm
\[
\eta(P,Q)=\max_{i,j}\sum_k|P_{ij,k}-Q_{ij,k}|.
\]
The geometric theorem below does not assume higher-dimensional uniqueness.

## 2. Claim 1: exact attainable geometry and an improved universal upper

### 2.1. Attainable fixed-point vectors

**Claim 1(a).** For every integer \(n\ge3\), a vector
\(x\in\Delta_{n-1}\) is a fixed point of at least one symmetric
parent-excluding QSO if and only if

\[
\boxed{
x_i\le(1-x_i)^2\quad\text{for all }i,
\qquad
x_i+x_j+2x_i x_j\le1\quad\text{for all }i\ne j.
}
\tag{4}
\]

This statement concerns existence of an operator with the prescribed fixed
point. It makes no higher-dimensional uniqueness or sensitivity assertion.

**Proof.** Fix \(x\). For an unordered parent pair \(i\le j\), let

\[
w_{ij}=\begin{cases}x_i^2&i=j,\\2x_i x_j&i<j,\end{cases}
\qquad A_{ij}=[n]\setminus\{i,j\}.
\]

The set of all attainable offspring vectors from this particular state is
the compact convex Minkowski sum

\[
\mathcal C_x=\sum_{i\le j}w_{ij}\Delta_{A_{ij}},
\qquad
\Delta_A=\operatorname{conv}\{e_k:k\in A\}.
\tag{5}
\]

The sets \(A_{ij}\) are nonempty because \(n\ge3\). Each distribution in a
summand supplies that parent row of \(P\), and the same row is used after
reversing distinct parents. Rows of weight zero may be completed arbitrarily
subject to (2).

The necessary and sufficient subset conditions for \(x\in\mathcal C_x\) are

\[
x(G)\le\sum_{i\le j:\,A_{ij}\cap G\ne\varnothing}w_{ij}
\quad\text{for every }G\subseteq[n].
\tag{6}
\]

Here is a short sufficiency proof, so no unexamined transportation-feasibility
assertion is needed. For any real vector \(z\), list its distinct values
\(t_1<\cdots<t_m\) and put \(G_\ell=\{k:z_k\ge t_\ell\}\). Then

\[
z=t_1\mathbf1+\sum_{\ell=2}^m(t_\ell-t_{\ell-1})\mathbf1_{G_\ell},
\]

and for every nonempty allowed set \(A\),

\[
\max_{k\in A}z_k
=t_1+\sum_{\ell=2}^m(t_\ell-t_{\ell-1})
  \mathbf1_{A\cap G_\ell\ne\varnothing}.
\]

Because \(\sum_{i\le j}w_{ij}=\sum_i x_i=1\), applying (6) to the nested
sets gives

\[
z\cdot x\le\sum_{i\le j}w_{ij}\max_{k\in A_{ij}}z_k
=\max_{y\in\mathcal C_x}z\cdot y.
\]

Finite-dimensional separation of a point from a compact convex set now
gives \(x\in\mathcal C_x\). Necessity of (6) follows directly by summing
offspring mass in \(G\).

For a singleton \(G=\{k\}\), the right side of (6) is \((1-x_k)^2\).
For \(G=\{k,\ell\}\), the only parent row with no allowed output in \(G\)
is the distinct pair \(k\ell\), of weight \(2x_kx_\ell\). For
\(|G|\ge3\), every parent pair has an allowed output in \(G\), so the right
side is one and the condition is automatic. Empty \(G\) is also automatic.
Thus (6) reduces exactly to (4). \(\square\)

The coordinator independently suggested the weighted-Hall formulation
during this task. I independently verified it and supplied the sorted-linear-
functional proof above. The argument applies to every \(n\ge3\); only the
optimization and sensitivity conclusions below are four-type statements.

### 2.2. Exact minimum of the forced-pair product

Put

\[
b=\frac{1-c}{1+2c},\qquad d=2cb,\qquad B=c+b=1-d,
\qquad m_0=bd=\frac{27-7\sqrt5}{121}.
\tag{7}
\]

Here \(c>b>d>0\), and numerically

\[
(c,b,d)\approx(0.381966011,0.350372906,0.267661084),
\qquad m_0\approx0.09378119138.
\]

**Claim 1(b).** Over all attainable four-type fixed-point vectors and all
partitions \(\{i,k\}\sqcup\{j,\ell}=[4]\),

\[
\boxed{p_i p_k+p_jp_\ell\ge m_0,}
\tag{8}
\]

and equality is attained by an admissible deterministic operator.

**Proof of the lower bound.** For any two coordinates \(x,y\le c\),
\((c-x)(c-y)\ge0\) gives \(xy\ge c(x+y)-c^2\). Combined with the pair
inequality in (4), this gives

\[
x+y\le\frac{1+2c^2}{1+2c}=B.
\tag{9}
\]

Thus it suffices to minimize the product expression under the weaker
constraints \(p_i\le c\), \(p_i+p_j\le B\), and simplex normalization.

Sort the four coordinates as \(A\ge C\ge D\ge F\ge0\). Of the three
pairings, \(AF+CD\) is the smallest, by the elementary rearrangement
identities. Write \(s=1-A-C=D+F\). Then

\[
AF+CD=Cs+(A-C)F
\ge Cs+(A-C)\max\{0,1-A-2C\}.
\tag{10}
\]

We use \(1/4\le A\le c\), \(C\le A\), and \(A+C\le B\).

If \(A+2C\ge1\), then \(A\ge1/3\), and the right side of (10) is
\(C(1-A-C)\). It is concave in \(C\) on

\[
\frac{1-A}{2}\le C\le\min\{A,B-A\}.
\]

At its lower endpoint the value is \((1-A)^2/4\ge c/4\ge bd\), using
\((1-c)^2=c\) and \(b+d=1-c\). At the upper endpoint:

* If \(A\le B/2\), the value is \(A(1-2A)\). This function decreases
  for \(A\ge1/3\), so it is at least \(B(1-B)/2\ge(B-c)(1-B)=bd\).
* If \(A\ge B/2\), the value is \((B-A)(1-B)\ge(B-c)(1-B)=bd\).

If \(A+2C\le1\), the right side of (10) is
\(A(1-A-2C)+C^2\), which decreases as \(C\) increases while \(C\le A\).
For \(A\le1/3\), use \(C\le A\) to bound it below by
\(A-2A^2\ge1/9>bd\), since \(1/4\le A\le1/3\).
For \(A\ge1/3\), use \(C\le(1-A)/2\) to bound it below by
\((1-A)^2/4\ge c/4\ge bd\). This exhausts all cases and proves (8).
The comparisons used above include \(2/3<B<2c\), so the interval endpoints
and signs of \(1-B\) are as stated. \(\square\)

**Attainment.** Specify the offspring of each unordered pair by

| Parents | Offspring |
| --- | --- |
| \(11\) | \(2\) |
| \(22\) | \(1\) |
| \(33\) | \(1\) |
| \(12\) | \(3\) |
| \(13\) | \(2\) |
| \(23\) | \(1\) |
| \(14\) | \(3\) |
| \(24\) | \(1\) |
| \(34\) | \(1\) |
| \(44\) | \(1\) |

Every listed offspring excludes its parents. This operator has fixed point

\[
p=(c,b,d,0).
\]

Indeed \(p_1=(b+d)^2=c\), \(p_3=2cb=d\), and
\(p_2=c^2+2cd=b\). The last identity follows from
\(b(1-4c^2)=c^2\). The fourth output is identically zero. For the partition
\(\{1,4\}\sqcup\{2,3}\), the product sum is exactly \(bd=m_0\).
Thus (8) is sharp even on the actual fixed-point locus, not only on a relaxed
capped simplex.

### 2.3. Consequence for coefficient sensitivity

I do not repeat the upper-bound proof of worker 013. Its intermediate
forced-parent-pair inequality says, in the two-positive/two-negative case,

\[
(1-2c)\|p(P)-p(Q)\|_1
\le\eta(P,Q)\,[1-2(q_iq_k+q_jq_\ell)],\qquad q=p(Q),
\tag{11}
\]

where the partition is the sign partition of \(p(P)-p(Q)\). If one sign
occurs only once, the existing bound has constant one. These statements
include zero coefficients and zero state coordinates.

Inserting (8) into (11) gives

\[
\boxed{
\|p(P)-p(Q)\|_1
\le\min\left\{2,\frac{204+95\sqrt5}{121}\eta(P,Q)\right\},
}
\tag{12}
\]

because

\[
\frac{1-2m_0}{1-2c}
=\frac{204+95\sqrt5}{121}<2\sqrt5-1.
\]

The new product minimum is sharp; this does **not** make the coefficient
constant in (12) sharp, because other inequalities in (11) need not have
simultaneous equality.

### Why the old capped-simplex extremizers fail

Worker 013 used

\[
p_i p_k+p_jp_\ell-c(1-2c)
=(c-p_i)(c-p_k)+(c-p_j)(c-p_\ell)\ge0.
\]

Equality requires one coordinate equal to \(c\) in each of two disjoint
pairs, hence two distinct coordinates equal to \(c\). But their pair
inequality would require

\[
2c+2c^2=10-4\sqrt5\le1,
\]

which is false. Equivalently, equality in the individual cap forces every
positive-weight parent row avoiding that output to produce it with
probability one; two capped outputs conflict on the diagonal row of a third
positive type. Therefore these capped-simplex extremizers cannot be fixed
points of any admissible coefficient array. Condition (4) gives the exact
additional feasibility constraints, rather than only this obstruction.


## Review and reproducibility

The all-dimensional geometry proof uses only finite-dimensional separation and an explicit support-function calculation. The sharper four-type coefficient estimate also uses the transfer inequality proved in the main note, in the exact form reproduced above. The parent checked the sorted-coordinate minimization, its attainable equality example, and the resulting constant. [The exact certificate](computations/049_exact_certificates.py) verifies the radical identities and admissible examples. It does not replace the universal geometric proof.

The complete049 report additionally proves a sharp derivative constant for the uniform three-type boundary family and gives a rational finite coefficient-sensitivity witness. Those statements are retained in the original report; the global optimal coefficient constant remains open. No formal proof-assistant verification or worldwide-priority clearance is claimed.
