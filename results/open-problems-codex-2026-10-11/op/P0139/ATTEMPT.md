# P0139 - research attempt (12 October 2026)

## Second-attempt update

The user's requested serious continuation is in [CONTINUATION.md](CONTINUATION.md). It records two new approaches and complete proofs of: qualitative convergence of the source's moving inverse clocks; enhanced physical-time p-variation continuity for 2<r<p<3 under specified stronger input convergence and tail conditions; canonical Brownian-loop energy and selected absolute-area summability in bounded domains; and a zero-area counterexample along every power cusp in the original source distance. Thus the fixed-schedule restriction of the original positive results below has now been removed under stronger hypotheses. The remaining gap is the norm-adapted cusp modulus, endpoint continuity without energy compactness, and verification of the enhanced convergence/uniform tails and lift identification for a particular stochastic or lattice coupling. The verdict remains PARTIAL.

## Scope and source verification

Source: Berestycki-Sauzedde, arXiv:2602.04673v1, Section 7, p.40. The question asks for Hölder, p-variation, or rough-path continuity of chronological attachment, perhaps along the cusp lambda >= C d_R0(X,X')^beta with an appropriately strengthened distance. No beta, enhanced domain, or exact continuity modulus is specified there. Lambda is the inverse backbone pace, not a cutoff.

The source's R has conditions (i)-(v) on p.9: finite attached duration and local finiteness by duration; equicontinuous loops; distinct first hitting times and unique temporal roots; dense first hitting times; regular intersecting pairs. R0 retains (i),(ii). Theorem 4.11, p.22, gives uniform first-level continuity near R x {0}. It supplies neither loop enhancements nor an area estimate.

**What is proved below:** a fixed-physical-clock countable attachment theorem for enhanced planar loops, including an explicit rough p-variation truncation bound. This is a special case/reduction, not a solution of continuity under varying chronological first hits, temporal roots, and clocks. A counterexample below concerns only a topology omitting area information.

## 1. Conventions

Fix 2 < p < 3 and q=p/2. For a two-index increment F, write

    ||F||_r = sup_P (sum_[s,t] in P |F(s,t)|^r)^(1/r).

All partitions are finite, ordered, and on the same physical interval [0,T]. A planar step-two weak geometric rough path is represented by its increments (x_st,a_st), where a_st is scalar antisymmetric signed area and

    x_st=x_su+x_ut,
    a_st=a_su+a_ut+(1/2) x_su wedge x_ut.

Here u wedge v=u_1 v_2-u_2 v_1. Its second tensor level is (1/2)x_st tensor x_st+a_st J, with J=e1 tensor e2-e2 tensor e1. Constant changes in tensor norms are absorbed into constants depending on p. Define V=||x||_p+||a||_q^(1/2). We use the increment distance

    D_p(X,Z)=||x^X-x^Z||_p+||a^X-a^Z||_q^(1/2).

On bounded first-level p-variation sets, this gives the usual step-two rough-path topology: the difference of symmetric tensor levels has q-variation at most

    (1/2)(||x^X||_p+||x^Z||_p)||x^X-x^Z||_p.

This follows termwise from u tensor u-v tensor v=(u-v) tensor u+v tensor (u-v), followed by sequence Hölder with 1/q=2/p. Initial positions are fixed throughout; an initial-position distance can be added separately.

## 2. Fixed-clock attachment theorem

Let Y be a continuous planar weak geometric p-rough path on [0,T], starting at zero, with norm V. Let I_i=(l_i,r_i), i in a countable index set, be pairwise disjoint nonempty open intervals in [0,T]. Require that **both levels of Y are constant on each closed [l_i,r_i]**. Equivalently all its rough increments inside that interval vanish. First-level constancy alone would allow central drift and is insufficient.

For each i give a continuous based enhanced loop L_i=(e_i,a_i) on [l_i,r_i], with e_i(l_i)=e_i(r_i)=0. Its rough increments satisfy Chen's identity. Set

    L_i^* = ||e_i||_p + ||a_i||_q^(1/2),
    c_i = a_i(l_i,r_i),
    E = (sum_i (L_i^*)^p)^(1/p),   A=sum_i |c_i|.

Assume E<infinity and A<infinity. Norms of individual loops are taken in their stated physical parametrizations. No clock is erased or optimized over.

For a finite subset K, attach the loops in K on their assigned intervals; on omitted intervals keep Y stationary, with the full original interval retained as waiting time. Concatenate the enhanced restrictions of Y and these enhanced loops. Call the result X^K. Only finitely many splices are made, so this construction is unambiguous by Chen's law.

**Theorem 1.** There is a unique exhaustion-independent limit X of X^K in D_p as K exhausts the indices. For every finite K, put

    eps_K=(sum_(i notin K) (L_i^*)^p)^(1/p),
    alpha_K=sum_(i notin K) |c_i|.

For a constant C_p independent of the number, location, and lengths of the intervals,

    ||x^X-x^K||_p <= C_p eps_K,
    ||a^X-a^K||_q <= C_p [eps_K^2+(V+E)eps_K+alpha_K].       (1)

In particular

    D_p(X,X^K) <= C_p {eps_K+[eps_K^2+(V+E)eps_K+alpha_K]^(1/2)}.   (2)

The same bound in the usual tensor rough metric follows by the symmetric-level estimate in Section 1. Every finite approximation and the limit have first-level norm <= C_p(V+E). For the whole lift,

    ||x^X||_p+||a^X||_q^(1/2) <= C_p[V+E+A^(1/2)].             (3)

The theorem does not assert that A is bounded by E^2: that implication is false for p>2.

### Proof, including the partition argument

Write y(t)=Y^1_0t and A_y(t)=a^Y_0t. For a finite K define e_K(t) to equal e_i(t) when t is inside an interval in K, and zero otherwise (also zero at endpoints). Write b_i(t)=a_i(l_i,t). Define

    B_K(t)=sum_(i in K,r_i <= t)c_i
           + b_i(t) if t is inside an interval i in K,

with the final summand zero otherwise. Then the global coordinates of X^K are

    x_K(t)=y(t)+e_K(t),
    A_K(t)=A_y(t)+B_K(t)+(1/2)y(t) wedge e_K(t).             (4)

To verify (4), before a loop the existing first increment is y(l_i); multiplying the group element by the loop prefix adds b_i+(1/2)y(l_i) wedge e_i. During that interval Y is constant as an enhanced path, so y(t)=y(l_i) and A_y(t)=A_y(l_i). On completing the loop, e_i=0 and only c_i remains. Between loops the previous completed loops have zero first displacement and central area, so they add no first-level cross terms. This proves (4) successively for every finite concatenation.

Expanding A_K(t)-A_K(s)-(1/2)x_K(s) wedge x_K(t) gives

    a^K_st = a^Y_st+B_K(t)-B_K(s)
       +(1/2)(y(t)-y(s)) wedge (e_K(t)+e_K(s))
       -(1/2)e_K(s) wedge e_K(t).                          (5)

This identity is checked algebraically in SpliceAlgebra.lean. It applies also when an endpoint lies exactly at a loop boundary, since e_i=0 there and b_i(r_i)=c_i.

Fix finite H subset K, and R=K\H. Write eps=(sum_R (L_i^*)^p)^(1/p), alpha=sum_R |c_i|, and f=e_K-e_H. For any partition divide its intervals into:

* interior intervals: s,t both in the same closed [l_i,r_i] for i in K;
* crossing intervals: all the other intervals.

If two closed loop intervals share an endpoint, a nondegenerate interval can be interior to at most one. Degenerate intervals can be dropped. On an interior interval, Y has zero increment and the two outputs are either identical, or one is L_i and the other is constant, for i in R. Interior partition subintervals within one loop have disjoint interiors, so by completing them to a partition of that loop,

    sum_interior |(x^K-x^H)_st|^p <= sum_R (L_i^*)^p,
    sum_interior |(a^K-a^H)_st|^q <= sum_R (L_i^*)^p.       (6)

For crossing intervals the following elementary counting fact is essential: the interior of any one loop interval contains endpoints of at most TWO crossing partition intervals, one entering it and one leaving it. Intermediate partition intervals with endpoints in that loop are interior intervals. Endpoints at the loop boundary contribute zero e_i or f_i and need no counting. Consequently the endpoint sequences over crossing intervals satisfy

    sum_cross (|e_K(s)|^p+|e_K(t)|^p) <= 2 sum_K (L_i^*)^p,
    sum_cross (|e_H(s)|^p+|e_H(t)|^p) <= 2 sum_H (L_i^*)^p,
    sum_cross (|f(s)|^p+|f(t)|^p) <= 2 eps^p.              (7)

Indeed |e_i(t)|<=||e_i||_p<=L_i^*. Also |b_i(t)|<=||a_i||_q<=(L_i^*)^2. The latter inequality concerns the single increment (l_i,t), NOT variation of the global-coordinate function b_i.

Subtract (5) for K and H. The difference B_K(t)-B_K(s)-B_H(t)+B_H(s) on a crossing interval is the sum of c_i for removed loops wholly traversed from s to t, plus at most two endpoint contributions: b_i(t) for a removed right endpoint loop and c_i-b_i(s) for a removed left endpoint loop. (A left endpoint exactly at a boundary may instead be assigned to the complete-loop sum; this does not affect the bound.) Completely traversed removed loops occur in at most one crossing partition interval. Their total q-norm is at most alpha: for their nonnegative absolute sums z_j, (sum z_j^q)^(1/q)<=sum z_j<=alpha. By endpoint counting, the q-norm of all endpoint terms is <=C_p eps^2, since |c_i-b_i(s)|<=2(L_i^*)^2.

The y-dependent term in the difference of (5) is

    (1/2)y_st wedge (f(t)+f(s)).

Its q-norm is bounded by C_p ||y||_p eps<=C_p V eps, using (7) and sequence Hölder. Explicitly, sum (u_j v_j)^q <= (sum u_j^p)^(1/2)(sum v_j^p)^(1/2), and taking the 1/q power gives ||u||_p ||v||_p.

For the remaining wedge term, use

    e_K(s) wedge e_K(t)-e_H(s) wedge e_H(t)
      = f(s) wedge e_K(t)+e_H(s) wedge f(t).

Its q-norm is <=C_p E eps by (7) and the same Hölder inequality. Adding these bounds by Minkowski (q>1) proves the second bound in (1) for the finite pair H,K, with eps and alpha over R. The first bound follows from (6),(7) and |f(t)-f(s)|^p<=2^(p-1)(|f(s)|^p+|f(t)|^p).

The identical first-level partition argument with H empty shows ||x^K-y||_p<=C_p E, hence ||x^K||_p<=C_p(V+E). Applying the area difference estimate with H empty gives

    ||a^K-a^Y||_q<=C_p[E^2+VE+A],

which proves (3) uniformly for all finite K.

For any exhaustion K_n, summability makes eps_(K_n),alpha_(K_n) tend to zero. The finite-pair bounds imply the increment arrays are Cauchy in the stated variation norms. Here is the needed completeness argument explicitly. Variation norm bounds the sup norm of any increment, since any [s,t] can be included in a partition. Thus the arrays converge uniformly; the limit is continuous and Chen's identities pass to the limit as finite polynomial identities. For any fixed partition, pass to the limit in the finite sum of powers. Taking its supremum shows the variation distance to the limit is at most the liminf of the distances to approximations. This proves convergence in variation and finiteness of the norms. The symmetric tensor identity passes to the limit too. Thus the limit is a weak geometric rough path. The bounds pass to it by the same argument. Comparing two finite subsets through their union shows independence of exhaustion. Uniqueness refers to this limit construction, not to all lifts of the resulting first-level path. This proves Theorem 1. QED.

### Theorem 2: continuity when enhanced loop data vary on the fixed schedule

Keep the enhanced backbone Y and the intervals I_i fixed. Give two families of based enhanced loops L_i and L'_i, both satisfying Theorem 1. Let E,E' denote their p-energy roots. Write

    d_i=||e_i-e'_i||_p+||a_i-a'_i||_q^(1/2),
    delta=(sum_i d_i^p)^(1/p),
    beta=sum_i |c_i-c'_i|.

Then their countable attachments X,X' satisfy

    ||x^X-x^X'||_p <= C_p delta,
    ||a^X-a^X'||_q <= C_p[delta^2+(V+E+E')delta+beta].    (8)

Consequently this attachment map is continuous on the fixed schedule in the input topology combining the l^p sum of loop rough increment distances and the l^1 distance of terminal areas. On sets with V,E,E' bounded it has the displayed local one-half-power modulus. Both loop duration and attachment interval are fixed in this theorem; there is no time quotient.

**Proof.** First retain finitely many loops in both families. The interior/crossing division uses their common intervals. On interior intervals the sum of first-level difference powers is bounded by sum d_i^p, and the sum of area difference q-powers by sum d_i^p. On crossing intervals, f=e-e' has endpoint magnitude at most d_i and at most two endpoint incidences per interval. The sequences of e and e' endpoints have p-norm bounded by C_p E and C_p E', respectively. The difference of prefixes b_i(t)-b'_i(t) is bounded by ||a_i-a'_i||_q<=d_i^2; the difference of suffixes is bounded by 2d_i^2, by using the two increments (l_i,r_i) and (l_i,s). Completed-loop differences have total absolute sum at most beta, hence q-norm at most beta. Subtracting (5), the y-dependent product is bounded by C_p V delta. The remaining wedge difference equals f(s) wedge e(t)+e'(s) wedge f(t) and has q-norm at most C_p(E+E')delta. Minkowski and the endpoint estimate for the first level give (8) for the finite families. Apply Theorem 1 separately to exhaust both families and pass each finite-partition estimate to the limit. This proves (8) and the asserted continuity. QED.

This topology is explicit input data, not the pullback of the output distance. The separate l^1 terminal-area requirement is not implied by the l^p local rough distance when p>2.

## 3. Connection with the source (conditional corollary)

For a source configuration X=(gamma,L), fix its chronological hit times, temporal roots and tie break, lambda, and the physical schedule I_i=(T_i,T_i+t_i). Suppose gamma is supplied with a continuous step-two weak geometric p-lift. Let sigma be the source's continuous nondecreasing inverse clock. Then Y=gamma lifted and composed with sigma is a rough path of norm at most that of gamma: any ordered sigma-image of a partition is an ordered backbone partition after repetitions are deleted. It is constant at both levels during each I_i.

Supply each rerooted loop with its enhancement in the fixed physical parametrization. If E<infinity and A<infinity, Theorem 1 constructs a lift of the source attachment path and proves (1)-(3) for deleting loops while retaining their durations as stationary waits. The first level equals the source path: inside every I_i it equals the stated rerooted loop; outside it equals gamma(sigma(t)), as follows either directly from uniform convergence of (4), or from the source's definition. This is a conditional corollary, with all its extra hypotheses explicit.

The finite approximations with waits are not necessarily source outputs for configurations with the loops deleted. Deleting a loop in the source changes the physical clock and can change inverse-clock regularity. Therefore this corollary does NOT transfer the estimate to source configurations in d_R0 or to the proposed cusp.

## 4. Obstruction when enhancement is omitted

For each m, concatenate m circles, each based at zero, of radius r=m^(-1/2), all positively oriented, on [0,1]. A single circle is

    z_r(u)=r(cos(2 pi u)-1, sin(2 pi u)),  0<=u<=1.

Its displacement vanishes at both ends, sup norm<=2r, length=2 pi r, and signed area=pi r^2, by (1/2) integral (x dy-y dx). Total area of the concatenation is pi because the first displacement of each completed circle is zero, so Chen cross terms vanish.

For every partition, intervals interior to one circle contribute at most its total length^p. On crossing intervals the endpoint counting argument of (7) applies and |z(t)-z(s)|^p<=2^(p-1)(|z(t)|^p+|z(s)|^p). Hence

    ||z_m||_p^p <= [(2 pi)^p+2^(2p)] m r^p,

so ||z_m||_p<=C_p m^(1/p-1/2) tends to zero for p>2. The crossing constant is 2^(p-1) times two endpoint incidences per circle times (2r)^p, namely 2^(2p) m r^p. The lift does not converge to the constant lift because its full-interval area is always pi. This rules out recovering lift continuity from first-level convergence alone, not continuity in an enhanced input topology or the authors' cusp conjecture.

## 5. First-attempt remaining gap and referee checks

The unsolved part is a theorem for **varying source configurations**: (a) stable intersections and roots in enhanced loop metrics; (b) changing chronological order of infinitely many small loops; (c) inverse clocks, including lambda -> 0, controlled in a topology yielding physical-time Hölder/p-variation estimates; (d) uniform enhanced small-loop tails for those perturbations. The source's conditions ensure qualitative first-level control, but contain no area information and no quantitative power modulus for intersection/hitting stability. No beta for the proposed cusp is proved here.

At the end of the first attempt we had not proved Brownian-loop-soup summability after selecting loops that intersect an SLE path. This gap is now resolved for bounded domains and compact intersecting sets of upper Minkowski dimension below two by CONTINUATION.md Proposition 4, with explicit tail exponents and an intersection-selection estimate. Identification of the full attached lift with a specified stochastic Stratonovich lift is still unproved. Uniform tails and enhanced matched-loop convergence across a particular coupling remain separate from the one-configuration summability result.

Hostile checks of Theorem 1:

1. Area of completed loops can accumulate although their first displacements vanish. The separate A hypothesis and alpha term retain that accumulation.
2. Global signed-area coordinates b_i(t) need not have q-variation controlled by the rough norm. The proof never makes that assertion: interior intervals use local rough increments; crossing intervals use at most two endpoint magnitudes.
3. Central backbone drift on intervals with stationary first level would invalidate the simple splice formula. Enhanced stationarity is explicitly assumed.
4. Partition endpoints may share a loop boundary. At such endpoints e=0; the area prefix/suffix decomposition remains valid.
5. Dense intervals and arbitrary exhaustion cause no order ambiguity: every finite construction uses actual temporal order; absolute area summability and the finite-pair estimate imply exhaustion independence.
6. The metric records increments at the same physical times. Retained waiting intervals are essential; no reparametrization quotient is used.
7. Tensor and antisymmetric metrics differ in their symmetric components. Section 1 supplies the required product estimate on the uniformly bounded first-level set.
8. Uniqueness is only of the prescribed enhanced concatenation limit. A first-level continuous path can admit different lifts.

Computational and Lean check results are recorded below once executed. They verify finite algebra and illustrative partitions, not the analytic supremum over all partitions; the latter is covered by the proof above.

### Finite computations completed

`python -X utf8 check_splice.py` exited 0. It constructs 12 based polygonal circles on a backbone with stationary attachment intervals, computes polygon signed areas directly, and compares these with (4) and (5). Maximum global-coordinate error was 6.661338147750939e-16; maximum error over 5000 randomly chosen increments was 7.771561172376096e-16. For p=2.5, 1000 randomly sampled partitions at each of seven truncation levels satisfied conservative bounds from (1). At full retention both differences were zero. Data and precise code are in numerical_checks.json and check_splice.py. This is a check of formulas and examples, not a numerical proof of the norm estimate.

The first Lean invocation failed at parsing because PowerShell's pipe converted the Unicode real-type symbol to a question mark. The diagnostic is preserved in lean_check_first_failure.json. The source now uses ASCII `Real`; no mathematical statement was changed by this encoding repair.

The rerun `lake env lean ~/brain_workers/TRIO_1011/op/P0139/SpliceAlgebra.lean`, executed from ~/lean_verify, **passed with exit code 0**, empty stdout and stderr, in 194.4068 seconds, with the requested 3600-second timeout. It imports only Mathlib.Data.Real.Basic and Mathlib.Tactic.Ring. Four polynomial identities are checked: the splice increment formula, the wedge difference formula, the Chen area cocycle, and central addition of two closed-loop signatures. All proofs use kernel-checked `ring`; there is no `sorry`, `admit`, `native_decide`, or unverified axiom declaration. This formalizes the algebraic step only, not the real-analysis partition theorem.

## Final verdict

**PARTIAL.** Theorems 1 and 2 and the conditional fixed-schedule source corollary are proved. The tiny-circle first-level obstruction is proved. The second attempt adds Theorem 3 and Propositions 4 and 5 in CONTINUATION.md, substantially narrowing the original gap. No exact solution in literature was identified; the later citing paper was fetched and screened. A full norm-adapted cusp statement or stochastic enhanced coupling/lift identification is still not proved. No full solution to P0139 is claimed.
