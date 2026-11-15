# A close pair and an open set of third observations

Let sigma(t)=max(t,0). In R^d, d>=2, consider finite-width networks

\[
 f(x)=\sum_j c_j\sigma(w_j\cdot x),\qquad
 Q(f;c,w)=\frac12\sum_j(c_j^2+\|w_j\|^2).
\]

There are no biases, linear skips, or output intercepts. A minimum-Q interpolant minimizes the displayed parameter objective subject to the interpolation constraints. Width is either unrestricted or fixed at any m>=3. Test inputs are uniform on S^{d-1}, with normalized surface measure. The regression function is zero, and the conditional excess squared risk is R(f)=E[f(X)^2].

Fix orthonormal e1,e2 and write

\[
 a=\cos(\theta/2),\quad b=\sin(\theta/2),\quad s=\sin\theta=2ab,
 \qquad x_1=ae_1+be_2,\quad x_2=ae_1-be_2.
\]

The first two labels are 1,-1. The third observation is (z,tau), where z lies on S^{d-1}. All statements below allow components of z and network weights outside span(e1,e2).

## Theorem

Fix 0<delta<=1 and H>=0. Uniformly over z with |z dot e2|>=delta, labels |tau|<=H, and every minimum-Q interpolant f_theta of these three observations,

\[
 \sup_{\|x\|\le1}
 \left|\theta f_\theta(x)
       +2\epsilon\sigma(-\epsilon e_2\cdot x)\right|
 \longrightarrow0,
 \qquad \epsilon=\operatorname{sign}(z\cdot e_2),
 \tag{1}
\]

as theta decreases to zero. Consequently, uniformly over the same choices,

\[
 \theta^2R(f_\theta)\longrightarrow\frac2d.
 \tag{2}
\]

In particular, there is a theta_0(delta,H,d)>0 such that

\[
 R(f_\theta)\ge\frac1{2d\theta^2},\qquad
 0<\theta<\theta_0,
 \tag{3}
\]

for every such third observation and every minimizer. For 0<delta<1 the strict condition |z dot e2|>delta describes a nonempty open set of positive surface measure.

Here is an explicit error bound. For 0<theta<=delta/2, put

\[
 K=2+\frac{2(H+2)}\delta,\quad
 U_\theta=\frac{2\theta}s+K\theta,\quad
 E_\theta=2\sqrt{U_\theta\left(U_\theta-\frac\theta b\right)},
\]
\[
 \eta_\theta=(1+\delta^{-1})E_\theta
               +\frac{\theta H}\delta+U_\theta-2.
 \tag{4}
\]

The left side of (1) is at most eta_theta. In particular eta_theta=O_{delta,H}(sqrt(theta)). The conclusion also holds for any interpolant whose parameter cost is at most 2/s+K, whether or not it minimizes Q.

## 1. Atomic representation

For a nonzero w_j define u_j=w_j/||w_j|| and gamma_j=c_j||w_j||. Units with zero coefficient or zero weight can be discarded. Then

\[
 f(x)=\sum_j\gamma_j\sigma(u_j\cdot x),\quad
 \|u_j\|=1,\qquad T:=\sum_j|\gamma_j|\le Q.
 \tag{5}
\]

The inequality is (c_j^2+||w_j||^2)/2 >= |c_j|||w_j||, summed over units. Conversely, the atomic coefficient gamma at unit direction u is realized with cost exactly |gamma| by c=sign(gamma)sqrt(|gamma|), w=sqrt(|gamma|)u. Thus atomic competitors yield parameter competitors with the same number of units.

For completeness, minimum-Q interpolants exist in both width conventions used here. For fixed m>=3, the competitor constructed below gives a nonempty constraint set. A bounded Q sublevel is compact in the finite-dimensional parameter space, and interpolation constraints are closed because ReLU is continuous. A minimizing sequence therefore has a feasible limit attaining the infimum. For unrestricted width, let A(u)=(sigma(u dot x1),sigma(u dot x2),sigma(u dot z)). The set C=conv{+A(u),-A(u): ||u||=1} is compact in R^3. To see compactness directly, any convex combination with more than four points admits an affine dependence; subtracting a suitable multiple of that dependence from its nonnegative coefficients preserves their sum and represented point while making at least one coefficient zero. Repetition reduces to four points. C is therefore the continuous image of a compact set of four atoms and four nonnegative coefficients summing to one. A feasible label vector belongs to T C for some finite T, and the infimum of such T is attained by compactness; it is positive since an atom has first coordinate of absolute value at most one and the first label is 1. An attained point of T C is a finite atomic representation, hence gives an attained parameter minimum by balancing as above. No uniqueness assertion is needed.

## 2. A uniformly bounded excess-cost competitor

First suppose q:=z dot e2>=delta, and write p=z dot e1. Put v=be1-ae2. For 0<theta<=delta/2<=1/2, we have b<=delta/4 and a>=3/4. Hence

\[
 h:=aq-bp\ge a\delta-b\ge\delta/2>0,
 \qquad 1/a\le2.
 \tag{6}
\]

Define

\[
 r=\frac{\tau-\sigma(p)/a}{h},\qquad
 F(x)=\frac1a\sigma(e_1\cdot x)
       -\frac1{ab}\sigma(v\cdot x)
       +r\sigma(-v\cdot x).
 \tag{7}
\]

At x1 the three unweighted atom values are a,0,0. At x2 they are a,s,0. Thus F(x1)=1 and F(x2)=1-s/(ab)=-1. At z, v dot z=-h<0 and (-v) dot z=h, so F(z)=sigma(p)/a+r h=tau. The correction atom vanishes at both pair samples, independently of the value or sign of r.

All three directions in (7) are unit vectors. Since |p|<=1, (6) gives

\[
 |r|\le\frac{2(H+2)}\delta.
\]

Balancing the three units as in (5) realizes F with

\[
 Q(F)\le\frac1a+\frac1{ab}+|r|
 \le\frac2s+K.
 \tag{8}
\]

Every minimum-Q interpolant, including every minimum at fixed width m>=3, therefore has cost at most the right side. The construction uses no assumption on the remaining coordinates of z.

## 3. Quantitative localization of signed atomic mass

Let f be any interpolant with Q<=2/s+K, and use (5). For a unit direction u put P=u dot e1, Q_2=u dot e2, and

\[
 g_\theta(u)=\frac{\sigma(aP+bQ_2)-\sigma(aP-bQ_2)}{2ab}.
 \tag{9}
\]

Monotonicity and the 1-Lipschitz property of sigma imply

\[
 0\le g_\theta(u)\le Q_2/a\quad(Q_2\ge0),\qquad
 Q_2/a\le g_\theta(u)\le0\quad(Q_2\le0).
 \tag{10}
\]

For a sign t in {-1,1}, if t Q_2>=0 then 0<=t g_theta(u)<=t Q_2/a, so

\[
 \|u-te_2\|^2=2(1-tQ_2)
 \le2(1-atg_\theta(u))\le4(1-atg_\theta(u)).
\]

If t Q_2<0, then t g_theta(u)<=0. Consequently ||u-te2||^2<=4<=4(1-a t g_theta(u)). In both cases

\[
 \|u-te_2\|^2\le4(1-atg_\theta(u)).
 \tag{11}
\]

This inequality holds for every ambient unit direction, including directions orthogonal to the sample plane and directions with the wrong sign of the second coordinate.

Set t_j=sign(gamma_j) and

\[
 M=\theta\sum_j|\gamma_j|,\quad
 A=\theta\sum_{\gamma_j>0}\gamma_j,\quad
 B=\theta\sum_{\gamma_j<0}|\gamma_j|,
 \qquad M=A+B.
\]

Pair interpolation and (9) give the exact identity

\[
 \sum_j\gamma_jg_\theta(u_j)=\frac{f(x_1)-f(x_2)}s=\frac2s.
 \tag{12}
\]

Multiplying (11) by theta|gamma_j| and summing therefore yields

\[
 \sum_j\theta|\gamma_j|\|u_j-t_je_2\|^2
 \le4\left(M-\frac{2a\theta}s\right)
 =4\left(M-\frac\theta b\right).
 \tag{13}
\]

In particular M>=theta/b>=2. By (5) and the assumed cost bound,

\[
 2\le M\le U_\theta.
 \tag{14}
\]

Compare the scaled network with its signed mass placed exactly at the two limiting directions:

\[
 G(x)=A\sigma(e_2\cdot x)-B\sigma(-e_2\cdot x).
\]

For ||x||<=1, the ReLU Lipschitz bound and Cauchy–Schwarz give

\[
 |\theta f(x)-G(x)|
 \le\sum_j\theta|\gamma_j|\|u_j-t_je_2\|
 \le\sqrt{M\sum_j\theta|\gamma_j|\|u_j-t_je_2\|^2}
 \le2\sqrt{M(M-\theta/b)}\le E_\theta.
 \tag{15}
\]

The last inequality follows because M>=theta/b and the product M(M-theta/b) increases there. This establishes localization quantitatively; it does not presume convergence of atom directions or a fixed number of units.

## 4. The third constraint selects one hemisphere

At the third point q>=delta, G(z)=Aq. Using f(z)=tau and (15),

\[
 A\delta\le Aq\le\theta H+E_\theta,
 \qquad A\le\frac{\theta H+E_\theta}\delta.
 \tag{16}
\]

Since B=M-A and M>=2, and the two ReLUs below have disjoint positive supports,

\[
 \sup_{\|x\|\le1}|G(x)+2\sigma(-e_2\cdot x)|
 =\max\{A,|2-B|\}\le A+M-2.
\]

Together with (14)–(16), this proves

\[
 \sup_{\|x\|\le1}|\theta f(x)+2\sigma(-e_2\cdot x)|
 \le E_\theta+\frac{\theta H+E_\theta}\delta+U_\theta-2
 =\eta_\theta.
 \tag{17}
\]

Here U_theta tends to 2, theta/b tends to 2, and

\[
 U_\theta-\theta/b
 =K\theta+\frac\theta b\frac{1-a}a=O_{\delta,H}(\theta).
 \tag{18}
\]

Thus eta_theta=O_{delta,H}(sqrt(theta)), proving the claimed uniform limit for positive q.

For q<=-delta, replace e2 by -e2, interchange the pair samples, and replace f by -f. The transformed pair again has labels (1,-1), the transformed third label is -tau, and the new third second-coordinate is -q>=delta. Parameter cost is unchanged. Applying (17) gives ||theta f-2 sigma(e2 dot x)||_infinity<=eta_theta. This is exactly (1) for negative q, with the same uniform constants.

## 5. Risk and a separate leading-term check

For X uniform on S^{d-1}, reflection symmetry and sum_i X_i^2=1 give

\[
 E[\sigma(e_2\cdot X)^2]=E[X_2^2]/2=\frac1{2d}.
\]

The limiting function in (1) therefore has squared L2 norm 4/(2d)=2/d. The triangle inequality in L2 and (17) give the explicit bounds

\[
 \left(\max\{0,\sqrt{2/d}-\eta_\theta\}\right)^2
 \le\theta^2R(f_\theta)
 \le(\sqrt{2/d}+\eta_\theta)^2.
 \tag{19}
\]

These prove (2). Taking theta small enough that eta_theta<sqrt(2/d)/2 proves (3).

A second derivation of the coefficient comes from the odd and even parts. The limiting function for q>0 is

\[
 -2\sigma(-X_2)=X_2-|X_2|.
\]

Its odd and even terms have squared L2 norms 1/d each and are orthogonal by reflection. Taking odd and even parts is continuous in the uniform norm, so each part of theta f_theta has limiting risk 1/d. For q<0 the limit is X2+|X2| and the same calculation applies. Their sum again gives 2/d. This check does not use a ReLU product kernel formula.

## 6. Random triples: a finite-sample consequence

Let X1,X2,X3 be iid uniform on S^{d-1}; let Y1,Y2,Y3 be independent Rademacher variables, independent of the inputs. Let f be any measurable selection of minimum-Q interpolants, with unrestricted width or a fixed width m>=3, and R=E_X[f(X)^2]. All statements in this section concern sample size three.

Such interpolants exist almost surely. Indeed the three inputs are pairwise nonparallel almost surely. Their atomic response vectors span R^3: if a vector lambda annihilated every response vector, then sum_i lambda_i sigma(u dot Xi) would vanish for every unit u. For each i choose a unit u0 perpendicular to Xi but to neither other input. Such a choice exists: for d=2 nonparallelism suffices; for larger d, a finite union of proper subspaces cannot cover Xi-perpendicular. On the spherical curve u(t)=u0 cos(t)+Xi sin(t), the i-th summand is lambda_i sigma(sin(t)), whose one-sided derivatives differ by lambda_i at zero. The other summands are smooth there since u0 dot Xj is nonzero. The identically zero sum has no derivative jump, so lambda_i=0. This holds for all i. Three independent atomic response vectors therefore interpolate arbitrary labels using at most three units. The compactness argument in Section 1 then supplies minimum-Q interpolants for fixed m>=3 and unrestricted width.

Conditional on a noncoincident, nonantipodal pair, define

\[
 e_1=\frac{X_1+X_2}{\|X_1+X_2\|},\qquad
 e_2=\frac{X_1-X_2}{\|X_1-X_2\|},\qquad
 \theta=\arccos(X_1\cdot X_2).
\]

These are orthonormal and give exactly the coordinates used above. The excluded pair events have probability zero. The event Y1=-Y2 has probability 1/2. Multiplying a minimizer and all its labels by -1 preserves optimality and risk, so the orientation of the opposite labels is immaterial.

For each fixed delta in (0,1), conditional on the pair the probability

\[
 p_{d,\delta}:=P(|X_3\cdot e_2|\ge\delta)>0
\]

is independent of that pair by rotation invariance. It tends to one as delta decreases to zero, because the equatorial section {X3 dot e2=0} has zero surface measure. Conditional on X1, the angle theta of X2 has density

\[
 C_d\sin^{d-2}\theta,\quad 0<\theta<\pi,\qquad
 C_d=\frac{\Gamma(d/2)}{\sqrt\pi\Gamma((d-1)/2)}.
 \tag{20}
\]

Indeed spherical polar coordinates about X1 give a surface element proportional to sin^{d-2}(theta) dtheta. Its normalization is the displayed beta integral; for d=2 the same formula is the uniform angle density 1/pi.

Fix delta. Apply (3) on the cap event, with H=1. For any r>0,

\[
 E[R^r]\ge\frac12p_{d,\delta}C_d(2d)^{-r}
       \int_0^{\theta_0}\theta^{-2r}\sin^{d-2}\theta\,d\theta.
 \tag{21}
\]

As theta decreases to zero the integrand is asymptotic to theta^{d-2-2r}; its integral diverges exactly when d-2-2r<=-1. Therefore

\[
 \boxed{E[R^r]=\infty\quad\text{for every }r\ge(d-1)/2.}
 \tag{22}
\]

In particular E[R]=infinity for d=2 and d=3 at n=3. The converse finiteness statement for smaller moments is not asserted.

There is also an explicit lower bound on the risk tail. Put alpha=(d-1)/2. By the uniform limit (2), for each fixed delta and each 0<xi<2/d there is a positive angle threshold below which R>=(2/d-xi)/theta^2 on the cap and opposite-label events. Thus, for all sufficiently large t,

\[
 P(R>t)\ge\frac12p_{d,\delta}C_d
       \int_0^{\sqrt{(2/d-\xi)/t}}\sin^{d-2}\theta\,d\theta.
\]

The integral is asymptotic to (2/d-xi)^alpha t^{-alpha}/(d-1). First take the lower limit as t tends to infinity; then let xi decrease to zero and delta decrease to zero. This gives

\[
 \boxed{\liminf_{t\to\infty}t^{(d-1)/2}P(R>t)
 \ge\frac{C_d}{2(d-1)}\left(\frac2d\right)^{(d-1)/2}.}
 \tag{23}
\]

Only the designated pair (X1,X2) was used. This is a lower bound, not a claimed sharp tail asymptotic. It also independently implies (22), including its logarithmically divergent endpoint, by integrating the tail of R^r.

## 7. Failure of uniformity as the third coordinate vanishes

The nonzero lower bound on |z dot e2| is substantive even when the third label is +1 and the third point stays far from the pair. Put h=theta/2, take 0<theta<pi/4, and define

\[
 u=be_1+ae_2,\quad v=be_1-ae_2,\qquad
 z_\theta=-\cos(3h)e_1+\sin(3h)e_2,
\]
\[
 f_2(x)=\frac{\sigma(u\cdot x)-\sigma(v\cdot x)}s.
 \tag{24}
\]

The pair responses of u,v are (s,0),(0,s), so f2 interpolates (1,-1). Moreover

\[
 u\cdot z_\theta=\sin(2h)=s,\qquad
 v\cdot z_\theta=-\sin(4h)<0,
\]

and hence f2(z_theta)=1 exactly.

To verify minimality without assuming a selection rule, the pair dual (1/s,-1/s) has price at most one on every unit atom. Here is the bound explicitly. In the orthonormal coordinates t=w dot x2, p=w dot u, one has w dot x1=c t+s p, where c=cos(theta)>0 and |p|<=1. If t<=0 then sigma(c t+s p)-sigma(t)<=s. If t>=0 and c t+s p<=0 the difference is -t<=0. In the remaining case it is (c-1)t+s p<=s. Interchanging x1,x2 gives the lower bound -s. Thus every pair interpolant has cost at least 2/s, and f2 attains it. Since f2 already satisfies the third constraint, it is also a minimum-Q three-point interpolant, using two units and therefore admissible at any width m>=3.

Finally theta/s tends to one, u tends to e2, and v tends to -e2. ReLU Lipschitz continuity gives uniform convergence theta f2(x) -> sigma(e2 dot x)-sigma(-e2 dot x)=e2 dot x. Consequently

\[
 \theta^2R(f_2)\longrightarrow\frac1d,
 \qquad z_\theta\cdot e_2=\sin(3\theta/2)\longrightarrow0.
 \tag{25}
\]

This contradicts the coefficient 2/d if the fixed-delta hypothesis is dropped. It does not contradict the positive-cap theorem, whose uniform angle threshold depends on delta.

## Relation to the earlier result and limits of the theorem

The earlier exact family has z=e2 and tau in {-1,1}. Its formulas interpolate because their atom-value columns are, respectively, (1,1-2b,1) and (0,s,0) for the positive-label construction, and (1,cos(theta),b), (0,s,0), (0,0,a) for the negative-label construction. Their stated costs equal their dual values. In both cases the coefficient of sigma(v dot x) is asymptotic to -2/theta, v tends to -e2, and all other coefficients stay bounded. This recovers their uniform limit and 2/d risk coefficient independently of their exact finite-angle risk formulas. The independent piecewise-antiderivative verification is in recheck_earlier.py.

The theorem replaces the single deterministic third location by an open set in every ambient dimension, allows arbitrary bounded third labels, and applies to every minimizer without proving uniqueness. Its random-triple conclusion concerns training-averaged finite-sample moments. It supplies no conclusion about convergence in probability or expected risk as n tends to infinity. Penalized biases, free linear skips, additional observations, and GD selection are outside the result. No conclusion is asserted uniformly near z dot e2=0, and no finiteness claim is made for r<(d-1)/2.
