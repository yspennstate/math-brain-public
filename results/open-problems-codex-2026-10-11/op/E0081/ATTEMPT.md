# E0081 — research record, 12 October 2026

## Exact scope and convention

Pitman and Tang, *Patterns in random walks and Brownian motion*, arXiv:1411.0041v3, Question 1.7, printed/PDF page 5:

> Given for each n a collection A_n of patterns of length n, what is the order of the expected waiting time ET(A_n) until some element of A_n is observed in a random walk?

The preceding paragraph specifies simple symmetric walks starting at zero, with increments ±1. Thus patterns are equivalently binary increment words; they are compared after translating the starting height, not by absolute spatial location. There are no structural hypotheses on the collections. Assume n≥1 and nonempty A⊆{0,1}^n. If A is empty the waiting time is infinite. For independent fair bits X_1,X_2,... define

T_A = min{t≥n : (X_{t-n+1},...,X_t)∈A}.

This is the **completion** time, consistent with the source's Theorem 2.1: for a singleton of length 1 the mean is 2, and for the entire collection it is n. The start time is T_A−n and can have a different order for dense collections. Our statements below concern completion times only.

This question is an asymptotic research program over unspecified families, not a proposed universal exponent. A formula for a fixed finite collection was already available in the source. None of the results below is claimed to resolve the program for all natural families.

## 1. Universal cardinality bounds

Put p=|A|/2^n. Then

    max(n,1/(2p)) ≤ E T_A ≤ n/p,

and consequently (n+1/p)/3 ≤ E T_A ≤ n/p.

**Proof.** The n-bit blocks ending at n,2n,3n,... are independent, and each belongs to A with probability p. If G is their first successful index, P(G>j)=(1−p)^j and E G=Σ_{j≥0}(1−p)^j=1/p. Since T_A≤nG, the upper bound follows, and finiteness is established before any expectation manipulations. For integer t≥0, there are at most t candidate completed windows by time t. Each has probability p, regardless of dependencies, so P(T_A≤t)≤tp. Therefore

    E T_A = Σ_{t≥0} P(T_A>t)
          ≥ Σ_{t≥0}(1−tp)_+
          ≥ ∫_0^∞ (1−xp)_+ dx = 1/(2p).

The last inequality follows because the integrand is decreasing and its integral over [t,t+1] is at most its value at t. Also T_A≥n deterministically. Finally n≤E T_A and 1/p≤2E T_A give the displayed combined bound. □

The constants are not asserted optimal. The n-factor uncertainty in the sparse regime is real, as Section 4 proves with equal cardinalities.

## 2. A finite combinatorial reduction with uniform constants

Define the enlarged word set

    D(A) = {x∈{0,1}^{2n−1} : one of its n consecutive n-bit windows lies in A},
    q = |D(A)|/2^{2n−1}.

For every nonempty A,

    n/(2q) ≤ E T_A ≤ (2n−1)/q < 2n/q.

Thus E T(A_n)=Θ(n/q_n) with constants independent of the families. This replaces inverse matching matrices by a finite union-counting problem; it does **not** estimate q_n for an arbitrary structured family.

**Proof of upper bound.** Divide the sequence into disjoint blocks of length 2n−1. Their memberships in D(A) are independent with success probability q. A successful block contains a completed occurrence by its last bit. Hence T_A≤(2n−1)G for a geometric G of mean 1/q.

**Proof of lower bound.** Number candidate windows by their start offsets s=0,1,2,... . A consecutive group of n offsets has probability q of containing an occurrence, by stationarity of independent bits. For integer j≥0 and jn≤t<(j+1)n there are at most jn windows completed by time t (if j=0 there are none). Partition their offsets into at most j groups of n, extending the last group if needed. The union bound gives P(T_A≤t)≤jq. Consequently

    E T_A ≥ n Σ_{j≥0}(1−jq)_+ ≥ n/(2q),

using the decreasing-function integral argument of Section 1. No independence between adjacent groups was used in this lower bound. □

Checks: n=1 gives q=p; A={0,1}^n gives q=1 and T_A=n. Also p≤q≤min(1,np), directly from one window and the union bound. The enlarged-set formula is computationally finite but can have exponential complexity. It is a bound/reduction, not a new universal exponent.

## 3. Runs: exact waiting time and density of the induced family

For 1≤k≤n let A(n,k) consist of n-bit words containing k consecutive 1s. Let R_k be the first completion time of k consecutive 1s in the infinite bit sequence. Then, pathwise,

    T_{A(n,k)} = max(n,R_k),
    E R_k = 2^{k+1}−2,
    2^{k+1}−2 ≤ E T_{A(n,k)} ≤ n+2^{k+1}−2.

**Proof of the pathwise identity.** If R_k≤n the first n-bit word contains the run, so T=n. If R_k>n, the n-bit window ending at R_k contains the run since k≤n; no earlier window can contain it without contradicting the definition of R_k. Thus T=R_k.

**Proof of the run mean.** The disjoint k-block trial bound proves E R_k≤k2^k<∞. Let h_i, 0≤i≤k, be the expected remaining time with i consecutive trailing 1s, with h_k=0. Conditional on the next independent bit, for i<k,

    h_i=1+(h_{i+1}+h_0)/2.

Write c=1+h_0/2. Repeated backward substitution from h_k=0 gives

    h_i=c Σ_{j=0}^{k-i-1}2^{-j}=2c(1−2^{-(k-i)}).

At i=0 this says h_0=(2+h_0)(1−2^{-k}); rearranging gives h_0=2^{k+1}−2. Substitution also gives h_i=2^{k+1}−2^{i+1}. The linear equations have a unique solution: backward substitution forces every h_i in terms of h_0, and the last equation has coefficient 2^{-k}>0. This algebraic formula and its Bellman equations are formalized separately in RunRecurrence.lean; the probability interpretation is proved here, not formalized there. The final inequalities follow from R_k≤max(n,R_k)≤n+R_k. □

**Density estimate.** Let p(n,k)=|A(n,k)|/2^n and μ=(n−k+2)/2^{k+1}. Then

    μ−μ²/2 ≤ p(n,k) ≤ μ.

The lower bound is useful when μ is small; when negative it is only a vacuous bound.

**Proof.** For i=1,...,n−k+1 let I_i indicate a run of k 1s starting at i that is either at i=1 or preceded by 0. Every word containing a run has at least one such start, and conversely. Put Z=Σ I_i. The first indicator has mean 2^{-k}; all the others have mean 2^{-(k+1)}, so E Z=μ. Two distinct indicators whose starts differ by at most k cannot both occur: the second's preceding 0 lies among the first's required 1s. At separation greater than k, their specified bit sets are disjoint, so their expectations factor. Therefore

    Σ_{i<j} E(I_i I_j) ≤ Σ_{i<j} E I_i E I_j ≤ μ²/2.

For every nonnegative integer z, 1_{z≥1}≤z and 1_{z≥1}≥z−z(z−1)/2 (check z=0,1,2, and z≥3). Taking expectations proves the assertion. In particular, if k=o(n) and n2^{-k}→0, then p(n,k)∼n/2^{k+1}. □

## 4. Equal-cardinality families separated by a factor of order n

For **every** sufficiently large integer n let k=ceil(2 log_2 n), and let A_n=A(n,k). Then

    p_n=|A_n|/2^n=Θ(1/n),
    E T(A_n)=Θ(n²).

Indeed n²≤2^k<2n², k=o(n), and Section 3 gives p_n∼n/2^{k+1}, as well as E T(A_n)=2^{k+1}+O(n). On the subsequence n=2^r, k=2r, these sharpen to p_n∼1/(2n) and E T(A_n)∼2n².

Now let m_n=|A_n| and choose the smallest integer d≥0 such that 2^{n-d}≤m_n. For these families eventually 1≤d≤n. Put C_n={words beginning with 1^d}. Choose B_n to contain all of C_n and, in descending lexicographic order, the first m_n−|C_n| remaining words. Then

    |B_n|=|A_n| exactly,       E T(B_n)=Θ(n).

**Proof.** By minimality of d, 2^{n-d}≤m_n<2^{n-d+1}, so

    1/p_n ≤ 2^d < 2/p_n.

The first occurrence of d consecutive 1s ends at R_d. The n-bit word starting at that run's start ends at R_d+n−d and belongs to C_n⊆B_n, regardless of its remaining bits. Therefore

    E T(B_n) ≤ E R_d+n−d ≤ 2^{d+1}+n < 4/p_n+n = O(n).

The lower bound is T(B_n)≥n. All filler words are fixed deterministically, before observing the random sequence. Thus both families have identical cardinalities at every sufficiently large n but their mean waiting times have ratio Θ(n). Extend them arbitrarily and identically over the finitely many smaller indices. □

This disproves any assertion that n and |A_n| alone determine the waiting-time order up to absolute constants. The source itself makes no such assertion; this counterexample is **not** a counterexample to Question 1.7. Both examples are defined as collections of increment patterns in the same walk model.

## 5. Sharp extremal orders at prescribed cardinality

The preceding examples can be strengthened to a complete extremal theorem. For integers 1≤m≤2^n put p=m/2^n and let the minimum and maximum range over **all** collections A⊆{0,1}^n with |A|=m. Uniformly in n,m,

    min E T_A = Θ(n+1/p),
    max E T_A = Θ((1+log_2 m)/p).

These are two-variable extremal bounds, not the order for a given family.

**Minimum: full proof.** Section 1 proves E T_A≥(n+1/p)/3. For any m<2^n choose the smallest d with 2^{n-d}≤m, and fill the subcube beginning with 1^d to cardinality m as in Section 4. Its mean is at most n+4/p. If m=2^n then T_A=n. Thus the minimum is between (n+1/p)/3 and 4(n+1/p).

**Universal logarithmic upper bound: full proof.** Let N be the number of occurrences among the n windows in the (2n−1)-bit word of Section 2. Then E N=np. For two window starts separated by l∈{1,...,n−1}, condition on the entire earlier n-bit word. If it belongs to A, the later window is obtained by appending l new fair independent bits to its fixed overlap. Among these 2^l extensions at most m can give an element of A. Hence the joint probability is at most p min(1,m2^{-l}). It follows that

    E N² ≤ np[1+2 Σ_{l=1}^{n−1}min(1,m2^{-l})]
          ≤ np(2 log_2 m+5).

For the last inequality put s=floor(log_2 m). The terms l≤s contribute at most s, and all terms l>s contribute at most m Σ_{l>s}2^{-l}=m2^{-s}<2. Extending a sum beyond n−1 only increases it. Since N vanishes off the event of probability q, Cauchy–Schwarz gives (E N)²≤q E N²: explicitly apply it to N and the indicator 1_{N>0}. Therefore q≥np/(2 log_2 m+5). Section 2 gives

    E T_A ≤ (4 log_2 m+10)/p ≤ 10(1+log_2 m)/p.

All calculations involve finite random variables, so no limiting or integrability assumptions are hidden.

**Matching extremal lower bound: full proof.** Write a_k=|A(n,k)|. These integers decrease with k, with a_n=1 and a_1=2^n−1. If m≥a_1, any collection of size m has E T_A≥n, and p≥1/2, log_2 m≤n, so E T_A≥(1+log_2 m)/(4p).

Otherwise choose the smallest k with a_k≤m. Then 2≤k≤n and a_k≤m<a_{k−1}. Choose a collection B of exactly m words such that

    A(n,k) ⊆ B ⊆ A(n,k−1),

by adding the first m−a_k words in the set difference in lexicographic order. Monotonicity of hitting times and Section 3 yield E T_B≥max(n,2^k−2)≥max(n,2^k)/2.

Put L=n−k+1≥1. The clump variable Z of Section 3 has mean μ=(L+1)/2^{k+1}. Its pair bound also gives E Z²≤μ+μ². Cauchy–Schwarz therefore gives p(n,k)=P(Z>0)≥μ/(1+μ). Since B contains A(n,k),

    p ≥ (L+1)/(2^{k+1}+L+1) ≥ L/(2^{k+1}+L).

The second inequality follows by cross multiplication: the difference of numerators after multiplication is 2^{k+1}>0. Set M=max(n,2^k). Since L≤n≤M and 2^{k+1}≤2M, it follows that p M≥L/3 and p E T_B≥L/6.

On the other hand, a_{k−1}≤(n−k+2)2^{n−k+1}=(L+1)2^L by the union bound over possible (k−1)-run starts, counting completions. Thus m<a_{k−1} implies log_2 m≤L+log_2(L+1)≤2L. The last inequality follows from L+1≤2^L for integers L≥1, proved by induction: equality holds at L=1, and L+2≤2(L+1)≤2^{L+1}. Hence p E T_B≥(log_2 m)/12. Section 1 also gives p E T_B≥1/2. Taking half the sum of these two lower bounds gives

    p E T_B ≥ 1/4+(log_2 m)/24 ≥ (1+log_2 m)/24.

Combining this construction with the universal upper bound proves

    (1+log_2 m)/(24p) ≤ max_{|A|=m} E T_A
                              ≤ 10(1+log_2 m)/p.

This includes the singleton regime, where the crude n/p bound has a spurious factor n. No claim of novelty is made: related fixed-collection overlap bounds may be classical. The proofs here are independent of matching-matrix inversion.

## 6. Hostile-referee checks and remaining gap

Potential failure points tested or explicitly avoided:

1. Start versus completion time: all formulas use completion time. In particular the prefix example ends at R_d+n−d, not R_d.
2. Independence: only disjoint bit blocks or disjoint specified bits are called independent. Adjacent window groups use union bounds.
3. Runs near the first bit: the start at i=1 has probability 2^{-k}, not 2^{-(k+1)}; it contributes the +2 in μ's numerator.
4. Overlapping starts: separation exactly k still conflicts; separation k+1 is independent.
5. Exact same cardinality: B_n uses a full subcube plus explicitly ordered filler, not an approximate power-of-two count.
6. Integrability: disjoint-block geometric domination is proved before using first-step equations.
7. The earlier ledger's excursion count argument is false: |E_{2n}|∼4^n/(4√π n^{3/2}), and its reciprocal density already equals the source's mean ∼4√π n^{3/2}. The earlier claimed n³ discrepancy is absent. Its autocorrelation-only formula for a multi-pattern race also omits cross terms. Neither is used here.
8. Inverse stochastic matrices need not be nonnegative. The source's wording on p. 9 is stronger than the row-sum conclusion needed there. None of our proofs assumes a nonnegative inverse.
9. The extremal maximum includes m=1, m=2^n−1, m=2^n and n=1. The dense endpoint is treated separately so the sandwich construction never requires a run of length zero.
10. At separation l<n, the earlier window fixes only the overlap; exactly l new independent bits remain. This conditional counting bound, not an unconditional assumption of independent windows, proves the logarithmic upper bound.

### Completed verification

`python -X utf8 check_patterns.py` passed on 12 October 2026. Its independent prefix-automaton absorbing-chain solver uses exact rational Gaussian elimination. It checked **398** collections: all nonempty collections for n=1,2,3, and fixed plus seeded random collections for n=4,5,6. It compared **357** of these exact means against the source's matching-matrix formula, and tested the universal bounds, the enlarged-word reduction and the logarithmic upper bound. It checked minimum and maximum constructions for all **62** pairs (n,m) with 1≤n≤5 and 1≤m≤2^n. Run densities were checked by exhaustive word enumeration for every k≤n≤8, and the pathwise run identity by every history of length n+3 in those cases. Exact smaller examples and rational run-state recursions through n=1024 are saved in checks.json. The asymptotic table supports but does not replace the proofs.

`lake env lean ~/brain_workers/TRIO_1011/op/E0081/RunRecurrence.lean`, run from ~/lean_verify, returned exit code **0** after 74.91 seconds; see lean_check.txt. Only Mathlib.Tactic.Ring was imported; there is no `sorry`, `native_decide`, or probabilistic theorem claimed formally verified. The checked statements are the boundary condition, initial value and exact rational Bellman recurrence. No additional Lean command was run concurrently.

**Remaining gap, updated after the second attempt.** The probability q_n in Section 2 remains unevaluated for an arbitrary natural, structured family A_n. Its enumeration is exponential in n and is not a general asymptotic classification. The extremal theorems of Section 5 say how large or small the mean can be at a given cardinality, not where an individually specified family lies between those extrema. The additional proof in [SECOND_ATTEMPT.md](SECOND_ATTEMPT.md), Sections 1–7, now establishes E T(FP_{λ,n})=Theta_λ(n log n) for each fixed λ<0, closing the source's first-passage **order** gap. Its exact leading constant and exact bridge constants remain undetermined here. Section 8 of that file also gives a general lower-tail overlap criterion. No retrieved later paper has been verified as resolving Question 1.7 under its full scope; rate limits restrict the original literature check. The overall verdict remains PARTIAL, with a stronger proved special case.
