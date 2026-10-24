# E0066 — trajectory investigation

Date: 2026-10-12. Verdict: PARTIAL. All simplices include their boundary.

## Exact source and scope

R. N. Ganikhodzhaev and U. A. Rozikov, *Quadratic Stochastic Operators: Results and Open Problems*, arXiv:0902.4207, Problem 13, PDF p. 8:

> Investigate the behavior of trajectories of the bistochastic quadratic operators.

We work with finite m and S^{m-1}={x in R^m: x_i>=0, sum_i x_i=1}, V_k(x)=sum_{i,j} p_{ij,k}x_ix_j, p_{ij,k}=p_{ji,k}>=0, sum_k p_{ij,k}=1, and V(x) majorised by x for every x in the entire simplex. No positivity, irreducibility, strict majorisation, or interior-start assumption is added. The source's Definition 4, p. 7, actually defines bistochasticity for arbitrary continuous maps.

The broad imperative is not equivalent to “all trajectories converge.” That assertion is false. General asymptotic periodicity is established in earlier literature. Below are full independent proofs, and an extension of the earlier repository rigidity argument to boundary supports. No novelty claim is made.

## Theorem 1: every trajectory is asymptotically periodic

For every continuous bistochastic map and initial x, there is a periodic orbit z_0,...,z_{p-1} with V(z_r)=z_{r+1 mod p}, such that V^{kp+r}(x) tends to z_r after choosing the phase. Every z_r is a coordinate rearrangement of the same sorted vector y, and

p <= m! / product_a (multiplicity of a in y)!.

Proof. Put T_k(u)=sum of the k largest coordinates, T_0=0. Each T_k(V^n x) is nonincreasing and bounded below by zero, so converges to s_k. Thus each sorted coordinate converges to y_k=s_k-s_{k-1}. Nonnegativity, decreasing order, and sum one pass to the limit. T_k is continuous: it is the maximum of finitely many linear functions sum_{i in I}u_i over k-element sets I. Hence sorting, whose coordinates are differences of these functions, is continuous. Every accumulation point has sorted vector y. Compactness gives a nonempty omega-limit set Omega contained in the finite set of distinct rearrangements of y. Its cardinality has the asserted bound, by choosing the positions of each distinct coordinate value successively.

Continuity gives V(Omega) subset Omega. It is onto: for z=lim V^{n_j}x with n_j tending to infinity, take a convergent subsequence of V^{n_j-1}x; its limit w belongs to Omega and V(w)=z. Thus V restricts to a permutation of Omega.

The distance of V^n x from Omega tends to zero. Otherwise compactness provides an accumulation point of a subsequence staying a fixed positive distance away, contradicting its membership in Omega. If Omega is a singleton, this already proves convergence and invariance makes its point fixed. Otherwise let d be the minimum distance between distinct omega-points. Uniform continuity supplies epsilon in (0,d/3) such that dist(u,v)<epsilon implies dist(Vu,Vv)<d/3. For all sufficiently large n there is a unique omega-point a_n within epsilon of V^n x. The triangle inequality gives dist(V(a_n),a_{n+1})<d/3+epsilon<d, so a_{n+1}=V(a_n). The index sequence therefore follows one cycle of the permutation V|Omega. Every omega-point must appear infinitely often among a_n: a subsequence converging to that point eventually has it as its unique nearby point. Consequently Omega is that single cycle. Each fixed-phase subsequence has only the corresponding cycle point as an accumulation point, hence converges to it by compactness. Relabeling absorbs the initial time shift. QED.

Corollaries. V is regular (every trajectory converges) iff it has no cycles of length >1. The barycentre is always fixed, since no other vector is majorised by the barycentre. Neither uniqueness of that fixed point nor regularity follows in general.

## Lemma 2: interior fixed-point rigidity

A quadratic bistochastic operator W fixing an interior vector y with pairwise distinct coordinates is the identity operator on the entire simplex.

Proof by induction on m. The one-coordinate case is immediate. Relabel so y_1>...>y_m>0. In a neighbourhood of y on the simplex, W_1(u)<=max_i u_i=u_1. Therefore g(u)=u_1-W_1(u) has a local minimum zero at y. Two-sided tangent perturbations are allowed because y is interior; all components of its ambient gradient equal a constant c. Hence partial_j W_1(y)=delta_{j1}-c. Homogeneity gives sum_j y_j partial_j W_1(y)=2W_1(y)=2y_1, so c=-y_1. Thus

(1) sum_i p_{ij,1}y_i=(delta_{j1}+y_1)/2 for every j.

For any nonempty index set I, evaluate bistochasticity at the vector uniform on I. Its maximum coordinate is 1/|I|, whence

(2) sum_{i,j in I}p_{ij,k}<=|I|.

Let p=p_{11,1} and a_i=p_{i1,1} for i>=2. Using I={1,...,s+1} and nonnegativity in (2), A_s=sum_{i=2}^{s+1}a_i <= (s+1-p)/2. Abel summation against y_2>=...>=y_m gives

sum_{i=2}^m a_i y_i = sum_{s=1}^{m-2}A_s(y_{s+1}-y_{s+2})+A_{m-1}y_m

<= (1-p/2)y_2 + (1/2)sum_{i=3}^m y_i.

The formula also applies for m=2, with the first sum empty. Combining this with (1), j=1, and sum y_i=1 yields (1-p)(y_1-y_2/2)<=0. Since p<=1 by stochasticity and y_1-y_2/2>0, p=1. Inequality (2) for I={1,i} gives a_i<=1/2. Equality (1), j=1, now says sum_{i>=2}(1/2-a_i)y_i=0. Every summand is nonnegative and y_i>0, so a_i=1/2. Equation (1) for j>=2 then gives sum_{i>=2}p_{ij,1}y_i=0. Thus all these coefficients vanish and W_1(u)=u_1 identically.

For u=(t,(1-t)z), write

W_k(u)=(1-t)[t(Bz)_k+(1-t)U_k(z)], k>=2,

where B_{kj}=2p_{1j,k} and U_k(z)=sum_{i,j>=2}p_{ij,k}z_i z_j. Stochasticity and the coefficients already determined show that B is column-stochastic and U is a QSO. Majorisation of (t,(1-t)w) by (t,(1-t)z) implies w is majorised by z. To justify cancellation explicitly: for every real a, majorisation implies sum_i(u_i-a)_+ <= sum_i(v_i-a)_+, since the hinge sum equals max_{0<=k<=m}(T_k(u)-ka). Cancel the common-coordinate term and use a=(1-t)b to obtain this inequality for w,z for all real b. These inequalities imply the top-k inequalities because T_k(w)=min_b[kb+sum_i(w_i-b)_+]; for k less than the dimension the minimum is attained at any b between its kth and (k+1)st largest coordinates, and for k equal to the dimension at any b below the smallest. Thus the reduced map tB+(1-t)U is bistochastic for every 0<=t<1. At t=0 this gives bistochasticity of U; taking t to 1 and using closedness of the top-k inequalities gives bistochasticity of B. Applying B to the uniform vector shows its rows also sum to one, so B is doubly stochastic.

Set z=(y_2,...,y_m)/(1-y_1). Fixedness gives z=y_1 Bz+(1-y_1)U(z), with Bz and U(z) majorised by z. For completeness, squared norm cannot increase under majorisation: the hinge inequalities just used, integrated over a in [0,1], give sum_i w_i^2/2<=sum_i z_i^2/2 for simplex vectors w majorised by z. The exact identity

||t u+(1-t)v||^2=t||u||^2+(1-t)||v||^2-t(1-t)||u-v||^2

at t=y_1 in (0,1) therefore forces Bz=U(z)=z. The induction hypothesis makes U the identity because z is interior and has distinct coordinates. Finally a doubly stochastic matrix fixing a distinct-coordinate vector is the identity: the largest output coordinate is a convex combination of inputs and attains their strictly largest value, so its row has only the corresponding unit entry; the column sum then clears its column, and induction on the remaining rows and columns proves the assertion. Thus B is the identity too. All coefficients of W equal (delta_{ik}+delta_{jk})/2. QED.

## Theorem 3: boundary-support extension

If x is periodic under a quadratic bistochastic V and its positive coordinates are pairwise distinct, its entire cycle is induced by a single coordinate permutation on the union of its supports. In particular its period divides the order of some permutation of at most m elements.

Proof. Majorisation along a periodic orbit must be equality in every top-k sum, since the sums are nonincreasing and return to their original values. Thus V(x) is a rearrangement of x. Choose a coordinate permutation P taking x to V(x), and put W=P^{-1}V. Then W is a QSO, bistochastic, and W(x)=x. Let I={i:x_i>0}. For k outside I,

0=W_k(x)=sum_{i,j in I}q_{ij,k}x_i x_j.

All terms are nonnegative with strictly positive x_i x_j, so q_{ij,k}=0 for all i,j in I and k outside I. Thus W maps the face supported on I to itself. On that face it is a QSO, and its majorisation is exactly the smaller-simplex majorisation because adding zero coordinates does not change the relevant top sums. Its fixed point x is interior in that face and has distinct coordinates there. Lemma 2, including its one-coordinate case, makes W the identity on the face. Therefore for each i in I, V(e_i)=P(e_i), and V agrees with P on the whole face supported on I.

Apply the same argument at every point x_t in the periodic orbit. Let U be the union of their supports. For every i in U, V(e_i) is a vertex e_{f(i)}, defining a single time-independent function f: the operator's value at e_i is independent of the choice of P. On each current support, f equals the permutation chosen at that phase, so supp(x_{t+1})=f(supp(x_t)) and each positive coordinate is transferred without alteration. Taking the union over a full cycle gives f(U)=U. A surjection of a finite set to itself is a bijection. Extend f by fixing the indices outside U; this is a coordinate permutation F on all m indices. At every phase V(x_t)=F(x_t). The period therefore divides the order of F, by the elementary division algorithm for powers of a permutation. QED.

This extends the earlier repository argument, which only treated full interior supports. It does not assume that the chosen rearrangement P is unique on zero coordinates; its restriction to positive coordinates is unique, and the vertex images determine f independently.

## Corollary 4: sharp three-type and two-type period bounds

For m=3 every trajectory is asymptotic to a cycle of length 1, 2, or 3. For m=2 the only possible lengths are 1 or 2.

Proof. In m=3, if the limiting sorted vector's positive values are distinct, apply Theorem 3 at a point of its limit cycle. A permutation of three elements has order 1, 2, or 3: its disjoint cycles are either three singletons, a transposition and singleton, or a three-cycle. A cycle period divides that order. If instead a positive value repeats, the vector is either (a,a,b) with at least two equal entries (including b=0), or has all three equal; it has at most three distinct rearrangements, and Theorem 1 bounds the period by three. For m=2, Theorem 1 already gives the bound two.

Sharpness and nonconvergence. Every coordinate permutation is a QSO with p_{ij,k}=(1_{f(i)=k}+1_{f(j)=k})/2, because sum x_i=1 reduces its quadratic formula to x_{f^{-1}(k)}. It preserves the sorted vector and is therefore bistochastic. A transposition acting on a vector with distinct swapped values has exact period two; a three-cycle acting on (1/2,1/3,1/6) has exact period three. Hence a universal convergence-to-a-point assertion is false, even for interior starting points.

## Theorem 5: complete trajectory description for two types

Write V(t,1-t)=(f(t),1-f(t)). For every quadratic bistochastic V there are real a,b with

f(t)=1/2+a(t-1/2)+b(t-1/2)^2, and |a|+|b|/2<=1.

If (a,b)=(1,0), V is the identity. If (a,b)=(-1,0), V swaps the coordinates and every noncentral point has period two. In every other case every interior initial point converges to (1/2,1/2). An endpoint either enters the interior and then converges to the centre, or reaches a fixed endpoint after at most one step. Thus no genuinely nonlinear two-type QBO has a nontrivial periodic orbit.

Proof. Bistochasticity fixes t=1/2. Subtracting that value from the quadratic polynomial gives the displayed representation. Two-dimensional majorisation is exactly |f(t)-1/2|<=|t-1/2|. For z=t-1/2 !=0 this is |a+bz|<=1; continuity extends it to z=0. The maximum over [-1/2,1/2] is |a|+|b|/2, which proves the coefficient bound. Conversely that bound implies the same majorisation inequality and ensures f maps [0,1] into [0,1]. Its Bernstein coefficients are p=f(1), r=f(0), q=1-(p+r)/2. The endpoint values are in [0,1], and hence q is too. The polynomial p t^2+2q t(1-t)+r(1-t)^2 agrees with f at 0,1/2,1, so is f. Taking complementary coefficients for the other output constructs a QSO. Thus the coefficient bound also gives a complete parameterisation of two-type QBOs.

When b=0 the recursion z_{n+1}=a z_n gives exactly the asserted identity, swap, or strict contraction cases. When b!=0, every interior z satisfies |a+bz|<=|a|+|b||z|<1. Its orbit remains interior and its radius decreases. If its limiting radius R were positive, choose an accumulation point z_* with |z_*|=R. Because every radius is at most the strictly interior initial radius, z_* is interior. Continuity and the existence of the next-iterate radius limit give |z_*|=|z_*||a+bz_*|, contradicting strict inequality. Thus R=0.

Starting at an endpoint, either an iterate enters the interior or the entire orbit stays in the two-element endpoint set. In the latter case it is eventually fixed or a two-cycle. A two-cycle would require f(0)=1 and f(1)=0, equivalently a-b/2=-1 and a+b/2=-1, so a=-1 and b=0. That is excluded in the nonlinear case, so the endpoint orbit reaches a fixed endpoint after at most one step. QED.

Boundary control. The genuine QSO f(t)=2t(1-t) has (a,b)=(0,-2), satisfies the coefficient bound, sends 1 to 0, and fixes 0. Only its interior trajectories converge to 1/2. This directly repairs the earlier memory's universal-boundary overstatement.

## Remaining gap

**Follow-up update, 2026-10-12:** the paragraph below describes the initial gap. The serious second attempt in [FOLLOWUP.md](FOLLOWUP.md) now proves that all interior periodic orbits, all interior-start limiting cycles, and all constant-support boundary cycles follow a single coordinate permutation. It gives an exact finite linear-algebra description of the entire interior periodic locus from B=DV(c)-J/m. Theorem 10 further determines every interior trajectory's limiting cycle and basin: V^n(x)-P^n R x tends to zero, where R averages a computable coordinate partition and P is fixed. The current unclassified periodic case is boundary cycles with repeated positive values and varying supports. The full source programme, including those boundary cases, remains PARTIAL.

No full classification of all quadratic bistochastic trajectory basins, cycle vectors, or possible periods in every dimension is supplied by the literal broad source or by this attempt. For m>=4, when positive coordinate values repeat, this proof supplies only the rearrangement-count bound. It does not prove that such a cycle is induced by one coordinate permutation, nor exclude a period larger than the maximal order of a permutation of m elements. That is a precise residual question, not asserted to be open in all literature. The independent three-type result and boundary-support extension are proved special cases, not a solution certificate for the broad programme.


## Hostile-referee checks

1. Sorted-coordinate continuity and lower bounds: proved using finite maxima, not assumed differentiability of sorting.
2. A finite omega-set might conceivably have several cycles: ruled out by the unique-nearby-point argument and visits to every omega-point. Forward invariance alone would not suffice.
3. The first-order condition in Lemma 2 needs two-sided perturbations: used only in the relative interior of the appropriate invariant face, never directly at a boundary point of the original simplex.
4. Abel summation uses decreasing positive weights: its displayed identity and prefix bounds are explicit, including m=2. The final sign is (1-p)(y_1-y_2/2)<=0, with both factors nonnegative.
5. Majorisation cancellation with a common coordinate: proved through hinge sums and their top-k variational formula; it does not assume the common coordinate has a fixed rank.
6. Zero-output face invariance depends on nonnegative coefficients: all products x_i x_j in the support are strictly positive, so cancellation is impossible. This is where QSO positivity matters.
7. The phase permutations may disagree off the current support: the common vertex images define f on the union of supports. Surjectivity f(U)=U is proved using the full periodic cycle, not inferred from one phase.
8. Repeated positive coordinates invalidate distinct-coordinate rigidity: linear averaging within a repeated block gives nonidentity fixed points. The three-type bound handles these separately via at most three rearrangements; no analogous order bound is asserted in larger dimensions.
9. Boundary convergence: f(t)=2t(1-t) fixes t=0 and sends t=1 to 0, verified exactly with fractions. Identity and coordinate permutations also prevent any universal centre-attraction claim.

`experiments.py` builds the necessary coefficient inequalities sum_{i,j in I}p_{ij,k}<=|I| for all nonempty subsets, together with stochasticity, nonnegativity, and prescribed fixed points/cycles. It ran 60 random-objective LP checks of face rigidity, in m=2,...,6 and all support sizes, with distinct positive rational weights and zero remaining coordinates. All feasible optima agreed with the identity coefficients on the fixed face to 1.49e-14. These LP constraints are necessary for every QBO, so failure to find a contradiction supports the proof; floating-point LP is not used as a certificate.

A bounded exploratory search sampled 24 ordered cycles each of lengths five and six among the 12 rearrangements of (0.4,0.4,0.15,0.05) in four types. All 48 LPs were reported infeasible. This does not exhaust cycle orders, prove an order bound, or establish an open problem. Full results and statuses are in experiments.json. The job used small dense matrices (well below 1 GB) and took about 1.2 seconds once imports completed.

`PeriodBound.lean` formalises only the finite permutation-order step for Fin 2 and Fin 3. Compilation status is recorded separately in lean_check.log; no claim that the full analytic proof is formalised is made.


Lean verification completed successfully: `lake env lean ~/brain_workers/TRIO_1011/op/E0066/PeriodBound.lean`, invoked from ~/lean_verify with a 3600-second subprocess timeout. Exit code 0. The file imports only Mathlib.Data.Fintype.Perm and uses `decide +kernel` for both finite statements. Reported axioms: propext, Classical.choice, Quot.sound. No sorry, no native_decide. The initial UTF-8 BOM parse failure is preserved in lean_check_initial.log; the BOM was removed and the successful rerun is in lean_check.log. Only the finite permutation-order statements are kernel checked; the analytic and support-rigidity proofs are written mathematical proofs.

Final referee conclusion: the proofs above survive the listed checks. The bounded literature search does not establish novelty or complete resolution of the source programme. STATE: DONE means this attempt is finished with its gap explicitly recorded; VERDICT remains PARTIAL.


## Second-attempt conclusion, 2026-10-12

Two previously untried approaches and complete follow-up proofs are in FOLLOWUP.md. The uniform-point reduction now gives explicit limits and basins for all interior trajectories: V^n(x)-P^n R x tends to zero. The partition-averaging projection R and permutation P are determined by the uniform linearisation. All interior periodic points form an affine-linear slice; the sharp limiting period bound is g(m). Constant-support boundary cycles are also covered. The remaining gap is repeated-positive-value boundary cycles with moving supports, and their full classification. Lean radial algebra, exact symbolic examples, and hostile LP checks passed. Final STATE: DONE, VERDICT: PARTIAL.
