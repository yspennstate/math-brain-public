# Worker FEIB27 (account acc2)

disk: small

# FEIB27 - find the inequality: linear-programming search for a local bound on the erasure entropy

Launched by an agent (laptop) for the author's 9 Nov 22:20 ask: solve the Fourier Entropy-Influence
conjecture. Read ~/fei_solve_agent/FLOW.md sections 12(u) (with its correction block), 12(v), 12(w); code
~/fei_solve_agent/code/step_info.py, relative_step.py, han_refine.py, mono_hidden.py
(`export PATH=/opt/homebrew/bin:/usr/local/bin:$PATH`).

Setting. f Boolean (+-1), mu(S) = f^(S)^2, U ~ mu, I = E|U|, H = H(mu). g = E_i f, h = D_i f, Inf_i = E h^2 = delta_i,
p_T = g^(T)^2, q_T = h^(T)^2, E_i = H(1[i in U] | U - i) = sum_T Phi(p_T, q_T), Phi(p, q) = (p + q) h2(p/(p + q)).
J_i = Jensen-Shannon divergence of the spectra of the two restrictions, J_i <= (2/ln 2) Inf_i.
Tree identity: H(f) = (1/2) H(f_0) + (1/2) H(f_1) + J_i + E_i. Equivalent forms of FEI (constants within 2/ln 2):
   (A) sum_i E_i <= C I for every f;      (G) every f has a coordinate with E_i <= C Inf_i;
   (T) there is a functional Theta >= 0 with Theta(f) <= C I(f) and, for every f, SOME i with
       E_i(f) + J_i(f) <= C Inf_i(f) + Theta(f) - (1/2) Theta(f_0) - (1/2) Theta(f_1)     (a supersolution).
Known supersolution: Theta = sum_j Inf_j log2(1/Inf_j) (Han, arXiv:2312.08271), which is not O(I).
FLOW 12(w) item 3 shows no Theta built from (Var, influences) alone can work (tribes). The exact step cost is
delta E_{rho_h}[log2(p/q)]_+ up to 2.45 delta: a coordinate is expensive exactly when, where h^ has its mass, g^ is
much larger pointwise.

The job: find, by computation, WHICH inequality is true, then try to prove it. Three searches.

1. Form (A) with a local right side. Build a census: all NPN classes at n <= 5; all monotone functions at n <= 6;
   10^4 random functions and random DNFs at n = 6..10; towers and the named functions of FLOW (tribes, PM(K33),
   hidden coordinate 12(u), pendant graph 12(v) item 4, thresholds, TD(w, Q) at small parameters, bent functions).
   For each f and i compute E_i and a dictionary of candidate nonnegative local terms t_k(f, i) whose sums over i
   are O(I) by construction, for example:
     Inf_i;  f^({i})^2;  sum_{S ni i} mu(S)/|S|  (sums to Var);  sum_{S ni i} mu(S) min(1, c/|S|);
     sum_j Inf_{ij}-type second-order influences normalised so that the double sum is at most I (say
     sum_{S ni i,j} mu(S)/(|S| - 1));  noise-stability differences at coordinate i (Inf_i^{(rho)} for a few rho);
     Inf_i log2(Var/Inf_i)_+ is NOT allowed (it does not sum to O(I)), but Inf_i log2(1 + M_i/Inf_i) with
     M_i = sum_{S ni i} mu(S)/|S| is worth a test;  E|h| , E|g| - type L1 quantities;  P[i in U, |U| <= r]/1.
   Solve the LP: minimise C subject to E_i(f) <= sum_k c_k t_k(f, i) for all (f, i) in the census, c_k >= 0,
   with C = the implied constant in sum_i E_i <= C I. Report which small subsets of terms are feasible on the
   whole census and with what constant; then attack each survivor with adversarial search (hill-climb the
   violation) until it breaks or survives 10^6 functions. A per-coordinate inequality that survives is a
   conjecture worth proving; also test the summed form only (sum_i on both sides), which is weaker.
2. Form (T). Same census, closed under restrictions (add all restrictions of the census functions). Candidate
   Theta: nonnegative combinations of functionals that are O(I): I itself, Var, sum_S mu(S) log2(1 + |S|) (not
   O(I), include it as a control), sum_i Inf_i^2-type, H^{(1)} = entropy of the level sizes, sum_S mu(S) |S| 2^-|S|,
   spectral entropy of the "skeleton" (U coarsened to blocks of a fixed partition) ... and min over i. LP: is
   there Theta in the span with the supersolution inequality for the best i at every census function? Report
   feasibility and the constant. Negative results with the explicit violating function are useful.
3. The pointwise ratio. For the census, tabulate the law of log2(p_T/q_T) under rho_h for the BEST coordinate and
   for the WORST; look for a structural statement that holds for the best coordinate of every census function
   (e.g. "at least half of the rho_h mass has p <= K q"; "E_{rho_h}[log2(p/q)]_+ <= K"), find the extremal
   functions, and say what they look like.
4. If a survivor of 1 or 2 has a proof by a known tool (hypercontractive level inequalities for h, which has
   support of measure delta; f * f = delta; g^ * h^ = 0; Shearer; log-Sobolev), write it, every step.

Rules for this brief: 2 threads, nice 10, under 3 GiB a process; folder under 150 MB (the disk on this machine is
near its floor: keep the census in memory or in one compact file, delete scratch as you go). Mark each statement
PROVED, CHECKED NUMERICALLY (with the command) or HEURISTIC. RESULTS.md as you go; REPORT.md at the end, with the
table of feasible term sets first.

