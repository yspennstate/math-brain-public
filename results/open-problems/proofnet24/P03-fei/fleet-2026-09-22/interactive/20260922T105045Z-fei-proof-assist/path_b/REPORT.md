# A logarithmic-scale variational certificate for recursive Boolean spectra

**Full FEI status:** OPEN / NOT PROVED.  
**Scope of the result:** iterates of a fixed balanced regular Boolean gate, including recursive ternary majority.  
**Classification:** proved intermediate information theorem, subject to independent review; no publication-priority claim.

## 1. What is proved

The recent oriented-cancellation report recovers one half of the leading dependence KL on the sparse one-point suspension. It correctly warns that independently summing binary event certificates can reuse the same credit. The recent restriction report preserves full KL through an exact signed multiscale ledger. The separate recursive-majority obstruction proves that individually labelled low Fourier levels plus a merged tail do not recover enough dependence information. These are the starting points, not claims resolved here. [Oriented-cancellation report](https://github.com/yspennstate/math-open-problems/blob/a83d4009cc98aeb739af4f40b1c2cfa8be7269d0/proofnet24/P03-fei/fleet-2026-09-22/fleet02/B08/B08-20260922T103745Z-0f440e/REPORT.md), [restriction ledger](https://github.com/yspennstate/math-open-problems/blob/b293d016f9bd94819fb11385986608b8acc0b83d/proofnet24/P03-fei/fleet-2026-09-22/fleet01/B15/b15-20260922T103236Z-restriction-iprojection-chain/REPORT.md), [coefficient-symbol correction](https://github.com/yspennstate/math-open-problems/blob/3a5fccff414043be05a0c7f2f219dabd9b44708b/proofnet24/P03-fei/fleet-2026-09-22/fleet01/B15/b15-20260922T103236Z-restriction-iprojection-chain/CORRECTION.md), [low-level projection barrier](https://github.com/yspennstate/math-open-problems/blob/bff0d7b6c21485f386841c42582eb04f32705046/proofnet24/P03-fei/fleet-2026-09-21/fleet03/B18/20260922T100641Z-lowlevel-projection-barrier/REPORT.md).

This report constructs **one normalized hybrid reference law** on the entire spectral set. Its likelihood ratio is a single entropy-variational test. For recursive ternary majority, keeping only the bottom logarithmically many physical hierarchy scales already supplies enough KL to pay the balanced Bellman deficit at center 6. A two-sided version keeps logarithmically many bottom scales and finitely many top scales and recovers the full dependence KL to any prescribed additive \(\varepsilon I\) accuracy.

The two-sided result extends to every fixed balanced regular gate with mean spectral cardinality strictly between 1 and its arity. The number of retained physical hierarchy scales is \(O(1+\log m+\log(1/\varepsilon))\) at iteration depth \(m\). This is a count of hierarchy levels, not a bound on computation or on the number of physical coordinates inspected.

This does not prove FEI for arbitrary Boolean functions. The construction uses an actual known disjoint composition tree and equal leaf occurrence marginals. It provides an explicit successful response to the recursive-majority information-extraction barrier, with coefficient one on the retained KL up to additive influence scale.

## 2. A genuine Boolean source and its occurrence I-projection

Let
\[
g:\{-1,1\}^b\longrightarrow\{-1,1\}
\]
be balanced. Write its nonempty squared Walsh law as
\[
\pi(T)=\widehat g(T)^2,\qquad
T\in 2^{[b]}\setminus\{\varnothing\}.
\]
Assume every coordinate has the same influence
\[
\alpha=\frac{\mu}{b},\qquad
\mu=\sum_T |T|\pi(T),\qquad 1<\mu<b.
\]
Put \(h=H(\pi)=H(g)\). The assumptions exclude parity and dictator degeneracies; they are not automatic for general gates.

Let \(f_m\) be the depth-\(m\) iterated composition of \(g\) on pairwise disjoint fresh variable blocks. There are
\[
N=b^m,\qquad I=I(f_m)=\mu^m
\]
leaves and total influence, and every leaf occurrence marginal is
\[
r=\alpha^m.
\]

The source spectral law \(P_m\) has the following exact tree representation. An active internal node chooses its nonempty set of active children with law \(\pi\), independently at different active nodes. Iterate until the leaves. The set of active leaves is the spectral random set. This follows directly by expanding the balanced disjoint composition: the coefficient on a leaf set is the outer coefficient on its active blocks times the child coefficients on the nonempty sets inside those blocks.

A height-\(j\) node means a node with \(j\) generations of leaves below it. The expected number of active height-\(j\) nodes is
\[
\mu^{m-j}.
\]
Entropy and mean cardinality therefore satisfy
\[
H(P_m)=h\sum_{j=1}^m\mu^{m-j}
=\frac{h}{\mu-1}(I-1).
\tag{2.1}
\]

Let \(Q_m\) be the maximum-entropy law on nonempty leaf subsets with occurrence marginals \(r\). It is the product Bernoulli law with leaf parameter
\[
t=cr
\]
conditioned on at least one active leaf, where \(c\in(0,1]\) is the unique positive solution of
\[
1-c=(1-cr)^N.
\tag{2.2}
\]
The exact occurrence credit is
\[
K_m=D_2(P_m\Vert Q_m)=H_{\max}(r,\ldots,r)-H(P_m).
\tag{2.3}
\]
This normalization and I-projection identity are the existing source input. [Exact occurrence I-projection](https://github.com/yspennstate/math-open-problems/blob/4bd6d05f1eb8325d665f2748f4d74dcee2550a04/proofnet24/P03-fei/fleet-2026-09-21/fleet02/B15/20260922T0829Z-influence-iprojection-kl/REPORT.md).

## 3. Exact local reference law at every physical scale

Define
\[
u_j=1-(1-t)^{b^j},\qquad 0\le j\le m,
\]
so \(u_0=t\) and \(u_m=c\).

Under \(Q_m\), conditional on a height-\(j\) node being active, its child-activation pattern has law
\[
R_j(T)
=\frac{u_{j-1}^{|T|}(1-u_{j-1})^{b-|T|}}{u_j},
\qquad T\ne\varnothing.
\tag{3.1}
\]
After this pattern is chosen, different active child blocks have independent conditional product laws on their leaves. Thus (3.1) generates \(Q_m\) recursively.

Set
\[
d_j=D_2(\pi\Vert R_j)\ge0.
\]
Because the cross entropy in (3.1) depends on \(T\) only through \(|T|\),
\[
\boxed{
d_j
=\log_2u_j-\mu\log_2u_{j-1}
-(b-\mu)\log_2(1-u_{j-1})-h.
}
\tag{3.2}
\]
No symmetry of \(\pi\) beyond equal occurrence marginals was used here.

The exact hierarchy gives
\[
\boxed{
K_m=\sum_{j=1}^m\mu^{m-j}d_j.
}
\tag{3.3}
\]
The general exact hierarchy identity is already available project-locally. What follows adds a specific normalized variational certificate and a quantitative truncation theorem, rather than treating (3.3) alone as progress. [Existing hierarchy identity](https://github.com/yspennstate/math-open-problems/blob/2bf247373576eb406ca91bb3ea5f3ce5e5ab8588/proofnet24/P03-fei/fleet-2026-09-21/fleet04/B15/20260922T091017Z-iprojection-composition-transfer/REPORT.md).

## 4. One hybrid law prevents repeated spending

Let \(\mathcal J\subseteq\{1,\ldots,m\}\) be any selected set of heights. Define \(\widetilde Q_{\mathcal J}\) by the same recursive physical tree as \(Q_m\), with the following rule at each active height-\(j\) node:

- if \(j\in\mathcal J\), choose its nonempty child pattern with the true generator law \(\pi\);
- otherwise choose it with the reference law \(R_j\).

These are normalized conditional distributions on every node. Consequently \(\widetilde Q_{\mathcal J}\) is one normalized probability law on nonempty leaf subsets.

For a source-realizable leaf set \(S\), its active-node tree and every child pattern are determined by \(S\). The likelihood ratio is therefore
\[
\log_2\frac{\widetilde Q_{\mathcal J}(S)}{Q_m(S)}
=
\sum_{\substack{v\ {\rm active}\\{\rm height}(v)\in\mathcal J}}
\log_2\frac{\pi(T_v)}{R_{{\rm height}(v)}(T_v)}.
\tag{4.1}
\]
Taking source expectation,
\[
\boxed{
\mathcal L_{\mathcal J}
:=
\mathbb E_{P_m}\log_2
\frac{\widetilde Q_{\mathcal J}}{Q_m}
=
\sum_{j\in\mathcal J}\mu^{m-j}d_j
\le K_m.
}
\tag{4.2}
\]

This lower bound follows from one normalized likelihood ratio:
\[
D_2(P_m\Vert Q_m)
-
\mathbb E_{P_m}\log_2
\frac{\widetilde Q_{\mathcal J}}{Q_m}
=
D_2(P_m\Vert\widetilde Q_{\mathcal J})\ge0.
\tag{4.3}
\]
Thus separate binary KL bounds are not being added.

If \(\pi\) vanishes on some patterns, (4.1) may be minus infinity outside the source support. There is no ambiguity under \(P_m\): every source-positive pattern has positive \(\pi\), so the displayed source expectation is finite. For a finite bounded variational-test formulation, replace \(\widetilde Q\) by \((1-\delta)\widetilde Q+\delta Q_m\), apply the finite entropy variational inequality, and let \(\delta\downarrow0\).

The exact lost credit is
\[
\boxed{
K_m-\mathcal L_{\mathcal J}
=
\sum_{j\notin\mathcal J}\mu^{m-j}d_j.
}
\tag{4.4}
\]
All coordinate and block labels are retained through the fixed physical tree and the genuine reference law. No entropy cost of choosing new labels or a data-dependent coordinate transformation is omitted.

## 5. Finite-depth omitted-scale bound

Put
\[
\ell=-\log_2(1-t),\qquad
A=\max\{0,\log_2b-h\}.
\]
For integers \(0\le L<M\le m\), omit exactly the middle heights
\[
j=L+1,\ldots,M.
\]

### Theorem 5.1

The discarded dependence credit obeys
\[
\boxed{
\begin{aligned}
\sum_{j=L+1}^{M}\mu^{m-j}d_j
\le{}&
\left(I\mu^{-L}-\mu^{m-M}\right)
\left[\log_2(1/t)+\frac{A}{\mu-1}\right]\\
&+I\ell\left[
\left(\frac b\mu\right)^M-
\left(\frac b\mu\right)^L
\right].
\end{aligned}
}
\tag{5.1}
\]

### Proof

For \(u=u_{j-1}\),
\[
u_j=1-(1-u)^b\le bu.
\]
Also \(u\ge t\), while
\[
-\log_2(1-u)=b^{j-1}\ell.
\]
Insert these three facts into (3.2):
\[
\begin{aligned}
d_j
&\le
(\mu-1)\log_2(1/u)
+(b-\mu)b^{j-1}\ell+\log_2b-h\\
&\le
(\mu-1)\log_2(1/t)
+(b-\mu)b^{j-1}\ell+A.
\end{aligned}
\tag{5.2}
\]
All terms in (5.2) are then summed with weight \(\mu^{m-j}\).

The first and third terms sum to
\[
\left(I\mu^{-L}-\mu^{m-M}\right)
\left[\log_2(1/t)+\frac{A}{\mu-1}\right].
\]
The middle term telescopes geometrically:
\[
\sum_{j=L+1}^{M}
\mu^{m-j}(b-\mu)b^{j-1}\ell
=
I\ell\left[
(b/\mu)^M-(b/\mu)^L
\right].
\]
This proves (5.1). \(\square\)

This estimate is uniform in the iteration depth. Its constants retain the actual generator's \(\mu,b,h\).

## 6. Coefficient-one recovery to arbitrary additive influence accuracy

Fix \(0<\varepsilon\le1\). At depths satisfying
\[
I=\mu^m\ge2,\qquad \alpha^m\le\frac12,
\tag{6.1}
\]
define
\[
a_m=m\log_2(1/\alpha)+1+\frac{A}{\mu-1},
\]
\[
L=
\left\lceil\log_\mu\frac{2a_m}{\varepsilon}\right\rceil,
\qquad
K=
\left\lceil
\log_{1/\alpha}\frac{4}{\varepsilon\ln2}
\right\rceil.
\tag{6.2}
\]
Retain the bottom \(L\) and top \(K\) heights:
\[
\mathcal J=
\{j:1\le j\le L\}
\cup
\{j:m-K<j\le m\}.
\tag{6.3}
\]
Intersect these sets with \(\{1,\ldots,m\}\). If they overlap, every height is retained. At the finitely many depths failing (6.1), retain every height.

### Theorem 6.1

For the single hybrid reference law defined above,
\[
\boxed{
0\le K_m-\mathcal L_{\mathcal J}\le\varepsilon I.
}
\tag{6.4}
\]
The number of retained heights is
\[
O_g\bigl(1+\log m+\log(1/\varepsilon)\bigr).
\]

### Proof

If there is no omitted middle interval, the loss is zero. Otherwise apply (5.1) with \(M=m-K\).

The positive root in (2.2) satisfies \(c\ge1/2\) under \(I\ge2\). Indeed at \(c=1/2\),
\[
(1-r/2)^N\le e^{-Nr/2}=e^{-I/2}\le e^{-1}<1/2,
\]
so the unique positive fixed point lies above \(1/2\). Consequently
\[
\log_2(1/t)\le m\log_2(1/\alpha)+1.
\]
The first line of (5.1) is at most
\[
I\mu^{-L}a_m\le\frac{\varepsilon I}{2}.
\tag{6.5}
\]
For the second line, use
\[
\ell\le\frac{t}{(1-t)\ln2},
\qquad
t=c\alpha^m\le\alpha^m\le\frac12.
\]
It is at most
\[
I\ell\alpha^{-(m-K)}
\le \frac{2I\alpha^K}{\ln2}
\le\frac{\varepsilon I}{2}.
\tag{6.6}
\]
This proves (6.4). The bounds in (6.2) give the scale count. \(\square\)

Since \(I\ge2\) implies \(I\le2(I-1)\), equations (2.1), (2.3) and (6.4) also yield
\[
\boxed{
\mathcal L_{\mathcal J}
\ge
H_{\max}(r,\ldots,r)
-
\left(\frac{h}{\mu-1}+2\varepsilon\right)(I-1).
}
\tag{6.7}
\]
At shallower depths full credit is retained, so (6.7) still holds. This proves that the explicit retained-information certificate pays a finite balanced Bellman deficit for the entire stated family. It is not obtained by assuming a universal lower bound on \(K_{\rm occ}\).

## 7. Ternary majority: bottom logarithmic scales alone pay center 6

For ternary majority,
\[
b=3,\quad \mu=\frac32,\quad h=2,\quad \alpha=\frac12,\quad A=0.
\]
At an active node, each singleton pattern and the all-three pattern has probability \(1/4\). The local credit is exactly
\[
d_j
=\log_2u_j-\frac32\log_2u_{j-1}
-\frac32\log_2(1-u_{j-1})-2.
\tag{7.1}
\]

Let
\[
L_m=\min\left\{
m,\left\lceil\log_{3/2}\bigl(4(m+1)\bigr)\right\rceil
\right\},
\]
and retain just the bottom heights \(1,\ldots,L_m\).

### Corollary 7.1

For every depth \(m\ge1\),
\[
\boxed{
K_m-\mathcal L_{\{1,\ldots,L_m\}}
\le2(I-1),
}
\tag{7.2}
\]
and therefore
\[
\boxed{
\mathcal L_{\{1,\ldots,L_m\}}
\ge H_{\max}-6(I-1).
}
\tag{7.3}
\]

### Proof

For \(m\le5\), \(4(m+1)\ge(3/2)^m\), so \(L_m=m\) and there is no loss. The same conclusion holds at any larger depth for which \(L_m=m\).

Otherwise \(m\ge6\), and (5.1) with \(M=m\) gives
\[
\begin{aligned}
K_m-\mathcal L
&\le
(I(3/2)^{-L_m}-1)\log_2(1/t)
+I\ell(2^m-2^{L_m})\\
&\le
I(3/2)^{-L_m}(m+1)
+\frac{I}{(1-2^{-m})\ln2}\\
&\le
\left(\frac14+\frac{64}{63\ln2}\right)I
<
\frac{149}{84}I.
\end{aligned}
\tag{7.4}
\]
Here \(c\ge1/2\) already follows from \(I\ge3/2>2\ln2\), and the last strict inequality uses \(\ln2>2/3\).

For \(m\ge6\), \(I\ge729/64>168/19\), so
\[
\frac{149}{84}I\le2(I-1).
\]
This proves (7.2). Recursive majority has \(H=4(I-1)\) by (2.1), and (2.3) then gives (7.3). \(\square\)

The constant 6 here is a bound certified for recursive majority by this particular incomplete-information mechanism. It is not a new universal FEI constant, and the exact family entropy ratio is already 4. The advance is that a concretely normalized, logarithmic-scale extraction pays the full relevant deficit, whereas the refuted low-level extraction paid an asymptotically vanishing fraction.

### Corollary 7.2 — logarithmic fine-scale retention is necessary in this architecture

Suppose a middle interval beginning at height \(L+1\) is omitted, so that this height is not retained by the top-scale suffix. If
\[
m\ge16,\qquad L\le\frac{m}{2\log_2 3},
\]
then
\[
\boxed{
K_m-\mathcal L_{\mathcal J}
\ge\frac{mI}{8(3/2)^{L+1}}.
}
\tag{7.5}
\]
Consequently a bound \(K_m-\mathcal L_{\mathcal J}\le B I\), for one fixed \(B>0\), requires
\[
L\ge \log_{3/2}\!\frac{m}{8B}-1.
\tag{7.6}
\]

To prove this, write \(u=u_L\). Equation (7.1) becomes
\[
d_{L+1}
=\log_2(3-3u+u^2)-2
+\tfrac12\log_2(1/u)+\tfrac32\log_2(1/(1-u)).
\]
Since \(3-3u+u^2\ge1\) and
\[
u_L\le3^L t\le3^L2^{-m},
\]
we have
\[
d_{L+1}\ge\tfrac12(m-L\log_2 3)-2\ge m/8.
\]
The one omitted node-height contribution is
\((3/2)^{m-L-1}d_{L+1}\), which proves (7.5). Thus the logarithmic bottom-scale count is necessary, up to constants, for this prefix-and-suffix hybrid architecture. This is not a lower bound for every possible variational statistic.

## 8. Why this survives the two known information barriers

The low-level barrier retains labelled Fourier sets of small cardinality and merges the remainder. The present certificate retains conditional activation patterns at selected heights of an actual physical composition tree. A pattern at a low physical height is observed inside every active subtree, including those belonging to arbitrarily large global Fourier sets. The mechanism therefore preserves information that small-cardinality projections discard.

For fixed \(\varepsilon\), the bottom cutoff grows with depth. It is not a fixed-depth code. The top-scale portion of Theorem 6.1 retains the rare empty/nonempty decisions that otherwise leave an additive influence-scale loss. Every contribution belongs to one normalized hybrid law, and the exact loss is a single nonnegative KL divergence.

The unweighted L2 barrier is also respected: the statistic here is a logarithmic likelihood ratio under \(Q_m\). Rare branch patterns contribute their full logarithmic reference probability. No quadratic Booleanity norm is substituted for that logarithm.

The physical tree is an essential hypothesis. An arbitrary composition-prime Boolean gate need not admit it. Producing a comparable source-valid reference law or an affordable adaptive physical hierarchy for those gates remains an unresolved full-FEI task.

## 9. Verification and reproducibility

The accompanying CHECKER.py uses Python's standard library, exact integer Walsh transforms for small genuine Boolean sources, and high-precision Decimal arithmetic for the explicit formulas.

It checks:

1. the source entropy/influence and local branching law for ternary majority and five-input majority;
2. the exact full KL sum (3.3) against the independent I-projection entropy formula;
3. finite-depth remainder bound (5.1) for multiple cutoffs and depths;
4. the bottom-only center-6 certificate for recursive ternary majority;
5. the two-sided \(\varepsilon I\) certificate for both generators;
6. for a genuine nine-bit depth-two majority source, direct enumeration of all nonempty leaf sets, normalization of the one hybrid reference, and equality of its variational expectation to the claimed partial KL sum.

The executed checker returned **PASS**: 266 finite remainder checks, both generators through depth 128, all displayed certificate inequalities, 512 independently generated truth-table entries for the nine-bit source, and all 511 nonempty sets for the hybrid normalization. Decimal computations support implementation and do not replace the analytic arbitrary-depth proofs.

For orientation, with \(\varepsilon=1/4\), ternary-majority depth 128 retains 18 bottom and 5 top heights; its measured omitted KL divided by influence is approximately 0.109684, below the proved 0.25 ceiling. Five-input-majority depth 128 retains 12 bottom and 4 top heights, with the corresponding ratio approximately 0.107691. These are finite numerical illustrations of Theorem 6.1.

## 10. Exact next implication

A full proof cannot assume that every Boolean source is a regular iterated composition. The next mathematical target is to construct a source-valid physical hierarchy for a wider class, with conditional activation laws and a hybrid reference whose omitted entropy admits an estimate analogous to (5.1).

The decisive feature to transport is the two geometric telescopings in (5.1): source active-node weights pay the fine-scale term, and the product-reference empty-block probability pays the coarse-scale term. A proposed generalization must reproduce both effects and must keep one normalized reference law. Merely summing event KLs or replacing \(K_{\rm occ}\) by a fixed fraction is not justified.

**Full FEI remains open.**
