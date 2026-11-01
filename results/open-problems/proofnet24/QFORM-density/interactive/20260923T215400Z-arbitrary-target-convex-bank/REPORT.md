# Arbitrary-target convex-bank estimate and a scoped hub theorem

Date: 2026-09-23 UTC.

## 1. A scalar arbitrary-target lemma

Let \(X,Y\) be independent real random variables with densities bounded by \(K_X,K_Y\). Let \(u:\mathbb R\to\mathbb R\) be measurable and let \(v:\mathbb R\to\mathbb R\) be finite convex or finite concave. For every Borel set \(E\) of finite Lebesgue measure \(\delta\),
\[
 \Pr\{2XY+u(X)+v(Y)\in E\}
 \le \min\{1,\,2\sqrt{2K_XK_Y\delta}\}.
 \tag{1}
\]
The target may have arbitrarily many components. Every quadratic \(v(y)=cy^2+dy+e\), including \(c=0\), satisfies the hypothesis, with a constant independent of all three coefficients.

**Proof.** Treat convex \(v\); the concave case reverses the monotonicity. Its right derivative \(w=v'_+\) is monotone and agrees with the derivative almost everywhere. Fix \(r>0\). Conditional on \(Y=y\), the bad derivative condition \(|2X+w(y)|\le r\) confines \(X\) to an interval of length \(r\), so it has probability at most \(K_Xr\). For fixed \(X=x\), each of the regions \(w(y)+2x<-r\) and \(w(y)+2x>r\) is an interval, and on each the function \(y\mapsto2xy+v(y)\) is one-to-one with inverse Lipschitz constant at most \(1/r\). The inverse image of the arbitrary target \(E-u(x)\) has length at most \(\delta/r\) on each region. Since the density of \(Y\) is bounded by \(K_Y\), the good contribution is at most \(2K_Y\delta/r\). Optimize \(K_Xr+2K_Y\delta/r\). \(\square\)

This does **not** establish (1) for arbitrary measurable \(v\): the derivative-good set can have indefinitely many monotone components.

## 2. A sharper one-bank square-map lemma

Let bank \(B=(L_B,V_B)\) have a joint probability density \(g_B\le M_B\). Let bank \(A=(L_A,V_A,P_A)\) have **any** probability law, independent of \(B\). In particular, \(A\) may have no planar density, and \(P_A\) can depend arbitrarily on its other coordinates. Set \(P_B=aL_B+bV_B\) for fixed real \(a,b\). Let \(H\), independent of both banks, have a density \(f_H\le1\). For arbitrary real \(\beta,\varepsilon\), define
\[
 L=L_A+L_B,\qquad V=V_A+V_B,\qquad P=P_A+aL_B+bV_B,
\]
\[
 Q=2HL+\beta L^2+V^2+2\varepsilon LP.
 \tag{2}
\]
Then \(Q\) has a density and
\[
 \|p_Q\|_\infty\le4\sqrt 2\,M_B+\tfrac12 .
 \tag{3}
\]
This includes cap-one hub densities with arbitrarily many fragmented components. The bound is uniform in \(\beta,\varepsilon,a,b\) and in the entire law of bank \(A\).

**Elementary square-map fact.** For any \(c,d\in\mathbb R\) and Borel \(E\) of length \(\delta\),
\[
 \big|\{y:(y+c)^2+d\in E\}\big|\le2\sqrt\delta.
 \tag{4}
\]
Indeed, for \(F=(E-d)\cap[0,\infty)\), the left side equals \(\int_F t^{-1/2}\,dt\), at most \(2\sqrt{|F|}\) by decreasing rearrangement. The estimate holds for disconnected and unbounded \(E\).

**Fixed-\(L\) slice.** Let \(\nu_A\) be the bank-\(A\) law. For almost every \(l\), define a finite, unnormalized measure \(\mu_l\) on the residual output by
\[
 \mu_l(E)=\int \nu_A(d\ell,dv_A,dp_A)
 \int_{\mathbb R} g_B(l-\ell,v_B)
 \mathbf1_E\!\left(
 \beta l^2+(v_A+v_B)^2+
 2\varepsilon l[p_A+a(l-\ell)+bv_B]\right)\,dv_B.
 \tag{5}
\]
For fixed \(l,\ell,v_A,p_A\), the argument of the indicator is a translated square in \(v_B\), since its \(v_B^2\) coefficient is exactly one. Hence (4) and \(g_B\le M_B\) give, uniformly in \(l\) and in the other-bank state,
\[
 \mu_l(E)\le2M_B\sqrt{|E|}.
 \tag{6}
\]
The measure \(\mu_l\) has total mass \(p_L(l)\), the density of \(L\), and \(\int_{\mathbb R}p_L(l)\,dl=1\). This is valid even when \(L_A\) is singular, because convolution with the absolutely continuous \(L_B\) produces the density \(p_L\).

**Integrating a fragmented hub.** As \(L=0\) has probability zero, conditioning on the banks yields a density representative
\[
 p_Q(s)=\int_{l\ne0}\frac1{2|l|}
 \int f_H\!\left(\frac{s-t}{2l}\right)\,d\mu_l(t)\,dl .
 \tag{7}
\]
For \(0<u<1\), write \(F_u=\{h:f_H(h)>u\}\). Layer cake and the normalization of \(f_H\) give
\[
 \int_0^1|F_u|\,du=1,\qquad
 \int_0^1\sqrt{|F_u|}\,du\le1.
 \tag{8}
\]
For \(|l|<1\), the target set of \(t\) where \(f_H((s-t)/(2l))>u\) is \(s-2lF_u\), with length \(2|l||F_u|\). By (6), its \(\mu_l\)-mass is at most \(2\sqrt2 M_B\sqrt{|l||F_u|}\). In (7), integrate \(1/(2|l|)\), then use \(\int_{|l|<1}|l|^{-1/2}\,dl=4\) and (8). This gives \(4\sqrt2 M_B\). For \(|l|\ge1\), use \(f_H\le1\), \(1/(2|l|)\le1/2\), and \(\int p_L=1\) to obtain another \(1/2\). This proves (3). \(\square\)

### Exact scope

The theorem needs a bank whose \(P\) contribution is affine in its own \(L,V\) coordinates, so that the residual output is a translated square in its \(V\) coordinate. The other bank and its \(P_A\) coordinate are unrestricted. An independently conditionable additional \(B\)-side offset also works if the conditional planar density bound survives conditioning. The argument does not handle a generally correlated third \(B\)-coordinate \(P_B\): conditioning on \(P_B\) may make the conditional planar density arbitrarily large, and \(v_B\mapsto(v_A+v_B)^2+2\varepsilon lP_B\) may lose convexity. The unrestricted arbitrary-measurable-local-phase lemma and the fully mixed-sign RMT theorem remain unproved.
