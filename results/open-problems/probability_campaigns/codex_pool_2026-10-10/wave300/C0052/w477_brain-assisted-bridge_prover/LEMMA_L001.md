# L001: conditional fourth-moment witness

Let X_n converge in law to X. Suppose E X_n=0, E X_n^2=1, the family {|X_n|^4} is uniformly integrable, and liminf (3-E X_n^4)>=epsilon>0. Then X is centered, has variance one, and E X^4<=3-epsilon; consequently X is not Gaussian.

Proof. For k=1,2,4, use bounded continuous truncations of x^k, then control the discarded tails by uniform integrability of |X_n|^4. For the limiting variable, integrability and the same tail control follow by the portmanteau inequality applied to nonnegative continuous truncated tail functions. This gives convergence of the first, second and fourth moments. The claimed deficit follows. The fourth moment of N(0,1) is three. QED.

This is an elementary conditional reduction, not a proof of non-triviality for the 3D Ising model. The required deficit is the unresolved input. Referee: w479; independent check pending.
