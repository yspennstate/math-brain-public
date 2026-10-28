# Original positive-prime queue cost is unbounded on nonuniform dual tribes

All logs are base two. Let disjoint blocks X_j have widths w_j>=1, j=1,...,r, and write u_j=OR(X_j) as a zero/one indicator. Put epsilon_j=2^-w_j, p_j=1-epsilon_j, P=product p_j and f=2 product u_j-1. Its COMPLETE positive prime table consists of all conjunctions selecting one positive literal per block: a true implicant must force every OR clause, and minimality removes all other literals. Thus every prime has width r and actual rarity pi=2^-r.

Fix ANY positive fractional packing lambda on this table before sampling; no uniformity, optimization assumption or choice of ordered covers is imposed. For A contained in one block with |A|=k>=1, each prime meets at most one coordinate of A. The ROOT_COMPONENTS.md groups are the k individual coordinates, with S_i=pi sum_{e contains i}lambda_e<=pi by the ORIGINAL packing rows. Hence

    -log Q_*(A) >= r(k-1)-3k pi.                     (1)

This upper-bounds the FULL output mass before taking logarithms. Name aggregation, overlapping/repeated runs, arbitrary forest posteriors and final ambiguity cannot defeat the bound.

## Actual Boolean spectral calculation

On a single OR block, the empty indicator Fourier coefficient is p_j and every nonempty coefficient has magnitude epsilon_j. For every nonempty A lying entirely in block j,

    fhat(A)^2=4 epsilon_j^2 (P/p_j)^2,
    I_j=2 w_j epsilon_j P/p_j,  I=sum_j I_j.           (2)

These formulas follow independently by product Fourier expansion and physical pivotal counting. Summing (1) over the ACTUAL one-block spectral sectors and using sum_{A subset X_j}|A|=w_j 2^(w_j-1) yields

    C_*(f):=sum_{A nonempty}fhat(A)^2 log(1/Q_*(A))
      >= sum_j I_j (P/p_j)
                [r(1-2p_j/w_j)-3 pi].               (3)

Other sectors have nonnegative cost and are simply omitted in this LOWER bound. Even if (1) is negative for k=1 it remains a legitimate lower bound and is summed with its sign. Root conditioning has already been included; no negative log D is dropped.

## Dimension-independent route obstruction, including nonsymmetric tables

For ANY integer w>=4 take r=2^w and an ARBITRARY pattern w_j in {w,w+1}. Distinct widths give genuinely nonuniform physical read and prime incidence. All patterns are allowed, including the homogeneous dual-tribes endpoint. Since p_j>=1-1/r,

    P/p_j >=(1-1/r)^(r-1)>e^-1>1/3.

The first strict inequality follows from -ln(1-t)<t/(1-t); e<3 follows from its positive series. Also 1-2p_j/w_j>=1-2/w>=1/2. The bracket in (3) is positive. Therefore

    C_*(f)/I(f)>r/6-pi>r/7.                         (4)

The last inequality uses r>=16, pi=2^-r<1/4 and r/42>=16/42>1/4. Thus the infimum over ALL feasible positive prime weights and ALL fixed ordered covers has unbounded ratio, at least 2^w/7. This refutes a universal constant payment for the ORIGINAL positive-prime conditioned queue itself, not merely an outer fractional estimate or a poor reference retuning.

The family is nondegenerate: 1/4<P<2/3, hence Var(f)>3/4. To check the lower bound, ln P>=r ln(1-1/r)>-r/(r-1)>=-16/15>-ln4, using ln2>2/3. For the upper bound, each p_j<=1-1/(2r), so P<e^-1/2<2/3.

## The actual entropy remains influence-paid

This is NOT an FEI counterfamily. Normalize each indicator's squared spectrum by p_j to a probability law mu_j. It has empty mass p_j and total nonempty mass epsilon_j, distributed uniformly among its nonempty subsets. The product mu has empty atom P, and the nonempty spectrum of f is exactly 4P mu. Consequently

    H(f)=h2(Var f)+4P[H(mu)-h2(P)] <=1+4P H(mu).

Now H(mu_j)=h2(epsilon_j)+epsilon_j log(2^w_j-1)
<=epsilon_j(2w_j+log e)<epsilon_j(2w_j+3/2). Thus

    H(f)<=1+(4+3/w)I(f).

Moreover I>=2P sum_j w_j epsilon_j>w/4>=1, since P>1/4 and epsilon_j>=1/(2r). Hence H(f)<(5+3/w)I(f)<=23I(f)/4<6I(f). This proof uses exact product spectrum and elementary entropy inequalities, not an assumed FEI bound or an entropy absorption with coefficient greater than one.

## Consequence for the stated PI-J posterior bound

For any distribution eta_A on distinct actual partition-forest runs outputting A, Gibbs' identity gives E_eta[-log q_cond(run)]-H(eta)>=-log Q_*(A). The source forest proof bounds each run cost ABOVE by log D+K_ref|A|+B_lambda(A;run). Therefore

    v log D+K_ref I+E_A[E_eta B_lambda-H(eta)]>=C_*(f).

In particular the fully conditioned residual is at least (r/7-K_ref)I on this family. NO posterior entropy refund can make that original positive-prime PI-J expression uniformly influence-paid. The binary wrapper is nonnegative and does not repair it. This is a route obstruction to that exact representation statement, not to C020 over arbitrary representations and not to full FEI.

The homogeneous endpoint becomes ordinary disjoint-block tribes after output/coordinate negation, so choosing output polarity can bypass this obstruction. It remains OPEN whether polarity selection, nonprime regular gates or another complete reference gives a universal influence-paid code. The shortest next step is to test both polarities against the component criterion, rather than further optimize this now-refuted fixed-polarity prime route.
