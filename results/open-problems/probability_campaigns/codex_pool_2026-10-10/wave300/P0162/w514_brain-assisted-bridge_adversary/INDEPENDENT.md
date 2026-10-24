# Independent record before paired proof access

Saved 2026-10-10. No w513 proof or attempt has been read.

Candidate exact target, pending primary-source recovery: for every n>=1 and every f:{-1,1}^n->{-1,1}, under uniform measure and the Walsh basis, a universal finite C should satisfy H(f)=sum_S hat(f)(S)^2 ln(1/hat(f)(S)^2) <= C I(f), where I(f)=sum_S |S|hat(f)(S)^2 and 0 ln(1/0)=0.

The simplest tempting bridge is false for arbitrary probability measures on subsets. Let q({i})=1/n and q(S)=0 otherwise. Then H(q)=ln(n), E_q|S|=1. The ratio diverges with n.

This is a bridge obstruction, not a Boolean counterexample. Were q a Boolean Fourier spectrum, f would have the form sum_i a_i x_i with every |a_i|=1/sqrt(n). But the coefficient of x_i x_j in f^2 is 2a_i a_j, nonzero for i != j. Booleanity requires f^2=1. Equivalently, its exact Fourier convolution constraints are sum_T hat(f)(T)hat(f)(T symmetric_difference U)=0 for every nonempty U. Any entropy argument replacing the signed coefficient vector with an arbitrary normalized subset law loses these constraints.

Next proof step: identify the actual retrieved theorem and compare all hypotheses with Boolean spectral realizability, then test whether its proposed bridge retains enough of these convolution constraints.
