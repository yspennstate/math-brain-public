PARTIAL

# C0002: intermediate level-set volume of the two-dimensional DGFF

Task: “Open problem C0002”, received 13 November 2026, approximately
06:58 Asia/Tbilisi. This is a partial research result. Printed work answers
substantial deviation regimes; the work here proves a finite-lattice
comparison rate and a first-order mean bias. The limiting second-order
fluctuation law and a matching upper rate to the continuum law remain
unestablished here. The numerical investigation is complete within the
stated resource limits.

## Setting and scope

Let D=(0,1)^2, V_N={1,...,N-1}^2, and let h be the zero-boundary DGFF
whose covariance is the killed simple-random-walk Green function G_N.
Put g=2/pi, L=log N, t=gL, beta=2 lambda/sqrt(g), and

\[
 X_N={\sqrt L\over N^2}e^{\beta^2t/2}
          \sum_{x\in V_N}1_{\{h_x\ge\beta t\}},\qquad
 M_N(\beta)={1\over N^2}\sum_{x\in V_N}e^{\beta h_x-\beta^2t/2},
 \qquad c_\beta={1\over\beta\sqrt{2\pi g}}.
\]

Corollary 2.9 of Biskup, arXiv:1712.09972v4, p. 27, gives
X_N converging in distribution to W_lambda=Z_lambda^D(D)/beta.
Theorem 2.7 is on pp. 26–27; Problem 16.2 is on p. 220 of this
arXiv version (the reproduced Springer volume places it on p. 392). In particular, subtracting Z_lambda(D) without the factor
1/beta changes the problem. A subtraction from the random continuum limit
also requires a specified joint coupling; the corollary alone specifies laws.

The two results below concern a deterministic first-order bias to this
continuum law and a same-field comparison with M_N. They do not identify
the limiting fluctuations about a coupled W_lambda.

## Quantitative results established here

**Theorem A (same-field chaos comparison).** For every fixed
0<lambda<1/sqrt(2), there is C_lambda<infinity such that

\[
 E[(X_N-c_\beta M_N(\beta))^2]\le {C_\lambda\over(\log N)^2}.
 \tag{A}
\]

Thus the L2 error to the *finite-lattice* exponential mass is O(1/log N).
In particular, for any b_N tending to infinity,

\[
 P\{|X_N-c_\beta M_N|>b_N/\log N\}\le C_\lambda/b_N^2.
 \tag{A1}
\]

This is not an upper bound for a distance to the continuum law: a
quantitative approximation of M_N by continuum GMC is an additional step.

**Theorem B (annealed bias and obstruction to faster Wasserstein convergence).**
For every fixed 0<lambda<1, write

\[
 q(u)=c_0+g\log r_D(u),\quad
 m_\lambda=c_\beta\int_D e^{\beta^2q(u)/2}\,du,
\]

where c_0=g(EulerGamma+(3/2)log 2) is the square-lattice potential-kernel
constant in Biskup's convention, and r_D is the conformal radius. Then

\[
 E X_N=m_\lambda+{B_\lambda\over\log N}
                     +O_\lambda((\log N)^{-2}),\tag{B}
\]
\[
 B_\lambda={c_\beta\over g}\int_D e^{\beta^2q(u)/2}
   \left({q(u)\over2}-{\beta^2q(u)^2\over2}-{1\over\beta^2}\right)du<0.
 \tag{B1}
\]

Here m_lambda=E W_lambda. Consequently

\[
 \liminf_{N\to\infty}(\log N)
 W_1(\mathcal L(X_N),\mathcal L(W_\lambda))\ge -B_\lambda>0.
 \tag{B2}
\]

The first-order bias therefore rules out o(1/log N) convergence in W1
for the specified, uncorrected normalization, for every lambda in (0,1).
No novelty claim is made for these estimates without further bibliographic
review. Full proofs follow. The literature audit gives the exact source results and their scope.

## Full proofs

All constants below may depend on a fixed beta>0. The domain is the unit
square; N is an integer at least 3. Notation is as in REPORT.md. These are
partial results, with no claim that the original fluctuation problem is solved.

## 1. Green-function bounds

Write v_x=G_N(x,x)=t+q_x and c_xy=G_N(x,y). The potential-kernel identity
and its expansion a(z)=g log|z|+c_0+O(|z|^{-2}) give

\[
 q_x\le C,\qquad v_x\ge g\log d_x-C,\qquad
 0\le c_{xy}\le g\log {N\over1+|x-y|}+C,                 \tag{1}
\]

where d_x is the distance to V_N^c. For the last bound use
G_N(x,y)=E_x a(S_tau-y)-a(x-y) and the fact that the exit site and y
are at distance at most sqrt(2)N+2. For the lower diagonal bound, use the
same identity in a lattice disk of radius comparable to d_x contained in
V_N, then domain monotonicity. Nonnegativity follows from the occupation
interpretation of G_N. These arguments include bounded distances by changing C.
See also Biskup, Theorem 1.17 and Lemmas 1.18, 1.21, pp. 14–15.

Let p=beta^2 g=4lambda^2. If p<2, annulus counting gives

\[
 \sup_x N^{-2}\sum_y (N/(1+|x-y|))^p\le C_p,             \tag{2}
\]
\[
 N^{-4}\sum_{|x-y|\le A N^{3/4}}
          (N/(1+|x-y|))^p\le C_{p,A}N^{-(2-p)/4}.       \tag{3}
\]

For example, there are at most C(r+1) sites in an annulus of integer
radius r, and summing (r+1)^{1-p} proves both estimates. The number of
vertices for which v_x<t/2 is O(N^{3/2}), by (1).

## 2. A two-variable Gaussian calculation

Take a centered Gaussian pair (H,J) with covariance matrix
Sigma=[[t+q,c],[c,t+r]]. Put

\[
 A(H)=\sqrt{t/g}\,e^{\beta^2t/2}1_{\{H\ge\beta t\}},\quad
 B(H)=c_\beta e^{\beta H-\beta^2t/2},\quad
 K=c_\beta^2 e^{\beta^2(q+r)/2+\beta^2c}.
\]

Then E[B(H)B(J)]=K. Suppose t+q,t+r>=t/2, q,r<=C_0,
and 0<=c<=t/4. For sufficiently large t, the eigenvalues of Sigma
lie between t/4 and 2t+C_0. Let S,T be independent exponential
random variables of rate beta, and define

\[
 F(z,c)={z\over2}+c-{1\over\beta^2}
                         -{\beta^2(z+c)^2\over2}.
\]

Completing the square in the Gaussian density gives the **exact** identities

\[
 {E[A(H)B(J)]\over K}
 =\sqrt{t\over t+q}\ E\exp\left\{-{(S-\beta(q+c))^2\over2(t+q)}\right\},\tag{4}
\]
\[
 {E[A(H)A(J)]\over K}
 ={t\over\sqrt{\det\Sigma}}\ E\exp\{-\tfrac12 U^T\Sigma^{-1}U\},
 \quad U=(S-\beta(q+c),T-\beta(r+c)).                     \tag{5}
\]

For clarity, the mixed Gaussian tilt shifts H by beta c and contributes
exp(beta^2(t+r)/2); at H=beta t+s the remaining square is
(s-beta(q+c))^2. The joint tilt uses beta(H+J) and produces both
entries of U. The density prefactors and the two exponential integrals
give precisely (4) and (5); no independence assumption is made on H,J.

Uniformly in the specified range, these identities imply

\[
 E[A(H)B(J)]/K=1+F(q,c)/t+R_q,                         \tag{6}
\]
\[
 E[A(H)A(J)]/K=1+[F(q,c)+F(r,c)]/t+R_{q,r},           \tag{7}
\]

with all remainders bounded in absolute value by

\[
 Ct^{-2}(1+|q|+|r|+c)^4.                              \tag{8}
\]

Here are the remainder details. On this range,

\[
 \sqrt{t/(t+q)}=1-q/(2t)+O(q^2/t^2),\quad
 t/\sqrt{\det\Sigma}=1-(q+r)/(2t)
                              +O((|q|+|r|+c)^2/t^2),
\]
\[
 \|\Sigma^{-1}-t^{-1}I\|
                      \le C(|q|+|r|+c)/t^2.             \tag{9}
\]

Taylor's theorem on the compact range q/t,r/t in [-1/2,C_0/t],
c/t in [0,1/4] proves the first two assertions. The last follows from
the resolvent identity and the eigenvalue lower bound. Use
|exp(-z)-1+z|<=z^2/2 for z>=0 and the finite first four moments of
S,T. Replacing the inverses by 1/t in the linear term incurs an error
bounded by Ct^{-2}(1+|q|+|r|+c)^3. Multiplication of the prefactor
expansions incurs at most the degree-four bound (8). In (4), the
coefficient is

\[
 -q/2-\tfrac12 E(S-\beta(q+c))^2=F(q,c),
\]

since ES=1/beta and ES^2=2/beta^2. In (5), the corresponding
coefficient is F(q,c)+F(r,c). This proves (6)–(8), even when q,r,c
are not bounded independently of t.

Subtracting the two mixed moments from the joint moment, the terms of
orders 1 and 1/t cancel. Thus

\[
 |E[(A(H)-B(H))(A(J)-B(J))]|
 \le Ct^{-2}e^{\beta^2(q+r)/2+\beta^2c}
                       (1+|q|+|r|+c)^4.                \tag{10}
\]

For **arbitrary** q,r<=C_0 and covariance c>=0, the elementary inequality
1_{H>=beta t}<=exp(beta H-beta^2t) also gives

\[
 |E[(A(H)-B(H))(A(J)-B(J))]|
 \le Ct\,e^{\beta^2(q+r)/2+\beta^2c}.                 \tag{11}
\]

Indeed each of the four products is nonnegative and is bounded by its
Gaussian exponential moment, with prefactors O(t), O(sqrt(t)), or O(1).
This remains valid for H=J, so diagonal pairs need no density formula.

## 3. Proof of Theorem A

Apply (10) to pairs with v_x,v_y>=t/2 and c_xy<=t/4. For q,r<=C_0,
exp(beta^2(q+r)/2)(1+|q|+|r|)^4 is uniformly bounded. For any epsilon>0,
(1+c)^4<=C_epsilon exp(epsilon c). Choose epsilon with
(beta^2+epsilon)g<2. Equations (1), (2), and (10), divided by N^4
and summed, give O(t^{-2}).

The excluded pairs have either v_x<t/2 or v_y<t/2, or c_xy>t/4.
The first two classes contribute at most Ct N^{-1/2} by (1), (2),
(11), and their O(N^{3/2}) possible bad vertices. For the last class,
(1) implies |x-y|<=A N^{3/4}. Equations (3) and (11) bound its
contribution by Ct N^{-(2-p)/4}. Each is O(t^{-2}). Therefore

\[
 E\left[\left(N^{-2}\sum_x(A(h_x)-B(h_x))\right)^2\right]
 \le Ct^{-2}+Ct[N^{-1/2}+N^{-(2-p)/4}]=O(t^{-2}).
\]

This is (A), since t=g log N. Chebyshev's inequality gives (A1).
The same proof works with any uniformly bounded deterministic weights
on the vertices, with a factor equal to their squared sup norm.

## 4. Quantitative diagonal approximation in a square

The following elementary finite-difference argument supplies the precision
needed for the mean expansion; qualitative convergence alone would not.
Let u=x/N have distance at least delta from the boundary and Ndelta>=2.
Define F_u(y) to be the continuum harmonic extension in D of the boundary
function log|z-u|, and F_{N,u}(y) the discrete harmonic extension of the
same boundary values on the lattice. Thus

\[
 q_x=c_0+gF_{N,u}(u)+O((N\delta)^{-2}),\quad
 q(u)=c_0+gF_u(u).                                      \tag{12}
\]

The first equality follows from the potential-kernel identity at x; the
second is the harmonic-measure definition of conformal radius.
Both extensions have sup norm at most C+|log delta|. At a point y
within epsilon of the boundary, each differs from the boundary value
at a nearest boundary point b by at most

\[
 C\delta^{-1}\sqrt{\epsilon+N^{-1}}.                     \tag{13}
\]

For the discrete function, stop the walk on exiting D. The projected
one-dimensional walk in the direction of a nearest side has mean exit
time at most CN^2(epsilon+N^{-1}); the two-dimensional exit occurs
no later. The martingale |S_n-S_0|^2-n, followed by Cauchy–Schwarz,
bounds the mean scaled exit displacement by C sqrt(epsilon+N^{-1}).
The boundary function is delta^{-1}-Lipschitz because both its radii
are at least delta. This proves (13). Brownian motion and its analogous
exit-time and squared-displacement martingales prove the continuum
assertion. Boundary regularity of a square ensures that this represents
the harmonic extension also at its corners.

On points at distance >=epsilon from the boundary, the interior
derivative estimate for harmonic functions gives
|D^4 F_u|<=C epsilon^{-4}(1+|log delta|). Taylor expansion of the
four-neighbor average cancels the second derivatives because Delta F_u=0.
Its discrete harmonicity defect is therefore bounded by
CN^{-4}epsilon^{-4}(1+|log delta|), as long as N^{-1}<epsilon/2.
Stop the walk on first entering the epsilon boundary layer. The expected
number of steps is at most CN^2. Optional summation of this defect,
together with (13), proves, for dist(y,boundary)>=2epsilon,

\[
 |F_{N,u}(y)-F_u(y)|
 \le C\delta^{-1}\sqrt{\epsilon+N^{-1}}
       +CN^{-2}\epsilon^{-4}(1+|\log\delta|).             \tag{14}
\]

Take epsilon=N^{-1/4}, and then delta=N^{-1/100}. Equations (12)–(14)
show a uniform polynomially small error on this shrinking bulk. In particular
the error is O(N^{-1/8}delta^{-1}+N^{-1}(1+|log delta|)
+(Ndelta)^{-2}). All constants may be increased to handle small N.

For completeness the Riemann-sum step is quantitative too. Differentiating
the boundary data with respect to u costs at most delta^{-1}, by the
maximum principle. Differentiating F_u in its evaluation variable costs
at most Cdelta^{-1}(1+|log delta|), by the interior harmonic gradient
estimate. Hence the gradient of q is bounded by this latter quantity
on the delta bulk. For any fixed a>0 and polynomial P, both
exp(aq)P(q) and its derivative as a function of q are bounded on
(-infinity,C], and q_x,q(u)<=C. Apply the gradient bound on cells
wholly in the bulk. Cells meeting its boundary and all cells in the
outer strip have total area O(delta+N^{-1}), and their summands are
uniformly bounded. It follows that

\[
 {1\over N^2}\sum_{x\in V_N}e^{a q_x}P(q_x)
       =\int_D e^{a q(u)}P(q(u))\,du+O_{a,P}(N^{-1/100}). \tag{15}
\]

The omitted lattice boundary row is also covered by this strip estimate.
In bounding the Riemann error one may enlarge the removed strip by
sqrt(2)/N; its remaining cells then stay at distance at least delta/2.

## 5. Proof of Theorem B

The one-variable analogue of the tilted integral is exact:

\[
 E A(h_x)=c_\beta e^{\beta^2q_x/2}
   \sqrt{t/(t+q_x)}\,
   E\exp\{- (S-\beta q_x)^2/[2(t+q_x)]\}.               \tag{16}
\]

For v_x>=t/2, the same Taylor bounds as in Section 2 give

\[
 E A(h_x)=c_\beta e^{\beta^2q_x/2}
   \left[1+{q_x/2-\beta^2q_x^2/2-1/\beta^2\over t}\right]
 +O(t^{-2}e^{\beta^2q_x/2}(1+|q_x|)^4).                \tag{17}
\]

The last factor is uniformly bounded for q_x<=C. Vertices with v_x<t/2
are O(N^{3/2}) in number. Their normalized contribution, and that of
the omitted leading and first-order terms, is O(sqrt(t)N^{-1/2}):
for A use 1_{h>=beta t}<=exp(beta h-beta^2t), and for the others use
boundedness of exp(beta^2q/2) times a polynomial. Summing (17), using
(15) with P=1 and with P(q)=q/2-beta^2q^2/2-1/beta^2, yields (B) and
(B1). Polynomial errors are absorbed by O(t^{-2}). No second-moment
assumption is required here, so lambda can range over all of (0,1).

Biskup's Lemma 3.10 (p. 39) identifies this leading expectation; the
GMC identification, or the expectation identity in Biskup–Louidor,
Theorem 2.3(3), identifies it with E[Z_lambda(D)/beta]. In particular,
there is no assumption here that convergence in distribution by itself
preserves the mean.

The coefficient is strictly negative pointwise, since

\[
 q/2-\beta^2q^2/2-1/\beta^2
 =-{\beta^2\over2}\left(q-{1\over2\beta^2}\right)^2
                         -{7\over8\beta^2}<0.           \tag{18}
\]

The integrals are finite because exp(beta^2q/2) times any fixed
polynomial in q is bounded above, and the square has finite area.
Finally |EY-EZ|<=W1(Law(Y),Law(Z)) for any integrable Y,Z, by either
the coupling definition or the 1-Lipschitz test function f(x)=x.
Equation (B2) follows from (B).

Equivalently, regarding m_lambda as a function m(beta) with
lambda=beta sqrt(g)/2, differentiation under the integral gives
B_lambda=-m''(beta)/(2g). Domination follows from boundedness of
exp(beta^2 q/2) times polynomials in q on any compact beta interval
inside (0,infinity). This provides a second derivation of (B1).

## 6. What this leaves open

Equation (A) alone does not quantify the coupling error of M_N to the
continuum GMC, and (B2) is a lower bound, not a matching upper bound.
Neither proof identifies a law for (log N)(X_N-W_lambda) in a prescribed
coupling. They do identify an unavoidable deterministic component at that
scale and a controlled finite-lattice comparison. A fluctuation conjecture
motivated by parameter derivatives of M_N is tested separately in the
numerical work, without being promoted to a theorem.

## Computation and checks

The sampler diagonalizes I-P in the orthonormal sine basis on
{1,...,N-1}^2. Its eigenvalues are

\[
 d_{kl}=\sin^2(\pi k/(2N))+\sin^2(\pi l/(2N)).
\]

Independent standard normal coefficients divided by sqrt(d_kl), followed by
an orthonormal type-I sine transform, give exactly covariance G_N=(I-P)^-1
in exact arithmetic. In particular, sampling the inverse of the unscaled
graph Laplacian would lose a factor four; this implementation includes it.
The boundary is zero at coordinates 0 and N, with (N-1)^2 random sites.

### Sampling and resource record

There are 7,636 independent fields, with four lambda values
(0.2, 0.4, 0.6, 0.8) measured on each, for 30,544 count observations.
The main and independent calibration batches use float64. The three N=8192
fields and one N=16384 field use float32. The largest grid contains
268,402,689 random sites. It is the largest dyadic grid whose float32
field fits below 4 GB; the next, N=32768, requires more than 4 GB for
the field alone. This is not a claim to optimize all possible grid sizes
or all sampling algorithms under the memory cap.

Each FFT uses one worker, and numerical library thread limits are set to
one. Priority was inherited as nice 15, below the requested priority 10;
raising it to exactly 10 was disallowed, so it remained 15. The largest
observed process peak was 1.485242 GB. The largest-grid preflight
budget was 3.421 GB. Jobs ran sequentially, with no retained fields or
background jobs. Their metadata, seeds, durations and peaks are saved.
The largest four fields are scale/resource checks, not reliable mean,
variance or distribution estimates.

### Empirical size distributions

At N=512, pooling 2,350 independent fields gives the following. Standard
errors are empirical Monte Carlo standard errors, not certified bounds
for heavy tails. The exact means use Gaussian tails and an independently
computed covariance diagonal, without Monte Carlo.

| lambda | mean | standard error | sample variance | median | 95% quantile | exact mean |
|---:|---:|---:|---:|---:|---:|---:|
| 0.2 | 0.636784 | 0.003983 | 0.037287 | 0.610727 | 1.002649 | 0.642421 |
| 0.4 | 0.415721 | 0.004751 | 0.053041 | 0.358060 | 0.885437 | 0.422967 |
| 0.6 | 0.333747 | 0.006713 | 0.105905 | 0.226230 | 0.982017 | 0.343309 |
| 0.8 | 0.321910 | 0.012325 | 0.357002 | 0.111923 | 1.246543 | 0.339022 |

The distributions are asymmetric and increasingly sensitive to rare fields
as lambda increases. At lambda=0.8, the limiting GMC mass has infinite
second moment: its two-point moment kernel has the nonintegrable
diagonal singularity |u-v|^{-4 lambda^2}. A finite-N sample variance
cannot be treated as an estimate of a finite limiting variance there.
At lambda=0.6, second moments exist but fourth moments of the limiting
chaos need not; second-moment error estimates can still be sensitive
to missed tails. Pooling the calibration fields changed some empirical
second moments substantially. The tables retain those outcomes.

[Empirical distribution functions](data/level_size_ecdf.svg) compare
N=128, 512 and 2048. CSV summaries also include skewness, excess kurtosis,
5% and 95% quantiles, and comparisons to exact means. Different N values
use independent fields. These simulations do not directly sample a
coupled continuum Z_lambda, and their residuals are not asserted to be
X_N minus a sample of that continuum limit.

### Exact mean and the slow approach to the bias coefficient

The diagonal of G_N was computed in O(N^2 log N) work using the identity
sin^2(a)=(1-cos(2a))/2 and a type-I cosine transform. Summing univariate
Gaussian upper tails then gives E X_N exactly up to floating-point error.
The continuum integrals are computed independently from the disk-to-square
conformal map f'(z)=C/sqrt(1-z^4), C=0.5393526011883794. Analytic
derivatives of its positive beta-function series give the q and q^2
moments in B_lambda. The area integral returns 1.0000000000018; doubling
the series cutoff changes the reported constants by less than 4e-11.
These are numerical stability checks, not interval-arithmetic enclosures.

| lambda | continuum mean m | bias coefficient B | exact E X_8192 | log(8192)(E X_8192-m) |
|---:|---:|---:|---:|---:|
| 0.2 | 0.996701 | -6.285957 | 0.701965 | -2.655844 |
| 0.4 | 0.513271 | -0.854987 | 0.444477 | -0.619896 |
| 0.6 | 0.386674 | -0.334764 | 0.354899 | -0.286327 |
| 0.8 | 0.377899 | -0.285734 | 0.349695 | -0.254138 |

Thus the negative bias is visible, but the first-order coefficient has
not been reached at these sizes, especially for lambda=0.2. The Gaussian
tail expansion requires beta^2 t=4 lambda^2 log N to be large. Making
lambda small improves moment integrability while making this numerical
asymptotic regime much harder to reach. The discrepancy in the last
table is consistent with the higher-order terms; it is not evidence for
a different asymptotic exponent. The full first-order remainders are
saved in data/exact_means.csv.

[Scaled mean bias](data/mean_bias.svg) displays that discrepancy directly.

### Fitted finite-size rates

The fitted model is RMSE(X_N-c_beta M_N) proportional to (log N)^(-p),
using N=256,512,1024,2048. Each N is resampled independently in 500
bootstrap replicates. This is a fit to the finite-lattice comparison,
not a fit of a distance to the continuum law. The last column fits the
exact deterministic bias m-E X_N on the same range.

| lambda | fitted p for RMSE | bootstrap percentile range | exact mean-bias exponent |
|---:|---:|---:|---:|
| 0.2 | 0.421 | [0.397, 0.442] | 0.482 |
| 0.4 | 0.517 | [0.212, 0.825] | 0.720 |
| 0.6 | 1.069 | [-0.202, 2.615] | 0.829 |
| 0.8 | 1.474 | [-0.682, 3.048] | 0.857 |

These finite-range exponents do not establish an asymptotic power. The
small-lambda fits are preasymptotic, as the exact mean demonstrates;
the larger-lambda fits have substantial tail uncertainty that an empirical
bootstrap can miss. The lambda=0.8 comparison is outside Theorem A's
L2 range. No asymptotic-rate claim is based on that row.

[Comparison rate plots](data/comparison_rate.svg) show both the raw RMSE
and log N times RMSE. All point estimates, fitting choices, bootstrap
seeds, and percentile ranges are saved in data/fits.json.

### Fluctuation candidate: a calculation to test, not a theorem

Formal Laplace inversion around its saddle point suggests, with
F_N(beta)=c_beta M_N(beta),

\[
 X_N=F_N(\beta)-{1\over2t}F_N''(\beta)+\text{smaller terms}.
 \tag{C}
\]

The experiments save D_N=(log N)(X_N-F_N) and the proposed proxy
-F_N''/(2g), using analytic derivatives of the finite sum. Their
empirical differences remain appreciable, particularly at lambda=0.2.
The raw residual has strong skewness in several batches; its
[Gaussian quantile plots](data/residual_qq.svg) do not support an
unqualified finite-size Gaussian approximation.

There is also a structural reason to avoid guessing a central limit
theorem from independent-site counting. If Q_beta=-1/2 partial_beta^2
+ beta^{-1} partial_beta - beta^{-2}, the candidate is c_beta Q_beta M_N/g.
On a power beta^k, Q_beta has coefficient -(k-1)(k-2)/2 times beta^{k-2}.
The linear and quadratic chaos terms cancel. Apart from the deterministic
term, its small-beta expansion starts at third Gaussian chaos. Establishing
(C) with a sufficiently small remainder and identifying it in a specified
DGFF/continuum coupling are further proof obligations. A limiting
non-Gaussian derivative-chaos law is a candidate, not a result of this report.

### Verification and reproduction

- code/validate.py builds the full sampler matrix at N=4,7,12. Its
  covariance agrees with a direct inverse of I-P to at most 1.8e-15;
  the independent diagonal cosine transform agrees to 1.4e-15.
- Float32 and float64 sampling from identical coefficients at N=128
  differ by 2.2e-7 RMS and 1.1e-6 at worst. Large-grid float32 results
  are approximate floating-point samples; no exact threshold-count
  equality with a float64 realization is claimed.
- Direct Gaussian quadrature checks the two-variable saddle cancellation:
  t^2 times the cancelled moment kernel at t=50,100,200,400 is
  1.2983,1.3949,1.4498,1.4792, consistent with a second-order remainder.
- A five-point finite difference of the independently integrated m(beta)
  verifies B=-m''/(2g) within 3.4e-10. The center diagonal constant is
  checked separately; its errors decrease from 6.5e-5 at N=64 to
  2.5e-7 at N=1024.
- code/audit.py checks sample counts, normalizations, every recorded
  resource cap, the bias identity, source-text decoding, and the absence
  of PDFs and paper images. Results are in data/audit.json.

Run from this directory, with Python 3, NumPy, SciPy and Matplotlib installed:

```sh
python3 code/fetch_sources.py
python3 code/validate.py
python3 code/experiment.py --plan main
python3 code/experiment.py --plan large
python3 code/experiment.py --plan calibration
python3 code/exact_means.py
python3 code/analyze.py
python3 code/audit.py
python3 code/build_report.py
```

Run numerical scripts sequentially. They retain the current process's nice
priority if it is at least 10 and otherwise request nice 10. In this run it
was 15. No new packages, scheduled tasks, visible terminals, publications,
pushes or external application changes were created.


## Literature audit and exact references

Search date: 13 November 2026. Primary-source texts are under sources/;
the manifest records text hashes and source URLs. Page references below are
one-based PDF/printed arXiv pages unless a journal page is explicitly given.
Searches are evidence of what was located, not a proof that no other work exists.

## Exact source and normalization

[M. Biskup, arXiv:1712.09972v4](https://arxiv.org/abs/1712.09972v4),
*Extrema of the two-dimensional discrete Gaussian free field*, revised
17 August 2019; published in Springer Proceedings in Mathematics &
Statistics 304 (2020), 163–407, DOI 10.1007/978-3-030-32011-9_3.
Saved complete as sources/biskup_1712.09972.txt, 235 pages.

- Theorem 1.17, p. 14: bulk diagonal and off-diagonal Green asymptotics.
- Lemma 1.21, p. 15: potential-kernel expansion including its constant.
- Section 2, pp. 19–32; specifically Theorem 2.7, pp. 26–27,
  and Corollary 2.9, p. 27. The count's limit is Z_lambda(D)/(alpha lambda).
- Intermediate-level arguments: Lectures 3 and 4, pp. 33–58;
  Lemma 3.6, pp. 37–38; Lemma 3.10, pp. 39–40; Lemma 3.11,
  pp. 40–42; GMC identification in Sections 4.3–4.4, pp. 50–56;
  truncation beyond the second-moment phase in Section 4.5, pp. 57–58.
- Problem 16.2, p. 220, following Problem 16.1. Its three requests are a
  rate of convergence, limiting fluctuations, and probabilities of deviations
  tending to zero. Its following paragraph explicitly allows that last
  interpretation to be broad. The p. 220 designation is verified for arXiv v4;
  it should not be transferred automatically to the Springer volume pagination.
  A text-only check of the reproduced volume places the problem on p. 392;
  details are in sources/page_map.txt. The user's p. 220 matches arXiv v4.

The whole indicated sections, rather than only the abstract or problem
statement, were consulted. The source text retains form feeds for page lookup.

Normalization check: equations (2.32), (3.24) and (3.57) imply
E Z_lambda(D)=beta m_lambda with beta=alpha lambda. The displayed
(3.60)–(3.61) on arXiv v4 p. 44 appear to miss this factor in their
intensity constant. The constants in this report are derived directly
from the Gaussian tail, and checked against the independent conformal
integral, rather than copied from that display.

## Direct results for the specified DGFF count

[M. Biskup and O. Louidor, arXiv:1612.01424](https://arxiv.org/abs/1612.01424),
*On intermediate level sets of two-dimensional discrete Gaussian free field*,
Ann. Inst. H. Poincaré Probab. Statist. **55** (2019), no. 4, 1948–1987,
DOI 10.1214/18-AIHP939. The arXiv v1 and the
[author's final AIHP manuscript](https://www.math.ucla.edu/~biskup/PDFs/papers/GFF-intermediate-final-AIHP.pdf)
are both saved. Theorem 2.1, p. 3, is the process limit; Corollary 2.2,
p. 4, gives the count; Theorem 2.3(3), p. 4, gives its limiting intensity;
Theorem 2.5, p. 6, identifies it as weighted subcritical GMC. These results
establish the limit and its mean, without a quantitative N-rate or a
second-order fluctuation law. Section 2.4 discusses remaining questions.

[E. Aïdékon, Y. Hu and Z. Shi, arXiv:1710.00348v2](https://arxiv.org/abs/1710.00348v2),
*Large deviations for level sets of branching Brownian motion and Gaussian
free fields*. Original: Zapiski Nauchnykh Seminarov POMI **457** (2017),
12–36. English translation: *Large Deviations for Level Sets of a Branching
Brownian Motion and Gaussian Free Fields*, Journal of Mathematical Sciences
**238** (2019), no. 4, 348–365,
[DOI 10.1007/s10958-019-04243-8](https://doi.org/10.1007/s10958-019-04243-8).
Theorem 4.1, **arXiv v2 p. 14**, proves

\[
 \lim_{N\to\infty}{\log P(\#H_N(\lambda)\ge N^{2a})\over\log N}
   =-\left({2\lambda^2\over1-a}-2\right),
 \qquad 1-\lambda^2<a<1.
\]

Here their gamma=sqrt(2/pi)=sqrt(g) and their eta=lambda, so the threshold
and covariance normalization match exactly. The definition and setting
are on arXiv pp. 13–14; the proof occupies Section 4. This directly settles
the upper-deviation question on the scale N^{2a}, with speed log N and
the displayed exponent. In terms of X_N, its threshold is
sqrt(log N) N^{2(a-1+lambda^2)}. This tends to infinity; it is not a
fixed-multiple deviation of the limiting random mass. An attempted journal
PDF fetch returned HTML rather than PDF, so no unverified journal theorem
page is assigned; the exact theorem and arXiv page above are verified.

[O. Daviaud, arXiv:math/0406609v4](https://arxiv.org/abs/math/0406609v4),
*Extremes of the discrete two-dimensional Gaussian free field*, Ann.
Probab. **34** (2006), no. 3, 962–986,
DOI 10.1214/009117906000000061. Theorem 1.3, arXiv p. 4,
gives the high-point cardinality exponent and a quantitative lower-tail
estimate below that exponent. It concerns a fixed interior subbox. That
lower-tail estimate is also valid as an upper bound for the whole-box
small-count event, by inclusion. It is not a lower-tail estimate for a
fixed positive value of X_N, which has a nondegenerate random limit.

Explicitly, equation (1.8) in that theorem states, for every delta>0,
P(|H_N(lambda)|<=N^{2(1-lambda^2)-delta})<=exp(-c(log N)^2)
for all sufficiently large N. This gives an upper bound with speed
(log N)^2, without an identified sharp constant for this event.

Thus the broad third part already has substantive answers in print.
It would be incorrect to report all deviation questions as unresolved.

## Named nearby literature: what it does and does not supply

[M. Biskup and O. Louidor, arXiv:1606.00510](https://arxiv.org/abs/1606.00510),
*Full extremal process, cluster law and freezing for the two-dimensional
discrete Gaussian free field*, Advances in Mathematics **330** (2018),
589–687, DOI 10.1016/j.aim.2018.02.018. Theorem 2.1, p. 4; Theorem
2.3, p. 6; Theorem 2.6, pp. 8–9; Corollary 2.8, p. 10. These concern
the extremal process around m_N, cluster laws, and supercritical Gibbs
weights/freezing, rather than second-order behavior at fixed lambda<1.

[J. Junnila, E. Saksman and C. Webb, arXiv:1806.02118v2](https://arxiv.org/abs/1806.02118v2),
*Imaginary multiplicative chaos: moments, regularity and connections to the
Ising model*, Ann. Appl. Probab. **30** (2020), no. 5, 2099–2164,
DOI 10.1214/19-AAP1553. Theorems 1.1, 1.2 and 1.3, arXiv pp. 3–5,
give convergence/uniqueness, regularity, and moments of imaginary chaos.
No theorem translating those estimates into a quantitative rate for the
positive DGFF high-point count was located. Oscillatory chaoses and
real-positive high-point indicators are different observables.

[J. Junnila, E. Saksman and C. Webb, arXiv:1808.06838v3](https://arxiv.org/abs/1808.06838v3),
*Decompositions of log-correlated fields with applications*, Ann. Appl.
Probab. **29** (2019), no. 6, 3786–3820, DOI 10.1214/19-AAP1492.
Theorem A, p. 2, and Theorem 4.5, p. 13, supply decompositions;
Theorem 5.3, pp. 17–18, treats critical chaos; Theorem 6.1, pp. 20–21,
gives holomorphic dependence on the chaos parameter. This last result
supports studying parameter derivatives as possible fluctuation terms.
It does not identify the fluctuation of a threshold count or specify
a finite-difference DGFF-to-continuum rate.

[H. Lacoin, R. Rhodes and V. Vargas, arXiv:1307.6117](https://arxiv.org/abs/1307.6117),
*Complex Gaussian multiplicative chaos*, Comm. Math. Phys. **337**
(2015), 569–632, DOI 10.1007/s00220-015-2362-4. Theorem 3.1, p. 11,
is convergence in the inner phase I; Theorem 4.2, p. 22, gives Gaussian
white-noise limits in phase III. These are complex-exponential phase
limits, not a count CLT in the present model. More recent Lacoin work
located includes arXiv:2301.05274, *Convergence for Complex Gaussian
Multiplicative Chaos on phase boundaries* (2023/2024); its object is
again complex chaos. No DGFF-count answer was found in these searches.

[C. Garban, N. Holden, A. Sepúlveda and X. Sun, arXiv:1805.00864v2](https://arxiv.org/abs/1805.00864v2),
*Negative moments for Gaussian multiplicative chaos on fractal sets*,
Electron. Commun. Probab. **23** (2018), paper 100, 1–10,
DOI 10.1214/18-ECP168. Theorem 1.1 and Remark 1.2, arXiv p. 3,
give all negative moments and faster-than-any-power small-mass bounds
for the limiting subcritical GMC. Weak convergence does not permit
substituting an N-dependent shrinking threshold into this result. It
therefore does not itself give a finite-N lower-deviation estimate.

[N. Berestycki, C. Webb and M. D. Wong, arXiv:1701.03289](https://arxiv.org/abs/1701.03289),
*Random Hermitian matrices and Gaussian multiplicative chaos*, Probab.
Theory Related Fields **172** (2018), 103–189,
DOI 10.1007/s00440-017-0806-9. Theorem 1.1, arXiv p. 2, is a
subcritical GMC limit for characteristic-polynomial powers in unitary
invariant Hermitian ensembles. It does not estimate the DGFF count.

[J. Junnila, G. Lambert and C. Webb, arXiv:2209.06548v2](https://arxiv.org/abs/2209.06548v2),
*Multiplicative chaos measures from thick points of log-correlated fields*,
Comm. Pure Appl. Math. **77** (2024), no. 11, 4212–4286,
DOI 10.1002/cpa.22205 (first published 17 May 2024).
Theorem 1.8, p. 7, identifies thick-point and exponential-chaos limits
in L1 under its assumptions. Theorem 1.4, p. 4, applies to continuum
mollifications; Theorem 1.2, p. 3, to CUE. The discussion on p. 5
explicitly leaves graph-discretization modifications uncarried out.
This is the most directly relevant later framework located, but its
stated convergence does not provide the requested DGFF N-rate or
second-order fluctuation law.

[J. Aru, T. Lupu and A. Sepúlveda, arXiv:1805.09204](https://arxiv.org/abs/1805.09204),
*The first passage sets of the 2D Gaussian free field: convergence and
isomorphisms*, Comm. Math. Phys. **375** (2020), 1885–1929,
DOI 10.1007/s00220-020-03718-z. Proposition 4.7, arXiv p. 21,
and Proposition 4.11, p. 23, concern convergence of
metric-graph first passage sets, local sets, and Minkowski content.
These are distinct from the number of vertices above a height growing
as a fixed fraction of the maximum. No count-rate/CLT result was located.

E. Bolthausen, J.-D. Deuschel and G. Giacomin, *Entropic repulsion and
the maximum of the two-dimensional harmonic crystal*, Ann. Probab.
**29** (2001), 1670–1692, DOI 10.1214/aop/1015345767, is the
background source for the maximum and hard-wall entropic repulsion.
Its results are not here asserted to give an exact rate function for
small normalized high-point mass: a hard-wall event and that event
are not equivalent. An accessible full text was sought separately;
any access failure is recorded rather than hidden by a guessed theorem.

## Searches with no verified matching citation

The suggested Kim–Lee title "Large deviations for intermediate level sets"
could not be verified by exact-title and combined author/title searches.
Likewise, no Cerf–Dembo joint result on this DGFF count was verified.
This is not an assertion that these people have no related work.

Representative queries used: "intermediate level sets" "large deviations";
"intermediate level sets" "convergence" "rate"; "Gaussian free field"
"level set size" fluctuations; "Gaussian free field" "moderate deviations"
"level sets"; DGFF fluctuations level 2024 2025 2026; Kim Lee Gaussian
free field deviations; Cerf Dembo Gaussian field deviations; rate of
convergence Gaussian multiplicative chaos; and author/name combinations
for every group listed above. Searches through 2026 also returned
dimension >=3 cluster-count CLTs (McAuley–Muirhead, arXiv:2501.14707),
integer-valued surfaces with floors, and BBM results. These were not
treated as solutions of the specified zero-boundary two-dimensional count.

## Assessment

Located direct results settle substantial upper and lower deviation regimes.
The searches and full-text checks did not locate a quantitative convergence
rate or a limiting second-order fluctuation law for the stated count.
Accordingly this project uses PARTIAL, not RESOLVED_IN_LITERATURE.
The estimates in PROOFS.md address a remaining quantitative aspect, with
the distinction between finite-lattice chaos and the continuum limit explicit.

## Remaining problem

A matching quantitative upper bound to the law of Z_lambda(D)/beta
requires control of the finite-lattice exponential mass against a
specified continuum GMC approximation. Theorem A does not supply that
control. A fluctuation law around the random limit requires a coupling
and a proof of the second-order expansion, beyond its mean. Existing
upper-deviation exponents and lower-deviation bounds cover important
vanishing-probability events, but do not settle all shrinking-threshold
or moderate-deviation regimes. These are the reasons for the PARTIAL
status. No solution of all three requests is claimed.
