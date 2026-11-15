# From cheap chunks to disjoint path witnesses

The statements checked are Lemmas `df:wi:chunk-witness` and `df:wi:chunk-defect` in OpenAI, *Strict convexity and differentiability of the planar exponential first-passage limit shape* (September 24, 2026). The source is [source-witnesses.tex](source-witnesses.tex), at repository revision `4eaee87548250b2682affda7d05d947c05554bae`. These two lemmas form one deterministic reduction. The probabilistic endpoint estimate is an explicit input when concluding that the resulting local events are rare; the BK and itinerary argument after this reduction is outside the present check.

## Assumptions and the rare-event interface

Fix a slope b in [−1,1], and write x(z)=z₁ and r(z)=z₂−bz₁. Let m₀>0, a₋<a₊, a=(a₋+a₊)/2, c=(a₊−a₋)/2>0, and

\[
 f(z)=m_0x(z)+ar(z),\quad f_\pm(z)=m_0x(z)+a_\pm r(z),
 \quad H(P)=\tau(P)-f(\Delta P),\quad
 H_\pm(P)=\tau(P)-f_\pm(\Delta P).
\]

Assume nonnegative finite edge weights. Cost counts every traversal. All three defects are additive under concatenation, and direct substitution gives

\[
 \min\{H_+(P),H_-(P)\}=H(P)-c|r(\Delta P)|.       \tag{1}
\]

Put η=min{1,c/4} and K=100(1+|a₋|+|a₊|). Take integers s≥2 and L≥1 satisfying

\[
 C_f:=\max\{|m_0-ab|,|a|\}\le\eta s,
 \quad 2m_0L-|a|(s+1)>\eta s,
 \quad 3\eta s+2|a|(s+1)<Ks.                       \tag{2}
\]

In the manuscript these follow by choosing a sufficiently large record scale: s→∞, L/s→∞, while b, the support slopes, η and K stay fixed. For the last inequality, s+1≤3s/2, η≤1, and |a|≤(|a₋|+|a₊|)/2 give the strictly stronger comparison 3η+3|a|<K.

For each integer pair (i,h), define

\[
 v_{i,h}=(iL,\lfloor biL\rfloor+hs),\qquad
 \mathcal B_{i,h}=v_{i,h}+\{|x|\le4L,\ |r|\le4s\}.
\]

Let Aᵢ,ₕ be the union of:

* the existence of a path inside Bᵢ,ₕ with H₊<−ηs or H₋<−ηs;
* the translated event E(s,L) at vᵢ₊₁,ₕ, namely a path from its column x=0 to x=L, entirely within its translated region −L≤x≤2L, |r|≤8s, with cost <m₀L+Ks.

The first event is o(1) by the earlier arbitrary-endpoint estimate with A=R=4 and ε=η. Its endpoints need not be deterministic. The second has probability ≤q₀ by the definition of L at the selected record scale. Exact lattice translation preserves the event probabilities and the displacement defects, so the union bound is ≤q₀+o(1), uniformly over i,h. At a sufficiently large single scale it is ≤2q₀. No independence between the two alternatives is used. The first event's box and the crossing event's box can differ; both are deterministic finite regions. Each path inequality has a deterministic right-hand side, and is decreasing in the weights.

## Chunk geometry, including rounding

Let P be a finite simple lattice path. Starting at a vertex p₀, cut the first time the displacement has |Δx|≥2L or |Δr|≥s. Such a chunk is full; the final uncut part is a remainder. Associate to each chunk the index

\[
 i=\lfloor x(p_0)/L\rfloor,\qquad h=\lfloor r(p_0)/s\rfloor.
\]

For an oriented nearest-neighbor step, |Δx|≤1 and |Δr|≤1. Since x is integer and L is integer, every chunk vertex z satisfies |x(z)−x(p₀)|≤2L; at a longitudinal cut equality is exactly 2L. The transverse coordinate can overshoot, but only by one: |r(z)−r(p₀)|≤s+1. Let θᵢ=biL−floor(biL) in [0,1). Then r(vᵢ,ₕ)=hs−θᵢ, so

\[
 0\le x(p_0)-iL<L,\quad
 0\le r(p_0)-hs<s,\quad
 0\le r(p_0)-r(v_{i,h})<s+1.
\]

It follows that −2L≤x(z)−iL<3L and |r(z)−r(vᵢ,ₕ)|<2s+2≤4s. Thus the entire chunk, including every subpath, is in Bᵢ,ₕ. This argument works for negative x, r, and b because floor, rather than truncation toward zero, is used.

The same calculation with θᵢ₊₁, directly from r(p₀)−hs, gives

\[
 |r(z)-r(v_{i+1,h})|<2s+2.                         \tag{3}
\]

This verifies the shifted crossing center without assuming that its fractional phase agrees with the chunk box's phase.

## A cheap full chunk contains a witness

Let Q be full with H(Q)<ηs.

If |r(ΔQ)|≥s, (1) and c≥4η give

\[
 \min_\sigma H_\sigma(Q)
 <(\eta-c)s\le-3\eta s<-\eta s.
\]

The whole chunk is a witness for Aᵢ,ₕ. This case includes a simultaneous longitudinal and transverse exit.

Otherwise |r(ΔQ)|<s, and fullness forces Δx=±2L. In the backward case, nonnegative cost gives

\[
 H(Q)\ge2m_0L-|a|\,|r(\Delta Q)|
 \ge2m_0L-|a|(s+1)>\eta s,
\]

a contradiction. Thus a cheap nontransverse full chunk exits forward.

Suppose Δx=2L. Its initial column is in [iL,(i+1)L), while its final column is in [(i+2)L,(i+3)L). Because x changes by at most one per step, it hits column (i+2)L. Let z be its first such hit and p its last hit of (i+1)L before z. The subpath Q′ from p to z stays between those columns: leaving left would require a later return to (i+1)L, and leaving right would require an earlier hit of (i+2)L. By (3), Q′ fits in the translated E(s,L) region. Its longitudinal displacement is L.

Write Q=Qᵢₙ*Q′*Qₒᵤₜ. If either outer piece has H<−ηs, it lies in Bᵢ,ₕ and min Hσ≤H makes it a witness for the first alternative. Empty pieces have defect zero and cannot enter this case. If neither outer piece has that property, additivity gives

\[
 H(Q')=H(Q)-H(Q_{\rm in})-H(Q_{\rm out})<3\eta s.
\]

Both endpoints of Q′ differ transversely from p₀ by at most s+1. Hence |r(ΔQ′)|≤2(s+1), and (2) yields

\[
 \tau(Q')=H(Q')+m_0L+ar(\Delta Q')
 <m_0L+3\eta s+2|a|(s+1)<m_0L+Ks.
\]

This is a witness for the second alternative. All three exit cases have been exhausted. The selected witnesses use only edges of Q.

## Very negative chunks supply multiple disjoint witnesses

For a chunk Q let M_Q be the largest number of pairwise edge-disjoint witnesses for its event Aᵢ,ₕ whose edges belong to Q. Every witness is nonempty: a zero-edge path cannot have negative defect, nor cross distinct columns. Since Q has finitely many edges, the attainable cardinalities form a finite nonempty subset of the nonnegative integers, including zero. Thus the maximum is attained.

For each oriented step e, linearity gives f(Δe) in {±(m₀−ab),±a}. Nonnegative cost therefore implies H(e)≥−C_f. Starting at the beginning of Q, stop at the first prefix with H<−ηs, split it off, and repeat on what remains. Immediately before the final step of a stopped prefix its defect was ≥−ηs, so the stopped prefix has defect ≥−ηs−C_f≥−2ηs. Each such prefix lies in the original chunk's box and has min Hσ≤H<−ηs, hence is a witness for the original event, rather than for a newly assigned box.

If t prefixes were split, simplicity makes their edge sets disjoint, so t≤M_Q. The unsplit suffix has defect ≥−ηs, even if empty. Additivity gives

\[
 H(Q)\ge-\eta s-2\eta s\,t
       \ge-\eta s-2\eta s\,M_Q.                    \tag{4}
\]

For a full chunk with M_Q=0, the preceding cheap-chunk lemma gives H(Q)≥ηs. For M_Q≥1, (4) and

\[
 (-\eta s-2\eta sM_Q)-(\eta s-4\eta sM_Q)
   =2\eta s(M_Q-1)\ge0
\]

give, in both cases,

\[
 H(Q)\ge\eta s-4\eta sM_Q.                        \tag{5}
\]

Apply (5) to N full chunks and (4), weakened to −ηs−4ηsM_Q, to the remainder. If M_tot is the sum of their maxima, then

\[
 H(P)\ge(N-1)\eta s-4\eta sM_{\rm tot}.            \tag{6}
\]

Choose a maximizing family for each chunk. Distinct chunks of a simple path share no edges, so their families combine into M_tot disjoint witnesses. Repeated chunk indices cause no problem: their events can be identical while their edge certificates are disjoint. Simplicity is essential at precisely this step and at t≤M_Q; the result is not asserted for walks that retrace edges.

## Independent checks and limits

The finite audit in [audit.py](audit.py) enumerates every directed contiguous subpath of each tested chunk and tests the event definitions directly. It computes M_Q by interval packing, independently of the threshold-splitting construction. This oracle is sufficient: the edge graph of a simple path is a chain, so loop erasure turns any witness using only its edges into one of those directed contiguous subpaths; erasure preserves endpoints and lowers or preserves cost. Greedy packing by increasing right endpoint gives the maximum number of edge-disjoint intervals, by the usual exchange argument. A dynamic-programming calculation supplies a second check of that packing number.

The identity (1) is independently checked by evaluating both functionals. The total bound (6) is checked from actual total path cost as well as by summing local bounds. Geometry is tested with negative coordinates, noninteger and negative slopes, phase changes between i and i+1, transverse and backward exits, cheap forward crossings, and repeated coarse indices. Strict inequality is retained: equality at H=ηs does not force a witness.

Under the stated hypotheses, no gap was found in this deterministic extraction and multiplicity reduction. It adds neither a new Gamma change of measure for arbitrary continuous laws nor a verification of the subsequent BK/itinerary estimate or of the whole preprint. The next step is `df:wi:continuous-bk` and its use for repeated event labels in `df:wi:long-paths`, especially the finite-bit upper approximation and the deterministic itinerary/composition union bound.
