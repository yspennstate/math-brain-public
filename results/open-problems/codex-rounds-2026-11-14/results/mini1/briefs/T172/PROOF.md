# A uniform bound with a growing number of batching levels

Write `epsilon = 1-rho`. Arrivals in this note are independent over queues
and slots, with one Bernoulli arrival of mean `rho/n` at each queue per slot.
All logarithms except `log_2` are natural.

**Theorem.** For every integer `n >= 2` and every
`0 < epsilon <= exp(-128)`, there is a scheduling policy for which

\[
 \sup_{t\geq0}\mathbb E Q_\Sigma(t)
 \leq \frac{10^6 n}{\varepsilon}
       \log\frac{144n}{\varepsilon}
       \bigl(1+\log(1/\varepsilon)\bigr)^9.                 \tag{1}
\]

Here the switch starts empty. The policy also has a stationary version
(including its scheduling phase) satisfying the same bound.

This bound contains logarithmic factors and does not give the exact
`O(n/epsilon)` bound. No assertion is made for temporally dependent arrivals
specified only through their rates.

The construction is the recursive batching policy of Taha Ameen and Weina
Wang, *Approaching Optimal Scaling of Queue Size for an Input-Queued Switch*,
[arXiv:2610.37521v1](https://arxiv.org/html/2610.37521v1), Section 3.1.
Their stated theorem fixes the number of levels. The point here is a uniform
choice of a growing number of levels, with all parameter conditions checked.
The argument below supplies the needed finite estimates.

## 1. Parameters, including rounding

Set

\[
 C=108,\quad K=144,\quad \ell=\log(1/\varepsilon),\quad
 h=\log(Kn/\varepsilon),\quad
 k=\left\lceil\log_2(1+\ell)\right\rceil,\quad
 \alpha=\frac{2^k}{2^k-1}.
\]

In particular `k >= 2`, `1 < alpha <= 4/3`, and `h >= 1`. Define integers

\[
 L_1=\lceil Kh\varepsilon^{-\alpha}\rceil,\qquad
 L_j=\lceil K\varepsilon^{-\alpha/2^{j-1}}\rceil\quad(2\leq j\leq k),
 \qquad T_j=\prod_{i=1}^jL_i.
\]

Put `beta_j = 2 alpha (1-2^{-j})` and `D=(2K)^k`. Since each expression
inside a ceiling is at least one, replacing its ceiling by twice that
expression gives

\[
 K^j h\varepsilon^{-\beta_j}\leq T_j
 \leq(2K)^j h\varepsilon^{-\beta_j},\qquad \beta_k=2.       \tag{2}
\]

In particular, every `T_j <= D h epsilon^{-2}`, and
`T_k >= K^2 h epsilon^{-2}`.

The following estimates control the dependence on `k`:

\[
 D\leq K\cdot2\,(1+\ell)^9=288(1+\ell)^9,\qquad
 D\leq\varepsilon^{-1/2},\qquad k\leq D.                 \tag{3}
\]

For the first inequality, `k <= 1+log_2(1+ell)`, and
`log(288)<6`, `log(2)>2/3`. For the second, these same estimates give
`log D <= 6+9 log(1+ell)`. At `ell=128` the right side is less than
`6+45=51<64`. The derivative of
`ell/2-6-9 log(1+ell)` is positive on `[128,infinity)`, proving
`log D <= ell/2` throughout that interval. The last inequality follows
from `288^k >= 2^k >= k`. Also,

\[
 \varepsilon^{-\alpha}
 =\varepsilon^{-1}\exp\!\left(\frac{\ell}{2^k-1}\right)
 \leq e\varepsilon^{-1}.                                \tag{4}
\]

Define integer service counts and real remainders recursively:

\[
 \begin{split}
 S_1&=\lfloor\rho T_1-C\sqrt{T_1h}\rfloor,&
 a_1&=\rho T_1-S_1,\\
 S_j&=\lfloor L_ja_{j-1}-C\sqrt{T_jh}\rfloor,&
 a_j&=L_ja_{j-1}-S_j\quad(2\leq j<k).
 \end{split}                                             \tag{5}
\]

Thus

\[
 C\sqrt{T_jh}\leq a_j<C\sqrt{T_jh}+1
                    \leq(C+1)\sqrt{T_jh}.                 \tag{6}
\]

At the final level use all remaining slots:

\[
 S_k=T_k-\sum_{j<k}(T_k/T_j)S_j
     =\varepsilon T_k+L_ka_{k-1}.                         \tag{7}
\]

The first expression shows that `S_k` is an integer even when `rho T_k`
and the `a_j` are not integers.

## 2. Policy and admissibility

Partition time into nested blocks: a level-1 block has `L_1` slots;
a level-`j` block has `L_j` consecutive level-`(j-1)` blocks.
In each block assign the first `S_1` slots of each level-1 subblock to
level 1, then the first unassigned `S_2` slots of each level-2 subblock to
level 2, and continue. The final level gets the remaining slots.

For `1 <= r <= k-2`, independently label each arriving packet with initial
level `r+1` with probability

\[
 \theta_r=\frac{a_r}{2\rho T_r}.
\]

Give it initial level 1 with the remaining probability. No packet starts
at level `k`. For `j<k` set

\[
 \tau_j=\sum_{r=j}^{k-2}\theta_r,\qquad
 m_j=\rho T_j\tau_j=\frac{T_j}{2}\sum_{r=j}^{k-2}\frac{a_r}{T_r}.
\]

Empty sums vanish. From (6) and `L_{j+1} >= 144`,

\[
 \frac{a_{j+1}/T_{j+1}}{a_j/T_j}
 \leq\frac{109}{108\sqrt{L_{j+1}}}
 \leq\frac{109}{1296}<\frac1{10}.
\]

Consequently,

\[
 m_j\leq\frac{a_j}{2}\sum_{r\geq0}10^{-r}
       =\frac{5a_j}{9}\leq\frac{2a_j}{3}.                 \tag{8}
\]

Write `d_1=rho T_1`, `d_j=L_j a_{j-1}` for `2 <= j<k`, and
`mu_j=d_j-m_j`, `nu_j=rho T_j-m_j`. Since `rho >= 1/2`,

\[
 \frac{d_1}{a_1}\geq\frac{6}{109}\varepsilon^{-1/2}>16,
 \qquad
 \frac{d_j}{a_j}\geq\frac{108\sqrt{L_j}}{109}
                    \geq\frac{1296}{109}>8\quad(j\geq2). \tag{9}
\]

For the first strict inequality it suffices that `epsilon <= exp(-128)`:
`exp(64)>2^64`, and `6*2^64>16*109`.
It follows that `tau_1=m_1/(rho T_1) <= 5/144 < 1`, so all labeling
probabilities are valid, and every `S_j>0`. The identities (5) telescope:

\[
 \sum_{i=1}^{j}(T_j/T_i)S_i=\rho T_j-a_j.                \tag{10}
\]

Thus a level-`j` block leaves `epsilon T_j+a_j>0` slots unassigned.
Before assigning `S_j`, there are `epsilon T_j+d_j` available slots,
which exceeds `S_j=d_j-a_j`. This proves feasibility of all allocations.

A packet at level `j<k` is eligible during the level-`j` block immediately
following its original arrival block at that level. At the first level-`j`
service slot, form the bipartite multigraph of all such eligible packets.
If it has an `S_j`-regular spanning subgraph, serve that subgraph in `S_j`
perfect matchings. Otherwise leave these service slots idle. After the
last such slot, promote every unserved eligible packet to level `j+1`.
Packets retain their original arrival times on promotion.

All promotions needed for a parent block occur before its first parent
service slot. Indeed, the latest child arrival block in a parent is served
in the first child block of the next parent; child service slots precede
the first parent slot there. Induction gives the same statement at every
level. Thus the eligibility rule can be implemented without waiting for
future packets.

At level `k`, collect the residual packets from a complete original
level-`k` arrival block at the first level-`k` service slot of the next
block. Decompose this graph into the minimum number of matchings and append
them to a FIFO list. Serve one matching per level-`k` slot while the list
is nonempty. All choices of subgraphs, decompositions, and ordering are
made by deterministic rules using only the graph in question.

A bipartite multigraph of maximum degree `M` decomposes into `M` matchings:
add edges to fill all vertex degrees to `M` (the two sides have equal
total deficits), and repeatedly remove a perfect matching. Such a matching
exists by Hall's condition, since `M|X| <= M|N(X)|`. Delete the added edges
after the decomposition. This also proves that an `S_j`-regular subgraph
can be served in exactly `S_j` slots.

## 3. A finite factor-test estimate

Here is the graph estimate needed for the service tests. Its proof is
included to specify the constants and the scope of its quantifiers.

Suppose a bipartite graph `R` on `n+n` vertices contains a random graph
`H` whose edge multiplicities are independent `Binomial(T,q)` variables.
Let real numbers `d,b` satisfy

\[
 nTq\geq d/2,\quad d\geq192\log n,\quad d\geq24b>0.
\]

Except on an event of probability at most `4 exp(-d/96)`, simultaneously
for every graph `R` containing this `H`, if all degrees of `R` lie in
`[d-b,d+b]`, it contains an `s`-regular spanning subgraph for every integer
`0 <= s <= d-3b`. The graph `R` may depend on `H`.

To prove the probability assertion, consider sets `X` of inputs and `Y`
of outputs, with sizes `x,y` satisfying
`0<x-y<min(y,n-x)`. The number of edges of `H` from `I\X` to `Y` is
binomial with mean at least `d(n-x)y/(2n)`. The binomial lower-tail bound
`P(B < E B/2) <= exp(-E B/8)` gives

\[
 \mathbb P\!\left(e_H(I\setminus X,Y)<\frac{d(n-x)y}{4n}\right)
 \leq\exp\!\left(-\frac{d(n-x)y}{16n}\right).             \tag{11}
\]

When `x+y<=n`, the conditions imply `x<2y`, `y>=2`, and `n-x>=n/3`.
There are at most `y` choices of `x` and at most `n^{3y-1}` pairs of
sets for each such choice. The union bound is at most

\[
 \sum_{y\geq2}yn^{3y-1}e^{-dy/48}
 \leq\sum_{y\geq2}e^{-(d/48-3\log n)y}
 \leq\frac{e^{-d/96}}{1-e^{-d/192}}
 \leq2e^{-d/96}.                                        \tag{12}
\]

Here `y<=n` in the finite sum, `d/48-3 log n >= d/192`, and
`exp(-d/192)<=1/n<=1/2`. For `x+y>n`, exchange input and output sides
and take the pair of complementary sets. This preserves the tested
edge count and reduces to the preceding case. Doubling (12) proves
that, except with probability `4 exp(-d/96)`, every such pair satisfies

\[
 e_H(I\setminus X,Y)\geq\frac{d(n-x)y}{4n}.              \tag{13}
\]

It remains to prove the deterministic consequence of (13). The integral
max-flow criterion for an `s`-regular spanning subgraph is

\[
 e_R(X,O\setminus Y)\geq s(x-y)\quad\hbox{for every }X,Y. \tag{14}
\]

Indeed, use capacity `s` from the source to each input and from each
output to the sink, and the edge multiplicities as intermediate
capacities. A cut with source-side vertices `X,Y` has capacity
`s(n-x)+e_R(X,O\Y)+sy`; requiring at least `sn` gives (14).

Suppose (14) fails for some `s<=d-3b`. Necessarily `x>y`.
By exchanging the two sides and taking complements if needed, arrange
`x+y<=n`. The degree bounds give

\[
 0\leq e_H(I\setminus X,Y)\leq e_R(I\setminus X,Y)
 <(d-3b)(x-y)-(d-b)x+(d+b)y=2b(2y-x).                    \tag{15}
\]

Thus `x<2y`, `0<x-y<y<=n-x`, and `n-x>=n/3`.
But (13) implies

\[
 e_H(I\setminus X,Y)\geq dy/12\geq2by>2b(2y-x),
\]

contradicting (15). This proves the graph estimate without any independence
assumption between `R` and `H`.

## 4. Uniform failure bounds at every level

All hypotheses for the preceding graph estimate hold uniformly in the
level. Specifically, (8)--(9) imply

\[
 \mu_j\geq24(a_j/9),\qquad
 \mu_j-a_j/3\geq S_j,\qquad
 a_j/9\leq\nu_j\leq T_j.                                \tag{16}
\]

For the last inequality on the left, use
`rho T_j/a_j >= rho sqrt(T_1/h)/109 > 16` and (8).
Also `mu_j>=d_j/2`. For `j=1`,
`mu_1/h >= (K/4)epsilon^{-1}>4608`.
For `j>=2`,
`mu_j/h >= (C K sqrt(K)/2)epsilon^{-1/2}>4608`.
Hence

\[
 \mu_j\geq4608h=96\cdot48h\geq192\log n.               \tag{17}
\]

For one original level-`j` arrival block, let `N_{v,j}` count the original
arrivals at port `v` with initial level at most `j`.
It is `Binomial(nT_j,rho(1-tau_j)/n)` with mean `nu_j`.
If all constituent lower-level tests succeed, the eligible graph `R`
has degrees

\[
 \deg_R(v)=N_{v,j}-(\rho T_j-d_j)
          =\mu_j+(N_{v,j}-\nu_j).                        \tag{18}
\]

For `j=1`, there are no lower removals and `R` itself has independent
binomial edges. For `j>=2`, let `H` consist of packets initially labeled
`j`. Its edges are independent `Binomial(T_j,rho theta_{j-1}/n)` variables
and its mean degree is `d_j/2 >= mu_j/2`. Such packets cannot be served
at lower levels, so `H` is always a subgraph of the eligible `R`.

Use the graph estimate with `d=mu_j`, `b=a_j/9`. For `j=1` take `H=R`;
its mean degree is `mu_1`. The two-sided binomial bound
`P(|B-E B|>x)<=2 exp(-x^2/(3 E B))`, valid for `0<x<=E B`,
and a union bound over ports show that a new failure at this level,
in the absence of any lower failure, is contained in an event of probability
at most

\[
 4n\exp\!\left(-\frac{a_j^2}{243\nu_j}\right)
       +4e^{-\mu_j/96}
 \leq4ne^{-48h}+4e^{-48h}\leq e^{-40h}=:p.               \tag{19}
\]

We used `C^2/243=48`, `nu_j<=T_j`, (17), `n<=exp(h)`, and `h>=1`;
indeed `8 exp(-47h)<=exp(-40h)` when `h>=1`.
No conditional probability estimate, or independence of failure events,
is used in (19).

Let `M_j` be the number of level-`1,...,j` blocks in one original
level-`j` block, including that block. Then

\[
 M_j=\sum_{i=1}^jT_j/T_i\leq jT_j/T_1\leq kT_j/T_1.     \tag{20}
\]

Induction and a union bound show that the probability of any lower or
current failure affecting this block is at most `M_j p`.
Let `F_j` be the total number of prescribed service slots missed because
of failed tests at levels at most `j` for its packets. It is zero without
such a failure and always at most `T_j`. Therefore

\[
 \mathbb EF_j\leq T_jM_jp\leq a_j\quad(j<k).            \tag{21}
\]

Here is an explicit check of the last inequality, uniform in `j,k`:
by (2), (3), (6), and `T_1>=Kh epsilon^{-1}`,

\[
 \frac{T_jM_jp}{a_j}
 \leq\frac{kD^{3/2}}{CK}\varepsilon^{-2}e^{-40h}
 \leq\frac{\varepsilon^{-13/4}}{CK}e^{-4h}
 =\frac{\varepsilon^{3/4}}{CK(Kn)^4}\leq1.              \tag{22}
\]

Let `R_j` be the residual graph from this original block after its last
level-`j` service slot, also including packets initially above level `j`.
The service counts telescope by (10); each successful slot at these
levels removes exactly one packet at every port. Thus, identically,

\[
 \deg_{R_j}(v)=N^{(v)}(T_j)-\rho T_j+a_j+F_j,            \tag{23}
\]

where `N^{(v)}(T_j)` counts all original arrivals at the port.
Taking expectations in (23) and using (21) gives

\[
 \mathbb E\deg_{R_j}(v)\leq2a_j,\qquad
 \mathbb E|E(R_j)|\leq2na_j.                            \tag{24}
\]

The second inequality sums only over inputs, so every packet is counted
once.

## 5. The queue of final-level matchings

Put `T=T_k` and `c=L_k a_{k-1}`. Let `F` be the sum of missed lower-level
slots for a complete original level-`k` arrival block. By (20),

\[
 0\leq F\leq T,\qquad
 \frac{\mathbb EF}{h}
 \leq\frac{kD^2}{K}\varepsilon^{-3}e^{-40h}
 \leq\frac{\varepsilon^{-9/2}}K e^{-6h}
 =\frac{\varepsilon^{3/2}}{K(Kn)^6}\leq1.               \tag{25}
\]

The residual graph decomposes into exactly

\[
 A=c+Z+F,\qquad Z=\max_v N^{(v)}(T)-\rho T              \tag{26}
\]

matchings. This follows from the maximum-degree decomposition and the
analogue of (23) before final-level service. In particular `A` is a
nonnegative integer bounded by `nT`. Distinct original level-`k` blocks
produce independent, identically distributed values of `A`: every lower
decision uses only that block's original arrivals and independent labels,
and fixed rules. Their service times may occur later, but do not change
this dependence on the original data.

We next bound `Z` without any unquantified limit. Define
`V=max_v |N^{(v)}(T)-rho T|` and `a=3 sqrt(Th)`.
Since `T>=K^2 h epsilon^{-2}`,
`a/(rho T)<=3 epsilon/(rho K)<=6/K<1`.
The binomial bound and the union bound give

\[
 \mathbb P(V>a)\leq4ne^{-3h}.
\]

As `V<=nT` and `T<=D h epsilon^{-2}`,

\[
 \mathbb EV^2\leq9Th+4n^3T^2e^{-3h}
 \leq\left(9+\frac{4D\varepsilon}{K^3}\right)Th
 \leq16Th.                                              \tag{27}
\]

The last step uses `D epsilon<=epsilon^{1/2}<=1` from (3).
In particular

\[
 0\leq\mathbb EZ\leq4\sqrt{Th},\qquad
 \mathbb EZ^2\leq16Th.                                  \tag{28}
\]

For the lower bound on the mean, `Z` dominates any one centered port count.
Equations (25)--(28) imply

\[
 0\leq\mathbb EA-c\leq4\sqrt{Th}+h
 \leq\left(\frac4K+\frac{\varepsilon}{K^2}\right)
          \varepsilon T\leq\frac{\varepsilon T}{2}.      \tag{29}
\]

Also `E F^2<=T E F<=Th`, so, without assuming independence between `Z`
and `F`,

\[
 \operatorname{Var}(A)
 \leq2\operatorname{Var}(Z)+2\operatorname{Var}(F)
 \leq34Th.                                              \tag{30}
\]

There are precisely `S_k=c+epsilon T` final-level service slots between
successive insertions into the list of matchings. If `W_b` is the number
of matchings just before insertion `b`, then

\[
 W_0=0,\qquad W_{b+1}=(W_b+A_b-S_k)^+.
\]

Let `delta=S_k-E A`. By (29),
`epsilon T/2 <= delta <= epsilon T`.
For completeness, the scalar queue bound used here is

\[
 \sup_b\mathbb EW_b\leq
 \frac{\operatorname{Var}(A)}{2\delta}+\frac\delta2.     \tag{31}
\]

To justify (31), let `X=A-S_k`. These bounded iid increments have negative
mean. For some `theta>0`, `r=E exp(theta X)<1`, by differentiating the
moment generating function at zero. A union bound over random-walk
partial sums gives an exponential tail for their supremum:
`P(sup_{m>=1} sum_{i=1}^m X_i>x)<=exp(-theta x) r/(1-r)` for `x>=0`.
The stationary Lindley queue can therefore be constructed from past
increments and has finite second moment. It is independent of the next
increment. In stationarity,
`(W+X)_+^2 <= (W+X)^2` gives
`0 <= -2 delta E W + E X^2`, hence (31) for its stationary mean.
Coupling a queue started at zero below this stationary queue proves
the claimed uniform bound for all `b`.

Combining (30)--(31),

\[
 q:=\sup_b\mathbb EW_b\leq34h/\varepsilon+\varepsilon T/2.
                                                               \tag{32}
\]

## 6. Count packets and complete the bound

Let `X_j(t)` denote the number of packets currently at level `j`.
A level-1 packet can come only from the current or preceding original
level-1 block, giving

\[
 \mathbb EX_1(t)\leq2n\rho T_1.
\]

For `2<=j<k`, every packet currently at level `j` came from the current
or preceding original level-`j` block. Those two blocks contain at most
`2L_j` level-`(j-1)` arrival blocks. Each such packet belongs to that
arrival block's residual graph `R_{j-1}`. Counting the whole residual
graphs can overcount packets already served, but cannot omit a current
level-`j` packet. By (24),

\[
 \mathbb EX_j(t)\leq4nL_ja_{j-1}.                       \tag{33}
\]

The same counting bounds final-level packets not yet inserted into the
list of matchings by `4nL_k a_{k-1}`. Between two insertions, the list
contains at most the number just before the first insertion plus its
new batch, hence at most `W_b+A_b` matchings. Each matching contains
at most `n` packets. By (29) and (32),

\[
 \mathbb EX_k(t)
 \leq n\bigl(5L_ka_{k-1}+34h/\varepsilon+\varepsilon T_k\bigr).
                                                               \tag{34}
\]

At startup some of the arrival blocks in these counts do not exist;
their omission only decreases the bounds. Summing gives

\[
 \mathbb EQ_\Sigma(t)\leq n\left(
 2T_1+4\sum_{j=2}^{k-1}L_ja_{j-1}+5L_ka_{k-1}
       +34h/\varepsilon+\varepsilon T_k\right).          \tag{35}
\]

There is no constant in (35) whose dependence on `k` is suppressed.
To bound it, the identity

\[
 \frac{\alpha}{2^{j-1}}+\frac{\beta_{j-1}}2=\alpha
\]

and (2), (6) give

\[
 L_ja_{j-1}\leq109(2K)^{(j+1)/2}h\varepsilon^{-\alpha}.
\]

The geometric series has ratio `sqrt(2K)>2`, so

\[
 \sum_{j=2}^kL_ja_{j-1}
 \leq218(2K)^{(k+1)/2}h\varepsilon^{-\alpha}
 \leq218D h\varepsilon^{-\alpha}.                       \tag{36}
\]

In addition,
`2T_1<=4K h epsilon^{-alpha}<=D h epsilon^{-alpha}`,
`34h/epsilon<=D h epsilon^{-alpha}`, and
`epsilon T_k<=D h epsilon^{-alpha}`.
Use coefficient 5 for all terms in (36) to obtain from (35)

\[
 \sup_t\mathbb EQ_\Sigma(t)
 \leq1093nD h\varepsilon^{-\alpha}
 \leq1100nD h\varepsilon^{-\alpha}.                     \tag{37}
\]

Finally (3), (4), and `e<3` give

\[
 1100D\varepsilon^{-\alpha}
 \leq1100\cdot288\cdot3\,
       \frac{(1+\ell)^9}{\varepsilon}
 =950400\,\frac{(1+\ell)^9}{\varepsilon}
 <10^6\,\frac{(1+\ell)^9}{\varepsilon},
\]

which proves (1).

To obtain a stationary version, use two-sided iid arrivals and labels,
and choose the block phase uniformly from `0,...,T_k-1` independently.
Lower-level packets and plans depend only on a bounded window of original
arrival blocks. At level `k`, use the stationary FIFO queue constructed
in the proof of (31). Its negative-drift workload has a finite last empty
epoch before any fixed insertion, so its ordered list of matchings is
well-defined from the original batches. The resulting process is invariant
under a one-slot shift. The packet counts (33)--(35) still apply, using
the stationary mean in (31). This proves the stationary assertion.

## 7. Limits of the result

The bound is uniform in `n` and in the stated interval of `epsilon`, but
has a factor `log(144n/epsilon)(1+log(1/epsilon))^9` above the conjectured
order. It applies to iid uniform Bernoulli traffic. Nonuniform rates,
other arrival laws, and removal of the logarithmic factors are not
established here. The large value of the explicit constant is immaterial
to the scaling claim, and has not been optimized.
