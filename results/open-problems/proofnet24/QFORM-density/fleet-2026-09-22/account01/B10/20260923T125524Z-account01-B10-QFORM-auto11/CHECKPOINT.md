SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B10, 2026-09-23T12:55:24Z.
attacking: the punctured near-null physical hub: derive an exact coupling-adapted rank-two compression and isolate the coefficient that must interpolate to the already-paid exact-null mixed-Fresnel endpoint.

# Early substantive checkpoint


Let M be real symmetric invertible 3x3, r a unit vector, alpha=r^T M r, m=M r, s=||m||, v=m/s, and P=I-vv^T. Let K=PMP restricted to v^perp. In the orthogonal decomposition R v direct_sum v^perp, write

M = [[mu,k^T],[k,K]],   mu=v^T M v.

Set ell=(mu/(2s))v+(1/s)k (where k is identified with its vector in v^perp). Then the exact identity is

M = m ell^T + ell m^T + P K P.

Moreover

det K = alpha det M / s^2.

Indeed det K/det M=(M^{-1})_{vv}=v^T M^{-1}v=(m^T M^{-1}m)/s^2=alpha/s^2.

If every eigenvalue of M has absolute value at least one and |alpha|<1, M is indefinite. By Cauchy interlacing, the 2x2 compression K has at least one eigenvalue of absolute value at least one. Thus the exact-null endpoint alpha=0 is precisely the rank drop det K=0; the nonzero near-null collar creates one additional residual-curvature direction whose determinant currency is exactly alpha det M/s^2.

Now suppose A=RMR^T, R^TR=I_3, and an ORIGINAL hub row is u_0=sqrt(h)r. The leaf Gram is G_L=I-h rr^T. The physical hub-to-leaf coupling vector g satisfies the exact identity

||g||_2^2 = h m^T(I-h rr^T)m = h(s^2-h alpha^2).

Under the current true collar h>63/64, |alpha|<1/16 and sigma_min(M)>=1, this gives

||g||_2^2 > (63/64)(1-1/256)=16065/16384.

So the punctured collar is not losing hyperbolic hub coupling.

For the second exact geometry, put a=alpha/s, b=sqrt(1-a^2), q=(r-a v)/b in v^perp, and choose w perpendicular to v,q. Then r=a v+b q and the leaf Gram restricted to v^perp is exactly

G_perp = diag(theta,1),

theta=1-h b^2=(1-h)+h alpha^2/s^2.

Hence the new residual direction is simultaneously a low-leaf-energy direction in the near-coloop limit. In the basis (v,q,w), if

M=[[mu,k1,k2],[k1,A,B],[k2,B,C]],

then Mr=s v forces

A=-(a/b)k1,   B=-(a/b)k2.

Thus the q row of the residual compression collapses linearly in alpha/s at the exact-null endpoint, while the physical hub coupling stays order one.

The normalized residual determinant after whitening by the leaf Gram is

det(G_perp^(1/2) K G_perp^(1/2)) = theta alpha det M/s^2.

This identifies the precise interpolation debt: a proof cannot simply divide by this determinant, because it vanishes at alpha=0 even though the completed exact-null mixed-Fresnel theorem has a uniform bound there. A valid receiver must retain the order-one hub coupling and the vanishing residual direction jointly, rather than use small-random-perturbation or post-rotation independence.
