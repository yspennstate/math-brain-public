# F0033 — research attempt, 2026-10-12

## Exact target and current outcome

For the infinite-volume wired stationary sandpile law ν on Z², with stable heights {0,1,2,3}, is η+δ₀ stabilizable using finitely many TOTAL legal topplings for ν-almost every η?

The source is verified in LITERATURE.md. No proof or counterexample for this ν has been obtained. The results below are deterministic reductions and bounds, valid without a stationarity assumption. They should not be presented as new literature results or as a solution of Question 6.7.

## 1. Least action, including barriers with negative final heights

For any finite wired domain D, define Δ_D v(x)=4v(x)−Σ_{y∈D,y∼x}v(y). Let h be a nonnegative initial configuration on D. Suppose v:D→N satisfies h−Δ_D v≤3 coordinatewise. The expression h−Δ_D v need NOT be nonnegative. Then every legal toppling sequence has cumulative counts at most v.

Proof. Suppose a first toppling would exceed v. Immediately before it, the toppling count t at that vertex x equals v(x), and t(y)≤v(y) at every vertex y. The current height at x is

    h(x)−4t(x)+Σ_{y∈D,y∼x}t(y)
       ≤h(x)−4v(x)+Σ_{y∈D,y∼x}v(y)≤3.

This contradicts legality, which requires height at least four. Therefore no first excess exists. In particular every legal sequence has length at most Σ_D v and an algorithm that topples some unstable vertex whenever one exists must terminate. At termination its heights are nonnegative (a legal toppling subtracts four from a height at least four) and at most three. If u and u' are counts of two terminating legal stabilizations, applying the same argument to each with the other as barrier yields u≤u' and u'≤u. Thus u=u'. This also proves independence of toppling order in the finite setting used here. QED.

The local contradiction is the theorem first_excess_impossible in LeastAction.lean. The entire lattice argument is a written proof, not a claim of full Lean formalization.

## 2. Explicit finite-box bound

Write B_r={x:||x||∞≤r}, r≥1, and let u_r stabilize (η|B_r)+δ₀ with a wired sink outside B_r. Set

    H_r(x)=(r+1)²−x₁²,  x∈B_r;
    v_r(x)=2H_r(x).

Then Δ_{B_r}H_r≥2. To see this, extend the quadratic expression to all lattice neighbours. Its full lattice Laplacian is exactly two:

    4(A−a²)−[(A−(a−1)²)+(A−(a+1)²)+2(A−a²)]=2.

For any neighbour of a vertex in B_r, the extended H_r is nonnegative, since |x₁|≤r+1. Removing outside neighbours from the Laplacian sum therefore increases the value. Consequently Δ_{B_r}v_r≥4. Because η(x)+δ₀(x)≤4, this v_r is a stable upper barrier. By §1,

    u_r(x)≤2((r+1)²−x₁²),
    S_r:=Σ_{x∈B_r}u_r(x)≤K_r:=2(r+1)²(2r+1)².             (1)

This proves finite stabilization in each box for EVERY stable initial state. It also excludes infinitely many topplings confined to a fixed finite box. It says nothing about escape through boxes with r→∞.

## 3. Domain monotonicity

If D⊂E are finite domains containing 0, with the same restricted initial η, then u_D≤u_E on D. Indeed, restrict u_E to D and note

    η+δ₀−Δ_D(u_E|D)
     = (η+δ₀−Δ_Eu_E)|D − Σ_{y∈E\D,y∼x}u_E(y)≤3.

This restriction is a nonnegative integer upper barrier, possibly with negative resulting heights. §1 yields the asserted inequality. Thus u∞(x):=lim_{r→∞}u_r(x) is well defined in N∪{∞} (extending u_r by zero outside B_r). QED.

## 4. Finite local certificates: an exact reduction

Let ∂B_r={x:||x||∞=r}. Define the cylinder event

    C_r={η: u_r(x)=0 for every x∈∂B_r}.

This is determined solely by the finitely many heights in B_r.

**Theorem.** For every stable η, the following are equivalent:

(a) η+δ₀ has a finite legal stabilization on the full lattice.
(b) η∈C_r for some r≥1.
(c) u∞ has finite support.

Moreover C_r⊂C_{r+1}. On C_r the full avalanche counts equal u_r (zero outside B_r), and its total size is at most K_r.

Proof of (b)⇒(a). Run the finite legal stabilization in B_r. Since no vertex on ∂B_r topples, it sends no grain outside B_r. Every height and legal toppling inside the box is therefore identical on the full lattice. At the end, heights inside are stable, and outside they equal the original stable heights. This is a finite full-lattice stabilization.

Proof of (a)⇒(b). A finite sequence has finite toppling support. Choose r so that all its topplings lie in B_{r−1}. Restriction of that sequence to B_r is a legal stabilization with no boundary topplings: outside B_r the full-lattice sequence has no topplings and inside final heights are stable. Finite abelianness from §1 makes its count equal u_r. Thus C_r holds.

For the assertions about counts and nesting, on C_r the same sequence stabilizes every B_m, m≥r, and has no topplings on their boundaries. Finite abelianness gives u_m=u_r extended by zero; thus C_m holds and u∞=u_r.

This proves (b)⇒(c). Conversely, if the support of u∞ is finite, choose r so it lies inside B_{r−1}. Since u_r≤u∞, the boundary counts u_r vanish, proving (b). Infinite values inside the support cause no exception: the conclusion C_r implies by the preceding paragraph that every u_m agrees with finite u_r. QED.

Hence for ANY probability law μ on stable configurations,

    μ(finite total avalanche)=lim_{r→∞}μ(C_r).               (2)

Proof: the event on the left is the increasing countable union of C_r, and probability is continuous from below. Measurability follows because each C_r is a finite cylinder. QED.

## 5. Exact finite-volume tail criterion for ν

For n≥r let R_n be the maximum ||x||∞ of a vertex toppled in B_n, with value −1 for an empty avalanche. Define p_{n,r}=ν_n(R_n≥r). Then

    q_r:=ν(C_r^c)=lim_{n→∞}p_{n,r}.                        (3)

Proof. For every fixed stable state on B_n, C_r^c is EXACTLY {R_n≥r}. If u_r has a boundary toppling, domain monotonicity forces u_n to have the same boundary toppling. If u_r has no boundary toppling, its stabilization is also a stabilization in B_n with no counts outside B_{r−1}, by the proof of §4. These exhaust the cases. Equivalently the avalanche cannot jump over a boundary: a non-origin vertex needs grains from an earlier toppling neighbour before its first toppling.

The event C_r is clopen in the product of finite discrete height spaces, so its probability converges under ν_n⇒ν. This proves (3). QED.

Combining (2) and (3) gives an exact restatement of the open question:

    ν(finite total avalanche)=1
       ⇔ lim_{r→∞}lim_{n→∞}ν_n(R_n≥r)=0.                  (4)

This is a uniform tightness criterion, not just convergence along r=n. More explicitly it is equivalent to

    lim_{r→∞}sup_{n≥r}ν_n(R_n≥r)=0.                       (5)

Proof of the nontrivial direction. If q_r→0, choose r₀ with q_{r₀}<ε. For some N≥r₀, all n≥N satisfy p_{n,r₀}<2ε by (3). For r≥N and n≥r, p_{n,r}≤p_{n,r₀}<2ε. This proves (5). Conversely q_r≤sup_{n≥r}p_{n,r}, so (5) implies (4). QED.

The same equivalence holds for tightness of total toppling counts S_n. If R_n<r, the certificate C_r holds, and (1) gives S_n≤K_r. Thus uniformly small radius tails yield uniformly small tails beyond deterministic K_r. Conversely if R_n≥r, the set of toppled vertices contains a nearest-neighbour path from 0 to ∂B_r, and hence at least r+1 vertices, so S_n≥r+1. To justify connectivity, consider the first toppling of each vertex: except at 0, its initial height was at most three, so an earlier neighbouring toppling supplied a grain; tracing strictly earlier first topplings must end at 0. Therefore tight total counts yield tight radius tails. Finitely many n<r can be included without effect because they have deterministic finite bounds (1). QED.

**Precise missing estimate:** prove q_r→0, or equivalently (5), for the actual wired recurrent laws ν_n. No such estimate is obtained here. Finite-domain termination, weak convergence alone, lower tail bounds, and infinite mean do not supply it.

## 6. Small deterministic cases and limits of proposed arguments

If η(0)≤2, adding one grain leaves a stable configuration and no topplings occur. If η(0)=3 and all its four neighbours have height at most two, one toppling at 0 stabilizes the lattice. These are exact special cases, with no probabilistic independence assumed.

For η≡3, the addition does NOT admit finite total stabilization. Indeed, suppose a finite full-lattice stabilization exists. It must topple 0. If x has toppled but an adjacent vertex y never topples, y starts at three, receives a grain from x, and has final height at least four, contradiction. Thus the nonempty finite toppling support has no edge to its complement; this is impossible in connected infinite Z². This is a deterministic counterexample to a universal assertion over all stable states, NOT a counterexample to the ν-almost-sure question; no positive ν-mass of that state is shown.

For finite waves starting with origin height exactly four, each non-origin vertex topples at most once. Proof: immediately after the previous completed wave all non-origin heights are at most three. After the origin topples once and is frozen, suppose a first second toppling occurs at y≠0. Each neighbour has toppled at most once before that moment, so y has received at most four grains in the entire wave. Its current height before a second toppling is at most 3+4−4=3, contradiction. The origin begins at four, loses four, and receives one grain from each neighbour in the wave. Thus its height at wave end is the number of those neighbours, and a next wave occurs iff all four participated. This local fact is also formalized in LeastAction.lean.

This argument applies to a COMPLETED finite wave. It cannot assume that an infinite-volume forward wave terminates. The prior attempt's substitution of a UST past for each numbered forward wave is unproved. BHJ Theorem 1.7(iii) instead proves finiteness of waves under conditioning on N=k. Countable union over finite k leaves {N=∞} untouched. Via that theorem one may derive ν(R=∞,N<∞)=0, but that is a literature-dependent reduction, not a new proof of N<∞.

For completeness the reduction using that theorem is exact: on each event {N=k} with k finite, all k waves are almost surely finite, so their finite union and the sum of their finite toppling counts are finite. Take the countable union over k, including k=0 (the empty avalanche). Conversely a finite total avalanche plainly has a finite origin count N. Therefore, using BHJ Theorem 1.7(iii), the target is equivalent to ν(N<∞)=1. Alternatively Theorem 1.8(ii) gives q_r≤ν(N>k)+C_k r^(−α_k) (the radius norm can be changed by fixed constants); if N were finite a.s., first r→∞ and then k→∞ would give q_r→0. No bound on ν(N>k) tending to zero has been established here.

The September 2026 comb and Vicsek results concern different recurrent graphs. They rule out a recurrence-only theorem with no graph-specific input. The Z² proof must exploit more than recurrence and finite-box abelianness.

## 7. Hostile-referee checklist and computational record

### A failed stopping route can be ruled out rigorously

Let N∈{0,1,2,…,∞} be the limiting number of origin topplings/waves, as in BHJ Theorem 1.9. That theorem proves EνN=∞. Put a_k=ν(N≥k). There do NOT exist ε>0 and k₀ such that

    a_{k+1}≤(1−ε)a_k for all k≥k₀.                        (6)

Proof. We may assume 0<ε≤1. Iterating (6) gives a_{k₀+j}≤(1−ε)^j a_{k₀}. Pointwise for every extended nonnegative integer N, N=Σ_{k≥1}1_{N≥k}; this equality also holds when N=∞. Applying monotone convergence to the nonnegative finite partial sums gives EνN=Σ_{k≥1}a_k. Its tail is bounded by a_{k₀}/ε, and its first k₀−1 terms are at most k₀−1. This contradicts EνN=∞. QED.

In fact a_k>0 for every finite k, since otherwise N would be bounded and have finite mean. Therefore all ratios a_{k+1}/a_k exist, and (6)'s impossibility implies

    limsup_{k→∞}ν(N≥k+1 | N≥k)=1.                        (7)

The ratios lie in [0,1]. If their limsup were less than one, they would eventually be at most 1−ε for some ε>0, contradicting (6). This proves (7).

Any proposed uniform lower bound ε on conditional stopping given the entire surviving wave history implies (6) after taking its conditional expectation over {N≥k}. Thus the earlier intake's suggested uniform stopping criterion is not merely missing a proof: it is incompatible with the known infinite mean. A possible proof of finiteness must allow stopping hazards tending arbitrarily close to zero along some sequence. This does not distinguish infinite-mean almost-sure finiteness from positive probability of N=∞, and hence does not answer the target question.

- Height convention checked against source: 0,…,3; instability starts at four.
- Source's infinite expected counts are not used as an almost-sure conclusion.
- Least action permits a negative formal barrier final state; its first-excess proof explicitly verifies why this is legitimate.
- Quadratic sign and wired boundary corrections are derived in §2, rather than assuming the full-space and killed Laplacians coincide.
- Weak convergence is used only on the finite cylinder C_r, not on an unbounded odometer.
- The two limits in (4) are in the stated order; (5) is proved separately. A diagonal boundary-escape estimate alone would not prove (4).
- Finiteness of support versus total counts is proved in §4, including the possibility of infinite counts at finitely many sites.
- Wave sampling bias and the last-wave/forward-wave distinction are checked against BHJ rather than inherited from the brain.
- finite_checks.py exhaustively enumerates 3×3 stable states, retains recurrent states via the burning test, compares ordinary and wave toppling counts, checks the wave continuation identity and quadratic bound, and searches for failures of nesting. It also compares certificates against full 5×5 avalanches for 10,000 seeded arbitrary stable states. Exact outputs are saved in finite_results.json. These tests check finite statements only; they do not sample ν or estimate its infinite-avalanche probability.
- The exhaustive test retained exactly 100,352 recurrent 3×3 states, with wave-count histogram N=0: 63,872; N=1: 35,328; N=2: 1,152. All comparisons and inequalities passed. Runtime reported by Python: 7.61 seconds.
- further_checks.py found a recurrent 5×5 state after three retained states where the second wave contains (1,−2), which the first wave misses. Heights in rows indexed by first coordinate −2,…,2, with second-coordinate columns −2,…,2, are [[3,1,3,1,3],[3,3,3,3,2],[2,3,3,3,3],[1,3,3,3,2],[1,3,3,3,1]]. The wave vertex lists are in further_results.json. On saturated wired B_r, r=1,…,12, all computed waves were the successive boxes B_r,B_{r−1},…,B₀, and their count was r+1. These are exact computed examples, not a proof for all r.
- LeastAction.lean formalizes three local algebraic ingredients. The final command exited 0 with no diagnostics; details and the corrected initial import failure are in LEAN_CHECK.md. No full measure-theoretic or sandpile theorem is claimed Lean-checked.

## Remaining gap

The proof stops precisely at the stationary-tail estimate (5). I have neither an upper bound tending to zero nor a positive lower bound on the infinite-avalanche probability. Therefore the verdict is PARTIAL, not SOLVED.

## Second serious attempt requested by the user

See SECOND_ATTEMPT.md for two new approaches (hole geometry/bootstrap with compact integer barriers; wave-chain/group-orbit recurrence), the pursued bootstrap approach, and complete new proofs. It constructs an allowed translation-ergodic periodic law with finite saturated components and low mean but positive infinite-avalanche probability, proves that finite saturated components always admit a compact REAL barrier, and separates this from the required INTEGER barrier. It also gives an everywhere-finite law with identical one-site marginals. None of these laws is ν. Exact construction checks and fresh finite-volume stationary Wilson/burning samples are retained. The stationary uniform-tail gap remains unresolved.
