# Why stationary averaging does not determine spatial cycle relaxation

This is an elementary calculation for the extension review, not a priority claim. It identifies a concrete obstruction to replacing graph-local permutation cycles by their stationary averaged split–merge generator.

## Exact covariance of a cycle-size observable

Let (G) be a connected weighted graph on (N\ge2) vertices and let each edge transposition occur at rate (c_{xy}). Start the interchange process (Sigma_t) in the uniform distribution on permutations. Its one-particle graph Laplacian is (Delta_G), with eigenvalues (0=\lambda_1<\lambda_2\le\cdots\le\lambda_N). Put

\[
 F(\sigma)=\#\{x:\sigma(x)=x\}-1.
\]

This observable depends only on cycle lengths: it is the number of singleton cycles minus one. Its mean is zero and variance is one. We claim the exact identity

\[
 \operatorname{Cov}(F(\Sigma_0),F(\Sigma_t))
 =\frac{\operatorname{Tr}(e^{-t\Delta_G})-1}{N-1}
 =\frac1{N-1}\sum_{j=2}^N e^{-\lambda_jt}.
\]

Write (Sigma_t=T_t\Sigma_0), with (T_t) independent of the initial uniform permutation. For a fixed permutation (	au), count ordered pairs of fixed-point events. If their indices coincide, both can hold only at a fixed point of (	au); if they differ, their prescribed images must differ. This gives

\[
 \mathbb E_\sigma[\operatorname{Fix}(\sigma)\operatorname{Fix}(\tau\sigma)]
 =\frac{\operatorname{Fix}(\tau)+N-2}{N-1},
\]

and therefore (mathbb E_\sigma[F(\sigma)F(\tau\sigma)]=(\operatorname{Fix}(\tau)-1)/(N-1)). A tagged particle in (T_t) follows the graph random walk, so (mathbb E\operatorname{Fix}(T_t)=\operatorname{Tr}(e^{-t\Delta_G})), proving the formula.

The eventual exponential decay rate of this cycle-size covariance is exactly (lambda_2(G)). On a unit-rate torus of side (L), this is (4\sin^2(\pi/L)\asymp L^{-2}). Thus even a size-only observable retains the diffusive time scale.

## What stationary projection would instead predict

Let (C_G=\sum_{\{x,y\}}c_{xy}). For every conjugacy-class function (f), uniformity and conjugation invariance make the mean squared change under each transposition identical. Hence its stationary forms satisfy

\[
 \mathcal E_G(f,f)=\frac{C_G}{\binom N2}\mathcal E_{K_N}(f,f),
\]

where every complete-graph edge has rate one. The stationary averaged generator on cycle types is therefore the complete-graph split–merge generator multiplied by (C_G/\binom N2). The complete-graph transposition gap is (N); this is also attained by the class function (F). The [interchange spectral-gap theorem](https://arxiv.org/pdf/0906.1238) consequently gives the averaged cycle-generator gap

\[
 \frac{2C_G}{N-1}.
\]

For graphs with bounded average degree this is of constant order, whereas the actual stationary cycle covariance can decay on a diffusive scale. There is no contradiction: the real cycle-type process on a general graph is not a Markov lumping of interchange.

For an explicit failure of lumpability, use the path (1-2-3-4). The permutations ((12)(34)) and ((13)(24)) both have cycle type (2+2). From the first, one path edge merges the cycles and two path edges split a cycle. From the second, all three path edges merge the cycles. Their exit rates to the same cycle-type classes differ.

This is why the stationary path-limit theorem of [Ioffe–Tóth](https://arxiv.org/html/1909.06188v2) must be distinguished from arbitrary-start mixing, and why a Dirichlet-form comparison alone must not be reinterpreted as an identity of projected trajectories. The new polymer TV proof avoids this issue: it differentiates the actual polymer density and uses the stationary energy identity at each time, without assuming cut-semigroup invariance.
