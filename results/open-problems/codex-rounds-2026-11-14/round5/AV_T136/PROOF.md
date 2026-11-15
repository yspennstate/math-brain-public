# Low-cut scalar source moments

The following lemma verifies the local scalar input (E7)–(E9) in Section 9 of OpenAI, *The low-temperature Sherrington–Kirkpatrick free-energy limiting law* (September 24, 2026). It is conditional on the regular scalar PDE and diffusion specified below. It does not establish the signed compression identity (E5), the spin-overlap estimates, or the stopped pressure-increment proposition.

## Statement and hypotheses

Let \(k(u)>0\) be smooth near zero, and let \(G(u,z)\) be an even smooth solution of
\[
 G_u=-\frac{k(u)}2\bigl(G_{zz}+uG_z^2\bigr).
 \tag{1}
\]
Write \(M=G_z\), \(A=G_{zz}\), \(B=G_{zzz}\), and
\[
 \chi=A(0,0),\qquad g=G_{zzzz}(0,0),\qquad k_0=k(0).
\]
Assume \(k\) is bounded above and away from zero, the needed derivatives through at least spatial order eight and time order three have uniform polynomial bounds, and \(M\) is globally Lipschitz in \(z\). These sufficient regularity hypotheses are imposed on a fixed small interval. For the inverse-jet size monomials in Section 5 assume also \(\chi>0\). Constants below can depend on these bounds. The source asserts the needed regularity for its scalar construction; its global construction is a separate input here.

The scalar positive diffusion is
\[
 d\zeta_u=\sqrt{k(u)}\,dW_u+u k(u)M(u,\zeta_u)\,du,\qquad \zeta_0=0.
 \tag{2}
\]
Copies share their Brownian motion until the prescribed split and use independent Brownian motions afterwards. Fix a cut \(c>0\), with all splits in \([0,c]\), and define
\[
 P^c(u,z)=A(u,z)+cM(u,z)^2.
\]
At the cut write \(M_A=M(c,\zeta_c^A)\), \(P_A=P^c(c,\zeta_c^A)\). For two branches splitting at \(v\),
\[
 \mathbb E[M_A M_B]=\chi^2k_0v+O(v^2),                                      \tag{3}
\]
\[
 \mathbb E[P_A P_B]
 =\chi^2+\chi^3k_0c^2+\frac12g^2k_0^2v^2+O(c^3).                           \tag{4}
\]
For three branches,
\[
 \mathbb E[P_A M_B M_C]=\chi^3k_0v_{BC}+O(c^2).                             \tag{5}
\]
If the designated splits satisfy \(v_{AB}=h<v_{AC}\), then \(v_{BC}=h\), and the sharper statement is
\[
 \mathbb E[P_A M_B M_C]=\chi^3k_0h+O(ch).                                   \tag{6}
\]
The other ordering follows by exchanging \(B,C\). The constants in (4)–(6) are uniform as \(v/c\) or \(h/c\) tends to zero. In particular the error in (6) vanishes at \(h=0\).

The source functions \(s_j=c^{-1}e^{-cG}\partial_z^j e^{cG}\) satisfy
\[
 s_1=M,\quad s_2=P^c,\quad
 s_3=B+3cMA+c^2M^3,
\]
\[
 s_4=G_{zzzz}+4cMB+3cA^2+6c^2M^2A+c^3M^4.                                \tag{7}
\]
Consequently, in every fixed \(L^p\) at the cut,
\[
 s_1=\chi\zeta_c+O(c^{3/2}),\quad s_2=\chi+O(c),\quad
 s_3=g\zeta_c+O(c^{3/2}),\quad s_4=g+O(c).                                  \tag{8}
\]

## 1. Moment bounds and generator identities

Oddness gives \(M(u,0)=B(u,0)=0\). The Lipschitz bound and Gronwall applied to (2), with Gaussian moment bounds for its deterministic diffusion coefficient, give
\[
 \|\zeta_u\|_p\le C_p\sqrt u.
\]
Since \(\sqrt{k(u)}-\sqrt{k_0}=O(u)\), the difference of the Gaussian stochastic integrals has \(L^p\) norm \(O(u^{3/2})\). The drift has norm bounded by
\(C_p\int_0^u r\sqrt r\,dr=O(u^{5/2})\). Thus
\[
 \|\zeta_u-\sqrt{k_0}W_u\|_p=O(u^{3/2}),\qquad
 \mathbb E\zeta_u^2=k_0u+O(u^2).                                          \tag{9}
\]
Taylor expansion, evenness, and the derivative bounds give
\[
 M(u,\zeta_u)=\chi\zeta_u+O_{L^p}(u^{3/2}),\quad
 A(u,\zeta_u)=\chi+O_{L^p}(u),\quad
 B(u,\zeta_u)=g\zeta_u+O_{L^p}(u^{3/2}).                                  \tag{10}
\]
Here and below products are estimated by Hölder at higher fixed orders. Equations (7) and (10) prove (8).

The space-time generator along (2) is
\[
 \mathcal D=\partial_u+\frac{k(u)}2\partial_{zz}+uk(u)M\partial_z.
\]
Differentiating (1) in \(z\) once and twice gives the exact cancellations
\[
 \mathcal D M=0,\qquad \mathcal D A=-ukA^2,\qquad
 \mathcal D(M^2)=kA^2.
\]
Therefore
\[
 dP^c(u,\zeta_u)
 =(c-u)k(u)A(u,\zeta_u)^2\,du
 +\sqrt{k(u)}\,[B+2cMA](u,\zeta_u)\,dW_u.                                 \tag{11}
\]
All martingales here are integrable under the moment hypotheses. Standard stopping on bounded fields, followed by the polynomial bounds, justifies Itô and removal of the stops.

## 2. The pair expansion by a branching product

The process \(M(u,\zeta_u)\) is a martingale. Conditioning at the split \(v\) and using independent futures yields
\[
 \mathbb E[M_A M_B]=\mathbb E[M(v,\zeta_v)^2].
\]
Equations (9)–(10) prove (3), with an error depending on \(v\), not on the terminal cut.

Run both branches to time \(u\), with their noises identical for \(u<v\). Apply the product formula to their \(P^c\) processes. At time zero both equal \(\chi\). The two drift terms integrate to
\[
 \int_0^c(c-u)k(u)\mathbb E[A_A(u)^2P_B^c(u)+A_B(u)^2P_A^c(u)]\,du.
\]
Uniformly for \(u\le c\), (10) gives the expectation \(2\chi^3+O(c)\) and \(k(u)=k_0+O(c)\). The resulting contribution is
\[
 2\chi^3k_0\int_0^c(c-u)\,du+O(c^3)
 =\chi^3k_0c^2+O(c^3).                                                    \tag{12}
\]
The common quadratic variation ends at \(v\). By (9)–(10), its expected rate is
\[
 k(u)\mathbb E[B(u,\zeta_u)+2cM(u,\zeta_u)A(u,\zeta_u)]^2
 =g^2k_0^2u+O(cu).
\]
Its integral is \(g^2k_0^2v^2/2+O(cv^2)\). Since \(v\le c\), this proves (4), uniformly even for \(v=0\) or \(v=c\).

At \(v=0\) the two branches are independent. Equation (4) then says
\((\mathbb E P_A)^2=\chi^2+\chi^3k_0c^2+O(c^3)\), consistent with (11), whose mean drift gives
\[
 \mathbb E P_A=\chi+\frac12\chi^2k_0c^2+O(c^3).                            \tag{13}
\]

## 3. An independent covariance derivation of the same coefficient

Condition at the split, and set
\(q(v,z)=\mathbb E[P^c(c,\zeta_c)\mid\zeta_v=z]\). Independent futures give
\[
 \mathbb E[P_A P_B]=(\mathbb E P_A)^2+\operatorname{Var}(q(v,\zeta_v)).       \tag{14}
\]
From (1), \(A_u(0,0)=-k_0g/2\). Taylor expansion at \((0,0)\) therefore gives
\[
 A(v,z)=\chi+\frac g2(z^2-k_0v)
       +O((v^2+vz^2+z^4)(1+|z|)^C).
\]
The term \(cM(v,z)^2\) has \(L^2\) norm \(O(cv)\). By (11) the conditional expected future drift has \(L^2\) norm \(O(c^2)\), using conditional Jensen and the uniform moment bounds. Hence
\[
 q(v,\zeta_v)=\chi+\frac g2(\zeta_v^2-k_0v)+R,\qquad \|R\|_2=O(c^2).
\]
By (9), \(\|\zeta_v^2-k_0W_v^2\|_2=O(v^2)\), so the Gaussian fourth moment gives
\[
 \operatorname{Var}(\zeta_v^2)=2k_0^2v^2+O(v^3).
\]
The covariance with \(R\) is \(O(vc^2)\) and its variance is \(O(c^4)\). For \(v\le c\le1\), these are \(O(c^3)\). Substitution in (14), with (13), recovers (4). Thus both the coefficient \(1/2\) and the absence of a term linear in \(c\) are checked independently.

## 4. The earlier-split factor in the triple expansion

The rough estimate follows from
\[
 \|(P_A-\chi)M_BM_C\|_1=O(c^2)
\]
and (3) for \(B,C\), proving (5).

For the sharper estimate, put \(v_{AB}=h<v_{AC}\). Tree consistency gives \(v_{BC}=h\). At time \(h\), branch \(B\) separates from the group containing \(A,C\). Condition on the common value \(z\). Define
\[
 F(z)=\mathbb E[(P_A-\chi)M_C\mid\zeta_h=z].
\]
The \(A,C\) split is fixed at any value in \([h,c]\). Their future law is invariant under simultaneous sign reversal of \(z\) and all Brownian increments. Since \(P-\chi\) is even and \(M\) is odd, \(F\) is odd.

For completeness, derivatives of the additive-noise flow with respect to its starting value solve
\[
 J'_u=uk(u)A(u,\zeta_u)J_u,\qquad J_h=1.
\]
The Lipschitz assumption bounds \(A\), hence \(J_u\) uniformly. Conditional moment estimates give
\(\|\zeta_u\|_p\le C_p(|z|+\sqrt c)\). Taylor bounds yield
\[
 |P^c(u,y)-\chi|\le C(u+y^2+cy^2)(1+|y|)^C,
 \quad |\partial_yP^c(u,y)|\le C|y|(1+|y|)^C,
\]
\[
 |M(u,y)|\le C|y|,\qquad |\partial_yM(u,y)|\le C.
\]
Differentiate \(F\), use these bounds and Hölder, and obtain uniformly in the later split
\[
 |F'(z)|\le C(c+z^2)(1+|z|)^C.
\]
Since \(F(0)=0\), integration from zero gives
\[
 |F(z)|\le C|z|(c+z^2)(1+|z|)^C.                                         \tag{15}
\]
Branch \(B\) has conditional mean \(M(h,z)\), by its martingale property. Conditional independence and (15) imply
\[
 \left|\mathbb E[(P_A-\chi)M_BM_C]\right|
 \le C\mathbb E[\zeta_h^2(c+\zeta_h^2)(1+|\zeta_h|)^C]
 \le C(ch+h^2)\le C'ch.
\]
Finally \(\chi\mathbb E[M_BM_C]=\chi^3k_0h+O(h^2)\) by (3); \(h^2\le ch\) proves (6). At \(h=0\), the \(B\) branch has zero mean and is independent of the others, so both sides are exactly zero. A bound merely \(O(c^2)\) would not supply this endpoint or the required smaller-scale factor.

## 5. Parameter derivatives and size scaling

The moment estimates also hold after one parameter derivative if \(k,G\) and their needed parameter derivatives satisfy the same bounds. This is an additional uniformity hypothesis, not a consequence of smoothness in \(u,z\) alone. With common Brownian drivers, the parameter derivative \(Y=\partial_\theta\zeta\) satisfies
\[
 dY_u=\partial_\theta\sqrt{k(u)}\,dW_u
 +u[(\partial_\theta k)M+k(\partial_\theta M)+kAY_u]\,du.
\]
Evenness gives \(\partial_\theta M(u,0)=0\). Gronwall yields \(\|Y_u\|_p=O(\sqrt u)\); subtracting the derivative of \(\sqrt{k_0}W_u\) gives \(O(u^{3/2})\). Differentiating the identities and estimates above therefore preserves all powers. For (15), differentiate the starting-field flow as well; bounded mixed derivatives give the same estimate for the parameter derivative of \(F'\). This proves the claimed \(O_*\) powers subject to these uniform hypotheses.

The exact PDE rescaling
\[
 G_\ell(u,z)=\ell^{-1}G_{\rm base}(u/\ell,\ell z),\qquad
 k_\ell(u)=\ell^{-3}k_{\rm base}(u/\ell)
\]
preserves (1), as direct substitution shows. Its initial jets have weights
\[
 \chi_\ell=\ell\chi_0,\quad g_\ell=\ell^3g_0,\quad
 k_\ell(0)=\ell^{-3}k_{\rm base}(0),\quad b_\circ=\chi^{-2}\ \text{has weight }-2.
\]
Thus the monomials occurring in the source have the following weights:

| Degree \(j\) | Monomial | Power of \(\ell\) |
| --- | --- | --- |
| 2 | \(b_\circ^2\chi^3k_0\) | \(-4\) |
| 2 | \(b_\circ^2g^2k_0^2\) | \(-4\) |
| 3 | \(b_\circ^3g^2k_0\) | \(-3\) |
| 3 | \(b_\circ^3\chi^3\) | \(-3\) |
| 4 | \(b_\circ^4g^2\) | \(-2\) |

With \(\ell=e^{\theta/6}\), each leading monomial is annihilated by \(1-j/6+\partial_\theta\). This checks the algebraic cancellation in (E6)–(E9). The source's assertion that its smoothed terminal construction differs from this scaling only exponentially in its terminal parameter is not proved here.

## Scope and remaining check

These calculations support the repeated-edge and three-block quadratic cases of the low-degree coefficient estimate, conditional on the signed compression identity and scalar regularity. They verify its covariance coefficient, the crucial earlier-split factor, and the formal size weights. They do not justify factoring internal signed allocations in (E5), projecting the spin tests through a cut, or the centered allocation estimate (E2)–(E3). The next check should derive (E5) directly in a finite hierarchy, including two cumulant parts sharing a cut block and repeated terminal labels.

