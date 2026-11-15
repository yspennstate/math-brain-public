# The Erdős–Rényi corollary of the stated cavity theorems

Fix d>0. All limits below keep d fixed. This argument uses two external
results: the general lower bound in Theorem 2.1, equation (2.11), of
Dmitry Panchenko, [The Mézard-Parisi formula, arXiv:2610.39545v1](https://arxiv.org/html/2610.39545v1),
and the hierarchical upper bound and cascade recursion in Theorem 4 and
Proposition 2 of Dmitry Panchenko and Michel Talagrand,
[Bounds for diluted mean-fields spin glass models, arXiv:math/0405357](https://arxiv.org/html/math/0405357).
The proofs of those external results are not reproduced here.

## 1. Clause and hypotheses

For beta>0 put

\[
 \theta(s,t)=\frac\beta2(1-st),\quad
 a=\frac{1+e^\beta}{2},\quad
 \tau=\frac{e^\beta-1}{e^\beta+1}.
\]

For s,t in {-1,1},

\[
 e^{\theta(s,t)}=a(1-\tau st).
\tag{1}
\]

Indeed the two sides are 1 when st=1 and e^beta when st=-1.
Thus the factorization assumptions hold with b=-tau and f(s)=s.
The deterministic f copies are independent, b is independent of them,
0<tau<1, and (-b)^k=tau^k>0 for every positive integer k.
The clause is invariant under swapping its inputs. Its maximum absolute
value is beta, so every required exponential moment is finite.
Take arity 2, interaction density lambda=d/2, and external field zero.

Let H_n have M~Pois(dn/2) ordered independent uniform vertex pairs,
with loops and repetitions retained. Then

\[
 F_n(\beta)=\frac1n\mathbb E\log
   \sum_{\sigma\in\{-1,1\}^n}
        \exp(\beta\operatorname{Cut}_{H_n}(\sigma))
\tag{2}
\]

is exactly the pressure of this clause model. A loop contributes zero.

## 2. A common trial functional

The extension of (1) to independent spin means u,v in [-1,1] is

\[
 C(u,v)=a(1-\tau uv),\qquad 1\le C(u,v)\le e^\beta.
\tag{3}
\]

Choose a finite depth r>=1, increasing cascade parameters
0<zeta_0<...<zeta_{r-1}<1, normalized Ruelle cascade weights V_alpha,
and a measurable h_0:[0,1]^r -> [-1,1]. For each input label I take an
independent array of uniform variables Z_gamma^I on the nonroot vertices
of the tree, independent of the cascade. Set

\[
 m_\alpha^I=h_0(Z_{\alpha|1}^I,\ldots,Z_{\alpha|r}^I).
\]

Let K_s~Pois(d) and K_e~Pois(d/2) be independent, with all input labels
distinct between different factors. Define

\[
 S_\alpha=\frac12\sum_{\varepsilon=\pm1}
               \prod_{j=1}^{K_s}C(m_\alpha^{s,j},\varepsilon),
 \qquad
 E_\alpha=\prod_{j=1}^{K_e}
               C(m_\alpha^{e,j,1},m_\alpha^{e,j,2}),
\]

and

\[
 \mathcal P_{d,\beta}(r,\boldsymbol\zeta,h_0)
 =\log2+\mathbb E\log\sum_\alpha V_\alpha S_\alpha
          -\mathbb E\log\sum_\alpha V_\alpha E_\alpha,
 \qquad I_d(\beta)=\inf_{r,\boldsymbol\zeta,h_0}\mathcal P_{d,\beta}.
\tag{4}
\]

This is equation (2.9) of the first paper at the specified parameters.
All logarithms are integrable: they lie between zero and beta times
their corresponding Poisson counts. The external general lower bound
therefore gives

\[
 \liminf_n F_n(\beta)\ge I_d(\beta).
\tag{5}
\]

The named symmetric-coupling examples of that paper are not needed.

## 3. Matching the upper-bound parameterization

First suppose |h_0|<=1-delta for some delta in (0,1). Define the real
field function x(z)=artanh(h_0(z)); then a spin with field x has mean
tanh x=h_0(z).

Here is an explicit nested-measure representation of the field array.
For a prefix z=(z_1,...,z_{r-1}), let nu_{r-1}(z) be the law of
x(z_1,...,z_{r-1},U), with U uniform. Recursively, for j=r-2,...,0,
let nu_j(z_1,...,z_j) be the law of
nu_{j+1}(z_1,...,z_j,U). The measure nu_0 has no random prefix.
Use the point mass at nu_0 as the top trial law in Section 5 of the
upper-bound paper. Conditional on any prefix, the subtrees produced by
the remaining uniforms are independent and have precisely this law.
This verifies equality in distribution of the whole field array,
not just of a field at one leaf. For r=1 this construction simply says
that the top trial law is the point mass at the distribution of x(U).

Write T for the iterated power-mean operator along a single branch,
with exponents zeta_0,...,zeta_{r-1}, integrating the last coordinate
first. Physical Poisson counts stay fixed during these integrations.
The cited cascade recursion gives

\[
 \mathbb E\log\sum_\alpha V_\alpha W_\alpha
       =\mathbb E\log T W
\tag{6}
\]

for the positive hierarchical arrays in (4). The site term on the
right is the site term in the upper bound after substituting tanh x=m.

For the edge term, condition on K_e=k. Write its k factors as C_j.
All auxiliary coordinates used by distinct C_j are independent.
At the deepest level their conditional power means multiply, because
the expectation of a product of independent factors is the product
of their expectations. The resulting factors still use disjoint
coordinates at the next level. Induction up the r levels proves

\[
 T\Bigl(\prod_{j=1}^k C_j\Bigr)=\prod_{j=1}^k T C_j.
\]

Taking logarithms, expectations and then the Poisson average yields

\[
 \mathbb E\log T E=\frac d2\,\mathbb E\log T C.
\tag{7}
\]

Consequently (4) is exactly a trial value supplied by the cited
hierarchical upper bound, which applies by Section 1. It follows that
F_n(beta)<=P_{d,beta}(r,zeta,h_0) for every bounded-field trial.

To include endpoint means, replace h_0 by (1-delta)h_0. Each mean changes
by at most delta. Formula (3) and C>=1 show

\[
 |\log C(u,v)-\log C(u',v')|
 \le a\tau(|u-u'|+|v-v'|).
\]

A site factor has only one changed input, so the absolute change of its
logarithm is at most a tau delta. An edge factor has two, giving at
most 2a tau delta. Products add these bounds, and a positive weighted
sum preserves a uniform bound on the logarithmic ratio. Thus the
absolute change of (4) is at most

\[
 a\tau\delta(\mathbb E K_s+2\mathbb E K_e)
       =d(e^\beta-1)\delta\longrightarrow0.
\]

Pass to delta down to zero, then take the infimum over all trials:
F_n(beta)<=I_d(beta). Together with (5), this proves

\[
 \lim_n F_n(\beta)=I_d(\beta).
\tag{8}
\]

No identification with the separate OpenAI manuscript is required.

## 4. Zero temperature

Let c_n=E MaxCut(H_n)/n. There are 2^n spin assignments, so the largest
summand in (2) and the sum of 2^n copies of that summand give

\[
 c_n\le F_n(\beta)/\beta\le c_n+\log2/\beta.
\tag{9}
\]

Also 0<=c_n<=d/2. Put A=liminf c_n and B=limsup c_n.
Equation (8) and the two sides of (9) imply
B<=I_d(beta)/beta<=A+log(2)/beta. Let beta tend to infinity:
B<=A, hence c_n converges to c(d), and

\[
 c(d)=\lim_{\beta\to\infty}\frac{I_d(\beta)}\beta,
 \qquad 0\le I_d(\beta)/\beta-c(d)\le\log2/\beta.
\tag{10}
\]

This is the zero-temperature limit of the optimized finite-temperature
cavity value. It makes no exchange of an infimum and a temperature
limit and asserts no minimizing hierarchy.

## 5. Independent audit of the simple-graph transfer

Poisson splitting gives independent multiplicities C_uv~Pois(d/n)
for unordered pairs u<v. To check the rate a second way, conditional
on M each pair has probability 2/n^2, so its mean is
(dn/2)(2/n^2)=d/n. The total mean over distinct pairs is d(n-1)/2;
the remaining mean d/2 consists of loops, as required by E M=dn/2.

Put x=d/n and q=1-e^{-x}. Collapsing each positive C_uv to one edge
gives G(n,q). Its expected deletion count is

\[
 D_n=\binom n2\mathbb E(C_{uv}-1)_+
     =\binom n2(x-1+e^{-x}).
\]

For n>d, obtain G(n,x) by retaining all existing G(n,q) edges and
adding each absent edge with conditional probability (x-q)/(1-q),
independently across pairs. This is a genuine joint construction with
the original multiplicities. Its expected addition count is also D_n.
One edge changes MaxCut by at most one, and loops change it by zero.
Since

\[
 x-1+e^{-x}=\int_0^x(1-e^{-t})\,dt
             \le\int_0^x t\,dt=x^2/2,
\]

the expected difference between the two optima has absolute value at most

\[
 2D_n\le\frac{d^2(n-1)}{2n}.
\tag{11}
\]

This independently reproduces the earlier constant using an integral
remainder rather than its second-derivative argument. Dividing by n
shows that G(n,d/n) has expected optimum density c(d).

Resampling a Bernoulli edge changes MaxCut by at most one and changes
the edge state with probability 2x(1-x). Efron–Stein therefore gives
Var(MaxCut)<=binom(n,2)x(1-x)=O(n). Chebyshev proves convergence in
probability to c(d).

Finally, with S(sigma)=-sum_e sigma_u sigma_v,
Cut(sigma)=(M+S(sigma))/2, including loops and multiplicities. Hence
Z_cut(beta)=exp(beta M/2) Z_S(beta/2). This independently checks the
density d/2, the factor 1/2 in the temperature, and cancellation of loops.

The random regular ensemble is not covered by this argument.
