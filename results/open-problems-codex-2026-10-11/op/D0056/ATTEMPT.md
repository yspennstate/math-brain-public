# D0056: a nonconstant counterexample under the stated moment hypothesis

Date: 2026-10-11. Verdict: SOLVED, by counterexample, using the published Chen–Shi product theorem. This is an implication proved here, not SOLVED_IN_LITERATURE, and no novelty claim is made.

## 1. Exact question and source scope

Fix an integer m >= 2. Let X_0 take values in the nonnegative integers, and define in distribution

    X_{n+1} = (X_n^(1) + ... + X_n^(m) - 1)^+,

with independent copies on the right. The proposed implication is

    (m-1) E[X_0 m^{X_0}] = E[m^{X_0}] < infinity
    ==> P(X_n > 0) ~ 4 / ((m-1)^2 n^2).

The fetched source is arXiv:1705.04787v2, 26 June 2019. Conjecture 1 on PDF page 3 says exactly this under condition (4), but the introduction on page 1 also assumes X_0 is not almost surely constant. We respect that standing assumption in the counterexample. Page 4 warns: “Possibly some additional integrability conditions, such as E(X_0^3 m^{X_0}) < ∞ in Theorem 3 below, are necessary for our conjectures to hold.”

The constant-law omission alone would make the supplied transcription false: for m=2, X_0=1 almost surely is critical and remains 1 at every step. That is not our counterexample to the source's conjecture.

## 2. Imported theorem and checked applicability

Chen and Shi, The stable Derrida–Retaux system at criticality, arXiv:2006.06140v1, Theorem 1.1, PDF page 3, prove the following. If the same deterministic m-ary recursion is critical and

    P(X_0=k) ~ c_0 m^{-k} k^{-alpha},  2 < alpha < 4, c_0>0,

then positive constants c_1,c_2 exist such that, for every n>=1,

    c_1 n^{alpha-2} <= product_{i=0}^{n-1} E[m^{X_i}]^{m-1}
                      <= c_2 n^{alpha-2}.

The paper's standing hypotheses also include P(X_0>=2)>0 and finite E[X_0 m^{X_0}]. These are verified below. We use only the upper bound. The upper-bound proof on PDF pages 20–21 was inspected: Lemma 5.1 bounds the product by a constant times n^2 divided by E[X_0^3 m^{X_0} 1_{2<=X_0<=3n}]. For our law the denominator is exactly c(3n-1), so this indeed gives O(n). The published theorem is the external mathematical input; our proof does not purport to formalize its proof.

## 3. Explicit probability law

Set m=2 and define

    A = sum_{k=2}^infinity 2^{-k} k^{-3},
    B = sum_{k=2}^infinity (k-1) k^{-3},
    c = 1/(A+B).

Define the law by

    p_0=c B,  p_1=0,  p_k=c 2^{-k} k^{-3} (k>=2).

Both sums are finite and strictly positive: A is bounded by a geometric series, and B is bounded by sum k^{-2}. Therefore c>0, every p_k is nonnegative, and

    sum_{k>=0} p_k = c(B+A)=1.

In particular p_0>0 and p_2>0, so X_0 is nonconstant and P(X_0>=2)>0.

All sums below are absolutely convergent. We have

    E[2^{X_0}] = cB + c sum_{k>=2} k^{-3} < infinity,
    E[X_0 2^{X_0}] = c sum_{k>=2} k^{-2} < infinity.

Since B=sum_{k>=2}(k^{-2}-k^{-3}), these expectations are equal. This is precisely the required binary criticality identity. The tail is exactly c 2^{-k} k^{-3}, so the imported theorem applies with alpha=3 and yields, for some finite C>0,

    Q_n := product_{i=0}^{n-1} E[2^{X_i}] <= C n  (n>=1).       (1)

The stronger weighted third moment is infinite:

    E[X_0^3 2^{X_0}] = c sum_{k>=2} 1 = infinity.

Thus the example satisfies the original moment hypothesis, including nondegeneracy, but falls outside a possible stronger-moment repair.

## 4. Exact scalar recursion

Write q_n=P(X_n>0), G_n(s)=E[s^{X_n}], and e_n=G_n(2)-1>=0. All these exponential moments are finite. Indeed G_0(2)<infinity, and at each step 2^{(x+y-1)^+}<=2^{x+y}, so independence gives G_{n+1}(2)<=G_n(2)^2<infinity.

For two independent copies, let S=X_n^(1)+X_n^(2). On S>=1, 2^{(S-1)^+}=2^{S-1}; on S=0 it equals 1 instead of 1/2. Thus

    G_{n+1}(2) = G_n(2)^2/2 + P(S=0)/2
               = G_n(2)^2/2 + (1-q_n)^2/2.

Expanding gives the exact recurrence

    e_{n+1} = e_n + e_n^2/2 - q_n + q_n^2/2.                 (2)

No smoothness or asymptotic differentiation is used.

## 5. Barrier lemma, with full proof

Lemma. Suppose e_n>=0 satisfies (2), and q_n~4/n^2. Then there is N>=1 such that

    e_n > 3/(2n) for every n>=N.                            (3)

Proof. From q_n~4/n^2, q_n->0 and

    n^2(q_n-q_n^2/2) -> 4.

Choose N such that q_n-q_n^2/2 >= 3/n^2 for every n>=N. Define b_n=3/(2n). Whenever n>=N and e_n<=b_n, nonnegativity gives e_n^2<=b_n^2, so (2) implies

    e_{n+1} <= e_n + 9/(8n^2) - 3/n^2
              = e_n - 15/(8n^2).

Also b_n-b_{n+1}=3/(2n(n+1))<=3/(2n^2). Consequently, writing d_n=e_n-b_n,

    d_{n+1} <= d_n - 3/(8n^2)                              (4)

whenever e_n<=b_n. In particular d_{n+1}<0 when d_n<=0, so that this condition persists at subsequent times. If there were j>=N with d_j<=0, (4) would give d_{j+1}<=-delta where delta=3/(8j^2)>0. Induction would then give d_k<=-delta for every k>=j+1. Hence

    e_k=b_k+d_k <= 3/(2k)-delta < 0

for all sufficiently large k, contradicting e_k>=0. Such j cannot exist. This proves (3). QED.

This is deliberately weaker than e_n~2/n and is sufficient. The previous intake attempt incorrectly treated a first-order e_n asymptotic as automatically differentiable; that inference is not used here.

## 6. Product contradiction

Assume, for contradiction, the survival conclusion q_n~4/n^2 for the explicit law. The lemma implies e_i>3/(2i) for i>=N. Therefore for n>N,

    log Q_n = sum_{i=0}^{n-1} log(1+e_i)
            >= sum_{i=N}^{n-1} log(1+3/(2i)).

For x>=0, log(1+x)>=x-x^2/2. For completeness, 1/(1+t)>=1-t for t>=0 because their difference is t^2/(1+t)>=0; integrate this inequality from 0 to x to obtain the log bound. It follows that

    log Q_n >= (3/2) sum_{i=N}^{n-1} 1/i
                 - (9/8) sum_{i=N}^{n-1} 1/i^2
             >= (3/2) log(n/N) - (9/8) sum_{i=N}^infinity 1/i^2.

Here the harmonic-sum bound follows by integrating 1/x on each interval [i,i+1], and the squared reciprocal sum is finite by the integral test. Thus a constant K>0 exists such that

    Q_n >= K n^{3/2}  (n>N).                               (5)

Combining (1) and (5) gives K n^{1/2}<=C for arbitrarily large n, an impossibility. Therefore this nonconstant critical law does NOT have P(X_n>0)~4/n^2. A single m=2 counterexample disproves the asserted universal implication for m>=2. QED.

## 7. Hostile referee checks

- Missing standing assumption: source page 1 checked. Our law has p_0,p_2>0, so the refutation does not rely on that omission.
- Same recursion: imported theorem has deterministic m independent copies and decrement 1, exactly as required; no continuous-time or random-offspring theorem is substituted.
- Criticality and integrability: every sum is explicitly given, converges absolutely, and the critical identity is exact, not a numerical fit.
- Stable theorem endpoints: alpha=3 lies strictly inside (2,4); page 4 explicitly says the new unified proof covers alpha=3, which was missing from the older argument.
- Moment propagation: the elementary bound above ensures that (2) is legitimate at every finite time.
- Cancellation: (2) is an exact polynomial identity. We never replace a difference of asymptotic equivalents by the difference of their leading terms.
- Barrier direction: the estimate applies BELOW the barrier and makes the gap strictly more negative. Persistence plus b_k->0 contradicts nonnegativity; summability of the decrement does not obstruct this because a fixed strictly negative gap already suffices.
- Product indices: both Q_n in the theorem and here contain indices 0 through n-1. Omitting finitely many factors in the lower bound is valid since G_i(2)>=1.
- Imported theorem proof: inspected pages 20–21, with truncated weighted third moment c(3n-1) for our law. The lower half of Theorem 1.1 is not needed.
- Numerical checks: check_exact.py tests the scalar identity and barrier inequality with rational arithmetic; checks.txt records counts and normalization approximations. These are supplementary checks, not evidence for a survival limit.
- Lean: Barrier.lean checks the exact polynomial identity and the one-step barrier estimate using ring and nlinarith, with specific Mathlib imports. lean_check.txt records the actual command and exit status. No sorry, axiom, or native_decide is used. This checks the algebra only, not the external theorem or the infinite-sequence proof.

## 8. Scope and remaining questions

There is no remaining gap in the counterexample to the question as posed, conditional only on the cited published theorem as a standard external input. This does not determine the actual survival asymptotic for the constructed law. The heavy-tail coefficient 3/2 predicted in the 2021 paper remains a conjecture here. The conjecture strengthened by E[X_0^3 m^{X_0}]<infinity is not refuted or proved by this argument, and the bounded literature search did not locate its resolution.

## Final verification record

The final Lean run returned exit code 0 in 105.18 seconds. Earlier attempts failed due to a UTF-8 BOM and a missing Mathlib.Data.Real.Basic import; both were corrected before the successful run. Both theorems in Barrier.lean now pass kernel checking. The numerical script passed 4,200 exact rational cases and 50-digit normalization and criticality checks.
