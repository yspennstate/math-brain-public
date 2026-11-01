Model actually running: **GPT-5.6 Sol. Reasoning/effort level: UNVERIFIED** — the model family is exposed by the runtime, but no separately authenticated maximum-effort metadata is available.

# P26 / LIVE20 T08 — dependent-shell Green transfer and a synchronized distance-two Cayley cutoff class

**Parent status before:** `PARTIAL / OPEN` for Salez Problem 2.3.

**Parent status after:** `PARTIAL / OPEN` for Salez Problem 2.3. The parent conjecture is not claimed solved. The proved restricted scope is strictly enlarged by a Green transfer theorem allowing arbitrarily dependent radial fronts, together with a new 912-regular Cayley spectral-expander class whose limiting TV profile is a correlated Gaussian orthant profile.

**Restricted theorem/application status:** `CANDIDATE_FULL`, pending later independent review.

**Publication novelty:** `UNVERIFIED`. A bounded dated search on 20 September 2026 for combinations of synchronized spherical products, exact-distance products and cutoff did not locate the theorem/application below. This is negative evidence only, not a priority claim. Historical repository product results are explicitly separated below.

Repository/branch: `yspennstate/math-open-problems` / `master`.

Controlling policy: `operations/PROGRESS20_2026-09-20.md`.

Run root: `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/`.

## 0. Compact handoff, preserved failures, and why this is not a duplicate product run

The latest own substantive report read was

`2026-09-20_17-59-36__cartesian-multifront-green-transfer.md`.

That report proved a fixed Cartesian-power Green theorem. The exact continuous-time semigroup factorized into independent coordinate semigroups, so the TV profile was the order statistic of **independent** radial fronts. Its concrete square of degree-six LPS graphs was degree 12, spectral but not long-range, with profile `1-Phi(.)^2`.

Two older product results were also checked before doing mathematics here:

* R16, `runs/R16/2026-09-16T19-48-00Z_i0112-synchronous-tensor-cutoff.md`, already proves cutoff for the direct/tensor square with kernel `P tensor P`. That route uses one common Poisson clock and does not count as new here.
* NM13-01, `2026-09-20T03-03-00Z__strong-product-nbrw-trace-cutoff.md`, already treats the ordinary strong square, i.e. the union of the Cartesian and one-step tensor edges. It explicitly records the historical synchronous tensor result.

Therefore this run does **not** count Cartesian products, the ordinary tensor square, or the ordinary strong square as progress. The new class replaces the synchronous one-step kernel `P tensor P` by the genuinely different shell kernel `K_2 tensor K_2`, where `K_2` is uniform on the nonbacktracking distance-two sphere, while retaining sparse private one-coordinate edges. Its radial increments are `0,+/-1,+/-2`; the shared event type creates macroscopic correlation, and the new transfer theorem does not assume independent radial fronts.

The newest relevant companion report read was NM13-01

`2026-09-20T15-20-00Z__eisenstein-halved-nbrw-cutoff.md`.

NM13-01 there owns a transitivity/incidence route: left halving of Eisenstein Cayley bigraphs and direct projection of NBRW to the halved Cayley shells. P26 remains complementary: covering-tree Green bounds, coupled radial fronts, and the new synchronized spherical operation below. No companion theorem is overwritten or re-labeled.

Preserved unresolved history: the general positive exceptional NBRW sector remains open; the earlier Ihara/first-repeated-directed-edge tangle attack remains incomplete; global point-source stationary `L^2` remains too strong. None of these is counted as movement in this run.

The root `POSTED.md` registry was checked. The posted Salez Problem 2.4 Abelian-Cayley product-condition material is not reopened.

## 1. Exact source convention and current boundary

Justin Salez, `arXiv:2508.21055v1` (28 August 2025), defines continuous time by inserting independent mean-one exponential holding times between applications of a discrete transition matrix `P`. Thus the exact convention throughout this report is

\[
H_t=e^{t(P-I)}
=e^{-t}\sum_{m\ge0}\frac{t^mP^m}{m!}.
\tag{1.1}
\]

In Section 2.2 of the source, an expander sequence has diverging size, uniformly bounded degree and spectral gap bounded away from zero, and Problem 2.3 is exactly

> Prove that all vertex-transitive expanders exhibit cutoff.

Fresh source screening on 20 September 2026 leaves that problem open.

Dylan J. Altschuler, `arXiv:2609.14945` (submitted 14 September 2026), proves Gaussian-profile cutoff for every fixed-degree **long-range expander** sequence and proves the strict hierarchy

\[
\text{Ramanujan}\Longrightarrow\text{long-range expansion}\Longrightarrow\text{spectral expansion},
\]

with neither converse. Long-range expansion is therefore not synonymous with the source hypothesis in Salez Problem 2.3.

Francesco Pedrotti--Justin Salez, `arXiv:2607.05345` (submitted 6 July 2026, July revision), prove a universal window theorem in terms of their non-equilibrium Poincare quantity `gamma_*`. The checked statement does not derive a suitable lower bound on `gamma_*` solely from vertex transitivity plus an ordinary fixed spectral gap.

For the explicit input family below I use the classical nonbipartite Lubotzky--Phillips--Sarnak degree-six Cayley Ramanujan subfamily. In the LPS construction, when `p=5` is a quadratic residue modulo the auxiliary prime, the graph is a nonbipartite Cayley graph of `PSL_2`; the Ramanujan bound and logarithmic girth are classical.

## 2. Parent before/after and mechanism-level advance

### Parent before

Salez Problem 2.3 was open. P26 had a Green theorem for independent Cartesian fronts; historical R16/NM13-01 work had ordinary synchronous tensor and strong-product cutoff classes.

### Parent after

Salez Problem 2.3 remains open. The strict new restricted scope is:

> A point-start chain whose endpoint law, conditional on a **possibly dependent** vector of covering-shell radii, factorizes into the corresponding shell laws inherits a quantitative cutoff profile from the joint radial crossing law. Applying this to a mixed private/synchronized distance-two spherical Cayley operation produces a 912-regular vertex-transitive spectral-expander sequence, outside long-range expansion, with an explicit correlated bivariate-normal orthant TV profile and an `O(sqrt(log n))` window.

The exact output gap proved below is

\[
\boxed{
\operatorname{gap}(Y_n)
\ge \frac{243-\sqrt5}{456}
=0.5279910789\ldots .
}
\tag{2.1}
\]

Writing `N=|V(Y_n)|`, the cutoff center is

\[
\boxed{T_N=\frac6{19}\log_5N,}
\tag{2.2}
\]

and for fixed `Z`, uniformly for `|z|<=Z`,

\[
\boxed{
 d_{Y_n}\!\left(\frac6{19}\log_5N+z\sqrt{\log_5N}\right)
 =1-\Phi_2(\kappa z,\kappa z;\rho)
 +O_Z\!\left(\frac{\log\log N}{\sqrt{\log N}}\right),
}
\tag{2.3}
\]

where `Phi_2(.,.;rho)` is the standard bivariate normal CDF with correlation

\[
\boxed{\rho=\frac{384}{521}}
\tag{2.4}
\]

and

\[
\boxed{\kappa^2=\frac{130321}{56268}.}
\tag{2.5}
\]

The mechanism-level advance is not the constants. It is that **radial independence is unnecessary**: the Green squeeze only needs shell factorization conditional on the joint radius. The common event clock may produce order-one covariance between the entropy fronts, and the limiting TV profile then records that covariance.

## 3. Theorem A — dependent multifront Green transfer

Let `(X_n)` be finite transitive regular graphs with uniform stationary law `pi_n`. Assume that for a chosen root `x` there are shell laws `nu^x_{n,r}` and a random vector

\[
\mathbf R_t=(R_t^{(1)},\ldots,R_t^{(k)})
\]

such that a transitive chain on `V(X_n)^k`, started from `\mathbf x=(x_1,...,x_k)`, has the exact mixture representation

\[
\mu_{n,t}^{\mathbf x}
=\mathbf E\left[
\nu_{n,R_t^{(1)}}^{x_1}\otimes\cdots\otimes
\nu_{n,R_t^{(k)}}^{x_k}
\right].
\tag{3.1}
\]

**No independence assumption is made on `\mathbf R_t`.**

Suppose there is an entropic radius `ell_n` and error functions `G_n,L_n` such that

\[
\sup_x\sup_{r\ge\ell_n+h}
\chi^2(\nu^x_{n,r}\Vert\pi_n)\le G_n(h),
\tag{3.2}
\]

and all shell supports with radius at most `ell_n-h` are contained in a set `A_{n,x}(ell_n-h)` satisfying

\[
\sup_x\pi_n(A_{n,x}(\ell_n-h))\le L_n(h).
\tag{3.3}
\]

Then for every `h>=0`, the worst-start TV distance `d_{n,k}(t)` of the output chain satisfies

\[
\boxed{
\Pr\!\left(\min_iR_t^{(i)}\le\ell_n-h\right)-kL_n(h)
\le d_{n,k}(t)
}
\tag{3.4}
\]

and

\[
\boxed{
 d_{n,k}(t)
\le
\Pr\!\left(\min_iR_t^{(i)}<\ell_n+h\right)
+\frac12\sqrt{(1+G_n(h))^k-1}.
}
\tag{3.5}
\]

### Proof

For the lower bound, set

\[
\mathcal A=
\bigcup_{i=1}^k
\{y\in V(X_n)^k:y_i\in A_{n,x_i}(\ell_n-h)\}.
\]

If any `R_t^{(i)}<=ell_n-h`, the endpoint lies in `mathcal A`, hence

\[
\mu_{n,t}^{\mathbf x}(\mathcal A)
\ge
\Pr(\min_iR_t^{(i)}\le\ell_n-h).
\]

Under product stationarity,

\[
\pi_n^{\otimes k}(\mathcal A)
\le kL_n(h).
\]

Testing TV on `mathcal A` proves (3.4).

For the upper bound, whenever every `r_i>=ell_n+h`, the exact tensor identity

\[
1+\chi^2\!\left(\bigotimes_i\mu_i\middle\|\bigotimes_i\pi_i\right)
=
\prod_i\left(1+\chi^2(\mu_i\Vert\pi_i)\right)
\tag{3.6}
\]

gives

\[
\chi^2\!\left(
\bigotimes_i\nu_{n,r_i}^{x_i}\middle\|\pi_n^{\otimes k}
\right)
\le(1+G_n(h))^k-1.
\]

Thus the good-shell product has TV at most one half the square root above. On the complementary event use the trivial TV bound one and average the mixture (3.1). This proves (3.5). `QED`

The theorem is strictly stronger than the preceding Cartesian theorem at the transfer step: all dependence is pushed into the joint crossing probability.

## 4. Quantitative correlated-front corollary

Assume `k` is fixed, `G_n(h)<=A(ell_n+h+2)^b e^{-ah}` and `L_n(h)<=Ae^{-ah}`. Suppose that outside a fixed boundary region the joint radius is a bounded-increment Markov-additive process which, after coupling away the boundary, is a rate-one compound-Poisson sum

\[
S_t=\sum_{j=1}^{N_t}X_j,
\qquad N_t\sim\operatorname{Poisson}(t),
\tag{4.1}
\]

with iid `X_j in R^k`,

\[
\mathbf E X_j=v\mathbf 1,
\qquad
B:=\mathbf E[X_jX_j^{\mathsf T}]
\tag{4.2}
\]

positive definite, and suppose the boundary correction has a uniform exponential tail.

Then

\[
\mathbf E S_t=vt\mathbf1,
\qquad
\operatorname{Cov}(S_t)=tB.
\tag{4.3}
\]

The second identity is the point at which Salez's exact Poisson convention matters: for a compound-Poisson sum the variance-rate matrix is the **second moment** `B`, not the covariance matrix of one jump.

A fixed-dimensional Berry--Esseen theorem for compound-Poisson sums gives an `O(t^{-1/2})` error for orthants. One convenient proof is to split `[0,t]` into `ceil(t)` equal pieces. The increments over those pieces are iid compound-Poisson vectors with parameter in `[1/2,1]`, uniformly bounded third moment and uniformly nondegenerate covariance; the usual fixed-dimensional Berry--Esseen theorem for convex sets applies.

If the boundary correction is truncated at `M=c log(t+2)`, its tail is `O(t^{-3})`, while moving an orthant boundary by `M` changes the limiting Gaussian probability by `O(M/sqrt(t))`. Therefore, uniformly for bounded `z` and threshold perturbations `u_i=O(log ell_n)`, at

\[
t_n(z)=\frac{\ell_n}{v}+z\sqrt{\ell_n}
\tag{4.4}
\]

we have

\[
\Pr(R_t^{(i)}\ge\ell_n+u_i\ \forall i)
=
\Pr(Z_i\le vz\ \forall i)
+O_Z\!\left(\frac{\log\ell_n}{\sqrt{\ell_n}}\right),
\tag{4.5}
\]

where

\[
Z\sim N\!\left(0,\frac{B}{v}\right).
\tag{4.6}
\]

Choose `h_n=c_0 log ell_n` so that the Green and support errors in Theorem A are `o(ell_n^{-1/2})`. Equations (3.4)--(3.5) and (4.5) then give the quantitative profile

\[
\boxed{
 d_{n,k}(t_n(z))
=1-\Pr(Z_i\le vz\ \forall i)
+O_Z\!\left(\frac{\log\ell_n}{\sqrt{\ell_n}}\right).
}
\tag{4.7}
\]

This is the correlated analogue of the independent order-statistic theorem from the preceding run.

## 5. Concrete synchronized distance-two spherical Cayley graph

Let

\[
G_n=\operatorname{Cay}(\Gamma_n,S_n)
\]

be a nonbipartite degree-six LPS Cayley Ramanujan sequence, with `|Gamma_n|=n`. Put `q=5`. The LPS girth diverges, so after discarding finitely many terms we may assume girth greater than four.

Let `W_n` be the endpoints of reduced words of length two:

\[
W_n=\{st:s,t\in S_n,\ t\ne s^{-1}\}.
\tag{5.1}
\]

Girth greater than four implies that the `6*5=30` reduced length-two words are distinct. Also `W_n` is inverse-closed. Let `K_2` be the uniform convolution kernel on `W_n`.

Define a Cayley graph on `Gamma_n^2` by the symmetric generating set

\[
\mathcal T_n
=
(S_n\times\{e\})
\sqcup
(\{e\}\times S_n)
\sqcup
(W_n\times W_n).
\tag{5.2}
\]

The three pieces are disjoint: the synchronized piece has both coordinates nonidentity, while a private piece has one identity coordinate. Therefore

\[
\boxed{D=6+6+30^2=912.}
\tag{5.3}
\]

Call the graph `Y_n`. It is a 912-regular Cayley graph, hence vertex-transitive. Its discrete SRW kernel is exactly

\[
\boxed{
Q
=\frac1{152}(P\otimes I+I\otimes P)
+\frac{75}{76}(K_2\otimes K_2).
}
\tag{5.4}
\]

Thus a jump is private in the first coordinate with probability `1/152`, private in the second coordinate with probability `1/152`, and is a synchronized independent distance-two spherical jump in both coordinates with probability `75/76`.

This is not the R16 direct product (`P tensor P`) and not the NM13-01 strong square (private `P` moves plus `P tensor P`).

## 6. Spectral expansion of the new output

For a degree-six graph the normalized distance-two nonbacktracking shell polynomial is

\[
\boxed{k_2(\lambda)=\frac65\lambda^2-\frac15.}
\tag{6.1}
\]

Indeed, on a six-regular tree there are 30 reduced two-step paths and

\[
K_2=\frac65P^2-\frac15I.
\]

Since all terms in (5.4) are polynomials in the two commuting coordinate copies of `P`, a product eigenvector with base normalized eigenvalues `(lambda,mu)` has output eigenvalue

\[
q(\lambda,\mu)
=
\frac{\lambda+\mu}{152}
+\frac{75}{76}k_2(\lambda)k_2(\mu).
\tag{6.2}
\]

The nonbipartite Ramanujan bound is

\[
|\lambda|\le\rho_0:=\frac{\sqrt5}{3}
\tag{6.3}
\]

for every nonconstant base mode. Hence

\[
-\frac15\le k_2(\lambda)\le\frac7{15}.
\tag{6.4}
\]

If exactly one coordinate is constant, say `lambda=1`, then the function of `mu` in (6.2) is convex on `[-rho_0,rho_0]`, and its larger endpoint is `mu=rho_0`. Thus

\[
q(1,\mu)
\le
\frac{1+\rho_0}{152}
+\frac{75}{76}\frac7{15}
=
\frac{71+\rho_0}{152}
=
\frac{213+\sqrt5}{456}.
\tag{6.5}
\]

If both coordinates are nonconstant, then simply

\[
q(\lambda,\mu)
\le
\frac{2\rho_0}{152}
+\frac{75}{76}\left(\frac7{15}\right)^2
=
\frac{\sqrt5}{228}+\frac{49}{228}.
\tag{6.6}
\]

The difference between the right side of (6.5) and that of (6.6) is

\[
\frac{115-\sqrt5}{456}>0.
\]

Therefore every nonconstant output eigenvalue is at most `(213+sqrt(5))/456`, proving

\[
\boxed{
\operatorname{gap}(Y_n)
\ge
1-\frac{213+\sqrt5}{456}
=
\frac{243-\sqrt5}{456}>0.52799.
}
\tag{6.7}
\]

So `(Y_n)` satisfies the exact bounded-degree spectral-expander hypothesis of Salez Problem 2.3.

## 7. Base shell Green front

Let `nu_r^x` be the projection to `G_n` of the uniform radius-`r` sphere in the universal six-regular tree rooted at a lift of `x`. Equivalently, `nu_r^x` is the endpoint law of length-`r` NBRW started by a uniform first edge from `x`.

Let `p_r(lambda)` denote the corresponding normalized spherical polynomial. It obeys

\[
p_0=1,\qquad p_1(\lambda)=\lambda,
\qquad
p_{r+1}(\lambda)=\frac65\lambda p_r(\lambda)-\frac15p_{r-1}(\lambda).
\tag{7.1}
\]

On the Ramanujan interval `|lambda|<=sqrt(5)/3`, the usual Chebyshev parametrization gives

\[
|p_r(\lambda)|\le(r+1)5^{-r/2}.
\tag{7.2}
\]

Transitivity turns the point-start shell collision into the spectral trace:

\[
\chi^2(\nu_r^x\Vert\pi_n)
=
\sum_{j=2}^n p_r(\lambda_j)^2
\le
n(r+1)^2 5^{-r}.
\tag{7.3}
\]

Set

\[
\ell_n=\lceil\log_5n\rceil.
\tag{7.4}
\]

Then for `r>=ell_n+h`,

\[
\boxed{
G_n(h)
\le C(\ell_n+h+2)^2 5^{-h}.
}
\tag{7.5}
\]

The support of every shell of radius at most `ell_n-h` lies in the ordinary base ball of that radius. The six-regular tree volume bound gives

\[
\boxed{L_n(h)\le C5^{-h}.}
\tag{7.6}
\]

These are exactly the hypotheses needed in Theorem A.

## 8. Why the synchronized spherical output has exact product shell laws

Lift each base coordinate to its universal six-regular tree. The private kernel `P` and the spherical kernel `K_2` are both invariant under the root stabilizer of that tree. Therefore, for any fixed history of event types, the law in a coordinate is uniform on a tree sphere conditional on its final radius.

At a synchronized event, the two `K_2` moves are chosen independently. At a private event only one coordinate moves. Conditional on the event-type history, the two coordinate random choices are independent. Hence, conditional on the two final radii `(r_1,r_2)`, the endpoint angular law is

\[
\nu_{r_1}^{x_1}\otimes\nu_{r_2}^{x_2},
\tag{8.1}
\]

and crucially this product law does not depend on the event-type history. Mixing over histories preserves (8.1). Thus the exact representation (3.1) holds with `k=2`, although the two radii are strongly dependent.

This is the bridge that makes the new class an application of the dependent-shell theorem rather than another product-chain black box.

## 9. Exact coupled radial clock

Away from the root boundary, one ordinary base step has radial increment

\[
\xi=\begin{cases}
+1,&5/6,\\
-1,&1/6,
\end{cases}
\qquad
\mathbf E\xi=\frac23,
\qquad
\mathbf E\xi^2=1.
\tag{9.1}
\]

A uniform reduced distance-two move has radial increment

\[
\eta=\begin{cases}
+2,&25/30=5/6,\\
0,&4/30=2/15,\\
-2,&1/30,
\end{cases}
\tag{9.2}
\]

because the reduced path may take zero, one, or two initial steps toward the root. Hence

\[
\mathbf E\eta=\frac85,
\qquad
\mathbf E\eta^2=\frac{52}{15}.
\tag{9.3}
\]

One output jump has increment vector `X=(X_1,X_2)` with the three event types

\[
X=\begin{cases}
(\xi,0),&1/152,\\
(0,\xi'),&1/152,\\
(\eta,\eta'),&75/76,
\end{cases}
\tag{9.4}
\]

where primed and unprimed increments are independent inside an event. Therefore each coordinate has drift

\[
\boxed{
v
=\frac1{152}\frac23
+\frac{75}{76}\frac85
=\frac{19}{12}.
}
\tag{9.5}
\]

The compound-Poisson second-moment matrix is

\[
\boxed{
B=\mathbf E[XX^{\mathsf T}]
=
\begin{pmatrix}
521/152&48/19\\
48/19&521/152
\end{pmatrix}.
}
\tag{9.6}
\]

Indeed the diagonal second moment is

\[
A:=\frac1{152}+\frac{75}{76}\frac{52}{15}
=\frac{521}{152},
\tag{9.7}
\]

while the off-diagonal contribution comes only from synchronized events:

\[
C:=\frac{75}{76}\left(\frac85\right)^2
=\frac{48}{19}.
\tag{9.8}
\]

Thus the asymptotic correlation is

\[
\boxed{\rho=\frac CA=\frac{384}{521}.}
\tag{9.9}
\]

The exact marginal interior increment distribution, including the event in which only the other coordinate moves, is

\[
\Pr(\Delta=2)=\frac{125}{152},\quad
\Pr(\Delta=1)=\frac5{912},\quad
\Pr(\Delta=0)=\frac{21}{152},\quad
\Pr(\Delta=-1)=\frac1{912},\quad
\Pr(\Delta=-2)=\frac5{152}.
\tag{9.10}
\]

### Boundary correction

At radii zero or one, an attempted negative move is reflected by the true spherical geometry. Couple the actual radius to the unrestricted increment chain by using the same proposed increment and replacing only the moves which would cross the root boundary. Every replacement is upward and has bounded size.

For the interior law (9.10), the explicit exponential calculation

\[
\boxed{
\mathbf E[2^{-\Delta}]=\frac{73}{152}<1
}
\tag{9.11}
\]

shows that `2^{-R_m}` is a strict supermartingale away from the fixed boundary region. Starting from radius two, the probability of returning to `{0,1}` is therefore uniformly below one. By the strong Markov property the number of boundary excursions has a geometric tail. Since each correction is bounded, the total correction vector `C_infinity` has a uniform exponential tail.

Consequently the actual radial pair differs from the unrestricted compound-Poisson sum by `O_P(1)`, with exponentially decaying tails, exactly as required in Section 4.

## 10. Correlated Gaussian cutoff profile

At output time

\[
t_n(z)=\frac{\ell_n}{v}+z\sqrt{\ell_n}
=\frac{12}{19}\ell_n+z\sqrt{\ell_n},
\tag{10.1}
\]

the unrestricted radial pair has mean

\[
vt_n(z)\mathbf1
=\ell_n\mathbf1+vz\sqrt{\ell_n}\mathbf1
\]

and covariance

\[
t_n(z)B
=\frac{\ell_n}{v}B+O(\sqrt{\ell_n}).
\]

Standardizing one coordinate gives the diagonal crossing coefficient

\[
\beta_*^2
=\frac{v^3}{A}
=\boxed{\frac{130321}{112536}}.
\tag{10.2}
\]

Let `Phi_2(a,b;rho)` denote the CDF of a standard bivariate normal with correlation `rho`. The quantitative two-dimensional Berry--Esseen estimate plus the exponentially light boundary correction yields, uniformly for bounded `z` and `|u_i|=O(log ell_n)`,

\[
\Pr(R_t^{(1)}\ge\ell_n+u_1,
      R_t^{(2)}\ge\ell_n+u_2)
=
\Phi_2(\beta_*z,\beta_*z;\rho)
+O_Z\!\left(\frac{\log\ell_n}{\sqrt{\ell_n}}\right).
\tag{10.3}
\]

Choose

\[
h_n=8\log_5\ell_n.
\]

Then (7.5)--(7.6) make the Green/support terms in Theorem A polynomially smaller than the Berry--Esseen error. Hence

\[
\boxed{
 d_{Y_n}\!\left(\frac{12}{19}\ell_n+z\sqrt{\ell_n}\right)
=1-\Phi_2(\beta_*z,\beta_*z;384/521)
+O_Z\!\left(\frac{\log\ell_n}{\sqrt{\ell_n}}\right).
}
\tag{10.4}
\]

Now `N=n^2`, so `ell_n=(1/2)log_5N+O(1)`. On the natural `sqrt(log_5N)` scale, put

\[
\kappa^2=2\beta_*^2
=\boxed{\frac{130321}{56268}}.
\tag{10.5}
\]

This gives the announced profile

\[
\boxed{
 d_{Y_n}\!\left(
\frac6{19}\log_5N+z\sqrt{\log_5N}
\right)
=
1-\Phi_2(\kappa z,\kappa z;384/521)
+O_Z\!\left(\frac{\log\log N}{\sqrt{\log N}}\right).
}
\tag{10.6}
\]

In particular the output has total-variation cutoff with `Theta(sqrt(log N))` window.

For a fixed `epsilon in (0,1)`, let `u_{epsilon,rho}` be the unique real number satisfying

\[
\Phi_2(u_{\epsilon,\rho},u_{\epsilon,\rho};\rho)=1-\epsilon.
\]

Since the diagonal bivariate normal CDF has positive derivative at every finite point,

\[
\boxed{
 t_{\rm mix}(\epsilon)
=
\frac6{19}\log_5N
+\kappa^{-1}u_{\epsilon,384/521}\sqrt{\log_5N}
+O_\epsilon(\log\log N).
}
\tag{10.7}
\]

At the entropic center `z=0`, the classical bivariate-normal orthant formula gives

\[
1-\Phi_2(0,0;\rho)
=
\frac34-\frac{\arcsin\rho}{2\pi}
=0.6181104801\ldots .
\tag{10.8}
\]

The profile is genuinely non-Gaussian. On the right, its tail is asymptotic to twice a one-dimensional Gaussian tail and has quadratic exponent `kappa^2/2`. On the left, the complementary lower-orthant probability has quadratic exponent `kappa^2/(1+rho)`. Since `rho=384/521` lies strictly between zero and one, these two quadratic coefficients differ; an affine Gaussian survival profile has the same quadratic coefficient on both sides.

## 11. The output is spectral but not long-range

One output step changes each base coordinate by at most two ordinary base edges. Therefore every output radius-`r` ball is contained in the product of two base radius-`2r` balls. The degree-six tree bound gives

\[
|B_{Y_n}(y,r)|
\le C\,5^{2r}\,5^{2r}
=C\,625^r.
\tag{11.1}
\]

But `Y_n` is degree `912`, so the singleton tree-growth benchmark in the long-range-expansion condition is

\[
(912-1)^r=911^r.
\]

Take

\[
r_N=\left\lfloor\frac12\log_{911}N\right\rfloor.
\]

Then the macroscopic saturation branch of the LRE lower bound is inactive, while

\[
\frac{|B_{Y_n}(y,r_N)|}{911^{r_N}}
\le
C\left(\frac{625}{911}\right)^{r_N}
\longrightarrow0.
\tag{11.2}
\]

Thus no fixed positive long-range-expansion constant can hold. The class is a genuine bounded-degree vertex-transitive **spectral-but-not-long-range** expander sequence. Its cutoff is not a direct application of Altschuler's output hypothesis.

## 12. Exact checker and decisive calculations

The executed exact arithmetic checker is

`2026-09-20_19-01-50__spherical_synchronized_green_checker.py`

created at commit `511941b2bba8374da8b654cf3230186dcc3971ac`.

Its archived output is

`2026-09-20_19-01-50__spherical_synchronized_green_checker.out`

created at commit `52440310b81963a24e016584f1792179ae6f0007`.

The executed output terminates with and begins from the marker

`P26_T08_SPHERICAL_SYNCHRONIZED_GREEN_EXACT_PASS`

and independently verifies:

* degree `912`, `D_2=30`, weights `1/152,1/152,75/76`;
* shell polynomial endpoint `k_2(rho_0)=7/15`;
* spectral gap lower bound `(243-sqrt(5))/456`;
* the complete marginal radial increment law (9.10);
* `v=19/12`, `A=521/152`, `C=48/19`, `rho=384/521`;
* the explicit supermartingale factor `73/152`;
* `beta_*^2=130321/112536` and `kappa^2=130321/56268`;
* center coefficient `6/19` on `log_5 N`;
* the center profile `0.6181104801284971`;
* the strict long-range branching mismatch `625<911`.

These checks are necessary sanity checks, not counted as separate mechanism advances.

## 13. C28 / NM13-01 coordination

The latest NM13-01 report, `2026-09-20T15-20-00Z__eisenstein-halved-nbrw-cutoff.md`, develops a different T08 route: a left-transitive Cayley bigraph is converted to its left-halved ordinary Cayley graph, and NBRW is projected directly to the halved shells. Its concrete p=2 output has degree 18.

Historical NM13-01 also already owns the ordinary strong square, so this report explicitly avoided `P tensor P` synchronized edges. P26 instead proves a dependence-tolerant shell theorem and applies it to **distance-two spherical synchronized edges**. The two workers therefore remain complementary: NM13-01 exploits transitivity-specific incidence/fiber structure, whereas P26 exploits shell Green cleanup plus a correlated covering-radius CLT.

## 14. Residual obstruction and next attack

The parent obstruction is now more sharply separated.

This run shows that neither multiple macroscopic entropy fronts nor order-one correlation between them is by itself an obstacle. If conditional shell laws factor and each late shell is Green-small, all dependence can be retained in a finite-dimensional radial crossing law and cutoff still follows quantitatively.

What remains difficult for general Salez T08 is still the **angular/positive-exceptional sector**: ordinary vertex transitivity plus a fixed spectral gap does not currently imply an entropic NBRW shell Green front. In particular, when a synchronized generating relation correlates the angular choices in the two coordinates, (8.1) can fail even if the radial vector is well behaved.

The next P26 attack will therefore target a genuinely new object rather than another product variant:

> **finite-rank correlated-shell Green defect.** Replace the exact product shell identity (8.1) by a decomposition of the conditional shell likelihood ratio into a product part plus a fixed-rank angular interaction. Prove that a matrix `chi^2` defect which is `o(1)` after `o(sqrt(log n))` additional shell layers transfers the same correlated radial profile. The first concrete test will be a sparse synchronized relation `R subset S x S`, where synchronized generator choices are correlated and the conditional angular law no longer factorizes.

That target attacks the precise failure of the present theorem and remains distinct from NM13-01's incidence/Hecke route.

## 15. Failed-route history preserved

* positive exceptional NBRW modes under mere transitivity + spectral expansion: unresolved;
* Ihara / first repeated directed-edge tangle control: incomplete;
* global point-source stationary `L^2` at the entropic time: too strong;
* scalar positive filters cannot cancel genuinely positive slow modes;
* ordinary Cartesian, direct/tensor and strong products: historical results, not counted again here.

No failed route is erased or promoted.

## 16. ledger_delta

```text
parent_problem: Salez arXiv:2508.21055 Problem 2.3
parent_before: OPEN/PARTIAL
parent_after: OPEN/PARTIAL
parent_level_change: strict restricted theorem-class enlargement; no claim of general resolution

mechanism_advance:
  - proved dependent-multifront Green squeeze; radial fronts may be arbitrarily dependent
  - proved quantitative correlated orthant-profile transfer under a compound-Poisson radial CLT
  - isolated exact rate-one effect: covariance rate is E[XX^T], preserving common-clock correlation

demonstrated_application:
  class: degree-912 Cayley graphs with private base edges and synchronized distance-two spherical edges
  base: nonbipartite degree-six LPS Ramanujan Cayley family
  spectral_gap_lower: (243-sqrt(5))/456
  cutoff_center: (6/19) log_5 N
  cutoff_window: Theta(sqrt(log N))
  profile: 1-Phi_2(kappa z,kappa z;384/521)
  kappa_squared: 130321/56268
  quantitative_profile_error: O_Z(log log N / sqrt(log N))
  long_range_status: proved NOT long-range by branching 625 < 911

not_counted_as_advances:
  - source recovery
  - repeated checks of Salez/Altschuler scope
  - checker execution by itself
  - historical Cartesian/tensor/strong product theorems

restricted_status: CANDIDATE_FULL pending later independent review
publication_novelty: UNVERIFIED

preserved_obstructions:
  - positive exceptional NBRW sector
  - incomplete Ihara first-repeat tangle route
  - stationary point-source L2 too strong

companion_split:
  NM13-01: transitivity/incidence/halving/Hecke-fiber mechanisms
  P26: shell Green transfer, coupled radial fronts, correlated-shell defects

next_attack:
  finite-rank correlated-shell Green defect for sparse synchronized angular relations

essential_code_commit: 511941b2bba8374da8b654cf3230186dcc3971ac
essential_output_commit: 52440310b81963a24e016584f1792179ae6f0007
```

End of complete P26 substantive T08 report.
