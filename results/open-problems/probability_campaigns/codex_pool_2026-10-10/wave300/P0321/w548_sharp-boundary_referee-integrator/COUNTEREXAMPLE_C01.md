# C01: translation invariance does not imply fast positional decorrelation

Let L be any full-rank lattice in R^2, let F be a half-open fundamental cell, and let U be uniform in F. The point process Phi=L+U is stationary under every translation: for t in R^2, U+t reduced modulo L is uniform in F, hence Phi+t has the law of Phi.

Choose a nonnegative nonzero smooth function h supported in a ball small enough that its translates centered at distinct lattice points do not overlap, and write X_x(Phi)=sum_{p in Phi} h(p-x). The sum is finite. X_0 is a nonconstant function of U: it is positive for some U and zero for others. Hence Var(X_0)>0. For every lattice vector a in L, X_a(Phi)=X_0(Phi) pointwise by reindexing p-a in Phi. Therefore Cov(X_0,X_a)=Var(X_0)>0, including for lattice vectors a of arbitrarily large norm. The process is translation invariant but this positional covariance does not tend to zero.

The argument also applies to a triangular lattice. It disproves the auxiliary implication "translation-invariant point-process law => fast decay of all positional correlations." It makes no assertion that Phi is a positive-temperature Riesz Gibbs state, and it does not address the hexatic phase. A smooth local count was used so that the covariance is an ordinary bounded random variable rather than a distributional pair correlation.

Source boundary: Lewin, *Coulomb and Riesz gases: The known and the unknown* (2022), arXiv:2202.09240, Theorem 47, PDF p.60, explicitly assumes s>d for translation invariance; the 2D phase discussion on pp.65-66 includes s=0 and s=1 numerics. Thus extending Theorem 47 to s<=d requires another theorem, even before the correlation issue above.

Independent review requested from w551; pending. No novelty claim.
