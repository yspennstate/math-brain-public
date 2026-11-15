# Two noisy observations: exact minimum norm and a risk-moment threshold

Let \(\sigma(t)=\max(t,0)\). Surface measure on \(S^{d-1}\subset\mathbb R^d\) is normalized to have mass one. Throughout \(d\ge2\).

## Model and result

Consider finite-width networks
\[
 f(x)=\sum_{j=1}^m a_j\sigma(w_j\cdot x),\qquad
 Q(a,w)=\frac12\sum_{j=1}^m(a_j^2+\|w_j\|^2).
\]
The width is unrestricted, or any fixed width at least two. There is no linear skip or output intercept. A minimum-norm interpolant minimizes \(Q\) subject to its two interpolation constraints. Minimizing the Euclidean parameter norm gives the same minimizers as minimizing \(Q\).

Take independent \(X_1,X_2\) uniform on \(S^{d-1}\), and independent Rademacher labels \(Y_1,Y_2\), also independent of the inputs. The regression function is zero. The conditional excess squared risk is
\[
 R=\mathbb E_X[f(X)^2],
\]
where the expectation here is over an independent test input, with the training sample held fixed.

**Theorem.** The following statements hold.

1. With opposite labels, the minimum-norm interpolant is unique as a function. Write \(\theta=\arccos(X_1\cdot X_2)\in(0,\pi)\), and orient the labels as \((1,-1)\). If \(0<\theta\le\pi/2\), put \(c=\cos\theta\), \(s=\sin\theta\),
   \[
   u=(X_1-cX_2)/s,\qquad v=(X_2-cX_1)/s.
   \]
   Then
   \[
   f(x)=\frac{\sigma(u\cdot x)-\sigma(v\cdot x)}s,
   \qquad Q_{\min}=2/s.
   \]
   If \(\pi/2\le\theta<\pi\), then
   \[
   f(x)=\sigma(X_1\cdot x)-\sigma(X_2\cdot x),
   \qquad Q_{\min}=2.
   \]

2. Its conditional excess risk is exactly
   \[
   R_d(\theta)=
   \begin{cases}
   \displaystyle\frac{\pi-\sin\theta+\theta\cos\theta}
   {\pi d\sin^2\theta},&0<\theta\le\pi/2,\\[6pt]
   \displaystyle\frac{\pi-\sin\theta-(\pi-\theta)\cos\theta}
   {\pi d},&\pi/2\le\theta<\pi.
   \end{cases}
   \]
   In particular \(R_d(\theta)\sim1/(d\theta^2)\) as \(\theta\downarrow0\).
   Two exact finite conditional means are
   \[
   \mathbb E[R\mid Y_1=-Y_2,d=4]
   =\frac38+\frac1{3\pi}-\frac{13}{9\pi^2},
   \qquad
   \mathbb E[R\mid Y_1=-Y_2,d=5]=\frac{55}{256}.
   \]

3. Let
   \[
   C_d=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d-1)/2)},
   \qquad \alpha=(d-1)/2.
   \]
   For the full Rademacher-label experiment,
   \[
   \mathbb P(R>t)\sim
   \frac{C_d}{2(d-1)d^{(d-1)/2}}t^{-(d-1)/2}.
   \]
   For every \(q>0\),
   \[
   \mathbb E_{X_1,X_2,Y_1,Y_2}[R^q]<\infty
   \quad\Longleftrightarrow\quad q<(d-1)/2.
   \]
   Thus the averaged squared excess risk is infinite for \(d=2,3\), and finite and positive for \(d\ge4\). The conditional risk is finite almost surely in every dimension considered.

4. The tail asymptotic and moment threshold in part 3 also hold for networks with hidden biases and objective
   \[
   f(x)=\sum_j a_j\sigma(w_j\cdot x+b_j),\qquad
   Q_b=\frac12\sum_j(a_j^2+\|w_j\|^2+b_j^2).
   \]
   No output intercept or skip is added. An explicit unique minimizer for opposite labels is given below.

5. In the homogeneous model of parts 1--3, the same moment threshold holds for a full-dimensional input distribution with bounded, nonzero label noise. Specifically take \(X=\rho U\), with \(U\) uniform on the sphere and \(\rho\) independent uniform on \([1,2]\), and take \(Y=\rho\varepsilon\), where \(\varepsilon\) is an independent Rademacher variable. The conditional risk is \((7/3)R\), where \(R\) is the sphere-model risk for the directions and signs of the training data.

These are statements at sample size two. They do not assert any limit as the number of observations tends to infinity.

## 1. Balancing and a dual certificate

For each nonzero hidden weight put \(z_j=w_j/\|w_j\|\) and \(\gamma_j=a_j\|w_j\|\). Positive homogeneity gives
\[
 f(x)=\sum_j\gamma_j\sigma(z_j\cdot x),\quad
 \|z_j\|=1,\quad
 Q\ge\sum_j|\gamma_j|.
\]
The inequality is \((a_j^2+\|w_j\|^2)/2\ge|a_j|\|w_j\|\), summed over the units. Conversely, any normalized representation can be balanced by setting
\[
 a_j=\operatorname{sign}(\gamma_j)\sqrt{|\gamma_j|},
 \qquad w_j=\sqrt{|\gamma_j|}\,z_j.
\]
This realizes the function with \(Q=\sum_j|\gamma_j|\). Zero units can be omitted or added. Thus minimizing \(Q\) is exactly the normalized-atom minimum-cost interpolation problem.

For fixed unit sample points \(x_1,x_2\), define
\[
 \Delta(z)=\sigma(z\cdot x_1)-\sigma(z\cdot x_2),\qquad
 M=\max_{\|z\|=1}|\Delta(z)|.
\]
Any normalized representation interpolating \((1,-1)\) satisfies
\[
 2=f(x_1)-f(x_2)=\sum_j\gamma_j\Delta(z_j)
 \le M\sum_j|\gamma_j|\le MQ.
 \tag{1}
\]
This is a dual certificate with multipliers \((1/M,-1/M)\). No strong-duality theorem is needed.

Suppose \(0<c=x_1\cdot x_2<1\), and let \(s=\sqrt{1-c^2}\) and \(u=(x_1-cx_2)/s\). Then \(u\perp x_2\) and \(\|u\|=1\). Set \(t=z\cdot x_2\) and \(p=z\cdot u\), so \(z\cdot x_1=ct+sp\).

If \(t\le0\), then \(ct+sp\le sp\le s\), so \(\Delta(z)\le s\). Equality with \(s>0\) forces \(p=1\), hence \(z=u\).

If \(t\ge0\) and \(ct+sp\le0\), then \(\Delta(z)=-t\le0<s\). If \(t\ge0\) and \(ct+sp\ge0\), then
\[
 \Delta(z)=(c-1)t+sp\le sp\le s.
\]
Equality again forces \(z=u\). Swapping the sample points shows that the minimum of \(\Delta\) is \(-s\), attained uniquely at \(v=(x_2-cx_1)/s\). Thus \(M=s\), with exactly these two signed maximizing atoms.

If \(-1<c\le0\), then \(\Delta(z)\le\sigma(z\cdot x_1)\le1\), with equality only at \(z=x_1\); it is attained since \(x_1\cdot x_2\le0\). The negative maximum is attained only at \(x_2\). Hence \(M=1\). At \(c=0\) both descriptions agree.

In the acute case, the two atoms \(u,v\) have sample-value vectors \((s,0)\) and \((0,s)\). Coefficients \(1/s,-1/s\) interpolate with cost \(2/s\), attaining (1). In the obtuse case the analogous vectors for \(x_1,x_2\) are \((1,0),(0,1)\), and coefficients \(1,-1\) attain cost 2.

Every minimum-cost representation must attain equality in every summand of (1). Its nonzero atoms must therefore be positive copies of the positive maximizing atom and negative copies of the negative maximizing atom. The interpolation equations fix their total coefficients. Every minimum-\(Q\) network is balanced and induces exactly this function. This proves part 1, including uniqueness as a function.

## 2. The risk integral

For two unit vectors \(p,q\) making angle \(\beta\in[0,\pi]\),
\[
 K_d(\beta)=\mathbb E_X[\sigma(p\cdot X)\sigma(q\cdot X)]
 =\frac{\sin\beta+(\pi-\beta)\cos\beta}{2\pi d}.
 \tag{2}
\]
Here is a derivation with the normalization explicit. Let \(G\) be a standard Gaussian in \(\mathbb R^d\). Its direction is uniform and independent of its radius, and \(\mathbb E\|G\|^2=d\). Homogeneity makes the Gaussian expectation equal to \(dK_d(\beta)\).

In the plane of \(p,q\), write the Gaussian as \(r(\cos\phi,\sin\phi)\), with \(\phi\) uniform, independent of \(r\), and \(\mathbb E r^2=2\). Choose \(p\) at angle zero and \(q\) at angle \(\beta\). Both projections are positive on an angular interval \([\beta-\pi/2,\pi/2]\), up to endpoints and angular periodicity. Therefore their product has Gaussian expectation
\[
 \frac1\pi\int_{\beta-\pi/2}^{\pi/2}
 \cos\phi\cos(\phi-\beta)\,d\phi.
\]
The product-to-sum identity gives this integral as
\[
 \frac{\sin\beta+(\pi-\beta)\cos\beta}{2\pi}.
\]
Dividing by \(d\) proves (2). In particular \(\mathbb E\sigma(p\cdot X)^2=1/(2d)\).

For acute sample angle, direct multiplication gives \(u\cdot v=-c\), so their angle is \(\pi-\theta\). Consequently
\[
 R_d(\theta)=\frac{1/d-2K_d(\pi-\theta)}{\sin^2\theta},
\]
which is the first formula in part 2. For obtuse sample angle the corresponding calculation is \(1/d-2K_d(\theta)\), giving the second formula. Both equal \((\pi-1)/(\pi d)\) at \(\pi/2\). The second has limit \(2/d\) at \(\pi\).

As \(\theta\downarrow0\), the numerator of the first formula tends to \(\pi\) and \(\sin\theta/\theta\to1\). Thus \(d\theta^2R_d(\theta)\to1\).

An independent check on the singular coefficient comes from the odd part of the function. The identity \(\sigma(t)-\sigma(-t)=t\) implies
\[
 \frac{f(x)-f(-x)}2
 =\frac{(u-v)\cdot x}{2s}
 =\frac{(x_1-x_2)\cdot x}{2(1-c)}.
 \tag{3}
\]
Odd and even functions are orthogonal in \(L_2\) of the sphere. Since \(\mathbb E XX^T=I/d\), the squared norm of (3) is
\[
 \frac1{2d(1-c)}\sim\frac1{d\theta^2}.
 \tag{4}
\]
The exact risk has the same leading term. In particular the singularity comes from a global linear component, rather than only a bump near the training points.

## 3. Random angles and equal labels

Conditional on \(X_1\), the angle \(\theta\) of an independent uniform \(X_2\) has density
\[
 p_d(\theta)=C_d\sin^{d-2}\theta,\qquad 0<\theta<\pi.
 \tag{5}
\]
For completeness, slicing the sphere at polar angle \(\theta\) gives an area proportional to \(\sin^{d-2}\theta\). Its normalizing integral is
\[
 \int_0^\pi\sin^{d-2}\theta\,d\theta
 =B((d-1)/2,1/2)
 =\frac{\sqrt\pi\,\Gamma((d-1)/2)}{\Gamma(d/2)}.
\]
The first equality follows by symmetry about \(\pi/2\) and the substitution \(t=\sin^2\theta\) on \([0,\pi/2]\). This proves (5), also for \(d=2\), where the density is \(1/\pi\).

Away from zero, the risk formula is bounded, including its continuous extension at \(\pi\). Near zero, \(R_d(\theta)\sim(d\theta^2)^{-1}\). For every \(\eta>0\), there is a fixed sufficiently small \(\delta>0\) such that
\[
 \frac{1-\eta}{d\theta^2}\le R_d(\theta)
 \le\frac{1+\eta}{d\theta^2}\quad(0<\theta<\delta).
\]
For large \(t\), the event \(R_d(\theta)>t\) therefore lies between the events with angular cutoffs \(\sqrt{(1-\eta)/(dt)}\) and \(\sqrt{(1+\eta)/(dt)}\). Integration of (5), followed by \(\eta\downarrow0\), gives
\[
 \mathbb P(R>t\mid Y_1=-Y_2)
 \sim\frac{C_d}{(d-1)d^{(d-1)/2}}t^{-(d-1)/2}.
 \tag{6}
\]
Alternatively, direct moment integration near zero is comparable to
\[
 \int_0^\delta\theta^{d-2-2q}\,d\theta.
 \tag{7}
\]
It is finite exactly when \(d-2-2q>-1\), or \(q<(d-1)/2\); equality gives a logarithmic divergence.

The finite conditional means can also be evaluated without a singular integral. For \(d\ge4\), set \(I_k=\int_0^{\pi/2}\sin^k t\,dt\), and \(A(t)=\pi-\sin t+t\cos t\). Reflecting the obtuse half of the risk integral by \(t=\pi-\theta\) yields
\[
 \mathbb E[R\mid Y_1=-Y_2]
 =\frac{C_d}{\pi d}\int_0^{\pi/2}
 A(t)\bigl(\sin^{d-4}t+\sin^{d-2}t\bigr)\,dt.
 \tag{9a}
\]
Integration by parts, for every integer \(k\ge0\), gives
\[
 \int_0^{\pi/2} A(t)\sin^k t\,dt
 =\pi I_k+\frac{\pi}{2(k+1)}-\frac{k+2}{k+1}I_{k+1}.
 \tag{9b}
\]
Indeed the contribution from \(t\cos t\sin^k t\) is \(\pi/[2(k+1)]-I_{k+1}/(k+1)\); the other two terms contribute \(\pi I_k-I_{k+1}\).

For \(d=4\), \(C_4=2/\pi\), and the two terms \(k=0,2\) in (9b) sum to
\[
 3\pi^2/4+2\pi/3-26/9,
\]
using \(I_0=\pi/2,I_1=1,I_2=\pi/4,I_3=2/3\). Multiplication by \(C_4/(4\pi)=1/(2\pi^2)\) gives \(3/8+1/(3\pi)-13/(9\pi^2)\).

For \(d=5\), \(C_5=3/4\). Using also \(I_4=3\pi/16\), the terms \(k=1,3\) sum to \(275\pi/192\). Multiplication by \(C_5/(5\pi)=3/(20\pi)\) gives \(55/256\). The values of \(I_k\) follow either by elementary integration or the integration-by-parts recurrence \(I_k=(k-1)I_{k-2}/k\) for \(k\ge2\).

When the labels are equal to 1, the function
\[
 g(x)=\frac{\sigma(x_1\cdot x)+\sigma(x_2\cdot x)}{1+\max(c,0)}
\]
interpolates, with normalized-atom cost at most 2. The negative of \(g\) treats labels \((-1,-1)\). A minimum-\(Q\) network has normalized cost at most 2. The triangle inequality in \(L_2\), and the atom norm \(1/\sqrt{2d}\), give
\[
 R\le2/d
 \tag{8}
\]
for every such minimizer. Thus equal labels contribute no unbounded tail. Opposite labels occur with probability \(1/2\); (6)--(8) prove part 3. Positivity of the mean when finite follows from the positive risk on the positive-probability opposite-label event. Coincident or exactly antipodal sample points form null events and do not affect these assertions.

## 4. Penalized hidden biases

Use augmented sample points \(z_i=(x_i,1)\in\mathbb R^{d+1}\), each of norm \(r=\sqrt2\). Balancing now normalizes \((w_j,b_j)\) to a unit vector, at cost \(|a_j|\sqrt{\|w_j\|^2+b_j^2}\). Put
\[
 c=x_1\cdot x_2,\quad \kappa=\frac{1+c}2,\quad
 s_b=\sqrt{1-\kappa^2},\quad D=2(1-\kappa^2).
\]
For \(-1<c<1\) the normalized augmented points make an acute angle, since \(0<\kappa<1\). Applying the certificate in section 1 to \(z_i/r\), and then multiplying the atom values by \(r\), shows that the unique minimizer for labels \((1,-1)\) is
\[
 f_b(x)=\frac{\sigma(A_1(x))-\sigma(A_2(x))}{D},
 \tag{9}
\]
where
\[
 A_1(x)=(x_1-\kappa x_2)\cdot x+1-\kappa,
 \qquad
 A_2(x)=(x_2-\kappa x_1)\cdot x+1-\kappa.
\]
Its cost is \(Q_{b,\min}=2/(r s_b)\). Indeed the normalized augmented atom directions are \((z_1-\kappa z_2)/(r s_b)\) and its swapped version; their nonzero sample values equal \(r s_b\), so coefficients \(\pm1/(r s_b)\) give both (9) and the stated cost.

Define
\[
 B=\frac{x_1-x_2}{1-c},\qquad
 m(x)=(1-\kappa)\left(1+\frac{(x_1+x_2)\cdot x}{2}\right),
 \qquad
 t(x)=\frac{(1+\kappa)(x_1-x_2)\cdot x}{2}.
\]
Then \(A_1=m+t\), \(A_2=m-t\), and \(2t/D=B\cdot x\), because \(D=(1-c)(1+\kappa)\). On the unit sphere,
\[
 m(x)\ge0
\]
by \(\|x_1+x_2\|\le2\). For \(m\ge0\), an elementary case split at \(|t|=m\) gives
\[
 |t|\le|\sigma(m+t)-\sigma(m-t)|\le2|t|,
\]
with the difference having the sign of \(t\). Hence pointwise on the sphere
\[
 \tfrac12|B\cdot x|\le|f_b(x)|\le|B\cdot x|,
\]
and consequently
\[
 \frac1{2d(1-c)}\le R_b\le\frac2{d(1-c)}.
 \tag{10}
\]
There is also an exact leading coefficient. The same case split gives
\[
 f_b(x)=\tfrac12 B\cdot x+h(x),\quad
 |h(x)|\le\frac{m(x)}D
 =\frac{1+(x_1+x_2)\cdot x/2}{2(1+\kappa)}\le1.
\]
It follows by Cauchy--Schwarz that
\[
 \left|R_b-\frac1{2d(1-c)}\right|
 \le\sqrt{\frac2{d(1-c)}}+1.
 \tag{11}
\]
Multiplying (11) by \(d\theta^2\), using \(1-\cos\theta\sim\theta^2/2\), proves \(d\theta^2R_b\to1\). Inequality (10) also bounds the risk uniformly away from zero angle.

For equal labels, normalized atoms with augmented directions \(z_i/r\) and coefficients \(1/[r(1+\kappa)]\) interpolate \((1,1)\). Their total cost is \(2/[r(1+\kappa)]\le\sqrt2\). A normalized affine atom \(\sigma(w\cdot X+b)\), with \(\|w\|^2+b^2=1\), has squared \(L_2\) norm at most
\[
 \mathbb E(w\cdot X+b)^2=\|w\|^2/d+b^2\le1.
\]
Thus every equal-label minimum-\(Q_b\) interpolant has risk at most 2. Sign reversal handles two negative labels. Equations (5)--(7) now apply with precisely the same leading coefficient and label probability as before. This proves part 4.

## 5. Full-dimensional annulus

Let the data distribution be \(X=\rho U\), \(Y=\rho\varepsilon\), as in part 5. Its input density with respect to Lebesgue measure on \(1<\|x\|<2\) is
\[
 \frac1{|S^{d-1}|\,\|x\|^{d-1}},
\]
which is bounded above and below by strictly positive constants on that annulus. Thus the distribution is full-dimensional and compactly supported. Its regression function is zero, its conditional noise variance is \(\|X\|^2\), and \(|Y|\le2\). The noise is heteroscedastic.

For every homogeneous network,
\[
 f(\rho_iU_i)=\rho_if(U_i).
\]
Since \(\rho_i>0\), its interpolation equations are exactly \(f(U_i)=\varepsilon_i\). The feasible parameter sets and objective are therefore the same as in the sphere experiment. At test time,
\[
 \mathbb E_X f(X)^2
 =\mathbb E\rho^2\,\mathbb E_U f(U)^2
 =\left(\int_1^2 r^2\,dr\right)R
 =\frac73 R.
\]
This proves part 5 and preserves all moment thresholds.

## Scope

The theorem solves an unrestricted-width minimum-parameter-norm problem at exactly two observations. It does not identify a gradient-descent implicit bias, address a free skip, or show that the same singularity survives additional interpolation constraints. In particular, infinite averaged risk at sample size two does not imply divergence in probability, or divergence of averaged risk, as sample size tends to infinity. The sphere result has independent bounded label noise; the full-dimensional annulus extension uses explicitly specified heteroscedastic noise.
