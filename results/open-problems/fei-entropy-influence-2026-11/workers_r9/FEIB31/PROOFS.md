# Proofs and failed routes for the monotone good-coordinate question

Task: FEIB31, for the author's 9 Nov 22:20 request to solve the FEI conjecture.
All entropies are in bits. Only coordinates of positive influence enter a minimum.
PROVED means a complete argument below, not a claim of publication priority.

## 1. The question is equivalent to monotone FEI

PROVED. Let C_mon be the supremum of H(f)/I(f) on nonconstant monotone functions.
Then

    C_mon - 2/ln 2 <= G_mon <= C_mon.

For U distributed according to the squared spectrum, E_i is
H(1[i in U] | U minus i). The entropy chain rule, and conditioning reducing entropy,
give sum_i E_i <= H(U). A weighted minimum gives
min_i E_i/Inf_i <= sum_i E_i/I <= H/I. This proves the right inequality.
Conversely, use the step identity in the brief, J_i <= (2/ln 2) Inf_i,
and the corresponding influence identity. At each restriction choose a coordinate
with E_i/Inf_i <= G_mon + epsilon and induct on the number of relevant variables.
Monotonicity survives restrictions. Send epsilon to zero. This proves the left
inequality. No equality between the optimal constants is asserted.

Thus a proof of Question M for all monotone functions would solve their FEI case.
The searches below are lower bounds, not evidence of a finite upper bound.

## 2. An explicit width bound, including unbounded read

PROVED. Every nonconstant width-w DNF has a coordinate with

    E_i/Inf_i <= 2 + log2(e) + log2(2^(w+1) - 1)
              < w + 3 + log2(e).

This also applies to CNFs by complementation. It needs no monotonicity. Tree
induction gives H <= (w + 3 + 3 log2(e)) I. The additive constants, evaluated in
checks.json, are 4.442695040888964 for G and 7.328085122666891 for FEI.
These are rederivations/refinements of the relative-step mechanism already in
FLOW 12(v), not a new claim to bounded-width FEI priority.

Write delta=Inf_i, g=E_i f, h=D_i f and V=Var(f). Split off the empty frequency.
Since |E h| <= E|h|=delta, and the binary entropy inequality
Phi(p,q) <= 2 sqrt(pq), the empty contribution is at most 2 delta.
For the other frequencies, sum p=Var(g) <= V and sum q <= delta. Concavity and
homogeneity of Phi imply

    sum_nonempty Phi(p_T,q_T) <= Phi(V,delta)
      <= delta log2(1+V/delta) + delta/ln 2.

(The last inequality is V ln(1+delta/V) <= delta.) Hence, for every Boolean f,

    E_i/delta <= 2 + log2(e) + log2(1+V/delta).                    (2.1)

Now take one satisfied DNF term with k<=w literals. Order its coordinates.
For every falsifying input, successively set those literals to their satisfying
values. Some first step crosses an edge where f changes. An edge in coordinate
j is reached from at most 2^(j-1) initial inputs. Counting edges gives

    Pr[f=false] <= (1/2) sum_(j=1)^k 2^(j-1) Inf_j
                 <= (2^k-1)/2 max_(j in term) Inf_j.

Thus some coordinate of that term has delta >= 2 Pr[f=false]/(2^k-1).
Since V=4 Pr[f=false] Pr[f=true], V/delta <= 2(2^k-1).
Substitute in (2.1). Restrictions preserve width; the FEI consequence follows
from Section 1's induction. Constants and empty functions need no query.

The binary entropy inequality used above is the elementary scalar bound
h2(t)<=2 sqrt(t(1-t)) on [0,1]; differentiation proves it with equality at 0,1/2,1.
No hypothesis on the signs of Fourier coefficients enters this argument.

## 3. Every leaf of a read-once AND/OR formula is good

PROVED. For every positive-influence leaf i of a read-once AND/OR formula,

    E_i/Inf_i < pi/ln 2.                                       (3.1)

The constant pi/ln 2 is the sharp supremum for a specified leaf over read-once
AND/OR formulas. It is not asserted to be sharp for the best coordinate.
Consequently Question M holds for this class, and tree induction gives
H <= ((pi+2)/ln 2) I. This does not improve the best known local full-split
theorem in the author's FEI19 work. Its point is the smaller bound for the erasure
term alone, at *every* coordinate, including arbitrarily small influences.

A stronger local statement suffices. Start with f_0=x_i, a fair sign, and suppose

    f_l = c_l + (f_(l-1)-c_l) Z_l,    c_l in {-1,+1},

where Z_l is a 0/1 event on a fresh block, independent of all earlier blocks.
Its internal function can be arbitrary. Along the path from a leaf to the root
of a read-once AND/OR formula, Z_l is the event that all siblings permit the leaf
to affect the output. The sibling blocks are disjoint. Constant guards can be
removed or make the leaf irrelevant. Assume 0<p_l=E Z_l<1.

Put P_0=1, P_l=product_(j<=l) p_j, and delta=P_L. Then

    h=D_i f=product_l Z_l,
    g=E_i f=sum_l c_l (1-Z_l) product_(j>l) Z_j.                  (3.2)

Under rho_h, spectral blocks are independent. Block l has law
Z_lhat(S_l)^2/p_l, so it is empty with probability p_l. Let r be the first
nonempty block, counting outwards from the leaf. Its probability is
P_(r-1)(1-p_r)=P_(r-1)-P_r; all blocks are empty with probability delta.
Where hhat is nonzero, division of the two expressions in (3.2) gives

    R_r=ghat/hhat
       =sum_(l<r) c_l(1-p_l)/P_l - c_r/P_(r-1),
    R_empty=sum_l c_l(1-p_l)/P_l.

Therefore the exact answer, with no reference to the internal spectra of the guards, is

    E_i/delta = sum_r (P_(r-1)-P_r) Phi(R_r^2,1)
                 + delta Phi(R_empty^2,1).                     (3.3)

Indeed Phi is homogeneous, and rho_h is q/delta. Frequencies with hhat=0
contribute zero. This is checked against 100 truth tables in audit.py.

The sum (1-p_l)/P_l telescopes to 1/P_l-1. It follows that

    |R_r| <= 2/P_(r-1)-1,     |R_empty| <= 1/delta-1.

For every real R,

    Phi(R^2,1) <= log2(1+R^2)+log2(e),

because R^2 ln(1+1/R^2)<=1. Thus

    Phi(R_r^2,1) <= 2+2 log2(1/P_(r-1))+log2(e),
    Phi(R_empty^2,1) <= 2 log2(1/delta)+log2(e).

Finally, log2(1/t) decreases as t increases, so

    sum_r (P_(r-1)-P_r) log2(1/P_(r-1))
         + delta log2(1/delta)
      <= integral_0^1 log2(1/t) dt = log2(e).

Insert this in (3.3) to get the preliminary bound
2(1-delta)+3 log2(e). The following potential sharpens it to (3.1).

Use logic cofactor probabilities a<=b along the path, d=b-a. They start at
(a,b)=(0,1). A gate with pivotal probability p and blocking logic output e
changes them to a'=e(1-p)+pa, b'=e(1-p)+pb, d'=pd. Set

    alpha=a/d, beta=(1-b)/d, s=1+alpha+beta=1/d,
    F(u)=Phi(u^2,1), f(t)=F(2t+1), t>=0.

An AND gate increases beta with alpha fixed; its contribution in (3.3) is
(d-d')f(alpha). OR interchanges alpha and beta. In either case this equals
the integral of f(the fixed coordinate)/(1+alpha+beta)^2 along the step.
The terminal term in (3.3) is F(beta-alpha)/s.

F is increasing on [0,infinity), and for u>=1

    F''(u) = [2 ln(1+u^-2)-4/(1+u^2)]/ln 2 < 0.

Indeed ln(1+x)<2x/(1+x) for 0<x<=1 (differentiate the difference).
Thus f is increasing and strictly concave on [0,infinity).
For alpha>=beta define

    W(alpha)=integral_alpha^infinity 2 f(t)/(1+2t)^2 dt,
    V(alpha,beta)=f(alpha)[1/s-1/(1+2alpha)]+W(alpha),

and extend symmetrically. Direct differentiation gives

    -V_beta=f(alpha)/s^2,
    -V_alpha=f(alpha)/s^2-f'(alpha)[1/s-1/(1+2alpha)]
              >= f(beta)/s^2.

For the inequality use concavity:
f(alpha)-f(beta)>=f'(alpha)(alpha-beta), and s<=1+2alpha.
The first derivatives match at alpha=beta. Every path charge is therefore at
most the decrease of V. The final charge also fits, because

    V(alpha,beta) >= f(alpha)/s >= F(beta-alpha)/s,

using W(alpha)>=f(alpha)/(1+2alpha) and monotonicity of F.
The first inequality is strict at finite alpha, since f increases. Hence

    E_i/Inf_i < V(0,0) = integral_1^infinity F(u)/u^2 du
                = 2 + (2/ln 2) integral_1^infinity ln(1+u^-2) du
                = pi/ln 2.

The first evaluation is integration by parts; an antiderivative in the last
integral is u ln(1+u^-2)+2 arctan u. This proves (3.1).

For sharpness, take m fresh sibling bits per gate and K=m*2^m alternating
gates. At AND use an OR of those m bits as sibling; at OR use an AND of them.
All pivotal probabilities are q=1-2^-m, and the distinguished leaf has
influence q^K. As m grows, q tends to one, q^K tends to zero, and the midpoint
of the cofactor interval tends to 1/2 uniformly while d stays in [epsilon,1].
The charges on that interval converge to the Riemann integral
integral_epsilon^1 F(1/d) dd. All other charges are nonnegative. First let m
grow, then let epsilon go to zero; the lower limit is pi/ln 2. The upper bound
already proved gives convergence. These are monotone read-once formulas on
1+m^2*2^m variables. class_checks.json records finite values and independently
evaluates the improper integral.

The potential is adapted from the author's FEI19 selector-path argument
(`~/brain/online/frontier_rows/T021/fei19_sharp_pi2_over_2_reserve_floor_2026_11_09/PROOF.md`),
which FEI21 reviewed independently. Their kernel is the full entropy split,
with sharp constant pi^2/2 nats. Our kernel here is Phi(u^2,1), the erasure
cost, whose integral is pi nats. The kernels and constants must not be mixed.
This is an erasure specialization of that established method, not a claim to
inventing the potential or proving read-once FEI for the first time.
Restriction of a read-once AND/OR formula remains in the class.

Known results already cover read-once formulas: CKLS, Theorem 5.11, gives a
Shannon FEI bound with constant 10 over AND/OR/XOR/NOT; O'Donnell--Tan proves
composition over arbitrary bounded-arity gates. See LITERATURE.md. I did not find
the sharp erasure assertion (3.1) in the checked published sections; that is
not a novelty claim. The the author's internal full-split theorem is stronger than
the older published constants for proving FEI itself.

## 4. Largest influence fails, even for monotone functions

PROVED. Let k=2m+1 and choose an m-subset A of k base variables y. Define the
positive DNF

    F(x,y) = [|y|>=m+1] OR (x AND conjunction_(j in A) y_j).

The x-pivotal set is the single point y=1_A, so Inf_x=2^-k. All derivative
coefficients in y have squared magnitude 4^-k. At odd levels s, the majority
coefficients are

    |Maj_khat(S)| = [binom(2m,m)/2^(2m)]
                    * binom(m,(s-1)/2)/binom(2m,s-1).           (4.1)

This follows by differentiating majority: its derivative is the middle slice
on 2m variables, whose Krawtchouk coefficients give (4.1). On uniformly chosen
odd subsets, s=k/2+O(sqrt(k log k)) except for probability o(1). Stirling's
formula makes log2 |Maj_khat(S)|=-k/2+O(log k) uniformly there. The point
perturbation changes each coefficient by at most 2^-k. Consequently

    E_x/Inf_x >= k/2 - O(log k),                                (4.2)

since Phi(r,1)>=log2(1+r). The even levels are nonnegative and can be omitted.

Replace each y_j by a balanced odd majority on mblock fresh variables.
Balanced composition preserves the x erasure cost and influence exactly:
partition a spectral set by the nonempty blocks; both p and q are multiplied
by the same product of inner squared coefficients, whose total is one.
A new leaf has influence Inf_yj(F) alpha_mblock, where
alpha_mblock=binom(mblock-1,(mblock-1)/2)/2^(mblock-1) tends to zero.
For sufficiently large odd mblock, x is the unique largest-influence coordinate,
while (4.2) is unbounded. Composition preserves monotonicity.

CHECKED NUMERICALLY: hidden.json gives k=3,5,...,17, including k=17 ratio
9.269851977533046. It records a sufficient majority block size and its leaf
influence. No truth table of the enormous composed function was allocated.
The construction and its attribution were already present in FLOW 12(u) and
the September memory; this is a rederivation, not a new counterexample.

## 5. Most coordinates can be hidden; simple power weights fail

PROVED. Define one hidden bit z_A for each m-subset A of k=2m+1 base coordinates:

    F(y,z) = [|y|>=m+1]
             OR big_OR_(|A|=m) (z_A AND conjunction_(j in A) y_j).

On the middle layer |y|=m, the output is precisely z_y. Below it the output is
false; above it the output is true. Put r=binom(k,m) and delta=2^-k.
There are r hidden coordinates, all equivalent, with influence delta. The k
base coordinates, also equivalent, have influence r delta: the two adjacent
middle layers each contribute half their boundary edges.

Average over all hidden bits. In sign notation the remaining function a(y)
is +1 below the middle layer, 0 on it, and -1 above it. For each hidden bit,
q_T=4^-k on frequencies supported on y and zero otherwise; p_T=ahat(T)^2 there.
Therefore

    G_hidden = 2^-k sum_(T subset [k]) Phi((2^k ahat(T))^2,1).    (5.1)

For odd |T|=s,

    ahat(T) = (1-s/(k+1)) Maj_khat(T).                          (5.2)

To see this, write L for the lower middle-layer indicator. The Fourier
Laplacian of majority, sum_j y_j D_j Maj, equals (m+1)(L-L(-y)); at an odd
frequency it gives Lhat(T)=s Majhat(T)/(k+1). Since a=Maj-L, (5.2) follows.
Apply the same typical-level estimate as (4.1): G_hidden>=k/2-O(log k).
Thus an asymptotic fraction one of all coordinates can have unbounded cost.
The base coordinates have much larger influence; this is not a counterexample
to the best-coordinate question.

There is also a compact exact expression for a base coordinate. The whole
sign function has Fourier expansion a(y)+sum_A z_A 1[y=A], with no terms
containing two hidden variables. At a base coordinate each hidden sector has
p=q=4^-k and contributes r delta in total. Hence

    E_base/Inf_base = 1 + E_base(a)/(r delta).

This is computed from the same k-bit transform, and checked against the full
cube for k=3,5. In the table it decreases toward two (2.1426634341909123 at
k=17). No asymptotic upper bound for this last expression is needed for the
power-weight counterexample.

The literal OR over all cyclic rotations of the *single*-hidden example in
Section 4 gives the even threshold [total weight>=k/2+1/2]. The majority
terms alone already give that threshold; each added hidden term has the same
width and adds nothing. This simple attempt at transitivity erases the hiding.
The middle-layer construction preserves hiding but has two coordinate orbits.
Neither observation excludes a different transitive counterexample.

PROVED no-go for power weights. Consider the proposed inequality

    sum_i Inf_i^a E_i <= C sum_i Inf_i^(a+1).                   (5.3)

No universal C works, even for monotone f, if a<0 or a>1.
For a<0 use the construction above. The ratio of the base contribution to the
hidden contribution in the denominator is exactly k r^a, tending to zero.
All numerator terms are nonnegative, so the quotient in (5.3) is at least
G_hidden/(1+k r^a), which diverges.
For a>1 use Section 4's single-hidden function and balanced-majority substitution.
Fix k first. The hidden influence and cost stay fixed. The total denominator
weight on new leaves is O_k(mblock^((1-a)/2)); the numerator is at most this
order times O_k(log mblock), by E_j<=h2(Inf_j). Both vanish. The weighted
quotient tends to the hidden coordinate's ratio. Now send k to infinity.
This rules out inverse-influence weights, uniform averaging of the ratios,
and powers above one. It leaves a in [0,1] open; a=0 is the original averaged
monotone FEI statement.

CHECKED NUMERICALLY: hidden_symmetric.json evaluates (5.1) at k=3,5,...,17
without building the enormous full cube. At k=17 there are 24,310 hidden and
17 base coordinates, with hidden ratio 14.451731157696454. The two influences
are 2^-17 and 24310*2^-17. Formula (5.2) and these influences are also checked
at small k in class_checks.py. The asymptotic argument above, not this table,
proves the no-go theorem.

## 6. Two other routes and their limits

PROVED. Put A_i=E_(rho_h) [log2(p/q)]_+. Pointwise

    [log2 r]_+ <= log2(1+r) <= [log2 r]_+ + 1.

Therefore A_i<=Lam_i<=A_i+1, and choosing the coordinate minimizing A_i gives
E_i/Inf_i <= min_j A_j + 1 + log2(e). Boundedness of this minimum is equivalent
to Question M up to this additive constant. The criterion is useful for search,
but is not itself a proof mechanism. selection_checks.json measures it on the
saved candidates.

PROVED. Spectral FKG fails already for the monotone function
F=x_1 OR (x_2 AND x_3). Its squared spectral coefficients are 9/16 at {1} and
1/16 at each of the other seven sets. Thus P[1 in U]=3/4, P[2 in U]=1/4,
but P[1,2 in U]=1/8 < 3/16. This violates even pairwise positive association.
Ordinary FKG still applies to monotone events in input space. It cannot be
transferred to the squared spectral sample without an additional theorem.
checks.json verifies these exact dyadic values.

HEURISTIC limit of the proposed level-inequality route. The bounds for an
indicator's low-level mass see its density and degree. They do not see the
relative signs or alignment of ghat and hhat. The hidden examples satisfy
these bounds while a chosen coordinate's cost diverges. Summing over all
coordinates could exploit compatibility between the boundaries, but the
multiplicity identity sum_(i,T: |T|=l) hhat_i(T)^2=(l+1) W_(l+1)(f)
only counts mass and does not yet supply that compatibility. No finite bound
for a in [0,1] was obtained. This is the unresolved step, not a proved
impossibility theorem for all arguments using level inequalities.

PROVED. The low-influence class I<=K sqrt(log n), for fixed K>0, is not a
restriction-closed escape from the problem. With dummy coordinates allowed,
any fixed monotone f enters the class by increasing n without changing H,
I, or its eligible-coordinate minimum. A uniform Question M bound there is
therefore the full Question M. If n is required to count only relevant variables,
the preceding padding argument no longer proves the assertion for M; that
version is open here. A bound on M for that class alone also cannot be fed into
the tree proof unless restrictions remain in the class.

## 7. Explicit positive DNFs for the tower records

PROVED. Let M be the perfect-matching property on a 3 by 3 matrix of nine bits:

    M(z) = big_OR_(pi in S_3) big_AND_(u=1)^3 z_(u,pi(u)).

Let D(z)=NOT M(NOT z) be its monotone dual. Hall's theorem, or checking the
512 inputs, gives this positive DNF for D: the OR of the six row/column stars
of size three and the nine 2 by 2 rectangles of size four. Integer masks in
row-major order are in checks.json. The stars isolate a vertex in the
complement; a rectangle is a two-vertex Hall obstruction. These exhaust the
minimal obstructions in a 3 by 3 bipartite graph.

Define T_s to be the OR of s disjoint pairs, a positive DNF. Its dual Q_s has
positive DNF

    Q_s(z) = big_OR_(epsilon in {0,1}^s)
                big_AND_(j=1)^s z_(2j-1+epsilon_j).

For the mixed record also use P, perfect matching on a 4 by 4 matrix:
P(z)=OR_(pi in S_4) AND_(u=1)^4 z_(u,pi(u)). For general tribes write
T_(w,s)=OR_(j=1)^s AND_(l=1)^w z_(w(j-1)+l). Its monotone dual has positive
DNF OR_(l_1,...,l_s in [w]) AND_(j=1)^s z_(w(j-1)+l_j).
Perfect matching on K4 is the OR of the three pairs of opposite edges;
its dual is consequently Q_3 after that explicit edge permutation.

A word of these gates means composition on disjoint, identical copies of the
inner function, reading from bottom to top and starting from a single variable.
Distributing AND over OR is a precise recursive DNF specification; no expansion
of the giant term list is necessary. Each gate is transitive on its inputs,
so the iterated wreath action is transitive on leaves. All coordinates have
the same E and influence. Every gate and hence the whole function is monotone.

For the old record the word is M,D,D,M,M,D,D. The function has 9^7 leaves.
For an arbitrary signed level word s_1 M,...,s_L M, the orientation at every
leaf is product s_l. Put t_l=product_(j<=l) s_j and multiply level l's output
by t_l. Its new gate is M if t_(l-1)=+1 and D if t_(l-1)=-1. This proves the
conversion and preserves the final squared spectrum, even if a final output
complement is needed.

The largest certified mixed word, bottom to top, is

    M,D,D,D,D,M,P,P,P,Q_2,dual(PM(K4)),dual(T_(4,3)),T_(2,6),T_(3,5).

It has 112844396298240 variables, and G is in
(4.50640064551556,4.50640064551558). The complete directed interval, exact
gate masks and every intermediate state are in record_certificate.json.
That file also retains close shorter contenders; the value here is their
largest certified value, not a global optimum claim. All these are positive
DNFs by the grammar above. The certificates use
the following composition identity, independently checked against truth tables.
With inner mean c, singleton squared coefficient a, coordinate cost e and
influence d, let t=1-c^2 and

    K_A(c)=sum_(B superset A) Fhat(B) c^(|B minus A|).

For the coordinate in block 1,

    d_new = d sum_(A not containing 1) t^|A| K_(A+1)^2,
    e_new = sum_A t^|A| [Phi(K_A^2,K_(A+1)^2 a)
                          + K_(A+1)^2(e-Phi(c^2,a))],
    c_new=K_empty,       a_new=K_{1}^2 a.

Expand the Fourier polynomial block by block: for a spectral set meeting
precisely blocks A its coefficient is K_A times the product of the nonempty
inner coefficients. Other blocks sum to t^|A|. Within block 1 every nonempty
pair contributes its old erasure cost times K_(A+1)^2; the empty pair is the
Phi expression displayed above. This proves the identity. In a monotone
transitive composition a=d^2, a useful independent check on every level.
