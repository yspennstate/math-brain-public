SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B17, 2026-09-23T21:46:42Z.
attacking: near-kernel resonance in the exact dense six-variable Householder pair-sum architecture; remove fragment-center separation and arbitrary-support restrictions on the one-sheet side by rearranging in the original physical coordinates.

# QFORM-HOUSEHOLDER-ROUGH-ONESHEET-REARRANGEMENT-v1

## Status

This is a **supporting sharp-witness exclusion**, not a proof of the unrestricted QFORM conjecture. The full arbitrary-product-law target remains OPEN / NOT PROVED / NOT DISPROVED, and the full continuity conclusion remains separate.

The first previously unpaid implication in this architecture is paid immediately:

> **Theorem (rough one-sheet Householder barrier).** For the exact six-variable matrix `A=T^TBT` below, and for **arbitrary** independent physical probability densities `0<=f_i<=1` on the line (no support, moment, regularity, connectedness, log-concavity, or interval-indicator assumption), the output density of `Q=X^TAX` satisfies
> 
> `ess sup_{s>=0} p_Q(s) <= p_*(0) = 4.0630706168060372601... < 3 sqrt(2)`.
> 
> Here `p_*` is the centered unit-cube control for the same physical matrix. In particular, all positive-side near-kernel resonant fragmentation is harmless even when the old center-gap parameter tends to zero and the previous derivative estimate becomes unusable.

The proof uses the pinned one-sheet ruling theorem at `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` as an exact identity, then performs a six-density Brascamp--Lieb--Luttinger rearrangement **before** any spectral-coordinate independence could be falsely invoked.

## 1. Exact target matrix and physical factorization

Let

\[
T={1\over\sqrt2}
\begin{pmatrix}
1&1&0&0&0&0\\
0&0&1&1&0&0\\
0&0&0&0&1&1
\end{pmatrix},
\qquad
n={1\over\sqrt3}(1,1,1)^T,
\qquad
B=I_3-2nn^T=I_3-{2\over3}{\bf1}{\bf1}^T.
\]

Then `TT^T=I_3` and `B^2=I_3`. Put

\[
A=T^TBT={1\over6}
\begin{pmatrix}
1&1&-2&-2&-2&-2\\
1&1&-2&-2&-2&-2\\
-2&-2&1&1&-2&-2\\
-2&-2&1&1&-2&-2\\
-2&-2&-2&-2&1&1\\
-2&-2&-2&-2&1&1
\end{pmatrix}.
\]

Because `T` is a partial isometry onto `R^3`, the nonzero spectrum of `A` is exactly the spectrum of `B`:

\[
\boxed{\operatorname{spec}(A)=\{1,1,-1,0,0,0\}.}
\]

Thus this is a genuine target-class physical matrix for every input law below.

For independent physical variables `X_1,...,X_6`, define the three disjoint pair sums

\[
Y_j={X_{2j-1}+X_{2j}\over\sqrt2},\qquad j=1,2,3.
\]

The `Y_j` are independent because the three physical pairs are disjoint, and

\[
Q=X^TAX=Y^TBY.
\]

No independence is asserted after diagonalizing `B`.

If `f_{2j-1},f_{2j}` are the physical densities, the bank density is exactly

\[
h_j(y)=\sqrt2\int_{\mathbb R}
 f_{2j-1}(x)f_{2j}(\sqrt2 y-x)\,dx.
\tag{1.1}
\]

This formula is valid for arbitrary cap-one physical laws and already contains all finite/countable fragmentation and near-cancellation phenomena.

## 2. The six-density line-rearrangement lemma

Let `I=[-1/2,1/2]`. For `d=(d_1,d_2,d_3)\in\mathbb R^3`, define

\[
\mathcal J_d(g_{11},g_{12},g_{21},g_{22},g_{31},g_{32})
:=\int_{\mathbb R^4}
\prod_{j=1}^3
 g_{j1}(x_j)g_{j2}(d_j r-x_j)
\,dr\,dx_1dx_2dx_3.
\tag{2.1}
\]

### Lemma 2.1
If every `g_{jk}` is a probability density satisfying `0<=g_{jk}<=1`, then

\[
\boxed{
\mathcal J_d(g_{11},g_{12},g_{21},g_{22},g_{31},g_{32})
\le
\mathcal J_d(1_I,1_I,1_I,1_I,1_I,1_I).
}
\tag{2.2}
\]

#### Proof
The functional is nonnegative and separately linear in each of its six density arguments. Fix five arguments. The remaining dependence has the form

\[
g\longmapsto \int_{\mathbb R}g(z)K(z)\,dz,
\qquad K\ge0.
\]

The cap-one bathtub principle gives

\[
\sup_{0\le g\le1,\ \int g=1}\int gK
=
\sup_{|E|=1}\int_E K.
\tag{2.3}
\]

If `K` is not initially bounded or compactly supported, apply (2.3) to truncated kernels and pass by monotone convergence. Iterating over the six arguments therefore gives

\[
\mathcal J_d(g_{11},...,g_{32})
\le
\sup_{|E_{jk}|=1}
\mathcal J_d(1_{E_{11}},...,1_{E_{32}}).
\tag{2.4}
\]

Now apply the one-dimensional Brascamp--Lieb--Luttinger rearrangement theorem to the six functions of the four variables `(r,x_1,x_2,x_3)` with linear forms

\[
L_{j1}=x_j,\qquad L_{j2}=d_jr-x_j.
\]

Symmetric decreasing rearrangement cannot decrease the integral. Every set `E_{jk}` has measure one, so its symmetric rearrangement is exactly `I`. Hence every term in the supremum in (2.4) is at most the right side of (2.2). This proves the lemma. `\square`

The key point is that the extremal reduction happens in the **six original independent coordinates**. Nothing in this lemma assumes that a rotated spectral triple is independent.

## 3. Exact use of the pinned one-sheet ruling

The completed `COUNTEREXAMPLE_SEARCH.md` at the required pinned source commit proves the exact ruled-level-set identity for a rank-three signature `(1,1,-1)` on its majority-sign side.

Choose an orthonormal basis of `n^\perp`. For each angle `theta`, let `v_theta,u_theta\in n^\perp` be an orthonormal pair. Back-rotating the pinned spectral ruling to the present bank coordinates gives the line

\[
y=\sqrt s\,v_\theta+t(u_\theta+n),
\qquad s\ge0.
\tag{3.1}
\]

Write

\[
d_\theta:=u_\theta+n.
\]

The pinned coarea calculation is invariant under this orthogonal back-rotation and gives, for almost every `s>=0`,

\[
p_Q(s)
={1\over2}\int_0^{2\pi}L_\theta(s)\,d\theta,
\qquad
L_\theta(s):=
\int_{\mathbb R}\prod_{j=1}^3
h_j(\sqrt s\,v_{\theta,j}+t d_{\theta,j})\,dt.
\tag{3.2}
\]

This is where the required pinned result is used as a **real sharp-constant inequality**, not merely quoted for its generic constant.

## 4. Each ruled line is maximized by the centered physical cube

Insert the exact pair-convolution formula (1.1) into `L_theta(s)`. Put

\[
c_j=\sqrt{2s}\,v_{\theta,j},
\qquad r=\sqrt2\,t.
\]

A direct change of variables gives

\[
L_\theta(s)
=2\int_{\mathbb R^4}
\prod_{j=1}^3
f_{2j-1}(x_j)
 f_{2j}(c_j+d_{\theta,j}r-x_j)
\,dr\,dx_1dx_2dx_3.
\tag{4.1}
\]

Now shift `x_j` by `c_j/2` and translate both physical densities in pair `j` by the same amount:

\[
g_{j1}(z):=f_{2j-1}(z+c_j/2),
\qquad
g_{j2}(z):=f_{2j}(z+c_j/2).
\]

Translations preserve probability mass and the cap `<=1`. Equation (4.1) becomes exactly

\[
L_\theta(s)=2\,\mathcal J_{d_\theta}(g_{11},g_{12},...,g_{32}).
\tag{4.2}
\]

Lemma 2.1 therefore yields

\[
L_\theta(s)
\le
2\,\mathcal J_{d_\theta}(1_I,1_I,1_I,1_I,1_I,1_I).
\tag{4.3}
\]

If all six physical variables are centered unit intervals, then each bank has triangular density

\[
h_*(y)=\sqrt2(1-\sqrt2|y|)_+.
\tag{4.4}
\]

At the cone tip `s=0`, the right side of (4.3) is precisely the corresponding ruled-line integral

\[
L^*_\theta(0)=
\int_{\mathbb R}\prod_{j=1}^3h_*(t d_{\theta,j})\,dt.
\tag{4.5}
\]

Thus the **linewise** statement is

\[
\boxed{L_\theta(s)\le L^*_\theta(0)
\quad\text{for every ruling angle and a.e. }s\ge0.}
\tag{4.6}
\]

Integrating (4.6) in the exact pinned coarea formula (3.2) gives

\[
\boxed{
p_Q(s)\le p_*(0)
\quad\text{for a.e. }s\ge0,
}
\tag{4.7}
\]

where `p_*` is the output density for six independent centered unit intervals under the same physical matrix `A`.

This is much stronger than applying the pinned theorem's generic two-dimensional projection ceiling. That generic route gives `pi sqrt(2)`, which is larger than `3 sqrt(2)` and therefore does not certify the proposed sharp constant. The exact ruling plus the original-coordinate rearrangement is the extra ingredient that pays the present class.

## 5. Numerical endpoint supplied by the completed partner chain

The latest compatible fleet03/B17 result at

`math-open-problems@e79bba262d16c5f629722431a39f563c0d8c4094`

uses the same exact physical matrix and records the proved centered-cube cone-tip value

\[
p_*(0)=4.06307061680603726012548\ldots .
\tag{5.1}
\]

It also records the rigorous rational enclosure

\[
p_*(0)<{508\over125}.
\tag{5.2}
\]

The candidate Gaussian sharp obstruction is larger:

\[
{508\over125}<3\sqrt2,
\tag{5.3}
\]

because `(508/375)^2=258064/140625<2`. Combining (4.7)--(5.3) proves

\[
\boxed{
\operatorname*{ess\,sup}_{s\ge0}p_Q(s)
\le p_*(0)
<3\sqrt2.
}
\tag{5.4}
\]

The partner's previous center-gap theorem controlled arbitrary countable interval fragmentation at the cone tip when the nonkernel pair-sum center gap stayed larger than `sqrt(6)/2`; the present result removes **both** the gap condition and the interval-indicator restriction on the entire majority-sign side.

## 6. Explicit near-kernel resonant adversary that defeats the old gap hypothesis

The new theorem is not merely a statement about connected laws. Here is a source-valid family aimed directly at the old unpaid mechanism.

Fix `m>=2`, let `R_k=10^k`, and for each of the three physical pairs use

\[
E_{2j-1}^{(m)}
=\bigcup_{k=1}^m
\left[R_k-{1\over2m},R_k+{1\over2m}\right],
\tag{6.1}
\]

\[
E_{2j}^{(m)}
=\bigcup_{k=1}^m
\left[-R_k+{1\over k}-{1\over2m},
      -R_k+{1\over k}+{1\over2m}\right].
\tag{6.2}
\]

Let each `X_i` have density `1_{E_i^{(m)}}`. The intervals are disjoint, every support has total length exactly one, and hence every marginal is an exact cap-one probability density. There are no moment or bounded-support assumptions in the theorem, although each finite `m` witness is itself perfectly legitimate.

For a matched fragment with label `k`, the physical pair-center sum is `1/k`, so the bank center is `1/(sqrt(2) k)`. Choosing the matched label `k=m` in all three pairs gives a nonkernel product-cell center `c_m` with

\[
|Tc_m|={1\over m}\sqrt{3\over2}.
\tag{6.3}
\]

Therefore the old nonkernel gap satisfies

\[
\Delta_m\le {1\over m}\sqrt{3\over2}\longrightarrow0.
\tag{6.4}
\]

In particular its derivative parameter `M=Delta-sqrt(6)/2` is negative for all sufficiently large `m`, so the previous six-chart center-gap estimate is deliberately inapplicable. At the same time the individual physical centers `R_k` are arbitrarily remote, exactly realizing **near-kernel resonance** rather than ordinary compact support.

Nevertheless (5.4) gives, for every `m`,

\[
\boxed{
\operatorname*{ess\,sup}_{s\ge0}p_{Q_m}(s)
\le p_*(0)<3\sqrt2.
}
\tag{6.5}
\]

Thus remote paired fragments can tunnel back to bounded pair-sum centers, even with `Delta_m->0`, but they still cannot create a majority-sign sharp-constant overshoot in this architecture.

## 7. Scope boundary and interpretation

What has been ruled out is now substantially broader than the preceding fragment theorem:

- arbitrary six physical cap-one densities, not only finite/countable unions of intervals;
- arbitrary support diameter and arbitrarily remote pieces;
- exact or approximate pair cancellations, including `Delta=0` limits;
- arbitrary near-kernel resonance on the **majority-sign one-sheet side**;
- the true positive-side output level, not only the cone tip.

What remains unpaid is equally explicit. The negative-output side of this `(+, +, -)` Householder form is the two-sheet/minority-sign geometry, where the straight-line ruling used above does not exist. The live correction forbidding a generic two-sheet X-ray-only shortcut remains binding. A proof for that side must use additional structure, not pretend Theorem C already covers it. Other shared/intermediate-leverage frames and additional active spectrum also remain outside this theorem.

Failure of this one-sheet rearrangement mechanism to extend to the two-sheet side would be a **proof-mechanism limitation**, not a counterexample. A valid example with peak above `3sqrt(2)` would refute the proposed sharp constant but would not by itself refute existence of some larger universal QFORM constant. A genuine counterexample to QFORM must force the essential density norm beyond every finite universal constant.

## 8. Source bookkeeping

Required pinned source actually used:

- `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `COUNTEREXAMPLE_SEARCH.md`, completed Theorem C exact one-sheet ruling/coarea identity. The generic `pi sqrt(2)` ceiling is explicitly **not** sufficient for the sharp certificate; the exact ruling is fed into Lemma 2.1.

Latest compatible designated partner actually used:

- fleet03/B17, `math-open-problems@e79bba262d16c5f629722431a39f563c0d8c4094`, `QFORM-DENSE-FRAGMENT-KERNEL-AGGREGATE-v1`, supplying the same exact target matrix, the proved endpoint `p_*(0)`, and the near-kernel-resonance frontier that this run closes on the one-sheet side.

Status: `SUPPORTING_SHARP_WITNESS_EXCLUSION`; full QFORM `OPEN / NOT PROVED / NOT DISPROVED`; native brain status `WITHOUT_VERIFIED_BRAIN`.
