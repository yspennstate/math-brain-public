# A third interpolation constraint at a fixed angle

Let sigma(t)=max(t,0). For d>=2 consider homogeneous two-layer networks

\[
 f(x)=\sum_{j=1}^m a_j\sigma(w_j\cdot x),\qquad
 Q=\frac12\sum_j(a_j^2+\|w_j\|^2).
\]

There are no biases, linear skip, or output intercept. Width is unrestricted. Let e1,e2 be orthonormal, and set

\[
 0<\theta<\pi/3,\quad h=\theta/2,\quad a=\cos h,\quad b=\sin h,
 \quad s=2ab=\sin\theta,
\]
\[
 x_1=ae_1+be_2,\quad x_2=ae_1-be_2,\quad x_3=e_2,
 \quad (y_1,y_2,y_3)=(1,-1,\tau),\quad\tau\in\{-1,1\}.
\]

The pair has separation theta, while the angles to the third point are pi/2-h and pi/2+h. Write v=be1-ae2. A test input X is uniform on the unit sphere, with normalized surface measure, and R=E[f(X)^2]. This is excess squared risk relative to the zero regression function. The theorem concerns these deterministic training configurations, with no sampling assertion about their probability.

## Theorem

For tau=1 define

\[
 W=\frac{1-b}{a}e_1+e_2,\qquad
 L=\|W\|=\sqrt{\frac2{1+b}},\qquad C_+=\frac{1-b}{ab}.
\]

The unique minimum-Q function is

\[
 f_+(x)=\sigma(W\cdot x)-C_+\sigma(v\cdot x),\qquad
 Q_+=L+C_+.
 \tag{1}
\]

Two units suffice, and the same conclusion holds at any fixed width at least two.

For tau=-1 define C_-=a/b and D=(1+b)/a. The unique minimum-Q function is

\[
 f_-(x)=\sigma(x_1\cdot x)-C_-\sigma(v\cdot x)
                         -D\sigma(-v\cdot x),\qquad
 Q_-=1+C_-+D=1+\frac1{ab}+\frac1a.
 \tag{2}
\]

Three units suffice, and the same conclusion holds at any fixed width at least three.

For the angle beta between W and v, equivalently

\[
 \cos\beta=-\sqrt{\frac{1-b}{2}},
\]

the exact risks are

\[
 R_+=\frac{L^2+C_+^2}{2d}
       -\frac{LC_+}{\pi d}
        [\sin\beta+(\pi-\beta)\cos\beta],
 \tag{3}
\]
\[
 R_-=\frac{1+C_-^2+D^2}{2d}-\frac{C_-+D}{\pi d}.
 \tag{4}
\]

For either sign of the third label,

\[
 \sup_{\|x\|\le1}|\theta f_\tau(x)+2\sigma(-e_2\cdot x)|\longrightarrow0,
 \qquad \theta^2R_\tau\longrightarrow\frac2d.
 \tag{5}
\]

Thus the third constraint changes the leading risk coefficient from 1/d to 2/d. It preserves a divergent global odd linear component and creates an equally large even component. These finite-sample statements do not determine the limit as sample size tends to infinity.

## 1. Atomic formulation and the two-point re-check

For each nonzero w set z=w/||w|| and gamma=a||w||. Positive homogeneity and the inequality (a^2+||w||^2)/2>=|a|||w|| give

\[
 f(x)=\sum_j\gamma_j\sigma(z_j\cdot x),\quad
 \|z_j\|=1,\quad Q\ge\sum_j|\gamma_j|.
 \tag{6}
\]

Conversely a unit-atom representation is realized with equality by parameters a_j=sign(gamma_j)sqrt(|gamma_j|), w_j=sqrt(|gamma_j|)z_j. Zero units may be added. It is therefore enough to minimize the sum of absolute atomic coefficients.

For a vector lambda in R^3 put

\[
 g_\lambda(z)=\sum_{i=1}^3\lambda_i\sigma(z\cdot x_i).
\]

If |g_lambda(z)|<=1 for all unit z, every interpolant has

\[
 Q\ge\sum_j|\gamma_j|\ge\sum_j\gamma_jg_\lambda(z_j)
 =\lambda\cdot y.
 \tag{7}
\]

Equality requires every nonzero coefficient to satisfy g_lambda(z_j)=sign(gamma_j). An explicit interpolant attaining lambda dot y proves optimality; identifying the equality atoms proves uniqueness as a function.

The needed two-point fact can be checked without optimization. Put u=be1+ae2. For a unit z write t=z dot x2, p=z dot u; then z dot x1=c t+s p, where c=cos(theta)>0. If t<=0, then sigma(c t+s p)<=s, so the difference Delta(z)=sigma(z dot x1)-sigma(z dot x2) is at most s. Equality forces p=1 and z=u. If t>=0 and c t+s p<=0 the difference is nonpositive. In the remaining case it equals (c-1)t+s p<=s; equality again forces z=u. Swapping the samples proves Delta>=-s, with equality only at v. This argument also handles components of z outside their plane.

Thus the two-point dual (1/s,-1/s) exposes exactly +u and -v. The interpolant [sigma(u dot x)-sigma(v dot x)]/s has cost 2/s and is unique. Its odd part, using sigma(t)-sigma(-t)=t, is x_(2)/(2b), where x_(2)=e2 dot x. The even part is

\[
 \frac{|b x_{(1)}+a x_{(2)}|-|b x_{(1)}-a x_{(2)}|}{4ab},
\]

whose absolute value is at most |x_(1)|/(2a), by the reverse triangle inequality after changing the sign in the second absolute value. Odd and even parts are orthogonal under a symmetric input law. Since E[X_i^2]=1/d,

\[
 \frac1{4db^2}\le R_{\rm two}\le\frac1{4db^2}+\frac1{4da^2},
 \qquad \theta^2R_{\rm two}\to1/d.
 \tag{8}
\]

This independently re-derives the earlier singular coefficient. Together with the pair-angle density proportional to sin(theta)^(d-2), it gives the same near-zero moment condition q<(d-1)/2. The exact two-point formula is independently checked by scalar quadrature in verify_three_point.py.

## 2. Reducing dual pricing to the plane

Write z=p e1+q e2+z_perp. The dual function depends only on p,q and is positively homogeneous. A bound on the planar unit circle gives the same bound for p^2+q^2<=1, hence for every ambient unit z. Equality at absolute value one requires p^2+q^2=1; consequently all exposed atoms lie in the plane. In what follows p^2+q^2=1.

If q<=0, the first pair's projections obey z dot x1<=z dot x2. There are only three activation possibilities: both active, only x2 active, or neither active. If q>=0, the possibilities are both active, only x1 active, or neither active.

## 3. Positive third label

Take k=L/2 and

\[
 \lambda=(1/s+k,-1/s,k-1/a).
 \tag{9}
\]

Here k>0, ak<1, and -1<k-1/a<0. Indeed a>sqrt(3)/2, 1/sqrt(3)<k<1/sqrt(2), so 1/a-k<2/sqrt(3)-1/sqrt(3)<1, and ak=sqrt((1-b)/2)<1.

For q<=0, the third atom vanishes, and

\[
 g_\lambda(z)=\Delta(z)/s+k\sigma(z\cdot x_1)\ge-1.
\]

Equality forces Delta=-s and sigma(z dot x1)=0, so z=v. For an upper bound, if x1 is inactive then g<=0. If it is active, both pair points are active and

\[
 g_\lambda(z)=ak p+(1/a+bk)q\le ak<1.
\]

Here p<=1, q<=0, and 1/a+bk>0.

For q>=0, Delta>=0, hence

\[
 g_\lambda(z)\ge(k-1/a)q\ge k-1/a>-1.
\]

For an upper bound put

\[
 r=\lambda_1x_1+\lambda_2x_2+\lambda_3e_2
   =ak e_1+k(1+b)e_2=W/L.
 \tag{10}
\]

The last equality follows from L^2=2/(1+b) and a^2=1-b^2. If both pair points are active, g=r dot z<=1. If only x1 is active, x2 dot z<=0 and lambda2<0, so g<=r dot z<=1. If neither is active then g=(k-1/a)q<=0. Equality at +1 requires z=r. This point is strictly in the both-active region: r dot x2=(1-2b)/L>0 and r dot x1=1/L>0, while r dot e2=1/L>0. We have proved dual feasibility and shown that the only signed equality atoms are +r and -v.

Now W dot x1=1, W dot x2=1-2b>0, W dot e2=1. Also v dot x1=0, v dot x2=s, and v dot e2=-a. Therefore (1) interpolates all three labels. Its unit-atom coefficients are L and -C_+. Its cost equals the dual value:

\[
 \lambda\cdot(1,-1,1)=2/s+L-1/a
 =L+\frac{1-b}{ab}=L+C_+.
\]

For any minimizer equality in (7) leaves only +r and -v. The constraint at x1 fixes the positive total coefficient as L; the constraint at x2 then fixes the negative total coefficient as -C_+. Thus every minimizer induces (1).

## 4. Negative third label

Take

\[
 \lambda=(1+1/s,-1/s,-1/a).
 \tag{11}
\]

For q<=0,

\[
 g_\lambda(z)=\Delta(z)/s+\sigma(z\cdot x_1)\ge-1,
\]

with equality only at v. If x1 is inactive, g<=0. If it is active then both pair points are active and

\[
 g_\lambda(z)=a p+(b+1/a)q\le a<1.
\]

For q>=0, if both pair points are active then Delta=2bq and g=sigma(z dot x1)<=1. Equality occurs only at z=x1; this point is in that region because cos(theta)>0. If neither is active, p<=-(b/a)q implies q<=a. Thus g=-q/a>=-1, with equality only at z=-v.

In the remaining region only x1 is active. The arc runs from -v=(-b,a) to u=(b,a). Parametrize it as

\[
 p=-b\cos t+a\sin t,\quad q=a\cos t+b\sin t,
 \qquad 0\le t\le\theta.
\]

Then z dot x1=sin(t), and

\[
 g_\lambda(z)=-\cos t+(1+\cot\theta)\sin t.
 \tag{12}
\]

Its derivative is sin(t)+(1+cot(theta))cos(t)>0 throughout this arc. Its endpoints are -1 and sin(theta), respectively. It stays in [-1,1], attaining -1 only at -v and never attaining +1. The only signed equality atoms of (11) are therefore +x1, -v and -(-v).

The three atoms have sample vectors

\[
 (\sigma(x_1\cdot x_i))_{i=1}^3=(1,\cos\theta,b),\quad
 (\sigma(v\cdot x_i))_{i=1}^3=(0,s,0),\quad
 (\sigma(-v\cdot x_i))_{i=1}^3=(0,0,a).
\]

Consequently (2) interpolates: its second value is cos(theta)-(a/b)s=-1, and its third is b-Da=-1. Moreover

\[
 1+C_-+D=1+\frac1{ab}+\frac1a
 =\lambda\cdot(1,-1,-1).
\]

The identity uses a/b+b/a=1/(ab). Thus (7) proves optimality. The displayed triangular sample-value matrix fixes all three coefficient totals, proving uniqueness as a function.

## 5. Exact risks and two independent leading-term checks

For unit vectors making angle beta, normalized spherical integration gives

\[
 K_d(\beta)=E[\sigma(r\cdot X)\sigma(t\cdot X)]
 =\frac{\sin\beta+(\pi-\beta)\cos\beta}{2\pi d}.
 \tag{13}
\]

One derivation takes a standard Gaussian G=radius times X. Its radius is independent of X and E[radius^2]=d. In the plane of the vectors, the Gaussian polar angle is uniform and its squared planar radius has mean 2. The common positive interval is [beta-pi/2,pi/2], and the product expectation is (1/pi) times the integral of cos(phi)cos(phi-beta) on this interval. Product-to-sum integration gives the numerator in (13) divided by 2pi; division by d proves the formula. In particular K_d(0)=1/(2d), K_d(pi/2)=1/(2pi d), and K_d(pi)=0.

For (1), W dot v=-(1-b)/a, so (W/L) dot v=-sqrt((1-b)/2). Squaring the two-unit representation and using (13) gives (3). For (2), x1 is perpendicular to v and -v, and the two opposite v atoms have disjoint positive supports. Squaring gives (4).

For the first leading-term derivation, C_+ theta and C_- theta both tend to 2, v tends to -e2, and L,D remain bounded. ReLU is 1-Lipschitz, so uniformly on the unit ball

\[
 |\theta C_\pm\sigma(v\cdot x)-2\sigma(-e_2\cdot x)|
 \le|\theta C_\pm-2|+2\|v+e_2\|\to0.
\]

All remaining terms in theta f vanish uniformly. This proves the first part of (5); integrating the squared limit gives 4E[sigma(-X2)^2]=2/d. Alternatively, in (3)--(4) only the term C_\pm^2/(2d) contributes after multiplication by theta^2. This recovers the same constant independently.

The odd part of any homogeneous atom representation is (sum gamma_j z_j) dot x /2. For f_+, its vector sum is

\[
 W-C_+v=(0,1/b),
\]

so its odd-part risk is exactly 1/(4db^2). For f_-, its vector sum is

\[
 x_1+(D-C_-)v
 =\left(\frac{b(1+b)}a,\frac1b-b-1\right).
\]

Its odd-part risk is the squared length of this vector divided by 4d. Multiplying either odd-part risk by theta^2 gives 1/d. The total coefficient is 2/d, and orthogonality of odd and even functions under uniform spherical measure therefore assigns coefficient 1/d to the even part as well. This explicitly rules out cancellation of the leading odd component in either case.

## Scope

The statements hold in every ambient dimension d>=2, because dual exposure forces all minimizing atoms into the two-dimensional sample span. The third sample lies at a fixed nonzero angle from the pair; its two possible bounded labels are both covered. The configurations are a special deterministic family, of measure zero under iid continuous sampling. There is no claim here about random triples, arbitrary additional constraints, penalized biases, a full-dimensional design, a GD-selected solution, or the n-to-infinity risk limit.
