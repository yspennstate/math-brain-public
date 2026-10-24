Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.**

# HARD7-05 route note — finite Hermite/Ritz certificate for the edge-smoothed comparator

New-method route written **before** constructing the exact checker.

The previous run changed comparison category from a killed half-line AR(1) chain to the edge-smoothed Gaussian comparator

\[
Y_j=(U_j+U_{j-1})/\sqrt{2(1+r)},\qquad r=4/5,
\]

and proved source covariance domination at every sampled lag. Its survival rate is the top spectral radius of

\[
(T_rf)(x)=\int_{y<-x}k_r(x,y)f(y)\,\phi(dy),
\]

but it stopped before a rigorous numerical norm bound. Floating reconnaissance gives `||T_{4/5}||` near `0.874`, which would beat the current AR comparison if it can be bounded rigorously below about `0.87625`.

This run will try three genuinely different moves from the preceding B6/B21/B29 triple:

- **B8 (discretize, but only as a proof-guiding finite Ritz problem).** Project the positive Perron mode onto polynomials through degree 24, then turn the selected trial polynomial into an exact moment certificate. No sampled path or floating eigenvalue will be used as proof.
- **B10 (derandomize).** Replace the numerical top eigenfunction by one fixed rational/integer polynomial `f`; all theorem-deciding quantities will be evaluated by exact rational interval arithmetic.
- **B14 (find/use the symmetry).** At `r=4/5`, rotate the one-step pair by `A=(X+Y)/sqrt(2(1+r))`, `D=(X-Y)/sqrt(2(1-r))`, so `X=(3A+D)/sqrt(10)`, `Y=(3A-D)/sqrt(10)`, and the cut is simply `A<0`. For the residual norm, use the two edge sums `A=(X+Y)/sqrt(2(1+r))`, `B=(Y+Z)/sqrt(2(1+r))`, whose correlation is exactly `9/10`; conditional on `(A,B)`,
  \[
  X={84A-30B\over19\sqrt{10}}+E,\qquad
  Z={-30A+84B\over19\sqrt{10}}+E,
  \quad E\sim N(0,1/19),
  \]
  with `E` independent. This reduces every degree-24 residual moment to exact bivariate Gaussian quadrant moments.

The intended certificate is Kato--Temple rather than a finite-grid spectral approximation. For a fixed polynomial `f`, compute exactly

\[
\mu={\langle f,Tf\rangle\over\|f\|_2^2},\qquad
\varepsilon^2={\|Tf\|_2^2\over\|f\|_2^2}-\mu^2.
\]

Since

\[
\operatorname{tr}(T_r^2)=\|T_r\|_{HS}^2={1\over2(1-r^2)}={25\over18},
\]

`lambda_1>=mu` implies every other eigenvalue has squared modulus at most `25/18-mu^2`. If that is below `(791/1000)^2`, then Kato--Temple gives

\[
\lambda_1\le \mu+{\varepsilon^2\over\mu-791/1000}.
\]

The concrete target is to certify this upper bound below `701/800=0.87625`. Combined with the already proved all-lag Slepian comparison and sampling interval `Delta=4 log(5/4)`, that would give

\[
\theta_{2,1/4}>{-\log(701/800)\over4\log(5/4)}> {37\over250}=0.148,
\]

moving the frozen source bracket width from `0.103389` to `0.102`.

Counterexample-first check: the first failure mode tested was that the polynomial Ritz residual would be too large for the trace-two spectral separation. Degrees <=20 are marginal; the degree-24 route numerically clears the `701/800` cap with room, so it is worth exact certification. If exact interval arithmetic destroys that margin, this route is abandoned rather than reported as progress.
