# C0017: independent cell comparison, with the gap exposed

Parent result: **not proved**. Current openness: **UNKNOWN**. The historical catalog statement and exact target are in STATEMENT_FOR_ADVERSARY.md. An October 2026 primary manuscript claims the parent result; its correctness has not been established here. The lemmas below do not depend on the parent being open and carry no novelty claim.

## Sources and prior-attempt digest

The 7 September catalog gives C0017 as square-lattice independent bond percolation at p=1/2, with both Cardy's formula and SLE_6 interface convergence. C0017-A001 tried a discrete holomorphic observable and stopped at the weak contour relations. Its stated spin sigma=2/3 is wrong in the standard convention used by Duminil-Copin: sigma=1-(2/pi)arccos(sqrt(q)/2), so q=1 gives sigma=1/3; sigma=2/3 gives q=3. The primary paper's Conjecture 1, Eq.(3.3), PDF page index 9, is explicitly conjectural for general q; the proved exceptional case uses q=2 and sigma=1/2. Thus the prior attempt supplies neither the missing square-bond limit nor a correct parameter.

Targeted C0017 searches in attempts_H_20260912 and attempts_I_20260914 returned no exact-ID hits. The Lean directory returned only the annotated ranking; no C0017 formal theorem was located. The Team O board contains nearby C0018 and C0050 work, but no C0017 row. No claim that the owner's work is exhausted follows from these bounded negative searches.

Brain-assisted choice: the ordinary recall took 55.62 s and its top three returned FPP reconnaissance, an unrefereed percolation-entropy result, and lecture-transcript delivery. None supplies the square-bond transfer theorem. In particular, a result using alpha_4 must not import the triangular exponent 5/4 to square bonds. The gap scar perceptron_proof_open_gaps_fleet_2026_07_12 warns that a passed pipeline does not certify the hardest mathematical step. This packet therefore proves elementary transfer lemmas while isolating the unverified model comparison.

## Definitions

A cell has a finite ordered terminal set T. Its state is a partition pi of T: terminals in the same block are connected inside the cell. For three distinct terminals there are five states: 1|2|3, 12|3, 13|2, 23|1, 123. On a fixed deterministic skeleton, terminals of different cells may be identified or joined by deterministic connections. Given all cell partitions, an event A (for example connection between two specified boundary sets) is a well-defined Boolean function f of the partitions.

Let mu_i and nu_i be two laws on cell i's same finite state set Omega_i. Let eta_i=TV(mu_i,nu_i)=sup_B |mu_i(B)-nu_i(B)|. For an exterior state x_{-i}, set

S_i(x_{-i})=1 if f(x_{-i},pi) is nonconstant as pi ranges over Omega_i, and 0 otherwise.

S_i is exterior sensitivity, not a claim that every changed cell is pivotal, and not an assumption about an arm exponent. Define the exterior hybrid law H_i=(product_{j<i} nu_j) times (product_{j>i} mu_j).

## Lemma L1: weighted comparison of independent cells

For every Boolean f on the finite product of the Omega_i, if the two complete laws are product laws mu=product mu_i and nu=product nu_i, then

|E_nu f - E_mu f| <= sum_i eta_i P_{H_i}(S_i=1).

Proof. Replace cells one at a time. In the i-th difference the exterior has exactly law H_i and the only replaced law is mu_i versus nu_i. Conditional on a fixed exterior x, if S_i(x)=0 the difference of the conditional expectations is zero. If S_i(x)=1, the set B_x={pi:f(x,pi)=1} satisfies |nu_i(B_x)-mu_i(B_x)|<=eta_i by the definition of total variation. Integrate this pointwise inequality over H_i, then use the triangle inequality in the telescoping sum. All conditioning and averaging are explicit. No conditional estimates are multiplied. QED.

This is the useful bridge: it asks for error only where the crossing event is sensitive, rather than matching all local laws exactly. It allows nonidentical cells and any Boolean event. It requires a common deterministic skeleton and independence of the cell partition variables in each endpoint law; these requirements are not consequences of RSW.

## Lemma L2: no exact finite independent-bond replacement of a three-terminal site

Let G=(V,E) be a finite undirected graph with three distinct terminal vertices a,b,c. Let each edge be independently open with 0<p_e<1. Its induced terminal-partition law cannot equal mu_p, where mu_p(1|2|3)=1-p and mu_p(123)=p, with 0<p<1, and all partial partitions have probability zero.

Proof. If a,b,c lie in different connected components of the deterministic graph so that all three cannot be connected, the mass on 123 is zero and differs from p. Otherwise choose a minimal subtree T connecting the three terminals, inside a spanning tree of their common component. Every leaf of T is a terminal. Choose one leaf, call it c after relabeling. The unique path P between the other two terminals a,b avoids c. Declare exactly the edges of P open and every other edge of G closed. The resulting terminal partition is ab|c. This particular configuration has probability product_{e in P} p_e times product_{e not in P}(1-p_e)>0, by the assumed independence and nondegeneracy. Thus a partial partition has positive mass, contradicting mu_p. QED.

If all p_e=1/2 and m=|E|, this argument also proves TV(law_G,mu_p)>=2^(-m) in the common-component case. If all three cannot connect, TV>=p. The finite-network bound depends on m; it does not rule out growing gadgets, approximate substitutions, dependent bonds, or universality. An occupied site is represented here as joining all three exposed neighbors simultaneously; the lemma concerns that explicit three-terminal representation only.

## Lemma L3: matching pair probabilities still leaves a crossing bias

Consider a star with terminals a,b,c and one central vertex, whose three edges are independent with common probability t. Set t=1/sqrt(2). Then P(a connected to b)=P(a connected to c)=P(b connected to c)=t^2=1/2. These agree with a fair all-or-none site cell. Nevertheless

P(a connected to {b,c})=t[1-(1-t)^2]=2t^2-t^3=1-1/(2sqrt(2)),

whereas the fair site cell gives 1/2. The bias is (1-1/sqrt(2))/2>0, approximately 0.1464466094. The external connections can designate a as one boundary set and both b,c as the other, so this is a bona fide crossing witness on the cell skeleton. This refutes the proposed inference 'matching the three pair-connectivity probabilities transfers every crossing probability.' The calculation uses independence of the three specified edges only. QED.

## Counterexample C1: independence cannot be dropped from L1

Let X=(Z,Z) and Y=(Z,1-Z), with Z a fair bit. Both coordinates have the same fair marginal, so all marginal eta_i are zero. For f(x)=1{x_1=x_2=1}, E f(X)=1/2 but E f(Y)=0. A bound obtained by inserting these marginal distances into L1 would say 1/2<=0. Thus product-law hypotheses are essential; block partitions that share unexplored random bonds cannot be substituted as if independent.

## Conditional bridge to the crossing part of C0017

Suppose for each small delta there is an explicit common deterministic planar skeleton and independent cell laws mu_delta,nu_delta such that its mu crossing probability approximates critical triangular-site crossing in the chosen marked Jordan domain with error r_mu(delta)->0, and its nu crossing probability approximates the square-bond crossing with error r_nu(delta)->0. Suppose further

B_delta=sum_i eta_{delta,i} P_{H_{delta,i}}(S_{delta,i}=1) -> 0.

Then L1 bounds the absolute difference of the two actual crossing probabilities by r_mu+r_nu+B_delta. The triangular-site theorem identifies the reference limit as Cardy's value, so the square-bond crossing has that value. This is a conditional corollary with a complete proof; none of its model-specific comparison assumptions has been proved here. It does not establish convergence of exploration curves to SLE_6.

As an arithmetic diagnostic only, if the number of cells is O(delta^-2), eta_i=O(delta^beta), and every relevant hybrid sensitivity is O(delta^a) uniformly, then B_delta=O(delta^(beta+a-2)), and beta+a>2 suffices. The value a=5/4 is not an available square-bond or arbitrary-hybrid assumption merely because it holds in the triangular reference model. In particular a fixed nonzero cell error and a=5/4 yield a bound growing like delta^-3/4, so this bound cannot close the argument. A four-arm interpretation of S_i would itself require a geometrical proof for the chosen cells and boundary locations.

## Single hardest remaining gap G1

Construct a geometrically faithful independent comparison between the two models, on common mesoscopic cell skeletons, and prove its total error r_mu(delta)+r_nu(delta)+B_delta tends to zero, uniformly for the marked domains needed. There is currently no such construction or estimate in this packet. L2 eliminates exact fixed finite independent-bond gadgets as one way to obtain it; L3 eliminates pair matching as a substitute. A stronger interface theorem requires additional tightness and identification after this crossing gap is closed.

NEXT: Have w419 independently rederive L1 and L2, and seek an explicit mesoscopic representation for G1 without assuming the square-lattice four-arm exponent or independence of overlapping blocks.
