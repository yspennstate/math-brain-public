# An empty-interval criterion for the nearest-neighbour part of T089

This is a deterministic reduction. It does not establish the required
empty-interval estimate for a chaotic billiard. The square-root loss in the
quantitative reduction is optimal under the stated regularity assumptions.

## 1. Finite-window definitions

Let W > 0 and let

\[
0\leq y_1\leq\cdots\leq y_N<W,\qquad N\geq2.
\]

Multiplicity is allowed. Define the cyclic gaps

\[
g_j=y_{j+1}-y_j\ (j<N),\qquad g_N=W-y_N+y_1,
\qquad \rho=N/W.
\]

Thus all gaps are nonnegative and their sum is W. Put

\[
F_N(s)=\frac1N\sum_{j=1}^N\mathbf1_{\{g_j\leq s\}},
\qquad
V_N(s)=\frac1W\sum_{j=1}^N(g_j-s)_+,\quad s\geq0.
\tag{1}
\]

Here V_N(s) is the probability that a positively oriented arc (t,t+s]
contains no points when t is uniform on the circle of circumference W. For
s < W, each gap of length g contributes precisely (g-s)_+ starting positions.
Endpoints have zero Lebesgue measure. For s >= W the probability and formula
are both zero. Repeated points contribute zero gaps and do not change this
argument.

The ordinary spacing CDF uses the N-1 internal gaps:

\[
F_N^{\rm int}(s)=\frac1{N-1}\sum_{j=1}^{N-1}
\mathbf1_{\{g_j\leq s\}}.
\]

If a is the number of internal gaps at most s and b is the indicator that the
cyclic gap is at most s, then

\[
F_N^{\rm int}(s)-F_N(s)
=\frac{a-(N-1)b}{N(N-1)}.
\]

Since 0 <= a <= N-1 and b is 0 or 1,

\[
\sup_{s\geq0}|F_N^{\rm int}(s)-F_N(s)|\leq1/N.
\tag{2}
\]

No upper bound on the largest gap is used.

Let F be a continuous probability CDF on [0,infinity), with F(0)=0 and mean
one. Its integrated survival function is

\[
E(s)=\int_s^\infty(1-F(u))\,du
=1-\int_0^s(1-F(u))\,du.
\tag{3}
\]

It is convex, nonincreasing, 1-Lipschitz, and continuously differentiable with
E'(s)=F(s)-1. In the GOE application, F is the exact unit-mean GOE bulk
nearest-neighbour CDF (the Gaudin law), and E is its integrated survival
function. No Wigner-surmise formula is substituted for F.

## 2. Quantitative theorem

Fix 0 < h <= S. Define

\[
\delta=\sup_{0\leq u\leq S+h}|V_N(u)-E(u)|,
\qquad
\omega(h)=\sup_{\substack{u,v\in[0,S+h]\\|u-v|\leq h}}
|F(u)-F(v)|.
\]

Then

\[
\boxed{\quad
\sup_{0\leq s\leq S}|F_N^{\rm int}(s)-F(s)|
\leq \frac1N+
\frac{2\delta/h+\omega(h)+|\rho-1|}{\rho}.
\quad}
\tag{4}
\]

### Proof

The right derivative of (1), including at a gap value and at zero, is

\[
(V_N)'_+(s)=-\frac1W\#\{j:g_j>s\}
=\rho(F_N(s)-1).
\tag{5}
\]

For s >= h, convexity gives the secant bounds

\[
\frac{V_N(s)-V_N(s-h)}h
\leq(V_N)'_+(s)
\leq\frac{V_N(s+h)-V_N(s)}h.
\tag{6}
\]

The right bound also holds for 0 <= s < h. Replacing the two endpoint values
in either secant by E costs at most 2 delta/h. Each secant of E is an average
of E'=F-1 on an interval of length h, so differs from F(s)-1 by at most
omega(h). For h <= s <= S this yields

\[
|\rho(F_N(s)-1)-(F(s)-1)|\leq2\delta/h+\omega(h).
\]

Use

\[
\rho(F_N-F)
=\rho(F_N-1)-(F-1)+(\rho-1)(1-F)
\]

and 0 <= 1-F <= 1. The result is the bound in (4), without 1/N, for the
cyclic CDF on [h,S].

For 0 <= s < h, the right secant gives the same upper bound for F_N(s)-F(s).
For the lower bound, F_N(s) >= 0 and F(s) <= omega(h), since F(0)=0. The
claimed bound still dominates omega(h): if rho <= 1 this follows from
omega(h)/rho >= omega(h); if rho >= 1, it follows from

\[
\frac{\omega(h)+\rho-1}{\rho}-\omega(h)
=\frac{(\rho-1)(1-\omega(h))}{\rho}\geq0.
\]

Finally use (2). This proves (4). In particular zero gaps and a very large
cyclic gap do not invalidate the estimate.

If F is M-Lipschitz on [0,S+h], then omega(h) <= Mh. For M > 0 and delta > 0,
the choice h = sqrt(2 delta/M), when it is <= S, gives

\[
\sup_{0\leq s\leq S}|F_N^{\rm int}(s)-F(s)|
\leq\frac1N+
\frac{2\sqrt{2M\delta}+|\rho-1|}{\rho}.
\tag{7}
\]

The interval on which delta is controlled must include this value of S+h.
Formula (4), rather than an unconstrained optimization, applies in every case.

## 3. A finite-grid certificate and window edges

Suppose a grid 0=t_0<...<t_m=R has largest interval length eta, R >= S+h,
and

\[
\max_i|V_N(t_i)-E(t_i)|\leq\epsilon.
\]

For t_i <= s <= t_{i+1}, monotonicity of V_N sandwiches it between its two
endpoint values. Since E is 1-Lipschitz,

\[
V_N(s)-E(s)\leq\epsilon+E(t_i)-E(s)\leq\epsilon+\eta,
\]

and

\[
V_N(s)-E(s)\geq-\epsilon+E(t_{i+1})-E(s)
\geq-\epsilon-\eta.
\]

Consequently (4) applies with delta replaced by epsilon+eta. Certified
absolute error tau in the tabulated values of E increases this to
epsilon+eta+tau. This is a deterministic grid certificate, not an estimate of
sampling uncertainty for Monte Carlo starts.

There is also a version using physical intervals without wrapping. For 0 <= s
< W define

\[
R_N(s)=\frac1{W-s}\int_0^{W-s}
\mathbf1_{\{(t,t+s]\ \text{has no points}\}}\,dt.
\]

Let A be this integral before normalization, and let B be the contribution
of the remaining starting positions [W-s,W) to the cyclic empty probability.
Then 0 <= A <= W-s and 0 <= B <= s. Hence

\[
V_N(s)-R_N(s)=B/W-\frac{sA}{W(W-s)},
\qquad |V_N(s)-R_N(s)|\leq s/W.
\tag{8}
\]

The two nonnegative terms are both at most s/W, so their difference is at
most s/W in absolute value; a factor of two is unnecessary. Thus grid errors
for R_N give a valid delta budget epsilon+eta+R/W (plus any table error),
provided R < W.

## 4. Equivalence and the Weyl-unfolded spectral window

Consider any sequence of finite windows with W -> infinity and rho=N/W -> 1.
Then the following are equivalent:

1. F_N^{int}(s) -> F(s) for all s >= 0.
2. V_N(s) -> E(s) locally uniformly on [0,infinity).

For (2) implies (1), fix S and h in (4), let N -> infinity, and then let
h decrease to zero. Continuity of F on each compact interval gives
omega(h) -> 0. For the reverse implication, first use inequality (2) to replace
the internal CDF by the cyclic one. Integrating (5)
gives the exact identity

\[
V_N(s)=1-\rho\int_0^s(1-F_N(u))\,du.
\tag{9}
\]

Therefore, for fixed S,

\[
\sup_{s\leq S}|V_N(s)-E(s)|
\leq S|\rho-1|+\int_0^S|F_N(u)-F(u)|\,du\longrightarrow0
\]

by dominated convergence. This avoids an unproved interchange of a limit and
a derivative. No moment assumption on individual finite windows is added;
their total gap length is exactly W. The target's mean-one assumption is used
in (3).

For a symmetry sector with counting function

\[
N_{\rm sec}(T)=cT+o(T),\qquad c>0,
\]

take the eigenvalues in [Lambda,2 Lambda), let

\[
y_j=c(\lambda_j-\Lambda),\qquad W=c\Lambda.
\]

Their number is c Lambda+o(Lambda), so rho -> 1 and N -> infinity. Thus the
nearest-neighbour part of T089 is equivalent to proving, for every fixed R,

\[
\sup_{0\leq s\leq R}
\left|\frac1{c\Lambda}\int_0^{c\Lambda}
\mathbf1_{\{\text{no unfolded level in the cyclic arc }(t,t+s]\}}
\,dt-E_{\rm GOE}(s)\right|\longrightarrow0.
\tag{10}
\]

By (8), cyclic arcs can be replaced by physical nonwrapping intervals without
changing the limit. Convergence only on increasingly fine finite grids is
sufficient by Section 3. This reduces the spacing assertion, not the full
point-process assertion, in T089.

The constant c must be the sector's Weyl coefficient. For a full planar
Dirichlet spectrum it is |Omega|/(4 pi). If Omega denotes the whole stadium
and one restricts to one of its four reflection-parity sectors, c is one
quarter of the full coefficient: the sector is a mixed Dirichlet/Neumann
problem on the quarter domain, and boundary conditions do not alter the
leading area term. If Omega already denotes that fundamental domain, its own
area gives the correct coefficient. More generally, if a sector has fraction
theta of the full leading density, its coefficient is theta |Omega|/(4 pi).
Using the full coefficient instead multiplies every correctly unfolded gap
by 1/theta, so a limiting CDF F becomes F(theta s), not F(s). This is an
exact scaling statement, not an inference from convergence of means alone.

## 5. Optimality of the square-root exponent

The exponent one half in (7) cannot be improved for all continuous targets
with bounded density, even when rho=1 and the data are exact finite spectra.

Take F(s)=s/2 on [0,2], extended by zero to the left and one to the right.
Its mean is one and

\[
E(s)=(2-s)^2/4\quad(0\leq s\leq2),\qquad E(s)=0\quad(s\geq2).
\]

Let N be even and start with the N gaps

\[
b_j=(2j-1)/N,\qquad j=1,\ldots,N.
\]

They sum to N. Choose 1 <= k <= N/2 and replace the central 2k gaps,
whose indices are N/2-k+1 through N/2+k, by the value 1. Call the resulting
gap CDF H and empty function U; these too are realized by N ordered points
on a circle of circumference N, by taking successive partial sums of the
positive gaps. Both means are exactly one. Set a=2k/N.

The unmodified midpoint-quantile CDF differs from F by at most 1/(2N).
Inside [1-a,1) the modified CDF is 1/2-k/N, and inside [1,1+a] it is
1/2+k/N. Outside this central interval it is the unmodified CDF. Hence

\[
\sup_{s\geq0}|H(s)-F(s)|=k/N.
\tag{11}
\]

For completeness, the midpoint empty function equals E at every cell
boundary 2j/N. On each such cell the sum defining it is the midpoint
quadrature for the convex hinge (t-s)_+. It is exact except in the one cell
containing s; its error there lies between -1/(4N^2) and zero. This follows
also by subtracting the quadratic E from the linear function on each side
of that cell's midpoint: the discrepancy vanishes at the cell endpoints
and has value -1/(4N^2) at its midpoint.

For s <= 1-a or s >= 1+a, replacing the central gaps preserves the empty
function: all replaced gaps are respectively above s, with unchanged total,
or below s. For 1-a <= s <= 1, the CDF H is constant and (9) gives

\[
U(s)-E(s)=-(s-(1-a))^2/4.
\]

For 1 <= s <= 1+a the same argument gives

\[
U(s)-E(s)=-(1+a-s)^2/4.
\]

The central maximum absolute error is a^2/4=k^2/N^2, attained at s=1.
It dominates the exterior error 1/(4N^2). Consequently

\[
\sup_{s\geq0}|U(s)-E(s)|=(k/N)^2,
\qquad
\sup_{s\geq0}|H(s)-F(s)|=
\sqrt{\sup_{s\geq0}|U(s)-E(s)|}.
\tag{12}
\]

For example k=1 and even N -> infinity rules out any universal bound
C delta^alpha with alpha > 1/2, already for this fixed continuous target
and unit-density cyclic spectra. This proves optimality of the exponent,
not of the numerical constant in (7), and makes no optimality assertion
specific to the GOE target. The internal CDF's explicit 1/N edge error
remains separate.

## 6. Remaining spectral input

No estimate in this note bounds (10) for a deterministic chaotic billiard.
The function in (10) is an empty-interval probability at unit spectral scale.
A smooth counting variance or a two-point form factor alone does not provide
that estimate. Establishing (10), even without a rate for one generic
symmetry-reduced chaotic billiard, remains the required spectral step.
