# Independent checks

All checks are analytic. No numerical evolution, eigenvalue estimate,
or positive-time far-tail assertion is used.

## 1. The preceding result holds

For round 4's shear, independently integrate its two Gaussian kernels:
\[
 \begin{split}
 h(w)&=\mathbb E_V K(1,V)K(V,w)\\
 &=\frac{e^{-(1+w^2)/2}}{2\sqrt3}
   \left[e^{(1+w)^2/6}-e^{(1-w)^2/6}\right]\\
 &=\frac{e^{-(1+w^2)/3}}{\sqrt3}\sinh(w/3).
 \end{split}
\]
Thus its residual is exactly \(g-\eta h\). The ratio
\[
 h/g=\frac{e^{(1+w^2)/6}}{\sqrt3[1+2\cosh(2w/3)]}
\]
starts at \(e^{1/6}/(3\sqrt3)<1\) and diverges. Its derivative has
the sign of N in PROOF.md (27), whose second derivative in (28) is
positive and whose derivative at zero is 1/3. Hence it increases
strictly and \(g-\eta h\) has one positive zero for \(0<\eta\leq1\).

The conditional Gaussian formula for the proximal law is
\(a\mid w\sim N((g-\eta h)(w)/\lambda,1)\). Its folded marginal
is \(q(r)\propto\exp((g-\eta h)(r)^2/(2\lambda^2))\gamma_+(dr)\).
Let A,B be the positive lobe heights and \(M=\max(A,B)\).
For a bridge containing its zero, the minimum-energy cutoff satisfies
\(u'=-1/(I q)\), where \(I=\int_{\rm bridge}1/q\).
Direct Cauchy–Schwarz proves its energy is \(1/I\).
Elementary upper and lower exponential integral bounds give
\[
 \lambda^2\log I\to M^2/2,
 \quad\lambda^2\log q(\text{left well})\to(A^2-M^2)/2,
 \quad\lambda^2\log q(\text{right well})\to(B^2-M^2)/2.
\]
Its variance is at least the product of those well masses. Therefore
the upper Rayleigh exponent is
\[
 -M^2/2-(A^2+B^2-2M^2)/2=-\min(A^2,B^2)/2.
\]
The cutoff depends on \(|w|\), so it is invariant under simultaneous
sign reversal. This reproduces round 4's main restricted-gap claim,
using the optimal bridge rather than its linear cutoff.

The KL and moment formulas also follow directly from the conditional
shift \(a\mid w\sim N(\eta g(w),1)\): they are
\(\eta^2J/2\) and \(2+\eta^2J\). Here
\(J=h(1)=(e^{-1/3}-e^{-1})/(2\sqrt3)\), giving an independent check
of the squared-g integral. The conditional predictor is \(\eta H\),
and its risk change is \(-\eta J+\eta^2\|H\|^2/2<0\) for the
stated range. No error in the earlier result was found.

## 2. Initial density derivative, independent of the input calculation

The risk part of the initial Fokker–Planck equation is
\(-\partial_a(g(v)\pi)-\partial_v(ag'(v)\pi)\). The OU part is
zero because \(\pi\) is its invariant law. Thus, in the weak sense,
\[
 \dot\rho_0(a,v)=a\ell(v)\pi(a,v),\qquad
 \ell(v)=g(v)+vg'(v)-g''(v).
\]
Direct differentiation of g gives
\[
 \begin{split}
 g''(v)&=e^{-(1+v^2)/2}[v^2\sinh v-2v\cosh v],\\
 \ell(v)&=e^{-(1+v^2)/2}
 [(1-2v^2)\sinh v+3v\cosh v].
 \end{split}
\]
Since \(\mathbb E A^2=1\), this yields
\(\dot f_0(x)=\mathbb E\ell(V)\sin(Vx)\).
Also \(\ell\gamma=g\gamma-(g'\gamma)'\), so
\[
 \mathbb E\ell(V)k(V)=\mathbb E[g(V)k(V)+g'(V)k'(V)]
\]
for the bounded smooth kernels used here. Taking k to be the sine
feature recovers both terms in PROOF.md (15).

For a second evaluation of D without differentiating h, put
\(A(s)=\mathbb E e^{-V^2+sV}=e^{s^2/6}/\sqrt3\).
The direct kernel calculation gives
\[
 \begin{split}
 D(w)&=\mathbb E\ell(V)K(V,w)\\
 &=\frac{e^{-(1+w^2)/2}}2
 \{A(1+w)-A(1-w)-2[A''(1+w)-A''(1-w)]
                    +3[A'(1+w)-A'(1-w)]\}.
 \end{split}
\]
Here \(A'=sA/3\) and \(A''=(1/3+s^2/9)A\). The coefficients of
\(A(1+w)\) and \(-A(1-w)\), before the outside factor, become
\((10+5w-2w^2)/9\) and \((10-5w-2w^2)/9\). Expanding the two
exponentials gives precisely D in PROOF.md (5). In particular all
three coefficients 10, -2 and 5 are recovered independently.

The initial density derivative is signed and unbounded relative to pi.
It is used only as a weak derivative; \((1+ta\ell(v))\pi\) is not
asserted to be a probability density for positive t.

## 3. Risk slope by parameter-gradient dissipation

At initialization the KL first variation has zero gradient. Therefore
the initial risk dissipation is
\[
 -\dot R_0=\mathbb E_\pi|\nabla(ag(V))|^2
 =\mathbb E g(V)^2+\mathbb E g'(V)^2.
\]
This route is independent of evaluating D at w=1. The first term is
\(J=(e^{-1/3}-e^{-1})/(2\sqrt3)\). To evaluate the second, write
\[
 g'(V)^2=e^{-1-V^2}
 [\cosh^2V-2V\cosh V\sinh V+V^2\sinh^2V].
\]
Using the same A and its first two derivatives, the three terms sum to
\[
 e^{-1}\left[\tfrac12(A(2)+A(0))-A'(2)
                    +\tfrac12(A''(2)-A''(0))\right]
 =\frac{2e^{-1/3}+3e^{-1}}{9\sqrt3}.
\]
Adding J gives
\((13e^{-1/3}-3e^{-1})/(18\sqrt3)\), as required. It is larger
than the output-only shear dissipation J. This checks the loss factor
1/2 and the contribution of hidden-weight motion.

At frequency zero another check is
\[
 \frac{D'(0)}{g'(0)}=\frac{25e^{1/6}}{27\sqrt3}>0.
\]
Indeed \(D'(0)=25e^{-1/3}/(27\sqrt3)\) follows from the explicit
formula, while (23) and (26) in PROOF.md give the same ratio by limits.
The near-zero initial residual slope decreases even though its
far-frequency derivative is positive.

## 4. Sign and tangent bounds checked without monotonicity of Q

For the positive tail, the two exponential branches of D are
\[
 \frac1{18\sqrt3}
 \left[(10-2w^2+5w)e^{-(w^2-w+1)/3}
      -(10-2w^2-5w)e^{-(w^2+w+1)/3}\right].
\]
The second is exponentially smaller than the first, whose coefficient
is asymptotic to \(-2w^2\). This independently checks the negative
tail of D and the positive tail of the initial residual derivative.

For the uniform bound, no derivative of Q is needed. Directly from
its denominator,
\[
 Q(w)\leq\frac1{\sqrt3}e^{(w^2-4w+1)/6}.
\]
On \([0,5]\), the quadratic in the exponent is at most its value 6
at w=5, since a convex quadratic takes its maximum at an endpoint.
Hence \(Q\leq e/\sqrt3\). The independent inequalities
\(P\leq25/9\), \(P(3)>0\), \(P(5)<0\), and \(P'<0\) then give
the same constant \(C_*\). This checks that the tangent has no
negative positive-frequency lobe for the stated range of t.

## 5. Fourth moment by scalar Itô calculus

Write \(S=A^2+V^2\). Its scalar drift is
\(2(AG+AVG'-\lambda S)+4\lambda\), and its quadratic-variation
rate is \(8\lambda S\). Thus the drift of \((1+S)^2\) is
\[
 4(1+S)(AG+AVG'-\lambda S)+8\lambda+16\lambda S.
\]
This agrees with the two-dimensional generator in PROOF.md (34).
The upper bound \(AG+AVG'\leq1/2+S\) bounds it by
\(10+22S+4S^2\), which is at most \(20(1+S)^2\).
The Gaussian initial moment is \(1+2\cdot2+8=13\).
Both the coefficient 20 and the initial value 13 are thus rechecked.

## 6. Second generator by the product rule

At a fixed time let \(B_1=G'k'\), \(Q_1=k''-k-vk'\).
The product rule gives, separately,
\[
 \begin{split}
 L(Gk)&=\lambda(Gk)''+(aG'-\lambda v)(Gk)',\\
 L(a^2B_1)&=(2aG-2\lambda a^2+2\lambda)B_1
       +\lambda a^2B_1''+(a^3G'-\lambda a^2v)B_1',\\
 L(\lambda aQ_1)&=\lambda GQ_1+\lambda a^2G'Q_1'
       +\lambda^2a(Q_1''-Q_1-vQ_1').
 \end{split}
\]
Adding these formulas reproduces PROOF.md (41). The OU contribution
in \(L(ak)\) is \(\lambda a(k''-k-vk')\); there is one copy of
\(-k\). Initially its expectation vanishes, but it must be retained
when estimating the second time derivative.

For an arithmetic check of all remainder constants:

- Kernel derivatives through order four are bounded by
  \(8\min(|w|,1)\). The largest needed absolute input moment is
  \(\mathbb E|X|^5=8\mathbb E|X|<8\).
- The G derivative bound 4 includes \(\sqrt{\mathbb E X^6}=\sqrt{15}<4\).
- \(B_1,B_1',B_1''\) have bounds 32, 64, 128, from the binomial
  coefficients 1; 1+1; 1+2+1. The bounds for \(Q_1,Q_1',Q_1''\)
  are \(16q,24q,32q\), from \(2+|v|,3+|v|,4+|v|\).
- The diffusion line in (41) has coefficient
  \(64+128+128+32=352\). The next two lines have coefficients
  \(4(64+16)=320\) and \(4(64+64+24)=608\).
  Their sum is 1280 after increasing powers of q.
- \(\mathbb E q^4\leq9M_T\), giving \(1280\cdot9=11520\).
  Each of \(\dot G,\dot G'\) is at most \(48\mathbb E q^2\leq144M_T\).
  The explicit time derivative therefore costs at most
  \(8\cdot144\cdot3=3456\) times \(M_T^2\min(|w|,1)\).
- \(11520+3456=14976\), and the integral Taylor factor is 1/2.
  The stated remainder constant \(15000M_T^2\) is larger than
  \(7488M_T^2\), so there is slack.

Finally, inserting (11) into
\(C_Tt^2\leq e^{-(1+L^2)/2}/4\) verifies the logarithmic window
exactly. Its leading coefficient 2 follows from balancing the absolute
\(t^2\) error with the Gaussian \(e^{-w^2/2}\) lower bound.

## 7. Attempts to overextend the result

- A positive far-tail derivative at t=0 does not imply a positive
  far tail at each t>0. The permissible time from differentiability
  can depend on the frequency. The proof makes no exchange of limits.
- The absolute Taylor error can dominate g outside (11). It is not
  a relative estimate in the Gaussian frequency tails. The actual
  trajectory might still have remote negative lobes.
- No persistent single-peak geometry or restricted-gap estimate is
  obtained from positivity on a growing interval.
- Temperature drops out only at first order. The quantitative
  constant-temperature remainder is not an annealing theorem.
- Free-energy decrease and the solution/moment class are explicit
  hypotheses. No claim about general unbounded-network well-posedness
  is hidden in the use of a weak generator.
- The original risk-time question remains unanswered. Neither a
  positive initial dissipation nor an initial positivity window gives
  the small-risk convergence rate.
