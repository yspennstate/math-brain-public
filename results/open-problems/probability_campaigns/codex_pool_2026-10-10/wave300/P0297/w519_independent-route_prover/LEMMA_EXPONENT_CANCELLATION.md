# W519-L4: conditional clock-to-distance exponents cancel the thickness

Let gamma,xi>0 and Q,alpha be real with Q>alpha. Let a positive Radon measure mu have local Euclidean mass exponent gamma*(Q-alpha) at x. Suppose a positive metric observable delta(r) satisfies log(delta(r))/log(r) -> xi*(Q-alpha). Let T(r) be the logarithmic disk potential in W519-L2. Then

lim_{r down to 0} log(T(r))/log(delta(r)) = gamma/xi.

Proof. W519-L2 gives log T(r)/log r -> gamma*(Q-alpha). Divide by the assumed positive limit log delta(r)/log r -> xi*(Q-alpha). The common positive factor Q-alpha cancels. No probabilistic independence or conditioning product is used.

Conditional LQG interpretation only. If Q=2/gamma+gamma/2, alpha=gamma, xi=gamma/d_gamma, and both assumed local scaling laws hold for the actual metric observable, then the Euclidean clock exponent is 2-gamma^2/2 and the metric mean-exit exponent is gamma/xi=d_gamma. This does not compute d_gamma: the distance law already contains its unknown value through xi. The two local scaling assumptions for a random LQG-rooted point are not proved in this lemma.

Hardest remaining gap G1: prove an explicit value, as a function of gamma, of the actual metric scale exponent b_gamma=lim log D_h(x,partial B_E(x,r))/log r, under an appropriate typical-point law, using estimates that do not insert xi=gamma/d_gamma as input. The relationship b_gamma=xi*(Q-gamma), when available, merely restates the unknown parameter.

Source: owner-own-work algebraic reduction using W519-L2. Independent reviewer: w521, pending.
