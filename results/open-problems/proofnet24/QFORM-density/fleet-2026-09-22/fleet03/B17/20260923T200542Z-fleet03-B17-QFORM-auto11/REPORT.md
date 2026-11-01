SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B17, 2026-09-23T20:05:42Z.
attacking: growing fragmented-support witnesses in the dense six-variable Householder geometry; aggregate exact kernel cancellations and bound all nonkernel cells without fragment-count loss.

# QFORM B17: countable-fragment cone-tip exclusion with exact kernel cancellations

## Status and scope

This report proves a new supporting theorem for an exact six-variable rotated target matrix. It removes the fragment-count loss from the preceding remote-cell argument and permits arbitrary finite or countable interval fragmentation, including exact pairwise remote cancellations. It does **not** prove the full QFORM conjecture and does not address the full-target continuity conclusion.


The designated completed partner result actually applied below is `fleet04/B17`,
`yspennstate/math-open-problems@4e8d5ae06f2657e9e1ac8a89f7bc26c9ff95169e`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B17/20260923T171805Z-fleet04-B17-QFORM-r5/REPORT.md`.
It supplies the exact main-cell scaling for the same dense matrix and fragmented cap-one laws.

## 1. Exact dense target and pair-sum factorization

Let

\[
T={1\over\sqrt2}\begin{pmatrix}
1&1&0&0&0&0\\
0&0&1&1&0&0\\
0&0&0&0&1&1
\end{pmatrix},
\qquad
B=I_3-{2\over3}{\bf1}{\bf1}^T,
\]
so `TT^T=I_3` and `B^2=I_3`. Put

\[
A=T^TBT={1\over6}\begin{pmatrix}
1&1&-2&-2&-2&-2\\
1&1&-2&-2&-2&-2\\
-2&-2&1&1&-2&-2\\
-2&-2&1&1&-2&-2\\
-2&-2&-2&-2&1&1\\
-2&-2&-2&-2&1&1
\end{pmatrix}.
\]
Then

\[
\boxed{\operatorname{spec}(A)=\{1,1,-1,0,0,0\}},\qquad \|A\|_{op}=1,
\]
and, crucially,

\[
|Aa|=|T^TBTa|=|BTa|=|Ta| \tag{1.1}
\]
for every `a` in the row-space component relevant to `A`; equivalently `|Aa|^2=a^TA^2a=|Ta|^2` because `A^2=T^TT`.

Let `p_*` denote the exact centered-unit-cube cone-tip density for this matrix,

\[
p_*=4.06307061680603726012548\ldots . \tag{1.2}
\]
The exact source is the fleet01/B17 dense triangular-bank calculation at `e83d0cc194d791acf31d6c86245204887cfd8171`.

## 2. Fragmented cap-one laws and the cell-center gap

For each physical coordinate `i=1,...,6`, let

\[
E_i=\bigsqcup_{k\in K_i}
[c_{i,k}-\ell_{i,k}/2,c_{i,k}+\ell_{i,k}/2],
\qquad
\ell_{i,k}>0,
\qquad
\sum_{k\in K_i}\ell_{i,k}=1,
\]
where `K_i` is finite or countable and the intervals are pairwise disjoint. Let `X_i` be independent with density `1_{E_i}`. Thus every marginal is an exact probability density satisfying `0<=f_i<=1`, with no connected-support or bounded-diameter assumption.

A product cell is indexed by `k=(k_1,...,k_6)` and has center

\[
c(k)=(c_{1,k_1},\ldots,c_{6,k_6}).
\]
Call the cell **kernel** if `T c(k)=0`; otherwise call it nonkernel. Define the nonkernel center gap

\[
\Delta:=\inf\{|Tc(k)|:Tc(k)\ne0\}\in(0,\infty]
\]
and

\[
M:=\Delta-\frac{\sqrt6}{2}. \tag{2.1}
\]
The theorem below applies whenever `M>0`. It is intentionally independent of the number of fragments.

## 3. Main theorem

### Theorem `QFORM-DENSE-FRAGMENT-KERNEL-AGGREGATE-v1`

For the matrix `A` above and every finite or countable interval fragmentation as in Section 2, if `M>0`, the cone-tip density obeys

\[
\boxed{
p_Q(0)\le p_*+{6\sqrt6\over M}.\ }
\tag{3.1}
\]
If `\Delta\ge\sqrt6`, then `M\ge\Delta/2`, hence

\[
\boxed{
p_Q(0)\le p_*+{12\sqrt6\over\Delta}.\ }
\tag{3.2}
\]
Consequently for any sequence of such fragmented laws with `\Delta\to\infty`, even if the number of fragments tends to infinity and even if arbitrarily many product cells have exact kernel cancellations,

\[
\boxed{\limsup p_Q(0)\le p_*<3\sqrt2.} \tag{3.3}
\]

Thus growing fragment count by itself cannot beat the centered dense cone-tip value. A stronger cone-tip witness in this architecture must force nonkernel cell centers to approach the pair-sum kernel at the critical physical scale `\Delta=O(1)` (equivalently `R\delta_R=O(1)` when centers are written as `R` times labels), or leave this architecture/off-tip level entirely.

## 4. Exact kernel aggregate: no fragment-count loss

The key point is that exact kernel cancellation factorizes bank by bank.

Consider one physical pair with interval lengths `a,b` and centers `u,v`. Its pair sum is `(X+Y)/sqrt(2)`. A product rectangle belongs to the exact kernel sector precisely when `u+v=0` in this bank. For a matched pair, write the centered overlap kernel

\[
\kappa_{a,b}(z)=
\left|[-a/2,a/2]\cap[z-b/2,z+b/2]\right|.
\]
For every `z`, elementary interval geometry gives

\[
\kappa_{a,b}(z)
\le \left({a+b\over2}-|z|\right)_+. \tag{4.1}
\]
Because intervals within each marginal are disjoint, a fixed interval center can match at most one interval center from the opposite marginal. Let `\mathcal M(z)` be the set of matched pairs active at `z`. Since the total interval lengths in each marginal are one,

\[
\begin{aligned}
\sum_{(a,b)\in\mathcal M(z)}\kappa_{a,b}(z)
&\le {1\over2}\sum_{\mathcal M(z)}(a+b)
      -|\mathcal M(z)|\,|z|\\
&\le (1-|z|)_+ .
\end{aligned}\tag{4.2}
\]
(The right side is automatically zero for `|z|>=1`, since every interval length is at most one.)

After the `sqrt(2)` pair-sum scaling, the aggregate exact-kernel subdensity in that bank therefore satisfies

\[
\boxed{
h_0(y)\le h_*(y):=\sqrt2(1-\sqrt2|y|)_+.}\tag{4.3}
\]
Here `h_*` is exactly the pair-sum density of two independent centered unit intervals.

Now `Tc(k)=0` is equivalent to exact cancellation in **all three disjoint physical pairs**. Hence the sum over all exact-kernel product cells factorizes as the product of three bank subdensities `h_{j,0}`. The exact cone coarea functional is positive, so (4.3) gives

\[
\begin{aligned}
p_{\rm ker}(0)
&=\int_{\mathbb R^3}\delta(y^TBy)
   \prod_{j=1}^3h_{j,0}(y_j)\,dy\\
&\le\int_{\mathbb R^3}\delta(y^TBy)
   \prod_{j=1}^3h_*(y_j)\,dy
=p_* .
\end{aligned}\tag{4.4}
\]
This pays **zero** factor for the number of exact-cancellation cells.

## 5. All nonkernel cells at once: six coordinate charts, not a cell sum

Let `x` belong to any nonkernel product cell with center `c`. Write `x=c+u`. Since each interval length is at most one,

\[
|u|\le\frac{\sqrt6}{2}.
\]
Using (1.1) and `||A||_{op}=1`,

\[
|Ax|\ge |Ac|-|Au|
\ge |Tc|-|u|
\ge \Delta-\frac{\sqrt6}{2}=M. \tag{5.1}
\]
Partition the entire nonkernel region measurably into six sets `N_j` according to which coordinate has maximal `|(Ax)_j|` (break ties by the smallest index). On `N_j`,

\[
|(Ax)_j|\ge {|Ax|\over\sqrt6}\ge {M\over\sqrt6},
\qquad
|\partial_{x_j}(x^TAx)|=2|(Ax)_j|
\ge {2M\over\sqrt6}. \tag{5.2}
\]
Fix the other five coordinates. As a function of `x_j`, `x^TAx` is a polynomial of degree at most two. It has at most two roots inside `N_j`; an identically-zero fiber is impossible there because of (5.2). The one-dimensional delta/root formula and the cap `f_j<=1` therefore give

\[
\int 1_{N_j}(x)f_j(x_j)\delta(x^TAx)\,dx_j
\le {\sqrt6\over M}. \tag{5.3}
\]
Integrating against the other five probability densities costs exactly one, not the number of their fragments. Therefore

\[
p_{\rm nonker}(0)
\le\sum_{j=1}^6{\sqrt6\over M}
={6\sqrt6\over M}. \tag{5.4}
\]
Combining (4.4) and (5.4) proves (3.1). This is the step that removes the preceding `63`-cell factor and remains valid for countably many fragments.

## 6. Actual application of the designated fleet04/B17 result

Take the partner family with `eta=10^{-3}`:

\[
f_R(x)=1_{[-(1-\eta)/2,(1-\eta)/2]}(x)
       +1_{[R,R+\eta]}(x)
\]
for all six independent coordinates. The only exact-kernel product cell is the all-central cell because every remote center is positive. The partner theorem gives its exact cone-tip contribution

\[
p_{\rm ker}(0)=(1-\eta)^4p_* . \tag{6.1}
\]
Every noncentral cell has at least one physical pair containing a remote coordinate, so its pair-sum center has magnitude at least `(R+eta/2)/sqrt(2)`. Thus

\[
\Delta\ge{R+\eta/2\over\sqrt2}>{R\over\sqrt2}.
\]
Equations (5.4) and (6.1) give the concrete partner inequality

\[
\boxed{
(1-\eta)^4p_*
\le p_{Q_R}(0)
\le (1-\eta)^4p_*
+{6\sqrt6\over R/\sqrt2-\sqrt6/2}.}
\tag{6.2}
\]
The left inequality is the partner's completed fragmented-main-cell result; the right inequality is new. In particular the former `252sqrt(6)/R` remote-cell error is replaced by a six-chart bound with no fragment-count factor.

There is a simple fully rational finite certificate already at `R>=120`. Use

\[
p_*<{508\over125},\qquad
{1\over\sqrt2}>{7\over10},\qquad
\sqrt6<{49\over20}.
\]
Then for `R>=120`,

\[
M>{3311\over40},
\qquad
{6\sqrt6\over M}<{588\over3311}.
\]
Hence

\[
p_{Q_R}(0)
<{508\over125}+{588\over3311}.
\]
Exactly,

\[
{140\over33}-\left({508\over125}+{588\over3311}\right)
={148\over177375}>0, \tag{6.3}
\]
and `140/99<sqrt(2)`, so

\[
\boxed{p_{Q_R}(0)<{140\over33}<3\sqrt2\qquad(R\ge120).}\tag{6.4}
\]
This improves the preceding explicit remote-fragment certificate `R>=3600` to `R>=120`, while simultaneously allowing arbitrarily many additional fragments subject to the center-gap condition.

## 7. What remains

The source-valid universal lower obstruction is still `C_*>=3sqrt(2)` from the diffuse rotated family; this theorem does not improve it. Instead it narrows the witness frontier.

The unresolved cone-tip fragmentation mechanism is now **near-kernel resonance**: nonkernel product-cell centers with `|Tc|=O(1)` despite their physical centers becoming large, or a continuum/countable accumulation at that scale. Off-zero global peaks also remain outside this theorem. More generally, the unrestricted QFORM theorem and arbitrary additional spectrum remain open.

Continuity is not claimed here. The result is a quantitative cone-tip bound for the stated exact product-fragment class.

Status: `SUPPORTING_QUANTITATIVE_WITNESS_EXCLUSION`; full QFORM `OPEN / NOT PROVED`; native brain status `WITHOUT_VERIFIED_BRAIN`.
