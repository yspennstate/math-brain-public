# Quantitative estimates for C0002

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
