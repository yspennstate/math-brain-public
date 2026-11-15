# Worker FEIB22 (account acc2)

disk: small

# FEIB22 - percolation: is E_i/Inf_i bounded on hex crossings, and which witness sees it

Launched by an agent (laptop) for the author's 9 Nov 22:20 ask: solve the Fourier Entropy-Influence
conjecture. Read ~/fei_solve_agent/FLOW.md sections 7, 12 (head, (l)), 12(o), 12(p); code
~/fei_solve_agent/code/mc_chain.py (class for `hex:L`, the resampling estimators W and V, `selftest`), results
in ~/fei_solve_agent/mc_run/*.json and out_*.txt (`export PATH=/opt/homebrew/bin:/usr/local/bin:$PATH`).

Setting. f Boolean (+-1), mu(S) = f^(S)^2, U ~ mu (the spectral sample), g = E_i f, h = D_i f, delta = Inf_i.
E_i = H(1[i in U] | U - i); FEI <=> every f has a coordinate with E_i <= C delta. Any statistic S of U - i gives
the upper bound H(1[i in U] | S(U - i)) >= E_i. The nested witness (S = last revealed element of U - i along an
order; computed from the resampling correlations W(R) = E h(x) h(x^R), V(R) = E g^2 - E g(x) g(x^R) along a chain
of sets R) gives, for i the centre hexagon of an L x L hex board and R = balls around i:
    L = 12: 4.10    L = 16: 4.270    L = 24: 4.440     (ratio L/Inf; trivial bound 5.5, 6.0, 6.7; 32..96 running)
It creeps up 0.17 a step. On tree-like DNFs the same creep was the witness, not the function (12(p)): the true
E_i/Inf was 2 while the nested witness grew like log D, and conditioning on the last TWO elements fixed it.

Your job: find out which it is for percolation.
1. Block witness. For a set B of hexagons not containing i, H(1[i in U] | U cap B) >= E_i, and the joint law of
   U cap (B + i) is the average over the outside configuration y of the spectral measure of the restricted
   function f_y on B + i. Estimate it by sampling y and taking the exact Walsh-Hadamard transform on the 2^(|B|+1)
   table (|B| up to 16-18). The plug-in estimate of sum_S Phi(p_S, q_S) is biased DOWN (Phi is concave), so report
   it with a bias check: split-sample estimates at several sample sizes and extrapolate, or a bias-corrected
   estimator; never report an unchecked plug-in number as an upper bound. Take B = the ball of radius r around i
   for r = 1, 2 (6 and 18 hexagons), boards L = 8, 12, 16, 24.
2. Window witness in resampling form. P[i in U, k in U, U misses R] = E D_k h(x) D_k h(x^R) and the same with g,
   so the last-two witness for the ball chain can be estimated with second derivatives. Implement it (reuse the
   hex evaluator of mc_chain.py), validate on a small board against the exact spectrum (L <= 4 has 16 hexagons),
   and run L = 12, 16, 24.
3. Exact small boards: for L = 3, 4 (9 and 16 hexagons) compute E_i/Inf_i exactly for every hexagon and the
   best nested and last-two witnesses; for L = 5 (25) do it if memory allows (2^25 doubles is 256 MB: fine).
4. Read what is known about the spectral sample of percolation near a point (Garban-Pete-Schramm, "The Fourier
   spectrum of critical percolation"; their conditional statements on the sample in a box given it is non-empty
   in a neighbourhood) and say what it predicts for H(1[i in U] | U - i)/Inf_i as the board grows: bounded, or
   growing like log L? One neutral clause of attribution per fact; mark predictions as predictions.
5. Report a table: L, Inf, nested witness, last-two witness, block witness r = 1, 2 (with bias checks), and the
   exact E_i/Inf_i where available; then one paragraph: is the creep the witness or the function.

Rules for this brief: 2 threads, nice 10, under 3 GiB a process; folder under 200 MB. Every number with its
command and its standard error. RESULTS.md as you go; REPORT.md at the end.

