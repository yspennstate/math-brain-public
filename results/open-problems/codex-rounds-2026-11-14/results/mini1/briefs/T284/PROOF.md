# Amplifying sparse independent-set search with density slack

All logarithms are natural unless marked otherwise. An independent set is represented by its vertex list. No overlap-gap or complexity assumption is used in this result.

## Theorem

Fix rational constants d>0 and 0<b<a<=1. Suppose a randomized algorithm A runs in time T(n), polynomial in n, on every n-vertex input graph. Suppose that for all sufficiently large n,

    P[A(G) returns an independent set of size at least ceil(a n)] >= c n^(-s),

where G has distribution G(n,d/n), the probability includes A's random bits, and c in (0,1] and s>=0 are constants.

Then for every constant L>0 there is a randomized polynomial-time algorithm B which, on G(n,d/n), returns an independent set of size at least ceil(b n) with failure probability O(n^(-L)). The degree d is unchanged.

Here is an explicit bound in the ideal model of exact Bernoulli sampling. Write eta=a-b, choose any fixed rational

    0 < delta <= min{1/2, eta/(4 d a^2)},

and set

    r=delta/2,
    h=ceil((s+L)/r),
    M=n^(h+1),
    k=ceil(a n),
    kappa=(2 log 2 - 1)/4 > 0.

For n large enough that the hypothesis holds and

    n>d,   n>=1/a,   n>=2/eta,

the failure probability is at most

    c^(-1) n^(-L) + exp(-n) + M exp(-kappa eta n).                 (1)

The running time is O(M(T(n)+n^2)), apart from logarithmic bit-sampling overhead. Trials can be processed one at a time.

## Analytic input

Let mu be a finite product probability measure. Define T_t by independently retaining each coordinate with probability exp(-t), and replacing it by a new sample from its marginal otherwise. For a strictly positive function f and q<p<1, the reverse hypercontractive inequality

    ||T_t f||_q >= ||f||_p    when t>=log((1-q)/(1-p))            (2)

holds for these product operators, independently of the dimension and the atom probabilities. This is Corollary 1.11 of Elchanan Mossel, Krzysztof Oleszkiewicz, and Arnab Sen, *On reverse hypercontractivity*, arXiv:1108.1210v5, PDF page 5: https://arxiv.org/pdf/1108.1210 . For nonzero real u, the notation is ||f||_u=(E_mu f^u)^(1/u).

We need the following consequence, including when f vanishes. Suppose 0<=f<=1 and E_mu f>=v>0. Set t=-log(1-delta), r=delta/2, and Q=T_t f. Then

    E_mu Q^(-r) <= v^(-1),
    mu{Q<u} <= v^(-1) u^r  for u>0.                            (3)

Indeed,

    (1-delta)(1+r)=(1-delta)(1+delta/2)
                 =1-delta/2-delta^2/2 <= 1-r.

Therefore t>=log((1+r)/(1-r)), so (2) applies with p=r and q=-r. Apply it first to f+z for z>0 and let z decrease to zero. The state space is finite and every transition probability of T_t is positive, hence Q is positive because E_mu f>0. This justifies passage to the limit, including in the negative moment. Since x^r>=x for x in [0,1],

    (E_mu Q^(-r))^(-1/r) >= (E_mu f^r)^(1/r) >= v^(1/r).

Raising both sides to the negative power -r reverses the inequality and gives the first part of (3). On {Q<u}, Q^(-r)>u^(-r); Markov's inequality gives the second part.

## Algorithm B

On input G, repeat the following M times with fresh, independent random bits in every trial.

1. Form H by refreshing every unordered vertex pair with probability delta. A refreshed pair is made an edge with probability p=d/n, independently; every other pair retains its status in G.
2. Run A on H using fresh random bits. Verify its output in H. If it is not an independent set of size at least k, discard the trial. Otherwise retain its k smallest-labelled vertices, giving a set I. This truncation uses only H and A's bits.
3. Inspect the edges of G[I]. For each such edge, mark its smaller-labelled endpoint for deletion. Delete all marked vertices from I. The remaining set J is independent in G and has size at least k-e_G(I).
4. If |J|>=ceil(b n), return J.

If all trials fail, return the empty set. Every returned nonempty J has been verified to be independent in G.

## Reaching a successful trial

Let mu_n be the law of G(n,p), and define

    f(H)=P[A(H) returns a valid independent set of size at least k | H].

This is a function used in the analysis; B need not compute it. It lies in [0,1] and has mean at least c n^(-s). For fixed input G, the probability that a trial passes step 2 is

    Q(G)=T_t f(G).

The edge coordinates of mu_n form a product of biased Bernoulli spaces. Thus (3), with v=c n^(-s), implies

    P_G[Q(G)<n^(-h)] <= c^(-1) n^(s-hr) <= c^(-1) n^(-L).     (4)

Conditional on G, all M trial graphs and all solver bits are independent across trials. When Q(G)>=n^(-h), the conditional probability that every trial fails step 2 is at most

    (1-Q(G))^M <= exp(-M Q(G)) <= exp(-n).                    (5)

Equations (4) and (5) bound failure to reach any successful solver output. They do not require that two outputs of A be close.

## Repairing a successful output

Consider one fixed trial, before selecting any trial on the basis of its result. Let X_e and Y_e be the indicators of a pair e in G and H. Their joint law satisfies

    P(X_e=1,Y_e=0)=p delta (1-p),
    P(Y_e=0)=1-p.

Consequently

    P(X_e=1 | Y_e=0)=delta p.                                 (6)

The joint laws of the pairs (X_e,Y_e) are independent across e. Conditional on the entire graph H, the variables X_e therefore remain independent, with the conditional law in (6) on every nonedge of H.

The solver bits are independent of G conditional on H. Condition further on these bits and on a successful step 2. Then I is a fixed k-set independent in H, so all its pairs satisfy Y_e=0. Hence, exactly,

    e_G(I) | (H, solver bits) has law Binomial(binom(k,2), delta d/n). (7)

The conditioning here is on a fixed trial's H and solver bits. It is not conditioning on which trial is the first successful one.

Let mu=binom(k,2) delta d/n. Since k<=a n+1 and k-1<=a n,

    mu <= (delta d/2)(a^2 n+a) <= delta d a^2 n <= eta n/4,    (8)

where n>=1/a is used in the middle inequality. Also

    k-ceil(b n) >= eta n-1 >= eta n/2.                        (9)

Thus a successful solver output is certainly repaired to the target size whenever e_G(I)<=eta n/2.

For X with the binomial law in (7),

    E 2^X = (1+delta d/n)^binom(k,2) <= exp(mu).

Markov's inequality and (8) give

    P(X>eta n/2)
      <= exp(mu-(log 2)eta n/2)
      <= exp(-kappa eta n).                                  (10)

The constant is positive because log 2=integral from 1 to 2 of (1/x) dx>1/2.

The bound (10) holds uniformly for every H and solver-bit realization that passes step 2. Integrating those conditional bounds shows that, for each fixed trial, the unconditional probability of passing step 2 and failing to repair to the target size is at most exp(-kappa eta n). A union bound over the M trials bounds the probability of any such failure by M exp(-kappa eta n). It is valid even though the trials share G.

Outside this union event, any trial passing step 2 yields an acceptable answer in G. Combining this observation with (4) and (5) proves (1). Since h is fixed, M is polynomial, and its product with exp(-kappa eta n) is smaller than every fixed inverse power of n for all sufficiently large n. This proves the theorem in the exact-sampling model.

## Finite-bit implementation

The rational parameters make the claimed algorithm an ordinary randomized Turing algorithm. Sample each Bernoulli parameter theta by rounding theta to a multiple of 2^(-w), then comparing a uniform w-bit integer against the corresponding integer threshold. The total variation error per Bernoulli draw is at most 2^(-w). Each trial uses at most 2 binom(n,2) such draws. Coupling all ideal and rounded draws therefore gives total error at most M n^2 2^(-w).

Choosing

    w=(h+ceil(L)+5) ceil(log_2 n)

gives total error at most n^(-L-2). All comparisons and the computation of the rounded rational thresholds take polynomial time. A's own randomness is unchanged. This adds at most n^(-L-2) to the failure bound and preserves the theorem.

## Consequence at the overlap scale

Fix an integer d>1 and epsilon>0 with (1+epsilon)log(d)/d<1. If a polynomial-time algorithm has success probability at least c n^(-s) for all sufficiently large n at target

    ceil((1+epsilon)(log d/d)n),

then for each 0<epsilon'<epsilon there is a polynomial-time algorithm with probability 1-O(n^(-L)), for any prescribed fixed L>0, at target

    ceil((1+epsilon')(log d/d)n).

To avoid any real-constant representation issue, choose rational densities b,a satisfying

    (1+epsilon')log d/d < b < a < (1+epsilon)log d/d.

The assumed solver succeeds at density a; the theorem yields density b, which exceeds the desired output target.

Equivalently, for a fixed integer d, let D_poly be the set of rational densities achievable with an eventual inverse-polynomial success lower bound, and let D_high be those achievable with success tending to one. Then

    sup(D_poly union {0}) = sup(D_high union {0}).

One inequality follows from D_high being contained in D_poly (use success at least 1/2 eventually). For the other, every a in D_poly puts every rational b in (0,a) into D_high by the theorem, and taking suprema finishes the argument.

This equality concerns thresholds with arbitrarily small fixed density slack. It does not assert amplification at exactly the same density. It also does not upgrade a success lower bound that holds only on a subsequence into success for all sufficiently large n. No all-algorithm hardness assumption, or all-algorithm obstruction at log d/d, has been established here.
