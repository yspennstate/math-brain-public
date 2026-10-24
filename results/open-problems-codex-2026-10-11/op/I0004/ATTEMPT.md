# I0004 — phase-zero recurrence and a transience family

Date: 2026-10-12. Verdict: PARTIAL. This document proves a special-case transience theorem, using a published sufficient criterion. A serious second attempt and its stronger theorem are recorded in FOLLOWUP.md, with the two new approaches in Section 9 below. Neither attempt classifies every irrational angle, and no novelty claim is made.

## 1. Exact chain and published input

Let α be irrational; replacing it by its fractional part, suppose 0<α<1. Put ε_y=+1 if {yα}<1/2 and ε_y=−1 otherwise. The chain on ℤ² jumps from (x,y) to (x+ε_y,y), (x,y+1), (x,y−1), each with probability 1/3. In particular ε_0=+1. We study recurrence of the origin. The chain is irreducible: both signs occur by density of the irrational orbit, vertical movement is unrestricted, and horizontal movements in either direction can be made at a suitable level. Thus recurrence/transience does not depend on the starting vertex.

The external theorem used for transience is Brémont, arXiv:2007.01573v2, Corollary 3.7(3), PDF p. 7:

> The condition ∑_{n≥1} 1/ϕ₊(n) < +∞ is sufficient for transience.

The notation is defined on PDF p. 5: for the bounded-variation, zero-mean function f(t)=(1_[0,1/2)(t)−1_[1/2,1)(t))/2, let F_k be its rotation cocycle at x=0, including F_0=0 and F_k=−∑_{j=k}^{−1}f(jα) for negative k. Then

ϕ₊(n)²=n²+∑_{−n≤k<ℓ≤n, kℓ≥0}(F_ℓ−F_k)².

The hypotheses match exactly: α_y=β_y=γ_y=1/3, µ_y=δ_{ε_y}, and ε_yγ_y/(1−γ_y)=ε_y/2=f(yα). Hypothesis 1.1 holds, for example with η=1/4: the three probabilities exceed η, support {±1} lies in (−4,4), and µ_y(0)=0. The function is piecewise constant, bounded variation and centered. There is no phase exception in this sufficient criterion. We invoke the published theorem rather than claim to reprove its probabilistic mechanism here.

## 2. A positive-side dispersion sufficient criterion

Define C(0)=0 and C(k)=∑_{y=1}^k ε_y for k≥1. For N≥1 set

S(N)=∑_{1≤u<v≤N}(C(v)−C(u))²,

D(N)=√(N²+S(N)), and B(N)=S(N)/N².

The identity S(N)=N∑_{k=1}^N C(k)²−(∑_{k=1}^N C(k))² follows by expanding the square in the ordered double sum and dividing by two. Consequently B(N) is the variance of the N equally weighted values C(1),…,C(N). S is nondecreasing in N because every summand is nonnegative and the index sets are nested. B itself need not be nondecreasing; no such property is assumed below.

For k≥1, F_k=(1+C(k−1))/2. Restricting the positive-side terms in ϕ₊(N+1) to 2≤k<ℓ≤N+1 gives exactly S(N)/4. Hence

ϕ₊(N+1)²≥(N+1)²+S(N)/4≥D(N)²/4.

Therefore ∑_N 1/D(N)<∞ implies ∑_n 1/ϕ₊(n)<∞ and transience. This is only a sufficient criterion; we do not assert the converse here.

## 3. Exact odd-denominator blocks at the source phase

Write α=[0;a_1,a_2,…], with convergents p_j/q_j, using q_0=1, q_{−1}=0 and q_{j+1}=a_{j+1}q_j+q_{j−1}. We use the standard convergent estimate

0<|α−p_j/q_j|<1/(q_j q_{j+1}).

This estimate follows, for completeness, from writing t=[a_{j+1};a_{j+2},…]>a_{j+1} and α=(p_j t+p_{j−1})/(q_j t+q_{j−1}); the determinant p_jq_{j−1}−p_{j−1}q_j has absolute value one. Thus the error has absolute value 1/[q_j(q_jt+q_{j−1})], strictly smaller than 1/(q_jq_{j+1}). The determinant formula follows inductively from the convergent recurrence. An infinite simple continued fraction defines an irrational number; the usual convergent construction or this tail formula establishes the stated objects.

**Block lemma.** Suppose p/q is a convergent with q odd, and its next digit is A≥32. Let K=⌊A/8⌋ and s=sign(α−p/q). Then for 0≤j<K and 1≤r≤q,

ε_{jq+r}=ε_r,

∑_{r=1}^q ε_r=s,

C(jq+r)=C(r)+js.

**Proof.** Set δ=α−p/q and q'=Aq+q_previous>Aq. Every y=jq+r under consideration satisfies 1≤y≤Kq, so |yδ|<K/q'≤1/(8q). For 1≤r<q, the fractional part of rp/q is a nonzero multiple of 1/q because p and q are coprime. Its distance to an integer is at least 1/q. As q is odd, its distance to any half-integer is at least 1/(2q). The perturbation yδ therefore crosses neither an integer nor a half-integer. Its square-wave sign is the same as at rp/q, independently of j.

For r=q, y=(j+1)q is a multiple of q. Its fractional part is {yδ}. If δ>0 this lies in (0,1/(8q)), and has sign +1. If δ<0 it lies in (1−1/(8q),1), and has sign −1. Thus this sign is always s. The q−1 nonzero residues occur in complementary pairs t/q and (q−t)/q, one on each side of 1/2, so their signs sum to zero. Each block consequently has sum s. Summing the preceding j blocks and the first r entries of the next block proves the cumulative identity. This proof starts at height 1, never assigns a rational approximation's sign to height 0, and applies to either sign of δ. ∎

## 4. Exact variance of repeated blocks

Let B=S(q)/q² be the variance of C(1),…,C(q), under the block lemma. For each integer 1≤J≤K,

S(Jq)=(Jq)² [B+(J²−1)/12].                                           (4.1)

**Proof.** Choose independently R uniform on {1,…,q} and U uniform on {0,…,J−1}. The Jq profile values are exactly C(R)+sU. Independence makes their covariance zero: expanding E[(C(R)+sU)²]−(E[C(R)+sU])² gives Var(C(R))+s²Var(U)=B+Var(U). The elementary sums ∑_{u=0}^{J−1}u=J(J−1)/2 and ∑u²=J(J−1)(2J−1)/6, each verified by induction, give Var(U)=(J²−1)/12. Multiplying the variance by (Jq)² proves (4.1). Equivalently, one can expand the pair-scatter formula above. The four-term algebra that cancels the cross term is kernel checked in BlockVariance.lean. ∎

For J≥2, (J²−1)/12≥J²/16. Indeed this is equivalent to J²≥4.

## 5. Special-case transience theorem

**Theorem.** Let

α=[0;1,2,A_1,2,A_2,2,A_3,2,…],

where A_m are positive integers, eventually A_m≥32, and

∑_{m≥1} log(2+A_m)/A_m <∞.                                          (5.1)

Then the exact phase-zero simple random walk in Section 1 is transient. No monotonicity, supergrowth or parity condition on the A_m is needed.

**Proof.** Let Q_m=q_{2m}. Thus the digit following Q_m is A_m, and the digit after it is 2. Since q_{2m}=2q_{2m−1}+q_{2m−2} and q_0=1, every Q_m is odd. Also, writing r=q_{2m−1}<Q_m,

Q_{m+1}=(2A_m+1)Q_m+2r,

so 2A_mQ_m<Q_{m+1}<(2A_m+3)Q_m≤3A_mQ_m whenever A_m≥3. These increasing Q_m tend to infinity.

Set K_m=⌊A_m/8⌋, L_m=K_mQ_m and B_m=S(Q_m)/Q_m². For all sufficiently large m, both A_m and A_{m−1} exceed 31, so K_m≥4 and K_m≥A_m/16.

First obtain a baseline from the preceding tower. Formula (4.1), monotonicity of S, and Q_m≤3A_{m−1}Q_{m−1} give

B_m ≥ S(L_{m−1})/Q_m²

≥ (L_{m−1}/Q_m)² K_{m−1}²/16

≥ (1/48)² (A_{m−1}/16)²/16

= A_{m−1}²/9,437,184 ≥ A_{m−1}²/10,000,000.                       (5.2)

Here L_{m−1}/Q_m≥1/48 follows from K_{m−1}≥A_{m−1}/16. This transfers a large profile variance through the following small digit without assuming that the variance is monotone.

Next, for Q_m≤n≤L_m, abbreviate Q=Q_m, B=B_m. We claim

D(n) ≥ (n/16)√(1+B+(n/Q)²).                                       (5.3)

If Q≤n<2Q, S(n)≥S(Q)=Q²B≥n²B/4 and (n/Q)²<4. Thus D(n)²≥n²(1+B/4)≥(n²/256)(1+B+(n/Q)²). If 2Q≤n≤L_m, put J=⌊n/Q⌋. Then 2≤J≤K_m and JQ≥n/2. By (4.1),

S(n)≥S(JQ)≥(n²/4)[B+J²/16]

≥n²B/4+n⁴/(256Q²).

Adding n² proves (5.3) also in this case.

For L_m≤n≤Q_{m+1}, the same identity gives

D(n)≥√S(L_m)≥K_m²Q_m/4≥A_m²Q_m/1024≥nA_m/3072.                 (5.4)

Now sum 1/D over the whole interval Q_m≤n<Q_{m+1}. Let a=A_{m−1}. From (5.2)–(5.3),

D(n)≥[n/(16√10,000,000)] max{a,n/Q_m}

on Q_m≤n≤L_m. For n≤aQ_m, summing 1/(na) costs at most (1+log a)/a, because ∑_{n=Q}^{aQ}1/n≤1+log a. For n>aQ_m, summing Q_m/n² costs at most 1/a by the integral comparison ∑_{n>aQ}n^(−2)≤1/(aQ). Truncating either range at L_m only reduces these bounds. The resulting stable-region cost is at most an absolute constant times log(2+a)/a.

For the remaining range, (5.4) gives a cost at most

(3072/A_m)∑_{n=L_m}^{Q_{m+1}}1/n

≤(3072/A_m)(1+log 48),

since Q_{m+1}/L_m≤48. Consequently an absolute constant M, independent of α and m, satisfies

∑_{n=Q_m}^{Q_{m+1}−1}1/D(n)

≤M[log(2+A_{m−1})/A_{m−1}+1/A_m].                                (5.5)

The intervals partition every sufficiently large integer n. Condition (5.1) makes the sum of (5.5) finite; it also implies ∑1/A_m<∞ because log(2+A_m)≥1 for A_m≥1. The finitely many omitted n do not matter. Thus ∑1/D(n)<∞ and Section 2 proves transience. ∎

## 6. Explicit consequences and recurrence baseline

The prior P21 handoff left unclassified

α_gap=[0;1,2,3,2,17,2,513,2,65537,2,…], with A_m=2^(m²)+1.

It meets the theorem: A_m≥32 for m≥3, and log(2+A_m)/A_m≤(m²+2)log(2)/2^(m²)≤(m²+2)log(2)/2^m for m≥1. The latter series converges: its successive-term ratio tends to 1/2 and is eventually at most 3/4. Therefore this previously unclassified exact phase-zero family is **transient**.

A simpler family is A_m=(m+6)², which is also transient. Indeed log(2+(m+6)²)/(m+6)² is bounded by a constant times log(m+6)/(m+6)², and log t≤√t for all sufficiently large t, so the series is dominated by a convergent t^(−3/2) series. All its spikes are at least 49. This example shows that the proof does not need Liouville supergrowth.

For comparison, Brémont's Theorem 3.2 (PDF p. 4) gives recurrence whenever ∑ log(1+a_n)/(a_1+⋯+a_n)=∞. In particular if a_n≤M for every n, each summand is at least log 2/(Mn), so the series diverges and the exact source walk is recurrent. The golden rotation [0;1,1,…] is recurrent. These verifications fully check the application of the published theorem; the underlying recurrence theorem is prior art. Thus a uniform answer “recurrent for every irrational” is false, and so is “transient for every irrational.”

## 7. Hostile-referee checks

1. **Source model:** exact phase zero retained; outgoing probabilities are 1/3; Brémont's horizontal-flow function is ε/2, not ε. The factor 1/2 is kept in Section 2.
2. **Discontinuity at zero:** block analysis uses positive heights 1,…,q and explicitly treats multiples of q. No almost-everywhere assertion is specialized to zero. The integer boundary can be approached from either side; neither is assigned the rational value by continuity.
3. **Parity:** only q_{2m} must be odd. This follows from the intervening even digit 2 regardless of the parity of A_m. Mixed odd spikes were included in exact finite checks.
4. **Every scale covered:** [Q_m,Q_{m+1}) is split into [Q_m,L_m] and [L_m,Q_{m+1}); there is no uncovered region near a new convergent. The second interval has bounded endpoint ratio ≤48.
5. **Variance dilution:** B(N) is not declared monotone. Only S(N) is; the normalization loss is bounded using Q_m≤3A_{m−1}Q_{m−1}. This is the key difference from an invalid monotone-variance argument.
6. **Block range:** K=⌊A/8⌋ ensures a perturbation strictly below 1/(8q), much smaller than the smallest half-boundary margin 1/(2q). The first block is included and the multiple at its endpoint is treated separately.
7. **Uniform constants:** all losses in (5.2)–(5.5) are explicit, independent of m and α; no increasing hidden constant spoils summability. Initial digits with A<32 only contribute finitely many scales.
8. **Computations:** finite_checks.py used exact modular integer arithmetic for long rational approximants, not floating point orientations. It checked the block identity, exact variance formula, baseline constant and selected stable/tail dispersion inequalities. Four examples cover roughly 0.85–2 million heights each, sequentially, with well under 1 GB memory. The expanded run took 128 seconds on the shared machine. A nonmonotone spike example tests a 128-to-32 drop; 3,252 additional boundary cases check both signs of the approximation error for odd denominators up to 51 and digits 32, 33, 64. All checks passed; finite results alone are not proofs for the irrational limit. See finite_checks.json.
9. **Lean:** BlockVariance.lean contains three algebraic identities with no sorry and no native_decide. The principal identity is ((a+x)−(b+y))²+((a+y)−(b+x))²=2(a−b)²+2(x−y)². Running `lake env lean ~/brain_workers/TRIO_1011/op/I0004/BlockVariance.lean` from ~/lean_verify exited 0, with no diagnostics, after 448.69 seconds. Only these identities, not the probability theorem or full argument, are claimed as kernel checked; see lean_check.txt.
10. **Novelty:** the theorem here is an independently written consequence of an established dispersion criterion. We have not searched every earlier application of that criterion and do not claim a new publication-level result.

## 8. Remaining gap after the first attempt (partly resolved by FOLLOWUP.md)

The full question permits arbitrary irrational continued fractions, with no intervening digit fixed at 2 and no summability hypothesis. Neither the sufficient recurrence theorem nor the special-case transience theorem above classifies every such angle. Even the subfamily [0;1,2,33,2,34,2,35,2,…], A_m=m+32, is not classified by the criteria applied here: our transience summability condition diverges, while Brémont's displayed recurrence sufficient condition converges. For the latter assertion, a_1+⋯+a_n grows quadratically in n and log(1+a_n)=O(log n), so its terms are O(log n/n²); this only shows that the sufficient test does not apply. It proves neither recurrence nor transience for that family. No conjectural outcome is promoted to a theorem.

Further work would need sharper control of profile variance across consecutive towers or a global necessary-and-sufficient arithmetic classification. The present proof settles the prior diagnostic α_gap and a broad additional class, but the unrestricted source problem remains unproved in this record.

## 9. Reopened attempt: two genuinely different approaches (2026-10-12)

**Approach A — accumulate variance with an almost lossless tower comparison.** The previous proof retained only a fixed small fraction of the preceding tower, losing a constant factor in the old variance at each step. Instead compare every complete q-block up to the next even convergent with the first q-block. Because the total angular displacement is O(1/q), at most an absolute number of letters can change in each block. The cumulative profile is therefore a translate of the old profile plus a uniformly bounded error. The law of total variance and a quadratic error inequality may give a recursion of the form B_{m+1}≥(1−O(1/A_m))B_m+cA_m²−O(A_m). For A_m=m+32, such a recursion should accumulate order m³ variance and make the dispersion series summable. This is stronger than the previously tried single-tower baseline.

**Approach B — use reflection and the excursion resolvent to obtain a phase-zero criterion.** The source coding satisfies ε_{−y}=−ε_y for y≠0. Positive and negative vertical excursions thus give opposite horizontal displacements, with the exceptional geometric run at height zero retained. One could derive the exact Fourier transform of the iid horizontal excursion increments from a half-line difference equation, and use a Chung–Fuchs/renewal criterion. This might separate the discontinuity's contribution from the symmetric excursion law and avoid continued-fraction sufficient tests. The unresolved task is controlling that characteristic function at small frequency for deterministic rotation scenery; no proof is claimed for this approach.

I pursue Approach A first because it directly targets the concrete unresolved family A_m=m+32 and allows every deterministic estimate to be checked independently of a new probabilistic limit theorem. The math store was queried for “Denjoy Koksma rotation discrepancy variance continued fractions Bremont recurrence”; the relevant card was read in full and its use is recorded in BRAIN_GAP.md.

## 10. Second-attempt outcome and current gap

FOLLOWUP.md proves transience for α=[0;a_1,b_1,A_1,b_2,A_2,…] whenever the b_m are uniformly bounded positive even integers and A_m≥c m^p eventually, for some c>0 and p>2/3. In particular A_m=m+32 with b_m=2 is now classified transient. The proof accumulates variance using a transfer inequality that retains a factor 1−2/A_m of the previous variance, then controls the whole dispersion sum uniformly even when spikes are arbitrarily large.

The exact finite checks in followup_checks.json passed, including variable even intervening digits, nonmonotone spikes, all complete-block errors at checked towers, rational variance inequalities, 18,496 scaled-square tests and 81,200 cubic-barrier tests. VarianceLoss.lean kernel checks the scaled-square inequality and cubic identity; the command exited 0 after 120.79 seconds. The infinite probabilistic theorem itself has not been formalized.

The current remaining gap is the classification of arbitrary irrational angles, including unrestricted parity/growth of the intervening digits and the boundary subfamily A_m=ceil(m^(2/3))+32, b_m=2. The method's reciprocal-dispersion upper bound is nonsummable at that exponent, which proves no outcome there. Approach B was recorded but not pursued, because Approach A produced a complete stronger special-case theorem. Final state of this further attempt: DONE, PARTIAL, with no novelty claim.
