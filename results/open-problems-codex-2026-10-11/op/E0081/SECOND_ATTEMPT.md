# Second attempt at E0081 — 12 October 2026

## Gap and two approaches not used in the first attempt

The previous record does not determine the enlarged-window occurrence probability for a specified structured family. A concrete remaining instance is the source's first-passage family FP_{lambda,n}, with lambda<0 fixed and endpoint lambda_n of order -sqrt(n): its displayed bounds are c_lambda n <= E T <= C_lambda n^(5/4).

**Approach A: first-passage ballot probabilities, conditioned overlaps and cluster size.** For a given first-passage word, compute the probability that a shifted overlapping window is another first-passage word. Retain the dependence of the ballot probability on its endpoint, rather than using the source's separate crude bounds on endpoint height and binomial mass. This may improve the maximum overlap sum, and hence improve the enlarged-window second-moment bound. This approach was not used in the original record, whose logarithmic bound depended on the whole family's cardinality rather than its first-passage structure.

**Approach B: descending-ladder renewal decomposition.** A first passage to -h decomposes into h first passages to -1. Their durations are iid odd-valued variables with generating function (1-sqrt(1-z^2))/z and tail of order t^(-1/2). Translate scanning all start positions into a relation between overlapping ladder-renewal intervals; try to use critical intersections of 1/2-stable renewal processes to determine the occurrence-cluster correction. This might explain a logarithmic correction, but the first obstruction is that start positions are not all descending ladder epochs of one fixed walk. One must justify the scanning/renewal correspondence before applying an intersection theorem.

Approach A is selected: it gives an exact finite overlap identity that can be independently enumerated, and it appears capable of replacing the power gap by a logarithmic gap. No n log n asymptotic is claimed until both sides are proved.

## Brain query

Ran the prescribed read-only math store script with: `ballot theorem first passage probability Pitman Tang waiting time exponent gap`. The returned cards were about first-passage **percolation**, not one-dimensional walk ballot probabilities. They do not resolve this gap and are not used as mathematical evidence. A more narrowly phrased ballot query will be tried if useful.

## Work in progress

For A=FP(n,h), define paths with increments +/-1, S_0=0, S_n=-h, S_j>-h for j<n, where 1<=h<=n and h has the parity of n. For a fixed such word w, and a shift 1<=l<n, preliminary derivation gives

    P(later shifted window lies in A | earlier word w)
      = 1_{S_l(w)<0} (|S_l(w)|/l) 2^{-l} binom(l,(l+S_l(w))/2).

The retained portion is above the new endpoint exactly when S_l<0, and the appended portion must first pass to S_l at time l.

## 1. Exact ballot count, with proof

For integers l>=1, 1<=a<=l of matching parity, let b(l,a) be the number of +/-1 paths first hitting -a at time l. Then

    b(l,a) = (a/l) binom(l,(l-a)/2).

**Proof.** Reverse the order of increments in a first-passage path. Its partial sum at time j is -a-S_{l-j}<0 for every 1<=j<=l. This is a bijection between first-passage paths and strictly negative paths ending at -a. A strictly negative path starts with -1. Remove this first step: the remaining l-1-step path stays nonpositive and ends at -(a-1). Put u=(l-a)/2. There are binom(l-1,u) unrestricted such paths. Those hitting +1 are in bijection, by reflecting the initial portion through its first +1, with unrestricted paths ending at -(a+1), counted by binom(l-1,u-1). Reflection lowers the endpoint by 2: the reflected prefix ends at -1 instead of +1. As usual binomial coefficients outside their index range are zero. The difference is

    binom(l-1,u)-binom(l-1,u-1)
      = ((l-u)/l-u/l) binom(l,u)
      = (a/l) binom(l,u).

The boundary u=0 has no bad path and gives the same formula. All bijections preserve the number of steps. □

In particular, the density of FP(n,h) is

    p(n,h) = (h/n) 2^{-n} binom(n,(n-h)/2).

## 2. Exact conditional overlap identity

**Proof.** Fix the earlier n-step first-passage word w. After shifting by l<n, the retained suffix ends at height -h-S_l relative to the new start. To be strictly above the later window's terminal value -h at this intermediate time, it is necessary that S_l<0. If S_l>=0, the suffix already reaches or crosses the new terminal level before the last step, so the conditional probability is zero. If S_l<0, every retained intermediate height S_j-S_l, l<=j<=n, is strictly above -h: for j<n, S_j>-h and subtracting a negative S_l only increases it; for j=n this follows from S_l<0. Thus the retained portion introduces no additional restriction. The l new independent fair increments must first reach a displacement S_l=-a at their last step. Section 1 counts them. Since S_l>-h for l<n, 1<=a<=h-1 whenever a>0. This proves the displayed identity above, including its zero case. □

## 3. Uniform ballot-probability bound without a Gaussian estimate

For matching-parity 1<=a<=l, let P_l(a)=2^{-l} binom(l,(l-a)/2). Then

    a P_l(a) <= 1,             b(l,a)/2^l <= 1/l.

**Proof.** The distribution of the symmetric l-step sum is symmetric. Its total strictly negative mass is at most 1/2. Among negative values -b with 1<=b<=a and matching parity, there are K=ceil(a/2) possibilities. Each has probability at least P_l(a), since binomial coefficients increase toward the middle: this follows directly from binom(l,j+1)/binom(l,j)=(l-j)/(j+1)>=1 for j<(l/2). Consequently K P_l(a)<=1/2. Since K>=a/2, we get a P_l(a)<=1. The ballot formula gives the second inequality. This deliberately uses a loose constant; no tail estimate is needed. □

## 4. Improved waiting-time bound for a concrete unresolved family

Let H_0=0, H_j=sum_{l=1}^j 1/l. For every admissible n,h, writing p=p(n,h),

    E T(FP(n,h)) <= ((2n-1)/(n p))(1+2H_{n-1})
                 <= 2(1+2H_{n-1})/p.

**Proof.** In a random (2n-1)-bit word let N count occurrences among its n candidate n-step windows, and q=P(N>0). Then E N=np. For two window starts separated by l<n, conditional on the earlier word being in FP(n,h), Sections 2 and 3 bound the probability of the later occurrence by 1/l. Thus their joint probability is at most p/l, and

    E N^2 <= np+2 sum_{l=1}^{n-1}(n-l)p/l
          <= np(1+2H_{n-1}).

Since N is zero off an event of probability q, Cauchy-Schwarz gives (E N)^2<=q E N^2. Hence q>=np/(1+2H_{n-1}). Apply the already proved disjoint-block bound E T<=(2n-1)/q from ATTEMPT.md Section 2. This proves the assertion. All random variables in the second-moment calculation are finite. Integrability of T follows separately from the disjoint n-step trial bound. For n=1 the harmonic sum is empty and the bound remains valid. □

**Fixed scaled endpoint consequence.** Let h_n=-lambda_n, with lambda<0 as in the source. For all sufficiently large n, h_n>0, h_n has n's parity, and h_n/sqrt(n)->a=|lambda|. Then

    p(n,h_n) ~ [a sqrt(2/pi) exp(-a^2/2)]/n,
    c_lambda n <= E T(FP_{lambda,n}) <= C_lambda n log n.

Here is the binomial asymptotic used in this statement. Set u=(n-h_n)/2, v=(n+h_n)/2 and x=h_n/n=O(n^{-1/2}). Stirling's classical factorial formula with relative error 1+O(1/j), applied at n,u,v (which all tend to infinity proportionally to n), yields

    2^{-n} binom(n,u)
      = (1+O(1/n)) sqrt(2/(pi n)) (1-x^2)^{-1/2}
        exp[-(n/2)((1-x)log(1-x)+(1+x)log(1+x))].

The bracket equals x^2+O(x^4), by Taylor's formula on |x|<=1/2; the remainder is uniform there because the fourth derivative is bounded. Thus n O(x^4)=O(1/n), the prefactor tends to 1, and the binomial probability is asymptotic to sqrt(2/(pi n)) exp(-a^2/2). Multiplication by h_n/n gives p's formula. The lower waiting-time bound is simply T>=n; the upper follows from Section 4 and H_{n-1}<=1+log n (integral comparison). Constants depend on lambda, not on n. □

In particular,

    lim_{n->infinity} log(E T(FP_{lambda,n}))/log n = 1.

Indeed the lower bound gives liminf>=1 and the upper gives limsup<=1 since log log n/log n->0. This determines the **polynomial exponent** for this special family, and excludes any claim E T=Theta(n^zeta) with fixed zeta>1. It does not decide between order n, order n log n, or an intermediate correction. The source's numerical suggestion of a fixed exponent in (1,5/4) is therefore not supported by this bound; it was a suggestion, not its stated theorem. No claim of a full solution to E0081 or of novelty is made.

## Next step

Test whether the harmonic loss can be removed: find a legal word whose conditional overlap sum grows like log n, and inspect exact enlarged-window probabilities. If worst-case overlap is logarithmically large, a uniform-over-words improvement cannot alone give an O(n) waiting-time bound; occurrence-biased or first-hit-biased path distributions would have to be controlled.

## 5. Stronger exact reduction to the first observed word

Let W be the first observed word at the completion time T, and for w in FP(n,h) let

    C(w)=1+sum_{l=1}^{n-1} g(l,-S_l(w)),
    g(l,a)=1_{1<=a<=l, l-a even} (a/l)2^{-l}binom(l,(l-a)/2).

Then the following identity is exact:

    p E T = E C(W),           1/p <= E T <= (1+H_{n-1})/p.

**Proof.** Let I_t indicate an occurrence completed at t, with I_t=0 for t<n. For t>=n, E I_t=p. Partition by the first completion time s and its word W. If t=s, the subsequent conditional occurrence probability is 1. If 0<t-s<n, it is g(t-s,-S_{t-s}(W)), by the overlap identity. If t-s>=n, the entire later word is composed of future independent increments and its conditional probability is p. The increments after the stopping time T are independent fair bits: to justify this without an unproved strong Markov assertion, condition on each deterministic event {T=s,W=w}, which depends only on the first s bits, and use independence of the remaining bits; then sum over s,w.

For 0<z<1, sum the resulting identity against z^t. All terms are nonnegative, so rearrangement of series is justified. This gives

    p z^n/(1-z)
      = E[z^T (1+sum_{l=1}^{n-1}g(l,-S_l(W))z^l+p z^n/(1-z))].

Equivalently,

    p z^n (1-E z^T)/(1-z)
      = E[z^T (1+sum_{l=1}^{n-1}g(l,-S_l(W))z^l)].

As z increases to 1, (1-z^T)/(1-z)=sum_{j=0}^{T-1}z^j increases to T, so monotone convergence gives the left-hand limit p E T. Integrability was proved by disjoint-block trials. The right-hand limit is E C(W), by bounded convergence, since C(W)<=1+H_{n-1}. This proves the identity and bounds. In particular the improved upper bound has a smaller constant than Section 4's second-moment argument; that earlier independent argument remains valid. □

This reduction isolates a precise remaining question: for h_n of order sqrt(n), determine the order of E C(W) under the **first-hit distribution**, rather than the uniform distribution on first-passage words. Order n would follow from a uniformly bounded first-hit mean C; order n log n would follow from a logarithmic lower bound for that mean. Neither follows merely from the pointwise upper bound.

## 6. A rigorous logarithmic obstruction to a worst-case improvement

Define a_l as the largest nonnegative integer of the same parity as l that is at most sqrt(l). Equivalently, it is floor(sqrt(l)), reduced by one if its parity is wrong. Then a_0=0, a_l-a_{l-1} is always +1 or -1. To check this: between consecutive squares the floor is constant and the parity correction alternates, giving increments +/-1. At a square l=j^2, the old floor j-1 has the parity of l-1 and the new floor j has the parity of l, so the increment is +1. The step at l=1 is also +1.

For n=h^2, the deterministic word whose partial sums are S_l=-a_l lies in FP(n,h): S_n=-h, while for l<n we have a_l<=h-1. Its conditional overlap sum satisfies

    C(w_h) ~ sqrt(2/pi) exp(-1/2) log n.

**Proof.** As l tends to infinity, a_l=sqrt(l)+O(1), with matching parity. The Stirling calculation of Section 4, now with n replaced by l and h_n replaced by a_l, shows

    2^{-l}binom(l,(l-a_l)/2) ~ sqrt(2/(pi l)) exp(-1/2).

Consequently g(l,a_l) ~ c/l, c=sqrt(2/pi)exp(-1/2)>0. The few zero a_l do not matter. For any epsilon>0, all sufficiently large terms lie between (c-epsilon)/l and (c+epsilon)/l. Summing and dividing by log n proves sum_{l<n}g(l,a_l)/log n -> c; the additive 1 in C does not change the limit. □

Thus the maximum C(w) on FP(h^2,h) is of order log n. An attempted proof C(w)<=constant for every first-passage word is false. This explicit obstruction does **not** prove E C(W) grows logarithmically: its first-hit probability may be very small. Replacing first-hit weights by uniform weights would be an unjustified step.

For h=1, all prefixes S_l>=0, so C(w)=1 for every word. Section 5 then gives the exact special case E T(FP(n,1))=1/p(n,1). This is a useful boundary check on the identity, and is distinct from the fixed lambda<0 scaling h of order sqrt(n).

## 7. Closing the logarithmic gap for fixed scaled first-passage endpoints

**Theorem.** For every fixed lambda<0, in the source's symmetric increment-word model,

    E T(FP_{lambda,n}) = Theta_lambda(n log n).

This is an order theorem for a concrete family, not an exact leading constant or a full classification of the arbitrary collections in Question 1.7. The proof below supplies the missing lower bound.

### 7.1 A first-hit domination lemma

For any nonempty family A of n-bit words, with density p, let U be uniform on A, let pi(w)=P(W=w) for the first observed word, and let alpha=p E T. Then

    pi(w) <= alpha U(w)                 for every w in A.

**Proof.** For s>=n, the event {T=s,W=w} is contained in the event {T>s-n, last n bits at s equal w}. The first component is measurable with respect to the first s-n bits, and the second uses the following n independent bits. Thus its probability is at most P(T>s-n)2^{-n}. Summing over s gives pi(w)<=2^{-n}sum_{r>=0}P(T>r)=2^{-n}E T. Since U(w)=1/|A| and p=|A|2^{-n}, this is the asserted inequality. T is integrable by disjoint-block trials. No independence between T and W is asserted. □

For the first-passage family Section 5 gives the further exact identity alpha=E_pi C(W).

### 7.2 An unconditioned logarithmic additive functional

Let S_l be an ordinary fair walk starting at zero, and put

    F_l(s) = g(l,-s),
    B_m = sum_{l=1}^m F_l(S_l).

There exist absolute positive constants c,K and an integer m_0 such that, for m>=m_0,

    E B_m >= c log m,       Var(B_m) <= K(1+log m).

**Mean, full proof.** By symmetry, writing P_l(a)=P(S_l=-a),

    E F_l(S_l) = sum_{a>0, a<=l, a=l mod 2} (a/l) P_l(a)^2.

For all sufficiently large l and all matching-parity a in [sqrt(l)/2,sqrt(l)], the uniform Stirling calculation of Section 4 gives P_l(a)>=c_0/sqrt(l) for some absolute c_0>0. Uniformity follows because a/l<=l^(-1/2), the Taylor remainder is O(1/l), and a^2/l stays in [1/4,1]. There are at least sqrt(l)/8 such integers for all sufficiently large l: the interval has length sqrt(l)/2, one parity has spacing 2, and discarding its endpoints loses at most two candidates. Each term has a/l>=1/(2sqrt(l)), so the displayed sum is at least c_0^2/(16l). Summing these lower bounds from a fixed l_0 to m, and absorbing the fixed initial part, gives E B_m>=c log m for sufficiently large m. No assertion about the exact coefficient is needed. □

**Binomial smoothing estimate.** If Y=S_r with r>=1, and s,t are integers of the same parity, then

    TV(Law(Y+s),Law(Y+t)) <= (|s-t|/2) M_r,
    M_r=max_x P(S_r=x) <= sqrt(2/(r+1)).

Here TV is half the sum of absolute differences of masses. The first inequality follows as follows. Index the parity lattice by consecutive integers. Its binomial masses are unimodal and vanish off a finite interval. Therefore the sum of absolute differences between adjacent masses is twice the maximum mass, by telescoping the increasing and decreasing parts. Shifting by one lattice unit (two walk units) has TV exactly M_r. An integer number |s-t|/2 of such shifts and the triangle inequality give the claim.

For completeness, write c_j=2^{-2j}binom(2j,j). Its recurrence is c_{j+1}=c_j(2j+1)/(2j+2), and c_j^2<=1/(j+1) follows by induction from c_0=1: the needed inequality is (2j+1)^2(j+2)<=4(j+1)^3, whose right minus left side is 3j+2>=0. For even r=2j the maximum is c_j. For odd r=2j+1 the maximum is c_j(2j+1)/(2j+2)<=c_j. These bounds imply M_r<=sqrt(2/(r+1)) for both parities. □

**Variance, full proof.** Section 3 gives 0<=F_l<=1/l. Thus diagonal variances sum to at most sum_{l>=1}1/l^2<infinity (the integral test suffices; its exact value is irrelevant).

Fix 1<=j<k, and write r=k-j. Given S_j=s, the future position at k has law s+S_r. Independently let S'_j have the law of S_j. Then S_r+S'_j has the unconditional law of S_k. Since s and S'_j have the same parity, the smoothing estimate and convexity of TV under averaging give

    |E(F_k(S_k)|S_j=s)-E F_k(S_k)|
      <= (1/k)(M_r/2) E|s-S'_j|
      <= K_0(|s|+sqrt(j))/(k sqrt(r)).

The first inequality uses the elementary fact that expectations of a function taking values in [0,M] differ by at most M times TV. The second uses E|S'_j|<=sqrt(E(S'_j)^2)=sqrt(j), with E(S'_j)^2=j from independence and zero mean of increments.

Multiply by F_j(S_j), average, and use E|S_j|<=sqrt(j) and F_j<=1/j. This gives

    |Cov(F_j(S_j),F_k(S_k))|
      <= K_1/(sqrt(j) k sqrt(k-j)).

For j<=k/2 this is at most K_2/(sqrt(j) k^(3/2)). Summing over these j contributes at most K_3/k, since sum_{j<=k/2}j^(-1/2)<=2sqrt(k). For k/2<j<k, instead use the crude bound |Cov|<=E F_j F_k+(E F_j)(E F_k)<=2/(jk). Summing these terms also contributes O(1/k), since j>k/2 and there are fewer than k/2 terms. Consequently sum_{j<k}|Cov|<=K_4/k. Sum over k<=m and add the diagonal bound to obtain Var(B_m)<=K(1+log m). This does not assume that B_m's summands are independent. □

Chebyshev's inequality now gives, for a suitable absolute c_1>0 and K_5<infinity,

    P(B_m < c_1 log m) <= K_5/log m

for all sufficiently large m: choose c_1=c/2 and divide the variance bound by ((c/2)log m)^2.

### 7.3 Transfer to uniform first-passage words

Let h_n/sqrt(n)->a>0 with matching parity, and U_n be the uniform law on FP(n,h_n). This is exactly the fair n-bit law conditioned on the first passage to -h_n occurring at n. Choose m=floor(n/2). For a particular initial m-step word, write its endpoint as s. If it already hits -h_n by m, its conditional likelihood under U_n is zero. Otherwise its likelihood ratio relative to the unconditioned prefix law is

    f_{n-m}(h_n+s)/p(n,h_n),

where f_r(b)=P(first passage to -b at r), with f_r(b)=0 if b is not a positive admissible endpoint. This follows from independence of the last n-m increments and the first-passage requirement; h_n+s>0 when the prefix survives.

The ballot bound of Section 3 gives f_{n-m}(b)<=1/(n-m). Section 4 gives p(n,h_n)>=c_a/n for sufficiently large n. Thus the likelihood ratio is at most 2/c_a, uniformly over every initial word. It follows that any event concerning the initial m increments has U_n-probability at most (2/c_a) times its unconditioned probability.

Since C(w)>=B_m(w) and log m/log n tends to 1, Section 7.2 therefore gives constants d_a,D_a>0 such that

    U_n{C(w)<d_a log n} <= D_a/log n

for all sufficiently large n. Explicitly take d_a=c_1/2 and use log m>=log n/2 eventually, then absorb 2/c_a and log n/log m into D_a. This uses prefix domination, not equality between the first-hit and uniform word laws. □

### 7.4 Lower bound under the first-hit law

Put L=d_a log n, r=D_a/log n, and alpha_n=p(n,h_n) E T. By Sections 7.1 and 7.3 the first-hit probability of the bad set {C<L} is at most alpha_n r. By the exact identity of Section 5,

    alpha_n = E_pi C(W) >= L(1-alpha_n r).

This inequality remains valid even if alpha_n r>1 (then its right side is negative). Rearrangement yields

    alpha_n >= L/(1+Lr)
            = [d_a/(1+d_a D_a)] log n.

Since p(n,h_n)=Theta_a(1/n), this proves E T>=c'_a n log n. Section 5 gives the matching upper bound. Taking h_n=-lambda_n proves the theorem. □

### Remaining gap after this theorem

For the concrete first-passage family the order gap is closed by this argument; an exact leading constant is still not proved. For arbitrary natural collections in Question 1.7 there is still no full classification. The question has no specified structural assumptions, and the extremal and finite-reduction results do not supply a computable asymptotic order for each possible family. The overall E0081 verdict therefore remains PARTIAL unless the theorem above is found to fail on review. The proof has not been claimed to be a theorem already in print.

## 8. General criterion extracted from the new proof

For any fixed n and nonempty A, define c_l(w) as the probability that the later n-bit window at shift l lies in A when the earlier window equals w, using l new independent bits. Let C_A(w)=1+sum_{l=1}^{n-1}c_l(w). The generating-function proof in Section 5 applies verbatim and gives p E T=E_pi C_A(W); for shifts at least n the conditional probability is p, exactly as before. Section 7.1 also applies without modification.

Consequently, if U is uniform on A and U{C_A<L}<=r, for some L>0 and r>=0, then

    E T >= L/[p(1+Lr)].

The full proof is the same two-line implication, now without a first-passage assumption: pi{C_A<L}<=p E T r, and p E T=E_pi C_A>=L(1-p E T r). Rearranging proves the criterion. This is a general lower bound in terms of the **lower tail** of overlap under the uniform word law. It avoids the false step of identifying uniform and first-hit weights. It is more informative than a second-moment lower bound on the probability of at least one occurrence when many occurrences form clusters.

## 9. Hostile-referee audit and completed checks

Every dependency in the n log n theorem was checked explicitly:

1. **Strict first passage and retained-window state.** The exact overlap formula was checked against enumeration of every possible appended word in **1,013** cases for n<=9. The strict boundary condition and the zero case S_l>=0 were both included.
2. **Ballot endpoints and parity.** The count h/n binom(n,(n-h)/2) was checked against full word enumeration. The binomial inequality a P_l(a)<=1 was checked for every admissible a<=l<=200, and its instances through l=12 were proved by Lean's `decide +kernel`.
3. **First-hit word law.** An independent prefix-automaton solver computed exact absorbing probabilities, not just expectations, for **20** admissible (n,h) pairs with n<=8. It checked pi(w)<=p E T/|A| and the identity p E T=E_pi C in exact rational arithmetic. Uniform and first-hit means differ in some cases, as expected.
4. **Logarithmic concentration.** The smoothing estimate was checked in **512** exact finite instances, including equality TV(shift by 2)=maximum binomial mass. The covariance bounds were checked in **120** exact cases. **146** prefix likelihood ratios were independently counted from first-passage word lists and compared with the killed-walk/future-passage formula.
5. **Moment recursion.** Exact rational first and second moments of B_m were computed for m=4,8,16,32,64. A separate deterministic floating-point moment recursion agrees at m=64 and was run through m=8192. Its variance divided by log m remains near 0.096; this is evidence for, not a substitute for, the analytic O(log m) proof. The exact covariance calculations concern unconditioned walks, which is the law used in the proof; conditioning is transferred only afterwards by the explicitly bounded likelihood ratio.
6. **Self-consistency algebra.** The step alpha>=L(1-alpha r) => alpha>=L/(1+Lr), for nonnegative L,r, was kernel checked in FirstPassageOverlap.lean. The final Lean run exited 0 in 71.60 seconds. No `sorry` or `native_decide` was used. The full probabilistic theorem is proved on paper here and is not claimed fully formalized in Lean.
7. **Worst-case versus first-hit averages.** The explicit square-root path is legal for n=h^2. Its C(w) was computed through n=16384 and grows logarithmically. This disproves a uniform constant bound but does not by itself prove the first-hit lower bound; Section 7 supplies the additional domination and concentration arguments.
8. **Large-integer probability conversion.** A simulation initially overflowed when converting an enormous binomial coefficient before division. It was corrected to form an exact Fraction first and convert the final probability. The corrected run completed, with all filter-alignment checks against direct word tests passing. No conclusion relies on the failed run.
9. **Completion versus start time.** The theorem is stated for completion time T. For the start time T-n, the proved n log n order is the same, since subtracting n changes the mean by a lower-order amount. Thus this new order theorem is unaffected by an additive-n convention difference.
10. **Scaling.** The lower-bound theorem requires a fixed a>0 with h_n/sqrt(n)->a. It is not asserted uniformly as a->0, nor applied to the fixed h=1 boundary. The constants in the prefix domination may be large and depend on a; only the asymptotic order is claimed.

Files: first_passage_checks.json, first_hit_checks.json, logarithmic_lower_checks.json, first_passage_lean_check.txt and their accompanying Python scripts reproduce the finite checks. Independent seeded simulation of q used 16,384 words per n at n=64,...,4096, in small batches well below 1 GB; q estimates decreased from 0.2822 to 0.2041. These finite simulations neither establish a leading constant nor override the proof.

### Additional audit observation

For n=64,h=8, the square-root word has C=26803890238587483831/9223372036854775808, while the downward-then-zigzag word (first h-1 downward steps, then alternating at distances h-1 and h-2, with the last step to h) has C=25829549157456623287/9223372036854775808. Their difference is the positive rational 464602032247/4398046511104. Both words were checked to lie in FP(64,8); their literal bit strings and exact values are saved in exact_column_counterexample.json. Thus the latter word is not a maximum of the column/conditional-overlap sum. This matters when interpreting the source's claimed extremal comparison preceding (2.21), whose printed sign conventions contain inconsistencies; none of the new proofs uses that comparison.

### Final verdict of this additional attempt

The proof of the first-passage **order** theorem survived the dependency audit above: E T(FP_{lambda,n})=Theta_lambda(n log n) for fixed lambda<0. No exact asymptotic constant was proved. The general lower-tail overlap criterion and the first-passage order theorem are additional proved results. E0081 remains **PARTIAL**, because the unrestricted family-indexed question is broader than this special case. The remaining gap is now the general classification/asymptotics for other specified natural collections, and the exact leading constant for this first-passage family, rather than its polynomial/order gap.
