# Exact obstructions to incomplete SLE identification

2026-10-10. Mathematical proofs below; no counterexample to C0017 is claimed. Review pending.

## L4: one Cardy martingale does not select kappa=6

Fix kappa>=0 with kappa!=6 and 0<a<b<c. For a Brownian motion B, solve locally in the open region 0<X<Y the smooth-coefficient SDE

dX = [2/X-beta(X,Y)]dt-sqrt(kappa)dB,
dY = [2/Y-beta(X,Y)]dt-sqrt(kappa)dB,
beta(X,Y) = (6-kappa)(1/X+1/Y)/3,
X_0=a, Y_0=b.

Existence up to exit from a compact subset follows by the ordinary locally Lipschitz SDE existence theorem (or by smooth globally Lipschitz cutoffs followed by stopping). Define W_t=integral_0^t beta(X_s,Y_s)ds+sqrt(kappa)B_t. Then A=X+W and A'=2/(A-W); similarly Bmark=Y+W solves the real Loewner equation for b. Thus X,Y are the genuine shifted boundary marks for this driver.

Apply the derivatives in ATTEMPT.md to f(X,Y)=C(X/Y). Its finite variation coefficient divided by Df is

-beta+(6-kappa)(1/X+1/Y)/3=0.

Consequently C(X/Y) is a bounded local martingale on every nondegenerate localization, although W's bracket is kappa dt and its drift is beta, not the SLE_6 driver characteristics. Let Z=g_t(c)-W_t; while 0<X<Y<Z, the coefficient for the second observable C(X/Z), divided by its positive Df, equals

(6-kappa)(1/Z-1/Y)/3,

which is nonzero. This proves the necessity of two nondegenerate martingale tests for the identification lemma. It also gives a rigorous family behind the finite algebraic negative controls; testing just one equation really can admit an incorrect diffusion.

## L5: small uniform error does not give small total variation

For positive integers n, let e_n(k)=(-1)^k/n at times t_k=k/n^2, k=0,...,n^2. Interpolate linearly if a continuous path is desired. Its sup norm is 1/n, whereas the total variation of its n^2 consecutive increments is n^2*(2/n)=2n. Thus e_n converges uniformly to zero but its variation diverges. This blocks summing a per-step observable error without a summability or martingale argument. It does not block the bounded martingale transfer lemma L3.

## L6: marginal reflection symmetry does not imply zero conditional drift

Let Z be a fair sign and W_t=Zt. Every marginal is reflection symmetric and E[W_t]=0. In the natural filtration of W, any s>0 reveals Z, so for t>s, E[W_t-W_s|F_s]=Z(t-s), not zero. This is a counterexample to a symmetry-to-martingale inference, not a model of square-lattice percolation.
