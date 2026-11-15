# A light-traffic expansion at a coordinate axis

Observe queues immediately before transmission attempts, with independent arrivals
added between consecutive observations. Thus

\[
 Q_i(t+1)=Q_i(t)-D_i(t)+A_i(t).
\]

All arrivals are independent across users and slots and independent of attempt
coins. Every transmission probability below is strictly between zero and one.

## 1. Statement

There are \(m+1\) users. Label the tagged user 0, and fix its transmission
probability \(p_0\). Write \(c=1-p_0\). The other users have probabilities
\(p_1,\ldots,p_m\) and Bernoulli arrival rates
\(\lambda_i=\varepsilon a_i\), where all \(a_i>0\) are fixed.

In the auxiliary system, user 0 attempts with probability \(p_0\) even when
its real queue is empty, sending a dummy packet in that case. The light queues
then evolve autonomously. For all sufficiently small positive \(\varepsilon\),
they have a unique stationary law \(\pi_\varepsilon\). Define

\[
 \mu(\varepsilon)=p_0\,\mathbb E_{\pi_\varepsilon}
       \prod_{i=1}^m(1-p_i\mathbf1_{\{Q_i>0\}}).
 \tag{1}
\]

For each such \(\varepsilon\), the original system is positive recurrent if
\(0<\lambda_0<\mu(\varepsilon)\), and is transient if
\(\mu(\varepsilon)<\lambda_0<1\). Consequently its stability threshold in the
tagged coordinate, defined as the supremum of stable \(\lambda_0\), equals
\(\mu(\varepsilon)\). No assertion is made at equality.

The expansion of this threshold is

\[
\boxed{
\begin{aligned}
 \mu(\varepsilon)=p_0\bigg[1
 &-\frac{\varepsilon}{c}\sum_i a_i\\
 &-\frac{\varepsilon^2}{c^2}
 \sum_{i<j}a_i a_j
 \frac{p_i+p_j-cp_i p_j}{p_i+p_j-2p_i p_j}
 \bigg]+O(\varepsilon^3).
\end{aligned}}
\tag{2}
\]

The implied constant depends on the fixed parameters, not on \(\varepsilon\).
For four users with all probabilities \(1/2\), and with the three light
arrival rates equal to \(\varepsilon\), the following explicit estimate holds:

\[
 \left|\mu(\varepsilon)-
  \left(\frac12-3\varepsilon-\frac{21}{2}\varepsilon^2\right)\right|
 \le400000\varepsilon^3,
 \qquad 0<\varepsilon\le\frac1{128}.
 \tag{3}
\]

## 2. A stationary tail estimate

Let \(W=\sum_{i=1}^m Q_i\) in the auxiliary system. If its nonempty set is
\(S\ne\varnothing\), a light packet departs with probability

\[
 d(S)=c\sum_{i\in S}p_i
                 \prod_{j\in S\setminus\{i\}}(1-p_j).
\]

Set \(\delta=\min_{S\ne\varnothing}d(S)>0\). There is at most one light
departure per slot. The generating function of the total arrivals is

\[
 G_\varepsilon(R)=\prod_i(1-\varepsilon a_i+\varepsilon a_iR).
\]

Choose \(\eta>0\) so small that, with
\(G_* =\prod_i(1+a_i\eta)\),
\(\beta_*=(1-\delta/2)G_*<1\). Restrict \(\varepsilon\) so that all arrival
probabilities are less than one and \(R=\eta/\varepsilon\ge2\).
For \(W>0\), independence of current arrivals and attempts gives

\[
 \mathbb E[R^{W(t+1)}\mid Q(t)]
 =G_\varepsilon(R)R^W(1-d(S)+d(S)/R)
 \le\beta_*R^W.
\]

At \(W=0\), the conditional expectation is \(G_\varepsilon(R)\). More
precisely, using \(\beta=G_\varepsilon(R)(1-\delta+\delta/R)\), the bound for
all states is

\[
 \mathbb E[R^{W(t+1)}\mid Q(t)]
 \le\beta R^W+\delta G_\varepsilon(R)(1-1/R)\mathbf1_{\{W=0\}}
 \le\beta_*R^W+\delta G_*.
\]

Starting empty and iterating gives

\[
 \sup_t\mathbb E R^{W(t)}
 \le M:=\max\left\{1,\frac{\delta G_*}{1-\beta_*}\right\}<\infty.
 \tag{4}
\]

Since sets with bounded \(W\) are finite, the distributions are uniformly
tight. Their Cesàro averages have a subsequence converging in total variation
to a probability law. If \(P\) is the transition matrix, a Cesàro average
\(\nu_T\) satisfies \(\|\nu_TP-\nu_T\|_1\le2/T\), so this limit is invariant.
The light chain is irreducible: no-arrival slots and isolated successful
attempts can empty any state, and arrivals during no-attempt slots can build
any state. Thus it is positive recurrent and has a unique stationary law.
Fatou's lemma applied to (4) gives

\[
 \mathbb E_{\pi_\varepsilon}R^W\le M,
 \qquad
 \pi_\varepsilon(W\ge k)\le M(\varepsilon/\eta)^k.
 \tag{5}
\]

In particular \(\mathbb P(W\ge k)=O(\varepsilon^k)\) for each fixed \(k\).
This proves the error estimates used below without assuming analytic
dependence of the infinite-state stationary distribution.

## 3. Pair probabilities through second order

Put \(b_i=\mathbb P(Q_i>0)\),
\(b_{ij}=\mathbb P(Q_i>0,Q_j>0)\), and
\(x_i=\pi_\varepsilon(Q=e_i)\). Finite stationary queue means, supplied by
(5), justify arrival-departure balance. For a light user,

\[
 \varepsilon a_i
 =cp_i\mathbb E\left[
 \mathbf1_{\{Q_i>0\}}
 \prod_{j\ne i}(1-p_j\mathbf1_{\{Q_j>0\}})\right]
 =cp_i b_i+O(\varepsilon^2).
\]

The error is supported on \(W\ge2\). Therefore

\[
 b_i=\frac{a_i}{cp_i}\varepsilon+O(\varepsilon^2),
 \qquad
 x_i=\frac{a_i}{cp_i}\varepsilon+O(\varepsilon^2),
 \qquad
 \pi_\varepsilon(Q=0)=1+O(\varepsilon).
 \tag{6}
\]

Fix distinct \(i,j\), and write \(x_{ij}=\pi_\varepsilon(Q=e_i+e_j)\).
At zero arrival rate the probability of leaving this state in one slot is

\[
 L_{ij}=c\{p_i(1-p_j)+p_j(1-p_i)\}
       =c(p_i+p_j-2p_i p_j)>0.
\]

Its stationary equation, retaining terms through order two, is

\[
\begin{aligned}
 L_{ij}x_{ij}
 ={}&a_i a_j\varepsilon^2
 +(1-cp_i)a_j\varepsilon x_i
 +(1-cp_j)a_i\varepsilon x_j
 +O(\varepsilon^3).
\end{aligned}
\tag{7}
\]

Here are all the omitted sources. Another singleton requires two arrivals,
so its contribution is \(O(\varepsilon)O(\varepsilon^2)\). A different state
of total size two requires at least one arrival, giving
\(O(\varepsilon^2)O(\varepsilon)\). States of total size at least three
have total stationary mass \(O(\varepsilon^3)\). Arrivals change the
diagonal transition probability by \(O(\varepsilon)\), multiplied by
\(x_{ij}=O(\varepsilon^2)\). Corrections to the three displayed transition
probabilities have the same order after multiplication by their source
probabilities. This accounts for every state.

Substituting (6) into (7), and observing that
\(b_{ij}-x_{ij}\le\mathbb P(W\ge3)\), gives

\[
\boxed{
 b_{ij}=
 \frac{a_i a_j(p_i+p_j-cp_i p_j)}
      {c^2p_i p_j(p_i+p_j-2p_i p_j)}
 \varepsilon^2+O(\varepsilon^3).}
\tag{8}
\]

In particular the leading pair coefficient exceeds the product of the
leading marginal coefficients. Their ratio is
\((p_i+p_j-cp_i p_j)/(p_i+p_j-2p_i p_j)>1\).

Summing light-user departure balances and using (5) for triple intersections
gives

\[
 \frac{\varepsilon}{c}\sum_i a_i
 =\sum_i p_i b_i-2\sum_{i<j}p_i p_jb_{ij}+O(\varepsilon^3).
\]

Expanding the product in (1) and eliminating the single-user terms yields

\[
 \frac{\mu(\varepsilon)}{p_0}
 =1-\frac{\varepsilon}{c}\sum_i a_i
     -\sum_{i<j}p_i p_jb_{ij}+O(\varepsilon^3).
\]

Equation (8) proves (2).

## 4. Connection to the original queues

Use independent primitive attempt and arrival coins for all users and slots.
In a stationary, two-sided version of the auxiliary light system, let
\(C_t\) indicate that user 0 attempts and all light users are silent. Its
mean is \(\mu\). The process of light states and marked slot outcomes is
stationary ergodic, since the light chain is irreducible positive recurrent
and its driving coins are independent across slots. The variables \(C_t\)
need not be independent across time or independent of future light states.

Suppose first that \(\lambda_0<\mu\), and let \(A_0(t)\) be independent
Bernoulli arrivals of mean \(\lambda_0\). Define

\[
 L_t=\sup_{n\ge0}\sum_{s=t-n}^{t-1}(A_0(s-1)-C_s),
 \qquad Y_t=L_t+A_0(t-1),
\]

with empty sum zero. The backward ergodic theorem says that the summands
have negative long-run mean, so this supremum is finite almost surely.
Its recursion is

\[
 L_{t+1}=(L_t+A_0(t-1)-C_t)^+,
 \qquad Y_{t+1}=(Y_t-C_t)^++A_0(t).
\]

Together with the stationary light environment, this constructs a stationary
auxiliary system with a finite real tagged queue and dummy transmissions when
that queue is empty.

Couple the original system, started empty, below this stationary system using
the same future arrivals and attempt coins. Coordinatewise order is preserved.
To check it, if a coordinate is strictly smaller, a single possible departure
cannot reverse its order. If equal and positive, an auxiliary success entails
an original success: every other original active queue is also active in the
auxiliary system, and the auxiliary system may have the additional tagged
dummy attempt. If equal and zero, both real departure counts are zero. Equal
arrivals preserve the order after service.

The stationary auxiliary vector is finite almost surely, so this coupling
makes the distributions of the original chain uniformly tight. The Cesàro
argument from Section 2 supplies an invariant probability distribution for
the original chain. It is irreducible by the same emptying and filling paths,
so it is positive recurrent.

Now suppose \(\lambda_0>\mu\). Start the light environment in its stationary
law and put

\[
 S_n=\sum_{t=0}^{n-1}(A_0(t)-C_t),\qquad S_0=0.
\]

The ergodic theorem gives \(S_n/n\to\lambda_0-\mu>0\). Hence
\(\inf_n S_n\) is finite almost surely. There is a deterministic integer
\(K\ge1\) such that the event
\(E_K=\{K+S_n\ge1\text{ for every }n\ge0\}\) has positive probability.
Indeed these events increase to an event of probability one as \(K\to\infty\).

Start the original tagged queue at \(K\), using the same light initial state
and coins as above. On \(E_K\), its queue never empties. Inductively it
therefore generates exactly the attempts used by the auxiliary environment,
and its size is \(K+S_n\to\infty\). Averaging over the countable stationary
light initial states shows that at least one deterministic initial light
state has positive probability of this escape. From that deterministic full
state there is positive probability never to hit the all-empty state. An
irreducible recurrent chain hits every state almost surely. The original
chain is therefore transient. This proves the threshold assertions.

## 5. Explicit error bound for four half-probability users

Here \(m=3\), all \(p_i=p_0=1/2\), and all \(a_i=1\). With \(k\) nonempty
light queues the light-departure probability is \(k/2^{k+1}\). For
\(k=1,2,3\) these are \(1/4,1/4,3/16\), so \(\delta=3/16\).

For \(0<\varepsilon\le1/128\), take \(R=1/(32\varepsilon)\ge4\). Then

\[
 G_\varepsilon(R)\le G_*=(33/32)^3,
 \quad 1-\delta+\delta/R\le55/64,
 \quad \beta_*=(55/64)(33/32)^3<1.
\]

The moment bound used in (4) is at most

\[
 \max\{1,\delta G_* /(1-\beta_*)\}
 =\frac{431244}{120617}<4.
\]

Consequently

\[
 T_2:=\mathbb P(W\ge2)\le4096\varepsilon^2,
 \qquad T_3:=\mathbb P(W\ge3)\le131072\varepsilon^3.
 \tag{9}
\]

Total arrival-departure balance also gives
\(3\varepsilon=\mathbb E d(S)\ge(3/16)\mathbb P(W>0)\), so
\(\mathbb P(W>0)\le16\varepsilon\).

Write \(b_{123}=\mathbb P(Q_1Q_2Q_3>0)\). Exact individual balance is

\[
 \varepsilon=\tfrac14b_i-\tfrac18(b_{ij}+b_{ik})
                        +\tfrac1{16}b_{123}.
\]

It implies \(0\le b_i-4\varepsilon\le T_2\). Thus, with
\(x_i=\pi(Q=e_i)\),

\[
 |x_i-4\varepsilon|\le8192\varepsilon^2,
 \qquad x_i\le16\varepsilon.
 \tag{10}
\]

For fixed distinct \(i,j\), let \(b=e_i+e_j\), let \(k\) be the other light
user, and denote a one-step transition probability by \(P_{qb}\). Direct
service-then-arrival enumeration gives

\[
\begin{aligned}
 P_{0b}&=\varepsilon^2(1-\varepsilon),\\
 P_{e_i b}=P_{e_j b}
 &=\tfrac34\varepsilon(1-\varepsilon)^2
   +\tfrac14\varepsilon^2(1-\varepsilon),\\
 P_{e_k b}&=\tfrac14\varepsilon^2(1-\varepsilon).
\end{aligned}
\]

In particular
\(|P_{e_i b}-(3/4)\varepsilon|\le2\varepsilon^2\).
The no-arrival diagonal is \(3/4\), so
\(|P_{bb}-3/4|\le3\varepsilon\). For any other state \(q\) with
\(W(q)=2\), \(P_{qb}\le3\varepsilon\): at least one arrival is required.

Use the stationary equation for \(b\) in the form

\[
 \tfrac14\pi(b)=
 \sum_{q\ne b}\pi(q)P_{qb}+\pi(b)(P_{bb}-3/4).
\]

The leading incoming term is
\(\varepsilon^2+2(4\varepsilon)(3\varepsilon/4)=7\varepsilon^2\).
The absolute errors are bounded as follows, with every entry multiplying
\(\varepsilon^3\):

| Source | Error constant | Reason |
|---|---:|---|
| Empty state | 17 | \(\mathbb P(W>0)\le16\varepsilon\), plus the factor \(1-\varepsilon\) |
| Singletons \(e_i,e_j\) | 12352 | \(2[(3/4)8192+16\cdot2]\), by (10) |
| Singleton \(e_k\) | 4 | \((16\varepsilon)(\varepsilon^2/4)\) |
| Other states of total size two | 12288 | \(3\varepsilon T_2\) |
| States of total size at least three | 131072 | \(T_3\) |
| Diagonal correction | 12288 | \(3\varepsilon\pi(b)\le3\varepsilon T_2\) |
| Total | 168021 | Sum of the preceding six entries |

Dividing by \(1/4\) yields
\(|\pi(b)-28\varepsilon^2|\le672084\varepsilon^3\). Since
\(0\le b_{ij}-\pi(b)\le T_3\),

\[
 |b_{ij}-28\varepsilon^2|\le803156\varepsilon^3.
 \tag{11}
\]

Summing the exact individual balances, then expanding (1), gives the exact
identity

\[
 \mu=\tfrac12-3\varepsilon
       -\tfrac18(b_{12}+b_{13}+b_{23})+\tfrac18 b_{123}.
\]

By (9) and (11), the absolute remainder after the quadratic term is at most

\[
 \frac{3\cdot803156+131072}{8}\varepsilon^3
 =\frac{635135}{2}\varepsilon^3
 <400000\varepsilon^3.
\]

This proves (3).

## 6. Independence comparison and a concrete unstable vector

Define the local independent-queue closure by busy fractions \(r_i\) solving

\[
 \varepsilon a_i=cp_i r_i\prod_{j\ne i}(1-p_jr_j),
 \qquad \widehat\mu=p_0\prod_i(1-p_ir_i).
\]

At \(\varepsilon=0,r=0\), the Jacobian of the first equations with respect
to \(r\) is the invertible diagonal matrix with entries \(cp_i\). The
implicit function theorem supplies the unique local branch, with
\(r_i=a_i\varepsilon/(cp_i)+O(\varepsilon^2)\). Summing the defining
equations and expanding the products gives

\[
 \widehat\mu=p_0\left[1-\frac{\varepsilon}{c}\sum_i a_i
       -\frac{\varepsilon^2}{c^2}\sum_{i<j}a_i a_j\right]
       +O(\varepsilon^3).
\]

Subtracting (2),

\[
 \widehat\mu-\mu
 =\frac{p_0(1+p_0)}{c^2}
 \sum_{i<j}\frac{a_i a_jp_ip_j}{p_i+p_j-2p_ip_j}
 \varepsilon^2+O(\varepsilon^3).
 \tag{12}
\]

For at least two light users the leading coefficient is strictly positive.
For four half-probability users the two quadratic coefficients are
\(-6\) and \(-21/2\), with gap \((9/2)\varepsilon^2\).

Here is a finite rational certificate. Set

\[
 \varepsilon=10^{-6},\qquad
 (\lambda_1,\lambda_2,\lambda_3,\lambda_0)
 =\left(\varepsilon,\varepsilon,\varepsilon,
        \tfrac12-3\varepsilon-8\varepsilon^2\right).
 \tag{13}
\]

By (3),

\[
 0.4999969999891\le\mu\le0.4999969999899
 <\lambda_0=0.499996999992.
\]

All displayed decimal endpoints are exact terminating decimals. The gap
between \(\lambda_0\) and the upper endpoint is \(21/10^{13}>0\).
Section 4 proves that this original four-user chain is transient.

For clarity, define the downward independent-queue region as the set of
vectors strictly coordinatewise below a vector

\[
 \sigma_i=\rho_i p_i\prod_{j\ne i}(1-\rho_jp_j),
 \qquad 0\le\rho_i\le1,\quad \max_i\rho_i=1.
\]

The vector (13) lies in this region. An explicit witness is
\(x=2\varepsilon+9\varepsilon^2\), \(\rho_0=1\), and
\(\rho_1=\rho_2=\rho_3=2x\). Its coordinates are

\[
 \sigma_i=\tfrac12x(1-x)^2\quad(i=1,2,3),
 \qquad \sigma_0=\tfrac12(1-x)^3.
\]

For \(\varepsilon=10^{-6}\), exact subtraction gives positive slacks

\[
 \sigma_i-\varepsilon
 =\frac{999935999946000486000729}
        {2000000000000000000000000000000000000}>0,
\]

\[
 \sigma_0-\lambda_0
 =\frac{1000100000134999513999271}
        {2000000000000000000000000000000000000}>0.
\]

Thus the independent-queue region is not an inner bound at these parameters.
This does not determine the whole stability region.

## 7. Independent finite calculation

The accompanying `verify.py` enumerates all attempt masks and all Bernoulli
arrival masks on the finite state set \(\{q:\sum q_i\le2\}\). It computes
stationary coefficients through degree two by rational linear algebra, using
two overflow rules: send an overflowing transition to zero, or send it to
its source state. These are checks of coefficients, not finite-buffer
stability tests.

The two rules cannot affect the original coefficients through degree two:
a state of total size \(w\le2\) has mass \(O(\varepsilon^w)\) by (5), and
overflow requires at least \(3-w\) arrivals, of probability
\(O(\varepsilon^{3-w})\). The entire modification is therefore
\(O(\varepsilon^3)\). Incoming mass from original states of size at least
three is also \(O(\varepsilon^3)\). The zero-arrival finite chain empties
almost surely and has only the empty recurrent state, so its stationary
coefficient equations with normalization have a unique solution.

Both rules reproduce (2) for the half-probability example, the quarter-
probability example, an asymmetric four-user example, and the two-user
linear-threshold sanity case. The stored rational output also checks all
constants and inequalities in Sections 5 and 6.
