# P0276: unweighted Abelian Cayley graphs with the product condition and no cutoff

Status: complete author-checked counterexample candidate to the literal unrestricted statement of Salez Problem 2.4. A scoped independent review is recorded below; novelty remains unverified. This construction has unbounded degree. It does not address a bounded-degree or random-generator version of the question.

## Primary source and scope

Justin Salez, *Modern aspects of Markov chains: entropy, curvature and the cutoff phenomenon*, arXiv:2508.21055, Problem 2.4, PDF page 27; the definitions are on pages 25-26. Primary PDF: https://arxiv.org/pdf/2508.21055 . Archived SHA256: 9b58f5e6c2b13103f9ca02ddd53b7890e259b2d93f632c25d3414dd87002e267.

The source defines the unweighted Cayley walk by uniform choice from a generating set. It asks whether cutoff is equivalent to the product condition for Abelian Cayley graphs, without a degree bound in that question. The subsequent paragraph separately introduces weighted increment laws. Therefore a weighted reset walk alone would not answer it. The construction below is a connected simple undirected unweighted Cayley graph and controls its entire state-space law.

The reset mechanism is classical prior art (often associated with Pak counterexamples); novelty, if any, would concern this exact unweighted realization and its application to the literal source statement. No novelty claim is made here. Earlier and later formulations may impose additional restrictions that this construction does not satisfy.

## The graph and its exact rates

For integers $d\ge8$, set

$$m_d=1+\left\lceil\frac{2^d\log d}{4}\right\rceil,
\qquad G_d=(\mathbb Z/2\mathbb Z)^d\times(\mathbb Z/m_d\mathbb Z).$$

Write $H_d=(\mathbb Z/2\mathbb Z)^d$, $K_d=\mathbb Z/m_d\mathbb Z$, and let $e_i$ be the cube basis vectors. The generating set is the disjoint union

$$S_d=\{(e_i,k):1\le i\le d,\ k\in K_d\setminus\{0\}\}
\ \cup\ \{(x,0):x\in H_d\setminus\{0\}\}.$$

It contains no identity and is inverse closed. The second part generates the cube factor, and adding $(e_1,0)$ to $(e_1,k)$ generates $(0,k)$, so it generates the full group. The Cayley graph is consequently simple, connected, undirected and vertex transitive. Every edge has the same transition weight. Its degree is

$$D_d=d(m_d-1)+2^d-1.$$

Use the rate-one continuization of simple random walk, whose generator is $P-I$. Split its jumps into local-type and global-type events. Their rates are

$$\alpha_d=\frac{d(m_d-1)}{D_d},\qquad
\theta_d=\frac{2^d-1}{D_d},\qquad
\beta_d=\frac{2^d}{D_d}.$$

On a local event the cube flips a uniformly chosen coordinate and the second coordinate receives an independent uniform nonzero increment. On a global event the cube receives a uniform nonzero increment and the second coordinate is unchanged.

## Exact projected semigroup

Let $L_d$ be the rate-one cube generator, and $\Pi_d$ the projection onto the uniform law on $H_d$. The transition operator for a uniform nonzero cube increment is

$$Q_d=\frac{2^d\Pi_d-I}{2^d-1}.$$

Therefore the cube projection has generator

$$\alpha_dL_d+\theta_d(Q_d-I)
=\alpha_dL_d+\beta_d(\Pi_d-I).$$

Since $\Pi_d$ commutes with the cube semigroup, if $q_d(t)$ is its total-variation distance from uniform when started at zero and $c_d(t)$ is the corresponding distance for rate-one cube walk, then

$$q_d(t)=e^{-\beta_dt}\,c_d(\alpha_dt).$$

This is exact; no replacement of a nonzero increment by an approximate reset is used.

## Control of the whole graph, not just its projection

Let $v_d(t)$ denote the total-variation distance of the full walk from the uniform law on $G_d$. Projection gives $v_d(t)\ge q_d(t)$. Let $N_t$ count local-type events, so $N_t$ is Poisson of mean $\alpha_dt$.

Conditional on the event types, their times, and all cube increments, the second coordinate is the sum of $N_t$ independent uniform nonzero $K_d$ increments. When $N_t\ge1$, its distance from uniform is at most $1/m_d$: the first increment has exactly that distance and subsequent convolution contracts total variation. When $N_t=0$, use the bound one. Coupling this conditional law to an independent uniform coordinate yields

$$0\le v_d(t)-q_d(t)\le e^{-\alpha_dt}+\frac1{m_d}.$$

Conditioning on the cube path is legitimate because local increments in the two factors are chosen independently given the event type. Their common jump count does not invalidate the conditional bound. Uniformity of an auxiliary coordinate is not silently assumed.

## A self-contained cube cutoff calculation

Define the comparison time

$$T_d=\frac{d\log d}{4\alpha_d}.$$

The rate-one cube coordinates flip independently at rate $1/d$. Their signs have means $e^{-2t/d}$ from the all-zero start. Hence

$$\chi^2(\mathcal L(X_t),\operatorname{Unif}(H_d))
=(1+e^{-4t/d})^d-1.$$

At $t=sd\log d/4$ this tends to zero for $s>1$, proving $c_d(t)\to0$. For $0<s<1$, the sum of coordinate signs has mean $d^{1-s/2}$ and variance at most $d$, while its stationary mean is zero and stationary variance is $d$. Chebyshev applied at half the former mean under both laws gives

$$c_d(sd\log d/4)\ge1-8d^{s-1}\longrightarrow1.$$

Also

$$\beta_dT_d=\frac{2^d\log d}{4(m_d-1)}\longrightarrow1.$$

Combining the exact projected formula with the whole-space error bound proves the limiting profile away from $s=1$:

$$\lim_{d\to\infty}v_d(sT_d)=
\begin{cases}e^{-s},&0<s<1,\\0,&s>1.\end{cases}$$

The large drop near $s=1$ does not constitute cutoff: a nonvanishing fraction of total-variation decay has already occurred gradually over a time proportional to $T_d$.

## Spectral gap and the product condition

Characters of $G_d$ are indexed by a subset $A\subseteq\{1,\ldots,d\}$ and a character $\psi$ of $K_d$. Put $a=|A|$. The eigenvalues of the discrete jump operator are

$$\lambda_{A,\psi}=\frac{(d-2a)c_\psi+b_A}{D_d},\qquad
c_\psi=\begin{cases}m_d-1,&\psi=1,\\-1,&\psi\ne1,\end{cases}
\quad b_A=\begin{cases}2^d-1,&A=\varnothing,\\-1,&A\ne\varnothing.\end{cases}$$

The three nonconstant sectors have gap candidates

$$\frac{2a(m_d-1)+2^d}{D_d}\quad(a\ge1,\psi=1),\qquad
\frac{dm_d}{D_d}\quad(A=\varnothing,\psi\ne1),\qquad
\frac{D_d+d-2a+1}{D_d}\quad(A\ne\varnothing,\psi\ne1).$$

For all sufficiently large $d$ the minimum is in the first sector at $a=1$. Thus

$$\gamma_d=\frac{2(m_d-1)+2^d}{D_d}
=\frac{2\alpha_d}{d}+\beta_d\sim\frac2d.$$

This also follows by noting that every nonconstant auxiliary-factor character is contracted at a rate bounded away from zero, while the first cube character has the displayed slow rate. The full character computation checks that a hidden auxiliary bottleneck has not been overlooked.

Write $t_d(\varepsilon)=\inf\{t:v_d(t)\le\varepsilon\}$. Monotonicity and the limiting profile imply

$$\frac{t_d(1/4)}{T_d}\longrightarrow1,\qquad
\frac{t_d(3/4)}{T_d}\longrightarrow\log(4/3).$$

For the first assertion, $e^{-s}>e^{-1}>1/4$ for every $s<1$, whereas the limit is zero for $s>1$. For the second, $e^{-s}$ crosses $3/4$ at the interior point $s=\log(4/3)$, so bracketing on either side gives the limit. Therefore

$$\gamma_d t_d(1/4)\sim\frac12\log d\longrightarrow\infty,
\qquad \frac{t_d(3/4)}{t_d(1/4)}\longrightarrow\log(4/3)<1.$$

The product condition holds and total-variation cutoff fails. By transitivity these are also the worst-start mixing times.

## Review limits

The potentially surprising assertion is that uniform generators can encode the rare-reset mechanism. Its load-bearing checks are disjointness and inverse closure of the generator set; exact projected reset rate $\beta_d$, which is different from the actual global jump rate $\theta_d$; conditional mixing of the auxiliary factor; the full character spectrum; and the distinction between a discontinuity in the limiting profile and cutoff. Each is derived above.

The construction has very large degree and specially chosen generators. It says nothing against the bounded-degree transitive-expander problem or almost-sure cutoff for uniformly random generating sets. Searches found both the literal Salez statement and related nilpotent-group conjecture formulations, but no verified prior disposition of this exact construction. The simple mechanism makes prior-art checking essential. This packet remains a candidate, with no promoted original solution count.


## Scoped independent review receipt

Root independently reviewed the proof pinned at SHA256 80633cef95af21172e4fc4f0f4c67c89845f5222e9806b74d8de721b4b64dbeb. Its report is at `~/<private-repo>/12_cognitive_architecture/audits/reports/2026/09/06/last200-implementation/P0276_unweighted_abelian_candidate_review.md`, SHA256 ee332a2aa7f3ab31cb0ae91a0a745f84eb2b21e0c18f028869602cfdf1b90e7b. The reviewer checked 8 graphs, 360 characters, 2720 projection entries, 16 conditional convolutions, 10 product-mass cases and 18 rejected bad controls, as well as the full total-variation coupling, spectrum and mixing-time brackets. No mathematical gap was found in that scope. The unbounded degree and chosen generators remain essential. Human review, unique live review node, present openness and novelty remain pending. This receipt is a scoped review, not original-solution promotion.
