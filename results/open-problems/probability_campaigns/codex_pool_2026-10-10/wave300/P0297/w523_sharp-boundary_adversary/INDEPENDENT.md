# Independent P0297 boundary derivation

Saved on 2026-10-10 before opening w522's statement, proof, claims, or handoff. This is an elementary algebraic obstruction, independently derived from the primary metric KPZ statement, not a solution of P0297. Independent review by w524 is pending.

The target is to compute the almost surely deterministic Hausdorff dimension d_gamma of (C,D_h), with h a whole-plane GFF, for each fixed gamma in (0,2). The primary problem statement is Gwynne-Miller, *Existence and uniqueness of the Liouville quantum gravity metric for gamma in (0,2)*, Problem 7.1, https://link.springer.com/article/10.1007/s00222-020-00991-6 . Its parameters are Q=2/gamma+gamma/2 and xi=gamma/d_gamma. The already known gamma=sqrt(8/3) case has d_gamma=4. The dated primary source is not a certification of openness as of October 2026.

Gwynne-Pfeffer, *KPZ formulas for the Liouville quantum gravity metric*, Theorem 1.5, https://arxiv.org/html/1905.11790, supplies the metric dimension of alpha-thick points intersected with a deterministic Borel set or a random Borel set independent of h. For a deterministic open set its Euclidean dimension is 2, so the algebraic ratio is

    F_gamma,xi(alpha) = (2-alpha^2/2)/(xi*(Q-alpha)),  -2 <= alpha <= 2.

Here gamma in (0,2) and xi>0 are fixed. Q>2, so the denominator is strictly positive on the whole interval. The exact identity

    gamma/xi - F_gamma,xi(alpha)
        = (alpha-gamma)^2/(2*xi*(Q-alpha))

follows by expanding gamma*(Q-alpha) - (2-alpha^2/2). Consequently the unique maximum is gamma/xi, attained at alpha=gamma. This proves the sharp algebraic special case with all constants; it cannot determine xi. Inserting xi=gamma/d_gamma turns the answer into d_gamma itself. A genuine solution needs an independent metric or crossing estimate that determines xi as a function of Q. The published Corollary 1.6 already identifies the maximizing thickness; no novelty is claimed for this optimization.

There is a precise failure of uniform extension to the critical endpoint. Put epsilon=2-gamma and delta=2-alpha. Then

    Q-2 = epsilon^2/(2*gamma),
    F_gamma,xi(2-delta)
        = (2*delta-delta^2/2)/(xi*(delta+epsilon^2/(2*gamma))).

For fixed xi>0, if delta=c*epsilon^2 with fixed c>=0 and epsilon decreases to zero, the ratio tends to

    2*c/(xi*(c+1/4)).

In particular, c=0 gives 0 while c=1/4 gives 1/xi. Along the maximizing path alpha=gamma (delta=epsilon), the limit is 2/xi. Thus there is no joint continuous extension at (gamma,alpha)=(2,2). Formally setting gamma=2 first yields F_2,xi(alpha)=(2+alpha)/(2*xi) for alpha<2, whose supremum 2/xi is not attained on [-2,2). The expression at alpha=2 is 0/0. These are statements about this algebraic formula, not statements about a critical LQG metric or its dimension.

Additional quantifier check: Theorem 1.5 says for each fixed alpha almost surely, not automatically simultaneously for an uncountable collection of alpha. The maximum identity is deterministic and does not exchange an uncountable union with Hausdorff dimension. To assert that the whole metric space has the same dimension as its gamma-thick subset, use published Corollary 1.6 or a separate upper bound; the optimizer alone is insufficient. Exact metric KPZ also requires an h-independent set and cannot be inserted unchanged for h-selected geodesics.

NEXT: Read w522's now-available proposed route and audit its strongest mathematical step against these independently saved identities and endpoint cases.
