# F0033 — second attempt, 2026-10-12

## The gap carried forward

ATTEMPT.md proved that the requested ν-almost-sure finite total avalanche is equivalent to

    lim_{r→∞} sup_{n≥r} ν_n(R_n≥r)=0.

Using BHJ's conditional finite-wave theorem, it is also equivalent to ν(N<∞)=1. Neither estimate is available. The known infinite mean excludes a uniformly positive stopping hazard.

## Two approaches not tried in the first attempt

**A. Hole geometry and heterogeneous bootstrap closure.** Represent the first wave by activation thresholds 4−η(x), then try to use the stationary law's deficit field d(x)=3−η(x), its spatial structure, and allowedness to build compact integer barriers Δv≥δ₀−d. This is different from merely bounding a finite-box odometer: it attempts to construct a barrier before taking an infinite-volume limit. Relevant neighbours are bootstrap percolation, robust sandpile backgrounds (Fey–Levine–Peres), and dependent-percolation crossing estimates. The first test is whether subcritical mean density, translation ergodicity, and the absence of forbidden subconfigurations actually suffice. They must not be assumed to do so.

**B. Finite sandpile-group orbits and a return-time interpretation.** Addition at 0 permutes the recurrent configurations in each finite wired box. Try to encode forward waves as an induced transformation and apply recurrence of a measure-preserving transformation instead of an expectation bound. This would accommodate an infinite mean return time. The key obligations are to construct an infinite-volume transformation without first assuming stabilization, identify a finite invariant measure on its section, and show that return corresponds to termination. The existing wave bijection concerns a size-biased ensemble; EνN=∞ means its unnormalized mass diverges. Merely invoking Poincaré recurrence or Kac's lemma without those constructions would be circular.

I pursue A: its activation and integer-barrier claims can be proved or refuted directly before importing any probabilistic hypothesis. Approach B is recorded as a genuine alternative but is not claimed established.

## Brain consultation

Read-only math_recall queries: `sandpile avalanche wave number tail tightness Jarai Hanson` (the actual gap), and `Fey Levine Peres robust backgrounds sandpile explosive` (neighbouring theorem/author). Outputs will be retained locally when returned; hints are not treated as proofs.

## Working record

The immediate experiment is an allowed, periodic ladder background: all heights are at least two, saturated components are finite, but a seed column may launch bootstrap activation indefinitely. If correct, this rules out a broad class of coarse-density/cluster arguments while identifying precisely which ν-specific estimates would still be required.

## 1. Exact first-wave reduction

If η(0)≤2, the avalanche is empty. Otherwise η(0)=3. Set A₀={0} and

    A_{j+1}=A_j ∪ {x≠0: η(x)+|{y∼x:y∈A_j}|≥4},
    A_∞=∪_{j≥0} A_j.

Then A_∞ is exactly the set reachable by legal topplings when 0 is toppled once and thereafter frozen. In particular A_∞ infinite implies there is no finite total full-lattice stabilization.

Proof. Every A_j is finite: activation can only occur adjacent to the previous finite active set. Topple 0, then each newly activated vertex in increasing layer order. A vertex not previously toppled has its original η height plus one grain from each already toppled neighbour; the activation inequality makes this toppling legal. Each neighbour topples at most once. No non-origin vertex can legally topple twice in such a wave: at a first attempted second toppling it has received at most four grains, and after its first toppling its current height is at most 3+4−4=3. Thus these finite prefixes are legal and realize all A_j. Conversely, induct on the toppling order of an arbitrary finite legal frozen-origin prefix: any newly toppled vertex has received enough grains from already toppled distinct neighbours, so it belongs to the closure. This establishes equality, with infinite waves understood through their finite prefixes, without presupposing wave termination.

For the last conclusion, suppose a finite legal stabilization with counts u exists. Its final heights satisfy η+δ₀−Δu≤3. The global first-excess proof from ATTEMPT.md §1 bounds the counts of EVERY finite legal prefix by u, even for prefixes with the origin frozen. But the prefixes just constructed visit infinitely many distinct sites as j grows, contradicting finite support of u. QED.

This reduction controls only the first wave. Finiteness of this closure alone does not prove a finite number of subsequent waves.

## 2. Compact integer barriers: an exact existence formulation

Let d=3−η. A finite total stabilization exists iff there is a finitely supported v:Z²→N with

    Δv≥δ₀−d.                                           (8)

Necessity: take v to be the finite legal stabilization counts; its final heights are η+δ₀−Δv≤3. Sufficiency: the global first-excess argument bounds every legal sequence by v, so it has at most Σ_x v(x) topplings. Choose an unstable vertex and topple while any remains. After at most that many steps the procedure terminates, since otherwise the next legal step would violate the bound. No grains or unstable sites can appear outside the finite one-neighbourhood of supp(v)∪{0}. Final heights are stable. QED.

This formulation identifies the real issue: a compact INTEGER supersolution, not a real-valued one. The construction below separates those requirements exactly.

## 3. A periodic allowed counterexample to coarse geometric hypotheses

Fix even p≥6 and q≥4. Define η_{p,q}:Z²→{2,3} by height three at precisely

    y≡0 (mod q) and [x odd or x≡0 (mod p)],
    or y≡−1 (mod q) and x even,

and height two elsewhere. The horizontal pairs of rows y=mq−1,mq are ladders. At x=kp their two sites both have height three; call these seed columns. Every other column has one height-three site and one height-two site.

### Allowedness and finite-volume recurrence

For any finite nonempty set F⊂Z², choose x∈F maximizing x₁+x₂. Its east and north neighbours are outside F, so deg_F(x)≤2≤η(x). Thus no finite F is a forbidden subconfiguration. This proof applies to every configuration with heights at least two and every translation of η_{p,q}. It also proves that every restriction to a finite wired box is recurrent: iteratively remove a vertex satisfying the burning inequality η(x)≥deg_F(x); this exists for each nonempty remaining F and removes all vertices in finitely many steps.

### Every height-three component has size one or four

On each ladder, away from seed columns, height-three sites alternate between its rows. They are diagonal neighbours and hence are not adjacent. At a seed x=kp, the lower site (kp,mq) is adjacent to the upper seed site (kp,mq−1) and to the two lower sites (kp±1,mq). Those four form a star. The upper seed's horizontal neighbours are height two; each lower leaf's vertical neighbour and next outward horizontal neighbour have height two. For p≥6 the stars from distinct seeds are disjoint and nonadjacent. For q≥4 distinct ladders have at least two intervening height-two rows, so there is no height-three adjacency between ladders. All remaining height-three sites are isolated. QED.

### A seed launches an infinite first wave

If addition occurs at any vertex of a seed star, all four star sites activate: a height-three site activates on receiving one grain, and the star is connected. In particular both sites of the seed column have toppled once. Suppose both sites in column k have activated. If the next column is not a seed, its height-three site activates from its already active same-row neighbour. Then its height-two site receives one grain from its same-row predecessor and one from the just-activated opposite-row site, and activates as well. If the next column is a seed, each of its height-three sites activates from its predecessor. The identical argument works to the left. Induction over the distance from the initial seed activates both sites in every column of the infinite ladder. All these are instances of §1's activation rule and require no repeated toppling. Hence the first-wave closure is infinite and no finite total stabilization exists.

If addition occurs at a height-two site, no toppling occurs. If it occurs at an isolated height-three site, exactly one toppling stabilizes the configuration: all four neighbours have height two and become at most three. Thus these three cases exhaust all sites and give an exact classification, not only a lower bound.

### A translation-invariant ergodic law and exact probabilities

Let (U,V) be uniform on {0,…,p−1}×{0,…,q−1}, and set η(x,y)=η_{p,q}(x+U,y+V). Denote this law μ_{p,q}. Translation permutes the phases, preserving the uniform law. The full Z² translation action on phases is transitive. Therefore an invariant measurable event pulls back to either all phases or none, and μ_{p,q} is ergodic under the full translation group. This does NOT assert ergodicity under each individual coordinate shift or mixing.

One p×q cell has p+1 height-three sites: p from alternation along the two ladder rows and one extra lower seed. Exactly four belong to the single seed star. Therefore

    E_μ η(0)=2+(p+1)/(pq),
    μ(no topplings)=1−(p+1)/(pq),
    μ(exactly one toppling)=(p−3)/(pq),
    μ(no finite total stabilization)=4/(pq).              (9)

For p=6,q=16 these are mean 199/96, and probabilities 89/96, 3/96, 4/96=1/24 respectively. In particular the mean is less than 17/8=204/96. Letting q grow with p=6 gives mean arbitrarily close to two from above while retaining a strictly positive infinite-avalanche probability.

Consequently even the joint hypotheses of translation invariance, full-group ergodicity, allowedness (and recurrent restrictions to every finite box), mean below 17/8, and bounded height-three components do NOT imply almost-sure finite avalanches on Z².

This is NOT a counterexample to F0033: μ_{p,q} is not the wired stationary weak-limit law ν. In particular μ puts zero mass on heights zero and one, is periodic rather than mixing, and no invariance under sandpile addition has been asserted. The construction identifies hypotheses too weak to settle the actual question.

### Even the identical one-site marginal can give opposite answers

On the 6×16 torus place height three at (0,0),(2,0),(4,0),(0,2),(2,2),(4,2),(0,4) and height two elsewhere; extend periodically to Z². All seven saturated sites are isolated, including across period boundaries. A uniform random translation gives a translation-invariant full-group ergodic law μ_safe, supported on allowed configurations by the same maximal-coordinate-sum argument. Its one-site law is EXACTLY the same as μ_{6,16}: height three with probability 7/96, height two with probability 89/96, and mean 199/96. But under μ_safe every single-grain avalanche has zero or one toppling, by the isolated-site calculation. Thus the one-site marginal, allowedness and translation ergodicity together cannot decide the question either. This is a proved stronger special case, not a statement about adding arbitrarily many grains.

## 4. Explicit finite fractional barrier with no finite integer barrier

Take the above background with p=6,q=16 and addition at the central lower seed site 0. Let

    C={0, (−1,0), (1,0), (0,−1)};
    w(0)=4; w=1 at the other three sites of C; w=0 elsewhere;
    v=w/13.

Then v is nonnegative, finitely supported and REAL-valued, and satisfies Δv≥δ₀−(3−η). In fact the proposed final heights η+δ₀−Δv are also nonnegative.

Proof. At 0, Δw=4·4−3=13; at a leaf, Δw=4·1−4=0. Each site of C has initial height three, so these are exactly the required scaled right sides, 13 and zero. Every vertex outside C adjacent to it has initial height two: this follows either from the explicit pattern or the star's isolation proved above. At such a vertex z,

    Δw(z)=−Σ_{y∼z,y∈C}w(y)≥−Σ_C w=−7≥−13,

which is at least 13(δ₀(z)−(3−η(z)))=−13. At all remaining outside vertices Δw=0 and the required right side is either −13 or zero. This proves the inequality everywhere. Final heights at C are three; at outside neighbours they lie between two and 2+7/13<3; elsewhere they are unchanged. QED.

Yet NO compact integer barrier satisfying (8) exists. Such a barrier would imply a finite total stabilization by §2, contradicting the proved infinite first-wave closure at this seed.

Simple rounding fails visibly. floor(v)=0 leaves the origin at height four. ceil(v)=1_C sends two units into each of (−1,−1) and (1,−1), both initially height two, producing height four there. Thus ceil(v) is not a stable upper barrier either. More elaborate finite rounding cannot work because the nonexistence proof excludes all finitely supported integer candidates.

The fractional v is an algebraic fractional-toppling barrier with stability threshold three. It is NOT asserted to be an odometer for the usual divisible sandpile with threshold one, nor a legal integral sandpile toppling sequence. Applying integer least action to fractional v would be invalid: a first integer toppling can leap past its fractional bound without previously equalling it.

This gives a concrete obstruction to replacing the stationary integer obstacle problem by a real potential-theoretic one and then rounding.

### A stronger general separation lemma

For EVERY stable configuration, if the connected height-three component C containing 0 is finite (or η(0)≤2), there is a compact nonnegative real-valued v with 0≤η+δ₀−Δv≤3. Thus a real-barrier criterion is already substantially weaker than the avalanche question.

Proof. The case η(0)≤2 uses v=0. Otherwise C is finite, connected and consists of height-three sites. Define the killed Laplacian L_C f(x)=4f(x)−Σ_{y∈C,y∼x}f(y). For any real vector f on C,

    Σ_C f(x)L_C f(x)
      =Σ_{unordered internal edges {x,y}}(f(x)−f(y))²
        +Σ_{edges from C to its complement {x,z}} f(x)².

All terms are nonnegative. Vanishing forces f constant along internal edges and zero at a boundary vertex. Connectedness and existence of a boundary edge for a finite nonempty subset of Z² force f≡0. Hence the finite symmetric matrix L_C is positive definite, invertible, and there is a unique real v on C satisfying L_Cv=δ₀.

It is nonnegative: extend v by zero outside C. If its minimum m<0 occurs at x∈C, all four extended neighbour values are at least m, so L_Cv(x)=4m−Σ_neighbours v≤0. Since the right side is nonnegative, equality is necessary, and all neighbours have value m. Propagation along C reaches a boundary edge, whose outside value is zero>m, contradiction. Therefore v≥0.

For z outside C put a(z)=Σ_{x∈C,x∼z}v(x). It is nonnegative and finitely supported. Summing L_Cv=δ₀ over C cancels each internal edge's contributions, leaving

    Σ_{z∉C}a(z)=1.

Thus each a(z)≤1. Every outside neighbour of C has η(z)≤2 because C is the entire connected height-three component. At C the final expression η+δ₀−Δv is exactly three; outside C it is η(z)+a(z), which lies in [0,3] at neighbours and equals the original stable height elsewhere. This proves the lemma. QED.

The star v of §4 is the explicit instance of this killed Green-function construction. Its fractional normalization is not an accident: the total outward flux is one, enough to fit the outside slack, while the integer model must first topple a site by a full unit and thereby sends FOUR outgoing grains. That integral threshold is precisely what a real Dirichlet solution loses.

## Checks obtained so far

ladder_checks.py verifies all local inequalities using integer scaling by 13, the burning criterion in seven wired boxes (r=2,…,32), first-wave propagation to each box's left and right boundary, all 96 translated phase classifications on a test box, and saturated components of size only one or four. Outputs in ladder_results.json. These tests support the complete proofs above but do not estimate ν.

The stronger same-marginal safe pattern was also checked on all 96 phases: exactly 89 empty and seven one-toppling avalanches. BootstrapStep.lean passed with exit code 0 and no diagnostics; its checked local implications and arithmetic are listed in LEAN_CHECK.md. The global proofs are written, not claimed fully formalized. The finite-volume stationary sampling job reported about 10.36 seconds runtime and saved results after each size.

## 5. Actual finite-volume stationary samples

To test approach A on the correct model rather than the constructed law, stationary_wave_sample.py samples ν_r using Wilson's algorithm for the wired UST and the ordinary inverse burning bijection. It retains the FOUR distinct outgoing edges at a boundary site, including parallel edges to the sink, and fixes their order. If D(x) is tree distance to the sink, m(x) counts neighbour edges to a vertex of smaller distance, and k(x) is the index of the parent edge among edges to distance D(x)−1, it sets

    η(x)=4−m(x)+k(x),   k=0,…,number_of_candidate_edges−1.

Why this is the correct inverse formula: at time D(x)−1 the remaining neighbour degree is 4 minus the number of edges to distances strictly smaller than D(x)−1; failure to burn then bounds η from above. Burning at time D(x) bounds it from below by 4−m(x). The integer interval has exactly the number of edges to distance D(x)−1 entries, indexed by the parent edge. Tree distances and this formula therefore recover a recurrent configuration through the standard burning bijection. Wilson sampling gives a uniform spanning tree, so this bijection gives the uniform recurrent law, with no mixing/burn-in assumption. The algorithm uses last-exit successors to erase loops; following successors from the starting vertex recovers the chronological loop-erased path because last visit times strictly increase along each retained successor until the wired tree is hit.

Independent implementation checks: the first three configurations at each size pass the burning recurrence test; ordinary finite wave topplings obey the existing per-wave legality assertions. At r=1 the sampled histogram (N=0,1,2) was (2546,1394,60) out of 4000, compared with the exhaustive law from the first attempt (63872,35328,1152)/100352. This is consistent with, but does not prove, sampler correctness. The correctness basis is the Wilson/burning construction, not histogram agreement.

The seeded runs (seed 330033) gave these counts of waves/whole avalanches reaching their OWN box boundary:

| box radius | samples | first wave reaches boundary | whole avalanche reaches boundary |
|---:|---:|---:|---:|
| 1 | 4000 | 1118 | 1118 |
| 4 | 400 | 94 | 94 |
| 8 | 300 | 44 | 46 |
| 16 | 200 | 27 | 30 |
| 32 | 100 | 6 | 9 |

The script also records fixed internal radii and the entire N histogram at each size, in stationary_wave_results.json. Sample counts at large sizes are small, and there is substantial tail variability. No exponent is fitted, no asymptotic conclusion is drawn, and first-wave radius is not substituted for full avalanche radius.

For another independent check, sampler_moment_checks.json compares sample means with Dhar expectations from a sparse numerical solve of Δ_r G(0,·)=δ₀. Eν_r N=G(0,0) and Eν_r S=Σ_xG(0,x). For r=1,4,8,16,32 the calculated means N are approximately 0.375,0.525,0.619,0.720,0.826; sample means are 0.379,0.523,0.560,0.710,0.820. At r=32 sample mean S=318.48 versus numerical expectation 320.85. These are floating-point cross-checks, not exact linear-algebra proofs or confidence-certified estimates.

**Critical referee restriction:** this table concerns r=n. Even if those diagonal probabilities were proved to tend to zero, it would not establish lim_r sup_{n≥r}ν_n(R_n≥r)=0. The fixed-radius observations across boxes are likewise finite data, not a uniform bound. The experiment provides no proof of ν-almost-sure finiteness.

## 6. Referee audit and precise stopping point

- Origin topples only once in the bootstrap reduction; layers count distinct already activated neighbours. Infinite activation is established via finite legal prefixes, not by assuming an infinite wave completes.
- Allowedness is verified for EVERY finite set using a maximal coordinate sum. Finite-box recurrence alone does not identify the uniform recurrent law.
- All finite height-three components are classified explicitly, including the seams of the horizontal and vertical periods.
- The induction through a new ladder column uses one height-three and one height-two vertex and gives the latter two distinct incoming grains.
- Translation ergodicity is for the FULL Z² action. No mixing or individual horizontal-shift ergodicity is claimed.
- μ_{p,q}, μ_safe and ν are kept distinct. The constructed law's positive infinite-avalanche probability is not attributed to ν.
- The real Green barrier has full-space boundary flux verified, its resulting heights stay nonnegative, and its total outward flux is exactly one. Integer least action is applied only to integer barriers.
- Neither absence of infinite saturated components nor a compact real barrier controls the later-wave count or provides the missing stationary estimate.
- Approach B still lacks a noncircular invariant probability space for the limiting wave transformation. Finite-volume addition permutations do not alone provide one.

**Remaining gap unchanged at the level of the target:** prove existence of a compact nonnegative INTEGER barrier for ν-almost every η, equivalently the stationary uniform-radius estimate from ATTEMPT.md. The new results show specifically that real barriers, one-site density information, allowedness, and saturated-component bounds cannot replace that requirement. No ν-specific bootstrap crossing bound or finite-wave-count estimate has been proved.

Verdict for this second attempt: PARTIAL. The proof and counterexample constructions concern useful reductions and stronger special cases, not a solution of F0033.
