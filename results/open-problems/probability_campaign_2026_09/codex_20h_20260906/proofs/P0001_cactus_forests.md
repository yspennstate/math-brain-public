# P0001: negative dependence for random forests

**Target remains unsolved here.** This note proves a special case and refutes an overly broad proof route. The special case is author checked; novelty is not claimed. No independent reviewer or proof assistant has checked this note.

The sourced target is Grimmett, *Selected problems in probability theory* (2022), Conjecture 4.2, PDF page 8: for a finite simple graph, uniformly choose an acyclic edge subset F. Are distinct edge indicators always negatively correlated? Tang and Zhang, arXiv:2603.10738v1 (March 2026), Conjecture 1.3, still states this general question. Their complete-graph results do not settle arbitrary graphs.

## A special case with an exact formula

Let G be a finite cactus graph: each edge belongs to at most one simple cycle. Give every edge a finite positive weight w_e. Choose an acyclic edge set F with probability proportional to the product of its selected edge weights. This includes the uniform forest measure when every w_e=1.

**Proposition.** This measure is negatively associated: if A and B are disjoint edge sets and f and g are increasing real functions of the indicators in A and B respectively, then Cov(f,g) <= 0.

**Proof.** Begin with independent Bernoulli edge indicators X_e with p_e=w_e/(1+w_e). Conditioning on acyclicity gives exactly the desired measure, because the product probability of an edge set is a constant times its product weight.

The cactus cycles have disjoint edge sets. Acyclicity is therefore the intersection, over cycles C, of the events that not every edge of C is selected. These events depend on disjoint coordinate sets. Conditioning preserves independence between the cycle blocks and the remaining bridge edges.

Consider one cycle block. Write H for the event that every coordinate equals one and q=P(H)=product(p_e). For disjoint coordinate sets A and B in that block, set a=E f, b=E g, f_*=f(1_A), and g_*=g(1_B). Independence gives E(fg)=ab. On H, f=f_* and g=g_*. Consequently

    E(f | H^c) = (a-q f_*)/(1-q),
    E(g | H^c) = (b-q g_*)/(1-q),
    E(fg | H^c) = (ab-q f_* g_*)/(1-q).

Subtracting the product of the first two equations from the third yields

    Cov(f,g | H^c)
      = -q (f_*-a)(g_*-b)/(1-q)^2 <= 0.

The inequality follows from monotonicity: f_* >= a and g_* >= b. The denominator is positive because every p_e<1.

For completeness, independence products preserve negative association. Suppose X and Y are independent negatively associated blocks. Condition first on Y. The conditional covariance of f(X_A,Y_C) and g(X_B,Y_D) is nonpositive whenever A,B are disjoint and C,D are disjoint. The two conditional expectations are increasing functions of the disjoint Y-coordinate sets C,D; their covariance is also nonpositive. The total covariance identity proves the claim for (X,Y). Induct over the finitely many blocks, including independent bridge coordinates. This proves the proposition.

For two distinct edges e,f in the same cycle, the formula becomes

    Cov(X_e,X_f | H^c)
      = -q (1-p_e)(1-p_f)/(1-q)^2.

For a uniform cycle with m edges this is

    -2^(m-2)/(2^m-1)^2.

Edges in different blocks have covariance zero.

## Second derivation and adversarial check

For the uniform cycle, count subsets directly. There are 2^m-1 forests, 2^(m-1)-1 containing a given edge, and 2^(m-2)-1 containing a specified pair. Thus the covariance numerator is

    (2^(m-2)-1)(2^m-1) - (2^(m-1)-1)^2 = -2^(m-2),

which agrees with the conditional-product calculation. For a triangle it gives -2/49. For a tree, all edge subsets are forests, and independent Bernoulli(1/2) indicators give zero covariance. These checks test both the sign and the degenerate no-cycle case.

The strongest reason this does not solve the target is that general cycles share edges. Their exclusion events no longer factor into independent blocks. One cannot simply say that conditioning independent bits on a decreasing event preserves negative association.

Here is a minimal counterexample to that proposed general principle. Take three fair independent bits (X1,X2,X3), conditioned on neither X1 X2 nor X2 X3 equaling one. The five allowed states are

    000, 100, 010, 001, 101.

Then E X1=E X3=2/5 and E(X1 X3)=1/5, so Cov(X1,X3)=1/25>0. The conditioning event is decreasing, but creates positive correlation. This is a counterexample to a proof route, not to the forest conjecture: the forbidden pairs do not form the circuit family of a graphic matroid. Circuit elimination would require another circuit, which is absent.

## Exact unresolved obligation

To extend this argument one needs a valid inequality controlling the interaction of overlapping cycle constraints, using graphic-matroid structure. Arbitrary decreasing-event conditioning cannot provide it. The target is not promoted beyond a partial attempt.

## Sources

- https://arxiv.org/abs/2205.07318 (Conjecture 4.2, page 8).
- https://arxiv.org/html/2603.10738v1 (Conjecture 1.3 and the discussion immediately following).

The calculations and proof above were derived during this campaign. They are not attributed to the cited papers.
