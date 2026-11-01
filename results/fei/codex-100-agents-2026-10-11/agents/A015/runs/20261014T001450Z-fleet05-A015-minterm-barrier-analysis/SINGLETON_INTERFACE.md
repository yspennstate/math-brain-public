# Physical singleton cost after actual witness erasure

All logarithms are base two. Fix the original conditioned forests.tex queue, gamma=6/5, one full order per gate (M_l=1), positive feasible lambda_l, pi_l=min(P(h_l=1),1/2), and D=product_l(1+lambda_l*pi_l)-1. This table and its orders are fixed before the output set. Put t=sum_l lambda_l*pi_l>0.

For A={j}, every eligible partition has exactly one used gate. Its source SCC is that gate; there are no children, determinant minor is the empty determinant 1, and factorial moment does nothing. The source nonroot weight is lambda_l*r_l(j)^(-gamma), so the exact *surrogate* partition mass is

    S_j = sum_(l:j in R_l) lambda_l*pi_l*r_l(j)^(-gamma).

Its complete signed surrogate residual is log(D/S_j), not log(1/S_j) alone. This follows directly from eq:forestcost and is also the degree-one specialization of A006 v1. No witness multiplicity between gate IDs is omitted. This identity is not the exact queue probability.

Exactly-one-root, size-one, zero-child events instead give the actual conditioned output lower bound

    Q_*({j}) >= (1/(4D)) sum_(l:j in R_l)
                      lambda_l*pi_l*theta_1^l(j)/Z_1^l.

The factors 1/2 and 1/2 are the size-one and zero-child laws. Root conditioning contributes lambda_l*pi_l/D, including all inactive root probabilities. These events are disjoint gate-labelled draws. Overlapping-subset, repeated-gate and other successful events can only increase Q_*. They are not counted as partition forests or assumed to have surrogate cost B.

## Coupled singleton ledger (diagnostic, not universal payment)

The decreasing rank weights have sum <=1+integral_1^infinity x^(-6/5) dx=6. Hence sum_j S_j<=6t, so q_j=S_j/(6t) is a subprobability on coordinates. Let W_1=sum_j P_f({j})>0 and rho_j=P_f({j})/W_1. Then the exact singleton part of the posterior-surrogate residual is

    sum_j P_f({j}) log(D/S_j)
      = W_1 [log(D/(6t)) + H(rho) + D_2(rho||q)].

Here KL to a subprobability includes its missing mass (equivalently normalize q and add log(1/sum q)). It is nonnegative. The signed log(D/(6t)) must be retained. This expression exposes the physical-coordinate allocation issue after latent names are refunded; it gives no influence payment for the combined KL and higher-degree terms. In particular it is not a newly claimed FEI-equivalent bridge.

## Application to the packet's all-relevant rare switch

Let r>=1, p=2^-r, and M_r=y+A_r(z-y). This balanced actual Boolean function has positive signed prime conjunctions precisely

    h_0=(y=1,z=1), h_i=(y=1,c_i=-1) for 1<=i<=r,
    h_*=(z=1,c_1=...=c_r=1).

To prove completeness: a positive implicant not forcing y=1 permits y=-1 and must force z=1 and all controls positive. If it forces y=1 but not z=1, it permits z=-1 and must force at least one negative control. Forcing y=z=1 contains h_0. All positive implicants therefore contain one listed clause; removing any literal from a listed clause permits a negative input. Their rarities are 1/4, ..., 1/4, p/2.

Choose lambda_0=1/4, lambda_i=3/(4r), lambda_*=1/4. At y the incidence total is one, at z it is 1/2, and at each control it is 3/(4r)+1/4<=1. Order y first in all clauses containing y; fix any full order for h_*. Then

    t=1/4+p/8 <=5/16,
    D= (17/16)(1+3/(16r))^r(1+p/8)-1,
    S_y=1/4.

For arbitrary nonnegative root odds of total t<1, expanding their product gives D=sum_(k>=1)e_k <=sum_(k>=1)t^k=t/(1-t). Thus D<=5/11 and the singleton signed surrogate residual satisfies

    log(D/S_y)=log(4D)<=log(20/11)<1.

Every y-clause has width two and Z_1=1+2^(-6/5)<3/2, with theta_1(y)=1. Therefore the stated selected ACTUAL queue events have mass exactly

    Q_selected({y})=1/[16D(1+2^(-6/5))] >11/120.

The corresponding complete queue cost for this singleton is <log(120/11)<4, uniformly in r. (The actual Q_* may be larger.) Physical spectrum P({y})=(1-p)^2 tends to one and I(M_r)=1+rp. In the preceding stage every coordinate-exchangeable complete reference cost/I diverged like log(r+2); these fixed, function-specific prime tables exhibit precisely the missing physical information. The number of y-witnesses grows as r+1 but their summed root/label mass stays 1/4. This is a narrow application of a reviewed interface, not a new known-class FEI bound or proof of a universal representation lemma.

More precisely, both surrogate and selected actual-event posteriors on these witnesses are rho_0=1/4 and rho_i=3/(4r). Thus

    H(witness | output={y})=h_2(1/4)+(3/4)log r
                          = E log(1/lambda_witness).

All root rarities equal two bits and all rank/allocation charges vanish. Hence E B-H=2 exactly. Root normalization then gives 2+log D=log(4D). For the actual queue events the same label refund holds, with their size/subset/zero-child costs retained, giving log(16D(1+2^(-6/5))). Merely choosing one witness, or summing costs without the actual posterior, misses an unbounded (3/4)log r refund on a spectral event whose probability tends to one. This is a direct separation between erased *witness names* and retained *physical coordinate names*.

## Exact boundary

The first unsupported line is a dimension-independent bound on the *whole* signed spectral expectation, using one fixed table and orders, with conditional terminal-core cross-entropy retained. Degree-one location payment does not bound degree>=2, the ownership sum, gate-scale congestion, or A007's signed Psi. A006's determinant identity computes those masses; it does not bound their influence-weighted expectation. The next useful step must couple this physical-location allocation to that whole-set posterior, rather than average it away or spend the same influence reserve separately in every degree.
