# Parameter stability and delayed concentration at transcendental parameters

For $0<\lambda<1$, let
\[
 R_\lambda=(1-\lambda)^{-1},\qquad
 s_\sigma(\lambda)=\sum_{j=0}^{n-1}\sigma_j\lambda^j,\qquad
 r_n(\lambda)=\frac{\lambda^n}{1-\lambda}.
\]
The signs are independent and fair. Let $\mu_n^\lambda$ be the law of
the first $n$ signs plus an independent uniform tail on
$[-r_n(\lambda),r_n(\lambda)]$. Thus
\[
 \mu_n^\lambda=2^{-n}\sum_{\sigma\in\{-1,1\}^n}
 U_{[s_\sigma(\lambda)-r_n(\lambda),\,
        s_\sigma(\lambda)+r_n(\lambda)]},
 \qquad
 A_n^\lambda(\delta)=\sup_{|E|\leq\delta}\mu_n^\lambda(E).
\]
Here $U_I$ is uniform probability on a nondegenerate interval $I$,
and the supremum is over Lebesgue measurable sets. The empty prefix at
$n=0$ is included. Define total variation by
\[
 d_{\rm TV}(\rho,\tau)=\sup_E|\rho(E)-\tau(E)|.
\]

**Stability proposition.** If $0<a\leq\lambda,\eta\leq b<1$, then
for every integer $n\geq0$ and every $\delta>0$,
\[
 \begin{split}
 d_{\rm TV}(\mu_n^\lambda,\mu_n^\eta)
 &\leq \min\{1,C_n(a,b)|\lambda-\eta|\},\\
 |A_n^\lambda(\delta)-A_n^\eta(\delta)|
 &\leq \min\{1,C_n(a,b)|\lambda-\eta|\},\\
 C_n(a,b)&=\frac{1-a}{(1-b)^2a^n}.
 \end{split}                                                     \tag{1}
\]
In particular, these cap functions are locally Lipschitz in the
parameter, including at parameters with exact prefix coincidences.

**Delayed-concentration theorem.** Fix $\delta_0>0$,
$\delta_0/4<\theta<1$, an integer $N\geq1$, $\delta_1>0$,
$0<\varepsilon<1$, and an integer $M>N$. There are an integer
$m\geq M$ and a nonempty open interval $J\subset(1/2,1)$ such that
every $\lambda\in J$ satisfies
\[
 A_n^\lambda(\delta_0)<\theta\quad(0\leq n\leq N),
 \qquad
 A_m^\lambda(\delta_1)>1-\varepsilon.                             \tag{2}
\]
The interval $J$ contains uncountably many transcendental parameters.
Moreover, given any finite collection of nonzero integer polynomials,
one can replace $J$ by a nonempty rational interval on which their
absolute values all have a common positive rational lower bound.

The late depth $m$ is existential. The theorem supplies an explicit
stability radius once that depth is supplied; it supplies no effective
upper bound for $m$. It asserts a finite concentration episode and
does not assert singularity at a transcendental parameter.

## 1. Uniform distributions on moving intervals

Let $I=[u,v]$, $I'=[u',v']$, with lengths $L,L'>0$. Since their
densities are constant, integrating their pointwise minimum gives
\[
 d_{\rm TV}(U_I,U_{I'})
 =1-\frac{|I\cap I'|}{\max(L,L')}.                               \tag{3}
\]
Indeed, for any two probability densities $f,g$, their difference
has integral zero. Its positive integral and negative absolute integral
are equal, and each equals $1-\int\min(f,g)$. This common value is
the supremum defining total variation.

Suppose that each corresponding pair of endpoints differs by at most
$e\geq0$. Choose the longer of $I,I'$ as $K$, with the other
called $K'$. The portions of $K\setminus K'$ to the left and right
have lengths at most $e$ each. This remains true for disjoint intervals:
if $K$ lies entirely to the left, its length is at most the difference
of the left endpoints, and the analogous assertion holds on the right.
Consequently (3) gives
\[
 d_{\rm TV}(U_I,U_{I'})
 =\frac{|K\setminus K'|}{|K|}
 \leq\min\left\{1,\frac{2e}{\max(L,L')}\right\}.                  \tag{4}
\]

## 2. The endpoint derivative bound

The two endpoints associated to a word $\sigma$ are
\[
 q_{\sigma,\pm}(t)=s_\sigma(t)\pm r_n(t).
\]
For $a\leq t\leq b$,
\[
 |q_{\sigma,\pm}'(t)|
 \leq\sum_{j=1}^{n-1}j b^{j-1}+r_n'(b)
 =\frac1{(1-b)^2}.                                               \tag{5}
\]
To verify both the inequality and the equality, use the positive series
$r_n(t)=\sum_{j=n}^\infty t^j$. Its derivative is the tail of the
positive series $\sum_{j\geq1}jt^{j-1}=(1-t)^{-2}$. Both the finite
sum and this tail increase with $t\in(0,1)$, and together they are
the full series at $b$. For $n=0$ and $n=1$, the finite sum is
empty and the same argument applies.

The mean value theorem now bounds corresponding endpoint differences
by $e=|\lambda-\eta|/(1-b)^2$. Also $r_n(t)$ increases with $t$,
so each word interval has length at least $2a^n/(1-a)$. Substitution
in (4) proves the first bound in (1) for each word distribution.
For any measurable $E$, the absolute difference between the two
mixture probabilities is at most the average of the absolute wordwise
differences. This proves the bound for $\mu_n$, retaining all word
multiplicities.

Finally, if $d=d_{\rm TV}(\mu_n^\lambda,\mu_n^\eta)$, then
$\mu_n^\lambda(E)\leq\mu_n^\eta(E)+d$ for every eligible $E$.
Taking suprema gives $A_n^\lambda(\delta)\leq A_n^\eta(\delta)+d$.
Interchanging the parameters proves the second bound in (1). No
maximizing set, endpoint ordering, or separation of prefix sums is needed.

## 3. The inherited singular controls

The following facts were established in full in
[the preceding proof](~/codex_op_1114r5/briefs/T075/PROOF.md).
For $k\geq2$, let $\lambda_k\in(1/2,1)$ solve
$\sum_{j=1}^k\lambda_k^j=1$. Then
\[
 0<2\lambda_k-1<2^{-k},\qquad \nu_{\lambda_k}\text{ is singular},    \tag{6}
\]
and, for every $1/2<\lambda<1$,
\[
 A_n^\lambda(\delta)
 \leq\min\left\{1,\frac{\delta(1-\lambda)}2+
       n\frac{(2\lambda-1)(1-\lambda)}\lambda\right\}
 \leq\min\{1,\delta/4+n(2\lambda-1)\}.                            \tag{7}
\]
For clarity, (7) follows by comparing $\mu_n^\lambda$ to uniform
probability on $[-R_\lambda,R_\lambda]$. One application of the
balanced two-branch Markov operator has total variation defect
$(2\lambda-1)(1-\lambda)/\lambda$. The operator contracts total
variation. Telescoping $n$ applications bounds the defect by $n$
times this quantity. The uniform probability of a set of length
$\delta$ is at most $\delta(1-\lambda)/2$, proving (7).

The singularity in (6) is the classical Pisot argument, with its root
location and nonzero Fourier factors proved in the linked proof.
It is an input here, rather than a new singularity claim.

We also need its following consequence, whose measure-theoretic step is
included. Coupling the true and uniform tails gives
\[
 \mu_n^{\lambda_k}\ \Longrightarrow\ \nu_{\lambda_k},\qquad
 |X-Z_n|\leq2R_{\lambda_k}\lambda_k^n.
\]
Given $0<q<1$, singularity and inner regularity give a compact null
set $F$ of $\nu_{\lambda_k}$-mass greater than $q$. There is a
bounded open set $G\supset F$ with $|G|<\delta_1$. The open-set
inequality for weak convergence gives
\[
 q<\nu_{\lambda_k}(G)
 \leq\liminf_n\mu_n^{\lambda_k}(G)
 \leq\liminf_n A_n^{\lambda_k}(\delta_1)\leq1.
\]
Letting $q\uparrow1$ proves
\[
 \lim_{n\to\infty}A_n^{\lambda_k}(\delta_1)=1.                     \tag{8}
\]

## 4. Transfer to an interval of parameters

Put
\[
 h_0=\theta-\delta_0/4>0,\qquad
 a=\tfrac12,\qquad b=\tfrac12+\frac{h_0}{2N}<1.
\]
Choose $k\geq2$ with $N2^{-k}<h_0$. Equation (6) then gives
$a<\lambda_k<b$. For every $a<\lambda<b$, (7) gives, simultaneously
for $0\leq n\leq N$,
\[
 A_n^\lambda(\delta_0)
 \leq\delta_0/4+n(2\lambda-1)<\theta.                              \tag{9}
\]
For $n=0$, strictness follows from $\delta_0/4<\theta$; for
$1\leq n\leq N$, it follows from $N(2\lambda-1)<h_0$.

By (8), choose an integer $m\geq M$ with
\[
 A_m^{\lambda_k}(\delta_1)>1-\varepsilon/2.
\]
Set
\[
 \rho=\min\left\{\frac{\lambda_k-a}{2},\,
                     \frac{b-\lambda_k}{2},\,
                     \frac{\varepsilon}{4C_m(a,b)}\right\}>0,
 \qquad J=(\lambda_k-\rho,\lambda_k+\rho).                        \tag{10}
\]
This interval lies in $(a,b)$. For $\lambda\in J$, (1) gives
\[
 A_m^\lambda(\delta_1)
 \geq A_m^{\lambda_k}(\delta_1)-C_m(a,b)|\lambda-\lambda_k|
 >1-\varepsilon/2-\varepsilon/4>1-\varepsilon.
\]
Together with (9), this proves (2). An open interval is uncountable,
whereas the algebraic numbers are countable: integer polynomials form a
countable set and each nonzero polynomial has finitely many real roots.
Removing them leaves uncountably many transcendental parameters in $J$.

## 5. Finite arithmetic exclusions

Let $P_1,\ldots,P_s$ be nonzero integer polynomials. The case $s=0$
needs no exclusions. Since their combined real root set is finite,
choose a rational $t\in J$ with $P_i(t)\ne0$ for all $i$. Write
$P_i(x)=\sum_j c_{ij}x^j$ and put
\[
 H_i=\sum_{j\geq1}j|c_{ij}|.
\]
For $x\in(0,1)$, $|P_i'(x)|\leq H_i$. Choose a positive rational
$r$ with $[t-r,t+r]\subset J$ and
$rH_i\leq|P_i(t)|/2$ whenever $H_i>0$. There is such an $r$
because there are only finitely many positive upper bounds to meet.
The mean value theorem gives, for every $x\in[t-r,t+r]$,
\[
 |P_i(x)|\geq |P_i(t)|-H_i r\geq |P_i(t)|/2.
\]
For constant polynomials this inequality also holds, since $H_i=0$.
Thus the common bound
\[
 \eta=\frac12\min_i|P_i(t)|>0
\]
is rational, and the rational interval $J'=(t-r,t+r)$ retains (2).
For example, one may take all nonzero polynomials of degree at most
$Q-1$ with coefficients in $\{-1,0,1\}$, for any prescribed integer
$Q\geq1$. Differences of distinct sign prefixes of length at most
$Q$ are twice such polynomial values. Hence there are no exact prefix
overlaps at those depths anywhere in $J'$, with separation at least
$2\eta$. The value $\eta$ is selected by the construction; it is
not an arbitrarily prescribed separation threshold.

## 6. The quantifiers in the obstruction

Let
\[
 \mathcal T=\{\lambda\in(1/2,1):\lambda\text{ is transcendental and }
 A_n^\lambda(\delta_0)<\theta\ (0\leq n\leq N)\}.
\]
For every $\delta_1>0$ and every integer $M>N$, the theorem gives
\[
 \sup_{\lambda\in\mathcal T}\ \sup_{m\geq M}
       A_m^\lambda(\delta_1)=1.                                  \tag{11}
\]
The upper bound is probability normalization. For every
$\varepsilon>0$, (2) supplies a transcendental $\lambda\in\mathcal T$
and an $m\geq M$ with cap greater than $1-\varepsilon$, proving
the reverse bound. The same conclusion holds after imposing any fixed
finite list of nonvanishing integer-polynomial conditions.

Equation (11) rules out a uniform all-depth cap bound on this entire
class from its finite initial caps and qualitative transcendence alone.
The parameter may depend on $\delta_1,\varepsilon,M$. No fixed
transcendental parameter is shown to concentrate at arbitrarily small
lengths. Such a parameter, if singular, would contradict T075; the
theorem does not construct one. A criterion that merely concludes
absolute continuity within the transcendental class is also not
contradicted by a finite episode of concentration.
