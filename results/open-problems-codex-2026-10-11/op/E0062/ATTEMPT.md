# E0062 — research attempt, 2026-10-12

Final mathematical results in this attempt:

- Every acyclic sign graph gives convergent trajectories, with zeros allowed.
- With no zero off-diagonal entries, the every-point ergodic theorem holds
  exactly for acyclic sign tournaments (using the published triangle theorem).
- A chordless four-cycle converges from every point if a−b−ab≥0 and
  c−d−cd≥0, with all four coefficients in (0,1].
- A chordless four-cycle with ac=bd and all coefficients in (0,1] has
  divergent averages at EVERY nonfixed interior point.
- The two preceding families give a proved pair with identical signs and
  zeros but opposite ergodic behaviour. Independent blocks extend these
  examples to higher dimensions.

The full arbitrary-matrix criterion is NOT proved. Verification scope and
the precise unresolved cases are recorded in Sections 8, 9 and 11.
All assertions of divergence refer to failure of the vector Cesàro limit
asked for in Problem 5.

## Exact question and source

Ganikhodzhaev and Rozikov, arXiv:0902.4207v2 (12 March 2009), PDF p. 4, Problem 5:
“Find necessary and sufficient conditions on matrix A of Volterra QSO under
which the ergodic theorem is true for the Volterra QSO on S^{m−1}, m ≥ 2.”
The operator is (7), PDF p. 2:
V_A(x)_i = x_i(1 + Σ_j a_ij x_j), where A^T = −A and |a_ij| ≤ 1.
The question concerns convergence of n^{-1} Σ_{k=0}^{n−1} V_A^k(x) for EVERY
x in the CLOSED simplex. No transversality assumption occurs in Problem 5.
The extracted text of the preceding source sentence omits a normalization
in its displayed description of Ulam's conjecture; we use the normalized
averages requested by the problem, consistent with the source's
historic-behavior definition. This is not a claim that the PDF itself has
a typographical error.

## 1. Acyclic sign graph: convergence of every trajectory (complete proof)

Define the directed graph G_A by i → j precisely when a_ij > 0 (winner → loser).
Zeros give no edge. Suppose G_A is acyclic. A finite acyclic directed graph
admits an ordering in which every arrow goes forward: if no vertex had
indegree zero, repeatedly following incoming edges would repeat a vertex,
creating a directed cycle. Remove an indegree-zero vertex and repeat.
After this permutation, a_ij ≥ 0 for i < j.

First V preserves the simplex. For x in the simplex,
1+(Ax)_i ≥ 1−Σ_{j≠i}x_j = x_i ≥ 0, so V_i(x) ≥ 0.
Also Σ_i V_i(x) = Σ_i x_i + Σ_ij a_ij x_i x_j = 1, because each
unordered pair cancels and each diagonal coefficient is zero. In particular,
if x_i=0 then V_i(x)=0; every face is invariant.

Write x(n)=V^n(x), and P_r(n)=Σ_{i≤r}x_i(n), for 1≤r<m.
The exact identity is

P_r(n+1)−P_r(n) = Σ_{i≤r<j} a_ij x_i(n)x_j(n) ≥ 0.

Indeed all terms with both indices ≤r cancel in pairs; the remaining terms
are exactly those displayed. Each P_r lies in [0,1], hence converges to a
number L_r. Put L_0=0 and L_m=1. Since
x_i(n)=P_i(n)−P_{i−1}(n), every coordinate converges to L_i−L_{i−1}.
The limit q is in the simplex. Continuity of the polynomial map and
x(n+1)=V(x(n)) imply q=V(q).

Convergence of the trajectory implies convergence of its Cesàro averages:
given ε>0, choose N so that |x_i(k)−q_i|<ε for k≥N. Then for n>N,
|n^{-1}Σ_{k<n}x_i(k)−q_i| ≤ n^{-1}Σ_{k<N}|x_i(k)−q_i|+ε,
whose upper limit is ≤ε. Let ε tend to zero, coordinate by coordinate.
This proof includes all zero entries, boundary points, and coefficients ±1.

There is also the exact finite bound
Σ_{n≥0} Σ_{i≤r<j}a_ij x_i(n)x_j(n) = L_r−P_r(0) ≤ 1.
For any edge i→j in the ordering, use r=i to conclude
Σ_n x_i(n)x_j(n) ≤ 1/a_ij. Thus q_i q_j=0 whenever a_ij≠0.
The limit's support is an independent set of G_A; conversely any point
supported on an independent set is fixed.

## 2. Heredity to faces and the directed-triangle obstruction

For a nonempty subset I, the face x_j=0 for j∉I is invariant by the formula.
Identifying its coordinates with a simplex, its restriction is exactly the
Volterra operator for the principal submatrix A_I. Consequently the property
“all initial points have convergent averages” for A implies it for every A_I.
Conversely, failure on one principal face gives failure for A, by inserting
zero coordinates in a witnessing trajectory and its averages.

Suppose i→j→k→i is a directed triangle. On its face, relabel x=x_i,
y=x_j,z=x_k. Its coefficients in source (9) are
a=a_ij>0, c=a_jk>0, b=a_ki>0. Thus source Theorem 3 (PDF p. 4)
applies and says this face operator fails the ergodic theorem. The face
argument implies failure for A. This is a rigorous reduction using the
published three-species theorem, NOT a new self-contained proof of that
theorem. Its statement and reference are recorded in LITERATURE.md.

## 3. Full characterization when every off-diagonal entry is nonzero

In this case G_A is a tournament. If it has no directed triangle, it has no
directed cycle: choose a shortest directed cycle v_1→v_2→…→v_l→v_1.
If l=3 we are done. If l≥4, the chord v_1,v_3 exists. If v_3→v_1,
v_1,v_2,v_3 form a triangle. If v_1→v_3, replacing the first two
edges by this chord gives a shorter directed cycle, a contradiction.
Therefore no directed triangle implies acyclicity.

Combining Sections 1 and 2 proves, under the nonzero-entry hypothesis:
the ergodic theorem for every point holds IF AND ONLY IF G_A is acyclic,
equivalently A can be permuted so that a_ij>0 for every i<j.
It also proves the full two-species case (acyclic automatically) and
three-species case (the only possible cycle is a triangle), including zeros.
This is a special case of E0062, not a solution to its zero-entry case.

## 4. Initial remaining gap

When zeros occur, a directed graph without directed triangles may contain
longer directed cycles. Example:
A = [[0,a,0,−d],[−a,0,b,0],[0,−b,0,c],[d,0,−c,0]],
where a,b,c,d>0. Its graph is the chordless cycle 1→2→3→4→1.
Neither Section 1 nor Section 2 decides its ergodicity.
Its determinant is (ac−bd)^2. When ac=bd it has positive kernel vectors;
when ac≠bd it has no interior fixed point. These observations alone prove
neither convergence nor nonconvergence of time averages.
For completeness, expand the determinant along the first row. The two
nonzero cofactors involve minors −c(ac−bd) and −b(ac−bd), giving
det(A)=ac(ac−bd)−bd(ac−bd)=(ac−bd)². If ac=bd, take any x_1,x_4>0,
put x_2=(d/a)x_4 and x_3=(a/b)x_1, and normalize their positive sum.
All four entries of Ax are zero. If ac≠bd, A is invertible and no positive
vector can satisfy Ax=0, which is necessary for an interior fixed point.

The earlier intake's proposed interior-optimal-strategy criterion is not
valid as stated: the positive cyclic three-species matrix has a positive
kernel equilibrium and fails the ergodic theorem by source Theorem 3.
The continuous-time identity d(log x_i)/dt=(Ax)_i is unavailable here;
the discrete identity is log x_i(n+1)−log x_i(n)=log(1+(Ax(n))_i).
Its quadratic error cannot be discarded without a proved bound.

## Referee checks (in progress)

Check the prefix identity without presuming strict signs; check faces with
zero coordinates; check ordering's orientation; never infer convergence
from approach to a continuum of fixed points. Numerical cyclic orbits must
retain extremely small positive coordinates: ordinary floating-point
underflow can create false convergence to a boundary vertex. Formalization
and experiments will be appended below when completed.

## 5. New proved cyclic family with zero entries: strong alternating dominance

For the four-cycle matrix in Section 4, assume 0<a,b,c,d≤1 and

a−b−ab>0, and c−d−cd>0.                      (D)

Then EVERY trajectory converges, so the ergodic theorem holds on the entire
closed simplex, although the sign graph has a directed cycle.

Proof. If an initial coordinate is zero, the trajectory stays in a proper
face. Every proper induced subgraph of this chordless four-cycle is acyclic,
so Section 1 gives convergence. It remains to consider x_i(0)>0 for all i.
The simplex estimate in Section 1 gives x_i(n+1)≥x_i(n)^2>0, so positivity
persists even if a coefficient equals one.

Set P_n=x_1(n)x_3(n), u_n=x_2(n), v_n=x_4(n), t_n=u_n+v_n, and
κ=min(a−b−ab,c−d−cd)>0. Direct expansion gives

P_{n+1}/P_n−1
 = (a−b)u_n+(c−d)v_n−ab u_n²−cd v_n²+(ac+bd)u_nv_n
 = (a−b−ab)u_n+(c−d−cd)v_n
   +ab u_n(1−u_n)+cd v_n(1−v_n)+(ac+bd)u_nv_n
 ≥ κ t_n.

All discarded terms are nonnegative because u_n,v_n∈[0,1] and all four
parameters are positive. Therefore P_n is nondecreasing and P_n≥P_0>0.
Also P_n≤1/4, since 4x_1x_3≤(x_1+x_3)²≤1. Summing
P_{n+1}−P_n≥κP_0 t_n from n=0 to N−1 yields

Σ_{n=0}^{N−1}t_n ≤ (1/4−P_0)/(κP_0).

Thus Σ_n t_n<∞ and t_n→0. Moreover
|x_1(n+1)−x_1(n)| = x_1(n)|a u_n−d v_n| ≤ t_n,
|x_3(n+1)−x_3(n)| = x_3(n)|−b u_n+c v_n| ≤ t_n,
using a,b,c,d≤1 and x_1,x_3≤1. For M>N the difference of either winner's
coordinates is at most Σ_{n=N}^{M−1}t_n, whose supremum tends to zero.
Hence x_1 and x_3 are Cauchy sequences of real numbers and have limits.
The other coordinates tend to zero. The trajectory converges to a point
(q_1,0,q_3,0) with q_1+q_3=1 and q_1q_3≥P_0>0. That entire edge is
fixed because a_13=0. Cesàro convergence follows from Section 1. QED.

For an exact rational example take a=c=9/10, b=d=1/10. Then
a−b−ab=c−d−cd=71/100>0. This is a PROVED example of an operator
whose directed sign graph contains a cycle and whose averages converge for
every point. The previous repository memo only provided numerical evidence
for this example; the product inequality above supplies the missing proof.
The numerical case (a,b,c,d)=(.8,.3,.7,.4) also satisfies (D), with κ=.02.

Condition (D) is sufficient only. Failure of (D), existence of an interior
fixed point, or a boundary cycle by itself is not established here as a
necessary or sufficient condition for nonergodicity.

### 5a. The equality cases also converge (complete refinement)

The two strict inequalities in (D) can both be weakened to
a−b−ab≥0 and c−d−cd≥0, with a,b,c,d still positive. For an interior
initial point P_0>0, the expansion above first gives P_n≥P_0. Put
s_n=x_1(n)+x_3(n). Since x_3(n)≤1,
s_n≥x_1(n)≥P_n≥P_0. Also 1−u_n≥s_n and 1−v_n≥s_n.
Consequently the discarded remainder itself is at least

ab u_n(1−u_n)+cd v_n(1−v_n)
 ≥ min(ab,cd) P_0 (u_n+v_n).

The whole increment therefore satisfies
P_{n+1}−P_n≥min(ab,cd)P_0² t_n, where the constant is strictly positive.
Summing gives Σ_n t_n≤(1/4−P_0)/(min(ab,cd)P_0²). The Cauchy
argument and the proper-face argument of Section 5 apply verbatim.
For example a=c=1,b=d=1/2 satisfies the equality conditions and is regular.
These weakened inequalities are still only sufficient conditions.

For every interior initial point in this family the limit obeys
d/c ≤ q_3/q_1 ≤ a/b. Indeed if −a q_1+b q_3>0, then for all sufficiently
large n the multiplier of the positive coordinate x_2(n) is ≥1+ε for
some ε>0, contradicting x_2(n)→0. The same argument applied to x_4
gives d q_1−c q_3≤0. Both q_1,q_3 are positive because their product is
at least P_0, so division is legitimate. No strict endpoint exclusion is
asserted.

## 6. Read-only comparison with prior attempts

Read origin/master:prob1000_lean_20260908/ultracode_20260909/E0062/memo.md
in ~/math-open-problems. It already proved the nonzero-entry
case using the same triangle-face obstruction, and computed log-coordinate
four-cycle orbits. Its statements that a sign-only criterion cannot work
relied on numerical evidence, not a proof of opposite behaviours. We use
none of its return-map estimates as proved results. Its proposed
continuous-time equilibrium analogy was rejected earlier, as Section 4
explains. Our new theorem proves convergence for its strongly asymmetric
example. The earlier memo lacked a rigorous balanced-cycle nonergodicity
proof; Section 10 below now proves
nonergodicity of the symmetric balanced cycle for 0<α<1.

## 7. Arbitrary-dimensional cyclic examples by independent blocks

Suppose, after a permutation, A is block diagonal and each block is either
acyclic in its sign graph or a four-cycle satisfying the nonstrict conditions
of Section 5a (possibly after relabelling). Then every trajectory converges
for every initial point in the full simplex.

Proof. For a block B, let s_B(n)=Σ_{i∈B}x_i(n). Cross-block coefficients
vanish. The within-block skew terms cancel, so s_B(n+1)=s_B(n)=s_B.
If s_B=0 all those coordinates vanish forever. If s_B>0, put
y_i(n)=x_i(n)/s_B for i∈B. Then Σ_{i∈B}y_i=1 and
y_i(n+1)=y_i(n)(1+Σ_{j∈B}s_B a_ij y_j(n)).
Thus the normalized block evolves under the Volterra matrix s_B A_B.
An acyclic sign graph remains acyclic after positive scaling. For a cyclic
block the scaled parameters a'=s_B a, b'=s_B b, c'=s_B c, d'=s_B d
belong to (0,1], and
a'−b'−a'b'=s_B(a−b−s_B ab)≥s_B(a−b−ab)≥0,
c'−d'−c'd'=s_B(c−d−s_B cd)≥s_B(c−d−cd)≥0,
since 0<s_B≤1. Section 5a gives convergence of y(n), hence of the original
block coordinates. There are finitely many blocks, so the whole trajectory
converges. QED. This supplies certified cyclic matrices in arbitrary larger
dimensions, but is not a criterion for arbitrary matrices with couplings.

## 8. Referee computations and reproducibility

### Balanced-four-cycle reduction (proved; does not prove average divergence)

For a=b=c=d=α∈(0,1], every nonfixed interior trajectory satisfies
x_1(n)x_3(n)→0 and x_2(n)x_4(n)→0. Hence every accumulation point lies
in the union of the four adjacent edges {1,2},{2,3},{3,4},{4,1}.

Proof. Put P_n=x_1x_3, Q_n=x_2x_4, u_n=x_1−x_3, v_n=x_2−x_4,
s_n=x_1+x_3. Directly from the update,
P_{n+1}=P_n(1−α²v_n²), Q_{n+1}=Q_n(1−α²u_n²),
u_{n+1}=u_n+αs_nv_n. Thus P,Q are nonnegative nonincreasing and have
limits P_*,Q_*. Coordinates stay strictly positive at every finite time.

Suppose both limits are positive. Telescoping the two product decrements
shows Σ_n v_n²<∞ and Σ_n u_n²<∞, since P_n≥P_*>0 and Q_n≥Q_*>0.
Therefore u_n,v_n→0. The identities s_n²=u_n²+4P_n and
(1−s_n)²=v_n²+4Q_n imply s_n→2√P_* and 1−s_n→2√Q_*.
Thus 2√P_*+2√Q_*=1. But at time zero, AM–GM gives
2√P_0+2√Q_0≤s_0+(1−s_0)=1. A nonfixed interior point has
u_0≠0 or v_0≠0: otherwise all four payoffs vanish and it is fixed.
If v_0≠0 then P_1<P_0; if u_0≠0 then Q_1<Q_0. Since both products
are positive initially and neither increases, this yields
2√P_*+2√Q_*<2√P_0+2√Q_0≤1, a contradiction.

Suppose P_*>0,Q_*=0. The decrement of P again gives v_n→0. Hence
(x_2+x_4)²=v_n²+4Q_n→0, so x_2,x_4→0 and s_n→1.
Now u_n²=s_n²−4P_n→1−4P_*>0. Strict positivity of x_2(0)+x_4(0)
gives P_*≤P_0≤s_0²/4<1/4, justifying the strict inequality.
Let h=√(1−4P_*)>0. Eventually |u_n|≥h/2, whereas
u_{n+1}−u_n=αs_nv_n→0. An eventual sign change would require a jump
of size at least h, so there are no such changes. Thus u_n converges to
either h or −h. If the limit is h>0, then
x_4(n+1)=x_4(n)(1+αu_n)≥x_4(n)(1+αh/2) eventually,
contradicting x_4(n)→0 and x_4(n)>0. If the limit is −h, the same
argument with x_2(n+1)=x_2(n)(1−αu_n) contradicts x_2(n)→0.
Thus this case is impossible. Interchanging opposite pairs rules out
P_*=0,Q_*>0. Both limits are therefore zero. Their continuous zero set
in the simplex is exactly the adjacent-edge union stated. QED.

This reduction alone proves neither convergence nor divergence of the
averages. Section 10 supplies a different argument for divergence when
0<α<1; no residence-time or return-map estimate is asserted here.

All scripts and outputs stay in this folder. No experiment is used as a
proof of infinite-time nonergodicity.

- experiments.py: six trajectories, each 100,000 steps, at most four
  coordinates; one case at a time, each under 100 seconds in the recorded
  run. Stores log coordinates, reconstructs x by normalized exponentials,
  updates logs with log1p((Ax)_i), and renormalizes. Stored logs retain very
  small species even when reconstruction rounds their masses to zero.
  Parameters are below one, so computed growth factors stay bounded away
  from zero and log1p is well-defined. See experiments.json for all inputs,
  times, states, average snapshots and smallest logs. Resident states that
  round to vertices do not prove convergence; those species may reappear.
- For the proved cyclic case (a,b,c,d)=(.8,.3,.7,.4), starting at
  (.1,.2,.3,.4), the n=100000 state is approximately
  (.558870240,0,.441129760,0); the means are
  (.558841102,.000033509,.441104742,.000020648). This agrees with the proof.
- For the balanced case a=b=c=d=.6, the means at n=50000 and 100000
  are approximately (.198647,.427712,.153982,.219658) and
  (.149826,.213856,.219703,.416616). The substantial movement supports
  persistent oscillation but does not prove it. The cyclic-three-species
  control also has moving means, consistent with the published obstruction.
- The same script checks the prefix identity and simplex preservation
  using exact fractions for all 729 upper-triangular patterns in
  {0,1/2,1}^6 and all three cuts of a four-species simplex. All passed.
- exact_checks.py: 81 parameter quadruples satisfying the strict four-cycle
  inequalities, each at all 286 denominator-ten simplex points. All 23,166
  exact rational checks passed, including boundary points and coefficient
  one. Checks the product identity, its lower bound, simplex preservation,
  winner-increment bounds, and P≤1/4. Result: exact_checks.json.
- equality_checks.py: all 858 exact rational checks passed at three equality
  parameter quadruples and all 286 denominator-ten simplex points. Result:
  equality_checks.json. These finite checks validate
  formulas and boundary inequalities, not the analytic convergence proof.
- Prefix.lean uses selective Mathlib imports and only ring, positivity,
  norm_num, linarith and ordinary order reasoning. It contains no sorry or
  native_decide. The command is lake env lean <absolute path to Prefix.lean>,
  run from ~/lean_verify. As of this entry it is waiting for
  the shared checker slot. Nothing is called Lean-checked until it exits
  successfully. The formalized objects are algebraic lemmas, not the entire
  convergence theorem.

## 9. Precise final mathematical gap

We have NOT obtained necessary and sufficient conditions for arbitrary
skew-symmetric A with zero entries. The proved triangle obstruction,
the sufficient families above, and the balanced-cycle theorem below leave
undecided, for example, a=c=.5,b=d=.4 on the chordless four-cycle. In general,
triangle-free cyclic graphs, interacting cyclic blocks, and parameter
regimes outside the product inequalities remain unclassified here.
The entire weighted balance region ac=bd with 0<a,b,c,d≤1 is now
classified as nonergodic for all nonfixed interior points in Section 14.
Whether every ergodic Volterra matrix must actually have convergent
trajectories is also not proved here. Literature coverage is bounded, and
recent inaccessible degenerate-system papers remain leads; no universal
unsolved-status assertion or novelty assertion is made.

## 10. Balanced-four-cycle nonergodicity (complete proof, 0<α<1)

Theorem. For a=b=c=d=α∈(0,1), every nonfixed interior initial point has
NONCONVERGENT coordinate Cesàro averages. The fixed interior points are
exactly x_1=x_3 and x_2=x_4. Every boundary trajectory converges by Section 1.

We use two standard compact-space measure facts: probability measures on a
compact metric space are sequentially compact for weak convergence; and
equality of their integrals against all continuous functions is equality
of the measures, hence also equality of all bounded Borel integrals.
These are the ordinary weak compactness and uniqueness theorems for
probability measures; the dynamical applications are proved explicitly next.

Let x(n)=V^n(x(0)) be nonfixed and interior, and
μ_n=n^{-1}Σ_{k=0}^{n−1}δ_{x(k)}. By Section 8, every accumulation point of
x(n) lies in the closed adjacent-edge network K. Compactness then implies
dist(x(n),K)→0: a subsequence a fixed positive distance away would have an
accumulation point outside K. For any weakly convergent subsequence of μ_n
with limit μ, its integral of the continuous nonnegative function
dist(·,K) is zero, by Cesàro regularity. Therefore μ(K)=1.

For any continuous f on the simplex,
∫(f∘V−f)dμ_n = (f(x(n))−f(x(0)))/n→0,
since f is bounded. Taking the weak limit, using continuity of V,
gives ∫f∘V dμ=∫f dμ. Uniqueness against continuous functions says
V_*μ=μ, so μ is invariant, including for bounded Borel test functions.

Each relative open edge E of K is mapped into itself and has no preimages
in K outside E. To check this, V fixes the vertices and preserves every
two-species face; on an interacting edge the winner's mass t∈(0,1)
updates to t'=t+αt(1−t)∈(0,1). The losing mass is
(1−t)(1−αt)>0. The other three open edges and vertices stay in their own
parts, so they cannot enter E. Define the bounded Borel function φ_E on K
to equal t on E and zero on K\E (extend it by zero outside K). Then
φ_E(Vz)−φ_E(z)=αt(1−t)>0 on E and is zero on K\E.
Invariance and μ(K)=1 imply the integral of this nonnegative function is
zero. As it is strictly positive at every point of E, μ(E)=0: E is the
countable union of sets where the function is at least 1/r. Applying this
to all four edges shows μ is supported on the four vertices.

Suppose for contradiction that the coordinate averages converge to q.
Every weak cluster measure μ is supported on the vertices, and its ith
coordinate integral is q_i. Thus μ=Σ_i q_i δ_{e_i}. All cluster measures
are identical, so μ_n converges weakly to this measure: otherwise a
subsequence outside some neighborhood of it would have a different weak
cluster point by compactness.

Let g=log(1+α)>0 and h=−log(1−α)>0. We have h>g since
h−g=−log(1−α²)>0. All growth factors 1+(Ax)_i lie in [1−α,1+α], so
F_i(x)=log(1+(Ax)_i) is continuous on the entire simplex. The exact
logarithmic iteration identity and weak convergence give

lim_n log x_i(n)/n = ∫F_i d(Σ_jq_jδ_{e_j}) = λ_i,

where
λ_1=gq_2−hq_4, λ_2=gq_3−hq_1,
λ_3=gq_4−hq_2, λ_4=gq_1−hq_3.
The initial log divided by n vanishes. Because x_i(n)≤1, λ_i≤0.
If λ_i<0, eventually x_i(n)≤exp(λ_i n/2), so Σ_n x_i(n)<∞,
and its Cesàro average q_i=0. Consequently q_iλ_i=0 for every i.

The exact algebraic identity
Σ_i q_iλ_i = (g−h)(q_1q_2+q_2q_3+q_3q_4+q_4q_1)
now implies every adjacent product is zero, since g−h<0 and q_i≥0.
Thus supp(q) is an independent set of the four-cycle. It cannot be a
single vertex: at q=e_1 the rate λ_4=g>0 contradicts λ_4≤0, and cyclic
relabeling covers the other vertices. Since Σ_iq_i=1, the support must be
exactly one of the two opposite pairs.

Consider first q_1,q_3>0, q_2=q_4=0. Then
λ_2+λ_4=(g−h)(q_1+q_3)=g−h<0, so at least one of λ_2,λ_4 is negative.
If λ_4<0, then Σ_n x_4(n)<∞. The coordinate changes are
Δx_1=αx_1(x_2−x_4), Δx_3=αx_3(x_4−x_2).
The negative part of Δx_1 is at most αx_4, and the positive part of Δx_3
is at most αx_4. Both relevant parts are summable.

For completeness, any bounded real sequence whose positive OR negative
increment parts are summable converges. Write its increment as p_n−r_n
with p_n,r_n≥0. If Σr_n<∞, then
Σ_{k<N}p_k=y_N−y_0+Σ_{k<N}r_k is bounded above by boundedness of y_N;
its nondecreasing partial sums thus converge. Hence Σp_n<∞ also, the
total variation is finite, and the sequence is Cauchy. The other case
is obtained by applying this argument to −y. This proves that x_1(n)
and x_3(n) converge. Their limits equal their Cesàro limits q_1,q_3>0.
Therefore P_n=x_1(n)x_3(n)→q_1q_3>0, contradicting Section 8.

If instead λ_2<0, Σ_n x_2(n)<∞; the positive part of Δx_1 and the
negative part of Δx_3 are bounded by αx_2. The same bounded-variation
argument gives the same contradiction. If supp(q)={2,4}, a cyclic
relabeling of the four indices interchanges the opposite pairs and repeats
the entire argument, with Q_n→0 supplying the contradiction. These exhaust
all possible q. No Cesàro limit exists. QED.

The restriction α<1 is used only for bounded continuity of logarithmic
growth factors. We do not claim this proof covers α=1.

Corollary: the sign pattern alone cannot characterize E0062 when zeros are
allowed. The exact matrices A(1/2,1/2,1/2,1/2) and
A(9/10,1/10,9/10,1/10) have identical signs and zeros. The first fails
ergodicity by this theorem, e.g. from (1/10,2/10,3/10,4/10), which is not
fixed. The second has convergent trajectories for EVERY point by Section 5.
This is now a proved pair, rather than the numerical pair in the old memo.

## 11. Hostile referee audit of the new nonergodicity argument

1. A weak limit on the boundary need not be supported on vertices. Here
   the support was first reduced to the adjacent-edge network by two exact
   product limits, and every invariant measure on each open edge was then
   excluded by a strictly positive Borel coboundary. No transversality or
   finite-fixed-set assertion is assumed.
2. The edge test function is discontinuous at vertices. It is used only
   AFTER invariance has been established as equality of measures by
   continuous tests, which legitimately implies bounded Borel invariance.
3. Convergent coordinate averages do not usually imply convergence of
   empirical measures. Here all weak cluster measures are vertex-supported,
   and their vertex weights equal the coordinate averages. This explicitly
   supplies the missing uniqueness implication.
4. The logarithm is not uniformly bounded when coefficients attain one.
   The continuous-log proof in Section 10 is restricted to 0<α<1;
   Sections 13–14 use clipped logarithms to cover coefficient one. The
   separate convergence theorem includes coefficient one without logs.
5. One missing-species growth rate can be zero. The proof requires only
   ONE strictly negative rate. Its exponential decay makes one-sided
   variation of BOTH surviving coordinates summable, sufficient for
   convergence; it never assumes both missing species decay exponentially.
6. Every-point and generic-point quantifiers differ. The balanced-cycle
   theorem directly treats EVERY nonfixed interior start; one rational
   witnessing point suffices for failure of the every-point requirement.
   The asymmetric theorem explicitly treats all boundary faces as well.
7. Opposing sign-pattern examples do not solve E0062. They rule out
   sign-only criteria and supply special cases; general magnitudes and
   coupled sparse graphs still need necessary-and-sufficient conditions.
8. Algebraic certificates do not certify measure-theoretic arguments.
   Lean's stated scope is finite identities and inequalities only. All
   analytic reasoning is given above as ordinary mathematical proofs.

## 12. Extension to weighted balanced cycles (complete proof)

Theorem. For the chordless four-cycle, if 0<a,b,c,d<1 and ac=bd,
every nonfixed interior initial point has divergent coordinate averages.

Proof of the boundary-network reduction. Write f_i(x)=(Ax)_i. Balance
implies f_3=−(b/a)f_1 and f_4=−(d/a)f_2. Put
p=b/(a+b), q=a/(a+b), r=d/(a+d), s=a/(a+d),
P(x)=x_1^p x_3^q and Q(x)=x_2^r x_4^s. The exponents in each pair are
strictly positive and sum to one. In the interior,
log(P(Vx)/P(x))=p log(1+f_1)+q log(1+f_3)≤p f_1+q f_3=0,
log(Q(Vx)/Q(x))=r log(1+f_2)+s log(1+f_4)≤r f_2+s f_4=0.
Here log(1+t)≤t for t>−1, with equality only at t=0; it follows by
differentiating t−log(1+t), whose minimum is at zero. Equality for the
first product holds precisely when f_1=0, and for the second precisely
when f_2=0. Every growth factor is at least 1−max(a,b,c,d)>0, so these
log increment functions are continuous on the closed simplex. P_n,Q_n
are positive nonincreasing sequences with nonnegative limits.

If P_*>0, then log(P_{n+1}/P_n)→0. Compactness and the strict equality
condition just proved give f_1(x(n))→0: otherwise an accumulation point
with |f_1|≥ε would have a strictly negative log increment. Similarly
Q_*>0 implies f_2(x(n))→0.

Let C_P=p^p q^q and C_Q=r^r s^s. Weighted AM–GM gives
P(x)≤C_P(x_1+x_3), Q(x)≤C_Q(x_2+x_4), with equality respectively
when x_1=p(x_1+x_3) and x_2=r(x_2+x_4). To see the first inequality
directly, for a fixed total T>0 write t=Tξ, 0≤ξ≤1. Then
t^p(T−t)^q=T ξ^p(1−ξ)^q, since p+q=1. The logarithmic derivative
of ξ^p(1−ξ)^q on (0,1) is p/ξ−q/(1−ξ), positive for ξ<p and
negative for ξ>p. Its unique maximum is C_P at ξ=p. At T=0 the
inequality is trivial. The second inequality is proved with r,s in place
of p,q.

If both product limits were positive, f_1,f_2→0 would give
x_1−p(x_1+x_3)→0 and x_2−r(x_2+x_4)→0, by solving the respective
linear equations. Uniform continuity of P,Q on the compact simplex then
gives P_n/C_P−(x_1+x_3)→0 and Q_n/C_Q−(x_2+x_4)→0. Thus
P_*/C_P+Q_*/C_Q=1. A nonfixed interior initial point has f_1≠0 or
f_2≠0 (their proportional counterparts exhaust all four payoffs), hence
one of P_1<P_0 or Q_1<Q_0 holds. Monotonicity implies
P_*/C_P+Q_*/C_Q<P_0/C_P+Q_0/C_Q≤1, a contradiction.

If P_*>0,Q_*=0, then f_1→0 and Q_n→0 force x_2,x_4→0. Indeed every
accumulation point has a x_2=d x_4 and x_2^r x_4^s=0, forcing both to
zero. Consequently x_1+x_3→1. Also
0<P_*≤P_0≤C_P(x_1(0)+x_3(0))<C_P.
On [0,1] the function H(t)=t^p(1−t)^q increases strictly up to p and
decreases strictly after p, as its logarithmic derivative shows. It has
exactly two roots of H(t)=P_*, one on either side of p, by continuity,
H(0)=H(1)=0, H(p)=C_P. Every accumulation point of x_1(n) is one of
these roots, and Δx_1=x_1 f_1→0. Such a sequence converges to one root:
choose disjoint small neighborhoods of the two roots. Eventually every
term is in their union (compactness), and jumps are smaller than their
separation, so no transition between them is possible. Only one root can
be an accumulation point, which forces convergence. Both winner coordinates
therefore converge to positive limits with x_1≠p. At that limit f_2≠0
and f_4=−(d/a)f_2. One of the two missing-species multipliers is thus
eventually at least 1+ε, contradicting its coordinate tending to zero.
The case P_*=0,Q_*>0 follows by the cyclic permutation
(1,2,3,4)→(2,3,4,1), which permutes a,b,c,d and preserves ac=bd.
Both products tend to zero. Their simultaneous zero set is the same
adjacent-edge network K as in Section 8.

Finish the averaging contradiction. The empirical-measure argument in
Section 10 uses only compactness, approach to K, and strict forward motion
on each interacting open edge. These hold here, since the edge update is
t'=t+e t(1−t) for its coefficient e∈{a,b,c,d}. It therefore proves that
all empirical cluster measures are vertex-supported. If coordinate means
converged to z, the measures would converge to Σ_i z_i δ_{e_i}.
Use g_e=log(1+e), h_e=−log(1−e). Exact telescoping logs now gives
λ_1=g_a z_2−h_d z_4, λ_2=g_b z_3−h_a z_1,
λ_3=g_c z_4−h_b z_2, λ_4=g_d z_1−h_c z_3.
As before λ_i≤0 and z_iλ_i=0. The exact identity is
Σ_i z_iλ_i=(g_a−h_a)z_1z_2+(g_b−h_b)z_2z_3
                 +(g_c−h_c)z_3z_4+(g_d−h_d)z_4z_1.
All four coefficients are strictly negative. Thus the support of z is
independent; a single vertex is impossible because its predator has positive
rate. The support is one opposite pair with both masses positive.

For support {1,3}, both missing rates cannot vanish simultaneously:
λ_2=λ_4=0 would imply h_a h_c=g_b g_d by multiplying the two equalities
and cancelling z_1z_3>0. But
h_a h_c>ac=bd>g_b g_d,
since h_e>e>g_e for every 0<e<1. These two strict scalar inequalities
follow from log(1+e)<e and −log(1−e)>e, the same logarithm inequality
above. Hence at least one of λ_2,λ_4 is negative. Its coordinate is
summable. If x_4 is summable, the negative part of Δx_1 is ≤d x_4 and
the positive part of Δx_3 is ≤c x_4; if x_2 is summable, the positive
part of Δx_1 is ≤a x_2 and the negative part of Δx_3 is ≤b x_2.
The bounded-variation lemma proved in Section 10 forces x_1,x_3 to
converge to their positive average masses, contradicting P_n→0.

For support {2,4}, both missing rates zero would imply
g_a g_c=h_b h_d, impossible because g_a g_c<ac=bd<h_b h_d.
If x_1 is summable, the negative part of Δx_2 is ≤a x_1 and the positive
part of Δx_4 is ≤d x_1. If x_3 is summable, the positive part of Δx_2
is ≤b x_3 and the negative part of Δx_4 is ≤c x_3. Either possibility
forces positive limits for x_2,x_4, contradicting Q_n→0. All possible
average supports have been excluded. QED.

This covers the weighted numerical case (.8,.4,.3,.6), since ac=bd=.24.
It does not classify ac≠bd, where an attracting fixed edge may coexist
with other long-term behaviours.

## 13. The symmetric coefficient-one endpoint (complete proof)

For a=b=c=d=1, every nonfixed interior trajectory also has nonconvergent
coordinate averages. The product-decay proof in Section 8 includes this
endpoint, and the empirical invariant-measure proof in Section 10 still
applies: on an interacting edge t'=t+t(1−t) stays strictly between zero
and one. Thus, under a hypothetical average limit z, the empirical measures
again converge to Σ_i z_i δ_{e_i}.

The logarithm can now be singular at boundary vertices, so use a different
argument. For M>0 define the continuous bounded function
F_{i,M}(x)=log(max(1+(Ax)_i,exp(−M))). Along the interior trajectory
the actual growth factors are positive, and log(1+(Ax)_i)≤F_{i,M}(x).
Telescoping the actual logarithms and taking upper limits gives

limsup_n log x_i(n)/n ≤ (log 2) z_prey(i) − M z_predator(i).

The own and neutral vertices contribute log 1=0, the prey contributes
log 2, and the predator contributes −M. If z_predator(i)>0, choose
M large enough that the right side is strictly negative. Then x_i(n) is
eventually exponentially bounded and summable, and z_i=0. This proves
every adjacent product z_i z_j=0, since the loser of each adjacent pair
cannot have positive average when the winner's average is positive.
The support is therefore one vertex or an opposite pair.

If the support is {1,3}, both missing species x_2 and x_4 are summable by
the displayed bound. The coordinate changes of x_1,x_3 have summable
absolute values, bounded by x_2+x_4. They converge to z_1,z_3>0,
contradicting P_n→0. The case {2,4} follows by cyclic relabelling.

If z=e_1, x_2 is summable because its predator has mass z_1=1. The
positive increments of x_1 and the negative increments of x_3 are bounded
by x_2. The bounded-variation lemma of Section 10 gives convergence of
both coordinates, to their average limits 1 and 0 respectively. Also
x_2→0, and the simplex identity then gives x_4→0. But
x_4(n+1)=x_4(n)(1+x_1(n)−x_3(n))≥(3/2)x_4(n) eventually,
contradicting x_4(n)>0 and x_4(n)→0. Cyclic relabelling rules out the
other three single vertices. No possible average limit remains. QED.

Hence the symmetric balanced-cycle result holds for every 0<α≤1.
The general weighted ac=bd theorem in Section 12 is still restricted to
coefficients strictly below one; only its fully symmetric endpoint was
extended here.
Section 14 removes the remaining restriction for the weighted family.

## 14. All weighted balance endpoints (complete refinement)

The weighted theorem in Section 12 in fact holds for 0<a,b,c,d≤1 and
ac=bd, including mixed coefficient-one endpoints. The needed refinements
are given in full here; all other proved parts of Section 12 still apply.

First, the weighted-product reduction remains valid. Every coordinate
stays positive along an interior trajectory, because V_i(x)≥x_i². Thus
all finite-time logarithms in Section 12 exist, even at coefficient one.
The nonpositive log increments still prove monotonicity of P_n,Q_n. On
the CLOSED simplex, instead of their potentially singular log increments,
use the continuous product multipliers
H_P(x)=(1+f_1(x))^p(1+f_3(x))^q,
H_Q(x)=(1+f_2(x))^r(1+f_4(x))^s.
The factors are nonnegative, and the exponents are positive, so these
functions are continuous including at a zero factor. If a factor is zero,
the corresponding H is zero. If both factors are positive, the logarithm
inequality from Section 12 gives H≤1, with equality exactly when both
payoffs vanish. Consequently H_P=1 iff f_1=f_3=0, and H_Q=1 iff
f_2=f_4=0. If P_*>0 then H_P(x(n))=P_{n+1}/P_n→1. By compactness
and this strict equality condition, f_1→0. The same argument works for
Q_*>0. The rest of the positive-limit exclusion in Section 12 uses only
these payoff limits, weighted AM–GM, bounded jumps and positive invasion
multipliers. It therefore proves P_n,Q_n→0 under the enlarged bounds.

The empirical-measure argument still gives vertex support under a
hypothetical average limit z. Each growth factor for coordinate i has a
single losing coefficient e∈(0,1] and a single winning coefficient
e'∈(0,1]. If e<1, its factor is uniformly at least 1−e>0 and the usual
continuous-log argument gives its actual rate
λ_i=g_{e'} z_prey(i)−h_e z_predator(i)≤0,
with z_i>0 implying λ_i=0. If e=1, the clipped logarithm argument of
Section 13 gives
limsup log x_i(n)/n ≤ g_{e'} z_prey(i)−M z_predator(i)
for every M>0. Therefore z_predator(i)>0 makes x_i summable and z_i=0.

We now prove independent support WITHOUT multiplying infinite rates.
Suppose two adjacent winner/loser vertices i,j have z_i,z_j>0. The
coefficient of i's advantage over j cannot be one, by the clipped-log
conclusion. If it is below one, the true finite rate of coordinate j
exists and equals zero, so
g_{next coefficient} z_next = h_{previous coefficient} z_i>0.
The next vertex therefore also has positive mass. Repeating this argument
round the four-cycle either reaches an edge of coefficient one, giving
an immediate contradiction, or makes all four masses positive with all
coefficients below one. In the latter case the strict-negative weighted
rate identity from Section 12 gives a contradiction. No adjacent pair
can have positive mass. Thus support is a single vertex or an opposite pair.

For a single vertex z=e_1, coordinate x_2 is summable: if a<1 its finite
rate is −h_a<0, and if a=1 the clipped bound is −M<0. The positive
increments of x_1 are at most a x_2 and the negative increments of x_3
at most b x_2. They converge to their averages 1 and 0. The other two
coordinates then tend to zero by summability and the simplex identity.
But the positive coordinate x_4 has multiplier tending to 1+d>1, a
contradiction. Cyclic relabelling treats each other single vertex.

For support {1,3}, if a=1 or c=1 the clipped bound immediately makes
x_2 or x_4 summable, respectively. If a,c<1, both missing rates are
finite. They cannot both be zero, because that would imply
h_a h_c=g_b g_d, whereas h_a h_c>ac=bd>g_b g_d. The inequalities
g_e<e hold also at e=1, since log 2<1. Thus at least one missing rate
is negative and its coordinate is summable. The one-sided-variation
argument in Section 12 then gives positive limits for x_1,x_3,
contradicting P_n→0. For support {2,4}, if b=1 or d=1 the clipped
bound makes x_3 or x_1 summable. Otherwise their finite rates cannot
both vanish because g_a g_c<ac=bd<h_b h_d. The corresponding variation
argument contradicts Q_n→0. All supports have been ruled out. QED.

Final balanced-cycle classification: for any 0<a,b,c,d≤1 with ac=bd,
fixed interior points have constant averages, EVERY other interior point
has divergent averages, and all boundary trajectories converge. Thus this
entire balance surface fails the every-point property in E0062.

## Final verification and verdict (2026-10-12T03:09:17.121978+00:00)

The shared Lean compiler outcome is unrecovered: the log records only a slot wait, the result marker remained RUNNING past its nominal hour, and no matching live runner/checker process was found. No Lean-checked claim is made. Ordinary proofs survived the author rereading.

The continuation author rereading is REFEREE.md. The only mathematical edit was to make the weighted-AM-GM scaling explicit; divergence is understood as failure of the vector limit. See VERIFICATION.md for exact formalization scope and saved outputs.

STATE: DONE; VERDICT: PARTIAL. No general necessary-and-sufficient criterion has been proved or verified in print. The concrete remaining unbalanced four-cycle and coupled-zero-matrix gap is stated in Section 9 and RESULTS.md.
