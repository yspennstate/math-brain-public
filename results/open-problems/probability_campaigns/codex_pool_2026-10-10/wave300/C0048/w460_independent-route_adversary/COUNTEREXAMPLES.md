# Exact audit obstructions (independently derived; referee pending)

These refute proposed proof mechanisms, not C0048 itself.

## CEX1: a strictly positive finite wired/free gap may vanish

Fix real q>1, 0<p<1. On the path with L edges, let free mean no identifications and wired mean the two endpoints are identified. Put alpha=p/[p+q(1-p)] in (0,1). Under the free random-cluster law, edges are iid Bernoulli(alpha), because k=L+1-|omega|. Identifying the endpoints reduces k by one except on the all-open configuration. Relative to the free law, the wired law is therefore tilted by 1+(q-1)*1_{all L edges open}. Thus for every path edge e,

    phi_w(e open) = [alpha+(q-1)*alpha^L]/[1+(q-1)*alpha^L],
    phi_w(e open)-phi_f(e open)
      = (q-1)*(1-alpha)*alpha^L/[1+(q-1)*alpha^L] > 0.

The difference tends to zero as L -> infinity. For q=3,p=1/2, alpha=1/4. The finite gap is 1/4 at L=1 and 1/172 at L=4, while its limit is zero. This is an exact Potts/random-cluster example of an invalid finite-size implication; d=1 is outside the target's d>=3 and hence this does not disprove the target conjecture. The premise needed in d>=3 is a lower bound that survives the thermodynamic limit on a fixed finite event, with constants independent of the outer box.

## CEX2: an O(1/n) pressure discrepancy cannot be differentiated

Let Z_n^f(t)=exp(2*n*t)+2 and Z_n^w(t)=2*exp(2*n*t)+1, and write f_n=n^-1 log Z_n^f, g_n=n^-1 log Z_n^w. Their ratio is between 1/2 and 2, hence sup_t|f_n-g_n|<=log(2)/n. Both limits are 2*max(t,0). But f_n'(0)=2/3 and g_n'(0)=4/3 for every n. Both finite-volume pressures are analytic and convex. This is a finite-state two-phase model counterexample to an abstract limit/derivative interchange, not a claimed nearest-neighbor Potts realization.

Minimal repair: use convex tangent inequalities to place limiting state energies in the pressure subgradient interval, as in ATTEMPT.md L4. A proof of zero derivative gap instead requires differentiability of the limit at the point in question, or a separately justified derivative convergence estimate.

NEXT: Apply these exact obstructions to the paired proof's critical separation and limit steps; record only the steps actually present.
