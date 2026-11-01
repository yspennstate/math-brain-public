# Independent inverse-covariance route for C0064

These are author proofs, awaiting independent review. They do not prove C0064.

## L1. A spectral floor from singleton clusters

For independent bond percolation on a finite graph, let T(x,y)=P(x<->y). For any complex vector f,

f*Tf = E[ sum over open clusters C of |sum_{x in C} f(x)|^2 ].

This follows by expanding the squared sums: each pair (x,y) contributes exactly when x and y are in the same cluster. Equivalently, assign independent fair signs to the clusters, conditional on the bond configuration, and take their covariance. Discarding the nonnegative terms from nonsingleton clusters gives

f*Tf >= sum_x P(C(x)={x}) |f(x)|^2.

With independent p-bonds and degree r(x), the singleton probability is (1-p)^{r(x)}: this product uses independence of the r(x) distinct incident bonds, not a multiplication of conditional connection probabilities.

The same identity holds for finitely supported f on Z^d, since only finitely many clusters meet its support. Thus f*T_pf >= (1-p)^{2d} ||f||_2^2. If chi(p)<infinity, tau_p is absolutely summable. Test with f(x)=exp(-ik.x) 1_{[-n,n]^d}(x)/sqrt((2n+1)^d). The quadratic form is sum_z tau_p(z) exp(ik.z) times the fraction of overlap of the box and its z-translate. This fraction tends to 1 for every fixed z and lies in [0,1]. Dominated convergence by tau_p in l1 proves

(1-p)^{2d} <= tauhat_p(k) <= chi(p), for every k and every 0<=p<1 with chi(p)<infinity.

The upper bound is the triangle inequality. In particular the Fourier transform is real, continuous, strictly positive, and pointwise invertible. This alone does not control how its inverse varies with k.

## L2. A signed direct-kernel coercivity criterion

Let d>=1 and let tau be a real, hyperoctahedrally invariant l1 function on Z^d with tauhat>0 and chi=sum tau>0. Assume an inverse convolution kernel A with tau*A=delta_0 and sum_x (1+|x|_1^2)|A(x)|<infinity. (This moment condition is a hypothesis; it is not inferred from L1.) Its inverse identity forces Ahat=1/tauhat; hence A inherits the same real, even, coordinate-permutation and sign-change symmetries. Define J(x)=-A(x) for x!=0, j=J(e1),

M = sum_{x: |x|_1>1} max(-J(x),0) |x|_1^2,
g = 2d*j - M,
E(k) = 1 - d^{-1} sum_i cos(k_i).

If g>0, then for every k,

tauhat(k) <= 1/[chi^{-1}+g*E(k)].

Proof. Absolute convergence and the inverse identity at k=0 give sum_x A(x)=chi^{-1}. Therefore

1/tauhat(k) = chi^{-1} + sum_{x!=0} J(x)(1-cos(k.x)).

The nearest-neighbour contribution is 2j sum_i(1-cos(k_i))=2d*j*E(k). The other positive J terms can be discarded for a lower bound. For x, choose a nearest-neighbour path of length n=|x|_1 from 0 to x. Telescoping exp(ik.x)-1 along its n steps, and using Cauchy–Schwarz, gives

1-cos(k.x) <= |x|_1 sum_i |x_i|(1-cos(k_i)).

The negative J tail consequently contributes in absolute value at most sum_i B_i(1-cos(k_i)), with B_i=sum_{|x|_1>1} max(-J(x),0)|x|_1|x_i|. Coordinate-permutation symmetry makes each B_i identical. Summing them gives M, so B_i=M/d. The tail is therefore at most M*E(k). Combine the bounds and invert the positive denominator.

This estimate keeps a signed tail. Replacing J by a nonnegative kernel without proof is invalid; L3 supplies a percolation counterexample to that shortcut.

## L3. Independent p-bond percolation on C4 has a signed inverse kernel

Label the vertices 0,1,2,3 cyclically, with four independent p-bonds, 0<p<1. Its connectivity covariance T is circulant, with first row (1,a,b,a), where

a = p+(1-p)p^3 = p+p^3-p^4,
b = 1-(1-p^2)^2 = 2p^2-p^4.

For adjacent vertices the direct bond and the other three-edge path give the first formula, with distinct-edge independence. For opposite vertices the two two-edge paths are edge-disjoint, which gives the second formula. The eigenvalues of T are lambda0=1+2a+b, lambda2=1-2a+b, and lambda1=lambda3=1-b. They are positive for 0<p<1, also following from L1.

The opposite-vertex entry of the inverse is

A(0,2) = (1/lambda0+1/lambda2-2/(1-b))/4
       = (2a^2-b-b^2)/[lambda0*lambda2*(1-b)]
       = p^4(1-p)^4/[lambda0*lambda2*(1-b)] > 0.

The last identity follows by direct polynomial expansion. Consequently J(2)=-A(0,2)<0: independent percolation and a positive connectivity covariance do not force a nonnegative direct kernel. At p=1/2, a=9/16, b=7/16, (lambda0,lambda2,lambda1)=(41/16,5/16,9/16), and A(0,2)=16/1845. This is a finite-graph counterexample to a general sign inference, not a counterexample to C0064 or to a dimension-specific lattice estimate.

## L4. The exact missing estimate and its conditional consequences

Suppose, for one fixed d>6 and some 0<p0<pc, the actual percolation inverse kernels A_p satisfy L2's moment condition and g_p>=g0>0 for every p in [p0,pc). Then L2 gives tauhat_p(k)<=1/[chi(p)^{-1}+g0 E(k)] in that interval. For p<=p0, coupling gives chi(p)<=chi(p0), hence tauhat_p(k)<=chi(p0)<=2chi(p0)/E(k) for E(k)>0. Thus an all-subcritical uniform infrared bound holds with A2=max(g0^{-1},2chi(p0)). A bound g_p>=c*p gives the stronger denominator form with A1=max(1,c^{-1}) on [p0,pc); below p0, chi(p)^{-1}+p E(k)<=1+2p0, so A1 may also be enlarged to chi(p0)(1+2p0).

To justify the critical endpoint, assume only that the all-subcritical bound above is established. For d>2, W(k)=A2/E(k) is integrable on the torus: E(k) is comparable to |k|^2 near its unique zero, k=0. The positive measures tauhat_p(k) dk/(2pi)^d have total mass tau_p(0)=1 and are bounded by W times Haar measure. Compactness gives weakly convergent subsequences, and domination by W survives the limit. For every x, their Fourier coefficient is tau_p(x), which increases to tau_pc(x) as p increases to pc. The last assertion follows because {0<->x} is an increasing union of finite-path events; each finite-path event depends on finitely many p-bonds, and a finite maximum argument proves continuity from below in p. Fourier coefficients determine a finite torus measure (trigonometric polynomials are dense in continuous functions). Thus all subsequences have the same limit: the spectral measure of tau_pc has an L1 density F_pc, with 0<=F_pc<=W almost everywhere. This is the critical Fourier interpretation used here. Pointwise convergence of the ordinary non-absolutely-convergent critical Fourier series is not asserted.

For d>6, the subcritical triangle sum equals the integral of tauhat_p^3 by absolute summability and convolution. It is at most integral W^3, finite because |k|^{-6} is locally integrable when d>6. The nonnegative triangle summands increase to their critical values, so monotone convergence proves the critical triangle condition. All these conclusions are conditional on the uniform gap; they do not establish it.

Single hardest missing step: prove g_p=2d J_p(e1)-sum_{|x|_1>1} J_p(x)^- |x|_1^2>=g0>0 (or a sharper coercivity bound) for the actual Z^d kernels, uniformly as p approaches pc, for d=7,8,9,10. Neither L1, L3, nor any finite-cycle computation supplies that step.
