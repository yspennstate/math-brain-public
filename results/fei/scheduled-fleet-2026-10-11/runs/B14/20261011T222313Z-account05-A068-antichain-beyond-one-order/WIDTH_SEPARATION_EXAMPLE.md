# Nonlinear cyclic controlled majority

For every odd q>=5, on 2q independent physical bits x,z, write z_j=(-1)^{u_j}, and define

    a_i(z)=(-1)^{u_i u_{i+1}}, indices modulo q,
    F_q(x,z)=MAJ_q(x_1 a_1(z),...,x_q a_q(z)),
    c_q=2^{-(q-1)} binom(q-1,(q-1)/2).

The base majority is regular. Controls are quadratic and overlap: each physical control participates in two inner control gates. F_q satisfies the new theorem, despite failing global unateness in every data coordinate. Indeed d_{x_i} F=a_i(z)d_i MAJ; a_i takes both signs, and for each such z one can choose the other data bits at a pivotal majority assignment. Hence data derivatives attain both +1 and -1. A desirability-width hypothesis on F_q is therefore unavailable, rather than merely wide.

Exact influences are

    Inf_{x_i}=c_q,
    Inf_{z_j}=(3/4)c_q,
    I_x=q c_q, I_z=(3/4)q c_q, I=(7/4)q c_q.

To prove the control formula, flipping u_j toggles logical vote j-1 iff u_{j-1}=1 and vote j iff u_{j+1}=1. The neighbors are independent uniform bits, so the number toggled is 0,1,2 with probabilities 1/4,1/2,1/4. Conditional on controls, logical data votes are independent uniform. Toggling one vote changes odd majority with probability c_q. Toggling two votes also changes it with probability c_q: their signs must agree (probability 1/2), and the q-2 remaining votes must sum to +1 or -1, whose probability is twice 2^{-(q-2)}binom(q-2,(q-3)/2). The binomial identity gives c_q. Averaging yields 3c_q/4.

The new complete-reference estimate is

    H(F_q) <= (C_reg+3/2) q c_q
            = ((4 C_reg+6)/7) I(F_q).

This is a uniform constant smaller than 8.937. No entropy equality with the base majority is claimed in the quadratic example: its conditional affine packet entropy is positive and paid by 2I_z.

The published arbitrary-combination bound can be applied by listing q dictators x_i and q regular controls a_i (each is OR in sign coordinates); it gives coefficient 11.238+(17/5)log_2(2q), growing without bound. This is a comparison with that valid explicit representation bound, not a proof that every possible regular representation needs 2q components or that the new family was unknown to all prior literature. The published width theorem cannot apply because F_q is not unate. Read-once parity composition cannot directly apply because controls are nonlinear and shared.

With z as a q-bit selector block, every branch is an oriented majority. Its selector influence per address is 3c_q/4 ->0; thus the uniform-positive-selector-energy hypothesis of the published fresh-selector closure fails. An individual neighboring-branch correlation is 1 or 1-2c_q, depending on whether zero or at least one vote is toggled; its average over selector edges is 1-3c_q/2. Every such correlation is strictly positive for q>=5, so the orthogonal-neighbor hypothesis fails as well. The raw selector entropy bill 2q has ratio to I equal to 8/(7c_q), diverging. The new conditional rank bill is at most 2I_z, with no such loss. Convergence c_q->0 follows from the baseline central-binomial density bound c_q<=(q)^{-1/2}.

For contrast, the linear cyclic family MAJ_q(x_i z_i z_{i+1}) has H exactly equal to base majority and I_x=I_z=q c_q. It is already an application of the recovered translation-symmetry reduction. It serves as a checked calibration, not the new mechanism.

The finite checker verifies both families at q=3,5,7. The formulas above are proved for every odd q>=5; no finite-to-infinite inference is used. Independent review and external novelty verification remain pending.
