# Second serious attempt — F0034, 12 October 2026

## Starting gap and two untried approaches

The first attempt proves forward termination and shows that any infinite injective inverse chain has endpoint times a_n↑τ, b_n↓τ, with a common finite spatial limit x. Its gap is to exclude such a chain at an exceptional random backbone point z=(x,τ), where the particle time slice has a cluster point. Deterministic-horizon relevant-point finiteness cannot be substituted at τ.

**Approach A: bottlenecks, equivalence classes and one-path excursions.** Show that every complete backbone path through z must pass through all the chain's separation vertices before τ and meeting vertices after τ. That would force a single incoming and a single outgoing equivalence class. Combine this with the 20-type classification, then try to reduce the remaining one-sided cluster cases to nested excursions around a single, countably representable left- or right-web path. Such a reduction could isolate a scalar excursion mechanism with an accessible distribution or reveal a deterministic obstruction. This has not been attempted in the first record.

**Approach B: multiscale marked-web exclusion.** An inverse chain requires compatible split/merge events in every sufficiently small parabolic neighbourhood of its limit. Use the Poisson marking construction and a multi-arm or quasi-multiplicativity estimate to seek a summable bound on these compatible events, rather than assume independent steps of the orbit. The brain's exceptional-time recall points toward Schramm–Steif's arm-event techniques in neighbouring percolation. Neither independence nor a net arm exponent is supplied by that analogy; each would need proof. This differs from the first attempt's first-moment density subtraction.

I select A because it starts with deterministic consequences of the already proved geometry. B is retained as a separate lead, with its exact missing estimate to be stated below.

## Read-only brain consultation

2026-10-12: `python -X utf8 ~/.claude/dreaming/math_recall.py "Brownian net exceptional times cluster points inverse chain Kou Schertzer"` returned no direct Brownian-net card. Relevant hint: Schramm–Steif, *Quantitative noise sensitivity and exceptional times for percolation*, DOI 10.4007/annals.2010.171.619; linked technique card `claim_644045ce021d905aa60b2d065f197a6a96352a41bb3aa633d62cefdb1144e0c6` on arm-event quasi-multiplicativity. This is a hint, not a theorem about the Brownian net. Other recall hits were unrelated. No brain.py call is made because the previous recall script reported an unsolicited refresh.

## Source passages now under audit

- Schertzer–Sun–Swart, *Special points of the Brownian net*, arXiv:0806.2326v2, Theorem 1.7 (20 types), Theorem 1.12 (equivalence classes and concatenation), Section 3.3 (cluster-point isolation), and Proposition 3.11 (nested excursions). Source already retrieved as special_points.pdf/txt.
- R. Kou, *Special times for the point set process of the Brownian Net*, arXiv:2512.10761v1, Lemma 7 and Proposition 8, PDF page 5, restate the isolation and excursion facts. Source already retrieved as special_times.pdf/txt.

Proofs and computations are appended as soon as checked. The first-attempt results are not assumed immune from correction.

## Result A1: the limit is a common bottleneck for all backbone histories

Let s_0,m_0,s_1,m_1,... be a hypothetical injective inverse chain, indexed as in Theorem 5 of ATTEMPT.md, and let z=(x,τ) be its limit. Then for every n and **every complete backbone path π through z**,

    π(a_n)=x(s_n),   π(b_n)=x(m_n).

Thus all incoming backbone histories at z belong to one incoming equivalence class, and all outgoing backbone futures belong to one outgoing equivalence class. Equivalence means coincidence along a sequence of times tending to τ, not equality on a whole interval.

**Proof.** First fix n. There is a complete backbone path from s_{n+1} to z. To see this without assuming that the chain itself is a single path, for each k>n+1 concatenate a path from s_0 through s_{n+1} to s_k and extend it completely. Compactness and the common spatial barriers on [a_0,b_0] give a convergent subsequence. Since a_k→τ and x(s_k)→x, uniform equicontinuity implies that its limit passes through both s_{n+1} and z. All paths have start −∞, so the limit is a complete backbone path.

The forward extreme branches from s_{n+1} first meet at m_n. Any future through z can be appended to the preceding complete path's past up to τ by the image-set property. This complete path through s_{n+1} stays between those two extremes up to their reunion, and therefore passes through m_n. It follows that every backbone path through z passes through m_n.

Now take any backbone history through z and append a future going through m_n, again using the image-set property. The backward extreme backbone histories from m_n first meet at s_n because φ(m_n)=s_n. Every backbone history ending at m_n must have the same coordinate as those extremes at time a_n. The appended path thus passes through s_n, proving the claim for the original history. Finally a_n↑τ and b_n↓τ give the two equivalence assertions. ∎

**Referee qualification.** These conclusions are initially about backbone paths. They do not by themselves say that every outgoing path of the full Brownian net at z can be attached to a backbone past. Theorem 1.12(d) has continuation restrictions at points carrying a subscript l or r. In particular it would be wrong to discard all split-type cluster points solely because the backbone has one outgoing equivalence class.

## Result A2: one-sided limits have an actual scalar excursion spine

If the limit z has an incoming left-web path l, then, after discarding finitely many chain vertices, all s_n and m_n lie on that same l. The symmetric statement holds for an incoming right-web path. For the left-spine case the forward extreme excursions from s_{n+1} to m_n have the form

    l and r_n, with r_n∈Wr,
    r_n>l on (a_{n+1},b_n),
    r_n(a_{n+1})=l(a_{n+1}), r_n(b_n)=l(b_n).

Their intervals are strictly nested around τ, and r_n(τ) strictly decreases to x. The extra chain condition is the **backbone** backward reunion φ(m_n)=s_n, one step earlier than the departure s_{n+1} of this excursion.

**Proof.** The first attempt shows that z is a cluster point of the backbone time slice. The isolation criterion, special-points Lemma 3.7 with T=−∞, implies that it cannot have both a left- and a right-web incoming path. If l is incoming, z is consequently of class Cl. All incoming net paths at such a point form a single equivalence class (Theorem 1.12(a) and the list in Theorem 1.7). In particular l and a complete backbone path through z coincide along times increasing to τ. At one such time t after l's starting time, hop from the backbone past to l. Proposition 3.15(i) makes the concatenation a complete backbone path which agrees with l on [t,∞). Result A1 then puts every s_n with a_n≥t and every m_n on l.

At a separation point, the incoming left-web path continues as the left-most outgoing branch, and the incoming right-web path as the right-most outgoing branch; this is the (p,pp)_s structure. Thus the left extreme from s_{n+1} is the continuation of l. The right extreme can be chosen as an incoming right-web path r_n continued through that separation. Its first reunion with l is m_n by φ(s_{n+1})=m_n, proving the excursion relations with starting times strictly before a_{n+1}.

The endpoints satisfy a_{n+1}<a_{n+2}<τ<b_{n+1}<b_n. At a_{n+2}, r_{n+1}=l<r_n. Right-web paths cannot cross each other, so r_{n+1}(τ)≤r_n(τ). If equality held, they would coalesce at that interior time and thereafter; at b_{n+1} this would force r_n=l before its first reunion b_n, a contradiction. The convergence to x follows from equicontinuity, since both endpoints shrink to z. ∎

This reduction is stronger than merely saying that an exceptional time exists. It does **not** prove that the additional backward-reunion compatibility is impossible. Proposition 3.11(a) explicitly proves that ordinary nested excursions occur at every Cl point, so nested excursion intervals alone cannot be an exclusion argument.

**Countable-spine corollary.** In the one-sided case, the eventual spine may be chosen from Wl(Q²) or Wr(Q²), rather than an uncountable random family. In particular it suffices to exclude compatible infinite excursion ladders along each deterministic-seed skeletal path, and separately handle the two-sided Cn case.

**Proof.** Sun–Swart, *The Brownian net*, arXiv:math/0610625, Lemma 3.4(b), independently fetched in this attempt (PDF page 27), says that every Brownian-web path agrees after any fixed positive delay from its start with a path from a deterministic countable dense skeleton. Apply this to a finite-start incoming segment of l, with delay smaller than the time remaining until τ. The same lemma holds for the drifted web by undoing its deterministic linear space-time tilt. Thus some l_q, q∈Q², agrees with l from a time t<τ onward. Discard finitely many vertices with a_n≤t. All remaining excursions and backward-reunion conditions in A2 are unchanged. There are only countably many possible q, so almost-sure exclusion for each seed would give simultaneous exclusion of all one-sided chain limits. The reflected proof handles right spines. ∎

The time τ along a fixed skeletal path is still random and ranges over an uncountable exceptional set. This corollary does not justify a union bound over τ or conditioning on τ as a stopping time. Moreover, a two-sided Cn limit has no incoming actual web spine; replacing its reflected extended spine by an actual skeletal web path would be unjustified.

## Result A3: exact planar ladders realize arbitrary inverse depth

I constructed an explicit family with the exact inverse-map relations, rather than merely nested intervals. The construction shows that **planarity, trivalence of finite split/merge vertices, continuity, compactness and a single excursion spine do not imply inverse termination**. This is a deterministic graph result; it is NOT a Brownian-net counterexample.

### Infinite construction

Use t as the vertical coordinate and put a complete spine at x=0. For i≥0 set h_i=2^(−i), and use the vertices

    s_i=(0,−h_i), m_i=(0,h_i),
    p_i=(4h_i/3,h_i/3), q_i=(h_i/3,2h_i/3).

Add a root meeting m_{−1}=(0,2). For i≥1 add a piecewise linear rail R_i with consecutive vertices s_i,p_i,q_{i−1},m_{i−1}. Add R_0 with consecutive vertices s_0,p_0,m_{−1}. Add a side connector p_i→q_i for every i≥0. Arrows follow increasing t. Each s_i and p_i has indegree 1 and outdegree 2; each m_i and q_i has indegree 2 and outdegree 1. Between s_i and m_i the spine includes all smaller-scale spine vertices. The accumulation point z=(0,0) is already on the spine and is not designated a split or merge vertex.

For i≥1 the coordinate of R_i is

    t+h_i                         for −h_i≤t≤h_i/3,
    14h_i/9−2t/3                  for h_i/3≤t≤4h_i/3,
    2h_i−t                        for 4h_i/3≤t≤2h_i.

For R_0 the last two segments are replaced by the one segment 8/5−4t/5 on [1/3,2]. The connector p_i→q_i has coordinate 7h_i/3−3t on [h_i/3,2h_i/3].

### Planarity and compactness proof

All rails lie strictly to the right of the spine in the interiors of their intervals. Consecutive rails are strictly ordered R_{i+1}<R_i on their common open time interval. For i≥1 this is checked by splitting at the breakpoints h_i/6,h_i/3,2h_i/3: before h_i/6 the coordinate difference is h_i/2; while only the inner rail is in its middle segment the difference increases from that positive value; while both are in their middle segments it is 7h_i/9; after the inner rail reaches its last segment the difference is 5h_i/9+t/3>0. The outer rail remains in its middle segment until after the inner rail has ended. For R_0 versus R_1, before t=1/3 the same positive ordering holds; on [1/3,2/3] the difference is 37/45−2t/15>0, and on [2/3,1] it is 3/5+t/5>0.

On the open connector interval h_i/3<t<2h_i/3 for i≥1,

    R_{i+1}(t)=7h_i/9−2t/3
      < 7h_i/3−3t
      < 14h_i/9−2t/3=R_i(t).

These strict inequalities reduce to t<2h_i/3 and t>h_i/3, respectively. The connector attaches to the outer rail at its bottom and inner rail at its top. For i=0 the upper difference is (11/5)(t−1/3)>0 and the lower inequality is unchanged. Thus no connector crosses a rail except at its two prescribed endpoints. Different connectors lie in different adjacent-rail gaps; they cannot cross each other. Rails touch the spine only at their prescribed departure and return points. This proves planarity and that there are no unlisted intersections.

All edge slopes have absolute value at most 3. Every complete graph path, extended along the spine before −1 and after 2, is therefore 3-Lipschitz. On intervals avoiding 0 the graph has only finitely many vertices, which gives the Lipschitz bound directly; continuity extends the bound across 0. Every smaller-scale rail and connector has diameter tending to zero and accumulates only at z. Hence the graph is closed. The set of all complete continuous directed paths in this graph is closed, uniformly bounded on [−1,2], and uniformly Lipschitz, so it is compact by Arzelà–Ascoli. Each rail and connector belongs to a complete path, and allowing every continuous directed graph path makes the graph-path image property automatic.

### Exact φ relations in the graph

Define φ for these graph split vertices as first reunion of left/right extreme graph paths, and for graph merge vertices as first backward reunion of the extreme graph histories. Then

    φ(s_0)=m_{−1}, φ(m_{−1})=s_0,
    φ(s_{i+1})=m_i, φ(m_i)=s_i for every i≥0.

**Proof.** The left extreme from s_i stays on the spine. Its right extreme follows R_i: at p_i the connector goes left, so the right extreme continues along the rail. The rail next meets the spine at m_{i−1}, and not sooner, giving the first set of forward relations (including i=0 with the root meeting).

At m_i the left backward extreme follows the spine. The right backward extreme first follows R_{i+1} backward to q_i. At q_i the backward right choice follows the connector to p_i on the outer rail R_i; the other parent is on the inner rail. From p_i it follows R_i backward to s_i. This history is strictly right of the spine until s_i, where the two histories reunite. This gives φ(m_i)=s_i. The root backward extremes similarly reunite at s_0. No unlisted intersections exist, and a backward traversal from any fixed q_i reaches its negative-time rail departure after finitely many edges, so accumulation at z cannot supply a more extreme hidden route. ∎

It follows that s_0,m_0,s_1,m_1,... is an infinite injective inverse chain converging to z, while every vertex in that chain has a finite forward orbit ending in the root two-cycle. The time slice at 0 contains 0 and all h_i, so it has a one-sided cluster at 0. The spine is the common complete path through z; it passes through every s_i,m_i, as required by A1. Thus the geometry isolated by A1–A2 is consistent with an infinite chain in this deterministic model.

### Exact finite checks and what they certify

`ladder_check.py` truncates the family at rail N, keeping s_0,...,s_N and m_0,...,m_{N−1}. The innermost rail is joined directly to q_{N−1}. All coordinates and times are rational `Fraction` values. It checks the indegree/outdegree lists, all forward and backward first-reunion identities for s,m,p,q and the root, and every pair of overlapping-time straight edges for a crossing or an unlisted intersection.

At N=1,2,3,5,10,20,40,80 all checks passed. For N=80 there are 324 vertices, 322 exact φ identity checks, 19,999 overlapping edge-pair checks, and an injective inverse chain with 161 vertices. This is an exact finite construction, not a Monte Carlo test. The infinite claim above has its own proof and is not inferred from those eight truncations.

`LadderGeometry.lean` formalizes the two affine between-rail inequalities and endpoint identities. Its compiler process remained queued at the shared Lean slot, so this new file is NOT reported as checked. It imports only Real.Basic and Tactic.Linarith, contains no sorry and no native_decide, and does not purport to check the Brownian-net law.

### Why this does not disprove Conjecture 8.1

The graph is deterministic and its paths are Lipschitz. Its extremal paths are not Brownian motions with drift, its branching is not a Poisson marking of Brownian-web intersection local time, and it does not have the stationary Poisson time-slice law. Nor have I embedded this graph with positive probability in the Brownian net. It is a counterexample only to the proposed implication from the listed geometric assumptions to inverse termination. In particular it invalidates a strategy which would try to finish A2 using just planar nesting and first-reunion ordering.

## Approach B: an explicit sufficient probabilistic target

The following reduction makes clear what a marked-web estimate would need to prove. For rational U and integer K≥1 let

    C_{U,K}=R_{−∞,U} ∩ ([-K,K] × [-K,min(K,U−1/K)]).

Empty rectangles are allowed. Each cohort has finite expected cardinality by source Proposition 4.7, since it is spatially and temporally bounded and stays distance at least 1/K below U. The countable union of these cohorts contains every finite backbone separation: choose rational U strictly between its time and its forward reunion time, or above its time if that reunion is +∞, and then choose K large enough.

Let Q_N(U,K) count the roots in C_{U,K} from which there is an injective inverse φ-chain of N edges. A sufficient condition for part (b) is

    E[Q_N(U,K)] → 0 as N→∞ for every rational U and integer K.

**Proof of sufficiency.** An infinite injective inverse chain has a finite-separation tail root after discarding its at most two formal endpoints and an optional meeting vertex. That root lies in one of the countably many cohorts. For a fixed cohort, existence of an infinite inverse chain rooted there implies Q_N≥1 for every N, so its probability is at most E[Q_N] for every N by Markov's inequality. The stated limit gives probability zero. A countable union over the cohorts still has probability zero. ∎

No such moment limit or quantitative rate is proved here. For example a bound E[Q_N]≤A(U,K)ρ^N with ρ<1 would suffice, but it remains a **conjectural sufficient estimate**, not numerical evidence or a proved property of the net. Counting separate ordinary excursions will not yield it: compatible backward reunions must be included in Q_N. Conditioning on an adaptively selected deepest excursion does not preserve the unconditioned Poisson-mark law without a further argument. The percolation quasi-multiplicativity card supplies neither that conditional law nor a Brownian-net arm estimate.

**Referee check on the converse.** I do not claim the moment limit is necessary for part (b). A rooted functional graph can have arbitrarily deep finite inverse branches but no infinite inverse ray if its preimage sets are not finite. Finite branching of the Brownian φ-preimage graph has not been established here, so applying König's lemma to infer a ray from finite chains of every depth would be an additional gap.

## Result B1: an exact return-duration measure and summability obstruction

There is one further rigorous consequence of the source density which restricts how rapidly a hypothetical inverse chain must collapse. For a separation s let H(s)=time(φ(s))−time(s) when φ(s) is finite, and omit nonreturning separations. The expected marked counting measure of (s,H(s)) has density

    dx dt ν(dh),   ν(dh)= (2/√π) e^(−h) h^(−3/2) dh, h>0.

Consequently for every bounded Borel spacetime region A and every p>1/2,

    E[ sum_{s∈S∩A, H(s)<∞} H(s)^p ]
       = |A| (2/√π) Γ(p−1/2).

In particular the expected total finite return-duration weight is 2|A| (p=1), and the second-power weight is |A| (p=2). These are unconditioned marked intensities, not a duration distribution obtained by selecting a uniformly random separation from an infinite-intensity set.

**Proof of the marked intensity.** The law is invariant under space and time translation, and H is unchanged by translating its vertex. For each δ>0 the marked process restricted to H≥δ has a locally finite expected counting measure: on a time interval of width at most δ/2 all such vertices lie in R_{−∞,U} for U equal to the top of the interval, whose expected count on a bounded spatial interval is finite by Proposition 4.7 and the integrability of its (U−t)^(−1/2) singularity. Cover a compact time interval by finitely many such intervals. The possible deterministic-top vertices have zero expected count and do not affect this conclusion.

A locally finite translation-invariant measure on R² is a constant multiple of Lebesgue measure. Applying this for each lifetime-mark Borel set bounded away from 0, and exhausting (0,∞), yields the product form dx dt ν(dh), with ν finite above every positive lifetime threshold. This is the usual uniqueness of Haar/Lebesgue measure, not an assumption of independence between marks or vertices.

Fix a deterministic U. The source's relevant-minus-permanent density gives the vertices whose finite H satisfies H≥U−t, for t<U, intensity 4g(U−t), where

    g(h)=Ψ(h)−2=e^(−h)/√(πh)−erfc(√h).

The product intensity simultaneously gives ν([U−t,∞)) at those same spacetime points. Equality of the two measures on all bounded test sets below U shows

    ν([h,∞))=4g(h)

for Lebesgue-almost every h>0. A tail function is monotone, and g is continuous, so one-sided limits extend this equality to every h and show that ν has no atoms. Differentiation gives

    g'(h)=−e^(−h)/(2√π h^(3/2)),

since the derivatives of the two h^(−1/2)e^(−h) contributions cancel. This gives the asserted density for ν. Tonelli's theorem then computes the weighted expectation as |A|∫h^pν(dh)=(2|A|/√π)Γ(p−1/2), finite precisely when p>1/2. For p≤1/2 the expectation is infinite; **almost-sure divergence is not inferred from that alone**. ∎

**Corollary: every hypothetical inverse chain has p-summable widths for all p>1/2.** Put w_n=b_{n−1}−a_n=H(s_n) for n≥1. Theorem 5 of the first attempt bounds the chain in a finite spacetime rectangle. The weighted sum over every deterministic rational rectangle is finite almost surely for each rational p>1/2 by the preceding finite-expectation identity. A countable intersection and enlargement to one such rectangle containing the entire hypothetical chain give ∑_n w_n^p<∞ simultaneously for rational p>1/2. Since w_n→0, comparison extends this to every real p>1/2.

The widths w_n decrease. For a decreasing summable sequence u_n=w_n^p, the tail bound

    floor(n/2) u_n ≤ sum_{k=floor(n/2)}^n u_k →0

shows n w_n^p→0. Thus w_n=o(n^(−1/p)) for every p>1/2, equivalently w_n=o(n^(−2+ε)) for every ε>0. In particular ∑(τ−a_n) and ∑(b_n−τ) are finite (use p=1 and the decomposition w_n=(τ−a_n)+(b_{n−1}−τ)). The assertion is simultaneous over chains because it follows from a countable family of weighted-count probability-one events, not by conditioning on a chosen chain. ∎

**Referee limits.** A geometric or faster width decay is compatible with all these estimates. In the deterministic ladder, w_n=3·2^(−n) for n≥1, and ∑w_n^p=3^p/(2^p−1) for every p>0. Therefore even the strengthened p-summability condition does not exclude a collapsed ladder. It supplies no estimate on the number of compatible backward-reunion choices. The mean lifetime measure has a short-duration h^(−3/2) singularity, which explains why counting small excursions alone is inadequate. Numerical evaluations of the exact Gamma constants and the dyadic comparison sums are saved in lifetime_moments.json; the proof above does not rely on numerical quadrature.

## What survived, what failed, and what remains

The first-attempt proof of (a) survives this audit: it uses finite forward reunions, the ancestral cone, and a deterministic positive-gap horizon, none of the unsupported random-horizon or finite-branching shortcuts discussed here.

Approach A has reached a rigorous bottleneck and countable one-sided-spine reduction. The proposed purely geometric exclusion then fails: the explicit planar ladder realizes the exact offset between forward excursion bottoms and backward reunion bottoms. The 2009 classification already allows cluster-point bottlenecks and ordinary nested excursions, so it supplies no contradiction at that stage.

The new lifetime calculation gives the additional necessary p-summability constraint for all p>1/2. It still allows the explicit rapid-collapse mechanism. No infinite compatible ladder has been shown to occur with positive probability in the Brownian net, and no theorem excludes it.

The remaining gap is now precise: exclude infinite **backbone backward-compatible** excursion ladders along each fixed skeletal left/right path at a random one-sided cluster time, and exclude the analogous construction at two-sided Cn limits whose incoming extremes are reflected rather than actual web paths. A bound on Q_N for finite-intensity root cohorts would handle both without treating the limit as deterministic. The bound is unproved. Full F0034 remains PARTIAL.


## Verification status at close

The exact rational ladder tests completed successfully. The earlier TemporalSqueeze.lean check remains verified with exit code 0 in lean_check.log. The new LadderGeometry.lean command was submitted from ~/lean_verify and reported waiting for a shared Lean slot. No compiler result has been returned; see ladder_lean_check.log. It is unverified, and none of the new mathematical claims relies on an asserted Lean success. I did not bypass the shared slot or kill any process. The affine identities are proved in the written geometry argument and checked exactly in the rational finite tests.
