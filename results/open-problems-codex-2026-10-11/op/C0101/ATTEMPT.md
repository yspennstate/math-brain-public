# C0101 — checked partial results, 2026-10-12

## Exact object and scope

Write K=2d-1, q_A(x)=x^T A x/2 and Δf(x)=sum_i(f(x+e_i)+f(x-e_i)-2f(x)). Matrices are real symmetric; A≤B means B-A is positive semidefinite. In the survey, p.21, S_d is the set of A for which Δceil(q_A) stabilizes locally under the nearest-neighbor sandpile rule (unstable means height≥2d); Γ_d is its Euclidean closure. The question on p.27 asks for maximal elements in d≥3 and their isolation and rationality. Isolation here means isolation within the set of maximal elements, not within Γ_d, which has downward directions.

No full classification, isolation theorem, or rationality theorem for all maximal elements is established below.

## 1. Least-action connection, with no growth assumption hidden

**Lemma 1.** A belongs to S_d iff there is an integer function g≥ceil(q_A) with Δg≤K.

Proof. Put h=ceil(q_A) and s=Δh. If stabilization occurs, its finite-at-each-site odometer u is nonnegative integer, and its final heights s+Δu≤K. Then g=h+u is the required function. Conversely, such a g gives w=g-h≥0 integer and s+Δw≤K. Every finite legal toppling sequence has odometer v≤w: otherwise immediately before the first violation at x, v(x)=w(x) and v(y)≤w(y) at every neighbor; hence (s+Δv)(x)≤(s+Δw)(x)≤K, contradicting legality. Enumerate the countable lattice and apply a fair toppling schedule (at stage n inspect the first n vertices, toppling an inspected unstable vertex once). The number of topplings at each x is bounded by w(x). Thus all these counts stabilize, and every vertex is eventually stable: an eventually unstable vertex would be revisited and topple indefinitely. Neighbor counts also eventually stabilize, so final heights exist and are ≤K. This proves local stabilization. □

**Lemma 2 (trace bound).** Every A in Γ_d satisfies tr A≤K.

Proof for S_d. Take g from Lemma 1. For ε>0, H(x)=g(x)-q_A(x)+ε|x|²≥ε|x|². Thus H attains a global minimum on the lattice (only finitely many points lie below any fixed value). At a minimizer x, ΔH(x)≥0, whereas ΔH≤K-tr A+2dε. Therefore tr A≤K+2dε. Let ε decrease to zero. The trace bound passes to the closure by continuity. □

**Lemma 3 (witness-to-closure).** If integer g satisfies Δg≤K and g=q_A+o(|x|²), then A belongs to Γ_d.

Proof. For every ε>0, g(x)-q_{A-εI}(x)=o(|x|²)+ε|x|²/2 tends to +∞ and has a finite lower bound. Choose an integer constant C making g+C≥ceil(q_{A-εI}) everywhere. Lemma 1 gives A-εI∈S_d. Let ε decrease to zero. □

The ε perturbation is essential: a representative with an unbounded linear error need not majorize q_A itself. Membership in the closure is what this lemma proves.

## 2. An explicit family maximal in the full matrix set

**Theorem 4.** Every symmetric integer matrix M with tr M=K is a maximal element of Γ_d. More generally, every symmetric integer matrix with tr M≤K belongs to Γ_d.

Proof. Define

    P_M(x)=sum_i M_ii*x_i*(x_i-1)/2 + sum_{i<j} M_ij*x_i*x_j.

Each consecutive product x_i(x_i-1) is even, so P_M is integer. A diagonal binomial term has directional second difference M_ii in direction i and zero in other directions; each mixed term is affine in each coordinate and has second difference zero. Thus ΔP_M=tr M. Expanding gives P_M=q_M-(1/2)sum_i M_ii x_i=q_M+O(|x|). Lemma 3 proves membership when tr M≤K. Now if B∈Γ_d and B≥M with tr M=K, D=B-M is positive semidefinite and tr D≤0 by Lemma 2. Each D_ii≥0, so each is zero. For i≠j, evaluating the quadratic form on e_i+e_j and e_i-e_j gives respectively 2D_ij≥0 and -2D_ij≥0; therefore D_ij=0. Hence B=M, proving maximality against all matrices, including non-diagonal competitors. □

This is an infinite rational family in every dimension. It does not classify maximal elements of lower trace and does not prove isolation of this family from other maximal elements.

## 3. Complete classification within the separable-witness class

Call diag(a_1,...,a_d) *separably representable* if there are integer functions f_i on Z with f_i(n)=a_i n²/2+o(n²), and g(x)=sum_i f_i(x_i) satisfies Δg≤K.

**Theorem 5.** This occurs iff sum_i ceil(a_i)≤K.

Necessity. Set b_i(n)=f_i(n+1)+f_i(n-1)-2f_i(n). The inequality sum_i b_i(n_i)≤K holds for every independent tuple. Fix all but one variable; it follows that each b_i is bounded above. Its integer supremum m_i is attained. Choose a maximizer in each coordinate; then sum_i m_i≤K. We show a_i≤m_i. For ε>0, H_i(n)=f_i(n)-(a_i-2ε)n²/2 tends to +∞, hence attains a minimum. There its second difference is nonnegative, while everywhere it is ≤m_i-a_i+2ε. Thus a_i≤m_i+2ε, and letting ε decrease to zero gives a_i≤m_i. Since m_i is integer, ceil(a_i)≤m_i; summing proves necessity.

Sufficiency. Fix real a and define f(0)=0 and integer increments f(n+1)-f(n)=floor(a n) for every integer n. Equivalently,

    f(n)=sum_{k=0}^{n-1} floor(a k)       if n>0,
    f(n)=-sum_{k=n}^{-1} floor(a k)      if n<0.

Replacing each floor(a k) by a k incurs error at most |n|. In both signs the sum of a k equals a n(n-1)/2, so f(n)=a n²/2+O(|n|). Its second difference is floor(a n)-floor(a(n-1))≤ceil(a): indeed a n≤a(n-1)+ceil(a), and monotonicity of floor, plus floor(t+j)=floor(t)+j for integer j, gives the inequality. Construct f_i this way and sum them; then Δg≤sum_i ceil(a_i)≤K. □

**Corollary 6.** Every separably representable diagonal A is dominated by an integer diagonal matrix of trace K, maximal in the full Γ_d. Consequently, a maximal element of Γ_d that has a separable representative must itself be integer diagonal of trace K.

Proof. Put c_i=ceil(a_i), s=sum_i c_i≤K, and M=diag(c_1+K-s,c_2,...,c_d). Then M-A is diagonal with nonnegative entries, tr M=K, and Theorem 4 applies. If A was maximal, A=M. Conversely every integer diagonal trace-K matrix has the separable binomial representative in Theorem 4. □

No claim is made that every diagonal member of Γ_d admits a separable representative. A coordinate restriction of a general representative does not control its one-dimensional Laplacian, since the other directions can supply negative contributions. Closure also must not be silently identified with existence of separable representatives.

## 4. Order structure and the rationality mechanism

**Theorem 7.** Γ_d is downward closed, and every A∈Γ_d lies below at least one maximal element.

Proof of downward closure. If A≤B∈S_d, the witness g≥ceil(q_B) in Lemma 1 also satisfies g≥ceil(q_A), so A∈S_d. If B∈Γ_d choose B_n∈S_d tending to B and set A_n=A+B_n-B. Then B_n-A_n=B-A is positive semidefinite, so A_n∈S_d, and A_n tends to A. Hence A∈Γ_d.

For existence, fix A∈Γ_d. The closed set T={B∈Γ_d:B≥A} is nonempty. Put t=K-tr A≥0. For B∈T, D=B-A is positive semidefinite and 0≤tr D≤t. In particular 0≤D_ii≤t. For i≠j, positivity of the quadratic form on se_i+e_j for every real s implies D_ij²≤D_ii D_jj (if D_ii=0 the linear coefficient must vanish; otherwise minimize the quadratic). Thus |D_ij|≤t. Therefore T is bounded and compact in finite dimension. The continuous trace has a maximizer M on T. If C≥M belongs to Γ_d, then C∈T and tr(C-M)≤0. The argument in Theorem 4 shows C=M. Hence M is maximal. □

**Theorem 8 (integer harmonic shifts).** If H is symmetric integer with tr H=0, then Γ_d+H=Γ_d.

Proof. If B∈S_d, take g_B≥ceil(q_B) with Δg_B≤K. The binomial polynomial P_H in Theorem 4 is integer, has ΔP_H=0, and P_H=q_H-l(x), where l(x)=(1/2)sum_i H_ii x_i. For ε>0,

    g_B+P_H-q_{B+H-εI} ≥ ε|x|²/2-l(x).

The right side has a finite lower bound; adding an integer constant yields an integer majorant of ceil(q_{B+H-εI}), of Laplacian ≤K. Thus B+H-εI∈S_d. For general A∈Γ_d choose B_n∈S_d tending to A and ε_n decreasing to zero; then B_n+H-ε_n I tends to A+H, proving inclusion in Γ_d. Repeat with -H to obtain equality. The shift preserves Loewner order, so it also maps maximal elements bijectively to maximal elements. □

**Lemma 9 (full-rank cocycle implies rationality).** Suppose an integer-valued function g on Z^d and a real matrix A satisfy

    g(x+v_j)-g(x)=x^T A v_j+c_j

for all x∈Z^d and for d linearly independent integer vectors v_j. Then A has rational entries, with denominators dividing |det V| for V=[v_1 ... v_d].

Proof. Subtract the identity at x from the identity at x+e_i. Its left side is an integer and its right side is (Av_j)_i. Hence every column Av_j is integer. Therefore W=AV is an integer matrix, V is an invertible integer matrix, and A=WV^{-1}=W adj(V)/det V. Both W and adj(V) are integer, giving the assertion. □

In particular, a representative g=q_A+b·x+r(x) with r periodic under a full-rank sublattice has this cocycle: the quadratic increment is x^TAv_j+q_A(v_j) and the linear increment is b·v_j. This proves rationality for that class. There is no proof here that all maximal matrices possess such representatives.

## 5. A noninteger-maximal existence result

**Theorem 10.** In every d≥3 there exists a maximal member of Γ_d that is not an integer matrix.

Proof. Let A_d have diagonal entries 1,1,2,...,2, entries A_12=A_21=1/2, and all other off-diagonal entries zero. Its trace is 2d-2. Set

    g_d(x)=floor((x_1²+x_2²+x_1*x_2)/2)+sum_{i=3}^d x_i².

This is integer and differs from q_{A_d} by an error r which is zero if x_1,x_2 are both even and -1/2 otherwise: x_1²+x_2²+x_1*x_2 is odd in each of the other three parity classes. The planar Laplacian of the floor term is 0,3,3,2 in parity classes (even,even), (odd,even), (even,odd), (odd,odd), respectively. Explicitly, the quadratic planar Laplacian is 2; the error's Laplacian is

    2r(1-a,b)+2r(a,1-b)-4r(a,b),

where a,b are the parity bits. Substitution gives -2,1,1,0 in the four classes. Each of the remaining squared coordinates contributes 2. Thus Δg_d≤3+2(d-2)=2d-1. Moreover g_d+1≥ceil(q_{A_d}), so Lemma 1 gives A_d∈S_d (not merely Γ_d).

No integer symmetric matrix M in Γ_d dominates A_d. Indeed, if it did, D=M-A_d would be positive semidefinite. Every D_ii would be a nonnegative integer and, by the trace bound, sum_i D_ii≤1. Consequently at least one of D_11,D_22 would vanish. Positive semidefiniteness then forces D_12=0 by the quadratic-form argument in Theorem 7. But D_12=M_12-1/2 cannot be zero when M_12 is integer, a contradiction.

Theorem 7 supplies a maximal B≥A_d. Such a B cannot be integer by the preceding paragraph. □

This does not prove A_d itself maximal, does not determine B, and does not prove B irrational. The conclusion is strictly weaker than a negative answer to the source's rationality question.

## Remaining gap

We have not controlled maximal elements without separable representatives, in particular those with trace<K. No result here proves all maximal elements rational or isolated, or produces an irrational/nonisolated maximal element in d≥3. A periodicity mechanism for maximal representatives, or a maximality certificate for a nonperiodic example, is still missing.

Theorem 10 proves existence of noninteger maximal matrices, but neither identifies them nor answers the question about *rational* entries.

## Computation and hostile self-referee

All computations were bounded runs lasting seconds; no long lattice evolution or growing search was used. `check_math.py` performed 480 exact integer quadratic/Laplacian checks in dimensions 1–6 and 56,303 exact rational floor-increment checks including negative curvatures and negative lattice indices. It reproduced the old false ceiling bound. Results: `math_checks.json`, all passed (about 15 seconds).

`periodic_search.py` formulates a period-two witness as g(x)=q_A(x)+b·x+r(x), with r periodic and eight integer g-values on {0,1}³. Cocycle offsets across cell boundaries are calculated exactly. An integer linear program enforces the eight inequalities Δg≤5. The original zero-linear-phase, bounded-value run is retained as `periodic_results.json`; it missed obvious integer examples because it excluded their allowed linear terms. The corrected run tests all eight phases b_i∈{0,-1/2}, which exhaust the affine-cocycle constants modulo adding integer linear functions, for 14 half-integral candidate matrices, with no bounds except the gauge g(0)=0. It returned 23 feasible certificates out of 112 phase cases in about 44 seconds (`periodic_phase_results.json`). Solver infeasibility is recorded only as numerical evidence within the periodic ansatz, never as exclusion from Γ. Time-limited failures likewise give no exclusion.

Each feasible certificate was extended by its exact cocycle and checked on all 343 points of [-3,3]³, including negative coordinates and boundary crossings: 7,889 exact checks. The explicit witness in Theorem 10 was separately checked in dimensions 3–8 on 486 lattice points and all four parity classes. Results: `periodic_checks.json`, all passed. Theorem 10's proof is the complete parity calculation, not an inference from floating-point solver output.

`WitnessAlgebra.lean` imports only `Mathlib.Tactic.Ring` and `Mathlib.Tactic.Linarith`. `lake env lean <absolute problem-folder path>/WitnessAlgebra.lean`, run from `~/lean_verify`, exited 0. The synchronous runner allowed a 3,600-second timeout; actual elapsed time including the shared-slot wait was about 473 seconds. `lean_result.json` and `lean_output.txt` retain the result. The checked statements are the one-variable binomial second difference, the zero mixed second difference, the complete three-dimensional witness Laplacian, its linear growth error, and the zero-diagonal off-diagonal implication. They use `ring` and `linarith`, with no `sorry`, added axioms, or `native_decide`. These are kernel-checked algebraic lemmas; the infinite-lattice arguments are written proofs, not Lean formalizations.

Referee checks:

1. **Normalization:** the survey sandpile stabilizes at heights≤2d-1, hence that is the bound on Δg, not 0 or the planar paper's 1. Checked against the source definition and toppling rule.
2. **Closure versus exact stabilization:** the binomial witness can have an unbounded linear error, so adding a constant alone need not dominate q_A. Lemma 3 first subtracts εI. A factor 1/2 in this perturbation was corrected during review. Theorem 10 has bounded error and does stabilize exactly after adding 1 to its witness.
3. **Infinite graph least action:** the proof bounds each vertex's toppling count before invoking a fair schedule; no finite-support assumption is used or needed.
4. **Trace argument:** minima exist because the ε perturbation makes the error coercive, regardless of the sign of q_A; trace passes to closure by continuity.
5. **Full maximality:** Theorem 4 excludes every positive-semidefinite increase through the trace bound; it is not merely maximal in a diagonal or integer slice.
6. **Separation:** only genuinely separable witnesses are classified. Independent coordinate maximizers exist because their second differences are bounded integer sequences. Negative curvatures and indices were tested exactly.
7. **Compactness:** a positive-semidefinite increment of bounded trace has bounded entries; the closed upper section is therefore compact. No compactness of the entire unbounded Γ is claimed.
8. **Periodicity/rationality:** Lemma 9 needs a full-rank affine cocycle. Periodic pictures or finite numerical patterns do not supply that hypothesis for all maximal elements.
9. **Noninteger versus irrational:** Theorem 10 excludes integer dominators using a trace gap of 1 and the half-integral off-diagonal entry. It does not exclude rational dominators. A maximal extension is obtained only existentially.
10. **Isolation:** no spacing between different maximal families is proved. The integer trace-ceiling family is discrete among itself, which does not imply isolation among all maximal elements.
