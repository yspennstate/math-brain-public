# Shortest crossings of the two-row ladder

Let \(G_n\) have vertices \((i,h)\), where \(0\leq i\leq n\) and \(h\in\{0,1\}\), horizontal edges \({(i-1,h),(i,h)}\) for \(1\leq i\leq n\), and vertical edges \({(i,0),(i,1)}\) for \(0\leq i\leq n\). Call the vertical edges rungs. Each edge is independently open with probability \(1/2\). The two vertices in column 0 are the left boundary, and those in column \(n\) are the right boundary. Boundary vertices are not identified, and boundary rungs are random.

Let \(H_n\) be the event that an open path connects these two boundaries. On \(H_n\), let \(S_n\) be the minimum number of edges in such a path, with its endpoints free to be any boundary vertices. Write \(T_n=S_n-n\). For \(n=0\), set \(H_0\) to be certain and \(S_0=T_0=0\).

**Theorem.** Define the unconditioned marked crossing probability

\[
 P_n(t)=\sum_{k\geq0}\mathbb P(H_n,\ T_n=k)t^k.
\]

Then, as a formal power series in \(z\),

\[
 \boxed{\quad
 \sum_{n\geq0}P_n(t)z^n
 =\frac{1-(1+t)z/8}
 {(1-z/4)\{1-(5+t)z/8+z^2/16\}}.
 \quad}                                                     \tag{1}
\]

In particular, putting

\[
 \lambda=\frac{3+\sqrt5}{8},\qquad
 \mu=\frac{3-\sqrt5}{8},
\]

gives

\[
 \mathbb P(H_n)=\frac{\lambda^{n+1}-\mu^{n+1}}{\lambda-\mu}.
                                                               \tag{2}
\]

The conditional mean and variance satisfy

\[
 \mathbb E[S_n\mid H_n]
 =\left(1+\frac1{2\sqrt5}\right)n+O(1),                         \tag{3}
\]

\[
 \operatorname{Var}(S_n\mid H_n)
 =\frac7{20\sqrt5}\,n+O(1).                                    \tag{4}
\]

Consequently, under the conditional law given \(H_n\), \(S_n/n\) converges in probability to \(1+1/(2\sqrt5)\). Every fixed conditional quantile of order strictly between 0 and 1, divided by \(n\), has the same limit.

These assertions concern a strip of fixed width. They do not identify the chemical-distance exponent for square boxes or compare that exponent between lattices.

## 1. Reduction of shortest paths to forced rail changes

For each \(i\in\{1,\ldots,n\}\), the cut between columns \(i-1\) and \(i\) consists of exactly two horizontal edges. A path from column 0 to column \(n\) crosses each such cut an odd number of times: every traversal changes which side of that cut contains the current vertex, and the endpoints are on opposite sides. A simple path cannot traverse either edge twice. Its number of traversals of the cut is therefore an odd positive integer at most two, hence exactly one.

A shortest path is simple, since deleting a cycle strictly decreases its length. The preceding observation shows that it is horizontally monotone. It has exactly \(n\) horizontal edges, and all its other edges are rungs. A shortest crossing uses no rung in column 0 or column \(n\): deleting that initial or terminal edge preserves a crossing because the endpoints are free. Thus the two boundary rungs never affect either \(H_n\) or \(S_n\).

Classify each horizontal cut as empty, double, top only, or bottom only. An empty cut prevents a crossing. A double cut has both edges open. A top-only or bottom-only cut forces the path onto the indicated rail; call such a cut single.

Suppose there are no empty cuts, and the single cuts occur at positions

\[
 i_1<i_2<\cdots<i_m.
\]

Between consecutive single cuts \(i_j\) and \(i_{j+1}\), let

\[
 r_j=i_{j+1}-i_j-1
\]

be the number of double cuts. If the two single cuts force the same rail, a path can stay on that rail throughout the intervening part. If they force opposite rails, every crossing must use at least one rung in columns \(i_j,\ldots,i_{j+1}-1\). Conversely, one open rung in these columns suffices: follow the first rail to that rung, change rail there, and follow the other rail to the next single cut. All the intervening horizontal cuts are double.

These sets of possible rung columns are disjoint for different consecutive pairs of single cuts. Thus a crossing exists precisely when every consecutive pair of opposite single cuts has at least one open rung between it. When a crossing exists, its minimum number of rungs equals the number of rail changes in the ordered list of single cuts. Indeed, each such change requires a rung in its own interval, and choosing one available rung in each of these intervals constructs a crossing attaining this lower bound. Before the first single cut and after the last one, the path can stay on the required rail. If \(m=0\), it can stay on either rail throughout and uses no rung.

This also proves the deterministic bounds \(n\leq S_n\leq2n-1\) for \(n\geq1\) on \(H_n\), because there are at most \(n\) single cuts and hence at most \(n-1\) changes.

## 2. The marked generating function

For this section only, allow an arbitrary edge probability \(p\in(0,1)\), and put

\[
 q=1-p,\qquad a=pq,\qquad b=p^2.
\]

A prescribed single-cut orientation has probability \(a\); a double cut has probability \(b\). When two consecutive single cuts have \(r\) double cuts between them, the number of candidate rungs is \(r+1\). The probability that at least one is open is \(1-q^{r+1}\). It is independent of all the horizontal cut states. The required rung events for different rail changes are independent, since their candidate sets are disjoint.

For a fixed orientation of one single cut, summing over the orientation of the next gives the transition weight

\[
 1+t(1-q^{r+1}).
\]

The first term corresponds to the same orientation; the second to the opposite orientation and its necessary open rung. The factor \(t\) records exactly one additional rung in a shortest crossing, even if several rungs happen to be open in that interval.

Let

\[
 A(z,t)=\sum_{r\geq0}(bz)^r\{1+t(1-q^{r+1})\}
 =\frac{1+t}{1-bz}-\frac{tq}{1-bqz}.
\]

If there are no single cuts, the contribution is \((1-bz)^{-1}\). If there are \(m\geq1\) single cuts, their orientations can be summed by first choosing either of two orientations and then applying the transition weight for each following single cut. The double runs before the first and after the last single cut each have generating function \((1-bz)^{-1}\). The resulting contribution for this value of \(m\) is

\[
 \frac{2az}{(1-bz)^2}\{azA(z,t)\}^{m-1}.
\]

Every horizontal cut sequence with no empty cuts has a unique decomposition of this kind. Summing over \(m\) therefore gives

\[
 F(z,t):=\sum_{n\geq0}P_n(t)z^n
 =\frac1{1-bz}
 +\frac{2az}{(1-bz)^2}\frac1{1-azA(z,t)}.                       \tag{5}
\]

All sums here are valid formal power series: \(azA(z,t)\) has zero constant coefficient. Rungs that are not needed for a forced change, including the two boundary rungs, have been summed out, each with total probability one.

For \(p=1/2\), \(a=b=1/4\) and \(q=1/2\). Bringing the denominator of the final factor in (5) to a common denominator gives

\[
\begin{aligned}
 D(z,t)
 &=(1-z/4)(1-z/8)
   -\frac z4\{(1+t)(1-z/8)-(t/2)(1-z/4)\}\\
 &=1-\frac{5+t}{8}z+\frac1{16}z^2.
\end{aligned}
\]

Thus

\[
 F(z,t)=\frac{D(z,t)+(z/2)(1-z/8)}{(1-z/4)D(z,t)}
 =\frac{1-(1+t)z/8}{(1-z/4)D(z,t)},
\]

which is (1).

## 3. Crossing probabilities

At \(t=1\), the numerator of (1) cancels \(1-z/4\), yielding

\[
 F(z,1)=\frac1{1-3z/4+z^2/16}
       =\frac1{(1-\lambda z)(1-\mu z)}.
\]

The coefficients of the last expression are

\[
 \sum_{j=0}^n\lambda^j\mu^{n-j}
 =\frac{\lambda^{n+1}-\mu^{n+1}}{\lambda-\mu},
\]

which proves (2).

## 4. Conditional mean, variance, and quantiles

For real \(t\) in a sufficiently small neighborhood of 1, define

\[
 \lambda(t)=\frac{5+t+\sqrt{(5+t)^2-16}}{16},\qquad
 \mu(t)=\frac{5+t-\sqrt{(5+t)^2-16}}{16}.
\]

These are distinct analytic functions there, and

\[
 D(z,t)=(1-\lambda(t)z)(1-\mu(t)z).
\]

At \(t=1\), \(\lambda(t)=\lambda>1/4>\mu=\mu(t)>0\). The three factors in the denominator of (1) are distinct near 1. Partial fractions therefore give analytic coefficients \(B(t),C(t),E(t)\) such that, for every \(n\),

\[
 P_n(t)=B(t)(1/4)^n+C(t)\lambda(t)^n+E(t)\mu(t)^n.              \tag{6}
\]

From (2), \(C(1)=\lambda/(\lambda-\mu)>0\). Shrink the neighborhood if necessary so that \(C\) and \(\lambda\) do not vanish and both other exponential bases remain smaller in modulus than \(\lambda(t)\), by a fixed factor less than one. Equation (6) and its first two derivatives then imply

\[
 \log P_n(t)=n\log\lambda(t)+\log C(t)+R_n(t),
\]

where \(R_n\) and its first two derivatives at \(t=1\) tend to zero. For example, after dividing (6) by \(C(t)\lambda(t)^n\), each differentiated remaining term is bounded by a constant times \(n^2\eta^n\) for some \(\eta<1\). This also justifies all subsequent differentiations of the asymptotic expression.

The conditional probability generating function of \(T_n\) is \(P_n(t)/P_n(1)\). Its moment generating function is \(P_n(e^\theta)/P_n(1)\). Consequently its mean and variance are, respectively, the first and second derivatives at \(\theta=0\) of

\[
 \log P_n(e^\theta)-\log P_n(1).
\]

Differentiating the displayed formula for \(\lambda(t)\), or its quadratic equation, gives

\[
 \frac{d}{dt}\log\lambda(t)
 =\frac1{\sqrt{(5+t)^2-16}},\qquad
 \frac{d^2}{dt^2}\log\lambda(t)
 =-\frac{5+t}{\{(5+t)^2-16\}^{3/2}}.
\]

It follows that

\[
 \left.\frac d{d\theta}\log\lambda(e^\theta)\right|_{\theta=0}
 =\frac1{\sqrt{20}}=\frac1{2\sqrt5},
\]

and

\[
\begin{aligned}
 \left.\frac{d^2}{d\theta^2}\log\lambda(e^\theta)\right|_{\theta=0}
 &=\frac1{\sqrt{20}}-\frac6{20^{3/2}}\\
 &=\frac7{20\sqrt5}.
\end{aligned}
\]

The derivatives of \(\log C(e^\theta)\) contribute bounded terms. Since \(S_n=n+T_n\), equations (3) and (4) follow.

For every \(\varepsilon>0\), Chebyshev's inequality and (3)–(4) imply

\[
 \mathbb P\left(\left|S_n/n-(1+1/(2\sqrt5))\right|>\varepsilon
       \;\middle|\;H_n\right)\longrightarrow0.
\]

For a fixed quantile order \(\alpha\in(0,1)\), this convergence places the conditional distribution function below \(\alpha\) at \(n(c-\varepsilon)\) and above \(\alpha\) at \(n(c+\varepsilon)\), for all sufficiently large \(n\), where \(c=1+1/(2\sqrt5)\). Hence the lower \(\alpha\)-quantile, divided by \(n\), tends to \(c\); the same argument applies to the usual alternative quantile conventions.

## 5. Independent checks

### Crossing probability from an unmarked connectivity transfer matrix

There are two surviving reachability states at the current column: both vertices are reachable from the left boundary (state A), or exactly one is reachable (state B). The two possible orientations of B have identical transition probabilities. The initial state is A because both left boundary vertices are possible starting points.

From A, both vertices of the next column are reachable if both horizontal edges are open, or exactly one horizontal edge is open and the next rung is open. At \(p=1/2\) this has probability \(1/4+(1/2)(1/2)=1/2\). Exactly one next vertex is reachable with probability \((1/2)(1/2)=1/4\).

From B, the horizontal edge on the reachable rail must be open, an event of probability \(1/2\). If it and the next rung are open, the next state is A; if it is open and the next rung is closed, the next state is B. Each case has probability \(1/4\). The other horizontal edge does not change these probabilities. The missing row mass is failure.

Thus

\[
 M=\begin{pmatrix}1/2&1/4\\1/4&1/4\end{pmatrix},\qquad
 \mathbb P(H_n)=(1,0)M^n\binom11.
\]

Reachability here can be taken to mean reachability by a horizontally monotone path, which is equivalent for crossings by Section 1. Allowing the last rung in this transfer description does not change survival: a rung can make an additional endpoint reachable but cannot create survival without a reachable endpoint already present.

The trace of \(M\) is \(3/4\) and its determinant is \(1/16\). Its characteristic equation is therefore \(x^2-(3/4)x+1/16=0\), with roots exactly \(\lambda,\mu\). Cayley–Hamilton gives the recurrence

\[
 \mathbb P(H_n)=\frac34\mathbb P(H_{n-1})-\frac1{16}\mathbb P(H_{n-2}),
\]

with initial values \(1,3/4\). This independently gives (2).

### Direct enumeration for one, two, and three horizontal cuts

For \(n=1\), the crossing occurs if at least one horizontal edge is open. Its probability is \(3/4\) and its length is 1. Thus \(P_1(t)=3/4\).

For \(n=2\), assign weight \(1/16\) to each sequence of two prescribed nonempty cut types \(double, top only, bottom only\). There is one sequence with no single cuts, four with one single cut, and two with two equal single orientations. All seven contribute no rung. The two sequences with opposite single orientations require the single intervening rung to be open, with probability \(1/2\). Hence

\[
 P_2(t)=\frac{7+t}{16}.
\]

For \(n=3\), each sequence of three prescribed nonempty cut types has horizontal probability \(1/64\). The following weights sum the probabilities of the needed rungs, in units of \(1/64\):

| Number of single cuts | Weight with 0 changes | Weight with 1 change | Weight with 2 changes |
|---|---:|---:|---:|
| 0 | 1 | 0 | 0 |
| 1 | 6 | 0 | 0 |
| 2 | 6 | \(7/2\) | 0 |
| 3 | 2 | 2 | \(1/2\) |

For the row with two single cuts, there are three choices of their positions and two equal-orientation choices each, giving 6. For opposite orientations, the two choices of consecutive positions each give \(2(1/2)=1\), while the separated position pair gives \(2(1-(1/2)^2)=3/2\). This totals \(7/2\). For the final row, the eight binary orientation sequences have zero, one, or two changes with multiplicities 2, 4, and 2. Their required rung probabilities are 1, \(1/2\), and \(1/4\), respectively. This proves

\[
 P_3(t)=\frac{30+11t+t^2}{128}.
\]

For an explicit algebraic check independent of the preceding classification, multiply (1) by its denominator. The denominator is

\[
 1-\frac{7+t}{8}z+\frac{7+t}{32}z^2-\frac1{64}z^3.
\]

The coefficient of \(z\), using \(P_0=1\), gives \(P_1=(7+t)/8-(1+t)/8=3/4\). The coefficient of \(z^2\) gives

\[
 P_2=\frac{7+t}{8}\frac34-\frac{7+t}{32}=\frac{7+t}{16}.
\]

The coefficient of \(z^3\) gives

\[
 P_3=\frac{(7+t)^2-3(7+t)+2}{128}
     =\frac{30+11t+t^2}{128}.
\]

Thus the direct classification and the generating function agree. In particular,

\[
 \mathbb P(H_2)=\frac12,\quad
 \mathbb E[S_2\mid H_2]=\frac{17}{8},\quad
 \mathbb P(H_3)=\frac{21}{64},\quad
 \mathbb E[S_3\mid H_3]=\frac{139}{42}.
\]

### Independent differentiation of the leading root

Write \(w=(5+t)/8\), so that \(\lambda(t)^2-w\lambda(t)+1/16=0\). Differentiating this quadratic gives

\[
 (2\lambda-w)\lambda'=\lambda/8.
\]

At \(t=1\), \(2\lambda-w=\sqrt5/4\). Therefore \(\lambda'/\lambda=1/(2\sqrt5)\), independently checking the coefficient in (3) from the quadratic rather than differentiating the explicit radical.

Differentiating again gives

\[
 (2\lambda-w)\lambda''=\lambda'/4-2(\lambda')^2.
\]

Put \(c=\lambda'/\lambda=1/(2\sqrt5)\) at \(t=1\). The preceding equation implies

\[
 \frac{\lambda''}{\lambda}-c^2
 =\frac{c/4-2\lambda c^2}{\sqrt5/4}-c^2
 =-\frac3{20\sqrt5}.
\]

Adding \(c\), as required by the substitution \(t=e^\theta\), yields \(7/(20\sqrt5)\), checking (4).

### Why the path reduction does not extend to three rows

On the three-row graph with columns \(0,1,2,3\) and rows \(0,1,2\), declare open exactly the seven edges of the path

\[
 (0,0),\ (1,0),\ (2,0),\ (2,1),\ (1,1),\ (1,2),\ (2,2),\ (3,2).
\]

Declare every other edge closed. The only nontrivial open component is this simple path, and its only left and right boundary vertices are its two endpoints. Hence it is the unique open left-right crossing and has length 7. It traverses the cut between columns 1 and 2 three times. There is no horizontally monotone open crossing. All configurations of this finite graph, including this one, have positive probability at \(p=1/2\).

Thus the two-edge cut argument is specific to two rows. Already at three rows, the forced-rail description omits valid crossings and cannot be used to compute shortest crossings without additional state.
