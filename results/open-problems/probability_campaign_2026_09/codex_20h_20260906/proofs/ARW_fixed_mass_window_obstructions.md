# Fixed mass and the ARW window-variance questions

Status: author-checked scope counterexample only. No independent review or novelty claim. The intended mesoscopic hyperuniformity problems remain unsolved.

Source: Levine and Silvestri, *Universality Conjectures for Activated Random Walk*, arXiv:2306.01698v2, Conjecture 27 and Question 28, PDF pages 15-16. Corpus entries P0389 and P0390. The two questions concern different laws, but share the following necessary correction to the observation-window quantifier.

## Deterministic complement identity

Let T be a finite set with N sites, and let I_x be zero-one occupation indicators with exactly k occupied sites almost surely. For every B contained in T,

$$S_B=\sum_{x\in B}I_x=k-S_{T\setminus B},\qquad \operatorname{Var}(S_B)=\operatorname{Var}(S_{T\setminus B}).$$

Both counts are bounded by their respective window sizes. The variance bound for a variable in an interval of length a is a squared divided by four. Thus

$$\operatorname{Var}(S_B)\le\frac14\min\{|B|,N-|B|\}^2.$$

This proof uses only fixed total mass, which holds after every free-chain addition and throughout each fixed-particle-number wake chain.

## Proper boxes already contradict the unrestricted lower bound

Take d=1 and T the cycle with L vertices. Fix any positive subcritical density rho, and put k=floor(rho L). Take the proper interval B consisting of L-1 vertices. If x is the omitted vertex, S_B=k-I_x, so its variance is at most 1/4. It cannot be at least c(L-1) for any positive c independent of L.

Uniform free driving is translation equivariant. For the wake chain, the unique stationary law is translation invariant because the transition kernel commutes with translations. Therefore each single-site mean is rho_L=k/L in both ensembles, and the variance of this proper box is exactly rho_L(1-rho_L). The whole torus gives the even simpler value zero, but the proper interval shows that requiring merely a strict subset does not repair the claim.

At zero density the configuration is empty and has variance zero for every window, giving another boundary exception. The positive fixed-density argument above does not rely on that exception.

## Global cancellation is not mesoscopic hyperuniformity

Under any fixed-mass law,

$$\sum_{y\in T}\operatorname{Cov}(I_x,I_y)=\operatorname{Cov}(I_x,k)=0.$$

Consider, only as a comparison model, a uniformly chosen k-subset of T. For x distinct from y,

$$\mathbb E I_x=\frac{k}{N},\qquad\mathbb E I_xI_y=\frac{k(k-1)}{N(N-1)}.$$

For a window with b sites, expansion of the variance gives

$$\operatorname{Var}(S_B)=b\,\rho_N(1-\rho_N)\frac{N-b}{N-1},\qquad\rho_N=k/N.$$

When b grows but b/N tends to zero and rho_N tends to a number strictly between zero and one, this is asymptotic to b times rho(1-rho). Therefore exact finite-volume covariance cancellation is compatible with volume-order mesoscopic fluctuations. Passing a finite-torus zero sum to an infinite-volume covariance sum requires additional uniform tail control.

## What remains

The natural next version restricts windows away from full volume, or takes the thermodynamic limit before the window limit. Neither restriction is asserted to have been prescribed by the source. Proving the ARW transition and its exponent in such a regime remains the actual mathematical problem. These elementary identities do not show that either actual ARW law is a uniform subset law, negatively associated, or hyperuniform.

## Second check

An exact rational enumeration of all k-subsets for small N independently checks the comparison variance and complement formula. The enumeration is a finite arithmetic control, not evidence that an unbounded ARW conjecture is solved. Its receipt is in ARW_window_exact_controls.json.
