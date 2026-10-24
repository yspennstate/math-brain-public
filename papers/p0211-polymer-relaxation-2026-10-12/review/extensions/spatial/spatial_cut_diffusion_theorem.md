# A spatial cut-diffusion extension in the rare-fragmentation regime

Research note, 12 October 2026. This is a new model-specific derivation for the extension project, not part of the existing manuscript. No claim of literature priority is made. The model retains the count-dependent reaction rates of the original cut chain and adds graph-local boundary transport; it is not a theorem for arbitrary spatial coagulation–fragmentation systems.

## Model

Let \(G=(V,E,c)\) be a finite weighted graph with \(N=|V|\ge2\). Write
\[
 (\Delta_G a)(x)=\sum_y c_{xy}(a(x)-a(y)), \qquad
 \lambda_G=\lambda_2(\Delta_G).
\]
Assume \(G\) is connected for the spatial interpretation. The result also allows a disconnected graph if \(\lambda_2=0\) is used.

The state space is the collection of nonempty subsets \(S\subseteq V\), with \(k=|S|\). At an absent site add a cut at rate \(\beta\); at a present site remove it at rate \((k-1)/N\). In addition, interchange occupancy across edge \(xy\) at rate \(D c_{xy}\). Equivalently,
\[
 (\mathcal L_{\beta,D,G} f)(S)
 =\beta\sum_{x\notin S}[f(S+x)-f(S)]
 +\frac{k-1}{N}\sum_{x\in S}[f(S-x)-f(S)]
 +D\sum_{\{x,y\}\in E}c_{xy}[f(S^{xy})-f(S)].
\]
The last sum vanishes when the endpoints have the same occupancy. The deletion term is zero at \(k=1\).

The reversible law remains
\[
 \pi_\beta(S)=Z^{-1}\frac{(\beta N)^k}{(k-1)!}.
\]
Indeed the reaction detailed-balance ratio from size \(k\) to \(k+1\) is \(\beta N/k\), and every occupancy swap preserves \(k\).

On a cycle, cuts define neighboring intervals. A birth splits an interval, a death merges adjacent intervals, and a swap of an occupied cut with a neighboring vacancy moves an interval boundary by one lattice step. The neighboring interval lengths remain positive. The full cut configuration, including positions, is the Markov state; its unordered interval lengths generally are not Markov.

## Theorem

Suppose
\[
 0<\beta\le N^{-2},\qquad D\ge0,\qquad c_0=1-2^{-1/2}.
\]
Let \(\gamma_{\mathrm{sp}}\) be the spectral gap of this full finite chain. Then
\[
 \boxed{\quad
 \min\left\{\frac2N,\;c_0N\beta+D\lambda_G\right\}
 \le \gamma_{\mathrm{sp}}
 \le
 \min\left\{\beta+\frac4N,\;\frac{N\beta}{2}+D\lambda_G\right\}.
 \quad}
\]
In particular,
\[
 c_0\min\left\{\frac1N,N\beta+D\lambda_G\right\}
 \le\gamma_{\mathrm{sp}}
 \le\frac92\min\left\{\frac1N,N\beta+D\lambda_G\right\}.
\]

On the cycle \(C_N\), \(N\ge3\), with each edge weight one,
\[
 \lambda_G=4\sin^2(\pi/N),\qquad
 \gamma_{\mathrm{sp}}\asymp
 \min\left\{N^{-1},N\beta+D N^{-2}\right\}.
\]
On a \(d\)-dimensional discrete torus of side \(L\ge3\), \(N=L^d\), the same graph eigenvalue is \(4\sin^2(\pi/L)\), giving
\[
 \gamma_{\mathrm{sp}}\asymp
 \min\left\{N^{-1},N\beta+D L^{-2}\right\}.
\]
For a torus in higher dimension the subset dynamics remains well-defined as reaction and diffusion of cuts/particles; it does not represent contiguous one-dimensional interval lengths.

## Proof

We use the complete Boolean harmonic decomposition established in the existing P0211 proof. It is important here that the decomposition is invariant under every coordinate permutation. Consequently each graph-edge transposition preserves every degree, even though the graph-swap generator is generally not invariant under all permutations.

For harmonic degree \(\ell\), the reaction generator is the one-dimensional killed operator
\[
 (A_\ell h)(k)
 =\beta(N-k-\ell)[h(k+1)-h(k)]
 +\frac{(k-1)(k-\ell)}N[h(k-1)-h(k)]
 -\left(\ell\beta+\frac{\ell(k-1)}N\right)h(k)
\]
on \(\ell\le k\le N-\ell\). Degree zero is the autonomous count chain on \(1,\ldots,N\), with birth rates \(\beta(N-k)\) and death rates \(k(k-1)/N\).

### Degree zero

The swap generator is zero on functions of \(k\). From the existing count-chain estimates,
\[
 \beta+\frac2N\le\gamma_Q
 \le\beta+4\max\{\sqrt\beta,N^{-1}\}
 =\beta+\frac4N.
\]
Thus all nonconstant radial functions have energy at least \(2/N\) times their variance, and they supply the first upper bound.

### Degrees at least two

The killing potential is at least
\[
 \ell\beta+\frac{\ell(\ell-1)}N\ge\frac2N.
\]
The birth–death portion has nonnegative Dirichlet form. The added graph-swap portion also has nonnegative Dirichlet form. Hence the sum has rate at least \(2/N\) on the direct sum of degrees \(\ell\ge2\). There is no need to estimate the graph spectrum in these sectors.

### Degree one

Let \(\eta_1\) denote the principal eigenvalue of \(-A_1\). We first prove
\[
 c_0N\beta\le\eta_1\le N\beta/2.
\]

For the upper bound use \(h(k)=1/k\), which is strictly positive on \(1,\ldots,N-1\). Direct cancellation gives
\[
 -\frac{A_1h(k)}{h(k)}=\frac{\beta N}{k+1}\le\frac{\beta N}{2}.
\]
The finite positive-vector comparison principle gives the desired upper bound.

For the lower bound use \(h(k)=k^{-1/2}\). At \(k=1\),
\[
 -\frac{A_1h(1)}{h(1)}
 =\beta+\beta(N-2)(1-2^{-1/2})
 \ge c_0N\beta.
\]
For \(k\ge2\), all birth contributions are nonnegative, while the death and killing terms give
\[
 -\frac{A_1h(k)}{h(k)}
 \ge\frac{k-1}{N}
 \left[1-(k-1)\left(\sqrt{\frac{k}{k-1}}-1\right)\right].
\]
Since
\[
 (k-1)\left(\sqrt{\frac{k}{k-1}}-1\right)
 =\frac1{\sqrt{k/(k-1)}+1}\le\frac12,
\]
the last display is at least \(1/(2N)\). The assumption \(\beta\le N^{-2}\) implies
\[
 \frac1{2N}\ge c_0N\beta.
\]
Positive-vector comparison now proves the lower bound for \(\eta_1\). For \(N=2\) there is only the state \(k=1\) in this sector, and the same conclusion holds directly.

Every degree-one function has the form
\[
 f(S)=\sum_j h_j(k)H_{a_j}(S),\qquad
 H_a(S)=\sum_{x\in S}a(x),\quad \sum_xa(x)=0.
\]
The graph swaps act on \(H_a\) as \(-H_{\Delta_G a}\). They do not change \(k\). Taking an eigenbasis of \(\Delta_G\) on the mean-zero subspace therefore reduces the combined generator to the independent operators
\[
 A_1-D\lambda_j I,\qquad j=2,\ldots,N.
\]
The smallest degree-one rate is exactly \(\eta_1+D\lambda_G\).

The degree subspaces are orthogonal and invariant for both parts of the generator. Combining degree zero, degree one, and degrees at least two yields the boxed inequalities. The simpler two-sided comparison follows because \(c_0<1\) and
\(\beta+4/N\le(9/2)N^{-1}\).

## What this establishes

The theorem isolates two distinct mechanisms. When there is usually one cut, reaction moves its location only by creating and then removing an additional cut, at an effective scale \(N\beta\). Local swaps move it diffusively at scale \(D\lambda_G\). The count mode caps the spectral gap at order \(1/N\).

This is a mathematically concrete extension with an explicit spatial bottleneck and a complete proof based on the existing harmonic machinery. The proof does not use the general Caputo–Liggett–Richthammer theorem: only the elementary degree-one graph action is needed. It is not yet a TV mixing theorem, a sharp-constant result, or a universality statement for other spatial reaction kernels.

The harmonic decomposition and positive-vector comparison remain established tools, credited in the earlier manuscript and its bibliography. Before presenting this new model-specific theorem as a publication, it should receive an independent proof check and a targeted priority review of reaction–diffusion subset chains.

