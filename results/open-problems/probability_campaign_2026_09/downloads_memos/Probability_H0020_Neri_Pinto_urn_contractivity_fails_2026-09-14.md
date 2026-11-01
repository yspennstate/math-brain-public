# Neri and Pinto, Remark 3.7: the truncated-norm contractivity condition does not hold for every tenable irreducible urn

14 September 2026. Ledger row H0020 (intake H). Source: M. Neri and P. Pinto, *Quantitative limit theorems for generalized Pólya urns with applications to random tree models*, arXiv:2607.07309, Section 3, Remark 3.7.

## The question

A generalized Pólya urn with $d$ colours and replacement matrix $R$ has balance $\lambda$ when every row of $R$ sums to $\lambda$; it is tenable when off-diagonal entries are nonnegative and each negative diagonal entry $R_{ii} = -d_i$ has $d_i$ dividing its row and the initial count; it is irreducible when the directed graph of positive off-diagonal entries is strongly connected. Theorem 1.1 of the source (the classical law of large numbers, $U(n)/n \to \lambda u$ with $u$ the normalised left eigenvector) is recovered there from a quantitative theorem whose hypothesis is a contractivity condition in a truncated inner product. For $1 \le p \le d$ let $J_p = \mathrm{diag}(1, \dots, 1, 0, \dots, 0)$ with $p$ ones, $C_d = I$ and $C_{d-1} = [\,I_{d-1} \mid -\mathbf 1\,]$, a $(d-1) \times d$ matrix. Proposition 3.6 there shows that for mean-zero $w$,
$$\langle w, w(R - \lambda I)\rangle_p \le -A\,\|w\|_p^2, \qquad A = -\lambda_{\max}\big(\mathrm{symm}(C_pJ_p(R^{\mathsf T} - \lambda I)C_p^{\mathsf T})\big),$$
and the paper's rates follow when $A > \lambda/2$. Remark 3.7 reads: "If one can show that $\lambda_{\max}(\mathrm{symm}(C_pJ_p(R^{\mathsf T} - \lambda I)C_p^{\mathsf T})) < 0$ for $p = d$ or $d-1$ for all tenable, irreducible generalized Pólya urns, then not only would Theorem 1.1 follow, but one would also obtain quantitative rates for the almost sure and $L^2$ convergence ... This question remains open."

The answer is no, in both halves.

## $p = d$ never works

With $C_d = J_d = I$ the matrix is $\mathrm{symm}(R^{\mathsf T} - \lambda I)$, and for the all-ones vector $\mathbf 1^{\mathsf T}(R^{\mathsf T} - \lambda I)\mathbf 1 = \sum_{ij}R_{ij} - \lambda d = 0$ because every row sums to $\lambda$. So $\lambda_{\max} \ge 0$ for every balanced urn, and the $p = d$ condition fails always. (The remark's intention for $p = d$ can only have been the restriction to mean-zero vectors; that restriction is what $p = d - 1$ implements.)

## $p = d - 1$ fails for an explicit five-colour urn

For $p = d - 1$ the quadratic form is, with $\tilde w = C_{d-1}^{\mathsf T}w = (w_1, \dots, w_{d-1}, -\sum_{i<d}w_i)$ ranging over the mean-zero vectors,
$$Q(\tilde w) = \sum_{i=1}^{d-1}\tilde w_i\,\big(\tilde w(R - \lambda I)\big)_i ,$$
the standard inner product with the last coordinate dropped. Take $d = 5$, $\lambda = 6$ and
$$R = \begin{pmatrix} 0&0&4&0&2\\ 2&4&0&0&0\\ 0&0&3&3&0\\ 2&0&0&4&0\\ 0&6&0&0&0 \end{pmatrix}.$$
Every row sums to $6$, all entries are nonnegative (so the urn is tenable from any initial composition), and the graph of positive off-diagonal entries contains the cycles $1 \to 3 \to 4 \to 1$ and $1 \to 5 \to 2 \to 1$, so it is irreducible. For $\tilde w = (-1, 1, -1, -1, 2)$:
$$\tilde wR = (0, 16, -7, -7, -2), \qquad \tilde w(R - 6I) = (6, 10, -1, -1, -14), \qquad Q(\tilde w) = (-1)(6) + (1)(10) + (-1)(-1) + (-1)(-1) = 6 > 0.$$
So no $A > 0$ exists: the matrix $\mathrm{symm}(C_4J_4(R^{\mathsf T} - 6I)C_4^{\mathsf T})$, which is
$$\begin{pmatrix} -6 & -2 & 2 & 1\\ -2 & -8 & -3 & -3\\ 2 & -3 & -3 & 3/2\\ 1 & -3 & 3/2 & -2\end{pmatrix},$$
has $w^{\mathsf T}Gw = 6$ at $w = (-1, 1, -1, -1)$ and largest eigenvalue $1.9779$.

The example came from a random search over integer replacement matrices with nonnegative entries (`h0020_search.py`, `h0020_search2.py`); the largest value found with a negative diagonal (tenable by divisibility) was $2.77$ on four colours. On three colours no violation was found under any ordering of the colours in 60,000 trials (largest value $-0.70$), and on four colours violations exist for some orderings but not for all orderings of the same urn in 40,000 trials; whether some urn violates the condition under every ordering of its colours, and whether three-colour urns always satisfy it, are recorded as questions.

## What this does and does not say

The source's Theorem 3.3 is a sufficient condition and its applications (the three tree models) verify the hypothesis directly, so nothing in the paper is affected. What fails is the hope expressed in Remark 3.7 that the truncated-norm contractivity is universal: it is not, so a proof of Theorem 1.1 with rates along those lines needs either a different norm (the natural candidate is the $\pi$-weighted or eigenvector-adapted inner product in which $R - \lambda I$ is dissipative on the mean-zero space, as in the standard spectral proofs) or a case distinction. Author checked, exact integer arithmetic for the witness, no independent read.
