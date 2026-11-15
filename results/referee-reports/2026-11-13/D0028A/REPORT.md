PARTIAL

# D0028: stationary measures of kinetically constrained spin models

The unrestricted conjecture is not settled here. No general resolution in print was located. Two extensions are proved below, without translation invariance:

1. On every strip `Z × H`, with H a finite connected graph, every stationary law of FA-1f is `λπ + (1−λ)δ₁`, for every `0<q<1`. The same conclusion holds for finite-range monotone binary heat-bath constraints that allow every FA-1f move and forbid updates in the all-filled configuration. There is no finite-energy assumption in this result.
2. On `Z²`, for any finite-range binary heat-bath KCM, a stationary law with uniformly bounded single-site conditional odds satisfies detailed balance. If the model internally spans large boxes with probability tending to one at every positive Bernoulli vacancy density, this law equals π. In particular this applies to planar FA-1f and FA-2f, at every `0<q<1`. A complete elementary proof of the required FA-2f bootstrap fact is included.

These are extensions of the source's entropy argument under restricted geometry or an additional measure hypothesis, not claims of a new general classification. Their novelty in the broader literature has not been established. All statements and proofs below are mathematical arguments, separate from the finite-state computational evidence.

## 1. Exact source, scope, and conditioning

The source is Fabio Martinelli, Assaf Shapira and Cristina Toninelli, *Long time behaviour of one facilitated kinetically constrained models: results and open problems*, [arXiv:2510.20461v1](https://arxiv.org/abs/2510.20461v1), 23 October 2025. Its Conjecture 3 and Theorem 2.13 are both on PDF p.8. Full text is archived in `sources/martinelli_shapira_toninelli_2025.txt`. Sections 1–3, including the proofs, were read completely. The detailed search record is `sources/LITERATURE.md`.

Use spins `η_x∈{0,1}`, with 0 infected/empty, `q∈(0,1)`, `p=1−q`, and `π=⊗ Ber(p)`. An update family is a finite nonempty collection U of finite nonempty subsets of `Z^d\{0}`. Its constraint is

`c_x(η)=1{there exists U∈U such that η_(x+u)=0 for every u∈U}`.

Thus the constraint is local, independent of η_x, and increasing in the set of vacancies. The generator is

`Lf(η)=Σ_x c_x(η) r_x(η)[f(η^x)−f(η)]`,

where `r_x(η)=q` if η_x=1 and `r_x(η)=p` if η_x=0. Equivalently `L=Σ_x c_x(π_x−I)`. General site-dependent versions with a uniform finite range are permitted in the strip proof. No particle-conserving exchange dynamics is included. The book's Section 2.2, printed p.6/PDF p.16, supplies the explicit update-family definition; the source Section 2 uses these constraints and also discusses bounded weighted variants such as BABP.

Bootstrap percolation repeatedly changes an occupied site to 0 whenever c_x=1 and never fills a vacancy. Its decreasing limit is BP(η). The stable set E is `{β: BP(β)=β}`. Both constant configurations belong to E, but a BP-stable configuration need not be a frozen KCM configuration: existing zeros can still be filled by the stochastic dynamics. `BP^Λ` means that only Λ is updated and the exterior is fixed to 1, unless a different fixed boundary is specified explicitly.

A stationary measure means a Borel probability μ invariant under the infinite-volume Feller semigroup: `μP_t=μ` for all t≥0. In particular `μ(Lf)=0` for every local f. This is not an assumption of translation invariance, reversibility, ergodicity, absolute continuity, or support on the component typical under π. Finite volume means a different, finite-state chain, with a prescribed frozen exterior or periodic identifications.

The target is a kernel β↦π_β and a probability μ* on E such that

`μ=∫_E π_β μ*(dβ)`.

If each π_β is supported on its fiber, necessarily `μ*=BP_#μ`. At a positive-probability fiber, π_β is ordinary conditional probability. At a null fiber, a regular conditional distribution of π given BP is only specified `BP_#π`-almost everywhere. It can be changed arbitrarily on a set of BP-values of zero `BP_#π` measure. The source gives the explicit product extension (2.6) for East, but **does not specify a canonical extension for every null fiber of a general update family**. It does not define one by a particular limiting procedure. Consequently a completely literal general reading needs this additional specification; arbitrary choices of regular-conditional versions cannot constitute a meaningful counterexample.

The strip result has just two fibers: π₀=π and π₁=δ₁. Here BP=1 has π-probability zero, but its fiber is the singleton {1}, so the supported extension is unambiguous. The planar finite-energy result has μ*=δ₀ and π(BP=0)=1. Neither result depends on an unspecified null conditioning.

A useful caution: the source's Theorem 2.2 describes local accessibility using the phrase “ergodic component.” This must not be replaced by a proof that every measurable invariant function is constant on a BP fiber. For instance π_q and π_a with a≠q can both give BP=0 almost surely in FA-1f, yet their almost-sure empirical vacancy densities distinguish them and are unchanged by finitely many flips. Finite legal connectivity alone does not establish infinite-volume uniqueness.

## 2. What the source proves, and the missing steps

### Detailed balance and the one-dimensional mechanism

For a finite V containing the entire constraint neighborhood of x, detailed balance means

`r_x(ζ)c_x(ζ) μ_V(ζ) = r_x(ζ^x)c_x(ζ) μ_V(ζ^x)`.

Equivalently `μ_V/π_V` is unchanged along legal flips. This is source Definition 2.3/(2.1), p.6, with the usual zero-mass convention.

Source Theorem 2.4, p.6, invokes Holley's entropy argument for stationary **translation-invariant** measures. Theorem 2.5, p.6, proved in Section 2.1, pp.8–11, removes translation invariance in dimension one. Translation invariance allows a volume average of nonnegative entropy production to identify each local term. Without it, production can in principle be concentrated near a spatial interface or supplied by the growing boundary.

In one dimension the boundary contains a uniformly bounded number of sites. Stationarity balances nonnegative bulk entropy production against a boundary term. Its boundedness makes the cumulative production summable. Successive boundary currents then vanish. A truncation of logarithmic density ratios controls the degenerate-rate boundary error uniformly in the interval length; taking length first and truncation second forces every bulk term to vanish. Section 3 below rederives this carefully, including the entropy sign, and extends it to strips.

For FA-1f, any vacancy empties a connected finite set. Hence the only full-lattice BP-values are 0 and 1. On the active fiber the probability that a growing interval contains a vacancy tends to one, and finite-volume detailed balance identifies its law with π conditioned on that event. This is source Lemma 2.8 and Corollary 2.9, p.7, with the lemma proved pp.11–12.

### East: a leftmost vacancy and orientation

In one-dimensional East, `c_x=1−η_(x−1)`. If there is a leftmost vacancy i, all sites left of i stay filled and i stays vacant. The remaining right half-line has an empty boundary at i. The measure is δ₁ to the left, δ₀ at i, and independent Bernoulli(p) to its right. Internal spanning gives the identification. If there are vacancies arbitrarily far to the left, a vacancy outside any fixed window can empty the window from its left: source (2.16), p.14. The external-spanning Lemma 2.11, pp.7 and 13, then identifies the measure with π. This is the leftmost-vacancy/renewal distinction needed for Theorem 2.12, pp.7 and 13–14; no general renewal independence is assumed in advance.

For d-dimensional East, an individual vacancy can infect its entire forward orthant. The stable interface consists of occupied sites behind an antichain and indispensable vacant seeds, with ordinary product spins downstream; infinite interfaces require the extended-coordinate treatment in source (2.6). Orientation makes the dynamics in a suitable finite downstream domain autonomous. The source proves pointwise convergence on each fiber in Lemma 2.19, p.14, using finite-chain ergodicity for finite seed boundaries and Chleboun–Faggionato–Martinelli's East relaxation result [5] for boundaries at infinity. Integrating that convergence against stationary μ proves Theorem 2.13. This bypasses a general non-translation-invariant entropy argument in d≥2.

Section 3 is also relevant, but does not prove the unrestricted conjecture. Theorem 3.1, pp.15–16, concerns the one-dimensional East-polluted FA-1f model. Its Lemma 3.2 uses the last legal ring across successive East barriers: downstream coin tosses cannot affect an upstream barrier. Repeating the conditional coin estimate bounds a long infection-free interval by p^n. This excludes the non-product stationary components from limit points when initial infections are unbounded to the left. The independence is supplied by orientation, rather than by a general property of legal paths.

### Why these arguments do not settle general higher-dimensional models

FA-2f on Z² has no single-vacancy expansion: two suitable vacancies are required, and finite empty droplets can need assistance from their surroundings. There is no autonomous downstream domain with one fixed seed as in East. In the North-East model the dynamics is oriented, but the update requires both predecessors vacant; orientation alone is not the single-seed mechanism. Infinite blocking paths and the density regime matter. The source's citation [13] for a NE analogue actually names a different competition-model paper; see the corrected literature discussion below.

The quantitative obstruction in source Remark 2.16, p.11, is that the boundary cutoff error grows like `|∂Λ_N| λe^(−λ)`. In d=2 it requires λ of order log N. The resulting extra factor log N multiplying the boundary currents defeats the summability argument. Section 4 removes this loss under an explicit additional hypothesis. In d≥3, even that improvement does not make the boundary harmonic series diverge.

For FA-1f in arbitrary dimension, and also for a model satisfying source Theorem 2.10 on the fully emptyable fiber, the minimal missing lemma along this route is:

> Every stationary measure supported on BP=0 satisfies the finite-cylinder detailed-balance identities.

For FA-1f this lemma, together with the internal-spanning argument below, immediately proves the whole classification. For the full conjecture there is a **second** missing issue: a canonical fiber law and uniqueness of the reversible law on each relevant possibly null fiber. Detailed balance alone does not supply this in arbitrary geometry. Thus a general “stationarity implies reversibility” assertion should not be reported as the entire conjecture.

## 3. Complete entropy proof on strips

All rates in this section are `0≤c_x≤1`; a fixed finite upper bound only changes constants. Neighborhoods have a common finite range r. On `Z×H` choose `V_n=[−nr,nr]×H`, increasing r if needed. Set `I_n=V_(n−1)` and `B_n=V_n\I_n`. Every constraint centered in I_n is measurable in V_n, every constraint centered in V_n is measurable in V_(n+1), and `|B_n|≤b` for a constant b depending on the fixed width and range. The identical notation on Z² gives `|B_n|≤bn`.

For a finite V, ζ∈{0,1}^V and x∈V write

`a_V(x,ζ)=∫ 1{η_V=ζ} c_x(η)r_x(η) μ(dη)`,

`b_V(x)=Σ_ζ |a_V(x,ζ)−a_V(x,ζ^x)|`.

When the constraint at x lies in V put

`A_V(x)=Σ_ζ [a_V(x,ζ)−a_V(x,ζ^x)] log[a_V(x,ζ)/a_V(x,ζ^x)]`.

Zero-zero terms are zero. These quantities satisfy:

(a) `A_V(x)≥0` and `A_W(x)≥A_V(x)` when V⊂W and x is interior in V;

(b) `b_V(x)≤b_W(x)` for V⊂W;

(c) `b_V(x)^2≤2A_V(x)` for interior x.

For (a), nonnegativity follows from `(a−b)log(a/b)≥0`; monotonicity is the log-sum inequality after grouping extensions of ζ. For (b) use the triangle inequality when grouping. For (c) use `(a−b)log(a/b)≥2(a−b)^2/(a+b)` and Cauchy–Schwarz, together with `Σ_ζ(a(ζ)+a(ζ^x))≤2`. In fact this gives a slightly sharper constant; the stated bound suffices.

We justify the zero-mass convention rather than imposing positivity. If `μ_V(ζ)=0`, stationarity applied to the indicator of ζ says that the total incoming rate into ζ is zero. Every incoming rate is nonnegative, so each is zero. In particular both paired a-values are zero. If x is interior and c_x(ζ)=1, positive mass at ζ forces positive mass at ζ^x by the same observation. Thus A_V(x) is finite and all logarithms below can be restricted to pairs of positive marginal masses.

Let `ρ_V=μ_V/π_V` on its support, and define

`ℓ_V(x,ζ)=log[ρ_V(ζ)/ρ_V(ζ^x)]`.

Stationarity applied to the finite local function `log ρ_V` (arbitrary finite values at zero-mass states) gives the entropy balance

`S_n := Σ_(x∈I_n) A_(V_n)(x) = 2H_n`,                         (3.1)

where

`H_n=−(1/2)Σ_(x∈B_n)Σ_ζ [a_(V_n)(x,ζ)−a_(V_n)(x,ζ^x)]ℓ_(V_n)(x,ζ)`.

To check the sign directly, the x-contribution to `μ(L logρ_V)` is `Σ_ζ a(x,ζ)[logρ_V(ζ^x)−logρ_V(ζ)]`. Symmetrizing yields the negative half-sum above. At an interior site with a nonzero paired rate, independence of c_x from η_x and `π_V(ζ)r_x(ζ)=π_V(ζ^x)r_x(ζ^x)` give `ℓ=log(a/a^x)`; zero-rate pairs contribute zero. Its total contribution is therefore `−A_V(x)/2`. This proves (3.1).

Let `M=max(p/q,q/p)`. For λ≥1 the boundary term obeys

`H_n ≤ (λ/2)Σ_(x∈B_n)b_(V_n)(x) + M|B_n| λe^(−λ)`.        (3.2)

Here is the full tail estimate. On ℓ>λ the positive part of `−(a−a^x)ℓ` is at most `a^xℓ≤μ_V(ζ^x)ℓ`. Since `μ_V(ζ^x)=μ_V(ζ)[π_V(ζ^x)/π_V(ζ)]e^(−ℓ)`, summing bounds this part by `Mλe^(−λ)`. On ℓ<−λ exchange ζ and ζ^x. On |ℓ|≤λ use λ|a−a^x|. Including the factors 1/2 gives (3.2). The same argument with threshold zero and `sup_(t≥0)te^(−t)=1/e` gives

`0≤S_n=2H_n≤(2M/e)|B_n|`.                                (3.3)

No lower bound on the transition rates was used.

By (a), S_n is nondecreasing. Also every x∈B_n is interior in V_(n+1), so

`S_(n+1)−S_n ≥ Σ_(x∈B_n) A_(V_(n+1))(x)`.                 (3.4)

Combining (b), (c), (3.4) and Cauchy–Schwarz yields

`Σ_(x∈B_n)b_(V_n)(x) ≤ sqrt[2|B_n|(S_(n+1)−S_n)]`.        (3.5)

On a strip, (3.3) bounds S_n uniformly. Hence `S_(n+1)−S_n→0` and the right side of (3.5) tends to zero. Fix λ in (3.2), take n→∞, and then λ→∞. Equations (3.1)–(3.2) show `S_n→0`. Since S_n is nonnegative and nondecreasing, it is identically zero. Every interior A-term is zero. Its nonnegative summands then give `a_V(x,ζ)=a_V(x,ζ^x)`.

These identities initially hold for the exhausting V_n. Given any finite cylinder W containing x's neighborhood, choose V_n⊃W and sum the identities over V_n\W. This gives detailed balance on W. We have proved:

**Strip balance theorem.** Every stationary measure of a uniformly finite-range binary heat-bath KCM on `Z×H`, with H finite, satisfies detailed balance. Spatial homogeneity is unnecessary.

### Identifying a measure by internal spanning

We need one elementary consequence of detailed balance. For finite connected V define `G_V={BP^V(η)=0_V}`, with filled exterior. All configurations in G_V are connected by legal flips within V: empty occupied sites successively in a legal bootstrap order to reach 0_V, then reverse such a sequence for the target configuration. Each flip is still legal with any actual exterior, by monotonicity.

For a flip in this path, apply detailed balance on an enlarged finite set containing V and its constraint boundary, then sum over that boundary. This gives

`μ_V(ζ)/π_V(ζ)=μ_V(ζ^x)/π_V(ζ^x)`.

It follows that the ratio is constant on G_V. Whenever μ(G_V)>0,

`μ(· | G_V)=π(· | G_V)` on the variables in V.               (3.6)

If `μ(G_(V_n))→1` and `π(G_(V_n))→1`, then for every cylinder event F supported in V_n,

`|μ(F)−π(F)|≤2[1−μ(G_(V_n))]+2[1−π(G_(V_n))]→0`.           (3.7)

For completeness, replace each unconditional law by its conditional law on G, with error at most 1−law(G), then use (3.6); the looser factor 2 in (3.7) is harmless. All finite-cylinder probabilities agree, so μ=π.

### Strip classification

Take the ordinary nearest-neighbor FA-1f constraint on the connected graph `Z×H`. A single vacancy empties every connected finite V containing it: follow paths outwards from that vacancy. Thus G_V is exactly the event that V contains a vacancy.

Let `a=μ({1})`. If a=1 there is nothing to prove. Otherwise define `ν=(μ−aδ₁)/(1−a)`. This is a probability measure supported on configurations with at least one vacancy. It is stationary because both μ and δ₁ are stationary. By the strip balance theorem it satisfies detailed balance. Since V_n exhausts the graph,

`ν(G_(V_n))→1`, and `π(G_(V_n))=1−p^|V_n|→1`.

Equations (3.6)–(3.7) prove ν=π. Therefore

`μ=(1−a)π+aδ₁`.

Both constituent measures are stationary, so this is an exact characterization. The mixing measure is `(1−a)δ₀+aδ₁` on E={0,1}. This proves the conjectured decomposition for every fixed-width FA-1f strip at every q. If additional monotone finite-range legal moves are allowed, every nonempty vacancy set still spans every connected finite V, whereas the all-filled state remains absorbing by assumption. The proof is unchanged.

## 4. Complete planar proof with a finite-energy hypothesis

Say μ has **uniform finite energy** if there is ε∈(0,1/2] such that for every finite V, x∈V, and every conditioning configuration with positive probability,

`ε≤μ(η_x=0 | η_(V\{x}))≤1−ε`.                              (4.1)

Merely assuming absolute continuity with respect to π on each finite box imposes no restriction: π gives every finite configuration positive probability. The uniform bound (4.1) is a genuine extra hypothesis.

The analogous bound given the entire complement is equivalent, by conditional expectations and martingale convergence. In particular (4.1) implies that every finite configuration has positive mass: reveal its sites successively, and each prescribed outcome has probability at least ε.

Equation (4.1) bounds adjacent marginal odds uniformly, so

`|ℓ_V(x,ζ)|≤K := log[(1−ε)/ε]+|log(p/q)|`.                 (4.2)

Use planar `V_n=[−nr,nr]^2`, I_n=V_(n−1), and B_n=V_n\I_n, so |B_n|≤bn. The balance identity (3.1) now gives, without any logarithmic truncation,

`S_n≤KΣ_(x∈B_n)b_(V_n)(x)≤K sqrt[2bn(S_(n+1)−S_n)]`.

If K=0 then S_n=0 immediately. Otherwise there are constants C,D>0 such that

`S_n²≤Cn(S_(n+1)−S_n)`, and `S_n≤Dn`.                     (4.3)

The second inequality follows from `b_V(x)≤2` and the first boundary bound. We give the discrete argument showing that (4.3) forces S≡0. If `S_m=s>0`, monotonicity gives for n≥m

`S_(n+1)≥S_n[1+s/(Cn)]`.

The product on the right diverges, because the sum of its logarithms dominates a constant times the harmonic series for large n. Thus S_n→∞. Choose m' so that S_n≥3C for n≥m'. The same recurrence then gives

`S_(n+1)≥S_n(1+3/n)≥S_n[(n+1)/n]²`.

Iteration implies `S_n≥S_(m')(n/m')²`, contradicting S_n≤Dn. Therefore every S_n=0, and the argument after (3.5) establishes all finite-cylinder detailed-balance identities.

**Planar balance theorem.** Every stationary uniformly finite-energy law of a finite-range binary heat-bath KCM on Z² is reversible in the detailed-balance sense, without a translation-invariance assumption. Zero transition rates are allowed.

### From detailed balance to π

Assume the update family has the internal-spanning property

`π_a(G_(V_n))→1 for every vacancy density a∈(0,1)`.          (4.4)

Uniform finite energy implies stochastic domination in vacancies of independent Bernoulli(ε). One direct finite-volume construction reveals the sites of V_n in any order, uses independent uniform variables, and puts a vacancy whenever the uniform variable is at most the current conditional vacancy probability. The same uniforms, thresholded at ε, give an independent vacancy subset. Conditional probabilities stay at least ε by (4.1). Since G_V is increasing in vacancies,

`μ(G_(V_n))≥π_ε(G_(V_n))→1`.

Also `π_q(G_(V_n))→1` by (4.4). The planar balance theorem and (3.6)–(3.7) prove μ=π_q. In particular BP=0 almost surely under both measures, so the decomposition holds with μ*=δ₀.

For FA-1f property (4.4) is immediate from connectedness. For a general stationary FA-1f μ one can instead assume (4.1) only for its normalized active part `(μ−μ({1})δ₁)/(1−μ({1}))`; that part is stationary, so the conclusion becomes the full mixture `λπ+(1−λ)δ₁`. This accommodates a frozen atom explicitly. It does not assert finite energy for every stationary active law.

### Elementary verification of (4.4) for planar FA-2f

Fix a∈(0,1), write t=1−a, and use squares `[1,N]^2`. Let

`L=ceil(C log N)`, with `C>3/|log t|`, and `m=ceil((log N)^(1/3))`.

For large N, m<L. Tile most of the square by disjoint L×L blocks. In a block require its bottom-left m×m square initially vacant. Starting there, grow a k×k vacant square by adding the next column of length k and the next row of length k+1, for k=m,...,L−1. A new column becomes vacant whenever it contains an initial vacancy: its empty neighbor in the old square and a consecutive vertical empty neighbor permit the two-neighbor rule to propagate up and down. The same holds for a new row.

All required strips are disjoint. Consequently the probability that a block internally empties is at least

`a^(m²) Π_(k=m)^(L−1)(1−t^k)(1−t^(k+1)) ≥ (1/2)a^(m²)`

for large N, since the sum of the omitted probabilities is at most `2t^m/(1−t)→0`. Events for disjoint blocks are independent. With `J=floor(N/L)^2`, the probability no block succeeds is at most

`exp[−J a^(m²)/2]→0`,

because `log J=2log N−O(log log N)` while `m²=O((log N)^(2/3))`.

Separately, a union bound shows that the probability of any fully occupied horizontal or vertical segment of length L is at most `2N² t^L→0`. On the complement of this event, any internally emptied L×L block can grow horizontally to a completely empty band across the box: each adjacent length-L column segment contains an initial vacancy. Then the band grows vertically to fill the box, because each new row contains an initial vacancy. Every operation stays inside the box, using filled exterior. Thus `π_a(G_[1,N]^2)→1`. Translation gives the centered-box version of (4.4).

This proves the planar FA-2f conclusion with no unproved bootstrap input. It remains an additional-hypothesis theorem: arbitrary singular stationary laws may violate (4.1).

## 5. Finite-volume theorem and computational evidence

For any finite domain V with a fixed boundary, or any finite periodic graph whose update rules exclude the updated vertex, legal flips preserve BP. Conversely configurations with the same terminal BP configuration connect to that terminal configuration by successively deleting legally deletable occupied sites. Reversing the second deletion path connects any two configurations in the fiber. Thus the finite-state communicating classes are exactly the finite BP fibers.

Since `π_V(ζ)r_x(ζ)c_x(ζ)=π_V(ζ^x)r_x(ζ^x)c_x(ζ^x)`, π_V restricted and normalized on each fiber is reversible. Every class is a finite irreducible chain. To see uniqueness directly, divide any stationary vector by the positive reversible weights; its density is harmonic for the same chain. At a maximum, the harmonic equation forces equality at every neighbor, hence throughout the class. Thus its density is constant and the stationary probability is unique. Therefore **every finite-volume stationary measure has exactly the desired mixture decomposition**, for every such update family and boundary condition. This proof does not pass to infinite volume: finite connectivity does not provide a uniform mixing time, tight control of boundaries, or uniqueness on null infinite fibers.

There were **57 completed cases**, at q=1/3 and 2/3 on four-site intervals/rings and 3×2 boxes/periodic graphs, plus a nondegenerate 3×3 FA-2f torus at q=1/3. Models: East, FA-1f, FA-2f, and North-East. Boundaries: filled, empty, alternating/checkerboard, and periodic. On the short periodic side of a 3×2 graph, FA-2f counts distinct neighboring vertices; it does not count the same vertex twice. The separate 3×3 torus avoids this convention issue entirely.

For q=a/b, the code constructs the integer matrix M=bQ, with off-diagonal flip entries a or b−a. SymPy computes `ker(M.T)` over the rationals. Independently computed BP fibers and graph components give identical partitions. On each fiber C the exact stationary vector has weights

`a^(number of zeros) (b−a)^(number of ones) / Σ_(ζ∈C) a^(zeros in ζ)(b−a)^(ones in ζ)`.

The code checks exact stationarity and normalization of every such vector, verifies that every independently returned nullspace vector is their linear combination, and checks a nontrivial convex mixture with positive weight on every fiber. A separate normalized floating-point solve on each class checks the probabilities numerically. **All exact residuals were zero; every kernel dimension equaled the number of BP fibers.** Maximum numerical probability error over all cases: `5.2735593669694936×10^−15`.

Some q=1/3 cases:

| Model/domain | Boundary | States | Kernel dimension = BP fibers | Largest fiber |
|---|---|---:|---:|---:|
| East, four sites | filled | 16 | 5 | 8 |
| East, four sites | empty | 16 | 1 | 16 |
| FA-1f, four-site ring | periodic | 16 | 2 | 15 |
| FA-2f, four-site ring | periodic | 16 | 10 | 7 |
| FA-2f, 3×2 | filled | 64 | 21 | 30 |
| FA-2f, 3×2 | empty | 64 | 1 | 64 |
| North-East, 3×2 | filled | 64 | 48 | 4 |
| North-East, 3×2 | periodic | 64 | 28 | 25 |
| FA-2f, 3×3 | periodic | 512 | 17 | 478 |

The last case has exact rank 495. These quantities were obtained from the rational kernel and checked against an independent graph partition.

A hand-derived check illustrates the non-product conditioning. On the four-site FA-2f ring, BP=0 exactly when the occupied vertices form an independent set. There are seven such states: the empty set, four singletons, and two opposite pairs. At q=1/3 their unnormalized weights are 1,2,4 respectively, so the normalizer is 17. Each occupied-site marginal is 6/17, while two adjacent occupied sites have joint probability zero, giving covariance `−36/289`. The nine remaining states are frozen singletons. Thus the kernel has dimension 10 and its active law is not a product measure. This agrees exactly with the computed artifact.

Artifacts: `code/finite_kcm.py`, `code/audit_results.py`, `code/aggregate_results.py`; `data/finite_summary.csv`, `data/verification.json`, `data/audit_run.txt`, and one rational-probability JSON per case. Reproduce the full calculation from this directory with:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/finite_kcm.py > data/finite_run.txt
python3 code/audit_results.py > data/audit_run.txt
```

The session inherited nice 10, verified with `os.getpriority`. All numerical libraries were capped at one thread; no multiprocessing or agents were used. The final complete 57-case run recorded a peak resident set of **85,213,184 bytes (about 81.3 MiB)** using Python’s `resource.getrusage`, and took about 33 seconds, including about 32 seconds for the 512-state case. The computation used matrices of at most 512×512. All bounds are well below the requested 4 GB and four-thread limits. No publication or push occurred. No PDF, page image, or scan was retained.

The independent artifact audit rederived the FA-2f ring weights/covariance, the five East interval classes, and the two FA-1f ring classes; checked normalization of all archived rational laws and source text hashes; and checked the required report status and absence of PDFs/images. The finite calculations are evidence and an implementation check, not an infinite-volume proof.

## 6. Literature outcome and exact locations

No general proof of Conjecture 3 in print was found. The strongest later explicit status check is Fabio Martinelli, *Kinetically Constrained Spin Models: A Short Survey*, [ICM 2026, DOI 10.1137/25M180425X](https://epubs.siam.org/doi/10.1137/25M180425X), online 13 July 2026: **Conjecture 1.6, printed p.499/PDF p.3**, restates the conjecture; Theorem 1.5 on that page restates source Theorem 2.10. This is evidence of an open status in July 2026, not a guarantee about every subsequent preprint. Semantic Scholar returned zero indexed citations, despite this known citation, so its empty list was not treated as exhaustive. Direct arXiv-id/title searches and authors' publication lists were also checked through the task date.

Exact source map for the checked arXiv v1:

| Result | Statement page | Proof pages | Actual scope |
|---|---:|---:|---|
| Definition 2.1; Theorem 2.2 | 6 | refers to book Cor.3.7 | BP and local legal accessibility |
| Theorem 2.4 | 6 | invokes Holley [11] | Stationary + translation-invariant implies detailed balance |
| Theorem 2.5 | 6 | 8–11 | Stationary in d=1 implies detailed balance |
| Lemma 2.8 | 7 | 11–12 | Identification using internal spanning |
| Corollary 2.9 | 7 | consequence of Lemma 2.8 | FA-1f, BABP, δ-West on Z |
| Theorem 2.10 | 7 | 12–13 | BP=0 uniqueness with detailed balance and π-internal spanning |
| Lemma 2.11 | 7 | 13 | Identification using external spanning |
| Theorem 2.12 | 7 | 13–14 | All stationary measures of one-dimensional East |
| Theorem 2.13; formula (2.6) | 8 | 14, Lemma 2.19 | All stationary measures of d-dimensional East |
| Conjecture 3 | 8 | none | General KCM decomposition |
| Remark 2.16 | 11 | — | The logarithmic obstruction in d=2 |
| Theorem 3.1; Lemma 3.2 | 15 | 15–16 | East-polluted FA-1f convergence using oriented barriers |

Related exact references:

- Hartarsky–Toninelli, *Kinetically Constrained Models*, SpringerBriefs Math. Phys.53 (2025), [arXiv:2412.13634](https://arxiv.org/abs/2412.13634): Lemmas 3.5–3.6 and Corollary 3.7, printed pp.16–17/PDF pp.26–27; Theorem 3.9, pp.17–18/PDF pp.27–28; Theorem 4.8, p.39/PDF p.49. The legal-path corollary explicitly assumes finite disagreement.
- Cancrini–Martinelli–Roberto–Toninelli, PTRF140 (2008), 459–504, [DOI 10.1007/s00440-007-0072-3](https://doi.org/10.1007/s00440-007-0072-3): **Proposition 2.5, p.467/PDF p.9**, gives equilibrium ergodicity iff bootstrap empties the origin almost surely; its arXiv version math/0610106 numbers the corresponding result Proposition 2.4. This is not a classification of all stationary measures.
- Blondel–Cancrini–Martinelli–Roberto–Toninelli, MPRF19 (2013), 383–406, [arXiv:1205.4584](https://arxiv.org/abs/1205.4584): **Theorem 2.1, arXiv PDF p.4**, requires q>1/2 and a uniform exponential vacancy-distance moment. It cannot by itself classify an arbitrary stationary law. No private claim note was used.
- Mountford, *A coupling of infinite particle systems*, J. Math. Kyoto Univ.35(1) (1995), 43–52, [DOI 10.1215/kjm/1250518839](https://doi.org/10.1215/kjm/1250518839): **Theorem 1 as invoked on source p.16** concerns invariant limit laws in one dimension. Full publisher text was unavailable here, so its full hypotheses were not independently certified. No all-dimensional FA-1f classification by Mountford was located.
- Kordzakhia–Lalley, *Ergodicity and mixing properties of the northeast model*, JAP43 (2006), 782–792, [arXiv:math/0601157](https://arxiv.org/abs/math/0601157): **Theorem 1, arXiv p.2**, is about time-ergodic translation-invariant stationary laws; Section 3, pp.7–8, gives non-translation-invariant examples. The source's reference [13] instead names their competition-model paper and should not be used as a precise NE theorem citation.
- Jahnel–Köppl, *Probability and Mathematical Physics* 6 (2025), 479–503, DOI 10.2140/pmp.2025.6.479, [arXiv:2303.10640v2](https://arxiv.org/abs/2303.10640): **Theorem 3.1, PDF p.8**, assumes strictly positive rates via (R3), PDF p.7. Thus it does not directly apply to KCM. The planar theorem proved here uses bounded conditional odds of the stationary measure while retaining zero transition rates.

The report therefore remains PARTIAL. Open: remove the conditional-odds assumption in the planar result; handle arbitrary non-translation-invariant stationary measures in higher dimensions; and specify and identify canonical laws on general null bootstrap fibers.

Task: “Open problem D0028” — received 2026-11-13, 08:55 +04 (Asia/Tbilisi; launch/task clock).
