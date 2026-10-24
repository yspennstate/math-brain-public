# Second serious attempt — E0025, 12 October 2026

The first attempt proved one hand-designed type-(1/4,3/4) example satisfies (H), but lacked finite-energy control for arbitrary densities and singular measures. The universal question remains the target.

## Two approaches not pursued in the first attempt

1. **Replace the particular density and exact scale recursion by a moment-separation theorem.** Split an arbitrary perturbing Lévy measure at a small-jump cutoff. Its large-jump mass and small-jump first moment control the Fourier exponent without knowing its density or phases. Derive conditions on these two moments that give wide good frequency intervals. This could cover arbitrary profiles, singular/atomic perturbations, and all 0<α<β<1, rather than one explicit density. Test the borderline where the intervals collapse, and test the brain's atomic example against this new criterion.
2. **Transfer (H) by equivalence of Lévy path laws.** Use the survey's change-of-measure Theorem 2.30 and the Hellinger criterion for equivalence of Poisson random measures: compare a problematic density with a stable or special-subordinator reference. A perturbation satisfying ∫(√ρ−√ρ_ref)² dx<∞ might inherit (H). The issue is whether arbitrary type-(α,β) densities admit such a reference: strong spikes generally have infinite Hellinger distance. This is a different probabilistic route, but looks less likely to close the current gap.

I pursue approach 1, because it offers a checkable stronger special case and a concrete test of the arbitrary-measure obstruction. Approach 2 is a proposed route only; no equivalence theorem is used without verifying its drift and path-law hypotheses.

## Brain query about the gap

Ran `math_recall.py "Hunt hypothesis Hu Sun finite energy Clog subordinators good frequency bands arbitrary Levy density"`. It returned the earlier atomic witness and general finite-energy cards, not a theorem providing the missing frequency windows. The atomic witness is used only as a test case; its point-polarity assertion remains heuristic. The store's Dirichlet-form S_0 cards concern a different presentation of energy and do not themselves supply the needed Fourier inequality.

## Working formulation

Let μ=μ_α+κ, where μ_α(dx)=1_(0,1](x)x^(-1-α)dx, 0<α<1, κ is any positive Lévy measure on (0,∞) with ∫(1∧x)κ(dx)<∞, and deterministic drift is zero. Define

M(h)=κ([h,∞)), L(h)=∫_(0,h) x κ(dx).

For every h>0 and z≥0,
|ψ_κ(z)|≤2M(h)+zL(h).

The candidate theorem requires cutoffs h_n and endpoints 1<u_n<v_n with M(h_n)≤C u_n^α, L(h_n)≤C v_n^(α−1), v_n≥u_n^s for a fixed s>1, u_n→∞, and Σ1/log u_n<∞. These assumptions would yield good bands with a common uniform constant. Precise window endpoints and constants will be checked next; simply identifying good frequency bands is not enough.

## Theorem A: a moment-separation criterion (complete proof)

Assume μ=μ_α+κ as above. Suppose there are a constant C>0, a constant s>1, cutoffs h_n>0, and strictly increasing endpoints u_n→∞ such that u_n≥2 and v_n≥u_n^s, with

M(h_n)≤C u_n^α, L(h_n)≤C v_n^(α−1), Σ_n 1/log u_n<∞.

Then the driftless subordinator with Lévy measure μ satisfies (H). No density is assumed for κ.

**Proof.** Absolute convergence of ψ_κ(z)=∫(1−e^(izx))κ(dx) follows from |1−e^(izx)|≤min(2,|z|x) and ∫(1∧x)κ(dx)<∞. Split κ into [h_n,∞) and (0,h_n). For any real z,

|ψ_κ(z)|≤2M(h_n)+|z|L(h_n).

This includes atoms at the cutoff in the first part, so none are lost. For the truncated stable base, the same integral split as in the first proof, with general α, gives

|ψ_α(z)|≤C_α|z|^α for |z|≥1,
C_α=1/(1−α)+2/α,
Re ψ_α(z)≥c_α|z|^α for |z|≥2,
c_α=(1−cos1)∫_1^2 t^(−1−α)dt>0.

For |z|<1, |ψ_α(z)|≤|z|/(1−α)≤C_α. Real parts of all positive Lévy-measure contributions are nonnegative. Hence R(z)≥c_α|z|^α for |z|≥2. Write A=1+R, B=|1+ψ|.

If |z|∈[u_n,v_n], then M(h_n)≤C|z|^α. Also

|z|L(h_n)≤C|z|v_n^(α−1)≤C|z|^α,

because α−1<0 and |z|≤v_n imply v_n^(α−1)≤|z|^(α−1). Thus

|ψ(z)|≤(C_α+3C)|z|^α,
B(z)≤K A(z), K=1+(C_α+3C)/c_α,

uniformly on these frequency bands. The added 1 is bounded by A.

For all |z|≤u_n, including |z|<1,

|ψ(z)|≤C_α u_n^α+2C u_n^α+C u_n v_n^(α−1)
≤(C_α+3C)u_n^α,

since v_n≥u_n and α−1<0. Therefore B(z)≤D_0u_n^α, D_0=1+C_α+3C. Choose D>D_0 and put y_n=D u_n^α. Fix any t with 1<t<s.

If y_n≤B(z)<y_n^t, the low-frequency bound excludes |z|≤u_n. Using the global lower bound for R then gives

|z|<(y_n^t/c_α)^(1/α)=c_α^(−1/α)D^(t/α)u_n^t.

For every sufficiently large n this is ≤u_n^s≤v_n, because u_n^(s−t)→∞. Thus the **entire** B-window {y_n≤B<y_n^t} is contained in the good frequency bands, with both signs of z included. No monotonicity of A or B was used.

Let η be any finite positive measure with finite 1-energy E(η)=∫A/B² |η̂|² dz. On the selected window B≤KA, so

∫_{y_n≤B<y_n^t}|η̂|²/(B log B)dz≤(K/log y_n)E(η).

The sum is finite, since log y_n=log D+αlog u_n and Σ1/log u_n<∞. After discarding the finite initial indices, y_n is strictly increasing, its first value exceeds 1, and it tends to infinity. This verifies survey Theorem 2.11(i), with its parameter ς=t and one sequence for all finite-energy measures.

Finally its regularity hypothesis holds: exp(−tR(z)) is integrable for every t>0 by R(z)≥c_α|z|^α outside [−2,2]. Fourier inversion gives bounded continuous transition densities; integration in time gives resolvent densities; Hawkes's equivalence, as stated on survey p. 4, gives lower semicontinuity of all 1-excessive functions. The criterion therefore implies (H). ∎

## Theorem B: arbitrary pulse measures, all α and β

Let 0<α<β<1, and set

K_crit=β(1−α)/(α(1−β)).

Let K>K_crit, let 0<r_n<1 satisfy r_(n+1)≤r_n^K, and let κ_n be arbitrary finite positive measures supported on [r_n,2r_n] with total mass κ_n((0,∞))≤C r_n^(−β). After omitting finitely many scales if necessary, the intervals are disjoint. Then the driftless subordinator with

μ(dx)=1_(0,1](x)x^(−1−α)dx+Σ_n κ_n(dx)

satisfies (H). This includes singular and atomic κ_n; in the density case κ_n(dx)=g_n(x)dx, 0≤g_n(x)≤C'x^(−1−β), it is a type-(α,β) example. No lower bound on any individual pulse is imposed.

**Proof.** K_crit>1 because β>α, so K>1. The recursion gives r_n≤r_1^(K^(n−1)), hence r_n→0. Each pulse has first moment at most 2C r_n^(1−β). Once r_n is sufficiently small, consecutive powers r_n^(1−β) decrease with ratio at most 1/2, since

r_(n+1)^(1−β)/r_n^(1−β)≤r_n^((K−1)(1−β))≤1/2.

Thus Σ_n∫x κ_n(dx)<∞. The total measure is a valid subordinator Lévy measure; its infinite activity already follows from the stable base. The finitely many omitted κ_n have finite total mass and can be included in the coarse mass bounds below by increasing constants. This avoids any appeal to arbitrary independent-sum closure.

For sufficiently large n the reverse coarse ratios obey

r_(n−1)^(−β)/r_n^(−β)≤r_(n−1)^((K−1)β)≤1/2.

Consequently Σ_(j≤n)κ_j((0,∞))≤C_1 r_n^(−β) for a uniform C_1. Similarly

Σ_(j>n)∫x κ_j(dx)≤4C r_(n+1)^(1−β)≤4C r_n^(K(1−β)).

Because 2r_(n+1)<r_n eventually, choose any h_n between these two endpoints. For κ=Σκ_j, its M(h_n) is exactly the prefix mass and its L(h_n) exactly the tail first moment. (Early finitely many pulses are all eventually above h_n.)

The strict inequality K>K_crit says

β/α < K(1−β)/(1−α).

Choose fixed p,q with β/α<p<q<K(1−β)/(1−α), and define u_n=r_n^(−p), v_n=r_n^(−q). The sequence u_n is strictly increasing and tends to infinity, and v_n=u_n^(q/p), with q/p>1. The moment bounds give

M(h_n)≤C_1 r_n^(−β)≤C_1u_n^α,
L(h_n)≤4C r_n^(K(1−β))≤4C r_n^(q(1−α))=4C v_n^(α−1),

because 0<r_n<1 and the displayed exponent inequalities have the specified direction. Furthermore

Σ1/log u_n≤[1/(p log(1/r_1))]Σ K^(−(n−1))<∞.

Theorem A applies after adjusting constants and dropping finite initial indices. This proves (H).

For the density subclass, the stable lower bound is immediate. The sufficiently late pulses are disjoint, while the finitely many early pulses give a finite maximum overlap multiplicity J. Thus ρ(x)≤(1+JC')x^(−1−β) on (0,1], because x^(−1−α)≤x^(−1−β) there. Choosing c>max(1,1+JC') verifies Definition 2.28. If all pulse intervals were disjoint from the outset, J=1. ∎

**What is stronger than before.** The first proof used only α=1/4, β=3/4, exact r_(n+1)=r_n^16, and exactly flat power-law pulses. Theorem B covers every parameter pair, only an upper gap bound on r_(n+1), arbitrary pulse profiles or singular measures, and every K>K_crit. For α=1/4, β=3/4 the threshold is 9, so K=10 already suffices. Theorem A goes further: it does not require pulse supports at all, only the measured prefix/tail conditions. These are proved special cases derived from an existing criterion, not claims of novelty or of a full solution.

## Hostile tests: where this stronger route still fails

### Boundary K=K_crit

Take exact recursion r_(n+1)=r_n^K and full pulses κ_n(dx)=1_[r_n,2r_n](x)x^(−1−β)dx. At a cutoff between the n-th and (n+1)-th supports,

M(h_n)≥c r_n^(−β), L(h_n)≥c r_(n+1)^(1−β)=c r_n^(K(1−β)).

Suppose fixed power endpoints u_n=r_n^(−p), v_n=r_n^(−q) met Theorem A's uniform moment bounds. The first inequality forces pα≥β: otherwise M/u_n^α≥c r_n^(pα−β)→∞. The second forces q(1−α)≤K(1−β): otherwise L/v_n^(α−1)≥c r_n^(K(1−β)−q(1−α))→∞. At K=K_crit these imply p≥β/α and q≤β/α, leaving no q>p.

For (α,β)=(1/4,3/4), K_crit=9 and p≥3≥q. This is a proved obstruction to **this fixed-power between-pulse implementation**. It is not a claim that (H) fails at K=9, or that another cutoff or Fourier estimate cannot work.

### Stronger boundary obstruction: allowing every cutoff does not help

The fixed-power test can be strengthened. For the same full-pulse perturbation κ, exact recursion r_(n+1)=r_n^K, and **every 1<K≤K_crit**, Theorem A fails for every possible sequence of cutoffs and frequency endpoints, not just between-pulse cutoffs or fixed powers. This statement concerns Theorem A with the chosen α-stable base, not (H).

Put d=(1−α)/α>0. A full pulse has mass m_β r_n^(−β) and first moment l_β r_n^(1−β), where m_β=∫_1^2 x^(−1−β)dx>0 and l_β=∫_1^2 x^(−β)dx>0. I claim that for every sufficiently small h,

M(h)^d L(h)≥c>0,

with c independent of h. For h in the gap (2r_(n+1),r_n), the prefix contains pulse n and the tail contains pulse n+1. Hence

M(h)^d L(h)≥m_β^d l_β r_n^(K(1−β)−βd)≥m_β^d l_β,

because K≤K_crit=βd/(1−β) makes the exponent nonpositive and r_n<1.

For h inside [r_n,2r_n], let t be the fraction of the n-th pulse mass included in [h,2r_n], so 0≤t≤1. If t≥1/2, then M(h)≥(m_β/2)r_n^(−β) while L(h) contains the whole (n+1)-th pulse. The same nonpositive exponent gives a uniform positive bound.

If t≤1/2, at least half the current pulse mass lies below h, and each such jump has size at least r_n. Thus L(h)≥(m_β/2)r_n^(1−β). The prefix contains the previous pulse, so M(h)≥m_β r_(n−1)^(−β)=m_β r_n^(−β/K). Therefore

M(h)^d L(h)≥m_β^d(m_β/2) r_n^((1−β)−βd/K)≥m_β^d(m_β/2),

again because K≤βd/(1−β). Endpoints cause no mass ambiguity here since the full pulses are densities. These two cases and the gaps cover all sufficiently small positive h; take c to be the minimum of the three positive constants.

But the assumptions of Theorem A would imply

M(h_n)^d L(h_n)≤(C u_n^α)^d C v_n^(α−1)
=C^(d+1)(u_n/v_n)^(1−α)
≤C^(d+1)u_n^((1−s)(1−α))→0,

contradicting the lower bound. Its cutoffs must indeed tend to zero, since L(h_n)→0 and L(ε)>0 for every fixed ε>0. Thus no cutoffs escape the argument. This proves a sharp limitation of the moment-separation criterion on this family: K>K_crit is sufficient by Theorem B, whereas 1<K≤K_crit cannot meet Theorem A for this perturbation and fixed base. The status of (H) throughout the latter range is not determined here.

### The brain's atomic example defeats Theorem A for every fixed base index

Let κ=Σ_(m≥1)a_m δ_(x_m), x_m=4^(−m²), a_m=2^(−m)4^(m²). At a cutoff x_(m+1)<h≤x_m,

M(h)≥a_m, L(h)=Σ_(j>m)a_jx_j=2^(−m).

If Theorem A held at such a cutoff for any fixed 0<α<1 and fixed C, its two bounds would force

u≥(a_m/C)^(1/α), v≤(C 2^m)^(1/(1−α)).

The logarithm of the lower bound for u is (m²log4−m log2−log C)/α, whereas the logarithm of the upper bound for v is (log C+m log2)/(1−α). The quadratic term eventually dominates, so u>v for all sufficiently large m. Thus no such bands exist.

This rules out the criterion for *any* sequence of cutoffs: its L(h_n)≤Cv_n^(α−1) would tend to zero because v_n≥u_n^s→∞. For this atomic measure L(h)→0 along a sequence only when its included-tail index m→∞ (cutoffs at atoms use the same convention, and their tail mass is 2^(−m)). Every sufficiently small positive cutoff belongs to one of the displayed intervals. Therefore the contradiction is unavoidable. Adding any truncated stable base μ_α does not repair the moment criterion. This does **not** prove failure of (H) for the atomic process or its stable regularization; it proves that this route cannot be made universal merely by adding a fixed stable base.

### A known positive case also lies outside the criterion with a weak base

If κ(dx)=1_(0,1](x)x^(−1−β)dx with β>α, then for h→0, M(h) is comparable to h^(−β) and L(h)=h^(1−β)/(1−β). The moment inequalities force u≥c h^(−β/α) and v≤C h^(−(1−β)/(1−α)), again incompatible with u<v since β/α>(1−β)/(1−α). Yet μ_α+κ is locally quasi-stable of index β: x^(−1−β)≤ρ≤2x^(−1−β) on (0,1]. Survey Proposition 2.27 implies (H). The failure is therefore a limitation of the chosen baseline/moment estimate, not a negative test for (H).

## Checking approach 2: direct stable-reference path equivalence fails

For the original density from ATTEMPT.md, compare with **any** truncated stable reference ν_γ(dx)=c 1_(0,1](x)x^(−1−γ)dx, c>0 and 0<γ<1. I prove the two processes' laws on the time interval [0,1] are mutually singular. This rules out direct equivalence-based transfer from any of these stable references. It does not rule out every special-subordinator reference.

First, for independent Poisson counts with parameters a,b, their Hellinger affinity is

Σ_(k≥0)√(e^(−a)a^k/k! · e^(−b)b^k/k!)
=exp(−(a+b)/2)Σ_(k≥0)(√(ab))^k/k!
=exp(−(√a−√b)²/2).

For counts in pairwise disjoint jump-size bins J_n, the finite-vector laws have affinity exp(−Σ_(n≤N)(√a_n−√b_n)²/2), by independence and the product rule. Here a_n=μ(J_n), b_n=ν_γ(J_n), and each bin is bounded away from zero, so these intensities are finite and the Lévy jump counts on [0,1] really are independent Poisson variables.

If Σ(√a_n−√b_n)²=∞, these finite-vector affinities tend to zero. To see that the full count laws are singular without assuming a general infinite-product theorem, choose N_k with affinity≤2^(−k). Let p_k,q_k be the count-vector probability mass functions through N_k, and E_k={p_k≥q_k}. Then

P(E_k^c)+Q(E_k)=Σ min(p_k,q_k)≤Σ√(p_kq_k)≤2^(−k).

By the first Borel–Cantelli lemma, under P all but finitely many E_k occur, while under Q only finitely many E_k occur. Hence P(liminf E_k)=1 and Q(liminf E_k)=0, proving singularity. Since jump counts in these bins are measurable functions of a càdlàg Lévy path, singularity of their pushforward laws implies singularity of the path laws.

Now use the original r_n=2^(−16^n).

* If γ≤α=1/4, choose J_n=[r_n,2r_n]. The original intensity a_n≥m r_n^(−β), β=3/4, while b_n=c d_γ r_n^(−γ), d_γ=∫_1^2 u^(−1−γ)du>0. Thus b_n/a_n→0, and eventually (√a_n−√b_n)²≥a_n/4. Since a_n→∞, the series diverges.
* If γ>α, choose J_n=(2r_n,4r_n). For all sufficiently large n these are disjoint bins lying in gaps between pulse supports, so the original density there is just x^(−1−α). Then a_n=d'_α r_n^(−α) and b_n=c d'_γ r_n^(−γ), with d'_δ=∫_2^4 u^(−1−δ)du>0. Now a_n/b_n→0, and eventually (√a_n−√b_n)²≥b_n/4; the series again diverges.

This proves the claimed singularity for every stable reference index γ and amplitude c. It supplies a concrete obstruction to approach 2 even for our already-proved positive example.

## Referee checklist and precise remaining gap

1. The perturbation may be singular and infinite, but each cutoff has finite M and finite L; the Lévy-integrability assumption guarantees both. At cutoff atoms, the half-open split is explicit.
2. The reversed inequality for exponent α−1 is essential in both the band and low-frequency estimates; its direction was checked.
3. Wide frequency bands alone do not suffice: all frequencies in each B-window were captured using a global lower bound and a global low-frequency upper bound. The constants are absorbed by taking t<s, not by assuming they are 1.
4. The energy bound is uniform over all finite-energy measures and uses their actual A/B² energy. No Lebesgue-average estimate replaces that quantifier.
5. The stable base supplies the required transition/resolvent densities. The criterion does not prove those hypotheses for a purely atomic arbitrary subordinator.
6. Early overlapping pulses need not be dropped from the process. They enter the uniform prefix constant and the finite density-overlap multiplicity; no use is made of the open arbitrary-sum question.
7. The condition K>K_crit is sufficient for Theorem B. The stronger threshold obstruction rules out every cutoff in Theorem A for the full-pulse family when 1<K≤K_crit; it and the atomic obstruction are not counterexamples to (H).
8. The path-singularity argument compares jump counts directly, handles every fixed stable reference, and does not confuse singular path laws with different polar sets or failure of (H).

**Remaining gap after the second attempt:** Theorem A requires a stable real-part lower bound and simultaneous prefix-mass/tail-moment separation. The full-pulse type-(α,β) densities with 1<K≤K_crit provably supply no such cutoffs for this fixed base, even allowing arbitrary cutoff locations and endpoints. The explicit atomic perturbation also supplies none for any fixed stable base index. The direct stable-reference equivalence route fails for the first positive example. We still have no method to control every finite-energy measure on bad Fourier frequencies without those moment gaps, and no general potential-theoretic argument converting semipolar sets into polar sets for all driftless infinite-activity subordinators. Neither universal statement in Question 5 is settled.

## Finite and numerical checks

`second_checks.py` saves `second_checks.json`. All parameter margins were checked with exact rational arithmetic for 15 ordered pairs α<β from {1/10,1/4,1/2,3/4,9/10,99/100}, taking K=K_crit+1/2 and selecting p,q by trisection of the available interval. It checks pα>β, p<q, q(1−α)<K(1−β), and a window exponent t>1 with pt<q.

The same script checks the atomic obstruction with C=1 and six fixed α values. The first incompatible tail indices are m=1,1,2,3,6,51 respectively. These finite checks support the quadratic-versus-linear calculation; the proof for every fixed α and C is the asymptotic argument above, not an extrapolation from those tests.

The independent-Poisson affinity formula was also checked by an 80-digit finite sum through k=499 for (a,b)=(0.1,1),(1,10),(10,100), agreeing with the closed form to relative error below 10^(−70). The full affinity identity and singularity proof are analytic; these sums are supplementary numerical evidence, not rigorous interval certificates.

## Second Lean verification

SecondMargins.lean passed lake env lean from ~/lean_verify, with no sorry or native_decide (see second_lean_check.txt). It kernel-checks the general algebraic implication from K>K_crit to existence of p<q in the admissible exponent interval, and five exact rational margin checks. The analytic theorems and path-singularity argument are not formalized.
