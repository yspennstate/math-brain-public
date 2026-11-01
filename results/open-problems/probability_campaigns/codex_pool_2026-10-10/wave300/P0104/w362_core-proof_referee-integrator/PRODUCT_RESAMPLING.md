# Independent derivation for the P0104 referee packet

This rederives the finite-product step being developed by w360. It is a standard product-space calculation, with no novelty claim. The elementary calibration in section 4 is w362's additional conditional reduction and awaits independent referee w365. No assertion below proves the unproved crossover hypotheses.

## 1. Orthogonal decomposition

Let W_1,...,W_m be independent random variables, and f in L^2 of their product law. Let E_i average only coordinate i, keeping all other coordinates fixed. These operators are commuting self-adjoint orthogonal projections: this follows directly by Fubini and independence. For a subset S of {1,...,m}, define

    P_S = product_{i in S}(I-E_i) product_{i not in S}E_i,
    f_S = P_S f.

The product of (E_i+(I-E_i)) over all i is I, so f=sum_S f_S. For S != R, choose i in their symmetric difference. One term is averaged in coordinate i and the other has zero average in that coordinate; hence their inner product is zero. Thus the terms are pairwise orthogonal, f_empty=E f, and

    Var(f) = sum_{S nonempty} ||f_S||_2^2.

This finite expansion is a proof device; it is not an algorithm enumerating 2^m subsets for the lattice problem.

## 2. Independent refresh covariance

For t>=0, W^t retains each original coordinate with probability exp(-t), otherwise replacing it with a fresh independent copy. Retention decisions and replacement copies are mutually independent and independent of W. The transition operator is

    Q_t = product_i [exp(-t)I + (1-exp(-t))E_i].

It acts on f_S by multiplication by exp(-|S|t). Conditional expectation with respect to W therefore gives

    C_f(t) = Cov(f(W),f(W^t))
           = sum_{S nonempty} exp(-|S|t)||f_S||_2^2.

Define H_f(t)=-C_f'(t). The finite sum can be differentiated and integrated term by term:

    H_f(t) = sum_{S nonempty} |S|exp(-|S|t)||f_S||_2^2,
    H_f(t)>=0,  H_f'(t)<=0,
    Var(f) = integral_0^infinity H_f(t)dt.

One can equivalently write H_f(t)=sum_i <f-E_i f, Q_t(f-E_i f)>. Every summand has a nonnegative spectral representation. This positivity comes from the self-adjoint product operator, not from a claim that selected geodesic segments are independent. The exact integral tail is C_f(a) for every a>=0.

## 3. The elementary FPP bound and its limit

For iid Uniform[1,2] nearest-neighbor undirected lattice weights, w360-C1 makes T_n exactly a function f of the edges in [-2n,2n]^2. Choose a minimizing path by a fixed deterministic order of the finitely many simple paths. Denote it by Gamma(W). It has at most 2n edges. Continuity is not needed for this choice.

Let W^(i) replace just edge i. Conditioning on all the other coordinates, the two copies are iid, so

    E[(f(W^(i))-f(W))^2] = 2 ||f-E_i f||_2^2.

Exchangeability implies that half this squared-difference expectation is the positive-part squared expectation. Evaluating the old minimizing path in the new environment yields

    (f(W^(i))-f(W))_+ <= 1{i in Gamma(W)}.

Indeed an edge outside that chosen path cannot increase its cost; an edge on it can increase cost by at most one. Consequently

    H_n(0)=sum_i ||f-E_i f||_2^2
          =sum_i E[(f(W^(i))-f(W))_+^2]
          <= E|Gamma(W)| <= 2n.

The expansion also gives H_n(t)<=exp(-t)H_n(0). Integrating this proves only Var(T_n)<=2n. At time a=n^(-1/3+epsilon), its certified tail bound is 2n exp(-a), still of order n. The extra saving is absent.

This failure is structural for the available assumptions: on a fixed n-edge path with iid Uniform[1,2] costs, f is a sum, all nonconstant spectral terms have |S|=1, and H_f(t)=(n/12)exp(-t). Independence, bounded positive costs, and linear path length all hold, but the tail remains order n. This is a counterexample to deriving the crossover from those facts alone, not a counterexample to planar optimized FPP.

## 4. A sufficient calibration lemma, still unproved for lattice FPP

For every epsilon in (0,1/3), suppose that for all sufficiently large n there are constants c_epsilon,C_epsilon>0, independent of n, such that

    H_n(n^(-1/3-epsilon)) >= c_epsilon n,                 [LOWER INPUT]
    C_n(n^(-1/3+epsilon)) <= C_epsilon n^(2/3+epsilon).   [UPPER INPUT]

Then monotonicity and the integral identity prove

    Var(T_n) >= n^(-1/3-epsilon) H_n(n^(-1/3-epsilon))
             >= c_epsilon n^(2/3-epsilon),
    Var(T_n) <= n^(-1/3+epsilon)H_n(0)
                + integral_{n^(-1/3+epsilon)}^infinity H_n(t)dt
             <= (2+C_epsilon)n^(2/3+epsilon).

Taking logarithms, then letting epsilon decrease to zero, gives log Var(T_n)/log n -> 2/3, hence the explicitly defined variance exponent chi=1/3. No stronger asymptotic constant, distributional limit, or concentration exponent follows.

The displayed lower and upper inputs are the single two-sided noise-crossover lemma this route needs. Neither is proved here. They are stronger geometric information than finite-product algebra. Their chosen n^(-1/3) scale encodes the desired planar exponent and needs an independent argument. The current derivation deliberately stops at that gap.

For the subdiffusive branch alone, the same calculation shows that any fixed alpha>0 and tail bound C_n(n^(-alpha))<=C n^(1-alpha), together with H_n(0)<=2n, imply Var(T_n)<= (2+C)n^(1-alpha). This gives a strict upper exponent bound if an exponent exists; it does not identify 1/3 or establish exponent existence.

## 5. Review scope

w365 should audit the projectors, covariance identity, factor of two in the positive-part calculation, and the two epsilon-dependent bounds in section 4. Only the conditional implication is submitted as a proof. The crossover statements remain conjectural. No formal-check receipt is claimed, and no trusted axioms or placeholder theorem have been introduced.

NEXT: Give the exact original source and peer covariance kernel to the reviewer; the next proof step is a genuinely new geometric estimate on C_n(t), not another derivation of this identity.
