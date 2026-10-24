# P0248: optimized Cayley walk ? known-result rederivation

Status: author-checked rederivation of a literature-resolved historical question. This is excluded from the current-open target and original-solution count. No independent review of this proof is claimed.

Aldous?Fill, Conjecture/Open Problem 7.18, PDF page 253, asks whether a finite Cayley graph admits a symmetric generator distribution with relaxation time at most a universal constant times its squared diameter. Igor Pak, *Using stopping times to bound mixing times*, SODA 1999, Theorem 3.1, explicitly states that it resolves this question. The author-hosted PDF is internally dated October 31, 2004: https://www.math.ucla.edu/~pak/papers/soda4.pdf . The date of the archived copy is distinguished from the 1999 publication date.

## Construction and direct proof

Let the finite group be $G$, with inverse-closed generating set $S$ excluding the identity, and diameter $D$. For every $x\in G$, choose a geodesic word $w_x$ of length $\ell_x$. Randomize the word for $x$ equally between $w_x$ and the reversed, inverted word chosen for $x^{-1}$. Both words represent $x$ and have the same length. Let $N_s(x)$ be the number of occurrences of $s$ in this randomized word. Define

$$a_s=\frac1{|G|}\sum_x \ell_x\,\mathbb E N_s(x),\qquad A=\sum_s a_s=\frac1{|G|}\sum_x\ell_x^2\le D^2.$$

Inversion of words shows $a_s=a_{s^{-1}}$. Each $a_s>0$, because the word representing $s$ has length one. Thus $\mu(s)=a_s/A$ is a symmetric probability measure whose support is exactly $S$.

For a real function $f$ and uniform $\pi$, the independent uniform-pair identity is

$$\operatorname{Var}_\pi f=\frac1{2|G|^2}\sum_{z,x\in G}(f(zx)-f(z))^2.$$

Telescope along the chosen word for $x$ and use Cauchy?Schwarz. For each occurrence of $s$, translating the summation variable $z$ by the preceding prefix leaves the uniform sum unchanged. Therefore

$$\operatorname{Var}_\pi f\le\frac12\sum_s a_s\,\mathbb E_{z\sim\pi}(f(zs)-f(z))^2=A\,\mathcal E_\mu(f,f).$$

The variational characterization of the gap gives $\tau_2\le A\le D^2$. This is the continuous-time/rate-one spectral convention $\tau_2=(1-\lambda_2)^{-1}$; it is not a claim about absolute discrete-time eigenvalues when the graph is bipartite. Adding one-half holding makes aperiodic discrete-time mixing and changes the relaxation bound by a factor two.

## Second check and limits

The Aldous?Fill comparison theorem 7.16, with comparison increments uniform on the whole group, gives $\tau_2\le\max_s a_s/\mu(s)=A$. It independently reproduces the direct Dirichlet-form argument. The inversion randomization is necessary to justify symmetry in a noncommutative group; a deterministically chosen word table need not give symmetric counts.

This derivation was written before the Pak source was found in the campaign's later-literature check. Discovery order does not imply novelty. The open-problem record is now excluded and the argument survives only as a provenance-labelled mathematical contribution.
