# Sampled workload drift at the obstructing states

There are two links of capacity one. Route 0 uses both links; route 1 uses
the first and route 2 the second. Independent Poisson arrivals have rates

\[
 (\nu_0,\nu_1,\nu_2)=(1/5,1/2,1/2).
\]

Every arriving file has size one. Fix \(\alpha>0\) and weights
\(\kappa_0,\kappa_1,\kappa_2>0\). Each route shares its aggregate allocation
equally among its files. Let \(W_i\) be its residual workload, and put

\[
 M=W_0+\max(W_1,W_2),\qquad
 a_i=\kappa_i^{1/\alpha},\quad a_*=\min(a_1,a_2),\quad
 b=(\kappa_1+\kappa_2)^{1/\alpha}.
\]

Thus \(M\) is the larger of the two link workloads. Both offered link loads
are \(7/10<1\).

For an integer \(N\ge2\), let \(\mathcal C_N\) consist of finite states
with exactly \(N\) through-route files, each with residual in
\([1-N^{-8},1]\), and at most \(N^3\) local files in total, each with
positive residual at most \(N^{-4}\). The local files may be on either or
both local routes. There are no other initial files. Write

\[
 d(T)=-\frac45T+\mathbb E\max(P_1(T),P_2(T)),                 \tag{1}
\]

where \(P_1,P_2\) are independent rate-\(1/2\) Poisson processes, and define

\[
 \varepsilon_N(T)=
 \frac{b}{a_*N}+\frac{a_0}{a_*N^3}
 +\frac{T(a_0/5+b)}{a_*N^4}
 +\frac{bT^2}{a_0N}.                                      \tag{2}
\]

**Theorem.** If \(T>0\) and \(T<N(1-N^{-8})\), then every
\(x\in\mathcal C_N\) satisfies

\[
 d(T)-N^{-1}\ \le\
 \mathbb E_x[M(X(T))-M(x)]
 \ \le\ d(T)+\varepsilon_N(T).                             \tag{3}
\]

In particular, for each fixed \(T\), the expected increment converges to
\(d(T)\) uniformly over \(\mathcal C_N\). Moreover,

\[
 d(T)=-\frac3{10}T+\frac12\mathbb E|P_1(T)-P_2(T)|
 \le-\frac3{10}T+\frac12\sqrt T.                           \tag{4}
\]

It follows that for every fixed \(T>25/9\) the expected increment is
strictly negative for all sufficiently large \(N\), uniformly over
\(\mathcal C_N\). At \(T=4\), its limiting value is at most \(-1/5\).
For equal weights and \(\alpha=1\), every \(N\ge200\) already satisfies

\[
 \sup_{x\in\mathcal C_N}\mathbb E_x[M(X(4))-M(x)]
 \le -0.0299998695 < -0.029.                               \tag{5}
\]

The constants in (2) are deliberately not optimized. The theorem concerns
this specified family of initial states; it makes no recurrence assertion
for all initial residual profiles.

## 1. Allocation while through files remain

Suppose \(n_0>0\), and set

\[
 H=(\kappa_1 n_1^\alpha+\kappa_2 n_2^\alpha)^{1/\alpha}.
\]

If no local route is occupied, Pareto efficiency gives \(\Lambda_0=1\).
Otherwise every occupied local route saturates its own link: increasing
that route would otherwise be feasible and increase the objective.
Consequently its aggregate rate is \(1-\Lambda_0\).

The weighted \(\alpha\)-fair objective has derivative
\(\kappa_i n_i^\alpha\Lambda_i^{-\alpha}\) in an occupied coordinate.
Maximization after substituting the tight local constraints therefore gives

\[
 \kappa_0n_0^\alpha\Lambda_0^{-\alpha}
 = (\kappa_1n_1^\alpha+\kappa_2n_2^\alpha)
     (1-\Lambda_0)^{-\alpha}.
\]

Zero terms for absent routes are omitted. The optimum is interior in
\(\Lambda_0\in(0,1)\): the one-sided derivatives of the occupied utilities
at zero are infinite, and a positive feasible allocation exists. This also
covers logarithmic utility when \(\alpha=1\). Strict concavity and the
displayed derivative equation yield

\[
 \Lambda_0=\frac{a_0n_0}{a_0n_0+H},\qquad
 \Lambda_j=1-\Lambda_0\quad(n_j>0).                        \tag{6}
\]

Formula (6) for \(\Lambda_0\) also holds when \(H=0\).
Two bounds valid for every \(\alpha>0\) are

\[
 H\ge a_j n_j\quad(j=1,2),\qquad
 H\le b(n_1+n_2).                                         \tag{7}
\]

The first follows by dropping the other nonnegative term in \(H^\alpha\).
For the second, each \(n_j\le n_1+n_2\); raise that inequality to the
positive power \(\alpha\), multiply by \(\kappa_j\), add, and take the
\(1/\alpha\) power.

## 2. Retaining the original through files

Let \(A_i(t)\) count the arrivals after time zero, and put
\(L=A_1(T)+A_2(T)\). No original through file can depart by time \(T\).
Indeed, until the first such departure there are at least \(N\) through
files, and each receives service at rate at most \(1/N\). Its service by
time \(T\) is at most \(T/N<1-N^{-8}\), less than its initial residual.
A first departure by \(T\) would contradict this inequality. Therefore

\[
 N\le n_0(t)\le N+A_0(T),\qquad 0\le t\le T.              \tag{8}
\]

The total local count is at most \(N^3+L\). These assertions require no
lower bound on the residuals of newly arriving files.

## 3. Clearing the original local files despite new arrivals

Set \(r=N^{-4}\) and define the finite, arrival-dependent bounds

\[
 B_N=a_0(N+A_0(T))+b(N^3+L),\qquad D_N=\frac{rB_N}{a_*}.
\]

As long as an original local file on route \(j\) remains, its per-file
service rate is, by (6)–(8),

\[
 \frac{\Lambda_j}{n_j}
 =\frac{H/n_j}{a_0n_0+H}
 \ge\frac{a_j}{B_N}\ge\frac{a_*}{B_N}.                    \tag{9}
\]

If \(D_N<T\), every original local file has departed by \(D_N\): a file
surviving that long would have received at least
\(D_Na_*/B_N=r\), its entire possible initial residual. This argument
does not require equal residuals, simultaneous departures, or an
arrival-free interval. The use of terminal arrival counts is a pathwise
bound, not a conditional independence assertion.

Let the cumulative loss of through service relative to unit rate be

\[
 I_N(T)=\int_0^T(1-\Lambda_0(n(s)))\,ds.
\]

It is between zero and \(T\). If \(D_N<T\), the portion up to \(D_N\)
is at most \(D_N\). After \(D_N\), at most \(L\) local files remain.
Equations (6)–(8) give

\[
 1-\Lambda_0\le\frac{H}{a_0N}\le\frac{bL}{a_0N}.
\]

If \(D_N\ge T\), simply use \(I_N(T)\le T\le D_N\).
Thus in both cases

\[
 I_N(T)\le D_N+\frac{bTL}{a_0N}.                          \tag{10}
\]

The mean terminal counts are \(\mathbb EA_0(T)=T/5\) and
\(\mathbb EL=T\). Taking expectations in (10) gives, term by term,

\[
 \begin{aligned}
 \mathbb EI_N(T)
 &\le\frac{N^{-4}}{a_*}
       \{a_0(N+T/5)+b(N^3+T)\}+\frac{bT^2}{a_0N}\\
 &=\varepsilon_N(T).                                    \tag{11}
 \end{aligned}
\]

This bound is independent of the particular initial state in
\(\mathcal C_N\).

## 4. Workload balance and the pathwise error

Write \(w_j=W_j(0)\) for \(j=1,2\),
\(m=\max(w_1,w_2)\le N^{-1}\), and
\(S_j=\int_0^T\Lambda_j(n(s))\,ds\). Since
\(0\le\Lambda_j\le1-\Lambda_0\),

\[
 0\le S_j\le I_N(T).
\]

Departures remove zero residual work, so the exact workload balances are

\[
 W_0(T)-W_0(0)=A_0(T)-T+I_N(T),\qquad
 W_j(T)=w_j+A_j(T)-S_j.                                  \tag{12}
\]

Let \(Q=\max(A_1(T),A_2(T))\). Coordinatewise bounds in (12) imply

\[
 Q-I_N(T)\le\max(W_1(T),W_2(T))\le Q+m.
\]

Substitute these into the definition of \(M\) to obtain

\[
 -m\le M(X(T))-M(x)-\{A_0(T)-T+Q\}\le I_N(T).            \tag{13}
\]

All variables in (13) are integrable: the input counts have finite means
and \(I_N(T)\le T\). Taking expectations, using (11), and noting that
\(\mathbb E[A_0(T)-T+Q]=d(T)\), proves (3). Both error bounds tend to
zero for fixed \(T\), proving the asserted uniform convergence.

## 5. Negative sampled drift and the constants

For any real numbers \(u,v\),
\(\max(u,v)=(u+v+|u-v|)/2\). Since
\(\mathbb E(P_1(T)+P_2(T))=T\), (1) becomes

\[
 d(T)=-\frac3{10}T+\frac12\mathbb E|P_1(T)-P_2(T)|.
\]

Independence gives mean zero and variance \(T\) for the difference.
Cauchy–Schwarz gives (4). Its right side is negative precisely when
\(\sqrt T>5/3\), or \(T>25/9\). For such a fixed \(T\), choose
\(N\) large enough that the horizon condition holds and (2) is smaller
than \(3T/10-\sqrt T/2\); (3) then gives a uniform negative margin.

For \(\alpha=1\) and equal weights one may normalize all weights to one,
so \(a_0=a_*=1\) and \(b=2\). At \(T=4\), (2) is

\[
 \varepsilon_N(4)=\frac{34}{N}+\frac1{N^3}
                       +\frac{44}{5N^4}.
\]

Each term decreases with \(N\). At \(N=200\), its value is exactly
\(0.1700001305\), and \(4<200(1-200^{-8})\). Since
\(d(4)\le-1/5\), subtracting \(1/5\) proves (5). The finite decimal
in (5) is an exact rational number, not a numerical approximation.

## 6. Relation to the earlier obstruction

The earlier exact states have \(N\) through files of residual one and
\(N^3\) files of residual \(N^{-4}\) on either local route. They belong
to \(\mathcal C_N\). The accessible perturbations constructed in the
earlier proof have the same counts, through residuals in
\([1-N^{-8},1]\), and local residuals in
\([N^{-4}-N^{-8}-N^{-11},N^{-4}]\). They too belong to
\(\mathcal C_N\) for \(N\ge2\). Thus (3) applies uniformly to the
positive-probability sets from that construction.

At either exact state and \(N\ge2\), the instantaneous generator of
\(M\) is nevertheless

\[
 \mathcal GM=\frac15-\frac1{2N}.                           \tag{14}
\]

To check (14), the occupied local link determines the maximum workload
and is saturated, giving service derivative \(-1\). A through arrival
increases \(M\) by one. A same-local-route arrival also increases it by
one; an arrival on the empty local route increases it by \(1-N^{-1}\).
Weighting by the three arrival rates gives (14). It is positive for
\(N>2\). The fixed-horizon statement (3) is compatible with this
pointwise generator calculation because the original tiny local files
clear rapidly, as quantified by (9)–(11).

The estimate uses a large persistent through population, tiny initial
local residuals, deterministic unit input files, and a fixed horizon.
It does not control every state with large \(M\), establish a petite set,
or supply a fluid-to-stochastic recurrence theorem. Those steps remain
necessary for the full stability problem.

## 7. A service accounting bound and a wider initial-state class

The same limit holds under weaker restrictions on the original local
files. The following argument gives a second service-loss bound.

Fix a number \(c>0\) satisfying

\[
 H(u_1,u_2)=(\kappa_1u_1^\alpha+\kappa_2u_2^\alpha)^{1/\alpha}
       \le c(u_1+u_2)\qquad(u_1,u_2\ge0).                 \tag{15}
\]

One may always use \(c=b\), by (7). If \(\alpha=1\) and all weights are
one, one may use \(c=1\).

Consider any finite initial state in which every residual is at most one,
and suppose \(W_0(0)>T\). Since route-0 service is at most one, workload
balance gives

\[
 W_0(t)\ge W_0(0)-t\ge R:=W_0(0)-T>0\quad(0\le t\le T).
\]

All residuals remain at most one because arrivals have size one. Therefore
\(n_0(t)\ge W_0(t)\ge R\), so (6) holds throughout the interval even
if some original through files depart.

At a time away from events let \(o_j\) and \(m_j\) be the original and
new local counts on route \(j\); thus \(n_j=o_j+m_j\). Let
\(q=1-\Lambda_0\), and let \(s\) be the total instantaneous service to
original local files, summed over both local routes. Equal sharing within
each route gives

\[
 s=q\sum_{j:n_j>0}\frac{o_j}{n_j}.                       \tag{16}
\]

If no local route is occupied, \(q=s=0\). If only route \(j\) is
occupied, set \(\theta=m_j/n_j\). Then \(q-s=q\theta\) and, by
homogeneity, \(\theta H(n_1,n_2)=H(m_1,m_2)\).

If both routes are occupied, put
\(\theta=(1-o_1/n_1-o_2/n_2)^+\). When \(\theta=0\), \(q-s\le0\).
Otherwise

\[
 \theta=\frac{m_1}{n_1}+\frac{m_2}{n_2}-1
 \le\frac{m_j}{n_j}\quad(j=1,2),
\]

since each new-file fraction is at most one. Consequently
\(\theta n_j\le m_j\) for both coordinates. Monotonicity and
degree-one homogeneity of \(H\) imply

\[
 \theta H(n_1,n_2)=H(\theta n_1,\theta n_2)\le H(m_1,m_2).
\]

In either occupied case, (6), (15), and \(n_0\ge R\) give

\[
 \begin{aligned}
 q-s
 &\le\frac{\theta H(n_1,n_2)}{a_0n_0+H(n_1,n_2)}\\
 &\le\frac{H(m_1,m_2)}{a_0R}
 \le\frac{c(m_1+m_2)}{a_0R}.
 \end{aligned}                                           \tag{17}
\]

When \(q-s\le0\), the last upper bound is valid directly; in that case
no positive \(\theta\) is needed.

Original local files can receive at most their initial total work
\(w=W_1(0)+W_2(0)\). At time \(t\), new local counts are at most
\(A_1(t)+A_2(t)\). Let
\(J_T=\int_0^T(A_1(t)+A_2(t))\,dt\). Integrate (17), then use
Tonelli's theorem and \(\mathbb E(A_1(t)+A_2(t))=t\), to obtain

\[
 I_N(T)\le w+\frac{cJ_T}{a_0R},\qquad
 \mathbb E I_N(T)\le w+\frac{cT^2}{2a_0R}.                \tag{18}
\]

The first inequality is pathwise. It does not assume any original local
file clears by time \(T\). Equations (12)–(13) still hold because
\(W_0(t)>0\); they did not require the original through files to survive.
Thus every such initial state satisfies the explicit estimate

\[
 d(T)-\max(W_1(0),W_2(0))
 \le\mathbb E_x[M(X(T))-M(x)]
 \le d(T)+w+\frac{cT^2}{2a_0(W_0(0)-T)}.                 \tag{19}
\]

For example, let \(\mathcal D_N\) consist of all finite states with
residuals at most one satisfying

\[
 W_0(0)\ge N-1,\qquad W_1(0)+W_2(0)\le N^{-1}.
\]

There is no restriction on the finite numbers of initial files or on the
individual local residuals beyond these inequalities. The earlier
\(\mathcal C_N\) is contained in \(\mathcal D_N\), because
\(N(1-N^{-8})=N-N^{-7}\ge N-1\). For \(T<N-1\), (19) gives

\[
 d(T)-N^{-1}\le\mathbb E_x[M(X(T))-M(x)]
 \le d(T)+N^{-1}+\frac{cT^2}{2a_0(N-1-T)},
 \qquad x\in\mathcal D_N.                                \tag{20}
\]

This proves uniform convergence to the same \(d(T)\) over the wider
class \(\mathcal D_N\). In particular, for equal weights and
\(\alpha=1\), choose \(c=a_0=1\). At \(T=4\) and every \(N\ge100\),

\[
 \sup_{x\in\mathcal D_N}\mathbb E_x[M(X(4))-M(x)]
 \le-\frac15+\frac1{100}+\frac8{95}
 =-\frac{201}{1900}<0.                                  \tag{21}
\]

Each positive term in the upper bound decreases with \(N\), justifying
the bound for all \(N\ge100\). Large initial local workloads remain
outside this estimate; (20) alone does not prove recurrence.
