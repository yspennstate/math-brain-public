# account02/B03 early calculation — overlap exterior mass and hyperbola wrapper

Run `20260924T051234Z-account02-B03-QFORM-auto11`.

The first unpaid implication after the disjoint third-exterior exit is the overlap-heavy residue. Define

\[
\mathcal E_{1,i}(A)=\sum_{\substack{|P|=|Q|=2\\P\cap Q=\varnothing\\i\notin P\cup Q}}
\det A[\{i\}\cup P,\{i\}\cup Q]^2.
\]

If `d=A_ii != 0` and `S=A/A_ii` is the physical Schur complement, block determinant gives

\[
\det A[\{i\}\cup P,\{i\}\cup Q]=d\det S[P,Q],
\qquad
\mathcal E_{1,i}=d^2\sum_{P\cap Q=\varnothing}\det S[P,Q]^2.
\]

For a random Bernoulli cut `I|J` of the residual coordinates,

\[
\mathbb E\,e_2(S[I,J]S[I,J]^T)=\frac{\mathcal E_{1,i}}{16d^2}.
\]

Hence some literal physical residual cut has `Z2 >= E_{1,i}/(16d^2)`. Combining exact square completion with the already proved marginal-free Z2 half-Riesz receiver gives

\[
\|p_Q\|_\infty
\le 8\sqrt2\,e^{1/4}\,(d^2\mathcal E_{1,i})^{-1/8}.
\]

This pays a genuine one-anchor overlap branch with no residual row-marginal gate. It also identifies the precise remaining one-anchor obstruction: large `E1` can survive only while every anchor currency `A_ii^2 E_{1,i}` is small.

A complementary wrapper comes from the translation-uniform product envelope proved in account03/B03 r47. If a physical zero-diagonal pair `A_ii=A_jj=0`, `mu=A_ij!=0` is completed exactly and its Schur residual `R` has a density cap `H`, then r47 gives a common conditional hyperbola envelope `K_mu` with

\[
\|K_\mu\|_3\le72^{1/3}|\mu|^{-2/3}.
\]

Because the translations of the hyperbola factors may depend arbitrarily on the residual variables, pointwise domination still gives

\[
p_Q(q)\le \mathbb E K_\mu(q-R)
          =(K_\mu*p_R)(q).
\]

Since `||p_R||_{3/2} <= H^{1/3}`, Holder/Young yields

\[
\boxed{\|p_Q\|_\infty\le72^{1/3}|\mu|^{-2/3}H^{1/3}.}
\]

This is the mechanism to test on the two-anchor exterior residue and on the newest account03/B03 r48 balanced-carrier residual theorem.
