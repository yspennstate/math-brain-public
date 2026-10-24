C0041 — exact target supplied to the adversary before the proof packet

Fix an integer d >= 2 and l in the Euclidean unit sphere S^(d-1). Let U = {+e_i,-e_i: 1<=i<=d}. At each x in Z^d, omega(x,.) is a probability vector on U; these vectors are independent and identically distributed under P. There is a deterministic kappa > 0 such that P(omega(x,e)>=kappa for every x,e)=1. Conditional on omega, X is the nearest-neighbor Markov chain started at 0 with transition P_(0,omega)(X_(n+1)=x+e | X_n=x)=omega(x,e). Write P_0 = integral P_(0,omega) dP for the annealed law.

Assume P_0(lim_(n->infinity) X_n.l = +infinity)=1. Does it follow that P_0(liminf_(n->infinity) (X_n.l)/n > 0)=1?

Source: Drewitz–Ramirez, Selected Topics in Random Walks in Random Environment, arXiv:1309.2589v1, Open Question 2.20, section 2.6 (intake locator p.24). https://arxiv.org/html/1309.2589 . The source defines directional ballisticity using liminf positive speed. A deterministic vector limit v with v.l>0 is a stronger convenient conclusion and must be distinguished from the literal question.

The September 23, 2026 preprint Directional transience implies ballisticity in https://github.com/openai/math claims the stronger conclusion. Current status: claimed resolution pending independent proof review. Neither publication nor a formalization catalogue is an independent mathematical check.

No open neighborhood of transient directions, positive local drift, (T), (T'), or polynomial exit-rate assumption belongs to C0041's input. No conclusion about merely positive probability of transience is used.
