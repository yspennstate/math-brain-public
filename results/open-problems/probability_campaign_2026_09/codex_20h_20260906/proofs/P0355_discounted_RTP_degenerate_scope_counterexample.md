# P0355: A degenerate case omitted by the discounted-tree nonendogeny conjecture

Status: author-checked literal-scope counterexample, retained as a partial candidate because strict discounting and nondegeneracy would exclude it. No current-open or originality certification. It is a sourced conjecture, not a newly invented problem; its substantive intended nondegenerate regime remains unsolved here.

Source: Aldous and Bandyopadhyay, *A survey of max-type recursive distributional equations*, Annals of Applied Probability 15 (2005), 1047-1110. Conjecture 34 and Corollary 33, journal page 1075, PDF page 29; definitions and preceding sufficient theorem on PDF pages 26-28. Primary author PDF: https://www.stat.berkeley.edu/~aldous/Papers/me107.pdf . The exact archived bytes are pinned in the source registry under `aldous_rde_2005`.

## Exact scope

The displayed equation is

$$X\overset d=\eta+\max_i\xi_iX_i,\qquad X\in\mathbb R_+.$$

Corollary 33 assumes that the supremum of discounted ray sums is finite, and that the homogeneous equation obtained by removing $\eta$ has a nonzero solution $Y$. Condition (39) adds independence of $\eta$ and the weights, and that zero belongs to the support of $\eta$. Its parenthetical reference says the hypotheses of Theorem 32 are one sufficient way to obtain the finite supremum; it does not state that they are mandatory. In particular, the strict inequalities $\xi_i<1$ in Theorem 32 are not repeated as assumptions of Corollary 33. The state space includes zero, as confirmed by the source's repeated use of $\delta_0$ and $\eta\ge0$.

Conjecture 34 asserts that the invariant recursive tree process with marginal $\mu_a$, obtained by iterating the equation from the law of $aY$, is nonendogenous whenever $a>0$.

## Construction and two checks

Use the deterministic full binary tree and, at every vertex, take

$$N=2,\qquad \eta=0,\qquad \xi_1=\xi_2=1,\qquad Y=1.$$

Every discounted ray sum is zero, so its supremum is the finite random variable $X=0$. The homogeneous equation holds exactly because $\max(1,1)=1$. The variable $\eta$ is independent of the deterministic weight vector and its support is $\{0\}$. For every $a\ge0$, the distributional operator fixes $\delta_a$:

$$T(\delta_a)=\delta_{\max(a,a)}=\delta_a.$$

Consequently $T^n(\operatorname{law}(aY))=\delta_a$ for every $n$, so the source's $\mu_a$ is exactly $\delta_a$, and these measures are distinct as $a$ varies.

On the entire tree set every vertex variable equal to $a$. This is an invariant recursive tree process: its recursion holds, variables at any finite boundary are independent constants with the required common marginal, and they are independent of all ancestral innovations. The root is a constant, hence measurable with respect to the innovation sigma-field. The process is endogenous.

An independent formulation uses conditional laws. Given all innovations, the conditional root law is $\delta_a$; two conditionally independent copies therefore agree with probability one. Equivalently the only coupling with both marginals $\delta_a$ is the diagonal point mass $\delta_{(a,a)}$. Both checks contradict the literal nonendogeny conclusion.

## Why the restriction matters

This example uses both zero additive marks and unit edge weights. Replacing the marks by the positive constant one makes every ray sum infinite, violating the finite-supremum hypothesis. Replacing both weights by a deterministic $c<1$ makes the constant positive $Y$ cease to solve the homogeneous equation, since $\max(cY,cY)=cY\ne Y$. These controls expose the two load-bearing boundary choices.

The example does not answer a revised conjecture with strict discounts, nonzero additive marks, or suitable nondegeneracy assumptions. Later work on bounded discounted tree sums often explicitly assumes positive additive marks, so this observation does not contradict those theorems. A bounded search for the precise conjecture did not identify a published correction; failure to find one is not evidence of novelty.
