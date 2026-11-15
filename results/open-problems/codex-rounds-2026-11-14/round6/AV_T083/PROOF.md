# The ordinary Bessel estimate for the selected scalar rows

The estimate below supplies the ordinary row bound asserted in OpenAI, *Pointwise convergence of triple ergodic averages for mixing transformations* (October 4, 2026), [base.tex](sources/candidate3-base.tex), lines 553–569, from its stated scalar frequency hypotheses. The source is OpenAI, *An L^3 bound for the trilinear Hilbert transform* (October 5, 2026), [base.tex](sources/H-base.tex), lines 171–209. Its short shell argument is written out here, including the scale count. The chart expansion, Weyl alternative and pooled tails that produce those scalar hypotheses are not assumed proved.

## Statement

Fix d≥1, an integer B≥2 and a real vector θ in R^d. The height of a rational number in lowest terms is the larger of the absolute numerator and positive denominator; vector height is the largest coordinate height. Let N be any subset of

\[
 \{a\cdot\theta:a\in\mathbb Q^d,\ \operatorname{height}(a)\le B\}.
 \tag{1}
\]

Let R be a bounded dyadic interval. Let E be a finite collection of pairs (I,ν), where I is a dyadic subinterval of R and ν belongs to N. Each pair occurs at most once. At every length r, assume the distinct frequencies occurring anywhere at that length satisfy

\[
 |\nu-\nu'|\ge r^{-1}\quad(\nu\ne\nu').                    \tag{2}
\]

Thus separation is imposed on the union of the centers at a depth, not merely on the centers inside each individual interval. For each selected pair let ω_{I,ν} be a C² function compactly supported in the interior of I, with

\[
 \int_I\omega_{I,\nu}=0,\qquad
 \max_{j=0,1,2}r^j\|\omega_{I,\nu}^{(j)}\|_\infty\le A.
 \tag{3}
\]

Let ψ be one fixed measurable function on R, with |ψ|≤1, used at all intervals and frequencies. Set

\[
 W_{I,\nu}f=r^{-1/2}\int_I e(\nu y)\omega_{I,\nu}(y)\psi(y)f(y)\,dy,
 \qquad e(t)=\exp(2\pi i t).
\]

Put

\[
 p=d+1,\quad H_p=p!B^{p^2+p},\quad
 R_p=4pH_p,\quad K_p=\lceil\log_2R_p\rceil,\quad
 S_p=p(K_p+2).
 \tag{4}
\]

Then, for every f in L²(R),

\[
 \left(\sum_{(I,\nu)\in E}|W_{I,\nu}f|^2\right)^{1/2}
 \le26A\sqrt{S_p}\,\|f\|_{L^2(R)}.                       \tag{5}
\]

In particular the squared Bessel bound is at most 676 A² S_p. It is polynomial in d and log(2B), apart from the displayed bump factor. Also

\[
 \#N\le(3B^2)^d,\qquad
 \log(2+\#N)\le\log3+d(\log3+2\log B).                   \tag{6}
\]

If there are no parameters, a single frequency can instead be encoded by d=1 and θ equal to that frequency; zero is encoded in the same way. Empty arrays have zero output. The constant in (5) is a convenient upper bound, with no optimality assertion.

## A scale count for bounded-height evaluations

We first prove the part of H's “Height bins” lemma needed here. Let η be any vector in R^p. Consider the finite set of positive magnitudes

\[
 V=\{|a\cdot\eta|:\operatorname{height}(a)\le B,\ a\cdot\eta\ne0\}.
\]

It can be covered by at most p intervals [s,R_p s]. To prove this, start with any minimally dependent vectors a_1,…,a_k of the indicated height. Minimal dependence implies k≤p+1 and rank k−1. Clear the denominators within each vector, using q_i equal to the product of its p denominators. Then q_i≤B^p and v_i=q_i a_i is integral with entries at most B^p in absolute value: the denominator of the coordinate under consideration is already one factor of q_i.

Choose k−1 coordinate rows of rank k−1. The signed maximal minors of the resulting (k−1)-by-k matrix form an integer null vector b. Each component is nonzero, since a zero component would give a dependence on a proper subset. Expansion of a determinant bounds

\[
 0<|b_i|\le(k-1)!B^{p(k-1)}\le p!B^{p^2}.
\]

Thus c_i=b_iq_i are nonzero integers, |c_i|≤H_p, and Σ_i c_i a_i=0.

Suppose vectors have successively increasing nonzero evaluation magnitudes s_1<⋯<s_k with s_{i+1}>R_p s_i. They must be independent. Otherwise use a minimal dependence as above and let s_* be its largest magnitude. Its term in the evaluated dependence has magnitude at least s_*. The other at most p terms have total magnitude at most

\[
 pH_p s_*/R_p=s_*/4,
\]

which cannot cancel it. There are therefore at most p such separated magnitudes. Greedily cover V, starting with its smallest uncovered element s and covering [s,R_p s]. The chosen starting points are successively separated by more than R_p, so this procedure stops after at most p intervals.

For any r_0>0 and any integer ℓ, a value v in one interval [s,R_p s] can satisfy

\[
 2^\ell\le r_0 2^n v<2^{\ell+1}                           \tag{7}
\]

only for integers n in a real interval of length log₂R_p+1. There are at most K_p+2 such integers. Summing over the at most p covering intervals proves

\[
 \#\{n:\text{some }v\in V\text{ satisfies (7)}\}\le S_p.   \tag{8}
\]

This bound is uniform in η, r_0 and ℓ, including arbitrarily close rational cancellations among the coordinates of η. It counts occupied scales rather than the number of values at one scale.

For completeness, log₂(p!)≤p log₂p gives

\[
 S_p\le p\bigl(5+(p+1)\log_2p+(p^2+p)\log_2B\bigr).
 \tag{9}
\]

Here the extra one in the ceiling and the two in S_p have both been included. Thus S_p is polynomial in p and log(2B); for example (9) is at most 9p³log₂(2pB). This last, looser bound follows by writing L=log₂(2pB)≥1 and bounding the bracket by 5+(p+1)²L≤9p²L.

## Frequency multiplicity

Extend g=ψf by zero to the real line, so ||g||₂≤||f||₂. Use the Fourier convention

\[
 \widehat g(\xi)=\int g(y)e(-\xi y)\,dy.
\]

For every dyadic length r, center ν at that length, and integer ℓ, let P_{r,ν,ℓ} be the orthogonal Fourier projection to

\[
 E_{r,\nu,\ell}=\{\xi:2^\ell/r\le|\xi+\nu|<2^{\ell+1}/r\}.
 \tag{10}
\]

Fix ξ. If ν=a·θ, then ξ+ν=(1,a)·(ξ,θ). This is a bounded-height evaluation in p=d+1 coordinates, with the same bound B. Discard zero evaluations temporarily. Equation (8) shows that (10) can hold at no more than S_p different lengths r, for this ξ and ℓ.

At one such length, the possible centers lie in two intervals of length 2^ℓ/r. Separation (2) bounds their number by

\[
 2(1+2^\ell).
\]

Consequently the multiplicity of the sets (10) is at most

\[
 M_\ell=2S_p(1+2^\ell).                                  \tag{11}
\]

Plancherel and finite summation in r and ν therefore give

\[
 \sum_{r,\nu}\|P_{r,\nu,\ell}g\|_2^2\le M_\ell\|g\|_2^2.
 \tag{12}
\]

For any fixed center, its omitted exact frequency ξ=−ν has Lebesgue measure zero. The catalog is finite, so all such omitted points together are a null set. The projections in (10), as ℓ varies, reconstruct g in L² for each fixed (r,ν).

## The low shells

Fix r,ν,ℓ and put u=e(ν·)P_{r,ν,ℓ}g. Its Fourier support is where 2^ℓ/r≤|η|<2^{ℓ+1}/r. Let u_I be its mean on I. Cancellation in (3) and Cauchy–Schwarz give

\[
 \left|r^{-1/2}\int_I\omega_{I,\nu}u\right|
 \le A\|u-u_I\|_{L^2(I)}
 \le Ar\|u'\|_{L^2(I)}.                                 \tag{13}
\]

One direct justification of the last inequality is
u(x)−u_I=r^{-1}∫_I(u(x)−u(z))dz. Jensen's inequality, the fundamental theorem of calculus, and |x−z|≤r show its squared integral is at most r²||u'||²_{L²(I)}. The band-limited u has an L² derivative, so this argument applies using its absolutely continuous representative.

For fixed r and ν the selected dyadic intervals are disjoint. Summing (13) squared over those intervals and using Plancherel proves

\[
 \sum_{I:|I|=r,(I,\nu)\in E}
 \left|r^{-1/2}\int_I\omega_{I,\nu}u\right|^2
 \le (4\pi A2^\ell)^2\|P_{r,\nu,\ell}g\|_2^2.
 \tag{14}
\]

Indeed ||u'||₂≤2π(2^{ℓ+1}/r)||u||₂. The bumps may depend on ν and on I; only their uniform bounds enter this argument. We use (14) for ℓ<0.

## The high shells

For the same u, define v by

\[
 \widehat v(\eta)=-(2\pi\eta)^{-2}\widehat u(\eta).
\]

Its support avoids zero, v''=u, and

\[
 \|v\|_2\le\frac{r^2}{4\pi^2 2^{2\ell}}\|u\|_2.
\]

Twice integrating by parts creates no boundary terms, because ω_{I,ν} has compact support in the interior of I. Thus

\[
 \left|r^{-1/2}\int_I\omega_{I,\nu}u\right|
 =\left|r^{-1/2}\int_I\omega_{I,\nu}''v\right|
 \le Ar^{-2}\|v\|_{L^2(I)}.
\]

Summing over disjoint intervals at this r,ν gives

\[
 \sum_{I:|I|=r,(I,\nu)\in E}
 \left|r^{-1/2}\int_I\omega_{I,\nu}u\right|^2
 \le\left(\frac{A}{4\pi^2}2^{-2\ell}\right)^2
       \|P_{r,\nu,\ell}g\|_2^2.                          \tag{15}
\]

We use (15) for ℓ≥0. These integrations hold in the weak derivative sense, or by approximation by smooth band-limited functions; both sides are continuous in the L² input norm.

## Summing the shells

Let V_ℓ be the output vector whose (I,ν) coordinate is the row applied to P_{r,ν,ℓ}g. Equations (12), (14) and (15) yield

\[
 \|V_\ell\|_{\ell^2(E)}\le c_\ell\sqrt{M_\ell}\|g\|_2,
 \quad
 c_\ell=\begin{cases}
 4\pi A2^\ell,&\ell<0,\\
 A(4\pi^2)^{-1}2^{-2\ell},&\ell\ge0.
 \end{cases}
\]

For ℓ<0, sqrt(M_ℓ)≤2sqrt(S_p); for ℓ≥0 it is at most 2sqrt(S_p)2^{ℓ/2}. Therefore

\[
 \begin{split}
 \sum_\ell\|V_\ell\|
 &\le A\sqrt{S_p}\left(
 8\pi\sum_{\ell<0}2^\ell+
 \frac1{2\pi^2}\sum_{\ell\ge0}2^{-3\ell/2}\right)\|g\|_2\\
 &=A\sqrt{S_p}\left(8\pi+
 \frac1{2\pi^2(1-2^{-3/2})}\right)\|g\|_2
 <26A\sqrt{S_p}\|g\|_2.                                 \tag{16}
 \end{split}
\]

For a rational audit of the constant, use π<22/7, π>3 and 2^{-3/2}<3/8. The parenthesis in (16) is less than 176/7+4/45=7948/315<26. Absolute summability in (16) permits Minkowski's inequality and the shell reconstruction of each row, proving (5). There are finitely many row coordinates, so no additional convergence issue occurs.

To prove (6), there are at most (2B+1)B≤3B² rational numbers of height at most B before removing duplicate representations. There are at most (3B²)^d coefficient vectors, hence no more distinct evaluations. Since this upper bound is at least one, 2+#N≤3(3B²)^d, giving the stated logarithmic inequality.

## Application to the source assertion

In H-base.tex the retained centers at each nonexceptional scale are clump representatives. They are selected from one finite main catalog and are separated by more than ε^{-1}/r. For an opposing slot the row frequency is ν=±γ/(b−a), with a,b distinct elements of {0,1,2,3}. Choose ε≤1/3, which is permitted by the source's choice of a sufficiently small ε. Then (2) holds for the whole set of representatives at that scale, uniformly over its intervals.

H-charts.tex, “Single-scale separation”, states γ=β+σ·θ, with bounded-height rational σ, and H-base.tex fixes the original parameters before varying scale. Include β as one more unrestricted real parameter and absorb the rational factor ±1/(b−a) into the coefficient height. Thus (1) holds for one fixed parameter vector. Its dimension is O(1+log H), and log B is polynomial in the source parameter \(\mathcal K=1+m+\log(2H)\), conditional on the chart and truncation statements used there.

The tensor expansion in H-base.tex supplies interior C² bumps of exact mean zero; their fixed-order derivative bounds are polynomial in the full tensor index. This is exactly (3), with A polynomial in that index. The separated multiplier ψ_e is one fixed bounded function on the birth root. Apply (5) after absorbing it into g; it may be rough and need not satisfy a derivative bound. Each selected interval-center pair occurs once. Restricting to a subroot or any subset of pairs only decreases the sum in (5).

It follows that the asserted joint Bessel bound is polynomial in \(\mathcal K\), with polynomial dependence on the fixed tensor index, provided the source's stated scalar frequency hypotheses hold. Equation (6) also supplies the claimed polynomial logarithm of the catalog size. The complete carriers m_ν=e(ν·)ψ_e remain the same functions at every interval carrying label ν, as required by round 5. The unbounded sizes of β and θ have no effect on either conclusion.

For a linear pooled-tail pair or a fixed predictor entry, the frequency is fixed and there is only one center at each scale; the same argument applies with one parameter. This verifies its ordinary row bound, but does not justify the pooled coefficient envelope or the size of the predictor list.

This completes the check of the ordinary selected-array Bessel step under the source's scalar hypotheses. It does not prove the Weyl alternative, the chart expansion and uniform pooled tails, the projected-input compression bound, the complete separated-scale lemma, the local depth estimate, or any pointwise ergodic theorem.

## Failure tests and limits

Deleting the scale-count hypothesis in general permits one chosen center near each shell at arbitrarily many scales; the above multiplicity argument then supplies no uniform bound. Separation only within individual intervals would not suffice for the center count preceding (11). These are actual dependencies of this proof.

There is a concrete obstruction if the multiplier may vary with the interval. Let R=[0,1], let ν=0, and define

\[
 w(t)=t^3(1-t)^3(t-1/2),\qquad
 \omega(u)=\begin{cases}w(2u-1/2),&1/4\le u\le3/4,\\0,&\text{otherwise}.\end{cases}
\]

The extension is C², supported in the interior of [0,1], and has integral zero by reflection. Its derivatives through order two obey one fixed bound. Put ω_I(y)=ω((y−left(I))/|I|), and replace the common ψ by ψ_I=sign(ω_I). With f=1 every row has magnitude |I|^{1/2}c, where

\[
 c=\int_0^1|\omega(u)|\,du=1/2048.
\]

To check the value independently, write h(t)=t⁴(1−t)⁴. Then w=−h'/8, so the positive half integral of w is h(1/2)/8=1/2048. The affine change of variable in ω and the two halves of its absolute value cancel their factors of two. At every full dyadic depth, the squared row outputs sum to c² because the interval lengths sum to one. At h depths the squared output is h c², while ||f||₂²=1. There is no uniform depth-independent Bessel bound for this altered hypothesis. This example does not apply to the source, where ψ_e is fixed on the birth root.

Exact center frequencies and exact cancellations cause no missing term, because Fourier mass is absolutely continuous for an L² input. Missing depths, empty arrays, repeated centers on different disjoint intervals, complex bumps, arbitrary dyadic root size and arbitrarily small nonzero evaluations are all covered. The C² compact-support hypothesis is stronger than the C¹ assumption of round 5’s abstract smooth-row estimate; it is available for the smooth tensors in this source application.
