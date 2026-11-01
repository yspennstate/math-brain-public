# A conditional-rank criterion for strict active-matrix concavity

Coordinator constructive lemma, 15 September 2026. This supplements ROOT_DIAMOND_ACTIVE_MATRIX. It assumes a certified projection diamond; it does not prove general diamond existence or general Lyons concavity.

Let W and V be orthogonal isometries of ranks r and 2 in C^n, with n>=r+3, and let K=P_W+VMV*, 0<M<I_2. Let x_(S,T) be a nonnegative unlabeled diamond coupling for the flag W contained in W+V. Suppose there is one bottom set S, |S|=r, such that:

1. p_S(K)>0 and p_(S+i)(K)>0 for every i outside S;
2. for every distinct i,j outside S, x_(S,S+i+j)>0.

Then the frozen logarithmic diamond coefficient Lambda in ROOT_DIAMOND_ACTIVE_MATRIX is strictly positive. Therefore, if k=min(r,n-r-2)<=4, the full active four-dimensional Hermitian Hessian has the gap

    -H''[A,A] >= min(Lambda, 2 C_k/(C_k+2 Lambda)) ||A||_F^2,
    C_k=8-2 log 2-4 log(k+1)>0.

Only one fully supported bottom conditional family is needed. Other diamond weights may be zero.

## Proof

Every supported diamond has the nonnegative logarithmic gap

    log(p_(S+i) p_(S+j)/(p_S p_(S+i+j))).

The average of these gaps is Lambda. If Lambda=0, every gap in hypothesis 2 must vanish. Condition on all sites of S being occupied. This conditioning event has positive probability because p_S>0. The conditional marginal kernel F on S^c is the Schur complement of K_S. Since the conditional empty atom is p_S/Pr(S contained in X)>0, I-F is positive definite. Its odds matrix L=F(I-F)^(-1) is consequently finite and positive semidefinite.

The exact atom ratios give

    L_ii=p_(S+i)/p_S>0,
    det L_{ij}=p_(S+i+j)/p_S.

The zero gaps force det L_{ij}=L_ii L_jj for every pair. Hermiticity gives L_ij=0. Thus L is a diagonal matrix of strictly positive entries and has rank n-r>=3.

But K has rank r+2, and K_S is invertible: its determinant is Pr(S contained in X)>0. Schur-complement rank additivity gives rank F=(r+2)-r=2. Since I-F is invertible, rank L=rank F=2, a contradiction. Hence Lambda>0. The stated gap follows from the already proved active-matrix theorem.

## Generic rank-one backgrounds in arbitrary dimension

For r=1 and any n>=4, take orthonormal w,V_1,V_2 such that every coordinate of w, every two-row minor of V, and every three-row minor of [w,V] is nonzero. C033's strict-Hall theorem constructs positive weight on every supported pair-to-triple inclusion. Its exact diamond marginal correspondence then makes every x_({i},{i,j,k}) positive. The atom conditions follow from the active-matrix formula, or from the positive middle marginals. The lemma proves strict full active-matrix concavity for all 0<M<I_2, with a uniform gap on compact parameter sets.

This is a strictness refinement of an already covered active-matrix family, not a new arbitrary-base concavity theorem. For n=4, ROOT_FOUR_SITE_BOUNDARY proves strictness under the weaker assumption that w and its one-dimensional complementary endpoint vector have no zero coordinates; active minors may vanish there.
