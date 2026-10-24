# Explicit reflected-integral selector after a positive-support entrance

Status: deterministic PROVED lemma, subject to the independent review in agents/g02_audit.md. No claim that every initialized endpoint has reached these initial data.

Let a(t)<0 and c(t)>=0 be continuous, bounded coefficients on a compact interval, with a bounded away from zero. Consider q'=c+a theta, theta in H(q), q(0)=q0>=0. Put g=c+a and

w(t)=q0+integral_0^t g(s)ds,
k(t)=max(0,-min_{0<=s<=t}w(s)),
q(t)=w(t)+k(t).

Then this is the unique absolutely continuous solution. Indeed k is nondecreasing, increases only where q=0, and q'=g where q>0. At almost every time with q=0, q'=0 and g<=0, so theta=-c/a lies in [0,1]. Where q>0 set theta=1. The exceptional release times do not affect the a.e. differential equation. These are elementary running-minimum properties for an absolutely continuous w. Uniqueness follows from (q-tilde q)(theta-tilde theta)>=0 and a<0. This also shows the solution cannot enter the negative half-line from nonnegative initial data.

For the two-input endpoint assume 0<rho<1 and take a=z r_b<0, c=rho z r_p>=0. The other coordinate is fixed by

q_p(t)=q_p(0)+rho[q_b(t)-q_b(0)]+(1-rho^2)z integral_0^t r_p(s)ds.

In particular, if q_b(0)=0, q_p(0)>0, and z r_p>=0, then q_p(t)>=q_p(0)>0. Thus the supporting gate is self-consistently active for this prescribed residual phase. Repeated release and recapture are determined by the running minimum of the integrated drift, rather than the sign of the instantaneous drift alone.

If q=0 before t*, g(t*)=0, and g'(t*)=kappa>0, then for a sufficiently short interval after t*, q(t)=integral_t*^t g(s)ds=(kappa/2)(t-t*)^2+o((t-t*)^2). If instead g touches zero but stays nonpositive, q remains zero. Hence an isolated equality is not enough to infer release; transversal sign change is a sufficient local condition.

The exact-rational code/release_check.py tests a prescribed residual r1=-1+3t/4,r2=1,rho=1/2, with z_L=1+t/L, gamma=1, q_b0=0,q_p0=1. The limiting normal coordinate is (3/8)(t-2/3)_+^2 and q_p=1+q_b/2+3t/4. It is an endpoint consistency check, not a random finite-width network simulation. Every reported output is actually executed and saved.

Scope: the reflected integral treats the selected endpoint after entry with positive support. A microscopic original mark that is entirely dead, or races across a corner before support becomes macroscopic, is not selected by this formula. Prior run002440 demonstrated why collapsing all original marks to q0=0 can discard gamma-dependent entrance information. Those counterexamples remain in force.
