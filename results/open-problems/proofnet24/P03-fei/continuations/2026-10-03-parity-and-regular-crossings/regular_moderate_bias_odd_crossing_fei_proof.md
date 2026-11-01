# Ordinary FEI for moderate-bias odd crossings with bounded weight ratio

Date: 2026-10-03. **Complete proof; independent internal analytic audit passes.**
This is a restricted ordinary Fourier entropy–influence result, without
output parity. Historical novelty is unverified. It does not resolve
arbitrary-weight three-crossing FEI or full Boolean FEI.

## Statement and explicit constants

All inputs are uniform on \(\{-1,1\}^n\), entropy is in bits, and
\(I_i(f)=\Pr[f(X)\ne f(X^{\oplus i})]\) is physical influence.
Let \(B\ge1\), \(\lambda\ge0\), and let \(m\ge1\) be odd. Assume
\[
 1\le w_i\le B,\qquad S(X)=\sum_{i=1}^n w_iX_i,
 \qquad \sigma^2=\sum_iw_i^2.
\]
Let \(F:\mathbb R\to\{-1,1\}\) have exactly \(m\) distinct genuine
crossings \(\theta_1<\cdots<\theta_m\): it is constant on each
complementary open interval, the labels on successive intervals are
opposite, and at each crossing its value is one of the two adjacent labels.
No other isolated point anomalies are allowed. Suppose
\[
 |θ_r|\le\lambda\sigma\quad(1\le r\le m).
\tag{1}
\]
Put \(g(X)=F(S(X))\). There is an explicit constant depending only on
\((m,B,\lambda)\) such that
\[
 \boxed{H(g)\le C(m,B,\lambda)I(g).}
\tag{2}
\]
In particular, (2) includes arbitrary-spacing three-crossing functions
under the stated weight and bias restrictions.

Here are concrete, deliberately unoptimized choices. Define
\[
 d=\frac{e^{-(\lambda+1)^2}}{\sqrt{2\pi}},\qquad
 c_D=\sqrt{2/3},\qquad E=2.24\sqrt2,
 \qquad A=\frac{41}{\sqrt2(1-e^{-1})},
\]
\[
 K=\max\left\{1,\left\lceil
       \left(\frac{2EmB}{dc_D}\right)^2\right\rceil\right\},
 \qquad
 N_0=\left\lceil\max\{2KB^2,K^2B^2\}\right\rceil.
\tag{3}
\]
Then (2) holds with
\[
 \boxed{C(m,B,\lambda)=
 \max\left\{\log_2N_0+3,
       \frac{(1+4Am)B\sqrt K}{(\ln2)dc_D}\right\}.}
\tag{4}
\]
In dimension zero entropy is zero, so the theorem is immediate. We prove
the statement below for \(n\ge1\).

Multiplying all weights and crossing points by the same positive number
does not change the Boolean function or condition (1). Thus the weight
premise equivalently requires that the ratio of the largest to the
smallest nonzero absolute weight is at most \(B\). Delete zero-weight
coordinates first; entropy and influence are unchanged by deleting them.
Arbitrary signs of the remaining weights are handled by coordinate sign
flips, which preserve the squared Fourier law and physical influences.
The crossing condition is imposed after scaling, relative to the resulting
score standard deviation.

## Established inputs and normalization

We use two established results.

1. Klivans–O'Donnell–Servedio, *Learning intersections and thresholds of
   halfspaces* (2004), Theorem 18, gives for every halfspace \(h\)
   \[
   \operatorname{NS}_\varepsilon(h)
      \le20.5p\sqrt{\varepsilon\ln(1/p)},
   \quad p=\min\{\Pr[h=1],\Pr[h=-1]\}.
   \tag{5}
   \]
   The noise here independently **flips** every coordinate with probability
   \(\varepsilon\). Constant halfspaces have noise sensitivity zero.
   Since \(p\sqrt{\ln(1/p)}\le1\), (5) implies
   \(\operatorname{NS}_\varepsilon(h)\le20.5\sqrt\varepsilon\).
   The author-hosted [full primary manuscript](https://www.cs.columbia.edu/~rocco/Public/focs02.pdf)
   states Theorem 18 on printed page 9. Its Theorem 21 already proves the
   union-bound noise estimate for functions of finitely many halfspaces.

2. The Berry–Esseen theorem for independent mean-zero summands with total
   variance \(s^2>0\) gives
   \[
   \sup_t\left|\Pr[R\le t]-\Phi(t/s)\right|
      \le0.56\frac{\sum_i\mathbb E|Z_i|^3}{s^3},
   \quad R=\sum_iZ_i.
   \tag{6}
   \]
   The constant \(0.56\) for nonidentical summands is stated explicitly
   in the unnumbered Berry–Esseen theorem in Section 11.5, printed page
   350, of O'Donnell's author-hosted
   [*Analysis of Boolean Functions*](https://www.cs.cmu.edu/~odonnell/papers/Analysis-of-Boolean-Functions-by-Ryan-ODonnell.pdf).
   For weighted signs bounded by \(B\), the right side of (6) is at most
   \(0.56B/s\).

Classical weak logarithmic FEI will handle bounded dimension. In the same
normalization, for every Boolean \(f\) and \(n\ge1\),
\[
 H(f)\le(\log_2n+3)I(f).
\tag{7}
\]
For completeness, let \(r\le1/2\) be the minority probability and
\(v=4r(1-r)\). Cube edge isoperimetry gives
\(I(f)\ge2r\log_2(1/r)\), and the elementary binary entropy estimate
\(h_2(v)\le4r\log_2(1/r)\) gives \(h_2(v)\le2I(f)\).
Conditional on a nonempty Fourier index, compare the spectral law to
\(Q(S)=n^{-|S|}/Z_n\), where
\(Z_n=(1+1/n)^n-1<2\). Nonnegative finite relative entropy gives
\[
 H(f)\le h_2(v)+I(f)\log_2n+v\log_2Z_n
        \le(\log_2n+3)I(f),
\]
using \(v\le I(f)\). Constants are handled before introducing the
conditional law. The edge-isoperimetric induction and each empty-atom
inequality are reproduced in the separate
[logarithmic parity proof](output_parity_unate_gate_combinations_logarithmic_proof.md).
Weak \(O(\log n)\) FEI is established prior work; see Section 1.1 and
Lemma 1.5 of the primary
[Wan–Wright–Wu manuscript](https://arxiv.org/pdf/1312.3003).

## Entropy upper bound from the halfspace noise estimate

There are halfspaces \(h_r\) changing sign at \(\theta_r\), each with
the tie choice needed to give
\[
 g=\eta\prod_{r=1}^m h_r,
\tag{8}
\]
for a constant sign \(\eta\). On the finite set of attained cube scores,
either tie choice is realizable by a small perturbation of that threshold.
This perturbation is used only to apply (5); the original crossing points
and bias condition are retained throughout the influence argument.
If \(g\) changes under noise, some \(h_r\) changes, so (5) and the
union bound give
\[
 \operatorname{NS}_\varepsilon(g)\le20.5m\sqrt\varepsilon.
\tag{9}
\]

Let \(D\) be the degree of a random squared-Fourier index, with law
\(W_j=\sum_{|S|=j}\widehat g(S)^2\). For integers \(k\ge1\), use
\(\varepsilon=1/(2k)\). The exact Fourier noise identity is
\[
 2\operatorname{NS}_\varepsilon(g)
    =\sum_S\widehat g(S)^2[1-(1-2\varepsilon)^{|S|}].
\]
Since \((1-1/k)^k\le e^{-1}\), including \(k=1\),
\[
 \Pr[D\ge k]\le\frac{Am}{\sqrt k}.
\tag{10}
\]
For real \(t>0\), \(\Pr[D\ge t]=\Pr[D\ge\lceil t\rceil]\), so
it is at most \(Am/\sqrt t\). Entropy conditional on degree is at
most \(\log_2\binom nj\), hence
\[
 H(g)\le\log_2(n+1)
       +\frac1{\ln2}\mathbb E[D\ln(en/D)].
\]
The expression at \(D=0\) is defined as zero. Put
\(b(t)=t\ln(en/t)\), so \(b'(t)=\ln(n/t)\ge0\) on \((0,n]\).
Layer cake and (10) imply
\[
 \mathbb E b(D)=\int_0^n\Pr[D\ge t]\ln(n/t)\,dt
       \le Am\int_0^nt^{-1/2}\ln(n/t)\,dt
       =4Am\sqrt n.
\]
Finally \(\ln(n+1)\le\sqrt n\) for \(n\ge1\): the derivative of
\(\sqrt n-\ln(n+1)\) is nonnegative because
\(n+1\ge2\sqrt n\), and its value at one is positive. We have proved
\[
 \boxed{H(g)\le C_H\sqrt n,\qquad C_H=(1+4Am)/\ln2.}
\tag{11}
\]
The upper bound (11) does not require odd \(m\), comparable weights,
or moderate crossing bias; those enter the influence lower bound next.

## A translation measure estimate using opposite tails

Because \(m\) is odd, the two tail labels of \(F\) are opposite.
For any real \(u,v\), let
\[
 A_{u,v}=\{r:F(r+u)\ne F(r+v)\}.
\]
Endpoint assignments affect only finitely many points. Let \(A^\circ_{u,v}\)
be the union of open intervals between the translated crossing points
on which these outputs differ, excluding all translated crossing points.
This is a union of at most \(2m\) disjoint bounded open intervals,
and differs from \(A_{u,v}\) only at finitely many points. Its endpoints
belong to \(\{\theta_r-u,\theta_r-v\}_r\); in particular,
\[
 A^\circ_{u,v}\subseteq
 [\theta_1-\max(u,v),\theta_m-\min(u,v)].
\tag{12}
\]
There are at most \(2m\) distinct endpoints and the two exterior
intervals have equal translated labels. Even if coincident endpoints
create a point hole in an otherwise pivotal interval, deleting that point
is compatible with the bound of \(2m\) open components.

Let the right and left tail labels be \(a_+\) and \(a_-=-a_+\).
The elementary signed translation identity is
\[
 \int_{\mathbb R}[F(r+v)-F(r+u)]\,dr
       =(v-u)(a_+-a_-).
\tag{13}
\]
For example, integrate over \([-L,L]\) with all translated crossings
strictly inside; cancellation leaves two tail intervals of length
\(|v-u|\). The integrand has absolute value two exactly on the
pivotal set, so (13) gives
\[
 \boxed{|A^\circ_{u,v}|\ge|u-v|.}
\tag{14}
\]
This is the only use of odd crossing count. It is uniform in the gaps
between crossing points.

## Fixed-size resampling and an influence lower bound

Assume \(n\ge N_0\), so in particular \(n\ge K\). Choose a uniformly
random \(K\)-subset \(J\subseteq[n]\), independent of all signs.
Write independent selected old and fresh scores, and the remaining score,
as
\[
 U=\sum_{i\in J}w_iX_i,
 \qquad V=\sum_{i\in J}w_iY_i,
 \qquad R=\sum_{i\notin J}w_iX_i.
\]
Conditional on \(J\), the variables \(U,V,R\) are independent and
\(|U|,|V|\le KB\). The old and resampled outputs are
\(F(R+U)\) and \(F(R+V)\). Set
\(s^2=\operatorname{Var}(R)=\sigma^2-\sum_{i\in J}w_i^2\).
The choice of \(N_0\) gives
\[
 \sigma^2\ge n\ge2KB^2,
 \qquad s^2\ge\sigma^2/2>0,
 \qquad KB\le\sqrt n\le\sigma.
\tag{15}
\]

By (1), (12), and (15), each relevant open interval lies in
\([-(\lambda+1)\sigma,(\lambda+1)\sigma]\). Throughout this interval
the density of \(N(0,s^2)\) is at least
\[
 \frac1{\sqrt{2\pi}s}\exp[-r^2/(2s^2)]
       \ge\frac{e^{-(\lambda+1)^2}}{\sqrt{2\pi}\sigma}
       =\frac d\sigma.
\tag{16}
\]
Meanwhile (6) gives CDF distance at most
\(\delta=0.56B/s\le0.56\sqrt2B/\sigma\).
For an open interval \((a,b)\),
\[
 \Pr[R\in(a,b)]\ge\Pr[N(0,s^2)\in(a,b)]-2\delta.
\tag{17}
\]
Indeed its discrete probability is \(\Pr[R<b]-\Pr[R\le a]\),
and the CDF estimate also holds for the left limit at \(b\), since
the Gaussian CDF is continuous. This justifies (17) at attained-score
atoms without a continuity assumption on the discrete score law.

Apply (17) to the at most \(2m\) open components. For every fixed
\(J,U=u,V=v\), equations (14) and (16) yield
\[
 \Pr[F(R+u)\ne F(R+v)]
       \ge\frac{d|u-v|-EmB}{\sigma}.
\tag{18}
\]
Negative right sides cause no problem. The estimate ignores any pivotal
endpoint atoms, which can only increase the true probability.

Let \(D_J=U-V\), and put \(a_J=\sum_{i\in J}w_i^2\ge K\).
Independence and the moments of \(X_i-Y_i\) give exactly
\[
 \mathbb E D_J^2=2a_J,
 \qquad
 \mathbb E D_J^4=3(2a_J)^2-4\sum_{i\in J}w_i^4
       \le3(2a_J)^2.
\]
Hölder interpolation gives
\(\mathbb E D_J^2\le(\mathbb E|D_J|)^{2/3}
 (\mathbb E D_J^4)^{1/3}\). Therefore
\[
 \mathbb E|D_J|\ge\sqrt{2a_J/3}\ge c_D\sqrt K.
\tag{19}
\]
Average (18), use (19), and then the choice of \(K\) in (3):
\[
 \begin{aligned}
 \Pr[g(X)\ne g(X^{\mathrm{resample}\,J})]
 &\ge\frac{dc_D\sqrt K-EmB}{\sigma}\\
 &\ge\frac{dc_D\sqrt K}{2\sigma}
 \ge\frac{dc_D\sqrt K}{2B\sqrt n}.
 \end{aligned}
\tag{20}
\]

For the reverse comparison, resample the selected coordinates one at a
time. Each intermediate input is uniform. Resampling coordinate \(i\)
changes the output with probability \(I_i(g)/2\): the fresh sign is
opposite the previous sign with probability one half, independently of
the pivotal event. A union bound, averaged over the uniformly random
subset, gives
\[
 \Pr[g(X)\ne g(X^{\mathrm{resample}\,J})]
       \le\frac12\mathbb E_J\sum_{i\in J}I_i(g)
       =\frac{K}{2n}I(g).
\tag{21}
\]
Combining (20) and (21) proves the quantitative lower bound
\[
 \boxed{I(g)\ge\frac{dc_D}{B\sqrt K}\sqrt n
        \qquad(n\ge N_0).}
\tag{22}
\]
The subset is independent of both old and fresh signs throughout; no
conditioning on the output is used.

## Finish the FEI bound and record its limits

For \(n\ge N_0\), divide (11) by (22) to obtain the second constant
in (4). For \(1\le n<N_0\), apply (7) and
\(\log_2n+3\le\log_2N_0+3\). This proves (2) in every dimension.

The result is an ordinary FEI bound for all crossing spacings, but its
constant depends on a bounded ratio of nonzero weights and bounded
normalized bias. It provides no constant uniform over arbitrary weight
ratios or threshold biases. The proof does not apply to even crossing
count: equal tail labels make the signed integral (13) vanish, and a
narrow rare slab can have much smaller influence than \(\sqrt n\).
It does not resolve general three-crossing FEI or full Boolean FEI.

The halfspace noise estimate, Berry–Esseen theorem, weak logarithmic FEI,
and the generic conversion from noise tails to an entropy bound are prior
mathematical tools. The specific restricted-class consequence has not
been checked for historical priority. No novelty or external peer-review
claim is made. The separate [independent analytic audit](regular_moderate_bias_odd_crossing_heat_audit.md)
passes each step. The [author checker](verify_regular_moderate_bias_odd_crossing.py)
and [report](regular_moderate_bias_odd_crossing_checks.json) pass 9,552 exact
translation/measure checks, 648 exact block moment and resampling checks,
7,152 endpoint-atom checks, and 960 exact degree/noise inequalities.
The [independent checker](verify_regular_odd_crossing_heat.py) and
[report](regular_odd_crossing_heat_checks.json) separately pass 2,400 exact
translation pairs, 18,166 legal endpoint assignments, 300 moment checks,
3,048 resampling masks and 168 exact averages. Gaussian comparisons are
labeled numerical supplements. Neither implementation enumerates a cube
at the enormous large-dimension cutoff; the analytic proof establishes
that regime. These are internal checks, not external peer review.

The separate [input-regular proof](input_regular_moderate_bias_odd_crossing_fei_proof.md)
removes the individual lower-weight requirement. This bounded-ratio
proof is preserved because it has a smaller block-size choice. Candidates
are separately retained, with no edits to older stable results.

## Prior work and known overlaps

Chakraborty, Kulkarni, Lokam and Saurabh, *Upper Bounds on Fourier Entropy*,
[primary ECCC revision 2](https://eccc.weizmann.ac.il/report/2013/052/revision/2/download/),
Theorem 4.5, already converts a noise sensitivity power bound into a
Fourier entropy bound. Their Corollary 4.8 supplies the established LTF
entropy bound of order square root of the dimension. Together with
KOS Theorem 21 and the edge-flip union bound, this framework gives
entropy of order m times square root of the dimension for functions
of m halfspaces. The explicit degree-tail integral above is a variant
of this established argument, and is not claimed new.

The one-crossing case is a linear threshold function and is not a
claimed novelty. Prior regular-LTF FEI appears in Corollary 10 of the
[primary regular/random-LTF manuscript](https://iuuk.mff.cuni.cz/~koucky/LBCAD/papers/random-ltf.pdf).
Its Definition 9 normalizes and bounds the bias as an additional weight;
our input regularity and normalized crossing bias are stated separately.
When all weights are equal, arbitrary score labelings are symmetric,
so FEI is already covered by the O'Donnell–Wright–Zhou
[primary symmetric-function theorem](https://www.cs.cmu.edu/~odonnell/papers/fei.pdf).
These overlaps must be credited. The specific m at least three weighted
odd-crossing consequence has not been certified historically new.
