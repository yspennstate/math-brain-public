# Density of the phase in the Zigzag Conjecture

All logarithms without a subscript are natural. A finite change to a set of positive integers has no effect on any density below.

## Statement

For real x sufficiently large, put

\[
 f(x)=2\log_2x-2\log_2\log_2x+2\log_2(e/2)+1,
 \qquad r=\sqrt2.
\]

For fixed 0<a<b<1 let

\[
 A_{a,b}=\{n:\{f(n)\}\in[a,b]\},\qquad d=b-a.
\]

Here braces denote fractional part. Then

\[
 \underline{\mathrm{dens}}(A_{a,b})
 =\frac{r^d-1}{r-1},\qquad
 \overline{\mathrm{dens}}(A_{a,b})
 =\frac{r(1-r^{-d})}{r-1}.                 \tag{1}
\]

Its logarithmic density exists and is d:

\[
 \lim_{N\to\infty}\frac1{\log N}
 \sum_{\substack{n\le N\\n\in A_{a,b}}}\frac1n=d. \tag{2}
\]

For integers n sufficiently large define

\[
 k(n)=\lfloor f(n)\rfloor,\quad
 \mu(n)=\binom n{k(n)}2^{-\binom{k(n)}2},\quad
 \theta(n)=\frac{\log\mu(n)}{\log n},\quad
 \lambda(n)=\frac12\max(\theta(n),1-\theta(n)).
\]

For 1/4<beta<1/2, the set B_beta={n:lambda(n)<=beta} has the densities in (1) with d=4 beta-1, and logarithmic density 4 beta-1. In particular, for beta=3/8 these densities are

\[
 \underline{\mathrm{dens}}(B_{3/8})=\frac1{1+2^{1/4}},
 \qquad
 \overline{\mathrm{dens}}(B_{3/8})=\frac{2^{1/4}}{1+2^{1/4}},
 \qquad \mathrm{logdens}(B_{3/8})=\frac12.       \tag{3}
\]

These are unconditional deterministic statements about explicit functions of n. A consequence for the chromatic number, conditional on the Zigzag Conjecture, is given at the end.

## Proof of the phase densities

Let ell=log 2 and c=log ell+1. Rewriting f gives

\[
 f(x)=\frac2\ell(\log x-\log\log x+c)-1,
 \qquad
 f'(x)=\frac2{\ell x}\left(1-\frac1{\log x}\right). \tag{4}
\]

Thus f is strictly increasing for x>e and tends to infinity. Write X(t) for its inverse on a sufficiently far out half-line. By differentiating f(X(t))=t,

\[
 \frac{d}{dt}\log X(t)
 =\frac{\ell/2}{1-1/\log X(t)}
 \longrightarrow\ell/2=\log r.               \tag{5}
\]

Integration over an interval of bounded length shows that for every fixed H,

\[
 \frac{X(t+s)}{X(t)}=r^s(1+o(1))
 \quad\hbox{uniformly for } |s|\le H.          \tag{6}
\]

Uniformity follows directly because the supremum of the difference between the derivative in (5) and log r on [t-H,t+H] tends to zero. Also, for all sufficiently large t that derivative is at least log r. Consequently, if j<=m are sufficiently large integers,

\[
 X(j)/X(m)\le r^{j-m}.                       \tag{7}
\]

One complete phase band in cycle j is the real interval [X(j+a),X(j+b)]. The number of integers in it differs from its length by at most two. There are O(log N) cycles below N, by (4), so all such rounding errors total O(log N)=o(N). The choice of closed endpoints also changes at most O(log N) terms.

Put Delta=r^b-r^a. The contribution of complete cycles preceding cycle m satisfies

\[
 \frac1{X(m)}\sum_{j<m}
       (X(j+b)-X(j+a))
 \longrightarrow \sum_{l=1}^{\infty}r^{-l}\Delta
 =\frac\Delta{r-1}=:C.                       \tag{8}
\]

Here and below an arbitrary fixed initial segment is omitted. To justify the infinite-sum limit, fix K and first use (6) for j=m-l with 1<=l<=K. For the remaining indices, (6) bounds X(j+b) by a fixed multiple of X(j) for every sufficiently large j. Equation (7) then bounds the remaining normalized sum by a constant times sum_{l>K} r^{-l}. The finitely many earlier terms divided by X(m) vanish. Letting K tend to infinity proves (8), including its error term.

For a general large integer N, write f(N)=m+u with m integer and 0<=u<1. The portion of the current cycle that has been counted is zero if u<a, has length X(m+u)-X(m+a) if a<=u<=b, and has length X(m+b)-X(m+a) if u>b. Equations (6)–(8) and the integer rounding estimate give

\[
 \frac{|A_{a,b}\cap[1,N]|}{N}=D(u)+o(1),       \tag{9}
\]

uniformly in u, where

\[
 D(u)=r^{-u}\begin{cases}
 C,&0\le u\le a,\\
 C+r^u-r^a,&a\le u\le b,\\
 C+\Delta,&b\le u\le1.
 \end{cases}                                \tag{10}
\]

The formulas match at a and b; they also give D(0)=D(1). On [0,a], D is decreasing. On [a,b],

\[
 D(u)=1+(C-r^a)r^{-u},\qquad
 C-r^a=\frac{r^b-r^{a+1}}{r-1}<0,
\]

so D is increasing. On [b,1], D is decreasing. Therefore its minimum is D(a) and its maximum is D(b). Substitution gives

\[
 D(a)=\frac{r^{b-a}-1}{r-1},\qquad
 D(b)=\frac{r(1-r^{a-b})}{r-1}.              \tag{11}
\]

Both extrema are attained as subsequential limits in (9). Indeed choose an integer N_m nearest to X(m+a), or to X(m+b). Its distance from that real number is bounded; by (4), f(N_m)-(m+a), or f(N_m)-(m+b), tends to zero. Thus its phase tends to a or b. This proves (1).

For logarithmic density compare the sum of 1/n in a band to the integral of dx/x over that band. For a band with left endpoint U tending to infinity, the error is O(1/U), including its two boundary terms: this follows by comparing 1/n on each whole unit interval with the integral of the decreasing function 1/x. The left endpoints X(j+a) grow at least geometrically by (7), so the sum of these errors over all cycles is bounded. By (6), one complete band contributes

\[
 \int_{X(j+a)}^{X(j+b)}\frac{dx}{x}
 =\log\frac{X(j+b)}{X(j+a)}\longrightarrow d\log r.
\]

Averaging these convergent contributions over the cycles through m gives m d log r+o(m). The unfinished cycle contributes O(1), by (6). Finally, (4) gives log N=m log r+o(m) when f(N)=m+u. Dividing proves (2).

## Independent derivation of theta's phase approximation

Put L=log n, M=2/ell and t={f(n)}. Then 0<=t<1 and

\[
 k=M(L-\log L+c)-1-t=ML+O(\log L).          \tag{12}
\]

For k=O(L), writing the binomial coefficient as a product gives

\[
 \log\binom nk=kL-\log k!+O(k^2/n).          \tag{13}
\]

For completeness, the correction is sum_{i=0}^{k-1} log(1-i/n). For sufficiently large n all i/n<=1/2 and |log(1-i/n)|<=2i/n; summing proves the error in (13). Comparing the increasing function log x with its integral gives

\[
 \log k!=k\log k-k+O(\log k).               \tag{14}
\]

Indeed the sum of log j from j=1 to k lies between the integral of log x from 1 to k and that integral plus log k; the integral is k log k-k+1.

Combining (13) and (14),

\[
 \log\mu
 =k\left[L-\frac\ell2(k-1)-\log k+1\right]
       +O(\log k+k^2/n).                    \tag{15}
\]

Using c=log ell+1 and (12), the expression in brackets is exactly

\[
 \log(ML/k)+\frac\ell2t.                   \tag{16}
\]

Since k=ML+O(log L), the product k log(ML/k) is O(log L), and k ell t/2=tL+O(log L), uniformly for 0<=t<1. Hence

\[
 \log\mu=tL+O(\log L),\qquad
 \theta(n)=\{f(n)\}+O\left(\frac{\log\log n}{\log n}\right). \tag{17}
\]

No probabilistic approximation has been used in (17).

Let g(t)=max(t,1-t)/2. This function is Lipschitz with constant 1/2 on the real line. Thus lambda(n)=g({f(n)})+o(1). For beta strictly between 1/4 and 1/2 and any sufficiently small fixed epsilon>0, eventually

\[
 A_{1-2(\mathrm{beta}-\epsilon),\,2(\mathrm{beta}-\epsilon)}
 \subseteq B_{\mathrm{beta}}
 \subseteq
 A_{1-2(\mathrm{beta}+\epsilon),\,2(\mathrm{beta}+\epsilon)}. \tag{18}
\]

The lengths of these two bands are 4(beta-epsilon)-1 and 4(beta+epsilon)-1. Applying (1) to the inclusions and letting epsilon decrease to zero proves the asserted lower and upper densities of B_beta, because both expressions in (1) are continuous in d. Applying (2) and the same squeeze proves its logarithmic density. Setting beta=3/8 gives d=1/2. Factoring r-1=(sqrt(r)-1)(sqrt(r)+1) gives (3).

## Conditional consequence for chromatic concentration

The following input is conjectural: Conjecture 10 of Annika Heckel and Oliver Riordan, *How does the chromatic number of a random graph vary?*, [arXiv:2103.14014v3](https://arxiv.org/html/2103.14014), predicts intervals of length n^{lambda(n)+o(1)} containing chi(G(n,1/2)) with probability tending to one, and vanishing probability in any prescribed intervals of length n^{lambda(n)-epsilon}, for each fixed epsilon>0. Its definitions of theta and lambda agree with those above.

For a fixed 0<q<1 define a precise width by

\[
 W_q(n)=\min\{v-u:u,v\in\mathbb Z,\ u\le v,
       \ \Pr(u\le\chi(G(n,1/2))\le v)\ge q\}.
\]

The minimum exists since chi lies in [1,n]. Conditional on Conjecture 10,

\[
 \frac{\log(1+W_q(n))}{\log n}=\lambda(n)+o(1). \tag{19}
\]

For the upper bound, round the endpoints of the conjectured high-probability intervals outwards; this adds at most two to their length. They have probability at least q for sufficiently large n.

For the lower bound, fix epsilon>0. If infinitely many W_q(n) were at most n^{lambda(n)-epsilon}, enlarge their minimizing intervals to that real length, and choose arbitrary intervals of that length for other n. The resulting sequence would have probability at least q infinitely often, contrary to the conjecture. Thus eventually W_q(n)>n^{lambda(n)-epsilon}. This argument for every fixed epsilon, together with the upper bound and lambda(n)>=1/4, proves (19).

In fact, under that conjecture the set

\[
 \left\{n:\frac{\log(1+W_q(n))}{\log n}\le\mathrm{beta}\right\}
\]

has the same lower, upper and logarithmic densities as B_beta. To see this, squeeze it between B_{beta-epsilon} and B_{beta+epsilon} using (19), then use continuity of the density formulas as in (18).

For beta=3/8, its positive lower density is 1/(1+2^{1/4}). Every set of natural density one intersects it infinitely often: removing a density-zero set cannot remove a set of positive lower density. On those integers the exponent is at most 3/8. Therefore (19) is incompatible with an exponent tending to 1/2 along any set of natural density one.

This last conclusion is conditional. The deterministic density theorem does not prove any unconditional concentration or non-concentration bound for chi(G(n,1/2)).
