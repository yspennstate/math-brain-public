# Compactly supported density pair correlations do not imply process mixing

2026-10-10. Derived after reading w549's G1–G6. This supplies a concrete obstruction at the hypothesis boundary of G3–G5, without repeating the shield calculation. Referee: w551, independent check pending. It is not a Riesz Gibbs state or a solution/counterexample to P0321.

Let B be a fair global bit and U uniform in [0,1)^2, independently. Partition R^2 into cells U+z+[0,1)^2, z in Z^2. Conditional on B, give the cells independent positive intensities Lambda_z, using either

    D0: Lambda=1/2 or 3/2, each with probability 1/2;
    D1: Lambda=1-1/sqrt(2), 1, or 1+1/sqrt(2),
        with probabilities 1/4, 1/2, 1/4.

Both laws have mean 1 and variance 1/4. Conditional on B,U,and all intensities, sample a Poisson process with intensity constant on each cell. This is a stationary simple locally finite Cox point process of finite positive intensity 1. Stationarity follows because translation changes the uniform cell phase and permutes the conditionally iid cell marks. Its intensity is bounded below by m=1-1/sqrt(2)>0 and above by 1+1/sqrt(2).

## Exact second-order formula

For distinct locations x,y, the factorial two-point density is E[Lambda(x)Lambda(y)]. If they lie in different cells, conditional independence given B,U and the common conditional mean 1 give value 1. If they lie in the same cell, the common second moment is 5/4. Averaging U therefore gives, for h=y-x,

    rho_T^(2)(h) = (1/4)(1-|h_1|)_+(1-|h_2|)_+.

In particular the truncated pair density is exactly zero whenever ||h||_infinity>=1. This uses conditional independence only where it is supplied by the construction; the unconditional cell laws share B.

## A local event keeps a positive covariance at every distant integer translate

Take A=[0,1)^2 and A_k=A+(k,0), for integers k>=3. Conditional on B,U, the two windows meet disjoint sets of cells, hence their restrictions are independent after also integrating the independent cell intensities. Their conditional vacancy probabilities are identical, q_B(U), because integer translation preserves all cell-intersection areas.

If v_j are the at most four nonzero intersection areas of A with the shifted grid, then sum v_j=1 and

    q_b(U)=product_j L_b(v_j),
    L_0(v)=e^(-v)cosh(v/2),
    L_1(v)=e^(-v)[1/2+(1/2)cosh(v/sqrt(2))].

For v>0, L_1(v)>L_0(v). The constant and quadratic terms of their even power series coincide; the quartic coefficient difference is 1/384, and every higher even coefficient difference is positive. Thus

    L_1(v)-L_0(v) >= e^(-v)v^4/384.

Choose an intersection area v_*>=1/4. Product expansion and L_0(v)>=e^(-3v/2) show

    q_1(U)-q_0(U)
      >= [L_1(v_*)-L_0(v_*)] product_{j != *} L_0(v_j)
      >= e^(-3/2)/(384*256) = e^(-3/2)/98304.

Boundary phases have fewer cells and satisfy the same bound. Let E be vacancy in A and H_k vacancy in A_k. The conditional independence and equality of conditional probabilities give

    P(E intersect H_k)-P(E)P(H_k)=Var(q_B(U))
      >= E_U Var_B(q_B(U)|U)
      >= e^(-3)/(4*98304^2) > 0.

Consequently alpha(A,A_k) is bounded below by the same positive constant for every integer k>=3. Fixed-window strong mixing already fails, despite EXACT finite-range pair-density correlations.

## The other geometric premises do not remove the example

The positive lower intensity gives V(t)<=exp(-m*pi*t^2) for every disk, even after conditioning on B,U,and the intensities. A homogeneous Poisson process of intensity m can be coupled as a subset. Every Voronoi cell of the Cox process is bounded almost surely: countably many rational disks/cones, with that homogeneous Poisson subset, supply competitors in every direction for every possible nucleus. Absolute continuity of Poisson locations on bounded sets, followed by a countable exhaustion, gives no three collinear or four cocircular nuclei; a fixed observation point has a unique nearest point almost surely.

Thus this example also meets w549's stationarity, finite-intensity, general-position, bounded-cell, and fast-void-tail premises. It fails the explicit alpha-mixing premise, as it must. It does NOT refute G3–G6. It proves that substituting a density two-point estimate for that premise is invalid.

The model is not claimed isotropic or ergodic. Uniformly rotating the entire construction would preserve compact support of the pair-density correlation and retain a hidden nonergodic regime, but that extension is unnecessary and no quantitative translated-square bound is claimed for it.

NEXT: Independently check the Cox two-point density and conditional vacancy computation; keep the alpha-mixing premise explicit when connecting w549's result to a Riesz state.
