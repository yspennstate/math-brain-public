# Finite local extinction certificates for adjacent Richardson seeds

Consider the nearest-neighbor two-type Richardson process on Z². Initially type 1 occupies o=(0,0), at rate 1, and type 2 occupies e=(1,0), at rate r>0. Write C for the event that both eventual occupied sets are infinite.

The bounds below concern these adjacent seeds in dimension two. They do not prove the unequal-rate conjecture.

## 1. A finite certificate for extinction in the infinite process

Let K be a finite set containing o but not e. Let G be a finite induced lattice graph containing K, every nearest neighbor of every vertex of K, and e.

Construct an auxiliary process on the entire lattice. Type 1 uses all its usual rate-1 infection arrows. Type 2 uses its usual rate-r arrows only on edges with both endpoints in G. Stop the process at the first of the following events:

1. A type-1 birth occurs outside K: failure.
2. Every neighbor of the current type-1 set is already infected: success.

Before stopping, both infections are contained in G. Indeed, type 1 is contained in K, every neighbor of K belongs to G, and type 2 has no permitted exit from G. Each effective transition infects a previously uninfected vertex. Consequently the stopped experiment has finitely many transitions. At a nonterminal state with some exposed type-1 neighbor, its total transition rate is positive. Thus it terminates almost surely.

Let q(G,K;r) be the probability of success. Then

    P(type 1 has a finite eventual set) >= q(G,K;r).                 (1)

To prove this, couple the auxiliary and original processes using the same directed Poisson arrows for each type. The original process has all the auxiliary type-2 arrows and additional type-2 arrows outside G. At all times,

    type 1 in the original process ⊆ type 1 in the auxiliary process,
    type 2 in the auxiliary process ⊆ type 2 in the original process.

These inclusions hold initially. At a type-1 birth in the original process, its source is type 1 in the auxiliary process. Its target cannot already be auxiliary type 2, since it is uninfected in the original process; the same arrow either infects the auxiliary target or finds it already type 1. At a type-2 birth in the auxiliary process, the symmetric argument applies. Additional original type-2 arrows preserve both inclusions. This proves the coupling claim by induction over arrows affecting a finite exploration. The usual nonexplosive construction extends it to all times: the total effective infection rate with n infected vertices is at most 4 max(1,r)n, and the corresponding linear-rate pure-birth process is nonexplosive.

On auxiliary success, type 1 is contained in K and all its neighbors are infected. Those neighbors outside its own set are type 2 and remain so forever. Auxiliary type 1 cannot make another birth. The coupled original type-1 set is therefore finite, proving (1).

At least one type has an infinite eventual set almost surely. To see this, fix a finite nearest-neighbor path from either seed to an arbitrary vertex. Inductively, once a vertex on the path is infected, its infection type sends an arrow to the next vertex after a finite waiting time, unless that next vertex is already infected. Every fixed vertex is eventually infected. Taking a countable intersection, the union of the two eventual sets is the whole lattice almost surely. Hence their two extinction events are disjoint.

Apply the same experiment after the lattice isometry x ↦ e-x, exchange the types, and rescale time so that the tested type again has rate 1. The competitor ratio is then 1/r. Thus

    P(C) <= 1 - q(G,K;r) - q(G,K;1/r).                             (2)

The finite graphs for the two certificates are images of one another; they need not be disjoint. Disjointness is needed only for the two actual extinction events, which was proved above.

## 2. Exact finite-state recurrence

A transient state is a pair (S,F) of disjoint occupied subsets of G, where o∈S⊆K and e∈F. Put H=G\(S∪F). For v∈H define

    s_v = number of nearest neighbors of v in S,
    f_v = number of nearest neighbors of v in F,
    h = Σ_{v∈H} s_v,       b = Σ_{v∈H} f_v.

All possible type-1 births are counted in h because G contains every neighbor of K. The probability Q(S,F;r) of success satisfies

    Q(S,F;r) = 1,                                                    if h=0,

    Q(S,F;r) = [r Σ_{v∈H} f_v Q(S,F∪{v};r)
                  + Σ_{v∈H∩K} s_v Q(S∪{v},F;r)] / (rb+h),          if h>0. (3)

A birth at v∉K has success probability zero and contributes only to the denominator. Formula (3) follows from the exponential race between all infection edges. Every child state has one fewer healthy vertex, so this is an acyclic, exact recurrence. In particular, q(G,K;r)=Q({o},{e};r) is a rational function of r, and it is a rational number at rational r.

`cluster_bounds.py` evaluates (3) with bit masks. A separate implementation propagates probability mass forward using coordinate sets, counting edges afresh. Both use exact integer fractions. Agreement is checked at every reported ratio and its reciprocal.

## 3. A four-site allowed region

Use

    K = {(0,0), (-1,0), (0,1), (0,-1)}.

Let N(K) denote the union of all nearest neighbors of vertices in K. Use the induced graph with vertex set

    G = K ∪ N(K) ∪ {(1,2), (1,-2), (-2,1), (-2,-1)}.

For explicitness, the rows of this 16-vertex graph are

    y= 2:  (0,2), (1,2)
    y= 1:  (-2,1), (-1,1), (0,1), (1,1)
    y= 0:  (-2,0), (-1,0), (0,0), (1,0)
    y=-1:  (-2,-1), (-1,-1), (0,-1), (1,-1)
    y=-2:  (0,-2), (1,-2).

There are at most 3³ 2¹¹=55296 possible states: the three initially healthy sites of K have three possible states, and the eleven other initially healthy sites have two. Only 2735 states are reached by (3), including success states. The calculation gives the following bounds from (2). Decimal values in this table are rounded upward to twelve places; exact fractions are in `cluster_data.json`.

| r | upper bound for P(C) |
|---:|---:|
| 1 | 0.963212367649 |
| 3/2 | 0.935503608356 |
| 2 | 0.879513957511 |
| 3 | 0.746557074658 |
| 5 | 0.517827898619 |
| 10 | 0.233499308635 |
| 100 | 0.003975074607 |

These are bounds for the infinite-lattice process, not estimates of finite-box coexistence probabilities.

## 4. A bound valid at every positive ratio

For the graph in Section 3, G\S is connected whenever S={o} or S={o,v} with v∈K\{o}. Here is a direct check. Deleting o leaves the original eight-cycle, with outer attachments connected to it. If v=(0,1) is also deleted, a connected backbone is

    (0,2), (1,2), (1,1), (1,0), (1,-1), (0,-1),
    (-1,-1), (-1,0), (-1,1), (-2,1), (-2,0), (-2,-1).

Consecutive entries are neighbors, and the remaining vertices (0,-2),(1,-2) attach to (0,-1),(1,-1). The case v=(0,-1) follows by reflecting y. If v=(-1,0) is deleted instead, the path

    (-1,1), (-2,1), (-2,0), (-2,-1), (-1,-1)

connects the remaining left part to the original cycle with (-1,0) deleted. The upper and lower outer pairs attach through (0,±1) and (1,±1). This proves all four connectivity assertions. They are also checked by graph searches in the scripts.

Rescale time so that the competitor has rate 1 and the tested type has rate ε=1/r. Until the first tested birth, its occupied set is {o}. That birth, if it occurs, is into one of K\{o}, because the remaining neighbor e was infected initially.

If there is no second tested birth, connectivity ensures that the competitor eventually occupies every other vertex of G. The tested type is then surrounded. Therefore auxiliary failure requires at least two tested births.

For a state (S,F) with |S|=2 as above, run only the competitor at rate 1, keeping S fixed and forbidden. Let F_t denote its growing occupied set, and let h(S,F_t) be the exposed tested-edge count from Section 2. Define the finite reward

    A(S,F) = E[∫_0^∞ h(S,F_t) dt].                                (4)

Connectivity implies the competitor eventually fills G\S. While h>0, at least one competitor edge is active. There are finitely many births, so (4) is finite. The conditional probability of a further tested birth is

    E[1-exp(-ε ∫_0^∞ h(S,F_t) dt)] <= ε A(S,F).                    (5)

This identity follows by conditioning on the competitor trajectory and requiring no tested arrow to any exposed site. It concerns the first subsequent tested birth only.

Now run the competitor alone with S₀={o}. Conditional on its trajectory, the density of the first tested birth at v at time t is

    ε s_v(S₀,F_t) exp(-ε ∫_0^t h(S₀,F_u) du) dt.

The exponential factor is at most 1. At that first birth, the Markov property and the memorylessness of the edge clocks allow (5) to be applied from (S₀∪{v},F_t). Consequently

    1-q(G,K;r) <= ε² B,

where

    B = E[∫_0^∞ Σ_{v∈K\(S₀∪F_t)}
                      s_v(S₀,F_t) A(S₀∪{v},F_t) dt].             (6)

This argument discards only factors between zero and one, so it gives an inequality for every ε>0, not merely an asymptotic expansion.

Both rewards have finite recurrences. At h=0 their values are zero. Otherwise b>0 by the connectivity just proved, and

    A(S,F) = h/b + Σ_v (f_v/b) A(S,F∪{v}),

    B(F) = Σ_v (f_v/b) B(F∪{v})
               + (1/b) Σ_{v∈K\(S₀∪F)} s_v A(S₀∪{v},F).         (7)

The waiting time to the next competitor birth has mean 1/b and its target distribution is f_v/b, proving (7). In (6), B=B({e}). Exact evaluation gives

    B = 2977401937361 / 53747712000
      = 55.39588247702525… .

The backward reward recursion and an independent forward propagation of occupation weights both give this fraction; see `audit_bounds.py` and `audit_data.json`. The value is also smaller than the elementary bound 1638: before the second tested birth there are at most fourteen births, the tested hazard before its first birth is at most 3, after its first birth at most 6, and the competitor hazard is at least 1. Summing (3/r)(6/r) over the 91 possible ordered birth positions gives 1638/r².

Since coexistence excludes auxiliary success, (1) gives P(C)≤1-q(G,K;r). Combining this with (6), the reflected experiment, and the probability bound 1 yields

    P(C) <= min{1, B/r², B r²,
                   1-q(G,K;r)-q(G,K;1/r)}.                       (8)

All the constants and finite-state probabilities in (8) have thus been specified by terminating exact recurrences.

## 5. The leading coefficient of this certificate

The restricted failure probability has the expansion

    1-q(G,K;r) = L/r² + O(r⁻³),

    L = 33393164656111 / 806215680000
      = 41.41964177143143… .                                     (9)

Here is an exact way to compute and check (9). Write ε=1/r and Z(S,F;ε)=1-Q(S,F;1/ε). With f_v,s_v,b,h as above, its recurrence is

    Z = [Σ_v f_v Z(S,F∪{v};ε)
           + ε(Σ_{v∉K} s_v + Σ_{v∈K} s_v Z(S∪{v},F;ε))]
          / (b+εh).                                              (10)

At h=0 it is zero. If b=0<h, cancel ε from numerator and denominator. Every expression then has a denominator nonzero at ε=0. Induction over the number of healthy vertices proves analyticity at zero for every state. Expand (10) through degree two by coefficient division. For numerator A(ε)+εD(ε), the coefficients obey

    b z₀=A₀,
    b z₁=A₁+D₀-hz₀,
    b z₂=A₂+D₁-hz₁

when b>0; use the canceled recurrence when b=0. `cluster_bounds.py` computes exactly (z₀,z₁,z₂)=(0,0,L) at the initial state.

For an independent positive calculation of L, use the two-insertion reward in (7) but weight the second tested birth by its zero-order eventual failure probability. A birth outside K has weight 1. For a birth within K, freeze the resulting tested set and fill every vertex reachable by the existing competitor without crossing that set. The weight is 1 if some unfilled vertex lies outside K, and 0 otherwise. Indeed, any remaining component is inaccessible to the competitor and is adjacent to the tested set, since G is connected. It will eventually be filled by the tested type. It causes failure exactly when it contains a vertex outside K.

Before the second tested birth, both the constant and first-order failure terms vanish by connectivity. Thus at order ε² there are no holding-time corrections from lower-order failures: the two-insertion weight just described is precisely the coefficient in (10). `audit_bounds.py` computes it by both backward integration and forward propagation, using separate reachability implementations. Both yield the fraction L in (9), also agreeing with the coefficient division.

Equation (9) is an asymptotic statement about the finite certificate. For the original process it implies only

    limsup_{r→∞} r² P(C) <= L.

It does not assert an asymptotic formula for the actual coexistence probability.

## 6. Independent singleton checks

For K={o}, remove o from the competitor graph and let T_v be its rate-1 hitting time of a neighbor v of o. The independent first type-1 arrows from o to these neighbors have exponential rate 1. The type remains a singleton exactly when all these arrows lose their races to the competitor. Consequently

    q(G,{o};r) = E exp[-(Σ_{v∼o} T_v)/r].                        (11)

The initially occupied neighbor has T_e=0. Suppressing the tested growth does not change the competitor process before the first tested birth, so (11) is an equality for the restricted singleton experiment. Removing the restriction on competitor edges can only shorten its hitting times and improves this lower bound on singleton trapping.

In the punctured 3-by-3 box, the graph is an eight-cycle. Number the cycle from e as 0,…,7; the three other neighbors of o are 2,4,6. The competitor's occupied vertices form an interval on this cycle. Until completion, its two advancing edges have total rate 2. At the final vertex the two edges have the same target but still total rate 2. Each front choice is a fair coin; an arbitrary final fair coin accounts for its duplicate target.

Among the 128 seven-coin sequences, each of the following eight triples (n₁,n₂,n₃) occurs sixteen times. Here n_k is the number of waiting intervals during which exactly k of the targets 2,4,6 remain uninfected:

    (1,2,3), (1,3,2), (2,1,3), (2,2,2),
    (2,2,3), (2,3,2), (3,1,3), (3,2,2).

Intervals with zero exposed targets contribute no factor. With x_k=2r/(2r+k), this gives the explicit formula

    q_cycle(r) = (1/8) Σ_{the eight triples} x₁^n₁ x₂^n₂ x₃^n₃.

For example q_cycle(1)=7/600, and (2) gives P(C)≤293/300 at equal rates. Its integrated exposure A=ΣT_v has moments

    E A=27/4,       E A²=431/8.

For a triple n, the conditional mean of A is (n₁+2n₂+3n₃)/2 and its conditional variance is (n₁+4n₂+9n₃)/4. Averaging over the eight triples proves these numbers independently of the state recurrence. A second check on the mean uses the two edge-disjoint arcs to cycle vertex k. Their traversal times are independent Gamma(k,1) and Gamma(8-k,1). Therefore

    E T_k = Σ_{i=0}^{k-1} Σ_{j=0}^{7-k}
                    binomial(i+j,i) / 2^(i+j+1).

Summing over k=2,4,6 again gives 27/4. The integral follows by multiplying the two integer-gamma survival polynomials and integrating e⁻²ᵗ t^(i+j).

`trapping_bounds.py` checks the cycle formula, both moments, and the forward/backward singleton recurrences. It also computes the 5-by-3 singleton certificate, which has 981 reached states. At r=2 its coexistence upper bound is exactly

    1183866617620303957642961 / 1284216233024601676800000.

The singleton certificates are auxiliary checks; the stronger reported bounds use (8).
