# P0249: reversibilization trace inequality ? known-result consequence

Status: author-checked complete argument for a historical conjecture. A later primary theorem implies the result, so this entry is excluded from the current-open target and original-solution count. The direct matrix proof is not independently reviewed here.

Source question: Aldous?Fill, Conjecture 9.22, PDF pages 327?329, asks whether $\operatorname{tr}[Z^2(P^*-P)]\ge0$. Here $P$ is an irreducible finite-state transition matrix, $P^*$ its adjoint in $L^2(\pi)$, and $Z$ the centered fundamental matrix. The centered convention is $Z1=0$ and $Z=(I-P)^{-1}$ on $L^2_0(\pi)$. Adding the constant projection to $Z$ would not change the displayed product.

## Direct matrix proof

Restrict all operators to the finite-dimensional real Hilbert space $L^2_0(\pi)$. Put

$$A=I-P=H+K,\quad H=\frac{A+A^*}{2},\quad K=\frac{A-A^*}{2}.$$

The reversible Dirichlet form shows $H$ is positive definite: its only zero-energy functions on the full space are constants, because the underlying undirected chain is connected. Also $K^*=-K$ and $P^*-P=2K$.

Let $Q=H^{-1/2}KH^{-1/2}$, $B=-Q^2=Q^*Q\succeq0$, and define $F(t)=\operatorname{tr}(H+tK)^{-1}$ for real $t$. All these inverses exist since their symmetric part is positive definite. Using transpose invariance of trace and averaging the inverses with $t$ and $-t$ gives

$$F(t)=\operatorname{tr}\!\left[H^{-1}(I+t^2B)^{-1}\right].$$

Indeed $(I+tQ)^{-1}+(I-tQ)^{-1}=2(I-t^2Q^2)^{-1}$. Differentiate the last trace formula:

$$F'(t)=-2t\operatorname{tr}\!\left[H^{-1}B(I+t^2B)^{-2}\right]\le0\qquad(t\ge0).$$

The product inside the trace need not be symmetric. Its trace is nonnegative because $C=B(I+t^2B)^{-2}$ is positive semidefinite and $\operatorname{tr}(H^{-1}C)=\operatorname{tr}(C^{1/2}H^{-1}C^{1/2})\ge0$. This explicitly avoids an invalid commuting assumption.

Differentiating the original inverse instead gives $F'(1)=-\operatorname{tr}(A^{-1}KA^{-1})=-\operatorname{tr}(A^{-2}K)$. Consequently

$$\operatorname{tr}[Z^2(P^*-P)]=-2F'(1)=4\operatorname{tr}\!\left[H^{-1}B(I+B)^{-2}\right]\ge0.$$

In fact equality holds if and only if $B=0$, equivalently $K=0$, equivalently the original chain is reversible. This follows from positive definiteness of $H^{-1}$ and the fact that the positive eigenvalues of $B$ remain positive under $b\mapsto b/(1+b)^2$.

## Independent route through established literature

Huang and Mao, *Variational formulas of asymptotic variance for general discrete-time Markov chains*, arXiv:2012.13895 (December 27, 2020), Theorem 4.3 on PDF page 14, proves that the asymptotic variance for a reversible kernel plus an antisymmetric perturbation is even in the perturbation parameter and decreases with its absolute value. Primary source: https://arxiv.org/abs/2012.13895 . This is a stronger observable-by-observable statement than the required trace monotonicity.

For finite irreducible chains, first add one-half holding: $R=(I+P)/2$. Every convex mixture of $R$ and $R^*$ is irreducible and aperiodic, so the theorem's spectral-radius assumption on the mean-zero space is satisfied. Apply it to $R_t=(R+R^*)/2+t(R-R^*)/2$, for $-1\le t\le1$.

For an orthonormal basis $(e_j)$ of $L^2_0(\pi)$, the Poisson-equation formula reads

$$\sum_j\widetilde\sigma^2(R_t,e_j)=2\operatorname{tr}(I-R_t)^{-1}-(n-1).$$

Theorem 4.3 therefore gives the same trace monotonicity. Differentiate from the left at $t=1$; analyticity identifies this with the full derivative and yields the conjectured inequality for $R$. Since $Z_R=2Z_P$ and $R^*-R=(P^*-P)/2$, its trace expression is twice that for $P$. The conclusion follows even if $P$ is periodic. The original series definition of $Z$ in the periodic case is interpreted through the centered inverse or Abel limit.

The source does not explicitly name Aldous?Fill Conjecture 9.22 in the checked passage. The implication just proved is the reason for exclusion; no claim of a new resolution is made. Earlier finite-state antisymmetric-perturbation work cited by Huang?Mao may contain the result still earlier.
