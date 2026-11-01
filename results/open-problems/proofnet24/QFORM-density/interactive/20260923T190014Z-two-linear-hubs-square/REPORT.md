# Two original linear hubs plus a transverse square

**Status:** proved sufficient theorem. The two hubs have no quadratic self-block. The light triple may have an arbitrary dependent joint law with a bounded density. This does not settle a nonzero quadratic form in the hubs or the one-hub leakage endpoint.

## Theorem

Let \(H_1,H_2\) be independent real random variables, each with probability density at most one, and let \(Z=(Y_1,Y_2,V)\) be independent of \(H=(H_1,H_2)\). The three coordinates of \(Z\) may be arbitrarily dependent, but suppose their joint probability density \(g\) is bounded by \(M<\infty\). For any \(\lambda\ne0\) and finite real measurable functions \(F,G\) of \(y=(y_1,y_2)\), put
\[
 Q=2H_1Y_1+2H_2Y_2+\lambda V^2+2VG(Y)+F(Y).
\]
Then \(Q\) has a bounded density and
\[
 \boxed{\displaystyle
 \|p_Q\|_\infty
 \le {5\over6}\left({16\sqrt2\,M\over\sqrt{|\lambda|}}\right)^{2/5}.
 }                                                        \tag{1}
\]
The bound is uniform in \(F,G\), in the marginal laws of the hubs, in the dependence inside \(Z\), and in the locations and tails of the variables.

If \(Z=TX'\) is a rank-three linear image of an independent cap-one product vector, the standard bounded-projection estimate
\[
 M\le {2^{3/2}\over\sqrt{\det(TT^{\mathsf T})}}
\]
gives
\[
 \|p_Q\|_\infty
 \le {5\over6}
 \left({64\over
 \sqrt{|\lambda|\det(TT^{\mathsf T})}}\right)^{2/5}.
                                                               \tag{2}
\]
For an orthonormal three-row projection and \(|\lambda|\ge1\), this is less than \(4.40\).

## Proof

Complete the square in \(V\), replacing it by \(V'=V+G(Y)/\lambda\). The shear \((y,v)\mapsto(y,v+G(y)/\lambda)\) has Jacobian one, so the joint density of \((Y,V')\) is still at most \(M\). Replace \(F\) by \(F-G^2/\lambda\). It therefore suffices to bound the form
\[
 Q=2H\cdot Y+\lambda V^2+F(Y).
\]

For \(y\ne0\), let \(k_y\) be the density of \(R_y=2H\cdot y\). Conditioning on whichever hub has the larger coefficient and convolving with the law of the other gives
\[
 \|k_y\|_\infty\le m(y):={1\over2\|y\|_\infty},
 \qquad \int_{\mathbb R}k_y(r)\,dr=1.                 \tag{3}
\]
For a fixed output level \(s\), the density kernel conditional on \(Z=(y,v)\) is
\[
 K_s(y,v)=k_y\!\left(s-F(y)-\lambda v^2\right).
\]
It obeys the pointwise cap \(K_s(y,v)\le m(y)\). Changing variables separately on the two branches of the square gives, for either sign of \(\lambda\),
\[
 \int_{\mathbb R}K_s(y,v)\,dv
 ={1\over\sqrt{|\lambda|}}
 \int_{\operatorname{sgn}(\lambda)(s-F(y)-r)>0}
 {k_y(r)\over\sqrt{|s-F(y)-r|}}\,dr
 \le 2\sqrt{m(y)/|\lambda|}.                          \tag{4}
\]
For the last inequality, among nonnegative densities bounded by \(m\) and of mass one, the one-sided decreasing kernel \(u^{-1/2}\) has largest integral when the density equals \(m\) on \(0<u<1/m\); that integral is \(2\sqrt m\).

Fix \(T>0\). On \(\|y\|_\infty\ge T\), use (3) and total mass one of \(g\), obtaining a contribution at most \(1/(2T)\). On \(\|y\|_\infty<T\), use \(g\le M\) and (4). Since the square \([-r,r]^2\) has area \(4r^2\),
\[
 \begin{aligned}
 \int_{\|y\|_\infty<T}\int_{\mathbb R}
      g(y,v)K_s(y,v)\,dv\,dy
 &\le {\sqrt2\,M\over\sqrt{|\lambda|}}
       \int_{[-T,T]^2}\|y\|_\infty^{-1/2}\,dy\\
 &= {16\sqrt2\,M\over3\sqrt{|\lambda|}}\,T^{3/2}.
 \end{aligned}                                            \tag{5}
\]
Thus
\[
 p_Q(s)\le {1\over2T}
      +{16\sqrt2\,M\over3\sqrt{|\lambda|}}\,T^{3/2}.
\]
The choice
\(T=(\sqrt{|\lambda|}/(16\sqrt2 M))^{2/5}\)
makes the right side equal to (1), independently of \(s\). The conditional densities and the finite bound construct an absolutely continuous output law. Formula (2) follows from the three-dimensional projection density bound. \(\square\)

## Boundary of the theorem

The proof uses the independent *linear* hubs in (3). If a term \(H^{\mathsf T}BH\) is added, the conditional density \(k_y\) may have a square-root or logarithmic singularity, and (3) fails. Formula (1) does not cover that term. Allowing an arbitrary nonlinear \(F(Y,V)\) would also permit cancellation of the displayed square and is not asserted.

For comparison, the earlier linear two-hub estimate bounds \(2H\cdot Y+R(Y,V)\) by \(2\sqrt{\|p_Y\|_\infty}\) when the two-dimensional marginal of \(Y\) is bounded. A three-dimensional joint cap \(g\le M\) does not imply a uniform bound on \(\|p_Y\|_\infty\), since \(V\) may have arbitrarily long support. The present square receiver pays this missing marginal bound.
