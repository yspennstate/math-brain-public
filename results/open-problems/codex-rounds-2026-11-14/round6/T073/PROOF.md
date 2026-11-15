# Triple broadcasts with arbitrary common diagonal values

Each site of Z² has an independent rate-one Poisson clock. At a ring,
its new spin is 1 with probability

\[
p_e(k)=(e,e,1/2,1-e,1-e)_k,\qquad 0\le k\le4,                 \tag{1}
\]

where k counts its four nearest neighbors with spin 1. A tie is resampled
fairly, independently of the previous spin. Throughout, 0≤e≤1/2 and
a=1/2−e. Define

\[
\begin{aligned}
P(e)&=\frac{17}{1260}e^4+\frac7{270}e^5
                   +\frac{767}{45360}e^6+\frac{23}{6160}e^7,\\
R(e)&=\frac{68}{2835}e^5+\frac7{150}e^6
                   +\frac{767}{24948}e^7+\frac{23}{3360}e^8,\\
C_4(e)&=4a(1-e^3/2)-\frac4{15}e^5a^3-\frac{16}{81}e^6a^3
                         -2a^4\bigl(P(e)+R(e)\bigr).
\end{aligned}                                                   \tag{2}
\]

**Theorem.** If C₄(e)<1, process (1) has exactly one stationary
probability measure. There is a unique e₄∈(0,1/4) with C₄(e₄)=1;
the sufficient criterion holds exactly for e>e₄ in [0,1/2]. In particular,
uniqueness holds throughout [0.24807553,1/2]. The exact bounds

\[
\frac{38387828333112147431787763}{154742504910672534362390528}
<e_4<
\frac{9596957083278036857946941}{38685626227668133590597632}
                                                               \tag{3}
\]

give e₄≈0.24807552621222013612253301.

The added terms in P and R come from nonalternating diagonal values.
This theorem gives no positive-noise coexistence conclusion.

## 1. Stationary ordered coupling

At every ring use an independent uniform U on [0,1], setting the new
spin to 1 precisely when U≤pₑ(k). The table (1) is nondecreasing in k,
so sharing clocks and marks preserves coordinatewise order η≤ξ.

This construction gives a Feller process on the compact product space
{0,1}^{Z²}. Indeed, backward exploration from a finite set in a bounded
time interval replaces each dependency at a rate-one ring by at most
four dependencies. A dominating branching process has expected population
bounded by its initial size times exp(3t), and finite expected total
number of branchings in a bounded interval. The exploration is almost
surely finite. Truncating to a large finite region therefore approximates
the expectation of each cylinder function uniformly over initial states.
These finite-region expectations are continuous. Cylinder functions
uniformly approximate continuous functions, proving the Feller property.
The same reasoning applies to the ordered pair process.

Let Sₜ be the single-copy semigroup. Attractiveness gives
δ₀Sₜ≤δ₀Sₜ₊ₛ and δ₁Sₜ≥δ₁Sₜ₊ₛ. For any finite set A the
probability that all its spins are 1 consequently converges. These
probabilities determine every cylinder probability by inclusion-exclusion.
Compactness then gives weak limits μ⁻ and μ⁺. Feller continuity and
the semigroup identity imply that both limits are stationary. Both are
translation invariant. Every stationary probability measure ν satisfies

\[
\mu^-\le\nu\le\mu^+,                                        \tag{4}
\]

because δ₀≤ν≤δ₁, and this inequality may be evolved by Sₜ and
passed to the limit. No translation invariance of ν is assumed.

Start the shared-clock ordered pair at (0,1) and average its laws over
[0,T]. Any subsequential weak limit λ is stationary: for every bounded
continuous f, evolving the average law by a fixed duration s changes
its integral by at most 2s‖f‖∞/T. Feller continuity passes this relation
to a weak limit. Its marginals are μ⁻ and μ⁺, because those marginal
laws already converge. Order and translation invariance pass to λ.

Run the pair from λ, independently of future clocks and marks. Put

\[
D_z=\xi_z-\eta_z,\quad d=\mathbb E D_z,\quad
q_x=p_e(K_x(\xi))-p_e(K_x(\eta)),
\]

where Kₓ counts 1-neighbors. Translation invariance makes d independent
of z. At a ring of x the expected new disagreement, conditional on the
pre-ring pair, is qₓ. Applying the generator to Dₓ gives

\[
\mathbb E q_x=d.                                              \tag{5}
\]

## 2. Exact local identity

Let N(x) be the four neighbors of x. Write
Mₓ=∑ᵧ∈N(x)Dᵧ, Tₓ=binom(Mₓ,3), and Jₓ=1_{Mₓ=3}.
Let Bₓ,ᵧ mean that the three sites in N(x)\{y} have the same common
spin in both copies. For each unordered pair A⊂N(x), let E_A mean
that the sites in A disagree, and the other two neighbors are common
and equal. Write Hₓ=∑_{|A|=2}1_{E_A}. Then

\[
q_x=a\left[M_x-\sum_{y\in N(x)}D_y1_{B_{x,y}}
                  -\frac12T_x-H_x-\frac12J_x\right].          \tag{6}
\]

For verification, write pₑ(k)=e+ag(k) with g=(0,0,1,2,2). If Mₓ=0,
both sides vanish. If Mₓ=1, let c count the common 1-neighbors among
the other three sites. The increment g(c+1)−g(c) is 0,1,1,0 for
c=0,1,2,3. The blocked term removes the single disagreement precisely
at c=0 or 3; the other corrections vanish.

If Mₓ≥2, all weighted blocked terms vanish. If Mₓ=2, let c count the
common 1-neighbors among the other two. The increment g(c+2)−g(c)
is 1,2,1 for c=0,1,2. Thus Hₓ removes one exactly at c=0 or 2,
and Tₓ=Jₓ=0. If Mₓ=3, the increment is 2, Hₓ=0 and Tₓ=Jₓ=1,
giving 3−1/2−1/2=2. If Mₓ=4, the increment is 2, Tₓ=4 and
Hₓ=Jₓ=0, giving 4−4/2=2. This proves (6), including a=0.

## 3. Last source rings and forcing

Fix a source v and an observation time T>0. At a source ring r∈(0,T],
write s=T−r and require no source ring after r. Suppose a future
construction succeeds with conditional probability at least

\[
\beta\exp(-s)(1-\exp(-s))^n                                \tag{7}
\]

uniformly over every post-ring history having Dᵥ(r)=1, and success
implies a target event F at T. Pathwise,

\[
1_{F(T)}\ge
\sum_{r\in\mathcal P_v\cap(0,T]}D_v(r)
                         1_{\{\text{construction succeeds from }r\}},
                                                               \tag{8}
\]

since at most one source ring has no later source ring. Insert a
deterministic source ring at r. Its pre-ring pair has law λ, because
insertion changes no past randomness. Its independent mark yields
mean post-ring disagreement E qᵥ=d by (5). Future randomness is
independent of the history and (7) is uniform in that history. The
unit-rate Poisson insertion formula applied to (8) therefore gives

\[
\begin{aligned}
\mathbb P(F)&\ge\beta d\int_0^T\exp(-s)(1-\exp(-s))^n\,ds\\
&=\frac{\beta d}{n+1}(1-\exp(-T))^{n+1}.
\end{aligned}
\]

The left side is independent of T by stationarity. Letting T increase
gives P(F)≥βd/(n+1). If several future constructions for a fixed r
are disjoint, their contributions can first be summed inside (8).
Their numbers n need not agree; apply the integral separately to each.

For n distinct nonsource sites, require each clock to ring after r and
select its last ring before T. This has probability (1−exp(−s))ⁿ.
Conditional on these events, the selected times are independent with
the same continuous distribution. Their relative order is uniform.
If L of their n! orders satisfy the needed precedences, the clock
coefficient after source integration is

\[
\frac{L}{n!}\frac1{n+1}=\frac{L}{(n+1)!}.                   \tag{9}
\]

A mark in [0,e] forces a common 1; a mark in (1−e,1] forces a
common 0. These intervals each have length e and work for every input.
The bounds below need only be proved when 0<e<1/2. At e=0 their
right sides contain a positive power of e and vanish. At e=1/2,
qₓ=0, so (5) gives d=0 and all the bounds are trivial.

## 4. Blocking and pair bounds

The bounds retained from the preceding construction are

\[
\mathbb E[D_y1_{B_{x,y}}]\ge\frac{e^3}{2}d,                 \tag{10}
\]

and

\[
\mathbb P(E_A)\ge
\begin{cases}
e^5a^2d/15,&A\text{ adjacent},\\
8e^6a^2d/81,&A\text{ opposite}.
\end{cases}                                                  \tag{11}
\]

For (10), use y as source and hold its disagreement. Force the other
three neighbors of x at their last rings after r either all to common
0 or all to common 1. There are two disjoint assignments, each with
mark probability e³, and no time constraints. With n=3, (9) gives
2e³/(3+1)=e³/2.

For (11), use x as source. Denote its compass neighbors by N,E,S,W
and its diagonals by NW,NE,SE,SW. A receiver with two diagonal helpers
of opposite common values has the source (0,1), common inputs 0 and 1,
and an arbitrary ordered axial input (l,u). Its lower and upper counts
are 1+l and 2+u. For (l,u)=(0,0),(0,1),(1,1), its update disagreement
probabilities are respectively a,2a,a.

For A={N,E}, force NW,NE,SE to 0,1,0 or 1,0,1, with each helper's
last ring preceding its adjacent receiver's last ring. Force S and W
to the same common value, with two choices. They are not direct inputs
to either receiver, so their clocks impose no precedences. The five
constrained vertices form NW<N>NE<E>SE and have 16 orders. To derive
this fraction independently, condition on two uniform receiver times
u,v. The helper-time probability is uv min(u,v); its integral is
2∫₀¹∫₀ᵛu²v du dv=2/15, hence 5!·2/15=16 orders. Interleaving the
two free clocks gives L=16·binom(7,5)·2!=672. The four forcing
assignments have total probability 4e⁵; the receiver successes have
conditional probability at least a². Formula (9) gives
4e⁵a²·672/8!=e⁵a²/15.

For A={N,S}, use both pairs NW,NE and SW,SE with opposite common
values. There are four diagonal assignments. Force E,W equal, with
two choices. Each receiver must be last within its disjoint group of
three clocks, so the admissible order fraction is 1/9. With n=8,
L=8!/9=4480. Eight forcing assignments give 8e⁶, and (9) gives
8e⁶a²·4480/9!=8e⁶a²/81. Rotation treats every pair.

For the conditional receiver products here and below, fix the initial
pair, all clock schedules, and all randomness except the selected
receiver marks. Condition the required helper marks into their forcing
intervals. The selected receiver marks remain independent uniforms.
Reveal them in chronological order. At a selected ring, causality makes
its pre-ring state depend only on earlier selected marks. Every prescribed
input has already had its forced last ring; the source has no later
ring. The receiver lower bound therefore holds conditional on every
earlier selected success. Iterated conditional expectation gives a² or
a³ as appropriate. The chosen receiver rings are last, so successes
persist to T. This argument permits arbitrary dependence through outside
sites; it asserts no independence of receiver spins.

## 5. All sixteen diagonal assignments

For a specified triple A⊂N(x), let G_A mean that all sites in A
disagree, and F_A mean that exactly the sites in A disagree among
N(x). The improved estimates are

\[
\mathbb P(G_A)\ge a^3P(e)d,\qquad
\mathbb P(F_A)\ge a^3R(e)d.                                  \tag{12}
\]

It suffices to give the construction for A={N,E,S}. Set

\[
(h_0,h_1,h_2,h_3)=(NW,NE,SE,SW),\qquad
(y_0,y_1,y_2)=(N,E,S).
\]

Use x as source. Choose arbitrary diagonal common values
b=(b₀,b₁,b₂,b₃)∈{0,1}⁴ and force them at their last rings after r.
Require hᵢ and hᵢ₊₁ to precede yᵢ. Let

\[
S(b)=\{i\in\{0,1,2\}:b_i=b_{i+1}\},\qquad m=|S(b)|.
\]

For i∈S(b), also force the outer axial site zᵢ=2yᵢ−x to common
1−bᵢ at its last ring after r, and require zᵢ<yᵢ. These axial sites
are distinct from all diagonals, receivers, source, and omitted neighbor.
No other clock precedences are imposed.

If i∉S(b), the receiver calculation in Section 4 gives disagreement
probability at least a for every ordered axial input. If i∈S(b), its
three nonsource inputs are bᵢ,bᵢ,1−bᵢ. If bᵢ=0, its lower/upper
counts are (1,2); if bᵢ=1, they are (2,3). In either case its
disagreement probability is exactly a. The chronological argument at
the end of Section 4 therefore gives simultaneous success probability
at least a³, uniformly over all outside histories. Success implies G_A.

There are n=7+m nonsource sites: four diagonals, three receivers, and
m extra axial helpers. For a fixed S there are exactly two assignments
b: choose b₀ freely and propagate equality when i∈S and inequality
when i∉S. Each assignment uses 4+m forcing marks, giving probability
e^{4+m}. Denote by L_S the number of admissible orders. The contribution
to P is therefore

\[
\frac{2L_S}{(8+m)!}e^{4+m}.                                 \tag{13}
\]

For fixed r, different b prescribe disjoint intervals for at least one
of the same four diagonal last-ring marks. Thus these constructions
are disjoint even though they require different sets of extra axial
clocks. Their probabilities can be added. This disjointness concerns
the construction events, not the target events G_A, which may overlap.

Here are the counts and their independent order probabilities:

| S | m | L_S | L_S/(7+m)! |
|---|---:|---:|---:|
| ∅ | 0 | 272 | 17/315 |
| {0} | 1 | 1582 | 113/2880 |
| {1} | 1 | 1540 | 11/288 |
| {2} | 1 | 1582 | 113/2880 |
| {0,1} | 2 | 10160 | 127/4536 |
| {0,2} | 2 | 10360 | 37/1296 |
| {1,2} | 2 | 10160 | 127/4536 |
| {0,1,2} | 3 | 74520 | 23/1120 |

The counts can be obtained by the following exact recursion. Label the
n vertices and let pred(v) be the set required before v. Set W(∅)=1.
For each subset I and each v∉I with pred(v)⊆I, add W(I) to
W(I∪{v}). Each linear extension gives a unique chain of prefixes,
and each such chain is one linear extension. Thus W(all)=L_S.

An independent integral gives all the fractions in the last column.
Replace the selected times by independent uniforms, which preserves
their uniform relative orders. Conditional on receiver times t₀,t₁,t₂,
the four diagonal precedence probabilities multiply to

\[
t_0t_2\min(t_0,t_1)\min(t_1,t_2).
\]

Each extra axial helper contributes tᵢ. Therefore the order probability is

\[
\int_{[0,1]^3}t_0t_2\min(t_0,t_1)\min(t_1,t_2)
                       \prod_{i\in S}t_i\,dt_0dt_1dt_2.       \tag{14}
\]

To evaluate it, partition the cube into the six orders
t_{π₀}<t_{π₁}<t_{π₂}. Assign each minimum to its earlier receiver.
Let cⱼ be the resulting exponent of t_{πⱼ}, including the endpoint
factors and the extra factors for S. Successive integration on that
simplex gives

\[
\frac1{(c_0+1)(c_0+c_1+2)(c_0+c_1+c_2+3)}.                 \tag{15}
\]

Adding the six rational terms gives the displayed probabilities.
Equations (13)–(15) give the four coefficients of P in (2).

For F_A, additionally require the omitted neighbor W to ring after r
and force its selected last mark to either common value. This is a
free clock vertex. It is absent from all receiver input sets, which are
{x,hᵢ,hᵢ₊₁,zᵢ}. Its effects through outside sites are covered by
arbitrary axial histories, or overwritten by forced axial marks when
those are required. The same a³ conditional bound applies.

The extra clock multiplies the number of orders by n+1, and the
source-integrated clock factor changes from L_S/(n+1)! to
(n+1)L_S/(n+2)!. There are two extra forcing choices. Thus the
contribution (13) is multiplied by

\[
2e\frac{8+m}{9+m}.                                          \tag{16}
\]

For fixed b the two omitted-neighbor choices are disjoint, and different
b remain disjoint at their diagonal marks. Summing (13) with the
factor (16) gives exactly R in (2). In particular, the four grouped
coefficients obey

\[
\begin{aligned}
\frac{17}{1260}\frac{16}{9}&=\frac{68}{2835},&
\frac7{270}\frac{18}{10}&=\frac7{150},\\
\frac{767}{45360}\frac{20}{11}&=\frac{767}{24948},&
\frac{23}{6160}\frac{22}{12}&=\frac{23}{3360}.
\end{aligned}
\]

This proves (12). Rotating the coordinates proves it for all four
triples; rotation invariance of λ is unnecessary.

## 6. Contraction and threshold

The variable Tₓ is the sum of the four indicators 1_{G_A}. The four
events F_A partition {Mₓ=3}, so Jₓ is the sum of their indicators.
Taking expectations in (6), applying (10)–(12), and counting four
adjacent pairs and two opposite pairs gives

\[
\begin{aligned}
d&\le4a(1-e^3/2)d
   -\frac a2\,4a^3P(e)d
   -a\left(\frac4{15}e^5a^2+\frac{16}{81}e^6a^2\right)d
   -\frac a2\,4a^3R(e)d\\
 &=C_4(e)d.
\end{aligned}
\]

The Tₓ and Jₓ terms overlap at Mₓ=3 exactly as prescribed by (6):
each removes half the gap. At Mₓ=4, Jₓ=0 and Tₓ/2=2 removes the
entire gap. No unused gap or disjointness of G_A is assumed.

If C₄(e)<1, this inequality implies d=0. By countability the coupled
copies then agree at every site almost surely. Their marginals coincide,
and (4) proves uniqueness of every stationary probability measure.
Existence was established in Section 1.

On [0,1/4], 4a(1−e³/2) is strictly decreasing. Every subtracted term
in (2) is a positive multiple of eᵐaⁿ with m≥n. In the interior,

\[
\frac{d}{de}(e^ma^n)=e^{m-1}a^{n-1}(m/2-(m+n)e)\ge0,
\]

since m/2−(m+n)e≥(m−n)/4. Thus C₄ strictly decreases there.
At the endpoints C₄(0)=2 and C₄(1/4)≤127/128<1. There is exactly
one root e₄ in this interval. For e≥1/4, all corrections remain
nonnegative and C₄(e)≤4a(1−e³/2)≤127/128<1. This proves the
criterion's characterization without asserting global monotonicity of C₄.

For reproducible exact sign calculations, expanding (2) gives

\[
\begin{aligned}
C_4(e)-1={}&1-4e-e^3+\frac{20143}{10080}e^4-\frac{169}{6480}e^5
 +\frac{106927}{604800}e^6-\frac{5755063}{19958400}e^7\\
&-\frac{561707}{39916800}e^8+\frac{424819}{1663200}e^9
 -\frac{48781}{4989600}e^{10}-\frac{2593}{62370}e^{11}
 -\frac{23}{1680}e^{12}.
\end{aligned}                                                   \tag{17}
\]

Exact rational evaluation of both (2) and (17) gives positive and
negative signs respectively at the lower and upper bounds in (3).
Their width is 1/154742504910672534362390528. An independent integer
polynomial calculation gives

\[
0.248075526212220136<e_4<0.248075526212220137.
\]

Let C₃ denote the preceding criterion, obtained by retaining only the
leading term in P and the leading term in R. Every added coefficient
is positive, so C₄(e)<C₃(e) for 0<e<1/2. At the rational point
e=0.24807553, exact calculation gives

\[
\begin{aligned}
C_4(e)&=0.999999984612015744454758680159985502\ldots<1,\\
C_3(e)&=1.000000317065932486634429222017556278\ldots>1.
\end{aligned}
\]

The threshold decreases by approximately 8.18341658138252485·10⁻⁸
from the previous root 0.24807560804638594994778149. The interval
in the theorem is therefore a strict extension of the preceding one.
There is no conclusion at e=e₄, for retained ties, or for low-noise
coexistence.

## 7. Exact finite checks

Run from this folder:

```
OMP_NUM_THREADS=1 nice -n 15 python3 -I -B verify_previous.py > previous_output.json
OMP_NUM_THREADS=1 nice -n 15 python3 -I -B audit.py > audit_stdout.json
```

The first script independently reconstructs the preceding local identity,
clock constants and exact numerical claims. The second calculates every
entry of the clock table by recursion and by (14)–(15), reconstructs all
four geometries and all sixteen common-diagonal assignments directly from
coordinates, and checks all 384 receiver/input cases. It checks the
free-clock and explicit-source counts, two polynomial constructions,
exact dyadic root bounds, and a separate integer decimal-grid enclosure.
The finite checks support the proof; they do not formally verify its
infinite-volume or conditional-probability arguments.
