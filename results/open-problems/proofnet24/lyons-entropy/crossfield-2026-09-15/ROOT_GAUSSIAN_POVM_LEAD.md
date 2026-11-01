# Root lead — a two-mode effect reduction and its realizability constraint

Status: original root lead, a proved abstract counterexample, and a stronger identity subsequently derived by X066. Root contributions are not extra sub-agents. Use X066's completed report for its precise physical hypotheses and resulting classification.

A fixed Gaussian background and two active modes suggest reducing measured atoms to positive effects on two-mode Fock space. In parity blocks, write E_y=diag(alpha_y,B_y,gamma_y), where B_y is positive two by two. The output probability at covariance M is

    p_y(M)=alpha_y det(I-M)+tr[B_y(M-det(M)I)]+gamma_y det M.

The proposed necessary Gaussian-effect identities are det B_y=alpha_y gamma_y, with sum alpha=sum gamma=1 and sum B=I. X066 proved these directly from the finite determinant lemma, without invoking a closure theorem: for an invertible shifted background C_y, alpha_y=s_y det C_y, T_y=V*C_y^-1 V, B_y=alpha_y(I+T_y), gamma_y=alpha_y det(I+T_y); polynomial continuation handles singular cases. Positivity follows by testing physical active inputs 0,I and rank-one projections.

These local constraints DO NOT imply entropy concavity. Take the ordinary two-mode occupation measurement and split only its empty outcome into 64 equal labels. Every refined effect still obeys the displayed Gaussian determinant identity and all completeness identities, and all effects commute. At M=tI its entropy is

    H_new(t)=2h(t)+(1-t)^2 log64,
    H_new''(1/2)=-8+12log2>0.

The final sign follows from log2>2/3, for example the strictly positive atanh series. More generally splitting a single outcome into N equal labels adds p_y(M)log N and its full quadratic acceleration; an arbitrary refinement therefore need not preserve covariance entropy concavity. This is not a Lyons counterexample: the colored empty outcomes are not the original fixed-coordinate DPP occupation measurement.

X066 derived an essential stronger physical constraint. For every positive coordinate field z, the effect generating matrix F(z)=sum_y z^y E_y is Gaussian:

    det B(z)=alpha(z)gamma(z)

as a multivariate polynomial identity. It follows from the determinant generating function det(I-K+ZK) with the same fixed background. In particular every adjacent pair of effects has a Gaussian sum. When their alpha values are positive, their normalized one-particle odds differ by a rank-at-most-one matrix. The artificial colored-empty refinement generally fails this generating identity.

X066's subsequent constructive route uses the full generating identity: if all B_y commute, one fixed active basis diagonalizes them. Unique factorization of b1(z)b2(z)=alpha(z)gamma(z), combined with multiaffinity, forces disjoint-variable factors corresponding to two actual fixed binary-input channels. Their balanced refinement has an affine entropy correction, unlike the colored-empty construction. This classification and its complete proof belong in X066; it should not be silently extended to noncommuting effects.

The outstanding physical route is to exploit the multivariate generating identities when the one-particle effects do not commute, retaining every measurement and normalization correction. Arbitrary positive Gaussian POVMs are too broad a replacement class.
