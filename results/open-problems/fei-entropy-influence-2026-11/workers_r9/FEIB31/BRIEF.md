# Worker FEIB31 (account acc2)

disk: small

# FEIB31 - monotone functions: does every monotone Boolean function have a good coordinate?

Launched by an agent (laptop) for the author's 9 Nov 22:20 ask: solve the Fourier Entropy-Influence
conjecture. Everything you need is in this brief; background is ~/fei_solve_agent/FLOW.md sections 12(u)-12(z).
Code: ~/fei_solve_agent/code/predictor.py (fast Walsh transform, families), mono_hidden.py, sym_enum.py.
`export PATH=/opt/homebrew/bin:/usr/local/bin:$PATH`; python3 has numpy. There is no math store on this machine.

Setting. f Boolean (+-1) on n bits, mu(S) = fhat(S)^2, I = total influence. For a coordinate i:
g = E_i f (average over x_i), h = D_i f = (f(x^{i->1}) - f(x^{i->-1}))/2, Inf_i = E h^2,
p_T = ghat(T)^2 = mu(T), q_T = hhat(T)^2 = mu(T+i) for T not containing i,
    E_i = sum_T Phi(p_T, q_T),  Phi(p,q) = (p+q) h2(p/(p+q)),     rho_h(T) = q_T / Inf_i,
    Lam_i = E_{T ~ rho_h} log2(1 + p_T/q_T),        Lam_i <= E_i/Inf_i <= Lam_i + 1/ln 2.
Tree identity H(f) = (1/2) H(f_0) + (1/2) H(f_1) + J_i + E_i with J_i <= (2/ln 2) Inf_i gives:
if EVERY function in a restriction-closed class has a coordinate with E_i <= G Inf_i, then H <= (G + 2/ln 2) I on
the class. Monotone functions are restriction-closed, and FEI for monotone functions is open. So:
    QUESTION M:  is  G_mon := sup over monotone f of  min_i E_i/Inf_i  finite?
Known: the largest value found over all functions is 4.50505 (a non-monotone tower); over monotone functions with
at most 6 variables and width-2 tribes it is 3.606847 (the OR of eight disjoint 2-clauses). A SINGLE coordinate can
be arbitrarily bad even for monotone f (a "hidden" coordinate that matters only on a small set B: ratio about
log2(1/Inf_i)); the claim is only about the best coordinate.
Monotone structure: h = 1_B (indicator of the boundary set B in the other n-1 coordinates: points where x_i is
pivotal), Inf_i = |B|/2^(n-1) = fhat({i}) up to sign. With A_+ = {y: f = +1 whatever x_i}, A_- = {y: f = -1
whatever x_i}, a = transform of 1_{A_+}, b = transform of 1_{A_-}: for T nonempty ghat(T) = a(T) - b(T) and
hhat(T) = -(a(T) + b(T)); at T empty ghat = |A_+| - |A_-|, hhat = |B| (densities). So a coordinate is good when,
on the spectral mass of 1_B, the transforms of the up-set A_+ and the down-set A_- do not nearly cancel in a + b
while adding in a - b. At level one a and b have opposite signs coordinatewise (A_+ is an up-set or down-set and
A_- the other kind), so |a - b| >= |a + b| there: level-one mass of 1_B is always expensive, higher levels can be
cheap.

The job, in order.
1. Adversary. Maximise min_i E_i/Inf_i over monotone functions: (a) exact hill-climb at n = 8..13 (moves: add or
   remove a minimal term / flip a boundary point keeping monotonicity), many starts (random DNFs of mixed widths,
   thresholds, tribes with unequal widths, monotone towers, perfect-matching and other graph properties on small
   graphs: connectivity, triangle, k-clique, Hamiltonicity on K_4, K_5, K_{3,3}); (b) transitive monotone
   functions (every coordinate is equivalent, so min = any): cyclic monotone DNFs at n = 12..20 with exact
   transforms, graph properties on K_5 (10 edges), K_6 (15), K_{3,3}, K_{4,4} (16), recursive tribes/majority
   towers by the composition law (E_i/Inf_i of a tower is computable from the base); (c) the hidden-coordinate
   construction made symmetric - can ALL coordinates be made hidden at once in a monotone function? This is the
   crux: a bad coordinate needs B small and structured relative to A_+, A_-; all coordinates bad at once seems to
   fight monotonicity (KKL: some influence is at least c log n / n times the variance; Talagrand).
   Report the record with the DNF.
2. Proof attempts for the best coordinate, in this order: (a) the max-influence coordinate - is it always good
   for monotone f? (test first; for general f it is known to fail); (b) the coordinate minimising
   E_{rho_h}[log2(p/q)]_+ ; (c) an averaging argument: sum_i Inf_i Lam_i <= C I restricted to monotone f is the
   monotone FEI itself - instead look for a weighting w_i with sum_i w_i E_i <= C sum_i w_i Inf_i provable by
   level inequalities for the indicator 1_B (hhat is the transform of a set of density Inf_i: its level-k weight is
   at most Inf_i^2 (2e ln(1/Inf_i)/k)^k) together with the identity sum_i hhat_i(T) = (|T|+1)-fold counting of
   mu(T+i); (d) submodularity / FKG: for monotone f the spectral sample has known positive-association-type
   properties at level 1 (fhat({i}) = Inf_i >= 0) - anything usable at higher levels?
3. Classes: prove Question M with an explicit G for (i) monotone DNFs of width at most w (G = O(w)? or better),
   (ii) read-once monotone formulas, (iii) monotone functions with I <= K sqrt(log n)... whichever falls.
   A complete proof for a new class is worth more than a survey.
4. Literature check before any novelty claim: FEI for monotone/unate functions (O'Donnell-Wright-Zhou for
   symmetric; Chakraborty-Kulkarni-Lokam-Saurabh; Shalev arXiv:1806.03646; Kelman et al. arXiv:1911.10579;
   Arunachalam et al. arXiv:1809.09819 on unate FMEI), and "min-entropy for monotone functions is easy because
   fhat({i}) = Inf_i". State exactly what is known for monotone f and where Question M stands relative to it.

Rules: one compute process at a time, at most 2 threads, nice 10, under 3 GiB; before any run longer than a
minute read `uptime` and use 1 thread if the 1-minute load is above 9. Folder under 60 MB (this disk is at its
floor: keep tables in memory, delete scratch as you go). Mark each statement PROVED, CHECKED NUMERICALLY (with
the command) or HEURISTIC. RESULTS.md as you go; REPORT.md at the end, verdict first (largest monotone value with
its function / what is proved / what blocks the proof).

