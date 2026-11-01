# R11 I0054 idea before code — explicit inversive-orbit derandomization

Model requested by owner: GPT-6 maximum. Actual runtime in this invocation: GPT-5.6 Sol; reasoning level UNVERIFIED.

Target: Aldous–Janson arXiv:2303.02529v3, Open Problem 18. Current frozen author-side model-class metric recovered from the newest complete R11 report: 69.

Methods for this run: #10 DERANDOMIZE, #16 COMPUTE SMALL CASES, #21 ASK WHO ELSE HAS THIS SHAPE.

## Candidate route

The preceding C069 model chooses, by the probabilistic method, a rank permutation whose cyclic translates make every fixed visible split test look asymptotically independent. Replace that existential ranking by the explicit algebraic permutation

    inv_p(x) = x^{-1} mod p for x != 0, and inv_p(0)=0

on the prime field F_p, with p=p_N the least prime >= N. For every threshold 1<=u<p and translation t in F_p, a label ell is red iff the standard representative inv_p(t+ell) lies in {0,...,u-1}; give this proposal clock rate 1/(2u(p-u)).

For fixed distinct visible offsets a_1,...,a_m, the translated m-tuples

    (inv_p(t+a_1),...,inv_p(t+a_m)),  t in F_p,

are the classical shifted-inversive pseudorandom point set. For every nonzero Fourier frequency h, the exponential sum is an additive-character sum of the rational function

    R_h(X)=sum_j h_j/(X+a_j).

Distinct offsets give distinct simple poles, so R_h is nonconstant whenever h is nonzero modulo p. Weil's rational-function bound plus Erdős–Turán–Koksma should give fixed-dimensional star discrepancy

    D_p^(m) = O_m(p^{-1/2}(log p)^m).

A threshold split box [0,u/p)^A x [u/p,1)^B is a signed union of at most 2^m anchored boxes. Therefore the difference between its translation count and p times the product volume is O_m(p D_p^(m)). Summing with weights 1/(2u(p-u)) costs only H_{p-1}; hence every specified i|j split rate differs from the beta integral B(i,j) by

    O_m(D_p^(m) log p) + o(1)
      = O_m(p^{-1/2}(log p)^{m+1}) + o(1).

If this calculation closes, exact hidden-label lumpability gives finite-state generator convergence on every fixed [k], then bounded-interval path total-variation convergence by uniformization, hence J1 and the projective CTCS(infinity) limit.

## Why #21 is relevant

This is the same finite-field inversion mechanism studied in the inversive-congruential pseudorandom-number literature. The discrepancy/exponential-sum machinery is classical prior art; the candidate new claim is only the CTCS-specific compiler/application.

## Small-case test to run (#16)

1. Verify inv_p is a permutation and every pair of leaf offsets is separable.
2. Exhaustively compute exact split-rate multisets for small N with p_N the least prime >= N.
3. Compare with the source CTCS split rates and with C069's recorded N=4 multiset {0,1/4,1/4} for balanced splits.
4. Do not count a new class unless an exact relabeling/time-rescaling invariant distinguishes it from both the source model and the retained neighboring class.

No code has been written for this run before this note.