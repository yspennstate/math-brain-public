# Positive-level restricted weak-L² for the near-hub form

**Scope.** This proves the proposed restricted weak-L² estimate at every nonnegative target, even when the light triple is dependent. Negative targets and the general quadratic-form density conjecture remain open. This note strengthens the positive-level density theorem and audits its coarea identity.

Let \(Y=(L,V,P)\) have a joint density on \(\mathbb R^3\), and suppose every normalized two-dimensional orthogonal projection of \(Y\) has density at most \(K_2\). For \(\beta,\varepsilon\in\mathbb R\), \(s\geq0\), \(0<\rho\leq1/2\), and measurable \(E\subset\mathbb R\) of finite length, put
\[
 T_s(l,v,p)=\frac{s-v^2-\beta l^2}{2l}-\varepsilon p,\qquad
 \mu_{\rho,s}(E)=\mathbb E\!\left[
 \frac{\mathbf 1_{\{\rho\leq|L|\leq2\rho\}}}{2|L|}
 \mathbf 1_E(T_s(L,V,P))\right].
\]

## Theorem

Uniformly in \(s\geq0,\rho,\beta,\varepsilon,E\),
\[
 \boxed{\mu_{\rho,s}(E)\leq 4\sqrt2\,K_2\sqrt{\rho\,|E|}.}
\]
No one-dimensional projection cap, independence within \(Y\), support bound, or regularity of the original-coordinate densities is required. In particular this holds for every orthonormal three-frame projection \(Y=U^TX\) of independent cap-one coordinates, where the standard projection theorem gives \(K_2\leq2\).

## Proof

Write \(R=\sqrt s\). For each real \(t\), define the linear forms
\[
 c_t=(t^2+\beta)/2,\quad W_t=V-tL,\quad U_t=c_tL+\varepsilon P.
\]
Restrict the law of \(Y\) to the shell \(\rho\leq|L|\leq2\rho\). Write \(f_t^{\rm sh}(w,u)\) for the resulting (subprobability) joint density of \((W_t,U_t)\), whenever the two forms are independent. The substitution \(V=R+tL\), whose Jacobian is \(|L|\), gives the coarea identity
\[
 \mu_{\rho,s}(E)
 =\frac12\int_{\mathbb R}\!\int_{\mathbb R}
 f_t^{\rm sh}(R,u)\,\mathbf 1_E(-Rt-u)\,du\,dt. \tag{1}
\]
It holds initially as an identity of measures in the target \(R\), hence for almost every \(s>0\). The final paragraph below upgrades the bound on \(\mu_{\rho,s}(E)\) to every \(s\geq0\). The exceptional \(t\) at which \((W_t,U_t)\) is rank deficient have zero Lebesgue measure.

The rows of the map \(Y\mapsto(L,W_t)\) are \((1,0,0)\) and \((-t,1,0)\), with exterior-product norm exactly one. Its joint density is therefore at most \(K_2\). The two shell intervals have combined \(l\)-length \(2\rho\), so
\[
 \int_{\mathbb R} f_t^{\rm sh}(R,u)\,du
 =f_{W_t}^{\rm sh}(R)\leq 2\rho K_2. \tag{2}
\]
The rows of \(Y\mapsto(W_t,U_t)\) are \((-t,1,0)\) and \((c_t,0,\varepsilon)\). Their exterior-product norm is
\[
 \Delta_t=\sqrt{c_t^2+\varepsilon^2(1+t^2)}
 \geq |t^2+\beta|/2.
\]
Restriction to the shell cannot increase a projected density, so
\[
 f_t^{\rm sh}(R,u)\leq K_2/\Delta_t
 \leq \frac{2K_2}{|t^2+\beta|}. \tag{3}
\]
Equations (1)–(3) imply
\[
 \mu_{\rho,s}(E)\leq
 K_2\int_{\mathbb R}
 \min\!\left\{\rho,\frac{|E|}{|t^2+\beta|}\right\}dt. \tag{4}
\]

For every real \(\beta\) and \(D>0\), the quadratic sublevel set obeys
\[
 \left|\{t:|t^2+\beta|\leq D\}\right|\leq2\sqrt{2D}. \tag{5}
\]
Indeed, for \(\beta\geq0\) its length is at most \(2\sqrt D\). For \(\beta=-a<0\), its length is \(2(\sqrt{a+D}-\sqrt{(a-D)_+})\), at most \(2\sqrt{2D}\) by the one-half Hölder continuity of the square root. Layer cake and (5) yield, for \(A,B>0\),
\[
 \int_{\mathbb R}\min\!\left\{A,\frac{B}{|t^2+\beta|}\right\}dt
 =\int_0^A\left|\left\{t:|t^2+\beta|<B/u\right\}\right|du
 \leq 4\sqrt2\sqrt{AB}. \tag{6}
\]
Putting \(A=\rho,B=|E|\) in (4) proves the claim for almost every \(s>0\), for each fixed \(E\). To obtain the advertised pointwise statement, first take \(E\) open. Since \(T_s(l,v,p)\) depends continuously on \(s\) whenever \(l\ne0\), Fatou's lemma shows that \(s\mapsto\mu_{\rho,s}(E)\) is lower semicontinuous. An almost-everywhere upper bound for a lower-semicontinuous function holds everywhere, including at the boundary \(s=0\) by right continuity of the domain. For a general measurable \(E\), choose open supersets \(O\supset E\) with \(|O|\downarrow|E|\) and use monotonicity of \(\mu\). This also proves the case \(|E|=0\).

## Audit and boundary

The earlier positive-level coarea theorem, [positive-level projection receiver](https://github.com/yspennstate/math-open-problems/blob/2e173282f01a69daef5a66b21138b3853477ab98/proofnet24/QFORM-density/interactive/20260923T203400Z-positive-level-projection-receiver/REPORT.md), has the correct identity, Jacobian, exterior-product factor, and uniform integral bounds. The shell restriction above replaces its one-dimensional cap with the planar cap of \((L,W_t)\), and produces the required factor \(\sqrt\rho\).

For negative \(s\), the substitution \(V=\sqrt s+tL\) has no real meaning. Using \(V=tL\) instead leaves \(s/(2L)\) in the second coarea coordinate; it is nonlinear, and (3) no longer follows from a linear projection cap. Thus the theorem is a positive-level special case of the proposed [restricted weak-L² target](https://github.com/yspennstate/math-open-problems/blob/62f9d598de628104d39ed19a9851b60f6eccded5/proofnet24/QFORM-density/interactive/20260923T204500Z-restricted-weak-l2-hub-target/REPORT.md), not a proof at negative levels.