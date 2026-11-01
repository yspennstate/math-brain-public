# P0220: explicit first-two law and a certified truncation of the known series

2026-10-10. Label: proof conditional on the existing patience-sorting stationary representation; awaiting w346 KEEP. No novelty or full-problem closure claim.

The cached Aldous problem page specifies drift dX_i/dt=X_i, with rate-one Poisson space-time left jumps. Constant-speed Rayleigh models are a different process. The previous P0220-A001 gives the established representation: first-row labels B=(1=b_1<...<b_k), independent unit-rate Poisson arrival times, and weights

    q_B=(1/b!)*sum_{lambda partition of b, lambda_1=k} f^lambda T(lambda,B), b=b_k,

where T counts standard tableaux with first row B. Conditional gamma gaps give the density exp(-x_k)*sum_B q_B product_{i>=2}(x_i-x_{i-1})^{b_i-b_{i-1}-1}/(b_i-b_{i-1}-1)!.

For k=2, a tableau with first row (1,b) must have shape (2,1^{b-2}): any box below its second column would need a label greater than b. There is exactly one such tableau and its shape dimension is b-1. Hence q_(1,b)=(b-1)/b!, b>=2. Put g=x_2-x_1. Then

    p(x_1,x_2)=exp(-x_2) F(g),
    F(g)=sum_{r>=0}(r+1)g^r/(r!(r+2)!)
        =I_1(2 sqrt(g))/sqrt(g)-I_2(2 sqrt(g))/g.

Here I_j(2 sqrt(g)) means the convergent series sum_{r>=0} g^{r+j/2}/(r!(r+j)!). The expression at g=0 is interpreted by continuity, F(0)=1/2. The density factors into exp(-x_1) times exp(-g)F(g). Thus X_1~Exp(1) is independent of the first gap. Its marginal consistency is integral_0^{x_2} F(g) dg=I_2(2 sqrt(x_2)); therefore P(X_2>x)=exp(-x) I_0(2 sqrt(x)), consistent with the old small-k calculation.

For every k, truncate the mixture at b_k<=M. Its omitted mass is exactly

    epsilon_{k,M}=P(B_k>M)=1/M! * sum_{lambda partition of M, lambda_1<k}(f^lambda)^2.

The equality uses consistency of restriction to labels <=M and the RSK count of uniform permutations of each shape. All omitted mixture terms are nonnegative and each conditional gamma density integrates to one. Hence the full density minus the truncated subdensity has L1 norm epsilon_{k,M}; every event's absolute probability error is at most epsilon_{k,M}. Normalizing the truncated mixture gives total variation at most epsilon_{k,M}, by the elementary mixture decomposition, using sup-event total variation.

For k=2 this is exactly 1/M!; for k=3 the finite partition sum can be computed exactly without trusting an asymptotic approximation. This turns the previously unquantified infinite series into an approximation with an exact error bound. It does not make large-k coefficient generation efficient.

Checks: compare hook dimensions to the independent removable-corner tableau recurrence; check sum dimensions squared=M!; check q_(1,b) sums to 1-1/M!; calculate finite partition sums for k=3 at M=8,12,16,20. Published small-k work predates this packet, so these formulas are consequences for the brain, not advertised discoveries.
