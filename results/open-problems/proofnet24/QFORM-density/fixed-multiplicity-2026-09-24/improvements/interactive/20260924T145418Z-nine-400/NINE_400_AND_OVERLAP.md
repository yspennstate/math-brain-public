# Nine eigenvalues with constant 400; a sharper spectral-overlap inequality

Run: interactive-20260924T145418Z-nine-400.
Owner objective: QFORM-FIXED-MULTIPLICITY-AUDIT-20260924.
Status: complete written mathematical derivation, self-checked; the new constant-400 synthesis and spectral-overlap inequality await independent review. This is an interactive contribution, not a scheduled-worker sign-in.

## Sources and precise scope

Baseline: yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2, proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex, blob 183ccd294763214e6a707e8d4749ff9a8cf7006d.

The threshold-nine mechanism was already derived by account03/B04 in improvements/account03/B04/20260924T121940Z-account03-B04-fixedmult-audit-r1/REPORT.md, blob 054facef834d29927713c5d42a1f09a541c5644b. The current run reread that complete report and reconstructed the argument below. Do not credit this run with first obtaining the threshold nine.

Related later sources actually read: account01/B04 NINE_DIRECTION_2510.md, blob c1868ff091c7418fd284a533697beda5e9d38ee4; account01/B02 r13 IMPROVEMENT.md, blob fc3761b698b94a0332492b4ca5bf767c1ae9ddf3; account01/B01 S8_OVERLAP_ENTROPY.md, blob f26192df69448db629b4211d5ebc733efe315dd5.

The new contributions here are an elementary parameter/negative-potential improvement giving constant 400 at multiplicity nine, and an exact spectral-tail/overlap-volume inequality with a quadratic error, rather than the preceding square-root error. No theorem at multiplicity eight or three is claimed. No exhaustive priority claim is made.

# Theorem A

Let X have arbitrary independent real coordinates with probability densities bounded by K>0. Let A=A^T be arbitrary and b,c arbitrary. If the ninth largest eigenvalue modulus satisfies s_9(A)>=s>0, then Q=X^T A X+b^T X+c has a density and

    ||p_Q||_infinity <= 400 K^2/s.

There are no moment, smoothness, iid, support, sign, exact-rank, or leverage restrictions. The assertion is an essential density bound; global continuity is not needed.

## 1. Analytic inputs and reconstruction of the row-promotion receiver

Use the baseline Fourier convention fhat(t)=integral exp(itx)f(x)dx. The baseline proves, without specialized external dependencies:

(a) geometric rank-one Brascamp-Lieb;
(b) density <=e^(d/2) for any d-dimensional orthogonal projection of a cap-one product law;
(c) integral |fhat(t)|^p dt <=2*pi*sqrt(2e)/sqrt(p), p>=2;
(d) E|Z-a|^(-1/2) <=(2*pi)^(-1/2) integral |t|^(-1/2)|phi_Z(t)|dt;
(e) scalar-square conditional density <=|a_ii|^(-1/2)|z-R|^(-1/2);
(f) the definite-pair density bound pi/sqrt(D), and the indefinite-pair envelope

    p(z) <= D^(-1/2)[6+log_+(16 sqrt(D)/|z-v|)].                 (1.1)

All of these statements have proofs in the baseline. The parameter choices below do not alter them.

Here is the complete additional product-Fourier argument behind the threshold reduction. Partition original independent coordinates into H,I,J; H consists of k literal coordinates, with joint density at most one. Write

    Q=F(X_H)+2 X_H^T(M_I X_I+M_J X_J+beta)+R(X_I,X_J),

where R is quadratic and all affine terms are allowed. Assume M_J has row rank k. Let S=sqrt(det(M_J M_J^T)), with S=1 for k=0. If a_i is row i of the I-J crossing matrix of R, write a_i=c_i+lambda_i M_J with c_i orthogonal to row(M_J), and collect c_i in C. For ell>=1 define

    Z_ell=sum_{|T|=ell} det(C_T C_T^T)>0,
    w_T=det(C_T C_T^T)/Z_ell,
    alpha_i=sum_{T containing i}w_T.

Assume alpha_i<=1/2 for positive marginals; omit zero-marginal factors by bounding them by one. Put q=k+ell. Then

    |phi_Q(t)| <= min(1,B_{k,ell}|t|^(-q/2)),                  (1.2)

    B_{k,ell}=pi^(q/2) 2^(ell/4) e^((k+2ell)/4)
       (ell^ell/ell!)^(1/4) S^(-1/2) Z_ell^(-1/4).             (1.3)

### Proof, including the conditional L2 step

Push exp(itF)dP_H to X_H; its complex density a_t is pointwise dominated by the ordinary density, so ||a_t||_2^2<=1. Push exp(itR)dP_(I,J) to M_I X_I+M_J X_J; call the complex density mu_t. The ordinary projected law has a bounded density because M_J has full row rank and X_I is independent of X_J; hence mu_t belongs to L1 and L2. Fourier transformation in the hub variables and Plancherel give

    |phi_Q(t)|^2 <= (pi/|t|)^k ||mu_t||_2^2.                  (1.4)

To justify the last norm bound carefully, choose a nonnegative, smooth, compactly supported probability mollifier rho_delta on R^k and put K_delta=rho_delta*reverse(rho_delta). Conditional on X_I=x, denote the phase-weighted pushforward of X_J through M_J X_J by nu_{t,x}. Translation of this measure by M_I x does not change its mollified L2 norm. Jensen in the Hilbert space L2 gives

    ||mu_t*rho_delta||_2^2 <= E_(X_I)||nu_(t,X_I)*rho_delta||_2^2.

Expand the right side with independent copies X_J,X'_J. Its kernel is the nonnegative probability density K_delta(M_J(X_J-X'_J)). The pure I phase cancels. The pure J phase is independent of X_I and is removed only AFTER integrating over the original independent X_i. Thus, with D=X_J-X'_J,

    ||mu_t*rho_delta||_2^2
      <= E_D K_delta(M_J D) product_i |fhat_i(2t a_i D)|.      (1.5)

The D_j are independent cap-one differences. The estimate is for the mollified norm, not a premature assertion about the unmollified norm. For k=0 the same calculation is the usual one-bank Cauchy-Schwarz decoupling, with no kernel or hub Plancherel factor.

Apply weighted Holder with weights w_T to the finite measure K_delta(M_J D)dP_D. This measure need not have mass one; Holder is valid nonetheless, because sum_T w_T=1. Each selected factor has exponent 1/alpha_i>=2. The map

    D -> (M_J D,(c_i D)_(i in T))

has row Gram determinant S^2 det(C_T C_T^T), by orthogonality. Its density is bounded by e^(q/2)/(S sqrt(det(C_T C_T^T))) by (b) and a deterministic linear change of variables. For fixed hub output z, a_i D=c_i D+lambda_i z. The scalar Fourier-power estimate (c), at scale 2t, therefore bounds the T-integral by

    e^(q/2)[pi sqrt(2e)/|t|]^ell
      product_(i in T)sqrt(alpha_i)
      /[S sqrt(det(C_T C_T^T))].                             (1.6)

The kernel integrates to one in z. The entropy identity needed after Holder is

    H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!).  (1.7)

Indeed randomly order the ell elements of a w-distributed subset. The ordered tuple has entropy H(w)+log(ell!), each position has law alpha_i/ell, and entropy subadditivity gives (1.7). Subadditivity follows, for example, from nonnegativity of relative entropy with respect to the product of the marginals, itself a consequence of log u<=u-1. Only finitely many original coordinates occur here.

Since det(C_T C_T^T)=Z_ell w_T, the geometric mean of determinant and marginal factors in (1.6) is at most

    Z_ell^(-1/2)(ell^ell/ell!)^(1/2).

The resulting estimate is independent of delta. Letting delta decrease to zero in L2 (or using weak compactness and the distributional approximate-identity limit) proves the same bound for ||mu_t||_2^2. Combining with (1.4) proves (1.2)-(1.3). No random rotation is asserted to preserve independence.

If ell=0 and k=q, condition on leftover original coordinates outside H and J. Phase-weighted pushforward of the J bank through M_J X_J has L2 norm squared <=e^(q/2)/S. Plancherel then gives the terminal envelope

    |phi_Q(t)| <= min(1,pi^(q/2)e^(q/4)S^(-1/2)|t|^(-q/2)).   (1.8)

The envelope is uniform in the conditioning, so it also bounds the unconditional characteristic function.

### Removal of the marginal restriction

For any literal physical cross block M put E_q(M)=e_q(MM^T), the sum of q-row Gram determinants. If its canonical row marginals are all <=1/2, use (1.2) with k=0,ell=q. Otherwise select a physical row carrying more than half the volume mass, promote its original coordinate to H, and project the remaining row vectors orthogonally off its span. Gram-Schmidt gives the exact identity

    incident q-volume = squared selected-row volume * residual (q-1)-volume.

Repeat when a residual marginal exceeds 1/2. After k promotions, the product

    det(P_H P_H^T) E_(q-k)(C)

is greater than E_q(M)/2^k. There are at most q promotions. At a diffuse stage apply (1.2); at the terminal stage use (1.8). Each promoted hub is a literal original coordinate, so its joint density cap is one. Its couplings to other coordinates of the original left bank are retained in M_I, not discarded.

For q=3 the largest coefficient after Fourier inversion occurs at k=0, giving

    ||p_Q||_infinity <= C3 E_3(M)^(-1/6),
    C3=3 sqrt(2)e(9/2)^(1/6)<15.                            (1.9)

To check dominance explicitly, the k=0,1,2 coefficients after the worst 2^k mass loss are

    3 sqrt(2) e^(1-k/6) [(3-k)^(3-k)/(3-k)!]^(1/6),

and the terminal coefficient is 3 sqrt(2e). All are no larger than the k=0 value. The strict comparison C3<15 follows from e<11/4 and

    15^6 - 26244(11/4)^6 = 40788279/1024 >0.

For q=2 the same argument and (d), using integral min(1,B/|t|)|t|^(-1/2)dt=8sqrt(B), give

    sup_a E|Q-a|^(-1/2) <= C2 E_2(M)^(-1/8),
    C2=8 sqrt(e)2^(-1/8)<14.                                (1.10)

The other promotion branches have coefficients 8*2^(-1/4)*e^(3/8) and 8*2^(-1/4)*e^(1/4), both smaller. This is a half-potential estimate, not a rank-two bounded-density theorem.

## 2. A quarter-power constant five, with elementary arithmetic

The baseline deterministic cut plus regularized determinant proof gives, when L=||A||>0,

    sup_a P(|Q-a|<u) <= min(1,5(u/L)^(1/4)).                 (2.1)

Here is an elementary improvement of its loose constant16. In the off-diagonal branch, the exact Gaussian-smoothing coefficient is

    Cq=2^(5/8) pi^(-1/4) e^(3/8) Gamma(3/8).

On [0,1], e^(-x)<=1-x+x^2/2, and on [1,infinity), x^(-5/8)<=1. Therefore

    Gamma(3/8) <=8/3-8/11+4/19+e^(-1)
                 <8/3-8/11+4/19+3/8.

Use 2^(5/8)<8/5, pi^(-1/4)<10/13, and e^(3/8)<8/5. These follow from 3<pi<4, 8/3<e<3, and raising to integer powers. The resulting rational upper bound for Cq is

    (8/5)(10/13)(8/5)(8/3-8/11+4/19+3/8)
      =4.972150656...<5.

In the scalar-diagonal branch the baseline bound is min(1,4sqrt(u/L)), which is at most 2(u/L)^(1/4). Thus (2.1) holds in both branches. Layer cake gives, whenever L>=1,

    sup_a E log_+(1/|Q-a|) <= L0:=4+4log5.                   (2.2)

## 3. Two better potential estimates

First, for every d!=0,

    J(d):=int_(-1)^1 |x|^(-1/2)|x-d|^(-1/2)dx
      <= J0+2log_+(1/|d|),  J0=pi+4log2.                   (3.1)

By reflection take d>0. For d<=1 the exact integral is

    J(d)=pi+2asinh(1/sqrt(d))+2acosh(1/sqrt(d)).

The product (1+sqrt(1+d))(1+sqrt(1-d)) is at most4: the two square roots sum to at most2 and their product is at most1. Taking logarithms proves (3.1). For d>=1 the exact formula is 2asinh(1/sqrt(d))+2asin(1/sqrt(d)), decreasing in d, and its value at1 is less than J0.

Second, every quadratic polynomial in two independent cap-one original coordinates whose symmetric quadratic matrix has determinant modulus D>0 satisfies

    sup_a E|Q-a|^(-1/2) <16 D^(-1/4).                       (3.2)

For a definite pair its density is at most pi/sqrt(D). A probability density bounded by M has full half potential at most2sqrt(2M), by integrating min(1,2M/t^2) over t>0. This gives a stronger result than (3.2).

For an indefinite pair, center at the critical value v and scale output by sqrt(D). Formula (1.1) gives a unit-mass density h(z)<=6+log_+(16/|z|). For any center a, split the half potential at |z-a|=delta. The far part costs at most delta^(-1/2). On the near part, the integral against the translated logarithmic envelope is maximal at a=0: layer cake reduces this to the fact that two intervals of given lengths overlap most when centered together. For 0<delta<=16 the near part is at most

    4sqrt(delta)[8+log(16/delta)].

Take delta=1/64. The total is at most

    12+5log2<16,

since log2<4/5. Undoing the output scaling proves (3.2). The proof uses only pointwise-bounded Borel versions and nonnegative test functions/Tonelli, so the estimate can be conditioned and averaged uniformly in a random critical value. It is a full half potential; no extra tail term is needed.

## 4. Retune scalar pivots and pair pivots separately

Use the normalized parameters

    d=3/40  (scalar-pivot threshold),
    p=1/400 (two-coordinate determinant threshold),
    h=2/25, kappa=h^2=4/625.                                (4.1)

A pivot means either |A_ii|>=d or |det A_[i,j]|>=p. Without either pivot,

    |A_ii|<d,
    |A_ij|^2<p+d^2=13/1600<1/121,
    |A_ij|<1/11.                                           (4.2)

For k=1,2,3 the baseline interpolation argument, with these new constants, proves

    no pivot and s_(4k-3)(A)>=1 imply V_k(A)>=kappa^k.       (4.3)

For completeness: if V_k<kappa^k, choose a ratio drop V_(r+1)<kappa V_r with0<=r<=k-1. A first zero volume is handled by the preceding positive volume. If r=0, ||A||<d+h<1. Otherwise the volume-sampled disjoint interpolation produces A=D+R+E with rankR<=3r, D=0 on the2r seed coordinates, E zero diagonal, ||E||_F<=(r+1)h, and rankR_[L,L]<=r outside the seed. Rank perturbation forces at least r+1 entries of D of modulus at least1-epsilon in L, where epsilon=||E||_F. On those indices,

    |R_ii|>=1-epsilon-d,
    sum_(j!=i)|R_ij|<r(1/11+epsilon).

Their difference is at least 1-d-r/11-(r+1)^2h. It is positive for r=1,2, with exact lower bounds

    r=1: 1131/2200;
    r=2:   51/2200.

Thus the (r+1)-coordinate restricted block is invertible, contradicting restricted rank<=r. Symmetry is required of A, not of R or E. This proves (4.3).

A fair physical coordinate partition has expectation E E_k(A_IJ)=4^(-k)V_k(A), hence some cross block satisfies E_k(M)>=4^(-k)kappa^k. In particular

    E_k(M)^(-1/(2k))<=2/h=25.                               (4.4)

For k=3, (1.9) gives a no-pivot density bound <25*15=375. For k=2, (1.10) gives a no-pivot full half potential <14sqrt(25)=70 when s_5>=1.

## 5. Finish Theorem A

Normalize K=s=1 and assume s_9(A)>=1.

No pivot: (4.3)-(4.4) and (1.9) give density<375.

Scalar pivot: completing the square costs at most d^(-1/2), and its Schur complement S retains at least eight large eigenvalues. Its induced affine terms are arbitrary.

If S has no pivot, s_5(S)>=1 and the full half potential is<70. The density of the original Q is<70/sqrt(d)<280.

If S has a scalar pivot, the next Schur complement retains at least one large eigenvalue. Equations (3.1)-(2.2) give the inner truncated half potential <=d^(-1/2)(J0+2L0); its tail costs at most1. The outer scalar profile therefore gives

    ||p_Q||_infinity <=d^(-1/2)+(J0+2L0)/d<400.              (5.1)

Indeed d^(-1/2)<4, pi<4, log2<7/10 and log5<17/10 yield J0+2L0<142/5, so the right side is<1148/3<383. The logarithm bounds follow from positive exponential Taylor partial sums: degree3 at7/10 exceeds2, and degree4 at17/10 exceeds5.

If S has a two-coordinate pivot, (3.2) gives full half potential<16p^(-1/4). The outer scalar profile gives density<16p^(-1/4)d^(-1/2)<16*5*4=320.

A definite two-coordinate pivot of A directly gives density<=pi/sqrt(p)<80.

An indefinite two-coordinate pivot of A has determinant-D, D>=p. Its Schur complement retains at least seven large eigenvalues, so (2.2) controls its random critical value. Averaging (1.1) gives

    ||p_Q||_infinity
      <=p^(-1/2)(6+log16+L0)+1/e
      =200+80log10+1/e<392.5<400.                            (5.2)

Here D^(-1/2)log_+D<=2/e, log10=log2+log5<12/5 and e>2. The definite, indefinite, scalar and no-pivot cases exhaust all possibilities. Absolute continuity in the pivot cases follows from the conditional change-of-variables formulas; in the no-pivot case it follows by Fourier inversion.

For general K,s set Y=KX and Qtilde=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c. Then Q=(s/K^2)Qtilde and s_9(A/s)>=1. Density scaling proves Theorem A.

# Theorem B: a spectral-tail inequality for overlap volume

For an arbitrary real square matrix A (symmetry is not needed here), define V_r as the sum of squared minors on ordered disjoint r-row/r-column sets. For V_r>0 put

    W^cross_(r,1)(A)
      =sum_(S,T disjoint r-sets; det A_ST!=0)
         sum_(h outside S union T) det A_(S+h,T+h)^2.         (B.1)

The same h is used as the added row and added column. Singular seeds are excluded deliberately. With singular values padded by zeros, define

    T_(3r)(A)=sum_(j>3r) s_j(A)^2.

Then

    W^cross_(r,1)(A)+(r+1)^2 V_(r+1)(A)
        >= V_r(A) T_(3r)(A).                               (B.2)

This replaces the previous square-root loss by a quadratic loss in the interpolation error.

## Proof

Sample each nonsingular disjoint seed (S,T) with probability det(A_ST)^2/V_r. Define P=A[:,T]A_ST^(-1)A[S,:], L=(S union T)^c, E_LL=offdiag(A_LL-P_LL), zero elsewhere, D_hh=A_hh-P_hh on L and zero on the seed, and R=A-D-E. Interpolation gives rankR<=3r by the exact support argument: R-P is supported in rows T or columns S. Also E has zero diagonal. Therefore

    ||A-R||_F^2=||D+E||_F^2=||D||_F^2+||E||_F^2.            (B.3)

The best-rank approximation inequality gives T_(3r)(A)<=||A-R||_F^2. To verify it without a black box, project orthogonally onto the range of any rank-at-most3r matrix R. Its perpendicular projection annihilates R, so ||A-R||_F^2>=||(I-P)A||_F^2. The largest possible captured trace tr(PAA^T) among rank-at-most3r orthogonal projections is the sum of the largest3r eigenvalues of AA^T; expand the trace in an orthonormal eigenbasis to prove this, using weights in[0,1] summing to at most3r. Thus the uncaptured trace is at least T_(3r)(A).

The bordered determinant identity with the same external index in row and column gives exactly

    E_seed ||D||_F^2=W^cross_(r,1)(A)/V_r(A).                (B.4)

For distinct external row and column indices the volume-sampled skeleton count gives

    E_seed ||E||_F^2 <=(r+1)^2 V_(r+1)(A)/V_r(A).            (B.5)

This is an inequality, because singular deleted seeds may have nonsingular extensions. Average (B.3) and combine (B.4)-(B.5), proving (B.2). No bound on the entries, diagonal, dimension or condition number was used.

## Eight-eigenvalue consequence

If A is symmetric and s_8(A)>=1, then T_6(A)>=2. Taking r=2 gives

    W^cross_(2,1)(A) >=2V_2(A)-9V_3(A).                     (B.6)

In the no-pivot terminal chamber V_2>=kappa^2 and V_3<kappa^3,

    W^cross_(2,1) >(2-9kappa)V_2 >=(2-9kappa)kappa^2.        (B.7)

With the original baseline kappa=1/6400, the coefficient is12791/6400=1.99859375, improving the previously read coefficient5929/3200=1.8528125. With the new parameter kappa=4/625, it is1214/625=1.9424 and the absolute lower bound is19424/244140625.

This supplies stronger overlap mass, not an analytic density receiver for overlap packets. A positive uniform W bound alone is NOT promoted to a bounded-density theorem. The remaining eight-direction obligation is still a product-preserving estimate handling the shared coordinate in the overlap minor and removing the critical logarithmic loss.

## Additional attempts and boundaries

A maximum-determinant disjoint seed has interpolation coefficients bounded by one under a single-row exchange; consequently its completed diagonal is bounded by(r+1) times the largest entry. This suggests a3r+1 rather than4r+1 structural threshold. However maximum determinant selection does not automatically retain the volume-sampled Frobenius residual bound. Controlling each bordered minor separately introduces dimension dependence when summed. No such simultaneous selection lemma is proved here; it must not be treated as a threshold-seven theorem.

Likewise no independence of a spectral remainder, no replacement of eigenvalue count by cross-block rank without proof, and no pointwise single-coordinate quadratic oscillatory decay is used. The global original assumptions are preserved throughout Theorem A.

## Review request

Independently check (1.5), the heavy-row promotion constants, separate pivot thresholds(4.1), the full pair half-potential(3.2), the final scalar/pair alternatives, and the exact orthogonality identity(B.3). The new constant400 and Theorem B have not yet received two independent end-to-end reviews. Keep the 17-eigenvalue baseline unchanged; publish reviews and any lower-threshold proofs in separate immutable folders.
