# Signed conditional partition for arbitrary gates

All logarithms are base two. Let d>=4 be even, delta=2^-d, t=sqrt(delta), b(y)=(-1)^(sum_j y_(2j-1)y_(2j)) on 0/1 labels, and let g be any Boolean sign on r>=1 disjoint physical bits x. Write a_V=hat g(V). Define the actual Boolean function F(y,x)=b(y)+1[y=0](g(x)-1). Each two-bit factor of b has Walsh coefficients (+,+,+,-)/2; hence hat b(R)=sigma_R t, sigma_R in {-1,1}, with counts N_sigma=(2^d+sigma 2^(d/2))/2. This follows alternatively from sum_R hat b(R)=b(0)=1. All hypotheses and counts are exact, with no exchangeability of physical subsets assumed.

Expanding the point indicator gives

    hat F(R,V)=sigma_R t 1[V=empty]+delta(a_V-1[V=empty]).

For a relevant gate query i, write E_i=Inf_i(g)>0. Its actual physical influence is e_i=delta E_i, directly by flips: only y=0 exposes the gate. For residual gate mask V not containing i, the complete derivative/reference laws on (R,V) are

    mu_i(R,V)=delta a_(V+i)^2/E_i,
    r_i(R,V)=hat F(R,V)^2+delta^2 a_(V+i)^2.

Their normalizers are one by Parseval; in particular reference-only mass is never discarded. The likelihood ratio depends only on (V,sigma_R). Therefore the partition retaining residual gate mask V and bent Fourier sign sigma_R preserves FULL KL exactly, including all conditional within-degree information relevant to this row. This is a signed, genuinely non-product partition, not a product-reference assumption. Its alphabet has at most 2^r cells; this theorem does not control the complexity of an arbitrary gate or its terminal entropy.

For V nonempty, r_i(R,V)=delta^2(a_V^2+a_(V+i)^2), so the conditional R distributions of derivative and reference are the same uniform law. For V=empty, define

    rho_i=1-delta+delta(a_empty^2+a_{i}^2),
    c_(i,sigma)=(sigma+t(a_empty-1))^2+delta a_{i}^2.

The complete reference mass of this cell is rho_i: summing squared bent amplitudes uses sum_R sigma_R t=1. The derivative mass is a_{i}^2/E_i. Conditional on this cell, derivative R has mass delta and reference R has mass delta c_(i,sigma_R)/rho_i. Define

    D0_i=sum_sigma N_sigma delta log(rho_i/c_(i,sigma)).

If a_i=0 the cell has no derivative mass, and its contribution is defined as zero. Chain rule now gives exactly

    D(mu_i||r_i)=D(mu_i^V||r_i^V)+(a_i^2/E_i)D0_i,
    L_i=e_i[D_full-D_mask]=delta a_i^2 D0_i.

This recovers A073's special two-bit gate formula: a_empty=a_i=1/2 gives c=1-sigma t+delta/2, rho=1-delta/2, and L_i=delta D0_i/4. That special sharper constant is not needed below.

For every gate, |a_empty-1|<=2 and t<=1/4. Thus c_(i,sigma)>=(1-2t)^2>=1/4. Parseval gives a_empty^2+a_i^2<=1, so rho_i<=1. Every positive conditional likelihood ratio is at most 4. Since the conditional distributions normalize, 0<=D0_i<=log(4)=2. Consequently

    0<=sum_(gate i) L_i<=2delta sum_i a_i^2<=2delta.

No factor r appears: the final bound is Parseval on the first-level gate coefficients, not a sum of individual worst-case charges. There is one dedicated physical reserve. The quadratic bent core has Inf_(y_j)(b)=1/2 and b(0)=b(e_j)=1. Whenever g(x)=-1, changing the value at y=0 toggles precisely the edge joining 0 to e_j from nonpivotal to pivotal, adding 2delta to conditional influence. Averaging x yields

    Inf_(y_j)(F)=1/2+delta(1-a_empty).

As delta<=1/16,

    sum_i L_i<=2delta<=1/8<=Inf_(y_1)(F)/4.

Charge the combined gate-row coarsening losses ONCE to this single dedicated quarter-reserve. Nothing here proves that the same reserve can also pay activation, core terminal entropy, or other history charges. Retaining the sign avoids these coarsening losses altogether, but retains a larger terminal reference alphabet.

## First unreconstructed universal implication

The scoped signed partition and reserve above are checked. The first unsupported implication toward C018/C024 is: a general non-flat Boolean terminal core admits such a complete conditional partition, with the residual terminal charge and the coarsening loss simultaneously paid from a globally nonoverlapping influence ledger. In exact C018 form the missing assertion remains sum_i e_i D(mu_i||r_i)>=sum_i e_i log(1/e_i)-K I(F) for one finite universal K. A bounded quotient loss does not supply this assertion. In this family an arbitrary g survives in the residual mask laws; its complexity and its terminal charge have not been bounded. No FEI claim follows.

## Independence and source comparison

The derivation was reconstructed from the statements of A096-SINGLE-SPECTATOR-REFUND-OWNERSHIP@1 and A073-NONZERO-ERASURE-BINARY-REMAINDER@1 before reading A073 DERIVATION.md. Source comparison afterward confirms the special-case coefficients and the isolated-reserve warning. The arbitrary-gate signed partition and summed Parseval budget are a new scoped extension, author-proved pending independent review. It uses no unproved campaign candidate.
