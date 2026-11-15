# Amplifying independent-set search by changing vertex rows

All logarithms are natural. Graphs are simple and have vertex set [n]. A randomized algorithm uses independent fair bits and has a polynomial worst-case running time on every input. No complexity assumption is used.

## Theorem

Fix a rational d>0 and a polynomial-time computable sequence of integers 1<=k_n<=n. Let A be a randomized polynomial-time algorithm. Suppose there are constants c>0 and s>=0 such that, for all sufficiently large n,

    P[A(G) returns an independent set of size at least k_n]
        >= c n^(-s),       G ~ G(n,d/n).                         (1)

For every fixed L>0 there are a randomized polynomial-time algorithm B and a constant C_0 such that, for all sufficiently large n,

    P[B(G) returns an independent set of size
          at least k_n-ceil(C_0 sqrt(n log n))] >= 1-n^(-L).    (2)

Every output of B is independent in its input graph, including on failure. No positive limiting density for k_n is needed. The running-time exponent can depend on a fixed inverse-polynomial success lower bound and on L.

More precisely, choose integers S>s and ell>=max{1,L}. There is a universal constant C from the concentration theorem below such that the loss in (2) can be replaced by

    R_n = ceil(C sqrt(n log(4 n^(S+ell)))).                    (3)

The algorithm may depend on S and ell but does not compute the actual success probability in (1). The conclusion is an amplification implication, not an algorithm achieving a previously unknown independent-set density.

## Imported concentration theorem

Theorem 1.1 of Omid Etesami, Saeed Mahloujifar, and Mohammad Mahmoody, *Computational Concentration of Measure: Optimal Bounds, Reductions, and More*, arXiv:1907.05401v1, https://arxiv.org/pdf/1907.05401 , gives the following result. Given sampling access to a finite product measure with m blocks, membership access to an event of measure at least epsilon, and epsilon,delta>0, a uniform randomized algorithm maps a random input to that event within block Hamming distance C sqrt(m log(1/(epsilon delta))) with probability at least 1-delta. Its time is polynomial in the total representation length and 1/(epsilon delta). Theorem 3.2 and Remark 3.3 give the representation-length and product-input formulations. The theorem is used as a published result; its proof is not reproduced here.

## A deterministic repair lemma

For i=1,...,n-1, define row i of a graph G to be the vector

    row_i(G) = (1_{ {i,j} in E(G) } : j=i+1,...,n).

For graphs G and H, let

    D(G,H) = {i in [n-1] : row_i(G) != row_i(H)}.             (4)

Then G and H induce the same graph on [n] minus D(G,H). Indeed, if i<j and both endpoints are outside D(G,H), then i is outside D(G,H), so the two row-i entries for {i,j} agree.

Consequently, if I is independent in H, then

    J = I minus D(G,H)                                      (5)

is independent in G and has size at least |I|-|D(G,H)|. This statement holds for every pair of graphs and every I. In particular, H and I can be selected adaptively using G. No conditional distribution of edges is needed.

Equivalently, D(G,H) is the set of smaller endpoints of all edges in the symmetric difference E(G) triangle E(H). It covers every changed edge. Deleting this cover leaves no edge on which G and H disagree. This is a second description of the same repair operation.

## Making the sampling measure finite-bit

Put p=d/n. For n>=2 and n>d, define

    m_n = ceil(log_2 n),
    w_n = (S+ell+6)m_n,
    q_n = floor(2^(w_n) p)/2^(w_n),
    eta_n = binom(n,2) 2^(-w_n).                            (6)

For the finitely many sizes with n<=d, n<2 or q_n=0, B returns the empty set. Since d is fixed and positive, eventually 0<q_n<=p<1: the rounding error is below 2^(-w_n)<=n^(-(S+ell+6)), which is eventually smaller than d/n.

Let P_p and P_q be the graph laws with independent edge parameters p and q_n. Couple the graphs using one common independent uniform variable per pair and thresholds p and q_n. Each pair differs with probability p-q_n<2^(-w_n), so the union bound gives

    ||P_p-P_q||_TV <= eta_n
       <= (1/2)n^(-(S+ell+4)).                              (7)

Here total variation means the supremum of event-probability differences. The last inequality uses binom(n,2)<=n^2/2 and 2^(m_n)>=n.

For all sufficiently large n, (1) implies v_n>=n^(-S), since c n^(S-s)>=1 eventually. Couple the same solver tape on the two graphs. The solver-success event therefore has probability under P_q at least

    n^(-S)-eta_n >= (1/2)n^(-S) = epsilon_n.                (8)

This argument uses only an initial-distribution comparison. It does not approximate the concentration algorithm's individual adaptive sampling calls.

## The product space and its membership oracle

Choose a known polynomial r(n) bounding the number of fair bits that A reads on any n-vertex graph. Supply exactly r(n) bits, padding unused bits. A(H;z) is then deterministic for a fixed tape z in {0,1}^r(n).

Use a product space with exactly n blocks:

    X_i = row_i(H),                 1<=i<=n-1,
    X_n = z.

In a graph sampled under P_q, the first n-1 blocks are independent: their underlying edge sets are disjoint. Within a row the bits are independent Bernoulli(q_n). The last block is an independent uniform r(n)-bit tape. The total representation length is

    N_n = binom(n,2)+r(n),                                  (9)

which is polynomial in n. This is the representation length, not the number n of blocks controlling Hamming distance.

Define the event

    E_n = {(H,z) : A(H;z) returns a valid independent set
                         of size at least k_n}.             (10)

Membership is decidable in polynomial time: simulate A with tape z, check that its vertex list has distinct labels in [n], check its size, and inspect all pairs in the set. Malformed outputs are rejected. Thus no oracle for finding independent sets or estimating a conditional success probability is required.

Equation (8) gives product measure at least epsilon_n for E_n. Its exact measure is not needed. Each graph-block sampler is implemented exactly by drawing independent w_n-bit integers and comparing them with 2^(w_n)q_n. The tape sampler draws r(n) fair bits. Rational arithmetic in (6) has polynomial bit complexity for fixed rational d. All samplers therefore have polynomial worst-case time.

## Algorithm and guarantee under the rounded measure

Set

    delta_n = (1/2)n^(-ell).

On input G, draw an independent uniform tape z. Apply the imported concentration algorithm to the point x=(row_1(G),...,row_(n-1)(G),z), using the product measure, membership predicate, epsilon_n and delta_n above. Decode its output as y=(H,z').

If E_n fails at y, return the empty set. Otherwise run A(H;z'), verify its output again, and retain any k_n vertices of that output, giving I. Compute D(G,H), and return J=I minus D(G,H). A final independence check may also be made; on an invalid or malformed intermediate result, return the empty set.

First suppose G has law P_q. Then x has exactly the product law required by the concentration theorem. With probability at least 1-delta_n, y belongs to E_n and

    HD(x,y) <= C sqrt(n log(1/(epsilon_n delta_n)))
             = C sqrt(n log(4 n^(S+ell))).                  (11)

Each member of D(G,H) accounts for one changed graph block. A change to the tape accounts for at most one additional block and requires no vertex deletion. Hence

    |D(G,H)| <= HD(x,y).                                    (12)

By the repair lemma, on this joint event the output is independent in G and

    |J| >= k_n-|D(G,H)| >= k_n-R_n.                         (13)

Independence of the returned set also holds outside this event by the same deterministic repair lemma or by returning the empty set. The theorem is applied to success on graph-and-tape pairs; treating a randomized solver's success probability as a deterministic graph-membership oracle would not justify this step.

## Transfer to G(n,d/n) and time bound

The code of B, including its q_n samplers, is the same whether its input law is P_p or P_q. Couple the initial graphs as in (7) and use the same initial tape and internal random bits of B. When the graphs agree, the entire computations agree, including every adaptive query. Thus the probability of the event in (13) changes by at most eta_n. Under the original input law its failure probability is at most

    delta_n+eta_n
       <= (1/2)n^(-ell)+(1/2)n^(-(S+ell+4))
       <= n^(-ell) <= n^(-L).                              (14)

This is one transfer of the complete randomized computation, not a separate error estimate per adaptive sampler call.

The concentration routine's oracle time is polynomial in N_n and 1/(epsilon_n delta_n)=4n^(S+ell). Each membership and sampling call has polynomial worst-case cost, as established above. Decoding, verification and repair are polynomial. The resulting B has polynomial worst-case running time. Since S and ell are fixed and n>=2,

    log(4 n^(S+ell)) = 2 log 2+(S+ell)log n
                     <= (S+ell+2)log n,

so (3) implies (2) with C_0=C sqrt(S+ell+2). This proves the theorem.

## Relation to the sparse overlap barrier

For a fixed polynomial-time computable theta in (0,1), a solver that achieves theta n vertices with eventual inverse-polynomial success yields one achieving

    theta n-O(sqrt(n log n))

with failure at most n^(-L), for any fixed L>0. Choose a polynomial-time computable integer target k_n with theta n-2<=k_n<=theta n and apply the theorem. Integer d>1 and rational epsilon>0 give theta=(1+epsilon)log(d)/d as an instance whenever theta<1. Explicitly, for x=(d-1)/(d+1), use log d=2 sum_{j>=0} x^(2j+1)/(2j+1). The remainder after J terms is at most 2 x^(2J+1)/((2J+1)(1-x^2)), by replacing each denominator in the tail with 2J+1 and summing a geometric series. Since d is fixed and x<1, O(log n) terms give a rational lower approximation theta_n with theta-1/n<=theta_n<=theta in polynomial time. Taking k_n=floor(n theta_n), and modifying finitely many initial terms to lie in [1,n], gives the required integer target.

The loss is o(n/log n), since its ratio to n/log n is O((log n)^(3/2)/sqrt(n)), which tends to zero. In particular it improves the preceding O(n log log n/log n) constant-success loss and answers its proposed O(n/log n) amplification question affirmatively, with a smaller loss. It also permits arbitrary eventual inverse-polynomial starting success and polynomially small failure. Its runtime exponent may depend on that success lower bound, unlike the preceding fixed-call-count transformation.

This application does not establish (1) above the overlap barrier. It gives neither an all-polynomial-time lower bound under a separate average-case assumption nor a barrier-crossing algorithm. It still loses vertices and does not establish amplification at exactly k_n.
