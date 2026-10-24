# Exact spectral gap for cut reactions with graph diffusion

Combined derivation by the extension working group, 12 October 2026. This is a research note for the new extension project, not a modification of the earlier manuscript. The proof below was checked algebraically, including sector endpoints. The general harmonic decomposition and positive-vector method are established tools. Novelty of this particular reaction–diffusion theorem remains subject to a targeted literature check.

## 1. Model and exact theorem

Let \(G=(V,E,c)\) be a connected weighted graph on \(N\ge2\) vertices, with symmetric nonnegative edge rates \(c_{xy}\). Let \(\lambda_G\) be the first positive eigenvalue of its random-walk Laplacian
\[
 \Delta_G a(x)=\sum_yc_{xy}(a(x)-a(y)).
\]
On nonempty subsets \(S\subseteq V\), \(k=|S|\), define
\[
 \begin{split}
 (\mathcal L_{\beta,D,G}f)(S)
 ={}&\beta\sum_{x\notin S}[f(S+x)-f(S)]\\
 &+\frac{k-1}{N}\sum_{x\in S}[f(S-x)-f(S)]\\
 &+D\sum_{\{x,y\}\in E}c_{xy}[f(S^{xy})-f(S)],
 \end{split}
\]
where \(\beta>0,D\ge0\), and \(S^{xy}\) swaps the occupancy of \(x,y\). The deletion rate at \(k=1\) is zero. Its reversible law is
\[
 \pi_\beta(S)=Z^{-1}\frac{(\beta N)^k}{(k-1)!}.
\]
The swap term preserves cardinality and is reversible for this same law.

Let \(Q\) be the cardinality chain,
\[
 Q(k,k+1)=\beta(N-k),\qquad Q(k,k-1)=k(k-1)/N,
\]
and write \(\gamma_Q\) for its gap. On \(k=1,\ldots,N-1\), define
\[
 \begin{split}
 (A_1h)(k)
 ={}&\beta(N-k-1)[h(k+1)-h(k)]\\
 &+\frac{(k-1)^2}{N}[h(k-1)-h(k)]
 -\left(\beta+\frac{k-1}{N}\right)h(k).
 \end{split}
\]
Terms with zero endpoint rates are omitted. Let \(\eta_1\) be the smallest eigenvalue of \(-A_1\).

**Exact theorem.** For every \(N,\beta,D,G\) as above,
\[
 \boxed{\displaystyle
 \gamma_{\mathrm{sp}}(N,\beta,D,G)
 =\min\{\gamma_Q(N,\beta),\ \eta_1(N,\beta)+D\lambda_G\}.}
\]
Moreover,
\[
 \eta_1\le\gamma_Q-\frac2N.
\]
In particular, at \(D=0\), the full cut-chain gap is exactly \(\eta_1\).

Set
\[
 s=\beta+\sqrt\beta+N^{-1},\qquad
 u=\beta+\min\{N\beta,\sqrt\beta\}.
\]
Then
\[
 \frac{u}{8}\le\eta_1\le u,\qquad
 \frac{s}{6}\le\gamma_Q\le4s,
\]
and consequently
\[
 \boxed{\displaystyle
 \frac18\min\{s,u+D\lambda_G\}
 \le\gamma_{\mathrm{sp}}
 \le4\min\{s,u+D\lambda_G\}.}
\]

The graph enters the exact gap through its one-particle random-walk gap alone. The proof does not invoke the general interchange-process spectral-gap theorem: higher harmonic sectors are already too fast to determine this model's gap.

## 2. A ratio lemma for the count derivative

The derivative of \(Q\) is the killed operator \(A\) on \(i=1,\ldots,N-1\) with rates and killing
\[
 \lambda_i=\beta(N-i-1),\qquad
 \mu_i=i(i-1)/N,\qquad V_i=\beta+2i/N.
\]
The nonzero spectrum of \(-Q\) is the spectrum of \(-A\). Let \(h>0\) satisfy
\[
 -Ah=\gamma_Qh.
\]
We claim
\[
 \frac{h(i+1)}{h(i)}\ge\frac12\qquad(1\le i\le N-2).
\]

If \(r=h(i+1)/h(i)<1/2\) is the global minimum forward ratio, the eigenvalue equation at \(i\) gives
\[
 \gamma_Q\ge\lambda_i(1-r)+\mu_i(1-r^{-1})+V_i,
\]
while that at \(i+1\) gives
\[
 \gamma_Q\le\lambda_{i+1}(1-r)+\mu_{i+1}(1-r^{-1})+V_{i+1}.
\]
Subtracting produces
\[
 0\ge\beta(1-r)+\frac{2i}{N}(r^{-1}-1)-\frac2N>0,
\]
a contradiction. At \(i=1\) the missing backward ratio is multiplied by \(\mu_1=0\); at \(i=N-2\) the missing next forward ratio is multiplied by \(\lambda_{N-1}=0\). For \(N=2\) there is no ratio to check.

## 3. Higher reaction sectors lie above the count gap

The Boolean harmonic decomposition expresses the reaction generator in degree \(\ell\) as \(A_\ell\) tensored with the identity on the degree-\(\ell\) harmonic space, where
\[
 \begin{split}
 (A_\ell g)(k)
 ={}&\beta(N-k-\ell)[g(k+1)-g(k)]\\
 &+\frac{(k-1)(k-\ell)}N[g(k-1)-g(k)]\\
 &-\left(\ell\beta+\frac{\ell(k-1)}N\right)g(k),
 \qquad \ell\le k\le N-\ell .
 \end{split}
\]
For \(\ell\ge2\), let \(r=k-\ell+1\) and \(g(k)=h(r)\). Subtracting the count-derivative eigenvalue equation gives the identity
\[
 \begin{split}
 -\frac{A_\ell g(k)}{g(k)}
 ={}&\gamma_Q
 +(\ell-1)\beta\left[2\frac{h(r+1)}{h(r)}-1\right]\\
 &+\frac{\ell-2}{N}
 \left[(r+\ell)-(r-1)\left(\frac{h(r-1)}{h(r)}-1\right)\right].
 \end{split}
\]
The first extra term is nonnegative by the ratio lemma. The backward ratio is at most two, so the bracket is at least \(\ell+1\). Therefore
\[
 \inf\operatorname{Spec}(-A_\ell)
 \ge\gamma_Q+\frac{(\ell-2)(\ell+1)}N
 \ge\gamma_Q.
\]
Positive-vector comparison justifies the first inequality.

Endpoint check: at \(r=1\), the term involving \(h(r-1)\) is omitted because its coefficient is zero. At the upper endpoint \(r=N-2\ell+1\), \(r+1\le N-1\), so the forward ratio is available, even though the original degree-\(\ell\) birth rate is zero.

As an additional consequence, compare \(A\) directly with \(A_1\) at the same index:
\[
 \frac{(A-A_1)h(i)}{h(i)}
 =\frac{(i-1)h(i-1)/h(i)-2i}{N}\le-\frac2N.
\]
The \(i=1\) expression is interpreted with zero backward term and equals \(-2/N\). Hence
\[
 -A_1h/h\le\gamma_Q-2/N,
\]
and positive-vector comparison proves \(\eta_1\le\gamma_Q-2/N\).

The same sector comparison, combined with cyclic invariance of polymer observables, supplies an independent proof of the earlier equality between the unlabelled polymer gap and the count gap. Granovsky–Erlihson already discuss that equality; it must not be advertised as a newly discovered equality.

## 4. Why the graph contribution is exact

Every coordinate permutation preserves each harmonic degree. The graph swap generator, being a nonnegative linear combination of these permutations minus the identity, therefore preserves the degree subspaces. Within degree \(\ell\), reactions act on the radial factor and graph swaps on the harmonic factor. Equivalently,
\[
 \mathcal L_{\beta,D,G}\big|_\ell
 =A_\ell\otimes I+I\otimes D\mathcal S_{G,\ell}.
\]
The inner product factors into the radial reversible weight and the harmonic inner product. Each \(-\mathcal S_{G,\ell}\) is nonnegative.

In degree zero the swaps are zero, and the first positive rate is \(\gamma_Q\). In degrees \(\ell\ge2\), the preceding comparison and nonnegativity of the swap form keep every rate at least \(\gamma_Q\).

In degree one write
\[
 H_a(S)=\sum_{x\in S}a(x),\qquad \sum_xa(x)=0.
\]
A direct calculation gives
\[
 \mathcal S_G H_a=-H_{\Delta_G a}.
\]
Thus the degree-one rates are the sums of the eigenvalues of \(-A_1\) and \(D\Delta_G\) restricted to mean-zero vectors. Their minimum is \(\eta_1+D\lambda_G\). Taking the minimum over degrees proves the exact formula.

## 5. Uniform estimate of the degree-one eigenvalue

### Upper bounds

The positive function \(h(k)=1/k\) gives
\[
 -A_1h/h=\frac{\beta N}{k+1}\le\frac{N\beta}{2}.
\]

There is also a useful global upper bound without a pointwise supersolution. Write \(j=k-1\). The birth–death part of \(A_1\), before killing, has birth \(\beta(N-2-j)\), death \(j^2/N\), and invariant law \(\nu\). Stationarity applied to \(j\) yields
\[
 \mathbb E_\nu j^2
 =\beta N(N-2-\mathbb E_\nu j)\le\beta N^2.
\]
Testing the killed Rayleigh quotient with the constant function therefore gives
\[
 \eta_1\le\beta+\frac{\mathbb E_\nu j}{N}
 \le\beta+\sqrt\beta.
\]
For \(N=2\), this is the one-state chain \(j=0\), and the same calculation is valid. Together the two upper bounds imply \(\eta_1\le u\).

### Lower bounds

Killing immediately gives \(\eta_1\ge\beta\). Another positive function, \(h(k)=k^{-1/2}\), gives at \(k=1\)
\[
 -A_1h/h
 =\beta+\beta(N-2)(1-2^{-1/2})
 \ge c_0N\beta,\qquad c_0=1-2^{-1/2}.
\]
At \(k\ge2\), the nonnegative birth term can be discarded, and
\[
 -A_1h/h\ge
 \frac{k-1}{N}\left[1-(k-1)\left(\sqrt{\frac{k}{k-1}}-1\right)\right]
 \ge\frac1{2N}.
\]
Thus
\[
 \eta_1\ge\min\{c_0N\beta,(2N)^{-1}\}.
\]

In the middle range \(N\ge8,\ 4/N^2\le\beta\le1/16\), set \(a=N\sqrt\beta\), so \(2\le a\le N/4\), and use \(h(k)=1/(k+a)\). Direct cancellation gives
\[
 -A_1h/h
 =\beta+\frac{\beta(N-k-1)}{k+a+1}
 +\frac{a(k-1)}{N(k+a-1)}.
\]
If \(k\le a\), the second term is at least \(\sqrt\beta/5\). If \(k\ge a\), the last term is at least \(\sqrt\beta/4\). Therefore \(\eta_1\ge\sqrt\beta/5\).

These estimates give \(\eta_1\ge u/8\) in all regimes:

- If \(\beta\le N^{-2}\), then \(u=(N+1)\beta\) and \(c_0N\beta\ge u/8\).
- If \(N\le7\) and \(\beta\ge N^{-2}\), then \(u=\beta+\sqrt\beta\le8\beta\).
- If \(N\ge8\) and \(N^{-2}\le\beta\le4N^{-2}\), the preceding reciprocal-square-root bound gives \(\eta_1\ge c_0/N\ge\sqrt\beta/7\), since \(c_0\ge2/7\); combine with \(\eta_1\ge\beta\).
- In the middle range, \(\eta_1\ge\max\{\beta,\sqrt\beta/5\}\ge u/6\).
- If \(\beta\ge1/16\), then \(u\le5\beta\).

Together with the established count-chain bounds, these prove the displayed uniform spatial estimate.

## 6. Spatial interpretation and limits

For \(0<\beta\le N^{-2}\), the sharper estimates from the same proof are
\[
 \min\{2/N,c_0N\beta+D\lambda_G\}
 \le\gamma_{\mathrm{sp}}
 \le\min\{\beta+4/N,N\beta/2+D\lambda_G\}.
\]
Hence the rare-fragmentation rate is
\[
 \gamma_{\mathrm{sp}}\asymp\min\{N^{-1},N\beta+D\lambda_G\}.
\]
For a unit-rate cycle, \(\lambda_G=4\sin^2(\pi/N)\); on a discrete torus of side \(L\ge3\), it is \(4\sin^2(\pi/L)\). This displays the diffusive bottleneck explicitly.

The model is a genuine Markov process on spatial cut configurations. On a cycle, the swaps transport interval boundaries. Its reaction rate still depends on the global cut count, and its stationary law remains exchangeable. These special features are what make the exact reduction possible. The result does not cover arbitrary size-dependent adjacent coagulation, spatially varying equilibrium weights, nonstationary random-interchange cycle limits, or sharp TV mixing.

The estimate is proved here; its priority and publication significance have not been independently certified. The spatial literature reviewed separately should guide the next, less symmetric model.

