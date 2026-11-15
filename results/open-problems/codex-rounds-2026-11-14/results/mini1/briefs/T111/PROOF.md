# Rare midpoint contamination of a two-point law

Let \(0<p<1\), \(q=1-p\), and \(\lambda\geq0\) be fixed. For every integer \(n>\lambda\), let \(Z_{n,1},\ldots,Z_{n,n}\) be iid within the row, with
\[
 \Pr(Z_{n,1}=0)=(1-\lambda/n)q,\qquad
 \Pr(Z_{n,1}=1)=\lambda/n,\qquad
 \Pr(Z_{n,1}=2)=(1-\lambda/n)p.
\]
Write \(\mu_n=EZ_{n,1}\), \(\sigma_n^2=\operatorname{Var}Z_{n,1}\),
\(X_{n,i}=(Z_{n,i}-\mu_n)/\sigma_n\), and
\[
 \rho_n=E|X_{n,1}|^3,\qquad
 \Delta_n=\sup_x\left|\Pr\left(n^{-1/2}\sum_iX_{n,i}\leq x\right)-\Phi(x)\right|.
\]
Different rows need not have the same law. Every row satisfies the hypotheses of the iid Berry–Esseen problem.

**Theorem.** The following limit holds:
\[
 \boxed{\lim_{n\to\infty}\frac{\sqrt n\,\Delta_n}{\rho_n}
 =R(p,\lambda):=
 \frac{1}{\sqrt{2\pi}(p^2+q^2)}
 \left(\frac{|q-p|}{6}+\frac{1+e^{-2\lambda}}4\right).}                 \tag{1}
\]
In particular, with \(B=3(1+e^{-2\lambda})\),
\[
 \boxed{\sup_{0<p<1}R(p,\lambda)
 =K(\lambda):=\frac{B+\sqrt{B^2+4}}{12\sqrt{2\pi}}.}                 \tag{2}
\]
The maximizers satisfy
\[
 |1-2p|=\frac{\sqrt{B^2+4}-B}{2}.
\]
Thus \(K(0)=C_E=(3+\sqrt{10})/(6\sqrt{2\pi})\), and
\(K(\lambda)<C_E\) whenever \(\lambda>0\). The order of operations in (2) is important: it optimizes the limit in (1), with \(p\) fixed in that limit. It is not a uniform-in-\(p\) theorem.

## 1. A binomial expansion, including the lattice correction

For fixed \(p\in(0,1)\), let \(B_m\) have distribution \(\operatorname{Bin}(m,p)\). Put \(v=mpq\), \(d=v^{-1/2}\), \(z=(r-mp)d\), and let \(\{r\}=r-\lfloor r\rfloor\). Uniformly over real \(r\),
\[
 \Pr(B_m\leq r)=\Phi(z)+d\phi(z)
 \left[\frac{q-p}{6}(1-z^2)+\frac12-\{r\}\right]
 +O_p\left(\frac{(\log m)^4}{m}\right).                              \tag{3}
\]
Only \(m\to\infty\) is intended here; constants may depend on the fixed \(p\).

Here is a derivation of the error order used in (3). For an integer \(l\), set \(u=(l-mp)/\sqrt v\). In the range \(|u|\leq\sqrt{48\log m}\), Stirling's formula gives
\[
 \log\Pr(B_m=l)=-\tfrac12\log(2\pi v)-u^2/2
 +\frac{q-p}{6\sqrt v}(u^3-3u)
 +O_p((1+|u|^4)/m).                                                   \tag{4}
\]
To check its coefficients, write \(s=l/m=p+\eta\). The logarithm of the exponential factor is \(-mD(s\Vert p)\), where
\[
 D(p+\eta\Vert p)=\frac{\eta^2}{2pq}
                  -\frac{q-p}{6p^2q^2}\eta^3+O_p(\eta^4).
\]
The prefactor contributes
\(-\tfrac12\log(2\pi mpq)-(q-p)\eta/(2pq)+O_p(\eta^2+1/m)\).
Substitution of \(\eta=u\sqrt{pq/m}\) proves (4). The Stirling remainder is \(O_p(1/m)\), since \(s\) stays in a compact subinterval of \((0,1)\).

Exponentiating (4), with its cubic term tending uniformly to zero on this range, yields
\[
 \Pr(B_m=l)=d\phi(u)\left[1+\frac{q-p}{6\sqrt v}(u^3-3u)
                    +O_p((1+|u|^6)/m)\right].                        \tag{5}
\]
The sum of its error terms is \(O_p((\log m)^3/m)\): the Gaussian lattice sum \(d\sum_l\phi((l-mp)d)\) is bounded, and \(1+|u|^6=O((\log m)^3)\) on the range.

The omitted tails are negligible. For completeness, exponential Markov applied to \((q+pe^t)^m\), minimized over \(t\), gives
\(\Pr(B_m\geq ms)\leq e^{-mD(s\Vert p)}\) for \(s>p\), and the corresponding lower-tail inequality for \(s<p\). At standardized distance \(\sqrt{48\log m}\), the entropy expansion just displayed gives \(mD\geq 16\log m\) for all sufficiently large \(m\). Tail probabilities are therefore \(O(m^{-16})\). Gaussian tails and their polynomial multiples at that distance are negligible as well.

The elementary trapezoidal estimate for a smooth integrable function \(f\) with integrable first two derivatives is
\[
 d\sum_{l\leq\lfloor r\rfloor}f((l-mp)d)
 =\int_{-\infty}^{z}f(u)\,du
   +d(1/2-\{r\})f(z)+O_f(d^2).                                      \tag{6}
\]
Indeed, apply the trapezoidal rule on each full grid interval ending at \((\lfloor r\rfloor-mp)d\). Its total error is at most a constant times \(d^2\int|f''|\). The last interval from that endpoint to \(z\) has length \(d\{r\}\); Taylor's formula changes its integral to \(d\{r\}f(z)+O(d^2\sup|f'|)\), proving (6).

Apply (6) to \(f=\phi\) and, in the correction term, to \(f(u)=(u^3-3u)\phi(u)\). The latter has integral \((1-z^2)\phi(z)\). Summing (5) proves (3) for thresholds inside the indicated range. For thresholds outside it, the tail bound proves (3) directly; \(z^2\phi(z)\) is negligible there. This also proves the asserted uniformity, rather than only a central expansion.

## 2. Conditioning on the number of midpoint summands

Put \(T_n=\sum_i Z_{n,i}\) and \(J_n=\#\{i:Z_{n,i}=1\}\). Then
\[
 J_n\sim\operatorname{Bin}(n,\lambda/n),\qquad
 (T_n\mid J_n=j)\ \stackrel{d}=\ j+2B_{n-j}.                          \tag{7}
\]
The binomial variables on the right have parameter \(p\). With \(a=q-p\) and \(\epsilon=\lambda/n\), direct computation gives
\[
 \mu_n=2p+a\epsilon,\qquad
 \sigma_n^2=4pq+(a^2-4pq)\epsilon-a^2\epsilon^2.                       \tag{8}
\]
For an integer \(k\), put \(z=(k-n\mu_n)/(\sigma_n\sqrt n)\). The conditional argument in (3) is
\[
 z_j=\frac{(k-j)/2-(n-j)p}{\sqrt{(n-j)pq}}
     =\frac{\sigma_n\sqrt n\,z+a(\lambda-j)}{2\sqrt{(n-j)pq}}.
\]
Uniformly for \(j\leq M_n:=\lceil10\log n\rceil\) and \(|z|\leq\sqrt{12\log n}\), (8) implies
\[
 z_j=z+\frac{a(\lambda-j)}{2\sqrt{npq}}
          +O_{p,\lambda}((\log n)^2/n).                              \tag{9}
\]
This error order is deliberately larger than necessary.

Terms with \(J_n>M_n\) can be discarded at any of the error orders in use. Indeed,
\[
 E e^{2J_n}=\left(1+\frac\lambda n(e^2-1)\right)^n
       \leq e^{\lambda(e^2-1)},\quad
 \Pr(J_n>M_n)\leq e^{\lambda(e^2-1)}n^{-20}.                          \tag{10}
\]
The same exponential-moment argument bounds the discarded first and second moments by a polynomial in \(n\) times \(n^{-20}\); that suffices below. When \(\lambda=0\), \(J_n=0\) identically.

Taylor expansion of \(\Phi(z_j)\), using the boundedness of \(\phi'\), gives
\[
 E\Phi(z_{J_n})=\Phi(z)+O_{p,\lambda}((\log n)^2/n),                  \tag{11}
\]
because the first-order term in (9) has expectation proportional to \(E(\lambda-J_n)=0\). In (11), expectations over the exceptional set in (10) are interpreted by discarding it first. The equality of the truncated and full first moments has negligible error. All smooth coefficient functions in (3) can likewise be replaced by their values at \(z\), at a cost \(O_{p,\lambda}((\log n)^4/n)\). Their derivatives are bounded, \(1/\sqrt{n-j}=1/\sqrt n+O(M_n/n^{3/2})\), and (9) gives the required error.

The fractional part in (3) is essential:
\[
 \frac12-\left\{\frac{k-j}{2}\right\}
       =\frac12\,\mathbf1_{\{j\equiv k\pmod2\}}.
\]
Write
\[
 A_n=E(-1)^{J_n}=(1-2\lambda/n)^n\longrightarrow A=e^{-2\lambda}.
\]
Thus \(\Pr(J_n\equiv k\pmod2)=(1+(-1)^k A_n)/2\). Substitution into (3), (7), and (11) proves
\[
 \Pr(T_n\leq k)-\Phi(z)
 =\frac{\phi(z)}{\sqrt{npq}}
  \left[\frac a6(1-z^2)+\frac{1+(-1)^k A_n}{4}\right]
  +o(n^{-1/2}),                                                       \tag{12}
\]
uniformly for integer \(k\) in the central range. The remainder can be bounded by \(O_{p,\lambda}((\log n)^4/n)\).

This expansion is uniform over *all* integer \(k\). Outside the central range, (9) at its boundary gives conditional standardized distances at least \(\sqrt{10\log n}\) for all retained \(j\), for sufficiently large \(n\). The entropy bound in Section 1 gives conditional tails at most \(n^{-3}\) there. Monotonicity extends the bound to more distant thresholds. Combine it with (10) and the normal tail bound. Both sides of (12), except its negligible remainder, are then \(o(n^{-1/2})\).

Using (5) conditionally gives, also uniformly in \(k\),
\[
 \Pr(T_n=k)=\frac{\phi(z)}{\sqrt{npq}}
                  \frac{1+(-1)^k A_n}{2}+o(n^{-1/2}).                 \tag{13}
\]
For retained \(j\) of matching parity the local leading term is \(\phi(z)/\sqrt{npq}\); for other \(j\) the mass is zero. Equations (9) and (10) justify the replacements exactly as above. Subtracting (13) from (12) gives
\[
 \Pr(T_n<k)-\Phi(z)
 =\frac{\phi(z)}{\sqrt{npq}}
  \left[\frac a6(1-z^2)-\frac{1+(-1)^k A_n}{4}\right]
  +o(n^{-1/2}).                                                       \tag{14}
\]

## 3. Taking the Kolmogorov supremum

Between consecutive integers the distribution function of \(T_n\) is constant, while the normal distribution function is continuous and increasing. The supremum of their absolute difference is consequently the supremum of the right values and left limits at integers. Equations (12) and (14) include both.

For all real \(z\),
\[
 \phi(z)\leq\phi(0),\qquad |1-z^2|\phi(z)\leq\phi(0).               \tag{15}
\]
For the second inequality, put \(y=z^2\). On \([0,1]\), \((1-y)e^{-y/2}\leq1\). On \([1,\infty)\), \((y-1)e^{-y/2}\) has maximum \(2e^{-3/2}<1\), at \(y=3\).

For sufficiently large \(n\), \(A_n\geq0\). Equations (12)–(15) show
\[
 \limsup_n\sqrt n\,\Delta_n
 \leq\frac{\phi(0)}{\sqrt{pq}}\left(\frac{|a|}{6}+\frac{1+A}{4}\right).
\]
For the reverse inequality, choose an even integer \(k_n\) nearest to \(n\mu_n\); its distance from \(n\mu_n\) is at most 1, so \(z_n\to0\). If \(a\geq0\), use the right value (12); if \(a<0\), use the left limit (14). These have absolute limiting coefficients \(|a|/6+(1+A)/4\). This proves equality in the preceding bound, including \(p=1/2\) and \(\lambda=0\).

Finally, the limiting centered third absolute moment of \(Z_{n,1}\) is
\[
 q(2p)^3+p(2q)^3=8pq(p^2+q^2),
\]
and \(\sigma_n^3\to8(pq)^{3/2}\). Hence
\(\rho_n\to(p^2+q^2)/\sqrt{pq}\), proving (1).

## 4. Optimization and consequences

Set \(t=|1-2p|\in[0,1)\), so that \(p^2+q^2=(1+t^2)/2\). Equation (1) becomes
\[
 R(p,\lambda)=\frac{2t+B}{6\sqrt{2\pi}(1+t^2)},\qquad
 B=3(1+e^{-2\lambda}).
\]
Its derivative has the sign of \(1-t^2-Bt\), which has exactly one zero in \((0,1)\):
\(t_*=(\sqrt{B^2+4}-B)/2\). Substituting \(t_*^2+Bt_*=1\) gives (2).

An independent algebraic check of the maximum avoids differentiation. Put
\(M=(B+\sqrt{B^2+4})/2\). Then \(M^2-BM=1\), and
\[
 M(1+t^2)-(B+2t)=M(t-1/M)^2\geq0.
\]
Equality occurs at \(t=1/M=t_*\), verifying the same maximum.

The function \(B\mapsto B+\sqrt{B^2+4}\) is strictly increasing. Since \(B(0)=6\) and \(B(\lambda)<6\) for \(\lambda>0\), (2) gives the asserted strict deficit. At \(\lambda=0\), \(p_*=(4-\sqrt{10})/2\) or its reflection, and the value is Esseen's constant.

The parity identity has a further interpretation: to first order, the contamination reduces the lattice contribution by the factor \((1+e^{-2\lambda})/2\), while the skewness contribution is unchanged. In this family, fixed positive \(n\) times midpoint mass excludes asymptotic attainment of \(C_E\), even after optimizing the fixed Bernoulli parameter. As \(\lambda\to\infty\) *after* taking the limit in \(n\), (2) tends to \((3+\sqrt{13})/(12\sqrt{2\pi})\). No statement uniform in unbounded \(\lambda\), in \(p\to0,1\), or over other contaminating locations is implied.

## 5. A compact-parameter stability consequence

Fix \(0<\delta<1/2\) and \(L<\infty\). Allow the parameters to vary with the row, with \(p_n\in[\delta,1-\delta]\), \(0\leq\lambda_n\leq L\), and midpoint probability \(\lambda_n/n\). Then
\[
 \frac{\sqrt n\,\Delta_n}{\rho_n}
       -R(p_n,\lambda_n)\longrightarrow0.                             \tag{16}
\]
To check uniformity, the derivatives in the entropy expansion and the Stirling remainders in Section 1 are bounded uniformly for \(p\in[\delta,1-\delta]\). The Gaussian integral estimates are independent of \(p\). In (10), replace its constant by \(\exp(L(e^2-1))\). The variance is bounded away from zero for large \(n\), uniformly in these parameters. All Taylor estimates in (9)–(14) therefore have uniform constants. The upper bound in Section 3 is uniform. For the lower bound, the nearest even integer remains within 1 of the mean uniformly, so its standardized distance is \(O_\delta(n^{-1/2})\). Finally,
\((1-2\lambda/n)^n=e^{-2\lambda}+O_L(n^{-1})\) uniformly on \([0,L]\), by expanding \(n\log(1-2\lambda/n)\). The third absolute moment and variance in (8) converge uniformly on the compact parameter set, proving (16). In fact the argument bounds the difference by \(O_{\delta,L}((\log n)^4/\sqrt n)\); no numerical constant for this remainder is asserted.

Consequently, if this family's normalized error tends to \(C_E\), then
\[
 \lambda_n\longrightarrow0,\qquad
 \operatorname{dist}\left(p_n,\left\{(4-\sqrt{10})/2,(\sqrt{10}-2)/2\right\}\right)
       \longrightarrow0.                                             \tag{17}
\]
Indeed, from any subsequence choose a further subsequence on which \((p_n,\lambda_n)\) converges. Equation (16) and continuity give \(R(p,\lambda)=C_E\) at its limit. Equation (2), its strict decrease for positive \(\lambda\), and its unique maximizing \(t\) imply \(\lambda=0\) and the two stated choices of \(p\). Compactness now forces (17) for the full sequence. The two displayed \(p\)'s are reflections and sum to 1. If the chosen interval excludes them, asymptotic attainment is impossible.
