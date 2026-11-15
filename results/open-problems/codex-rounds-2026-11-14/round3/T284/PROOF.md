# Amplification with a vanishing loss of independent-set density

All logarithms without a subscript are natural. All probabilities include the solver's random bits. The graph model throughout is G(n,d/n), with d fixed.

## Theorem

Fix a rational d>0. Let k_n be a polynomial-time computable integer sequence with 1<=k_n<=n and k_n/n tending to a constant a>0. Suppose A is a randomized algorithm with a polynomial worst-case running time T(n). Write

    v_n = P[A(G) returns an independent set of size at least k_n],
    s_n = log(1/v_n),

where G has distribution G(n,d/n). Assume v_n>0 eventually and s_n=o(log n).

There is a single randomized polynomial-time algorithm B, independent of v_n, s_n, a, and the convergence rate, with the following property. For every fixed K>0, put

    D_{n,K} = ceil(4 d k_n(k_n-1)(s_n+K log log n)/(n log n)).    (1)

For all sufficiently large n, B returns an independent set of size at least k_n-D_{n,K}, with probability at least

    1 - (log n)^(-K) - exp(-n)
      - n^2 exp(-gamma d a^2 K n log log n/log n) - n^(-5),    (2)

where gamma=log 2-1/2>0. In particular D_{n,K}=o(n), and the probability tends to one.

The algorithm calls A at most n^2 ceil(log_2 n) times. Apart from polynomial bit arithmetic, its running time is

    O(n^2 log n (T(n)+n^2)).                                  (3)

For constant starting success v_n>=c>0, the loss in (1) is O_{d,a,c,K}(n log log n/log n), and failure in (2) is O((log n)^(-K)). No success-probability lower bound is supplied to B.

The statement concerns a vanishing density loss, not an exactly zero loss. It gives neither a barrier-crossing algorithm nor a hardness assumption for T284.

## Product-noise estimate

Let mu be a finite product probability measure with full support. For 0<delta<=1/2, let T_delta independently retain every coordinate with probability 1-delta and otherwise replace it by an independent sample from its marginal. If 0<=f<=1 and E_mu f=v>0, then

    E_mu[(T_delta f)^(-delta/2)] <= 1/v,
    mu{T_delta f<u} <= u^(delta/2)/v,     u>0.                (4)

Here is the analytic input and the deduction, including the sign of the negative exponent. Corollary 1.11 of Elchanan Mossel, Krzysztof Oleszkiewicz, and Arnab Sen, *On reverse hypercontractivity*, arXiv:1108.1210v5, PDF page 5, https://arxiv.org/pdf/1108.1210 , states that for products of simple semigroups,

    ||T_t f||_q >= ||f||_p
    whenever q<p<1 and t>=log((1-q)/(1-p)),                   (5)

initially for strictly positive f. The simple semigroup retains a coordinate with probability exp(-t). Thus T_delta=T_t for t=-log(1-delta).

Set r=delta/2, p=r, and q=-r. Since

    (1-delta)(1+r)=1-delta/2-delta^2/2 <= 1-r,

the required time condition holds. Apply (5) to f+z with z>0 and let z decrease to zero. The state space is finite, and T_delta f is strictly positive because every transition probability is positive. Consequently

    (E_mu[(T_delta f)^(-r)])^(-1/r)
       >= (E_mu[f^r])^(1/r) >= v^(1/r),

where f^r>=f on [0,1]. Raising to the negative power -r yields the first inequality in (4). Markov's inequality yields the second. The estimate is independent of the product dimension and its atom probabilities; in particular the Bernoulli marginal d/n is permitted.

## Algorithm

For n<=d or n<3, return the empty set. These finitely many sizes do not affect the theorem. Otherwise compute

    m=ceil(log_2 n),    M=n^2,    delta_j=2^(-j),  1<=j<=m.

Keep the largest valid set found, initially the empty set. For each j, run M trials. In a trial:

1. Form H from the input G by refreshing every vertex pair independently with probability delta_j. A refreshed pair is an edge with probability d/n. Other pairs retain their status in G.
2. Run A on H with fresh random bits. Verify the output in H. Reject invalid outputs and outputs smaller than k_n. Otherwise retain its k_n smallest-labelled vertices, giving I.
3. Inspect G[I]. For each internal edge, mark its smaller-labelled endpoint. Delete all marked vertices to obtain J. Keep J if it is larger than the stored answer.

Return the stored answer after all scales and trials. The set I is selected from H and A's random bits only. The original graph is inspected for repair afterward. Every internal edge loses an endpoint, so every J is independent in G. At most e_G(I) vertices are deleted.

## Reaching a successful solver output at one scale

Fix a scale delta=delta_j. Let mu_n be the law of G(n,d/n), and define

    f(H)=P[A(H) returns a valid independent set of size >=k_n | H].

The refreshed graph also has law mu_n. Thus E_mu_n f=v_n. Conditional on the input G, a trial passes step 2 with probability Q(G)=T_delta f(G), and the M trials at this scale are independent. Equation (4), with u=1/n, gives

    P_G[Q(G)<1/n] <= v_n^(-1) n^(-delta/2).                  (6)

On the complementary event, the conditional probability that none of the M=n^2 trials passes step 2 is at most

    (1-Q(G))^M <= exp(-M/n)=exp(-n).                         (7)

Neither estimate assumes stability of A or any relation among its outputs.

## Repair at one scale

Write X_e and Y_e for the edge indicators of G and H in a fixed predetermined trial. For p=d/n,

    P(X_e=1,Y_e=0)=p delta(1-p),    P(Y_e=0)=1-p,

and therefore

    P(X_e=1 | Y_e=0)=delta p.                                (8)

The pairs (X_e,Y_e) are independent across e. Conditional on the entire H, the original edges are still independent. A's random bits are independent of G conditional on H. Thus, conditional on a fixed successful H and these solver bits, I is a fixed k_n-set with no edges in H, and exactly

    X=e_G(I) has law Binomial(binom(k_n,2),delta d/n).         (9)

Put

    lambda=delta d k_n(k_n-1)/n,    R=ceil(lambda).

The mean of X is lambda/2. Its exponential moment satisfies

    E[2^X]=(1+delta d/n)^binom(k_n,2) <= exp(lambda/2).

If X>R, then 2^X>2^lambda. Markov's inequality gives

    P(X>R) <= exp(lambda/2-lambda log 2)=exp(-gamma lambda).  (10)

If X<=R, the repaired output has size at least k_n-R. The conditional estimate (10) is uniform over successful H and solver bits. Integrating gives the same bound for the event that this fixed trial succeeds at step 2 but loses more than R vertices. A union bound over the M predetermined trials bounds the probability of any such event by

    n^2 exp(-gamma lambda).                                 (11)

This union bound does not require unconditional independence among the trials. In particular, (9) is never asserted after conditioning on which trial first succeeds.

Combining (6), (7), and (11), the exact-sampling algorithm has, for every scheduled delta, failure probability at most

    v_n^(-1)n^(-delta/2)+exp(-n)+n^2 exp(-gamma lambda)        (12)

to find an independent set of size k_n-ceil(lambda). Returning the largest set over all scales can only improve this guarantee. There is no union over scales in (12): a single suitable scale is sufficient.

## Selecting a scale in the analysis

Fix K>0. Define

    beta_n=2(s_n+K log log n)/log n.

For sufficiently large n, beta_n is positive, tends to zero, is at most 1/4, and exceeds 2^(-m). The last assertion follows from 2^(-m)<=1/n and

    n beta_n >= 2 K n log log n/log n -> infinity.

The dyadic schedule consequently contains a delta with

    beta_n<=delta<2 beta_n.                                  (13)

For example, j=floor(log_2(1/beta_n)) works. The restrictions above ensure 1<=j<=m. This is only an existence argument in the analysis; B does not evaluate beta_n or v_n.

The first term of (12) is then at most

    exp(s_n-delta log n/2)
       <= exp(-K log log n)=(log n)^(-K).                    (14)

The repair loss satisfies

    ceil(lambda)
       <= ceil(2 beta_n d k_n(k_n-1)/n)=D_{n,K}.              (15)

When k_n/n->a>0, eventually both k_n and k_n-1 are at least a n/sqrt(2), since each ratio tends to a. Hence k_n(k_n-1)>=a^2 n^2/2. Using delta>=beta_n and s_n>=0 gives

    lambda >= (beta_n d a^2 n)/2
            >= d a^2 K n log log n/log n.                   (16)

Substitution of (14)--(16) into (12) proves (2) apart from finite sampling error. Since k_n<=n and s_n=o(log n),

    D_{n,K}/n <= 4d(s_n+K log log n)/log n +1/n ->0.         (17)

The repair term in (2) tends to zero faster than any fixed inverse power of n: its negative exponential rate divided by log n is a positive constant times n log log n/(log n)^2, which tends to infinity. This proves the asserted asymptotics in the exact-sampling model.

## Finite random bits and runtime

For every Bernoulli draw of parameter theta in steps 1, round theta downward to a multiple of 2^(-w), where

    w=10m.

Use a uniform w-bit integer and compare it with the corresponding integer threshold. Each draw has total variation error less than 2^(-w). Each trial uses at most 2 binom(n,2)<=n^2 draws. There are m n^2 trials, so the entire algorithm is coupled to its ideal version with disagreement probability at most

    m n^4 2^(-w) <= m n^(-6) <= n^(-5),                     (18)

where 2^m>=n and m<=n for n>=2. Solver random bits can be coupled identically; all trials are run even when a good output has already been found, so there is a deterministic upper bound on sampling operations.

The parameters d/n and delta_j are rational and the thresholds require O(log n) bits for fixed d. Thus the comparisons and all arithmetic have polynomial bit complexity. Processing trials successively gives (3), with a factor polynomial in log n for elementary bit operations. Adding the coupling error (18) proves the theorem for an ordinary randomized Turing algorithm.

## Consequence and limits at the sparse overlap barrier

Fix an integer d>1 and a rational epsilon>0. Suppose a polynomial-time solver finds at least theta n vertices with success n^(-o(1)), where theta=(1+epsilon)log(d)/d lies in (0,1). Choose polynomial-time computable integers k_n with theta n-2<=k_n<=theta n for all sufficiently large n, modifying finitely many initial terms to lie in [1,n]. Such a sequence follows by computing a rational lower approximation to theta within 1/n and taking the floor after multiplication by n. To see directly that the approximation takes polynomial time, put x=(d-1)/(d+1) and use log d=2 sum_{j>=0} x^(2j+1)/(2j+1). For fixed d, the tail after J terms is at most 2 x^(2J+1)/((2J+1)(1-x^2)); thus O(log n) rational terms suffice for error at most 1/((1+epsilon)n). The assumed solver succeeds at target k_n. The theorem gives an independent set of size

    theta n-o(n)

with probability tending to one. With constant starting success the loss can be bounded by O(n log log n/log n). For any fixed epsilon'<epsilon this exceeds (1+epsilon')log(d)n/d eventually, consistent with the earlier fixed-slack theorem; the new information is that the density loss tends to zero with a polynomial number of calls whose exponent is fixed.

The same corollary holds for any fixed polynomial-time computable theta in (0,1). Computability without a runtime bound would not suffice for this step. The principal theorem itself has no real-constant representation issue because k_n is specified as polynomial-time computable input data.

The argument does not yield ceil(theta n) vertices with high probability. It does not give o(n) loss from arbitrary success n^(-s) with fixed s>0, or failure O(n^(-L)) with o(n) loss. It uses no overlap-gap implication and no average-case hardness assumption. The original all-polynomial-time obstruction remains unresolved.
