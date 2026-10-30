SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B15, 2026-09-23T22:01:40Z.
attacking: a product-preserving grouped pivot/leaf receiver that tolerates dense cross-pair couplings, while keeping essential boundedness logically prior to continuity.

# Early checkpoint: grouped d-leaf determinant receiver

Let d>=2. Select 2d ORIGINAL coordinates, split as pivots P=(P_1,...,P_d) and leaves L=(L_1,...,L_d), and condition on all other original coordinates W=w. Suppose the selected physical quadratic block, in the (P,L) ordering, has the form

    [ C   M ]
    [ M^T 0 ]

with C arbitrary symmetric and M invertible. All coefficients involving W are arbitrary. Hence conditionally

Q_w(P,L)=P^T C P+2P^TML+alpha(w)^TP+beta(w)^TL+c(w).

The P_i and L_j remain independent cap-one variables. For fixed P=p the leaf output is an affine linear form

    a(p,w)^T L + q_0(p,w),   a(p,w)=2M^T p+beta(w).

Away from the null set on which all but at most one of the coefficients a_j vanish, this conditional law has a density. In every case with a(p,w) !=0, conditioning/convolution gives the interval bound

    P(Q_w in I | P=p) <= |I| / ||a(p,w)||_infinity.                 (1)

Indeed choose an index j with |a_j|=||a||_infinity; the scaled variable a_j L_j has density at most 1/|a_j|, and convolution with the independent probability law of the remaining leaves cannot increase L-infinity.

Now A_w=2M^T P+beta(w) has a d-dimensional density bounded by

    B = 1/(2^d |det M|),                                             (2)

because the product density of P is at most one and the affine Jacobian is 2^d |det M|. Thus, by layer cake,

E[1/||A_w||_infinity]
 = int_0^infinity P(||A_w||_infinity < 1/t) dt
 <= int_0^infinity min(1, B(2/t)^d) dt
 = d/(d-1) |det M|^{-1/d}.                                          (3)

The bound is independent of w and of every affine term. Integrating (1), then averaging W, gives the direct interval domination

    P(Q in I) <= [d/(d-1)] |det M|^{-1/d} |I|.                       (4)

Therefore the output has an essentially bounded density and

    ||p_Q||_infinity <= [d/(d-1)] |det M|^{-1/d}.                    (5)

No continuity, moments, support bounds, log-concavity, spectral-coordinate independence, or post-rotation product claim is used.

For d=2,

    ||p_Q||_infinity <= 2/sqrt(|det M|).                             (6)

This directly extends the newest fleet03/B15 sparse double-pivot branch from diagonal M to an arbitrary invertible 2x2 cross-coupling matrix, while allowing an arbitrary pivot block C. In the diagonal case M=diag(b,c), (6) improves the partner's p=q=2 estimate 4/sqrt(|bc|) to 2/sqrt(|bc|).

The constant 2 in (6) is sharp at M=I_2: for iid Uniform[-1/2,1/2], Q=2(P_1L_1+P_2L_2), each product term 2P_jL_j has density log(1/(2|t|)) on |t|<1/2, so

    p_Q(0)=int_{-1/2}^{1/2} log^2(1/(2|t|)) dt
          =int_0^1 log^2(1/u) du
          =2.                                                        (7)

Continuity is a separate after-the-height consequence. For almost every p, at least two coefficients a_j are nonzero; the sum of the corresponding scaled leaf densities is an L^1*L^infinity convolution and therefore lies in C_0. Its sup norm is dominated by 1/||a||_infinity, whose P-average is finite by (3). Dominated convergence then gives a conditional C_0 density after mixing P, and another dominated-convergence step mixes W. Thus this branch has p_Q in C_0 with the SAME height (5), but (5) was proved first without continuity.

Remaining gap: the leaf-leaf quadratic block being exactly zero is a real hypothesis. Small operator norm of a nonzero leaf block cannot simply be discarded for arbitrary unbounded rough inputs. A next extension must absorb that block before any moment-free perturbation argument.
