# An explicit convergence rate for half-averaged four-type operators

Parent derivation, 14 September 2026. This note supplies a quantitative version of agent020's qualitative half-step argument. Agent024 independently verified every inequality, the preimage choice, boundary cases, and the exact rational constants; its full report and arithmetic certificate accompany this note. All operators satisfy the strict non-Volterra conditions in `FOUR_TYPE_UNIQUENESS.md`.

Let \(T=(I+V)/2\), \(q=49/128\), \(d=1-2q=15/64\), and
\[
\varepsilon=d^2/2=225/8192,\qquad R=1-\varepsilon=7967/8192.
\]
Then
\[
\|T^n x-x^*\|_1\le 2R^{n-3}\qquad(n\ge3),
\]
where \(x^*\) is the unique fixed point and \(x\) is any simplex point. The rate is a sufficient bound; no optimality is claimed.

## The two-step cap

For a coordinate \(k\), put \(s=x_k\), \(v=V_k(x)\), and \(y=Tx\). Then \(0\le v\le(1-s)^2\), \(y_k=(s+v)/2\), and \(y_i\ge x_i/2\). The nonnegative coefficient defect implies
\[
(1-y_k)^2-V_k(y)
=\sum_{i,j\ne k}(1-P_{ij,k})y_i y_j
\ge\tfrac14[(1-s)^2-v].
\]
It follows by expansion that
\[
(T^2x)_k\le\frac{3+(2s-1)v+v^2}{8}.
\]
This expression is convex in \(v\). At its two allowed endpoints it equals \(3/8\) and \([3+s^2(1-s)^2]/8\), respectively. Since \(s(1-s)\le1/4\), every coordinate is at most \(q\). This reproduces agent008's sharp cap.

The images \(S_j=T^j(\Delta_3)\) are nested and invariant under \(T\). Thus \(S_3\subset S_2\subset K_q\). The cap \(K_q\) itself need not be invariant.

## A uniform overlap bound

For \(m\in\Delta_3\), define the column-stochastic matrix
\[
A(m)_{ki}=\sum_a m_aP_{ai,k}.
\]
For two nonnegative unit-sum columns \(a,b\), their total-variation distance is \(1-\sum_k\min(a_k,b_k)\). We prove that every pair of columns of \(A(m)\) has overlap at least \(\varepsilon\) whenever
\[
m=\tfrac12(T^3x+T^3y).
\tag{1}
\]

Fix two different column indices. If both corresponding masses are at least \(\varepsilon\), the columns contain the common offspring distribution \(P_{ij,\cdot}\), multiplied by \(m_j\) and \(m_i\), respectively. Their overlap is at least \(\min(m_i,m_j)\ge\varepsilon\).

Otherwise let \(r\) be an index in the pair with \(m_r=t<\varepsilon\), and write the other index as \(j\); the two remaining indices are \(k,\ell\). Because every coordinate of \(m\) is at most \(q\), each coordinate other than \(r\) is at least
\[
1-t-2q=d-t>\varepsilon.
\tag{2}
\]
In particular, there cannot be a second coordinate below \(\varepsilon\).

Choose \(z\) from \(\{T^2x,T^2y\}\) so that \((Tz)_r\le m_r=t\). Such a choice exists by (1). Both \(z_r\le2t\) and \(V_r(z)\le2t\), while \(z\in K_q\). Hence every \(z_a\) with \(a\ne r\) is at least \(d-2t>0\). For any distinct \(a,b\ne r\),
\[
2P_{ab,r}(d-2t)^2\le2P_{ab,r}z_a z_b\le V_r(z)\le2t.
\]
Thus
\[
P_{ab,r}\le\theta(t):=\frac{t}{(d-2t)^2}.
\tag{3}
\]
For the parental pair \(\ell,j\), the only allowed offspring are \(k,r\); similarly for \(k,j\). Consequently
\[
A_{kj}\ge m_\ell(1-\theta(t)),\qquad
A_{\ell j}\ge m_k(1-\theta(t)).
\tag{4}
\]
For the pair \(r,j\), all offspring belong to \(\{k,\ell\}\), so
\[
A_{kr}+A_{\ell r}\ge m_j.
\tag{5}
\]

The function \(\theta\) is increasing on \([0,\varepsilon]\), and
\[
\theta(\varepsilon)=2048/2401<1.
\]
Put \(h=(d-t)(1-\theta(t))>0\). Equations (2), (4), and (5), together with \(\min(a,h)+\min(b,h)\ge\min(a+b,h)\), show that the two columns overlap by at least
\[
\min(A_{kr},A_{kj})+\min(A_{\ell r},A_{\ell j})\ge h.
\]
Both nonnegative factors defining \(h\) decrease with \(t\). Therefore
\[
h\ge(d-\varepsilon)(1-\theta(\varepsilon))
=\frac{598335}{19668992}
>\frac{225}{8192}=\varepsilon.
\tag{6}
\]
For the last comparison the denominator on the left is \(8192\cdot2401\), and the numerator corresponding to the right is \(540225\). This proves the uniform overlap claim, including \(t=0\).

## From overlap to contraction

Write \(\delta(A)=\max_{i,j}\frac12\|A(e_i-e_j)\|_1\). The overlap result gives \(\delta(A(m))\le1-\varepsilon\) at every midpoint (1). Polarization yields
\[
Tx-Ty=B((x+y)/2)(x-y),\qquad B(m)=\tfrac12I+A(m).
\]
Its columns have equal sum \(3/2\). The zero-sum \(\ell^1\) norm is the maximum of \(\mathbf1_G^TB(e_i-e_j)\) over all subsets \(G\) and column pairs. If the two indices lie on the same side, the identity term cancels and the bound is \(\delta(A)\). If they cross against the identity sign, the bound is \(-1/2+\delta(A)\). If they cross with its sign, singleton and triple cuts give at most \(1/2\), while a two-pair cut gives at most \(1/2+q\) by the transfer lemma in the main note. Therefore
\[
\|B(m)|_{\sum z_i=0}\|_{1\to1}
\le\max\{1-\varepsilon,1/2+q\}=R<1.
\]
For \(x,y\in S_3\), their midpoint has form (1), so \(T\) is an \(R\)-contraction on the compact invariant set \(S_3\). The fixed point belongs to this set because \(x^*=T^3x^*\). Iteration and the simplex diameter two prove the displayed global rate.

This result concerns \((I+V)/2\). The original \(V\) can have a period-two orbit. No conclusion of convergence for raw iteration is implied.
