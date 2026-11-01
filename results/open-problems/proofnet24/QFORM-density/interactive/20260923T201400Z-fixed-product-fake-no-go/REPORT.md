# Fixed-product exclusion of the independent-hub leakage shell

**Status:** proved local bound for each fixed full-rank product projection; **no dimension-uniform QFORM bound**. This excludes exact realization of the dependent-light shell in [the earlier projection-only falsifier](https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T192452Z-independent-hub-all-projections-fake/REPORT.md). It is not a counterexample to the original conjecture.

## Statement

Let \(X_1,\ldots,X_n\) be independent real random variables with probability densities bounded by one. Let \(H\), also of density at most one, be independent of all \(X_i\). Write
\[
 (L,V,P)^T=U X,\qquad U\in\mathbb R^{3\times n},\qquad \operatorname{rank}U=3.
\]
Select three physical columns \(S\) for which \(M=U_S\) is invertible, and put \(\kappa=s_{\min}(M)>0\). For every real \(\varepsilon\), define
\[
 Q=2HL+V^2+2\varepsilon LP.
\]
For almost every \(x\in[-3/2,-1/2]\), its density satisfies
\[
 p_Q(x)\le \frac12+\frac{48\sqrt3}{\kappa}.                    \tag{1}
\]
The same proof gives \(p_Q(x)\le 1/2+24\sqrt3/(\kappa\sigma)\) on \(x\le-\sigma<0\). The estimate is independent of supports, moments, dimension outside the chosen minor, and \(\varepsilon\). Its dependence on \(\kappa\) is essential to its scope.

In particular, the earlier dependent-light law \(g(l,v,p)\) cannot equal the law of \(UX\) for any fixed full-rank \(U\) and independent cap-one inputs. This conclusion applies even without the orthonormal-row requirement. It therefore applies to every fixed orthonormal three-projection of independent original coordinates.

## Product curved-tube estimate

Fix \(x\in[-3/2,-1/2]\), write \(\gamma=-x\ge1/2\), and put
\[
 F_x(l,v,p)=\varepsilon p+\frac{\gamma+v^2}{2l}
 \quad(l\ne0).
\]
For \(0<r<1\) and any interval \(I\subset\mathbb R\),
\[
 \Pr\{r\le |L|\le2r,\ F_x(L,V,P)\in I\}
 \le \frac{96\sqrt3}{\kappa}|I|r^2.                          \tag{2}
\]

To prove (2), condition on all physical inputs outside \(S\). The remaining map from three independent cap-one inputs \(x_S\) to \((l,v,p)\) is affine with linear part \(M\). On \(r\le |l|\le2r\),
\[
 |\partial_lF_x|=\frac{\gamma+v^2}{2l^2}
 \ge \frac1{16r^2}.
\]
Thus
\[
 \|\nabla_{x_S}F_x\|_2
 =\|M^T\nabla_{(l,v,p)}F_x\|_2
 \ge\frac{\kappa}{16r^2}.
\]
At every point at least one of the three physical partial derivatives has magnitude at least
\(D=\kappa/(16\sqrt3\,r^2)\). Partition the tube event according to such a coordinate.

Fix the other two inputs in one part. Along the selected input line, each level equation \(F_x=y\), after multiplying by \(2l\), is
\[
 2l(\varepsilon p-y)+\gamma+v^2=0.                           \tag{3}
\]
Here \(l,v,p\) are affine in the free input, so (3) is a polynomial of degree at most two. Except for levels on which \(F_x\) is constant, it has at most two solutions. Constant levels have zero selected derivative and cannot occur in the derivative-gated part. The one-dimensional area formula therefore bounds the length of that part by \(2|I|/D\). Its probability has the same bound because the free input density is at most one. Integrating the other two input laws, then summing the three derivative choices, gives
\[
 3\frac{2|I|}{D}
 =\frac{96\sqrt3}{\kappa}|I|r^2.
\]
The estimate is uniform in the conditioned translations, so averaging over the remaining inputs proves (2). The argument works for arbitrarily fragmented supports.

## Density bound

Since \(H\) is independent of the light variables, conditioning on them and inverting the affine map in \(H\) gives the density version
\[
 p_Q(x)=
 \mathbb E\!\left[
 \frac{f_H(-F_x(L,V,P))}{2|L|}
 \right]                                                     \tag{4}
\]
for almost every \(x\), with the \(L=0\) null set omitted. The part \(|L|\ge1\) is at most \(1/2\) because \(f_H\le1\).

Let \(\nu_r\) be the unnormalized pushforward law of \(F_x(L,V,P)\) on \(r\le|L|\le2r\). Inequality (2) for all intervals implies \(\nu_r\) has a density bounded by \(96\sqrt3 r^2/\kappa\). Hence, using \(\int f_H=1\),
\[
 \mathbb E[
 1_{\{r\le|L|\le2r\}}f_H(-F_x(L,V,P))]
 \le \frac{96\sqrt3}{\kappa}r^2.                             \tag{5}
\]
The factor \(1/(2|L|)\) in (4) is at most \(1/(2r)\) on this shell. Sum (5) over \(r_j=2^{-j-1}\), \(j\ge0\), for which \(\sum_jr_j=1\). This proves (1).

For \(x\le-\sigma\), the lower derivative bound is \(\sigma/(8r^2)\), and the same calculation gives the stated \(24\sqrt3/(\kappa\sigma)\) term.

## Exact exclusion of the fake shell

In the earlier construction, \(f_H=\sum_k1_{I_k}\) with \(|I_k|=a_k\to0\). Its \(k\)-th matched light shell contributes the continuous density
\[
 p_k(-1)=\frac{a_k}{1024}\log\frac1{a_k}                     \tag{6}
\]
and, in fact, remains close to this value on an interval about \(-1\). That shell has \(0<|L|<1\).

If its light law were \(UX\) as above, the part of (4) from \(H\in I_k\) and \(0<|L|<1\) would be at most \(48\sqrt3\,a_k/\kappa\): in (5) replace \(f_H\) by \(1_{I_k}\), whose integral is \(a_k\). This would force
\[
 \log(1/a_k)\le\frac{49152\sqrt3}{\kappa}                    \tag{7}
\]
for every \(k\), contradicting \(a_k\to0\). Equivalently, the full fake law has unbounded essential density near \(-1\), contradicting the finite local bound (1). Thus no fixed full-rank product projection realizes this particular dependent light law. This does not exclude other product-law mechanisms.

## Aggregation across repeated physical directions

There is a dimension-free extension when the physical light frame has a bounded number of **exact** line directions. Suppose the columns of the Parseval frame \(U\), with \(UU^T=I_3\), lie on at most \(d\) lines through the origin. Partition the original inputs by line. For each nonempty bank, its contribution to \((L,V,P)\) is one scalar sum \(S_b\) times a fixed unit direction. The banks are independent. Normalize each scalar sum by the Euclidean norm of its coefficient vector; the one-dimensional product-projection theorem bounds its density by \(\sqrt e\). The resulting three-by-\(d\) effective coefficient matrix is still Parseval.

The area-formula proof above works for independent inputs of density at most \(\sqrt e\), at a factor \(\sqrt e\) cost. Cauchy–Binet on the effective \(d\)-column frame supplies a three-column minor of smallest singular value at least \(\binom d3^{-1/2}\). Therefore
\[
 p_Q(x)\le\frac12+48\sqrt{3e}\sqrt{\binom d3}
 \qquad(-3/2\le x\le-1/2).                                  \tag{8}
\]
The bound does not depend on the number of original physical coordinates in those banks. For exactly three line directions the effective matrix is orthogonal, giving \(1/2+48\sqrt{3e}\).

This requires exact collinearity within each bank. With approximate directions and unbounded fragmented original supports, the residual projections cannot be discarded as small random perturbations. The general diffuse-frame case remains open.

## Quantitative limitation

If \(UU^T=I_3\), Cauchy–Binet gives
\[
 \sum_{|S|=3}\det(U_S)^2=1.
\]
Some minor therefore has \(|\det U_S|\ge\binom n3^{-1/2}\). Each singular value of \(U_S\) is at most one, so its smallest singular value obeys
\(\kappa\ge|\det U_S|\ge\binom n3^{-1/2}\). Formula (1) consequently gives the explicit but dimension-dependent bound
\[
 p_Q(x)\le \frac12+48\sqrt3\sqrt{\binom n3}
 \quad(-3/2\le x\le-1/2).                                   \tag{9}
\]
Diffuse frames make every individual physical minor small. Removing this loss requires using aggregate product structure across many coordinates. The present result neither closes that step nor handles an additional \(\beta L^2\) term, other spectral branches, or all output levels. The universal QFORM bounded-density conjecture remains **OPEN**.

The physical-minor area-formula method is related to the benchmark in [the curved dyadic product-tube note](https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T202000Z-curved-dyadic-product-tube/REPORT.md). The contribution here is its favorable-sign local density consequence and the direct exclusion of the independent-hub fake shell.
