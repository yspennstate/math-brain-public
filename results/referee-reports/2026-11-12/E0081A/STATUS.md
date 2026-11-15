# E0081A status (2026-11-12 23:05 laptop clock)

Problem: Pitman-Tang (arXiv 1411.0041) Question 1.7 / open problem 2.3(2): order of E T(FP_{lambda,n}), fixed lambda<0.
Known before: c n <= E T <= C n^{5/4}. Peres conjectured n log n (Tang 2017 thesis, Conj. 2.5.2; published chapter Conj. 1).

Codex run E0081A (gpt-6.1-sol, high, Mac mini 1) reports PROVED: c n log n <= E T_n <= C n log n.
- Upper bound on block-hit probability C/log n: three-piece decomposition plus a strong-Markov range bound for
  X - Y at strict descending record times of Y (O(sqrt n) record visits, return potential ~ log n / (2 pi)).
- Lower bound c/log n: exact conditional overlap f_s(-w(s)) <= C/s, then first-success / second moment.
- Also: matching-matrix column sums O(log n) instead of O(n^{1/4}).

Checked by an agent line by line (Lemmas 2-6 and the deduction): no gap found. Open point: the source's
Table 1 (about 1.8 n) disagrees with the run's Monte Carlo (4.16 n at n=100, lambda=-1); convention not settled.

REFEREED MINOR by E0081AR (13 Nov): proof correct; five fixes: (4) needs k integer; state endpoint rounding (floor, parity +1; n=1000 lambda=-1 gives a=32 not 30); Table 1 convention (source (2.4) is ending time; every Table 1 value is below the exact lower bound 1/f_n(a), so the source table is wrong); credit source (2.21) for the overlap count; fix file paths. Handed to an agent for the paper.
