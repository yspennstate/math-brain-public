Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.** Source metric remains `d_sym=3`; planned methods **B21 / B25 / B30**.

# Idea before code — codimension-two cube sections as a bivariate box-spline/Rademacher inequality

The preceding STUCK1 recovery killed one exact `V=12,F=22,I=98` witness by a coupled radial descent, but it did not give a uniform contradiction. Rather than add another local KKT lemma, change the object being optimized.

For a generic centrally symmetric four-polytope with exactly twelve vertices write

\[
P=\operatorname{conv}\{\pm v_1,\ldots,\pm v_6\},\qquad
A=(v_1\ \cdots\ v_6)\in\mathbb R^{4\times6}.
\]

Let `B in R^{2 x 6}` have full row rank and `BA^T=0`. Then `A^T(P^circ)` is the codimension-two central cube section

\[
C=\ker B\cap[-1,1]^6.
\]

Xu's 2009 paper recasts the `2n+2`-facet/codimension-one case as a *univariate* box-spline inequality. The first post-Lopez--Reisner case here has codimension two, so the natural next object is the **bivariate box spline**: the density at zero of

\[
Y=\sum_{i=1}^6 b_iU_i,\qquad U_i\stackrel{iid}{\sim}\mathrm{Unif}[-1,1],
\]

where `b_i` are the columns of `B`.

The hoped-for exact identity is stronger than a mere analogy. For each pair `J={j,k}`, let `I=J^c`, let

\[
N_J(B)=\#\{\varepsilon\in\{\pm1\}^{I}:\ -B_I\varepsilon\in B_J(-1,1)^2\},
\]

and let

\[
p_J(B)=\Pr\{-B_IU_I\in B_J[-1,1]^2\}.
\]

`N_J` is the exact number of simplicial facets of `P` whose omitted antipodal pair indices are `J`; `p_J` is the continuous uniform hit probability for the *same* parallelogram.

The proposed double-count is

\[
|P||P^\circ|=\frac23\sum_{|J|=2}N_Jp_J
\tag{I}
\]

for the generic 4D/6-pair case. Therefore the entire generic twelve-vertex Mahler inequality would be equivalent to the concrete fifteen-term inequality

\[
\boxed{\sum_{|J|=2}N_J(B)p_J(B)\ge16.}
\tag{BS12}
\]

The boundary/nonsimplicial case should then follow by centrally symmetric generic perturbation and continuity, provided all twelve vertices are retained. This would turn the first unknown vertex count into a rank-two Gale/box-spline problem instead of a four-dimensional polytope-classification problem.

Three deliberately different moves:

- **B21 (ask who else has this shape):** port Xu/Ball's box-spline language from codimension one to the bivariate codimension-two section forced by six antipodal vertex pairs.
- **B25 (count the same thing twice):** compute the product once from primal facet cones plus complementary minors and once from coarea/central box-spline density.
- **B30 (one direction at a time):** localize the coarea density to each `2 x 2` Gale basis `B_J`; conditioning on the four complementary uniforms should give `p_J=4|det B_J| f_B(0)`, making (I) exact.

Before any code, the mathematical obligation is to prove every normalization in (I), then identify whether `(BS12)` has a plausible pointwise strengthening. In particular, do **not** assume `p_J >= N_J/16`: an arbitrary centrally symmetric convex subset of a cube need not have volume fraction at least its vertex fraction, and even in this structured family that pointwise inequality requires testing. Code, if warranted, will only test the exact identity and hunt for failure of naive strengthenings; it will not be used as evidence for the universal inequality.
