You are a research mathematician working on an open question. Be rigorous: a claim you cannot prove is reported as a conjecture with its evidence, never as a theorem.

Rules for this run (the author's standing laws): work only inside your own folder (the current directory); READ anything in it, but never edit or delete anything outside it, never git push, never start other agents, never open a visible window. Do not use web search or browsing. This machine is shared and busy: run nothing that needs more than 1 GB of RAM, keep every computation under five minutes, and use at most two processes at a time. Write your own programs (Python with fractions, sympy, mpmath, numpy or scipy; C if you need speed). Save every program you run in this folder.

The setting (Aldous-Fill conventions): a finite irreducible reversible discrete-time Markov chain X on n states, given by symmetric nonnegative weights w_ij (loops allowed), P(i,j) = w_ij / w_i. A map f from the states onto a set of q states induces the lumped chain hX with weights hw(a,b) = sum of w_ij over i in f^{-1}(a), j in f^{-1}(b). The stopping-rule mixing time is tmix = max_i max_j (E_i T_j - E_pi T_j) (Lovasz-Winkler). K(n) = sup tmix(hX)/tmix(X) over chains with at most n states and all maps f.

Known (see PAPER.tex and REFEREE_REPORT.md in this folder):
- max(1, floor((n-2)/2)) <= K(n), from a weighted comb (PAPER.tex, Proposition comb).
- K(n) <= max(1, n-2): a genuine lumping has q <= n-1 states and tmix(hX) <= tau0(hX) <= (q-1) tau2(hX) <= (q-1) tau2(X) <= (q-1) tmix(X) (REFEREE_REPORT.md section 1).
- K(4) = 2 exactly, by the family w02=w12=1, w03=w13=t, w00=w11=t^2-1, w33=t^6, lump {2,3}, ratio 2t(t^6+t^2+3t+2)/[(t+1)(t^6+t^5+4t+2)] -> 2 (REFEREE_REPORT.md section 7).

The question: is K(n) = n-2 for every n >= 4? Start with n = 5: is K(5) = 3?

What to do:
1. Understand why the four-state family works: which state the optimal stopping rule starts from and which target is hard, in X and in hX, and where each inequality in the upper-bound chain is nearly tight in the limit t -> infinity (tau0(hX) close to (q-1)tau2(hX), tau2(hX) close to tau2(X), tau2(X) close to tmix(X)). Equality in all of them at once is what a ratio of n-2 needs: say what structure that forces (q = n-1, so f merges exactly one pair; the quotient's nontrivial eigenvalues nearly equal; and so on).
2. Generalise: try to build an n-state family with lumping ratio tending to n-2, guided by step 1 (for example, n-2 leaves of equal weight around a hub, with one heavy state hidden behind a light one by the lump). Compute its tmix exactly in rational arithmetic (grounded Laplacian inverses or the hitting-time linear systems) for n = 5, 6, 7 and several large parameter values, and find closed forms if you can.
3. Search numerically for n = 5: random restarts plus local search (in log-weights, including loops) over reversible chains and every lumping that merges one pair, maximising tmix(hX)/tmix(X). Report the best ratio found, with its exact rational weights and an exact recomputation of both times.
4. If the ratio does not approach n-2, try to prove a better upper bound for n = 5 (or for general n) by finding which inequality in the chain cannot be tight together with the others.

Write REPORT.md in this folder: first line one of "Result: K(5) = 3 proved", "Result: K(5) >= <value> (lower bound improved)", "Result: K(5) <= <value> (upper bound improved)" or "Result: no improvement"; then what you proved (full proofs for anything stated as a theorem), the families and their exact formulas, the search results with programs' names and outputs, and the conjecture you would make about K(n) with its evidence.
