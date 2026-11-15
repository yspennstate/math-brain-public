# Finite-depth comparison for regular-degree bands

T067-DEGREE-BAND-COMPARISON-001 v1. Status: proof (unaudited).
This is a standard Blackwell-comparison lemma; no novelty is claimed.

For the q-state symmetric Potts channel K_t=tI+(1-t)J/q with uniform
prior, let W_n(d,t) be the experiment consisting of all depth-n leaf
states of the regular d-ary broadcast tree, conditional on its root.
For integers1<=d<=D and0<=lambda<=eta<=1, W_n(d,lambda) is a Blackwell
garbling of W_n(D,eta), for every finite n. At n=0 the experiment is
the root state itself, and the garbling is identity.

Inductively suppose a root-state-independent kernel maps W_(n-1)(D,eta)
to W_(n-1)(d,lambda). In each of d selected strong branches apply this
kernel to the descendant observation. The resulting branch experiment,
conditional on its parent state, is K_eta W_(n-1)(d,lambda). Let rho be
the unconditional law of W_(n-1)(d,lambda) under its uniform state prior.
For eta>0, retain the branch output with probability c=lambda/eta;
otherwise replace it with an independent rho draw. Hide the choice flag.
The resulting root-conditional observation law is

  c K_eta W_(n-1)+(1-c)J W_(n-1)/q = K_lambda W_(n-1).

Discard the other D-d branches. All retention and replacement choices
are independent between branches and independent of the root; the
inductive kernels act separately on branches. Conditional independence
therefore gives precisely W_n(d,lambda). If eta=0 then lambda=0 and the
same conclusion follows by discarding the strong observation and drawing
the independent unconditional weak observation. These operations establish
a genuine stochastic kernel, not just an ordering of scalar moments.

Let p_w,p_s be the weak and strong root posteriors, realized with this
coupling. Conditional expectation gives p_w=E[p_s|Y_w]. Jensen implies

  E||p_w-u||^2 <= E||p_s-u||^2.

For q=3 this squared norm is exactly the signal x=E||3p-1||^2/9.
The root-conditional version E_1[p_1]-1/3 equals it by calibration and
permutation symmetry. Revealing a replacement flag would define a
different experiment and would not prove this exact channel identity.

In particular, fix an integer band[a,b] and eta>=1/sqrt(a). If a rigorous
upgraded BP calculation for W_N(b,eta) gives x_N<=r, the critical process
of every d in[a,b] has x_N<=r. Its later signals decrease. If a local
fixed-point exclusion lemma applies uniformly to that band on0<x<=r,
then each critical process is nonreconstructible. The limiting law is a
fixed point by the reverse-martingale and BP continuity argument written
in COMPENSATED-D89-001 Section3. Smaller positive lambda follow from
the same comparison with equal degree. The dominating envelope may be
supercritical; only its finite-depth signal bound is required.

This lemma supplies no successful finite-depth bound or new settled degree.
