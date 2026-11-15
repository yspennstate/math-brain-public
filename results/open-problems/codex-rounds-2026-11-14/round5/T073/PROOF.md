# Exact-three disagreement correction for the fair-tie process

At each site of Z² an independent rate-one Poisson clock updates a spin
in {0,1}. If k of its four nearest neighbors have spin 1, the updated
spin is 1 with probability

\[
p_e(k)=
\begin{cases}
e,&k=0,1,\\
1/2,&k=2,\\
1-e,&k=3,4.
\end{cases}                                                     \tag{1}
\]

Thus a tie is resampled fairly, independently of the site's old spin.
Assume 0≤e≤1/2 and put a=1/2−e. Define

\[
\begin{aligned}
C_2(e)&=4a(1-e^3/2)-\frac{17}{630}e^4a^4
                 -\frac4{15}e^5a^3-\frac{16}{81}e^6a^3,\\
C_3(e)&=C_2(e)-\frac{136}{2835}e^5a^4.
\end{aligned}                                                   \tag{2}
\]

**Theorem.** If C₃(e)<1, process (1) has exactly one stationary probability
measure. There is a unique e₃∈(0,1/4) with C₃(e₃)=1, and this sufficient
condition holds precisely for e>e₃ in [0,1/2]. In particular, uniqueness
holds throughout [0.24807562,1/2]. Exact bounds are

\[
\frac{19193920498167976369215855}{77371252455336267181195264}
<e_3<
\frac{38387840996335952738431711}{154742504910672534362390528}.
                                                               \tag{3}
\]

The new estimate concerns exactly three disagreeing neighbors. The
low-noise coexistence statement is unresolved here.

## 1. Stationary ordered coupling

Give every clock ring an independent uniform mark U∈[0,1], and update
to 1 exactly when U≤pₑ(k). The sequence pₑ(k) is nondecreasing. Sharing
the clocks and marks therefore preserves coordinatewise order between
two configurations η≤ξ.

The construction defines a Feller process on the compact product space
{0,1}^{Z²}. To see the needed finite dependence, explore backward from
a finite set over a bounded interval. Each dependency is replaced at a
rate-one ring by at most four dependencies. A dominating branching
process has expected population at most its starting population times
exp(3t), and finite expected total number of branchings on bounded time
intervals. Thus the exploration is almost surely finite. Its truncation
to a large finite region gives continuity of the semigroup on cylinder
functions. Uniform approximation gives continuity on every continuous
function. The same construction applies to the ordered pair process.

Write Sₜ for the one-copy semigroup. Attractiveness implies
δ₀Sₜ≤δ₀Sₜ₊ₛ and δ₁Sₜ≥δ₁Sₜ₊ₛ. For every finite set A, the probability
that all its spins equal 1 is therefore monotone in t. These probabilities
determine all cylinder probabilities by inclusion-exclusion. Compactness
then gives weak limits μ⁻ and μ⁺. The Feller property and semigroup
identity show that these limits are stationary. Translation invariance
passes from the initial states and dynamics to both limits. For every
stationary measure ν, including ones without translation invariance,

\[
\mu^-\le\nu\le\mu^+.                                        \tag{4}
\]

Indeed, apply Sₜ to δ₀≤ν≤δ₁ and let t increase.

Start the ordered pair process at (0,1) and average its laws over [0,T].
Any weak subsequential limit λ is stationary: applying the pair semigroup
for a fixed duration s changes the average expectation of a bounded
continuous function f by at most 2s‖f‖∞/T; Feller continuity passes this
identity to the limit. Its marginals are μ⁻ and μ⁺, since the individual
laws converge. It is supported on ordered pairs and is translation
invariant.

Run the pair from λ, independently of future clocks and marks. Put

\[
D_z=\xi_z-\eta_z,\qquad d=\mathbb E D_z,
\qquad q_x=p_e(K_x(\xi))-p_e(K_x(\eta)),
\]

where Kₓ counts 1-neighbors of x. Translation invariance makes d
independent of z. At a ring of x the conditional mean new disagreement
is qₓ. Only rings of x change Dₓ, so the generator identity for this
bounded local function gives

\[
\mathbb E q_x=d.                                              \tag{5}
\]

## 2. An exact local identity

Let N(x) be the set of four neighbors of x, and define

\[
M_x=\sum_{y\in N(x)}D_y,\qquad T_x=\binom{M_x}{3},
\qquad J_x=\mathbf1_{\{M_x=3\}}.
\]

For y∈N(x), let Bₓ,ᵧ be the event that all three sites in N(x)\{y}
have one common value in both copies. For an unordered pair A⊂N(x),
let E_A mean that its two sites disagree, and the other two sites have
one common value in both copies. Set Hₓ=∑_{|A|=2}1_{E_A}. Then

\[
q_x=a\left[\sum_{y\in N(x)}D_y(1-\mathbf1_{B_{x,y}})
                       -\frac12T_x-H_x-\frac12J_x\right].     \tag{6}
\]

To verify (6), write pₑ(k)=e+ag(k), where g=(0,0,1,2,2). If Mₓ=0,
both sides are zero. If Mₓ=1, write c for the number of common 1-neighbors
among the other three. The increment g(c+1)−g(c) is 0,1,1,0 for
c=0,1,2,3, respectively. The blocked term removes the sole disagreement
exactly when c=0 or 3, and Tₓ=Hₓ=Jₓ=0.

If Mₓ≥2, all weighted blocked terms vanish. For Mₓ=2, let c count the
common 1-neighbors at the remaining two sites. The increment
g(c+2)−g(c) is 1,2,1 for c=0,1,2. Here Hₓ equals 1 precisely when
c=0 or 2, and Tₓ=Jₓ=0. For Mₓ=3, the lower and upper counts are
(0,3) or (1,4), so the increment is 2. The bracket is
3−1/2−0−1/2=2. For Mₓ=4, the increment is 2, Tₓ=4 and Hₓ=Jₓ=0,
so the bracket is 4−2=2. This proves the identity; it also holds when a=0.

Thus the earlier inequality, obtained by omitting Jₓ/2, leaves exactly
this residual. The Tₓ and Jₓ terms both contribute at Mₓ=3; together
they use its gap of one. At Mₓ=4 only Tₓ contributes.

## 3. Last-source-ring estimate

The following calculation is used for all event bounds. Fix a source
v and an observation time T>0. For a source ring r∈(0,T], write s=T−r.
Require no source ring after r. Suppose that, uniformly over every
post-ring history with Dᵥ(r)=1, a future success event has conditional
probability at least

\[
\beta\exp(-s)(1-\exp(-s))^n,                                \tag{7}
\]

and success implies a target event F at T. There is at most one source
ring with no later ring, so pathwise

\[
\mathbf1_{F(T)}\ge
\sum_{r\in\mathcal P_v\cap(0,T]}D_v(r)
                  \mathbf1_{\{\text{success from }r\}}.        \tag{8}
\]

Here Dᵥ(r) is the disagreement immediately after the ring. Apply the
unit-rate Poisson insertion formula to this sum. At a deterministic
inserted r the pre-ring pair has law λ, since inserting a ring does not
change the past. Its independent uniform mark produces a post-ring
disagreement of mean E qᵥ=d by (5). Future clocks and marks are
independent of this history, and (7) is uniform in it. Consequently,

\[
\mathbb P(F)\ge
\beta d\int_0^T\exp(-s)(1-\exp(-s))^n\,ds
=\frac{\beta d}{n+1}(1-\exp(-T))^{n+1}.
\]

Stationarity makes the left side independent of T. Letting T tend to
infinity gives P(F)≥βd/(n+1). This uses a stationary process followed
forward from time zero; it assumes no independence after conditioning
on a disagreement at the observation time.

For n distinct nonsource clocks required to ring after r, the probability
is (1−exp(−s))ⁿ. Conditional on this event, their last times are independent
and identically distributed with a continuous law. If L of their n!
orders satisfy specified precedence constraints, their contribution to β
is L/n!, and after source integration the clock coefficient is

\[
\frac{L}{(n+1)!}.                                            \tag{9}
\]

There are two useful forcing mark intervals. A mark in [0,e] forces
common 1; a mark in (1−e,1] forces common 0. Each has length e and is
independent of all inputs.

## 4. Transmission and the preceding event bounds

The receiver calculation is the same for each broadcast below. Hold a
source disagreement at x by prohibiting further source rings. Give a
selected neighbor y of x two diagonal helper inputs, one forced to common
0 and the other to common 1 before y's selected last ring. Its fourth,
outer axial input is an arbitrary ordered pair (l,u). Its lower and
upper 1-counts are 1+l and 2+u. The three possibilities are

| Axial pair | Lower/upper counts | Update disagreement probability |
|---|---|---|
| (0,0) | (1,2) | a |
| (0,1) | (1,3) | 2a |
| (1,1) | (2,3) | a |

For k selected receivers this gives a simultaneous success probability
at least aᵏ. Here is the conditional justification. Fix the initial pair,
all clock schedules, a forcing assignment, and all marks other than the
k selected receiver marks. Conditioning the forcing marks into their
intervals leaves those k marks independent uniforms. Reveal them in time
order. By causality, the pre-ring state at each selected ring depends
only on earlier selected marks. Its source is still a disagreement and
its two helpers have their required values, because their selected rings
precede this receiver and they have no later rings. The displayed lower
bound therefore holds conditional on every earlier selected success.
Iterated conditional expectation gives aᵏ. Each selected receiver ring
is its last, so all successes persist to T. Arbitrary dependence through
the outside sites is included in the unrestricted axial inputs.

For e=0 or a=0 the broadcast lower bounds below have zero right side;
the conditional forcing argument is needed only for 0<e<1/2.

First, for each y∈N(x), the preceding blocking estimate is

\[
\mathbb E[D_y\mathbf1_{B_{x,y}}]\ge\frac{e^3}{2}d.             \tag{10}
\]

Take y as source. Require the three other neighbors of x to ring after
r and force their last marks either all to common 0 or all to common 1.
These choices have total probability 2e³. There are n=3 clocks and no
precedence constraints. Equation (9) gives 2e³/(3+1)=e³/2. Use
F={Dᵧ=1}∩Bₓ,ᵧ in (8).

Second, for each specified triple A⊂N(x),

\[
\mathbb E\prod_{y\in A}D_y\ge\frac{17}{1260}e^4a^3d.         \tag{11}
\]

For A={N,E,S} use x as source. In compass notation the four helpers
NW,NE,SE,SW receive alternating common values, either 0,1,0,1 or
1,0,1,0. The selected last ring of each receiver follows those of its
two adjacent helpers. The seven-clock precedence graph is the fence

\[
NW<N>NE<E>SE<S>SW.
\]

The ranks of the times in the displayed order form permutations with
descent set {2,4,6}. Counting permutations with descents allowed only at
chosen cuts, then applying inclusion-exclusion, gives

\[
L=\frac{7!}{2!2!2!1!}
 -\left(\frac{7!}{2!2!3!}+\frac{7!}{2!4!1!}
                         +\frac{7!}{4!2!1!}\right)
 +\binom72+\binom74+\binom76-1
=272.
\]

There are two disjoint helper forcing assignments of probability e⁴
each, and three receiver successes of conditional probability at least
a³. Thus (9) gives 2·272e⁴a³/8!=17e⁴a³/1260. Rotating the
construction treats all four triples; rotation invariance of λ is not
needed.

Third, for a pair A⊂N(x), the preceding bounds are

\[
\mathbb P(E_A)\ge
\begin{cases}
e^5a^2d/15,&A\text{ adjacent},\\
8e^6a^2d/81,&A\text{ opposite}.
\end{cases}                                                    \tag{12}
\]

For an adjacent pair, say {N,E}, use source x and helpers NW,NE,SE.
Their two valid assignments are 0,1,0 and 1,0,1. The two remaining
neighbors S,W are forced to one common value, giving two further
assignments. All seven nonsource sites must ring after r. The helper
and receiver clocks form the five-site fence NW<N>NE<E>SE with
5!/(2!2!1!)−binom(5,2)−binom(5,4)+1=16 orders. The two common
neighbors impose no precedence constraints. Interleaving their clocks
gives L=16·binom(7,5)·2!=672. The forcing marks have total probability
4e⁵, and the two receiver successes contribute a². Thus (9) gives
4·672e⁵a²/8!=e⁵a²/15.

For an opposite pair, say {N,S}, the four helpers NW,NE,SW,SE split
into two independent pairs. Each pair can take either opposite-valued
assignment, giving four choices. The other two compass neighbors E,W
are forced equal with two choices. Thus there are eight assignments of
probability e⁶ each. Each receiver must be last within its group of
three clocks, with probability 1/3 per disjoint group. The other two
clocks are free, so L=8!/9=4480. Equation (9) gives
8e⁶a²·4480/9!=8e⁶a²/81.

In both pair constructions the common compass neighbors are not direct
inputs of the selected receivers. Any influence they have through other
sites is covered by the forcing and arbitrary axial inputs. Their clock
times can be unrestricted. This also applies to the new event below.

## 5. Exactly three disagreements

For a triple A⊂N(x), let

\[
F_A=\{D_y=1\text{ for }y\in A,\ D_w=0
                     \text{ for the unique }w\in N(x)\setminus A\}.
\]

The four events F_A are disjoint and Jₓ=∑_{|A|=3}1_{F_A}. The new bound is

\[
\mathbb P(F_A)\ge\frac{68}{2835}e^5a^3d.                     \tag{13}
\]

For A={N,E,S}, take precisely the source, helpers, receiver constraints
and alternating helper assignments in (11). Add one requirement: the
omitted neighbor W must ring after r and its selected last mark must
force it to a common value, either 0 or 1. There is no constraint between
this ring and the other seven selected rings. Indeed, the input sets at
the receivers are

\[
\begin{aligned}
N &: \{x,NW,NE,2N\},\\
E &: \{x,NE,SE,2E\},\\
S &: \{x,SE,SW,2S\}.
\end{aligned}
\]

Here 2N=x+(0,2), 2E=x+(2,0), and 2S=x+(0,−2).

W is absent from all three. It can affect the outside histories, but
the receiver calculation in Section 4 permits every ordered axial input.
The helpers supply their prescribed values after their last rings,
irrespective of prior histories. The source has no later ring. Thus the
same conditional lower bound a³ holds, even after the selected W mark
has been fixed in its forcing interval.

The helper assignments and the two choices of W's value use distinct
marks. They give four disjoint assignments with probability e⁵ each.
On success the three receivers disagree at T and W is common, so F_A
holds. Eight nonsource sites must ring after r. Each of the 272 allowed
orders on the seven constrained sites admits eight insertions of the
free W clock. Hence

\[
L=8\cdot272=2176,
\qquad \frac{L}{9!}=\frac{17}{2835}.
\]

More explicitly, the success probability conditional on a post-source
disagreement is at least

\[
\exp(-s)(1-\exp(-s))^8\frac{2176}{8!}\,4e^5a^3.
\]

Apply (8), use (5) for the inserted source ring, and let T increase.
The integral contributes 1/9, proving (13). Independently, relative to
the bound (11), this coefficient is multiplied by 2e for the extra
forcing mark and by 8/9 for the extra required clock:

\[
\frac{17}{1260}e^4a^3\cdot 2e\cdot\frac89
=\frac{68}{2835}e^5a^3.
\]

This compares the explicit clock and forcing coefficients. The uniform
conditional transmission estimate in Section 4 applies to both constructions.

Rotation gives (13) for every omitted neighbor. Summing the four target
events yields

\[
\mathbb E J_x\ge\frac{272}{2835}e^5a^3d.                     \tag{14}
\]

## 6. Uniqueness and the numerical threshold

Take expectations in (6). Equations (10)–(12), four triples, four
adjacent pairs, and two opposite pairs give

\[
d\le C_2(e)d-\frac a2\mathbb E J_x.
\]

Using (14) therefore gives d≤C₃(e)d. If C₃(e)<1, d=0. The lattice is
countable, so the stationary ordered pair agrees at every site almost
surely. Its marginals coincide, and (4) proves uniqueness of every
stationary probability measure. Existence was supplied by μ⁻ above.

For the root assertion, on [0,1/4] the factor 4a(1−e³/2) strictly
decreases. Every correction eᵐaⁿ in (2) is nondecreasing there: in the
interior its derivative is

\[
e^{m-1}a^{n-1}(ma-ne),\qquad
ma-ne=m/2-(m+n)e\ge(m-n)/4\ge0.
\]

The exponents are (4,4),(5,3),(6,3),(5,4). Thus C₃ strictly decreases
on [0,1/4], with C₃(0)=2 and C₃(1/4)≤127/128<1. It has a unique
root e₃ there. For e≥1/4 all corrections are nonnegative and
C₃(e)≤4a(1−e³/2)≤127/128<1. This proves the characterization in the
theorem without asserting global monotonicity of C₃.

An independent expansion gives

\[
\begin{aligned}
C_3(e)-1={}&1-4e-e^3+\frac{20143}{10080}e^4-\frac{37}{1620}e^5
 +\frac{1801}{11340}e^6\\
&-\frac{17}{63}e^7+\frac{223}{5670}e^8+\frac{424}{2835}e^9.
\end{aligned}                                                   \tag{15}
\]

Exact rational evaluation of (2) and (15) gives positive and negative
signs respectively at the lower and upper bounds in (3). Their width is
1/154742504910672534362390528. A separate integer polynomial calculation
gives the coarser enclosure

\[
0.248075608046385949<e_3<0.248075608046385950.
\]

Thus e₃≈0.24807560804638594994778149. At the rational endpoint
e=0.24807562, exact arithmetic gives

\[
\begin{aligned}
C_3(e)&=0.999999951438061612953781774988235293\ldots<1,\\
C_2(e)&=1.000000132984221050821350907284113492\ldots>1.
\end{aligned}
\]

The decrease from the preceding threshold is approximately
4.46879407623789879·10⁻⁸. These comparisons prove a strict extension
of the earlier sufficient condition.

The result concerns (1). It gives no conclusion at e=e₃ and no proof of
positive-noise coexistence.
