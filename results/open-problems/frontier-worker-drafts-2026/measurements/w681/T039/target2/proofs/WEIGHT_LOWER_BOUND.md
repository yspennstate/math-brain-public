# Heilman's radial weight lower bound (153)

Source-attributed technical bound; the following proof expansion is unaudited.
Sources: arXiv:2608.00333v1, (153), and the pinned author implementation
plur_cert_positive.py, build_constants and positive_q_integrand.

For real b, define S(b)=4 integral_0^infinity u^2 exp(-u^2-2bu) du.
Equivalently, S(b)=sqrt(pi)(1+2b^2)exp(b^2)erfc(b)-2b.
For q>=0 put

H(q)=(pi/2) integral_0^(2/3) v(1-3v/2)sin(pi v) S(-q cos(pi v)) dv.

For 0<rho<1 set d=1-rho^2, alpha=rho/sqrt(d), kappa=rho^2/d,
j1=(9-pi sqrt(3))/(4pi^2), and

Jtilde(x)=alpha exp(-kappa x^2)[H(alpha x)+(j1/2)S(alpha x)].

This is J_+(x^2)/x for x>0, with its continuous extension at x=0.
Then, for every x>=0,

Jtilde(x)>=(6-pi)/(4pi^(3/2)) alpha exp(-kappa x^2)>0.

Indeed S(b)>0 for every real b, and S(b)>=sqrt(pi) when b<=0,
directly from its positive integral. For 0<=v<=1/2 we have
-q cos(pi v)<=0. All of the integrand defining H is nonnegative
on [0,2/3]. Consequently

H(q)>=(pi sqrt(pi)/2) integral_0^(1/2) v(1-3v/2)sin(pi v)dv
     =(pi sqrt(pi)/2)(6-pi)/(2pi^3)
     =(6-pi)/(4pi^(3/2)).

Since j1>0 and S(q)>0, the claimed bound follows. The displayed
integral is evaluated by integrating v sin(pi v) and v^2 sin(pi v)
twice by parts. This explains the analytic denominator floor in the
certificate even when a coarse interval enclosure would lose positivity.
This bound alone does not establish a full-operator or Hilbert-Schmidt
estimate; the tail calculation used for target 2 separately needs rho<1/2.
