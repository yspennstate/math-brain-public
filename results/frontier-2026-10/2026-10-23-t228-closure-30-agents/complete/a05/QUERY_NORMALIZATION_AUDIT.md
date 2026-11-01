# Audit: the query token needs its own stability condition

A05, 2026-10-23. This is a direct counterexample to an unrestricted reading of a source construction, not a novelty claim and not an objection to C002's different sequence-length normalization.

## Source and exact update

Primary source: Kang, Lee and Cheng, *Transformers Can Learn Posterior Predictive Distributions In-Context*, arXiv:2605.26713v1 / ICML 2026:

https://arxiv.org/html/2605.26713v1#S5

Equation (14) gives, for the query x as well as the context tokens,

    u_{l+1}(x) = (1-eta*s/s_x) u_l(x)
                    + (eta/s_x) sum_i k(x_i,x)(y_i-u_l(x_i)),
    s_x = sum_i k(x_i,x),

where s is the observation-noise variance. The text following (14) expressly includes the query in the tokenwise reciprocal-normalizer scaling. Immediately before this construction, the context spectral argument supplies the range 0<eta<2/(1+s) for unit-diagonal RBF kernels. That range need not stabilize the query token.

## A one-context RBF counterexample

Let n=1, k(x_1,x_1)=k(x_*,x_*)=1, k(x_1,x_*)=g with 0<g<1, and y_1=1. RBF realizes every such g by distance sqrt(2 log(1/g)); even a two-point compact domain suffices. Let both registers initialize at zero.

The context register a_l and query register b_l obey

    a_{l+1} = [1-eta(1+s)]a_l+eta,
    b_{l+1} = [1-eta*s/g]b_l+eta(1-a_l).                    (A)

The correct fixed points are

    a_* = 1/(1+s),     b_* = g/(1+s).

Put alpha=1-eta(1+s), c=1-eta*s/g. If c!=alpha, solving the recurrences exactly gives

    b_l-b_* = C c^l - eta/[ (1+s)(c-alpha) ] alpha^l,
    C = g(1-g)/[g(1+s)-s].                                (B)

For eta in (0,2/(1+s)), |alpha|<1. Choose 0<g<eta*s/2. Then c<-1. Excluding the single value g=s/(1+s) ensures c!=alpha, and C!=0 because g is strictly between zero and one. Consequently the query diverges although the context converges. In fact g<eta*s/2<s/(1+s) already excludes that exceptional value.

An especially transparent example is

    s=1, eta=1/2, g=1/10.

Then alpha=0, c=-4, a_l=1/2 for every l>=1, and

    b_0=0, b_1=1/2, b_2=-7/4, b_3=29/4, ...,
    b_l=1/20-(9/80)(-4)^l  for l>=1.

The correct query mean is 1/20. The variance-reduction recursion is g times the mean recursion here. Since the noisy marginal prior variance is 2, the uncorrected output variance is 2-g b_l and can eventually become negative. This is an algebraic failure of the query update, not just a loose error estimate.

## A simple stability repair, with a limited theorem

Replace every normalizer by its ridge-inclusive version

    r_i = sum_j k(x_i,x_j)+s,     r_x=sum_i k(x_i,x)+s.

Assume the kernel Gram entries and query cross-covariances are nonnegative, as for RBF. The context operator is R^{-1}(G+sI), R=diag(r_i). It is similar to a symmetric positive-definite matrix and is row stochastic, so its eigenvalues lie in (0,1]. Thus 0<eta<2 stabilizes the context update. The query homogeneous factor is 1-eta*s/r_x, which also has magnitude <1 because 0<s/r_x<=1. The forcing from the context converges geometrically, so the query converges too. The fixed points are unchanged because the positive normalizers cancel from their defining equations.

For an explicit common bound, if k(x_i,x_j)<=K and k(x_i,x)<=K, and 0<eta<=1, set

    q=1-eta*s/(nK+s) < 1.

The context error contracts in the R-weighted norm at rate <=q. The query obeys

    |e_x(l)| <= q^l |e_x(0)|
                   + [eta ||R^{-1/2}k_x||/r_x]
                       l q^{l-1} ||e_context(0)||_R.

The extra l factor explicitly covers a resonant forcing rate. This repair establishes convergence; it is not an implementation-count theorem or an optimal-rate claim. An architecture must actually expose/compute the ridge-inclusive normalizer, e.g. with an additional noise/sentinel contribution. One cannot silently treat reciprocal row sums as already available from arbitrary normalized attention.

## Other source precision checks

Theorem 5.3 of the source expressly gives a *sufficient* O(n log(1/epsilon)) depth condition for a constrained Richardson construction, and Remark 5.4 distinguishes it from more flexible transformers. Do not misreport it as a universal lower bound. Its proof C.3 displays a reversed logarithmic inequality and switches between a +2 and +1 condition-number denominator; the ordinary sufficient Richardson rate is easily repaired, but the query stability issue above is independent.

C002 uses (1/N_tok) sum ReLU(score) value, where N_tok is a fixed padded token count. It does not divide by an RBF row sum, and this counterexample does not apply to it.
