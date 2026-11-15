# Worker FEIB24 (account acc2)

disk: small

# FEIB24 - monotone functions: exhaustive erasure ratios, which coordinate is good, and a charging argument

Launched by an agent (laptop) for the author's 9 Nov 22:20 ask: solve the Fourier Entropy-Influence
conjecture. Read ~/fei_solve_agent/FLOW.md sections 7 (all), 11 (head, (c)), 12(q), 12(s), 12(t), 12(u); code
~/fei_solve_agent/code/mono_hidden.py and mono_hidden_comp.py (exact E_i and Inf_i from a truth table)
(`export PATH=/opt/homebrew/bin:/usr/local/bin:$PATH`).

Setting. f Boolean (+-1), mu(S) = f^(S)^2, U ~ mu, I = E|U|, H = H(mu). g = E_i f, h = D_i f, Inf_i = E h^2,
E_i = H(1[i in U] | U - i) = sum_T Phi(g^(T)^2, h^(T)^2), Phi(p, q) = (p + q) h2(p / (p + q)). Facts (FLOW 7, 12(u)):
 - sum_i E_i <= H (Han), and H(f) = (1/2) H(f_0) + (1/2) H(f_1) + J_i + E_i with J_i <= (2/ln 2) Inf_i. So FEI
   <=> sum_i E_i <= C I for all f <=> every f has a coordinate with E_i <= C Inf_i, and
   sup_f min_i E_i/Inf_i = sup_f H/I (>= 6.5218).
 - For any decision tree reading all variables, H(f) = sum_v P(v) (E + J)(v), I(f) = sum_v P(v) Inf(v): one tree
   with sum_v P(v) E(v) <= C I(f) gives FEI for f; bad nodes may be paid for by other nodes.
 - E_i / Inf_i = log2(1/Inf_i) - D(pi_h || nu) + O(1), pi_h = h^2-spectrum normalised, nu = law of U - i. A
   coordinate is good exactly when, for typical T ~ pi_h, g^(T)^2 <= K h^(T)^2.
Monotone functions are closed under restrictions, so "every monotone f has a good coordinate" is equivalent to
FEI for monotone functions, which is open as far as I know (check).

Known examples for monotone f.
 - MAJ_k: E_i = 0 at every coordinate (g odd, h even: disjoint supports).
 - Hidden coordinate (12(u)): f = MAJ_k(y) OR (x AND [y >= y0]), |y0| = (k-1)/2. Inf_x = 2^-k,
   E_x/Inf_x = 3.52, 4.24, 4.99, 5.78, 6.62, 7.48, 8.37, 9.27 at k = 3..17 (about k/2), while the y variables have
   E/Inf -> 0. x is in a shortest term. Composing each y_j with MAJ_m leaves E_x, Inf_x unchanged (checked) and
   makes x the largest-influence coordinate. So neither "largest influence" nor "any variable of a shortest term"
   is a rule, even for monotone f.
 - Critical percolation crossings: bulk sites are good (12(t)), by a chain of scales.
 - Thresholds: every threshold function has a good coordinate (section 11).

Tasks.
1. Exhaustive. All monotone functions on n <= 6 variables up to permutation (16,353 classes at n = 6; n = 7 by
   sampling and by hill-climbing inside the monotone class). Exactly: G_mono(n) = max_f min_i E_i/Inf_i,
   max_f H/I, max_f (sum_i E_i)/I, and the extremal functions (as DNFs). Compare with the unrestricted maxima at
   the same n if cheap (n <= 5 exhaustive over all NPN classes). Does G_mono(n) look bounded? What do the
   extremal functions look like?
2. Which coordinate. On the n = 6 census, test rules that pick a coordinate from simple data and report the worst
   ratio E_i/Inf_i each rule ever picks: largest influence; smallest influence; variable in the most shortest
   terms; variable maximising Inf_i^2 / mu({i})... (for monotone f, f^({i}) = +-Inf_i, so use other statistics:
   level-2 weight through i, W_i^{(2)} / Inf_i; the "private mass" P[i in U, |U| = 1] / Inf_i = Inf_i); variable
   minimising E_i / Inf_i among those of a minterm AND a maxterm of least size. Find a rule that never picks worse
   than a fixed constant on the census, then try to break it with constructions like 12(u) and compositions.
3. Hunt for a bad monotone function. Hill-climb and construct (compositions, tribes of hidden-coordinate gadgets,
   towers) to maximise min_i E_i/Inf_i over monotone f for n up to 20 or so. Report the record and the function.
   The unrestricted record is 6.5218 in the limit (towers of the perfect-matching function of K33, not monotone
   in the usual sense - check whether a monotone function reaches above 4).
4. Charging. For the hidden-coordinate family and its compositions, exhibit the tree (or just the sum over i)
   in which the bad coordinate is paid for, and try to prove a general statement of this kind for monotone f:
   e.g. sum_i E_i <= C sum_i Inf_i using sum_i Inf_i^2 <= 1 and f^({i}) = Inf_i, or a bound
   E_i <= C Inf_i + (something summable against I). Every step written. A clean lemma that is true on the whole
   n = 6 census and proved is worth more than a broad heuristic.
5. Literature, one neutral clause each, only from sources you can open: what is known about FEI or Fourier
   min-entropy for monotone functions, and for DNFs.

Rules for this brief: 2 threads, nice 10, under 3 GiB a process; folder under 200 MB. Proofs go in PROOFS.md with
every step written; mark each statement PROVED, CHECKED NUMERICALLY (with the command) or HEURISTIC. RESULTS.md as
you go; REPORT.md at the end.

